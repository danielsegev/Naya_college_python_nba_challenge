# Start game
def choose_first():
    
  # Import data
  import_data()
  
  # Start game
  while True:
    print("Welcome to the NBA trivia/stats generator!")
    print("Please choose one of the following:")
    print('1 - Play trivia')
    print('2 - Show stats')
    game = input("\nChoose one option: ").strip().title()

    if game == '2':
      print(general_stats())
      choose_next()
      return

    elif game == '1':
      play_game()
      return

    else:
      print('I am sorry, I did not get your answer. Please try again.')
      continue

# Continue game
def choose_next():
  while True:
    print("Please choose one of the following:")
    print('1 - Play trivia')
    print('2 - Show stats')
    print('3 - Quit')
    print("Choose one option:\n")
    game = input()
    if game == '2':
      print(general_stats())
      choose_next()
      return
    elif game == '1':
      play_game()
      return
    elif game == '3':
      print("Thanks for playing!")
      return
    else:
      print('I am sorry, I did not get your answer. Please try again.')