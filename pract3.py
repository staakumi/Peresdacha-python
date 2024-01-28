
import random
def save_to_json(player, location, visited_locations):
    save_data = {
        "player": player.__dict__,
        "location": location,
        "visited_locations": list(visited_locations)
    }
    with open("game_state.json", "w") as file:
        json.dump(save_data, file)

def save_to_csv(player, location):
    with open('game_data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([player.name, player.health, player.power, location])

if __name__ == "__main__":
    player, location, visited_locations = load_game_state()
    if player is None:
        player = Character("Player", 100, 20)
        location = "forest"
        visited_locations = set()


def introduction():
    print("Welcome to the text adventure game!")
    name = input("Enter your name: ")
    print(f"Hello, {name}! Let's start the adventure.")

def choose_path():
    print("You find yourself in a dark forest.")
    choice = input("Do you want to go left or right? ").lower()
    if choice == "left":
        print("You encounter a friendly squirrel.")
    elif choice == "right":
        print("You stumble upon a mysterious cave.")
    else:
        print("Invalid choice. Please try again.")
        choose_path()

def explore_cave():
    print("You enter the cave and find a treasure chest.")
    decision = input("Open the chest? (yes/no) ").lower()
    if decision == "yes":
        print("Congratulations! You found the hidden treasure.")
    elif decision == "no":
        print("You leave the cave empty-handed.")
    else:
        print("Invalid decision. Please try again.")
        explore_cave()

def main():
    introduction()
    choose_path()
    explore_cave()

if __name__ == "__main__":
    main()
    locations = ['forest', 'cave', 'castle', 'village']
objects = {'forest': ['tree', 'bush', 'squirrel'], 'cave': ['treasure chest', 'bats', 'rocks'], 
           'castle': ['throne', 'armor', 'sword'], 'village': ['inn', 'blacksmith', 'market']}
visited_locations = set()

def visit_location(location):
    if location in locations:
        if location not in visited_locations:
            print(f"You are now in the {location}. You see: {', '.join(objects[location])}")
            visited_locations.add(location)
        else:
            print(f"You have already visited the {location}.")
    else:
        print("Invalid location.")

def main_game():
    for loc in locations:
        visit_location(loc)

if __name__ == "__main__":
    main_game()
    
    def __init__(self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

    def attack(self, enemy):
        print(f"{self.name} attacks {enemy.name}")
        enemy.health -= self.power

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Power: {self.power})"


def battle():
    player = Character("Player", 100, 20)
    enemy = Character("Goblin", 80, 15)
    print(f"A wild {enemy.name} appears!")
    while player.health > 0 and enemy.health > 0:
        print(player)
        print(enemy)
        print()
        input("Press Enter to attack!")
        player.attack(enemy)
        if enemy.health <= 0:
            print(f"The {enemy.name} is defeated! You win!")
            break
        enemy.attack(player)
        if player.health <= 0:
            print("You have been defeated. Game over.")
            break


if __name__ == "__main__":
    battle()
    dialogues = {
    "squirrel": "Hello traveler, what brings you to the forest?",
    "villager": "Welcome to our village! Feel free to explore and rest at the inn.",
    "blacksmith": "I can forge powerful weapons for you, traveler. Take a look at my wares."
}

def talk_to_npc(npc):
    if npc in dialogues:
        print(dialogues[npc])
    else:
        print("This NPC does not have anything to say.")

def main_interaction():
    talk_to_npc("squirrel")
    talk_to_npc("villager")
    talk_to_npc("blacksmith")

if __name__ == "__main__":
    main_interaction()
    print("Congratulations for playing!")
    
    

if __name__ == "__main__":
    ending()
    
    if game_completed:
        save_to_json(player, location, visited_locations)
        save_to_csv(player, location)
    