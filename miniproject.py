no=(int(input("enter a number:")))
s1=input("enter a string:")
for i in s1:
    if(i=="A"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 and i!=1 
                    or j==no and i!=1
                    or i==1 and j!=1 and j!=no
                    or i==(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #B
    elif(i=="B"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2
                   or i==1 and j>=(no+1)//2 and j!=no
                   or j==no and i!=1 and i!=no and i!=(no+1)//2
                   or i==no and j>=(no+1)//2 and j!=no
                   or i==(no+1)//2 and j>(no+1)//2 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #C
    elif(i=="C"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=1 and i!=no
                   or i==1 and j>(no+1)//2
                   or i==no and j>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #D
    elif(i=="D"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==1 and j>(no+1)//2 and j!=no
                   or i==no and j>(no+1)//2 and j!=no
                   or j==no and i!=1 and i!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #E
    elif(i=="E"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==1 and j>(no+1)//2 
                   or i==(no+1)//2 and j>(no+1)//2
                   or i==no and j>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #F
    elif(i=="F"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==1 and j>(no+1)//2 
           or i==(no+1)//2 and j>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #G
    elif(i=="G"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 and i!=1 and i!=no
           or i==1 and j!=1 and j!=no
           or i==no and j<(no+1)//2 and j!=(no+1)//2 and j!=1
           or j==(no+1)//2 and i>(no+1)//2 and i!=j and i!=no
           or i==(no+1)//2 and j>(no+1)//2 and j!=no
           or j==no and i>(no+1)//2 and i!=(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #H
    elif(i=="H"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 or j==no or i==(no+1)//2):
                     print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #I
    elif(i=="I"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==1 or i==no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #J
    elif(i=="J"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=no or i==1
                or i==no and j<(no+1)//2 and j!=1 and j!=(no+1)//2
                or i==no-1 and j<(no+1)//2 and j!=no//2 and j!=2 and j!=3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #K
    elif(i=="K"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i+j==(no+1) and j>(no+1)//2
           or i==j and j>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #L
    elif(i=="L"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 or i==no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #M
    elif(i=="M"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 or i==j and j<(no+1)//2 
           or i+j==(no+1) and j>(no+1)//2
           or j==no or i==(no+1)//2 and i==j):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #N
    elif(i=="N"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 or j==no or i==j):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print() 
    #O
    elif(i=="O"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 and i!=1 and i!=no
                   or j==no and i!=1 and i!=no
                   or i==1 and j!=1 and j!=no
                   or i==no and j!=1 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #P
    elif(i=="P"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==1 and j>(no+1)//2 and j!=no
           or j==no and i<(no+1)//2 and i!=1 and i!=(no+1)//2
           or i==(no+1)//2 and j>(no+1)//2 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #Q
    elif(i=="Q"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 and j!=1 and j!=no and j!=no-1
           or j==1 and i!=1 and i!=no-1 and i!=no
           or i==no-1 and j!=1 and j!=no 
           or j==no-1 and i!=1 and i!=no-1 and i!=no
           or i==j and i>=(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #R
    
    elif(i=="R"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==1 and j>(no+1)//2 and j!=no
           or j==no and i<(no+1)//2 and i!=1 and i!=(no+1)//2
           or i==(no+1)//2 and j>(no+1)//2 and j!=no
           or i==j and i>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #S
    elif(i=="S"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 and j!=1 and j!=no
           or j==1 and i<(no+1)//2 and i!=(no+1)//2 and i!=1
           or i==(no+1)//2 and j!=1 and j!=no
           or j==no and i>(no+1)//2 and i!=(no+1)//2 and i!=no
           or i==no and j!=no and j!=1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #T
    elif(i=="T"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 or j==(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #U
    elif(i=="U"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 and i!=1 and i!=no
                   or j==no and i!=1 and i!=no
                   or i==no and j!=1 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #V
    elif(i=="V"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 and i<=(no+1)//2
           or j==no and i<=(no+1)//2
           or i==no and j==(no+1)//2
           or i==no-1 and j==2 or i==no-2 and j==1 or i==no-3 and j==1
           or j==no-1 and i==no-1 or j==no and i==no-2 or j==no and i==no-3):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #W
    elif(i=="W"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 or i+j==no+1 and i>(no+1)//2
           or i==j and i>(no+1)//2 or j==no
           or i==(no+1)//2 and i==j):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #X
    elif(i=="X"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==j or i+j==(no+1)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #Y
    elif(i=="Y"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i+j==no+1 or i==j and i<(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #Z 
    elif(i=="Z"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 or i+j==no+1 or i==no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
    #a
    elif(i=="a"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 and j>(no+1)//2 and j!=no
                or j==no and i!=1 
                or i==(no+1)//2 and j>(no+1)//2 and j!=(no+1)//2
                or i==no and j>(no+1)//2 and j!=(no+1)//2 
                or j==(no+1)//2 and i>(no+1)//2 and i!=(no+1)//2 and i!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


#b
    elif(i=="b"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or j==no and i>(no+1)//2 and i!=(no+1)//2 and i!=no
                or i==(no+1)//2 and j>+(no+1)//2 and j!=no
                or i==no and j>(no+1)//2 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

#c
    elif(i=="c"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==(no+1)//2 and j>(no+1)//2 
                or j==(no+1)//2 and i>(no+1)//2 and i!=no
                or i==no and j>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


#d
    elif(i=="d"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==no
                or i==(no+1)//2 and j>(no+1)//2 and j!=(no+1)//2
                or j==(no+1)//2 and i>(no+1)//2 and i!=no
                or i==no and j!=(no+1)//2 and j>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #e
    elif(i=="e"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==(no+1)//2 and j>(no+1)//2 and j!=no
                or j==no and i<(no+1)//2 and i!=1 and i!=(no+1)//2
                or j==(no+1)//2 and i!=1 and i!=no
                or i==1 and j>(no+1)//2 and j!=(no+1)//2 and j!=no
                or i==no and j>(no+1)//2 and j!=(no+1)//2 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
        #f
    elif(i=="f"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i+j-1!=(no+1)//2
                or i==(no+1)//2 and j!=no and j>(no+1)//2
                or i==1 and j!=no and j!=(no+1)//2 and j>(no+1)//2
                or i==2 and j==no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


        #g
    elif(i=="g"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i<(no+1)//2 and i!=1
                or i==(no+1)//2 and j>(no+1)//2 and j!=(no+1)//2
                or j==no and i!=(no+1)//2 and i!=no and i!=1
                or i==1 and j>(no+1)//2 and j!=no
                or i==no and j>(no+1)//2 and j!=no
                or i==no-1 and j==(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


        #h
    elif(i=="h"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==(no+1)//2 and j!=no and j>(no+1)//2
                or j==no and i>(no+1)//2 and i!=(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #i
    elif(i=="i"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=2) :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


        #j
    elif(i=="j"):    
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=2 and i!=no
                or i==no and j<(no+1)//2 and j!=(no+1)//2 and j!=1
                or i==no-1 and j==1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #k
    elif(i=="k"):
        for i in range(1,no+1):
                for j in range(1,no+1):
                    if(j==(no+1)//2 or i+j==(no+1) and j>(no+1)//2
                    or i==j and j>(no+1)//2):
                        print("*",end=" ")
                    else:
                        print(" ",end=" ")
                print()


        #l
    elif(i=="l"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

        #m
    elif(i=="m"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==2 and i>(no+1)//2 
                    or j==(no+3)//2 and i>(no+1)//2
                    or j==no and i>(no+1)//2 
                    or i==(no+1)//2 and j!=2 and j!=(no+3)//2 and j!=no):
                        print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #n
    elif(i=="n"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i>(no+1)//2
                    or j==no and i>(no+1)//2
                    or i==(no+1)//2 and j!=no and j!=(no+1)//2 and j>((no+1)//2)-2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #o
    elif(i=="o"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i>(no+1)//2 and i!=(no+1)//2 and i!=no
                    or j==no and i>(no+1)//2 and i!=(no+1)//2 and i!=no
                    or i==(no+1)//2 and j>(no+1)//2 and j!=(no+1)//2 and j!=no
                    or i==no and j>(no+1)//2 and j!=(no+1)//2 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #p
    elif(i=="p"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==1 and j>(no+1)//2 and j!=no
                    or j==no and i<(no+1)//2 and i!=1 and i!=(no+1)//2
                    or i==(no+1)//2 and j>(no+1)//2 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #q
    elif(i=="q"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or j==1 and i<(no+1)//2 and i!=1
                    or i==(no+1)//2 and j<(no+1)//2 and j!=1
                    or i==1 and j<(no+1)//2 and j!=1
                    or i+j==(no+(no-1)//2+1)):
                        print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #r
    elif(i=="r"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i>(no+1)//2
                    or i==(no+1)//2 and j>(no+1)//2 and j!=no and j!=(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #s
    elif(i=="s"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==2 and j!=1 and j!=no and j!=2 and j!=no-1
                    or j==2 and i<(no+1)//2 and i!=(no+1)//2 and i!=1 and i!=2
                    or i==(no+1)//2 and j!=1 and j!=no and j!=2 and j!=no-1
                    or j==no-1 and i>(no+1)//2 and i!=(no+1)//2 and i!=no and i!=no-1
                    or i==no-1 and j!=no and j!=1 and j!=no-1 and j!=2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()
            
            #t
    elif(i=="t"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=no or i==(no+1)//2 and j>(no+1)//2
                    or i==no and j>(no+1)//2 and j!=(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #u
    elif(i=="u"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=no and i>(no+1)//2
                    or j==no-1 and i!=no and i>(no+1)//2
                    or i==no and j>(no+1)//2 and j!=no-1 and j!=(no+1)//2
                    or j==no and i==no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #v
    elif(i=="v"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i>(no+1)//2 and i!=no
                    or j==no and i>(no+1)//2 and i!=no
                    or i==no and j>(no+1)//2 and j!=no and j!=no-1 and j!=6):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #w
    elif(i=="w"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 and i>=(no+1)//2
                    or j==no and i>=(no+1)//2
                    or i+j-1==no+1 and i>(no+1)//2
                    or i-1==j and i>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #x
    elif(i=="x"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==j+1 and i>=(no+1)//2
                    or i+j-1==(no+(no-1)//2-1) and i>=(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #y
    elif(i=="y"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i+j-1==(no+(no-1)//2-1) or i==j and i<=(no+1)//2 and j!=1 and j!=2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #z
    elif(i=="z"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==(no+1)//2 and j>=(no+1)//2
                    or i+j-2==(no+(no-1)//2-1)
                    or i==no and j>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #0
    elif(i=="0"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==no or j==no or i==1 or j==1 or i+j==(no+1)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

            #1
    elif(i=="1"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 or i==no or i+j-1==(no+1)//2 ):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #2
    elif(i=="2"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 and j!=1 and j!=no
                    or j==no and i!=1 and i<(no+1)//2
                    or i==(no+1)//2 and j!=no and j!=1
                    or j==1 and i>(no+1)//2 and i!=(no+1)//2 and i!=no
                    or i==no and j!=1 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

                
            #3
    elif(i=="3"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 and j!=1 and j!=no
                    or i==(no+1)//2 and j!=1 and j!=no
                    or i==no and j!=1 and j!=no
                    or j==no and i!=1 and i!=(no+1)//2 and i!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #4
    elif(i=="4"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=no or i==(no+1)//2 and j!=no and j!=no-1 or i+j-1==(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #5
    elif(i=="5"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1  and j!=no or j==1 and i<(no+1)//2
                    or i==(no+1)//2 and j!=no 
                    or j==no and i!=(no+1)//2 and i!=no and i!=1 and i>(no+1)//2
                    or i==no and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #6
    elif(i=="6"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=1 and i!=no
                    or i==1 and j>(no+1)//2 and j!=no
                    or i==no and j>(no+1)//2 and j!=(no+1)//2 and j!=no
                    or j==no and i>(no+1)//2 and i!=no and i!=(no+1)//2
                    or i==(no+1)//2 and j>(no+1)//2 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #7
    elif(i=="7"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 or i+j==(no+1)):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #8
    elif(i=="8"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(i==1 and j!=1 and j!=no
                    or i==no and j!=1 and j!=no
                    or j==1 and i!=1 and i!=no and i!=(no+1)//2
                    or j==no and i!=1 and i!=no and i!=(no+1)//2
                    or i==(no+1)//2 and j!=1 and j!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()


            #9
    elif(i=="9"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==(no+1)//2 and i!=1 and i<(no+1)//2
                    or i==1 and j!=(no+1)//2 and j>(no+1)//2 and j!=no
                    or j==no and i!=1 and i!=no
                    or i==no and j!=no and j>(no+1)//2
                    or i==(no+1)//2 and j>(no+1)//2):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

                
            #10
    elif(i=="10"):
        for i in range(1,no+1):
            for j in range(1,no+1):
                if(j==1 or i==1 and j!=2 and j!=no
                    or j==no and i!=1 and i!=no
                    or i==no and j!=2 and j!=no
                    or j==2 and i!=1 and i!=no):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()