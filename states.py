# Copyright (c) 2012 David Hayes

"""All the game states, including main menu and shooting at things."""


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


class ShootingAtThings(object):
  """State of player controlling ship and shooting things."""
  def __init__(self, ship):
    self.ship = ship

  def draw(self):
    self.ship.draw()
