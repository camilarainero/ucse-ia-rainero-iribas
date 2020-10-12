from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = ( (10,30,60,80,120), () , (300) )

GOAL_STATE = ( (), (10,30,60,80,120) , (_) )

   
class puente(SearchProblem):
    def is_goal(self, state):
        return state==GOAL_STATE

    def actions(self, state):
        acciones=()
        personas_izq=state[0]
        personas_der=state[1]
        tiempo_linterna=state[2]
        combinaciones=itertools.combinations(personas_izq,2) #Combinaciones de a 1 o 2 personas
        for x in combinaciones:    
            personas_a_pasar=x 
            tiempo_personas_a_pasar=max(personas_a_pasar)

            min_personas_derecha=min(personas_der)
            min_personas_pasan(min(personas_que_pasan))   
                   
            if min_personas_derecha<min_personas_pasan:
                tiempo=tiempo_personas_a_pasar+min_personas_derecha
                if tiempo<tiempo_linterna:
                    acciones.append(personas_a_pasar,min_personas_derecha)
            else: 
                tiempo=tiempo_personas_a_pasar+min_personas_pasan
                if tiempo<tiempo_linterna:
                    acciones.append(personas_a_pasar,min_personas_pasan)
        return acciones
            

    def result(self, state, action):
        personas_izquierda=state[0]
        personas_derecha=state[1]
        tiempo_linterna=state[2]

        personas_pasan=action[0]
        persona_volver=action[1]

        #Primero mover las personas
        personas_izquierda.remove(personas_pasan)
        personas_derecha.append(personas_pasan)    

        personas_derecha.remove(persona_volver)
        personas_izquierda.append(persona_volver)

        #Despues descontar tiempo
        tiempo_personas_pasan=max(personas_pasan)
        tiempo_linterna-=tiempo_personas_pasan
        tiempo_linterna-=persona_volver

        estado=(personas_izquierda,personas_derecha,tiempo_linterna)
        return estado
        
    
    def cost(self, state1, action, state2):
        personas_pasan=action[0]
        maximo=max(personas_pasan)
        persona_volver=action[1]
        tiempo_total=maximo+persona_volver

        returno tiempo_total



problem = puente(INITIAL_STATE)
result = depth_first(problem, graph_search=True, viewer=WebViewer())