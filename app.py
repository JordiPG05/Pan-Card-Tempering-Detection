from app import app
from config import DevelopmentConfig

if __name__ == '__main__':
   app.run()
   app.config["ENV"] = "production"