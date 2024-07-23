let editor = document.querySelector('#script_editor');


let aceEditor = ace.edit(editor, {
  theme: 'ace/theme/tomorrow_night',
  mode: 'ace/mode/sql',
});

// change font size of ace editor 
aceEditor.setOptions({
    fontSize: "14px"
});


// get the file id from the url
let url = window.location.href;
// get the last part of the url
let get_file_id = url.split('/').pop();
//console.log(get_file_id);

//
// from the ace editor, send the text to the server
//


let timeout = null;

aceEditor.getSession().on('change', function() {
  if (timeout !== null) {
    clearTimeout(timeout);
  }
  timeout = setTimeout(function() {

    let text = aceEditor.getValue();
    let file_id = get_file_id

    // console.log(text);
      fetch('http://127.0.0.1:8000/editor/api/table_transform', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ file_id: file_id, text: text })
        
      })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        triggerFunction();
      })
      .catch(error => console.error('Error:', error));
    
  }, 1000);
});




// trigger when getting response
function triggerFunction() {
  
  // write here
}