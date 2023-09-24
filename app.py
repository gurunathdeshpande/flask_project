from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return"<h1>gurunath</h1>"

@app.route('/success/<int:score>')
def success(score):
    return "gurunath has passed and the score is "+ str(score)
#variable rule
@app.route('/fail/<int:score>')
def fail(score):
    return "gurunath has failed and the score is "+ str(score)

@app.route('/form' , methods=['GET','POST'])
def form():
    if request.method=='GET':
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3

        #return render_template("form.html" , score=average_marks)
        
        res=""
        if average_marks>=50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res , score=average_marks))

if __name__=="__main__":
    app.run(debug=True)