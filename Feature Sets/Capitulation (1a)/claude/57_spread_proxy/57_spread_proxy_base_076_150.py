"""
57_spread_proxy — Base Features 076-150
Domain: HIGH-LOW SPREAD illiquidity estimators — effective bid-ask spread proxies
        from OHLC (Corwin-Schultz, Abdi-Ranaldi, Roll-style, high-low%, gap-based).
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


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _hl_spread_raw(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Simple (high-low)/close spread proxy."""
    return _safe_div(high - low, close)


def _beta_cs(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz beta."""
    log_hl = (_log_safe(high) - _log_safe(low)) ** 2
    return log_hl + log_hl.shift(1)


def _gamma_cs(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz gamma."""
    h2 = pd.concat([high, high.shift(1)], axis=1).max(axis=1)
    l2 = pd.concat([low, low.shift(1)], axis=1).min(axis=1)
    return (_log_safe(h2) - _log_safe(l2)) ** 2


def _cs_spread(high: pd.Series, low: pd.Series) -> pd.Series:
    """Corwin-Schultz spread estimate, floored at 0."""
    k1 = 3.0 - 2.0 * np.sqrt(2.0)
    beta = _beta_cs(high, low)
    gamma = _gamma_cs(high, low)
    alpha = (np.sqrt(2.0 * beta) - np.sqrt(beta)) / k1 - np.sqrt(gamma / k1)
    return (2.0 * (np.exp(alpha) - 1.0) / (1.0 + np.exp(alpha))).clip(lower=0.0)


def _ar_spread(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Abdi-Ranaldi spread: 4*(log(close) - log(midpoint))."""
    mid = 0.5 * (high + low)
    return 4.0 * (_log_safe(close) - _log_safe(mid))


def _roll_cov(close: pd.Series, w: int) -> pd.Series:
    """Rolling covariance of delta_close with lagged delta_close."""
    dc = close.diff(1)
    dc1 = dc.shift(1)
    return dc.rolling(w, min_periods=max(2, w // 2)).cov(dc1)


def _roll_spread(close: pd.Series, w: int) -> pd.Series:
    """Roll effective spread: 2*sqrt(max(-cov,0))."""
    return 2.0 * np.sqrt((-_roll_cov(close, w)).clip(lower=0.0))


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


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
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-087): Composite spread estimators and cross-estimator signals ---

def spr_076_spread_composite_hl_cs_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d mean of composite spread = avg(HL spread, CS spread) — two estimators blended."""
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    cs21 = _rolling_mean(_cs_spread(high, low), _TD_MON)
    return (hl21 + cs21) / 2.0


def spr_077_spread_composite_hl_ar_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d mean of composite spread = avg(HL spread, |AR spread|)."""
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    ar21 = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)
    return (hl21 + ar21) / 2.0


def spr_078_spread_composite_cs_ar_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d mean of composite spread = avg(CS spread, |AR spread|)."""
    cs21 = _rolling_mean(_cs_spread(high, low), _TD_MON)
    ar21 = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)
    return (cs21 + ar21) / 2.0


def spr_079_spread_composite_all3_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d mean composite of HL, CS, and |AR| spread estimators — three-way blend."""
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    cs21 = _rolling_mean(_cs_spread(high, low), _TD_MON)
    ar21 = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)
    return (hl21 + cs21 + ar21) / 3.0


def spr_080_spread_composite_all3_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63d mean composite of HL, CS, and |AR| spread estimators."""
    hl = _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR)
    cs = _rolling_mean(_cs_spread(high, low), _TD_QTR)
    ar = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_QTR)
    return (hl + cs + ar) / 3.0


def spr_081_spread_composite_zscore_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d z-score of the three-way composite spread."""
    comp = spr_079_spread_composite_all3_21d(high, low, close)
    return _safe_div(comp - _rolling_mean(comp, _TD_YEAR), _rolling_std(comp, _TD_YEAR))


def spr_082_spread_composite_pct_rank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252d percentile rank of the three-way composite spread."""
    comp = spr_079_spread_composite_all3_21d(high, low, close)
    return comp.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def spr_083_cs_minus_hl_spread_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Difference: 21d-mean CS spread minus 21d-mean HL spread (estimator divergence)."""
    cs21 = _rolling_mean(_cs_spread(high, low), _TD_MON)
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    return cs21 - hl21


def spr_084_ar_minus_hl_spread_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Difference: 21d-mean |AR| spread minus 21d-mean HL spread."""
    ar21 = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    return ar21 - hl21


def spr_085_spread_dispersion_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Std dev of {HL-spread, CS-spread, |AR|-spread} 21d means (estimator disagreement)."""
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    cs21 = _rolling_mean(_cs_spread(high, low), _TD_MON)
    ar21 = _rolling_mean(_ar_spread(high, low, close).abs(), _TD_MON)
    arr = pd.concat([hl21, cs21, ar21], axis=1)
    return arr.std(axis=1)


def spr_086_roll_spread_vs_hl_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21d Roll spread to 21d HL spread (microstructure vs range)."""
    rs = _rolling_mean(_roll_spread(close, _TD_MON), _TD_MON)
    hl = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    return _safe_div(rs, hl)


def spr_087_roll_spread_vs_cs_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21d Roll spread to 21d CS spread."""
    rs = _rolling_mean(_roll_spread(close, _TD_MON), _TD_MON)
    cs = _rolling_mean(_cs_spread(high, low), _TD_MON)
    return _safe_div(rs, cs)


# --- Group H (088-100): Volume-adjusted spread and turnover-weighted spreads ---

def spr_088_hl_spread_vol_weighted_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Volume-weighted 21d mean HL spread (high-volume days count more)."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(_rolling_sum(hl * volume, _TD_MON), _rolling_sum(volume, _TD_MON))


def spr_089_hl_spread_vol_weighted_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Volume-weighted 63d mean HL spread."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(_rolling_sum(hl * volume, _TD_QTR), _rolling_sum(volume, _TD_QTR))


def spr_090_cs_spread_vol_weighted_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 21d mean CS spread."""
    cs = _cs_spread(high, low)
    return _safe_div(_rolling_sum(cs * volume, _TD_MON), _rolling_sum(volume, _TD_MON))


def spr_091_spread_times_volume_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """21d mean of HL-spread * volume (cost-of-trading proxy per day)."""
    return _rolling_mean(_hl_spread_raw(high, low, close) * volume, _TD_MON)


def spr_092_spread_times_turnover_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """21d mean of HL-spread * dollar-volume (HL * close * volume)."""
    dvol = close * volume
    return _rolling_mean(_hl_spread_raw(high, low, close) * dvol, _TD_MON)


def spr_093_hl_spread_on_high_vol_days_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """21d mean HL spread on days with above-avg volume (stress periods)."""
    hl = _hl_spread_raw(high, low, close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    hl_hv = hl.where(volume > avg_vol, np.nan)
    return hl_hv.rolling(_TD_MON, min_periods=1).mean()


def spr_094_hl_spread_on_low_vol_days_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """21d mean HL spread on days with below-avg volume (illiquid thinning)."""
    hl = _hl_spread_raw(high, low, close)
    avg_vol = _rolling_mean(volume, _TD_MON)
    hl_lv = hl.where(volume <= avg_vol, np.nan)
    return hl_lv.rolling(_TD_MON, min_periods=1).mean()


def spr_095_high_vs_low_vol_spread_ratio_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Ratio of HL spread on high-vol days to low-vol days over 21d."""
    return _safe_div(
        spr_093_hl_spread_on_high_vol_days_21d(high, low, close, volume),
        spr_094_hl_spread_on_low_vol_days_21d(high, low, close, volume),
    )


def spr_096_spread_vol_norm_daily(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """Daily HL spread divided by log(volume) as price-impact normalization."""
    log_vol = np.log(volume.clip(lower=1.0))
    return _safe_div(_hl_spread_raw(high, low, close), log_vol)


def spr_097_spread_vol_norm_21d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """21d mean of HL-spread / log(volume)."""
    return _rolling_mean(spr_096_spread_vol_norm_daily(high, low, close, volume), _TD_MON)


def spr_098_spread_vol_norm_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """63d mean of HL-spread / log(volume)."""
    return _rolling_mean(spr_096_spread_vol_norm_daily(high, low, close, volume), _TD_QTR)


def spr_099_spread_vol_norm_zscore_63d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """63d z-score of HL-spread / log(volume) proxy."""
    sn = spr_096_spread_vol_norm_daily(high, low, close, volume)
    return _safe_div(sn - _rolling_mean(sn, _TD_QTR), _rolling_std(sn, _TD_QTR))


def spr_100_spread_vol_norm_pct_rank_252d(
    high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series
) -> pd.Series:
    """252d percentile rank of HL-spread / log(volume)."""
    sn = spr_096_spread_vol_norm_daily(high, low, close, volume)
    return sn.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group I (101-112): HL spread std, range ratios, true-range comparisons ---

def spr_101_hl_spread_std_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """63-day rolling std of HL spread proxy (spread volatility at quarterly horizon)."""
    return _rolling_std(_hl_spread_raw(high, low, close), _TD_QTR)


def spr_102_hl_spread_std_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """252-day rolling std of HL spread proxy."""
    return _rolling_std(_hl_spread_raw(high, low, close), _TD_YEAR)


def spr_103_hl_spread_coeff_var_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coefficient of variation of HL spread over 21d: std/mean."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(_rolling_std(hl, _TD_MON), _rolling_mean(hl, _TD_MON))


def spr_104_hl_spread_coeff_var_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coefficient of variation of HL spread over 63d."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(_rolling_std(hl, _TD_QTR), _rolling_mean(hl, _TD_QTR))


def spr_105_hl_range_pct_open(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Daily (high-low) as percentage of open price."""
    return _safe_div(high - low, open.replace(0, np.nan))


def spr_106_hl_range_pct_open_21d(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """21d mean of (high-low)/open spread proxy."""
    return _rolling_mean(spr_105_hl_range_pct_open(high, low, open), _TD_MON)


def spr_107_hl_range_pct_open_zscore_63d(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """63d z-score of (high-low)/open spread proxy."""
    hlpo = spr_105_hl_range_pct_open(high, low, open)
    return _safe_div(hlpo - _rolling_mean(hlpo, _TD_QTR), _rolling_std(hlpo, _TD_QTR))


def spr_108_tr_vs_hl_ratio_21d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """21d mean ratio of true range to HL range (gaps inflate TR above HL)."""
    hl = high - low
    tr = pd.concat([hl, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rolling_mean(_safe_div(tr, hl.replace(0, np.nan)), _TD_MON)


def spr_109_tr_vs_hl_ratio_63d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """63d mean ratio of true range to HL range."""
    hl = high - low
    tr = pd.concat([hl, (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
    return _rolling_mean(_safe_div(tr, hl.replace(0, np.nan)), _TD_QTR)


def spr_110_tr_spread_pct_close_21d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """21d mean of true-range / close as TR-based spread proxy."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    return _rolling_mean(_safe_div(tr, close), _TD_MON)


def spr_111_tr_spread_zscore_63d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """63d z-score of TR/close spread proxy."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    tr_spr = _safe_div(tr, close)
    return _safe_div(tr_spr - _rolling_mean(tr_spr, _TD_QTR), _rolling_std(tr_spr, _TD_QTR))


def spr_112_tr_spread_pct_rank_252d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """252d percentile rank of TR/close spread proxy."""
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs(),
    ], axis=1).max(axis=1)
    tr_spr = _safe_div(tr, close)
    return tr_spr.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group J (113-125): EWM spread estimators and adaptive baselines ---

def spr_113_cs_spread_ewm_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM(span=5) of Corwin-Schultz spread (ultra-short smoothing)."""
    return _ewm_mean(_cs_spread(high, low), _TD_WEEK)


def spr_114_cs_spread_ewm_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM(span=63) of Corwin-Schultz spread."""
    return _ewm_mean(_cs_spread(high, low), _TD_QTR)


def spr_115_hl_spread_ewm_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM(span=5) of HL spread proxy (rapid short-term smoothing)."""
    return _ewm_mean(_hl_spread_raw(high, low, close), _TD_WEEK)


def spr_116_hl_spread_ewm_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM(span=63) of HL spread proxy."""
    return _ewm_mean(_hl_spread_raw(high, low, close), _TD_QTR)


def spr_117_hl_spread_ewm_vs_sma_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """EWM(21) minus SMA(21) of HL spread (recent-vs-stable spread divergence)."""
    hl = _hl_spread_raw(high, low, close)
    return _ewm_mean(hl, _TD_MON) - _rolling_mean(hl, _TD_MON)


def spr_118_cs_spread_ewm_vs_sma_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """EWM(63) minus SMA(63) of CS spread."""
    cs = _cs_spread(high, low)
    return _ewm_mean(cs, _TD_QTR) - _rolling_mean(cs, _TD_QTR)


def spr_119_hl_spread_above_ewm21_streak(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Consecutive days HL spread > its EWM(21) (spread sustained above trend)."""
    hl = _hl_spread_raw(high, low, close)
    cond = hl > _ewm_mean(hl, _TD_MON)
    return _consec_streak(cond)


def spr_120_cs_spread_above_ewm21_streak(high: pd.Series, low: pd.Series) -> pd.Series:
    """Consecutive days CS spread > its EWM(21)."""
    cs = _cs_spread(high, low)
    cond = cs > _ewm_mean(cs, _TD_MON)
    return _consec_streak(cond)


def spr_121_hl_spread_acceleration_5d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d diff of 5d-EWM HL spread (short-term spread acceleration)."""
    return _ewm_mean(_hl_spread_raw(high, low, close), _TD_WEEK).diff(_TD_WEEK)


def spr_122_cs_spread_acceleration_5d(high: pd.Series, low: pd.Series) -> pd.Series:
    """5d diff of 5d-EWM CS spread."""
    return _ewm_mean(_cs_spread(high, low), _TD_WEEK).diff(_TD_WEEK)


def spr_123_hl_spread_gt2x_21d_mean_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: daily HL spread > 2x its 21d rolling mean (extreme spread spike)."""
    hl = _hl_spread_raw(high, low, close)
    return (hl > 2.0 * _rolling_mean(hl, _TD_MON)).astype(float)


def spr_124_cs_spread_gt2x_21d_mean_flag(high: pd.Series, low: pd.Series) -> pd.Series:
    """Flag: daily CS spread > 2x its 21d rolling mean."""
    cs = _cs_spread(high, low)
    return (cs > 2.0 * _rolling_mean(cs, _TD_MON)).astype(float)


def spr_125_spread_spike_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of days in 21d window where HL spread > 2x its 21d mean (spike frequency)."""
    hl = _hl_spread_raw(high, low, close)
    spike = (hl > 2.0 * _rolling_mean(hl, _TD_MON)).astype(float)
    return _rolling_sum(spike, _TD_MON)


# --- Group K (126-138): Spread level vs prior periods, multi-horizon comparisons ---

def spr_126_hl_spread_21d_vs_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21d-mean HL spread to 63d-mean HL spread (short vs medium horizon)."""
    return _safe_div(
        _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON),
        _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR),
    )


def spr_127_hl_spread_21d_vs_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 21d-mean HL spread to 252d-mean HL spread (recent vs long-term)."""
    return _safe_div(
        _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON),
        _rolling_mean(_hl_spread_raw(high, low, close), _TD_YEAR),
    )


def spr_128_hl_spread_63d_vs_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 63d-mean HL spread to 252d-mean HL spread."""
    return _safe_div(
        _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR),
        _rolling_mean(_hl_spread_raw(high, low, close), _TD_YEAR),
    )


def spr_129_cs_spread_21d_vs_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21d-mean CS spread to 63d-mean CS spread."""
    return _safe_div(
        _rolling_mean(_cs_spread(high, low), _TD_MON),
        _rolling_mean(_cs_spread(high, low), _TD_QTR),
    )


def spr_130_cs_spread_21d_vs_252d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 21d-mean CS spread to 252d-mean CS spread."""
    return _safe_div(
        _rolling_mean(_cs_spread(high, low), _TD_MON),
        _rolling_mean(_cs_spread(high, low), _TD_YEAR),
    )


def spr_131_roll_spread_21d_vs_252d(close: pd.Series) -> pd.Series:
    """Ratio of 21d Roll spread to 252d Roll spread."""
    return _safe_div(_roll_spread(close, _TD_MON), _roll_spread(close, _TD_YEAR))


def spr_132_hl_spread_half_life_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Ratio of 126d-mean to 252d-mean HL spread (half-year vs full-year spread level)."""
    return _safe_div(
        _rolling_mean(_hl_spread_raw(high, low, close), _TD_HALF),
        _rolling_mean(_hl_spread_raw(high, low, close), _TD_YEAR),
    )


def spr_133_spread_regime_21d_gt_63d_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: 21d-mean HL spread > 63d-mean HL spread (widening regime active)."""
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    hl63 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR)
    return (hl21 > hl63).astype(float)


def spr_134_spread_regime_63d_gt_252d_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: 63d-mean HL spread > 252d-mean HL spread."""
    hl63 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR)
    hl252 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_YEAR)
    return (hl63 > hl252).astype(float)


def spr_135_spread_regime_all_widening_flag(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Flag: 5d > 21d > 63d HL spread means (all horizons in widening alignment)."""
    hl5  = _rolling_mean(_hl_spread_raw(high, low, close), _TD_WEEK)
    hl21 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    hl63 = _rolling_mean(_hl_spread_raw(high, low, close), _TD_QTR)
    return ((hl5 > hl21) & (hl21 > hl63)).astype(float)


def spr_136_hl_spread_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of daily HL spread over trailing 21 days."""
    return _linslope(_hl_spread_raw(high, low, close), _TD_MON)


def spr_137_hl_spread_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """OLS slope of daily HL spread over trailing 63 days."""
    return _linslope(_hl_spread_raw(high, low, close), _TD_QTR)


def spr_138_cs_spread_slope_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """OLS slope of daily CS spread over trailing 21 days."""
    return _linslope(_cs_spread(high, low), _TD_MON)


# --- Group L (139-150): Spread-return interaction and cross-signal features ---

def spr_139_spread_times_neg_ret_21d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """21d mean of HL spread on down-return days only (spread*distress interaction)."""
    hl = _hl_spread_raw(high, low, close)
    ret = close.pct_change(1)
    hl_down = hl.where(ret < 0, 0.0)
    return _rolling_mean(hl_down, _TD_MON)


def spr_140_spread_times_neg_ret_63d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """63d mean of HL spread on down-return days only."""
    hl = _hl_spread_raw(high, low, close)
    ret = close.pct_change(1)
    hl_down = hl.where(ret < 0, 0.0)
    return _rolling_mean(hl_down, _TD_QTR)


def spr_141_spread_down_vs_up_day_ratio_21d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Ratio of avg HL spread on down-days to avg HL spread on up-days, 21d window."""
    hl = _hl_spread_raw(high, low, close)
    ret = close.pct_change(1)
    hl_down = hl.where(ret < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    hl_up   = hl.where(ret > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(hl_down, hl_up)


def spr_142_spread_down_vs_up_day_ratio_63d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """Ratio of avg HL spread on down-days to up-days, 63d window."""
    hl = _hl_spread_raw(high, low, close)
    ret = close.pct_change(1)
    hl_down = hl.where(ret < 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    hl_up   = hl.where(ret > 0, np.nan).rolling(_TD_QTR, min_periods=1).mean()
    return _safe_div(hl_down, hl_up)


def spr_143_spread_corr_with_neg_ret_63d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """63d rolling correlation of HL spread with negative daily return (spread widens on down days)."""
    hl = _hl_spread_raw(high, low, close)
    ret = close.pct_change(1).clip(upper=0.0)
    return hl.rolling(_TD_QTR, min_periods=_TD_MON).corr(ret)


def spr_144_spread_ret_product_21d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """21d mean of (HL spread * |return|) — joint spread-volatility signal."""
    hl = _hl_spread_raw(high, low, close)
    ret_abs = close.pct_change(1).abs()
    return _rolling_mean(hl * ret_abs, _TD_MON)


def spr_145_spread_ret_product_63d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """63d mean of (HL spread * |return|)."""
    hl = _hl_spread_raw(high, low, close)
    ret_abs = close.pct_change(1).abs()
    return _rolling_mean(hl * ret_abs, _TD_QTR)


def spr_146_hl_spread_cross_vol_ratio_21d(
    high: pd.Series, low: pd.Series, close: pd.Series
) -> pd.Series:
    """21d (HL spread mean) / (return std) — spread cost per unit of price vol."""
    hl_m = _rolling_mean(_hl_spread_raw(high, low, close), _TD_MON)
    ret_std = _rolling_std(close.pct_change(1), _TD_MON)
    return _safe_div(hl_m, ret_std)


def spr_147_cs_spread_cross_vol_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """21d CS spread mean divided by 21d return std (CS spread per vol unit)."""
    cs_m = _rolling_mean(_cs_spread(high, low), _TD_MON)
    ret_std = _rolling_std(close.pct_change(1), _TD_MON)
    return _safe_div(cs_m, ret_std)


def spr_148_spread_expanding_pct_of_max(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current HL spread as pct of its expanding historical max (distress proximity)."""
    hl = _hl_spread_raw(high, low, close)
    return _safe_div(hl, hl.expanding(min_periods=1).max())


def spr_149_spread_sum_over_decline_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Sum of HL spread over the last 21 days conditional on price decline (cumulative cost)."""
    hl = _hl_spread_raw(high, low, close)
    ret = close.pct_change(1)
    hl_down = hl.where(ret < 0, 0.0)
    return _rolling_sum(hl_down, _TD_MON)


def spr_150_roll_spread_21d_expanding_pct_rank(close: pd.Series) -> pd.Series:
    """Expanding percentile rank of 21d Roll spread (all-time liquidity deterioration rank)."""
    return _roll_spread(close, _TD_MON).expanding(min_periods=5).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

SPREAD_PROXY_REGISTRY_076_150 = {
    "spr_076_spread_composite_hl_cs_21d": {"inputs": ["high", "low", "close"], "func": spr_076_spread_composite_hl_cs_21d},
    "spr_077_spread_composite_hl_ar_21d": {"inputs": ["high", "low", "close"], "func": spr_077_spread_composite_hl_ar_21d},
    "spr_078_spread_composite_cs_ar_21d": {"inputs": ["high", "low", "close"], "func": spr_078_spread_composite_cs_ar_21d},
    "spr_079_spread_composite_all3_21d": {"inputs": ["high", "low", "close"], "func": spr_079_spread_composite_all3_21d},
    "spr_080_spread_composite_all3_63d": {"inputs": ["high", "low", "close"], "func": spr_080_spread_composite_all3_63d},
    "spr_081_spread_composite_zscore_21d": {"inputs": ["high", "low", "close"], "func": spr_081_spread_composite_zscore_21d},
    "spr_082_spread_composite_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": spr_082_spread_composite_pct_rank_252d},
    "spr_083_cs_minus_hl_spread_21d": {"inputs": ["high", "low", "close"], "func": spr_083_cs_minus_hl_spread_21d},
    "spr_084_ar_minus_hl_spread_21d": {"inputs": ["high", "low", "close"], "func": spr_084_ar_minus_hl_spread_21d},
    "spr_085_spread_dispersion_21d": {"inputs": ["high", "low", "close"], "func": spr_085_spread_dispersion_21d},
    "spr_086_roll_spread_vs_hl_ratio_21d": {"inputs": ["high", "low", "close"], "func": spr_086_roll_spread_vs_hl_ratio_21d},
    "spr_087_roll_spread_vs_cs_ratio_21d": {"inputs": ["high", "low", "close"], "func": spr_087_roll_spread_vs_cs_ratio_21d},
    "spr_088_hl_spread_vol_weighted_21d": {"inputs": ["high", "low", "close", "volume"], "func": spr_088_hl_spread_vol_weighted_21d},
    "spr_089_hl_spread_vol_weighted_63d": {"inputs": ["high", "low", "close", "volume"], "func": spr_089_hl_spread_vol_weighted_63d},
    "spr_090_cs_spread_vol_weighted_21d": {"inputs": ["high", "low", "volume"], "func": spr_090_cs_spread_vol_weighted_21d},
    "spr_091_spread_times_volume_21d": {"inputs": ["high", "low", "close", "volume"], "func": spr_091_spread_times_volume_21d},
    "spr_092_spread_times_turnover_21d": {"inputs": ["high", "low", "close", "volume"], "func": spr_092_spread_times_turnover_21d},
    "spr_093_hl_spread_on_high_vol_days_21d": {"inputs": ["high", "low", "close", "volume"], "func": spr_093_hl_spread_on_high_vol_days_21d},
    "spr_094_hl_spread_on_low_vol_days_21d": {"inputs": ["high", "low", "close", "volume"], "func": spr_094_hl_spread_on_low_vol_days_21d},
    "spr_095_high_vs_low_vol_spread_ratio_21d": {"inputs": ["high", "low", "close", "volume"], "func": spr_095_high_vs_low_vol_spread_ratio_21d},
    "spr_096_spread_vol_norm_daily": {"inputs": ["high", "low", "close", "volume"], "func": spr_096_spread_vol_norm_daily},
    "spr_097_spread_vol_norm_21d": {"inputs": ["high", "low", "close", "volume"], "func": spr_097_spread_vol_norm_21d},
    "spr_098_spread_vol_norm_63d": {"inputs": ["high", "low", "close", "volume"], "func": spr_098_spread_vol_norm_63d},
    "spr_099_spread_vol_norm_zscore_63d": {"inputs": ["high", "low", "close", "volume"], "func": spr_099_spread_vol_norm_zscore_63d},
    "spr_100_spread_vol_norm_pct_rank_252d": {"inputs": ["high", "low", "close", "volume"], "func": spr_100_spread_vol_norm_pct_rank_252d},
    "spr_101_hl_spread_std_63d": {"inputs": ["high", "low", "close"], "func": spr_101_hl_spread_std_63d},
    "spr_102_hl_spread_std_252d": {"inputs": ["high", "low", "close"], "func": spr_102_hl_spread_std_252d},
    "spr_103_hl_spread_coeff_var_21d": {"inputs": ["high", "low", "close"], "func": spr_103_hl_spread_coeff_var_21d},
    "spr_104_hl_spread_coeff_var_63d": {"inputs": ["high", "low", "close"], "func": spr_104_hl_spread_coeff_var_63d},
    "spr_105_hl_range_pct_open": {"inputs": ["high", "low", "open"], "func": spr_105_hl_range_pct_open},
    "spr_106_hl_range_pct_open_21d": {"inputs": ["high", "low", "open"], "func": spr_106_hl_range_pct_open_21d},
    "spr_107_hl_range_pct_open_zscore_63d": {"inputs": ["high", "low", "open"], "func": spr_107_hl_range_pct_open_zscore_63d},
    "spr_108_tr_vs_hl_ratio_21d": {"inputs": ["high", "low", "close"], "func": spr_108_tr_vs_hl_ratio_21d},
    "spr_109_tr_vs_hl_ratio_63d": {"inputs": ["high", "low", "close"], "func": spr_109_tr_vs_hl_ratio_63d},
    "spr_110_tr_spread_pct_close_21d": {"inputs": ["high", "low", "close"], "func": spr_110_tr_spread_pct_close_21d},
    "spr_111_tr_spread_zscore_63d": {"inputs": ["high", "low", "close"], "func": spr_111_tr_spread_zscore_63d},
    "spr_112_tr_spread_pct_rank_252d": {"inputs": ["high", "low", "close"], "func": spr_112_tr_spread_pct_rank_252d},
    "spr_113_cs_spread_ewm_5d": {"inputs": ["high", "low"], "func": spr_113_cs_spread_ewm_5d},
    "spr_114_cs_spread_ewm_63d": {"inputs": ["high", "low"], "func": spr_114_cs_spread_ewm_63d},
    "spr_115_hl_spread_ewm_5d": {"inputs": ["high", "low", "close"], "func": spr_115_hl_spread_ewm_5d},
    "spr_116_hl_spread_ewm_63d": {"inputs": ["high", "low", "close"], "func": spr_116_hl_spread_ewm_63d},
    "spr_117_hl_spread_ewm_vs_sma_21d": {"inputs": ["high", "low", "close"], "func": spr_117_hl_spread_ewm_vs_sma_21d},
    "spr_118_cs_spread_ewm_vs_sma_63d": {"inputs": ["high", "low"], "func": spr_118_cs_spread_ewm_vs_sma_63d},
    "spr_119_hl_spread_above_ewm21_streak": {"inputs": ["high", "low", "close"], "func": spr_119_hl_spread_above_ewm21_streak},
    "spr_120_cs_spread_above_ewm21_streak": {"inputs": ["high", "low"], "func": spr_120_cs_spread_above_ewm21_streak},
    "spr_121_hl_spread_acceleration_5d": {"inputs": ["high", "low", "close"], "func": spr_121_hl_spread_acceleration_5d},
    "spr_122_cs_spread_acceleration_5d": {"inputs": ["high", "low"], "func": spr_122_cs_spread_acceleration_5d},
    "spr_123_hl_spread_gt2x_21d_mean_flag": {"inputs": ["high", "low", "close"], "func": spr_123_hl_spread_gt2x_21d_mean_flag},
    "spr_124_cs_spread_gt2x_21d_mean_flag": {"inputs": ["high", "low"], "func": spr_124_cs_spread_gt2x_21d_mean_flag},
    "spr_125_spread_spike_count_21d": {"inputs": ["high", "low", "close"], "func": spr_125_spread_spike_count_21d},
    "spr_126_hl_spread_21d_vs_63d": {"inputs": ["high", "low", "close"], "func": spr_126_hl_spread_21d_vs_63d},
    "spr_127_hl_spread_21d_vs_252d": {"inputs": ["high", "low", "close"], "func": spr_127_hl_spread_21d_vs_252d},
    "spr_128_hl_spread_63d_vs_252d": {"inputs": ["high", "low", "close"], "func": spr_128_hl_spread_63d_vs_252d},
    "spr_129_cs_spread_21d_vs_63d": {"inputs": ["high", "low"], "func": spr_129_cs_spread_21d_vs_63d},
    "spr_130_cs_spread_21d_vs_252d": {"inputs": ["high", "low"], "func": spr_130_cs_spread_21d_vs_252d},
    "spr_131_roll_spread_21d_vs_252d": {"inputs": ["close"], "func": spr_131_roll_spread_21d_vs_252d},
    "spr_132_hl_spread_half_life_ratio": {"inputs": ["high", "low", "close"], "func": spr_132_hl_spread_half_life_ratio},
    "spr_133_spread_regime_21d_gt_63d_flag": {"inputs": ["high", "low", "close"], "func": spr_133_spread_regime_21d_gt_63d_flag},
    "spr_134_spread_regime_63d_gt_252d_flag": {"inputs": ["high", "low", "close"], "func": spr_134_spread_regime_63d_gt_252d_flag},
    "spr_135_spread_regime_all_widening_flag": {"inputs": ["high", "low", "close"], "func": spr_135_spread_regime_all_widening_flag},
    "spr_136_hl_spread_slope_21d": {"inputs": ["high", "low", "close"], "func": spr_136_hl_spread_slope_21d},
    "spr_137_hl_spread_slope_63d": {"inputs": ["high", "low", "close"], "func": spr_137_hl_spread_slope_63d},
    "spr_138_cs_spread_slope_21d": {"inputs": ["high", "low"], "func": spr_138_cs_spread_slope_21d},
    "spr_139_spread_times_neg_ret_21d": {"inputs": ["high", "low", "close"], "func": spr_139_spread_times_neg_ret_21d},
    "spr_140_spread_times_neg_ret_63d": {"inputs": ["high", "low", "close"], "func": spr_140_spread_times_neg_ret_63d},
    "spr_141_spread_down_vs_up_day_ratio_21d": {"inputs": ["high", "low", "close"], "func": spr_141_spread_down_vs_up_day_ratio_21d},
    "spr_142_spread_down_vs_up_day_ratio_63d": {"inputs": ["high", "low", "close"], "func": spr_142_spread_down_vs_up_day_ratio_63d},
    "spr_143_spread_corr_with_neg_ret_63d": {"inputs": ["high", "low", "close"], "func": spr_143_spread_corr_with_neg_ret_63d},
    "spr_144_spread_ret_product_21d": {"inputs": ["high", "low", "close"], "func": spr_144_spread_ret_product_21d},
    "spr_145_spread_ret_product_63d": {"inputs": ["high", "low", "close"], "func": spr_145_spread_ret_product_63d},
    "spr_146_hl_spread_cross_vol_ratio_21d": {"inputs": ["high", "low", "close"], "func": spr_146_hl_spread_cross_vol_ratio_21d},
    "spr_147_cs_spread_cross_vol_ratio_21d": {"inputs": ["high", "low", "close"], "func": spr_147_cs_spread_cross_vol_ratio_21d},
    "spr_148_spread_expanding_pct_of_max": {"inputs": ["high", "low", "close"], "func": spr_148_spread_expanding_pct_of_max},
    "spr_149_spread_sum_over_decline_21d": {"inputs": ["high", "low", "close"], "func": spr_149_spread_sum_over_decline_21d},
    "spr_150_roll_spread_21d_expanding_pct_rank": {"inputs": ["close"], "func": spr_150_roll_spread_21d_expanding_pct_rank},
}
