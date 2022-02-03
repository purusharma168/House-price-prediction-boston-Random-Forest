from flask import Flask, escape, request, render_template
import pickle

model = pickle.load(open("final_model.pkl", 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/prediction', methods=['GET', 'POST'])
def prediction():
    if request.method == "POST":
        try:
            if request.form:
                dict_req = dict(request.form)
                # print(dict_req)
                data = dict_req.values()
                # print(data)
                data = [list(map(float, data))]
                # print(data)
                response = model.predict(data).tolist()[0]
                # print(response)
                return render_template("prediction.html", prediction_text="Price of house - >"+str(response))

        except Exception as e:
            print(e)
            error = {"error": "Something went wrong!! Try again later!"}
            error = {"error": e}
            return render_template("prediction.html", prediction_text=error)

        return render_template("prediction.html")


    else:
        return render_template("prediction.html")


if __name__ == '__main__':
    app.debug = True
    app.run(port=8000)