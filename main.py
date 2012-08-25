# A shoot-em-up game in pyglet, to learn the library.

import pyglet
from pyglet.gl import *


WIDTH = 640
HEIGHT = 480


background_image = None


def load_image(filename):
  image_file = pyglet.resource.file(filename)
  image = pyglet.image.load(filename, file=image_file)
  image.anchor_x = image.width / 2
  image.anchor_y = image.height / 2
  return image


# Initialize window globally so we can use the short form
# of event handler signup.
window = pyglet.window.Window(width=WIDTH, height=HEIGHT)


# The main update loop.
@window.event
def on_draw():
  window.clear()
  background_image.blit(WIDTH / 2, HEIGHT / 2)


# Kicks everything off.
def main():
  global background_image
  # Set the resource load path.
  pyglet.resource.path = ['res/images']
  pyglet.resource.reindex()

  # Load images.
  background_image = load_image('stars.png')

  pyglet.app.run()


if __name__ == '__main__':
  main()
