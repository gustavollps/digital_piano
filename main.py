from pynput.keyboard import Listener
from mingus.midi import fluidsynth

fluidsynth.init('SalC5Light2.sf2', "alsa")
scale = 3
starting_key = 12 * scale

def on_press(key):
    global scale
    global starting_key
    if hasattr(key, 'name'):
        if key.name == 'page_up':
            scale = scale + 1
        elif key.name == 'page_down':
            scale = scale - 1
        elif key.name == 'tab':
            fluidsynth.play_Note(starting_key -2, 0, 127)
        elif key.name == 'space':
            fluidsynth.stop_everything()
        if scale > 7:
            scale = 7
        if scale < 0:
            scale = 0
        starting_key = 12 * scale

    if hasattr(key, 'char'):
        if key.char == '1':
            fluidsynth.play_Note(starting_key + 1, 0, 127)
        elif key.char == 'q':
            fluidsynth.play_Note(starting_key + 0, 0, 127)
        elif key.char == '2':
            fluidsynth.play_Note(starting_key + 1, 0, 127)
        elif key.char == 'w':
            fluidsynth.play_Note(starting_key + 2, 0, 127)
        elif key.char == '3':
            fluidsynth.play_Note(starting_key + 3, 0, 127)
        elif key.char == 'e':
            fluidsynth.play_Note(starting_key + 4, 0, 127)
        elif key.char == 'r':
            fluidsynth.play_Note(starting_key + 5, 0, 127)  # FA
        elif key.char == '5':
            fluidsynth.play_Note(starting_key + 6, 0, 127)
        elif key.char == 't':
            fluidsynth.play_Note(starting_key + 7, 0, 127)
        elif key.char == '6':
            fluidsynth.play_Note(starting_key + 8, 0, 127)
        elif key.char == 'y':
            fluidsynth.play_Note(starting_key + 9, 0, 127)
        elif key.char == '7':
            fluidsynth.play_Note(starting_key + 10, 0, 127)
        elif key.char == 'u':
            fluidsynth.play_Note(starting_key + 11, 0, 127)  # SI
        elif key.char == 'i':
            fluidsynth.play_Note(starting_key + 12, 0, 127)  # DO 2
        elif key.char == '9':
            fluidsynth.play_Note(starting_key + 13, 0, 127)
        elif key.char == 'o':
            fluidsynth.play_Note(starting_key + 14, 0, 127)  # RE
        elif key.char == '0':
            fluidsynth.play_Note(starting_key + 15, 0, 127)
        elif key.char == 'p':
            fluidsynth.play_Note(starting_key + 16, 0, 127)  # MI
        elif key.char == '´':
            fluidsynth.play_Note(starting_key + 17, 0, 127)
        elif key.char == '=':
            fluidsynth.play_Note(starting_key + 18, 0, 127)
        elif key.char == '\\':
            fluidsynth.play_Note(starting_key + 19, 0, 127)  # SOL
        elif key.char == 'a':
            fluidsynth.play_Note(starting_key + 20, 0, 127)
        elif key.char == 'z':
            fluidsynth.play_Note(starting_key + 21, 0, 127)
        elif key.char == 's':
            fluidsynth.play_Note(starting_key + 22, 0, 127)
        elif key.char == 'x':
            fluidsynth.play_Note(starting_key + 23, 0, 127)
        elif key.char == 'c':
            fluidsynth.play_Note(starting_key + 24, 0, 127)  # DO 3
        elif key.char == 'f':
            fluidsynth.play_Note(starting_key + 25, 0, 127)
        elif key.char == 'v':
            fluidsynth.play_Note(starting_key + 26, 0, 127)
        elif key.char == 'g':
            fluidsynth.play_Note(starting_key + 27, 0, 127)
        elif key.char == 'b':
            fluidsynth.play_Note(starting_key + 28, 0, 127)
        elif key.char == 'n':
            fluidsynth.play_Note(starting_key + 29, 0, 127)
        elif key.char == 'j':
            fluidsynth.play_Note(starting_key + 30, 0, 127)
        elif key.char == 'm':
            fluidsynth.play_Note(starting_key + 31, 0, 127)
        elif key.char == 'k':
            fluidsynth.play_Note(starting_key + 32, 0, 127)
        elif key.char == ',':
            fluidsynth.play_Note(starting_key + 33, 0, 127)
        elif key.char == 'l':
            fluidsynth.play_Note(starting_key + 34, 0, 127)
        elif key.char == '.':
            fluidsynth.play_Note(starting_key + 35, 0, 127)  # SI
        elif key.char == ';':
            fluidsynth.play_Note(starting_key + 36, 0, 127)  # DO 4
        elif key.char == '~':
            fluidsynth.play_Note(starting_key + 37, 0, 127)
        elif key.char == '/':
            fluidsynth.play_Note(starting_key + 38, 0, 127)
        elif key.char == ']':
            fluidsynth.play_Note(starting_key + 39, 0, 127)


# Collect events until released
with Listener(on_press=on_press) as listener:
    listener.join()
