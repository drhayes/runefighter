# Copyright (c) 2012 David Hayes

"""All the game states, including main menu and shooting at things."""

from pyglet.window import key


class StateManager(object):
  """Tracks current state and updates periodically."""
  def __init__(self, window, starfield):
    self.window = window
    self.starfield = starfield
    self.current_state = None

  def on_draw(self):
    self.window.clear()
    self.starfield.draw()

    if self.current_state:
      return self.current_state.draw()
    return False

  def on_key_press(self, symbol, modifiers):
    if self.current_state:
      return self.current_state.on_key_press(symbol, modifiers)
    return False

  def create_transition(self, new_state):
    def transition():
      self.current_state = new_state
    return transition


class State(object):
  """Game state that handles drawing, key presses, etc."""
  def on_draw(self):
        pass

  def on_key_press(self, symbol, modifiers):
        pass


class TitleScreen(State):
  """Show the title screen until player presses spacebar."""
  def __init__(self, title, press_space, transition):
    super(TitleScreen, self).__init__()
    self.title = title
    self.press_space = press_space
    self.transition = transition

  def draw(self):
    self.title.draw()
    self.press_space.draw()

  def on_key_press(self, symbol, modifiers):
    if symbol == key.SPACE:
      self.transition()
      return True


class ShootingAtThings(State):
  """State of player controlling ship and shooting things."""
  def __init__(self, ship):
    super(ShootingAtThings, self).__init__()
    self.ship = ship

  def draw(self):
    self.ship.draw()
