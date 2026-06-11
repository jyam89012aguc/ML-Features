"""
35_capitulation_thrust — Base Features 076-150
Domain: sharp final-leg-down thrust signatures — violent terminal acceleration of decline
        Continued: intraday thrust patterns, low-of-leg vs prior ranges, body-to-range ratios,
        thrust persistence scores, cross-horizon thrust comparisons, volume-on-thrust signals,
        tail-return distributions, sigma-burst clusters, low-close ratios, thrust reversals.
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


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _log_ret(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(1)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi   = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return np.nan if den == 0 else num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


def _tr(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """True range."""
    return pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low  - close.shift(1)).abs(),
    ], axis=1).max(axis=1)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Low-of-leg vs prior trading ranges ---

def cth_076_low_vs_21d_range_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Today's low as percentile position within trailing 21-day high-low range (0=at low)."""
    lo21 = _rolling_min(low, _TD_MON)
    hi21 = _rolling_max(low, _TD_MON)
    return _safe_div(low - lo21, hi21 - lo21 + _EPS)


def cth_077_low_vs_63d_range_pct(close: pd.Series, low: pd.Series) -> pd.Series:
    """Today's low as percentile position within trailing 63-day low range."""
    lo63 = _rolling_min(low, _TD_QTR)
    hi63 = _rolling_max(low, _TD_QTR)
    return _safe_div(low - lo63, hi63 - lo63 + _EPS)


def cth_078_close_vs_21d_low_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log-ratio of today's close to 21-day low (proximity to thrust trough)."""
    lo21 = _rolling_min(low, _TD_MON)
    return _log_safe(close) - _log_safe(lo21)


def cth_079_close_vs_63d_low_ratio(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log-ratio of today's close to 63-day low."""
    lo63 = _rolling_min(low, _TD_QTR)
    return _log_safe(close) - _log_safe(lo63)


def cth_080_low_expansion_5d(low: pd.Series) -> pd.Series:
    """Log-ratio of 5-day ago low to today's low (how much the trough expanded in 5d)."""
    return _log_safe(low.shift(_TD_WEEK)) - _log_safe(low)


def cth_081_low_expansion_21d(low: pd.Series) -> pd.Series:
    """Log-ratio of 21-day ago low to today's low (trough expansion over month)."""
    return _log_safe(low.shift(_TD_MON)) - _log_safe(low)


def cth_082_new_low_depth_21d(close: pd.Series, low: pd.Series) -> pd.Series:
    """How far today's low is below the prior 21-day minimum low (new-low depth)."""
    prior_lo = low.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    return (prior_lo - low).clip(lower=0) / close.clip(lower=_EPS)


def cth_083_new_low_depth_63d(close: pd.Series, low: pd.Series) -> pd.Series:
    """How far today's low is below prior 63-day minimum (new-low depth quarterly)."""
    prior_lo = low.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    return (prior_lo - low).clip(lower=0) / close.clip(lower=_EPS)


def cth_084_thrust_below_21d_low_flag(low: pd.Series) -> pd.Series:
    """Flag: today's low breaks the prior 21-day minimum (thrust through support)."""
    prior_lo = low.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    return (low < prior_lo).astype(float)


def cth_085_thrust_below_63d_low_freq_21d(low: pd.Series) -> pd.Series:
    """Frequency of new-63d-low penetrations in trailing 21 days."""
    prior_lo = low.shift(1).rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).min()
    flag = (low < prior_lo).astype(float)
    return _rolling_sum(flag, _TD_MON)


# --- Group I (086-095): Body-to-range ratios (candle anatomy during thrust) ---

def cth_086_body_to_range_ratio_5d(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean |close-open|/(high-low) over trailing 5 days (body fill in thrust)."""
    body  = (close - open).abs()
    rng   = (high - low).clip(lower=_EPS)
    return _rolling_mean(body / rng, _TD_WEEK)


def cth_087_bear_body_fraction_5d(close: pd.Series, open: pd.Series,
                                   high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean bear-candle body/(high-low) over 5 days (only negative-body days)."""
    body  = (open - close).clip(lower=0)
    rng   = (high - low).clip(lower=_EPS)
    return _rolling_mean(body / rng, _TD_WEEK)


def cth_088_bear_body_fraction_21d(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean bear-candle body/(high-low) over 21 days."""
    body  = (open - close).clip(lower=0)
    rng   = (high - low).clip(lower=_EPS)
    return _rolling_mean(body / rng, _TD_MON)


def cth_089_lower_wick_ratio_5d(close: pd.Series, open: pd.Series, low: pd.Series) -> pd.Series:
    """Mean lower-wick / (open-close range) over trailing 5 days."""
    lower_wick = (pd.concat([close, open], axis=1).min(axis=1) - low).clip(lower=0)
    body_rng   = (close - open).abs().clip(lower=_EPS)
    return _rolling_mean(lower_wick / body_rng, _TD_WEEK)


def cth_090_upper_wick_ratio_5d(close: pd.Series, open: pd.Series,
                                  high: pd.Series) -> pd.Series:
    """Mean upper-wick / body over trailing 5 days (failed rally wick in thrust)."""
    upper_wick = (high - pd.concat([close, open], axis=1).max(axis=1)).clip(lower=0)
    body_rng   = (close - open).abs().clip(lower=_EPS)
    return _rolling_mean(upper_wick / body_rng, _TD_WEEK)


def cth_091_close_near_low_flag_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where close is in lowest 20% of day's range in trailing 5 days."""
    pos = _safe_div(close - low, high - low + _EPS)
    flag = (pos < 0.20).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def cth_092_close_near_low_flag_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where close is in lowest 20% of day's range in trailing 21 days."""
    pos  = _safe_div(close - low, high - low + _EPS)
    flag = (pos < 0.20).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_093_open_near_high_bear_5d(close: pd.Series, open: pd.Series,
                                    high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days: open near high AND close near low (strong bear session) in 5d."""
    open_pos  = _safe_div(open  - low, high - low + _EPS)
    close_pos = _safe_div(close - low, high - low + _EPS)
    flag = ((open_pos > 0.70) & (close_pos < 0.30)).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def cth_094_open_near_high_bear_21d(close: pd.Series, open: pd.Series,
                                     high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of strong bear sessions (open near high, close near low) in 21 days."""
    open_pos  = _safe_div(open  - low, high - low + _EPS)
    close_pos = _safe_div(close - low, high - low + _EPS)
    flag = ((open_pos > 0.70) & (close_pos < 0.30)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_095_max_bear_body_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Maximum single-day bear body (open-close) in trailing 5 days."""
    bear_body = (open - close).clip(lower=0)
    return _rolling_max(bear_body, _TD_WEEK)


# --- Group J (096-105): Thrust persistence scores ---

def cth_096_thrust_persist_score_5d(close: pd.Series) -> pd.Series:
    """Fraction of last 5 days with negative 1-day return (persistence of thrust)."""
    lr   = _log_ret(close)
    down = (lr < 0).astype(float)
    return _rolling_mean(down, _TD_WEEK)


def cth_097_thrust_persist_score_10d(close: pd.Series) -> pd.Series:
    """Fraction of last 10 days with negative 1-day return."""
    lr   = _log_ret(close)
    down = (lr < 0).astype(float)
    return down.rolling(10, min_periods=5).mean()


def cth_098_thrust_persist_score_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days with negative 1-day return."""
    lr   = _log_ret(close)
    down = (lr < 0).astype(float)
    return _rolling_mean(down, _TD_MON)


def cth_099_thrust_persist_large_down_5d(close: pd.Series) -> pd.Series:
    """Fraction of last 5 days with return below -1% (large down-day persistence)."""
    lr   = _log_ret(close)
    flag = (lr < -0.01).astype(float)
    return _rolling_mean(flag, _TD_WEEK)


def cth_100_thrust_persist_large_down_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days with return below -1%."""
    lr   = _log_ret(close)
    flag = (lr < -0.01).astype(float)
    return _rolling_mean(flag, _TD_MON)


def cth_101_thrust_persist_xlarge_down_5d(close: pd.Series) -> pd.Series:
    """Fraction of last 5 days with return below -2% (extra-large down persistence)."""
    lr   = _log_ret(close)
    flag = (lr < -0.02).astype(float)
    return _rolling_mean(flag, _TD_WEEK)


def cth_102_thrust_persist_xlarge_down_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21 days with return below -2%."""
    lr   = _log_ret(close)
    flag = (lr < -0.02).astype(float)
    return _rolling_mean(flag, _TD_MON)


def cth_103_thrust_ema_vs_sma_5d(close: pd.Series) -> pd.Series:
    """EMA5 minus SMA5 of daily returns (EMA weights recent days more in thrust)."""
    lr  = _log_ret(close)
    ema = _ewm_mean(lr, _TD_WEEK)
    sma = _rolling_mean(lr, _TD_WEEK)
    return ema - sma


def cth_104_thrust_persist_composite(close: pd.Series) -> pd.Series:
    """Composite persistence: fraction-down-5d * fraction-down-21d (dual-window)."""
    lr    = _log_ret(close)
    down  = (lr < 0).astype(float)
    p5    = _rolling_mean(down, _TD_WEEK)
    p21   = _rolling_mean(down, _TD_MON)
    return p5 * p21


def cth_105_thrust_cumulative_z_5d(close: pd.Series) -> pd.Series:
    """Sum of daily z-scores over trailing 5 days (cumulative sigma thrust)."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    return _rolling_sum(z, _TD_WEEK)


# --- Group K (106-115): Cross-horizon thrust comparisons ---

def cth_106_thrust_5d_vs_21d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of absolute 5d return to absolute 21d return (recency concentration)."""
    c5  = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))).abs()
    c21 = (_log_safe(close) - _log_safe(close.shift(_TD_MON))).abs()
    return _safe_div(c5, c21 + _EPS)


def cth_107_thrust_5d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of absolute 5d return to absolute 63d return."""
    c5  = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))).abs()
    c63 = (_log_safe(close) - _log_safe(close.shift(_TD_QTR))).abs()
    return _safe_div(c5, c63 + _EPS)


def cth_108_thrust_21d_vs_63d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of absolute 21d return to absolute 63d return."""
    c21 = (_log_safe(close) - _log_safe(close.shift(_TD_MON))).abs()
    c63 = (_log_safe(close) - _log_safe(close.shift(_TD_QTR))).abs()
    return _safe_div(c21, c63 + _EPS)


def cth_109_thrust_21d_vs_126d_ratio(close: pd.Series) -> pd.Series:
    """Ratio of absolute 21d return to absolute 126d return."""
    c21  = (_log_safe(close) - _log_safe(close.shift(_TD_MON))).abs()
    c126 = (_log_safe(close) - _log_safe(close.shift(_TD_HALF))).abs()
    return _safe_div(c21, c126 + _EPS)


def cth_110_final_vs_earlier_leg_21_63(close: pd.Series) -> pd.Series:
    """Last-21d loss vs prior-21d-to-63d loss (final leg steeper than prior leg)."""
    leg_final = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    leg_prior  = _log_safe(close.shift(_TD_MON)) - _log_safe(close.shift(_TD_QTR))
    return _safe_div(leg_final, leg_prior.abs() + _EPS)


def cth_111_final_vs_earlier_leg_5_21(close: pd.Series) -> pd.Series:
    """Last-5d loss vs prior 5d-to-21d loss ratio."""
    leg_final = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    leg_prior  = _log_safe(close.shift(_TD_WEEK)) - _log_safe(close.shift(_TD_MON))
    return _safe_div(leg_final, leg_prior.abs() + _EPS)


def cth_112_return_diff_5d_21d(close: pd.Series) -> pd.Series:
    """Difference: 5d cumulative return minus 21d cumulative return (final-leg excess)."""
    c5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    c21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return c5 - c21


def cth_113_horizon_thrust_rank_5d(close: pd.Series) -> pd.Series:
    """Rank (pct) of current 5d return among 5d returns in trailing 252 days."""
    c5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    return c5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cth_114_horizon_thrust_rank_21d(close: pd.Series) -> pd.Series:
    """Rank (pct) of current 21d return among 21d returns in trailing 252 days."""
    c21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    return c21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cth_115_horizon_thrust_rank_63d(close: pd.Series) -> pd.Series:
    """Rank (pct) of current 63d return among 63d returns in trailing 252 days."""
    c63 = _log_safe(close) - _log_safe(close.shift(_TD_QTR))
    return c63.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group L (116-125): Volume-on-thrust signals ---

def cth_116_vol_on_down_days_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on down-days in trailing 5 days (selling pressure intensity)."""
    lr      = _log_ret(close)
    down_v  = volume.where(lr < 0, np.nan)
    return down_v.rolling(_TD_WEEK, min_periods=1).mean()


def cth_117_vol_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume on down-days in trailing 21 days."""
    lr     = _log_ret(close)
    down_v = volume.where(lr < 0, np.nan)
    return down_v.rolling(_TD_MON, min_periods=1).mean()


def cth_118_vol_down_vs_up_ratio_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean volume on down-days vs up-days in trailing 5 days."""
    lr     = _log_ret(close)
    down_v = volume.where(lr < 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    up_v   = volume.where(lr > 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()
    return _safe_div(down_v, up_v)


def cth_119_vol_down_vs_up_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Ratio of mean volume on down-days vs up-days in trailing 21 days."""
    lr     = _log_ret(close)
    down_v = volume.where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    up_v   = volume.where(lr > 0, np.nan).rolling(_TD_MON, min_periods=1).mean()
    return _safe_div(down_v, up_v)


def cth_120_vol_thrust_score_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of negative returns in trailing 5 days (thrust energy)."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    return _rolling_sum(lr * vol_n, _TD_WEEK)


def cth_121_vol_thrust_score_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted sum of negative returns in trailing 21 days."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    return _rolling_sum(lr * vol_n, _TD_MON)


def cth_122_vol_surge_on_worst_day_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume on the worst single-day return day in trailing 21 days (panic volume)."""
    lr = _log_ret(close)
    def _vol_worst(idx_slice):
        if len(idx_slice) == 0:
            return np.nan
        return float(idx_slice[int(np.argmin(idx_slice))])
    _ = lr  # used below via window position
    combined = pd.concat([lr, volume], axis=1)
    combined.columns = ["lr", "vol"]
    def _worst_vol(arr_lr, arr_vol):
        if len(arr_lr) == 0:
            return np.nan
        idx = int(np.argmin(arr_lr))
        return arr_vol[idx]
    # Use apply on two-column rolling
    result = pd.Series(np.nan, index=close.index)
    lr_arr  = lr.values
    vol_arr = volume.values
    for i in range(len(close)):
        start = max(0, i - _TD_MON + 1)
        window_lr  = lr_arr[start:i+1]
        window_vol = vol_arr[start:i+1]
        if len(window_lr) == 0 or np.all(np.isnan(window_lr)):
            result.iloc[i] = np.nan
        else:
            valid = ~np.isnan(window_lr)
            if valid.sum() == 0:
                result.iloc[i] = np.nan
            else:
                idx = int(np.nanargmin(window_lr))
                result.iloc[i] = window_vol[idx]
    return result


def cth_123_vol_norm_on_thrust_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume-normalized-by-252d-avg on down-days in trailing 5 days."""
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    lr      = _log_ret(close)
    return vol_n.where(lr < 0, np.nan).rolling(_TD_WEEK, min_periods=1).mean()


def cth_124_vol_norm_on_thrust_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean normalized volume on down-days in trailing 21 days."""
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    lr      = _log_ret(close)
    return vol_n.where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()


def cth_125_vol_and_return_corr_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 21-day correlation between daily return and volume (negative = panic)."""
    lr = _log_ret(close)
    return lr.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).corr(volume)


# --- Group M (126-135): Tail-return distributions and sigma-burst clusters ---

def cth_126_return_skew_21d(close: pd.Series) -> pd.Series:
    """21-day rolling skewness of daily returns (negative = left-tail thrust)."""
    lr = _log_ret(close)
    return lr.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).skew()


def cth_127_return_skew_63d(close: pd.Series) -> pd.Series:
    """63-day rolling skewness of daily returns."""
    lr = _log_ret(close)
    return lr.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).skew()


def cth_128_return_kurtosis_63d(close: pd.Series) -> pd.Series:
    """63-day rolling excess kurtosis of daily returns (fat-tail / burst magnitude)."""
    lr = _log_ret(close)
    return lr.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).kurt()


def cth_129_left_tail_mean_21d(close: pd.Series) -> pd.Series:
    """Mean return on days in the bottom 10th percentile of the 21-day return distribution."""
    lr = _log_ret(close)
    p10 = lr.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).quantile(0.10)
    return lr.where(lr <= p10, np.nan).rolling(_TD_MON, min_periods=1).mean()


def cth_130_left_tail_mean_63d(close: pd.Series) -> pd.Series:
    """Mean return on days in the bottom 10th percentile of the 63-day distribution."""
    lr  = _log_ret(close)
    p10 = lr.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).quantile(0.10)
    return lr.where(lr <= p10, np.nan).rolling(_TD_QTR, min_periods=1).mean()


def cth_131_sigma_burst_cluster_5d(close: pd.Series) -> pd.Series:
    """Count of days exceeding -1.5 sigma in trailing 5 days (cluster of shocks)."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    flag = (z < -1.5).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def cth_132_sigma_burst_cluster_21d(close: pd.Series) -> pd.Series:
    """Count of days exceeding -2 sigma in trailing 21 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    flag = (z < -2.0).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_133_sigma_burst_cluster_63d(close: pd.Series) -> pd.Series:
    """Count of days exceeding -2 sigma in trailing 63 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    flag = (z < -2.0).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def cth_134_max_consecutive_sigma_hits_21d(close: pd.Series) -> pd.Series:
    """Max consecutive days below -1 sigma within trailing 21 days."""
    lr = _log_ret(close)
    mn = _rolling_mean(lr, _TD_YEAR)
    sd = _rolling_std(lr, _TD_YEAR)
    z  = _safe_div(lr - mn, sd)
    cond = z < -1.0
    def _max_run(arr):
        mx = cur = 0
        for v in arr:
            if v:
                cur += 1
                if cur > mx:
                    mx = cur
            else:
                cur = 0
        return float(mx)
    return cond.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).apply(_max_run, raw=True)


def cth_135_vol_of_vol_5d(close: pd.Series) -> pd.Series:
    """5-day std of 1-day absolute returns (vol-of-vol in thrust window)."""
    lr = _log_ret(close).abs()
    return _rolling_std(lr, _TD_WEEK)


# --- Group N (136-145): Low-close ratios and close-to-low strength ---

def cth_136_close_to_low_5d_avg(close: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (close - low) / close over trailing 5 days (tail below close = panic)."""
    ratio = (close - low) / close.clip(lower=_EPS)
    return _rolling_mean(ratio, _TD_WEEK)


def cth_137_close_to_low_21d_avg(close: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (close - low) / close over trailing 21 days."""
    ratio = (close - low) / close.clip(lower=_EPS)
    return _rolling_mean(ratio, _TD_MON)


def cth_138_low_vs_open_5d_avg(low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean (open - low) / open over trailing 5 days (intraday collapse from open)."""
    ratio = (open - low).clip(lower=0) / open.clip(lower=_EPS)
    return _rolling_mean(ratio, _TD_WEEK)


def cth_139_low_vs_open_21d_avg(low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean (open - low) / open over trailing 21 days."""
    ratio = (open - low).clip(lower=0) / open.clip(lower=_EPS)
    return _rolling_mean(ratio, _TD_MON)


def cth_140_high_to_close_bear_5d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean (high - close) / high over trailing 5 days (how far close fell from high)."""
    ratio = (high - close).clip(lower=0) / high.clip(lower=_EPS)
    return _rolling_mean(ratio, _TD_WEEK)


def cth_141_high_to_close_bear_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean (high - close) / high over trailing 21 days."""
    ratio = (high - close).clip(lower=0) / high.clip(lower=_EPS)
    return _rolling_mean(ratio, _TD_MON)


def cth_142_close_below_midpoint_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 5 days where close < midpoint of day's range."""
    mid  = (high + low) / 2.0
    flag = (close < mid).astype(float)
    return _rolling_mean(flag, _TD_WEEK)


def cth_143_close_below_midpoint_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Fraction of last 21 days where close < midpoint of day's range."""
    mid  = (high + low) / 2.0
    flag = (close < mid).astype(float)
    return _rolling_mean(flag, _TD_MON)


def cth_144_open_to_low_vs_range_5d(high: pd.Series, low: pd.Series, open: pd.Series) -> pd.Series:
    """Mean (open-low) / (high-low) over 5 days (how early in range the low formed)."""
    ratio = _safe_div(open - low, high - low + _EPS)
    return _rolling_mean(ratio, _TD_WEEK)


def cth_145_tail_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio of 5th-percentile return to 95th-percentile return in 21d (tail asymmetry)."""
    lr  = _log_ret(close)
    p5  = lr.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).quantile(0.05)
    p95 = lr.rolling(_TD_MON, min_periods=max(5, _TD_MON // 2)).quantile(0.95)
    return _safe_div(p5.abs(), p95.abs() + _EPS)


# --- Group O (146-150): Thrust reversal and exhaustion signals ---

def cth_146_intraday_reversal_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days with large intraday range but close near session high (reversal wick) in 5d."""
    rng  = (high - low).clip(lower=_EPS)
    pos  = _safe_div(close - low, rng)
    flag = (pos > 0.80).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def cth_147_intraday_reversal_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of close-near-high reversal days in trailing 21 days."""
    rng  = (high - low).clip(lower=_EPS)
    pos  = _safe_div(close - low, rng)
    flag = (pos > 0.80).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_148_gap_fill_down_ratio_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of gap-down days where intraday action further extended the gap (no fill)."""
    gap_down   = (open < close.shift(1))
    no_fill    = (close < open)
    both       = (gap_down & no_fill).astype(float)
    gap_count  = gap_down.astype(float)
    s_both     = _rolling_sum(both, _TD_MON)
    s_gaps     = _rolling_sum(gap_count, _TD_MON)
    return _safe_div(s_both, s_gaps)


def cth_149_thrust_exhaustion_high_vol_small_ret(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: high volume (>1.5x avg) but small absolute return (<0.3%) — exhaustion candle."""
    avg_vol  = _rolling_mean(volume, _TD_MON)
    high_vol = (volume > 1.5 * avg_vol).astype(float)
    lr       = _log_ret(close).abs()
    small_ret = (lr < 0.003).astype(float)
    return _rolling_sum(high_vol * small_ret, _TD_MON)


def cth_150_thrust_score_final_composite(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Final composite: z(5d ret) * z(vol/avg) * persistence21d (all three thrust axes)."""
    cum5    = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    z5      = _safe_div(cum5 - _rolling_mean(cum5, _TD_YEAR), _rolling_std(cum5, _TD_YEAR))
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_r   = _safe_div(volume, avg_vol)
    zvol    = _safe_div(vol_r - _rolling_mean(vol_r, _TD_YEAR), _rolling_std(vol_r, _TD_YEAR))
    lr      = _log_ret(close)
    pers    = _rolling_sum((lr < 0).astype(float), _TD_MON) / _TD_MON
    return z5 * zvol * pers


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITULATION_THRUST_REGISTRY_076_150 = {
    "cth_076_low_vs_21d_range_pct": {"inputs": ["close", "low"], "func": cth_076_low_vs_21d_range_pct},
    "cth_077_low_vs_63d_range_pct": {"inputs": ["close", "low"], "func": cth_077_low_vs_63d_range_pct},
    "cth_078_close_vs_21d_low_ratio": {"inputs": ["close", "low"], "func": cth_078_close_vs_21d_low_ratio},
    "cth_079_close_vs_63d_low_ratio": {"inputs": ["close", "low"], "func": cth_079_close_vs_63d_low_ratio},
    "cth_080_low_expansion_5d": {"inputs": ["low"], "func": cth_080_low_expansion_5d},
    "cth_081_low_expansion_21d": {"inputs": ["low"], "func": cth_081_low_expansion_21d},
    "cth_082_new_low_depth_21d": {"inputs": ["close", "low"], "func": cth_082_new_low_depth_21d},
    "cth_083_new_low_depth_63d": {"inputs": ["close", "low"], "func": cth_083_new_low_depth_63d},
    "cth_084_thrust_below_21d_low_flag": {"inputs": ["low"], "func": cth_084_thrust_below_21d_low_flag},
    "cth_085_thrust_below_63d_low_freq_21d": {"inputs": ["low"], "func": cth_085_thrust_below_63d_low_freq_21d},
    "cth_086_body_to_range_ratio_5d": {"inputs": ["close", "open", "high", "low"], "func": cth_086_body_to_range_ratio_5d},
    "cth_087_bear_body_fraction_5d": {"inputs": ["close", "open", "high", "low"], "func": cth_087_bear_body_fraction_5d},
    "cth_088_bear_body_fraction_21d": {"inputs": ["close", "open", "high", "low"], "func": cth_088_bear_body_fraction_21d},
    "cth_089_lower_wick_ratio_5d": {"inputs": ["close", "open", "low"], "func": cth_089_lower_wick_ratio_5d},
    "cth_090_upper_wick_ratio_5d": {"inputs": ["close", "open", "high"], "func": cth_090_upper_wick_ratio_5d},
    "cth_091_close_near_low_flag_5d": {"inputs": ["close", "high", "low"], "func": cth_091_close_near_low_flag_5d},
    "cth_092_close_near_low_flag_21d": {"inputs": ["close", "high", "low"], "func": cth_092_close_near_low_flag_21d},
    "cth_093_open_near_high_bear_5d": {"inputs": ["close", "open", "high", "low"], "func": cth_093_open_near_high_bear_5d},
    "cth_094_open_near_high_bear_21d": {"inputs": ["close", "open", "high", "low"], "func": cth_094_open_near_high_bear_21d},
    "cth_095_max_bear_body_5d": {"inputs": ["close", "open"], "func": cth_095_max_bear_body_5d},
    "cth_096_thrust_persist_score_5d": {"inputs": ["close"], "func": cth_096_thrust_persist_score_5d},
    "cth_097_thrust_persist_score_10d": {"inputs": ["close"], "func": cth_097_thrust_persist_score_10d},
    "cth_098_thrust_persist_score_21d": {"inputs": ["close"], "func": cth_098_thrust_persist_score_21d},
    "cth_099_thrust_persist_large_down_5d": {"inputs": ["close"], "func": cth_099_thrust_persist_large_down_5d},
    "cth_100_thrust_persist_large_down_21d": {"inputs": ["close"], "func": cth_100_thrust_persist_large_down_21d},
    "cth_101_thrust_persist_xlarge_down_5d": {"inputs": ["close"], "func": cth_101_thrust_persist_xlarge_down_5d},
    "cth_102_thrust_persist_xlarge_down_21d": {"inputs": ["close"], "func": cth_102_thrust_persist_xlarge_down_21d},
    "cth_103_thrust_ema_vs_sma_5d": {"inputs": ["close"], "func": cth_103_thrust_ema_vs_sma_5d},
    "cth_104_thrust_persist_composite": {"inputs": ["close"], "func": cth_104_thrust_persist_composite},
    "cth_105_thrust_cumulative_z_5d": {"inputs": ["close"], "func": cth_105_thrust_cumulative_z_5d},
    "cth_106_thrust_5d_vs_21d_ratio": {"inputs": ["close"], "func": cth_106_thrust_5d_vs_21d_ratio},
    "cth_107_thrust_5d_vs_63d_ratio": {"inputs": ["close"], "func": cth_107_thrust_5d_vs_63d_ratio},
    "cth_108_thrust_21d_vs_63d_ratio": {"inputs": ["close"], "func": cth_108_thrust_21d_vs_63d_ratio},
    "cth_109_thrust_21d_vs_126d_ratio": {"inputs": ["close"], "func": cth_109_thrust_21d_vs_126d_ratio},
    "cth_110_final_vs_earlier_leg_21_63": {"inputs": ["close"], "func": cth_110_final_vs_earlier_leg_21_63},
    "cth_111_final_vs_earlier_leg_5_21": {"inputs": ["close"], "func": cth_111_final_vs_earlier_leg_5_21},
    "cth_112_return_diff_5d_21d": {"inputs": ["close"], "func": cth_112_return_diff_5d_21d},
    "cth_113_horizon_thrust_rank_5d": {"inputs": ["close"], "func": cth_113_horizon_thrust_rank_5d},
    "cth_114_horizon_thrust_rank_21d": {"inputs": ["close"], "func": cth_114_horizon_thrust_rank_21d},
    "cth_115_horizon_thrust_rank_63d": {"inputs": ["close"], "func": cth_115_horizon_thrust_rank_63d},
    "cth_116_vol_on_down_days_5d": {"inputs": ["close", "volume"], "func": cth_116_vol_on_down_days_5d},
    "cth_117_vol_on_down_days_21d": {"inputs": ["close", "volume"], "func": cth_117_vol_on_down_days_21d},
    "cth_118_vol_down_vs_up_ratio_5d": {"inputs": ["close", "volume"], "func": cth_118_vol_down_vs_up_ratio_5d},
    "cth_119_vol_down_vs_up_ratio_21d": {"inputs": ["close", "volume"], "func": cth_119_vol_down_vs_up_ratio_21d},
    "cth_120_vol_thrust_score_5d": {"inputs": ["close", "volume"], "func": cth_120_vol_thrust_score_5d},
    "cth_121_vol_thrust_score_21d": {"inputs": ["close", "volume"], "func": cth_121_vol_thrust_score_21d},
    "cth_122_vol_surge_on_worst_day_21d": {"inputs": ["close", "volume"], "func": cth_122_vol_surge_on_worst_day_21d},
    "cth_123_vol_norm_on_thrust_5d": {"inputs": ["close", "volume"], "func": cth_123_vol_norm_on_thrust_5d},
    "cth_124_vol_norm_on_thrust_21d": {"inputs": ["close", "volume"], "func": cth_124_vol_norm_on_thrust_21d},
    "cth_125_vol_and_return_corr_21d": {"inputs": ["close", "volume"], "func": cth_125_vol_and_return_corr_21d},
    "cth_126_return_skew_21d": {"inputs": ["close"], "func": cth_126_return_skew_21d},
    "cth_127_return_skew_63d": {"inputs": ["close"], "func": cth_127_return_skew_63d},
    "cth_128_return_kurtosis_63d": {"inputs": ["close"], "func": cth_128_return_kurtosis_63d},
    "cth_129_left_tail_mean_21d": {"inputs": ["close"], "func": cth_129_left_tail_mean_21d},
    "cth_130_left_tail_mean_63d": {"inputs": ["close"], "func": cth_130_left_tail_mean_63d},
    "cth_131_sigma_burst_cluster_5d": {"inputs": ["close"], "func": cth_131_sigma_burst_cluster_5d},
    "cth_132_sigma_burst_cluster_21d": {"inputs": ["close"], "func": cth_132_sigma_burst_cluster_21d},
    "cth_133_sigma_burst_cluster_63d": {"inputs": ["close"], "func": cth_133_sigma_burst_cluster_63d},
    "cth_134_max_consecutive_sigma_hits_21d": {"inputs": ["close"], "func": cth_134_max_consecutive_sigma_hits_21d},
    "cth_135_vol_of_vol_5d": {"inputs": ["close"], "func": cth_135_vol_of_vol_5d},
    "cth_136_close_to_low_5d_avg": {"inputs": ["close", "low"], "func": cth_136_close_to_low_5d_avg},
    "cth_137_close_to_low_21d_avg": {"inputs": ["close", "low"], "func": cth_137_close_to_low_21d_avg},
    "cth_138_low_vs_open_5d_avg": {"inputs": ["low", "open"], "func": cth_138_low_vs_open_5d_avg},
    "cth_139_low_vs_open_21d_avg": {"inputs": ["low", "open"], "func": cth_139_low_vs_open_21d_avg},
    "cth_140_high_to_close_bear_5d": {"inputs": ["close", "high"], "func": cth_140_high_to_close_bear_5d},
    "cth_141_high_to_close_bear_21d": {"inputs": ["close", "high"], "func": cth_141_high_to_close_bear_21d},
    "cth_142_close_below_midpoint_5d": {"inputs": ["close", "high", "low"], "func": cth_142_close_below_midpoint_5d},
    "cth_143_close_below_midpoint_21d": {"inputs": ["close", "high", "low"], "func": cth_143_close_below_midpoint_21d},
    "cth_144_open_to_low_vs_range_5d": {"inputs": ["high", "low", "open"], "func": cth_144_open_to_low_vs_range_5d},
    "cth_145_tail_ratio_21d": {"inputs": ["close"], "func": cth_145_tail_ratio_21d},
    "cth_146_intraday_reversal_5d": {"inputs": ["close", "high", "low"], "func": cth_146_intraday_reversal_5d},
    "cth_147_intraday_reversal_21d": {"inputs": ["close", "high", "low"], "func": cth_147_intraday_reversal_21d},
    "cth_148_gap_fill_down_ratio_21d": {"inputs": ["close", "open"], "func": cth_148_gap_fill_down_ratio_21d},
    "cth_149_thrust_exhaustion_high_vol_small_ret": {"inputs": ["close", "volume"], "func": cth_149_thrust_exhaustion_high_vol_small_ret},
    "cth_150_thrust_score_final_composite": {"inputs": ["close", "volume"], "func": cth_150_thrust_score_final_composite},
}
