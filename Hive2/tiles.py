import random
import world, actions
# from actions import Quit

class MapTile:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError()
    
    def modify_player(self, player):
        raise NotImplementedError()

    def adjacent_moves(self):
        """Returns all move actions for adjacent tiles."""
        moves = []
        if world.tile_at(self.x + 1, self.y):
            moves.append(actions.MoveEast())
        if world.tile_at(self.x - 1, self.y):
            moves.append(actions.MoveWest())
        if world.tile_at(self.x, self.y - 1):
            moves.append(actions.MoveNorth())
        if world.tile_at(self.x, self.y + 1):
            moves.append(actions.MoveSouth())
        return moves

    def available_actions(self):

        available_actions = self.adjacent_moves()
        available_actions.append(actions.Quit())
        return available_actions


class NeutralTile(MapTile):
    # For dev only
    def intro_text(self, player):
        return """
        Rien de spécial ici...
        Coord. : x{} y{}
        """.format(self.x, self.y)

    def modify_player(self, player):
        pass


class TwoChoicesTile(MapTile):
    #Ancienne Tile
    def intro_text(self, player):
        if player.upgrade == False: 
            return """Vous utilisé vos Jambe ! """

        if player.upgrade == True: 
            return """Vous utilisé vos Bras ! """

        if player.upgrade == None:
            return """Vous ne passerez pas ! """

    def modify_player(self, player):
        pass


class StartingTile(MapTile):
    def intro_text(self, player):
        return """
        Bienvenue
        """

    def modify_player(self, player):
        pass


class LeavingTile(MapTile):
    def intro_text(self, player):
        return """
        GoodBye
        """

    def modify_player(self, player):
        player.victory = True


class UpgradeTile(MapTile):
    #Choix entre les bras ou les jambes.

    def intro_text(self, player):
        return"""UpgradeTile"""

    def modify_player(self, player):
        choix = input("""Choix:""")
        if choix == 'a' :
            player.upgrade = True
        elif choix == 'b' :
            player.upgrade = False
        print(player.upgrade)


class SasTile(MapTile):
    def intro_text(self, player):
        return"""SasTile"""
    def modify_player(self, player):
        pass


class LobbyTile1(MapTile):
    def intro_text(self, player):
        return"""LobbyTile"""
    def modify_player(self, player):
        pass


class LobbyTile2(MapTile):
    def intro_text(self, player):
        return"""LobbyTile2"""
    def modify_player(self, player):
        pass


class LobbyTile3(MapTile):
    def intro_text(self, player):
        return"""LobbyTile3"""
    def modify_player(self, player):
        pass


class ReactorTile(MapTile):
    def intro_text(self, player):
        return """ReactorRoom"""
    def modify_player(self, player):
        pass


class HabitationTile1(MapTile):
    def intro_text(self, player):
        return """HabitationRoom1"""
    def modify_player(self, player):
        pass


class HabitationTile2(MapTile):
    def intro_text(self, player):
        return """HabitationRoom2"""
    def modify_player(self, player):
        pass


class HabitationTile3(MapTile):
    def intro_text(self, player):
        return """HabitationRoom3"""
    def modify_player(self, player):
        pass


class HabitationTile4(MapTile):
    def intro_text(self, player):
        return """HabitationRoom4"""
    def modify_player(self, player):
        pass


class ArtificialIntelligenceTile(MapTile):
    def intro_text(self, player):
        return """ArtificialIntelligenceTile"""
    def modify_player(self, player):
        pass


class LifeSupportTile(MapTile):
    def intro_text(self, player):
        return """LifeSupportTile"""
    def modify_player(self, player):
        pass


class ControlRoomTile(MapTile):
    def intro_text(self, player):
        return """La salle de control"""
    def modify_player(self, player):
        pass


class LongCorridorTile(MapTile):
    def intro_text(self, player):
        return """LongCorridorTile"""
    def modify_player(self, player):
        pass

class NPCTile(MapTile):
    def intro_text():
        return 'first text of Non Player Character'
    def modify_player(self, player):
        pass