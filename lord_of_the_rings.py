"""
            A custom website using an API
            Only for fans
"""

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_ckeditor import request
from forms import ToolsForm
import pandas as pd
import random
import os
from dotenv import load_dotenv

data = pd.read_csv('lord_of_the_rings.csv')
columns = data.columns


def get_who_is_it(char):
    who_is_it = data[data.name == char]
    index_who = who_is_it.index[0]
    for column in columns:
        if str(who_is_it[column][index_who]) == 'nan':
            who_is_it.at[index_who, column] = 'No information'
    return who_is_it, index_who


app = Flask(__name__)
load_dotenv('.env')
SECRET_KEY = os.getenv('SECRET_KEY')
app.config['SECRET_KEY'] = SECRET_KEY
Bootstrap(app)


@app.route('/')
def demo():
    char = random.choice(data.name)
    who_is_it, index_who = get_who_is_it(char)
    return render_template("index.html", char=who_is_it, columns=columns, index=index_who)


@app.route('/tools', methods=['GET', 'POST'])
def tools():
    form = ToolsForm()
    if form.validate_on_submit():
        character = request.form.get('character')
        who_is_it, index_who = get_who_is_it(character)
        return render_template("index.html", char=who_is_it, columns=columns, index=index_who)
    return render_template("tools.html", form=form)


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

