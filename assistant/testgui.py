import os
command = "set volume to 50"
print(command[-1]+command[-2])
script = "osascript -e 'set volume output volume {}'".format(50)