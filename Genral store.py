import mysql.connector as sql
passwd=input("Enter your sql password- ")
try:
    cunobj=sql.connect(host="localhost",user="root",passwd='%s'%(passwd,))
except:
    print("Wrong Password")
    exit()
conobj=cunobj.cursor()
try:
    conobj.execute("create database Genral_Store")
    conobj.execute("use Genral_Store")
except:
    conobj.execute("use Genral_Store")
    print(13)
#Stock Managament
def sm():
    #Create record
    def create():
         global SM1
         true=1
         while true:
             print("\t⚓Creation of Records⚓")
             SM1=input("Enter name of the table- ")
             try:
                 conobj.execute("create table %s(P_name varchar(20),Company varchar(20),Expiry varchar(30),Qty int,Price int)"%(SM1,))
                 break
             except :
                 print("Table already exist")
         in_t=int(input("Enter the number of records you want to Insert"))
         for i in range (in_t):
             Pn=input("Enter  Product Name- ")
             C=input("Enter  Company Name- ")
             E=input("Enter Date- ")
             Q=int(input("Enter Quantity- "))
             P=int(input("Enter Price- "))         
             conobj.execute("insert into %s values('%s','%s','%s',%s,%s)"%(SM1,Pn,C,E,Q,P))
             cunobj.commit()
         print("⚜Your table is created successfully⚜")
    #display all
    def display():
        print("\t❄Display❄")
        conobj.execute("select * from %s"%(SM1,))
        a=conobj.fetchall()
        print("[(\'P_name\',\'Company\',Expiry,Qty,Price)]")
        print(a)
    #display particular 
    def displaypr():
        print("\t✨Display particular✨") 
        pname=input("Enter your Product name")
        conobj.execute("select * from '%s' where P_name='%s'"%(SM,pname))
        a=conobj.fetchall()
        print(a)
    #Edit
    def edit():
        op1=input("Do you want to edit the table you created or a old one?\n")
        while 1:
            if op1 in ["1","a","A","created"]:
                pname=input("Enter the Product you want to edit-: ")
                price=int(input("Enter the New Price of '%s'"%(pname,)))
                conobj.execute("update '%s' set price=%s where p_name='%s'"%(SM1,price,pname))
                break
            elif op1 in ["2","b","B","old"]:
                table=input("Enter your table name-: ")
                pname=input("Enter the Product you want to edit-: ")
                price=int(input("Enter the New Price of '%s'"%(pname,)))
                conobj.execute("update '%s' set price=%s where p_name='%s'"%(table,price,pname))
                break
            else:
                print("Inveled opsion")
    #Delete
    def delete():
        op1=input("Do you want to delete the table you created or a old one?\n")
        while 1:
            if op1 in ["1","a","A","created"]:
                pname=input("Enter the Product you want to delete-: ")
                conobj.execute("delete from '%s' where p_name='%s'"%(SM1,pname))
                break
            elif op1 in ["2","b","B","old"]:
                table=input("Enter your table name-: ")
                pname=input("Enter the Product you want to delete-: ")
                conobj.execute("delete from '%s' where p_name='%s'"%(table,pname))
                break
            else:
                print("Inveled opsion")
    print("-"*12+"Stock Managment"+"-"*12)
    print("\tChoose one option -: ")
    print("a)Create\nb)Display\nc)Display particular\nd)Edit\ne)Delete")
    op=input("Enter your option- ")
    if op in ("a","a)"):
        create()
    elif op in ("b","b)"):
        display()
    elif op in ("c","c)"):
        displaypr()
    elif op in ("d","d)"):
        edit()
    elif op in ("e","e)"):
        delete()
    else :
        print("Error invalid syntax")       
#Bill Genrater
def bill():
           global Nm
           global Q
           global Pr
           f=open("Bill","a+")
           Nm=input("Enter Product Name: ")
           Q=int(input("Enter Product Quantity: "))
           Pr=int(input("Enter Product's Cost with out GST: "))
           Gst=int(input("Enter GST of the Product: "))
           Sn=input("Enter Store Name: ")
           Ad=input("Enter Address: ")
           Ph=input("Enter PhoneNo: ")
           f.write('*'*30+"BILL"+'*'*30+"\n")
           f.write('_'*28+Sn+'_'*25+"\n")
           f.write("ItemName: "+Nm+"\n")
           f.write("Quantity: "+str(Q)+"\n")
           f.write("Cost without GST: "+"$"+str(Pr)+"\n")
           f.write("GST: "+str(Gst)+"%"+"\n")
           f.write("Total Price: "+"$"+str((Pr*Q)*(Gst/100)+(Pr*Q))+"\n")
           f.write("PhoneNo: "+str(Ph)+"\n")
           f.write("Address: "+Ad+"\n") 
           f.write('='*28+"THANK YOU"+'='*27+"\n")
           print("Bill Genrated Succsesfully !!")
           pri=f.read()
           print(pri)
           f.close()
           return True
#Sales
def sales():
    try:
        conobj.execute("create table sales(Bill_no int,Product varchar(30),Qty int,Price int)")
    except:
        #to satisfy except statment_________________________________________
        not_for_any_perpuse=78877

    if option in ("D","D)","d","d)","4","4)"):
            emty=1
            if true:
                conobj.execute("insert into sales values(%s,'%s',%s,%s)"%(emty,Nm,Q,Pr))
                emty=+1
            else:
                print("Nothing has been Soled yet")
    elif option in ("B","B)","b","b)","2","2)"):
                conobj.execute("select * from sales order by Bill_no")
                fetchobj=conobj.fetchall()
                if fetchobj==[]:
                    print("Nothing has been soled yet")
                else:
                    print("[(Bill No.,Product Nm,Qty,Price)]")
                    print(fetchobj)           
#purchase
def purchase():
    try:
        conobj.execute("create table purchase(Product_Sno int,Product_Nm varchar(30),Qty int,Cost int)")
    except:
        #To satisfy except statment________________________________________
        not_for_any_perpuse2=787878
    int_=int(input("Enter the number of product you have purchased-: "))
    for i in range (int_):
        a=input("Enter product name")
        b=int(input("Enter your product's qontity"))            #some problem ower here ;)
        c=int(input("Enter your product's cost"))
        conobj.execute("insert into purchase values(%s,'%s',%s,%s)"%(i+1,a,b,c))
        cunobj.commit()
    print("Your values has been added sucsesfully")            #some problem ower here ;)   
    
#Main Page
true=False
while 1:
    print("-"*12+"Choose one of the options"+"-"*12)
    print("A) Stock Management")
    print("B) Sales")
    print("C)Purchase")
    print("D)Bill ")
    print("E)Exit")
    option=input("Enter your option -: ")
    if  option in ("A","A)","a","a)","1","1)"):
        sm()
    elif option in ("B","B)","b","b)","2","2)"):
        sales()
    elif option in ("C","C)","c","c)","3","3)"):
        purchase()
    elif option in ("D","D)","d","d)","4","4)"):
        true=bill()
        sales()
    elif option in ("E","E)","e","e)","5","5)"):
        print("❤Thanks For Your Visit❤")
        break
    else:
        print("«"*15+"Error invalid value"+"»"*15)
