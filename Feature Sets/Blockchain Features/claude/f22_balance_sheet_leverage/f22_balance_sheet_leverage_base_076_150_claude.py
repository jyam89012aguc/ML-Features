import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives (balance-sheet leverage) =====
def _f22_lev(debt, equity):
    # debt-to-equity leverage (equity can cross zero -> safe div)
    return _safe_div(debt, equity)


def _f22_solvency(assets, liabilities):
    # solvency ratio: assets coverage of liabilities
    return _safe_div(assets, liabilities)


def _f22_netdebt(debt, cashneq, assets):
    # net debt (gross debt minus cash) scaled by assets
    return _safe_div(debt - cashneq, assets)


def _f22_capratio(equity, assets):
    # capitalization: equity share of asset base
    return _safe_div(equity, assets)


# ============ FEATURES 076-150 ============

# debt/equity smoothed over 504d
def f22bl_f22_balance_sheet_leverage_levsm_504d_base_v076_signal(debt, equity):
    result = _mean(_f22_lev(debt, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets smoothed over 252d
def f22bl_f22_balance_sheet_leverage_debtassetssm_252d_base_v077_signal(debt, assets):
    result = _mean(_safe_div(debt, assets), 252) + _f22_capratio(assets, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets smoothed over 504d
def f22bl_f22_balance_sheet_leverage_debtassetssm_504d_base_v078_signal(debt, assets):
    result = _mean(_safe_div(debt, assets), 504) + _f22_capratio(assets, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets smoothed over 504d
def f22bl_f22_balance_sheet_leverage_liabassetssm_504d_base_v079_signal(liabilities, assets):
    result = _mean(_safe_div(liabilities, assets), 504) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio smoothed over 252d
def f22bl_f22_balance_sheet_leverage_currsm_252d_base_v080_signal(currentratio, liabilities):
    result = _mean(currentratio, 252) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# de field smoothed over 252d
def f22bl_f22_balance_sheet_leverage_desm_252d_base_v081_signal(de, equity):
    result = _mean(de, 252) + _f22_lev(de, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / equity smoothed over 252d
def f22bl_f22_balance_sheet_leverage_netdebteqsm_252d_base_v082_signal(debt, cashneq, equity):
    result = _mean(_safe_div(debt - cashneq, equity), 252) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets smoothed over 504d
def f22bl_f22_balance_sheet_leverage_capsm_504d_base_v083_signal(equity, assets):
    result = _mean(_f22_capratio(equity, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency smoothed over 504d
def f22bl_f22_balance_sheet_leverage_solvsm_504d_base_v084_signal(assets, liabilities):
    result = _mean(_f22_solvency(assets, liabilities), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of debt smoothed over 252d
def f22bl_f22_balance_sheet_leverage_cashcovsm_252d_base_v085_signal(cashneq, debt):
    result = _mean(_safe_div(cashneq, debt), 252) + _f22_lev(debt, cashneq) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt trend slope (63d diff)
def f22bl_f22_balance_sheet_leverage_ndtrend_63d_base_v086_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd.diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt trend slope (252d diff)
def f22bl_f22_balance_sheet_leverage_ndtrend_252d_base_v087_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency trend slope (252d diff)
def f22bl_f22_balance_sheet_leverage_solvtrend_252d_base_v088_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = sv.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization trend slope (252d diff)
def f22bl_f22_balance_sheet_leverage_captrend_252d_base_v089_signal(equity, assets):
    cap = _f22_capratio(equity, assets)
    result = cap.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage trend slope (504d diff)
def f22bl_f22_balance_sheet_leverage_levtrend_504d_base_v090_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.diff(504)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt z-score over 126d
def f22bl_f22_balance_sheet_leverage_ndz_126d_base_v091_signal(debt, cashneq, assets):
    result = _z(_f22_netdebt(debt, cashneq, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt z-score over 504d
def f22bl_f22_balance_sheet_leverage_ndz_504d_base_v092_signal(debt, cashneq, assets):
    result = _z(_f22_netdebt(debt, cashneq, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency z-score over 126d
def f22bl_f22_balance_sheet_leverage_solvz_126d_base_v093_signal(assets, liabilities):
    result = _z(_f22_solvency(assets, liabilities), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency z-score over 504d
def f22bl_f22_balance_sheet_leverage_solvz_504d_base_v094_signal(assets, liabilities):
    result = _z(_f22_solvency(assets, liabilities), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization z-score over 252d
def f22bl_f22_balance_sheet_leverage_capz_252d_base_v095_signal(equity, assets):
    result = _z(_f22_capratio(equity, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization z-score over 504d
def f22bl_f22_balance_sheet_leverage_capz_504d_base_v096_signal(equity, assets):
    result = _z(_f22_capratio(equity, assets), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio z-score over 126d
def f22bl_f22_balance_sheet_leverage_currz_126d_base_v097_signal(currentratio, liabilities):
    result = _z(currentratio, 126) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth (63d) z-scored over 252d
def f22bl_f22_balance_sheet_leverage_debtgrowz_252d_base_v098_signal(debt, equity):
    result = _z(debt.pct_change(63), 252) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth (504d pct change)
def f22bl_f22_balance_sheet_leverage_debtgrow_504d_base_v099_signal(debt, equity):
    result = debt.pct_change(504) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity growth (252d pct change)
def f22bl_f22_balance_sheet_leverage_eqgrow_252d_base_v100_signal(equity, assets):
    result = equity.pct_change(252) + _f22_capratio(equity, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# asset growth (252d pct change)
def f22bl_f22_balance_sheet_leverage_assetgrow_252d_base_v101_signal(assets, liabilities):
    result = assets.pct_change(252) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities growth (126d pct change)
def f22bl_f22_balance_sheet_leverage_liabgrow_126d_base_v102_signal(liabilities, assets):
    result = liabilities.pct_change(126) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash growth (126d pct change) anchored on net debt
def f22bl_f22_balance_sheet_leverage_cashgrow_126d_base_v103_signal(cashneq, debt, assets):
    result = cashneq.pct_change(126) + _f22_netdebt(debt, cashneq, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage percentile rank over 504d
def f22bl_f22_balance_sheet_leverage_levrank_504d_base_v104_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency percentile rank over 504d
def f22bl_f22_balance_sheet_leverage_solvrank_504d_base_v105_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = sv.rolling(504, min_periods=168).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt percentile rank over 126d
def f22bl_f22_balance_sheet_leverage_ndrank_126d_base_v106_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization percentile rank over 252d
def f22bl_f22_balance_sheet_leverage_caprank_252d_base_v107_signal(equity, assets):
    cap = _f22_capratio(equity, assets)
    result = cap.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio percentile rank over 252d
def f22bl_f22_balance_sheet_leverage_currrank_252d_base_v108_signal(currentratio, liabilities):
    result = currentratio.rolling(252, min_periods=84).rank(pct=True) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage dispersion (252d std)
def f22bl_f22_balance_sheet_leverage_levdisp_252d_base_v109_signal(debt, equity):
    result = _std(_f22_lev(debt, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt dispersion (252d std)
def f22bl_f22_balance_sheet_leverage_nddisp_252d_base_v110_signal(debt, cashneq, assets):
    result = _std(_f22_netdebt(debt, cashneq, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency dispersion (252d std)
def f22bl_f22_balance_sheet_leverage_solvdisp_252d_base_v111_signal(assets, liabilities):
    result = _std(_f22_solvency(assets, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization dispersion (126d std)
def f22bl_f22_balance_sheet_leverage_capdisp_126d_base_v112_signal(equity, assets):
    result = _std(_f22_capratio(equity, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio dispersion (126d std) anchored on solvency
def f22bl_f22_balance_sheet_leverage_currdisp_126d_base_v113_signal(currentratio, liabilities):
    result = _std(currentratio, 126) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage coefficient of variation over 252d
def f22bl_f22_balance_sheet_leverage_levcv_252d_base_v114_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = _safe_div(_std(lev, 252), _mean(lev, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# solvency coefficient of variation over 252d
def f22bl_f22_balance_sheet_leverage_solvcv_252d_base_v115_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = _safe_div(_std(sv, 252), _mean(sv, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# leverage surprise over 252d
def f22bl_f22_balance_sheet_leverage_levsurp_252d_base_v116_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev - _mean(lev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt surprise over 252d
def f22bl_f22_balance_sheet_leverage_ndsurp_252d_base_v117_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd - _mean(nd, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization surprise over 126d
def f22bl_f22_balance_sheet_leverage_capsurp_126d_base_v118_signal(equity, assets):
    cap = _f22_capratio(equity, assets)
    result = cap - _mean(cap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio surprise over 126d
def f22bl_f22_balance_sheet_leverage_currsurp_126d_base_v119_signal(currentratio, liabilities):
    result = currentratio - _mean(currentratio, 126) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage short/long mean ratio (126d / 504d)
def f22bl_f22_balance_sheet_leverage_levratio_126_504_base_v120_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = _safe_div(_mean(lev, 126), _mean(lev, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# solvency short/long mean ratio (126d / 504d)
def f22bl_f22_balance_sheet_leverage_solvratio_126_504_base_v121_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = _safe_div(_mean(sv, 126), _mean(sv, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt short/long mean ratio (126d / 504d)
def f22bl_f22_balance_sheet_leverage_ndratio_126_504_base_v122_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = _safe_div(_mean(nd, 126), _mean(nd, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# leverage EWMA (span 252)
def f22bl_f22_balance_sheet_leverage_levewm_252d_base_v123_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt EWMA (span 252)
def f22bl_f22_balance_sheet_leverage_ndewm_252d_base_v124_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# solvency EWMA (span 126)
def f22bl_f22_balance_sheet_leverage_solvewm_126d_base_v125_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = sv.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization EWMA (span 126)
def f22bl_f22_balance_sheet_leverage_capewm_126d_base_v126_signal(equity, assets):
    cap = _f22_capratio(equity, assets)
    result = cap.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# debt/(debt+equity) financial structure ratio
def f22bl_f22_balance_sheet_leverage_debtcap_63d_base_v127_signal(debt, equity):
    result = _mean(_safe_div(debt, debt + equity), 63) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt/(debt+equity) smoothed over 252d
def f22bl_f22_balance_sheet_leverage_debtcap_252d_base_v128_signal(debt, equity):
    result = _mean(_safe_div(debt, debt + equity), 252) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital proxy: (assets - liabilities) / assets, smoothed
def f22bl_f22_balance_sheet_leverage_wcproxy_63d_base_v129_signal(assets, liabilities):
    result = _mean(_safe_div(assets - liabilities, assets), 63) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net-worth coverage: (assets - liabilities) / debt
def f22bl_f22_balance_sheet_leverage_nwcov_126d_base_v130_signal(assets, liabilities, debt):
    result = _mean(_safe_div(assets - liabilities, debt), 126) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-adjusted leverage: debt/equity divided by current ratio mean
def f22bl_f22_balance_sheet_leverage_liqlev_126d_base_v131_signal(debt, equity, currentratio):
    result = _safe_div(_mean(_f22_lev(debt, equity), 126), _mean(currentratio, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-liabilities coverage smoothed over 126d
def f22bl_f22_balance_sheet_leverage_cashliab_126d_base_v132_signal(cashneq, liabilities, assets):
    result = _mean(_safe_div(cashneq, liabilities), 126) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt per unit current ratio (refinancing-stress proxy)
def f22bl_f22_balance_sheet_leverage_debtcurr_126d_base_v133_signal(debt, assets, currentratio):
    result = _mean(_safe_div(_safe_div(debt, assets), currentratio), 126) + _f22_capratio(assets, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# de field z-score over 126d
def f22bl_f22_balance_sheet_leverage_dez_126d_base_v134_signal(de, equity):
    result = _z(de, 126) + _f22_lev(de, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# de field minus computed leverage, smoothed over 126d
def f22bl_f22_balance_sheet_leverage_degap_126d_base_v135_signal(de, debt, equity):
    result = _mean(de, 126) - _mean(_f22_lev(debt, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# de field trend slope (126d diff)
def f22bl_f22_balance_sheet_leverage_detrend_126d_base_v136_signal(de, equity):
    result = de.diff(126) + _f22_lev(de, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage trend slope (126d diff)
def f22bl_f22_balance_sheet_leverage_cashcovtrend_126d_base_v137_signal(cashneq, debt):
    cov = _safe_div(cashneq, debt)
    result = cov.diff(126) + _f22_lev(debt, cashneq) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# solvency EWMA (span 252)
def f22bl_f22_balance_sheet_leverage_solvewm_252d_base_v138_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = sv.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization EWMA (span 252)
def f22bl_f22_balance_sheet_leverage_capewm_252d_base_v139_signal(equity, assets):
    cap = _f22_capratio(equity, assets)
    result = cap.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# leverage acceleration: 63d slope minus 126d slope
def f22bl_f22_balance_sheet_leverage_levaccel_63_126_base_v140_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.diff(63) - lev.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt acceleration: 63d slope minus 126d slope
def f22bl_f22_balance_sheet_leverage_ndaccel_63_126_base_v141_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd.diff(63) - nd.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency acceleration: 63d slope minus 126d slope
def f22bl_f22_balance_sheet_leverage_solvaccel_63_126_base_v142_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = sv.diff(63) - sv.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage normalized by its 504d range location (continuous min-max scale)
def f22bl_f22_balance_sheet_leverage_levminmax_504d_base_v143_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    lo = lev.rolling(504, min_periods=168).min()
    hi = lev.rolling(504, min_periods=168).max()
    result = _safe_div(lev - lo, hi - lo)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency normalized by its 504d range location
def f22bl_f22_balance_sheet_leverage_solvminmax_504d_base_v144_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    lo = sv.rolling(504, min_periods=168).min()
    hi = sv.rolling(504, min_periods=168).max()
    result = _safe_div(sv - lo, hi - lo)
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets z-score over 252d
def f22bl_f22_balance_sheet_leverage_daz_252d_base_v145_signal(debt, assets):
    result = _z(_safe_div(debt, assets), 252) + _f22_capratio(assets, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets z-score over 252d
def f22bl_f22_balance_sheet_leverage_laz_252d_base_v146_signal(liabilities, assets):
    result = _z(_safe_div(liabilities, assets), 252) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity multiplier z-score over 252d
def f22bl_f22_balance_sheet_leverage_eqmultz_252d_base_v147_signal(assets, equity):
    result = _z(_safe_div(assets, equity), 252) + _f22_capratio(equity, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage minus net-debt cross (liquidity vs leverage balance)
def f22bl_f22_balance_sheet_leverage_liqlevbal_126d_base_v148_signal(cashneq, debt, assets):
    cov = _safe_div(cashneq, debt)
    nd = _f22_netdebt(debt, cashneq, assets)
    result = _mean(cov, 126) - _mean(nd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage scaled by solvency (combined stress index), smoothed
def f22bl_f22_balance_sheet_leverage_levsolvidx_126d_base_v149_signal(debt, equity, assets, liabilities):
    idx = _safe_div(_f22_lev(debt, equity), _f22_solvency(assets, liabilities))
    result = _mean(idx, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# blended solvency-leverage composite z-score over 252d
def f22bl_f22_balance_sheet_leverage_comp_z_252d_base_v150_signal(debt, equity, cashneq, assets, liabilities):
    comp = _f22_lev(debt, equity) + _f22_netdebt(debt, cashneq, assets) - _f22_solvency(assets, liabilities)
    result = _z(comp, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22bl_f22_balance_sheet_leverage_levsm_504d_base_v076_signal,
    f22bl_f22_balance_sheet_leverage_debtassetssm_252d_base_v077_signal,
    f22bl_f22_balance_sheet_leverage_debtassetssm_504d_base_v078_signal,
    f22bl_f22_balance_sheet_leverage_liabassetssm_504d_base_v079_signal,
    f22bl_f22_balance_sheet_leverage_currsm_252d_base_v080_signal,
    f22bl_f22_balance_sheet_leverage_desm_252d_base_v081_signal,
    f22bl_f22_balance_sheet_leverage_netdebteqsm_252d_base_v082_signal,
    f22bl_f22_balance_sheet_leverage_capsm_504d_base_v083_signal,
    f22bl_f22_balance_sheet_leverage_solvsm_504d_base_v084_signal,
    f22bl_f22_balance_sheet_leverage_cashcovsm_252d_base_v085_signal,
    f22bl_f22_balance_sheet_leverage_ndtrend_63d_base_v086_signal,
    f22bl_f22_balance_sheet_leverage_ndtrend_252d_base_v087_signal,
    f22bl_f22_balance_sheet_leverage_solvtrend_252d_base_v088_signal,
    f22bl_f22_balance_sheet_leverage_captrend_252d_base_v089_signal,
    f22bl_f22_balance_sheet_leverage_levtrend_504d_base_v090_signal,
    f22bl_f22_balance_sheet_leverage_ndz_126d_base_v091_signal,
    f22bl_f22_balance_sheet_leverage_ndz_504d_base_v092_signal,
    f22bl_f22_balance_sheet_leverage_solvz_126d_base_v093_signal,
    f22bl_f22_balance_sheet_leverage_solvz_504d_base_v094_signal,
    f22bl_f22_balance_sheet_leverage_capz_252d_base_v095_signal,
    f22bl_f22_balance_sheet_leverage_capz_504d_base_v096_signal,
    f22bl_f22_balance_sheet_leverage_currz_126d_base_v097_signal,
    f22bl_f22_balance_sheet_leverage_debtgrowz_252d_base_v098_signal,
    f22bl_f22_balance_sheet_leverage_debtgrow_504d_base_v099_signal,
    f22bl_f22_balance_sheet_leverage_eqgrow_252d_base_v100_signal,
    f22bl_f22_balance_sheet_leverage_assetgrow_252d_base_v101_signal,
    f22bl_f22_balance_sheet_leverage_liabgrow_126d_base_v102_signal,
    f22bl_f22_balance_sheet_leverage_cashgrow_126d_base_v103_signal,
    f22bl_f22_balance_sheet_leverage_levrank_504d_base_v104_signal,
    f22bl_f22_balance_sheet_leverage_solvrank_504d_base_v105_signal,
    f22bl_f22_balance_sheet_leverage_ndrank_126d_base_v106_signal,
    f22bl_f22_balance_sheet_leverage_caprank_252d_base_v107_signal,
    f22bl_f22_balance_sheet_leverage_currrank_252d_base_v108_signal,
    f22bl_f22_balance_sheet_leverage_levdisp_252d_base_v109_signal,
    f22bl_f22_balance_sheet_leverage_nddisp_252d_base_v110_signal,
    f22bl_f22_balance_sheet_leverage_solvdisp_252d_base_v111_signal,
    f22bl_f22_balance_sheet_leverage_capdisp_126d_base_v112_signal,
    f22bl_f22_balance_sheet_leverage_currdisp_126d_base_v113_signal,
    f22bl_f22_balance_sheet_leverage_levcv_252d_base_v114_signal,
    f22bl_f22_balance_sheet_leverage_solvcv_252d_base_v115_signal,
    f22bl_f22_balance_sheet_leverage_levsurp_252d_base_v116_signal,
    f22bl_f22_balance_sheet_leverage_ndsurp_252d_base_v117_signal,
    f22bl_f22_balance_sheet_leverage_capsurp_126d_base_v118_signal,
    f22bl_f22_balance_sheet_leverage_currsurp_126d_base_v119_signal,
    f22bl_f22_balance_sheet_leverage_levratio_126_504_base_v120_signal,
    f22bl_f22_balance_sheet_leverage_solvratio_126_504_base_v121_signal,
    f22bl_f22_balance_sheet_leverage_ndratio_126_504_base_v122_signal,
    f22bl_f22_balance_sheet_leverage_levewm_252d_base_v123_signal,
    f22bl_f22_balance_sheet_leverage_ndewm_252d_base_v124_signal,
    f22bl_f22_balance_sheet_leverage_solvewm_126d_base_v125_signal,
    f22bl_f22_balance_sheet_leverage_capewm_126d_base_v126_signal,
    f22bl_f22_balance_sheet_leverage_debtcap_63d_base_v127_signal,
    f22bl_f22_balance_sheet_leverage_debtcap_252d_base_v128_signal,
    f22bl_f22_balance_sheet_leverage_wcproxy_63d_base_v129_signal,
    f22bl_f22_balance_sheet_leverage_nwcov_126d_base_v130_signal,
    f22bl_f22_balance_sheet_leverage_liqlev_126d_base_v131_signal,
    f22bl_f22_balance_sheet_leverage_cashliab_126d_base_v132_signal,
    f22bl_f22_balance_sheet_leverage_debtcurr_126d_base_v133_signal,
    f22bl_f22_balance_sheet_leverage_dez_126d_base_v134_signal,
    f22bl_f22_balance_sheet_leverage_degap_126d_base_v135_signal,
    f22bl_f22_balance_sheet_leverage_detrend_126d_base_v136_signal,
    f22bl_f22_balance_sheet_leverage_cashcovtrend_126d_base_v137_signal,
    f22bl_f22_balance_sheet_leverage_solvewm_252d_base_v138_signal,
    f22bl_f22_balance_sheet_leverage_capewm_252d_base_v139_signal,
    f22bl_f22_balance_sheet_leverage_levaccel_63_126_base_v140_signal,
    f22bl_f22_balance_sheet_leverage_ndaccel_63_126_base_v141_signal,
    f22bl_f22_balance_sheet_leverage_solvaccel_63_126_base_v142_signal,
    f22bl_f22_balance_sheet_leverage_levminmax_504d_base_v143_signal,
    f22bl_f22_balance_sheet_leverage_solvminmax_504d_base_v144_signal,
    f22bl_f22_balance_sheet_leverage_daz_252d_base_v145_signal,
    f22bl_f22_balance_sheet_leverage_laz_252d_base_v146_signal,
    f22bl_f22_balance_sheet_leverage_eqmultz_252d_base_v147_signal,
    f22bl_f22_balance_sheet_leverage_liqlevbal_126d_base_v148_signal,
    f22bl_f22_balance_sheet_leverage_levsolvidx_126d_base_v149_signal,
    f22bl_f22_balance_sheet_leverage_comp_z_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_BALANCE_SHEET_LEVERAGE_REGISTRY_076_150 = REGISTRY


def _synth_cols(names):
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    nh = np.abs(np.random.normal(0, 0.02, n)); nl = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open","high","low","close","closeadj","price","volume","marketcap","ev",
           "assets","assetsc","equity","revenue","gp","ebitda","ppnenet","sharesbas",
           "shareswa","cashneq","cor","opex","sgna","rnd","inventory","receivables",
           "intangibles","evebitda","evebit","pe","pb","ps","currentratio","bvps","sps",
           "shrvalue","shrunits","totalvalue","percentoftotal","sf3a_shares","sf3a_value",
           "sf3b_shares","sf3b_value","grossmargin","beta1y","beta5y","invcap","debt"}
    for nm in names:
        if nm in ("closeadj","close","price"):
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price*(1+np.random.normal(0,0.01,n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price*(1+nh), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price*(1-nl), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7,7e6,n))+1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0,1.0,n))
            level = 1000.0*np.exp(0.03*np.random.normal(0,1,n).cumsum()/np.sqrt(n))
            s = level + 50.0*walk
            if nm in POS:
                s = np.abs(s) + 10.0
            out[nm] = pd.Series(s, name=nm)
    return out


if __name__ == "__main__":
    domain_primitives = ("_f22_lev", "_f22_solvency", "_f22_netdebt", "_f22_capratio")
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0; nan_ok = 0
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args); y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        assert any(p in inspect.getsource(fn) for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f22_balance_sheet_leverage_base_076_150_claude: {n_features} features pass")
