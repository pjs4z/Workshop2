---
title: "Dark Mode CSS Variable Palette Specification"
category: "Design"
canonical_entities:
  - id: "design_token"
    type: "design_token"
    alias_found: "tokens"
potential_misalignments: []
ai_roles:
  - "UX Designer"
  - "Art Director"
  - "System Architect"
last_updated: "2025-07-31"
---


## Dark Mode CSS Variable Palette Specification

The specification establishes a complete dark-mode palette by binding every functional role—text, foreground, border, icon, surface, focus ring, and semantic feedback—to a small set of calibrated neutral, brand, and status hues. Neutral tones anchor backgrounds and borders, cascading from deep charcoal foundations through graded bone and silver highlights to guarantee sufficient contrast. On top of this base, vivid brand amber drives primary emphasis, while red, gold, and teal articulate error, warning, and success states. Each color presents hover, active, and disabled variations, allowing interaction cues to remain legible without breaking the overall harmony.  

These tokens form an abstract layer that components reference instead of raw values, letting designers switch themes or adjust accessibility ratios without touching implementation code. Shadows, inner glows, and subtle overlays add depth appropriate to dark surfaces, and a parallel set of role aliases—such as primary, secondary, destructive, and muted—maps directly to brand or neutral primitives so motion across contexts feels coherent. The result is a resilient system that unifies visual language across the product suite, accelerates development, and preserves readability under low-light conditions.
Processed from: css-variables-dark 23a5b735d5538085829cc2cd374e0c0f.md
