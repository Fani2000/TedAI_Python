from Lasso import Lasso
from SpeechRegognition import SpeechRecognition
from WikipediaSearch import WikipediaSearch
from JokeAPI import Joke

ted = Lasso()
ted.Talk('My name is Ted Lasso! an AI tool to answer all your queries.')

def main():
    try:
        ted.Talk('How may I help you?')

        speech = SpeechRecognition()
        joke = Joke()

        speech.Record()

        print(f"This is what you said: {speech.r}")

        if "tell me a joke" in speech.r or "joke" in speech.r:
            joke.TellJoke()
        else:
            wiki = WikipediaSearch()
            summary = wiki.Summary(speech.r)

            if summary:
                ted.Talk(f"Here is what I found about {speech.r}")
                ted.Talk(summary[0:80])

                ted.Talk('I am done. I am glad I help you with your query.')

    except:
        ted.Talk("Couldn't find what you asked,Please Ask another question again.")
        ted.Talk("Goodbye Bitch!, you worthless peace of trash.")
        exit(1)
        # main()

main()
