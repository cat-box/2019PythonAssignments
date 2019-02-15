from team import Team
from player_forward import PlayerForward
from player_goalie import PlayerGoalie

team_a = Team()
forward = PlayerForward(47, "Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40)
goalie = PlayerGoalie(1, "Roberto", "Luongo", 190.5, 215, 1, "Apr 4, 1979", 1997, 788, 83, 705, 30, 12, 13)

forward_update = PlayerForward(47, "QUACK", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40)

team_a.add(forward)
team_a.add(goalie)

team_a.update(forward_update)

list_players = team_a.get_all_players()

player_1 = list_players[0].get_fname()
player_2 = list_players[1].get_fname()

print(player_1)
print(player_2)