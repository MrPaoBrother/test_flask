#!/usr/bin/env Python
# coding=utf-8

from flask import Flask

from flask import request

from flask import render_template

import config

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

@app.route('/' , methods=['GET' , 'POST'])
def main():
    return render_template('index.html' , title="Hi" , music = "带你去履行")

if __name__ == '__main__':
    app.run(host=config.REMOTE_IP)
    