from toybox import shout, slugify


def test_shout():
    assert shout("hello") == "HELLO!"


def test_slugify_basic():
    assert slugify("Hello, World!") == "hello-world"


def test_slugify_runs_and_edges():
    assert slugify("  --Already -- Slugged-- ") == "already-slugged"


def test_slugify_numbers():
    assert slugify("Top 10 Reasons!") == "top-10-reasons"
