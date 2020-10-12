from simpleai.search import SearchProblem, breadth_first, depth_first, uniform_cost
from simpleai.search.viewers import WebViewer, BaseViewer

INITIAL_STATE = (
)

GOAL_STATE = (

)

   
class NombreProblema(SearchProblem):
    def is_goal(self, state):
        return state==GOAL_STATE

    def actions(self, state):


    def result(self, state, action):
        
    
    def cost(self, state1, action, state2):


problem = NombreProblema(INITIAL_STATE)
result = depth_first(problem, graph_search=True, viewer=WebViewer())