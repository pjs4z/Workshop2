---
title: Color Modes
category: Design
canonical_entities: "[object Object],[object Object]"
potential_misalignments: []
ai_roles:
  - UX Designer
  - System Architect
  - Art Director
last_updated: 2025-07-31
---


## Color Modes

The palette defines a single, brand-wide colour architecture that automatically adapts to light or dark user preference. Every shade first expresses a semantic role—text, borders, surfaces, foreground elements, or visual effects—and only then resolves to an underlying pigment. This indirection lets designers work with intent-based tokens such as “primary text” or “error background” while the system computes the appropriate tint for each mode. A parallel utility scale supplements the core set with evenly stepped hues across blue, brand orange, gray, and other functional families, ensuring both expressive range and tonal harmony.

Component tokens sit one layer higher, translating semantic colours into context-specific behaviours for buttons, sliders, icons, tooltips, and similar interface parts. Each component inherits the universal roles but may override them for interactive states like hover, focus, disabled, or destructive action, guaranteeing visual consistency without sacrificing nuance. Additional alpha and shadow values complete the kit, enabling depth, overlays, and accessibility-compliant focus rings that remain legible in all environments.

Together these mechanisms produce a cohesive visual language that protects brand identity, streamlines theme switching, and reduces implementation friction. Designers gain a predictable canvas; engineers receive a single source of truth; users experience readable, accessible interfaces regardless of device or lighting condition.
Processed from: 1. Color modes.md
