""" player_name = 'Diamond'
player_attack = 10
player_heal = 16
health = 100 """

#create variable to contain all information
#use a list
""" player = ['Diamond', 10, 16, 100]
player2 = ['Ruby', 10, 16, 100] """


#booleans easily help control while loops
game_running = True


while game_running == True:
  new_round = True
  #create dictionary use key value pairs
  player ={
  'name': 'Diamond',
  'attack': 13,
  'heal': 16,
  'health': 100
  }
  monster ={
  'name': 'Iron',
  'attack': 12,
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

    player_won = False
    monster_won = False

    print('---'*7)
    # use print statement to create user interface using input method
    print('Please select action: ')
    print('1) Attack')
    print('2) Heal')
    print('3) Exit Game')
    player_choice = input()

    if player_choice == '1':
        monster['health'] = monster['health'] - player['attack']
        if monster['health'] <= 0:
          player_won = True
        else:
          player['health'] = player['health'] - monster['attack']
          if player['health'] <= 0:
            monster_won = True

    elif player_choice == '2':
      player['health'] = player['health'] + player['heal']

      player['health'] = player['health'] - monster['attack']
      if player['health'] <= 0:
        monster_won = True


    elif player_choice == '3':
      new_round = False
      game_running = False

    else:
      print('Invalid selection')

    if player_won == False and monster_won == False:
        player_result = "{} remaining health is {}"
        monster_result = "{} remaining health is {}"
        print(player_result.format(player['name'], player['health']))
        print(monster_result.format(monster['name'], monster['health']))
        
    elif player_won:
        player_won_result = "{} won!"
        print(player_won_result.format(player['name']))
        new_round = False

    elif monster_won:
        print('The Monster won')
        new_round = False
