from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

cantidad_jarros=5
initial_state=() #El estado es una lista de elementos con la cantidad de jarros que hay por ejemplo podria ser (0,0,0,0,5)
goal_state=()

def inicializar_jarros(cantidad_jarros-): #Esta funcion armaría el estado inicial dependiendo de la cantidad de jarros
    for x in (cantidad_jarros-1):
        if x<cantidad_jarros-1):
            initial_state.append(0)
        else
            initial_state.append(cantidad_jarros)

def armar_estado_meta(cantidad_jarros): #Esta funcion armaría el estado meta dependiendo de la cantidad de jarros
    for x in (cantidad_jarros-1):
        goal_state.append(1)

   
class JarrosProblem(SearchProblem):
    def is_goal(self, state):
        return state==goal_state

    def actions(self, state): #La accion tendria la estructura (jarro origen,jarro destino) 
        acciones=()
        for jarro_origen, litros_origen in enumerate(state):
            for jarro_destino, litros_destino in enumerate(state):
                if (litros_origen > 0 and self.cantidad_jarros(jarro_destino, litros_destino) > 0):
                    acciones.append((jarro_origen, jarro_destino))
        return acciones


    def result(self, state, action):
        
    
    def cost(self, state1, action, state2):


    def heuristic(self, state):
        #Cantidad de jarros vacios
        #No podria usar como heuristica la cantidad de jarros que no tienen un litro porque sobrestima por ejemplo si tengo el estado (0,2,1,1) en ese caso el costo seria 1 porque me falta llenar el pirmer jarro pero la heuristica seria 2 osea sobreestima porque hay 2 jarros que no tienen un litro

problem = NombreProblema(INITIAL_STATE)
result = depth_first(problem, graph_search=True, viewer=WebViewer())