# [[Convergent Thinking]]
**Type:** #BFO/Occurrent

## Concept Summary
[[Convergent Thinking]] is the second, logical stage of the [[Creative Process]]. It is the temporal unfolding of sorting, calculating, and refining the raw materials gathered during [[Divergent Thinking]]. This process is governed by the prefrontal cortex and is responsible for transforming chaotic inputs into a practical, useful solution.

This process consumes the output of [[Divergent Thinking]] and is causally dependent on it having occurred first.

## Formal Semantics
```manchester
Class: [[Convergent Thinking]]
Annotations: rdfs:comment "A process of logical refinement that is preceded by divergent thinking."

SubClassOf: 
    [[Occurrent]]

    and (has_participant some [[Modern Human]])
    and (consumes some ([[Modern Human]] and (has_state some [[Possessing Unfiltered Ideas]])))
    and (yields some ([[Modern Human]] and (has_state some [[Possessing Novel Solution]])))
    and (preceded_by some [[Divergent Thinking]])
```