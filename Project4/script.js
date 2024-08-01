document.addEventListener('DOMContentLoaded', () => {
    const svgCanvas = document.getElementById('svgCanvas');
    const drawCircleButton = document.getElementById('drawCircle');
    const drawSquareButton = document.getElementById('drawSquare');
    const sizeInput = document.getElementById('size');

    let currentShape = null;

    // Function to create a circle
    function drawCircle() {
        const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        const radius = 50;
        circle.setAttribute('cx', 100);
        circle.setAttribute('cy', 100);
        circle.setAttribute('r', radius);
        circle.setAttribute('fill', 'lightblue');
        circle.setAttribute('stroke', 'blue');
        circle.setAttribute('stroke-width', '2');
        circle.setAttribute('data-type', 'circle');
        circle.addEventListener('click', () => setCurrentShape(circle));
        svgCanvas.appendChild(circle);
    }

    // Function to create a square
    function drawSquare() {
        const square = document.createElementNS('http://www.w3.org/2000/svg', 'rect');
        const size = 50;
        square.setAttribute('x', 150);
        square.setAttribute('y', 150);
        square.setAttribute('width', size);
        square.setAttribute('height', size);
        square.setAttribute('fill', 'lightcoral');
        square.setAttribute('stroke', 'red');
        square.setAttribute('stroke-width', '2');
        square.setAttribute('data-type', 'square');
        square.addEventListener('click', () => setCurrentShape(square));
        svgCanvas.appendChild(square);
    }

    // Set the current shape for resizing
    function setCurrentShape(shape) {
        if (currentShape) {
            currentShape.setAttribute('stroke', currentShape.getAttribute('data-type') === 'circle' ? 'blue' : 'red');
        }
        currentShape = shape;
        currentShape.setAttribute('stroke', 'green');
    }


    drawCircleButton.addEventListener('click', drawCircle);
    drawSquareButton.addEventListener('click', drawSquare);
});
