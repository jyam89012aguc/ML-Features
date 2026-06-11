"""
46_gap_structure — Base Features 076-150
Domain: overnight gap frequency, magnitude, fill behavior, distribution, and gap-type classification
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
Gap = (open - prior_close) / prior_close. All features backward-looking only.
Gap-type taxonomy (076-150 extension): per-type magnitude, recency, fill-within-N, distress signals.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _gap_pct(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight gap as fraction of prior close."""
    prior_close = close.shift(1)
    return _safe_div(open_ - prior_close, prior_close.abs().clip(lower=_EPS))


def _gap_up(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Up-gap magnitude; 0 on non-up-gap days."""
    return _gap_pct(close, open_).clip(lower=0)


def _gap_down(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Down-gap magnitude (positive); 0 on non-down-gap days."""
    return _gap_pct(close, open_).clip(upper=0).abs()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Gap-type classification helpers (self-contained, duplicated from file 1) ──

def _trend_direction(close: pd.Series, w: int = _TD_MON) -> pd.Series:
    """Rolling sign of price trend: +1 uptrend, -1 downtrend, 0 flat."""
    slope = close.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda x: float(np.polyfit(np.arange(len(x)), x, 1)[0]) if len(x) >= 2 else 0.0,
        raw=True
    )
    return np.sign(slope)


def _trailing_range_position(close: pd.Series, high: pd.Series, low: pd.Series,
                              open_: pd.Series, w: int = _TD_MON) -> pd.Series:
    """Open relative to prior trailing range [0=at low, 1=at high]."""
    prior_high = high.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    prior_low = low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    rng = (prior_high - prior_low).clip(lower=_EPS)
    return _safe_div(open_ - prior_low, rng).clip(0.0, 1.0)


def _vol_ratio(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    """Current volume relative to trailing w-day average (using prior bars)."""
    avg = volume.shift(1).rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=_EPS)
    return _safe_div(volume, avg)


def _trend_maturity(close: pd.Series, w: int = _TD_QTR) -> pd.Series:
    """Fraction of trailing w bars where close is above its own w-bar rolling mean."""
    rolling_mean_w = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > rolling_mean_w).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


def _common_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    inside_range = (rng_pos > 0.1) & (rng_pos < 0.9)
    return ((ag > _EPS) & (ag < 0.005) & inside_range).astype(float)


def _breakaway_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                        volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    outside_range = (rng_pos <= 0.1) | (rng_pos >= 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & outside_range & (vol_r > 1.2)).astype(float)


def _runaway_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                      volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    mid_trend = (maturity > 0.3) & (maturity < 0.72)
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    inside_range = (rng_pos > 0.1) & (rng_pos < 0.9)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & in_trend_dir & mid_trend & inside_range & (vol_r > 0.8)).astype(float)


def _exhaustion_gap_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                         volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    gap_dir = np.sign(g)
    in_trend_dir = (trend_dir == gap_dir) & (trend_dir != 0)
    maturity = _trend_maturity(close, _TD_QTR)
    late_uptrend = (trend_dir > 0) & (maturity > 0.75)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    late_trend = late_uptrend | late_downtrend
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & in_trend_dir & late_trend & (vol_r > 1.5)).astype(float)


def _exhaustion_gap_down_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                               volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    trend_dir = _trend_direction(close, _TD_MON)
    maturity = _trend_maturity(close, _TD_QTR)
    late_downtrend = (trend_dir < 0) & (maturity < 0.25)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & (g < 0) & late_downtrend & (vol_r > 1.5)).astype(float)


def _breakaway_gap_down_flag(close: pd.Series, open_: pd.Series, high: pd.Series, low: pd.Series,
                              volume: pd.Series) -> pd.Series:
    g = _gap_pct(close, open_)
    ag = g.abs()
    rng_pos = _trailing_range_position(close, high, low, open_, _TD_MON)
    vol_r = _vol_ratio(volume, _TD_MON)
    return ((ag > 0.005) & (g < 0) & (rng_pos <= 0.1) & (vol_r > 1.2)).astype(float)


def _days_since_flag(flag: pd.Series, max_lookback: int = _TD_YEAR) -> pd.Series:
    """Days elapsed since the last True bar; NaN if never in trailing max_lookback bars."""
    idx = np.arange(len(flag))
    result = np.full(len(flag), np.nan)
    flag_arr = flag.values.astype(float)
    for i in range(len(flag)):
        start = max(0, i - max_lookback + 1)
        sub = flag_arr[start: i + 1]
        hits = np.where(sub > 0)[0]
        if len(hits) > 0:
            result[i] = float(len(sub) - 1 - hits[-1])
    return pd.Series(result, index=flag.index)


# ── Feature functions 076-125: range/volume/reversal/ATR (unchanged) ──────────

# --- Group H (076-085): Gap vs intraday range relationships ---

def gap_076_gap_vs_intraday_range_ratio(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's abs gap as fraction of today's intraday range (H-L)."""
    ag = _gap_pct(close, open).abs()
    intra = (high - low) / close.shift(1).abs().clip(lower=_EPS)
    return _safe_div(ag, intra.clip(lower=_EPS))


def gap_077_gap_vs_range_ratio_21d_avg(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average of abs-gap / intraday-range ratio."""
    ag = _gap_pct(close, open).abs()
    intra = (high - low) / close.shift(1).abs().clip(lower=_EPS)
    ratio = _safe_div(ag, intra.clip(lower=_EPS))
    return _rolling_mean(ratio, _TD_MON)


def gap_078_gap_vs_range_ratio_63d_avg(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day average of abs-gap / intraday-range ratio."""
    ag = _gap_pct(close, open).abs()
    intra = (high - low) / close.shift(1).abs().clip(lower=_EPS)
    ratio = _safe_div(ag, intra.clip(lower=_EPS))
    return _rolling_mean(ratio, _TD_QTR)


def gap_079_open_vs_midpoint(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Open relative to prior day's midpoint (H+L)/2, as pct of prior close."""
    prior_mid = (high.shift(1) + low.shift(1)) / 2.0
    prior_close = close.shift(1).abs().clip(lower=_EPS)
    return _safe_div(open - prior_mid, prior_close)


def gap_080_open_vs_midpoint_21d_avg(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average of open vs prior midpoint."""
    return _rolling_mean(gap_079_open_vs_midpoint(close, open, high, low), _TD_MON)


def gap_081_gap_body_ratio(close: pd.Series, open: pd.Series) -> pd.Series:
    """Today's abs gap as fraction of prior day's abs candle body |close-open|."""
    body = (close.shift(1) - open.shift(1)).abs().clip(lower=_EPS)
    return _safe_div(_gap_pct(close, open).abs(), body / close.shift(1).abs().clip(lower=_EPS))


def gap_082_gap_body_ratio_21d_avg(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average gap-to-prior-body ratio."""
    return _rolling_mean(gap_081_gap_body_ratio(close, open), _TD_MON)


def gap_083_gap_extends_trend_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """1 if gap direction matches prior day's close-vs-open direction (gap extends trend)."""
    prior_dir = np.sign(close.shift(1) - open.shift(1))
    gap_dir = np.sign(open - close.shift(1))
    return (prior_dir == gap_dir).astype(float)


def gap_084_gap_extends_trend_freq_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days where gap extends prior-day trend."""
    return _rolling_mean(gap_083_gap_extends_trend_flag(close, open), _TD_MON)


def gap_085_gap_extends_trend_freq_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days where gap extends prior-day trend."""
    return _rolling_mean(gap_083_gap_extends_trend_flag(close, open), _TD_QTR)


# --- Group I (086-095): Gap vs volume relationship ---

def gap_086_gap_down_vol_product_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day average of (down-gap magnitude * volume) — gap-weighted selling pressure."""
    dg = _gap_down(close, open)
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return _rolling_mean(dg * vol_norm, _TD_MON)


def gap_087_gap_abs_vol_product_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day average of (abs-gap * vol-norm) — gap-weighted total activity."""
    ag = _gap_pct(close, open).abs()
    avg_vol = _rolling_mean(volume, _TD_MON)
    vol_norm = _safe_div(volume, avg_vol.clip(lower=_EPS))
    return _rolling_mean(ag * vol_norm, _TD_MON)


def gap_088_large_gap_high_vol_freq_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63 days with both abs-gap > 1% and volume > 21d avg vol."""
    ag = _gap_pct(close, open).abs()
    avg_vol = _rolling_mean(volume, _TD_MON)
    cond = (ag > 0.01) & (volume > avg_vol)
    return _rolling_count_true(cond, _TD_QTR) / _TD_QTR


def gap_089_gap_down_vol_above_avg_freq_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of down-gap days (last 63) with above-avg volume."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    dg = _gap_pct(close, open) < 0
    high_vol = volume > avg_vol
    cond = dg & high_vol
    dn_sum = _rolling_count_true(dg, _TD_QTR).clip(lower=1)
    cond_sum = _rolling_count_true(cond, _TD_QTR)
    return _safe_div(cond_sum, dn_sum)


def gap_090_gap_up_vol_below_avg_freq_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of up-gap days (last 63) with below-avg volume (weak bounces)."""
    avg_vol = _rolling_mean(volume, _TD_MON)
    ug = _gap_pct(close, open) > 0
    low_vol = volume < avg_vol
    cond = ug & low_vol
    up_sum = _rolling_count_true(ug, _TD_QTR).clip(lower=1)
    cond_sum = _rolling_count_true(cond, _TD_QTR)
    return _safe_div(cond_sum, up_sum)


def gap_091_avg_vol_on_gap_days_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on any gap day (abs-gap > 0) vs all days, 21d."""
    ag = _gap_pct(close, open).abs()
    gap_vol = volume.where(ag > _EPS, np.nan)
    return gap_vol.rolling(_TD_MON, min_periods=1).mean()


def gap_092_avg_vol_on_gap_down_days_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Average volume on down-gap days over trailing 63 days."""
    dg = _gap_pct(close, open) < 0
    gap_vol = volume.where(dg, np.nan)
    return gap_vol.rolling(_TD_QTR, min_periods=1).mean()


def gap_093_gap_vol_weighted_signed_21d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average signed gap over 21 days."""
    g = _gap_pct(close, open)
    weighted = g * volume
    vol_sum = _rolling_sum(volume, _TD_MON).clip(lower=_EPS)
    return _safe_div(_rolling_sum(weighted, _TD_MON), vol_sum)


def gap_094_gap_vol_weighted_signed_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average signed gap over 63 days."""
    g = _gap_pct(close, open)
    weighted = g * volume
    vol_sum = _rolling_sum(volume, _TD_QTR).clip(lower=_EPS)
    return _safe_div(_rolling_sum(weighted, _TD_QTR), vol_sum)


def gap_095_gap_vol_ratio_down_up_63d(close: pd.Series, open: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of avg volume on down-gap days to avg volume on up-gap days, 63d."""
    g = _gap_pct(close, open)
    dn_vol = volume.where(g < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    up_vol = volume.where(g > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(dn_vol, up_vol)


# --- Group J (096-105): Gap vs prior-day return relationship ---

def gap_096_gap_after_up_day_avg_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average signed gap on days following an up close, 63d."""
    prior_up = close.shift(1) > close.shift(2)
    g = _gap_pct(close, open)
    g_after_up = g.where(prior_up, np.nan)
    return g_after_up.rolling(_TD_QTR, min_periods=1).mean()


def gap_097_gap_after_down_day_avg_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Average signed gap on days following a down close, 63d."""
    prior_dn = close.shift(1) < close.shift(2)
    g = _gap_pct(close, open)
    g_after_dn = g.where(prior_dn, np.nan)
    return g_after_dn.rolling(_TD_QTR, min_periods=1).mean()


def gap_098_gap_after_large_down_day_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Avg signed gap after a large down day (prior-day ret < -2%), 63d."""
    prior_ret = close.shift(1).pct_change(1)
    prior_large_dn = prior_ret < -0.02
    g = _gap_pct(close, open)
    g_after = g.where(prior_large_dn, np.nan)
    return g_after.rolling(_TD_QTR, min_periods=1).mean()


def gap_099_gap_corr_with_prior_ret_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 63-day correlation between today's signed gap and prior day's return."""
    g = _gap_pct(close, open)
    prior_ret = close.pct_change(1).shift(1)
    return g.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).corr(prior_ret)


def gap_100_gap_corr_with_prior_ret_126d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Rolling 126-day correlation between signed gap and prior day's return."""
    g = _gap_pct(close, open)
    prior_ret = close.pct_change(1).shift(1)
    return g.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).corr(prior_ret)


def gap_101_gap_reversal_flag(close: pd.Series, open: pd.Series) -> pd.Series:
    """1 if today's close is in the opposite direction to the overnight gap (gap reversal)."""
    g = _gap_pct(close, open)
    intraday_ret = close - open
    reversal = (np.sign(g) != 0) & (np.sign(intraday_ret) != np.sign(g))
    return reversal.astype(float)


def gap_102_gap_reversal_freq_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 21 days where gap was reversed by end of day."""
    return _rolling_mean(gap_101_gap_reversal_flag(close, open), _TD_MON)


def gap_103_gap_reversal_freq_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of last 63 days where gap was reversed by end of day."""
    return _rolling_mean(gap_101_gap_reversal_flag(close, open), _TD_QTR)


def gap_104_gap_down_reversal_freq_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of down-gap days (last 63) where close ended above open (reversal)."""
    g = _gap_pct(close, open)
    intraday = close - open
    dn_reversal = (g < 0) & (intraday > 0)
    dn_days = g < 0
    dn_rev_sum = _rolling_count_true(dn_reversal, _TD_QTR)
    dn_sum = _rolling_count_true(dn_days, _TD_QTR).clip(lower=1)
    return _safe_div(dn_rev_sum, dn_sum)


def gap_105_gap_up_reversal_freq_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of up-gap days (last 63) where close ended below open (reversal)."""
    g = _gap_pct(close, open)
    intraday = close - open
    up_reversal = (g > 0) & (intraday < 0)
    up_days = g > 0
    up_rev_sum = _rolling_count_true(up_reversal, _TD_QTR)
    up_sum = _rolling_count_true(up_days, _TD_QTR).clip(lower=1)
    return _safe_div(up_rev_sum, up_sum)


# --- Group K (106-115): Gap vs ATR and volatility normalization ---

def gap_106_gap_vs_atr_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's abs gap normalized by 21-day ATR (gap in ATR units)."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr21 = _rolling_mean(tr, _TD_MON)
    pc = close.shift(1).abs().clip(lower=_EPS)
    atr_pct = _safe_div(atr21, pc)
    return _safe_div(_gap_pct(close, open).abs(), atr_pct.clip(lower=_EPS))


def gap_107_gap_vs_atr_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's abs gap normalized by 63-day ATR."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr63 = _rolling_mean(tr, _TD_QTR)
    pc = close.shift(1).abs().clip(lower=_EPS)
    atr_pct = _safe_div(atr63, pc)
    return _safe_div(_gap_pct(close, open).abs(), atr_pct.clip(lower=_EPS))


def gap_108_avg_gap_vs_atr_ratio_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day avg of daily (abs-gap / ATR) ratio."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    pc = close.shift(1).abs().clip(lower=_EPS)
    atr_pct = tr / pc
    ratio = _safe_div(_gap_pct(close, open).abs(), atr_pct.clip(lower=_EPS))
    return _rolling_mean(ratio, _TD_QTR)


def gap_109_gap_vol_adj_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day avg gap divided by 21-day std of close returns (vol-adjusted gap)."""
    g = _gap_pct(close, open)
    ret_std = _rolling_std(close.pct_change(1), _TD_MON)
    return _safe_div(_rolling_mean(g.abs(), _TD_MON), ret_std.clip(lower=_EPS))


def gap_110_gap_vol_adj_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day avg gap divided by 63-day std of close returns."""
    g = _gap_pct(close, open)
    ret_std = _rolling_std(close.pct_change(1), _TD_QTR)
    return _safe_div(_rolling_mean(g.abs(), _TD_QTR), ret_std.clip(lower=_EPS))


def gap_111_gap_down_vs_atr_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's down-gap magnitude normalized by 21-day ATR."""
    tr = pd.concat([high - low, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    atr21 = _rolling_mean(tr, _TD_MON)
    pc = close.shift(1).abs().clip(lower=_EPS)
    atr_pct = _safe_div(atr21, pc).clip(lower=_EPS)
    return _safe_div(_gap_down(close, open), atr_pct)


def gap_112_gap_extremity_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 21 days where abs gap exceeds 2x 21-day avg abs gap."""
    ag = _gap_pct(close, open).abs()
    avg = _rolling_mean(ag, _TD_MON)
    threshold = avg * 2.0
    return _rolling_count_true(ag > threshold, _TD_MON) / _TD_MON


def gap_113_gap_extremity_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 63 days where abs gap exceeds 2x 63-day avg abs gap."""
    ag = _gap_pct(close, open).abs()
    avg = _rolling_mean(ag, _TD_QTR)
    threshold = avg * 2.0
    return _rolling_count_true(ag > threshold, _TD_QTR) / _TD_QTR


def gap_114_gap_skew_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day skewness of signed gap distribution (tail asymmetry)."""
    g = _gap_pct(close, open)
    m = _rolling_mean(g, _TD_QTR)
    s = _rolling_std(g, _TD_QTR).clip(lower=_EPS)
    z = _safe_div(g - m, s)
    return z.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(lambda x: float(np.mean(x ** 3)), raw=True)


def gap_115_gap_skew_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """252-day skewness of signed gap distribution."""
    g = _gap_pct(close, open)
    m = _rolling_mean(g, _TD_YEAR)
    s = _rolling_std(g, _TD_YEAR).clip(lower=_EPS)
    z = _safe_div(g - m, s)
    return z.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).apply(lambda x: float(np.mean(x ** 3)), raw=True)


# --- Group L (116-125): Gap vs close-to-close return decomposition ---

def gap_116_gap_fraction_of_daily_ret_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day avg of abs-gap / abs-daily-return (how much of daily move is overnight)."""
    g = _gap_pct(close, open).abs()
    daily_ret = close.pct_change(1).abs().clip(lower=_EPS)
    return _rolling_mean(_safe_div(g, daily_ret), _TD_MON)


def gap_117_gap_fraction_of_daily_ret_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day avg of abs-gap / abs-daily-return."""
    g = _gap_pct(close, open).abs()
    daily_ret = close.pct_change(1).abs().clip(lower=_EPS)
    return _rolling_mean(_safe_div(g, daily_ret), _TD_QTR)


def gap_118_gap_vs_intraday_contribution_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day avg signed gap minus 21-day avg intraday return (open-to-close)."""
    g = _rolling_mean(_gap_pct(close, open), _TD_MON)
    intra = _rolling_mean(_safe_div(close - open, close.shift(1).abs().clip(lower=_EPS)), _TD_MON)
    return g - intra


def gap_119_gap_sum_vs_total_ret_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative gap return (63d) as fraction of total cumulative return (63d)."""
    gap_sum = _rolling_sum(_gap_pct(close, open), _TD_QTR)
    total_ret = close.pct_change(1)
    total_sum = _rolling_sum(total_ret, _TD_QTR)
    return _safe_div(gap_sum, total_sum.replace(0, np.nan))


def gap_120_gap_sum_vs_total_ret_252d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Cumulative gap return (252d) as fraction of total cumulative return (252d)."""
    gap_sum = _rolling_sum(_gap_pct(close, open), _TD_YEAR)
    total_ret = close.pct_change(1)
    total_sum = _rolling_sum(total_ret, _TD_YEAR)
    return _safe_div(gap_sum, total_sum.replace(0, np.nan))


def gap_121_intraday_ret_after_gap_down_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Avg intraday return (close-open/prior_close) on down-gap days, 63d."""
    g = _gap_pct(close, open)
    intra = _safe_div(close - open, close.shift(1).abs().clip(lower=_EPS))
    intra_on_dn = intra.where(g < 0, np.nan)
    return intra_on_dn.rolling(_TD_QTR, min_periods=1).mean()


def gap_122_intraday_ret_after_gap_up_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Avg intraday return on up-gap days, 63d."""
    g = _gap_pct(close, open)
    intra = _safe_div(close - open, close.shift(1).abs().clip(lower=_EPS))
    intra_on_up = intra.where(g > 0, np.nan)
    return intra_on_up.rolling(_TD_QTR, min_periods=1).mean()


def gap_123_overnight_to_intraday_ratio_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day avg ratio: abs overnight gap / abs intraday move."""
    ag = _gap_pct(close, open).abs()
    intra = _safe_div((close - open).abs(), close.shift(1).abs().clip(lower=_EPS))
    return _rolling_mean(_safe_div(ag, intra.clip(lower=_EPS)), _TD_QTR)


def gap_124_gap_plus_intraday_corr_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """63-day correlation between gap size and intraday return (same day)."""
    g = _gap_pct(close, open)
    intra = _safe_div(close - open, close.shift(1).abs().clip(lower=_EPS))
    return g.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).corr(intra)


def gap_125_close_to_open_vs_open_to_close_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of 63-day avg abs gap to 63-day avg abs intraday move."""
    ag = _rolling_mean(_gap_pct(close, open).abs(), _TD_QTR)
    ai = _rolling_mean(_safe_div((close - open).abs(), close.shift(1).abs().clip(lower=_EPS)), _TD_QTR)
    return _safe_div(ag, ai.clip(lower=_EPS))


# --- Group M (126-135): Gap-type per-type magnitude and fill-within-N ──────────

def gap_126_exhaustion_gap_down_mag_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                         volume: pd.Series) -> pd.Series:
    """Average magnitude of down-exhaustion gaps over trailing 63 days."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    mag_on_flag = dg.where(flag > 0, np.nan)
    return mag_on_flag.rolling(_TD_QTR, min_periods=1).mean()


def gap_127_breakaway_gap_down_mag_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Average magnitude of down-breakaway gaps over trailing 63 days."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    mag_on_flag = dg.where(flag > 0, np.nan)
    return mag_on_flag.rolling(_TD_QTR, min_periods=1).mean()


def gap_128_runaway_gap_down_mag_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                      volume: pd.Series) -> pd.Series:
    """Average magnitude of runaway down-gaps over trailing 63 days."""
    flag = _runaway_gap_flag(close, open, high, low, volume)
    dg = _gap_down(close, open)
    # Runaway down gaps: runaway flag AND gap is down
    g = _gap_pct(close, open)
    combined = (flag > 0) & (g < 0)
    mag_on_flag = dg.where(combined, np.nan)
    return mag_on_flag.rolling(_TD_QTR, min_periods=1).mean()


def gap_129_common_gap_down_mag_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Average magnitude of common down-gaps over trailing 63 days."""
    flag = _common_gap_flag(close, open, high, low)
    g = _gap_pct(close, open)
    dg = _gap_down(close, open)
    combined = (flag > 0) & (g < 0)
    mag_on_flag = dg.where(combined, np.nan)
    return mag_on_flag.rolling(_TD_QTR, min_periods=1).mean()


def gap_130_exhaustion_gap_fill_5d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                    volume: pd.Series) -> pd.Series:
    """Fraction of exhaustion gaps (5 days ago) that filled within 5 days. Backward-safe."""
    ex_flag = _exhaustion_gap_flag(close, open, high, low, volume)
    # For each bar: was there an exhaustion gap 5 days ago, and did price fill it in [t-4..t]?
    ex_flag_shifted = ex_flag.shift(_TD_WEEK)
    g_shifted = _gap_pct(close, open).shift(_TD_WEEK)
    prior_close_shifted = close.shift(1).shift(_TD_WEEK)
    roll_high = high.rolling(_TD_WEEK, min_periods=1).max()
    roll_low = low.rolling(_TD_WEEK, min_periods=1).min()
    up_filled = (g_shifted > 0) & (roll_low <= prior_close_shifted)
    dn_filled = (g_shifted < 0) & (roll_high >= prior_close_shifted)
    filled = ((up_filled | dn_filled) & (ex_flag_shifted > 0)).astype(float)
    has_ex = (ex_flag_shifted > 0).astype(float)
    return _safe_div(
        _rolling_sum(filled, _TD_QTR),
        _rolling_sum(has_ex, _TD_QTR).clip(lower=1)
    )


def gap_131_exhaustion_gap_down_fill_5d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                         volume: pd.Series) -> pd.Series:
    """Fraction of DOWN exhaustion gaps (5 days ago) that filled within 5 days."""
    ex_dn_flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ex_dn_shifted = ex_dn_flag.shift(_TD_WEEK)
    prior_close_shifted = close.shift(1).shift(_TD_WEEK)
    roll_high = high.rolling(_TD_WEEK, min_periods=1).max()
    dn_filled = (ex_dn_shifted > 0) & (roll_high >= prior_close_shifted)
    has_ex_dn = (ex_dn_shifted > 0).astype(float)
    return _safe_div(
        _rolling_sum(dn_filled.astype(float), _TD_QTR),
        _rolling_sum(has_ex_dn, _TD_QTR).clip(lower=1)
    )


def gap_132_breakaway_gap_fill_5d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                   volume: pd.Series) -> pd.Series:
    """Fraction of breakaway gaps (5 days ago) that filled within 5 days (low fill rate = strong move)."""
    ba_flag = _breakaway_gap_flag(close, open, high, low, volume)
    ba_shifted = ba_flag.shift(_TD_WEEK)
    g_shifted = _gap_pct(close, open).shift(_TD_WEEK)
    prior_close_shifted = close.shift(1).shift(_TD_WEEK)
    roll_high = high.rolling(_TD_WEEK, min_periods=1).max()
    roll_low = low.rolling(_TD_WEEK, min_periods=1).min()
    up_filled = (g_shifted > 0) & (roll_low <= prior_close_shifted)
    dn_filled = (g_shifted < 0) & (roll_high >= prior_close_shifted)
    filled = ((up_filled | dn_filled) & (ba_shifted > 0)).astype(float)
    has_ba = (ba_shifted > 0).astype(float)
    return _safe_div(
        _rolling_sum(filled, _TD_QTR),
        _rolling_sum(has_ba, _TD_QTR).clip(lower=1)
    )


def gap_133_days_since_exhaustion_gap(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                       volume: pd.Series) -> pd.Series:
    """Days elapsed since last exhaustion gap (any direction); NaN if none in 252d."""
    flag = _exhaustion_gap_flag(close, open, high, low, volume)
    return _days_since_flag(flag, _TD_YEAR)


def gap_134_days_since_exhaustion_gap_down(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Days elapsed since last DOWN exhaustion gap; NaN if none in 252d."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    return _days_since_flag(flag, _TD_YEAR)


def gap_135_days_since_breakaway_gap_down(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """Days elapsed since last DOWN breakaway gap; NaN if none in 252d."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    return _days_since_flag(flag, _TD_YEAR)


# --- Group N (136-145): Gap-type counts across windows and distress composites ---

def gap_136_exhaustion_gap_down_count_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """Count of down-exhaustion gaps in trailing 21 days."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_MON)


def gap_137_breakaway_gap_down_count_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                          volume: pd.Series) -> pd.Series:
    """Count of down-breakaway gaps in trailing 21 days."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_MON)


def gap_138_exhaustion_gap_down_count_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                            volume: pd.Series) -> pd.Series:
    """Count of down-exhaustion gaps in trailing 252 days."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_YEAR)


def gap_139_breakaway_gap_down_count_252d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """Count of down-breakaway gaps in trailing 252 days."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    return _rolling_sum(flag, _TD_YEAR)


def gap_140_exhaustion_vs_breakaway_down_ratio_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                                    volume: pd.Series) -> pd.Series:
    """Ratio of down-exhaustion count to down-breakaway count over 63 days."""
    ex = _rolling_sum(_exhaustion_gap_down_flag(close, open, high, low, volume), _TD_QTR)
    ba = _rolling_sum(_breakaway_gap_down_flag(close, open, high, low, volume), _TD_QTR)
    return _safe_div(ex, ba.clip(lower=1))


def gap_141_gap_type_distress_score_21d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                         volume: pd.Series) -> pd.Series:
    """Composite distress score: weighted sum of exhaustion-down + breakaway-down flags, 21d.
    Weights: exhaustion=2, breakaway=1 (both signal capitulation risk)."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    score = 2.0 * ex_dn + 1.0 * ba_dn
    return _rolling_sum(score, _TD_MON)


def gap_142_runaway_gap_down_count_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                        volume: pd.Series) -> pd.Series:
    """Count of runaway (continuation) down-gaps in trailing 63 days."""
    flag = _runaway_gap_flag(close, open, high, low, volume)
    g = _gap_pct(close, open)
    dn_runaway = ((flag > 0) & (g < 0)).astype(float)
    return _rolling_sum(dn_runaway, _TD_QTR)


def gap_143_gap_type_entropy_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                  volume: pd.Series) -> pd.Series:
    """Shannon entropy of gap-type distribution over 63 days (0=all one type, high=mixed).
    Types: common, breakaway, runaway, exhaustion, unclassified."""
    common = _rolling_sum(_common_gap_flag(close, open, high, low), _TD_QTR)
    ba = _rolling_sum(_breakaway_gap_flag(close, open, high, low, volume), _TD_QTR)
    run = _rolling_sum(_runaway_gap_flag(close, open, high, low, volume), _TD_QTR)
    ex = _rolling_sum(_exhaustion_gap_flag(close, open, high, low, volume), _TD_QTR)
    g = _gap_pct(close, open)
    has_gap = _rolling_sum((g.abs() > _EPS).astype(float), _TD_QTR)
    classified = (common + ba + run + ex).clip(upper=has_gap)
    unclassified = (has_gap - classified).clip(lower=0)
    total = has_gap.clip(lower=1)
    counts = pd.concat([common, ba, run, ex, unclassified], axis=1)
    def entropy_row(row):
        total_r = row.sum()
        if total_r <= 0:
            return np.nan
        probs = row / total_r
        probs = probs[probs > 0]
        return float(-np.sum(probs * np.log(probs + _EPS)))
    return counts.apply(entropy_row, axis=1)


def gap_144_exhaustion_gap_down_vol_excess_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                                volume: pd.Series) -> pd.Series:
    """Average volume ratio on down-exhaustion gap days over 63 days (climactic vol measure)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_ex = vol_r.where(flag > 0, np.nan)
    return vol_on_ex.rolling(_TD_QTR, min_periods=1).mean()


def gap_145_breakaway_gap_down_vol_excess_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                               volume: pd.Series) -> pd.Series:
    """Average volume ratio on down-breakaway gap days over 63 days."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    vol_r = _vol_ratio(volume, _TD_MON)
    vol_on_ba = vol_r.where(flag > 0, np.nan)
    return vol_on_ba.rolling(_TD_QTR, min_periods=1).mean()


# --- Group O (146-150): Slope and trend of gap-type metrics ---

def gap_146_gap_abs_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of abs gap over trailing 21 days (trending larger or smaller)."""
    return _linslope(_gap_pct(close, open).abs(), _TD_MON)


def gap_147_gap_abs_slope_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope of abs gap over trailing 63 days."""
    return _linslope(_gap_pct(close, open).abs(), _TD_QTR)


def gap_148_exhaustion_gap_down_slope_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                           volume: pd.Series) -> pd.Series:
    """OLS slope of down-exhaustion gap flag over trailing 63 days (trend in exhaustion frequency)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    return _linslope(flag, _TD_QTR)


def gap_149_gap_distress_score_slope_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series,
                                          volume: pd.Series) -> pd.Series:
    """OLS slope of 21-day distress score over 63 days (accelerating capitulation signal)."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    score_raw = 2.0 * ex_dn + 1.0 * ba_dn
    score_21 = _rolling_sum(score_raw, _TD_MON)
    return _linslope(score_21, _TD_QTR)


def gap_150_gap_fill_rate_slope_63d(close: pd.Series, open: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of rolling 21-day gap-fill frequency over trailing 63 days."""
    prior_close = close.shift(1)
    gap = open - prior_close
    filled = ((gap > 0) & (low <= prior_close) | (gap < 0) & (high >= prior_close)).astype(float)
    fill_rate = _rolling_mean(filled, _TD_MON)
    return _linslope(fill_rate, _TD_QTR)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_STRUCTURE_REGISTRY_076_150 = {
    "gap_076_gap_vs_intraday_range_ratio": {"inputs": ["close", "open", "high", "low"], "func": gap_076_gap_vs_intraday_range_ratio},
    "gap_077_gap_vs_range_ratio_21d_avg": {"inputs": ["close", "open", "high", "low"], "func": gap_077_gap_vs_range_ratio_21d_avg},
    "gap_078_gap_vs_range_ratio_63d_avg": {"inputs": ["close", "open", "high", "low"], "func": gap_078_gap_vs_range_ratio_63d_avg},
    "gap_079_open_vs_midpoint": {"inputs": ["close", "open", "high", "low"], "func": gap_079_open_vs_midpoint},
    "gap_080_open_vs_midpoint_21d_avg": {"inputs": ["close", "open", "high", "low"], "func": gap_080_open_vs_midpoint_21d_avg},
    "gap_081_gap_body_ratio": {"inputs": ["close", "open"], "func": gap_081_gap_body_ratio},
    "gap_082_gap_body_ratio_21d_avg": {"inputs": ["close", "open"], "func": gap_082_gap_body_ratio_21d_avg},
    "gap_083_gap_extends_trend_flag": {"inputs": ["close", "open"], "func": gap_083_gap_extends_trend_flag},
    "gap_084_gap_extends_trend_freq_21d": {"inputs": ["close", "open"], "func": gap_084_gap_extends_trend_freq_21d},
    "gap_085_gap_extends_trend_freq_63d": {"inputs": ["close", "open"], "func": gap_085_gap_extends_trend_freq_63d},
    "gap_086_gap_down_vol_product_21d": {"inputs": ["close", "open", "volume"], "func": gap_086_gap_down_vol_product_21d},
    "gap_087_gap_abs_vol_product_21d": {"inputs": ["close", "open", "volume"], "func": gap_087_gap_abs_vol_product_21d},
    "gap_088_large_gap_high_vol_freq_63d": {"inputs": ["close", "open", "volume"], "func": gap_088_large_gap_high_vol_freq_63d},
    "gap_089_gap_down_vol_above_avg_freq_63d": {"inputs": ["close", "open", "volume"], "func": gap_089_gap_down_vol_above_avg_freq_63d},
    "gap_090_gap_up_vol_below_avg_freq_63d": {"inputs": ["close", "open", "volume"], "func": gap_090_gap_up_vol_below_avg_freq_63d},
    "gap_091_avg_vol_on_gap_days_21d": {"inputs": ["close", "open", "volume"], "func": gap_091_avg_vol_on_gap_days_21d},
    "gap_092_avg_vol_on_gap_down_days_63d": {"inputs": ["close", "open", "volume"], "func": gap_092_avg_vol_on_gap_down_days_63d},
    "gap_093_gap_vol_weighted_signed_21d": {"inputs": ["close", "open", "volume"], "func": gap_093_gap_vol_weighted_signed_21d},
    "gap_094_gap_vol_weighted_signed_63d": {"inputs": ["close", "open", "volume"], "func": gap_094_gap_vol_weighted_signed_63d},
    "gap_095_gap_vol_ratio_down_up_63d": {"inputs": ["close", "open", "volume"], "func": gap_095_gap_vol_ratio_down_up_63d},
    "gap_096_gap_after_up_day_avg_63d": {"inputs": ["close", "open"], "func": gap_096_gap_after_up_day_avg_63d},
    "gap_097_gap_after_down_day_avg_63d": {"inputs": ["close", "open"], "func": gap_097_gap_after_down_day_avg_63d},
    "gap_098_gap_after_large_down_day_63d": {"inputs": ["close", "open"], "func": gap_098_gap_after_large_down_day_63d},
    "gap_099_gap_corr_with_prior_ret_63d": {"inputs": ["close", "open"], "func": gap_099_gap_corr_with_prior_ret_63d},
    "gap_100_gap_corr_with_prior_ret_126d": {"inputs": ["close", "open"], "func": gap_100_gap_corr_with_prior_ret_126d},
    "gap_101_gap_reversal_flag": {"inputs": ["close", "open"], "func": gap_101_gap_reversal_flag},
    "gap_102_gap_reversal_freq_21d": {"inputs": ["close", "open"], "func": gap_102_gap_reversal_freq_21d},
    "gap_103_gap_reversal_freq_63d": {"inputs": ["close", "open"], "func": gap_103_gap_reversal_freq_63d},
    "gap_104_gap_down_reversal_freq_63d": {"inputs": ["close", "open"], "func": gap_104_gap_down_reversal_freq_63d},
    "gap_105_gap_up_reversal_freq_63d": {"inputs": ["close", "open"], "func": gap_105_gap_up_reversal_freq_63d},
    "gap_106_gap_vs_atr_21d": {"inputs": ["close", "open", "high", "low"], "func": gap_106_gap_vs_atr_21d},
    "gap_107_gap_vs_atr_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_107_gap_vs_atr_63d},
    "gap_108_avg_gap_vs_atr_ratio_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_108_avg_gap_vs_atr_ratio_63d},
    "gap_109_gap_vol_adj_21d": {"inputs": ["close", "open"], "func": gap_109_gap_vol_adj_21d},
    "gap_110_gap_vol_adj_63d": {"inputs": ["close", "open"], "func": gap_110_gap_vol_adj_63d},
    "gap_111_gap_down_vs_atr_21d": {"inputs": ["close", "open", "high", "low"], "func": gap_111_gap_down_vs_atr_21d},
    "gap_112_gap_extremity_21d": {"inputs": ["close", "open"], "func": gap_112_gap_extremity_21d},
    "gap_113_gap_extremity_63d": {"inputs": ["close", "open"], "func": gap_113_gap_extremity_63d},
    "gap_114_gap_skew_63d": {"inputs": ["close", "open"], "func": gap_114_gap_skew_63d},
    "gap_115_gap_skew_252d": {"inputs": ["close", "open"], "func": gap_115_gap_skew_252d},
    "gap_116_gap_fraction_of_daily_ret_21d": {"inputs": ["close", "open"], "func": gap_116_gap_fraction_of_daily_ret_21d},
    "gap_117_gap_fraction_of_daily_ret_63d": {"inputs": ["close", "open"], "func": gap_117_gap_fraction_of_daily_ret_63d},
    "gap_118_gap_vs_intraday_contribution_21d": {"inputs": ["close", "open"], "func": gap_118_gap_vs_intraday_contribution_21d},
    "gap_119_gap_sum_vs_total_ret_63d": {"inputs": ["close", "open"], "func": gap_119_gap_sum_vs_total_ret_63d},
    "gap_120_gap_sum_vs_total_ret_252d": {"inputs": ["close", "open"], "func": gap_120_gap_sum_vs_total_ret_252d},
    "gap_121_intraday_ret_after_gap_down_63d": {"inputs": ["close", "open"], "func": gap_121_intraday_ret_after_gap_down_63d},
    "gap_122_intraday_ret_after_gap_up_63d": {"inputs": ["close", "open"], "func": gap_122_intraday_ret_after_gap_up_63d},
    "gap_123_overnight_to_intraday_ratio_63d": {"inputs": ["close", "open"], "func": gap_123_overnight_to_intraday_ratio_63d},
    "gap_124_gap_plus_intraday_corr_63d": {"inputs": ["close", "open"], "func": gap_124_gap_plus_intraday_corr_63d},
    "gap_125_close_to_open_vs_open_to_close_63d": {"inputs": ["close", "open"], "func": gap_125_close_to_open_vs_open_to_close_63d},
    "gap_126_exhaustion_gap_down_mag_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_126_exhaustion_gap_down_mag_63d},
    "gap_127_breakaway_gap_down_mag_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_127_breakaway_gap_down_mag_63d},
    "gap_128_runaway_gap_down_mag_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_128_runaway_gap_down_mag_63d},
    "gap_129_common_gap_down_mag_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_129_common_gap_down_mag_63d},
    "gap_130_exhaustion_gap_fill_5d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_130_exhaustion_gap_fill_5d},
    "gap_131_exhaustion_gap_down_fill_5d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_131_exhaustion_gap_down_fill_5d},
    "gap_132_breakaway_gap_fill_5d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_132_breakaway_gap_fill_5d},
    "gap_133_days_since_exhaustion_gap": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_133_days_since_exhaustion_gap},
    "gap_134_days_since_exhaustion_gap_down": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_134_days_since_exhaustion_gap_down},
    "gap_135_days_since_breakaway_gap_down": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_135_days_since_breakaway_gap_down},
    "gap_136_exhaustion_gap_down_count_21d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_136_exhaustion_gap_down_count_21d},
    "gap_137_breakaway_gap_down_count_21d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_137_breakaway_gap_down_count_21d},
    "gap_138_exhaustion_gap_down_count_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_138_exhaustion_gap_down_count_252d},
    "gap_139_breakaway_gap_down_count_252d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_139_breakaway_gap_down_count_252d},
    "gap_140_exhaustion_vs_breakaway_down_ratio_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_140_exhaustion_vs_breakaway_down_ratio_63d},
    "gap_141_gap_type_distress_score_21d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_141_gap_type_distress_score_21d},
    "gap_142_runaway_gap_down_count_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_142_runaway_gap_down_count_63d},
    "gap_143_gap_type_entropy_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_143_gap_type_entropy_63d},
    "gap_144_exhaustion_gap_down_vol_excess_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_144_exhaustion_gap_down_vol_excess_63d},
    "gap_145_breakaway_gap_down_vol_excess_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_145_breakaway_gap_down_vol_excess_63d},
    "gap_146_gap_abs_slope_21d": {"inputs": ["close", "open"], "func": gap_146_gap_abs_slope_21d},
    "gap_147_gap_abs_slope_63d": {"inputs": ["close", "open"], "func": gap_147_gap_abs_slope_63d},
    "gap_148_exhaustion_gap_down_slope_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_148_exhaustion_gap_down_slope_63d},
    "gap_149_gap_distress_score_slope_63d": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_149_gap_distress_score_slope_63d},
    "gap_150_gap_fill_rate_slope_63d": {"inputs": ["close", "open", "high", "low"], "func": gap_150_gap_fill_rate_slope_63d},
}
