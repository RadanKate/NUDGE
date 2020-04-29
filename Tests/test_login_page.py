import pytest


def test_login(login):
    login.login()
    assert (login.is_login_error_displayed() == False)
