from flask import Flask,render_template,request
app = Flask(__name__)
import def_income

@app.route('/income',methods=['GET','POST'])
def hello_world():
    result = ''
    #[[48 ' Private' ' 11th' ' Machine-op-inspct' ' White' ' Male' 40 ' <=50K']]
    # df = data[['age', 'workclass', 'education', 'occupation', 'race', 'sex', 'hours-per-week', 'income']]
    if request.method == 'POST':
        age = int(request.form['age'])
        workclass = ' '+request.form['workclass']
        education = ' '+request.form['education']
        occupation = ' '+request.form['occupation']
        race = ' '+request.form['race']
        sex = ' '+request.form['sex']
        hours_per_week = int(request.form['hou'])
        print(workclass)
        arr = [[age,workclass,education,occupation,race,sex,hours_per_week,' <=50K']]
        r = def_income.income(arr)
        result = '대출 가능'
        if r == 0:
            result = '대출 불가'
        

    return render_template('income.html',result=result)

if __name__ == '__main__':
    app.run()