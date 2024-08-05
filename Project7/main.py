import panel as pn
from panel.pane import SVG
from io import BytesIO

pn.extension(sizing_mode="stretch_width")

# Create widgets
slider = pn.widgets.FloatSlider(start=0, end=10, name='Amplitude', width=200)
color_picker = pn.widgets.ColorPicker(name='Color', value='#ff0000', width=200)
shape_selector = pn.widgets.Select(name='Shape', options=['circle', 'square', 'triangle'], width=200)
x_input = pn.widgets.FloatInput(name='X Coordinate', value=150, width=200)
y_input = pn.widgets.FloatInput(name='Y Coordinate', value=150, width=200)

def update_svg(amplitude, color, shape, x, y):
    svg_width = 300
    svg_height = 300
    # Create a simple SVG dynamically based on the slider value and selected color and shape
    if shape == 'circle':
        svg_template = f'''
        <svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
          <circle cx="{x}" cy="{y}" r="{amplitude * 15}" stroke="black" stroke-width="3" fill="{color}" />
        </svg>
        '''
    elif shape == 'square':
        size = amplitude * 30
        svg_template = f'''
        <svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
          <rect x="{x - size / 2}" y="{y - size / 2}" width="{size}" height="{size}" stroke="black" stroke-width="3" fill="{color}" />
        </svg>
        '''
    elif shape == 'triangle':
        size = amplitude * 30
        half_size = size / 2
        svg_template = f'''
        <svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
          <polygon points="{x},{y - size} {x - half_size},{y + half_size} {x + half_size},{y + half_size}" stroke="black" stroke-width="3" fill="{color}" />
        </svg>
        '''
    return SVG(BytesIO(svg_template.encode('utf-8')), width=svg_width, height=svg_height)

svg_pane = pn.bind(update_svg, slider, color_picker, shape_selector, x_input, y_input)

# Arrange the widgets and the SVG, and set the height and width of the Row layout
layout = pn.Row(
    pn.Column(slider, color_picker, shape_selector, x_input, y_input),
    svg_pane,
    height=600,  
    width=1200   
)

layout.servable(target="main")
