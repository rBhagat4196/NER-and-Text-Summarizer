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

#    {% for string in original_text %}
#                 {% if vis[string] == 1 }
#                    <span style="color: red">{{string entities[string]}}</li>
#                 {% else %}
#                    <span>{{string}}</span>
#                {% endif %}
            # {% endfor %}
# {% if condition %}
#     # Code to execute if condition is true
# {% elif another_condition %}
#     # Code to execute if another_condition is true
# {% else %}
#     # Code to execute if neither condition is true
# {% endif %}
# <!-- {{original_text}}   -->
#             {% for string in original_text %}
#               <!-- {% if vis[string] == 1 %} -->
#                 <span>{{string}}</span>
#                <!-- {% else %} -->
#                <!-- <span>{{string}}</span> -->
#               <!-- {% endif %} -->
# <!-- #                 {% else %} -->
#             <!-- <span>{{string}}</span> -->
#             {% endfor %}

# {% for entity in entities %}
#       <span style="color: {{ entity.label }};">{{ entity.text }} ({{ entity.label }})</span><br>
#     {% endfor %}
#   </div>
#   {% endif %}
#   {% if summary %}
#   <h2>Summary</h2>
#   <p>{{ summary }}</p>
#   {% endif %}
#   {% if text %}
#   <h2>Input Text</h2>
#   <p>{{ text }}</p>
#   {% endif %}