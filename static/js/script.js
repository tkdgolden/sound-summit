$(function() {
    var selected = null;
    var wordsToDo = [];
    var wordsCompleted = [];

    function dragoverHandler(evt) {
        evt.preventDefault();
    }

    function dropHandler(evt) {
        if ($(evt.target).hasClass("sound")) {
            evt.target.parentElement.appendChild(selected);
        }
        else {
            evt.target.appendChild(selected);
        }
    }

    $(".sound").on("click", function(evt) {
        evt.preventDefault();
        var keyword = evt.currentTarget.id;
        var audio = new Audio(`/static/audio/PHONEME-${keyword}.mp3`);
        audio.play();
    });

    $(".sound").on("dragstart", function(evt) {
        selected = evt.currentTarget;
    });
    $(".dropzone").on("dragover", dragoverHandler);
    $(".dropzone").on("drop", dropHandler);
    $(".answer").on("dragover", dragoverHandler);
    $(".answer").on("drop", dropHandler);

    $(".evaluate").on("click", function(evt) {
        const words = Array.from(evt.target.nextElementSibling.children);
        var submission = "";
        words.forEach(function(word) {
            submission = submission.concat(word.dataset.ipa);
        });
        const answer = evt.target.dataset.answer;
        if (submission == answer) {
            const index = wordsToDo.indexOf(parseInt(evt.target.parentElement.id));
            wordsToDo.splice(index, 1);
            $(evt.target.parentElement).hide();
            start();
        }
        else {
            alert("INCORRECT");
        }
    })

    $(".reset").on("click", function(evt) {
        const chosen = Array.from(evt.target.previousElementSibling.previousElementSibling.children);
        chosen.forEach(function(word) {
            evt.target.previousElementSibling.appendChild(word);
        })
    })

    $(".question").each(function() {
        wordsToDo.push(parseInt($(this)[0].id));
        $(this).hide();
    })

    function start() {
        const startIndex = Math.floor((Math.random() * wordsToDo.length));
        const start = wordsToDo[startIndex];
        $(`#${start}`).show();
    }

    start();
});