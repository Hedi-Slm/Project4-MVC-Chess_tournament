from collections import defaultdict
import uuid
from models.entities.match import Match
from models.entities.round import Round
from models.managers.match_manager import MatchManager
from models.managers.player_manager import PlayerManager
from models.managers.round_manager import RoundManager
from views.utilities_message_view import UtilitiesMessageView


class Tournament:
    def __init__(
        self,
        name,
        location,
        start_date,
        end_date,
        description,
        number_rounds=4,
        current_round=0,
        rounds=None,
        players=None,
        has_begun=False,
        already_met_players=None,
        players_scores=None,
        id=None,
    ):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.number_rounds = int(number_rounds)
        self.current_round = int(current_round)
        self.rounds = [] if rounds is None else rounds
        self.players = [] if players is None else players
        self.description = description
        self.has_begun = has_begun
        self.already_met_players = (
            defaultdict(list)
            if already_met_players is None
            else defaultdict(list, already_met_players)
        )
        self.players_scores = (
            defaultdict(int)
            if players_scores is None
            else defaultdict(int, players_scores)
        )
        self.id = id or str(uuid.uuid4())

    def valid_start_condition(self):
        number_of_players = len(self.players)
        if int(number_of_players) < 2 * int(self.number_rounds):
            UtilitiesMessageView.display_warning_message(
                "To avoid players facing multiple times during the"
                " tournament, there must be at least two times"
                " the number of players than rounds.")
            return False
        if int(number_of_players) % 2 != 0:
            UtilitiesMessageView.display_warning_message(
                "The number of players must be even to start the tournament."
            )
            return False

        return True

    def pair_players(self):
        if not self.players:
            return []

        sorted_players = sorted(
            self.players,
            key=lambda player: self.players_scores.get(player.chess_id, 0),
            reverse=True,
        )
        pairs = []
        while len(sorted_players) >= 2:
            player1 = sorted_players.pop(0)
            for player2 in sorted_players:
                if (
                    player1.chess_id
                    not in self.already_met_players[player2.chess_id]
                ):
                    pairs.append((player1, player2))
                    self.already_met_players[player1.chess_id].append(
                        player2.chess_id
                    )
                    self.already_met_players[player2.chess_id].append(
                        player1.chess_id
                    )
                    sorted_players.remove(player2)
                    break
        return pairs

    @staticmethod
    def create_matches(pairs):
        matches = []
        for player1, player2 in pairs:
            new_match = Match(player1, player2)
            matches.append(new_match)
        return matches

    def create_round(self):
        if int(self.current_round) >= int(self.number_rounds):
            print("Maximum number of rounds reached.")
            return None

        self.current_round += 1
        round_name = f"Round {self.current_round}"

        pairs = self.pair_players()
        matches = self.create_matches(pairs)
        MatchManager.save_matches(matches)

        new_round = Round(name=round_name, matches=matches)
        self.rounds.append(new_round)
        RoundManager.save_rounds(new_round)
        print(f"Round '{round_name}' created with {len(matches)} matches.")
        return new_round

    def to_dict(self):
        return {
            "name": self.name,
            "location": self.location,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "number_rounds": self.number_rounds,
            "current_round": self.current_round,
            "rounds": [
                rnd.round_id for rnd in self.rounds
            ],  # Save only round IDs
            "players": [
                player.chess_id for player in self.players
            ],  # Assume it's a list of player IDs
            "description": self.description,
            "has_begun": self.has_begun,
            "already_met_players": self.already_met_players,
            "players_scores": self.players_scores,
            "id": self.id,
        }

    @classmethod
    def from_dict(cls, data):
        # Load tournament with round and player IDs
        return cls(
            name=data["name"],
            location=data["location"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            number_rounds=int(data["number_rounds"]),
            current_round=int(data["current_round"]),
            rounds=RoundManager.load_rounds_to_tournament(data["rounds"]),
            players=PlayerManager.load_players_to_tournament(data["players"]),
            description=data["description"],
            has_begun=data["has_begun"],
            already_met_players=defaultdict(list, data["already_met_players"]),
            players_scores=defaultdict(int, data["players_scores"]),
            id=data["id"],
        )
