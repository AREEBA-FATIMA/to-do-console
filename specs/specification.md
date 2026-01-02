# Specification: In-Memory To-Do App (Phase 1)

## 1. Overview
A high-quality CLI application for managing tasks in real-time memory. Designed for students to learn Spec-Driven Development (SDD) with Spec-Kit Plus.

## 2. User Stories
- **As a** student developer
- **I want** to manage a list of tasks via CMD
- **So that** I can track my daily goals without persistence.

## 3. Requirements & Acceptance Criteria
- [ ] **R1: Add Task**
  - **Acceptance Criteria**: Command `add "Title" ["Description"]` adds a task with status "Pending".
- [ ] **R2: View Tasks**
  - **Acceptance Criteria**: Command `list` displays all tasks in a table. Supports `--done` and `--pending` filters.
- [ ] **R3: Update Task**
  - **Acceptance Criteria**: Command `update <id> "New Title" ["New Desc"]` modifies an existing task.
- [ ] **R4: Delete Task**
  - **Acceptance Criteria**: Command `delete <id>` removes the task permanently from memory.
- [ ] **R5: Mark Complete**
  - **Acceptance Criteria**: Command `done <id>` changes status to "Done". `undone <id>` reverts to "Pending".

## 4. Uncertainties & Constraints
- [NEEDS CLARIFICATION]: Should IDs be recycled after deletion? (Default: No).
- **Constraint**: All operations must be in-memory (loss of data on exit).
- **Constraint**: Must use Python 3.13 features (type hints, dataclasses).

## 5. Metadata
- Ref: Hackathon 2 Phase 1
- Phase: Specify
