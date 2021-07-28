import joblib
# load the model
loaded_model=joblib.load('dib_79.pkl')
pred=loaded_model.predict([[10,12,45,32,55,22,45,22]])
if pred[0]==1:
    print("diabetic")
else:
    print("nondiabetic")
