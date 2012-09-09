# Copyright (c) 2012 David Hayes

"""Main file for my shoot-em-up game using pyglet."""

import pyglet
from pyglet.gl import *


import constants
import process
import resources
import states


class Player(object):
  """The one and only player."""
  def __init__(self, lives=3, score=0):
    self.lives = lives
    self.score = score


# Kicks everything off.
def main():
  # Instantiate the player.
  player = Player()

  # The window where all the drawing takes place.
  window = pyglet.window.Window(width=constants.SCREEN_WIDTH,
    height=constants.SCREEN_HEIGHT)
  window.set_caption('Runefighter')

  # Instantiate the resource manager.
  res_man = resources.ResourceManager(constants.RESOURCE_PATH)
  # Load the images.
  res_man.load_image('title')
  starfield_image = res_man.load_image('stars')
  starfield_image.anchor_x = starfield_image.anchor_y = 0
  res_man.load_image('ship')
  # Load fonts.
  res_man.load_font('m48')
  res_man.add_font('main_font', constants.FONT_NAME, 32)

  # Load sprites.
  ship = pyglet.sprite.Sprite(res_man.ship, x=50, y=70)

  # Get some text.
  res_man.create_label('press_space', 'Press Space To Continue',
    x=constants.SCREEN_WIDTH / 2, y=120)
  res_man.create_label('get_ready', 'Get Ready')
  score_label = res_man.create_label('score', 'Score',
    x=constants.SCORE_LABEL_X_POS,
    y=constants.SCORE_LABEL_Y_POS)
  score_label.anchor_x = 'left'
  score_label.anchor_y = 'top'

  # Processes.
  title = process.TitleGraphic(res_man)
  title.start()
  starfield = process.Starfield(res_man)
  starfield.start()

  # State manager and states.
  state_manager = states.StateManager(window, starfield)

  shooting_at_things = states.ShootingAtThings(player, res_man, ship)
  transition_to_shooting = state_manager.create_transition(shooting_at_things)
  get_ready = states.GetReady(player, res_man, transition_to_shooting)
  transition_to_ready = state_manager.create_transition(get_ready)
  title_screen = states.TitleScreen(title, res_man, transition_to_ready)
  transition_to_title_screen = state_manager.create_transition(title_screen)

  transition_to_title_screen()

  # Make the StateManager instance responsible for drawing things.
  window.push_handlers(state_manager)

  pyglet.app.run()


if __name__ == '__main__':
  main()
