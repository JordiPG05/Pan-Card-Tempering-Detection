# Importamos librerias
from app import app
from flask import request, render_template
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image

# Añadir ruta a config
'''
Establecen las rutas de los directorios donde
se guardarán los archivos cargados inicialmente,
los archivos originales y los archivos generados
'''
app.config['INITIAL_FILE_UPLOADS'] = 'app/static/uploads'
app.config['EXISTNG_FILE'] = 'app/static/original'
app.config['GENERATED_FILE'] = 'app/static/generated'

# Definir la ruta raiz
@app.route("/", methods=["GET", "POST"]) # Añadimos solicitudes GET y POST
def index():

	# Ejecutar si la solicitud es GET
	if request.method == "GET":
	    return render_template("index.html") # Carga la plantilla html

	# Ejecutar si la solicitud es POST
    '''
    En este caso se realizara el mismo procedimiento que en el NoteBook'''
	if request.method == "POST":
                # Cargamos la imagen
                file_upload = request.files['file_upload']
                filename = file_upload.filename
                
                # Realizamos un resize a 250x160
                uploaded_image = Image.open(file_upload).resize((250,160))
                uploaded_image.save(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

                # Cargamos la imagen original y le hacemos un resize
                original_image = Image.open(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg')).resize((250,160))
                original_image.save(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg'))

                # Cargamos las imagenes como arrays
                original_image = cv2.imread(os.path.join(app.config['EXISTNG_FILE'], 'image.jpg'))
                uploaded_image = cv2.imread(os.path.join(app.config['INITIAL_FILE_UPLOADS'], 'image.jpg'))

                # Convertimos a escala de grises
                original_gray = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
                uploaded_gray = cv2.cvtColor(uploaded_image, cv2.COLOR_BGR2GRAY)

                # Calculamos la similitud y la differencia
                (score, diff) = structural_similarity(original_gray, uploaded_gray, full=True)
                diff = (diff * 255).astype("uint8")

                # Buscamos el punto de corte y los contornos
                thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
                cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
                cnts = imutils.grab_contours(cnts)
                
                # Dibujamos los contornos
                for c in cnts:
                    (x, y, w, h) = cv2.boundingRect(c)
                    cv2.rectangle(original_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
                    cv2.rectangle(uploaded_image, (x, y), (x + w, y + h), (0, 0, 255), 2)

                # Guardamos todas las imagenes
                cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_original.jpg'), original_image)
                cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_uploaded.jpg'), uploaded_image)
                cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_diff.jpg'), diff)
                cv2.imwrite(os.path.join(app.config['GENERATED_FILE'], 'image_thresh.jpg'), thresh)
                return render_template('index.html',pred=str(round(score*100,2)) + '%' + ' correct')
       
# Main
if __name__ == '__main__':
    app.run(debug=True)
