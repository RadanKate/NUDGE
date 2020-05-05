import pytest


def test_dashboard(dashboard):
    assert (dashboard.is_inside_dashboard_page() == True)
