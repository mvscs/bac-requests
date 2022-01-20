import logging
import requests
from flask import Flask
app = Flask(__name__)
@app.route('/entry', methods=['GET', 'POST'])
def test():
    url = 'https://631629-sb1.extforms.netsuite.com/app/site/hosting/scriptlet.nl?script=8348&deploy=1&compid=631629_SB1&h=775ff9f7bf48ce708b53'
    myobj   = {'somekey': 'somevalue'}
    headers = {'content-type': 'application/json', 'User-Agent':'Mozilla/5'}
    x = requests.post(url, data = myobj, headers=headers)
    return (x.text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
