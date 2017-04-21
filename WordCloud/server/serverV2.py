import collections
import re
from flask import Flask, jsonify, request
import nltk
from nltk.collocations import *
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer

from flask_cors import CORS, cross_origin

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()

app = Flask(__name__)
#

app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

@app.route('/')
def index():
    return 'The server is up and running!'
       
@app.route('/GetNgrams', methods=['GET', 'POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def GetNgrams():
    n = request.args.get('n')
    s = request.args.get('word')
    with open('e.txt', 'r') as myfile:
        data=myfile.read().replace('\n', ' ')
    punctuation = re.compile(r'[-.?!,":;()/\|0-9]') 
    lines = punctuation.sub(" ", data)
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(lines)
    params_filter = lambda *w: s not in w
    if int(n)==3:
        finder = TrigramCollocationFinder.from_words(tokens)       
        finder.apply_ngram_filter(params_filter)
        return jsonify(finder.nbest(trigram_measures.likelihood_ratio, 10))
    else:
        finder = BigramCollocationFinder.from_words(tokens)       
        finder.apply_ngram_filter(params_filter)
        return jsonify(finder.nbest(bigram_measures.likelihood_ratio, 10))

    
def main():
    app.run(debug = True)

if __name__ == '__main__': main()