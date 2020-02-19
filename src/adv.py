from room import Room
from player import Player

# Declare all the rooms

room = {
    'fay': Room("Fay Pirate Bay", "fay"),
    'village': Room("Westlight Village", "village"),
    'mountain': Room("Northcrest Mountain", "mountain"),
    'forest': Room("Woodmallow Forest", "forest"),
    'castle': Room("Black Castle", "castle"),
    'island': Room("Glassfall Island", "island"),
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
print("\nWelcome to Meadowswamp Adventure!\nTo navigate around you will use the cardinal directions\nNorth (N), East (E), South (S), and West (W).\nYou can use \'q\' at any time to leave the game.\n")
# playerName = input("Enter your character's name: ")
# automatically name the player and start the game for now
player = Player("Ethan", room['village'])

# Write a loop that:
#
# * Prints the current room name
print(f'You now entered the {player.currentRoom}.')
# * Prints the current description (the textwrap module might be useful here).
print(f'You are now in the {player.currentRoom.action} room')
# * Waits for user input and decides what to do.
move = input("Enter N, S, W, or E to move that direction:").lower()
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while move != "q":
    if move == "n":
        if hasattr(player.currentRoom, 'go_n'):
            print(player.currentRoom.go_n)
            player.currentRoom = player.currentRoom.go_n
        else:
            print("Nothing but darkness lies ahead. Choose another path.")
    elif move == "e":
        if hasattr(player.currentRoom, 'go_e'):
            print(player.currentRoom.go_e)
            player.currentRoom = player.currentRoom.go_e
        else:
            print("Nothing but darkness lies ahead. Choose another path.")
    elif move == "s":
        if hasattr(player.currentRoom, 'go_s'):
            print(player.currentRoom.go_s)
            player.currentRoom = player.currentRoom.go_s
        else:
            print("Nothing but darkness lies ahead. Choose another path.")
    elif move == "w":
        if hasattr(player.currentRoom, 'go_w'):
            print(player.currentRoom.go_w)
            player.currentRoom = player.currentRoom.go_w
        else:
            print("Nothing but darkness lies ahead. Choose another path.")
    else:
        print("*Please enter a valid direction*")
    move = input("Enter N, S, W, or E to move that direction:").lower()

print("Next time don't just quit but finish what you started!")