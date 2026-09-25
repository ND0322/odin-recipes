from flask import Flask, render_template


app = Flask(__name__)



recipes = {
    "Lasagna": {
        "name": "Lasagna",
        "description": "Tasty",
        "ingredients": [
            "La",
            "sa",
            "gna"
        ],
        "steps": [
            "Cook the Lasagna",
            "Eat it"
        ]
    },

    "Carbonara": {
        "name": "Carbonara",
        "description": "mm",
        "ingredients": [
            "Carb",
            "O",
            "Nara"
        ],
        "steps": [
            "Cook the carb",
            "Cook the nara",
            "Eat it"
        ]
    },

    "Mac": {
            "name": "Mac",
            "description": "mm",
            "ingredients": [
                "mac",
                "cheese"
            ],
            "steps": [
                "Cook the mac",
                "Cook the cheese",
                "Eat it"
            ]
    },

     "Cacioepepe": {
        "name": "Cacioepepe",
        "description": "mm",
        "ingredients": [
            "cacio",
            "pepe"
        ],
        "steps": [
            "Cook the cacio",
            "Cook the pepe",
            "Eat it"
        ]
    }

    
}



@app.route("/")
def home():
    return render_template("index.html", recipes=recipes)

@app.route("/recipe/<name>")
def recipe(name):
    return render_template(f"recipe.html", name=name, steps = recipes[name]['steps'], ingredients = recipes[name]['ingredients'], description = recipes[name]['description'])



if __name__ == '__main__':
    app.run(debug=True)