#NumerosdeFibonacci
def main():
    index = int(input("Enter the index: "))
    n1=0
    n2=1
    i=1
    n2=1
    serie=0
   if index  >= 0:
        if index  == 0:
            print(n1)
        elif index  == 1:
            print(n2)
        elif index  >= 2:
            for i in range(index -1):
                nu = n1 + n2 
                n1 = n2
                n2 = serie
            print(serie)
if __name__=='__main__':
    main()
