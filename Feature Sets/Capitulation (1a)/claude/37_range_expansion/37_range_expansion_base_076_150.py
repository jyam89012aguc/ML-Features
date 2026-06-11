"""
37_range_expansion — Base Features 076-150
Domain: true-range expansion near the low — TR acceleration, range-expansion
        percentile ranks, multi-window ATR spread, volume-weighted range, gap
        contribution to TR, high-low vs open-close decomposition, rolling max
        TR ratios, NR7/NR4/WR7/WR4 narrow/wide-range patterns, inside-bar and
        outside-bar signatures, and NR-then-expansion sequences
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range: max of H-L, |H-prevC|, |L-prevC|."""
    prev_c = close.shift(1)
    return pd.concat([
        high - low,
        (high - prev_c).abs(),
        (low  - prev_c).abs(),
    ], axis=1).max(axis=1)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c     = cond.astype(int)
    group = (~cond).cumsum()
    return c.groupby(group).cumsum().astype(float)


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    """Count of True values in trailing w periods."""
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi  = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _days_since(cond: pd.Series) -> pd.Series:
    """Number of bars since last True in cond (0 = today is True)."""
    out = pd.Series(np.nan, index=cond.index, dtype=float)
    last = -1
    for i, v in enumerate(cond):
        if v:
            last = i
        if last >= 0:
            out.iloc[i] = i - last
    return out


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-088): Range acceleration — TR change over time ---

def rex_076_tr_5d_pct_change(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day percentage change in TR (short-term range acceleration)."""
    tr = _tr(close, high, low)
    return tr.pct_change(_TD_WEEK)


def rex_077_tr_21d_pct_change(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day percentage change in TR."""
    tr = _tr(close, high, low)
    return tr.pct_change(_TD_MON)


def rex_078_atr21_5d_pct_change(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day percentage change in 21-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return atr.pct_change(_TD_WEEK)


def rex_079_atr21_21d_pct_change(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day percentage change in 21-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return atr.pct_change(_TD_MON)


def rex_080_atr63_21d_pct_change(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day percentage change in 63-day ATR."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return atr.pct_change(_TD_MON)


def rex_081_tr_diff_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day absolute difference in TR."""
    tr = _tr(close, high, low)
    return tr.diff(_TD_WEEK)


def rex_082_tr_diff_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day absolute difference in TR."""
    tr = _tr(close, high, low)
    return tr.diff(_TD_MON)


def rex_083_atr21_slope_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21-day ATR over a trailing 21-day window."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _linslope(atr, _TD_MON)


def rex_084_atr21_slope_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of 21-day ATR over a trailing 63-day window."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _linslope(atr, _TD_QTR)


def rex_085_tr_acceleration_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5-day TR change (second derivative of range)."""
    tr   = _tr(close, high, low)
    vel  = tr.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def rex_086_atr21_zscore_vs_atr252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of current 21-day ATR relative to 252-day distribution of ATR21."""
    tr   = _tr(close, high, low)
    atr  = _rolling_mean(tr, _TD_MON)
    m    = _rolling_mean(atr, _TD_YEAR)
    s    = _rolling_std(atr, _TD_YEAR)
    return _safe_div(atr - m, s)


def rex_087_hl_5d_pct_change(high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day percentage change in H-L range."""
    hl = high - low
    return hl.pct_change(_TD_WEEK)


def rex_088_hl_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of H-L range over trailing 21 days."""
    hl = high - low
    return _linslope(hl, _TD_MON)


# --- Group H (089-100): Multi-window ATR spread and structural ratios ---

def rex_089_atr5_minus_atr63_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Spread (ATR5 - ATR63) normalized by ATR63."""
    tr    = _tr(close, high, low)
    atr5  = _rolling_mean(tr, _TD_WEEK)
    atr63 = _rolling_mean(tr, _TD_QTR)
    return _safe_div(atr5 - atr63, atr63)


def rex_090_atr21_minus_atr252_norm(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Spread (ATR21 - ATR252) normalized by ATR252."""
    tr     = _tr(close, high, low)
    atr21  = _rolling_mean(tr, _TD_MON)
    atr252 = _rolling_mean(tr, _TD_YEAR)
    return _safe_div(atr21 - atr252, atr252)


def rex_091_atr_term_structure_5_21_63(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Weighted term-structure score: (ATR5/ATR21 + ATR21/ATR63) / 2."""
    tr    = _tr(close, high, low)
    atr5  = _rolling_mean(tr, _TD_WEEK)
    atr21 = _rolling_mean(tr, _TD_MON)
    atr63 = _rolling_mean(tr, _TD_QTR)
    r1    = _safe_div(atr5,  atr21)
    r2    = _safe_div(atr21, atr63)
    return (r1 + r2) / 2.0


def rex_092_max_atr21_252d_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of current ATR21 within 252-day ATR21 history."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return atr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_093_max_atr63_252d_pct_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of current ATR63 within 252-day ATR63 history."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_QTR)
    return atr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_094_atr21_expanding_max_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Current ATR21 as fraction of all-time expanding maximum ATR21."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return _safe_div(atr, atr.expanding(min_periods=1).max())


def rex_095_hl_to_tr_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """H-L / TR ratio — gap contribution: <1 means gap adds to TR beyond H-L."""
    tr = _tr(close, high, low)
    hl = high - low
    return _safe_div(hl, tr)


def rex_096_gap_contribution_to_tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of TR explained by overnight gap: (TR - HL) / TR."""
    tr = _tr(close, high, low)
    hl = high - low
    return _safe_div(tr - hl, tr).clip(lower=0)


def rex_097_gap_contribution_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day average fraction of TR from overnight gap."""
    tr  = _tr(close, high, low)
    hl  = high - low
    gap = _safe_div(tr - hl, tr).clip(lower=0)
    return _rolling_mean(gap, _TD_MON)


def rex_098_oc_range_vs_hl(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Ratio of |open-close| to H-L range (body vs full bar)."""
    body = (close - open).abs()
    hl   = (high - low).replace(0, np.nan)
    return body / hl


def rex_099_oc_range_21d_avg(close: pd.Series, high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21-day average |open-close| as fraction of H-L."""
    body = (close - open).abs()
    hl   = (high - low).replace(0, np.nan)
    ratio = body / hl
    return _rolling_mean(ratio, _TD_MON)


def rex_100_upper_shadow_vs_hl(high: pd.Series, low: pd.Series, close: pd.Series, open: pd.Series) -> pd.Series:
    """Upper shadow (H - max(O,C)) as fraction of H-L (rejection zone size)."""
    body_top = pd.concat([close, open], axis=1).max(axis=1)
    upper    = (high - body_top).clip(lower=0)
    hl       = (high - low).replace(0, np.nan)
    return upper / hl


# --- Group I (101-112): Volume-weighted and volume-interaction range features ---

def rex_101_vwap_tr_vs_atr21(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted TR (TR*vol) / 21-day avg of (TR*vol)."""
    tr    = _tr(close, high, low)
    vwtr  = tr * volume
    avg   = _rolling_mean(vwtr, _TD_MON)
    return _safe_div(vwtr, avg)


def rex_102_vol_weighted_hl_ratio_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted H-L / 21-day avg volume-weighted H-L."""
    vwhl = (high - low) * volume
    avg  = _rolling_mean(vwhl, _TD_MON)
    return _safe_div(vwhl, avg)


def rex_103_expansion_on_high_volume_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of last 21 days where TR > ATR21 AND volume > 21-day avg vol."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    cond  = (tr > atr) & (volume > avg_v)
    return _rolling_count_true(cond, _TD_MON)


def rex_104_expansion_on_high_volume_63d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of last 63 days where TR > ATR21 AND volume > 21-day avg vol."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    cond  = (tr > atr) & (volume > avg_v)
    return _rolling_count_true(cond, _TD_QTR)


def rex_105_expansion_high_vol_fraction_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21 days with TR expansion AND high volume."""
    return rex_103_expansion_on_high_volume_21d(close, high, low, volume) / _TD_MON


def rex_106_high_vol_expansion_consec(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Consecutive days of TR > ATR21 AND volume > 21-day avg vol."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    cond  = (tr > atr) & (volume > avg_v)
    return _consec_streak(cond)


def rex_107_tr_vol_product_zscore_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of TR*volume product relative to 21-day distribution."""
    tr  = _tr(close, high, low)
    tv  = tr * volume
    m   = _rolling_mean(tv, _TD_MON)
    s   = _rolling_std(tv, _TD_MON)
    return _safe_div(tv - m, s)


def rex_108_tr_vol_product_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of TR*volume within trailing 252-day history."""
    tr = _tr(close, high, low)
    tv = tr * volume
    return tv.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_109_vol_normalized_hl_21d_avg(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day avg of (H-L) / 21-day avg volume (range per unit volume)."""
    hl    = high - low
    avg_v = _rolling_mean(volume, _TD_MON)
    return _rolling_mean(_safe_div(hl, avg_v), _TD_MON)


def rex_110_expansion_low_volume_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of last 21 days where TR > ATR21 AND volume < 21-day avg vol (suspect)."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    cond  = (tr > atr) & (volume < avg_v)
    return _rolling_count_true(cond, _TD_MON)


def rex_111_high_vol_expansion_near_low_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of last 21 days: TR > ATR21, vol > avg vol, close in lowest 20% of 63-day range."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    avg_v = _rolling_mean(volume, _TD_MON)
    lo63  = _rolling_min(close, _TD_QTR)
    hi63  = _rolling_max(close, _TD_QTR)
    rng   = (hi63 - lo63).replace(0, np.nan)
    pos   = (close - lo63) / rng
    cond  = (tr > atr) & (volume > avg_v) & (pos <= 0.20)
    return _rolling_count_true(cond, _TD_MON)


def rex_112_tr_vol_corr_21d(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day rolling correlation between TR and volume."""
    tr = _tr(close, high, low)
    return tr.rolling(_TD_MON, min_periods=max(2, _TD_MON // 2)).corr(volume)


# --- Group J (113-125): Rolling max TR ratios and spike flags ---

def rex_113_tr_vs_max_tr_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR as fraction of 21-day rolling max TR."""
    tr   = _tr(close, high, low)
    mx21 = _rolling_max(tr, _TD_MON)
    return _safe_div(tr, mx21)


def rex_114_tr_vs_max_tr_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR as fraction of 63-day rolling max TR."""
    tr   = _tr(close, high, low)
    mx63 = _rolling_max(tr, _TD_QTR)
    return _safe_div(tr, mx63)


def rex_115_tr_vs_max_tr_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR as fraction of 252-day rolling max TR."""
    tr    = _tr(close, high, low)
    mx252 = _rolling_max(tr, _TD_YEAR)
    return _safe_div(tr, mx252)


def rex_116_max_tr_21d_vs_atr252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max 21-day TR divided by 252-day ATR."""
    tr    = _tr(close, high, low)
    mx21  = _rolling_max(tr, _TD_MON)
    atr   = _rolling_mean(tr, _TD_YEAR)
    return _safe_div(mx21, atr)


def rex_117_max_tr_63d_vs_atr252(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Max 63-day TR divided by 252-day ATR."""
    tr   = _tr(close, high, low)
    mx63 = _rolling_max(tr, _TD_QTR)
    atr  = _rolling_mean(tr, _TD_YEAR)
    return _safe_div(mx63, atr)


def rex_118_max_tr_21d_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of 21-day max TR within 252-day history of max-TR-21d."""
    tr   = _tr(close, high, low)
    mx21 = _rolling_max(tr, _TD_MON)
    return mx21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_119_tr_spike_flag_3x_atr21(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Binary: today's TR > 3x 21-day ATR (major range spike)."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return (tr > 3 * atr).astype(float)


def rex_120_tr_spike_count_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TR > 3x ATR21 events in trailing 63 days."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    spike = tr > 3 * atr
    return _rolling_count_true(spike, _TD_QTR)


def rex_121_tr_spike_count_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of TR > 3x ATR21 events in trailing 252 days."""
    tr    = _tr(close, high, low)
    atr   = _rolling_mean(tr, _TD_MON)
    spike = tr > 3 * atr
    return _rolling_count_true(spike, _TD_YEAR)


def rex_122_tr_expanding_max_ratio(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Today's TR as fraction of expanding (all-time) maximum TR."""
    tr = _tr(close, high, low)
    return _safe_div(tr, tr.expanding(min_periods=1).max())


def rex_123_atr21_pct_rank_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of ATR21 within 252-day history of ATR21."""
    tr  = _tr(close, high, low)
    atr = _rolling_mean(tr, _TD_MON)
    return atr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_124_hl_pct_rank_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Percentile rank of today's H-L range within trailing 252-day H-L series."""
    hl = high - low
    return hl.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def rex_125_max_tr_21d_expanding_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21-day max TR (all-history extremity)."""
    tr   = _tr(close, high, low)
    mx21 = _rolling_max(tr, _TD_MON)
    return mx21.expanding(min_periods=5).rank(pct=True)


# --- Group K (126-137): NR7 / NR4 / WR7 / WR4 narrow and wide range patterns ---

def rex_126_nr7_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR7 flag: today's H-L range is the narrowest of the last 7 bars."""
    hl    = high - low
    min7  = hl.rolling(7, min_periods=4).min()
    return (hl <= min7).astype(float)


def rex_127_nr4_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """NR4 flag: today's H-L range is the narrowest of the last 4 bars."""
    hl   = high - low
    min4 = hl.rolling(4, min_periods=2).min()
    return (hl <= min4).astype(float)


def rex_128_wr7_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR7 flag: today's H-L range is the widest of the last 7 bars."""
    hl   = high - low
    max7 = hl.rolling(7, min_periods=4).max()
    return (hl >= max7).astype(float)


def rex_129_wr4_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """WR4 flag: today's H-L range is the widest of the last 4 bars."""
    hl   = high - low
    max4 = hl.rolling(4, min_periods=2).max()
    return (hl >= max4).astype(float)


def rex_130_nr7_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 days in the trailing 21-day window."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    flag = (hl <= min7).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rex_131_nr7_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of NR7 days in the trailing 63-day window."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    flag = (hl <= min7).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_132_wr7_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of WR7 days in the trailing 21-day window."""
    hl   = high - low
    max7 = hl.rolling(7, min_periods=4).max()
    flag = (hl >= max7).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rex_133_wr7_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of WR7 days in the trailing 63-day window."""
    hl   = high - low
    max7 = hl.rolling(7, min_periods=4).max()
    flag = (hl >= max7).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_134_days_since_nr7(high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of bars since the most recent NR7 day (0 = today is NR7)."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    flag = (hl <= min7)
    return _days_since(flag)


def rex_135_days_since_wr7(high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of bars since the most recent WR7 day (0 = today is WR7)."""
    hl   = high - low
    max7 = hl.rolling(7, min_periods=4).max()
    flag = (hl >= max7)
    return _days_since(flag)


def rex_136_nr7_consec_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive NR7 streak length (bars of contraction)."""
    hl   = high - low
    min7 = hl.rolling(7, min_periods=4).min()
    flag = (hl <= min7)
    return _consec_streak(flag)


def rex_137_nr_then_expansion_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: yesterday was NR7 AND today's range > yesterday's range (NR7 breakout)."""
    hl      = high - low
    min7    = hl.rolling(7, min_periods=4).min()
    was_nr7 = (hl.shift(1) <= min7.shift(1))
    expanded = hl > hl.shift(1)
    return (was_nr7 & expanded).astype(float)


# --- Group L (138-150): Inside bar and outside bar patterns ---

def rex_138_inside_bar_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside bar flag: today's high <= prior high AND today's low >= prior low."""
    return ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)


def rex_139_outside_bar_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Outside bar flag: today's high > prior high AND today's low < prior low."""
    return ((high > high.shift(1)) & (low < low.shift(1))).astype(float)


def rex_140_inside_bar_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of inside bars in the trailing 21-day window."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rex_141_inside_bar_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of inside bars in the trailing 63-day window."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_142_inside_bar_count_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of inside bars in the trailing 252-day window."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def rex_143_outside_bar_count_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of outside bars in the trailing 21-day window."""
    flag = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    return _rolling_sum(flag, _TD_MON)


def rex_144_outside_bar_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of outside bars in the trailing 63-day window."""
    flag = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_145_consec_inside_bar_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Current consecutive inside bar streak length (consolidation depth)."""
    flag = (high <= high.shift(1)) & (low >= low.shift(1))
    return _consec_streak(flag)


def rex_146_outside_after_inside_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: yesterday was inside bar AND today is outside bar (range-expansion breakout)."""
    ib_yesterday = (high.shift(1) <= high.shift(2)) & (low.shift(1) >= low.shift(2))
    ob_today     = (high > high.shift(1)) & (low < low.shift(1))
    return (ib_yesterday & ob_today).astype(float)


def rex_147_outside_after_inside_count_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of outside-after-inside bar events in trailing 63-day window."""
    ib_yesterday = (high.shift(1) <= high.shift(2)) & (low.shift(1) >= low.shift(2))
    ob_today     = (high > high.shift(1)) & (low < low.shift(1))
    flag = (ib_yesterday & ob_today).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def rex_148_inside_bar_fraction_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 bars that were inside bars (consolidation density)."""
    flag = ((high <= high.shift(1)) & (low >= low.shift(1))).astype(float)
    return _rolling_mean(flag, _TD_MON)


def rex_149_days_since_inside_bar(high: pd.Series, low: pd.Series) -> pd.Series:
    """Number of bars since the most recent inside bar (0 = today is inside bar)."""
    flag = (high <= high.shift(1)) & (low >= low.shift(1))
    return _days_since(flag)


def rex_150_wr7_after_nr7_expansion_ratio(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of H-L range to the prior NR7 range — expansion magnitude from compression."""
    hl      = high - low
    min7    = hl.rolling(7, min_periods=4).min()
    was_nr7 = (hl.shift(1) <= min7.shift(1))
    nr7_hl  = hl.shift(1).where(was_nr7, np.nan).ffill()
    return _safe_div(hl, nr7_hl)


# ── Registry ──────────────────────────────────────────────────────────────────

RANGE_EXPANSION_REGISTRY_076_150 = {
    "rex_076_tr_5d_pct_change": {"inputs": ["close", "high", "low"], "func": rex_076_tr_5d_pct_change},
    "rex_077_tr_21d_pct_change": {"inputs": ["close", "high", "low"], "func": rex_077_tr_21d_pct_change},
    "rex_078_atr21_5d_pct_change": {"inputs": ["close", "high", "low"], "func": rex_078_atr21_5d_pct_change},
    "rex_079_atr21_21d_pct_change": {"inputs": ["close", "high", "low"], "func": rex_079_atr21_21d_pct_change},
    "rex_080_atr63_21d_pct_change": {"inputs": ["close", "high", "low"], "func": rex_080_atr63_21d_pct_change},
    "rex_081_tr_diff_5d": {"inputs": ["close", "high", "low"], "func": rex_081_tr_diff_5d},
    "rex_082_tr_diff_21d": {"inputs": ["close", "high", "low"], "func": rex_082_tr_diff_21d},
    "rex_083_atr21_slope_21d": {"inputs": ["close", "high", "low"], "func": rex_083_atr21_slope_21d},
    "rex_084_atr21_slope_63d": {"inputs": ["close", "high", "low"], "func": rex_084_atr21_slope_63d},
    "rex_085_tr_acceleration_5d": {"inputs": ["close", "high", "low"], "func": rex_085_tr_acceleration_5d},
    "rex_086_atr21_zscore_vs_atr252": {"inputs": ["close", "high", "low"], "func": rex_086_atr21_zscore_vs_atr252},
    "rex_087_hl_5d_pct_change": {"inputs": ["high", "low"], "func": rex_087_hl_5d_pct_change},
    "rex_088_hl_slope_21d": {"inputs": ["high", "low"], "func": rex_088_hl_slope_21d},
    "rex_089_atr5_minus_atr63_norm": {"inputs": ["close", "high", "low"], "func": rex_089_atr5_minus_atr63_norm},
    "rex_090_atr21_minus_atr252_norm": {"inputs": ["close", "high", "low"], "func": rex_090_atr21_minus_atr252_norm},
    "rex_091_atr_term_structure_5_21_63": {"inputs": ["close", "high", "low"], "func": rex_091_atr_term_structure_5_21_63},
    "rex_092_max_atr21_252d_pct_rank": {"inputs": ["close", "high", "low"], "func": rex_092_max_atr21_252d_pct_rank},
    "rex_093_max_atr63_252d_pct_rank": {"inputs": ["close", "high", "low"], "func": rex_093_max_atr63_252d_pct_rank},
    "rex_094_atr21_expanding_max_ratio": {"inputs": ["close", "high", "low"], "func": rex_094_atr21_expanding_max_ratio},
    "rex_095_hl_to_tr_ratio": {"inputs": ["close", "high", "low"], "func": rex_095_hl_to_tr_ratio},
    "rex_096_gap_contribution_to_tr": {"inputs": ["close", "high", "low"], "func": rex_096_gap_contribution_to_tr},
    "rex_097_gap_contribution_21d_avg": {"inputs": ["close", "high", "low"], "func": rex_097_gap_contribution_21d_avg},
    "rex_098_oc_range_vs_hl": {"inputs": ["close", "high", "low", "open"], "func": rex_098_oc_range_vs_hl},
    "rex_099_oc_range_21d_avg": {"inputs": ["close", "high", "low", "open"], "func": rex_099_oc_range_21d_avg},
    "rex_100_upper_shadow_vs_hl": {"inputs": ["high", "low", "close", "open"], "func": rex_100_upper_shadow_vs_hl},
    "rex_101_vwap_tr_vs_atr21": {"inputs": ["close", "high", "low", "volume"], "func": rex_101_vwap_tr_vs_atr21},
    "rex_102_vol_weighted_hl_ratio_21d": {"inputs": ["high", "low", "volume"], "func": rex_102_vol_weighted_hl_ratio_21d},
    "rex_103_expansion_on_high_volume_21d": {"inputs": ["close", "high", "low", "volume"], "func": rex_103_expansion_on_high_volume_21d},
    "rex_104_expansion_on_high_volume_63d": {"inputs": ["close", "high", "low", "volume"], "func": rex_104_expansion_on_high_volume_63d},
    "rex_105_expansion_high_vol_fraction_21d": {"inputs": ["close", "high", "low", "volume"], "func": rex_105_expansion_high_vol_fraction_21d},
    "rex_106_high_vol_expansion_consec": {"inputs": ["close", "high", "low", "volume"], "func": rex_106_high_vol_expansion_consec},
    "rex_107_tr_vol_product_zscore_21d": {"inputs": ["close", "high", "low", "volume"], "func": rex_107_tr_vol_product_zscore_21d},
    "rex_108_tr_vol_product_pct_rank_252d": {"inputs": ["close", "high", "low", "volume"], "func": rex_108_tr_vol_product_pct_rank_252d},
    "rex_109_vol_normalized_hl_21d_avg": {"inputs": ["high", "low", "volume"], "func": rex_109_vol_normalized_hl_21d_avg},
    "rex_110_expansion_low_volume_21d": {"inputs": ["close", "high", "low", "volume"], "func": rex_110_expansion_low_volume_21d},
    "rex_111_high_vol_expansion_near_low_21d": {"inputs": ["close", "high", "low", "volume"], "func": rex_111_high_vol_expansion_near_low_21d},
    "rex_112_tr_vol_corr_21d": {"inputs": ["close", "high", "low", "volume"], "func": rex_112_tr_vol_corr_21d},
    "rex_113_tr_vs_max_tr_21d": {"inputs": ["close", "high", "low"], "func": rex_113_tr_vs_max_tr_21d},
    "rex_114_tr_vs_max_tr_63d": {"inputs": ["close", "high", "low"], "func": rex_114_tr_vs_max_tr_63d},
    "rex_115_tr_vs_max_tr_252d": {"inputs": ["close", "high", "low"], "func": rex_115_tr_vs_max_tr_252d},
    "rex_116_max_tr_21d_vs_atr252": {"inputs": ["close", "high", "low"], "func": rex_116_max_tr_21d_vs_atr252},
    "rex_117_max_tr_63d_vs_atr252": {"inputs": ["close", "high", "low"], "func": rex_117_max_tr_63d_vs_atr252},
    "rex_118_max_tr_21d_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rex_118_max_tr_21d_pct_rank_252d},
    "rex_119_tr_spike_flag_3x_atr21": {"inputs": ["close", "high", "low"], "func": rex_119_tr_spike_flag_3x_atr21},
    "rex_120_tr_spike_count_63d": {"inputs": ["close", "high", "low"], "func": rex_120_tr_spike_count_63d},
    "rex_121_tr_spike_count_252d": {"inputs": ["close", "high", "low"], "func": rex_121_tr_spike_count_252d},
    "rex_122_tr_expanding_max_ratio": {"inputs": ["close", "high", "low"], "func": rex_122_tr_expanding_max_ratio},
    "rex_123_atr21_pct_rank_252d": {"inputs": ["close", "high", "low"], "func": rex_123_atr21_pct_rank_252d},
    "rex_124_hl_pct_rank_252d": {"inputs": ["high", "low"], "func": rex_124_hl_pct_rank_252d},
    "rex_125_max_tr_21d_expanding_rank": {"inputs": ["close", "high", "low"], "func": rex_125_max_tr_21d_expanding_rank},
    "rex_126_nr7_flag": {"inputs": ["high", "low"], "func": rex_126_nr7_flag},
    "rex_127_nr4_flag": {"inputs": ["high", "low"], "func": rex_127_nr4_flag},
    "rex_128_wr7_flag": {"inputs": ["high", "low"], "func": rex_128_wr7_flag},
    "rex_129_wr4_flag": {"inputs": ["high", "low"], "func": rex_129_wr4_flag},
    "rex_130_nr7_count_21d": {"inputs": ["high", "low"], "func": rex_130_nr7_count_21d},
    "rex_131_nr7_count_63d": {"inputs": ["high", "low"], "func": rex_131_nr7_count_63d},
    "rex_132_wr7_count_21d": {"inputs": ["high", "low"], "func": rex_132_wr7_count_21d},
    "rex_133_wr7_count_63d": {"inputs": ["high", "low"], "func": rex_133_wr7_count_63d},
    "rex_134_days_since_nr7": {"inputs": ["high", "low"], "func": rex_134_days_since_nr7},
    "rex_135_days_since_wr7": {"inputs": ["high", "low"], "func": rex_135_days_since_wr7},
    "rex_136_nr7_consec_streak": {"inputs": ["high", "low"], "func": rex_136_nr7_consec_streak},
    "rex_137_nr_then_expansion_flag": {"inputs": ["high", "low"], "func": rex_137_nr_then_expansion_flag},
    "rex_138_inside_bar_flag": {"inputs": ["high", "low"], "func": rex_138_inside_bar_flag},
    "rex_139_outside_bar_flag": {"inputs": ["high", "low"], "func": rex_139_outside_bar_flag},
    "rex_140_inside_bar_count_21d": {"inputs": ["high", "low"], "func": rex_140_inside_bar_count_21d},
    "rex_141_inside_bar_count_63d": {"inputs": ["high", "low"], "func": rex_141_inside_bar_count_63d},
    "rex_142_inside_bar_count_252d": {"inputs": ["high", "low"], "func": rex_142_inside_bar_count_252d},
    "rex_143_outside_bar_count_21d": {"inputs": ["high", "low"], "func": rex_143_outside_bar_count_21d},
    "rex_144_outside_bar_count_63d": {"inputs": ["high", "low"], "func": rex_144_outside_bar_count_63d},
    "rex_145_consec_inside_bar_streak": {"inputs": ["high", "low"], "func": rex_145_consec_inside_bar_streak},
    "rex_146_outside_after_inside_flag": {"inputs": ["high", "low"], "func": rex_146_outside_after_inside_flag},
    "rex_147_outside_after_inside_count_63d": {"inputs": ["high", "low"], "func": rex_147_outside_after_inside_count_63d},
    "rex_148_inside_bar_fraction_21d": {"inputs": ["high", "low"], "func": rex_148_inside_bar_fraction_21d},
    "rex_149_days_since_inside_bar": {"inputs": ["high", "low"], "func": rex_149_days_since_inside_bar},
    "rex_150_wr7_after_nr7_expansion_ratio": {"inputs": ["high", "low"], "func": rex_150_wr7_after_nr7_expansion_ratio},
}
