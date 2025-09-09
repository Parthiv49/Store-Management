import mysql.connector
import matplotlib.pyplot as py
import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
a=mysql.connector.connect(user='root',host='localhost',passwd='1234')
if a.is_connected():
    print('Successfully Connected')
b=a.cursor()
def a1():
    Name=input(str('Enter your Name: '))
    phone_no=int(input('Enter your Phone number: '))
    print("You're welcome")
    while 1:
        try:
            b.execute('create database if not exists store')
            b.execute('use store')
            b.execute('select item from clothes')
            print('Available cloth items: ')
            for x in b:
                c=x[0]
                print(c)
            d=input('Do you want to continue?(Y/N) ')
            if d=='n' and 'N':
                break
            item=input('What do you want to buy? ')
            b.execute('select item from clothes where item=%s',[item])
            d=b.fetchone()
            if d==None:
                print('There is no such item named',item)
            else:
                print('Available Brands for',item,': ')
                b.execute('select brand from brand where item=%s',[item])
                for x in b:
                    c=x[0]
                    print(c)
                brand=input('Which brand you would like to choose? ')
                b.execute('select brand from brand where brand=%s and item=%s',[brand,item])
                e=b.fetchone()
                if e==None:
                    print('There is no brand named',brand,'available at the moment')
                else:
                    b.execute('select brand from brand where brand=%s and item=%s',[brand,item])
                    for x in b:
                        d=x[0]
                    b.execute('select price from price where item=%s and brand=%s',[item,brand])
                    for x in b:
                        c=x[0]
                        print(c)
                    price=int(input('What price do you want?: '))
                    b.execute('select price from price where item=%s and brand=%s and price=%s',[item,brand,price])
                    d=b.fetchone()
                    if d==None:
                        print('There is no',item,'of brand',brand,'with price Rs.',price)
                    else:
                        print('Price for the',item,'of brand',brand,'is: Rs.',price)
                        h=input('Do you want to buy it?(Y/N) ')
                        if h=='Y' or h=='y':
                            b.execute('create table if not exists purchase(Name varchar(20),Phone_no int,purchase_date date,purchase_time time,item varchar(20),brand varchar(20),price int,quantity int,amount int,foreign key(item) references clothes(item) on delete cascade on update cascade)')
                            a.commit()
                            d=int(input('How much Quantity do you  want? '))
                            e=d*price
                            b.execute('insert into purchase values(%s,%s,current_date(),current_time(),%s,%s,%s,%s,%s)',[Name,phone_no,item,brand,price,d,e])
                            a.commit()
                            b.execute('select quantity from stock where item=%s and brand=%s and price=%s',[item,brand,price])
                            for x in b:
                                quantity=x[0]
                            if(quantity>d):
                                f=quantity-d
                                b.execute('update stock set quantity=%s where item=%s and brand=%s and price=%s',[f,item,brand,c])
                                a.commit()
                                print("Successfully Purchased.")
                            else:
                                print("Out of Stock")
                        elif h=='N' or h=='n':
                           continue
                        else:
                            print("You've choosen an incorrect option")
        except:
            print('There is no clothes item available at the moment.')
            return
def a2():
    Name=input('Enter your Name: ')
    password=input('Enter password: ')
    if password=='staff':
        print('Successfully Logged in.')
        print('Your presence has been marked.')
    else:
        print('Incorrect password!!')
def a3():
    Name=input('Enter you Name: ')
    password=input('Enter password: ')
    if Name=='admin':
        if password=='password':
            print('Login Successful')
            while 1:
                b.execute('create database if not exists store')
                a.commit()
                b.execute('use store')
                b.execute('create table if not exists clothes(item varchar(20) primary key)')
                a.commit()
                b.execute('create table if not exists brand(item varchar(20),brand varchar(20) not null,foreign key(item) references clothes(item) on delete cascade on update cascade)')
                a.commit()
                print('$'*30)
                print('1. Show all the clothes item: ')
                print('2. Enter the clothes item: ')
                print('3. Delete the clothes item: ')
                print('4. Enter the brand of a cloth item: ')
                print('5. Delete the brand of a cloth item: ')
                print('6. Enter the price of a cloth item: ')
                print('7. Change the price of a cloth item: ')
                print('8. Delete the price of a cloth item: ')
                print('9. Enter the stock: ')
                print('10. Update the stock: ')
                print('11. Delete the stock: ')
                print('12. Show purchase details: ')
                print('13. Show Line Chart of sales: ')
                print('14. Show Bar Chart of sales: ')
                print('15. Logout')
                try:
                    opt=int(input('Enter your choice: '))
                    if opt==1:
                        b.execute('select* from clothes')
                        for x in b:
                            c=x[0]
                            print(c)
                    elif opt==2:
                        try:
                            b.execute('select* from clothes')
                            for x in b:
                                d=x[0]
                                print(d)
                            item=input(str('Enter the item name: '))
                            c=[item]
                            b.execute('insert into clothes(item) values(%s)',c)
                            a.commit()
                            b.execute('select* from clothes')
                            for x in b:
                                d=x[0]
                                print(d)
                        except:
                            print('Item',item,'already exists')
                    elif opt==3:
                        try:
                            b.execute('select* from clothes')
                            for x in b:
                                d=x[0]
                                print(d)
                            item=input(str('Enter the item name: '))
                            c=[item]
                            b.execute('Delete from clothes where item=%s',c)
                            a.commit()
                            b.execute('select* from clothes')
                            for x in b:
                                d=x[0]
                                print(d)
                        except:
                            print('Item',item,"doesn't exists")
                    elif opt==4:
                        b.execute('select* from brand')
                        for x in b:
                            c=x[0]
                            d=x[1]
                            print(c,d)
                        item=input(str('Enter the item name: '))
                        brand=input(str('Enter the brand name: '))
                        b.execute('select item from clothes where item=%s',[item])
                        e=b.fetchone()
                        b.execute('select brand from brand where item=%s and brand=%s',[item,brand])
                        f=b.fetchone()
                        if e==None:
                            print('Item',item,"doesn't exists")
                        elif f!=None:
                            print('Brand',brand,'already exists')         
                        else:
                            b.execute('insert into brand(item,brand) values(%s,%s)',[item,brand])
                            b.execute('select* from brand')
                            for x in b:
                                c=x[0]
                                d=x[1]
                                print(c,d)
                    elif opt==5:
                        b.execute('select* from brand')
                        for x in b:
                            c=x[0]
                            d=x[1]
                            print(c,d)
                        item=input(str('Enter the item name: '))
                        brand=input(str('Enter the brand name: '))
                        b.execute('select item from clothes where item=%s',[item])
                        e=b.fetchone()
                        b.execute('select brand from brand where item=%s and brand=%s',[item,brand])
                        f=b.fetchone()
                        if e==None:
                            print('Item',item,"doesn't exists")
                        elif f==None:
                            print('Brand',brand,"doesn't exists for item",item)         
                        else:
                            b.execute('delete from brand where item=%s and brand=%s',[item,brand])
                            b.execute('select* from brand')
                            for x in b:
                                c=x[0]
                                d=x[1]
                                print(c,d)
                    elif opt==6:
                        b.execute('create table if not exists price(item varchar(20),brand varchar(20),price int,foreign key(item) references clothes(item) on delete cascade on update cascade)')
                        b.execute('select* from price')
                        for x in b:
                            e=x[0]
                            f=x[1]
                            g=x[2]
                            print(e,f,g)
                        item=input(str('Enter the item name: '))
                        brand=input(str('Enter the brand: '))
                        price=input(str('Enter the price: '))
                        b.execute('select item from clothes where item=%s',[item])
                        e=b.fetchone()
                        b.execute('select brand from brand where item=%s and brand=%s',[item,brand])
                        f=b.fetchone()
                        if e==None:
                            print('Item',item,"doesn't exists")
                        elif f==None:
                            print('Brand',brand,"doesn't exists for item",item)
                        else:
                            b.execute('select price from price where item=%s and brand=%s and price=%s',[item,brand,price])
                            g=b.fetchone()
                            if g==None:
                                try:
                                    b.execute('insert into price(item,brand,price) values(%s,%s,%s)',[item,brand,price])
                                    b.execute('select* from price')
                                    for x in b:
                                        e=x[0]
                                        f=x[1]
                                        g=x[2]
                                        print(e,f,g)
                                except:
                                     print('Only integer is allowed for price.')
                            else:
                                print('Data with entered details already exists.')
                    elif opt==7:
                        b.execute('select* from price')
                        for x in b:
                            e=x[0]
                            f=x[1]
                            g=x[2]
                            print(e,f,g)
                        item=input(str('Enter the item name: '))
                        brand=input(str('Enter the brand: '))
                        price=input(str('Enter the old price: '))
                        p=input(str('Enter the new price: '))
                        b.execute('select item from clothes where item=%s',[item])
                        e=b.fetchone()
                        b.execute('select brand from brand where item=%s and brand=%s',[item,brand])
                        f=b.fetchone()
                        if e==None:
                            print('Item',item,"doesn't exists")
                        elif f==None:
                            print('Brand',brand,"doesn't exists for item",item)
                        else:
                            try:
                                b.execute('update price set price=%s where item=%s and brand=%s and price=%s',[p,item,brand,price])
                                b.execute('create table if not exists stock(item varchar(20),brand varchar(20),price int,quantity int,foreign key(item) references clothes(item) on delete cascade on update cascade)')
                                b.execute('update stock set price=%s where item=%s and brand=%s and price=%s',[p,item,brand,price])
                                b.execute('select* from price')
                                for x in b:
                                    e=x[0]
                                    f=x[1]
                                    g=x[2]
                                    print(e,f,g)
                            except:
                                print('Only integer is allowed for price.')
                    elif opt==8:
                        b.execute('select* from price')
                        for x in b:
                            e=x[0]
                            f=x[1]
                            g=x[2]
                            print(e,f,g)
                        item=input(str('Enter the item name: '))
                        brand=input(str('Enter the brand: '))
                        price=input(str('Enter the price: '))
                        b.execute('select item from clothes where item=%s',[item])
                        e=b.fetchone()
                        b.execute('select brand from brand where item=%s and brand=%s',[item,brand])
                        f=b.fetchone()
                        if e==None:
                            print('Item',item,"doesn't exists")
                        elif f==None:
                            print('Brand',brand,"doesn't exists for item",item)
                        else:
                            try:
                                b.execute('delete from price where item=%s and brand=%s and price=%s',[item,brand,price])
                                b.execute('select* from price')
                                for x in b:
                                    e=x[0]
                                    f=x[1]
                                    g=x[2]
                                    print(e,f,g)
                            except:
                                print('Only integer is allowed for price.')
                    elif opt==9:
                        b.execute('create table if not exists stock(item varchar(20),brand varchar(20),price int,quantity int,foreign key(item) references clothes(item) on delete cascade on update cascade)')
                        b.execute('select* from stock')
                        for x in b:
                            e=x[0]
                            f=x[1]
                            g=x[2]
                            h=x[3]
                            print(e,f,g,h)
                        item=input(str('Enter the item name: '))
                        brand=input(str('Enter the brand: '))
                        price=input(str('Enter the price: '))
                        quantity=input(str('Enter the quantity: '))
                        b.execute('select item from clothes where item=%s',[item])
                        e=b.fetchone()
                        b.execute('select brand from brand where item=%s and brand=%s',[item,brand])
                        f=b.fetchone()
                        b.execute('select price from price where item=%s and brand=%s and price=%s',[item,brand,price])
                        g=b.fetchone()
                        if e==None:
                            print('Item',item,"doesn't exists")
                        elif f==None:
                            print('Brand',brand,"doesn't exists for item",item)
                        elif g==None:
                            print('Item',item,'of brand',brand,'with price',price,"doesn't exists")
                        else:
                            b.execute('select quantity from stock where item=%s and brand=%s and price=%s and quantity=%s',[item,brand,price,quantity])
                            h=b.fetchone()
                            if h==None:
                                try:
                                    b.execute('insert into stock(item,brand,price,quantity) values(%s,%s,%s,%s)',[item,brand,price,quantity])
                                    b.execute('select* from stock')
                                    for x in b:
                                        e=x[0]
                                        f=x[1]
                                        g=x[2]
                                        h=x[3]
                                        print(e,f,g,h)
                                except:
                                    print('Only integer is allowed for quantity.')
                            else:
                                print('Data with entered details already exists.')
                    elif opt==10:
                        b.execute('select* from stock')
                        for x in b:
                            e=x[0]
                            f=x[1]
                            g=x[2]
                            h=x[3]
                            print(e,f,g,h)
                        item=input(str('Enter the item name: '))
                        brand=input(str('Enter the brand: '))
                        price=input(str('Enter the price: '))
                        quantity=input(str('Enter the quantity: '))
                        b.execute('select item from clothes where item=%s',[item])
                        e=b.fetchone()
                        b.execute('select brand from brand where item=%s and brand=%s',[item,brand])
                        f=b.fetchone()
                        b.execute('select price from price where item=%s and brand=%s and price=%s',[item,brand,price])
                        g=b.fetchone()
                        if e==None:
                            print('Item',item,"doesn't exists")
                        elif f==None:
                            print('Brand',brand,"doesn't exists for item",item)
                        elif g==None:
                            print('Item',item,'of brand',brand,'with price',price,"doesn't exists")
                        else:
                            b.execute('select quantity from stock where item=%s and brand=%s and price=%s and quantity=%s',[item,brand,price,quantity])
                            h=b.fetchone()
                            if h==None:
                                try:
                                    b.execute('update stock set quantity=%s where item=%s and brand=%s and price=%s',[quantity,item,brand,price])
                                    b.execute('select* from stock')
                                    for x in b:
                                        e=x[0]
                                        f=x[1]
                                        g=x[2]
                                        h=x[3]
                                        print(e,f,g,h)
                                except:
                                    print('Only integer is allowed for quantity.')
                            else:
                                print('Data with entered details already exists.')
                    elif opt==11:
                        b.execute('select* from stock')
                        for x in b:
                            e=x[0]
                            f=x[1]
                            g=x[2]
                            h=x[3]
                            print(e,f,g,h)
                        item=input(str('Enter the item name: '))
                        brand=input(str('Enter the brand: '))
                        price=input(str('Enter the price: '))
                        quantity=input(str('Enter the quantity: '))
                        b.execute('select item from clothes where item=%s',[item])
                        e=b.fetchone()
                        b.execute('select brand from brand where item=%s and brand=%s',[item,brand])
                        f=b.fetchone()
                        b.execute('select price from price where item=%s and brand=%s and price=%s',[item,brand,price])
                        g=b.fetchone()
                        if e==None:
                            print('Item',item,"doesn't exists")
                        elif f==None:
                            print('Brand',brand,"doesn't exists for item",item)
                        elif g==None:
                            print('Item',item,'of brand',brand,'with price',price,"doesn't exists")
                        else:
                            try:
                                b.execute('delete from stock where item=%s and brand=%s and price=%s and quantity=%s',[item,brand,price,quantity])
                                b.execute('select* from stock')
                                for x in b:
                                    e=x[0]
                                    f=x[1]
                                    g=x[2]
                                    h=x[3]
                                    print(e,f,g,h)
                            except:
                                print('Only integer is allowed for quantity.')
                    elif opt==12:
                        b.execute('create table if not exists purchase(Name varchar(20),Phone_no int,purchase_date date,purchase_time time,item varchar(20),brand varchar(20),price int,quantity int,amount int,foreign key(item) references clothes(item) on delete cascade on update cascade)')
                        b.execute('select* from purchase')
                        for x in b:
                            c=x[0]
                            d=x[1]
                            e=x[2]
                            f=x[3]
                            g=x[4]
                            h=x[5]
                            i=x[6]
                            j=x[7]
                            k=x[8]
                            print(f"Name: {c}, Phone No: {d}, Date: {e}, Time: {f}, Item: {g}, Brand: {h}, Price: {i}, Quantity: {j}, Amount: {k}")
                            print("\n")
                    elif opt==13:
                        print('1. Item Vs Quantity graph')
                        print('2. Brand Vs Quantity graph')
                        j=int(input('Enter the option: '))
                        try:
                            if j==1:
                                df=pd.read_sql('select item,sum(quantity) as quantity from purchase group by item',a)
                                c=df['item']
                                d=df['quantity']
                                py.style.use('dark_background')
                                py.plot(c,d,label='Item Vs Quantity')
                                py.xlabel('Item')
                                py.ylabel('Quantity')
                                py.legend()
                                py.show()
                            elif j==2:
                                df=pd.read_sql('select brand,sum(quantity) as quantity from purchase group by brand',a)
                                c=df['brand']
                                d=df['quantity']
                                py.style.use('dark_background')
                                py.plot(c,d,label='Brand Vs Quantity')
                                py.xlabel('Brand')
                                py.ylabel('Quantity')
                                py.legend()
                                py.show()
                            else:
                                print("You've chosen wrong option.")
                                
                        except ValueError:
                            print('Only integer is allowed')
                    elif opt==14:
                        print('1. Item Vs Quantity graph')
                        print('2. Brand Vs Quantity graph')
                        j=int(input('Enter the option: '))
                        try:
                            if j==1:
                                df=pd.read_sql('select item,sum(quantity) as quantity from purchase group by item',a)
                                c=df['item']
                                d=df['quantity']
                                py.style.use('dark_background')
                                py.bar(c,d,label='Item Vs Quantity')
                                py.xlabel('Item')
                                py.ylabel('Quantity')
                                py.legend()
                                py.show()
                            elif j==2:
                                df=pd.read_sql('select brand,sum(quantity) as quantity from purchase group by brand',a)
                                c=df['brand']
                                d=df['quantity']
                                py.style.use('dark_background')
                                py.bar(c,d,label='Brand Vs Quantity')
                                py.xlabel('Brand')
                                py.ylabel('Quantity')
                                py.legend()
                                py.show()
                            else:
                                print("You've chosen wrong option.")
                        except ValueError:
                            print('Only integer is allowed')
                    elif opt==15:
                        break
                    else:
                        print('Invalid Choice!!')
                except ValueError:
                    print('Only integer is allowed.')
        else:
            print('Incorrect Password')
    else:
        print('Incorrect Owner Details.')
while 1:
    print('$'*40)
    print('$'*11,'Store Management','$'*11)
    print('$'*40)
    print('1. Enter as a Customer: ')
    print('2. Enter as a Staff Member: ')
    print('3. Enter as an Owner: ') 
    try:
        opt=int(input('Enter the option: '))
        if opt==1:
            a1()
            os.system('cls')
        elif opt==2:
            a2()
        elif opt==3:
            a3()
        else:
            print("You've chosen wrong option.")
    except ValueError:
        print('Only integer is allowed.')