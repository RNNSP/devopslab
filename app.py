from flask import Flask

app = Flask(_name_)

@app.route("/")
def pagina_inicial():
    return "Hello World"

if _name_ == '_main_':
    app.run()