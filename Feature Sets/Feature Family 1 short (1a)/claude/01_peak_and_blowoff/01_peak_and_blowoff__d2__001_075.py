"""peak_and_blowoff d2 features 001-075 — second-derivative wrappers (acceleration)."""
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
#                    D2 FEATURES 001-075
# ============================================================

def f01_pab_001_log_dist_above_252d_high_d2(high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff()


def f01_pab_002_log_dist_above_63d_high_d2(high):
    rmax = high.rolling(QDAYS, min_periods=MDAYS).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff()


def f01_pab_003_log_dist_above_1260d_high_d2(high):
    rmax = high.rolling(1260, min_periods=YDAYS).max()
    return (_safe_log(high) - _safe_log(rmax)).diff().diff()


def f01_pab_004_days_since_252d_high_d2(high):
    def _bsm(w):
        return (len(w) - 1) - int(np.argmax(w))
    return high.rolling(YDAYS, min_periods=QDAYS).apply(_bsm, raw=True).diff().diff()


def f01_pab_005_consecutive_new_252d_highs_d2(high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    is_new = (high >= rmax).astype(float)
    grp = (is_new == 0).cumsum()
    return is_new.groupby(grp).cumsum().diff().diff()


def f01_pab_006_fraction_252d_within_1pct_of_max_d2(high):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    within = (high / rmax.replace(0, np.nan) >= 0.99).astype(float)
    return within.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()


def f01_pab_007_position_in_252d_range_d2(close, high, low):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    rmin = low.rolling(YDAYS, min_periods=QDAYS).min()
    rng = (rmax - rmin).replace(0, np.nan)
    return ((close - rmin) / rng).diff().diff()


def f01_pab_008_new_high_break_then_fail_count_21d_d2(close, high):
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((high > prior_max) & (close < close.shift(1))).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_009_ath_pressure_intensity_z_d2(high, low, close):
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    atr = _atr(high, low, close, MDAYS)
    excess = (high - prior_max) / atr.replace(0, np.nan)
    return _rolling_zscore(excess, YDAYS).diff().diff()


def f01_pab_010_count_252d_high_breaks_63d_d2(high):
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    return (high > prior_max).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()


def f01_pab_011_log_price_curvature_63d_d2(close):
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
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_curv, raw=True).diff().diff()


def f01_pab_012_log_price_curvature_252d_d2(close):
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
    return lp.rolling(YDAYS, min_periods=QDAYS).apply(_curv, raw=True).diff().diff()


def f01_pab_013_log_price_exp_fit_r2_63d_d2(close):
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
        return 1.0 - ((w - pred) ** 2).sum() / ss_tot
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_r2, raw=True).diff().diff()


def f01_pab_014_slope_acceleration_ratio_21_63_d2(close):
    lp = _safe_log(close)
    s21 = lp.diff(MDAYS) / MDAYS
    s63 = lp.diff(QDAYS) / QDAYS
    return _safe_div(s21, s63).diff().diff()


def f01_pab_015_positive_d2_streak_21d_d2(close):
    lp = _safe_log(close)
    d2 = lp.diff().diff()
    pos = (d2 > 0).astype(float)
    grp = (pos == 0).cumsum()
    return pos.groupby(grp).cumsum().diff().diff()


def f01_pab_016_cumulative_arc_height_above_linear_63d_d2(close):
    lp = _safe_log(close)
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_arc, raw=True).diff().diff()


def f01_pab_017_parabolic_slope_zscore_21d_d2(close):
    lp = _safe_log(close)
    slope = lp.diff(MDAYS) / MDAYS
    return _rolling_zscore(slope, YDAYS).diff().diff()


def f01_pab_018_third_moment_log_resid_63d_d2(close):
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
    return lp.rolling(QDAYS, min_periods=MDAYS).apply(_skew, raw=True).diff().diff()


def f01_pab_019_compound_advance_decay_21_vs_63_d2(close):
    lp = _safe_log(close)
    g21 = lp.diff(MDAYS) / MDAYS
    g63 = lp.diff(QDAYS) / QDAYS
    return _safe_div(g21, g63).diff().diff()


def f01_pab_020_log_price_velocity_acceleration_63d_d2(close):
    lp = _safe_log(close)
    slope = lp.diff(MDAYS) / MDAYS
    return _rolling_slope(slope, QDAYS).diff().diff()


def f01_pab_021_log_return_5d_d2(close):
    return _safe_log(close).diff(WDAYS).diff().diff()


def f01_pab_022_log_return_21d_d2(close):
    return _safe_log(close).diff(MDAYS).diff().diff()


def f01_pab_023_log_return_63d_d2(close):
    return _safe_log(close).diff(QDAYS).diff().diff()


def f01_pab_024_log_return_252d_d2(close):
    return _safe_log(close).diff(YDAYS).diff().diff()


def f01_pab_025_log_return_21d_zscore_252d_d2(close):
    r = _safe_log(close).diff(MDAYS)
    return _rolling_zscore(r, YDAYS).diff().diff()


def f01_pab_026_log_return_63d_zscore_252d_d2(close):
    r = _safe_log(close).diff(QDAYS)
    return _rolling_zscore(r, YDAYS).diff().diff()


def f01_pab_027_momentum_autocorr_lag1_21d_d2(close):
    r = _safe_log(close).diff()
    def _ac(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        a, b = w[:-1], w[1:]
        if a.std() == 0 or b.std() == 0:
            return np.nan
        return float(np.corrcoef(a, b)[0, 1])
    return r.rolling(MDAYS, min_periods=WDAYS).apply(_ac, raw=True).diff().diff()


def f01_pab_028_up_day_streak_max_63d_d2(close):
    up = (close.diff() > 0).astype(int)
    grp = (up == 0).cumsum()
    streak = up.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=WDAYS).max().diff().diff()


def f01_pab_029_up_day_fraction_63d_d2(close):
    up = (close.diff() > 0).astype(float)
    return up.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff()


def f01_pab_030_drift_to_vol_ratio_63d_d2(close):
    r = _safe_log(close).diff()
    m = r.rolling(QDAYS, min_periods=MDAYS).mean()
    s = r.rolling(QDAYS, min_periods=MDAYS).std()
    return (m / s.replace(0, np.nan)).diff().diff()


def f01_pab_031_close_to_sma21_ratio_d2(close):
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    return (_safe_div(close, sma) - 1.0).diff().diff()


def f01_pab_032_close_to_sma63_ratio_d2(close):
    sma = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return (_safe_div(close, sma) - 1.0).diff().diff()


def f01_pab_033_close_to_sma252_ratio_d2(close):
    sma = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(close, sma) - 1.0).diff().diff()


def f01_pab_034_sma21_to_sma63_ratio_d2(close):
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return (_safe_div(s21, s63) - 1.0).diff().diff()


def f01_pab_035_sma63_to_sma252_ratio_d2(close):
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(s63, s252) - 1.0).diff().diff()


def f01_pab_036_atr_normalized_sma21_extension_d2(high, low, close):
    sma = close.rolling(MDAYS, min_periods=WDAYS).mean()
    atr = _atr(high, low, close, MDAYS)
    return ((close - sma) / atr.replace(0, np.nan)).diff().diff()


def f01_pab_037_linear_regression_extension_63d_atr_norm_d2(high, low, close):
    def _resid(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        return float(w[-1] - (c1 * (len(w) - 1) + c0))
    resid = close.rolling(QDAYS, min_periods=MDAYS).apply(_resid, raw=True)
    atr = _atr(high, low, close, MDAYS)
    return (resid / atr.replace(0, np.nan)).diff().diff()


def f01_pab_038_anchored_252d_vwap_extension_d2(close, volume):
    pv = (close * volume).rolling(YDAYS, min_periods=QDAYS).sum()
    vv = volume.rolling(YDAYS, min_periods=QDAYS).sum()
    vwap = _safe_div(pv, vv)
    return (_safe_div(close, vwap) - 1.0).diff().diff()


def f01_pab_039_ma_stacking_score_d2(close):
    s21 = close.rolling(MDAYS, min_periods=WDAYS).mean()
    s63 = close.rolling(QDAYS, min_periods=MDAYS).mean()
    s252 = close.rolling(YDAYS, min_periods=QDAYS).mean()
    score = (close > s21).astype(float) + (s21 > s63).astype(float) + (s63 > s252).astype(float)
    return score.diff().diff()


def f01_pab_040_ema21_minus_ema63_ratio_d2(close):
    e21 = close.ewm(span=MDAYS, adjust=False, min_periods=WDAYS).mean()
    e63 = close.ewm(span=QDAYS, adjust=False, min_periods=MDAYS).mean()
    return _safe_div(e21 - e63, e63).diff().diff()


def f01_pab_041_volume_zscore_252d_d2(volume):
    return _rolling_zscore(volume, YDAYS).diff().diff()


def f01_pab_042_log_volume_ratio_21d_vs_252d_d2(volume):
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    v252 = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_log(_safe_div(v21, v252)).diff().diff()


def f01_pab_043_dollar_volume_zscore_252d_d2(close, volume):
    return _rolling_zscore(close * volume, YDAYS).diff().diff()


def f01_pab_044_up_minus_down_volume_zscore_21d_d2(close, volume):
    direction = np.sign(close.diff())
    signed_vol = (direction * volume).fillna(0.0)
    cum21 = signed_vol.rolling(MDAYS, min_periods=WDAYS).sum()
    return _rolling_zscore(cum21, YDAYS).diff().diff()


def f01_pab_045_up_volume_share_63d_d2(close, volume):
    up = (close.diff() > 0).astype(float)
    up_vol = (up * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    total = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(up_vol, total).diff().diff()


def f01_pab_046_obv_zscore_252d_d2(close, volume):
    direction = np.sign(close.diff()).fillna(0.0)
    obv = (direction * volume).cumsum()
    return _rolling_zscore(obv, YDAYS).diff().diff()


def f01_pab_047_obv_slope_63d_d2(close, volume):
    direction = np.sign(close.diff()).fillna(0.0)
    obv = (direction * volume).cumsum()
    return _rolling_slope(obv, QDAYS).diff().diff()


def f01_pab_048_obv_minus_price_slope_divergence_63d_d2(close, volume):
    direction = np.sign(close.diff()).fillna(0.0)
    obv = (direction * volume).cumsum()
    obv_z = _rolling_zscore(_rolling_slope(obv, QDAYS), YDAYS)
    px_z = _rolling_zscore(_rolling_slope(close, QDAYS), YDAYS)
    return (obv_z - px_z).diff().diff()


def f01_pab_049_ad_line_slope_63d_d2(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0.0) * volume).cumsum()
    return _rolling_slope(ad, QDAYS).diff().diff()


def f01_pab_050_ad_minus_price_slope_divergence_63d_d2(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0.0) * volume).cumsum()
    ad_z = _rolling_zscore(_rolling_slope(ad, QDAYS), YDAYS)
    px_z = _rolling_zscore(_rolling_slope(close, QDAYS), YDAYS)
    return (ad_z - px_z).diff().diff()


def f01_pab_051_money_flow_index_14d_d2(high, low, close, volume):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff())
    pos = rmf.where(direction > 0, 0.0).rolling(14, min_periods=WDAYS).sum()
    neg = rmf.where(direction < 0, 0.0).rolling(14, min_periods=WDAYS).sum()
    mr = pos / neg.replace(0, np.nan)
    return (100.0 - (100.0 / (1.0 + mr))).diff().diff()


def f01_pab_052_volume_climax_count_63d_d2(close, volume):
    v21 = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    is_climax = ((close.diff() > 0) & (volume > 3.0 * v21)).astype(float)
    return is_climax.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()


def f01_pab_053_volume_dryup_after_peak_21d_d2(volume):
    v5 = volume.rolling(WDAYS, min_periods=2).mean()
    v21_max = volume.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(v5, v21_max).diff().diff()


def f01_pab_054_price_volume_efficiency_63d_d2(close, volume):
    r = _safe_log(close).diff(QDAYS)
    cum_v = _safe_log(volume).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(r, cum_v).diff().diff()


def f01_pab_055_peak_dollar_volume_zscore_21d_d2(close, volume):
    dv = close * volume
    peak21 = dv.rolling(MDAYS, min_periods=WDAYS).max()
    return _rolling_zscore(peak21, YDAYS).diff().diff()


def f01_pab_056_atr_21_to_atr_252_ratio_d2(high, low, close):
    a21 = _atr(high, low, close, MDAYS)
    a252 = _atr(high, low, close, YDAYS)
    return (_safe_div(a21, a252) - 1.0).diff().diff()


def f01_pab_057_true_range_zscore_252d_d2(high, low, close):
    return _rolling_zscore(_true_range(high, low, close), YDAYS).diff().diff()


def f01_pab_058_realized_vol_21d_d2(close):
    r = _safe_log(close).diff()
    return (r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(YDAYS)).diff().diff()


def f01_pab_059_realized_vol_21_vs_252_ratio_d2(close):
    r = _safe_log(close).diff()
    v21 = r.rolling(MDAYS, min_periods=WDAYS).std()
    v252 = r.rolling(YDAYS, min_periods=QDAYS).std()
    return (_safe_div(v21, v252) - 1.0).diff().diff()


def f01_pab_060_parkinson_vol_21d_d2(high, low):
    lr = (_safe_log(high) - _safe_log(low)) ** 2
    pk = np.sqrt(lr.rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0)) * YDAYS)
    return pk.diff().diff()


def f01_pab_061_parkinson_to_realized_ratio_21d_d2(high, low, close):
    lr = (_safe_log(high) - _safe_log(low)) ** 2
    pk = np.sqrt(lr.rolling(MDAYS, min_periods=WDAYS).mean() / (4.0 * np.log(2.0)) * YDAYS)
    r = _safe_log(close).diff()
    rv = r.rolling(MDAYS, min_periods=WDAYS).std() * np.sqrt(YDAYS)
    return _safe_div(pk, rv).diff().diff()


def f01_pab_062_garman_klass_vol_21d_d2(open_, high, low, close):
    lh, ll, lo, lc = _safe_log(high), _safe_log(low), _safe_log(open_), _safe_log(close)
    term = 0.5 * (lh - ll) ** 2 - (2.0 * np.log(2.0) - 1.0) * (lc - lo) ** 2
    return (np.sqrt(term.rolling(MDAYS, min_periods=WDAYS).mean() * YDAYS)).diff().diff()


def f01_pab_063_rogers_satchell_vol_21d_d2(open_, high, low, close):
    lh, ll, lo, lc = _safe_log(high), _safe_log(low), _safe_log(open_), _safe_log(close)
    term = (lh - lc) * (lh - lo) + (ll - lc) * (ll - lo)
    return (np.sqrt(term.rolling(MDAYS, min_periods=WDAYS).mean() * YDAYS)).diff().diff()


def f01_pab_064_vol_of_vol_63d_d2(close):
    r = _safe_log(close).diff()
    rv = r.rolling(MDAYS, min_periods=WDAYS).std()
    return rv.rolling(QDAYS, min_periods=MDAYS).std().diff().diff()


def f01_pab_065_wide_range_bar_count_21d_d2(high, low, close):
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS)
    flag = (tr > 2.0 * atr).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_066_body_to_range_ratio_avg_21d_d2(open_, high, low, close):
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    return (body / rng).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()


def f01_pab_067_upper_wick_dominance_near_high_21d_d2(open_, high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    upper = high - close.where(close > open_, open_)
    rng = (high - low).replace(0, np.nan)
    share = (upper / rng).where(near, np.nan)
    return share.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()


def f01_pab_068_lower_wick_dominance_near_high_21d_d2(open_, high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    lower = close.where(close < open_, open_) - low
    rng = (high - low).replace(0, np.nan)
    share = (lower / rng).where(near, np.nan)
    return share.rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()


def f01_pab_069_doji_count_near_high_21d_d2(open_, high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    doji = (body / rng) < 0.1
    return (near & doji).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_070_shooting_star_count_near_high_21d_d2(open_, high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    body = (close - open_).abs()
    upper = high - close.where(close > open_, open_)
    lower = close.where(close < open_, open_) - low
    rng = (high - low).replace(0, np.nan)
    pat = ((upper / rng) > 0.6) & ((body / rng) < 0.3) & ((lower / rng) < 0.15)
    return (near & pat).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_071_close_in_lower_third_near_high_count_21d_d2(open_, high, low, close):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    rng = (high - low).replace(0, np.nan)
    pos = (close - low) / rng
    weak = pos < (1.0 / 3.0)
    return (near & weak).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_072_key_reversal_down_count_63d_d2(close, high):
    prior_max = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    flag = ((high > prior_max) & (close < close.shift(1))).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()


def f01_pab_073_outside_bar_bearish_count_63d_d2(open_, high, low, close):
    outside = (high > high.shift(1)) & (low < low.shift(1))
    bearish = close < close.shift(1)
    return (outside & bearish).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()


def f01_pab_074_inside_day_count_near_high_21d_d2(high, low):
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan) >= 0.98
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return (near & inside).astype(float).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()


def f01_pab_075_bearish_engulfing_count_63d_d2(open_, close):
    prev_up = close.shift(1) > open_.shift(1)
    cur_down = close < open_
    engulf = (open_ > close.shift(1)) & (close < open_.shift(1))
    return (prev_up & cur_down & engulf).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()


# ============================================================
#                        REGISTRY
# ============================================================

PEAK_AND_BLOWOFF_D2_REGISTRY_001_075 = {
    "f01_pab_001_log_dist_above_252d_high_d2": {"inputs": ["high"], "func": f01_pab_001_log_dist_above_252d_high_d2},
    "f01_pab_002_log_dist_above_63d_high_d2": {"inputs": ["high"], "func": f01_pab_002_log_dist_above_63d_high_d2},
    "f01_pab_003_log_dist_above_1260d_high_d2": {"inputs": ["high"], "func": f01_pab_003_log_dist_above_1260d_high_d2},
    "f01_pab_004_days_since_252d_high_d2": {"inputs": ["high"], "func": f01_pab_004_days_since_252d_high_d2},
    "f01_pab_005_consecutive_new_252d_highs_d2": {"inputs": ["high"], "func": f01_pab_005_consecutive_new_252d_highs_d2},
    "f01_pab_006_fraction_252d_within_1pct_of_max_d2": {"inputs": ["high"], "func": f01_pab_006_fraction_252d_within_1pct_of_max_d2},
    "f01_pab_007_position_in_252d_range_d2": {"inputs": ["close", "high", "low"], "func": f01_pab_007_position_in_252d_range_d2},
    "f01_pab_008_new_high_break_then_fail_count_21d_d2": {"inputs": ["close", "high"], "func": f01_pab_008_new_high_break_then_fail_count_21d_d2},
    "f01_pab_009_ath_pressure_intensity_z_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_009_ath_pressure_intensity_z_d2},
    "f01_pab_010_count_252d_high_breaks_63d_d2": {"inputs": ["high"], "func": f01_pab_010_count_252d_high_breaks_63d_d2},
    "f01_pab_011_log_price_curvature_63d_d2": {"inputs": ["close"], "func": f01_pab_011_log_price_curvature_63d_d2},
    "f01_pab_012_log_price_curvature_252d_d2": {"inputs": ["close"], "func": f01_pab_012_log_price_curvature_252d_d2},
    "f01_pab_013_log_price_exp_fit_r2_63d_d2": {"inputs": ["close"], "func": f01_pab_013_log_price_exp_fit_r2_63d_d2},
    "f01_pab_014_slope_acceleration_ratio_21_63_d2": {"inputs": ["close"], "func": f01_pab_014_slope_acceleration_ratio_21_63_d2},
    "f01_pab_015_positive_d2_streak_21d_d2": {"inputs": ["close"], "func": f01_pab_015_positive_d2_streak_21d_d2},
    "f01_pab_016_cumulative_arc_height_above_linear_63d_d2": {"inputs": ["close"], "func": f01_pab_016_cumulative_arc_height_above_linear_63d_d2},
    "f01_pab_017_parabolic_slope_zscore_21d_d2": {"inputs": ["close"], "func": f01_pab_017_parabolic_slope_zscore_21d_d2},
    "f01_pab_018_third_moment_log_resid_63d_d2": {"inputs": ["close"], "func": f01_pab_018_third_moment_log_resid_63d_d2},
    "f01_pab_019_compound_advance_decay_21_vs_63_d2": {"inputs": ["close"], "func": f01_pab_019_compound_advance_decay_21_vs_63_d2},
    "f01_pab_020_log_price_velocity_acceleration_63d_d2": {"inputs": ["close"], "func": f01_pab_020_log_price_velocity_acceleration_63d_d2},
    "f01_pab_021_log_return_5d_d2": {"inputs": ["close"], "func": f01_pab_021_log_return_5d_d2},
    "f01_pab_022_log_return_21d_d2": {"inputs": ["close"], "func": f01_pab_022_log_return_21d_d2},
    "f01_pab_023_log_return_63d_d2": {"inputs": ["close"], "func": f01_pab_023_log_return_63d_d2},
    "f01_pab_024_log_return_252d_d2": {"inputs": ["close"], "func": f01_pab_024_log_return_252d_d2},
    "f01_pab_025_log_return_21d_zscore_252d_d2": {"inputs": ["close"], "func": f01_pab_025_log_return_21d_zscore_252d_d2},
    "f01_pab_026_log_return_63d_zscore_252d_d2": {"inputs": ["close"], "func": f01_pab_026_log_return_63d_zscore_252d_d2},
    "f01_pab_027_momentum_autocorr_lag1_21d_d2": {"inputs": ["close"], "func": f01_pab_027_momentum_autocorr_lag1_21d_d2},
    "f01_pab_028_up_day_streak_max_63d_d2": {"inputs": ["close"], "func": f01_pab_028_up_day_streak_max_63d_d2},
    "f01_pab_029_up_day_fraction_63d_d2": {"inputs": ["close"], "func": f01_pab_029_up_day_fraction_63d_d2},
    "f01_pab_030_drift_to_vol_ratio_63d_d2": {"inputs": ["close"], "func": f01_pab_030_drift_to_vol_ratio_63d_d2},
    "f01_pab_031_close_to_sma21_ratio_d2": {"inputs": ["close"], "func": f01_pab_031_close_to_sma21_ratio_d2},
    "f01_pab_032_close_to_sma63_ratio_d2": {"inputs": ["close"], "func": f01_pab_032_close_to_sma63_ratio_d2},
    "f01_pab_033_close_to_sma252_ratio_d2": {"inputs": ["close"], "func": f01_pab_033_close_to_sma252_ratio_d2},
    "f01_pab_034_sma21_to_sma63_ratio_d2": {"inputs": ["close"], "func": f01_pab_034_sma21_to_sma63_ratio_d2},
    "f01_pab_035_sma63_to_sma252_ratio_d2": {"inputs": ["close"], "func": f01_pab_035_sma63_to_sma252_ratio_d2},
    "f01_pab_036_atr_normalized_sma21_extension_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_036_atr_normalized_sma21_extension_d2},
    "f01_pab_037_linear_regression_extension_63d_atr_norm_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_037_linear_regression_extension_63d_atr_norm_d2},
    "f01_pab_038_anchored_252d_vwap_extension_d2": {"inputs": ["close", "volume"], "func": f01_pab_038_anchored_252d_vwap_extension_d2},
    "f01_pab_039_ma_stacking_score_d2": {"inputs": ["close"], "func": f01_pab_039_ma_stacking_score_d2},
    "f01_pab_040_ema21_minus_ema63_ratio_d2": {"inputs": ["close"], "func": f01_pab_040_ema21_minus_ema63_ratio_d2},
    "f01_pab_041_volume_zscore_252d_d2": {"inputs": ["volume"], "func": f01_pab_041_volume_zscore_252d_d2},
    "f01_pab_042_log_volume_ratio_21d_vs_252d_d2": {"inputs": ["volume"], "func": f01_pab_042_log_volume_ratio_21d_vs_252d_d2},
    "f01_pab_043_dollar_volume_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f01_pab_043_dollar_volume_zscore_252d_d2},
    "f01_pab_044_up_minus_down_volume_zscore_21d_d2": {"inputs": ["close", "volume"], "func": f01_pab_044_up_minus_down_volume_zscore_21d_d2},
    "f01_pab_045_up_volume_share_63d_d2": {"inputs": ["close", "volume"], "func": f01_pab_045_up_volume_share_63d_d2},
    "f01_pab_046_obv_zscore_252d_d2": {"inputs": ["close", "volume"], "func": f01_pab_046_obv_zscore_252d_d2},
    "f01_pab_047_obv_slope_63d_d2": {"inputs": ["close", "volume"], "func": f01_pab_047_obv_slope_63d_d2},
    "f01_pab_048_obv_minus_price_slope_divergence_63d_d2": {"inputs": ["close", "volume"], "func": f01_pab_048_obv_minus_price_slope_divergence_63d_d2},
    "f01_pab_049_ad_line_slope_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f01_pab_049_ad_line_slope_63d_d2},
    "f01_pab_050_ad_minus_price_slope_divergence_63d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f01_pab_050_ad_minus_price_slope_divergence_63d_d2},
    "f01_pab_051_money_flow_index_14d_d2": {"inputs": ["high", "low", "close", "volume"], "func": f01_pab_051_money_flow_index_14d_d2},
    "f01_pab_052_volume_climax_count_63d_d2": {"inputs": ["close", "volume"], "func": f01_pab_052_volume_climax_count_63d_d2},
    "f01_pab_053_volume_dryup_after_peak_21d_d2": {"inputs": ["volume"], "func": f01_pab_053_volume_dryup_after_peak_21d_d2},
    "f01_pab_054_price_volume_efficiency_63d_d2": {"inputs": ["close", "volume"], "func": f01_pab_054_price_volume_efficiency_63d_d2},
    "f01_pab_055_peak_dollar_volume_zscore_21d_d2": {"inputs": ["close", "volume"], "func": f01_pab_055_peak_dollar_volume_zscore_21d_d2},
    "f01_pab_056_atr_21_to_atr_252_ratio_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_056_atr_21_to_atr_252_ratio_d2},
    "f01_pab_057_true_range_zscore_252d_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_057_true_range_zscore_252d_d2},
    "f01_pab_058_realized_vol_21d_d2": {"inputs": ["close"], "func": f01_pab_058_realized_vol_21d_d2},
    "f01_pab_059_realized_vol_21_vs_252_ratio_d2": {"inputs": ["close"], "func": f01_pab_059_realized_vol_21_vs_252_ratio_d2},
    "f01_pab_060_parkinson_vol_21d_d2": {"inputs": ["high", "low"], "func": f01_pab_060_parkinson_vol_21d_d2},
    "f01_pab_061_parkinson_to_realized_ratio_21d_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_061_parkinson_to_realized_ratio_21d_d2},
    "f01_pab_062_garman_klass_vol_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_062_garman_klass_vol_21d_d2},
    "f01_pab_063_rogers_satchell_vol_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_063_rogers_satchell_vol_21d_d2},
    "f01_pab_064_vol_of_vol_63d_d2": {"inputs": ["close"], "func": f01_pab_064_vol_of_vol_63d_d2},
    "f01_pab_065_wide_range_bar_count_21d_d2": {"inputs": ["high", "low", "close"], "func": f01_pab_065_wide_range_bar_count_21d_d2},
    "f01_pab_066_body_to_range_ratio_avg_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_066_body_to_range_ratio_avg_21d_d2},
    "f01_pab_067_upper_wick_dominance_near_high_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_067_upper_wick_dominance_near_high_21d_d2},
    "f01_pab_068_lower_wick_dominance_near_high_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_068_lower_wick_dominance_near_high_21d_d2},
    "f01_pab_069_doji_count_near_high_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_069_doji_count_near_high_21d_d2},
    "f01_pab_070_shooting_star_count_near_high_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_070_shooting_star_count_near_high_21d_d2},
    "f01_pab_071_close_in_lower_third_near_high_count_21d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_071_close_in_lower_third_near_high_count_21d_d2},
    "f01_pab_072_key_reversal_down_count_63d_d2": {"inputs": ["close", "high"], "func": f01_pab_072_key_reversal_down_count_63d_d2},
    "f01_pab_073_outside_bar_bearish_count_63d_d2": {"inputs": ["open", "high", "low", "close"], "func": f01_pab_073_outside_bar_bearish_count_63d_d2},
    "f01_pab_074_inside_day_count_near_high_21d_d2": {"inputs": ["high", "low"], "func": f01_pab_074_inside_day_count_near_high_21d_d2},
    "f01_pab_075_bearish_engulfing_count_63d_d2": {"inputs": ["open", "close"], "func": f01_pab_075_bearish_engulfing_count_63d_d2},
}
