"""Tiny string helpers for a throwaway toy project."""


def shout(text: str) -> str:
    """Return text in uppercase with a trailing exclamation mark."""
    return text.upper() + "!"


def slugify(text: str) -> str:
    """Turn a title into a URL slug.

    Lowercase the text, replace every run of non-alphanumeric
    characters with a single hyphen, and strip leading/trailing
    hyphens. Example: "Hello, World!" -> "hello-world".
    """
    raise NotImplementedError("slugify is not implemented yet")
