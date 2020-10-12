from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

pos_inicial_jugador=(0,0)
pos_enemigo=(1,1)
pos_base_enemigo=(2,2)

#initial_state=(pos_jugador,pos_enemigo,pos_base_enemigo)

def dibujar_tablero(pos_jugador,pos_enemigo,pos_base_enemigo):
#El estado podria ser el teblero 
#((0,0,BE)    
# (0,E,0)
# (J,0,0))

#O sino podria ser ((0,0),(1,1),(2,2)) representando posicion jugador, posicion enemigo, posicion base enemigo

INITIAL_STATE = ((0,0),(1,1),(2,2))
GOAL_STATE = ((2,2))

   
class Dota(SearchProblem):
    def is_goal(self, state):
        return state==GOAL_STATE

    def actions(self, state):
        acciones=()
        #Mover al jugador en posiciones arriba, abajo, izquierda, derecha. 
        #Si donde lo puedo mover esta el enemigo o la base ataco y muevo.

        p_jugador,p_enemigo,p_base=state
        f_jugador, c_jugador=p_jugador
        f_enemigo, c_enemigo=p_enemigo

        if f_jugador+1<2
            #Puedo subir
            f_nueva_jugador=f_jugador+1
            
        if f_jugador[0]-1>0
            #Puedo bajar
            f_nueva_jugador=f_jugador-1

        if c_jugador[1]+1<2
            #Puedo ir a la derecha
            c_nueva_jugador=c_jugador+1

        if c_jugador[1]-1>0
            #Puedo ir a la izquierda
            c_nueva_jugador=c_jugador-1
        

        if f_nueva_jugador,c_nueva_jugador==f_enemigo,c_enemigo: 
            #hacia donde me quiero mover esta el enemigo 
            
        if p_jugador


    def result(self, state, action):
        
    
    def cost(self, state1, action, state2):


problem = NombreProblema(INITIAL_STATE)
result = depth_first(problem, graph_search=True, viewer=WebViewer())