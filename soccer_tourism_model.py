# soccer_tourism_model.py

# --- モデルの係数（これまでの分析結果から設定） ---
# Jリーグ観戦者のうち県外から来る人の割合
OUT_OF_PREFECTURE_RATE = 0.137

# ワールドカップ後のJリーグ観客増加率（2002年の実績に基づくシナリオ）
WORLD_CUP_EFFECT_COEFFICIENTS = {
    "none": 1.0,         # 影響なし
    "modest": 1.10,      # 保守的シナリオ (10%増)
    "optimistic": 1.20   # 楽観的シナリオ (20%増)
}

def simulate_soccer_tourists(
    baseline_annual_attendance: int,
    world_cup_effect_scenario: str = "none"
) -> dict:
    """
    Jリーグの年間来場者数から、県外からの観光客数を試算する特化モデル。

    Args:
        baseline_annual_attendance (int): 年間のJリーグ総来場者数（例: 浦和＋大宮の約82万人）
        world_cup_effect_scenario (str): W杯効果のシナリオ ('none', 'modest', 'optimistic')

    Returns:
        dict: 試算結果。
    """
    if world_cup_effect_scenario not in WORLD_CUP_EFFECT_COEFFICIENTS:
        raise ValueError("シナリオは 'none', 'modest', 'optimistic' のいずれかを選択してください。")

    world_cup_factor = WORLD_CUP_EFFECT_COEFFICIENTS[world_cup_effect_scenario]

    # 1. W杯効果を反映した総来場者数を計算
    projected_attendance = baseline_annual_attendance * world_cup_factor

    # 2. 県外からの観光客数を計算
    estimated_tourists = projected_attendance * OUT_OF_PREFECTURE_RATE

    return {
        "scenario": {
            "baseline_annual_attendance": baseline_annual_attendance,
            "world_cup_effect": world_cup_effect_scenario
        },
        "projected_total_attendance": int(projected_attendance),
        "estimated_out_of_prefecture_tourists": int(estimated_tourists)
    }
