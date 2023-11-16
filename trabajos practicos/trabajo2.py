# Crea un programa para una discoteca que me pregunte la edad.
# Si el usuario es menor de edad (Menor de 18 años), me debe de devolver el siguiente mensaje:
# Lo siento, eres menor de edad y no puedes pasar.

# Si el usuario es mayor de edad (Mayor de 18 años), me debe de devolver el siguiente mensaje.
# Bienvenido, que te diviertas.


# Pregunta a plantear: Hola, Esta es una discoteca y necesito saber tu edad... ¿Cuantos años tienes?:

pregunta = input("Hola, ¿cómo estás? Esta es una discoteca. ¿Podrías decirme tu edad?: ")

# Convertir la entrada a un entero
edad = int(pregunta)

if edad >= 18:
    print("¡Claro, pasa! Que tengas un buen día.")
else:
  print("Lo siento, no puedes entrar. Eres menor de edad.")