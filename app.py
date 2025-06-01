from flask import Flask, render_template, request

app = Flask(__name__)

grade ={
    'A+': 9,
    'A' : 8,
    'B+': 7,
    'B': 6,
    'C+': 5,
    'C': 4,
    'D+':3,
    'D':2,
    'E':1

}

@app.route('/', methods=['GET','POST'])
def home():
    percentage = None
    total = None
    if request.method == 'POST':
        try:
            subjects = [
            request.form['first_language'],
            request.form['second_language'],
            request.form['english'],
            request.form['hindi'],
            request.form['social_science'],
            request.form['physics'],
            request.form['chemistry'],
            request.form['biology'],
            request.form['mathematics'],
            request.form['it']
                        ]
            mark = [grade.get(g.upper(),0) for g in subjects]
            total = sum(mark)
            percentage = round((total/90)*100,2)
        except:
            total="Error"
            percentage="Invalid input"

    return render_template('index.html', total=total, percentage=percentage)



if __name__=="__main__":
    app.run(debug=True)