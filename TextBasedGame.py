# Author: Levi Winters
# Date: 12/6/2022

# Function that displays the game instructions to the player
def game_instructions():
    print("Text-Based Adventure Game")
    print(' ' * 20)
    print("You find yourself trapped inside of a haunted house. \nBefore you can leave, you need to collect 6 "
          "items "
          "to defeat a giant spider that is keeping you trapped.")
    print("You will need a book from the library to learn how to defeat the spider.")
    print("Armor from the bedroom to protect your body, a helmet from the cellar to protect your head.")
    print("A sword from the dungeon to stab the spider, a shield from the gallery to protect yourself from the "
          "spider's venom.")
    print("Finally, a healing crystal from the kitchen to keep you alive during the fight.\n")
    print("To travel around the rooms, enter 'north', 'east', 'south', or 'west'.")
    print("Enter 'yes' when prompted to add an item to your inventory.")
    print("Otherwise, enter 'exit' at anytime to quit the game.")
    print(' ' * 20)


def main():
    # Calling the function for displaying the game instructions to the player
    game_instructions()
    # Dictionary containing variables linking rooms to one another and linking items to their corresponding rooms
    rooms = {
        'Great Hall': {'SOUTH': 'Bedroom', 'NORTH': 'Dungeon', 'WEST': 'Library',
                       'EAST': 'Kitchen', 'item': None},
        'Bedroom': {'EAST': 'Cellar', 'NORTH': 'Great Hall', 'item': 'Armor'},
        'Cellar': {'WEST': 'Bedroom', 'item': 'Helmet'},
        'Library': {'EAST': 'Great Hall', 'item': 'Book'},
        'Kitchen': {'WEST': 'Great Hall', 'NORTH': 'Dining Room', 'item': 'Healing Crystal'},
        'Dining Room': {'SOUTH': 'Kitchen', 'item': 'Spider'},  # Spider
        'Dungeon': {'SOUTH': 'Great Hall', 'EAST': 'Gallery', 'item': 'Sword'},
        'Gallery': {'WEST': 'Dungeon', 'item': 'Shield'}
    }

    # Place the player in the starting room and assign each direction
    current_room = 'Great Hall'

    # Initiate a variable for the inventory
    inventory = []

    while True:
        if current_room == 'Dining Room':
            print('\nThe giant spider gazes at you from across the room with its beady eyes glittering with malice.')
            if len(inventory) == 6:  # If the player has all 6 items they will complete the game
                print('You then draw your sword and prepare to strike the head off of this arachnid creature.')
                print('The spider then staggers to its feet and charges. You leap out of its way and slice it in half.')
                print('As the spider tumbles to the floor, you watch the floor crumble beneath its feet.')
                print('You then quickly make your way to the exit of the haunted house.')
                print('At last, you step outside and take a moment to catch your breath and heal up a bit.')
                print('Congratulations! You have collected all items and defeated the spider!')
            else:
                print('Suddenly, the creature lunges with its sharp fangs reminding you that your few remaining '
                      'precious minutes are ticking away.')
                print('A hard snapping sound fills the air as its giant jaws clamp around your body.')
                print('Your breath is suddenly gone. You fall to the ground.')
                print('The spider then devours you! Death has been swiftly unavoidable.')
            break

        if rooms[current_room]['item'] is not None:
            print('You found:', rooms[current_room]['item'])
            take_item = input('Would you like to take the ' + rooms[current_room]['item'] + '?: ').upper()
            if take_item == 'EXIT'.upper():
                break  # Break out of the gameplay loop to exit the game when player is prompted to take an item

            # Input validation for adding an item to the inventory
            while take_item not in ['YES']:
                print('Please enter a valid response.')
                take_item = input('Would you like to take the ' + rooms[current_room]['item'] + '?: ').upper()
            if take_item == 'YES':
                inventory.append(rooms[current_room]['item'])
                rooms[current_room]['item'] = None
        else:
            if current_room != 'Great Hall':
                print('There is nothing else to take in this room.')  # Print when player is in the starting room

        # Display the inventory to the player
        print('Inventory: ', inventory)

        # Receive input from the player for the desired change in direction
        move_direction = input('\nWhich direction would you like to go?: ').upper()
        if move_direction == 'EXIT'.upper():
            break  # Break out of the gameplay loop to exit the game when player is prompted to move around
        directions = list(rooms[current_room].keys())
        directions.remove('item')
        # Input validation for changing direction
        while move_direction not in directions:
            print('You cannot go that way.')
            move_direction = input('\nWhich direction would you like to go instead?: ').upper()

        next_room = rooms[current_room][move_direction]
        print('You make your way to the', next_room + '.')

        current_room = next_room

    print('\nThanks for playing the game. I hope you enjoyed it.')  # This string is printed regardless of the outcome


if __name__ == "__main__":
    main()
