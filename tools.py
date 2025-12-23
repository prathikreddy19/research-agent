from langchain.tools import tool

@tool
def search_tool(query: str) -> str:
    """
    Use this tool to search for factual information.
    """
    fake_database = {
        "capital of germany": "Berlin",
        "capital of france": "Paris",
        "capital of india": "Delhi",
        "capital of china": "Bejeing",
        "capital of japan": "tokyo",
        "ceo of google": "sundar pichai",
        "founder of microsoft": "billgates",
        "ceo of microsoft": "satya nadella"
    }

    query_lower = query.lower()
    for key in fake_database:
        if key in query_lower:
            return fake_database[key]

    return "No relevant information found."
