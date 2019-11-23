# TapSearch

A simple program called TapSearch using which you may search a word within a set of documents to retrieve the top 10 paragraphs in which the word is present

## Using TapSearch
### Providing Input Text
Submit your documents separated by exactly two newlines as following:

```
Paragraph-1

Paragraph-2
```
### Searching
In the input field provided, enter the word you would like to search for and click on TapSearch

### Search Results
The top 10 (or less) paragraphs that contain the word entered are displayed

## API
TapSearch performs the following functions in the following sequence to get matching documents:

* **1. preProcessing() -** Splits the user submission to index at paragraphs and index each paragraph as a separate document.
* **2. index() -** Generates a mapping of word to paragraph in which the word is present
* **3. search() -** Given a word, search for it and retrieve the top 10 paragraphs (documents) that contain it
* **4. clear() -** Clears indices and document indices

## Running the tests

```
Sample Input Text:
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Consectetur a erat nam at lectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque.

Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id.

Sample Input Word:
lorem

Sample Output:
lorem - Document #1
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.  Consectetur a erat nam at lectus urna duis convallis. Sed viverra ipsum nunc aliquet bibendum enim facilisis gravida neque.

lorem - Document #2
Maecenas volutpat blandit aliquam etiam erat velit scelerisque. Arcu dictum varius duis at consectetur lorem donec. Aliquet porttitor lacus luctus accumsan tortor. Duis ut diam quam nulla porttitor massa id.
```



