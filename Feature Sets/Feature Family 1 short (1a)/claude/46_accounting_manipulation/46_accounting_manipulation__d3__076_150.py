"""accounting_manipulation d3 features 076_150 — order-3 difference of corresponding base feature.

Each function inlines the base body and wraps the final return with .diff().diff().diff(). Self-contained per HANDOFF.
"""

import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


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


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy(s):
    return s - s.shift(4)


def _qoq(s):
    return s.diff()


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _consec_streak_pos(s, window):
    def _streak(w):
        c = 0
        for v in w[::-1]:
            if np.isnan(v):
                break
            if v > 0:
                c += 1
            else:
                break
        return c
    return s.rolling(window, min_periods=1).apply(_streak, raw=True)


def _consec_streak_neg(s, window):
    def _streak(w):
        c = 0
        for v in w[::-1]:
            if np.isnan(v):
                break
            if v < 0:
                c += 1
            else:
                break
        return c
    return s.rolling(window, min_periods=1).apply(_streak, raw=True)


def f46_amnp_076_inventory_buildup_above_revenue_persistence_4q_d3(inventory, revenue):
    flag = (_yoy_pct(inventory) > _yoy_pct(revenue)).astype(float)
    return (flag.rolling(4, min_periods=2).sum()).diff().diff().diff()


def f46_amnp_077_inventory_zscore_12q_d3(inventory):
    return (_rolling_zscore(inventory, 12, min_periods=4)).diff().diff().diff()


def f46_amnp_078_inventory_breach_of_8q_max_indicator_d3(inventory):
    rmax = inventory.rolling(8, min_periods=3).max().shift(1)
    return ((inventory > rmax).astype(float)).diff().diff().diff()


def f46_amnp_079_inventory_growth_acceleration_d3(inventory):
    return (_qoq_pct(inventory).diff()).diff().diff().diff()


def f46_amnp_080_inventory_growth_consec_above_rev_growth_streak_d3(inventory, revenue):
    diff = _yoy_pct(inventory) - _yoy_pct(revenue)
    return (_consec_streak_pos(diff, 16)).diff().diff().diff()


def f46_amnp_081_inventory_to_payables_ratio_qoq_change_d3(inventory, payables):
    return (_safe_div(inventory, payables).diff()).diff().diff().diff()


def f46_amnp_082_ar_plus_inventory_growth_minus_rev_growth_yoy_d3(receivables, inventory, revenue):
    return (_yoy_pct(receivables + inventory) - _yoy_pct(revenue)).diff().diff().diff()


def f46_amnp_083_ar_plus_inventory_to_revenue_yoy_change_d3(receivables, inventory, revenue):
    ratio = _safe_div(receivables + inventory, _ttm(revenue))
    return (ratio - ratio.shift(4)).diff().diff().diff()


def f46_amnp_084_inventory_writedown_risk_proxy_d3(inventory, cogs):
    return (_qoq_pct(inventory) - _qoq_pct(cogs)).diff().diff().diff()


def f46_amnp_085_inventory_ttm_avg_growth_yoy_d3(inventory):
    return (_yoy_pct(_ttm(inventory))).diff().diff().diff()


def f46_amnp_086_capex_to_depamor_ratio_d3(capex, depamor):
    return (_safe_div(capex.abs(), depamor)).diff().diff().diff()


def f46_amnp_087_capex_to_depamor_qoq_change_d3(capex, depamor):
    return (_safe_div(capex.abs(), depamor).diff()).diff().diff().diff()


def f46_amnp_088_capex_to_depamor_zscore_8q_d3(capex, depamor):
    return (_rolling_zscore(_safe_div(capex.abs(), depamor), 8, min_periods=3)).diff().diff().diff()


def f46_amnp_089_depamor_to_ppnenet_ratio_d3(depamor, ppnenet):
    return (_safe_div(depamor, ppnenet)).diff().diff().diff()


def f46_amnp_090_depamor_to_ppnenet_yoy_change_d3(depamor, ppnenet):
    r = _safe_div(depamor, ppnenet)
    return (r - r.shift(4)).diff().diff().diff()


def f46_amnp_091_ppnenet_growth_minus_revenue_growth_yoy_d3(ppnenet, revenue):
    return (_yoy_pct(ppnenet) - _yoy_pct(revenue)).diff().diff().diff()


def f46_amnp_092_capex_yoy_pct_d3(capex):
    return (_yoy_pct(capex.abs())).diff().diff().diff()


def f46_amnp_093_capex_qoq_pct_d3(capex):
    return (_qoq_pct(capex.abs())).diff().diff().diff()


def f46_amnp_094_capex_8q_slope_d3(capex):
    return (_rolling_slope(capex.abs(), 8, min_periods=3)).diff().diff().diff()


def f46_amnp_095_intangibles_to_assets_ratio_d3(intangibles, assets):
    return (_safe_div(intangibles, assets)).diff().diff().diff()


def f46_amnp_096_intangibles_yoy_pct_d3(intangibles):
    return (_yoy_pct(intangibles)).diff().diff().diff()


def f46_amnp_097_intangibles_growth_minus_revenue_growth_yoy_d3(intangibles, revenue):
    return (_yoy_pct(intangibles) - _yoy_pct(revenue)).diff().diff().diff()


def f46_amnp_098_intangibles_zscore_8q_d3(intangibles):
    return (_rolling_zscore(intangibles, 8, min_periods=3)).diff().diff().diff()


def f46_amnp_099_capitalized_costs_proxy_qoq_d3(ppnenet, intangibles, revenue):
    return (_safe_div((ppnenet + intangibles).diff(), revenue.abs())).diff().diff().diff()


def f46_amnp_100_depamor_share_of_revenue_d3(depamor, revenue):
    return (_safe_div(depamor, revenue)).diff().diff().diff()


def f46_amnp_101_depamor_share_of_revenue_qoq_change_d3(depamor, revenue):
    return (_safe_div(depamor, revenue).diff()).diff().diff().diff()


def f46_amnp_102_impairment_risk_proxy_indicator_d3(ppnenet):
    return ((_qoq_pct(ppnenet) < -0.10).astype(float)).diff().diff().diff()


def f46_amnp_103_goodwill_proxy_growth_d3(intangibles):
    return (_yoy_pct(intangibles)).diff().diff().diff()


def f46_amnp_104_asset_quality_index_qoq_change_d3(assetsc, ppnenet, assets):
    aqi_cur = 1.0 - _safe_div(assetsc + ppnenet, assets)
    aqi_prv = 1.0 - _safe_div(assetsc.shift(4) + ppnenet.shift(4), assets.shift(4))
    return (_safe_div(aqi_cur, aqi_prv).diff()).diff().diff().diff()


def f46_amnp_105_asset_quality_index_8q_slope_d3(assetsc, ppnenet, assets):
    aqi_cur = 1.0 - _safe_div(assetsc + ppnenet, assets)
    aqi_prv = 1.0 - _safe_div(assetsc.shift(4) + ppnenet.shift(4), assets.shift(4))
    return (_rolling_slope(_safe_div(aqi_cur, aqi_prv), 8, min_periods=3)).diff().diff().diff()


def f46_amnp_106_deferredrev_to_revenue_zscore_8q_d3(deferredrev, revenue):
    return (_rolling_zscore(_safe_div(deferredrev, _ttm(revenue)), 8, min_periods=3)).diff().diff().diff()


def f46_amnp_107_deferredrev_qoq_pct_d3(deferredrev):
    return (_qoq_pct(deferredrev)).diff().diff().diff()


def f46_amnp_108_deferredrev_yoy_pct_d3(deferredrev):
    return (_yoy_pct(deferredrev)).diff().diff().diff()


def f46_amnp_109_deferredrev_growth_minus_revenue_growth_yoy_d3(deferredrev, revenue):
    return (_yoy_pct(deferredrev) - _yoy_pct(revenue)).diff().diff().diff()


def f46_amnp_110_deferredrev_drawdown_from_8q_max_d3(deferredrev):
    rmax = deferredrev.rolling(8, min_periods=3).max()
    return (_safe_div(deferredrev, rmax) - 1.0).diff().diff().diff()


def f46_amnp_111_deferredrev_decay_4q_d3(deferredrev):
    return (deferredrev - deferredrev.shift(4)).diff().diff().diff()


def f46_amnp_112_liabilities_to_assets_qoq_change_d3(liabilities, assets):
    return (_safe_div(liabilities, assets).diff()).diff().diff().diff()


def f46_amnp_113_liabilities_to_assets_zscore_8q_d3(liabilities, assets):
    return (_rolling_zscore(_safe_div(liabilities, assets), 8, min_periods=3)).diff().diff().diff()


def f46_amnp_114_currentliab_to_currentassets_qoq_change_d3(liabilitiesc, assetsc):
    return (_safe_div(liabilitiesc, assetsc).diff()).diff().diff().diff()


def f46_amnp_115_payables_to_cogs_ratio_d3(payables, cogs):
    return (_safe_div(payables, cogs)).diff().diff().diff()


def f46_amnp_116_payables_to_cogs_yoy_change_d3(payables, cogs):
    r = _safe_div(payables, cogs)
    return (r - r.shift(4)).diff().diff().diff()


def f46_amnp_117_payables_growth_minus_cogs_growth_yoy_d3(payables, cogs):
    return (_yoy_pct(payables) - _yoy_pct(cogs)).diff().diff().diff()


def f46_amnp_118_payables_stretching_proxy_d3(payables, cogs):
    return (_yoy_pct(payables) - _yoy_pct(cogs)).diff().diff().diff()


def f46_amnp_119_payables_share_of_liabilities_yoy_change_d3(payables, liabilities):
    share = _safe_div(payables, liabilities)
    return (share - share.shift(4)).diff().diff().diff()


def f46_amnp_120_liabilities_growth_persistence_above_assets_4q_d3(liabilities, assets):
    flag = (_yoy_pct(liabilities) > _yoy_pct(assets)).astype(float)
    return (flag.rolling(4, min_periods=2).sum()).diff().diff().diff()


def f46_amnp_121_shortterm_debt_buildup_proxy_d3(liabilitiesc):
    return (_qoq_pct(liabilitiesc)).diff().diff().diff()


def f46_amnp_122_shortterm_debt_share_yoy_change_d3(liabilitiesc, liabilities):
    share = _safe_div(liabilitiesc, liabilities)
    return (share - share.shift(4)).diff().diff().diff()


def f46_amnp_123_accrued_liabilities_proxy_qoq_d3(liabilitiesc, payables, deferredrev):
    return (_qoq_pct(liabilitiesc - payables - deferredrev)).diff().diff().diff()


def f46_amnp_124_liabilities_zscore_12q_d3(liabilities):
    return (_rolling_zscore(liabilities, 12, min_periods=4)).diff().diff().diff()


def f46_amnp_125_debt_growth_minus_revenue_growth_yoy_d3(debt, revenue):
    return (_yoy_pct(debt) - _yoy_pct(revenue)).diff().diff().diff()


def f46_amnp_126_piotroski_reverse_count_d3(netinc, ncfo, assets, revenue, gp):
    acc = _safe_div(netinc - ncfo, assets)
    roa = _safe_div(_ttm(netinc), assets)
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    at = _safe_div(_ttm(revenue), assets)
    f1 = (netinc < 0).astype(float)
    f2 = (ncfo < 0).astype(float)
    f3 = (acc > 0).astype(float)
    f4 = ((roa - roa.shift(4)) < 0).astype(float)
    f5 = ((gm - gm.shift(4)) < 0).astype(float)
    f6 = ((at - at.shift(4)) < 0).astype(float)
    return (f1 + f2 + f3 + f4 + f5 + f6).diff().diff().diff()


def f46_amnp_127_dechow_f_score_proxy_d3(receivables, revenue, gp, assetsc, ppnenet, assets,
                                    depamor, sgna, debt, liabilitiesc, cashneq, netinc, ncfo):
    dsri = _safe_div(_safe_div(receivables, revenue), _safe_div(receivables.shift(4), revenue.shift(4)))
    sgi = _safe_div(revenue, revenue.shift(4))
    acc = _safe_div(netinc - ncfo, assets)
    acc_z = _rolling_zscore(acc, 8, min_periods=3)
    lvgi = _safe_div(_safe_div(debt + liabilitiesc, assets),
                     _safe_div(debt.shift(4) + liabilitiesc.shift(4), assets.shift(4)))
    return (0.25 * dsri + 0.25 * sgi + 0.25 * acc_z + 0.25 * lvgi).diff().diff().diff()


def f46_amnp_128_earnings_management_score_d3(netinc, ncfo, assets, receivables, inventory):
    acc = _safe_div(netinc - ncfo, assets)
    acc_z = _rolling_zscore(acc, 8, min_periods=3)
    rec_z = _rolling_zscore(receivables, 8, min_periods=3)
    inv_z = _rolling_zscore(inventory, 8, min_periods=3)
    return (acc_z + rec_z + inv_z).diff().diff().diff()


def f46_amnp_129_red_flag_count_8q_d3(receivables, revenue, gp, assetsc, ppnenet, assets,
                                depamor, sgna, debt, liabilitiesc, cashneq):
    dsri = _safe_div(_safe_div(receivables, revenue), _safe_div(receivables.shift(4), revenue.shift(4)))
    gmi = _safe_div(_safe_div(gp.shift(4), revenue.shift(4)), _safe_div(gp, revenue))
    aqi = _safe_div(1.0 - _safe_div(assetsc + ppnenet, assets),
                    1.0 - _safe_div(assetsc.shift(4) + ppnenet.shift(4), assets.shift(4)))
    sgi = _safe_div(revenue, revenue.shift(4))
    depi = _safe_div(_safe_div(depamor.shift(4), depamor.shift(4) + ppnenet.shift(4)),
                     _safe_div(depamor, depamor + ppnenet))
    sgai = _safe_div(_safe_div(sgna, revenue), _safe_div(sgna.shift(4), revenue.shift(4)))
    lvgi = _safe_div(_safe_div(debt + liabilitiesc, assets),
                     _safe_div(debt.shift(4) + liabilitiesc.shift(4), assets.shift(4)))
    tata = _safe_div((receivables - receivables.shift(4)) - (cashneq - cashneq.shift(4)) - depamor, assets)
    m = (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
         + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    flag = (m > -2.22).astype(float)
    return (flag.rolling(8, min_periods=2).sum()).diff().diff().diff()


def f46_amnp_130_quality_of_earnings_index_8q_mean_d3(ncfo, netinc):
    return (_safe_div(ncfo, netinc).rolling(8, min_periods=3).mean()).diff().diff().diff()


def f46_amnp_131_cash_flow_quality_8q_slope_d3(ncfo, netinc):
    return (_rolling_slope(_safe_div(ncfo, netinc), 8, min_periods=3)).diff().diff().diff()


def f46_amnp_132_cash_flow_quality_drawdown_from_8q_max_d3(ncfo, netinc):
    q = _safe_div(ncfo, netinc)
    rmax = q.rolling(8, min_periods=3).max()
    return (_safe_div(q, rmax) - 1.0).diff().diff().diff()


def f46_amnp_133_sales_growth_minus_assets_growth_yoy_d3(revenue, assets):
    return (_yoy_pct(revenue) - _yoy_pct(assets)).diff().diff().diff()


def f46_amnp_134_assets_growth_minus_equity_growth_yoy_d3(assets, equity):
    return (_yoy_pct(assets) - _yoy_pct(equity)).diff().diff().diff()


def f46_amnp_135_cash_burn_vs_reported_earnings_yoy_d3(ncfo, netinc):
    s = -(ncfo - netinc)
    return (s - s.shift(4)).diff().diff().diff()


def f46_amnp_136_negative_accrual_consec_streak_d3(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (_consec_streak_neg(acc, 16)).diff().diff().diff()


def f46_amnp_137_positive_accrual_consec_streak_d3(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (_consec_streak_pos(acc, 16)).diff().diff().diff()


def f46_amnp_138_accrual_persistence_above_zero_8q_d3(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    flag = (acc > 0).astype(float)
    return (flag.rolling(8, min_periods=3).mean()).diff().diff().diff()


def f46_amnp_139_m_score_red_flag_consec_streak_d3(receivables, revenue, gp, assetsc, ppnenet, assets,
                                              depamor, sgna, debt, liabilitiesc, cashneq):
    dsri = _safe_div(_safe_div(receivables, revenue), _safe_div(receivables.shift(4), revenue.shift(4)))
    gmi = _safe_div(_safe_div(gp.shift(4), revenue.shift(4)), _safe_div(gp, revenue))
    aqi = _safe_div(1.0 - _safe_div(assetsc + ppnenet, assets),
                    1.0 - _safe_div(assetsc.shift(4) + ppnenet.shift(4), assets.shift(4)))
    sgi = _safe_div(revenue, revenue.shift(4))
    depi = _safe_div(_safe_div(depamor.shift(4), depamor.shift(4) + ppnenet.shift(4)),
                     _safe_div(depamor, depamor + ppnenet))
    sgai = _safe_div(_safe_div(sgna, revenue), _safe_div(sgna.shift(4), revenue.shift(4)))
    lvgi = _safe_div(_safe_div(debt + liabilitiesc, assets),
                     _safe_div(debt.shift(4) + liabilitiesc.shift(4), assets.shift(4)))
    tata = _safe_div((receivables - receivables.shift(4)) - (cashneq - cashneq.shift(4)) - depamor, assets)
    m = (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
         + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    flag = (m > -2.22).astype(float) - 0.5  # positive when red
    return (_consec_streak_pos(flag, 16)).diff().diff().diff()


def f46_amnp_140_quality_growth_proxy_d3(revenue, receivables):
    return (_yoy_pct(revenue) - _yoy_pct(receivables)).diff().diff().diff()


def f46_amnp_141_fictitious_sales_proxy_indicator_d3(receivables, revenue):
    rec_g = _yoy_pct(receivables)
    rev_g = _yoy_pct(revenue)
    cond = ((rec_g > 2.0 * rev_g) & (rev_g > 0)).astype(float)
    return (cond).diff().diff().diff()


def f46_amnp_142_cookie_jar_reserve_proxy_d3(deferredrev, revenue):
    z = _rolling_zscore(_safe_div(deferredrev, _ttm(revenue)), 8, min_periods=3)
    return ((z < -1.0).astype(float)).diff().diff().diff()


def f46_amnp_143_expense_capitalization_proxy_indicator_d3(ppnenet, opex):
    return ((_qoq_pct(ppnenet) > _qoq_pct(opex)).astype(float)).diff().diff().diff()


def f46_amnp_144_revenue_pull_forward_proxy_d3(revenue, receivables):
    rev_qoq = _qoq_pct(revenue)
    rec_qoq = _qoq_pct(receivables)
    cond = ((rev_qoq > rev_qoq.rolling(4, min_periods=2).mean()) & (rec_qoq > rev_qoq)).astype(float)
    return (cond).diff().diff().diff()


def f46_amnp_145_expense_understatement_proxy_d3(opex, cogs):
    return ((_yoy_pct(opex) < _yoy_pct(cogs)).astype(float)).diff().diff().diff()


def f46_amnp_146_tax_avoidance_proxy_d3(taxexp, ebit):
    r = _safe_div(taxexp, ebit)
    return (r - r.shift(4)).diff().diff().diff()


def f46_amnp_147_one_time_charge_proxy_d3(netinc, opinc):
    return (_safe_div((netinc - opinc).abs(), netinc.abs())).diff().diff().diff()


def f46_amnp_148_earnings_smoothing_proxy_d3(netinc, revenue):
    margin = _safe_div(netinc, revenue)
    sd = margin.rolling(8, min_periods=3).std()
    return (_safe_div(1.0, 1.0 + sd)).diff().diff().diff()


def f46_amnp_149_cash_disconnect_index_8q_max_d3(ncfo, netinc, assets):
    s = _safe_div((ncfo - netinc).abs(), assets)
    return (s.rolling(8, min_periods=3).max()).diff().diff().diff()


def f46_amnp_150_accounting_red_flag_terminal_signal_d3(receivables, revenue, gp, assetsc, ppnenet, assets,
                                                   depamor, sgna, debt, liabilitiesc, cashneq, netinc, ncfo):
    dsri = _safe_div(_safe_div(receivables, revenue), _safe_div(receivables.shift(4), revenue.shift(4)))
    gmi = _safe_div(_safe_div(gp.shift(4), revenue.shift(4)), _safe_div(gp, revenue))
    aqi = _safe_div(1.0 - _safe_div(assetsc + ppnenet, assets),
                    1.0 - _safe_div(assetsc.shift(4) + ppnenet.shift(4), assets.shift(4)))
    sgi = _safe_div(revenue, revenue.shift(4))
    depi = _safe_div(_safe_div(depamor.shift(4), depamor.shift(4) + ppnenet.shift(4)),
                     _safe_div(depamor, depamor + ppnenet))
    sgai = _safe_div(_safe_div(sgna, revenue), _safe_div(sgna.shift(4), revenue.shift(4)))
    lvgi = _safe_div(_safe_div(debt + liabilitiesc, assets),
                     _safe_div(debt.shift(4) + liabilitiesc.shift(4), assets.shift(4)))
    tata = _safe_div((receivables - receivables.shift(4)) - (cashneq - cashneq.shift(4)) - depamor, assets)
    m = (-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi
         + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)
    acc = _safe_div(netinc - ncfo, assets)
    pos_streak = _consec_streak_pos(acc, 16)
    cond = ((m > -2.22) & (pos_streak >= 4) & (_yoy_pct(receivables) > _yoy_pct(revenue))).astype(float)
    return (cond).diff().diff().diff()


ACCOUNTING_MANIPULATION_D3_REGISTRY_076_150 = {
    "f46_amnp_076_inventory_buildup_above_revenue_persistence_4q_d3": {"inputs": ["inventory", "revenue"], "func": f46_amnp_076_inventory_buildup_above_revenue_persistence_4q_d3},
    "f46_amnp_077_inventory_zscore_12q_d3": {"inputs": ["inventory"], "func": f46_amnp_077_inventory_zscore_12q_d3},
    "f46_amnp_078_inventory_breach_of_8q_max_indicator_d3": {"inputs": ["inventory"], "func": f46_amnp_078_inventory_breach_of_8q_max_indicator_d3},
    "f46_amnp_079_inventory_growth_acceleration_d3": {"inputs": ["inventory"], "func": f46_amnp_079_inventory_growth_acceleration_d3},
    "f46_amnp_080_inventory_growth_consec_above_rev_growth_streak_d3": {"inputs": ["inventory", "revenue"], "func": f46_amnp_080_inventory_growth_consec_above_rev_growth_streak_d3},
    "f46_amnp_081_inventory_to_payables_ratio_qoq_change_d3": {"inputs": ["inventory", "payables"], "func": f46_amnp_081_inventory_to_payables_ratio_qoq_change_d3},
    "f46_amnp_082_ar_plus_inventory_growth_minus_rev_growth_yoy_d3": {"inputs": ["receivables", "inventory", "revenue"], "func": f46_amnp_082_ar_plus_inventory_growth_minus_rev_growth_yoy_d3},
    "f46_amnp_083_ar_plus_inventory_to_revenue_yoy_change_d3": {"inputs": ["receivables", "inventory", "revenue"], "func": f46_amnp_083_ar_plus_inventory_to_revenue_yoy_change_d3},
    "f46_amnp_084_inventory_writedown_risk_proxy_d3": {"inputs": ["inventory", "cogs"], "func": f46_amnp_084_inventory_writedown_risk_proxy_d3},
    "f46_amnp_085_inventory_ttm_avg_growth_yoy_d3": {"inputs": ["inventory"], "func": f46_amnp_085_inventory_ttm_avg_growth_yoy_d3},
    "f46_amnp_086_capex_to_depamor_ratio_d3": {"inputs": ["capex", "depamor"], "func": f46_amnp_086_capex_to_depamor_ratio_d3},
    "f46_amnp_087_capex_to_depamor_qoq_change_d3": {"inputs": ["capex", "depamor"], "func": f46_amnp_087_capex_to_depamor_qoq_change_d3},
    "f46_amnp_088_capex_to_depamor_zscore_8q_d3": {"inputs": ["capex", "depamor"], "func": f46_amnp_088_capex_to_depamor_zscore_8q_d3},
    "f46_amnp_089_depamor_to_ppnenet_ratio_d3": {"inputs": ["depamor", "ppnenet"], "func": f46_amnp_089_depamor_to_ppnenet_ratio_d3},
    "f46_amnp_090_depamor_to_ppnenet_yoy_change_d3": {"inputs": ["depamor", "ppnenet"], "func": f46_amnp_090_depamor_to_ppnenet_yoy_change_d3},
    "f46_amnp_091_ppnenet_growth_minus_revenue_growth_yoy_d3": {"inputs": ["ppnenet", "revenue"], "func": f46_amnp_091_ppnenet_growth_minus_revenue_growth_yoy_d3},
    "f46_amnp_092_capex_yoy_pct_d3": {"inputs": ["capex"], "func": f46_amnp_092_capex_yoy_pct_d3},
    "f46_amnp_093_capex_qoq_pct_d3": {"inputs": ["capex"], "func": f46_amnp_093_capex_qoq_pct_d3},
    "f46_amnp_094_capex_8q_slope_d3": {"inputs": ["capex"], "func": f46_amnp_094_capex_8q_slope_d3},
    "f46_amnp_095_intangibles_to_assets_ratio_d3": {"inputs": ["intangibles", "assets"], "func": f46_amnp_095_intangibles_to_assets_ratio_d3},
    "f46_amnp_096_intangibles_yoy_pct_d3": {"inputs": ["intangibles"], "func": f46_amnp_096_intangibles_yoy_pct_d3},
    "f46_amnp_097_intangibles_growth_minus_revenue_growth_yoy_d3": {"inputs": ["intangibles", "revenue"], "func": f46_amnp_097_intangibles_growth_minus_revenue_growth_yoy_d3},
    "f46_amnp_098_intangibles_zscore_8q_d3": {"inputs": ["intangibles"], "func": f46_amnp_098_intangibles_zscore_8q_d3},
    "f46_amnp_099_capitalized_costs_proxy_qoq_d3": {"inputs": ["ppnenet", "intangibles", "revenue"], "func": f46_amnp_099_capitalized_costs_proxy_qoq_d3},
    "f46_amnp_100_depamor_share_of_revenue_d3": {"inputs": ["depamor", "revenue"], "func": f46_amnp_100_depamor_share_of_revenue_d3},
    "f46_amnp_101_depamor_share_of_revenue_qoq_change_d3": {"inputs": ["depamor", "revenue"], "func": f46_amnp_101_depamor_share_of_revenue_qoq_change_d3},
    "f46_amnp_102_impairment_risk_proxy_indicator_d3": {"inputs": ["ppnenet"], "func": f46_amnp_102_impairment_risk_proxy_indicator_d3},
    "f46_amnp_103_goodwill_proxy_growth_d3": {"inputs": ["intangibles"], "func": f46_amnp_103_goodwill_proxy_growth_d3},
    "f46_amnp_104_asset_quality_index_qoq_change_d3": {"inputs": ["assetsc", "ppnenet", "assets"], "func": f46_amnp_104_asset_quality_index_qoq_change_d3},
    "f46_amnp_105_asset_quality_index_8q_slope_d3": {"inputs": ["assetsc", "ppnenet", "assets"], "func": f46_amnp_105_asset_quality_index_8q_slope_d3},
    "f46_amnp_106_deferredrev_to_revenue_zscore_8q_d3": {"inputs": ["deferredrev", "revenue"], "func": f46_amnp_106_deferredrev_to_revenue_zscore_8q_d3},
    "f46_amnp_107_deferredrev_qoq_pct_d3": {"inputs": ["deferredrev"], "func": f46_amnp_107_deferredrev_qoq_pct_d3},
    "f46_amnp_108_deferredrev_yoy_pct_d3": {"inputs": ["deferredrev"], "func": f46_amnp_108_deferredrev_yoy_pct_d3},
    "f46_amnp_109_deferredrev_growth_minus_revenue_growth_yoy_d3": {"inputs": ["deferredrev", "revenue"], "func": f46_amnp_109_deferredrev_growth_minus_revenue_growth_yoy_d3},
    "f46_amnp_110_deferredrev_drawdown_from_8q_max_d3": {"inputs": ["deferredrev"], "func": f46_amnp_110_deferredrev_drawdown_from_8q_max_d3},
    "f46_amnp_111_deferredrev_decay_4q_d3": {"inputs": ["deferredrev"], "func": f46_amnp_111_deferredrev_decay_4q_d3},
    "f46_amnp_112_liabilities_to_assets_qoq_change_d3": {"inputs": ["liabilities", "assets"], "func": f46_amnp_112_liabilities_to_assets_qoq_change_d3},
    "f46_amnp_113_liabilities_to_assets_zscore_8q_d3": {"inputs": ["liabilities", "assets"], "func": f46_amnp_113_liabilities_to_assets_zscore_8q_d3},
    "f46_amnp_114_currentliab_to_currentassets_qoq_change_d3": {"inputs": ["liabilitiesc", "assetsc"], "func": f46_amnp_114_currentliab_to_currentassets_qoq_change_d3},
    "f46_amnp_115_payables_to_cogs_ratio_d3": {"inputs": ["payables", "cogs"], "func": f46_amnp_115_payables_to_cogs_ratio_d3},
    "f46_amnp_116_payables_to_cogs_yoy_change_d3": {"inputs": ["payables", "cogs"], "func": f46_amnp_116_payables_to_cogs_yoy_change_d3},
    "f46_amnp_117_payables_growth_minus_cogs_growth_yoy_d3": {"inputs": ["payables", "cogs"], "func": f46_amnp_117_payables_growth_minus_cogs_growth_yoy_d3},
    "f46_amnp_118_payables_stretching_proxy_d3": {"inputs": ["payables", "cogs"], "func": f46_amnp_118_payables_stretching_proxy_d3},
    "f46_amnp_119_payables_share_of_liabilities_yoy_change_d3": {"inputs": ["payables", "liabilities"], "func": f46_amnp_119_payables_share_of_liabilities_yoy_change_d3},
    "f46_amnp_120_liabilities_growth_persistence_above_assets_4q_d3": {"inputs": ["liabilities", "assets"], "func": f46_amnp_120_liabilities_growth_persistence_above_assets_4q_d3},
    "f46_amnp_121_shortterm_debt_buildup_proxy_d3": {"inputs": ["liabilitiesc"], "func": f46_amnp_121_shortterm_debt_buildup_proxy_d3},
    "f46_amnp_122_shortterm_debt_share_yoy_change_d3": {"inputs": ["liabilitiesc", "liabilities"], "func": f46_amnp_122_shortterm_debt_share_yoy_change_d3},
    "f46_amnp_123_accrued_liabilities_proxy_qoq_d3": {"inputs": ["liabilitiesc", "payables", "deferredrev"], "func": f46_amnp_123_accrued_liabilities_proxy_qoq_d3},
    "f46_amnp_124_liabilities_zscore_12q_d3": {"inputs": ["liabilities"], "func": f46_amnp_124_liabilities_zscore_12q_d3},
    "f46_amnp_125_debt_growth_minus_revenue_growth_yoy_d3": {"inputs": ["debt", "revenue"], "func": f46_amnp_125_debt_growth_minus_revenue_growth_yoy_d3},
    "f46_amnp_126_piotroski_reverse_count_d3": {"inputs": ["netinc", "ncfo", "assets", "revenue", "gp"], "func": f46_amnp_126_piotroski_reverse_count_d3},
    "f46_amnp_127_dechow_f_score_proxy_d3": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq", "netinc", "ncfo"], "func": f46_amnp_127_dechow_f_score_proxy_d3},
    "f46_amnp_128_earnings_management_score_d3": {"inputs": ["netinc", "ncfo", "assets", "receivables", "inventory"], "func": f46_amnp_128_earnings_management_score_d3},
    "f46_amnp_129_red_flag_count_8q_d3": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq"], "func": f46_amnp_129_red_flag_count_8q_d3},
    "f46_amnp_130_quality_of_earnings_index_8q_mean_d3": {"inputs": ["ncfo", "netinc"], "func": f46_amnp_130_quality_of_earnings_index_8q_mean_d3},
    "f46_amnp_131_cash_flow_quality_8q_slope_d3": {"inputs": ["ncfo", "netinc"], "func": f46_amnp_131_cash_flow_quality_8q_slope_d3},
    "f46_amnp_132_cash_flow_quality_drawdown_from_8q_max_d3": {"inputs": ["ncfo", "netinc"], "func": f46_amnp_132_cash_flow_quality_drawdown_from_8q_max_d3},
    "f46_amnp_133_sales_growth_minus_assets_growth_yoy_d3": {"inputs": ["revenue", "assets"], "func": f46_amnp_133_sales_growth_minus_assets_growth_yoy_d3},
    "f46_amnp_134_assets_growth_minus_equity_growth_yoy_d3": {"inputs": ["assets", "equity"], "func": f46_amnp_134_assets_growth_minus_equity_growth_yoy_d3},
    "f46_amnp_135_cash_burn_vs_reported_earnings_yoy_d3": {"inputs": ["ncfo", "netinc"], "func": f46_amnp_135_cash_burn_vs_reported_earnings_yoy_d3},
    "f46_amnp_136_negative_accrual_consec_streak_d3": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_136_negative_accrual_consec_streak_d3},
    "f46_amnp_137_positive_accrual_consec_streak_d3": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_137_positive_accrual_consec_streak_d3},
    "f46_amnp_138_accrual_persistence_above_zero_8q_d3": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_138_accrual_persistence_above_zero_8q_d3},
    "f46_amnp_139_m_score_red_flag_consec_streak_d3": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq"], "func": f46_amnp_139_m_score_red_flag_consec_streak_d3},
    "f46_amnp_140_quality_growth_proxy_d3": {"inputs": ["revenue", "receivables"], "func": f46_amnp_140_quality_growth_proxy_d3},
    "f46_amnp_141_fictitious_sales_proxy_indicator_d3": {"inputs": ["receivables", "revenue"], "func": f46_amnp_141_fictitious_sales_proxy_indicator_d3},
    "f46_amnp_142_cookie_jar_reserve_proxy_d3": {"inputs": ["deferredrev", "revenue"], "func": f46_amnp_142_cookie_jar_reserve_proxy_d3},
    "f46_amnp_143_expense_capitalization_proxy_indicator_d3": {"inputs": ["ppnenet", "opex"], "func": f46_amnp_143_expense_capitalization_proxy_indicator_d3},
    "f46_amnp_144_revenue_pull_forward_proxy_d3": {"inputs": ["revenue", "receivables"], "func": f46_amnp_144_revenue_pull_forward_proxy_d3},
    "f46_amnp_145_expense_understatement_proxy_d3": {"inputs": ["opex", "cogs"], "func": f46_amnp_145_expense_understatement_proxy_d3},
    "f46_amnp_146_tax_avoidance_proxy_d3": {"inputs": ["taxexp", "ebit"], "func": f46_amnp_146_tax_avoidance_proxy_d3},
    "f46_amnp_147_one_time_charge_proxy_d3": {"inputs": ["netinc", "opinc"], "func": f46_amnp_147_one_time_charge_proxy_d3},
    "f46_amnp_148_earnings_smoothing_proxy_d3": {"inputs": ["netinc", "revenue"], "func": f46_amnp_148_earnings_smoothing_proxy_d3},
    "f46_amnp_149_cash_disconnect_index_8q_max_d3": {"inputs": ["ncfo", "netinc", "assets"], "func": f46_amnp_149_cash_disconnect_index_8q_max_d3},
    "f46_amnp_150_accounting_red_flag_terminal_signal_d3": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq", "netinc", "ncfo"], "func": f46_amnp_150_accounting_red_flag_terminal_signal_d3},
}
