from flask import Flask
app = Flask(__name__)
from flask import render_template, request
from TapSearch import TapSearch
ts = TapSearch()


@app.route('/', methods=['GET', 'POST'])
def submit_input():
    ts.clear()
    return render_template('submit_input.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    inputText = request.form['documents']

    # Removing default extra spaces : \r from using TextArea tag
    inputText = inputText.replace('\r', '')

    ts.documents = inputText
    ts.preProcessing()
    ts.index()

    return render_template('search.html')


@app.route('/results', methods=['GET', 'POST'])
def results():
    searchWord = request.form['search_word']
    searchResults = ts.search(searchWord.lower())
    print(searchResults)
    if searchResults:
        return render_template('results.html', searchResults=searchResults, documentIndex=ts.documentIndex, searchWord=searchWord)
    else:
        return render_template('not_found.html', searchWord=searchWord)


if __name__ == '__main__':
    app.run()

