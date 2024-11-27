from utils.utilities import get_valid_date


class TournamentView:
    @staticmethod
    def show_tournament_menu():
        print("What would you like to do?")
        print("1. Add tournament")
        print("2. Show tournament list")
        print("3. Tournament manager")
        print("4. Back to main menu")
        return input("Enter your choice: ")

    @staticmethod
    def show_tournaments_list(tournaments):
        if not tournaments:
            print("No tournaments found")
            return

        for tournament in tournaments:
            print(f"{tournament.name} - {tournament.location} - {tournament.start_date} - {tournament.end_date}")

    @staticmethod
    def get_tournament_details():
        name = input("Enter tournament name: ")
        location = input("Enter tournament location: ")

        # Use the helper function to get and validate dates
        start_date = get_valid_date("Enter tournament start date (dd/mm/yyyy): ")
        while True:
            end_date = get_valid_date("Enter tournament end date (dd/mm/yyyy): ")
            if end_date > start_date:
                break
            print("End date must be later than the start date. Please try again.")

        description = input("Enter tournament description: ")
        return {
            "name": name,
            "location": location,
            "start_date": start_date.strftime("%d/%m/%Y"),
            "end_date": end_date.strftime("%d/%m/%Y"),
            "description": description,
        }