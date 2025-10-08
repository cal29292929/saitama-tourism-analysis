# tourism_model.py

def simulate_saitama_tourists(
    baseline_visitors: int,
    quarter: int,
    has_promotion_campaign: bool = False,
    new_attraction_opens: bool = False
) -> dict:
    """
    埼玉県の四半期別観光客数をシミュレーションするモデル。

    Args:
        baseline_visitors (int): 基準となる観光客数（例: 2025年1-3月期の実績値 2,936,600人）
        quarter (int): シミュレーション対象の四半期 (1, 2, 3, 4)。
        has_promotion_campaign (bool): 大規模な観光プロモーションの有無。
        new_attraction_opens (bool): 新しい大規模観光施設のオープンの有無。

    Returns:
        dict: シミュレーション結果と内訳。
    """
    # 1. 季節係数の設定（2025年のQ1→Q2の実績から算出）
    # Q1を1.0とした場合、Q2は約1.38倍の観光客数だった
    seasonality_coefficients = {
        1: 1.0,   # 1-3月期
        2: 1.38,  # 4-6月期（春の行楽シーズン）
        3: 1.25,  # 7-9月期（夏休みシーズン、仮説値）
        4: 1.15   # 10-12月期（秋の行楽・年末、仮説値）
    }
    seasonal_factor = seasonality_coefficients.get(quarter, 1.0)

    # 2. 施策係数の設定（仮説）
    promotion_factor = 1.15 if has_promotion_campaign else 1.0  # プロモーションで15%増と仮定
    attraction_factor = 1.20 if new_attraction_opens else 1.0    # 新施設オープンで20%増と仮定

    # 3. シミュレーションの実行
    estimated_visitors = baseline_visitors * seasonal_factor * promotion_factor * attraction_factor

    return {
        "scenario": {
            "baseline_visitors": baseline_visitors,
            "quarter": f"{quarter}Q",
            "promotion_campaign": has_promotion_campaign,
            "new_attraction_opens": new_attraction_opens
        },
        "coefficients": {
            "seasonal_factor": seasonal_factor,
            "promotion_factor": promotion_factor,
            "attraction_factor": attraction_factor
        },
        "estimated_total_visitors": int(estimated_visitors)
    }
