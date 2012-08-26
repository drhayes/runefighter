# Copyright (c) 2012 David Hayes

"""Main file for my shoot-em-up game using pyglet."""


import pyglet
from pyglet.gl import *


import process
import states


WIDTH = 640
HEIGHT = 480


def load_image(filename):
  image_file = pyglet.resource.file(filename)
  image = pyglet.image.load(filename, file=image_file)
  image.anchor_x = image.width / 2
  image.anchor_y = image.height / 2
  return image


# Kicks everything off.
def main():
  # The window where all the drawing takes place.
  window = pyglet.window.Window(width=WIDTH, height=HEIGHT)
  window.set_caption('Runefighter')

  # Set the resource load path.
  pyglet.resource.path = ['res/images', 'res/fonts']
  pyglet.resource.reindex()

  # Load images.
  background_image = load_image('stars.png')
  background_image.anchor_x = background_image.anchor_y = 0
  ship_image = load_image('ship.png')

  # Load fonts.
  pyglet.resource.add_font('m48.ttf')
  main_font = pyglet.font.load('M48_RETROFUTURE', 32)

  # Load sprites.
  ship = pyglet.sprite.Sprite(ship_image, x=50, y=50)

  # Processes.
  starfield = process.Starfield(background_image, HEIGHT)
  starfield.start()

  # Start state machine.
  shooting_at_things = states.ShootingAtThings(ship)
  game_states = [shooting_at_things]
  state_manager = states.StateManager(window, game_states, starfield)
  state_manager.current_state = game_states[0]
  # Make the StateManager instance responsible for drawing things.
  window.push_handlers(state_manager)

  pyglet.app.run()


if __name__ == '__main__':
  main()
