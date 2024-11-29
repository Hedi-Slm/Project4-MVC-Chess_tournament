import uuid
from models.managers.player_manager import PlayerManager
from views.tournament_manager_view import TournamentManagerView
from views.utilities_message_view import UtilitiesMessageView


class Match:
    def __init__(
        self,
        player1,
        player2,
        player1_score=0,
        player2_score=0,
        match_result=None,
        match_id=None,
    ):
        self.player1 = player1
        self.player2 = player2
        self.player1_score = int(player1_score)
        self.player2_score = int(player2_score)
        self.match_result = (
            (
                [self.player1, self.player1_score],
                [self.player2, self.player2_score],
            )
            if match_result
            else ()
        )
        self.match_id = match_id or str(uuid.uuid4())

    def set_result(self):
        result = TournamentManagerView.set_match_result(
            self.player1, self.player2
        )
        match result:
            case "1":
                self.player1_score = 1
            case "2":
                self.player2_score = 1
            case "3":
                self.player1_score = 0.5
                self.player2_score = 0.5
            case _:
                UtilitiesMessageView.display_error_message("Invalid choice")
                return False
        self.match_result = (
            [self.player1, self.player1_score],
            [self.player2, self.player2_score],
        )
        return [
            (self.player1.chess_id, self.player1_score),
            (self.player2.chess_id, self.player2_score),
        ]

    def to_dict(self):
        return {
            "player1": self.player1.chess_id,
            "player2": self.player2.chess_id,
            "player1_score": self.player1_score,
            "player2_score": self.player2_score,
            "match_result": (
                [self.player1.chess_id, self.player1_score],
                [self.player2.chess_id, self.player2_score],
            ),
            "match_id": self.match_id,
        }

    @classmethod
    def from_dict(cls, data):
        player1 = PlayerManager.get_id_in_player_database(data["player1"])
        player2 = PlayerManager.get_id_in_player_database(data["player2"])
        return cls(
            player1=player1,
            player2=player2,
            player1_score=int(data["player1_score"]),
            player2_score=int(data["player2_score"]),
            match_result=(
                [player1, int(data["player1_score"])],
                [player2, int(data["player2_score"])],
            ),
            match_id=data["match_id"],
        )
