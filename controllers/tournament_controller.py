from models.managers.tournament_manager import TournamentManager
from controllers.tournament_manager_controller import (
    TournamentManagerController,
)
from views.tournament_view import TournamentView
from views.utilities_message_view import UtilitiesMessageView


class TournamentController:
    def __init__(self):
        self.tournaments = TournamentManager.load_all_tournaments_object()

    def add_tournament(self):
        details = TournamentView.get_tournament_details()
        tournament = TournamentManager.create_tournament(details)
        self.tournaments[tournament.id] = tournament
        TournamentManager.save_tournaments(tournament)

    def show_tournament_menu(self):
        while True:
            choice = TournamentView.show_tournament_menu()

            match choice:
                case "1":
                    self.add_tournament()
                case "2":
                    TournamentView.show_tournaments_list(
                        list(self.tournaments.values())
                    )
                case "3":
                    if not self.tournaments:
                        UtilitiesMessageView.display_warning_message(
                            "Cannot manage tournaments: No tournaments found"
                        )
                    else:
                        tournament_manager = TournamentManagerController(
                            self.tournaments
                        )
                        tournament_manager.show_tournament_manager_menu()
                case "4":
                    break
                case _:
                    UtilitiesMessageView.display_error_message(
                        "Invalid choice"
                    )
