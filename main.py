print("Hola Mundo!! Soy Isa :]")
print("Hola Mundo 1!!")

# Soy un comentario
print("Hola Mundo 2!!")

"""
Texto que no se va a interpretar
Texto que no se va a interpretar
Texto que no se va a interpretar
"""

# Variables
texto = "Repaso de Python con Víctor"
nombre = "Isa Oliver"
altura = "187cm"
year = 2023

print(f"{texto} - {nombre} - {altura} - {str(year)}")
print(texto + "-" + nombre + "-" + altura + "-" + str(year))

# Entrada
sitioweb = input("¿Cuál es tu página web?")
print("El sitio web del usuario es: " + sitioweb)

# Condiciones
var_altura = int(input("¿Cuál es tu altura?"))

def mostrarAltura(altura):
    resultado = ""

    if altura >= 180:
        resultado = "Eres una persona alta"
    else:
        resultado = "Eres bajito"

    return resultado

print(mostrarAltura(var_altura))

# Listas
personas = ["Victor", "Paco", "Pedro"]

print(personas[2])

for persona in personas:
    print("-" + persona)