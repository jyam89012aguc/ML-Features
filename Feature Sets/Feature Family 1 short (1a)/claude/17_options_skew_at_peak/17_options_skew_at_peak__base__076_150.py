"""options_skew_at_peak base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py — covers put/call volume & open-interest
dynamics, IV term-structure dispersion, deep put/call IV asymmetry,
skew-with-IV composites, and regime-fusion blowoff scores. Inputs: OPT2
(ORATS) columns. PIT-clean: right-anchored rolling, explicit min_periods,
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


def _rolling_rank_pct(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).any():
            return np.nan
        return (np.searchsorted(np.sort(w), w[-1], side="right") - 0.5) / len(w)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)


def _days_since_max(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)


def _days_since_min(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmin(w)))
    return s.rolling(window, min_periods=min_periods).apply(_f, raw=True)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _max_streak_above(s, threshold, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    flag = (s > threshold).astype(int)
    def _ms(w):
        if np.isnan(w).any():
            return np.nan
        best = cur = 0
        for v in w:
            if v > 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return flag.rolling(window, min_periods=min_periods).apply(_ms, raw=True)


# ============================================================
#                  FEATURES 076-150
# ============================================================

def f17_oskp_076_put_volume_zscore_252d(put_volume: pd.Series) -> pd.Series:
    """Z-score of put volume vs 252d — extreme put-side participation."""
    return _rolling_zscore(put_volume, YDAYS)


def f17_oskp_077_put_volume_log_diff_5d(put_volume: pd.Series) -> pd.Series:
    """5d log change in put volume — week-scale put-flow thrust."""
    return _safe_log(put_volume).diff(WDAYS)


def f17_oskp_078_call_to_put_volume_log_diff_21d(call_volume: pd.Series, put_volume: pd.Series) -> pd.Series:
    """21d change in log(call_vol/put_vol) — call-vs-put flow rotation."""
    r = _safe_log(call_volume) - _safe_log(put_volume)
    return r.diff(MDAYS)


def f17_oskp_079_call_volume_ema5_to_ema63(call_volume: pd.Series) -> pd.Series:
    """EMA(5)/EMA(63) of call volume — call-flow acceleration vs quarterly baseline."""
    return _safe_div(_ema(call_volume, WDAYS), _ema(call_volume, QDAYS))


def f17_oskp_080_put_volume_ema5_to_ema63(put_volume: pd.Series) -> pd.Series:
    """EMA(5)/EMA(63) of put volume — put-flow acceleration vs quarterly baseline."""
    return _safe_div(_ema(put_volume, WDAYS), _ema(put_volume, QDAYS))


def f17_oskp_081_call_oi_zscore_252d(call_oi: pd.Series) -> pd.Series:
    """Z-score of call open interest vs 252d — call-side positioning extremity."""
    return _rolling_zscore(call_oi, YDAYS)


def f17_oskp_082_put_oi_zscore_252d(put_oi: pd.Series) -> pd.Series:
    """Z-score of put open interest vs 252d — put-side positioning extremity."""
    return _rolling_zscore(put_oi, YDAYS)


def f17_oskp_083_put_call_oi_ratio_level(put_oi: pd.Series, call_oi: pd.Series) -> pd.Series:
    """put_oi / call_oi — raw stocks-of-bet asymmetry."""
    return _safe_div(put_oi, call_oi)


def f17_oskp_084_put_call_oi_ratio_zscore_252d(put_oi: pd.Series, call_oi: pd.Series) -> pd.Series:
    """Z-score of put/call OI ratio vs 252d."""
    r = _safe_div(put_oi, call_oi)
    return _rolling_zscore(r, YDAYS)


def f17_oskp_085_put_call_oi_ratio_rank_pct_252d(put_oi: pd.Series, call_oi: pd.Series) -> pd.Series:
    """Percentile rank of put/call OI ratio in trailing 252d."""
    r = _safe_div(put_oi, call_oi)
    return _rolling_rank_pct(r, YDAYS)


def f17_oskp_086_call_oi_log_diff_21d(call_oi: pd.Series) -> pd.Series:
    """21d log change in call OI — monthly call-side positioning thrust."""
    return _safe_log(call_oi).diff(MDAYS)


def f17_oskp_087_put_oi_log_diff_21d(put_oi: pd.Series) -> pd.Series:
    """21d log change in put OI — monthly put-side positioning thrust."""
    return _safe_log(put_oi).diff(MDAYS)


def f17_oskp_088_net_oi_change_call_minus_put_21d(call_oi: pd.Series, put_oi: pd.Series) -> pd.Series:
    """21d Δ(call OI) − 21d Δ(put OI) — net positioning shift."""
    return call_oi.diff(MDAYS) - put_oi.diff(MDAYS)


def f17_oskp_089_call_oi_pct_change_63d(call_oi: pd.Series) -> pd.Series:
    """63d percent change in call OI — quarterly call-positioning expansion."""
    return _safe_div(call_oi - call_oi.shift(QDAYS), call_oi.shift(QDAYS))


def f17_oskp_090_put_oi_pct_change_63d(put_oi: pd.Series) -> pd.Series:
    """63d percent change in put OI — quarterly put-positioning expansion."""
    return _safe_div(put_oi - put_oi.shift(QDAYS), put_oi.shift(QDAYS))


def f17_oskp_091_call_volume_to_oi_ratio(call_volume: pd.Series, call_oi: pd.Series) -> pd.Series:
    """call_volume / call_oi — daily call-churn ratio."""
    return _safe_div(call_volume, call_oi)


def f17_oskp_092_put_volume_to_oi_ratio(put_volume: pd.Series, put_oi: pd.Series) -> pd.Series:
    """put_volume / put_oi — daily put-churn ratio."""
    return _safe_div(put_volume, put_oi)


def f17_oskp_093_days_since_call_oi_max_252d(call_oi: pd.Series) -> pd.Series:
    """Bars since call OI hit its 252d rolling max — recency of call-positioning peak."""
    return _days_since_max(call_oi, YDAYS)


def f17_oskp_094_days_since_put_oi_max_252d(put_oi: pd.Series) -> pd.Series:
    """Bars since put OI hit its 252d rolling max — recency of put-positioning peak."""
    return _days_since_max(put_oi, YDAYS)


def f17_oskp_095_call_oi_at_yearly_max_indicator(call_oi: pd.Series) -> pd.Series:
    """1 if call OI equals its 252d rolling max within 1e-6 tolerance, else 0."""
    mx = call_oi.rolling(YDAYS, min_periods=QDAYS).max()
    return ((call_oi >= mx - 1e-6) & call_oi.notna() & mx.notna()).astype(float)


def f17_oskp_096_put_oi_at_yearly_max_indicator(put_oi: pd.Series) -> pd.Series:
    """1 if put OI equals its 252d rolling max within 1e-6 tolerance, else 0."""
    mx = put_oi.rolling(YDAYS, min_periods=QDAYS).max()
    return ((put_oi >= mx - 1e-6) & put_oi.notna() & mx.notna()).astype(float)


def f17_oskp_097_call_volume_top_decile_count_63d(call_volume: pd.Series) -> pd.Series:
    """Bars in last 63d where call_volume sits in trailing-252d top decile."""
    thr = call_volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (call_volume >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_098_put_volume_top_decile_count_63d(put_volume: pd.Series) -> pd.Series:
    """Bars in last 63d where put_volume sits in trailing-252d top decile."""
    thr = put_volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (put_volume >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_099_call_volume_to_avg_21d(call_volume: pd.Series) -> pd.Series:
    """call_volume / SMA(21d, call_volume) — short-window participation amplification."""
    avg = call_volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(call_volume, avg)


def f17_oskp_100_put_volume_to_avg_21d(put_volume: pd.Series) -> pd.Series:
    """put_volume / SMA(21d, put_volume) — short-window put participation amplification."""
    avg = put_volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(put_volume, avg)


def f17_oskp_101_atm_iv_30_60_spread_abs(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """|60d-IV − 30d-IV| — absolute front-term spread magnitude."""
    return (atm_iv_60d - atm_iv_30d).abs()


def f17_oskp_102_atm_iv_30_60_spread_zscore_252d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Z-score of absolute |60d−30d| spread vs 252d."""
    s = (atm_iv_60d - atm_iv_30d).abs()
    return _rolling_zscore(s, YDAYS)


def f17_oskp_103_atm_iv_60_90_spread_abs(atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """|90d-IV − 60d-IV| — absolute back-term spread magnitude."""
    return (atm_iv_90d - atm_iv_60d).abs()


def f17_oskp_104_atm_iv_max_minus_min_30_60_90(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """max(30d,60d,90d) − min(30d,60d,90d) — IV-surface spread across tenors."""
    df = pd.concat([atm_iv_30d, atm_iv_60d, atm_iv_90d], axis=1)
    return df.max(axis=1) - df.min(axis=1)


def f17_oskp_105_atm_iv_dispersion_pct_rank_252d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """Percentile rank of IV-surface std across tenors vs 252d."""
    df = pd.concat([atm_iv_30d, atm_iv_60d, atm_iv_90d], axis=1)
    sd = df.std(axis=1)
    return _rolling_rank_pct(sd, YDAYS)


def f17_oskp_106_atm_iv_30d_relative_change_vs_60d_21d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """21d Δ(30d-IV) − 21d Δ(60d-IV) — front-vs-mid term differential change."""
    return atm_iv_30d.diff(MDAYS) - atm_iv_60d.diff(MDAYS)


def f17_oskp_107_atm_iv_60d_relative_change_vs_90d_21d(atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """21d Δ(60d-IV) − 21d Δ(90d-IV) — mid-vs-back term differential change."""
    return atm_iv_60d.diff(MDAYS) - atm_iv_90d.diff(MDAYS)


def f17_oskp_108_atm_iv_term_steepening_acceleration_21d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Second 21d change of (60d−30d) term slope — term-structure acceleration."""
    slope = atm_iv_60d - atm_iv_30d
    return slope.diff(MDAYS).diff(MDAYS)


def f17_oskp_109_atm_iv_term_inversion_max_intensity_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Max over 63d of max(0, 30d-IV − 60d-IV) — worst inversion spike in window."""
    inv = (atm_iv_30d - atm_iv_60d).clip(lower=0)
    return inv.rolling(QDAYS, min_periods=MDAYS).max()


def f17_oskp_110_atm_iv_term_humped_count_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """Bars in last 63d where 60d-IV > 30d-IV AND 60d-IV > 90d-IV — humped term structure."""
    flag = ((atm_iv_60d > atm_iv_30d) & (atm_iv_60d > atm_iv_90d)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_111_atm_iv_term_inverted_humped_count_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """Bars in last 63d where 60d-IV < 30d-IV AND 60d-IV < 90d-IV — inverted hump."""
    flag = ((atm_iv_60d < atm_iv_30d) & (atm_iv_60d < atm_iv_90d)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_112_atm_iv_30d_below_60d_streak(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where 30d-IV < 60d-IV — sustained normal-slope regime."""
    flag = (atm_iv_30d < atm_iv_60d).astype(int)
    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True)


def f17_oskp_113_atm_iv_intra_term_volatility_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    """Std over 63d of the cross-tenor std of (30,60,90) — how 'wobbly' the term-structure is."""
    df = pd.concat([atm_iv_30d, atm_iv_60d, atm_iv_90d], axis=1)
    cross = df.std(axis=1)
    return cross.rolling(QDAYS, min_periods=MDAYS).std()


def f17_oskp_114_atm_iv_30d_quarterly_max_minus_long_baseline(atm_iv_30d: pd.Series) -> pd.Series:
    """max(63d 30d-IV) − mean(252d 30d-IV) — peak IV vs annual baseline."""
    qmax = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).max()
    ymean = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    return qmax - ymean


def f17_oskp_115_atm_iv_30d_increase_thrust_5d(atm_iv_30d: pd.Series) -> pd.Series:
    """5d log change in 30d-IV — week-scale IV up-thrust."""
    return _safe_log(atm_iv_30d).diff(WDAYS)


def f17_oskp_116_atm_iv_30d_increase_thrust_21d(atm_iv_30d: pd.Series) -> pd.Series:
    """21d log change in 30d-IV — monthly IV up-thrust."""
    return _safe_log(atm_iv_30d).diff(MDAYS)


def f17_oskp_117_atm_iv_30d_collapse_thrust_5d(atm_iv_30d: pd.Series) -> pd.Series:
    """Min(5d log change in 30d-IV, 0) — week-scale IV collapse intensity."""
    return _safe_log(atm_iv_30d).diff(WDAYS).clip(upper=0.0)


def f17_oskp_118_atm_iv_30d_collapse_thrust_21d(atm_iv_30d: pd.Series) -> pd.Series:
    """Min(21d log change in 30d-IV, 0) — monthly IV collapse intensity."""
    return _safe_log(atm_iv_30d).diff(MDAYS).clip(upper=0.0)


def f17_oskp_119_atm_iv_30d_range_of_motion_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """(max-min)/median of 30d-IV over 63d — robust range-of-motion."""
    mx = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).max()
    mn = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).min()
    med = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).median()
    return _safe_div(mx - mn, med)


def f17_oskp_120_atm_iv_30d_above_median_max_streak_63d(atm_iv_30d: pd.Series) -> pd.Series:
    """Longest consecutive run within 63d where 30d-IV is above its 252d trailing median."""
    med = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).median()
    return _max_streak_above(atm_iv_30d - med, 0.0, QDAYS)


def f17_oskp_121_put_iv_30d_zscore_252d(put_iv_30d: pd.Series) -> pd.Series:
    """Z-score of 30d put-wing IV vs 252d."""
    return _rolling_zscore(put_iv_30d, YDAYS)


def f17_oskp_122_put_iv_30d_rank_pct_252d(put_iv_30d: pd.Series) -> pd.Series:
    """Percentile rank of 30d put-wing IV vs 252d."""
    return _rolling_rank_pct(put_iv_30d, YDAYS)


def f17_oskp_123_put_iv_60d_zscore_252d(put_iv_60d: pd.Series) -> pd.Series:
    """Z-score of 60d put-wing IV vs 252d."""
    return _rolling_zscore(put_iv_60d, YDAYS)


def f17_oskp_124_call_iv_30d_zscore_252d(call_iv_30d: pd.Series) -> pd.Series:
    """Z-score of 30d call-wing IV vs 252d — call-side richness."""
    return _rolling_zscore(call_iv_30d, YDAYS)


def f17_oskp_125_call_iv_30d_rank_pct_252d(call_iv_30d: pd.Series) -> pd.Series:
    """Percentile rank of 30d call-wing IV vs 252d."""
    return _rolling_rank_pct(call_iv_30d, YDAYS)


def f17_oskp_126_call_iv_60d_zscore_252d(call_iv_60d: pd.Series) -> pd.Series:
    """Z-score of 60d call-wing IV vs 252d."""
    return _rolling_zscore(call_iv_60d, YDAYS)


def f17_oskp_127_put_call_iv_log_ratio_30d(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    """log(put-IV/call-IV) at 30d — symmetric wing asymmetry."""
    return _safe_log(put_iv_30d) - _safe_log(call_iv_30d)


def f17_oskp_128_put_call_iv_log_ratio_zscore_252d(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    """Z-score of log(put-IV/call-IV) 30d vs 252d."""
    r = _safe_log(put_iv_30d) - _safe_log(call_iv_30d)
    return _rolling_zscore(r, YDAYS)


def f17_oskp_129_put_call_iv_log_ratio_change_21d(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    """21d change in log(put-IV/call-IV) at 30d — wing-asymmetry rotation."""
    return (_safe_log(put_iv_30d) - _safe_log(call_iv_30d)).diff(MDAYS)


def f17_oskp_130_put_iv_above_call_iv_count_63d(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where put-IV > call-IV — fear-side dominance persistence."""
    flag = (put_iv_30d > call_iv_30d).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_131_call_iv_above_put_iv_streak(call_iv_30d: pd.Series, put_iv_30d: pd.Series) -> pd.Series:
    """Current consecutive-bar streak with call-IV > put-IV — call-side richness regime."""
    flag = (call_iv_30d > put_iv_30d).astype(int)
    def _streak(w):
        if np.isnan(w).any():
            return np.nan
        n = 0
        for v in w[::-1]:
            if v > 0:
                n += 1
            else:
                break
        return float(n)
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True)


def f17_oskp_132_call_iv_drop_thrust_21d(call_iv_30d: pd.Series) -> pd.Series:
    """Min(21d log change in call-IV, 0) — call-wing IV collapse (post-blowoff)."""
    return _safe_log(call_iv_30d).diff(MDAYS).clip(upper=0.0)


def f17_oskp_133_call_iv_drop_thrust_63d(call_iv_30d: pd.Series) -> pd.Series:
    """Min(63d log change in call-IV, 0) — quarterly call-wing IV collapse."""
    return _safe_log(call_iv_30d).diff(QDAYS).clip(upper=0.0)


def f17_oskp_134_put_iv_pump_thrust_21d(put_iv_30d: pd.Series) -> pd.Series:
    """Max(21d log change in put-IV, 0) — put-wing IV inflation thrust."""
    return _safe_log(put_iv_30d).diff(MDAYS).clip(lower=0.0)


def f17_oskp_135_put_iv_pump_thrust_63d(put_iv_30d: pd.Series) -> pd.Series:
    """Max(63d log change in put-IV, 0) — quarterly put-wing IV inflation."""
    return _safe_log(put_iv_30d).diff(QDAYS).clip(lower=0.0)


def f17_oskp_136_skew_steepening_with_iv_rising_count_63d(iv_skew_30d: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where BOTH skew is rising 21d and IV is rising 21d (compound stress)."""
    flag = ((iv_skew_30d.diff(MDAYS) > 0) & (atm_iv_30d.diff(MDAYS) > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_137_skew_steepening_with_iv_rank_high_indicator(iv_skew_30d: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    """1 if skew is rising 21d AND IV percentile rank > 0.75 in 252d, else 0."""
    sk_up = (iv_skew_30d.diff(MDAYS) > 0)
    iv_r = _rolling_rank_pct(atm_iv_30d, YDAYS)
    return ((sk_up) & (iv_r > 0.75)).astype(float)


def f17_oskp_138_call_dominance_index_level(call_volume: pd.Series, put_volume: pd.Series, call_oi: pd.Series, put_oi: pd.Series) -> pd.Series:
    """(call_vol + call_oi) / (put_vol + put_oi + call_vol + call_oi) — share of call-side activity."""
    num = call_volume.fillna(0) + call_oi.fillna(0)
    den = num + put_volume.fillna(0) + put_oi.fillna(0)
    valid = call_volume.notna() & put_volume.notna() & call_oi.notna() & put_oi.notna()
    out = _safe_div(num, den)
    return out.where(valid, np.nan)


def f17_oskp_139_call_dominance_index_log_diff_21d(call_volume: pd.Series, put_volume: pd.Series, call_oi: pd.Series, put_oi: pd.Series) -> pd.Series:
    """21d log change in call-dominance index."""
    num = call_volume.fillna(0) + call_oi.fillna(0)
    den = num + put_volume.fillna(0) + put_oi.fillna(0)
    valid = call_volume.notna() & put_volume.notna() & call_oi.notna() & put_oi.notna()
    idx = _safe_div(num, den).where(valid, np.nan)
    return _safe_log(idx).diff(MDAYS)


def f17_oskp_140_call_dominance_above_p95_count_63d(call_volume: pd.Series, put_volume: pd.Series, call_oi: pd.Series, put_oi: pd.Series) -> pd.Series:
    """Bars in last 63d where call-dominance index is above its trailing 252d p95."""
    num = call_volume.fillna(0) + call_oi.fillna(0)
    den = num + put_volume.fillna(0) + put_oi.fillna(0)
    valid = call_volume.notna() & put_volume.notna() & call_oi.notna() & put_oi.notna()
    idx = _safe_div(num, den).where(valid, np.nan)
    thr = idx.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (idx >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_141_iv_term_inverted_and_skew_flat_count_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, iv_skew_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where 30d-IV > 60d-IV AND skew ≤ trailing-252d p25 (panic-no-fear regime)."""
    inv = (atm_iv_30d > atm_iv_60d)
    sk_thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flat = (iv_skew_30d <= sk_thr)
    flag = (inv & flat).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_142_iv_above_realized_and_skew_low_count_63d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series, iv_skew_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where IV > realized AND skew below trailing 252d p25 (rich+complacent)."""
    rich = (atm_iv_30d > iv_realized_30d)
    sk_thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    low = (iv_skew_30d <= sk_thr)
    flag = (rich & low).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_143_call_vol_high_iv_high_count_63d(call_volume: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where call volume > trailing 252d p90 AND IV > trailing 252d p90."""
    cv_thr = call_volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    iv_thr = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((call_volume >= cv_thr) & (atm_iv_30d >= iv_thr)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_144_put_oi_high_skew_high_count_63d(put_oi: pd.Series, iv_skew_30d: pd.Series) -> pd.Series:
    """Bars in last 63d where put OI > trailing 252d p90 AND skew > trailing 252d p90."""
    oi_thr = put_oi.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    sk_thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((put_oi >= oi_thr) & (iv_skew_30d >= sk_thr)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_145_atm_iv_30d_mean_revert_thrust_21d(atm_iv_30d: pd.Series) -> pd.Series:
    """If 30d-IV was at trailing 21d max within last 21d, current pct distance below that max."""
    rmax = atm_iv_30d.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(atm_iv_30d - rmax, rmax)


def f17_oskp_146_atm_iv_30d_recovery_above_long_mean_streak(atm_iv_30d: pd.Series) -> pd.Series:
    """Longest consecutive 63d run where 30d-IV is above its 252d mean — sustained elevated regime."""
    m = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    return _max_streak_above(atm_iv_30d - m, 0.0, QDAYS)


def f17_oskp_147_vrp_collapse_and_call_dominance_count_63d(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series, call_volume: pd.Series, put_volume: pd.Series) -> pd.Series:
    """Bars in last 63d where VRP < trailing 252d p25 AND put/call volume ratio < trailing 252d p25."""
    vrp = atm_iv_30d - iv_realized_30d
    pcr = _safe_div(put_volume, call_volume)
    vrp_thr = vrp.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    pcr_thr = pcr.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = ((vrp <= vrp_thr) & (pcr <= pcr_thr)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum()


def f17_oskp_148_composite_blowoff_iv_skew_score_63d(atm_iv_30d: pd.Series, iv_skew_30d: pd.Series) -> pd.Series:
    """Mean over 63d of (IV percentile rank − skew percentile rank) — IV-rich-skew-poor blowoff score."""
    iv_r = _rolling_rank_pct(atm_iv_30d, YDAYS)
    sk_r = _rolling_rank_pct(iv_skew_30d, YDAYS)
    return (iv_r - sk_r).rolling(QDAYS, min_periods=MDAYS).mean()


def f17_oskp_149_composite_topping_iv_pattern_63d(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    """Mean over 63d of indicator: 30d-IV > 60d-IV AND 30d-IV > realized — topping regime fraction."""
    flag = ((atm_iv_30d > atm_iv_60d) & (atm_iv_30d > iv_realized_30d)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean()


def f17_oskp_150_composite_skew_complacency_score_63d(iv_skew_30d: pd.Series, put_volume: pd.Series, call_volume: pd.Series) -> pd.Series:
    """Mean over 63d of (1 − skew percentile rank) * (1 − put/call vol percentile rank) — fused complacency."""
    sk_r = _rolling_rank_pct(iv_skew_30d, YDAYS)
    pcr = _safe_div(put_volume, call_volume)
    pcr_r = _rolling_rank_pct(pcr, YDAYS)
    score = (1.0 - sk_r) * (1.0 - pcr_r)
    return score.rolling(QDAYS, min_periods=MDAYS).mean()


# ============================================================
#                        REGISTRY
# ============================================================

OPTIONS_SKEW_AT_PEAK_BASE_REGISTRY_076_150 = {
    "f17_oskp_076_put_volume_zscore_252d": {"inputs": ["put_volume"], "func": f17_oskp_076_put_volume_zscore_252d},
    "f17_oskp_077_put_volume_log_diff_5d": {"inputs": ["put_volume"], "func": f17_oskp_077_put_volume_log_diff_5d},
    "f17_oskp_078_call_to_put_volume_log_diff_21d": {"inputs": ["call_volume", "put_volume"], "func": f17_oskp_078_call_to_put_volume_log_diff_21d},
    "f17_oskp_079_call_volume_ema5_to_ema63": {"inputs": ["call_volume"], "func": f17_oskp_079_call_volume_ema5_to_ema63},
    "f17_oskp_080_put_volume_ema5_to_ema63": {"inputs": ["put_volume"], "func": f17_oskp_080_put_volume_ema5_to_ema63},
    "f17_oskp_081_call_oi_zscore_252d": {"inputs": ["call_oi"], "func": f17_oskp_081_call_oi_zscore_252d},
    "f17_oskp_082_put_oi_zscore_252d": {"inputs": ["put_oi"], "func": f17_oskp_082_put_oi_zscore_252d},
    "f17_oskp_083_put_call_oi_ratio_level": {"inputs": ["put_oi", "call_oi"], "func": f17_oskp_083_put_call_oi_ratio_level},
    "f17_oskp_084_put_call_oi_ratio_zscore_252d": {"inputs": ["put_oi", "call_oi"], "func": f17_oskp_084_put_call_oi_ratio_zscore_252d},
    "f17_oskp_085_put_call_oi_ratio_rank_pct_252d": {"inputs": ["put_oi", "call_oi"], "func": f17_oskp_085_put_call_oi_ratio_rank_pct_252d},
    "f17_oskp_086_call_oi_log_diff_21d": {"inputs": ["call_oi"], "func": f17_oskp_086_call_oi_log_diff_21d},
    "f17_oskp_087_put_oi_log_diff_21d": {"inputs": ["put_oi"], "func": f17_oskp_087_put_oi_log_diff_21d},
    "f17_oskp_088_net_oi_change_call_minus_put_21d": {"inputs": ["call_oi", "put_oi"], "func": f17_oskp_088_net_oi_change_call_minus_put_21d},
    "f17_oskp_089_call_oi_pct_change_63d": {"inputs": ["call_oi"], "func": f17_oskp_089_call_oi_pct_change_63d},
    "f17_oskp_090_put_oi_pct_change_63d": {"inputs": ["put_oi"], "func": f17_oskp_090_put_oi_pct_change_63d},
    "f17_oskp_091_call_volume_to_oi_ratio": {"inputs": ["call_volume", "call_oi"], "func": f17_oskp_091_call_volume_to_oi_ratio},
    "f17_oskp_092_put_volume_to_oi_ratio": {"inputs": ["put_volume", "put_oi"], "func": f17_oskp_092_put_volume_to_oi_ratio},
    "f17_oskp_093_days_since_call_oi_max_252d": {"inputs": ["call_oi"], "func": f17_oskp_093_days_since_call_oi_max_252d},
    "f17_oskp_094_days_since_put_oi_max_252d": {"inputs": ["put_oi"], "func": f17_oskp_094_days_since_put_oi_max_252d},
    "f17_oskp_095_call_oi_at_yearly_max_indicator": {"inputs": ["call_oi"], "func": f17_oskp_095_call_oi_at_yearly_max_indicator},
    "f17_oskp_096_put_oi_at_yearly_max_indicator": {"inputs": ["put_oi"], "func": f17_oskp_096_put_oi_at_yearly_max_indicator},
    "f17_oskp_097_call_volume_top_decile_count_63d": {"inputs": ["call_volume"], "func": f17_oskp_097_call_volume_top_decile_count_63d},
    "f17_oskp_098_put_volume_top_decile_count_63d": {"inputs": ["put_volume"], "func": f17_oskp_098_put_volume_top_decile_count_63d},
    "f17_oskp_099_call_volume_to_avg_21d": {"inputs": ["call_volume"], "func": f17_oskp_099_call_volume_to_avg_21d},
    "f17_oskp_100_put_volume_to_avg_21d": {"inputs": ["put_volume"], "func": f17_oskp_100_put_volume_to_avg_21d},
    "f17_oskp_101_atm_iv_30_60_spread_abs": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_101_atm_iv_30_60_spread_abs},
    "f17_oskp_102_atm_iv_30_60_spread_zscore_252d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_102_atm_iv_30_60_spread_zscore_252d},
    "f17_oskp_103_atm_iv_60_90_spread_abs": {"inputs": ["atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_103_atm_iv_60_90_spread_abs},
    "f17_oskp_104_atm_iv_max_minus_min_30_60_90": {"inputs": ["atm_iv_30d", "atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_104_atm_iv_max_minus_min_30_60_90},
    "f17_oskp_105_atm_iv_dispersion_pct_rank_252d": {"inputs": ["atm_iv_30d", "atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_105_atm_iv_dispersion_pct_rank_252d},
    "f17_oskp_106_atm_iv_30d_relative_change_vs_60d_21d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_106_atm_iv_30d_relative_change_vs_60d_21d},
    "f17_oskp_107_atm_iv_60d_relative_change_vs_90d_21d": {"inputs": ["atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_107_atm_iv_60d_relative_change_vs_90d_21d},
    "f17_oskp_108_atm_iv_term_steepening_acceleration_21d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_108_atm_iv_term_steepening_acceleration_21d},
    "f17_oskp_109_atm_iv_term_inversion_max_intensity_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_109_atm_iv_term_inversion_max_intensity_63d},
    "f17_oskp_110_atm_iv_term_humped_count_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_110_atm_iv_term_humped_count_63d},
    "f17_oskp_111_atm_iv_term_inverted_humped_count_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_111_atm_iv_term_inverted_humped_count_63d},
    "f17_oskp_112_atm_iv_30d_below_60d_streak": {"inputs": ["atm_iv_30d", "atm_iv_60d"], "func": f17_oskp_112_atm_iv_30d_below_60d_streak},
    "f17_oskp_113_atm_iv_intra_term_volatility_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d", "atm_iv_90d"], "func": f17_oskp_113_atm_iv_intra_term_volatility_63d},
    "f17_oskp_114_atm_iv_30d_quarterly_max_minus_long_baseline": {"inputs": ["atm_iv_30d"], "func": f17_oskp_114_atm_iv_30d_quarterly_max_minus_long_baseline},
    "f17_oskp_115_atm_iv_30d_increase_thrust_5d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_115_atm_iv_30d_increase_thrust_5d},
    "f17_oskp_116_atm_iv_30d_increase_thrust_21d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_116_atm_iv_30d_increase_thrust_21d},
    "f17_oskp_117_atm_iv_30d_collapse_thrust_5d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_117_atm_iv_30d_collapse_thrust_5d},
    "f17_oskp_118_atm_iv_30d_collapse_thrust_21d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_118_atm_iv_30d_collapse_thrust_21d},
    "f17_oskp_119_atm_iv_30d_range_of_motion_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_119_atm_iv_30d_range_of_motion_63d},
    "f17_oskp_120_atm_iv_30d_above_median_max_streak_63d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_120_atm_iv_30d_above_median_max_streak_63d},
    "f17_oskp_121_put_iv_30d_zscore_252d": {"inputs": ["put_iv_30d"], "func": f17_oskp_121_put_iv_30d_zscore_252d},
    "f17_oskp_122_put_iv_30d_rank_pct_252d": {"inputs": ["put_iv_30d"], "func": f17_oskp_122_put_iv_30d_rank_pct_252d},
    "f17_oskp_123_put_iv_60d_zscore_252d": {"inputs": ["put_iv_60d"], "func": f17_oskp_123_put_iv_60d_zscore_252d},
    "f17_oskp_124_call_iv_30d_zscore_252d": {"inputs": ["call_iv_30d"], "func": f17_oskp_124_call_iv_30d_zscore_252d},
    "f17_oskp_125_call_iv_30d_rank_pct_252d": {"inputs": ["call_iv_30d"], "func": f17_oskp_125_call_iv_30d_rank_pct_252d},
    "f17_oskp_126_call_iv_60d_zscore_252d": {"inputs": ["call_iv_60d"], "func": f17_oskp_126_call_iv_60d_zscore_252d},
    "f17_oskp_127_put_call_iv_log_ratio_30d": {"inputs": ["put_iv_30d", "call_iv_30d"], "func": f17_oskp_127_put_call_iv_log_ratio_30d},
    "f17_oskp_128_put_call_iv_log_ratio_zscore_252d": {"inputs": ["put_iv_30d", "call_iv_30d"], "func": f17_oskp_128_put_call_iv_log_ratio_zscore_252d},
    "f17_oskp_129_put_call_iv_log_ratio_change_21d": {"inputs": ["put_iv_30d", "call_iv_30d"], "func": f17_oskp_129_put_call_iv_log_ratio_change_21d},
    "f17_oskp_130_put_iv_above_call_iv_count_63d": {"inputs": ["put_iv_30d", "call_iv_30d"], "func": f17_oskp_130_put_iv_above_call_iv_count_63d},
    "f17_oskp_131_call_iv_above_put_iv_streak": {"inputs": ["call_iv_30d", "put_iv_30d"], "func": f17_oskp_131_call_iv_above_put_iv_streak},
    "f17_oskp_132_call_iv_drop_thrust_21d": {"inputs": ["call_iv_30d"], "func": f17_oskp_132_call_iv_drop_thrust_21d},
    "f17_oskp_133_call_iv_drop_thrust_63d": {"inputs": ["call_iv_30d"], "func": f17_oskp_133_call_iv_drop_thrust_63d},
    "f17_oskp_134_put_iv_pump_thrust_21d": {"inputs": ["put_iv_30d"], "func": f17_oskp_134_put_iv_pump_thrust_21d},
    "f17_oskp_135_put_iv_pump_thrust_63d": {"inputs": ["put_iv_30d"], "func": f17_oskp_135_put_iv_pump_thrust_63d},
    "f17_oskp_136_skew_steepening_with_iv_rising_count_63d": {"inputs": ["iv_skew_30d", "atm_iv_30d"], "func": f17_oskp_136_skew_steepening_with_iv_rising_count_63d},
    "f17_oskp_137_skew_steepening_with_iv_rank_high_indicator": {"inputs": ["iv_skew_30d", "atm_iv_30d"], "func": f17_oskp_137_skew_steepening_with_iv_rank_high_indicator},
    "f17_oskp_138_call_dominance_index_level": {"inputs": ["call_volume", "put_volume", "call_oi", "put_oi"], "func": f17_oskp_138_call_dominance_index_level},
    "f17_oskp_139_call_dominance_index_log_diff_21d": {"inputs": ["call_volume", "put_volume", "call_oi", "put_oi"], "func": f17_oskp_139_call_dominance_index_log_diff_21d},
    "f17_oskp_140_call_dominance_above_p95_count_63d": {"inputs": ["call_volume", "put_volume", "call_oi", "put_oi"], "func": f17_oskp_140_call_dominance_above_p95_count_63d},
    "f17_oskp_141_iv_term_inverted_and_skew_flat_count_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d", "iv_skew_30d"], "func": f17_oskp_141_iv_term_inverted_and_skew_flat_count_63d},
    "f17_oskp_142_iv_above_realized_and_skew_low_count_63d": {"inputs": ["atm_iv_30d", "iv_realized_30d", "iv_skew_30d"], "func": f17_oskp_142_iv_above_realized_and_skew_low_count_63d},
    "f17_oskp_143_call_vol_high_iv_high_count_63d": {"inputs": ["call_volume", "atm_iv_30d"], "func": f17_oskp_143_call_vol_high_iv_high_count_63d},
    "f17_oskp_144_put_oi_high_skew_high_count_63d": {"inputs": ["put_oi", "iv_skew_30d"], "func": f17_oskp_144_put_oi_high_skew_high_count_63d},
    "f17_oskp_145_atm_iv_30d_mean_revert_thrust_21d": {"inputs": ["atm_iv_30d"], "func": f17_oskp_145_atm_iv_30d_mean_revert_thrust_21d},
    "f17_oskp_146_atm_iv_30d_recovery_above_long_mean_streak": {"inputs": ["atm_iv_30d"], "func": f17_oskp_146_atm_iv_30d_recovery_above_long_mean_streak},
    "f17_oskp_147_vrp_collapse_and_call_dominance_count_63d": {"inputs": ["atm_iv_30d", "iv_realized_30d", "call_volume", "put_volume"], "func": f17_oskp_147_vrp_collapse_and_call_dominance_count_63d},
    "f17_oskp_148_composite_blowoff_iv_skew_score_63d": {"inputs": ["atm_iv_30d", "iv_skew_30d"], "func": f17_oskp_148_composite_blowoff_iv_skew_score_63d},
    "f17_oskp_149_composite_topping_iv_pattern_63d": {"inputs": ["atm_iv_30d", "atm_iv_60d", "iv_realized_30d"], "func": f17_oskp_149_composite_topping_iv_pattern_63d},
    "f17_oskp_150_composite_skew_complacency_score_63d": {"inputs": ["iv_skew_30d", "put_volume", "call_volume"], "func": f17_oskp_150_composite_skew_complacency_score_63d},
}
