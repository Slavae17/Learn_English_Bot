from app import app, db
from app.components import Categories, Word

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Categories': Categories, 'Word': Word}