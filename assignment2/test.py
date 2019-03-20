from player_forward import PlayerForward
from team import Team
import json

player1 = PlayerForward("Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40)
player2 = PlayerForward("John", "Doe", 123, 23, 3, "Sept 2, 2534", "1234", "WN", "R", 3, 5, 65)

team = Team("./players.json")

#team.add(player1)
#print(json.dumps(((team.get_all_players())[0].to_dict()), indent=4))
#print(id((team.get_all_players())[0]))
# team.delete(id(player2))

#player_list = team.get_all_players()
#player1 = player_list[0]
#print(player1.to_dict())

print(json.dumps((team.get_all_players())["2380120105032"], indent=4))