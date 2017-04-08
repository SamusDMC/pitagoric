# Run cool stuff of mathematics.

from app import app
import os

if os.getenv('DEBUG') == 'True':
    app.run(debug=True)
else:
    app.run()
