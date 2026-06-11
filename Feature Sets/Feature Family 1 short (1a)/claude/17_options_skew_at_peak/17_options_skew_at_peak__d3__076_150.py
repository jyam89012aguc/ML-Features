"""options_skew_at_peak d3 features 076_150 — 3rd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff().diff() so the output is the third bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
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
    idx = num.index if hasattr(num, 'index') else None
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
        return (np.searchsorted(np.sort(w), w[-1], side='right') - 0.5) / len(w)
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

def f17_oskp_076_put_volume_zscore_252d_d3(put_volume: pd.Series) -> pd.Series:
    return _rolling_zscore(put_volume, YDAYS).diff().diff().diff()

def f17_oskp_077_put_volume_log_diff_5d_d3(put_volume: pd.Series) -> pd.Series:
    return _safe_log(put_volume).diff(WDAYS).diff().diff().diff()

def f17_oskp_078_call_to_put_volume_log_diff_21d_d3(call_volume: pd.Series, put_volume: pd.Series) -> pd.Series:
    r = _safe_log(call_volume) - _safe_log(put_volume)
    return r.diff(MDAYS).diff().diff().diff()

def f17_oskp_079_call_volume_ema5_to_ema63_d3(call_volume: pd.Series) -> pd.Series:
    return _safe_div(_ema(call_volume, WDAYS), _ema(call_volume, QDAYS)).diff().diff().diff()

def f17_oskp_080_put_volume_ema5_to_ema63_d3(put_volume: pd.Series) -> pd.Series:
    return _safe_div(_ema(put_volume, WDAYS), _ema(put_volume, QDAYS)).diff().diff().diff()

def f17_oskp_081_call_oi_zscore_252d_d3(call_oi: pd.Series) -> pd.Series:
    return _rolling_zscore(call_oi, YDAYS).diff().diff().diff()

def f17_oskp_082_put_oi_zscore_252d_d3(put_oi: pd.Series) -> pd.Series:
    return _rolling_zscore(put_oi, YDAYS).diff().diff().diff()

def f17_oskp_083_put_call_oi_ratio_level_d3(put_oi: pd.Series, call_oi: pd.Series) -> pd.Series:
    return _safe_div(put_oi, call_oi).diff().diff().diff()

def f17_oskp_084_put_call_oi_ratio_zscore_252d_d3(put_oi: pd.Series, call_oi: pd.Series) -> pd.Series:
    r = _safe_div(put_oi, call_oi)
    return _rolling_zscore(r, YDAYS).diff().diff().diff()

def f17_oskp_085_put_call_oi_ratio_rank_pct_252d_d3(put_oi: pd.Series, call_oi: pd.Series) -> pd.Series:
    r = _safe_div(put_oi, call_oi)
    return _rolling_rank_pct(r, YDAYS).diff().diff().diff()

def f17_oskp_086_call_oi_log_diff_21d_d3(call_oi: pd.Series) -> pd.Series:
    return _safe_log(call_oi).diff(MDAYS).diff().diff().diff()

def f17_oskp_087_put_oi_log_diff_21d_d3(put_oi: pd.Series) -> pd.Series:
    return _safe_log(put_oi).diff(MDAYS).diff().diff().diff()

def f17_oskp_088_net_oi_change_call_minus_put_21d_d3(call_oi: pd.Series, put_oi: pd.Series) -> pd.Series:
    return (call_oi.diff(MDAYS) - put_oi.diff(MDAYS)).diff().diff().diff()

def f17_oskp_089_call_oi_pct_change_63d_d3(call_oi: pd.Series) -> pd.Series:
    return _safe_div(call_oi - call_oi.shift(QDAYS), call_oi.shift(QDAYS)).diff().diff().diff()

def f17_oskp_090_put_oi_pct_change_63d_d3(put_oi: pd.Series) -> pd.Series:
    return _safe_div(put_oi - put_oi.shift(QDAYS), put_oi.shift(QDAYS)).diff().diff().diff()

def f17_oskp_091_call_volume_to_oi_ratio_d3(call_volume: pd.Series, call_oi: pd.Series) -> pd.Series:
    return _safe_div(call_volume, call_oi).diff().diff().diff()

def f17_oskp_092_put_volume_to_oi_ratio_d3(put_volume: pd.Series, put_oi: pd.Series) -> pd.Series:
    return _safe_div(put_volume, put_oi).diff().diff().diff()

def f17_oskp_093_days_since_call_oi_max_252d_d3(call_oi: pd.Series) -> pd.Series:
    return _days_since_max(call_oi, YDAYS).diff().diff().diff()

def f17_oskp_094_days_since_put_oi_max_252d_d3(put_oi: pd.Series) -> pd.Series:
    return _days_since_max(put_oi, YDAYS).diff().diff().diff()

def f17_oskp_095_call_oi_at_yearly_max_indicator_d3(call_oi: pd.Series) -> pd.Series:
    mx = call_oi.rolling(YDAYS, min_periods=QDAYS).max()
    return ((call_oi >= mx - 1e-06) & call_oi.notna() & mx.notna()).astype(float).diff().diff().diff()

def f17_oskp_096_put_oi_at_yearly_max_indicator_d3(put_oi: pd.Series) -> pd.Series:
    mx = put_oi.rolling(YDAYS, min_periods=QDAYS).max()
    return ((put_oi >= mx - 1e-06) & put_oi.notna() & mx.notna()).astype(float).diff().diff().diff()

def f17_oskp_097_call_volume_top_decile_count_63d_d3(call_volume: pd.Series) -> pd.Series:
    thr = call_volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (call_volume >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_098_put_volume_top_decile_count_63d_d3(put_volume: pd.Series) -> pd.Series:
    thr = put_volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (put_volume >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_099_call_volume_to_avg_21d_d3(call_volume: pd.Series) -> pd.Series:
    avg = call_volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(call_volume, avg).diff().diff().diff()

def f17_oskp_100_put_volume_to_avg_21d_d3(put_volume: pd.Series) -> pd.Series:
    avg = put_volume.rolling(MDAYS, min_periods=WDAYS).mean()
    return _safe_div(put_volume, avg).diff().diff().diff()

def f17_oskp_101_atm_iv_30_60_spread_abs_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    return (atm_iv_60d - atm_iv_30d).abs().diff().diff().diff()

def f17_oskp_102_atm_iv_30_60_spread_zscore_252d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    s = (atm_iv_60d - atm_iv_30d).abs()
    return _rolling_zscore(s, YDAYS).diff().diff().diff()

def f17_oskp_103_atm_iv_60_90_spread_abs_d3(atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    return (atm_iv_90d - atm_iv_60d).abs().diff().diff().diff()

def f17_oskp_104_atm_iv_max_minus_min_30_60_90_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    df = pd.concat([atm_iv_30d, atm_iv_60d, atm_iv_90d], axis=1)
    return (df.max(axis=1) - df.min(axis=1)).diff().diff().diff()

def f17_oskp_105_atm_iv_dispersion_pct_rank_252d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    df = pd.concat([atm_iv_30d, atm_iv_60d, atm_iv_90d], axis=1)
    sd = df.std(axis=1)
    return _rolling_rank_pct(sd, YDAYS).diff().diff().diff()

def f17_oskp_106_atm_iv_30d_relative_change_vs_60d_21d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    return (atm_iv_30d.diff(MDAYS) - atm_iv_60d.diff(MDAYS)).diff().diff().diff()

def f17_oskp_107_atm_iv_60d_relative_change_vs_90d_21d_d3(atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    return (atm_iv_60d.diff(MDAYS) - atm_iv_90d.diff(MDAYS)).diff().diff().diff()

def f17_oskp_108_atm_iv_term_steepening_acceleration_21d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    slope = atm_iv_60d - atm_iv_30d
    return slope.diff(MDAYS).diff(MDAYS).diff().diff().diff()

def f17_oskp_109_atm_iv_term_inversion_max_intensity_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
    inv = (atm_iv_30d - atm_iv_60d).clip(lower=0)
    return inv.rolling(QDAYS, min_periods=MDAYS).max().diff().diff().diff()

def f17_oskp_110_atm_iv_term_humped_count_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    flag = ((atm_iv_60d > atm_iv_30d) & (atm_iv_60d > atm_iv_90d)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_111_atm_iv_term_inverted_humped_count_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    flag = ((atm_iv_60d < atm_iv_30d) & (atm_iv_60d < atm_iv_90d)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_112_atm_iv_30d_below_60d_streak_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series) -> pd.Series:
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
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True).diff().diff().diff()

def f17_oskp_113_atm_iv_intra_term_volatility_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, atm_iv_90d: pd.Series) -> pd.Series:
    df = pd.concat([atm_iv_30d, atm_iv_60d, atm_iv_90d], axis=1)
    cross = df.std(axis=1)
    return cross.rolling(QDAYS, min_periods=MDAYS).std().diff().diff().diff()

def f17_oskp_114_atm_iv_30d_quarterly_max_minus_long_baseline_d3(atm_iv_30d: pd.Series) -> pd.Series:
    qmax = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).max()
    ymean = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    return (qmax - ymean).diff().diff().diff()

def f17_oskp_115_atm_iv_30d_increase_thrust_5d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _safe_log(atm_iv_30d).diff(WDAYS).diff().diff().diff()

def f17_oskp_116_atm_iv_30d_increase_thrust_21d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _safe_log(atm_iv_30d).diff(MDAYS).diff().diff().diff()

def f17_oskp_117_atm_iv_30d_collapse_thrust_5d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _safe_log(atm_iv_30d).diff(WDAYS).clip(upper=0.0).diff().diff().diff()

def f17_oskp_118_atm_iv_30d_collapse_thrust_21d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    return _safe_log(atm_iv_30d).diff(MDAYS).clip(upper=0.0).diff().diff().diff()

def f17_oskp_119_atm_iv_30d_range_of_motion_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    mx = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).max()
    mn = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).min()
    med = atm_iv_30d.rolling(QDAYS, min_periods=MDAYS).median()
    return _safe_div(mx - mn, med).diff().diff().diff()

def f17_oskp_120_atm_iv_30d_above_median_max_streak_63d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    med = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).median()
    return _max_streak_above(atm_iv_30d - med, 0.0, QDAYS).diff().diff().diff()

def f17_oskp_121_put_iv_30d_zscore_252d_d3(put_iv_30d: pd.Series) -> pd.Series:
    return _rolling_zscore(put_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_122_put_iv_30d_rank_pct_252d_d3(put_iv_30d: pd.Series) -> pd.Series:
    return _rolling_rank_pct(put_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_123_put_iv_60d_zscore_252d_d3(put_iv_60d: pd.Series) -> pd.Series:
    return _rolling_zscore(put_iv_60d, YDAYS).diff().diff().diff()

def f17_oskp_124_call_iv_30d_zscore_252d_d3(call_iv_30d: pd.Series) -> pd.Series:
    return _rolling_zscore(call_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_125_call_iv_30d_rank_pct_252d_d3(call_iv_30d: pd.Series) -> pd.Series:
    return _rolling_rank_pct(call_iv_30d, YDAYS).diff().diff().diff()

def f17_oskp_126_call_iv_60d_zscore_252d_d3(call_iv_60d: pd.Series) -> pd.Series:
    return _rolling_zscore(call_iv_60d, YDAYS).diff().diff().diff()

def f17_oskp_127_put_call_iv_log_ratio_30d_d3(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    return (_safe_log(put_iv_30d) - _safe_log(call_iv_30d)).diff().diff().diff()

def f17_oskp_128_put_call_iv_log_ratio_zscore_252d_d3(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    r = _safe_log(put_iv_30d) - _safe_log(call_iv_30d)
    return _rolling_zscore(r, YDAYS).diff().diff().diff()

def f17_oskp_129_put_call_iv_log_ratio_change_21d_d3(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    return (_safe_log(put_iv_30d) - _safe_log(call_iv_30d)).diff(MDAYS).diff().diff().diff()

def f17_oskp_130_put_iv_above_call_iv_count_63d_d3(put_iv_30d: pd.Series, call_iv_30d: pd.Series) -> pd.Series:
    flag = (put_iv_30d > call_iv_30d).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_131_call_iv_above_put_iv_streak_d3(call_iv_30d: pd.Series, put_iv_30d: pd.Series) -> pd.Series:
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
    return flag.rolling(QDAYS, min_periods=WDAYS).apply(_streak, raw=True).diff().diff().diff()

def f17_oskp_132_call_iv_drop_thrust_21d_d3(call_iv_30d: pd.Series) -> pd.Series:
    return _safe_log(call_iv_30d).diff(MDAYS).clip(upper=0.0).diff().diff().diff()

def f17_oskp_133_call_iv_drop_thrust_63d_d3(call_iv_30d: pd.Series) -> pd.Series:
    return _safe_log(call_iv_30d).diff(QDAYS).clip(upper=0.0).diff().diff().diff()

def f17_oskp_134_put_iv_pump_thrust_21d_d3(put_iv_30d: pd.Series) -> pd.Series:
    return _safe_log(put_iv_30d).diff(MDAYS).clip(lower=0.0).diff().diff().diff()

def f17_oskp_135_put_iv_pump_thrust_63d_d3(put_iv_30d: pd.Series) -> pd.Series:
    return _safe_log(put_iv_30d).diff(QDAYS).clip(lower=0.0).diff().diff().diff()

def f17_oskp_136_skew_steepening_with_iv_rising_count_63d_d3(iv_skew_30d: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    flag = ((iv_skew_30d.diff(MDAYS) > 0) & (atm_iv_30d.diff(MDAYS) > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_137_skew_steepening_with_iv_rank_high_indicator_d3(iv_skew_30d: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    sk_up = iv_skew_30d.diff(MDAYS) > 0
    iv_r = _rolling_rank_pct(atm_iv_30d, YDAYS)
    return (sk_up & (iv_r > 0.75)).astype(float).diff().diff().diff()

def f17_oskp_138_call_dominance_index_level_d3(call_volume: pd.Series, put_volume: pd.Series, call_oi: pd.Series, put_oi: pd.Series) -> pd.Series:
    num = call_volume.fillna(0) + call_oi.fillna(0)
    den = num + put_volume.fillna(0) + put_oi.fillna(0)
    valid = call_volume.notna() & put_volume.notna() & call_oi.notna() & put_oi.notna()
    out = _safe_div(num, den)
    return out.where(valid, np.nan).diff().diff().diff()

def f17_oskp_139_call_dominance_index_log_diff_21d_d3(call_volume: pd.Series, put_volume: pd.Series, call_oi: pd.Series, put_oi: pd.Series) -> pd.Series:
    num = call_volume.fillna(0) + call_oi.fillna(0)
    den = num + put_volume.fillna(0) + put_oi.fillna(0)
    valid = call_volume.notna() & put_volume.notna() & call_oi.notna() & put_oi.notna()
    idx = _safe_div(num, den).where(valid, np.nan)
    return _safe_log(idx).diff(MDAYS).diff().diff().diff()

def f17_oskp_140_call_dominance_above_p95_count_63d_d3(call_volume: pd.Series, put_volume: pd.Series, call_oi: pd.Series, put_oi: pd.Series) -> pd.Series:
    num = call_volume.fillna(0) + call_oi.fillna(0)
    den = num + put_volume.fillna(0) + put_oi.fillna(0)
    valid = call_volume.notna() & put_volume.notna() & call_oi.notna() & put_oi.notna()
    idx = _safe_div(num, den).where(valid, np.nan)
    thr = idx.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (idx >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_141_iv_term_inverted_and_skew_flat_count_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, iv_skew_30d: pd.Series) -> pd.Series:
    inv = atm_iv_30d > atm_iv_60d
    sk_thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flat = iv_skew_30d <= sk_thr
    flag = (inv & flat).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_142_iv_above_realized_and_skew_low_count_63d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series, iv_skew_30d: pd.Series) -> pd.Series:
    rich = atm_iv_30d > iv_realized_30d
    sk_thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    low = iv_skew_30d <= sk_thr
    flag = (rich & low).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_143_call_vol_high_iv_high_count_63d_d3(call_volume: pd.Series, atm_iv_30d: pd.Series) -> pd.Series:
    cv_thr = call_volume.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    iv_thr = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((call_volume >= cv_thr) & (atm_iv_30d >= iv_thr)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_144_put_oi_high_skew_high_count_63d_d3(put_oi: pd.Series, iv_skew_30d: pd.Series) -> pd.Series:
    oi_thr = put_oi.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    sk_thr = iv_skew_30d.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((put_oi >= oi_thr) & (iv_skew_30d >= sk_thr)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_145_atm_iv_30d_mean_revert_thrust_21d_d3(atm_iv_30d: pd.Series) -> pd.Series:
    rmax = atm_iv_30d.rolling(MDAYS, min_periods=WDAYS).max()
    return _safe_div(atm_iv_30d - rmax, rmax).diff().diff().diff()

def f17_oskp_146_atm_iv_30d_recovery_above_long_mean_streak_d3(atm_iv_30d: pd.Series) -> pd.Series:
    m = atm_iv_30d.rolling(YDAYS, min_periods=QDAYS).mean()
    return _max_streak_above(atm_iv_30d - m, 0.0, QDAYS).diff().diff().diff()

def f17_oskp_147_vrp_collapse_and_call_dominance_count_63d_d3(atm_iv_30d: pd.Series, iv_realized_30d: pd.Series, call_volume: pd.Series, put_volume: pd.Series) -> pd.Series:
    vrp = atm_iv_30d - iv_realized_30d
    pcr = _safe_div(put_volume, call_volume)
    vrp_thr = vrp.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    pcr_thr = pcr.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    flag = ((vrp <= vrp_thr) & (pcr <= pcr_thr)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff().diff()

def f17_oskp_148_composite_blowoff_iv_skew_score_63d_d3(atm_iv_30d: pd.Series, iv_skew_30d: pd.Series) -> pd.Series:
    iv_r = _rolling_rank_pct(atm_iv_30d, YDAYS)
    sk_r = _rolling_rank_pct(iv_skew_30d, YDAYS)
    return (iv_r - sk_r).rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f17_oskp_149_composite_topping_iv_pattern_63d_d3(atm_iv_30d: pd.Series, atm_iv_60d: pd.Series, iv_realized_30d: pd.Series) -> pd.Series:
    flag = ((atm_iv_30d > atm_iv_60d) & (atm_iv_30d > iv_realized_30d)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()

def f17_oskp_150_composite_skew_complacency_score_63d_d3(iv_skew_30d: pd.Series, put_volume: pd.Series, call_volume: pd.Series) -> pd.Series:
    sk_r = _rolling_rank_pct(iv_skew_30d, YDAYS)
    pcr = _safe_div(put_volume, call_volume)
    pcr_r = _rolling_rank_pct(pcr, YDAYS)
    score = (1.0 - sk_r) * (1.0 - pcr_r)
    return score.rolling(QDAYS, min_periods=MDAYS).mean().diff().diff().diff()
OPTIONS_SKEW_AT_PEAK_D3_REGISTRY_076_150 = {'f17_oskp_076_put_volume_zscore_252d_d3': {'inputs': ['put_volume'], 'func': f17_oskp_076_put_volume_zscore_252d_d3}, 'f17_oskp_077_put_volume_log_diff_5d_d3': {'inputs': ['put_volume'], 'func': f17_oskp_077_put_volume_log_diff_5d_d3}, 'f17_oskp_078_call_to_put_volume_log_diff_21d_d3': {'inputs': ['call_volume', 'put_volume'], 'func': f17_oskp_078_call_to_put_volume_log_diff_21d_d3}, 'f17_oskp_079_call_volume_ema5_to_ema63_d3': {'inputs': ['call_volume'], 'func': f17_oskp_079_call_volume_ema5_to_ema63_d3}, 'f17_oskp_080_put_volume_ema5_to_ema63_d3': {'inputs': ['put_volume'], 'func': f17_oskp_080_put_volume_ema5_to_ema63_d3}, 'f17_oskp_081_call_oi_zscore_252d_d3': {'inputs': ['call_oi'], 'func': f17_oskp_081_call_oi_zscore_252d_d3}, 'f17_oskp_082_put_oi_zscore_252d_d3': {'inputs': ['put_oi'], 'func': f17_oskp_082_put_oi_zscore_252d_d3}, 'f17_oskp_083_put_call_oi_ratio_level_d3': {'inputs': ['put_oi', 'call_oi'], 'func': f17_oskp_083_put_call_oi_ratio_level_d3}, 'f17_oskp_084_put_call_oi_ratio_zscore_252d_d3': {'inputs': ['put_oi', 'call_oi'], 'func': f17_oskp_084_put_call_oi_ratio_zscore_252d_d3}, 'f17_oskp_085_put_call_oi_ratio_rank_pct_252d_d3': {'inputs': ['put_oi', 'call_oi'], 'func': f17_oskp_085_put_call_oi_ratio_rank_pct_252d_d3}, 'f17_oskp_086_call_oi_log_diff_21d_d3': {'inputs': ['call_oi'], 'func': f17_oskp_086_call_oi_log_diff_21d_d3}, 'f17_oskp_087_put_oi_log_diff_21d_d3': {'inputs': ['put_oi'], 'func': f17_oskp_087_put_oi_log_diff_21d_d3}, 'f17_oskp_088_net_oi_change_call_minus_put_21d_d3': {'inputs': ['call_oi', 'put_oi'], 'func': f17_oskp_088_net_oi_change_call_minus_put_21d_d3}, 'f17_oskp_089_call_oi_pct_change_63d_d3': {'inputs': ['call_oi'], 'func': f17_oskp_089_call_oi_pct_change_63d_d3}, 'f17_oskp_090_put_oi_pct_change_63d_d3': {'inputs': ['put_oi'], 'func': f17_oskp_090_put_oi_pct_change_63d_d3}, 'f17_oskp_091_call_volume_to_oi_ratio_d3': {'inputs': ['call_volume', 'call_oi'], 'func': f17_oskp_091_call_volume_to_oi_ratio_d3}, 'f17_oskp_092_put_volume_to_oi_ratio_d3': {'inputs': ['put_volume', 'put_oi'], 'func': f17_oskp_092_put_volume_to_oi_ratio_d3}, 'f17_oskp_093_days_since_call_oi_max_252d_d3': {'inputs': ['call_oi'], 'func': f17_oskp_093_days_since_call_oi_max_252d_d3}, 'f17_oskp_094_days_since_put_oi_max_252d_d3': {'inputs': ['put_oi'], 'func': f17_oskp_094_days_since_put_oi_max_252d_d3}, 'f17_oskp_095_call_oi_at_yearly_max_indicator_d3': {'inputs': ['call_oi'], 'func': f17_oskp_095_call_oi_at_yearly_max_indicator_d3}, 'f17_oskp_096_put_oi_at_yearly_max_indicator_d3': {'inputs': ['put_oi'], 'func': f17_oskp_096_put_oi_at_yearly_max_indicator_d3}, 'f17_oskp_097_call_volume_top_decile_count_63d_d3': {'inputs': ['call_volume'], 'func': f17_oskp_097_call_volume_top_decile_count_63d_d3}, 'f17_oskp_098_put_volume_top_decile_count_63d_d3': {'inputs': ['put_volume'], 'func': f17_oskp_098_put_volume_top_decile_count_63d_d3}, 'f17_oskp_099_call_volume_to_avg_21d_d3': {'inputs': ['call_volume'], 'func': f17_oskp_099_call_volume_to_avg_21d_d3}, 'f17_oskp_100_put_volume_to_avg_21d_d3': {'inputs': ['put_volume'], 'func': f17_oskp_100_put_volume_to_avg_21d_d3}, 'f17_oskp_101_atm_iv_30_60_spread_abs_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_101_atm_iv_30_60_spread_abs_d3}, 'f17_oskp_102_atm_iv_30_60_spread_zscore_252d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_102_atm_iv_30_60_spread_zscore_252d_d3}, 'f17_oskp_103_atm_iv_60_90_spread_abs_d3': {'inputs': ['atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_103_atm_iv_60_90_spread_abs_d3}, 'f17_oskp_104_atm_iv_max_minus_min_30_60_90_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_104_atm_iv_max_minus_min_30_60_90_d3}, 'f17_oskp_105_atm_iv_dispersion_pct_rank_252d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_105_atm_iv_dispersion_pct_rank_252d_d3}, 'f17_oskp_106_atm_iv_30d_relative_change_vs_60d_21d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_106_atm_iv_30d_relative_change_vs_60d_21d_d3}, 'f17_oskp_107_atm_iv_60d_relative_change_vs_90d_21d_d3': {'inputs': ['atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_107_atm_iv_60d_relative_change_vs_90d_21d_d3}, 'f17_oskp_108_atm_iv_term_steepening_acceleration_21d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_108_atm_iv_term_steepening_acceleration_21d_d3}, 'f17_oskp_109_atm_iv_term_inversion_max_intensity_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_109_atm_iv_term_inversion_max_intensity_63d_d3}, 'f17_oskp_110_atm_iv_term_humped_count_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_110_atm_iv_term_humped_count_63d_d3}, 'f17_oskp_111_atm_iv_term_inverted_humped_count_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_111_atm_iv_term_inverted_humped_count_63d_d3}, 'f17_oskp_112_atm_iv_30d_below_60d_streak_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d'], 'func': f17_oskp_112_atm_iv_30d_below_60d_streak_d3}, 'f17_oskp_113_atm_iv_intra_term_volatility_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'atm_iv_90d'], 'func': f17_oskp_113_atm_iv_intra_term_volatility_63d_d3}, 'f17_oskp_114_atm_iv_30d_quarterly_max_minus_long_baseline_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_114_atm_iv_30d_quarterly_max_minus_long_baseline_d3}, 'f17_oskp_115_atm_iv_30d_increase_thrust_5d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_115_atm_iv_30d_increase_thrust_5d_d3}, 'f17_oskp_116_atm_iv_30d_increase_thrust_21d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_116_atm_iv_30d_increase_thrust_21d_d3}, 'f17_oskp_117_atm_iv_30d_collapse_thrust_5d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_117_atm_iv_30d_collapse_thrust_5d_d3}, 'f17_oskp_118_atm_iv_30d_collapse_thrust_21d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_118_atm_iv_30d_collapse_thrust_21d_d3}, 'f17_oskp_119_atm_iv_30d_range_of_motion_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_119_atm_iv_30d_range_of_motion_63d_d3}, 'f17_oskp_120_atm_iv_30d_above_median_max_streak_63d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_120_atm_iv_30d_above_median_max_streak_63d_d3}, 'f17_oskp_121_put_iv_30d_zscore_252d_d3': {'inputs': ['put_iv_30d'], 'func': f17_oskp_121_put_iv_30d_zscore_252d_d3}, 'f17_oskp_122_put_iv_30d_rank_pct_252d_d3': {'inputs': ['put_iv_30d'], 'func': f17_oskp_122_put_iv_30d_rank_pct_252d_d3}, 'f17_oskp_123_put_iv_60d_zscore_252d_d3': {'inputs': ['put_iv_60d'], 'func': f17_oskp_123_put_iv_60d_zscore_252d_d3}, 'f17_oskp_124_call_iv_30d_zscore_252d_d3': {'inputs': ['call_iv_30d'], 'func': f17_oskp_124_call_iv_30d_zscore_252d_d3}, 'f17_oskp_125_call_iv_30d_rank_pct_252d_d3': {'inputs': ['call_iv_30d'], 'func': f17_oskp_125_call_iv_30d_rank_pct_252d_d3}, 'f17_oskp_126_call_iv_60d_zscore_252d_d3': {'inputs': ['call_iv_60d'], 'func': f17_oskp_126_call_iv_60d_zscore_252d_d3}, 'f17_oskp_127_put_call_iv_log_ratio_30d_d3': {'inputs': ['put_iv_30d', 'call_iv_30d'], 'func': f17_oskp_127_put_call_iv_log_ratio_30d_d3}, 'f17_oskp_128_put_call_iv_log_ratio_zscore_252d_d3': {'inputs': ['put_iv_30d', 'call_iv_30d'], 'func': f17_oskp_128_put_call_iv_log_ratio_zscore_252d_d3}, 'f17_oskp_129_put_call_iv_log_ratio_change_21d_d3': {'inputs': ['put_iv_30d', 'call_iv_30d'], 'func': f17_oskp_129_put_call_iv_log_ratio_change_21d_d3}, 'f17_oskp_130_put_iv_above_call_iv_count_63d_d3': {'inputs': ['put_iv_30d', 'call_iv_30d'], 'func': f17_oskp_130_put_iv_above_call_iv_count_63d_d3}, 'f17_oskp_131_call_iv_above_put_iv_streak_d3': {'inputs': ['call_iv_30d', 'put_iv_30d'], 'func': f17_oskp_131_call_iv_above_put_iv_streak_d3}, 'f17_oskp_132_call_iv_drop_thrust_21d_d3': {'inputs': ['call_iv_30d'], 'func': f17_oskp_132_call_iv_drop_thrust_21d_d3}, 'f17_oskp_133_call_iv_drop_thrust_63d_d3': {'inputs': ['call_iv_30d'], 'func': f17_oskp_133_call_iv_drop_thrust_63d_d3}, 'f17_oskp_134_put_iv_pump_thrust_21d_d3': {'inputs': ['put_iv_30d'], 'func': f17_oskp_134_put_iv_pump_thrust_21d_d3}, 'f17_oskp_135_put_iv_pump_thrust_63d_d3': {'inputs': ['put_iv_30d'], 'func': f17_oskp_135_put_iv_pump_thrust_63d_d3}, 'f17_oskp_136_skew_steepening_with_iv_rising_count_63d_d3': {'inputs': ['iv_skew_30d', 'atm_iv_30d'], 'func': f17_oskp_136_skew_steepening_with_iv_rising_count_63d_d3}, 'f17_oskp_137_skew_steepening_with_iv_rank_high_indicator_d3': {'inputs': ['iv_skew_30d', 'atm_iv_30d'], 'func': f17_oskp_137_skew_steepening_with_iv_rank_high_indicator_d3}, 'f17_oskp_138_call_dominance_index_level_d3': {'inputs': ['call_volume', 'put_volume', 'call_oi', 'put_oi'], 'func': f17_oskp_138_call_dominance_index_level_d3}, 'f17_oskp_139_call_dominance_index_log_diff_21d_d3': {'inputs': ['call_volume', 'put_volume', 'call_oi', 'put_oi'], 'func': f17_oskp_139_call_dominance_index_log_diff_21d_d3}, 'f17_oskp_140_call_dominance_above_p95_count_63d_d3': {'inputs': ['call_volume', 'put_volume', 'call_oi', 'put_oi'], 'func': f17_oskp_140_call_dominance_above_p95_count_63d_d3}, 'f17_oskp_141_iv_term_inverted_and_skew_flat_count_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'iv_skew_30d'], 'func': f17_oskp_141_iv_term_inverted_and_skew_flat_count_63d_d3}, 'f17_oskp_142_iv_above_realized_and_skew_low_count_63d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d', 'iv_skew_30d'], 'func': f17_oskp_142_iv_above_realized_and_skew_low_count_63d_d3}, 'f17_oskp_143_call_vol_high_iv_high_count_63d_d3': {'inputs': ['call_volume', 'atm_iv_30d'], 'func': f17_oskp_143_call_vol_high_iv_high_count_63d_d3}, 'f17_oskp_144_put_oi_high_skew_high_count_63d_d3': {'inputs': ['put_oi', 'iv_skew_30d'], 'func': f17_oskp_144_put_oi_high_skew_high_count_63d_d3}, 'f17_oskp_145_atm_iv_30d_mean_revert_thrust_21d_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_145_atm_iv_30d_mean_revert_thrust_21d_d3}, 'f17_oskp_146_atm_iv_30d_recovery_above_long_mean_streak_d3': {'inputs': ['atm_iv_30d'], 'func': f17_oskp_146_atm_iv_30d_recovery_above_long_mean_streak_d3}, 'f17_oskp_147_vrp_collapse_and_call_dominance_count_63d_d3': {'inputs': ['atm_iv_30d', 'iv_realized_30d', 'call_volume', 'put_volume'], 'func': f17_oskp_147_vrp_collapse_and_call_dominance_count_63d_d3}, 'f17_oskp_148_composite_blowoff_iv_skew_score_63d_d3': {'inputs': ['atm_iv_30d', 'iv_skew_30d'], 'func': f17_oskp_148_composite_blowoff_iv_skew_score_63d_d3}, 'f17_oskp_149_composite_topping_iv_pattern_63d_d3': {'inputs': ['atm_iv_30d', 'atm_iv_60d', 'iv_realized_30d'], 'func': f17_oskp_149_composite_topping_iv_pattern_63d_d3}, 'f17_oskp_150_composite_skew_complacency_score_63d_d3': {'inputs': ['iv_skew_30d', 'put_volume', 'call_volume'], 'func': f17_oskp_150_composite_skew_complacency_score_63d_d3}}
