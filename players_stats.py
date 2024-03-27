# Show statistics
def general_stats():
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