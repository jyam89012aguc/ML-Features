"""accounting_manipulation d2 features 001_075 — order-2 difference of corresponding base feature.

Each function inlines the base body and wraps the final return with .diff().diff(). Self-contained per HANDOFF.
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


def f46_amnp_001_sloan_accruals_to_assets_d2(netinc, ncfo, assets):
    return (_safe_div(netinc - ncfo, assets)).diff().diff()


def f46_amnp_002_sloan_accruals_ttm_to_assets_d2(netinc, ncfo, assets):
    return (_safe_div(_ttm(netinc) - _ttm(ncfo), assets)).diff().diff()


def f46_amnp_003_earnings_quality_ratio_d2(ncfo, netinc):
    return (_safe_div(ncfo, netinc)).diff().diff()


def f46_amnp_004_earnings_quality_ttm_d2(ncfo, netinc):
    return (_safe_div(_ttm(ncfo), _ttm(netinc))).diff().diff()


def f46_amnp_005_cash_minus_accrual_to_revenue_d2(ncfo, netinc, revenue):
    return (_safe_div(ncfo - netinc, _ttm(revenue).abs())).diff().diff()


def f46_amnp_006_accruals_4q_change_d2(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (acc - acc.shift(4)).diff().diff()


def f46_amnp_007_accruals_qoq_change_d2(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (acc.diff()).diff().diff()


def f46_amnp_008_log_abs_accruals_d2(netinc, ncfo):
    return (np.log((netinc - ncfo).abs() + 1.0)).diff().diff()


def f46_amnp_009_accruals_yoy_pct_d2(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (_yoy_pct(acc)).diff().diff()


def f46_amnp_010_accruals_volatility_8q_d2(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (acc.rolling(8, min_periods=3).std()).diff().diff()


def f46_amnp_011_accruals_negative_consec_streak_d2(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (_consec_streak_neg(acc, 16)).diff().diff()


def f46_amnp_012_accruals_positive_consec_streak_d2(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (_consec_streak_pos(acc, 16)).diff().diff()


def f46_amnp_013_accruals_zscore_8q_d2(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (_rolling_zscore(acc, 8, min_periods=3)).diff().diff()


def f46_amnp_014_accruals_zscore_12q_d2(netinc, ncfo, assets):
    acc = _safe_div(netinc - ncfo, assets)
    return (_rolling_zscore(acc, 12, min_periods=4)).diff().diff()


def f46_amnp_015_earnings_quality_8q_slope_d2(ncfo, netinc):
    eq = _safe_div(ncfo, netinc)
    return (_rolling_slope(eq, 8, min_periods=3)).diff().diff()


def f46_amnp_016_ncfo_minus_netinc_to_assets_ttm_d2(ncfo, netinc, assets):
    return (_safe_div(_ttm(ncfo) - _ttm(netinc), assets)).diff().diff()


def f46_amnp_017_ncfo_minus_netinc_to_equity_d2(ncfo, netinc, equity):
    return (_safe_div(ncfo - netinc, equity.abs())).diff().diff()


def f46_amnp_018_ncfo_minus_netinc_to_revenue_ttm_d2(ncfo, netinc, revenue):
    return (_safe_div(_ttm(ncfo) - _ttm(netinc), _ttm(revenue).abs())).diff().diff()


def f46_amnp_019_cash_conversion_qoq_change_d2(ncfo, netinc):
    cc = _safe_div(ncfo, netinc)
    return (cc.diff()).diff().diff()


def f46_amnp_020_nonoperating_accrual_proxy_d2(ncfo, netinc, depamor, assets):
    return (_safe_div(ncfo - netinc - depamor, assets)).diff().diff()


def f46_amnp_021_dsri_d2(receivables, revenue):
    cur = _safe_div(receivables, revenue)
    prv = _safe_div(receivables.shift(4), revenue.shift(4))
    return (_safe_div(cur, prv)).diff().diff()


def f46_amnp_022_gmi_d2(gp, revenue):
    prv = _safe_div(gp.shift(4), revenue.shift(4))
    cur = _safe_div(gp, revenue)
    return (_safe_div(prv, cur)).diff().diff()


def f46_amnp_023_aqi_d2(assetsc, ppnenet, assets):
    cur = 1.0 - _safe_div(assetsc + ppnenet, assets)
    prv = 1.0 - _safe_div(assetsc.shift(4) + ppnenet.shift(4), assets.shift(4))
    return (_safe_div(cur, prv)).diff().diff()


def f46_amnp_024_sgi_d2(revenue):
    return (_safe_div(revenue, revenue.shift(4))).diff().diff()


def f46_amnp_025_depi_d2(depamor, ppnenet):
    prv = _safe_div(depamor.shift(4), depamor.shift(4) + ppnenet.shift(4))
    cur = _safe_div(depamor, depamor + ppnenet)
    return (_safe_div(prv, cur)).diff().diff()


def f46_amnp_026_sgai_d2(sgna, revenue):
    cur = _safe_div(sgna, revenue)
    prv = _safe_div(sgna.shift(4), revenue.shift(4))
    return (_safe_div(cur, prv)).diff().diff()


def f46_amnp_027_lvgi_d2(debt, liabilitiesc, assets):
    cur = _safe_div(debt + liabilitiesc, assets)
    prv = _safe_div(debt.shift(4) + liabilitiesc.shift(4), assets.shift(4))
    return (_safe_div(cur, prv)).diff().diff()


def f46_amnp_028_tata_to_assets_d2(receivables, cashneq, depamor, assets):
    return (_safe_div((receivables - receivables.shift(4)) - (cashneq - cashneq.shift(4)) - depamor, assets)).diff().diff()


def f46_amnp_029_beneish_m_score_proxy_d2(receivables, revenue, gp, assetsc, ppnenet, assets,
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
    return ((-4.84 + 0.92 * dsri + 0.528 * gmi + 0.404 * aqi + 0.892 * sgi).diff().diff()
            + 0.115 * depi - 0.172 * sgai + 4.679 * tata - 0.327 * lvgi)


def f46_amnp_030_m_score_4q_slope_d2(receivables, revenue, gp, assetsc, ppnenet, assets,
                               depamor, sgna, debt, liabilitiesc, cashneq):
    m = f46_amnp_029_beneish_m_score_proxy_d2(receivables, revenue, gp, assetsc, ppnenet,
                                       assets, depamor, sgna, debt, liabilitiesc, cashneq)
    return (_rolling_slope(m, 4, min_periods=2)).diff().diff()


def f46_amnp_031_m_score_yoy_change_d2(receivables, revenue, gp, assetsc, ppnenet, assets,
                                 depamor, sgna, debt, liabilitiesc, cashneq):
    m = f46_amnp_029_beneish_m_score_proxy_d2(receivables, revenue, gp, assetsc, ppnenet,
                                       assets, depamor, sgna, debt, liabilitiesc, cashneq)
    return (m - m.shift(4)).diff().diff()


def f46_amnp_032_dsri_qoq_change_d2(receivables, revenue):
    dsri = _safe_div(_safe_div(receivables, revenue), _safe_div(receivables.shift(4), revenue.shift(4)))
    return (dsri.diff()).diff().diff()


def f46_amnp_033_gmi_qoq_change_d2(gp, revenue):
    gmi = _safe_div(_safe_div(gp.shift(4), revenue.shift(4)), _safe_div(gp, revenue))
    return (gmi.diff()).diff().diff()


def f46_amnp_034_sgi_qoq_change_d2(revenue):
    return (_safe_div(revenue, revenue.shift(4)).diff()).diff().diff()


def f46_amnp_035_sgai_qoq_change_d2(sgna, revenue):
    sgai = _safe_div(_safe_div(sgna, revenue), _safe_div(sgna.shift(4), revenue.shift(4)))
    return (sgai.diff()).diff().diff()


def f46_amnp_036_lvgi_qoq_change_d2(debt, liabilitiesc, assets):
    lvgi = _safe_div(_safe_div(debt + liabilitiesc, assets),
                     _safe_div(debt.shift(4) + liabilitiesc.shift(4), assets.shift(4)))
    return (lvgi.diff()).diff().diff()


def f46_amnp_037_m_score_above_neg_2_22_count_8q_d2(receivables, revenue, gp, assetsc, ppnenet, assets,
                                              depamor, sgna, debt, liabilitiesc, cashneq):
    m = f46_amnp_029_beneish_m_score_proxy_d2(receivables, revenue, gp, assetsc, ppnenet,
                                       assets, depamor, sgna, debt, liabilitiesc, cashneq)
    flag = (m > -2.22).astype(float)
    return (flag.rolling(8, min_periods=2).sum()).diff().diff()


def f46_amnp_038_dsri_above_1_4_count_8q_d2(receivables, revenue):
    dsri = _safe_div(_safe_div(receivables, revenue), _safe_div(receivables.shift(4), revenue.shift(4)))
    flag = (dsri > 1.4).astype(float)
    return (flag.rolling(8, min_periods=2).sum()).diff().diff()


def f46_amnp_039_tata_qoq_change_d2(receivables, cashneq, depamor, assets):
    tata = _safe_div((receivables - receivables.shift(4)) - (cashneq - cashneq.shift(4)) - depamor, assets)
    return (tata.diff()).diff().diff()


def f46_amnp_040_tata_zscore_8q_d2(receivables, cashneq, depamor, assets):
    tata = _safe_div((receivables - receivables.shift(4)) - (cashneq - cashneq.shift(4)) - depamor, assets)
    return (_rolling_zscore(tata, 8, min_periods=3)).diff().diff()


def f46_amnp_041_m_score_4q_minus_8q_mean_diff_d2(receivables, revenue, gp, assetsc, ppnenet, assets,
                                             depamor, sgna, debt, liabilitiesc, cashneq):
    m = f46_amnp_029_beneish_m_score_proxy_d2(receivables, revenue, gp, assetsc, ppnenet,
                                       assets, depamor, sgna, debt, liabilitiesc, cashneq)
    return (m.rolling(4, min_periods=2).mean() - m.rolling(8, min_periods=3).mean()).diff().diff()


def f46_amnp_042_m_score_acceleration_d2(receivables, revenue, gp, assetsc, ppnenet, assets,
                                   depamor, sgna, debt, liabilitiesc, cashneq):
    m = f46_amnp_029_beneish_m_score_proxy_d2(receivables, revenue, gp, assetsc, ppnenet,
                                       assets, depamor, sgna, debt, liabilitiesc, cashneq)
    return (m.diff().diff()).diff().diff()


def f46_amnp_043_depi_qoq_change_d2(depamor, ppnenet):
    depi = _safe_div(_safe_div(depamor.shift(4), depamor.shift(4) + ppnenet.shift(4)),
                     _safe_div(depamor, depamor + ppnenet))
    return (depi.diff()).diff().diff()


def f46_amnp_044_depi_above_1_count_4q_d2(depamor, ppnenet):
    depi = _safe_div(_safe_div(depamor.shift(4), depamor.shift(4) + ppnenet.shift(4)),
                     _safe_div(depamor, depamor + ppnenet))
    flag = (depi > 1.0).astype(float)
    return (flag.rolling(4, min_periods=2).sum()).diff().diff()


def f46_amnp_045_lvgi_8q_slope_d2(debt, liabilitiesc, assets):
    lvgi = _safe_div(_safe_div(debt + liabilitiesc, assets),
                     _safe_div(debt.shift(4) + liabilitiesc.shift(4), assets.shift(4)))
    return (_rolling_slope(lvgi, 8, min_periods=3)).diff().diff()


def f46_amnp_046_receivables_to_revenue_ttm_zscore_8q_d2(receivables, revenue):
    ratio = _safe_div(receivables, _ttm(revenue))
    return (_rolling_zscore(ratio, 8, min_periods=3)).diff().diff()


def f46_amnp_047_dso_jump_d2(receivables, revenue):
    cur = _safe_div(receivables, revenue)
    prv = _safe_div(receivables.shift(1), revenue.shift(1))
    return (cur - prv).diff().diff()


def f46_amnp_048_dso_8q_slope_d2(receivables, revenue):
    dso = _safe_div(receivables, revenue)
    return (_rolling_slope(dso, 8, min_periods=3)).diff().diff()


def f46_amnp_049_receivables_yoy_pct_minus_revenue_yoy_pct_d2(receivables, revenue):
    return (_yoy_pct(receivables) - _yoy_pct(revenue)).diff().diff()


def f46_amnp_050_receivables_qoq_pct_minus_revenue_qoq_pct_d2(receivables, revenue):
    return (_qoq_pct(receivables) - _qoq_pct(revenue)).diff().diff()


def f46_amnp_051_receivables_share_of_assets_yoy_change_d2(receivables, assets):
    share = _safe_div(receivables, assets)
    return (share - share.shift(4)).diff().diff()


def f46_amnp_052_receivables_share_of_assets_zscore_8q_d2(receivables, assets):
    share = _safe_div(receivables, assets)
    return (_rolling_zscore(share, 8, min_periods=3)).diff().diff()


def f46_amnp_053_receivables_8q_slope_d2(receivables):
    return (_rolling_slope(receivables, 8, min_periods=3)).diff().diff()


def f46_amnp_054_receivables_to_revenue_drawup_from_8q_min_d2(receivables, revenue):
    ratio = _safe_div(receivables, _ttm(revenue))
    rmin = ratio.rolling(8, min_periods=3).min()
    return (_safe_div(ratio - rmin, rmin.abs())).diff().diff()


def f46_amnp_055_receivables_q_minus_ttm_avg_share_d2(receivables, revenue):
    ratio = _safe_div(receivables, _ttm(revenue))
    return (ratio - ratio.rolling(4, min_periods=2).mean()).diff().diff()


def f46_amnp_056_receivables_zscore_12q_d2(receivables):
    return (_rolling_zscore(receivables, 12, min_periods=4)).diff().diff()


def f46_amnp_057_receivables_growth_4q_consec_positive_d2(receivables):
    qoq = receivables.diff()
    return (_consec_streak_pos(qoq, 4)).diff().diff()


def f46_amnp_058_receivables_8q_acceleration_d2(receivables):
    return (_qoq_pct(receivables).diff()).diff().diff()


def f46_amnp_059_receivables_breach_of_8q_max_indicator_d2(receivables):
    rmax = receivables.rolling(8, min_periods=3).max().shift(1)
    return ((receivables > rmax).astype(float)).diff().diff()


def f46_amnp_060_delta_receivables_to_delta_revenue_yoy_d2(receivables, revenue):
    return (_safe_div(receivables - receivables.shift(4), (revenue - revenue.shift(4)).abs())).diff().diff()


def f46_amnp_061_receivables_to_payables_ratio_d2(receivables, payables):
    return (_safe_div(receivables, payables)).diff().diff()


def f46_amnp_062_receivables_to_payables_qoq_change_d2(receivables, payables):
    return (_safe_div(receivables, payables).diff()).diff().diff()


def f46_amnp_063_receivables_yoy_pct_above_30pct_indicator_d2(receivables):
    return ((_yoy_pct(receivables) > 0.30).astype(float)).diff().diff()


def f46_amnp_064_receivables_growth_persistence_above_rev_growth_4q_d2(receivables, revenue):
    flag = (_yoy_pct(receivables) > _yoy_pct(revenue)).astype(float)
    return (flag.rolling(4, min_periods=2).sum()).diff().diff()


def f46_amnp_065_receivables_growth_persistence_above_rev_growth_8q_d2(receivables, revenue):
    flag = (_yoy_pct(receivables) > _yoy_pct(revenue)).astype(float)
    return (flag.rolling(8, min_periods=3).sum()).diff().diff()


def f46_amnp_066_inventory_to_revenue_ttm_zscore_8q_d2(inventory, revenue):
    ratio = _safe_div(inventory, _ttm(revenue))
    return (_rolling_zscore(ratio, 8, min_periods=3)).diff().diff()


def f46_amnp_067_dio_jump_d2(inventory, cogs):
    dio = _safe_div(inventory, _ttm(cogs))
    return (dio.diff()).diff().diff()


def f46_amnp_068_inventory_growth_minus_cogs_growth_yoy_d2(inventory, cogs):
    return (_yoy_pct(inventory) - _yoy_pct(cogs)).diff().diff()


def f46_amnp_069_inventory_growth_minus_revenue_growth_yoy_d2(inventory, revenue):
    return (_yoy_pct(inventory) - _yoy_pct(revenue)).diff().diff()


def f46_amnp_070_inventory_8q_slope_d2(inventory):
    return (_rolling_slope(inventory, 8, min_periods=3)).diff().diff()


def f46_amnp_071_inventory_share_of_assets_yoy_change_d2(inventory, assets):
    share = _safe_div(inventory, assets)
    return (share - share.shift(4)).diff().diff()


def f46_amnp_072_inventory_share_of_assets_zscore_8q_d2(inventory, assets):
    share = _safe_div(inventory, assets)
    return (_rolling_zscore(share, 8, min_periods=3)).diff().diff()


def f46_amnp_073_inventory_qoq_pct_minus_revenue_qoq_pct_d2(inventory, revenue):
    return (_qoq_pct(inventory) - _qoq_pct(revenue)).diff().diff()


def f46_amnp_074_inventory_to_assets_drawup_from_8q_min_d2(inventory, assets):
    share = _safe_div(inventory, assets)
    smin = share.rolling(8, min_periods=3).min()
    return (_safe_div(share - smin, smin.abs())).diff().diff()


def f46_amnp_075_inventory_yoy_pct_above_30pct_indicator_d2(inventory):
    return ((_yoy_pct(inventory) > 0.30).astype(float)).diff().diff()


ACCOUNTING_MANIPULATION_D2_REGISTRY_001_075 = {
    "f46_amnp_001_sloan_accruals_to_assets_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_001_sloan_accruals_to_assets_d2},
    "f46_amnp_002_sloan_accruals_ttm_to_assets_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_002_sloan_accruals_ttm_to_assets_d2},
    "f46_amnp_003_earnings_quality_ratio_d2": {"inputs": ["ncfo", "netinc"], "func": f46_amnp_003_earnings_quality_ratio_d2},
    "f46_amnp_004_earnings_quality_ttm_d2": {"inputs": ["ncfo", "netinc"], "func": f46_amnp_004_earnings_quality_ttm_d2},
    "f46_amnp_005_cash_minus_accrual_to_revenue_d2": {"inputs": ["ncfo", "netinc", "revenue"], "func": f46_amnp_005_cash_minus_accrual_to_revenue_d2},
    "f46_amnp_006_accruals_4q_change_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_006_accruals_4q_change_d2},
    "f46_amnp_007_accruals_qoq_change_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_007_accruals_qoq_change_d2},
    "f46_amnp_008_log_abs_accruals_d2": {"inputs": ["netinc", "ncfo"], "func": f46_amnp_008_log_abs_accruals_d2},
    "f46_amnp_009_accruals_yoy_pct_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_009_accruals_yoy_pct_d2},
    "f46_amnp_010_accruals_volatility_8q_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_010_accruals_volatility_8q_d2},
    "f46_amnp_011_accruals_negative_consec_streak_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_011_accruals_negative_consec_streak_d2},
    "f46_amnp_012_accruals_positive_consec_streak_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_012_accruals_positive_consec_streak_d2},
    "f46_amnp_013_accruals_zscore_8q_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_013_accruals_zscore_8q_d2},
    "f46_amnp_014_accruals_zscore_12q_d2": {"inputs": ["netinc", "ncfo", "assets"], "func": f46_amnp_014_accruals_zscore_12q_d2},
    "f46_amnp_015_earnings_quality_8q_slope_d2": {"inputs": ["ncfo", "netinc"], "func": f46_amnp_015_earnings_quality_8q_slope_d2},
    "f46_amnp_016_ncfo_minus_netinc_to_assets_ttm_d2": {"inputs": ["ncfo", "netinc", "assets"], "func": f46_amnp_016_ncfo_minus_netinc_to_assets_ttm_d2},
    "f46_amnp_017_ncfo_minus_netinc_to_equity_d2": {"inputs": ["ncfo", "netinc", "equity"], "func": f46_amnp_017_ncfo_minus_netinc_to_equity_d2},
    "f46_amnp_018_ncfo_minus_netinc_to_revenue_ttm_d2": {"inputs": ["ncfo", "netinc", "revenue"], "func": f46_amnp_018_ncfo_minus_netinc_to_revenue_ttm_d2},
    "f46_amnp_019_cash_conversion_qoq_change_d2": {"inputs": ["ncfo", "netinc"], "func": f46_amnp_019_cash_conversion_qoq_change_d2},
    "f46_amnp_020_nonoperating_accrual_proxy_d2": {"inputs": ["ncfo", "netinc", "depamor", "assets"], "func": f46_amnp_020_nonoperating_accrual_proxy_d2},
    "f46_amnp_021_dsri_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_021_dsri_d2},
    "f46_amnp_022_gmi_d2": {"inputs": ["gp", "revenue"], "func": f46_amnp_022_gmi_d2},
    "f46_amnp_023_aqi_d2": {"inputs": ["assetsc", "ppnenet", "assets"], "func": f46_amnp_023_aqi_d2},
    "f46_amnp_024_sgi_d2": {"inputs": ["revenue"], "func": f46_amnp_024_sgi_d2},
    "f46_amnp_025_depi_d2": {"inputs": ["depamor", "ppnenet"], "func": f46_amnp_025_depi_d2},
    "f46_amnp_026_sgai_d2": {"inputs": ["sgna", "revenue"], "func": f46_amnp_026_sgai_d2},
    "f46_amnp_027_lvgi_d2": {"inputs": ["debt", "liabilitiesc", "assets"], "func": f46_amnp_027_lvgi_d2},
    "f46_amnp_028_tata_to_assets_d2": {"inputs": ["receivables", "cashneq", "depamor", "assets"], "func": f46_amnp_028_tata_to_assets_d2},
    "f46_amnp_029_beneish_m_score_proxy_d2": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq"], "func": f46_amnp_029_beneish_m_score_proxy_d2},
    "f46_amnp_030_m_score_4q_slope_d2": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq"], "func": f46_amnp_030_m_score_4q_slope_d2},
    "f46_amnp_031_m_score_yoy_change_d2": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq"], "func": f46_amnp_031_m_score_yoy_change_d2},
    "f46_amnp_032_dsri_qoq_change_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_032_dsri_qoq_change_d2},
    "f46_amnp_033_gmi_qoq_change_d2": {"inputs": ["gp", "revenue"], "func": f46_amnp_033_gmi_qoq_change_d2},
    "f46_amnp_034_sgi_qoq_change_d2": {"inputs": ["revenue"], "func": f46_amnp_034_sgi_qoq_change_d2},
    "f46_amnp_035_sgai_qoq_change_d2": {"inputs": ["sgna", "revenue"], "func": f46_amnp_035_sgai_qoq_change_d2},
    "f46_amnp_036_lvgi_qoq_change_d2": {"inputs": ["debt", "liabilitiesc", "assets"], "func": f46_amnp_036_lvgi_qoq_change_d2},
    "f46_amnp_037_m_score_above_neg_2_22_count_8q_d2": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq"], "func": f46_amnp_037_m_score_above_neg_2_22_count_8q_d2},
    "f46_amnp_038_dsri_above_1_4_count_8q_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_038_dsri_above_1_4_count_8q_d2},
    "f46_amnp_039_tata_qoq_change_d2": {"inputs": ["receivables", "cashneq", "depamor", "assets"], "func": f46_amnp_039_tata_qoq_change_d2},
    "f46_amnp_040_tata_zscore_8q_d2": {"inputs": ["receivables", "cashneq", "depamor", "assets"], "func": f46_amnp_040_tata_zscore_8q_d2},
    "f46_amnp_041_m_score_4q_minus_8q_mean_diff_d2": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq"], "func": f46_amnp_041_m_score_4q_minus_8q_mean_diff_d2},
    "f46_amnp_042_m_score_acceleration_d2": {"inputs": ["receivables", "revenue", "gp", "assetsc", "ppnenet", "assets", "depamor", "sgna", "debt", "liabilitiesc", "cashneq"], "func": f46_amnp_042_m_score_acceleration_d2},
    "f46_amnp_043_depi_qoq_change_d2": {"inputs": ["depamor", "ppnenet"], "func": f46_amnp_043_depi_qoq_change_d2},
    "f46_amnp_044_depi_above_1_count_4q_d2": {"inputs": ["depamor", "ppnenet"], "func": f46_amnp_044_depi_above_1_count_4q_d2},
    "f46_amnp_045_lvgi_8q_slope_d2": {"inputs": ["debt", "liabilitiesc", "assets"], "func": f46_amnp_045_lvgi_8q_slope_d2},
    "f46_amnp_046_receivables_to_revenue_ttm_zscore_8q_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_046_receivables_to_revenue_ttm_zscore_8q_d2},
    "f46_amnp_047_dso_jump_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_047_dso_jump_d2},
    "f46_amnp_048_dso_8q_slope_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_048_dso_8q_slope_d2},
    "f46_amnp_049_receivables_yoy_pct_minus_revenue_yoy_pct_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_049_receivables_yoy_pct_minus_revenue_yoy_pct_d2},
    "f46_amnp_050_receivables_qoq_pct_minus_revenue_qoq_pct_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_050_receivables_qoq_pct_minus_revenue_qoq_pct_d2},
    "f46_amnp_051_receivables_share_of_assets_yoy_change_d2": {"inputs": ["receivables", "assets"], "func": f46_amnp_051_receivables_share_of_assets_yoy_change_d2},
    "f46_amnp_052_receivables_share_of_assets_zscore_8q_d2": {"inputs": ["receivables", "assets"], "func": f46_amnp_052_receivables_share_of_assets_zscore_8q_d2},
    "f46_amnp_053_receivables_8q_slope_d2": {"inputs": ["receivables"], "func": f46_amnp_053_receivables_8q_slope_d2},
    "f46_amnp_054_receivables_to_revenue_drawup_from_8q_min_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_054_receivables_to_revenue_drawup_from_8q_min_d2},
    "f46_amnp_055_receivables_q_minus_ttm_avg_share_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_055_receivables_q_minus_ttm_avg_share_d2},
    "f46_amnp_056_receivables_zscore_12q_d2": {"inputs": ["receivables"], "func": f46_amnp_056_receivables_zscore_12q_d2},
    "f46_amnp_057_receivables_growth_4q_consec_positive_d2": {"inputs": ["receivables"], "func": f46_amnp_057_receivables_growth_4q_consec_positive_d2},
    "f46_amnp_058_receivables_8q_acceleration_d2": {"inputs": ["receivables"], "func": f46_amnp_058_receivables_8q_acceleration_d2},
    "f46_amnp_059_receivables_breach_of_8q_max_indicator_d2": {"inputs": ["receivables"], "func": f46_amnp_059_receivables_breach_of_8q_max_indicator_d2},
    "f46_amnp_060_delta_receivables_to_delta_revenue_yoy_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_060_delta_receivables_to_delta_revenue_yoy_d2},
    "f46_amnp_061_receivables_to_payables_ratio_d2": {"inputs": ["receivables", "payables"], "func": f46_amnp_061_receivables_to_payables_ratio_d2},
    "f46_amnp_062_receivables_to_payables_qoq_change_d2": {"inputs": ["receivables", "payables"], "func": f46_amnp_062_receivables_to_payables_qoq_change_d2},
    "f46_amnp_063_receivables_yoy_pct_above_30pct_indicator_d2": {"inputs": ["receivables"], "func": f46_amnp_063_receivables_yoy_pct_above_30pct_indicator_d2},
    "f46_amnp_064_receivables_growth_persistence_above_rev_growth_4q_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_064_receivables_growth_persistence_above_rev_growth_4q_d2},
    "f46_amnp_065_receivables_growth_persistence_above_rev_growth_8q_d2": {"inputs": ["receivables", "revenue"], "func": f46_amnp_065_receivables_growth_persistence_above_rev_growth_8q_d2},
    "f46_amnp_066_inventory_to_revenue_ttm_zscore_8q_d2": {"inputs": ["inventory", "revenue"], "func": f46_amnp_066_inventory_to_revenue_ttm_zscore_8q_d2},
    "f46_amnp_067_dio_jump_d2": {"inputs": ["inventory", "cogs"], "func": f46_amnp_067_dio_jump_d2},
    "f46_amnp_068_inventory_growth_minus_cogs_growth_yoy_d2": {"inputs": ["inventory", "cogs"], "func": f46_amnp_068_inventory_growth_minus_cogs_growth_yoy_d2},
    "f46_amnp_069_inventory_growth_minus_revenue_growth_yoy_d2": {"inputs": ["inventory", "revenue"], "func": f46_amnp_069_inventory_growth_minus_revenue_growth_yoy_d2},
    "f46_amnp_070_inventory_8q_slope_d2": {"inputs": ["inventory"], "func": f46_amnp_070_inventory_8q_slope_d2},
    "f46_amnp_071_inventory_share_of_assets_yoy_change_d2": {"inputs": ["inventory", "assets"], "func": f46_amnp_071_inventory_share_of_assets_yoy_change_d2},
    "f46_amnp_072_inventory_share_of_assets_zscore_8q_d2": {"inputs": ["inventory", "assets"], "func": f46_amnp_072_inventory_share_of_assets_zscore_8q_d2},
    "f46_amnp_073_inventory_qoq_pct_minus_revenue_qoq_pct_d2": {"inputs": ["inventory", "revenue"], "func": f46_amnp_073_inventory_qoq_pct_minus_revenue_qoq_pct_d2},
    "f46_amnp_074_inventory_to_assets_drawup_from_8q_min_d2": {"inputs": ["inventory", "assets"], "func": f46_amnp_074_inventory_to_assets_drawup_from_8q_min_d2},
    "f46_amnp_075_inventory_yoy_pct_above_30pct_indicator_d2": {"inputs": ["inventory"], "func": f46_amnp_075_inventory_yoy_pct_above_30pct_indicator_d2},
}
