"""40_atr_expansion_dynamics d2 features 526-600 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import math
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260

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
    idx = num.index if hasattr(num, 'index') else None
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

def _ema(s, n):
    return s.ewm(span=n, min_periods=n, adjust=False).mean()

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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f40_atxd_526_tr_volume_logs_corr_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(log TR, log volume) over 252d (log-scale coupling)."""
    return _safe_log(_true_range(high, low, close)).rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(volume)).diff().diff()

def f40_atxd_527_tr_volume_zscore_corr_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(TR z-score, volume z-score) over 252d."""
    tr_z = _rolling_zscore(_true_range(high, low, close), YDAYS)
    v_z = _rolling_zscore(volume, YDAYS)
    return tr_z.rolling(YDAYS, min_periods=QDAYS).corr(v_z).diff().diff()

def f40_atxd_528_tr_after_volume_spike_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean TR in 5 bars after volume_z > 3 events over 252d (post-vol-spike range)."""
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    spike_lag = (vz.shift(WDAYS) > 3.0).fillna(False)
    tr = _true_range(high, low, close)
    return tr.where(spike_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_529_volume_after_tr_spike_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume in 5 bars after TR > 3·ATR(21) events over 252d (post-range-spike volume)."""
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    spike_lag = (tr.shift(WDAYS) > 3 * atr_lag.shift(WDAYS)).fillna(False)
    return volume.where(spike_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_530_tr_volume_joint_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean (TR-z + volume-z) over 21d — composite vol+range z-score."""
    tr_z = _rolling_zscore(_true_range(high, low, close), YDAYS)
    v_z = _rolling_zscore(volume, YDAYS)
    return (tr_z + v_z).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f40_atxd_531_high_tr_high_vol_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars where TR > 252d p75 AND volume > 252d p75, over 63d."""
    tr = _true_range(high, low, close)
    tr_p75 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    v_p75 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    return ((tr > tr_p75) & (volume > v_p75)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f40_atxd_532_high_tr_low_vol_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars where TR > 252d p75 AND volume < 252d p25 — divergent range/volume, 63d."""
    tr = _true_range(high, low, close)
    tr_p75 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    v_p25 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.25).shift(1)
    return ((tr > tr_p75) & (volume < v_p25)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f40_atxd_533_low_tr_high_vol_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars where TR < 252d p25 AND volume > 252d p75 over 63d (suppressed range, surging vol)."""
    tr = _true_range(high, low, close)
    tr_p25 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.25).shift(1)
    v_p75 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    return ((tr < tr_p25) & (volume > v_p75)).astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f40_atxd_534_dollar_range_volume_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Z-score of (TR·close·volume) — dollar-range-volume over 252d."""
    dvr = _true_range(high, low, close) * close * volume
    return _rolling_zscore(dvr, YDAYS).diff().diff()

def f40_atxd_535_atr_per_dollar_traded_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """ATR(21) / mean(close·volume) over 21d (ATR per dollar traded)."""
    a = _atr(high, low, close, MDAYS)
    dv = (close * volume).rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(a, dv).diff().diff()

def f40_atxd_536_range_volume_cov_5d_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Rolling 252d mean of (TR·volume) − (mean TR)·(mean volume) over 5d (5d covariance proxy)."""
    tr = _true_range(high, low, close)
    cov5 = (tr * volume).rolling(WDAYS, min_periods=2).mean() - tr.rolling(WDAYS, min_periods=2).mean() * volume.rolling(WDAYS, min_periods=2).mean()
    return cov5.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_537_volume_per_unit_range_21d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean volume / TR over 21d (volume per unit of range — liquidity proxy)."""
    return _safe_div(volume, _true_range(high, low, close)).rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f40_atxd_538_tr_volume_signed_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Σ(TR · sign(r) · volume) over 21d (signed range-volume flow)."""
    r = close.diff()
    tr = _true_range(high, low, close)
    return (tr * np.sign(r) * volume).rolling(MDAYS, min_periods=WDAYS).sum().diff().diff()

def f40_atxd_539_volume_weighted_tr_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Σ(TR · volume) / Σ volume over 252d (volume-weighted ATR-style)."""
    tr = _true_range(high, low, close)
    return _safe_div((tr * volume).rolling(YDAYS, min_periods=QDAYS).sum(), volume.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f40_atxd_540_corr_atr_vol_change_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(ΔATR, Δvolume) over 252d."""
    return _atr(high, low, close, MDAYS).diff().rolling(YDAYS, min_periods=QDAYS).corr(volume.diff()).diff().diff()

def f40_atxd_541_consecutive_higher_tr_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR > TR.shift(1) AND TR.shift(1) > TR.shift(2) (2-bar TR rise) over 252d."""
    tr = _true_range(high, low, close)
    pattern = (tr > tr.shift(1)) & (tr.shift(1) > tr.shift(2))
    return pattern.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_542_consecutive_lower_tr_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR < TR.shift(1) AND TR.shift(1) < TR.shift(2) (2-bar TR fall) over 252d."""
    tr = _true_range(high, low, close)
    pattern = (tr < tr.shift(1)) & (tr.shift(1) < tr.shift(2))
    return pattern.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_543_atr_double_in_5d_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(21) > 2·ATR(21).shift(5) over 252d (ATR doubling in 5d)."""
    a = _atr(high, low, close, MDAYS)
    return (a > 2 * a.shift(WDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_544_atr_halve_in_5d_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(21) < 0.5·ATR(21).shift(5) over 252d (ATR halving in 5d)."""
    a = _atr(high, low, close, MDAYS)
    return (a < 0.5 * a.shift(WDAYS)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_545_tr_outlier_count_p99_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where TR > 252d-p99 of TR distribution, over 252d."""
    tr = _true_range(high, low, close)
    p99 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.99).shift(1)
    return (tr > p99).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_546_consecutive_tr_outliers_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of 2+ consecutive TR > 252d-p95 events over 252d."""
    tr = _true_range(high, low, close)
    p95 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.95).shift(1)
    out = tr > p95
    consec = out & out.shift(1).fillna(False)
    return consec.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_547_atr_w_pattern_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR W-pattern: 5d-rising → 5d-falling → 5d-rising → 5d-falling, count over 252d."""
    a = _atr(high, low, close, MDAYS)
    rising_now = a > a.shift(WDAYS)
    falling_5_ago = a.shift(WDAYS) < a.shift(WDAYS * 2)
    rising_10_ago = a.shift(WDAYS * 2) > a.shift(WDAYS * 3)
    falling_15_ago = a.shift(WDAYS * 3) < a.shift(WDAYS * 4)
    w = rising_now & falling_5_ago & rising_10_ago & falling_15_ago
    return w.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_548_atr_m_pattern_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR M-pattern: 5d-falling → 5d-rising → 5d-falling → 5d-rising, count over 252d."""
    a = _atr(high, low, close, MDAYS)
    falling_now = a < a.shift(WDAYS)
    rising_5_ago = a.shift(WDAYS) > a.shift(WDAYS * 2)
    falling_10_ago = a.shift(WDAYS * 2) < a.shift(WDAYS * 3)
    rising_15_ago = a.shift(WDAYS * 3) > a.shift(WDAYS * 4)
    m = falling_now & rising_5_ago & falling_10_ago & rising_15_ago
    return m.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_549_max_atr_within_63d_to_current_ratio_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max(ATR, 63d) / current ATR — overhead vol-extreme proxy."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a.rolling(QDAYS, min_periods=MDAYS).max(), a).diff().diff()

def f40_atxd_550_min_atr_within_63d_to_current_ratio_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """min(ATR, 63d) / current ATR — vol-floor proxy."""
    a = _atr(high, low, close, MDAYS)
    return _safe_div(a.rolling(QDAYS, min_periods=MDAYS).min(), a).diff().diff()

def f40_atxd_551_atr_seasonal_5d_pattern_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(ATR(21), ATR(21).shift(5)) over 252d — 5d ATR pattern (weekly-period)."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(WDAYS)).diff().diff()

def f40_atxd_552_atr_seasonal_21d_pattern_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(ATR(21), ATR(21).shift(21)) over 252d (monthly-period)."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(MDAYS)).diff().diff()

def f40_atxd_553_atr_local_max_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ATR(21) local maxima (a_t > a_{t-1} AND a_t > a_{t+1}) — restate causally: a_{t-1} > a_{t-2} AND a_{t-1} > a_t."""
    a = _atr(high, low, close, MDAYS)
    local_max = (a.shift(1) > a.shift(2)) & (a.shift(1) > a)
    return local_max.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_554_atr_local_min_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of ATR(21) local minima — restate causally: a_{t-1} < a_{t-2} AND a_{t-1} < a_t."""
    a = _atr(high, low, close, MDAYS)
    local_min = (a.shift(1) < a.shift(2)) & (a.shift(1) < a)
    return local_min.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_555_atr_zigzag_amplitude_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean |ATR(21) zigzag amplitude| — distance between adjacent local extrema, over 252d."""
    a = _atr(high, low, close, MDAYS)

    def _amp(w):
        ww = w[~np.isnan(w)]
        n = len(ww)
        if n < QDAYS:
            return np.nan
        ext = []
        for i in range(1, n - 1):
            if ww[i] > ww[i - 1] and ww[i] > ww[i + 1] or (ww[i] < ww[i - 1] and ww[i] < ww[i + 1]):
                ext.append(ww[i])
        if len(ext) < 2:
            return np.nan
        return float(np.mean(np.abs(np.diff(ext))))
    return a.rolling(YDAYS, min_periods=QDAYS).apply(_amp, raw=True).diff().diff()

def f40_atxd_556_tr_corr_with_5d_return_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(TR, 5d log-return) over 252d (range-vs-recent-trend coupling)."""
    tr = _true_range(high, low, close)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(r5).diff().diff()

def f40_atxd_557_tr_corr_with_21d_return_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(TR, 21d log-return) over 252d."""
    tr = _true_range(high, low, close)
    r21 = _safe_log(close) - _safe_log(close.shift(MDAYS))
    return tr.rolling(YDAYS, min_periods=QDAYS).corr(r21).diff().diff()

def f40_atxd_558_tr_corr_with_neg_5d_return_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(TR, 5d return) restricted to negative-5d-return bars over 252d (TR expansion on declines)."""
    tr = _true_range(high, low, close)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    neg = r5 < 0
    return tr.where(neg, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(r5.where(neg, np.nan)).diff().diff()

def f40_atxd_559_tr_corr_with_pos_5d_return_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(TR, 5d return) restricted to positive-5d-return bars over 252d."""
    tr = _true_range(high, low, close)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    pos = r5 > 0
    return tr.where(pos, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(r5.where(pos, np.nan)).diff().diff()

def f40_atxd_560_atr_ranges_after_negative_5d_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars where prior 5d-return < 0 over 252d (post-decline ATR)."""
    a = _atr(high, low, close, MDAYS)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    neg = r5.shift(1) < 0
    return a.where(neg, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_561_atr_ranges_after_positive_5d_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars where prior 5d-return > 0 over 252d (post-rally ATR)."""
    a = _atr(high, low, close, MDAYS)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    pos = r5.shift(1) > 0
    return a.where(pos, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_562_tr_ratio_to_5d_return_magnitude_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR / |5d return| over 252d — range-per-unit-net-move."""
    tr = _true_range(high, low, close)
    r5_abs = (_safe_log(close) - _safe_log(close.shift(WDAYS))).abs()
    return _safe_div(tr, r5_abs).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_563_tr_grows_with_dd_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars where TR rises AND drawdown depth deepens, over 252d (range expands as drawdown grows)."""
    tr = _true_range(high, low, close)
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    return ((tr.diff() > 0) & (dd.diff() > 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_564_tr_shrinks_in_recovery_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Count of bars where TR falls AND drawdown narrows over 252d."""
    tr = _true_range(high, low, close)
    rmax = close.rolling(QDAYS, min_periods=MDAYS).max()
    dd = 1.0 - _safe_div(close, rmax)
    return ((tr.diff() < 0) & (dd.diff() < 0)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_565_atr_post_drawdown_recovery_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean ATR(21) on bars where close hits new 63d-high after being in drawdown >5% (recovery)."""
    a = _atr(high, low, close, MDAYS)
    rmax63 = close.rolling(QDAYS, min_periods=MDAYS).max()
    in_dd = close.shift(WDAYS) < 0.95 * rmax63.shift(WDAYS)
    new_high_63 = close >= rmax63
    recovery = in_dd & new_high_63
    return a.where(recovery, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_566_atr_skew_vs_return_skew_corr_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Corr(rolling 21d skew(ATR), rolling 21d skew(close.diff())) over 252d."""
    a = _atr(high, low, close, MDAYS)
    atr_skew = a.rolling(MDAYS, min_periods=WDAYS).skew()
    ret_skew = close.diff().rolling(MDAYS, min_periods=WDAYS).skew()
    return atr_skew.rolling(YDAYS, min_periods=QDAYS).corr(ret_skew).diff().diff()

def f40_atxd_567_tr_z_minus_r_z_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Mean (TR z-score − |r| z-score) over 252d — range-vs-magnitude divergence."""
    tr_z = _rolling_zscore(_true_range(high, low, close), YDAYS)
    r_z = _rolling_zscore(close.diff().abs(), YDAYS)
    return (tr_z - r_z).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_568_atr_predicts_5d_return_corr_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Corr(ATR(21)_t, 5d trailing return at t+5) — restated causally via shift."""
    a = _atr(high, low, close, MDAYS)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    return r5.rolling(YDAYS, min_periods=QDAYS).corr(a.shift(WDAYS)).diff().diff()

def f40_atxd_569_tr_grows_after_close_below_open_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR on bars where prior bar close < open (bearish prior), over 252d."""
    tr = _true_range(high, low, close)
    bear_prior = close.shift(1) < open.shift(1)
    return tr.where(bear_prior, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_570_tr_grows_after_close_above_open_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean TR on bars where prior bar close > open (bullish prior), over 252d."""
    tr = _true_range(high, low, close)
    bull_prior = close.shift(1) > open.shift(1)
    return tr.where(bull_prior, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_571_atr5_atr21_synced_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(5)-direction == ATR(21)-direction (both up or both down) over 63d."""
    a5 = _atr(high, low, close, WDAYS)
    a21 = _atr(high, low, close, MDAYS)
    synced = (np.sign(a5.diff()) == np.sign(a21.diff())) & (np.sign(a5.diff()) != 0)
    return synced.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f40_atxd_572_atr21_atr63_synced_count_63d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR(21)-direction == ATR(63)-direction over 63d."""
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    synced = (np.sign(a21.diff()) == np.sign(a63.diff())) & (np.sign(a21.diff()) != 0)
    return synced.astype(float).rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f40_atxd_573_atr_all_horizons_rising_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR at all horizons (5/21/63) rising over 252d."""
    a5 = _atr(high, low, close, WDAYS)
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    rising = (a5.diff() > 0) & (a21.diff() > 0) & (a63.diff() > 0)
    return rising.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_574_atr_all_horizons_falling_count_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Count of bars where ATR at all horizons (5/21/63) falling over 252d."""
    a5 = _atr(high, low, close, WDAYS)
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    falling = (a5.diff() < 0) & (a21.diff() < 0) & (a63.diff() < 0)
    return falling.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f40_atxd_575_atr5_corr_atr63_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(ATR(5), ATR(63)) over 252d (short-vs-long ATR coupling)."""
    return _atr(high, low, close, WDAYS).rolling(YDAYS, min_periods=QDAYS).corr(_atr(high, low, close, QDAYS)).diff().diff()

def f40_atxd_576_atr21_corr_atr252_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Corr(ATR(21), ATR(252)) over 252d."""
    return _atr(high, low, close, MDAYS).rolling(YDAYS, min_periods=QDAYS).corr(_atr(high, low, close, YDAYS)).diff().diff()

def f40_atxd_577_atr_horizons_spread_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (max ATR − min ATR) across horizons {5,21,63,252} over 252d (cross-horizon spread)."""
    a5 = _atr(high, low, close, WDAYS)
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    a252 = _atr(high, low, close, YDAYS)
    stacked = pd.concat([a5, a21, a63, a252], axis=1)
    return (stacked.max(axis=1) - stacked.min(axis=1)).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_578_atr_horizons_iqr_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean IQR of ATR across horizons {5,21,63,252} over 252d."""
    a5 = _atr(high, low, close, WDAYS)
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    a252 = _atr(high, low, close, YDAYS)
    stacked = pd.concat([a5, a21, a63, a252], axis=1)
    return (stacked.quantile(0.75, axis=1) - stacked.quantile(0.25, axis=1)).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_579_atr_horizons_cv_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean CV (std/mean) across horizons {5,21,63,252} ATR values, over 252d."""
    a5 = _atr(high, low, close, WDAYS)
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    a252 = _atr(high, low, close, YDAYS)
    stacked = pd.concat([a5, a21, a63, a252], axis=1)
    return _safe_div(stacked.std(axis=1), stacked.mean(axis=1)).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_580_natr21_252d_range_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max NATR(21) − min NATR(21) over 252d / mean NATR(21) — relative NATR range."""
    n = _safe_div(_atr(high, low, close, MDAYS), close)
    rng = n.rolling(YDAYS, min_periods=QDAYS).max() - n.rolling(YDAYS, min_periods=QDAYS).min()
    return _safe_div(rng, n.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f40_atxd_581_atr_horizons_alignment_score_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean sign-alignment score: count of horizons (5,21,63,252) where ATR > 252d-median, over 252d."""
    score = pd.Series(0.0, index=close.index)
    for n in (WDAYS, MDAYS, QDAYS, YDAYS):
        a = _atr(high, low, close, n)
        med = a.rolling(YDAYS, min_periods=QDAYS).median()
        score = score + (a > med).astype(float)
    return score.diff().diff()

def f40_atxd_582_atr_horizons_correlation_avg_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean pairwise correlation across ATR at horizons {5,21,63} over 252d."""
    a5 = _atr(high, low, close, WDAYS)
    a21 = _atr(high, low, close, MDAYS)
    a63 = _atr(high, low, close, QDAYS)
    c1 = a5.rolling(YDAYS, min_periods=QDAYS).corr(a21)
    c2 = a5.rolling(YDAYS, min_periods=QDAYS).corr(a63)
    c3 = a21.rolling(YDAYS, min_periods=QDAYS).corr(a63)
    return ((c1 + c2 + c3) / 3.0).diff().diff()

def f40_atxd_583_atr_horizons_cross_zscore_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Z-score of ATR(5) computed within ATR(252) distribution over 252d (cross-horizon outlier indicator)."""
    a5 = _atr(high, low, close, WDAYS)
    a252 = _atr(high, low, close, YDAYS)
    return _safe_div(a5 - a252.rolling(YDAYS, min_periods=QDAYS).mean(), a252.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff()

def f40_atxd_584_atr_spread_acceleration_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d slope of (ATR(5) − ATR(21)) over 252d (cross-horizon spread velocity)."""
    spread = _atr(high, low, close, WDAYS) - _atr(high, low, close, MDAYS)
    return _rolling_slope(spread, WDAYS).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_585_atr5_atr21_ratio_velocity_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d % change of (ATR(5)/ATR(21)) over 252d."""
    ratio = _safe_div(_atr(high, low, close, WDAYS), _atr(high, low, close, MDAYS))
    return _safe_div(ratio - ratio.shift(WDAYS), ratio.shift(WDAYS)).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f40_atxd_586_tr_max_to_avg_ratio_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """max(TR)/mean(TR) over 252d — max-to-average ratio."""
    tr = _true_range(high, low, close)
    return _safe_div(tr.rolling(YDAYS, min_periods=QDAYS).max(), tr.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f40_atxd_587_tr_top10_pct_share_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ TR of top-10% bars / Σ TR total over 252d."""
    tr = _true_range(high, low, close)
    p90 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return _safe_div(tr.where(tr > p90, 0.0).rolling(YDAYS, min_periods=QDAYS).sum(), tr.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f40_atxd_588_tr_bottom10_pct_share_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ TR of bottom-10% bars / Σ TR total over 252d."""
    tr = _true_range(high, low, close)
    p10 = tr.rolling(YDAYS, min_periods=QDAYS).quantile(0.1).shift(1)
    return _safe_div(tr.where(tr < p10, 0.0).rolling(YDAYS, min_periods=QDAYS).sum(), tr.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f40_atxd_589_tr_concentration_top5_bars_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Σ top-5-bar TR / Σ TR over 252d — concentration of range in 5 biggest bars."""
    tr = _true_range(high, low, close)

    def _conc(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS or ww.sum() == 0:
            return np.nan
        return float(np.sort(ww)[-5:].sum() / ww.sum())
    return tr.rolling(YDAYS, min_periods=QDAYS).apply(_conc, raw=True).diff().diff()

def f40_atxd_590_atr_rolling_max_pctrank_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Pct-rank of ATR(21) within trailing 252d window (alt measure of position in distribution)."""
    a = _atr(high, low, close, MDAYS)
    return a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True).diff().diff()

def f40_atxd_591_atr_rolling_median_distance_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / rolling-252d median(ATR(21)) − 1 — relative distance from median."""
    a = _atr(high, low, close, MDAYS)
    return (_safe_div(a, a.rolling(YDAYS, min_periods=QDAYS).median()) - 1.0).diff().diff()

def f40_atxd_592_atr_rolling_iqr_normalized_dist_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """(ATR(21) − median) / IQR over 252d — IQR-normalized deviation."""
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    iqr = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75) - a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return _safe_div(a - med, iqr).diff().diff()

def f40_atxd_593_atr_rolling_p95_distance_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR(21) / 252d-p95(ATR(21)) − 1 — distance from 95th percentile (proxy for stress)."""
    a = _atr(high, low, close, MDAYS)
    return (_safe_div(a, a.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)) - 1.0).diff().diff()

def f40_atxd_594_atr_compression_phase_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) in bottom 25% of 252d AND been there for >5 days (sustained compression)."""
    a = _atr(high, low, close, MDAYS)
    p25 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    low_now = a < p25
    return (low_now & low_now.shift(1).fillna(False) & low_now.shift(2).fillna(False) & low_now.shift(3).fillna(False) & low_now.shift(4).fillna(False)).astype(float).diff().diff()

def f40_atxd_595_atr_expansion_phase_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) in top 25% of 252d AND been there for >5 days (sustained expansion)."""
    a = _atr(high, low, close, MDAYS)
    p75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    high_now = a > p75
    return (high_now & high_now.shift(1).fillna(False) & high_now.shift(2).fillna(False) & high_now.shift(3).fillna(False) & high_now.shift(4).fillna(False)).astype(float).diff().diff()

def f40_atxd_596_atr_transition_indicator_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Indicator: ATR(21) crosses from below median to above (transitioning up) within 5d."""
    a = _atr(high, low, close, MDAYS)
    med = a.rolling(YDAYS, min_periods=QDAYS).median()
    above = a > med
    above_5d_ago = above.shift(WDAYS).fillna(False)
    return (above & ~above_5d_ago).astype(float).diff().diff()

def f40_atxd_597_atr_velocity_acceleration_combo_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """ATR-slope × ATR-acceleration — combined velocity-acceleration signal over 252d."""
    a = _atr(high, low, close, MDAYS)
    slope = _rolling_slope(a, MDAYS)
    accel = a.diff().diff().rolling(MDAYS, min_periods=WDAYS).mean()
    return (slope * accel).diff().diff()

def f40_atxd_598_atr_volatility_normalized_change_5d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """5d-change ATR / std(ATR) over 252d (vol-normalized 5d ATR change)."""
    a = _atr(high, low, close, MDAYS)
    chg5 = a - a.shift(WDAYS)
    sd252 = a.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(chg5, sd252).diff().diff()

def f40_atxd_599_atr_outlier_recovery_time_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean bars for ATR(21) to recover to median after outlier (ATR>p95) event, over 252d."""
    a = _atr(high, low, close, MDAYS).values
    arr_idx = np.arange(len(a))
    med_series = pd.Series(a).rolling(YDAYS, min_periods=QDAYS).median().values
    p95_series = pd.Series(a).rolling(YDAYS, min_periods=QDAYS).quantile(0.95).values
    out = np.full(len(a), np.nan)
    for i in range(YDAYS, len(a) - MDAYS):
        if np.isnan(a[i]):
            continue
        rec = []
        for j in range(i - YDAYS, i):
            if np.isnan(a[j]) or np.isnan(p95_series[j]) or a[j] <= p95_series[j]:
                continue
            tgt = med_series[j]
            for k in range(j + 1, min(j + MDAYS, len(a))):
                if not np.isnan(a[k]) and a[k] <= tgt:
                    rec.append(k - j)
                    break
        if rec:
            out[i] = float(np.mean(rec))
    return pd.Series(out, index=close.index).diff().diff()

def f40_atxd_600_atr_quartile_dwell_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Current dwell time in ATR(21) quartile (bars since current quartile started)."""
    a = _atr(high, low, close, MDAYS)
    p25 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p50 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.5)
    p75 = a.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q = pd.Series(0, index=close.index, dtype='Int64')
    q[a < p25] = 1
    q[(a >= p25) & (a < p50)] = 2
    q[(a >= p50) & (a < p75)] = 3
    q[a >= p75] = 4
    arr = q.fillna(0).values
    out = np.zeros(len(arr), dtype=float)
    cur = 0
    cur_q = 0
    for i, v in enumerate(arr):
        if v != cur_q:
            cur_q = v
            cur = 1
        else:
            cur += 1
        out[i] = cur
    return pd.Series(out, index=close.index).diff().diff()
ATR_EXPANSION_DYNAMICS_D2_REGISTRY_526_600 = {'f40_atxd_526_tr_volume_logs_corr_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_526_tr_volume_logs_corr_252d_d2}, 'f40_atxd_527_tr_volume_zscore_corr_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_527_tr_volume_zscore_corr_252d_d2}, 'f40_atxd_528_tr_after_volume_spike_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_528_tr_after_volume_spike_252d_d2}, 'f40_atxd_529_volume_after_tr_spike_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_529_volume_after_tr_spike_252d_d2}, 'f40_atxd_530_tr_volume_joint_zscore_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_530_tr_volume_joint_zscore_252d_d2}, 'f40_atxd_531_high_tr_high_vol_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_531_high_tr_high_vol_count_63d_d2}, 'f40_atxd_532_high_tr_low_vol_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_532_high_tr_low_vol_count_63d_d2}, 'f40_atxd_533_low_tr_high_vol_count_63d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_533_low_tr_high_vol_count_63d_d2}, 'f40_atxd_534_dollar_range_volume_zscore_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_534_dollar_range_volume_zscore_252d_d2}, 'f40_atxd_535_atr_per_dollar_traded_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_535_atr_per_dollar_traded_21d_d2}, 'f40_atxd_536_range_volume_cov_5d_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_536_range_volume_cov_5d_252d_d2}, 'f40_atxd_537_volume_per_unit_range_21d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_537_volume_per_unit_range_21d_d2}, 'f40_atxd_538_tr_volume_signed_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_538_tr_volume_signed_252d_d2}, 'f40_atxd_539_volume_weighted_tr_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_539_volume_weighted_tr_252d_d2}, 'f40_atxd_540_corr_atr_vol_change_252d_d2': {'inputs': ['high', 'low', 'close', 'volume'], 'func': f40_atxd_540_corr_atr_vol_change_252d_d2}, 'f40_atxd_541_consecutive_higher_tr_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_541_consecutive_higher_tr_count_252d_d2}, 'f40_atxd_542_consecutive_lower_tr_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_542_consecutive_lower_tr_count_252d_d2}, 'f40_atxd_543_atr_double_in_5d_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_543_atr_double_in_5d_count_252d_d2}, 'f40_atxd_544_atr_halve_in_5d_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_544_atr_halve_in_5d_count_252d_d2}, 'f40_atxd_545_tr_outlier_count_p99_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_545_tr_outlier_count_p99_252d_d2}, 'f40_atxd_546_consecutive_tr_outliers_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_546_consecutive_tr_outliers_count_252d_d2}, 'f40_atxd_547_atr_w_pattern_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_547_atr_w_pattern_count_252d_d2}, 'f40_atxd_548_atr_m_pattern_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_548_atr_m_pattern_count_252d_d2}, 'f40_atxd_549_max_atr_within_63d_to_current_ratio_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_549_max_atr_within_63d_to_current_ratio_d2}, 'f40_atxd_550_min_atr_within_63d_to_current_ratio_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_550_min_atr_within_63d_to_current_ratio_d2}, 'f40_atxd_551_atr_seasonal_5d_pattern_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_551_atr_seasonal_5d_pattern_252d_d2}, 'f40_atxd_552_atr_seasonal_21d_pattern_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_552_atr_seasonal_21d_pattern_252d_d2}, 'f40_atxd_553_atr_local_max_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_553_atr_local_max_count_252d_d2}, 'f40_atxd_554_atr_local_min_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_554_atr_local_min_count_252d_d2}, 'f40_atxd_555_atr_zigzag_amplitude_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_555_atr_zigzag_amplitude_252d_d2}, 'f40_atxd_556_tr_corr_with_5d_return_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_556_tr_corr_with_5d_return_252d_d2}, 'f40_atxd_557_tr_corr_with_21d_return_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_557_tr_corr_with_21d_return_252d_d2}, 'f40_atxd_558_tr_corr_with_neg_5d_return_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_558_tr_corr_with_neg_5d_return_252d_d2}, 'f40_atxd_559_tr_corr_with_pos_5d_return_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_559_tr_corr_with_pos_5d_return_252d_d2}, 'f40_atxd_560_atr_ranges_after_negative_5d_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_560_atr_ranges_after_negative_5d_252d_d2}, 'f40_atxd_561_atr_ranges_after_positive_5d_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_561_atr_ranges_after_positive_5d_252d_d2}, 'f40_atxd_562_tr_ratio_to_5d_return_magnitude_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_562_tr_ratio_to_5d_return_magnitude_252d_d2}, 'f40_atxd_563_tr_grows_with_dd_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_563_tr_grows_with_dd_count_252d_d2}, 'f40_atxd_564_tr_shrinks_in_recovery_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_564_tr_shrinks_in_recovery_count_252d_d2}, 'f40_atxd_565_atr_post_drawdown_recovery_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_565_atr_post_drawdown_recovery_252d_d2}, 'f40_atxd_566_atr_skew_vs_return_skew_corr_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_566_atr_skew_vs_return_skew_corr_252d_d2}, 'f40_atxd_567_tr_z_minus_r_z_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_567_tr_z_minus_r_z_252d_d2}, 'f40_atxd_568_atr_predicts_5d_return_corr_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f40_atxd_568_atr_predicts_5d_return_corr_252d_d2}, 'f40_atxd_569_tr_grows_after_close_below_open_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f40_atxd_569_tr_grows_after_close_below_open_252d_d2}, 'f40_atxd_570_tr_grows_after_close_above_open_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f40_atxd_570_tr_grows_after_close_above_open_252d_d2}, 'f40_atxd_571_atr5_atr21_synced_count_63d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_571_atr5_atr21_synced_count_63d_d2}, 'f40_atxd_572_atr21_atr63_synced_count_63d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_572_atr21_atr63_synced_count_63d_d2}, 'f40_atxd_573_atr_all_horizons_rising_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_573_atr_all_horizons_rising_count_252d_d2}, 'f40_atxd_574_atr_all_horizons_falling_count_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_574_atr_all_horizons_falling_count_252d_d2}, 'f40_atxd_575_atr5_corr_atr63_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_575_atr5_corr_atr63_252d_d2}, 'f40_atxd_576_atr21_corr_atr252_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_576_atr21_corr_atr252_252d_d2}, 'f40_atxd_577_atr_horizons_spread_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_577_atr_horizons_spread_252d_d2}, 'f40_atxd_578_atr_horizons_iqr_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_578_atr_horizons_iqr_252d_d2}, 'f40_atxd_579_atr_horizons_cv_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_579_atr_horizons_cv_252d_d2}, 'f40_atxd_580_natr21_252d_range_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_580_natr21_252d_range_252d_d2}, 'f40_atxd_581_atr_horizons_alignment_score_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_581_atr_horizons_alignment_score_252d_d2}, 'f40_atxd_582_atr_horizons_correlation_avg_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_582_atr_horizons_correlation_avg_252d_d2}, 'f40_atxd_583_atr_horizons_cross_zscore_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_583_atr_horizons_cross_zscore_252d_d2}, 'f40_atxd_584_atr_spread_acceleration_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_584_atr_spread_acceleration_252d_d2}, 'f40_atxd_585_atr5_atr21_ratio_velocity_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_585_atr5_atr21_ratio_velocity_252d_d2}, 'f40_atxd_586_tr_max_to_avg_ratio_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_586_tr_max_to_avg_ratio_252d_d2}, 'f40_atxd_587_tr_top10_pct_share_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_587_tr_top10_pct_share_252d_d2}, 'f40_atxd_588_tr_bottom10_pct_share_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_588_tr_bottom10_pct_share_252d_d2}, 'f40_atxd_589_tr_concentration_top5_bars_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_589_tr_concentration_top5_bars_252d_d2}, 'f40_atxd_590_atr_rolling_max_pctrank_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_590_atr_rolling_max_pctrank_252d_d2}, 'f40_atxd_591_atr_rolling_median_distance_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_591_atr_rolling_median_distance_252d_d2}, 'f40_atxd_592_atr_rolling_iqr_normalized_dist_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_592_atr_rolling_iqr_normalized_dist_252d_d2}, 'f40_atxd_593_atr_rolling_p95_distance_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_593_atr_rolling_p95_distance_252d_d2}, 'f40_atxd_594_atr_compression_phase_indicator_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_594_atr_compression_phase_indicator_d2}, 'f40_atxd_595_atr_expansion_phase_indicator_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_595_atr_expansion_phase_indicator_d2}, 'f40_atxd_596_atr_transition_indicator_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_596_atr_transition_indicator_d2}, 'f40_atxd_597_atr_velocity_acceleration_combo_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_597_atr_velocity_acceleration_combo_252d_d2}, 'f40_atxd_598_atr_volatility_normalized_change_5d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_598_atr_volatility_normalized_change_5d_d2}, 'f40_atxd_599_atr_outlier_recovery_time_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_599_atr_outlier_recovery_time_252d_d2}, 'f40_atxd_600_atr_quartile_dwell_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f40_atxd_600_atr_quartile_dwell_252d_d2}}