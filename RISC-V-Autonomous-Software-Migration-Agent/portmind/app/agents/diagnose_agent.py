from app.llm.client import LLMClient

class DiagnoseAgent:
    def __init__(self):
        self.llm = LLMClient()

    def analyze(self, logs):
        return self.llm.analyze(logs)
