/* Load myVideo after the website is loaded. */
window.addEventListener('load', function() {
    var video = document.getElementById('myVideo');
    video.load();
    video.play();
});