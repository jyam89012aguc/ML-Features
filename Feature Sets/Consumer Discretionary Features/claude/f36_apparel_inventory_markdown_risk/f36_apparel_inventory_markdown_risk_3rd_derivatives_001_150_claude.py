import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f36_inv_days(inventory, cor):
    # Inventory days = inventory / (annualized cogs / 365)
    daily_cor = _mean(cor, 63) / 365.0
    return inventory / daily_cor.replace(0, np.nan)


def _f36_inv_revenue_divergence(inventory, revenue, w):
    # Inventory growth minus revenue growth over window
    inv_g = inventory.pct_change(w)
    rev_g = revenue.pct_change(w)
    return inv_g - rev_g


def _f36_markdown_risk_signal(inventory, revenue, grossmargin, w):
    # High inventory growth + falling margins => markdown risk
    inv_g = inventory.pct_change(w)
    rev_g = revenue.pct_change(w)
    gm_chg = grossmargin.diff(w)
    return (inv_g - rev_g) - gm_chg


def f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v001_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21)
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v002_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21)
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v003_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21)
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v004_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21)
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v005_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21)
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v006_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21)
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v007_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63)
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v008_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63)
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v009_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63)
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v010_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63)
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v011_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63)
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v012_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63)
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v013_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126)
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v014_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126)
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v015_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126)
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v016_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126)
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v017_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126)
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v018_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126)
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v019_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252)
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v020_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252)
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v021_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252)
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v022_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252)
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v023_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252)
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v024_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252)
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v025_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378)
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v026_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378)
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v027_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378)
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v028_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378)
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v029_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378)
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v030_signal(inventory, cor, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378)
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v031_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v032_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v033_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v034_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v035_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v036_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v037_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v038_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v039_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v040_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v041_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v042_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v043_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v044_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v045_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v046_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v047_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v048_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v049_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v050_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v051_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v052_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v053_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v054_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v055_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 378)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v056_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 378)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v057_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 378)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v058_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 378)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v059_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 378)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v060_signal(inventory, revenue, closeadj):
    base = _f36_inv_revenue_divergence(inventory, revenue, 378)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v061_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v062_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v063_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v064_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v065_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v066_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v067_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v068_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v069_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v070_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v071_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v072_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v073_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v074_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v075_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v076_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v077_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v078_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v079_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v080_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v081_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v082_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v083_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v084_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v085_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v086_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v087_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v088_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v089_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v090_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v091_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21) * grossmargin
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v092_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21) * grossmargin
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v093_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21) * grossmargin
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v094_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21) * grossmargin
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v095_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21) * grossmargin
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v096_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 21) * grossmargin
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v097_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63) * grossmargin
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v098_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63) * grossmargin
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v099_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63) * grossmargin
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v100_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63) * grossmargin
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v101_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63) * grossmargin
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v102_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 63) * grossmargin
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v103_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126) * grossmargin
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v104_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126) * grossmargin
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v105_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126) * grossmargin
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v106_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126) * grossmargin
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v107_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126) * grossmargin
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v108_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 126) * grossmargin
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v109_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252) * grossmargin
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v110_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252) * grossmargin
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v111_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252) * grossmargin
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v112_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252) * grossmargin
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v113_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252) * grossmargin
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v114_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 252) * grossmargin
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v115_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378) * grossmargin
    result = _jerk(base, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v116_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378) * grossmargin
    result = _jerk(base, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v117_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378) * grossmargin
    result = _jerk(base, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v118_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378) * grossmargin
    result = _jerk(base, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v119_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378) * grossmargin
    result = _jerk(base, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v120_signal(inventory, cor, grossmargin, closeadj):
    base = _mean(_f36_inv_days(inventory, cor), 378) * grossmargin
    result = _jerk(base, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v121_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21) * grossmargin
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v122_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21) * grossmargin
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v123_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21) * grossmargin
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v124_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21) * grossmargin
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v125_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21) * grossmargin
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v126_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21) * grossmargin
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v127_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63) * grossmargin
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v128_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63) * grossmargin
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v129_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63) * grossmargin
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v130_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63) * grossmargin
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v131_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63) * grossmargin
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v132_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63) * grossmargin
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v133_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126) * grossmargin
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v134_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126) * grossmargin
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v135_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126) * grossmargin
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v136_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126) * grossmargin
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v137_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126) * grossmargin
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v138_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126) * grossmargin
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v139_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252) * grossmargin
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v140_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252) * grossmargin
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v141_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252) * grossmargin
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v142_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252) * grossmargin
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v143_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252) * grossmargin
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v144_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252) * grossmargin
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v145_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378) * grossmargin
    result = _jerk(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v146_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378) * grossmargin
    result = _jerk(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v147_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378) * grossmargin
    result = _jerk(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v148_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378) * grossmargin
    result = _jerk(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v149_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378) * grossmargin
    result = _jerk(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v150_signal(inventory, revenue, grossmargin, closeadj):
    base = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378) * grossmargin
    result = _jerk(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v001_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v002_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v003_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v004_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v005_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_jerk_v006_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v007_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v008_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v009_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v010_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v011_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_jerk_v012_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v013_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v014_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v015_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v016_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v017_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_jerk_v018_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v019_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v020_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v021_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v022_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v023_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_jerk_v024_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v025_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v026_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v027_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v028_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v029_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_jerk_v030_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v031_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v032_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v033_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v034_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v035_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_jerk_v036_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v037_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v038_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v039_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v040_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v041_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_jerk_v042_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v043_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v044_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v045_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v046_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v047_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_jerk_v048_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v049_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v050_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v051_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v052_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v053_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_jerk_v054_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v055_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v056_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v057_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v058_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v059_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_378d_jerk_v060_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v061_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v062_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v063_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v064_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v065_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_jerk_v066_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v067_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v068_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v069_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v070_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v071_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_jerk_v072_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v073_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v074_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v075_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v076_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v077_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_jerk_v078_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v079_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v080_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v081_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v082_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v083_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_jerk_v084_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v085_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v086_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v087_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v088_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v089_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_jerk_v090_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v091_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v092_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v093_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v094_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v095_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_jerk_v096_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v097_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v098_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v099_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v100_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v101_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_jerk_v102_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v103_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v104_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v105_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v106_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v107_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_jerk_v108_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v109_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v110_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v111_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v112_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v113_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_jerk_v114_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v115_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v116_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v117_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v118_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v119_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_jerk_v120_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v121_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v122_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v123_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v124_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v125_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_jerk_v126_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v127_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v128_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v129_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v130_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v131_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_jerk_v132_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v133_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v134_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v135_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v136_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v137_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_jerk_v138_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v139_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v140_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v141_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v142_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v143_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_jerk_v144_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v145_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v146_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v147_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v148_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v149_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_APPAREL_INVENTORY_MARKDOWN_RISK_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")

    cols = {
        "closeadj": closeadj, "volume": volume,
        "revenue": revenue, "cor": cor, "inventory": inventory,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
    }


    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f36_inv_days", "_f36_inv_revenue_divergence", "_f36_markdown_risk_signal",)
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f36_apparel_inventory_markdown_risk_jerk_001_150_claude: {n_features} features pass")
