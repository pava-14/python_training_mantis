__author__ = 'apavlenko'


def test_add_new_project(app):
    app.session.login("administrator", "root")
    current_list = app.projects.get_projects_list()
    print(f"\n{current_list}")
