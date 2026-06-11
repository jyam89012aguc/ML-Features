"""hypergrowth_deceleration_cliff d1 features 076_150 — 1st-derivative wrappers.

Each function inlines the corresponding base body and appends .diff() so the output is the first bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
import numpy as np
import pandas as pd
QDAYS = 63
YDAYS = 252
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260
MDAYS = 21
WDAYS = 5

def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))

def _safe_log_signed(s):
    return np.sign(s) * np.log1p(s.abs())

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

def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()

def f43_hdcl_076_revenue_growth_trajectory_slope_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_slope(yoy, DDAYS_2Y).diff()

def f43_hdcl_077_revenue_growth_trajectory_slope_20q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return _rolling_slope(yoy, DDAYS_5Y).diff()

def f43_hdcl_078_revenue_growth_trajectory_curvature_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    slope8 = _rolling_slope(yoy, DDAYS_2Y)
    return _rolling_slope(slope8, DDAYS_2Y).diff()

def f43_hdcl_079_revenue_growth_jump_count_negative_8q_d1(revenue: pd.Series) -> pd.Series:
    accel = _safe_log(revenue).diff(QDAYS).diff(QDAYS)
    m = accel.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    sd = accel.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    flag = (accel < m - 2.0 * sd).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_080_revenue_growth_step_change_negative_indicator_d1(revenue: pd.Series) -> pd.Series:
    accel = _safe_log(revenue).diff(QDAYS).diff(QDAYS)
    m = accel.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    sd = accel.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    return (accel < m - 2.0 * sd).astype(float).where(accel.notna() & sd.notna(), np.nan).diff()

def f43_hdcl_081_revenue_growth_zscore_change_4q_d1(revenue: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    return z.diff(YDAYS).diff()

def f43_hdcl_082_revenue_growth_zscore_change_acceleration_4q_d1(revenue: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    return z.diff(YDAYS).diff(YDAYS).diff()

def f43_hdcl_083_revenue_yoy_distribution_skewness_20q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)

    def _sk(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 3).mean() / sd ** 3)
    return yoy.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_sk, raw=True).diff()

def f43_hdcl_084_revenue_yoy_distribution_kurtosis_20q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)

    def _k(w):
        if np.isnan(w).any():
            return np.nan
        sd = w.std()
        if sd == 0:
            return np.nan
        return float(((w - w.mean()) ** 4).mean() / sd ** 4 - 3.0)
    return yoy.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_k, raw=True).diff()

def f43_hdcl_085_revenue_yoy_distribution_minimum_20q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return yoy.rolling(DDAYS_5Y, min_periods=YDAYS).min().diff()

def f43_hdcl_086_revenue_yoy_distribution_p75_minus_p25_20q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    p75 = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    p25 = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    return (p75 - p25).diff()

def f43_hdcl_087_revenue_growth_persistence_above_zero_streak_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy > 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_088_revenue_growth_persistence_below_zero_streak_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = (yoy < 0).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_089_revenue_growth_oscillation_count_8q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    sg = np.sign(qoq.fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)
    return flip.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_090_revenue_growth_directional_consistency_8q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    sg = np.sign(qoq)
    return sg.rolling(DDAYS_2Y, min_periods=YDAYS).mean().abs().diff()

def f43_hdcl_091_revenue_growth_smoothed_ema5q_vs_ema20q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    e5q = _ema(yoy, QDAYS * 5)
    e20q = _ema(yoy, DDAYS_5Y)
    return (_safe_div(e5q, e20q) - 1.0).diff()

def f43_hdcl_092_revenue_growth_ema5q_decel_thrust_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    e = _ema(yoy, QDAYS * 5)
    return (e - e.shift(QDAYS * 5)).diff()

def f43_hdcl_093_revenue_growth_pivot_signal_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    mx = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    sd = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).std()
    return _safe_div(mx - yoy, sd).diff()

def f43_hdcl_094_revenue_growth_inflection_recency_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    slope = _rolling_slope(yoy, QDAYS * 5)
    sg = np.sign(slope.fillna(0))
    flip = (sg.diff().abs() > 0).astype(float)
    return _recency_since_event(flip, DDAYS_5Y).diff()

def f43_hdcl_095_revenue_growth_break_below_mean_recency_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((yoy < m) & (yoy.shift(1) >= m.shift(1))).astype(float)
    return _recency_since_event(flag, DDAYS_5Y).diff()

def f43_hdcl_096_revenue_growth_break_below_5pct_recency_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = ((yoy < 0.05) & (yoy.shift(1) >= 0.05)).astype(float)
    return _recency_since_event(flag, DDAYS_5Y).diff()

def f43_hdcl_097_revenue_growth_decay_half_life_proxy_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    mx = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    mn = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).min()
    return _safe_div(yoy - mn, mx - mn).diff()

def f43_hdcl_098_revenue_growth_trajectory_zscore_combination_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (_rolling_zscore(yoy, DDAYS_5Y) - _rolling_zscore(yoy, DDAYS_2Y)).diff()

def f43_hdcl_099_revenue_growth_3y_slope_vs_5y_slope_diff_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (_rolling_slope(yoy, DDAYS_3Y) - _rolling_slope(yoy, DDAYS_5Y)).diff()

def f43_hdcl_100_revenue_growth_recent_vs_baseline_diff_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    return (yoy.rolling(QDAYS * 2, min_periods=QDAYS).mean() - yoy.rolling(DDAYS_2Y, min_periods=YDAYS).mean()).diff()

def f43_hdcl_101_revenue_growth_vs_ar_growth_gap_8q_d1(revenue: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(accountsreceivable).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_102_revenue_growth_vs_inventory_growth_gap_8q_d1(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(inventory).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_103_revenue_growth_vs_capex_growth_gap_8q_d1(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(capex).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_104_revenue_growth_vs_sgna_growth_gap_8q_d1(revenue: pd.Series, sgna: pd.Series) -> pd.Series:
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(sgna).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_105_revenue_growth_vs_rnd_growth_gap_8q_d1(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(rnd).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_106_revenue_per_sgna_change_yoy_d1(revenue: pd.Series, sgna: pd.Series) -> pd.Series:
    prod = _safe_div(revenue, sgna)
    return _safe_log(prod).diff(YDAYS).diff()

def f43_hdcl_107_working_capital_growth_outpacing_revenue_streak_d1(revenue: pd.Series, workingcapital: pd.Series) -> pd.Series:
    flag = (_safe_log_signed(workingcapital).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_108_inventory_growth_outpacing_revenue_streak_d1(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    flag = (_safe_log(inventory).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_109_ar_growth_outpacing_revenue_streak_d1(revenue: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
    flag = (_safe_log(accountsreceivable).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_110_sgna_growth_outpacing_revenue_streak_d1(revenue: pd.Series, sgna: pd.Series) -> pd.Series:
    flag = (_safe_log(sgna).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_111_capex_growth_outpacing_revenue_streak_d1(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    flag = (_safe_log_signed(capex).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_112_revenue_growth_quality_score_8q_d1(revenue: pd.Series, accountsreceivable: pd.Series, inventory: pd.Series) -> pd.Series:
    ryoy = _safe_log(revenue).diff(YDAYS)
    aryoy = _safe_log(accountsreceivable).diff(YDAYS)
    inyoy = _safe_log(inventory).diff(YDAYS)
    flag = ((ryoy > 0) & (aryoy <= ryoy) & (inyoy <= ryoy)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_113_cash_conversion_with_revenue_growth_change_d1(revenue: pd.Series, fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    cc = _safe_div(fcf, netinc)
    cc_chg = cc.diff(YDAYS)
    ryoy = _safe_log(revenue).diff(YDAYS)
    return (cc_chg * np.sign(ryoy)).diff()

def f43_hdcl_114_ebitda_to_revenue_growth_decay_8q_d1(revenue: pd.Series, ebitda: pd.Series) -> pd.Series:
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(ebitda).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_115_fcf_to_revenue_growth_decay_8q_d1(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log_signed(fcf).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_116_gp_to_revenue_growth_decay_8q_d1(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    diff = _safe_log(revenue).diff(YDAYS) - _safe_log(gp).diff(YDAYS)
    return diff.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_117_incremental_revenue_per_incremental_capex_8q_d1(revenue: pd.Series, capex: pd.Series) -> pd.Series:
    dr = revenue - revenue.shift(DDAYS_2Y)
    dc = capex - capex.shift(DDAYS_2Y)
    return _safe_div(dr, dc).diff()

def f43_hdcl_118_incremental_revenue_per_incremental_rnd_8q_d1(revenue: pd.Series, rnd: pd.Series) -> pd.Series:
    dr = revenue - revenue.shift(DDAYS_2Y)
    dr_rnd = rnd - rnd.shift(DDAYS_2Y)
    return _safe_div(dr, dr_rnd).diff()

def f43_hdcl_119_incremental_margin_decay_8q_d1(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    dg = gp - gp.shift(DDAYS_2Y)
    dr = revenue - revenue.shift(DDAYS_2Y)
    return _safe_div(dg, dr).diff()

def f43_hdcl_120_capital_intensity_change_yoy_d1(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    ci = _safe_div(capex, revenue)
    return ci.diff(YDAYS).diff()

def f43_hdcl_121_operating_leverage_breakdown_indicator_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    flag = ((_safe_log(revenue).diff(YDAYS) > 0.1) & (_safe_log_signed(opinc).diff(YDAYS) < 0)).astype(float)
    return flag.where(revenue.notna() & opinc.notna(), np.nan).diff()

def f43_hdcl_122_negative_operating_leverage_streak_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (_safe_log_signed(opinc).diff(YDAYS) < 0)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff()

def f43_hdcl_123_revenue_growth_with_negative_opinc_count_8q_d1(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (opinc < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_124_revenue_growth_with_negative_fcf_count_8q_d1(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (fcf < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_125_revenue_growth_with_negative_netinc_count_8q_d1(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (netinc < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_126_revenue_yoy_drop_5pct_in_1q_indicator_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return (drop > 0.05).astype(float).where(drop.notna(), np.nan).diff()

def f43_hdcl_127_revenue_yoy_drop_10pct_in_1q_indicator_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return (drop > 0.1).astype(float).where(drop.notna(), np.nan).diff()

def f43_hdcl_128_revenue_yoy_drop_20pct_in_1q_indicator_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return (drop > 0.2).astype(float).where(drop.notna(), np.nan).diff()

def f43_hdcl_129_revenue_yoy_drop_5pct_in_2q_indicator_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS * 2) - yoy
    return (drop > 0.05).astype(float).where(drop.notna(), np.nan).diff()

def f43_hdcl_130_revenue_yoy_drop_10pct_in_2q_indicator_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS * 2) - yoy
    return (drop > 0.1).astype(float).where(drop.notna(), np.nan).diff()

def f43_hdcl_131_revenue_yoy_acceleration_collapse_indicator_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    flag = ((yoy.shift(YDAYS) > 0.3) & (yoy < 0.05)).astype(float)
    return flag.where(yoy.notna() & yoy.shift(YDAYS).notna(), np.nan).diff()

def f43_hdcl_132_max_single_q_yoy_drop_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return drop.rolling(DDAYS_2Y, min_periods=YDAYS).max().diff()

def f43_hdcl_133_max_2q_yoy_drop_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS * 2) - yoy
    return drop.rolling(DDAYS_2Y, min_periods=YDAYS).max().diff()

def f43_hdcl_134_max_4q_yoy_drop_20q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(YDAYS) - yoy
    return drop.rolling(DDAYS_5Y, min_periods=YDAYS).max().diff()

def f43_hdcl_135_cliff_breadth_count_4q_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    r_neg = (_safe_log(revenue).diff(YDAYS) < 0).astype(int)
    o_neg = (_safe_log_signed(opinc).diff(YDAYS) < 0).astype(int)
    f_neg = (_safe_log_signed(fcf).diff(YDAYS) < 0).astype(int)
    n_neg = (_safe_log_signed(netinc).diff(YDAYS) < 0).astype(int)
    total = (r_neg + o_neg + f_neg + n_neg).astype(float)
    flag = (total >= 3).astype(float)
    return flag.rolling(YDAYS, min_periods=QDAYS).sum().diff()

def f43_hdcl_136_revenue_qoq_negative_4q_in_row_indicator_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq < 0).astype(int)
    streak = _streak_above_zero(flag, YDAYS)
    return (streak >= 4 * QDAYS).astype(float).where(streak.notna(), np.nan).diff()

def f43_hdcl_137_revenue_qoq_negative_2q_in_row_indicator_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq < 0).astype(int)
    streak = _streak_above_zero(flag, YDAYS)
    return (streak >= 2 * QDAYS).astype(float).where(streak.notna(), np.nan).diff()

def f43_hdcl_138_revenue_qoq_persistent_negativity_count_8q_d1(revenue: pd.Series) -> pd.Series:
    qoq = _safe_log(revenue).diff(QDAYS)
    flag = (qoq < 0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_139_revenue_yoy_below_peak_log_distance_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    peak = yoy.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    return (_safe_log_signed(yoy) - _safe_log_signed(peak)).diff()

def f43_hdcl_140_revenue_yoy_below_2y_max_log_distance_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    peak = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).max()
    return (_safe_log_signed(yoy) - _safe_log_signed(peak)).diff()

def f43_hdcl_141_growth_cliff_composite_indicator_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    flag = ((drop > 0.1) & (_safe_log_signed(opinc).diff(YDAYS) < 0) & (_safe_log_signed(fcf).diff(YDAYS) < 0)).astype(float)
    return flag.where(drop.notna(), np.nan).diff()

def f43_hdcl_142_growth_cliff_intensity_score_8q_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    s = (drop > 0.1).astype(float) + (_safe_log_signed(opinc).diff(YDAYS) < 0).astype(float) + (_safe_log_signed(fcf).diff(YDAYS) < 0).astype(float)
    return s.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_143_growth_cliff_recency_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    flag = (drop > 0.1).astype(float)
    return _recency_since_event(flag, DDAYS_5Y).diff()

def f43_hdcl_144_growth_cliff_persistence_8q_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    flag = (drop > 0.05).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff()

def f43_hdcl_145_growth_cliff_zscore_5y_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    drop = yoy.shift(QDAYS) - yoy
    return _rolling_zscore(drop, DDAYS_5Y).diff()

def f43_hdcl_146_hypergrowth_to_decel_transition_score_d1(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    s = (yoy.shift(YDAYS) > 0.3).astype(float) * (yoy < 0.1).astype(float)
    return s.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_147_hypergrowth_peak_distance_with_compound_decel_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    yoy_r = _safe_log(revenue).diff(YDAYS)
    distance = yoy_r.rolling(DDAYS_5Y, min_periods=YDAYS).max() - yoy_r
    cond = ((_safe_log_signed(opinc).diff(YDAYS) < 0) & (_safe_log_signed(fcf).diff(YDAYS) < 0)).astype(float)
    return (distance * cond).diff()

def f43_hdcl_148_composite_f43_hdcl_blowoff_score_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series) -> pd.Series:
    r_pct = _rolling_rank_pct(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    o_pct = _rolling_rank_pct(_safe_log_signed(opinc).diff(YDAYS), DDAYS_5Y)
    f_pct = _rolling_rank_pct(_safe_log_signed(fcf).diff(YDAYS), DDAYS_5Y)
    s = r_pct * (1.0 - o_pct) * (1.0 - f_pct)
    return s.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_149_composite_f43_hdcl_distress_score_d1(revenue: pd.Series, opinc: pd.Series, fcf: pd.Series, netinc: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    decel = yoy < yoy.shift(YDAYS)
    distress = (opinc < 0) | (fcf < 0) | (netinc < 0)
    flag = (decel & distress).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff()

def f43_hdcl_150_composite_f43_hdcl_topping_score_d1(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, fcf: pd.Series, netinc: pd.Series, ebitda: pd.Series) -> pd.Series:
    series_list = [_safe_log(revenue).diff(YDAYS), _safe_log(gp).diff(YDAYS), _safe_log_signed(opinc).diff(YDAYS), _safe_log_signed(fcf).diff(YDAYS), _safe_log_signed(netinc).diff(YDAYS), _safe_log_signed(ebitda).diff(YDAYS)]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        r = _rolling_rank_pct(s, DDAYS_5Y)
        total = total + (1.0 - r)
        valid = valid & r.notna()
    avg = (total / len(series_list)).where(valid, np.nan)
    return avg.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff()
HYPERGROWTH_DECELERATION_CLIFF_D1_REGISTRY_076_150 = {'f43_hdcl_076_revenue_growth_trajectory_slope_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_076_revenue_growth_trajectory_slope_8q_d1}, 'f43_hdcl_077_revenue_growth_trajectory_slope_20q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_077_revenue_growth_trajectory_slope_20q_d1}, 'f43_hdcl_078_revenue_growth_trajectory_curvature_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_078_revenue_growth_trajectory_curvature_8q_d1}, 'f43_hdcl_079_revenue_growth_jump_count_negative_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_079_revenue_growth_jump_count_negative_8q_d1}, 'f43_hdcl_080_revenue_growth_step_change_negative_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_080_revenue_growth_step_change_negative_indicator_d1}, 'f43_hdcl_081_revenue_growth_zscore_change_4q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_081_revenue_growth_zscore_change_4q_d1}, 'f43_hdcl_082_revenue_growth_zscore_change_acceleration_4q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_082_revenue_growth_zscore_change_acceleration_4q_d1}, 'f43_hdcl_083_revenue_yoy_distribution_skewness_20q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_083_revenue_yoy_distribution_skewness_20q_d1}, 'f43_hdcl_084_revenue_yoy_distribution_kurtosis_20q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_084_revenue_yoy_distribution_kurtosis_20q_d1}, 'f43_hdcl_085_revenue_yoy_distribution_minimum_20q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_085_revenue_yoy_distribution_minimum_20q_d1}, 'f43_hdcl_086_revenue_yoy_distribution_p75_minus_p25_20q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_086_revenue_yoy_distribution_p75_minus_p25_20q_d1}, 'f43_hdcl_087_revenue_growth_persistence_above_zero_streak_d1': {'inputs': ['revenue'], 'func': f43_hdcl_087_revenue_growth_persistence_above_zero_streak_d1}, 'f43_hdcl_088_revenue_growth_persistence_below_zero_streak_d1': {'inputs': ['revenue'], 'func': f43_hdcl_088_revenue_growth_persistence_below_zero_streak_d1}, 'f43_hdcl_089_revenue_growth_oscillation_count_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_089_revenue_growth_oscillation_count_8q_d1}, 'f43_hdcl_090_revenue_growth_directional_consistency_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_090_revenue_growth_directional_consistency_8q_d1}, 'f43_hdcl_091_revenue_growth_smoothed_ema5q_vs_ema20q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_091_revenue_growth_smoothed_ema5q_vs_ema20q_d1}, 'f43_hdcl_092_revenue_growth_ema5q_decel_thrust_d1': {'inputs': ['revenue'], 'func': f43_hdcl_092_revenue_growth_ema5q_decel_thrust_d1}, 'f43_hdcl_093_revenue_growth_pivot_signal_d1': {'inputs': ['revenue'], 'func': f43_hdcl_093_revenue_growth_pivot_signal_d1}, 'f43_hdcl_094_revenue_growth_inflection_recency_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_094_revenue_growth_inflection_recency_5y_d1}, 'f43_hdcl_095_revenue_growth_break_below_mean_recency_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_095_revenue_growth_break_below_mean_recency_5y_d1}, 'f43_hdcl_096_revenue_growth_break_below_5pct_recency_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_096_revenue_growth_break_below_5pct_recency_5y_d1}, 'f43_hdcl_097_revenue_growth_decay_half_life_proxy_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_097_revenue_growth_decay_half_life_proxy_8q_d1}, 'f43_hdcl_098_revenue_growth_trajectory_zscore_combination_d1': {'inputs': ['revenue'], 'func': f43_hdcl_098_revenue_growth_trajectory_zscore_combination_d1}, 'f43_hdcl_099_revenue_growth_3y_slope_vs_5y_slope_diff_d1': {'inputs': ['revenue'], 'func': f43_hdcl_099_revenue_growth_3y_slope_vs_5y_slope_diff_d1}, 'f43_hdcl_100_revenue_growth_recent_vs_baseline_diff_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_100_revenue_growth_recent_vs_baseline_diff_8q_d1}, 'f43_hdcl_101_revenue_growth_vs_ar_growth_gap_8q_d1': {'inputs': ['revenue', 'accountsreceivable'], 'func': f43_hdcl_101_revenue_growth_vs_ar_growth_gap_8q_d1}, 'f43_hdcl_102_revenue_growth_vs_inventory_growth_gap_8q_d1': {'inputs': ['revenue', 'inventory'], 'func': f43_hdcl_102_revenue_growth_vs_inventory_growth_gap_8q_d1}, 'f43_hdcl_103_revenue_growth_vs_capex_growth_gap_8q_d1': {'inputs': ['revenue', 'capex'], 'func': f43_hdcl_103_revenue_growth_vs_capex_growth_gap_8q_d1}, 'f43_hdcl_104_revenue_growth_vs_sgna_growth_gap_8q_d1': {'inputs': ['revenue', 'sgna'], 'func': f43_hdcl_104_revenue_growth_vs_sgna_growth_gap_8q_d1}, 'f43_hdcl_105_revenue_growth_vs_rnd_growth_gap_8q_d1': {'inputs': ['revenue', 'rnd'], 'func': f43_hdcl_105_revenue_growth_vs_rnd_growth_gap_8q_d1}, 'f43_hdcl_106_revenue_per_sgna_change_yoy_d1': {'inputs': ['revenue', 'sgna'], 'func': f43_hdcl_106_revenue_per_sgna_change_yoy_d1}, 'f43_hdcl_107_working_capital_growth_outpacing_revenue_streak_d1': {'inputs': ['revenue', 'workingcapital'], 'func': f43_hdcl_107_working_capital_growth_outpacing_revenue_streak_d1}, 'f43_hdcl_108_inventory_growth_outpacing_revenue_streak_d1': {'inputs': ['revenue', 'inventory'], 'func': f43_hdcl_108_inventory_growth_outpacing_revenue_streak_d1}, 'f43_hdcl_109_ar_growth_outpacing_revenue_streak_d1': {'inputs': ['revenue', 'accountsreceivable'], 'func': f43_hdcl_109_ar_growth_outpacing_revenue_streak_d1}, 'f43_hdcl_110_sgna_growth_outpacing_revenue_streak_d1': {'inputs': ['revenue', 'sgna'], 'func': f43_hdcl_110_sgna_growth_outpacing_revenue_streak_d1}, 'f43_hdcl_111_capex_growth_outpacing_revenue_streak_d1': {'inputs': ['revenue', 'capex'], 'func': f43_hdcl_111_capex_growth_outpacing_revenue_streak_d1}, 'f43_hdcl_112_revenue_growth_quality_score_8q_d1': {'inputs': ['revenue', 'accountsreceivable', 'inventory'], 'func': f43_hdcl_112_revenue_growth_quality_score_8q_d1}, 'f43_hdcl_113_cash_conversion_with_revenue_growth_change_d1': {'inputs': ['revenue', 'fcf', 'netinc'], 'func': f43_hdcl_113_cash_conversion_with_revenue_growth_change_d1}, 'f43_hdcl_114_ebitda_to_revenue_growth_decay_8q_d1': {'inputs': ['revenue', 'ebitda'], 'func': f43_hdcl_114_ebitda_to_revenue_growth_decay_8q_d1}, 'f43_hdcl_115_fcf_to_revenue_growth_decay_8q_d1': {'inputs': ['revenue', 'fcf'], 'func': f43_hdcl_115_fcf_to_revenue_growth_decay_8q_d1}, 'f43_hdcl_116_gp_to_revenue_growth_decay_8q_d1': {'inputs': ['revenue', 'gp'], 'func': f43_hdcl_116_gp_to_revenue_growth_decay_8q_d1}, 'f43_hdcl_117_incremental_revenue_per_incremental_capex_8q_d1': {'inputs': ['revenue', 'capex'], 'func': f43_hdcl_117_incremental_revenue_per_incremental_capex_8q_d1}, 'f43_hdcl_118_incremental_revenue_per_incremental_rnd_8q_d1': {'inputs': ['revenue', 'rnd'], 'func': f43_hdcl_118_incremental_revenue_per_incremental_rnd_8q_d1}, 'f43_hdcl_119_incremental_margin_decay_8q_d1': {'inputs': ['revenue', 'gp'], 'func': f43_hdcl_119_incremental_margin_decay_8q_d1}, 'f43_hdcl_120_capital_intensity_change_yoy_d1': {'inputs': ['capex', 'revenue'], 'func': f43_hdcl_120_capital_intensity_change_yoy_d1}, 'f43_hdcl_121_operating_leverage_breakdown_indicator_d1': {'inputs': ['revenue', 'opinc'], 'func': f43_hdcl_121_operating_leverage_breakdown_indicator_d1}, 'f43_hdcl_122_negative_operating_leverage_streak_d1': {'inputs': ['revenue', 'opinc'], 'func': f43_hdcl_122_negative_operating_leverage_streak_d1}, 'f43_hdcl_123_revenue_growth_with_negative_opinc_count_8q_d1': {'inputs': ['revenue', 'opinc'], 'func': f43_hdcl_123_revenue_growth_with_negative_opinc_count_8q_d1}, 'f43_hdcl_124_revenue_growth_with_negative_fcf_count_8q_d1': {'inputs': ['revenue', 'fcf'], 'func': f43_hdcl_124_revenue_growth_with_negative_fcf_count_8q_d1}, 'f43_hdcl_125_revenue_growth_with_negative_netinc_count_8q_d1': {'inputs': ['revenue', 'netinc'], 'func': f43_hdcl_125_revenue_growth_with_negative_netinc_count_8q_d1}, 'f43_hdcl_126_revenue_yoy_drop_5pct_in_1q_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_126_revenue_yoy_drop_5pct_in_1q_indicator_d1}, 'f43_hdcl_127_revenue_yoy_drop_10pct_in_1q_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_127_revenue_yoy_drop_10pct_in_1q_indicator_d1}, 'f43_hdcl_128_revenue_yoy_drop_20pct_in_1q_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_128_revenue_yoy_drop_20pct_in_1q_indicator_d1}, 'f43_hdcl_129_revenue_yoy_drop_5pct_in_2q_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_129_revenue_yoy_drop_5pct_in_2q_indicator_d1}, 'f43_hdcl_130_revenue_yoy_drop_10pct_in_2q_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_130_revenue_yoy_drop_10pct_in_2q_indicator_d1}, 'f43_hdcl_131_revenue_yoy_acceleration_collapse_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_131_revenue_yoy_acceleration_collapse_indicator_d1}, 'f43_hdcl_132_max_single_q_yoy_drop_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_132_max_single_q_yoy_drop_8q_d1}, 'f43_hdcl_133_max_2q_yoy_drop_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_133_max_2q_yoy_drop_8q_d1}, 'f43_hdcl_134_max_4q_yoy_drop_20q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_134_max_4q_yoy_drop_20q_d1}, 'f43_hdcl_135_cliff_breadth_count_4q_d1': {'inputs': ['revenue', 'opinc', 'fcf', 'netinc'], 'func': f43_hdcl_135_cliff_breadth_count_4q_d1}, 'f43_hdcl_136_revenue_qoq_negative_4q_in_row_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_136_revenue_qoq_negative_4q_in_row_indicator_d1}, 'f43_hdcl_137_revenue_qoq_negative_2q_in_row_indicator_d1': {'inputs': ['revenue'], 'func': f43_hdcl_137_revenue_qoq_negative_2q_in_row_indicator_d1}, 'f43_hdcl_138_revenue_qoq_persistent_negativity_count_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_138_revenue_qoq_persistent_negativity_count_8q_d1}, 'f43_hdcl_139_revenue_yoy_below_peak_log_distance_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_139_revenue_yoy_below_peak_log_distance_5y_d1}, 'f43_hdcl_140_revenue_yoy_below_2y_max_log_distance_d1': {'inputs': ['revenue'], 'func': f43_hdcl_140_revenue_yoy_below_2y_max_log_distance_d1}, 'f43_hdcl_141_growth_cliff_composite_indicator_d1': {'inputs': ['revenue', 'opinc', 'fcf'], 'func': f43_hdcl_141_growth_cliff_composite_indicator_d1}, 'f43_hdcl_142_growth_cliff_intensity_score_8q_d1': {'inputs': ['revenue', 'opinc', 'fcf'], 'func': f43_hdcl_142_growth_cliff_intensity_score_8q_d1}, 'f43_hdcl_143_growth_cliff_recency_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_143_growth_cliff_recency_5y_d1}, 'f43_hdcl_144_growth_cliff_persistence_8q_d1': {'inputs': ['revenue'], 'func': f43_hdcl_144_growth_cliff_persistence_8q_d1}, 'f43_hdcl_145_growth_cliff_zscore_5y_d1': {'inputs': ['revenue'], 'func': f43_hdcl_145_growth_cliff_zscore_5y_d1}, 'f43_hdcl_146_hypergrowth_to_decel_transition_score_d1': {'inputs': ['revenue'], 'func': f43_hdcl_146_hypergrowth_to_decel_transition_score_d1}, 'f43_hdcl_147_hypergrowth_peak_distance_with_compound_decel_d1': {'inputs': ['revenue', 'opinc', 'fcf'], 'func': f43_hdcl_147_hypergrowth_peak_distance_with_compound_decel_d1}, 'f43_hdcl_148_composite_f43_hdcl_blowoff_score_d1': {'inputs': ['revenue', 'opinc', 'fcf'], 'func': f43_hdcl_148_composite_f43_hdcl_blowoff_score_d1}, 'f43_hdcl_149_composite_f43_hdcl_distress_score_d1': {'inputs': ['revenue', 'opinc', 'fcf', 'netinc'], 'func': f43_hdcl_149_composite_f43_hdcl_distress_score_d1}, 'f43_hdcl_150_composite_f43_hdcl_topping_score_d1': {'inputs': ['revenue', 'gp', 'opinc', 'fcf', 'netinc', 'ebitda'], 'func': f43_hdcl_150_composite_f43_hdcl_topping_score_d1}}
