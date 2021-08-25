__author__ = 'apavlenko'


class Project:
    def __init__(self, id=None, name=None, status=None, enabled=None, igc=None, view_status=None, description=None):
        self.id = id
        self.name = name
        self.status = status
        self.enabled = enabled
        self.igc = igc
        self.view_status = view_status
        self.description = description

    def __repr__(self):
        return f"{self.name}:{self.status}:{self.enabled}:{self.view_status}:{self.description}"

    def __eq__(self, other):
        if not isinstance(other, Project):
            return False
        return self.name == other.name and self.status == other.status and self.description == other.description
