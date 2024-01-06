import random


class Room:
    def __init__(self, name):
        self.name = name
        self.doors = []
        self.content = {'key': round(random.random())}

    def add_door(self, door):
        self.doors.append(door)

    def view_doors(self):
        door_names = [door.get_other_room(self).name for door in self.doors]
        return door_names


class Door:
    def __init__(self, room1, room2, is_closed=False):
        self.room1 = room1
        self.room2 = room2
        self.is_closed = is_closed

    def get_other_room(self, location):
        if location == self.room1:
            return self.room2
        elif location == self.room2:
            return self.room1


class Player:
    def __init__(self, name, rooms):
        self.name = name
        self.location = random.choice(rooms)
        self.hp = len(rooms)
        self.inventory = {'keys': 0}

    def look_around(self):
        doors = self.location.view_doors()
        print(f"You are in {self.location.name}.")
        if any(self.location.content.values()):
            print('There is in the room: ')
            for i in self.location.content:
                if i:
                    print(f'{i} - {self.location.content[i]}')
        if self.location.content['key']:
            self.inventory['keys'] += 1
            self.location.content['key'] -= 1
            print('You got a key!')
        print("You see doors leading to the following rooms:")
        for ind, door in enumerate(doors):
            print(ind, door)


    def enter_room(self, door_index):
        doors = self.location.doors
        if 0 <= door_index < len(doors):
            if doors[door_index].is_closed:
                print('Door is closed!')
                if self.inventory['keys']:
                    print(f'You have {self.inventory['keys']} keys! Use the key to open the door?\n0. No\n1. Yes')
                    choice = input()
                    if choice in ('0', '1'):
                        if choice == '1':
                            doors[door_index].is_closed = False
                            self.inventory['keys'] -= 1
                        else:
                            print('Choose other room!')
                            return
                else:
                    print("You don't have any keys")
                    print('Choose other room!')
                    return
            next_room = doors[door_index].get_other_room(self.location)
            self.location = next_room
            print(f"You entered {self.location.name}.")
            self.hp -= 1
            if self.location == winning_room:
                print("Congratulations! You've reached the winning room!")
        else:
            print("Invalid door index.")


room1 = Room("Room 1")
room2 = Room("Room 2")
room3 = Room("Room 3")
room4 = Room("Room 4")
room5 = Room("Room 5")
room6 = Room("Room 6")
rooms = [room1, room2, room3, room4, room5, room6]
winning_room = room5

door1 = Door(room1, room2)
door2 = Door(room2, room3, True)
door3 = Door(room1, room3)
door4 = Door(room3, room4, True)
door5 = Door(room2, room4)
door6 = Door(room4, room5, True)
door7 = Door(room2, room6, True)

room1.add_door(door1)
room1.add_door(door3)
room2.add_door(door1)
room2.add_door(door2)
room2.add_door(door5)
room2.add_door(door7)
room3.add_door(door2)
room3.add_door(door3)
room3.add_door(door4)
room4.add_door(door4)
room4.add_door(door5)
room4.add_door(door6)

player = Player("Player", rooms)

while True:
    if player.location == winning_room:
        break
    elif not player.location.doors:
        print("It's a dead end! Game over!")
        break
    elif all(door.is_closed for door in player.location.doors) and not player.inventory['keys']:
        print("Game over! All doors are closed and you don't have any keys")
    player.look_around()
    door_index = int(input("Choose a door to enter (enter the door index): "))
    player.enter_room(door_index)
    if player.hp == 0:
        print('You are dead! Game over!')
        break
