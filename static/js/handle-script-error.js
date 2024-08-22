function showScriptError(errList) {
    var error_html = '';
    errList.forEach(message => {
        error_html += `
            <div class="p-1 text-danger border-start border-danger border-5 bg-dark">
                <div>
                    <i class="bi bi-exclamation-circle-fill me-1"></i>
                    ${message}
                </div>
            </div>
        `;
    });
    document.getElementById('script-error-message').innerHTML = error_html;
}

function showScriptSuccess() {
    document.getElementById('script-error-message').innerHTML = `
        <div class="p-1 text-success border-start border-success border-5 bg-dark">
            <div>
                <i class="bi bi-check-circle-fill me-1"></i>
                No error found
            </div>
        </div>
    `;
}