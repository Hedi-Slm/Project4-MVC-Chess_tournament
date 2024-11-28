import json
import os
from models.managers.round_manager import RoundManager
from models.entities.tournament import Tournament
from utils.utilities import TOURNAMENTS_DATA_LOCATION
from views.utilities_message_view import UtilitiesMessageView


class TournamentManager:
    @staticmethod
    def load_all_tournaments_object():
        if not os.path.exists(TOURNAMENTS_DATA_LOCATION):
            return {}
        try:
            with open(TOURNAMENTS_DATA_LOCATION, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as e:
            UtilitiesMessageView.display_error_message(f"Error loading tournaments: {e}")
        return {key: Tournament.from_dict(value) for key, value in data.items()}

    @staticmethod
    def load_all_tournaments_dict():
        if not os.path.exists(TOURNAMENTS_DATA_LOCATION):
            return {}
        try:
            with open(TOURNAMENTS_DATA_LOCATION, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as e:
            UtilitiesMessageView.display_error_message(f"Error loading tournaments: {e}")
        return data

    @staticmethod
    def create_tournament(details):
        tournament = Tournament(**details)
        return tournament

    @staticmethod
    def save_tournaments(tournament):
        loaded_tournaments = TournamentManager.load_all_tournaments_dict()
        for key, value in loaded_tournaments.items():
            if key == tournament.id:
                loaded_tournaments[key] = tournament.to_dict()
                break
        else:
            loaded_tournaments[tournament.id] = tournament.to_dict()

        try:
            with open(TOURNAMENTS_DATA_LOCATION, "w", encoding="utf-8") as file:
                json.dump(loaded_tournaments, file, indent=4)
        except Exception as e:
            UtilitiesMessageView.display_error_message(f"Error saving tournaments: {e}")

    @staticmethod
    def end_tournament_round(current_tournament, current_round):
        matches_results = RoundManager.end_current_round_matches(current_round)
        if not matches_results:
            return False
        for match_result in matches_results:
            player_id = match_result[0]
            player_score = match_result[1]
            current_tournament.players_scores[player_id] += player_score

    @staticmethod
    def check_previous_round_end(current_tournament):
        previous_round = current_tournament.rounds[-1]
        if previous_round.is_ended:
            return True
        return False
