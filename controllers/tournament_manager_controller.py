from models.managers.match_manager import MatchManager
from models.managers.round_manager import RoundManager
from views.player_view import PlayerView
from views.tournament_manager_view import TournamentManagerView
from models.managers.player_manager import PlayerManager
from models.managers.tournament_manager import TournamentManager
from utils.utilities import check_chess_id_format
from views.utilities_message_view import UtilitiesMessageView


class TournamentManagerController:
    def __init__(self, tournaments):
        self.tournaments = tournaments
        self.chosen_tournament = self.choose_tournament()
        self.rounds = RoundManager.load_all_rounds_object()
        self.matches = MatchManager.load_all_matches_object()
        self.players = PlayerManager.load_all_players_object()

    def choose_tournament(self):
        choice = TournamentManagerView.choose_tournament(
            list(self.tournaments.values())
        )
        return choice

    def modify_tournament_details(self):
        if self.chosen_tournament.has_begun:
            UtilitiesMessageView.display_warning_message(
                "Tournament has already begun. Details cannot be changed."
            )
            return

        while True:
            TournamentManagerView.change_tournament_details_menu(
                self.chosen_tournament
            )
            choice = TournamentManagerView.get_user_choice()

            match choice:
                case "1":
                    new_tournament_name = (
                        TournamentManagerView.get_new_tournament_name(
                            self.chosen_tournament.name
                        )
                    )
                    self.chosen_tournament.name = new_tournament_name
                    TournamentManager.save_tournaments(self.chosen_tournament)
                case "2":
                    new_tournament_location = (
                        TournamentManagerView.get_new_tournament_location(
                            self.chosen_tournament.location
                        )
                    )
                    self.chosen_tournament.location = new_tournament_location
                    TournamentManager.save_tournaments(self.chosen_tournament)
                case "3":
                    new_tournament_start_date = (
                        TournamentManagerView.get_new_tournament_start_date(
                            self.chosen_tournament.start_date,
                            self.chosen_tournament.end_date,
                        )
                    )
                    self.chosen_tournament.start_date = (
                        new_tournament_start_date
                    )
                    TournamentManager.save_tournaments(self.chosen_tournament)
                case "4":
                    new_tournament_end_date = (
                        TournamentManagerView.get_new_tournament_end_date(
                            self.chosen_tournament.end_date,
                            self.chosen_tournament.start_date,
                        )
                    )
                    self.chosen_tournament.end_date = new_tournament_end_date
                    TournamentManager.save_tournaments(self.chosen_tournament)
                case "5":
                    new_tournament_number_rounds = (int(
                        TournamentManagerView.get_new_number_of_rounds(
                            self.chosen_tournament.number_rounds
                        ))
                    )
                    self.chosen_tournament.number_rounds = (
                        new_tournament_number_rounds
                    )
                    TournamentManager.save_tournaments(self.chosen_tournament)
                case "6":
                    new_tournament_description = (
                        TournamentManagerView.get_new_tournament_description(
                            self.chosen_tournament.description
                        )
                    )
                    self.chosen_tournament.description = (
                        new_tournament_description
                    )
                    TournamentManager.save_tournaments(self.chosen_tournament)
                case "7":
                    break
                case _:
                    UtilitiesMessageView.display_error_message(
                        "Invalid choice"
                    )

    def add_player_to_tournament_and_db(self):
        player_id = TournamentManagerView.get_player_id()
        if not check_chess_id_format(player_id):
            UtilitiesMessageView.display_warning_message(
                "Invalid Chess ID format."
            )
            return

        if player_id in [
            player.chess_id for player in self.chosen_tournament.players
        ]:
            UtilitiesMessageView.display_warning_message(
                "Player is already registered in this tournament."
            )
            return

        if player_id not in self.players:
            player_data = PlayerView.get_player_details(player_id)
            temp_player = PlayerManager.create_player(player_data)
            self.players[player_id] = temp_player
            self.chosen_tournament.players.append(temp_player)
            PlayerManager.save_players(self.players)
        else:
            self.chosen_tournament.players.append(self.players[player_id])

        UtilitiesMessageView.display_success_message(
            "Player added to tournament successfully."
        )

        TournamentManager.save_tournaments(self.chosen_tournament)

    def start_new_round(self):
        started = False
        if not self.chosen_tournament.has_begun:
            if not self.chosen_tournament.valid_start_condition():
                return
            self.chosen_tournament.has_begun = True
        else:
            started = True

        if started:
            if not TournamentManager.check_previous_round_end(
                    self.chosen_tournament
            ):
                UtilitiesMessageView.display_warning_message(
                    "Cannot start new round: Previous round has not ended."
                )
                return
        new_round = self.chosen_tournament.create_round()
        if not new_round:
            return
        TournamentManager.save_tournaments(self.chosen_tournament)
        UtilitiesMessageView.display_success_message(
            f"New round '{new_round.name}' created successfully."
        )

    def end_round(self):
        if not self.chosen_tournament.rounds:
            UtilitiesMessageView.display_warning_message(
                "Tournament has not begun yet."
            )
            return

        current_round = self.chosen_tournament.rounds[-1]

        if current_round.is_ended:
            UtilitiesMessageView.display_warning_message(
                "There is no round in progress that can be ended,"
                " please start a new round first."
            )
            return

        TournamentManager.end_tournament_round(
            self.chosen_tournament, current_round
        )
        RoundManager.save_rounds(current_round)
        TournamentManager.save_tournaments(self.chosen_tournament)
        UtilitiesMessageView.display_success_message(
            "Round ended and scores updated."
        )

    def show_tournament_manager_menu(self):
        while True:
            choice = TournamentManagerView.show_tournament_manager_menu()

            match choice:
                case "1":
                    self.modify_tournament_details()
                case "2":
                    self.start_new_round()
                case "3":
                    TournamentManagerView.display_tournament_details(
                        self.chosen_tournament
                    )
                case "4":
                    TournamentManagerView.display_players(
                        self.chosen_tournament.players
                    )
                case "5":
                    self.add_player_to_tournament_and_db()
                case "6":
                    self.end_round()
                case "7":
                    break
                case _:
                    UtilitiesMessageView.display_error_message(
                        "Invalid choice. Please try again."
                    )
