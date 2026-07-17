from bokeh.plotting import figure,output_file,show
x_data = [1,2,3,4,5]
y_data = [6,7,2,4,5]
output_file('line_char.html")
        p = figure(title="Simple Line Plot Example",x_axis_label="X Axis",y_axis_label="Y Axis",width=600,height=400)
        p.line(x_data,y_data,legend_label="Growth Trend",line_width=3,line_color="navy")
        show(p)
