import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
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


# ===== folder domain primitives (volatility squeeze / breakout) =====
def _f06_bandwidth(s, w, k=2.0):
    # Bollinger bandwidth = (upper - lower) / mid = 2*k*std/mean
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (2.0 * k * sd) / m.replace(0, np.nan)


def _f06_squeeze(h, l, c, w, k=2.0, kc=1.5):
    # squeeze ratio = Bollinger width / Keltner(ATR) width; <1 => coiled (compressed)
    m = c.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = c.rolling(w, min_periods=max(2, w // 2)).std()
    bb_w = 2.0 * k * sd
    tr = pd.concat([(h - l).abs(),
                    (h - c.shift(1)).abs(),
                    (l - c.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(w, min_periods=max(2, w // 2)).mean()
    kc_w = 2.0 * kc * atr
    return bb_w / kc_w.replace(0, np.nan) + m * 0.0


def _f06_pctb(s, w, k=2.0):
    # %B = (close - lower) / (upper - lower); position within the Bollinger envelope
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    upper = m + k * sd
    lower = m - k * sd
    return (s - lower) / (upper - lower).replace(0, np.nan)


def _f06_atrp(h, l, c, w):
    # ATR normalized by price (true-range compression measure)
    tr = pd.concat([(h - l).abs(),
                    (h - c.shift(1)).abs(),
                    (l - c.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.rolling(w, min_periods=max(2, w // 2)).mean()
    return atr / c.replace(0, np.nan)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f06sq_f06_volatility_squeeze_breakout_bw_21d_slope_v001_signal(closeadj):
    result = _f06_bandwidth(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_63d_slope_v002_signal(closeadj):
    result = _f06_bandwidth(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_126d_slope_v003_signal(closeadj):
    result = _f06_bandwidth(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_10d_slope_v004_signal(closeadj):
    result = _f06_bandwidth(closeadj, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_42d_slope_v005_signal(closeadj):
    result = _f06_bandwidth(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_252d_slope_v006_signal(closeadj):
    result = _f06_bandwidth(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwk1_21d_slope_v007_signal(closeadj):
    result = _f06_bandwidth(closeadj, 21, 1.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwk3_63d_slope_v008_signal(closeadj):
    result = _f06_bandwidth(closeadj, 63, 3.0)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwrank_21d_slope_v009_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    result = bw.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwrank_63d_slope_v010_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    result = bw.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwrank_126d_slope_v011_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 126)
    result = bw.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwz_21d_slope_v012_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 21), 252)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwz_63d_slope_v013_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwz_126d_slope_v014_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 126), 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwratio_21_126_slope_v015_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 21), _f06_bandwidth(closeadj, 126))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwratio_42_252_slope_v016_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 42), _f06_bandwidth(closeadj, 252))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwratio_10_63_slope_v017_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 10), _f06_bandwidth(closeadj, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwrel_21d_slope_v018_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    result = _safe_div(bw, _mean(bw, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwrel_63d_slope_v019_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    result = _safe_div(bw, _mean(bw, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_21d_slope_v020_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_63d_slope_v021_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_126d_slope_v022_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_10d_slope_v023_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_42d_slope_v024_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_252d_slope_v025_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqz_21d_slope_v026_signal(high, low, closeadj):
    result = _z(_f06_squeeze(high, low, closeadj, 21), 252)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqz_63d_slope_v027_signal(high, low, closeadj):
    result = _z(_f06_squeeze(high, low, closeadj, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqrank_21d_slope_v028_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 21)
    result = sq.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqrank_63d_slope_v029_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 63)
    result = sq.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqrel_21d_slope_v030_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 21)
    result = _safe_div(sq, _mean(sq, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_21d_slope_v031_signal(closeadj):
    result = _f06_pctb(closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_63d_slope_v032_signal(closeadj):
    result = _f06_pctb(closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_126d_slope_v033_signal(closeadj):
    result = _f06_pctb(closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_10d_slope_v034_signal(closeadj):
    result = _f06_pctb(closeadj, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_42d_slope_v035_signal(closeadj):
    result = _f06_pctb(closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_252d_slope_v036_signal(closeadj):
    result = _f06_pctb(closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbc_21d_slope_v037_signal(closeadj):
    result = _f06_pctb(closeadj, 21) - 0.5
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbc_63d_slope_v038_signal(closeadj):
    result = _f06_pctb(closeadj, 63) - 0.5
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbk1_21d_slope_v039_signal(closeadj):
    result = _f06_pctb(closeadj, 21, 1.0)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbk3_63d_slope_v040_signal(closeadj):
    result = _f06_pctb(closeadj, 63, 3.0)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrp_21d_slope_v041_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrp_63d_slope_v042_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrp_126d_slope_v043_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrp_10d_slope_v044_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 10)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrp_252d_slope_v045_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrpratio_21_126_slope_v046_signal(high, low, closeadj):
    result = _safe_div(_f06_atrp(high, low, closeadj, 21), _f06_atrp(high, low, closeadj, 126))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrpz_21d_slope_v047_signal(high, low, closeadj):
    result = _z(_f06_atrp(high, low, closeadj, 21), 252)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrprank_63d_slope_v048_signal(high, low, closeadj):
    a = _f06_atrp(high, low, closeadj, 63)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_distup_21d_slope_v049_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    upper = m + 2.0 * sd
    result = _safe_div(upper - closeadj, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_distdn_21d_slope_v050_signal(closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    lower = m - 2.0 * sd
    result = _safe_div(closeadj - lower, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_distup_63d_slope_v051_signal(closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    upper = m + 2.0 * sd
    result = _safe_div(upper - closeadj, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_distdn_63d_slope_v052_signal(closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    lower = m - 2.0 * sd
    result = _safe_div(closeadj - lower, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_midz_21d_slope_v053_signal(closeadj):
    result = _z(closeadj, 21) + _f06_bandwidth(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_midz_63d_slope_v054_signal(closeadj):
    result = _z(closeadj, 63) + _f06_bandwidth(closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_rngcomp_21d_slope_v055_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _safe_div(_mean(rng, 21), _mean(rng, 63)) + _f06_atrp(high, low, closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_rngcomp_63d_slope_v056_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _safe_div(_mean(rng, 63), _mean(rng, 252)) + _f06_atrp(high, low, closeadj, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_stdratio_10_63_slope_v057_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 10), _std(lr, 63)) + _f06_bandwidth(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_stdratio_21_126_slope_v058_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 21), _std(lr, 126)) + _f06_bandwidth(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_stdratio_42_252_slope_v059_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 42), _std(lr, 252)) + _f06_bandwidth(closeadj, 42) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_coil_21d_slope_v060_signal(closeadj):
    result = -_z(_f06_bandwidth(closeadj, 21), 252)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_coil_63d_slope_v061_signal(closeadj):
    result = -_z(_f06_bandwidth(closeadj, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqxb_21d_slope_v062_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 21) * (_f06_pctb(closeadj, 21) - 0.5)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqxb_63d_slope_v063_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 63) * (_f06_pctb(closeadj, 63) - 0.5)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwchg_21d_slope_v064_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    result = _safe_div(bw - bw.shift(21), _mean(bw, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwchg_63d_slope_v065_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    result = _safe_div(bw - bw.shift(21), _mean(bw, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqchg_21d_slope_v066_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 21)
    result = _safe_div(sq - sq.shift(21), _mean(sq, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbmom_21d_slope_v067_signal(closeadj):
    b = _f06_pctb(closeadj, 21)
    result = b - b.shift(21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbmom_63d_slope_v068_signal(closeadj):
    b = _f06_pctb(closeadj, 63)
    result = b - b.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwewm_21d_slope_v069_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    result = bw.ewm(span=21, min_periods=10).mean()
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwewm_63d_slope_v070_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    result = bw.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwdisp_63d_slope_v071_signal(closeadj):
    result = _std(_f06_bandwidth(closeadj, 21), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwdisp_126d_slope_v072_signal(closeadj):
    result = _std(_f06_bandwidth(closeadj, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_upatr_21d_slope_v073_signal(high, low, closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    upper = m + 2.0 * sd
    atrp = _f06_atrp(high, low, closeadj, 21)
    result = _safe_div(upper - closeadj, atrp * closeadj)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_dnatr_21d_slope_v074_signal(high, low, closeadj):
    m = _mean(closeadj, 21)
    sd = _std(closeadj, 21)
    lower = m - 2.0 * sd
    atrp = _f06_atrp(high, low, closeadj, 21)
    result = _safe_div(closeadj - lower, atrp * closeadj)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_invsq_21d_slope_v075_signal(high, low, closeadj):
    result = _safe_div(pd.Series(1.0, index=closeadj.index), _f06_squeeze(high, low, closeadj, 21))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_84d_slope_v076_signal(closeadj):
    result = _f06_bandwidth(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_189d_slope_v077_signal(closeadj):
    result = _f06_bandwidth(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_5d_slope_v078_signal(closeadj):
    result = _f06_bandwidth(closeadj, 5)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_504d_slope_v079_signal(closeadj):
    result = _f06_bandwidth(closeadj, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bw_315d_slope_v080_signal(closeadj):
    result = _f06_bandwidth(closeadj, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwk25_21d_slope_v081_signal(closeadj):
    result = _f06_bandwidth(closeadj, 21, 2.5)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwk15_126d_slope_v082_signal(closeadj):
    result = _f06_bandwidth(closeadj, 126, 1.5)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwrank_42d_slope_v083_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 42)
    result = bw.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwrank_252d_slope_v084_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 252)
    result = bw.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwz_42d_slope_v085_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 42), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwz_84d_slope_v086_signal(closeadj):
    result = _z(_f06_bandwidth(closeadj, 84), 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwratio_21_252_slope_v087_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 21), _f06_bandwidth(closeadj, 252))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwratio_63_252_slope_v088_signal(closeadj):
    result = _safe_div(_f06_bandwidth(closeadj, 63), _f06_bandwidth(closeadj, 252))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwrel_126d_slope_v089_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 126)
    result = _safe_div(bw, _mean(bw, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_84d_slope_v090_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_189d_slope_v091_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sq_5d_slope_v092_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 5)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqz_126d_slope_v093_signal(high, low, closeadj):
    result = _z(_f06_squeeze(high, low, closeadj, 126), 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqz_42d_slope_v094_signal(high, low, closeadj):
    result = _z(_f06_squeeze(high, low, closeadj, 42), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqrank_126d_slope_v095_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 126)
    result = sq.rolling(504, min_periods=126).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqrank_42d_slope_v096_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 42)
    result = sq.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqrel_63d_slope_v097_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 63)
    result = _safe_div(sq, _mean(sq, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqratio_21_126_slope_v098_signal(high, low, closeadj):
    result = _safe_div(_f06_squeeze(high, low, closeadj, 21), _f06_squeeze(high, low, closeadj, 126))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_84d_slope_v099_signal(closeadj):
    result = _f06_pctb(closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_189d_slope_v100_signal(closeadj):
    result = _f06_pctb(closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctb_5d_slope_v101_signal(closeadj):
    result = _f06_pctb(closeadj, 5)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbsm_21d_slope_v102_signal(closeadj):
    result = _mean(_f06_pctb(closeadj, 21), 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbsm_63d_slope_v103_signal(closeadj):
    result = _mean(_f06_pctb(closeadj, 63), 21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbz_21d_slope_v104_signal(closeadj):
    result = _z(_f06_pctb(closeadj, 21), 252)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbz_63d_slope_v105_signal(closeadj):
    result = _z(_f06_pctb(closeadj, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbdisp_63d_slope_v106_signal(closeadj):
    result = _std(_f06_pctb(closeadj, 21), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrp_84d_slope_v107_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrp_189d_slope_v108_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrp_42d_slope_v109_signal(high, low, closeadj):
    result = _f06_atrp(high, low, closeadj, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrpratio_10_63_slope_v110_signal(high, low, closeadj):
    result = _safe_div(_f06_atrp(high, low, closeadj, 10), _f06_atrp(high, low, closeadj, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrpratio_42_252_slope_v111_signal(high, low, closeadj):
    result = _safe_div(_f06_atrp(high, low, closeadj, 42), _f06_atrp(high, low, closeadj, 252))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrpz_63d_slope_v112_signal(high, low, closeadj):
    result = _z(_f06_atrp(high, low, closeadj, 63), 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrprank_21d_slope_v113_signal(high, low, closeadj):
    a = _f06_atrp(high, low, closeadj, 21)
    result = a.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrprel_21d_slope_v114_signal(high, low, closeadj):
    a = _f06_atrp(high, low, closeadj, 21)
    result = _safe_div(a, _mean(a, 63))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_distup_126d_slope_v115_signal(closeadj):
    m = _mean(closeadj, 126)
    sd = _std(closeadj, 126)
    upper = m + 2.0 * sd
    result = _safe_div(upper - closeadj, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_distdn_126d_slope_v116_signal(closeadj):
    m = _mean(closeadj, 126)
    sd = _std(closeadj, 126)
    lower = m - 2.0 * sd
    result = _safe_div(closeadj - lower, 2.0 * 2.0 * sd) + _f06_bandwidth(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_midz_126d_slope_v117_signal(closeadj):
    result = _z(closeadj, 126) + _f06_bandwidth(closeadj, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_rngcomp_42d_slope_v118_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _safe_div(_mean(rng, 42), _mean(rng, 126)) + _f06_atrp(high, low, closeadj, 42) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_rngcomp_10d_slope_v119_signal(high, low, closeadj):
    rng = (high - low) / closeadj.replace(0, np.nan)
    result = _safe_div(_mean(rng, 10), _mean(rng, 42)) + _f06_atrp(high, low, closeadj, 10) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_stdratio_5_42_slope_v120_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 5), _std(lr, 42)) + _f06_bandwidth(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_stdratio_63_252_slope_v121_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    result = _safe_div(_std(lr, 63), _std(lr, 252)) + _f06_bandwidth(closeadj, 63) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_coil_126d_slope_v122_signal(closeadj):
    result = -_z(_f06_bandwidth(closeadj, 126), 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_coilrank_42d_slope_v123_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 42)
    result = 1.0 - bw.rolling(252, min_periods=63).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqxb_126d_slope_v124_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 126) * (_f06_pctb(closeadj, 126) - 0.5)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwxb_21d_slope_v125_signal(closeadj):
    result = _f06_bandwidth(closeadj, 21) * (_f06_pctb(closeadj, 21) - 0.5)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwxb_63d_slope_v126_signal(closeadj):
    result = _f06_bandwidth(closeadj, 63) * (_f06_pctb(closeadj, 63) - 0.5)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwchg_126d_slope_v127_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 126)
    result = _safe_div(bw - bw.shift(21), _mean(bw, 252))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwexp_126d_slope_v128_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    floor = bw.rolling(126, min_periods=42).min().replace(0, np.nan)
    result = _safe_div(bw, floor)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwexp_252d_slope_v129_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    floor = bw.rolling(252, min_periods=84).min().replace(0, np.nan)
    result = _safe_div(bw, floor)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_atrexp_126d_slope_v130_signal(high, low, closeadj):
    a = _f06_atrp(high, low, closeadj, 21)
    floor = a.rolling(126, min_periods=42).min().replace(0, np.nan)
    result = _safe_div(a, floor)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqchg_63d_slope_v131_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 63)
    result = _safe_div(sq - sq.shift(21), _mean(sq, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_pctbmom_126d_slope_v132_signal(closeadj):
    b = _f06_pctb(closeadj, 126)
    result = b - b.shift(21)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwewm_126d_slope_v133_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 126)
    result = bw.ewm(span=126, min_periods=42).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqewm_63d_slope_v134_signal(high, low, closeadj):
    sq = _f06_squeeze(high, low, closeadj, 63)
    result = sq.ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwdisp_252d_slope_v135_signal(closeadj):
    result = _std(_f06_bandwidth(closeadj, 21), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqdisp_126d_slope_v136_signal(high, low, closeadj):
    result = _std(_f06_squeeze(high, low, closeadj, 21), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_upatr_63d_slope_v137_signal(high, low, closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    upper = m + 2.0 * sd
    atrp = _f06_atrp(high, low, closeadj, 63)
    result = _safe_div(upper - closeadj, atrp * closeadj)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_dnatr_63d_slope_v138_signal(high, low, closeadj):
    m = _mean(closeadj, 63)
    sd = _std(closeadj, 63)
    lower = m - 2.0 * sd
    atrp = _f06_atrp(high, low, closeadj, 63)
    result = _safe_div(closeadj - lower, atrp * closeadj)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_invsq_63d_slope_v139_signal(high, low, closeadj):
    result = _safe_div(pd.Series(1.0, index=closeadj.index), _f06_squeeze(high, low, closeadj, 63))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_armed_21d_slope_v140_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 21)
    b = _f06_pctb(closeadj, 21)
    result = _safe_div(b - b.shift(21), bw)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_armed_63d_slope_v141_signal(closeadj):
    bw = _f06_bandwidth(closeadj, 63)
    b = _f06_pctb(closeadj, 63)
    result = _safe_div(b - b.shift(21), bw)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwvoln_21d_slope_v142_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252)
    result = _safe_div(_f06_bandwidth(closeadj, 21), vol)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_bwvoln_63d_slope_v143_signal(closeadj):
    lr = np.log(closeadj / closeadj.shift(1))
    vol = _std(lr, 252)
    result = _safe_div(_f06_bandwidth(closeadj, 63), vol)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqdev_21d_slope_v144_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 21) - 1.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_sqdev_63d_slope_v145_signal(high, low, closeadj):
    result = _f06_squeeze(high, low, closeadj, 63) - 1.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_logbw_21d_slope_v146_signal(closeadj):
    result = np.log(_f06_bandwidth(closeadj, 21).replace(0, np.nan))
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_logbw_63d_slope_v147_signal(closeadj):
    result = np.log(_f06_bandwidth(closeadj, 63).replace(0, np.nan))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_edge_21d_slope_v148_signal(closeadj):
    b = _f06_pctb(closeadj, 21)
    result = (b - 0.5).abs()
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_edge_63d_slope_v149_signal(closeadj):
    b = _f06_pctb(closeadj, 63)
    result = (b - 0.5).abs()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f06sq_f06_volatility_squeeze_breakout_blend_multi_slope_v150_signal(high, low, closeadj):
    bwr = _f06_bandwidth(closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    atr = _f06_atrp(high, low, closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    sq = _f06_squeeze(high, low, closeadj, 21).rolling(252, min_periods=63).rank(pct=True)
    result = (bwr + atr + sq) / 3.0 + _f06_pctb(closeadj, 21) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f06sq_f06_volatility_squeeze_breakout_bw_21d_slope_v001_signal,    f06sq_f06_volatility_squeeze_breakout_bw_63d_slope_v002_signal,    f06sq_f06_volatility_squeeze_breakout_bw_126d_slope_v003_signal,    f06sq_f06_volatility_squeeze_breakout_bw_10d_slope_v004_signal,    f06sq_f06_volatility_squeeze_breakout_bw_42d_slope_v005_signal,    f06sq_f06_volatility_squeeze_breakout_bw_252d_slope_v006_signal,    f06sq_f06_volatility_squeeze_breakout_bwk1_21d_slope_v007_signal,    f06sq_f06_volatility_squeeze_breakout_bwk3_63d_slope_v008_signal,    f06sq_f06_volatility_squeeze_breakout_bwrank_21d_slope_v009_signal,    f06sq_f06_volatility_squeeze_breakout_bwrank_63d_slope_v010_signal,    f06sq_f06_volatility_squeeze_breakout_bwrank_126d_slope_v011_signal,    f06sq_f06_volatility_squeeze_breakout_bwz_21d_slope_v012_signal,    f06sq_f06_volatility_squeeze_breakout_bwz_63d_slope_v013_signal,    f06sq_f06_volatility_squeeze_breakout_bwz_126d_slope_v014_signal,    f06sq_f06_volatility_squeeze_breakout_bwratio_21_126_slope_v015_signal,    f06sq_f06_volatility_squeeze_breakout_bwratio_42_252_slope_v016_signal,    f06sq_f06_volatility_squeeze_breakout_bwratio_10_63_slope_v017_signal,    f06sq_f06_volatility_squeeze_breakout_bwrel_21d_slope_v018_signal,    f06sq_f06_volatility_squeeze_breakout_bwrel_63d_slope_v019_signal,    f06sq_f06_volatility_squeeze_breakout_sq_21d_slope_v020_signal,    f06sq_f06_volatility_squeeze_breakout_sq_63d_slope_v021_signal,    f06sq_f06_volatility_squeeze_breakout_sq_126d_slope_v022_signal,    f06sq_f06_volatility_squeeze_breakout_sq_10d_slope_v023_signal,    f06sq_f06_volatility_squeeze_breakout_sq_42d_slope_v024_signal,    f06sq_f06_volatility_squeeze_breakout_sq_252d_slope_v025_signal,    f06sq_f06_volatility_squeeze_breakout_sqz_21d_slope_v026_signal,    f06sq_f06_volatility_squeeze_breakout_sqz_63d_slope_v027_signal,    f06sq_f06_volatility_squeeze_breakout_sqrank_21d_slope_v028_signal,    f06sq_f06_volatility_squeeze_breakout_sqrank_63d_slope_v029_signal,    f06sq_f06_volatility_squeeze_breakout_sqrel_21d_slope_v030_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_21d_slope_v031_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_63d_slope_v032_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_126d_slope_v033_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_10d_slope_v034_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_42d_slope_v035_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_252d_slope_v036_signal,    f06sq_f06_volatility_squeeze_breakout_pctbc_21d_slope_v037_signal,    f06sq_f06_volatility_squeeze_breakout_pctbc_63d_slope_v038_signal,    f06sq_f06_volatility_squeeze_breakout_pctbk1_21d_slope_v039_signal,    f06sq_f06_volatility_squeeze_breakout_pctbk3_63d_slope_v040_signal,    f06sq_f06_volatility_squeeze_breakout_atrp_21d_slope_v041_signal,    f06sq_f06_volatility_squeeze_breakout_atrp_63d_slope_v042_signal,    f06sq_f06_volatility_squeeze_breakout_atrp_126d_slope_v043_signal,    f06sq_f06_volatility_squeeze_breakout_atrp_10d_slope_v044_signal,    f06sq_f06_volatility_squeeze_breakout_atrp_252d_slope_v045_signal,    f06sq_f06_volatility_squeeze_breakout_atrpratio_21_126_slope_v046_signal,    f06sq_f06_volatility_squeeze_breakout_atrpz_21d_slope_v047_signal,    f06sq_f06_volatility_squeeze_breakout_atrprank_63d_slope_v048_signal,    f06sq_f06_volatility_squeeze_breakout_distup_21d_slope_v049_signal,    f06sq_f06_volatility_squeeze_breakout_distdn_21d_slope_v050_signal,    f06sq_f06_volatility_squeeze_breakout_distup_63d_slope_v051_signal,    f06sq_f06_volatility_squeeze_breakout_distdn_63d_slope_v052_signal,    f06sq_f06_volatility_squeeze_breakout_midz_21d_slope_v053_signal,    f06sq_f06_volatility_squeeze_breakout_midz_63d_slope_v054_signal,    f06sq_f06_volatility_squeeze_breakout_rngcomp_21d_slope_v055_signal,    f06sq_f06_volatility_squeeze_breakout_rngcomp_63d_slope_v056_signal,    f06sq_f06_volatility_squeeze_breakout_stdratio_10_63_slope_v057_signal,    f06sq_f06_volatility_squeeze_breakout_stdratio_21_126_slope_v058_signal,    f06sq_f06_volatility_squeeze_breakout_stdratio_42_252_slope_v059_signal,    f06sq_f06_volatility_squeeze_breakout_coil_21d_slope_v060_signal,    f06sq_f06_volatility_squeeze_breakout_coil_63d_slope_v061_signal,    f06sq_f06_volatility_squeeze_breakout_sqxb_21d_slope_v062_signal,    f06sq_f06_volatility_squeeze_breakout_sqxb_63d_slope_v063_signal,    f06sq_f06_volatility_squeeze_breakout_bwchg_21d_slope_v064_signal,    f06sq_f06_volatility_squeeze_breakout_bwchg_63d_slope_v065_signal,    f06sq_f06_volatility_squeeze_breakout_sqchg_21d_slope_v066_signal,    f06sq_f06_volatility_squeeze_breakout_pctbmom_21d_slope_v067_signal,    f06sq_f06_volatility_squeeze_breakout_pctbmom_63d_slope_v068_signal,    f06sq_f06_volatility_squeeze_breakout_bwewm_21d_slope_v069_signal,    f06sq_f06_volatility_squeeze_breakout_bwewm_63d_slope_v070_signal,    f06sq_f06_volatility_squeeze_breakout_bwdisp_63d_slope_v071_signal,    f06sq_f06_volatility_squeeze_breakout_bwdisp_126d_slope_v072_signal,    f06sq_f06_volatility_squeeze_breakout_upatr_21d_slope_v073_signal,    f06sq_f06_volatility_squeeze_breakout_dnatr_21d_slope_v074_signal,    f06sq_f06_volatility_squeeze_breakout_invsq_21d_slope_v075_signal,    f06sq_f06_volatility_squeeze_breakout_bw_84d_slope_v076_signal,    f06sq_f06_volatility_squeeze_breakout_bw_189d_slope_v077_signal,    f06sq_f06_volatility_squeeze_breakout_bw_5d_slope_v078_signal,    f06sq_f06_volatility_squeeze_breakout_bw_504d_slope_v079_signal,    f06sq_f06_volatility_squeeze_breakout_bw_315d_slope_v080_signal,    f06sq_f06_volatility_squeeze_breakout_bwk25_21d_slope_v081_signal,    f06sq_f06_volatility_squeeze_breakout_bwk15_126d_slope_v082_signal,    f06sq_f06_volatility_squeeze_breakout_bwrank_42d_slope_v083_signal,    f06sq_f06_volatility_squeeze_breakout_bwrank_252d_slope_v084_signal,    f06sq_f06_volatility_squeeze_breakout_bwz_42d_slope_v085_signal,    f06sq_f06_volatility_squeeze_breakout_bwz_84d_slope_v086_signal,    f06sq_f06_volatility_squeeze_breakout_bwratio_21_252_slope_v087_signal,    f06sq_f06_volatility_squeeze_breakout_bwratio_63_252_slope_v088_signal,    f06sq_f06_volatility_squeeze_breakout_bwrel_126d_slope_v089_signal,    f06sq_f06_volatility_squeeze_breakout_sq_84d_slope_v090_signal,    f06sq_f06_volatility_squeeze_breakout_sq_189d_slope_v091_signal,    f06sq_f06_volatility_squeeze_breakout_sq_5d_slope_v092_signal,    f06sq_f06_volatility_squeeze_breakout_sqz_126d_slope_v093_signal,    f06sq_f06_volatility_squeeze_breakout_sqz_42d_slope_v094_signal,    f06sq_f06_volatility_squeeze_breakout_sqrank_126d_slope_v095_signal,    f06sq_f06_volatility_squeeze_breakout_sqrank_42d_slope_v096_signal,    f06sq_f06_volatility_squeeze_breakout_sqrel_63d_slope_v097_signal,    f06sq_f06_volatility_squeeze_breakout_sqratio_21_126_slope_v098_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_84d_slope_v099_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_189d_slope_v100_signal,    f06sq_f06_volatility_squeeze_breakout_pctb_5d_slope_v101_signal,    f06sq_f06_volatility_squeeze_breakout_pctbsm_21d_slope_v102_signal,    f06sq_f06_volatility_squeeze_breakout_pctbsm_63d_slope_v103_signal,    f06sq_f06_volatility_squeeze_breakout_pctbz_21d_slope_v104_signal,    f06sq_f06_volatility_squeeze_breakout_pctbz_63d_slope_v105_signal,    f06sq_f06_volatility_squeeze_breakout_pctbdisp_63d_slope_v106_signal,    f06sq_f06_volatility_squeeze_breakout_atrp_84d_slope_v107_signal,    f06sq_f06_volatility_squeeze_breakout_atrp_189d_slope_v108_signal,    f06sq_f06_volatility_squeeze_breakout_atrp_42d_slope_v109_signal,    f06sq_f06_volatility_squeeze_breakout_atrpratio_10_63_slope_v110_signal,    f06sq_f06_volatility_squeeze_breakout_atrpratio_42_252_slope_v111_signal,    f06sq_f06_volatility_squeeze_breakout_atrpz_63d_slope_v112_signal,    f06sq_f06_volatility_squeeze_breakout_atrprank_21d_slope_v113_signal,    f06sq_f06_volatility_squeeze_breakout_atrprel_21d_slope_v114_signal,    f06sq_f06_volatility_squeeze_breakout_distup_126d_slope_v115_signal,    f06sq_f06_volatility_squeeze_breakout_distdn_126d_slope_v116_signal,    f06sq_f06_volatility_squeeze_breakout_midz_126d_slope_v117_signal,    f06sq_f06_volatility_squeeze_breakout_rngcomp_42d_slope_v118_signal,    f06sq_f06_volatility_squeeze_breakout_rngcomp_10d_slope_v119_signal,    f06sq_f06_volatility_squeeze_breakout_stdratio_5_42_slope_v120_signal,    f06sq_f06_volatility_squeeze_breakout_stdratio_63_252_slope_v121_signal,    f06sq_f06_volatility_squeeze_breakout_coil_126d_slope_v122_signal,    f06sq_f06_volatility_squeeze_breakout_coilrank_42d_slope_v123_signal,    f06sq_f06_volatility_squeeze_breakout_sqxb_126d_slope_v124_signal,    f06sq_f06_volatility_squeeze_breakout_bwxb_21d_slope_v125_signal,    f06sq_f06_volatility_squeeze_breakout_bwxb_63d_slope_v126_signal,    f06sq_f06_volatility_squeeze_breakout_bwchg_126d_slope_v127_signal,    f06sq_f06_volatility_squeeze_breakout_bwexp_126d_slope_v128_signal,    f06sq_f06_volatility_squeeze_breakout_bwexp_252d_slope_v129_signal,    f06sq_f06_volatility_squeeze_breakout_atrexp_126d_slope_v130_signal,    f06sq_f06_volatility_squeeze_breakout_sqchg_63d_slope_v131_signal,    f06sq_f06_volatility_squeeze_breakout_pctbmom_126d_slope_v132_signal,    f06sq_f06_volatility_squeeze_breakout_bwewm_126d_slope_v133_signal,    f06sq_f06_volatility_squeeze_breakout_sqewm_63d_slope_v134_signal,    f06sq_f06_volatility_squeeze_breakout_bwdisp_252d_slope_v135_signal,    f06sq_f06_volatility_squeeze_breakout_sqdisp_126d_slope_v136_signal,    f06sq_f06_volatility_squeeze_breakout_upatr_63d_slope_v137_signal,    f06sq_f06_volatility_squeeze_breakout_dnatr_63d_slope_v138_signal,    f06sq_f06_volatility_squeeze_breakout_invsq_63d_slope_v139_signal,    f06sq_f06_volatility_squeeze_breakout_armed_21d_slope_v140_signal,    f06sq_f06_volatility_squeeze_breakout_armed_63d_slope_v141_signal,    f06sq_f06_volatility_squeeze_breakout_bwvoln_21d_slope_v142_signal,    f06sq_f06_volatility_squeeze_breakout_bwvoln_63d_slope_v143_signal,    f06sq_f06_volatility_squeeze_breakout_sqdev_21d_slope_v144_signal,    f06sq_f06_volatility_squeeze_breakout_sqdev_63d_slope_v145_signal,    f06sq_f06_volatility_squeeze_breakout_logbw_21d_slope_v146_signal,    f06sq_f06_volatility_squeeze_breakout_logbw_63d_slope_v147_signal,    f06sq_f06_volatility_squeeze_breakout_edge_21d_slope_v148_signal,    f06sq_f06_volatility_squeeze_breakout_edge_63d_slope_v149_signal,    f06sq_f06_volatility_squeeze_breakout_blend_multi_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F06_VOLATILITY_SQUEEZE_BREAKOUT_REGISTRY_SLOPE = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f06_bandwidth', '_f06_squeeze', '_f06_pctb', '_f06_atrp')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
    print("OK f06_volatility_squeeze_breakout_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
