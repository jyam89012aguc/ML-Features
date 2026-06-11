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

def f090ibc_f090_insider_buy_clustering_proxy_scb_5d_base_v001_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_5d_base_v002_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_5d_base_v003_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_10d_base_v004_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_10d_base_v005_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_10d_base_v006_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_21d_base_v007_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_21d_base_v008_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_21d_base_v009_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_42d_base_v010_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_42d_base_v011_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_42d_base_v012_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_63d_base_v013_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_63d_base_v014_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_63d_base_v015_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_126d_base_v016_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_126d_base_v017_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_126d_base_v018_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_189d_base_v019_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_189d_base_v020_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_189d_base_v021_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_252d_base_v022_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_252d_base_v023_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_252d_base_v024_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_378d_base_v025_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_378d_base_v026_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_378d_base_v027_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scb_504d_base_v028_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bpt_504d_base_v029_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cli_504d_base_v030_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_5d_base_v031_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_5d_base_v032_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_5d_base_v033_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_10d_base_v034_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_10d_base_v035_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_10d_base_v036_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_21d_base_v037_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_21d_base_v038_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_21d_base_v039_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_42d_base_v040_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_42d_base_v041_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_42d_base_v042_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_63d_base_v043_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_63d_base_v044_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_63d_base_v045_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_126d_base_v046_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_126d_base_v047_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_126d_base_v048_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_189d_base_v049_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_189d_base_v050_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_189d_base_v051_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_252d_base_v052_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_252d_base_v053_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_252d_base_v054_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_378d_base_v055_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_378d_base_v056_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_378d_base_v057_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbabs_504d_base_v058_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptabs_504d_base_v059_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_cliabs_504d_base_v060_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_5d_base_v061_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_5d_base_v062_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisqrt_5d_base_v063_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_10d_base_v064_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_10d_base_v065_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisqrt_10d_base_v066_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_21d_base_v067_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_21d_base_v068_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisqrt_21d_base_v069_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_42d_base_v070_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_42d_base_v071_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisqrt_42d_base_v072_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_63d_base_v073_signal(sharesbas, closeadj):
    base = _f090_share_change_burst(sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_63d_base_v074_signal(sharesbas, closeadj):
    base = _f090_burst_pattern(sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f090ibc_f090_insider_buy_clustering_proxy_clisqrt_63d_base_v075_signal(sharesbas, closeadj):
    base = _f090_clustering_intensity(sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f090ibc_f090_insider_buy_clustering_proxy_scb_5d_base_v001_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_5d_base_v002_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_5d_base_v003_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_10d_base_v004_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_10d_base_v005_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_10d_base_v006_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_21d_base_v007_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_21d_base_v008_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_21d_base_v009_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_42d_base_v010_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_42d_base_v011_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_42d_base_v012_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_63d_base_v013_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_63d_base_v014_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_63d_base_v015_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_126d_base_v016_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_126d_base_v017_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_126d_base_v018_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_189d_base_v019_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_189d_base_v020_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_189d_base_v021_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_252d_base_v022_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_252d_base_v023_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_252d_base_v024_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_378d_base_v025_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_378d_base_v026_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_378d_base_v027_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scb_504d_base_v028_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bpt_504d_base_v029_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cli_504d_base_v030_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_5d_base_v031_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_5d_base_v032_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_5d_base_v033_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_10d_base_v034_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_10d_base_v035_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_10d_base_v036_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_21d_base_v037_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_21d_base_v038_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_21d_base_v039_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_42d_base_v040_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_42d_base_v041_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_42d_base_v042_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_63d_base_v043_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_63d_base_v044_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_63d_base_v045_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_126d_base_v046_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_126d_base_v047_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_126d_base_v048_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_189d_base_v049_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_189d_base_v050_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_189d_base_v051_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_252d_base_v052_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_252d_base_v053_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_252d_base_v054_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_378d_base_v055_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_378d_base_v056_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_378d_base_v057_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbabs_504d_base_v058_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptabs_504d_base_v059_signal,
    f090ibc_f090_insider_buy_clustering_proxy_cliabs_504d_base_v060_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_5d_base_v061_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_5d_base_v062_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisqrt_5d_base_v063_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_10d_base_v064_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_10d_base_v065_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisqrt_10d_base_v066_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_21d_base_v067_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_21d_base_v068_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisqrt_21d_base_v069_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_42d_base_v070_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_42d_base_v071_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisqrt_42d_base_v072_signal,
    f090ibc_f090_insider_buy_clustering_proxy_scbsqrt_63d_base_v073_signal,
    f090ibc_f090_insider_buy_clustering_proxy_bptsqrt_63d_base_v074_signal,
    f090ibc_f090_insider_buy_clustering_proxy_clisqrt_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F090_INSIDER_BUY_CLUSTERING_PROXY_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f090_insider_buy_clustering_proxy_base_001_075_claude: {n_features} features pass")
