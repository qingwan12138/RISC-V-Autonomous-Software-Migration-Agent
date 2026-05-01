from app.agents.repo_agent import RepoAgent
from app.agents.dep_agent import DependencyAgent
from app.agents.build_agent import BuildAgent
from app.agents.diagnose_agent import DiagnoseAgent
from app.agents.patch_agent import PatchAgent
from app.agents.validate_agent import ValidateAgent

class SupervisorAgent:
    def __init__(self):
        self.repo = RepoAgent()
        self.dep = DependencyAgent()
        self.build = BuildAgent()
        self.diagnose = DiagnoseAgent()
        self.patch = PatchAgent()
        self.validate = ValidateAgent()

    def run(self, repo_url, target):
        repo_path = self.repo.clone(repo_url)
        deps = self.dep.scan(repo_path)

        ok, logs = self.build.run(repo_path, target)
        if not ok:
            diagnosis = self.diagnose.analyze(logs)
            self.patch.apply(repo_path, diagnosis)
            ok, logs = self.build.run(repo_path, target)

        runtime_ok = self.validate.run(repo_path, target)

        return {
            "repo": repo_url,
            "dependencies": deps,
            "build_success": ok,
            "runtime_success": runtime_ok
        }
