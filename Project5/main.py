from js import document
from pyodide.ffi.wrappers import add_event_listener

svgCanvas = document.getElementById('svgCanvas')
drawCircleButton = document.getElementById('drawCircle')
drawSquareButton = document.getElementById('drawSquare')
drawTriangleButton = document.getElementById('drawTriangle')
rewriteButton= document.getElementById('rewrite')
sizeInput = document.getElementById('size')
posXInput=  document.getElementById('posix')
posYInput=  document.getElementById('posiy')
colorInput= document.getElementById('color')

currentShape = None
currentSize = None

def drawCircle(event):
    global currentShape
    circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle')
    radius = 50
    circle.setAttribute('cx', 100)
    circle.setAttribute('cy', 100)
    circle.setAttribute('r', radius)
    circle.setAttribute('fill', '#ADD8E6')
    circle.setAttribute('stroke', 'blue')
    circle.setAttribute('stroke-width', '2')
    circle.setAttribute('data-type', 'circle')
    add_event_listener(circle, 'click', lambda event: setCurrentShape(circle))
    svgCanvas.appendChild(circle)

def drawSquare(event):
    global currentShape
    square = document.createElementNS('http://www.w3.org/2000/svg', 'rect')
    size = 50
    square.setAttribute('x', 150)
    square.setAttribute('y', 150)
    square.setAttribute('width', size)
    square.setAttribute('height', size)
    square.setAttribute('fill', '#f08080')
    square.setAttribute('stroke', 'blue')
    square.setAttribute('stroke-width', '2')
    square.setAttribute('data-type', 'square')
    add_event_listener(square, 'click', lambda event: setCurrentShape(square))
    svgCanvas.appendChild(square)

def drawTriangle(event):
    global currentShape
    triangle = document.createElementNS('http://www.w3.org/2000/svg', 'polygon')
    triangle.setAttribute('points', "100,10 40,180 160,180")
    triangle.setAttribute('width', '50')
    triangle.setAttribute('height', '50')
    triangle.setAttribute('fill', '#ADD8E6')
    triangle.setAttribute('stroke', 'blue')
    triangle.setAttribute('stroke-width', '2')
    triangle.setAttribute('data-type', 'triangle')
    add_event_listener(triangle, 'click', lambda event: setCurrentShape(triangle))
    svgCanvas.appendChild(triangle)


def rewriteShape(*args):
    global currentShape
    if currentShape:
        #get the color, x, y and size for the figure
        x = int(posXInput.value)
        y = int(posYInput.value)
        size = int(sizeInput.value)
        color = colorInput.value
        if currentShape.getAttribute('data-type') == 'circle':
            currentShape.setAttribute('cx', x)
            currentShape.setAttribute('cy', y)
            currentShape.setAttribute('r', size)
        elif currentShape.getAttribute('data-type') == 'triangle':
            currentShape.setAttribute('points', f"{x},{y} {x-60},{y+170} {x+60},{y+170}")
           
            '''
            It can work: 
            currentShape.setAttribute("transform", f"translate({x},{y})")
            '''
        else:
            currentShape.setAttribute('x', x)
            currentShape.setAttribute('y', y)
            currentShape.setAttribute('width', size)
            currentShape.setAttribute('height', size)
        currentShape.setAttribute('fill', color)


def setCurrentShape(shape):
    global currentShape
    if currentShape:
        currentShape.setAttribute('stroke', 'blue')
    currentShape = shape
    currentShape.setAttribute('stroke', 'green')

    # Update input fields with the shape's current position
    print(currentShape.getAttribute('fill'))
    colorInput.value=currentShape.getAttribute('fill')


    if currentShape.getAttribute('data-type') == 'circle':
        posXInput.value = currentShape.getAttribute('cx')
        posYInput.value = currentShape.getAttribute('cy')
        #update size field
        sizeInput.value = currentShape.getAttribute('r')
    else:
        posXInput.value = currentShape.getAttribute('x')
        posYInput.value = currentShape.getAttribute('y')
        #update size field
        sizeInput.value = currentShape.getAttribute('width')
        sizeInput.value = currentShape.getAttribute('height')




add_event_listener(drawCircleButton, 'click', drawCircle)
add_event_listener(drawSquareButton, 'click', drawSquare)

add_event_listener(rewriteButton, 'click', rewriteShape)
add_event_listener(drawTriangleButton, 'click', drawTriangle)