__author__ = 'apavlenko'

import random

from model.project import Project


def test_add_new_project(app):
    app.session.login("administrator", "root")
    current_list = app.projects.get_projects_list()
    new_project_data = Project.get_random_project_data()
    app.projects.add_new_project(new_project_data)
    new_list = app.projects.get_projects_list()
    current_list.append(new_project_data)
    # debug
    print(f"\n***\nCurrent List:{current_list}")
    print(f"\nNew Item:{new_project_data}")
    print(f"\nNew List:{new_list}\n***")
    assert sorted(current_list, key=Project.id_or_max) == sorted(new_list, key=Project.id_or_max)
