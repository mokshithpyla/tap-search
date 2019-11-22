from app import app

from flask import render_template, request

import sys

@app.route('/', methods=['GET', 'POST'])
def index():
    """
        Renders Home Page
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run()

