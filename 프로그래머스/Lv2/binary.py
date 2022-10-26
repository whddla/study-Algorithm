# 이진 변환 반복하기


def solution(s):
    cnt = 0
    zero = 0
    while True:
        # 더이상 제거할 0이 없을때
        if s == '1':
            return [cnt, zero]
        # 실행될 때 마다 횟 수 1증가
        cnt += 1
        # 0이 존재할때 마다 개수를 더해줌
        zero += s.count('0')
        # 1의 개수를 다시 2진수로 바꾼 값을 s에 저장
        # bin 은 ob~~ 이런 형식으로 저장되기 때문에 [2:] 부터 뽑아줌
        s = bin(s.count('1'))[2:]
print(solution('100110'))