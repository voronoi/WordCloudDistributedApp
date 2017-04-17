import collections
import re
from flask import Flask, jsonify
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from flask_cors import CORS, cross_origin

app = Flask(__name__)
#

app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/foo": {"origins": "http://localhost:port"}})

@app.route('/')
def index():
    return 'The server is up and running!'



def tokenize(string):
    """Convert string to lowercase and tokenize using regExp tokenizer.
    """
    string = string.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(string)
    return tokens


def count_ngrams(linesRaw, length):
    min_length = 1
    """Iterate through given lines iterator (file object or list of
    lines) and return n-gram frequencies. The return value is a dict
    mapping the length of the n-gram to a collections.Counter
    object of n-gram tuple and number of times that n-gram occurred.
    Returned dict includes n-grams of length length.
    """
    ngrams = {length: collections.Counter()}
    queue = collections.deque(maxlen=length)

    def add_queue():
        current = tuple(queue)
        if len(current) >= length:
            ngrams[length][current[:length]] += 1
    punctuation = re.compile(r'[-.?!,":;()/\|0-9]')   # Strip all Punctuation
    lines = [punctuation.sub(" ", do) for do in linesRaw]   
    for line in lines:
        for word in tokenize(line):
            if (word not in stopwords.words('english')):
                if (word != 'n' and word != 'u'):
                    queue.append(word)
                    if len(queue) >= length:
                        add_queue()
    while len(queue) > min_length:
        queue.popleft()
        add_queue()
    return ngrams


def return_most_frequent(ngrams, num=10):
    """Return num most common n-grams of each length in n-grams dict."""
    for n in sorted(ngrams):
        fi = {}
        for gram, count in ngrams[n].most_common(num):
            fi[(' '.join(gram))] = count
        return fi
                
        
@app.route('/GetNgrams/<int:n>', methods=['GET', 'POST'])
@cross_origin(origin='localhost',headers=['Content- Type','Authorization'])
def GetNgrams(n):
    with open('e.txt') as f:
        ngrams = count_ngrams(f, n)
    ngramsDict = return_most_frequent(ngrams)   
    return jsonify(ngramsDict)

    
def main():
    app.run(debug = True)

if __name__ == '__main__': main()