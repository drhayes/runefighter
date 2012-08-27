# Copyright (c) 2012 David Hayes

"""Time updateable processes."""


import math
from pyglet import clock


# pixels / second
TITLE_RATE = 20
START_TITLE_Y = 180
END_TITLE_Y = 300
# pixels / second
STARFIELD_RATE = 40


class Process(object):
  """Encapsulates a method called every so often in an update loop."""
  def __init__(self, frequency=0.01):
    self.frequency = frequency

  def start(self):
    clock.schedule_interval(self.update, self.frequency)

  def stop(self):
    clock.unschedule(self.update)

  def update(self, dt):
    pass


class TitleGraphic(Process):
  """A title that slides into place."""
  def __init__(self, title_image):
    super(TitleGraphic, self).__init__()
    self.title_image = title_image
    self.y = START_TITLE_Y

  def update(self, dt):
    if self.y < END_TITLE_Y:
      self.y += int(math.ceil(TITLE_RATE * dt))

  def draw(self):
    self.title_image.blit(320, self.y)


class Starfield(Process):
  """A scrolling starfield in the background."""
  def __init__(self, starfield_image, max_height):
    super(Starfield, self).__init__()
    self.starfield_image = starfield_image
    self.max_height = max_height
    self.y = 0

  def update(self, dt):
    self.y -= int(math.ceil(STARFIELD_RATE * dt))
    if self.y < -self.max_height:
      self.y = 0 + (self.max_height + self.y)

  def draw(self):
    self.starfield_image.blit(0, self.y)
    self.starfield_image.blit(0, self.y + self.max_height)
