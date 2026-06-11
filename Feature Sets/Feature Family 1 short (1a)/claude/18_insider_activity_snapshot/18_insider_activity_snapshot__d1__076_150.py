"""insider_activity_snapshot d1 features 076_150 — 1st-derivative wrappers.

Each function inlines the corresponding base body and appends .diff() so the output is the first bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
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

def f18_iasp_076_ceo_buy_value_zscore_252d_d1(ceo_buy_value: pd.Series) -> pd.Series:
    return _rolling_zscore(ceo_buy_value, YDAYS).diff()

def f18_iasp_077_days_since_ceo_buy_event_252d_d1(ceo_buy_value: pd.Series) -> pd.Series:
    flag = (ceo_buy_value.fillna(0) > 0).astype(float)
    return _recency_since_event(flag, YDAYS).diff()

def f18_iasp_078_ceo_buy_to_sell_log_ratio_63d_d1(ceo_buy_value: pd.Series, ceo_sell_value: pd.Series) -> pd.Series:
    b = ceo_buy_value.rolling(QDAYS, min_periods=MDAYS).sum()
    s = ceo_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_log(_safe_div(b, s)).diff()

def f18_iasp_079_cfo_buy_value_zscore_252d_d1(cfo_buy_value: pd.Series) -> pd.Series:
    return _rolling_zscore(cfo_buy_value, YDAYS).diff()

def f18_iasp_080_days_since_cfo_buy_event_252d_d1(cfo_buy_value: pd.Series) -> pd.Series:
    flag = (cfo_buy_value.fillna(0) > 0).astype(float)
    return _recency_since_event(flag, YDAYS).diff()

def f18_iasp_081_ceo_cfo_joint_sell_days_count_63d_d1(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series) -> pd.Series:
    flag = ((ceo_sell_value.fillna(0) > 0) & (cfo_sell_value.fillna(0) > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_082_multi_role_sell_days_count_63d_d1(officer_sell_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    flag = ((officer_sell_value.fillna(0) > 0) & (director_sell_value.fillna(0) > 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_083_mass_sell_event_count_63d_d1(insider_sell_count: pd.Series) -> pd.Series:
    flag = (insider_sell_count >= 3).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_084_insider_breadth_sell_pct_63d_d1(insider_sell_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    den = insider_sell_count.fillna(0) + insider_buy_count.fillna(0)
    ratio = _safe_div(insider_sell_count, den)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f18_iasp_085_insider_breadth_buy_pct_63d_d1(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    den = insider_sell_count.fillna(0) + insider_buy_count.fillna(0)
    ratio = _safe_div(insider_buy_count, den)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f18_iasp_086_insider_breadth_net_count_pct_63d_d1(insider_sell_count: pd.Series, insider_buy_count: pd.Series) -> pd.Series:
    den = insider_sell_count.fillna(0) + insider_buy_count.fillna(0)
    num = insider_sell_count.fillna(0) - insider_buy_count.fillna(0)
    ratio = _safe_div(num, den)
    return ratio.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f18_iasp_087_cross_role_sell_dominance_index_63d_d1(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series, officer_sell_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    csuite = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)).rolling(QDAYS, min_periods=MDAYS).sum()
    total = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0) + officer_sell_value.fillna(0) + director_sell_value.fillna(0)).rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(csuite, total).diff()

def f18_iasp_088_c_suite_sell_share_of_total_63d_d1(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    csuite = (ceo_sell_value.fillna(0) + cfo_sell_value.fillna(0)).rolling(QDAYS, min_periods=MDAYS).sum()
    all_ = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(csuite, all_).diff()

def f18_iasp_089_director_sell_share_of_total_63d_d1(director_sell_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    d = director_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    all_ = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(d, all_).diff()

def f18_iasp_090_insider_sell_concentration_top_role_63d_d1(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series, officer_sell_value: pd.Series, director_sell_value: pd.Series) -> pd.Series:
    ceo = ceo_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    cfo = cfo_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    off_ = officer_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    dir_ = director_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    df = pd.concat([ceo, cfo, off_, dir_], axis=1)
    mx = df.max(axis=1)
    tot = df.sum(axis=1)
    return _safe_div(mx, tot).diff()

def f18_iasp_091_mass_buy_event_count_63d_d1(insider_buy_count: pd.Series) -> pd.Series:
    flag = (insider_buy_count >= 3).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_092_insider_breadth_buy_minus_sell_count_63d_d1(insider_buy_count: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    return (insider_buy_count.fillna(0) - insider_sell_count.fillna(0)).rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_093_form4_filings_count_zscore_252d_d1(form4_filings_count: pd.Series) -> pd.Series:
    return _rolling_zscore(form4_filings_count, YDAYS).diff()

def f18_iasp_094_form4_filings_count_sum_63d_d1(form4_filings_count: pd.Series) -> pd.Series:
    return form4_filings_count.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_095_form4_filings_count_top_decile_count_63d_d1(form4_filings_count: pd.Series) -> pd.Series:
    thr = form4_filings_count.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (form4_filings_count >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_096_form4_late_filings_count_63d_d1(late_filings_count: pd.Series) -> pd.Series:
    return late_filings_count.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_097_form4_late_filings_pct_63d_d1(late_filings_count: pd.Series, form4_filings_count: pd.Series) -> pd.Series:
    late = late_filings_count.rolling(QDAYS, min_periods=MDAYS).sum()
    tot = form4_filings_count.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(late, tot).diff()

def f18_iasp_098_form4_late_filings_zscore_252d_d1(late_filings_count: pd.Series) -> pd.Series:
    return _rolling_zscore(late_filings_count, YDAYS).diff()

def f18_iasp_099_form4_late_burst_count_63d_d1(late_filings_count: pd.Series) -> pd.Series:
    flag = (late_filings_count >= 2).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_100_form4_filings_concentration_top5_days_63d_d1(form4_filings_count: pd.Series) -> pd.Series:

    def _tm(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)[-5:].sum()
        tot = w.sum()
        return s / tot if tot > 0 else np.nan
    return form4_filings_count.rolling(QDAYS, min_periods=MDAYS).apply(_tm, raw=True).diff()

def f18_iasp_101_planned_sell_value_zscore_252d_d1(planned_sell_value: pd.Series) -> pd.Series:
    return _rolling_zscore(planned_sell_value, YDAYS).diff()

def f18_iasp_102_unplanned_sell_value_zscore_252d_d1(unplanned_sell_value: pd.Series) -> pd.Series:
    return _rolling_zscore(unplanned_sell_value, YDAYS).diff()

def f18_iasp_103_planned_vs_unplanned_sell_log_ratio_63d_d1(planned_sell_value: pd.Series, unplanned_sell_value: pd.Series) -> pd.Series:
    p = planned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    u = unplanned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_log(_safe_div(p, u)).diff()

def f18_iasp_104_unplanned_sell_share_of_total_63d_d1(unplanned_sell_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    u = unplanned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    t = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(u, t).diff()

def f18_iasp_105_unplanned_sell_top_decile_count_63d_d1(unplanned_sell_value: pd.Series) -> pd.Series:
    thr = unplanned_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (unplanned_sell_value >= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_106_unplanned_sell_log_diff_21d_d1(unplanned_sell_value: pd.Series) -> pd.Series:
    return _safe_log(unplanned_sell_value).diff(MDAYS).diff()

def f18_iasp_107_unplanned_sell_sum_63d_to_sma_252d_d1(unplanned_sell_value: pd.Series) -> pd.Series:
    s63 = unplanned_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    sma = unplanned_sell_value.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(s63, sma * QDAYS).diff()

def f18_iasp_108_days_since_unplanned_sell_burst_252d_d1(unplanned_sell_value: pd.Series) -> pd.Series:
    thr = unplanned_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = (unplanned_sell_value >= thr).astype(float)
    return _recency_since_event(flag, YDAYS).diff()

def f18_iasp_109_unplanned_sell_concentration_top3_days_63d_d1(unplanned_sell_value: pd.Series) -> pd.Series:

    def _tm(w):
        if np.isnan(w).any():
            return np.nan
        s = np.sort(w)[-3:].sum()
        tot = w.sum()
        return s / tot if tot > 0 else np.nan
    return unplanned_sell_value.rolling(QDAYS, min_periods=MDAYS).apply(_tm, raw=True).diff()

def f18_iasp_110_unplanned_sell_count_zscore_252d_d1(unplanned_sell_count: pd.Series) -> pd.Series:
    return _rolling_zscore(unplanned_sell_count, YDAYS).diff()

def f18_iasp_111_planned_sell_dryup_streak_max_252d_d1(planned_sell_value: pd.Series) -> pd.Series:
    flag = (planned_sell_value.fillna(0) == 0).astype(int)
    return _max_streak_above_zero(flag, YDAYS).diff()

def f18_iasp_112_unplanned_sell_acceleration_21d_d1(unplanned_sell_value: pd.Series) -> pd.Series:
    return _safe_log(unplanned_sell_value).diff(MDAYS).diff(MDAYS).diff()

def f18_iasp_113_planned_minus_unplanned_log_ratio_change_21d_d1(planned_sell_value: pd.Series, unplanned_sell_value: pd.Series) -> pd.Series:
    return (_safe_log(planned_sell_value) - _safe_log(unplanned_sell_value)).diff(MDAYS).diff()

def f18_iasp_114_unplanned_sell_persistence_above_p75_252d_d1(unplanned_sell_value: pd.Series) -> pd.Series:
    thr = unplanned_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    flag = (unplanned_sell_value >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f18_iasp_115_sell_plan_mix_volatility_63d_d1(planned_sell_value: pd.Series, unplanned_sell_value: pd.Series) -> pd.Series:
    den = planned_sell_value.fillna(0) + unplanned_sell_value.fillna(0)
    ratio = _safe_div(unplanned_sell_value, den)
    return ratio.rolling(QDAYS, min_periods=MDAYS).std().diff()

def f18_iasp_116_insider_holdings_post_pct_change_21d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    return insider_holdings_post_pct.diff(MDAYS).diff()

def f18_iasp_117_insider_holdings_post_pct_change_63d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    return insider_holdings_post_pct.diff(QDAYS).diff()

def f18_iasp_118_insider_holdings_post_pct_change_252d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    return insider_holdings_post_pct.diff(YDAYS).diff()

def f18_iasp_119_insider_holdings_drop_zscore_252d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    d = insider_holdings_post_pct.diff(MDAYS)
    return _rolling_zscore(d, YDAYS).diff()

def f18_iasp_120_insider_holdings_under_p10_count_63d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    thr = insider_holdings_post_pct.rolling(YDAYS, min_periods=QDAYS).quantile(0.1)
    flag = (insider_holdings_post_pct <= thr).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_121_days_since_insider_holdings_max_252d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    return _days_since_max(insider_holdings_post_pct, YDAYS).diff()

def f18_iasp_122_insider_holdings_dryup_intensity_63d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    d = insider_holdings_post_pct.diff().clip(upper=0.0)
    return d.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f18_iasp_123_insider_holdings_acceleration_21d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    return insider_holdings_post_pct.diff(MDAYS).diff(MDAYS).diff()

def f18_iasp_124_insider_holdings_collapse_thrust_63d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    return _safe_log(insider_holdings_post_pct).diff(QDAYS).clip(upper=0.0).diff()

def f18_iasp_125_insider_holdings_min_in_252d_log_distance_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    mn = insider_holdings_post_pct.rolling(YDAYS, min_periods=QDAYS).min()
    return (_safe_log(insider_holdings_post_pct) - _safe_log(mn)).diff()

def f18_iasp_126_insider_holdings_above_p50_streak_max_63d_d1(insider_holdings_post_pct: pd.Series) -> pd.Series:
    med = insider_holdings_post_pct.rolling(YDAYS, min_periods=QDAYS).median()
    flag = (insider_holdings_post_pct - med > 0).astype(int)
    return _max_streak_above_zero(flag, QDAYS).diff()

def f18_iasp_127_ten_pct_holder_sell_value_zscore_252d_d1(ten_pct_holder_sell_value: pd.Series) -> pd.Series:
    return _rolling_zscore(ten_pct_holder_sell_value, YDAYS).diff()

def f18_iasp_128_ten_pct_holder_sell_value_sum_63d_d1(ten_pct_holder_sell_value: pd.Series) -> pd.Series:
    return ten_pct_holder_sell_value.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_129_ten_pct_holder_sell_log_diff_21d_d1(ten_pct_holder_sell_value: pd.Series) -> pd.Series:
    return _safe_log(ten_pct_holder_sell_value).diff(MDAYS).diff()

def f18_iasp_130_ten_pct_holder_share_of_sell_63d_d1(ten_pct_holder_sell_value: pd.Series, insider_sell_value: pd.Series) -> pd.Series:
    h = ten_pct_holder_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    t = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(h, t).diff()

def f18_iasp_131_sell_dominance_composite_63d_d1(insider_net_value: pd.Series, insider_sell_count: pd.Series, late_filings_count: pd.Series) -> pd.Series:
    flag = ((insider_net_value < 0) & (insider_sell_count >= 2) & (late_filings_count >= 1)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f18_iasp_132_ceo_cfo_simul_top_decile_count_63d_d1(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series) -> pd.Series:
    ceo_thr = ceo_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    cfo_thr = cfo_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((ceo_sell_value >= ceo_thr) & (cfo_sell_value >= cfo_thr)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_133_days_since_insider_buy_event_252d_d1(insider_buy_value: pd.Series) -> pd.Series:
    flag = (insider_buy_value.fillna(0) > 0).astype(float)
    return _recency_since_event(flag, YDAYS).diff()

def f18_iasp_134_insider_capitulation_signal_63d_d1(insider_sell_value: pd.Series, insider_sell_count: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    sell_thr = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((insider_sell_value >= sell_thr) & (insider_sell_count >= 3) & (insider_buy_value.fillna(0) == 0)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_135_sell_intensity_above_p95_count_252d_d1(insider_sell_value: pd.Series) -> pd.Series:
    thr = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    flag = (insider_sell_value >= thr).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f18_iasp_136_sell_intensity_zscore_acceleration_21d_d1(insider_sell_value: pd.Series) -> pd.Series:
    z = _rolling_zscore(insider_sell_value, YDAYS)
    return z.diff(MDAYS).diff()

def f18_iasp_137_c_suite_sell_count_zscore_252d_d1(ceo_sell_value: pd.Series, cfo_sell_value: pd.Series) -> pd.Series:
    cnt = ((ceo_sell_value.fillna(0) > 0).astype(int) + (cfo_sell_value.fillna(0) > 0).astype(int)).astype(float)
    return _rolling_zscore(cnt, YDAYS).diff()

def f18_iasp_138_sell_to_buy_value_ratio_zscore_252d_d1(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    r = _safe_div(insider_sell_value, insider_buy_value)
    return _rolling_zscore(r, YDAYS).diff()

def f18_iasp_139_sell_burst_intensity_max_63d_d1(insider_sell_value: pd.Series) -> pd.Series:
    mx = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).max()
    med = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).median()
    return _safe_div(mx, med).diff()

def f18_iasp_140_high_value_sell_followed_by_zero_buy_count_63d_d1(insider_sell_value: pd.Series, insider_buy_value: pd.Series) -> pd.Series:
    sell = insider_sell_value.fillna(0) > 0
    buy = insider_buy_value.fillna(0) > 0
    zero_buy_window = buy.rolling(WDAYS, min_periods=2).sum() == 0
    flag = (sell & ~buy & zero_buy_window).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_141_multi_day_consecutive_net_sell_max_streak_252d_d1(insider_net_value: pd.Series) -> pd.Series:
    flag = (insider_net_value < 0).astype(int)
    return _max_streak_above_zero(flag, YDAYS).diff()

def f18_iasp_142_net_sell_intensity_topdecile_count_252d_d1(insider_net_value: pd.Series) -> pd.Series:
    abs_thr = insider_net_value.abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.9)
    flag = ((insider_net_value.abs() >= abs_thr) & (insider_net_value < 0)).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f18_iasp_143_sell_concentration_top1_day_share_of_63d_d1(insider_sell_value: pd.Series) -> pd.Series:
    mx = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).max()
    tot = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    return _safe_div(mx, tot).diff()

def f18_iasp_144_sell_concentration_top1_day_share_of_252d_d1(insider_sell_value: pd.Series) -> pd.Series:
    mx = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).max()
    tot = insider_sell_value.rolling(YDAYS, min_periods=QDAYS).sum()
    return _safe_div(mx, tot).diff()

def f18_iasp_145_net_sell_topping_score_63d_d1(insider_net_value: pd.Series, insider_sell_count: pd.Series) -> pd.Series:
    z_net = _rolling_zscore(insider_net_value, YDAYS)
    z_cnt = _rolling_zscore(insider_sell_count, YDAYS)
    return (-z_net * z_cnt).rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f18_iasp_146_net_sell_persistence_streak_max_63d_d1(insider_net_value: pd.Series) -> pd.Series:
    flag = (insider_net_value < 0).astype(int)
    return _max_streak_above_zero(flag, QDAYS).diff()

def f18_iasp_147_insider_signal_inflection_count_63d_d1(insider_net_value: pd.Series) -> pd.Series:
    sg = np.sign(insider_net_value.fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)
    return flip.rolling(QDAYS, min_periods=MDAYS).sum().diff()

def f18_iasp_148_composite_distress_insider_score_63d_d1(insider_net_value: pd.Series, insider_sell_value: pd.Series, insider_buy_value: pd.Series, late_filings_count: pd.Series) -> pd.Series:
    sell_z = _rolling_zscore(insider_sell_value, YDAYS)
    flag = ((insider_net_value < 0) & (sell_z > 1.0) & (insider_buy_value.fillna(0) == 0) & (late_filings_count >= 1)).astype(float)
    return flag.rolling(QDAYS, min_periods=MDAYS).mean().diff()

def f18_iasp_149_composite_insider_topping_score_252d_d1(insider_sell_value: pd.Series, insider_sell_count: pd.Series, ceo_sell_value: pd.Series, cfo_sell_value: pd.Series) -> pd.Series:
    r1 = _rolling_rank_pct(insider_sell_value, YDAYS)
    r2 = _rolling_rank_pct(insider_sell_count, YDAYS)
    r3 = _rolling_rank_pct(ceo_sell_value, YDAYS)
    r4 = _rolling_rank_pct(cfo_sell_value, YDAYS)
    score = (r1 + r2 + r3 + r4) / 4.0
    return score.rolling(YDAYS, min_periods=QDAYS).mean().diff()

def f18_iasp_150_composite_insider_blowoff_score_252d_d1(insider_sell_value: pd.Series, insider_buy_value: pd.Series, insider_holdings_post_pct: pd.Series) -> pd.Series:
    s63 = insider_sell_value.rolling(QDAYS, min_periods=MDAYS).sum()
    b63 = insider_buy_value.rolling(QDAYS, min_periods=MDAYS).sum()
    rs = _rolling_rank_pct(s63, YDAYS)
    rb = _rolling_rank_pct(b63, YDAYS)
    rh = _rolling_rank_pct(insider_holdings_post_pct, YDAYS)
    score = rs * (1.0 - rb) * (1.0 - rh)
    return score.rolling(YDAYS, min_periods=QDAYS).mean().diff()
INSIDER_ACTIVITY_SNAPSHOT_D1_REGISTRY_076_150 = {'f18_iasp_076_ceo_buy_value_zscore_252d_d1': {'inputs': ['ceo_buy_value'], 'func': f18_iasp_076_ceo_buy_value_zscore_252d_d1}, 'f18_iasp_077_days_since_ceo_buy_event_252d_d1': {'inputs': ['ceo_buy_value'], 'func': f18_iasp_077_days_since_ceo_buy_event_252d_d1}, 'f18_iasp_078_ceo_buy_to_sell_log_ratio_63d_d1': {'inputs': ['ceo_buy_value', 'ceo_sell_value'], 'func': f18_iasp_078_ceo_buy_to_sell_log_ratio_63d_d1}, 'f18_iasp_079_cfo_buy_value_zscore_252d_d1': {'inputs': ['cfo_buy_value'], 'func': f18_iasp_079_cfo_buy_value_zscore_252d_d1}, 'f18_iasp_080_days_since_cfo_buy_event_252d_d1': {'inputs': ['cfo_buy_value'], 'func': f18_iasp_080_days_since_cfo_buy_event_252d_d1}, 'f18_iasp_081_ceo_cfo_joint_sell_days_count_63d_d1': {'inputs': ['ceo_sell_value', 'cfo_sell_value'], 'func': f18_iasp_081_ceo_cfo_joint_sell_days_count_63d_d1}, 'f18_iasp_082_multi_role_sell_days_count_63d_d1': {'inputs': ['officer_sell_value', 'director_sell_value'], 'func': f18_iasp_082_multi_role_sell_days_count_63d_d1}, 'f18_iasp_083_mass_sell_event_count_63d_d1': {'inputs': ['insider_sell_count'], 'func': f18_iasp_083_mass_sell_event_count_63d_d1}, 'f18_iasp_084_insider_breadth_sell_pct_63d_d1': {'inputs': ['insider_sell_count', 'insider_buy_count'], 'func': f18_iasp_084_insider_breadth_sell_pct_63d_d1}, 'f18_iasp_085_insider_breadth_buy_pct_63d_d1': {'inputs': ['insider_buy_count', 'insider_sell_count'], 'func': f18_iasp_085_insider_breadth_buy_pct_63d_d1}, 'f18_iasp_086_insider_breadth_net_count_pct_63d_d1': {'inputs': ['insider_sell_count', 'insider_buy_count'], 'func': f18_iasp_086_insider_breadth_net_count_pct_63d_d1}, 'f18_iasp_087_cross_role_sell_dominance_index_63d_d1': {'inputs': ['ceo_sell_value', 'cfo_sell_value', 'officer_sell_value', 'director_sell_value'], 'func': f18_iasp_087_cross_role_sell_dominance_index_63d_d1}, 'f18_iasp_088_c_suite_sell_share_of_total_63d_d1': {'inputs': ['ceo_sell_value', 'cfo_sell_value', 'insider_sell_value'], 'func': f18_iasp_088_c_suite_sell_share_of_total_63d_d1}, 'f18_iasp_089_director_sell_share_of_total_63d_d1': {'inputs': ['director_sell_value', 'insider_sell_value'], 'func': f18_iasp_089_director_sell_share_of_total_63d_d1}, 'f18_iasp_090_insider_sell_concentration_top_role_63d_d1': {'inputs': ['ceo_sell_value', 'cfo_sell_value', 'officer_sell_value', 'director_sell_value'], 'func': f18_iasp_090_insider_sell_concentration_top_role_63d_d1}, 'f18_iasp_091_mass_buy_event_count_63d_d1': {'inputs': ['insider_buy_count'], 'func': f18_iasp_091_mass_buy_event_count_63d_d1}, 'f18_iasp_092_insider_breadth_buy_minus_sell_count_63d_d1': {'inputs': ['insider_buy_count', 'insider_sell_count'], 'func': f18_iasp_092_insider_breadth_buy_minus_sell_count_63d_d1}, 'f18_iasp_093_form4_filings_count_zscore_252d_d1': {'inputs': ['form4_filings_count'], 'func': f18_iasp_093_form4_filings_count_zscore_252d_d1}, 'f18_iasp_094_form4_filings_count_sum_63d_d1': {'inputs': ['form4_filings_count'], 'func': f18_iasp_094_form4_filings_count_sum_63d_d1}, 'f18_iasp_095_form4_filings_count_top_decile_count_63d_d1': {'inputs': ['form4_filings_count'], 'func': f18_iasp_095_form4_filings_count_top_decile_count_63d_d1}, 'f18_iasp_096_form4_late_filings_count_63d_d1': {'inputs': ['late_filings_count'], 'func': f18_iasp_096_form4_late_filings_count_63d_d1}, 'f18_iasp_097_form4_late_filings_pct_63d_d1': {'inputs': ['late_filings_count', 'form4_filings_count'], 'func': f18_iasp_097_form4_late_filings_pct_63d_d1}, 'f18_iasp_098_form4_late_filings_zscore_252d_d1': {'inputs': ['late_filings_count'], 'func': f18_iasp_098_form4_late_filings_zscore_252d_d1}, 'f18_iasp_099_form4_late_burst_count_63d_d1': {'inputs': ['late_filings_count'], 'func': f18_iasp_099_form4_late_burst_count_63d_d1}, 'f18_iasp_100_form4_filings_concentration_top5_days_63d_d1': {'inputs': ['form4_filings_count'], 'func': f18_iasp_100_form4_filings_concentration_top5_days_63d_d1}, 'f18_iasp_101_planned_sell_value_zscore_252d_d1': {'inputs': ['planned_sell_value'], 'func': f18_iasp_101_planned_sell_value_zscore_252d_d1}, 'f18_iasp_102_unplanned_sell_value_zscore_252d_d1': {'inputs': ['unplanned_sell_value'], 'func': f18_iasp_102_unplanned_sell_value_zscore_252d_d1}, 'f18_iasp_103_planned_vs_unplanned_sell_log_ratio_63d_d1': {'inputs': ['planned_sell_value', 'unplanned_sell_value'], 'func': f18_iasp_103_planned_vs_unplanned_sell_log_ratio_63d_d1}, 'f18_iasp_104_unplanned_sell_share_of_total_63d_d1': {'inputs': ['unplanned_sell_value', 'insider_sell_value'], 'func': f18_iasp_104_unplanned_sell_share_of_total_63d_d1}, 'f18_iasp_105_unplanned_sell_top_decile_count_63d_d1': {'inputs': ['unplanned_sell_value'], 'func': f18_iasp_105_unplanned_sell_top_decile_count_63d_d1}, 'f18_iasp_106_unplanned_sell_log_diff_21d_d1': {'inputs': ['unplanned_sell_value'], 'func': f18_iasp_106_unplanned_sell_log_diff_21d_d1}, 'f18_iasp_107_unplanned_sell_sum_63d_to_sma_252d_d1': {'inputs': ['unplanned_sell_value'], 'func': f18_iasp_107_unplanned_sell_sum_63d_to_sma_252d_d1}, 'f18_iasp_108_days_since_unplanned_sell_burst_252d_d1': {'inputs': ['unplanned_sell_value'], 'func': f18_iasp_108_days_since_unplanned_sell_burst_252d_d1}, 'f18_iasp_109_unplanned_sell_concentration_top3_days_63d_d1': {'inputs': ['unplanned_sell_value'], 'func': f18_iasp_109_unplanned_sell_concentration_top3_days_63d_d1}, 'f18_iasp_110_unplanned_sell_count_zscore_252d_d1': {'inputs': ['unplanned_sell_count'], 'func': f18_iasp_110_unplanned_sell_count_zscore_252d_d1}, 'f18_iasp_111_planned_sell_dryup_streak_max_252d_d1': {'inputs': ['planned_sell_value'], 'func': f18_iasp_111_planned_sell_dryup_streak_max_252d_d1}, 'f18_iasp_112_unplanned_sell_acceleration_21d_d1': {'inputs': ['unplanned_sell_value'], 'func': f18_iasp_112_unplanned_sell_acceleration_21d_d1}, 'f18_iasp_113_planned_minus_unplanned_log_ratio_change_21d_d1': {'inputs': ['planned_sell_value', 'unplanned_sell_value'], 'func': f18_iasp_113_planned_minus_unplanned_log_ratio_change_21d_d1}, 'f18_iasp_114_unplanned_sell_persistence_above_p75_252d_d1': {'inputs': ['unplanned_sell_value'], 'func': f18_iasp_114_unplanned_sell_persistence_above_p75_252d_d1}, 'f18_iasp_115_sell_plan_mix_volatility_63d_d1': {'inputs': ['planned_sell_value', 'unplanned_sell_value'], 'func': f18_iasp_115_sell_plan_mix_volatility_63d_d1}, 'f18_iasp_116_insider_holdings_post_pct_change_21d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_116_insider_holdings_post_pct_change_21d_d1}, 'f18_iasp_117_insider_holdings_post_pct_change_63d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_117_insider_holdings_post_pct_change_63d_d1}, 'f18_iasp_118_insider_holdings_post_pct_change_252d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_118_insider_holdings_post_pct_change_252d_d1}, 'f18_iasp_119_insider_holdings_drop_zscore_252d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_119_insider_holdings_drop_zscore_252d_d1}, 'f18_iasp_120_insider_holdings_under_p10_count_63d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_120_insider_holdings_under_p10_count_63d_d1}, 'f18_iasp_121_days_since_insider_holdings_max_252d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_121_days_since_insider_holdings_max_252d_d1}, 'f18_iasp_122_insider_holdings_dryup_intensity_63d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_122_insider_holdings_dryup_intensity_63d_d1}, 'f18_iasp_123_insider_holdings_acceleration_21d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_123_insider_holdings_acceleration_21d_d1}, 'f18_iasp_124_insider_holdings_collapse_thrust_63d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_124_insider_holdings_collapse_thrust_63d_d1}, 'f18_iasp_125_insider_holdings_min_in_252d_log_distance_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_125_insider_holdings_min_in_252d_log_distance_d1}, 'f18_iasp_126_insider_holdings_above_p50_streak_max_63d_d1': {'inputs': ['insider_holdings_post_pct'], 'func': f18_iasp_126_insider_holdings_above_p50_streak_max_63d_d1}, 'f18_iasp_127_ten_pct_holder_sell_value_zscore_252d_d1': {'inputs': ['ten_pct_holder_sell_value'], 'func': f18_iasp_127_ten_pct_holder_sell_value_zscore_252d_d1}, 'f18_iasp_128_ten_pct_holder_sell_value_sum_63d_d1': {'inputs': ['ten_pct_holder_sell_value'], 'func': f18_iasp_128_ten_pct_holder_sell_value_sum_63d_d1}, 'f18_iasp_129_ten_pct_holder_sell_log_diff_21d_d1': {'inputs': ['ten_pct_holder_sell_value'], 'func': f18_iasp_129_ten_pct_holder_sell_log_diff_21d_d1}, 'f18_iasp_130_ten_pct_holder_share_of_sell_63d_d1': {'inputs': ['ten_pct_holder_sell_value', 'insider_sell_value'], 'func': f18_iasp_130_ten_pct_holder_share_of_sell_63d_d1}, 'f18_iasp_131_sell_dominance_composite_63d_d1': {'inputs': ['insider_net_value', 'insider_sell_count', 'late_filings_count'], 'func': f18_iasp_131_sell_dominance_composite_63d_d1}, 'f18_iasp_132_ceo_cfo_simul_top_decile_count_63d_d1': {'inputs': ['ceo_sell_value', 'cfo_sell_value'], 'func': f18_iasp_132_ceo_cfo_simul_top_decile_count_63d_d1}, 'f18_iasp_133_days_since_insider_buy_event_252d_d1': {'inputs': ['insider_buy_value'], 'func': f18_iasp_133_days_since_insider_buy_event_252d_d1}, 'f18_iasp_134_insider_capitulation_signal_63d_d1': {'inputs': ['insider_sell_value', 'insider_sell_count', 'insider_buy_value'], 'func': f18_iasp_134_insider_capitulation_signal_63d_d1}, 'f18_iasp_135_sell_intensity_above_p95_count_252d_d1': {'inputs': ['insider_sell_value'], 'func': f18_iasp_135_sell_intensity_above_p95_count_252d_d1}, 'f18_iasp_136_sell_intensity_zscore_acceleration_21d_d1': {'inputs': ['insider_sell_value'], 'func': f18_iasp_136_sell_intensity_zscore_acceleration_21d_d1}, 'f18_iasp_137_c_suite_sell_count_zscore_252d_d1': {'inputs': ['ceo_sell_value', 'cfo_sell_value'], 'func': f18_iasp_137_c_suite_sell_count_zscore_252d_d1}, 'f18_iasp_138_sell_to_buy_value_ratio_zscore_252d_d1': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f18_iasp_138_sell_to_buy_value_ratio_zscore_252d_d1}, 'f18_iasp_139_sell_burst_intensity_max_63d_d1': {'inputs': ['insider_sell_value'], 'func': f18_iasp_139_sell_burst_intensity_max_63d_d1}, 'f18_iasp_140_high_value_sell_followed_by_zero_buy_count_63d_d1': {'inputs': ['insider_sell_value', 'insider_buy_value'], 'func': f18_iasp_140_high_value_sell_followed_by_zero_buy_count_63d_d1}, 'f18_iasp_141_multi_day_consecutive_net_sell_max_streak_252d_d1': {'inputs': ['insider_net_value'], 'func': f18_iasp_141_multi_day_consecutive_net_sell_max_streak_252d_d1}, 'f18_iasp_142_net_sell_intensity_topdecile_count_252d_d1': {'inputs': ['insider_net_value'], 'func': f18_iasp_142_net_sell_intensity_topdecile_count_252d_d1}, 'f18_iasp_143_sell_concentration_top1_day_share_of_63d_d1': {'inputs': ['insider_sell_value'], 'func': f18_iasp_143_sell_concentration_top1_day_share_of_63d_d1}, 'f18_iasp_144_sell_concentration_top1_day_share_of_252d_d1': {'inputs': ['insider_sell_value'], 'func': f18_iasp_144_sell_concentration_top1_day_share_of_252d_d1}, 'f18_iasp_145_net_sell_topping_score_63d_d1': {'inputs': ['insider_net_value', 'insider_sell_count'], 'func': f18_iasp_145_net_sell_topping_score_63d_d1}, 'f18_iasp_146_net_sell_persistence_streak_max_63d_d1': {'inputs': ['insider_net_value'], 'func': f18_iasp_146_net_sell_persistence_streak_max_63d_d1}, 'f18_iasp_147_insider_signal_inflection_count_63d_d1': {'inputs': ['insider_net_value'], 'func': f18_iasp_147_insider_signal_inflection_count_63d_d1}, 'f18_iasp_148_composite_distress_insider_score_63d_d1': {'inputs': ['insider_net_value', 'insider_sell_value', 'insider_buy_value', 'late_filings_count'], 'func': f18_iasp_148_composite_distress_insider_score_63d_d1}, 'f18_iasp_149_composite_insider_topping_score_252d_d1': {'inputs': ['insider_sell_value', 'insider_sell_count', 'ceo_sell_value', 'cfo_sell_value'], 'func': f18_iasp_149_composite_insider_topping_score_252d_d1}, 'f18_iasp_150_composite_insider_blowoff_score_252d_d1': {'inputs': ['insider_sell_value', 'insider_buy_value', 'insider_holdings_post_pct'], 'func': f18_iasp_150_composite_insider_blowoff_score_252d_d1}}
