import sys
import cv2
import random

def cut_image(image_file, m, n, output_filename):
    # 이미지 파일 읽기
    image = cv2.imread(image_file)

    # 오류 검출
    if image is None:
        print("이미지를 불러오는데 실패하였습니다.")
        return
    
    # 이미지 크기 조정
    if image.shape[0] % n != 0: # 나머지가 0이 아닐 경우 높이 - 나머지
        image = image[:-(image.shape[0] % n), :]
    if image.shape[1] % m != 0:
        image = image[:, :-(image.shape[1] % m)]
        
    # 이미지를 m x n 크기로 나누기
    tile_height = image.shape[0] // n
    tile_width = image.shape[1] // m

    # 타일 이미지 저장
    tiles = []

    for i in range(n):
        for j in range(m):
            # 타일의 좌측 위부터 계산
            top = i * tile_height
            left = j * tile_width

            # 타일 이미지 가져오기
            tile = image[top:top+tile_height, left:left+tile_width].copy()

            # 변형 적용
            if random.random() < 0.5:
                tile = cv2.flip(tile, 1)  # mirroring
            if random.random() < 0.5:
                tile = cv2.flip(tile, 0)  # flipping
            if random.random() < 0.5:
                tile = cv2.rotate(tile, cv2.ROTATE_90_CLOCKWISE)  # 90 degree rotation

            tiles.append(tile)

            # 출력 파일명 생성
            output_file_name = f"{output_filename}_{i}_{j}.jpg"

            # 타일 이미지 저장
            cv2.imwrite(output_file_name, tile)

            print(f"타일 ({i}, {j})이 {output_file_name}으로 저장되었습니다.")
            
    return tiles

def main():
    # 명령어 입력 확인
    if len(sys.argv) != 5: # 실행파일, 입력파일이름, 행, 열, 출력파일이름 총 5개 입력이 되지 않을 경우 오류
        print("잘못된 입력입니다. 출력파일이름, 행, 열, 입력파일이름을 이용해 주세요")
        return
    # argv[]로 각 인덱스마다 값을 확인 및 입력
    image_file_name = sys.argv[1]
    m = int(sys.argv[2])
    n = int(sys.argv[3])
    output_filename = sys.argv[4]

    # 이미지 자르기 및 타일 이미지 저장
    cut_image(image_file_name, m, n, output_filename)

if __name__ == "__main__":
    main()