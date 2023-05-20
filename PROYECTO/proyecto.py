import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

entrada= np.array([1 , 6 ,30, 7, 70, 43, 503, 201, 1005, 99], dtype=float)
resultados= np.array([0.0254,0.1524, 0.762, 0.1778, 1.0922 , 12.776, 5.1054, 25.527, 2.514 ], dtype=float)

capa1= tf.keras.layers.Dense(units=1, input_shape=[1])
modelo=tf.keras.Sequential([capa1])

modelo.compile(optimizer=tf.keras.optimizers.Adam(0.1), loss= "mean_squared_error")

entramineto= modelo.fit(entrada,resultados, epochs=500, verbose=False)

modelo.save("RedNeuronal.h5")
modelo.save_weights("Pesos.h5")

i= input("pulgadas: ")
i=float(i)

prediccion= modelo.predict([i])
print(prediccion)