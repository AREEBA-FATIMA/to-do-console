import sys
from src.repository import InMemoryTaskRepository
from src.cli import ToDoCLI

def main():
    print("==========================================")
    print("   Spec-Kit Plus: In-Memory To-Do App   ")
    print("           (Phase 1 - GIAIC)            ")
    print("==========================================")
    print("Type 'help' to see available commands.")

    repo = InMemoryTaskRepository()
    cli = ToDoCLI(repo)
    
    try:
        while True:
            user_input = input("\nsdd-ri> ").strip()
            if not cli.handle_command(user_input):
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
