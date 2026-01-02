# Feature: Task CRUD

## 1. Description
Core functionality for managing a to-do list in-memory.

## 2. Requirements
- **Create**: Add a task with title and optional description.
- **Read**: List tasks with status filtering.
- **Update**: Modify title or description.
- **Delete**: Remove a task by ID.
- **Status Tap**: Toggle tasks between Pending and Done.

## 3. Acceptance Criteria
- [ ] `add` adds task with status Pending.
- [ ] `list` shows formatted table.
- [ ] `done` changes status to Done.
- [ ] `delete` removes task from memory.
- [ ] Error shown for invalid IDs.
