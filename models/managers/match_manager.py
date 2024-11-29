import json
import os
from models.entities.match import Match
from utils.utilities import MATCHES_DATA_LOCATION
from views.utilities_message_view import UtilitiesMessageView


class MatchManager:
    @staticmethod
    def load_all_matches_object():
        if not os.path.exists(MATCHES_DATA_LOCATION):
            return {}
        try:
            with open(MATCHES_DATA_LOCATION, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as e:
            UtilitiesMessageView.display_error_message(
                f"Error loading matches: {e}"
            )
        return {key: Match.from_dict(value) for key, value in data.items()}

    @staticmethod
    def load_all_matches_dict():
        if not os.path.exists(MATCHES_DATA_LOCATION):
            return {}
        try:
            with open(MATCHES_DATA_LOCATION, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as e:
            UtilitiesMessageView.display_error_message(
                f"Error loading matches: {e}"
            )
        return data

    @staticmethod
    def save_matches(matches):
        loaded_matches = MatchManager.load_all_matches_dict()
        for match_ in matches:
            for key, value in loaded_matches.items():
                if match_.match_id == key:
                    loaded_matches[key] = match_.to_dict()
                    break
            else:
                loaded_matches[match_.match_id] = match_.to_dict()
        try:
            with open(MATCHES_DATA_LOCATION, "w", encoding="utf-8") as file:
                json.dump(loaded_matches, file, indent=4)
        except Exception as e:
            UtilitiesMessageView.display_error_message(
                f"Error saving matches: {e}"
            )

    @staticmethod
    def load_matches_to_round(match_id_list):
        matches_db = MatchManager.load_all_matches_object()
        return [matches_db[match_id] for match_id in match_id_list]
