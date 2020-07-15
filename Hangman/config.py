new_game = 0

games_completed = 0
games_won = 0
win_percentage = 0


def add_game():
    global games_completed
    games_completed += 1
    return games_completed


def add_win():
    global games_won
    games_won += 1
    return games_won

def add_loss():
    global games_won
    games_won += 0
    return games_won


def calculate_win_percentage():
    global win_percentage
    global games_won
    global games_completed
    return int(games_won * 100 / games_completed)
