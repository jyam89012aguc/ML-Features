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
def _f092_marketcap_trend(marketcap, w):
    return _mean(marketcap, w) / _mean(marketcap, w * 2).replace(0, np.nan) - 1.0


def _f092_mc_per_share(marketcap, sharesbas):
    return marketcap / sharesbas.replace(0, np.nan)


def _f092_inst_buildup_proxy(marketcap, sharesbas, w):
    mps = marketcap / sharesbas.replace(0, np.nan)
    return mps.pct_change(w)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_5d_base_v001_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_5d_base_v002_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_5d_base_v003_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_10d_base_v004_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_10d_base_v005_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_10d_base_v006_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_21d_base_v007_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_21d_base_v008_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_21d_base_v009_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_42d_base_v010_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_42d_base_v011_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_42d_base_v012_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_63d_base_v013_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_63d_base_v014_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_63d_base_v015_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_126d_base_v016_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_126d_base_v017_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_126d_base_v018_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_189d_base_v019_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_189d_base_v020_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_189d_base_v021_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_252d_base_v022_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_252d_base_v023_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_252d_base_v024_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_378d_base_v025_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_378d_base_v026_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_378d_base_v027_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_504d_base_v028_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_504d_base_v029_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_504d_base_v030_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_5d_base_v031_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_5d_base_v032_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 5)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_5d_base_v033_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 5).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_10d_base_v034_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_10d_base_v035_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 10)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_10d_base_v036_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 10).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_21d_base_v037_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_21d_base_v038_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 21)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_21d_base_v039_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 21).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_42d_base_v040_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_42d_base_v041_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 42)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_42d_base_v042_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 42).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_63d_base_v043_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_63d_base_v044_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_63d_base_v045_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_126d_base_v046_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_126d_base_v047_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_126d_base_v048_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 126).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_189d_base_v049_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_189d_base_v050_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_189d_base_v051_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 189).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_252d_base_v052_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_252d_base_v053_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_252d_base_v054_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_378d_base_v055_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_378d_base_v056_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_378d_base_v057_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 378).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_504d_base_v058_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_504d_base_v059_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 504)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_504d_base_v060_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = _z(base, 504).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_5d_base_v061_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_5d_base_v062_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 5)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_5d_base_v063_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.sign(_z(base, 5)) * _z(base, 5).abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_10d_base_v064_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_10d_base_v065_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 10)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_10d_base_v066_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.sign(_z(base, 10)) * _z(base, 10).abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_21d_base_v067_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_21d_base_v068_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 21)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_21d_base_v069_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.sign(_z(base, 21)) * _z(base, 21).abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_42d_base_v070_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_42d_base_v071_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 42)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_42d_base_v072_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.sign(_z(base, 42)) * _z(base, 42).abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_63d_base_v073_signal(marketcap, sharesbas, closeadj):
    base = _f092_marketcap_trend(marketcap, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_63d_base_v074_signal(marketcap, sharesbas, closeadj):
    base = _f092_inst_buildup_proxy(marketcap, sharesbas, 63)
    result = np.sign(base) * base.abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_63d_base_v075_signal(marketcap, sharesbas, closeadj):
    base = _f092_mc_per_share(marketcap, sharesbas)
    result = np.sign(_z(base, 63)) * _z(base, 63).abs().pow(0.5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_5d_base_v001_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_5d_base_v002_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_5d_base_v003_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_10d_base_v004_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_10d_base_v005_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_10d_base_v006_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_21d_base_v007_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_21d_base_v008_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_21d_base_v009_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_42d_base_v010_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_42d_base_v011_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_42d_base_v012_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_63d_base_v013_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_63d_base_v014_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_63d_base_v015_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_126d_base_v016_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_126d_base_v017_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_126d_base_v018_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_189d_base_v019_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_189d_base_v020_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_189d_base_v021_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_252d_base_v022_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_252d_base_v023_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_252d_base_v024_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_378d_base_v025_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_378d_base_v026_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_378d_base_v027_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_rawz_504d_base_v028_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_rawz_504d_base_v029_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_rawz_504d_base_v030_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_5d_base_v031_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_5d_base_v032_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_5d_base_v033_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_10d_base_v034_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_10d_base_v035_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_10d_base_v036_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_21d_base_v037_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_21d_base_v038_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_21d_base_v039_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_42d_base_v040_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_42d_base_v041_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_42d_base_v042_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_63d_base_v043_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_63d_base_v044_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_63d_base_v045_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_126d_base_v046_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_126d_base_v047_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_126d_base_v048_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_189d_base_v049_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_189d_base_v050_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_189d_base_v051_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_252d_base_v052_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_252d_base_v053_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_252d_base_v054_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_378d_base_v055_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_378d_base_v056_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_378d_base_v057_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_absz_504d_base_v058_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_absz_504d_base_v059_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_absz_504d_base_v060_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_5d_base_v061_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_5d_base_v062_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_5d_base_v063_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_10d_base_v064_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_10d_base_v065_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_10d_base_v066_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_21d_base_v067_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_21d_base_v068_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_21d_base_v069_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_42d_base_v070_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_42d_base_v071_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_42d_base_v072_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mctrend_sqrtz_63d_base_v073_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_instbuild_sqrtz_63d_base_v074_signal,
    f092iob_f092_institutional_ownership_buildup_proxy_mcpershare_sqrtz_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F092_INSTITUTIONAL_OWNERSHIP_BUILDUP_PROXY_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    dps = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    payoutratio = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {
        "closeadj": closeadj, "volume": volume, "sharesbas": sharesbas,
        "marketcap": marketcap, "dps": dps, "payoutratio": payoutratio,
        "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f092_marketcap_trend", "_f092_mc_per_share", "_f092_inst_buildup_proxy")
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
    print(f"OK f092_institutional_ownership_buildup_proxy_base_001_075_claude: {n_features} features pass")
