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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f090_share_change_burst(sharesbas, w):
    chg = -sharesbas.diff(periods=w)
    sd = sharesbas.diff(periods=1).rolling(w, min_periods=max(1, w // 2)).std()
    return chg / (sd.replace(0, np.nan) * np.sqrt(float(w)))


def _f090_burst_pattern(sharesbas, w):
    decl = (-sharesbas.diff(periods=1)).clip(lower=0)
    return decl.rolling(w, min_periods=max(1, w // 2)).sum() / sharesbas.abs().shift(w).replace(0, np.nan)


def _f090_clustering_intensity(sharesbas, w):
    b = -(sharesbas.diff(periods=w) / sharesbas.abs().shift(w).replace(0, np.nan))
    m = b.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = b.rolling(w, min_periods=max(1, w // 2)).std()
    return (b - m) / sd.replace(0, np.nan)

def f090ibc_f090_insider_buy_clustering_proxy_scb_5d_slope_v001_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_5d_slope_v002_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_5d_slope_v003_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_10d_slope_v004_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_10d_slope_v005_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_10d_slope_v006_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_21d_slope_v007_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_21d_slope_v008_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_21d_slope_v009_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_42d_slope_v010_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_42d_slope_v011_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_42d_slope_v012_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_63d_slope_v013_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_63d_slope_v014_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_63d_slope_v015_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_126d_slope_v016_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_126d_slope_v017_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_126d_slope_v018_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 126) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_189d_slope_v019_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_189d_slope_v020_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_189d_slope_v021_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 189) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_252d_slope_v022_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_252d_slope_v023_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_252d_slope_v024_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 252) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_378d_slope_v025_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_378d_slope_v026_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_378d_slope_v027_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 378) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_504d_slope_v028_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_504d_slope_v029_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_504d_slope_v030_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 504) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_5d_slope_v031_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_5d_slope_v032_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_5d_slope_v033_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_10d_slope_v034_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_10d_slope_v035_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_10d_slope_v036_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_21d_slope_v037_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_21d_slope_v038_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_21d_slope_v039_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_42d_slope_v040_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_42d_slope_v041_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_42d_slope_v042_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_63d_slope_v043_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_63d_slope_v044_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_63d_slope_v045_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_126d_slope_v046_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_126d_slope_v047_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_126d_slope_v048_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_189d_slope_v049_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_189d_slope_v050_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_189d_slope_v051_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 189) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_252d_slope_v052_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_252d_slope_v053_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_252d_slope_v054_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_378d_slope_v055_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_378d_slope_v056_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_378d_slope_v057_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 378) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_504d_slope_v058_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_504d_slope_v059_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_504d_slope_v060_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 504) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_5d_slope_v061_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_5d_slope_v062_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_5d_slope_v063_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_10d_slope_v064_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_10d_slope_v065_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_10d_slope_v066_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_21d_slope_v067_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_21d_slope_v068_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_21d_slope_v069_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_42d_slope_v070_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_42d_slope_v071_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_42d_slope_v072_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_63d_slope_v073_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_63d_slope_v074_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_63d_slope_v075_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_126d_slope_v076_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_126d_slope_v077_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_126d_slope_v078_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_189d_slope_v079_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_189d_slope_v080_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_189d_slope_v081_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_252d_slope_v082_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_252d_slope_v083_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_252d_slope_v084_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_378d_slope_v085_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_378d_slope_v086_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_378d_slope_v087_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_504d_slope_v088_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_504d_slope_v089_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_504d_slope_v090_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_5d_slope_v091_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 5)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_5d_slope_v092_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 5)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_5d_slope_v093_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 5)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_10d_slope_v094_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 10)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_10d_slope_v095_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 10)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_10d_slope_v096_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 10)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_21d_slope_v097_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 21)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_21d_slope_v098_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 21)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_21d_slope_v099_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 21)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_42d_slope_v100_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 42)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_42d_slope_v101_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 42)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_42d_slope_v102_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 42)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_63d_slope_v103_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 63)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_63d_slope_v104_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 63)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_63d_slope_v105_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 63)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_126d_slope_v106_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 126)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_126d_slope_v107_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 126)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_126d_slope_v108_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 126)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_189d_slope_v109_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 189)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_189d_slope_v110_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 189)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_189d_slope_v111_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 189)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_252d_slope_v112_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 252)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_252d_slope_v113_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 252)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_252d_slope_v114_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 252)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_378d_slope_v115_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 378)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_378d_slope_v116_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 378)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_378d_slope_v117_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 378)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsq_504d_slope_v118_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 504)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsq_504d_slope_v119_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 504)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisq_504d_slope_v120_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 504)) * closeadj * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_5d_slope_v121_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_5d_slope_v122_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_5d_slope_v123_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 5)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_10d_slope_v124_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 10)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_10d_slope_v125_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 10)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_10d_slope_v126_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 10)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_21d_slope_v127_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 21)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_21d_slope_v128_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 21)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_21d_slope_v129_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 21)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_42d_slope_v130_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 42)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_42d_slope_v131_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 42)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_42d_slope_v132_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 42)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_63d_slope_v133_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 63)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_63d_slope_v134_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 63)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_63d_slope_v135_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 63)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_126d_slope_v136_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 126)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_126d_slope_v137_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 126)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_126d_slope_v138_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 126)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_189d_slope_v139_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 189)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_189d_slope_v140_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 189)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_189d_slope_v141_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 189)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_252d_slope_v142_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 252)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_252d_slope_v143_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 252)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_252d_slope_v144_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 252)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_378d_slope_v145_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 378)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_378d_slope_v146_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 378)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_378d_slope_v147_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 378)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbab_504d_slope_v148_signal(sharesbas, closeadj):
    base = (_f090_share_change_burst(sharesbas, 504)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptab_504d_slope_v149_signal(sharesbas, closeadj):
    base = (_f090_burst_pattern(sharesbas, 504)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliab_504d_slope_v150_signal(sharesbas, closeadj):
    base = (_f090_clustering_intensity(sharesbas, 504)).abs() * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f090ibc_f090_insider_buy_clustering_proxy_scb_5d_slope_v001_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_5d_slope_v002_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_5d_slope_v003_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_10d_slope_v004_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_10d_slope_v005_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_10d_slope_v006_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_21d_slope_v007_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_21d_slope_v008_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_21d_slope_v009_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_42d_slope_v010_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_42d_slope_v011_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_42d_slope_v012_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_63d_slope_v013_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_63d_slope_v014_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_63d_slope_v015_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_126d_slope_v016_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_126d_slope_v017_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_126d_slope_v018_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_189d_slope_v019_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_189d_slope_v020_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_189d_slope_v021_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_252d_slope_v022_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_252d_slope_v023_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_252d_slope_v024_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_378d_slope_v025_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_378d_slope_v026_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_378d_slope_v027_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_504d_slope_v028_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_504d_slope_v029_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_504d_slope_v030_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_5d_slope_v031_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_5d_slope_v032_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_5d_slope_v033_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_10d_slope_v034_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_10d_slope_v035_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_10d_slope_v036_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_21d_slope_v037_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_21d_slope_v038_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_21d_slope_v039_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_42d_slope_v040_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_42d_slope_v041_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_42d_slope_v042_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_63d_slope_v043_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_63d_slope_v044_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_63d_slope_v045_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_126d_slope_v046_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_126d_slope_v047_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_126d_slope_v048_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_189d_slope_v049_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_189d_slope_v050_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_189d_slope_v051_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_252d_slope_v052_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_252d_slope_v053_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_252d_slope_v054_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_378d_slope_v055_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_378d_slope_v056_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_378d_slope_v057_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_504d_slope_v058_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_504d_slope_v059_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_504d_slope_v060_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_5d_slope_v061_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_5d_slope_v062_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_5d_slope_v063_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_10d_slope_v064_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_10d_slope_v065_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_10d_slope_v066_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_21d_slope_v067_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_21d_slope_v068_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_21d_slope_v069_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_42d_slope_v070_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_42d_slope_v071_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_42d_slope_v072_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_63d_slope_v073_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_63d_slope_v074_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_63d_slope_v075_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_126d_slope_v076_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_126d_slope_v077_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_126d_slope_v078_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_189d_slope_v079_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_189d_slope_v080_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_189d_slope_v081_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_252d_slope_v082_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_252d_slope_v083_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_252d_slope_v084_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_378d_slope_v085_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_378d_slope_v086_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_378d_slope_v087_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_504d_slope_v088_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_504d_slope_v089_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_504d_slope_v090_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_5d_slope_v091_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_5d_slope_v092_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_5d_slope_v093_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_10d_slope_v094_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_10d_slope_v095_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_10d_slope_v096_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_21d_slope_v097_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_21d_slope_v098_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_21d_slope_v099_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_42d_slope_v100_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_42d_slope_v101_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_42d_slope_v102_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_63d_slope_v103_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_63d_slope_v104_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_63d_slope_v105_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_126d_slope_v106_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_126d_slope_v107_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_126d_slope_v108_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_189d_slope_v109_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_189d_slope_v110_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_189d_slope_v111_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_252d_slope_v112_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_252d_slope_v113_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_252d_slope_v114_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_378d_slope_v115_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_378d_slope_v116_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_378d_slope_v117_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsq_504d_slope_v118_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsq_504d_slope_v119_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisq_504d_slope_v120_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_5d_slope_v121_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_5d_slope_v122_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_5d_slope_v123_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_10d_slope_v124_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_10d_slope_v125_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_10d_slope_v126_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_21d_slope_v127_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_21d_slope_v128_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_21d_slope_v129_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_42d_slope_v130_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_42d_slope_v131_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_42d_slope_v132_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_63d_slope_v133_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_63d_slope_v134_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_63d_slope_v135_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_126d_slope_v136_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_126d_slope_v137_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_126d_slope_v138_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_189d_slope_v139_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_189d_slope_v140_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_189d_slope_v141_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_252d_slope_v142_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_252d_slope_v143_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_252d_slope_v144_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_378d_slope_v145_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_378d_slope_v146_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_378d_slope_v147_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbab_504d_slope_v148_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptab_504d_slope_v149_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliab_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F090_INSIDER_BUY_CLUSTERING_PROXY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")

    cols = {"sharesbas": sharesbas, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f090_share_change_burst", "_f090_burst_pattern", "_f090_clustering_intensity",)
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
    print(f"OK f090_insider_buy_clustering_proxy_2nd_derivatives_001_150_claude: {n_features} features pass")
