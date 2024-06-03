// 取得 whiteboard 元素
var whiteboard = document.getElementById('whiteboard');

// 防止滾輪滾動的預設行為
whiteboard.addEventListener('wheel', function(event) {
    event.preventDefault();
});

// 定義變數以儲存滑鼠按下時的初始位置
var initialX = 0;
var initialY = 0;
var isDragging = false;

// 為 whiteboard 元素新增 'mousedown' 事件監聽器以捕捉滑鼠按下事件
whiteboard.addEventListener('mousedown', function(event) {
    // 儲存滑鼠按下時的初始位置
    initialX = event.clientX;
    initialY = event.clientY;

    // 標記為拖動狀態
    isDragging = true;

    // 防止文字選取
    event.preventDefault();
});

// 添加滑鼠移動事件監聽器
document.addEventListener('mousemove', function(event) {
    // 檢查是否處於拖動狀態
    if (isDragging) {
        // 計算滑鼠移動的距離
        var deltaX = event.clientX - initialX;
        var deltaY = event.clientY - initialY;

        // 更新 whiteboard 的捲動位置
        whiteboard.scrollLeft -= deltaX;
        whiteboard.scrollTop -= deltaY;

        // 更新初始位置
        initialX = event.clientX;
        initialY = event.clientY;
    }
});

// 為 whiteboard 元素新增 'mouseup' 事件監聽器以捕捉滑鼠釋放事件
document.addEventListener('mouseup', function(event) {
    // 標記為非拖動狀態
    isDragging = false;
});
