# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.list = []

    def add_item(self, item):
        self.list.append(item)

    def remove_item(self, item):
        del self.list[self.list.index(item)]

