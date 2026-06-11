"""leverage_buildup_acceleration base features 001-075 — Pipeline 1a-inverse short-side blowup family.

Per HANDOFF §6 (families 29-36 special rule): base features are PATTERN-DETECTION
HYPOTHESES about acceleration dynamics of leverage buildup — NOT raw 2nd/3rd
derivatives. Detectors include: cliff-edge events, inflection-point classifiers,
structural-break tests, acceleration-vs-baseline z-scores, compound-deterioration
co-occurrence, sign-flip detectors. Distinct from trajectory family 24
(debt_buildup_trajectory).

Inputs: SF1 quarterly (debt, debtc, debtnc, equity, assets, ebitda, ebit, fcf,
ncfo, intexp, cashneq, revenue). Quarterly cadence: window units are quarters.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
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
    """Slope-of-recent-n minus slope-of-prior-n (sign of structural break in trend)."""
    return _rolling_slope(s, n) - _rolling_slope(s.shift(n), n)


def _accel(s, n):
    """Acceleration: n-period diff of (n-period diff)."""
    return s.diff(n).diff(n)


def _jerk(s, n):
    """Jerk: n-period diff of n-period diff of n-period diff."""
    return s.diff(n).diff(n).diff(n)


# ============================================================
#                  FEATURES 001-075
# ============================================================

def f32_lbac_001_debt_cliff_jump_vs_8q_std(debt: pd.Series) -> pd.Series:
    """Cliff-edge detector: latest 1Q debt jump / 8Q std of debt changes."""
    chg = debt.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return chg / sd.replace(0, np.nan)


def f32_lbac_002_debt_1q_chg_vs_mean_4q_chg(debt: pd.Series) -> pd.Series:
    """Latest 1Q debt change / mean 4Q debt change — cliff-edge ratio."""
    chg = debt.diff()
    m = chg.rolling(Y, min_periods=2).mean()
    return _safe_div(chg, m.abs())


def f32_lbac_003_debt_structural_break_8q_vs_8q(debt: pd.Series) -> pd.Series:
    """Slope of debt over recent 8Q minus slope over prior 8Q — structural break magnitude."""
    return _structural_break_score(debt, Y2)


def f32_lbac_004_debt_inflection_smoothed_vs_raw_sign_flip(debt: pd.Series) -> pd.Series:
    """Count of sign flips of (raw debt slope 4Q - EMA-smoothed slope) in 8Q — inflection probability."""
    sl = _rolling_slope(debt, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f32_lbac_005_compound_debt_up_cash_down_4q(debt: pd.Series, cashneq: pd.Series) -> pd.Series:
    """Count of 4Q windows where both debt rose AND cash declined."""
    co = ((debt.diff() > 0) & (cashneq.diff() < 0)).astype(float)
    return co.rolling(Y, min_periods=2).sum()


def f32_lbac_006_debt_growth_zscore_16q(debt: pd.Series) -> pd.Series:
    """Z-score of 1Q debt change over 16Q distribution."""
    return _rolling_zscore(debt.diff(), Y4)


def f32_lbac_007_debt_4q_chg_vs_16q_std(debt: pd.Series) -> pd.Series:
    """4Q debt change / 16Q std of 4Q changes."""
    chg4 = debt.diff(Y)
    sd = chg4.rolling(Y4, min_periods=6).std()
    return chg4 / sd.replace(0, np.nan)


def f32_lbac_008_debt_jerk_zscore_16q(debt: pd.Series) -> pd.Series:
    """Z-score of 1Q jerk of log debt over 16Q."""
    j = _jerk(_safe_log(debt), Q)
    return _rolling_zscore(j, Y4)


def f32_lbac_009_debt_cumulative_excess_above_8q_linear(debt: pd.Series) -> pd.Series:
    """Cumulative excess of debt above its 8Q linear fit — bulging buildup."""
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return debt.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f32_lbac_010_debt_quadratic_curvature_8q(debt: pd.Series) -> pd.Series:
    """Quadratic c2 of debt polyfit over 8Q — convex acceleration when positive."""
    return _quadratic_c2(debt, Y2)


def f32_lbac_011_debt_inflection_count_d2_positive_8q(debt: pd.Series) -> pd.Series:
    """Count of bars in 8Q where 2nd diff of debt is positive — inflection probability."""
    d2 = debt.diff().diff()
    flag = (d2 > 0).astype(float)
    return flag.rolling(Y2, min_periods=3).sum()


def f32_lbac_012_debt_exp_fit_r2_8q(debt: pd.Series) -> pd.Series:
    """R² of log-debt linear fit over 8Q — exponential-growth signature."""
    ld = _safe_log(debt)
    def _r2(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        ss_res = ((w - pred) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return ld.rolling(Y2, min_periods=4).apply(_r2, raw=True)


def f32_lbac_013_debt_slope_acceleration_4q_minus_12q(debt: pd.Series) -> pd.Series:
    """4Q debt slope minus 12Q debt slope — recent vs trailing trend speedup."""
    return _rolling_slope(debt, Y) - _rolling_slope(debt, Y3)


def f32_lbac_014_log_debt_x2_regression_r2(debt: pd.Series) -> pd.Series:
    """R² of quadratic fit of log-debt over 8Q — non-linear acceleration goodness."""
    ld = _safe_log(debt)
    def _r2q(w):
        if np.isnan(w).any() or len(w) < 4:
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        coef = np.polyfit(x, w, 2)
        pred = np.polyval(coef, x)
        ss_res = ((w - pred) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return ld.rolling(Y2, min_periods=4).apply(_r2q, raw=True)


def f32_lbac_015_debt_accel_baseline_z_1q_vs_12q(debt: pd.Series) -> pd.Series:
    """1Q debt change z-scored vs 12Q distribution of 1Q changes."""
    chg = debt.diff()
    return _rolling_zscore(chg, Y3)


def f32_lbac_016_compound_debt_up_assets_flat_4q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Count of 4Q with debt rising while assets are flat (|chg|/assets<0.01)."""
    flat = (assets.diff().abs() / assets.replace(0, np.nan)) < 0.01
    flag = ((debt.diff() > 0) & flat).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_017_compound_debt_up_revenue_flat_4q(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Count of 4Q with debt rising while revenue is flat — debt without growth."""
    flat = (revenue.diff().abs() / revenue.replace(0, np.nan)) < 0.01
    flag = ((debt.diff() > 0) & flat).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_018_compound_debt_up_ebitda_down_4q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Count of 4Q with debt rising AND ebitda falling — leverage with deterioration."""
    flag = ((debt.diff() > 0) & (ebitda.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_019_ratio_largest_debt_jump_to_mean_jump_8q(debt: pd.Series) -> pd.Series:
    """Max(|1Q debt chg| over 8Q) / mean(|1Q debt chg| over 8Q)."""
    chg = debt.diff().abs()
    return _safe_div(chg.rolling(Y2, min_periods=3).max(), chg.rolling(Y2, min_periods=3).mean())


def f32_lbac_020_quarters_since_debt_last_accelerated(debt: pd.Series) -> pd.Series:
    """Quarters since the last time debt acceleration (1Q d2) crossed above zero."""
    d2 = debt.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f32_lbac_021_debt_recent_4q_minus_prior_4q_avg_chg(debt: pd.Series) -> pd.Series:
    """Mean 1Q debt change in last 4Q minus mean in prior 4Q."""
    chg = debt.diff()
    a = chg.rolling(Y, min_periods=2).mean()
    b = chg.shift(Y).rolling(Y, min_periods=2).mean()
    return a - b


def f32_lbac_022_log_debt_cumulative_minus_linear_8q(debt: pd.Series) -> pd.Series:
    """Sum of (log debt - 8Q linear fit) over 8Q — concavity vs linear baseline."""
    ld = _safe_log(debt)
    def _ex(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        return float((w - (c1 * x + c0)).sum())
    return ld.rolling(Y2, min_periods=4).apply(_ex, raw=True)


def f32_lbac_023_debt_arc_area_above_8q_linear(debt: pd.Series) -> pd.Series:
    """Sum of positive log-debt residuals above 8Q linear fit — bulge integral."""
    ld = _safe_log(debt)
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return ld.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f32_lbac_024_debt_cliff_count_2sigma_16q(debt: pd.Series) -> pd.Series:
    """Count of 1Q debt changes with z>2 (vs 16Q dist) inside last 16Q."""
    z = _rolling_zscore(debt.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f32_lbac_025_debt_growth_cv_8q(debt: pd.Series) -> pd.Series:
    """CV of 1Q debt-change series over 8Q (dispersion of growth pulses)."""
    chg = debt.diff()
    return _safe_div(chg.rolling(Y2, min_periods=3).std(), chg.rolling(Y2, min_periods=3).mean().abs())


def f32_lbac_026_debt_to_equity_accel_z_16q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in D/E over 16Q."""
    de = _safe_div(debt, equity)
    return _rolling_zscore(de.diff(), Y4)


def f32_lbac_027_debt_to_equity_cliff_jump_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1Q D/E jump / 8Q std of D/E changes — cliff detector."""
    de = _safe_div(debt, equity)
    chg = de.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return chg / sd.replace(0, np.nan)


def f32_lbac_028_debt_to_equity_structural_break_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E recent-8Q slope minus prior-8Q slope."""
    de = _safe_div(debt, equity)
    return _structural_break_score(de, Y2)


def f32_lbac_029_debt_to_assets_accel_z_16q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in D/A over 16Q."""
    da = _safe_div(debt, assets)
    return _rolling_zscore(da.diff(), Y4)


def f32_lbac_030_debt_to_assets_cliff_8q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """1Q D/A jump / 8Q std of D/A changes."""
    da = _safe_div(debt, assets)
    chg = da.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return chg / sd.replace(0, np.nan)


def f32_lbac_031_debt_to_ebitda_accel_z_16q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in debt/ebitda over 16Q."""
    de = _safe_div(debt, ebitda)
    return _rolling_zscore(de.diff(), Y4)


def f32_lbac_032_net_debt_to_ebitda_accel_z_16q(debt: pd.Series, cashneq: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in (debt-cash)/ebitda over 16Q."""
    nd = _safe_div(debt - cashneq, ebitda)
    return _rolling_zscore(nd.diff(), Y4)


def f32_lbac_033_interest_coverage_accel_deterioration_z_16q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in ebit/intexp — positive = deteriorating coverage."""
    cov = _safe_div(ebit, intexp)
    return _rolling_zscore(-cov.diff(), Y4)


def f32_lbac_034_interest_coverage_cliff_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """1Q drop in coverage / 8Q std of coverage changes — cliff in interest coverage."""
    cov = _safe_div(ebit, intexp)
    chg = cov.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return -chg / sd.replace(0, np.nan)


def f32_lbac_035_fixed_charge_coverage_accel_z(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in ebitda/intexp over 16Q — fixed-charge coverage deterioration."""
    cov = _safe_div(ebitda, intexp)
    return _rolling_zscore(-cov.diff(), Y4)


def f32_lbac_036_de_inflection_smoothed_raw_sign_flip_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Sign-flip count of D/E slope minus its EMA-smoothed slope, over 8Q."""
    de = _safe_div(debt, equity)
    sl = _rolling_slope(de, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f32_lbac_037_de_exp_fit_r2_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """R² of linear fit of log(D/E) over 4Q — exponential rise in leverage signature."""
    lde = _safe_log(_safe_div(debt, equity))
    def _r2(w):
        if np.isnan(w).any() or len(w) < 3:
            return np.nan
        x = np.arange(len(w))
        ss_tot = ((w - w.mean()) ** 2).sum()
        if ss_tot == 0:
            return np.nan
        c1, c0 = np.polyfit(x, w, 1)
        pred = c1 * x + c0
        ss_res = ((w - pred) ** 2).sum()
        return 1.0 - ss_res / ss_tot
    return lde.rolling(Y, min_periods=3).apply(_r2, raw=True)


def f32_lbac_038_da_structural_break_4q_vs_12q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """D/A 4Q slope minus 12Q slope — speedup of leverage as fraction of assets."""
    da = _safe_div(debt, assets)
    return _rolling_slope(da, Y) - _rolling_slope(da, Y3)


def f32_lbac_039_compound_de_up_ebit_down_4q(debt: pd.Series, equity: pd.Series, ebit: pd.Series) -> pd.Series:
    """Count of 4Q with D/E rising AND ebit falling."""
    de = _safe_div(debt, equity)
    flag = ((de.diff() > 0) & (ebit.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_040_compound_de_up_fcf_down_4q(debt: pd.Series, equity: pd.Series, fcf: pd.Series) -> pd.Series:
    """Count of 4Q with D/E rising AND fcf falling — leverage with cash drain."""
    de = _safe_div(debt, equity)
    flag = ((de.diff() > 0) & (fcf.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_041_debt_to_ebitda_latest_to_8q_max(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Current debt/ebitda / 8Q max — proximity to recent leverage peak."""
    r = _safe_div(debt, ebitda)
    return _safe_div(r, r.rolling(Y2, min_periods=3).max())


def f32_lbac_042_quarters_since_debt_ebitda_accelerated(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Quarters since debt/ebitda d2 crossed above zero."""
    r = _safe_div(debt, ebitda)
    d2 = r.diff().diff()
    flag = (d2 > 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f32_lbac_043_debt_ebitda_zscore_8q_cumulative(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Cumulative z-score of debt/ebitda over last 8Q (vs 16Q dist) — sustained elevation."""
    r = _safe_div(debt, ebitda)
    z = _rolling_zscore(r, Y4)
    return z.rolling(Y2, min_periods=3).sum()


def f32_lbac_044_de_arc_area_above_8q_linear(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Arc area of D/E above its 8Q linear fit."""
    r = _safe_div(debt, equity)
    def _arc(w):
        if np.isnan(w).any():
            return np.nan
        x = np.arange(len(w))
        c1, c0 = np.polyfit(x, w, 1)
        resid = w - (c1 * x + c0)
        return float(np.clip(resid, 0, None).sum())
    return r.rolling(Y2, min_periods=4).apply(_arc, raw=True)


def f32_lbac_045_de_2sigma_jump_count_16q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Count of D/E 1Q changes with z>2 over 16Q."""
    r = _safe_div(debt, equity)
    z = _rolling_zscore(r.diff(), Y4)
    flag = (z > 2.0).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f32_lbac_046_log_de_slope_4q_minus_12q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Log(D/E) 4Q slope minus 12Q slope — log-space speedup."""
    lde = _safe_log(_safe_div(debt, equity))
    return _rolling_slope(lde, Y) - _rolling_slope(lde, Y3)


def f32_lbac_047_de_4q_chg_to_de_level_ratio(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """(4Q D/E change) / current D/E — relative growth magnitude."""
    r = _safe_div(debt, equity)
    return _safe_div(r.diff(Y), r.abs())


def f32_lbac_048_d2_log_de_zscore_16q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of 2nd diff of log(D/E) over 16Q."""
    lde = _safe_log(_safe_div(debt, equity))
    return _rolling_zscore(lde.diff().diff(), Y4)


def f32_lbac_049_debt_ebitda_tail_event_count_4q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Count of last 4Q with debt/ebitda exceeding 99th-pct of 16Q distribution."""
    r = _safe_div(debt, ebitda)
    p = r.rolling(Y4, min_periods=6).quantile(0.99)
    flag = (r >= p).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_050_composite_leverage_stress_accel_4q(debt: pd.Series, equity: pd.Series, ebitda: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Mean over 4Q of: z(D/E chg) + z(D/EBITDA chg) + z(-coverage chg)."""
    de = _safe_div(debt, equity)
    dE = _safe_div(debt, ebitda)
    cov = _safe_div(ebit, intexp)
    score = _rolling_zscore(de.diff(), Y4) + _rolling_zscore(dE.diff(), Y4) + _rolling_zscore(-cov.diff(), Y4)
    return score.rolling(Y, min_periods=2).mean()


def f32_lbac_051_coverage_slope_4q_minus_12q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Interest coverage 4Q slope minus 12Q slope — coverage trend speedup (negative = worsening fast)."""
    cov = _safe_div(ebit, intexp)
    return _rolling_slope(cov, Y) - _rolling_slope(cov, Y3)


def f32_lbac_052_coverage_cliff_50pct_drop_count_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of 8Q windows where coverage dropped >50pct vs prior quarter."""
    cov = _safe_div(ebit, intexp)
    flag = (cov / cov.shift(1).replace(0, np.nan) < 0.5).astype(float)
    return flag.rolling(Y2, min_periods=3).sum()


def f32_lbac_053_coverage_chg_zscore_16q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of 1Q coverage change over 16Q."""
    cov = _safe_div(ebit, intexp)
    return _rolling_zscore(cov.diff(), Y4)


def f32_lbac_054_ebit_intexp_jerk(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """3rd diff of ebit/intexp — jerk in coverage trajectory."""
    cov = _safe_div(ebit, intexp)
    return cov.diff().diff().diff()


def f32_lbac_055_ebitda_intexp_accel_z(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of 2nd diff of ebitda/intexp over 16Q."""
    cov = _safe_div(ebitda, intexp)
    return _rolling_zscore(cov.diff().diff(), Y4)


def f32_lbac_056_fcf_to_debt_accel_deterioration_z(fcf: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in fcf/debt over 16Q — positive = deteriorating debt-paying-capacity."""
    r = _safe_div(fcf, debt)
    return _rolling_zscore(-r.diff(), Y4)


def f32_lbac_057_fcf_to_debt_cliff_8q(fcf: pd.Series, debt: pd.Series) -> pd.Series:
    """1Q drop in fcf/debt / 8Q std of changes."""
    r = _safe_div(fcf, debt)
    chg = r.diff()
    sd = chg.rolling(Y2, min_periods=3).std()
    return -chg / sd.replace(0, np.nan)


def f32_lbac_058_ocf_to_debt_accel_z(ncfo: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in operating-cash-flow/debt over 16Q."""
    r = _safe_div(ncfo, debt)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_059_cash_to_debt_accel_z(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of 1Q chg in cash/debt — liquidity-to-debt acceleration."""
    r = _safe_div(cashneq, debt)
    return _rolling_zscore(r.diff(), Y4)


def f32_lbac_060_coverage_inflection_smoothed_raw_sign_flip_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Sign-flip count of coverage slope vs its EMA-smoothed slope, over 8Q."""
    cov = _safe_div(ebit, intexp)
    sl = _rolling_slope(cov, Y)
    sm = sl.ewm(span=4, adjust=False, min_periods=2).mean()
    flip = (np.sign(sl - sm) != np.sign((sl - sm).shift(1))).astype(float)
    return flip.rolling(Y2, min_periods=3).sum()


def f32_lbac_061_compound_coverage_down_debt_up_4q(ebit: pd.Series, intexp: pd.Series, debt: pd.Series) -> pd.Series:
    """Count 4Q with coverage falling AND debt rising — compound deterioration."""
    cov = _safe_div(ebit, intexp)
    flag = ((cov.diff() < 0) & (debt.diff() > 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_062_compound_coverage_down_revenue_down_4q(ebit: pd.Series, intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Count 4Q with coverage falling AND revenue falling — operational + financial stress."""
    cov = _safe_div(ebit, intexp)
    flag = ((cov.diff() < 0) & (revenue.diff() < 0)).astype(float)
    return flag.rolling(Y, min_periods=2).sum()


def f32_lbac_063_quarters_since_coverage_worsened(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Quarters since interest coverage last had a negative change."""
    cov = _safe_div(ebit, intexp)
    flag = (cov.diff() < 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f32_lbac_064_fcf_intexp_accel_deterioration_z(fcf: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of -1Q chg in fcf/intexp over 16Q."""
    r = _safe_div(fcf, intexp)
    return _rolling_zscore(-r.diff(), Y4)


def f32_lbac_065_coverage_cumulative_excess_deterioration_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Sum of negative coverage 1Q changes over 8Q — cumulative loss in coverage."""
    cov = _safe_div(ebit, intexp)
    chg = cov.diff()
    return chg.where(chg < 0, 0).rolling(Y2, min_periods=3).sum()


def f32_lbac_066_coverage_quadratic_c2_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Quadratic c2 of coverage over 8Q — concave decline signature when negative."""
    cov = _safe_div(ebit, intexp)
    return _quadratic_c2(cov, Y2)


def f32_lbac_067_coverage_structural_break_4q_vs_16q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Coverage 4Q slope minus 16Q slope — short-horizon trend speedup."""
    cov = _safe_div(ebit, intexp)
    return _rolling_slope(cov, Y) - _rolling_slope(cov, Y4)


def f32_lbac_068_coverage_latest_to_16q_max_ratio(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Current coverage / 16Q max — distance from recent best."""
    cov = _safe_div(ebit, intexp)
    return _safe_div(cov, cov.rolling(Y4, min_periods=6).max())


def f32_lbac_069_log_coverage_slope_4q_minus_12q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Log-coverage 4Q slope minus 12Q slope — log-space speedup."""
    lc = _safe_log(_safe_div(ebit, intexp))
    return _rolling_slope(lc, Y) - _rolling_slope(lc, Y3)


def f32_lbac_070_coverage_below_2x_fraction_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Fraction of last 8Q with coverage <2x — distressed-coverage regime."""
    cov = _safe_div(ebit, intexp)
    flag = (cov < 2.0).astype(float)
    return flag.rolling(Y2, min_periods=3).mean()


def f32_lbac_071_coverage_below_1x_fraction_8q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Fraction of last 8Q with coverage <1x — interest-impair regime."""
    cov = _safe_div(ebit, intexp)
    flag = (cov < 1.0).astype(float)
    return flag.rolling(Y2, min_periods=3).mean()


def f32_lbac_072_quarters_since_coverage_neg_accel(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Quarters since coverage d2 last crossed below zero."""
    cov = _safe_div(ebit, intexp)
    d2 = cov.diff().diff()
    flag = (d2 < 0).astype(float)
    last = pd.Series(np.where(flag > 0, np.arange(len(flag)), np.nan), index=flag.index).ffill()
    return pd.Series(np.arange(len(flag)), index=flag.index) - last


def f32_lbac_073_coverage_tail_event_count_16q(ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Count of coverage values below 5th-pct of 16Q distribution in last 16Q."""
    cov = _safe_div(ebit, intexp)
    p = cov.rolling(Y4, min_periods=6).quantile(0.05)
    flag = (cov <= p).astype(float)
    return flag.rolling(Y4, min_periods=6).sum()


def f32_lbac_074_composite_coverage_deterioration_accel_4q(ebit: pd.Series, ebitda: pd.Series, intexp: pd.Series, fcf: pd.Series) -> pd.Series:
    """Mean 4Q of -z(coverage chg) + -z(ebitda/intexp chg) + -z(fcf/intexp chg)."""
    c1 = _rolling_zscore(_safe_div(ebit, intexp).diff(), Y4)
    c2 = _rolling_zscore(_safe_div(ebitda, intexp).diff(), Y4)
    c3 = _rolling_zscore(_safe_div(fcf, intexp).diff(), Y4)
    return (-c1 - c2 - c3).rolling(Y, min_periods=2).mean()


def f32_lbac_075_composite_leverage_coverage_accel_combo_z(debt: pd.Series, equity: pd.Series, ebit: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z(D/E chg) + Z(-coverage chg) — combined leverage & coverage acceleration."""
    de = _safe_div(debt, equity)
    cov = _safe_div(ebit, intexp)
    return _rolling_zscore(de.diff(), Y4) + _rolling_zscore(-cov.diff(), Y4)


# ============================================================
#                        REGISTRY
# ============================================================

LEVERAGE_BUILDUP_ACCELERATION_BASE_REGISTRY_001_075 = {
    "f32_lbac_001_debt_cliff_jump_vs_8q_std": {"inputs": ["debt"], "func": f32_lbac_001_debt_cliff_jump_vs_8q_std},
    "f32_lbac_002_debt_1q_chg_vs_mean_4q_chg": {"inputs": ["debt"], "func": f32_lbac_002_debt_1q_chg_vs_mean_4q_chg},
    "f32_lbac_003_debt_structural_break_8q_vs_8q": {"inputs": ["debt"], "func": f32_lbac_003_debt_structural_break_8q_vs_8q},
    "f32_lbac_004_debt_inflection_smoothed_vs_raw_sign_flip": {"inputs": ["debt"], "func": f32_lbac_004_debt_inflection_smoothed_vs_raw_sign_flip},
    "f32_lbac_005_compound_debt_up_cash_down_4q": {"inputs": ["debt", "cashneq"], "func": f32_lbac_005_compound_debt_up_cash_down_4q},
    "f32_lbac_006_debt_growth_zscore_16q": {"inputs": ["debt"], "func": f32_lbac_006_debt_growth_zscore_16q},
    "f32_lbac_007_debt_4q_chg_vs_16q_std": {"inputs": ["debt"], "func": f32_lbac_007_debt_4q_chg_vs_16q_std},
    "f32_lbac_008_debt_jerk_zscore_16q": {"inputs": ["debt"], "func": f32_lbac_008_debt_jerk_zscore_16q},
    "f32_lbac_009_debt_cumulative_excess_above_8q_linear": {"inputs": ["debt"], "func": f32_lbac_009_debt_cumulative_excess_above_8q_linear},
    "f32_lbac_010_debt_quadratic_curvature_8q": {"inputs": ["debt"], "func": f32_lbac_010_debt_quadratic_curvature_8q},
    "f32_lbac_011_debt_inflection_count_d2_positive_8q": {"inputs": ["debt"], "func": f32_lbac_011_debt_inflection_count_d2_positive_8q},
    "f32_lbac_012_debt_exp_fit_r2_8q": {"inputs": ["debt"], "func": f32_lbac_012_debt_exp_fit_r2_8q},
    "f32_lbac_013_debt_slope_acceleration_4q_minus_12q": {"inputs": ["debt"], "func": f32_lbac_013_debt_slope_acceleration_4q_minus_12q},
    "f32_lbac_014_log_debt_x2_regression_r2": {"inputs": ["debt"], "func": f32_lbac_014_log_debt_x2_regression_r2},
    "f32_lbac_015_debt_accel_baseline_z_1q_vs_12q": {"inputs": ["debt"], "func": f32_lbac_015_debt_accel_baseline_z_1q_vs_12q},
    "f32_lbac_016_compound_debt_up_assets_flat_4q": {"inputs": ["debt", "assets"], "func": f32_lbac_016_compound_debt_up_assets_flat_4q},
    "f32_lbac_017_compound_debt_up_revenue_flat_4q": {"inputs": ["debt", "revenue"], "func": f32_lbac_017_compound_debt_up_revenue_flat_4q},
    "f32_lbac_018_compound_debt_up_ebitda_down_4q": {"inputs": ["debt", "ebitda"], "func": f32_lbac_018_compound_debt_up_ebitda_down_4q},
    "f32_lbac_019_ratio_largest_debt_jump_to_mean_jump_8q": {"inputs": ["debt"], "func": f32_lbac_019_ratio_largest_debt_jump_to_mean_jump_8q},
    "f32_lbac_020_quarters_since_debt_last_accelerated": {"inputs": ["debt"], "func": f32_lbac_020_quarters_since_debt_last_accelerated},
    "f32_lbac_021_debt_recent_4q_minus_prior_4q_avg_chg": {"inputs": ["debt"], "func": f32_lbac_021_debt_recent_4q_minus_prior_4q_avg_chg},
    "f32_lbac_022_log_debt_cumulative_minus_linear_8q": {"inputs": ["debt"], "func": f32_lbac_022_log_debt_cumulative_minus_linear_8q},
    "f32_lbac_023_debt_arc_area_above_8q_linear": {"inputs": ["debt"], "func": f32_lbac_023_debt_arc_area_above_8q_linear},
    "f32_lbac_024_debt_cliff_count_2sigma_16q": {"inputs": ["debt"], "func": f32_lbac_024_debt_cliff_count_2sigma_16q},
    "f32_lbac_025_debt_growth_cv_8q": {"inputs": ["debt"], "func": f32_lbac_025_debt_growth_cv_8q},
    "f32_lbac_026_debt_to_equity_accel_z_16q": {"inputs": ["debt", "equity"], "func": f32_lbac_026_debt_to_equity_accel_z_16q},
    "f32_lbac_027_debt_to_equity_cliff_jump_8q": {"inputs": ["debt", "equity"], "func": f32_lbac_027_debt_to_equity_cliff_jump_8q},
    "f32_lbac_028_debt_to_equity_structural_break_8q": {"inputs": ["debt", "equity"], "func": f32_lbac_028_debt_to_equity_structural_break_8q},
    "f32_lbac_029_debt_to_assets_accel_z_16q": {"inputs": ["debt", "assets"], "func": f32_lbac_029_debt_to_assets_accel_z_16q},
    "f32_lbac_030_debt_to_assets_cliff_8q": {"inputs": ["debt", "assets"], "func": f32_lbac_030_debt_to_assets_cliff_8q},
    "f32_lbac_031_debt_to_ebitda_accel_z_16q": {"inputs": ["debt", "ebitda"], "func": f32_lbac_031_debt_to_ebitda_accel_z_16q},
    "f32_lbac_032_net_debt_to_ebitda_accel_z_16q": {"inputs": ["debt", "cashneq", "ebitda"], "func": f32_lbac_032_net_debt_to_ebitda_accel_z_16q},
    "f32_lbac_033_interest_coverage_accel_deterioration_z_16q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_033_interest_coverage_accel_deterioration_z_16q},
    "f32_lbac_034_interest_coverage_cliff_8q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_034_interest_coverage_cliff_8q},
    "f32_lbac_035_fixed_charge_coverage_accel_z": {"inputs": ["ebitda", "intexp"], "func": f32_lbac_035_fixed_charge_coverage_accel_z},
    "f32_lbac_036_de_inflection_smoothed_raw_sign_flip_8q": {"inputs": ["debt", "equity"], "func": f32_lbac_036_de_inflection_smoothed_raw_sign_flip_8q},
    "f32_lbac_037_de_exp_fit_r2_4q": {"inputs": ["debt", "equity"], "func": f32_lbac_037_de_exp_fit_r2_4q},
    "f32_lbac_038_da_structural_break_4q_vs_12q": {"inputs": ["debt", "assets"], "func": f32_lbac_038_da_structural_break_4q_vs_12q},
    "f32_lbac_039_compound_de_up_ebit_down_4q": {"inputs": ["debt", "equity", "ebit"], "func": f32_lbac_039_compound_de_up_ebit_down_4q},
    "f32_lbac_040_compound_de_up_fcf_down_4q": {"inputs": ["debt", "equity", "fcf"], "func": f32_lbac_040_compound_de_up_fcf_down_4q},
    "f32_lbac_041_debt_to_ebitda_latest_to_8q_max": {"inputs": ["debt", "ebitda"], "func": f32_lbac_041_debt_to_ebitda_latest_to_8q_max},
    "f32_lbac_042_quarters_since_debt_ebitda_accelerated": {"inputs": ["debt", "ebitda"], "func": f32_lbac_042_quarters_since_debt_ebitda_accelerated},
    "f32_lbac_043_debt_ebitda_zscore_8q_cumulative": {"inputs": ["debt", "ebitda"], "func": f32_lbac_043_debt_ebitda_zscore_8q_cumulative},
    "f32_lbac_044_de_arc_area_above_8q_linear": {"inputs": ["debt", "equity"], "func": f32_lbac_044_de_arc_area_above_8q_linear},
    "f32_lbac_045_de_2sigma_jump_count_16q": {"inputs": ["debt", "equity"], "func": f32_lbac_045_de_2sigma_jump_count_16q},
    "f32_lbac_046_log_de_slope_4q_minus_12q": {"inputs": ["debt", "equity"], "func": f32_lbac_046_log_de_slope_4q_minus_12q},
    "f32_lbac_047_de_4q_chg_to_de_level_ratio": {"inputs": ["debt", "equity"], "func": f32_lbac_047_de_4q_chg_to_de_level_ratio},
    "f32_lbac_048_d2_log_de_zscore_16q": {"inputs": ["debt", "equity"], "func": f32_lbac_048_d2_log_de_zscore_16q},
    "f32_lbac_049_debt_ebitda_tail_event_count_4q": {"inputs": ["debt", "ebitda"], "func": f32_lbac_049_debt_ebitda_tail_event_count_4q},
    "f32_lbac_050_composite_leverage_stress_accel_4q": {"inputs": ["debt", "equity", "ebitda", "ebit", "intexp"], "func": f32_lbac_050_composite_leverage_stress_accel_4q},
    "f32_lbac_051_coverage_slope_4q_minus_12q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_051_coverage_slope_4q_minus_12q},
    "f32_lbac_052_coverage_cliff_50pct_drop_count_8q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_052_coverage_cliff_50pct_drop_count_8q},
    "f32_lbac_053_coverage_chg_zscore_16q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_053_coverage_chg_zscore_16q},
    "f32_lbac_054_ebit_intexp_jerk": {"inputs": ["ebit", "intexp"], "func": f32_lbac_054_ebit_intexp_jerk},
    "f32_lbac_055_ebitda_intexp_accel_z": {"inputs": ["ebitda", "intexp"], "func": f32_lbac_055_ebitda_intexp_accel_z},
    "f32_lbac_056_fcf_to_debt_accel_deterioration_z": {"inputs": ["fcf", "debt"], "func": f32_lbac_056_fcf_to_debt_accel_deterioration_z},
    "f32_lbac_057_fcf_to_debt_cliff_8q": {"inputs": ["fcf", "debt"], "func": f32_lbac_057_fcf_to_debt_cliff_8q},
    "f32_lbac_058_ocf_to_debt_accel_z": {"inputs": ["ncfo", "debt"], "func": f32_lbac_058_ocf_to_debt_accel_z},
    "f32_lbac_059_cash_to_debt_accel_z": {"inputs": ["cashneq", "debt"], "func": f32_lbac_059_cash_to_debt_accel_z},
    "f32_lbac_060_coverage_inflection_smoothed_raw_sign_flip_8q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_060_coverage_inflection_smoothed_raw_sign_flip_8q},
    "f32_lbac_061_compound_coverage_down_debt_up_4q": {"inputs": ["ebit", "intexp", "debt"], "func": f32_lbac_061_compound_coverage_down_debt_up_4q},
    "f32_lbac_062_compound_coverage_down_revenue_down_4q": {"inputs": ["ebit", "intexp", "revenue"], "func": f32_lbac_062_compound_coverage_down_revenue_down_4q},
    "f32_lbac_063_quarters_since_coverage_worsened": {"inputs": ["ebit", "intexp"], "func": f32_lbac_063_quarters_since_coverage_worsened},
    "f32_lbac_064_fcf_intexp_accel_deterioration_z": {"inputs": ["fcf", "intexp"], "func": f32_lbac_064_fcf_intexp_accel_deterioration_z},
    "f32_lbac_065_coverage_cumulative_excess_deterioration_8q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_065_coverage_cumulative_excess_deterioration_8q},
    "f32_lbac_066_coverage_quadratic_c2_8q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_066_coverage_quadratic_c2_8q},
    "f32_lbac_067_coverage_structural_break_4q_vs_16q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_067_coverage_structural_break_4q_vs_16q},
    "f32_lbac_068_coverage_latest_to_16q_max_ratio": {"inputs": ["ebit", "intexp"], "func": f32_lbac_068_coverage_latest_to_16q_max_ratio},
    "f32_lbac_069_log_coverage_slope_4q_minus_12q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_069_log_coverage_slope_4q_minus_12q},
    "f32_lbac_070_coverage_below_2x_fraction_8q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_070_coverage_below_2x_fraction_8q},
    "f32_lbac_071_coverage_below_1x_fraction_8q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_071_coverage_below_1x_fraction_8q},
    "f32_lbac_072_quarters_since_coverage_neg_accel": {"inputs": ["ebit", "intexp"], "func": f32_lbac_072_quarters_since_coverage_neg_accel},
    "f32_lbac_073_coverage_tail_event_count_16q": {"inputs": ["ebit", "intexp"], "func": f32_lbac_073_coverage_tail_event_count_16q},
    "f32_lbac_074_composite_coverage_deterioration_accel_4q": {"inputs": ["ebit", "ebitda", "intexp", "fcf"], "func": f32_lbac_074_composite_coverage_deterioration_accel_4q},
    "f32_lbac_075_composite_leverage_coverage_accel_combo_z": {"inputs": ["debt", "equity", "ebit", "intexp"], "func": f32_lbac_075_composite_leverage_coverage_accel_combo_z},
}
