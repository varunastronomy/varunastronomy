#!/usr/bin/env python3
import json
from pathlib import Path
from urllib.request import Request, urlopen

owner = "varunastronomy"
start = "<!-- REPOSITORY_INDEX_START -->"
end = "<!-- REPOSITORY_INDEX_END -->"
request = Request(f"https://api.github.com/users/{owner}/repos?per_page=100&type=public", headers={"User-Agent": "profile-index-updater"})
with urlopen(request, timeout=30) as response:
    repositories = json.load(response)
lines = []
for repo in sorted(repositories, key=lambda item: item["name"].lower()):
    if repo["name"] == owner or repo.get("fork"):
        continue
    description = (repo.get("description") or "Research software repository").strip()
    lines.append(f'- [{repo["name"]}]({repo["html_url"]}) — {description}')
readme = Path(__file__).resolve().parents[1] / "README.md"
text = readme.read_text()
before, remainder = text.split(start, 1)
_, after = remainder.split(end, 1)
readme.write_text(before + start + "\n" + "\n".join(lines) + "\n" + end + after)
