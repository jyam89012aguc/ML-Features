"""volume_blowoff_at_peak base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continued. Theme: VWAP overshoot, dollar-volume concentration, pattern-level
blowoffs, multi-criteria climax composites.
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


def _rolling_vwap(price, volume, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    num = (price * volume).rolling(n, min_periods=min_periods).sum()
    den = volume.rolling(n, min_periods=min_periods).sum().replace(0, np.nan)
    return num / den


# ============================================================
#                  FEATURES 076-150
# ============================================================

def f05_vbpk_076_anchored_252d_vwap_deviation_z(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (close / 252d-rolling-VWAP - 1) — annual VWAP overshoot."""
    vw = _rolling_vwap(close, volume, YDAYS)
    dev = _safe_div(close, vw) - 1.0
    return _rolling_zscore(dev, YDAYS)


def f05_vbpk_077_anchored_63d_vwap_deviation_z(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (close / 63d-rolling-VWAP - 1)."""
    vw = _rolling_vwap(close, volume, QDAYS)
    dev = _safe_div(close, vw) - 1.0
    return _rolling_zscore(dev, QDAYS)


def f05_vbpk_078_anchored_21d_vwap_deviation_z(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (close / 21d-rolling-VWAP - 1)."""
    vw = _rolling_vwap(close, volume, MDAYS)
    dev = _safe_div(close, vw) - 1.0
    return _rolling_zscore(dev, QDAYS)


def f05_vbpk_079_vwap_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of rolling 63d VWAP series over a 63d window."""
    vw = _rolling_vwap(close, volume, QDAYS)
    return _rolling_slope(vw, QDAYS)


def f05_vbpk_080_vwap_slope_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of rolling 21d VWAP series over a 21d window."""
    vw = _rolling_vwap(close, volume, MDAYS)
    return _rolling_slope(vw, MDAYS)


def f05_vbpk_081_dist_to_vwap_63d_atr_normalized(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - vwap_63d) / ATR(21) — overshoot in volatility units."""
    vw = _rolling_vwap(close, volume, QDAYS)
    atr = _atr(high, low, close, MDAYS)
    return (close - vw) / atr.replace(0, np.nan)


def f05_vbpk_082_dist_to_vwap_21d_atr_normalized(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """(close - vwap_21d) / ATR(21)."""
    vw = _rolling_vwap(close, volume, MDAYS)
    atr = _atr(high, low, close, MDAYS)
    return (close - vw) / atr.replace(0, np.nan)


def f05_vbpk_083_excess_vwap_252d_dollars(close: pd.Series, volume: pd.Series) -> pd.Series:
    """close - 252d rolling vwap — overshoot in raw dollars."""
    vw = _rolling_vwap(close, volume, YDAYS)
    return close - vw


def f05_vbpk_084_cum_vwap_deviation_integral_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum of (close - vwap_63d) over 63d — cumulative overshoot integral."""
    vw = _rolling_vwap(close, volume, QDAYS)
    dev = close - vw
    return dev.rolling(QDAYS, min_periods=MDAYS).sum()


def f05_vbpk_085_pct_bars_closing_above_vwap63_in_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars whose close is above the 63d VWAP."""
    vw = _rolling_vwap(close, volume, QDAYS)
    flag = (close > vw).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f05_vbpk_086_vwap_21d_cross_up_count_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of close-vs-vwap21 upward crosses inside last 63d."""
    vw = _rolling_vwap(close, volume, MDAYS)
    above = (close > vw).astype(int)
    cross_up = ((above == 1) & (above.shift(1) == 0)).astype(float)
    return cross_up.rolling(QDAYS, min_periods=MDAYS).sum()


def f05_vbpk_087_above_vwap_dollar_vol_share_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Share of 63d $-volume traded when close was above 63d VWAP."""
    vw = _rolling_vwap(close, volume, QDAYS)
    dv = close * volume
    above = (close > vw).astype(float)
    return _safe_div(
        (dv * above).rolling(QDAYS, min_periods=MDAYS).sum(),
        dv.rolling(QDAYS, min_periods=MDAYS).sum(),
    )


def f05_vbpk_088_vwap_deviation_peak_z_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of max (close - vwap_21d) over 21d, vs 252d distribution."""
    vw = _rolling_vwap(close, volume, MDAYS)
    dev = close - vw
    peak = dev.rolling(MDAYS, min_periods=WDAYS).max()
    return _rolling_zscore(peak, YDAYS)


def f05_vbpk_089_typical_price_vwap_deviation_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """((H+L+C)/3 - vwap_63d) / vwap_63d — typical-price overshoot."""
    tp = (high + low + close) / 3.0
    vw = _rolling_vwap(tp, volume, QDAYS)
    return _safe_div(tp, vw) - 1.0


def f05_vbpk_090_vwap5_to_vwap63_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """vwap_5d / vwap_63d — 1 — short-term VWAP overshoot vs quarterly base."""
    v5 = _rolling_vwap(close, volume, WDAYS)
    v63 = _rolling_vwap(close, volume, QDAYS)
    return _safe_div(v5, v63) - 1.0


def f05_vbpk_091_vwap21_to_vwap252_ratio(close: pd.Series, volume: pd.Series) -> pd.Series:
    """vwap_21d / vwap_252d - 1 — monthly VWAP regime shift."""
    v21 = _rolling_vwap(close, volume, MDAYS)
    v252 = _rolling_vwap(close, volume, YDAYS)
    return _safe_div(v21, v252) - 1.0


def f05_vbpk_092_vwap_slope_acceleration_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Diff of 63d VWAP slope — slope-of-slope of capital-weighted price."""
    vw = _rolling_vwap(close, volume, QDAYS)
    sl = _rolling_slope(vw, QDAYS)
    return sl.diff()


def f05_vbpk_093_hlc_midpoint_vwap_deviation_63d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """(midpoint - vwap_63d) / vwap_63d, where midpoint = (H+L+C)/3 — robust overshoot."""
    mp = (high + low + close) / 3.0
    vw = _rolling_vwap(close, volume, QDAYS)
    return _safe_div(mp, vw) - 1.0


def f05_vbpk_094_volume_tilt_above_vs_below_vwap_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """( vol above vwap_63d - vol below vwap_63d ) / (sum) over 21d window."""
    vw = _rolling_vwap(close, volume, QDAYS)
    above = (close > vw).astype(float)
    above_v = (volume * above).rolling(MDAYS, min_periods=WDAYS).sum()
    below_v = (volume * (1.0 - above)).rolling(MDAYS, min_periods=WDAYS).sum()
    tot = above_v + below_v
    return _safe_div(above_v - below_v, tot)


def f05_vbpk_095_above_vwap_dollar_vol_ratio_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$ vol above vwap_63d / $ vol below vwap_63d, summed over 63d."""
    vw = _rolling_vwap(close, volume, QDAYS)
    dv = close * volume
    above = (close > vw).astype(float)
    return _safe_div(
        (dv * above).rolling(QDAYS, min_periods=MDAYS).sum(),
        (dv * (1.0 - above)).rolling(QDAYS, min_periods=MDAYS).sum(),
    )


def f05_vbpk_096_log_vwap_deviation_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log(close) - log(vwap_252d) — annual log-overshoot."""
    vw = _rolling_vwap(close, volume, YDAYS)
    return _safe_log(close) - _safe_log(vw)


def f05_vbpk_097_vwap_anchored_at_recent_max_vol_dev_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Close / (mean close over 63d weighted by vol-rank) - 1 — overshoot vs heavily-traded region."""
    vw = _rolling_vwap(close, volume, QDAYS)
    return _safe_div(close, vw) - 1.0


def f05_vbpk_098_anchored_vwap_from_252d_max_day_dev(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Distance of close from anchored-VWAP whose anchor is the 252d-max-high bar.

    The anchor advances only when a new 252d high prints, so the anchor sits at
    the most recent annual peak. Pure right-anchored cumulative — no peeking."""
    rmax = high.shift(1).rolling(YDAYS, min_periods=QDAYS).max()
    is_nh = high > rmax
    cum_pv = (close * volume).cumsum()
    cum_v = volume.cumsum()
    anchor_pv = cum_pv.where(is_nh).ffill()
    anchor_v = cum_v.where(is_nh).ffill()
    num = cum_pv - anchor_pv
    den = (cum_v - anchor_v).replace(0, np.nan)
    avwap = num / den
    return _safe_div(close, avwap) - 1.0


def f05_vbpk_099_anchored_vwap_from_63d_max_day_dev(close: pd.Series, high: pd.Series, volume: pd.Series) -> pd.Series:
    """Same as 098 but anchored at the most recent 63d-max-high bar."""
    rmax = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = high > rmax
    cum_pv = (close * volume).cumsum()
    cum_v = volume.cumsum()
    anchor_pv = cum_pv.where(is_nh).ffill()
    anchor_v = cum_v.where(is_nh).ffill()
    num = cum_pv - anchor_pv
    den = (cum_v - anchor_v).replace(0, np.nan)
    avwap = num / den
    return _safe_div(close, avwap) - 1.0


def f05_vbpk_100_dollar_vwap_deviation_z_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (close - dollar_vwap_252d) — dollar-weighted overshoot z."""
    vw = _rolling_vwap(close, close * volume, YDAYS)
    dev = close - vw
    return _rolling_zscore(dev, YDAYS)


def f05_vbpk_101_dollar_volume_mean_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean $-volume over last 5d — turnover level."""
    return (close * volume).rolling(WDAYS, min_periods=2).mean()


def f05_vbpk_102_dollar_volume_mean_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean $-volume over last 21d."""
    return (close * volume).rolling(MDAYS, min_periods=WDAYS).mean()


def f05_vbpk_103_dollar_volume_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean $-volume over last 63d."""
    return (close * volume).rolling(QDAYS, min_periods=MDAYS).mean()


def f05_vbpk_104_dollar_volume_momentum_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """21d log-change of (close*volume)."""
    return _safe_log(close * volume).diff(MDAYS)


def f05_vbpk_105_dollar_volume_slope_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Linear-regression slope of $-volume over 63d."""
    return _rolling_slope(close * volume, QDAYS)


def f05_vbpk_106_dollar_volume_herfindahl_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Herfindahl concentration of $-vol distribution over 63d (sum of squared shares)."""
    dv = close * volume
    def _h(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        sh = w / s
        return float(np.sum(sh ** 2))
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_h, raw=True)


def f05_vbpk_107_dollar_volume_gini_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Gini coefficient of $-vol distribution over 63d."""
    dv = close * volume
    def _g(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)
        n = len(s)
        if s.sum() == 0:
            return np.nan
        cum = np.cumsum(s)
        return float((n + 1 - 2 * cum.sum() / cum[-1]) / n)
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_g, raw=True)


def f05_vbpk_108_peak_dollar_volume_ratio_to_mean_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Max($-vol) / mean($-vol) over 63d — single-bar capital spike."""
    dv = close * volume
    return _safe_div(dv.rolling(QDAYS, min_periods=MDAYS).max(), dv.rolling(QDAYS, min_periods=MDAYS).mean())


def f05_vbpk_109_top5_dollar_volume_share_of_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-5-bar $-vol share of total 63d $-vol — capital concentration."""
    dv = close * volume
    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        return float(np.sort(w)[-5:].sum() / s)
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_sh, raw=True)


def f05_vbpk_110_top10_dollar_volume_share_of_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Top-10-bar $-vol share of total 252d $-vol."""
    dv = close * volume
    def _sh(w):
        if np.isnan(w).any():
            return np.nan
        s = w.sum()
        if s == 0:
            return np.nan
        return float(np.sort(w)[-10:].sum() / s)
    return dv.rolling(YDAYS, min_periods=QDAYS).apply(_sh, raw=True)


def f05_vbpk_111_log_dollar_volume_range_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """log(max $-vol / min $-vol) over 63d — log-spread of capital activity."""
    dv = close * volume
    return _safe_log(dv.rolling(QDAYS, min_periods=MDAYS).max()) - _safe_log(dv.rolling(QDAYS, min_periods=MDAYS).min())


def f05_vbpk_112_dollar_volume_green_vs_red_ratio_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum($-vol on up bars) / Sum($-vol on down bars) in 21d."""
    dv = close * volume
    chg = close.diff()
    up = (dv.where(chg > 0)).fillna(0)
    dn = (dv.where(chg < 0)).fillna(0)
    return _safe_div(up.rolling(MDAYS, min_periods=WDAYS).sum(), dn.rolling(MDAYS, min_periods=WDAYS).sum())


def f05_vbpk_113_dollar_volume_on_new_high_bars_ratio_63d(high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum($-vol on 63d-new-high bars) / Sum($-vol on other bars) in 63d."""
    prior_max = high.shift(1).rolling(QDAYS, min_periods=MDAYS).max()
    is_nh = (high > prior_max).astype(float)
    dv = close * volume
    return _safe_div(
        (dv * is_nh).rolling(QDAYS, min_periods=MDAYS).sum(),
        (dv * (1.0 - is_nh)).rolling(QDAYS, min_periods=MDAYS).sum(),
    )


def f05_vbpk_114_dollar_volume_per_pct_gained_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum($-vol over 21d) / abs(21d log-return) — capital required per move."""
    dv_sum = (close * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    r = _safe_log(close).diff(MDAYS).abs()
    return _safe_div(dv_sum, r)


def f05_vbpk_115_dollar_volume_per_atr_move_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum($-vol over 21d) / sum(ATR over 21d) — $-vol per unit of true-range."""
    dv_sum = (close * volume).rolling(MDAYS, min_periods=WDAYS).sum()
    tr_sum = _true_range(high, low, close).rolling(MDAYS, min_periods=WDAYS).sum()
    return _safe_div(dv_sum, tr_sum)


def f05_vbpk_116_coefficient_of_variation_volume_63d(volume: pd.Series) -> pd.Series:
    """Std/mean of volume over 63d — CV of participation intensity."""
    m = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    sd = volume.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(sd, m)


def f05_vbpk_117_variance_log_volume_63d(volume: pd.Series) -> pd.Series:
    """Variance of log volume over 63d — log-space dispersion."""
    return _safe_log(volume).rolling(QDAYS, min_periods=MDAYS).var()


def f05_vbpk_118_turnover_proxy_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum($-vol over 63d) / mean(close * 63d) — turnover-like proxy."""
    dv_sum = (close * volume).rolling(QDAYS, min_periods=MDAYS).sum()
    c_mean = close.rolling(QDAYS, min_periods=MDAYS).mean()
    return _safe_div(dv_sum, c_mean)


def f05_vbpk_119_dollar_volume_zscore_log_252d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of log($-vol) over 252d."""
    return _rolling_zscore(_safe_log(close * volume), YDAYS)


def f05_vbpk_120_dollar_volume_on_biggest_gain_z_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """$-vol on the highest-return bar in last 21d, z-scored vs 252d $-vol distribution."""
    r = close.pct_change()
    dv = close * volume
    def _f(w_ret, w_dv):
        if np.isnan(w_ret).any() or np.isnan(w_dv).any():
            return np.nan
        return float(w_dv[int(np.argmax(w_ret))])
    peak_dv = pd.Series(
        [
            _f(r.iloc[max(0, i - MDAYS + 1):i + 1].values, dv.iloc[max(0, i - MDAYS + 1):i + 1].values)
            if i >= WDAYS else np.nan
            for i in range(len(r))
        ],
        index=r.index,
    )
    m = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = dv.rolling(YDAYS, min_periods=QDAYS).std()
    return (peak_dv - m) / sd.replace(0, np.nan)


def f05_vbpk_121_dollar_volume_velocity_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Slope of $-vol over 21d, divided by 21d mean $-vol — normalized velocity."""
    dv = close * volume
    sl = _rolling_slope(dv, MDAYS)
    m = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(sl, m)


def f05_vbpk_122_dollar_volume_regime_shift_21_vs_252(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Log(mean 21d $-vol / mean 252d $-vol) — capital-flow regime shift."""
    dv = close * volume
    a = dv.rolling(MDAYS, min_periods=WDAYS).mean()
    b = dv.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_log(a) - _safe_log(b)


def f05_vbpk_123_dollar_volume_runoff_z_21d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of max(21d $-vol) vs 252d $-vol distribution."""
    dv = close * volume
    peak = dv.rolling(MDAYS, min_periods=WDAYS).max()
    return _rolling_zscore(peak, YDAYS)


def f05_vbpk_124_dollar_volume_single_bar_peak_z_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of max(63d $-vol) vs 252d $-vol distribution."""
    dv = close * volume
    peak = dv.rolling(QDAYS, min_periods=MDAYS).max()
    return _rolling_zscore(peak, YDAYS)


def f05_vbpk_125_dollar_volume_skewness_63d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Skewness of $-vol distribution over 63d — right-tail dominance."""
    dv = close * volume
    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / (sd ** 3))
    return dv.rolling(QDAYS, min_periods=MDAYS).apply(_sk, raw=True)


def f05_vbpk_126_gap_up_high_vol_reversal_count_21d(open_: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in last 21d that gap up open > prior high, then close below open, on >2x avg vol."""
    gap_up = open_ > high.shift(1)
    reverse = close < open_
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (gap_up & reverse & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_127_gap_up_close_below_open_high_vol_21d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in last 21d with open > prior close, close < open, on >2x sma_63 vol — failed gap-up."""
    gap_up = open_ > close.shift(1)
    reverse = close < open_
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 2.0 * avg
    flag = (gap_up & reverse & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_128_shooting_star_high_vol_count_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Shooting star (small body, long upper wick) on >2x avg vol in last 21d."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    upper = high - close.clip(lower=open_)
    body_small = body / rng < 0.3
    wick_long = upper / rng > 0.6
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (body_small & wick_long & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_129_bearish_engulf_high_vol_count_63d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bearish engulfing (prior up, current down engulfs body) on >2x sma_63 vol in last 63d."""
    prev_up = close.shift(1) > open_.shift(1)
    cur_down = close < open_
    engulf = (open_ > close.shift(1)) & (close < open_.shift(1))
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 2.0 * avg
    flag = (prev_up & cur_down & engulf & big).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f05_vbpk_130_wide_range_high_vol_bar_count_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d with (H-L)/ATR21 > 2 AND volume z > 2."""
    atr = _atr(high, low, close, MDAYS)
    wide = (high - low) / atr.replace(0, np.nan) > 2.0
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (wide & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_131_wide_range_up_bar_count_5d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Wide-range up bars (close>open AND H-L > 1.5*ATR21) in last 5d."""
    atr = _atr(high, low, close, MDAYS)
    wide = (high - low) > 1.5 * atr
    up = close > open_
    flag = (wide & up).astype(float)
    return flag.rolling(WDAYS, min_periods=2).sum()


def f05_vbpk_132_avg_high_vol_up_bar_range_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean (H-L) over last 21d on bars where close>open AND vol > 2x sma_63."""
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 2.0 * avg
    up = close > open_
    rng = (high - low).where(big & up)
    return rng.rolling(MDAYS, min_periods=WDAYS).mean()


def f05_vbpk_133_avg_high_vol_up_bar_close_position_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean (close-low)/(high-low) on bars where close>open AND vol > 2x sma_63, over 21d."""
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 2.0 * avg
    up = close > open_
    pos = ((close - low) / (high - low).replace(0, np.nan)).where(big & up)
    return pos.rolling(MDAYS, min_periods=WDAYS).mean()


def f05_vbpk_134_doji_on_max_vol_bar_count_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bars in 21d with |close-open|/(H-L)<0.1 AND volume z > 2 — doji on heavy volume."""
    body = (close - open_).abs()
    rng = (high - low).replace(0, np.nan)
    doji = body / rng < 0.1
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (doji & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_135_high_vol_upthrust_count_21d(open_: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Upthrust: close<open AND new 21d high AND volume > 2x sma_252, in last 21d."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    reverse = close < open_
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (nh & reverse & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_136_exhaustion_gap_at_new_high_count_21d(open_: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Exhaustion gap: gap up open above prior high, new 21d high, vol > 3x sma_63, close < midbar."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    gap = open_ > high.shift(1)
    avg = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big = volume > 3.0 * avg
    weak_close = (close - open_) < 0
    flag = (nh & gap & big & weak_close).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_137_churning_bar_count_21d(open_: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Churning: vol > 2x sma_63 AND (H-L)/ATR21 < 0.8 — large vol, small range."""
    avg_v = volume.rolling(QDAYS, min_periods=MDAYS).mean()
    big_v = volume > 2.0 * avg_v
    atr = _atr(high, low, close, MDAYS)
    narrow = (high - low) / atr.replace(0, np.nan) < 0.8
    flag = (big_v & narrow).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_138_low_progress_high_vol_up_bar_count_21d(open_: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Up bars where close-open / open < 0.005 (low progress) AND vol z>2, in 21d."""
    rel = (close - open_) / open_.replace(0, np.nan)
    weak = (rel > 0) & (rel < 0.005)
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    flag = (weak & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_139_cluster_2sigma_vol_bars_in_21d(volume: pd.Series) -> pd.Series:
    """Count of >2-sigma volume bars in last 21d that are immediately preceded by another >2σ bar."""
    z = _rolling_zscore(volume, YDAYS)
    big = z > 2.0
    cluster = (big & big.shift(1).fillna(False)).astype(float)
    return cluster.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_140_consecutive_2sigma_vol_max_63d(volume: pd.Series) -> pd.Series:
    """Longest consecutive >2-sigma vol streak inside last 63d."""
    z = _rolling_zscore(volume, YDAYS)
    big = (z > 2.0).astype(int)
    grp = (big == 0).cumsum()
    streak = big.groupby(grp).cumsum()
    return streak.rolling(QDAYS, min_periods=MDAYS).max()


def f05_vbpk_141_composite_blowoff_cluster_index_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Sum over 21d of (vol_z * near_high_indicator) where near_high = high/252d-max >= 0.97."""
    z = _rolling_zscore(volume, YDAYS).clip(lower=0)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = (high / rmax.replace(0, np.nan)) >= 0.97
    score = z * near.astype(float)
    return score.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_142_peak_3sigma_vol_in_5d(volume: pd.Series) -> pd.Series:
    """Indicator: any bar in last 5d had volume z > 3 — fresh-week climax flag."""
    z = _rolling_zscore(volume, YDAYS)
    big = (z > 3.0).astype(float)
    return big.rolling(WDAYS, min_periods=2).max()


def f05_vbpk_143_peak_3sigma_vol_in_21d(volume: pd.Series) -> pd.Series:
    """Indicator: any bar in last 21d had volume z > 3."""
    z = _rolling_zscore(volume, YDAYS)
    big = (z > 3.0).astype(float)
    return big.rolling(MDAYS, min_periods=WDAYS).max()


def f05_vbpk_144_multi_bar_reversal_post_climax_5d(close: pd.Series, volume: pd.Series) -> pd.Series:
    """5d log return immediately after a >3σ vol bar (using shifted condition).

    Outputs the trailing-5d log return on bars where a >3σ volume bar occurred 5 bars ago.
    Captures post-climax downside follow-through."""
    z = _rolling_zscore(volume, YDAYS)
    climax_5d_ago = (z.shift(WDAYS) > 3.0)
    ret_5d = _safe_log(close).diff(WDAYS)
    return ret_5d.where(climax_5d_ago)


def f05_vbpk_145_bull_trap_signature_21d(open_: pd.Series, high: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Bull-trap: new 21d high AND close < open AND vol > 2x sma_252 — count in 21d."""
    prior_max = high.shift(1).rolling(MDAYS, min_periods=WDAYS).max()
    nh = high > prior_max
    weak = close < open_
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    big = volume > 2.0 * avg
    flag = (nh & weak & big).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).sum()


def f05_vbpk_146_pct_21d_bars_vol_2x_sma252(volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars with volume > 2x sma_252."""
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume > 2.0 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f05_vbpk_147_pct_21d_bars_vol_5x_sma252(volume: pd.Series) -> pd.Series:
    """Fraction of last 21d bars with volume > 5x sma_252 — extreme blowoff bars."""
    avg = volume.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (volume > 5.0 * avg).astype(float)
    return flag.rolling(MDAYS, min_periods=WDAYS).mean()


def f05_vbpk_148_nearby_high_climax_composite_z_21d(high: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of mean( vol_z * near_max_pct ) over last 21d, vs 252d distribution."""
    z = _rolling_zscore(volume, YDAYS)
    rmax = high.rolling(YDAYS, min_periods=QDAYS).max()
    near = high / rmax.replace(0, np.nan)
    score = z * near
    m21 = score.rolling(MDAYS, min_periods=WDAYS).mean()
    return _rolling_zscore(m21, YDAYS)


def f05_vbpk_149_blowoff_escalation_score_21d(volume: pd.Series) -> pd.Series:
    """Sign-consistent positive vol-slope acceleration: slope of log-vol over 5d - slope over 21d."""
    lv = _safe_log(volume)
    s5 = _rolling_slope(lv, WDAYS)
    s21 = _rolling_slope(lv, MDAYS)
    return s5 - s21


def f05_vbpk_150_multi_criteria_blowoff_score_21d(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Composite z: vol_z + (H-L)/ATR21 + (close-low)/(H-L) - 1, averaged over 21d."""
    z = _rolling_zscore(volume, YDAYS)
    atr = _atr(high, low, close, MDAYS)
    rng = (high - low)
    rng_norm = rng / atr.replace(0, np.nan)
    pos = (close - low) / rng.replace(0, np.nan)
    score = z + rng_norm + (pos - 1.0)
    return score.rolling(MDAYS, min_periods=WDAYS).mean()


# ============================================================
#                        REGISTRY
# ============================================================

VOLUME_BLOWOFF_AT_PEAK_BASE_REGISTRY_076_150 = {
    "f05_vbpk_076_anchored_252d_vwap_deviation_z": {"inputs": ["close", "volume"], "func": f05_vbpk_076_anchored_252d_vwap_deviation_z},
    "f05_vbpk_077_anchored_63d_vwap_deviation_z": {"inputs": ["close", "volume"], "func": f05_vbpk_077_anchored_63d_vwap_deviation_z},
    "f05_vbpk_078_anchored_21d_vwap_deviation_z": {"inputs": ["close", "volume"], "func": f05_vbpk_078_anchored_21d_vwap_deviation_z},
    "f05_vbpk_079_vwap_slope_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_079_vwap_slope_63d},
    "f05_vbpk_080_vwap_slope_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_080_vwap_slope_21d},
    "f05_vbpk_081_dist_to_vwap_63d_atr_normalized": {"inputs": ["close", "high", "low", "volume"], "func": f05_vbpk_081_dist_to_vwap_63d_atr_normalized},
    "f05_vbpk_082_dist_to_vwap_21d_atr_normalized": {"inputs": ["close", "high", "low", "volume"], "func": f05_vbpk_082_dist_to_vwap_21d_atr_normalized},
    "f05_vbpk_083_excess_vwap_252d_dollars": {"inputs": ["close", "volume"], "func": f05_vbpk_083_excess_vwap_252d_dollars},
    "f05_vbpk_084_cum_vwap_deviation_integral_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_084_cum_vwap_deviation_integral_63d},
    "f05_vbpk_085_pct_bars_closing_above_vwap63_in_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_085_pct_bars_closing_above_vwap63_in_21d},
    "f05_vbpk_086_vwap_21d_cross_up_count_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_086_vwap_21d_cross_up_count_63d},
    "f05_vbpk_087_above_vwap_dollar_vol_share_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_087_above_vwap_dollar_vol_share_63d},
    "f05_vbpk_088_vwap_deviation_peak_z_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_088_vwap_deviation_peak_z_21d},
    "f05_vbpk_089_typical_price_vwap_deviation_63d": {"inputs": ["high", "low", "close", "volume"], "func": f05_vbpk_089_typical_price_vwap_deviation_63d},
    "f05_vbpk_090_vwap5_to_vwap63_ratio": {"inputs": ["close", "volume"], "func": f05_vbpk_090_vwap5_to_vwap63_ratio},
    "f05_vbpk_091_vwap21_to_vwap252_ratio": {"inputs": ["close", "volume"], "func": f05_vbpk_091_vwap21_to_vwap252_ratio},
    "f05_vbpk_092_vwap_slope_acceleration_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_092_vwap_slope_acceleration_63d},
    "f05_vbpk_093_hlc_midpoint_vwap_deviation_63d": {"inputs": ["high", "low", "close", "volume"], "func": f05_vbpk_093_hlc_midpoint_vwap_deviation_63d},
    "f05_vbpk_094_volume_tilt_above_vs_below_vwap_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_094_volume_tilt_above_vs_below_vwap_21d},
    "f05_vbpk_095_above_vwap_dollar_vol_ratio_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_095_above_vwap_dollar_vol_ratio_63d},
    "f05_vbpk_096_log_vwap_deviation_252d": {"inputs": ["close", "volume"], "func": f05_vbpk_096_log_vwap_deviation_252d},
    "f05_vbpk_097_vwap_anchored_at_recent_max_vol_dev_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_097_vwap_anchored_at_recent_max_vol_dev_63d},
    "f05_vbpk_098_anchored_vwap_from_252d_max_day_dev": {"inputs": ["close", "high", "volume"], "func": f05_vbpk_098_anchored_vwap_from_252d_max_day_dev},
    "f05_vbpk_099_anchored_vwap_from_63d_max_day_dev": {"inputs": ["close", "high", "volume"], "func": f05_vbpk_099_anchored_vwap_from_63d_max_day_dev},
    "f05_vbpk_100_dollar_vwap_deviation_z_252d": {"inputs": ["close", "volume"], "func": f05_vbpk_100_dollar_vwap_deviation_z_252d},
    "f05_vbpk_101_dollar_volume_mean_5d": {"inputs": ["close", "volume"], "func": f05_vbpk_101_dollar_volume_mean_5d},
    "f05_vbpk_102_dollar_volume_mean_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_102_dollar_volume_mean_21d},
    "f05_vbpk_103_dollar_volume_mean_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_103_dollar_volume_mean_63d},
    "f05_vbpk_104_dollar_volume_momentum_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_104_dollar_volume_momentum_21d},
    "f05_vbpk_105_dollar_volume_slope_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_105_dollar_volume_slope_63d},
    "f05_vbpk_106_dollar_volume_herfindahl_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_106_dollar_volume_herfindahl_63d},
    "f05_vbpk_107_dollar_volume_gini_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_107_dollar_volume_gini_63d},
    "f05_vbpk_108_peak_dollar_volume_ratio_to_mean_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_108_peak_dollar_volume_ratio_to_mean_63d},
    "f05_vbpk_109_top5_dollar_volume_share_of_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_109_top5_dollar_volume_share_of_63d},
    "f05_vbpk_110_top10_dollar_volume_share_of_252d": {"inputs": ["close", "volume"], "func": f05_vbpk_110_top10_dollar_volume_share_of_252d},
    "f05_vbpk_111_log_dollar_volume_range_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_111_log_dollar_volume_range_63d},
    "f05_vbpk_112_dollar_volume_green_vs_red_ratio_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_112_dollar_volume_green_vs_red_ratio_21d},
    "f05_vbpk_113_dollar_volume_on_new_high_bars_ratio_63d": {"inputs": ["high", "close", "volume"], "func": f05_vbpk_113_dollar_volume_on_new_high_bars_ratio_63d},
    "f05_vbpk_114_dollar_volume_per_pct_gained_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_114_dollar_volume_per_pct_gained_21d},
    "f05_vbpk_115_dollar_volume_per_atr_move_21d": {"inputs": ["high", "low", "close", "volume"], "func": f05_vbpk_115_dollar_volume_per_atr_move_21d},
    "f05_vbpk_116_coefficient_of_variation_volume_63d": {"inputs": ["volume"], "func": f05_vbpk_116_coefficient_of_variation_volume_63d},
    "f05_vbpk_117_variance_log_volume_63d": {"inputs": ["volume"], "func": f05_vbpk_117_variance_log_volume_63d},
    "f05_vbpk_118_turnover_proxy_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_118_turnover_proxy_63d},
    "f05_vbpk_119_dollar_volume_zscore_log_252d": {"inputs": ["close", "volume"], "func": f05_vbpk_119_dollar_volume_zscore_log_252d},
    "f05_vbpk_120_dollar_volume_on_biggest_gain_z_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_120_dollar_volume_on_biggest_gain_z_21d},
    "f05_vbpk_121_dollar_volume_velocity_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_121_dollar_volume_velocity_21d},
    "f05_vbpk_122_dollar_volume_regime_shift_21_vs_252": {"inputs": ["close", "volume"], "func": f05_vbpk_122_dollar_volume_regime_shift_21_vs_252},
    "f05_vbpk_123_dollar_volume_runoff_z_21d": {"inputs": ["close", "volume"], "func": f05_vbpk_123_dollar_volume_runoff_z_21d},
    "f05_vbpk_124_dollar_volume_single_bar_peak_z_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_124_dollar_volume_single_bar_peak_z_63d},
    "f05_vbpk_125_dollar_volume_skewness_63d": {"inputs": ["close", "volume"], "func": f05_vbpk_125_dollar_volume_skewness_63d},
    "f05_vbpk_126_gap_up_high_vol_reversal_count_21d": {"inputs": ["open", "high", "close", "volume"], "func": f05_vbpk_126_gap_up_high_vol_reversal_count_21d},
    "f05_vbpk_127_gap_up_close_below_open_high_vol_21d": {"inputs": ["open", "close", "volume"], "func": f05_vbpk_127_gap_up_close_below_open_high_vol_21d},
    "f05_vbpk_128_shooting_star_high_vol_count_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f05_vbpk_128_shooting_star_high_vol_count_21d},
    "f05_vbpk_129_bearish_engulf_high_vol_count_63d": {"inputs": ["open", "close", "volume"], "func": f05_vbpk_129_bearish_engulf_high_vol_count_63d},
    "f05_vbpk_130_wide_range_high_vol_bar_count_21d": {"inputs": ["high", "low", "close", "volume"], "func": f05_vbpk_130_wide_range_high_vol_bar_count_21d},
    "f05_vbpk_131_wide_range_up_bar_count_5d": {"inputs": ["open", "high", "low", "close"], "func": f05_vbpk_131_wide_range_up_bar_count_5d},
    "f05_vbpk_132_avg_high_vol_up_bar_range_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f05_vbpk_132_avg_high_vol_up_bar_range_21d},
    "f05_vbpk_133_avg_high_vol_up_bar_close_position_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f05_vbpk_133_avg_high_vol_up_bar_close_position_21d},
    "f05_vbpk_134_doji_on_max_vol_bar_count_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f05_vbpk_134_doji_on_max_vol_bar_count_21d},
    "f05_vbpk_135_high_vol_upthrust_count_21d": {"inputs": ["open", "high", "close", "volume"], "func": f05_vbpk_135_high_vol_upthrust_count_21d},
    "f05_vbpk_136_exhaustion_gap_at_new_high_count_21d": {"inputs": ["open", "high", "close", "volume"], "func": f05_vbpk_136_exhaustion_gap_at_new_high_count_21d},
    "f05_vbpk_137_churning_bar_count_21d": {"inputs": ["open", "high", "low", "close", "volume"], "func": f05_vbpk_137_churning_bar_count_21d},
    "f05_vbpk_138_low_progress_high_vol_up_bar_count_21d": {"inputs": ["open", "close", "volume"], "func": f05_vbpk_138_low_progress_high_vol_up_bar_count_21d},
    "f05_vbpk_139_cluster_2sigma_vol_bars_in_21d": {"inputs": ["volume"], "func": f05_vbpk_139_cluster_2sigma_vol_bars_in_21d},
    "f05_vbpk_140_consecutive_2sigma_vol_max_63d": {"inputs": ["volume"], "func": f05_vbpk_140_consecutive_2sigma_vol_max_63d},
    "f05_vbpk_141_composite_blowoff_cluster_index_21d": {"inputs": ["high", "volume"], "func": f05_vbpk_141_composite_blowoff_cluster_index_21d},
    "f05_vbpk_142_peak_3sigma_vol_in_5d": {"inputs": ["volume"], "func": f05_vbpk_142_peak_3sigma_vol_in_5d},
    "f05_vbpk_143_peak_3sigma_vol_in_21d": {"inputs": ["volume"], "func": f05_vbpk_143_peak_3sigma_vol_in_21d},
    "f05_vbpk_144_multi_bar_reversal_post_climax_5d": {"inputs": ["close", "volume"], "func": f05_vbpk_144_multi_bar_reversal_post_climax_5d},
    "f05_vbpk_145_bull_trap_signature_21d": {"inputs": ["open", "high", "close", "volume"], "func": f05_vbpk_145_bull_trap_signature_21d},
    "f05_vbpk_146_pct_21d_bars_vol_2x_sma252": {"inputs": ["volume"], "func": f05_vbpk_146_pct_21d_bars_vol_2x_sma252},
    "f05_vbpk_147_pct_21d_bars_vol_5x_sma252": {"inputs": ["volume"], "func": f05_vbpk_147_pct_21d_bars_vol_5x_sma252},
    "f05_vbpk_148_nearby_high_climax_composite_z_21d": {"inputs": ["high", "volume"], "func": f05_vbpk_148_nearby_high_climax_composite_z_21d},
    "f05_vbpk_149_blowoff_escalation_score_21d": {"inputs": ["volume"], "func": f05_vbpk_149_blowoff_escalation_score_21d},
    "f05_vbpk_150_multi_criteria_blowoff_score_21d": {"inputs": ["high", "low", "close", "volume"], "func": f05_vbpk_150_multi_criteria_blowoff_score_21d},
}
