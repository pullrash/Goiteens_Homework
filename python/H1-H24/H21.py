colors = {
        "чорний":"R=0, G=0, B=0",
        "червоний":"R=255, G=0, B=0",
        "жовтий":"R=255, G=255, B=0",
        "зелений":"R=0, G=255, B=0",
        "фіолетовий":"R=127, G=0, B=255",
        "синій":"R=0, G=0, B=255",
        "оранжевий":"R=200, G=100, B=0",
        "білий":"R=255, G=255, B=255"
}

while True: 
    user_color = input("введіть коляр ").lower()
    if user_color in colors:
        str_rgb = colors[user_color]
        red = str_rgb[str_rgb.index("R")+2:str_rgb.index(",")]
        grean = str_rgb[str_rgb.index("G")+2:str_rgb.index("B")-2]
        blue = str_rgb[str_rgb.index("B")+2:]
        print(f"\033[38;2;{red};{grean};{blue}m{str_rgb}\033[0m")
    else:
        print("колір не знайдено")
        break