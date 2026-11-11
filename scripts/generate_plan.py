
from pathlib import Path
from datetime import date

output = Path("content_plan.txt")

plan = f"""
YOUTUBE AUTOMATION - CONTENT PLAN
Date: {date.today()}

CHANNEL: Sumit Mishra
LANGUAGE: Hindi + Hinglish
NICHE: AI and Technology

SHORTS IDEAS:
1. AI kya hai?
2. Kya AI jobs le lega?
3. Students ke liye 3 free AI tools

LONG VIDEO IDEA:
Will AI Take Away Human Jobs?

RULE:
Research facts before publishing.
Never invent statistics.
"""

output.write_text(plan, encoding="utf-8")
print("Content plan created successfully!")
