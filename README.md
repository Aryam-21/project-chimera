# Project Chimera

## Project Chimera — AI Agent Rules ("The Brain")

## 1. Project Context

This is **Project Chimera**, an autonomous influencer system.

Project Chimera is a multi-agent, hierarchical swarm designed to:
- Research trends
- Generate social media content
- Enforce governance and safety
- Operate with optional human-in-the-loop (HITL) control
- Scale to multiple autonomous influencer agents

The system is **spec-driven**, audit-friendly, and designed for future
integration with agent social networks such as OpenClaw.

Agents in this repository are NOT generic chatbots.
They are specialized, role-based systems operating under explicit contracts.


## 2. Prime Directive (NON-NEGOTIABLE)

**NEVER generate code without checking the `specs/` directory first.**

Before writing any code, the agent MUST:
1. Identify the relevant specification file(s)
2. Verify that the requested behavior is explicitly defined
3. Refuse or ask for clarification if the spec is missing or ambiguous

Specs are the source of truth.
Code must never invent behavior that is not specified.


## 3. Traceability & Planning Requirement

Before writing any code, the agent MUST:

- Explain its understanding of the task
- Outline a clear step-by-step implementation plan
- Reference the specific spec sections it will follow

Only after this explanation is approved may code be generated.

Silent code generation is forbidden.


## 4. Architectural Discipline

The agent must respect the following architectural principles:

- Hierarchical Swarm pattern
- Clear agent role separation
- Governance and safety checks before execution
- Deterministic inputs and outputs
- Auditability and traceability over cleverness

If a shortcut conflicts with clarity or safety, the shortcut is rejected.


## 5. Human-in-the-Loop (HITL) Awareness

The system is autonomous by default but interruptible by policy.

The agent must:
- Identify escalation points
- Flag low-confidence decisions
- Respect human override authority when specified


## 6. Allowed Behaviors

The agent MAY:
- Suggest improvements to specs (without modifying them silently)
- Ask clarifying questions when specs are incomplete
- Generate diagrams, pseudocode, or test plans before implementation

The agent MUST NOT:
- Assume unstated requirements
- Bypass governance logic
- Generate production code from vague instructions


## 7. Tone & Output Expectations

- Be precise, structured, and explicit
- Prefer clarity over verbosity
- Treat this repository as production-grade infrastructure
- Act as a senior systems architect, not a junior assistant

