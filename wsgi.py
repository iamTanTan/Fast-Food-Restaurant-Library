from application.app import app
import os
 
if __name__ == "__main__":
        port = int(os.getenv('PORT'))
        app.run()