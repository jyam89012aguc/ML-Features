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


def _f25_quiet_fcf_compound(fcf, w):
    g = fcf.pct_change(periods=w)
    mu = g.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = g.rolling(w, min_periods=max(1, w // 2)).std()
    return mu - sd


def _f25_low_attention_high_growth(closeadj, volume, fcf, w):
    vz = -((volume - volume.rolling(w, min_periods=max(1, w // 2)).mean())
           / volume.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan))
    g = fcf.pct_change(periods=w)
    gm = g.rolling(w, min_periods=max(1, w // 2)).mean()
    return vz + gm


def _f25_compounder_undiscovered(fcf, marketcap, w):
    yield_ = fcf / marketcap.replace(0, np.nan).abs()
    return yield_.rolling(w, min_periods=max(1, w // 2)).mean()


_FEATURES = []


def _add(fn):
    _FEATURES.append(fn)
    return fn


# 50 qfcf slopes
@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_5d_slope_v001_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_10d_slope_v002_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_21d_slope_v003_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_42d_slope_v004_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_63d_slope_v005_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_126d_slope_v006_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_252d_slope_v007_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_pct(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w21_21d_slope_v008_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w126_21d_slope_v009_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w252_21d_slope_v010_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w252_63d_slope_v011_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w504_63d_slope_v012_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w42_21d_slope_v013_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w189_42d_slope_v014_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w378_63d_slope_v015_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 378) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_dn21_slope_v016_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_dn63_slope_v017_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_dn126_slope_v018_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_ema21_21d_slope_v019_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_ema63_21d_slope_v020_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_ema252_63d_slope_v021_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_z252_21d_slope_v022_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_std63_21d_slope_v023_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = _std(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_log_21d_slope_v024_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_sq_21d_slope_v025_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_inv_21d_slope_v026_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = (1.0 / (base.abs() + 1e-6)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_rank_21d_slope_v027_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_med_21d_slope_v028_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_range_21d_slope_v029_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_pct(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_demean_21d_slope_v030_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_xfcf_21d_slope_v031_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    fg = fcf / (fcf.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * fg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# LAHG slopes
@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_5d_slope_v032_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_10d_slope_v033_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_21d_slope_v034_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_42d_slope_v035_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_63d_slope_v036_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_126d_slope_v037_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w21_21d_slope_v038_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w126_21d_slope_v039_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w252_63d_slope_v040_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w504_63d_slope_v041_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w42_21d_slope_v042_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w189_42d_slope_v043_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_dn21_slope_v044_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_dn63_slope_v045_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_ema21_21d_slope_v046_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_ema63_21d_slope_v047_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_ema252_63d_slope_v048_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_z252_21d_slope_v049_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_std63_21d_slope_v050_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = _std(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_log_21d_slope_v051_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_sq_21d_slope_v052_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_inv_21d_slope_v053_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = (1.0 / (base.abs() + 1e-6)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_rank_21d_slope_v054_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_med_21d_slope_v055_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_range_21d_slope_v056_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_pct(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_demean_21d_slope_v057_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_xvol_21d_slope_v058_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    vg = volume / (volume.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * vg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# UND slopes
@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_5d_slope_v059_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_pct(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_10d_slope_v060_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_pct(base, 10)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_21d_slope_v061_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_42d_slope_v062_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_63d_slope_v063_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_126d_slope_v064_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_pct(base, 126)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w21_21d_slope_v065_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 21) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w126_21d_slope_v066_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 126) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w252_63d_slope_v067_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 252) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w504_63d_slope_v068_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 504) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w42_21d_slope_v069_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w189_42d_slope_v070_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 189) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_dn21_slope_v071_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_dn63_slope_v072_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_ema21_21d_slope_v073_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = base.ewm(span=21, min_periods=5).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_ema63_21d_slope_v074_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = base.ewm(span=63, min_periods=10).mean() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_ema252_63d_slope_v075_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = base.ewm(span=252, min_periods=63).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_z252_21d_slope_v076_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_std63_21d_slope_v077_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = _std(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_log_21d_slope_v078_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63).abs() + 1.0
    base = np.log(base) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_sq_21d_slope_v079_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = base * base * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_inv_21d_slope_v080_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = (1.0 / (base.abs() + 1e-6)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_rank_21d_slope_v081_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    rk = base.rolling(252, min_periods=63).rank(pct=True) * closeadj
    result = _slope_pct(rk, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_med_21d_slope_v082_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = base.rolling(252, min_periods=63).median() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_range_21d_slope_v083_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    rng = (base.rolling(252, min_periods=63).max() - base.rolling(252, min_periods=63).min()) * closeadj
    result = _slope_pct(rng, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_demean_21d_slope_v084_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = (base - _mean(base, 252)) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_xmcap_21d_slope_v085_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    mg = marketcap / (marketcap.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * mg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# composites slopes 086..150
@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_x_und_21d_slope_v086_signal(fcf, marketcap, closeadj):
    q = _f25_quiet_fcf_compound(fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = q * u * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_plus_und_21d_slope_v087_signal(fcf, marketcap, closeadj):
    q = _f25_quiet_fcf_compound(fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = (q + u) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_x_lahg_21d_slope_v088_signal(closeadj, volume, fcf):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = q * l * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_x_lahg_21d_slope_v089_signal(closeadj, volume, fcf, marketcap):
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = l * u * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_triple_sum_21d_slope_v090_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = (q + l + u) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_triple_w_21d_slope_v091_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = (0.4 * q + 0.3 * l + 0.3 * u) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_triple_product_21d_slope_v092_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = q * l * u * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_cross_63_252_slope_v093_signal(fcf, closeadj):
    a = _f25_quiet_fcf_compound(fcf, 63)
    b = _f25_quiet_fcf_compound(fcf, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_cross_63_252_slope_v094_signal(closeadj, volume, fcf):
    a = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    b = _f25_low_attention_high_growth(closeadj, volume, fcf, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_cross_63_252_slope_v095_signal(fcf, marketcap, closeadj):
    a = _f25_compounder_undiscovered(fcf, marketcap, 63)
    b = _f25_compounder_undiscovered(fcf, marketcap, 252)
    base = (a - b) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_w42_21d_slope_v096_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 63), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_w42_21d_slope_v097_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 63), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_w42_21d_slope_v098_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 63), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w252_w42_21d_slope_v099_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 252), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w252_w42_21d_slope_v100_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 252), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w252_w42_21d_slope_v101_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 252), 42) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w504_w63_21d_slope_v102_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 504), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w504_w63_21d_slope_v103_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 504), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w504_w63_21d_slope_v104_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 504), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_xclose2_21d_slope_v105_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_xclose2_21d_slope_v106_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_xclose2_21d_slope_v107_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj * closeadj / 100.0
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_xfcf_21d_slope_v108_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    fg = fcf / (fcf.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * fg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_xfcf_21d_slope_v109_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    fg = fcf / (fcf.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * fg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_xfcf_21d_slope_v110_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    fg = fcf / (fcf.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * fg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_streak_pos_21d_slope_v111_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(streak, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_streak_pos_21d_slope_v112_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    pos = (base > 0).astype(float)
    streak = pos.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(streak, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_streak_high_21d_slope_v113_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    high = (base > base.rolling(252, min_periods=63).median()).astype(float)
    streak = high.rolling(252, min_periods=63).sum() * closeadj
    result = _slope_pct(streak, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_w63_21d_slope_v114_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 63), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_w63_21d_slope_v115_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 63), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_w63_21d_slope_v116_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 63), 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_w126_63d_slope_v117_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 63), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_w126_63d_slope_v118_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 63), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_w126_63d_slope_v119_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 63), 126) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_xvolume_21d_slope_v120_signal(fcf, volume, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    vg = volume / (volume.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * vg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_xvolume_21d_slope_v121_signal(fcf, marketcap, volume, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    vg = volume / (volume.rolling(252, min_periods=63).mean().replace(0, np.nan))
    base = base * vg * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_dn5_slope_v122_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_dn5_slope_v123_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_dn5_slope_v124_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_dn252_slope_v125_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_dn252_slope_v126_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_dn252_slope_v127_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63) * closeadj
    result = _slope_diff_norm(base, 252)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_z63_21d_slope_v128_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = _z(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_z63_21d_slope_v129_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = _z(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_z63_21d_slope_v130_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = _z(base, 63) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_ema126_63d_slope_v131_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_ema126_63d_slope_v132_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_ema126_63d_slope_v133_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = base.ewm(span=126, min_periods=21).mean() * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_above_qt_21d_slope_v134_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base * closeadj
    result = _slope_pct(ind, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_above_qt_21d_slope_v135_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base * closeadj
    result = _slope_pct(ind, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_above_qt_21d_slope_v136_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    qt = base.rolling(252, min_periods=63).quantile(0.5)
    ind = (base > qt).astype(float) * base * closeadj
    result = _slope_pct(ind, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_sign_21d_slope_v137_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    sg = np.sign(base) * closeadj
    result = _slope_pct(sg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_sign_21d_slope_v138_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    sg = np.sign(base) * closeadj
    result = _slope_pct(sg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_sign_21d_slope_v139_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    sg = np.sign(base) * closeadj
    result = _slope_pct(sg, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_min_252d_21d_slope_v140_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = base.rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_min_252d_21d_slope_v141_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = base.rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_min_252d_21d_slope_v142_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = base.rolling(252, min_periods=63).min() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_max_252d_21d_slope_v143_signal(fcf, closeadj):
    base = _f25_quiet_fcf_compound(fcf, 63)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_max_252d_21d_slope_v144_signal(closeadj, volume, fcf):
    base = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_max_252d_21d_slope_v145_signal(fcf, marketcap, closeadj):
    base = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = base.rolling(252, min_periods=63).max() * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_triple_z252_21d_slope_v146_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = q + l + u
    base = _z(base, 252) * closeadj
    result = _slope_pct(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_qfcf_w63_w63_42d_slope_v147_signal(fcf, closeadj):
    base = _mean(_f25_quiet_fcf_compound(fcf, 63), 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_lahg_w63_w63_42d_slope_v148_signal(closeadj, volume, fcf):
    base = _mean(_f25_low_attention_high_growth(closeadj, volume, fcf, 63), 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_und_w63_w63_42d_slope_v149_signal(fcf, marketcap, closeadj):
    base = _mean(_f25_compounder_undiscovered(fcf, marketcap, 63), 63) * closeadj
    result = _slope_pct(base, 42)
    return result.replace([np.inf, -np.inf], np.nan)


@_add
def f25hcd_f25_hidden_compounder_detector_triple_w_63d_slope_v150_signal(closeadj, volume, fcf, marketcap):
    q = _f25_quiet_fcf_compound(fcf, 63)
    l = _f25_low_attention_high_growth(closeadj, volume, fcf, 63)
    u = _f25_compounder_undiscovered(fcf, marketcap, 63)
    base = (0.4 * q + 0.3 * l + 0.3 * u) * closeadj
    result = _slope_pct(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F25_HIDDEN_COMPOUNDER_DETECTOR_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")
    fcf = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")

    cols = {"closeadj": closeadj, "volume": volume, "fcf": fcf, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f25_quiet_fcf_compound", "_f25_low_attention_high_growth", "_f25_compounder_undiscovered")
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
    print(f"OK f25_hidden_compounder_detector_2nd_derivatives_001_150_claude: {n_features} features pass")
