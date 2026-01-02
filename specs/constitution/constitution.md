# Constitution: Development Principles

## 1. Spec-Driven Development (SDD)
- No implementation without a specification.
- Specs are stored in `specs/`.
- Implementation must follow the plan and tasks generated from specs.

## 2. Reusable Intelligence (RI)
- Extract common patterns to `skills/`.
- Reference skills in project `CLAUDE.md`.
- Build for the future (Phase 2, 3, etc.).

## 3. High Standards
- **Python**: 3.13+, strict typing (Mypy), PEP 8 (Flake8).
- **Testing**: 80%+ coverage, unit tests for core logic.
- **In-Memory**: No DB persistence in Phase 1.
