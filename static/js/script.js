$(function () {

    var selected = null;
    var wordsToDo = [];
    const difficulty = $("#title").data("difficulty");
    const allSounds = {};
    var totalNumWords = 1;
    const hikerCoords = {
        0: {top: 500, left: 325, trans: 1},
        1: {top: 266, left: 140, trans: 1}, 
        2: {top: 245, left: 196, trans: -1}, 
        3: {top: 220, left: 167, trans: 1}, 
        4: {top: 156, left: 240, trans: 1}, 
        5: {top: 202, left: 310, trans: 1}, 
        6: {top: 155, left: 400, trans: 1}, 
        7: {top: 112, left: 405, trans: -1}, 
        8: {top: 128, left: 306, trans: -1}, 
        9: {top: 100, left: 268, trans: 1}, 
        10: {top: 93, left: 333, trans: -1}, 
        11: {top: 59, left: 310, trans: 1},
        12: {top: 0, left: 325, trans: 1}};
    const correct = [];
    const wrong = [];
    const audio = new Audio();

    /**
     * adds a word to the global wordsToDo array
     */
    function addToDo() {
        wordsToDo.push(parseInt($(this)[0].id));
        $(this).hide();
    }

    /**
     * counts the total number of words for global totalNumWords variable and gives progress fractions a corresponding id
     */
    function initializeProgress() {
        totalNumWords += 1;
    }

    /**
    * iterates through the given array to iterate through it's children and add each sound to global allSounds, if it didn't already exist there
    * @param {Array} words 
    */
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

    /**
     * adds a number (based on global difficulty int) of HTMLElements to the given array, randomly chosen from global allSounds array
     * @param {Array} options 
     * @returns 
     */
    function addWrongOptions(options) {
        for (var j = 0; j < difficulty; j++) {
            const randomIndex = Math.floor(Math.random() * Object.keys(allSounds).length);
            const btn = $(`<button id='${Object.keys(allSounds)[randomIndex]}' class='sound btn btn-success d-inline-block' data-ipa='${Object.values(allSounds)[randomIndex]}' type='button' draggable='true'><i class="fa-solid fa-${Object.keys(allSounds)[randomIndex]}"></i></button>`);
            options.push(btn[0]);
        }

        return options;
    }

    /**
     * takes given array of options and appends them to word element in a random order
     * @param {HTMLElement} word 
     * @param {Array} withWrongOptions 
     */
    function displayOptionsRandomly(word, withWrongOptions) {
        const len = withWrongOptions.length;

        for (var i = 0; i < (len); i++) {
            const randomIndex = Math.floor(Math.random() * withWrongOptions.length);
            word.appendChild(withWrongOptions[randomIndex]);
            withWrongOptions.splice(randomIndex, 1);
        }
    }

    /**
     * scrambles all of the options (with new wrong options if necessary) for all words
     */
    function scramble() {
        const words = Array.from($(".dropzone"));

        addToAllSounds(words);
        words.forEach(function (word) {
            const options = Array.from(word.children);

            options.forEach(function (option) {
                word.removeChild(option);
            })

            const withWrongOptions = addWrongOptions(options);
            displayOptionsRandomly(word, withWrongOptions);
        })
    }

    /**
     * displays a new random word from the global wordsToDo array
     */
    function start() {
        const startIndex = Math.floor((Math.random() * wordsToDo.length));
        const start = wordsToDo[startIndex];
        const curr = totalNumWords - wordsToDo.length;
        const curFlavor = $(`#p${curr}`);
        curFlavor.show();
        $(`#${start} .p-flavor`).append(curFlavor);
        $(`#${start}`).show();
        playScript("p" + curr);
    }

    /**
     * allows drag capabilities
     * @param {Event} evt 
     */
    function dragoverHandler(evt) {
        evt.preventDefault();
    }

    /**
     * drops button into submission box, even if hovering over a button that is already there
     * @param {Event} evt 
     */
    function dropHandler(evt) {
        if ($(evt.target).hasClass("sound")) {
            evt.target.parentElement.appendChild(selected);
        }
        else {
            evt.target.appendChild(selected);
        }
    }

    /**
     * evaluate the number of completed questions, and use that number to show the correct number of progress fractions as complete
     */
    function displayProgress() {
        const complete = totalNumWords - wordsToDo.length - 1;
        $(".flavor").hide();
        $($(`#a${complete}`)[0]).show();
        $(".flavor-container").show();

        $("#hiker").css("top", hikerCoords[complete].top);
        $("#hiker").css("left", hikerCoords[complete].left);
        $("#hiker").css("transform", "scaleX(" + hikerCoords[complete].trans+ ")");

        playScript("a"+ complete);
    }

    function playScript(script) {
        if (audio.paused == true) {
            audio.src = `/static/audio/${script}.ogg`;

            audio.play();
        }
    }

    function showFinal() {
        correct.forEach(function(word) {
            const item = document.createElement("ul");
            item.textContent = word;
            $("#complete").append(item);
        })
        wrong.forEach(function(word) {
            const item = document.createElement("ul");
            item.textContent = word;
            $("#wrong").append(item);
        })
        $("#final").show()
    }

    /**
     * evaluates if all words have been completed, if so send to success page, if not, update progress bar
     */
    function checkComplete() {
        const complete = totalNumWords - wordsToDo.length - 1;
        if (complete === 12) {
            $(".question").hide();
            showFinal();
            playScript("final");
            displayProgress();
        }
        else {
            displayProgress();
        }
    }

    /**
     * takes currently chosen elements and moves them to the unchosen container
     * @param {Array} unchosen 
     */
    function putSoundsBack(unchosen) {
        const chosen = Array.from(unchosen.previousElementSibling.children);

        chosen.forEach(function (word) {
            unchosen.appendChild(word);
        })
    }

    /**
     * creates audio elements for the given sounds and play them in order
     * @param {Array} sounds 
     */
    function playSelectedSounds(sounds) {
        const submission = [];
        var counter = 0;

        sounds.forEach(function (sound) {
            const testSound = new Audio(`/static/audio/PHONEME-${sound.id}.mp3`);
            testSound.addEventListener("ended", () => {
                counter = counter + 1;
                if (submission[counter]) {
                    submission[counter].play();
                }
            })
            submission.push(testSound);
        });
        submission[counter].play();
    }

    /**
     * removes the correctly answered question from the global wordsToDo array
     * @param {HTMLElement} question 
     */
    function removeFromToDo(question) {
        const index = wordsToDo.indexOf(parseInt(question.id));

        wordsToDo.splice(index, 1);
    }

    /**
     * takes the given element and extracts the relevant information
     * @param {HTMLElement} answerBox 
     * @returns {string} the current submission as a string of ipa symbols
     */
    function gatherSubmission(answerBox) {
        const guessSounds = Array.from(answerBox.children);
        var submission = "";

        guessSounds.forEach(function (sound) {
            submission = submission.concat(sound.dataset.ipa);
        });

        return submission;
    }

    /**
     * check that the current submission matches that question's answer and update page for true or false possibilities
     * @param {Event} evt 
     */
    function evaluateSubmission(evt) {
        const question = evt.target.parentElement.parentElement.parentElement;
        const answerBox = evt.target.parentElement.previousElementSibling.children[0];
        const unchosen = evt.target.parentElement.previousElementSibling.children[1];
        const submission = gatherSubmission(answerBox);
        const answer = evt.target.dataset.answer;
        const word = question.children[1].children[0].children[0].innerText;
        const word_id = question.id;
        if (submission == answer) {
            removeFromToDo(question);
            correct.push(word);
            $(question).hide();
            $(`#f${word_id}`).removeClass("incomplete");
            $(`#f${word_id}`).removeClass("wrong");
            $(`#f${word_id}`).addClass("done");
            checkComplete();
        }
        else {
            alert("INCORRECT");
            putSoundsBack(unchosen);
            wrong.push(word);
            $(`#f${word_id}`).removeClass("incomplete");
            $(`#f${word_id}`).addClass("wrong");
            $(question).hide();
            $(".flavor").hide();
            $(".wrong").show();
            $(".flavor-container").show();
            playScript("wrong");
        }
    }

    /**
     * given a sound keyword, play the corresponding audio file
     * @param {string} keyword 
     */
    function playSound(keyword) {
        audio.src = `/static/audio/PHONEME-${keyword}.mp3`;

        audio.play();
    }

    function nextQuestion(evt) {
        evt.preventDefault();
        const selected = parseInt(evt.target.alt);
        const complete = totalNumWords - wordsToDo.length - 1;
        if (selected <= complete) {
            alert("completed!");
        }
        else if (selected === complete + 1) {
            $("#intro").hide();
            $(".flavor-container").hide();
            start();
        }
        else {
            alert("you're not quite there yet!");
        }
    }

    // add all words to global wordsToDo array for reference
    $(".question").each(addToDo);

    // get total word count, and set progress bar to 0
    $(".fraction").each(initializeProgress);

    // add wrong options and randomize option order for all questions
    scramble();

    $(".character").on("mouseover", function() {
        playScript("game-intro");
    });

    $(".once").on("mouseover", function() {
        playScript("once");
    })

    // display first question at random
    $("#begin").on("click", function() {
        $("#intro").hide();
        start();
    });

    // event listeners:
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
    $(".evaluate").on("click", function (evt) {
        evaluateSubmission(evt);
    });
    $(".test").on("click", function (evt) {
        const sounds = Array.from(evt.target.parentElement.previousElementSibling.children[0].children);
        playSelectedSounds(sounds);
    });
    $(".reset").on("click", function (evt) {
        putSoundsBack(evt.target.parentElement.previousElementSibling.children[1]);
    });
    $("area").on("click", function (evt) {
        evt.preventDefault();
        if (checkDisplay() === true) {
            nextQuestion(evt);
        }
    })

    function checkDisplay() {
        const fcDisplay = $(".flavor-container").css("display") === "block"
        const introDisplay = $("#intro").css("display") === "block"
        if (fcDisplay || introDisplay) {
            return true;
        }
        else {
            return false;
        }
    }

    window.addEventListener("scroll", function(evt) {
        const topDistance = window.scrollY;
        const layers = document.querySelectorAll("[data-type='parallax']");
        for (var i = 0; i <= layers.length; i++) {
            const depth = layers[i].dataset.depth;
            const movement = -(topDistance * depth);
            console.log(depth);
            const translate3d = 'translate3d(0, ' + movement + 'px, 0)';
            layers[i].style['-webkit-transform'] = translate3d;
            layers[i].style['-moz-transform'] = translate3d;
            layers[i].style['-ms-transform'] = translate3d;
            layers[i].style['-o-transform'] = translate3d;
            layers[i].style.transform = translate3d;
        }
    })
});