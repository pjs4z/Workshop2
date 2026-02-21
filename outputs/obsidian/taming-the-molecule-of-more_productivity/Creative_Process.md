# [[Creative Process]]
**Type:** #BFO/Occurrent

## Concept Summary
The [[Creative Process]] is a mechanical, two-stage event designed to overcome [[Cognitive Fixation]] and produce novel solutions. It is not treated as a mystical talent but as a disciplined practice. The process is defined by its two essential sub-processes, or parts: [[Divergent Thinking]] followed by [[Convergent Thinking]].

The overall function is to transform an agent from a state of being mentally "stuck" to a state of possessing an innovative idea.

## Formal Semantics
```manchester
Class: [[Creative Process]]
Annotations: rdfs:comment "A macro-process for generating novelty which consumes cognitive fixation."

SubClassOf: 
    [[Occurrent]]

    and (has_participant some [[Modern Human]])
    and (has_part some [[Divergent Thinking]])
    and (has_part some [[Convergent Thinking]])
    and (consumes some ([[Modern Human]] and (has_state some [[Cognitive Fixation]])))
    and (yields some ([[Modern Human]] and (has_state some [[Possessing Novel Solution]])))
```