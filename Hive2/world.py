import tiles

# #world_dsl = """
# |  |  |  |  |NE|  |NE|  |  |
# |  |NE|NE|  |NE|NE|NE|NE|  |
# |  |  |NE|  |NE|  |  |  |  |
# |NE|NE|NE|NE|NE|NE|NE|NE|NE|
# |  |NE|  |  |NE|  |NE|  |  |
# |NE|NE|ST|  |NE|  |NE|  |  |
# |  |LE|  |NE|NE|NE|  |  |  |
# """

world_dsl = """
|  |  |  |  |AI|  |LE|  |  |
|  |RE|NE|  |SS|NE|NE|ST|  |
|  |  |LC|  |NE|  |  |  |  |
|H1|NE|L3|NE|L2|SS|L1|SS|CR|
|  |SS|  |  |NE|  |NE|  |  |
|H2|NE|H4|  |NE|  |LS|  |  |
|  |H3|  |NE|NE|NE|  |  |  |
"""

#L1 LOBBY 1, L2 LOBBY 2, L3 LOBBY 3
#IA IA ROOM
#H1 H2 H3 H4 HABITATION ROOM
#LS LIFE SUPPORT ROOM
#RE REACTOR ROOM
#SS SAS
#EV EVENT ROOM


tile_type_dict = {"LE": tiles.LeavingTile,
                  "ST": tiles.StartingTile,
                  "NE": tiles.NeutralTile,
                  "UT": tiles.UpgradeTile,
                  "TC": tiles.TwoChoicesTile,
                  "SS": tiles.SasTile,
                  "L1": tiles.LobbyTile1,
                  "L2": tiles.LobbyTile2,
                  "L3": tiles.LobbyTile3,
                  "RE": tiles.ReactorTile,
                  "H1": tiles.HabitationTile1,
                  "H2": tiles.HabitationTile2,
                  "H3": tiles.HabitationTile3,
                  "H4": tiles.HabitationTile4,
                  "AI": tiles.ArtificialIntelligenceTile,
                  "LS": tiles.LifeSupportTile,
                  "CR": tiles.ControlRoomTile,
                  "LC": tiles.LongCorridorTile,
                  "  ": None}


world_map = []
starting_position = (0, 0)

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|LE|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True


def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            row.append(tile_type(x, y) if tile_type else None)
            if dsl_cell == 'ST':
                global starting_position
                starting_position = (x, y)

        world_map.append(row)


def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None