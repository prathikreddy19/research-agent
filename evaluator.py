def is_factual_question(question: str) -> bool:
    keywords = ["capital", "ceo", "founder", "population", "when", "who"]
    return any(keyword in question.lower() for keyword in keywords)


def evaluate_run(run_result: dict) -> dict:
    """
    Evaluates agent behavior and detects mistakes.
    """
    question = run_result["question"]
    used_tool = run_result["used_tool"]
    tool_output = run_result["tool_output"]
    final_answer = run_result["final_answer"]

    factual = is_factual_question(question)

    if factual:
        if not used_tool:
            return {"status": "FAILURE", "mistake": "TOOL_NOT_USED"}

        if used_tool and tool_output and final_answer != tool_output:
            return {"status": "FAILURE", "mistake": "TOOL_OUTPUT_IGNORED"}

        if used_tool and not tool_output:
            return {"status": "FAILURE", "mistake": "ANSWER_TOO_EARLY"}

    return {"status": "SUCCESS", "mistake": None}
