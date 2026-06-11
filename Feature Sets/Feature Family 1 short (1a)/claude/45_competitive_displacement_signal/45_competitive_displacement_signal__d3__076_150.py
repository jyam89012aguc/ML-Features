"""competitive_displacement_signal d3 features 076_150 — 3rd-derivative wrappers.

Each function inlines the corresponding base body and appends .diff().diff().diff() so the output is the third bar-over-bar derivative of the base signal. Helpers, constants, and PIT discipline are identical to the matching __base__076_150.py."""
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

def f45_cdis_076_gp_margin_decline_with_revenue_decel_count_8q_d3(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((gm.diff(QDAYS) < 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_077_opinc_margin_decline_with_revenue_decel_count_8q_d3(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    om = _safe_div(opinc, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((om.diff(QDAYS) < 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_078_fcf_margin_decline_with_revenue_decel_count_8q_d3(fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    fm = _safe_div(fcf, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((fm.diff(QDAYS) < 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_079_ebitda_margin_decline_with_revenue_decel_count_8q_d3(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    em = _safe_div(ebitda, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((em.diff(QDAYS) < 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_080_compound_margin_revenue_decel_count_8q_d3(gp: pd.Series, opinc: pd.Series, fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    om_d = (_safe_div(opinc, revenue).diff(QDAYS) < 0).astype(int)
    fm_d = (_safe_div(fcf, revenue).diff(QDAYS) < 0).astype(int)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (gm_d + om_d + fm_d >= 2) & (yoy < m)
    flag = cond.astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_081_margin_compression_speed_during_decel_d3(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    slope = _rolling_slope(gm, DDAYS_2Y)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return (slope * cond).diff().diff().diff()

def f45_cdis_082_negative_operating_leverage_breadth_count_8q_d3(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, ebitda: pd.Series) -> pd.Series:
    r_pos = _safe_log(revenue).diff(YDAYS) > 0
    any_neg = (_safe_log(gp).diff(YDAYS) < 0) | (_safe_log_signed(opinc).diff(YDAYS) < 0) | (_safe_log_signed(ebitda).diff(YDAYS) < 0)
    flag = (r_pos & any_neg).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_083_sgna_to_revenue_rise_with_revenue_decel_d3(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    sgr = _safe_div(sgna, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((sgr.diff(YDAYS) > 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_084_cor_to_revenue_rise_with_revenue_decel_d3(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    cr = _safe_div(cor, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((cr.diff(YDAYS) > 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_085_reinvestment_increase_with_margin_drop_count_8q_d3(capex: pd.Series, gp: pd.Series, revenue: pd.Series) -> pd.Series:
    cyoy = _safe_log_signed(capex).diff(YDAYS)
    gm_d = _safe_div(gp, revenue).diff(QDAYS)
    flag = ((cyoy > 0) & (gm_d < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_086_capex_to_revenue_rise_with_fcf_margin_drop_count_8q_d3(capex: pd.Series, revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    ci = _safe_div(capex, revenue)
    fm = _safe_div(fcf, revenue)
    flag = ((ci.diff(YDAYS) > 0) & (fm.diff(YDAYS) < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_087_capex_intensity_above_5y_baseline_with_decel_d3(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    ci = _safe_div(capex, revenue)
    ci_m = ci.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((ci > ci_m) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_088_sgna_acceleration_during_revenue_decel_d3(sgna: pd.Series, revenue: pd.Series) -> pd.Series:
    diff = _safe_log(sgna).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return (diff * cond).diff().diff().diff()

def f45_cdis_089_cor_acceleration_during_revenue_decel_d3(cor: pd.Series, revenue: pd.Series) -> pd.Series:
    diff = _safe_log(cor).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return (diff * cond).diff().diff().diff()

def f45_cdis_090_rnd_acceleration_during_revenue_decel_d3(rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    diff = _safe_log(rnd).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return (diff * cond).diff().diff().diff()

def f45_cdis_091_cost_efficiency_breakdown_during_decel_d3(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    diff = _safe_log(opex).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return (diff * cond).diff().diff().diff()

def f45_cdis_092_cost_acceleration_during_revenue_decel_breadth_8q_d3(opex: pd.Series, sgna: pd.Series, cor: pd.Series, revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = yoy < m
    flag1 = _safe_log(opex).diff(YDAYS) > yoy
    flag2 = _safe_log(sgna).diff(YDAYS) > yoy
    flag3 = _safe_log(cor).diff(YDAYS) > yoy
    breadth = (flag1.astype(int) + flag2.astype(int) + flag3.astype(int)) * decel.astype(int)
    return breadth.astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_093_operating_leverage_negative_streak_d3(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (_safe_log_signed(opinc).diff(YDAYS) < 0)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff().diff()

def f45_cdis_094_operating_leverage_negative_count_8q_d3(revenue: pd.Series, opinc: pd.Series) -> pd.Series:
    flag = ((_safe_log(revenue).diff(YDAYS) > 0) & (_safe_log_signed(opinc).diff(YDAYS) < 0)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_095_fixed_cost_burden_proxy_level_d3(sgna: pd.Series, rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(sgna + rnd, revenue).diff().diff().diff()

def f45_cdis_096_fixed_cost_burden_rise_during_decel_d3(sgna: pd.Series, rnd: pd.Series, revenue: pd.Series) -> pd.Series:
    bur = _safe_div(sgna + rnd, revenue)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return (bur.diff(YDAYS) * cond).diff().diff().diff()

def f45_cdis_097_cost_pressure_composite_8q_d3(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    r = _safe_div(opex, revenue)
    m = r.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = (r > m).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_098_cost_pressure_yoy_change_d3(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opex, revenue).diff(YDAYS).diff().diff().diff()

def f45_cdis_099_cost_pressure_acceleration_d3(opex: pd.Series, revenue: pd.Series) -> pd.Series:
    return _safe_div(opex, revenue).diff(YDAYS).diff(YDAYS).diff().diff().diff()

def f45_cdis_100_cost_competitive_squeeze_score_5y_d3(opex: pd.Series, revenue: pd.Series, gp: pd.Series) -> pd.Series:
    or_ = _safe_div(opex, revenue)
    gm = _safe_div(gp, revenue)
    or_m = or_.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    gm_m = gm.rolling(DDAYS_5Y, min_periods=YDAYS).mean()
    flag = ((or_ > or_m) & (gm < gm_m)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_101_debt_to_assets_level_d3(debt: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(debt, assets).diff().diff().diff()

def f45_cdis_102_debt_to_assets_change_yoy_d3(debt: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(debt, assets).diff(YDAYS).diff().diff().diff()

def f45_cdis_103_debt_to_assets_change_5y_d3(debt: pd.Series, assets: pd.Series) -> pd.Series:
    return _safe_div(debt, assets).diff(DDAYS_5Y).diff().diff().diff()

def f45_cdis_104_debt_to_assets_zscore_5y_d3(debt: pd.Series, assets: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(debt, assets), DDAYS_5Y).diff().diff().diff()

def f45_cdis_105_debt_growth_outpacing_revenue_streak_d3(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    flag = (_safe_log(debt).diff(YDAYS) > _safe_log(revenue).diff(YDAYS)).astype(int)
    return _streak_above_zero(flag, DDAYS_5Y).diff().diff().diff()

def f45_cdis_106_debt_yoy_minus_revenue_yoy_d3(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    return (_safe_log(debt).diff(YDAYS) - _safe_log(revenue).diff(YDAYS)).diff().diff().diff()

def f45_cdis_107_debt_intensity_acceleration_5y_d3(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(debt, revenue), DDAYS_5Y).diff().diff().diff()

def f45_cdis_108_debt_to_ebitda_level_d3(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    return _safe_div(debt, ebitda).diff().diff().diff()

def f45_cdis_109_debt_to_ebitda_change_5y_d3(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    return _safe_div(debt, ebitda).diff(DDAYS_5Y).diff().diff().diff()

def f45_cdis_110_debt_to_ebitda_zscore_5y_d3(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(debt, ebitda), DDAYS_5Y).diff().diff().diff()

def f45_cdis_111_debt_funded_growth_indicator_d3(debt: pd.Series, revenue: pd.Series) -> pd.Series:
    flag = ((_safe_log(debt).diff(YDAYS) > 0.1) & (_safe_log(revenue).diff(YDAYS) < 0)).astype(float)
    return flag.where(debt.notna() & revenue.notna(), np.nan).diff().diff().diff()

def f45_cdis_112_financial_leverage_distress_count_8q_d3(debt: pd.Series, ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    de = _safe_div(debt, ebitda)
    de_thr = de.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    int_burden = _safe_div(intexp, ebitda)
    flag = ((de > de_thr) & (int_burden > 0.25)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_113_interest_coverage_proxy_level_d3(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(ebitda, intexp).diff().diff().diff()

def f45_cdis_114_interest_coverage_change_5y_d3(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    return _safe_div(ebitda, intexp).diff(DDAYS_5Y).diff().diff().diff()

def f45_cdis_115_interest_coverage_zscore_5y_d3(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(ebitda, intexp), DDAYS_5Y).diff().diff().diff()

def f45_cdis_116_interest_coverage_below_2x_count_8q_d3(ebitda: pd.Series, intexp: pd.Series) -> pd.Series:
    ic = _safe_div(ebitda, intexp)
    flag = (ic < 2.0).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_117_interest_burden_rise_during_revenue_decel_d3(intexp: pd.Series, ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    bur = _safe_div(intexp, ebitda)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    cond = (yoy < m).astype(float)
    return (bur.diff(YDAYS) * cond).diff().diff().diff()

def f45_cdis_118_cash_to_debt_level_d3(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    return _safe_div(cashneq, debt).diff().diff().diff()

def f45_cdis_119_cash_to_debt_change_5y_d3(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    return _safe_div(cashneq, debt).diff(DDAYS_5Y).diff().diff().diff()

def f45_cdis_120_cash_to_debt_zscore_5y_d3(cashneq: pd.Series, debt: pd.Series) -> pd.Series:
    return _rolling_zscore(_safe_div(cashneq, debt), DDAYS_5Y).diff().diff().diff()

def f45_cdis_121_debt_overhang_acceleration_5y_d3(debt: pd.Series, equity: pd.Series) -> pd.Series:
    return _rolling_slope(_safe_div(debt, equity), DDAYS_5Y).diff().diff().diff()

def f45_cdis_122_debt_overhang_with_growth_decel_count_8q_d3(debt: pd.Series, equity: pd.Series, revenue: pd.Series) -> pd.Series:
    de = _safe_div(debt, equity)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((de.diff(YDAYS) > 0) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_2Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_123_leverage_concentration_top1_year_5y_d3(debt: pd.Series) -> pd.Series:
    d = _safe_log(debt).diff(YDAYS)
    mx = d.rolling(DDAYS_5Y, min_periods=YDAYS).max()
    pos_sum = d.clip(lower=0).rolling(DDAYS_5Y, min_periods=YDAYS).sum()
    return _safe_div(mx, pos_sum).diff().diff().diff()

def f45_cdis_124_leverage_burst_intensity_5y_d3(debt: pd.Series) -> pd.Series:
    return _safe_log(debt).diff(YDAYS).rolling(DDAYS_5Y, min_periods=YDAYS).max().diff().diff().diff()

def f45_cdis_125_leverage_distress_composite_score_5y_d3(debt: pd.Series, ebitda: pd.Series, intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    de = _safe_div(debt, ebitda)
    de_thr = de.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    int_burden = _safe_div(intexp, ebitda)
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((de > de_thr) & (int_burden > 0.25) & (yoy < m)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_126_displacement_breadth_score_8q_d3(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float)
    return total.rolling(DDAYS_2Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_127_displacement_breadth_score_5y_d3(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float)
    return total.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_128_inventory_ar_burst_with_margin_collapse_count_5y_d3(inventory: pd.Series, accountsreceivable: pd.Series, revenue: pd.Series, gp: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_div(inventory + accountsreceivable, revenue), DDAYS_5Y)
    gm_d = _safe_div(gp, revenue).diff(QDAYS)
    flag = ((z > 1.0) & (gm_d < 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_129_cash_burn_with_inventory_build_indicator_d3(fcf: pd.Series, inventory: pd.Series, revenue: pd.Series) -> pd.Series:
    z = _rolling_zscore(_safe_div(inventory, revenue), DDAYS_5Y)
    flag = ((fcf < 0) & (z > 1.0)).astype(float)
    return flag.where(fcf.notna() & z.notna(), np.nan).diff().diff().diff()

def f45_cdis_130_cash_burn_with_margin_collapse_indicator_d3(fcf: pd.Series, gp: pd.Series, revenue: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    p25 = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    flag = ((fcf < 0) & (gm < p25)).astype(float)
    return flag.where(fcf.notna() & gm.notna(), np.nan).diff().diff().diff()

def f45_cdis_131_revenue_decel_with_inventory_build_count_5y_d3(revenue: pd.Series, inventory: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    inv = _safe_div(inventory, revenue)
    flag = ((yoy < m) & (inv.diff(YDAYS) > 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_132_revenue_decel_with_ar_build_count_5y_d3(revenue: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    ar = _safe_div(accountsreceivable, revenue)
    flag = ((yoy < m) & (ar.diff(YDAYS) > 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_133_revenue_decel_with_debt_build_count_5y_d3(revenue: pd.Series, debt: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    dyoy = _safe_log(debt).diff(YDAYS)
    flag = ((yoy < m) & (dyoy > 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_134_revenue_decel_with_cash_burn_count_5y_d3(revenue: pd.Series, fcf: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    flag = ((yoy < m) & (fcf < 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_135_revenue_decel_with_margin_compression_count_5y_d3(revenue: pd.Series, gp: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    gm_d = _safe_div(gp, revenue).diff(QDAYS)
    flag = ((yoy < m) & (gm_d < 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_136_multi_signal_coincidence_count_5y_d3(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series, debt: pd.Series) -> pd.Series:
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
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).sum().diff().diff().diff()

def f45_cdis_137_displacement_intensity_max_5y_d3(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return total.rolling(DDAYS_5Y, min_periods=YDAYS).max().diff().diff().diff()

def f45_cdis_138_displacement_intensity_recency_5y_d3(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
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
    return total.rolling(DDAYS_5Y, min_periods=YDAYS).apply(_dsm, raw=True).diff().diff().diff()

def f45_cdis_139_displacement_intensity_acceleration_d3(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    decel = (yoy < m).astype(int)
    inv_build = (_safe_log(inventory).diff(YDAYS) > yoy).astype(int)
    ar_build = (_safe_log(accountsreceivable).diff(YDAYS) > yoy).astype(int)
    fcf_neg = (fcf < 0).astype(int)
    gm_d = (_safe_div(gp, revenue).diff(QDAYS) < 0).astype(int)
    total = (decel + inv_build + ar_build + fcf_neg + gm_d).astype(float).rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    return _rolling_slope(total, DDAYS_5Y).diff().diff().diff()

def f45_cdis_140_displacement_zscore_composite_d3(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series) -> pd.Series:
    z1 = _rolling_zscore(-_safe_div(fcf, revenue), DDAYS_5Y)
    z2 = _rolling_zscore(_safe_div(inventory, revenue), DDAYS_5Y)
    z3 = _rolling_zscore(_safe_div(accountsreceivable, revenue), DDAYS_5Y)
    z4 = _rolling_zscore(-_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    return ((z1 + z2 + z3 + z4) / 4.0).diff().diff().diff()

def f45_cdis_141_composite_f45_cdis_distress_5y_score_d3(revenue: pd.Series, fcf: pd.Series, gp: pd.Series, inventory: pd.Series, debt: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    m = yoy.rolling(YDAYS, min_periods=QDAYS).mean()
    gm = _safe_div(gp, revenue)
    gm_p25 = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    inv = _safe_div(inventory, revenue)
    inv_p75 = inv.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.75)
    dyoy = _safe_log(debt).diff(YDAYS)
    flag = ((yoy < m) & (fcf < 0) & (gm < gm_p25) & (inv > inv_p75) & (dyoy > 0)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_142_composite_f45_cdis_topping_5y_score_d3(revenue: pd.Series, gp: pd.Series, opinc: pd.Series, fcf: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series) -> pd.Series:
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
    return avg.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_143_composite_f45_cdis_blowoff_5y_score_d3(revenue: pd.Series, gp: pd.Series, fcf: pd.Series, debt: pd.Series, capex: pd.Series) -> pd.Series:
    gm = _safe_div(gp, revenue)
    fm = _safe_div(fcf, revenue)
    gm_p25 = gm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    fm_p25 = fm.rolling(DDAYS_5Y, min_periods=YDAYS).quantile(0.25)
    dyoy = _safe_log(debt).diff(YDAYS)
    cyoy = _safe_log_signed(capex).diff(YDAYS)
    flag = ((gm < gm_p25) & (fm < fm_p25) & (dyoy > 0.15) & (cyoy > 0.2)).astype(float)
    return flag.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff().diff()

def f45_cdis_144_composite_f45_cdis_inventory_ar_pressure_d3(inventory: pd.Series, accountsreceivable: pd.Series, revenue: pd.Series) -> pd.Series:
    r1 = _rolling_rank_pct(_safe_div(inventory, revenue), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(accountsreceivable, revenue), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(inventory + accountsreceivable, revenue), DDAYS_5Y)
    return ((r1 + r2 + r3) / 3.0).diff().diff().diff()

def f45_cdis_145_composite_f45_cdis_debt_pressure_d3(debt: pd.Series, ebitda: pd.Series, intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    r1 = _rolling_rank_pct(_safe_div(debt, ebitda), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(intexp, ebitda), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(debt, revenue), DDAYS_5Y)
    return ((r1 + r2 + r3) / 3.0).diff().diff().diff()

def f45_cdis_146_composite_f45_cdis_margin_pressure_d3(gp: pd.Series, opinc: pd.Series, ebitda: pd.Series, fcf: pd.Series, revenue: pd.Series) -> pd.Series:
    r1 = _rolling_rank_pct(_safe_div(gp, revenue), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(opinc, revenue), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(ebitda, revenue), DDAYS_5Y)
    r4 = _rolling_rank_pct(_safe_div(fcf, revenue), DDAYS_5Y)
    return ((1.0 - r1 + (1.0 - r2) + (1.0 - r3) + (1.0 - r4)) / 4.0).diff().diff().diff()

def f45_cdis_147_composite_f45_cdis_cash_pressure_d3(cashneq: pd.Series, fcf: pd.Series, debt: pd.Series, revenue: pd.Series) -> pd.Series:
    r1 = _rolling_rank_pct(_safe_div(cashneq, revenue), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(cashneq, debt), DDAYS_5Y)
    burn_int = _safe_div(fcf.clip(upper=0).abs(), revenue)
    r3 = _rolling_rank_pct(burn_int, DDAYS_5Y)
    return ((1.0 - r1 + (1.0 - r2) + r3) / 3.0).diff().diff().diff()

def f45_cdis_148_composite_f45_cdis_revenue_pressure_d3(revenue: pd.Series) -> pd.Series:
    yoy = _safe_log(revenue).diff(YDAYS)
    r1 = _rolling_rank_pct(yoy, DDAYS_5Y)
    vol = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).std()
    r2 = _rolling_rank_pct(vol, DDAYS_5Y)
    avg_8q = yoy.rolling(DDAYS_2Y, min_periods=YDAYS).mean()
    r3 = _rolling_rank_pct(avg_8q, DDAYS_5Y)
    return ((1.0 - r1 + r2 + (1.0 - r3)) / 3.0).diff().diff().diff()

def f45_cdis_149_composite_f45_cdis_cost_pressure_d3(opex: pd.Series, sgna: pd.Series, cor: pd.Series, revenue: pd.Series) -> pd.Series:
    r1 = _rolling_rank_pct(_safe_div(opex, revenue), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(sgna, revenue), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(cor, revenue), DDAYS_5Y)
    return ((r1 + r2 + r3) / 3.0).diff().diff().diff()

def f45_cdis_150_composite_f45_cdis_aggregate_displacement_score_d3(revenue: pd.Series, inventory: pd.Series, accountsreceivable: pd.Series, fcf: pd.Series, gp: pd.Series, debt: pd.Series) -> pd.Series:
    r1 = 1.0 - _rolling_rank_pct(_safe_log(revenue).diff(YDAYS), DDAYS_5Y)
    r2 = _rolling_rank_pct(_safe_div(inventory, revenue), DDAYS_5Y)
    r3 = _rolling_rank_pct(_safe_div(accountsreceivable, revenue), DDAYS_5Y)
    burn = _safe_div(fcf.clip(upper=0).abs(), revenue)
    r4 = _rolling_rank_pct(burn, DDAYS_5Y)
    r5 = 1.0 - _rolling_rank_pct(_safe_div(gp, revenue), DDAYS_5Y)
    r6 = _rolling_rank_pct(_safe_div(debt, revenue), DDAYS_5Y)
    score = (r1 + r2 + r3 + r4 + r5 + r6) / 6.0
    return score.rolling(DDAYS_5Y, min_periods=YDAYS).mean().diff().diff().diff()
COMPETITIVE_DISPLACEMENT_SIGNAL_D3_REGISTRY_076_150 = {'f45_cdis_076_gp_margin_decline_with_revenue_decel_count_8q_d3': {'inputs': ['gp', 'revenue'], 'func': f45_cdis_076_gp_margin_decline_with_revenue_decel_count_8q_d3}, 'f45_cdis_077_opinc_margin_decline_with_revenue_decel_count_8q_d3': {'inputs': ['opinc', 'revenue'], 'func': f45_cdis_077_opinc_margin_decline_with_revenue_decel_count_8q_d3}, 'f45_cdis_078_fcf_margin_decline_with_revenue_decel_count_8q_d3': {'inputs': ['fcf', 'revenue'], 'func': f45_cdis_078_fcf_margin_decline_with_revenue_decel_count_8q_d3}, 'f45_cdis_079_ebitda_margin_decline_with_revenue_decel_count_8q_d3': {'inputs': ['ebitda', 'revenue'], 'func': f45_cdis_079_ebitda_margin_decline_with_revenue_decel_count_8q_d3}, 'f45_cdis_080_compound_margin_revenue_decel_count_8q_d3': {'inputs': ['gp', 'opinc', 'fcf', 'revenue'], 'func': f45_cdis_080_compound_margin_revenue_decel_count_8q_d3}, 'f45_cdis_081_margin_compression_speed_during_decel_d3': {'inputs': ['gp', 'revenue'], 'func': f45_cdis_081_margin_compression_speed_during_decel_d3}, 'f45_cdis_082_negative_operating_leverage_breadth_count_8q_d3': {'inputs': ['revenue', 'gp', 'opinc', 'ebitda'], 'func': f45_cdis_082_negative_operating_leverage_breadth_count_8q_d3}, 'f45_cdis_083_sgna_to_revenue_rise_with_revenue_decel_d3': {'inputs': ['sgna', 'revenue'], 'func': f45_cdis_083_sgna_to_revenue_rise_with_revenue_decel_d3}, 'f45_cdis_084_cor_to_revenue_rise_with_revenue_decel_d3': {'inputs': ['cor', 'revenue'], 'func': f45_cdis_084_cor_to_revenue_rise_with_revenue_decel_d3}, 'f45_cdis_085_reinvestment_increase_with_margin_drop_count_8q_d3': {'inputs': ['capex', 'gp', 'revenue'], 'func': f45_cdis_085_reinvestment_increase_with_margin_drop_count_8q_d3}, 'f45_cdis_086_capex_to_revenue_rise_with_fcf_margin_drop_count_8q_d3': {'inputs': ['capex', 'revenue', 'fcf'], 'func': f45_cdis_086_capex_to_revenue_rise_with_fcf_margin_drop_count_8q_d3}, 'f45_cdis_087_capex_intensity_above_5y_baseline_with_decel_d3': {'inputs': ['capex', 'revenue'], 'func': f45_cdis_087_capex_intensity_above_5y_baseline_with_decel_d3}, 'f45_cdis_088_sgna_acceleration_during_revenue_decel_d3': {'inputs': ['sgna', 'revenue'], 'func': f45_cdis_088_sgna_acceleration_during_revenue_decel_d3}, 'f45_cdis_089_cor_acceleration_during_revenue_decel_d3': {'inputs': ['cor', 'revenue'], 'func': f45_cdis_089_cor_acceleration_during_revenue_decel_d3}, 'f45_cdis_090_rnd_acceleration_during_revenue_decel_d3': {'inputs': ['rnd', 'revenue'], 'func': f45_cdis_090_rnd_acceleration_during_revenue_decel_d3}, 'f45_cdis_091_cost_efficiency_breakdown_during_decel_d3': {'inputs': ['opex', 'revenue'], 'func': f45_cdis_091_cost_efficiency_breakdown_during_decel_d3}, 'f45_cdis_092_cost_acceleration_during_revenue_decel_breadth_8q_d3': {'inputs': ['opex', 'sgna', 'cor', 'revenue'], 'func': f45_cdis_092_cost_acceleration_during_revenue_decel_breadth_8q_d3}, 'f45_cdis_093_operating_leverage_negative_streak_d3': {'inputs': ['revenue', 'opinc'], 'func': f45_cdis_093_operating_leverage_negative_streak_d3}, 'f45_cdis_094_operating_leverage_negative_count_8q_d3': {'inputs': ['revenue', 'opinc'], 'func': f45_cdis_094_operating_leverage_negative_count_8q_d3}, 'f45_cdis_095_fixed_cost_burden_proxy_level_d3': {'inputs': ['sgna', 'rnd', 'revenue'], 'func': f45_cdis_095_fixed_cost_burden_proxy_level_d3}, 'f45_cdis_096_fixed_cost_burden_rise_during_decel_d3': {'inputs': ['sgna', 'rnd', 'revenue'], 'func': f45_cdis_096_fixed_cost_burden_rise_during_decel_d3}, 'f45_cdis_097_cost_pressure_composite_8q_d3': {'inputs': ['opex', 'revenue'], 'func': f45_cdis_097_cost_pressure_composite_8q_d3}, 'f45_cdis_098_cost_pressure_yoy_change_d3': {'inputs': ['opex', 'revenue'], 'func': f45_cdis_098_cost_pressure_yoy_change_d3}, 'f45_cdis_099_cost_pressure_acceleration_d3': {'inputs': ['opex', 'revenue'], 'func': f45_cdis_099_cost_pressure_acceleration_d3}, 'f45_cdis_100_cost_competitive_squeeze_score_5y_d3': {'inputs': ['opex', 'revenue', 'gp'], 'func': f45_cdis_100_cost_competitive_squeeze_score_5y_d3}, 'f45_cdis_101_debt_to_assets_level_d3': {'inputs': ['debt', 'assets'], 'func': f45_cdis_101_debt_to_assets_level_d3}, 'f45_cdis_102_debt_to_assets_change_yoy_d3': {'inputs': ['debt', 'assets'], 'func': f45_cdis_102_debt_to_assets_change_yoy_d3}, 'f45_cdis_103_debt_to_assets_change_5y_d3': {'inputs': ['debt', 'assets'], 'func': f45_cdis_103_debt_to_assets_change_5y_d3}, 'f45_cdis_104_debt_to_assets_zscore_5y_d3': {'inputs': ['debt', 'assets'], 'func': f45_cdis_104_debt_to_assets_zscore_5y_d3}, 'f45_cdis_105_debt_growth_outpacing_revenue_streak_d3': {'inputs': ['debt', 'revenue'], 'func': f45_cdis_105_debt_growth_outpacing_revenue_streak_d3}, 'f45_cdis_106_debt_yoy_minus_revenue_yoy_d3': {'inputs': ['debt', 'revenue'], 'func': f45_cdis_106_debt_yoy_minus_revenue_yoy_d3}, 'f45_cdis_107_debt_intensity_acceleration_5y_d3': {'inputs': ['debt', 'revenue'], 'func': f45_cdis_107_debt_intensity_acceleration_5y_d3}, 'f45_cdis_108_debt_to_ebitda_level_d3': {'inputs': ['debt', 'ebitda'], 'func': f45_cdis_108_debt_to_ebitda_level_d3}, 'f45_cdis_109_debt_to_ebitda_change_5y_d3': {'inputs': ['debt', 'ebitda'], 'func': f45_cdis_109_debt_to_ebitda_change_5y_d3}, 'f45_cdis_110_debt_to_ebitda_zscore_5y_d3': {'inputs': ['debt', 'ebitda'], 'func': f45_cdis_110_debt_to_ebitda_zscore_5y_d3}, 'f45_cdis_111_debt_funded_growth_indicator_d3': {'inputs': ['debt', 'revenue'], 'func': f45_cdis_111_debt_funded_growth_indicator_d3}, 'f45_cdis_112_financial_leverage_distress_count_8q_d3': {'inputs': ['debt', 'ebitda', 'intexp'], 'func': f45_cdis_112_financial_leverage_distress_count_8q_d3}, 'f45_cdis_113_interest_coverage_proxy_level_d3': {'inputs': ['ebitda', 'intexp'], 'func': f45_cdis_113_interest_coverage_proxy_level_d3}, 'f45_cdis_114_interest_coverage_change_5y_d3': {'inputs': ['ebitda', 'intexp'], 'func': f45_cdis_114_interest_coverage_change_5y_d3}, 'f45_cdis_115_interest_coverage_zscore_5y_d3': {'inputs': ['ebitda', 'intexp'], 'func': f45_cdis_115_interest_coverage_zscore_5y_d3}, 'f45_cdis_116_interest_coverage_below_2x_count_8q_d3': {'inputs': ['ebitda', 'intexp'], 'func': f45_cdis_116_interest_coverage_below_2x_count_8q_d3}, 'f45_cdis_117_interest_burden_rise_during_revenue_decel_d3': {'inputs': ['intexp', 'ebitda', 'revenue'], 'func': f45_cdis_117_interest_burden_rise_during_revenue_decel_d3}, 'f45_cdis_118_cash_to_debt_level_d3': {'inputs': ['cashneq', 'debt'], 'func': f45_cdis_118_cash_to_debt_level_d3}, 'f45_cdis_119_cash_to_debt_change_5y_d3': {'inputs': ['cashneq', 'debt'], 'func': f45_cdis_119_cash_to_debt_change_5y_d3}, 'f45_cdis_120_cash_to_debt_zscore_5y_d3': {'inputs': ['cashneq', 'debt'], 'func': f45_cdis_120_cash_to_debt_zscore_5y_d3}, 'f45_cdis_121_debt_overhang_acceleration_5y_d3': {'inputs': ['debt', 'equity'], 'func': f45_cdis_121_debt_overhang_acceleration_5y_d3}, 'f45_cdis_122_debt_overhang_with_growth_decel_count_8q_d3': {'inputs': ['debt', 'equity', 'revenue'], 'func': f45_cdis_122_debt_overhang_with_growth_decel_count_8q_d3}, 'f45_cdis_123_leverage_concentration_top1_year_5y_d3': {'inputs': ['debt'], 'func': f45_cdis_123_leverage_concentration_top1_year_5y_d3}, 'f45_cdis_124_leverage_burst_intensity_5y_d3': {'inputs': ['debt'], 'func': f45_cdis_124_leverage_burst_intensity_5y_d3}, 'f45_cdis_125_leverage_distress_composite_score_5y_d3': {'inputs': ['debt', 'ebitda', 'intexp', 'revenue'], 'func': f45_cdis_125_leverage_distress_composite_score_5y_d3}, 'f45_cdis_126_displacement_breadth_score_8q_d3': {'inputs': ['revenue', 'inventory', 'accountsreceivable', 'fcf', 'gp'], 'func': f45_cdis_126_displacement_breadth_score_8q_d3}, 'f45_cdis_127_displacement_breadth_score_5y_d3': {'inputs': ['revenue', 'inventory', 'accountsreceivable', 'fcf', 'gp'], 'func': f45_cdis_127_displacement_breadth_score_5y_d3}, 'f45_cdis_128_inventory_ar_burst_with_margin_collapse_count_5y_d3': {'inputs': ['inventory', 'accountsreceivable', 'revenue', 'gp'], 'func': f45_cdis_128_inventory_ar_burst_with_margin_collapse_count_5y_d3}, 'f45_cdis_129_cash_burn_with_inventory_build_indicator_d3': {'inputs': ['fcf', 'inventory', 'revenue'], 'func': f45_cdis_129_cash_burn_with_inventory_build_indicator_d3}, 'f45_cdis_130_cash_burn_with_margin_collapse_indicator_d3': {'inputs': ['fcf', 'gp', 'revenue'], 'func': f45_cdis_130_cash_burn_with_margin_collapse_indicator_d3}, 'f45_cdis_131_revenue_decel_with_inventory_build_count_5y_d3': {'inputs': ['revenue', 'inventory'], 'func': f45_cdis_131_revenue_decel_with_inventory_build_count_5y_d3}, 'f45_cdis_132_revenue_decel_with_ar_build_count_5y_d3': {'inputs': ['revenue', 'accountsreceivable'], 'func': f45_cdis_132_revenue_decel_with_ar_build_count_5y_d3}, 'f45_cdis_133_revenue_decel_with_debt_build_count_5y_d3': {'inputs': ['revenue', 'debt'], 'func': f45_cdis_133_revenue_decel_with_debt_build_count_5y_d3}, 'f45_cdis_134_revenue_decel_with_cash_burn_count_5y_d3': {'inputs': ['revenue', 'fcf'], 'func': f45_cdis_134_revenue_decel_with_cash_burn_count_5y_d3}, 'f45_cdis_135_revenue_decel_with_margin_compression_count_5y_d3': {'inputs': ['revenue', 'gp'], 'func': f45_cdis_135_revenue_decel_with_margin_compression_count_5y_d3}, 'f45_cdis_136_multi_signal_coincidence_count_5y_d3': {'inputs': ['revenue', 'inventory', 'accountsreceivable', 'fcf', 'gp', 'debt'], 'func': f45_cdis_136_multi_signal_coincidence_count_5y_d3}, 'f45_cdis_137_displacement_intensity_max_5y_d3': {'inputs': ['revenue', 'inventory', 'accountsreceivable', 'fcf', 'gp'], 'func': f45_cdis_137_displacement_intensity_max_5y_d3}, 'f45_cdis_138_displacement_intensity_recency_5y_d3': {'inputs': ['revenue', 'inventory', 'accountsreceivable', 'fcf', 'gp'], 'func': f45_cdis_138_displacement_intensity_recency_5y_d3}, 'f45_cdis_139_displacement_intensity_acceleration_d3': {'inputs': ['revenue', 'inventory', 'accountsreceivable', 'fcf', 'gp'], 'func': f45_cdis_139_displacement_intensity_acceleration_d3}, 'f45_cdis_140_displacement_zscore_composite_d3': {'inputs': ['revenue', 'inventory', 'accountsreceivable', 'fcf'], 'func': f45_cdis_140_displacement_zscore_composite_d3}, 'f45_cdis_141_composite_f45_cdis_distress_5y_score_d3': {'inputs': ['revenue', 'fcf', 'gp', 'inventory', 'debt'], 'func': f45_cdis_141_composite_f45_cdis_distress_5y_score_d3}, 'f45_cdis_142_composite_f45_cdis_topping_5y_score_d3': {'inputs': ['revenue', 'gp', 'opinc', 'fcf', 'inventory', 'accountsreceivable'], 'func': f45_cdis_142_composite_f45_cdis_topping_5y_score_d3}, 'f45_cdis_143_composite_f45_cdis_blowoff_5y_score_d3': {'inputs': ['revenue', 'gp', 'fcf', 'debt', 'capex'], 'func': f45_cdis_143_composite_f45_cdis_blowoff_5y_score_d3}, 'f45_cdis_144_composite_f45_cdis_inventory_ar_pressure_d3': {'inputs': ['inventory', 'accountsreceivable', 'revenue'], 'func': f45_cdis_144_composite_f45_cdis_inventory_ar_pressure_d3}, 'f45_cdis_145_composite_f45_cdis_debt_pressure_d3': {'inputs': ['debt', 'ebitda', 'intexp', 'revenue'], 'func': f45_cdis_145_composite_f45_cdis_debt_pressure_d3}, 'f45_cdis_146_composite_f45_cdis_margin_pressure_d3': {'inputs': ['gp', 'opinc', 'ebitda', 'fcf', 'revenue'], 'func': f45_cdis_146_composite_f45_cdis_margin_pressure_d3}, 'f45_cdis_147_composite_f45_cdis_cash_pressure_d3': {'inputs': ['cashneq', 'fcf', 'debt', 'revenue'], 'func': f45_cdis_147_composite_f45_cdis_cash_pressure_d3}, 'f45_cdis_148_composite_f45_cdis_revenue_pressure_d3': {'inputs': ['revenue'], 'func': f45_cdis_148_composite_f45_cdis_revenue_pressure_d3}, 'f45_cdis_149_composite_f45_cdis_cost_pressure_d3': {'inputs': ['opex', 'sgna', 'cor', 'revenue'], 'func': f45_cdis_149_composite_f45_cdis_cost_pressure_d3}, 'f45_cdis_150_composite_f45_cdis_aggregate_displacement_score_d3': {'inputs': ['revenue', 'inventory', 'accountsreceivable', 'fcf', 'gp', 'debt'], 'func': f45_cdis_150_composite_f45_cdis_aggregate_displacement_score_d3}}
