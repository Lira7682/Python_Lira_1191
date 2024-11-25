print(" ")#espacio
print("Lira Hernandez Dayana Yamileth 1191")#datos del realizador
print(" ")#espacio
cadena = input('Ingresa cadena : ')
#solicita al usuario ingresar cadena
count = 0 #inicializacion de contador
for c in cadena: #para c en cadena
    if c == c.upper():
    #si c igual q cadena en mayusculas
        count += 1 #contador mas o igual q 1
print('Número de mayusculas', count)#imprime numero de mayuculas
print(" ")#espacio