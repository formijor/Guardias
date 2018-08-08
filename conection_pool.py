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
        print (datos)
        
    def guardar_nueva_conexion(self, conexion):
        fecha = time.strftime("%x")
        hora = time.strftime("%H:%M:%S")
        sql = """INSERT INTO conexiones (codigo, archivo, fecha_conexion, 
            hora_conexion) 
            VALUES """ + str((conexion.codigo, conexion.archivo, fecha, hora))
        
        
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
        return True
    
    def finalizar_conexion(self, codigo_conexion):
        conexion = self.pool_conexiones.pop(codigo_conexion)
        conexion.finalizar_conexion()

    



class Conexion():
    def __init__(self, codigo, cliente, archivo):
        self.codigo = codigo
        self.cliente = cliente
        self.archivo = archivo
        self.cola_mensajes = []
    
    def iniciar_conexion(self, archivo):
        self.conexion = sqlite3.connect(archivo)
        self.cursor = self.conexion.cursor()
        return True
    
    def cerrar_conexion(self, codigo, cursor, conexion):
        self.cursor = self.cursor.close()
        self.conexion.close()
        print ('Conexion ' + str(codigo) + ' Terminada')       
        return True

    #def enviar_mensaje(self, mensaje, datos):
        
        
pool = PoolConexiones(5)
pool.obtener_conexiones_activas()      
        
    
    
    
    
    
    
    
    
        
        

class pool_conexiones2():
    def __init__(self):
        self.conexiones = {}
        self.espera = {}
        
    def solicitar_conexion(self, cliente, dbFile):
        codigo = self.obtener_codigo_identificacion_conexion()
        conexion = self.abrir_conexion(dbFile)
        conect_cliente = Conexion(codigo, cliente, conexion)
        self.registrar_conexion(conect_cliente)
        return codigo        
    
    def obtener_codigo_identificacion_conexion(self):         
        codigo = random.randint(100, 999)
        while codigo in self.conexiones:
            codigo = random.randint(100, 999)
        return codigo
    
    def registrar_conexion(self, conexion):
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
        
    
    
    
    


        




#pool_instancia = pool_conexiones()
#codigo = pool_instancia.solicitar_conexion('Jorge', 'Data\\guardias_data.db')
#print (pool_instancia.conexiones)
#pool_instancia.validar_peticion((codigo, 'Jorge'), 'mensaje')
#print (pool_instancia.cerrar_conexion(codigo))
        