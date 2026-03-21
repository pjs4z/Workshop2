---
title: "AI Agent Building Directive"
category: "Architecture"
canonical_entities:
  - id: "Coach_Bear"
    type: "persona"
    alias_found: "Coach Bear"
  - id: "Dr_Love"
    type: "persona"
    alias_found: "Dr. Love"
  - id: "Brotherhood_Hub"
    type: "module"
    alias_found: "Brotherhood hub"
potential_misalignments:
  - span: "onboarding journey"
    issue: "banned_journey_reference"
  - span: "user journey"
    issue: "banned_journey_reference"
ai_roles:
  - System Architect
  - UX Designer
  - Platform Strategist
last_updated: "2025-07-31"
---


## AI Agent Building Directive

The Reset Order delivers a voice-led recovery experience that pairs an immersive onboarding journey with four core services: Coach Bear for daily guidance, Dr. Love for dating support, a progress dashboard that tracks wins and streaks, and a Brotherhood hub that anchors group meetings. A web portal orchestrates every user interaction while a multi-engine backend interprets intent, stores state, and generates narrative content, maintaining each character’s distinct voice across text, audio, and visuals.

Development advances in tightly sequenced phases that first link the portal to the backend, then layer in onboarding, coaching dialogues, progress computation, and community features before converging on full-system tests and production release. Data flows through a relational store, vector search, real-time channels, and adaptive caches to ensure instant responses, while scheduled jobs and conversation handlers personalize outreach and detect crises. Scalability, security, and cost discipline guide every decision, with benchmarks set for sub-second latency, four-figure concurrency, and unwavering persona consistency. Success is defined by a seamless user journey from sign-up to community engagement, sustained daily coaching, and measurable momentum toward recovery.
Processed from: AI_AGENT_BUILDING_DIRECTIVE.md
