import os

paths = [
    r"d:\hackathon 2\cli\hackathon-2\history",
    r"d:\hackathon 2\cli\hackathon-2\history\prompts",
    r"d:\hackathon 2\cli\hackathon-2\history\prompts\constitution",
    r"d:\hackathon 2\cli\hackathon-2\history\prompts\spec",
    r"d:\hackathon 2\cli\hackathon-2\history\prompts\plan",
    r"d:\hackathon 2\cli\hackathon-2\history\prompts\tasks",
    r"d:\hackathon 2\cli\hackathon-2\history\prompts\implementation",
    r"d:\hackathon 2\cli\hackathon-2\history\prompts\general",
]

for p in paths:
    try:
        os.makedirs(p, exist_ok=True)
        print(f"Created: {p}")
    except Exception as e:
        print(f"Error creating {p}: {e}")
