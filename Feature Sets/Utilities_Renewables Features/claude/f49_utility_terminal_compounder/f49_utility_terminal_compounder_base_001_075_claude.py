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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


# ===== folder domain primitives =====
def _f49_quality_composite(roic, fcf, revenue, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    fy = fcf / revenue.replace(0, np.nan)
    fy_m = fy.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq * fy_m


def _f49_compounder_score(roic, ebitdamargin, w):
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    eq = ebitdamargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return rq + eq


def _f49_terminal_quality(fcf, revenue, dps, w):
    fg = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    rg = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    dg = dps.rolling(w, min_periods=max(1, w // 2)).mean()
    return (fg / rg.replace(0, np.nan)) * dg


# ===== features =====
def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s00_base_v001_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s00_base_v002_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_5d_s00_base_v003_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 5)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_10d_s00_base_v004_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_10d_s00_base_v005_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_10d_s00_base_v006_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 10)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_21d_s00_base_v007_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_21d_s00_base_v008_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_21d_s00_base_v009_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 21)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_42d_s00_base_v010_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_42d_s00_base_v011_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_42d_s00_base_v012_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 42)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_63d_s00_base_v013_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_63d_s00_base_v014_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_63d_s00_base_v015_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 63)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_84d_s00_base_v016_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_84d_s00_base_v017_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_84d_s00_base_v018_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 84)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s00_base_v019_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_105d_s00_base_v020_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_105d_s00_base_v021_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 105)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s00_base_v022_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_126d_s00_base_v023_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_126d_s00_base_v024_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 126)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s00_base_v025_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_147d_s00_base_v026_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_147d_s00_base_v027_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 147)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_168d_s00_base_v028_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_168d_s00_base_v029_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_168d_s00_base_v030_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 168)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_189d_s00_base_v031_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_189d_s00_base_v032_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_189d_s00_base_v033_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 189)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_210d_s00_base_v034_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_210d_s00_base_v035_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_210d_s00_base_v036_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 210)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_231d_s00_base_v037_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_231d_s00_base_v038_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_231d_s00_base_v039_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 231)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_252d_s00_base_v040_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_252d_s00_base_v041_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_252d_s00_base_v042_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_294d_s00_base_v043_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_294d_s00_base_v044_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_294d_s00_base_v045_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 294)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_336d_s00_base_v046_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_336d_s00_base_v047_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_336d_s00_base_v048_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 336)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_378d_s00_base_v049_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_378d_s00_base_v050_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_378d_s00_base_v051_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 378)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_420d_s00_base_v052_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_420d_s00_base_v053_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_420d_s00_base_v054_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 420)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_462d_s00_base_v055_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_462d_s00_base_v056_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_462d_s00_base_v057_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 462)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_504d_s00_base_v058_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_504d_s00_base_v059_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_tq_frd_504d_s00_base_v060_signal(fcf, revenue, dps, roic, closeadj):
    base = _f49_terminal_quality(fcf, revenue, dps, 504)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v061_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v062_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v063_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v064_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v065_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v066_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v067_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v068_signal(roic, fcf, revenue, ebitdamargin, closeadj):
    base = _f49_quality_composite(roic, fcf, revenue, 5)
    result = _ema(base, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v069_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _ema(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v070_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _ema(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v071_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _ema(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v072_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _ema(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v073_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _ema(base, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v074_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _ema(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v075_signal(roic, ebitdamargin, fcf, revenue, closeadj):
    base = _f49_compounder_score(roic, ebitdamargin, 5)
    result = _ema(base, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s00_base_v001_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s00_base_v002_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_5d_s00_base_v003_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_10d_s00_base_v004_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_10d_s00_base_v005_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_10d_s00_base_v006_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_21d_s00_base_v007_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_21d_s00_base_v008_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_21d_s00_base_v009_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_42d_s00_base_v010_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_42d_s00_base_v011_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_42d_s00_base_v012_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_63d_s00_base_v013_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_63d_s00_base_v014_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_63d_s00_base_v015_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_84d_s00_base_v016_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_84d_s00_base_v017_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_84d_s00_base_v018_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_105d_s00_base_v019_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_105d_s00_base_v020_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_105d_s00_base_v021_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_126d_s00_base_v022_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_126d_s00_base_v023_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_126d_s00_base_v024_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_147d_s00_base_v025_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_147d_s00_base_v026_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_147d_s00_base_v027_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_168d_s00_base_v028_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_168d_s00_base_v029_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_168d_s00_base_v030_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_189d_s00_base_v031_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_189d_s00_base_v032_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_189d_s00_base_v033_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_210d_s00_base_v034_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_210d_s00_base_v035_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_210d_s00_base_v036_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_231d_s00_base_v037_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_231d_s00_base_v038_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_231d_s00_base_v039_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_252d_s00_base_v040_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_252d_s00_base_v041_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_252d_s00_base_v042_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_294d_s00_base_v043_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_294d_s00_base_v044_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_294d_s00_base_v045_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_336d_s00_base_v046_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_336d_s00_base_v047_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_336d_s00_base_v048_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_378d_s00_base_v049_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_378d_s00_base_v050_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_378d_s00_base_v051_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_420d_s00_base_v052_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_420d_s00_base_v053_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_420d_s00_base_v054_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_462d_s00_base_v055_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_462d_s00_base_v056_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_462d_s00_base_v057_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_504d_s00_base_v058_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_504d_s00_base_v059_signal,
    f49utc_f49_utility_terminal_compounder_tq_frd_504d_s00_base_v060_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v061_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v062_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v063_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v064_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v065_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v066_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v067_signal,
    f49utc_f49_utility_terminal_compounder_qc_rfr_5d_s01_base_v068_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v069_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v070_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v071_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v072_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v073_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v074_signal,
    f49utc_f49_utility_terminal_compounder_cs_re_5d_s01_base_v075_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F49_UTILITY_TERMINAL_COMPOUNDER_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    dps     = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "dps": dps, "ebitdamargin": ebitdamargin, "fcf": fcf, "revenue": revenue, "roic": roic}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f49_quality_composite", "_f49_compounder_score", "_f49_terminal_quality",)
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
    print(f"OK f49_utility_terminal_compounder_base_001_075_claude: {n_features} features pass")
