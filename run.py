from app import create_app, db

app = create_app()
# Initialize SocketIO with your Flask app

if __name__ == '__main__':
    with app.app_context():
        # Create all tables if they don't exist
        db.create_all()
    # Run the application
    app.run(host='0.0.0.0', port=5000)
