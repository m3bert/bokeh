from bokeh.plotting import figure, output_file, show

output_file("background.html")

# create a new plot with a title
p = figure(plot_width=400, plot_height=400)
p.background_fill = "beige"

p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=10)

show(p)