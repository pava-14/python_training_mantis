__author__ = 'apavlenko'

from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def get_projects_count(self):
        wd = self.app.wd
        self.app.menu.open_manage_projects()
        projects_table_rows = wd.find_elements_by_css_selector('table[cellspacing="1"].width100 tr')
        return len(projects_table_rows) - 2

    def get_projects_list(self):
        caption_offset = 2
        row_selector = 'table[cellspacing="1"].width100 tr'
        project_list = []
        wd = self.app.wd
        self.app.menu.open_manage_projects()
        all_row_count = len(wd.find_elements_by_css_selector(row_selector))
        projects_count = all_row_count - caption_offset
        for i in range(projects_count):
            project_properties = wd.find_elements_by_css_selector(f'.row-{i + 1} td')
            project_list.append(Project(name=project_properties[0].text,
                                        status=project_properties[1].text,
                                        enabled=project_properties[2].text,
                                        view_status=project_properties[3].text,
                                        description=project_properties[4].text))
        return project_list

    def add_new_project(self):
        pass

    def delete_project_by_name(self):
        pass
