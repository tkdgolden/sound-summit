$(function() {
    $(".sound").on("click", function(evt) {
        evt.preventDefault();
        var keyword = evt.currentTarget.id;
        var audio = new Audio(`/static/audio/PHONEME-${keyword}.mp3`);
        audio.play();
    });
});