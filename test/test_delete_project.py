__author__ = 'apavlenko'

import random

from model.project import Project


def test_delete_project(app):
    app.session.login("administrator", "root")
    current_list = app.projects.get_projects_list()
    if len(current_list) == 0:
        app.projects.add_new_project(Project.get_random_project_data())
        current_list = app.projects.get_projects_list()
    project_for_delete = random.choice(current_list)
    app.projects.delete_project(project_for_delete)
    new_list = app.projects.get_projects_list()
    current_list.remove(project_for_delete)
    assert sorted(current_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
