import sys
import cv2

def merge_image(tiles, m, n):
    # 결과 이미지를 저장할 변수 초기화
    result = []

    for i in range(n):
        row_tiles = tiles[i * m:(i + 1) * m]

        # 타일 이미지 가로로 합치기
        row_image = cv2.hconcat(row_tiles)
        result.append(row_image)

    # 결과 이미지 세로로 합치기
    output = cv2.vconcat(result)

    return output

def main():
    # 명령줄 인수 오류확인
    if len(sys.argv) != 5:
        print("잘못된 입력입니다. 입력파일이름, 행, 열, 출력파일이름을 이용해 주세요")
        return

    prefix_input_filename = sys.argv[1]
    m = int(sys.argv[2])
    n = int(sys.argv[3])
    output_filename = sys.argv[4]

    # 타일 이미지 로드
    tiles = []
    for i in range(m * n):
        tile_file_name = f"{prefix_input_filename}_{i}.jpg"
        tile_image = cv2.imread(tile_file_name)

        if tile_image is None:
            print(f"파일을 읽는데 실패했습니다{i}.")
            return

        tiles.append(tile_image)

    # 이미지 합치기
    output = merge_image(tiles, m, n)

    # 출력 파일명 생성
    output_file_name = f"{output_filename}.jpg"

    # 결과 이미지 저장
    cv2.imwrite(output_file_name, output)

    print(f"{output_file_name}로 저장되었습니다.")

if __name__ == "__main__":
    main()
