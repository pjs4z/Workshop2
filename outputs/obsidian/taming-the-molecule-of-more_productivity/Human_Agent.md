# [[Human Agent]]
**Type:** #BFO/Independent_Continuant

## Concept Summary
The Human Agent is the fundamental bearer of all cognitive and physiological states within this system. It is the vessel that experiences dissatisfaction, pursues creativity, and attempts to exert conscious control over its own biological imperatives. As an Independent Continuant, it endures through time while its internal states (Dependent Continuants) are transformed by Occurrents.

## Formal Semantics
```manchester
Class: [[Human Agent]]
Annotations: rdfs:comment "A biological organism possessing cognitive faculties, serving as the bearer of states and the executor of processes."

SubClassOf: 
    [[Independent_Continuant]]

    # A Human Agent is the subject of various states
    and (has_state some [[Familiarity]])
    and (has_state some [[Cognitive Fixation]])
    and (has_state some [[The 'Promise'/'Itch']])
    and (has_state some [[Hypnagogia]])
    and (has_state some [[Tragic Optimism]])
    and (has_state some [[Unrefined Ideas]])

    # A Human Agent participates in all key processes
    and (participates_in some [[Dopaminergic Cycle]])
    and (participates_in some [[Creative Process]])
    and (participates_in some [[Hypnagogic Capture]])
    and (participates_in some [[Taming the Biological Imperative]])
    
    # Mereological relationship
    and (has_part some [[The Unconscious Mind]])
```