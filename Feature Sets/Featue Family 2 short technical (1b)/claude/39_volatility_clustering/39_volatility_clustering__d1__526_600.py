"""39_volatility_clustering d1 features 526-600 — order-1 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff(). Self-contained; helpers redefined locally per HANDOFF."""
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

def _log_ret(close):
    return _safe_log(close).diff()

def _rolling_sigma(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std()

def f39_vclu_526_sigma_on_gap_up_days_252d_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean σ_21 on >1% gap-up days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    gap_up = open > close.shift(1) * 1.01
    return s.where(gap_up, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_527_sigma_on_gap_down_days_252d_d1(open: pd.Series, close: pd.Series) -> pd.Series:
    """Mean σ_21 on >1% gap-down days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    gap_dn = open < close.shift(1) * 0.99
    return s.where(gap_dn, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_528_sigma_on_big_up_days_252d_d1(close: pd.Series) -> pd.Series:
    """Mean σ_21 on big-up days (r > 2σ) over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    big_up = r > 2 * s.shift(1)
    return s.where(big_up, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_529_sigma_on_big_down_days_252d_d1(close: pd.Series) -> pd.Series:
    """Mean σ_21 on big-down days (r < -2σ) over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    big_dn = r < -2 * s.shift(1)
    return s.where(big_dn, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_530_sigma_at_new_21d_high_252d_d1(close: pd.Series, high: pd.Series) -> pd.Series:
    """Mean σ_21 on bars where close at 21d-high over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    at_high = close >= close.rolling(MDAYS, min_periods=WDAYS).max()
    return s.where(at_high, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_531_sigma_at_new_21d_low_252d_d1(close: pd.Series, low: pd.Series) -> pd.Series:
    """Mean σ_21 on bars where close at 21d-low over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    at_low = close <= close.rolling(MDAYS, min_periods=WDAYS).min()
    return s.where(at_low, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_532_sigma_on_outside_bar_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean σ_21 on outside bars (today engulfs prior) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    outside = (high > high.shift(1)) & (low < low.shift(1))
    return s.where(outside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_533_sigma_on_inside_bar_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean σ_21 on inside bars (today inside prior) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    inside = (high < high.shift(1)) & (low > low.shift(1))
    return s.where(inside, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_534_sigma_on_wide_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean σ_21 on bars with TR > 2·ATR(21).shift(1) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    wide = tr > 2 * atr_lag
    return s.where(wide, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_535_sigma_on_narrow_range_252d_d1(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean σ_21 on bars with TR < 0.5·ATR(21).shift(1) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    tr = _true_range(high, low, close)
    atr_lag = _atr(high, low, close, MDAYS).shift(1)
    narrow = tr < 0.5 * atr_lag
    return s.where(narrow, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_536_sigma_5d_pct_change_d1(close: pd.Series) -> pd.Series:
    """5d % change of σ_21 — short-horizon σ momentum."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s - s.shift(WDAYS), s.shift(WDAYS)).diff()

def f39_vclu_537_sigma_21d_pct_change_d1(close: pd.Series) -> pd.Series:
    """21d % change of σ_21."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s - s.shift(MDAYS), s.shift(MDAYS)).diff()

def f39_vclu_538_sigma_63d_pct_change_d1(close: pd.Series) -> pd.Series:
    """63d % change of σ_21."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s - s.shift(QDAYS), s.shift(QDAYS)).diff()

def f39_vclu_539_sigma_momentum_accel_21d_d1(close: pd.Series) -> pd.Series:
    """5d Δσ_21 − 21d Δσ_21 — σ-momentum acceleration."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s - s.shift(WDAYS) - (s - s.shift(MDAYS))).diff()

def f39_vclu_540_sigma_momentum_sign_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of bars where 5d Δσ_21 > 0 over 252d (σ-up frequency)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    up = s - s.shift(WDAYS) > 0
    return up.astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_541_sigma_log_momentum_21d_d1(close: pd.Series) -> pd.Series:
    """log(σ_21 / σ_21.shift(21)) — log σ-momentum."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (_safe_log(s) - _safe_log(s.shift(MDAYS))).diff()

def f39_vclu_542_sigma_momentum_volatility_63d_d1(close: pd.Series) -> pd.Series:
    """Std of 5d Δσ_21 over 63d — vol-of-momentum."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s - s.shift(WDAYS)).rolling(QDAYS, min_periods=MDAYS).std().diff()

def f39_vclu_543_sigma_momentum_max_drawdown_63d_d1(close: pd.Series) -> pd.Series:
    """Max drop in σ_21 over 63d (vol drawdown)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _max_drop(w):
        ww = w[~np.isnan(w)]
        if len(ww) < WDAYS:
            return np.nan
        peak = np.maximum.accumulate(ww)
        return float(np.max(1.0 - ww / peak))
    return s.rolling(QDAYS, min_periods=MDAYS).apply(_max_drop, raw=True).diff()

def f39_vclu_544_sigma_momentum_max_buildup_63d_d1(close: pd.Series) -> pd.Series:
    """Max buildup in σ_21 over 63d (from trough to peak)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

    def _max_buildup(w):
        ww = w[~np.isnan(w)]
        if len(ww) < WDAYS:
            return np.nan
        trough = np.minimum.accumulate(ww)
        return float(np.max(ww / trough - 1.0))
    return s.rolling(QDAYS, min_periods=MDAYS).apply(_max_buildup, raw=True).diff()

def f39_vclu_545_sigma_recovery_after_drop_252d_d1(close: pd.Series) -> pd.Series:
    """Mean bars for σ_21 to recover to 80% of prior peak after a 30%+ drop, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS).values
    out = np.full(len(s), np.nan)
    for i in range(YDAYS, len(s) - MDAYS):
        if np.isnan(s[i]):
            continue
        rev = []
        for j in range(i - YDAYS, i):
            if np.isnan(s[j]):
                continue
            past_peak = np.nanmax(s[max(0, j - MDAYS):j + 1])
            if past_peak <= 0 or s[j] / past_peak > 0.7:
                continue
            target = 0.8 * past_peak
            for k in range(j + 1, min(j + MDAYS, len(s))):
                if not np.isnan(s[k]) and s[k] >= target:
                    rev.append(k - j)
                    break
        if rev:
            out[i] = float(np.mean(rev))
    return pd.Series(out, index=close.index).diff()

def f39_vclu_546_sigma21_outside_2std_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 outside ±2 std of its rolling 252d mean."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = s.rolling(YDAYS, min_periods=QDAYS).std()
    z = _safe_div(s - mu, sd)
    return (z.abs() > 2.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_547_sigma21_outside_3std_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 outside ±3 std of its rolling 252d mean (anomaly)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = s.rolling(YDAYS, min_periods=QDAYS).std()
    z = _safe_div(s - mu, sd)
    return (z.abs() > 3.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_548_sigma_residual_from_trend_252d_d1(close: pd.Series) -> pd.Series:
    """σ_21 − linear-trend(σ_21, 252d) — residual from trend (anomaly proxy)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sl = _rolling_slope(s, YDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    return (s - mu).diff()

def f39_vclu_549_sigma_residual_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of σ_21 residual from 252d trend."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = s.rolling(YDAYS, min_periods=QDAYS).std()
    return _safe_div(s - mu, sd).diff()

def f39_vclu_550_sigma_robust_zscore_mad_252d_d1(close: pd.Series) -> pd.Series:
    """Robust z-score: (σ_21 − median) / MAD over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    mad = (s - med).abs().rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(s - med, mad).diff()

def f39_vclu_551_sigma_chebyshev_anomaly_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of bars where |σ_21 − median| / std > 1/√0.05 ≈ 4.47 (Chebyshev p<0.05) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    sd = s.rolling(YDAYS, min_periods=QDAYS).std()
    z = _safe_div(s - med, sd).abs()
    return (z > 4.47).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_552_sigma_consec_anomaly_252d_d1(close: pd.Series) -> pd.Series:
    """Count of consecutive σ-anomaly days (|z|>2 for 2+ bars in a row) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = s.rolling(YDAYS, min_periods=QDAYS).std()
    z = _safe_div(s - mu, sd).abs()
    consec = (z > 2.0) & (z.shift(1) > 2.0).fillna(False)
    return consec.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_553_sigma_iqr_outlier_count_252d_d1(close: pd.Series) -> pd.Series:
    """Tukey-IQR outlier count: σ_21 outside [p25 − 1.5·IQR, p75 + 1.5·IQR] over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    iqr = p75 - p25
    out = (s < p25 - 1.5 * iqr) | (s > p75 + 1.5 * iqr)
    return out.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_554_sigma_grubbs_max_anomaly_252d_d1(close: pd.Series) -> pd.Series:
    """Grubbs-style max-anomaly: max |σ − mean| / std over 252d (largest outlier z)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mu = s.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = s.rolling(YDAYS, min_periods=QDAYS).std()
    z = _safe_div((s - mu).abs(), sd)
    return z.rolling(YDAYS, min_periods=QDAYS).max().diff()

def f39_vclu_555_sigma_jump_count_zscore_above_4_252d_d1(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 z-score (within 252d) > 4 (extreme high σ) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    z = _rolling_zscore(s, YDAYS)
    return (z > 4.0).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_556_sigma5_minus_sigma21_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of (σ_5 − σ_21) within 252d."""
    r = _log_ret(close)
    diff = _rolling_sigma(r, WDAYS) - _rolling_sigma(r, MDAYS)
    return _rolling_zscore(diff, YDAYS).diff()

def f39_vclu_557_sigma21_minus_sigma63_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of (σ_21 − σ_63) within 252d."""
    r = _log_ret(close)
    diff = _rolling_sigma(r, MDAYS) - _rolling_sigma(r, QDAYS)
    return _rolling_zscore(diff, YDAYS).diff()

def f39_vclu_558_sigma63_minus_sigma252_zscore_252d_d1(close: pd.Series) -> pd.Series:
    """Z-score of (σ_63 − σ_252) within 252d."""
    r = _log_ret(close)
    diff = _rolling_sigma(r, QDAYS) - _rolling_sigma(r, YDAYS)
    return _rolling_zscore(diff, YDAYS).diff()

def f39_vclu_559_sigma_inversion_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of bars where σ_5 > σ_21 > σ_63 > σ_252 (full inversion) over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s21 = _rolling_sigma(r, MDAYS)
    s63 = _rolling_sigma(r, QDAYS)
    s252 = _rolling_sigma(r, YDAYS)
    inv = (s5 > s21) & (s21 > s63) & (s63 > s252)
    return inv.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_560_sigma_ordered_count_252d_d1(close: pd.Series) -> pd.Series:
    """Count of bars where σ_5 < σ_21 < σ_63 < σ_252 (normal term-structure) over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s21 = _rolling_sigma(r, MDAYS)
    s63 = _rolling_sigma(r, QDAYS)
    s252 = _rolling_sigma(r, YDAYS)
    ordered = (s5 < s21) & (s21 < s63) & (s63 < s252)
    return ordered.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_561_sigma_ratio_5_21_pctrank_252d_d1(close: pd.Series) -> pd.Series:
    """Pct-rank of σ_5/σ_21 ratio within 252d distribution."""
    r = _log_ret(close)
    ratio = _safe_div(_rolling_sigma(r, WDAYS), _rolling_sigma(r, MDAYS))
    return ratio.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True).diff()

def f39_vclu_562_sigma_ratio_21_252_pctrank_252d_d1(close: pd.Series) -> pd.Series:
    """Pct-rank of σ_21/σ_252 ratio within 252d distribution."""
    r = _log_ret(close)
    ratio = _safe_div(_rolling_sigma(r, MDAYS), _rolling_sigma(r, YDAYS))
    return ratio.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True).diff()

def f39_vclu_563_sigma_ts_curvature_score_252d_d1(close: pd.Series) -> pd.Series:
    """σ-term-structure curvature score: |σ_5 − 2·σ_21 + σ_63| over 252d mean (concavity magnitude)."""
    r = _log_ret(close)
    curv = (_rolling_sigma(r, WDAYS) - 2 * _rolling_sigma(r, MDAYS) + _rolling_sigma(r, QDAYS)).abs()
    return curv.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_564_sigma_ts_slope_score_252d_d1(close: pd.Series) -> pd.Series:
    """σ-term-structure slope: (σ_252 − σ_5) / σ_21 over 252d mean (term-structure shape proxy)."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s21 = _rolling_sigma(r, MDAYS)
    s252 = _rolling_sigma(r, YDAYS)
    slope = _safe_div(s252 - s5, s21)
    return slope.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_565_sigma_horizons_correlation_252d_d1(close: pd.Series) -> pd.Series:
    """Mean pairwise correlation across σ at horizons {5,21,63} over 252d."""
    r = _log_ret(close)
    s5 = _rolling_sigma(r, WDAYS)
    s21 = _rolling_sigma(r, MDAYS)
    s63 = _rolling_sigma(r, QDAYS)
    c1 = s5.rolling(YDAYS, min_periods=QDAYS).corr(s21)
    c2 = s5.rolling(YDAYS, min_periods=QDAYS).corr(s63)
    c3 = s21.rolling(YDAYS, min_periods=QDAYS).corr(s63)
    return ((c1 + c2 + c3) / 3.0).diff()

def f39_vclu_566_corr_sigma_vol_logs_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(log σ_21, log volume) over 252d (vol-volume coupling in log space)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_log(s + 1e-12).rolling(YDAYS, min_periods=QDAYS).corr(_safe_log(volume)).diff()

def f39_vclu_567_sigma_at_high_vol_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean σ_21 on top-decile-volume days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return s.where(volume > p90, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_568_sigma_at_low_vol_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean σ_21 on bottom-decile-volume days over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p10 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.1).shift(1)
    return s.where(volume < p10, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_569_sigma_at_vol_spike_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars where σ_21 > median AND volume > p90, over 252d (vol+volume co-spike)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    p90 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9).shift(1)
    return ((s > med) & (volume > p90)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_570_sigma_decoupled_from_vol_count_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Count of bars where σ_21 > p90 BUT volume < p10 (vol-vol decoupled), over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sp90 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    vp10 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.1).shift(1)
    return ((s > sp90) & (volume < vp10)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_571_corr_sigma_dvolume_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(σ_21, Δvolume) over 252d — vol-vs-volume-change coupling."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(volume.diff()).diff()

def f39_vclu_572_corr_dsigma_dvolume_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(Δσ_21, Δvolume) over 252d — co-movement of vol-changes."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.diff().rolling(YDAYS, min_periods=QDAYS).corr(volume.diff()).diff()

def f39_vclu_573_sigma_per_unit_volume_21d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """σ_21 / volume z-score average over 21d (vol-efficiency: σ-per-unit-volume)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    return _safe_div(s, vz.abs() + 1e-06).rolling(MDAYS, min_periods=WDAYS).mean().diff()

def f39_vclu_574_dollar_volume_sigma_corr_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Corr(σ_21, log(close·volume) dollar-volume) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    dv = _safe_log(close * volume)
    return s.rolling(YDAYS, min_periods=QDAYS).corr(dv).diff()

def f39_vclu_575_sigma_high_vol_pct_in_recent_63d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Fraction of high-σ-AND-high-vol days in last 63d / fraction in last 252d (regime-shift indicator)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    smed = s.rolling(YDAYS, min_periods=QDAYS).median()
    vp75 = volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.75).shift(1)
    flag = (s > smed) & (volume > vp75)
    recent = flag.astype(float).rolling(QDAYS, min_periods=MDAYS).mean()
    annual = flag.astype(float).rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(recent, annual).diff()

def f39_vclu_576_sigma_when_r_pos_minus_neg_252d_d1(close: pd.Series) -> pd.Series:
    """Mean σ_21 on positive-r days minus negative-r days, over 252d."""
    r = _log_ret(close)
    s = _rolling_sigma(r, MDAYS)
    pos = s.where(r > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    neg = s.where(r < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (pos - neg).diff()

def f39_vclu_577_sigma_when_5d_return_positive_252d_d1(close: pd.Series) -> pd.Series:
    """Mean σ_21 when 5d trailing return > 0 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    return s.where(r5 > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_578_sigma_when_5d_return_negative_252d_d1(close: pd.Series) -> pd.Series:
    """Mean σ_21 when 5d trailing return < 0 over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    return s.where(r5 < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_579_sigma_after_3day_streak_252d_d1(close: pd.Series) -> pd.Series:
    """Mean σ_21 after 3 consecutive up- or down-day streaks over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r = _log_ret(close)
    three_up = (r.shift(1) > 0) & (r.shift(2) > 0) & (r.shift(3) > 0)
    three_dn = (r.shift(1) < 0) & (r.shift(2) < 0) & (r.shift(3) < 0)
    return s.where(three_up | three_dn, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_580_sigma_lead_lag_return_252d_d1(close: pd.Series) -> pd.Series:
    """Corr(σ_21_t, r_{t+5}) using causal lag form (σ at t-5 vs r at t), 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r = _log_ret(close)
    return r.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(WDAYS)).diff()

def f39_vclu_581_sigma_predicts_abs_return_5d_252d_d1(close: pd.Series) -> pd.Series:
    """Corr(σ_21_t-5, |r_t|) over 252d — σ-predicts-future-magnitude (causal lag)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r_abs = _log_ret(close).abs()
    return r_abs.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(WDAYS)).diff()

def f39_vclu_582_sigma_vs_trend_strength_252d_d1(close: pd.Series) -> pd.Series:
    """Corr(σ_21, |21d return|) over 252d — vol-vs-trend-strength coupling."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r21 = (_safe_log(close) - _safe_log(close.shift(MDAYS))).abs()
    return s.rolling(YDAYS, min_periods=QDAYS).corr(r21).diff()

def f39_vclu_583_sigma_high_vol_neg_return_corr_252d_d1(close: pd.Series) -> pd.Series:
    """Corr(σ_21, r) restricted to high-σ regime (σ > median) over 252d — high-vol leverage effect."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r = _log_ret(close)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    hi = s > med
    return s.where(hi, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(r.where(hi, np.nan)).diff()

def f39_vclu_584_sigma_low_vol_neg_return_corr_252d_d1(close: pd.Series) -> pd.Series:
    """Corr(σ_21, r) restricted to low-σ regime over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r = _log_ret(close)
    med = s.rolling(YDAYS, min_periods=QDAYS).median()
    lo = s < med
    return s.where(lo, np.nan).rolling(YDAYS, min_periods=QDAYS).corr(r.where(lo, np.nan)).diff()

def f39_vclu_585_sigma_extreme_event_followup_252d_d1(close: pd.Series) -> pd.Series:
    """Mean σ_21 in 5 bars after a 3σ_21 event (post-extreme σ-shift) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    r = _log_ret(close)
    sig_prior = s.shift(WDAYS)
    extreme_lag = r.shift(WDAYS).abs() > 3 * sig_prior.shift(1)
    return s.where(extreme_lag, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_586_sigma_ratio_recent_vs_prior_year_d1(close: pd.Series) -> pd.Series:
    """Mean σ_21 in last 126d / mean σ_21 in days 126-252 ago (semi-annual ratio)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    recent = s.rolling(126, min_periods=63).mean()
    prior = s.shift(126).rolling(126, min_periods=63).mean()
    return _safe_div(recent, prior).diff()

def f39_vclu_587_sigma_volatility_score_252d_d1(close: pd.Series) -> pd.Series:
    """σ-of-σ / mean-σ over 252d — relative vol-of-vol."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s.rolling(YDAYS, min_periods=QDAYS).std(), s.rolling(YDAYS, min_periods=QDAYS).mean()).diff()

def f39_vclu_588_sigma_consistency_score_252d_d1(close: pd.Series) -> pd.Series:
    """1 − (max σ_21 − min σ_21) / mean σ_21 over 252d (higher = more consistent vol)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    rng = s.rolling(YDAYS, min_periods=QDAYS).max() - s.rolling(YDAYS, min_periods=QDAYS).min()
    mean = s.rolling(YDAYS, min_periods=QDAYS).mean()
    return (1.0 - _safe_div(rng, mean)).diff()

def f39_vclu_589_sigma_decay_after_high_252d_d1(close: pd.Series) -> pd.Series:
    """Mean (σ_21 − σ_21 21d ago) on days when σ_21 in top quartile, over 252d (post-peak σ-decay)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p75 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    top = s > p75
    return (s - s.shift(MDAYS)).where(top, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_590_sigma_buildup_after_low_252d_d1(close: pd.Series) -> pd.Series:
    """Mean (σ_21 − σ_21 21d ago) on days when σ_21 in bottom quartile, over 252d (post-trough buildup)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    p25 = s.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    bot = s < p25
    return (s - s.shift(MDAYS)).where(bot, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_591_sigma_zigzag_amplitude_252d_d1(close: pd.Series) -> pd.Series:
    """Mean |σ_21 zigzag amplitude|: distance between local extrema over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)

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
    return s.rolling(YDAYS, min_periods=QDAYS).apply(_amp, raw=True).diff()

def f39_vclu_592_sigma_at_lowest_in_252d_252d_d1(close: pd.Series) -> pd.Series:
    """Indicator: σ_21 within 5% of its 252d-min (very-compressed regime)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mn = s.rolling(YDAYS, min_periods=QDAYS).min()
    return (s <= 1.05 * mn).astype(float).diff()

def f39_vclu_593_sigma_at_highest_in_252d_252d_d1(close: pd.Series) -> pd.Series:
    """Indicator: σ_21 within 5% of its 252d-max (very-expanded regime)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    mx = s.rolling(YDAYS, min_periods=QDAYS).max()
    return (s >= 0.95 * mx).astype(float).diff()

def f39_vclu_594_sigma_distance_from_252d_min_d1(close: pd.Series) -> pd.Series:
    """σ_21 / 252d-min(σ_21) − 1 — distance above multi-month floor."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (_safe_div(s, s.rolling(YDAYS, min_periods=QDAYS).min()) - 1.0).diff()

def f39_vclu_595_sigma_distance_from_252d_max_d1(close: pd.Series) -> pd.Series:
    """1 − σ_21 / 252d-max(σ_21) — distance below multi-month ceiling."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (1.0 - _safe_div(s, s.rolling(YDAYS, min_periods=QDAYS).max())).diff()

def f39_vclu_596_count_sigma_above_lag1_252d_d1(close: pd.Series) -> pd.Series:
    """Fraction of bars where σ_21_t > σ_21_{t-1} (σ-up-day frequency) over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return (s > s.shift(1)).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f39_vclu_597_sigma_realized_jump_count_5d_252d_d1(close: pd.Series) -> pd.Series:
    """Count of bars where σ_21 changes by more than 1·std-of-σ in 5 days, over 252d."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    sigma_of_s = s.rolling(MDAYS, min_periods=WDAYS).std()
    chg5 = (s - s.shift(WDAYS)).abs()
    return (chg5 > sigma_of_s).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f39_vclu_598_sigma_corr_with_lag252_252d_d1(close: pd.Series) -> pd.Series:
    """Corr(σ_21_t, σ_21_{t-252}) over 504d window — year-over-year vol persistence."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).corr(s.shift(YDAYS)).diff()

def f39_vclu_599_sigma_realized_252d_vs_long_run_d1(close: pd.Series) -> pd.Series:
    """σ_252 / mean σ_252 over past 1260d — long-vol vs historical mean."""
    s = _rolling_sigma(_log_ret(close), YDAYS)
    return _safe_div(s, s.rolling(DDAYS_5Y, min_periods=DDAYS_2Y).mean()).diff()

def f39_vclu_600_sigma_volatility_of_volatility_252d_d1(close: pd.Series) -> pd.Series:
    """std(σ_21) / σ_21 over 252d — relative vol-of-vol (different from CV in earlier batch)."""
    s = _rolling_sigma(_log_ret(close), MDAYS)
    return _safe_div(s.rolling(YDAYS, min_periods=QDAYS).std(), s).diff()
VOLATILITY_CLUSTERING_D1_REGISTRY_526_600 = {'f39_vclu_526_sigma_on_gap_up_days_252d_d1': {'inputs': ['open', 'close'], 'func': f39_vclu_526_sigma_on_gap_up_days_252d_d1}, 'f39_vclu_527_sigma_on_gap_down_days_252d_d1': {'inputs': ['open', 'close'], 'func': f39_vclu_527_sigma_on_gap_down_days_252d_d1}, 'f39_vclu_528_sigma_on_big_up_days_252d_d1': {'inputs': ['close'], 'func': f39_vclu_528_sigma_on_big_up_days_252d_d1}, 'f39_vclu_529_sigma_on_big_down_days_252d_d1': {'inputs': ['close'], 'func': f39_vclu_529_sigma_on_big_down_days_252d_d1}, 'f39_vclu_530_sigma_at_new_21d_high_252d_d1': {'inputs': ['close', 'high'], 'func': f39_vclu_530_sigma_at_new_21d_high_252d_d1}, 'f39_vclu_531_sigma_at_new_21d_low_252d_d1': {'inputs': ['close', 'low'], 'func': f39_vclu_531_sigma_at_new_21d_low_252d_d1}, 'f39_vclu_532_sigma_on_outside_bar_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f39_vclu_532_sigma_on_outside_bar_252d_d1}, 'f39_vclu_533_sigma_on_inside_bar_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f39_vclu_533_sigma_on_inside_bar_252d_d1}, 'f39_vclu_534_sigma_on_wide_range_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f39_vclu_534_sigma_on_wide_range_252d_d1}, 'f39_vclu_535_sigma_on_narrow_range_252d_d1': {'inputs': ['high', 'low', 'close'], 'func': f39_vclu_535_sigma_on_narrow_range_252d_d1}, 'f39_vclu_536_sigma_5d_pct_change_d1': {'inputs': ['close'], 'func': f39_vclu_536_sigma_5d_pct_change_d1}, 'f39_vclu_537_sigma_21d_pct_change_d1': {'inputs': ['close'], 'func': f39_vclu_537_sigma_21d_pct_change_d1}, 'f39_vclu_538_sigma_63d_pct_change_d1': {'inputs': ['close'], 'func': f39_vclu_538_sigma_63d_pct_change_d1}, 'f39_vclu_539_sigma_momentum_accel_21d_d1': {'inputs': ['close'], 'func': f39_vclu_539_sigma_momentum_accel_21d_d1}, 'f39_vclu_540_sigma_momentum_sign_252d_d1': {'inputs': ['close'], 'func': f39_vclu_540_sigma_momentum_sign_252d_d1}, 'f39_vclu_541_sigma_log_momentum_21d_d1': {'inputs': ['close'], 'func': f39_vclu_541_sigma_log_momentum_21d_d1}, 'f39_vclu_542_sigma_momentum_volatility_63d_d1': {'inputs': ['close'], 'func': f39_vclu_542_sigma_momentum_volatility_63d_d1}, 'f39_vclu_543_sigma_momentum_max_drawdown_63d_d1': {'inputs': ['close'], 'func': f39_vclu_543_sigma_momentum_max_drawdown_63d_d1}, 'f39_vclu_544_sigma_momentum_max_buildup_63d_d1': {'inputs': ['close'], 'func': f39_vclu_544_sigma_momentum_max_buildup_63d_d1}, 'f39_vclu_545_sigma_recovery_after_drop_252d_d1': {'inputs': ['close'], 'func': f39_vclu_545_sigma_recovery_after_drop_252d_d1}, 'f39_vclu_546_sigma21_outside_2std_count_252d_d1': {'inputs': ['close'], 'func': f39_vclu_546_sigma21_outside_2std_count_252d_d1}, 'f39_vclu_547_sigma21_outside_3std_count_252d_d1': {'inputs': ['close'], 'func': f39_vclu_547_sigma21_outside_3std_count_252d_d1}, 'f39_vclu_548_sigma_residual_from_trend_252d_d1': {'inputs': ['close'], 'func': f39_vclu_548_sigma_residual_from_trend_252d_d1}, 'f39_vclu_549_sigma_residual_zscore_252d_d1': {'inputs': ['close'], 'func': f39_vclu_549_sigma_residual_zscore_252d_d1}, 'f39_vclu_550_sigma_robust_zscore_mad_252d_d1': {'inputs': ['close'], 'func': f39_vclu_550_sigma_robust_zscore_mad_252d_d1}, 'f39_vclu_551_sigma_chebyshev_anomaly_count_252d_d1': {'inputs': ['close'], 'func': f39_vclu_551_sigma_chebyshev_anomaly_count_252d_d1}, 'f39_vclu_552_sigma_consec_anomaly_252d_d1': {'inputs': ['close'], 'func': f39_vclu_552_sigma_consec_anomaly_252d_d1}, 'f39_vclu_553_sigma_iqr_outlier_count_252d_d1': {'inputs': ['close'], 'func': f39_vclu_553_sigma_iqr_outlier_count_252d_d1}, 'f39_vclu_554_sigma_grubbs_max_anomaly_252d_d1': {'inputs': ['close'], 'func': f39_vclu_554_sigma_grubbs_max_anomaly_252d_d1}, 'f39_vclu_555_sigma_jump_count_zscore_above_4_252d_d1': {'inputs': ['close'], 'func': f39_vclu_555_sigma_jump_count_zscore_above_4_252d_d1}, 'f39_vclu_556_sigma5_minus_sigma21_zscore_252d_d1': {'inputs': ['close'], 'func': f39_vclu_556_sigma5_minus_sigma21_zscore_252d_d1}, 'f39_vclu_557_sigma21_minus_sigma63_zscore_252d_d1': {'inputs': ['close'], 'func': f39_vclu_557_sigma21_minus_sigma63_zscore_252d_d1}, 'f39_vclu_558_sigma63_minus_sigma252_zscore_252d_d1': {'inputs': ['close'], 'func': f39_vclu_558_sigma63_minus_sigma252_zscore_252d_d1}, 'f39_vclu_559_sigma_inversion_count_252d_d1': {'inputs': ['close'], 'func': f39_vclu_559_sigma_inversion_count_252d_d1}, 'f39_vclu_560_sigma_ordered_count_252d_d1': {'inputs': ['close'], 'func': f39_vclu_560_sigma_ordered_count_252d_d1}, 'f39_vclu_561_sigma_ratio_5_21_pctrank_252d_d1': {'inputs': ['close'], 'func': f39_vclu_561_sigma_ratio_5_21_pctrank_252d_d1}, 'f39_vclu_562_sigma_ratio_21_252_pctrank_252d_d1': {'inputs': ['close'], 'func': f39_vclu_562_sigma_ratio_21_252_pctrank_252d_d1}, 'f39_vclu_563_sigma_ts_curvature_score_252d_d1': {'inputs': ['close'], 'func': f39_vclu_563_sigma_ts_curvature_score_252d_d1}, 'f39_vclu_564_sigma_ts_slope_score_252d_d1': {'inputs': ['close'], 'func': f39_vclu_564_sigma_ts_slope_score_252d_d1}, 'f39_vclu_565_sigma_horizons_correlation_252d_d1': {'inputs': ['close'], 'func': f39_vclu_565_sigma_horizons_correlation_252d_d1}, 'f39_vclu_566_corr_sigma_vol_logs_252d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_566_corr_sigma_vol_logs_252d_d1}, 'f39_vclu_567_sigma_at_high_vol_252d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_567_sigma_at_high_vol_252d_d1}, 'f39_vclu_568_sigma_at_low_vol_252d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_568_sigma_at_low_vol_252d_d1}, 'f39_vclu_569_sigma_at_vol_spike_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_569_sigma_at_vol_spike_count_252d_d1}, 'f39_vclu_570_sigma_decoupled_from_vol_count_252d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_570_sigma_decoupled_from_vol_count_252d_d1}, 'f39_vclu_571_corr_sigma_dvolume_252d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_571_corr_sigma_dvolume_252d_d1}, 'f39_vclu_572_corr_dsigma_dvolume_252d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_572_corr_dsigma_dvolume_252d_d1}, 'f39_vclu_573_sigma_per_unit_volume_21d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_573_sigma_per_unit_volume_21d_d1}, 'f39_vclu_574_dollar_volume_sigma_corr_252d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_574_dollar_volume_sigma_corr_252d_d1}, 'f39_vclu_575_sigma_high_vol_pct_in_recent_63d_d1': {'inputs': ['close', 'volume'], 'func': f39_vclu_575_sigma_high_vol_pct_in_recent_63d_d1}, 'f39_vclu_576_sigma_when_r_pos_minus_neg_252d_d1': {'inputs': ['close'], 'func': f39_vclu_576_sigma_when_r_pos_minus_neg_252d_d1}, 'f39_vclu_577_sigma_when_5d_return_positive_252d_d1': {'inputs': ['close'], 'func': f39_vclu_577_sigma_when_5d_return_positive_252d_d1}, 'f39_vclu_578_sigma_when_5d_return_negative_252d_d1': {'inputs': ['close'], 'func': f39_vclu_578_sigma_when_5d_return_negative_252d_d1}, 'f39_vclu_579_sigma_after_3day_streak_252d_d1': {'inputs': ['close'], 'func': f39_vclu_579_sigma_after_3day_streak_252d_d1}, 'f39_vclu_580_sigma_lead_lag_return_252d_d1': {'inputs': ['close'], 'func': f39_vclu_580_sigma_lead_lag_return_252d_d1}, 'f39_vclu_581_sigma_predicts_abs_return_5d_252d_d1': {'inputs': ['close'], 'func': f39_vclu_581_sigma_predicts_abs_return_5d_252d_d1}, 'f39_vclu_582_sigma_vs_trend_strength_252d_d1': {'inputs': ['close'], 'func': f39_vclu_582_sigma_vs_trend_strength_252d_d1}, 'f39_vclu_583_sigma_high_vol_neg_return_corr_252d_d1': {'inputs': ['close'], 'func': f39_vclu_583_sigma_high_vol_neg_return_corr_252d_d1}, 'f39_vclu_584_sigma_low_vol_neg_return_corr_252d_d1': {'inputs': ['close'], 'func': f39_vclu_584_sigma_low_vol_neg_return_corr_252d_d1}, 'f39_vclu_585_sigma_extreme_event_followup_252d_d1': {'inputs': ['close'], 'func': f39_vclu_585_sigma_extreme_event_followup_252d_d1}, 'f39_vclu_586_sigma_ratio_recent_vs_prior_year_d1': {'inputs': ['close'], 'func': f39_vclu_586_sigma_ratio_recent_vs_prior_year_d1}, 'f39_vclu_587_sigma_volatility_score_252d_d1': {'inputs': ['close'], 'func': f39_vclu_587_sigma_volatility_score_252d_d1}, 'f39_vclu_588_sigma_consistency_score_252d_d1': {'inputs': ['close'], 'func': f39_vclu_588_sigma_consistency_score_252d_d1}, 'f39_vclu_589_sigma_decay_after_high_252d_d1': {'inputs': ['close'], 'func': f39_vclu_589_sigma_decay_after_high_252d_d1}, 'f39_vclu_590_sigma_buildup_after_low_252d_d1': {'inputs': ['close'], 'func': f39_vclu_590_sigma_buildup_after_low_252d_d1}, 'f39_vclu_591_sigma_zigzag_amplitude_252d_d1': {'inputs': ['close'], 'func': f39_vclu_591_sigma_zigzag_amplitude_252d_d1}, 'f39_vclu_592_sigma_at_lowest_in_252d_252d_d1': {'inputs': ['close'], 'func': f39_vclu_592_sigma_at_lowest_in_252d_252d_d1}, 'f39_vclu_593_sigma_at_highest_in_252d_252d_d1': {'inputs': ['close'], 'func': f39_vclu_593_sigma_at_highest_in_252d_252d_d1}, 'f39_vclu_594_sigma_distance_from_252d_min_d1': {'inputs': ['close'], 'func': f39_vclu_594_sigma_distance_from_252d_min_d1}, 'f39_vclu_595_sigma_distance_from_252d_max_d1': {'inputs': ['close'], 'func': f39_vclu_595_sigma_distance_from_252d_max_d1}, 'f39_vclu_596_count_sigma_above_lag1_252d_d1': {'inputs': ['close'], 'func': f39_vclu_596_count_sigma_above_lag1_252d_d1}, 'f39_vclu_597_sigma_realized_jump_count_5d_252d_d1': {'inputs': ['close'], 'func': f39_vclu_597_sigma_realized_jump_count_5d_252d_d1}, 'f39_vclu_598_sigma_corr_with_lag252_252d_d1': {'inputs': ['close'], 'func': f39_vclu_598_sigma_corr_with_lag252_252d_d1}, 'f39_vclu_599_sigma_realized_252d_vs_long_run_d1': {'inputs': ['close'], 'func': f39_vclu_599_sigma_realized_252d_vs_long_run_d1}, 'f39_vclu_600_sigma_volatility_of_volatility_252d_d1': {'inputs': ['close'], 'func': f39_vclu_600_sigma_volatility_of_volatility_252d_d1}}