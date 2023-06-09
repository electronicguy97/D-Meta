#!/bin/bash

# 명령줄 인수 파싱
if [ "$#" -ne 5 ]; then
    echo "오류: bash run_script.sh image_file_name column_num row_num output_file_name를 이용해 주세요"
    exit 1
fi

# 입력 인수 저장
image_file_name=$1
column_num=$2
row_num=$3
output_file_name=$4

# 이미지 자르기
python cut_image.py $image_file_name $column_num $row_num $output_file_name

# 이미지 합치기
python merge_image.py $prefix_input_filename $column_num $row_num $output_file_name