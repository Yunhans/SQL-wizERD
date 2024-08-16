export function handleSpecificTable(data) {
    const table_data = data.table_data;
    document.getElementById('inputTableName').value = table_data.name;

    var attribute_html = '';
    var total_index = 0;
    table_data.attribute.forEach(function(value, index){
        attribute_html += '\
            <div class="row mb-2">\
                <div class="col-md-4">\
                    <input type="text" class="form-control" id="inputAttrName-'+ index + '" value='+ value.name +'>\
                </div>\
                <div class="col-md-4">\
                    <input class="form-control" list="datalistOptions" id="inputType-'+ index + '" value='+ value.type +'>\
                    <datalist id="datalistOptions">\
                        <option value="INT">\
                        <option value="VARCHAR(255)">\
                        <option value="DATE">\
                    </datalist>\
                </div>\
                <div class="col-md-4 d-flex justify-content-around">\
                    <!-- primary key -->\
                    <input type="checkbox" class="btn-check" id="key-check-'+ index + '" autocomplete="off" '+ (value.primary_key? "checked" : "") +' >\
                    <label class="btn btn-outline-warning" for="key-check-'+ index + '" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="primary key">\
                        <i class="bi bi-key-fill"></i>\
                    </label>\
                    <!-- notnull -->\
                    <input type="checkbox" class="btn-check" id="null-check-'+ index + '" autocomplete="off" '+ (value.not_null? "checked" : "") +'>\
                    <label class="btn btn-outline-danger" for="null-check-'+ index + '" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="not null">\
                        <i class="bi bi-ban"></i>\
                    </label>\
                    <!-- unique -->\
                    <input type="checkbox" class="btn-check" id="uni-check-'+ index + '" autocomplete="off" '+ (value.unique? "checked" : "") +'>\
                    <label class="btn btn-outline-dark" for="uni-check-'+ index + '" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="unique">\
                        <i class="bi bi-star-fill"></i>\
                    </label>	\
                    <!-- edit -->\
                    <div class="btn-group">\
                        <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">\
                            <i class="bi bi-three-dots"></i>\
                        </button>\
                        <div class="dropdown-menu" style="min-width: 250px;">\
                            <p class="dropdown-header">Other Constraints</p>\
                            <div class="form-check mx-3 mb-2">\
                                <input class="form-check-input" type="checkbox" value="" id="auto-check-'+ index + '"  >\
                                <label class="form-check-label" for="auto-check-'+ index + '">\
                                    auto increment\
                                </label>\
                            </div>\
                            <div class="mx-3">\
                                <label for="default-'+ index + '" class="form-label mb-0">default</label>\
                                <input type="text" class="form-control form-control-sm" id="default-'+ index + '">\
                            </div>\
                            <div class="dropdown-divider"></div>\
                            <p class="dropdown-header">Actions</p>\
                            <button type="button" class="btn btn-sm btn-danger mx-3 mb-2"><i class="bi bi-trash3"></i> Delete attribute</button>\
                        </div>\
                    </div>\
                </div>\
            </div>\
        ';	
        total_index = index;
    });

    // attr rows
    document.getElementById('attribute-container').innerHTML = attribute_html;

    // add attr btn
    document.getElementById('add-attr-btn').innerHTML = '<button type="button" class="btn btn-sm border-0 text-primary mb-0" onclick="addAttributes('+ total_index +')"><i class="bi bi-plus-circle"></i> Add attribute</button>';
}

export function handleTableDrag(nodeData) {
    const message = JSON.stringify({ action: 'edit position', nodeData: nodeData });
    window.parent.postMessage(message, 'http://127.0.0.1:8000/whiteboard/');
}