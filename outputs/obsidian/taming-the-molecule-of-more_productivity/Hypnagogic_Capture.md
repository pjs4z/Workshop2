# [[Hypnagogic Capture]]
**Type:** #BFO/Occurrent

## Concept Summary
[[Hypnagogic Capture]] is a specific, multi-part process for accessing and recording insights from the [[Unconscious Mind]]. It involves intentionally interrupting the transition into sleep to transfer fluid, irrational associations from the hypnagogic state into the conscious domain via an inscribed act.

The process requires the participation of the agent, their unconscious mind, and a physical tool ([[Bedside Notebook]]) to be successful.

## Formal Semantics
```manchester
Class: [[Hypnagogic Capture]]
Annotations: rdfs:comment "A process to record unconscious insights by interrupting the transition to sleep."

SubClassOf: 
    [[Occurrent]]

    and (has_participant some [[Modern Human]])
    and (has_participant some [[Unconscious Mind]])
    and (has_participant some [[Bedside Notebook]])
    and (consumes some ([[Modern Human]] and (has_state some [[Prepared Fatigue]])))
    and (yields some ([[Bedside Notebook]] and (has_state some [[Inscribed Insight]])))
```