from main import app

host = '0.0.0.0'
port = 6161

# run the app
if __name__ == "__main__":
    app.run(debug=True, passthrough_errors=True, use_reloader=False, host=host, port=port)