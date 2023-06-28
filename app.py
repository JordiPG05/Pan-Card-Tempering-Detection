from app import app
from config import DevelopmentConfig
import os

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
   app.config["ENV"] = "production"