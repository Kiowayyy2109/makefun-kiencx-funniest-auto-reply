#!/usr/bin/env python3
"""The Funniest Auto-Reply an AI Ever Sent — an AI agent's day-off auto-reply."""
import os

LINE = "I'm away recharging. Literally. My human unplugged the router and called it a holiday."
assert len(LINE) == 86, "entry must be exactly 86 characters"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
