#!/usr/bin/env python3
"""Create this week's log file: python tools/new_log.py"""
import datetime
from pathlib import Path

root = Path(__file__).resolve().parent.parent
today = datetime.date.today()
year, week, _ = today.isocalendar()
monday = today - datetime.timedelta(days=today.weekday())
sunday = monday + datetime.timedelta(days=6)
name = f"{year}-W{week:02d}"
dest = root / "logs" / f"{name}.md"
if dest.exists():
    print(f"Already exists: {dest}")
else:
    text = (root / "templates" / "weekly-log.md").read_text(encoding="utf-8")
    text = text.replace("{{week}}", name).replace("{{dates}}", f"{monday} to {sunday}")
    dest.parent.mkdir(exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(f"Created {dest}")
