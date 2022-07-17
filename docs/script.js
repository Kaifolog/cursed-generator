button.onclick = function () {
        let text1 = document.getElementById('txt1');
        let text2 = document.getElementById('txt2');

        substitutions = JSON.parse(dict);

        raw_string = text1.value;
        revised = "";

        let CURSED_LVL;

        if (cb3.checked) {
                CURSED_LVL = 10;
        }
        else {
                CURSED_LVL = 5;
        }

        function replace_indicator() { return (Math.floor(Math.random() * 10) < CURSED_LVL); };

        function isascii(character) { return /^[\x00-\x7F]*$/.test(character); }

        for (var symbol of raw_string) {

                if (symbol in substitutions && replace_indicator())
                        if (cb1.checked) {
                                let substitution_char = substitutions[symbol][Math.floor(Math.random() * (substitutions[symbol]).length)]
                                if (isascii(substitution_char)) {
                                        revised += substitution_char;
                                }
                                else {
                                        revised += symbol;
                                }

                        }
                        else {
                                revised += substitutions[symbol][Math.floor(Math.random() * (substitutions[symbol]).length)]
                        }
                else {
                        revised += symbol;
                }
        }

        text2.value = revised;
}

cb2.onclick = function () {
        cb2.checked = true;
        cb1.checked = false;
}
cb1.onclick = function () {
        cb1.checked = true;
        cb2.checked = false;
}