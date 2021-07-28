import pickle
# load the model
loaded_model=pickle.load(open('dib_79.pkl' , 'rb'))
pred=loaded_model.predict([[10,12,45,32,55,22,45,22]])
if pred[0]==1:
    print("diabetic")
else:
    print("nondiabetic")
