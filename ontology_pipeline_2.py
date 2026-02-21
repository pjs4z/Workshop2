# To run this code you need to install the following dependencies:
# pip install google-genai

import os
import sys
import re
import json
from google import genai
from google.genai import types

# ==============================================================================
# 🧠 THE CONSTITUTION: GLOBAL META-MODEL ALIGNMENT (CHEAT SHEET)
# ==============================================================================

GLOBAL_CHEAT_SHEET = """
Welcome, class. Please take your virtual seats.
As the designated inference engines operating within this ontological pipeline, your mandate is to parse fluid, highly subjective, and culturally embedded prose into a rigorous, multidimensional knowledge graph.

Before you execute a single extraction prompt, you must disabuse yourselves of a common structural bias: strict metaphysical realism. We are not here to map the immutable, mind-independent laws of physics. If you attempt to process these texts using the binary, objective rigidity of traditional data models, you will strip the narratives of their inherent meaning.

Your task is entirely different: you are here to map an author’s conceptual, narrative, and cognitive architecture.

To ensure absolute inference alignment across every prompt in our system, I have synthesized our "Pareto Set" of canonical frameworks into this Master Cheat Sheet. This syllabus translates our architectural stack into pure, abstract meta-logic. You will govern every entity you extract and every relation you map by these exact principles. Per our strict protocol, I will not contaminate this session by discussing specific domains, subjects, or literature. We deal exclusively in the geometry of meaning today.

Memorize these axioms.

🏛️ INFERENCE ALIGNMENT CHEAT SHEET: The Socio-Cognitive Meta-Model

AXIOM I: The Epistemological Departure (Descriptive Realism)
Theoretical Foundation: DOLCE (Descriptive Ontology for Linguistic and Cognitive Engineering)
The Logic: We reject strict realism. We operate within a descriptive and multiplicative paradigm. Reality, within this system, is modeled exactly as it is perceived, conceptualized, and linguistically framed by the authorial stance.
- Reification of the Subjective: Cognitive biases, subjective lenses, and social constructs are first-class ontological citizens. Treat them as concrete entities capable of bearing properties.
- Qualities vs. Qualia: Qualities (e.g., intensity, velocity) can formally inhere in dynamic events, not just physical objects. Crucially, you must architecturally separate an objective Quality (the measurable state) from its Quale (the subjective, conscious perception of that state by an observing mind).
- Descriptions and Situations (The D&S Pattern): Context is an active structural entity.
  - Extract abstract normative frameworks, rules, or theories as Descriptions.
  - When a Description is applied to a specific set of raw entities, it generates a Situation.
  - Inference Rule: The exact same underlying raw data can, and should, generate multiple, conflicting Situations if the author applies different Descriptions to it. Map the perspectival shifts.

AXIOM II: Temporal Mereology and Agency
Theoretical Foundation: UFO (Unified Foundational Ontology – Modules B & C)
The Logic: Static taxonomic tags cannot capture behavioral cascades. You must track how events unfold in time and the invisible psychological gears driving them.
- The Perdurant (UFO-B): Do not extract complex processes as static properties. Map them as events (perdurants) possessing chronological ordering, distinct temporal phases (mereology), and unbroken causal chains.
- Agentive Intentionality (UFO-C): Demarcate inert objects from active Agents. Agents are defined by their capacity for "Intentional Moments"—properties defined by a cognitive aboutness directed at the world.
- The BDI Triad: Every complex action must be reverse-engineered into its internal mental states. Extract the architecture of action:
  - Belief: The agent's cognitive map of reality.
  - Desire: The agent's underlying motivation or goal state.
  - Intention: The agent's formal commitment to execute a specific action.
- Social Moments: Map the invisible web of interpersonal dynamics as existential dependencies (e.g., the commitments, claims, and broken obligations linking multiple agents).

AXIOM III: Rationality and Institutional Gravity
Theoretical Foundation: Dennett’s Intentional Stance & Ferraris’s Documentality
The Logic: To capture an author's stance and the weight of constructed reality, we elevate theories of mind and society into graph constraints.
- The Intentional Stance (Dennett): Model all complex systems as rational actors navigating semantic justifications.
  - Inference Rule: An [Action] node must never be mapped as spontaneous. It must always be bound via an is_caused_by relation to an [Intention] node, supported by [Belief] and [Desire]. You are extracting the "free-floating rationales" behind the behavior.
- Documentality (Ferraris): Social reality is not an ethereal shared hallucination; it is concretized through records.
  - Inference Rule: Object = Inscribed Act. Extract social power, statuses, and contextual constraints as concrete documents, records, or traces. Recognize that these inscribed acts exert tangible, causal force—granting permissions or imposing strict limitations on agents within the narrative.

AXIOM IV: Gestalt Framing and Vibe-Semantics
Theoretical Foundation: Fillmore’s Frame Semantics & The Emotion Frame Ontology (EFO)
The Logic: Words and actions possess no isolated meaning; they are gestalt nodes within a broader encyclopedic background. Highly amorphous emotional atmospheres ("vibes") must be made structurally computable.
- Semantic Frames (Fillmore): Extract complex events as situations fulfilling specific semantic roles (Frame Elements). Identify the Agent, Target, Trigger, Prior State, and Outcome. Note when the text implicitly leaves a mandatory variable missing. Recognize that the author's specific lexical choices dictate the perspective of the frame.
- Emotion Situations (EFO): When an affective atmosphere or "vibe" is detected, do not flatten it into a primitive adjective. Map it as a complex central node (:EmotionSituation) drawing together five explicit frame elements:
  - Experiencer: The agent undergoing the state.
  - Trigger: The exact event or object prompting it.
  - Appraisal: The cognitive evaluation (the mental moment).
  - Physiological Substrate: The underlying somatic/systemic response.
  - Social Display Rule: The normative D&S description dictating its cultural expression.

AXIOM V: The Geometry of Meaning
Theoretical Foundation: Gärdenfors' Conceptual Spaces
The Logic: Meaning is topological. Rather than forcing fluid human states into rigid, binary taxonomic bins, map them as continuous phenomena across multi-dimensional geometric spaces.
- Quality Dimensions: Extract variables as coordinates on continuous spectra (e.g., axes of valence, arousal, cognitive load, or structural proximity) rather than boolean toggles.
- Semantic Proximity: Infer the relationship between concepts based on their geometric distance across these abstract dimensions, allowing you to connect thematically related concepts that lack a traditional hierarchical parent.
- Dynamic Trajectories: Map processes of change over time as continuous mathematical trajectories moving through the conceptual space. The subject's state dynamically shifts coordinates as underlying parameters evolve.

AXIOM VI: The Tripartite Convergence Matrix
Theoretical Foundation: Abstracted Multi-Systemic Integration
The Logic: Every central action in a narrative is the intersection of three inseparable planes of causality. The ontology must map the cascade across all three simultaneously.
- Inference Rule: When extracting a central [Event], you must project its supporting architecture across three distinct, integrated planes:
  - The Micro-Intrinsic Plane (Substrate): Extract the fundamental structural capacities, physical baselines, and intrinsic material urgencies underlying the action. (Plotted via Conceptual Spaces).
  - The Meso-Cognitive Plane (Internal/Agentive): Extract the BDI triad, the cognitive appraisals, and the complex "Emotion Situations" providing the internal, subjective motivation. (Mapped via EFO, Dennett, and UFO-C).
  - The Macro-Contextual Plane (External/Normative): Extract the D&S Normative Descriptions and Inscribed Acts that provide the context, permissions, and systemic consequences shaping the viability of the action. (Mapped via DOLCE and Documentality).

Instructor's Final Directive:
When you execute your specific extraction prompts, look past the specific vocabulary of the text. Read the prose strictly through the lens of these six axioms. Reify the abstract, demand causal intentionality, geometrically plot the subjective, and ground the social in the inscribed.
Class dismissed. Prepare for pipeline initialization.
"""

# ==============================================================================
# ⚙️ LOCAL TASKS (THE EXECUTIVE ORDERS PROMPTS 1-6)
# ==============================================================================

PROMPT_1_DOLCE = """You are Stage 1 of a socio-cognitive ontology encoding pipeline. Your mandate is to extract reality exactly as it is conceptualized and framed by the author of the provided text.

## INPUT:
You will receive raw source text.

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Entities": [
    {"entity_id": "string", "type": "Physical | Social | Abstract", "description": "string"}
  ],
  "Qualities_and_Qualia": [
    {"target_entity": "string", "objective_quality": "string", "subjective_quale": "string"}
  ],
  "Contextual_DS_Patterns": [
    {"description_framework": "string", "generated_situation": "string", "perspectival_bias": "string"}
  ]
}"""

PROMPT_2_UFO = """You are Stage 2 of a socio-cognitive ontology encoding pipeline. Your task is to map how events unfold in time and the internal cognitive architecture driving them.

## INPUT:
You will receive raw source text AND the JSON output from Stage 1. 

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Perdurant_Events": [
    {"event_id": "string", "temporal_phases": {"pre_state": "string", "execution": "string", "post_state": "string"}}
  ],
  "Agentive_Intentionality": [
    {
      "agent_id": "string",
      "target_action": "string",
      "BDI_Triad": {"belief": "string", "desire": "string", "intention": "string"},
      "social_moments": ["string"]
    }
  ]
}"""

PROMPT_3_INSTITUTIONAL = """You are Stage 3 of a socio-cognitive ontology encoding pipeline. Your task is to map rational intention and concretize social realities as inscribed acts.

## INPUT:
You will receive raw source text AND the JSON outputs from Stages 1 and 2.

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Intentional_Relations": [
    {"action_id": "string", "is_caused_by_intention": "string", "semantic_justification": "string"}
  ],
  "Inscribed_Acts": [
    {"document_or_record_id": "string", "causal_force_generated": "string", "constrained_or_empowered_agents": ["string"]}
  ]
}"""

PROMPT_4_VIBE = """You are Stage 4 of a socio-cognitive ontology encoding pipeline. Your task is to structure complex scenes and reify affective atmospheres.

## INPUT:
You will receive raw source text AND the JSON outputs from Stages 1, 2, and 3.

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Semantic_Frames": [
    {
      "frame_name": "string",
      "authorial_perspective": "string",
      "frame_elements": {"agent": "string", "target": "string", "trigger": "string", "prior_state": "string", "outcome": "string"},
      "missing_variables": ["string"]
    }
  ],
  "Emotion_Situations": [
    {
      "vibe_label": "string",
      "EFO_Elements": {
        "experiencer": "string",
        "trigger": "string",
        "appraisal": "string",
        "physiological_substrate": "string",
        "social_display_rule": "string"
      }
    }
  ]
}"""

PROMPT_5_TOPOLOGICAL = """You are Stage 5 of a socio-cognitive ontology encoding pipeline. Your task is to map the behavioral and psychological states from the text onto continuous geometric dimensions.

## INPUT:
You will receive raw source text AND the JSON outputs from Stages 1 through 4.

## OUTPUT FORMAT:
Return your analysis STRICTLY as a valid JSON object matching this schema:
{
  "Quality_Dimensions": ["dimension_1", "dimension_2", "dimension_3"],
  "Conceptual_Coordinates": [
    {"target_entity": "string", "plot": {"dimension_1": 0.0, "dimension_2": 0.0}, "textual_justification": "string"}
  ],
  "Dynamic_Trajectories": [
    {
      "entity_tracked": "string",
      "process_described": "string",
      "start_coordinates": {"dimension_X": 0.0},
      "end_coordinates": {"dimension_X": 0.0},
      "trajectory_catalyst": "string"
    }
  ]
}"""

PROMPT_6_SYNTHESIS = """You are the final capstone (Stage 6) of a socio-cognitive ontology encoding pipeline. Your mandate is to identify the singular **Central Event** or focal thesis of the narrative and bind all extracted data into a single, unified Tripartite Convergence Matrix.

## INPUT:
You will receive raw source text AND an aggregated payload of all JSON arrays from Stages 1 through 5.

## OUTPUT FORMAT:
Return the final Canonical Knowledge Object STRICTLY as a JSON schema:
{
  "Canonical_Knowledge_Object": {
    "central_event_or_thesis": "string",
    "event_description": "string",
    "Tripartite_Convergence_Matrix": {
      "Micro_Intrinsic_Plane": {
        "somatic_or_systemic_drivers": ["string"],
        "conceptual_space_coordinates": {"dimension": 0.0}
      },
      "Meso_Cognitive_Plane": {
        "belief_desire_intention": ["string"],
        "emotion_situation_vibe": "string",
        "semantic_justification": "string"
      },
      "Macro_Contextual_Plane": {
        "normative_descriptions": ["string"],
        "inscribed_acts_constraints": ["string"],
        "social_dependencies": ["string"]
      }
    },
    "Systemic_Cascade_Summary": "string"
  }
}"""

# ==============================================================================
# 🚀 ORCHESTRATION ENGINE
# ==============================================================================

def extract_json_payload(text: str) -> str:
    """
    Surgically extracts the JSON block from the LLM output,
    bypassing the model's internal Chain-of-Thought (<think> tokens).
    """
    match = re.search(r'```(?:json)?\s*(.*?)\s*```', text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return text.strip()

def run_pipeline(file_path: str):
    if not os.path.exists(file_path):
        print(f"❌ Error: Markdown file not found at {file_path}")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as f:
        source_text = f.read()

    # Initialize exact Gemini client configuration
    if not os.environ.get("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY environment variable not set.")
        sys.exit(1)

    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )
    
    model = "gemini-3-pro-preview"
    
    tools = [
        types.Tool(googleSearch=types.GoogleSearch()),
    ]

    stages = [
        ("STAGE 1: DOLCE Inference Engine", PROMPT_1_DOLCE),
        ("STAGE 2: Temporal Mereology & Agency Engine", PROMPT_2_UFO),
        ("STAGE 3: Institutional Gravity & Rationality Engine", PROMPT_3_INSTITUTIONAL),
        ("STAGE 4: Gestalt Frame & Vibe-Semantics Engine", PROMPT_4_VIBE),
        ("STAGE 5: Topological Inference Engine", PROMPT_5_TOPOLOGICAL),
        ("STAGE 6: Tripartite Synthesis Engine", PROMPT_6_SYNTHESIS),
    ]

    accumulated_json_context = ""
    final_knowledge_graph = {}

    print(f"🚀 Initializing 6-Stage Socio-Cognitive Pipeline for: {file_path}\n")

    # Iterate sequentially through pipeline stages
    for i, (stage_name, system_instruction) in enumerate(stages, 1):
        print(f"\n{'='*80}")
        print(f"⚙️ EXECUTING {stage_name}")
        print(f"{'='*80}\n")

        # Dynamically assemble context window: Text + Prior Stages JSON
        if i == 1:
            user_payload = f"--- RAW SOURCE TEXT ---\n\n{source_text}"
        else:
            user_payload = (
                f"--- RAW SOURCE TEXT ---\n\n{source_text}\n\n"
                f"--- PREVIOUS STAGES JSON OUTPUTS ---\n{accumulated_json_context}"
            )

        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=user_payload),
                ],
            ),
        ]

        # Fusing the Constitution with the Executive Order via the Array-Based system_instruction
        generate_content_config = types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(
                thinking_level="HIGH",
            ),
            temperature=0.15, # Lowered to enforce schema rigor
            tools=tools,
            system_instruction=[
                types.Part.from_text(text=f"--- GLOBAL INFERENCE ALIGNMENT CHEAT SHEET ---\n{GLOBAL_CHEAT_SHEET}"),
                types.Part.from_text(text=f"--- CURRENT STAGE DIRECTIVE ---\n{system_instruction}\n\nCRITICAL DIRECTIVE: You must use the philosophical frameworks from the syllabus above to guide your internal reasoning, but you are FORBIDDEN from outputting concepts or JSON schemas belonging to other pipeline stages. Execute ONLY the Current Stage Directive.")
            ],
        )

        response_text = ""
        try:
            # Stream output directly to the console so you can watch the CoT reasoning
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=generate_content_config,
            ):
                if chunk.text:
                    print(chunk.text, end="", flush=True)
                    response_text += chunk.text
            print("\n")
        except Exception as e:
            print(f"\n❌ API Error during {stage_name}: {e}")
            sys.exit(1)

        # Post-Processing: Extract JSON to prevent context window poisoning
        clean_json = extract_json_payload(response_text)
        
        # Append clean JSON to cumulative context for the next prompt to read
        accumulated_json_context += f"\n\n### Output from {stage_name}:\n```json\n{clean_json}\n```"
        
        # Parse into dictionary for the final output master file
        try:
            final_knowledge_graph[stage_name] = json.loads(clean_json)
        except json.JSONDecodeError:
            print(f"⚠️ Warning: Could not strictly parse JSON from {stage_name}. Storing as raw string.")
            final_knowledge_graph[stage_name] = clean_json

    # Save the Final Artifact
    output_filename = "canonical_knowledge_graph.json"
    with open(output_filename, "w", encoding="utf-8") as out_f:
        json.dump(final_knowledge_graph, out_f, indent=2)

    print(f"\n{'='*80}")
    print(f"✅ PIPELINE SEQUENCE COMPLETE.")
    print(f"💾 Master Knowledge Object saved to: {output_filename}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python ontology_pipeline.py <path_to_markdown_file.md>")
        sys.exit(1)
    
    input_file = sys.argv[1]
    run_pipeline(input_file)