from room import Room

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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

    user_input = input("Enter a direction you want to go in or q to quit: ")
    while user_input:
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
        else:
            print('Wrong input!')
            user_input = input("Enter a direction in n, s, e or w you want to go or q to quit: ")
        
    