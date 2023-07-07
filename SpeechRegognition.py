import speech_recognition as sr

class SpeechRecognition:
    def __init__(self) -> None:
        self.recognizer = sr.Recognizer()

    def Record(self):
        print("Start speaking...")
        self.mic = sr.Microphone()
        with self.mic as source:
            audio = self.recognizer.listen(source, timeout=5)
            self.r = self.recognizer.recognize_google(audio)
    
        



