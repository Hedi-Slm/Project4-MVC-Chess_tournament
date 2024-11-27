from models.managers.player_manager import PlayerManager
from utils.utilities import check_chess_id_format
from views.player_view import PlayerView


class PlayerController:
    def __init__(self):
        # Load players using PlayerManager
        self.players = PlayerManager.load_all_players_object()

    def add_player(self):
        # Get player details from the view
        player_id = PlayerView.get_player_id()

        # Check if the chess ID is valid and if it's not already in the database
        if not check_chess_id_format(player_id):
            print("Invalid chess ID format.")
            return

        if player_id in self.players:
            print("Chess ID already exists in the database.")
            return

        player_data = PlayerView.get_player_details(player_id)

        # Create a new player and add it
        player = PlayerManager.create_player(player_data)
        self.players[player_id] = player

        PlayerManager.save_players(self.players)
        print("Player added successfully.")

    def show_player_list(self):
        # Show the sorted player list via the view
        sorted_players = sorted(self.players.values(), key=lambda player: player.first_name+player.last_name)
        PlayerView.show_players_list(sorted_players)

    def show_player_menu(self):
        while True:
            # Show the menu and handle the user's choice
            choice = PlayerView.show_player_menu()

            match choice:
                case "1":
                    self.add_player()
                case "2":
                    self.show_player_list()
                case "3":
                    print("Returning to main menu.")
                    break
                case _:
                    print("Invalid choice. Please try again.")
