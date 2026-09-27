"""Rewrite the "Recently starred" block in README.md from the GitHub API."""
import json
import os
import re
import urllib.request

USER = os.environ.get("GH_USER", "SharpThunder")
COUNT = 8
README = "README.md"

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/starred?per_page={COUNT}",
    headers={
        "Accept": "application/vnd.github.star+json",
        **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {}),
    },
)
with urllib.request.urlopen(req) as resp:
    stars = json.load(resp)

rows = ["| Repo | What it is | ⭐ |", "|---|---|---|"]
for s in stars:
    repo = s["repo"]
    desc = (repo.get("description") or "").replace("|", "/").strip()
    if len(desc) > 90:
        desc = desc[:87].rstrip() + "..."
    rows.append(f"| [{repo['full_name']}]({repo['html_url']}) | {desc} | {repo['stargazers_count']:,} |")

with open(README, encoding="utf-8") as f:
    text = f.read()

block = "<!-- STARRED:START -->\n" + "\n".join(rows) + "\n<!-- STARRED:END -->"
text = re.sub(r"<!-- STARRED:START -->.*?<!-- STARRED:END -->", block, text, flags=re.S)

with open(README, "w", encoding="utf-8") as f:
    f.write(text)
