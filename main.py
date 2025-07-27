from flask import Flask, render_template, request

app = Flask(__name__)

def get_generation(i):
    i = int(i)

    if(i < 1928):
        return "Greatest Generation"
    elif(i >= 1928 and i <= 1945):
        return "Silent Generation"
    elif(i >= 1946 and i <= 1964):
        return "Baby Boomer"
    elif(i >= 1965 and i <= 1980):
        return "Generation X"
    elif(i >= 1981 and i <= 1996):
        return "Millennial"
    elif(i >= 1997 and i <= 2012):
        return "Generation Z"
    elif(i >= 2013 and i <= 2024):
        return "Generation Alpha"
    elif(i == 2025):
        return "Generation Beta"
    else:
        return "This is not a valid year or you are not born yet. Please enter a valid year."

@app.route("/gencheck", methods=["GET", "POST"])
def index():
    generation = None
    if request.method == "POST":
        birth_year = request.form["birthyear"]
        generation = get_generation(birth_year)
    return render_template("gencheck.html", generation=generation)

if __name__ == "__main__":
    app.run(debug=True)