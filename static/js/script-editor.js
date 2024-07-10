let editor = document.querySelector('#script_editor');


let aceEditor = ace.edit(editor, {
  theme: 'ace/theme/tomorrow_night',
  mode: 'ace/mode/sql',
});

// change font size of ace editor 
aceEditor.setOptions({
    fontSize: "14px"
});

const userInfoElement = document.getElementById('userInfo');
const userId = userInfoElement.getAttribute('data-user-id');
console.log(userId);
//turns string into array
const userFile = userInfoElement.getAttribute('data-user-file');

//cosole type of userFile
//str
console.log(userFile);




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

    let file_id = userFile[0][0];
    console.log(file_id);

    // console.log(text);
      fetch('http://127.0.0.1:8000/editor/api/table_transform', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ file_id:file_id,text: text })
        
      })
      .then(response => response.json())
      .then(data => console.log(data))
      .catch(error => console.error('Error:', error));
    
  }, 1000);
});

