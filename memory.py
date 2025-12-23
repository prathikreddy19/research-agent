class Memory:
    def __init__(self):
        self.history = []

    def record(self, run_id: int, question: str, evaluation: dict):
        entry = {
            "run_id": run_id,
            "question": question,
            "status": evaluation["status"],
            "mistake": evaluation["mistake"]
        }
        self.history.append(entry)

    def get_all(self):
        return self.history

    def get_mistakes(self):
        return [h for h in self.history if h["status"] == "FAILURE"]

    def count_mistake(self, mistake_type: str) -> int:
        return sum(1 for h in self.history if h["mistake"] == mistake_type)
