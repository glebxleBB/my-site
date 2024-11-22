from flask import Flask, request, render_template

render_template
app = Flask(__name__)

@app.route('/')
def home():
    user_ip = request.remote_addr
    return render_template("apple.html", ip = user_ip)

if __name__ == '__main__':
    app.run(debug=True)