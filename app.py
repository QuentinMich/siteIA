from flask import Flask, render_template

app = Flask(
    __name__,
    template_folder=".",
    static_folder=".",
    static_url_path=""
)

@app.route("/")
def accueil():
    return render_template("index.html")


@app.route("/form")
def formulaire():
    return render_template("template/form.html")


if __name__ == "__main__":
    app.run(debug=True)