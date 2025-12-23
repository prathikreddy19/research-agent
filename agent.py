import random
from langchain_core.tools import Tool
from langchain_community.llms.fake import FakeListLLM
from tools import search_tool


class NaiveResearchAgent:
    def __init__(self):
        self.force_search = False  # learning constraint

        self.llm = FakeListLLM(
            responses=[
                "I think I can answer this directly.",
                "Let me search for this information.",
                "Here is the final answer."
            ]
        )

        self.search = Tool(
            name="SearchTool",
            func=search_tool.run,
            description="Use this tool to find factual information."
        )

    def run(self, question: str, factual: bool) -> dict:
        """
        Executes one run of the agent.
        """
        # Apply learning constraint
        if self.force_search and factual:
            used_tool = True
        else:
            used_tool = random.choice([True, False])

        tool_output = None

        if used_tool:
            tool_output = self.search.func(question)
            # Still allow mistakes initially
            if random.choice([True, False]):
                final_answer = tool_output
            else:
                final_answer = "Ignored tool output."
        else:
            final_answer = "Answered directly without using search."

        return {
            "question": question,
            "used_tool": used_tool,
            "tool_output": tool_output,
            "final_answer": final_answer
        }
