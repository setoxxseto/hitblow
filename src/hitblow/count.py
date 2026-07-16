def get_max_tries(digits: int) -> int:
    """桁数に応じた最大試行回数を返す"""
    return 10  # 必要なら digits に応じて変えてもOK


def is_over_limit(tries: int, max_tries: int) -> bool:
    """上限に達したかどうかを判定する"""
    return tries >= max_tries