from app import create_app, db
from flask_socketio import SocketIO

app = create_app()
socketio = SocketIO(app)  # Initialize SocketIO with your Flask app

if __name__ == '__main__':
    
    with app.app_context():
        db.create_all()  # Create database tables
    port = int(os.environ.get('PORT', 5000))
    socketio.run(app, host='0.0.0.0', port=port)
