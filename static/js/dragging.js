
const card = document.getElementById('draggableCard');
const cardHeader = document.getElementById('draggableHeader');
const whiteboard = document.getElementById('whiteboard');
const whiteboardBorder = document.getElementById('whiteboard-border');//
let dragOffset = {x: 0, y: 0};
let isDragging = false;

cardHeader.addEventListener('mousedown', (event) => {
    event.preventDefault();
    isDragging = true;
    dragOffset.x = event.clientX - event.target.getBoundingClientRect().left;
    dragOffset.y = event.clientY - event.target.getBoundingClientRect().top;
});

whiteboard.addEventListener('mousemove', (event) => {
    event.preventDefault();
    if (isDragging) {
        //
        const draggableElement = card;
        let newLeft = event.clientX - dragOffset.x;
        let newTop = event.clientY - dragOffset.y;

        // Calculate the bounds of the whiteboard-border
        const borderRect = whiteboardBorder.getBoundingClientRect();
        const cardRect = card.getBoundingClientRect();

        // // Check if the new position is within the bounds of the whiteboard-border
        // if (newLeft < borderRect.left) {
        //     newLeft = borderRect.left;
        // } else if (newLeft + cardRect.width > borderRect.right) {
        //     newLeft = borderRect.right - cardRect.width;
        // }

        // if (newTop < borderRect.top) {
        //     newTop = borderRect.top;
        // } else if (newTop + cardRect.height > borderRect.bottom) {
        //     newTop = borderRect.bottom - cardRect.height;
        // }
        
        // Set the new position of the card
        // const draggableElement = card;
        draggableElement.style.position = 'absolute';
        draggableElement.style.left = event.clientX - dragOffset.x + 'px';
        draggableElement.style.top = event.clientY - dragOffset.y + 'px';
    }
});

document.addEventListener('mouseup', (event) => {
    isDragging = false;
});


