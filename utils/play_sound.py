import pygame

# takes sound file with extension as an argument then plays the corresponding sound
def play_sound(sound_file):
    try:
        pygame.mixer.init()
        sound = pygame.mixer.Sound(f"./sounds/{sound_file}")
        sound.play()
        pygame.time.wait(int(sound.get_length() * 1000))  # Wait for the sound to finish playing
    except FileNotFoundError:
        print(f"{sound_file} file not found.")
    except Exception:
        print("Error with playing notification audio.")
    finally:
        pygame.mixer.quit()