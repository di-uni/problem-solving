import sys
from collections import deque

T = int(sys.stdin.readline().rstrip())
queue = deque()

for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    docs = deque(list(map(int, sys.stdin.readline().rstrip().split())))

    max_doc = max(docs)
    cnt = 0     # 현재까지 뽑은 순서를 저장하는 변수
    while True:
        if docs[0] == max_doc:
            docs.popleft()
            cnt += 1
            if M == 0:          # 인쇄 순서가 궁금한 숫자를 현재 뽑은 상태
                print(cnt)
                break
            max_doc = max(docs)  # max_doc이 한 번 나왔으니 max 값을 다시 구한다.
        else:
            docs.append(docs.popleft())
        M -= 1  # 뽑든 안 뽑든 popleft를 하게 되므로 M 값은 한 칸 땡겨진다.
        if M == -1:
            M = len(docs) - 1
