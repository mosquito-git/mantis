

def test_login1(app):
    app.session.login("administrator", "root")
    assert app.session.is_logged_in_as("administrator")