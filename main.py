from pyscript import display 

def calculate(evt):
    g1 = float(document.getElementById("g1").value)
    g2 = float(document.getElementById("g2").value)
    g3 = float(document.getElementById("g3").value)

    gwa = (g1 + g2 + g3) / 3
    document.getElementById("result").innerText = f"Your GWA is {gwa:.2f}"

document.getElementById("calc").addEventListener("click", calculate)
