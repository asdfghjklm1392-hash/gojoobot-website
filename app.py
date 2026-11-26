
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html lang="fa" dir="rtl">
    <head><meta charset="UTF-8"><title>گو جو بات</title></head>
    <body style="background:#07101f;color:white;text-align:center;padding:80px;font-family:tahoma">
    <h1>سلام! سایت گو جو بات روشن است 🎉</h1>
    <p>سرور پایتون با موفقیت کار می‌کند.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
