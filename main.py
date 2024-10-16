import random
from logging import root
from tkinter import *
from tkinter import Label, messagebox, StringVar
import time;
import datetime;

t=Tk()
t.title("car management system")
t.geometry('1350x700+0+0')
LeftMayFrame=Frame(t,width=1000,height=650,bd=8,relief='raise')
LeftMayFrame.pack(side=LEFT)
RightMayFrame=Frame(t,width=350,height=650,bd=8,relief='raise')
RightMayFrame.pack(side=RIGHT)
LeftMayFrame1=Frame(LeftMayFrame,width=1000,height=225,bd=8,relief='raise')
LeftMayFrame1.pack(side=TOP)
LeftMayFrame2=Frame(LeftMayFrame,width=1000,height=225,bd=8,relief='raise')
LeftMayFrame2.pack(side=TOP)
LeftMayFrame3=Frame(LeftMayFrame,width=1000,height=100,bd=8,relief='raise')
LeftMayFrame3.pack(side=TOP)
LeftMayFrame4=Frame(LeftMayFrame,width=1000,height=100,bd=8,relief='raise')
LeftMayFrame4.pack(side=TOP)


RightMayFrame1=Frame(RightMayFrame,width=350,height=325,bd=8,relief='raise')
RightMayFrame1.pack(side=TOP)
RightMayFrame2=Frame(RightMayFrame,width=350,height=325,bd=8,relief='raise')
RightMayFrame2.pack(side=BOTTOM)

txtReceipt=Text(RightMayFrame2,height=16,width=33,bd=8,font=('arial',11,'bold'))
txtReceipt.grid(row=0,column=0)
#-----------------------------------------------Cost of Renting a Car---------------------------------------------
def CarRentalCost():
    NoofDays=float(NumberOfDays.get())
    CarDiscount=float(Discount.get())
    DailyRate=float(DaysRented.get())
    RentalCost=(((NoofDays*DailyRate)*CarDiscount)/100)
    CostofRental="$",str("%.2f"%((NoofDays*DailyRate)-RentalCost))
    Total.set(CostofRental)
    ID=random.randint(51,95)
    randomID=str(ID)
    CustomerID.set("CAR"+randomID)
    Inv=random.randint(15,112)
    InvID=str(Inv)
    InvoiceId.set("INV"+InvID)

#-----------------------------------------------Variable----------------------------------------------------------
var1=IntVar()
var2=IntVar()
var3=IntVar()
var4=IntVar()
var5=IntVar()
var6=IntVar()
var7=IntVar()
var8=IntVar()
CustomerID=StringVar()
DaysRented=StringVar()
Discount=StringVar()
NumberOfDays=StringVar()
InvoiceId=StringVar()
Total=StringVar()
EngineSize=StringVar()
Style=StringVar()
RegisteredYear=StringVar()
ClassId=StringVar()
CarDiscription=StringVar()
MilesBefore=StringVar()
MilesAfter=StringVar()
Make=StringVar()
Model=StringVar()
CarColour=StringVar()
CarInsurance=StringVar()
Area=StringVar()
IssueBy=StringVar()
IssueDate=StringVar()
LicenceNumber=StringVar()
LastName=StringVar()
Street=StringVar()
EngineMade=StringVar()
FirstName=StringVar()
Title=StringVar()
Customer=StringVar()
PostCode=StringVar()
Dateoforder=StringVar()
Receipt_Ref=StringVar()
#------------------------------------------Function Defination-----------------------------------------------------
def uExit():
    a=messagebox.askyesno("Exit system","Do you want to quit?")
    if a>0:
        t.destroy()
        return
#-------------------------------------------Reset------------------------------------------------------------------

def Reset():
    var1.set("")
    var2.set("")
    var3.set("")
    var4.set("")
    var5.set(0)
    var6.set(0)
    var7.set(0)
    var8.set(0)




    DaysRented.set("")
    Discount.set("")
    NumberOfDays.set("")
    Total.set("")
    EngineSize.set("")
    RegisteredYear.set("")
    CarDiscription.set("")
    MilesBefore.set(" ")
    MilesAfter.set("")
    Make.set(" ")
    Model.set("")
    EngineMade.set("")
    CarColour.set("")
    Dateoforder.set("")
    Receipt_Ref.set("")

    CarInsurance.set(" ")
    Area.set("")
    IssueBy.set("")
    IssueDate.set(" ")
    LicenceNumber.set("")
    LastName.set("")
    Street.set("")
    FirstName.set("")
    Title.set("")
    Customer.set("")
    PostCode.set("")
    MilesBefore.set(" ")
    MilesAfter.set("")
    txtReceipt.delete("1.0",END)
#--------------------------------------------Receipt-----------------------------------------------------------------
def Receipt():
    txtReceipt.delete("1.0",END)
    x = random.randint(108,506)
    randomRef=str(x)
    Receipt_Ref.set("BILL"+randomRef)
    txtReceipt.insert(END,"Receipt Ref:\t"+Receipt_Ref.get()+'\n\nDate:\t'+IssueDate.get()+"\n\n")
    txtReceipt.insert(END,"CAR RENTAL SERVICES\n\n")
    txtReceipt.insert(END,"CustomerID: \t"+txtCustomerId.get()+"\n\n")
    txtReceipt.insert(END,"Days Rented: \t"+DaysRented.get()+"\n\n")
    txtReceipt.insert(END,"NumberOfDays: \t"+NumberOfDays.get()+"\n\n")
    txtReceipt.insert(END,"InvoiceID: \t"+txtInvoiceId.get()+"\n\n")
    txtReceipt.insert(END,"Discount: \t"+Discount.get()+"\n\n")
    txtReceipt.insert(END,"TOtal: \t"+Total.get()+"\n\n")







#-----------------------------------------RightMayFrame1------------------------------------------------------------
Style=Checkbutton(RightMayFrame1,text='STYLE\t',onvalue=1,offvalue=0,font=('arial',14,'bold'))
Style.grid(row=0,sticky=W)
ClassId=Checkbutton(RightMayFrame1,text='CLASS ID\t\t',onvalue=1,offvalue=0,font=('arial',14,'bold'))
ClassId.grid(row=1,sticky=W)
InvoiceId=Checkbutton(RightMayFrame1,text='INVOICE ID\t',onvalue=1,offvalue=0,font=('arial',14,'bold'))
InvoiceId.grid(row=2,sticky=W)
DailyRate=Checkbutton(RightMayFrame1,text='DAILY RATE\t',onvalue=1,offvalue=0,font=('arial',14,'bold'))
DailyRate.grid(row=3,sticky=W)
Automatic=Checkbutton(RightMayFrame1,text='AUTOMATIC\t',onvalue=1,offvalue=0,font=('arial',14,'bold'))
Automatic.grid(row=4,sticky=W)
AirCondition=Checkbutton(RightMayFrame1,text='AIR CONDITION \t',onvalue=1,offvalue=0,font=('arial',14,'bold'))
AirCondition.grid(row=5,sticky=W)
InsuranceSold=Checkbutton(RightMayFrame1,text='INSURANCE SOLD \t',onvalue=1,offvalue=0,font=('arial',14,'bold'))
InsuranceSold.grid(row=6,sticky=W)
CustomerDetails=Checkbutton(RightMayFrame1,text='CUSTOMER DETAILS \t',onvalue=1,offvalue=0,font=('arial',14,'bold'))
CustomerDetails.grid(row=7,sticky=W)







#----------------------------------------LeftMayFrame1-------------------------------------------------------------
lb1Customer=Label(LeftMayFrame1,font=('arial',11,'bold'),text="CUSTOMER",bd=8)
lb1Customer.grid(row=0,column=0,sticky=W)
txtCustomer=Entry(LeftMayFrame1 ,font=('arial',11,'bold'),text="CUSTOMER",bd=8,width=31,justify='left' ,textvariable=Customer)
txtCustomer.grid(row=0,column=1)


lb1Title=Label(LeftMayFrame1,font=('arial',11,'bold'),text="TITLE",bd=8)
lb1Title.grid(row=0,column=2,sticky=W)
txtTitle=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="TITLE",bd=8,width=31,justify='left',textvariable=Title)
txtTitle.grid(row=0,column=3)


lb1FirstName=Label(LeftMayFrame1,font=('arial',11,'bold'),text="FIRST NAME",bd=8)
lb1FirstName.grid(row=0,column=4,sticky=W)
txtFirstName=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="FIRST NAME",bd=8,width=31,justify='left',textvariable=FirstName)
txtFirstName.grid(row=0,column=5)

lb1LastName=Llb1CustomerID=Label(LeftMayFrame1,font=('arial',11,'bold'),text="LAST NAME",bd=8)
lb1LastName.grid(row=1,column=0,sticky=W)
txtLastName=Entry(LeftMayFrame1 ,font=('arial',11,'bold'),text="LAST NAME",bd=8,width=31,justify='left',textvariable=LastName)
txtLastName.grid(row=1,column=1)


lb1Street=Label(LeftMayFrame1,font=('arial',11,'bold'),text="STREET",bd=8)
lb1Street.grid(row=1,column=2,sticky=W)
txtStreet=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="STREET",bd=8,width=31,justify='left',textvariable=Street)
txtStreet.grid(row=1,column=3)


lb1Area=Label(LeftMayFrame1,font=('arial',11,'bold'),text="AREA",bd=8)
lb1Area.grid(row=1,column=4,sticky=W)
txtArea=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="AREA",bd=8,width=31,justify='left',textvariable=Area)
txtArea.grid(row=1,column=5)

lb1PostCode=Label(LeftMayFrame1,font=('arial',11,'bold'),text="POST CODE ",bd=8)
lb1PostCode.grid(row=2,column=0,sticky=W)
txtPostCode=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="POST CODE",bd=8,width=31,justify='left',textvariable=PostCode)
txtPostCode.grid(row=2,column=1)

lb1LicenceNumber=Label(LeftMayFrame1,font=('arial',11,'bold'),text="LICENCE NUMBER",bd=8)
lb1LicenceNumber.grid(row=2,column=2,sticky=W)
txtLicenceNumber=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="LICENCE NUMBER",bd=8,width=31,justify='left',textvariable=LicenceNumber)
txtLicenceNumber.grid(row=2,column=3)

lb1IssueDate=Label(LeftMayFrame1,font=('arial',11,'bold'),text="ISSUE DATE ",bd=8)
lb1IssueDate.grid(row=2,column=4,sticky=W)
txtIssueDate=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="ISSUE DATE",bd=8,width=31,justify='left',textvariable=IssueDate)
txtIssueDate.grid(row=2,column=5)


lb1IssueBy=Label(LeftMayFrame1,font=('arial',11,'bold'),text="ISSUE BY ",bd=8)
lb1IssueBy.grid(row=3,column=0,sticky=W)
txtIssueBy=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="ISSUE BY ",bd=8,width=31,justify='left',textvariable=IssueBy)
txtIssueBy.grid(row=3,column=1)

lb1MilesBefore=Label(LeftMayFrame1,font=('arial',11,'bold'),text="MILES BEFORE",bd=8)
lb1MilesBefore.grid(row=3,column=2,sticky=W)
txtMilesBefore=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="MILES BEFORE",bd=8,width=31,justify='left',textvariable=MilesBefore)
txtMilesBefore.grid(row=3,column=3)

lb1MilesAfter=Label(LeftMayFrame1,font=('arial',11,'bold'),text="MILES AFTER ",bd=8)
lb1MilesAfter.grid(row=3,column=4,sticky=W)
txtMilesAfter=Entry(LeftMayFrame1,font=('arial',11,'bold'),text="MILES AFTER",bd=8,width=31,justify='left',textvariable=MilesAfter)
txtMilesAfter.grid(row=3,column=5)
#--------------------------------------------RightMayFrame2----------------------------------------------------
txtReceipt=Text(RightMayFrame2,height=20,width=35,bd=8,font=('arial',11,'bold'))
txtReceipt.grid(row=0,column=0)
#---------------------------------------------Date in RightMayFrame-----------------------------------------------
Dateoforder.set(time.strftime("%d/%m/%y"))

#---------------------------------------LeftMayFrame2--------------------------------------------------------------
lb1EngineSize=Label(LeftMayFrame2,font=('arial',11,'bold'),text="ENGINE SIZE",bd=8)
lb1EngineSize.grid(row=0,column=0,sticky=W)
txtEngineSize=Entry(LeftMayFrame2 ,font=('arial',11,'bold'),text="ENGINE SIZE",bd=8,width=31,justify='left',textvariable=EngineSize)
txtEngineSize.grid(row=0,column=1)
lb1Style=Label(LeftMayFrame2,font=('arial',11,'bold'),text="STYLE",bd=8)
lb1Style.grid(row=0,column=2,sticky=W)
txtStyle=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="STYLE",bd=8,width=31,justify='left',textvariable=var3)
txtStyle.grid(row=0,column=3)
lb1RegisteredYear=Label(LeftMayFrame2,font=('arial',11,'bold'),text="REGISTERED YEAR",bd=8)
lb1RegisteredYear.grid(row=0,column=4,sticky=W)
txtRegisteredYear=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="REGISTERED YEAR",bd=8,width=31,justify='left',textvariable=RegisteredYear)
txtRegisteredYear.grid(row=0,column=5)
lb1ClassId=Label(LeftMayFrame2,font=('arial',11,'bold'),text="CLASS ID",bd=8)
lb1ClassId.grid(row=1,column=0,sticky=W)
txtClassId=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="CLASS ID",bd=8,width=31,justify='left',textvariable=var4)
txtClassId.grid(row=1,column=1)
lb1CarDiscription=Label(LeftMayFrame2,font=('arial',11,'bold'),text="CAR DISCRIPTION",bd=8)
lb1CarDiscription.grid(row=1,column=2,sticky=W)
txtCarDiscription=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="CAR DISCRIPTION",bd=8,width=31,justify='left',textvariable=CarDiscription)
txtCarDiscription.grid(row=1,column=3)
lb1MilesBefore=Label(LeftMayFrame2,font=('arial',11,'bold'),text="MILES BEFORE",bd=8)
lb1MilesBefore.grid(row=1,column=4,sticky=W)
txtMilesBefore=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="MILES BEFORE",bd=8,width=31,justify='left',textvariable=MilesBefore)
txtMilesBefore.grid(row=1,column=5)
lb1MilesAfter=Label(LeftMayFrame2,font=('arial',11,'bold'),text="MILES AFTER",bd=8)
lb1MilesAfter.grid(row=2,column=0,sticky=W)
txtMilesAfter=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="NUMBER OF DAYS",bd=8,width=31,justify='left',textvariable=MilesAfter)
txtMilesAfter.grid(row=2,column=1)
lb1Make=Label(LeftMayFrame2,font=('arial',11,'bold'),text="MAKE",bd=8)
lb1Make.grid(row=2,column=2,sticky=W)
txtMake=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="MAKE",bd=8,width=31,justify='left',textvariable=Make)
txtMake.grid(row=2,column=3)
lb1Model=Label(LeftMayFrame2,font=('arial',11,'bold'),text="MODEL",bd=8)
lb1Model.grid(row=2,column=4,sticky=W)
txtModel=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="TOTAL",bd=8,width=31,justify='left',textvariable=Model)
txtModel.grid(row=2,column=5)
lb1EngineMade=Label(LeftMayFrame2,font=('arial',11,'bold'),text="ENGINE MADE",bd=8)
lb1EngineMade.grid(row=3,column=0,sticky=W)
txtEngineMade=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="ENGINE MADE",bd=8,width=31,justify='left',textvariable=EngineMade)
txtEngineMade.grid(row=3,column=1)
lb1CarColour=Label(LeftMayFrame2,font=('arial',11,'bold'),text="CAR COLOUR",bd=8)
lb1CarColour.grid(row=3,column=2,sticky=W)
txtCarColour=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="CAR COLOUR ",bd=8,width=31,justify='left',textvariable=CarColour)
txtCarColour.grid(row=3,column=3)
lb1CarInsurance=Label(LeftMayFrame2,font=('arial',11,'bold'),text="CAR INSURANCE",bd=8)
lb1CarInsurance.grid(row=3,column=4,sticky=W)
txtCarInsuramce=Entry(LeftMayFrame2,font=('arial',11,'bold'),text="CAR INSURANCE ",bd=8,width=31,justify='left',textvariable=CarInsurance)
txtCarInsuramce.grid(row=3,column=5)
#----------------------------------------LeftMayFrame3-----------------------------------------------------
lb1CustomerID=Label(LeftMayFrame3,font=('arial',11,'bold'),text="CUSTOMER ID",bd=8)
lb1CustomerID.grid(row=0,column=0,sticky=W)
txtCustomerId=Entry(LeftMayFrame3,font=('arial',11,'bold'),text="CUSTOMER ID",bd=8,width=31,justify='left',textvariable=var1)
txtCustomerId.grid(row=0,column=1)


lb1DaysRented=Label(LeftMayFrame3,font=('arial',11,'bold'),text="DAYS RENTED",bd=8)
lb1DaysRented.grid(row=0,column=2,sticky=W)
txtDaysRented=Entry(LeftMayFrame3,font=('arial',11,'bold'),text="CUSTOMER ID",bd=8,width=31,justify='left',textvariable=DaysRented)
txtDaysRented.grid(row=0,column=3)


lb1Discount=Label(LeftMayFrame3,font=('arial',11,'bold'),text="DISCOUNT",bd=8)
lb1Discount.grid(row=0,column=4,sticky=W)
txtDiscount=Entry(LeftMayFrame3,font=('arial',11,'bold'),text="DISCOUNT",bd=8,width=31,justify='left',textvariable=Discount)
txtDiscount.grid(row=0,column=5)

lb1NumberOfDays=Label(LeftMayFrame3,font=('arial',11,'bold'),text="NUMBER OF DAYS",bd=8)
lb1NumberOfDays.grid(row=1,column=0,sticky=W)
txtNumberOfDays=Entry(LeftMayFrame3,font=('arial',11,'bold'),text="NUMBER OF DAYS",bd=8,width=31,justify='left',textvariable=NumberOfDays)
txtNumberOfDays.grid(row=1,column=1)

lb1InvoiceId=Label(LeftMayFrame3,font=('arial',11,'bold'),text="INVOICE ID",bd=8)
lb1InvoiceId.grid(row=1,column=2,sticky=W)
txtInvoiceId=Entry(LeftMayFrame3,font=('arial',11,'bold'),text="INVOICE ID",bd=8,width=31,justify='left',textvariable=var2)
txtInvoiceId.grid(row=1,column=3)

lb1Total=Label(LeftMayFrame3,font=('arial',11,'bold'),text="TOTAL",bd=8)
lb1Total.grid(row=1,column=4,sticky=W)
txtTotal=Entry(LeftMayFrame3,font=('arial',11,'bold'),text="TOTAL",bd=8,width=31,justify='left',textvariable=Total)
txtTotal.grid(row=1,column=5)





#--------------------------------------------------LeftMayFrame4-----------------------------------------------
btnTotal=Button(LeftMayFrame4,text='TOTAL',padx=4,pady=4,bd=16,fg="black",font=('arial',11,'bold'),width=20,height=1,command=CarRentalCost)
btnTotal.grid(row=0,column=0)
btnReceipt=Button(LeftMayFrame4,text='RECEIPT',padx=4,pady=4,bd=16,fg="black",font=('arial',11,'bold'),width=20,height=1,command=Receipt)
btnReceipt.grid(row=0,column=1)
btnReset=Button(LeftMayFrame4,text='RESET',padx=4,pady=4,bd=16,fg="black",font=('arial',11,'bold'),width=20,height=1,command=Reset)
btnReset.grid(row=0,column=2)
btnExit=Button(LeftMayFrame4,text='EXIT',padx=4,pady=4,bd=16,fg="black",font=('arial',11,'bold'),width=20,height=1,command=uExit)
btnExit.grid(row=0,column=3)







t.mainloop()
