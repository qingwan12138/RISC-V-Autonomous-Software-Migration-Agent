import subprocess

class ValidateAgent:
    def run(self, repo, target):
        bins = [f for f in repo.rglob("*") if f.is_file() and f.stat().st_mode & 0o111]
        if not bins:
            return False

        qemu = f"qemu-{target.split('-')[0]}"
        r = subprocess.run([qemu, str(bins[0])], capture_output=True, text=True)
        return r.returncode == 0
