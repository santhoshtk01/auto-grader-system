import re


def find_score(text):
    """
    This function searches for different score representations in text using regular expressions and returns the score if found.

    Args:
        text (str): The text to search for score representations.

    Returns:
        int: The extracted score if found, otherwise None.
    """
    patterns = [
        r"(\d+) out of (\d+)",  # Matches "X out of Y" format
        r"score of (\d+)",  # Matches "score of X" format
        r"Score: (\d+)/(\d+)",  # Matches "Score: X/Y" format
        r"between a (\d+) and a (\d+)",  # Matches "between a X and a Y" format
    ]

    for pattern in patterns:
        match = re.search(
            pattern, text, re.IGNORECASE
        )  # Search with case-insensitive matching
        if match:
            if len(match.groups()) == 1:  # "between a X and a Y" format
                return int(match.group(1))  # Return the first captured group (score)
            else:
                # For other formats, return the first captured group (score)
                return int(match.group(1))

    return None
