# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.list = []
        
    def update_room(self, new_room):
        self.current_room = new_room

    def add_item(self, item):
        self.list.append(item)
    
    def remove_item(self, item):
        del self.list[self.list.index(item)]
        