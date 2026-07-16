def score(tries):
    """
    スコア計算
    初回1000点、以降100点ずつ減点
    """
    point = 1000 - (tries - 1) * 100
    return max(point, 0)