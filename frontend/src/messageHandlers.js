export function handleSpecificTable(data) {

    /* eslint-disable no-undef */
    fk_attr=[];
    /* eslint-enable no-undef */
    const table_data = data.table_data;
    document.getElementById('inputTableName').value = table_data.name;

    var attribute_html = '';
    var foreign_key_html = '';
    var total_attrbute_index = 0;
    var total_foreign_key_index = 0;
    table_data.attribute.forEach(function(value, index){
        attribute_html += `
            <div class="row mb-2" id="attribute-row-${index}">
                <div class="col-4">
                    <input type="text" class="form-control" id="inputAttrName-${index}" value=${value.name}>
                </div>
                <div class="col-4">
                    <input class="form-control" list="datalistOptions" id="inputType-${index}" value=${value.type}>
                    <datalist id="datalistOptions">
                        <option value="INT">
                        <option value="VARCHAR(255)">
                        <option value="DATE">
                    </datalist>
                </div>
                <div class="col-4 d-flex justify-content-around">
                    <!-- primary key -->
                    <input type="checkbox" class="btn-check" id="key-check-${index}" autocomplete="off" ${(value.primary_key? "checked" : "")}>
                    <label class="btn btn-outline-warning" for="key-check-${index}" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="primary key">
                        <i class="bi bi-key-fill"></i>
                    </label>
                    <!-- notnull -->
                    <input type="checkbox" class="btn-check" id="null-check-${index}" autocomplete="off" ${(value.not_null? "checked" : "")}>
                    <label class="btn btn-outline-danger" for="null-check-${index}" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="not null">
                        <i class="bi bi-ban"></i>
                    </label>
                    <!-- unique -->
                    <input type="checkbox" class="btn-check" id="uni-check-${index}" autocomplete="off" ${(value.unique? "checked" : "")}>
                    <label class="btn btn-outline-dark" for="uni-check-${index}" data-bs-toggle="tooltip" data-bs-placement="bottom" data-bs-title="unique">
                        <i class="bi bi-star-fill"></i>
                    </label>	
                    <!-- edit -->
                    <div class="btn-group">
                        <button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
                            <i class="bi bi-three-dots"></i>
                        </button>
                        <div class="dropdown-menu shadow" style="min-width: 250px;">
                            <p class="dropdown-header">Other Constraints</p>
                            <div class="form-check mx-3 mb-2">
                                <input class="form-check-input" type="checkbox" id="auto-check-${index}"  >
                                <label class="form-check-label" for="auto-check-${index}">
                                    auto increment
                                </label>
                            </div>
                            <div class="mx-3">
                                <label for="default-${index}" class="form-label mb-0">default</label>
                                <input type="text" class="form-control form-control-sm" id="default-${index}" value=${(value.default === null? "": value.default)}>
                            </div>
                            <div class="dropdown-divider"></div>
                            <p class="dropdown-header">Actions</p>
                            <button type="button" class="btn btn-sm btn-danger mx-3 mb-2" id="delete-attr-btn-${index}" onclick="deleteAttribute(${index})">
                                <i class="bi bi-trash3"></i> Delete attribute
                            </button>
                        </div>
                    </div>
                </div>
            </div>
        `;
        total_attrbute_index = index;
        /* eslint-disable no-undef */
        fk_attr.push(value.name);
        /* eslint-enable no-undef */
    });

    table_data.foreign_keys.forEach(function(value, index){
        foreign_key_html += `
            <div class="row mb-2" id="fk-row-${index}">
                <div class="col-4">
                    <select id="fk-attr-options-${index}" class="form-select">
                        <option value="${value.from.split('.')[1]}" selected>${value.from.split('.')[1]}</option>
                    </select>
                </div>
                <div class="col-7">
                    <div class="input-group">
                        <select id="ref-table-options-${index}" class="form-select" onchange="populateAttributes(this.value, ${index})">
                            <option selected>${value.references.split('.')[0]}</option>
                        </select>
                        <span class="input-group-text rounded-0">.</span>
                        <select id="ref-attr-options-${index}" class="form-select">
                            <option selected>${value.references.split('.')[1]}</option>
                        </select>
                    </div>
                </div>
                <div class="col-1">
                    <button type="button" class="btn btn-outline-danger border-0" onclick="deleteForeignKey(${index})">
                        <i class="bi bi-trash3"></i>
                    </button>  
                </div>
            </div>
        `;
        total_foreign_key_index = index;
    });


    document.getElementById('edit_table_id').innerHTML = table_data.id;

    // attr rows
    document.getElementById('attribute-container').innerHTML = attribute_html;

    // foreign key rows
    document.getElementById('fk-container').innerHTML = foreign_key_html;

    // add attr btn
    document.getElementById('add-attr-btn').innerHTML = `<button type="button" class="btn btn-sm border-0 text-primary mb-0" onclick="addAttribute(${total_attrbute_index})"><i class="bi bi-plus-circle"></i> Add attribute</button>`;

    // add attr btn
    document.getElementById('add-fk-btn').innerHTML = `<button type="button" class="btn btn-sm border-0 text-primary mb-0" onclick="addForeignKey(${total_foreign_key_index})"><i class="bi bi-plus-circle"></i> Add Foreign key</button>`;

    // Reinitialize Bootstrap tooltips
    /* eslint-disable no-undef */
    tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
    tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))
    insertFKOptions(fk_attr);
    /* eslint-enable no-undef */
}

export function handleTableDrag(nodeData) {
    const message = JSON.stringify({ action: 'edit position', nodeData: nodeData });
    window.parent.postMessage(message, 'http://127.0.0.1:8000/whiteboard/');
}

export function handleReference(data) {
    /* eslint-disable no-undef */
    reference_table = data.map(table => table.name);
    reference_data = data;
    // console.log(reference_table);
    insertReferenceTableOptions(reference_table);
    insertReferenceAttrOptions(reference_data);
    /* eslint-enable no-undef */
}