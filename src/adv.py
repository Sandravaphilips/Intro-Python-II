from room import Room
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'first': Item('pen', 'used for writing'),
    'second': Item('book', 'for readin purposes'),
    'third': Item('laptop', 'Can perform a number of operations'),
    'fourth': Item('phone', 'for making and receiving calls'),
    'fifth': Item('bucket', 'for fetching water')
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].list = [items['first'], items['second']]
room['foyer'].list = [items['third'], items['fourth']]
room['overlook'].list = [items['fifth']]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

import textwrap
from player import Player

player_name = input("Enter your name: ")
players_room = room['outside']

new_player = Player(player_name, room['outside'])

wrapper = textwrap.TextWrapper(width=50) 

while players_room:
    print(new_player.current_room.name)
    word_list = wrapper.wrap(text=new_player.current_room.description) 
    for element in word_list: 
        print(element) 
    if len(new_player.current_room.list) == 0:
        print("There are no items in this room")
    else:
        print('Items available in this room are: ')
        for itm in new_player.current_room.list:
            print(itm.name)

    user_input = input("Enter an item you wat to take, a direction you want to go in or q to quit: ")
    split_input = user_input.split()
    while len(split_input) == 1:
        if user_input == 'n' or user_input == 's'or user_input == 'e' or user_input == 'w':
            if user_input == 'n':
                new_room = new_player.current_room.n_to
            elif user_input == 's':
                new_room = new_player.current_room.s_to
            elif user_input == 'e':
                new_room = new_player.current_room.e_to
            else:
                new_room = new_player.current_room.w_to
            if not new_room:
                print('Movement in that direction is not allowed!')
            new_player.update_room(new_room)
            players_room = new_room
            break
        elif user_input == 'q':
            print('Thank you for playing our game. Hope to see you soon.') 
            players_room = ''
            break
        elif user_input == 'i':
            if len(new_player.list) == 0:
                print('You have no items')
            else:
                print('Items you have currently are: ')
                for itm in new_player.list:
                    print(itm.name)
            break
        else:
            print('Wrong input!')
            user_input = input("Enter an item you wat to take, a direction you want to go in or q to quit: ")

    if len(split_input) == 2:
        action = split_input[0]
        action_item = split_input[1]
        room_item = [i for i in new_player.current_room.list if i.name == action_item]
        player_item = [i for i in new_player.list if i.name == action_item]

        if action == 'get' or action == 'drop':
            if len(room_item) > 0 or len(player_item) > 0:
                if action == 'get':
                    new_player.current_room.remove_item(room_item[0])
                    new_player.add_item(room_item[0])
                    print(room_item[0].on_take())
                else:
                    new_player.current_room.add_item(player_item[0])
                    new_player.remove_item(player_item[0])
                    print(player_item[0].on_drop())
            else: 
                print(f'There is no {action_item} in your room ')            
        else:
            print('Please enter a valid action')

        
    
        
    