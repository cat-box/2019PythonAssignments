from player_forward import PlayerForward
from player_goalie import PlayerGoalie
from team import Team
import json
import os

player1 = PlayerForward("Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", "2011", "LW", "L", 8, 5, 40, "forward")
player2 = PlayerForward("John", "Doe", 123, 23, 3, "Sept 2, 2534", "1234", "WN", "R", 3, 5, 65, "Forward")
player3 = PlayerGoalie("Bob", "Smith", 321, 100, 4, "Jan 1, 1990", "2000", 123, 432, 40, 20, 20, 20, "goalie") 

team = Team("C:\\Users\\cathy\\OneDrive\\Documents\\2019_SPRING\\2019PythonAssignments\\assignment2\\players.json")

team.add(player1)
team.add(player2)
team.add(player3)



#print(id((team.get_all_players())[0]))
# team.delete(id(player2))

#player_list = team.get_all_players()
#player1 = player_list[0]
#print(player1.to_dict())

#team.add(player3)


#print(json.dumps((team.get_all_players())["2380120105032"], indent=4))

print(repr(team))