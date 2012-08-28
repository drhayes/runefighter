# Copyright (c) 2012 David Hayes

"""All the game states, including main menu and shooting at things."""

import pyglet


class StateManager(object):
  """Tracks current state and updates periodically."""
  def __init__(self, window, states, starfield):
    self.window = window
    self.states = states
    self.starfield = starfield
    self.current_state = None

  def on_draw(self):
    self.window.clear()
    self.starfield.draw()

    if self.current_state:
      self.current_state.draw()

  def on_key_press(self, symbol, modifiers):
    if self.current_state:
      self.current_state.on_key_press(symbol, modifiers)


class State(object):
  """Game state that handles drawing, key presses, etc."""
  def on_draw(self):
        pass

  def on_key_press(self, symbol, modifiers):
        pass


class TitleScreen(State):
  """Show the title screen until player presses spacebar."""
  def __init__(self, title):
    self.title = title

  def draw(self):
    self.title.draw()


class ShootingAtThings(State):
  """State of player controlling ship and shooting things."""
  def __init__(self, ship):
    self.ship = ship

  def draw(self):
    self.ship.draw()
