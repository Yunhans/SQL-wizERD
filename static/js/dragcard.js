function makeTableDraggable() {
    cards = document.getElementsByClassName('mytable');
    cardHeaders = document.getElementsByClassName('myheader');
    
    for (let i = 0; i < cards.length; i++) {
        let card = cards[i];
        let cardHeader = cardHeaders[i];
    
        cardHeader.addEventListener('mousedown', function(event) {
            card.dataset.initialX = event.clientX;
            card.dataset.initialY = event.clientY;
            card.dataset.isDragging = true;
            cardHeader.style.cursor = 'grabbing';
            event.preventDefault();

    
            function mouseMoveHandler(event) {
                if (card.dataset.isDragging === 'true') {
                    let deltaX = event.clientX - card.dataset.initialX;
                    let deltaY = event.clientY - card.dataset.initialY;
                    card.style.left = card.offsetLeft + deltaX + 'px';
                    card.style.top = card.offsetTop + deltaY + 'px';
                    card.dataset.initialX = event.clientX;
                    card.dataset.initialY = event.clientY;
                }
            }
    
            function mouseUpHandler(event) {
                card.dataset.isDragging = false;
                cardHeader.style.cursor = 'grab';
                document.removeEventListener('mousemove', mouseMoveHandler);
                document.removeEventListener('mouseup', mouseUpHandler);
            }
    
            document.addEventListener('mousemove', mouseMoveHandler);
            document.addEventListener('mouseup', mouseUpHandler);
        });
        cardHeader.addEventListener('mouseover', function(event) {
            cardHeader.style.cursor = 'grab';
        });
    }
}
