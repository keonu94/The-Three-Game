# Author: Joshua White
# Date: 12/02/2021
# Description: Program is a game that allows two players to select
# up to three numbers each, alternatively. The numbers have to be 0-9,
# and if at any point the sum of a players numbers equal 15, that player wins

class TheThreeGame:
    """TheThreeGame class represents TheThreeGame which stores the moves made by
    two players and checks/updates the status of the game during each move.
    If the move is not valid, it returns False."""
    def __init__(self):
        """Takes no parameters and initializes player moves, game status, and which
         player's turn it is. All data members are private"""
        self._game_status = "GAME_UNFINISHED"
        self._1_player = []
        self._2_player = []
        self._player_turn = 0

    def get_winner(self):
        """Takes no Parameters and Returns the winner if there is one, and None otherwise"""
        if self._game_status == "FIRST_PLAYER_WON" or "SECOND_PLAYER_WON":
            return self._game_status
        else:
            return None

    def is_it_a_draw(self):
        """Takes no parameters and Returns IT_IS_A_DRAW if there isn't a winner
        and both players have finished playing. Also returns the winner, if
        there is a winner or GAME_UNFINISHED otherwise"""
        if self._game_status != "GAME_UNFINISHED":
            return self._game_status
        else:
            return self._game_status

    def make_move(self, player, num):
        """Takes two parameters:
        player - Represents which player is making a move
        num - Represents which number the player selected
        Returns and stores valid moves made by each player,
        and False otherwise, while also checking/updating the
        game's status each turn"""
        if 1 <= num < 10:
            if self._game_status == "GAME_UNFINISHED":
                if player == "first_player" and self._player_turn % 2 == 0 and num not in self._2_player:
                    if num not in self._1_player and self._player_turn < 7:
                        self._player_turn += 1
                        self._1_player.append(num)
                        if sum(self._1_player) == 15:
                            self._game_status = "FIRST_PLAYER_WON"
                        return True
                    else:
                        return False
                elif player == "second_player" and self._player_turn % 2 == 1 and num not in self._1_player:
                    if num not in self._2_player and self._player_turn < 7:
                        self._player_turn += 1
                        self._2_player.append(num)
                        if sum(self._2_player) == 15:
                            self._game_status = "SECOND_PLAYER_WON"
                        elif len(self._1_player) + len(self._2_player) == 6:
                            self._game_status = "IT_IS_A_DRAW"
                        return True
                else:
                    return False
        else:
            return False


