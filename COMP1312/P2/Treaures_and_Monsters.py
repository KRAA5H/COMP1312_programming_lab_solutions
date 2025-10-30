from random import randint 
room_items = ["bow", "armour", "boomerang", "shield", "sword"]

# Complete the definition of treasure_room()
def treasure_room():
    print("You have found the ultimate treasure chest! You win the game!")

def item_room():
    print(f"You found {room_items[randint(0, len(room_items)-1)]}, you decide to pick it up!")
    return 

def monster_room():
    print("You have entered a room with a monster!")
    choice = input("Do you choose to fight or flee?")
    valid_input = False
    while not valid_input:
        if choice == "fight":
            return fight_monster()
        elif choice == "flee":
            print("You fled back to the starting room.")
            return True
        else:
            print("Invalid choice. Please choose to fight or flee.")
            choice = input("Do you choose to fight or flee?")

def fight_monster():
    print("You are fighting the monster...")
    chance = randint(1, 9)
    if chance > 3:
        print("You defeated the monster! You win!")
        return True
    else:
        print("The monster defeated you. You lose the game.")
        return False

def stating_room():
    no_of_doors = 3
    treasure_room_door_no = randint(1,  no_of_doors)
    print(f"You are in a room with 3 doors.")
    while True:
        door_choice = int(input(f"Which door (1 - 3) do you choose? "))
        if door_choice == treasure_room_door_no:
            treasure_room()
            break
        else:
            if randint(0,1) == 0:
                item_room()
            else:
                if not monster_room():
                    break


# stating_room()