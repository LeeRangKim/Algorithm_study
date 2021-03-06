tests = int(input())

for t in range(1,tests+1):
    n, m = map(int, input().split())
    max_die = 0
    #파리 갯수 2차원 배열로 입력받기
    bugs = [list(map(int, input().split())) for _ in range(n)]
    
    #파리채
    for i in range(n-m+1):
        for j in range(n-m+1):
            #total은 i,j가 바뀔때마다 초기화 해줘야함
            total = 0  
            for k in range(m):
                for l in range(m):
                    total += bugs[i+k][j+l]
            #최댓값 구하기
            if max_die < total:
                max_die = total

    print(f'#{t} {max_die}')        
