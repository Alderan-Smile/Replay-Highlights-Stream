<?php
$videoFolder = 'Outplayed';
$ignoredFolders = ['temp-capture'];

function hasNewVideos($dir) {
    global $videoFolder, $ignoredFolders;
    
    $iterator = new RecursiveIteratorIterator(new RecursiveDirectoryIterator($dir), RecursiveIteratorIterator::SELF_FIRST);
    
    foreach ($iterator as $file) {
        if ($file->isFile() && $file->getExtension() === 'mp4' && !in_array($file->getFilename(), $ignoredFolders)) {
            $latestVideoFile = $videoFolder . '/latest.mp4';
            
            if (!file_exists($latestVideoFile) || filemtime($file) > filemtime($latestVideoFile)) {
                copy($file->getPathname(), $latestVideoFile);
                return true;
            }
        }
    }
    
    return false;
}

if (hasNewVideos($videoFolder)) {
    echo 'new_videos';
} else {
    echo 'no_new_videos';
}
?>
