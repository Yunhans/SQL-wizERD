const card = document.getElementById('draggableCard');
const cardHeader = document.getElementById('draggableHeader');
const whiteboard = document.getElementById('whiteboard');
var dragOffset = {x: card.style.left, y: card.style.left};
let isDragging = false;

cardHeader.addEventListener('mousedown', (event) => {
    event.preventDefault();
    isDragging = true;
    const cardRect = card.getBoundingClientRect();
    dragOffset.x = event.clientX - cardRect.left;
    dragOffset.y = event.clientY - cardRect.top;
});

document.addEventListener('mousemove', (event) => {
    event.preventDefault();
    if (isDragging) {
        const draggableElement = card;
        draggableElement.style.left = event.clientX - dragOffset.x + 'px';
        draggableElement.style.top = event.clientY - dragOffset.y + 'px';
    }
});

document.addEventListener('mouseup', (event) => {
    isDragging = false;
});



