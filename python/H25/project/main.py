from charts.plots import generate_bar , generate_plot, generate_stairs
data = {2023: 0, 2024: 40, 2025: 10, 2026: 100}
setings = {"color":"red", "width":2, "style":"-", "mark":"o", "x_name":"year", "y_name":"stomks", "title_name":"stonks"}
if __name__ == "__main__":
    print("start")
    generate_plot(data, setings)
    generate_bar(data, setings)
    generate_stairs(data, setings) 