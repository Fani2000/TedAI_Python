import pyjokes as jk
from Lasso import Lasso

class Joke:
    def __init__(self) -> None:
       self.ted = Lasso()

    def TellJoke(self):
        joke = jk.get_joke(language='en', category="all")
        self.ted.Talk(joke)
