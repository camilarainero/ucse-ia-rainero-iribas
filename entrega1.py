from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer

def tupla_a_lista(t):
    return [list(row) for row in t]

def lista_a_tupla(t):
    return tuple(tuple(row) for row in t)

# Definir ciudades y sus distancias
DISTANCIAS = {
    ('sunchales', 'lehmann'): 32,
    ('lehmann', 'rafaela'): 8,
    ('rafaela', 'susana'): 10,
    ('susana', 'angelica'): 25,
    ('angelica', 'san_vicente'): 18,
    ('angelica', 'sc_de_saguier'): 60,
    ('rafaela', 'esperanza'): 70,
    ('esperanza', 'recreo'): 20,
    ('recreo', 'santa_fe'): 10,
    ('santa_fe', 'santo_tome'): 5,
    ('santo_tome', 'angelica'): 85,
    ('santo_tome', 'sauce_viejo'): 15,
}
# Agregamos las inversas también:
for (ciudad1, ciudad2), kms in list(DISTANCIAS.items()):
    DISTANCIAS[(ciudad2, ciudad1)] = kms


estado_inicial=[[],[]]
'''Estructura del estado:
[ [ (paquete, ciudad_actual, ciudad_destino), ...] , [ (camion,combustible,ciudad), ...] ] 
'''        
# Armamos el estado inicial con los parametros
def armar_estado_inicial(paquetes,camiones):
    inicial=[[],[]]
    for p in paquetes: 
        inicial[0].append(p)
    for c in camiones:
        inicial[1].append(c)

    return inicial

sedes=('rafaela','santa_fe')

class ProblemaCamiones(SearchProblem):

    def is_goal(self, state):    
    #El problema termina cuando todos los paqetes estan en su ciudad destino y los camiones estan en alguna sede       
        nuevo_estado = state 
        paquetes,camiones= nuevo_estado
     
        for p in paquetes:
            if p[1]!=p[2]: #Verificamos que todos los paquetes estan en ciudad destino 
                return False
 
        for c in camiones:
            if c[2] not in sedes: #Verificamos que todos los camiones esten en alguna sede
                return False
        return True  #True si todos los paquetes estan en su ciudad destino y todos los camiones estan en alguna sede          


    def actions(self,state):    

        # Estructura de la acción: 
        # [ [(camion), (ciudad),(combustible que me lleva moverme a la ciudad),(paquetes)] ] 
        # ejemplo = [ ['c1','rafaela',0.5],['p1','p2','p3'] ]
        paquetes,camiones=state 
        acciones=[]

        #Podemos ver de restringir las accione sposibles preguntando si me alcanza el combustible si no alcanza no la agrego

        for c in camiones:
            camion,ciudad,combustible=c                    

            #Por cada camion recorro Distancias y busco hacia donde se puede mover en funcion de la ciudad donde esta
            for ciudades,distancia in DISTANCIAS.items(): 
                accion_c=[] #accion_c es accio del camion (camion, ciudad, combustible)
                paquetes_llevo=[]
                ciudad_actual,ciudad_destino=ciudades
                if ciudad == ciudad_actual:
                    destino=ciudad_destino
                    combustible_que_gasto=(distancia/100)
                    #accion_c.append( [ c[0] , destino , combustible_que_gasto ] )                   
                    accion_c.append(c[0])
                    accion_c.append(destino)
                    accion_c.append(combustible_que_gasto)

                    for p in paquetes:
                        if p[1]==ciudad:
                            paquetes_llevo.append(p[0])
                    
                    acciones.append([accion_c,paquetes_llevo])     
                  
        return acciones
           
        
    def cost(self, state,action,state2):  

        return 1    

    def result(self, state, action):
        # Tiene que ser una tupla        
        # El result tiene que: 
        #   Mover camion de una ciudad a otra 
        #   Llevar los paquetes 
        #   Descontar o incrementar combustible.        
        
        paquetes,camiones=state      
        camiones_estado=tupla_a_lista(camiones)
        paquetes_estado =tupla_a_lista(paquetes)
        
        camion, paquetes_lleva=action

        camion_elegido=camion[0]
        destino=camion[1]
        combustible_restar=camion[2]
        
        for c in camiones_estado:
            if camion_elegido==c[0]: #Busco el camion que se tiene que mover             
                c[1]=destino #Es lo que despues voy a reemplazar en el estado ciudad                
                c[2]=c[2]-combustible_restar #Es lo que despues voy a reemplazar en el estado combustible
                
        for pll in paquetes_lleva: #Busco los paquetes que tiene que mover
            for p in paquetes_estado:
                if p[0]==pll: #Si son iguales lo reemplazo en el estado
                    p[1]=destino

        estado = (lista_a_tupla(paquetes_estado),lista_a_tupla(camiones_estado))
        print("estado",estado)
        print("estado tupla",lista_a_tupla(estado))

        return lista_a_tupla(estado)   
        

    def heuristic(self, state):
        return 1
     

def planear_camiones(metodo, camiones, paquetes):
    # Armar el estado inicial
    estado_inicial=armar_estado_inicial(paquetes,camiones)

    # Llamamos al problema y le pasamos el estado inicial
    problema = ProblemaCamiones(lista_a_tupla(estado_inicial))

    funciones = {
        'breadth_first': breadth_first,
        'depth_first': depth_first,
        'greedy': greedy,
        'astar': astar
    }
    funcion_busqueda = funciones[metodo]

    result = funcion_busqueda(problema)
    
    print (result)
    print (result.path)
    #itinerario = ...armar el itinerario en base a la solución encontrada en result, leyendo result.path(), etc...
    
    return result
    
 


if __name__ == '__main__':
    
    #viewer = WebViewer()
	#viewer = ConsoleViewer()
	#viewer = None
	#viewer = BaseViewer()
	    
    itinerario = planear_camiones(
    # método de búsqueda a utilizar. Puede ser: astar, breadth_first, depth_first, uniform_cost o greedy
    metodo="breadth_first",
    camiones=[
    # id, ciudad actual, y capacidad de combustible máxima (litros)
        ('c1', 'rafaela', 1.5),
        ('c2', 'rafaela', 2),
        ('c3', 'santa_fe', 2),
    ],
    paquetes=[
        # id, ciudad de origen, y ciudad de destino
        ('p1', 'rafaela', 'angelica'),
        ('p2', 'rafaela', 'santa_fe'),
        ('p3', 'esperanza', 'susana'),
        ('p4', 'recreo', 'san_vicente'),
    ],
    )
    print ('EL RESULTADO ES')
    print (itinerario)