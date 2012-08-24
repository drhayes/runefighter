import pyglet

WIDTH = 640
HEIGHT = 480

window = pyglet.window.Window(
  width=WIDTH, height=HEIGHT)

@window.event
def on_draw():
  window.clear()

pyglet.app.run()
