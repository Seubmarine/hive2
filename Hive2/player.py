class Player():
    def __init__(self, starting_position):
        self.location_x, self.location_y = starting_position
        self.victory = False
        self.hp = 3
        #Health Point or number of survivalble turn the player can take
        self.upgrade = None
        #State of the character to have the legs or arms upgrade: None == Nothing, False == Legs, True == Arms

    #Vérifie si vivant
    def is_alive(self):
        return self.hp > 0

    #How to move
    def move(self, dx, dy):
        self.location_x += dx
        self.location_y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    #faire une action
    def do_action(self, action, **kwargs):
        action_method = getattr(self, action.method.__name__)
        if action_method:
            action_method(**kwargs)

    def active_victory(self):
        self.victory = True

    # def upgrade_arms(self):
    #     self.upgrade = True

    # def upgrade_legs(self):
    #     self.upgrade = False