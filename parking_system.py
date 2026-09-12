import turtle
import time
import random

mydb = mysql.connector.connect(host = 'localhost',user ='root',password = 'Admin$123', database ='project_12')
mycursor = mydb.cursor()
mycursor.execute('create table parkinginfo(PARKING_ID int primary key, NAME varchar(225), Car_Number_plate varchar(25),Entry_Time varchar(100), Exit_Time varchar(100))')
mycursor.execute('create table payment(PARKING_ID int, Amount int, Time varchar(100))')



Colours=['maroon','maroon','maroon','maroon','maroon','forest green','gold']#to choose colour for filling boxes
green=[]#to save the boxes with free parking slot
turtle.speed(0)#increasing speed of turtle
#alignment to the bottom left
turtle.penup()
turtle.forward(200)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(850)
turtle.right(90)
turtle.pendown()
#for outline of parking lot
turtle.fillcolor('black')
turtle.begin_fill()
for i in range(2):
    turtle.forward(550)
    turtle.right(90)
    turtle.forward(1200)
    turtle.right(90)
turtle.end_fill()
turtle.forward(120)
turtle.right(90)
#for squares
for ROW in range(4):
    for column in range(13):
        #aligning the turtle to  draw the next square
        turtle.penup()
        turtle.forward(80)
        turtle.pendown()
        #colouring boxes
        choice=random.choice(Colours)
        turtle.fillcolor(choice)
        turtle.begin_fill()
        #saving all green slots
        if choice=='forest green':
            green+=[(column+1,ROW)]#(slot number,row number)
        #drawing 1 square
        for square in range(4):
            turtle.forward(70)
            turtle.right(90)
        turtle.end_fill()
    #to align to the next row
    turtle.penup()
    turtle.backward(1040)
    turtle.left(90)
    turtle.forward(130)
    turtle.right(90)
    turtle.pendown()
#key
#creating a box
for i in range(2):
    turtle.forward(190)
    turtle.right(90)
    turtle.forward(80)
    turtle.right(90)
turtle.forward(20)
key=['KEY:','Red: Parked','Yellow: Reserved','Green: Available']
for i in key:
    turtle.penup()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.write(i,font=('courier new',11,'normal'))
#heading, entry and exit
turtle.goto(-350.00,300.00)
turtle.write('Spotfinder:Efficient Parking System',font=('courier new',25,'normal'))
turtle.goto(470.00,260.00)
turtle.write('Exit',font=('courier new',20,'normal'))
turtle.goto(-630.00,-340.00)
turtle.write('Entry',font=('courier new',20,'normal'))

#interactive mode
turtle.textinput('Welcome', "Hello! Thank you for choosing Efficient Parking System.Press enter to continue.")
while(True):
    slot_or_reservation=int(turtle.textinput('Slot or Reservation', '''Are you in the parking lot or are you looking for a reservation?
Type 1 for In parking lot or 2 for reservation:'''))
    if slot_or_reservation not in [1,2]:
        turtle.textinput('Slot or Reservation', 'Incorrect. Press enter to try again.')
    else:
        break
while(True):
    exit_or_entry=eval(turtle.textinput('Near exit or entry','''Do you want to park near the entry gate or the exit gate?
Type 1 for near entry or 2 for near exit:'''))
    if exit_or_entry not in [1,2]:
        turtle.textinput('Exit or Entry', 'Incorrect. Press enter to try again.')
    else:
        break
#calculating distance to each green box
distance={}
for i in green:
    distance[(130*i[1]+80*i[0])]=i
#finding slot closest to entry or exit
if exit_or_entry == 1:
    slot=distance[min(distance)]#calculating closest to entry
elif exit_or_entry == 2:
    slot=distance[max(distance)]#calculating closest to exit
#entry path
EntryExit=turtle.Turtle()#EntryExit is a turtle created which shows the path to the slot from entry and to exit
EntryExit.color('white')
EntryExit.width(4)
EntryExit.hideturtle()
#alignment
EntryExit.penup()
EntryExit.goto(-610,-300)
EntryExit.pendown()
EntryExit.showturtle()
EntryExit.speed(1)
EntryExit.left(90)
EntryExit.forward(20)
#navigation
EntryExit.forward(130*slot[1])
EntryExit.right(90)
EntryExit.forward(80*slot[0])
EntryExit.left(90)
EntryExit.forward(30)
#fill is a turtle for colouring the box which is parked or reserved
fill=turtle.Turtle()
fill.hideturtle()
fill.penup()
fill.speed(0)

fill.goto(EntryExit.position())
fill.pendown()
fill.backward(35)
#reservation
if slot_or_reservation == 2:
    fill.fillcolor('yellow')
    fill.begin_fill()
    for square in range(4):
        fill.forward(70)
        fill.left(90)
    fill.end_fill()
    turtle.textinput('Reservation','Your slot is reserved. Click enter when you reach the parking lot.')
turtle.textinput('Parking','Park your vehicle in the slot shown. Click enter to fill details.')


name = str(turtle.textinput('INPUT Name','Enter Name : '))
Carnumberplate = str(turtle.textinput('INPUT car no.','Car Plate no. : '))
#starttime = mycursor.execute('select time(now())')
start=time.time()#noting the time when the person parks
start_str=time.ctime()
start_str_format = start_str[:11] + start_str[20:] +'  '+ start_str[11:20]
fill.fillcolor('red')
fill.begin_fill()
for square in range(4):
    fill.forward(70)
    fill.left(90)
fill.end_fill()
#time taken
turtle.textinput('Thank you for parking','Enjoy your time!, When you are done and wish to leave, press enter!')
stop=time.time()#noting the time when the person exits
stop_str=time.ctime()
stop_str_format = stop_str[:11] + stop_str[20:] +'  '+ stop_str[11:20]
#change
#id
#mycursor.execute("select * from parkinginfo")
'''full_data = mycursor.fetchall()
last_entry = full_data[-1]
last_id = last_entry[0]
id = int(last_id) +1'''



#endtime = mycursor.execute('select time(now())')
'''sql_info = 'insert into parkinginfo(PARKING_ID,NAME,Car_Number_plate,Entry_Time,Exit_Time) values(%s,%s,%s,%s,%s)'
val_info = [id , name, Carnumberplate , start , stop]
mycursor.execute(sql_info,val_info)
mydb.commit()'''




EntryExit.clear()
EntryExit.hideturtle()
seconds=stop-start
hours=int(seconds//3600)
minutes=int((seconds%3600)//60)
Seconds=int((seconds%3600)%60)
time = str(hours)+' hrs, '+str(minutes)+' mins, '+str(Seconds)+' secs'
total_time='Total time taken: '+str(hours)+' hours, '+str(minutes)+' minutes and '+str(Seconds)+' seconds.'
turtle.textinput('Time',total_time)
#Amount to pay:
'''amount=50
if hours>0:
    amount+=(30*(hours-1))
if minutes>0 and hours>0:
    amount+=(0.5*minutes)
payment='You have to pay '+str(amount)+'\nPress enter after you have paid'


sql_pay = 'insert into payment(parking_id,amount,time)values(%s,%s,%s)'
val_pay = [id,amount,time]
mycursor.execute(sql_pay,val_pay)
mydb.commit()'''


'''#bill
mycursor.execute("select * from parkinginfo")
full_data = mycursor.fetchall()
last_entry = full_data[-1]
info_str = str('Name : '+ str(last_entry[1]) +'\n'+'Car Number Plate : '+ str(last_entry[2])+'\n'+'Entry Time : '+ start_str_format +'\t'  +'\n'+'Exit Time : ' + stop_str_format +'\n'+'Time spent : '+ str(total_time) +'\n'*2+'Amount Paid : '+str( amount)+'\n')
#info_str = str('Name : '+ str(full_data[-1][1]) +'\n'+'Car Number Plate : '+ str(full_data[-1][2])+'\n'+'Entry Time : '+ str(full_data[-1][3]) +'\n'+'Exit Time : '+str(full_data[-1][4])+'\n'+'Time spent : '+ str(total_time) +'\n'*2+'Amount Paid : '+str( amount)+'\n')

turtle.textinput('BILL',info_str)'''
def bill():
    mycursor.execute("select * from parkinginfo")
    full_data = mycursor.fetchall()
    last_entry = full_data[-1]
    info_str = str('Name : '+ str(last_entry[1]) +'\n'+'Car Number Plate : '+ str(last_entry[2])+'\n'+'Entry Time : '+ start_str_format +'\t'  +'\n'+'Exit Time : ' + stop_str_format +'\n'+'Time spent : '+ str(total_time) +'\n'*2+'Amount Paid : '+str( amount)+'\n')
    turtle.textinput('BILL',info_str)
#bill()


#exit
EntryExit.penup()
EntryExit.forward(70)
EntryExit.showturtle()
EntryExit.pendown()
EntryExit.forward(30)
EntryExit.right(90)
#navigation
EntryExit.forward(80*(14-slot[0]))
EntryExit.left(90)
EntryExit.forward(130*(3-slot[1])+10)
turtle.textinput('Exit','Press enter after you exit!')
fill.clear()
fill.hideturtle()
EntryExit.clear()
EntryExit.hideturtle()
turtle.textinput('Thank you','Thank You, Visit Next Time')




