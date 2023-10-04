from src.main import app
import src.callbacks # Чтобы подключить callbacks

if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")
