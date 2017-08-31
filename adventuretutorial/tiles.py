import items
import enemies


class MapTile():
    def __init__(self):
        self.x = x
        self.y = y

    def intro_text(self):
        raise NotImplementedError

    def modify_player(self):
        # this is so if a subclass forgets to define modify player it will raise an error
        raise NotImplementedError


class StartingRoom(MapTile):
    def intro_text(self):
        return '''
        You find yourself in a cave with flickering lights. You can make out 4 paths
        '''

    def modify_player(self, player):
        # Room action has no impact on player
        pass


class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)


class EnemyRoom(MapTile):

    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super().__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy_damage
            print('Enemy does {} damage. You have {} damage remaining.'.format(self.enemy.damage, the_player.hp))


class EmptyCavePath(MapTile):

    def intro_text(self):
        return '''
        Another unremarkable part of the cave. You must continute onwards.
        '''

    def modify_player(self, player):
        # Room has no action
        pass


class GiantSpiderRoom(EnemyRoom):
    def __init__(self, x, y):
        super().__init__(x, y, enemies.GiantSpider())

    def intro_text(self):
        if self.enemy.is_alive():
            return '''
            A giant spider jumps down from its web in front of you!
            '''
        else:
            return '''
            The corpse of the dead spider rots on the ground
            '''


class FindDaggerRoom(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Dagger())

    def intro_text(self):
        return '''
        You notice something shiny in the corner.
        It's a dagger! You pick it up.
        '''
