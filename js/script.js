document.addEventListener('DOMContentLoaded', function() {
  var archivoActual = '';

  setInterval(function() {
    detectarArchivoMP4(archivoActual, function(nuevoArchivo) {
      if (nuevoArchivo !== archivoActual) {
        archivoActual = nuevoArchivo;
        reproducirVideo(archivoActual);
      }
    });
  }, 2000); // Detectar cada 2 segundos (ajusta según tus necesidades)

  function detectarArchivoMP4(archivoActual, callback) {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '../php/detectar_archivo.php?archivo=' + encodeURIComponent(archivoActual), true);
    xhr.onreadystatechange = function() {
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
        var nuevoArchivo = xhr.responseText.trim();
        callback(nuevoArchivo);
      }
    };
    xhr.send();
  }

  function reproducirVideo(archivo) {
    var videoPlayer = document.getElementById('videoPlayer');
    videoPlayer.src = archivo;
  }
});
