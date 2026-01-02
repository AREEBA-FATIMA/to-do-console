from typing import List, Optional
from src.models import TaskStatus, Task
from src.repository import InMemoryTaskRepository, TaskNotFoundError

class ToDoCLI:
    def __init__(self, repo: InMemoryTaskRepository):
        self.repo = repo

    def handle_command(self, user_input: str) -> bool:
        if not user_input.strip():
            return True
        
        parts = user_input.split()
        cmd = parts[0].lower()
        args = parts[1:]

        if cmd in ("exit", "quit"):
            print("Exiting Spec-Kit Plus To-Do App. Goodbye!")
            return False
        
        try:
            if cmd == "add":
                self._add(args)
            elif cmd == "list":
                self._list(args)
            elif cmd == "done":
                self._mark_done(args)
            elif cmd == "undone":
                self._mark_undone(args)
            elif cmd == "update":
                self._update(args)
            elif cmd == "delete":
                self._delete(args)
            elif cmd == "help":
                self._show_help()
            else:
                print(f"Unknown command: {cmd}. Type 'help' for available commands.")
        except Exception as e:
            print(f"Error: {e}")
        
        return True

    def _add(self, args: List[str]):
        if not args:
            print("Usage: add <title> [description]")
            return
        title = args[0]
        description = " ".join(args[1:]) if len(args) > 1 else ""
        task = self.repo.add(title, description)
        print(f"✅ Task #{task.id} added successfully.")

    def _list(self, args: List[str]):
        status_filter = None
        if args:
            if args[0] == "--done":
                status_filter = TaskStatus.DONE
            elif args[0] == "--pending":
                status_filter = TaskStatus.PENDING

        tasks = self.repo.get_all(status_filter)
        if not tasks:
            print("ℹ️ No tasks found.")
            return

        print(f"\n{'ID':<4} | {'Status':<10} | {'Title':<20} | {'Description'}")
        print("-" * 60)
        for t in tasks:
            status_tag = f"[{t.status.value}]"
            print(f"{t.id:<4} | {status_tag:<10} | {t.title:<20} | {t.description}")

    def _mark_done(self, args: List[str]):
        if not args:
            print("Usage: done <id>")
            return
        task_id = int(args[0])
        self.repo.mark_status(task_id, TaskStatus.DONE)
        print(f"✅ Task #{task_id} marked as Done.")

    def _mark_undone(self, args: List[str]):
        if not args:
            print("Usage: undone <id>")
            return
        task_id = int(args[0])
        self.repo.mark_status(task_id, TaskStatus.PENDING)
        print(f"✅ Task #{task_id} marked as Pending.")

    def _update(self, args: List[str]):
        if len(args) < 2:
            print("Usage: update <id> <new_title> [new_description]")
            return
        task_id = int(args[0])
        title = args[1]
        description = " ".join(args[2:]) if len(args) > 2 else None
        self.repo.update(task_id, title, description)
        print(f"✅ Task #{task_id} updated.")

    def _delete(self, args: List[str]):
        if not args:
            print("Usage: delete <id>")
            return
        task_id = int(args[0])
        self.repo.delete(task_id)
        print(f"✅ Task #{task_id} deleted.")

    def _show_help(self):
        print("\nAvailable Commands:")
        print("  add <title> [desc]         Add a new task")
        print("  list [--done|--pending]    List tasks")
        print("  done <id>                  Mark task as completed")
        print("  undone <id>                Mark task as pending")
        print("  update <id> <title> [desc] Update task details")
        print("  delete <id>                Delete a task")
        print("  help                       Show this menu")
        print("  exit / quit                Close the application")
