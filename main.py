### Integrte html with flask
### http get and post



from flask import Flask, redirect, url_for, render_template, request
## creates a wsgi application to communication between webserver and web app
app = Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res =  "PASS"
    else:
        res =  "FAIL"
    exp = {'score':score, 'res':res}
    return render_template('result.html', result = exp)
    

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks is "+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    results=''
    if(marks<50):
        results = 'fail'
    else:
        results='success'
    return redirect(url_for(results, score=marks))


@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        ds = float(request.form['datascience'])
        total = (science+maths+c+ds)/4

    return redirect(url_for("success", score=total))


if __name__=='__main__':
    app.run(debug=True)