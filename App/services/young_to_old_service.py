import numpy as np
import tensorflow as tf


def normalize_image(img):
    return np.array(img) / 127.5 - 1.


def load_model(to_young: bool):
    if to_young:
        reconstructed_model = tf.keras.models.load_model("./data_models/generator_AB")
    else:
        reconstructed_model = tf.keras.models.load_model("./data_models/generator_BA")

    return reconstructed_model


def translate_image(to_young: bool, image):
    reconstructed_model = load_model(to_young)

    image = image / 127.5 - 1.
    input = np.expand_dims(image, axis=0)

    shape = input.shape
    return reconstructed_model.predict(input)
