from flask import Flask, render_template, request, send_from_directory

app = Flask(__name__, template_folder=".")


# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")


# Página de login
@app.route("/login.html")
def login():
    return render_template("login.html")


#Flask liga ao CSS
@app.route("/css/<path:arquivo>")
def css(arquivo):
    return send_from_directory("css", arquivo)


#Flask liga as imagens
@app.route("/img/<path:arquivo>")
def img(arquivo):
    return send_from_directory("img", arquivo)


# Usuario e sENHA
@app.route("/entrar", methods=["POST"])
def entrar():

    usuario = request.form["usuario"]
    senha = request.form["senha"]

    if usuario == "admin" and senha == "123":
        return render_template("sucesso.html")

    return "Usuário ou senha incorretos!"


if __name__ == "__main__":
    app.run(debug=True)