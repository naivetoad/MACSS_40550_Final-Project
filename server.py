import mesa
from model import Schelling


def get_happy_agents(model):
    """
    Display a text count of how many happy agents there are.
    """
    return f"Happy agents: {model.happy}; Agents happy with travel time: {model.happy_with_travel_time}; Agents happy with homophily: {model.happy_with_homophily}"


def schelling_draw(agent):
    """
    Portrayal Method for canvas
    """
    # Portray generic cell
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0, "Color": "white"}

    # Differentiate portrayal for cities and agents
    x, y = agent.pos if agent is not None else (None, None)
    if agent.model.city_center == [x, y]:
        portrayal["Color"] = "black"  # Set city center color to black
        portrayal["Shape"] = "rect"  # Set shape to rectangle for city center
        portrayal["w"] = 0.8  
        portrayal["h"] = 0.8  
        portrayal["Layer"] = 1  # Ensure city center is drawn above empty cells but below agents
        return portrayal

    # Portrayal for agents
    if agent is not None:
        portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 2}  # Agents are drawn on top
        if agent.type == 0:
            portrayal["Color"] = ["#FF0000", "#FF9999"]
            portrayal["stroke_color"] = "#00FF00"
        else:
            portrayal["Color"] = ["#0000FF", "#9999FF"]
            portrayal["stroke_color"] = "#000000"

    return portrayal


canvas_element = mesa.visualization.CanvasGrid(
    portrayal_method=schelling_draw,
    grid_width=60,
    grid_height=70,
    canvas_width=500,
    canvas_height=800,
)
happy_chart = mesa.visualization.ChartModule([{"Label": "happy", "Color": "Black"}, {"Label": "happy_with_travel_time", "Color": "Blue"}, {"Label": "happy_with_homophily", "Color": "Green"}])

model_params = {
    "height": 70,
    "width": 60,
    "density": mesa.visualization.Slider(
        name="Agent Density", value=0.7, min_value=0.1, max_value=1.0, step=0.1
    ),
    "minority_pc": mesa.visualization.Slider(
        name="Minority Percentage", value=0.5, min_value=0.00, max_value=1.0, step=0.05
    ),
    "preference_ratio": mesa.visualization.Slider(
        name="Preference Ratio (Travel Time to Homophily)", value = 0.5, min_value = 0, max_value=1, step=0.1
    )
}

server = mesa.visualization.ModularServer(
    model_cls=Schelling,
    visualization_elements=[canvas_element, get_happy_agents, happy_chart],
    name="Schelling Segregation Model",
    model_params=model_params,
)
