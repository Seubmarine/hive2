import tiles

world_dsl = """
|  |  |  |LE|  |
|  |FG|EM|GS|  |
|  |  |EM|  |  |
|  |  |EM|  |  |
|GS|EM|ST|EM|FD|
|  |  |FG|  |  |
|  |  |OG|  |  |
"""


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

tile_type_dict = {"LE": tiles.LeaveCaveRoom,
                  "ST": tiles.StartingRoom,
                  "EM": tiles.EmptyCavePath,
                  "GS": tiles.GiantSpiderRoom,
                  "OG": tiles.OgreRoom,
                  "FG": tiles.Find5GoldRoom,
                  "FD": tiles.FindDaggerRoom,
                  "  ": None}


world_map = []
starting_position = (0, 0)


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


def tile_exists(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None