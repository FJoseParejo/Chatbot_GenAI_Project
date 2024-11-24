from multiprocessing.pool import RUN
from urllib import response
import google.generativeai as genai
import PIL.Image
from properties import api_key, to_markdown
from dotenv import load_dotenv
import os


def main():
    # Config the API 
    genai.configure(api_key=os.getenv('SECRET_KEY'))

    # Establecemos el modelo que vamos a usar
    model = genai.GenerativeModel("gemini-1.5-flash")

    # Ruta de la imagen al modelo
    ruta_imagen = "remoto.jpg"
    img = PIL.Image.open(ruta_imagen)

    # # Send the image to the model
    # response = model.generate_content(img)

    # # Printer the response
    # print(to_markdown(response.text))

    instruction = "Escribe un breve y atractivo post de un blog basado en la imagen y en mi experiencia. Debe incluir una descripcion de la foto"

    # To generate the content
    response = model.generate_content([instruction, img], stream=True)
    response.resolve()
    print(to_markdown(response.text))

if __name__ == "__main__":
    main()
