//Variables globales

//Evitar el submit del formulario vacio
var form = document.getElementById("Uploadcsv");
function handleForm(event) { event.preventDefault(); } 
form.addEventListener('submit', handleForm);

//Validar que el archivo sea un csv y no un campo vacio u otro tipo de archivo
function validarFile(){
    var file = document.getElementById("csvfile").value;
    if (file == null || file == "" ){
        alert("Por favor seleccione un archivo");
        //return false;
    }else{

        extension = file.substring(file.lastIndexOf('.'),file.length);
        // Si la extensión obtenida no está incluida en la lista de valores del atributo "accept", mostrar un error.
        if(document.getElementById('csvfile').getAttribute('accept').split(',').indexOf(extension) < 0) {
            alert('Archivo inválido. No se permite la extensión ' + extension);
            //return false;
        }else{
            //return true;
            upload_csv();
        }
    }
}

// Evitar el reenvio del formulario
if (window.history.replaceState) { // verifica disponibilidad
    window.history.replaceState(null, null, window.location.href);
  }

//Cancelar la subida del archivo csv
var cancel_button = document.getElementById("cancel_button");
cancel_button.addEventListener("click", function(){
    document.getElementById('csvfile').value=""
});

//Cancelar la subida del archivo pdf
var cancel_button_pdf = document.getElementById("cancel_button_pdf");
cancel_button_pdf.addEventListener("click", function(){
    document.getElementById('pdffile').value=""
    close_modal_pdf();
});

// Obtener el crsf token
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

//Subir el archivo
async function upload_csv(){
    //Obtener el archivo
    var file = document.getElementById('csvfile').files[0];
    var data = new FormData();
    data.append('file', file);
    document.getElementById("cancel_button").click();
    const csrftoken = getCookie('csrftoken');
    const request = new Request(
        'upload_csv/', { headers: { 'X-CSRFToken': csrftoken } }
    );
    await fetch(request, {
        method: 'POST',
        mode: 'same-origin',
        body: data,
    })
    .then( res => res.blob())
    .then( blob => {
        if(blob.type == "text/html"){
            let element_map = document.getElementById('success_tic');
            element_map.classList.remove("d-none");
            element_map.classList.add("d-block");
            document.body.classList.add('modal-open');
        }else{
            var a = document.createElement("a");
            a.href = window.URL.createObjectURL(blob);
            a.download = "Errores";
            a.click();
        }
    });
}

function close_success_tic(){
    let modal = document.getElementById("success_tic");
    modal.classList.remove("d-block");
    modal.classList.add("d-none");
    document.body.classList.remove("modal-open");
    reloadAsGet();
}

//Abrir el modal para guardar archivo pdf
function open_modal_pdf(id){
    let element_map = document.getElementById('PdfModal');
    element_map.classList.remove("d-none");
    element_map.classList.add("d-block");
    document.body.classList.add('modal-open');
    num_escritura = document.getElementById("num_escritura");
    num_escritura.value = id;
}

function close_modal_pdf (){
    modal = document.getElementById("PdfModal");
    modal.classList.remove("d-block");
    modal.classList.add("d-none");
    document.body.classList.remove('modal-open');
}

//Validar que el archivo sea un pdf y no un campo vacio u otro tipo de archivo
function validarFilePDF(){
    var file = document.getElementById("pdffile").value;
    if (file == null || file == "" ){
        alert("Por favor seleccione un archivo");
        //return false;
    }else{

        extension = file.substring(file.lastIndexOf('.'),file.length);
        // Si la extensión obtenida no está incluida en la lista de valores del atributo "accept", mostrar un error.
        if(document.getElementById('pdffile').getAttribute('accept').split(',').indexOf(extension) < 0) {
            alert('Archivo inválido. No se permite la extensión ' + extension);
            //return false;
        }else{
            //return true;
            upload_pdf();
        }
    }
}

async function upload_pdf(){
    //Obtener el archivo
    var file = document.getElementById('pdffile').files[0];
    var id = document.getElementById("num_escritura").value;
    var data = new FormData();
    data.append('file', file);
    data.append('id', id);
    const csrftoken = getCookie('csrftoken');
    const request = new Request(
        'upload_pdf/', { headers: { 'X-CSRFToken': csrftoken } }
    );
    await fetch(request, {
        method: 'POST',
        mode: 'same-origin',
        body: data,
    })
    .then(function(response) {
        if (response.ok) {
            return response;
        }
    })
    .then(function(response) {
        if (response.ok) {
            document.getElementById("cancel_button_pdf").click();
            reloadAsGet();
        }
        else{ 
            alert("Error al subir el archivo, revise su conectividad e intentelo nuevamente");
        }
    })
}


function reloadAsGet()
{
    var loc = window.location;
    window.location = loc.protocol + '//' + loc.host + loc.pathname + loc.search;
}