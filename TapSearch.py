class TapSearch:
    def __init__(self):
        self.documents = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam at lectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque. 



Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id.

'''
        self.documentIndex = {}
        self.preProcessing()
        self.invertedIndex = {}

    def clear(self):
        self.documentIndex.clear()
        self.invertedIndex.clear()

    def index(self):

        for UNIQUE_ID in range(1, len(self.documentIndex)+1):
            for word in self.documentIndex[UNIQUE_ID].split():
                word = word.replace('.', '')
                word = word.lower()
                if word not in self.invertedIndex:
                    self.invertedIndex[word] = [UNIQUE_ID]
                else:
                    self.invertedIndex[word].append(UNIQUE_ID)
        # print(self.invertedIndex)

    def search(self, word):
        if word in self.invertedIndex:
            results = self.invertedIndex[word][:10]
            print(set(results))
            for UNIQUE_ID in set(results):
                print(word, ' found in', self.documentIndex[UNIQUE_ID])

    def preProcessing(self):

        UNIQUE_ID = 1
        for document in self.documents.split('\n\n\n'):
            self.documentIndex[UNIQUE_ID] = document
            UNIQUE_ID += 1
        print(self.documentIndex)


if __name__ == '__main__':
    TS = TapSearch()
    TS.index()
    TS.search('lorem')
    TS.clear()