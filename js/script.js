window.addEventListener('DOMContentLoaded', function() {
  // Obtener el elemento de video
  var video = document.getElementById('video');

  // Variable para almacenar la URL del último video creado
  var lastVideoUrl = null;

  // Función para cargar y reproducir el video
  function loadVideo() {
    fetch('scan.php')
      .then(function(response) {
        return response.json();
      })
      .then(function(data) {
        var videos = data.videos;

        // Verificar si se encontraron videos
        if (videos.length > 0) {
          // Obtener la URL del último video creado
          var lastVideo = videos[videos.length - 1];
          
          // Verificar si el último video es diferente al anterior
          if (lastVideo !== lastVideoUrl) {
            // Actualizar la fuente del video
            video.src = lastVideo;
            
            // Almacenar la URL del último video como referencia
            lastVideoUrl = lastVideo;
          }
        }
      })
      .catch(function(error) {
        console.error('Error al cargar los videos:', error);
      });
  }

  // Llamar a la función para cargar y reproducir el video al cargar la página
  loadVideo();

  // Actualizar el video cada 5 segundos
  setInterval(loadVideo, 5000);
});