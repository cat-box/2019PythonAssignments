from team import Team
from player_forward import PlayerForward

team = Team("players.sqlite")

player = PlayerForward("Sven", "Baertschi", 180.34, 190, 47, "Oct 5, 1992", 2011, "LW", "L", 8, 5, 40, "forward")

print(team.add(player))
# team.delete(2493305080408)
