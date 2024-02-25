import speech_recognition as sr
from gtts import gTTS
import os
from pydub import AudioSegment
from pydub.playback import play
import tempfile

#sesi tanımak için fonskiyonlar oluşuruyorum

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Dinliyorum...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        #sesi tanımak için google kullanıyoruz
        command = recognizer.recognize_google(audio, language='tr-TR')
        print("Şunu söylediniz: " + command)
        return command
    except sr.UnknownValueError:
        print("Üzgünüm söylediklerinizi anlayamadım.")
        return ""
    except sr.RequestError as e:
        print("Google konuşma tanıma hizmetinden sonuçlar istenemedi;{0}".format(e))
        return""
    
def speak(text):
    tts = gTTS(text)
    # Sesi geçici bir MP3 dosyası olarak kaydediyorum
    temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix= '.mp3')
    tts.save(temp_audio.name)
    temp_audio.close()


    audio = AudioSegment.from_mp3(temp_audio.name)
    play(audio)

    os.remove(temp_audio.name)

while True:
    command = recognize_speech().lower()

    if "merhaba" in command:
        print("Selamlar!")
        continue
    elif "adın ne" in command:
        print("Adım Mustafa senin sesli asistanın.")
        continue
    elif "çıkış" in command:
        print("Görüşmek üzere!")
        break

