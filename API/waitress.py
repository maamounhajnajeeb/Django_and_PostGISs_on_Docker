from API.wsgi import application
from waitress import serve
import os


if __name__ == "__main__":
    print("Waitress server is runing")
    port, host = os.environ.get("PORT", default=8000), os.environ.get("HOST", default="0.0.0.0")
    print(f"Your app is running on {host}:{port}")
    App = serve(app=application, host=host, port=port)
