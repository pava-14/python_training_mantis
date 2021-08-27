__author__ = 'apavlenko'

import random
import string
from sys import maxsize


class Project:
    def __init__(self, project_id=None, name=None, status=None, enabled=None, igc=None, view_status=None,
                 description=None):
        self.project_id = project_id
        self.name = name
        self.status = status
        self.enabled = enabled
        self.igc = igc
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return f"{self.project_id}:{self.name}:{self.status}:{self.enabled}:{self.view_status}:{self.description}"

    def __eq__(self, other):
        if not isinstance(other, Project):
            return False
        return self.name == other.name and self.status == other.status and self.description == other.description

    def id_or_max(self):
        if self.project_id:
            return int(self.project_id)
        else:
            return maxsize

    @staticmethod
    def get_random_project_data():
        return Project(name=Project.get_random_project_name(),
                       status=random.choice(Project.get_available_project_status()),
                       igc=Project.get_random_flag(),
                       enabled=Project.get_random_flag(),
                       view_status=random.choice(Project.get_available_project_view_status()),
                       description=Project.get_random_project_description())

    @staticmethod
    def get_random_project_name():
        symbols = string.ascii_letters + string.digits
        return "Project " + "".join([random.choice(symbols) for i in range(random.randrange(6, 10))])

    @staticmethod
    def get_random_project_description():
        symbols = string.ascii_letters + string.digits
        return "Some description " + "".join([random.choice(symbols) for i in range(random.randrange(10, 20))])

    @staticmethod
    def get_available_project_status():
        return ['development', 'release', 'stable', 'obsolete']

    @staticmethod
    def get_available_project_view_status():
        return ['public', 'private']

    @staticmethod
    def get_random_flag():
        return str(random.randint(0, 1))
