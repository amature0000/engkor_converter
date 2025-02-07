import requests
import re

OWNER = "amature0000"
REPO = "engkor_converter"

def get_latest_release() -> str:
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/releases/latest"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        latest_version = data.get("tag_name")
        release_notes = data.get("body")
        if latest_version and release_notes:            
            cleaned_notes = re.sub(r'^.*## 변경사항', '', release_notes, flags=re.DOTALL)
            cleaned_notes = re.sub(r'## 다운로드 파일.*$', '', cleaned_notes, flags=re.DOTALL)
            filtered_notes = cleaned_notes.strip()
            return latest_version, filtered_notes
        else:
            return "No releases found", "오류: 릴리즈를 확인할 수 없습니다."
    else:
        return f"Failed to fetch release info: {response.status_code}", "오류: 릴리즈를 확인할 수 없습니다."
