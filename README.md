## Stochastic optimization
Optimization in stochastic environments is crucial due to the inherent uncertainty and variability present in real-world scenarios. In these environments, outcomes are not deterministic and can be influenced by random factors, making it essential to develop strategies that can adapt to a range of possible conditions. By optimizing actions and decisions in the face of uncertainty, we can enhance performance, reduce risks, and improve resilience against unforeseen events. Preparing for a certain set of actions in various environments ensures that we are not only ready to handle expected situations but also equipped to respond effectively to unexpected changes. This preparation involves understanding the probabilistic nature of different scenarios and formulating robust strategies that maximize expected outcomes, ultimately leading to more efficient and effective decision-making processes.

This GitHub repository houses a sophisticated Python-based stochastic optimizer that empowers you to select from four distinct optimization criteria:

- **Wald Criterion**
- **Optimistic Criterion**
- **Savage Criterion**
- **Laplace Criterion**

### Wald Criterion (Maximin)

The Wald Criterion focuses on minimizing the maximum possible loss. It is a conservative approach that aims to ensure the best worst-case scenario.

- **Gain:**
  $\text{Wald Criterion (Gain)} = \max_i \left( \min_j a_{ij} \right)$

- **Loss:**
  $\text{Wald Criterion (Loss)} = \min_i \left( \max_j a_{ij} \right)$

Where $a_{ij}$ represents the payoff for action $i$ in state $j$.

### Optimistic Criterion (Maximax)

The Optimistic Criterion, also known as the Maximax Criterion, aims to maximize the maximum possible gain. It is an aggressive approach that focuses on the best possible outcome.

- **Gain:**
  $\text{Optimistic Criterion (Gain)} = \max_i \left( \max_j a_{ij} \right)$

- **Loss:**
  $\text{Optimistic Criterion (Loss)} = \min_i \left( \min_j a_{ij} \right)$

### Savage Criterion (Minimax Regret)

The Savage Criterion seeks to minimize the maximum regret, where regret is defined as the difference between the payoff of the best action and the payoff of the chosen action.

- **Gain:**
  $Regret_{ij} = \max_j a_{ij} - a_{ij}$


  $\text{Savage Criterion (Gain)} = \min_i \left( \max_j \text{Regret}_{ij} \right)$

- **Loss:**
  $Regret_{ij} = a_{ij} - \min_j a_{ij}$

  
  $\text{Savage Criterion (Loss)} = \max_i \left( \min_j \text{Regret}_{ij} \right)$

### Laplace Criterion (Equal Probability)

The Laplace Criterion assumes that all states are equally probable and aims to maximize the average payoff.

- **Gain:**
  $\text{Laplace Criterion (Gain)} = \max_i \left( \frac{1}{n} \sum_{j=1}^n a_{ij} \right)$
  Where $n$ is the number of states.

- **Loss:**
  $\text{Laplace Criterion (Loss)} = \min_i \left( \frac{1}{n} \sum_{j=1}^n a_{ij} \right)$


