from player_forward import PlayerForward
from team import Team

player1 = PlayerForward("Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40)
player2 = PlayerForward("John", "Doe", 123, 23, 3, "Sept 2, 2534", "1234", "WN", "R", 3, 5, 65)

team = Team()

team.add(player1)
print((team.get_all_players())[0]._id)
print(id((team.get_all_players())[0]))
# team.delete(id(player2))
