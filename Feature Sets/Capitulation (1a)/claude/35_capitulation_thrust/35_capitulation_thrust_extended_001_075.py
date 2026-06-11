"""
35_capitulation_thrust — Extended Features 001-075
Domain: sharp final-leg-down thrust signatures — violent terminal acceleration of decline
        Extended variants: new windows, VWAP-based thrust, volume-confirmed thrusts,
        multi-day cumulative thrust magnitude, expanded percentile ranks, z-scores,
        regime flags, intraday gap-to-range patterns, consecutive new-low streaks,
        overnight vs intraday decomposition, multi-leg volume confluence, tail-event
        density ratios, high-low channel break frequency, candle compression patterns.
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


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c     = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-010): New-window steepest return variants ---

def cth_ext_001_min_return_3d(close: pd.Series) -> pd.Series:
    """Minimum (most negative) 3-day cumulative log-return in trailing 10-day window."""
    cum3 = _log_safe(close) - _log_safe(close.shift(3))
    return _rolling_min(cum3, 10)


def cth_ext_002_min_return_7d(close: pd.Series) -> pd.Series:
    """Minimum 7-day cumulative log-return within trailing 21-day window."""
    cum7 = _log_safe(close) - _log_safe(close.shift(7))
    return _rolling_min(cum7, _TD_MON)


def cth_ext_003_min_return_15d(close: pd.Series) -> pd.Series:
    """Minimum 15-day cumulative log-return within trailing 63-day window."""
    cum15 = _log_safe(close) - _log_safe(close.shift(15))
    return _rolling_min(cum15, _TD_QTR)


def cth_ext_004_min_return_42d(close: pd.Series) -> pd.Series:
    """Minimum 42-day cumulative log-return within trailing 126-day window."""
    cum42 = _log_safe(close) - _log_safe(close.shift(42))
    return _rolling_min(cum42, _TD_HALF)


def cth_ext_005_min_return_5d_pct_rank_126d(close: pd.Series) -> pd.Series:
    """Percentile rank of worst 5-day return within 126-day (half-year) history."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    worst = _rolling_min(cum5, _TD_MON)
    return worst.rolling(_TD_HALF, min_periods=_TD_QTR).rank(pct=True)


def cth_ext_006_min_return_10d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of worst 10-day return within 252-day history."""
    cum10 = _log_safe(close) - _log_safe(close.shift(10))
    worst = _rolling_min(cum10, _TD_MON)
    return worst.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cth_ext_007_min_return_3d_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of worst 3-day return vs 63-day distribution of 3-day returns."""
    cum3  = _log_safe(close) - _log_safe(close.shift(3))
    mn    = _rolling_mean(cum3, _TD_QTR)
    sd    = _rolling_std(cum3, _TD_QTR)
    worst = _rolling_min(cum3, 10)
    return _safe_div(worst - mn, sd)


def cth_ext_008_min_return_7d_zscore_126d(close: pd.Series) -> pd.Series:
    """Z-score of worst 7-day return vs 126-day distribution."""
    cum7  = _log_safe(close) - _log_safe(close.shift(7))
    mn    = _rolling_mean(cum7, _TD_HALF)
    sd    = _rolling_std(cum7, _TD_HALF)
    worst = _rolling_min(cum7, _TD_MON)
    return _safe_div(worst - mn, sd)


def cth_ext_009_min_return_42d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of worst 42-day return vs 252-day distribution."""
    cum42 = _log_safe(close) - _log_safe(close.shift(42))
    mn    = _rolling_mean(cum42, _TD_YEAR)
    sd    = _rolling_std(cum42, _TD_YEAR)
    worst = _rolling_min(cum42, _TD_HALF)
    return _safe_div(worst - mn, sd)


def cth_ext_010_min_return_5d_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of the worst 5-day return."""
    cum5  = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    worst = _rolling_min(cum5, _TD_MON)
    return worst.expanding(min_periods=_TD_QTR).rank(pct=True)


# --- Group B (011-020): Volume-confirmed thrust signatures ---

def cth_ext_011_vol_confirmed_down_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in last 5d where return < 0 AND volume > 252d-avg volume."""
    lr      = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    flag    = ((lr < 0) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def cth_ext_012_vol_confirmed_down_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of volume-confirmed down-days in trailing 21 days."""
    lr      = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    flag    = ((lr < 0) & (volume > avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_ext_013_vol_confirmed_large_down_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of days in last 5d: return < -1.5% AND volume > 1.5x avg (high-conviction thrust)."""
    lr       = _log_ret(close)
    avg_vol  = _rolling_mean(volume, _TD_YEAR)
    flag     = ((lr < -0.015) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def cth_ext_014_vol_confirmed_large_down_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of high-conviction thrust days (return < -1.5%, vol > 1.5x) in 21 days."""
    lr       = _log_ret(close)
    avg_vol  = _rolling_mean(volume, _TD_YEAR)
    flag     = ((lr < -0.015) & (volume > 1.5 * avg_vol)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_ext_015_vol_down_day_frac_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 21-day volume that traded on down-days."""
    lr       = _log_ret(close)
    down_vol = volume.where(lr < 0, 0.0)
    return _safe_div(_rolling_sum(down_vol, _TD_MON), _rolling_sum(volume, _TD_MON))


def cth_ext_016_vol_down_day_frac_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of total 5-day volume that traded on down-days."""
    lr       = _log_ret(close)
    down_vol = volume.where(lr < 0, 0.0)
    return _safe_div(_rolling_sum(down_vol, _TD_WEEK), _rolling_sum(volume, _TD_WEEK))


def cth_ext_017_vol_weighted_neg_return_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted average of negative daily returns over 21 days (selling force)."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    wsum    = _rolling_sum(lr * vol_n, _TD_MON)
    wt      = _rolling_sum(vol_n, _TD_MON)
    return _safe_div(wsum, wt)


def cth_ext_018_vol_surge_down_3d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of 3-day windows where volume > 2x avg AND cumulative return < -3% (panic spike)."""
    cum3    = _log_safe(close) - _log_safe(close.shift(3))
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol3    = _rolling_sum(volume, 3)
    flag    = ((cum3 < -0.03) & (vol3 > 2.0 * avg_vol * 3)).astype(float)
    return _rolling_sum(flag, _TD_MON)


def cth_ext_019_obv_down_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OLS slope of on-balance-volume over 21 days (OBV trend in thrust)."""
    lr  = _log_ret(close)
    sign = np.sign(lr).fillna(0)
    obv  = (sign * volume).cumsum()
    return _linslope(obv, _TD_MON)


def cth_ext_020_vol_zscore_on_down_days_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean z-score of volume on down-days in trailing 21 days (abnormality of selling volume)."""
    lr      = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    sd_vol  = _rolling_std(volume, _TD_YEAR)
    zvol    = _safe_div(volume - avg_vol, sd_vol)
    return zvol.where(lr < 0, np.nan).rolling(_TD_MON, min_periods=1).mean()


# --- Group C (021-030): Multi-day cumulative thrust magnitude ---

def cth_ext_021_cum_loss_clipped_3d(close: pd.Series) -> pd.Series:
    """Cumulative clipped negative 3-day log-return (only losses count, gains = 0)."""
    lr = _log_ret(close).clip(upper=0)
    return _rolling_sum(lr, 3)


def cth_ext_022_cum_loss_clipped_10d(close: pd.Series) -> pd.Series:
    """Cumulative clipped negative 10-day log-return."""
    lr = _log_ret(close).clip(upper=0)
    return _rolling_sum(lr, 10)


def cth_ext_023_cum_loss_clipped_15d(close: pd.Series) -> pd.Series:
    """Cumulative clipped negative 15-day log-return."""
    lr = _log_ret(close).clip(upper=0)
    return _rolling_sum(lr, 15)


def cth_ext_024_cum_loss_clipped_42d(close: pd.Series) -> pd.Series:
    """Cumulative clipped negative 42-day log-return."""
    lr = _log_ret(close).clip(upper=0)
    return _rolling_sum(lr, 42)


def cth_ext_025_cum_loss_3d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 3-day clipped cumulative loss vs 252-day distribution."""
    lr   = _log_ret(close).clip(upper=0)
    cum3 = _rolling_sum(lr, 3)
    mn   = _rolling_mean(cum3, _TD_YEAR)
    sd   = _rolling_std(cum3, _TD_YEAR)
    return _safe_div(cum3 - mn, sd)


def cth_ext_026_cum_loss_10d_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 10-day clipped cumulative loss vs 252-day distribution."""
    lr    = _log_ret(close).clip(upper=0)
    cum10 = _rolling_sum(lr, 10)
    mn    = _rolling_mean(cum10, _TD_YEAR)
    sd    = _rolling_std(cum10, _TD_YEAR)
    return _safe_div(cum10 - mn, sd)


def cth_ext_027_cum_loss_pct_rank_5d_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5-day cumulative loss-only return in 252-day history."""
    lr   = _log_ret(close).clip(upper=0)
    cum5 = _rolling_sum(lr, _TD_WEEK)
    return cum5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cth_ext_028_cum_loss_pct_rank_21d_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21-day cumulative loss-only return in 252-day history."""
    lr    = _log_ret(close).clip(upper=0)
    cum21 = _rolling_sum(lr, _TD_MON)
    return cum21.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cth_ext_029_vol_weighted_cum_loss_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 5-day cumulative loss (losses scaled by relative volume)."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    return _rolling_sum(lr * vol_n, _TD_WEEK)


def cth_ext_030_vol_weighted_cum_loss_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Volume-weighted 21-day cumulative loss."""
    lr      = _log_ret(close).clip(upper=0)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    vol_n   = _safe_div(volume, avg_vol)
    return _rolling_sum(lr * vol_n, _TD_MON)


# --- Group D (031-040): Consecutive new-low streaks ---

def cth_ext_031_consec_new_low_5d(close: pd.Series) -> pd.Series:
    """Consecutive days setting new 5-day closing lows (panic-phase streak)."""
    lo5  = close.rolling(_TD_WEEK, min_periods=1).min().shift(1)
    flag = (close < lo5)
    return _consec_streak(flag)


def cth_ext_032_consec_new_low_21d(close: pd.Series) -> pd.Series:
    """Consecutive days setting new 21-day closing lows."""
    lo21 = close.rolling(_TD_MON, min_periods=1).min().shift(1)
    flag = (close < lo21)
    return _consec_streak(flag)


def cth_ext_033_consec_new_low_63d(close: pd.Series) -> pd.Series:
    """Consecutive days setting new 63-day closing lows."""
    lo63 = close.rolling(_TD_QTR, min_periods=1).min().shift(1)
    flag = (close < lo63)
    return _consec_streak(flag)


def cth_ext_034_consec_new_low_252d(close: pd.Series) -> pd.Series:
    """Consecutive days setting new 252-day closing lows."""
    lo252 = close.rolling(_TD_YEAR, min_periods=1).min().shift(1)
    flag  = (close < lo252)
    return _consec_streak(flag)


def cth_ext_035_new_21d_low_freq_63d(close: pd.Series) -> pd.Series:
    """Count of new-21d-low closes in trailing 63 days (frequency of thrust penetrations)."""
    lo21 = close.rolling(_TD_MON, min_periods=1).min().shift(1)
    flag = (close < lo21).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def cth_ext_036_new_63d_low_freq_252d(close: pd.Series) -> pd.Series:
    """Count of new-63d-low closes in trailing 252 days."""
    lo63 = close.rolling(_TD_QTR, min_periods=1).min().shift(1)
    flag = (close < lo63).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def cth_ext_037_consec_down_days_streak(close: pd.Series) -> pd.Series:
    """Current consecutive down-day streak (each day close < prior close)."""
    lr   = _log_ret(close)
    flag = lr < 0
    return _consec_streak(flag)


def cth_ext_038_max_consec_down_streak_21d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day streak in trailing 21 days."""
    lr   = _log_ret(close)
    cond = (lr < 0).astype(float)
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


def cth_ext_039_max_consec_down_streak_63d(close: pd.Series) -> pd.Series:
    """Maximum consecutive down-day streak in trailing 63 days."""
    lr   = _log_ret(close)
    cond = (lr < 0).astype(float)
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
    return cond.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).apply(_max_run, raw=True)


def cth_ext_040_low_expansion_3d(low: pd.Series) -> pd.Series:
    """Log-ratio of 3-day-ago low to today's low (3-day trough expansion)."""
    return _log_safe(low.shift(3)) - _log_safe(low)


# --- Group E (041-050): Overnight vs intraday decomposition ---

def cth_ext_041_overnight_ret_5d_sum(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day sum of overnight log-returns (close-to-open gap losses)."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    return _rolling_sum(overnight, _TD_WEEK)


def cth_ext_042_intraday_ret_5d_sum(close: pd.Series, open: pd.Series) -> pd.Series:
    """5-day sum of intraday log-returns (open-to-close)."""
    intraday = _log_safe(close) - _log_safe(open)
    return _rolling_sum(intraday, _TD_WEEK)


def cth_ext_043_overnight_ret_21d_sum(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day sum of overnight log-returns (gap component of move)."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    return _rolling_sum(overnight, _TD_MON)


def cth_ext_044_intraday_ret_21d_sum(close: pd.Series, open: pd.Series) -> pd.Series:
    """21-day sum of intraday log-returns (body component)."""
    intraday = _log_safe(close) - _log_safe(open)
    return _rolling_sum(intraday, _TD_MON)


def cth_ext_045_overnight_vs_total_ret_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Fraction of 5-day total loss that is overnight (gap) component."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    total5    = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    over5     = _rolling_sum(overnight, _TD_WEEK)
    return _safe_div(over5, total5.abs() + _EPS)


def cth_ext_046_intraday_neg_count_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days with negative intraday return (close < open) in trailing 5 days."""
    intraday = _log_safe(close) - _log_safe(open)
    return _rolling_sum((intraday < 0).astype(float), _TD_WEEK)


def cth_ext_047_overnight_neg_count_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days with negative overnight return (gap down) in trailing 5 days."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    return _rolling_sum((overnight < 0).astype(float), _TD_WEEK)


def cth_ext_048_overnight_neg_count_21d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of negative overnight (gap-down) sessions in trailing 21 days."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    return _rolling_sum((overnight < 0).astype(float), _TD_MON)


def cth_ext_049_both_overnight_and_intraday_neg_5d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Count of days in 5d where BOTH overnight AND intraday returns are negative."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    intraday  = _log_safe(close) - _log_safe(open)
    flag = ((overnight < 0) & (intraday < 0)).astype(float)
    return _rolling_sum(flag, _TD_WEEK)


def cth_ext_050_overnight_loss_zscore_63d(close: pd.Series, open: pd.Series) -> pd.Series:
    """Z-score of current overnight return vs 63-day overnight return distribution."""
    overnight = _log_safe(open) - _log_safe(close.shift(1))
    mn        = _rolling_mean(overnight, _TD_QTR)
    sd        = _rolling_std(overnight, _TD_QTR)
    return _safe_div(overnight - mn, sd)


# --- Group F (051-060): Intraday range and channel-break patterns ---

def cth_ext_051_atr_5d_vs_63d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 5-day ATR to 63-day ATR (thrust volatility vs quarterly baseline)."""
    atr  = _tr(close, high, low) / close.clip(lower=_EPS)
    r5   = _rolling_mean(atr, _TD_WEEK)
    r63  = _rolling_mean(atr, _TD_QTR)
    return _safe_div(r5, r63)


def cth_ext_052_atr_3d_vs_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of 3-day ATR to 21-day ATR (ultra-short burst relative to monthly range)."""
    atr = _tr(close, high, low) / close.clip(lower=_EPS)
    r3  = _rolling_mean(atr, 3)
    r21 = _rolling_mean(atr, _TD_MON)
    return _safe_div(r3, r21)


def cth_ext_053_atr_norm_10d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """10-day mean ATR normalized by close (intermediate burst window)."""
    atr = _tr(close, high, low)
    return _rolling_mean(atr, 10) / close.clip(lower=_EPS)


def cth_ext_054_atr_expanding_rank(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of 5-day normalized ATR."""
    atr = _tr(close, high, low)
    r5  = _rolling_mean(atr, _TD_WEEK) / close.clip(lower=_EPS)
    return r5.expanding(min_periods=_TD_QTR).rank(pct=True)


def cth_ext_055_range_expansion_3d_vs_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Ratio of mean 3-day (H-L)/C range to mean 21-day (H-L)/C range."""
    rng = (high - low) / close.clip(lower=_EPS)
    r3  = _rolling_mean(rng, 3)
    r21 = _rolling_mean(rng, _TD_MON)
    return _safe_div(r3, r21)


def cth_ext_056_close_below_bollinger_lower_21d(close: pd.Series) -> pd.Series:
    """Depth of close below 21-day Bollinger lower band (2 sigma)."""
    mn = _rolling_mean(close, _TD_MON)
    sd = _rolling_std(close, _TD_MON)
    lower = mn - 2.0 * sd
    return (lower - close).clip(lower=0) / close.clip(lower=_EPS)


def cth_ext_057_close_below_bollinger_lower_63d(close: pd.Series) -> pd.Series:
    """Depth of close below 63-day Bollinger lower band (2 sigma)."""
    mn = _rolling_mean(close, _TD_QTR)
    sd = _rolling_std(close, _TD_QTR)
    lower = mn - 2.0 * sd
    return (lower - close).clip(lower=0) / close.clip(lower=_EPS)


def cth_ext_058_close_below_bollinger_lower_21d_flag(close: pd.Series) -> pd.Series:
    """Binary flag: close is below 21-day Bollinger lower band (2 sigma)."""
    mn    = _rolling_mean(close, _TD_MON)
    sd    = _rolling_std(close, _TD_MON)
    lower = mn - 2.0 * sd
    return (close < lower).astype(float)


def cth_ext_059_days_below_boll_lower_21d_in_63d(close: pd.Series) -> pd.Series:
    """Count of days below 21-day Bollinger lower band in trailing 63 days."""
    mn    = _rolling_mean(close, _TD_MON)
    sd    = _rolling_std(close, _TD_MON)
    lower = mn - 2.0 * sd
    flag  = (close < lower).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def cth_ext_060_high_low_channel_break_freq_21d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of days where low breaks below prior 21-day low in trailing 21 days."""
    prior_lo = low.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    flag     = (low < prior_lo).astype(float)
    return _rolling_sum(flag, _TD_MON)


# --- Group G (061-075): Regime flags and advanced composite scores ---

def cth_ext_061_thrust_regime_flag_5d(close: pd.Series) -> pd.Series:
    """Flag: 5-day return is below -2x its 252-day median absolute deviation."""
    cum5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    med  = _rolling_median(cum5, _TD_YEAR)
    mad  = (cum5 - med).abs().rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    return (cum5 < med - 2.0 * mad).astype(float)


def cth_ext_062_thrust_regime_flag_21d(close: pd.Series) -> pd.Series:
    """Flag: 21-day return is below -2x its 252-day MAD (extreme monthly thrust)."""
    cum21 = _log_safe(close) - _log_safe(close.shift(_TD_MON))
    med   = _rolling_median(cum21, _TD_YEAR)
    mad   = (cum21 - med).abs().rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    return (cum21 < med - 2.0 * mad).astype(float)


def cth_ext_063_vol_regime_surge_flag(volume: pd.Series) -> pd.Series:
    """Flag: today's volume exceeds 252-day median by more than 2x MAD (volume shock)."""
    med = _rolling_median(volume, _TD_YEAR)
    mad = (volume - med).abs().rolling(_TD_YEAR, min_periods=_TD_QTR).median()
    return (volume > med + 2.0 * mad).astype(float)


def cth_ext_064_combined_price_vol_panic_flag(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Flag: 5d return in bottom 5th pct of 252d distribution AND volume in top 5th pct."""
    cum5    = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    r_rank  = cum5.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    v_rank  = volume.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return ((r_rank < 0.05) & (v_rank > 0.95)).astype(float)


def cth_ext_065_panic_score_4factor(close: pd.Series, high: pd.Series, low: pd.Series,
                                     volume: pd.Series) -> pd.Series:
    """4-factor panic score: z(5d ret) + z(vol) + z(ATR/C) + z(down-day frac) in 21d."""
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
    return (z_ret + z_vol + z_atr + z_frac) / 4.0


def cth_ext_066_drawdown_126d_pct_rank_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 126-day drawdown from peak in 252-day history."""
    pk  = _rolling_max(close, _TD_HALF)
    dd  = _log_safe(close) - _log_safe(pk)
    return dd.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def cth_ext_067_drawdown_252d_expanding_rank(close: pd.Series) -> pd.Series:
    """Expanding all-time percentile rank of 252-day drawdown from peak."""
    pk = _rolling_max(close, _TD_YEAR)
    dd = _log_safe(close) - _log_safe(pk)
    return dd.expanding(min_periods=_TD_QTR).rank(pct=True)


def cth_ext_068_tail_density_ratio_21d_vs_126d(close: pd.Series) -> pd.Series:
    """Ratio of 21-day fraction-below-2sigma to 126-day fraction-below-2sigma."""
    lr    = _log_ret(close)
    mn    = _rolling_mean(lr, _TD_YEAR)
    sd    = _rolling_std(lr, _TD_YEAR)
    flag  = (lr < mn - 2.0 * sd).astype(float)
    f21   = _rolling_sum(flag, _TD_MON) / _TD_MON
    f126  = _rolling_sum(flag, _TD_HALF) / _TD_HALF
    return _safe_div(f21, f126 + _EPS)


def cth_ext_069_left_tail_quantile_5pct_63d(close: pd.Series) -> pd.Series:
    """5th-percentile daily return in trailing 63-day window (deep tail threshold)."""
    lr = _log_ret(close)
    return lr.rolling(_TD_QTR, min_periods=max(5, _TD_QTR // 2)).quantile(0.05)


def cth_ext_070_left_tail_quantile_1pct_252d(close: pd.Series) -> pd.Series:
    """1st-percentile daily return in trailing 252-day window (extreme tail threshold)."""
    lr = _log_ret(close)
    return lr.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.01)


def cth_ext_071_vol_spike_and_down_composite_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: sum of (vol_z * |ret|) on down-days only in trailing 5 days."""
    lr      = _log_ret(close)
    avg_vol = _rolling_mean(volume, _TD_YEAR)
    sd_vol  = _rolling_std(volume, _TD_YEAR)
    zvol    = _safe_div(volume - avg_vol, sd_vol)
    signal  = (zvol * lr.abs()).where(lr < 0, 0.0)
    return _rolling_sum(signal, _TD_WEEK)


def cth_ext_072_candle_compression_5d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (H-L)/5d-ATR in trailing 5 days normalized by 21d-ATR (range compression ratio)."""
    rng    = high - low
    atr5   = _rolling_mean(_tr(close, high, low), _TD_WEEK)
    atr21  = _rolling_mean(_tr(close, high, low), _TD_MON)
    comp   = _safe_div(rng, atr5 + _EPS)
    return _rolling_mean(comp, _TD_WEEK) * _safe_div(atr5, atr21 + _EPS)


def cth_ext_073_thrust_zscore_ewm_5d(close: pd.Series) -> pd.Series:
    """EWM-based z-score of 5-day cumulative loss (span=63d) for fast mean-reversion context."""
    cum5 = _log_safe(close) - _log_safe(close.shift(_TD_WEEK))
    mn   = _ewm_mean(cum5, _TD_QTR)
    sd   = cum5.ewm(span=_TD_QTR, min_periods=max(1, _TD_QTR // 2)).std()
    return _safe_div(cum5 - mn, sd)


def cth_ext_074_new_low_depth_126d(close: pd.Series, low: pd.Series) -> pd.Series:
    """How far today's low is below the prior 126-day minimum low (new-low depth semi-annual)."""
    prior_lo = low.shift(1).rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).min()
    return (prior_lo - low).clip(lower=0) / close.clip(lower=_EPS)


def cth_ext_075_combined_thrust_capitulation_score(close: pd.Series, high: pd.Series,
                                                    low: pd.Series, volume: pd.Series) -> pd.Series:
    """Capitulation composite: z(5d_loss) + z(vol_down_frac) + z(atr_norm) + z(new_low_depth_21d).
    All four pillars: price magnitude, volume confirmation, range expansion, low penetration."""
    cum5    = (_log_safe(close) - _log_safe(close.shift(_TD_WEEK))).clip(upper=0)
    z_cum5  = _safe_div(cum5 - _rolling_mean(cum5, _TD_YEAR), _rolling_std(cum5, _TD_YEAR))

    lr      = _log_ret(close)
    dv      = volume.where(lr < 0, 0.0)
    frac_dv = _safe_div(_rolling_sum(dv, _TD_MON), _rolling_sum(volume, _TD_MON))
    z_frac  = _safe_div(frac_dv - _rolling_mean(frac_dv, _TD_YEAR), _rolling_std(frac_dv, _TD_YEAR))

    atr_n   = _tr(close, high, low) / close.clip(lower=_EPS)
    z_atr   = _safe_div(atr_n - _rolling_mean(atr_n, _TD_YEAR), _rolling_std(atr_n, _TD_YEAR))

    prior_lo = low.shift(1).rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).min()
    nld      = (prior_lo - low).clip(lower=0) / close.clip(lower=_EPS)
    z_nld    = _safe_div(nld - _rolling_mean(nld, _TD_YEAR), _rolling_std(nld, _TD_YEAR))

    return (z_cum5 + z_frac + z_atr + z_nld) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITULATION_THRUST_EXTENDED_REGISTRY_001_075 = {
    "cth_ext_001_min_return_3d": {"inputs": ["close"], "func": cth_ext_001_min_return_3d},
    "cth_ext_002_min_return_7d": {"inputs": ["close"], "func": cth_ext_002_min_return_7d},
    "cth_ext_003_min_return_15d": {"inputs": ["close"], "func": cth_ext_003_min_return_15d},
    "cth_ext_004_min_return_42d": {"inputs": ["close"], "func": cth_ext_004_min_return_42d},
    "cth_ext_005_min_return_5d_pct_rank_126d": {"inputs": ["close"], "func": cth_ext_005_min_return_5d_pct_rank_126d},
    "cth_ext_006_min_return_10d_pct_rank_252d": {"inputs": ["close"], "func": cth_ext_006_min_return_10d_pct_rank_252d},
    "cth_ext_007_min_return_3d_zscore_63d": {"inputs": ["close"], "func": cth_ext_007_min_return_3d_zscore_63d},
    "cth_ext_008_min_return_7d_zscore_126d": {"inputs": ["close"], "func": cth_ext_008_min_return_7d_zscore_126d},
    "cth_ext_009_min_return_42d_zscore_252d": {"inputs": ["close"], "func": cth_ext_009_min_return_42d_zscore_252d},
    "cth_ext_010_min_return_5d_expanding_rank": {"inputs": ["close"], "func": cth_ext_010_min_return_5d_expanding_rank},
    "cth_ext_011_vol_confirmed_down_5d": {"inputs": ["close", "volume"], "func": cth_ext_011_vol_confirmed_down_5d},
    "cth_ext_012_vol_confirmed_down_21d": {"inputs": ["close", "volume"], "func": cth_ext_012_vol_confirmed_down_21d},
    "cth_ext_013_vol_confirmed_large_down_5d": {"inputs": ["close", "volume"], "func": cth_ext_013_vol_confirmed_large_down_5d},
    "cth_ext_014_vol_confirmed_large_down_21d": {"inputs": ["close", "volume"], "func": cth_ext_014_vol_confirmed_large_down_21d},
    "cth_ext_015_vol_down_day_frac_21d": {"inputs": ["close", "volume"], "func": cth_ext_015_vol_down_day_frac_21d},
    "cth_ext_016_vol_down_day_frac_5d": {"inputs": ["close", "volume"], "func": cth_ext_016_vol_down_day_frac_5d},
    "cth_ext_017_vol_weighted_neg_return_21d": {"inputs": ["close", "volume"], "func": cth_ext_017_vol_weighted_neg_return_21d},
    "cth_ext_018_vol_surge_down_3d": {"inputs": ["close", "volume"], "func": cth_ext_018_vol_surge_down_3d},
    "cth_ext_019_obv_down_slope_21d": {"inputs": ["close", "volume"], "func": cth_ext_019_obv_down_slope_21d},
    "cth_ext_020_vol_zscore_on_down_days_21d": {"inputs": ["close", "volume"], "func": cth_ext_020_vol_zscore_on_down_days_21d},
    "cth_ext_021_cum_loss_clipped_3d": {"inputs": ["close"], "func": cth_ext_021_cum_loss_clipped_3d},
    "cth_ext_022_cum_loss_clipped_10d": {"inputs": ["close"], "func": cth_ext_022_cum_loss_clipped_10d},
    "cth_ext_023_cum_loss_clipped_15d": {"inputs": ["close"], "func": cth_ext_023_cum_loss_clipped_15d},
    "cth_ext_024_cum_loss_clipped_42d": {"inputs": ["close"], "func": cth_ext_024_cum_loss_clipped_42d},
    "cth_ext_025_cum_loss_3d_zscore_252d": {"inputs": ["close"], "func": cth_ext_025_cum_loss_3d_zscore_252d},
    "cth_ext_026_cum_loss_10d_zscore_252d": {"inputs": ["close"], "func": cth_ext_026_cum_loss_10d_zscore_252d},
    "cth_ext_027_cum_loss_pct_rank_5d_252d": {"inputs": ["close"], "func": cth_ext_027_cum_loss_pct_rank_5d_252d},
    "cth_ext_028_cum_loss_pct_rank_21d_252d": {"inputs": ["close"], "func": cth_ext_028_cum_loss_pct_rank_21d_252d},
    "cth_ext_029_vol_weighted_cum_loss_5d": {"inputs": ["close", "volume"], "func": cth_ext_029_vol_weighted_cum_loss_5d},
    "cth_ext_030_vol_weighted_cum_loss_21d": {"inputs": ["close", "volume"], "func": cth_ext_030_vol_weighted_cum_loss_21d},
    "cth_ext_031_consec_new_low_5d": {"inputs": ["close"], "func": cth_ext_031_consec_new_low_5d},
    "cth_ext_032_consec_new_low_21d": {"inputs": ["close"], "func": cth_ext_032_consec_new_low_21d},
    "cth_ext_033_consec_new_low_63d": {"inputs": ["close"], "func": cth_ext_033_consec_new_low_63d},
    "cth_ext_034_consec_new_low_252d": {"inputs": ["close"], "func": cth_ext_034_consec_new_low_252d},
    "cth_ext_035_new_21d_low_freq_63d": {"inputs": ["close"], "func": cth_ext_035_new_21d_low_freq_63d},
    "cth_ext_036_new_63d_low_freq_252d": {"inputs": ["close"], "func": cth_ext_036_new_63d_low_freq_252d},
    "cth_ext_037_consec_down_days_streak": {"inputs": ["close"], "func": cth_ext_037_consec_down_days_streak},
    "cth_ext_038_max_consec_down_streak_21d": {"inputs": ["close"], "func": cth_ext_038_max_consec_down_streak_21d},
    "cth_ext_039_max_consec_down_streak_63d": {"inputs": ["close"], "func": cth_ext_039_max_consec_down_streak_63d},
    "cth_ext_040_low_expansion_3d": {"inputs": ["low"], "func": cth_ext_040_low_expansion_3d},
    "cth_ext_041_overnight_ret_5d_sum": {"inputs": ["close", "open"], "func": cth_ext_041_overnight_ret_5d_sum},
    "cth_ext_042_intraday_ret_5d_sum": {"inputs": ["close", "open"], "func": cth_ext_042_intraday_ret_5d_sum},
    "cth_ext_043_overnight_ret_21d_sum": {"inputs": ["close", "open"], "func": cth_ext_043_overnight_ret_21d_sum},
    "cth_ext_044_intraday_ret_21d_sum": {"inputs": ["close", "open"], "func": cth_ext_044_intraday_ret_21d_sum},
    "cth_ext_045_overnight_vs_total_ret_5d": {"inputs": ["close", "open"], "func": cth_ext_045_overnight_vs_total_ret_5d},
    "cth_ext_046_intraday_neg_count_5d": {"inputs": ["close", "open"], "func": cth_ext_046_intraday_neg_count_5d},
    "cth_ext_047_overnight_neg_count_5d": {"inputs": ["close", "open"], "func": cth_ext_047_overnight_neg_count_5d},
    "cth_ext_048_overnight_neg_count_21d": {"inputs": ["close", "open"], "func": cth_ext_048_overnight_neg_count_21d},
    "cth_ext_049_both_overnight_and_intraday_neg_5d": {"inputs": ["close", "open"], "func": cth_ext_049_both_overnight_and_intraday_neg_5d},
    "cth_ext_050_overnight_loss_zscore_63d": {"inputs": ["close", "open"], "func": cth_ext_050_overnight_loss_zscore_63d},
    "cth_ext_051_atr_5d_vs_63d": {"inputs": ["close", "high", "low"], "func": cth_ext_051_atr_5d_vs_63d},
    "cth_ext_052_atr_3d_vs_21d": {"inputs": ["close", "high", "low"], "func": cth_ext_052_atr_3d_vs_21d},
    "cth_ext_053_atr_norm_10d": {"inputs": ["close", "high", "low"], "func": cth_ext_053_atr_norm_10d},
    "cth_ext_054_atr_expanding_rank": {"inputs": ["close", "high", "low"], "func": cth_ext_054_atr_expanding_rank},
    "cth_ext_055_range_expansion_3d_vs_21d": {"inputs": ["close", "high", "low"], "func": cth_ext_055_range_expansion_3d_vs_21d},
    "cth_ext_056_close_below_bollinger_lower_21d": {"inputs": ["close"], "func": cth_ext_056_close_below_bollinger_lower_21d},
    "cth_ext_057_close_below_bollinger_lower_63d": {"inputs": ["close"], "func": cth_ext_057_close_below_bollinger_lower_63d},
    "cth_ext_058_close_below_bollinger_lower_21d_flag": {"inputs": ["close"], "func": cth_ext_058_close_below_bollinger_lower_21d_flag},
    "cth_ext_059_days_below_boll_lower_21d_in_63d": {"inputs": ["close"], "func": cth_ext_059_days_below_boll_lower_21d_in_63d},
    "cth_ext_060_high_low_channel_break_freq_21d": {"inputs": ["close", "high", "low"], "func": cth_ext_060_high_low_channel_break_freq_21d},
    "cth_ext_061_thrust_regime_flag_5d": {"inputs": ["close"], "func": cth_ext_061_thrust_regime_flag_5d},
    "cth_ext_062_thrust_regime_flag_21d": {"inputs": ["close"], "func": cth_ext_062_thrust_regime_flag_21d},
    "cth_ext_063_vol_regime_surge_flag": {"inputs": ["volume"], "func": cth_ext_063_vol_regime_surge_flag},
    "cth_ext_064_combined_price_vol_panic_flag": {"inputs": ["close", "volume"], "func": cth_ext_064_combined_price_vol_panic_flag},
    "cth_ext_065_panic_score_4factor": {"inputs": ["close", "high", "low", "volume"], "func": cth_ext_065_panic_score_4factor},
    "cth_ext_066_drawdown_126d_pct_rank_252d": {"inputs": ["close"], "func": cth_ext_066_drawdown_126d_pct_rank_252d},
    "cth_ext_067_drawdown_252d_expanding_rank": {"inputs": ["close"], "func": cth_ext_067_drawdown_252d_expanding_rank},
    "cth_ext_068_tail_density_ratio_21d_vs_126d": {"inputs": ["close"], "func": cth_ext_068_tail_density_ratio_21d_vs_126d},
    "cth_ext_069_left_tail_quantile_5pct_63d": {"inputs": ["close"], "func": cth_ext_069_left_tail_quantile_5pct_63d},
    "cth_ext_070_left_tail_quantile_1pct_252d": {"inputs": ["close"], "func": cth_ext_070_left_tail_quantile_1pct_252d},
    "cth_ext_071_vol_spike_and_down_composite_5d": {"inputs": ["close", "volume"], "func": cth_ext_071_vol_spike_and_down_composite_5d},
    "cth_ext_072_candle_compression_5d": {"inputs": ["close", "high", "low"], "func": cth_ext_072_candle_compression_5d},
    "cth_ext_073_thrust_zscore_ewm_5d": {"inputs": ["close"], "func": cth_ext_073_thrust_zscore_ewm_5d},
    "cth_ext_074_new_low_depth_126d": {"inputs": ["close", "low"], "func": cth_ext_074_new_low_depth_126d},
    "cth_ext_075_combined_thrust_capitulation_score": {"inputs": ["close", "high", "low", "volume"], "func": cth_ext_075_combined_thrust_capitulation_score},
}
