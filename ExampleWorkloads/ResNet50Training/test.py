from DNNHelper import DNNHelper
import tensorflow as tf


dnnhelper = DNNHelper(signIn = True, credsFile="TAPISCreds.json")

# Traning Data
fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
train_images = train_images / 255.0
test_images = test_images / 255.0

# Traning Data
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10)
])
print("============================\n", model.summary(),"\n============================\n" )

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

# model_JSON = dnnhelper.getModelSummaryJSON(model)

# path_to_image = "PATH TO THE CREATED CONTAMNIER IMAGE"
# dnnhelper.createAppDefinition(path_to_image, model_JSON)


dnnhelper.getResouceEstimation(model)





