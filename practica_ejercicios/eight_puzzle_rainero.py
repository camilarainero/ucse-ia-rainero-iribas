from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = (
    (1, 4, 2),
    (0, 3, 5),
    (6, 7, 8),
)

GOAL_STATE = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
)

def posicion_(n,state): #Funcion para devolver la posicion de un numero
    for f, fila in enumerate(state):     #Por cada fila
        for c, value in enumerate(fila):     #Buscar el valor en esa fila
            if value==n:    #Si es igual al numero que me llega por parametro
                return f,c

class EightPuzzle(SearchProblem):
    def is_goal(self, state):
        return state==GOAL_STATE

    def actions(self, state): #Devuelve la lista de acciones que puedo hacer, es decir el numero que muevo con el 0
        #Tengo que encontrar el cero para ver que acciones puedo hacer
        f_cero,c_cero = posicion(0,state)

        acciones=[]

        if f_cero>0:
            acciones.append(state[f_cero-1][c_cero]) #Puedo moverme arriba

        if f_cero<2:
            acciones.append(state[f_cero+1][c_cero]) #Puedo moverme abajo
        
        if c_cero>0:
            acciones.append(state[f_cero][c_cero-1]) #Puedo moverme a la izq

        if c_cero<2:
            acciones.append(state[f_cero][c_cero+1]) #Puedo moverme a la der
        
        return acciones

            
    def result(self, state, action):
        f_pieza_mover, c_pieza_mover= posicion(action,state)
        f_cero,c_cero = posicion(0,state)

        state_modificable=list(list(f) for f in state) #Convierto una tupla de tuplas en una lista de listas

        state_modificable[f_cero][c_cero]=action
        state_modificable[f_pieza_mover][c_pieza_mover]=0

        state_modificable=tuple(tuple(f) for f in state) #Convierto una lista de listas en una tupla de tuplas 
        
        return state_modificable
    
    def cost(self, state1, action, state2):
        return 1


problem = EightPuzzle(INITIAL_STATE)
result = depth_first(problem, graph_search=True, viewer=WebViewer())