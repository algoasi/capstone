from bottle import route, run, post, request, static_file, redirect
import os
import pickle

model_pkl = open("diabetes_pred_model", "rb")
model = pickle.load(model_pkl)
model_pkl.close()

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public')

@route("/")
def hello():
    redirect("/index.html")

@post("/predict")
def do_predict():
    print(request.json)
    pregnancies = request.json.get("pregnancies")
    glucose = request.json.get("glucose")
    blood_pressure = request.json.get("blood_pressure")
    skin_thickness = request.json.get("skin_thickness")
    insulin = request.json.get("insulin")
    bmi = request.json.get("bmi")
    diabetes_pedigree_function = request.json.get("diabetes_fn")
    age = request.json.get("age")

    data = [[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]]
    prediction = model.predict(data)
    return dict(data=prediction.tolist()[0])

if os.environ.get('APP_LOCATION') == None:
    run(host='localhost', port=8080, debug=True)
else:
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))