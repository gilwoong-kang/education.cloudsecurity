from typing import TextIO
from io import StringIO

# 헤더 건너뛰고 첫 데이터 추출
def skip_header(reader: TextIO) -> str:
    '''
        reader 내 헤더를 건너뛰고 첫 번째 데이터를 반환한다.
    '''
    
    line = reader.readline()
    line = reader.readline()
    while line.startswith('#'):
        line = reader.readline()
        
    return line

# 데이터를 읽어들여 출력하는 함수
def process_file(reader: TextIO) -> None:
    print(skip_header(reader).strip())

def find_largest(line:str) -> int:
    largest = -1
    for value in line.split():
        v = int(value[:-1])
        if v > largest:
            largest = v
    return largest