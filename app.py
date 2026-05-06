from flask import Flask

# Create Flask application object
app = Flask(__name__)

# Define route (homepage)
@app.route("/")
def home():
    return "Hello Cloud"

# Run the app
if __name__ == "__main__":
    app.run()
