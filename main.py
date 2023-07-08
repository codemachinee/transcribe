import speech_recognition as sr
import json
from pydub import AudioSegment

r = sr.Recognizer()
# with sr.AudioFile('test.mp3') as source:
with sr.AudioFile('test.wav') as source:
    # r.adjust_for_ambient_noise(source)
    audio = r.record(source)
    try:
        # text = r.recognize_google(audio, language='ru-RU')
        text = r.recognize_vosk(audio, language='ru')
        text = json.loads(text)['text']
    except sr.UnknownValueError:
        pass

with open('data.txt', 'w') as f:
    json.dump(text, f, ensure_ascii=False, indent=4)
    # f.write(text)

