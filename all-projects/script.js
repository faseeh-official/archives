window.onload = function() {
    // Load videos after all content:
    var itemVideos = document.querySelectorAll('video.item-video');
    itemVideos.forEach(function(video) {
        var source = video.querySelector('source');
        source.src = source.getAttribute('data-src');
        video.load();
    });

    // Load images after all content:
    var itemImages = document.querySelectorAll('img.item-img');
    itemImages.forEach(function(img) {
        img.src = img.getAttribute('data-src');
    });
}