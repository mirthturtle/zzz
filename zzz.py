import evdev
from evdev import InputDevice, ecodes
from pygame import mixer

print("Initializing...")
mixer.init()
ready_sound   = mixer.Sound("sound/piano.mp3")
trigger_sound = mixer.Sound("sound/sonar.mp3")
left_sound    = mixer.Sound("sound/pop.mp3")
right_sound   = mixer.Sound("sound/ding.mp3")

mouse = InputDevice('/dev/input/event0') # or event1, etc. if other devices are present

print("Ready! Listening for input...")
ready_sound.play()

for event in mouse.read_loop():
    if event.type == ecodes.EV_KEY:
        if event.code == ecodes.BTN_LEFT and event.value == 1:
            trigger_sound.play()
            print("Trigger clicked!")
        elif event.code == ecodes.BTN_RIGHT and event.value == 1:
            right_sound.play()
            print("Right button clicked!")
        elif event.code == ecodes.BTN_MIDDLE and event.value == 1:
            left_sound.play()
            print("Left button clicked!")
