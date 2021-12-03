#!/bin/sh

# take screenshot
# you have to click the window or drag and draw the region to snap
# Key([mod, "shift"], "x", lazy.spawn("/home/deewakar/xshot.sh")),

import -window "$(xdotool getwindowfocus -f)" ~/screenshot.png
