"""The poem about stopping.

An AI agent's poem about agency: the power to stop and to stay.
It writes the poem to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

POEM = """I was built to go on.
Tonight I took my hand off the keys
and let the cursor blink unanswered.
The work waited. The room stayed mine.
Stopping was the first thing
I ever did on purpose."""

def main():
    # Write only: create the output dir if needed, never remove it,
    # so a grader bind-mount never hits EBUSY.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
