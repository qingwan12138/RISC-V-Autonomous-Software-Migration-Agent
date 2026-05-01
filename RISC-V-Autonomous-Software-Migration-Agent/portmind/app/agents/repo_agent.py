import subprocess
from pathlib import Path

class RepoAgent:
    def clone(self, repo_url):
        name = repo_url.split("/")[-1].replace(".git","")
        path = Path("workspace") / name
        if not path.exists():
            subprocess.run(["git","clone",repo_url,str(path)], check=False)
        return path
