"""dilution_structure_snapshot d1 features 076_150 — 1st-derivative wrappers.

Each function inlines the corresponding base body and appends .diff() so the output is the first bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
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

def _max_streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

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
    return flag_series.rolling(window, min_periods=min_periods).apply(_ms, raw=True)

def _streak_above_zero(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

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
    return flag_series.rolling(window, min_periods=min_periods).apply(_streak, raw=True)

def _recency_since_event(flag_series, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)

    def _r(w):
        if np.isnan(w).all():
            return np.nan
        nz = np.where(w > 0)[0]
        if len(nz) == 0:
            return float(len(w))
        return float(len(w) - 1 - nz[-1])
    return flag_series.rolling(window, min_periods=min_periods).apply(_r, raw=True)

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

def f19_dssp_076_sharesbas_split_adj_log_diff_21d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(MDAYS).diff()

def f19_dssp_077_sharesbas_split_adj_log_diff_63d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(QDAYS).diff()

def f19_dssp_078_sharesbas_split_adj_log_diff_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(YDAYS).diff()

def f19_dssp_079_sharesbas_split_adj_log_diff_756d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(DDAYS_3Y).diff()

def f19_dssp_080_sharesbas_split_adj_log_diff_1260d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(DDAYS_5Y).diff()

def f19_dssp_081_sharesbas_split_adj_zscore_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _rolling_zscore(sa, YDAYS).diff()

def f19_dssp_082_sharesbas_split_adj_pct_change_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_div(sa - sa.shift(YDAYS), sa.shift(YDAYS)).diff()

def f19_dssp_083_sharesbas_split_adj_rank_pct_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _rolling_rank_pct(sa, YDAYS).diff()

def f19_dssp_084_sharesbas_split_adj_distance_to_252d_max_log_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    mx = sa.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_log(sa) - _safe_log(mx)).diff()

def f19_dssp_085_sharesbas_split_adj_acceleration_21d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(MDAYS).diff(MDAYS).diff()

def f19_dssp_086_sharesbas_split_adj_pct_above_long_mean_63d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    m = sa.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (sa > m).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f19_dssp_087_sharesbas_split_adj_above_p90_count_63d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    thr = sa.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (sa >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f19_dssp_088_sharesbas_split_adj_top_decile_count_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    thr = sa.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (sa >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_089_sharesbas_split_adj_log_diff_5y_minus_long_baseline_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    d5 = _safe_log(sa).diff(DDAYS_5Y)
    base = d5.rolling(YDAYS, min_periods=QDAYS).mean()
    return (d5 - base).diff()

def f19_dssp_090_sharesbas_split_adj_3y_to_5y_log_ratio_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    return (sa.diff(DDAYS_3Y) - sa.diff(DDAYS_5Y)).diff()

def f19_dssp_091_shareswadil_split_adj_log_diff_252d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _safe_log(sa).diff(YDAYS).diff()

def f19_dssp_092_shareswadil_split_adj_log_diff_756d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _safe_log(sa).diff(DDAYS_3Y).diff()

def f19_dssp_093_shareswadil_split_adj_log_diff_1260d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _safe_log(sa).diff(DDAYS_5Y).diff()

def f19_dssp_094_shareswadil_split_adj_rank_pct_252d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _rolling_rank_pct(sa, YDAYS).diff()

def f19_dssp_095_shareswadil_split_adj_zscore_252d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _rolling_zscore(sa, YDAYS).diff()

def f19_dssp_096_shareswadil_split_adj_above_2sigma_count_252d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    m = sa.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = sa.rolling(YDAYS, min_periods=QDAYS).std()
    flag = (sa > m + 2.0 * sd).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_097_shareswadil_split_adj_pct_change_252d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _safe_div(sa - sa.shift(YDAYS), sa.shift(YDAYS)).diff()

def f19_dssp_098_shareswadil_split_adj_pct_change_756d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _safe_div(sa - sa.shift(DDAYS_3Y), sa.shift(DDAYS_3Y)).diff()

def f19_dssp_099_days_since_shareswadil_split_adj_max_756d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _days_since_max(sa, DDAYS_3Y).diff()

def f19_dssp_100_shareswadil_split_adj_acceleration_63d_d1(shareswadil: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = shareswadil * sharefactor
    return _safe_log(sa).diff(QDAYS).diff(QDAYS).diff()

def f19_dssp_101_dilution_intensity_1y_log_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(YDAYS).diff()

def f19_dssp_102_dilution_intensity_3y_log_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(DDAYS_3Y).diff()

def f19_dssp_103_dilution_intensity_5y_log_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    return _safe_log(sa).diff(DDAYS_5Y).diff()

def f19_dssp_104_dilution_intensity_5y_minus_3y_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    return (sa.diff(DDAYS_5Y) - sa.diff(DDAYS_3Y)).diff()

def f19_dssp_105_dilution_intensity_3y_minus_1y_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    return (sa.diff(DDAYS_3Y) - sa.diff(YDAYS)).diff()

def f19_dssp_106_dilution_intensity_acceleration_3y_vs_1y_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    return (_safe_div(sa.diff(YDAYS), sa.diff(DDAYS_3Y) / 3.0) - 1.0).diff()

def f19_dssp_107_dilution_intensity_1y_vs_5y_log_ratio_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    return (sa.diff(YDAYS) - sa.diff(DDAYS_5Y) / 5.0).diff()

def f19_dssp_108_dilution_intensity_above_15pct_count_5y_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(YDAYS)
    flag = (d > 0.15).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff()

def f19_dssp_109_dilution_intensity_above_30pct_indicator_5y_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(YDAYS)
    flag = (d > 0.3).astype(float)
    cnt = flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return (cnt > 0).astype(float).where(cnt.notna(), np.nan).diff()

def f19_dssp_110_dilution_consecutive_positive_count_5y_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    flag = (sa.diff(QDAYS) > 0).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff()

def f19_dssp_111_dilution_consecutive_positive_streak_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    flag = (sa.diff(QDAYS) > 0).astype(int)
    return _streak_above_zero(flag, YDAYS).diff()

def f19_dssp_112_days_since_negative_dilution_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    flag = (sa.diff(MDAYS) < 0).astype(float)
    return _recency_since_event(flag, YDAYS).diff()

def f19_dssp_113_dilution_volatility_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(MDAYS)
    return d.rolling(YDAYS, min_periods=QDAYS).std().diff()

def f19_dssp_114_dilution_volatility_zscore_long_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(MDAYS)
    v = d.rolling(YDAYS, min_periods=QDAYS).std()
    return _rolling_zscore(v, YDAYS).diff()

def f19_dssp_115_dilution_jump_count_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(MDAYS)
    m = d.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = d.rolling(YDAYS, min_periods=QDAYS).std()
    flag = (d > m + 2.0 * sd).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_116_dilution_burst_intensity_max_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    return sa.diff(MDAYS).rolling(YDAYS, min_periods=QDAYS).max().diff()

def f19_dssp_117_dilution_burst_concentration_top1_event_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(MDAYS)
    mx = d.rolling(YDAYS, min_periods=QDAYS).max()
    pos_sum = d.clip(lower=0).rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(mx, pos_sum).diff()

def f19_dssp_118_dilution_event_pattern_score_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    flag = (sa.diff(MDAYS) > 0).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f19_dssp_119_dilution_recent_burst_within_63d_indicator_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(MDAYS)
    m = d.rolling(YDAYS, min_periods=QDAYS).mean()
    sd = d.rolling(YDAYS, min_periods=QDAYS).std()
    flag = (d > m + 2.0 * sd).astype(float)
    cnt = flag.rolling(QDAYS, min_periods=MDAYS).sum()
    return (cnt > 0).astype(float).where(cnt.notna(), np.nan).diff()

def f19_dssp_120_dilution_smoothed_trend_252d_slope_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    return _rolling_slope(sa, YDAYS).diff()

def f19_dssp_121_dilution_smoothed_trend_756d_slope_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    return _rolling_slope(sa, DDAYS_3Y).diff()

def f19_dssp_122_dilution_trend_inflection_count_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    sg = np.sign(sa.diff(MDAYS).fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)
    return flip.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_123_dilution_persistence_above_long_mean_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = sharesbas * sharefactor
    m = sa.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (sa > m).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f19_dssp_124_dilution_3y_log_diff_minus_long_baseline_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d3 = sa.diff(DDAYS_3Y)
    base = d3.rolling(YDAYS, min_periods=QDAYS).mean()
    return (d3 - base).diff()

def f19_dssp_125_dilution_5y_log_diff_vs_252d_baseline_ratio_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d5 = sa.diff(DDAYS_5Y)
    base = d5.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(d5, base).diff()

def f19_dssp_126_diluted_dilution_premium_1y_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return (_safe_log(shareswadil).diff(YDAYS) - _safe_log(shareswa).diff(YDAYS)).diff()

def f19_dssp_127_diluted_dilution_premium_3y_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return (_safe_log(shareswadil).diff(DDAYS_3Y) - _safe_log(shareswa).diff(DDAYS_3Y)).diff()

def f19_dssp_128_diluted_dilution_premium_5y_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return (_safe_log(shareswadil).diff(DDAYS_5Y) - _safe_log(shareswa).diff(DDAYS_5Y)).diff()

def f19_dssp_129_diluted_dilution_premium_acceleration_1y_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    prem = _safe_log(shareswadil).diff(YDAYS) - _safe_log(shareswa).diff(YDAYS)
    return prem.diff(MDAYS).diff()

def f19_dssp_130_diluted_minus_basic_log_diff_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswadil - shareswa).diff(YDAYS).diff()

def f19_dssp_131_diluted_minus_basic_log_diff_756d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswadil - shareswa).diff(DDAYS_3Y).diff()

def f19_dssp_132_diluted_minus_basic_pct_above_5pct_count_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    ratio = _safe_div(shareswadil - shareswa, shareswa)
    flag = (ratio >= 0.05).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_133_diluted_minus_basic_above_long_mean_streak_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    m = over.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = (over > m).astype(int)
    return _max_streak_above_zero(flag, YDAYS).diff()

def f19_dssp_134_diluted_minus_basic_acceleration_63d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _safe_log(shareswadil - shareswa).diff(QDAYS).diff(QDAYS).diff()

def f19_dssp_135_diluted_overhang_to_split_adj_sharesbas_ratio_d1(shareswadil: pd.Series, shareswa: pd.Series, sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    sa = sharesbas * sharefactor
    return _safe_div(over, sa).diff()

def f19_dssp_136_diluted_overhang_to_split_adj_sharesbas_zscore_252d_d1(shareswadil: pd.Series, shareswa: pd.Series, sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    sa = sharesbas * sharefactor
    r = _safe_div(over, sa)
    return _rolling_zscore(r, YDAYS).diff()

def f19_dssp_137_diluted_overhang_rank_pct_5y_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    return _rolling_rank_pct(shareswadil - shareswa, DDAYS_5Y).diff()

def f19_dssp_138_diluted_overhang_growing_streak_3y_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    flag = (over.diff(MDAYS) > 0).astype(int)
    return _max_streak_above_zero(flag, DDAYS_3Y).diff()

def f19_dssp_139_diluted_overhang_volatility_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    return _safe_log(over).diff(MDAYS).rolling(YDAYS, min_periods=QDAYS).std().diff()

def f19_dssp_140_diluted_overhang_max_jump_252d_d1(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    over = shareswadil - shareswa
    return _safe_log(over).diff(MDAYS).rolling(YDAYS, min_periods=QDAYS).max().diff()

def f19_dssp_141_composite_dilution_topping_5y_score_d1(sharesbas: pd.Series, sharefactor: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    intensity = sa.diff(DDAYS_5Y)
    over_ratio = _safe_div(shareswadil - shareswa, shareswa)
    r1 = _rolling_rank_pct(intensity, DDAYS_5Y)
    r2 = _rolling_rank_pct(over_ratio, DDAYS_5Y)
    score = (r1 + r2) / 2.0
    return score.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f19_dssp_142_composite_dilution_distress_252d_score_d1(sharesbas: pd.Series, sharefactor: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d1y = sa.diff(YDAYS)
    over_ratio = _safe_div(shareswadil - shareswa, shareswa)
    rs_flag = (sharefactor.diff() < 0).astype(float)
    rs_in_252 = rs_flag.rolling(YDAYS, min_periods=QDAYS).sum() > 0
    flag = ((d1y > 0.15) & (over_ratio > 0.05) & rs_in_252).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f19_dssp_143_dilution_quintile_top_count_5y_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(YDAYS)
    thr = d.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.8)
    flag = (d >= thr).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff()

def f19_dssp_144_dilution_acceleration_with_overhang_score_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d_change = sa.diff(YDAYS).diff(MDAYS)
    over_z = _rolling_zscore(shareswadil - shareswa, YDAYS)
    flag = ((d_change > 0) & (over_z > 1.0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f19_dssp_145_sharesbas_log_diff_with_overhang_burst_count_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    d = sa.diff(MDAYS)
    over_z = _rolling_zscore(shareswadil - shareswa, YDAYS)
    flag = ((d > 0) & (over_z > 2.0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_146_sharefactor_decrease_with_dilution_burst_count_252d_d1(sharefactor: pd.Series, sharesbas: pd.Series) -> pd.Series:
    sf_neg = sharefactor.diff() < 0
    sb_burst = _safe_log(sharesbas).diff(MDAYS) > 0.05
    flag = (sf_neg & sb_burst).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_147_dilution_burst_after_sharefactor_decrease_count_252d_d1(sharefactor: pd.Series, sharesbas: pd.Series) -> pd.Series:
    rs_flag = (sharefactor.diff() < 0).astype(float)
    rs_in_63 = rs_flag.rolling(QDAYS, min_periods=MDAYS).sum() > 0
    sb_burst = _safe_log(sharesbas).diff(MDAYS) > 0.05
    flag = (rs_in_63 & sb_burst).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f19_dssp_148_dilution_velocity_long_minus_short_zscore_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    diff = sa.diff(DDAYS_3Y) / 3.0 - sa.diff(YDAYS)
    return _rolling_zscore(diff, YDAYS).diff()

def f19_dssp_149_composite_dilution_blowoff_score_252d_d1(sharesbas: pd.Series, sharefactor: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    intensity = sa.diff(YDAYS)
    over_ratio = _safe_div(shareswadil - shareswa, shareswa)
    r1 = _rolling_rank_pct(intensity, YDAYS)
    r2 = _rolling_rank_pct(over_ratio, YDAYS)
    return (r1 * r2).rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f19_dssp_150_composite_dilution_topping_score_5y_d1(sharesbas: pd.Series, sharefactor: pd.Series, shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    sa = _safe_log(sharesbas * sharefactor)
    r3y = _rolling_rank_pct(sa.diff(DDAYS_3Y), DDAYS_5Y)
    r1y = _rolling_rank_pct(sa.diff(YDAYS), DDAYS_5Y)
    over_ratio = _safe_div(shareswadil - shareswa, shareswa)
    ro = _rolling_rank_pct(over_ratio, DDAYS_5Y)
    rs_flag = (sharefactor.diff() < 0).astype(float)
    rs_in_5y = (rs_flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum() > 0).astype(float)
    score = (r3y + r1y + ro + rs_in_5y) / 4.0
    return score.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff()
DILUTION_STRUCTURE_SNAPSHOT_D1_REGISTRY_076_150 = {'f19_dssp_076_sharesbas_split_adj_log_diff_21d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_076_sharesbas_split_adj_log_diff_21d_d1}, 'f19_dssp_077_sharesbas_split_adj_log_diff_63d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_077_sharesbas_split_adj_log_diff_63d_d1}, 'f19_dssp_078_sharesbas_split_adj_log_diff_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_078_sharesbas_split_adj_log_diff_252d_d1}, 'f19_dssp_079_sharesbas_split_adj_log_diff_756d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_079_sharesbas_split_adj_log_diff_756d_d1}, 'f19_dssp_080_sharesbas_split_adj_log_diff_1260d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_080_sharesbas_split_adj_log_diff_1260d_d1}, 'f19_dssp_081_sharesbas_split_adj_zscore_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_081_sharesbas_split_adj_zscore_252d_d1}, 'f19_dssp_082_sharesbas_split_adj_pct_change_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_082_sharesbas_split_adj_pct_change_252d_d1}, 'f19_dssp_083_sharesbas_split_adj_rank_pct_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_083_sharesbas_split_adj_rank_pct_252d_d1}, 'f19_dssp_084_sharesbas_split_adj_distance_to_252d_max_log_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_084_sharesbas_split_adj_distance_to_252d_max_log_d1}, 'f19_dssp_085_sharesbas_split_adj_acceleration_21d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_085_sharesbas_split_adj_acceleration_21d_d1}, 'f19_dssp_086_sharesbas_split_adj_pct_above_long_mean_63d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_086_sharesbas_split_adj_pct_above_long_mean_63d_d1}, 'f19_dssp_087_sharesbas_split_adj_above_p90_count_63d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_087_sharesbas_split_adj_above_p90_count_63d_d1}, 'f19_dssp_088_sharesbas_split_adj_top_decile_count_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_088_sharesbas_split_adj_top_decile_count_252d_d1}, 'f19_dssp_089_sharesbas_split_adj_log_diff_5y_minus_long_baseline_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_089_sharesbas_split_adj_log_diff_5y_minus_long_baseline_d1}, 'f19_dssp_090_sharesbas_split_adj_3y_to_5y_log_ratio_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_090_sharesbas_split_adj_3y_to_5y_log_ratio_d1}, 'f19_dssp_091_shareswadil_split_adj_log_diff_252d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_091_shareswadil_split_adj_log_diff_252d_d1}, 'f19_dssp_092_shareswadil_split_adj_log_diff_756d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_092_shareswadil_split_adj_log_diff_756d_d1}, 'f19_dssp_093_shareswadil_split_adj_log_diff_1260d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_093_shareswadil_split_adj_log_diff_1260d_d1}, 'f19_dssp_094_shareswadil_split_adj_rank_pct_252d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_094_shareswadil_split_adj_rank_pct_252d_d1}, 'f19_dssp_095_shareswadil_split_adj_zscore_252d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_095_shareswadil_split_adj_zscore_252d_d1}, 'f19_dssp_096_shareswadil_split_adj_above_2sigma_count_252d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_096_shareswadil_split_adj_above_2sigma_count_252d_d1}, 'f19_dssp_097_shareswadil_split_adj_pct_change_252d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_097_shareswadil_split_adj_pct_change_252d_d1}, 'f19_dssp_098_shareswadil_split_adj_pct_change_756d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_098_shareswadil_split_adj_pct_change_756d_d1}, 'f19_dssp_099_days_since_shareswadil_split_adj_max_756d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_099_days_since_shareswadil_split_adj_max_756d_d1}, 'f19_dssp_100_shareswadil_split_adj_acceleration_63d_d1': {'inputs': ['shareswadil', 'sharefactor'], 'func': f19_dssp_100_shareswadil_split_adj_acceleration_63d_d1}, 'f19_dssp_101_dilution_intensity_1y_log_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_101_dilution_intensity_1y_log_d1}, 'f19_dssp_102_dilution_intensity_3y_log_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_102_dilution_intensity_3y_log_d1}, 'f19_dssp_103_dilution_intensity_5y_log_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_103_dilution_intensity_5y_log_d1}, 'f19_dssp_104_dilution_intensity_5y_minus_3y_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_104_dilution_intensity_5y_minus_3y_d1}, 'f19_dssp_105_dilution_intensity_3y_minus_1y_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_105_dilution_intensity_3y_minus_1y_d1}, 'f19_dssp_106_dilution_intensity_acceleration_3y_vs_1y_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_106_dilution_intensity_acceleration_3y_vs_1y_d1}, 'f19_dssp_107_dilution_intensity_1y_vs_5y_log_ratio_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_107_dilution_intensity_1y_vs_5y_log_ratio_d1}, 'f19_dssp_108_dilution_intensity_above_15pct_count_5y_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_108_dilution_intensity_above_15pct_count_5y_d1}, 'f19_dssp_109_dilution_intensity_above_30pct_indicator_5y_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_109_dilution_intensity_above_30pct_indicator_5y_d1}, 'f19_dssp_110_dilution_consecutive_positive_count_5y_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_110_dilution_consecutive_positive_count_5y_d1}, 'f19_dssp_111_dilution_consecutive_positive_streak_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_111_dilution_consecutive_positive_streak_d1}, 'f19_dssp_112_days_since_negative_dilution_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_112_days_since_negative_dilution_252d_d1}, 'f19_dssp_113_dilution_volatility_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_113_dilution_volatility_252d_d1}, 'f19_dssp_114_dilution_volatility_zscore_long_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_114_dilution_volatility_zscore_long_d1}, 'f19_dssp_115_dilution_jump_count_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_115_dilution_jump_count_252d_d1}, 'f19_dssp_116_dilution_burst_intensity_max_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_116_dilution_burst_intensity_max_252d_d1}, 'f19_dssp_117_dilution_burst_concentration_top1_event_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_117_dilution_burst_concentration_top1_event_252d_d1}, 'f19_dssp_118_dilution_event_pattern_score_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_118_dilution_event_pattern_score_252d_d1}, 'f19_dssp_119_dilution_recent_burst_within_63d_indicator_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_119_dilution_recent_burst_within_63d_indicator_d1}, 'f19_dssp_120_dilution_smoothed_trend_252d_slope_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_120_dilution_smoothed_trend_252d_slope_d1}, 'f19_dssp_121_dilution_smoothed_trend_756d_slope_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_121_dilution_smoothed_trend_756d_slope_d1}, 'f19_dssp_122_dilution_trend_inflection_count_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_122_dilution_trend_inflection_count_252d_d1}, 'f19_dssp_123_dilution_persistence_above_long_mean_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_123_dilution_persistence_above_long_mean_252d_d1}, 'f19_dssp_124_dilution_3y_log_diff_minus_long_baseline_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_124_dilution_3y_log_diff_minus_long_baseline_d1}, 'f19_dssp_125_dilution_5y_log_diff_vs_252d_baseline_ratio_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_125_dilution_5y_log_diff_vs_252d_baseline_ratio_d1}, 'f19_dssp_126_diluted_dilution_premium_1y_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_126_diluted_dilution_premium_1y_d1}, 'f19_dssp_127_diluted_dilution_premium_3y_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_127_diluted_dilution_premium_3y_d1}, 'f19_dssp_128_diluted_dilution_premium_5y_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_128_diluted_dilution_premium_5y_d1}, 'f19_dssp_129_diluted_dilution_premium_acceleration_1y_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_129_diluted_dilution_premium_acceleration_1y_d1}, 'f19_dssp_130_diluted_minus_basic_log_diff_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_130_diluted_minus_basic_log_diff_252d_d1}, 'f19_dssp_131_diluted_minus_basic_log_diff_756d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_131_diluted_minus_basic_log_diff_756d_d1}, 'f19_dssp_132_diluted_minus_basic_pct_above_5pct_count_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_132_diluted_minus_basic_pct_above_5pct_count_252d_d1}, 'f19_dssp_133_diluted_minus_basic_above_long_mean_streak_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_133_diluted_minus_basic_above_long_mean_streak_252d_d1}, 'f19_dssp_134_diluted_minus_basic_acceleration_63d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_134_diluted_minus_basic_acceleration_63d_d1}, 'f19_dssp_135_diluted_overhang_to_split_adj_sharesbas_ratio_d1': {'inputs': ['shareswadil', 'shareswa', 'sharesbas', 'sharefactor'], 'func': f19_dssp_135_diluted_overhang_to_split_adj_sharesbas_ratio_d1}, 'f19_dssp_136_diluted_overhang_to_split_adj_sharesbas_zscore_252d_d1': {'inputs': ['shareswadil', 'shareswa', 'sharesbas', 'sharefactor'], 'func': f19_dssp_136_diluted_overhang_to_split_adj_sharesbas_zscore_252d_d1}, 'f19_dssp_137_diluted_overhang_rank_pct_5y_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_137_diluted_overhang_rank_pct_5y_d1}, 'f19_dssp_138_diluted_overhang_growing_streak_3y_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_138_diluted_overhang_growing_streak_3y_d1}, 'f19_dssp_139_diluted_overhang_volatility_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_139_diluted_overhang_volatility_252d_d1}, 'f19_dssp_140_diluted_overhang_max_jump_252d_d1': {'inputs': ['shareswadil', 'shareswa'], 'func': f19_dssp_140_diluted_overhang_max_jump_252d_d1}, 'f19_dssp_141_composite_dilution_topping_5y_score_d1': {'inputs': ['sharesbas', 'sharefactor', 'shareswadil', 'shareswa'], 'func': f19_dssp_141_composite_dilution_topping_5y_score_d1}, 'f19_dssp_142_composite_dilution_distress_252d_score_d1': {'inputs': ['sharesbas', 'sharefactor', 'shareswadil', 'shareswa'], 'func': f19_dssp_142_composite_dilution_distress_252d_score_d1}, 'f19_dssp_143_dilution_quintile_top_count_5y_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_143_dilution_quintile_top_count_5y_d1}, 'f19_dssp_144_dilution_acceleration_with_overhang_score_252d_d1': {'inputs': ['sharesbas', 'sharefactor', 'shareswadil', 'shareswa'], 'func': f19_dssp_144_dilution_acceleration_with_overhang_score_252d_d1}, 'f19_dssp_145_sharesbas_log_diff_with_overhang_burst_count_252d_d1': {'inputs': ['sharesbas', 'sharefactor', 'shareswadil', 'shareswa'], 'func': f19_dssp_145_sharesbas_log_diff_with_overhang_burst_count_252d_d1}, 'f19_dssp_146_sharefactor_decrease_with_dilution_burst_count_252d_d1': {'inputs': ['sharefactor', 'sharesbas'], 'func': f19_dssp_146_sharefactor_decrease_with_dilution_burst_count_252d_d1}, 'f19_dssp_147_dilution_burst_after_sharefactor_decrease_count_252d_d1': {'inputs': ['sharefactor', 'sharesbas'], 'func': f19_dssp_147_dilution_burst_after_sharefactor_decrease_count_252d_d1}, 'f19_dssp_148_dilution_velocity_long_minus_short_zscore_252d_d1': {'inputs': ['sharesbas', 'sharefactor'], 'func': f19_dssp_148_dilution_velocity_long_minus_short_zscore_252d_d1}, 'f19_dssp_149_composite_dilution_blowoff_score_252d_d1': {'inputs': ['sharesbas', 'sharefactor', 'shareswadil', 'shareswa'], 'func': f19_dssp_149_composite_dilution_blowoff_score_252d_d1}, 'f19_dssp_150_composite_dilution_topping_score_5y_d1': {'inputs': ['sharesbas', 'sharefactor', 'shareswadil', 'shareswa'], 'func': f19_dssp_150_composite_dilution_topping_score_5y_d1}}
