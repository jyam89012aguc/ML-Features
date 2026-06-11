"""Auto-generated D3 wrappers from revenue_deceleration_jerk__base__076_150.py.

Each function inlines the base body and appends .diff() chained 3 time(s)."""
import numpy as np
import pandas as pd
Q = 1
Y = 4
Y2 = 8
Y3 = 12
Y4 = 16

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

def _structural_break_score(s, n):
    return _rolling_slope(s, n) - _rolling_slope(s.shift(n), n)

def f34_rdjk_076_compound_revenue_jerk_ebit_jerk_same_sign_4q_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    je = ebit.diff().diff().diff()
    flag = ((np.sign(jr) == np.sign(je)) & (jr != 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_077_compound_revenue_jerk_margin_jerk_4q_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    margin = _safe_div(netinc, revenue)
    jm = margin.diff().diff().diff()
    flag = ((jr < 0) & (jm < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_078_compound_revenue_jerk_cash_jerk_4q_d3(revenue: pd.Series, cashneq: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    jc = cashneq.diff().diff().diff()
    flag = ((jr < 0) & (jc < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_079_compound_revenue_jerk_dilution_jerk_4q_d3(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    js = shareswa.diff().diff().diff()
    flag = ((jr < 0) & (js > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_080_compound_revenue_jerk_receivables_jerk_4q_d3(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    jrec = receivables.diff().diff().diff()
    flag = ((jr < 0) & (jrec > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_081_compound_revenue_jerk_inventory_jerk_4q_d3(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    ji = inventory.diff().diff().diff()
    flag = ((jr < 0) & (ji > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_082_jerk_cooccurrence_count_3metrics_4q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    je = ebit.diff().diff().diff()
    jn = netinc.diff().diff().diff()
    flag = ((jr < 0) & (je < 0) & (jn < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_083_jerk_magnitude_divergence_revenue_ebit_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    jr_z = _rolling_zscore(revenue.diff().diff().diff(), Y4).abs()
    je_z = _rolling_zscore(ebit.diff().diff().diff(), Y4).abs()
    return (jr_z - je_z).diff().diff().diff()

def f34_rdjk_084_revenue_jerk_vs_margin_jerk_z_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    margin = _safe_div(netinc, revenue)
    return (_rolling_zscore(revenue.diff().diff().diff(), Y4) - _rolling_zscore(margin.diff().diff().diff(), Y4)).diff().diff().diff()

def f34_rdjk_085_revenue_jerk_vs_cash_flow_jerk_z_d3(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    return (_rolling_zscore(revenue.diff().diff().diff(), Y4) - _rolling_zscore(fcf.diff().diff().diff(), Y4)).diff().diff().diff()

def f34_rdjk_086_jerk_gm_compression_count_4q_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    gm = _safe_div(ebit, revenue)
    flag = ((jr < 0) & (gm.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_087_compound_jerk_index_4q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series, cashneq: pd.Series) -> pd.Series:
    jr_z = _rolling_zscore(revenue.diff().diff().diff(), Y4).abs()
    stress = (ebit.diff() < 0).astype(float) + (netinc.diff() < 0).astype(float) + (cashneq.diff() < 0).astype(float)
    return (jr_z * stress).rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_088_compound_jerk_pos_declining_traj_4q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    flag = ((j > 0) & (revenue.diff(Y) < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_089_compound_jerk_pos_revenue_z_neg_4q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    z = _rolling_zscore(revenue, Y4)
    flag = ((j > 0) & (z < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_090_compound_jerk_with_ebit_decline_4q_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    flag = ((j < 0) & (ebit.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_091_revenue_jerk_sequential_decline_4q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    down = revenue.diff() < 0
    two_consec = (down & down.shift(1)).astype(float)
    flag = (j < 0).astype(float) * two_consec
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_092_revenue_jerk_with_yoy_negative_4q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    yoy = revenue.pct_change(Y)
    flag = ((j < 0) & (yoy < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_093_revenue_jerk_with_2q_qoq_decline_4q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    qoq = revenue.pct_change()
    down2 = ((qoq < 0) & (qoq.shift(1) < 0)).astype(float)
    flag = (j < 0).astype(float) * down2
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_094_revenue_jerk_receivables_grow_faster_4q_d3(revenue: pd.Series, receivables: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    flag = ((j < 0) & (receivables.pct_change() > revenue.pct_change())).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_095_revenue_jerk_inventory_grow_faster_4q_d3(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    flag = ((j < 0) & (inventory.pct_change() > revenue.pct_change())).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_096_revenue_jerk_with_debt_up_4q_d3(revenue: pd.Series, debt: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    flag = ((j < 0) & (debt.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_097_revenue_jerk_with_shares_up_4q_d3(revenue: pd.Series, shareswa: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    flag = ((j < 0) & (shareswa.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_098_revenue_jerk_multimetric_stress_4q_d3(revenue: pd.Series, ebit: pd.Series, cashneq: pd.Series, debt: pd.Series, shareswa: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    score = (j < 0).astype(float) + (ebit.diff() < 0).astype(float) + (cashneq.diff() < 0).astype(float) + (debt.diff() > 0).astype(float) + (shareswa.diff() > 0).astype(float)
    return score.rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_099_revenue_jerk_highest_decile_16q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    p = j.rolling(Y4, min_periods=6).quantile(0.9)
    return (j >= p).astype(float).diff().diff().diff()

def f34_rdjk_100_revenue_jerk_composite_stress_count_4q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series, cashneq: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    je = ebit.diff().diff().diff()
    jn = netinc.diff().diff().diff()
    jc = cashneq.diff().diff().diff()
    flag = ((jr < 0) & ((je < 0) | (jn < 0) | (jc < 0))).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_101_revenue_accel_slope_cliff_8q_d3(revenue: pd.Series) -> pd.Series:
    sl = _rolling_slope(revenue.diff().diff(), Y)
    chg = sl.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff().diff()

def f34_rdjk_102_log_revenue_accel_slope_cliff_8q_d3(revenue: pd.Series) -> pd.Series:
    sl = _rolling_slope(_safe_log(revenue).diff().diff(), Y)
    chg = sl.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff().diff()

def f34_rdjk_103_compound_revenue_decel_accelerating_decel_4q_d3(revenue: pd.Series) -> pd.Series:
    chg = revenue.diff()
    d2 = chg.diff()
    d3 = d2.diff()
    flag = ((chg < 0) & (d2 < 0) & (d3 < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_104_compound_revenue_accel_sign_chg_margin_sign_chg_4q_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    d2 = revenue.diff().diff()
    margin_chg = _safe_div(netinc, revenue).diff()
    f1 = np.sign(d2) != np.sign(d2.shift(1))
    f2 = np.sign(margin_chg) != np.sign(margin_chg.shift(1))
    flag = (f1 & f2).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_105_compound_revenue_accel_sign_chg_ebit_decline_4q_d3(revenue: pd.Series, ebit: pd.Series) -> pd.Series:
    d2 = revenue.diff().diff()
    f1 = np.sign(d2) != np.sign(d2.shift(1))
    f2 = ebit.diff() < 0
    flag = (f1 & f2).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_106_revenue_accel_persistence_index_8q_d3(revenue: pd.Series) -> pd.Series:
    d2 = revenue.diff().diff()
    flag = (d2 < 0).astype(float)
    return flag.rolling(Y2, min_periods=3).mean().diff().diff().diff()

def f34_rdjk_107_revenue_accel_persistence_index_16q_d3(revenue: pd.Series) -> pd.Series:
    d2 = revenue.diff().diff()
    flag = (d2 < 0).astype(float)
    return flag.rolling(Y4, min_periods=6).mean().diff().diff().diff()

def f34_rdjk_108_compound_persistence_jerk_4q_d3(revenue: pd.Series) -> pd.Series:
    d2 = revenue.diff().diff()
    persist = (d2 < 0).astype(float).rolling(Y2, min_periods=3).mean()
    j = d2.diff()
    p25 = j.rolling(Y4, min_periods=6).quantile(0.25)
    return (persist * (j <= p25).astype(float)).diff().diff().diff()

def f34_rdjk_109_revenue_jerk_lowest_decile_16q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    p = j.rolling(Y4, min_periods=6).quantile(0.1)
    return (j <= p).astype(float).diff().diff().diff()

def f34_rdjk_110_revenue_accel_quartile_transition_count_16q_d3(revenue: pd.Series) -> pd.Series:
    d2 = revenue.diff().diff()
    q1 = d2.rolling(Y4, min_periods=6).quantile(0.25)
    q3 = d2.rolling(Y4, min_periods=6).quantile(0.75)
    cur_q = pd.cut(d2.fillna(0), bins=[-np.inf, -10000000000.0, -1000000000.0, 1000000000.0, 10000000000.0, np.inf], labels=False)
    f1 = (np.sign(d2 - q1) != np.sign((d2 - q1).shift(1))).astype(float)
    f2 = (np.sign(d2 - q3) != np.sign((d2 - q3).shift(1))).astype(float)
    return (f1 + f2).rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f34_rdjk_111_revenue_accel_hampel_outliers_count_16q_d3(revenue: pd.Series) -> pd.Series:
    d2 = revenue.diff().diff()
    med = d2.rolling(Y4, min_periods=6).median()
    mad = (d2 - med).abs().rolling(Y4, min_periods=6).median()
    flag = ((d2 - med).abs() > 3.0 * mad).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f34_rdjk_112_revenue_jerk_hampel_outliers_count_16q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    med = j.rolling(Y4, min_periods=6).median()
    mad = (j - med).abs().rolling(Y4, min_periods=6).median()
    flag = ((j - med).abs() > 3.0 * mad).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f34_rdjk_113_revenue_jerk_to_chg_ratio_d3(revenue: pd.Series) -> pd.Series:
    return _safe_div(revenue.diff().diff().diff(), revenue.diff().abs()).diff().diff().diff()

def f34_rdjk_114_revenue_accel_to_chg_ratio_d3(revenue: pd.Series) -> pd.Series:
    return _safe_div(revenue.diff().diff(), revenue.diff().abs()).diff().diff().diff()

def f34_rdjk_115_jerk_dormancy_then_2sigma_event_count_16q_d3(revenue: pd.Series) -> pd.Series:
    jerk = revenue.diff().diff().diff()
    jerk_z = _rolling_zscore(jerk, 16)
    dormancy = (jerk.shift(1).rolling(4, min_periods=3).std() < 0.5 * jerk.rolling(16, min_periods=4).std())
    event = (jerk_z.abs() > 2) & dormancy
    return event.astype(float).rolling(16, min_periods=4).sum().diff().diff().diff()

def f34_rdjk_116_revenue_jerk_to_noise_ratio_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff().abs()
    sd = revenue.diff().rolling(Y4, min_periods=6).std()
    return (j / sd.replace(0, np.nan)).diff().diff().diff()

def f34_rdjk_117_revenue_jerk_peak_trough_ratio_8q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    return _safe_div(j.rolling(Y2, min_periods=3).max() - j.rolling(Y2, min_periods=3).min(), j.rolling(Y4, min_periods=6).std()).diff().diff().diff()

def f34_rdjk_118_revenue_jerk_vs_self_baseline_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    return (j - j.rolling(Y4, min_periods=6).mean()).diff().diff().diff()

def f34_rdjk_119_revenue_jerk_regime_score_8q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    z = _rolling_zscore(j, Y4)
    return (np.sign(j) * z.abs()).rolling(Y2, min_periods=3).mean().diff().diff().diff()

def f34_rdjk_120_revenue_jerk_z_above_2sigma_count_16q_d3(revenue: pd.Series) -> pd.Series:
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f34_rdjk_121_revenue_jerk_z_below_minus2sigma_count_16q_d3(revenue: pd.Series) -> pd.Series:
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4)
    flag = (z < -2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f34_rdjk_122_revenue_jerk_z_abs_exceedance_count_16q_d3(revenue: pd.Series) -> pd.Series:
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4).abs()
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f34_rdjk_123_jerk_lead_lag_with_yoy_accel_lag1_8q_d3(revenue: pd.Series) -> pd.Series:
    yoy = _safe_div(revenue.diff(4), revenue.shift(4).abs())
    accel = yoy.diff().diff()
    jerk = yoy.diff().diff().diff()
    return (jerk * accel.shift(1)).rolling(8, min_periods=4).mean().diff().diff().diff()

def f34_rdjk_124_jerk_conditional_on_low_yoy_level_q25_16q_d3(revenue: pd.Series) -> pd.Series:
    yoy = _safe_div(revenue.diff(4), revenue.shift(4).abs())
    jerk = yoy.diff().diff().diff()
    q25 = yoy.rolling(16, min_periods=4).quantile(0.25)
    cond = yoy < q25
    return jerk.where(cond, np.nan).rolling(16, min_periods=4).mean().diff().diff().diff()

def f34_rdjk_125_jerk_neg_streak_with_calm_baseline_8q_d3(revenue: pd.Series) -> pd.Series:
    jerk = revenue.diff().diff().diff()
    jerk_z = _rolling_zscore(jerk, 8)
    calm = (jerk_z.shift(1).abs() < 1).astype(float).rolling(4, min_periods=3).mean()
    qualifying = (jerk_z < -1) & (calm >= 0.75)
    qual_int = qualifying.astype(int)

    def _longest_run(w):
        if np.all(np.isnan(w)):
            return np.nan
        w = np.nan_to_num(w, nan=0).astype(int)
        best = cur = 0
        for v in w:
            cur = cur + 1 if v else 0
            best = max(best, cur)
        return float(best)
    return qual_int.rolling(8, min_periods=3).apply(_longest_run, raw=True).diff().diff().diff()

def f34_rdjk_126_composite_jerk_accel_signflip_stress_4q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    z_j = _rolling_zscore(j, Y4).abs()
    d2 = revenue.diff().diff()
    flip = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    return (z_j + flip).rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_127_composite_jerk_accel_signflip_count_8q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    d2 = revenue.diff().diff()
    f1 = (np.sign(j) != np.sign(j.shift(1))).astype(float)
    f2 = (np.sign(d2) != np.sign(d2.shift(1))).astype(float)
    return (f1 + f2).rolling(Y2, min_periods=3).sum().diff().diff().diff()

def f34_rdjk_128_weighted_composite_jerk_z_4q_d3(revenue: pd.Series, netinc: pd.Series, ebit: pd.Series) -> pd.Series:
    margin = _safe_div(netinc, revenue)
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4) + _rolling_zscore(margin.diff().diff().diff(), Y4) + _rolling_zscore(ebit.diff().diff().diff(), Y4)
    return z.rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_129_composite_jerk_revenue_deterioration_4q_d3(revenue: pd.Series) -> pd.Series:
    z_j = _rolling_zscore(revenue.diff().diff().diff(), Y4).abs()
    deter = (revenue.diff() < 0).astype(float)
    return (z_j + deter).rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_130_revenue_chaos_index_8q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    return _safe_div(j.rolling(Y2, min_periods=3).std(), j.abs().rolling(Y2, min_periods=3).mean()).diff().diff().diff()

def f34_rdjk_131_revenue_jerk_variance_ratio_8q_vs_16q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    return _safe_div(j.rolling(Y2, min_periods=3).var(), j.rolling(Y4, min_periods=6).var()).diff().diff().diff()

def f34_rdjk_132_revenue_jerk_lyapunov_proxy_8q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff().abs()
    return _safe_log(_safe_div(j, j.shift(1))).rolling(Y2, min_periods=3).mean().diff().diff().diff()

def f34_rdjk_133_revenue_jerk_regime_persistence_4q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    m = j.rolling(Y, min_periods=2).mean()
    flag = (np.sign(j) == np.sign(m)).astype(float)
    return flag.rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_134_compound_terminal_jerk_warning_4q_d3(revenue: pd.Series, ebit: pd.Series, cashneq: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    je = ebit.diff().diff().diff()
    flag = ((jr < 0) & (je < 0) & (cashneq.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_135_revenue_accel_cliff_edge_probability_8q_d3(revenue: pd.Series) -> pd.Series:
    z = _rolling_zscore(revenue.diff().diff(), Y4).abs()
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y2, min_periods=3).mean().diff().diff().diff()

def f34_rdjk_136_revenue_jerk_accel_covariance_8q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    d2 = revenue.diff().diff()
    return j.rolling(Y2, min_periods=3).cov(d2).diff().diff().diff()

def f34_rdjk_137_revenue_jerk_margin_jerk_covariance_8q_d3(revenue: pd.Series, netinc: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    margin = _safe_div(netinc, revenue)
    jm = margin.diff().diff().diff()
    return jr.rolling(Y2, min_periods=3).cov(jm).diff().diff().diff()

def f34_rdjk_138_composite_jerk_dispersion_across_metrics_4q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(revenue.diff().diff().diff(), Y4).rolling(Y, min_periods=2).mean()
    z2 = _rolling_zscore(ebit.diff().diff().diff(), Y4).rolling(Y, min_periods=2).mean()
    z3 = _rolling_zscore(netinc.diff().diff().diff(), Y4).rolling(Y, min_periods=2).mean()
    return pd.concat([z1, z2, z3], axis=1).std(axis=1).diff().diff().diff()

def f34_rdjk_139_revenue_jerk_weighted_by_magnitude_4q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    z = _rolling_zscore(j, Y4)
    return (np.sign(j) * z ** 2).rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_140_jerk_onset_breadth_across_horizons_4_8_12_16_d3(revenue: pd.Series) -> pd.Series:
    jerk = revenue.diff().diff().diff()
    return (
        (_rolling_zscore(jerk, 4).abs() > 2.5).astype(float).fillna(0)
        + (_rolling_zscore(jerk, 8).abs() > 2.5).astype(float).fillna(0)
        + (_rolling_zscore(jerk, 12).abs() > 2.5).astype(float).fillna(0)
        + (_rolling_zscore(jerk, 16).abs() > 2.5).astype(float).fillna(0)
    ).diff().diff().diff()

def f34_rdjk_141_log_jerk_onset_after_2_consec_low_var_q_d3(revenue: pd.Series) -> pd.Series:
    log_rev = _safe_log(revenue)
    log_jerk = log_rev.diff().diff().diff()
    jerk_z = _rolling_zscore(log_jerk, 8)
    recent_var = log_jerk.shift(1).rolling(2, min_periods=2).std()
    long_var = log_jerk.rolling(8, min_periods=4).std()
    fire = (jerk_z.abs() > 2.5) & (recent_var < 0.5 * long_var)
    return fire.astype(float).where(jerk_z.notna(), np.nan).diff().diff().diff()

def f34_rdjk_142_revenue_jerk_vs_self_baseline_8q_d3(revenue: pd.Series) -> pd.Series:
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4)
    return (z - z.rolling(Y2, min_periods=3).mean()).diff().diff().diff()

def f34_rdjk_143_revenue_jerk_consensus_index_4q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    je = ebit.diff().diff().diff()
    jn = netinc.diff().diff().diff()
    same = ((np.sign(jr) == np.sign(je)) & (np.sign(je) == np.sign(jn))).astype(float)
    return same.rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_144_revenue_jerk_anomaly_score_4q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4) ** 2 + _rolling_zscore(ebit.diff().diff().diff(), Y4) ** 2 + _rolling_zscore(netinc.diff().diff().diff(), Y4) ** 2
    return z.rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_145_composite_jerk_regime_change_count_16q_d3(revenue: pd.Series) -> pd.Series:
    j = revenue.diff().diff().diff()
    m4 = j.rolling(Y, min_periods=2).mean()
    flip = (np.sign(m4) != np.sign(m4.shift(1))).astype(float)
    return flip.rolling(Y4, min_periods=6).sum().diff().diff().diff()

def f34_rdjk_146_composite_jerk_escalation_4q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4).abs() + _rolling_zscore(ebit.diff().diff().diff(), Y4).abs() + _rolling_zscore(netinc.diff().diff().diff(), Y4).abs()
    return _safe_div(z.rolling(Y, min_periods=2).mean(), z.rolling(Y4, min_periods=6).std()).diff().diff().diff()

def f34_rdjk_147_terminal_jerk_warning_composite_4q_d3(revenue: pd.Series, ebit: pd.Series, cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    je = ebit.diff().diff().diff()
    flag = ((jr < 0) & (je < 0) & (cashneq.diff() < 0) & (debt.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff().diff()

def f34_rdjk_148_cliff_edge_jerk_probability_8q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(revenue.diff().diff().diff(), Y4).abs()
    z2 = _rolling_zscore(ebit.diff().diff().diff(), Y4).abs()
    z3 = _rolling_zscore(netinc.diff().diff().diff(), Y4).abs()
    flag = ((z1 > 2.0) | (z2 > 2.0) | (z3 > 2.0)).astype(float)
    return flag.rolling(Y2, min_periods=3).mean().diff().diff().diff()

def f34_rdjk_149_terminal_jerk_state_composite_4q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series, cashneq: pd.Series, debt: pd.Series, shareswa: pd.Series) -> pd.Series:
    jr = revenue.diff().diff().diff()
    je = ebit.diff().diff().diff()
    jn = netinc.diff().diff().diff()
    score = (jr < 0).astype(float) + (je < 0).astype(float) + (jn < 0).astype(float) + (cashneq.diff() < 0).astype(float) + (debt.diff() > 0).astype(float) + (shareswa.diff() > 0).astype(float)
    return score.rolling(Y, min_periods=2).mean().diff().diff().diff()

def f34_rdjk_150_final_revenue_decel_jerk_composite_8q_d3(revenue: pd.Series, ebit: pd.Series, netinc: pd.Series, cashneq: pd.Series) -> pd.Series:
    z = _rolling_zscore(revenue.diff().diff().diff(), Y4) + _rolling_zscore(ebit.diff().diff().diff(), Y4) + _rolling_zscore(netinc.diff().diff().diff(), Y4) + _rolling_zscore(-cashneq.diff().diff().diff(), Y4)
    return z.rolling(Y2, min_periods=3).mean().diff().diff().diff()
REVENUE_DECELERATION_JERK_D3_REGISTRY_076_150 = {'f34_rdjk_076_compound_revenue_jerk_ebit_jerk_same_sign_4q_d3': {'inputs': ['revenue', 'ebit'], 'func': f34_rdjk_076_compound_revenue_jerk_ebit_jerk_same_sign_4q_d3}, 'f34_rdjk_077_compound_revenue_jerk_margin_jerk_4q_d3': {'inputs': ['revenue', 'netinc'], 'func': f34_rdjk_077_compound_revenue_jerk_margin_jerk_4q_d3}, 'f34_rdjk_078_compound_revenue_jerk_cash_jerk_4q_d3': {'inputs': ['revenue', 'cashneq'], 'func': f34_rdjk_078_compound_revenue_jerk_cash_jerk_4q_d3}, 'f34_rdjk_079_compound_revenue_jerk_dilution_jerk_4q_d3': {'inputs': ['revenue', 'shareswa'], 'func': f34_rdjk_079_compound_revenue_jerk_dilution_jerk_4q_d3}, 'f34_rdjk_080_compound_revenue_jerk_receivables_jerk_4q_d3': {'inputs': ['revenue', 'receivables'], 'func': f34_rdjk_080_compound_revenue_jerk_receivables_jerk_4q_d3}, 'f34_rdjk_081_compound_revenue_jerk_inventory_jerk_4q_d3': {'inputs': ['revenue', 'inventory'], 'func': f34_rdjk_081_compound_revenue_jerk_inventory_jerk_4q_d3}, 'f34_rdjk_082_jerk_cooccurrence_count_3metrics_4q_d3': {'inputs': ['revenue', 'ebit', 'netinc'], 'func': f34_rdjk_082_jerk_cooccurrence_count_3metrics_4q_d3}, 'f34_rdjk_083_jerk_magnitude_divergence_revenue_ebit_d3': {'inputs': ['revenue', 'ebit'], 'func': f34_rdjk_083_jerk_magnitude_divergence_revenue_ebit_d3}, 'f34_rdjk_084_revenue_jerk_vs_margin_jerk_z_d3': {'inputs': ['revenue', 'netinc'], 'func': f34_rdjk_084_revenue_jerk_vs_margin_jerk_z_d3}, 'f34_rdjk_085_revenue_jerk_vs_cash_flow_jerk_z_d3': {'inputs': ['revenue', 'fcf'], 'func': f34_rdjk_085_revenue_jerk_vs_cash_flow_jerk_z_d3}, 'f34_rdjk_086_jerk_gm_compression_count_4q_d3': {'inputs': ['revenue', 'ebit'], 'func': f34_rdjk_086_jerk_gm_compression_count_4q_d3}, 'f34_rdjk_087_compound_jerk_index_4q_d3': {'inputs': ['revenue', 'ebit', 'netinc', 'cashneq'], 'func': f34_rdjk_087_compound_jerk_index_4q_d3}, 'f34_rdjk_088_compound_jerk_pos_declining_traj_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_088_compound_jerk_pos_declining_traj_4q_d3}, 'f34_rdjk_089_compound_jerk_pos_revenue_z_neg_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_089_compound_jerk_pos_revenue_z_neg_4q_d3}, 'f34_rdjk_090_compound_jerk_with_ebit_decline_4q_d3': {'inputs': ['revenue', 'ebit'], 'func': f34_rdjk_090_compound_jerk_with_ebit_decline_4q_d3}, 'f34_rdjk_091_revenue_jerk_sequential_decline_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_091_revenue_jerk_sequential_decline_4q_d3}, 'f34_rdjk_092_revenue_jerk_with_yoy_negative_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_092_revenue_jerk_with_yoy_negative_4q_d3}, 'f34_rdjk_093_revenue_jerk_with_2q_qoq_decline_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_093_revenue_jerk_with_2q_qoq_decline_4q_d3}, 'f34_rdjk_094_revenue_jerk_receivables_grow_faster_4q_d3': {'inputs': ['revenue', 'receivables'], 'func': f34_rdjk_094_revenue_jerk_receivables_grow_faster_4q_d3}, 'f34_rdjk_095_revenue_jerk_inventory_grow_faster_4q_d3': {'inputs': ['revenue', 'inventory'], 'func': f34_rdjk_095_revenue_jerk_inventory_grow_faster_4q_d3}, 'f34_rdjk_096_revenue_jerk_with_debt_up_4q_d3': {'inputs': ['revenue', 'debt'], 'func': f34_rdjk_096_revenue_jerk_with_debt_up_4q_d3}, 'f34_rdjk_097_revenue_jerk_with_shares_up_4q_d3': {'inputs': ['revenue', 'shareswa'], 'func': f34_rdjk_097_revenue_jerk_with_shares_up_4q_d3}, 'f34_rdjk_098_revenue_jerk_multimetric_stress_4q_d3': {'inputs': ['revenue', 'ebit', 'cashneq', 'debt', 'shareswa'], 'func': f34_rdjk_098_revenue_jerk_multimetric_stress_4q_d3}, 'f34_rdjk_099_revenue_jerk_highest_decile_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_099_revenue_jerk_highest_decile_16q_d3}, 'f34_rdjk_100_revenue_jerk_composite_stress_count_4q_d3': {'inputs': ['revenue', 'ebit', 'netinc', 'cashneq'], 'func': f34_rdjk_100_revenue_jerk_composite_stress_count_4q_d3}, 'f34_rdjk_101_revenue_accel_slope_cliff_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_101_revenue_accel_slope_cliff_8q_d3}, 'f34_rdjk_102_log_revenue_accel_slope_cliff_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_102_log_revenue_accel_slope_cliff_8q_d3}, 'f34_rdjk_103_compound_revenue_decel_accelerating_decel_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_103_compound_revenue_decel_accelerating_decel_4q_d3}, 'f34_rdjk_104_compound_revenue_accel_sign_chg_margin_sign_chg_4q_d3': {'inputs': ['revenue', 'netinc'], 'func': f34_rdjk_104_compound_revenue_accel_sign_chg_margin_sign_chg_4q_d3}, 'f34_rdjk_105_compound_revenue_accel_sign_chg_ebit_decline_4q_d3': {'inputs': ['revenue', 'ebit'], 'func': f34_rdjk_105_compound_revenue_accel_sign_chg_ebit_decline_4q_d3}, 'f34_rdjk_106_revenue_accel_persistence_index_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_106_revenue_accel_persistence_index_8q_d3}, 'f34_rdjk_107_revenue_accel_persistence_index_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_107_revenue_accel_persistence_index_16q_d3}, 'f34_rdjk_108_compound_persistence_jerk_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_108_compound_persistence_jerk_4q_d3}, 'f34_rdjk_109_revenue_jerk_lowest_decile_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_109_revenue_jerk_lowest_decile_16q_d3}, 'f34_rdjk_110_revenue_accel_quartile_transition_count_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_110_revenue_accel_quartile_transition_count_16q_d3}, 'f34_rdjk_111_revenue_accel_hampel_outliers_count_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_111_revenue_accel_hampel_outliers_count_16q_d3}, 'f34_rdjk_112_revenue_jerk_hampel_outliers_count_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_112_revenue_jerk_hampel_outliers_count_16q_d3}, 'f34_rdjk_113_revenue_jerk_to_chg_ratio_d3': {'inputs': ['revenue'], 'func': f34_rdjk_113_revenue_jerk_to_chg_ratio_d3}, 'f34_rdjk_114_revenue_accel_to_chg_ratio_d3': {'inputs': ['revenue'], 'func': f34_rdjk_114_revenue_accel_to_chg_ratio_d3}, 'f34_rdjk_115_jerk_dormancy_then_2sigma_event_count_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_115_jerk_dormancy_then_2sigma_event_count_16q_d3}, 'f34_rdjk_116_revenue_jerk_to_noise_ratio_d3': {'inputs': ['revenue'], 'func': f34_rdjk_116_revenue_jerk_to_noise_ratio_d3}, 'f34_rdjk_117_revenue_jerk_peak_trough_ratio_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_117_revenue_jerk_peak_trough_ratio_8q_d3}, 'f34_rdjk_118_revenue_jerk_vs_self_baseline_d3': {'inputs': ['revenue'], 'func': f34_rdjk_118_revenue_jerk_vs_self_baseline_d3}, 'f34_rdjk_119_revenue_jerk_regime_score_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_119_revenue_jerk_regime_score_8q_d3}, 'f34_rdjk_120_revenue_jerk_z_above_2sigma_count_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_120_revenue_jerk_z_above_2sigma_count_16q_d3}, 'f34_rdjk_121_revenue_jerk_z_below_minus2sigma_count_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_121_revenue_jerk_z_below_minus2sigma_count_16q_d3}, 'f34_rdjk_122_revenue_jerk_z_abs_exceedance_count_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_122_revenue_jerk_z_abs_exceedance_count_16q_d3}, 'f34_rdjk_123_jerk_lead_lag_with_yoy_accel_lag1_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_123_jerk_lead_lag_with_yoy_accel_lag1_8q_d3}, 'f34_rdjk_124_jerk_conditional_on_low_yoy_level_q25_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_124_jerk_conditional_on_low_yoy_level_q25_16q_d3}, 'f34_rdjk_125_jerk_neg_streak_with_calm_baseline_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_125_jerk_neg_streak_with_calm_baseline_8q_d3}, 'f34_rdjk_126_composite_jerk_accel_signflip_stress_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_126_composite_jerk_accel_signflip_stress_4q_d3}, 'f34_rdjk_127_composite_jerk_accel_signflip_count_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_127_composite_jerk_accel_signflip_count_8q_d3}, 'f34_rdjk_128_weighted_composite_jerk_z_4q_d3': {'inputs': ['revenue', 'netinc', 'ebit'], 'func': f34_rdjk_128_weighted_composite_jerk_z_4q_d3}, 'f34_rdjk_129_composite_jerk_revenue_deterioration_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_129_composite_jerk_revenue_deterioration_4q_d3}, 'f34_rdjk_130_revenue_chaos_index_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_130_revenue_chaos_index_8q_d3}, 'f34_rdjk_131_revenue_jerk_variance_ratio_8q_vs_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_131_revenue_jerk_variance_ratio_8q_vs_16q_d3}, 'f34_rdjk_132_revenue_jerk_lyapunov_proxy_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_132_revenue_jerk_lyapunov_proxy_8q_d3}, 'f34_rdjk_133_revenue_jerk_regime_persistence_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_133_revenue_jerk_regime_persistence_4q_d3}, 'f34_rdjk_134_compound_terminal_jerk_warning_4q_d3': {'inputs': ['revenue', 'ebit', 'cashneq'], 'func': f34_rdjk_134_compound_terminal_jerk_warning_4q_d3}, 'f34_rdjk_135_revenue_accel_cliff_edge_probability_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_135_revenue_accel_cliff_edge_probability_8q_d3}, 'f34_rdjk_136_revenue_jerk_accel_covariance_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_136_revenue_jerk_accel_covariance_8q_d3}, 'f34_rdjk_137_revenue_jerk_margin_jerk_covariance_8q_d3': {'inputs': ['revenue', 'netinc'], 'func': f34_rdjk_137_revenue_jerk_margin_jerk_covariance_8q_d3}, 'f34_rdjk_138_composite_jerk_dispersion_across_metrics_4q_d3': {'inputs': ['revenue', 'ebit', 'netinc'], 'func': f34_rdjk_138_composite_jerk_dispersion_across_metrics_4q_d3}, 'f34_rdjk_139_revenue_jerk_weighted_by_magnitude_4q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_139_revenue_jerk_weighted_by_magnitude_4q_d3}, 'f34_rdjk_140_jerk_onset_breadth_across_horizons_4_8_12_16_d3': {'inputs': ['revenue'], 'func': f34_rdjk_140_jerk_onset_breadth_across_horizons_4_8_12_16_d3}, 'f34_rdjk_141_log_jerk_onset_after_2_consec_low_var_q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_141_log_jerk_onset_after_2_consec_low_var_q_d3}, 'f34_rdjk_142_revenue_jerk_vs_self_baseline_8q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_142_revenue_jerk_vs_self_baseline_8q_d3}, 'f34_rdjk_143_revenue_jerk_consensus_index_4q_d3': {'inputs': ['revenue', 'ebit', 'netinc'], 'func': f34_rdjk_143_revenue_jerk_consensus_index_4q_d3}, 'f34_rdjk_144_revenue_jerk_anomaly_score_4q_d3': {'inputs': ['revenue', 'ebit', 'netinc'], 'func': f34_rdjk_144_revenue_jerk_anomaly_score_4q_d3}, 'f34_rdjk_145_composite_jerk_regime_change_count_16q_d3': {'inputs': ['revenue'], 'func': f34_rdjk_145_composite_jerk_regime_change_count_16q_d3}, 'f34_rdjk_146_composite_jerk_escalation_4q_d3': {'inputs': ['revenue', 'ebit', 'netinc'], 'func': f34_rdjk_146_composite_jerk_escalation_4q_d3}, 'f34_rdjk_147_terminal_jerk_warning_composite_4q_d3': {'inputs': ['revenue', 'ebit', 'cashneq', 'debt'], 'func': f34_rdjk_147_terminal_jerk_warning_composite_4q_d3}, 'f34_rdjk_148_cliff_edge_jerk_probability_8q_d3': {'inputs': ['revenue', 'ebit', 'netinc'], 'func': f34_rdjk_148_cliff_edge_jerk_probability_8q_d3}, 'f34_rdjk_149_terminal_jerk_state_composite_4q_d3': {'inputs': ['revenue', 'ebit', 'netinc', 'cashneq', 'debt', 'shareswa'], 'func': f34_rdjk_149_terminal_jerk_state_composite_4q_d3}, 'f34_rdjk_150_final_revenue_decel_jerk_composite_8q_d3': {'inputs': ['revenue', 'ebit', 'netinc', 'cashneq'], 'func': f34_rdjk_150_final_revenue_decel_jerk_composite_8q_d3}}
