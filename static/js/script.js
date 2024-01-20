$(function () {
    var selected = null;
    var wordsToDo = [];
    const list = $("#title").data("list");
    const difficulty = $("#title").data("difficulty");
    const allSounds = {};

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

    function scramble() {
        const zones = Array.from($(".dropzone"));
        zones.forEach(function (zone) {
            const buttons = Array.from(zone.children);
            const len = buttons.length;
            for (var i = 0; i < len; i++) {
                if (allSounds[buttons[i].id] == null) {
                    allSounds[buttons[i].id] = $(buttons[i]).data("ipa");
                }
            }
        })
        zones.forEach(function (zone) {
            const buttons = Array.from(zone.children);
            const len = buttons.length;
            buttons.forEach(function (child) {
                zone.removeChild(child);
            })
            for (var j = 0; j < difficulty; j++) {
                const randomIndex = Math.floor(Math.random() * Object.keys(allSounds).length);
                const btn = $(`<button id='${Object.keys(allSounds)[randomIndex]}' class='sound' data-ipa='${Object.values(allSounds)[randomIndex]}' type='button' draggable='true'>${Object.keys(allSounds)[randomIndex]}</button>`);
                buttons.push(btn[0]);
            }
            for (var i = 0; i < (len + difficulty); i++) {
                const randomIndex = Math.floor(Math.random() * buttons.length);
                zone.appendChild(buttons[randomIndex]);
                buttons.splice(randomIndex, 1);
            }

        })
    }

    scramble();

    $(".sound").on("click", function (evt) {
        evt.preventDefault();
        var keyword = evt.currentTarget.id;
        var audio = new Audio(`/static/audio/PHONEME-${keyword}.mp3`);
        audio.play();
    });

    $(".sound").on("dragstart", function (evt) {
        selected = evt.currentTarget;
    });
    $(".dropzone").on("dragover", dragoverHandler);
    $(".dropzone").on("drop", dropHandler);
    $(".answer").on("dragover", dragoverHandler);
    $(".answer").on("drop", dropHandler);

    $(".evaluate").on("click", function (evt) {
        const words = Array.from(evt.target.parentElement.nextElementSibling.children);
        var submission = "";
        words.forEach(function (word) {
            submission = submission.concat(word.dataset.ipa);
        });
        const answer = evt.target.dataset.answer;
        if (submission == answer) {
            const index = wordsToDo.indexOf(parseInt(evt.target.parentElement.parentElement.id));
            wordsToDo.splice(index, 1);
            $(evt.target.parentElement.parentElement).hide();
            start();
            displayProgress();
        }
        else {
            alert("INCORRECT");
            $(evt.target.parentElement.parentElement).hide();
            start();
        }
    })

    $(".test").on("click", function (evt) {
        const words = Array.from(evt.target.parentElement.nextElementSibling.children);
        const submission = [];
        var counter = 0;
        words.forEach(function (word) {
            var audio = new Audio(`/static/audio/PHONEME-${word.id}.mp3`);
            audio.addEventListener("ended", (evt) => {
                counter = counter + 1;
                if (submission[counter]) {
                    submission[counter].play();
                }
            })
            submission.push(audio);
        });
        submission[counter].play();
    })

    $(".reset").on("click", function (evt) {
        const chosen = Array.from(evt.target.previousElementSibling.previousElementSibling.children);
        chosen.forEach(function (word) {
            evt.target.previousElementSibling.appendChild(word);
        })
    })

    $(".question").each(function () {
        wordsToDo.push(parseInt($(this)[0].id));
        $(this).hide();
    })

    function start() {
        const startIndex = Math.floor((Math.random() * wordsToDo.length));
        const start = wordsToDo[startIndex];
        $(`#${start}`).show();
    }

    var counter = 1;
    $(".fraction").each(function () {
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