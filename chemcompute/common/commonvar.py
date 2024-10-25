import numpy as np

#color_1 blue
c1 = '#4c88cf'
#color_2 green
c2 = '#49a452'
#color_3 red
c3 = '#c33939'
#color_4 deep blue
c4 = '#0000e6'
#color_5 apple
c5 = '#2db300'
#color_6 orange
c6 = '#ff5c33'
#color_7 cyan
c7 = '#41dfe9'
#color_8 brown
c8 = '#86592d'
#color_9 pink
c9 = '#ff66cc'
#color_10 light grey
c10 = '#a6a6a6'
#color_11 grey
c11 = '#737373'
#color_12 black
c12 = '#000000'

lcolor = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]

dict_color = {
    'Ru': c1,
    'C': c2,
    'O': c3
}

dcolors = {
    'black': "#000000",
    'red': "#FF0000",
    'green': "#00C11A",
    'blue': "#0000FF",
    'dred': "#880000",
    'dgreen': "#008800",
    'dblue': "#000088",
    'yellow': "#FFAA00",
    'turquoise': "#00FFFF",
    'pink': "#FF00EE",
    'dyellow': "#888800",
    'dturquoise': "#008888",
    'violet': "#880088",
    'orange': "#FF8800",
    'green2': "#88FF00",
    'blue2': "#8800FF",
    'pink2': "#FF0088",
    'lgreen': "#00FF88",
    'lblue': "#0088FF",
}



def hex_to_RGB(hex_str):
    """ #FFFFFF -> [255,255,255]"""
    #Pass 16 to the integer function for change of base
    return [int(hex_str[i:i+2], 16) for i in range(1,6,2)]

def get_color_gradient(c1, c2, n):
    """
    Given two hex colors, returns a color gradient
    with n colors.
    """
    assert n > 1
    c1_rgb = np.array(hex_to_RGB(c1))/255
    c2_rgb = np.array(hex_to_RGB(c2))/255
    mix_pcts = [x/(n-1) for x in range(n)]
    rgb_colors = [((1-mix)*c1_rgb + (mix*c2_rgb)) for mix in mix_pcts]
    return ["#" + "".join([format(int(round(val*255)), "02x") for val in item]) for item in rgb_colors]
