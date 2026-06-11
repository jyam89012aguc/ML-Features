"""
46_gap_structure — 3rd Derivatives (Features drv3_001-025)
Domain: rate of change of 2nd-derivative gap-structure features — acceleration of velocity
Asset class: US equities | Daily OHLCV (price/volume ONLY — SEP folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
Includes acceleration of gap-type classification velocity features (exhaustion, breakaway).
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
    return num / den.replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_count_true(cond: pd.Series, w: int) -> pd.Series:
    return cond.astype(float).rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _gap_pct(close: pd.Series, open_: pd.Series) -> pd.Series:
    prior_close = close.shift(1)
    return _safe_div(open_ - prior_close, prior_close.abs().clip(lower=_EPS))


def _gap_down(close: pd.Series, open_: pd.Series) -> pd.Series:
    return _gap_pct(close, open_).clip(upper=0).abs()


def _gap_up(close: pd.Series, open_: pd.Series) -> pd.Series:
    return _gap_pct(close, open_).clip(lower=0)


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


# ── Gap-type classification helpers (self-contained) ─────────────────────────

def _trend_direction(close: pd.Series, w: int = _TD_MON) -> pd.Series:
    slope = close.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda x: float(np.polyfit(np.arange(len(x)), x, 1)[0]) if len(x) >= 2 else 0.0,
        raw=True
    )
    return np.sign(slope)


def _trailing_range_position(close: pd.Series, high: pd.Series, low: pd.Series,
                              open_: pd.Series, w: int = _TD_MON) -> pd.Series:
    prior_high = high.shift(1).rolling(w, min_periods=max(1, w // 2)).max()
    prior_low = low.shift(1).rolling(w, min_periods=max(1, w // 2)).min()
    rng = (prior_high - prior_low).clip(lower=_EPS)
    return _safe_div(open_ - prior_low, rng).clip(0.0, 1.0)


def _vol_ratio(volume: pd.Series, w: int = _TD_MON) -> pd.Series:
    avg = volume.shift(1).rolling(w, min_periods=max(1, w // 2)).mean().clip(lower=_EPS)
    return _safe_div(volume, avg)


def _trend_maturity(close: pd.Series, w: int = _TD_QTR) -> pd.Series:
    rolling_mean_w = close.rolling(w, min_periods=max(1, w // 2)).mean()
    above = (close > rolling_mean_w).astype(float)
    return above.rolling(w, min_periods=max(1, w // 2)).mean()


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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

# --- drv3_001-010: Acceleration of core gap metrics ---

def gap_drv3_001_avg_gap_abs_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day avg abs gap (acceleration of gap-size velocity)."""
    avg = _rolling_mean(_gap_pct(close, open).abs(), _TD_MON)
    vel = avg.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_002_avg_gap_abs_21d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day-velocity of 21-day avg abs gap."""
    avg = _rolling_mean(_gap_pct(close, open).abs(), _TD_MON)
    vel21 = avg.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_003_gap_down_freq_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down-gap frequency (jerk in frequency)."""
    freq = _rolling_count_true(_gap_pct(close, open) < 0, _TD_MON) / _TD_MON
    vel = freq.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_004_gap_std_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day gap std (gap volatility jerk)."""
    s = _rolling_std(_gap_pct(close, open), _TD_MON)
    vel = s.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_005_gap_down_sum_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day cumulative down-gap return."""
    dg_sum = _rolling_sum(_gap_down(close, open), _TD_MON)
    vel = dg_sum.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_006_gap_down_freq_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day down-gap frequency."""
    freq = _rolling_count_true(_gap_pct(close, open) < 0, _TD_QTR) / _TD_QTR
    vel21 = freq.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_007_gap_std_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day gap std."""
    s = _rolling_std(_gap_pct(close, open), _TD_QTR)
    vel21 = s.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_008_gap_abs_zscore_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 252-day abs-gap z-score (acceleration of extremity)."""
    ag = _gap_pct(close, open).abs()
    m = _rolling_mean(ag, _TD_YEAR)
    s = _rolling_std(ag, _TD_YEAR)
    z = _safe_div(ag - m, s)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_009_gap_net_bias_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day net overnight gap bias."""
    bias = _rolling_sum(_gap_up(close, open), _TD_QTR) - _rolling_sum(_gap_down(close, open), _TD_QTR)
    vel21 = bias.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_010_gap_vol_ratio_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21d/252d gap vol ratio (regime acceleration)."""
    ag = _gap_pct(close, open).abs()
    ratio = _safe_div(_rolling_std(ag, _TD_MON), _rolling_std(ag, _TD_YEAR).clip(lower=_EPS))
    vel = ratio.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


# --- drv3_011-025: Acceleration of gap-type classification metrics ─────────────

def gap_drv3_011_exhaustion_gap_down_count_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                                   high: pd.Series, low: pd.Series,
                                                                   volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day down-exhaustion count (capitulation acceleration)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    cnt = _rolling_sum(flag, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_012_breakaway_gap_down_count_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                                  high: pd.Series, low: pd.Series,
                                                                  volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day down-breakaway count."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    cnt = _rolling_sum(flag, _TD_QTR)
    vel21 = cnt.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_013_exhaustion_gap_down_ewm_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                           high: pd.Series, low: pd.Series,
                                                           volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-span EWM of down-exhaustion gap flag (jerk in capitulation pulse)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ewm = _ewm_mean(flag, _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_014_breakaway_gap_down_ewm_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                          high: pd.Series, low: pd.Series,
                                                          volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-span EWM of down-breakaway gap flag."""
    flag = _breakaway_gap_down_flag(close, open, high, low, volume)
    ewm = _ewm_mean(flag, _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_015_gap_type_distress_score_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                               high: pd.Series, low: pd.Series,
                                                               volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day gap-type distress score (jerk in capitulation distress)."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    score = _rolling_sum(2.0 * ex_dn + 1.0 * ba_dn, _TD_MON)
    vel = score.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_016_exhaustion_gap_down_count_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                                  high: pd.Series, low: pd.Series,
                                                                  volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day down-exhaustion count (short-horizon jerk)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    cnt21 = _rolling_sum(flag, _TD_MON)
    vel = cnt21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_017_exhaustion_gap_all_count_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                                high: pd.Series, low: pd.Series,
                                                                volume: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-day all-direction exhaustion gap count."""
    flag = _exhaustion_gap_flag(close, open, high, low, volume)
    cnt21 = _rolling_sum(flag, _TD_MON)
    vel = cnt21.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_018_exhaustion_vs_breakaway_ratio_21d_diff_5d_diff(close: pd.Series, open: pd.Series,
                                                                  high: pd.Series, low: pd.Series,
                                                                  volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in exhaustion/breakaway down ratio (63d)."""
    ex = _rolling_sum(_exhaustion_gap_down_flag(close, open, high, low, volume), _TD_QTR)
    ba = _rolling_sum(_breakaway_gap_down_flag(close, open, high, low, volume), _TD_QTR)
    ratio = _safe_div(ex, ba.clip(lower=1))
    vel21 = ratio.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_019_gap_down_share_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day down-gap share."""
    dn_sum = _rolling_sum(_gap_down(close, open), _TD_QTR)
    tot_sum = _rolling_sum(_gap_pct(close, open).abs(), _TD_QTR).clip(lower=_EPS)
    share = _safe_div(dn_sum, tot_sum)
    vel21 = share.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_020_gap_abs_ewm_21d_5d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """Second 5-day diff of 21-span EWM of abs gap (jerk in smoothed gap size)."""
    ewm = _ewm_mean(_gap_pct(close, open).abs(), _TD_MON)
    vel = ewm.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def gap_drv3_021_gap_down_sum_63d_21d_diff_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day change in 63-day cumulative down-gap return."""
    dg_sum = _rolling_sum(_gap_down(close, open), _TD_QTR)
    vel21 = dg_sum.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def gap_drv3_022_gap_signed_avg_21d_5d_diff_slope(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-diff of 21-day signed avg gap."""
    avg = _rolling_mean(_gap_pct(close, open), _TD_MON)
    vel = avg.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def gap_drv3_023_exhaustion_gap_down_ewm_21d_slope(close: pd.Series, open: pd.Series,
                                                     high: pd.Series, low: pd.Series,
                                                     volume: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 21-span EWM of down-exhaustion flag (trend in capitulation EWM)."""
    flag = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ewm = _ewm_mean(flag, _TD_MON)
    return _linslope(ewm, _TD_MON)


def gap_drv3_024_gap_std_21d_5d_diff_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day-velocity of 21-day gap std."""
    s = _rolling_std(_gap_pct(close, open), _TD_MON)
    vel = s.diff(_TD_WEEK)
    return _linslope(vel, _TD_MON)


def gap_drv3_025_gap_type_distress_score_slope_63d_5d_diff(close: pd.Series, open: pd.Series,
                                                             high: pd.Series, low: pd.Series,
                                                             volume: pd.Series) -> pd.Series:
    """5-day diff of OLS slope of 21-day distress score over 63 days (acceleration of distress trend)."""
    ex_dn = _exhaustion_gap_down_flag(close, open, high, low, volume)
    ba_dn = _breakaway_gap_down_flag(close, open, high, low, volume)
    score_raw = 2.0 * ex_dn + 1.0 * ba_dn
    score_21 = _rolling_sum(score_raw, _TD_MON)
    slope = _linslope(score_21, _TD_QTR)
    return slope.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

GAP_STRUCTURE_REGISTRY_3RD_DERIVATIVES = {
    "gap_drv3_001_avg_gap_abs_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_001_avg_gap_abs_21d_5d_diff_5d_diff},
    "gap_drv3_002_avg_gap_abs_21d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_002_avg_gap_abs_21d_21d_diff_5d_diff},
    "gap_drv3_003_gap_down_freq_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_003_gap_down_freq_21d_5d_diff_5d_diff},
    "gap_drv3_004_gap_std_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_004_gap_std_21d_5d_diff_5d_diff},
    "gap_drv3_005_gap_down_sum_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_005_gap_down_sum_21d_5d_diff_5d_diff},
    "gap_drv3_006_gap_down_freq_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_006_gap_down_freq_63d_21d_diff_5d_diff},
    "gap_drv3_007_gap_std_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_007_gap_std_63d_21d_diff_5d_diff},
    "gap_drv3_008_gap_abs_zscore_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_008_gap_abs_zscore_5d_diff_5d_diff},
    "gap_drv3_009_gap_net_bias_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_009_gap_net_bias_63d_21d_diff_5d_diff},
    "gap_drv3_010_gap_vol_ratio_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_010_gap_vol_ratio_5d_diff_5d_diff},
    "gap_drv3_011_exhaustion_gap_down_count_63d_21d_diff_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_011_exhaustion_gap_down_count_63d_21d_diff_5d_diff},
    "gap_drv3_012_breakaway_gap_down_count_63d_21d_diff_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_012_breakaway_gap_down_count_63d_21d_diff_5d_diff},
    "gap_drv3_013_exhaustion_gap_down_ewm_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_013_exhaustion_gap_down_ewm_5d_diff_5d_diff},
    "gap_drv3_014_breakaway_gap_down_ewm_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_014_breakaway_gap_down_ewm_5d_diff_5d_diff},
    "gap_drv3_015_gap_type_distress_score_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_015_gap_type_distress_score_21d_5d_diff_5d_diff},
    "gap_drv3_016_exhaustion_gap_down_count_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_016_exhaustion_gap_down_count_21d_5d_diff_5d_diff},
    "gap_drv3_017_exhaustion_gap_all_count_21d_5d_diff_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_017_exhaustion_gap_all_count_21d_5d_diff_5d_diff},
    "gap_drv3_018_exhaustion_vs_breakaway_ratio_21d_diff_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_018_exhaustion_vs_breakaway_ratio_21d_diff_5d_diff},
    "gap_drv3_019_gap_down_share_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_019_gap_down_share_63d_21d_diff_5d_diff},
    "gap_drv3_020_gap_abs_ewm_21d_5d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_020_gap_abs_ewm_21d_5d_diff_5d_diff},
    "gap_drv3_021_gap_down_sum_63d_21d_diff_5d_diff": {"inputs": ["close", "open"], "func": gap_drv3_021_gap_down_sum_63d_21d_diff_5d_diff},
    "gap_drv3_022_gap_signed_avg_21d_5d_diff_slope": {"inputs": ["close", "open"], "func": gap_drv3_022_gap_signed_avg_21d_5d_diff_slope},
    "gap_drv3_023_exhaustion_gap_down_ewm_21d_slope": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_023_exhaustion_gap_down_ewm_21d_slope},
    "gap_drv3_024_gap_std_21d_5d_diff_slope_21d": {"inputs": ["close", "open"], "func": gap_drv3_024_gap_std_21d_5d_diff_slope_21d},
    "gap_drv3_025_gap_type_distress_score_slope_63d_5d_diff": {"inputs": ["close", "open", "high", "low", "volume"], "func": gap_drv3_025_gap_type_distress_score_slope_63d_5d_diff},
}
