from flask import Flask, render_template, request, send_from_directory, session, redirect, url_for

app = Flask(__name__, template_folder=".")
app.secret_key = "bencom-chave-secreta"

# Página inicial
@app.route("/")
def inicio():
    return render_template("index.html")


# Página de login
@app.route("/login.html")
def login():

    destino = request.args.get("destino", "inicio")

    return render_template(
        "login.html",
        destino=destino
    )


# Permite carregar os arquivos CSS
@app.route("/css/<path:arquivo>")
def css(arquivo):
    return send_from_directory("css", arquivo)


# Permite carregar as imagens
@app.route("/img/<path:arquivo>")
def img(arquivo):
    return send_from_directory("img", arquivo)

@app.route("/enviar-mensagem")
def enviar_mensagem():

    if session.get("logado"):
        return render_template("mensagem.html")

    return redirect("/login.html?destino=mensagem")


# Recebe os dados do formulário de login
@app.route("/entrar", methods=["POST"])
def entrar():

    usuario = request.form["usuario"]
    senha = request.form["senha"]

    destino = request.form.get("destino", "inicio")

    if usuario == "admin" and senha == "123":

        session["logado"] = True
        session["nome"] = "Luís"
        session["foto"] = "perfil.png"

        if destino == "mensagem":
            return render_template("sucesso.html", destino="mensagem")

        return render_template("sucesso.html", destino="inicio")

    return render_template(
        "login.html",
        erro="Usuário ou senha incorretos.",
        destino=destino
    )

@app.route("/enviar", methods=["POST"])
def enviar():

    if not session.get("logado"):
        return redirect("/login.html?destino=mensagem")

    assunto = request.form["assunto"]
    mensagem = request.form["mensagem"]

    return render_template(
        "mensagem-enviada.html",
        assunto=assunto,
        mensagem=mensagem
    )

@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/cadastro.html")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    nome = request.form["nome"]
    email = request.form["email"]
    usuario = request.form["usuario"]
    senha = request.form["senha"]
    confirmar_senha = request.form["confirmar_senha"]

    if senha != confirmar_senha:

        return render_template(
            "cadastro.html",
            erro="As senhas não coincidem."
        )

    if len(senha) < 8:

        return render_template(
            "cadastro.html",
            erro="A senha deve ter pelo menos 8 caracteres."
        )

    return redirect("/login.html")
    
# Inicia o servidor
if __name__ == "__main__":
    app.run(debug=True)
