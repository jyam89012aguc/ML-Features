"""
35_capitulation_thrust — Extended 2nd Derivatives (Features cth_extdrv2_001-025)
Domain: rate of change of extended base capitulation-thrust concepts — velocity of
        extended thrust measures. Diffs (5d/21d), pct_change, and rolling OLS slopes
        applied to extended base feature concepts.
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
    """Rolling OLS slope over w periods (backward-looking)."""
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def cth_extdrv2_001_min_return_3d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of worst-3d-return in 10-day window (velocity of short-horizon thrust depth)."""
    cum3  = _log_safe(close) - _log_safe(close.shift(3))
    worst = _rolling_min(cum3, 10)
    return worst.diff(_TD_WEEK)


def cth_extdrv2_002_min_return_7d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of worst-7d-return in 21-day window (monthly velocity of weekly thrust)."""
    cum7  = _log_safe(close) - _log_safe(close.shift(7))
    worst = _rolling_min(cum7, _TD_MON)
    return worst.diff(_TD_MON)


def cth_extdrv2_003_cum_loss_3d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 3-day clipped cumulative loss (velocity of 3-day loss accumulation)."""
    lr   = _log_ret(close).clip(upper=0)
    cum3 = _rolling_sum(lr, 3)
    return cum3.diff(_TD_WEEK)


def cth_extdrv2_004_cum_loss_10d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 10-day clipped cumulative loss (velocity of 10-day loss pace)."""
    lr    = _log_ret(close).clip(upper=0)
    cum10 = _rolling_sum(lr, 10)
    return cum10.diff(_TD_WEEK)


def cth_extdrv2_005_cum_loss_21d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of 21-day clipped cumulative loss (monthly acceleration of monthly loss)."""
    lr    = _log_ret(close).clip(upper=0)
    cum21 = _rolling_sum(lr, _TD_MON)
    return cum21.diff(_TD_MON)


def cth_extdrv2_006_vol_confirmed_down_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of count of volume-confirmed down-days in 21-day window."""
    lr      = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    flag    = ((lr < 0) & (volume > avg_vol)).astype(float)
    cnt     = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def cth_extdrv2_007_vol_down_frac_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day fraction of volume traded on down-days."""
    lr       = _log_ret(close)
    down_vol = volume.where(lr < 0, 0.0)
    frac     = _safe_div(_rolling_sum(down_vol, _TD_MON), _rolling_sum(volume, _TD_MON))
    return frac.diff(_TD_WEEK)


def cth_extdrv2_008_consec_new_low_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive-new-21d-low streak (velocity of new-low formation)."""
    lo21 = close.rolling(_TD_MON, min_periods=1).min().shift(1)
    cond = close < lo21
    c    = cond.astype(int)
    grp  = (~cond).cumsum()
    streak = c.groupby(grp).cumsum().astype(float)
    return streak.diff(_TD_WEEK)


def cth_extdrv2_009_consec_down_days_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of consecutive down-day streak (acceleration of consecutive down days)."""
    lr   = _log_ret(close)
    cond = lr < 0
    c    = cond.astype(int)
    grp  = (~cond).cumsum()
    streak = c.groupby(grp).cumsum().astype(float)
    return streak.diff(_TD_WEEK)


def cth_extdrv2_010_overnight_ret_21d_sum_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day overnight return sum (velocity of overnight gap accumulation)."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    cum21     = _rolling_sum(overnight, _TD_MON)
    return cum21.diff(_TD_WEEK)


def cth_extdrv2_011_intraday_ret_21d_sum_5d_diff(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day diff of 21-day intraday return sum (velocity of body-loss accumulation)."""
    intraday = _log_safe(close) - _log_safe(open)
    cum21    = _rolling_sum(intraday, _TD_MON)
    return cum21.diff(_TD_WEEK)


def cth_extdrv2_012_atr_5d_vs_63d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 5d-ATR/63d-ATR ratio (velocity of range-expansion relative to baseline)."""
    atr  = _tr(close, high, low) / close.clip(lower=_EPS)
    r5   = _rolling_mean(atr, _TD_WEEK)
    r63  = _rolling_mean(atr, _TD_QTR)
    rat  = _safe_div(r5, r63)
    return rat.diff(_TD_WEEK)


def cth_extdrv2_013_atr_3d_vs_21d_5d_diff(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """5-day diff of 3d-ATR/21d-ATR ratio (velocity of ultra-short range burst)."""
    atr = _tr(close, high, low) / close.clip(lower=_EPS)
    r3  = _rolling_mean(atr, 3)
    r21 = _rolling_mean(atr, _TD_MON)
    rat = _safe_div(r3, r21)
    return rat.diff(_TD_WEEK)


def cth_extdrv2_014_boll_lower_depth_21d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of depth below 21-day Bollinger lower band (velocity of band penetration)."""
    mn    = _rolling_mean(close, _TD_MON)
    sd    = _rolling_std(close, _TD_MON)
    lower = mn - 2.0 * sd
    depth = (lower - close).clip(lower=0) / close.clip(lower=_EPS)
    return depth.diff(_TD_WEEK)


def cth_extdrv2_015_boll_lower_depth_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of depth below 63-day Bollinger lower band."""
    mn    = _rolling_mean(close, _TD_QTR)
    sd    = _rolling_std(close, _TD_QTR)
    lower = mn - 2.0 * sd
    depth = (lower - close).clip(lower=0) / close.clip(lower=_EPS)
    return depth.diff(_TD_MON)


def cth_extdrv2_016_new_21d_low_freq_63d_21d_diff(close: pd.Series) -> pd.Series:
    """21-day diff of count of new-21d-low closes in trailing 63 days."""
    lo21 = close.rolling(_TD_MON, min_periods=1).min().shift(1)
    flag = (close < lo21).astype(float)
    cnt  = _rolling_sum(flag, _TD_QTR)
    return cnt.diff(_TD_MON)


def cth_extdrv2_017_vol_confirmed_large_down_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of count of high-conviction thrust days in 21-day window."""
    lr      = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    flag    = ((lr < -0.015) & (volume > 1.5 * avg_vol)).astype(float)
    cnt     = _rolling_sum(flag, _TD_MON)
    return cnt.diff(_TD_WEEK)


def cth_extdrv2_018_tail_density_ratio_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 21d-vs-126d tail density ratio (velocity of tail concentration)."""
    lr    = _log_ret(close)
    mn    = _rolling_mean(lr, _TD_YEAR)
    sd    = _rolling_std(lr, _TD_YEAR)
    flag  = (lr < mn - 2.0 * sd).astype(float)
    f21   = _rolling_sum(flag, _TD_MON) / _TD_MON
    f126  = _rolling_sum(flag, _TD_HALF) / _TD_HALF
    ratio = _safe_div(f21, f126 + _EPS)
    return ratio.diff(_TD_WEEK)


def cth_extdrv2_019_obv_down_slope_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day OBV slope (velocity of on-balance-volume trend direction)."""
    lr   = _log_ret(close)
    sign = np.sign(lr).fillna(0)
    obv  = (sign * volume).cumsum()
    slp  = _linslope(obv, _TD_MON)
    return slp.diff(_TD_WEEK)


def cth_extdrv2_020_min_return_42d_slope_21d(close: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the worst-42d-return (trend in semi-quarterly thrust depth)."""
    cum42 = _log_safe(close) - _log_safe(close.shift(42))
    worst = _rolling_min(cum42, _TD_HALF)
    return _linslope(worst, _TD_MON)


def cth_extdrv2_021_thrust_regime_flag_5d_pct_change_21d(close: pd.Series) -> pd.Series:
    """21-day rolling sum of 5-day thrust regime flag (regime persistence velocity)."""
    cum5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    med  = _rolling_median(cum5, _TD_YEAR)
    mad  = (cum5 - med).abs().rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    flag = (cum5 < med - 2.0 * mad).astype(float)
    return _rolling_sum(flag, _TD_MON).diff(_TD_WEEK)


def cth_extdrv2_022_drawdown_126d_5d_diff(close: pd.Series) -> pd.Series:
    """5-day diff of 126-day drawdown from peak (velocity of semi-annual drawdown deepening)."""
    pk = _rolling_max(close, _TD_HALF)
    dd = _log_safe(close) - _log_safe(pk)
    return dd.diff(_TD_WEEK)


def cth_extdrv2_023_vol_weighted_cum_loss_21d_5d_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of 21-day volume-weighted cumulative loss (velocity of vol-adjusted selling)."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    score   = _rolling_sum(lr * vol_n, _TD_MON)
    return score.diff(_TD_WEEK)


def cth_extdrv2_024_overnight_vs_total_5d_slope_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the overnight/total-5d ratio (trend in gap-vs-body split)."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    total5    = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    over5     = _rolling_sum(overnight, _TD_WEEK)
    ratio     = _safe_div(over5, total5.abs() + _EPS)
    return _linslope(ratio, _TD_MON)


def cth_extdrv2_025_panic_4factor_score_5d_diff(close: pd.Series, high: pd.Series,
                                                  low: pd.Series, volume: pd.Series) -> pd.Series:
    """5-day diff of the 4-factor panic score (velocity of composite panic escalation)."""
    cum5    = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    z_ret   = _safe_div(cum5   - _rolling_mean(cum5,   _TD_YEAR), _rolling_std(cum5,   _TD_YEAR))
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_r   = _safe_div(volume, avg_vol)
    z_vol   = _safe_div(vol_r  - _rolling_mean(vol_r,  _TD_YEAR), _rolling_std(vol_r,  _TD_YEAR))
    atr_n   = _tr(close, high, low) / close.clip(lower=_EPS)
    z_atr   = _safe_div(atr_n  - _rolling_mean(atr_n,  _TD_YEAR), _rolling_std(atr_n,  _TD_YEAR))
    lr      = _log_ret(close)
    frac    = _rolling_sum((lr < 0).astype(float), _TD_MON) / _TD_MON
    z_frac  = _safe_div(frac   - _rolling_mean(frac,   _TD_YEAR), _rolling_std(frac,   _TD_YEAR))
    score   = (z_ret + z_vol + z_atr + z_frac) / 4.0
    return score.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITULATION_THRUST_EXTENDED_REGISTRY_2ND_DERIVATIVES = {
    "cth_extdrv2_001_min_return_3d_5d_diff": {"inputs": ["close"], "func": cth_extdrv2_001_min_return_3d_5d_diff},
    "cth_extdrv2_002_min_return_7d_21d_diff": {"inputs": ["close"], "func": cth_extdrv2_002_min_return_7d_21d_diff},
    "cth_extdrv2_003_cum_loss_3d_5d_diff": {"inputs": ["close"], "func": cth_extdrv2_003_cum_loss_3d_5d_diff},
    "cth_extdrv2_004_cum_loss_10d_5d_diff": {"inputs": ["close"], "func": cth_extdrv2_004_cum_loss_10d_5d_diff},
    "cth_extdrv2_005_cum_loss_21d_21d_diff": {"inputs": ["close"], "func": cth_extdrv2_005_cum_loss_21d_21d_diff},
    "cth_extdrv2_006_vol_confirmed_down_21d_5d_diff": {"inputs": ["close", "volume"], "func": cth_extdrv2_006_vol_confirmed_down_21d_5d_diff},
    "cth_extdrv2_007_vol_down_frac_21d_5d_diff": {"inputs": ["close", "volume"], "func": cth_extdrv2_007_vol_down_frac_21d_5d_diff},
    "cth_extdrv2_008_consec_new_low_21d_5d_diff": {"inputs": ["close"], "func": cth_extdrv2_008_consec_new_low_21d_5d_diff},
    "cth_extdrv2_009_consec_down_days_5d_diff": {"inputs": ["close"], "func": cth_extdrv2_009_consec_down_days_5d_diff},
    "cth_extdrv2_010_overnight_ret_21d_sum_5d_diff": {"inputs": ["close", "open"], "func": cth_extdrv2_010_overnight_ret_21d_sum_5d_diff},
    "cth_extdrv2_011_intraday_ret_21d_sum_5d_diff": {"inputs": ["close", "open"], "func": cth_extdrv2_011_intraday_ret_21d_sum_5d_diff},
    "cth_extdrv2_012_atr_5d_vs_63d_5d_diff": {"inputs": ["close", "high", "low"], "func": cth_extdrv2_012_atr_5d_vs_63d_5d_diff},
    "cth_extdrv2_013_atr_3d_vs_21d_5d_diff": {"inputs": ["close", "high", "low"], "func": cth_extdrv2_013_atr_3d_vs_21d_5d_diff},
    "cth_extdrv2_014_boll_lower_depth_21d_5d_diff": {"inputs": ["close"], "func": cth_extdrv2_014_boll_lower_depth_21d_5d_diff},
    "cth_extdrv2_015_boll_lower_depth_63d_21d_diff": {"inputs": ["close"], "func": cth_extdrv2_015_boll_lower_depth_63d_21d_diff},
    "cth_extdrv2_016_new_21d_low_freq_63d_21d_diff": {"inputs": ["close"], "func": cth_extdrv2_016_new_21d_low_freq_63d_21d_diff},
    "cth_extdrv2_017_vol_confirmed_large_down_21d_5d_diff": {"inputs": ["close", "volume"], "func": cth_extdrv2_017_vol_confirmed_large_down_21d_5d_diff},
    "cth_extdrv2_018_tail_density_ratio_5d_diff": {"inputs": ["close"], "func": cth_extdrv2_018_tail_density_ratio_5d_diff},
    "cth_extdrv2_019_obv_down_slope_21d_5d_diff": {"inputs": ["close", "volume"], "func": cth_extdrv2_019_obv_down_slope_21d_5d_diff},
    "cth_extdrv2_020_min_return_42d_slope_21d": {"inputs": ["close"], "func": cth_extdrv2_020_min_return_42d_slope_21d},
    "cth_extdrv2_021_thrust_regime_flag_5d_pct_change_21d": {"inputs": ["close"], "func": cth_extdrv2_021_thrust_regime_flag_5d_pct_change_21d},
    "cth_extdrv2_022_drawdown_126d_5d_diff": {"inputs": ["close"], "func": cth_extdrv2_022_drawdown_126d_5d_diff},
    "cth_extdrv2_023_vol_weighted_cum_loss_21d_5d_diff": {"inputs": ["close", "volume"], "func": cth_extdrv2_023_vol_weighted_cum_loss_21d_5d_diff},
    "cth_extdrv2_024_overnight_vs_total_5d_slope_21d": {"inputs": ["close", "open"], "func": cth_extdrv2_024_overnight_vs_total_5d_slope_21d},
    "cth_extdrv2_025_panic_4factor_score_5d_diff": {"inputs": ["close", "high", "low", "volume"], "func": cth_extdrv2_025_panic_4factor_score_5d_diff},
}
