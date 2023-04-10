from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "poggers"


@app.route('/')
def form_main():
    return render_template("index.html")




@app.route('/process', methods=["POST"])
def process_form ():
    session['student_name'] = request.form['s_name']
    session['student_location'] = request.form['s_location']
    session['student_favlang'] = request.form['s_favlang']
    session['student_comment'] = request.form['s_comment']
    session['student_check'] = request.form.get('s_check')
    return redirect('/result')



@app.route('/result')
def result_form():
    return render_template("result.html")

@app.route('/reset_session')
def reset():
    session.clear()
    return redirect('/')











































if __name__ == "__main__":
    app.run(debug=True)