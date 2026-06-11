"""peak_and_blowoff base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses (continued in __base__076_150.py for 150 total).
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

def f01_pab_001_log_dist_above_252d_high(high: pd.Series) -> pd.Series:
    """Log distance of high above 252d rolling max — annual ATH extension."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_log(high) - _safe_log(rmax)


def f01_pab_002_log_dist_above_63d_high(high: pd.Series) -> pd.Series:
    """Log distance above 63d high — quarterly breakout extension."""
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return _safe_log(high) - _safe_log(rmax)


def f01_pab_003_log_dist_above_1260d_high(high: pd.Series) -> pd.Series:
    """Log distance above 5y high — secular top extension."""
    rmax = high.rolling(1260, min_periods=YDAYS).max()
    return _safe_log(high) - _safe_log(rmax)


def f01_pab_004_days_since_252d_high(high: pd.Series) -> pd.Series:
    """Bars since 252d rolling max was hit — recency of annual peak."""
    def _bsm(w):
        return (len(w) - 1) - int(np.argmax(w))
    return high.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True)


def f01_pab_005_consecutive_new_252d_highs(high: pd.Series) -> pd.Series:
    """Length of current consecutive new-252d-high streak."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_new = (high >= rmax).astype(float)
    grp = (is_new == 0).cumsum()
    return is_new.groupby(grp).cumsum()


def f01_pab_006_fraction_252d_within_1pct_of_max(high: pd.Series) -> pd.Series:
    """Share of last 252 bars within 1% of the 252d max."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = (high / rmax.replace(0, np.nan) >= 0.99).astype(float)
    return within.rolling(YDAYS, min_periods=QDAYS).mean()


def f01_pab_007_position_in_252d_range(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Close placement in 252d range, 0=bottom 1=top."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return (close - rmin) / rng


def f01_pab_008_new_high_break_then_fail_count_21d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars in last 21 making new 252d high but closing below prior close."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    fail = close < close.shift(1)
    flag = (new_high & fail).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_009_ath_pressure_intensity_z(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of (high - prior 252d max) / ATR21 — breakout violence."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, MDAYS)
    excess = (high - prior_max) / atr.replace(0, np.nan)
    return _rolling_zscore(excess, YDAYS)


def f01_pab_010_count_252d_high_breaks_63d(high: pd.Series) -> pd.Series:
    """Count of bars in last 63 that set a new 252d high — breakout frequency."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = (high > prior_max).astype(float)
    return new_high.rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_011_log_price_curvature_63d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of log-price polyfit over 63d — parabolic curvature."""
    lp = _safe_log(close)
    def _curv(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            c2 = np.polyfit(x, w, 2)[0]
        except Exception:
            return np.nan
        return c2
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_curv, raw=True)


def f01_pab_012_log_price_curvature_252d(close: pd.Series) -> pd.Series:
    """Quadratic coefficient of log-price polyfit over 252d — long-horizon curvature."""
    lp = _safe_log(close)
    def _curv(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        try:
            c2 = np.polyfit(x, w, 2)[0]
        except Exception:
            return np.nan
        return c2
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_curv, raw=True)


def f01_pab_013_log_price_exp_fit_r2_63d(close: pd.Series) -> pd.Series:
    """R² of linear fit on log-price over 63d — measures exponentiality of trend."""
    lp = _safe_log(close)
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        ss_res = ((w - pred) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_r2, raw=True)


def f01_pab_014_slope_acceleration_ratio_21_63(close: pd.Series) -> pd.Series:
    """21d log-slope / 63d log-slope — speed-up factor."""
    lp = _safe_log(close)
    s21 = lp.diff(MDAYS) / MDAYS
    s63 = lp.diff(QDAYS) / QDAYS
    return _safe_div(s21, s63)


def f01_pab_015_positive_d2_streak_21d(close: pd.Series) -> pd.Series:
    """Length of current consecutive streak of positive 2nd-derivative log-price bars."""
    lp = _safe_log(close)
    d2 = lp.diff().diff()
    pos = (d2 > 0).astype(float)
    grp = (pos == 0).cumsum()
    return pos.groupby(grp).cumsum()


def f01_pab_016_cumulative_arc_height_above_linear_63d(close: pd.Series) -> pd.Series:
    """Sum of positive log-price residuals above 63d linear fit — parabolic arc area."""
    lp = _safe_log(close)
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_arc, raw=True)


def f01_pab_017_parabolic_slope_zscore_21d(close: pd.Series) -> pd.Series:
    """Z-score of recent 21d log-price slope vs 252d history."""
    lp = _safe_log(close)
    slope = lp.diff(MDAYS) / MDAYS
    return _rolling_zscore(slope, YDAYS)


def f01_pab_018_third_moment_log_resid_63d(close: pd.Series) -> pd.Series:
    """Skewness of residuals from 63d log-price linear fit — trajectory asymmetry."""
    lp = _safe_log(close)
    def _skew(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        sd = resid.std()
        if sd == 0:
            return np.nan
        return float(((resid - resid.mean()) ** 3).mean() / (sd ** 3))
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_skew, raw=True)


def f01_pab_019_compound_advance_decay_21_vs_63(close: pd.Series) -> pd.Series:
    """21d geometric mean log return / 63d geometric mean log return."""
    lp = _safe_log(close)
    g21 = lp.diff(MDAYS) / MDAYS
    g63 = lp.diff(QDAYS) / QDAYS
    return _safe_div(g21, g63)


def f01_pab_020_log_price_velocity_acceleration_63d(close: pd.Series) -> pd.Series:
    """63d slope of the 21d log-price slope — meta-acceleration."""
    lp = _safe_log(close)
    slope = lp.diff(MDAYS) / MDAYS
    return _rolling_slope(slope, QDAYS)


def f01_pab_021_log_return_5d(close: pd.Series) -> pd.Series:
    """5-day log return — short-horizon thrust."""
    return _safe_log(close).diff(WDAYS)


def f01_pab_022_log_return_21d(close: pd.Series) -> pd.Series:
    """21-day log return — monthly thrust."""
    return _safe_log(close).diff(MDAYS)


def f01_pab_023_log_return_63d(close: pd.Series) -> pd.Series:
    """63-day log return — quarterly thrust."""
    return _safe_log(close).diff(QDAYS)


def f01_pab_024_log_return_252d(close: pd.Series) -> pd.Series:
    """252-day log return — annual run-up."""
    return _safe_log(close).diff(YDAYS)


def f01_pab_025_log_return_21d_zscore_252d(close: pd.Series) -> pd.Series:
    """21d log return z-scored vs 252d distribution."""
    r = _safe_log(close).diff(MDAYS)
    return _rolling_zscore(r, YDAYS)


def f01_pab_026_log_return_63d_zscore_252d(close: pd.Series) -> pd.Series:
    """63d log return z-scored vs 252d distribution."""
    r = _safe_log(close).diff(QDAYS)
    return _rolling_zscore(r, YDAYS)


def f01_pab_027_momentum_autocorr_lag1_21d(close: pd.Series) -> pd.Series:
    """Lag-1 autocorrelation of daily log returns over 21d window."""
    r = _safe_log(close).diff()
    def _ac(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        a, b = w[:-1], w[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return r.rolling(MDAYS, min_periods=WDAYS).apply(_ac, raw=True)


def f01_pab_028_up_day_streak_max_63d(close: pd.Series) -> pd.Series:
    """Longest consecutive up-day streak inside the last 63 bars."""
    up = (close.diff() > 0).astype(int)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=WDAYS).max()


def f01_pab_029_up_day_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of up days in last 63d."""
    up = (close.diff() > 0).astype(float)
    return up.rolling(QDAYS, min_periods=MDAYS).mean()


def f01_pab_030_drift_to_vol_ratio_63d(close: pd.Series) -> pd.Series:
    """Mean daily log return / std over 63d (Sharpe-like)."""
    r = _safe_log(close).diff()
    m = r.rolling(QDAYS, min_periods=MDAYS).mean()
    s = r.rolling(QDAYS, min_periods=MDAYS).std()
    return m / s.replace(0, np.nan)


def f01_pab_031_close_to_sma21_ratio(close: pd.Series) -> pd.Series:
    """Close / SMA(21) - 1 — short-term overshoot."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(close, sma) - 1.0


def f01_pab_032_close_to_sma63_ratio(close: pd.Series) -> pd.Series:
    """Close / SMA(63) - 1 — medium-term posture."""
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(close, sma) - 1.0


def f01_pab_033_close_to_sma252_ratio(close: pd.Series) -> pd.Series:
    """Close / SMA(252) - 1 — long-trend regime extension."""
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(close, sma) - 1.0


def f01_pab_034_sma21_to_sma63_ratio(close: pd.Series) -> pd.Series:
    """SMA(21)/SMA(63) - 1 — short vs medium trend alignment."""
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(s21, s63) - 1.0


def f01_pab_035_sma63_to_sma252_ratio(close: pd.Series) -> pd.Series:
    """SMA(63)/SMA(252) - 1 — medium vs long trend alignment."""
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s63, s252) - 1.0


def f01_pab_036_atr_normalized_sma21_extension(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(Close - SMA21) / ATR21 — extension in volatility units."""
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, MDAYS)
    return (close - sma) / atr.replace(0, np.nan)


def f01_pab_037_linear_regression_extension_63d_atr_norm(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Last-bar residual from 63d close linear fit, divided by ATR21."""
    def _resid(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        return float(w[-1] - (c1 * (len(w) - 1) + c0))
    resid = close.rolling(QDAYS, min_periods=MDAYS).apply(_resid, raw=True)
    atr = _atr(high, low, close, MDAYS)
    return resid / atr.replace(0, np.nan)


def f01_pab_038_anchored_252d_vwap_extension(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close / 252d rolling VWAP - 1."""
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vwap = _safe_div(pv, vv)
    return _safe_div(close, vwap) - 1.0


def f01_pab_039_ma_stacking_score(close: pd.Series) -> pd.Series:
    """0-3 score counting close>SMA21, SMA21>SMA63, SMA63>SMA252 — trend stack health."""
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return (close > s21).astype(float) + (s21 > s63).astype(float) + (s63 > s252).astype(float)


def f01_pab_040_ema21_minus_ema63_ratio(close: pd.Series) -> pd.Series:
    """(EMA21 - EMA63)/EMA63 — momentum-vs-trend spread."""
    e21 = close.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean()
    e63 = close.ewm(span=QDAYS, adjust=False, min_periods=MDAYS).mean()
    return _safe_div(e21 - e63, e63)


def f01_pab_041_volume_zscore_252d(volume: pd.Series) -> pd.Series:
    """Raw volume z-score over 252d."""
    return _rolling_zscore(volume, YDAYS)


def f01_pab_042_log_volume_ratio_21d_vs_252d(volume: pd.Series) -> pd.Series:
    """log(avg vol 21d / avg vol 252d) — volume regime expansion."""
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_log(_safe_div(v21, v252))


def f01_pab_043_dollar_volume_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Dollar volume (close*volume) z-scored over 252d."""
    return _rolling_zscore(close * volume, YDAYS)


def f01_pab_044_up_minus_down_volume_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign(close.diff)*volume summed over 21d, z-scored vs 252d distribution."""
    direction = np.sign(close.diff())
    signed_vol = (direction * volume).fillna(0.0)
    cum21 = signed_vol.rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(cum21, YDAYS)


def f01_pab_045_up_volume_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of up-day volume / sum of total volume over 63d."""
    up = (close.diff() > 0).astype(float)
    up_vol = (up * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    total = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(up_vol, total)


def f01_pab_046_obv_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Standard OBV z-scored over 252d."""
    direction = np.sign(close.diff()).fillna(0.0)
    obv = (direction * volume).cumsum()
    return _rolling_zscore(obv, YDAYS)


def f01_pab_047_obv_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of OBV."""
    direction = np.sign(close.diff()).fillna(0.0)
    obv = (direction * volume).cumsum()
    return _rolling_slope(obv, QDAYS)


def f01_pab_048_obv_minus_price_slope_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-normalized OBV slope minus z-normalized price slope (63d) — bearish OBV divergence."""
    direction = np.sign(close.diff()).fillna(0.0)
    obv = (direction * volume).cumsum()
    obv_z = _rolling_zscore(_rolling_slope(obv, QDAYS), YDAYS)
    px_z = _rolling_zscore(_rolling_slope(close, QDAYS), YDAYS)
    return obv_z - px_z


def f01_pab_049_ad_line_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of Accumulation/Distribution line."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0.0) * volume).cumsum()
    return _rolling_slope(ad, QDAYS)


def f01_pab_050_ad_minus_price_slope_divergence_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-normalized AD-line slope minus z-normalized price slope (63d)."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0.0) * volume).cumsum()
    ad_z = _rolling_zscore(_rolling_slope(ad, QDAYS), YDAYS)
    px_z = _rolling_zscore(_rolling_slope(close, QDAYS), YDAYS)
    return ad_z - px_z


def f01_pab_051_money_flow_index_14d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """14-day Money Flow Index — volume-weighted RSI."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff())
    pos = rmf.where(direction > 0, 0.0).rolling(14, min_periods=WDAYS).sum()
    neg = rmf.where(direction < 0, 0.0).rolling(14, min_periods=WDAYS).sum()
    mr = pos / neg.replace(0, np.nan)
    return 100.0 - (100.0 / (1.0 + mr))


def f01_pab_052_volume_climax_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in last 63 with up close AND volume > 3x SMA21 of volume."""
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    is_climax = ((close.diff() > 0) & (volume > 3.0 * v21)).astype(float)
    return is_climax.rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_053_volume_dryup_after_peak_21d(volume: pd.Series) -> pd.Series:
    """Last-5d mean volume / 21d max volume — dryup after climax."""
    v5 = volume.rolling(WDAYS, min_periods=2).mean()
    v21_max = volume.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(v5, v21_max)


def f01_pab_054_price_volume_efficiency_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d log return / 63d cumulative log-volume — return per unit volume."""
    r = _safe_log(close).diff(QDAYS)
    cum_v = _safe_log(volume).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(r, cum_v)


def f01_pab_055_peak_dollar_volume_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max dollar volume in last 21d, z-scored vs 252d distribution."""
    dv = close * volume
    peak21 = dv.rolling(MDAYS, min_periods=WDAYS).max()
    return _rolling_zscore(peak21, YDAYS)


def f01_pab_056_atr_21_to_atr_252_ratio(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21)/ATR(252) - 1 — volatility regime expansion."""
    a21 = _atr(high, low, close, MDAYS)
    a252 = _atr(high, low, close, YDAYS)
    return _safe_div(a21, a252) - 1.0


def f01_pab_057_true_range_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Today's True Range z-scored over 252d."""
    return _rolling_zscore(_true_range(high, low, close), YDAYS)


def f01_pab_058_realized_vol_21d(close: pd.Series) -> pd.Series:
    """Annualized 21d std of daily log returns."""
    r = _safe_log(close).diff()
    return r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(YDAYS)


def f01_pab_059_realized_vol_21_vs_252_ratio(close: pd.Series) -> pd.Series:
    """21d realized vol / 252d realized vol - 1."""
    r = _safe_log(close).diff()
    v21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(v21, v252) - 1.0


def f01_pab_060_parkinson_vol_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Parkinson high-low estimator, 21d annualized."""
    lr = (_safe_log(high) - _safe_log(low)) ** 2
    return np.sqrt(lr.rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0)) * YDAYS)


def f01_pab_061_parkinson_to_realized_ratio_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Parkinson 21d vol / close-to-close realized vol — intraday whipping ratio."""
    lr = (_safe_log(high) - _safe_log(low)) ** 2
    pk = np.sqrt(lr.rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0)) * YDAYS)
    r = _safe_log(close).diff()
    rv = r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(YDAYS)
    return _safe_div(pk, rv)


def f01_pab_062_garman_klass_vol_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Garman-Klass 21d annualized OHLC vol."""
    lh, ll, lo, lc = _safe_log(high), _safe_log(low), _safe_log(open_), _safe_log(close)
    term = 0.5 * (lh - ll) ** 2 - (2.0 * np.log(2.0) - 1.0) * (lc - lo) ** 2
    return np.sqrt(term.rolling(MDAYS, min_periods=WDAYS).mean() * YDAYS)


def f01_pab_063_rogers_satchell_vol_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell drift-free 21d OHLC vol."""
    lh, ll, lo, lc = _safe_log(high), _safe_log(low), _safe_log(open_), _safe_log(close)
    term = (lh - lc) * (lh - lo) + (ll - lc) * (ll - lo)
    return np.sqrt(term.rolling(MDAYS, min_periods=WDAYS).mean() * YDAYS)


def f01_pab_064_vol_of_vol_63d(close: pd.Series) -> pd.Series:
    """63d std of 21d rolling realized vol — vol-of-vol."""
    r = _safe_log(close).diff()
    rv = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv.rolling(QDAYS, min_periods=MDAYS).std()


def f01_pab_065_wide_range_bar_count_21d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Bars in last 21 with TR > 2x ATR21."""
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS)
    flag = (tr > 2.0 * atr).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_066_body_to_range_ratio_avg_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |close-open|/(high-low) over 21d — body dominance vs indecision."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    return (body / rng).rolling(MDAYS, min_periods=WDAYS).mean()


def f01_pab_067_upper_wick_dominance_near_high_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean upper-wick share of bars within 2% of 252d high in last 21."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    upper = high - close.where(close > open_, open_)
    rng = (high - low).replace(0, np.nan)
    share = (upper / rng).where(near, np.nan)
    return share.rolling(MDAYS, min_periods=WDAYS).mean()


def f01_pab_068_lower_wick_dominance_near_high_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean lower-wick share of bars within 2% of 252d high in last 21."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    lower = close.where(close < open_, open_) - low
    rng = (high - low).replace(0, np.nan)
    share = (lower / rng).where(near, np.nan)
    return share.rolling(MDAYS, min_periods=WDAYS).mean()


def f01_pab_069_doji_count_near_high_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Doji bars (body/range<0.1) near 252d high count in last 21."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    doji = (body / rng) < 0.1
    return (near & doji).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_070_shooting_star_count_near_high_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Shooting-star pattern bars near 252d high in last 21."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    body = (close - open_).abs()
    upper = high - close.where(close > open_, open_)
    lower = close.where(close < open_, open_) - low
    rng = (high - low).replace(0, np.nan)
    pat = ((upper / rng) > 0.6) & ((body / rng) < 0.3) & ((lower / rng) < 0.15)
    return (near & pat).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_071_close_in_lower_third_near_high_count_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Near-high bars in last 21 closing in lower third of own range — weak closes."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    weak = pos < (1.0 / 3.0)
    return (near & weak).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_072_key_reversal_down_count_63d(close: pd.Series, high: pd.Series) -> pd.Series:
    """Bars in last 63 making new 252d high but closing below prior close."""
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    new_high = high > prior_max
    fail = close < close.shift(1)
    return (new_high & fail).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_073_outside_bar_bearish_count_63d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Outside-bar (engulfing range) with bearish close, count last 63."""
    outside = (high > high.shift(1)) & (low < low.shift(1))
    bearish = close < close.shift(1)
    return (outside & bearish).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


def f01_pab_074_inside_day_count_near_high_21d(high: pd.Series, low: pd.Series) -> pd.Series:
    """Inside days near 252d high in last 21 — coiling at top."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return (near & inside).astype(float).rolling(MDAYS, min_periods=WDAYS).sum()


def f01_pab_075_bearish_engulfing_count_63d(open_: pd.Series, close: pd.Series) -> pd.Series:
    """Bearish engulfing pattern count in last 63d."""
    prev_up = close.shift(1) > open_.shift(1)
    cur_down = close < open_
    engulf = (open_ > close.shift(1)) & (close < open_.shift(1))
    return (prev_up & cur_down & engulf).astype(float).rolling(QDAYS, min_periods=MDAYS).sum()


# ============================================================
#                        REGISTRY
# ============================================================

PEAK_AND_BLOWOFF_BASE_REGISTRY_001_075 = {
    "f01_pab_001_log_dist_above_252d_high": {"inputs": ["high"], "func": f01_pab_001_log_dist_above_252d_high},
    "f01_pab_002_log_dist_above_63d_high": {"inputs": ["high"], "func": f01_pab_002_log_dist_above_63d_high},
    "f01_pab_003_log_dist_above_1260d_high": {"inputs": ["high"], "func": f01_pab_003_log_dist_above_1260d_high},
    "f01_pab_004_days_since_252d_high": {"inputs": ["high"], "func": f01_pab_004_days_since_252d_high},
    "f01_pab_005_consecutive_new_252d_highs": {"inputs": ["high"], "func": f01_pab_005_consecutive_new_252d_highs},
    "f01_pab_006_fraction_252d_within_1pct_of_max": {"inputs": ["high"], "func": f01_pab_006_fraction_252d_within_1pct_of_max},
    "f01_pab_007_position_in_252d_range": {"inputs": ["close", "high", "low"], "func": f01_pab_007_position_in_252d_range},
    "f01_pab_008_new_high_break_then_fail_count_21d": {"inputs": ["close", "high"], "func": f01_pab_008_new_high_break_then_fail_count_21d},
    "f01_pab_009_ath_pressure_intensity_z": {"inputs": ["high", "low", "close"], "func": f01_pab_009_ath_pressure_intensity_z},
    "f01_pab_010_count_252d_high_breaks_63d": {"inputs": ["high"], "func": f01_pab_010_count_252d_high_breaks_63d},
    "f01_pab_011_log_price_curvature_63d": {"inputs": ["close"], "func": f01_pab_011_log_price_curvature_63d},
    "f01_pab_012_log_price_curvature_252d": {"inputs": ["close"], "func": f01_pab_012_log_price_curvature_252d},
    "f01_pab_013_log_price_exp_fit_r2_63d": {"inputs": ["close"], "func": f01_pab_013_log_price_exp_fit_r2_63d},
    "f01_pab_014_slope_acceleration_ratio_21_63": {"inputs": ["close"], "func": f01_pab_014_slope_acceleration_ratio_21_63},
    "f01_pab_015_positive_d2_streak_21d": {"inputs": ["close"], "func": f01_pab_015_positive_d2_streak_21d},
    "f01_pab_016_cumulative_arc_height_above_linear_63d": {"inputs": ["close"], "func": f01_pab_016_cumulative_arc_height_above_linear_63d},
    "f01_pab_017_parabolic_slope_zscore_21d": {"inputs": ["close"], "func": f01_pab_017_parabolic_slope_zscore_21d},
    "f01_pab_018_third_moment_log_resid_63d": {"inputs": ["close"], "func": f01_pab_018_third_moment_log_resid_63d},
    "f01_pab_019_compound_advance_decay_21_vs_63": {"inputs": ["close"], "func": f01_pab_019_compound_advance_decay_21_vs_63},
    "f01_pab_020_log_price_velocity_acceleration_63d": {"inputs": ["close"], "func": f01_pab_020_log_price_velocity_acceleration_63d},
    "f01_pab_021_log_return_5d": {"inputs": ["close"], "func": f01_pab_021_log_return_5d},
    "f01_pab_022_log_return_21d": {"inputs": ["close"], "func": f01_pab_022_log_return_21d},
    "f01_pab_023_log_return_63d": {"inputs": ["close"], "func": f01_pab_023_log_return_63d},
    "f01_pab_024_log_return_252d": {"inputs": ["close"], "func": f01_pab_024_log_return_252d},
    "f01_pab_025_log_return_21d_zscore_252d": {"inputs": ["close"], "func": f01_pab_025_log_return_21d_zscore_252d},
    "f01_pab_026_log_return_63d_zscore_252d": {"inputs": ["close"], "func": f01_pab_026_log_return_63d_zscore_252d},
    "f01_pab_027_momentum_autocorr_lag1_21d": {"inputs": ["close"], "func": f01_pab_027_momentum_autocorr_lag1_21d},
    "f01_pab_028_up_day_streak_max_63d": {"inputs": ["close"], "func": f01_pab_028_up_day_streak_max_63d},
    "f01_pab_029_up_day_fraction_63d": {"inputs": ["close"], "func": f01_pab_029_up_day_fraction_63d},
    "f01_pab_030_drift_to_vol_ratio_63d": {"inputs": ["close"], "func": f01_pab_030_drift_to_vol_ratio_63d},
    "f01_pab_031_close_to_sma21_ratio": {"inputs": ["close"], "func": f01_pab_031_close_to_sma21_ratio},
    "f01_pab_032_close_to_sma63_ratio": {"inputs": ["close"], "func": f01_pab_032_close_to_sma63_ratio},
    "f01_pab_033_close_to_sma252_ratio": {"inputs": ["close"], "func": f01_pab_033_close_to_sma252_ratio},
    "f01_pab_034_sma21_to_sma63_ratio": {"inputs": ["close"], "func": f01_pab_034_sma21_to_sma63_ratio},
    "f01_pab_035_sma63_to_sma252_ratio": {"inputs": ["close"], "func": f01_pab_035_sma63_to_sma252_ratio},
    "f01_pab_036_atr_normalized_sma21_extension": {"inputs": ["high", "low", "close"], "func": f01_pab_036_atr_normalized_sma21_extension},
    "f01_pab_037_linear_regression_extension_63d_atr_norm": {"inputs": ["high", "low", "close"], "func": f01_pab_037_linear_regression_extension_63d_atr_norm},
    "f01_pab_038_anchored_252d_vwap_extension": {"inputs": ["close", "volume"], "func": f01_pab_038_anchored_252d_vwap_extension},
    "f01_pab_039_ma_stacking_score": {"inputs": ["close"], "func": f01_pab_039_ma_stacking_score},
    "f01_pab_040_ema21_minus_ema63_ratio": {"inputs": ["close"], "func": f01_pab_040_ema21_minus_ema63_ratio},
    "f01_pab_041_volume_zscore_252d": {"inputs": ["volume"], "func": f01_pab_041_volume_zscore_252d},
    "f01_pab_042_log_volume_ratio_21d_vs_252d": {"inputs": ["volume"], "func": f01_pab_042_log_volume_ratio_21d_vs_252d},
    "f01_pab_043_dollar_volume_zscore_252d": {"inputs": ["close", "volume"], "func": f01_pab_043_dollar_volume_zscore_252d},
    "f01_pab_044_up_minus_down_volume_zscore_21d": {"inputs": ["close", "volume"], "func": f01_pab_044_up_minus_down_volume_zscore_21d},
    "f01_pab_045_up_volume_share_63d": {"inputs": ["close", "volume"], "func": f01_pab_045_up_volume_share_63d},
    "f01_pab_046_obv_zscore_252d": {"inputs": ["close", "volume"], "func": f01_pab_046_obv_zscore_252d},
    "f01_pab_047_obv_slope_63d": {"inputs": ["close", "volume"], "func": f01_pab_047_obv_slope_63d},
    "f01_pab_048_obv_minus_price_slope_divergence_63d": {"inputs": ["close", "volume"], "func": f01_pab_048_obv_minus_price_slope_divergence_63d},
    "f01_pab_049_ad_line_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f01_pab_049_ad_line_slope_63d},
    "f01_pab_050_ad_minus_price_slope_divergence_63d": {"inputs": ["high", "low", "close", "volume"], "func": f01_pab_050_ad_minus_price_slope_divergence_63d},
    "f01_pab_051_money_flow_index_14d": {"inputs": ["high", "low", "close", "volume"], "func": f01_pab_051_money_flow_index_14d},
    "f01_pab_052_volume_climax_count_63d": {"inputs": ["close", "volume"], "func": f01_pab_052_volume_climax_count_63d},
    "f01_pab_053_volume_dryup_after_peak_21d": {"inputs": ["volume"], "func": f01_pab_053_volume_dryup_after_peak_21d},
    "f01_pab_054_price_volume_efficiency_63d": {"inputs": ["close", "volume"], "func": f01_pab_054_price_volume_efficiency_63d},
    "f01_pab_055_peak_dollar_volume_zscore_21d": {"inputs": ["close", "volume"], "func": f01_pab_055_peak_dollar_volume_zscore_21d},
    "f01_pab_056_atr_21_to_atr_252_ratio": {"inputs": ["high", "low", "close"], "func": f01_pab_056_atr_21_to_atr_252_ratio},
    "f01_pab_057_true_range_zscore_252d": {"inputs": ["high", "low", "close"], "func": f01_pab_057_true_range_zscore_252d},
    "f01_pab_058_realized_vol_21d": {"inputs": ["close"], "func": f01_pab_058_realized_vol_21d},
    "f01_pab_059_realized_vol_21_vs_252_ratio": {"inputs": ["close"], "func": f01_pab_059_realized_vol_21_vs_252_ratio},
    "f01_pab_060_parkinson_vol_21d": {"inputs": ["high", "low"], "func": f01_pab_060_parkinson_vol_21d},
    "f01_pab_061_parkinson_to_realized_ratio_21d": {"inputs": ["high", "low", "close"], "func": f01_pab_061_parkinson_to_realized_ratio_21d},
    "f01_pab_062_garman_klass_vol_21d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_062_garman_klass_vol_21d},
    "f01_pab_063_rogers_satchell_vol_21d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_063_rogers_satchell_vol_21d},
    "f01_pab_064_vol_of_vol_63d": {"inputs": ["close"], "func": f01_pab_064_vol_of_vol_63d},
    "f01_pab_065_wide_range_bar_count_21d": {"inputs": ["high", "low", "close"], "func": f01_pab_065_wide_range_bar_count_21d},
    "f01_pab_066_body_to_range_ratio_avg_21d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_066_body_to_range_ratio_avg_21d},
    "f01_pab_067_upper_wick_dominance_near_high_21d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_067_upper_wick_dominance_near_high_21d},
    "f01_pab_068_lower_wick_dominance_near_high_21d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_068_lower_wick_dominance_near_high_21d},
    "f01_pab_069_doji_count_near_high_21d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_069_doji_count_near_high_21d},
    "f01_pab_070_shooting_star_count_near_high_21d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_070_shooting_star_count_near_high_21d},
    "f01_pab_071_close_in_lower_third_near_high_count_21d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_071_close_in_lower_third_near_high_count_21d},
    "f01_pab_072_key_reversal_down_count_63d": {"inputs": ["close", "high"], "func": f01_pab_072_key_reversal_down_count_63d},
    "f01_pab_073_outside_bar_bearish_count_63d": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_073_outside_bar_bearish_count_63d},
    "f01_pab_074_inside_day_count_near_high_21d": {"inputs": ["high", "low"], "func": f01_pab_074_inside_day_count_near_high_21d},
    "f01_pab_075_bearish_engulfing_count_63d": {"inputs": ["open", "close"], "func": f01_pab_075_bearish_engulfing_count_63d},
}
