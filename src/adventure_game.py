# establish the direction in which the user can move
# establish a way to track how far the user has moved (and therefore which room he/she is in)
# print out a description
# set limits for how far the user can move
# Create “walls” around the rooms that tell the user, “You can’t move further in this direction

def adventure_game():

    print(

        """
        Welcome to my house! You can stop any time by typing 'stop'.

        Here is the floor plan of the house: 

         -------------------------------------------
        |   Kitchen   |   Bedroom    |   Office     |
         -------------------------------------------
        |   Toilet    |   Storage    |  Guest Room  |
         -------------------------------------------
        """
    )

    Kitchen = "kitchen, where the spice of life comes alive"
    Bedroom = "bedroom, where the magic happens"
    Office = "office, the source of wealth"
    Toilet = "toilet you know what happens here"
    Storage = "storage, where there are all sorts of stuff"
    Guest_Room = "guest room, where you have friends"

    # list of rooms
    room = [[Kitchen, Bedroom, Office],[Toilet, Storage, Guest_Room]]
    
    # start in the first row
    current_row_index = 0
    # start in the first room (kitchen)
    current_room_index = 0
    # walk counter
    walk_count = 0

    while True:
        current_room = room[current_row_index][current_room_index]
        # let users move through rooms based on user input and get descriptions of each room.
        direction = input(f"You are in {current_room}.\nWhich direction would you like to move to?\nPlease enter left/right/up/down/stop: ").lower()

        if direction == "left":
            if current_room_index == 0:
                print("\nYou cannot go left, try the other direction.")
            else:
                current_room_index -= 1
                walk_count += 1
                print(f"\nYou moved left to the {room[current_row_index][current_room_index]}.")

        elif direction == "right":
            if current_room_index == len(room[current_row_index]) -1:
                print("\nYou cannot go right, try the other direction.")
            else:
                current_room_index += 1
                walk_count += 1
                print(f"\nYou moved right to the {room[current_row_index][current_room_index]}.")

        elif direction == "up":
            if current_row_index == 0:
                print("\nYou cannot go up, try the other direction.")
            else:
                current_row_index -= 1
                walk_count += 1
                print(f"\nYou moved up to the {room[current_row_index][current_room_index]}.")

        elif direction == "down":
            if current_row_index == len(room) -1:
                print("\nYou cannot go down, try the other direction.")
            else:
                current_row_index += 1
                walk_count += 1
                print(f"\nYou moved down to the {room[current_row_index][current_room_index]}.")
        
        elif direction == "stop":
            print(f"\nYou are in the {room[current_row_index][current_room_index]}. Thank you for your visit!")
            break

        else:
            print("\nInvalid Input. Please enter left or right or stop.")
            continue

        print(f"\nTotal walks taken: {walk_count}\n")

adventure_game()











