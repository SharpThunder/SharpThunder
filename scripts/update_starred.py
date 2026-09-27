"""Rewrite the "What my stars say" and "Recently starred" blocks in README.md."""
import json
import os
import re
import urllib.request

USER = os.environ.get("GH_USER", "SharpThunder")
RECENT = 8
README = "README.md"

# Bucket -> keywords matched against topics, repo name and description.
BUCKETS = {
    "Kubernetes": ["kubernetes", "k8s", "helm", "k3s", "kubectl", "cncf", "operator"],
    "Security": ["security", "devsecops", "vulnerab", "pentest", "hacking", "siem"],
    "Cloud (AWS/Azure/GCP)": ["aws", "azure", "gcp", "google-cloud", "lambda"],
    "Containers": ["docker", "container", "podman"],
    "Observability": ["monitoring", "observability", "prometheus", "grafana", "logging", "tracing", "ebpf"],
    "IaC": ["terraform", "opentofu", "ansible", "pulumi", "infrastructure-as-code", "iac"],
    "CI/CD & GitOps": ["ci-cd", "cicd", "github-actions", "gitops", "argo", "flux", "continuous"],
    "Self-hosted & homelab": ["self-hosted", "selfhosted", "homelab", "proxmox"],
}


def get(url):
    token = os.environ.get("GITHUB_TOKEN")
    req = urllib.request.Request(url, headers={
        "Accept": "application/vnd.github.star+json",
        **({"Authorization": f"Bearer {token}"} if token else {}),
    })
    with urllib.request.urlopen(req) as resp:
        return json.load(resp), resp.headers.get("Link", "")


stars, url = [], f"https://api.github.com/users/{USER}/starred?per_page=100"
while url:
    page, link = get(url)
    stars += page
    m = re.search(r'<([^>]+)>; rel="next"', link)
    url = m.group(1) if m else None


def text(s):
    r = s["repo"]
    return " ".join([r["full_name"], r.get("description") or "", *r.get("topics", [])]).lower()


counts = {b: sum(any(k in text(s) for k in kws) for s in stars) for b, kws in BUCKETS.items()}
top = max(counts.values()) or 1
first_year = min(s["starred_at"][:4] for s in stars)
lines = [f"{len(stars):,} repos starred since {first_year}", ""]
for b, n in sorted(counts.items(), key=lambda kv: -kv[1]):
    lines.append(f"{b:<22} {'█' * round(24 * n / top):<24} {n}")
stats = "```text\n" + "\n".join(lines) + "\n```"

rows = ["| Repo | What it is | ⭐ |", "|---|---|---|"]
for s in stars[:RECENT]:
    r = s["repo"]
    desc = (r.get("description") or "").replace("|", "/").strip()
    if len(desc) > 90:
        desc = desc[:87].rstrip() + "..."
    rows.append(f"| [{r['full_name']}]({r['html_url']}) | {desc} | {r['stargazers_count']:,} |")


def put(src, name, body):
    return re.sub(rf"<!-- {name}:START -->.*?<!-- {name}:END -->",
                  lambda _: f"<!-- {name}:START -->\n{body}\n<!-- {name}:END -->", src, flags=re.S)


with open(README, encoding="utf-8") as f:
    readme = f.read()
readme = put(readme, "STATS", stats)
readme = put(readme, "STARRED", "\n".join(rows))
with open(README, "w", encoding="utf-8") as f:
    f.write(readme)
