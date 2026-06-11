"""volume_distribution_dryup base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continued. Theme: AD/OBV/MFI dryup, turnover & participation contraction,
silent-topping patterns, time-shape of fade.
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


def _obv(close, volume):
    sign = np.sign(close.diff()).fillna(0)
    return (sign * volume).cumsum()


def _ad_line(high, low, close, volume):
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    return (clv.fillna(0) * volume).cumsum()


def _mfi(high, low, close, volume, n=14):
    tp = (high + low + close) / 3.0
    rmf = tp * volume
    pos = rmf.where(tp > tp.shift(1), 0.0)
    neg = rmf.where(tp < tp.shift(1), 0.0)
    pos_sum = pos.rolling(n, min_periods=max(n // 3, 2)).sum()
    neg_sum = neg.rolling(n, min_periods=max(n // 3, 2)).sum()
    mr = pos_sum / neg_sum.replace(0, np.nan)
    return 100.0 - 100.0 / (1.0 + mr)


def _cmf(high, low, close, volume, n=21):
    rng = (high - low).replace(0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    mfv = clv.fillna(0) * volume
    return mfv.rolling(n, min_periods=max(n // 3, 2)).sum() / volume.rolling(n, min_periods=max(n // 3, 2)).sum().replace(0, np.nan)


# ============================================================
#                  FEATURES 076-150
# ============================================================

def f06_vddu_076_ad_line_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of Accumulation/Distribution line over 21d — flattening when dry."""
    return _rolling_slope(_ad_line(high, low, close, volume), MDAYS)


def f06_vddu_077_ad_line_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of AD line over 63d."""
    return _rolling_slope(_ad_line(high, low, close, volume), QDAYS)


def f06_vddu_078_obv_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of OBV over 21d."""
    return _rolling_slope(_obv(close, volume), MDAYS)


def f06_vddu_079_obv_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of OBV over 63d."""
    return _rolling_slope(_obv(close, volume), QDAYS)


def f06_vddu_080_obv_price_slope_divergence_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of price (normalized) minus slope of OBV (normalized) over 63d."""
    p_sl = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    obv = _obv(close, volume)
    o_sl = _rolling_slope(obv, QDAYS) / obv.rolling(QDAYS, min_periods=MDAYS).mean().abs().replace(0, np.nan)
    return p_sl - o_sl


def f06_vddu_081_ad_price_slope_divergence_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of price minus slope of AD line, both normalized, over 63d."""
    p_sl = _rolling_slope(close, QDAYS) / close.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    ad = _ad_line(high, low, close, volume)
    a_sl = _rolling_slope(ad, QDAYS) / ad.rolling(QDAYS, min_periods=MDAYS).mean().abs().replace(0, np.nan)
    return p_sl - a_sl


def f06_vddu_082_vwap_21d_slope_decay(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of rolling 21d VWAP, then its diff — slope-decay signal."""
    num = (close * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    den = volume.rolling(MDAYS, min_periods=WDAYS).sum().replace(0, np.nan)
    vw = num / den
    return _rolling_slope(vw, MDAYS).diff()


def f06_vddu_083_dollar_vwap_slope_decay_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of rolling 63d dollar-VWAP, then its diff."""
    dv = close * volume
    num = (close * dv).rolling(QDAYS, min_periods=MDAYS).sum()
    den = dv.rolling(QDAYS, min_periods=MDAYS).sum().replace(0, np.nan)
    vw = num / den
    return _rolling_slope(vw, QDAYS).diff()


def f06_vddu_084_avg_dollar_vol_above_vwap63_decline(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of mean $-vol on above-VWAP-63d bars — declining when interest fades."""
    num = (close * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum().replace(0, np.nan)
    vw = num / den
    above = close > vw
    dv = close * volume
    above_dv = dv.where(above)
    return _rolling_slope(above_dv.rolling(MDAYS, min_periods=WDAYS).mean(), MDAYS)


def f06_vddu_085_above_to_below_vwap_vol_ratio_decay_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of (above-VWAP vol / below-VWAP vol)."""
    num = (close * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    den = volume.rolling(QDAYS, min_periods=MDAYS).sum().replace(0, np.nan)
    vw = num / den
    above = close > vw
    av = volume.where(above).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum()
    bv = volume.where(~above).fillna(0).rolling(MDAYS, min_periods=WDAYS).sum()
    ratio = _safe_div(av, bv)
    return _rolling_slope(ratio, MDAYS)


def f06_vddu_086_mfi_slope_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of MFI(14) — declining money flow."""
    return _rolling_slope(_mfi(high, low, close, volume, 14), MDAYS)


def f06_vddu_087_mfi_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of MFI(14)."""
    return _rolling_slope(_mfi(high, low, close, volume, 14), QDAYS)


def f06_vddu_088_cmf_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 21d — drying when near zero/negative."""
    return _cmf(high, low, close, volume, MDAYS)


def f06_vddu_089_cmf_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Chaikin Money Flow over 63d."""
    return _cmf(high, low, close, volume, QDAYS)


def f06_vddu_090_cmf_slope_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """63d slope of CMF(21) — money-flow trend decline."""
    return _rolling_slope(_cmf(high, low, close, volume, MDAYS), QDAYS)


def f06_vddu_091_ease_of_movement_decay_21d(high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """21d slope of ease-of-movement: ((H+L)/2 diff) * (H-L) / volume."""
    mid = (high + low) / 2.0
    box = (high - low) / volume.replace(0, np.nan)
    eom = mid.diff() / box.replace(0, np.nan)
    eom_smooth = eom.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_slope(eom_smooth, MDAYS)


def f06_vddu_092_pvi_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of Positive Volume Index over 21d."""
    pvi = pd.Series(100.0, index=close.index)
    vu = volume > volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vu, chg, 0.0), index=close.index)
    pvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_slope(pvi, MDAYS)


def f06_vddu_093_nvi_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of Negative Volume Index over 21d."""
    vd = volume < volume.shift(1)
    chg = close.pct_change().fillna(0)
    incr = pd.Series(np.where(vd, chg, 0.0), index=close.index)
    nvi = 100.0 * (1.0 + incr).cumprod()
    return _rolling_slope(nvi, MDAYS)


def f06_vddu_094_vroc_21d(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 21d (pct change)."""
    return volume.pct_change(MDAYS)


def f06_vddu_095_vroc_63d(volume: pd.Series) -> pd.Series:
    """Volume rate of change over 63d (pct change)."""
    return volume.pct_change(QDAYS)


def f06_vddu_096_obv_plateau_index_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 - |slope of OBV 21d| / 252d std of OBV — high when flat (plateau)."""
    obv = _obv(close, volume)
    sl = _rolling_slope(obv, MDAYS).abs()
    sd = obv.rolling(YDAYS, min_periods=QDAYS).std().replace(0, np.nan)
    return 1.0 - _safe_div(sl, sd)


def f06_vddu_097_obv_plateau_index_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 - |slope of OBV 63d| / 252d std of OBV."""
    obv = _obv(close, volume)
    sl = _rolling_slope(obv, QDAYS).abs()
    sd = obv.rolling(YDAYS, min_periods=QDAYS).std().replace(0, np.nan)
    return 1.0 - _safe_div(sl, sd)


def f06_vddu_098_ad_line_plateau_index_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """1 - |slope of AD line 63d| / 252d std of AD line."""
    ad = _ad_line(high, low, close, volume)
    sl = _rolling_slope(ad, QDAYS).abs()
    sd = ad.rolling(YDAYS, min_periods=QDAYS).std().replace(0, np.nan)
    return 1.0 - _safe_div(sl, sd)


def f06_vddu_099_cumulative_net_vol_flatness_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Std of (cumulative net vol over 63d) — low when flat / drying."""
    chg = close.diff()
    net = (volume.where(chg > 0).fillna(0)) - (volume.where(chg < 0).fillna(0))
    cum = net.rolling(QDAYS, min_periods=MDAYS).sum()
    return cum.rolling(MDAYS, min_periods=WDAYS).std()


def f06_vddu_100_cumulative_net_vol_cv_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Coefficient of variation of cumulative net vol 63d — high when noisy/dry."""
    chg = close.diff()
    net = (volume.where(chg > 0).fillna(0)) - (volume.where(chg < 0).fillna(0))
    cum = net.rolling(QDAYS, min_periods=MDAYS).sum()
    m = cum.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = cum.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(sd, m.abs())


def f06_vddu_101_avg_dollar_vol_5d_to_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean $-vol 5d / mean $-vol 63d — short-burst capital contraction."""
    dv = close * volume
    return _safe_div(dv.rolling(WDAYS, min_periods=2).mean(), dv.rolling(QDAYS, min_periods=MDAYS).mean())


def f06_vddu_102_dollar_volume_rank_pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of current $-vol within last 252d (low when dry)."""
    dv = close * volume
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
        if not np.isnan(w).any() else np.nan,
        raw=True,
    )


def f06_vddu_103_dollar_volume_herfindahl_drop_21_vs_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Herfindahl of $-vol 21d minus 63d Herfindahl — concentration drop."""
    dv = close * volume
    def _h(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        sh = w / s
        return float(np.sum(sh ** 2))
    h21 = dv.rolling(MDAYS, min_periods=WDAYS).apply(_h, raw=True)
    h63 = dv.rolling(QDAYS, min_periods=MDAYS).apply(_h, raw=True)
    return h21 - h63


def f06_vddu_104_dollar_volume_entropy_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shannon entropy of $-vol shares over 63d (normalized) — high = no concentration."""
    dv = close * volume
    def _e(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        p = w / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum() / np.log(len(w)))
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_e, raw=True)


def f06_vddu_105_days_since_dollar_vol_2x_avg(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since the last bar with $-vol > 2x SMA_252 $-vol."""
    dv = close * volume
    avg = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (dv > 2.0 * avg).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f06_vddu_106_dollar_volume_contraction_at_new_high_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean $-vol on 63d-new-high bars / mean $-vol on all 63d bars."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    nh = (high > prior_max).astype(float)
    dv = close * volume
    nh_mean = _safe_div(
        (dv * nh).rolling(QDAYS, min_periods=MDAYS).sum(),
        nh.rolling(QDAYS, min_periods=MDAYS).sum(),
    )
    return _safe_div(nh_mean, dv.rolling(QDAYS, min_periods=MDAYS).mean())


def f06_vddu_107_low_participation_new_high_count_21d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d with new 21d high AND $-vol below 252d $-vol median."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    dv = close * volume
    med = dv.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (nh & (dv < med)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_vddu_108_dollar_vol_high_vs_low_days_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Avg $-vol on top-50pct return days / bottom-50pct return days over 63d."""
    r = close.pct_change()
    med_r = r.rolling(QDAYS, min_periods=MDAYS).median()
    dv = close * volume
    high_dv = dv.where(r > med_r)
    low_dv = dv.where(r < med_r)
    return _safe_div(
        high_dv.rolling(QDAYS, min_periods=MDAYS).mean(),
        low_dv.rolling(QDAYS, min_periods=MDAYS).mean(),
    )


def f06_vddu_109_top3_dollar_vol_days_share_decline_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-3 bar $-vol share of 63d total — declining = dryup."""
    dv = close * volume
    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        return float(np.sort(w)[-3:].sum() / s)
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_sh, raw=True)


def f06_vddu_110_recent_5d_vs_prior_5d_dollar_vol_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(5d $-vol) / Sum(prior 5d $-vol) — week-over-week contraction."""
    dv = close * volume
    a = dv.rolling(WDAYS, min_periods=2).sum()
    b = dv.shift(WDAYS).rolling(WDAYS, min_periods=2).sum()
    return _safe_div(a, b)


def f06_vddu_111_recent_21d_vs_prior_21d_dollar_vol_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(21d $-vol) / Sum(prior 21d $-vol) — month-over-month contraction."""
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).sum()
    b = dv.shift(MDAYS).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(a, b)


def f06_vddu_112_recent_63d_vs_prior_63d_dollar_vol_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(63d $-vol) / Sum(prior 63d $-vol) — quarter-over-quarter contraction."""
    dv = close * volume
    a = dv.rolling(QDAYS, min_periods=MDAYS).sum()
    b = dv.shift(QDAYS).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(a, b)


def f06_vddu_113_log_dollar_vol_zscore_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of log $-vol over 252d (deep-negative when dry)."""
    return _rolling_zscore(_safe_log(close * volume), YDAYS)


def f06_vddu_114_log_dollar_vol_zscore_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of log $-vol over 63d."""
    return _rolling_zscore(_safe_log(close * volume), QDAYS)


def f06_vddu_115_pct_rank_dollar_vol_21d_mean_in_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Percentile rank of mean-21d $-vol in 252d distribution of mean-21d $-vol."""
    dv = close * volume
    m21 = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    return m21.rolling(YDAYS, min_periods=QDAYS).apply(
        lambda w: (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
        if not np.isnan(w).any() else np.nan,
        raw=True,
    )


def f06_vddu_116_avg_log_dollar_vol_21_vs_252_diff(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean log $-vol 21d minus mean log $-vol 252d."""
    lv = _safe_log(close * volume)
    return lv.rolling(MDAYS, min_periods=WDAYS).mean() - lv.rolling(YDAYS, min_periods=QDAYS).mean()


def f06_vddu_117_dollar_vol_on_rally_bars_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope over 63d of mean $-vol on up-bars (in 21d window)."""
    chg = close.diff()
    dv = close * volume
    rally_dv = dv.where(chg > 0).rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_slope(rally_dv, QDAYS)


def f06_vddu_118_dollar_vol_selloff_vs_rally_relative_rise_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(sum down-bar $-vol over 63d) / (sum up-bar $-vol over 63d) — rising = relative dryup of rally."""
    chg = close.diff()
    dv = close * volume
    up = dv.where(chg > 0).fillna(0).rolling(QDAYS, min_periods=MDAYS).sum()
    dn = dv.where(chg < 0).fillna(0).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(dn, up)


def f06_vddu_119_dollar_vol_cv_21_vs_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """CV(21d $-vol) - CV(63d $-vol)."""
    dv = close * volume
    cv21 = dv.rolling(MDAYS, min_periods=WDAYS).std() / dv.rolling(MDAYS, min_periods=WDAYS).mean().replace(0, np.nan)
    cv63 = dv.rolling(QDAYS, min_periods=MDAYS).std() / dv.rolling(QDAYS, min_periods=MDAYS).mean().replace(0, np.nan)
    return cv21 - cv63


def f06_vddu_120_dollar_vol_gini_decline_21_vs_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gini($-vol over 21d) minus Gini($-vol over 63d) — concentration drop."""
    dv = close * volume
    def _g(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)
        n = len(s)
        tot = s.sum()
        if tot == 0:
            return np.nan
        cum = np.cumsum(s)
        return float((n + 1 - 2 * cum.sum() / cum[-1]) / n)
    g21 = dv.rolling(MDAYS, min_periods=WDAYS).apply(_g, raw=True)
    g63 = dv.rolling(QDAYS, min_periods=MDAYS).apply(_g, raw=True)
    return g21 - g63


def f06_vddu_121_share_bars_dollar_vol_below_half_sma252_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars with $-vol < 0.5 * SMA_252 $-vol."""
    dv = close * volume
    avg = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (dv < 0.5 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_122_share_bars_dollar_vol_below_quarter_sma252_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars with $-vol < 0.25 * SMA_252 $-vol."""
    dv = close * volume
    avg = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (dv < 0.25 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_123_dollar_vol_slope_normalized_by_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol slope over 63d / mean $-vol 63d."""
    dv = close * volume
    sl = _rolling_slope(dv, QDAYS)
    m = dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(sl, m)


def f06_vddu_124_dollar_vol_oscillator_pct_21_63(close: pd.Series, volume: pd.Series) -> pd.Series:
    """(SMA21($-vol) - SMA63($-vol)) / SMA63($-vol) — pct deviation oscillator."""
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    b = dv.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(a - b, b)


def f06_vddu_125_dollar_vol_drying_composite_z_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (-1 * mean 21d $-vol) vs 252d distribution — positive when dry."""
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(-a, YDAYS)


def f06_vddu_126_days_since_vol_above_95pct_252d(volume: pd.Series) -> pd.Series:
    """Bars since last vol exceeded 95th percentile of 252d."""
    p = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (volume >= p).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f06_vddu_127_days_since_dollar_vol_above_95pct_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars since last $-vol exceeded 95th percentile of 252d $-vol."""
    dv = close * volume
    p = dv.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (dv >= p).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f06_vddu_128_longest_low_vol_streak_21d(volume: pd.Series) -> pd.Series:
    """Longest consecutive-low-vol (vol < 252d median) streak length in last 21d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low = (volume < med).astype(int)
    grp = (low == 0).cumsum()
    streak = low.groupby(grp).cumsum()
    return streak.rolling(MDAYS, min_periods=WDAYS).max()


def f06_vddu_129_longest_low_vol_streak_63d(volume: pd.Series) -> pd.Series:
    """Longest consecutive-low-vol streak in last 63d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low = (volume < med).astype(int)
    grp = (low == 0).cumsum()
    streak = low.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=MDAYS).max()


def f06_vddu_130_avg_low_vol_streak_length_63d(volume: pd.Series) -> pd.Series:
    """Mean length of low-vol streaks observed in last 63d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low = (volume < med).astype(int)
    grp = (low == 0).cumsum()
    streak = low.groupby(grp).cumsum()
    return streak.where(low == 1).rolling(QDAYS, min_periods=MDAYS).mean()


def f06_vddu_131_low_vol_cluster_count_5bar_63d(volume: pd.Series) -> pd.Series:
    """Count of >=5-bar low-vol clusters that ended inside last 63d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low = (volume < med).astype(int)
    grp = (low == 0).cumsum()
    streak = low.groupby(grp).cumsum()
    ended_long = ((streak.shift(1) >= 5) & (low == 0)).astype(float)
    return ended_long.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_vddu_132_quietness_ratio_median_21d_to_max_252d(volume: pd.Series) -> pd.Series:
    """Median(21d vol) / Max(252d vol) — quietness vs annual peak."""
    a = volume.rolling(MDAYS, min_periods=WDAYS).median()
    b = volume.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(a, b)


def f06_vddu_133_quietness_ratio_dollar_vol_21_to_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Median(21d $-vol) / Max(252d $-vol)."""
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).median()
    b = dv.rolling(YDAYS, min_periods=QDAYS).max()
    return _safe_div(a, b)


def f06_vddu_134_silent_days_near_top_fraction_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars near 252d high (>=0.95) AND low vol (z<0)."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)) >= 0.95
    z = _rolling_zscore(volume, YDAYS)
    low = z < 0
    flag = (near & low).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_135_silent_days_near_top_fraction_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 63d bars near 252d high AND low vol."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)) >= 0.95
    z = _rolling_zscore(volume, YDAYS)
    low = z < 0
    flag = (near & low).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f06_vddu_136_avg_vol_last_5d_to_breakout_day_vol_63d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol last 5d / vol on most-recent 63d-new-high bar."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = high > prior_max
    bo_vol = volume.where(is_nh).ffill()
    avg5 = volume.rolling(WDAYS, min_periods=2).mean()
    return _safe_div(avg5, bo_vol)


def f06_vddu_137_post_max_vol_decay_rate_63d(volume: pd.Series) -> pd.Series:
    """Linear-regression slope of log-vol over 63d bars POST the 63d-max bar.

    Approximated by negative slope of log-vol over 63d — declining after peak."""
    return _rolling_slope(_safe_log(volume), QDAYS)


def f06_vddu_138_recovery_vs_decline_vol_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean vol on bounces (close>prev close after down bar) / mean vol on declines, 21d."""
    chg = close.diff()
    bounce = (chg > 0) & (chg.shift(1) < 0)
    decline = (chg < 0)
    bv = volume.where(bounce).rolling(MDAYS, min_periods=WDAYS).mean()
    dv = volume.where(decline).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(bv, dv)


def f06_vddu_139_fade_volume_signature_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Negative slope of vol over 21d combined with near-zero abs return over 21d.

    Higher value = volume fading while price holds."""
    sl = _rolling_slope(volume, MDAYS)
    flat = -_safe_log(close).diff(MDAYS).abs()
    return -sl + flat * volume.rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_140_apathy_score_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z(-volume) + Z(-ATR21) — sum of low-vol and low-range z-scores over 21d window."""
    z_v = -_rolling_zscore(volume, YDAYS)
    atr = _atr(high, low, close, MDAYS)
    z_a = -_rolling_zscore(atr, YDAYS)
    return (z_v + z_a).rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_141_apathy_score_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z(-vol) + Z(-ATR21) averaged over 63d."""
    z_v = -_rolling_zscore(volume, YDAYS)
    atr = _atr(high, low, close, MDAYS)
    z_a = -_rolling_zscore(atr, YDAYS)
    return (z_v + z_a).rolling(QDAYS, min_periods=MDAYS).mean()


def f06_vddu_142_low_vol_high_position_bar_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d where close in upper third of range AND vol < 252d median."""
    pos = (close - low) / (high - low).replace(0, np.nan)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((pos >= 2.0 / 3.0) & (volume < med)).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f06_vddu_143_low_vol_high_position_bar_count_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 63d where close in upper third of range AND vol < 252d median."""
    pos = (close - low) / (high - low).replace(0, np.nan)
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    flag = ((pos >= 2.0 / 3.0) & (volume < med)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f06_vddu_144_low_vol_consecutive_new_high_count_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Longest consecutive low-vol new-high streak in last 21d."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low = volume < med
    cond = (nh & low).astype(int)
    grp = (cond == 0).cumsum()
    streak = cond.groupby(grp).cumsum()
    return streak.rolling(MDAYS, min_periods=WDAYS).max()


def f06_vddu_145_consecutive_submedian_vol_max_21d(volume: pd.Series) -> pd.Series:
    """Max length of consecutive sub-median-vol bars inside last 21d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low = (volume < med).astype(int)
    grp = (low == 0).cumsum()
    streak = low.groupby(grp).cumsum()
    return streak.rolling(MDAYS, min_periods=WDAYS).max()


def f06_vddu_146_consecutive_submedian_vol_max_63d(volume: pd.Series) -> pd.Series:
    """Max length of consecutive sub-median-vol bars inside last 63d."""
    med = volume.rolling(YDAYS, min_periods=QDAYS).median()
    low = (volume < med).astype(int)
    grp = (low == 0).cumsum()
    streak = low.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=MDAYS).max()


def f06_vddu_147_effort_vs_result_low_vol_per_pct_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum(21d vol) / sum(21d |log return|) — vol per unit price movement, low = dry."""
    v_sum = volume.rolling(MDAYS, min_periods=WDAYS).sum()
    r_sum = _safe_log(close).diff().abs().rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(v_sum, r_sum)


def f06_vddu_148_quiet_topping_consolidation_score_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean over 21d of: near_high * (1 / (ATR21 * volume_z+1)) — quiet AND elevated."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)).clip(upper=1.0)
    atr = _atr(high, low, close, MDAYS)
    z_v = _rolling_zscore(volume, YDAYS).clip(lower=-3.0, upper=3.0)
    quiet = 1.0 / (atr.replace(0, np.nan) * (z_v + 4.0))
    return (near * quiet).rolling(MDAYS, min_periods=WDAYS).mean()


def f06_vddu_149_quiet_topping_consolidation_score_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 148 but averaged over 63d."""
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)).clip(upper=1.0)
    atr = _atr(high, low, close, MDAYS)
    z_v = _rolling_zscore(volume, YDAYS).clip(lower=-3.0, upper=3.0)
    quiet = 1.0 / (atr.replace(0, np.nan) * (z_v + 4.0))
    return (near * quiet).rolling(QDAYS, min_periods=MDAYS).mean()


def f06_vddu_150_composite_dryup_score_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite: -log(vol contraction ratio) + (-vol z) + days since 63d max vol, averaged 63d."""
    a = volume.rolling(MDAYS, min_periods=WDAYS).mean()
    b = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    contraction = -(_safe_log(a) - _safe_log(b))
    z = -_rolling_zscore(volume, YDAYS)
    def _bsm(w):
        return (len(w) - 1) - int(np.argmax(w))
    days = volume.rolling(QDAYS, min_periods=MDAYS).apply(_bsm, raw=True)
    score = contraction + z + days / float(QDAYS)
    return score.rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
#                        REGISTRY
# ============================================================

VOLUME_DISTRIBUTION_DRYUP_BASE_REGISTRY_076_150 = {
    "f06_vddu_076_ad_line_slope_21d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_076_ad_line_slope_21d},
    "f06_vddu_077_ad_line_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_077_ad_line_slope_63d},
    "f06_vddu_078_obv_slope_21d": {"inputs": ["close", "volume"], "func": f06_vddu_078_obv_slope_21d},
    "f06_vddu_079_obv_slope_63d": {"inputs": ["close", "volume"], "func": f06_vddu_079_obv_slope_63d},
    "f06_vddu_080_obv_price_slope_divergence_63d": {"inputs": ["close", "volume"], "func": f06_vddu_080_obv_price_slope_divergence_63d},
    "f06_vddu_081_ad_price_slope_divergence_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_081_ad_price_slope_divergence_63d},
    "f06_vddu_082_vwap_21d_slope_decay": {"inputs": ["close", "volume"], "func": f06_vddu_082_vwap_21d_slope_decay},
    "f06_vddu_083_dollar_vwap_slope_decay_63d": {"inputs": ["close", "volume"], "func": f06_vddu_083_dollar_vwap_slope_decay_63d},
    "f06_vddu_084_avg_dollar_vol_above_vwap63_decline": {"inputs": ["close", "volume"], "func": f06_vddu_084_avg_dollar_vol_above_vwap63_decline},
    "f06_vddu_085_above_to_below_vwap_vol_ratio_decay_21d": {"inputs": ["close", "volume"], "func": f06_vddu_085_above_to_below_vwap_vol_ratio_decay_21d},
    "f06_vddu_086_mfi_slope_21d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_086_mfi_slope_21d},
    "f06_vddu_087_mfi_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_087_mfi_slope_63d},
    "f06_vddu_088_cmf_21d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_088_cmf_21d},
    "f06_vddu_089_cmf_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_089_cmf_63d},
    "f06_vddu_090_cmf_slope_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_090_cmf_slope_63d},
    "f06_vddu_091_ease_of_movement_decay_21d": {"inputs": ["high", "low", "volume"], "func": f06_vddu_091_ease_of_movement_decay_21d},
    "f06_vddu_092_pvi_slope_21d": {"inputs": ["close", "volume"], "func": f06_vddu_092_pvi_slope_21d},
    "f06_vddu_093_nvi_slope_21d": {"inputs": ["close", "volume"], "func": f06_vddu_093_nvi_slope_21d},
    "f06_vddu_094_vroc_21d": {"inputs": ["volume"], "func": f06_vddu_094_vroc_21d},
    "f06_vddu_095_vroc_63d": {"inputs": ["volume"], "func": f06_vddu_095_vroc_63d},
    "f06_vddu_096_obv_plateau_index_21d": {"inputs": ["close", "volume"], "func": f06_vddu_096_obv_plateau_index_21d},
    "f06_vddu_097_obv_plateau_index_63d": {"inputs": ["close", "volume"], "func": f06_vddu_097_obv_plateau_index_63d},
    "f06_vddu_098_ad_line_plateau_index_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_098_ad_line_plateau_index_63d},
    "f06_vddu_099_cumulative_net_vol_flatness_63d": {"inputs": ["close", "volume"], "func": f06_vddu_099_cumulative_net_vol_flatness_63d},
    "f06_vddu_100_cumulative_net_vol_cv_63d": {"inputs": ["close", "volume"], "func": f06_vddu_100_cumulative_net_vol_cv_63d},
    "f06_vddu_101_avg_dollar_vol_5d_to_63d": {"inputs": ["close", "volume"], "func": f06_vddu_101_avg_dollar_vol_5d_to_63d},
    "f06_vddu_102_dollar_volume_rank_pct_252d": {"inputs": ["close", "volume"], "func": f06_vddu_102_dollar_volume_rank_pct_252d},
    "f06_vddu_103_dollar_volume_herfindahl_drop_21_vs_63": {"inputs": ["close", "volume"], "func": f06_vddu_103_dollar_volume_herfindahl_drop_21_vs_63},
    "f06_vddu_104_dollar_volume_entropy_63d": {"inputs": ["close", "volume"], "func": f06_vddu_104_dollar_volume_entropy_63d},
    "f06_vddu_105_days_since_dollar_vol_2x_avg": {"inputs": ["close", "volume"], "func": f06_vddu_105_days_since_dollar_vol_2x_avg},
    "f06_vddu_106_dollar_volume_contraction_at_new_high_63d": {"inputs": ["high", "close", "volume"], "func": f06_vddu_106_dollar_volume_contraction_at_new_high_63d},
    "f06_vddu_107_low_participation_new_high_count_21d": {"inputs": ["high", "close", "volume"], "func": f06_vddu_107_low_participation_new_high_count_21d},
    "f06_vddu_108_dollar_vol_high_vs_low_days_ratio_63d": {"inputs": ["close", "volume"], "func": f06_vddu_108_dollar_vol_high_vs_low_days_ratio_63d},
    "f06_vddu_109_top3_dollar_vol_days_share_decline_63d": {"inputs": ["close", "volume"], "func": f06_vddu_109_top3_dollar_vol_days_share_decline_63d},
    "f06_vddu_110_recent_5d_vs_prior_5d_dollar_vol_ratio": {"inputs": ["close", "volume"], "func": f06_vddu_110_recent_5d_vs_prior_5d_dollar_vol_ratio},
    "f06_vddu_111_recent_21d_vs_prior_21d_dollar_vol_ratio": {"inputs": ["close", "volume"], "func": f06_vddu_111_recent_21d_vs_prior_21d_dollar_vol_ratio},
    "f06_vddu_112_recent_63d_vs_prior_63d_dollar_vol_ratio": {"inputs": ["close", "volume"], "func": f06_vddu_112_recent_63d_vs_prior_63d_dollar_vol_ratio},
    "f06_vddu_113_log_dollar_vol_zscore_252d": {"inputs": ["close", "volume"], "func": f06_vddu_113_log_dollar_vol_zscore_252d},
    "f06_vddu_114_log_dollar_vol_zscore_63d": {"inputs": ["close", "volume"], "func": f06_vddu_114_log_dollar_vol_zscore_63d},
    "f06_vddu_115_pct_rank_dollar_vol_21d_mean_in_252d": {"inputs": ["close", "volume"], "func": f06_vddu_115_pct_rank_dollar_vol_21d_mean_in_252d},
    "f06_vddu_116_avg_log_dollar_vol_21_vs_252_diff": {"inputs": ["close", "volume"], "func": f06_vddu_116_avg_log_dollar_vol_21_vs_252_diff},
    "f06_vddu_117_dollar_vol_on_rally_bars_slope_63d": {"inputs": ["close", "volume"], "func": f06_vddu_117_dollar_vol_on_rally_bars_slope_63d},
    "f06_vddu_118_dollar_vol_selloff_vs_rally_relative_rise_63d": {"inputs": ["close", "volume"], "func": f06_vddu_118_dollar_vol_selloff_vs_rally_relative_rise_63d},
    "f06_vddu_119_dollar_vol_cv_21_vs_63": {"inputs": ["close", "volume"], "func": f06_vddu_119_dollar_vol_cv_21_vs_63},
    "f06_vddu_120_dollar_vol_gini_decline_21_vs_63": {"inputs": ["close", "volume"], "func": f06_vddu_120_dollar_vol_gini_decline_21_vs_63},
    "f06_vddu_121_share_bars_dollar_vol_below_half_sma252_21d": {"inputs": ["close", "volume"], "func": f06_vddu_121_share_bars_dollar_vol_below_half_sma252_21d},
    "f06_vddu_122_share_bars_dollar_vol_below_quarter_sma252_21d": {"inputs": ["close", "volume"], "func": f06_vddu_122_share_bars_dollar_vol_below_quarter_sma252_21d},
    "f06_vddu_123_dollar_vol_slope_normalized_by_mean_63d": {"inputs": ["close", "volume"], "func": f06_vddu_123_dollar_vol_slope_normalized_by_mean_63d},
    "f06_vddu_124_dollar_vol_oscillator_pct_21_63": {"inputs": ["close", "volume"], "func": f06_vddu_124_dollar_vol_oscillator_pct_21_63},
    "f06_vddu_125_dollar_vol_drying_composite_z_21d": {"inputs": ["close", "volume"], "func": f06_vddu_125_dollar_vol_drying_composite_z_21d},
    "f06_vddu_126_days_since_vol_above_95pct_252d": {"inputs": ["volume"], "func": f06_vddu_126_days_since_vol_above_95pct_252d},
    "f06_vddu_127_days_since_dollar_vol_above_95pct_252d": {"inputs": ["close", "volume"], "func": f06_vddu_127_days_since_dollar_vol_above_95pct_252d},
    "f06_vddu_128_longest_low_vol_streak_21d": {"inputs": ["volume"], "func": f06_vddu_128_longest_low_vol_streak_21d},
    "f06_vddu_129_longest_low_vol_streak_63d": {"inputs": ["volume"], "func": f06_vddu_129_longest_low_vol_streak_63d},
    "f06_vddu_130_avg_low_vol_streak_length_63d": {"inputs": ["volume"], "func": f06_vddu_130_avg_low_vol_streak_length_63d},
    "f06_vddu_131_low_vol_cluster_count_5bar_63d": {"inputs": ["volume"], "func": f06_vddu_131_low_vol_cluster_count_5bar_63d},
    "f06_vddu_132_quietness_ratio_median_21d_to_max_252d": {"inputs": ["volume"], "func": f06_vddu_132_quietness_ratio_median_21d_to_max_252d},
    "f06_vddu_133_quietness_ratio_dollar_vol_21_to_252": {"inputs": ["close", "volume"], "func": f06_vddu_133_quietness_ratio_dollar_vol_21_to_252},
    "f06_vddu_134_silent_days_near_top_fraction_21d": {"inputs": ["high", "volume"], "func": f06_vddu_134_silent_days_near_top_fraction_21d},
    "f06_vddu_135_silent_days_near_top_fraction_63d": {"inputs": ["high", "volume"], "func": f06_vddu_135_silent_days_near_top_fraction_63d},
    "f06_vddu_136_avg_vol_last_5d_to_breakout_day_vol_63d": {"inputs": ["high", "volume"], "func": f06_vddu_136_avg_vol_last_5d_to_breakout_day_vol_63d},
    "f06_vddu_137_post_max_vol_decay_rate_63d": {"inputs": ["volume"], "func": f06_vddu_137_post_max_vol_decay_rate_63d},
    "f06_vddu_138_recovery_vs_decline_vol_ratio_21d": {"inputs": ["close", "volume"], "func": f06_vddu_138_recovery_vs_decline_vol_ratio_21d},
    "f06_vddu_139_fade_volume_signature_21d": {"inputs": ["close", "volume"], "func": f06_vddu_139_fade_volume_signature_21d},
    "f06_vddu_140_apathy_score_21d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_140_apathy_score_21d},
    "f06_vddu_141_apathy_score_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_141_apathy_score_63d},
    "f06_vddu_142_low_vol_high_position_bar_count_21d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_142_low_vol_high_position_bar_count_21d},
    "f06_vddu_143_low_vol_high_position_bar_count_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_143_low_vol_high_position_bar_count_63d},
    "f06_vddu_144_low_vol_consecutive_new_high_count_21d": {"inputs": ["high", "volume"], "func": f06_vddu_144_low_vol_consecutive_new_high_count_21d},
    "f06_vddu_145_consecutive_submedian_vol_max_21d": {"inputs": ["volume"], "func": f06_vddu_145_consecutive_submedian_vol_max_21d},
    "f06_vddu_146_consecutive_submedian_vol_max_63d": {"inputs": ["volume"], "func": f06_vddu_146_consecutive_submedian_vol_max_63d},
    "f06_vddu_147_effort_vs_result_low_vol_per_pct_21d": {"inputs": ["close", "volume"], "func": f06_vddu_147_effort_vs_result_low_vol_per_pct_21d},
    "f06_vddu_148_quiet_topping_consolidation_score_21d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_148_quiet_topping_consolidation_score_21d},
    "f06_vddu_149_quiet_topping_consolidation_score_63d": {"inputs": ["high", "low", "close", "volume"], "func": f06_vddu_149_quiet_topping_consolidation_score_63d},
    "f06_vddu_150_composite_dryup_score_63d": {"inputs": ["close", "volume"], "func": f06_vddu_150_composite_dryup_score_63d},
}
