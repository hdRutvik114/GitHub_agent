# github_fetcher.py

import requests

ALLOWED_EXTENSIONS = [".js", ".html", ".css", ".py", ".md", ".json"]

# optional: skip heavy/unnecessary folders
SKIP_FOLDERS = ["node_modules", ".git", "dist", "build"]


def is_valid_file(file):
    """
    Check if file extension is allowed
    """
    file_path = file.get("path", "")
    return any(file_path.endswith(ext) for ext in ALLOWED_EXTENSIONS)


def fetch_repo(owner, repo, path=""):
    """
    Recursively fetch all valid files from a GitHub repository
    (works for MERN, nested folders, etc.)
    """

    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"
    response = requests.get(url)

    # 🔴 handle API errors
    if response.status_code != 200:
        print("Error:", response.text)
        return []

    data = response.json()

    # 🔴 if not list → something wrong
    if not isinstance(data, list):
        return []

    files = []

    for item in data:

        # skip unwanted folders
        if item["type"] == "dir" and any(skip in item["path"] for skip in SKIP_FOLDERS):
            continue

        # ✅ CASE 1: file
        if item["type"] == "file":

            # filter extensions early (efficient)
            if not is_valid_file(item):
                continue

            file_response = requests.get(item["download_url"])

            files.append({
                "path": item["path"],
                "content": file_response.text
            })

        # ✅ CASE 2: directory → recurse
        elif item["type"] == "dir":
            sub_files = fetch_repo(owner, repo, item["path"])
            files.extend(sub_files)

    return files