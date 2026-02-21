# [[Dopaminergic Cycle]]
**Type:** #BFO/Occurrent

## Concept Summary
The [[Dopaminergic Cycle]] is the core feedback loop of desire and dissatisfaction. The process begins when an agent in a state of contentment ([[State of Familiarity]]) is triggered by [[Dopamine]] to pursue a novel target. Upon acquisition, the satisfaction is transient, leading to hedonic adaptation and a return to dissatisfaction, thus restarting the cycle.

This process is framed as a maladaptive relic of evolutionary biology, functioning destructively in an environment of modern abundance.

## Formal Semantics
```manchester
Class: [[Dopaminergic Cycle]]
Annotations: rdfs:comment "A process that transforms an agent from a state of familiarity to a state of restless dissatisfaction."

SubClassOf: 
    [[Occurrent]]

    and (has_participant some [[Modern Human]])
    and (has_participant some [[Dopamine]])
    and (consumes some ([[Modern Human]] and (has_state some [[State of Familiarity]])))
    and (yields some ([[Modern Human]] and (has_state some [[Restless Dissatisfaction]])))
```