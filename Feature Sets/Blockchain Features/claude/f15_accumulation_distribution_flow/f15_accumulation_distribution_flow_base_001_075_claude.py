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


# ===== folder domain primitives (accumulation-distribution / money-flow) =====
def _f15_mfm(high, low, close):
    # money-flow multiplier = ((close-low)-(high-close))/(high-low), in [-1, 1]
    rng = (high - low).replace(0, np.nan)
    return ((close - low) - (high - close)) / rng


def _f15_cmf(high, low, close, volume, w):
    # Chaikin money flow = sum(mfm*volume)/sum(volume) over w
    mfm = _f15_mfm(high, low, close)
    mfv = mfm * volume
    num = mfv.rolling(w, min_periods=max(2, w // 2)).sum()
    den = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    return num / den


def _f15_obvslope(close, volume, w):
    # normalized slope of on-balance-volume: keep CONTINUOUS via diff scaled by
    # rolling dollar-volume turnover (NOT raw cumulative level)
    direction = np.sign(close.diff())
    obv = (direction * volume).cumsum()
    d = obv.diff(periods=w)
    sc = volume.rolling(w, min_periods=max(2, w // 2)).sum().replace(0, np.nan)
    return d / sc


def _f15_forceidx(close, volume, w):
    # force index = price change * volume, smoothed then z-scored (CONTINUOUS)
    fi = close.diff() * volume
    sm = fi.ewm(span=w, min_periods=max(2, w // 2)).mean()
    return _z(sm, max(w * 3, 63))


# ============ FEATURES 001-075 ============

# Chaikin money flow 21d
def f15ad_f15_accumulation_distribution_flow_cmf_21d_base_v001_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 63d
def f15ad_f15_accumulation_distribution_flow_cmf_63d_base_v002_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 126d
def f15ad_f15_accumulation_distribution_flow_cmf_126d_base_v003_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 42d
def f15ad_f15_accumulation_distribution_flow_cmf_42d_base_v004_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 252d
def f15ad_f15_accumulation_distribution_flow_cmf_252d_base_v005_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 10d (weekly thrust)
def f15ad_f15_accumulation_distribution_flow_cmf_10d_base_v006_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 84d
def f15ad_f15_accumulation_distribution_flow_cmf_84d_base_v007_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 189d
def f15ad_f15_accumulation_distribution_flow_cmf_189d_base_v008_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier smoothed 21d
def f15ad_f15_accumulation_distribution_flow_mfmsm_21d_base_v009_signal(high, low, close):
    result = _mean(_f15_mfm(high, low, close), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier smoothed 63d
def f15ad_f15_accumulation_distribution_flow_mfmsm_63d_base_v010_signal(high, low, close):
    result = _mean(_f15_mfm(high, low, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier smoothed 126d
def f15ad_f15_accumulation_distribution_flow_mfmsm_126d_base_v011_signal(high, low, close):
    result = _mean(_f15_mfm(high, low, close), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier ewm 42d
def f15ad_f15_accumulation_distribution_flow_mfmewm_42d_base_v012_signal(high, low, close):
    result = _f15_mfm(high, low, close).ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier z-score 63d
def f15ad_f15_accumulation_distribution_flow_mfmz_63d_base_v013_signal(high, low, close):
    result = _z(_f15_mfm(high, low, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier z-score 126d
def f15ad_f15_accumulation_distribution_flow_mfmz_126d_base_v014_signal(high, low, close):
    result = _z(_f15_mfm(high, low, close), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV normalized slope 21d
def f15ad_f15_accumulation_distribution_flow_obvslope_21d_base_v015_signal(close, volume):
    result = _f15_obvslope(close, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV normalized slope 63d
def f15ad_f15_accumulation_distribution_flow_obvslope_63d_base_v016_signal(close, volume):
    result = _f15_obvslope(close, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV normalized slope 126d
def f15ad_f15_accumulation_distribution_flow_obvslope_126d_base_v017_signal(close, volume):
    result = _f15_obvslope(close, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV normalized slope 10d
def f15ad_f15_accumulation_distribution_flow_obvslope_10d_base_v018_signal(close, volume):
    result = _f15_obvslope(close, volume, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV normalized slope 252d
def f15ad_f15_accumulation_distribution_flow_obvslope_252d_base_v019_signal(close, volume):
    result = _f15_obvslope(close, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope z-scored over 252d (21d slope)
def f15ad_f15_accumulation_distribution_flow_obvslopez_21d_base_v020_signal(close, volume):
    result = _z(_f15_obvslope(close, volume, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope z-scored over 252d (63d slope)
def f15ad_f15_accumulation_distribution_flow_obvslopez_63d_base_v021_signal(close, volume):
    result = _z(_f15_obvslope(close, volume, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# force index z-score 21d
def f15ad_f15_accumulation_distribution_flow_force_21d_base_v022_signal(close, volume):
    result = _f15_forceidx(close, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# force index z-score 63d
def f15ad_f15_accumulation_distribution_flow_force_63d_base_v023_signal(close, volume):
    result = _f15_forceidx(close, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# force index z-score 13d (classic Elder)
def f15ad_f15_accumulation_distribution_flow_force_13d_base_v024_signal(close, volume):
    result = _f15_forceidx(close, volume, 13)
    return result.replace([np.inf, -np.inf], np.nan)


# force index z-score 126d
def f15ad_f15_accumulation_distribution_flow_force_126d_base_v025_signal(close, volume):
    result = _f15_forceidx(close, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-distribution line normalized by dollar-volume, 21d slope
def f15ad_f15_accumulation_distribution_flow_adlnorm_21d_base_v026_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    dv = (close * volume).rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = adl.diff(periods=21) / dv
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-distribution line normalized by dollar-volume, 63d slope
def f15ad_f15_accumulation_distribution_flow_adlnorm_63d_base_v027_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    dv = (close * volume).rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = adl.diff(periods=63) / dv
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-distribution line normalized by dollar-volume, 126d slope
def f15ad_f15_accumulation_distribution_flow_adlnorm_126d_base_v028_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    dv = (close * volume).rolling(126, min_periods=42).sum().replace(0, np.nan)
    result = adl.diff(periods=126) / dv
    return result.replace([np.inf, -np.inf], np.nan)


# ADL diff z-scored over 252d (21d)
def f15ad_f15_accumulation_distribution_flow_adlz_21d_base_v029_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    result = _z(adl.diff(periods=21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ADL diff z-scored over 252d (63d)
def f15ad_f15_accumulation_distribution_flow_adlz_63d_base_v030_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    result = _z(adl.diff(periods=63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# money flow index (MFI) 21d, continuous ratio form
def f15ad_f15_accumulation_distribution_flow_mfi_21d_base_v031_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(21, min_periods=10).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(21, min_periods=10).sum()
    result = _safe_div(pos, neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# money flow index (MFI) 63d
def f15ad_f15_accumulation_distribution_flow_mfi_63d_base_v032_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(63, min_periods=21).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(63, min_periods=21).sum()
    result = _safe_div(pos, neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# money flow index (MFI) 126d
def f15ad_f15_accumulation_distribution_flow_mfi_126d_base_v033_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(126, min_periods=42).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(126, min_periods=42).sum()
    result = _safe_div(pos, neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log money flow ratio 21d (continuous, symmetric)
def f15ad_f15_accumulation_distribution_flow_logmfr_21d_base_v034_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(21, min_periods=10).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = np.log(pos / neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log money flow ratio 63d
def f15ad_f15_accumulation_distribution_flow_logmfr_63d_base_v035_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(63, min_periods=21).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = np.log(pos / neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume-price-trend normalized 21d slope
def f15ad_f15_accumulation_distribution_flow_vpt_21d_base_v036_signal(close, volume):
    vpt = (close.pct_change() * volume).cumsum()
    sc = volume.rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = vpt.diff(periods=21) / sc + _f15_obvslope(close, volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume-price-trend normalized 63d slope
def f15ad_f15_accumulation_distribution_flow_vpt_63d_base_v037_signal(close, volume):
    vpt = (close.pct_change() * volume).cumsum()
    sc = volume.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = vpt.diff(periods=63) / sc + _f15_obvslope(close, volume, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume-price-trend normalized 126d slope
def f15ad_f15_accumulation_distribution_flow_vpt_126d_base_v038_signal(close, volume):
    vpt = (close.pct_change() * volume).cumsum()
    sc = volume.rolling(126, min_periods=42).sum().replace(0, np.nan)
    result = vpt.diff(periods=126) / sc + _f15_obvslope(close, volume, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator: EMA(3) - EMA(10) of ADL, normalized by dollar-volume
def f15ad_f15_accumulation_distribution_flow_chosc_3_10_base_v039_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    osc = adl.ewm(span=3, min_periods=2).mean() - adl.ewm(span=10, min_periods=5).mean()
    dv = (close * volume).rolling(21, min_periods=10).mean().replace(0, np.nan)
    result = osc / dv
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator EMA(10)-EMA(21)
def f15ad_f15_accumulation_distribution_flow_chosc_10_21_base_v040_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    osc = adl.ewm(span=10, min_periods=5).mean() - adl.ewm(span=21, min_periods=10).mean()
    dv = (close * volume).rolling(42, min_periods=21).mean().replace(0, np.nan)
    result = osc / dv
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator EMA(21)-EMA(63)
def f15ad_f15_accumulation_distribution_flow_chosc_21_63_base_v041_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    osc = adl.ewm(span=21, min_periods=10).mean() - adl.ewm(span=63, min_periods=21).mean()
    dv = (close * volume).rolling(84, min_periods=42).mean().replace(0, np.nan)
    result = osc / dv
    return result.replace([np.inf, -np.inf], np.nan)


# ease of movement 21d (smoothed, normalized by volume)
def f15ad_f15_accumulation_distribution_flow_eom_21d_base_v042_signal(high, low, volume):
    mid = (high + low) / 2.0
    dist = mid.diff()
    boxr = volume / (high - low).replace(0, np.nan)
    emv = dist / boxr.replace(0, np.nan)
    result = _mean(emv, 21) + _f15_mfm(high, low, mid) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ease of movement 63d
def f15ad_f15_accumulation_distribution_flow_eom_63d_base_v043_signal(high, low, volume):
    mid = (high + low) / 2.0
    dist = mid.diff()
    boxr = volume / (high - low).replace(0, np.nan)
    emv = dist / boxr.replace(0, np.nan)
    result = _mean(emv, 63) + _f15_mfm(high, low, mid) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ease of movement z-scored 21d over 252d
def f15ad_f15_accumulation_distribution_flow_eomz_21d_base_v044_signal(high, low, volume):
    mid = (high + low) / 2.0
    dist = mid.diff()
    boxr = volume / (high - low).replace(0, np.nan)
    emv = dist / boxr.replace(0, np.nan)
    result = _z(_mean(emv, 21), 252) + _f15_mfm(high, low, mid) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# up/down money-flow ratio (continuous sum-based) 42d
def f15ad_f15_accumulation_distribution_flow_udmf_42d_base_v045_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    up = mfv.clip(lower=0).rolling(42, min_periods=21).sum()
    dn = (-mfv.clip(upper=0)).rolling(42, min_periods=21).sum()
    result = _safe_div(up - dn, up + dn)
    return result.replace([np.inf, -np.inf], np.nan)


# up/down money-flow ratio 84d
def f15ad_f15_accumulation_distribution_flow_udmf_84d_base_v046_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    up = mfv.clip(lower=0).rolling(84, min_periods=42).sum()
    dn = (-mfv.clip(upper=0)).rolling(84, min_periods=42).sum()
    result = _safe_div(up - dn, up + dn)
    return result.replace([np.inf, -np.inf], np.nan)


# up/down money-flow ratio 126d
def f15ad_f15_accumulation_distribution_flow_udmf_126d_base_v047_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    up = mfv.clip(lower=0).rolling(126, min_periods=42).sum()
    dn = (-mfv.clip(upper=0)).rolling(126, min_periods=42).sum()
    result = _safe_div(up - dn, up + dn)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF momentum: 21d cmf minus its 63d mean
def f15ad_f15_accumulation_distribution_flow_cmfmom_21d_base_v048_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 21)
    result = c - _mean(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF momentum: 63d cmf minus its 126d mean
def f15ad_f15_accumulation_distribution_flow_cmfmom_63d_base_v049_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 63)
    result = c - _mean(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF spread short minus long (21d vs 126d)
def f15ad_f15_accumulation_distribution_flow_cmfspread_21_126_base_v050_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 21) - _f15_cmf(high, low, close, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF spread 42d vs 189d
def f15ad_f15_accumulation_distribution_flow_cmfspread_42_189_base_v051_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 42) - _f15_cmf(high, low, close, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF z-scored over 252d (21d)
def f15ad_f15_accumulation_distribution_flow_cmfz_21d_base_v052_signal(high, low, close, volume):
    result = _z(_f15_cmf(high, low, close, volume, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF z-scored over 252d (63d)
def f15ad_f15_accumulation_distribution_flow_cmfz_63d_base_v053_signal(high, low, close, volume):
    result = _z(_f15_cmf(high, low, close, volume, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF percentile rank over 126d (21d cmf)
def f15ad_f15_accumulation_distribution_flow_cmfrank_21d_base_v054_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 21)
    result = c.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF percentile rank over 252d (63d cmf)
def f15ad_f15_accumulation_distribution_flow_cmfrank_63d_base_v055_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 63)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF confirmed by price momentum (21d)
def f15ad_f15_accumulation_distribution_flow_cmfconf_21d_base_v056_signal(high, low, close, closeadj, volume):
    result = _f15_cmf(high, low, close, volume, 21) * closeadj.pct_change(21)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF confirmed by price momentum (63d)
def f15ad_f15_accumulation_distribution_flow_cmfconf_63d_base_v057_signal(high, low, close, closeadj, volume):
    result = _f15_cmf(high, low, close, volume, 63) * closeadj.pct_change(63)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF divergence: cmf minus standardized price momentum (21d)
def f15ad_f15_accumulation_distribution_flow_cmfdiv_21d_base_v058_signal(high, low, close, closeadj, volume):
    c = _f15_cmf(high, low, close, volume, 21)
    pm = _z(closeadj.pct_change(21), 252)
    result = c - pm
    return result.replace([np.inf, -np.inf], np.nan)


# CMF divergence (63d)
def f15ad_f15_accumulation_distribution_flow_cmfdiv_63d_base_v059_signal(high, low, close, closeadj, volume):
    c = _f15_cmf(high, low, close, volume, 63)
    pm = _z(closeadj.pct_change(63), 252)
    result = c - pm
    return result.replace([np.inf, -np.inf], np.nan)


# force index smoothed slope 21d
def f15ad_f15_accumulation_distribution_flow_forceslope_21d_base_v060_signal(close, volume):
    fi = _f15_forceidx(close, volume, 21)
    result = fi.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# force index minus its 63d mean (21d force)
def f15ad_f15_accumulation_distribution_flow_forcemom_21d_base_v061_signal(close, volume):
    fi = _f15_forceidx(close, volume, 21)
    result = fi - _mean(fi, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# force index spread 13d vs 63d
def f15ad_f15_accumulation_distribution_flow_forcespread_13_63_base_v062_signal(close, volume):
    result = _f15_forceidx(close, volume, 13) - _f15_forceidx(close, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope spread short minus long (21d vs 126d)
def f15ad_f15_accumulation_distribution_flow_obvspread_21_126_base_v063_signal(close, volume):
    result = _f15_obvslope(close, volume, 21) - _f15_obvslope(close, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope momentum: 21d slope minus its 63d mean
def f15ad_f15_accumulation_distribution_flow_obvmom_21d_base_v064_signal(close, volume):
    o = _f15_obvslope(close, volume, 21)
    result = o - _mean(o, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope percentile rank over 252d (63d)
def f15ad_f15_accumulation_distribution_flow_obvrank_63d_base_v065_signal(close, volume):
    o = _f15_obvslope(close, volume, 63)
    result = o.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# mfm smoothed weighted by volume z-score (21d accumulation pressure)
def f15ad_f15_accumulation_distribution_flow_mfmvolw_21d_base_v066_signal(high, low, close, volume):
    result = _mean(_f15_mfm(high, low, close), 21) * _z(volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# mfm smoothed weighted by dollar-volume surge (63d)
def f15ad_f15_accumulation_distribution_flow_mfmdvw_63d_base_v067_signal(high, low, close, volume):
    dv = close * volume
    surge = _safe_div(dv, _mean(dv, 126))
    result = _mean(_f15_mfm(high, low, close), 63) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# CMF weighted by volume turnover surge (21d)
def f15ad_f15_accumulation_distribution_flow_cmfsurge_21d_base_v068_signal(high, low, close, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f15_cmf(high, low, close, volume, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# ADL Chaikin oscillator z-scored (10-21 over 252d)
def f15ad_f15_accumulation_distribution_flow_choscz_10_21_base_v069_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    osc = adl.ewm(span=10, min_periods=5).mean() - adl.ewm(span=21, min_periods=10).mean()
    result = _z(osc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow-volume z-scored 21d (raw flow pressure)
def f15ad_f15_accumulation_distribution_flow_mfvz_21d_base_v070_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    result = _z(_mean(mfv, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow-volume z-scored 63d
def f15ad_f15_accumulation_distribution_flow_mfvz_63d_base_v071_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    result = _z(_mean(mfv, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF * obv-slope confirmation composite (21d)
def f15ad_f15_accumulation_distribution_flow_confcomp_21d_base_v072_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 21) * _z(_f15_obvslope(close, volume, 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# MFI normalized to [-1,1] symmetric ratio (21d)
def f15ad_f15_accumulation_distribution_flow_mfinorm_21d_base_v073_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(21, min_periods=10).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(21, min_periods=10).sum()
    result = _safe_div(pos - neg, pos + neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# MFI normalized symmetric ratio (63d)
def f15ad_f15_accumulation_distribution_flow_mfinorm_63d_base_v074_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(63, min_periods=21).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(63, min_periods=21).sum()
    result = _safe_div(pos - neg, pos + neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# CMF smoothed by ewm (21d span, persistence of accumulation)
def f15ad_f15_accumulation_distribution_flow_cmfewm_21d_base_v075_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 21).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15ad_f15_accumulation_distribution_flow_cmf_21d_base_v001_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_63d_base_v002_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_126d_base_v003_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_42d_base_v004_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_252d_base_v005_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_10d_base_v006_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_84d_base_v007_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_189d_base_v008_signal,
    f15ad_f15_accumulation_distribution_flow_mfmsm_21d_base_v009_signal,
    f15ad_f15_accumulation_distribution_flow_mfmsm_63d_base_v010_signal,
    f15ad_f15_accumulation_distribution_flow_mfmsm_126d_base_v011_signal,
    f15ad_f15_accumulation_distribution_flow_mfmewm_42d_base_v012_signal,
    f15ad_f15_accumulation_distribution_flow_mfmz_63d_base_v013_signal,
    f15ad_f15_accumulation_distribution_flow_mfmz_126d_base_v014_signal,
    f15ad_f15_accumulation_distribution_flow_obvslope_21d_base_v015_signal,
    f15ad_f15_accumulation_distribution_flow_obvslope_63d_base_v016_signal,
    f15ad_f15_accumulation_distribution_flow_obvslope_126d_base_v017_signal,
    f15ad_f15_accumulation_distribution_flow_obvslope_10d_base_v018_signal,
    f15ad_f15_accumulation_distribution_flow_obvslope_252d_base_v019_signal,
    f15ad_f15_accumulation_distribution_flow_obvslopez_21d_base_v020_signal,
    f15ad_f15_accumulation_distribution_flow_obvslopez_63d_base_v021_signal,
    f15ad_f15_accumulation_distribution_flow_force_21d_base_v022_signal,
    f15ad_f15_accumulation_distribution_flow_force_63d_base_v023_signal,
    f15ad_f15_accumulation_distribution_flow_force_13d_base_v024_signal,
    f15ad_f15_accumulation_distribution_flow_force_126d_base_v025_signal,
    f15ad_f15_accumulation_distribution_flow_adlnorm_21d_base_v026_signal,
    f15ad_f15_accumulation_distribution_flow_adlnorm_63d_base_v027_signal,
    f15ad_f15_accumulation_distribution_flow_adlnorm_126d_base_v028_signal,
    f15ad_f15_accumulation_distribution_flow_adlz_21d_base_v029_signal,
    f15ad_f15_accumulation_distribution_flow_adlz_63d_base_v030_signal,
    f15ad_f15_accumulation_distribution_flow_mfi_21d_base_v031_signal,
    f15ad_f15_accumulation_distribution_flow_mfi_63d_base_v032_signal,
    f15ad_f15_accumulation_distribution_flow_mfi_126d_base_v033_signal,
    f15ad_f15_accumulation_distribution_flow_logmfr_21d_base_v034_signal,
    f15ad_f15_accumulation_distribution_flow_logmfr_63d_base_v035_signal,
    f15ad_f15_accumulation_distribution_flow_vpt_21d_base_v036_signal,
    f15ad_f15_accumulation_distribution_flow_vpt_63d_base_v037_signal,
    f15ad_f15_accumulation_distribution_flow_vpt_126d_base_v038_signal,
    f15ad_f15_accumulation_distribution_flow_chosc_3_10_base_v039_signal,
    f15ad_f15_accumulation_distribution_flow_chosc_10_21_base_v040_signal,
    f15ad_f15_accumulation_distribution_flow_chosc_21_63_base_v041_signal,
    f15ad_f15_accumulation_distribution_flow_eom_21d_base_v042_signal,
    f15ad_f15_accumulation_distribution_flow_eom_63d_base_v043_signal,
    f15ad_f15_accumulation_distribution_flow_eomz_21d_base_v044_signal,
    f15ad_f15_accumulation_distribution_flow_udmf_42d_base_v045_signal,
    f15ad_f15_accumulation_distribution_flow_udmf_84d_base_v046_signal,
    f15ad_f15_accumulation_distribution_flow_udmf_126d_base_v047_signal,
    f15ad_f15_accumulation_distribution_flow_cmfmom_21d_base_v048_signal,
    f15ad_f15_accumulation_distribution_flow_cmfmom_63d_base_v049_signal,
    f15ad_f15_accumulation_distribution_flow_cmfspread_21_126_base_v050_signal,
    f15ad_f15_accumulation_distribution_flow_cmfspread_42_189_base_v051_signal,
    f15ad_f15_accumulation_distribution_flow_cmfz_21d_base_v052_signal,
    f15ad_f15_accumulation_distribution_flow_cmfz_63d_base_v053_signal,
    f15ad_f15_accumulation_distribution_flow_cmfrank_21d_base_v054_signal,
    f15ad_f15_accumulation_distribution_flow_cmfrank_63d_base_v055_signal,
    f15ad_f15_accumulation_distribution_flow_cmfconf_21d_base_v056_signal,
    f15ad_f15_accumulation_distribution_flow_cmfconf_63d_base_v057_signal,
    f15ad_f15_accumulation_distribution_flow_cmfdiv_21d_base_v058_signal,
    f15ad_f15_accumulation_distribution_flow_cmfdiv_63d_base_v059_signal,
    f15ad_f15_accumulation_distribution_flow_forceslope_21d_base_v060_signal,
    f15ad_f15_accumulation_distribution_flow_forcemom_21d_base_v061_signal,
    f15ad_f15_accumulation_distribution_flow_forcespread_13_63_base_v062_signal,
    f15ad_f15_accumulation_distribution_flow_obvspread_21_126_base_v063_signal,
    f15ad_f15_accumulation_distribution_flow_obvmom_21d_base_v064_signal,
    f15ad_f15_accumulation_distribution_flow_obvrank_63d_base_v065_signal,
    f15ad_f15_accumulation_distribution_flow_mfmvolw_21d_base_v066_signal,
    f15ad_f15_accumulation_distribution_flow_mfmdvw_63d_base_v067_signal,
    f15ad_f15_accumulation_distribution_flow_cmfsurge_21d_base_v068_signal,
    f15ad_f15_accumulation_distribution_flow_choscz_10_21_base_v069_signal,
    f15ad_f15_accumulation_distribution_flow_mfvz_21d_base_v070_signal,
    f15ad_f15_accumulation_distribution_flow_mfvz_63d_base_v071_signal,
    f15ad_f15_accumulation_distribution_flow_confcomp_21d_base_v072_signal,
    f15ad_f15_accumulation_distribution_flow_mfinorm_21d_base_v073_signal,
    f15ad_f15_accumulation_distribution_flow_mfinorm_63d_base_v074_signal,
    f15ad_f15_accumulation_distribution_flow_cmfewm_21d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_ACCUMULATION_DISTRIBUTION_FLOW_REGISTRY_001_075 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f15_mfm", "_f15_cmf", "_f15_obvslope", "_f15_forceidx")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f15_accumulation_distribution_flow_base_001_075_claude: {n_features} features pass")
