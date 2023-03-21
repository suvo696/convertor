from flask import Flask, render_template, request
import pickle

app = Flask(__name__,static_folder='public/template', template_folder='public')


@app.route("/")
def index():
	return render_template("index.html")

@app.route("/register")
def register():
	return render_template("register.html")

@app.route("/invoice", methods=['POST'])
def invoice():
	username = request.form['username']
	password = request.form['password']
	if(username == 'sandip' and password == '1234'):
		return render_template("invoice.html")
	else:
		return render_template("register.html")

@app.route("/types")
def types():
	return render_template("types.html")

@app.route("/upload")
def upload():
	return render_template("upload.html")

@app.route("/nav")
def nav():
	return render_template("nav.html")

@app.route("/multipleUpload")
def multipleUpload():
	return render_template("multipleUpload.html")

@app.route("/uploader", methods=['POST'])
def uploader():
	# Get the list of files from webpage
	files = request.files.getlist("file")
	select = request.form.get('select')
	# Iterate for each file in the files List, and Save them
	for file in files:
		file.save('uploaded/'+file.filename)
	return "<h1>Files Uploaded Successfully.!"+select+"</h1>"


# prediction function
def ValuePredictor(to_predict_list):
    loaded_model = pickle.load(open("model.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result[0]


if __name__ == "__main__":
	app.run(debug=True)
