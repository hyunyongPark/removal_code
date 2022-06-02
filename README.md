# Background Removal System Code Discription

### Requirements

* python 3.6

#### 환경 세팅

The install cmd is:
```
conda create -n your_prjname python=3.6
conda activate your_prjname
pip install -r requirements.txt
```

- your_prjname : 생성할 가상환경 (파이썬버전은 3.6 고정)


### 

Remove the background from a remote image
```bash
curl -s http://input.png | rembg > output.png
```

Remove the background from a local file
```bash
rembg -o path/to/output.png path/to/input.png
```

Remove the background from all images in a folder
```bash
rembg -p path/to/input path/to/output
```

### Add a custom model

Copy the `custom-model.pth` file to `~/.u2net` and run:

```bash
curl -s http://input.png | rembg -m custom-model > output.png
```

### Usage as a server

Start the server
```bash
rembg-server
```

Open your browser to
```
http://localhost:5000?url=http://image.png
```

Also you can send the file as a FormData (multipart/form-data):
```
<form action="http://localhost:5000" method="post" enctype="multipart/form-data">
   <input type="file" name="file"/>
   <input type="submit" value="upload"/>
</form>
```

### Usage as a library

#### Example 1: Read from stdin and write to stdout

In `app.py`
```python
import sys
from rembg.bg import remove

sys.stdout.buffer.write(remove(sys.stdin.buffer.read()))
```

Then run
```
cat input.png | python app.py > out.png
```

#### Example 2: Using PIL

In `app.py`
```python
from rembg.bg import remove
import numpy as np
import io
from PIL import Image

input_path = 'input.png'
output_path = 'out.png'

f = np.fromfile(input_path)
result = remove(f)
img = Image.open(io.BytesIO(result)).convert("RGBA")
img.save(output_path)
```

Then run
```
python app.py
```

### Usage as a docker

Just run

```
curl -s http://input.png | docker run -i -v ~/.u2net:/root/.u2net danielgatis/rembg:latest > output.png
```

### Advance usage

Sometimes it is possible to achieve better results by turning on alpha matting. Example:
```bash
curl -s http://input.png | rembg -a -ae 15 > output.png
```

<table>
    <thead>
        <tr>
            <td>Original</td>
            <td>Without alpha matting</td>
            <td>With alpha matting (-a -ae 15)</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><img src="https://raw.githubusercontent.com/danielgatis/rembg/master/examples/food-1.jpg"/></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/rembg/master/examples/food-1.out.jpg"/></td>
            <td><img src="https://raw.githubusercontent.com/danielgatis/rembg/master/examples/food-1.out.alpha.jpg"/></td>
        </tr>
    </tbody>
</table>



### References

- https://arxiv.org/pdf/2005.09007.pdf
- https://github.com/NathanUA/U-2-Net
- https://github.com/pymatting/pymatting

