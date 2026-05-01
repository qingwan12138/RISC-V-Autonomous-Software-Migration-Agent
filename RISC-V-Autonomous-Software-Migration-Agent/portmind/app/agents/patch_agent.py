from pathlib import Path

class PatchAgent:
    def apply(self, repo, diagnosis):
        patch = Path(repo) / "auto_fix.patch"
        patch.write_text(str(diagnosis), encoding="utf-8")
        return patch
