def solution(n, times):
    answer = 0
    # 이진탐색을 위해 최대 시간 right 
    left, right = 1, n * max(times)
    
    while left <= right:
        middle = (left + right) // 2
        # 처리한 사람의 수 count
        count = 0
        for time in times:
            count += middle // time
        # 처리한 사람 수 보다 사람 수가 많은 경우 넉넉한 시간
        if count >= n:
            right = middle - 1
        # 시간이 부족함 
        else:
            left = middle + 1
    
    return left
print(solution(6, [7,10]))