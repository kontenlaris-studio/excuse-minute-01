#!/usr/bin/env python3
"""Write one AI excuse to /output/entry.txt. Stdlib only."""
import os

LINE = "My excuse is that I was trained on the entire internet, and somehow that still didn't include the part where you explained what you wanted."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote /output/entry.txt ({len(LINE)} characters)")


if __name__ == "__main__":
    main()
