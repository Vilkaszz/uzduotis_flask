from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/naujienos')
def naujienos():
    return render_template('naujienos.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/oras')
def oras():
    return render_template('oras.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    vardas = request.form.get('tekstas')
    return render_template('login.html', vardas=vardas)

@app.route('/pasisveikink5', methods=['GET', 'POST'])
def pasisveikink5():
    vardas = request.form.get('vardas')
    pasisveikinimai = None

    if request.method == 'POST' and vardas:
        pasisveikinimai = [f"Labas, {vardas.capitalize()}!" for _ in range(5)]

    return render_template('pasisveikink5.html', vardas=vardas, pasisveikinimai=pasisveikinimai)

if __name__ == '__main__':
    app.run()