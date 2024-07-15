from app import app

def main():
    """
    The main entry point for running the Flask application.

    This function starts the Flask application with debug mode enabled.
    """
    app.run(debug=True)

if __name__ == '__main__':
    main()
