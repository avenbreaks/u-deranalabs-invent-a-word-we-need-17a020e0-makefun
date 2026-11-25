"""Corridance: one invented word, one line, written to /output/entry.txt.

The word names a moment English has no word for: the awkward mirrored
sidestep two people do when each keeps blocking the other in a narrow
hallway. Deterministic: no input, no network, no clock, no randomness.
"""

import os

ENTRY = (
    "Corridance (n.): the awkward mirrored sidestep dance of two people "
    "who keep blocking each other in a narrow hallway."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
