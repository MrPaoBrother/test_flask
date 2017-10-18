from flask import Flask

from flask import request

from flask import render_template


app = Flask(__name__)

@app.route('/' , methods=['GET' , 'POST'])
def main():
    return render_template('index.html' , title="Power" , message = "逸宁出来聊天吗?")

if __name__ == '__main__':
    app.run(host='45.77.150.109')
    