# Pan Card Tempering Detection

## About this project

[ES] 
Este proyecto tiene como objetivo utilizar la visión por computadora para detectar la manipulación de tarjetas bancarias. El sistema permitirá a las organizaciones verificar la autenticidad de las identificaciones proporcionadas, como tarjetas Adha y tarjetas bancarias, las cuales a veces pueden ser falsificadas.

En lugar de depender de sistemas de verificación en línea que pueden ser lentos, este proyecto permitirá una verificación instantánea. El proceso implica cargar una imagen de la tarjeta bancaria y verificar si coincide con la imagen original.

[EN]
This project aims to use computer vision to detect bank card tampering. The system will enable organizations to verify the authenticity of provided IDs, such as Adha cards and bank cards, which can sometimes be forged.

Instead of relying on online verification systems that can be slow, this project will enable instant verification. The process involves uploading an image of the bank card and verifying if it matches the original image.


### Step to run application:

- Step 1:	Create the copy of the project 

- Step 2: Open command prompt and change your current path 
to folder where you can find 'app.py' file.

- Step 3: Create environment by command given below-
conda create -name <environment name>

- Step 4: Activate environment by command as follows-
conda activate <environment name>

- Step 5: Use command below to install required dependencies-
python -m pip install -r requirements.txt

- Step 6: Run application by command;
python app.py
You will get url copy it and paste in browser.

- Step 7: You have sample_data folder where you can get images to test.

### Step to run the application in Docker:

- Step 1: Create the copy of the project (`git clone <url_of_repository>`).

- Step 2: Open the command prompt and change the current path 
to the folder where the 'app.py' file is located. (`cd <directory_name>`)

- Step 3: Run the command to create the image (`docker build -t pan-card:latest .`)

- Step 4: Run the command to create and run the container (`docker run --name my-container -d pan-card:latest`)
