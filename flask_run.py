# @time:2020/10/9 12:25
# Author:Small-J

from flask import Flask, render_template

app = Flask(__name__, template_folder='html')


@app.route('/')
def index():
    return render_template('Bi_render.html')


if __name__ == '__main__':
    app.run(debug=True)