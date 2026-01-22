import requests

def fetch_github_issue(repo_url, issue_number):
    try:
        parts = repo_url.replace("https://github.com/", "").split("/")
        owner, repo = parts[0], parts[1]

        api_url = f"https://api.github.com/repos/{owner}/{repo}/issues/{issue_number}"
        response = requests.get(api_url)

        if response.status_code != 200:
            return None, "Issue not found or repository is invalid"

        issue = response.json()

        comments_url = issue.get("comments_url")
        comments_response = requests.get(comments_url)
        comments = comments_response.json() if comments_response.status_code == 200 else []

        return {
            "title": issue.get("title", ""),
            "body": issue.get("body", ""),
            "comments": [c.get("body", "") for c in comments]
        }, None

    except Exception as e:
        return None, str(e)
