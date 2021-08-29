from selenium import webdriver

from fixture.james import JamesHelper
from fixture.menu import MenuHelper
from fixture.project import ProjectHelper
from fixture.session import SessionHelper


class Application:
    def __init__(self, browser, config):
        if browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError(f"Unrecognized browser {browser}")
        # self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.menu = MenuHelper(self)
        self.projects = ProjectHelper(self)
        self.james = JamesHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url()
            return True
        except Exception:
            print(Exception)
            return False

    def open_home_page(self):
        wd = self.wd
        if not (wd.current_url.endswith("/index.php") and len(wd.find_elements_by_id("search_count")) > 0):
            wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()

    def destroy(self):
        self.wd.quit()
