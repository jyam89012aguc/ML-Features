"""Auto-generated D2 wrappers from leverage_buildup_acceleration__base__076_150.py.

Each function inlines the base body and appends .diff() chained 2 time(s)."""
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

def _quadratic_c2(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 2, 3)

    def _c2(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        x = np.arange(len(w))
        try:
            c2, _, _ = np.polyfit(x, w, 2)
            return float(c2)
        except Exception:
            return np.nan
    return s.rolling(n, min_periods=min_periods).apply(_c2, raw=True)

def _structural_break_score(s, n):
    return _rolling_slope(s, n) - _rolling_slope(s.shift(n), n)

def f32_lbac_076_assets_to_equity_accel_z_d2(assets: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(assets, equity)
    return _rolling_zscore(r.diff(), Y4).diff().diff()

def f32_lbac_077_current_ratio_accel_deterioration_z_d2(assets: pd.Series, debt: pd.Series) -> pd.Series:
    r = _safe_div(assets, debt + 1.0)
    return _rolling_zscore(-r.diff(), Y4).diff().diff()

def f32_lbac_078_quick_ratio_accel_z_d2(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    r = _safe_div(cashneq, debt)
    return _rolling_zscore(r.diff(), Y4).diff().diff()

def f32_lbac_079_working_capital_accel_deterioration_z_d2(assets: pd.Series, debt: pd.Series) -> pd.Series:
    wc = assets - debt
    return _rolling_zscore(-wc.diff(), Y4).diff().diff()

def f32_lbac_080_wc_to_sales_accel_z_d2(assets: pd.Series, debt: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(assets - debt, revenue)
    return _rolling_zscore(r.diff(), Y4).diff().diff()

def f32_lbac_081_shares_outstanding_accel_z_d2(shareswa: pd.Series) -> pd.Series:
    return _rolling_zscore(shareswa.diff(), Y4).diff().diff()

def f32_lbac_082_equity_accel_deterioration_z_d2(equity: pd.Series) -> pd.Series:
    return _rolling_zscore(-equity.diff(), Y4).diff().diff()

def f32_lbac_083_cash_equiv_accel_deterioration_z_d2(cashneq: pd.Series) -> pd.Series:
    return _rolling_zscore(-cashneq.diff(), Y4).diff().diff()

def f32_lbac_084_tangible_book_accel_z_d2(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    tb = equity - intangibles
    return _rolling_zscore(tb.diff(), Y4).diff().diff()

def f32_lbac_085_assets_to_equity_structural_break_4q_vs_12q_d2(assets: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(assets, equity)
    return (_rolling_slope(r, Y) - _rolling_slope(r, Y3)).diff().diff()

def f32_lbac_086_cash_inflection_smoothed_raw_sign_flip_8q_d2(cashneq: pd.Series) -> pd.Series:
    sl = _rolling_slope(cashneq, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum().diff().diff()

def f32_lbac_087_compound_shares_up_cash_down_4q_d2(shareswa: pd.Series, cashneq: pd.Series) -> pd.Series:
    flag = ((shareswa.diff() > 0) & (cashneq.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_088_compound_liab_up_equity_flat_4q_d2(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    flat = equity.diff().abs() / equity.replace(0, np.nan) < 0.01
    flag = ((liabilities.diff() > 0) & flat).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_089_compound_assets_down_debt_up_4q_d2(assets: pd.Series, debt: pd.Series) -> pd.Series:
    flag = ((assets.diff() < 0) & (debt.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_090_equity_largest_drop_to_8q_std_d2(equity: pd.Series) -> pd.Series:
    chg = equity.diff()
    mn = chg.rolling(Y2, min_periods=3).min()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (-mn / sd.replace(0, np.nan)).diff().diff()

def f32_lbac_091_quarters_since_equity_neg_accel_d2(equity: pd.Series) -> pd.Series:
    d2 = equity.diff().diff()
    flag = (d2 < 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return (pd.Series(np.arange(len(flag)), index=flag.index) - last).diff().diff()

def f32_lbac_092_wc_to_sales_jerk_z_d2(assets: pd.Series, debt: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(assets - debt, revenue)
    return _rolling_zscore(r.diff().diff().diff(), Y4).diff().diff()

def f32_lbac_093_equity_to_liab_accel_deterioration_z_d2(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    r = _safe_div(equity, liabilities)
    return _rolling_zscore(-r.diff(), Y4).diff().diff()

def f32_lbac_094_shares_cliff_10pct_jump_count_8q_d2(shareswa: pd.Series) -> pd.Series:
    pct = shareswa.pct_change()
    flag = (pct > 0.1).astype(float)
    return flag.rolling(Y2, min_periods=3).sum().diff().diff()

def f32_lbac_095_shares_4q_chg_to_16q_std_d2(shareswa: pd.Series) -> pd.Series:
    chg4 = shareswa.diff(Y)
    sd = chg4.rolling(Y4, min_periods=6).std()
    return (chg4 / sd.replace(0, np.nan)).diff().diff()

def f32_lbac_096_equity_erosion_arc_area_8q_d2(equity: pd.Series) -> pd.Series:

    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, None, 0).sum())
    return equity.rolling(Y2, min_periods=4).apply(_arc, raw=True).diff().diff()

def f32_lbac_097_dilution_rate_recent_minus_prior_4q_d2(shareswa: pd.Series) -> pd.Series:
    chg = shareswa.pct_change()
    a = chg.rolling(Y, min_periods=2).mean()
    b = chg.shift(Y).rolling(Y, min_periods=2).mean()
    return (a - b).diff().diff()

def f32_lbac_098_dilution_2sigma_quarter_count_16q_d2(shareswa: pd.Series) -> pd.Series:
    z = _rolling_zscore(shareswa.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff()

def f32_lbac_099_composite_bs_accel_deterioration_4q_d2(equity: pd.Series, cashneq: pd.Series, shareswa: pd.Series) -> pd.Series:
    z_e = _rolling_zscore(-equity.diff(), Y4)
    z_c = _rolling_zscore(-cashneq.diff(), Y4)
    z_s = _rolling_zscore(shareswa.diff(), Y4)
    return (z_e + z_c + z_s).rolling(Y, min_periods=2).mean().diff().diff()

def f32_lbac_100_log_shares_slope_4q_minus_12q_d2(shareswa: pd.Series) -> pd.Series:
    ls = _safe_log(shareswa)
    return (_rolling_slope(ls, Y) - _rolling_slope(ls, Y3)).diff().diff()

def f32_lbac_101_short_debt_share_accel_z_d2(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    r = _safe_div(debtc, debtc + debtnc)
    return _rolling_zscore(r.diff(), Y4).diff().diff()

def f32_lbac_102_short_debt_share_cliff_8q_d2(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    r = _safe_div(debtc, debtc + debtnc)
    chg = r.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return (chg / sd.replace(0, np.nan)).diff().diff()

def f32_lbac_103_net_debt_chg_to_ebitda_accel_z_d2(debt: pd.Series, cashneq: pd.Series, ebitda: pd.Series) -> pd.Series:
    r = _safe_div(debt - cashneq, ebitda)
    return _rolling_zscore(r.diff(), Y4).diff().diff()

def f32_lbac_104_d2_debt_to_cash_ratio_d2(debt: pd.Series, cashneq: pd.Series) -> pd.Series:
    r = _safe_div(debt, cashneq)
    return r.diff().diff().diff().diff()

def f32_lbac_105_quarters_since_short_debt_accelerated_d2(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    r = _safe_div(debtc, debtc + debtnc)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return (pd.Series(np.arange(len(flag)), index=flag.index) - last).diff().diff()

def f32_lbac_106_compound_short_debt_up_cash_down_4q_d2(debtc: pd.Series, cashneq: pd.Series) -> pd.Series:
    flag = ((debtc.diff() > 0) & (cashneq.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_107_short_debt_structural_break_4q_vs_12q_d2(debtc: pd.Series) -> pd.Series:
    return (_rolling_slope(debtc, Y) - _rolling_slope(debtc, Y3)).diff().diff()

def f32_lbac_108_short_debt_cumulative_excess_8q_d2(debtc: pd.Series) -> pd.Series:

    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return debtc.rolling(Y2, min_periods=4).apply(_arc, raw=True).diff().diff()

def f32_lbac_109_debt_composition_entropy_shift_8q_d2(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    r = _safe_div(debtc, debtc + debtnc)
    return r.rolling(Y2, min_periods=3).std().diff().diff()

def f32_lbac_110_log_debt_mix_chg_z_16q_d2(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    lr = _safe_log(_safe_div(debtc, debtnc))
    return _rolling_zscore(lr.diff(), Y4).diff().diff()

def f32_lbac_111_debt_rollover_risk_short_debt_to_cash_accel_d2(debtc: pd.Series, cashneq: pd.Series) -> pd.Series:
    r = _safe_div(debtc, cashneq)
    return _rolling_zscore(r.diff(), Y4).diff().diff()

def f32_lbac_112_short_debt_inflection_smoothed_raw_sign_flip_8q_d2(debtc: pd.Series) -> pd.Series:
    sl = _rolling_slope(debtc, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum().diff().diff()

def f32_lbac_113_short_debt_recent_4q_minus_prior_4q_d2(debtc: pd.Series) -> pd.Series:
    chg = debtc.diff()
    a = chg.rolling(Y, min_periods=2).mean()
    b = chg.shift(Y).rolling(Y, min_periods=2).mean()
    return (a - b).diff().diff()

def f32_lbac_114_short_debt_to_total_latest_to_16q_max_d2(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    r = _safe_div(debtc, debtc + debtnc)
    return _safe_div(r, r.rolling(Y4, min_periods=6).max()).diff().diff()

def f32_lbac_115_short_debt_2sigma_count_16q_d2(debtc: pd.Series) -> pd.Series:
    z = _rolling_zscore(debtc.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum().diff().diff()

def f32_lbac_116_composite_short_debt_accel_stress_4q_d2(debtc: pd.Series, cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    score = _rolling_zscore(debtc.diff(), Y4) + _rolling_zscore(-cashneq.diff(), Y4) + _rolling_zscore(debt.diff(), Y4)
    return score.rolling(Y, min_periods=2).mean().diff().diff()

def f32_lbac_117_intexp_accel_z_16q_d2(intexp: pd.Series) -> pd.Series:
    return _rolling_zscore(intexp.diff(), Y4).diff().diff()

def f32_lbac_118_effective_rate_accel_z_d2(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    r = _safe_div(intexp, debt)
    return _rolling_zscore(r.diff(), Y4).diff().diff()

def f32_lbac_119_compound_rate_up_debt_up_4q_d2(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    r = _safe_div(intexp, debt)
    flag = ((r.diff() > 0) & (debt.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_120_quarters_since_rate_accelerated_d2(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    r = _safe_div(intexp, debt)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return (pd.Series(np.arange(len(flag)), index=flag.index) - last).diff().diff()

def f32_lbac_121_debt_service_coverage_accel_deterioration_z_d2(ebitda: pd.Series, intexp: pd.Series, debtc: pd.Series) -> pd.Series:
    r = _safe_div(ebitda, intexp + debtc)
    return _rolling_zscore(-r.diff(), Y4).diff().diff()

def f32_lbac_122_composite_debt_service_accel_score_4q_d2(ebitda: pd.Series, intexp: pd.Series, debtc: pd.Series, fcf: pd.Series) -> pd.Series:
    a = _rolling_zscore(-_safe_div(ebitda, intexp + debtc).diff(), Y4)
    b = _rolling_zscore(-_safe_div(fcf, intexp + debtc).diff(), Y4)
    return (a + b).rolling(Y, min_periods=2).mean().diff().diff()

def f32_lbac_123_debt_growth_to_revenue_growth_accel_z_d2(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    spread = debt.pct_change(Y) - revenue.pct_change(Y)
    return _rolling_zscore(spread.diff(), Y4).diff().diff()

def f32_lbac_124_d2_debt_to_revenue_ratio_d2(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(debt, revenue)
    return r.diff().diff().diff().diff()

def f32_lbac_125_cumulative_excess_debt_growth_over_revenue_4q_d2(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    spread = debt.pct_change(Y) - revenue.pct_change(Y)
    return spread.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_126_multimetric_accel_coincidence_count_4q_d2(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    f1 = _safe_div(debt, ebitda).diff().diff() > 0
    f2 = _safe_div(debt, equity).diff().diff() > 0
    f3 = _safe_div(ebit, intexp).diff().diff() < 0
    flag = (f1 & f2 & f3).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_127_compound_all_deteriorating_count_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series) -> pd.Series:
    cov = _safe_div(ebit, intexp)
    flag = ((debt.diff() > 0) & (equity.diff() < 0) & (cov.diff() < 0) & (cashneq.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_128_weighted_composite_z_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(debt.diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    return (z1 + z2 + z3).rolling(Y, min_periods=2).mean().diff().diff()

def f32_lbac_129_composite_stress_accel_4q_d2(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(_safe_div(debt, ebitda).diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    return (z1 + z2).rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_130_variance_explained_by_accel_8q_d2(debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(debt, equity)
    chg = r.diff()
    return _safe_div(chg.rolling(Y2, min_periods=3).var(), chg.rolling(Y4, min_periods=6).var()).diff().diff()

def f32_lbac_131_multivariate_accel_outlier_z_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    z = _rolling_zscore(debt.diff(), Y4) ** 2 + _rolling_zscore(equity.diff(), Y4) ** 2 + _rolling_zscore(ebit.diff(), Y4) ** 2 + _rolling_zscore(intexp.diff(), Y4) ** 2
    return z.rolling(Y, min_periods=2).mean().diff().diff()

def f32_lbac_132_cumulative_stress_accel_index_8q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(debt.diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    return (z1 + z2 + z3).rolling(Y2, min_periods=3).sum().diff().diff()

def f32_lbac_133_compound_deterioration_count_ratio_16q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series) -> pd.Series:
    cov = _safe_div(ebit, intexp)
    flag = ((debt.diff() > 0) & (equity.diff() < 0) & (cov.diff() < 0) & (cashneq.diff() < 0)).astype(float)
    return _safe_div(flag.rolling(Y, min_periods=2).sum(), flag.rolling(Y4, min_periods=6).sum()).diff().diff()

def f32_lbac_134_acceleration_phase_indicator_8q_d2(debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(debt, equity)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    return flag.rolling(Y2, min_periods=3).mean().diff().diff()

def f32_lbac_135_inflection_composite_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    f1 = (np.sign(debt.diff().diff()) != np.sign(debt.diff().diff().shift(1))).astype(float)
    f2 = (np.sign(_safe_div(debt, equity).diff().diff()) != np.sign(_safe_div(debt, equity).diff().diff().shift(1))).astype(float)
    f3 = (np.sign(_safe_div(ebit, intexp).diff().diff()) != np.sign(_safe_div(ebit, intexp).diff().diff().shift(1))).astype(float)
    return (f1 + f2 + f3).rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_136_quadratic_fit_composite_8q_d2(debt: pd.Series, equity: pd.Series) -> pd.Series:
    de = _safe_div(debt, equity)
    return ((_quadratic_c2(debt, Y2) + _quadratic_c2(de, Y2)) / 2.0).diff().diff()

def f32_lbac_137_structural_break_composite_test_8q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    sb1 = _structural_break_score(debt, Y2)
    sb2 = _structural_break_score(_safe_div(debt, equity), Y2)
    sb3 = _structural_break_score(-_safe_div(ebit, intexp), Y2)
    return (sb1 + sb2 + sb3).diff().diff()

def f32_lbac_138_composite_jerk_index_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    j1 = debt.diff().diff().diff().abs()
    j2 = _safe_div(debt, equity).diff().diff().diff().abs()
    j3 = _safe_div(ebit, intexp).diff().diff().diff().abs()
    return ((j1 + j2 + j3) / 3.0).rolling(Y, min_periods=2).mean().diff().diff()

def f32_lbac_139_cliff_edge_composite_count_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(debt.diff(), Y4).abs()
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4).abs()
    z3 = _rolling_zscore(_safe_div(ebit, intexp).diff(), Y4).abs()
    flag = ((z1 > 2.0) | (z2 > 2.0) | (z3 > 2.0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_140_leverage_accel_vs_revenue_accel_spread_4q_d2(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    spread = debt.diff().diff() - revenue.diff().diff()
    return spread.rolling(Y, min_periods=2).mean().diff().diff()

def f32_lbac_141_composite_vs_self_baseline_8q_d2(debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(debt, equity)
    z = _rolling_zscore(r, Y4)
    return (z - z.rolling(Y2, min_periods=3).mean()).diff().diff()

def f32_lbac_142_accel_regime_change_count_16q_d2(debt: pd.Series, equity: pd.Series) -> pd.Series:
    r = _safe_div(debt, equity)
    sl = _rolling_slope(r, Y)
    flip = (np.sign(sl) != np.sign(sl.shift(1))).astype(float)
    return flip.rolling(Y4, min_periods=6).sum().diff().diff()

def f32_lbac_143_weighted_composite_metric_accel_4q_d2(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series) -> pd.Series:
    z1 = 0.4 * _rolling_zscore(_safe_div(debt, ebitda).diff(), Y4)
    z2 = 0.3 * _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = 0.3 * _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    return (z1 + z2 + z3).rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_144_dispersion_accel_metrics_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(debt.diff(), Y4).rolling(Y, min_periods=2).mean()
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4).rolling(Y, min_periods=2).mean()
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4).rolling(Y, min_periods=2).mean()
    return pd.concat([z1, z2, z3], axis=1).std(axis=1).diff().diff()

def f32_lbac_145_coincidence_index_z2_across_metrics_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(debt.diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    flag = ((z1 > 2.0) & (z2 > 2.0) & (z3 > 2.0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_146_composite_leverage_escalation_4q_d2(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(_safe_div(debt, ebitda).diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    comp = z1 + z2 + z3
    return _safe_div(comp.rolling(Y, min_periods=2).mean(), comp.rolling(Y4, min_periods=6).std()).diff().diff()

def f32_lbac_147_terminal_accel_warning_composite_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series) -> pd.Series:
    f1 = debt.diff().diff() > 0
    f2 = _safe_div(ebit, intexp).diff().diff() < 0
    f3 = cashneq.diff().diff() < 0
    flag = (f1 & f2 & f3).astype(float)
    return flag.rolling(Y, min_periods=2).sum().diff().diff()

def f32_lbac_148_cliff_edge_probability_8q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(debt.diff(), Y4).abs()
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4).abs()
    z3 = _rolling_zscore(_safe_div(ebit, intexp).diff(), Y4).abs()
    flag = ((z1 > 2.0) | (z2 > 2.0) | (z3 > 2.0)).astype(float)
    return flag.rolling(Y2, min_periods=3).mean().diff().diff()

def f32_lbac_149_terminal_state_composite_score_4q_d2(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series, fcf: pd.Series) -> pd.Series:
    cov = _safe_div(ebit, intexp)
    score = (debt.diff() > 0).astype(float) + (equity.diff() < 0).astype(float) + (cov.diff() < 0).astype(float) + (cashneq.diff() < 0).astype(float) + (fcf.diff() < 0).astype(float)
    return score.rolling(Y, min_periods=2).mean().diff().diff()

def f32_lbac_150_final_leverage_buildup_accel_composite_8q_d2(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series, shareswa: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(_safe_div(debt, ebitda).diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    z4 = _rolling_zscore(-cashneq.diff(), Y4)
    z5 = _rolling_zscore(shareswa.diff(), Y4)
    return (z1 + z2 + z3 + z4 + z5).rolling(Y2, min_periods=3).mean().diff().diff()
LEVERAGE_BUILDUP_ACCELERATION_D2_REGISTRY_076_150 = {'f32_lbac_076_assets_to_equity_accel_z_d2': {'inputs': ['assets', 'equity'], 'func': f32_lbac_076_assets_to_equity_accel_z_d2}, 'f32_lbac_077_current_ratio_accel_deterioration_z_d2': {'inputs': ['assets', 'debt'], 'func': f32_lbac_077_current_ratio_accel_deterioration_z_d2}, 'f32_lbac_078_quick_ratio_accel_z_d2': {'inputs': ['cashneq', 'debt'], 'func': f32_lbac_078_quick_ratio_accel_z_d2}, 'f32_lbac_079_working_capital_accel_deterioration_z_d2': {'inputs': ['assets', 'debt'], 'func': f32_lbac_079_working_capital_accel_deterioration_z_d2}, 'f32_lbac_080_wc_to_sales_accel_z_d2': {'inputs': ['assets', 'debt', 'revenue'], 'func': f32_lbac_080_wc_to_sales_accel_z_d2}, 'f32_lbac_081_shares_outstanding_accel_z_d2': {'inputs': ['shareswa'], 'func': f32_lbac_081_shares_outstanding_accel_z_d2}, 'f32_lbac_082_equity_accel_deterioration_z_d2': {'inputs': ['equity'], 'func': f32_lbac_082_equity_accel_deterioration_z_d2}, 'f32_lbac_083_cash_equiv_accel_deterioration_z_d2': {'inputs': ['cashneq'], 'func': f32_lbac_083_cash_equiv_accel_deterioration_z_d2}, 'f32_lbac_084_tangible_book_accel_z_d2': {'inputs': ['equity', 'intangibles'], 'func': f32_lbac_084_tangible_book_accel_z_d2}, 'f32_lbac_085_assets_to_equity_structural_break_4q_vs_12q_d2': {'inputs': ['assets', 'equity'], 'func': f32_lbac_085_assets_to_equity_structural_break_4q_vs_12q_d2}, 'f32_lbac_086_cash_inflection_smoothed_raw_sign_flip_8q_d2': {'inputs': ['cashneq'], 'func': f32_lbac_086_cash_inflection_smoothed_raw_sign_flip_8q_d2}, 'f32_lbac_087_compound_shares_up_cash_down_4q_d2': {'inputs': ['shareswa', 'cashneq'], 'func': f32_lbac_087_compound_shares_up_cash_down_4q_d2}, 'f32_lbac_088_compound_liab_up_equity_flat_4q_d2': {'inputs': ['liabilities', 'equity'], 'func': f32_lbac_088_compound_liab_up_equity_flat_4q_d2}, 'f32_lbac_089_compound_assets_down_debt_up_4q_d2': {'inputs': ['assets', 'debt'], 'func': f32_lbac_089_compound_assets_down_debt_up_4q_d2}, 'f32_lbac_090_equity_largest_drop_to_8q_std_d2': {'inputs': ['equity'], 'func': f32_lbac_090_equity_largest_drop_to_8q_std_d2}, 'f32_lbac_091_quarters_since_equity_neg_accel_d2': {'inputs': ['equity'], 'func': f32_lbac_091_quarters_since_equity_neg_accel_d2}, 'f32_lbac_092_wc_to_sales_jerk_z_d2': {'inputs': ['assets', 'debt', 'revenue'], 'func': f32_lbac_092_wc_to_sales_jerk_z_d2}, 'f32_lbac_093_equity_to_liab_accel_deterioration_z_d2': {'inputs': ['equity', 'liabilities'], 'func': f32_lbac_093_equity_to_liab_accel_deterioration_z_d2}, 'f32_lbac_094_shares_cliff_10pct_jump_count_8q_d2': {'inputs': ['shareswa'], 'func': f32_lbac_094_shares_cliff_10pct_jump_count_8q_d2}, 'f32_lbac_095_shares_4q_chg_to_16q_std_d2': {'inputs': ['shareswa'], 'func': f32_lbac_095_shares_4q_chg_to_16q_std_d2}, 'f32_lbac_096_equity_erosion_arc_area_8q_d2': {'inputs': ['equity'], 'func': f32_lbac_096_equity_erosion_arc_area_8q_d2}, 'f32_lbac_097_dilution_rate_recent_minus_prior_4q_d2': {'inputs': ['shareswa'], 'func': f32_lbac_097_dilution_rate_recent_minus_prior_4q_d2}, 'f32_lbac_098_dilution_2sigma_quarter_count_16q_d2': {'inputs': ['shareswa'], 'func': f32_lbac_098_dilution_2sigma_quarter_count_16q_d2}, 'f32_lbac_099_composite_bs_accel_deterioration_4q_d2': {'inputs': ['equity', 'cashneq', 'shareswa'], 'func': f32_lbac_099_composite_bs_accel_deterioration_4q_d2}, 'f32_lbac_100_log_shares_slope_4q_minus_12q_d2': {'inputs': ['shareswa'], 'func': f32_lbac_100_log_shares_slope_4q_minus_12q_d2}, 'f32_lbac_101_short_debt_share_accel_z_d2': {'inputs': ['debtc', 'debtnc'], 'func': f32_lbac_101_short_debt_share_accel_z_d2}, 'f32_lbac_102_short_debt_share_cliff_8q_d2': {'inputs': ['debtc', 'debtnc'], 'func': f32_lbac_102_short_debt_share_cliff_8q_d2}, 'f32_lbac_103_net_debt_chg_to_ebitda_accel_z_d2': {'inputs': ['debt', 'cashneq', 'ebitda'], 'func': f32_lbac_103_net_debt_chg_to_ebitda_accel_z_d2}, 'f32_lbac_104_d2_debt_to_cash_ratio_d2': {'inputs': ['debt', 'cashneq'], 'func': f32_lbac_104_d2_debt_to_cash_ratio_d2}, 'f32_lbac_105_quarters_since_short_debt_accelerated_d2': {'inputs': ['debtc', 'debtnc'], 'func': f32_lbac_105_quarters_since_short_debt_accelerated_d2}, 'f32_lbac_106_compound_short_debt_up_cash_down_4q_d2': {'inputs': ['debtc', 'cashneq'], 'func': f32_lbac_106_compound_short_debt_up_cash_down_4q_d2}, 'f32_lbac_107_short_debt_structural_break_4q_vs_12q_d2': {'inputs': ['debtc'], 'func': f32_lbac_107_short_debt_structural_break_4q_vs_12q_d2}, 'f32_lbac_108_short_debt_cumulative_excess_8q_d2': {'inputs': ['debtc'], 'func': f32_lbac_108_short_debt_cumulative_excess_8q_d2}, 'f32_lbac_109_debt_composition_entropy_shift_8q_d2': {'inputs': ['debtc', 'debtnc'], 'func': f32_lbac_109_debt_composition_entropy_shift_8q_d2}, 'f32_lbac_110_log_debt_mix_chg_z_16q_d2': {'inputs': ['debtc', 'debtnc'], 'func': f32_lbac_110_log_debt_mix_chg_z_16q_d2}, 'f32_lbac_111_debt_rollover_risk_short_debt_to_cash_accel_d2': {'inputs': ['debtc', 'cashneq'], 'func': f32_lbac_111_debt_rollover_risk_short_debt_to_cash_accel_d2}, 'f32_lbac_112_short_debt_inflection_smoothed_raw_sign_flip_8q_d2': {'inputs': ['debtc'], 'func': f32_lbac_112_short_debt_inflection_smoothed_raw_sign_flip_8q_d2}, 'f32_lbac_113_short_debt_recent_4q_minus_prior_4q_d2': {'inputs': ['debtc'], 'func': f32_lbac_113_short_debt_recent_4q_minus_prior_4q_d2}, 'f32_lbac_114_short_debt_to_total_latest_to_16q_max_d2': {'inputs': ['debtc', 'debtnc'], 'func': f32_lbac_114_short_debt_to_total_latest_to_16q_max_d2}, 'f32_lbac_115_short_debt_2sigma_count_16q_d2': {'inputs': ['debtc'], 'func': f32_lbac_115_short_debt_2sigma_count_16q_d2}, 'f32_lbac_116_composite_short_debt_accel_stress_4q_d2': {'inputs': ['debtc', 'cashneq', 'debt'], 'func': f32_lbac_116_composite_short_debt_accel_stress_4q_d2}, 'f32_lbac_117_intexp_accel_z_16q_d2': {'inputs': ['intexp'], 'func': f32_lbac_117_intexp_accel_z_16q_d2}, 'f32_lbac_118_effective_rate_accel_z_d2': {'inputs': ['intexp', 'debt'], 'func': f32_lbac_118_effective_rate_accel_z_d2}, 'f32_lbac_119_compound_rate_up_debt_up_4q_d2': {'inputs': ['intexp', 'debt'], 'func': f32_lbac_119_compound_rate_up_debt_up_4q_d2}, 'f32_lbac_120_quarters_since_rate_accelerated_d2': {'inputs': ['intexp', 'debt'], 'func': f32_lbac_120_quarters_since_rate_accelerated_d2}, 'f32_lbac_121_debt_service_coverage_accel_deterioration_z_d2': {'inputs': ['ebitda', 'intexp', 'debtc'], 'func': f32_lbac_121_debt_service_coverage_accel_deterioration_z_d2}, 'f32_lbac_122_composite_debt_service_accel_score_4q_d2': {'inputs': ['ebitda', 'intexp', 'debtc', 'fcf'], 'func': f32_lbac_122_composite_debt_service_accel_score_4q_d2}, 'f32_lbac_123_debt_growth_to_revenue_growth_accel_z_d2': {'inputs': ['debt', 'revenue'], 'func': f32_lbac_123_debt_growth_to_revenue_growth_accel_z_d2}, 'f32_lbac_124_d2_debt_to_revenue_ratio_d2': {'inputs': ['debt', 'revenue'], 'func': f32_lbac_124_d2_debt_to_revenue_ratio_d2}, 'f32_lbac_125_cumulative_excess_debt_growth_over_revenue_4q_d2': {'inputs': ['debt', 'revenue'], 'func': f32_lbac_125_cumulative_excess_debt_growth_over_revenue_4q_d2}, 'f32_lbac_126_multimetric_accel_coincidence_count_4q_d2': {'inputs': ['debt', 'equity', 'ebitda', 'ebit', 'intexp'], 'func': f32_lbac_126_multimetric_accel_coincidence_count_4q_d2}, 'f32_lbac_127_compound_all_deteriorating_count_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp', 'cashneq'], 'func': f32_lbac_127_compound_all_deteriorating_count_4q_d2}, 'f32_lbac_128_weighted_composite_z_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_128_weighted_composite_z_4q_d2}, 'f32_lbac_129_composite_stress_accel_4q_d2': {'inputs': ['debt', 'equity', 'ebitda', 'intexp'], 'func': f32_lbac_129_composite_stress_accel_4q_d2}, 'f32_lbac_130_variance_explained_by_accel_8q_d2': {'inputs': ['debt', 'equity'], 'func': f32_lbac_130_variance_explained_by_accel_8q_d2}, 'f32_lbac_131_multivariate_accel_outlier_z_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_131_multivariate_accel_outlier_z_4q_d2}, 'f32_lbac_132_cumulative_stress_accel_index_8q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_132_cumulative_stress_accel_index_8q_d2}, 'f32_lbac_133_compound_deterioration_count_ratio_16q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp', 'cashneq'], 'func': f32_lbac_133_compound_deterioration_count_ratio_16q_d2}, 'f32_lbac_134_acceleration_phase_indicator_8q_d2': {'inputs': ['debt', 'equity'], 'func': f32_lbac_134_acceleration_phase_indicator_8q_d2}, 'f32_lbac_135_inflection_composite_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_135_inflection_composite_4q_d2}, 'f32_lbac_136_quadratic_fit_composite_8q_d2': {'inputs': ['debt', 'equity'], 'func': f32_lbac_136_quadratic_fit_composite_8q_d2}, 'f32_lbac_137_structural_break_composite_test_8q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_137_structural_break_composite_test_8q_d2}, 'f32_lbac_138_composite_jerk_index_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_138_composite_jerk_index_4q_d2}, 'f32_lbac_139_cliff_edge_composite_count_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_139_cliff_edge_composite_count_4q_d2}, 'f32_lbac_140_leverage_accel_vs_revenue_accel_spread_4q_d2': {'inputs': ['debt', 'revenue'], 'func': f32_lbac_140_leverage_accel_vs_revenue_accel_spread_4q_d2}, 'f32_lbac_141_composite_vs_self_baseline_8q_d2': {'inputs': ['debt', 'equity'], 'func': f32_lbac_141_composite_vs_self_baseline_8q_d2}, 'f32_lbac_142_accel_regime_change_count_16q_d2': {'inputs': ['debt', 'equity'], 'func': f32_lbac_142_accel_regime_change_count_16q_d2}, 'f32_lbac_143_weighted_composite_metric_accel_4q_d2': {'inputs': ['debt', 'equity', 'ebitda', 'ebit', 'intexp', 'cashneq'], 'func': f32_lbac_143_weighted_composite_metric_accel_4q_d2}, 'f32_lbac_144_dispersion_accel_metrics_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_144_dispersion_accel_metrics_4q_d2}, 'f32_lbac_145_coincidence_index_z2_across_metrics_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_145_coincidence_index_z2_across_metrics_4q_d2}, 'f32_lbac_146_composite_leverage_escalation_4q_d2': {'inputs': ['debt', 'equity', 'ebitda', 'ebit', 'intexp'], 'func': f32_lbac_146_composite_leverage_escalation_4q_d2}, 'f32_lbac_147_terminal_accel_warning_composite_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp', 'cashneq'], 'func': f32_lbac_147_terminal_accel_warning_composite_4q_d2}, 'f32_lbac_148_cliff_edge_probability_8q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp'], 'func': f32_lbac_148_cliff_edge_probability_8q_d2}, 'f32_lbac_149_terminal_state_composite_score_4q_d2': {'inputs': ['debt', 'equity', 'ebit', 'intexp', 'cashneq', 'fcf'], 'func': f32_lbac_149_terminal_state_composite_score_4q_d2}, 'f32_lbac_150_final_leverage_buildup_accel_composite_8q_d2': {'inputs': ['debt', 'equity', 'ebitda', 'ebit', 'intexp', 'cashneq', 'shareswa'], 'func': f32_lbac_150_final_leverage_buildup_accel_composite_8q_d2}}
