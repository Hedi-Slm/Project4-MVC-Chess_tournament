import json
import os
from models.entities.player import Player
from utils.utilities import PLAYER_DATA_LOCATION
from views.utilities_message_view import UtilitiesMessageView


class PlayerManager:
    @staticmethod
    def load_all_players_object():
        if not os.path.exists(PLAYER_DATA_LOCATION):
            return {}

        try:
            with open(PLAYER_DATA_LOCATION, "r", encoding="utf-8") as file:
                data = json.load(file)
            return {key: Player(**player) for key, player in data.items()}
        except (OSError, json.JSONDecodeError) as e:
            UtilitiesMessageView.display_error_message(
                f"Error loading players: {e}"
            )
            return {}

    @staticmethod
    def get_id_in_player_database(chess_id):
        # Get or create a player with the given chess ID
        players = PlayerManager.load_all_players_object()
        if chess_id in players:
            return players[chess_id]
        return False

    @staticmethod
    def save_players(players):
        serialized_players = {
            player.chess_id: player.to_dict() for player in players.values()
        }
        try:
            with open(PLAYER_DATA_LOCATION, "w", encoding="utf-8") as file:
                json.dump(serialized_players, file, indent=4)
        except OSError as e:
            UtilitiesMessageView.display_error_message(
                f"Error saving players: {e}"
            )

    @staticmethod
    def create_player(player_info):
        # Create a new player instance
        return Player(**player_info)

    @staticmethod
    def load_players_to_tournament(player_id_list):
        players_db = PlayerManager.load_all_players_object()
        return [players_db[player_id] for player_id in player_id_list]
