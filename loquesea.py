# Hacer un codigo que me de 3 opciones para una comida
# 1. Sandwich
# 2. Jugo de mora
# 3. Arroz

# El usuario debera de escoger alguna de estas 3 opciones y
# el programa debera de decirme brevemente como se prepara cada cosa.  

pregunta = input ("escoje entre estas 3 comidas jugo de mora, sandwich, arroz") 
if pregunta == ("jugo de mora"):
    print ("mezclar agua con mora azucar licuar y servirse")
elif pregunta == ("arroz"):
    print (" la arrozera echar arroz lavar el arroz 3 veces, le echas aceite y sal taparlo y ponerlo a fuego, bajas la rozera y servirse")
elif pregunta == ("sandwich"):
    print ("cojer pan,queso jamon y calentarlo por los 2 lados y servirse con el jugo de mora")
else:
    print ("no tengo funcion para eso")