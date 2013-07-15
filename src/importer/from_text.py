''' Via python manage.py shell_plus from /src/,
    run execfile('importer/from_text.py')
'''
from players import models
import datetime

pd_file = open('importer/text_data/mens_players.data', 'rb')
dd_file = open('importer/text_data/mens_doubles_teams.data', 'rb')


def save_player(first_name, last_name, birthday_parts):
    p = Player(
        first_name=first_name,
        last_name=last_name,
        gender=models.Gender.MALE,
        birthday=datetime.date(*birthday_parts),
    )
    p.save()
    return p


def get_pair(line):
    players = []
    for player_name in line.rstrip().split(','):
        (first_name, last_name) = player_name.strip().split(' ')
        players.append(
            Player.objects.get(first_name=first_name, last_name=last_name)
        )
    players = sorted(players, key=lambda p: p.id)
    return players


def save_pair(players):
    s = Side(player_a=players[0])

    if len(players) == 1:
        s.type=models.SideType.SINGLES
    elif len(players) == 2:
        s.player_b=players[1]
        s.type=models.SideType.DOUBLES

    s.save()
    s.players = players
    s.save()
    return s


for line in pd_file:
    birthday_parts = line.rstrip().split(',')

    name = birthday_parts.pop(0)
    first_name, last_name = name.split('.')

    birthday_parts = map(int, birthday_parts)

    p = save_player(first_name, last_name, birthday_parts)
    s = save_pair([ p ])


for line in dd_file:
    save_pair(get_pair(line))
