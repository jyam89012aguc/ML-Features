import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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


# ===== folder domain primitives: range-based volatility estimators =====
def _f11re_logsq(num, den):
    r = np.log(num.replace(0, np.nan) / den.replace(0, np.nan))
    return r * r


def _f11re_parkinson(high, low, w):
    hl = _f11re_logsq(high, low)
    var = hl.rolling(w, min_periods=max(1, w // 2)).mean() / (4.0 * np.log(2.0))
    return np.sqrt(var)


def _f11re_garman_klass(open_, high, low, close, w):
    term = 0.5 * _f11re_logsq(high, low) - (2.0 * np.log(2.0) - 1.0) * _f11re_logsq(close, open_)
    var = term.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sqrt(var.clip(lower=0))


def _f11re_rogers_satchell(open_, high, low, close, w):
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    term = hc * ho + lc * lo
    var = term.rolling(w, min_periods=max(1, w // 2)).mean()
    return np.sqrt(var.clip(lower=0))


def _f11re_overnight_var(open_, close, w):
    on = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    return on.rolling(w, min_periods=max(1, w // 2)).var()


def _f11re_open_close_var(open_, close, w):
    oc = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    return oc.rolling(w, min_periods=max(1, w // 2)).var()


def _f11re_yang_zhang(open_, high, low, close, w):
    on = np.log(open_.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    oc = np.log(close.replace(0, np.nan) / open_.replace(0, np.nan))
    von = on.rolling(w, min_periods=max(1, w // 2)).var()
    voc = oc.rolling(w, min_periods=max(1, w // 2)).var()
    hc = np.log(high.replace(0, np.nan) / close.replace(0, np.nan))
    ho = np.log(high.replace(0, np.nan) / open_.replace(0, np.nan))
    lc = np.log(low.replace(0, np.nan) / close.replace(0, np.nan))
    lo = np.log(low.replace(0, np.nan) / open_.replace(0, np.nan))
    rs = (hc * ho + lc * lo).rolling(w, min_periods=max(1, w // 2)).mean()
    k = 0.34 / (1.34 + (w + 1.0) / (w - 1.0))
    var = von + k * voc + (1.0 - k) * rs
    return np.sqrt(var.clip(lower=0))


def _f11re_true_range(high, low, close):
    pc = close.shift(1)
    a = (high - low).abs()
    b = (high - pc).abs()
    c = (low - pc).abs()
    return pd.concat([a, b, c], axis=1).max(axis=1)


def _f11re_atr(high, low, close, w):
    tr = _f11re_true_range(high, low, close)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _f11re_hl_range(high, low, close):
    return (high - low) / close.replace(0, np.nan)


# ============================================================
# --- volatility-cone positions (range-vol percentile across horizons) ---
# Parkinson 5d cone position vs 252d history
def f11re_f11_range_vol_estimators_parkcone_5d_base_v076_signal(high, low):
    p = _f11re_parkinson(high, low, 5)
    b = _rank(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 63d cone position vs 504d history
def f11re_f11_range_vol_estimators_parkcone_63d_base_v077_signal(high, low):
    p = _f11re_parkinson(high, low, 63)
    b = _rank(p, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 5d cone position vs 252d history
def f11re_f11_range_vol_estimators_gkcone_5d_base_v078_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 5)
    b = _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price 63d cone position vs 504d history (long-horizon range-vol percentile)
def f11re_f11_range_vol_estimators_atrcone_63d_base_v079_signal(high, low, close, closeadj):
    atrp = _f11re_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    b = _rank(atrp, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- upside vs downside range (semi-range) volatility ---
# upside range sigma 21d: Parkinson restricted to up-days (close>open)
def f11re_f11_range_vol_estimators_upsemirng_21d_base_v080_signal(open, high, low, close):
    upday = (close > open).astype(float)
    hl = _f11re_logsq(high, low) * upday
    var = hl.rolling(21, min_periods=10).sum() / (upday.rolling(21, min_periods=10).sum().replace(0, np.nan) * 4.0 * np.log(2.0))
    b = np.sqrt(var)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# downside range sigma 21d: Parkinson restricted to down-days (close<open)
def f11re_f11_range_vol_estimators_dnsemirng_21d_base_v081_signal(open, high, low, close):
    dnday = (close < open).astype(float)
    hl = _f11re_logsq(high, low) * dnday
    var = hl.rolling(21, min_periods=10).sum() / (dnday.rolling(21, min_periods=10).sum().replace(0, np.nan) * 4.0 * np.log(2.0))
    b = np.sqrt(var)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# semi-range skew: down-day range minus up-day range, normalized (downside range premium)
def f11re_f11_range_vol_estimators_semirngskew_63d_base_v082_signal(open, high, low, close):
    upday = (close > open).astype(float)
    dnday = (close < open).astype(float)
    hl = _f11re_logsq(high, low)
    uv = (hl * upday).rolling(63, min_periods=21).sum() / upday.rolling(63, min_periods=21).sum().replace(0, np.nan)
    dv = (hl * dnday).rolling(63, min_periods=21).sum() / dnday.rolling(63, min_periods=21).sum().replace(0, np.nan)
    b = (dv - uv) / (dv + uv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-vol asymmetry & shape ---
# upper-wick range share: (high-max(open,close)) vs full range, 21d (selling pressure)
def f11re_f11_range_vol_estimators_uwickshare_21d_base_v083_signal(open, high, low, close):
    upper = high - pd.concat([open, close], axis=1).max(axis=1)
    rng = (high - low)
    share = upper.rolling(21, min_periods=10).sum() / rng.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = share - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# lower-wick range share: (min(open,close)-low) vs full range, 21d (buying support)
def f11re_f11_range_vol_estimators_lwickshare_21d_base_v084_signal(open, high, low, close):
    lower = pd.concat([open, close], axis=1).min(axis=1) - low
    rng = (high - low)
    share = lower.rolling(21, min_periods=10).sum() / rng.rolling(21, min_periods=10).sum().replace(0, np.nan)
    b = share - 0.25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# body-vs-range: |close-open| / (high-low), 21d mean (directional conviction within range)
def f11re_f11_range_vol_estimators_bodyrng_21d_base_v085_signal(open, high, low, close):
    body = (close - open).abs()
    rng = (high - low)
    b = (body / rng.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-vol momentum & acceleration across estimators ---
# Parkinson 63d momentum: 21d change (range-vol trend)
def f11re_f11_range_vol_estimators_parkmom_63d_base_v086_signal(high, low):
    p = _f11re_parkinson(high, low, 63)
    b = p - p.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 63d momentum: 21d change
def f11re_f11_range_vol_estimators_gkmom_63d_base_v087_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 63)
    b = g - g.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price 63d momentum: 21d change (normalized by closeadj)
def f11re_f11_range_vol_estimators_atrmom_63d_base_v088_signal(high, low, close, closeadj):
    atrp = _f11re_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    b = atrp - atrp.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson log-acceleration: 21d ROC of the 21d Parkinson change (range-vol curvature)
def f11re_f11_range_vol_estimators_parkaccel_21d_base_v089_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    chg = p - p.shift(21)
    b = chg - chg.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-vol regime distance & compression/expansion ---
# Parkinson 21d distance to its 252d median (range-vol regime gap)
def f11re_f11_range_vol_estimators_parkregdist_base_v090_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    med = p.rolling(252, min_periods=126).median()
    b = p / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 21d distance to its 252d median
def f11re_f11_range_vol_estimators_gkregdist_base_v091_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 21)
    med = g.rolling(252, min_periods=126).median()
    b = g / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Bollinger-style range bandwidth: 21d ATR/price bandwidth vs its 252d range (squeeze)
def f11re_f11_range_vol_estimators_atrsqueeze_base_v092_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    lo = atrp.rolling(252, min_periods=126).min()
    hi = atrp.rolling(252, min_periods=126).max()
    b = (atrp - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol compression streak: consecutive days Parkinson21 below its 63d mean (coiling)
def f11re_f11_range_vol_estimators_parkcompress_base_v093_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    base = p.rolling(63, min_periods=21).mean()
    comp = (p < base).astype(float)
    grp = (comp == 0).cumsum()
    streak = comp.groupby(grp).cumsum()
    tight = (1.0 - p / base.replace(0, np.nan)).clip(lower=0)
    b = streak / 21.0 + tight.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol expansion days: count of Parkinson21 > 1.5x its 63d mean over 63d (blowup freq)
def f11re_f11_range_vol_estimators_parkexpcnt_base_v094_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    base = p.rolling(63, min_periods=21).mean()
    blow = (p > 1.5 * base).astype(float)
    cnt = blow.rolling(63, min_periods=21).sum()
    mag = (p / base.replace(0, np.nan) - 1.0).clip(lower=0).rolling(21, min_periods=10).mean()
    b = cnt + 5.0 * mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- vol-of-vol on range estimators ---
# Parkinson vol-of-vol 126d (instability of range-vol)
def f11re_f11_range_vol_estimators_parkvov_126d_base_v095_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    b = p.rolling(126, min_periods=63).std() / p.rolling(126, min_periods=63).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK vol-of-vol 63d
def f11re_f11_range_vol_estimators_gkvov_63d_base_v096_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 21)
    b = g.rolling(63, min_periods=21).std() / g.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price vol-of-vol 63d
def f11re_f11_range_vol_estimators_atrvov_63d_base_v097_signal(high, low, close):
    atrp = _f11re_atr(high, low, close, 21) / close.replace(0, np.nan)
    b = atrp.rolling(63, min_periods=21).std() / atrp.rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- cross-estimator spreads (estimator divergence = gaps/jumps/drift signatures) ---
# GK minus Parkinson, 63d normalized (open-close jump content vs pure HL)
def f11re_f11_range_vol_estimators_gkparkspr_63d_base_v098_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 63)
    p = _f11re_parkinson(high, low, 63)
    b = (g - p) / p.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Yang-Zhang minus GK, 63d normalized (overnight-gap content)
def f11re_f11_range_vol_estimators_yzgkspr_63d_base_v099_signal(open, high, low, close):
    y = _f11re_yang_zhang(open, high, low, close, 63)
    g = _f11re_garman_klass(open, high, low, close, 63)
    b = (y - g) / y.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS minus GK, 63d normalized (drift-content divergence)
def f11re_f11_range_vol_estimators_rsgkspr_63d_base_v100_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 63)
    g = _f11re_garman_klass(open, high, low, close, 63)
    b = (r - g) / g.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/price minus Parkinson-equivalent: true-range gap premium over HL-range, 63d
def f11re_f11_range_vol_estimators_atrparkspr_63d_base_v101_signal(high, low, close, closeadj):
    atrp = _f11re_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    hlp = ((high - low) / closeadj.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = (atrp - hlp) / hlp.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- term-structure slopes / curvature across windows ---
# Parkinson term slope: (Park21 - Park126)/Park252 (range-vol term slope)
def f11re_f11_range_vol_estimators_parktermslope_base_v102_signal(high, low):
    p21 = _f11re_parkinson(high, low, 21)
    p126 = _f11re_parkinson(high, low, 126)
    p252 = _f11re_parkinson(high, low, 252)
    b = (p21 - p126) / p252.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson term curvature: Park21 - 2*Park63 + Park126 (vol-cone curvature)
def f11re_f11_range_vol_estimators_parktermcurv_base_v103_signal(high, low):
    p21 = _f11re_parkinson(high, low, 21)
    p63 = _f11re_parkinson(high, low, 63)
    p126 = _f11re_parkinson(high, low, 126)
    b = (p21 - 2.0 * p63 + p126) / p63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR term slope: (ATR5 - ATR21)/ATR63 (short-horizon true-range term slope)
def f11re_f11_range_vol_estimators_atrtermslope_base_v104_signal(high, low, close):
    a5 = _f11re_atr(high, low, close, 5)
    a21 = _f11re_atr(high, low, close, 21)
    a63 = _f11re_atr(high, low, close, 63)
    b = (a5 - a21) / a63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK term ratio 63d/252d (long-end range-vol term structure)
def f11re_f11_range_vol_estimators_gkterm_63v252_base_v105_signal(open, high, low, close):
    s = _f11re_garman_klass(open, high, low, close, 63)
    l = _f11re_garman_klass(open, high, low, close, 252)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- close-position-in-range dynamics ---
# close-in-day-range 63d trend: 21d change in mean close position (accumulation drift)
def f11re_f11_range_vol_estimators_clrngpostrend_base_v106_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    m = pos.rolling(21, min_periods=10).mean()
    b = m - m.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of days closing in upper third of range over 63d (sustained strength in range)
def f11re_f11_range_vol_estimators_clrngupper_base_v107_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    upper = (pos >= 0.6667).astype(float)
    b = upper.rolling(63, min_periods=21).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-position dispersion: std of close-in-range over 63d (indecision/whipsaw)
def f11re_f11_range_vol_estimators_clrngdisp_base_v108_signal(high, low, close):
    pos = (close - low) / (high - low).replace(0, np.nan)
    b = pos.rolling(63, min_periods=21).std()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- overnight-gap range family (news-driven juniors) ---
# overnight var share trend over 126d (gap-risk regime shift)
def f11re_f11_range_vol_estimators_onsharelong_base_v109_signal(open, close):
    von = _f11re_overnight_var(open, close, 126)
    voc = _f11re_open_close_var(open, close, 126)
    b = von / (von + voc).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vol z-score vs 252d (gap-vol spike regime)
def f11re_f11_range_vol_estimators_onvolz_base_v110_signal(open, close):
    on = np.sqrt(_f11re_overnight_var(open, close, 21).clip(lower=0))
    b = _z(on, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vol percentile-rank vs 252d (gap-vol cone position)
def f11re_f11_range_vol_estimators_onvolrank_base_v111_signal(open, close):
    on = np.sqrt(_f11re_overnight_var(open, close, 21).clip(lower=0))
    b = _rank(on, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday vol z-score vs 252d (open-close range-vol regime)
def f11re_f11_range_vol_estimators_ocvolz_base_v112_signal(open, close):
    oc = np.sqrt(_f11re_open_close_var(open, close, 21).clip(lower=0))
    b = _z(oc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-vol vs price-level / amplitude interactions ---
# 52w high-low amplitude / closeadj (full-cycle range amplitude)
def f11re_f11_range_vol_estimators_amplitude_252d_base_v113_signal(high, low, closeadj):
    hi = _rmax(high, 252)
    lo = _rmin(low, 252)
    b = (hi - lo) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 504d amplitude / closeadj (two-year range amplitude)
def f11re_f11_range_vol_estimators_amplitude_504d_base_v114_signal(high, low, closeadj):
    hi = _rmax(high, 504)
    lo = _rmin(low, 504)
    b = (hi - lo) / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# amplitude vs realized range: 252d hi-lo amplitude / sum of daily ranges (range efficiency)
def f11re_f11_range_vol_estimators_rangeeff_252d_base_v115_signal(high, low, closeadj):
    hi = _rmax(high, 252)
    lo = _rmin(low, 252)
    path = (high - low).rolling(252, min_periods=126).sum()
    b = (hi - lo) / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range efficiency 63d (net amplitude vs total intraday travel)
def f11re_f11_range_vol_estimators_rangeeff_63d_base_v116_signal(high, low, close):
    hi = _rmax(high, 63)
    lo = _rmin(low, 63)
    path = (high - low).rolling(63, min_periods=21).sum()
    b = (hi - lo) / path.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-vol cyclical / regime counts ---
# count of true-range expansion days (TR>ATR21) over 63d (active-range regime)
def f11re_f11_range_vol_estimators_trexpdays_base_v117_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    exp = (tr > atr).astype(float)
    cnt = exp.rolling(63, min_periods=21).mean()
    mag = (tr / atr.replace(0, np.nan) - 1.0).clip(lower=0).rolling(21, min_periods=10).mean()
    b = cnt + mag
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# longest run of contraction days in last 63d (coiling persistence)
def f11re_f11_range_vol_estimators_contractrun_base_v118_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    atr = tr.rolling(21, min_periods=10).mean()
    comp = (tr < atr).astype(float)
    grp = (comp == 0).cumsum()
    streak = comp.groupby(grp).cumsum()
    b = streak.rolling(63, min_periods=21).max() / 21.0 + streak / 63.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since last large range-shock (TR z>2.5) scaled (recency of range blowup)
def f11re_f11_range_vol_estimators_shockrecency_base_v119_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    z = _z(tr, 126)
    shock = (z > 2.5)
    idx = pd.Series(np.arange(len(tr)), index=tr.index)
    last = idx.where(shock).ffill()
    dsince = (idx - last)
    b = -np.log1p(dsince.clip(lower=0)) + 0.1 * z.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- multi-estimator consensus & disagreement ---
# range-estimator agreement: 1 - normalized dispersion across Park/GK/RS 21d (consensus)
def f11re_f11_range_vol_estimators_estagree_21d_base_v120_signal(open, high, low, close):
    sp = _f11re_parkinson(high, low, 21)
    sg = _f11re_garman_klass(open, high, low, close, 21)
    sr = _f11re_rogers_satchell(open, high, low, close, 21)
    stk = pd.concat([sp, sg, sr], axis=1)
    disp = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    b = -disp
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-estimator disagreement z vs 252d (jump-regime extremity)
def f11re_f11_range_vol_estimators_estdisagz_base_v121_signal(open, high, low, close):
    sp = _f11re_parkinson(high, low, 63)
    sg = _f11re_garman_klass(open, high, low, close, 63)
    sr = _f11re_rogers_satchell(open, high, low, close, 63)
    stk = pd.concat([sp, sg, sr], axis=1)
    disp = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    b = _z(disp, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# max-minus-min estimator at 21d, normalized (range-estimator spread, jump proxy)
def f11re_f11_range_vol_estimators_estspread_21d_base_v122_signal(open, high, low, close):
    sp = _f11re_parkinson(high, low, 21)
    sg = _f11re_garman_klass(open, high, low, close, 21)
    sr = _f11re_rogers_satchell(open, high, low, close, 21)
    sy = _f11re_yang_zhang(open, high, low, close, 21)
    stk = pd.concat([sp, sg, sr, sy], axis=1)
    b = (stk.max(axis=1) - stk.min(axis=1)) / stk.mean(axis=1).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-vol risk-adjusted / efficiency forms ---
# return per unit of Parkinson range-vol, 63d (range-vol-adjusted drift)
def f11re_f11_range_vol_estimators_retperpark_63d_base_v123_signal(high, low, closeadj):
    ret = np.log(closeadj.replace(0, np.nan) / closeadj.shift(63).replace(0, np.nan))
    p = _f11re_parkinson(high, low, 63)
    b = ret / (p * np.sqrt(63.0)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute return vs ATR: |21d move| in ATR units (efficiency of price travel)
def f11re_f11_range_vol_estimators_moveinatr_21d_base_v124_signal(high, low, close, closeadj):
    move = (closeadj - closeadj.shift(21)).abs()
    atr = _f11re_atr(high, low, close, 21)
    b = move / (atr * np.sqrt(21.0)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-variance concentration: max daily log-range^2 over 21d vs the 21d sum (Herfindahl-like)
def f11re_f11_range_vol_estimators_vardrag_21d_base_v125_signal(high, low):
    lr2 = _f11re_logsq(high, low)
    mx = lr2.rolling(21, min_periods=10).max()
    tot = lr2.rolling(21, min_periods=10).sum()
    b = mx / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- gap-adjusted true range & wick-range estimators ---
# Wilder ATR/price vs simple ATR/price spread (smoothing-sensitive range regime)
def f11re_f11_range_vol_estimators_atrsmoothspr_base_v126_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    wild = tr.ewm(alpha=1.0 / 21.0, min_periods=11).mean()
    simple = tr.rolling(21, min_periods=10).mean()
    b = (wild - simple) / simple.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# normalized ATR using median true-range (robust ATR/price, outlier-resistant), 21d
def f11re_f11_range_vol_estimators_medatr_21d_base_v127_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    med = tr.rolling(21, min_periods=10).median()
    b = med / close.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR mean vs ATR median spread (true-range skew / fat-tail of daily ranges), 63d
def f11re_f11_range_vol_estimators_atrskew_63d_base_v128_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    mn = tr.rolling(63, min_periods=21).mean()
    med = tr.rolling(63, min_periods=21).median()
    b = (mn - med) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- long-horizon range-vol levels normalized by closeadj ---
# Parkinson 504d annualized (multi-year range-vol level)
def f11re_f11_range_vol_estimators_park_504d_base_v129_signal(high, low):
    b = _f11re_parkinson(high, low, 504) * np.sqrt(252.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Parkinson 504d vs 126d ratio (multi-year vs half-year range-vol term)
def f11re_f11_range_vol_estimators_parkterm_126v504_base_v130_signal(high, low):
    s = _f11re_parkinson(high, low, 126)
    l = _f11re_parkinson(high, low, 504)
    b = s / l.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR/closeadj 504d level (multi-year true-range vol)
def f11re_f11_range_vol_estimators_atr_504d_base_v131_signal(high, low, close, closeadj):
    atr = _f11re_atr(high, low, close, 504)
    b = atr / closeadj.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 504d annualized vs its 252d median (multi-year regime gap)
def f11re_f11_range_vol_estimators_gk_504d_base_v132_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 504) * np.sqrt(252.0)
    med = g.rolling(252, min_periods=126).median()
    b = g / med.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-vol breakout-from-squeeze signatures ---
# squeeze-to-expansion: Parkinson21 now vs its 63d min, gated by prior compression
def f11re_f11_range_vol_estimators_parkbreakout_base_v133_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    lo = p.rolling(63, min_periods=21).min()
    expand = p / lo.replace(0, np.nan) - 1.0
    prior_tight = (lo / p.rolling(252, min_periods=126).median().replace(0, np.nan))
    b = expand * (1.0 - prior_tight).clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ATR breakout: ATR5 crossing above ATR63, magnitude-weighted (range-vol ignition)
def f11re_f11_range_vol_estimators_atrbreakout_base_v134_signal(high, low, close):
    a5 = _f11re_atr(high, low, close, 5)
    a63 = _f11re_atr(high, low, close, 63)
    b = (a5 / a63.replace(0, np.nan) - 1.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range bandwidth: (Park21 max - min) over 63d normalized (recent range-vol travel)
def f11re_f11_range_vol_estimators_parkbandwidth_base_v135_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    hi = p.rolling(63, min_periods=21).max()
    lo = p.rolling(63, min_periods=21).min()
    mn = p.rolling(63, min_periods=21).mean()
    b = (hi - lo) / mn.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- intraday close-to-open vs open-to-close range decomposition ---
# day-direction range bias: mean sign(close-open)*range/close over 21d (directional range)
def f11re_f11_range_vol_estimators_dirrng_21d_base_v136_signal(open, high, low, close):
    sign = np.sign(close - open)
    rng = (high - low) / close.replace(0, np.nan)
    b = (sign * rng).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-to-range ratio: |open - prior close| vs day's HL range, 21d (overnight gap size)
def f11re_f11_range_vol_estimators_gaptorange_base_v137_signal(open, high, low, close):
    gap = (open - close.shift(1)).abs()
    rng = (high - low)
    b = (gap / rng.replace(0, np.nan)).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday continuation: magnitude-weighted product of overnight gap and intraday move, 63d
def f11re_f11_range_vol_estimators_gapfollow_base_v138_signal(open, close):
    gap = np.log(open.replace(0, np.nan) / close.shift(1).replace(0, np.nan))
    intraday = np.log(close.replace(0, np.nan) / open.replace(0, np.nan))
    prod = gap * intraday
    b = prod.rolling(63, min_periods=21).mean() / (gap.abs().rolling(63, min_periods=21).mean()
                                                   * intraday.abs().rolling(63, min_periods=21).mean()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- range-vol skewness / kurtosis of daily ranges ---
# 63d skew of daily HL-range/close (range-distribution asymmetry)
def f11re_f11_range_vol_estimators_rngskew_63d_base_v139_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    b = hl.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126d kurtosis of daily true-range/close (fat-tailed range regime)
def f11re_f11_range_vol_estimators_rngkurt_126d_base_v140_signal(high, low, close):
    trp = _f11re_true_range(high, low, close) / close.replace(0, np.nan)
    b = trp.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 90th-percentile daily range vs median range, 126d (range tail-ratio)
def f11re_f11_range_vol_estimators_rngtailratio_base_v141_signal(high, low, close):
    hl = _f11re_hl_range(high, low, close)
    q90 = hl.rolling(126, min_periods=63).quantile(0.9)
    q50 = hl.rolling(126, min_periods=63).quantile(0.5)
    b = q90 / q50.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- composite range-vol regime / cycle position ---
# blended range-vol cone: mean percentile of Park/GK/ATR vs 252d (consensus regime)
def f11re_f11_range_vol_estimators_blendcone_base_v142_signal(open, high, low, close):
    cp = _rank(_f11re_parkinson(high, low, 21), 252)
    cg = _rank(_f11re_garman_klass(open, high, low, close, 21), 252)
    ca = _rank(_f11re_atr(high, low, close, 21) / close.replace(0, np.nan), 252)
    b = pd.concat([cp, cg, ca], axis=1).mean(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol cycle phase: position of ATR/price in its 504d range (long range-vol cycle)
def f11re_f11_range_vol_estimators_atrcyclepos_base_v143_signal(high, low, close, closeadj):
    atrp = _f11re_atr(high, low, close, 63) / closeadj.replace(0, np.nan)
    lo = atrp.rolling(504, min_periods=252).min()
    hi = atrp.rolling(504, min_periods=252).max()
    b = (atrp - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# range-vol trend persistence: sign-consistency of Park21 weekly changes over 63d
def f11re_f11_range_vol_estimators_parktrendpersist_base_v144_signal(high, low):
    p = _f11re_parkinson(high, low, 21)
    chg = np.sign(p - p.shift(5))
    b = chg.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- additional distinct facets ---
# Parkinson 21d minus its 5d (very-short range-vol expansion delta)
def f11re_f11_range_vol_estimators_parkfastdelta_base_v145_signal(high, low):
    p21 = _f11re_parkinson(high, low, 21)
    p5 = _f11re_parkinson(high, low, 5)
    b = (p5 - p21) / p21.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GK 126d annualized z vs 504d (long-horizon GK regime extremity)
def f11re_f11_range_vol_estimators_gkz_126d_base_v146_signal(open, high, low, close):
    g = _f11re_garman_klass(open, high, low, close, 126)
    b = _z(g, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# RS 126d annualized percentile-rank vs 504d (long drift-vol cone)
def f11re_f11_range_vol_estimators_rsrank_126d_base_v147_signal(open, high, low, close):
    r = _f11re_rogers_satchell(open, high, low, close, 126)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true-range z momentum: 21d change in TR-z-vs-63d (range-shock acceleration)
def f11re_f11_range_vol_estimators_trzmom_base_v148_signal(high, low, close):
    tr = _f11re_true_range(high, low, close)
    z = _z(tr, 63)
    sm = z.rolling(21, min_periods=10).mean()
    b = sm - sm.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# high-low range vs closeadj, 126d, normalized by its own 252d level (range-vol regime)
def f11re_f11_range_vol_estimators_hlrngreg_126d_base_v149_signal(high, low, closeadj):
    hl = ((high - low) / closeadj.replace(0, np.nan)).rolling(126, min_periods=63).mean()
    base = hl.rolling(252, min_periods=126).mean()
    b = hl / base.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# YZ 21d vs its 252d median, percentile-ranked (full-estimator regime cone)
def f11re_f11_range_vol_estimators_yzcone_base_v150_signal(open, high, low, close):
    y = _f11re_yang_zhang(open, high, low, close, 21)
    b = _rank(y, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f11re_f11_range_vol_estimators_parkcone_5d_base_v076_signal,
    f11re_f11_range_vol_estimators_parkcone_63d_base_v077_signal,
    f11re_f11_range_vol_estimators_gkcone_5d_base_v078_signal,
    f11re_f11_range_vol_estimators_atrcone_63d_base_v079_signal,
    f11re_f11_range_vol_estimators_upsemirng_21d_base_v080_signal,
    f11re_f11_range_vol_estimators_dnsemirng_21d_base_v081_signal,
    f11re_f11_range_vol_estimators_semirngskew_63d_base_v082_signal,
    f11re_f11_range_vol_estimators_uwickshare_21d_base_v083_signal,
    f11re_f11_range_vol_estimators_lwickshare_21d_base_v084_signal,
    f11re_f11_range_vol_estimators_bodyrng_21d_base_v085_signal,
    f11re_f11_range_vol_estimators_parkmom_63d_base_v086_signal,
    f11re_f11_range_vol_estimators_gkmom_63d_base_v087_signal,
    f11re_f11_range_vol_estimators_atrmom_63d_base_v088_signal,
    f11re_f11_range_vol_estimators_parkaccel_21d_base_v089_signal,
    f11re_f11_range_vol_estimators_parkregdist_base_v090_signal,
    f11re_f11_range_vol_estimators_gkregdist_base_v091_signal,
    f11re_f11_range_vol_estimators_atrsqueeze_base_v092_signal,
    f11re_f11_range_vol_estimators_parkcompress_base_v093_signal,
    f11re_f11_range_vol_estimators_parkexpcnt_base_v094_signal,
    f11re_f11_range_vol_estimators_parkvov_126d_base_v095_signal,
    f11re_f11_range_vol_estimators_gkvov_63d_base_v096_signal,
    f11re_f11_range_vol_estimators_atrvov_63d_base_v097_signal,
    f11re_f11_range_vol_estimators_gkparkspr_63d_base_v098_signal,
    f11re_f11_range_vol_estimators_yzgkspr_63d_base_v099_signal,
    f11re_f11_range_vol_estimators_rsgkspr_63d_base_v100_signal,
    f11re_f11_range_vol_estimators_atrparkspr_63d_base_v101_signal,
    f11re_f11_range_vol_estimators_parktermslope_base_v102_signal,
    f11re_f11_range_vol_estimators_parktermcurv_base_v103_signal,
    f11re_f11_range_vol_estimators_atrtermslope_base_v104_signal,
    f11re_f11_range_vol_estimators_gkterm_63v252_base_v105_signal,
    f11re_f11_range_vol_estimators_clrngpostrend_base_v106_signal,
    f11re_f11_range_vol_estimators_clrngupper_base_v107_signal,
    f11re_f11_range_vol_estimators_clrngdisp_base_v108_signal,
    f11re_f11_range_vol_estimators_onsharelong_base_v109_signal,
    f11re_f11_range_vol_estimators_onvolz_base_v110_signal,
    f11re_f11_range_vol_estimators_onvolrank_base_v111_signal,
    f11re_f11_range_vol_estimators_ocvolz_base_v112_signal,
    f11re_f11_range_vol_estimators_amplitude_252d_base_v113_signal,
    f11re_f11_range_vol_estimators_amplitude_504d_base_v114_signal,
    f11re_f11_range_vol_estimators_rangeeff_252d_base_v115_signal,
    f11re_f11_range_vol_estimators_rangeeff_63d_base_v116_signal,
    f11re_f11_range_vol_estimators_trexpdays_base_v117_signal,
    f11re_f11_range_vol_estimators_contractrun_base_v118_signal,
    f11re_f11_range_vol_estimators_shockrecency_base_v119_signal,
    f11re_f11_range_vol_estimators_estagree_21d_base_v120_signal,
    f11re_f11_range_vol_estimators_estdisagz_base_v121_signal,
    f11re_f11_range_vol_estimators_estspread_21d_base_v122_signal,
    f11re_f11_range_vol_estimators_retperpark_63d_base_v123_signal,
    f11re_f11_range_vol_estimators_moveinatr_21d_base_v124_signal,
    f11re_f11_range_vol_estimators_vardrag_21d_base_v125_signal,
    f11re_f11_range_vol_estimators_atrsmoothspr_base_v126_signal,
    f11re_f11_range_vol_estimators_medatr_21d_base_v127_signal,
    f11re_f11_range_vol_estimators_atrskew_63d_base_v128_signal,
    f11re_f11_range_vol_estimators_park_504d_base_v129_signal,
    f11re_f11_range_vol_estimators_parkterm_126v504_base_v130_signal,
    f11re_f11_range_vol_estimators_atr_504d_base_v131_signal,
    f11re_f11_range_vol_estimators_gk_504d_base_v132_signal,
    f11re_f11_range_vol_estimators_parkbreakout_base_v133_signal,
    f11re_f11_range_vol_estimators_atrbreakout_base_v134_signal,
    f11re_f11_range_vol_estimators_parkbandwidth_base_v135_signal,
    f11re_f11_range_vol_estimators_dirrng_21d_base_v136_signal,
    f11re_f11_range_vol_estimators_gaptorange_base_v137_signal,
    f11re_f11_range_vol_estimators_gapfollow_base_v138_signal,
    f11re_f11_range_vol_estimators_rngskew_63d_base_v139_signal,
    f11re_f11_range_vol_estimators_rngkurt_126d_base_v140_signal,
    f11re_f11_range_vol_estimators_rngtailratio_base_v141_signal,
    f11re_f11_range_vol_estimators_blendcone_base_v142_signal,
    f11re_f11_range_vol_estimators_atrcyclepos_base_v143_signal,
    f11re_f11_range_vol_estimators_parktrendpersist_base_v144_signal,
    f11re_f11_range_vol_estimators_parkfastdelta_base_v145_signal,
    f11re_f11_range_vol_estimators_gkz_126d_base_v146_signal,
    f11re_f11_range_vol_estimators_rsrank_126d_base_v147_signal,
    f11re_f11_range_vol_estimators_trzmom_base_v148_signal,
    f11re_f11_range_vol_estimators_hlrngreg_126d_base_v149_signal,
    f11re_f11_range_vol_estimators_yzcone_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F11_RANGE_VOL_ESTIMATORS_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
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

    assert n_features == 75, n_features
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

    print("OK f11_range_vol_estimators_base_076_150_claude: %d features pass" % n_features)
