from flask import Flask
from bardapi import Bard
import os
import requests
from bardapi.constants import SESSION_HEADERS

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    token = 'eAinwJWrpT2o2E5ssPSI4xe59s9MNQPuSlSxAej7Lk89hnpEL1bCGg5lrfFdkmksGla4Ig.'
    os.environ['_BARD_API_KEY']=token
    session = requests.Session()
    session.headers = SESSION_HEADERS
    session.cookies.set("__Secure-1PSID", token)
   # session.cookies.set("__Secure-1PSIDTS", "<VALUE>")
   # session.cookies.set("__Secure-1PSIDCC", "<VALUE>")

    bard = Bard(token=token, session=session)

    ans = bard.get_answer("나와 내 동년배들이 좋아하는 뉴진스에 대해서 알려줘")['content']
    return ans


if __name__ == '__main__':
    app.run()
