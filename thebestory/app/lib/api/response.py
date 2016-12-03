"""
The Bestory Project
"""

from collections import OrderedDict

from thebestory.app.lib.api.code import WARNING, ERROR

__all__ = [
    "ok",
    "warning",
    "error"
]


def ok(data):
    return OrderedDict(
        status="ok",
        data=data
    )


def warning(code, data):
    return OrderedDict(
        status="warning",
        warning=OrderedDict(
            code=code,
            message=WARNING[code]
        ),
        data=data
    )


def error(code):
    return OrderedDict(
        status="error",
        error=OrderedDict(
            code=code,
            message=ERROR[code]
        )
    )
