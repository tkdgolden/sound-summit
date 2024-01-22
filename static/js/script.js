$(function () {

    var selected = null;
    var wordsToDo = [];
    const list = $("#title").data("list");
    const difficulty = $("#title").data("difficulty");
    const allSounds = {};
    var totalNumWords = 1;

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
        $(this).attr('id', `f${totalNumWords}`)
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
            const btn = $(`<button id='${Object.keys(allSounds)[randomIndex]}' class='sound btn btn-success d-inline-block' data-ipa='${Object.values(allSounds)[randomIndex]}' type='button' draggable='true'>${Object.keys(allSounds)[randomIndex]}</button>`);
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

        $(`#${start}`).show();
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

        for (var i = 1; i <= complete; i++) {
            $(`#f${i}`).removeClass("incomplete");
            $(`#f${i}`).addClass("done");
        }
    }

    /**
     * evaluates if all words have been completed, if so send to success page, if not, update progress bar
     */
    function checkComplete() {
        if (wordsToDo.length === 0) {
            window.location = `/success?list_id=${list}`;
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
            var audio = new Audio(`/static/audio/PHONEME-${sound.id}.mp3`);
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

    /**
     * given a sound keyword, play the corresponding audio file
     * @param {string} keyword 
     */
    function playSound(keyword) {
        var audio = new Audio(`/static/audio/PHONEME-${keyword}.mp3`);

        audio.play();
    }

    // add all words to global wordsToDo array for reference
    $(".question").each(addToDo);

    // get total word count, and set progress bar to 0
    $(".fraction").each(initializeProgress);

    // add wrong options and randomize option order for all questions
    scramble();

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
});