#import json
#
#
#def parse_json_response(response: str) -> dict:
#    """
#    Parse a JSON string returned by the LLM.
#    """
#    return json.loads(response)
#


import json
import re


def parse_json_response(response: str) -> dict:
    """
    Parse JSON returned by the LLM.

    Handles:
    - Raw JSON
    - JSON wrapped in Markdown code fences
    - Leading/trailing whitespace

    Raises:
        ValueError: If valid JSON cannot be extracted.
    """

    response = response.strip()

    # Remove Markdown code fences if present
    response = re.sub(r"^```(?:json)?\s*", "", response)
    response = re.sub(r"\s*```$", "", response)

    try:
        return json.loads(response)

    except json.JSONDecodeError as e:
        raise ValueError(
            f"Failed to parse JSON response from LLM.\nResponse:\n{response}"
        ) from e