from tkinter import *
import random
import os
import sys
from tkinter import messagebox


class Bill_App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.configure(bg="#73A6D7")
        self.root.title("POS system - Point of Sale Software")
        title = Label(self.root, text="Post-machine", bd=12, relief=RIDGE, font=(
            "Arial Black", 20), bg="#1761BF", fg="white").pack(fill=X)
        # ===================================variables=======================================================================================
        self.Muffin = IntVar()
        self.Snack = IntVar()
        self.Donut = IntVar()
        self.Candy = IntVar()
        self.Lolipop = IntVar()

        self.Cookies = IntVar()
        self.Brownie = IntVar()
        self.Rice = IntVar()
        self.Orange = IntVar()
        
        self.Pear = IntVar()
        self.Raspberry = IntVar()
        self.Mango = IntVar()
        
        self.Plum = IntVar()
        self.Grape = IntVar()
        self.Carrots = IntVar()
        self.Shampoo = IntVar()
        
        self.Honey = IntVar()
        self.Cream = IntVar()
        self.Foam = IntVar()
        self.Masks = IntVar()
        self.Carrotshands = IntVar()
        
        self.total_sna = StringVar()
        self.total_gro = StringVar()
        self.total_hyg = StringVar()
        self.a = StringVar()
        self.b = StringVar()
        self.c = StringVar()
        self.c_name = StringVar()
        self.bill_no = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no.set(str(x))
        self.phone = StringVar()
        # ==========================================customer details label frame=================================================
        details = LabelFrame(self.root, text="customer detail", font=(
            "Arial Black", 12), bg="#1761BF", fg="white", relief=GROOVE, bd=10)
        details.place(x=0, y=80, relwidth=1)
        cust_name = Label(details, text="Customer name", font=(
            "Arial Black", 14), bg="#1761BF", fg="white").grid(row=0, column=0, padx=15)

        cust_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.c_name).grid(row=0, column=1, padx=8)

        contact_name = Label(details, text="No Contact", font=(
            "Arial Black", 14), bg="#1761BF", fg="white").grid(row=0, column=2, padx=10)

        contact_entry = Entry(details, borderwidth=4, width=30,
                              textvariable=self.phone).grid(row=0, column=3, padx=8)

        bill_name = Label(details, text="Invoice", font=(
            "Arial Black", 14), bg="#1761BF", fg="white").grid(row=0, column=4, padx=10)

        bill_entry = Entry(details, borderwidth=4, width=30,
                           textvariable=self.bill_no).grid(row=0, column=5, padx=8)
        # =======================================Snacks label frame=================================================================
        Snacks = LabelFrame(self.root, text="Sweet 5%", font=(
            "Arial Black", 12), bg="#1761BF", fg="#ffffff", relief=GROOVE, bd=10)
        Snacks.place(x=5, y=180, height=380, width=325)

        item1 = Label(Snacks, text="Muffin", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=0, column=0, pady=11)
        item1_entry = Entry(Snacks, borderwidth=2, width=15,
                            textvariable=self.Muffin).grid(row=0, column=1, padx=10)

        item2 = Label(Snacks, text="Snack", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=1, column=0, pady=11)
        item2_entry = Entry(Snacks, borderwidth=2, width=15,
                            textvariable=self.Snack).grid(row=1, column=1, padx=10)

        item3 = Label(Snacks, text="Donut", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=2, column=0, pady=11)
        item3_entry = Entry(Snacks, borderwidth=2, width=15,
                            textvariable=self.Donut).grid(row=2, column=1, padx=10)

        item4 = Label(Snacks, text="Candy", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=3, column=0, pady=11)
        item4_entry = Entry(Snacks, borderwidth=2, width=15,
                            textvariable=self.Candy).grid(row=3, column=1, padx=10)

        item5 = Label(Snacks, text="Lolipop", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=4, column=0, pady=11)
        item5_entry = Entry(Snacks, borderwidth=2, width=15,
                            textvariable=self.Lolipop).grid(row=4, column=1, padx=10)

        item6 = Label(Snacks, text="Cookies", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=5, column=0, pady=11)
        item6_entry = Entry(Snacks, borderwidth=2, width=15,
                            textvariable=self.Cookies).grid(row=5, column=1, padx=10)

        item7 = Label(Snacks, text="Brownie", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=6, column=0, pady=11)
        item7_entry = Entry(Snacks, borderwidth=2, width=15,
                            textvariable=self.Brownie).grid(row=6, column=1, padx=10)
        # ===================================GROCERY=====================================================================================
        grocery = LabelFrame(self.root, text="Groceries 10%", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#1761BF", fg="#ffffff")
        grocery.place(x=340, y=180, height=380, width=325)

        item8 = Label(grocery, text="Rice", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=0, column=0, pady=11)
        item8_entry = Entry(grocery, borderwidth=2, width=15,
                            textvariable=self.Rice).grid(row=0, column=1, padx=10)

        item9 = Label(grocery, text="Orange", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=1, column=0, pady=11)
        item9_entry = Entry(grocery, borderwidth=2, width=15,
                            textvariable=self.Orange).grid(row=1, column=1, padx=10)

        item10 = Label(grocery, text="Pear", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=2, column=0, pady=11)
        item10_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.Pear).grid(row=2, column=1, padx=10)

        item11 = Label(grocery, text="Raspberry", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=3, column=0, pady=11)
        item11_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.Raspberry).grid(row=3, column=1, padx=10)

        item12 = Label(grocery, text="Mango", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=4, column=0, pady=11)
        item12_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.Mango).grid(row=4, column=1, padx=10)

        item13 = Label(grocery, text="Plum", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=5, column=0, pady=11)
        item13_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.Plum).grid(row=5, column=1, padx=10)

        item14 = Label(grocery, text="Grape", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=6, column=0, pady=11)
        item14_entry = Entry(grocery, borderwidth=2, width=15,
                             textvariable=self.Grape).grid(row=6, column=1, padx=10)
        # ========================================beauty and hygine===============================================================================
        hygine = LabelFrame(self.root, text="Beauty and Hygiene 7%", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#1761BF", fg="#ffffff")
        hygine.place(x=677, y=180, height=380, width=325)

        item15 = Label(hygine, text="Soap", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=0, column=0, pady=11)
        item15_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.Carrots).grid(row=0, column=1, padx=10)

        item16 = Label(hygine, text="Shampoo", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=1, column=0, pady=11)
        item16_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.Shampoo).grid(row=1, column=1, padx=10)

        item17 = Label(hygine, text="Lotion-Body", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=2, column=0, pady=11)
        item17_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.Honey).grid(row=2, column=1, padx=10)

        item18 = Label(hygine, text="Cream-Body", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=3, column=0, pady=11)
        item18_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.Cream).grid(row=3, column=1, padx=10)

        item19 = Label(hygine, text="Foam-To-shave", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=4, column=0, pady=11)
        item19_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.Foam).grid(row=4, column=1, padx=10)

        item20 = Label(hygine, text="Mask-Face", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=5, column=0, pady=11)
        item20_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.Masks).grid(row=5, column=1, padx=10)

        item21 = Label(hygine, text="Soap-hands", font=(
            "Arial Black", 11), bg="#1761BF", fg="#ffffff").grid(row=6, column=0, pady=11)
        item21_entry = Entry(hygine, borderwidth=2, width=15,
                             textvariable=self.Carrotshands).grid(row=6, column=1, padx=10)
        # =====================================================billarea==============================================================================
        billarea = Frame(self.root, bd=10, relief=GROOVE, bg="#1761BF")
        billarea.place(x=1010, y=188, width=330, height=372)

        bill_title = Label(billarea, text="Billing Area", font=(
            "Arial Black", 17), bd=7, relief=GROOVE, bg="#1761BF", fg="#ffffff").pack(fill=X)

        scrol_y = Scrollbar(billarea, orient=VERTICAL)
        self.txtarea = Text(billarea, yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT, fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH, expand=1)
        # =================================================billing menu=========================================================================================
        billing_menu = LabelFrame(self.root, text="Billing summary", font=(
            "Arial Black", 12), relief=GROOVE, bd=10, bg="#1761BF", fg="white")
        billing_menu.place(x=0, y=560, relwidth=1, height=137)

        total_Snacks = Label(billing_menu, text="Total Price Sweets", font=(
            "Arial Black", 11), bg="#1761BF", fg="white").grid(row=0, column=0)
        total_Snacks_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.total_sna).grid(row=0, column=1, padx=10, pady=7)

        total_grocery = Label(billing_menu, text="Total Grocery Price", font=(
            "Arial Black", 11), bg="#1761BF", fg="white").grid(row=1, column=0)
        total_grocery_entry = Entry(billing_menu, width=30, borderwidth=2,
                                    textvariable=self.total_gro).grid(row=1, column=1, padx=10, pady=7)

        total_hygine = Label(billing_menu, text="Total price Beauty and Hygiene", font=(
            "Arial Black", 11), bg="#1761BF", fg="white").grid(row=2, column=0)
        total_hygine_entry = Entry(billing_menu, width=30, borderwidth=2,
                                   textvariable=self.total_hyg).grid(row=2, column=1, padx=10, pady=7)

        tax_Snacks = Label(billing_menu, text="Impuesto Dulces", font=(
            "Arial Black", 11), bg="#1761BF", fg="white").grid(row=0, column=2)
        tax_Snacks_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.a).grid(
            row=0, column=3, padx=10, pady=7)

        tax_grocery = Label(billing_menu, text="Food Taxes", font=(
            "Arial Black", 11), bg="#1761BF", fg="white").grid(row=1, column=2)
        tax_grocery_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.b).grid(
            row=1, column=3, padx=10, pady=7)

        tax_hygine = Label(billing_menu, text="Taxes Beauty and Hygiene", font=(
            "Arial Black", 11), bg="#1761BF", fg="white").grid(row=2, column=2)
        tax_hygine_entry = Entry(billing_menu, width=30, borderwidth=2, textvariable=self.c).grid(
            row=2, column=3, padx=10, pady=7)

        button_frame = Frame(billing_menu, bd=7, relief=GROOVE, bg="#73A6D7")
        button_frame.place(x=950, width=500, height=95)

        button_total = Button(button_frame, text="Total cost", font=("Arial Black", 15), pady=10,
                              bg="#1761BF", fg="#ffffff", command=lambda: total(self)).grid(row=0, column=0, padx=12)
        button_clear = Button(button_frame, text="To reset", font=("Arial Black", 15), pady=10,
                              bg="#1761BF", fg="#ffffff", command=lambda: clear(self)).grid(row=0, column=1, padx=10, pady=6)
        button_exit = Button(button_frame, text="Quit", font=("Arial Black", 15), pady=10, bg="#1761BF",
                             fg="#ffffff", width=8, command=lambda: exit1(self)).grid(row=0, column=2, padx=10, pady=6)
        intro(self)


def total(self):
    if (self.c_name.get == "" or self.phone.get() == ""):
        messagebox.showerror("Error", "Complete los datos del cliente!!")
    self.nu = self.Muffin.get()*1200
    self.no = self.Snack.get()*4000
    self.la = self.Donut.get()*1000
    self.ore = self.Candy.get()*2000
    self.mu = self.Lolipop.get()*3500
    self.si = self.Cookies.get()*6050
    self.na = self.Brownie.get()*1500
    total_Snacks_price = (
        self.nu +
        self.no +
        self.la +
        self.ore +
        self.mu +
        self.si +
        self.na)
    self.total_sna.set(str(total_Snacks_price)+" COP")
    self.a.set(str(round(total_Snacks_price*0.05, 3))+" COP")

    self.at = self.Rice.get()*4200
    self.pa = self.Orange.get()*12050
    self.oi = self.Raspberry.get()*11300
    self.ri = self.Pear.get()*160050
    self.su = self.Mango.get()*5550
    self.te = self.Grape.get()*4800
    self.da = self.Plum.get()*7665
    total_grocery_price = (
        self.at +
        self.pa +
        self.oi +
        self.ri +
        self.su +
        self.te +
        self.da)

    self.total_gro.set(str(total_grocery_price)+" COP")
    self.b.set(str(round(total_grocery_price*0.1, 3))+" COP")

    self.so = self.Carrots.get()*3000
    self.sh = self.Shampoo.get()*18000
    self.cr = self.Cream.get()*130000
    self.lo = self.Honey.get()*50000
    self.fo = self.Foam.get()*8500
    self.ma = self.Masks.get()*10000
    self.sa = self.Carrotshands.get()*2005

    total_hygine_price = (
        self.so +
        self.sh +
        self.cr +
        self.lo +
        self.fo +
        self.ma +
        self.sa)

    self.total_hyg.set(str(total_hygine_price)+" COP")
    self.c.set(str(round(total_hygine_price*0.07, 3))+" COP")
    self.total_all_bill = (total_Snacks_price +
                           total_grocery_price +
                           total_hygine_price +
                           (round(total_grocery_price*0.1, 3)) +
                           (round(total_hygine_price*0.07, 3)) +
                           (round(total_Snacks_price*0.05, 3)))
    self.total_all_bil = str(self.total_all_bill)+" COP"
    billarea(self)


def intro(self):
    self.txtarea.delete(1.0, END)
    self.txtarea.insert(
        END, "\tWelcome to your Store\n\tPhone +57 316 243 00 81")
    self.txtarea.insert(END, f"\n\nFactura Número. : {self.bill_no.get()}")
    self.txtarea.insert(END, f"\nClient Name : {self.c_name.get()}")
    self.txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
    self.txtarea.insert(END, "\n====================================\n")
    self.txtarea.insert(END, "\nProduct\t\tQuantity\tPrice\n")
    self.txtarea.insert(END, "\n====================================\n")


def billarea(self):
    intro(self)
    if self.Muffin.get() != 0:
        self.txtarea.insert(
            END, f"Muffin\t\t {self.Muffin.get()}\t{self.nu}\n")
    if self.Snack.get() != 0:
        self.txtarea.insert(
            END, f"Snack\t\t {self.Snack.get()}\t{self.no}\n")
    if self.Donut.get() != 0:
        self.txtarea.insert(
            END, f"Donut\t\t {self.Donut.get()}\t{self.la}\n")
    if self.Candy.get() != 0:
        self.txtarea.insert(END, f"Candy\t\t {self.Candy.get()}\t{self.ore}\n")
    if self.Lolipop.get() != 0:
        self.txtarea.insert(
            END, f"Lolipops\t\t {self.Lolipop.get()}\t{self.mu}\n")
    if self.Cookies.get() != 0:
        self.txtarea.insert(
            END, f"Cookies\t\t {self.Cookies.get()}\t{self.si}\n")
    if self.Brownie.get() != 0:
        self.txtarea.insert(
            END, f"Brownie\t\t {self.Brownie.get()}\t{self.na}\n")
    if self.Rice.get() != 0:
        self.txtarea.insert(END, f"Rice\t\t {self.Rice.get()}\t{self.at}\n")
    if self.Orange.get() != 0:
        self.txtarea.insert(END, f"Orange\t\t {self.Orange.get()}\t{self.pa}\n")
    if self.Pear.get() != 0:
        self.txtarea.insert(
            END, f"Pear\t\t {self.Pear.get()}\t{self.ri}\n")
    if self.Raspberry.get() != 0:
        self.txtarea.insert(
            END, f"Raspberry\t\t {self.Raspberry.get()}\t{self.oi}\n")
    if self.Mango.get() != 0:
        self.txtarea.insert(
            END, f"Mango\t\t {self.Mango.get()}\t{self.su}\n")
    if self.Plum.get() != 0:
        self.txtarea.insert(
            END, f"Plum\t\t {self.Plum.get()}\t{self.da}\n")
    if self.Grape.get() != 0:
        self.txtarea.insert(
            END, f"Grape\t\t {self.Grape.get()}\t{self.te}\n")
    if self.Carrots.get() != 0:
        self.txtarea.insert(END, f"Soap\t\t {self.Carrots.get()}\t{self.so}\n")
    if self.Shampoo.get() != 0:
        self.txtarea.insert(
            END, f"Shampoo\t\t {self.Shampoo.get()}\t{self.sh}\n")
    if self.Honey.get() != 0:
        self.txtarea.insert(
            END, f"Lotion-Body\t\t {self.Honey.get()}\t{self.lo}\n")
    if self.Cream.get() != 0:
        self.txtarea.insert(
            END, f"Cream-Body\t\t {self.Cream.get()}\t{self.cr}\n")
    if self.Foam.get() != 0:
        self.txtarea.insert(
            END, f"Foam-To shave\t\t {self.Foam.get()}\t{self.fo}\n")
    if self.Masks.get() != 0:
        self.txtarea.insert(
            END, f"Mask-Face\t\t {self.Masks.get()}\t{self.ma}\n")
    if self.Carrotshands.get() != 0:
        self.txtarea.insert(
            END, f"Soap-hands\t\t {self.Carrotshands.get()}\t{self.sa}\n")

    self.txtarea.insert(END, f"------------------------------------\n")
    if self.a.get() != "0.0 COP":
        self.txtarea.insert(END, f"Total Imp Dulces: {self.a.get()}\n")
    if self.b.get() != "0.0 COP":
        self.txtarea.insert(
            END, f"Total Imp Groceries 10%: {self.b.get()}\n")
    if self.c.get() != "0.0 COP":
        self.txtarea.insert(
            END, f"Total Imp Belleza e Higiene: {self.c.get()}\n")
    self.txtarea.insert(END, f"Monto Total cost : {self.total_all_bil}\n")
    self.txtarea.insert(END, f"------------------------------------\n")


def clear(self):
    self.txtarea.delete(1.0, END)
    self.Muffin.set(0)
    self.Snack.set(0)
    self.Donut.set(0)
    self.Candy.set(0)
    self.Lolipop.set(0)
    self.Cookies.set(0)
    self.Brownie.set(0)
    self.Rice.set(0)
    self.Orange.set(0)
    self.Pear.set(0)
    self.Raspberry.set(0)
    self.Mango.set(0)
    self.Plum.set(0)
    self.Grape.set(0)
    self.Carrots.set(0)
    self.Shampoo.set(0)
    self.Honey.set(0)
    self.Cream.set(0)
    self.Foam.set(0)
    self.Masks.set(0)
    self.Carrotshands.set(0)
    self.total_sna.set(0)
    self.total_gro.set(0)
    self.total_hyg.set(0)
    self.a.set(0)
    self.b.set(0)
    self.c.set(0)
    self.c_name.set(0)
    self.bill_no.set(0)
    self.bill_no.set(0)
    self.phone.set(0)


def exit1(self):
    self.root.destroy()


root = Tk()
obj = Bill_App(root)
root.mainloop()
