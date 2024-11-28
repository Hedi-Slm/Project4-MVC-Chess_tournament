import re
from datetime import datetime
from views.utilities_message_view import UtilitiesMessageView

TOURNAMENTS_DATA_LOCATION = 'data/tournaments.json'
ROUNDS_DATA_LOCATION = 'data/rounds.json'
MATCHES_DATA_LOCATION = 'data/matches.json'
PLAYER_DATA_LOCATION = 'data/players.json'


def get_valid_date(message="Enter a date (dd/mm/yyyy): "):
    while True:
        user_input = input(message)
        try:
            # Validate and parse the input date
            return datetime.strptime(user_input, "%d/%m/%Y")
        except ValueError:
            UtilitiesMessageView.display_error_message("Invalid date format! Please use dd/mm/yyyy.")


def check_chess_id_format(chess_id):
    if re.match(r"^[A-Za-z]{2}\d{5}$", chess_id):
        return True
    UtilitiesMessageView.display_warning_message("ID must be 2 characters followed by 5 digits")
    return False

