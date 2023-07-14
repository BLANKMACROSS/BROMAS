from PIL import Image, ImageDraw, ImageFont

def agregar_texto(imagen, texto, color, tamaño_fuente):
    # Abre la imagen utilizando PIL
    imagen_pil = Image.open(imagen)

    # Crea un objeto ImageDraw para dibujar en la imagen
    draw = ImageDraw.Draw(imagen_pil)

    # Crea un objeto de fuente con el tamaño deseado
    fuente = ImageFont.truetype("arial.ttf", tamaño_fuente)

    # Obtiene las dimensiones de la imagen
    ancho, alto = imagen_pil.size

    # Calcula las coordenadas para centrar el texto
    texto_ancho, texto_alto = draw.textsize(texto, font=fuente)
    x = (ancho - texto_ancho) // 2
    y = (alto - texto_alto) // 2

    # Dibuja el texto en la imagen
    draw.text((x, y), texto, font=fuente, fill=color)

    # Guarda la imagen con el texto agregado
    nombre_imagen = f"{texto}.png"
    imagen_pil.save(nombre_imagen)

    print("Imagen guardada con éxito.")

# Función que obtene el texto del usuario
def obtener_entrada_usuario():
    texto = input("Ingresa el texto que deseas agregar a la imagen: ")
    tamaño_fuente = int(input("Ingresa el tamaño de la fuente: "))
    return texto, tamaño_fuente

# Las epecificaciones de uso
imagen = "Bromas.png"
color = (0, 255, 0)  # Verde (R, G, B)

texto, tamaño_fuente = obtener_entrada_usuario()
agregar_texto(imagen, texto, color, tamaño_fuente)

# Vivimos en una sociedad xd puto el que lo lea
