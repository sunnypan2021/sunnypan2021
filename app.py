from flask import Flask, render_template, request
import joblib
# instance of an app
app = Flask(__name__)# here we will give this step, to let this step run only for app.py

model=joblib.load('dib_79.pkl')
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')# one function has just one decorator
def home():
    return render_template('home.html')

@app.route('/blog', methods= ['POST'])
def contact():#Exp = request.form.get('exp')email = request.form.get('email')phone = request.form.get('phone')address = request.form.get('address')
    pred = request.form.get('pred')
    plas = request.form.get('plas')
    pres = request.form.get('pres')
    skin = request.form.get('skin')
    test = request.form.get('test')
    mass = request.form.get('mass')
    pedi = request.form.get('pedi')
    age = request.form.get('age')
    output=model.predict([[int(pred),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    #print(Exp,email,phone,address)# this will be printed on the console log not on html page
    print(output)
    if output[0]==1:
        output='diabetic'
    else:
        output='nondiabetic'

    return render_template('contact.html', predictedtext=f'the person is {output}')# predictedtext we have to pass in contact.html form in curly brackets as ginger-template
    #return 'contact page'
# run the app
if __name__=='__main__':
    app.run(debug=True)# this will active the debugger and any changes will be automatically working

