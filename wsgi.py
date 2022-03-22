from system.dfweb import app, appConfig


if __name__ == "__main__":
    app.run(debug=False, threaded=True, host=appConfig.host(), port=appConfig.port())
