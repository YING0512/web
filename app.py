from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# 啟動 Flask 伺服器
if __name__ == "__main__":
    app.run(debug=True,host='127.0.0.1', port=5000)
