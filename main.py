import pytest
# adding comment for git commit

def always_returns_true():
    return False


def test_always_returns_true():
    assert always_returns_true()
