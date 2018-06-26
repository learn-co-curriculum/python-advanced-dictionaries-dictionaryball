game_dict = {
    'home': {
        'team_name': "Brooklyn Nets",
        'colors': ["Black", "White"],
        'players': [
            {'name': "Alan Anderson", 'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1 },
            {'name': "Reggie Evans", 'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12, 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7 },
            {'name': "Brook Lopez", 'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19, 'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15 },
            {'name': "Mason Plumlee", 'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5 },
            {'name': "Jason Terry", 'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2, 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1 }
        ]
    },
    'away': {
        'team_name': "Charlotte Hornets",
        'colors': ["Turquoise", "Purple"],
        'players': [
            {'name': "Jeff Adrien", 'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2 },
            {'name': "Bismak Biyombo", 'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10 },
            {'name': "DeSagna Diop", 'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5 },
            {'name': "Ben Gordon", 'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0 },
            {'name': "Brendan Haywood", 'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12 }
        ]
    }
}

def game_dictionary():
    return game_dict

def num_points_scored(name):
    player = find_the_player(name)
    return player['points']


def shoe_size(name):
    player = find_the_player(name)
    return player['shoe']


def team_colors(team_name):
    team = find_the_team(team_name)
    return team['colors']


def team_names():
    return [team['team_name'] for team in teams()]


def player_numbers(team_name):
    return [player['number'] for player in find_the_team(team_name)['players']]


def player_stats(player_name):
    return find_the_player(player_name)


def big_shoe_rebounds():
    return player_biggest_shoe_size()['rebounds']


def teams():
    return game_dict.values()


def players():
    players = []
    for team in teams():
        for player in team['players']:
            players.append(player)
    return players


def find_the_team(team_name):
    return next((team for team in teams() if team['team_name'].lower() == team_name.lower()), "{team_name} not playing this game".format(team_name=team_name))


def find_the_player(name):
    return next(player for player in players() if player['name'] == name)


def player_biggest_shoe_size():
    all_players = players()
    current_player = all_players[0]
    for player in all_players:
        if player['shoe'] > current_player['shoe']:
            current_player = player
    return current_player
