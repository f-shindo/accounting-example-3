from flask import Flask, request, render_template
from GetTransaction import tx_get

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    title = '過去のトランザクション数を調べたいウォレットを入力してください'

    if request.method == 'GET':
        number = ''
        return render_template('index.html', number=number, title=title)
    else:
        address = request.form.get('address')
        network = request.form.get('list_data')
        number = tx_get(address, network)
        return render_template('index.html', address = address, network = network, number=number, title=title)


if __name__ == '__main__':
    app.run()
