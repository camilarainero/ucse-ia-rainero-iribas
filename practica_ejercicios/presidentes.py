from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = ( (cap,cap,com,com,cen,cen),(),() )

GOAL_STATE = ( (),(),(ca,ca,co,co,ce,ce) )

def validaciones(state,p,so):
    sala1=state[0]
    sala2=state[1]
    sala3=state[2]

    if so == 1:
        sala1.remove(p)
        sala2.append(p)
    else:
        sala2.remove(p)
        sala3.append(p)

    estado=sala1,sala2,sala3

    estan_conspirando=conspiracion(estado)
    estan_aislados=aislados(estado)

    if (estan_conspirando==False) and (estan_aislados==False):
        return True
    else:
        return False
 

#Valida que no haya dos presidentes de la misma facción en la misma sala solo
def conspiracion(estado):
    sala1=state[0]
    sala2=state[1]
    sala3=state[2]

    if ((len(sala1)==2) and (sala1[0]==sala1[1])) or ((len(sala2)==2) and (sala2[0]==sala2[1])) or ((len(sala3)==2) and (sala3[0]==sala3[1])) : #Hay dos presidentes solos conspirando en una misma sala
        return True
    else: 
        return False


#Valida que no esten separados por mas de una sala
def aislados(estado)
    sala1=state[0]
    sala2=state[1]
    sala3=state[2]

    if (("cap" in sala1) and ("cap" in sala3)) or (("com" in sala1) and ("com" in sala3)) or (("cen" in sala1) and ("cen" in sala3)):
        return True
    else:
        return False
    

class presidentes(SearchProblem):
    def is_goal(self, state):
        return state==GOAL_STATE

    def actions(self, state):
        acciones=()
        sala1=state[0]
        sala2=state[1]
        sala3=state[2]

        combinaciones_sala1_a_sala2=itertools.combinations(sala1,2)
        combinaciones_sala2_a_sala3=itertools.combinations(sala2,2)

        #Definir presidentes a mover
        for p in combinaciones_sala1_a_sala2:
            #Si quiero mover de sala 1 a sala2
            if validaciones(state,p,1)==True
                acciones.append(p,1)
        for p in combinaciones_sala2_a_sala3:
            #Si quiero mover de sala 2 a sala 3
            if validaciones(state,p,2)==False
                if validaciones==True
                    acciones.append(p,1)

        return acciones

    def result(self, state, action):
        sala1=state[0]
        sala2=state[1]
        sala3=state[2]

        presidentes_mover,so=action

        if so == 1:
            sala1.remove(p)
            sala2.append(p)
        else:
            sala2.remove(p)
            sala3.append(p)

        estado=sala1,sala2,sala3
        return estado
        
    def cost(self, state1, action, state2):
        return 1

    def heuristic(self, state):
        sala3=state[2]

        return (6-len(sala3))



problem = presidentes(INITIAL_STATE)
result = depth_first(problem, graph_search=True, viewer=WebViewer())