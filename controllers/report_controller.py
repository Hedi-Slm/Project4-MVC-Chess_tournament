from models.managers.player_manager import PlayerManager
from models.managers.round_manager import RoundManager
from models.managers.tournament_manager import TournamentManager
from views.player_view import PlayerView
from views.report_view import ReportView
from views.tournament_manager_view import TournamentManagerView
from views.tournament_view import TournamentView
from views.utilities_message_view import UtilitiesMessageView


class ReportController:
    def __init__(self):
        self.players = PlayerManager.load_all_players_object()
        self.tournaments = TournamentManager.load_all_tournaments_object()
        self.rounds = RoundManager.load_all_rounds_object()
        self.chosen_tournament = None

    def show_player_list(self):
        # Show the sorted player list via the view
        sorted_players = sorted(
            self.players.values(),
            key=lambda player: player.first_name + player.last_name,
        )
        PlayerView.show_players_list(sorted_players)

    def show_tournament_list(self):
        TournamentView.show_tournaments_list(list(self.tournaments.values()))

    def choose_tournament(self):
        choice = TournamentManagerView.choose_tournament(
            list(self.tournaments.values())
        )
        self.chosen_tournament = choice

    def show_rounds_and_matches_in_chosen_tournament(self):
        if not self.chosen_tournament:
            UtilitiesMessageView.display_warning_message(
                "Choose a tournament first"
            )
            return
        ReportView.show_rounds_and_matches(self.chosen_tournament)

    def show_player_list_in_chosen_tournament(self):
        if not self.chosen_tournament:
            UtilitiesMessageView.display_warning_message(
                "Choose a tournament first"
            )
            return
        ReportView.show_players_in_tournament(self.chosen_tournament)

    def report_menu(self):
        while True:
            choice = ReportView.report_menu()
            match choice:
                case "1":
                    self.show_player_list()
                case "2":
                    ReportView.show_all_tournaments(self.tournaments)
                case "3":
                    self.choose_tournament()
                case "4":
                    self.show_player_list_in_chosen_tournament()
                case "5":
                    self.show_rounds_and_matches_in_chosen_tournament()
                case "6":
                    break
                case _:
                    UtilitiesMessageView.display_error_message(
                        "Invalid choice"
                    )
