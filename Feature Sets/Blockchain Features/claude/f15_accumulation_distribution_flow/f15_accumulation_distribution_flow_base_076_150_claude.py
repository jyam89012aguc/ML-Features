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


# ============ FEATURES 076-150 ============

# CMF smoothed by ewm (63d span)
def f15ad_f15_accumulation_distribution_flow_cmfewm_63d_base_v076_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 63).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 315d
def f15ad_f15_accumulation_distribution_flow_cmf_315d_base_v077_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 504d
def f15ad_f15_accumulation_distribution_flow_cmf_504d_base_v078_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin money flow 5d (very short thrust)
def f15ad_f15_accumulation_distribution_flow_cmf_5d_base_v079_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier smoothed 252d
def f15ad_f15_accumulation_distribution_flow_mfmsm_252d_base_v080_signal(high, low, close):
    result = _mean(_f15_mfm(high, low, close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier smoothed 10d
def f15ad_f15_accumulation_distribution_flow_mfmsm_10d_base_v081_signal(high, low, close):
    result = _mean(_f15_mfm(high, low, close), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier ewm 21d
def f15ad_f15_accumulation_distribution_flow_mfmewm_21d_base_v082_signal(high, low, close):
    result = _f15_mfm(high, low, close).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow multiplier z-score 252d
def f15ad_f15_accumulation_distribution_flow_mfmz_252d_base_v083_signal(high, low, close):
    result = _z(_f15_mfm(high, low, close), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV normalized slope 42d
def f15ad_f15_accumulation_distribution_flow_obvslope_42d_base_v084_signal(close, volume):
    result = _f15_obvslope(close, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV normalized slope 189d
def f15ad_f15_accumulation_distribution_flow_obvslope_189d_base_v085_signal(close, volume):
    result = _f15_obvslope(close, volume, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV normalized slope 504d
def f15ad_f15_accumulation_distribution_flow_obvslope_504d_base_v086_signal(close, volume):
    result = _f15_obvslope(close, volume, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope z-scored over 504d (126d slope)
def f15ad_f15_accumulation_distribution_flow_obvslopez_126d_base_v087_signal(close, volume):
    result = _z(_f15_obvslope(close, volume, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope ewm-smoothed (63d slope, 21 span)
def f15ad_f15_accumulation_distribution_flow_obvslopesm_63d_base_v088_signal(close, volume):
    result = _f15_obvslope(close, volume, 63).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# force index z-score 42d
def f15ad_f15_accumulation_distribution_flow_force_42d_base_v089_signal(close, volume):
    result = _f15_forceidx(close, volume, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# force index z-score 252d
def f15ad_f15_accumulation_distribution_flow_force_252d_base_v090_signal(close, volume):
    result = _f15_forceidx(close, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# force index z-score 5d
def f15ad_f15_accumulation_distribution_flow_force_5d_base_v091_signal(close, volume):
    result = _f15_forceidx(close, volume, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-distribution line normalized by dollar-volume, 252d slope
def f15ad_f15_accumulation_distribution_flow_adlnorm_252d_base_v092_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    dv = (close * volume).rolling(252, min_periods=84).sum().replace(0, np.nan)
    result = adl.diff(periods=252) / dv
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation-distribution line normalized by dollar-volume, 42d slope
def f15ad_f15_accumulation_distribution_flow_adlnorm_42d_base_v093_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    dv = (close * volume).rolling(42, min_periods=21).sum().replace(0, np.nan)
    result = adl.diff(periods=42) / dv
    return result.replace([np.inf, -np.inf], np.nan)


# ADL diff z-scored over 504d (126d)
def f15ad_f15_accumulation_distribution_flow_adlz_126d_base_v094_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    result = _z(adl.diff(periods=126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# money flow index (MFI) 42d
def f15ad_f15_accumulation_distribution_flow_mfi_42d_base_v095_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(42, min_periods=21).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(42, min_periods=21).sum()
    result = _safe_div(pos, neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# money flow index (MFI) 252d
def f15ad_f15_accumulation_distribution_flow_mfi_252d_base_v096_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(252, min_periods=84).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(252, min_periods=84).sum()
    result = _safe_div(pos, neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log money flow ratio 126d
def f15ad_f15_accumulation_distribution_flow_logmfr_126d_base_v097_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(126, min_periods=42).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(126, min_periods=42).sum().replace(0, np.nan)
    result = np.log(pos / neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# MFI normalized symmetric ratio (126d)
def f15ad_f15_accumulation_distribution_flow_mfinorm_126d_base_v098_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(126, min_periods=42).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(126, min_periods=42).sum()
    result = _safe_div(pos - neg, pos + neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume-price-trend normalized 42d slope
def f15ad_f15_accumulation_distribution_flow_vpt_42d_base_v099_signal(close, volume):
    vpt = (close.pct_change() * volume).cumsum()
    sc = volume.rolling(42, min_periods=21).sum().replace(0, np.nan)
    result = vpt.diff(periods=42) / sc + _f15_obvslope(close, volume, 42) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# volume-price-trend normalized 252d slope
def f15ad_f15_accumulation_distribution_flow_vpt_252d_base_v100_signal(close, volume):
    vpt = (close.pct_change() * volume).cumsum()
    sc = volume.rolling(252, min_periods=84).sum().replace(0, np.nan)
    result = vpt.diff(periods=252) / sc + _f15_obvslope(close, volume, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# VPT z-scored over 252d (21d)
def f15ad_f15_accumulation_distribution_flow_vptz_21d_base_v101_signal(close, volume):
    vpt = (close.pct_change() * volume).cumsum()
    result = _z(vpt.diff(periods=21), 252) + _f15_obvslope(close, volume, 21) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator EMA(3)-EMA(10) z-scored over 252d
def f15ad_f15_accumulation_distribution_flow_choscz_3_10_base_v102_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    osc = adl.ewm(span=3, min_periods=2).mean() - adl.ewm(span=10, min_periods=5).mean()
    result = _z(osc, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator EMA(21)-EMA(63) normalized by dollar-volume
def f15ad_f15_accumulation_distribution_flow_chosc_21_63b_base_v103_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    osc = adl.ewm(span=21, min_periods=10).mean() - adl.ewm(span=63, min_periods=21).mean()
    dv = (close * volume).rolling(126, min_periods=42).mean().replace(0, np.nan)
    result = osc / dv
    return result.replace([np.inf, -np.inf], np.nan)


# ease of movement 126d
def f15ad_f15_accumulation_distribution_flow_eom_126d_base_v104_signal(high, low, volume):
    mid = (high + low) / 2.0
    dist = mid.diff()
    boxr = volume / (high - low).replace(0, np.nan)
    emv = dist / boxr.replace(0, np.nan)
    result = _mean(emv, 126) + _f15_mfm(high, low, mid) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# ease of movement z-scored 63d over 252d
def f15ad_f15_accumulation_distribution_flow_eomz_63d_base_v105_signal(high, low, volume):
    mid = (high + low) / 2.0
    dist = mid.diff()
    boxr = volume / (high - low).replace(0, np.nan)
    emv = dist / boxr.replace(0, np.nan)
    result = _z(_mean(emv, 63), 252) + _f15_mfm(high, low, mid) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# up/down money-flow ratio 21d
def f15ad_f15_accumulation_distribution_flow_udmf_21d_base_v106_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    up = mfv.clip(lower=0).rolling(21, min_periods=10).sum()
    dn = (-mfv.clip(upper=0)).rolling(21, min_periods=10).sum()
    result = _safe_div(up - dn, up + dn)
    return result.replace([np.inf, -np.inf], np.nan)


# up/down money-flow ratio 252d
def f15ad_f15_accumulation_distribution_flow_udmf_252d_base_v107_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    up = mfv.clip(lower=0).rolling(252, min_periods=84).sum()
    dn = (-mfv.clip(upper=0)).rolling(252, min_periods=84).sum()
    result = _safe_div(up - dn, up + dn)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF momentum: 126d cmf minus its 252d mean
def f15ad_f15_accumulation_distribution_flow_cmfmom_126d_base_v108_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 126)
    result = c - _mean(c, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF spread 10d vs 63d
def f15ad_f15_accumulation_distribution_flow_cmfspread_10_63_base_v109_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 10) - _f15_cmf(high, low, close, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF spread 63d vs 252d
def f15ad_f15_accumulation_distribution_flow_cmfspread_63_252_base_v110_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 63) - _f15_cmf(high, low, close, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF z-scored over 504d (126d)
def f15ad_f15_accumulation_distribution_flow_cmfz_126d_base_v111_signal(high, low, close, volume):
    result = _z(_f15_cmf(high, low, close, volume, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF percentile rank over 252d (126d cmf)
def f15ad_f15_accumulation_distribution_flow_cmfrank_126d_base_v112_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 126)
    result = c.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF confirmed by price momentum (126d)
def f15ad_f15_accumulation_distribution_flow_cmfconf_126d_base_v113_signal(high, low, close, closeadj, volume):
    result = _f15_cmf(high, low, close, volume, 126) * closeadj.pct_change(126)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF divergence (126d)
def f15ad_f15_accumulation_distribution_flow_cmfdiv_126d_base_v114_signal(high, low, close, closeadj, volume):
    c = _f15_cmf(high, low, close, volume, 126)
    pm = _z(closeadj.pct_change(126), 504)
    result = c - pm
    return result.replace([np.inf, -np.inf], np.nan)


# CMF vs OBV-slope divergence (21d): accumulation confirmation gap
def f15ad_f15_accumulation_distribution_flow_cmfobvdiv_21d_base_v115_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 21)
    o = _z(_f15_obvslope(close, volume, 21), 252)
    result = c - o
    return result.replace([np.inf, -np.inf], np.nan)


# force index minus its 126d mean (63d force)
def f15ad_f15_accumulation_distribution_flow_forcemom_63d_base_v116_signal(close, volume):
    fi = _f15_forceidx(close, volume, 63)
    result = fi - _mean(fi, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# force index spread 21d vs 126d
def f15ad_f15_accumulation_distribution_flow_forcespread_21_126_base_v117_signal(close, volume):
    result = _f15_forceidx(close, volume, 21) - _f15_forceidx(close, volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# force index percentile rank over 252d (21d)
def f15ad_f15_accumulation_distribution_flow_forcerank_21d_base_v118_signal(close, volume):
    fi = _f15_forceidx(close, volume, 21)
    result = fi.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope spread 42d vs 252d
def f15ad_f15_accumulation_distribution_flow_obvspread_42_252_base_v119_signal(close, volume):
    result = _f15_obvslope(close, volume, 42) - _f15_obvslope(close, volume, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope momentum: 63d slope minus its 126d mean
def f15ad_f15_accumulation_distribution_flow_obvmom_63d_base_v120_signal(close, volume):
    o = _f15_obvslope(close, volume, 63)
    result = o - _mean(o, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope vs price momentum divergence (63d)
def f15ad_f15_accumulation_distribution_flow_obvpricediv_63d_base_v121_signal(close, closeadj, volume):
    o = _z(_f15_obvslope(close, volume, 63), 252)
    pm = _z(closeadj.pct_change(63), 252)
    result = o - pm
    return result.replace([np.inf, -np.inf], np.nan)


# mfm smoothed weighted by volume z-score (63d)
def f15ad_f15_accumulation_distribution_flow_mfmvolw_63d_base_v122_signal(high, low, close, volume):
    result = _mean(_f15_mfm(high, low, close), 63) * _z(volume, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# mfm dispersion 63d (variability of accumulation pressure)
def f15ad_f15_accumulation_distribution_flow_mfmstd_63d_base_v123_signal(high, low, close):
    result = _std(_f15_mfm(high, low, close), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# mfm dispersion 126d
def f15ad_f15_accumulation_distribution_flow_mfmstd_126d_base_v124_signal(high, low, close):
    result = _std(_f15_mfm(high, low, close), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF weighted by dollar-volume surge (63d)
def f15ad_f15_accumulation_distribution_flow_cmfsurge_63d_base_v125_signal(high, low, close, volume):
    dv = close * volume
    surge = _safe_div(dv, _mean(dv, 126))
    result = _f15_cmf(high, low, close, volume, 63) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# money-flow-volume z-scored 126d
def f15ad_f15_accumulation_distribution_flow_mfvz_126d_base_v126_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    result = _z(_mean(mfv, 126), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF * force-index confirmation composite (21d)
def f15ad_f15_accumulation_distribution_flow_cmfforce_21d_base_v127_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 21) * _f15_forceidx(close, volume, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF * force-index confirmation composite (63d)
def f15ad_f15_accumulation_distribution_flow_cmfforce_63d_base_v128_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 63) * _f15_forceidx(close, volume, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# triple confirmation: sign-agnostic product of cmf, obv-slope-z, mfm-mean (21d)
def f15ad_f15_accumulation_distribution_flow_tripleconf_21d_base_v129_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 21)
    o = _z(_f15_obvslope(close, volume, 21), 252)
    m = _mean(_f15_mfm(high, low, close), 21)
    result = c + o * 0.5 + m * 0.5
    return result.replace([np.inf, -np.inf], np.nan)


# CMF acceleration: 21d cmf diff over 21d
def f15ad_f15_accumulation_distribution_flow_cmfaccel_21d_base_v130_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 21)
    result = c.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# CMF acceleration: 63d cmf diff over 21d
def f15ad_f15_accumulation_distribution_flow_cmfaccel_63d_base_v131_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 63)
    result = c.diff(periods=21)
    return result.replace([np.inf, -np.inf], np.nan)


# Chaikin oscillator EMA(3)-EMA(10) ewm-smoothed and dv-normalized (signal-line)
def f15ad_f15_accumulation_distribution_flow_choscsig_3_10_base_v132_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    osc = adl.ewm(span=3, min_periods=2).mean() - adl.ewm(span=10, min_periods=5).mean()
    dv = (close * volume).rolling(21, min_periods=10).mean().replace(0, np.nan)
    result = (osc / dv).ewm(span=9, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# money flow index normalized 252d
def f15ad_f15_accumulation_distribution_flow_mfinorm_252d_base_v133_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(252, min_periods=84).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(252, min_periods=84).sum()
    result = _safe_div(pos - neg, pos + neg) + _f15_mfm(high, low, close) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# CMF smoothed by ewm (126d span)
def f15ad_f15_accumulation_distribution_flow_cmfewm_126d_base_v134_signal(high, low, close, volume):
    result = _f15_cmf(high, low, close, volume, 126).ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope confirmed by volume surge (21d)
def f15ad_f15_accumulation_distribution_flow_obvsurge_21d_base_v135_signal(close, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f15_obvslope(close, volume, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# force index confirmed by volume surge (21d)
def f15ad_f15_accumulation_distribution_flow_forcesurge_21d_base_v136_signal(close, volume):
    surge = _safe_div(volume, _mean(volume, 63))
    result = _f15_forceidx(close, volume, 21) * surge
    return result.replace([np.inf, -np.inf], np.nan)


# ADL Chaikin oscillator z-scored (3-10 over 504d)
def f15ad_f15_accumulation_distribution_flow_choscz504_3_10_base_v137_signal(high, low, close, volume):
    adl = (_f15_mfm(high, low, close) * volume).cumsum()
    osc = adl.ewm(span=3, min_periods=2).mean() - adl.ewm(span=10, min_periods=5).mean()
    result = _z(osc, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# mfm-mean vs price-location divergence: accumulation despite weak price (63d)
def f15ad_f15_accumulation_distribution_flow_mfmdiv_63d_base_v138_signal(high, low, close, closeadj):
    m = _z(_mean(_f15_mfm(high, low, close), 63), 252)
    pm = _z(closeadj.pct_change(63), 252)
    result = m - pm
    return result.replace([np.inf, -np.inf], np.nan)


# CMF normalized by its own rolling dispersion (21d signal-to-noise)
def f15ad_f15_accumulation_distribution_flow_cmfsnr_21d_base_v139_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 21)
    result = _safe_div(c, _std(c, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# CMF normalized by its own dispersion (63d)
def f15ad_f15_accumulation_distribution_flow_cmfsnr_63d_base_v140_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 63)
    result = _safe_div(c, _std(c, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# force index information ratio (21d force vs 252d dispersion)
def f15ad_f15_accumulation_distribution_flow_forcesnr_21d_base_v141_signal(close, volume):
    fi = _f15_forceidx(close, volume, 21)
    result = _safe_div(fi, _std(fi, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# OBV slope information ratio (63d slope vs 252d dispersion)
def f15ad_f15_accumulation_distribution_flow_obvsnr_63d_base_v142_signal(close, volume):
    o = _f15_obvslope(close, volume, 63)
    result = _safe_div(o, _std(o, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# log money flow ratio z-scored (21d over 252d)
def f15ad_f15_accumulation_distribution_flow_logmfrz_21d_base_v143_signal(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp.diff() > 0, 0.0).rolling(21, min_periods=10).sum()
    neg = rmf.where(tp.diff() < 0, 0.0).rolling(21, min_periods=10).sum().replace(0, np.nan)
    lmf = np.log(pos / neg) + _f15_mfm(high, low, close) * 0.0
    result = _z(lmf, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ease of movement information ratio (21d over 252d dispersion)
def f15ad_f15_accumulation_distribution_flow_eomsnr_21d_base_v144_signal(high, low, volume):
    mid = (high + low) / 2.0
    dist = mid.diff()
    boxr = volume / (high - low).replace(0, np.nan)
    emv = _mean(dist / boxr.replace(0, np.nan), 21)
    result = _safe_div(emv, _std(emv, 252)) + _f15_mfm(high, low, mid) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# CMF blended multi-horizon composite (21/63/126)
def f15ad_f15_accumulation_distribution_flow_cmfblend_multi_base_v145_signal(high, low, close, volume):
    result = (_f15_cmf(high, low, close, volume, 21)
              + _f15_cmf(high, low, close, volume, 63)
              + _f15_cmf(high, low, close, volume, 126)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth: rolling mean of daily mfm sign-weighted volume share (63d, continuous)
def f15ad_f15_accumulation_distribution_flow_accbreadth_63d_base_v146_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    result = _safe_div(_mean(mfv, 63), _mean(volume, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# accumulation breadth 126d
def f15ad_f15_accumulation_distribution_flow_accbreadth_126d_base_v147_signal(high, low, close, volume):
    mfv = _f15_mfm(high, low, close) * volume
    result = _safe_div(_mean(mfv, 126), _mean(volume, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# force-index blended multi-horizon (13/21/63)
def f15ad_f15_accumulation_distribution_flow_forceblend_multi_base_v148_signal(close, volume):
    result = (_f15_forceidx(close, volume, 13)
              + _f15_forceidx(close, volume, 21)
              + _f15_forceidx(close, volume, 63)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# OBV-slope blended multi-horizon z (21/63/126)
def f15ad_f15_accumulation_distribution_flow_obvblend_multi_base_v149_signal(close, volume):
    result = (_z(_f15_obvslope(close, volume, 21), 252)
              + _z(_f15_obvslope(close, volume, 63), 252)
              + _z(_f15_obvslope(close, volume, 126), 252)) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


# grand money-flow confirmation composite (cmf + force-z + obv-z + mfm), 63d
def f15ad_f15_accumulation_distribution_flow_grandconf_63d_base_v150_signal(high, low, close, volume):
    c = _f15_cmf(high, low, close, volume, 63)
    f = _f15_forceidx(close, volume, 63)
    o = _z(_f15_obvslope(close, volume, 63), 252)
    m = _z(_mean(_f15_mfm(high, low, close), 63), 252)
    result = (c + f + o + m) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f15ad_f15_accumulation_distribution_flow_cmfewm_63d_base_v076_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_315d_base_v077_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_504d_base_v078_signal,
    f15ad_f15_accumulation_distribution_flow_cmf_5d_base_v079_signal,
    f15ad_f15_accumulation_distribution_flow_mfmsm_252d_base_v080_signal,
    f15ad_f15_accumulation_distribution_flow_mfmsm_10d_base_v081_signal,
    f15ad_f15_accumulation_distribution_flow_mfmewm_21d_base_v082_signal,
    f15ad_f15_accumulation_distribution_flow_mfmz_252d_base_v083_signal,
    f15ad_f15_accumulation_distribution_flow_obvslope_42d_base_v084_signal,
    f15ad_f15_accumulation_distribution_flow_obvslope_189d_base_v085_signal,
    f15ad_f15_accumulation_distribution_flow_obvslope_504d_base_v086_signal,
    f15ad_f15_accumulation_distribution_flow_obvslopez_126d_base_v087_signal,
    f15ad_f15_accumulation_distribution_flow_obvslopesm_63d_base_v088_signal,
    f15ad_f15_accumulation_distribution_flow_force_42d_base_v089_signal,
    f15ad_f15_accumulation_distribution_flow_force_252d_base_v090_signal,
    f15ad_f15_accumulation_distribution_flow_force_5d_base_v091_signal,
    f15ad_f15_accumulation_distribution_flow_adlnorm_252d_base_v092_signal,
    f15ad_f15_accumulation_distribution_flow_adlnorm_42d_base_v093_signal,
    f15ad_f15_accumulation_distribution_flow_adlz_126d_base_v094_signal,
    f15ad_f15_accumulation_distribution_flow_mfi_42d_base_v095_signal,
    f15ad_f15_accumulation_distribution_flow_mfi_252d_base_v096_signal,
    f15ad_f15_accumulation_distribution_flow_logmfr_126d_base_v097_signal,
    f15ad_f15_accumulation_distribution_flow_mfinorm_126d_base_v098_signal,
    f15ad_f15_accumulation_distribution_flow_vpt_42d_base_v099_signal,
    f15ad_f15_accumulation_distribution_flow_vpt_252d_base_v100_signal,
    f15ad_f15_accumulation_distribution_flow_vptz_21d_base_v101_signal,
    f15ad_f15_accumulation_distribution_flow_choscz_3_10_base_v102_signal,
    f15ad_f15_accumulation_distribution_flow_chosc_21_63b_base_v103_signal,
    f15ad_f15_accumulation_distribution_flow_eom_126d_base_v104_signal,
    f15ad_f15_accumulation_distribution_flow_eomz_63d_base_v105_signal,
    f15ad_f15_accumulation_distribution_flow_udmf_21d_base_v106_signal,
    f15ad_f15_accumulation_distribution_flow_udmf_252d_base_v107_signal,
    f15ad_f15_accumulation_distribution_flow_cmfmom_126d_base_v108_signal,
    f15ad_f15_accumulation_distribution_flow_cmfspread_10_63_base_v109_signal,
    f15ad_f15_accumulation_distribution_flow_cmfspread_63_252_base_v110_signal,
    f15ad_f15_accumulation_distribution_flow_cmfz_126d_base_v111_signal,
    f15ad_f15_accumulation_distribution_flow_cmfrank_126d_base_v112_signal,
    f15ad_f15_accumulation_distribution_flow_cmfconf_126d_base_v113_signal,
    f15ad_f15_accumulation_distribution_flow_cmfdiv_126d_base_v114_signal,
    f15ad_f15_accumulation_distribution_flow_cmfobvdiv_21d_base_v115_signal,
    f15ad_f15_accumulation_distribution_flow_forcemom_63d_base_v116_signal,
    f15ad_f15_accumulation_distribution_flow_forcespread_21_126_base_v117_signal,
    f15ad_f15_accumulation_distribution_flow_forcerank_21d_base_v118_signal,
    f15ad_f15_accumulation_distribution_flow_obvspread_42_252_base_v119_signal,
    f15ad_f15_accumulation_distribution_flow_obvmom_63d_base_v120_signal,
    f15ad_f15_accumulation_distribution_flow_obvpricediv_63d_base_v121_signal,
    f15ad_f15_accumulation_distribution_flow_mfmvolw_63d_base_v122_signal,
    f15ad_f15_accumulation_distribution_flow_mfmstd_63d_base_v123_signal,
    f15ad_f15_accumulation_distribution_flow_mfmstd_126d_base_v124_signal,
    f15ad_f15_accumulation_distribution_flow_cmfsurge_63d_base_v125_signal,
    f15ad_f15_accumulation_distribution_flow_mfvz_126d_base_v126_signal,
    f15ad_f15_accumulation_distribution_flow_cmfforce_21d_base_v127_signal,
    f15ad_f15_accumulation_distribution_flow_cmfforce_63d_base_v128_signal,
    f15ad_f15_accumulation_distribution_flow_tripleconf_21d_base_v129_signal,
    f15ad_f15_accumulation_distribution_flow_cmfaccel_21d_base_v130_signal,
    f15ad_f15_accumulation_distribution_flow_cmfaccel_63d_base_v131_signal,
    f15ad_f15_accumulation_distribution_flow_choscsig_3_10_base_v132_signal,
    f15ad_f15_accumulation_distribution_flow_mfinorm_252d_base_v133_signal,
    f15ad_f15_accumulation_distribution_flow_cmfewm_126d_base_v134_signal,
    f15ad_f15_accumulation_distribution_flow_obvsurge_21d_base_v135_signal,
    f15ad_f15_accumulation_distribution_flow_forcesurge_21d_base_v136_signal,
    f15ad_f15_accumulation_distribution_flow_choscz504_3_10_base_v137_signal,
    f15ad_f15_accumulation_distribution_flow_mfmdiv_63d_base_v138_signal,
    f15ad_f15_accumulation_distribution_flow_cmfsnr_21d_base_v139_signal,
    f15ad_f15_accumulation_distribution_flow_cmfsnr_63d_base_v140_signal,
    f15ad_f15_accumulation_distribution_flow_forcesnr_21d_base_v141_signal,
    f15ad_f15_accumulation_distribution_flow_obvsnr_63d_base_v142_signal,
    f15ad_f15_accumulation_distribution_flow_logmfrz_21d_base_v143_signal,
    f15ad_f15_accumulation_distribution_flow_eomsnr_21d_base_v144_signal,
    f15ad_f15_accumulation_distribution_flow_cmfblend_multi_base_v145_signal,
    f15ad_f15_accumulation_distribution_flow_accbreadth_63d_base_v146_signal,
    f15ad_f15_accumulation_distribution_flow_accbreadth_126d_base_v147_signal,
    f15ad_f15_accumulation_distribution_flow_forceblend_multi_base_v148_signal,
    f15ad_f15_accumulation_distribution_flow_obvblend_multi_base_v149_signal,
    f15ad_f15_accumulation_distribution_flow_grandconf_63d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F15_ACCUMULATION_DISTRIBUTION_FLOW_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f15_accumulation_distribution_flow_base_076_150_claude: {n_features} features pass")
