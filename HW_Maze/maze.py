import random


class Room:
    def __init__(self, room_id, name):
        self.room_id = room_id
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
        self.location = random.choice(list(rooms))
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


def create_labyrinth(labyrinth_data):
    rooms = {}

    # Create rooms
    for room_data in labyrinth_data:
        room_id = room_data["id"]
        room_name = room_data["name"]
        room = Room(room_id, room_name)
        rooms[room_id] = room

    doors = []
    # Create doors
    for room_data in labyrinth_data:
        room_id = room_data["id"]
        room = rooms[room_id]
        door_ids = room_data["doors"]
        for door_id in door_ids:
            other_room = rooms[door_id]

            # Check if the door is already created in the opposite direction
            opposite_door = None
            for other_door in other_room.doors:
                if other_door.room2 == room:
                    opposite_door = other_door
                    break

            # If the opposite door exists, use it instead of creating a new one
            if opposite_door:
                room.add_door(opposite_door)
            else:
                door = Door(room, other_room)
                doors.append(door)
                room.add_door(door)

    for i in random.sample(doors, 3):
        i.is_closed = True

    return rooms


# Example labyrinth data
LEVEL1 = [
    {
        "id": "room-1",
        "name": "Room 1",
        "doors": ["room-2", "room-3"]
    },
    {
        "id": "room-2",
        "name": "Room 2",
        "doors": ["room-1", "room-3", "room-4", "room-6"]
    },
    {
        "id": "room-3",
        "name": "Room 3",
        "doors": ["room-1", "room-2", "room-4"]
    },
    {
        "id": "room-4",
        "name": "Room 4",
        "doors": ["room-2", "room-3", "room-5"]
    },
    {
        "id": "room-5",
        "name": "Room 5",
        "doors": []
    },
    {
        "id": "room-6",
        "name": "Room 6",
        "doors": []
    }
]

labyrinth = create_labyrinth(LEVEL1)
rooms = labyrinth.values()
winning_room = labyrinth['room-5']

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
