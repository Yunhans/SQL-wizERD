let editor = document.querySelector('#script_editor');


let aceEditor = ace.edit(editor, {
  theme: 'ace/theme/ambiance',
  mode: 'ace/mode/sql',
});

// change font size of ace editor 
aceEditor.setOptions({
    fontSize: "16px"
});

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


    // console.log(text);
      fetch('http://127.0.0.1:8000/editor/api/table_transform', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
    
  }, 1000);
});