# D-Meta
image cut&amp;merge
주니어입니다. 
___
## 과제 내용
1. 2x2, 3x3, 3x4(optional) 파일을 자르고 50 확률로 mirror, flip, rotation 후 저장
2. 크기의 나머지가 생겨 자르기 원할 하지 않을 경우 임의로 사진의 크기 변경
3. 변환된 파일을 다시 하나의 사진으로 변환
* 2x2 ~ 3x4는 m과 n으로 대체하여 풀었습니다.

# Cut_image.py
m과 n을 입력시 파일을 자르고 변환하는 부분을 담당합니다.

# merge_image.py
m과 n으로 잘리고 변환된 파일을 하나로 붙히 부분을 담당합니다.

# c_m_run.sh
shell script로 명령어를 실행하는 것을 도와줍니다.

예시로 bash c_m_run.sh input_image.jpg 3 4 output_image를 동착시키면됩니다.
또한 CUt_image.py merge_image.py를 따로 동작시킬 수 있습니다


## 참고 사이트
https://stackoverflow.com/ (스택오브플로우)

https://opencv.org/ (오픈시브이)

https://www.youtube.com/watch?v=XK3eU9egll8&t=6959s (유튜브)

https://www.youtube.com/watch?v=-1Egx1pv_H0&t=213s (유튜브)

https://wjh2307.tistory.com/7 (개인 사이트)
