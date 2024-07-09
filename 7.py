def maxScore(cardPoints, k):
    n = len(cardPoints)
    total_sum = sum(cardPoints)
    
    window_sum = sum(cardPoints[:n-k])
    max_score = total_sum - window_sum
    
    for i in range(1, k + 1):
        window_sum = window_sum -  cardPoints[i - 1] + cardPoints[n - k + i - 1]
        max_score = max(max_score, total_sum - window_sum)
    return max_score
