import pandas as pd
import urllib.request
from PIL import Image
import io
from IPython.display import display
import random
import os
import sys
import time
import requests

# Generate Google Drive Link
def csv_drive_path_generator(url):
    path = 'https://drive.google.com/uc?export=download&id=' + url.split('/')[-2]
    return path


# Import data from Google Drive
def import_data():
    link = "https://drive.google.com/file/d/1-6zrHHfF2a9jfXqgPFlP93CngzAxfkZ8/view?usp=sharing"
    path_response = requests.get(csv_drive_path_generator(link))
    nba_data = pd.read_csv(io.StringIO(path_response.content.decode('utf-8')))
    return nba_data


# Clue 1 - player's birthdate, city and state
def clue_1(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  birthdate = player_data['born'].min()
  birth_city = player_data['birth_city'].min()
  birth_state = player_data['birth_state'].min()
  return (f'He was born at {birthdate} in {birth_city}, {birth_state}.')


# Clue 2 - player's first and last years played
def clue_2(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  first_year = player_data['year'].min()
  last_year = player_data['year'].max()
  return (f"He played from {first_year} to {last_year}")


# Clue 3 - player's teams played
def clue_3(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  first_team = player_data.sort_values(by='year')['team'].iloc[0]
  last_team = player_data.sort_values(by='year', ascending=False)['team'].iloc[0]
  if first_team == last_team:
    return (f'He played all of his career in {first_team}.')
  else:
    return (f'First team: {first_team}. Last team: {last_team}.')


# Clue 4 - player's height and weight
def clue_4(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  height = player_data['height'].min()
  weight = player_data['weight'].min()
  return (f'He weighs {weight} kg, and is {height} cm tall.')


# Clue 5 - achievements
def clue_5(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  championships = player_data['championships'].min()
  mvps = player_data['mvps'].min()
  allstar_selections = player_data['allstar_selections'].min()
  all_nba = player_data['all_nba'].min()
  return (f'He won {championships} championsips, {mvps} MVPs, was selected {allstar_selections} times to the allstar game, and was All-NBA {all_nba} times during his career.')


# Clue 6 - player's position
def clue_6(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  position = player_data['position'].max()
  return (f'He played in the {position} position.')


# Clue 7 - player's total and avg points
def clue_7(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  total_points = player_data['pts'].sum()
  total_games = player_data['g'].sum()
  average_points = round(total_points / total_games, 2)
  return print(f'He scored a total of {total_points} points during his career.\nAveraged {average_points} points per game.')


# Clue 8 - player's college
def clue_8(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  college = player_data['collage'].min()
  return (f"The player played for {college} in college.")


# player's general statistics
def players_stats(player_name):
  player_data = nba_data[nba_data['player_name'] == player_name]
  grouped_data = player_data.groupby(['year', 'team']).agg({'pts': 'sum', 'rtb': 'sum', 'ast': 'sum', 'g': 'sum'}).reset_index()
  grouped_data = grouped_data.rename(columns={'year': 'Year', 'team': 'Team', 'pts': 'Total Points', 'rtb': 'Total Rebounds', 'ast': 'Total Assists', 'g': 'GP'})
  grouped_data['PPG'] = round(grouped_data['Total Points'] / grouped_data['GP'],1)
  grouped_data['RPG'] = round(grouped_data['Total Rebounds'] / grouped_data['GP'],1)
  grouped_data['APG'] = round(grouped_data['Total Assists'] / grouped_data['GP'],1)
  grouped_data = grouped_data.drop(columns=['Total Points', 'Total Rebounds', 'Total Assists'])
  return grouped_data


# Show statistics
def general_stats():
  nba_data = import_data()
  print('1 - By Year')
  print('2 - All Time')
  time_span = input('Please choose one of the following: ').strip().title()
  if time_span == '2':
      while True:
        print("Please choose your main metric:")
        print("1 - Points")
        print("2 - Rebounds")
        print("3 - Assists")
        measure = input('Please type your choice: ').strip().title()
        if measure == '1':
          grouped_data = nba_data.groupby(['player_name']).agg({'pts': 'sum', 'g': 'sum'}).reset_index()
          grouped_data = grouped_data.rename(columns={'player_name': 'Player Name', 'pts': 'Total Points', 'g': 'Games Played'})
          grouped_data['Points per Game'] = round(grouped_data['Total Points'] / grouped_data['Games Played'],1)
          grouped_data = grouped_data.sort_values(by='Points per Game', ascending=False)
          grouped_data = grouped_data.head(10)
          #print(grouped_data)
          return grouped_data
        elif measure == '2':
          grouped_data = nba_data.groupby(['player_name']).agg({'rtb': 'sum', 'g': 'sum'}).reset_index()
          grouped_data = grouped_data.rename(columns={'player_name': 'Player Name', 'rtb': 'Total Rebounds', 'g': 'Games Played'})
          grouped_data['Rebounds per Game'] = round(grouped_data['Total Rebounds'] / grouped_data['Games Played'],1)
          grouped_data = grouped_data.sort_values(by='Rebounds per Game', ascending=False)
          grouped_data = grouped_data.head(10)
          #print(grouped_data)
          return grouped_data
        elif measure == '3':
          grouped_data = nba_data.groupby(['player_name']).agg({'ast': 'sum', 'g': 'sum'}).reset_index()
          grouped_data = grouped_data.rename(columns={'player_name': 'Player Name', 'ast': 'Total Assists', 'g': 'Games Played'})
          grouped_data['Assists per Game'] = round(grouped_data['Total Assists'] / grouped_data['Games Played'],1)
          grouped_data = grouped_data.sort_values(by='Assists per Game', ascending=False)
          grouped_data = grouped_data.head(10)
          #print(grouped_data)
          return grouped_data
        else:
          print("I am sorry, I did not get that. Let's try again.")
          continue
  elif time_span == '1':
    year = input('Please choose a year from 1985 to 2017: ').strip().title()
    while True:
      if int(year) >= 1985 and int(year) <= 2017:
        while True:
          print("Please choose your main metric:")
          print("1 - Points")
          print("2 - Rebounds")
          print("3 - Assists")
          measure = input('Please type your choice: ').strip().title()
          if measure == '1':
            grouped_data = nba_data[nba_data['year'] == int(year)].groupby(['player_name', 'year']).agg({'pts': 'sum', 'g': 'sum'}).reset_index()
            grouped_data = grouped_data.rename(columns={'player_name': 'Player Name', 'pts': 'Total Points', 'g': 'Games Played'})
            grouped_data['Points per Game'] = round(grouped_data['Total Points'] / grouped_data['Games Played'],1)
            grouped_data = grouped_data.sort_values(by='Points per Game', ascending=False)
            grouped_data = grouped_data.head(10)
            #print(grouped_data)
            return grouped_data
          elif measure == '2':
            grouped_data = nba_data[nba_data['year'] == int(year)].groupby(['player_name', 'year']).agg({'rtb': 'sum', 'g': 'sum'}).reset_index()
            grouped_data = grouped_data.rename(columns={'player_name': 'Player Name', 'rtb': 'Total Rebounds', 'g': 'Games Played'})
            grouped_data['Rebounds per Game'] = round(grouped_data['Total Rebounds'] / grouped_data['Games Played'],1)
            grouped_data = grouped_data.sort_values(by='Rebounds per Game', ascending=False)
            grouped_data = grouped_data.head(10)
            #print(grouped_data)
            return grouped_data
          elif measure == '3':
            grouped_data = nba_data[nba_data['year'] == int(year)].groupby(['player_name', 'year']).agg({'ast': 'sum', 'g': 'sum'}).reset_index()
            grouped_data = grouped_data.rename(columns={'player_name': 'Player Name', 'ast': 'Total Assists', 'g': 'Games Played'})
            grouped_data['Assists per Game'] = round(grouped_data['Total Assists'] / grouped_data['Games Played'],1)
            grouped_data = grouped_data.sort_values(by='Assists per Game', ascending=False)
            grouped_data = grouped_data.head(10)
            #print(grouped_data)
            return grouped_data
          else:
            print("I am sorry, I did not get that. Let's try again.")
            continue
      else:
        year = input('Invalid Year. \nPlease choose a year from 1985 to 2017: ').strip().title()
        continue


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

    # Load data
    nba_data = import_data()
    
    # Number of clues in the bank
    number_of_questions = 8

    # Select a random player
    player = select_random_player()

    # Define the URL of the image (work only on Google Colab env)
    player_data = nba_data[nba_data['player_name'] == player]
    url = player_data['image'].min()

    # Open the URL and download the image data (work only on Google Colab env)
    image_data = urllib.request.urlopen(url).read()

    # Create an Image object from the downloaded data (work only on Google Colab env)
    image = Image.open(io.BytesIO(image_data))

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
            resize_percentage = 50  # 50% of the original size
            image.thumbnail((image.width * resize_percentage // 100, image.height * resize_percentage // 100))
            display(image)

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
    resize_percentage = 50  # 50% of the original size
    image.thumbnail((image.width * resize_percentage // 100, image.height * resize_percentage // 100))
    display(image)

    # Return to main function
    time.sleep(2)
    choose_next()
    return

# Start game
def choose_first():
  while True:
    print("Welcome to the NBA trivia/stats generator!")
    print("Please choose one of the following:")
    print('1 - Play trivia')
    print('2 - Show stats')
    #game = input("\nChoose one option: ").strip().title()
    print("Choose one option:\n")
    game = input()

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


# Main function
def main():
    choose_first()
if __name__ == "__main__":
    main()