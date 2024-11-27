from controllers.report_controller import ReportController
from views.main_view import MainView
from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController


class MainController:
    @staticmethod
    def show_main_menu():
        while True:
            MainView.show_main_menu()
            choice = MainView.get_user_choice()

            match choice:
                case "1":
                    player_controller = PlayerController()
                    player_controller.show_player_menu()
                case "2":
                    tournament_controller = TournamentController()
                    tournament_controller.show_tournament_menu()
                case "3":
                    report_controller = ReportController()
                    report_controller.report_menu()
                case "4":
                    break


