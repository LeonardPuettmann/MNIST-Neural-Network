# -*- coding: utf-8 -*-
import tensorflow as tf
from tensorflow import keras
import numpy as np
from keras.models import Sequential
from keras.layers import Input, Dense  # Import aller wichtigen Packages und Libraries

data = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = data.load_data() # Laden des Datensets

print(train_images.shape)
print(test_images.shape)

plt.imshow(train_images[10453], cmap=plt.cm.binary)
print(train_labels[10453])

plt.colorbar() 

np.set_printoptions(edgeitems=28, linewidth=1000,
    formatter= dict(float=lambda x: "%.3g" % x))
print(train_images[10453])

total_classes = 10
train_labels_vectorized = keras.utils.to_categorical(train_labels, total_classes)
test_labels_vectorized = keras.utils.to_categorical(test_labels, total_classes) # Vektorisierung der Labels in 10 Klassen. Das neuronale Netz soll später eine Zahl in eine der 10 Klassen einordnen. 
                                                                                # Die gewollte Klasse, die das Netz vorhersagen soll, erhält den Wert 1, alle anderen den Wert 0. Die Vektorisierung der Labels in einen Array 
                                                                                # ist auch für den Lernprozess wichtig, damit das Neuronale Netz mithilfe der Abweichung zwischen der Ausgabe des Netzes und
                                                                                # dem Wert des Labels einen Fehlerwert ermitteln kann. 

print(f"bisher: {train_labels [0]}")
print(f"neue Annotation: {train_labels_vectorized[0]}")
print(f"bisher_Test: {test_labels [7]}")
print(f"neue Annotation_Test: {test_labels_vectorized[7]}")

model = keras.Sequential([
   keras.layers.Flatten(input_shape=(28, 28)),               # Eingabeschicht
   keras.layers.Dense(128, activation ='sigmoid'),          # Verborgene Schicht
   keras.layers.Dense(total_classes, activation='sigmoid')   # Ausgabeschicht
])

model.compile(
    optimizer='sgd',              # Stochastic Gradient Descent
    loss='mean_squared_error',    # Quadratische Fehlerfunktion. Loss = Die Summe aller quadrierter Differenzen zwischen Output und dem tatsächlichen Wert. Wir quadriert, damit alle Fehlerwerte positiv sind. Ziel ist es, die Summe aler positiven Fehler auf 0 zu bringen, daher würden negative Fehlerwerte keinen Sinn machen
    metrics=['accuracy'])         # Anzahl der korrekt klassifizierten Bilder am Ende der Epoche

model.fit(train_images, train_labels_vectorized, epochs=10, verbose=True)

eval_loss, eval_accuracy = model.evaluate(test_images, test_labels_vectorized, verbose=False)
print("Model accuracy: %.2f" % eval_accuracy)
