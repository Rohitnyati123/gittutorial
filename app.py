from flask import Flask, render_template,request
import pickle
import project_db
import config

object_model = pickle.load(open("lr_student.pkl", "rb"))

app=Flask(__name__)

@app.route("/")
def index():
    print("hello rohit")
    return render_template("index.html")

@app.route("/prediction", methods=["POST"])
def get_predict():
    print("heloooooooooo")

    cgpa_1 = float(request.form.get('cgpa'))
    iq_1 = int(request.form.get('iq'))
    profile_score_1 = int(request.form.get('profile_score'))

    result=object_model.predict([[cgpa_1,iq_1,profile_score_1]])
    
    if result[0]==0:
        place = "*******************Sorry : Not Placed*******************"
    
    else:
        place = "*******************Congratulations: Placed Sucessfully*******************"
    print(place)
    project_db.collection_user.insert_one({"CGPA":cgpa_1, "IQ":iq_1, "Profile Score":profile_score_1,"Result":place})
    return render_template("index.html",prediction =place)

if __name__ == '__main__':
    app.run(debug=True,port=config.Port_Number,host="0.0.0.0") 