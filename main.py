# Copyright (c) 2012 David Hayes

"""Main file for my shoot-em-up game using pyglet."""

import pyglet
from pyglet.gl import *


import constants
import process
import states


def load_image(filename):
  image_file = pyglet.resource.file(filename)
  image = pyglet.image.load(filename, file=image_file)
  image.anchor_x = image.width / 2
  image.anchor_y = image.height / 2
  return image


# Kicks everything off.
def main():
  # The window where all the drawing takes place.
  window = pyglet.window.Window(width=constants.SCREEN_WIDTH,
    height=constants.SCREEN_HEIGHT)
  window.set_caption('Runefighter')

  # Set the resource load path.
  pyglet.resource.path = ['res/images', 'res/fonts']
  pyglet.resource.reindex()

  # Load images.
  title_image = load_image('title.png')
  starfield_image = load_image('stars.png')
  starfield_image.anchor_x = starfield_image.anchor_y = 0
  ship_image = load_image('ship.png')

  # Load fonts.
  pyglet.resource.add_font('m48.ttf')
  main_font = pyglet.font.load(constants.FONT_NAME, 32)

  # Load sprites.
  ship = pyglet.sprite.Sprite(ship_image, x=50, y=50)

  # Processes.
  title = process.TitleGraphic(title_image)
  title.start()
  starfield = process.Starfield(starfield_image)
  starfield.start()

  # State manager and states.
  state_manager = states.StateManager(window, starfield)

  shooting_at_things = states.ShootingAtThings(ship)
  transition_to_shooting = state_manager.create_transition(shooting_at_things)
  title_screen = states.TitleScreen(title, transition_to_shooting)

  state_manager.current_state = title_screen

  # Make the StateManager instance responsible for drawing things.
  window.push_handlers(state_manager)

  pyglet.app.run()


if __name__ == '__main__':
  main()
