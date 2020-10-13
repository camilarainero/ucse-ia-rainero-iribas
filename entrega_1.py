from simpleai.search import SearchProblem, breadth_first, depth_first, greedy, astar
from simpleai.search.viewers import WebViewer, BaseViewer, ConsoleViewer


'''Estado inicial podria ser
( 
(rafaela, (paquetes))
(sunchales, (paquetes))
(lehmann, (paquetes))
(susana, (paquetes))
(sc_de_saguier, (paquetes))
(esperanza, (paquetes))
(recreo, (paquetes))
(santa_fe, (paquetes))
(san_vicente, (paquetes))
(santo_tome, (paquetes))
(angelica,(paquetes))
(sauce_viejo(paquetes))
),
(
(camion1,ciudad) 
(camion2,ciudad) 
(camion3,ciudad) ..
)
'''        
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


def tupla_a_lista(t):
    return [list(row) for row in t]

def lista_a_tupla(t):
    return tuple(tuple(row) for row in t)

class ProblemaCamiones(SearchProblem):

    def is_goal(self, state):        

    def actions(self,state):            

    def cost(self, state,action,state2):        

    def result(self, state, action):
        
    def heuristic(self, state):
  
     


def planear_camiones(metodo,camiones,paquetes):
    # Armar el estado inicial
    #INICIAL=
    
    # visor = ConsoleViewer()
    # visor = WebViewer()

    # Llamamos al problema y le pasamos el estado inicial
    problema = ProblemaCamiones(lista_a_tupla(INICIAL))

    '''
    funciones = {
        'breadth_first': breadth_first,
        'depth_first': depth_first,
        'greedy': greedy,
        'astar': astar
    }
    funcion_busqueda = funciones[metodo_busqueda]

    resultado = funcion_busqueda(problema, graph_search=True)#,viewer=visor)
    # print (resultado)
    # print (resultado.path)
    '''
    resultado=problema
    
    return resultado


if __name__ == '__main__':
    
    #viewer = WebViewer()
	#viewer = ConsoleViewer()
	#viewer = None
	#viewer = BaseViewer()

	#metodo = "greedy"
	#metodo = "breadth_first"
	#metodo = "astar"
	#metodo = "depth_first"
	    
    itinerario = planear_camiones(
    # método de búsqueda a utilizar. Puede ser: astar, breadth_first, depth_first, uniform_cost o greedy
    metodo="astar",
    camiones=[
    # id, ciudad de origen, y capacidad de combustible máxima (litros)
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

	#result = planear_camiones('breadth_first', camiones, paquetes)