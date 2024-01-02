from flask import Flask, jsonify , render_template 

app = Flask(__name__)
l = []

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/')
@app.route('/total_combinations')
def get_total_combinations():
    number_of_dice = 2
    sides = 6
    total_combinations = sides ** number_of_dice
    return jsonify(total_combinations)
    


@app.route('/')
@app.route('/distribution')
def get_distribution_list():
    sides = 6
    distribution_list = []
    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            total = i + j
            combination_map = {
                "Die A": i,
                "Die B": j,
                "Sum": total,
            }
            l.append(total)
            distribution_list.append(combination_map)
    return jsonify(distribution_list)
     
@app.route('/')
@app.route('/probability')
def get_probability():
    sides =6
    for i in range(1, sides + 1):
        for j in range(1, sides + 1):
            total = i + j
            combination_map = {
                "Die A": i,
                "Die B": j,
                "Sum": total,
            }
            l.append(total)

    probability = []
    x = list(set(l))
    for i in range(len(x)):
        probability.append(l.count(x[i]))
        probability[i] = f"'{probability[i]}':'{str(l.count(x[i]))}/{36}'"

    #output1 = {"total_combinations": total_combinations}
    #output2 = {"distribution": distribution_list}
    output3 = {"probability": probability}

    return jsonify(output3)

if __name__ == "__main__":
    app.run(debug=True)