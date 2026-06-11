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


def f36aim_f36_apparel_inventory_markdown_risk_invdays_5d_base_v001_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 5) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_10d_base_v002_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 10) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_base_v003_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 21) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_42d_base_v004_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 42) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_base_v005_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 63) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_base_v006_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 126) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_189d_base_v007_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 189) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_base_v008_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 252) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_base_v009_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 378) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdays_504d_base_v010_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 504) * closeadj / 1000.0
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysz_21d_base_v011_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _z(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysz_63d_base_v012_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysz_126d_base_v013_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysz_252d_base_v014_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysz_504d_base_v015_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_5d_base_v016_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 5)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_10d_base_v017_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 10)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_base_v018_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_42d_base_v019_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_base_v020_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_base_v021_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_base_v022_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_base_v023_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_42d_base_v024_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 42)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_base_v025_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_base_v026_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_189d_base_v027_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 189)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_base_v028_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_base_v029_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdrisk_504d_base_v030_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 504)
    result = d * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_base_v031_signal(inventory, cor, grossmargin, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 21) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_base_v032_signal(inventory, cor, grossmargin, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 63) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_base_v033_signal(inventory, cor, grossmargin, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 126) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_base_v034_signal(inventory, cor, grossmargin, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 252) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_base_v035_signal(inventory, cor, grossmargin, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 378) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_504d_base_v036_signal(inventory, cor, grossmargin, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 504) * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_10d_base_v037_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _ema(d, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_21d_base_v038_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _ema(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_63d_base_v039_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _ema(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_126d_base_v040_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _ema(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_252d_base_v041_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _ema(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_378d_base_v042_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 21)
    result = _ema(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskz_63d_base_v043_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskz_126d_base_v044_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskz_189d_base_v045_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskz_252d_base_v046_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskz_378d_base_v047_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskz_504d_base_v048_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_21d_base_v049_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 21) * closeadj * closeadj / 1e4
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_63d_base_v050_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 63) * closeadj * closeadj / 1e4
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_126d_base_v051_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 126) * closeadj * closeadj / 1e4
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_252d_base_v052_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 252) * closeadj * closeadj / 1e4
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_378d_base_v053_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 378) * closeadj * closeadj / 1e4
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_504d_base_v054_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = _mean(d, 504) * closeadj * closeadj / 1e4
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_21d_base_v055_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 5)
    result = _std(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_63d_base_v056_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 15)
    result = _std(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_126d_base_v057_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 31)
    result = _std(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_252d_base_v058_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = _std(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_378d_base_v059_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 94)
    result = _std(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_504d_base_v060_signal(inventory, revenue, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 126)
    result = _std(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_base_v061_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_base_v062_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 63)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_base_v063_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 126)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_189d_base_v064_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 189)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_base_v065_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_base_v066_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 378)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_504d_base_v067_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 504)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdayschg_21d_base_v068_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdayschg_63d_base_v069_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdayschg_252d_base_v070_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = d.diff(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgm_63d_base_v071_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 63)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgm_252d_base_v072_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_inv_revenue_divergence(inventory, revenue, 252)
    result = d * grossmargin * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskmean_126d_base_v073_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _mean(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_mdriskmean_252d_base_v074_signal(inventory, revenue, grossmargin, closeadj):
    d = _f36_markdown_risk_signal(inventory, revenue, grossmargin, 21)
    result = _mean(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f36aim_f36_apparel_inventory_markdown_risk_invdaysratio_252d_base_v075_signal(inventory, cor, closeadj):
    d = _f36_inv_days(inventory, cor)
    result = (d / _mean(d, 252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36aim_f36_apparel_inventory_markdown_risk_invdays_5d_base_v001_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_10d_base_v002_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_21d_base_v003_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_42d_base_v004_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_63d_base_v005_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_126d_base_v006_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_189d_base_v007_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_252d_base_v008_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_378d_base_v009_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdays_504d_base_v010_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysz_21d_base_v011_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysz_63d_base_v012_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysz_126d_base_v013_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysz_252d_base_v014_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysz_504d_base_v015_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_5d_base_v016_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_10d_base_v017_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_21d_base_v018_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_42d_base_v019_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_63d_base_v020_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_126d_base_v021_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdiv_252d_base_v022_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_21d_base_v023_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_42d_base_v024_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_63d_base_v025_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_126d_base_v026_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_189d_base_v027_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_252d_base_v028_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_378d_base_v029_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdrisk_504d_base_v030_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_21d_base_v031_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_63d_base_v032_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_126d_base_v033_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_252d_base_v034_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_378d_base_v035_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxgm_504d_base_v036_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_10d_base_v037_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_21d_base_v038_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_63d_base_v039_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_126d_base_v040_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_252d_base_v041_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivema_378d_base_v042_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskz_63d_base_v043_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskz_126d_base_v044_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskz_189d_base_v045_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskz_252d_base_v046_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskz_378d_base_v047_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskz_504d_base_v048_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_21d_base_v049_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_63d_base_v050_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_126d_base_v051_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_252d_base_v052_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_378d_base_v053_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysxpx_504d_base_v054_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_21d_base_v055_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_63d_base_v056_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_126d_base_v057_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_252d_base_v058_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_378d_base_v059_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivstd_504d_base_v060_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_21d_base_v061_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_63d_base_v062_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_126d_base_v063_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_189d_base_v064_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_252d_base_v065_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_378d_base_v066_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskxgm_504d_base_v067_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdayschg_21d_base_v068_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdayschg_63d_base_v069_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdayschg_252d_base_v070_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgm_63d_base_v071_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invrevdivxgm_252d_base_v072_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskmean_126d_base_v073_signal,
    f36aim_f36_apparel_inventory_markdown_risk_mdriskmean_252d_base_v074_signal,
    f36aim_f36_apparel_inventory_markdown_risk_invdaysratio_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_APPAREL_INVENTORY_MARKDOWN_RISK_REGISTRY_001_075 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f36_apparel_inventory_markdown_risk_001_075_claude: {n_features} features pass")
