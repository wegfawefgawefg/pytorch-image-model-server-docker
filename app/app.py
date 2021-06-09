import socket
import numpy as np
import json
import requests
import json
import base64
import io

from PIL import Image, ImageOps
import numpy as np
import torch
from flask import Flask
from flask import render_template

from model import ConvNet, MODEL, IM_SCALE

'''
TODO:
before compiling this for arm
1. fix the endpoints to be all targets instead of the fake one
2. fix the port to 8080 again
'''

app = Flask(__name__)

# NET = ConvNet().float().cuda()
NET = ConvNet().half().cuda()
NET.load_state_dict(torch.load(MODEL))
NET.eval()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get():
    # local_docker_network_ip = socket.gethostbyname(socket.gethostname())
    # subnet_mask = local_docker_network_ip[:-2]
    # all_targets = [3, 4, 5, 6]
    # targets = [subnet_mask + ".0" + str(num) for num in all_targets]
    targets = ["0.0.0.0"]
    print(targets)
    data = []
    for target in targets:
        try:
            endpoint = f"http://{target}:8080/get"
            print(endpoint)
            response = requests.get(endpoint)
            if response.status_code == 200:
                j = response.json()
                # j = request.json
                im_64 = j["val"]
                im_raw = base64.b64decode(im_64)
                im = Image.open(io.BytesIO(im_raw))
                im = im.resize(IM_SCALE)
                im = ImageOps.grayscale(im)
                im = np.array(im) / 255.0
                im = torch.tensor(im, dtype=torch.float32).unsqueeze(0).unsqueeze(0).cuda().half()
               
                with torch.no_grad():
                    inf = NET(im)
                data = {"val": inf.item()}
                response = app.response_class(
                    response=json.dumps(data),
                    status=200,
                    mimetype='application/json'
                )
                return response

            #     svs_response = json.loads(response.text)
            #     num = svs_response["val"]
            #     print(num)
            # data.append(num)
        except Exception as e:
            print(e)
    return str(data)

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=8081)