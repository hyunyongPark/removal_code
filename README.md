# Background Removal System Code Discription

### Original git
```
해당 코드는 rembg 공식 git으로부터 사용되었습니다.
아래의 version은 python 3.8 이상으로부터 변경되었으며, 본 post에서는 3.6버전에서의 구버전 rembg 코드를 참고하여 작성되었습니다. 
```
- https://github.com/danielgatis/rembg

### Requirements

* python 3.6
* flask>=1.1.2
* numpy>=1.19.5
* pillow>=8.0.1
* scikit-image>=0.17.2
* torch>=1.7.0
* torchvision>=0.8.1
* waitress>=1.4.4
* tqdm>=4.51.0
* requests>=2.24.0
* scipy>=1.5.4
* pymatting>=1.1.1
* filetype>=1.0.7
* hsh>=1.1.0




### 환경 세팅

The install cmd is:
```
conda create -n your_prjname python=3.6
conda activate your_prjname
cd /생성된 가상환경경로
pip install -r rembg/requirements.txt
```

- your_prjname : 생성할 가상환경 이름 (파이썬버전은 3.6 고정)


### 학습 weight file 다운로드 
아래의 링크를 통해 학습 weight 파일을 다운받습니다. 해당 파일은 rembg에서 학습한 pretrained file입니다.
해당 weight 파일은 "가상환경/rembg/src/rembg/cmd/" 에 위치하도록 합니다.  
- https://drive.google.com/drive/folders/1tm6HLIx_r9jNquIUPyGtHk1TQR2XOWIw?usp=sharing
https://github.com/hyunyongPark/removal_code/blob/main/img/img1.PNG


### 사용사항

Remove the background from a remote image
```

python3 rembg/src/rembg/cmd/cli.py --input_path "원본 이미지가 저장된 로컬 경로" --output_path "배경제거 처리 된 이미지가 저장될 경로"

```



### Result
<table>
    <thead>
        <tr>
            <td>Original</td>
            <td>Without background</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td><img src="https://github.com/hyunyongPark/removal_code/blob/master/test1.jpg"/></td>
            <td><img src="https://github.com/hyunyongPark/removal_code/blob/main/output/test1._removed.jpg"/></td>
        </tr>
    </tbody>
</table>




### References

- https://arxiv.org/pdf/2005.09007.pdf
- https://github.com/NathanUA/U-2-Net
- https://github.com/pymatting/pymatting

