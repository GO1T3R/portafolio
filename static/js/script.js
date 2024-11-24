// Selección del canvas
const canvas = document.getElementById('neuralCanvas');
const ctx = canvas.getContext('2d');

// Tamaño inicial del canvas
canvas.width = window.innerWidth;
canvas.height = 300;

// Variables para nodos y conexiones
const nodes = [];
const connections = [];
const nodeCount = 30;
let mouse = { x: null, y: null };

// Ajustar para pantallas de alta resolución
function adjustCanvasForHighDPI() {
    const dpi = window.devicePixelRatio || 1; // Detecta el DPI de la pantalla
    const computedStyle = getComputedStyle(canvas); // Obtiene el tamaño visual del canvas

    // Mantén el tamaño visual (CSS)
    const width = parseFloat(computedStyle.getPropertyValue('width'));
    const height = parseFloat(computedStyle.getPropertyValue('height'));

    // Ajusta la resolución interna
    canvas.width = width * dpi;
    canvas.height = height * dpi;

    // Escala el contexto para corregir la proporción de píxeles
    ctx.scale(dpi, dpi);
}

// Llamar a la función para ajustar el canvas
adjustCanvasForHighDPI();

// Crear nodos
for (let i = 0; i < nodeCount; i++) {
    nodes.push({
        x: Math.random() * canvas.width,
        y: Math.random() * canvas.height,
        radius: Math.random() * 3 + 1,
        dx: Math.random() * 2 - 1,
        dy: Math.random() * 2 - 1,
        originalX: Math.random() * canvas.width, // Posición original
        originalY: Math.random() * canvas.height,
        dispersionFactor: 0, // Factor de dispersión
    });
}

// Crear conexiones
function updateConnections() {
    connections.length = 0; // Limpiar conexiones
    for (let i = 0; i < nodes.length; i++) {
        for (let j = i + 1; j < nodes.length; j++) {
            const distance = Math.hypot(nodes[i].x - nodes[j].x, nodes[i].y - nodes[j].y);
            if (distance < 100) {
                connections.push([i, j]);
            }
        }
    }
}

// Dibujar nodos
function drawNodes() {
    nodes.forEach(node => {
        ctx.beginPath();
        ctx.arc(node.x, node.y, node.radius, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(128, 128, 128, 0.7)'; // Color gris y opaco
        ctx.fill();
    });
}

// Dibujar conexiones
function drawConnections() {
    connections.forEach(([i, j]) => {
        const nodeA = nodes[i];
        const nodeB = nodes[j];
        ctx.beginPath();
        ctx.moveTo(nodeA.x, nodeA.y);
        ctx.lineTo(nodeB.x, nodeB.y);
        ctx.strokeStyle = 'rgba(128, 128, 128, 0.3)'; // Líneas opacas
        ctx.lineWidth = 1;
        ctx.stroke();
    });
}

// Animación
function animate() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    nodes.forEach(node => {
        node.x += node.dx;
        node.y += node.dy;

        // Rebotar en los bordes
        if (node.x < 0 || node.x > canvas.width) node.dx *= -1;
        if (node.y < 0 || node.y > canvas.height) node.dy *= -1;

        // Desplazarse del mouse
        if (mouse.x && mouse.y) {
            const dx = node.x - mouse.x;
            const dy = node.y - mouse.y;
            const distance = Math.hypot(dx, dy);

            if (distance < 100) {
                // Empujar los nodos lejos del mouse
                const pushStrength = (100 - distance) / 10; // Fuerza de empuje

                node.x += (dx / distance) * pushStrength; 
                node.y += (dy / distance) * pushStrength;
            }
        }
    });

    updateConnections();
    drawConnections();
    drawNodes();
    requestAnimationFrame(animate);
}

// Ajustar tamaño del canvas al redimensionar
window.addEventListener('resize', () => {
    canvas.width = window.innerWidth;
    canvas.height = 300;
});

// Detectar posición del mouse
canvas.addEventListener('mousemove', e => {
    const rect = canvas.getBoundingClientRect();
    mouse.x = e.clientX - rect.left;
    mouse.y = e.clientY - rect.top;
});

// Reiniciar posición del mouse al salir del canvas
canvas.addEventListener('mouseleave', () => {
    mouse.x = null;
    mouse.y = null;
});

// Iniciar animación
animate();
