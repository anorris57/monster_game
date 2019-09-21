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

  while new_round == True:

    player_won = False
    monster_won = False

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

        pattack_result = "New monster health is {}"
        mattack_result = "New player health is {}"
        print(pattack_result.format(monster['health']))
        print(mattack_result.format(player['health']))

    elif player_choice == '2':
      print('Heal player')

    elif player_choice == '3':
      new_round = False
      game_running = False

    else:
      print('Invalid selection')

    if player_won == True or monster_won == True:
      new_round = False