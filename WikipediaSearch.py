import wikipedia

class WikipediaSearch: 
    def __init__(self) -> None:
        pass

    def Search(self, searchText):
        self.results = wikipedia.search(searchText, results=3)
        return self.results

    def Summary(self, topic):
        self.summary = wikipedia.summary(topic)
        return self.summary