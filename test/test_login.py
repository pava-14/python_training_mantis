__author__ = 'apavlenko'


def test_login(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_as("administrator")