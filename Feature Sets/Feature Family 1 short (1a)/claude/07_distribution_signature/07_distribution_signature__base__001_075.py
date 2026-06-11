"""distribution_signature base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Theme: institutional distribution MECHANICS — supply/demand imbalance, effort-vs-result
mismatches, OBV/AD/CMF/MFI divergences, Wyckoff-style upthrusts and weak rallies.
Distinct from vbpk (single-event climaxes) and vddu (volume contraction): dsig
targets the SHAPE of unloading. 150 distinct hypotheses. PIT-clean.
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
#                  FEATURES 001-075
# ============================================================

def f07_dsig_001_up_minus_down_vol_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (up-bar vol - down-bar vol) over 21d — negative = selling pressure."""
    chg = close.diff()
    net = volume.where(chg > 0, 0) - volume.where(chg < 0, 0)
    return _rolling_zscore(net, MDAYS)


def f07_dsig_002_up_minus_down_vol_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (up-bar vol - down-bar vol) over 63d."""
    chg = close.diff()
    net = volume.where(chg > 0, 0) - volume.where(chg < 0, 0)
    return _rolling_zscore(net, QDAYS)


def f07_dsig_003_down_vol_fraction_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(down-bar vol) / Sum(all vol) over 21d."""
    chg = close.diff()
    dn = volume.where(chg < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dn, tot)


def f07_dsig_004_down_vol_fraction_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(down-bar vol) / Sum(all vol) over 63d."""
    chg = close.diff()
    dn = volume.where(chg < 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    tot = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dn, tot)


def f07_dsig_005_down_vol_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of down-bar vol over 63d (rising = building supply)."""
    chg = close.diff()
    dn = volume.where(chg < 0, 0)
    return _rolling_slope(dn, QDAYS)


def f07_dsig_006_down_vol_zscore_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of down-bar vol over 21d."""
    chg = close.diff()
    dn = volume.where(chg < 0, 0)
    return _rolling_zscore(dn, MDAYS)


def f07_dsig_007_down_vol_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of down-bar vol over 63d."""
    chg = close.diff()
    dn = volume.where(chg < 0, 0)
    return _rolling_zscore(dn, QDAYS)


def f07_dsig_008_up_vol_zscore_decline_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of up-bar vol over 63d (declining = thin demand)."""
    chg = close.diff()
    up = volume.where(chg > 0, 0)
    return _rolling_zscore(up, QDAYS)


def f07_dsig_009_up_vol_regression_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of up-bar volume over 63d."""
    chg = close.diff()
    up = volume.where(chg > 0, 0)
    return _rolling_slope(up, QDAYS)


def f07_dsig_010_up_minus_down_vol_cumulative_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Cumulative net up-down vol over 63d window (positive = accumulation, negative = distribution)."""
    chg = close.diff()
    net = volume.where(chg > 0, 0) - volume.where(chg < 0, 0)
    return net.rolling(QDAYS, min_periods=MDAYS).sum()


def f07_dsig_011_up_minus_down_vol_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of (up vol - down vol) over 63d."""
    chg = close.diff()
    net = volume.where(chg > 0, 0) - volume.where(chg < 0, 0)
    return _rolling_slope(net, QDAYS)


def f07_dsig_012_supply_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-bar vol / Up-bar vol summed over 21d (high = supply > demand)."""
    chg = close.diff()
    up = volume.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = volume.where(chg < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dn, up)


def f07_dsig_013_supply_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Down-bar vol / Up-bar vol summed over 63d."""
    chg = close.diff()
    up = volume.where(chg > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    dn = volume.where(chg < 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dn, up)


def f07_dsig_014_supply_ratio_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of supply ratio over 63d."""
    chg = close.diff()
    up = volume.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    dn = volume.where(chg < 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    ratio = _safe_div(dn, up)
    return _rolling_slope(ratio, QDAYS)


def f07_dsig_015_down_vol_days_fraction_21d(close: pd.Series) -> pd.Series:
    """Fraction of last 21d bars where close fell — pure down-bar count."""
    flag = (close.diff() < 0).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f07_dsig_016_down_vol_days_fraction_63d(close: pd.Series) -> pd.Series:
    """Fraction of last 63d bars where close fell."""
    flag = (close.diff() < 0).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f07_dsig_017_red_vs_green_vol_mean_21d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on close<open bars / avg vol on close>open bars over 21d."""
    red = volume.where(close < open_)
    green = volume.where(close > open_)
    return _safe_div(
        red.rolling(MDAYS, min_periods=WDAYS).mean(),
        green.rolling(MDAYS, min_periods=WDAYS).mean(),
    )


def f07_dsig_018_red_vs_green_vol_mean_63d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on red bars / avg vol on green bars over 63d."""
    red = volume.where(close < open_)
    green = volume.where(close > open_)
    return _safe_div(
        red.rolling(QDAYS, min_periods=MDAYS).mean(),
        green.rolling(QDAYS, min_periods=MDAYS).mean(),
    )


def f07_dsig_019_red_bar_vol_slope_63d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of red-bar vol (vol on close<open bars) over 63d."""
    red = volume.where(close < open_, 0)
    return _rolling_slope(red, QDAYS)


def f07_dsig_020_avg_vol_close_below_open_21d_z(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score (vs 252d vol distribution) of mean vol on close<open bars in 21d."""
    red = volume.where(close < open_)
    m = red.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(m, YDAYS)


def f07_dsig_021_avg_vol_close_below_open_63d_z(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 020 but over 63d window."""
    red = volume.where(close < open_)
    m = red.rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(m, YDAYS)


def f07_dsig_022_close_below_open_vol_weighted_pct_63d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Vol-weighted fraction of bars closing below open over 63d."""
    red_v = volume.where(close < open_, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    tot_v = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(red_v, tot_v)


def f07_dsig_023_red_bar_dollar_vol_z_63d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of mean (close*volume) on red bars over 63d vs 252d $-vol distribution."""
    dv = close * volume
    red_dv = dv.where(close < open_)
    m = red_dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _rolling_zscore(m, YDAYS)


def f07_dsig_024_weighted_directional_vol_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(sign(chg) * vol * |chg|) over 21d / sum(vol*|chg|) — directional weighted index."""
    chg = close.diff()
    w = volume * chg.abs()
    sw = volume * chg
    num = sw.rolling(MDAYS, min_periods=WDAYS).sum()
    den = w.rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(num, den)


def f07_dsig_025_weighted_directional_vol_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 024 over 63d."""
    chg = close.diff()
    w = volume * chg.abs()
    sw = volume * chg
    num = sw.rolling(QDAYS, min_periods=MDAYS).sum()
    den = w.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(num, den)


def f07_dsig_026_churning_bar_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d with vol > 2x SMA_63 AND (H-L)/ATR21 < 0.8."""
    avg_v = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_v = volume > 2.0 * avg_v
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) / atr.replace(0, np.nan) < 0.8
    flag = (big_v & narrow).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f07_dsig_027_churning_bar_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 026 over 63d."""
    avg_v = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_v = volume > 2.0 * avg_v
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) / atr.replace(0, np.nan) < 0.8
    flag = (big_v & narrow).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f07_dsig_028_avg_vol_on_small_range_bars_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg vol on bars where (H-L)/ATR21 < 0.5 over 21d — heavy vol on tiny bars = churning."""
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) / atr.replace(0, np.nan) < 0.5
    v = volume.where(narrow)
    return v.rolling(MDAYS, min_periods=WDAYS).mean()


def f07_dsig_029_effort_result_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(vol over 21d) / sum(|pct change| over 21d) — vol per unit move."""
    v = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    r = close.pct_change().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(v, r)


def f07_dsig_030_effort_result_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 029 over 63d."""
    v = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    r = close.pct_change().abs().rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(v, r)


def f07_dsig_031_up_effort_result_mismatch_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(up-bar vol) / Sum(up-bar pct gain) over 21d — heavy vol for tiny gains."""
    chg = close.pct_change()
    up_v = volume.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    up_r = chg.where(chg > 0, 0).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(up_v, up_r)


def f07_dsig_032_up_effort_result_mismatch_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 031 over 63d."""
    chg = close.pct_change()
    up_v = volume.where(chg > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    up_r = chg.where(chg > 0, 0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(up_v, up_r)


def f07_dsig_033_high_vol_low_close_position_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d with vol z > 2 AND close in lower third of range — heavy sell-into-rally."""
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    pos = (close - low) / (high - low).replace(0, np.nan)
    weak = pos < 1.0 / 3.0
    flag = (big & weak).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f07_dsig_034_high_vol_low_close_position_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 033 over 63d."""
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    pos = (close - low) / (high - low).replace(0, np.nan)
    weak = pos < 1.0 / 3.0
    flag = (big & weak).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f07_dsig_035_vol_per_atr_move_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(vol over 21d) / sum(TR over 21d) — vol per dollar of true range."""
    v = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    tr = _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(v, tr)


def f07_dsig_036_vol_per_atr_move_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 035 over 63d."""
    v = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    tr = _true_range(high, low, close).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(v, tr)


def f07_dsig_037_log_vol_log_range_ratio_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Log(mean 21d vol) / log(mean 21d range) — multiplicative effort-result ratio."""
    v = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    r = (high - low).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_log(v) - _safe_log(r)


def f07_dsig_038_churning_intensity_z_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z(vol z - range z) where range z is (H-L)/ATR(252) — high vol relative to range."""
    z_v = _rolling_zscore(volume, YDAYS)
    atr252 = _atr(high, low, close, YDAYS)
    rng_norm = (high - low) / atr252.replace(0, np.nan)
    z_r = _rolling_zscore(rng_norm, YDAYS)
    return (z_v - z_r).rolling(MDAYS, min_periods=WDAYS).mean()


def f07_dsig_039_churning_intensity_z_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 038 averaged over 63d."""
    z_v = _rolling_zscore(volume, YDAYS)
    atr252 = _atr(high, low, close, YDAYS)
    rng_norm = (high - low) / atr252.replace(0, np.nan)
    z_r = _rolling_zscore(rng_norm, YDAYS)
    return (z_v - z_r).rolling(QDAYS, min_periods=MDAYS).mean()


def f07_dsig_040_high_vol_narrow_range_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d with vol z > 1.5 AND range < 60pct of ATR21."""
    z = _rolling_zscore(volume, YDAYS)
    big = z > 1.5
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) < 0.6 * atr
    flag = (big & narrow).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f07_dsig_041_high_vol_narrow_range_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 040 over 63d."""
    z = _rolling_zscore(volume, YDAYS)
    big = z > 1.5
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) < 0.6 * atr
    flag = (big & narrow).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f07_dsig_042_wide_vol_low_progress_count_21d(close: pd.Series, volume: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Bars in 21d with wide range AND tiny close change — big effort, no progress."""
    atr = _atr(high, low, close, MDAYS)
    wide = (high - low) > 1.5 * atr
    rel = (close - close.shift(1)).abs() / close.shift(1).replace(0, np.nan)
    tiny = rel < 0.005
    big_v = _rolling_zscore(volume, YDAYS) > 1.0
    flag = (wide & tiny & big_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f07_dsig_043_vol_expansion_without_price_expansion_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of (vol z - |return| z) — vol rising while moves shrink."""
    z_v = _rolling_zscore(volume, YDAYS)
    z_r = _rolling_zscore(close.pct_change().abs(), YDAYS)
    return _rolling_slope(z_v - z_r, MDAYS)


def f07_dsig_044_price_volume_correlation_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d rolling Pearson correlation of close vs volume (negative = distribution)."""
    return close.rolling(MDAYS, min_periods=WDAYS).corr(volume)


def f07_dsig_045_price_volume_correlation_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d rolling Pearson correlation of close vs volume."""
    return close.rolling(QDAYS, min_periods=MDAYS).corr(volume)


def f07_dsig_046_price_vol_slope_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(slope of price over 63d / mean) - (slope of vol over 63d / mean) — sign-divergence."""
    p_sl = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    v_sl = _rolling_slope(volume, QDAYS) / volume.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return p_sl - v_sl


def f07_dsig_047_cum_vol_vs_cum_price_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of cumulative volume 63d - slope of cumulative close 63d, both normalized."""
    cv = volume.rolling(QDAYS, min_periods=MDAYS).sum()
    cp = close.rolling(QDAYS, min_periods=MDAYS).sum()
    v_sl = _rolling_slope(cv, QDAYS) / cv.replace(0, np.nan)
    p_sl = _rolling_slope(cp, QDAYS) / cp.replace(0, np.nan)
    return v_sl - p_sl


def f07_dsig_048_distribution_day_count_1pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d with return < -1pct AND vol > prior-bar vol — IBD-style distribution days."""
    chg = close.pct_change()
    big_loss = chg < -0.01
    higher_v = volume > volume.shift(1)
    flag = (big_loss & higher_v).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f07_dsig_049_distribution_day_count_1pct_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 048 over 63d."""
    chg = close.pct_change()
    big_loss = chg < -0.01
    higher_v = volume > volume.shift(1)
    flag = (big_loss & higher_v).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f07_dsig_050_distribution_day_cluster_max_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max consecutive-distribution-day streak inside last 63d."""
    chg = close.pct_change()
    big_loss = chg < -0.01
    higher_v = volume > volume.shift(1)
    flag = (big_loss & higher_v).astype(int)
    grp = (flag == 0).cumsum()
    streak = flag.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=MDAYS).max()


def f07_dsig_051_obv_slope_63d_neg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope over 63d (negative = distribution)."""
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    return _rolling_slope(obv, QDAYS)


def f07_dsig_052_obv_slope_252d_neg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """OBV slope over 252d."""
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    return _rolling_slope(obv, YDAYS)


def f07_dsig_053_obv_price_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sign(price slope 63d) * sign(OBV slope 63d) * abs(diff) — divergence magnitude (negative=bear div)."""
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    p_sl = _rolling_slope(close, QDAYS)
    o_sl = _rolling_slope(obv, QDAYS)
    p_n = p_sl / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    o_n = o_sl / obv.rolling(QDAYS, min_periods=MDAYS).mean().abs().replace(0, np.nan)
    return p_n - o_n


def f07_dsig_054_obv_price_divergence_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 053 over 252d."""
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    p_sl = _rolling_slope(close, YDAYS)
    o_sl = _rolling_slope(obv, YDAYS)
    p_n = p_sl / close.rolling(YDAYS, min_periods=QDAYS).mean().replace(0, np.nan)
    o_n = o_sl / obv.rolling(YDAYS, min_periods=QDAYS).mean().abs().replace(0, np.nan)
    return p_n - o_n


def f07_dsig_055_obv_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of OBV vs its 252d distribution."""
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    return _rolling_zscore(obv, YDAYS)


def f07_dsig_056_obv_plateau_count_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d where |OBV diff| / 21d-std of OBV < 0.1 — plateau indicator."""
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    flat = (obv.diff().abs() < 0.1 * obv.rolling(MDAYS, min_periods=WDAYS).std()).astype(float)
    return flat.rolling(MDAYS, min_periods=WDAYS).sum()


def f07_dsig_057_ad_line_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Accumulation/Distribution line slope over 63d (negative = distribution)."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    return _rolling_slope(ad, QDAYS)


def f07_dsig_058_ad_line_slope_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD line slope over 252d."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    return _rolling_slope(ad, YDAYS)


def f07_dsig_059_ad_price_divergence_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """AD-line vs price slope divergence over 63d."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    p_sl = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    a_sl = _rolling_slope(ad, QDAYS) / ad.rolling(QDAYS, min_periods=MDAYS).mean().abs().replace(0, np.nan)
    return p_sl - a_sl


def f07_dsig_060_ad_line_zscore_252d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of AD line vs its 252d distribution."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    return _rolling_zscore(ad, YDAYS)


def f07_dsig_061_cmf_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 21d (negative = distribution)."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    return mfv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)


def f07_dsig_062_cmf_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 63d."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    return mfv.rolling(QDAYS, min_periods=MDAYS).sum() / volume.rolling(QDAYS, min_periods=MDAYS).sum().replace(0, np.nan)


def f07_dsig_063_cmf_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of CMF(21) over 21d."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    cmf = mfv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    return _rolling_slope(cmf, MDAYS)


def f07_dsig_064_cmf_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of CMF(21) over 63d."""
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    cmf = mfv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    return _rolling_slope(cmf, QDAYS)


def f07_dsig_065_mfi_14d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Money Flow Index over 14d."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    pos_sum = pos.rolling(14, min_periods=5).sum()
    neg_sum = neg.rolling(14, min_periods=5).sum()
    mr = pos_sum / neg_sum.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + mr)


def f07_dsig_066_mfi_28d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """MFI over 28d."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    pos_sum = pos.rolling(28, min_periods=10).sum()
    neg_sum = neg.rolling(28, min_periods=10).sum()
    mr = pos_sum / neg_sum.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + mr)


def f07_dsig_067_mfi_divergence_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Price 63d slope - MFI(14) 63d slope (both normalized) — divergence."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    mr = pos.rolling(14, min_periods=5).sum() / neg.rolling(14, min_periods=5).sum().replace(0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    p_n = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    m_n = _rolling_slope(mfi, QDAYS) / mfi.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return p_n - m_n


def f07_dsig_068_mfi_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of MFI(14) over 21d."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    mr = pos.rolling(14, min_periods=5).sum() / neg.rolling(14, min_periods=5).sum().replace(0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return _rolling_slope(mfi, MDAYS)


def f07_dsig_069_mfi_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of MFI(14) over 63d."""
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    mr = pos.rolling(14, min_periods=5).sum() / neg.rolling(14, min_periods=5).sum().replace(0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + mr)
    return _rolling_slope(mfi, QDAYS)


def f07_dsig_070_nvi_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of Negative Volume Index over 21d — smart-money proxy."""
    vd = volume < volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vd, chg, 0.0), index=close.index)
    nvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_slope(nvi, MDAYS)


def f07_dsig_071_pvi_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of Positive Volume Index over 21d."""
    vu = volume > volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vu, chg, 0.0), index=close.index)
    pvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_slope(pvi, MDAYS)


def f07_dsig_072_nvi_to_pvi_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """NVI / PVI 21d-mean — smart-money vs herd participation."""
    vd = volume < volume.shift(1)
    vu = volume > volume.shift(1)
    chg = close.pct_change().fillna(0)
    nvi_incr = pd.Series(np.where(vd, chg, 0.0), index=close.index)
    pvi_incr = pd.Series(np.where(vu, chg, 0.0), index=close.index)
    nvi = 100.0 * (1.0 + nvi_incr).cumprod()
    pvi = 100.0 * (1.0 + pvi_incr).cumprod()
    return _safe_div(
        nvi.rolling(MDAYS, min_periods=WDAYS).mean(),
        pvi.rolling(MDAYS, min_periods=WDAYS).mean(),
    )


def f07_dsig_073_nvi_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of NVI over 63d."""
    vd = volume < volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vd, chg, 0.0), index=close.index)
    nvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_zscore(nvi, QDAYS)


def f07_dsig_074_pvi_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of PVI over 63d."""
    vu = volume > volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vu, chg, 0.0), index=close.index)
    pvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_zscore(pvi, QDAYS)


def f07_dsig_075_composite_moneyflow_distribution_score_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean of (-z(OBV slope) + -z(AD slope) + -z(CMF)) over 63d — composite distribution z."""
    sign = np.sign(close.diff()).fillna(0)
    obv = (sign * volume).cumsum()
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv.fillna(0) * volume).cumsum()
    mfv = clv.fillna(0) * volume
    cmf = mfv.rolling(MDAYS, min_periods=WDAYS).sum() / volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    z_o = -_rolling_zscore(_rolling_slope(obv, QDAYS), YDAYS)
    z_a = -_rolling_zscore(_rolling_slope(ad, QDAYS), YDAYS)
    z_c = -_rolling_zscore(cmf, YDAYS)
    return (z_o + z_a + z_c).rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
#                        REGISTRY
# ============================================================

DISTRIBUTION_SIGNATURE_BASE_REGISTRY_001_075 = {
    "f07_dsig_001_up_minus_down_vol_zscore_21d": {"inputs": ["close", "volume"], "func": f07_dsig_001_up_minus_down_vol_zscore_21d},
    "f07_dsig_002_up_minus_down_vol_zscore_63d": {"inputs": ["close", "volume"], "func": f07_dsig_002_up_minus_down_vol_zscore_63d},
    "f07_dsig_003_down_vol_fraction_21d": {"inputs": ["close", "volume"], "func": f07_dsig_003_down_vol_fraction_21d},
    "f07_dsig_004_down_vol_fraction_63d": {"inputs": ["close", "volume"], "func": f07_dsig_004_down_vol_fraction_63d},
    "f07_dsig_005_down_vol_slope_63d": {"inputs": ["close", "volume"], "func": f07_dsig_005_down_vol_slope_63d},
    "f07_dsig_006_down_vol_zscore_21d": {"inputs": ["close", "volume"], "func": f07_dsig_006_down_vol_zscore_21d},
    "f07_dsig_007_down_vol_zscore_63d": {"inputs": ["close", "volume"], "func": f07_dsig_007_down_vol_zscore_63d},
    "f07_dsig_008_up_vol_zscore_decline_63d": {"inputs": ["close", "volume"], "func": f07_dsig_008_up_vol_zscore_decline_63d},
    "f07_dsig_009_up_vol_regression_slope_63d": {"inputs": ["close", "volume"], "func": f07_dsig_009_up_vol_regression_slope_63d},
    "f07_dsig_010_up_minus_down_vol_cumulative_63d": {"inputs": ["close", "volume"], "func": f07_dsig_010_up_minus_down_vol_cumulative_63d},
    "f07_dsig_011_up_minus_down_vol_slope_63d": {"inputs": ["close", "volume"], "func": f07_dsig_011_up_minus_down_vol_slope_63d},
    "f07_dsig_012_supply_ratio_21d": {"inputs": ["close", "volume"], "func": f07_dsig_012_supply_ratio_21d},
    "f07_dsig_013_supply_ratio_63d": {"inputs": ["close", "volume"], "func": f07_dsig_013_supply_ratio_63d},
    "f07_dsig_014_supply_ratio_slope_63d": {"inputs": ["close", "volume"], "func": f07_dsig_014_supply_ratio_slope_63d},
    "f07_dsig_015_down_vol_days_fraction_21d": {"inputs": ["close"], "func": f07_dsig_015_down_vol_days_fraction_21d},
    "f07_dsig_016_down_vol_days_fraction_63d": {"inputs": ["close"], "func": f07_dsig_016_down_vol_days_fraction_63d},
    "f07_dsig_017_red_vs_green_vol_mean_21d": {"inputs": ["open", "close", "volume"], "func": f07_dsig_017_red_vs_green_vol_mean_21d},
    "f07_dsig_018_red_vs_green_vol_mean_63d": {"inputs": ["open", "close", "volume"], "func": f07_dsig_018_red_vs_green_vol_mean_63d},
    "f07_dsig_019_red_bar_vol_slope_63d": {"inputs": ["open", "close", "volume"], "func": f07_dsig_019_red_bar_vol_slope_63d},
    "f07_dsig_020_avg_vol_close_below_open_21d_z": {"inputs": ["open", "close", "volume"], "func": f07_dsig_020_avg_vol_close_below_open_21d_z},
    "f07_dsig_021_avg_vol_close_below_open_63d_z": {"inputs": ["open", "close", "volume"], "func": f07_dsig_021_avg_vol_close_below_open_63d_z},
    "f07_dsig_022_close_below_open_vol_weighted_pct_63d": {"inputs": ["open", "close", "volume"], "func": f07_dsig_022_close_below_open_vol_weighted_pct_63d},
    "f07_dsig_023_red_bar_dollar_vol_z_63d": {"inputs": ["open", "close", "volume"], "func": f07_dsig_023_red_bar_dollar_vol_z_63d},
    "f07_dsig_024_weighted_directional_vol_index_21d": {"inputs": ["close", "volume"], "func": f07_dsig_024_weighted_directional_vol_index_21d},
    "f07_dsig_025_weighted_directional_vol_index_63d": {"inputs": ["close", "volume"], "func": f07_dsig_025_weighted_directional_vol_index_63d},
    "f07_dsig_026_churning_bar_count_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_026_churning_bar_count_21d},
    "f07_dsig_027_churning_bar_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_027_churning_bar_count_63d},
    "f07_dsig_028_avg_vol_on_small_range_bars_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_028_avg_vol_on_small_range_bars_21d},
    "f07_dsig_029_effort_result_ratio_21d": {"inputs": ["close", "volume"], "func": f07_dsig_029_effort_result_ratio_21d},
    "f07_dsig_030_effort_result_ratio_63d": {"inputs": ["close", "volume"], "func": f07_dsig_030_effort_result_ratio_63d},
    "f07_dsig_031_up_effort_result_mismatch_21d": {"inputs": ["close", "volume"], "func": f07_dsig_031_up_effort_result_mismatch_21d},
    "f07_dsig_032_up_effort_result_mismatch_63d": {"inputs": ["close", "volume"], "func": f07_dsig_032_up_effort_result_mismatch_63d},
    "f07_dsig_033_high_vol_low_close_position_count_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_033_high_vol_low_close_position_count_21d},
    "f07_dsig_034_high_vol_low_close_position_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_034_high_vol_low_close_position_count_63d},
    "f07_dsig_035_vol_per_atr_move_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_035_vol_per_atr_move_21d},
    "f07_dsig_036_vol_per_atr_move_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_036_vol_per_atr_move_63d},
    "f07_dsig_037_log_vol_log_range_ratio_21d": {"inputs": ["high", "low", "volume"], "func": f07_dsig_037_log_vol_log_range_ratio_21d},
    "f07_dsig_038_churning_intensity_z_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_038_churning_intensity_z_21d},
    "f07_dsig_039_churning_intensity_z_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_039_churning_intensity_z_63d},
    "f07_dsig_040_high_vol_narrow_range_count_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_040_high_vol_narrow_range_count_21d},
    "f07_dsig_041_high_vol_narrow_range_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_041_high_vol_narrow_range_count_63d},
    "f07_dsig_042_wide_vol_low_progress_count_21d": {"inputs": ["close", "volume", "high", "low"], "func": f07_dsig_042_wide_vol_low_progress_count_21d},
    "f07_dsig_043_vol_expansion_without_price_expansion_21d": {"inputs": ["close", "volume"], "func": f07_dsig_043_vol_expansion_without_price_expansion_21d},
    "f07_dsig_044_price_volume_correlation_21d": {"inputs": ["close", "volume"], "func": f07_dsig_044_price_volume_correlation_21d},
    "f07_dsig_045_price_volume_correlation_63d": {"inputs": ["close", "volume"], "func": f07_dsig_045_price_volume_correlation_63d},
    "f07_dsig_046_price_vol_slope_divergence_63d": {"inputs": ["close", "volume"], "func": f07_dsig_046_price_vol_slope_divergence_63d},
    "f07_dsig_047_cum_vol_vs_cum_price_slope_63d": {"inputs": ["close", "volume"], "func": f07_dsig_047_cum_vol_vs_cum_price_slope_63d},
    "f07_dsig_048_distribution_day_count_1pct_21d": {"inputs": ["close", "volume"], "func": f07_dsig_048_distribution_day_count_1pct_21d},
    "f07_dsig_049_distribution_day_count_1pct_63d": {"inputs": ["close", "volume"], "func": f07_dsig_049_distribution_day_count_1pct_63d},
    "f07_dsig_050_distribution_day_cluster_max_63d": {"inputs": ["close", "volume"], "func": f07_dsig_050_distribution_day_cluster_max_63d},
    "f07_dsig_051_obv_slope_63d_neg": {"inputs": ["close", "volume"], "func": f07_dsig_051_obv_slope_63d_neg},
    "f07_dsig_052_obv_slope_252d_neg": {"inputs": ["close", "volume"], "func": f07_dsig_052_obv_slope_252d_neg},
    "f07_dsig_053_obv_price_divergence_63d": {"inputs": ["close", "volume"], "func": f07_dsig_053_obv_price_divergence_63d},
    "f07_dsig_054_obv_price_divergence_252d": {"inputs": ["close", "volume"], "func": f07_dsig_054_obv_price_divergence_252d},
    "f07_dsig_055_obv_zscore_252d": {"inputs": ["close", "volume"], "func": f07_dsig_055_obv_zscore_252d},
    "f07_dsig_056_obv_plateau_count_21d": {"inputs": ["close", "volume"], "func": f07_dsig_056_obv_plateau_count_21d},
    "f07_dsig_057_ad_line_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_057_ad_line_slope_63d},
    "f07_dsig_058_ad_line_slope_252d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_058_ad_line_slope_252d},
    "f07_dsig_059_ad_price_divergence_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_059_ad_price_divergence_63d},
    "f07_dsig_060_ad_line_zscore_252d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_060_ad_line_zscore_252d},
    "f07_dsig_061_cmf_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_061_cmf_21d},
    "f07_dsig_062_cmf_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_062_cmf_63d},
    "f07_dsig_063_cmf_slope_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_063_cmf_slope_21d},
    "f07_dsig_064_cmf_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_064_cmf_slope_63d},
    "f07_dsig_065_mfi_14d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_065_mfi_14d},
    "f07_dsig_066_mfi_28d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_066_mfi_28d},
    "f07_dsig_067_mfi_divergence_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_067_mfi_divergence_63d},
    "f07_dsig_068_mfi_slope_21d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_068_mfi_slope_21d},
    "f07_dsig_069_mfi_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_069_mfi_slope_63d},
    "f07_dsig_070_nvi_slope_21d": {"inputs": ["close", "volume"], "func": f07_dsig_070_nvi_slope_21d},
    "f07_dsig_071_pvi_slope_21d": {"inputs": ["close", "volume"], "func": f07_dsig_071_pvi_slope_21d},
    "f07_dsig_072_nvi_to_pvi_ratio_21d": {"inputs": ["close", "volume"], "func": f07_dsig_072_nvi_to_pvi_ratio_21d},
    "f07_dsig_073_nvi_zscore_63d": {"inputs": ["close", "volume"], "func": f07_dsig_073_nvi_zscore_63d},
    "f07_dsig_074_pvi_zscore_63d": {"inputs": ["close", "volume"], "func": f07_dsig_074_pvi_zscore_63d},
    "f07_dsig_075_composite_moneyflow_distribution_score_63d": {"inputs": ["high", "low", "close", "volume"], "func": f07_dsig_075_composite_moneyflow_distribution_score_63d},
}
