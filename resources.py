# Copyright (c) 2012 David Hayes

"""Images and fonts and things."""

import os
import pyglet


import constants


def create_label(text, x=constants.SCREEN_WIDTH / 2,
    y=constants.SCREEN_HEIGHT / 2):
  return pyglet.text.Label(text, font_name=constants.FONT_NAME,
    anchor_x='center', x=x, y=y)


class ResourceManager(object):
  """Single point for loading images and things.

  Pass this object to other objects that require fonts and images
  and things instead of each individual font and image.

  This class mostly lets pyglet do the work, storing almost nothing."""
  def __init__(self, resource_path_stub):
    # Set pyglet's resource load path.
    image_path = os.path.join(resource_path_stub, constants.IMAGE_PATH_FRAGMENT)
    font_path = os.path.join(resource_path_stub, constants.FONT_PATH_FRAGMENT)
    pyglet.resource.path = [image_path, font_path]
    pyglet.resource.reindex()

  def load_image(self, image_name):
    """Load image and make available as attribute on class."""
    filename = constants.IMAGE_FILENAME_FORMAT % (image_name,)
    image_file = pyglet.resource.file(filename)
    image = pyglet.image.load(filename, file=image_file)
    image.anchor_x = image.width / 2
    image.anchor_y = image.height / 2
    self.__dict__[image_name] = image
    return image

  def load_font(self, font_name):
    filename = constants.FONT_FILENAME_FORMAT % (font_name,)
    pyglet.resource.add_font('m48.ttf')

  def add_font(self, font_name, font_system_name, font_size=12):
    font = pyglet.font.load(font_system_name, font_size)
    self.__dict__[font_name] = font

