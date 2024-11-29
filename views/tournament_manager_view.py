from utils.utilities import get_valid_date


class TournamentManagerView:
    @staticmethod
    def show_tournament_manager_menu():
        print("What would you like to do?")
        print("1. Modify specific details")
        print("2. Start new round")
        print("3. View tournament details")
        print("4. View players in the tournament")
        print("5. Add player to tournament")
        print("6. End round")
        print("7. Save and quit")
        return input("Enter your choice: ")

    @staticmethod
    def choose_tournament(tournaments):
        if not tournaments:
            print("No tournaments found")
            return
        print("Choose a tournament \n\n")
        print("Tournaments: \n")

        for index, tournament in enumerate(tournaments, start=1):
            print(
                f"{index}. {tournament.name} - {tournament.location} "
                f"({tournament.start_date} - {tournament.end_date})"
            )

        choice = input("Enter the number of the tournament: ")
        if (
                not choice.isdigit()
                or int(choice) < 1
                or int(choice) > len(tournaments)
        ):
            print("Please enter a valid number")
            return None
        return tournaments[int(choice) - 1]

    @staticmethod
    def get_user_choice():
        return input("Enter your choice: ")

    @staticmethod
    def display_tournament_details(tournament):
        print(f"Name: {tournament.name}")
        print(f"Location: {tournament.location}")
        print(f"Start date: {tournament.start_date}")
        print(f"End date: {tournament.end_date}")
        print(f"Number of total rounds: {tournament.number_rounds}")
        round_name = tournament.current_round if tournament.has_begun \
            else 'Tournament has not yet begun'
        print(f"Current round: {round_name}")
        if tournament.players_scores:
            print("Current player ranking:")
            for chess_id, score in sorted(tournament.players_scores.items(),
                                          key=lambda x: x[1], reverse=True):
                for player in tournament.players:
                    if player.chess_id == chess_id:
                        print(f"{player.first_name} {player.last_name}"
                              f" current score: {score}")

        print(f"Description: {tournament.description}")
        if tournament.players:
            TournamentManagerView.display_players(tournament.players)
        else:
            print("No players found")

    @staticmethod
    def change_tournament_details_menu(tournament):
        TournamentManagerView.display_tournament_details(tournament)

        print("What would you like to change?")
        print("1. Name")
        print("2. Location")
        print("3. Start date")
        print("4. End date")
        print("5. Number of rounds")
        print("6. Description")
        print("7. Back to main menu")

    @staticmethod
    def display_rounds(tournament):
        if not tournament.rounds:
            print("No rounds found")
            return
        print("Rounds: \n")
        for round_instance in tournament.rounds:
            print(f"Round: {round_instance.name}")
            for match in round_instance.matches:
                print(f"Match: {match}")

    @staticmethod
    def display_players(tournament_players):
        if not tournament_players:
            print("No players found")
            return
        print("Players:")
        for player in tournament_players:
            print(
                f"{player.first_name} {player.last_name} ID: {player.chess_id}"
            )

    @staticmethod
    def set_match_result(player1, player2):
        print(f"Who won between {player1.first_name} and {player2.first_name}")
        result = input(f"Type 1 for: {player1.first_name} \n"
                       f"Type 2 for: {player2.first_name} \n"
                       f"Type 3 for draw: ")
        return result

    @staticmethod
    def get_player_id():
        return input("Enter player ID: ")

    @staticmethod
    def get_first_name():
        return input("Enter first name: ")

    @staticmethod
    def get_last_name():
        return input("Enter last name: ")

    @staticmethod
    def get_birth_date():
        return input("Enter birth date: ")

    @staticmethod
    def get_new_tournament_name(current_name):
        print(f"Name: {current_name}")
        return input("Enter the new tournament name: ")

    @staticmethod
    def get_new_tournament_location(current_location):
        print(f"Location: {current_location}")
        return input("Enter the new tournament location: ")

    @staticmethod
    def get_new_tournament_start_date(current_start_date, end_date):
        print(f"Start date: {current_start_date} - End date: {end_date}")
        while True:
            new_start_date = (
                get_valid_date(
                    "Enter the new tournament start date (dd/mm/yyyy): "
                )
            ).strftime("%d/%m/%Y")
            if new_start_date < end_date:
                break
            print("Start date must be before the end date. Please try again.")
        return new_start_date

    @staticmethod
    def get_new_tournament_end_date(current_end_date, start_date):
        print(f"Start date: {start_date} - End date: {current_end_date}")
        while True:
            new_end_date = (
                get_valid_date(
                    "Enter the new tournament end date (dd/mm/yyyy): "
                )
            ).strftime("%d/%m/%Y")
            if new_end_date > start_date:
                break
            print("End date must be after the start date. Please try again.")
        return new_end_date

    @staticmethod
    def get_new_number_of_rounds(current_number_of_rounds):
        print(f"Current number of rounds: {current_number_of_rounds}")
        return input("Enter the new number of rounds: ")

    @staticmethod
    def get_new_tournament_description(current_description):
        print(f"Current description:\n {current_description}")
        return input("Enter the new tournament description: ")
