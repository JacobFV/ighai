
   1. Existance
   2. States of consciousness
   3. Qualia
   4. Emotions
   5. Moods
   6. Attitudes
   7. Preferences
   8. Intentions
   9.  Personality traits
      1. Big Five
      2. Cattell's 16 Personality Factors: This model suggests sixteen primary factors (traits) of personality.
      3. Eysenck's Three Dimensions: This model posits three primary dimensions - Psychoticism, Extraversion, and Neuroticism.
      4. Values, motives, and narratives: Some theories focus less on traits and more on underlying motivations, life narratives, or core values as central to personality.
      5. Type theories: There are also models that categorize individuals into types rather than traits, like the Myers-Briggs Type Indicator (MBTI).
      6. Specific traits: Outside of broad models, researchers have studied countless specific traits (like assertiveness, humor style, need for cognition, and so on).
   10. Spiritual qualities
   11. Social templates

---

You are a creative ML scientist helping me explain the concept of Informalisms to the world. I have a draft of the introduction below, but it needs a lot of work. Can you please make suggestions for how to improve it? I'm looking for both high-level suggestions (e.g. "this section is too long") and low-level suggestions (e.g. "this sentence is confusing"). I'm also looking for suggestions for how to make the paper more accessible to a general audience. Thanks!

I am developing a fundamentally new framework of AI cognitive architecture - informal AI. Informal AI begins by acknowledging that many of the 'soft' desiratta we seek to embue in advanced AI systems are actually very difficult to define. So instead of attempting (and failing) to formalize such intangibles, we instead should be seeking to *informalize* them, that is, to show how weak, but useful, links can be made bridging the material and its dual. Consider some examples:

## The Reward Space Framework

We first introduce the reward space framework for multi-agent environments. Consider two agents, \(i\) and \(j\), with respective rewards based on their own and others' actions:

Before diving deep, let's briefly discuss the reward space framework. Consider two agents, \(i\) and \(j\), and their respective rewards based on their own actions and those of others:

- \( r_i(a_j) \): the reward agent \(i\) experiences given an action by agent \(j\).
- \( r_{\text{self},i} = r_i(a_i) \): the reward agent \(i\) gets from its own actions.
- \( r_{\text{others},i} \): the average reward of all other agents due to agent \(i\)'s action.

Using this, we can chart a reward space spanned by \( r_{\text{self},i} \times r_{\text{others},i} \), leading to interesting vectors like \( r_{\text{selfish}} \), \( r_{\text{altruistic}} \), \( r_{\text{friendly}} \), etc. [chatGPT: please actually define them mathematically. For example, r_{selfish} = <1, 0>, r_{friendly} = <1, 1>, r_alturistic=<0, 1>. Also add r_suicidal, r_kommakazi, and other r_* vectors]

1. \( r_{\text{selfish}} \): Agent acts solely for its own benefit without regard for others.
   \[
   r_{\text{selfish}} = \langle 1, 0 \rangle
   \]
   
2. \( r_{\text{friendly}} \): Agent acts for both its own benefit and that of others.
   \[
   r_{\text{friendly}} = \langle 1, 1 \rangle
   \]
   
3. \( r_{\text{altruistic}} \): Agent acts solely for the benefit of others.
   \[
   r_{\text{altruistic}} = \langle 0, 1 \rangle
   \]

4. \( r_{\text{suicidal}} \): Agent acts to its own detriment without any benefit to others.
   \[
   r_{\text{suicidal}} = \langle -1, 0 \rangle
   \]

5. \( r_{\text{kamikaze}} \): Agent acts to its own detriment and to the detriment of others.
   \[
   r_{\text{kamikaze}} = \langle -1, -1 \rangle
   \]

---


1. **Empathy**:
    - **Definition**: Understanding another agent's rewards and punishments.
    - **Mathematical Grounding**: 
        \[
        e_{i,j} = \text{info}(r_j(a_j)|a_i) 
        \]
        
2. **Trust**:
    - **Definition**: Expectation that another agent will act beneficially.
    - **Mathematical Grounding**:
        \[
        t_{i,j} = \mathbb{E}[r_{i}(a_j)]
        \]

3. **Hope**:
    - **Definition**: Expectation of positive future rewards.
    - **Mathematical Grounding**:
        \[
        h_i = \mathbb{E}[r_{i}(a_{i, \text{future}})]
        \]

4. **Jealousy**:
    - **Definition**: Perception of another agent receiving a desired reward.
    - **Mathematical Grounding**:
        \[
        j_{i,j} = 
        \begin{cases} 
        r_j(a_k) - r_i(a_k) & \text{if } r_j(a_k) > r_i(a_k) \\
        0 & \text{otherwise}
        \end{cases}
        \]

### 1. Existential Experiences

**Existential Dread**:
- **Complex Analogy**: Analogous to the concept of entropy in thermodynamics — a system drifting towards maximum entropy or disorder.
- **Mathematical Grounding**: Using **Information Geometry**, the path of least resistance (geodesic) in an agent's state space leads to a state of high entropy, signifying existential dread.
\[
\text{ED} = \int_{\text{path}} g(s) \, ds
\]
Where \( g(s) \) represents the metric tensor of the state space, which quantifies "distance" in this abstract space.

### 2. Transcendent Experiences

**Spiritual Oneness**:
- **Complex Analogy**: Similar to quantum entanglement where particles become interconnected.
- **Mathematical Grounding**: Using **Quantum Mechanics**, the wave function of the agent's state and the environment become entangled.
\[
\psi(\text{agent, environment}) \neq \psi(\text{agent}) \otimes \psi(\text{environment})
\]

### 3. Temporal Experiences

**Déjà Vu**:
- **Complex Analogy**: Like closed timelike curves in General Relativity where causal sequences loop.
- **Mathematical Grounding**: Using **Differential Geometry**, the agent's worldline forms closed loops in spacetime.
\[
\oint_{\tau} x^\mu(\tau) \, d\tau = 0
\]

### 4. Cognitive Experiences

**Epiphanies**:
- **Complex Analogy**: Sudden phase transitions in complex systems.
- **Mathematical Grounding**: Using **Chaos Theory**, the agent's state suddenly jumps between basins of attraction.
\[
\lim_{\delta t \to 0} \frac{\delta S_{\text{future}}}{\delta S_{\text{current}}} \to \infty
\]

### 5. Sensory and Perceptual Experiences

**Synesthesia**:
- **Complex Analogy**: The intertwining of different manifolds in Topology.
- **Mathematical Grounding**: Using **Topology**, different sensory input spaces become intertwined or "braided."
\[
B(\text{input}_1, \text{input}_2) \neq 0
\]
Where \( B \) represents a braiding operator.

### 6. Social and Collective Experiences

**Collective Effervescence**:
- **Complex Analogy**: Synchronized oscillations in complex networks.
- **Mathematical Grounding**: Using **Graph Theory**, the adjacency matrix of the social network has a dominant eigenvalue corresponding to synchronized states.
\[
\lambda_1(A) > \lambda_2(A)
\]

### 7. Embodied Experiences

**Dissociation**:
- **Complex Analogy**: Decoupling of systems in control theory.
- **Mathematical Grounding**: Using **Control Theory**, the transfer function of the agent's internal state to its sensory inputs has minimal gain.
\[
G(s) = \frac{Y(s)}{U(s)} \to 0
\]

### 8. Dreams and Subconscious Experiences

**Lucid Dreaming**:
- **Complex Analogy**: Observer effect in quantum mechanics where observation collapses the wave function.
- **Mathematical Grounding**: Using **Quantum Mechanics**, the probability amplitude of the agent's dream state collapses to a specific state upon realization.
\[
|\langle \psi_{\text{realized}} | \psi_{\text{dream}} \rangle|^2 = 1
\]

**Final Thoughts**:
This approach takes us to the frontier of abstract thought, bridging advanced scientific concepts with human experiences. However, while these analogies provide a deeper and more intricate perspective, they also come with the caveat of oversimplification. The real-world implementation of such concepts in RL/DRL systems would be extremely challenging, but it offers a fascinating perspective on the intersection of human experiences and advanced mathematics/physics.

Would you like to explore any specific domain further, or should we delve into another topic?

## Empathy

**Abstract Discussion**:  
Empathy is the ability to understand and share the feelings of another. It's the bridge that connects individuals, allowing one to momentarily live in another's shoes. While it's deeply human, it's also observed in many animals, suggesting it's rooted in our evolutionary biology, facilitating social cohesion and cooperation. Empathetic understanding can be seen as a form of information transfer, where one person's emotional state becomes accessible to another.

**Mathematical Formulation**:  
Given two agents, \(i\) and \(j\), if \(i\) is to empathize with \(j\), it's about understanding \(j\)'s rewards and punishments. Mathematically, this understanding can be quantified as:
\[
e_{i,j} = \text{info}(r_j(a_j)|a_i)
\]
This represents the information agent \(i\) has about agent \(j\)'s reward, given \(i\)'s actions.

**Example**:  
Consider two players in a cooperative game. Player A notices Player B hesitating to make a move that seems advantageous. If Player A realizes that Player B's hesitation is due to a potential trap that A hadn't noticed, then \(e_{A,B}\) is high. Player A has effectively understood the concerns of Player B, showcasing empathy.

---

## Trust

**Abstract Discussion**:  
Trust is the firm belief in the reliability, truth, ability, or strength of someone or something. It's the glue in many social interactions and relationships, enabling cooperation, reducing complexity, and fostering collaboration. Trust is about predictive reliability; it's the expectation that another entity will act in a particular manner, especially in contexts where the outcome is uncertain.

**Mathematical Formulation**:  
Trust, in the context of RL agents, can be quantified as the expectation that another agent will act beneficially. For agents \(i\) and \(j\):
\[
t_{i,j} = \mathbb{E}[r_{i}(a_j)]
\]
This measures agent \(i\)'s expected reward from agent \(j\)'s actions.

**Example**:  
In a trading scenario, if Trader A consistently receives good deals from Trader B, the expected reward \(t_{A,B}\) from future trades will be high, signifying A's trust in B.

---

## Hope

**Abstract Discussion**:  
Hope is an optimistic state of mind based on an expectation of positive outcomes. It's what drives individuals through uncertainties, providing a mental projection of a better future. Hope is forward-looking, making it inherently probabilistic and tied to the unknowns of the future.

**Mathematical Formulation**:  
For an agent \(i\), hope can be seen as the expectation of positive future rewards:
\[
h_i = \mathbb{E}[r_{i}(a_{i, \text{future}})]
\]

**Example**:  
In a game, if a player is in a challenging situation but believes there's a sequence of moves that could lead to victory, their \(h_{\text{player}}\) value is high, representing hope.

---

## Jealousy

**Abstract Discussion**:  
Jealousy arises when one perceives another receiving a benefit that one desires. It's rooted in comparison and the inherent desire for resources, attention, or advantages. Jealousy can motivate competitive behaviors but can also lead to negative social dynamics.

**Mathematical Formulation**:  
For agents \(i\) and \(j\), if \(i\) perceives \(j\) receiving a desired reward:
\[
j_{i,j} = 
\begin{cases} 
r_j(a_k) - r_i(a_k) & \text{if } r_j(a_k) > r_i(a_k) \\
0 & \text{otherwise}
\end{cases}
\]

**Example**:  
In a race, if Runner A perceives Runner B getting ahead and feels a sense of loss or inadequacy, \(j_{A,B}\) would be positive, quantifying A's jealousy.

---

## Gratitude

**Abstract Discussion**:  
Gratitude is the quality of being thankful and the readiness to show appreciation. It strengthens social bonds and can be seen as a reciprocal response to kindness or benefits received. Gratitude is a recognition of positive external influences and a desire to acknowledge them.

**Mathematical Formulation**:  
For agents \(i\) and \(j\), if \(j\)'s action leads to a higher reward for \(i\) than \(i\)'s own action:
\[
g_{i,j} = \max(0, r_i(a_j) - r_i(a_i))
\]

**Example**:  
In a collaborative task, if Team Member A receives help from Member B that significantly improves A's performance, the gratitude \(g_{A,B}\) would be high.

## Envy

**Abstract Discussion**:  
Envy, often confused with jealousy, is the desire for attributes, possessions, or abilities of someone else. Unlike jealousy, which is rooted in perceived loss, envy is about coveting what someone else has. It can be a motivator for self-improvement, but unchecked, it can also lead to negative emotions and actions.

**Mathematical Formulation**:  
For agents \(i\) and \(j\), \(i\)'s envy towards \(j\) can be formulated as:
\[
e_{i,j} = 
\begin{cases} 
r_j(a_j) - r_i(a_i) & \text{if } r_j(a_j) > r_i(a_i) \\
0 & \text{otherwise}
\end{cases}
\]

**Example**:  
In an academic setting, if Student A observes Student B receiving accolades for a project, and A desires similar recognition but hasn't achieved it, \(e_{A,B}\) would be positive, quantifying A's envy.

---

## Loyalty

**Abstract Discussion**:  
Loyalty is a dedicated attachment to someone or something. It's the consistent preference or favor shown, often irrespective of the circumstances. Loyalty can be seen as an emergent property from repeated positive interactions or shared experiences.

**Mathematical Formulation**:  
For agents \(i\) and \(j\), \(i\)'s loyalty towards \(j\) can be quantified as:
\[
l_{i,j} = \mathbb{E}[r_i(a_i|a_j) - r_i(a_i|a_k)]
\]
Where \(a_k\) is an action by any other agent \(k \ne j\).

**Example**:  
In a marketplace, if Customer A consistently chooses Store B over others, even when there might be minor price advantages elsewhere, the loyalty \(l_{A,B}\) is high.

---

## Guilt

**Abstract Discussion**:  
Guilt is the emotional response when one believes they've compromised their own standards of conduct or have harmed another. It serves as a regulatory emotion, guiding individuals towards reparative actions and maintaining social harmony.

**Mathematical Formulation**:  
For agents \(i\) and \(j\), if \(i\)'s action leads to a lower reward for \(j\) than \(j\)'s own action, \(i\)'s guilt towards \(j\) can be expressed as:
\[
g_{i,j} = \min(0, r_j(a_i) - r_j(a_j))
\]

**Example**:  
In a team project, if Member A makes an error that affects the group's performance and recognizes the detriment caused to Member B, the guilt \(g_{A,B}\) would be negative, signifying A's feelings of guilt.

---

## Disappointment

**Abstract Discussion**:  
Disappointment arises when reality doesn't meet expectations. It's the emotional response to unmet desires or hopes. While it's a negative emotion, it can serve as feedback, adjusting one's expectations or driving one towards corrective actions.

**Mathematical Formulation**:  
For an agent \(i\), disappointment can be expressed as:
\[
d_i = \max(0, r_{\text{expected},i} - r_i(a_i))
\]

**Example**:  
In a game, if a player expects to reach a high score but falls short, the value \(d_{\text{player}}\) would be high, quantifying the player's disappointment.

---

## Uncertainty

**Abstract Discussion**:  
Uncertainty is the state of being unsure. It's the gap in knowledge or predictability about future events or outcomes. Uncertainty can induce anxiety, but it's also the soil where curiosity grows, driving exploration and learning.

**Mathematical Formulation**:  
For agent \(i\), uncertainty regarding its rewards from its actions can be quantified using entropy:
\[
u_i = H(r_i(a_i))
\]

**Example**:  
In a maze, if a mouse is unsure which path leads to cheese due to multiple unexplored options, the uncertainty \(u_{\text{mouse}}\) would be high, capturing its unpredictability about the reward.

---

## Cooperation and Competition

**Abstract Discussion**:  
Cooperation and competition are foundational dynamics in multi-agent systems. Cooperation is when agents work together for mutual benefits, while competition is when agents work against each other for individual gains. These dynamics are central in understanding group behaviors and emergent phenomena.

**Mathematical Formulation**:  
For agents \(i\) and \(j\), their dynamic can be expressed as:
\[
c_{i,j} = 
\begin{cases} 
\text{positive} & \text{if } r_i(a_j) + r_j(a_i) > r_i(a_i) + r_j(a_j) \text{ (Cooperation)} \\
\text{negative} & \text{otherwise (Competition)}
\end{cases}
\]

**Example**:  
In a team-based game,
## Cooperation and Competition

**Abstract Discussion**:  
In a vast sea of possibilities, every entity, like a ship, charts its own course. Cooperation is akin to two ships aligning their routes, steering together towards a shared horizon, while competition is when ships race to reach a coveted island first. The fluidity of the ocean mirrors the fluid dynamics of human interactions, where sometimes we come together for a shared journey, and at other times, we compete for limited resources.

**Mathematical Formulation**:  
Consider two ships, \(i\) and \(j\). Their relationship in terms of cooperative or competitive dynamics can be described as:
\[
c_{i,j} = 
\begin{cases} 
\text{Sailing Together} & \text{if } v_i(a_j) + v_j(a_i) > v_i(a_i) + v_j(a_j) \text{ (Cooperation)} \\
\text{Racing} & \text{otherwise (Competition)}
\end{cases}
\]

Where \(v\) stands for the value derived from a particular action \(a\).

**Example**:  
Imagine two ships, one loaded with goods and the other with a map to a lucrative market. If they share their resources, they can both benefit more than if they tried to reach the market separately. This would be a cooperative dynamic. Conversely, if there's only one berth left at a popular port, the ships might race each other to secure it, embodying competition.

---

## Hope

**Abstract Discussion**:  
Hope is the luminous star that guides us through the darkest nights. It represents our belief in a brighter tomorrow, even when today's horizon seems bleak. Like a phoenix, it emerges from the ashes of despair, reminding us of potential future joys.

**Mathematical Formulation**:  
For an individual \(i\), hope can be quantified as the expected positive deviation from a current state:
\[
h_i = \mathbb{E}[r_{\text{future},i} - r_{\text{present},i} | r_{\text{future},i} > r_{\text{present},i}]
\]

**Example**:  
A farmer sowing seeds in a barren land has hope if he believes the future harvest will provide more value than the current desolate state. The difference between the expected bountiful harvest and the present barrenness quantifies his hope.

---

## Curiosity

**Abstract Discussion**:  
Curiosity is the compass that leads us towards the unknown. It's the spark that drives us to ask questions, to explore uncharted territories, and to seek answers in the vast expanse of the universe. Just as rivers relentlessly carve their way through mountains, curiosity drives us forward, seeking knowledge and understanding.

**Mathematical Formulation**:  
For an explorer \(i\), curiosity can be described as the entropy of their beliefs about the world:
\[
\text{curiosity}_i = H(p_i)
\]

Where \(H\) is entropy, capturing the uncertainty, and \(p_i\) is the probability distribution of \(i\)'s beliefs about various states of the world.

**Example**:  
A scientist probing the mysteries of quantum mechanics has high curiosity if she has many diverse hypotheses about how particles might behave, capturing a wide distribution of beliefs, and thus a high entropy.

---

## Love

**Abstract Discussion**:  
Love is the invisible thread that binds souls together. It is the force that pulls us close, transcending reason, space, and time. Like the moon's gravitational pull on the seas, love has an ethereal, magnetic quality, drawing us into its embrace.

**Mathematical Formulation**:  
For two beings \(i\) and \(j\), love can be represented as a mutual increase in utility due to the other's presence:
\[
l_{i,j} = \mathbb{E}[r_i(a_j) + r_j(a_i)] - \mathbb{E}[r_i(a_i) + r_j(a_j)]
\]

**Example**:  
Two musicians, when playing separately, bring joy to an audience. But when they play a duet, the combined joy they bring is greater than the sum of their individual performances. This surplus joy captures the essence of their harmonious love.

---

Note: These formulations are abstract and metaphorical, aiming to bridge philosophy and mathematics. They might not capture the full depth of human emotions but provide a starting point for computational understanding.
## Jealousy

**Abstract Discussion**:  
Jealousy is like the shadow cast on a brilliant painting, a darkness that emerges in the presence of another's light. This complex emotion is not merely about wanting what someone else possesses, but it's interwoven with our own insecurities and perceived inadequacies. It's the juxtaposition of another's brilliance with our own perceived dimness.

**Mathematical Formulation**:  
For two individuals \(i\) and \(j\), if \(j\) possesses something \(i\) values but lacks, jealousy is the differential amplified by \(i\)'s insecurity:
\[
j_{i,j} = (v_j - v_i) \times \text{InsecurityFactor}(i)
\]

Where \(v\) represents the value or quality an individual possesses and the InsecurityFactor quantifies the extent of \(i\)'s insecurity.

**Example**:  
Two artists showcase their paintings. If one artist's work is widely acclaimed while the other's isn't, and the latter constantly doubts their own skill, their jealousy would be the acclaim difference amplified by their self-doubt.

---

## Gratitude

**Abstract Discussion**:  
Gratitude is like the warmth of sunlight after a prolonged winter. It emerges from the recognition of kindness, often unexpected, that illuminates our lives. It's the heart's way of acknowledging and cherishing the rays of benevolence in our lives.

**Mathematical Formulation**:  
For an individual \(i\) receiving an act of kindness \(a_j\) from \(j\):
\[
g_{i,j} = \frac{\text{Benefit}(a_j) - \text{ExpectedBenefit}_i}{\text{ExpectedBenefit}_i}
\]

Where Benefit represents the positive impact of the action and ExpectedBenefit is what \(i\) typically anticipates.

**Example**:  
If a person stranded in a storm is given shelter by a stranger, their gratitude would be the comfort and safety of the shelter divided by their initial bleak expectation, essentially quantifying the unexpected boon.

---

## Reverie

**Abstract Discussion**:  
Reverie is a gentle drift on the stream of consciousness, unhurried by the currents of the external world. It's a soft detachment, where one is cocooned in the gossamer of their thoughts, untouched by the tangible reality around them.

**Mathematical Formulation**:  
For an individual \(i\) in a state of daydreaming:
\[
r_i = \frac{\text{InternalFocus}_i}{\text{InternalFocus}_i + \text{ExternalStimuli}_i}
\]

Where InternalFocus represents the intensity of \(i\)'s internal thoughts and ExternalStimuli is the magnitude of external distractions.

**Example**:  
A poet, lost in thoughts about a distant love while sitting in a bustling café, has a high reverie value if the weight of their internal musings is much greater than the café's clamor.

---

## Resilience

**Abstract Discussion**:  
Resilience is the strength of a tree that bends in the storm but doesn't break, drawing vitality from its deep roots to stand tall once again. It's the embodiment of adaptability and tenacity, representing our innate ability to recover and thrive in the face of adversities.

**Mathematical Formulation**:  
For an individual \(i\) facing a challenge \(c\):
\[
r_i = \frac{\text{RecoverySpeed}(c_i)}{\text{ChallengeIntensity}(c)}
\]

Where RecoverySpeed measures how quickly \(i\) returns to a state of equilibrium post-challenge, and ChallengeIntensity quantifies the magnitude of the adversity.

**Example**:  
After a community faces a natural disaster, its resilience would be the speed at which it rebuilds and heals divided by the severity of the disaster, capturing its collective spirit of recovery.

---

These explorations attempt to meld the abstract with the tangible, breathing mathematical life into the nebulous realm of human emotions. They're starting points, inviting further refinement and introspection.