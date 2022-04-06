from project1i.player import Player

class Guild:

    def __init__(self, name):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        self.players.append(player)
        player.guild = self.name
        return f'Welcome player {player} to the guild {self.name}'

    def kick_player(self, player_name: str):
        if player_name in self.players:
            self.players.remove(player_name)
            Player.guild =  "Unaffiliated"
            return
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):

        return f"Guild: {self.name}\n"

