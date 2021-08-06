from pydub import AudioSegment
import os


def detect_leading_silence(sound, silence_threshold=-50.0, chunk_size=10):
    trim_ms = 0  # ms

    assert chunk_size > 0
    while sound[trim_ms:trim_ms + chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms


try:
    os.mkdir("clipped")
    print("made new directory 'clipped'")
except:
    pass

for file in os.listdir(os.curdir):
    print("found file: " + file)
    if file.endswith('.mp3'):
        print("picked mp3: " + file)
        sound = AudioSegment.from_file(os.curdir + "/" + file, format="mp3")

        start_trim = detect_leading_silence(sound)
        end_trim = detect_leading_silence(sound.reverse())

        duration = len(sound)
        trimmed_sound = sound[start_trim:duration - end_trim]

        trimmed_sound.export("clipped/" + file, format="mp3")
        print("exported: clipped/" + file)
