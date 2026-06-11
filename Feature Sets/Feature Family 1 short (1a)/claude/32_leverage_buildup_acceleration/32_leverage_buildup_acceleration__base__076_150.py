"""leverage_buildup_acceleration base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continued. Theme: balance-sheet quality acceleration deterioration, debt-maturity
composition acceleration, composite multi-metric acceleration detectors.
"""
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
    idx = num.index if hasattr(num, "index") else None
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


# ============================================================
#                  FEATURES 076-150
# ============================================================

def f32_lbac_076_assets_to_equity_accel_z(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in assets/equity over 16Q — leverage-multiplier acceleration."""
    r = _safe_div(assets, equity)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_077_current_ratio_accel_deterioration_z(assets: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in assets/(debt+1) over 16Q — liquidity-ratio deterioration acceleration."""
    r = _safe_div(assets, debt + 1.0)
    return _rolling_zscore(-r.diff(), Y4)


def f32_lbac_078_quick_ratio_accel_z(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in (cash/debt) — quick-ratio proxy acceleration (cash-only liquidity)."""
    r = _safe_div(cashneq, debt)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_079_working_capital_accel_deterioration_z(assets: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in (assets-debt) — working-capital proxy deterioration."""
    wc = assets - debt
    return _rolling_zscore(-wc.diff(), Y4)


def f32_lbac_080_wc_to_sales_accel_z(assets: pd.Series, debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in (assets-debt)/revenue over 16Q — operating-leverage acceleration."""
    r = _safe_div(assets - debt, revenue)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_081_shares_outstanding_accel_z(shareswa: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in shareswa — dilution-rate acceleration."""
    return _rolling_zscore(shareswa.diff(), Y4)


def f32_lbac_082_equity_accel_deterioration_z(equity: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in equity over 16Q — equity erosion acceleration."""
    return _rolling_zscore(-equity.diff(), Y4)


def f32_lbac_083_cash_equiv_accel_deterioration_z(cashneq: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in cash over 16Q — cash-burn acceleration."""
    return _rolling_zscore(-cashneq.diff(), Y4)


def f32_lbac_084_tangible_book_accel_z(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in (equity - intangibles) over 16Q — tangible-book acceleration."""
    tb = equity - intangibles
    return _rolling_zscore(tb.diff(), Y4)


def f32_lbac_085_assets_to_equity_structural_break_4q_vs_12q(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """A/E 4Q slope minus 12Q slope — leverage-multiplier trend speedup."""
    r = _safe_div(assets, equity)
    return _rolling_slope(r, Y) - _rolling_slope(r, Y3)


def f32_lbac_086_cash_inflection_smoothed_raw_sign_flip_8q(cashneq: pd.Series) -> pd.Series:
    """Sign-flip count of cash slope vs EMA-smoothed slope over 8Q — cash-trajectory inflection."""
    sl = _rolling_slope(cashneq, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f32_lbac_087_compound_shares_up_cash_down_4q(shareswa: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Count of 4Q with shares rising AND cash falling — dilution + cash drain coincidence."""
    flag = ((shareswa.diff() > 0) & (cashneq.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_088_compound_liab_up_equity_flat_4q(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Count of 4Q with liabilities rising AND equity within 1pct of prior — liab without equity offset."""
    flat = (equity.diff().abs() / equity.replace(0, np.nan)) < 0.01
    flag = ((liabilities.diff() > 0) & flat).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_089_compound_assets_down_debt_up_4q(assets: pd.Series, debt: pd.Series) -> pd.Series:
    """Count of 4Q with assets shrinking AND debt rising — distress signature."""
    flag = ((assets.diff() < 0) & (debt.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_090_equity_largest_drop_to_8q_std(equity: pd.Series) -> pd.Series:
    """Max 1Q equity drop in 8Q / 8Q std of equity changes."""
    chg = equity.diff()
    mn = chg.rolling(Y2, min_periods=3).min()
    sd = chg.rolling(Y2, min_periods=3).std()
    return -mn / sd.replace(0, np.nan)


def f32_lbac_091_quarters_since_equity_neg_accel(equity: pd.Series) -> pd.Series:
    """Quarters since equity d2 last crossed below zero."""
    d2 = equity.diff().diff()
    flag = (d2 < 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f32_lbac_092_wc_to_sales_jerk_z(assets: pd.Series, debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of 3rd diff of (assets-debt)/revenue over 16Q — jerk in operating-leverage trajectory."""
    r = _safe_div(assets - debt, revenue)
    return _rolling_zscore(r.diff().diff().diff(), Y4)


def f32_lbac_093_equity_to_liab_accel_deterioration_z(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in equity/liabilities over 16Q — equity-coverage deterioration."""
    r = _safe_div(equity, liabilities)
    return _rolling_zscore(-r.diff(), Y4)


def f32_lbac_094_shares_cliff_10pct_jump_count_8q(shareswa: pd.Series) -> pd.Series:
    """Count of 8Q with 1Q share-count jump >10pct — dilution-cliff events."""
    pct = shareswa.pct_change()
    flag = (pct > 0.10).astype(float)
    return flag.rolling(Y2, min_periods=3).sum()


def f32_lbac_095_shares_4q_chg_to_16q_std(shareswa: pd.Series) -> pd.Series:
    """4Q share-count change / 16Q std of 4Q changes."""
    chg4 = shareswa.diff(Y)
    sd = chg4.rolling(Y4, min_periods=6).std()
    return chg4 / sd.replace(0, np.nan)


def f32_lbac_096_equity_erosion_arc_area_8q(equity: pd.Series) -> pd.Series:
    """Sum of negative residuals of equity vs 8Q linear fit — erosion-below-trend integral."""
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, None, 0).sum())
    return equity.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f32_lbac_097_dilution_rate_recent_minus_prior_4q(shareswa: pd.Series) -> pd.Series:
    """Mean 1Q share-count pct chg in last 4Q minus mean in prior 4Q."""
    chg = shareswa.pct_change()
    a = chg.rolling(Y, min_periods=2).mean()
    b = chg.shift(Y).rolling(Y, min_periods=2).mean()
    return a - b


def f32_lbac_098_dilution_2sigma_quarter_count_16q(shareswa: pd.Series) -> pd.Series:
    """Count of 1Q share-count changes with z>2 (vs 16Q) over 16Q."""
    z = _rolling_zscore(shareswa.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f32_lbac_099_composite_bs_accel_deterioration_4q(equity: pd.Series, cashneq: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Mean 4Q of (-z(equity chg) + -z(cash chg) + z(shares chg))."""
    z_e = _rolling_zscore(-equity.diff(), Y4)
    z_c = _rolling_zscore(-cashneq.diff(), Y4)
    z_s = _rolling_zscore(shareswa.diff(), Y4)
    return (z_e + z_c + z_s).rolling(Y, min_periods=2).mean()


def f32_lbac_100_log_shares_slope_4q_minus_12q(shareswa: pd.Series) -> pd.Series:
    """Log-share-count 4Q slope minus 12Q slope — log-space dilution speedup."""
    ls = _safe_log(shareswa)
    return _rolling_slope(ls, Y) - _rolling_slope(ls, Y3)


def f32_lbac_101_short_debt_share_accel_z(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in debtc/(debtc+debtnc) — short-debt-share acceleration."""
    r = _safe_div(debtc, debtc + debtnc)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_102_short_debt_share_cliff_8q(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    """1Q jump in short-debt share / 8Q std of changes."""
    r = _safe_div(debtc, debtc + debtnc)
    chg = r.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return chg / sd.replace(0, np.nan)


def f32_lbac_103_net_debt_chg_to_ebitda_accel_z(debt: pd.Series, cashneq: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in (debt-cash)/ebitda — net-leverage acceleration."""
    r = _safe_div(debt - cashneq, ebitda)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_104_d2_debt_to_cash_ratio(debt: pd.Series, cashneq: pd.Series) -> pd.Series:
    """2nd diff of debt/cash — acceleration of debt-to-cash."""
    r = _safe_div(debt, cashneq)
    return r.diff().diff()


def f32_lbac_105_quarters_since_short_debt_accelerated(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    """Quarters since short-debt-share d2 crossed above zero."""
    r = _safe_div(debtc, debtc + debtnc)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f32_lbac_106_compound_short_debt_up_cash_down_4q(debtc: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Count of 4Q with short-debt rising AND cash falling — rollover-stress coincidence."""
    flag = ((debtc.diff() > 0) & (cashneq.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_107_short_debt_structural_break_4q_vs_12q(debtc: pd.Series) -> pd.Series:
    """Short-debt 4Q slope minus 12Q slope."""
    return _rolling_slope(debtc, Y) - _rolling_slope(debtc, Y3)


def f32_lbac_108_short_debt_cumulative_excess_8q(debtc: pd.Series) -> pd.Series:
    """Cumulative positive residual of short-debt above 8Q linear fit."""
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return debtc.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f32_lbac_109_debt_composition_entropy_shift_8q(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    """8Q std of (debtc share) — variability of composition (rising = composition churn)."""
    r = _safe_div(debtc, debtc + debtnc)
    return r.rolling(Y2, min_periods=3).std()


def f32_lbac_110_log_debt_mix_chg_z_16q(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    """Z-score of log(debtc/debtnc) 1Q change over 16Q."""
    lr = _safe_log(_safe_div(debtc, debtnc))
    return _rolling_zscore(lr.diff(), Y4)


def f32_lbac_111_debt_rollover_risk_short_debt_to_cash_accel(debtc: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in debtc/cash — rollover-coverage acceleration deterioration."""
    r = _safe_div(debtc, cashneq)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_112_short_debt_inflection_smoothed_raw_sign_flip_8q(debtc: pd.Series) -> pd.Series:
    """Sign-flip count of short-debt slope vs EMA-smoothed slope over 8Q."""
    sl = _rolling_slope(debtc, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f32_lbac_113_short_debt_recent_4q_minus_prior_4q(debtc: pd.Series) -> pd.Series:
    """Mean 1Q short-debt change in last 4Q minus mean in prior 4Q."""
    chg = debtc.diff()
    a = chg.rolling(Y, min_periods=2).mean()
    b = chg.shift(Y).rolling(Y, min_periods=2).mean()
    return a - b


def f32_lbac_114_short_debt_to_total_latest_to_16q_max(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    """Current short-debt-share / 16Q max — proximity to recent peak."""
    r = _safe_div(debtc, debtc + debtnc)
    return _safe_div(r, r.rolling(Y4, min_periods=6).max())


def f32_lbac_115_short_debt_2sigma_count_16q(debtc: pd.Series) -> pd.Series:
    """Count of 1Q short-debt changes with z>2 over 16Q."""
    z = _rolling_zscore(debtc.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f32_lbac_116_composite_short_debt_accel_stress_4q(debtc: pd.Series, cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """Mean 4Q of z(short-debt chg) + z(-cash chg) + z(debt chg)."""
    score = _rolling_zscore(debtc.diff(), Y4) + _rolling_zscore(-cashneq.diff(), Y4) + _rolling_zscore(debt.diff(), Y4)
    return score.rolling(Y, min_periods=2).mean()


def f32_lbac_117_intexp_accel_z_16q(intexp: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in interest expense over 16Q."""
    return _rolling_zscore(intexp.diff(), Y4)


def f32_lbac_118_effective_rate_accel_z(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in intexp/debt — effective-rate acceleration."""
    r = _safe_div(intexp, debt)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_119_compound_rate_up_debt_up_4q(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """Count of 4Q with effective-rate rising AND debt rising — compounding-burden coincidence."""
    r = _safe_div(intexp, debt)
    flag = ((r.diff() > 0) & (debt.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_120_quarters_since_rate_accelerated(intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """Quarters since effective-rate d2 last crossed above zero."""
    r = _safe_div(intexp, debt)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f32_lbac_121_debt_service_coverage_accel_deterioration_z(ebitda: pd.Series, intexp: pd.Series, debtc: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in ebitda/(intexp+debtc) — debt-service-coverage deterioration."""
    r = _safe_div(ebitda, intexp + debtc)
    return _rolling_zscore(-r.diff(), Y4)


def f32_lbac_122_composite_debt_service_accel_score_4q(ebitda: pd.Series, intexp: pd.Series, debtc: pd.Series, fcf: pd.Series) -> pd.Series:
    """Mean 4Q of -z(ebitda/(intexp+debtc) chg) + -z(fcf/(intexp+debtc) chg)."""
    a = _rolling_zscore(-_safe_div(ebitda, intexp + debtc).diff(), Y4)
    b = _rolling_zscore(-_safe_div(fcf, intexp + debtc).diff(), Y4)
    return (a + b).rolling(Y, min_periods=2).mean()


def f32_lbac_123_debt_growth_to_revenue_growth_accel_z(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in (4Q debt growth - 4Q revenue growth) — leverage-growing-faster-than-business."""
    spread = debt.pct_change(Y) - revenue.pct_change(Y)
    return _rolling_zscore(spread.diff(), Y4)


def f32_lbac_124_d2_debt_to_revenue_ratio(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """2nd diff of debt/revenue — convexity of leverage relative to top line."""
    r = _safe_div(debt, revenue)
    return r.diff().diff()


def f32_lbac_125_cumulative_excess_debt_growth_over_revenue_4q(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Cumulative (debt 4Q pct chg - revenue 4Q pct chg) over last 4Q."""
    spread = debt.pct_change(Y) - revenue.pct_change(Y)
    return spread.rolling(Y, min_periods=2).sum()


def f32_lbac_126_multimetric_accel_coincidence_count_4q(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count 4Q with debt/ebitda d2>0 AND D/E d2>0 AND coverage d2<0 — coincidence of accelerating stress metrics."""
    f1 = _safe_div(debt, ebitda).diff().diff() > 0
    f2 = _safe_div(debt, equity).diff().diff() > 0
    f3 = _safe_div(ebit, intexp).diff().diff() < 0
    flag = (f1 & f2 & f3).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_127_compound_all_deteriorating_count_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Count 4Q where debt rose AND equity fell AND coverage fell AND cash fell — quadruple-deterioration coincidence."""
    cov = _safe_div(ebit, intexp)
    flag = ((debt.diff() > 0) & (equity.diff() < 0) & (cov.diff() < 0) & (cashneq.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_128_weighted_composite_z_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Mean 4Q of (z(debt chg) + z(D/E chg) + z(-coverage chg)) — weighted leverage-stress accelerator."""
    z1 = _rolling_zscore(debt.diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    return (z1 + z2 + z3).rolling(Y, min_periods=2).mean()


def f32_lbac_129_composite_stress_accel_4q(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Sum over 4Q of (z(d/ebitda chg) + z(d/e chg))."""
    z1 = _rolling_zscore(_safe_div(debt, ebitda).diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    return (z1 + z2).rolling(Y, min_periods=2).sum()


def f32_lbac_130_variance_explained_by_accel_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """8Q variance of D/E 1Q changes / 16Q variance — recent acceleration variability concentration."""
    r = _safe_div(debt, equity)
    chg = r.diff()
    return _safe_div(chg.rolling(Y2, min_periods=3).var(), chg.rolling(Y4, min_periods=6).var())


def f32_lbac_131_multivariate_accel_outlier_z_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Sum of squared z-scores across 4 metrics, averaged over 4Q — multivariate outlier index."""
    z = (
        _rolling_zscore(debt.diff(), Y4) ** 2
        + _rolling_zscore(equity.diff(), Y4) ** 2
        + _rolling_zscore(ebit.diff(), Y4) ** 2
        + _rolling_zscore(intexp.diff(), Y4) ** 2
    )
    return z.rolling(Y, min_periods=2).mean()


def f32_lbac_132_cumulative_stress_accel_index_8q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Cumulative sum over 8Q of composite stress z-score."""
    z1 = _rolling_zscore(debt.diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    return (z1 + z2 + z3).rolling(Y2, min_periods=3).sum()


def f32_lbac_133_compound_deterioration_count_ratio_16q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series) -> pd.Series:
    """4Q compound-deterioration count / 16Q baseline count."""
    cov = _safe_div(ebit, intexp)
    flag = ((debt.diff() > 0) & (equity.diff() < 0) & (cov.diff() < 0) & (cashneq.diff() < 0)).astype(float)
    return _safe_div(flag.rolling(Y, min_periods=2).sum(), flag.rolling(Y4, min_periods=6).sum())


def f32_lbac_134_acceleration_phase_indicator_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Fraction of last 8Q where D/E d2 > 0 — probability of being in acceleration phase."""
    r = _safe_div(debt, equity)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    return flag.rolling(Y2, min_periods=3).mean()


def f32_lbac_135_inflection_composite_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Sum over 4Q of indicator flags where any of debt/D-E/coverage d2 changed sign."""
    f1 = (np.sign(debt.diff().diff()) != np.sign(debt.diff().diff().shift(1))).astype(float)
    f2 = (np.sign(_safe_div(debt, equity).diff().diff()) != np.sign(_safe_div(debt, equity).diff().diff().shift(1))).astype(float)
    f3 = (np.sign(_safe_div(ebit, intexp).diff().diff()) != np.sign(_safe_div(ebit, intexp).diff().diff().shift(1))).astype(float)
    return (f1 + f2 + f3).rolling(Y, min_periods=2).sum()


def f32_lbac_136_quadratic_fit_composite_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Mean of quadratic c2 of debt and D/E over 8Q — average convexity across leverage metrics."""
    de = _safe_div(debt, equity)
    return (_quadratic_c2(debt, Y2) + _quadratic_c2(de, Y2)) / 2.0


def f32_lbac_137_structural_break_composite_test_8q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Sum of structural-break scores across debt, D/E, coverage over 8Q windows."""
    sb1 = _structural_break_score(debt, Y2)
    sb2 = _structural_break_score(_safe_div(debt, equity), Y2)
    sb3 = _structural_break_score(-_safe_div(ebit, intexp), Y2)
    return sb1 + sb2 + sb3


def f32_lbac_138_composite_jerk_index_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Mean 4Q absolute 3rd-diff across debt, D/E, coverage."""
    j1 = debt.diff().diff().diff().abs()
    j2 = _safe_div(debt, equity).diff().diff().diff().abs()
    j3 = _safe_div(ebit, intexp).diff().diff().diff().abs()
    return ((j1 + j2 + j3) / 3.0).rolling(Y, min_periods=2).mean()


def f32_lbac_139_cliff_edge_composite_count_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of 4Q with any metric (debt/D-E/coverage) showing |1Q chg z| > 2."""
    z1 = _rolling_zscore(debt.diff(), Y4).abs()
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4).abs()
    z3 = _rolling_zscore(_safe_div(ebit, intexp).diff(), Y4).abs()
    flag = ((z1 > 2.0) | (z2 > 2.0) | (z3 > 2.0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_140_leverage_accel_vs_revenue_accel_spread_4q(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """1Q debt-acceleration minus 1Q revenue-acceleration averaged over 4Q."""
    spread = debt.diff().diff() - revenue.diff().diff()
    return spread.rolling(Y, min_periods=2).mean()


def f32_lbac_141_composite_vs_self_baseline_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """(Current D/E z) - (mean 8Q D/E z) — deviation from short-term self-baseline."""
    r = _safe_div(debt, equity)
    z = _rolling_zscore(r, Y4)
    return z - z.rolling(Y2, min_periods=3).mean()


def f32_lbac_142_accel_regime_change_count_16q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Count of sign changes of D/E 4Q slope inside last 16Q."""
    r = _safe_div(debt, equity)
    sl = _rolling_slope(r, Y)
    flip = (np.sign(sl) != np.sign(sl.shift(1))).astype(float)
    return flip.rolling(Y4, min_periods=6).sum()


def f32_lbac_143_weighted_composite_metric_accel_4q(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Sum 4Q of (0.4*z(d/ebitda chg) + 0.3*z(d/e chg) + 0.3*z(-coverage chg))."""
    z1 = 0.4 * _rolling_zscore(_safe_div(debt, ebitda).diff(), Y4)
    z2 = 0.3 * _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = 0.3 * _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    return (z1 + z2 + z3).rolling(Y, min_periods=2).sum()


def f32_lbac_144_dispersion_accel_metrics_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Std across 4Q-mean z-scores of debt, D/E, -coverage — disagreement among accelerators."""
    z1 = _rolling_zscore(debt.diff(), Y4).rolling(Y, min_periods=2).mean()
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4).rolling(Y, min_periods=2).mean()
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4).rolling(Y, min_periods=2).mean()
    return pd.concat([z1, z2, z3], axis=1).std(axis=1)


def f32_lbac_145_coincidence_index_z2_across_metrics_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of bars in last 4Q where ALL of {debt chg z>2, D/E chg z>2, -coverage chg z>2} hold."""
    z1 = _rolling_zscore(debt.diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    flag = ((z1 > 2.0) & (z2 > 2.0) & (z3 > 2.0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_146_composite_leverage_escalation_4q(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Mean 4Q of (mean of composite-stress z-scores divided by 16Q std of same)."""
    z1 = _rolling_zscore(_safe_div(debt, ebitda).diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    comp = z1 + z2 + z3
    return _safe_div(comp.rolling(Y, min_periods=2).mean(), comp.rolling(Y4, min_periods=6).std())


def f32_lbac_147_terminal_accel_warning_composite_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Sum 4Q of indicator (debt d2>0 AND coverage d2<0 AND cash d2<0) — terminal-state acceleration."""
    f1 = debt.diff().diff() > 0
    f2 = _safe_div(ebit, intexp).diff().diff() < 0
    f3 = cashneq.diff().diff() < 0
    flag = (f1 & f2 & f3).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_148_cliff_edge_probability_8q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Fraction of last 8Q bars where any of debt/D-E/coverage 1Q-chg z > 2."""
    z1 = _rolling_zscore(debt.diff(), Y4).abs()
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4).abs()
    z3 = _rolling_zscore(_safe_div(ebit, intexp).diff(), Y4).abs()
    flag = ((z1 > 2.0) | (z2 > 2.0) | (z3 > 2.0)).astype(float)
    return flag.rolling(Y2, min_periods=3).mean()


def f32_lbac_149_terminal_state_composite_score_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series, fcf: pd.Series) -> pd.Series:
    """Mean 4Q of sum of indicators for {debt up + equity down + coverage down + cash down + fcf down}."""
    cov = _safe_div(ebit, intexp)
    score = (
        (debt.diff() > 0).astype(float)
        + (equity.diff() < 0).astype(float)
        + (cov.diff() < 0).astype(float)
        + (cashneq.diff() < 0).astype(float)
        + (fcf.diff() < 0).astype(float)
    )
    return score.rolling(Y, min_periods=2).mean()


def f32_lbac_150_final_leverage_buildup_accel_composite_8q(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series, cashneq: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Mean over 8Q of: z(d/ebitda chg) + z(d/e chg) + z(-coverage chg) + z(-cash chg) + z(shares chg)."""
    z1 = _rolling_zscore(_safe_div(debt, ebitda).diff(), Y4)
    z2 = _rolling_zscore(_safe_div(debt, equity).diff(), Y4)
    z3 = _rolling_zscore(-_safe_div(ebit, intexp).diff(), Y4)
    z4 = _rolling_zscore(-cashneq.diff(), Y4)
    z5 = _rolling_zscore(shareswa.diff(), Y4)
    return (z1 + z2 + z3 + z4 + z5).rolling(Y2, min_periods=3).mean()


# ============================================================
#                        REGISTRY
# ============================================================

LEVERAGE_BUILDUP_ACCELERATION_BASE_REGISTRY_076_150 = {
    "f32_lbac_076_assets_to_equity_accel_z": {"inputs": ["assets", "equity"], "func": f32_lbac_076_assets_to_equity_accel_z},
    "f32_lbac_077_current_ratio_accel_deterioration_z": {"inputs": ["assets", "debt"], "func": f32_lbac_077_current_ratio_accel_deterioration_z},
    "f32_lbac_078_quick_ratio_accel_z": {"inputs": ["cashneq", "debt"], "func": f32_lbac_078_quick_ratio_accel_z},
    "f32_lbac_079_working_capital_accel_deterioration_z": {"inputs": ["assets", "debt"], "func": f32_lbac_079_working_capital_accel_deterioration_z},
    "f32_lbac_080_wc_to_sales_accel_z": {"inputs": ["assets", "debt", "revenue"], "func": f32_lbac_080_wc_to_sales_accel_z},
    "f32_lbac_081_shares_outstanding_accel_z": {"inputs": ["shareswa"], "func": f32_lbac_081_shares_outstanding_accel_z},
    "f32_lbac_082_equity_accel_deterioration_z": {"inputs": ["equity"], "func": f32_lbac_082_equity_accel_deterioration_z},
    "f32_lbac_083_cash_equiv_accel_deterioration_z": {"inputs": ["cashneq"], "func": f32_lbac_083_cash_equiv_accel_deterioration_z},
    "f32_lbac_084_tangible_book_accel_z": {"inputs": ["equity", "intangibles"], "func": f32_lbac_084_tangible_book_accel_z},
    "f32_lbac_085_assets_to_equity_structural_break_4q_vs_12q": {"inputs": ["assets", "equity"], "func": f32_lbac_085_assets_to_equity_structural_break_4q_vs_12q},
    "f32_lbac_086_cash_inflection_smoothed_raw_sign_flip_8q": {"inputs": ["cashneq"], "func": f32_lbac_086_cash_inflection_smoothed_raw_sign_flip_8q},
    "f32_lbac_087_compound_shares_up_cash_down_4q": {"inputs": ["shareswa", "cashneq"], "func": f32_lbac_087_compound_shares_up_cash_down_4q},
    "f32_lbac_088_compound_liab_up_equity_flat_4q": {"inputs": ["liabilities", "equity"], "func": f32_lbac_088_compound_liab_up_equity_flat_4q},
    "f32_lbac_089_compound_assets_down_debt_up_4q": {"inputs": ["assets", "debt"], "func": f32_lbac_089_compound_assets_down_debt_up_4q},
    "f32_lbac_090_equity_largest_drop_to_8q_std": {"inputs": ["equity"], "func": f32_lbac_090_equity_largest_drop_to_8q_std},
    "f32_lbac_091_quarters_since_equity_neg_accel": {"inputs": ["equity"], "func": f32_lbac_091_quarters_since_equity_neg_accel},
    "f32_lbac_092_wc_to_sales_jerk_z": {"inputs": ["assets", "debt", "revenue"], "func": f32_lbac_092_wc_to_sales_jerk_z},
    "f32_lbac_093_equity_to_liab_accel_deterioration_z": {"inputs": ["equity", "liabilities"], "func": f32_lbac_093_equity_to_liab_accel_deterioration_z},
    "f32_lbac_094_shares_cliff_10pct_jump_count_8q": {"inputs": ["shareswa"], "func": f32_lbac_094_shares_cliff_10pct_jump_count_8q},
    "f32_lbac_095_shares_4q_chg_to_16q_std": {"inputs": ["shareswa"], "func": f32_lbac_095_shares_4q_chg_to_16q_std},
    "f32_lbac_096_equity_erosion_arc_area_8q": {"inputs": ["equity"], "func": f32_lbac_096_equity_erosion_arc_area_8q},
    "f32_lbac_097_dilution_rate_recent_minus_prior_4q": {"inputs": ["shareswa"], "func": f32_lbac_097_dilution_rate_recent_minus_prior_4q},
    "f32_lbac_098_dilution_2sigma_quarter_count_16q": {"inputs": ["shareswa"], "func": f32_lbac_098_dilution_2sigma_quarter_count_16q},
    "f32_lbac_099_composite_bs_accel_deterioration_4q": {"inputs": ["equity", "cashneq", "shareswa"], "func": f32_lbac_099_composite_bs_accel_deterioration_4q},
    "f32_lbac_100_log_shares_slope_4q_minus_12q": {"inputs": ["shareswa"], "func": f32_lbac_100_log_shares_slope_4q_minus_12q},
    "f32_lbac_101_short_debt_share_accel_z": {"inputs": ["debtc", "debtnc"], "func": f32_lbac_101_short_debt_share_accel_z},
    "f32_lbac_102_short_debt_share_cliff_8q": {"inputs": ["debtc", "debtnc"], "func": f32_lbac_102_short_debt_share_cliff_8q},
    "f32_lbac_103_net_debt_chg_to_ebitda_accel_z": {"inputs": ["debt", "cashneq", "ebitda"], "func": f32_lbac_103_net_debt_chg_to_ebitda_accel_z},
    "f32_lbac_104_d2_debt_to_cash_ratio": {"inputs": ["debt", "cashneq"], "func": f32_lbac_104_d2_debt_to_cash_ratio},
    "f32_lbac_105_quarters_since_short_debt_accelerated": {"inputs": ["debtc", "debtnc"], "func": f32_lbac_105_quarters_since_short_debt_accelerated},
    "f32_lbac_106_compound_short_debt_up_cash_down_4q": {"inputs": ["debtc", "cashneq"], "func": f32_lbac_106_compound_short_debt_up_cash_down_4q},
    "f32_lbac_107_short_debt_structural_break_4q_vs_12q": {"inputs": ["debtc"], "func": f32_lbac_107_short_debt_structural_break_4q_vs_12q},
    "f32_lbac_108_short_debt_cumulative_excess_8q": {"inputs": ["debtc"], "func": f32_lbac_108_short_debt_cumulative_excess_8q},
    "f32_lbac_109_debt_composition_entropy_shift_8q": {"inputs": ["debtc", "debtnc"], "func": f32_lbac_109_debt_composition_entropy_shift_8q},
    "f32_lbac_110_log_debt_mix_chg_z_16q": {"inputs": ["debtc", "debtnc"], "func": f32_lbac_110_log_debt_mix_chg_z_16q},
    "f32_lbac_111_debt_rollover_risk_short_debt_to_cash_accel": {"inputs": ["debtc", "cashneq"], "func": f32_lbac_111_debt_rollover_risk_short_debt_to_cash_accel},
    "f32_lbac_112_short_debt_inflection_smoothed_raw_sign_flip_8q": {"inputs": ["debtc"], "func": f32_lbac_112_short_debt_inflection_smoothed_raw_sign_flip_8q},
    "f32_lbac_113_short_debt_recent_4q_minus_prior_4q": {"inputs": ["debtc"], "func": f32_lbac_113_short_debt_recent_4q_minus_prior_4q},
    "f32_lbac_114_short_debt_to_total_latest_to_16q_max": {"inputs": ["debtc", "debtnc"], "func": f32_lbac_114_short_debt_to_total_latest_to_16q_max},
    "f32_lbac_115_short_debt_2sigma_count_16q": {"inputs": ["debtc"], "func": f32_lbac_115_short_debt_2sigma_count_16q},
    "f32_lbac_116_composite_short_debt_accel_stress_4q": {"inputs": ["debtc", "cashneq", "debt"], "func": f32_lbac_116_composite_short_debt_accel_stress_4q},
    "f32_lbac_117_intexp_accel_z_16q": {"inputs": ["intexp"], "func": f32_lbac_117_intexp_accel_z_16q},
    "f32_lbac_118_effective_rate_accel_z": {"inputs": ["intexp", "debt"], "func": f32_lbac_118_effective_rate_accel_z},
    "f32_lbac_119_compound_rate_up_debt_up_4q": {"inputs": ["intexp", "debt"], "func": f32_lbac_119_compound_rate_up_debt_up_4q},
    "f32_lbac_120_quarters_since_rate_accelerated": {"inputs": ["intexp", "debt"], "func": f32_lbac_120_quarters_since_rate_accelerated},
    "f32_lbac_121_debt_service_coverage_accel_deterioration_z": {"inputs": ["ebitda", "intexp", "debtc"], "func": f32_lbac_121_debt_service_coverage_accel_deterioration_z},
    "f32_lbac_122_composite_debt_service_accel_score_4q": {"inputs": ["ebitda", "intexp", "debtc", "fcf"], "func": f32_lbac_122_composite_debt_service_accel_score_4q},
    "f32_lbac_123_debt_growth_to_revenue_growth_accel_z": {"inputs": ["debt", "revenue"], "func": f32_lbac_123_debt_growth_to_revenue_growth_accel_z},
    "f32_lbac_124_d2_debt_to_revenue_ratio": {"inputs": ["debt", "revenue"], "func": f32_lbac_124_d2_debt_to_revenue_ratio},
    "f32_lbac_125_cumulative_excess_debt_growth_over_revenue_4q": {"inputs": ["debt", "revenue"], "func": f32_lbac_125_cumulative_excess_debt_growth_over_revenue_4q},
    "f32_lbac_126_multimetric_accel_coincidence_count_4q": {"inputs": ["debt", "equity", "ebitda", "ebit", "intexp"], "func": f32_lbac_126_multimetric_accel_coincidence_count_4q},
    "f32_lbac_127_compound_all_deteriorating_count_4q": {"inputs": ["debt", "equity", "ebit", "intexp", "cashneq"], "func": f32_lbac_127_compound_all_deteriorating_count_4q},
    "f32_lbac_128_weighted_composite_z_4q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_128_weighted_composite_z_4q},
    "f32_lbac_129_composite_stress_accel_4q": {"inputs": ["debt", "equity", "ebitda", "intexp"], "func": f32_lbac_129_composite_stress_accel_4q},
    "f32_lbac_130_variance_explained_by_accel_8q": {"inputs": ["debt", "equity"], "func": f32_lbac_130_variance_explained_by_accel_8q},
    "f32_lbac_131_multivariate_accel_outlier_z_4q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_131_multivariate_accel_outlier_z_4q},
    "f32_lbac_132_cumulative_stress_accel_index_8q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_132_cumulative_stress_accel_index_8q},
    "f32_lbac_133_compound_deterioration_count_ratio_16q": {"inputs": ["debt", "equity", "ebit", "intexp", "cashneq"], "func": f32_lbac_133_compound_deterioration_count_ratio_16q},
    "f32_lbac_134_acceleration_phase_indicator_8q": {"inputs": ["debt", "equity"], "func": f32_lbac_134_acceleration_phase_indicator_8q},
    "f32_lbac_135_inflection_composite_4q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_135_inflection_composite_4q},
    "f32_lbac_136_quadratic_fit_composite_8q": {"inputs": ["debt", "equity"], "func": f32_lbac_136_quadratic_fit_composite_8q},
    "f32_lbac_137_structural_break_composite_test_8q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_137_structural_break_composite_test_8q},
    "f32_lbac_138_composite_jerk_index_4q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_138_composite_jerk_index_4q},
    "f32_lbac_139_cliff_edge_composite_count_4q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_139_cliff_edge_composite_count_4q},
    "f32_lbac_140_leverage_accel_vs_revenue_accel_spread_4q": {"inputs": ["debt", "revenue"], "func": f32_lbac_140_leverage_accel_vs_revenue_accel_spread_4q},
    "f32_lbac_141_composite_vs_self_baseline_8q": {"inputs": ["debt", "equity"], "func": f32_lbac_141_composite_vs_self_baseline_8q},
    "f32_lbac_142_accel_regime_change_count_16q": {"inputs": ["debt", "equity"], "func": f32_lbac_142_accel_regime_change_count_16q},
    "f32_lbac_143_weighted_composite_metric_accel_4q": {"inputs": ["debt", "equity", "ebitda", "ebit", "intexp", "cashneq"], "func": f32_lbac_143_weighted_composite_metric_accel_4q},
    "f32_lbac_144_dispersion_accel_metrics_4q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_144_dispersion_accel_metrics_4q},
    "f32_lbac_145_coincidence_index_z2_across_metrics_4q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_145_coincidence_index_z2_across_metrics_4q},
    "f32_lbac_146_composite_leverage_escalation_4q": {"inputs": ["debt", "equity", "ebitda", "ebit", "intexp"], "func": f32_lbac_146_composite_leverage_escalation_4q},
    "f32_lbac_147_terminal_accel_warning_composite_4q": {"inputs": ["debt", "equity", "ebit", "intexp", "cashneq"], "func": f32_lbac_147_terminal_accel_warning_composite_4q},
    "f32_lbac_148_cliff_edge_probability_8q": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_148_cliff_edge_probability_8q},
    "f32_lbac_149_terminal_state_composite_score_4q": {"inputs": ["debt", "equity", "ebit", "intexp", "cashneq", "fcf"], "func": f32_lbac_149_terminal_state_composite_score_4q},
    "f32_lbac_150_final_leverage_buildup_accel_composite_8q": {"inputs": ["debt", "equity", "ebitda", "ebit", "intexp", "cashneq", "shareswa"], "func": f32_lbac_150_final_leverage_buildup_accel_composite_8q},
}
