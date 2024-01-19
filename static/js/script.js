$(function() {
    var selected = null;
    var wordsToDo = [];
    const list = $("#title").data("list");

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
            displayProgress();
        }
        else {
            alert("INCORRECT");
            $(evt.target.parentElement).hide();
            start();
        }
    })

    $(".reset").on("click", function(evt) {
        const chosen = Array.from(evt.target.previousElementSibling.previousElementSibling.children);
        chosen.forEach(function(word) {
            evt.target.previousElementSibling.appendChild(word);
        })
    })

    function scramble() {
        const zones = Array.from($(".dropzone"));
        zones.forEach(function(zone) {
            const buttons = Array.from(zone.children);
            const len = buttons.length;
            buttons.forEach(function(child) {
                zone.removeChild(child);
            })
            for (var i = 0; i < len; i++) {
                const randomIndex = Math.floor(Math.random() * buttons.length);
                console.log(buttons[randomIndex])
                zone.appendChild(buttons[randomIndex]);
                buttons.splice(randomIndex, 1);
            }
        })
    }
    scramble();

    $(".question").each(function() {
        wordsToDo.push(parseInt($(this)[0].id));
        $(this).hide();
    })

    function start() {
        const startIndex = Math.floor((Math.random() * wordsToDo.length));
        const start = wordsToDo[startIndex];
        $(`#${start}`).show();
    }

    var counter = 1;
    $(".fraction").each(function() {
        $(this).attr('id', `f${counter}`)
        $(this).addClass("incomplete");
        $(this).show();
        counter += 1;
    })

    function displayProgress() {
        if (wordsToDo.length === 0) {
            window.location = `/success?list_id=${list}`;
        }
        else {
            const complete = counter - wordsToDo.length - 1;
            for (var i = 1; i <= complete; i++) {
                $(`#f${i}`).removeClass("incomplete");
                $(`#f${i}`).addClass("done");
            }
        }
    }

    start();

});