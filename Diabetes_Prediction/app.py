from flask import Flask,render_template,url_for,redirect,request
import pickle
import warnings


app=Flask(__name__)
# loadding index page
@app.route("/")
def index():
	return render_template("index.html")

#check_diabetes
@app.route("/check_diabetes",methods=['GET','POST'])
def check_diabetes():
	if request.method=='POST':
		#male,age,BPMeds,sysBP,diaBP,BMI,heartRate,glucose
		name=request.form["name"]
		gender=int(request.form["gender"])
		age=int(request.form["age"])
		BPMeds=float(request.form["BPMeds"])
		sysBP=float(request.form["sysBP"])
		diaBP=float(request.form["diaBP"])
		BMI=float(request.form["BMI"])
		heartRate=float(request.form["heartRate"])
		glucose=float(request.form["glucose"])
		with warnings.catch_warnings():
			warnings.simplefilter("ignore")
			with open('diabetes_model','rb') as file:
				model=pickle.load(file)
			#passes arguments   [[male,age,BPMeds,sysBP,diaBP,BMI,heartRate,glucose]]
			res=model.predict([[gender,age,BPMeds,sysBP,diaBP,BMI,heartRate,glucose]])
		#data={"name":name,"age":age}
		result=[name,res[0]]
#		return redirect(url_for("home"))
		return render_template("index.html",data=result)


	return render_template("check_diabetes.html")

if(__name__=='__main__'):
	app.run(debug=True)