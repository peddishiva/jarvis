import pygame

import eel

# Playing assistant sound function

@eel.expose
def playAssistantSound():
    pygame.mixer.init()
    pygame.mixer.music.load("www\\assets\\audio\\start_sound.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)