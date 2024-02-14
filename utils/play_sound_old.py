from simpleaudio import WaveObject

#takes sound file with extension as argument then plays corresponding sound
def play_sound(sound_file):
    try:
        audio_object = WaveObject.from_wave_file(f"./sounds/{sound_file}")
        play = audio_object.play()
        play.wait_done()
        play.stop()
    except FileNotFoundError:
        print(f"{sound_file} file not found.")
    except Exception:
        print("Error with playing notification audio.")
    finally:
        return