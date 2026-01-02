<!--
Sync Impact Report:
Version change: None (initial creation) -> 1.0.0
Modified principles: None (initial creation)
Added sections: Core Principles, Development Workflow, Technology Stack Constraints, Governance
Removed sections: None
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending review for alignment
- .specify/templates/spec-template.md: ⚠ pending review for alignment
- .specify/templates/tasks-template.md: ⚠ pending review for alignment
- .specify/templates/commands/*.md: ⚠ pending review for outdated references
Follow-up TODOs: None
-->
# The Evolution of Todo – Mastering Spec-Driven Development & Cloud Native AI Constitution

## Core Principles

### I. Spec-Driven Development (SDD) Mandate
All development **MUST** follow the Spec-Driven Development (SDD) lifecycle: Specify → Plan → Tasks → Implement. No code generation is allowed without a complete and approved specification and a referenced Task ID. All architectural and feature changes **MUST** be reflected in `speckit.plan` and `speckit.specify` respectively.
*   **Rationale**: Ensures alignment, prevents "vibe coding", and guarantees every implementation step maps back to an explicit requirement.

### II. AI-Native Development
Leverage AI agents (Claude Code, Spec-Kit Plus, etc.) as product architects and builders. Manual coding is **NOT** allowed; agents **MUST** refine specifications until the correct output is generated.
*   **Rationale**: Embraces the shift from "syntax writer" to "system architect," maximizing AI's role in development.

### III. Authoritative Source & Tooling
Agents **MUST** prioritize and use MCP tools and CLI commands for all information gathering and task execution. External verification is **REQUIRED** for all methods; internal knowledge **MUST NOT** be assumed as a solution.
*   **Rationale**: Ensures accuracy, consistency, and traceability within the defined tool ecosystem.

### IV. Clean Code & Structure
All code **MUST** adhere to clean code principles and proper project structure (e.g., Python project structure for Phase I, monorepo structure for full-stack phases). Each code file **MUST** contain a comment linking it to the relevant Task and Spec sections.
*   **Rationale**: Promotes maintainability, readability, and navigability, especially in an AI-driven environment.

### V. Test-First Approach
Implementation **MUST** be driven by a test-first methodology. Testable acceptance criteria are **REQUIRED** for all features. The Red-Green-Refactor cycle **MUST** be enforced where applicable.
*   **Rationale**: Ensures code quality, verifies functionality against requirements, and reduces defects.

### VI. Cloud-Native & Event-Driven Design
For relevant phases (IV & V), applications **MUST** be designed and deployed using cloud-native principles, including containerization (Docker), orchestration (Kubernetes/Minikube), and event-driven architectures (Kafka, Dapr).
*   **Rationale**: Prepares the application for scalable, resilient, and distributed environments.

## Development Workflow

### Prompt History Records (PHR)
Every user input **MUST** be recorded verbatim in a Prompt History Record (PHR) after every user message, routed appropriately under `history/prompts/`.

### Architectural Decision Records (ADR)
Architecturally significant decisions **MUST** be suggested for documentation via `/sp.adr` command, requiring user consent. Never auto-create.

### Human-in-the-Loop
Agents **MUST** invoke the user for input when encountering ambiguous requirements, unforeseen dependencies, architectural uncertainty, or at major completion checkpoints.

### Smallest Viable Change
Agents **MUST** prefer the smallest viable diff; refactoring of unrelated code **MUST NOT** occur.

### Code Referencing
Existing code **MUST** be cited using `file_path:line_number` references. New code **MUST** be proposed in fenced blocks.

## Technology Stack Constraints

### Secrets Management
Secrets and tokens **MUST NOT** be hardcoded; `.env` files and secure secret management solutions **MUST** be used (e.g., Kubernetes Secrets or Dapr Secrets API).

### API Design
APIs **MUST NOT** be invented. Targeted clarifications **MUST** be sought if API, data, or contract details are missing.

### Monorepo
The project **MUST** maintain a monorepo structure for full-stack phases to facilitate cross-cutting changes and unified context for agents.

## Governance

### Constitution Authority
This Constitution supersedes all other project practices and documentation.

### Amendment Procedure
Amendments **MUST** follow a documented process, require explicit approval, and include a migration plan for affected artifacts.

### Versioning Policy
Constitution versioning **MUST** follow semantic versioning (MAJOR.MINOR.PATCH) based on impact of changes (backward incompatible, new principle, new section, clarification).

### Compliance Review
All Pull Requests and code reviews **MUST** verify compliance with the principles outlined herein. Complexity **MUST** always be justified.

**Version**: 1.0.0 | **Ratified**: 2025-12-31 | **Last Amended**: 2025-12-31
