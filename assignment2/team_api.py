

from flask import Flask, request
import json
from team import Team
from player_forward import PlayerForward
from player_goalie import PlayerGoalie


PLAYER_TYPE_FORWARD = "forward"
PLAYER_TYPE_GOALIE = "goalie"

app = Flask(__name__)

team = Team("./players.json")


@app.route('/team/players', methods=['POST'])
def add_player():
    """ Adds a player to the team """
    content = request.json

    try:
        player_id = content['']
        player_type = content['fname']
        print(player_type)

        if player_type is PLAYER_TYPE_FORWARD:
            #player = PlayerForward(content['fname'], content['lname'], content['height'], content['weight'], content['jersey_num'], content['date_birth'], content['year_joined'], content['zone'], content['shooting_hand'], content['goals'], content['assists'], content['total_shots'], content['player_type'])
            
            response = app.response_class(
                response = "success",
                status = 200
            )
        elif player_type is PLAYER_TYPE_GOALIE:
            #player = PlayerGoalie(content['fname'], content['lname'], content['height'], content['weight'], content['jersey_num'], content['date_birth'], content['year_joined'], content["shots_against"], content["goals_against"], content["goals_saved"], content["games_played"], content["games_won"], content["games_lost"], content["player_type"])

            response = app.response_class(
                response = "success",
                status = 200
            )

        else:
            raise Exception
    except ValueError as e:
        response = app.response_class(
            response = str(e),
            status = 400
        )

    return response

    
if __name__ == "__main__":
    app.run()