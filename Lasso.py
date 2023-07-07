import pyttsx3

class Lasso: 

    def __init__(self) -> None:
        self.engine = pyttsx3.init()
        self._setRate(125)
        self._setVolume(1)
        self._setVoices()
        
    def _setRate(self, rate):
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate)
    
    def _setVolume(self, level):
        self.volume = self.engine.getProperty("volume")
        self.engine.setProperty('volume', level)

    def _setVoices(self):
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

    def Talk(self, message):
        self.engine.say(message)
        self.engine.save_to_file(message, "test.mp3")
        self.engine.runAndWait()
        self.engine.stop()
