from pyscript import document

def set_svg_content(svg_content):
    # Inject SVG content into the panel
    svg_panel = document.querySelector("svg-panel")
    svg_panel.innerHTML = svg_content

def create_circle(event):
    svg_content = '''
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <circle cx="100" cy="100" r="80" stroke="black" stroke-width="3" fill="red" />
    </svg>
    '''
    svg_panel = document.querySelector("svg-panel")
    svg_panel.innerHTML = svg_content
    #set_svg_content(svg_content)

def create_square(event):
    svg_content = '''
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <rect x="50" y="50" width="100" height="100" stroke="black" stroke-width="3" fill="blue" />
    </svg>
    '''
    svg_panel = document.querySelector("svg-panel")
    svg_panel.innerHTML = svg_content
    #set_svg_content(svg_content)

def create_triangle(event):
    svg_content = '''
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <polygon points="100,20 20,180 180,180" stroke="black" stroke-width="3" fill="green" />
    </svg>
    '''
    svg_panel = document.querySelector("svg-panel")
    svg_panel. = svg_content
    #set_svg_content(svg_content)

def create_diamond(event):
    svg_content = '''
    <svg width="200" height="200" xmlns="http://www.w3.org/2000/svg">
        <polygon points="100,20 180,100 100,180 20,100" stroke="black" stroke-width="3" fill="yellow" />
    </svg>
    '''
    svg_panel = document.querySelector("svg-panel")
    svg_panel.innerHTML = svg_content
    #set_svg_content(svg_content)

