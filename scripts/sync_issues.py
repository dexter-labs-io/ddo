import os
import requests

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
REPO = "dexter-labs-io/ddo"
HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"}

def create_issue_from_file(filepath):
    with open(filepath, "r") as f:
        lines = f.readlines()
    title = [l for l in lines if l.startswith("title:")][0].split(":", 1)[1].strip().strip('"[]')
    labels = [l for l in lines if l.startswith("labels:")][0].split(":", 1)[1].strip().strip('[]').replace("'", "").split(",")
    body = "".join(lines[lines.index("---\n")+1:])
    data = {"title": title, "body": body, "labels": [l.strip() for l in labels]}
    r = requests.post(f"https://api.github.com/repos/{REPO}/issues", json=data, headers=HEADERS)
    print(f"Issue created: {r.status_code} - {title}")

if __name__ == "__main__":
    for file in os.listdir(".github/ISSUE_TEMPLATES"):
        if file.endswith(".md"):
            create_issue_from_file(f".github/ISSUE_TEMPLATES/{file}")
