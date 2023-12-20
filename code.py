import csv

# Define the path to the CSV file
csv_file = 'Full_Dataset.csv'  # Replace with the actual path to your CSV file

# Initialize variables for analysis
num_rows = 0
num_cols = 0
columns = []
total_goals = 0
season_goals = {}
league_goals = {}
time_goals = {}

#Read the CSV file and return the data as a list of lists
def read_csv_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Process the data to calculate the statistics
def process_data(data):
    for row in data[1:]:
        process_row(row)

# Calculate the basic statistics for the dataset
def calculate_basic_statistics(data):
    global num_rows, num_cols, columns
    num_rows = len(data)
    num_cols = len(data[0])
    columns = data[0]

# Process each row of the data
def process_row(row):
    global total_goals
    if row[4] and row[5]:
        season = row[1][-4:]
        league = row[-1]
        if season not in season_goals:
            season_goals[season] = {'total_goals': 0, 'num_matches': 0}
        if league not in league_goals:
            league_goals[league] = {'total_goals': 0, 'num_matches': 0}
        if row[2] not in time_goals:
            time_goals[row[2]] = {'total_goals': 0, 'num_matches': 0}
        total_goals = float(row[4]) + float(row[5])
        season_goals[season]['total_goals'] += total_goals
        season_goals[season]['num_matches'] += 1
        league_goals[league]['total_goals'] += total_goals
        league_goals[league]['num_matches'] += 1
        time_goals[row[2]]['total_goals'] += total_goals
        time_goals[row[2]]['num_matches'] += 1

# Calculate the average goals per season
def calculate_average_goals_per_season():
    if num_rows > 1:
        min_season = ''
        min_average_goals = float('inf')
        max_season = ''
        max_average_goals = 0
        for season, goals in season_goals.items():
            average_goals = goals['total_goals'] / goals['num_matches']
            if average_goals > max_average_goals:
                max_season = season
                max_average_goals = average_goals
            if average_goals < min_average_goals:
                min_season = season
                min_average_goals = average_goals
        return max_season, min_season
    else:
        return None, None

# Calculate the average goals per league
def calculate_average_goals_per_league():
    if num_rows > 1:
        max_league = ''
        min_league = ''
        max_average_goals = 0
        min_average_goals = float('inf')
        for league, goals in league_goals.items():
            average_goals = goals['total_goals'] / goals['num_matches']
            if average_goals > max_average_goals:
                max_league = league
                max_average_goals = average_goals
            if average_goals < min_average_goals:
                min_league = league
                min_average_goals = average_goals
        return max_league, min_league
    else:
        return None, None

# Calculate the time with the most goals
def calculate_time_with_most_goals():
    if num_rows > 1:
        max_time = ''
        max_goals = 0
        for time, goals in time_goals.items():
            if goals['total_goals'] > max_goals:
                max_time = time
                max_goals = goals['total_goals']
        return max_time
    else:
        return None

# Main function
if __name__ == "__main__":
    data = read_csv_file(csv_file)
    calculate_basic_statistics(data)
    process_data(data)

    # Basic Dataset Statistics
    print("Basic Dataset Statistics:")
    print("Number of rows:", num_rows)
    print("Number of columns:", num_cols)
    print("Columns:", columns)

    max_season, min_season = calculate_average_goals_per_season()
    max_league = calculate_average_goals_per_league()
    max_time = calculate_time_with_most_goals()

    if max_season and min_season:
        print("Season with the highest average goals per match:", max_season)
        print("Season with the lowest average goals per match:", min_season)
    else:
        print("No match data found in the CSV for season statistics.")

    if max_time:
        print("Time when teams score the most goals:", max_time)
    else:
        print("No match data found in the CSV for time statistics.")

    max_league, min_league = calculate_average_goals_per_league()

    if max_league:
        print("League with the highest average goals per match:", max_league)
    else:
        print("No match data found in the CSV for league statistics.")

    if min_league:
        print("League with the lowest average goals per match:", min_league)
    else:
     print("No match data found in the CSV for league statistics.")
