from flask import Flask, jsonify, request
from flask_cors import CORS

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods = ['GET'])
def get_articles():
    #Run h
    return jsonify({"Hello":"World"})

#Set the recommended program here
recommendedProgram = "NA"

@app.route('/get-population', methods = ['GET', 'POST'])
def recommend_program():
    if request.method == 'POST':
        year = request.form.get('year')
        rooms = request.form.get('rooms')
        fulltime = request.form.get('fulltime')
        partime = request.form.get('parttime')
        #Run here recommend program
        #import libraries
        import numpy as np
        import pandas as pd  
        from sklearn.model_selection import train_test_split
        from sklearn.linear_model import LinearRegression
        from sklearn.metrics import mean_squared_error

        DATA_CSV_FILE = pd.read_csv('population.csv')
        DATA_CSV_FILE.isnull().sum()

        print(DATA_CSV_FILE)
        X = pd.DataFrame(np.c_[
            DATA_CSV_FILE['Year'],
            DATA_CSV_FILE['Rooms'],
            DATA_CSV_FILE['FullTime'],
            DATA_CSV_FILE['PartTime']],
            columns = ['Year',
            'Rooms',
            'FullTime',
            'PartTime'])
        Y = DATA_CSV_FILE['Population']


        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state=5)
        print(X_train.shape)
        print(X_test.shape)
        print(Y_train.shape)
        print(Y_test.shape)

        lin_model = LinearRegression()
        lin_model.fit(X_train, Y_train)

        predict_population = lin_model.predict([[2022, 70, 30, 20]])
        predict_population = int(predict_population)

        return jsonify({"population":predict_population})
    else:
        return jsonify({"program: ":'Please submit the fields first.'})


if __name__ == "__main__":
    app.run(debug=True)