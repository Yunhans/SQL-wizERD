function receiveMessage(e) {
    const data = JSON.parse(e.data);
    if (data.action === "edit info") {
        console.log("Parent Data received:", data);
        getTableData(data.table_id);
        getReferenceData(file_id);
    }
    else if (data.action === "edit position") {
        console.log("Parent Data received:", data.nodeData);
        updataTablePosition(data.nodeData);
    }
    else if (data.action === "edit table info") {
        console.log("Parent Data received:", data.data);
        updataTableInfo(data.data);
    } 
    else if (data.action === "add table") {
        console.log("Parent Data received:", [data.x, data.y]);
        addTable(data.x, data.y);
    }
}

// 監聽 message 事件
window.addEventListener('message', receiveMessage, false);

function getTableData(table_id) {
    $.ajax({
        url: '/api/table/get/specific/' + table_id,
        type: 'GET',
        crossDomain: true,
        cache: false,
        dataType: 'json',
        timeout: 5000,
        success: function(data){
            // console.log(data);
            passTableData(data);
        },
        error: function () {
            alert("無法連線到伺服器！");    
        }
    });
}

function passTableData(data){
    try {
        const message = JSON.stringify({ task: 'specificTable', table_data: data });

        // Ensure the iframe exists
        var iframe = document.getElementById("whiteboard-react");
        if (!iframe) {
            console.error("Iframe with id 'whiteboard-react' not found");
            return;
        }

        // Check if contentWindow is available
        if (!iframe.contentWindow) {
            console.error("contentWindow is not available");
            return;
        }

        // Send the message
        iframe.contentWindow.postMessage(message, "http://localhost:8080");

    } catch (error) {
        console.error("Failed to send data:", error);
    }
}

function updataTablePosition(nodeData){
    var request = {
        'updates': nodeData
    };

    var data_string = JSON.stringify(request);

    // console.log(data_string);

    $.ajax({
        type: "PUT",
        url: "/api/table/update/position",
        crossDomain: true,
        contentType: "application/json",
        data: data_string,
        cache: false,
        dataType: 'json',
        timeout: 5000,
        statusCode: {
            200: function(response) {
                console.log("Position update successfully");
                // updateSQLFromERD();
            },
        }
    });
}

function updataTableInfo(data){
    const data_string = data;

    // console.log(data_string);

    $.ajax({
        type: "PUT",
        url: "/api/table/update/info",
        crossDomain: true,
        contentType: "application/json",
        data: data_string,
        cache: false,
        dataType: 'json',
        timeout: 5000,
        statusCode: {
            200: function(response) {
                console.log("Table info update successfully");
                updateSQLFromERD();
                getAllTableData(file_id);
            },
        }
    });
}

function getReferenceData(file_id) {
    $.ajax({
        url: '/api/table/get/' + file_id,
        type: 'GET',
        crossDomain: true,
        cache: false,
        dataType: 'json',
        timeout: 5000,
        success: function(data){
            console.log(data);
            passReferenceData(data);
        },
        error: function () {
        alert("無法連線到伺服器！");
        }
    });
}

function passReferenceData(data) {
    try {
        var reference_data = JSON.parse(JSON.stringify(data));


        const simplifiedData = reference_data.map(table => ({
            name: table.name,
            attribute: table.attribute.map(attr => attr.name)
        }));

        console.log(simplifiedData);
        
        // Ensure the iframe exists
        var iframe = document.getElementById("whiteboard-react");
        if (!iframe) {
            console.error("Iframe with id 'whiteboard-react' not found");
            return;
        }
        
        // Check if contentWindow is available
        if (!iframe.contentWindow) {
            console.error("contentWindow is not available");
            return;
        }

        // const message = JSON.stringify({ task: 'reference', reference_data: simplifiedData });

        // Send the message
        iframe.contentWindow.postMessage(JSON.stringify({ task: 'reference', reference_data: simplifiedData }), "http://localhost:8080");

    } catch (error) {
        console.error("Failed to send data:", error);
    }
}

function addTable(x, y){
    var request = {
        'file_id': file_id,
        'name': 'table',
        'attribute': [
            {
                "name": "id",
                "type": "INT",
                "primary_key": true,
                "not_null": false,
                "unique": false,
                "auto_increment": false,
                "default": null
            }
        ],
        'foreign_keys': [],
        'location': {
            'x': x.toFixed(2),
            'y': y.toFixed(2)
        }
    };

    var data_string = JSON.stringify(request);

    // console.log(data_string);

    $.ajax({
        type: "POST",
        url: "/api/table/create",
        crossDomain: true,
        contentType: "application/json",
        data: data_string,
        cache: false,
        dataType: 'json',
        timeout: 5000,
        statusCode: {
            200: function(response) {
                console.log("Table create successfully");
            },
        }
    });
    getAllTableData(file_id);
}