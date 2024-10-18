//console.log("hello world");
let convertButton = document.getElementById("convert-btn");
let output = document.getElementById('output');

//Button click
convertButton.addEventListener('click', () => {
    checkInput()
});


function checkInput() {
    let numberStr = document.getElementById("number").value;
    let number = parseInt(numberStr, 10)
    let msg = ""

    //checking the input
    if (!number) {
        msg = "Please enter a valid number"
    }
    else if (number <= -1) {
        msg = "Please enter a number greater than or equal to 1"
    }
    else if (number >= 4000) {
        msg = "Please enter a number less than or equal to 3999"
    }
    else {
        //convert to roman here
        msg = convertToRoman(number)
    }
    console.log(msg)
    output.innerText = msg

}

function convertToRoman(number) {
    //console.log("Convert to")

    let msg = []
    while (number > 0) {
        //Search through all of the values
        if ((number - 1000) >= 0) {
            console.log("M")
            msg.push("M")
            number -= 1000
        }
        else if ((number - 900) >= 0) {
            console.log("CM")
            msg.push("CM")
            number -= 900
        }
        else if ((number - 500) >= 0) {
            console.log("D")
            msg.push("D")
            number -= 500
        }
        else if ((number - 400) >= 0) {
            console.log("CD")
            msg.push("CD")
            number -= 400
        }
        else if ((number - 100) >= 0) {
            console.log("C")
            msg.push("C")
            number -= 100
        }
        else if ((number - 90) >= 0) {
            console.log("XC")
            msg.push("XC")
            number -= 90
        }
        else if ((number - 50) >= 0) {
            console.log("L")
            msg.push("L")
            number -= 50
        }
        else if ((number - 40) >= 0) {
            console.log("XL")
            msg.push("XL")
            number -= 40
        }
        else if ((number - 10) >= 0) {
            console.log("X")
            msg.push("X")
            number -= 10
        }
        else if ((number - 9) >= 0) {
            console.log("IX")
            msg.push("IX")
            number -= 9
        }
        else if ((number - 5) >= 0) {
            console.log("V")
            msg.push("V")
            number -= 5
        }
        else if ((number - 4) >= 0) {
            console.log("IV")
            msg.push("IV")
            number -= 4
        }
        else if ((number - 1) >= 0) {
            console.log("I")
            msg.push("I")
            number -= 1
        }
    }

    //Output the message to the user
    console.log(msg)
    return msg.join(''); //Take the array of characters and turn into one string
}