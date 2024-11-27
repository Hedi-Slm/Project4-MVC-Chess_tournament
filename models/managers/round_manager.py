import json
import os
from models.managers.match_manager import MatchManager
from models.entities.round import Round
from utils.utilities import ROUNDS_DATA_LOCATION


class RoundManager:
    @staticmethod
    def load_all_rounds_object():
        if not os.path.exists(ROUNDS_DATA_LOCATION):
            return {}
        try:
            with open(ROUNDS_DATA_LOCATION, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as e:
            print(f"Error loading rounds: {e}")
        return {key: Round.from_dict(value) for key, value in data.items()}

    @staticmethod
    def load_all_rounds_dict():
        if not os.path.exists(ROUNDS_DATA_LOCATION):
            return {}
        try:
            with open(ROUNDS_DATA_LOCATION, "r", encoding="utf-8") as file:
                data = json.load(file)
        except Exception as e:
            print(f"Error loading rounds: {e}")
        return data

    @staticmethod
    def end_current_round_matches(current_round):
        match_results = []
        for match in current_round.matches:
            match_result = match.set_result()
            if not match_result:
                return False
            match_results.append(match_result[0])
            match_results.append(match_result[1])

        MatchManager.save_matches(current_round.matches)
        current_round.end_round()
        RoundManager.save_rounds(current_round)
        return match_results

    @staticmethod
    def load_rounds_to_tournament(round_id_list):
        rounds_db = RoundManager.load_all_rounds_object()
        return [rounds_db[round_id] for round_id in round_id_list]

    @staticmethod
    def save_rounds(rounds):
        loaded_rounds = RoundManager.load_all_rounds_dict()

        round_dict = rounds.to_dict()

        for key, value in loaded_rounds.items():
            if key == rounds.round_id:
                loaded_rounds[key] = round_dict  # Replace the round with updated data
                break
        else:
            loaded_rounds[rounds.round_id] = round_dict  # Add new round if it doesn't exist

        try:
            with open(ROUNDS_DATA_LOCATION, "w", encoding="utf-8") as file:
                json.dump(loaded_rounds, file, indent=4)
        except Exception as e:
            print(f"Error saving rounds: {e}")

