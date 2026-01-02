# SDD Architecture Plan - In-Memory To-Do App

## Overview
The application follows a modular architecture to separate concerns and ensure testability. Key components include the Model, Repository, and CLI Interface.

## Components

### 1. Model (`src/models.py`)
- `Task` (dataclass):
  - `id: int`
  - `title: str`
  - `description: str`
  - `status: str` (Enum: PENDING, DONE)
  - `created_at: datetime`

### 2. Repository (`src/repository.py`)
- `ITaskRepository` (Interface/Protocol): Defines the contract for task operations.
- `InMemoryTaskRepository` (Implementation): 
  - Uses a `dict[int, Task]` for $O(1)$ lookups.
  - Manages a thread-safe `_next_id` counter.
  - Methods: `add()`, `get_all()`, `get_by_id()`, `update()`, `delete()`.

### 3. CLI Interface (`src/cli.py`)
- Uses `argparse` for command parsing.
- Handles user input/output.
- Communicates with the `InMemoryTaskRepository`.
- Logic for formatting and printing tables.

## Data Flow
1. User enters command (e.g., `add "Buy Milk"`).
2. `cli.py` parses the arguments.
3. `cli.py` calls `repository.add(title="Buy Milk")`.
4. `repository` creates a `Task` object, assigns an ID, and stores it.
5. `repository` returns the created `Task`.
6. `cli.py` prints a success message.

## Error Handling Strategy
- **Repository Layer**: Raises custom exceptions (e.g., `TaskNotFoundError`).
- **CLI Layer**: Catches exceptions and displays user-friendly messages.

## Testing Strategy
- Unit tests for `InMemoryTaskRepository` to verify all CRUD operations.
- Integration tests for CLI commands using mock inputs.
