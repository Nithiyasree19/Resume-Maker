from typing import Any

from config import llm
from utils.parser import parse_json_response


def invoke_json(prompt, variables: dict) -> dict:
    """
    Invoke the LLM and parse the response as JSON.
    """

    chain = prompt | llm

    response = chain.invoke(variables)

    return parse_json_response(response.content)


def invoke_text(prompt, variables: dict) -> str:
    """
    Invoke the LLM and return plain text.
    """

    chain = prompt | llm

    response = chain.invoke(variables)

    return response.content.strip()