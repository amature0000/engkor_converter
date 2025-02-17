import requests

OWNER = "amature0000"
REPO = "engkor_converter"

def get_latest_release() -> str:
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"
    response = requests.get(url)

    if response.status_code == 200:
        latest_version = response.json().get("tag_name")
        return latest_version if latest_version else "No releases found"
    else:
        return f"Failed to fetch release info: {response.status_code}"