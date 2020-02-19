from room import Room
from player import Player
import textwrap

# Declare all the rooms

room = {
    'fay': Room("Fay Pirate Bay", "Here you found an fleet of Pirate ships on the beach. Over to the left near the coconut tree you notice a group of Pirates yelling while all circled around a treasure map. Frightened you need to move on before they notice you are witnessing the scene."),
    'village': Room("Westlight Village", "You were born in this small village and know every brick. As a child you were a troublemaker and have not left a single stone unturned. You're tired of this place and would like to go out and see the world. What adventure lies ahead?"),
    'mountain': Room("Northcrest Mountain", "You walked for what seemed like weeks and you are finally at the top of mount Northcrest. In the far east you can see the Woodmallow Forest and over to the North you see the Fay Pirate Bay. You realize you can't say up here for long."),
    'forest': Room("Woodmallow Forest", "It's lighter than you expected, the light shines through the branches creating patterns that almost looks like a path. You start to follow it but realize it's only taking you in circles. Again you'll have to use your compass to keep going."),
    'castle': Room("Black Castle", "You sneaked into the castle using a small gate you found over on the northwest corner of the Castle wall. You start looking around and find the citizens of the castle are quite nice. You take a quick note of the location and move on with your journey."),
    'island': Room("Glassfall Island", "At last, a few days at sea and you weren't sure if you were going to make it. What can you find here? Is the island inhabited? You do some exploration and find some nice greenry for shelter. You spend the night there and at dawn head out to the mainland again."),
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
print(f'You start in the {player.currentRoom}.')
# * Prints the current description (the textwrap module might be useful here).
print(textwrap.fill(player.currentRoom.description, 50))
# * Waits for user input and decides what to do.
move = input("Enter N, S, W, or E to move in the direction:").lower()
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while move != "q":
    if move == "n":
        if hasattr(player.currentRoom, 'go_n'):
            player.currentRoom = player.currentRoom.go_n
            print(f'You went to the North and ended up in the {player.currentRoom}.\n')
            print(textwrap.fill(player.currentRoom.description, 50))
        else:
            print("Nothing but darkness lies ahead. Choose another path.")
    elif move == "e":
        if hasattr(player.currentRoom, 'go_e'):
            player.currentRoom = player.currentRoom.go_e
            print(f'You went to the East and ended up in the {player.currentRoom}.\n')
            print(textwrap.fill(player.currentRoom.description, 50))
        else:
            print("Nothing but darkness lies ahead. Choose another path.")
    elif move == "s":
        if hasattr(player.currentRoom, 'go_s'):
            player.currentRoom = player.currentRoom.go_s
            print(f'You went to the South and ended up in the {player.currentRoom}.\n')
            print(textwrap.fill(player.currentRoom.description, 50))
        else:
            print("Nothing but darkness lies ahead. Choose another path.")
    elif move == "w":
        if hasattr(player.currentRoom, 'go_w'):
            player.currentRoom = player.currentRoom.go_w
            print(f'You went to the West and ended up in the {player.currentRoom}.\n')
            print(textwrap.fill(player.currentRoom.description, 50))
        else:
            print("Nothing but darkness lies ahead. Choose another path.")
    else:
        print("Please enter a valid direction or \'q\' to quit")
    move = input("\nEnter N, S, W, or E to move in the direction:").lower()

print("Next time don't just quit but finish what you started!")