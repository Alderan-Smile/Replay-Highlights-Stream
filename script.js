window.addEventListener('DOMContentLoaded', function() {
    // Función para cargar los videos MP4 encontrados
    function loadVideos() {
      fetch('scan.php')
        .then(function(response) {
          return response.json();
        })
        .then(function(data) {
          var videoContainer = document.getElementById('video-container');
          videoContainer.innerHTML = '';
  
          if (data.videos.length > 0) {
            // Reproducir el último video encontrado
            var video = document.createElement('video');
            var lastVideo = data.videos[data.videos.length - 1];
            video.src = lastVideo;
            video.controls = true;
            video.autoplay = true;
  
            videoContainer.appendChild(video);
          } else {
            // Mostrar un mensaje si no se encontraron videos
            videoContainer.innerHTML = 'No se encontraron videos MP4.';
          }
  
          // Mostrar en consola la cantidad de videos encontrados
          console.log('Se encontraron ' + data.videos.length + ' videos MP4.');
        })
        .catch(function(error) {
          console.error('Error al cargar los videos:', error);
        });
    }
  
    // Función para iniciar la observación de cambios en la carpeta
    function startFileObserver() {
      var folder = 'videos'; // Ruta relativa a la ubicación del archivo script.js
      var ignoredFolders = ['temp-capture'];
      
      // Crear un observador de cambios en el sistema de archivos
      var fileObserver = new FileSystemWatcher();
      fileObserver.observe(folder);
      
      // Evento que se dispara cuando se detectan cambios en la carpeta
      fileObserver.onchange = function(fileList) {
        var newVideos = [];
        
        // Filtrar solo los archivos MP4 y que no se encuentren en carpetas ignoradas
        fileList.forEach(function(file) {
          if (file.name.toLowerCase().endsWith('.mp4')) {
            var skipFile = false;
            
            ignoredFolders.forEach(function(ignoredFolder) {
              if (file.path.toLowerCase().includes(ignoredFolder.toLowerCase())) {
                skipFile = true;
              }
            });
            
            if (!skipFile) {
              newVideos.push(file.path);
            }
          }
        });
        
        if (newVideos.length > 0) {
          console.log('Se detectaron nuevos videos MP4:', newVideos);
        }
        
        // Actualizar la lista de videos si se encontraron nuevos videos
        if (newVideos.length > 0) {
          loadVideos();
        }
      };
      
      // Iniciar la observación de cambios
      fileObserver.start();
    }
  
    // Llamar a la función para cargar los videos al cargar la página
    loadVideos();
  
    // Iniciar la observación de cambios en la carpeta cada 5 segundos
    setInterval(startFileObserver, 5000);
  });
  

// window.addEventListener('DOMContentLoaded', function() {
//     // Función para cargar los videos MP4 encontrados
//     function loadVideos() {
//       fetch('scan.php')
//         .then(function(response) {
//           return response.json();
//         })
//         .then(function(data) {
//           var videoContainer = document.getElementById('video-container');
//           videoContainer.innerHTML = '';
          
//           if (data.videos.length > 0) {
//             // Reproducir el último video encontrado
//             var video = document.createElement('video');
//             var lastVideo = data.videos[data.videos.length - 1];
//             video.src = lastVideo;
//             video.controls = true;
//             video.autoplay = true;
            
//             videoContainer.appendChild(video);
//           } else {
//             // Mostrar un mensaje si no se encontraron videos
//             videoContainer.innerHTML = 'No se encontraron videos MP4.';
//           }
          
//           // Mostrar en consola la cantidad de videos encontrados
//           console.log('Se encontraron ' + data.videos.length + ' videos MP4.');
//         })
//         .catch(function(error) {
//           console.error('Error al cargar los videos:', error);
//         });
//     }
    
//     // Llamar a la función para cargar los videos al cargar la página
//     loadVideos();
    
//     // Actualizar los videos cada 5 segundos
//     setInterval(loadVideos, 5000);
//   });