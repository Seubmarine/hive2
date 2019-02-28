import world
from player import Player

intro_text = """5.. 4.. 3.. 2.. 1.. BIIIIP..

Furent les premiers mots que j'entendu a mon réveil. Une lumiere blanche m'aveugler.
Je caché mes yeux avec ma main et commenca a scruté les environs en quête de réponses.


"""

def play():

    world.parse_world_dsl() # load tiles
    player = Player(world.starting_position)

    #These lines load the starting room and display the text
    room = world.tile_at(player.location_x, player.location_y)
    print(intro_text)

    while player.is_alive() and not player.victory:
        #Loop begins here
        room = world.tile_at(player.location_x, player.location_y)
        # import ipdb; ipdb.set_trace()
        room.modify_player(player)

        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            
            print(room.intro_text(player))
            print("Choose an action:\n")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ')
            for action in available_actions:
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    break

if __name__ == "__main__":
    play()
