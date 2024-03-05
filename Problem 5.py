class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_model(self):
        return self.nickname

    def get_year(self):
        return self.weapons

    def get_color(self):
        return self. weaknesses

    def profile(self):
        return self.nickname, self.weapons, self. weaknesses

player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries',]
player1.weaknesses = ['slow']

for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

def check_tasks(character_items, character_debuffs):
    # Define the requirements for each task
    tasks = {
        'Climb a mountain': {
            'needed_items': ['rope', 'coat', 'first aid kit'],
            'forbidden_debuffs': ['slow']
        },
        'Cook a meal': {
            'needed_items': ['pan', 'groceries'],
            'forbidden_debuffs': ['small']
        },
        'Write a book': {
            'needed_items': ['pen', 'paper', 'idea'],
            'forbidden_debuffs': ['confusion']
        }
    }
    for task, requirements in tasks.items():
        items_check = all(item in character_items for item in requirements['needed_items'])
        debuffs_check = not any(debuff in character_debuffs for debuff in requirements['forbidden_debuffs'])