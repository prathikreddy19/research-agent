from agent import NaiveResearchAgent
from evaluator import evaluate_run, is_factual_question
from memory import Memory

agent = NaiveResearchAgent()
memory = Memory()

question = "What is the capital of Germany?"

for run_id in range(1, 7):
    print(f"\n--- RUN {run_id} ---")

    factual = is_factual_question(question)
    result = agent.run(question, factual)
    evaluation = evaluate_run(result)

    memory.record(run_id, question, evaluation)

    print("Question:", result["question"])
    print("Used Tool:", result["used_tool"])
    print("Tool Output:", result["tool_output"])
    print("Final Answer:", result["final_answer"])
    print("Evaluation:", evaluation)

    tool_skip_count = memory.count_mistake("TOOL_NOT_USED")
    if tool_skip_count >= 2 and not agent.force_search:
        agent.force_search = True
        print("LEARNING UPDATE:")
        print("- Detected repeated TOOL_NOT_USED mistakes")
        print("- Enforcing mandatory search tool usage for factual questions")

print("\nFinal Memory:")
for entry in memory.get_all():
    print(entry)
