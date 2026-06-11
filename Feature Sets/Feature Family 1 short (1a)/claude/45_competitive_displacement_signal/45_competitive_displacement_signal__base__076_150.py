"""competitive_displacement_signal base features 076-150 — Pipeline 1a-inverse short-side blowup family.

Continuation of __base__001_075.py — margin-with-revenue-decel coincidence
(negative operating leverage during share loss), debt-funded-growth and
interest-burden stress, multi-metric displacement coincidence, and
composite aggregate-displacement scores. PIT-clean.
"""
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


# ============================================================
#                  FEATURES 076-150
# ============================================================

def f45_cdis_076_gp_margin_decline_with_revenue_decel_count_8q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where GP margin diff < 0 AND revenue YoY < trailing-1y mean — joint compression."""
    gm = _safe_div(gp, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((gm.diff(QDAYS) < 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_077_opinc_margin_decline_with_revenue_decel_count_8q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where op margin diff < 0 AND revenue YoY decelerating."""
    om = _safe_div(opinc, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((om.diff(QDAYS) < 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_078_fcf_margin_decline_with_revenue_decel_count_8q(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where FCF margin diff < 0 AND revenue YoY decelerating."""
    fm = _safe_div(fcf, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((fm.diff(QDAYS) < 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_079_ebitda_margin_decline_with_revenue_decel_count_8q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where EBITDA margin diff < 0 AND revenue YoY decelerating."""
    em = _safe_div(ebitda, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((em.diff(QDAYS) < 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_080_compound_margin_revenue_decel_count_8q(gp: pd.Series, opinc: pd.Series, fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where at least 2 of (gm, om, fcfm) declining AND revenue decelerating."""
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    om_d = (_safe_div(opinc, revenue).diff(QDAYS) < 0).astype(int)
    fm_d = (_safe_div(fcf, revenue).diff(QDAYS) < 0).astype(int)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = ((gm_d + om_d + fm_d) >= 2) & (yoy < m)
    flag = cond.astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_081_margin_compression_speed_during_decel(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Trailing-8q regression slope of GP margin × indicator(revenue YoY < 1y mean) — compression rate during decel."""
    gm = _safe_div(gp, revenue)
    slope = _rolling_slope(gm, DDAYS_2Y)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return slope * cond


def f45_cdis_082_negative_operating_leverage_breadth_count_8q(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Bars in trailing 8q where revenue YoY > 0 AND (gp YoY < 0 OR opinc YoY < 0 OR ebitda YoY < 0)."""
    r_pos = (_safe_log(revenue).diff(YDAYS) > 0)
    any_neg = ((_safe_log(gp).diff(YDAYS) < 0) | (_safe_log_signed(opinc).diff(YDAYS) < 0) | (_safe_log_signed(ebitda).diff(YDAYS) < 0))
    flag = (r_pos & any_neg).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_083_sgna_to_revenue_rise_with_revenue_decel(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean over 8q of indicator((sgna/rev) rising 1y) AND (revenue YoY decel) — competitive-cost-pressure score."""
    sgr = _safe_div(sgna, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((sgr.diff(YDAYS) > 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_084_cor_to_revenue_rise_with_revenue_decel(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean over 8q of indicator((cor/rev) rising 1y) AND (revenue YoY decel) — COGS-pressure-during-share-loss score."""
    cr = _safe_div(cor, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((cr.diff(YDAYS) > 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_085_reinvestment_increase_with_margin_drop_count_8q(capex: pd.Series, gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where capex YoY > 0 AND gp margin diff < 0 — failed-reinvestment count."""
    cyoy = _safe_log_signed(capex).diff(YDAYS)
    gm_d = _safe_div(gp, revenue).diff(QDAYS)
    flag = ((cyoy > 0) & (gm_d < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_086_capex_to_revenue_rise_with_fcf_margin_drop_count_8q(capex: pd.Series, revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """Bars in trailing 8q where capex/rev rising 1y AND fcf-margin falling 1y."""
    ci = _safe_div(capex, revenue)
    fm = _safe_div(fcf, revenue)
    flag = ((ci.diff(YDAYS) > 0) & (fm.diff(YDAYS) < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_087_capex_intensity_above_5y_baseline_with_decel(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean over 8q of (capex/revenue > 5y mean) AND (revenue YoY < 1y mean) — over-investment during share loss."""
    ci = _safe_div(capex, revenue)
    ci_m = ci.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((ci > ci_m) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_088_sgna_acceleration_during_revenue_decel(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    """(sgna YoY) − (revenue YoY) × indicator(revenue decel) — competitive-cost-acceleration intensity."""
    diff = _safe_log(sgna).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return diff * cond


def f45_cdis_089_cor_acceleration_during_revenue_decel(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """(cor YoY) − (revenue YoY) × indicator(revenue decel) — COGS-acceleration intensity during share loss."""
    diff = _safe_log(cor).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return diff * cond


def f45_cdis_090_rnd_acceleration_during_revenue_decel(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    """(rnd YoY) − (revenue YoY) × indicator(revenue decel) — last-ditch R&D-spend intensity."""
    diff = _safe_log(rnd).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return diff * cond


def f45_cdis_091_cost_efficiency_breakdown_during_decel(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """(opex YoY) − (revenue YoY) × indicator(revenue decel) — composite cost-efficiency breakdown."""
    diff = _safe_log(opex).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return diff * cond


def f45_cdis_092_cost_acceleration_during_revenue_decel_breadth_8q(opex: pd.Series, sgna: pd.Series, cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean over 8q of count of cost-metrics (opex, sgna, cor) growing > revenue YoY when revenue is decelerating."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m)
    flag1 = (_safe_log(opex).diff(YDAYS) > yoy)
    flag2 = (_safe_log(sgna).diff(YDAYS) > yoy)
    flag3 = (_safe_log(cor).diff(YDAYS) > yoy)
    breadth = (flag1.astype(int) + flag2.astype(int) + flag3.astype(int)) * decel.astype(int)
    return breadth.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_093_operating_leverage_negative_streak(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Current consecutive-bar streak where revenue YoY > 0 AND opinc YoY < 0 — sustained negative leverage."""
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (_safe_log_signed(opinc).diff(YDAYS) < 0)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_094_operating_leverage_negative_count_8q(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    """Bars in trailing 8q with negative operating leverage (revenue+, opinc−)."""
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (_safe_log_signed(opinc).diff(YDAYS) < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_095_fixed_cost_burden_proxy_level(sgna: pd.Series, rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    """(sgna + rnd) / revenue — fixed-cost burden share."""
    return _safe_div(sgna + rnd, revenue)


def f45_cdis_096_fixed_cost_burden_rise_during_decel(sgna: pd.Series, rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    """1y Δ of (sgna+rnd)/revenue × indicator(revenue decel) — fixed-cost rise during share loss."""
    bur = _safe_div(sgna + rnd, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return bur.diff(YDAYS) * cond


def f45_cdis_097_cost_pressure_composite_8q(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean over 8q of (opex/revenue > trailing-5y mean of itself) — cost-pressure prevalence."""
    r = _safe_div(opex, revenue)
    m = r.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (r > m).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_098_cost_pressure_yoy_change(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """1y Δ of (opex/revenue) — cost-pressure shift over 1y."""
    return _safe_div(opex, revenue).diff(YDAYS)


def f45_cdis_099_cost_pressure_acceleration(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    """Second 252d Δ of (opex/revenue) — change in cost-pressure rate."""
    return _safe_div(opex, revenue).diff(YDAYS).diff(YDAYS)


def f45_cdis_100_cost_competitive_squeeze_score_5y(opex: pd.Series, revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Mean over 5y of [(opex/rev > 5y mean) AND (gp/rev < 5y mean)] — combined cost-and-margin squeeze."""
    or_ = _safe_div(opex, revenue)
    gm = _safe_div(gp, revenue)
    or_m = or_.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    gm_m = gm.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((or_ > or_m) & (gm < gm_m)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f45_cdis_101_debt_to_assets_level(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Debt / assets — leverage ratio."""
    return _safe_div(debt, assets)


def f45_cdis_102_debt_to_assets_change_yoy(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """1y change in debt / assets — annual leverage shift."""
    return _safe_div(debt, assets).diff(YDAYS)


def f45_cdis_103_debt_to_assets_change_5y(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """5y change in debt / assets."""
    return _safe_div(debt, assets).diff(DDAYS_5Y)


def f45_cdis_104_debt_to_assets_zscore_5y(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of debt / assets vs 5y."""
    return _rolling_zscore(_safe_div(debt, assets), DDAYS_5Y)


def f45_cdis_105_debt_growth_outpacing_revenue_streak(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Current streak where debt YoY > revenue YoY — sustained debt-funded-growth."""
    flag = (_safe_log(debt).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y)


def f45_cdis_106_debt_yoy_minus_revenue_yoy(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Debt YoY − revenue YoY — debt-vs-revenue growth gap."""
    return _safe_log(debt).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)


def f45_cdis_107_debt_intensity_acceleration_5y(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """5y regression slope of (debt/revenue) on time — accelerating leverage if positive."""
    return _rolling_slope(_safe_div(debt, revenue), DDAYS_5Y)


def f45_cdis_108_debt_to_ebitda_level(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Debt / EBITDA — leverage-coverage ratio."""
    return _safe_div(debt, ebitda)


def f45_cdis_109_debt_to_ebitda_change_5y(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """5y change in debt / EBITDA."""
    return _safe_div(debt, ebitda).diff(DDAYS_5Y)


def f45_cdis_110_debt_to_ebitda_zscore_5y(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of debt/EBITDA vs 5y."""
    return _rolling_zscore(_safe_div(debt, ebitda), DDAYS_5Y)


def f45_cdis_111_debt_funded_growth_indicator(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if debt YoY > 0.10 AND revenue YoY < 0 — debt up, revenue down (clear debt-funded-stagnation)."""
    flag = ((_safe_log(debt).diff(YDAYS) > 0.10) & (_safe_log(revenue).diff(YDAYS) < 0)).astype(float)
    return flag.where(debt.notna() & revenue.notna(), np.nan)


def f45_cdis_112_financial_leverage_distress_count_8q(debt: pd.Series, ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Bars in trailing 8q where debt/ebitda > trailing-5y p75 AND intexp > 0.25 × ebitda."""
    de = _safe_div(debt, ebitda)
    de_thr = de.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    int_burden = _safe_div(intexp, ebitda)
    flag = ((de > de_thr) & (int_burden > 0.25)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_113_interest_coverage_proxy_level(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Interest coverage = ebitda / intexp."""
    return _safe_div(ebitda, intexp)


def f45_cdis_114_interest_coverage_change_5y(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """5y change in interest coverage."""
    return _safe_div(ebitda, intexp).diff(DDAYS_5Y)


def f45_cdis_115_interest_coverage_zscore_5y(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Z-score of interest coverage vs 5y."""
    return _rolling_zscore(_safe_div(ebitda, intexp), DDAYS_5Y)


def f45_cdis_116_interest_coverage_below_2x_count_8q(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    """Bars in trailing 8q where interest coverage < 2 — sub-investment-grade-coverage frequency."""
    ic = _safe_div(ebitda, intexp)
    flag = (ic < 2.0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_117_interest_burden_rise_during_revenue_decel(intexp: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """1y Δ of (intexp/ebitda) × indicator(revenue YoY < 1y mean) — interest burden shift during share loss."""
    bur = _safe_div(intexp, ebitda)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return bur.diff(YDAYS) * cond


def f45_cdis_118_cash_to_debt_level(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """Cash / debt — liquidity vs leverage."""
    return _safe_div(cashneq, debt)


def f45_cdis_119_cash_to_debt_change_5y(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """5y change in cash / debt."""
    return _safe_div(cashneq, debt).diff(DDAYS_5Y)


def f45_cdis_120_cash_to_debt_zscore_5y(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of cash/debt vs 5y."""
    return _rolling_zscore(_safe_div(cashneq, debt), DDAYS_5Y)


def f45_cdis_121_debt_overhang_acceleration_5y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """5y regression slope of (debt/equity) on time — accelerating overhang if positive."""
    return _rolling_slope(_safe_div(debt, equity), DDAYS_5Y)


def f45_cdis_122_debt_overhang_with_growth_decel_count_8q(debt: pd.Series, equity: pd.Series, revenue: pd.Series) -> pd.Series:
    """Bars in trailing 8q where (debt/equity rising 1y) AND (revenue YoY < 1y mean)."""
    de = _safe_div(debt, equity)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((de.diff(YDAYS) > 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum()


def f45_cdis_123_leverage_concentration_top1_year_5y(debt: pd.Series) -> pd.Series:
    """(max 1y log change in debt over 5y) / (sum of positive 1y log changes over 5y) — top-event concentration."""
    d = _safe_log(debt).diff(YDAYS)
    mx = d.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    pos_sum = d.clip(lower=0).rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return _safe_div(mx, pos_sum)


def f45_cdis_124_leverage_burst_intensity_5y(debt: pd.Series) -> pd.Series:
    """Max 1y log change in debt over 5y — biggest annual debt issuance event."""
    return _safe_log(debt).diff(YDAYS).rolling(DDAYS_5Y, min_periods=YDAYS).max()


def f45_cdis_125_leverage_distress_composite_score_5y(debt: pd.Series, ebitda: pd.Series, intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean over 5y of [(debt/ebitda > 5y p75) AND (intexp/ebitda > 0.25) AND (revenue YoY < 1y mean)]."""
    de = _safe_div(debt, ebitda)
    de_thr = de.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    int_burden = _safe_div(intexp, ebitda)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((de > de_thr) & (int_burden > 0.25) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f45_cdis_126_displacement_breadth_score_8q(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    """Mean over 8q of count of displacement signals firing: rev decel + inv build + AR build + fcf<0 + gp margin compression."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float)
    return total.rolling(DDAYS_2Y, min_periods=YDAYS).mean()


def f45_cdis_127_displacement_breadth_score_5y(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    """5y version of the displacement breadth — long-horizon prevalence of multi-signal displacement."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float)
    return total.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f45_cdis_128_inventory_ar_burst_with_margin_collapse_count_5y(inventory: pd.Series, accountsreceivable: pd.Series, revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Bars in trailing 5y where (Inv+AR)/rev z>1 AND gp margin diff < 0."""
    z = _rolling_zscore(_safe_div(inventory + accountsreceivable, revenue), DDAYS_5Y)
    gm_d = _safe_div(gp, revenue).diff(QDAYS)
    flag = ((z > 1.0) & (gm_d < 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_129_cash_burn_with_inventory_build_indicator(fcf: pd.Series, inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if fcf < 0 AND inventory/rev z > 1 — fused burn-and-stuck-inventory event."""
    z = _rolling_zscore(_safe_div(inventory, revenue), DDAYS_5Y)
    flag = ((fcf < 0) & (z > 1.0)).astype(float)
    return flag.where(fcf.notna() & z.notna(), np.nan)


def f45_cdis_130_cash_burn_with_margin_collapse_indicator(fcf: pd.Series, gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """1 if fcf < 0 AND gp margin < 5y p25 — fused burn-and-margin-collapse event."""
    gm = _safe_div(gp, revenue)
    p25 = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    flag = ((fcf < 0) & (gm < p25)).astype(float)
    return flag.where(fcf.notna() & gm.notna(), np.nan)


def f45_cdis_131_revenue_decel_with_inventory_build_count_5y(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    """Bars in trailing 5y where revenue YoY decel AND inventory/rev rising 1y."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    inv = _safe_div(inventory, revenue)
    flag = ((yoy < m) & (inv.diff(YDAYS) > 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_132_revenue_decel_with_ar_build_count_5y(revenue: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
    """Bars in trailing 5y where revenue YoY decel AND AR/rev rising 1y."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    ar = _safe_div(accountsreceivable, revenue)
    flag = ((yoy < m) & (ar.diff(YDAYS) > 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_133_revenue_decel_with_debt_build_count_5y(revenue: pd.Series, debt: pd.Series) -> pd.Series:
    """Bars in trailing 5y where revenue YoY decel AND debt YoY > 0."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    dyoy = _safe_log(debt).diff(YDAYS)
    flag = ((yoy < m) & (dyoy > 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_134_revenue_decel_with_cash_burn_count_5y(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    """Bars in trailing 5y where revenue YoY decel AND fcf < 0."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((yoy < m) & (fcf < 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_135_revenue_decel_with_margin_compression_count_5y(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    """Bars in trailing 5y where revenue YoY decel AND gp margin diff < 0 — share-loss-and-margin-loss prevalence."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    gm_d = _safe_div(gp, revenue).diff(QDAYS)
    flag = ((yoy < m) & (gm_d < 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_136_multi_signal_coincidence_count_5y(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series, debt: pd.Series) -> pd.Series:
    """Bars in trailing 5y where ≥3 of (decel, inv-build, AR-build, fcf<0, gm-down, debt-up) fire."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_div(inventory, revenue).diff(YDAYS) > 0).astype(int)
    ar_build = (_safe_div(accountsreceivable, revenue).diff(YDAYS) > 0).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    debt_up = (_safe_log(debt).diff(YDAYS) > 0).astype(int)
    total = decel + inv_build + ar_build + fcf_neg + gm_d + debt_up
    flag = (total >= 3).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum()


def f45_cdis_137_displacement_intensity_max_5y(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    """Max within 5y of the same 8q-rolling displacement-breadth score."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return total.rolling(DDAYS_5Y, min_periods=YDAYS).max()


def f45_cdis_138_displacement_intensity_recency_5y(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    """Bars since the 5y-rolling-max of displacement intensity — recency of worst displacement period."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    def _dsm(w):
        if np.isnan(w).all():
            return np.nan
        return float(len(w) - 1 - int(np.nanargmax(w)))
    return total.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_dsm, raw=True)


def f45_cdis_139_displacement_intensity_acceleration(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    """5y regression slope of the displacement breadth score — accelerating displacement if positive."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _rolling_slope(total, DDAYS_5Y)


def f45_cdis_140_displacement_zscore_composite(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series) -> pd.Series:
    """Mean of z-scores (vs 5y) of (1 − fcf/rev), inv/rev, AR/rev, −revenue YoY — composite displacement z."""
    z1 = _rolling_zscore(-_safe_div(fcf, revenue), DDAYS_5Y)
    z2 = _rolling_zscore(_safe_div(inventory, revenue), DDAYS_5Y)
    z3 = _rolling_zscore(_safe_div(accountsreceivable, revenue), DDAYS_5Y)
    z4 = _rolling_zscore(-_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    return (z1 + z2 + z3 + z4) / 4.0


def f45_cdis_141_composite_f45_cdis_distress_5y_score(revenue: pd.Series, fcf: pd.Series, gp: pd.Series, inventory: pd.Series, debt: pd.Series) -> pd.Series:
    """Mean over 5y of indicator(revenue decel AND fcf<0 AND gm < 5y p25 AND inv/rev > 5y p75 AND debt YoY > 0)."""
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    gm = _safe_div(gp, revenue)
    gm_p25 = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    inv = _safe_div(inventory, revenue)
    inv_p75 = inv.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    dyoy = _safe_log(debt).diff(YDAYS)
    flag = ((yoy < m) & (fcf < 0) & (gm < gm_p25) & (inv > inv_p75) & (dyoy > 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f45_cdis_142_composite_f45_cdis_topping_5y_score(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, fcf: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
    """Mean over 5y of avg(1 − rank_pct over 5y) for gm, om, fcfm, (1 − inv/rev), (1 − AR/rev)."""
    gm = _safe_div(gp, revenue)
    om = _safe_div(opinc, revenue)
    fm = _safe_div(fcf, revenue)
    inv = -_safe_div(inventory, revenue)
    ar = -_safe_div(accountsreceivable, revenue)
    series_list = [gm, om, fm, inv, ar]
    total = pd.Series(0.0, index=revenue.index)
    valid = pd.Series(True, index=revenue.index)
    for s in series_list:
        r = _rolling_rank_pct(s, DDAYS_5Y)
        total = total + (1.0 - r)
        valid = valid & r.notna()
    avg = (total / len(series_list)).where(valid, np.nan)
    return avg.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f45_cdis_143_composite_f45_cdis_blowoff_5y_score(revenue: pd.Series, gp: pd.Series, fcf: pd.Series, debt: pd.Series, capex: pd.Series) -> pd.Series:
    """Mean over 5y of indicator(gm < 5y p25 AND fcf/rev < 5y p25 AND debt YoY > 0.15 AND capex YoY > 0.20)."""
    gm = _safe_div(gp, revenue)
    fm = _safe_div(fcf, revenue)
    gm_p25 = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    fm_p25 = fm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    dyoy = _safe_log(debt).diff(YDAYS)
    cyoy = _safe_log_signed(capex).diff(YDAYS)
    flag = ((gm < gm_p25) & (fm < fm_p25) & (dyoy > 0.15) & (cyoy > 0.20)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


def f45_cdis_144_composite_f45_cdis_inventory_ar_pressure(inventory: pd.Series, accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean of [rank_pct(inv/rev) + rank_pct(AR/rev) + rank_pct((inv+AR)/rev)] / 3 — combined working-capital pressure."""
    r1 = _rolling_rank_pct(_safe_div(inventory, revenue), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(accountsreceivable, revenue), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(inventory + accountsreceivable, revenue), DDAYS_5Y)
    return (r1 + r2 + r3) / 3.0


def f45_cdis_145_composite_f45_cdis_debt_pressure(debt: pd.Series, ebitda: pd.Series, intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean of [rank_pct(debt/ebitda) + rank_pct(intexp/ebitda) + rank_pct(debt/revenue)] / 3 — combined leverage pressure."""
    r1 = _rolling_rank_pct(_safe_div(debt, ebitda), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(intexp, ebitda), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(debt, revenue), DDAYS_5Y)
    return (r1 + r2 + r3) / 3.0


def f45_cdis_146_composite_f45_cdis_margin_pressure(gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean of [(1 − rank_pct gm) + (1 − rank_pct om) + (1 − rank_pct em) + (1 − rank_pct fm)] / 4 over 5y."""
    r1 = _rolling_rank_pct(_safe_div(gp, revenue), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(opinc, revenue), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(ebitda, revenue), DDAYS_5Y)
    r4 = _rolling_rank_pct(_safe_div(fcf, revenue), DDAYS_5Y)
    return ((1.0 - r1) + (1.0 - r2) + (1.0 - r3) + (1.0 - r4)) / 4.0


def f45_cdis_147_composite_f45_cdis_cash_pressure(cashneq: pd.Series, fcf: pd.Series, debt: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean of [(1 − rank_pct cash/rev) + (1 − rank_pct cash/debt) + rank_pct(|fcf|/rev when fcf<0)] / 3 over 5y."""
    r1 = _rolling_rank_pct(_safe_div(cashneq, revenue), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(cashneq, debt), DDAYS_5Y)
    burn_int = _safe_div(fcf.clip(upper=0).abs(), revenue)
    r3 = _rolling_rank_pct(burn_int, DDAYS_5Y)
    return ((1.0 - r1) + (1.0 - r2) + r3) / 3.0


def f45_cdis_148_composite_f45_cdis_revenue_pressure(revenue: pd.Series) -> pd.Series:
    """Mean of [(1 − rank_pct of YoY) + rank_pct of revenue-volatility-8q + (1 − rank_pct of trailing-8q mean YoY)] / 3 over 5y."""
    yoy = _safe_log(revenue).diff(YDAYS)
    r1 = _rolling_rank_pct(yoy, DDAYS_5Y)
    vol = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    r2 = _rolling_rank_pct(vol, DDAYS_5Y)
    avg_8q = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    r3 = _rolling_rank_pct(avg_8q, DDAYS_5Y)
    return ((1.0 - r1) + r2 + (1.0 - r3)) / 3.0


def f45_cdis_149_composite_f45_cdis_cost_pressure(opex: pd.Series, sgna: pd.Series, cor: pd.Series, revenue: pd.Series) -> pd.Series:
    """Mean of [rank_pct(opex/rev) + rank_pct(sgna/rev) + rank_pct(cor/rev)] / 3 over 5y."""
    r1 = _rolling_rank_pct(_safe_div(opex, revenue), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(sgna, revenue), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(cor, revenue), DDAYS_5Y)
    return (r1 + r2 + r3) / 3.0


def f45_cdis_150_composite_f45_cdis_aggregate_displacement_score(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series, debt: pd.Series) -> pd.Series:
    """Mean over 5y of [(1 − rank_pct rev YoY) + rank_pct inv/rev + rank_pct AR/rev + rank_pct(|fcf burn|) + (1 − rank_pct gm) + rank_pct debt/rev] / 6."""
    r1 = (1.0 - _rolling_rank_pct(_safe_log(revenue).diff(YDAYS), DDAYS_5Y))
    r2 = _rolling_rank_pct(_safe_div(inventory, revenue), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(accountsreceivable, revenue), DDAYS_5Y)
    burn = _safe_div(fcf.clip(upper=0).abs(), revenue)
    r4 = _rolling_rank_pct(burn, DDAYS_5Y)
    r5 = (1.0 - _rolling_rank_pct(_safe_div(gp, revenue), DDAYS_5Y))
    r6 = _rolling_rank_pct(_safe_div(debt, revenue), DDAYS_5Y)
    score = (r1 + r2 + r3 + r4 + r5 + r6) / 6.0
    return score.rolling(DDAYS_5Y, min_periods=YDAYS).mean()


# ============================================================
#                        REGISTRY
# ============================================================

COMPETITIVE_DISPLACEMENT_SIGNAL_BASE_REGISTRY_076_150 = {
    "f45_cdis_076_gp_margin_decline_with_revenue_decel_count_8q": {"inputs": ["gp", "revenue"], "func": f45_cdis_076_gp_margin_decline_with_revenue_decel_count_8q},
    "f45_cdis_077_opinc_margin_decline_with_revenue_decel_count_8q": {"inputs": ["opinc", "revenue"], "func": f45_cdis_077_opinc_margin_decline_with_revenue_decel_count_8q},
    "f45_cdis_078_fcf_margin_decline_with_revenue_decel_count_8q": {"inputs": ["fcf", "revenue"], "func": f45_cdis_078_fcf_margin_decline_with_revenue_decel_count_8q},
    "f45_cdis_079_ebitda_margin_decline_with_revenue_decel_count_8q": {"inputs": ["ebitda", "revenue"], "func": f45_cdis_079_ebitda_margin_decline_with_revenue_decel_count_8q},
    "f45_cdis_080_compound_margin_revenue_decel_count_8q": {"inputs": ["gp", "opinc", "fcf", "revenue"], "func": f45_cdis_080_compound_margin_revenue_decel_count_8q},
    "f45_cdis_081_margin_compression_speed_during_decel": {"inputs": ["gp", "revenue"], "func": f45_cdis_081_margin_compression_speed_during_decel},
    "f45_cdis_082_negative_operating_leverage_breadth_count_8q": {"inputs": ["revenue", "gp", "opinc", "ebitda"], "func": f45_cdis_082_negative_operating_leverage_breadth_count_8q},
    "f45_cdis_083_sgna_to_revenue_rise_with_revenue_decel": {"inputs": ["sgna", "revenue"], "func": f45_cdis_083_sgna_to_revenue_rise_with_revenue_decel},
    "f45_cdis_084_cor_to_revenue_rise_with_revenue_decel": {"inputs": ["cor", "revenue"], "func": f45_cdis_084_cor_to_revenue_rise_with_revenue_decel},
    "f45_cdis_085_reinvestment_increase_with_margin_drop_count_8q": {"inputs": ["capex", "gp", "revenue"], "func": f45_cdis_085_reinvestment_increase_with_margin_drop_count_8q},
    "f45_cdis_086_capex_to_revenue_rise_with_fcf_margin_drop_count_8q": {"inputs": ["capex", "revenue", "fcf"], "func": f45_cdis_086_capex_to_revenue_rise_with_fcf_margin_drop_count_8q},
    "f45_cdis_087_capex_intensity_above_5y_baseline_with_decel": {"inputs": ["capex", "revenue"], "func": f45_cdis_087_capex_intensity_above_5y_baseline_with_decel},
    "f45_cdis_088_sgna_acceleration_during_revenue_decel": {"inputs": ["sgna", "revenue"], "func": f45_cdis_088_sgna_acceleration_during_revenue_decel},
    "f45_cdis_089_cor_acceleration_during_revenue_decel": {"inputs": ["cor", "revenue"], "func": f45_cdis_089_cor_acceleration_during_revenue_decel},
    "f45_cdis_090_rnd_acceleration_during_revenue_decel": {"inputs": ["rnd", "revenue"], "func": f45_cdis_090_rnd_acceleration_during_revenue_decel},
    "f45_cdis_091_cost_efficiency_breakdown_during_decel": {"inputs": ["opex", "revenue"], "func": f45_cdis_091_cost_efficiency_breakdown_during_decel},
    "f45_cdis_092_cost_acceleration_during_revenue_decel_breadth_8q": {"inputs": ["opex", "sgna", "cor", "revenue"], "func": f45_cdis_092_cost_acceleration_during_revenue_decel_breadth_8q},
    "f45_cdis_093_operating_leverage_negative_streak": {"inputs": ["revenue", "opinc"], "func": f45_cdis_093_operating_leverage_negative_streak},
    "f45_cdis_094_operating_leverage_negative_count_8q": {"inputs": ["revenue", "opinc"], "func": f45_cdis_094_operating_leverage_negative_count_8q},
    "f45_cdis_095_fixed_cost_burden_proxy_level": {"inputs": ["sgna", "rnd", "revenue"], "func": f45_cdis_095_fixed_cost_burden_proxy_level},
    "f45_cdis_096_fixed_cost_burden_rise_during_decel": {"inputs": ["sgna", "rnd", "revenue"], "func": f45_cdis_096_fixed_cost_burden_rise_during_decel},
    "f45_cdis_097_cost_pressure_composite_8q": {"inputs": ["opex", "revenue"], "func": f45_cdis_097_cost_pressure_composite_8q},
    "f45_cdis_098_cost_pressure_yoy_change": {"inputs": ["opex", "revenue"], "func": f45_cdis_098_cost_pressure_yoy_change},
    "f45_cdis_099_cost_pressure_acceleration": {"inputs": ["opex", "revenue"], "func": f45_cdis_099_cost_pressure_acceleration},
    "f45_cdis_100_cost_competitive_squeeze_score_5y": {"inputs": ["opex", "revenue", "gp"], "func": f45_cdis_100_cost_competitive_squeeze_score_5y},
    "f45_cdis_101_debt_to_assets_level": {"inputs": ["debt", "assets"], "func": f45_cdis_101_debt_to_assets_level},
    "f45_cdis_102_debt_to_assets_change_yoy": {"inputs": ["debt", "assets"], "func": f45_cdis_102_debt_to_assets_change_yoy},
    "f45_cdis_103_debt_to_assets_change_5y": {"inputs": ["debt", "assets"], "func": f45_cdis_103_debt_to_assets_change_5y},
    "f45_cdis_104_debt_to_assets_zscore_5y": {"inputs": ["debt", "assets"], "func": f45_cdis_104_debt_to_assets_zscore_5y},
    "f45_cdis_105_debt_growth_outpacing_revenue_streak": {"inputs": ["debt", "revenue"], "func": f45_cdis_105_debt_growth_outpacing_revenue_streak},
    "f45_cdis_106_debt_yoy_minus_revenue_yoy": {"inputs": ["debt", "revenue"], "func": f45_cdis_106_debt_yoy_minus_revenue_yoy},
    "f45_cdis_107_debt_intensity_acceleration_5y": {"inputs": ["debt", "revenue"], "func": f45_cdis_107_debt_intensity_acceleration_5y},
    "f45_cdis_108_debt_to_ebitda_level": {"inputs": ["debt", "ebitda"], "func": f45_cdis_108_debt_to_ebitda_level},
    "f45_cdis_109_debt_to_ebitda_change_5y": {"inputs": ["debt", "ebitda"], "func": f45_cdis_109_debt_to_ebitda_change_5y},
    "f45_cdis_110_debt_to_ebitda_zscore_5y": {"inputs": ["debt", "ebitda"], "func": f45_cdis_110_debt_to_ebitda_zscore_5y},
    "f45_cdis_111_debt_funded_growth_indicator": {"inputs": ["debt", "revenue"], "func": f45_cdis_111_debt_funded_growth_indicator},
    "f45_cdis_112_financial_leverage_distress_count_8q": {"inputs": ["debt", "ebitda", "intexp"], "func": f45_cdis_112_financial_leverage_distress_count_8q},
    "f45_cdis_113_interest_coverage_proxy_level": {"inputs": ["ebitda", "intexp"], "func": f45_cdis_113_interest_coverage_proxy_level},
    "f45_cdis_114_interest_coverage_change_5y": {"inputs": ["ebitda", "intexp"], "func": f45_cdis_114_interest_coverage_change_5y},
    "f45_cdis_115_interest_coverage_zscore_5y": {"inputs": ["ebitda", "intexp"], "func": f45_cdis_115_interest_coverage_zscore_5y},
    "f45_cdis_116_interest_coverage_below_2x_count_8q": {"inputs": ["ebitda", "intexp"], "func": f45_cdis_116_interest_coverage_below_2x_count_8q},
    "f45_cdis_117_interest_burden_rise_during_revenue_decel": {"inputs": ["intexp", "ebitda", "revenue"], "func": f45_cdis_117_interest_burden_rise_during_revenue_decel},
    "f45_cdis_118_cash_to_debt_level": {"inputs": ["cashneq", "debt"], "func": f45_cdis_118_cash_to_debt_level},
    "f45_cdis_119_cash_to_debt_change_5y": {"inputs": ["cashneq", "debt"], "func": f45_cdis_119_cash_to_debt_change_5y},
    "f45_cdis_120_cash_to_debt_zscore_5y": {"inputs": ["cashneq", "debt"], "func": f45_cdis_120_cash_to_debt_zscore_5y},
    "f45_cdis_121_debt_overhang_acceleration_5y": {"inputs": ["debt", "equity"], "func": f45_cdis_121_debt_overhang_acceleration_5y},
    "f45_cdis_122_debt_overhang_with_growth_decel_count_8q": {"inputs": ["debt", "equity", "revenue"], "func": f45_cdis_122_debt_overhang_with_growth_decel_count_8q},
    "f45_cdis_123_leverage_concentration_top1_year_5y": {"inputs": ["debt"], "func": f45_cdis_123_leverage_concentration_top1_year_5y},
    "f45_cdis_124_leverage_burst_intensity_5y": {"inputs": ["debt"], "func": f45_cdis_124_leverage_burst_intensity_5y},
    "f45_cdis_125_leverage_distress_composite_score_5y": {"inputs": ["debt", "ebitda", "intexp", "revenue"], "func": f45_cdis_125_leverage_distress_composite_score_5y},
    "f45_cdis_126_displacement_breadth_score_8q": {"inputs": ["revenue", "inventory", "accountsreceivable", "fcf", "gp"], "func": f45_cdis_126_displacement_breadth_score_8q},
    "f45_cdis_127_displacement_breadth_score_5y": {"inputs": ["revenue", "inventory", "accountsreceivable", "fcf", "gp"], "func": f45_cdis_127_displacement_breadth_score_5y},
    "f45_cdis_128_inventory_ar_burst_with_margin_collapse_count_5y": {"inputs": ["inventory", "accountsreceivable", "revenue", "gp"], "func": f45_cdis_128_inventory_ar_burst_with_margin_collapse_count_5y},
    "f45_cdis_129_cash_burn_with_inventory_build_indicator": {"inputs": ["fcf", "inventory", "revenue"], "func": f45_cdis_129_cash_burn_with_inventory_build_indicator},
    "f45_cdis_130_cash_burn_with_margin_collapse_indicator": {"inputs": ["fcf", "gp", "revenue"], "func": f45_cdis_130_cash_burn_with_margin_collapse_indicator},
    "f45_cdis_131_revenue_decel_with_inventory_build_count_5y": {"inputs": ["revenue", "inventory"], "func": f45_cdis_131_revenue_decel_with_inventory_build_count_5y},
    "f45_cdis_132_revenue_decel_with_ar_build_count_5y": {"inputs": ["revenue", "accountsreceivable"], "func": f45_cdis_132_revenue_decel_with_ar_build_count_5y},
    "f45_cdis_133_revenue_decel_with_debt_build_count_5y": {"inputs": ["revenue", "debt"], "func": f45_cdis_133_revenue_decel_with_debt_build_count_5y},
    "f45_cdis_134_revenue_decel_with_cash_burn_count_5y": {"inputs": ["revenue", "fcf"], "func": f45_cdis_134_revenue_decel_with_cash_burn_count_5y},
    "f45_cdis_135_revenue_decel_with_margin_compression_count_5y": {"inputs": ["revenue", "gp"], "func": f45_cdis_135_revenue_decel_with_margin_compression_count_5y},
    "f45_cdis_136_multi_signal_coincidence_count_5y": {"inputs": ["revenue", "inventory", "accountsreceivable", "fcf", "gp", "debt"], "func": f45_cdis_136_multi_signal_coincidence_count_5y},
    "f45_cdis_137_displacement_intensity_max_5y": {"inputs": ["revenue", "inventory", "accountsreceivable", "fcf", "gp"], "func": f45_cdis_137_displacement_intensity_max_5y},
    "f45_cdis_138_displacement_intensity_recency_5y": {"inputs": ["revenue", "inventory", "accountsreceivable", "fcf", "gp"], "func": f45_cdis_138_displacement_intensity_recency_5y},
    "f45_cdis_139_displacement_intensity_acceleration": {"inputs": ["revenue", "inventory", "accountsreceivable", "fcf", "gp"], "func": f45_cdis_139_displacement_intensity_acceleration},
    "f45_cdis_140_displacement_zscore_composite": {"inputs": ["revenue", "inventory", "accountsreceivable", "fcf"], "func": f45_cdis_140_displacement_zscore_composite},
    "f45_cdis_141_composite_f45_cdis_distress_5y_score": {"inputs": ["revenue", "fcf", "gp", "inventory", "debt"], "func": f45_cdis_141_composite_f45_cdis_distress_5y_score},
    "f45_cdis_142_composite_f45_cdis_topping_5y_score": {"inputs": ["revenue", "gp", "opinc", "fcf", "inventory", "accountsreceivable"], "func": f45_cdis_142_composite_f45_cdis_topping_5y_score},
    "f45_cdis_143_composite_f45_cdis_blowoff_5y_score": {"inputs": ["revenue", "gp", "fcf", "debt", "capex"], "func": f45_cdis_143_composite_f45_cdis_blowoff_5y_score},
    "f45_cdis_144_composite_f45_cdis_inventory_ar_pressure": {"inputs": ["inventory", "accountsreceivable", "revenue"], "func": f45_cdis_144_composite_f45_cdis_inventory_ar_pressure},
    "f45_cdis_145_composite_f45_cdis_debt_pressure": {"inputs": ["debt", "ebitda", "intexp", "revenue"], "func": f45_cdis_145_composite_f45_cdis_debt_pressure},
    "f45_cdis_146_composite_f45_cdis_margin_pressure": {"inputs": ["gp", "opinc", "ebitda", "fcf", "revenue"], "func": f45_cdis_146_composite_f45_cdis_margin_pressure},
    "f45_cdis_147_composite_f45_cdis_cash_pressure": {"inputs": ["cashneq", "fcf", "debt", "revenue"], "func": f45_cdis_147_composite_f45_cdis_cash_pressure},
    "f45_cdis_148_composite_f45_cdis_revenue_pressure": {"inputs": ["revenue"], "func": f45_cdis_148_composite_f45_cdis_revenue_pressure},
    "f45_cdis_149_composite_f45_cdis_cost_pressure": {"inputs": ["opex", "sgna", "cor", "revenue"], "func": f45_cdis_149_composite_f45_cdis_cost_pressure},
    "f45_cdis_150_composite_f45_cdis_aggregate_displacement_score": {"inputs": ["revenue", "inventory", "accountsreceivable", "fcf", "gp", "debt"], "func": f45_cdis_150_composite_f45_cdis_aggregate_displacement_score},
}
