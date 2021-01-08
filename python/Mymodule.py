import urllib.request

# url = 'https://robjhyndman.com/tsdldata/ecology1/hopedale.dat'
# with urllib.request.urlopen(url) as webpage:
#         for line in webpage:
#             line = line.strip()
#             line = line.decode('utf-8')
#             print(line)
#

with open('./hopedale.txt', 'r') as file:
    # 첫번째 줄은 설명문이므로 건너뛴다.
    file.readline()

    # 줄 단위로 읽은 내용이 "#"으로 시작하는 경우
    # 아무런 처리를 하지 않는다.
    data = file.readline()
    while data.startswith('#'):
        data = file.readline()

    # 처음으로 "#"으로 시작하지 않는 경우
    # 처음으로 나온 숫자를 합계로 설정
    total_pelts = int(data.strip())

    # 나머지 숫자 데이터를 읽어서 합계에 추가
    for data in file:
        total_pelts = total_pelts + int(data.strip())

print("전체 모피의 수는 " + str(total_pelts) + "개입니다.")
