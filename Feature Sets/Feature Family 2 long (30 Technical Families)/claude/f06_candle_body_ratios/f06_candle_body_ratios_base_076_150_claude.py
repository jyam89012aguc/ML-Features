"""f06_candle_body_ratios base features 076-150.

Domain: candle body ratios -- the SECOND set of 75 distinct features
beyond base_001_075. No structural duplicates with base_001_075:
each feature here uses a different formula or aggregation than v001-v075,
not just a different window size.

Every function is a fully expanded def with formula inline. NaN policy:
never fillna(0) inside rolling code; only replace([inf,-inf], nan) at
final return. Windows > 21 use closeadj; windows <=21 use close. Within
single-bar OHLC features (window <= 5) use unadjusted o/h/l/c.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# --- Group AA: body relative to inter-bar move ----------------------------


def f06cb_f06_candle_body_ratios_bodydir_align_1d_base_v076_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """sign-product of intra-bar body direction and close-position bias:
    sign(close-open) * (clpos - 0.5). Aligned +ve when close in upper half AND bull,
    or close in lower half AND bear (i.e., body color matches closing pressure)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng - 0.5
    sb = np.sign(close - open)
    out = sb * cp
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_dayret_abs_rng_1d_base_v077_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """|close - prev_close|/range -- absolute daily return scaled by intra-bar range.
    Captures how much the daily move occupied the bar regardless of direction."""
    rng = (high - low).replace(0.0, np.nan)
    out = (close - close.shift(1)).abs() / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_std_50d_base_v078_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar std of |closeadj-open|/closeadj."""
    body = (closeadj - open).abs()
    n = body / closeadj.replace(0.0, np.nan)
    out = n.rolling(50, min_periods=50).std()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_pcoutside_1d_base_v079_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """1 if prev_close lies OUTSIDE today's bar (prev_close > high OR prev_close < low),
    else 0. Captures gap-magnitude regime via inclusion test in bar."""
    pc = close.shift(1)
    cond = ((pc > high) | (pc < low)).astype(float)
    out = cond
    out[pc.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyac1_30d_base_v080_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Lag-1 autocorr of body magnitude over 30 bars."""
    body = (close - open).abs()
    out = body.rolling(30, min_periods=30).corr(body.shift(1))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngmean_50d_base_v081_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """50-bar mean of (high-low)/typical price (close-based normalization).
    Independent of v056 (30d window, different denominator scheme)."""
    rng = (high - low)
    out = rng.rolling(50, min_periods=50).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysz_max_5d_base_v082_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar MAX of |close-open|/close. Recent peak body magnitude."""
    body = (close - open).abs() / close.replace(0.0, np.nan)
    out = body.rolling(5, min_periods=5).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upsh_max_5d_base_v083_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar max of upper-shadow / range."""
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = upper / rng
    out = s.rolling(5, min_periods=5).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_losh_max_5d_base_v084_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar max of lower-shadow / range."""
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    s = lower / rng
    out = s.rolling(5, min_periods=5).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_doji_soft_30d_base_v085_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in 30 with body/range < 0.15 (soft doji frequency)."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    doji = (r < 0.15).astype(float)
    out = doji.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_marub_soft_30d_base_v086_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in 30 with body/range > 0.6 (soft marubozu freq)."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    m = (r > 0.6).astype(float)
    out = m.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_3bar_brprod_3d_base_v087_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Geometric mean (cube root of product) of last-3 body/range. Different
    structure from arithmetic means / sums."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    log_r = np.log(r + 1e-9)
    log_mean = log_r.rolling(3, min_periods=3).mean()
    out = np.exp(log_mean)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clhi_strk_5d_base_v088_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive bars with close-position > 0.6. Length of run."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    near = (cp > 0.6).astype(int)
    grp = (near == 0).cumsum()
    cnt = near.groupby(grp).cumcount() + 1
    out = cnt.where(near == 1, 0).astype(float)
    out[rng.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_cllo_strk_5d_base_v089_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive bars with close-position < 0.4. Length of run."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    near = (cp < 0.4).astype(int)
    grp = (near == 0).cumsum()
    cnt = near.groupby(grp).cumcount() + 1
    out = cnt.where(near == 1, 0).astype(float)
    out[rng.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_atr_iqr_30d_base_v090_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar IQR of (true-range / close). Dispersion of TR normalized."""
    pc = close.shift(1)
    tr1 = (high - low).abs()
    tr2 = (high - pc).abs()
    tr3 = (low - pc).abs()
    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
    norm = tr / close.replace(0.0, np.nan)
    q75 = norm.rolling(30, min_periods=30).quantile(0.75)
    q25 = norm.rolling(30, min_periods=30).quantile(0.25)
    out = q75 - q25
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brslope_5d_base_v091_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Slope of body/range over 5 bars: diff(3) of brrat / typical brrat."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    mu = r.rolling(10, min_periods=5).mean().replace(0.0, np.nan)
    out = r.diff(3) / mu
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_q90_30d_base_v092_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar 90th percentile of close-position-in-bar -- upper tail of closing pressure."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(30, min_periods=30).quantile(0.9)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clhi_frac_20d_base_v093_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Fraction of bars in 20 with close-position > 0.5."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = (cp > 0.5).astype(float).rolling(20, min_periods=20).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodymid_up_30d_base_v094_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar fraction of bars where body's midpoint is in upper half of the bar.
    ((open+close)/2 > (high+low)/2)."""
    bmid = (open + close) * 0.5
    bar_mid = (high + low) * 0.5
    cond = (bmid > bar_mid).astype(float)
    out = cond.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shabsdiff_sq_1d_base_v095_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """((upper - lower)/range)^2 -- squared net wick imbalance (non-monotone in shasym)."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    diff = (upper - lower) / rng
    out = diff * diff
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_hammer_skew_30d_base_v096_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar skew of (lower-upper)/range. Asymmetry skew of shadows.
    Different structure than base-1 hammer features (which are means/sums)."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    diff = (lower - upper) / rng
    out = diff.rolling(30, min_periods=30).skew()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_invhammer_max_10d_base_v097_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """10-bar MAX of (upper/range)*(1 - body/range) -- single most dominant upper-shadow bar."""
    body = (close - open).abs()
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = (upper / rng) * (1.0 - body / rng)
    out = s.rolling(10, min_periods=10).max()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_uplodiff_sd_30d_base_v098_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar std of (upper/range - lower/range). Variability of net wick direction."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    diff = (upper - lower) / rng
    out = diff.rolling(30, min_periods=30).std()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_hi_step_1d_base_v099_signal(high: pd.Series) -> pd.Series:
    """log(high / prev high) -- daily high-step."""
    ph = high.shift(1).replace(0.0, np.nan)
    out = np.log(high / ph)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_lo_step_1d_base_v100_signal(low: pd.Series) -> pd.Series:
    """log(low / prev low) -- daily low-step."""
    pl = low.shift(1).replace(0.0, np.nan)
    out = np.log(low / pl)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_hi_overshoot_30d_base_v101_signal(high: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar count of bars where high > prev_close * 1.005 (overshoot threshold).
    Different aggregation than v099's daily log step."""
    pc = close.shift(1)
    cond = (high > pc * 1.005).astype(float)
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_lo_undershoot_30d_base_v102_signal(low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar count of bars where low < prev_close * 0.995."""
    pc = close.shift(1)
    cond = (low < pc * 0.995).astype(float)
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bar_overlap_1d_base_v103_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Bar overlap: max(0, min(high, prev_high) - max(low, prev_low)) / range.
    Fraction of today's bar that overlapped yesterday's bar."""
    ph = high.shift(1)
    pl = low.shift(1)
    overlap = np.minimum(high, ph) - np.maximum(low, pl)
    overlap = overlap.where(overlap > 0.0, 0.0)
    rng = (high - low).replace(0.0, np.nan)
    out = overlap / rng
    out[ph.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_iqr_30d_base_v104_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar IQR (q75-q25) of shadow asymmetry. Spread of shadow imbalance."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    q75 = sa.rolling(30, min_periods=30).quantile(0.75)
    q25 = sa.rolling(30, min_periods=30).quantile(0.25)
    out = q75 - q25
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upsh_corr_prev_30d_base_v105_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar rolling corr between upper-shadow/range and its lag-1.
    Measures persistence of upper-wick regime."""
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = upper / rng
    out = s.rolling(30, min_periods=30).corr(s.shift(1))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng3sum_3d_base_v106_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """3-bar high - 3-bar low (rolling)/ 3-bar close-based norm.
    Compound 3-bar range vs current range."""
    h3 = high.rolling(3, min_periods=3).max()
    l3 = low.rolling(3, min_periods=3).min()
    rng = (high - low).replace(0.0, np.nan)
    out = (h3 - l3) / rng
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_sbodysum_5d_base_v107_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar sum of signed body / 5-bar sum of range -- net body-direction over range."""
    sbody = (close - open)
    rng = (high - low)
    sb_sum = sbody.rolling(5, min_periods=5).sum()
    rng_sum = rng.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    out = sb_sum / rng_sum
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rngsum_5d_base_v108_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar sum of range divided by close (level-normalized cumulative range)."""
    rng = (high - low)
    rs = rng.rolling(5, min_periods=5).sum()
    out = rs / close.replace(0.0, np.nan)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_largbody_cnt_21d_base_v109_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars in 21 where body > 21d mean body (large-body bars)."""
    body = (close - open).abs()
    mu = body.rolling(21, min_periods=21).mean()
    cond = (body > mu).astype(float)
    out = cond.rolling(21, min_periods=21).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodydiv_dret_30d_base_v110_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of |close-open|/|close - prev_close| -- intra-bar churn ratio."""
    body = (close - open).abs()
    dret = (close - close.shift(1)).abs().replace(0.0, np.nan)
    r = body / dret
    out = r.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_body_in_50dh_50d_base_v111_signal(high: pd.Series, low: pd.Series, open: pd.Series, close: pd.Series) -> pd.Series:
    """Body midpoint position in 50-day high-low range: (bmid - 50dLow)/(50dHigh-50dLow)."""
    bmid = (open + close) * 0.5
    h50 = high.rolling(50, min_periods=50).max()
    l50 = low.rolling(50, min_periods=50).min()
    den = (h50 - l50).replace(0.0, np.nan)
    out = (bmid - l50) / den
    return out.replace([np.inf, -np.inf], np.nan)




def f06cb_f06_candle_body_ratios_sbodysq_30d_base_v113_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of sign(body) * body^2 / close^2 -- signed body-squared."""
    sb = np.sign(close - open) * ((close - open) ** 2) / (close.replace(0.0, np.nan) ** 2)
    out = sb.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_body_ema_5d_base_v114_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """5-span EWMA of body magnitude (relative to close)."""
    body = (close - open).abs() / close.replace(0.0, np.nan)
    out = body.ewm(span=5, adjust=False, min_periods=5).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_ema_21d_base_v115_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21-span EWMA of body/range."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.ewm(span=21, adjust=False, min_periods=21).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_ema_30d_base_v116_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-span EWMA of close-position-in-bar."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.ewm(span=30, adjust=False, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng_ac1_30d_base_v117_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """30-bar lag-1 autocorrelation of bar range. Tests range-regime persistence."""
    rng = (high - low)
    out = rng.rolling(30, min_periods=30).corr(rng.shift(1))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysharpe_50d_base_v118_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar mean(body)/std(body) -- body-magnitude sharpe."""
    body = (closeadj - open).abs()
    mu = body.rolling(50, min_periods=50).mean()
    sd = body.rolling(50, min_periods=50).std().replace(0.0, np.nan)
    out = mu / sd
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_rnk_30d_base_v119_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of shadow asymmetry over 30 bars."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    out = sa.rolling(30, min_periods=15).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyac_pos_30d_base_v120_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar lag-1 autocorr of signed body (close-open)/close. Tests body-direction persistence."""
    sb = (close - open) / close.replace(0.0, np.nan)
    out = sb.rolling(30, min_periods=30).corr(sb.shift(1))
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brclpos_corr_30d_base_v121_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar rolling corr between body/range and close-position-in-bar."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    br = body / rng
    cp = (close - low) / rng
    out = br.rolling(30, min_periods=30).corr(cp)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng_consist_30d_base_v122_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """30-bar fraction of bars where range > prior-bar range. Range-expansion persistence."""
    rng = (high - low)
    exp = (rng > rng.shift(1)).astype(float)
    out = exp.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_brhalf_strk_5d_base_v123_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive bars with body/range > 0.5. Length of streak."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    near = (r > 0.5).astype(int)
    grp = (near == 0).cumsum()
    cnt = near.groupby(grp).cumcount() + 1
    out = cnt.where(near == 1, 0).astype(float)
    out[rng.isna()] = np.nan
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodysum_5d_base_v124_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5-bar sum(|body|) / 5-bar sum(range). Aggregated brrat over 5 bars."""
    body = (close - open).abs()
    rng = (high - low)
    bs = body.rolling(5, min_periods=5).sum()
    rs = rng.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    out = bs / rs
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clop_vol_norm_1d_base_v125_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(close - open) * (high - low) / close^2 -- product of signed body and range,
    normalized by price^2. A bar-energy / momentum-strength score."""
    sbody = close - open
    rng = high - low
    out = (sbody * rng) / (close.replace(0.0, np.nan) ** 2)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyrng_q90_30d_base_v126_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar 90th-percentile of body/range -- upper tail of body fullness."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r.rolling(30, min_periods=30).quantile(0.9)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_body_mad_30d_base_v127_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar MAD (mean abs deviation) of body magnitude. Robust dispersion."""
    body = (close - open).abs()
    mu = body.rolling(30, min_periods=30).mean()
    abs_dev = (body - mu).abs()
    out = abs_dev.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_mad_30d_base_v128_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar MAD of body/range."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    mu = r.rolling(30, min_periods=30).mean()
    abs_dev = (r - mu).abs()
    out = abs_dev.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)




def f06cb_f06_candle_body_ratios_bullfrac_spread_60d_base_v130_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """5-bar bull-fraction minus 60-bar bull-fraction. Short-vs-long color regime diff."""
    bull = (closeadj > open).astype(float)
    s5 = bull.rolling(5, min_periods=5).mean()
    s60 = bull.rolling(60, min_periods=60).mean()
    out = s5 - s60
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodybull_disagree_30d_base_v131_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar count of bars where signed body-pressure disagrees with the
    median signed body over the window: sign(close-open) != sign(rolling 30d median signed body).
    Captures churn vs prevailing color regime."""
    sb = (close - open) / close.replace(0.0, np.nan)
    med = sb.rolling(30, min_periods=30).median()
    disagree = (np.sign(sb) * np.sign(med) < 0).astype(float)
    out = disagree.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_rnk_50d_base_v132_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-day percentile rank of close-position-in-bar (closeadj basis).
    Distinct from base-1 brrnk (rank of brrat)."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (closeadj - low) / rng
    out = cp.rolling(50, min_periods=25).rank(pct=True)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clhi06_strk_7d_base_v133_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """7-bar rolling sum of (close-pos>0.6) bars. Recent buying-pressure intensity."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    near = (cp > 0.6).astype(float)
    out = near.rolling(7, min_periods=7).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bigrng_cnt_30d_base_v134_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in 30 where range > 1.5x 30d mean range. Extreme-range count."""
    rng = (high - low)
    mu = rng.rolling(30, min_periods=30).mean()
    cond = (rng > 1.5 * mu).astype(float)
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_smallrng_cnt_30d_base_v135_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars in 30 where range < 0.5x 30d mean range. Inside-bar / tight-bar count."""
    rng = (high - low)
    mu = rng.rolling(30, min_periods=30).mean()
    cond = (rng < 0.5 * mu).astype(float)
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodyalign_30d_base_v136_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar count of body-and-dret-aligned bars:
    sign(close-open) == sign(close-prev_close)."""
    sb = np.sign(close - open)
    sd = np.sign(close - close.shift(1))
    cond = ((sb * sd) > 0).astype(float)
    out = cond.rolling(30, min_periods=30).sum()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shape_std_50d_base_v137_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """50-bar std of arctan((upper-lower)/(body+0.001*range)).
    Spread of bar-shape over time, not just mean level."""
    rng = (high - low)
    body = (close - open).abs() + rng * 0.001
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    si = np.arctan((upper - lower) / body.replace(0.0, np.nan))
    out = si.rolling(50, min_periods=50).std()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_br_diff_7d_base_v138_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """body/range - body/range.shift(7). 7-bar change in body fullness."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    r = body / rng
    out = r - r.shift(7)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_upbody_kurt_30d_base_v139_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar kurtosis of log((upper+eps)/(body+eps)) -- tail thickness of
    upper-shadow-to-body ratio."""
    upper = high - np.maximum(open, close)
    body = (close - open).abs()
    eps = (high - low).abs() * 0.01 + 1e-12
    s = np.log((upper + eps) / (body + eps))
    out = s.rolling(30, min_periods=30).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_clpos_kurt_30d_base_v140_signal(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar kurtosis of close-position-in-bar -- tail thickness of close-position dist."""
    rng = (high - low).replace(0.0, np.nan)
    cp = (close - low) / rng
    out = cp.rolling(30, min_periods=30).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bullbear_emadiff_30d_base_v141_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """EMA-7 minus EMA-30 of (bull-bear indicator) -- short-vs-long color regime spread (EMA-based)."""
    sb = np.sign(close - open).astype(float)
    e7 = sb.ewm(span=7, adjust=False, min_periods=7).mean()
    e30 = sb.ewm(span=30, adjust=False, min_periods=30).mean()
    out = e7 - e30
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_openpos_std_30d_base_v142_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar std of (open - prev_close)/range. Variability of open-position-vs-prev-close."""
    rng = (high - low).replace(0.0, np.nan)
    pc = close.shift(1)
    s = (open - pc) / rng
    out = s.rolling(30, min_periods=30).std()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_rng_z_7d_base_v143_signal(high: pd.Series, low: pd.Series) -> pd.Series:
    """7-bar z-score of range. Short-term range surprise."""
    rng = (high - low)
    mu = rng.rolling(7, min_periods=7).mean()
    sd = rng.rolling(7, min_periods=7).std().replace(0.0, np.nan)
    out = (rng - mu) / sd
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_sgnbrrat_30d_base_v144_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar mean of (1 - body/range) * sign(close-open) -- wick-residual signed."""
    body = (close - open).abs()
    rng = (high - low).replace(0.0, np.nan)
    sb = np.sign(close - open)
    r = (1.0 - body / rng) * sb
    out = r.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shasym_rngcorr_50d_base_v145_signal(open: pd.Series, high: pd.Series, low: pd.Series, closeadj: pd.Series) -> pd.Series:
    """50-bar corr between shadow-asymmetry and range/closeadj.
    Tests whether big-range bars have a directional wick bias (closeadj basis)."""
    upper = high - np.maximum(open, closeadj)
    lower = np.minimum(open, closeadj) - low
    den = (upper + lower).replace(0.0, np.nan)
    sa = (upper - lower) / den
    rng = (high - low) / closeadj.replace(0.0, np.nan)
    out = sa.rolling(50, min_periods=50).corr(rng)
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_no_upsh_30d_base_v146_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar fraction of bars with upper-shadow/range < 0.1 (no upper wick)."""
    upper = high - np.maximum(open, close)
    rng = (high - low).replace(0.0, np.nan)
    s = upper / rng
    cond = (s < 0.1).astype(float)
    out = cond.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_no_losh_30d_base_v147_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar fraction of bars with lower-shadow/range < 0.1 (no lower wick)."""
    lower = np.minimum(open, close) - low
    rng = (high - low).replace(0.0, np.nan)
    s = lower / rng
    cond = (s < 0.1).astype(float)
    out = cond.rolling(30, min_periods=30).mean()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodymad_robz_60d_base_v148_signal(open: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Robust z of body magnitude: (body - 60d median) / 60d MAD."""
    body = (closeadj - open).abs()
    med = body.rolling(60, min_periods=60).median()
    mad = (body - med).abs().rolling(60, min_periods=60).median().replace(0.0, np.nan)
    out = (body - med) / mad
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_shimbal_kurt_30d_base_v149_signal(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """30-bar kurtosis of (upper - lower)/close -- tail thickness of wick imbalance."""
    upper = high - np.maximum(open, close)
    lower = np.minimum(open, close) - low
    s = (upper - lower) / close.replace(0.0, np.nan)
    out = s.rolling(30, min_periods=30).kurt()
    return out.replace([np.inf, -np.inf], np.nan)


def f06cb_f06_candle_body_ratios_bodymom_ema_diff_30d_base_v150_signal(open: pd.Series, close: pd.Series) -> pd.Series:
    """EMA-5 minus EMA-30 of signed body/close -- MACD-style differential of body momentum."""
    sb = (close - open) / close.replace(0.0, np.nan)
    e5 = sb.ewm(span=5, adjust=False, min_periods=5).mean()
    e30 = sb.ewm(span=30, adjust=False, min_periods=30).mean()
    out = e5 - e30
    return out.replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


def _e(fn, *inputs):
    return fn.__name__, {"inputs": list(inputs), "func": fn}


f06_candle_body_ratios_base_076_150_REGISTRY = dict([
    _e(f06cb_f06_candle_body_ratios_bodydir_align_1d_base_v076_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_dayret_abs_rng_1d_base_v077_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodysz_std_50d_base_v078_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_pcoutside_1d_base_v079_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyac1_30d_base_v080_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_rngmean_50d_base_v081_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_bodysz_max_5d_base_v082_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_upsh_max_5d_base_v083_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_losh_max_5d_base_v084_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_doji_soft_30d_base_v085_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_marub_soft_30d_base_v086_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_3bar_brprod_3d_base_v087_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clhi_strk_5d_base_v088_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_cllo_strk_5d_base_v089_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_atr_iqr_30d_base_v090_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_brslope_5d_base_v091_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_q90_30d_base_v092_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clhi_frac_20d_base_v093_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodymid_up_30d_base_v094_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shabsdiff_sq_1d_base_v095_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_hammer_skew_30d_base_v096_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_invhammer_max_10d_base_v097_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_uplodiff_sd_30d_base_v098_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_hi_step_1d_base_v099_signal, "high"),
    _e(f06cb_f06_candle_body_ratios_lo_step_1d_base_v100_signal, "low"),
    _e(f06cb_f06_candle_body_ratios_hi_overshoot_30d_base_v101_signal, "high", "close"),
    _e(f06cb_f06_candle_body_ratios_lo_undershoot_30d_base_v102_signal, "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bar_overlap_1d_base_v103_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_shasym_iqr_30d_base_v104_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upsh_corr_prev_30d_base_v105_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rng3sum_3d_base_v106_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_sbodysum_5d_base_v107_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rngsum_5d_base_v108_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_largbody_cnt_21d_base_v109_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_bodydiv_dret_30d_base_v110_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_body_in_50dh_50d_base_v111_signal, "high", "low", "open", "close"),
    _e(f06cb_f06_candle_body_ratios_sbodysq_30d_base_v113_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_body_ema_5d_base_v114_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_br_ema_21d_base_v115_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_ema_30d_base_v116_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rng_ac1_30d_base_v117_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_bodysharpe_50d_base_v118_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_shasym_rnk_30d_base_v119_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyac_pos_30d_base_v120_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_brclpos_corr_30d_base_v121_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rng_consist_30d_base_v122_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_brhalf_strk_5d_base_v123_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodysum_5d_base_v124_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clop_vol_norm_1d_base_v125_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodyrng_q90_30d_base_v126_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_body_mad_30d_base_v127_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_br_mad_30d_base_v128_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bullfrac_spread_60d_base_v130_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_bodybull_disagree_30d_base_v131_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_rnk_50d_base_v132_signal, "open", "high", "low", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_clhi06_strk_7d_base_v133_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bigrng_cnt_30d_base_v134_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_smallrng_cnt_30d_base_v135_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_bodyalign_30d_base_v136_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_shape_std_50d_base_v137_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_br_diff_7d_base_v138_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_upbody_kurt_30d_base_v139_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_clpos_kurt_30d_base_v140_signal, "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bullbear_emadiff_30d_base_v141_signal, "open", "close"),
    _e(f06cb_f06_candle_body_ratios_openpos_std_30d_base_v142_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_rng_z_7d_base_v143_signal, "high", "low"),
    _e(f06cb_f06_candle_body_ratios_sgnbrrat_30d_base_v144_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_shasym_rngcorr_50d_base_v145_signal, "open", "high", "low", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_no_upsh_30d_base_v146_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_no_losh_30d_base_v147_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodymad_robz_60d_base_v148_signal, "open", "closeadj"),
    _e(f06cb_f06_candle_body_ratios_shimbal_kurt_30d_base_v149_signal, "open", "high", "low", "close"),
    _e(f06cb_f06_candle_body_ratios_bodymom_ema_diff_30d_base_v150_signal, "open", "close"),
])


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f06_candle_body_ratios_base_076_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
