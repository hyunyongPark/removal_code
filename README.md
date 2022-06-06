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

- your_prjname : 생성할 가상환경 이름 (파이썬버전은 3.6 고정)

### 사용사항

Remove the background from a remote image
```
python3 rembg/src/rembg/cmd --input_path "원본 이미지가 저장된 로컬 경로" --output_path "배경제거 처리 된 이미지가 저장될 경로"

```




### References

- https://arxiv.org/pdf/2005.09007.pdf
- https://github.com/NathanUA/U-2-Net
- https://github.com/pymatting/pymatting

