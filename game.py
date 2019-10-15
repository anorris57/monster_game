""" player_name = 'Diamond'
player_attack = 10
player_heal = 16
health = 100 """

#create variable to contain all information
#use a list
""" player = ['Diamond', 10, 16, 100]
player2 = ['Ruby', 10, 16, 100] """

import random
#booleans easily help control while loops
game_running = True
game_results = []

def calculate_monster_attack(attack_min, attack_max):
  return random.randint(attack_min,attack_max)

def game_ends(winner_name):
  print(f'{winner_name} won the game!')
  """ player_won_result = "{} won!"
    print(player_won_result.format(winner_name)) """


while game_running == True:
  counter = 0
  new_round = True
  #create dictionary use key value pairs
  player ={
  'name': 'Diamond',
  'attack': 13,
  'heal': 16,
  'health': 100
  }
  monster = {
  'name': 'Iron',
  'attack_min': 10,
  'attack_max': 20,
  'health': 100
  }

  print('---'*7)
  print('Enter Player name')
  player['name']= input()

  print('---'*7)
  playerInfo = "{} has {} health."
  print(playerInfo.format(player['name'], player['health']))
  print(playerInfo.format(monster['name'], monster['health']))

  while new_round == True:

    counter = counter + 1
    player_won = False
    monster_won = False

    print('---'*7)
    # use print statement to create user interface using input method
    print('Please select action: ')
    print('1) Attack')
    print('2) Heal')
    print('3) Exit Game')
    print('4) Show Results')
    player_choice = input()

    if player_choice == '1':
        monster['health'] = monster['health'] - player['attack']
        if monster['health'] <= 0:
          player_won = True
        else:
       #   monster_attack = random.randint(10,20)
          player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
          if player['health'] <= 0:
            monster_won = True

    elif player_choice == '2':
    #  monster_attack = random.randint(10,20)
    #  player_heal = random.randint(9, 19)
      player['health'] = player['health'] + player['heal']

      player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
      if player['health'] <= 0:
        monster_won = True


    elif player_choice == '3':
      new_round = False
      game_running = False
    
    elif player_choice =='4':
      for list_item in game_results:
        print(list_item)

    else:
      print('Invalid selection')

    if player_won == False and monster_won == False:
        player_result = "{} remaining health is {}"
        monster_result = "{} remaining health is {}"
        print(player_result.format(player['name'], player['health']))
        print(monster_result.format(monster['name'], monster['health']))
        
    elif player_won:
        game_ends(player['name'])
        round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
        game_results.append(round_result)
        new_round = False

    elif monster_won:
        game_ends(monster['name'])
        round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
        game_results.append(round_result)
        new_round = False
        
"""     elif player_won:
        player_won_result = "{} won!"
        print(player_won_result.format(player['name']))
        new_round = False

    elif monster_won:
        print('The Monster won')
        new_round = False """
