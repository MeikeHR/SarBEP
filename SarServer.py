from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import UserSettableParameter

from SarModel import SearchAndRescue
from SarAgent import Unit
from SarAgent import MissingPerson

def portrayal_method(agent):
    "Checks if the agent is an instance of a Unit of of a missing person: change portrayal accordingly"
    if agent is None:
        return

    if isinstance(agent, Unit):
        portrayal = {"Shape": "arrowHead",
                     "Filled": "true",
                     "Layer": 0,
                     "Color": "blue",
                     "scale": 1,
                     "heading_x": 1,
                     "heading_y": 0}
    else:
        # is the agent the missing person?
        portrayal = {"Shape": "circle",
                        "Filled": "true",
                        "Layer": 0,
                        "Color": "red",
                        "r": 1}
    return portrayal


grid = CanvasGrid(portrayal_method, 30, 20, 600 ,400)
params = {
    "height": 30,
    "width": 20,
    "search_pattern_slider": UserSettableParameter('choice', "Zoekpatroon", value='Parallel Sweep',
                                          choices=['Parallel Sweep',
                                                   'Expanding Square',
                                                   'Sector Search',
                                                   'Random Search'])
}

server = ModularServer(SearchAndRescue, [grid], "Sar Model", params)
