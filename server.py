import mesa
from model import Schelling


def get_happy_agents(model):
    """
    Display data collection in text
    """
    return f"Happy agents: {model.happy}; Agents happy with travel time: {model.happy_with_travel_time}; Agents happy with homophily: {model.happy_with_homophily}"


def schelling_draw(agent):
    """
    Portrayal method for canvas
    """
    # Portrayl for blocks
    portrayal = {"Shape": "rect", "w": 1, "h": 1, "Filled": "true", "Layer": 0, "Color": "white"}

    # Portrayl for the city center
    x, y = agent.pos if agent is not None else (None, None)
    if agent.model.city_center == [(x, y)]:
        portrayal["Color"] = "black" 
        portrayal["Shape"] = "rect"
        portrayal["w"] = 0.8  
        portrayal["h"] = 0.8  
        portrayal["Layer"] = 1  # Ensure the city center is displayed above agents
        return portrayal

    # Portrayal for agents
    if agent is not None:
        portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}
        if agent.type == 0:
            portrayal["Color"] = ["#FF0000", "#FF9999"]
            portrayal["stroke_color"] = "#00FF00"
        else:
            portrayal["Color"] = ["#0000FF", "#9999FF"]
            portrayal["stroke_color"] = "#000000"

    return portrayal


# Set up the canvas
canvas_element = mesa.visualization.CanvasGrid(
    portrayal_method=schelling_draw,
    grid_width=60,
    grid_height=70,
    canvas_width=600,
    canvas_height=700,
)


# Display data collection in a chart
happy_chart = mesa.visualization.ChartModule([{"Label": "happy", "Color": "Black"}, 
                                              {"Label": "happy_with_travel_time", "Color": "Blue"}, 
                                              {"Label": "happy_with_homophily", "Color": "Green"}])


# Set up modifiable paramters 
model_params = {
    "height": 70,
    "width": 60,
    "density": mesa.visualization.Slider(
        name="Agent Density", value=0.7, min_value=0.1, max_value=1.0, step=0.1
    ),
    "minority_pc": mesa.visualization.Slider(
        name="Minority Percentage", value=0.5, min_value=0.00, max_value=1.0, step=0.05
    ),
    "preference": mesa.visualization.Slider(
        name="Preference(0:Homophily, 1:travel time)", value = 0.5, min_value = 0, max_value=1, step=0.1
    )
}

# Set up the server 
server = mesa.visualization.ModularServer(
    model_cls=Schelling,
    visualization_elements=[canvas_element, get_happy_agents, happy_chart],
    name="Schelling Segregation Model",
    model_params=model_params,
)
