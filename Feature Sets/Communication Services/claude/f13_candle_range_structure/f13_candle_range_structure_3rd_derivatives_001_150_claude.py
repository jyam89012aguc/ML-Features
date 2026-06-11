import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== derivative operators (math 1st/2nd derivative via finite differences) =====
def _slope(s, w):
    # 1st discrete derivative: average per-step change over horizon w
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    # 2nd discrete derivative: change of slope over horizon w (curvature/acceleration)
    sl = (s - s.shift(w)) / float(w)
    return (sl - sl.shift(w)) / float(w)


# ===== candle / range-structure base primitives =====
def _f13_range(high, low):
    return (high - low)


def _f13_body_abs(open, close):
    return (close - open).abs()


def _f13_body_ratio(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - open).abs() / rng


def _f13_sbody_ratio(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - open) / rng


def _f13_upper_wick_ratio(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    top = pd.concat([open, close], axis=1).max(axis=1)
    return (high - top) / rng


def _f13_lower_wick_ratio(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    bot = pd.concat([open, close], axis=1).min(axis=1)
    return (bot - low) / rng


def _f13_close_in_range(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return (close - low) / rng


def _f13_range_pct(high, low, close):
    return (high - low) / close.replace(0, np.nan)


def _f13_clv(high, low, close):
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f13_truerange(high, low, close):
    pc = close.shift(1)
    a = (high - low)
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)



# jerk _jerk (roc=21) of base candle metric: bodyrng_sm21
def f13cr_f13_candle_range_structure_bodyrng_sm21_21d_jerk_v001_signal(open, high, low, close):
    base = _mean(_f13_body_ratio(open, high, low, close), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyrng_sm63
def f13cr_f13_candle_range_structure_bodyrng_sm63_21d_jerk_v002_signal(open, high, low, close):
    base = _mean(_f13_body_ratio(open, high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=10) of base candle metric: bodyrng_sm10
def f13cr_f13_candle_range_structure_bodyrng_sm10_10d_jerk_v003_signal(open, high, low, close):
    base = _mean(_f13_body_ratio(open, high, low, close), 10)
    d = _jerk(base, 10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyrng_z63
def f13cr_f13_candle_range_structure_bodyrng_z63_21d_jerk_v004_signal(open, high, low, close):
    base = _z(_f13_body_ratio(open, high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: sbodyrng_sm21
def f13cr_f13_candle_range_structure_sbodyrng_sm21_21d_jerk_v005_signal(open, high, low, close):
    base = _mean(_f13_sbody_ratio(open, high, low, close), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: sbodyrng_sm63
def f13cr_f13_candle_range_structure_sbodyrng_sm63_21d_jerk_v006_signal(open, high, low, close):
    base = _mean(_f13_sbody_ratio(open, high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=10) of base candle metric: sbodyrng_sm10
def f13cr_f13_candle_range_structure_sbodyrng_sm10_10d_jerk_v007_signal(open, high, low, close):
    base = _mean(_f13_sbody_ratio(open, high, low, close), 10)
    d = _jerk(base, 10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyrng_rank126
def f13cr_f13_candle_range_structure_bodyrng_rank126_21d_jerk_v008_signal(open, high, low, close):
    base = _rank(_mean(_f13_body_ratio(open, high, low, close), 21), 126)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodymag_sm21
def f13cr_f13_candle_range_structure_bodymag_sm21_21d_jerk_v009_signal(open, close):
    base = _mean((close - open).abs() / close.replace(0, np.nan), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodymag_sm63
def f13cr_f13_candle_range_structure_bodymag_sm63_21d_jerk_v010_signal(open, close):
    base = _mean((close - open).abs() / close.replace(0, np.nan), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: sbodymag_sm21
def f13cr_f13_candle_range_structure_sbodymag_sm21_21d_jerk_v011_signal(open, close):
    base = _mean((close - open) / close.replace(0, np.nan), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=10) of base candle metric: sbodymag_sm10
def f13cr_f13_candle_range_structure_sbodymag_sm10_10d_jerk_v012_signal(open, close):
    base = _mean((close - open) / close.replace(0, np.nan), 10)
    d = _jerk(base, 10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodymag_z126
def f13cr_f13_candle_range_structure_bodymag_z126_21d_jerk_v013_signal(open, close):
    base = _z((close - open).abs() / close.replace(0, np.nan), 126)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodysign_sm21
def f13cr_f13_candle_range_structure_bodysign_sm21_21d_jerk_v014_signal(open, close):
    base = _mean(np.sign(close - open), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodysign_sm63
def f13cr_f13_candle_range_structure_bodysign_sm63_21d_jerk_v015_signal(open, close):
    base = _mean(np.sign(close - open), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=5) of base candle metric: cir_sm5
def f13cr_f13_candle_range_structure_cir_sm5_5d_jerk_v016_signal(high, low, close):
    base = _mean(_f13_close_in_range(high, low, close), 5)
    d = _jerk(base, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_sm21
def f13cr_f13_candle_range_structure_cir_sm21_21d_jerk_v017_signal(high, low, close):
    base = _mean(_f13_close_in_range(high, low, close), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_sm63
def f13cr_f13_candle_range_structure_cir_sm63_21d_jerk_v018_signal(high, low, close):
    base = _mean(_f13_close_in_range(high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_z63
def f13cr_f13_candle_range_structure_cir_z63_21d_jerk_v019_signal(high, low, close):
    base = _z(_f13_close_in_range(high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_rank126
def f13cr_f13_candle_range_structure_cir_rank126_21d_jerk_v020_signal(high, low, close):
    base = _rank(_mean(_f13_close_in_range(high, low, close), 21), 126)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_edge_sm21
def f13cr_f13_candle_range_structure_cir_edge_sm21_21d_jerk_v021_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = _mean((cir - 0.5).abs() * 2.0, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: body_vol_corr63
def f13cr_f13_candle_range_structure_body_vol_corr63_21d_jerk_v022_signal(open, close, volume):
    bm = (close - open).abs() / close.replace(0, np.nan)
    cov = (bm * volume).rolling(63, min_periods=21).mean() - _mean(bm, 63) * _mean(volume, 63)
    base = cov / (_std(bm, 63) * _std(volume, 63)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: logrange_skew63
def f13cr_f13_candle_range_structure_logrange_skew63_21d_jerk_v023_signal(high, low):
    lr = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    base = lr.rolling(63, min_periods=21).skew()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: sbody_kurt63
def f13cr_f13_candle_range_structure_sbody_kurt63_21d_jerk_v024_signal(open, high, low, close):
    base = _f13_sbody_ratio(open, high, low, close).rolling(63, min_periods=21).kurt()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: uwick_sm21
def f13cr_f13_candle_range_structure_uwick_sm21_21d_jerk_v025_signal(open, high, low, close):
    base = _mean(_f13_upper_wick_ratio(open, high, low, close), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: uwick_sm63
def f13cr_f13_candle_range_structure_uwick_sm63_21d_jerk_v026_signal(open, high, low, close):
    base = _mean(_f13_upper_wick_ratio(open, high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: lwick_sm21
def f13cr_f13_candle_range_structure_lwick_sm21_21d_jerk_v027_signal(open, high, low, close):
    base = _mean(_f13_lower_wick_ratio(open, high, low, close), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: lwick_sm63
def f13cr_f13_candle_range_structure_lwick_sm63_21d_jerk_v028_signal(open, high, low, close):
    base = _mean(_f13_lower_wick_ratio(open, high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wickskew_sm21
def f13cr_f13_candle_range_structure_wickskew_sm21_21d_jerk_v029_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = _mean(lw - uw, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wickskew_sm63
def f13cr_f13_candle_range_structure_wickskew_sm63_21d_jerk_v030_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = _mean(lw - uw, 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wickasym_sm21
def f13cr_f13_candle_range_structure_wickasym_sm21_21d_jerk_v031_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = _mean((uw - lw).abs(), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wickprod_sm21
def f13cr_f13_candle_range_structure_wickprod_sm21_21d_jerk_v032_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = _mean(uw * lw, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: uwick_z63
def f13cr_f13_candle_range_structure_uwick_z63_21d_jerk_v033_signal(open, high, low, close):
    base = _z(_f13_upper_wick_ratio(open, high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: lwick_z63
def f13cr_f13_candle_range_structure_lwick_z63_21d_jerk_v034_signal(open, high, low, close):
    base = _z(_f13_lower_wick_ratio(open, high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpct_sm21
def f13cr_f13_candle_range_structure_rngpct_sm21_21d_jerk_v035_signal(high, low, close):
    base = _mean(_f13_range_pct(high, low, close), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpct_sm63
def f13cr_f13_candle_range_structure_rngpct_sm63_21d_jerk_v036_signal(high, low, close):
    base = _mean(_f13_range_pct(high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=10) of base candle metric: rngpct_sm10
def f13cr_f13_candle_range_structure_rngpct_sm10_10d_jerk_v037_signal(high, low, close):
    base = _mean(_f13_range_pct(high, low, close), 10)
    d = _jerk(base, 10)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpct_z63
def f13cr_f13_candle_range_structure_rngpct_z63_21d_jerk_v038_signal(high, low, close):
    base = _z(_f13_range_pct(high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpct_rank126
def f13cr_f13_candle_range_structure_rngpct_rank126_21d_jerk_v039_signal(high, low, close):
    base = _rank(_mean(_f13_range_pct(high, low, close), 21), 126)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngexp_5v21
def f13cr_f13_candle_range_structure_rngexp_5v21_21d_jerk_v040_signal(high, low):
    rng = _f13_range(high, low)
    base = _mean(rng, 5) / _mean(rng, 21).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngexp_10v63
def f13cr_f13_candle_range_structure_rngexp_10v63_21d_jerk_v041_signal(high, low):
    rng = _f13_range(high, low)
    base = _mean(rng, 10) / _mean(rng, 63).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: trgap_sm21
def f13cr_f13_candle_range_structure_trgap_sm21_21d_jerk_v042_signal(high, low, close):
    tr = _f13_truerange(high, low, close)
    rng = _f13_range(high, low)
    base = _mean((tr - rng) / close.replace(0, np.nan), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: trgap_sm63
def f13cr_f13_candle_range_structure_trgap_sm63_21d_jerk_v043_signal(high, low, close):
    tr = _f13_truerange(high, low, close)
    rng = _f13_range(high, low)
    base = _mean((tr - rng) / close.replace(0, np.nan), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngvol_sm21
def f13cr_f13_candle_range_structure_rngvol_sm21_21d_jerk_v044_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    base = _std(rp, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngvol_sm63
def f13cr_f13_candle_range_structure_rngvol_sm63_21d_jerk_v045_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    base = _std(rp, 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngcov_63
def f13cr_f13_candle_range_structure_rngcov_63_21d_jerk_v046_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    base = _std(rp, 63) / _mean(rp, 63).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngvbody_sm21
def f13cr_f13_candle_range_structure_rngvbody_sm21_21d_jerk_v047_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close).replace(0, np.nan)
    base = _mean((rng / body).clip(upper=50), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodytr_gap21
def f13cr_f13_candle_range_structure_bodytr_gap21_21d_jerk_v048_signal(open, high, low, close):
    body = _f13_body_abs(open, close)
    tr = _f13_truerange(high, low, close).replace(0, np.nan)
    rng = _f13_range(high, low).replace(0, np.nan)
    base = _mean(body / tr - body / rng, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: brskew_sm21
def f13cr_f13_candle_range_structure_brskew_sm21_21d_jerk_v049_signal(open, high, low, close):
    base = _f13_body_ratio(open, high, low, close).rolling(21, min_periods=10).skew()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: brentropy_sm21
def f13cr_f13_candle_range_structure_brentropy_sm21_21d_jerk_v050_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close).clip(0, 1)
    base = _mean(br * (1.0 - br), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: climax_sm21
def f13cr_f13_candle_range_structure_climax_sm21_21d_jerk_v051_signal(high, low, volume):
    rngz = _z(_f13_range(high, low), 63)
    volz = _z(volume, 63)
    base = _mean(rngz.clip(lower=0) * volz.clip(lower=0), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngvolconf_sm21
def f13cr_f13_candle_range_structure_rngvolconf_sm21_21d_jerk_v052_signal(high, low, volume):
    rngz = _z(_f13_range(high, low), 63)
    volz = _z(volume, 63)
    base = _mean(rngz * volz, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: effort_sm21
def f13cr_f13_candle_range_structure_effort_sm21_21d_jerk_v053_signal(high, low, close, volume):
    rp = _f13_range_pct(high, low, close).replace(0, np.nan)
    base = _z(volume / rp, 63).rolling(21, min_periods=5).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: vwcir_sm21
def f13cr_f13_candle_range_structure_vwcir_sm21_21d_jerk_v054_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    num = (cir * volume).rolling(21, min_periods=5).sum()
    den = volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    base = num / den - 0.5
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: vwclv_sm63
def f13cr_f13_candle_range_structure_vwclv_sm63_21d_jerk_v055_signal(high, low, close, volume):
    clv = _f13_clv(high, low, close)
    num = (clv * volume).rolling(63, min_periods=21).sum()
    den = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = num / den
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: dirrng_sm63
def f13cr_f13_candle_range_structure_dirrng_sm63_21d_jerk_v056_signal(open, high, low, close):
    rngz = _z(_f13_range(high, low), 126)
    base = _mean(np.sign(close - open) * rngz, 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngdirskew_sm21
def f13cr_f13_candle_range_structure_rngdirskew_sm21_21d_jerk_v057_signal(open, high, low, close):
    rngz = _z(_f13_range(high, low), 63)
    base = _mean(np.sign(close - open) * rngz, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: hlc_pos_disp21
def f13cr_f13_candle_range_structure_hlc_pos_disp21_21d_jerk_v058_signal(high, low, close):
    typ = (high + low + close) / 3.0
    rng = (high - low).replace(0, np.nan)
    base = _std((close - typ) / rng, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: excbal_sm63
def f13cr_f13_candle_range_structure_excbal_sm63_21d_jerk_v059_signal(open, high, low):
    rng = (high - low).replace(0, np.nan)
    base = _mean(((high - open) - (open - low)) / rng, 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: openinrng_sm21
def f13cr_f13_candle_range_structure_openinrng_sm21_21d_jerk_v060_signal(open, high, low):
    rng = (high - low).replace(0, np.nan)
    base = _mean((open - low) / rng, 21) - 0.5
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngoverlap_sm21
def f13cr_f13_candle_range_structure_rngoverlap_sm21_21d_jerk_v061_signal(high, low):
    ov = (pd.concat([high, high.shift(1)], axis=1).min(axis=1) - pd.concat([low, low.shift(1)], axis=1).max(axis=1)).clip(lower=0)
    rng = (high - low).replace(0, np.nan)
    base = _mean(ov / rng, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyoverlap_sm21
def f13cr_f13_candle_range_structure_bodyoverlap_sm21_21d_jerk_v062_signal(open, close):
    lo = pd.concat([open, close], axis=1).min(axis=1)
    hi = pd.concat([open, close], axis=1).max(axis=1)
    ov = (pd.concat([hi, hi.shift(1)], axis=1).min(axis=1) - pd.concat([lo, lo.shift(1)], axis=1).max(axis=1)).clip(lower=0)
    rng = (hi - lo).replace(0, np.nan)
    base = _mean(ov / rng, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: gapinbar_sm21
def f13cr_f13_candle_range_structure_gapinbar_sm21_21d_jerk_v063_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    base = _mean((open - close.shift(1)).abs() / rng, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: opendrive_sm21
def f13cr_f13_candle_range_structure_opendrive_sm21_21d_jerk_v064_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    base = _mean((open - close.shift(1)) / rng, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: overnight_sm21
def f13cr_f13_candle_range_structure_overnight_sm21_21d_jerk_v065_signal(open, high, low, close):
    onr = (open - close.shift(1)) / close.shift(1).replace(0, np.nan)
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    base = _std(onr, 21) / (_std(onr, 21) + _std(rng, 21)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngclust_63
def f13cr_f13_candle_range_structure_rngclust_63_21d_jerk_v066_signal(high, low):
    rng = _f13_range(high, low)
    lag = rng.shift(1)
    cov = (rng * lag).rolling(63, min_periods=21).mean() - _mean(rng, 63) * _mean(lag, 63)
    base = cov / (_std(rng, 63) * _std(lag, 63)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cirautocorr_63
def f13cr_f13_candle_range_structure_cirautocorr_63_21d_jerk_v067_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    lag = cir.shift(1)
    cov = (cir * lag).rolling(63, min_periods=21).mean() - _mean(cir, 63) * _mean(lag, 63)
    base = cov / (_std(cir, 63) * _std(lag, 63)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: edgeclose_sm63
def f13cr_f13_candle_range_structure_edgeclose_sm63_21d_jerk_v068_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = _mean((cir - 0.5).abs() * 2.0, 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: closetoext_disp21
def f13cr_f13_candle_range_structure_closetoext_disp21_21d_jerk_v069_signal(high, low, close):
    to_hi = (high - close)
    to_lo = (close - low)
    rng = (high - low).replace(0, np.nan)
    nearest = pd.concat([to_hi, to_lo], axis=1).min(axis=1) / rng
    base = _std(nearest, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: clvquality_sm21
def f13cr_f13_candle_range_structure_clvquality_sm21_21d_jerk_v070_signal(open, high, low, close):
    clv = _f13_clv(high, low, close)
    br = _f13_body_ratio(open, high, low, close)
    base = _mean(clv * br, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: lowrecov_sm21
def f13cr_f13_candle_range_structure_lowrecov_sm21_21d_jerk_v071_signal(open, high, low, close):
    dn = (open > close).astype(float)
    rng = (high - low).replace(0, np.nan)
    rec = (close - low) / rng
    base = (rec * dn).rolling(21, min_periods=5).sum() / dn.rolling(21, min_periods=5).sum().replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: shapeentropy_sm21
def f13cr_f13_candle_range_structure_shapeentropy_sm21_21d_jerk_v072_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = _mean(pd.concat([br, uw, lw], axis=1).std(axis=1), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyrng_ema42
def f13cr_f13_candle_range_structure_bodyrng_ema42_21d_jerk_v073_signal(open, high, low, close):
    base = _f13_body_ratio(open, high, low, close).ewm(span=42, min_periods=21).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyrng_med63
def f13cr_f13_candle_range_structure_bodyrng_med63_21d_jerk_v074_signal(open, high, low, close):
    base = _f13_body_ratio(open, high, low, close).rolling(63, min_periods=21).median()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyrng_kurt63
def f13cr_f13_candle_range_structure_bodyrng_kurt63_21d_jerk_v075_signal(open, high, low, close):
    base = _f13_body_ratio(open, high, low, close).rolling(63, min_periods=21).kurt()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyrng_disp63
def f13cr_f13_candle_range_structure_bodyrng_disp63_21d_jerk_v076_signal(open, high, low, close):
    base = _std(_f13_body_ratio(open, high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: sbodyrng_ema21
def f13cr_f13_candle_range_structure_sbodyrng_ema21_21d_jerk_v077_signal(open, high, low, close):
    base = _f13_sbody_ratio(open, high, low, close).ewm(span=21, min_periods=10).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: sbodyrng_med21
def f13cr_f13_candle_range_structure_sbodyrng_med21_21d_jerk_v078_signal(open, high, low, close):
    base = _f13_sbody_ratio(open, high, low, close).rolling(21, min_periods=10).median()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyrun_sm
def f13cr_f13_candle_range_structure_bodyrun_sm_21d_jerk_v079_signal(open, close):
    sgn = np.sign(close - open)
    grp = (sgn != sgn.shift(1)).cumsum()
    rl = sgn.groupby(grp).cumcount() + 1
    base = _mean(sgn * rl.clip(upper=12) / 12.0, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodyskew_63
def f13cr_f13_candle_range_structure_bodyskew_63_21d_jerk_v080_signal(open, high, low, close):
    sbr = _f13_sbody_ratio(open, high, low, close)
    base = sbr.rolling(63, min_periods=21).skew()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_ema21
def f13cr_f13_candle_range_structure_cir_ema21_21d_jerk_v081_signal(high, low, close):
    base = _f13_close_in_range(high, low, close).ewm(span=21, min_periods=10).mean() - 0.5
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_med63
def f13cr_f13_candle_range_structure_cir_med63_21d_jerk_v082_signal(high, low, close):
    base = _f13_close_in_range(high, low, close).rolling(63, min_periods=21).median() - 0.5
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_skew63
def f13cr_f13_candle_range_structure_cir_skew63_21d_jerk_v083_signal(high, low, close):
    base = _f13_close_in_range(high, low, close).rolling(63, min_periods=21).skew()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_disp63
def f13cr_f13_candle_range_structure_cir_disp63_21d_jerk_v084_signal(high, low, close):
    base = _std(_f13_close_in_range(high, low, close), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir_diffvol
def f13cr_f13_candle_range_structure_cir_diffvol_21d_jerk_v085_signal(high, low, close):
    base = _std(_f13_close_in_range(high, low, close).diff(), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: clvvol_ema42
def f13cr_f13_candle_range_structure_clvvol_ema42_21d_jerk_v086_signal(high, low, close, volume):
    clv = _f13_clv(high, low, close)
    w = clv * volume
    base = w.ewm(span=42, min_periods=21).mean() / volume.ewm(span=42, min_periods=21).mean().replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: clv_kurt63
def f13cr_f13_candle_range_structure_clv_kurt63_21d_jerk_v087_signal(high, low, close):
    base = _f13_clv(high, low, close).rolling(63, min_periods=21).kurt()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: uwick_ema21
def f13cr_f13_candle_range_structure_uwick_ema21_21d_jerk_v088_signal(open, high, low, close):
    base = _f13_upper_wick_ratio(open, high, low, close).ewm(span=21, min_periods=10).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: lwick_ema21
def f13cr_f13_candle_range_structure_lwick_ema21_21d_jerk_v089_signal(open, high, low, close):
    base = _f13_lower_wick_ratio(open, high, low, close).ewm(span=21, min_periods=10).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wickskew_vol42
def f13cr_f13_candle_range_structure_wickskew_vol42_21d_jerk_v090_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = _std(lw - uw, 42)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wickskew_rank126
def f13cr_f13_candle_range_structure_wickskew_rank126_21d_jerk_v091_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = _rank(_mean(lw - uw, 21), 126)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: uwick_at_highs21
def f13cr_f13_candle_range_structure_uwick_at_highs21_21d_jerk_v092_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    at_hi = (close > _rmax(close, 10).shift(1)).astype(float)
    num = (uw * at_hi).rolling(63, min_periods=21).sum()
    den = at_hi.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = num / den
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: uwick_med63
def f13cr_f13_candle_range_structure_uwick_med63_21d_jerk_v093_signal(open, high, low, close):
    base = _f13_upper_wick_ratio(open, high, low, close).rolling(63, min_periods=21).median()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: lwick_med63
def f13cr_f13_candle_range_structure_lwick_med63_21d_jerk_v094_signal(open, high, low, close):
    base = _f13_lower_wick_ratio(open, high, low, close).rolling(63, min_periods=21).median()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpct_ema42
def f13cr_f13_candle_range_structure_rngpct_ema42_21d_jerk_v095_signal(high, low, close):
    base = _f13_range_pct(high, low, close).ewm(span=42, min_periods=21).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpct_med63
def f13cr_f13_candle_range_structure_rngpct_med63_21d_jerk_v096_signal(high, low, close):
    base = _f13_range_pct(high, low, close).rolling(63, min_periods=21).median()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpct_skew63
def f13cr_f13_candle_range_structure_rngpct_skew63_21d_jerk_v097_signal(high, low, close):
    base = _f13_range_pct(high, low, close).rolling(63, min_periods=21).skew()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpct_kurt63
def f13cr_f13_candle_range_structure_rngpct_kurt63_21d_jerk_v098_signal(high, low, close):
    base = _f13_range_pct(high, low, close).rolling(63, min_periods=21).kurt()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rng_log_sm21
def f13cr_f13_candle_range_structure_rng_log_sm21_21d_jerk_v099_signal(high, low, close):
    base = _mean(np.log(_f13_range_pct(high, low, close).replace(0, np.nan)), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngexp_ema
def f13cr_f13_candle_range_structure_rngexp_ema_21d_jerk_v100_signal(high, low):
    rng = _f13_range(high, low)
    base = rng.ewm(span=10, min_periods=5).mean() / rng.ewm(span=63, min_periods=21).mean().replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rng_upsemi63
def f13cr_f13_candle_range_structure_rng_upsemi63_21d_jerk_v101_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    med = rp.rolling(126, min_periods=63).median()
    base = _std((rp - med).clip(lower=0), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rng_dnsemi63
def f13cr_f13_candle_range_structure_rng_dnsemi63_21d_jerk_v102_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    med = rp.rolling(126, min_periods=63).median()
    base = _std((med - rp).clip(lower=0), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: gap_to_tr_21
def f13cr_f13_candle_range_structure_gap_to_tr_21_21d_jerk_v103_signal(open, high, low, close):
    tr = _f13_truerange(high, low, close).replace(0, np.nan)
    g = (open - close.shift(1)).abs()
    base = _mean(g / tr, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngvbody_ema21
def f13cr_f13_candle_range_structure_rngvbody_ema21_21d_jerk_v104_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close).replace(0, np.nan)
    base = (rng / body).clip(upper=50).ewm(span=21, min_periods=10).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodytr_ema21
def f13cr_f13_candle_range_structure_bodytr_ema21_21d_jerk_v105_signal(open, high, low, close):
    body = _f13_body_abs(open, close)
    tr = _f13_truerange(high, low, close).replace(0, np.nan)
    base = (body / tr).ewm(span=21, min_periods=10).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: body_range_corr63
def f13cr_f13_candle_range_structure_body_range_corr63_21d_jerk_v106_signal(open, high, low, close):
    body = _f13_body_abs(open, close)
    rng = _f13_range(high, low)
    cov = (body * rng).rolling(63, min_periods=21).mean() - _mean(body, 63) * _mean(rng, 63)
    base = cov / (_std(body, 63) * _std(rng, 63)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: climaxup_sm21
def f13cr_f13_candle_range_structure_climaxup_sm21_21d_jerk_v107_signal(high, low, close, volume):
    rngz = _z(_f13_range(high, low), 63).clip(lower=0)
    cir = (_f13_close_in_range(high, low, close) - 0.5).clip(lower=0)
    volz = _z(volume, 63).clip(lower=0)
    base = _mean(rngz * cir * volz, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: climaxdn_sm21
def f13cr_f13_candle_range_structure_climaxdn_sm21_21d_jerk_v108_signal(high, low, close, volume):
    rngz = _z(_f13_range(high, low), 63).clip(lower=0)
    cir = (0.5 - _f13_close_in_range(high, low, close)).clip(lower=0)
    volz = _z(volume, 63).clip(lower=0)
    base = _mean(rngz * cir * volz, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: capit_sm21
def f13cr_f13_candle_range_structure_capit_sm21_21d_jerk_v109_signal(open, high, low, close, volume):
    down = (close < open).astype(float)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    volz = _z(volume, 63).clip(lower=0)
    base = _mean(down * lw * volz, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngvolcorr_63
def f13cr_f13_candle_range_structure_rngvolcorr_63_21d_jerk_v110_signal(high, low, volume):
    rng = _f13_range(high, low)
    cov = (rng * volume).rolling(63, min_periods=21).mean() - _mean(rng, 63) * _mean(volume, 63)
    base = cov / (_std(rng, 63) * _std(volume, 63)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cirvolcorr_63
def f13cr_f13_candle_range_structure_cirvolcorr_63_21d_jerk_v111_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    cov = (cir * volume).rolling(63, min_periods=21).mean() - _mean(cir, 63) * _mean(volume, 63)
    base = cov / (_std(cir, 63) * _std(volume, 63)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: vwbodyrng_sm21
def f13cr_f13_candle_range_structure_vwbodyrng_sm21_21d_jerk_v112_signal(open, high, low, close, volume):
    br = _f13_body_ratio(open, high, low, close)
    num = (br * volume).rolling(21, min_periods=5).sum()
    den = volume.rolling(21, min_periods=5).sum().replace(0, np.nan)
    base = num / den
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: range_per_vol_63
def f13cr_f13_candle_range_structure_range_per_vol_63_21d_jerk_v113_signal(high, low, close, volume):
    rp = _f13_range_pct(high, low, close)
    amih = rp / volume.replace(0, np.nan)
    base = _z(amih, 126).rolling(63, min_periods=21).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: widebias_63
def f13cr_f13_candle_range_structure_widebias_63_21d_jerk_v114_signal(high, low, close):
    clv = _f13_clv(high, low, close)
    rngz = _z(_f13_range(high, low), 63)
    wide = (rngz > 1.0).astype(float)
    num = (clv * wide).rolling(63, min_periods=21).sum()
    den = wide.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = num / den
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wideasym_63
def f13cr_f13_candle_range_structure_wideasym_63_21d_jerk_v115_signal(open, high, low, close):
    rngz = _z(_f13_range(high, low), 63)
    up = ((close > open) & (rngz > 1.0)).astype(float)
    dn = ((close < open) & (rngz > 1.0)).astype(float)
    base = _mean(up - dn, 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: dirrng_signmag
def f13cr_f13_candle_range_structure_dirrng_signmag_21d_jerk_v116_signal(open, high, low, close):
    rngz = _z(_f13_range(high, low), 126)
    sbr = _f13_sbody_ratio(open, high, low, close)
    base = _mean(sbr * rngz.abs(), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: typdrift_3bar
def f13cr_f13_candle_range_structure_typdrift_3bar_21d_jerk_v117_signal(high, low, close):
    typ = (high + low + close) / 3.0
    center = typ.rolling(3, min_periods=2).mean()
    rng = _f13_range(high, low).rolling(3, min_periods=2).mean().replace(0, np.nan)
    base = _mean((close - center) / rng, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: excbal_ema63
def f13cr_f13_candle_range_structure_excbal_ema63_21d_jerk_v118_signal(open, high, low):
    rng = (high - low).replace(0, np.nan)
    base = (((high - open) - (open - low)) / rng).ewm(span=63, min_periods=21).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: openpos_med21
def f13cr_f13_candle_range_structure_openpos_med21_21d_jerk_v119_signal(open, high, low):
    rng = (high - low).replace(0, np.nan)
    base = ((open - low) / rng).rolling(21, min_periods=10).median() - 0.5
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: gapinbar_med63
def f13cr_f13_candle_range_structure_gapinbar_med63_21d_jerk_v120_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    base = ((open - close.shift(1)).abs() / rng).rolling(63, min_periods=21).median()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: opendrive_ema21
def f13cr_f13_candle_range_structure_opendrive_ema21_21d_jerk_v121_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    base = ((open - close.shift(1)) / rng).ewm(span=21, min_periods=10).mean()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: gapup_sm21
def f13cr_f13_candle_range_structure_gapup_sm21_21d_jerk_v122_signal(open, high):
    base = _mean(((open - high.shift(1)) / high.shift(1).replace(0, np.nan)).clip(lower=0), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: gapdn_sm21
def f13cr_f13_candle_range_structure_gapdn_sm21_21d_jerk_v123_signal(open, low):
    base = _mean(((low.shift(1) - open) / low.shift(1).replace(0, np.nan)).clip(lower=0), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: overnight_share63
def f13cr_f13_candle_range_structure_overnight_share63_21d_jerk_v124_signal(open, high, low, close):
    onr = (open - close.shift(1)) / close.shift(1).replace(0, np.nan)
    rng = _f13_range(high, low) / close.replace(0, np.nan)
    base = _std(onr, 63) / (_std(onr, 63) + _std(rng, 63)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngvarratio_63
def f13cr_f13_candle_range_structure_rngvarratio_63_21d_jerk_v125_signal(high, low):
    rng = _f13_range(high, low)
    v1 = _std(rng, 21) ** 2
    v5 = _std(rng.rolling(5, min_periods=3).mean(), 21) ** 2 * 5.0
    base = v5 / v1.replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngburst_21
def f13cr_f13_candle_range_structure_rngburst_21_21d_jerk_v126_signal(high, low):
    rngz = _z(_f13_range(high, low), 63)
    base = _std(rngz, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngshock_21
def f13cr_f13_candle_range_structure_rngshock_21_21d_jerk_v127_signal(high, low, close):
    rp = _f13_range_pct(high, low, close)
    base = _rmax(rp, 21) / rp.rolling(63, min_periods=21).median().replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rejhi_63
def f13cr_f13_candle_range_structure_rejhi_63_21d_jerk_v128_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    at_hi = (high >= _rmax(high, 21)).astype(float)
    num = (uw * at_hi).rolling(63, min_periods=21).sum()
    den = at_hi.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = num / den
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: demlo_63
def f13cr_f13_candle_range_structure_demlo_63_21d_jerk_v129_signal(open, high, low, close):
    lw = _f13_lower_wick_ratio(open, high, low, close)
    at_lo = (low <= _rmin(low, 21)).astype(float)
    num = (lw * at_lo).rolling(63, min_periods=21).sum()
    den = at_lo.rolling(63, min_periods=21).sum().replace(0, np.nan)
    base = num / den
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: pinpress_sm21
def f13cr_f13_candle_range_structure_pinpress_sm21_21d_jerk_v130_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = _mean(pd.concat([uw, lw], axis=1).max(axis=1), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wickbal_at_lows21
def f13cr_f13_candle_range_structure_wickbal_at_lows21_21d_jerk_v131_signal(open, high, low, close):
    lw = _f13_lower_wick_ratio(open, high, low, close)
    at_lo = (low <= _rmin(low, 10)).astype(float)
    num = (lw * at_lo).rolling(42, min_periods=15).sum()
    den = at_lo.rolling(42, min_periods=15).sum().replace(0, np.nan)
    base = num / den
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: revbar_sm21
def f13cr_f13_candle_range_structure_revbar_sm21_21d_jerk_v132_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    pu = (close.shift(1) > open.shift(1)).astype(float)
    pd_ = (close.shift(1) < open.shift(1)).astype(float)
    base = _mean(pu * uw + pd_ * lw, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: trendday_sm21
def f13cr_f13_candle_range_structure_trendday_sm21_21d_jerk_v133_signal(open, high, low, close):
    rng = (high - low).replace(0, np.nan)
    drive = (close - open).abs() / rng
    cir = _f13_close_in_range(high, low, close)
    base = _mean(drive * (cir - 0.5).abs() * 2.0, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngpath_21
def f13cr_f13_candle_range_structure_rngpath_21_21d_jerk_v134_signal(high, low):
    rng = _f13_range(high, low)
    base = _mean(rng.diff().abs(), 21) / _mean(rng, 21).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: exhcombo_63
def f13cr_f13_candle_range_structure_exhcombo_63_21d_jerk_v135_signal(open, high, low, close, volume):
    rngz = _z(_f13_range(high, low), 126).clip(lower=0)
    uw = _f13_upper_wick_ratio(open, high, low, close)
    volz = _z(volume, 126).clip(lower=0)
    base = _mean(rngz * uw * volz, 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: exhaust_21
def f13cr_f13_candle_range_structure_exhaust_21_21d_jerk_v136_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    rngz = _z(_f13_range(high, low), 63)
    prev_wide = (rngz.shift(1) > 1.0).astype(float)
    base = _mean(prev_wide * (0.25 - br).clip(lower=0), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: rngbodydiv_21
def f13cr_f13_candle_range_structure_rngbodydiv_21_21d_jerk_v137_signal(open, high, low, close):
    rng = _f13_range(high, low)
    body = _f13_body_abs(open, close)
    rg = _mean(rng, 5) / _mean(rng, 21).replace(0, np.nan)
    bg = _mean(body, 5) / _mean(body, 21).replace(0, np.nan)
    base = rg - bg
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: squeeze_5v126
def f13cr_f13_candle_range_structure_squeeze_5v126_21d_jerk_v138_signal(high, low):
    rng = _f13_range(high, low)
    base = _mean(rng, 5) / _mean(rng, 126).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: garmanklass_21
def f13cr_f13_candle_range_structure_garmanklass_21_21d_jerk_v139_signal(open, high, low, close):
    hl = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    co = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    gk = 0.5 * hl ** 2 - (2 * np.log(2) - 1) * co ** 2
    base = np.sqrt(_mean(gk, 21).clip(lower=0))
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: cir3mom_21
def f13cr_f13_candle_range_structure_cir3mom_21_21d_jerk_v140_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = _mean(cir - cir.shift(3), 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: brcov_63
def f13cr_f13_candle_range_structure_brcov_63_21d_jerk_v141_signal(open, high, low, close):
    br = _f13_body_ratio(open, high, low, close)
    base = _std(br, 63) / _mean(br, 63).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: edge_med63
def f13cr_f13_candle_range_structure_edge_med63_21d_jerk_v142_signal(high, low, close):
    cir = _f13_close_in_range(high, low, close)
    base = ((cir - 0.5).abs() * 2.0).rolling(63, min_periods=21).median()
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wickwt_21
def f13cr_f13_candle_range_structure_wickwt_21_21d_jerk_v143_signal(open, high, low, close):
    uw = (high - pd.concat([open, close], axis=1).max(axis=1))
    lw = (pd.concat([open, close], axis=1).min(axis=1) - low)
    rng = _f13_range(high, low).replace(0, np.nan)
    base = _mean(lw - uw, 21) / _mean(rng, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: clv_wide_sm21
def f13cr_f13_candle_range_structure_clv_wide_sm21_21d_jerk_v144_signal(high, low, close):
    clv = _f13_clv(high, low, close)
    rngz = _z(_f13_range(high, low), 63)
    base = _mean(clv * rngz, 21)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: bodymag_rank126
def f13cr_f13_candle_range_structure_bodymag_rank126_21d_jerk_v145_signal(open, close):
    bm = (close - open).abs() / close.replace(0, np.nan)
    base = _rank(_mean(bm, 10), 126)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: strongvol_63
def f13cr_f13_candle_range_structure_strongvol_63_21d_jerk_v146_signal(high, low, close, volume):
    cir = _f13_close_in_range(high, low, close)
    vavg = _mean(volume, 63)
    base = _mean((cir > 0.6).astype(float) * (volume / vavg.replace(0, np.nan)), 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: uw_lw_cov63
def f13cr_f13_candle_range_structure_uw_lw_cov63_21d_jerk_v147_signal(open, high, low, close):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    lw = _f13_lower_wick_ratio(open, high, low, close)
    base = (uw * lw).rolling(63, min_periods=21).mean() - _mean(uw, 63) * _mean(lw, 63)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: parkinson_63
def f13cr_f13_candle_range_structure_parkinson_63_21d_jerk_v148_signal(high, low):
    lr = np.log(high.replace(0, np.nan) / low.replace(0, np.nan))
    base = np.sqrt((lr ** 2).rolling(63, min_periods=21).mean())
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: updnbody_asym63
def f13cr_f13_candle_range_structure_updnbody_asym63_21d_jerk_v149_signal(open, close):
    r = (close - open) / close.replace(0, np.nan)
    up = r.clip(lower=0)
    dn = (-r).clip(lower=0)
    base = _mean(up, 63) - _mean(dn, 63) - 0.5 * (_std(up, 63) - _std(dn, 63))
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# jerk _jerk (roc=21) of base candle metric: wick_vol_corr63
def f13cr_f13_candle_range_structure_wick_vol_corr63_21d_jerk_v150_signal(open, high, low, close, volume):
    uw = _f13_upper_wick_ratio(open, high, low, close)
    cov = (uw * volume).rolling(63, min_periods=21).mean() - _mean(uw, 63) * _mean(volume, 63)
    base = cov / (_std(uw, 63) * _std(volume, 63)).replace(0, np.nan)
    d = _jerk(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f13cr_f13_candle_range_structure_bodyrng_sm21_21d_jerk_v001_signal,
    f13cr_f13_candle_range_structure_bodyrng_sm63_21d_jerk_v002_signal,
    f13cr_f13_candle_range_structure_bodyrng_sm10_10d_jerk_v003_signal,
    f13cr_f13_candle_range_structure_bodyrng_z63_21d_jerk_v004_signal,
    f13cr_f13_candle_range_structure_sbodyrng_sm21_21d_jerk_v005_signal,
    f13cr_f13_candle_range_structure_sbodyrng_sm63_21d_jerk_v006_signal,
    f13cr_f13_candle_range_structure_sbodyrng_sm10_10d_jerk_v007_signal,
    f13cr_f13_candle_range_structure_bodyrng_rank126_21d_jerk_v008_signal,
    f13cr_f13_candle_range_structure_bodymag_sm21_21d_jerk_v009_signal,
    f13cr_f13_candle_range_structure_bodymag_sm63_21d_jerk_v010_signal,
    f13cr_f13_candle_range_structure_sbodymag_sm21_21d_jerk_v011_signal,
    f13cr_f13_candle_range_structure_sbodymag_sm10_10d_jerk_v012_signal,
    f13cr_f13_candle_range_structure_bodymag_z126_21d_jerk_v013_signal,
    f13cr_f13_candle_range_structure_bodysign_sm21_21d_jerk_v014_signal,
    f13cr_f13_candle_range_structure_bodysign_sm63_21d_jerk_v015_signal,
    f13cr_f13_candle_range_structure_cir_sm5_5d_jerk_v016_signal,
    f13cr_f13_candle_range_structure_cir_sm21_21d_jerk_v017_signal,
    f13cr_f13_candle_range_structure_cir_sm63_21d_jerk_v018_signal,
    f13cr_f13_candle_range_structure_cir_z63_21d_jerk_v019_signal,
    f13cr_f13_candle_range_structure_cir_rank126_21d_jerk_v020_signal,
    f13cr_f13_candle_range_structure_cir_edge_sm21_21d_jerk_v021_signal,
    f13cr_f13_candle_range_structure_body_vol_corr63_21d_jerk_v022_signal,
    f13cr_f13_candle_range_structure_logrange_skew63_21d_jerk_v023_signal,
    f13cr_f13_candle_range_structure_sbody_kurt63_21d_jerk_v024_signal,
    f13cr_f13_candle_range_structure_uwick_sm21_21d_jerk_v025_signal,
    f13cr_f13_candle_range_structure_uwick_sm63_21d_jerk_v026_signal,
    f13cr_f13_candle_range_structure_lwick_sm21_21d_jerk_v027_signal,
    f13cr_f13_candle_range_structure_lwick_sm63_21d_jerk_v028_signal,
    f13cr_f13_candle_range_structure_wickskew_sm21_21d_jerk_v029_signal,
    f13cr_f13_candle_range_structure_wickskew_sm63_21d_jerk_v030_signal,
    f13cr_f13_candle_range_structure_wickasym_sm21_21d_jerk_v031_signal,
    f13cr_f13_candle_range_structure_wickprod_sm21_21d_jerk_v032_signal,
    f13cr_f13_candle_range_structure_uwick_z63_21d_jerk_v033_signal,
    f13cr_f13_candle_range_structure_lwick_z63_21d_jerk_v034_signal,
    f13cr_f13_candle_range_structure_rngpct_sm21_21d_jerk_v035_signal,
    f13cr_f13_candle_range_structure_rngpct_sm63_21d_jerk_v036_signal,
    f13cr_f13_candle_range_structure_rngpct_sm10_10d_jerk_v037_signal,
    f13cr_f13_candle_range_structure_rngpct_z63_21d_jerk_v038_signal,
    f13cr_f13_candle_range_structure_rngpct_rank126_21d_jerk_v039_signal,
    f13cr_f13_candle_range_structure_rngexp_5v21_21d_jerk_v040_signal,
    f13cr_f13_candle_range_structure_rngexp_10v63_21d_jerk_v041_signal,
    f13cr_f13_candle_range_structure_trgap_sm21_21d_jerk_v042_signal,
    f13cr_f13_candle_range_structure_trgap_sm63_21d_jerk_v043_signal,
    f13cr_f13_candle_range_structure_rngvol_sm21_21d_jerk_v044_signal,
    f13cr_f13_candle_range_structure_rngvol_sm63_21d_jerk_v045_signal,
    f13cr_f13_candle_range_structure_rngcov_63_21d_jerk_v046_signal,
    f13cr_f13_candle_range_structure_rngvbody_sm21_21d_jerk_v047_signal,
    f13cr_f13_candle_range_structure_bodytr_gap21_21d_jerk_v048_signal,
    f13cr_f13_candle_range_structure_brskew_sm21_21d_jerk_v049_signal,
    f13cr_f13_candle_range_structure_brentropy_sm21_21d_jerk_v050_signal,
    f13cr_f13_candle_range_structure_climax_sm21_21d_jerk_v051_signal,
    f13cr_f13_candle_range_structure_rngvolconf_sm21_21d_jerk_v052_signal,
    f13cr_f13_candle_range_structure_effort_sm21_21d_jerk_v053_signal,
    f13cr_f13_candle_range_structure_vwcir_sm21_21d_jerk_v054_signal,
    f13cr_f13_candle_range_structure_vwclv_sm63_21d_jerk_v055_signal,
    f13cr_f13_candle_range_structure_dirrng_sm63_21d_jerk_v056_signal,
    f13cr_f13_candle_range_structure_rngdirskew_sm21_21d_jerk_v057_signal,
    f13cr_f13_candle_range_structure_hlc_pos_disp21_21d_jerk_v058_signal,
    f13cr_f13_candle_range_structure_excbal_sm63_21d_jerk_v059_signal,
    f13cr_f13_candle_range_structure_openinrng_sm21_21d_jerk_v060_signal,
    f13cr_f13_candle_range_structure_rngoverlap_sm21_21d_jerk_v061_signal,
    f13cr_f13_candle_range_structure_bodyoverlap_sm21_21d_jerk_v062_signal,
    f13cr_f13_candle_range_structure_gapinbar_sm21_21d_jerk_v063_signal,
    f13cr_f13_candle_range_structure_opendrive_sm21_21d_jerk_v064_signal,
    f13cr_f13_candle_range_structure_overnight_sm21_21d_jerk_v065_signal,
    f13cr_f13_candle_range_structure_rngclust_63_21d_jerk_v066_signal,
    f13cr_f13_candle_range_structure_cirautocorr_63_21d_jerk_v067_signal,
    f13cr_f13_candle_range_structure_edgeclose_sm63_21d_jerk_v068_signal,
    f13cr_f13_candle_range_structure_closetoext_disp21_21d_jerk_v069_signal,
    f13cr_f13_candle_range_structure_clvquality_sm21_21d_jerk_v070_signal,
    f13cr_f13_candle_range_structure_lowrecov_sm21_21d_jerk_v071_signal,
    f13cr_f13_candle_range_structure_shapeentropy_sm21_21d_jerk_v072_signal,
    f13cr_f13_candle_range_structure_bodyrng_ema42_21d_jerk_v073_signal,
    f13cr_f13_candle_range_structure_bodyrng_med63_21d_jerk_v074_signal,
    f13cr_f13_candle_range_structure_bodyrng_kurt63_21d_jerk_v075_signal,
    f13cr_f13_candle_range_structure_bodyrng_disp63_21d_jerk_v076_signal,
    f13cr_f13_candle_range_structure_sbodyrng_ema21_21d_jerk_v077_signal,
    f13cr_f13_candle_range_structure_sbodyrng_med21_21d_jerk_v078_signal,
    f13cr_f13_candle_range_structure_bodyrun_sm_21d_jerk_v079_signal,
    f13cr_f13_candle_range_structure_bodyskew_63_21d_jerk_v080_signal,
    f13cr_f13_candle_range_structure_cir_ema21_21d_jerk_v081_signal,
    f13cr_f13_candle_range_structure_cir_med63_21d_jerk_v082_signal,
    f13cr_f13_candle_range_structure_cir_skew63_21d_jerk_v083_signal,
    f13cr_f13_candle_range_structure_cir_disp63_21d_jerk_v084_signal,
    f13cr_f13_candle_range_structure_cir_diffvol_21d_jerk_v085_signal,
    f13cr_f13_candle_range_structure_clvvol_ema42_21d_jerk_v086_signal,
    f13cr_f13_candle_range_structure_clv_kurt63_21d_jerk_v087_signal,
    f13cr_f13_candle_range_structure_uwick_ema21_21d_jerk_v088_signal,
    f13cr_f13_candle_range_structure_lwick_ema21_21d_jerk_v089_signal,
    f13cr_f13_candle_range_structure_wickskew_vol42_21d_jerk_v090_signal,
    f13cr_f13_candle_range_structure_wickskew_rank126_21d_jerk_v091_signal,
    f13cr_f13_candle_range_structure_uwick_at_highs21_21d_jerk_v092_signal,
    f13cr_f13_candle_range_structure_uwick_med63_21d_jerk_v093_signal,
    f13cr_f13_candle_range_structure_lwick_med63_21d_jerk_v094_signal,
    f13cr_f13_candle_range_structure_rngpct_ema42_21d_jerk_v095_signal,
    f13cr_f13_candle_range_structure_rngpct_med63_21d_jerk_v096_signal,
    f13cr_f13_candle_range_structure_rngpct_skew63_21d_jerk_v097_signal,
    f13cr_f13_candle_range_structure_rngpct_kurt63_21d_jerk_v098_signal,
    f13cr_f13_candle_range_structure_rng_log_sm21_21d_jerk_v099_signal,
    f13cr_f13_candle_range_structure_rngexp_ema_21d_jerk_v100_signal,
    f13cr_f13_candle_range_structure_rng_upsemi63_21d_jerk_v101_signal,
    f13cr_f13_candle_range_structure_rng_dnsemi63_21d_jerk_v102_signal,
    f13cr_f13_candle_range_structure_gap_to_tr_21_21d_jerk_v103_signal,
    f13cr_f13_candle_range_structure_rngvbody_ema21_21d_jerk_v104_signal,
    f13cr_f13_candle_range_structure_bodytr_ema21_21d_jerk_v105_signal,
    f13cr_f13_candle_range_structure_body_range_corr63_21d_jerk_v106_signal,
    f13cr_f13_candle_range_structure_climaxup_sm21_21d_jerk_v107_signal,
    f13cr_f13_candle_range_structure_climaxdn_sm21_21d_jerk_v108_signal,
    f13cr_f13_candle_range_structure_capit_sm21_21d_jerk_v109_signal,
    f13cr_f13_candle_range_structure_rngvolcorr_63_21d_jerk_v110_signal,
    f13cr_f13_candle_range_structure_cirvolcorr_63_21d_jerk_v111_signal,
    f13cr_f13_candle_range_structure_vwbodyrng_sm21_21d_jerk_v112_signal,
    f13cr_f13_candle_range_structure_range_per_vol_63_21d_jerk_v113_signal,
    f13cr_f13_candle_range_structure_widebias_63_21d_jerk_v114_signal,
    f13cr_f13_candle_range_structure_wideasym_63_21d_jerk_v115_signal,
    f13cr_f13_candle_range_structure_dirrng_signmag_21d_jerk_v116_signal,
    f13cr_f13_candle_range_structure_typdrift_3bar_21d_jerk_v117_signal,
    f13cr_f13_candle_range_structure_excbal_ema63_21d_jerk_v118_signal,
    f13cr_f13_candle_range_structure_openpos_med21_21d_jerk_v119_signal,
    f13cr_f13_candle_range_structure_gapinbar_med63_21d_jerk_v120_signal,
    f13cr_f13_candle_range_structure_opendrive_ema21_21d_jerk_v121_signal,
    f13cr_f13_candle_range_structure_gapup_sm21_21d_jerk_v122_signal,
    f13cr_f13_candle_range_structure_gapdn_sm21_21d_jerk_v123_signal,
    f13cr_f13_candle_range_structure_overnight_share63_21d_jerk_v124_signal,
    f13cr_f13_candle_range_structure_rngvarratio_63_21d_jerk_v125_signal,
    f13cr_f13_candle_range_structure_rngburst_21_21d_jerk_v126_signal,
    f13cr_f13_candle_range_structure_rngshock_21_21d_jerk_v127_signal,
    f13cr_f13_candle_range_structure_rejhi_63_21d_jerk_v128_signal,
    f13cr_f13_candle_range_structure_demlo_63_21d_jerk_v129_signal,
    f13cr_f13_candle_range_structure_pinpress_sm21_21d_jerk_v130_signal,
    f13cr_f13_candle_range_structure_wickbal_at_lows21_21d_jerk_v131_signal,
    f13cr_f13_candle_range_structure_revbar_sm21_21d_jerk_v132_signal,
    f13cr_f13_candle_range_structure_trendday_sm21_21d_jerk_v133_signal,
    f13cr_f13_candle_range_structure_rngpath_21_21d_jerk_v134_signal,
    f13cr_f13_candle_range_structure_exhcombo_63_21d_jerk_v135_signal,
    f13cr_f13_candle_range_structure_exhaust_21_21d_jerk_v136_signal,
    f13cr_f13_candle_range_structure_rngbodydiv_21_21d_jerk_v137_signal,
    f13cr_f13_candle_range_structure_squeeze_5v126_21d_jerk_v138_signal,
    f13cr_f13_candle_range_structure_garmanklass_21_21d_jerk_v139_signal,
    f13cr_f13_candle_range_structure_cir3mom_21_21d_jerk_v140_signal,
    f13cr_f13_candle_range_structure_brcov_63_21d_jerk_v141_signal,
    f13cr_f13_candle_range_structure_edge_med63_21d_jerk_v142_signal,
    f13cr_f13_candle_range_structure_wickwt_21_21d_jerk_v143_signal,
    f13cr_f13_candle_range_structure_clv_wide_sm21_21d_jerk_v144_signal,
    f13cr_f13_candle_range_structure_bodymag_rank126_21d_jerk_v145_signal,
    f13cr_f13_candle_range_structure_strongvol_63_21d_jerk_v146_signal,
    f13cr_f13_candle_range_structure_uw_lw_cov63_21d_jerk_v147_signal,
    f13cr_f13_candle_range_structure_parkinson_63_21d_jerk_v148_signal,
    f13cr_f13_candle_range_structure_updnbody_asym63_21d_jerk_v149_signal,
    f13cr_f13_candle_range_structure_wick_vol_corr63_21d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F13_CANDLE_RANGE_STRUCTURE_REGISTRY_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0004, 0.032, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.012, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(1.2e6, 7e5, n)) + 5e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    ALLOW = {"open", "high", "low", "close", "closeadj", "volume"}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs=%s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f13_candle_range_structure_jerk_001_150_claude: %d features pass" % n_features)
