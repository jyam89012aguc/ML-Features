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

def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_5d_base_v001_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_5d_base_v002_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_5d_base_v003_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_10d_base_v004_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_10d_base_v005_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_10d_base_v006_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_21d_base_v007_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_21d_base_v008_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_21d_base_v009_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_42d_base_v010_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_42d_base_v011_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_42d_base_v012_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_63d_base_v013_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_63d_base_v014_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_63d_base_v015_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_126d_base_v016_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_126d_base_v017_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_126d_base_v018_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 126)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_189d_base_v019_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_189d_base_v020_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_189d_base_v021_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 189)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_252d_base_v022_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_252d_base_v023_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_252d_base_v024_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 252)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_378d_base_v025_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_378d_base_v026_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_378d_base_v027_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 378)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbtanh_504d_base_v028_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpttanh_504d_base_v029_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clitanh_504d_base_v030_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 504)
    result = np.tanh(_z(base, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_5d_base_v031_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_5d_base_v032_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_5d_base_v033_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_10d_base_v034_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_10d_base_v035_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_10d_base_v036_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_21d_base_v037_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_21d_base_v038_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_21d_base_v039_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_42d_base_v040_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_42d_base_v041_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_42d_base_v042_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_63d_base_v043_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_63d_base_v044_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_63d_base_v045_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_126d_base_v046_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_126d_base_v047_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_126d_base_v048_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 126)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_189d_base_v049_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_189d_base_v050_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_189d_base_v051_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 189)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_252d_base_v052_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_252d_base_v053_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_252d_base_v054_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 252)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_378d_base_v055_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_378d_base_v056_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_378d_base_v057_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 378)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbclip_504d_base_v058_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptclip_504d_base_v059_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliclip_504d_base_v060_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 504)
    result = _z(base, 252).clip(-3.0, 3.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbvar_5d_base_v061_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptvar_5d_base_v062_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clivar_5d_base_v063_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5)
    result = base.rolling(5, min_periods=max(2, 5 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbvar_10d_base_v064_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptvar_10d_base_v065_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clivar_10d_base_v066_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10)
    result = base.rolling(10, min_periods=max(2, 10 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbvar_21d_base_v067_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptvar_21d_base_v068_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clivar_21d_base_v069_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21)
    result = base.rolling(21, min_periods=max(2, 21 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbvar_42d_base_v070_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptvar_42d_base_v071_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clivar_42d_base_v072_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42)
    result = base.rolling(42, min_periods=max(2, 42 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbvar_63d_base_v073_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptvar_63d_base_v074_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clivar_63d_base_v075_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63)
    result = base.rolling(63, min_periods=max(2, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_5d_base_v001_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_5d_base_v002_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_5d_base_v003_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_10d_base_v004_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_10d_base_v005_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_10d_base_v006_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_21d_base_v007_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_21d_base_v008_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_21d_base_v009_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_42d_base_v010_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_42d_base_v011_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_42d_base_v012_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_63d_base_v013_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_63d_base_v014_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_63d_base_v015_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_126d_base_v016_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_126d_base_v017_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_126d_base_v018_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_189d_base_v019_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_189d_base_v020_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_189d_base_v021_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_252d_base_v022_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_252d_base_v023_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_252d_base_v024_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_378d_base_v025_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_378d_base_v026_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_378d_base_v027_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbtanh_504d_base_v028_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpttanh_504d_base_v029_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clitanh_504d_base_v030_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_5d_base_v031_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_5d_base_v032_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_5d_base_v033_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_10d_base_v034_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_10d_base_v035_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_10d_base_v036_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_21d_base_v037_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_21d_base_v038_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_21d_base_v039_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_42d_base_v040_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_42d_base_v041_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_42d_base_v042_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_63d_base_v043_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_63d_base_v044_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_63d_base_v045_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_126d_base_v046_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_126d_base_v047_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_126d_base_v048_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_189d_base_v049_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_189d_base_v050_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_189d_base_v051_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_252d_base_v052_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_252d_base_v053_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_252d_base_v054_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_378d_base_v055_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_378d_base_v056_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_378d_base_v057_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbclip_504d_base_v058_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptclip_504d_base_v059_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliclip_504d_base_v060_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbvar_5d_base_v061_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptvar_5d_base_v062_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clivar_5d_base_v063_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbvar_10d_base_v064_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptvar_10d_base_v065_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clivar_10d_base_v066_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbvar_21d_base_v067_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptvar_21d_base_v068_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clivar_21d_base_v069_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbvar_42d_base_v070_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptvar_42d_base_v071_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clivar_42d_base_v072_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbvar_63d_base_v073_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptvar_63d_base_v074_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clivar_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F090_INSIDER_BUY_CLUSTERING_PROXY_REGISTRY_076_150 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f090_insider_buy_clustering_proxy_base_076_150_claude: {n_features} features pass")
