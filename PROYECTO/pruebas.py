import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import matplotlib.pyplot as plt

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


#print(Probs_Patient)
#print(data)




heart_disease=["CHD","heart failure","arrhythmias","arterial hypertension"]                             #variable independiente x
                                                                                                        #colesterol, puede surgir de CHD, 
                                                                                                        #por CHD, 
                                                                                                        #presion sanguinia, hereditario

#print(tabl_FRAMINGHAM())
#print(Herat_Failure())

user_array=np.array(data)
print(user_array)
probs_Array=np.array(Probs_Patient)
print(probs_Array)


x_train=user_array[:7].reshape(70,-1)
y_train=probs_Array[:7].reshape(28,1).astype(np.float32)

x_val=user_array[7:].reshape(30,-1)
y_val=probs_Array[7:].reshape(12,1).astype(np.float32)

x_test=x_val.copy().reshape(30,-1)
y_test=y_val.copy().reshape(12,1).astype(np.float32)
