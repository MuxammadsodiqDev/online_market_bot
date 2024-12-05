import sqlite3

def basketRead(user_id):
    try:
        con = sqlite3.connect("online_market.db")
        cursor = con.cursor()
        cursor.execute(f"""select * from basket where user_id = {user_id}""")
        a = cursor.fetchall()
        cursor.close()
        return a 
    except(Exception, sqlite3.Error)as error:
        print("error",error)
    finally:
        if con:
            con.close()

def basketDelete(user_id):
    try :
        con = sqlite3.connect("online_market.db")
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM basket WHERE user_id = {user_id}")
        con.commit()
    except(Exception,sqlite3.Error) as error:
        print(error)
    finally:
        if con:
            cursor.close()
            con.close()
            print("yangi qator qo'shildi.")


def basketInsert(category, name, count, user_id):
    try:
        con = sqlite3.connect("online_market.db")
        cursor = con.cursor()
        cursor.execute("""insert into basket(category,name,count,user_id) values(?,?,?,?)""",(category,name,count,user_id))
        con.commit()
        cursor.close()
    except(Exception,sqlite3.Error) as error:
        print(error)
    finally:
        if con:
            con.close()
            print("yangi qator qo'shildi.")

# try : 
#     con = sqlite3.connect("online_market.db")
#     cursor = con.cursor()
#     cursor.execute("""create table basket(
#                    id integer primary key not null,
#                    category text not null,
#                    name text not null,
#                    count integer not null,
#                    user_id integer not null
#     )""")
# except(Exception,sqlite3.Error) as error:
#         print("error",error)
# finally:
#         if con:
#             con.close()
#         print("malumot qo'shildi")




def productRead(category):
    try:
        con = sqlite3.connect("online_market.db")
        cursor = con.cursor()
        cursor.execute(f"""select * from products where connect_id = {category}""")
        a = cursor.fetchall()
        cursor.close()
        return a 
    except(Exception, sqlite3.Error)as error:
        print("error",error)
    finally:
        if con:
            con.close()


def categoryRead():
    try:
        con = sqlite3.connect("online_market.db")
        cursor = con.cursor()
        cursor.execute(f"""select * from categories""")
        a = cursor.fetchall()
        cursor.close()
        return a 
    except(Exception, sqlite3.Error)as error:
        print("error",error)
    finally:
        if con:
            con.close()

def productAdd(product_name,products_price,image,connect_id):
    try:
        con = sqlite3.connect("online_market.db")
        cursor = con.cursor()
        cursor.execute("""insert into products(product_name,products_price,image,connect_id) values(?,?,?,?)""",
                       (product_name,products_price,image,connect_id))
        con.commit()
        cursor.close()
    except(Exception,sqlite3.Error) as error:
        print("error",error)
    finally:
        if con:
            con.close()
        print("malumot qo'shildi")


def categoryAdd(category):
    try:
        con = sqlite3.connect("online_market.db")
        cursor = con.cursor()
        cursor.execute("""insert into categories(category_name) values(?)""",
                       (category,))
        con.commit()
        cursor.close()
    except(Exception,sqlite3.Error) as error:
        print("error",error)
    finally:
        if con:
            con.close()
        print("malumot qo'shildi")







# try:
#     con = sqlite3.connect("online_market.db")
#     cursor = con.cursor()
#     cursor.execute(""" create table categories(
#                    id INTEGER PRIMARY KEY NOT NULL,
#                    category_name text not null);""")
#     con.commit()
#     cursor.close()
#     print("table yaratildi")
# except(Exception,sqlite3.Error) as error:
#     print("error",error)
# finally:
#     if con:
#         cursor.close()
#         con.close()


# try:
#     con = sqlite3.connect("online_market.db")
#     cursor = con.cursor()
#     cursor.execute(""" create table products(
#                    product_id integer primary key not null ,
#                    product_name text not null,
#                    products_price integer not null,
#                    image text not null,
#                    connect_id integer);""")
#     con.commit()
#     cursor.close()
#     print("tabla yaratildi")
# except(Exception,sqlite3.Error) as error:
#     print("error",error)
# finally:
#     if con:
#         cursor.close()
#         con.close()

# try:
#     con = sqlite3.connect("online_market.db")
#     cursor = con.cursor()
#     cursor.execute(""" create table karzinka(
#                    user_id integer not null,
#                    product_name text not null,
#                    products_price int not null);""")
#     con.commit()
#     cursor.close()
#     print("tabla yaratildi")
# except(Exception,sqlite3.Error) as error:
#     print("error",error)
# finally:
#     if con:
#         con.close()


# def productRead(connect_id):
#     try:
#         con = sqlite3.connect("online_market.db")
#         cursor = con.cursor()
#         cursor.execute(f"""select * from products where connect_id = {connect_id}""")
#         a = cursor.fetchall()
#         cursor.close()
#         return a 
#     except(Exception, sqlite3.Error)as error:
#         print("error",error)
#     finally:
#         if con:
#             con.close()