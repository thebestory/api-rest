"""
The Bestory Project
"""

WARNING = {
    # Object of action warings
    2001: "Unknown user",
    2002: "Unknown topic",
    2003: "Unknown story",
    2004: "Unknown comment",

    # Listing and method limits warnings
    3001: "Incorrect limit",
}

ERROR = {
    # API errors
    1001: "Endpoint not found",
    1002: "Too many requests",
    1003: "Unauthorized",
    1004: "Story not submitted due to server error",
    1005: "Comment not submitted due to server error",
    1006: "Like/Unlike not submitted due to server error",

    # Object of action errors
    2001: "Unknown user",
    2002: "Unknown topic",
    2003: "Unknown story",
    2004: "Unknown comment",

    # Listing and method limits errors
    3001: "Incorrect listing request",
    3002: "Incorrect story submit request",
    3003: "Incorrect comment submit request",

    # Access errors
    4001: "Insufficient permission",
    4002: "Cannot edit a story authored by another user",

    # Submitted content errors
    5001: "User validation error",
    5002: "Cannot send an empty story",
    5003: "Cannot send an empty comment",
    5004: "Too short story",
    5005: "Too short comment",
    5006: "Too long story",
    5007: "Too long comment",
}