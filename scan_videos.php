<?php
$ignoredFolders = array("temp-capture"); // Carpetas a ignorar

function scanVideos($dir) {
    global $ignoredFolders; // Agrega esta línea para acceder a la variable $ignoredFolders

    $videos = array();
    $files = scandir($dir);
    foreach ($files as $file) {
        if ($file != "." && $file != "..") {
            $path = $dir . DIRECTORY_SEPARATOR . $file;
            if (is_dir($path) && !in_array($file, $ignoredFolders)) {
                $videos = array_merge($videos, scanVideos($path));
            } elseif (is_file($path) && strtolower(pathinfo($path, PATHINFO_EXTENSION)) === "mp4") {
                $videos[] = $path;
            }
        }
    }
    return $videos;
}

$videos = scanVideos("Outplayed");
echo json_encode($videos);
?>
