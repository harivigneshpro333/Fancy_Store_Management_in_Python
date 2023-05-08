from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import datetime as dt
import time
import os
import sqlite3
import tkinter as tk
from tkinter import messagebox
import msg

#billing 
class billing:
    def bil_search(self):
        self.id=int(self.searchbillentry.get())
        def read_the_File(fileex):
            try:
                file1=open(fileex,"r")
                file1.close
                #view=file1.readline()
                self.textbill.delete('1.0','end')
                for lines in file1:
                    self.textbill.insert('end',lines)
            except Exception as v:
                print("read_the_File",v)
        def read_blob_data(empid):
            try:
                self.sqlite=sqlite3.connect("login1.db")
                self.cursor=self.sqlite.cursor()
                self.readquery='''SELECT * FROM BILLING_STORE WHERE BILLNO=? '''
                self.cursor.execute(self.readquery,(empid,))
                self.record=self.cursor.fetchall()
                rows=[]
                for row in self.record:
                    rows+=row
                self.exportfile=rows[6]
                self.cursor.close()
                read_the_File(self.exportfile)
            except Exception as m:
                messagebox.showerror("Error","File Is Not Found.......")
                print("read_blob_data",m)
        read_blob_data(self.id)
    def billview_print(self):
        try:
            self.reviewnum=(str(self.searchbillentry.get())+".txt")
            os.startfile(self.reviewnum,"print")
        except Exception as j:
            messagebox.showerror("Error","File in Exception")
            print("billview_print",J)
            
        
    def exit(self):
        self.bill_page.destroy()
    def bill_view(self):
        try:
            self.bill_page=Tk()
            self.bill_page.geometry("600x700")
            self.bill_page.title("Bill View")
            self.bill_page.pack_propagate(False)
            self.bill_page.resizable(height="False",width="False")
            self.headFrame=Frame(self.bill_page,highlightbackground="goldenrod", highlightthickness=2, relief="raised")
            self.headFrame.pack(side=TOP,fill=X)
            self.headFrame.config(bg="teal")
            self.searchframe=Frame(self.bill_page,highlightbackground="goldenrod", highlightthickness=2, relief="raised")
            self.searchframe.config(bg="mediumturquoise")
            self.searchframe.pack(side=TOP,fill=X)
            self.heading=Label(self.headFrame,text= "BILL  REVIEW",font=("arial" , "20"),bg="teal",fg="black")
            self.heading.pack(fill=X,side=TOP)
            self.bill_label=Label(self.searchframe,text="BIll NO :",font=("arial", 20), fg="black", bg="mediumturquoise")
            self.bill_label.pack(side=LEFT,fill=X,ipadx=1,ipady=1,padx=1,pady=1)
            self.searchbillentry=Entry(self.searchframe, width=18, font=("arial", 20), fg="black", bg="thistle")
            self.searchbillentry.pack(side=LEFT,fill=X,ipadx=5,ipady=1,padx=5,pady=1)
            self.bill_search=Button(self.searchframe,text="SEARCH",width=10,height=1,font=("arial",18),fg="black",bg="teal",activebackground="brown",activeforeground="black",command=d.bil_search)
            self.bill_search.pack(side=RIGHT,fill=X,ipadx=1,ipady=1,padx=5,pady=1)
            self.reviewfra=LabelFrame(self.bill_page,text="Review",font=("arial",25),fg="purple")
            self.reviewfra.config(bg="teal")
            self.reviewfra.pack(side=TOP,fill=X)
            self.scrollbar_y=Scrollbar(self.reviewfra,orient=VERTICAL)
            self.textbill=Text(self.reviewfra,font=("times new romans",15),fg="purple",bg="thistle",width=50,height=20,yscrollcommand=self.scrollbar_y.set)
            self.scrollbar_y.pack(side=RIGHT,fill=Y)
            self.scrollbar_y.config(command=self.textbill.yview)
            self.textbill.pack(pady=5)
            self.bottomframe=Frame(self.bill_page,highlightbackground="teal", highlightthickness=3, relief="raised")
            self.bottomframe.config(bg="cornflowerblue")
            self.bottomframe.pack(side=BOTTOM,fill=X)
            self.bottom_back=Button(self.bottomframe,text="Back",font=("arial",10,'bold'),fg="black",bg="mediumslateblue",activebackground="aliceblue",activeforeground="black",height=3,width=16,command=d.exit)
            self.bottom_back.pack(side=LEFT,padx=60,pady=10)
            self.preview_pri=Button(self.bottomframe,text="Print Preview",font=("arial",10,'bold'),fg="black",bg="mediumslateblue",activebackground="aliceblue",activeforeground="black",height=3,width=20,command=d.billview_print)
            self.preview_pri.pack(side=RIGHT,padx=50,pady=10)
   
                
        except Exception as l:
            print("bill_view",l)
                
        
        
        
    def back_bill(self):
        self.page.destroy()
    def print_preview(self):
        try:
            self.filename=str(self.fileentry.get())
#get the value from Text label in end to end Text values by using code in below:
            self.create=self.textarea.get('1.0','end-1c')
    #crete the file new and write by using file handling
            self.file=open(self.filename,"x")
            self.file.write(self.create)
            self.file.close()
    #code to out print to printer 
            os.startfile(self.filename,"print")
        except Exception as a:
            messagebox.showerror("Error","File Already Exists")
            print("print_preview",a)
    def updateable(self):
        try:
#sql connect
            self.sql=sqlite3.connect("login1.db")
            self.cursor=self.sql.cursor()
            for results in self.tree_view.get_children():
                self.readtree=[]
                for values in self.tree_view.item(results)['values']:
                    self.readtree.append(values)
                self.Code=self.readtree[0]
                self.Qty=self.readtree[2]
                self.Query=('''SELECT * FROM ITEM_STORE WHERE CODE=?''')
                self.cursor.execute(self.Query,(self.Code,))
                self.Records=self.cursor.fetchall()
                self.dataval=[]
                for limits in self.Records:
                    self.dataval.append(limits)
                self.rowed=(self.dataval[0])
                if(self.rowed[2]<self.Qty):
                    self.error="Out Of Stock Code:",self.Code
                    messagebox.showerror("Error",self.error)
                else:
                    self.minus_db=((self.rowed[2])-self.Qty)
            
                    self.UpdateQue=('''UPDATE ITEM_STORE SET QUANTITY=? WHERE CODE=? ''')
                    self.cursor.execute(self.UpdateQue,(self.minus_db,self.Code,))
                    self.sql.commit()
                    #self.cursor.close()
                    messagebox.showinfo("Info","***UpdateSuccessfully***")
                    if(self.minus_db==0):
                        self.A="No Stock In Base....Code No:",self.Code
                        messagebox.showinfo("Info",self.A)
                        
                    
                    
                
                
                
        except Exception as w:
            print("updateable",w)

    def print_bills(self):
        if(self.mobileentry.get()=="" or self.nameentry.get()=="" or self.emailentry.get()=="" or self.totalentry.get()=="" or self.goventry.get()=="" or self.billentry.get()==""):
            messagebox.showerror("Error","Plz  Add all Details First Then Print")
        else:
            try:
                d.updateable()
                self.page=Tk()
                self.page.geometry("600x700")
                self.page.title("Bill Print")
                self.page.pack_propagate(False)
                self.page.resizable(height="False",width="False")
                self.billbutton=Button(self.page,text="BILL RECIEPT",font=("arial",10,'bold'),fg="black",bg="powderblue",activebackground="firebrick",activeforeground="lime",height=2)
                self.billbutton.pack(side=TOP,fill=X)
                self.billlabel=LabelFrame(self.page,text="Billing",font=("arial",25),fg="firebrick")
                self.billlabel.config(bg="powderblue")
                self.billlabel.pack(side=TOP,fill=X)
                self.billreciept=Label(self.billlabel,font=("arial",15),bg="powderblue",fg="purple")
                self.billreciept.configure(text="**********Welcome To Sree Fancy Store***********")
                self.billreciept.pack(side=TOP,fill=X)
                self.gstno=Label(self.billlabel,font=("arial",15),bg="powderblue",fg="purple")
                self.gstno.configure(text="*********GstNo:22ALRKX0000Z1G5************")
                self.gstno.pack(side=TOP,fill=X)
                self.scroll_y=Scrollbar(self.billlabel,orient=VERTICAL)
                self.textarea=Text(self.billlabel,width=50,height=20,yscrollcommand=self.scroll_y.set,bg="powderblue",fg="black",font=("times new romans",15))
                self.scroll_y.pack(side=RIGHT,fill=Y)
                self.scroll_y.config(command=self.textarea.yview)
                self.a=("*******************************Bill**********************************")
                self.b=("\nBill Number:"+str(self.billentry.get())+"\t\t\t\t"+"Date: "+str(self.Date['text']))
                self.c=("\nCustomer Name:"+str(self.nameentry.get())+"\t\t\t\t"+"Time: "+str(self.Times['text']))
                self.d=("\nPhone Number:"+str(self.mobileentry.get()))
                self.e=("\nCustomer Email:"+str(self.emailentry.get()))
                self.f=("\n********************************************************************")
                self.g=("\nProducts\t\t\tQty\t\tPrice")
                self.textarea.insert('end',self.a)
                self.textarea.insert('end',self.b)
                self.textarea.insert('end',self.c)
                self.textarea.insert('end',self.d)
                self.textarea.insert('end',self.e)
                self.textarea.insert('end',self.f)
                self.textarea.insert('end',self.g)
                self.textarea.insert('end',self.f)
                for result in self.tree_view.get_children():
                    self.billtree=[]
                    for value in self.tree_view.item(result)['values']:
                        self.billtree.append(value)
                    self.h=("\n"+str(self.billtree[1])+"\t\t\t"+str(self.billtree[2])+"\t\t"+str(self.billtree[3]))
                    self.textarea.insert('end',self.h)
                self.textarea.insert('end',self.f)
                self.alltotal=(int(self.totalentry.get())+float(self.goventry.get()))
                self.i=("\nSub Amount:"+"\t\t\t\tRs"+str(self.totalentry.get()))
                self.str=str(self.goventry.get())
                self.j=("\nTax Amount:"+"\t\t\t\tRs"+self.str[:6])
                self.totl=str(self.alltotal)
                self.k=("\nTotal Amount:"+"\t\t\t\tRs"+str(self.totl[:6]))
                self.l=("\n\n*************************Thank You*******************************")
                self.textarea.insert('end',self.i)
                self.textarea.insert('end',self.j)
                self.textarea.insert('end',self.k)
                self.textarea.insert('end',self.f)
                self.textarea.insert('end',self.l)
                self.textarea.pack(pady=5)
                self.bottomfra=Frame(self.page,highlightbackground="black", highlightthickness=3, relief="raised")
                self.bottomfra.config(bg="powderblue")
                self.bottomfra.pack(side=BOTTOM,fill=X)
                self.b_ack_=Button(self.bottomfra,text="Back",font=("arial",10,'bold'),fg="black",bg="mediumslateblue",activebackground="aliceblue",activeforeground="black",height=3,width=16,command=d.back_bill)
                self.b_ack_.pack(side=LEFT,padx=80,pady=10)
                self.fileentry=Entry(self.bottomfra,font=("arial",18,'bold'),fg="black",bg="mediumslateblue",width=12)
                self.adding=(str(self.billentry.get())+".txt")
                self.fileentry.insert('0',self.adding)
                self.fileentry.pack(side=LEFT,padx=2,pady=10,ipady=7)
                self.preview=Button(self.bottomfra,text="Print Preview",font=("arial",10,'bold'),fg="black",bg="mediumslateblue",activebackground="aliceblue",activeforeground="black",height=3,width=20,command=d.print_preview)
                self.preview.pack(side=RIGHT,padx=10,pady=10)
            except Exception as v:
                print("print_bills",v)
    
    def generate_bill(self):
        if(self.mobileentry.get()=="" or self.nameentry.get()=="" or self.emailentry.get()=="" or self.totalentry.get()=="" or self.goventry.get()=="" or self.billentry.get()==""):
            messagebox.showerror("Error","Plz  Add The Card First Then Generate Bill")
        else:
            try:
                self.billno_db=str(self.billentry.get())
                self.mobile_db=str(self.mobileentry.get())
                self.time_db=str(self.Times['text'])
                self.date_db=str(self.Date['text'])
                self.z=int(self.totalentry.get())+float(self.goventry.get())
                self.total_db=str(self.z)
                self.tax=str(self.goventry.get())
                self.tax_db=self.tax[:5]
                
                def converted_to_binarycode(filedirect):
                    with open (filedirect,"rb") as files:
                        blobdata=files.readlines()
                    return blobdata
                    
                def Input(BILLNO, MOBILENO, DATE, TIME, TAX, TOTAL,BILL):
                    self.cursor=self.databas.cursor()
                    self.inputquery=(''' INSERT INTO BILLING_STORE(BILLNO,MOBILENO,DATE,TIME,TAX,TOTAL,BILL) VALUES(?,?,?,?,?,?,?)''')
                    self.file_db=converted_to_binarycode(BILL)
                    data_tuple=(BILLNO, MOBILENO, DATE, TIME, TAX, TOTAL,BILL)
                    self.cursor.execute(self.inputquery,data_tuple)
                    self.databas.commit() 
                    self.cursor.close()
                self.filename_db=str(self.adding)
                self.mobileentry.delete(0,'end')
                self.nameentry.delete(0,'end')
                self.emailentry.delete(0,'end')
                self.totalentry.delete(0,'end')
                self.goventry.delete(0,'end')
                for items in self.tree_view.get_children():
                    self.tree_view.delete(items)
                messagebox.showinfo("Info","Bill Saved Sucessfully.......")
                Input(self.billno_db,self.mobile_db,self.date_db,self.time_db,self.tax_db,self.total_db,self.filename_db)
                '''msg.main()'''

            except Exception as x:
                print("generate_bill",x)
                
    
    def auto_fill(self):
        if(self.codelentry.get()==""):
            messagebox.showinfo("Error","If  U Want To Access Autofill, Do First Fill The Code")
        else:
            try:
                self.databas=sqlite3.connect("login1.db")
                self.cursor=self.databas.cursor()
                self.querylan=(''' SELECT CODE FROM ITEM_STORE ''')
                self.cursor.execute(self.querylan)
                self.Trys=self.cursor.fetchall()
                self.tyre=[]
                for self.Trye in self.Trys:
                    self.tyre.append(self.Trye[0])
                self.de=int(self.codelentry.get())
                self.i1=0
                self.fun=0
                for self.i1 in range(0,len(self.tyre)):
                    if(self.de!=self.tyre[self.i1]):
                        self.fun=self.fun+1
                if(self.fun==len(self.tyre)):
                    messagebox.showerror("Searching","Code Is Not Exists")
                else:
                    self.s=self.codelentry.get()
                    self.query1=(''' SELECT CODE,ITEM,QUANTITY,PRICE,GST,TOTALPRICE FROM ITEM_STORE WHERE CODE=?''')
                    self.cursor.execute(self.query1,(self.s,))
                    self.road=self.cursor.fetchall()
                    self.way=list(self.road[0])
                    self.subentry.delete(0,"end")
                    self.productentry.delete(0,'end')
                    self.gst1entry.delete(0,'end')
                    self.subentry.insert(0,"Fancy Items")
                    self.productentry.insert(0,str(self.way[1]))
                    self.gst1entry.insert(0,int(self.way[4]))
                    self.profile=(self.way[3]*0.20)
                    self.profile1=int(self.profile+self.way[3])
                    self.priceentry.delete(0,'end')
                    self.priceentry.insert(0,self.profile1)
            except Exception as a:
                print("auto_fill",a)
        
    def delete_item(self):
        try:
            self.selected=self.tree_view.selection()
            self.msgbox=messagebox.askquestion("Item Cancel","Are u Sure To Canceled The Item?",icon="warning")
            if self.msgbox =="yes":
#take and the value in treeview
                self.curitem=self.tree_view.focus()
                self.det=self.tree_view.item(self.curitem)
                self.pro=self.det.get("values")[2:]
                self.qunty=self.pro[0]
                self.gov=self.pro[1]
                self.cost=self.pro[2]
#minus the deleted the selection item
                self.mul=0
                self.mul=self.qunty*self.cost
                self.totale1=self.totale1-self.mul
                self.govresult=(self.gov/100)*self.mul
                self.gsttol1=self.gsttol1-self.govresult
#delete and insert the remainder in entry
                self.totalentry.delete(0,'end')
                self.totalentry.insert(0,self.totale1)
                self.goventry.delete(0,'end')
                self.goventry.insert(0,self.gsttol1)
#deleted the treeview columns            
                self.tree_view.delete(self.selected)
                messagebox.showinfo("Msg","Item Canceled")
            else:
                messagebox.showinfo("Msg","Item Returned")
            if(self.totalentry.get()=="0"):
                self.goventry.delete(0,'end')
                self.totalentry.delete(0,'end')
        except Exception as d:
            messagebox.showerror("Error","Selected the Deleted Items First")
            print("delete_item",d)
    def addto(self):
        if(self.codelentry.get()=="" or self.subentry.get()=="" or self.productentry.get()=="" or self.priceentry.get()=="" or self.gst1entry.get()==""):
            messagebox.showerror("Error","Plz fill the item First")
        elif(self.qtyentry.get()==""):
            messagebox.showerror("Error","Plz Fill the Quantity Of Item")
        else:
            self.msgbox1=messagebox.askquestion("Confirmation ","Are u Sure To Add The Item?",icon="warning")
            if(self.msgbox1=="yes"):
                self.tree_view.insert("",index=0,values=(self.codelentry.get(),self.productentry.get(),self.qtyentry.get(),self.gst1entry.get(),self.priceentry.get()))
                self.price1=int(self.priceentry.get())
                self.Qty=int (self.qtyentry.get())
                self.gSt=int(self.gst1entry.get())
                self.totale=self.price1*self.Qty
                self.gstto=(self.gSt/100)
                self.gsttol=float(self.gstto*self.totale)
                self.codelentry.delete(0,'end')
                self.subentry.delete(0,'end')
                self.productentry.delete(0,'end')
                self.qtyentry.delete(0,'end')
                self.gst1entry.delete(0,'end')
                self.priceentry.delete(0,'end')
                self.totalentry.delete(0,'end')
                self.goventry.delete(0,'end')
                self.totale1=self.totale1+self.totale
                self.gsttol1=self.gsttol1+self.gsttol
                self.totalentry.insert(0,self.totale1)
                self.goventry.insert(0,self.gsttol1)
            else:
                messagebox.showinfo("Info","Returned To Billing ")
        
    def back_upbill(self):
        self.Root.destroy()
    def button_wid(self):
        self.buttonframe=Frame(self.Root,highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        self.buttonframe.config(bg="teal")
        self.buttonframe.pack(side=BOTTOM,fill=X)
        self.back_= Button(self.buttonframe, text="BACK", font=("Helvetica", "18"), bg="burlywood", fg="black",activebackground="steelblue",activeforeground="white",command=d.back_upbill)
        self.back_.grid(row=0,column=0,padx=40,pady=20,ipadx=20,ipady=8)
#view of total entry in the root
        self.totale1=0
        self.gsttol1=0
        self.add= Button(self.buttonframe, text="Add To Cart", font=("Helvetica", "18"), bg="mediumslateblue", fg="black",activebackground="lime",activeforeground="navy",command=d.addto)
        self.add.grid(row=0,column=1,padx=40,pady=20,ipadx=20,ipady=8)
        self.generate= Button(self.buttonframe, text="SAVE BILL", font=("Helvetica", "18"), bg="mediumslateblue", fg="black",activebackground="navy",activeforeground="cyan",command=d.generate_bill)
        self.generate.grid(row=0,column=2,padx=40,pady=20,ipadx=20,ipady=8)
        self.cl_ear= Button(self.buttonframe, text="Cancel Item", font=("Helvetica", "18"), bg="mediumslateblue", fg="black",activebackground="orangered",activeforeground="black",command=d.delete_item)
        self.cl_ear.grid(row=0,column=3,padx=40,pady=20,ipadx=20,ipady=8)
        self.print= Button(self.buttonframe, text="Print", font=("Helvetica", "18"), bg="mediumslateblue", fg="black",activebackground="navy",activeforeground="yellow",command=d.print_bills)
        self.print.grid(row=0,column=4,padx=40,pady=20,ipadx=10,ipady=8)
        self.billview= Button(self.buttonframe, text="Bill View", font=("Helvetica", "18"), bg="burlywood", fg="black",activebackground="lawngreen",activeforeground="firebrick",command=d.bill_view)
        self.billview.grid(row=0,column=5,padx=25,pady=20,ipadx=10,ipady=8)

        #self.but_ton.pack(side=LEFT, fill=X,padx=20, pady=20)
        
        
    def image(self):
        ima_ge=PhotoImage(file="C:\\Users\\Admin\\Desktop\\live project_py\\fancy2.png")
        self.im_age=Label(self.Root,image=ima_ge,width=410,height=205)
        self.im_age.image=ima_ge
        self.im_age.place(x=0,y=385)
#image 2
        ima_ge=PhotoImage(file="C:\\Users\\Admin\\Desktop\\live project_py\\fancy5.png")
        self.im_age=Label(self.Root,image=ima_ge,width=410,height=205)
        self.im_age.image=ima_ge
        self.im_age.place(x=412,y=385)
        d.treeview()
        

    def treeview(self):
        s=ttk.Style()
        s.configure('Treeview',rowheight=18)
        self.tree_view= ttk.Treeview(self.Root)
        self.tree_view.place(x=827,y=387)
        #self.tree_view.pack(side=RIGHT,fill=BOTH,padx=600,pady=0)
        #self.tree_view.pack(side=RIGHT,padx=360,pady=0)
        #self.tree_view.configure(selectmode="browse")
        #browse is not allowed multi selection in treeview#extended can exists multi selection
#scrollbar 
        self.scrol_lbary=ttk.Scrollbar(self.Root,orient=VERTICAL) 
        self.scrol_lbary.place(x=1350,y=388,height=200)
        self.tree_view.configure(yscrollcommand=self.scrol_lbary.set)
        self.scrol_lbary.configure(command=self.tree_view.yview)
        #self.scrol_lbary.pack(side=RIGHT,padx=515)
        #self.scrol_lbary.place(relx=0.002,rely=0.922,width=651,height=22)
#treeview:
        self.tree_view["columns"] = ("CODE", "ITEM", "QUANTITY","GST" ,"PRICE")
#allignment:
        self.tree_view.column("#0", width=0, stretch=NO)
        self.tree_view.column("#1", width=80)
        self.tree_view.column("#2", width=140)
        self.tree_view.column("#3", width=120)
        self.tree_view.column("#4", width=90)
        self.tree_view.column("#5", width=90)
#headling text
        self.tree_view.heading("#0", text="")
        self.tree_view.heading("#1", text="CODE")
        self.tree_view.heading("#2", text="ITEM")
        self.tree_view.heading("#3", text="QUANTITY")
        self.tree_view.heading("#4", text="GST") 
        self.tree_view.heading("#5", text="PRICE")
          #self.tree_view.pack(side=TOP,fill=X)
        d.button_wid()
    def last_bill(self):
        try:
            self.finder=sqlite3.connect("login1.db")
            self.cursor=self.finder.cursor()
            lastquery=''' SELECT BILLNO FROM BILLING_STORE '''
            self.cursor.execute(lastquery)
            self.rec=self.cursor.fetchall()
            self.cursor.close()
            for datas in self.rec:
                pass
            self.billentry.delete(0,'end')
            self.billentry.insert('end',datas)
        except Exception as b:
            print(b)
    def billingframe(self):
# display main frame
        self.billingframe=Frame(self.Root,highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        self.billingframe.config(bg="powderblue")
        self.billingframe.pack(side=TOP,fill=X)
        
#customer frame1
        self.customerid=LabelFrame(self.billingframe,text="Customer",font=("arial",25),fg="firebrick")
        self.customerid.config(bg="powderblue")
        self.customerid.pack(side=LEFT,padx=20,pady=20)
#customer mobile 
        self.mobile=Label(self.customerid,text="Mobile No:",font=("arial",15),fg="navy",bg="powderblue")
        self.mobile.grid(row=0,column=0,sticky=W,padx=10)
        self.mobileentry=Entry(self.customerid, width=10, font=("arial", 15), fg="black", bg="paleturquoise")
        self.mobileentry.grid(row=0,column=1,padx=20,pady=5)
#customer name     
        self.name=Label(self.customerid,text="Customer Name :",font=("arial",15),fg="navy",bg="powderblue")
        self.name.grid(row=1,column=0,sticky=W,padx=10)
        self.nameentry=Entry(self.customerid, width=10, font=("arial", 15), fg="black", bg="paleturquoise")
        self.nameentry.grid(row=1,column=1,padx=20,pady=5) 
#customer email
        self.email=Label(self.customerid,text="Email :",font=("arial",15),fg="navy",bg="powderblue")
        self.email.grid(row=2,column=0,sticky=W,padx=10)
        self.emailentry=Entry(self.customerid, width=10, font=("arial", 15), fg="black", bg="paleturquoise")
        self.emailentry.grid(row=2,column=1,padx=20,pady=5)
#product frame2
        self.product=LabelFrame(self.billingframe,text="Product",font=("arial",25),fg="firebrick",bg="powderblue")
        self.product.pack(side=LEFT,ipadx=50)
#code label and combo
        self.codel=Label(self.product,text="Code :",font=("arial",15),fg="navy",bg="powderblue")
        self.codel.grid(row=0,column=0,sticky=W,padx=10,pady=5)
        self.codelentry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.codelentry.grid(row=0,column=1,sticky=W,padx=10,pady=5) 
#subcatetory label and combo
        self.subcategory=Label(self.product,text="Sub Category:",font=("arial",15),fg="navy",bg="powderblue")
        self.subcategory.grid(row=1,column=0,sticky=W,padx=10,pady=5)
        self.subentry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.subentry.grid(row=1,column=1,sticky=W,padx=10,pady=5)
#productname label and combo:
        
        self.productna=Label(self.product,text="Product Name:",font=("arial",15),fg="navy",bg="powderblue")
        self.productna.grid(row=2,column=0,sticky=W,padx=10,pady=5)
        self.productentry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.productentry.grid(row=2,column=1,sticky=W,padx=10,pady=5)
        
#fill button:
        self.fill=Button(self.product,text="?",fg="black",bg="red",command=d.auto_fill)
        self.fill.grid(row=0,column=2)
#price label and combo:
        self.price=Label(self.product,text="Price :",font=("arial",15),fg="navy",bg="powderblue")
        self.price.grid(row=0,column=3,sticky=W,padx=2,pady=5)
        self.priceentry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.priceentry.grid(row=0,column=4,sticky=W,padx=10,pady=5)
#qty label and entry
        self.qty=Label(self.product,text="Qty :",font=("arial",15),fg="navy",bg="powderblue")
        self.qty.grid(row=1,column=3,sticky=W,padx=2,pady=5)
        self.qtyentry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.qtyentry.grid(row=1,column=4,sticky=W,padx=10,pady=5)
#gst label and entry:
        self.gst1=Label(self.product,text="Gst% :",font=("arial",15),fg="navy",bg="powderblue")
        self.gst1.grid(row=2,column=3,sticky=W,padx=2,pady=5)
        self.gst1entry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.gst1entry.grid(row=2,column=4,sticky=W,padx=10,pady=5)
       
# sub total label and entry
        self.subtotal=Label(self.product,text="Sub Total :",font=("arial",15),fg="navy",bg="powderblue")
        self.subtotal.grid(row=0,column=5,sticky=W,padx=10,pady=5)
        self.totalentry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.totalentry.grid(row=0,column=6,sticky=W,padx=10,pady=5)
#Gov tax label and entry
        self.govtax=Label(self.product,text="Gov Tax :",font=("arial",15),fg="navy",bg="powderblue")
        self.govtax.grid(row=1,column=5,sticky=W,padx=10,pady=5)
        self.goventry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.goventry.grid(row=1,column=6,sticky=W,padx=10,pady=5)
#bill no label and entry
        self.billlabel=Label(self.product,text="Bill No :",font=("arial",15),fg="navy",bg="powderblue")
        self.billlabel.grid(row=2,column=5,sticky=W,padx=10,pady=5)
        self.billentry=Entry(self.product,width=12,font=("arial",15),fg="black", bg="paleturquoise")
        self.billentry.grid(row=2,column=6,sticky=W,padx=10,pady=5)
        self.lastbill=Button(self.product,text="?",fg="white",bg="purple",command=d.last_bill)
        self.lastbill.grid(row=2,column=7)
        d.image()

        

        
        
    def time_date(self):
        Time=time.strftime("%H:%M:%S")
        self.Times.config(text=Time)
        #self.head.config(text="TIME:")
        self.Times.after(200,d.time_date)
    def frames_2(self):
        self.frames2=Frame(self.Root,highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        self.frames2.pack(side=TOP,fill=X)
        self.frames2.config(bg="darkcyan")
        self.time=Label(self.frames2,text="TIME:",font=("arial",20),fg="black",bg="darkcyan")
        self.time.pack(side=LEFT,ipadx=5)
        self.Times=Label(self.frames2,font=("arial",20),fg="darkblue",bg="darkcyan")
        d.time_date()
        self.Times.pack(side=LEFT,ipadx=7)
        self.heading=Label(self.frames2,text="BILLING SOFTWARE FOR SREE FANCY",font=("arial",30,"bold"),fg="black",bg="darkcyan")
        self.heading.pack(side=LEFT,ipadx=80)
        self.date=dt.datetime.now()
        self.Date=Label(self.frames2,text=f"{self.date:%D}",font=("arial",25,),fg="black",bg="darkcyan")
        self.Date.pack(side=RIGHT,ipadx=20)
        d.billingframe()
        
        
    def __init__(self,root):
        self.Root=root
    def billing1(self):
        self.Root.title("Billing Page")
        self.Root.geometry("1400x700")
        self.Root.resizable(height="True",width="True")
        self.frames1=Frame(self.Root, highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        self.frames1.pack(side=TOP,fill=X)
#image in frame
        img=PhotoImage(file="C:\\Users\\Admin\\Desktop\\live project_py\\fancy4.png")
        self.ima=Label(self.frames1,image=img,width=670,height=120)
        self.ima.image=img
        self.ima.pack(side=LEFT,fill=X)
        img2=PhotoImage(file="C:\\Users\\Admin\\Desktop\\live project_py\\fancy2.png")
        self.ima1=Label(self.frames1,image=img2,width=690,height=120)
        self.ima1.image=img2
        self.ima1.pack(side=LEFT,fill=X)
        global d
        d=billing(self.Root)
        d.frames_2()
        
'''def treeview(self):
        self.miniframe=self.Root
        self.treeframe=Frame(self.miniframe,highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        self.treeframe.pack(side=RIGHT,padx=40)
        self.tree_view= ttk.Treeview(self.treeframe)
        self.tree_view.pack(side=TOP,fill=X)
        self.tree_view.configure(selectmode="extended")
#scrollbar 
        self.scrol_lbary=Scrollbar(self.tree_view,orient=VERTICAL)
        self.scrol_lbary.pack(side=RIGHT,fill=Y,ipadx=0,ipady=100)
        #scrolly.place(relx=0.002,rely=0.922,width=651,height=22)
        self.tree_view.configure(yscrollcommand=self.scrol_lbary.set)
        self.scrol_lbary.configure(command=self.tree_view.yview)
#treeview:
        self.tree_view["columns"] = ("CODE", "ITEM", "QUANTITY", "PRICE")
#allignment:
        self.tree_view.column("#0", width=0, stretch=NO)
        self.tree_view.column("#1", width=20)
        self.tree_view.column("#2", width=30)
        self.tree_view.column("#3", width=20)
        self.tree_view.column("#4", width=30)
#headling text
        self.tree_view.heading("#0", text="")
        self.tree_view.heading("#1", text="CODE")
        self.tree_view.heading("#2", text="ITEM")
        self.tree_view.heading("#3", text="QUANTITY")
        self.tree_view.heading("#4", text="PRICE")
        self.tree_view.pack(side=TOP,fill=X)

'''





###################image insert  one of the method###########
#img=ImageTk.PhotoImage(Image.open("image/flowers.png"))
#img.resize((300,200),Image.LANCZOS)
#photo=ImageTk.PhotoImage(img)
'''print(self.billtree[:2])
        self.h=(str(self.billtree[0])+"\t\t\t"+str(self.billtree[1]+"\t\t"+str(self.billtree[2])))
        self.textarea.insert('end',self.h)
 
self.billreview=Button(self.bill_page,text="BILL REVIEW",font=("arial",10,'bold'),fg="black",bg="powderblue",activebackground="firebrick",activeforeground="lime",height=2)
            self.billreview.pack(side=TOP,fill=X)
            self.billnum=Label(self.searchframe,text="Bill No:",font=("arial",22,'bold'),fg="black",bg="teal")
            self.billnum.pack(side=LEFT,padx=5,pady=5)
            self.billnumentry=Entry(self.searchframe,font=("arial",20),fg="black",bg="powderblue",width=20)
            self.billnumentry.pack(side=LEFT,padx=30,pady=5,ipadx=10)
            self.searchButton=Button(self.searchframe,text="Search",font=("arial",20),fg="black",bg="powderblue",activebackground="navy",activeforeground="white")
            self.searchButton.pack(side=RIGHT,pady=5)'''      
