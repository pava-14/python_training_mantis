__author__ = 'apavlenko'

import random

from model.project import Project


def test_edit_project(app):
    app.session.login("administrator", "root")
    current_list = app.projects.get_projects_list()
    if len(current_list) == 0:
        app.projects.add_new_project(Project.get_random_project_data())
        current_list = app.projects.get_projects_list()
    new_project_data = Project.get_random_project_data()
    project_for_edit = random.choice(current_list)
    # Keep current project_id
    new_project_data.project_id = project_for_edit.project_id
    app.projects.edit_project(project_for_edit, new_project_data)
    new_list = app.projects.get_projects_list()
    current_list[current_list.index(project_for_edit)] = new_project_data
    assert sorted(current_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
