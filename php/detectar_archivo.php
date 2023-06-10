<?php
function buscarNuevoArchivoMP4($directorio, $archivoActual) {
  $carpetasIgnoradas = ['temp-capture']; // Carpeta(s) a ignorar

  $archivos = [];
  $directorioActual = new RecursiveDirectoryIterator($directorio, RecursiveDirectoryIterator::SKIP_DOTS);
  $iterador = new RecursiveIteratorIterator($directorioActual, RecursiveIteratorIterator::SELF_FIRST);

  foreach ($iterador as $ruta => $objeto) {
    if ($objeto->isFile() && $objeto->getExtension() === 'mp4') {
      $carpetaPadre = $objeto->getPathInfo()->getFilename();
      if (!in_array($carpetaPadre, $carpetasIgnoradas)) {
        $archivos[] = $ruta;
      }
    }
  }

  $indiceArchivoActual = array_search($archivoActual, $archivos);
  if ($indiceArchivoActual !== false && isset($archivos[$indiceArchivoActual + 1])) {
    return $archivos[$indiceArchivoActual + 1];
  } else {
    return '';
  }
}

$directorio = '../Outplayed'; // Ruta de la carpeta de videos local
$archivoActual = isset($_GET['archivo']) ? $_GET['archivo'] : '';
$nuevoArchivoMP4 = buscarNuevoArchivoMP4($directorio, $archivoActual);
echo $nuevoArchivoMP4;
?>
