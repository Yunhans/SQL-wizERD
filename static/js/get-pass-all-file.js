var file_id = $("#file_info").text();
var user_id = $("#userInfo").text();

getAllFiles(user_id);

document.getElementById("whiteboard-react").onload = function() {
    // passTableData({ key: 'value' });
    setTimeout(function(){
        // console.log("Executed after 1 second");
        getAllTableData(file_id);
    }, 500);
};

function getAllFiles(user_id) {
    $.ajax({
        type: "GET",
        url: "../api/file/get/" + user_id,
        crossDomain: true,
        cache: false,
        dataType: 'json',
        timeout: 5000,
        success: function (response) {
            updateFiles(response.files);
            console.log(response);
        },
        error: function () {
            alert("抓取檔案失敗");
        }
    });
}

function updateFiles(files){
    $("#file_container").empty();
    var file_html = '';
    var file_link = "''";
    $.each(files, function(index, value) {
        file_html += '\
            <div class="card mb-2" onclick="location.href='+ "'/whiteboard/" + value[0] + "';"+'">\
                <div class="card-header">\
                    '+ value[1] +'\
                </div>';

        var imgSrc = '/static/img/file_imgs/' + value[0] + '.png';
        $.ajax({
            url: imgSrc,
            type: 'HEAD',
            success: function() {
                // If the image exists, use it
                // file_html += '<img class="bd-placeholder-img card-img-top object-fit-cover" width="100%" height="225" src="' + imgSrc + '" alt="文件檔案"></img>';
                file_html += '<img src="' + imgSrc + '" class="card-img-top object-fit-cover" alt="..." height="250px"></div>';
            },
            error: function() {
                // If the image doesn't exist, use a default image
                file_html += '<img src="/static/img/eer_default.png" class="card-img-top object-fit-cover" alt="..." height="250px"></div>';
            },
            async: false // Ensure the request is completed before moving on
        });

        if( file_id === value[0].toString() ){
            document.getElementById("file_name").innerHTML = value[1];
        }
    })
    $("#file_container").append(file_html);
}

function getAllTableData(file_id){
    $.ajax({
        url: '/api/table/get/' + file_id,
        type: 'GET',
        crossDomain: true,
        cache: false,
        dataType: 'json',
        timeout: 5000,
        success: function(data){
            // console.log(data);
            passAllTableData(data);
        },
        error: function () {
            alert("無法連線到伺服器！");
        }
    });
}

function passAllTableData(data) {
    try {
        var table_data = JSON.parse(JSON.stringify(data));

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

        const convertJson = (input) => {
            const task = "allTables";

            const nodes = input.map(table => ({
                id: table.id.toString(),
                type: "table",
                data: {
                    id: table.id.toString(),
                    label: table.name,
                    attribute: table.attribute.map(attr => ({
                        name: attr.name,
                        type: attr.type,
                        isKey: attr.primary_key
                    }))
                },
                position: {
                    x: parseFloat(table.location.x),
                    y: parseFloat(table.location.y)
                }
            }));

            const edges = input.flatMap(table => 
                table.foreign_keys.map(fk => {
                const [sourceTable, sourceColumn] = fk.from.split(".");
                const [targetTable, targetColumn] = fk.references.split(".");
                return {
                    id: `${sourceTable.trim()}.${sourceColumn}->${targetTable.trim()}.${targetColumn}`,
                    source: nodes.find(node => node.data.label === sourceTable.trim()).id,
                    target: nodes.find(node => node.data.label === targetTable.trim()).id,
                    markerStart: 'hasManyReversed',
                    sourceHandle: 'a',
                    targetHandle: 'b',
                    type: "floating"
                };
                })
            );

            return {
                task,
                nodes,
                edges
            };
        };

        const outputJson = JSON.stringify(convertJson(table_data));
        // console.log(JSON.stringify(outputJson, null, 2));


        // Send the message
        iframe.contentWindow.postMessage(outputJson, "http://localhost:8080");

        // console.log("Data sent:", outputJson);

    } catch (error) {
        console.error("Failed to send data:", error);
    }
}