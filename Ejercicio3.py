#Cambio de variables dentro de las funciones o métododos
x = "bueno"

def myfunc():
  x = "fantastico"
  print("Python es " + x)

myfunc()

print("Python es " + x)

def sefunc ():
 global x
 x = 1
 print ("Python es " + str (x))
 
sefunc ()
#Otra prueba con la función
def prufun ():
    print ("Python es " + str (x))
prufun ()
