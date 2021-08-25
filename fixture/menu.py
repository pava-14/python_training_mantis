__author__ = 'apavlenko'


class MenuHelper:
    def __init__(self, app):
        self.app = app

    def open_manage_projects(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def main_my_view(self):
        wd = self.app.wd
        pass
