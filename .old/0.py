from abc import ABC, abstractmethod
import asyncio
from multiprocessing import Queue
from typing import Generic, TypeVar, Any

import tree
from networkx.classes.multidigraph import MultiDiGraph
import networkx as nx


T_obs = TypeVar("T_obs")
T_act = TypeVar("T_act")


class Node(ABC):
    _ports: dict[str, Queue]
    
    @property
    def ports(self) -> list[str]:
        return list(self._ports.keys())
    
    def get(self, port: str) -> Any:
        return self._ports[port].get()
    
    def set(self, port: str, value: Any):
        self._ports[port].put(value)


class InputNode(Generic[T_obs], Node, ABC):
    @abstractmethod
    async def get_obs(self) -> T_obs:
        pass


class OutputNode(Generic[T_act], Node, ABC):
    @abstractmethod
    async def set_action(self, action: T_act):
        pass


class ProcessorNode(Node, ABC):
    @abstractmethod
    async def process(self):
        pass


T_obs_i = TypeVar("T_obs_i")
T_action_i = TypeVar("T_action_i")


class CompositeNode(
    Generic[T_obs, T_act, T_obs_i, T_action_i],
    InputNode[T_obs],
    OutputNode[T_act],
    ProcessorNode,
    ABC,
):
    connectivity: MultiDiGraph
    obs_structure: tree.Structure[T_obs_i] | None = None
    action_structure: tree.Structure[T_action_i] | None = None

    @property
    def _obs_structure(self) -> tree.Structure[T_obs_i]:
        if self.obs_structure is None:
            self.obs_structure = [None] * len(self.sensors)
        return self.obs_structure

    @property
    def _action_structure(self) -> tree.Structure[T_action_i]:
        if self.action_structure is None:
            self.action_structure = [None] * len(self.actuators)
        return self.action_structure

    @property
    def nodes(self) -> list[Node]:
        return list(self.connectivity.nodes)

    @property
    def sensors(self) -> list[InputNode]:
        input_flattened = [node for node in self.nodes if isinstance(node, InputNode)]
        return tree.unflatten_as(input_flattened, self.obs_structure)

    @property
    def actuators(self) -> list[OutputNode]:
        return [node for node in self.nodes if isinstance(node, OutputNode)]

    @property
    def processors(self) -> list[ProcessorNode]:
        return [node for node in self.nodes if isinstance(node, ProcessorNode)]

    @abstractmethod
    async def get_obs(self) -> T_obs:
        flat_obs = await asyncio.gather(*[sensor.get_obs() for sensor in self.sensors])
        return tree.unflatten_as(flat_obs, self._obs_structure)

    @abstractmethod
    async def set_action(self, action: T_act):
        flat_action = tree.flatten(action)
        for actuator_i, flat_action_i in zip(self.actuators, flat_action):
            await actuator_i.set_action(flat_action_i)
    @abstractmethod
    async def process(self):
        # Determine the processing order of nodes based on the connectivity
        processing_order = list(nx.topological_sort(self.connectivity))
        
        # Process all nodes in the determined order
        for node in processing_order:
            if isinstance(node, ProcessorNode):
                await node.process()
        

class Brain(CompositeNode, ABC):
    pass


class