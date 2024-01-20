$(function () {

    var selected = null;
    var wordsToDo = [];
    const list = $("#title").data("list");
    const difficulty = $("#title").data("difficulty");
    const allSounds = {};
    var totalNumWords = 1;

    function addToDo() {
        wordsToDo.push(parseInt($(this)[0].id));
        $(this).hide();
    }

    function initializeProgress() {
        $(this).attr('id', `f${totalNumWords}`)
        $(this).addClass("incomplete");
        $(this).show();
        totalNumWords += 1;
    }

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
        const words = Array.from($(".dropzone"));

        addToAllSounds(words);
        words.forEach(function (word) {
            const options = Array.from(word.children);

            options.forEach(function (option) {
                word.removeChild(option);
            })

            const withWrongOptions = addWrongOptions(options);
            console.log(allSounds);
            displayOptionsRandomly(word, withWrongOptions);
        })
    }

    function displayOptionsRandomly(word, withWrongOptions) {
        const len = withWrongOptions.length;

        for (var i = 0; i < (len); i++) {
            const randomIndex = Math.floor(Math.random() * withWrongOptions.length);
            word.appendChild(withWrongOptions[randomIndex]);
            withWrongOptions.splice(randomIndex, 1);
        }
    }

    function addWrongOptions(options) {
        for (var j = 0; j < difficulty; j++) {
            const randomIndex = Math.floor(Math.random() * Object.keys(allSounds).length);
            const btn = $(`<button id='${Object.keys(allSounds)[randomIndex]}' class='sound' data-ipa='${Object.values(allSounds)[randomIndex]}' type='button' draggable='true'>${Object.keys(allSounds)[randomIndex]}</button>`);
            options.push(btn[0]);
        }

        return options;
    }

    function addToAllSounds(words) {
        words.forEach(function (word) {
            const options = Array.from(word.children);
            const len = options.length;

            for (var i = 0; i < len; i++) {
                if (allSounds[options[i].id] == null) {
                    allSounds[options[i].id] = $(options[i]).data("ipa");
                }
            }
        })
    }

    function start() {
        const startIndex = Math.floor((Math.random() * wordsToDo.length));
        const start = wordsToDo[startIndex];

        $(`#${start}`).show();
    }

    function checkComplete() {
        if (wordsToDo.length === 0) {
            window.location = `/success?list_id=${list}`;
        }
        else {
            displayProgress();
        }
    }

    function displayProgress() {
        const complete = totalNumWords - wordsToDo.length - 1;

        for (var i = 1; i <= complete; i++) {
            $(`#f${i}`).removeClass("incomplete");
            $(`#f${i}`).addClass("done");
        }
    }

    function putSoundsBack(unchosen) {
        const chosen = Array.from(unchosen.previousElementSibling.children);

        chosen.forEach(function (word) {
            unchosen.appendChild(word);
        })
    }

    function playSelectedSounds(words) {
        const submission = [];
        var counter = 0;

        words.forEach(function (word) {
            var audio = new Audio(`/static/audio/PHONEME-${word.id}.mp3`);
            audio.addEventListener("ended", () => {
                counter = counter + 1;
                if (submission[counter]) {
                    submission[counter].play();
                }
            })
            submission.push(audio);
        });
        submission[counter].play();
    }

    function evaluateSubmission(evt) {
        const question = evt.target.parentElement.parentElement;
        const answerBox = evt.target.parentElement.nextElementSibling;
        const unchosen = evt.target.parentElement.nextElementSibling.nextElementSibling;
        const submission = gatherSubmission(answerBox);
        const answer = evt.target.dataset.answer;

        if (submission == answer) {
            removeFromToDo(question);
            $(question).hide();
            start();
            checkComplete();
        }
        else {
            alert("INCORRECT");
            putSoundsBack(unchosen);
            $(question).hide();
            start();
        }
    }

    function removeFromToDo(question) {
        const index = wordsToDo.indexOf(parseInt(question.id));

        wordsToDo.splice(index, 1);
    }

    function gatherSubmission(answerBox) {
        const guessSounds = Array.from(answerBox.children);
        var submission = "";

        guessSounds.forEach(function (sound) {
            submission = submission.concat(sound.dataset.ipa);
        });

        return submission;
    }

    function playSound(keyword) {
        var audio = new Audio(`/static/audio/PHONEME-${keyword}.mp3`);

        audio.play();
    }

    $(".question").each(addToDo);

    $(".fraction").each(initializeProgress);

    scramble();

    start();

    $(".sound").on("click", function (evt) {
        evt.preventDefault();
        var keyword = evt.currentTarget.id;
        playSound(keyword);
    });

    $(".sound").on("dragstart", function (evt) {
        selected = evt.currentTarget;
    });
    $(".dropzone").on("dragover", dragoverHandler);
    $(".dropzone").on("drop", dropHandler);
    $(".answer").on("dragover", dragoverHandler);
    $(".answer").on("drop", dropHandler);

    $(".evaluate").on("click", function(evt) {
        evaluateSubmission(evt);
    });

    $(".test").on("click", function (evt) {
        const words = Array.from(evt.target.parentElement.nextElementSibling.children);
        playSelectedSounds(words);
    });

    $(".reset").on("click", function(evt) {
        putSoundsBack(evt.target.previousElementSibling);
    });
});