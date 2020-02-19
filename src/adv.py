from room import Room

# Declare all the rooms

room = {
    'fay': Room("Fay Pirate Bay", "room action here"),
    'village': Room("Westlight Village", "room action here"),
    'mountain': Room("Northcrest Mountain", "room action here"),
    'forest': Room("Woodmallow Forest", "room action here"),
    'castle': Room("Black Castle", "room action here"),
    'island': Room("Glassfall Island", "room action here"),
}


# Link rooms together

room['fay'].go_e = room['village']
room['fay'].go_s = room['mountain']
room['village'].go_s = room['forest']
room['village'].go_w = room['fay']
room['mountain'].go_e = room['forest']
room['mountain'].go_n = room['fay']
room['forest'].go_n = room['village']
room['forest'].go_e = room['castle']
room['forest'].go_s = room['island']
room['forest'].go_w = room['mountain']
room['castle'].go_w = room['forest']
room['island'].go_n = room['forest']

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
