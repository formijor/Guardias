
import datetime

def get_lista_meses_dias(mes):
    lista_meses = ['Enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 
                   'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre']
    lista_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes is None:
        return lista_meses, lista_dias
    elif mes == 'meses':
        return lista_meses
    elif type(mes) == int:
        return lista_meses[mes-1], lista_dias[mes - 1]
    elif type(mes) == str:
        posicion = lista_meses.index(mes)
        return lista_meses[posicion], lista_dias[posicion]

def get_feriados(mes):
    lista_feriados = [[1], [12,13], [24,29,30], [2, 30], [1, 25], [17, 20, 25],
                      [2, 9], [20], [], [15], [19], [8, 24, 25, 31]]
    if mes == None:
        meses_feriados = get_lista_meses_dias('meses') +  lista_feriados
        return list(zip(get_lista_meses_dias('meses'), lista_feriados))
    elif type(mes) == int:
        return lista_feriados[mes-1]
    
def get_vacaciones(persona):
    vacaciones = ''
    #Codigo que obtiene los datos de vacaciones de la bd
    return vacaciones

def get_anio_actual():
    return datetime.datetime.now().year

def get_mes_actual():
    return datetime.datetime.now().month

def get_dia_actual():
    return datetime.datetime.now().day

def get_personas_grupo_trabajo(grupo):
    '''Obtiene las personas que componen un grupo de trabajo'''
    lista_personas_grupo = ''
    #aca va codigo que obtiene los datos de una bd
    return lista_personas_grupo

def get_grupos_trabajo():
    '''Obtiene los grupos de trabajo (solo grupo)'''
    lista_grupo_trabajo = ''
    #aca va codigo que obtiene los datos de una bd
    return lista_grupo_trabajo

def get_grupos_trabajo_y_personas():
    '''Obtiene los grupo de trabajo y las personas que los componen'''
    lista_grupos_y_personas = []
    for grupo in get_grupos_trabajo():
        lista_grupos_y_personas.add(grupo + get_personas_grupo_trabajo(grupo))
    return lista_grupos_y_personas   

def test():
    print (get_anio_actual())
    print (get_mes_actual())
    print (get_dia_actual())
    print (get_lista_meses_dias('meses'))
    print (get_feriados(12))

test()