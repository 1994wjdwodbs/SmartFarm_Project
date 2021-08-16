import sqlite3

# smart_farm db 생성 및 SF_machine 초기 Rec 생성
def db_init():
    SQL_File_Name = 'Create_Tbl_Schema.sql'

    TableSchema=''
    with open(SQL_File_Name, 'r') as SchemaFile:
        TableSchema  = SchemaFile.read().replace('\n', ' ')

    #Connect or Create DB File
    conn = sqlite3.connect('smart_farm.db')
    curs = conn.cursor()

    #Create Tables
    if sqlite3.complete_statement(TableSchema): # 세미콜론으로 끝나는 쿼리문이면 True
    # execute(sql[, parameters])
    # cursor() 메서드를 호출하여 커서 객체를 만들고, 지정된 parameters를 사용하여
    # 커서의 execute() 메서드를 호출한 다음, 커서를 반환

    # executescript(script_sql)
    # cursor() 메서드를 호출하여 커서 객체를 만들고, 지정된 sql_script를 사용하여 
    # 커서의 executescript() 메서드를 호출한 다음, 커서를 반환
        curs.executescript(TableSchema)

    # Insert Values
    curs.execute("INSERT INTO `SF_machine` (LED, w_level, l_level, s_level, pump, fan_in, fan_out, temp, humi) VALUES('0','0','0','0','false','false','false','0','0')")

    conn.commit()

    # Close DB
    curs.close()

def getAllProperty():

    #Connect DB File
    conn = sqlite3.connect('smart_farm.db')
    curs = conn.cursor()

    curs.execute('SELECT * FROM `SF_machine`')
    rows = curs.fetchall()

    rec = ()

    for row in rows:
        # print(row)
        # results = f'idx : {row[0]}, LED : {row[1]}, w_level : {row[2]}, l_level : {row[3]}, s_level : {row[4]}, pump : {row[5]}, fan_in : {row[6]}, fan_out : {row[7]}, temp : {row[8]}, humi : {row[9]}'
        # print(results)
        rec = row

    curs.close()

    return rec

def getProperty(par_name):

    #Connect DB File
    conn = sqlite3.connect('smart_farm.db')
    curs = conn.cursor()

    curs.execute('SELECT ' + str(par_name) + ' FROM `SF_machine`')
    print(curs.fetchone()[0])

    curs.close()

def SetProperty(par_name, par_val):

    #Connect DB File
    conn = sqlite3.connect('smart_farm.db')
    curs = conn.cursor()

    UPDATE_QUERY = 'UPDATE SF_machine SET ' + str(par_name) + ' = :VAL WHERE idx = 1'
    curs.execute(UPDATE_QUERY, {'VAL' : par_val})
    
    conn.commit()
    curs.close()

SetProperty('LED', 75)
getAllProperty()
getProperty('LED')