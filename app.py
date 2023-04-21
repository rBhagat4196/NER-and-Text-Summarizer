from flask import Flask , render_template , request
from text_summary import summarizer

app = Flask(__name__)
@app.route('/')

def index():
    return render_template('index.html')

@app.route('/analyse' , methods = ['GET' , 'POST'])


def analyse():
    if(request.method == 'POST'):
        rawtext = request.form['rawtext']
        summary , original_text , len_orig_text , len_summary , entities , html = summarizer(rawtext )
    return render_template('summary.html' , summary=summary , original_text =original_text , len_orig_text = len_orig_text , len_summary = len_summary  , entities = entities , html = html)


if __name__ == "__main__":
    app.run(debug=True)

