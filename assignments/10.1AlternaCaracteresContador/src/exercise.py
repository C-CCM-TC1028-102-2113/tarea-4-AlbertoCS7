#Alternacaracterescontador
def main():
    repeticiones=int(input("¿Cuantas veces se va a repetir el caracter?"))
    
        for i in range (repeticiones):
            if i % 2 == 0:
            print(i,"-%")
            else:
            print(i,"-#")

    
   
if __name__=='__main__':   
    main()
