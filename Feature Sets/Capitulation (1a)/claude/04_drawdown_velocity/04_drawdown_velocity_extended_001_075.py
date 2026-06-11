"""
04_drawdown_velocity — Extended Features 001-075
Domain: speed of price decline, slope of the fall, drawdown velocity —
        deeper variants: high-low velocity, open-gap velocity, EWM-based speed,
        drawdown rate across additional windows, volume-scaled speed composites,
        volatility-regime-conditioned velocity, percentile rank and z-score
        expansions, decay-curve metrics, and cross-horizon speed signals.
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
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _log_ret(s: pd.Series, n: int = 1) -> pd.Series:
    return np.log(s.clip(lower=_EPS)).diff(n)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rolling_slope(s: pd.Series, w: int) -> pd.Series:
    """OLS slope of s over rolling window of length w."""
    def _slope(y):
        if len(y) < 2:
            return np.nan
        x = np.arange(len(y), dtype=float)
        xm = x - x.mean()
        ym = y - y.mean()
        denom = (xm * xm).sum()
        if denom == 0:
            return np.nan
        return (xm * ym).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=True)


def _atr(high: pd.Series, low: pd.Series, close: pd.Series, w: int = 14) -> pd.Series:
    tr = pd.concat([
        high - low,
        (high - close.shift(1)).abs(),
        (low - close.shift(1)).abs()
    ], axis=1).max(axis=1)
    return tr.rolling(w, min_periods=max(1, w // 2)).mean()


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-009): High-based and low-based velocity ---

def dvel_ext_001_high_vel_5d(high: pd.Series) -> pd.Series:
    """5-day log return of daily high — speed of upper bound descent."""
    return _log_ret(high, 5) / 5.0


def dvel_ext_002_high_vel_21d(high: pd.Series) -> pd.Series:
    """21-day log return of daily high normalised per day."""
    return _log_ret(high, _TD_MON) / _TD_MON


def dvel_ext_003_high_vel_63d(high: pd.Series) -> pd.Series:
    """63-day log return of daily high normalised per day."""
    return _log_ret(high, _TD_QTR) / _TD_QTR


def dvel_ext_004_low_vel_5d(low: pd.Series) -> pd.Series:
    """5-day log return of daily low — how fast lows are sinking."""
    return _log_ret(low, 5) / 5.0


def dvel_ext_005_low_vel_21d(low: pd.Series) -> pd.Series:
    """21-day log return of daily low normalised per day."""
    return _log_ret(low, _TD_MON) / _TD_MON


def dvel_ext_006_low_vel_63d(low: pd.Series) -> pd.Series:
    """63-day log return of daily low normalised per day."""
    return _log_ret(low, _TD_QTR) / _TD_QTR


def dvel_ext_007_hl_midpoint_vel_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """21-day velocity of the high-low midpoint — unbiased bar-centre descent rate."""
    mid = (high + low) / 2.0
    return _log_ret(mid, _TD_MON) / _TD_MON


def dvel_ext_008_hl_midpoint_vel_63d(high: pd.Series, low: pd.Series) -> pd.Series:
    """63-day velocity of the high-low midpoint."""
    mid = (high + low) / 2.0
    return _log_ret(mid, _TD_QTR) / _TD_QTR


def dvel_ext_009_low_vs_high_vel_divergence_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Low velocity minus high velocity over 21d — widening = expanding range on descent."""
    return _log_ret(low, _TD_MON) / _TD_MON - _log_ret(high, _TD_MON) / _TD_MON


# --- Group B (010-017): Open-gap velocity ---

def dvel_ext_010_open_gap_vel_1d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Overnight gap log-return (open / prev_close) — single-day gap-down speed."""
    return np.log(open_.clip(lower=_EPS)) - np.log(close.shift(1).clip(lower=_EPS))


def dvel_ext_011_open_gap_vel_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """21-day rolling mean of overnight gap log-return — persistent gap-down velocity."""
    gap = np.log(open_.clip(lower=_EPS)) - np.log(close.shift(1).clip(lower=_EPS))
    return _rolling_mean(gap, _TD_MON)


def dvel_ext_012_open_gap_vel_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """63-day rolling mean of overnight gap log-return."""
    gap = np.log(open_.clip(lower=_EPS)) - np.log(close.shift(1).clip(lower=_EPS))
    return _rolling_mean(gap, _TD_QTR)


def dvel_ext_013_open_gap_neg_freq_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Fraction of 21d days with negative overnight gap."""
    gap = np.log(open_.clip(lower=_EPS)) - np.log(close.shift(1).clip(lower=_EPS))
    return (gap < 0).astype(float).rolling(_TD_MON, min_periods=10).mean()


def dvel_ext_014_open_gap_neg_freq_63d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Fraction of 63d days with negative overnight gap."""
    gap = np.log(open_.clip(lower=_EPS)) - np.log(close.shift(1).clip(lower=_EPS))
    return (gap < 0).astype(float).rolling(_TD_QTR, min_periods=30).mean()


def dvel_ext_015_intraday_vel_1d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Single-day intraday log-return (close / open) — within-day directional speed."""
    return np.log(close.clip(lower=_EPS)) - np.log(open_.clip(lower=_EPS))


def dvel_ext_016_intraday_vel_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean of intraday log-returns over 21d — persistent intraday down-bias."""
    intra = np.log(close.clip(lower=_EPS)) - np.log(open_.clip(lower=_EPS))
    return _rolling_mean(intra, _TD_MON)


def dvel_ext_017_gap_plus_intraday_vel_21d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Mean total daily log-return decomposed: overnight + intraday over 21d."""
    gap = np.log(open_.clip(lower=_EPS)) - np.log(close.shift(1).clip(lower=_EPS))
    intra = np.log(close.clip(lower=_EPS)) - np.log(open_.clip(lower=_EPS))
    return _rolling_mean(gap + intra, _TD_MON)


# --- Group C (018-026): EWM velocity variants ---

def dvel_ext_018_ewm_vel_span10(close: pd.Series) -> pd.Series:
    """Log-return of EWM(span=10) close — smooth fast descent speed."""
    s = _ewm_mean(close, 10)
    return _log_ret(s, 1)


def dvel_ext_019_ewm_vel_span21(close: pd.Series) -> pd.Series:
    """Log-return of EWM(span=21) close."""
    s = _ewm_mean(close, _TD_MON)
    return _log_ret(s, 1)


def dvel_ext_020_ewm_vel_span63(close: pd.Series) -> pd.Series:
    """Log-return of EWM(span=63) close — smooth medium-term descent speed."""
    s = _ewm_mean(close, _TD_QTR)
    return _log_ret(s, 1)


def dvel_ext_021_ewm_vel_spread_10v63(close: pd.Series) -> pd.Series:
    """EWM(10) velocity minus EWM(63) velocity — short-vs-long smooth speed divergence."""
    return _log_ret(_ewm_mean(close, 10), 1) - _log_ret(_ewm_mean(close, _TD_QTR), 1)


def dvel_ext_022_ewm_vel_spread_21v126(close: pd.Series) -> pd.Series:
    """EWM(21) velocity minus EWM(126) velocity."""
    return _log_ret(_ewm_mean(close, _TD_MON), 1) - _log_ret(_ewm_mean(close, _TD_HALF), 1)


def dvel_ext_023_ewm_slope_63d_logprice(close: pd.Series) -> pd.Series:
    """OLS slope of EWM(21)-smoothed log(close) over 63d window."""
    s = _ewm_mean(np.log(close.clip(lower=_EPS)), _TD_MON)
    return _rolling_slope(s, _TD_QTR)


def dvel_ext_024_ewm_slope_21d_logprice(close: pd.Series) -> pd.Series:
    """OLS slope of EWM(10)-smoothed log(close) over 21d window."""
    s = _ewm_mean(np.log(close.clip(lower=_EPS)), 10)
    return _rolling_slope(s, _TD_MON)


def dvel_ext_025_ewm_neg_vel_days_21d(close: pd.Series) -> pd.Series:
    """Fraction of 21d days where EWM(10) velocity is negative."""
    v = _log_ret(_ewm_mean(close, 10), 1)
    return (v < 0).astype(float).rolling(_TD_MON, min_periods=10).mean()


def dvel_ext_026_ewm_vel_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of EWM(10) daily velocity within trailing 63d distribution."""
    v = _log_ret(_ewm_mean(close, 10), 1)
    return _safe_div(v - _rolling_mean(v, _TD_QTR), _rolling_std(v, _TD_QTR))


# --- Group D (027-035): Drawdown velocity with additional window sizes ---

def dvel_ext_027_dd_vel_42d(close: pd.Series) -> pd.Series:
    """Drawdown depth from 42d high / days since 42d high — 2-month horizon."""
    roll_max = _rolling_max(close, 42)
    dd = _safe_div(close - roll_max, roll_max)
    days_since = close.rolling(42, min_periods=5).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dd, days_since + 1)


def dvel_ext_028_dd_vel_126d(close: pd.Series) -> pd.Series:
    """Drawdown depth from 126d high / days since 126d high — half-year horizon."""
    roll_max = _rolling_max(close, _TD_HALF)
    dd = _safe_div(close - roll_max, roll_max)
    days_since = close.rolling(_TD_HALF, min_periods=21).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    return _safe_div(dd, days_since + 1)


def dvel_ext_029_worst_3d_drop_in_21d(close: pd.Series) -> pd.Series:
    """Most negative 3-day log return within last 21 days."""
    return _log_ret(close, 3).rolling(_TD_MON, min_periods=5).min()


def dvel_ext_030_worst_3d_drop_in_63d(close: pd.Series) -> pd.Series:
    """Most negative 3-day log return within last 63 days."""
    return _log_ret(close, 3).rolling(_TD_QTR, min_periods=10).min()


def dvel_ext_031_worst_1d_drop_in_21d(close: pd.Series) -> pd.Series:
    """Most negative 1-day log return (worst day) within last 21 days."""
    return _log_ret(close, 1).rolling(_TD_MON, min_periods=5).min()


def dvel_ext_032_worst_1d_drop_in_63d(close: pd.Series) -> pd.Series:
    """Worst single-day log return within last 63 days."""
    return _log_ret(close, 1).rolling(_TD_QTR, min_periods=10).min()


def dvel_ext_033_worst_63d_drop_in_504d(close: pd.Series) -> pd.Series:
    """Most negative 63d log return within last 504 days (2-year window)."""
    return _log_ret(close, _TD_QTR).rolling(504, min_periods=_TD_QTR).min()


def dvel_ext_034_avg_worst_5pct_daily_vel_252d(close: pd.Series) -> pd.Series:
    """Mean of the worst 5% single-day log returns within trailing 252d — tail speed."""
    dr = _log_ret(close, 1)
    thresh = dr.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    return dr.where(dr <= thresh).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def dvel_ext_035_dd_vel_ratio_21v63(close: pd.Series) -> pd.Series:
    """Ratio of 21d drawdown velocity to 63d drawdown velocity — short vs medium speed."""
    roll_max21 = _rolling_max(close, _TD_MON)
    dd21 = _safe_div(close - roll_max21, roll_max21)
    ds21 = close.rolling(_TD_MON, min_periods=5).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    v21 = _safe_div(dd21, ds21 + 1)

    roll_max63 = _rolling_max(close, _TD_QTR)
    dd63 = _safe_div(close - roll_max63, roll_max63)
    ds63 = close.rolling(_TD_QTR, min_periods=10).apply(
        lambda x: len(x) - 1 - int(np.argmax(x)), raw=True)
    v63 = _safe_div(dd63, ds63 + 1)
    return _safe_div(v21, v63)


# --- Group E (036-044): Volatility-regime-conditioned velocity ---

def dvel_ext_036_vel_to_vol_ratio_63d_5d(close: pd.Series) -> pd.Series:
    """5d log-return / 63d realised vol — recent speed relative to medium-term vol."""
    v5 = _log_ret(close, 5)
    vol63 = _log_ret(close, 1).rolling(_TD_QTR, min_periods=10).std() * np.sqrt(_TD_QTR)
    return _safe_div(v5, vol63)


def dvel_ext_037_vel_to_vol_ratio_126d_21d(close: pd.Series) -> pd.Series:
    """21d log-return / 126d realised vol."""
    v21 = _log_ret(close, _TD_MON)
    vol126 = _log_ret(close, 1).rolling(_TD_HALF, min_periods=21).std() * np.sqrt(_TD_HALF)
    return _safe_div(v21, vol126)


def dvel_ext_038_vel_to_atr_ratio_5d(close: pd.Series, high: pd.Series,
                                      low: pd.Series) -> pd.Series:
    """5d price change / ATR(14) — speed relative to recent true-range volatility."""
    return _safe_div(close - close.shift(5), _atr(high, low, close, 14))


def dvel_ext_039_vel_to_atr_ratio_10d(close: pd.Series, high: pd.Series,
                                       low: pd.Series) -> pd.Series:
    """10d price change / ATR(14)."""
    return _safe_div(close - close.shift(10), _atr(high, low, close, 14))


def dvel_ext_040_neg_vel_vol_ratio_21d(close: pd.Series) -> pd.Series:
    """Ratio: mean negative daily return / std of all daily returns over 21d —
    downside speed relative to total dispersion."""
    dr = _log_ret(close, 1)
    neg_mean = dr.where(dr < 0).rolling(_TD_MON, min_periods=5).mean()
    total_std = _rolling_std(dr, _TD_MON)
    return _safe_div(neg_mean, total_std)


def dvel_ext_041_downside_vol_share_63d(close: pd.Series) -> pd.Series:
    """Fraction of total variance attributable to negative-return days over 63d."""
    dr = _log_ret(close, 1)
    neg_var = (dr.where(dr < 0, 0) ** 2).rolling(_TD_QTR, min_periods=10).sum()
    tot_var = (dr ** 2).rolling(_TD_QTR, min_periods=10).sum()
    return _safe_div(neg_var, tot_var)


def dvel_ext_042_high_vol_regime_neg_vel_63d(close: pd.Series) -> pd.Series:
    """Mean negative daily velocity on high-vol days (vol > 63d median vol) over 63d."""
    dr = _log_ret(close, 1)
    vol21 = _rolling_std(dr, _TD_MON)
    med_vol = vol21.rolling(_TD_QTR, min_periods=10).median()
    high_vol_day = vol21 > med_vol
    neg_high_vol = dr.where((dr < 0) & high_vol_day)
    return neg_high_vol.rolling(_TD_QTR, min_periods=10).mean()


def dvel_ext_043_atr_norm_vel_126d(close: pd.Series, high: pd.Series,
                                    low: pd.Series) -> pd.Series:
    """126d price change normalized by ATR(63)."""
    return _safe_div(close - close.shift(_TD_HALF), _atr(high, low, close, _TD_QTR))


def dvel_ext_044_realised_vol_ratio_21v252(close: pd.Series) -> pd.Series:
    """Ratio of 21d realised vol to 252d realised vol — vol regime shift indicator;
    > 1 means current volatility is elevated (panic regime)."""
    dr = _log_ret(close, 1)
    vol21 = _rolling_std(dr, _TD_MON)
    vol252 = _rolling_std(dr, _TD_YEAR)
    return _safe_div(vol21, vol252)


# --- Group F (045-053): Percentile rank and z-score of velocity ---

def dvel_ext_045_vel_pctrank_252d_1d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 1-day velocity in trailing 252d distribution."""
    return _log_ret(close, 1).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dvel_ext_046_vel_pctrank_252d_63d(close: pd.Series) -> pd.Series:
    """Percentile rank of current 63d velocity in trailing 252d distribution."""
    return _log_ret(close, _TD_QTR).rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def dvel_ext_047_vel_pctrank_504d_21d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d velocity in trailing 504d (2yr) distribution."""
    return _log_ret(close, _TD_MON).rolling(504, min_periods=_TD_QTR).rank(pct=True)


def dvel_ext_048_vel_zscore_126d_5d(close: pd.Series) -> pd.Series:
    """Z-score of 5-day velocity vs trailing 126-day distribution."""
    v = _log_ret(close, 5)
    return _safe_div(v - _rolling_mean(v, _TD_HALF), _rolling_std(v, _TD_HALF))


def dvel_ext_049_vel_zscore_126d_21d(close: pd.Series) -> pd.Series:
    """Z-score of 21d velocity vs trailing 126d distribution."""
    v = _log_ret(close, _TD_MON)
    return _safe_div(v - _rolling_mean(v, _TD_HALF), _rolling_std(v, _TD_HALF))


def dvel_ext_050_neg_vel_freq_126d(close: pd.Series) -> pd.Series:
    """Fraction of 126d days with negative daily return."""
    dr = _log_ret(close, 1)
    return (dr < 0).astype(float).rolling(_TD_HALF, min_periods=21).mean()


def dvel_ext_051_neg_vel_freq_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252d days with negative daily return."""
    dr = _log_ret(close, 1)
    return (dr < 0).astype(float).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def dvel_ext_052_neg_21d_vel_freq_252d(close: pd.Series) -> pd.Series:
    """Fraction of rolling 21d-velocity observations < 0 over trailing 252d."""
    v21 = _log_ret(close, _TD_MON)
    return (v21 < 0).astype(float).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


def dvel_ext_053_vel_below_minus2std_freq_252d(close: pd.Series) -> pd.Series:
    """Fraction of 252d days where 1d velocity is below -2 sigma (extreme-down days)."""
    dr = _log_ret(close, 1)
    thresh = _rolling_mean(dr, _TD_YEAR) - 2.0 * _rolling_std(dr, _TD_YEAR)
    return (dr < thresh).astype(float).rolling(_TD_YEAR, min_periods=_TD_QTR).mean()


# --- Group G (054-062): Volume-velocity composites ---

def dvel_ext_054_dvol_vel_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day velocity of dollar volume (close * volume) — rate of change of trading value."""
    dvol = close * volume
    return _log_ret(dvol, 5) / 5.0


def dvel_ext_055_dvol_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21-day velocity of dollar volume."""
    dvol = close * volume
    return _log_ret(dvol, _TD_MON) / _TD_MON


def dvel_ext_056_vwap_neg_vel_freq_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63d days where rolling 5d VWAP had a negative return."""
    vwap = _safe_div(
        (close * volume).rolling(5, min_periods=3).sum(),
        _rolling_sum(volume, 5))
    return (_log_ret(vwap, 1) < 0).astype(float).rolling(_TD_QTR, min_periods=10).mean()


def dvel_ext_057_vol_surge_neg_vel_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg volume-normalised magnitude of negative daily returns over 21d.
    (volume-weighted downside thrust)."""
    dr = _log_ret(close, 1)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    return (dr.where(dr < 0, 0) * vol_norm.fillna(1.0)).rolling(_TD_MON, min_periods=5).mean()


def dvel_ext_058_vol_surge_neg_vel_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted downside thrust over 63d."""
    dr = _log_ret(close, 1)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_QTR))
    return (dr.where(dr < 0, 0) * vol_norm.fillna(1.0)).rolling(_TD_QTR, min_periods=10).mean()


def dvel_ext_059_heavy_down_day_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 63d days that are both negative-return AND above-median volume —
    heavy-selling sessions."""
    dr = _log_ret(close, 1)
    med_vol = _rolling_mean(volume, _TD_QTR)
    heavy_down = ((dr < 0) & (volume > med_vol)).astype(float)
    return heavy_down.rolling(_TD_QTR, min_periods=10).sum()


def dvel_ext_060_heavy_down_day_pct_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of 63d days that are heavy-selling sessions."""
    dr = _log_ret(close, 1)
    med_vol = _rolling_mean(volume, _TD_QTR)
    heavy_down = ((dr < 0) & (volume > med_vol)).astype(float)
    return heavy_down.rolling(_TD_QTR, min_periods=10).mean()


def dvel_ext_061_vwap_vel_126d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """126-day VWAP velocity: rate of change of rolling VWAP."""
    vwap = _safe_div(
        (close * volume).rolling(_TD_HALF, min_periods=21).sum(),
        _rolling_sum(volume, _TD_HALF))
    return _log_ret(vwap, _TD_MON) / _TD_MON


def dvel_ext_062_vol_wtd_down_vel_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of 21d vol-weighted downside velocity vs 252d distribution."""
    dr = _log_ret(close, 1)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    vw_neg = (dr.where(dr < 0, 0) * vol_norm.fillna(1.0)).rolling(_TD_MON, min_periods=5).mean()
    return _safe_div(vw_neg - _rolling_mean(vw_neg, _TD_YEAR),
                     _rolling_std(vw_neg, _TD_YEAR))


# --- Group H (063-069): Velocity decay / half-life metrics ---

def dvel_ext_063_vel_halflife_proxy_63d(close: pd.Series) -> pd.Series:
    """AR(1) coefficient of daily log-returns over 63d — proxy for velocity persistence.
    Near 1 = momentum (speed persists); near 0 = random; negative = mean-reverting."""
    dr = _log_ret(close, 1)
    def _ar1(y):
        if len(y) < 3:
            return np.nan
        x = y[:-1]
        y2 = y[1:]
        xm, ym = x.mean(), y2.mean()
        denom = np.sum((x - xm) ** 2)
        if denom < _EPS:
            return np.nan
        return np.sum((x - xm) * (y2 - ym)) / denom
    return dr.rolling(63, min_periods=20).apply(_ar1, raw=True)


def dvel_ext_064_vel_mean_reversion_score_21d(close: pd.Series) -> pd.Series:
    """Mean reversion of velocity: negative of AR(1) coef of daily returns over 21d.
    More positive = stronger mean reversion of the decline speed."""
    dr = _log_ret(close, 1)
    def _neg_ar1(y):
        if len(y) < 3:
            return np.nan
        x = y[:-1]
        y2 = y[1:]
        xm, ym = x.mean(), y2.mean()
        denom = np.sum((x - xm) ** 2)
        if denom < _EPS:
            return np.nan
        return -np.sum((x - xm) * (y2 - ym)) / denom
    return dr.rolling(21, min_periods=8).apply(_neg_ar1, raw=True)


def dvel_ext_065_vel_ewm_decay_ratio_10v21(close: pd.Series) -> pd.Series:
    """Ratio EWM(10) velocity / EWM(21) velocity — fast decay vs slow decay signal."""
    v10 = _log_ret(_ewm_mean(close, 10), 1)
    v21 = _log_ret(_ewm_mean(close, _TD_MON), 1)
    return _safe_div(v10, v21)


def dvel_ext_066_vel_trend_21d(close: pd.Series) -> pd.Series:
    """OLS slope of the 1-day velocity series over 21d — is speed increasing or decreasing?"""
    v1 = _log_ret(close, 1)
    return _rolling_slope(v1, _TD_MON)


def dvel_ext_067_vel_trend_63d(close: pd.Series) -> pd.Series:
    """OLS slope of the 1-day velocity series over 63d."""
    v1 = _log_ret(close, 1)
    return _rolling_slope(v1, _TD_QTR)


def dvel_ext_068_vel_curvature_63d(close: pd.Series) -> pd.Series:
    """Second difference of 21d velocity: rate of change of velocity change over 63d.
    Negative = velocity is deteriorating faster."""
    v21 = _log_ret(close, _TD_MON) / _TD_MON
    return v21.diff(21)


def dvel_ext_069_consec_streak_down_63d(close: pd.Series) -> pd.Series:
    """Maximum length of a consecutive-down-day streak within the last 63 days."""
    dr = _log_ret(close, 1)
    streak = _consec_streak(dr < 0)
    return streak.rolling(_TD_QTR, min_periods=10).max()


# --- Group I (070-075): Composite and cross-domain velocity features ---

def dvel_ext_070_vel_composite_z_all_horizons(close: pd.Series) -> pd.Series:
    """Composite: equal-weight z-score of 1d, 5d, 21d, 63d, 126d velocities
    vs their 252d distributions. More negative = broad-based velocity distress."""
    def _z(v, w=_TD_YEAR):
        return _safe_div(v - _rolling_mean(v, w), _rolling_std(v, w))
    v1  = _log_ret(close, 1)
    v5  = _log_ret(close, 5)
    v21 = _log_ret(close, _TD_MON)
    v63 = _log_ret(close, _TD_QTR)
    v126 = _log_ret(close, _TD_HALF)
    return (_z(v1) + _z(v5) + _z(v21) + _z(v63) + _z(v126)) / 5.0


def dvel_ext_071_hl_vel_vs_close_vel_21d(close: pd.Series, high: pd.Series,
                                          low: pd.Series) -> pd.Series:
    """(High velocity - Low velocity) / abs(Close velocity) over 21d —
    expanding HL range relative to close move = panic spreading."""
    hv = _log_ret(high, _TD_MON) / _TD_MON
    lv = _log_ret(low, _TD_MON) / _TD_MON
    cv = _log_ret(close, _TD_MON) / _TD_MON
    return _safe_div(hv - lv, cv.abs())


def dvel_ext_072_vol_adjusted_composite_vel_21d(close: pd.Series, high: pd.Series,
                                                 low: pd.Series,
                                                 volume: pd.Series) -> pd.Series:
    """Composite vol-adjusted velocity: z(5d vel/ATR) + z(21d vol-weighted neg vel)
    over 252d — surface combining speed and selling pressure."""
    v5_atr = _safe_div(close - close.shift(5), _atr(high, low, close, 14))
    dr = _log_ret(close, 1)
    vol_norm = _safe_div(volume, _rolling_mean(volume, _TD_MON))
    vw_neg = (dr.where(dr < 0, 0) * vol_norm.fillna(1.0)).rolling(_TD_MON, min_periods=5).mean()
    def _z(s):
        return _safe_div(s - _rolling_mean(s, _TD_YEAR), _rolling_std(s, _TD_YEAR))
    return (_z(v5_atr) + _z(vw_neg)) / 2.0


def dvel_ext_073_open_gap_vel_zscore_252d(close: pd.Series, open_: pd.Series) -> pd.Series:
    """Z-score of 21d mean overnight gap velocity vs 252d distribution."""
    gap = np.log(open_.clip(lower=_EPS)) - np.log(close.shift(1).clip(lower=_EPS))
    gap21 = _rolling_mean(gap, _TD_MON)
    return _safe_div(gap21 - _rolling_mean(gap21, _TD_YEAR), _rolling_std(gap21, _TD_YEAR))


def dvel_ext_074_vel_asymmetry_score_63d(close: pd.Series) -> pd.Series:
    """Up-day avg velocity minus down-day avg velocity over 63d —
    larger negative = heavier falling vs lifting."""
    dr = _log_ret(close, 1)
    up_vel = dr.where(dr > 0).rolling(_TD_QTR, min_periods=10).mean()
    dn_vel = dr.where(dr < 0).rolling(_TD_QTR, min_periods=10).mean()
    return up_vel + dn_vel  # up positive, down negative; sum negative = sell dominates


def dvel_ext_075_capitulation_vel_score(close: pd.Series, high: pd.Series,
                                         low: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation velocity score: composite of z-scored worst-1d drop in 21d,
    heavy-selling day count (63d), vol-adjusted 5d velocity, and HL midpoint
    21d velocity — all scaled to 252d, summed and averaged."""
    def _z(s, w=_TD_YEAR):
        return _safe_div(s - _rolling_mean(s, w), _rolling_std(s, w))
    # worst 1d drop in 21d (more negative = worse)
    w1 = _log_ret(close, 1).rolling(_TD_MON, min_periods=5).min()
    # heavy down day count 63d
    dr = _log_ret(close, 1)
    med_vol = _rolling_mean(volume, _TD_QTR)
    hd = ((dr < 0) & (volume > med_vol)).astype(float).rolling(_TD_QTR, min_periods=10).sum()
    # vol-adjusted 5d velocity
    v5_atr = _safe_div(close - close.shift(5), _atr(high, low, close, 14))
    # HL midpoint 21d velocity
    mid = (high + low) / 2.0
    midv = _log_ret(mid, _TD_MON) / _TD_MON
    return (_z(w1) + _z(hd) + _z(v5_atr) + _z(midv)) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

DRAWDOWN_VELOCITY_EXTENDED_REGISTRY_001_075 = {
    "dvel_ext_001_high_vel_5d":                    {"inputs": ["high"],                               "func": dvel_ext_001_high_vel_5d},
    "dvel_ext_002_high_vel_21d":                   {"inputs": ["high"],                               "func": dvel_ext_002_high_vel_21d},
    "dvel_ext_003_high_vel_63d":                   {"inputs": ["high"],                               "func": dvel_ext_003_high_vel_63d},
    "dvel_ext_004_low_vel_5d":                     {"inputs": ["low"],                                "func": dvel_ext_004_low_vel_5d},
    "dvel_ext_005_low_vel_21d":                    {"inputs": ["low"],                                "func": dvel_ext_005_low_vel_21d},
    "dvel_ext_006_low_vel_63d":                    {"inputs": ["low"],                                "func": dvel_ext_006_low_vel_63d},
    "dvel_ext_007_hl_midpoint_vel_21d":            {"inputs": ["high", "low"],                        "func": dvel_ext_007_hl_midpoint_vel_21d},
    "dvel_ext_008_hl_midpoint_vel_63d":            {"inputs": ["high", "low"],                        "func": dvel_ext_008_hl_midpoint_vel_63d},
    "dvel_ext_009_low_vs_high_vel_divergence_21d": {"inputs": ["high", "low"],                        "func": dvel_ext_009_low_vs_high_vel_divergence_21d},
    "dvel_ext_010_open_gap_vel_1d":                {"inputs": ["close", "open"],                      "func": dvel_ext_010_open_gap_vel_1d},
    "dvel_ext_011_open_gap_vel_21d":               {"inputs": ["close", "open"],                      "func": dvel_ext_011_open_gap_vel_21d},
    "dvel_ext_012_open_gap_vel_63d":               {"inputs": ["close", "open"],                      "func": dvel_ext_012_open_gap_vel_63d},
    "dvel_ext_013_open_gap_neg_freq_21d":          {"inputs": ["close", "open"],                      "func": dvel_ext_013_open_gap_neg_freq_21d},
    "dvel_ext_014_open_gap_neg_freq_63d":          {"inputs": ["close", "open"],                      "func": dvel_ext_014_open_gap_neg_freq_63d},
    "dvel_ext_015_intraday_vel_1d":                {"inputs": ["close", "open"],                      "func": dvel_ext_015_intraday_vel_1d},
    "dvel_ext_016_intraday_vel_21d":               {"inputs": ["close", "open"],                      "func": dvel_ext_016_intraday_vel_21d},
    "dvel_ext_017_gap_plus_intraday_vel_21d":      {"inputs": ["close", "open"],                      "func": dvel_ext_017_gap_plus_intraday_vel_21d},
    "dvel_ext_018_ewm_vel_span10":                 {"inputs": ["close"],                              "func": dvel_ext_018_ewm_vel_span10},
    "dvel_ext_019_ewm_vel_span21":                 {"inputs": ["close"],                              "func": dvel_ext_019_ewm_vel_span21},
    "dvel_ext_020_ewm_vel_span63":                 {"inputs": ["close"],                              "func": dvel_ext_020_ewm_vel_span63},
    "dvel_ext_021_ewm_vel_spread_10v63":           {"inputs": ["close"],                              "func": dvel_ext_021_ewm_vel_spread_10v63},
    "dvel_ext_022_ewm_vel_spread_21v126":          {"inputs": ["close"],                              "func": dvel_ext_022_ewm_vel_spread_21v126},
    "dvel_ext_023_ewm_slope_63d_logprice":         {"inputs": ["close"],                              "func": dvel_ext_023_ewm_slope_63d_logprice},
    "dvel_ext_024_ewm_slope_21d_logprice":         {"inputs": ["close"],                              "func": dvel_ext_024_ewm_slope_21d_logprice},
    "dvel_ext_025_ewm_neg_vel_days_21d":           {"inputs": ["close"],                              "func": dvel_ext_025_ewm_neg_vel_days_21d},
    "dvel_ext_026_ewm_vel_zscore_63d":             {"inputs": ["close"],                              "func": dvel_ext_026_ewm_vel_zscore_63d},
    "dvel_ext_027_dd_vel_42d":                     {"inputs": ["close"],                              "func": dvel_ext_027_dd_vel_42d},
    "dvel_ext_028_dd_vel_126d":                    {"inputs": ["close"],                              "func": dvel_ext_028_dd_vel_126d},
    "dvel_ext_029_worst_3d_drop_in_21d":           {"inputs": ["close"],                              "func": dvel_ext_029_worst_3d_drop_in_21d},
    "dvel_ext_030_worst_3d_drop_in_63d":           {"inputs": ["close"],                              "func": dvel_ext_030_worst_3d_drop_in_63d},
    "dvel_ext_031_worst_1d_drop_in_21d":           {"inputs": ["close"],                              "func": dvel_ext_031_worst_1d_drop_in_21d},
    "dvel_ext_032_worst_1d_drop_in_63d":           {"inputs": ["close"],                              "func": dvel_ext_032_worst_1d_drop_in_63d},
    "dvel_ext_033_worst_63d_drop_in_504d":         {"inputs": ["close"],                              "func": dvel_ext_033_worst_63d_drop_in_504d},
    "dvel_ext_034_avg_worst_5pct_daily_vel_252d":  {"inputs": ["close"],                              "func": dvel_ext_034_avg_worst_5pct_daily_vel_252d},
    "dvel_ext_035_dd_vel_ratio_21v63":             {"inputs": ["close"],                              "func": dvel_ext_035_dd_vel_ratio_21v63},
    "dvel_ext_036_vel_to_vol_ratio_63d_5d":        {"inputs": ["close"],                              "func": dvel_ext_036_vel_to_vol_ratio_63d_5d},
    "dvel_ext_037_vel_to_vol_ratio_126d_21d":      {"inputs": ["close"],                              "func": dvel_ext_037_vel_to_vol_ratio_126d_21d},
    "dvel_ext_038_vel_to_atr_ratio_5d":            {"inputs": ["close", "high", "low"],               "func": dvel_ext_038_vel_to_atr_ratio_5d},
    "dvel_ext_039_vel_to_atr_ratio_10d":           {"inputs": ["close", "high", "low"],               "func": dvel_ext_039_vel_to_atr_ratio_10d},
    "dvel_ext_040_neg_vel_vol_ratio_21d":          {"inputs": ["close"],                              "func": dvel_ext_040_neg_vel_vol_ratio_21d},
    "dvel_ext_041_downside_vol_share_63d":         {"inputs": ["close"],                              "func": dvel_ext_041_downside_vol_share_63d},
    "dvel_ext_042_high_vol_regime_neg_vel_63d":    {"inputs": ["close"],                              "func": dvel_ext_042_high_vol_regime_neg_vel_63d},
    "dvel_ext_043_atr_norm_vel_126d":              {"inputs": ["close", "high", "low"],               "func": dvel_ext_043_atr_norm_vel_126d},
    "dvel_ext_044_realised_vol_ratio_21v252":      {"inputs": ["close"],                              "func": dvel_ext_044_realised_vol_ratio_21v252},
    "dvel_ext_045_vel_pctrank_252d_1d":            {"inputs": ["close"],                              "func": dvel_ext_045_vel_pctrank_252d_1d},
    "dvel_ext_046_vel_pctrank_252d_63d":           {"inputs": ["close"],                              "func": dvel_ext_046_vel_pctrank_252d_63d},
    "dvel_ext_047_vel_pctrank_504d_21d":           {"inputs": ["close"],                              "func": dvel_ext_047_vel_pctrank_504d_21d},
    "dvel_ext_048_vel_zscore_126d_5d":             {"inputs": ["close"],                              "func": dvel_ext_048_vel_zscore_126d_5d},
    "dvel_ext_049_vel_zscore_126d_21d":            {"inputs": ["close"],                              "func": dvel_ext_049_vel_zscore_126d_21d},
    "dvel_ext_050_neg_vel_freq_126d":              {"inputs": ["close"],                              "func": dvel_ext_050_neg_vel_freq_126d},
    "dvel_ext_051_neg_vel_freq_252d":              {"inputs": ["close"],                              "func": dvel_ext_051_neg_vel_freq_252d},
    "dvel_ext_052_neg_21d_vel_freq_252d":          {"inputs": ["close"],                              "func": dvel_ext_052_neg_21d_vel_freq_252d},
    "dvel_ext_053_vel_below_minus2std_freq_252d":  {"inputs": ["close"],                              "func": dvel_ext_053_vel_below_minus2std_freq_252d},
    "dvel_ext_054_dvol_vel_5d":                    {"inputs": ["close", "volume"],                    "func": dvel_ext_054_dvol_vel_5d},
    "dvel_ext_055_dvol_vel_21d":                   {"inputs": ["close", "volume"],                    "func": dvel_ext_055_dvol_vel_21d},
    "dvel_ext_056_vwap_neg_vel_freq_63d":          {"inputs": ["close", "volume"],                    "func": dvel_ext_056_vwap_neg_vel_freq_63d},
    "dvel_ext_057_vol_surge_neg_vel_21d":          {"inputs": ["close", "volume"],                    "func": dvel_ext_057_vol_surge_neg_vel_21d},
    "dvel_ext_058_vol_surge_neg_vel_63d":          {"inputs": ["close", "volume"],                    "func": dvel_ext_058_vol_surge_neg_vel_63d},
    "dvel_ext_059_heavy_down_day_count_63d":       {"inputs": ["close", "volume"],                    "func": dvel_ext_059_heavy_down_day_count_63d},
    "dvel_ext_060_heavy_down_day_pct_63d":         {"inputs": ["close", "volume"],                    "func": dvel_ext_060_heavy_down_day_pct_63d},
    "dvel_ext_061_vwap_vel_126d":                  {"inputs": ["close", "volume"],                    "func": dvel_ext_061_vwap_vel_126d},
    "dvel_ext_062_vol_wtd_down_vel_zscore_252d":   {"inputs": ["close", "volume"],                    "func": dvel_ext_062_vol_wtd_down_vel_zscore_252d},
    "dvel_ext_063_vel_halflife_proxy_63d":         {"inputs": ["close"],                              "func": dvel_ext_063_vel_halflife_proxy_63d},
    "dvel_ext_064_vel_mean_reversion_score_21d":   {"inputs": ["close"],                              "func": dvel_ext_064_vel_mean_reversion_score_21d},
    "dvel_ext_065_vel_ewm_decay_ratio_10v21":      {"inputs": ["close"],                              "func": dvel_ext_065_vel_ewm_decay_ratio_10v21},
    "dvel_ext_066_vel_trend_21d":                  {"inputs": ["close"],                              "func": dvel_ext_066_vel_trend_21d},
    "dvel_ext_067_vel_trend_63d":                  {"inputs": ["close"],                              "func": dvel_ext_067_vel_trend_63d},
    "dvel_ext_068_vel_curvature_63d":              {"inputs": ["close"],                              "func": dvel_ext_068_vel_curvature_63d},
    "dvel_ext_069_consec_streak_down_63d":         {"inputs": ["close"],                              "func": dvel_ext_069_consec_streak_down_63d},
    "dvel_ext_070_vel_composite_z_all_horizons":   {"inputs": ["close"],                              "func": dvel_ext_070_vel_composite_z_all_horizons},
    "dvel_ext_071_hl_vel_vs_close_vel_21d":        {"inputs": ["close", "high", "low"],               "func": dvel_ext_071_hl_vel_vs_close_vel_21d},
    "dvel_ext_072_vol_adjusted_composite_vel_21d": {"inputs": ["close", "high", "low", "volume"],     "func": dvel_ext_072_vol_adjusted_composite_vel_21d},
    "dvel_ext_073_open_gap_vel_zscore_252d":       {"inputs": ["close", "open"],                      "func": dvel_ext_073_open_gap_vel_zscore_252d},
    "dvel_ext_074_vel_asymmetry_score_63d":        {"inputs": ["close"],                              "func": dvel_ext_074_vel_asymmetry_score_63d},
    "dvel_ext_075_capitulation_vel_score":         {"inputs": ["close", "high", "low", "volume"],     "func": dvel_ext_075_capitulation_vel_score},
}
