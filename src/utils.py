import pygame
import os

def load_image(file):
    file = os.path.join('assets', file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit(f'Could not load image "{file}" {pygame.get_error()}')
    return surface.convert_alpha()

def load_all_images():
    tile_type = []
    object_type = []
    agent_type = []

    # Load tile images
    tile_type.append(load_image('basic111x128/platformerTile_48_ret.png'))  # grass
    tile_type.append(load_image('ext/isometric-blocks/PNG/Platformer tiles/platformerTile_33.png'))  # brick
    tile_type.append(load_image('ext/isometric-blocks/PNG/Abstract tiles/abstractTile_12.png'))  # blue grass
    tile_type.append(load_image('ext/isometric-blocks/PNG/Abstract tiles/abstractTile_09.png'))  # grey brick

    # Load object images
    object_type.append(None)  # default -- never drawn
    object_type.append(load_image('basic111x128/tree_small_NW_ret.png'))  # normal tree
    object_type.append(load_image('basic111x128/blockHuge_N_ret.png'))  # construction block
    object_type.append(load_image('basic111x128/tree_small_NW_ret_red.png'))  # burning tree

    # Load agent images
    agent_type.append(None)  # default -- never drawn
    agent_type.append(load_image('basic111x128/invader_ret.png'))  # invader
    agent_type.append(load_image('basic111x128/ghost_pinky.png'))  # purple ghost
    agent_type.append(load_image('basic111x128/baby.png'))  # baby

    return tile_type, object_type, agent_type
