from tkinter import*
import tkinter as tk
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
import sqlite3
import time
import datetime as dtl
from PIL import ImageTk,Image
from billingcode import billing

class billingcodeX(billing):
    def billing():
        root=tk.Toplevel()
        b=billing(root)
        b.billing1()
        
#view4_:Are check database data of items
class view4_:
    def se_arch():
        s=s_entry.get()
        query1=(''' SELECT CODE,ITEM,QUANTITY,PRICE,GST,TOTALPRICE FROM ITEM_STORE WHERE CODE=?''')
        cursor.execute(query1,(s,))
        road=cursor.fetchall()
        Tree.delete(*Tree.get_children())
        for i in road:
            Tree.insert("",index=0,values=road[0])
    def re_fresh():
        Tree.delete(*Tree.get_children())
        query2=('''SELECT  CODE,ITEM,QUANTITY,PRICE,GST,TOTALPRICE FROM ITEM_STORE''')
        biger=datab.execute(query2)
        datab.commit()
        for retry in biger:
            Tree.insert("",'end',iid=retry[0],values=retry)
    def backend():
        view4.destroy()
        view3_.items()
    def deleter():
        selected=Tree.selection()
        query=('''DELETE FROM ITEM_STORE WHERE CODE=?''')
        #delete from item_store where code=%s
        datab.execute(query,(selected))
        datab.commit()
        Tree.delete(selected)
        messagebox.showerror("Info","  Data Deleted in DB!!! ")
    def next_up():
        view3.destroy()
        global view4
        view4=Tk()
        view4.geometry("700x630")
        view4.resizable(height="False",width="False")
        view4.pack_propagate(False)
        view4.title("Database View List")
        frame6_1=Frame(view4,highlightbackground="olive", highlightthickness=3, relief="raised")
        frame6_1.pack(side=TOP,fill=X)
        frame6_1.config(bg="darkcyan")
        head=Label(frame6_1,text= "DATABASE VIEW LIST",font=("arial" , "20"),bg="darkcyan",fg="black")
        head.pack(fill=X,side=TOP)
        frame6= Frame(view4, highlightbackground="olive", highlightthickness=3, relief="raised")
        frame6.pack(side=TOP,fill=X)
        frame6.config(bg="darkturquoise")
        s_label=Label(frame6,text="ITEM CODE :",font=("arial", 20), fg="black", bg="darkturquoise")
        s_label.pack(side=LEFT,fill=X,ipadx=1,ipady=1,padx=1,pady=1)
        global s_entry
        s_entry=Entry(frame6, width=25, font=("arial", 20), fg="black", bg="thistle")
        s_entry.pack(side=LEFT,fill=X,ipadx=5,ipady=1,padx=5,pady=1)
        search=Button(frame6,text="SEARCH",width=10,height=1,font=("arial",18),fg="black",bg="teal",activebackground="brown",activeforeground="black",command=view4_.se_arch)
        search.pack(side=RIGHT,fill=X,ipadx=1,ipady=1,padx=5,pady=1)
        #treeview:
        global Tree
        Tree= ttk.Treeview(view4)
        Tree.pack(fill=X,side=TOP,ipadx=0,ipady=90)
        Tree.configure(selectmode="extended")
        #scrollbar:
        scrolly=Scrollbar(Tree,orient=VERTICAL)
        scrolly.pack(side=RIGHT,fill=Y,ipadx=0,ipady=100)
        #scrolly.place(relx=0.002,rely=0.922,width=651,height=22)
        Tree.configure(yscrollcommand=scrolly.set)
        scrolly.configure(command=Tree.yview)
        Tree["columns"] = ("CODE", "ITEM", "QUANTITY", "PRICE", "GST%", "TOTAL PRICE")
        #allignment:
        Tree.column("#0", width=0, stretch=NO)
        Tree.column("#1", width=20)
        Tree.column("#2", width=30)
        Tree.column("#3", width=20)
        Tree.column("#4", width=30)
        Tree.column("#5", width=25, )
        Tree.column("#6", width=30)
        #headling text
        Tree.heading("#0", text="")
        Tree.heading("#1", text="CODE")
        Tree.heading("#2", text="ITEM")
        Tree.heading("#3", text="QUANTITY")
        Tree.heading("#4", text="PRICE")
        Tree.heading("#5", text="GST%")
        Tree.heading("#6", text="TOTAL PRICE")
        query=('''SELECT  CODE,ITEM,QUANTITY,PRICE,GST,TOTALPRICE FROM ITEM_STORE''')
        global big 
        big=datab.execute(query)
        for read in big:
            Tree.insert("",'end',iid=read[0],values=(read[0],read[1],read[2],read[3],read[4],read[5]))
        frame6_2=Frame(view4,highlightbackground="khaki", highlightthickness=3, relief="raised")
        frame6_2.pack(side=TOP,fill=X)
        frame6_2.config(bg="cadetblue")
        back1=Button(frame6_2,text="Back",width=10,height=7,font=("arial",18),fg="black",bg="rosybrown",activebackground="magenta",activeforeground="indigo",command=view4_.backend)
        back1.pack(side=LEFT,fill=X,padx=50,pady=15)
        refresh=Button(frame6_2,text="Refresh",width=10,height=7,font=("arial",18),fg="black",bg="teal",activebackground="springgreen",activeforeground="maroon",command=view4_.re_fresh)
        refresh.pack(side=LEFT,fill=X,padx=20,pady=15)
        #back1.pack(side=LEFT,fill=X,ipadx=1,ipady=1,padx=1,pady=30)
        deletedb=Button(frame6_2,text="DeleteDB",width=10,height=7,font=("arial",18),fg="black",bg="tomato",activebackground="deeppink",activeforeground="aliceblue",command=view4_.deleter)
        #deletedb.pack(side=RIGHT,fill=X,ipadx=30,ipady=1,padx=5,pady=30)
        deletedb.pack(side=RIGHT,fill=X,padx=50,pady=15)
#view3_:new items adding view
class view3_:
    def delete_all():
        select=myTree.selection()
        myTree.delete(select)
        messagebox.showerror("Info","  Data Deleted!!! ")
    def update_all():
        if co_entry.get()=="" or it_entry.get()==""or price_entry.get()==""or quantity_entry.get()==""or gst_entry.get()=="" or total_entry.get()=="" :
                messagebox.showerror("ERROR"," Please!!!'Fill The All Details' ")
        else:
            query2=(''' SELECT CODE FROM ITEM_STORE ''')
            Try=datab.execute(query2)
            datab.commit()
            global tyre
            tyre=[]
            for Trye in Try:
                tyre.append(Trye[0])
            d=int(co_entry.get())
            i=0
            for i in range(0,len(tyre)):
                if(d==tyre[i]):
                    messagebox.showinfo("update","Already Exists The CODE")
            try:
                def insert(CODE, ITEM, QUANTITY, PRICE, GST, TOTALPRICE):
                    datab.execute(''' INSERT INTO ITEM_STORE(CODE,ITEM,QUANTITY,PRICE,GST,TOTALPRICE) VALUES(?,?,?,?,?,?)'''
                              , (CODE, ITEM, QUANTITY, PRICE, GST, TOTALPRICE))
                    datab.commit()
                tree=insert(co_entry.get(),it_entry.get(),quantity_entry.get(),price_entry.get(),gst_entry.get(),total_entry.get())
                messagebox.showinfo("Info","Data Sucessfully Update")
                myTree.insert("",index=0,values=( ("\t   "+co_entry.get()),("\t   "+it_entry.get()),("\t   "+quantity_entry.get()),("\t   "+price_entry.get()),("\t   "+gst_entry.get()),("\t   "+total_entry.get())))
            except Exception as a:
                print(a)
            
    def total_():
        if co_entry.get()=="" or it_entry.get()==""or price_entry.get()==""or quantity_entry.get()==""or gst_entry.get()=="" :
            messagebox.showerror("ERROR"," Please!!!'Fill The All Details' ")
        else:
            total_entry.delete(0,END)
            price=int(price_entry.get())
            quantity=int(quantity_entry.get())
            gst=int(gst_entry.get())
            s_total=price*quantity
            n_total=(gst/100)*s_total
            n=n_total+s_total
            n1=float(n)
            total_entry.insert(0,n1)
        
    def back_up():
        view3.destroy()
        #view3_.manage()
        
    def clear_():
        co_entry.delete(0,'end')
        it_entry.delete(0,END)
        price_entry.delete(0,END)
        quantity_entry.delete(0,END)
        gst_entry.delete(0,END)
        total_entry.delete(0,END)
    def buttons(view3_3):
        frame3 = Frame(view3_3, highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        frame3.pack(fill=X, side=TOP)
        frame3.config(bg="aquamarine")
        BACK = Button(frame3, text="BACK", font=("arial", 20), fg="black", bg="burlywood", padx=10, pady=10,activebackground="indigo",activeforeground="lime",command=view3_.back_up).grid(row=3, column=0, padx=60, pady=18)
        update = Button(frame3, text="UPDATE", font=("arial", 20), fg="black", bg="royalblue", padx=10, pady=10,activebackground="aqua",activeforeground="navy",command=view3_.update_all).grid(row=3, column=2, padx=40, pady=18)
        clear_lab = Button(frame3, text="CLEAR", font=("arial", 20), fg="black", bg="royalblue", padx=10, pady=10,activebackground="red",activeforeground="darkslategray",command=view3_.clear_).grid(row=3, column=3, padx=40, pady=18)
        delete = Button(frame3, text="DELETE", font=("arial", 20), fg="black", bg="royalblue", padx=10, pady=10,activebackground="firebrick",activeforeground="navy",command=view3_.delete_all).grid(row=3, column=5, padx=40, pady=18)
        total = Button(frame3, text="TOTAL", font=("arial", 20), fg="black", bg="royalblue", padx=10, pady=10,activebackground="yellow",activeforeground="teal",command=view3_.total_).grid(row=3, column=7, padx=40, pady=18)
        next_page = Button(frame3, text="NEXT", font=("arial", 20), fg="black", bg="burlywood", padx=10, pady=10,activebackground="midnightblue",activeforeground="ghostwhite",command=view4_.next_up).grid(row=3, column=9, padx=40, pady=18)
        
        
    
    def Entry(view3_2):
        global  co_entry,it_entry,price_entry,quantity_entry,gst_entry,total_entry
        frame2 = Frame(view3_2, highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        frame2.pack(fill=X, side=TOP)
        frame2.config(bg="cadetblue")
#filling        
        code =  Label(frame2, text="CODE:", font=("arial", 20), fg="black", bg="cadetblue").grid(row=0, column=0, padx=10, pady=30)
        co_entry = Entry(frame2, width=10, font=("arial", 20), fg="navy", bg="paleturquoise")
        #co_entry.insert(0,"675")
        co_entry.grid(row=0, column=1, padx=10, pady=30)
        item = Label(frame2, text="ITEM :", font=("arial", 20), fg="black", bg="cadetblue").grid(row=0, column=2, padx=60, pady=15)
        it_entry = Entry(frame2, width=15, font=("arial", 20), fg="navy", bg="paleturquoise")
        it_entry.grid(row=0, column=3, padx=10, pady=15)
        price = Label(frame2, text="RATE :", font=("arial", 20), fg="black", bg="cadetblue").grid(row=0, column=4, padx=60, pady=15)
        price_entry = Entry(frame2,width=15, font=("arial", 20), fg="navy", bg="paleturquoise")
        price_entry.grid(row=0, column=5, padx=10, pady=15)
        quantity = Label(frame2, text="QUANTITY:", font=("arial", 20), fg="black", bg="cadetblue").grid(row=1, column=0, padx=40, pady=15)
        quantity_entry = Entry(frame2,width=10, font=("arial", 20), fg="navy", bg="paleturquoise")
        quantity_entry.grid(row=1, column=1, padx=10, pady=30)
        gst = Label(frame2, text="GST:", font=("arial", 20), fg="black", bg="cadetblue").grid(row=1, column=2, padx=60, pady=15)
        gst_entry = Entry(frame2, width=15, font=("arial", 20), fg="navy", bg="paleturquoise")
        gst_entry.grid(row=1, column=3, padx=10, pady=15)
        total = Label(frame2, text="TOTAL:", font=("arial", 20), fg="black", bg="cadetblue").grid(row=1, column=4, padx=60, pady=15)
        total_entry = Entry(frame2,width=15, font=("arial", 20), fg="navy", bg="paleturquoise")
        total_entry.grid(row=1, column=5, padx=10, pady=15)
        view3_.buttons(view3_2)

        
    def tree(view3_1):
#for items view in Tree entry boxes
#fix the columns;
        global myTree
        myTree= ttk.Treeview(view3_1)
        myTree.pack(fill=X)
        myTree.configure(selectmode="extended")
#scrollbar 
        scrollbary=Scrollbar(myTree,orient=VERTICAL)
        scrollbary.pack(side=RIGHT,fill=Y,ipadx=0,ipady=100)
        #scrolly.place(relx=0.002,rely=0.922,width=651,height=22)
        myTree.configure(yscrollcommand=scrollbary.set)
        scrollbary.configure(command=myTree.yview)
#treeview:
        myTree["columns"] = ("CODE", "ITEM", "QUANTITY", "PRICE", "GST%", "TOTAL PRICE")
#allignment:
        myTree.column("#0", width=0, stretch=NO)
        myTree.column("#1", width=20)
        myTree.column("#2", width=30)
        myTree.column("#3", width=20)
        myTree.column("#4", width=30)
        myTree.column("#5", width=25, )
        myTree.column("#6", width=30)
#headling text
        myTree.heading("#0", text="")
        myTree.heading("#1", text="CODE")
        myTree.heading("#2", text="ITEM")
        myTree.heading("#3", text="QUANTITY")
        myTree.heading("#4", text="PRICE")
        myTree.heading("#5", text="GST%")
        myTree.heading("#6", text="TOTAL PRICE")
       
        #obj.function
        view3_.Entry(view3_1)
    def time1_date():
        Time1=time.strftime("%H:%M:%S")
        Times1.config(text=Time1)
        Times1.after(200,view3_.time1_date)
    def items():
        global view3
        view3=tk.Toplevel()
        view3.title("ITEMS REGSITER")
        view3.geometry("1400x700")
        frameshead=Frame(view3, highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        frameshead.pack(side=TOP,fill=X)
        headimg=PhotoImage(file="C:\\Users\\Admin\\Desktop\\live project_py\\fancy5.png")
        headima=Label(frameshead,image=headimg,width=650,height=80)
        headima.image=headimg
        headima.pack(side=LEFT,fill=X)
        headimg1=PhotoImage(file="C:\\Users\\Admin\\Desktop\\live project_py\\fancy2.png")
        headima1=Label(frameshead,image=headimg1,width=1080,height=80)
        headima1.image=headimg1
        headima1.pack(side=LEFT,fill=X)
        #view3.resizable(height="False",width="False")
        frame1 = Frame(view3, highlightbackground="olive", highlightthickness=3)
        frame1.pack(side=TOP,fill=X)
        frame1.config(bg="mediumturquoise")
        global Times1
        Times1=Label(frame1,font=("arial",20),fg="black",bg="mediumturquoise")
        view3_.time1_date()
        Times1.pack(side=LEFT,padx=7)
        headling = Label(frame1, text="SOFTWARE FOR REGISTRATION THE ITEMS", font=("arial", 25,"bold"), fg="midnightblue", bg="mediumturquoise")
        #headling.grid(row=0, columns=1,padx=50)
        headling.pack(side=LEFT,fill=X,padx=180)
        date1=dtl.datetime.now()
        Date1=Label(frame1,text=f"{date1:%D}",font=("arial",25,),fg="navy",bg="mediumturquoise")
        Date1.pack(side=RIGHT,ipadx=20)
        view3_.tree(view3)
        #obj.call function with arguments
#view_2 management view
class view_2:
    def cl_ose():
        view1.destroy()
    def manage():
        global view1
        view1 = Tk()
        view1.title("HOME PAGE")
        view1.geometry("400x200")
        background = "cadetblue"
        #view1.iconbitmap("favicon.ico")
        view1.config(bg=background)
        my_font1=Font(family="arial",size=20,weight="bold",underline=1,)
        man_age = Label(view1, text="MANAGEMENT SYSTEM", font=my_font1, bg="cadetblue", fg="black").place(x=65,y=5)
        bil_ling= Button(view1, text="BILLING", font=("Helvetica", "18"), bg="teal", fg="black",activebackground="springgreen",activeforeground="darkred",command=billingcodeX.billing).pack(side=LEFT, fill=X, ipadx=30, ipady=5, padx=20, pady=20)
        item_s= Button(view1, text="ITEMS", font=("Helvetica", "18"), bg="teal", fg="black",activebackground="purple",activeforeground="thistle",command=view3_.items).pack(side=RIGHT, fill=X, ipadx=30, ipady=5, padx=20, pady=20)
        Admin=Button(view1,text="ADMIN",font=("Helvetica", "18"),bg="teal",fg="black",activebackground="blue",activeforeground="black").place(x=160,y=140)
        back_=Button(view1,text="X",font=("arial","15"),bg="firebrick",fg="black",activebackground="darkblue",activeforeground="white",command=view_2.cl_ose).place(x=2,y=2)
#view_1login page:
class view_1:
    def clear():
        u_entry.delete(0,'end')
        p_entry.delete(0,'end')
#database connection view
class database1:
    def check1():
        global datab
        #global cursor
        datab=sqlite3.connect("login1.db")
        global cursor
        cursor=datab.cursor()
        cursor.fetchall()
        cursor.execute((''' SELECT * FROM my_login1 WHERE USERNAME=? AND PASSWORD=? '''),(u_entry.get() ,p_entry.get()))
        row=cursor.fetchall()
        if row:
            messagebox.showinfo(title="login",message="Login Successfully")
            view.destroy()
            view_2.manage()
        else:
            messagebox.showinfo(title="login",message="Login Denied")
#login page
background="mediumpurple"
view=Tk()
view.title("Application")
view.geometry("280x220")
view.resizable(height="False",width="False")
view.pack_propagate(False)
my_font=Font(family="Helvetica",size=15,weight="bold",underline=1)
top_1=Label (view,text="SREE-FANCY",font=my_font,bg="mediumpurple",fg="black").pack()
login_txt2=Label(view, text= "LOGIN FORM", font=("Helvetica" , "17"),bg="mediumpurple",fg="black").pack()
view.config(bg="mediumpurple")
frame1=Frame(view)
frame1.pack(side= TOP , fill=X)
frame1.config(bg="mediumpurple")
user_name1=Label(frame1,text= "username:",font=("arial" , "15"),bg="mediumpurple",fg="black",padx=10,pady=0).grid(row=1,sticky=W)
u_entry=Entry(frame1,bg="paleturquoise",fg="black")
u_entry.insert(0,"hari")
u_entry.grid(row=1,column=1)
pass_word1=Label(frame1,text="password:",font=("arial" , "15"),bg="mediumpurple",fg="black",padx=10,pady=0).grid(row=2,sticky=W)
p_entry=Entry(frame1, show="*",bg="paleturquoise",fg="black")
p_entry.insert(0,"3016")
p_entry.grid(row=2,column=1)
login_button=Button(view, text="login",font=("arial", "17"),bg="yellowgreen",fg="black",activebackground="fuchsia",activeforeground="midnightblue",command=database1.check1).pack(side=RIGHT,fill=X,ipadx=25,ipady=5,padx=20,pady=20)
#login_button.pack(anchor=E,padx=30,pady=20)
clear_up=Button(view,text="clear",font=("arial", "17"),bg="crimson",fg="black",activebackground="red",activeforeground="black",command=view_1.clear).pack(side=LEFT,fill=X,ipadx=25,ipady=5,padx=20,pady=20)
#clear_up.pack(anchor=W,padx=30,pady=20)

mainloop()


'''
##################################################
if(delete to database):
query=( DELETE FROM ITEM_STORE WHERE CODE=?)
            #delete from item_store where code=%s
        de=datab.execute(query,(select,))
        datab.commit()
            messagebox.showerror("Info"," Deleted in DB!!! ")
#        widget admin to permaneny to allocate compulsary
  #      update function or edit on dbase
        

#######################################################
def clear_item():
        print(" r")
        #codex.delete(0END)
        #codex=IntVar()
        #codex.delete(0,END)
        #c.destroy()
      #  c.replace(" ")
        #c.delete(0,END)
        print()
        #itemx.delete("0","end")
      #  pricex.delete("0","end")
        #gstx.delete("0","end")
       # quantityx.delete("0","end")
      #  totalx.delete("0","end")
        print("h")
big=datab.execute( SELECT  CODE,ITEM,QUANTITY,PRICE,GST,TOTALPRICE FROM ITEM_STORE)
            for record in big:
                h=list(record[0])
                print(h)
scroll=ttk.Scrollbar(view3_1,orient="vertical")
        myTree.configure(command=myTree.yview)
        scroll.configure(Yscrollcommand=scroll.set)
        scroll.pack(fill=y,side=RIGHT)'''
      
################################try of image insert in tkinter ######################
############error is :pyimage doesn't exsits:solution in below of that error###################
'''Root=tk.Toplevel()
        Root.title("hello")
        Root.geometry("1400x700")
        Root.resizable(height="True", width="True")
        #frames1 = Frame(Root, highlightbackground="goldenrod", highlightthickness=3, relief="raised")
        #frames1.pack(side=TOP, fill=X)
        #bou=Button(Root,text="click",fg="black",bg="green")
        #bou.pack(side=TOP,fill=X)
        img=PhotoImage(file="C:\\Users\\Admin\\Desktop\\duplicate project\\flowers.png")
        ima =Label(Root, image=img,width=400,height=300)
        ima.image=img
        ima.place(x=100,y=0)
        
            #canvas=Canvas(Root,width=500,height=300,bg="blue")
            
            #img=PhotoImage(file="C:\\Users\\Admin\\Desktop\\duplicate project\\flowers.png")
            #canvas.create_image(0,0,image=img,anchor=NW)
            #canvas.pack()
            #img=ImageTk.PhotoImage(Image.open("duplicate project/flowers.png"))
        #img=PhotoImage(name="image_1",file="duplicate project//flowers.png")
        #ima.pack(side=TOP, fill=X)
img1=Image.open("C:\\Users\\Admin\\Desktop\\live project_py\\fancy3.jpg")
        self.bg=ImageTk.PhotoImage(img1)
        
'''  

