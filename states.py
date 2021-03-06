# Copyright (c) 2012 David Hayes

"""All the game states, including main menu and shooting at things."""

from datetime import datetime
from pyglet.window import key


import constants


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
      return self.current_state.on_draw()
    return False

  def on_key_press(self, symbol, modifiers):
    if self.current_state:
      return self.current_state.on_key_press(symbol, modifiers)
    return False

  def create_transition(self, new_state):
    def transition():
      if self.current_state:
        self.current_state.deactivate()
      self.current_state = new_state
      self.current_state.activate()
    return transition


class State(object):
  """Game state that handles drawing, key presses, etc."""
  def activate(self):
    """Called when state is transitioned to."""
    pass

  def deactivate(self):
    """Called when state is transitioned out of."""
    pass

  def on_draw(self):
    """Called to draw on the screen when this state is activated."""
    pass

  def on_key_press(self, symbol, modifiers):
    """Called when a key is pressed when this state is activated."""
    pass


class TitleScreen(State):
  """Show the title screen until player presses spacebar."""
  def __init__(self, title, res_man, transition):
    super(TitleScreen, self).__init__()
    self.title = title
    self.press_space = res_man.press_space
    self.transition = transition

  def on_draw(self):
    self.title.draw()
    self.press_space.draw()

  def on_key_press(self, symbol, modifiers):
    if symbol == key.SPACE:
      self.transition()
      return True


class PlayerStatState(State):
  """State where player stats are displayed."""
  def __init__(self, player, res_man):
    super(PlayerStatState, self).__init__()
    self.player = player
    self.res_man = res_man
    self.ship_image = res_man.ship
    self.score_label = res_man.score
    self.current_score = player.score
    self.numeric_score_label = None

  def on_draw(self):
    if self.need_to_update_numeric_score_label():
      self.update_numeric_score()
    self.score_label.draw()
    self.numeric_score_label.draw()
    # Draw the number of lives at the bottom.
    for i in xrange(0, self.player.lives - 1):
      x = (constants.LIVES_IMAGE_WIDTH + 10) + (i * (constants.LIVES_IMAGE_WIDTH + 8))
      self.ship_image.blit(
        x, 20, width=constants.LIVES_IMAGE_WIDTH, height=constants.LIVES_IMAGE_HEIGHT)

  def need_to_update_numeric_score_label(self):
    return self.current_score != self.player.score or self.numeric_score_label is None

  def update_numeric_score(self):
    if self.numeric_score_label:
      self.numeric_score_label.delete()
    self.numeric_score_label = self.res_man.create_label('numeric_score',
      str(self.player.score),
      x=constants.NUMERIC_SCORE_X_POS,
      y=constants.NUMERIC_SCORE_Y_POS)
    self.numeric_score_label.anchor_x = 'left'


class GetReady(PlayerStatState):
  """Show the text get ready and transition in a few seconds."""
  def __init__(self, player, res_man, transition):
    super(GetReady, self).__init__(player, res_man)
    self.get_ready = res_man.get_ready
    self.transition = transition

  def activate(self):
    self.start = datetime.now()

  def on_draw(self):
    super(GetReady, self).on_draw()
    self.get_ready.draw()
    if datetime.now() - self.start > constants.READY_TIME_DELTA:
      self.transition()


class ShootingAtThings(PlayerStatState):
  """State of player controlling ship and shooting things."""
  def __init__(self, player, res_man, ship):
    super(ShootingAtThings, self).__init__(player, res_man)
    self.ship = ship

  def on_draw(self):
    super(ShootingAtThings, self).on_draw()
    self.ship.draw()
