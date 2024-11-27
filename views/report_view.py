class ReportView:

    @staticmethod
    def show_all_tournaments(tournaments):
        if not tournaments:
            print("No tournaments found")
            return
        print("\nList of all tournaments:\n")
        for tournament_id, tournament in tournaments.items():
            print(f"{tournament.name} - {tournament.location} - {tournament.start_date} - {tournament.end_date}")

    @staticmethod
    def show_players_in_tournament(tournament):
        if not tournament.players:
            print("No players found")
            return

        sorted_players = sorted(tournament.players, key=lambda player_: player_.first_name + player_.last_name)
        print("\nList of tournament players in alphabetical order:\n")
        for player in sorted_players:
            print(f"{player.first_name} {player.last_name} ID: {player.chess_id}")

    @staticmethod
    def show_rounds_and_matches(tournament):
        if not tournament.rounds:
            print("No rounds found")
            return
        print("\nRounds:")
        for round_instance in tournament.rounds:
            print(f"\n{round_instance.name}")
            for match in round_instance.matches:
                print(f"Match: {match.match_result[0][0].first_name} {match.match_result[0][0].last_name}"
                      f" score {match.match_result[0][1]} - {match.match_result[1][0].first_name} "
                      f"{match.match_result[1][0].last_name} score {match.match_result[1][1]}")

    @staticmethod
    def report_menu():
        print("\nReport Menu:\n")
        print("What would you like to do?")
        print("1. List of all players in alphabetical order")
        print("2. List of all tournaments")
        print("3. Choose tournament")
        print("4. List of tournament players in alphabetical order")
        print("5. List of all tournament rounds and all round matches")
        print("6. Back to main menu")
        return input("Enter your choice: ")