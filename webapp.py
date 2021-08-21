from flask Import flask
import urllib.request
import numpy as np

app = Flask(__name__)

@app.route('/')
def display_image():
    url = input (' Please Enter Image URL: ')
    url_response = urllib.request.urlopen(url)
    img = np.array(bytearray(url_response.read()), dtype=np.uint8)
    return img

if __name__ == '__main__':
     app.run(host="0.0.0.0", debug=True)
