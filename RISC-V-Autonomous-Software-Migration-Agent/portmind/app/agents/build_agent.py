import os
import subprocess

class BuildAgent:
    def run(self, repo, target):
        env = os.environ.copy()
        env["CC"] = f"{target}-gcc"

        if (repo / "CMakeLists.txt").exists():
            subprocess.run(["cmake","-B","build","."], cwd=repo, env=env)
            r = subprocess.run(
                ["cmake","--build","build"],
                cwd=repo, env=env, capture_output=True, text=True
            )
            return r.returncode == 0, r.stdout + r.stderr

        r = subprocess.run(
            ["make"], cwd=repo, env=env, capture_output=True, text=True
        )
        return r.returncode == 0, r.stdout + r.stderr
