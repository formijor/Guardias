'''
Created on 7 ago. 2018

@author: JorInt
'''

import sqlite3
import random
import manejodb
import time

    
class PoolConexiones():
    def __init__(self, numero_maximo_conexiones):
        self.numero_conexiones = numero_maximo_conexiones
        self.pool_conexiones = {}
        self.conectar_pool('Data\\pool_config.db')
        
    def conectar_pool(self, archivo):
        self.conexion_pool = sqlite3.connect(archivo)
        self.cursor_pool = self.conexion_pool.cursor()
        
    def obtener_conexiones_activas(self):
        sql = "SELECT * FROM vista_conexiones_activas"
        self.cursor_pool.execute(sql)
        datos = self.cursor_pool.fetchall()
        return datos
                   
    def guardar_nueva_conexion(self, conexion):
        fecha = time.strftime("%x")
        hora = time.strftime("%H:%M:%S")
        sql = """INSERT INTO conexiones (codigo, archivo, fecha_conexion, 
            hora_conexion)
            VALUES """ + str((conexion.codigo, conexion.archivo, fecha, hora))
        #print (sql)
        self.cursor_pool.execute(sql)
        #self.conexion_pool.commit()
        
    def generar_codigo_identificacion_conexion(self):
        codigo = random.randint(100, 999)
        while codigo in self.pool_conexiones:
            codigo = random.randint(100, 999)
        return codigo
        
    def crear_conexion(self, archivo, cliente):
        mensaje = 'Establecer conexion'
        codigo_conexion = self.generar_codigo_identificacion_conexion()
        conectado = Conexion(codigo_conexion, cliente, archivo)
        self.pool_conexiones[codigo_conexion] = conectado
        self.guardar_nueva_conexion(conectado)
        return conectado
    
    def finalizar_conexion(self, codigo):
        conexion = self.pool_conexiones.pop(codigo)
        conexion.cerrar_conexion()
        
    def registrar_desconexion(self, conexion):
        fecha = time.strftime("%x")
        hora = time.strftime("%H:%M:%S")
        sql = "UPDATE conexiones SET fecha_desconexion = " + "'"+fecha+"'"
        sql += ", hora_desconexion = " + str('"'+hora+'"') 
        print (conexion.codigo)
        #sql +=  "WHERE codigo = " + str(conexion.codigo)  
        sql += " WHERE fecha_desconexion is Null"
        self.cursor_pool.execute(sql)
        self.conexion_pool.commit()    
   
    def imprimir_conexiones_activas(self, datos):
        print("CONEXIONES ACTIVAS \n------------------------------")
        columnas = ('id_conexiones_activas', 'codigo', 'archivo', 'fecha_conexion', 'hora_conexion')
        for D in datos:
            for cont in range(len(columnas)):
                print (columnas[cont] + ": " + str(D[cont]))
            print ("\n-------------------------------")
            
    def borrar_datos_tablas(self):
        sql = "DELETE FROM conexiones_activas"
        self.cursor_pool.execute(sql)
        self.conexion_pool.commit()
        
    def test(self):
        sql = """SELECT * FROM conexiones
                """
        self.cursor_pool.execute(sql)
        datos = self.cursor_pool.fetchall()
        print (datos)
    

class Conexion():
    def __init__(self, codigo, cliente, archivo):
        self.codigo = codigo
        self.cliente = cliente
        self.archivo = archivo
        self.cola_mensajes = []
        self.iniciar_conexion()
    
    def iniciar_conexion(self):
        self.conexion = sqlite3.connect(self.archivo)
        self.cursor = self.conexion.cursor()
        return True
    
    def cerrar_conexion(self):
        self.cursor.close()
        self.conexion.close()
        print ('Conexion ' + str(self.codigo) + ' Terminada')       
        return True

    #def enviar_mensaje(self, mensaje, datos):

def imprimir_tabla(pool):
    sql = "SELECT * FROM conexiones_activas"    
    pool.cursor_pool.execute(sql)
    print (pool.cursor_pool.fetchall())
        
        
        
#---------------------------TEST--------------------       
pool = PoolConexiones(5)
datos = pool.obtener_conexiones_activas()      
pool.imprimir_conexiones_activas(datos)
#pool.test()

conect = pool.crear_conexion('Data\guardias_data.db', 'Jorge')
datos = pool.obtener_conexiones_activas()      
pool.imprimir_conexiones_activas(datos)

#input()

pool.registrar_desconexion(conect)
datos = pool.obtener_conexiones_activas()
pool.imprimir_conexiones_activas(datos)
pool.test()


#pool.borrar_datos_tablas()

#imprimir_tabla(pool)  """




    
