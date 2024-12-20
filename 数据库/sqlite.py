import sqlite3

#数据库 test.db  多个表格   Excel
#游标   工具   增删改查  cursor
#SQL   数据库语言   ORM 封装
#commit  DDL  隐式
db=sqlite3.connect("test.db")
cursor=db.cursor()

cursor.execute("""
    create table if not exists Study(
        id integer primary key autoincrement,
        name varchar(10) not null
    );
""")

# cursor.execute("""
#     insert into Study (name) values("ytttt4")
# """)
# db.commit()

cursor.execute("""
    delete from Study where id=2;
""")
db.commit()

cursor.execute("""
    update Study set name="Yt5" where id=5;
""")
db.commit()

results=cursor.execute("""
    select * from Study;
""")
print(results.fetchall())

cursor.close()
db.close()