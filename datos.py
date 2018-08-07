'''
Created on 6 ago. 2018

@author: formijor
'''

import sqlite3


def crear_conexion(dbFile):
    conexion = sqlite3.connect(dbFile)
    return conexion
    
def cerrar_conexion(conexion):
    """Cierra la conexion con la base de datos"""
    try:
        conexion.close()
        return True
    except:
        return False

def crear_cursor(conexion):
    cursor = conexion.cursor()
    return cursor 

def insert_registros(conexion, cursor, tabla, columnas, registros):
    sql = "INSERT INTO " + str(tabla) + str(columnas) + " VALUES " + str(registros)
    cursor.execute(sql)
    conexion.commit()
    
def get_guardias(cursor):
    sql= "SELECT * FROM vista_historial_guardias"
    cursor.execute(sql)
    return cursor.fetchall()

def get_personas(cursor):
    sql = "SELECT * FROM vista_personas"
    cursor.execute(sql)
    return cursor.fetchall()
    
#--------------------------------------TEST---------------------------------
def test_guardias():
    conexion = crear_conexion('Data\\guardias_data.db')
    cursor = crear_cursor(conexion)
    guardias = get_guardias(cursor)
    print (guardias)
    
def test_insertar_registros():
    conexion = crear_conexion('Data\\guardias_data.db')
    cursor = crear_cursor(conexion)
    insert_registros(conexion, cursor, 'persona', '(nombre)', '("Jorge"), ("Laura"), ("Luis"), ("Ezequiel")')
    
def test_personas():
    conexion = crear_conexion('Data\\guardias_data.db')
    cursor = crear_cursor(conexion)
    personas = get_personas(cursor)
    print (personas)
    
    
#test_insertar_registros()
test_personas()

