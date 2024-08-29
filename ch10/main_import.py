import csv
import sys
import sqlite3

def main():

    with sqlite3.connect("customers.db") as con:
        cur = con.cursor()

        with open('customers.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                sql = """INSERT INTO `customers_tbl`(first_name,last_name,email,gender,ip_address)
                VALUES(?,?,?,?,?)"""
                data_row = list(row.values())[1:]
                cur.execute(sql,data_row)
    
    
    
    # versioning python x.y.z x: major, y: minor, z ,patch
    # print(sys.version_info.major)
    # print(sys.version_info.minor)
    # print(sys.version_info.micro)



if __name__ == '__main__':
    main()