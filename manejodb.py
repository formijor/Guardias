'''
Created on 17 jul. 2018

@author: formijor
'''

class ManejoDb_guardias():
    def __init__(self, mensaje):
        pass

    def recibir_mensaje(self, mensaje, datos):
        if mensaje == 'Consulta':
            pass
            
            
            
    def ejecutar_consulta(self, datos, cursor, conexion):
        pass
        
        






   
    
def obtener_vacaciones(persona):
    vacaciones = ''
    sql = '''SELECT * FROM      
            WHERE persona = %d''', persona
    #codigo obtiene directo de la bd
    return vacaciones

def obtener_usuarios():
    sql = "SELECT * FROM vista_personas"

   