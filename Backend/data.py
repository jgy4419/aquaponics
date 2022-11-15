import pymysql
from datetime import datetime
import time
import serial
import pandas as pd

# init serial port
ser1 = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
)
ser2 = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
)

# init sql
conn, cur = None, None
sql = ""

# define function
def pushData(data):
    ser2.write(data)

def connection():
    global conn, cur
    conn = pymysql.connect(host='localhost', user='root', password='wls0827', db='CDP', charset='utf8')
    cur = conn.cursor()
    sql = "select * from sensor"
    cur.execute(sql)

def dataCheck(serial):
    dic = {'humidity': 'no', 'temperature': 'no', 'soilHumidity': 'no', 'light': 'no'}
    while 'no' in dic.values():
        re = serial.readline()[:-2].decode().rstrip().replace('\'', '').replace('%', '').replace('C', '')
        if len(re.split(',')) == 2:
            name, value = re.split(',')
            dic[name] = value
    return dic.values()

def dataCheck2(serial):
    for _ in range(3):
        re = str(serial.readline())
        if "ph" in re:
            re = re[2:-5]
            break
    value = re.split(',')[1]
    return value

def dataInput():
    global conn, cur
    data1 = dataCheck(ser1)
    data2 = dataCheck2(ser2)
    h, t, s, l, p = *[float(i) for i in data1], data2
    insertSql = "INSERT INTO sensor (humidity, temperature, soilHumidity, light, ph) VALUES (%s, %s, %s, %s, %s);"
    cur.execute(insertSql, (h, t, s, l, p))
    conn.commit()

def dataFind():
    global conn, cur
    sql = "SELECT time, humidity, temperature, soilHumidity, light, ph FROM sensor ORDER BY time ASC"
    cur.execute(sql)
    result = cur.fetchall()
    conn.commit()
    p = pd.read_sql(sql, conn, index_col='time')
    return p

def disconnection():
    global conn
    conn.close()

if __name__=='__main__':
    connection()
    try:
        while True:
            dataInput()
            df = dataFind()
            print(df)
    except KeyboardInterrupt:
        print("exit")

    disconnection()