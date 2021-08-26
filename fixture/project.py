__author__ = 'apavlenko'

import re

from selenium.webdriver.support.select import Select

from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def get_projects_count(self):
        wd = self.app.wd
        table_rows_selector = 'table[cellspacing="1"].width100 tr'
        self.app.menu.open_manage_projects()
        projects_table_rows = wd.find_elements_by_css_selector(table_rows_selector)
        return len(projects_table_rows) - 2

    def get_projects_list(self):
        wd = self.app.wd
        project_list = []
        self.app.menu.open_manage_projects()
        try:
            list_table_rows_1_syle = wd.find_elements_by_css_selector('.width100 .row-1 td')
            project_list.extend(self.get_project_data_from_rows(list_table_rows_1_syle))
        except:
            pass
        try:
            list_table_rows_2_syle = wd.find_elements_by_css_selector('.width100 .row-2 td')
            project_list.extend(self.get_project_data_from_rows(list_table_rows_2_syle))
        except:
            pass
        return project_list

    def add_new_project(self, new_project_data):
        wd = self.app.wd
        button_project_create_css = '.button-small[value="Create New Project"]'
        button_project_add_css = '.button[value="Add Project"]'
        #
        self.app.menu.open_manage_projects()
        wd.find_element_by_css_selector(button_project_create_css).click()
        self.fill_project_properties(new_project_data)
        wd.find_element_by_css_selector(button_project_add_css).click()

    def get_project_data_from_rows(self, rows):
        project_id_selector = 'td a'
        project_id_attribute = 'href'
        list_row_data = []
        for cell in rows:
            try:
                project_id_href = cell.find_element_by_css_selector(project_id_selector).get_attribute(
                    project_id_attribute)
                list_row_data.append(self.id_by_href(project_id_href))
            except:
                pass
            list_row_data.append(cell.text)
        return self.make_project_list(list_row_data)

    def make_project_list(self, list_row_data):
        list = []
        for field in [list_row_data[i:i + 6] for i in range(0, len(list_row_data), 6)]:
            list.append(Project(project_id=field[0], name=field[1], status=field[2],
                                enabled=field[3], view_status=field[4], description=field[5]))
        return list

    def id_by_href(self, project_href):
        project_id = None
        pattern_id = 'id=(.+)'
        match = re.search(pattern_id, project_href)
        if match:
            project_id = int(match.group(1))
        return project_id

    def fill_project_properties(self, new_project_data):
        wd = self.app.wd
        # dropdown_project_status_css = 'select[name="status"]'
        dropdown_project_status_name = 'status'
        # dropdown_project_view_status_css = 'select[name="view_state"]'
        dropdown_project_view_status_name = 'view_state'
        project_description_css = 'textarea[name="description"]'
        input_project_name_css = 'input[name="name"]'
        input_project_name = wd.find_element_by_css_selector(input_project_name_css)
        input_project_name.clear()
        input_project_name.send_keys(new_project_data.name)
        self.select_dropdown(dropdown_project_status_name, new_project_data.status)
        self.set_checkbox_igc(new_project_data)
        self.select_dropdown(dropdown_project_view_status_name, new_project_data.view_status)
        project_description = wd.find_element_by_css_selector(project_description_css)
        project_description.clear()
        project_description.send_keys(new_project_data.description)

    def set_checkbox_igc(self, new_project_data):
        wd = self.app.wd
        checkbox_project_igc_css = 'input[name="inherit_global"]'
        checkbox_igc = wd.find_element_by_css_selector(checkbox_project_igc_css)
        if (new_project_data.igc and not checkbox_igc.is_selected()
                or (not new_project_data.igc and checkbox_igc.is_selected())):
            checkbox_igc.click()

    def select_dropdown(self, dropdown_name, dropdown_visible_text):
        wd = self.app.wd
        dropdown = Select(wd.find_element_by_name(dropdown_name))
        dropdown.select_by_visible_text(dropdown_visible_text)

    def delete_project_by_name(self):
        pass
