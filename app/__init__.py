from flask import Flask

app = Flask(__name__)
app.config["ENV"] = "production"

# Definimos el tipo de entorno
if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views # Importamos las views 
