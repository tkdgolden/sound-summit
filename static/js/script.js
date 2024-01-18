$(function() {
    $(".sound").on("click", function(evt) {
        evt.preventDefault();
        var ipa_symbol = evt.currentTarget.id;
        var audio = new Audio(`/static/audio/PHONEME-${ipa_symbol}.mp3`);
        audio.play();
    });
});