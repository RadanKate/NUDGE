import pytest


def test_dashboard(dashboard):
    assert dashboard.is_dashboard_page_displayed_correctly()
