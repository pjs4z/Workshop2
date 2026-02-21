# [[Divergent Thinking]]
**Type:** #BFO/Occurrent

## Concept Summary
[[Divergent Thinking]] is the first stage of the [[Creative Process]]. It is the temporal unfolding of gathering information, ideas, and stimuli without judgment or logical filtering. Described as "taking down the velvet rope," its purpose is to create a wide, chaotic pool of raw material for later refinement.

This process is fundamentally dopaminergic, driven by the search for novelty and salience. It must precede the logical sorting of [[Convergent Thinking]].

## Formal Semantics
```manchester
Class: [[Divergent Thinking]]
Annotations: rdfs:comment "A process of non-judgmental idea generation that precedes convergent thinking."

SubClassOf: 
    [[Occurrent]]

    and (has_participant some [[Modern Human]])
    and (consumes some ([[Modern Human]] and (has_state some [[Cognitive Fixation]])))
    and (yields some ([[Modern Human]] and (has_state some [[Possessing Unfiltered Ideas]])))
    and (precedes some [[Convergent Thinking]])
```