from random import randint,uniform,random,choice
Bombo_lideres=["Rusia","Alemania","Brasil","Portugal","Argentina","Belgica","Polonia","Francia"]
Bombo_dos=["España","Peru","Suiza","Inglaterra","Colombia","Mexico","Uruguay","Croacia"]
Bombo_tres=["Dinamarca","Islandia","Costa rica","Suecia","Tunez","Egipto","Senegal","Iran"]
Bombo_cuatro=["Serbia","Nigeria","Australia","Japon","Marruecos","Panama","Corea del sur","Arabia Saudi"]
lista1=[1,2,3]
lista2=[1,2,3]
lista3=[1,2,3]
lista4=[1,2,3]
lista5=[1,2,3]
lista6=[1,2,3]
lista7=[1,2,3]
lista8=[1,2,3]
Grupo_a=[1,"2","3","4"]
Grupo_b=["1","2","3","4"]
Grupo_c=["1","2","3","4"]
Grupo_d=["1","2","3","4"]
Grupo_e=["1","2","3","4"]
Grupo_f=["1","2","3","4"]
Grupo_g=["1","2","3","4"]
Grupo_h=["1","2","3","4"]
maricada=[]
Conmebol=["Brasil","Uruguay","Argentina","Colombia","Peru"]
Uefa=["Suiza","Croacia","Suecia","Dinamarca","Francia","Portugal","Alemania","Serbia","Polonia","Inglaterra","España","Belgica","Islandia","Rusia"]
Caf=["Nigeria","Egipto","Senegal","Tunez","Marruecos"]
Afc=["Iran","Japon","Corea del Sur","Arabia Saudi","Australia"]
Concacaf=["Mexico","Costa Rica","Panama"]
x=input("Inserte cualquier tecla numerica o alfabetica o simbolica para empezar el sorteo de los grupos del mundial ")
maricada.append(x)
if len(maricada)==1:
    print("Estan cargando los datos... ")
    Grupo_a[0]='Rusia'
    Bombo_lideres.remove("Rusia")
    b1=choice(Bombo_lideres)
    Grupo_b[0]=b1
    Bombo_lideres.remove(b1)
    c1=choice(Bombo_lideres)
    Grupo_c[0]=c1
    Bombo_lideres.remove(c1)
    d1=choice(Bombo_lideres)
    Grupo_d[0]=d1
    Bombo_lideres.remove(d1)
    e1=choice(Bombo_lideres)
    Grupo_e[0]=e1
    Bombo_lideres.remove(e1)
    f1=choice(Bombo_lideres)
    Grupo_f[0]=f1
    Bombo_lideres.remove(f1)
    g1=choice(Bombo_lideres)
    Grupo_g[0]=g1
    Bombo_lideres.remove(g1)
    h1=choice(Bombo_lideres)
    Grupo_h[0]=h1
    Bombo_lideres.remove(h1)
    a0=choice(Bombo_dos)
    num1=choice(lista1)
    lista1.remove(num1)
    Grupo_a[num1]=a0
    Bombo_dos.remove(a0)
    b0=choice(Bombo_dos)
    print(b0)
    print(Grupo_b)
    c=b0 in Conmebol
    d=Grupo_b[0] in Conmebol
    if c==True and d==True:
        print("Ya hay un pais perteneciente a la conmebol en este grupo, se ira al siguiente grupo")
    else:
            numb=choice(lista2)
            lista2.remove(numb)
            Grupo_b[numb]=b0
            Bombo_dos.remove(b0)
            print (Grupo_b)
    elif b0 in Conmebol and Grupo_c[0] in Conmebol:
            if b0 in Conmebol and Grupo_d[0] in Conmebol:
                if b0 in Conmebol and Grupo_e[0] in Conmebol:
                    if b0 in Conmebol and Grupo_f[0] in Conmebol:
                        if b0 in Conmebol and Grupo_g[0] in Conmebol:
                            if b0 in Conmebol and Grupo_h[0] in Conmebol:
                                print("mi polla")