from pyscript import document

def checkNum(e):
    num_bers = ["1", "2", "3", "4", "5"]

    num1= document.getElementById("num1").value
    name = "Erin Goat"

    confirm_num = num1 in num_bers

    message = (f'Sorry {name}, your number is not found.', f'Congratulations! {name}, your number is found.')

    document.getElementById("output1").innerHTML = message[confirm_num]