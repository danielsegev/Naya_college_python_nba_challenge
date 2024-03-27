# Generate a random player
def select_random_player():
  player = nba_data.sample()
  player_name = player['player_name'].values[0]
  return player_name

def clues_generator(number, player):
    clue_number = "clue_" + str(number)

    # Call the function dynamically
    if hasattr(sys.modules[__name__], clue_number):
      return getattr(sys.modules[__name__], clue_number)(player)
    else:
      return f"Clue {number} does not exist."


# Play trivia
def play_game():
    print("Welcome to the NBA Stat Trivia Challenge!")
    print("You have up to 5 attempts to guess the player.")
    print("Type 'clue' to reveal more clues.")
    print("Type 'stats' to display the player's career statistics.")
    print("Type 'quit' at any time to exit the game.")
    print("Good luck!")
    
    # Number of clues in the bank
    number_of_questions = 8

    # Select a random player
    player = select_random_player()

    # Define the URL of the image (work only on Google Colab env)
    player_data = nba_data[nba_data['player_name'] == player]
    url = player_data['image'].min()

    # Open the URL and download the image data (work only on Google Colab env)
    #image_data = urllib.request.urlopen(url).read()

    # Create an Image object from the downloaded data (work only on Google Colab env)
    # image = Image.open(io.BytesIO(image_data))

    # Display the clues to the player
    random_number = random.randint(1, number_of_questions)
    first_clue = clues_generator(random_number, player)
    print(f"Here is you first clue: {first_clue}")

    # Number of attempts allowed
    attempts_left = 5

    # Keep track of used clues
    used_clues = [random_number]

    while attempts_left > 0:
        guess = input("\nEnter your guess: ").strip().title()

        if guess.lower() == 'quit':
            print("Thanks for playing!")
            return

        if guess == player:
            print("Congratulations! You guessed correctly.")
            # Display the image in the notebook
            #resize_percentage = 50  # 50% of the original size
            #image.thumbnail((image.width * resize_percentage // 100, image.height * resize_percentage // 100))
            #display(image)

            # Return to main function
            time.sleep(2)
            choose_next()

            return

        if guess.lower() == 'stats':
          print(players_stats(player))
          continue

        # Check if the user wants to reveal one more clue
        if guess.lower() == 'clue':
          if len(used_clues) < number_of_questions:
            while True:
              new_clue = random.randint(1, number_of_questions)
              if new_clue not in used_clues:
                additional_clue = clues_generator(new_clue, player)
                print(f"Here's an additional clue: {additional_clue}")
                used_clues.append(new_clue)
                break
            continue
          else:
            print("Sorry, you're out of clues.")
            print(f"You have {attempts_left} attempts left.")
            continue
        print("Sorry, that's incorrect.")
        attempts_left -= 1
        print(f"You have {attempts_left} attempts left.")

    print(f"\nYou've used all your attempts. The correct answer is: {player}")

    # Display the image in the notebook (work only on Google Colab env)
    #resize_percentage = 50  # 50% of the original size
    #image.thumbnail((image.width * resize_percentage // 100, image.height * resize_percentage // 100))
    #display(image)

    # Return to main function
    time.sleep(2)
    choose_next()
    return