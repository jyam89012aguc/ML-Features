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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f47_quiet_fcf_growth(fcf, w):
    m = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = fcf.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return m / sd


def _f47_low_attention_growth(closeadj, volume, fcf, w):
    dv = (closeadj * volume).rolling(w, min_periods=max(1, w // 2)).mean()
    g = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    return g * closeadj / dv.replace(0, np.nan)


def _f47_hidden_quality_score(fcf, roic, w):
    fg = fcf.rolling(w, min_periods=max(1, w // 2)).mean()
    rq = roic.rolling(w, min_periods=max(1, w // 2)).mean()
    return fg * rq


# ===== features =====
def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s00_jw21_jerk_v001_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s00_jw63_jerk_v002_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s00_jw126_jerk_v003_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s00_jw21_jerk_v004_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s00_jw63_jerk_v005_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_5d_s00_jw126_jerk_v006_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_5d_s00_jw21_jerk_v007_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 5)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_5d_s00_jw63_jerk_v008_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 5)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_5d_s00_jw126_jerk_v009_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 5)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_10d_s00_jw21_jerk_v010_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_10d_s00_jw63_jerk_v011_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 10)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_10d_s00_jw126_jerk_v012_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 10)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_10d_s00_jw21_jerk_v013_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_10d_s00_jw63_jerk_v014_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 10)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_10d_s00_jw126_jerk_v015_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 10)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_10d_s00_jw21_jerk_v016_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 10)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_10d_s00_jw63_jerk_v017_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 10)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_10d_s00_jw126_jerk_v018_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 10)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_21d_s00_jw21_jerk_v019_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_21d_s00_jw63_jerk_v020_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_21d_s00_jw126_jerk_v021_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_21d_s00_jw21_jerk_v022_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_21d_s00_jw63_jerk_v023_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_21d_s00_jw126_jerk_v024_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_21d_s00_jw21_jerk_v025_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 21)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_21d_s00_jw63_jerk_v026_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 21)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_21d_s00_jw126_jerk_v027_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 21)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_42d_s00_jw21_jerk_v028_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_42d_s00_jw63_jerk_v029_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_42d_s00_jw126_jerk_v030_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_42d_s00_jw21_jerk_v031_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_42d_s00_jw63_jerk_v032_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_42d_s00_jw126_jerk_v033_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_42d_s00_jw21_jerk_v034_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 42)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_42d_s00_jw63_jerk_v035_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 42)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_42d_s00_jw126_jerk_v036_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 42)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_63d_s00_jw21_jerk_v037_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_63d_s00_jw63_jerk_v038_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_63d_s00_jw126_jerk_v039_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_63d_s00_jw21_jerk_v040_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_63d_s00_jw63_jerk_v041_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_63d_s00_jw126_jerk_v042_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_63d_s00_jw21_jerk_v043_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 63)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_63d_s00_jw63_jerk_v044_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 63)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_63d_s00_jw126_jerk_v045_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 63)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_84d_s00_jw21_jerk_v046_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_84d_s00_jw63_jerk_v047_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_84d_s00_jw126_jerk_v048_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_84d_s00_jw21_jerk_v049_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_84d_s00_jw63_jerk_v050_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_84d_s00_jw126_jerk_v051_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s00_jw21_jerk_v052_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 84)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s00_jw63_jerk_v053_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 84)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s00_jw126_jerk_v054_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 84)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s00_jw21_jerk_v055_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s00_jw63_jerk_v056_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s00_jw126_jerk_v057_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 105)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s00_jw21_jerk_v058_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s00_jw63_jerk_v059_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_105d_s00_jw126_jerk_v060_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 105)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s00_jw21_jerk_v061_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s00_jw63_jerk_v062_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s00_jw126_jerk_v063_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 105)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s00_jw21_jerk_v064_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s00_jw63_jerk_v065_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s00_jw126_jerk_v066_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s00_jw21_jerk_v067_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s00_jw63_jerk_v068_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_126d_s00_jw126_jerk_v069_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s00_jw21_jerk_v070_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s00_jw63_jerk_v071_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s00_jw126_jerk_v072_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 126)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s00_jw21_jerk_v073_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s00_jw63_jerk_v074_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s00_jw126_jerk_v075_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 147)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s00_jw21_jerk_v076_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s00_jw63_jerk_v077_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_147d_s00_jw126_jerk_v078_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 147)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s00_jw21_jerk_v079_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s00_jw63_jerk_v080_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s00_jw126_jerk_v081_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 147)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_168d_s00_jw21_jerk_v082_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 168)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_168d_s00_jw63_jerk_v083_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 168)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_168d_s00_jw126_jerk_v084_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 168)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_168d_s00_jw21_jerk_v085_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 168)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_168d_s00_jw63_jerk_v086_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 168)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_168d_s00_jw126_jerk_v087_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 168)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_168d_s00_jw21_jerk_v088_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 168)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_168d_s00_jw63_jerk_v089_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 168)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_168d_s00_jw126_jerk_v090_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 168)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_189d_s00_jw21_jerk_v091_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 189)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_189d_s00_jw63_jerk_v092_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 189)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_189d_s00_jw126_jerk_v093_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 189)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_189d_s00_jw21_jerk_v094_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 189)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_189d_s00_jw63_jerk_v095_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 189)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_189d_s00_jw126_jerk_v096_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 189)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_189d_s00_jw21_jerk_v097_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 189)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_189d_s00_jw63_jerk_v098_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 189)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_189d_s00_jw126_jerk_v099_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 189)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_210d_s00_jw21_jerk_v100_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 210)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_210d_s00_jw63_jerk_v101_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 210)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_210d_s00_jw126_jerk_v102_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 210)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_210d_s00_jw21_jerk_v103_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 210)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_210d_s00_jw63_jerk_v104_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 210)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_210d_s00_jw126_jerk_v105_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 210)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_210d_s00_jw21_jerk_v106_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 210)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_210d_s00_jw63_jerk_v107_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 210)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_210d_s00_jw126_jerk_v108_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 210)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_231d_s00_jw21_jerk_v109_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 231)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_231d_s00_jw63_jerk_v110_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 231)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_231d_s00_jw126_jerk_v111_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 231)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_231d_s00_jw21_jerk_v112_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 231)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_231d_s00_jw63_jerk_v113_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 231)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_231d_s00_jw126_jerk_v114_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 231)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_231d_s00_jw21_jerk_v115_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 231)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_231d_s00_jw63_jerk_v116_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 231)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_231d_s00_jw126_jerk_v117_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 231)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_252d_s00_jw21_jerk_v118_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_252d_s00_jw63_jerk_v119_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_252d_s00_jw126_jerk_v120_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_252d_s00_jw21_jerk_v121_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_252d_s00_jw63_jerk_v122_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_252d_s00_jw126_jerk_v123_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_252d_s00_jw21_jerk_v124_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 252)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_252d_s00_jw63_jerk_v125_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 252)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_252d_s00_jw126_jerk_v126_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 252)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_294d_s00_jw21_jerk_v127_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 294)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_294d_s00_jw63_jerk_v128_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 294)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_294d_s00_jw126_jerk_v129_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 294)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_294d_s00_jw21_jerk_v130_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 294)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_294d_s00_jw63_jerk_v131_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 294)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_294d_s00_jw126_jerk_v132_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 294)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_294d_s00_jw21_jerk_v133_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 294)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_294d_s00_jw63_jerk_v134_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 294)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_294d_s00_jw126_jerk_v135_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 294)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_336d_s00_jw21_jerk_v136_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 336)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_336d_s00_jw63_jerk_v137_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 336)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_336d_s00_jw126_jerk_v138_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 336)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_336d_s00_jw21_jerk_v139_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 336)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_336d_s00_jw63_jerk_v140_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 336)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_336d_s00_jw126_jerk_v141_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 336)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_336d_s00_jw21_jerk_v142_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 336)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_336d_s00_jw63_jerk_v143_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 336)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_hq_fr_336d_s00_jw126_jerk_v144_signal(fcf, roic, closeadj):
    base = _f47_hidden_quality_score(fcf, roic, 336)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_378d_s00_jw21_jerk_v145_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 378)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_378d_s00_jw63_jerk_v146_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 378)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_qf_fcf_378d_s00_jw126_jerk_v147_signal(fcf, closeadj, volume):
    base = _f47_quiet_fcf_growth(fcf, 378)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_378d_s00_jw21_jerk_v148_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 378)
    result = _jerk(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_378d_s00_jw63_jerk_v149_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 378)
    result = _jerk(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f47hrc_f47_hidden_renewable_compounder_la_full_378d_s00_jw126_jerk_v150_signal(closeadj, volume, fcf):
    base = _f47_low_attention_growth(closeadj, volume, fcf, 378)
    result = _jerk(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s00_jw21_jerk_v001_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s00_jw63_jerk_v002_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_5d_s00_jw126_jerk_v003_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s00_jw21_jerk_v004_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s00_jw63_jerk_v005_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_5d_s00_jw126_jerk_v006_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_5d_s00_jw21_jerk_v007_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_5d_s00_jw63_jerk_v008_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_5d_s00_jw126_jerk_v009_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_10d_s00_jw21_jerk_v010_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_10d_s00_jw63_jerk_v011_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_10d_s00_jw126_jerk_v012_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_10d_s00_jw21_jerk_v013_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_10d_s00_jw63_jerk_v014_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_10d_s00_jw126_jerk_v015_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_10d_s00_jw21_jerk_v016_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_10d_s00_jw63_jerk_v017_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_10d_s00_jw126_jerk_v018_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_21d_s00_jw21_jerk_v019_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_21d_s00_jw63_jerk_v020_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_21d_s00_jw126_jerk_v021_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_21d_s00_jw21_jerk_v022_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_21d_s00_jw63_jerk_v023_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_21d_s00_jw126_jerk_v024_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_21d_s00_jw21_jerk_v025_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_21d_s00_jw63_jerk_v026_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_21d_s00_jw126_jerk_v027_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_42d_s00_jw21_jerk_v028_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_42d_s00_jw63_jerk_v029_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_42d_s00_jw126_jerk_v030_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_42d_s00_jw21_jerk_v031_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_42d_s00_jw63_jerk_v032_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_42d_s00_jw126_jerk_v033_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_42d_s00_jw21_jerk_v034_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_42d_s00_jw63_jerk_v035_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_42d_s00_jw126_jerk_v036_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_63d_s00_jw21_jerk_v037_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_63d_s00_jw63_jerk_v038_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_63d_s00_jw126_jerk_v039_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_63d_s00_jw21_jerk_v040_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_63d_s00_jw63_jerk_v041_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_63d_s00_jw126_jerk_v042_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_63d_s00_jw21_jerk_v043_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_63d_s00_jw63_jerk_v044_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_63d_s00_jw126_jerk_v045_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_84d_s00_jw21_jerk_v046_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_84d_s00_jw63_jerk_v047_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_84d_s00_jw126_jerk_v048_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_84d_s00_jw21_jerk_v049_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_84d_s00_jw63_jerk_v050_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_84d_s00_jw126_jerk_v051_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s00_jw21_jerk_v052_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s00_jw63_jerk_v053_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_84d_s00_jw126_jerk_v054_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s00_jw21_jerk_v055_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s00_jw63_jerk_v056_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_105d_s00_jw126_jerk_v057_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s00_jw21_jerk_v058_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s00_jw63_jerk_v059_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_105d_s00_jw126_jerk_v060_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s00_jw21_jerk_v061_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s00_jw63_jerk_v062_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_105d_s00_jw126_jerk_v063_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s00_jw21_jerk_v064_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s00_jw63_jerk_v065_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_126d_s00_jw126_jerk_v066_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s00_jw21_jerk_v067_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s00_jw63_jerk_v068_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_126d_s00_jw126_jerk_v069_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s00_jw21_jerk_v070_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s00_jw63_jerk_v071_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_126d_s00_jw126_jerk_v072_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s00_jw21_jerk_v073_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s00_jw63_jerk_v074_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_147d_s00_jw126_jerk_v075_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s00_jw21_jerk_v076_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s00_jw63_jerk_v077_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_147d_s00_jw126_jerk_v078_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s00_jw21_jerk_v079_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s00_jw63_jerk_v080_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_147d_s00_jw126_jerk_v081_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_168d_s00_jw21_jerk_v082_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_168d_s00_jw63_jerk_v083_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_168d_s00_jw126_jerk_v084_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_168d_s00_jw21_jerk_v085_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_168d_s00_jw63_jerk_v086_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_168d_s00_jw126_jerk_v087_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_168d_s00_jw21_jerk_v088_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_168d_s00_jw63_jerk_v089_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_168d_s00_jw126_jerk_v090_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_189d_s00_jw21_jerk_v091_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_189d_s00_jw63_jerk_v092_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_189d_s00_jw126_jerk_v093_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_189d_s00_jw21_jerk_v094_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_189d_s00_jw63_jerk_v095_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_189d_s00_jw126_jerk_v096_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_189d_s00_jw21_jerk_v097_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_189d_s00_jw63_jerk_v098_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_189d_s00_jw126_jerk_v099_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_210d_s00_jw21_jerk_v100_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_210d_s00_jw63_jerk_v101_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_210d_s00_jw126_jerk_v102_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_210d_s00_jw21_jerk_v103_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_210d_s00_jw63_jerk_v104_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_210d_s00_jw126_jerk_v105_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_210d_s00_jw21_jerk_v106_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_210d_s00_jw63_jerk_v107_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_210d_s00_jw126_jerk_v108_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_231d_s00_jw21_jerk_v109_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_231d_s00_jw63_jerk_v110_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_231d_s00_jw126_jerk_v111_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_231d_s00_jw21_jerk_v112_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_231d_s00_jw63_jerk_v113_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_231d_s00_jw126_jerk_v114_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_231d_s00_jw21_jerk_v115_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_231d_s00_jw63_jerk_v116_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_231d_s00_jw126_jerk_v117_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_252d_s00_jw21_jerk_v118_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_252d_s00_jw63_jerk_v119_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_252d_s00_jw126_jerk_v120_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_252d_s00_jw21_jerk_v121_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_252d_s00_jw63_jerk_v122_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_252d_s00_jw126_jerk_v123_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_252d_s00_jw21_jerk_v124_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_252d_s00_jw63_jerk_v125_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_252d_s00_jw126_jerk_v126_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_294d_s00_jw21_jerk_v127_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_294d_s00_jw63_jerk_v128_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_294d_s00_jw126_jerk_v129_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_294d_s00_jw21_jerk_v130_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_294d_s00_jw63_jerk_v131_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_294d_s00_jw126_jerk_v132_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_294d_s00_jw21_jerk_v133_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_294d_s00_jw63_jerk_v134_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_294d_s00_jw126_jerk_v135_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_336d_s00_jw21_jerk_v136_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_336d_s00_jw63_jerk_v137_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_336d_s00_jw126_jerk_v138_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_336d_s00_jw21_jerk_v139_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_336d_s00_jw63_jerk_v140_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_336d_s00_jw126_jerk_v141_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_336d_s00_jw21_jerk_v142_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_336d_s00_jw63_jerk_v143_signal,
    f47hrc_f47_hidden_renewable_compounder_hq_fr_336d_s00_jw126_jerk_v144_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_378d_s00_jw21_jerk_v145_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_378d_s00_jw63_jerk_v146_signal,
    f47hrc_f47_hidden_renewable_compounder_qf_fcf_378d_s00_jw126_jerk_v147_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_378d_s00_jw21_jerk_v148_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_378d_s00_jw63_jerk_v149_signal,
    f47hrc_f47_hidden_renewable_compounder_la_full_378d_s00_jw126_jerk_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F47_HIDDEN_RENEWABLE_COMPOUNDER_REGISTRY_JERK_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    roic    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    cols = {"closeadj": closeadj, "fcf": fcf, "roic": roic, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f47_quiet_fcf_growth", "_f47_low_attention_growth", "_f47_hidden_quality_score",)
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
    print(f"OK f47_hidden_renewable_compounder_3rd_derivatives_001_150_claude: {n_features} features pass")
