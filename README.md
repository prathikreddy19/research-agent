# Research Agent with Learning Feedback Loop

This project demonstrates a simple AI research agent that improves its behaviour over time by learning from its own mistakes. The focus of this project is not perfect answers, but showing how an agent can evaluate its actions, detect errors, and adjust its behaviour in future runs.

## Problem Overview

The agent answers user questions. Some questions are factual and require external information, while others can be answered directly. The agent must decide whether to use a search tool before generating a final answer.

In the initial runs, the agent is intentionally allowed to make mistakes such as skipping the required tool or ignoring tool output. These mistakes are later used to improve the agent’s behaviour.

## Tools Used

- Python
- LangChain (for tool abstraction)
- Custom Search Tool (simulated)

## Agent Behaviour

- Factual questions (e.g. capitals, founders, CEOs) require the use of a search tool.
- Non-factual questions can be answered directly.
- Early runs may contain incorrect behaviour by design.

## Evaluation Logic

After each run, the system evaluates:
- Whether the required tool was used
- Whether the tool output was correctly used
- Whether the final answer was produced at the correct time

Each run is classified as either **SUCCESS** or **FAILURE**, along with a specific mistake type.

## Learning Mechanism

The system maintains a memory of past runs and mistakes. When the same mistake occurs multiple times (for example, skipping the search tool), the agent’s behaviour is updated by enforcing constraints in future runs.

This feedback loop allows the agent to reduce repeated mistakes over time.

## Logs and Improvement

Sample execution logs are available in `logs.txt`.  
These logs show:
- Early incorrect behaviour
- Detection of repeated mistakes
- Learning updates
- Improved behaviour in later runs

## How to Run

```bash
python run.py

Limitations

Learning is rule-based and limited to specific mistake patterns.

The search tool is simulated and not connected to a real API.

More complex reasoning and tools can be added in future versions.


---

## 🔹 STEP 3: Save the File

Press:


Ctrl + S


---

## 🔹 STEP 4: Commit README to Git

Open **VS Code Terminal** and run:

```bash
git add README.md
git commit -m "Add README with project explanation"
git push