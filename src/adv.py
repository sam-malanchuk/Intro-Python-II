from item import Item
from room import Room
from player import Player
import textwrap

# Declare all the items

item = {
    'sword': Item('sword', 'an extremely powerful and reinforced bronze with a sharp double-edged blade'),
    'treasure': Item('treasure', 'something about the treasure box'),
    'shrubs': Item('shrubs', 'something about the mountain shrubs'),
    'coat': Item('coat', 'something about the fur coat'),
    'fish': Item('fish', 'something about the sea fish'),
    'rope': Item('rope', 'something about the rope'),
}

# Declare all the rooms

room = {
    'fay': Room("Fay Pirate Bay", "Here you found an fleet of Pirate ships on the beach. Over to the left near the coconut tree you notice a group of Pirates yelling while all circled around a treasure map. Frightened you need to move on before they notice you are witnessing the scene.", [item['treasure']]),
    'village': Room("Westlight Village", "You were born in this small village and know every brick. As a child you were a troublemaker and have not left a single stone unturned. You're tired of this place and would like to go out and see the world. What adventure lies ahead?", [item['rope']]),
    'mountain': Room("Northcrest Mountain", "You walked for what seemed like weeks and you are finally at the top of mount Northcrest. In the far east you can see the Woodmallow Forest and over to the North you see the Fay Pirate Bay. You realize you can't say up here for long.", [item['shrubs']]),
    'forest': Room("Woodmallow Forest", "It's lighter than you expected, the light shines through the branches creating patterns that almost looks like a path. You start to follow it but realize it's only taking you in circles. Again you'll have to use your compass to keep going.", [item['coat']]),
    'castle': Room("Black Castle", "You sneaked into the castle using a small gate you found over on the northwest corner of the Castle wall. You start looking around and find the citizens of the castle are quite nice. You take a quick note of the location and move on with your journey.", [item['sword']]),
    'island': Room("Glassfall Island", "At last, a few days at sea and you weren't sure if you were going to make it. What can you find here? Is the island inhabited? You do some exploration and find some nice greenry for shelter. You spend the night there and at dawn head out to the mainland again.", [item['fish']]),
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
playerName = input("Enter your character's name: ")
# automatically name the player and start the game for now
player = Player(playerName, room['village'])

# Write a loop that:
#
# * Prints the current room name
print(f'\nWelcome {player.name}, you start in the {player.currentRoom}.\n')
# * Prints the current description (the textwrap module might be useful here).
print(textwrap.fill(player.currentRoom.description, 50))
if len(player.currentRoom.items) > 0:
    print('\nYou found the following items:')
    for item in player.currentRoom.items:
        print(item.name)
else:
    print('\nThere doesn\'t seem to be any items here')
# * Waits for user input and decides what to do.
move = input("\nEnter N, S, W, or E to move in the direction:").lower().split()
# print(f'This whats up:{move}')
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
while move[0] != "q":
    if len(move) == 1:
        # only one word input
        if move[0] == "n":
            if hasattr(player.currentRoom, 'go_n'):
                player.currentRoom = player.currentRoom.go_n
                print(f'You went to the North and ended up in the {player.currentRoom}.\n')
                print(textwrap.fill(player.currentRoom.description, 50))
                if len(player.currentRoom.items) > 0:
                    print('\nYou found the following items:')
                    for item in player.currentRoom.items:
                        print(item.name)
                else:
                    print('\nThere doesn\'t seem to be any items here')
            else:
                print("Nothing but darkness lies ahead. Choose another path.")
        elif move[0] == "e":
            if hasattr(player.currentRoom, 'go_e'):
                player.currentRoom = player.currentRoom.go_e
                print(f'You went to the East and ended up in the {player.currentRoom}.\n')
                print(textwrap.fill(player.currentRoom.description, 50))
                if len(player.currentRoom.items) > 0:
                    print('\nYou found the following items:')
                    for item in player.currentRoom.items:
                        print(item.name)
                else:
                    print('\nThere doesn\'t seem to be any items here')
            else:
                print("Nothing but darkness lies ahead. Choose another path.")
        elif move[0] == "s":
            if hasattr(player.currentRoom, 'go_s'):
                player.currentRoom = player.currentRoom.go_s
                print(f'You went to the South and ended up in the {player.currentRoom}.\n')
                print(textwrap.fill(player.currentRoom.description, 50))
                if len(player.currentRoom.items) > 0:
                    print('\nYou found the following items:')
                    for item in player.currentRoom.items:
                        print(item.name)
                else:
                    print('\nThere doesn\'t seem to be any items here')
            else:
                print("Nothing but darkness lies ahead. Choose another path.")
        elif move[0] == "w":
            if hasattr(player.currentRoom, 'go_w'):
                player.currentRoom = player.currentRoom.go_w
                print(f'You went to the West and ended up in the {player.currentRoom}.\n')
                print(textwrap.fill(player.currentRoom.description, 50))
                if len(player.currentRoom.items) > 0:
                    print('\nYou found the following items:')
                    for item in player.currentRoom.items:
                        print(item.name)
                else:
                    print('\nThere doesn\'t seem to be any items here')
            else:
                print("Nothing but darkness lies ahead. Choose another path.")
        elif move[0] == "i" or move[0] == "inventory":
            if len(player.items) > 0:
                print("You got the following items in your inventory:")
                for item in player.items:
                    print(item.name)
            else:
                print("You don't have any items in your inventory")
                print("Travel around and use \"get\" or \"take\" to pick them up")
        elif move[0] == "help":
            print("\nHere is a list of commands you can use:\n\nDirectional:\nn (goes north from current position)\ne (goes east from current position)\ns (goes south from current position)\nw (goes west from current position)\n\nItems:\ni (lists the items you've picked up)\ninventory (lists the items you\'ve picked up)\nget itemname (replace itemname with the item to pick up from the current location)\ntake itemname (replace itemname with the item to pick up from the current location)\ndrop itemname (replace itemname with the item to drop at the current location)\n\nOthers:\nq (quits the game)\nhelp (provides information on all in-game commands")
        else:
            print("Please enter a valid direction or \'q\' to quit")
        move = input("\nEnter N, S, W, or E to move in the direction:").lower().split()

    else:
        # there are two words
        if move[0] == "take" or move[0] == "get":
            foundItem = False
            for item in player.currentRoom.items:
                if move[1] == item.name:
                    player.currentRoom.items.remove(item)
                    player.items.append(item)
                    print(f'{player.name} picked up the {move[1]} from the {player.currentRoom.name}!')
                    foundItem = True
            if foundItem == False:
                print(f'Could not find \"{move[1]}\" in this area')
        elif move[0] == "drop":
            foundItem = False
            for item in player.items:
                if move[1] == item.name:
                    player.items.remove(item)
                    player.currentRoom.items.append(item)
                    print(f'You\'ve dropped the {item.name} in the {player.currentRoom.name}.')
                    foundItem = True
            if foundItem == False:
                print(f'{player.name} does not have a {move[1]} in the inventory')
        else:
            print("Please enter a valid command or \'q\' to quit")

        move = input("\nEnter N, S, W, or E to move in the direction:").lower().split()


print("Next time don't just quit but finish what you started!")