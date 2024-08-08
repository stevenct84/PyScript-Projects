import panel as pn
from js import document
pn.extension(sizing_mode="stretch_width")

# Create widgets
slider = pn.widgets.FloatSlider(start=0, end=10, name='Amplitude', width=200)
color_picker = pn.widgets.ColorPicker(name='Color', value='#ff0000', width=200)
shape_selector = pn.widgets.Select(name='Shape', options=['circle', 'square', 'triangle'], width=200)
x_input = pn.widgets.FloatInput(name='X Coordinate', value=150, width=200)
y_input = pn.widgets.FloatInput(name='Y Coordinate', value=150, width=200)
add_button = pn.widgets.Button(name='Add Shape', button_type='primary', width=200)
re_button = pn.widgets.Button(name='Search Shape', button_type='primary', width=200)


# List to store shapes
shapes = []
selected_shape_id = None

def add_shape(event):
    shape_id = len(shapes)
    shape = {
        'id': shape_id,
        'shape': shape_selector.value,
        'amplitude': slider.value,
        'color': color_picker.value,
        'x': x_input.value,
        'y': y_input.value
    }
    shapes.append(shape)
    svg_pane.object = create_svg(shapes)

def update_shape(event):
    if selected_shape_id is not None:
        shape = shapes[selected_shape_id]
        shape['amplitude'] = slider.value
        shape['color'] = color_picker.value
        shape['x'] = x_input.value
        shape['y'] = y_input.value
        svg_pane.object = create_svg(shapes)

def create_svg(shapes):
    svg_width = 400
    svg_height = 400
    svg_elements = []
    for shape in shapes:
        if shape['shape'] == 'circle':
            svg_elements.append(f'''
            <circle id="shape_{shape['id']}" cx="{shape['x']}" cy="{shape['y']}" r="{shape['amplitude'] * 15}" stroke="black" stroke-width="3" fill="{shape['color']}" onclick="shapeClicked({shape['id']})" />
            ''')
        elif shape['shape'] == 'square':
            size = shape['amplitude'] * 30
            svg_elements.append(f'''
            <rect id="shape_{shape['id']}" x="{shape['x'] - size / 2}" y="{shape['y'] - size / 2}" width="{size}" height="{size}" stroke="black" stroke-width="3" fill="{shape['color']}" onclick="shapeClicked({shape['id']})" />
            ''')
        elif shape['shape'] == 'triangle':
            size = shape['amplitude'] * 30
            half_size = size / 2
            svg_elements.append(f'''
            <polygon id="shape_{shape['id']}" points="{shape['x']},{shape['y'] - size} {shape['x'] - half_size},{shape['y'] + half_size} {shape['x'] + half_size},{shape['y'] + half_size}" stroke="black" stroke-width="3" fill="{shape['color']}" onclick="shapeClicked({shape['id']})" />
            ''')
    svg_template = f'''
    <svg width="{svg_width}" height="{svg_height}" xmlns="http://www.w3.org/2000/svg">
        {''.join(svg_elements)}
    </svg>
    <script>
        function shapeClicked(id) {{
            var shape_id_input = document.getElementById('shape_id_input');
            shape_id_input.value = id;
            shape_id_input.dispatchEvent(new Event('change'));
        }}
    </script>
    '''
    return svg_template

# Create an empty HTML pane
svg_pane = pn.pane.HTML(create_svg(shapes), width=400, height=400)

# Hidden input to store the selected shape ID
shape_id_input = pn.widgets.TextInput(name='Shape ID', value='', visible=False)



def search_shape(event):
    # Access the outer shadow root host
    outer_host = document.querySelector('.bk-Row')

    # Create the outer shadow root if it doesn't already exist
    if not outer_host.shadowRoot:
        outer_host.attachShadow({'mode': 'open'})

    # Get the outer shadow root
    outer_shadow_root = outer_host.shadowRoot

    # Access the inner host element
    inner_host = outer_shadow_root.querySelector('.bk-panel-models-markup-HTML')

    # Create the inner shadow root if it doesn't already exist
    if not inner_host.shadowRoot:
        inner_host.attachShadow({'mode': 'open'})

    # Get the inner shadow root
    inner_shadow_root = inner_host.shadowRoot

    figure = inner_shadow_root.querySelector('#shape_0')

    print(figure)

    if figure:
        figure.setAttribute('fill', 'green')



# Set up button click events
add_button.on_click(add_shape)
re_button.on_click(search_shape)
shape_id_input.param.watch(update_shape, 'value')

# Update selected shape ID based on user click
def update_selected_shape_id(event):
    global selected_shape_id
    selected_shape_id = int(event.new)
    shape = shapes[selected_shape_id]
    slider.value = shape['amplitude']
    color_picker.value = shape['color']
    x_input.value = shape['x']
    y_input.value = shape['y']

shape_id_input.param.watch(update_selected_shape_id, 'value')

# Arrange the widgets and the SVG
layout = pn.Row(
    pn.Column(slider, color_picker, shape_selector, x_input, y_input, add_button,re_button, shape_id_input),
    svg_pane,
    height=500,  
    width=800    
)

layout.servable(target="main")
