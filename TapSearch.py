class TapSearch:
    def __init__(self):
        self.documents = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Magna ac placerat vestibulum lectus. Elit duis tristique sollicitudin nibh sit amet commodo. Senectus et netus et malesuada fames. Fermentum iaculis eu non diam phasellus vestibulum lorem sed. Dictumst quisque sagittis purus sit amet volutpat consequat mauris. Aliquam ut porttitor leo a diam sollicitudin tempor. Consectetur a erat nam at lectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque.

Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Lectus sit amet est placerat in egestas erat imperdiet. Ante in nibh mauris cursus mattis. Tellus rutrum tellus pellentesque eu tincidunt. Euismod quis viverra nibh cras pulvinar mattis. Proin nibh nisl condimentum id venenatis a. Quam elementum pulvinar etiam non quam. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id.
'''
        self.documentIndex = {}
        self.invertedIndex = {}

    # Clears Indices and Document Indices
    def clear(self):
        self.documentIndex.clear()
        self.invertedIndex.clear()

    # Indexes a given document
    def index(self):

        for UNIQUE_ID in range(1, len(self.documentIndex)+1):
            for word in self.documentIndex[UNIQUE_ID].split():

                # separating periods from last words
                word = word.replace('.', '')

                word = word.lower()
                if word not in self.invertedIndex:
                    self.invertedIndex[word] = [UNIQUE_ID]
                else:
                    self.invertedIndex[word].append(UNIQUE_ID)

    # Searches for given word in retrieves the top 10 paragraphs (Documents) that contain it
    def search(self, word):
        if word in self.invertedIndex:
            results = set(self.invertedIndex[word])
            return list(results)[:10].sort()

    # Pre - processes the user submission to index each paragraph as a separate document.
    def preProcessing(self):

        UNIQUE_ID = 1
        for document in self.documents.split('\n\n'):
            self.documentIndex[UNIQUE_ID] = document
            UNIQUE_ID += 1


if __name__ == '__main__':
    ts = TapSearch()
    ts.preProcessing()
    ts.index()
    ts.search('lorem')
    ts.clear()