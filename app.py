from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

def main():
    
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template("index.html")

    return app

if __name__ == "__main__":
    app = main()
    app.run(debug=True)