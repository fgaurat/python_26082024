from tkinter import *
from tkinter import ttk

from CustomerDAO import CustomerDAO

def main():
    customerDAO =  CustomerDAO(r"../customers.db")
    customers = customerDAO.find_all()

    ws = Tk()
    ws.title('Customers')
    ws.geometry('800x600')

    tv = ttk.Treeview(ws,show="headings")
    tv['columns']=('Id', 'Name', 'FirstName')

    tv.column('Id',  anchor=CENTER,stretch=NO)
    tv.column('Name', anchor=CENTER, width=80)
    tv.column('FirstName', anchor=CENTER, width=80)

    tv.heading('Id', text='Id', anchor=CENTER)
    tv.heading('Name', text='Lastname', anchor=CENTER)
    tv.heading('FirstName', text='Firstname', anchor=CENTER)

    for customer in customers:
        tv.insert(parent='', index=customer.id, iid=customer.id, text='', values=(customer.id,customer.last_name,customer.first_name))
    
    tv.pack(fill=BOTH,expand=True)



    ws.mainloop()




def main_hello():
    root = Tk()

    frm = ttk.Frame(root, padding=10)

    frm.grid()

    ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
    ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
    
    root.mainloop()

if __name__ == '__main__':
    main()