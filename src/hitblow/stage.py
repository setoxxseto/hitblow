"""ステージ管理"""

_stage = 1


def get_stage():
    return _stage


def clear_stage():
    global _stage
    _stage += 1


def reset_stage():
    global _stage
    _stage = 1