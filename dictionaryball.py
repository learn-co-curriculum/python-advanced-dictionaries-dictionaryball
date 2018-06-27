game_dictionary = {
    'home': {
        'team_name': "Brooklyn Nets",
        'colors': ["Black", "White"],
        'players': {
            "Alan Anderson": {'number': 0, 'shoe': 16, 'points': 22, 'rebounds': 12, 'assists': 12, 'steals': 3, 'blocks': 1, 'slam_dunks': 1 },
            "Reggie Evans": {'number': 30, 'shoe': 14, 'points': 12, 'rebounds': 12, 'assists': 12, 'steals': 12, 'blocks': 12, 'slam_dunks': 7 },
            "Brook Lopez": {'number': 11, 'shoe': 17, 'points': 17, 'rebounds': 19, 'assists': 10, 'steals': 3, 'blocks': 1, 'slam_dunks': 15 },
            "Mason Plumlee": {'number': 1, 'shoe': 19, 'points': 26, 'rebounds': 12, 'assists': 6, 'steals': 3, 'blocks': 8, 'slam_dunks': 5 },
            "Jason Terry": {'number': 31, 'shoe': 15, 'points': 19, 'rebounds': 2, 'assists': 2, 'steals': 4, 'blocks': 11, 'slam_dunks': 1 }
        }
    },
    'away': {
        'team_name': "Charlotte Hornets",
        'colors': ["Turquoise", "Purple"],
        'players': {
            "Jeff Adrien": {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2 },
            "Bismak Biyombo": {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10 },
            "DeSagna Diop": {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5 },
            "Ben Gordon": {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0 },
            "Brendan Haywood": {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12 }
        }
    }
}

def game_dict():
    return game_dictionary

def num_points_scored(name):
    player = find_the_player(name)
    return player[name]['points']


def shoe_size(name):
    player = find_the_player(name)
    return player[name]['shoe']


def team_colors(team_name):
    team = find_the_team(team_name)
    return team['colors']


def team_names():
    return [team['team_name'] for team in teams()]


def player_numbers(team_name):
    return [player_stats(player)['number'] for player in find_the_team(team_name)['players']]


def player_stats(player_name):
    return players()[player_name]


def big_shoe_rebounds():
    name = list(player_biggest_shoe_size())[0]
    return player_biggest_shoe_size()[name]['rebounds']


def teams():
    return game_dict().values()


def players():
    players = {}
    all_teams = teams()
    for team in all_teams:
        for player , stats in team['players'].items():
            players[player] = stats
    return players


def find_the_team(team_name):
    return next((team for team in teams() if team['team_name'].lower() == team_name.lower()), "{team_name} not playing this game".format(team_name=team_name))


def find_the_player(name):
    all_teams = teams()
    for team in all_teams:
        return next(({player: stats} for player , stats in team['players'].items() if player.lower() == name.lower()), None)

def player_biggest_shoe_size():
    player_dicts = players()
    all_players = [{player: stats} for player,stats in player_dicts.items()]
    current_player = all_players[0]
    current_player_name = list(current_player)[0]
    for player in all_players:
        for name, stats in player.items():
            if stats['shoe'] > player_dicts[current_player_name]['shoe']:
                current_player = player
                current_player_name = list(current_player)[0]
    return current_player

for team, data in game_dict().items():
    for team_data, other in data.items():
        print(team_data)
# print(num_points_scored('Mason Plumlee'))
# print(find_the_player('Mason Plumlee'))
# print(player_stats('Mason Plumlee'))
# print(player_numbers("Charlotte Hornets"))
# print(player_biggest_shoe_size())
# print(players())
# print(teams())
# print(team_names())
# print(big_shoe_rebounds())
# print(team_colors("Charlotte Hornets"))
