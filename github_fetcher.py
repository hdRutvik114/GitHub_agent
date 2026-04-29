# github_fetcher.py

import requests

def fetch_repo(owner, repo, path=""):
    """
    Recursively fetch all files from a GitHub repository.

    Params:
    - owner: GitHub username
    - repo: repository name
    - path: current folder path (used for recursion)

    Returns:
    - List of dictionaries:
      { "path": file_path, "content": file_content }
    """

    # GitHub API endpoint to get repo contents
    url = f"https://api.github.com/repos/{owner}/{repo}/contents/{path}"

    response = requests.get(url)

    # convert response to JSON
    data = response.json()

    files = []

    # loop through each item (file or folder)
    for item in data:

        # CASE 1: If it's a file
        if item["type"] == "file":

            # download raw file content
            file_response = requests.get(item["download_url"])

            files.append({
                "path": item["path"],        # file path inside repo
                "content": file_response.text  # actual code/content
            })

        # CASE 2: If it's a directory → recurse
        elif item["type"] == "dir":

            # call same function again for subfolder
            sub_files = fetch_repo(owner, repo, item["path"])

            # add subfolder files to main list
            files.extend(sub_files)

    return files