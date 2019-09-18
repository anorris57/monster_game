""" player_name = 'Diamond'
player_attack = 10
player_heal = 16
health = 100 """

#create variable to contain all information
#use a list
""" player = ['Diamond', 10, 16, 100]
player2 = ['Ruby', 10, 16, 100] """

#create dictionary use key value pairs
player ={
  'name': 'Diamond',
  'attack': 10,
  'heal': 16,
  'health': 100
}
monster ={
  'name': 'Iron',
  'attack': 12,
  'health': 100
}
#booleans easily help control while loops
game_running = True


while game_running == True:
  # use print statement to create user interface using input method
  print('Please select action: ')
  print('1) Attack')
  print('2) Heal')
  player_choice = input()

  if player_choice == '1':
      monster['health'] = monster['health'] - player['attack']
      player['health'] = player['health'] - monster['attack']
      pattack_result = "New monster health is {}"
      mattack_result = "New player health is {}"
      print(pattack_result.format(monster['health']))
      print(mattack_result.format(player['health']))

  elif player_choice == '2':
    print('Heal player')
  else:
    print('Invalid selection')

  if player['health'] <= 0:
    game_running = False