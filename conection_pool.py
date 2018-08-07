'''
Created on 7 ago. 2018

@author: JorInt
'''

import sqlite3
import random


def crear_conexion(dbFile):
    conexion = sqlite3.connect(dbFile)
    return conexion
    
def close_conexion(conexion):
    """Cierra la conexion con la base de datos"""
    try:
        conexion.close()
        return True
    except:
        return False

def crear_cursor(conexion):
    cursor = conexion.cursor()
    return cursor 

def cerrar_cursor(cursor):
    cursor.close()
    

class pool_conexiones():
    def __init__(self):
        self.conexiones = {}
        self.espera = {}
        
    def solicitar_conexion(self, cliente, dbFile):
        codigo = self.obtener_codigo_identificacion_conexion()
        conexion = self.abrir_conexion(dbFile)
        conect_cliente = Conexion(codigo, cliente, conexion)
        self.guardar_conexion(conect_cliente)
        #print (conect_cliente)
        return codigo        
    
    def obtener_codigo_identificacion_conexion(self):         
        codigo = random.randint(100, 999)
        while codigo in self.conexiones:
            codigo = random.randint(100, 999)
        return codigo
    
    def guardar_conexion(self, conexion):
        self.conexiones[conexion.codigo] = conexion
        return True
        
    def eliminar_conexion(self, codigo):
        conexion = self.conexiones.pop(codigo)
        return conexion
    
    def abrir_conexion(self, dbFile):
        conexion = crear_conexion(dbFile)
        cursor = crear_cursor(conexion)
        print ('Cliente Conectado')
        return (cursor, conexion)
    
    def cerrar_conexion(self, codigo):
        conect = self.eliminar_conexion(codigo)
        cerrar_cursor(conect.conexion[0])
        close_conexion(conect.conexion[1])
        print ('Conexion ' + str(codigo) + ' Terminada')       
        return True
    
    def validar_peticion(self, credencial, mensaje):
        if credencial[0] not in self.espera and credencial[0] in self.conexiones:
            conexion = self.conexiones[credencial[0]]
            if conexion.cliente == credencial[1]:
                print ('Solicitud aprobada')
                print (mensaje)
                #self.manejador_base_datos.recibir_accion(mensaje)
            else:
                self.cerrar_conexion(codigo)
                print ('Conexion no valida 2')
        else:
            print ('Conexion no valida 1')
            
    def denegar_acceso(self, conexion):
        self.espera[conexion.codigo] = conexion
        
    def aprobar_acceso(self, conexion):
        self.espera.pop(conexion.codigo)    
        
    
class Conexion():
    def __init__(self, codigo, cliente, conexion):
        self.codigo = codigo
        self.cliente = cliente
        self.conexion = conexion

pool_instancia = pool_conexiones()
codigo = pool_instancia.solicitar_conexion('Jorge', 'Data\\guardias_data.db')
print (pool_instancia.conexiones)
pool_instancia.validar_peticion((codigo, 'Jorge'), 'mensaje')
#print (pool_instancia.cerrar_conexion(codigo))
        