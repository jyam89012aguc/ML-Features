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


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f08_capex_growth(capex, w):
    return capex.pct_change(periods=w)


def _f08_capex_to_revenue(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f08_capex_intensity_change(capex, revenue, w):
    intens = capex / revenue.replace(0, np.nan).abs()
    return intens.diff(periods=w)


def _make_features():
    feats = []

    # base concept building blocks (name, callable building base series)
    # Each tuple: (concept_name, base_fn(closeadj, capex, revenue) -> series, inputs_signature_tuple)
    # We'll use closures to bind args.

    return feats


# Build 150 slope features systematically with explicit definitions

# 1: slope of 21d capex growth, 5d
def f08cap_f08_capex_acceleration_grow_21d_slope_v001_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_21d_slope_v002_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_63d_slope_v003_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_63d_slope_v004_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 63) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_126d_slope_v005_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 126) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_126d_slope_v006_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 126) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_252d_slope_v007_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_252d_slope_v008_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_504d_slope_v009_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_504d_slope_v010_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_21d_slope_v011_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 21) * closeadj
    return _slope_pct(base, 5).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_21d_slope_v012_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_63d_slope_v013_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_63d_slope_v014_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 63) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_126d_slope_v015_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 126) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_126d_slope_v016_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 126) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_252d_slope_v017_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 252) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_252d_slope_v018_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_504d_slope_v019_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 504) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_504d_slope_v020_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_21d_slope_v021_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 21) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_21d_slope_v022_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_63d_slope_v023_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_126d_slope_v024_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 126) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_252d_slope_v025_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 252) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_252d_slope_v026_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_504d_slope_v027_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_504d_slope_v028_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growstd_21d_slope_v029_signal(capex, closeadj):
    base = _std(_f08_capex_growth(capex, 21), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growstd_63d_slope_v030_signal(capex, closeadj):
    base = _std(_f08_capex_growth(capex, 21), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growstd_252d_slope_v031_signal(capex, closeadj):
    base = _std(_f08_capex_growth(capex, 21), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growstd_504d_slope_v032_signal(capex, closeadj):
    base = _std(_f08_capex_growth(capex, 21), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevstd_21d_slope_v033_signal(capex, revenue, closeadj):
    base = _std(_f08_capex_to_revenue(capex, revenue), 21) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevstd_63d_slope_v034_signal(capex, revenue, closeadj):
    base = _std(_f08_capex_to_revenue(capex, revenue), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevstd_252d_slope_v035_signal(capex, revenue, closeadj):
    base = _std(_f08_capex_to_revenue(capex, revenue), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevstd_504d_slope_v036_signal(capex, revenue, closeadj):
    base = _std(_f08_capex_to_revenue(capex, revenue), 504) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growz_21d_slope_v037_signal(capex, closeadj):
    base = _z(_f08_capex_growth(capex, 21), 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growz_63d_slope_v038_signal(capex, closeadj):
    base = _z(_f08_capex_growth(capex, 21), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growz_252d_slope_v039_signal(capex, closeadj):
    base = _z(_f08_capex_growth(capex, 21), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growz_504d_slope_v040_signal(capex, closeadj):
    base = _z(_f08_capex_growth(capex, 21), 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevz_21d_slope_v041_signal(capex, revenue, closeadj):
    base = _z(_f08_capex_to_revenue(capex, revenue), 21) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevz_63d_slope_v042_signal(capex, revenue, closeadj):
    base = _z(_f08_capex_to_revenue(capex, revenue), 63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevz_252d_slope_v043_signal(capex, revenue, closeadj):
    base = _z(_f08_capex_to_revenue(capex, revenue), 252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevz_504d_slope_v044_signal(capex, revenue, closeadj):
    base = _z(_f08_capex_to_revenue(capex, revenue), 504) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_5d_slope_v045_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 5) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_10d_slope_v046_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 10) * closeadj
    return _slope_diff_norm(base, 10).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_42d_slope_v047_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 42) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_189d_slope_v048_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 189) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_378d_slope_v049_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 378) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_5d_slope_v050_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 5) * closeadj
    return _slope_pct(base, 5).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_10d_slope_v051_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 10) * closeadj
    return _slope_pct(base, 10).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_42d_slope_v052_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 42) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_189d_slope_v053_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 189) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_378d_slope_v054_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 378) * closeadj
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growema_21d_slope_v055_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growema_63d_slope_v056_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growema_252d_slope_v057_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 21).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevema_21d_slope_v058_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue).ewm(span=21, adjust=False).mean() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevema_63d_slope_v059_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevema_252d_slope_v060_signal(capex, revenue, closeadj):
    base = _f08_capex_to_revenue(capex, revenue).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevgap_21v252_slope_v061_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    base = (_mean(b, 21) - _mean(b, 252)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevgap_63v252_slope_v062_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    base = (_mean(b, 63) - _mean(b, 252)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevgap_63v504_slope_v063_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    base = (_mean(b, 63) - _mean(b, 504)) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevgap_126v504_slope_v064_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    base = (_mean(b, 126) - _mean(b, 504)) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growsq_63d_slope_v065_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 63)
    base = g * g.abs() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growsq_252d_slope_v066_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 252)
    base = g * g.abs() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevsq_63d_slope_v067_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    base = _mean(b * b, 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevsq_252d_slope_v068_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    base = _mean(b * b, 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxcrev_21d_slope_v069_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 21)
    c = _f08_capex_to_revenue(capex, revenue)
    base = g * c * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxcrev_63d_slope_v070_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    c = _f08_capex_to_revenue(capex, revenue)
    base = g * c * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxcrev_252d_slope_v071_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    c = _f08_capex_to_revenue(capex, revenue)
    base = g * c * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintema_63d_slope_v072_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 63).ewm(span=63, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintema_252d_slope_v073_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 252).ewm(span=252, adjust=False).mean() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxrev_63d_slope_v074_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    base = g * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxrev_252d_slope_v075_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    base = g * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintxrev_63d_slope_v076_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 63)
    base = i * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintxrev_252d_slope_v077_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 252)
    base = i * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevxcret_63d_slope_v078_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cret = closeadj.pct_change(63)
    base = c * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevxcret_252d_slope_v079_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cret = closeadj.pct_change(252)
    base = c * cret * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growsign_63d_slope_v080_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 63)
    base = np.sign(g) * g.abs() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxprice_21d_slope_v081_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = g * closeadj * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxprice_63d_slope_v082_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 63)
    base = g * closeadj * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxprice_252d_slope_v083_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 252)
    base = g * closeadj * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevxprice_63d_slope_v084_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = _mean(c, 63) * closeadj * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevxprice_252d_slope_v085_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = _mean(c, 252) * closeadj * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growabs_63d_slope_v086_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = _mean(g.abs(), 63) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growabs_252d_slope_v087_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = _mean(g.abs(), 252) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growsum_63d_slope_v088_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    base = g.rolling(63, min_periods=21).sum() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growsum_252d_slope_v089_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    base = g.rolling(252, min_periods=63).sum() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growmax_63d_slope_v090_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = g.rolling(63, min_periods=21).max() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growmax_252d_slope_v091_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = g.rolling(252, min_periods=63).max() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growmin_63d_slope_v092_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = g.rolling(63, min_periods=21).min() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growmin_252d_slope_v093_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = g.rolling(252, min_periods=63).min() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growrng_252d_slope_v094_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    rng = g.rolling(252, min_periods=63).max() - g.rolling(252, min_periods=63).min()
    base = rng * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevmax_252d_slope_v095_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = c.rolling(252, min_periods=63).max() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevmin_252d_slope_v096_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = c.rolling(252, min_periods=63).min() * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevrng_252d_slope_v097_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    rng = c.rolling(252, min_periods=63).max() - c.rolling(252, min_periods=63).min()
    base = rng * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevpct_252d_slope_v098_signal(capex, revenue, closeadj):
    b = _f08_capex_to_revenue(capex, revenue)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growpct_252d_slope_v099_signal(capex, closeadj):
    b = _f08_capex_growth(capex, 21)
    mx = b.rolling(252, min_periods=63).max()
    mn = b.rolling(252, min_periods=63).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growpct_504d_slope_v100_signal(capex, closeadj):
    b = _f08_capex_growth(capex, 21)
    mx = b.rolling(504, min_periods=126).max()
    mn = b.rolling(504, min_periods=126).min()
    rng = (mx - mn).replace(0, np.nan)
    base = ((b - mn) / rng) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxcret_63d_slope_v101_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 63)
    cret = closeadj.pct_change(63)
    base = g * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxcret_252d_slope_v102_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 252)
    cret = closeadj.pct_change(252)
    base = g * cret * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintxcret_63d_slope_v103_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 63)
    cret = closeadj.pct_change(63)
    base = i * cret * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintxcret_252d_slope_v104_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 252)
    cret = closeadj.pct_change(252)
    base = i * cret * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growsqrt_63d_slope_v105_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21).abs()
    base = np.sqrt(_mean(g, 63)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growsqrt_252d_slope_v106_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21).abs()
    base = np.sqrt(_mean(g, 252)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevsqrt_63d_slope_v107_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue).abs()
    base = np.sqrt(_mean(c, 63)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevsqrt_252d_slope_v108_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue).abs()
    base = np.sqrt(_mean(c, 252)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevcv_63d_slope_v109_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cv = _std(c, 63) / _mean(c, 63).replace(0, np.nan).abs()
    base = cv * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevcv_252d_slope_v110_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    cv = _std(c, 252) / _mean(c, 252).replace(0, np.nan).abs()
    base = cv * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_accelcount_63d_slope_v111_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    accel = (g > 0.05).astype(float)
    base = accel.rolling(63, min_periods=21).sum() * closeadj + g
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_accelcount_252d_slope_v112_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    accel = (g > 0.05).astype(float)
    base = accel.rolling(252, min_periods=63).sum() * closeadj + g
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_decelcount_252d_slope_v113_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    dec = (g < -0.05).astype(float)
    base = dec.rolling(252, min_periods=63).sum() * closeadj + g
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_decelcount_504d_slope_v114_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 5)
    dec = (g < -0.05).astype(float)
    base = dec.rolling(504, min_periods=126).sum() * closeadj + g
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_capratio_63v252_slope_v115_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    ratio = _mean(capex, 63) / _mean(capex, 252).replace(0, np.nan).abs()
    base = ratio * closeadj + g * 0
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_capratio_126v504_slope_v116_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    ratio = _mean(capex, 126) / _mean(capex, 504).replace(0, np.nan).abs()
    base = ratio * closeadj + g * 0
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevratio_21v252_slope_v117_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = (_mean(c, 21) / _mean(c, 252).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevratio_63v252_slope_v118_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = (_mean(c, 63) / _mean(c, 252).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevratio_63v504_slope_v119_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = (_mean(c, 63) / _mean(c, 504).replace(0, np.nan)) * closeadj
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_caplog_252d_slope_v120_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = np.log(_mean(capex, 252).replace(0, np.nan).abs()) * closeadj / 10 + g * 0
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crevlog_252d_slope_v121_signal(capex, revenue, closeadj):
    c = _f08_capex_to_revenue(capex, revenue)
    base = np.log(_mean(c, 252).replace(0, np.nan).abs()) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintcum_63d_slope_v122_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 21)
    base = i.rolling(63, min_periods=21).sum() * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintcum_252d_slope_v123_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 21)
    base = i.rolling(252, min_periods=63).sum() * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintcum_504d_slope_v124_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 21)
    base = i.rolling(504, min_periods=126).sum() * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxrevgrow_63d_slope_v125_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    rg = revenue.pct_change(63)
    base = g * rg * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxrevgrow_252d_slope_v126_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    rg = revenue.pct_change(252)
    base = g * rg * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growminusrev_63d_slope_v127_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    rg = revenue.pct_change(63)
    base = (g - rg) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growminusrev_252d_slope_v128_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    rg = revenue.pct_change(252)
    base = (g - rg) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growoverrev_63d_slope_v129_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    rg = revenue.pct_change(63)
    base = (g / rg.replace(0, np.nan)) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_accel_21m63_slope_v130_signal(capex, closeadj):
    g21 = _f08_capex_growth(capex, 21)
    g63 = _f08_capex_growth(capex, 63)
    base = (g21 - g63) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_accel_63m252_slope_v131_signal(capex, closeadj):
    g63 = _f08_capex_growth(capex, 63)
    g252 = _f08_capex_growth(capex, 252)
    base = (g63 - g252) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_accel_252m504_slope_v132_signal(capex, closeadj):
    g252 = _f08_capex_growth(capex, 252)
    g504 = _f08_capex_growth(capex, 504)
    base = (g252 - g504) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintnorm_63d_slope_v133_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 63)
    c = _f08_capex_to_revenue(capex, revenue)
    base = (i / c.replace(0, np.nan).abs()) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iintnorm_252d_slope_v134_signal(capex, revenue, closeadj):
    i = _f08_capex_intensity_change(capex, revenue, 252)
    c = _f08_capex_to_revenue(capex, revenue)
    base = (i / c.replace(0, np.nan).abs()) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_overinv_63d_slope_v135_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    c = _f08_capex_to_revenue(capex, revenue)
    z = _z(c, 252)
    base = g * z * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_overinv_252d_slope_v136_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 252)
    c = _f08_capex_to_revenue(capex, revenue)
    z = _z(c, 504)
    base = g * z * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_composite_252d_slope_v137_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 63)
    i = _f08_capex_intensity_change(capex, revenue, 63)
    base = (g + i) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_composite_504d_slope_v138_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 126)
    i = _f08_capex_intensity_change(capex, revenue, 252)
    base = (g + i) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_caplevel_252d_slope_v139_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = capex / capex.rolling(252, min_periods=63).median().replace(0, np.nan).abs()
    base = base * closeadj + g * 0
    return _slope_pct(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_caplevel_504d_slope_v140_signal(capex, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = capex / capex.rolling(504, min_periods=126).median().replace(0, np.nan).abs()
    base = base * closeadj + g * 0
    return _slope_pct(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_5d_21slope_v141_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 5) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_5d_21slope_v142_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 5) * closeadj
    return _slope_pct(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_5d_slope_v143_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 5) * closeadj
    return _slope_diff_norm(base, 5).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_42d_slope_v144_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 42) * closeadj
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_189d_slope_v145_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 189) * closeadj
    return _slope_diff_norm(base, 63).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_378d_slope_v146_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 378) * closeadj
    return _slope_diff_norm(base, 126).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_growxrev_21d_slope_v147_signal(capex, revenue, closeadj):
    g = _f08_capex_growth(capex, 21)
    base = g * revenue * closeadj / 1e9
    return _slope_diff_norm(base, 21).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_grow_252d_long_slope_v148_signal(capex, closeadj):
    base = _f08_capex_growth(capex, 252) * closeadj
    return _slope_diff_norm(base, 252).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_crev_504d_long_slope_v149_signal(capex, revenue, closeadj):
    base = _mean(_f08_capex_to_revenue(capex, revenue), 504) * closeadj
    return _slope_pct(base, 252).replace([np.inf, -np.inf], np.nan)


def f08cap_f08_capex_acceleration_iint_504d_long_slope_v150_signal(capex, revenue, closeadj):
    base = _f08_capex_intensity_change(capex, revenue, 504) * closeadj
    return _slope_diff_norm(base, 252).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08cap_f08_capex_acceleration_grow_21d_slope_v001_signal,
    f08cap_f08_capex_acceleration_grow_21d_slope_v002_signal,
    f08cap_f08_capex_acceleration_grow_63d_slope_v003_signal,
    f08cap_f08_capex_acceleration_grow_63d_slope_v004_signal,
    f08cap_f08_capex_acceleration_grow_126d_slope_v005_signal,
    f08cap_f08_capex_acceleration_grow_126d_slope_v006_signal,
    f08cap_f08_capex_acceleration_grow_252d_slope_v007_signal,
    f08cap_f08_capex_acceleration_grow_252d_slope_v008_signal,
    f08cap_f08_capex_acceleration_grow_504d_slope_v009_signal,
    f08cap_f08_capex_acceleration_grow_504d_slope_v010_signal,
    f08cap_f08_capex_acceleration_crev_21d_slope_v011_signal,
    f08cap_f08_capex_acceleration_crev_21d_slope_v012_signal,
    f08cap_f08_capex_acceleration_crev_63d_slope_v013_signal,
    f08cap_f08_capex_acceleration_crev_63d_slope_v014_signal,
    f08cap_f08_capex_acceleration_crev_126d_slope_v015_signal,
    f08cap_f08_capex_acceleration_crev_126d_slope_v016_signal,
    f08cap_f08_capex_acceleration_crev_252d_slope_v017_signal,
    f08cap_f08_capex_acceleration_crev_252d_slope_v018_signal,
    f08cap_f08_capex_acceleration_crev_504d_slope_v019_signal,
    f08cap_f08_capex_acceleration_crev_504d_slope_v020_signal,
    f08cap_f08_capex_acceleration_iint_21d_slope_v021_signal,
    f08cap_f08_capex_acceleration_iint_21d_slope_v022_signal,
    f08cap_f08_capex_acceleration_iint_63d_slope_v023_signal,
    f08cap_f08_capex_acceleration_iint_126d_slope_v024_signal,
    f08cap_f08_capex_acceleration_iint_252d_slope_v025_signal,
    f08cap_f08_capex_acceleration_iint_252d_slope_v026_signal,
    f08cap_f08_capex_acceleration_iint_504d_slope_v027_signal,
    f08cap_f08_capex_acceleration_iint_504d_slope_v028_signal,
    f08cap_f08_capex_acceleration_growstd_21d_slope_v029_signal,
    f08cap_f08_capex_acceleration_growstd_63d_slope_v030_signal,
    f08cap_f08_capex_acceleration_growstd_252d_slope_v031_signal,
    f08cap_f08_capex_acceleration_growstd_504d_slope_v032_signal,
    f08cap_f08_capex_acceleration_crevstd_21d_slope_v033_signal,
    f08cap_f08_capex_acceleration_crevstd_63d_slope_v034_signal,
    f08cap_f08_capex_acceleration_crevstd_252d_slope_v035_signal,
    f08cap_f08_capex_acceleration_crevstd_504d_slope_v036_signal,
    f08cap_f08_capex_acceleration_growz_21d_slope_v037_signal,
    f08cap_f08_capex_acceleration_growz_63d_slope_v038_signal,
    f08cap_f08_capex_acceleration_growz_252d_slope_v039_signal,
    f08cap_f08_capex_acceleration_growz_504d_slope_v040_signal,
    f08cap_f08_capex_acceleration_crevz_21d_slope_v041_signal,
    f08cap_f08_capex_acceleration_crevz_63d_slope_v042_signal,
    f08cap_f08_capex_acceleration_crevz_252d_slope_v043_signal,
    f08cap_f08_capex_acceleration_crevz_504d_slope_v044_signal,
    f08cap_f08_capex_acceleration_grow_5d_slope_v045_signal,
    f08cap_f08_capex_acceleration_grow_10d_slope_v046_signal,
    f08cap_f08_capex_acceleration_grow_42d_slope_v047_signal,
    f08cap_f08_capex_acceleration_grow_189d_slope_v048_signal,
    f08cap_f08_capex_acceleration_grow_378d_slope_v049_signal,
    f08cap_f08_capex_acceleration_crev_5d_slope_v050_signal,
    f08cap_f08_capex_acceleration_crev_10d_slope_v051_signal,
    f08cap_f08_capex_acceleration_crev_42d_slope_v052_signal,
    f08cap_f08_capex_acceleration_crev_189d_slope_v053_signal,
    f08cap_f08_capex_acceleration_crev_378d_slope_v054_signal,
    f08cap_f08_capex_acceleration_growema_21d_slope_v055_signal,
    f08cap_f08_capex_acceleration_growema_63d_slope_v056_signal,
    f08cap_f08_capex_acceleration_growema_252d_slope_v057_signal,
    f08cap_f08_capex_acceleration_crevema_21d_slope_v058_signal,
    f08cap_f08_capex_acceleration_crevema_63d_slope_v059_signal,
    f08cap_f08_capex_acceleration_crevema_252d_slope_v060_signal,
    f08cap_f08_capex_acceleration_crevgap_21v252_slope_v061_signal,
    f08cap_f08_capex_acceleration_crevgap_63v252_slope_v062_signal,
    f08cap_f08_capex_acceleration_crevgap_63v504_slope_v063_signal,
    f08cap_f08_capex_acceleration_crevgap_126v504_slope_v064_signal,
    f08cap_f08_capex_acceleration_growsq_63d_slope_v065_signal,
    f08cap_f08_capex_acceleration_growsq_252d_slope_v066_signal,
    f08cap_f08_capex_acceleration_crevsq_63d_slope_v067_signal,
    f08cap_f08_capex_acceleration_crevsq_252d_slope_v068_signal,
    f08cap_f08_capex_acceleration_growxcrev_21d_slope_v069_signal,
    f08cap_f08_capex_acceleration_growxcrev_63d_slope_v070_signal,
    f08cap_f08_capex_acceleration_growxcrev_252d_slope_v071_signal,
    f08cap_f08_capex_acceleration_iintema_63d_slope_v072_signal,
    f08cap_f08_capex_acceleration_iintema_252d_slope_v073_signal,
    f08cap_f08_capex_acceleration_growxrev_63d_slope_v074_signal,
    f08cap_f08_capex_acceleration_growxrev_252d_slope_v075_signal,
    f08cap_f08_capex_acceleration_iintxrev_63d_slope_v076_signal,
    f08cap_f08_capex_acceleration_iintxrev_252d_slope_v077_signal,
    f08cap_f08_capex_acceleration_crevxcret_63d_slope_v078_signal,
    f08cap_f08_capex_acceleration_crevxcret_252d_slope_v079_signal,
    f08cap_f08_capex_acceleration_growsign_63d_slope_v080_signal,
    f08cap_f08_capex_acceleration_growxprice_21d_slope_v081_signal,
    f08cap_f08_capex_acceleration_growxprice_63d_slope_v082_signal,
    f08cap_f08_capex_acceleration_growxprice_252d_slope_v083_signal,
    f08cap_f08_capex_acceleration_crevxprice_63d_slope_v084_signal,
    f08cap_f08_capex_acceleration_crevxprice_252d_slope_v085_signal,
    f08cap_f08_capex_acceleration_growabs_63d_slope_v086_signal,
    f08cap_f08_capex_acceleration_growabs_252d_slope_v087_signal,
    f08cap_f08_capex_acceleration_growsum_63d_slope_v088_signal,
    f08cap_f08_capex_acceleration_growsum_252d_slope_v089_signal,
    f08cap_f08_capex_acceleration_growmax_63d_slope_v090_signal,
    f08cap_f08_capex_acceleration_growmax_252d_slope_v091_signal,
    f08cap_f08_capex_acceleration_growmin_63d_slope_v092_signal,
    f08cap_f08_capex_acceleration_growmin_252d_slope_v093_signal,
    f08cap_f08_capex_acceleration_growrng_252d_slope_v094_signal,
    f08cap_f08_capex_acceleration_crevmax_252d_slope_v095_signal,
    f08cap_f08_capex_acceleration_crevmin_252d_slope_v096_signal,
    f08cap_f08_capex_acceleration_crevrng_252d_slope_v097_signal,
    f08cap_f08_capex_acceleration_crevpct_252d_slope_v098_signal,
    f08cap_f08_capex_acceleration_growpct_252d_slope_v099_signal,
    f08cap_f08_capex_acceleration_growpct_504d_slope_v100_signal,
    f08cap_f08_capex_acceleration_growxcret_63d_slope_v101_signal,
    f08cap_f08_capex_acceleration_growxcret_252d_slope_v102_signal,
    f08cap_f08_capex_acceleration_iintxcret_63d_slope_v103_signal,
    f08cap_f08_capex_acceleration_iintxcret_252d_slope_v104_signal,
    f08cap_f08_capex_acceleration_growsqrt_63d_slope_v105_signal,
    f08cap_f08_capex_acceleration_growsqrt_252d_slope_v106_signal,
    f08cap_f08_capex_acceleration_crevsqrt_63d_slope_v107_signal,
    f08cap_f08_capex_acceleration_crevsqrt_252d_slope_v108_signal,
    f08cap_f08_capex_acceleration_crevcv_63d_slope_v109_signal,
    f08cap_f08_capex_acceleration_crevcv_252d_slope_v110_signal,
    f08cap_f08_capex_acceleration_accelcount_63d_slope_v111_signal,
    f08cap_f08_capex_acceleration_accelcount_252d_slope_v112_signal,
    f08cap_f08_capex_acceleration_decelcount_252d_slope_v113_signal,
    f08cap_f08_capex_acceleration_decelcount_504d_slope_v114_signal,
    f08cap_f08_capex_acceleration_capratio_63v252_slope_v115_signal,
    f08cap_f08_capex_acceleration_capratio_126v504_slope_v116_signal,
    f08cap_f08_capex_acceleration_crevratio_21v252_slope_v117_signal,
    f08cap_f08_capex_acceleration_crevratio_63v252_slope_v118_signal,
    f08cap_f08_capex_acceleration_crevratio_63v504_slope_v119_signal,
    f08cap_f08_capex_acceleration_caplog_252d_slope_v120_signal,
    f08cap_f08_capex_acceleration_crevlog_252d_slope_v121_signal,
    f08cap_f08_capex_acceleration_iintcum_63d_slope_v122_signal,
    f08cap_f08_capex_acceleration_iintcum_252d_slope_v123_signal,
    f08cap_f08_capex_acceleration_iintcum_504d_slope_v124_signal,
    f08cap_f08_capex_acceleration_growxrevgrow_63d_slope_v125_signal,
    f08cap_f08_capex_acceleration_growxrevgrow_252d_slope_v126_signal,
    f08cap_f08_capex_acceleration_growminusrev_63d_slope_v127_signal,
    f08cap_f08_capex_acceleration_growminusrev_252d_slope_v128_signal,
    f08cap_f08_capex_acceleration_growoverrev_63d_slope_v129_signal,
    f08cap_f08_capex_acceleration_accel_21m63_slope_v130_signal,
    f08cap_f08_capex_acceleration_accel_63m252_slope_v131_signal,
    f08cap_f08_capex_acceleration_accel_252m504_slope_v132_signal,
    f08cap_f08_capex_acceleration_iintnorm_63d_slope_v133_signal,
    f08cap_f08_capex_acceleration_iintnorm_252d_slope_v134_signal,
    f08cap_f08_capex_acceleration_overinv_63d_slope_v135_signal,
    f08cap_f08_capex_acceleration_overinv_252d_slope_v136_signal,
    f08cap_f08_capex_acceleration_composite_252d_slope_v137_signal,
    f08cap_f08_capex_acceleration_composite_504d_slope_v138_signal,
    f08cap_f08_capex_acceleration_caplevel_252d_slope_v139_signal,
    f08cap_f08_capex_acceleration_caplevel_504d_slope_v140_signal,
    f08cap_f08_capex_acceleration_grow_5d_21slope_v141_signal,
    f08cap_f08_capex_acceleration_crev_5d_21slope_v142_signal,
    f08cap_f08_capex_acceleration_iint_5d_slope_v143_signal,
    f08cap_f08_capex_acceleration_iint_42d_slope_v144_signal,
    f08cap_f08_capex_acceleration_iint_189d_slope_v145_signal,
    f08cap_f08_capex_acceleration_iint_378d_slope_v146_signal,
    f08cap_f08_capex_acceleration_growxrev_21d_slope_v147_signal,
    f08cap_f08_capex_acceleration_grow_252d_long_slope_v148_signal,
    f08cap_f08_capex_acceleration_crev_504d_long_slope_v149_signal,
    f08cap_f08_capex_acceleration_iint_504d_long_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_CAPEX_ACCELERATION_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")

    cols = {"closeadj": closeadj, "capex": capex, "revenue": revenue}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_capex_growth", "_f08_capex_to_revenue", "_f08_capex_intensity_change")
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
    print(f"OK f08_capex_acceleration_2nd_derivatives_001_150_claude: {n_features} features pass")
