import sqlite3
from Customer import Customer


class CustomerDAO:

    def __init__(self,db_file) -> None:
        self.__con = sqlite3.connect(db_file)
    
    def find_all(self)->list[Customer]:
        customers = []
        cur = self.__con.cursor()
        result = cur.execute('SELECT id,first_name,last_name,email,gender,ip_address FROM customers_tbl')
        for r in result.fetchall():
            c = Customer(*r)
            customers.append(c)
        
        return customers
    
    
    def __del__(self):
        self.__con.close()
