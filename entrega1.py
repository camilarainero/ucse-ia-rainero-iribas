from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer
from itertools import combinations

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

#Calculamos la distancia minima para despues usarla en la heuristica
distancia_minima=min(DISTANCIAS.values())

sedes=('rafaela','santa_fe')

estado_inicial=[[],[]]
# Estructura del estado:
# [ [ (paquete, ciudad_actual, ciudad_destino), ...] , [ (camion,combustible,ciudad), ...] ] 
        
# Armamos el estado inicial con los parametros
def armar_estado_inicial(paquetes,camiones):
    inicial=[[],[]]
    for p in paquetes: 
        inicial[0].append(p)
    for c in camiones:
        inicial[1].append(c)
    return inicial

capacidad=[]
def guardar_capacidad(camiones):
    for c in camiones:
        capacidad.append([c[0],c[2]])
    
class ProblemaCamiones(SearchProblem):

    def is_goal(self, state):    
        #El problema termina cuando todos los paquetes estan en su ciudad destino y los camiones estan en alguna sede       
        nuevo_estado = state 
        paquetes,camiones= nuevo_estado     
        for p in paquetes:
            if p[1]!=p[2]: # Verificamos que todos los paquetes estan en ciudad destino 
                return False

        for c in camiones:
            if c[1] not in sedes: # Verificamos que todos los camiones esten en alguna sede
                return False
        return True  #True si todos los paquetes estan en su ciudad destino y todos los camiones estan en alguna sede          


    def actions(self,state):    
        # Estructura de la acción: 
        # [ [(camion), (ciudad),(combustible que me lleva moverme a la ciudad),(paquetes)] ] 
        # ejemplo = [ ['c1','rafaela',0.5],['p1','p2','p3'] ]
        paquetes,camiones=state 
        acciones=[]
        
        for c in camiones:
            # Por cada camion recorro Distancias y busco hacia donde se puede mover segun la ciudad donde esta.
            camion,ciudad,combustible=c          
            for ciudades,distancia in DISTANCIAS.items(): 
                accion_c=[] #accion_c es accion del camion (camion, ciudad, combustible)
                paquetes_llevo=[]
                ciudad_actual,ciudad_destino=ciudades
                if ciudad == ciudad_actual: # Si la ciudad del camion es igual a la ciudad de la distancia
                    destino=ciudad_destino # Entonces destino es la ciudad a donde el camion puede ir
                    combustible_que_gasto=(distancia/100) # Y combusible que le cuesta  

                    if combustible_que_gasto <= combustible: #Si el combustible que llevaria ir es menor al que tiene se puede aplicar la acción                
                        accion_c.append(c[0]) # Guardo que camion es
                        accion_c.append(destino) # Guardo a donde va 
                        accion_c.append(combustible_que_gasto) # Guardo que combustible le insume

                        # Agregamos todos los paquetes que puede llevar
                        for p in paquetes:
                            if p[1]==ciudad: # Si esta en la ciudad del camion
                                if p[1]!=p[2]: # y si el paquete no esta en su destino
                                    paquetes_llevo.append(p[0])  

                        acciones.append([accion_c,paquetes_llevo]) # Agrego para cada camion todos los paquetes

                        #Agregamos combinaciones de paquetes que puede llevar
                        paquetes_tupla=tuple(paquetes_llevo)
                        for p in range(2,len(paquetes_tupla)):
                            if p != 0:
                                combinaciones_paquetes= combinations(paquetes_tupla,p)
                                for cp in combinaciones_paquetes:
                                    acciones.append([accion_c,list(cp)]) # Agrego para cada camion las combinaciones de los paquetes que puede llevar

        return acciones
           
        
    def cost(self,state,action,state2):  
        #print(action[0][2])
        #print("Costo",action[0][2])
        return action[0][2]   

    def result(self, state, action):      
        # El result tiene que: 
        #   - Mover camion de una ciudad a otra 
        #   - Llevar los paquetes 
        #   - Descontar o incrementar combustible     
        
        paquetes,camiones=state      
        camiones_estado=tupla_a_lista(camiones)
        paquetes_estado =tupla_a_lista(paquetes)
        
        camion, paquetes_lleva=action

        camion_elegido=camion[0]
        destino=camion[1]
        combustible_restar=camion[2]
        
        for c in camiones_estado:
            if camion_elegido==c[0]: #Busco el camion que se tiene que mover             
                c[1]=destino #Muevo el camion al destino 
                if destino in sedes: #Si el camion llegó a una sede incremento su combustible
                    for cap in capacidad:
                        if cap[0]==camion_elegido:
                            c[2]=cap[1]
                else: #Si no esta en una sede descuento combustible 
                    c[2]=round(c[2],2)-round(combustible_restar,2) 
                    if c[2]<0:
                        c[2]=0
                
        for pll in paquetes_lleva: #Busco los paquetes que tiene que mover
            for p in paquetes_estado:
                if p[0]==pll: #Si son iguales lo reemplazo en el estado
                    p[1]=destino

        estado = (lista_a_tupla(paquetes_estado),lista_a_tupla(camiones_estado))
        #print ("Accion", action)
        #print("Estado",estado)        

        return lista_a_tupla(estado)   
        

    def heuristic(self, state):
        # La heuristica va a ser la cantidad de paquetes que faltan llegar a su destino multiplicado por los litros de la menor distancia que el camion puede llegar a recorrer 
        
        paquetes,camiones=state      
        camiones_estado=tupla_a_lista(camiones)
        paquetes_estado =tupla_a_lista(paquetes)
        cantidad_paquetes_faltan_llegar=0

        for p in paquetes_estado:
            if p[1]!=p[2]:
                cantidad_paquetes_faltan_llegar+=1

        return (cantidad_paquetes_faltan_llegar*(distancia_minima/100)) 
     

def planear_camiones(metodo, camiones, paquetes):
    # Armar el estado inicial
    estado_inicial=armar_estado_inicial(paquetes,camiones)

    # Inicializar las capacidades de los camiones
    guardar_capacidad(camiones)

    # Llamamos al problema y le pasamos el estado inicial
    problema = ProblemaCamiones(lista_a_tupla(estado_inicial))

    funciones = {
        'breadth_first': breadth_first,
        'depth_first': depth_first,
        'uniform_cost': uniform_cost,
        'greedy': greedy,
        'astar': astar
    }
    funcion_busqueda = funciones[metodo]

    result = funcion_busqueda(problema, graph_search=True)
    itinerario=[]
    
    #Armar itinerario
    for action,state in result.path():
        
        if action!= None:
            camion,paquetes=action
            print(paquetes)
            print(camion)
            
            camion_elegido=camion[0]
            destino=camion[1]
            combustible_restar=camion[2]
        
            paquetes_tupla=lista_a_tupla(paquetes)
            paquetes_lleva=[]

            for p in paquetes:                
                paquetes_lleva.append(p)
            
            itinerario.append((camion_elegido,destino, combustible_restar,tuple(paquetes_lleva)))    
            print(itinerario)

    return itinerario
   
 


if __name__ == '__main__':
    
    #viewer = WebViewer()
	#viewer = ConsoleViewer()
	#viewer = None
	#viewer = BaseViewer()
	    
    itinerario = planear_camiones(
    # método de búsqueda a utilizar. Puede ser: astar, breadth_first, depth_first, uniform_cost o greedy
    metodo="astar", 
	camiones=[
    # id, ciudad actual, y capacidad de combustible máxima (litros)
        ('c1', 'rafaela', 1.5),
    ],
    paquetes=[
        # id, ciudad de origen, y ciudad de destino
        ('p1', 'rafaela', 'lehmann'),
        ('p2', 'rafaela', 'lehmann'),
        ('p3', 'rafaela', 'sunchales'),
        ('p4', 'lehmann', 'rafaela'),
		('p5', 'sunchales', 'susana'),
		('p6', 'rafaela', 'susana'),
    ],
    )
        
    print ('EL RESULTADO ES')
    print (itinerario)
