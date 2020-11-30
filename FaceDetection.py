from app import app
import waitress
import os

if __name__ == "__main__":
    app.debug = False
    port = int(os.environ.get('PORT', 33507))
    waitress.serve(app, port=port)
