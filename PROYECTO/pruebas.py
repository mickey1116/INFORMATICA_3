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
    user.append(age)
    user.append(sex)
    user.append(blood_pressure)
    user.append(cholesterol)
    user.append(sugar_level)
    user.append(body_mass_index)
    user.append(inheritance)
    user.append(smoker)
    data.append(user)


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
        


def tabl_FRAMINGHAM():    
    CHD_probanility=[]
    for i in data:
        points=0
        print(i[1])
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

heart_disease=["CHD","heart failure","arrhythmias","arterial hypertension", "congenital heart disease"] #variable independiente x
                                                                                                        #colesterol, puede surgir de CHD, 
                                                                                                        #por CHD, 
                                                                                                        #presion sanguinia, hereditario



print(tabl_FRAMINGHAM())
#user_array=np.array(data)
#print(user_array)
print(data)