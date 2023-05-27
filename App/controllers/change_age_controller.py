import PIL.Image
import numpy as np
from flask import Blueprint, render_template, abort
from flask import send_file
from flask import request
from io import BytesIO
import base64
import re
import os
from skimage import io, transform
import tensorflow as tf
from PIL import Image
from services.young_to_old_service import translate_image


os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
change_age_controller = Blueprint('change_age_controller', __name__)

pattern = '^[a-zA-Z0-9_]+$'
image_size = 128

# install tensorflow
# export model
# implement change


@change_age_controller.route('/api/change-age', methods=['POST'])
def transfer_style_method():

    make_younger: bool = True
    if "make_younger" in request.args and re.match(pattern, request.args["make_younger"]):
        make_younger = request.args["make_younger"]

    content = request.json['content']
    content_img_input = BytesIO(base64.b64decode(content, validate=True))
    content_img = PIL.Image.open(content_img_input, )

    image_array = np.array(content_img)[:, :, 0:3].astype('float32')
    resized_image = transform.resize(image_array, output_shape=(128, 128))

    result = translate_image(to_young=make_younger, image=resized_image)

    result = np.squeeze(result, axis=0)
    result = 0.5 * result + 0.2

    shape = result.shape

    pil_img = tf.keras.utils.array_to_img(result)
    buff = BytesIO()
    pil_img.save(buff, format="JPEG")

    return {
        "image": "data:image/jpeg;base64," + base64.b64encode(buff.getvalue()).decode()
    }
