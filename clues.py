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