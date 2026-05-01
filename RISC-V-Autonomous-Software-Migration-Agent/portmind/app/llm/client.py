class LLMClient:
    def analyze(self, logs):
        if "undefined reference" in logs:
            return {"fix": "missing link library"}
        if "No such file or directory" in logs:
            return {"fix": "missing dependency"}
        return {"fix": "manual review required"}
