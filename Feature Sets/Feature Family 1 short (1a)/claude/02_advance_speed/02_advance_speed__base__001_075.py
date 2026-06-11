"""advance_speed base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Hypothesis: velocity, acceleration character, and burst dynamics of the upward
advance into the peak distinguish stocks that will get stuck at -80% from those
that won't. 75 distinct hypotheses (continued in __base__076_150.py for 150).
Inputs: SEP OHLCV only. PIT-clean: right-anchored rolling, explicit min_periods,
no centered windows, no .shift(-N).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


# ============================================================
#                    FEATURES 001-075
# ============================================================

def f02_advs_001_compound_log_speed_from_252d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close / 252d-min(low)) per bar since that min — trough-anchored velocity."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0)


def f02_advs_002_compound_log_speed_from_63d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close / 63d-min(low)) per bar since that min."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(QDAYS, min_periods=MDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0)


def f02_advs_003_compound_log_speed_from_1260d_low(close: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close / 1260d-min(low)) per bar since that min — secular trough velocity."""
    rmin = low.rolling(1260, min_periods=YDAYS).min()
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(1260, min_periods=YDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0)


def f02_advs_004_ratio_compound_speed_252d_vs_1260d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Annual vs secular trough-to-now speed — recent acceleration over long-cycle base."""
    r252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    r1260 = low.rolling(1260, min_periods=YDAYS).min()
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    d252 = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    d1260 = low.rolling(1260, min_periods=YDAYS).apply(_dsm, raw=True)
    sp_y = _safe_div(_safe_log(close) - _safe_log(r252), d252 + 1.0)
    sp_5y = _safe_div(_safe_log(close) - _safe_log(r1260), d1260 + 1.0)
    return _safe_div(sp_y, sp_5y)


def f02_advs_005_compound_log_speed_zscore_in_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Z-score of the 252d trough-to-now speed vs its own 252d history."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    sp = _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0)
    return _rolling_zscore(sp, YDAYS)


def f02_advs_006_compound_speed_excess_vs_baseline_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Trough-anchored pace minus its own 252d median — excess pace vs typical."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    sp = _safe_div(_safe_log(close) - _safe_log(rmin), days + 1.0)
    return sp - sp.rolling(YDAYS, min_periods=QDAYS).median()


def f02_advs_007_log_close_to_rolling_252d_vwap(close: pd.Series, volume: pd.Series, low: pd.Series) -> pd.Series:
    """Log(close / 252d-VWAP) per bar — VWAP-anchored advance speed."""
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vwap = _safe_div(pv, vv)
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div(_safe_log(close) - _safe_log(vwap), days + 1.0)


def f02_advs_008_compound_speed_in_atr_units_from_252d_low(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """(close - 252d-min(low)) / ATR21 per bar — speed scaled by typical move."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div((close - rmin) / atr.replace(0, np.nan), days + 1.0)


def f02_advs_009_compound_speed_in_atr_units_from_63d_low(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """Quarterly-trough version of f02_advs_008."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(QDAYS, min_periods=MDAYS).apply(_dsm, raw=True)
    return _safe_div((close - rmin) / atr.replace(0, np.nan), days + 1.0)


def f02_advs_010_recovery_speed_from_252d_low(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Share of 252d range traversed per bar since 252d low — pace of recovery."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rng = (rmax - rmin).replace(0, np.nan)
    def _dsm(w):
        return (len(w) - 1) - int(np.argmin(w))
    days = low.rolling(YDAYS, min_periods=QDAYS).apply(_dsm, raw=True)
    return _safe_div((close - rmin) / rng, days + 1.0)


def f02_advs_011_exponential_velocity_ema_21d(close: pd.Series) -> pd.Series:
    """EMA(span=21) of daily log returns — exponentially-weighted pace estimate."""
    r = _safe_log(close).diff()
    return r.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean()


def f02_advs_012_log_arc_height_above_min_low_252d(close: pd.Series, low: pd.Series) -> pd.Series:
    """Sum over 252d of log(close) - log(252d-min(low)) — area of the advance arc."""
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    height = (_safe_log(close) - _safe_log(rmin)).clip(lower=0)
    return height.rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_013_velocity_recent_minus_baseline_21d_in_252d(close: pd.Series) -> pd.Series:
    """21d daily log-return mean minus baseline daily mean over prior 252d."""
    r = _safe_log(close).diff()
    recent = r.rolling(MDAYS, min_periods=WDAYS).mean()
    base = r.rolling(YDAYS, min_periods=QDAYS).mean()
    return recent - base


def f02_advs_014_velocity_dispersion_iqr_252d(close: pd.Series) -> pd.Series:
    """Inter-quartile range of daily log returns over 252d — dispersion of pace."""
    r = _safe_log(close).diff()
    q75 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q25 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return q75 - q25


def f02_advs_015_velocity_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of daily log returns over 252d — return-distribution asymmetry."""
    r = _safe_log(close).diff()
    return r.rolling(YDAYS, min_periods=QDAYS).skew()


def f02_advs_016_velocity_kurt_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of daily log returns over 252d — tail thickness."""
    r = _safe_log(close).diff()
    return r.rolling(YDAYS, min_periods=QDAYS).kurt()


def f02_advs_017_velocity_p95_minus_p50_252d(close: pd.Series) -> pd.Series:
    """Right-tail dispersion of daily log returns over 252d."""
    r = _safe_log(close).diff()
    q95 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    return q95 - q50


def f02_advs_018_velocity_p50_minus_p5_252d(close: pd.Series) -> pd.Series:
    """Left-tail dispersion of daily log returns over 252d."""
    r = _safe_log(close).diff()
    q50 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.50)
    q05 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    return q50 - q05


def f02_advs_019_velocity_pct_rank_5d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 5d log return vs its 252d distribution."""
    r5 = _safe_log(close).diff(WDAYS)
    return r5.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f02_advs_020_velocity_pct_rank_21d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 21d log return vs its 252d distribution."""
    r21 = _safe_log(close).diff(MDAYS)
    return r21.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f02_advs_021_velocity_pct_rank_63d_in_252d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d log return vs its 252d distribution."""
    r63 = _safe_log(close).diff(QDAYS)
    return r63.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f02_advs_022_velocity_burst_above_2sd_count_252d(close: pd.Series) -> pd.Series:
    """Days in last 252 with |z| > 2 on the upside in daily log returns."""
    r = _safe_log(close).diff()
    z = _rolling_zscore(r, YDAYS)
    return (z > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_023_velocity_burst_below_2sd_count_252d(close: pd.Series) -> pd.Series:
    """Days in last 252 with z < -2 on daily log returns (downside bursts during advance)."""
    r = _safe_log(close).diff()
    z = _rolling_zscore(r, YDAYS)
    return (z < -2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_024_velocity_runs_above_zero_max_252d(close: pd.Series) -> pd.Series:
    """Longest streak of positive daily log returns within last 252 bars."""
    pos = (_safe_log(close).diff() > 0).astype(int)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_025_velocity_mad_252d(close: pd.Series) -> pd.Series:
    """Mean absolute daily log return over 252d — path roughness."""
    r = _safe_log(close).diff().abs()
    return r.rolling(YDAYS, min_periods=QDAYS).mean()


def f02_advs_026_acceleration_max_252d(close: pd.Series) -> pd.Series:
    """Max single-bar 2nd derivative of log price over last 252 bars."""
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_027_acceleration_min_252d(close: pd.Series) -> pd.Series:
    """Min single-bar 2nd derivative of log price over last 252 bars."""
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).min()


def f02_advs_028_acceleration_range_252d(close: pd.Series) -> pd.Series:
    """Max-minus-min 2nd derivative of log price over 252 bars — accel swing range."""
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).max() - a.rolling(YDAYS, min_periods=QDAYS).min()


def f02_advs_029_acceleration_sign_changes_count_63d(close: pd.Series) -> pd.Series:
    """Count of accel sign flips over 63d — regime jitteriness."""
    a = _safe_log(close).diff().diff()
    flip = (np.sign(a) != np.sign(a.shift(1))).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum()


def f02_advs_030_acceleration_positive_run_max_252d(close: pd.Series) -> pd.Series:
    """Longest streak of positive accel within 252 bars."""
    pos = (_safe_log(close).diff().diff() > 0).astype(int)
    grp = (pos == 0).cumsum()
    streak = pos.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_031_acceleration_negative_run_max_252d(close: pd.Series) -> pd.Series:
    """Longest streak of negative accel within 252 bars."""
    neg = (_safe_log(close).diff().diff() < 0).astype(int)
    grp = (neg == 0).cumsum()
    streak = neg.groupby(grp).cumsum()
    return streak.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_032_terminal_acceleration_21d_zscore_in_252d(close: pd.Series) -> pd.Series:
    """Z-score of last-21d mean acceleration vs 252d distribution."""
    a = _safe_log(close).diff().diff()
    mr = a.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(mr, YDAYS)


def f02_advs_033_acceleration_dispersion_iqr_252d(close: pd.Series) -> pd.Series:
    """IQR of acceleration over 252d."""
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)


def f02_advs_034_acceleration_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of acceleration over 252d."""
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).skew()


def f02_advs_035_acceleration_kurt_252d(close: pd.Series) -> pd.Series:
    """Excess kurtosis of acceleration over 252d."""
    a = _safe_log(close).diff().diff()
    return a.rolling(YDAYS, min_periods=QDAYS).kurt()


def f02_advs_036_acceleration_pct_rank_recent_5d_in_252d(close: pd.Series) -> pd.Series:
    """Mean accel last 5d, percentile-ranked vs 252d distribution of 5d-mean accel."""
    a = _safe_log(close).diff().diff()
    m5 = a.rolling(WDAYS, min_periods=2).mean()
    return m5.rolling(YDAYS, min_periods=QDAYS).rank(pct=True)


def f02_advs_037_acceleration_above_p95_count_63d(close: pd.Series) -> pd.Series:
    """Days in last 63 where accel exceeded its 252d 95th percentile."""
    a = _safe_log(close).diff().diff()
    p95 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    return (a > p95).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f02_advs_038_acceleration_autocorr_lag1_63d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of acceleration over 63d."""
    a = _safe_log(close).diff().diff()
    def _ac(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        x, y = w[:-1], w[1:]
        if x.std() == 0 or y.std() == 0:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    return a.rolling(QDAYS, min_periods=MDAYS).apply(_ac, raw=True)


def f02_advs_039_acceleration_autocorr_lag5_252d(close: pd.Series) -> pd.Series:
    """Lag-5 autocorrelation of acceleration over 252d."""
    a = _safe_log(close).diff().diff()
    def _ac(w):
        if np.isnan(w).any() or len(w) < 11:
            return np.nan
        x, y = w[:-5], w[5:]
        if x.std() == 0 or y.std() == 0:
            return np.nan
        return float(np.corrcoef(x, y)[0, 1])
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_ac, raw=True)


def f02_advs_040_acceleration_velocity_corr_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr(acceleration, velocity) — pro-cyclical thrust."""
    v = _safe_log(close).diff()
    a = v.diff()
    return v.rolling(QDAYS, min_periods=MDAYS).corr(a)


def f02_advs_041_acceleration_vol_corr_63d(close: pd.Series) -> pd.Series:
    """Rolling 63d corr(acceleration, |velocity|) — thrust co-moves with magnitude."""
    v = _safe_log(close).diff()
    a = v.diff()
    return a.rolling(QDAYS, min_periods=MDAYS).corr(v.abs())


def f02_advs_042_acceleration_zscore_p95_252d(close: pd.Series) -> pd.Series:
    """95th percentile of the daily accel z-score over 252d."""
    a = _safe_log(close).diff().diff()
    z = _rolling_zscore(a, YDAYS)
    return z.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)


def f02_advs_043_acceleration_dropoff_5d_vs_21d(close: pd.Series) -> pd.Series:
    """Mean accel last 5d minus mean accel last 21d — late-phase fade or surge."""
    a = _safe_log(close).diff().diff()
    return a.rolling(WDAYS, min_periods=2).mean() - a.rolling(MDAYS, min_periods=WDAYS).mean()


def f02_advs_044_pre_peak_acceleration_buildup_63d(close: pd.Series) -> pd.Series:
    """Slope of acceleration over 63d — is the curvature itself growing?"""
    a = _safe_log(close).diff().diff()
    return _rolling_slope(a, QDAYS)


def f02_advs_045_acceleration_terminal_thrust_5d_zscore(close: pd.Series) -> pd.Series:
    """Z-score of last-5d mean acceleration vs 252d distribution."""
    a = _safe_log(close).diff().diff()
    m5 = a.rolling(WDAYS, min_periods=2).mean()
    return _rolling_zscore(m5, YDAYS)


def f02_advs_046_max_1d_log_return_252d(close: pd.Series) -> pd.Series:
    """Largest single-day log return inside the last 252 bars."""
    r = _safe_log(close).diff()
    return r.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_047_min_1d_log_return_252d(close: pd.Series) -> pd.Series:
    """Worst single-day log return inside the last 252 bars."""
    r = _safe_log(close).diff()
    return r.rolling(YDAYS, min_periods=QDAYS).min()


def f02_advs_048_max_1d_log_return_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of the biggest 1d log return in the last 252 vs its history."""
    r = _safe_log(close).diff()
    mx = r.rolling(YDAYS, min_periods=QDAYS).max()
    return _rolling_zscore(mx, YDAYS)


def f02_advs_049_count_outsize_up_days_z_gt_3_252d(close: pd.Series) -> pd.Series:
    """Days in 252 with daily-return z > 3 — extreme upside surprises."""
    r = _safe_log(close).diff()
    z = _rolling_zscore(r, YDAYS)
    return (z > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_050_count_outsize_down_days_z_lt_neg3_252d(close: pd.Series) -> pd.Series:
    """Days in 252 with z < -3 — extreme downside (rare during advance)."""
    r = _safe_log(close).diff()
    z = _rolling_zscore(r, YDAYS)
    return (z < -3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_051_mean_top10_log_returns_252d(close: pd.Series) -> pd.Series:
    """Mean of the 10 largest daily log returns in last 252."""
    r = _safe_log(close).diff()
    def _t10(w):
        if np.isnan(w).all():
            return np.nan
        ww = w[~np.isnan(w)]
        if len(ww) < 10:
            return np.nan
        return float(np.sort(ww)[-10:].mean())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_t10, raw=True)


def f02_advs_052_mean_bottom10_log_returns_252d(close: pd.Series) -> pd.Series:
    """Mean of the 10 smallest daily log returns in last 252."""
    r = _safe_log(close).diff()
    def _b10(w):
        if np.isnan(w).all():
            return np.nan
        ww = w[~np.isnan(w)]
        if len(ww) < 10:
            return np.nan
        return float(np.sort(ww)[:10].mean())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_b10, raw=True)


def f02_advs_053_ratio_top10_to_bottom10_returns_252d(close: pd.Series) -> pd.Series:
    """Mean(top10) / |mean(bottom10)| — upside-vs-downside extreme asymmetry."""
    r = _safe_log(close).diff()
    def _t10(w):
        ww = w[~np.isnan(w)]
        return float(np.sort(ww)[-10:].mean()) if len(ww) >= 10 else np.nan
    def _b10(w):
        ww = w[~np.isnan(w)]
        return float(np.sort(ww)[:10].mean()) if len(ww) >= 10 else np.nan
    top = r.rolling(YDAYS, min_periods=QDAYS).apply(_t10, raw=True)
    bot = r.rolling(YDAYS, min_periods=QDAYS).apply(_b10, raw=True)
    return _safe_div(top, bot.abs())


def f02_advs_054_share_of_252d_log_gain_from_top10_days(close: pd.Series) -> pd.Series:
    """Sum of top-10 daily log returns / 252d log return — concentration of advance."""
    r = _safe_log(close).diff()
    def _t10s(w):
        ww = w[~np.isnan(w)]
        return float(np.sort(ww)[-10:].sum()) if len(ww) >= 10 else np.nan
    top_sum = r.rolling(YDAYS, min_periods=QDAYS).apply(_t10s, raw=True)
    total = r.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(top_sum, total)


def f02_advs_055_share_of_252d_log_gain_from_top5_days(close: pd.Series) -> pd.Series:
    """Sum of top-5 daily log returns / 252d log return."""
    r = _safe_log(close).diff()
    def _t5s(w):
        ww = w[~np.isnan(w)]
        return float(np.sort(ww)[-5:].sum()) if len(ww) >= 5 else np.nan
    top_sum = r.rolling(YDAYS, min_periods=QDAYS).apply(_t5s, raw=True)
    total = r.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(top_sum, total)


def f02_advs_056_days_above_3pct_log_return_252d(close: pd.Series) -> pd.Series:
    """Count of days in 252 with log return > 0.03."""
    r = _safe_log(close).diff()
    return (r > 0.03).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_057_days_below_neg3pct_log_return_252d(close: pd.Series) -> pd.Series:
    """Count of days in 252 with log return < -0.03 — bad-day count during the run-up."""
    r = _safe_log(close).diff()
    return (r < -0.03).astype(float).rolling(YDAYS, min_periods=QDAYS).sum()


def f02_advs_058_max_3d_log_return_252d(close: pd.Series) -> pd.Series:
    """Largest rolling 3-day log return inside last 252 bars."""
    r3 = _safe_log(close).diff(3)
    return r3.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_059_max_5d_log_return_252d(close: pd.Series) -> pd.Series:
    """Largest rolling 5-day log return inside last 252 bars."""
    r5 = _safe_log(close).diff(WDAYS)
    return r5.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_060_max_10d_log_return_252d(close: pd.Series) -> pd.Series:
    """Largest rolling 10-day log return inside last 252 bars."""
    r10 = _safe_log(close).diff(10)
    return r10.rolling(YDAYS, min_periods=QDAYS).max()


def f02_advs_061_velocity_volume_corr_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 63d corr(daily log return, log volume) — price–volume confirmation."""
    r = _safe_log(close).diff()
    lv = _safe_log(volume)
    return r.rolling(QDAYS, min_periods=MDAYS).corr(lv)


def f02_advs_062_velocity_volume_corr_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d corr(daily log return, log volume)."""
    r = _safe_log(close).diff()
    lv = _safe_log(volume)
    return r.rolling(YDAYS, min_periods=QDAYS).corr(lv)


def f02_advs_063_velocity_per_log_volume_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d log return divided by 21d sum of log volume — return per unit log-volume."""
    r21 = _safe_log(close).diff(MDAYS)
    cv = _safe_log(volume).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(r21, cv)


def f02_advs_064_velocity_per_log_volume_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d log return divided by 63d sum of log volume."""
    r63 = _safe_log(close).diff(QDAYS)
    cv = _safe_log(volume).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(r63, cv)


def f02_advs_065_fractal_efficiency_21d(close: pd.Series) -> pd.Series:
    """|net 21d log move| / sum |daily log returns| over 21d — path directness."""
    lp = _safe_log(close)
    net = (lp - lp.shift(MDAYS)).abs()
    path = lp.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(net, path)


def f02_advs_066_fractal_efficiency_63d(close: pd.Series) -> pd.Series:
    """|net 63d log move| / 63d sum |daily log returns|."""
    lp = _safe_log(close)
    net = (lp - lp.shift(QDAYS)).abs()
    path = lp.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net, path)


def f02_advs_067_fractal_efficiency_252d(close: pd.Series) -> pd.Series:
    """|net 252d log move| / 252d sum |daily log returns|."""
    lp = _safe_log(close)
    net = (lp - lp.shift(YDAYS)).abs()
    path = lp.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net, path)


def f02_advs_068_efficiency_ratio_21d(close: pd.Series) -> pd.Series:
    """Kaufman ER over 21d — signed net log change / sum |1d log change|."""
    lp = _safe_log(close)
    net = lp - lp.shift(MDAYS)
    path = lp.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(net, path)


def f02_advs_069_efficiency_ratio_63d(close: pd.Series) -> pd.Series:
    """Kaufman ER over 63d."""
    lp = _safe_log(close)
    net = lp - lp.shift(QDAYS)
    path = lp.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net, path)


def f02_advs_070_efficiency_ratio_change_21d_vs_63d(close: pd.Series) -> pd.Series:
    """ER21 - ER63 — short-vs-medium directional efficiency shift."""
    lp = _safe_log(close)
    net21 = lp - lp.shift(MDAYS)
    path21 = lp.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    net63 = lp - lp.shift(QDAYS)
    path63 = lp.diff().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(net21, path21) - _safe_div(net63, path63)


def f02_advs_071_kaufman_efficiency_252d(close: pd.Series) -> pd.Series:
    """Kaufman ER over 252d."""
    lp = _safe_log(close)
    net = lp - lp.shift(YDAYS)
    path = lp.diff().abs().rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(net, path)


def f02_advs_072_advance_path_smoothness_63d(close: pd.Series) -> pd.Series:
    """1 / (1 + cv of daily log returns over 63d) — higher = smoother advance."""
    r = _safe_log(close).diff()
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    m = r.rolling(QDAYS, min_periods=MDAYS).mean().abs()
    cv = sd / m.replace(0, np.nan)
    return _safe_div(pd.Series(1.0, index=close.index), 1.0 + cv)


def f02_advs_073_advance_path_smoothness_252d(close: pd.Series) -> pd.Series:
    """1 / (1 + cv of daily log returns over 252d) — longer-horizon smoothness."""
    r = _safe_log(close).diff()
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    m = r.rolling(YDAYS, min_periods=QDAYS).mean().abs()
    cv = sd / m.replace(0, np.nan)
    return _safe_div(pd.Series(1.0, index=close.index), 1.0 + cv)


def f02_advs_074_log_return_per_atr_252d(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """252d log return divided by current ATR21 — net move in ATR-equivalent units."""
    r = _safe_log(close).diff(YDAYS)
    atr = _atr(high, low, close, MDAYS)
    return _safe_div(r * close, atr)


def f02_advs_075_close_distance_per_atr_from_63d_low(close: pd.Series, low: pd.Series, high: pd.Series) -> pd.Series:
    """(close - 63d-min(low)) / ATR21 — quarterly trough extension in vol units."""
    rmin = low.rolling(QDAYS, min_periods=MDAYS).min()
    atr = _atr(high, low, close, MDAYS)
    return (close - rmin) / atr.replace(0, np.nan)


# ============================================================
#                        REGISTRY
# ============================================================

ADVANCE_SPEED_BASE_REGISTRY_001_075 = {
    "f02_advs_001_compound_log_speed_from_252d_low": {"inputs": ["close", "low"], "func": f02_advs_001_compound_log_speed_from_252d_low},
    "f02_advs_002_compound_log_speed_from_63d_low": {"inputs": ["close", "low"], "func": f02_advs_002_compound_log_speed_from_63d_low},
    "f02_advs_003_compound_log_speed_from_1260d_low": {"inputs": ["close", "low"], "func": f02_advs_003_compound_log_speed_from_1260d_low},
    "f02_advs_004_ratio_compound_speed_252d_vs_1260d": {"inputs": ["close", "low"], "func": f02_advs_004_ratio_compound_speed_252d_vs_1260d},
    "f02_advs_005_compound_log_speed_zscore_in_252d": {"inputs": ["close", "low"], "func": f02_advs_005_compound_log_speed_zscore_in_252d},
    "f02_advs_006_compound_speed_excess_vs_baseline_252d": {"inputs": ["close", "low"], "func": f02_advs_006_compound_speed_excess_vs_baseline_252d},
    "f02_advs_007_log_close_to_rolling_252d_vwap": {"inputs": ["close", "volume", "low"], "func": f02_advs_007_log_close_to_rolling_252d_vwap},
    "f02_advs_008_compound_speed_in_atr_units_from_252d_low": {"inputs": ["close", "low", "high"], "func": f02_advs_008_compound_speed_in_atr_units_from_252d_low},
    "f02_advs_009_compound_speed_in_atr_units_from_63d_low": {"inputs": ["close", "low", "high"], "func": f02_advs_009_compound_speed_in_atr_units_from_63d_low},
    "f02_advs_010_recovery_speed_from_252d_low": {"inputs": ["close", "high", "low"], "func": f02_advs_010_recovery_speed_from_252d_low},
    "f02_advs_011_exponential_velocity_ema_21d": {"inputs": ["close"], "func": f02_advs_011_exponential_velocity_ema_21d},
    "f02_advs_012_log_arc_height_above_min_low_252d": {"inputs": ["close", "low"], "func": f02_advs_012_log_arc_height_above_min_low_252d},
    "f02_advs_013_velocity_recent_minus_baseline_21d_in_252d": {"inputs": ["close"], "func": f02_advs_013_velocity_recent_minus_baseline_21d_in_252d},
    "f02_advs_014_velocity_dispersion_iqr_252d": {"inputs": ["close"], "func": f02_advs_014_velocity_dispersion_iqr_252d},
    "f02_advs_015_velocity_skew_252d": {"inputs": ["close"], "func": f02_advs_015_velocity_skew_252d},
    "f02_advs_016_velocity_kurt_252d": {"inputs": ["close"], "func": f02_advs_016_velocity_kurt_252d},
    "f02_advs_017_velocity_p95_minus_p50_252d": {"inputs": ["close"], "func": f02_advs_017_velocity_p95_minus_p50_252d},
    "f02_advs_018_velocity_p50_minus_p5_252d": {"inputs": ["close"], "func": f02_advs_018_velocity_p50_minus_p5_252d},
    "f02_advs_019_velocity_pct_rank_5d_in_252d": {"inputs": ["close"], "func": f02_advs_019_velocity_pct_rank_5d_in_252d},
    "f02_advs_020_velocity_pct_rank_21d_in_252d": {"inputs": ["close"], "func": f02_advs_020_velocity_pct_rank_21d_in_252d},
    "f02_advs_021_velocity_pct_rank_63d_in_252d": {"inputs": ["close"], "func": f02_advs_021_velocity_pct_rank_63d_in_252d},
    "f02_advs_022_velocity_burst_above_2sd_count_252d": {"inputs": ["close"], "func": f02_advs_022_velocity_burst_above_2sd_count_252d},
    "f02_advs_023_velocity_burst_below_2sd_count_252d": {"inputs": ["close"], "func": f02_advs_023_velocity_burst_below_2sd_count_252d},
    "f02_advs_024_velocity_runs_above_zero_max_252d": {"inputs": ["close"], "func": f02_advs_024_velocity_runs_above_zero_max_252d},
    "f02_advs_025_velocity_mad_252d": {"inputs": ["close"], "func": f02_advs_025_velocity_mad_252d},
    "f02_advs_026_acceleration_max_252d": {"inputs": ["close"], "func": f02_advs_026_acceleration_max_252d},
    "f02_advs_027_acceleration_min_252d": {"inputs": ["close"], "func": f02_advs_027_acceleration_min_252d},
    "f02_advs_028_acceleration_range_252d": {"inputs": ["close"], "func": f02_advs_028_acceleration_range_252d},
    "f02_advs_029_acceleration_sign_changes_count_63d": {"inputs": ["close"], "func": f02_advs_029_acceleration_sign_changes_count_63d},
    "f02_advs_030_acceleration_positive_run_max_252d": {"inputs": ["close"], "func": f02_advs_030_acceleration_positive_run_max_252d},
    "f02_advs_031_acceleration_negative_run_max_252d": {"inputs": ["close"], "func": f02_advs_031_acceleration_negative_run_max_252d},
    "f02_advs_032_terminal_acceleration_21d_zscore_in_252d": {"inputs": ["close"], "func": f02_advs_032_terminal_acceleration_21d_zscore_in_252d},
    "f02_advs_033_acceleration_dispersion_iqr_252d": {"inputs": ["close"], "func": f02_advs_033_acceleration_dispersion_iqr_252d},
    "f02_advs_034_acceleration_skew_252d": {"inputs": ["close"], "func": f02_advs_034_acceleration_skew_252d},
    "f02_advs_035_acceleration_kurt_252d": {"inputs": ["close"], "func": f02_advs_035_acceleration_kurt_252d},
    "f02_advs_036_acceleration_pct_rank_recent_5d_in_252d": {"inputs": ["close"], "func": f02_advs_036_acceleration_pct_rank_recent_5d_in_252d},
    "f02_advs_037_acceleration_above_p95_count_63d": {"inputs": ["close"], "func": f02_advs_037_acceleration_above_p95_count_63d},
    "f02_advs_038_acceleration_autocorr_lag1_63d": {"inputs": ["close"], "func": f02_advs_038_acceleration_autocorr_lag1_63d},
    "f02_advs_039_acceleration_autocorr_lag5_252d": {"inputs": ["close"], "func": f02_advs_039_acceleration_autocorr_lag5_252d},
    "f02_advs_040_acceleration_velocity_corr_63d": {"inputs": ["close"], "func": f02_advs_040_acceleration_velocity_corr_63d},
    "f02_advs_041_acceleration_vol_corr_63d": {"inputs": ["close"], "func": f02_advs_041_acceleration_vol_corr_63d},
    "f02_advs_042_acceleration_zscore_p95_252d": {"inputs": ["close"], "func": f02_advs_042_acceleration_zscore_p95_252d},
    "f02_advs_043_acceleration_dropoff_5d_vs_21d": {"inputs": ["close"], "func": f02_advs_043_acceleration_dropoff_5d_vs_21d},
    "f02_advs_044_pre_peak_acceleration_buildup_63d": {"inputs": ["close"], "func": f02_advs_044_pre_peak_acceleration_buildup_63d},
    "f02_advs_045_acceleration_terminal_thrust_5d_zscore": {"inputs": ["close"], "func": f02_advs_045_acceleration_terminal_thrust_5d_zscore},
    "f02_advs_046_max_1d_log_return_252d": {"inputs": ["close"], "func": f02_advs_046_max_1d_log_return_252d},
    "f02_advs_047_min_1d_log_return_252d": {"inputs": ["close"], "func": f02_advs_047_min_1d_log_return_252d},
    "f02_advs_048_max_1d_log_return_zscore_252d": {"inputs": ["close"], "func": f02_advs_048_max_1d_log_return_zscore_252d},
    "f02_advs_049_count_outsize_up_days_z_gt_3_252d": {"inputs": ["close"], "func": f02_advs_049_count_outsize_up_days_z_gt_3_252d},
    "f02_advs_050_count_outsize_down_days_z_lt_neg3_252d": {"inputs": ["close"], "func": f02_advs_050_count_outsize_down_days_z_lt_neg3_252d},
    "f02_advs_051_mean_top10_log_returns_252d": {"inputs": ["close"], "func": f02_advs_051_mean_top10_log_returns_252d},
    "f02_advs_052_mean_bottom10_log_returns_252d": {"inputs": ["close"], "func": f02_advs_052_mean_bottom10_log_returns_252d},
    "f02_advs_053_ratio_top10_to_bottom10_returns_252d": {"inputs": ["close"], "func": f02_advs_053_ratio_top10_to_bottom10_returns_252d},
    "f02_advs_054_share_of_252d_log_gain_from_top10_days": {"inputs": ["close"], "func": f02_advs_054_share_of_252d_log_gain_from_top10_days},
    "f02_advs_055_share_of_252d_log_gain_from_top5_days": {"inputs": ["close"], "func": f02_advs_055_share_of_252d_log_gain_from_top5_days},
    "f02_advs_056_days_above_3pct_log_return_252d": {"inputs": ["close"], "func": f02_advs_056_days_above_3pct_log_return_252d},
    "f02_advs_057_days_below_neg3pct_log_return_252d": {"inputs": ["close"], "func": f02_advs_057_days_below_neg3pct_log_return_252d},
    "f02_advs_058_max_3d_log_return_252d": {"inputs": ["close"], "func": f02_advs_058_max_3d_log_return_252d},
    "f02_advs_059_max_5d_log_return_252d": {"inputs": ["close"], "func": f02_advs_059_max_5d_log_return_252d},
    "f02_advs_060_max_10d_log_return_252d": {"inputs": ["close"], "func": f02_advs_060_max_10d_log_return_252d},
    "f02_advs_061_velocity_volume_corr_63d": {"inputs": ["close", "volume"], "func": f02_advs_061_velocity_volume_corr_63d},
    "f02_advs_062_velocity_volume_corr_252d": {"inputs": ["close", "volume"], "func": f02_advs_062_velocity_volume_corr_252d},
    "f02_advs_063_velocity_per_log_volume_21d": {"inputs": ["close", "volume"], "func": f02_advs_063_velocity_per_log_volume_21d},
    "f02_advs_064_velocity_per_log_volume_63d": {"inputs": ["close", "volume"], "func": f02_advs_064_velocity_per_log_volume_63d},
    "f02_advs_065_fractal_efficiency_21d": {"inputs": ["close"], "func": f02_advs_065_fractal_efficiency_21d},
    "f02_advs_066_fractal_efficiency_63d": {"inputs": ["close"], "func": f02_advs_066_fractal_efficiency_63d},
    "f02_advs_067_fractal_efficiency_252d": {"inputs": ["close"], "func": f02_advs_067_fractal_efficiency_252d},
    "f02_advs_068_efficiency_ratio_21d": {"inputs": ["close"], "func": f02_advs_068_efficiency_ratio_21d},
    "f02_advs_069_efficiency_ratio_63d": {"inputs": ["close"], "func": f02_advs_069_efficiency_ratio_63d},
    "f02_advs_070_efficiency_ratio_change_21d_vs_63d": {"inputs": ["close"], "func": f02_advs_070_efficiency_ratio_change_21d_vs_63d},
    "f02_advs_071_kaufman_efficiency_252d": {"inputs": ["close"], "func": f02_advs_071_kaufman_efficiency_252d},
    "f02_advs_072_advance_path_smoothness_63d": {"inputs": ["close"], "func": f02_advs_072_advance_path_smoothness_63d},
    "f02_advs_073_advance_path_smoothness_252d": {"inputs": ["close"], "func": f02_advs_073_advance_path_smoothness_252d},
    "f02_advs_074_log_return_per_atr_252d": {"inputs": ["close", "high", "low"], "func": f02_advs_074_log_return_per_atr_252d},
    "f02_advs_075_close_distance_per_atr_from_63d_low": {"inputs": ["close", "low", "high"], "func": f02_advs_075_close_distance_per_atr_from_63d_low},
}
