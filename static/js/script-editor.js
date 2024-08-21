// let editor = document.querySelector('#script_editor');


// let aceEditor = ace.edit(editor, {
//   theme: 'ace/theme/tomorrow_night',
//   mode: 'ace/mode/sql',
// });


/*
  --SETTING--
*/

var editor = ace.edit("script_editor");
editor.setTheme("ace/theme/tomorrow_night");
editor.session.setMode("ace/mode/sql");

editor.setOptions({
    fontSize: "14px"
});


/*
 -- PLACEHOLDER --
*/

var placeholderText = "-- Type your script...";
editor.setValue(placeholderText, -1);

// remove the placeholder text if there is any input
editor.on('focus', function() {
  if (editor.getValue() === placeholderText) {
    editor.setValue('');
  }
});

// restore the placeholder if the editor is empty
editor.on('blur', function() {
  if (editor.getValue().trim() === '') {
    editor.setValue(placeholderText, -1);
  }
});




// get the file id from the url
let url = window.location.href;
// get the last part of the url
let get_file_id = url.split('/').pop();
//console.log(get_file_id);

// let updatingFromSQL = false;
// let updateFromERD = false;
let isUserChange = true;


// Debounce function: delay
function debounce(func, delay) {
  let timer;
  return function (...args) {
      clearTimeout(timer);
      timer = setTimeout(() => func.apply(this, args), delay);
  };
}


//--------------------------------------------------------------------------------

// script to erd



// transformation functions

  // send to backend

async function transformScriptToERD(script) {
  let file_id = get_file_id;
  try {
      const response = await fetch("http://127.0.0.1:8000/editor/api/script_to_erd", {
          method: 'POST',
          headers: {
              'Content-Type': 'application/json',
          },
          body: JSON.stringify({
              file_id: file_id,
              text: script
          }),
      });
      
      if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error in transformScriptToERD:', error);
      throw error;
  }
}




// Update functions

  // update the erd display

async function updateERDFromSQL(script) {
  try {
      isUserChange = false;
      const result = await transformScriptToERD(script);

      if (result.status === 'success') {
        // clear existing syntax error

        // update the erd display
        getAllTableData(get_file_id);
      }
      else if(result.status === 'error') {
        // show syntax error
        
      }
  } catch (error) {
      console.error('Error updating ERD from SQL:', error);
  } finally {
      isUserChange = true;
  }
}


// Debounce the update functions
const debouncedSyncEditor = debounce(() => {
  if (isUserChange) {
      const script = editor.getValue();
      updateERDFromSQL(script);
  }
}, 400);


// Add event listeners
editor.getSession().on('change', () => {
  if (isUserChange) {
      debouncedSyncEditor();
  }
});

//--------------------------------------------------------------------------------


// erd to script


// transformation functions
  
  // send to backend
  
async function transformERDToScript() {
  let file_id = get_file_id;
  try {
      const response = await fetch(`http://127.0.0.1:8000/editor/api/erd_to_script/${file_id}`, {
          method: 'GET',
          headers: {
              'Content-Type': 'application/json',
          }
      });
      
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      
      const data = await response.json();
      return data;
  } catch (error) {
      console.error('Error in transformERDToScript:', error);
      throw error;
  }
}


// Update the SQL script display
async function updateSQLFromERD() {
  try {
      isUserChange = false;
      const script = await transformERDToScript();
      editor.setValue(script,-1);
  } catch (error) {
      console.error('Error updating SQL from ERD:', error);
  } finally {
      isUserChange = true;
  }
}

