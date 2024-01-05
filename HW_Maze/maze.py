

class Room:
    def __init__(self, name):
        self.name = name
        self.doors = []

    def add_door(self, door):
        self.doors.append(door)

    def view_doors(self):
        door_names = [door.get_other_room(self).name for door in self.doors]
        return door_names


class Door:
    def __init__(self, room1, room2):
        self.room1 = room1
        self.room2 = room2

    def get_other_room(self, location):
        if location == self.room1:
            return self.room2
        elif location == self.room2:
            return self.room1


class Player:
    def __init__(self, name, start_location):
        self.name = name
        self.location = start_location

    def look_around(self):
        doors = self.location.view_doors()
        print(f"You are in {self.location.name}.")
        print("You see doors leading to the following rooms:")
        for ind, door in enumerate(doors):
            print(ind, door)

    def enter_room(self, door_index):
        doors = self.location.doors
        if 0 <= door_index < len(doors):
            next_room = doors[door_index].get_other_room(self.location)
            self.location = next_room
            print(f"You entered {self.location.name}.")
            if self.location == winning_room:
                print("Congratulations! You've reached the winning room!")
                return True
        else:
            print("Invalid door index.")


room1 = Room("Room 1")
room2 = Room("Room 2")
room3 = Room("Room 3")
room4 = Room("Room 4")
room5 = Room("Room 5")
winning_room = room5

door1 = Door(room1, room2)
door2 = Door(room2, room3)
door3 = Door(room1, room3)
door4 = Door(room3, room4)
door5 = Door(room2, room4)
door6 = Door(room4, room5)

room1.add_door(door1)
room1.add_door(door3)
room2.add_door(door1)
room2.add_door(door2)
room2.add_door(door5)
room3.add_door(door2)
room3.add_door(door3)
room3.add_door(door4)
room4.add_door(door4)
room4.add_door(door5)
room4.add_door(door6)

player = Player("Player", room1)

while True:
    player.look_around()
    door_index = int(input("Choose a door to enter (enter the door index): "))
    move = player.enter_room(door_index)
    if move:
        break

