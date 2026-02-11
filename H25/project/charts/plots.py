import matplotlib.pyplot as plt
from typing import Dict

def generate_plot(data: Dict, setings: Dict):
    x = data.keys()
    y = data.values()
    col = setings["color"]
    width = setings["width"]
    style = setings["style"]
    mark = setings["mark"]
    x_name = setings["x_name"]
    y_name = setings["y_name"]
    title_name = setings["title_name"]

    plot = plt.plot(x, y, color=col, linewidth=width, linestyle=style, marker=mark)
    plt.xlabel(x_name)
    plt.ylabel(y_name)
    plt.title(title_name)

    plt.show()

def generate_bar(data:Dict, setings: Dict):
    y = data.values()
    x = data.keys()
    col = setings["color"]
    width = setings["width"]

    bar = plt.bar(x, y, color=col, width=(width/4))
    
    plt.show()

def generate_stairs(data:Dict, setings:Dict):
    y =data.values()
    width = setings["width"]

    stairs = plt.stairs(y, linewidth=width)

    plt.show()