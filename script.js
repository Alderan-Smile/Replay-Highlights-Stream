document.addEventListener("DOMContentLoaded", function() {
    var videoPlayer = document.getElementById("videoPlayer");
    var currentIndex = 0;
    var videos = [];

    loadVideos();
    setInterval(loadVideos, 5000); // Cada 5 segundos

    function loadVideos() {
        var xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4 && this.status === 200) {
                var newVideos = JSON.parse(this.responseText);
                if (newVideos.length > videos.length) {
                    videos = newVideos;
                    playNextVideo();
                }
            }
        };
        xhttp.open("GET", "scan_videos.php", true);
        xhttp.send();
    }

    function playNextVideo() {
        if (currentIndex < videos.length) {
            videoPlayer.src = videos[currentIndex];
            currentIndex++;
        } else {
            currentIndex = 0;
            videos = [];
            videoPlayer.src = "";
        }
    }

    videoPlayer.addEventListener("ended", function() {
        playNextVideo();
    });
});
