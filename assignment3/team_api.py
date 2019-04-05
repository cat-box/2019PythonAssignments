from flask import Flask, request
import json
from team import Team
from player_forward import PlayerForward
from player_goalie import PlayerGoalie


app = Flask(__name__)

PLAYERS_DB = "players.sqlite"

team = Team(PLAYERS_DB)

PLAYER_TYPE_FORWARD = "forward"
PLAYER_TYPE_GOALIE = "goalie"


@app.route('/team/players', methods=['POST'])
def add_player():
    """ Adds a player to the team """
    content = request.json

    try:
        print(content['player_type'])
        player_type = content["player_type"].lower()

        if player_type == PLAYER_TYPE_FORWARD:
            player = PlayerForward(content["fname"], content["lname"], content["height"], content["weight"], content["jersey_num"], content["date_birth"], content["year_joined"], content["zone"], content["shooting_hand"], content["goals"], content["assists"], content["total_shots"], content["player_type"])

            id = str(team.add(player))

            response = app.response_class(
                status=200,
                response=id
            )
        elif player_type == PLAYER_TYPE_GOALIE:
            player = PlayerGoalie(content["fname"], content["lname"], content["height"], content["weight"], content["jersey_num"], content["date_birth"], content["year_joined"], content["shots_against"], content["goals_against"], content["goals_saved"], content["games_played"], content["games_won"], content["games_lost"], content["player_type"])

            id = str(team.add(player))

            response = app.response_class(
                status=200,
                response=id
            )
        else:
            raise Exception
    except ValueError as e:
        response = app.response_class(
            response=str(e),#"Player is invalid",
            status=400
        )

    return response


@app.route("/team/players/<int:player_id>", methods=["PUT"])
def update_player(player_id):
    """ Updates player's attributes """
    content = request.json

    try:
        player_type = content["player_type"].lower()

        if player_type == PLAYER_TYPE_FORWARD:
            player = PlayerForward(content["fname"], content["lname"], content["height"], content["weight"], content["jersey_num"], content["date_birth"], content["year_joined"], content["zone"], content["shooting_hand"], content["goals"], content["assists"], content["total_shots"], content["player_type"])
            player.id = player_id
            team.update(player)
            response = app.response_class(
                status=200
            )
        elif player_type == PLAYER_TYPE_GOALIE:
            player = PlayerGoalie(content["fname"], content["lname"], content["height"], content["weight"], content["jersey_num"], content["date_birth"], content["year_joined"], content["shots_against"], content["goals_against"], content["goals_saved"], content["games_played"], content["games_won"], content["games_lost"], content["player_type"])
            player.id = player_id
            team.update(player)
            response = app.response_class(
                status=200
            )
        else:
            raise Exception

    except ValueError as e:
        response = app.response_class(
            status=404,
            response=str(e)
        )

    return response


@app.route("/team/players/<int:player_id>", methods=["DELETE"])
def remove_player(player_id):
    """ Removes player """
    try:
        team.delete(player_id)

        response = app.response_class(
            status=200
        )

    except Exception as e:
        response = app.response_class(
            status=404,
            response=str(e)
        )

    return response


@app.route("/team/players/<int:player_id>", methods=["GET"])
def get_player(player_id):
    """ Gets player by player_id """
    try:
        player = team.get_player(player_id)
        
        response = app.response_class(
            status=200,
            response=json.dumps(player.to_dict()),
            mimetype="application/json"
        )
    except:
        response = app.response_class(
            status=404,
            response="Player not found"
        )

    return response
    

@app.route("/team/players/all", methods=["GET"])
def get_all_players():
    """ Gets all players in team """
    players = team.get_all_players()

    player_list = []

    for player in players:
        player_list.append(player.to_dict())
    
    response = app.response_class(
        status=200,
        response = json.dumps(player_list),
        mimetype="application/json"
    )

    return response


@app.route("/team/players/all/<player_type>", methods=["GET"])
def get_players_of_type(player_type):
    """ Gets all players of a type """
    try:
        players_of_type = team.get_all_by_type(player_type)

        player_list = []

        for player in players_of_type:
            player_list.append(player.to_dict())
        
        response = app.response_class(
            status=200,
            response=json.dumps(player_list),
            mimetype="application/json"
        )
    except:
        response = app.response_class(
            status=400,
            response="Invalid player type"
        )

    return response


if __name__ == "__main__":  
    app.run()
