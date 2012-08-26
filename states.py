"""All the game states, including main menu and shooting at things."""


class CurrentState(object):
  """Tracks current state and updates periodically."""
  def __init__(self, window, states):
    self.window = window
    self.states = states
    self.current_state = None

  def on_draw(self):
    if self.current_state:
      self.current_state.draw()


class ShootingAtThings(object):
  """State of player controlling ship and shooting things."""

  def draw(self):
    pass
