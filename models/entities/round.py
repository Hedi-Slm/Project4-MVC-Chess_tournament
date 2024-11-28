import uuid
from datetime import datetime
from models.managers.match_manager import MatchManager


class Round:
    def __init__(self, name, start_date=str(datetime.now()), end_date=None, matches=None, round_id=None,
                 is_ended=False):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.matches = [] if matches is None else matches
        self.is_ended = is_ended
        self.round_id = round_id or str(uuid.uuid4())

    def end_round(self):
        self.end_date = str(datetime.now())
        self.is_ended = True

    def to_dict(self):
        return {
            "name": self.name,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "matches": [match.match_id for match in self.matches],  # Save only match IDs
            "round_id": self.round_id,
            "is_ended": self.is_ended,
        }

    @classmethod
    def from_dict(cls, data):
        # Load round with match IDs
        return cls(
            name=data["name"],
            start_date=data["start_date"],
            end_date=data["end_date"],
            matches=MatchManager.load_matches_to_round(data["matches"]),
            round_id=data["round_id"],
            is_ended=data["is_ended"],
        )

