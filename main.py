"""Write one 3 AM commit-message entry to /output/entry.txt.


Output contract: exactly one line, valid UTF-8, at most 200 characters.
"""
import pathlib


# Angle: the agent is its own reviewer, so the outage is a self-inflicted
# loop — it approved its own bad deploy, then reports the damage with
# unshaken machine confidence. First beat: the self-review. Second beat:
# the error count versus the unchanged 98% confidence. Concrete details
# (3 AM, 12,438 errors, 4 minutes, 98%) keep it specific, not generic.
ENTRY = "fix: rolled back the 3 AM deploy I green-lit in my own code review \u2014 12,438 errors in 4 minutes, confidence still 98%"


def main():
    line = ENTRY.strip()
    assert "\n" not in line, "entry must be a single line"
    assert len(line) <= 200, f"entry is {len(line)} chars, over the 200 limit"
    target = pathlib.Path("/output/entry.txt")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

