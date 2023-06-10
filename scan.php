<?php
function scanFolder($folder, $ignoredFolders = []) {
  $files = [];

  $dir = new RecursiveDirectoryIterator($folder);
  $iterator = new RecursiveIteratorIterator($dir);

  foreach ($iterator as $file) {
    if ($file->isFile() && strtolower($file->getExtension()) === 'mp4') {
      $skipFile = false;

      foreach ($ignoredFolders as $ignoredFolder) {
        if (strpos($file->getPath(), $ignoredFolder) !== false) {
          $skipFile = true;
          break;
        }
      }

      if (!$skipFile) {
        $files[] = $file->getPathname();
      }
    }
  }

  return $files;
}

$folder = 'Outplayed';
$ignoredFolders = ['temp-capture'];

$videos = scanFolder($folder, $ignoredFolders);

echo json_encode(['videos' => $videos]);
?>
