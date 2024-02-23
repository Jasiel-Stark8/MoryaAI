import mongoengine as db

def initialize_db(app):
    """
    Initializes the database connection using the provided app configuration.

    Args:
        app (Flask): The Flask application object.

    Returns:
        None
    """
    db_name = app.config['DB_NAME']
    host = app.config['DB_HOST']
    db.connect(db_name, db_host=host)
