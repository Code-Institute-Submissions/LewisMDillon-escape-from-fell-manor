import time
import sys
import os
import random
import art
import gametext


def clear():
    os.system('clear')


def type_effect(text, speed=0.04):
    '''
    prints out text letter by letter, adjust speed argument
    to change speed, lower is faster
    '''
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)


CENT = "{:^80}".format  # variable for centering text in terminal


def paragraph():
    print("\n\n")


def confirm():
    paragraph()
    input(CENT("-- Press ENTER to continue --"))
    clear()


def display_title_screen():
    """
    Displays the Main Game Logo
    """
    clear()
    TITLE = art.TITLE
    type_effect(TITLE, 0.002)
    confirm()
    display_main_menu()


def display_main_menu():
    """
    Displays the main menu
    """
    clear()
    MAIN_MENU = art.MAIN_MENU
    type_effect(MAIN_MENU, 0.003)
    paragraph()
    print(CENT("Type 'play', 'help', or 'quit'"))
    title_screen_options()


def title_screen_options():
    """
    presents user with different selectable options at
    the title screen
    """
    option = input('\n> ')
    if option.lower().strip() == ('play'):
        player_setup()
        game_introduction()
    elif option.lower().strip() == ('help'):
        help_screen()
    elif option.lower().strip() == ('quit'):
        quit_game()
    elif option.lower().strip() == ('test'):
        test_function()
    else:
        print('Please type play, help, or quit')
        confirm()
        display_main_menu()
        title_screen_options()


def help_screen():
    """
    Displays the game instructions on ASCII art
    background
    """
    clear()
    HELP = art.HELP
    print(HELP)
    confirm()
    display_main_menu()
    title_screen_options()


def quit_game():
    print('Exiting Game...')
    sys.exit()


# Player Setup ############
class Player:
    """
    Player character class
    """
    def __init__(
        self, name, location, health, weapon, strength, shield, armour,
        lantern, manormap, eyeglass, silver_key, password
                ):
        self.name = name
        self.location = location
        self.health = health
        self.weapon = weapon
        self.shield = shield
        self.strength = strength
        self.armour = armour
        self.lantern = lantern
        self.manormap = manormap
        self.eyeglass = eyeglass
        self.silver_key = silver_key
        self.password = password


myPlayer = Player(
    'Player', 'c3', 10, 'No Weapon', 2, 'No Shield', 2,
    False, False, False, False, False
    )


# Enemies Setup ###########
class Monster:
    """
    Monster class
    """
    def __init__(self, name, health, strength, armour):
        self.name = name
        self.health = health
        self.strength = strength
        self.armour = armour


ogre = Monster('Ogre', 10, 4, 2)
haunted_chest = Monster('Haunted Chest', 12, 5, 2)
gorehowl = Monster('Gorehowl', 20, 8, 1)


class Weapon:
    """
    Weapon class
    """
    def __init__(self, name, strength):
        self.name = name
        self.strength = strength


rusty_dagger = Weapon('RUSTY DAGGER', 4)
silver_sword = Weapon('SILVER SWORD', 8)


class Shield:
    """
    Shield class
    """
    def __init__(self, name, armour):
        self.name = name
        self.armour = armour


wooden_shield = Shield('Wooden Shield', 4)
iron_shield = Shield('Iron Shield', 8)


def player_setup():
    """
    Sets player starting attributes to default values
    """
    myPlayer.name = 'Player'
    myPlayer.location = 'c3'
    myPlayer.health = 10
    myPlayer.weapon = 'No Weapon'
    myPlayer.strength = 2
    myPlayer.shield = 'No Shield'
    myPlayer.armour = 2
    myPlayer.lantern = False
    myPlayer.manormap = False
    myPlayer.eyeglass = False
    myPlayer.silver_key = False
    myPlayer.password = False


def inventory_screen():
    """
    Displays the player inventory, lists all weapons,
    equipment, and items the player has found & displays player health
    """
    print("\nHere are the items and equipment " 
          "that you have gathered on your journey so far:")
    if myPlayer.weapon == 'Rusty Dagger':
        print(
            f"\nWeapon: {myPlayer.weapon} -- +{rusty_dagger.strength - 2} damage"
            )
    elif myPlayer.weapon == 'Silver Sword':
        print(
            f"\nWeapon: {myPlayer.weapon} -- +{silver_sword.strength - 2} damage"
            )
    else:
        print(f"\nWeapon: {myPlayer.weapon}")

    if myPlayer.shield == 'Wooden Shield':
        print(
            f"\nShield: {myPlayer.shield} -- +{wooden_shield.armour - 2} armour"
            )
    elif myPlayer.shield == 'Iron Shield':
        print(
            f"\nShield: {myPlayer.shield} -- +{iron_shield.armour - 2} armour"
            )
    else:
        print(f"\nShield: {myPlayer.shield}")
    print("\nOther items:")
    if myPlayer.lantern:
        print("Lantern")
    else:
        print("None")
    if myPlayer.manormap:
        print("Map")
    if myPlayer.eyeglass:
        print("Eyeglass")
    if myPlayer.silver_key:
        print("Silver Key")
    
    print(f"\n Your health is currently at {myPlayer.health}")
    

def display_map():
    print(f"{map_dict[myPlayer.location]}")


# Test Function #######################
def test_function():
    print('The test function ran successfuly')
    print(f"the player is currently in room {myPlayer.location}")
    calculate_valid_directions()
    

# Map ########
#     _________________
#     |a1 |a2 |a3 |a4 |
#     |___|___|___|___|
#     |b1 |b2 |b3 |b4 |
#     |___|___|___|___|
#     |c1 |c2 |c3 |c4 |
#     |___|___|___|___|
#     |d1 |d2 |d3 |d4 |
#     |___|___|___|___|

room_map = {
    'a1': {
        'room_name': 'Study',
        'description': (f"{gametext.room_descriptions['a1']}"),
        'details': (f"{gametext.room_details['a1']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b1',
        'east': 'a2',
        'west': False
    },
    'a2': {
        'room_name': 'Black Chasm',
        'description': (f"{gametext.room_descriptions['a2']}"),
        'details': (f"{gametext.room_details['a2']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'a3',
        'west': False
    },
    'a3': {
        'room_name': 'Library',
        'description': (f"{gametext.room_descriptions['a3']}"),
        'details': (f"{gametext.room_details['a3']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'a4',
        'west': 'a2'
    },
    'a4': {
        'room_name': 'Dining room',
        'description': (f"{gametext.room_descriptions['a4']}"),
        'details': (f"{gametext.room_details['a4']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': 'b4',
        'east': False,
        'west': 'a3'
    },
    'b1': {
        'room_name': 'Upstairs Corridor',
        'description': (f"{gametext.room_descriptions['b1']}"),
        'details': (f"{gametext.room_details['b1']}"),
        'entered': False,
        'completed': False,
        'north': 'a1',
        'south': 'c1',
        'east': 'b2',
        'west': False
    },
    'b2': {
        'room_name': 'Arena',
        'description': (f"{gametext.room_descriptions['b2']}"),
        'details': (f"{gametext.room_details['b2']}"),
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': False,
        'west': 'b1'
    },
    'b3': {
        'room_name': 'Storage Room',
        'description': (f"{gametext.room_descriptions['b3']}"),
        'details': (f"{gametext.room_details['b3']}"),
        'entered': False,
        'looked': False,
        'lantern_looked': False,
        'completed': False,
        'north': False,
        'south': 'c3',
        'east': 'b4',
        'west': False
    },
    'b4': {
        'room_name': 'Grand Hall',
        'description': (f"{gametext.room_descriptions['b4']}"),
        'details': (f"{gametext.room_details['b4']}"),
        'entered': False,
        'completed': False,
        'north': 'a4',
        'south': 'c4',
        'east': False,
        'west': 'b3'
    },
    'c1': {
        'room_name': 'Final Door',
        'description': (f"{gametext.room_descriptions['c1']}"),
        'details': (f"{gametext.room_details['c1']}"),
        'entered': False,
        'completed': False,
        'north': 'b1',
        'south': False,
        'east': False,
        'west': False
    },
    'c2': {
        'room_name': 'Alcove',
        'description': (f"{gametext.room_descriptions['c2']}"),
        'details': (f"{gametext.room_details['c2']}"),
        'entered': False,
        'completed': False,
        'north': 'b2',
        'south': False,
        'east': False,
        'west': False
    },
    'c3': {
        'room_name': 'Prison Cell',
        'description': (f"{gametext.room_descriptions['c3']}"),
        'details': (f"{gametext.room_details['c3']}"),
        'entered': True,
        'completed': False,
        'north': 'b3',
        'south': False,
        'east': False,
        'west': False
    },
    'c4': {
        'room_name': 'Stone Corridor',
        'description': (f"{gametext.room_descriptions['c4']}"),
        'details': (f"{gametext.room_details['c4']}"),
        'entered': False,
        'completed': False,
        'north': 'b4',
        'south': 'd4',
        'east': False,
        'west': False
    },
    'd1': {
        'room_name': 'Final Room',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': 'c1',
        'south': False,
        'east': False,
        'west': False
    },
    'd2': {
        'room_name': 'Altar',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'd3',
        'west': False
    },
    'd3': {
        'room_name': 'Goblin Room',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': False,
        'south': False,
        'east': 'd4',
        'west': 'd2'
    },
    'd4': {
        'room_name': 'Riddle Room',
        'description': 'a spike pit',
        'details': 'you look around and see spikes',
        'entered': False,
        'completed': False,
        'north': 'c4',
        'south': False,
        'east': False,
        'west': 'd3'
    },
}

map_dict = {
    'a1': art.MAPA1,
    'a2': art.MAPA2,
    'a3': art.MAPA3,
    'a4': art.MAPA4,
    'b1': art.MAPB1,
    'b2': art.MAPB2,
    'b3': art.MAPB3,
    'b4': art.MAPB4,
    'c1': art.MAPC1,
    'c2': art.MAPC2,
    'c3': art.MAPC3,
    'c4': art.MAPC4,
    'd1': art.MAPD1,
    'd2': art.MAPD2,
    'd3': art.MAPD3,
    'd4': art.MAPD4,
}


def game_introduction():
    clear()
    type_effect("What is your name, victim ")
    time.sleep(0.35)
    type_effect('\b\b\b\b\b\b\b', 0.03)
    type_effect('brave adventurer? \n')
    name = input('> ')
    myPlayer.name = name
    clear()
    type_effect(f"Welcome, {myPlayer.name}, to Fell Manor\n")
    type_effect("Please, do make yourself at home. \n")
    type_effect("But you may wish to steer clear of the other guests. \n")
    type_effect("You might find them...")
    time.sleep(0.5)
    type_effect("\nless than hospitable \n", 0.05)
    type_effect("Heh heh heh heh \n", 0.18)
    game_instructions()


def update_player_location(destination):
    """
    Sets player location value to value of
    destination, passed as an argument.
    """
    clear()
    myPlayer.location = destination
    print_room_description()
    room_map[myPlayer.location]['entered'] = True


def print_room_description():
    if room_map[myPlayer.location]['entered']:
        print(
            f"You are back in the {room_map[myPlayer.location]['description']}"
            )
    else:
        type_effect(
            "You find yourself in"
            f" a {room_map[myPlayer.location]['description']}"
            )
        if myPlayer.location == 'b2':
            arena_details()


def print_room_details():
    if room_map[myPlayer.location]['completed']:
        type_effect("You have found all there is to find in this room", 0.03)

    elif myPlayer.location == 'b3':
        storage_room_details()

    elif myPlayer.location == 'a3':
        library_details()

    elif myPlayer.location == 'a4':
        dining_room_prompt()

    elif myPlayer.location == 'c3':
        prison_cell_details()

    elif myPlayer.location == 'c4':
        type_effect(room_map[myPlayer.location]['details'])
        lantern_prompt()

    elif myPlayer.location == 'a2':
        black_chasm_details()

    elif myPlayer.location == 'a1':
        study_details()

    elif myPlayer.location == 'b1':
        candlelit_corridor_details()

    elif myPlayer.location == 'c1':
        final_door_details()

    else:
        type_effect(room_map[myPlayer.location]['details'])


def storage_room_details():
    if room_map['b3']['looked'] is True:
        if myPlayer.lantern is False:
            type_effect(gametext.room_details_looked['b3'])
        else:
            type_effect(gametext.room_details_lantern['b3'])
            myPlayer.manormap = True
            room_map['b3']['completed'] = True

    else:
        if myPlayer.lantern is False:
            if myPlayer.weapon == 'No Weapon':
                myPlayer.weapon = 'Rusty Dagger'
                myPlayer.strength = 4
                type_effect(room_map['b3']['details'])
                room_map['b3']['looked'] = True
        else:
            type_effect(gametext.room_details_combined['b3'])
            if myPlayer.weapon == 'No Weapon':
                myPlayer.weapon = 'Rusty Dagger'
                myPlayer.strength = 4
            myPlayer.manormap = True
            room_map['b3']['completed'] = True
    

def prison_cell_details():
    if myPlayer.lantern is False:
        type_effect(room_map[myPlayer.location]['details'])
    else:
        if myPlayer.shield == 'No Shield':
            type_effect(gametext.room_details_lantern['c3'])
            myPlayer.shield = 'Wooden Shield'
            myPlayer.armour = 4
            (room_map[myPlayer.location]['completed']) = True
        else:
            type_effect(gametext.room_details_lesser_item['c3'])
            (room_map[myPlayer.location]['completed']) = True


def library_details():
    if myPlayer.eyeglass:
        type_effect(gametext.room_details_eyeglass['a3'])
    else:
        type_effect(gametext.room_details['a3'])


def black_chasm_details():
    if myPlayer.lantern:
        type_effect(gametext.room_details_lantern['a2'])
        room_map['a2']['west'] = 'a1'
        room_map['a2']['completed'] = True
    else:
        type_effect("\nDo you want to step forward into the blackness? (yes/no)")
        answer = input("> ")
        if answer.lower().strip() == 'yes':
            type_effect(gametext.room_details['a2'])
            player_death()
        else:
            main_prompt()


def study_details():
    type_effect(gametext.room_details['a1'])
    type_effect("\nDo you want to open the chest? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(gametext.enemy_text['haunted_chest'])
        combat(haunted_chest)
        room_map['a1']['completed'] = True
    else:
        type_effect("You step nervously back from the chest.")


def candlelit_corridor_details():
    type_effect(gametext.room_details['b1'])
    type_effect("\nDo you want to drink the liquid? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(gametext.item_text['health_potion'])
        update_player_health(5)
        room_map['b1']['completed'] = True
    else:
        type_effect(
            "You leave the vial where it is and slide the drawer shut"
            )


def arena_details():
    type_effect(
        f"\n\n'Welcome {myPlayer.name}.\n"
                 )
    type_effect(
        "You spin around to see a tall slender man in a red and gold cloak,"
        "smiling from ear to ear, his feet floating six inches of the ground."
        "\n At the same time, you see all manner of foul creatures scurrying"
        " around the upper levels of the arena, fighting for seats."
    )
    type_effect(
        "The cloked man turns and in a grandiose gesture you see"
        " two unnaturally long, grey-skinned arms emerge from his cloak"
        " into the air before he speaks again:"

        "\n\n'Can we please be upstanding for this evening's main event."
        f"The brave adventurer {myPlayer.name} will take on our undefeated"
        " champion, GOREHOWL!'\n\n"

        "With that, the cloaked man vanishes and you hear a terrifying"
        "guttural growl from the door on the opposite end of the room."
        "\n Suddenly, a huge beast charges forth from the door! You only"
        " get a brief second to take in its huge mass of fur and fangs"
        " before it is upon you!"
    )
    combat(gorehowl)


def alcove_details():
    type_effect(gametext.room_details['c2'])
    myPlayer.eyeglass = True
    room_map['c2']['completed'] = True


def final_door_details():
    if myPlayer.password:
        type_effect(gametext.room_details_password['c1'])
        room_map['c1']['south'] = 'd1'
        room_map['c1']['completed'] = True


def update_player_health(num):
    myPlayer.health = myPlayer.health + num
    if myPlayer.health <= 0:
        player_death()


def update_enemy_health(enemy, num):
    enemy.health = enemy.health + num
    if enemy.health <= 0:
        enemy_death(enemy)


def player_death():
    type_effect("\n\nYou Died....")
    time.sleep(4)
    main()


def gorehowl_death():
    type_effect("\n\nYou defeated Gorehowl!\n\n")
    type_effect(gametext.enemy_death['gorehowl'])
    room_map['b2']['completed'] = True


def enemy_death(enemy):
    type_effect(f"You defeated the {enemy.name}!\n")
    if myPlayer.location == 'a4':
        type_effect(gametext.enemy_death['ogre'])
        update_player_health(10)
        room_map['a4']['completed'] = True
    elif myPlayer.location == 'a1':
        type_effect(gametext.enemy_death['haunted_chest'])
        myPlayer.shield = 'Iron Shield'
        myPlayer.armour = 8
        room_map['a1']['completed'] = True
    elif myPlayer.location == 'b2':
        type_effect(gametext.enemy_death['gorehowl'])
        room_map['b2']['completed'] = True
        

def game_begin_message():
    type_effect(f"You awake in a {room_map[myPlayer.location]['description']}")


def calculate_valid_directions():
    directions_list = []
    for key, value in room_map[myPlayer.location].items():
        if key in ['north', 'south', 'east', 'west']:
            if value is not False:
                directions_list.append(key)
    type_effect(" you can travel: \n", 0.003)
    for direction in directions_list:
        type_effect(direction + '\n', 0.003)
    return directions_list


def main_prompt():
    print("\n")
    if myPlayer.manormap is False:
        type_effect(
            "\n----------------------------------------"
            "\nYou can 'look' around the room for more information,"
            "\ntype 'items' to view your items & health, \nor", 0.003
                 )
    else:
        type_effect(
            "\n----------------------------------------"
            "\nYou can 'look' around the room for more information,"
            "\ntype 'items' to view your items & health,"
            "\ntype 'map' to view the map,\nor", 0.003
                 )
    directions_list = calculate_valid_directions()
    print("\n")
    type_effect("What would you like to do?\n", 0.003)
    answer = input("> ")
    if answer.lower().strip() in directions_list:
        update_player_location(room_map[myPlayer.location][f"{answer}"])
    elif answer.lower().strip() == 'look':
        clear()
        print_room_details()
    elif answer.lower().strip() == 'items':
        inventory_screen()
    elif answer.lower().strip() == 'map':
        if myPlayer.manormap:
            display_map()

    main_prompt()


def lantern_prompt():
    type_effect("\nDo you want to try to grab the lantern? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        lantern_attempt()
    else:
        main_prompt()
        

def lantern_attempt():
    rng = random.randint(1, 3)
    if rng <= 2:
        type_effect(gametext.item_text['lantern_success'])
        myPlayer.lantern = True
        room_map['c4']['completed'] = True
    else:
        type_effect(gametext.item_text['lantern_failure'])
        update_player_health(1)
        type_effect("\nDo you want to try again? (yes/no)")
        answer = input("> ")
        if answer.lower().strip() == 'yes':
            lantern_attempt()
        else:
            main_prompt()


def dining_room_prompt():
    type_effect(f"{gametext.room_details['a4']}")
    type_effect("\nDo you take a bite? (yes/no)\n")
    answer = input("> ")
    if answer.lower().strip() == 'yes':
        type_effect(
            "You take a bite of the bread, it is astonishingly tasty,"
            " fluffy and warm, yet delightfully crunchy."
            "\n\n **Your health increases by 2 points**\n\n"
            )
        update_player_health(2)
        type_effect(gametext.enemy_text['ogre'])
        combat(ogre)


def game_instructions():
    clear()
    type_effect("You must escape from Fell Manor! \n", 0.01)
    type_effect("To move from room to room, type 'north', 'south',\n", 0.01)
    type_effect("'east' or 'west' when prompted.", 0.01)
    print('\n')
    type_effect("You can also type 'look' to examine", 0.01)
    type_effect(" the room you are in for more information \n", 0.01)
    print("\n")
    type_effect("Many challenges await you,\n", 0.01)
    type_effect("Good Luck!\n", 0.01)
    print("\n \n")
    input("-- press ENTER to begin --")
    clear()
    game_begin_message()
    main_prompt()


def combat(enemy):
    clear()
    type_effect(f"\nThe {enemy.name} attacks!")
    enemy_attack_strength = random.randint(0, 4) + enemy.strength - myPlayer.armour
    if enemy_attack_strength < 0:
        enemy_attack_strength = 0
    type_effect(f"\nThe {enemy.name} hits you for {enemy_attack_strength} damage!")
    print(f"\nYour health was at {myPlayer.health}")
    print(
        f"\nafter that attack, it's now at {myPlayer.health - enemy_attack_strength}"
        )
    update_player_health(enemy_attack_strength * -1)

    input("\n\nPress ENTER to attack!")
    clear()
    if myPlayer.weapon == 'No Weapon':
        type_effect(f"\nYou attack the {enemy.name} with your bare fists!")
    else:
        type_effect(f"\nYou attack the {enemy.name} with your {myPlayer.weapon}!")
    attack_strength = random.randint(0, 4) + myPlayer.strength - enemy.armour
    if attack_strength < 0:
        attack_strength = 0
    print(f"\nYou hit the {enemy.name} for {attack_strength} damage!")
    print(f"\nThe {enemy.name}'s health was at {enemy.health}")
    print(f"\nAfter that attack, it's now at {enemy.health - attack_strength}")
    update_enemy_health(enemy, attack_strength * -1)
   
    if enemy.health <= 0:
        return
    else:
        input("\nPress ENTER to continue!")
        combat(enemy)


def main():
    display_title_screen()

main()
