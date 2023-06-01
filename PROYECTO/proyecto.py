import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import random_split, TensorDataset
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
import pandas as pd

data=[]
for user in range(0,10):
    user=[]
    age=np.random.randint(1,90)
    gender=["Hombre", "Mujer"]
    sex=np.random.choice(gender)
    blood_pressure=np.random.randint(60,120)
    cholesterol=np.random.randint(120, 300)
    sugar_level=np.random.randint(50,140)
    body_mass_index=np.random.randint(17,35)
    a=["si", "no"]
    inheritance=np.random.choice(a)
    smoker=np.random.choice(a)
    sedentary=np.random.choice(a)
    previous_HD=np.random.choice(a)
    user.append(age)                                #0
    user.append(sex)                                #1
    user.append(blood_pressure)                     #2
    user.append(cholesterol)                        #3
    user.append(sugar_level)                        #4
    user.append(body_mass_index)                    #5
    user.append(inheritance)                        #6
    user.append(smoker)                             #7
    user.append(sedentary)                          #8
    user.append(previous_HD)                        #9
    data.append(user)                               

### probabilidades
def tabl_1(i,points):
    if i[1]== "Hombre":
        if i[0]<=39:
            points+=-1
        elif 40<=i[0]<=59:
            points+=+4
        elif 60<=i[0]:        #edades
            points+=+7
    if i[1]== "Mujer":
        if i[0]<=39:
            points+=-6
        elif 40<=i[0]<=59:
            points+=+6
        elif 60<=i[0]:        #edades
            points+=+8
    return points

def tabl_2(i,points):
    if i[1]== "Hombre":
        if i[2]<=90:
            points+=1               #precion sanguinea
        elif 90<=i[2]:
            points+=3
    if i[1]== "Mujer":
        if i[2]<=90:
            points+=-2               #precion sanguinea
        elif 90<=i[2]:
            points+=3
    return points

def risk_quantifier(i,points):
    risk=0
    if i[1]== "Hombre":
        if points<=5:
           risk=0.08
        elif 6<=points<=9:
            risk=0.2
        elif 10<=points>=12:
            risk=0.37
        elif 13<=points:
            risk=0.53
    if i[1]== "Mujer":
        if points<=5:
           risk=0.08
        elif 6<=points<=9:
            risk=0.2
        elif 10<=points>=12:
            risk=0.37
        elif 13<=points:
            risk=0.53
    return risk

def tabl_FRAMINGHAM():          #CHD
    CHD_probanility=[]
    for i in data:
        points=0
        if i[1] == "Hombre":
            points=tabl_1(i,points)+tabl_2(i,points)
            if i[4]>=125:         #nivel de azucar para diabetes
                points+=2
            if i[7]>="si":        #fumador
                points+=2
            if i[3]>=240:         #colesterol
                points+=3
            if i[6]>="si":        #hereditario
                points+=5
        if i[1]== "Mujer":
            points=tabl_1(i,points)+tabl_2(i,points)
            if i[4]>=125:         #nivel de azucar para diabetes
                points+=2
            if i[7]>="si":        #fumador
                points+=2
            if i[6]>="si":        #hereditario
                points+=5
            if i[3]>=240:         #colesterol
                points+=2
        CHD_probanility.append(risk_quantifier(i,points))
    return CHD_probanility

def Herat_Failure():
    List_Prob_Heart_Failure=[]
    for i in data:
        points=0
        if 65<i[0]:         #edad
            points+=1
        if i[6]=="si":      #hereditario
            points+=1
        if i[7]=="si":    #fuma
            points+=1
        if i[8]=="si":    #vida sedentaria
            points+=1
        if i[5]>=30:        #indice de masa corporal
            points+=1
        if i[4]>=125:         #nivel de azucar para diabetes
            points+=1
        Prob_Heart_Failure = round(points/6,2)
        List_Prob_Heart_Failure.append(Prob_Heart_Failure)
    return List_Prob_Heart_Failure
        
def Arrhytmias():
    List_Prob_Arrhytmias=[]
    for i in data:
        points=0
        if i[9]=="si":
            points+=2
        if 65<i[0]:         #edad
            points+=1
        if i[7]=="si":    #fuma
            points+=1
        if i[6]=="si":      #hereditario
            points+=1
        prob_Arrhytmias=round(points/4,2)
        List_Prob_Arrhytmias.append(prob_Arrhytmias)
    return List_Prob_Arrhytmias
        
def Arterial_Hypertension():
    List_Prob_Hypertension=[]
    for i in data:
        prob=0
        if i[2]>=90:
            prob+=0.3
        if i[6]=="si":
            prob+=0.43
        List_Prob_Hypertension.append(prob)
    return List_Prob_Hypertension

### organizandolas por paciente

Probs_Patient=[]
list_CHD=tabl_FRAMINGHAM()
list_HF=Herat_Failure()
list_A=Arrhytmias()
list_AH=Arterial_Hypertension()


for i in range(0,10):
    Probs=[]
    Probs.append(float(list_CHD[i]))
    Probs.append(float(list_HF[i]))
    Probs.append(float(list_A[i]))
    Probs.append(float(list_AH[i]))
    Probs_Patient.append(Probs)

datos_y=pd.DataFrame(data= Probs_Patient)
datos_y.head()
indices=[]
for i in range(0,10):
    indices.append(i)
columnas=["edad","género","presión sanguinea","colesterol","nivel de azucar","indice de masa corporal","enfermedad hereditaria", "fuma","vida sedentaria", "enfermedad cardiaca previa"]
datos=pd.DataFrame(index=indices,columns=columnas,data=data)

datos_x=pd.get_dummies(datos)
datos_x.head()

###convertiendo a numpy

escalador=StandardScaler()
datos_x=escalador.fit_transform(datos_x)

datos_x.shape[0]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test= train_test_split(datos_x,datos_y, test_size=0.2, random_state=2)


n_entradas=x_train.shape[1]

### tensores

t_x_train= torch.from_numpy(x_train).float().to("cpu")
t_x_test= torch.from_numpy(x_test).float().to("cpu")
t_y_train= torch.from_numpy(y_train.values).float().to("cpu")
t_y_test= torch.from_numpy(y_test.values).float().to("cpu")
t_y_train=t_y_train[:,None]
t_y_test=t_y_test[:,None]

print(t_y_train.shape)
print(t_x_train.shape)

### estructura de red neuronal

class Red(nn.Module):
    def __init__(self, n_entradas):
        super(Red, self).__init__()
        self.linear1=nn.Linear(n_entradas,15)
        self.linear2=nn.Linear(15,10)
        self.linear3=nn.Linear(10,5)
        self.linear4=nn.Linear(5,4)


    def forward(self, inputs):
        pred_1=torch.sigmoid(input=self.linear1(inputs))
        pred_2=torch.sigmoid(input=self.linear2(pred_1))
        pred_3=torch.sigmoid(input=self.linear3(pred_2))
        pred_f=torch.sigmoid(input=self.linear4(pred_3))
        return pred_f

#### entrenamiento
lr=0.001
epochs=1000
estatus_print=100

model=Red(n_entradas=n_entradas)
loss_fn=nn.BCELoss()
optimizer=torch.optim.Adam(params=model.parameters(),lr=lr)
print("arquitectura del modelo: {}".format(model))
historico=pd.DataFrame()

print("entrenando modelo")

for epoch in range(1, epochs+1):
    y_pred=model(t_x_train)
    y_pred= y_pred.unsqueeze(1)
    loss= loss_fn(input=y_pred, target=t_y_train)           #Error con lad dimensiones de los tensores
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

    if epoch % estatus_print==0:
        print(f"\nEpoch {epoch} \t Loss: {round(loss.item(),4)}")

    with torch.no_grad():
        y_pred=model(t_x_test)
        y_pred_class=y_pred.round()     #posible quitar
        correct=(y_pred_class==t_y_test).sum()
        accuracy=100*correct/float(len(t_y_test))
        if epoch % estatus_print ==0:
            print("Accuracy: {}".format(accuracy.item()))

    df_tmp=pd.DataFrame(data={
        "epoch": epoch,
        "loss": round(loss.item(),4),
        "Accuracy":round(accuracy.item(), 4)
    },index=[0])
    historico=pd.concat(objs=[historico,df_tmp],ignore_index=True,sort=False)


print("accuracy final: {}".format(round(accuracy.item(),4)))