
import mysql.connector as ms
mycon=ms.connect(host='localhost',user='root',passwd='20031998',database='library')
mycursor=mycon.cursor()

#Student/Teacher functions:
        
def Issue():
    print('**WELCOME TO THE BOOKS ISSUING WINDOW**')
    print('Enter the details of the %s who wants to issue books '%(c))
    sid=int(input('Enter %s id '%(c)))
    sn=input('Enter %s name '%(c))
    bn=input('Enter the name of issued book ')
    query="insert into {} values({},'{}','{}',curdate(),null,null)".format(c,sid,sn,bn)
    mycursor.execute(query)
    mycon.commit()


def Return():
    print('**WELCOME TO THE BOOKS RETURNING WINDOW**')
    print('Enter the details of the %s who wants to return books: '%(c))
    sid=int(input('Enter %s id '%(c)))
    print('*AMOUNT OF FINE IS 2RS/DAY IF NOT SUBMITTED WITHIN 2 WEEKS*')

    mycursor.execute('select datediff(curdate(),issuing_date) from %s where id=%s'%(c,sid,))
    n=mycursor.fetchone()
    fine=n[0]*2
    mycursor.execute('update %s set returning_date=curdate() where id=%s;'%(c,sid,))
    mycursor.execute('update %s set fine=%s where id=%s;'%(c,fine,sid))
    mycon.commit()
    if n[0]>14:
        print('*AMOUNT OF FINE NEEDED TO BE SUBMITTED IS*',fine*2)
    else:
        print('*AMOUNT OF FINE NEEDED TO BE SUBMITTED IS 0*')
    

def Update():

    print ('**WELCOME TO THE %s UPDATE WINDOW**'%(c))

    a=int(input('Enter the id of the %s whose record you want to update '%(c)))

    mycursor.execute('select * from %s where id=%s;'%(c,a,))
    data=mycursor.fetchone()

    if data==None:
        print('**RECORD NOT FOUND**')
        return  
    else:
        print('-'*91)
        print('%10s'%'ID','%15s'%'NAME','%15s'%'ISSUED_BOOKNAME','%15s'%'ISSUING_DATE','%15s'%'RETURNING_DATE','%15s'%'FINE')
        print('-'*91)
        print('%10s'%data[0],'%15s'%data[1],'%15s'%data[2],'%15s'%data[3],'%15s'%data[4],'%15s'%data[5])
        print('-'*91)
        
    b=input('''Which attribute of the record do you want to update?
''')
    c1=input('Enter the new value of %s '%(b,))
            
    mycursor.execute('update %s set %s="%s" where id=%s;'%(c,b,c1,a))
    print('**RECORD UPDATED**')

def Display():
    id=int(input('Enter %s Id to display all the details of the %s '%(c.capitalize(),c.capitalize())))
    mycursor.execute("select * from %s where id=%s"%(c,id))
    data=mycursor.fetchall()
    if data==[]:
        print('**RECORD NOT FOUND**')
    else:
        print('-'*91)
        print('%10s'%'ID','%15s'%'NAME','%15s'%'ISSUED_BOOKNAME','%15s'%'ISSUING_DATE','%15s'%'RETURNING_DATE','%15s'%'FINE')
        print('-'*91)
        for row in data:
            print('%10s'%row[0],'%15s'%row[1],'%15s'%row[2],'%15s'%row[3],'%15s'%row[4],'%15s'%row[5])
        print('-'*91)

#Books Functions:

def Update_b():

    print ('**WELCOME TO THE BOOKS UPDATE WINDOW**')

    a=int(input('Enter the id of the book whose record you want to update '))

    mycursor.execute('select * from books where book_id=%s;'%(a,))
    data=mycursor.fetchone()
    print(data)
    if data==None:
        print('**RECORD NOT FOUND**')
        return  
    else:
        print('-'*56)
        print('%7s'%'BOOK_ID','%15s'%'BOOK_NAME','%15s'%'PUBLISHER','%15s'%'BOOK_TYPE')
        print('-'*56)
        print('%7s'%data[0],'%15s'%data[1],'%15s'%data[2],'%15s'%data[3])
        print('-'*56)  
        
    b=input('''Which attribute of the record do you want to update?
''')
    c=input('Enter the new value of %s '%(b,))
            
    mycursor.execute('update books set %s="%s" where book_id=%s;'%(b,c,a))
    mycon.commit()
    print('**RECORD UPDATED**')

def Display_b():
    mycursor.execute("select * from books")
    data=mycursor.fetchall()
    if data==[]:
        print('**RECORDS NOT FOUND**')
        return  
    else:
        print('-'*56)
        print('%7s'%'BOOK_ID','%15s'%'BOOK_NAME','%15s'%'PUBLISHER','%15s'%'BOOK_TYPE')
        print('-'*56)
        for row in data:
            print('%7s'%row[0],'%15s'%row[1],'%15s'%row[2],'%15s'%row[3])
        print('-'*56)
    
def Insert_b():
   print('**WELCOME TO THE BOOKS DATA ENTRY**')
   ans='y'
   while ans.lower()=='y':
       bid=int(input('Enter Book id '))
       bn=input('Enter Book name ')
       pn=input('Enter Publisher name ')
       bt=input('Enter Book type ')
       query="insert into books values({0},'{1}','{2}','{3}')".format(bid,bn,pn,bt)
       mycursor.execute(query)
       mycon.commit()
       print('**BOOK SAVED**')
       ans=input("ADD MORE BOOKS? ")

def Delete_b():
    delete='y'
    while delete.lower()=='y':
        bid=int(input('Enter Book id '))
        query="delete from books where book_id=%s;"%(bid,)
        mycursor.execute(query)
        print("**BOOK DELETED**")
        delete=input("DELETE MORE BOOKS? ")

def Search_b():

    print('**WELCOME TO BOOK SEARCH WINDOW**')

    a=int(input('enter the id of the book whose record you want to search '))

    mycursor.execute('select * from books where book_id=%s;'%(a,))
    data=mycursor.fetchone()

    if data==None:
        print('**RECORD NOT FOUND**')
        return  
    else:
        print('-'*56)
        print('%7s'%'BOOK ID','%15s'%'BOOK NAME','%15s'%'PUBLISHER','%15s'%'BOOK TYPE')
        print('-'*56)
        print('%7s'%data[0],'%15s'%data[1],'%15s'%data[2],'%15s'%data[3])
        print('-'*56)

import time
time.sleep(0.3)
print('****WELCOME TO THE LIBRARY MANAGEMENT SYSTEM****')

while True:
    time.sleep(0.5)
    print(('*')*91)
    print('''#1 for ADMIN LOGIN 
#2 for TEACHER LOGIN 
#3 for STUDENT LOGIN
#4 for EXIT''')
    print(('*')*91)
    user=int(input('ENTER YOUR CHOICE '))

    if user==1:
        while True:
            time.sleep(0.5)
            print("***WELCOME TO ADMIN'S LOGIN WINDOW***")
            print(('*')*91)
            print('''    #1  for ADDING A BOOK
    #2  for DELETING A BOOK
    #3  for SEARCHING A BOOK
    #4  for UPDATING THE DETAILS OF A BOOK
    #5  for UPDATING THE DETAILS OF A STUDENT
    #6  for UPDATING THE DETAILS OF A TEACHER
    #7  for ISSUING A BOOK FOR STUDENT
    #8  for RETURNING A BOOK BY STUDENT
    #9  for ISSUING A BOOK FOR TEACHER
    #10 for RETURNING A BOOK BY TEACHER
    #11 for DISPLAYING BOOKS
    #12 for EXIT''')
            print(('*')*91)
            
            choice=int(input('ENTER YOUR CHOICE  '))

            if choice==1:
                Insert_b()
            elif choice==2:
                Delete_b()
            elif choice==3:
                Search_b()
            elif choice==4:
                Update_b()
            elif choice==5:
                c='student'
                Update()
            elif choice==6:
                c='teacher'
                Update()
            elif choice==7:
                c='student'
                ans='y'
                while ans.lower()=='y':
                    Issue()
                    ans=input('Issue more books? ')
                print('**BOOKS HAVE BEEN ISSUED**')
            elif choice==8:
                c='student'
                ans='y'
                while ans.lower()=='y':
                    Return()
                    ans=input('Return more books? ')
                print('**BOOKS HAVE BEEN RETURNED**')
            elif choice==9:
                c='teacher'
                ans='y'
                while ans.lower()=='y':
                    Issue()
                    ans=input('Issue more books?')
                print('**BOOKS HAVE BEEN ISSUED**')
            elif choice==10:
                c='teacher'
                ans='y'
                while ans.lower()=='y':
                    Return()
                    ans=input('Return more books? ')
                    print('**BOOKS HAVE BEEN RETURNED**')   
            elif choice==11:
                Display_b()
            elif choice==12:
                print()
                break
            else:
                print('Enter a no between 1 and 12 only')
            print()
            
    elif user==2:
        c='teacher'
        import time
        time.sleep(0.5)
        print('***WELCOME TO TEACHER\'S LOGIN WINDOW***')
        Display()

    elif user==3:
        c='student'
        import time
        time.sleep(0.5)
        print('***WELCOME TO STUDENT\'S LOGIN WINDOW***')
        Display()

    elif user==4:
        print()
        print('HOPE YOU COME BACK SOON :)')
        break

    else:
        print('Enter a number between 1 and 4 only')
    
