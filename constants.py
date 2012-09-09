"""Constants used throughout the game, centralized for easy editing."""

from datetime import timedelta

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FONT_NAME = 'M48_RETROFUTURE'
READY_TIME_DELTA = timedelta(0, 1)

RESOURCE_PATH = 'res'
IMAGE_PATH_FRAGMENT = 'images'
FONT_PATH_FRAGMENT = 'fonts'
# Assume all images are pngs and fonts are ttfs.
IMAGE_FILENAME_FORMAT = '%s.png'
FONT_FILENAME_FORMAT = '%s.ttf'

LIVES_IMAGE_WIDTH = 32
LIVES_IMAGE_HEIGHT = 32
