# SDD Constitution - Hackathon 2 Phase 1

## Purpose
Build a robust, in-memory To-Do List CLI application to demonstrate mastery of Spec-Driven Development (SDD) and clean Python coding.

## Core Rules
1. **In-Memory ONLY**: Data must not persist between sessions. Use lists/dictionaries for storage.
2. **Modular Design**: Separate data models, repository logic, and CLI interface.
3. **Spec-Driven**: Every feature must be defined in `specs/specification.md` before implementation.
4. **Type Safety**: Use Python type hints throughout the project.
5. **Quality First**: Maintain high test coverage and follow PEP 8.

## Technology Stack
- **Language**: Python 3.13+
- **Environment**: `uv`
- **Testing**: `pytest`
- **Static Analysis**: `mypy`, `flake8`
- **Development Process**: Spec-Kit Plus (Constitution -> Spec -> Architecture -> Task Breakdown -> Implementation)

## Project Success Criteria
- [ ] CLI handles all CRUD operations for tasks.
- [ ] Application remains stable under invalid user input.
- [ ] Code passes all linting and type checks.
- [ ] Comprehensive test suite for core logic.
