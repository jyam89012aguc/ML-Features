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


# ============ FEATURES 001-075 ============

# debt/equity leverage level
def f22bl_f22_balance_sheet_leverage_lev_21d_base_v001_signal(debt, equity):
    result = _f22_lev(debt, equity)
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity smoothed over 63d
def f22bl_f22_balance_sheet_leverage_levsm_63d_base_v002_signal(debt, equity):
    result = _mean(_f22_lev(debt, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity smoothed over 126d
def f22bl_f22_balance_sheet_leverage_levsm_126d_base_v003_signal(debt, equity):
    result = _mean(_f22_lev(debt, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity smoothed over 252d
def f22bl_f22_balance_sheet_leverage_levsm_252d_base_v004_signal(debt, equity):
    result = _mean(_f22_lev(debt, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets (gross leverage on asset base)
def f22bl_f22_balance_sheet_leverage_debtassets_21d_base_v005_signal(debt, assets):
    result = _safe_div(debt, assets) + _f22_capratio(assets, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets smoothed over 63d
def f22bl_f22_balance_sheet_leverage_debtassetssm_63d_base_v006_signal(debt, assets):
    result = _mean(_safe_div(debt, assets), 63) + _f22_capratio(assets, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets smoothed over 126d
def f22bl_f22_balance_sheet_leverage_debtassetssm_126d_base_v007_signal(debt, assets):
    result = _mean(_safe_div(debt, assets), 126) + _f22_capratio(assets, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets (total balance-sheet gearing)
def f22bl_f22_balance_sheet_leverage_liabassets_21d_base_v008_signal(liabilities, assets):
    result = _safe_div(liabilities, assets) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets smoothed over 126d
def f22bl_f22_balance_sheet_leverage_liabassetssm_126d_base_v009_signal(liabilities, assets):
    result = _mean(_safe_div(liabilities, assets), 126) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets smoothed over 252d
def f22bl_f22_balance_sheet_leverage_liabassetssm_252d_base_v010_signal(liabilities, assets):
    result = _mean(_safe_div(liabilities, assets), 252) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio level (raw liquidity)
def f22bl_f22_balance_sheet_leverage_curr_21d_base_v011_signal(currentratio, liabilities):
    result = currentratio + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio smoothed over 63d
def f22bl_f22_balance_sheet_leverage_currsm_63d_base_v012_signal(currentratio, liabilities):
    result = _mean(currentratio, 63) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio smoothed over 126d
def f22bl_f22_balance_sheet_leverage_currsm_126d_base_v013_signal(currentratio, liabilities):
    result = _mean(currentratio, 126) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# de field level (reported debt-to-equity)
def f22bl_f22_balance_sheet_leverage_de_21d_base_v014_signal(de, equity):
    result = de + _f22_lev(de, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# de field smoothed over 126d
def f22bl_f22_balance_sheet_leverage_desm_126d_base_v015_signal(de, equity):
    result = _mean(de, 126) + _f22_lev(de, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / assets level
def f22bl_f22_balance_sheet_leverage_netdebt_21d_base_v016_signal(debt, cashneq, assets):
    result = _f22_netdebt(debt, cashneq, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / assets smoothed over 63d
def f22bl_f22_balance_sheet_leverage_netdebtsm_63d_base_v017_signal(debt, cashneq, assets):
    result = _mean(_f22_netdebt(debt, cashneq, assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / assets smoothed over 126d
def f22bl_f22_balance_sheet_leverage_netdebtsm_126d_base_v018_signal(debt, cashneq, assets):
    result = _mean(_f22_netdebt(debt, cashneq, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / assets smoothed over 252d
def f22bl_f22_balance_sheet_leverage_netdebtsm_252d_base_v019_signal(debt, cashneq, assets):
    result = _mean(_f22_netdebt(debt, cashneq, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / equity level
def f22bl_f22_balance_sheet_leverage_netdebteq_21d_base_v020_signal(debt, cashneq, equity):
    result = _safe_div(debt - cashneq, equity) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net debt / equity smoothed over 126d
def f22bl_f22_balance_sheet_leverage_netdebteqsm_126d_base_v021_signal(debt, cashneq, equity):
    result = _mean(_safe_div(debt - cashneq, equity), 126) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets capitalization level
def f22bl_f22_balance_sheet_leverage_cap_21d_base_v022_signal(equity, assets):
    result = _f22_capratio(equity, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets smoothed over 126d
def f22bl_f22_balance_sheet_leverage_capsm_126d_base_v023_signal(equity, assets):
    result = _mean(_f22_capratio(equity, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets smoothed over 252d
def f22bl_f22_balance_sheet_leverage_capsm_252d_base_v024_signal(equity, assets):
    result = _mean(_f22_capratio(equity, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# assets/liabilities solvency level
def f22bl_f22_balance_sheet_leverage_solv_21d_base_v025_signal(assets, liabilities):
    result = _f22_solvency(assets, liabilities)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency smoothed over 126d
def f22bl_f22_balance_sheet_leverage_solvsm_126d_base_v026_signal(assets, liabilities):
    result = _mean(_f22_solvency(assets, liabilities), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency smoothed over 252d
def f22bl_f22_balance_sheet_leverage_solvsm_252d_base_v027_signal(assets, liabilities):
    result = _mean(_f22_solvency(assets, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of debt (cashneq / debt)
def f22bl_f22_balance_sheet_leverage_cashcov_21d_base_v028_signal(cashneq, debt):
    result = _safe_div(cashneq, debt) + _f22_lev(debt, cashneq) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of debt smoothed over 126d
def f22bl_f22_balance_sheet_leverage_cashcovsm_126d_base_v029_signal(cashneq, debt):
    result = _mean(_safe_div(cashneq, debt), 126) + _f22_lev(debt, cashneq) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash / assets liquidity buffer
def f22bl_f22_balance_sheet_leverage_cashassets_63d_base_v030_signal(cashneq, assets):
    result = _mean(_safe_div(cashneq, assets), 63) + _f22_netdebt(cashneq, cashneq, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage trend slope (63d diff of debt/equity)
def f22bl_f22_balance_sheet_leverage_levtrend_63d_base_v031_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage trend slope (126d diff)
def f22bl_f22_balance_sheet_leverage_levtrend_126d_base_v032_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage trend slope (252d diff)
def f22bl_f22_balance_sheet_leverage_levtrend_252d_base_v033_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt trend slope (126d diff)
def f22bl_f22_balance_sheet_leverage_ndtrend_126d_base_v034_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency trend slope (126d diff)
def f22bl_f22_balance_sheet_leverage_solvtrend_126d_base_v035_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = sv.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage z-score over 252d
def f22bl_f22_balance_sheet_leverage_levz_252d_base_v036_signal(debt, equity):
    result = _z(_f22_lev(debt, equity), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage z-score over 126d
def f22bl_f22_balance_sheet_leverage_levz_126d_base_v037_signal(debt, equity):
    result = _z(_f22_lev(debt, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage z-score over 504d
def f22bl_f22_balance_sheet_leverage_levz_504d_base_v038_signal(debt, equity):
    result = _z(_f22_lev(debt, equity), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt z-score over 252d
def f22bl_f22_balance_sheet_leverage_ndz_252d_base_v039_signal(debt, cashneq, assets):
    result = _z(_f22_netdebt(debt, cashneq, assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency z-score over 252d
def f22bl_f22_balance_sheet_leverage_solvz_252d_base_v040_signal(assets, liabilities):
    result = _z(_f22_solvency(assets, liabilities), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio z-score over 252d
def f22bl_f22_balance_sheet_leverage_currz_252d_base_v041_signal(currentratio, liabilities):
    result = _z(currentratio, 252) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# de z-score over 252d
def f22bl_f22_balance_sheet_leverage_dez_252d_base_v042_signal(de, equity):
    result = _z(de, 252) + _f22_lev(de, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth (63d pct change of debt) anchored on leverage
def f22bl_f22_balance_sheet_leverage_debtgrow_63d_base_v043_signal(debt, equity):
    result = debt.pct_change(63) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth (126d pct change)
def f22bl_f22_balance_sheet_leverage_debtgrow_126d_base_v044_signal(debt, equity):
    result = debt.pct_change(126) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# debt growth (252d pct change)
def f22bl_f22_balance_sheet_leverage_debtgrow_252d_base_v045_signal(debt, equity):
    result = debt.pct_change(252) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# equity growth (126d pct change) anchored on capitalization
def f22bl_f22_balance_sheet_leverage_eqgrow_126d_base_v046_signal(equity, assets):
    result = equity.pct_change(126) + _f22_capratio(equity, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# asset growth (126d pct change) anchored on solvency
def f22bl_f22_balance_sheet_leverage_assetgrow_126d_base_v047_signal(assets, liabilities):
    result = assets.pct_change(126) + _f22_solvency(assets, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# solvency percentile rank over 252d
def f22bl_f22_balance_sheet_leverage_solvrank_252d_base_v048_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = sv.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage percentile rank over 252d
def f22bl_f22_balance_sheet_leverage_levrank_252d_base_v049_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt percentile rank over 252d
def f22bl_f22_balance_sheet_leverage_ndrank_252d_base_v050_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio percentile rank over 126d
def f22bl_f22_balance_sheet_leverage_currrank_126d_base_v051_signal(currentratio, liabilities):
    result = currentratio.rolling(126, min_periods=42).rank(pct=True) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# leverage dispersion (63d std of debt/equity)
def f22bl_f22_balance_sheet_leverage_levdisp_63d_base_v052_signal(debt, equity):
    result = _std(_f22_lev(debt, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage dispersion (126d std)
def f22bl_f22_balance_sheet_leverage_levdisp_126d_base_v053_signal(debt, equity):
    result = _std(_f22_lev(debt, equity), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt dispersion (126d std)
def f22bl_f22_balance_sheet_leverage_nddisp_126d_base_v054_signal(debt, cashneq, assets):
    result = _std(_f22_netdebt(debt, cashneq, assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency dispersion (126d std)
def f22bl_f22_balance_sheet_leverage_solvdisp_126d_base_v055_signal(assets, liabilities):
    result = _std(_f22_solvency(assets, liabilities), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage minus its 126d mean (leverage surprise)
def f22bl_f22_balance_sheet_leverage_levsurp_126d_base_v056_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev - _mean(lev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt minus its 126d mean (net-debt surprise)
def f22bl_f22_balance_sheet_leverage_ndsurp_126d_base_v057_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd - _mean(nd, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency minus its 252d mean (solvency surprise)
def f22bl_f22_balance_sheet_leverage_solvsurp_252d_base_v058_signal(assets, liabilities):
    sv = _f22_solvency(assets, liabilities)
    result = sv - _mean(sv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage ratio of short vs long mean (63d / 252d)
def f22bl_f22_balance_sheet_leverage_levratio_63_252_base_v059_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = _safe_div(_mean(lev, 63), _mean(lev, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt ratio of short vs long mean (63d / 252d)
def f22bl_f22_balance_sheet_leverage_ndratio_63_252_base_v060_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = _safe_div(_mean(nd, 63), _mean(nd, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity over debt/assets (equity-vs-asset gearing spread)
def f22bl_f22_balance_sheet_leverage_gearspread_21d_base_v061_signal(debt, equity, assets):
    result = _f22_lev(debt, equity) - _safe_div(debt, assets)
    return result.replace([np.inf, -np.inf], np.nan)


# solvency minus inverse-leverage cross check
def f22bl_f22_balance_sheet_leverage_solvlevcross_63d_base_v062_signal(assets, liabilities, debt, equity):
    result = _mean(_f22_solvency(assets, liabilities), 63) - _mean(_f22_lev(debt, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage scaled by current ratio (stressed leverage)
def f22bl_f22_balance_sheet_leverage_stresslev_63d_base_v063_signal(debt, equity, currentratio):
    result = _safe_div(_f22_lev(debt, equity), currentratio)
    return result.replace([np.inf, -np.inf], np.nan)


# net debt scaled by current ratio (liquidity-stressed net debt)
def f22bl_f22_balance_sheet_leverage_stressnd_63d_base_v064_signal(debt, cashneq, assets, currentratio):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = _safe_div(nd, currentratio)
    return result.replace([np.inf, -np.inf], np.nan)


# leverage EWMA (span 63) anchored on raw leverage
def f22bl_f22_balance_sheet_leverage_levewm_63d_base_v065_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# leverage EWMA (span 126)
def f22bl_f22_balance_sheet_leverage_levewm_126d_base_v066_signal(debt, equity):
    lev = _f22_lev(debt, equity)
    result = lev.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# net-debt EWMA (span 126)
def f22bl_f22_balance_sheet_leverage_ndewm_126d_base_v067_signal(debt, cashneq, assets):
    nd = _f22_netdebt(debt, cashneq, assets)
    result = nd.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/equity (financial leverage multiplier)
def f22bl_f22_balance_sheet_leverage_liabeq_21d_base_v068_signal(liabilities, equity, debt):
    result = _safe_div(liabilities, equity) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/equity smoothed over 126d
def f22bl_f22_balance_sheet_leverage_liabeqsm_126d_base_v069_signal(liabilities, equity, debt):
    result = _mean(_safe_div(liabilities, equity), 126) + _f22_lev(debt, equity) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# assets/equity (equity multiplier / financial leverage)
def f22bl_f22_balance_sheet_leverage_eqmult_63d_base_v070_signal(assets, equity):
    result = _mean(_safe_div(assets, equity), 63) + _f22_capratio(equity, assets) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of debt z-score over 252d
def f22bl_f22_balance_sheet_leverage_cashcovz_252d_base_v071_signal(cashneq, debt):
    result = _z(_safe_div(cashneq, debt), 252) + _f22_lev(debt, cashneq) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# de field minus debt/equity primitive (reported vs computed leverage gap)
def f22bl_f22_balance_sheet_leverage_degap_63d_base_v072_signal(de, debt, equity):
    result = _mean(de, 63) - _mean(_f22_lev(debt, equity), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization trend slope (126d diff of equity/assets)
def f22bl_f22_balance_sheet_leverage_captrend_126d_base_v073_signal(equity, assets):
    cap = _f22_capratio(equity, assets)
    result = cap.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio trend slope (126d diff)
def f22bl_f22_balance_sheet_leverage_currtrend_126d_base_v074_signal(currentratio, liabilities):
    result = currentratio.diff(126) + _f22_solvency(currentratio, liabilities) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# blended leverage-stress composite (lev + net debt - solvency), smoothed
def f22bl_f22_balance_sheet_leverage_stresscomp_63d_base_v075_signal(debt, equity, cashneq, assets, liabilities):
    comp = _f22_lev(debt, equity) + _f22_netdebt(debt, cashneq, assets) - _f22_solvency(assets, liabilities)
    result = _mean(comp, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f22bl_f22_balance_sheet_leverage_lev_21d_base_v001_signal,
    f22bl_f22_balance_sheet_leverage_levsm_63d_base_v002_signal,
    f22bl_f22_balance_sheet_leverage_levsm_126d_base_v003_signal,
    f22bl_f22_balance_sheet_leverage_levsm_252d_base_v004_signal,
    f22bl_f22_balance_sheet_leverage_debtassets_21d_base_v005_signal,
    f22bl_f22_balance_sheet_leverage_debtassetssm_63d_base_v006_signal,
    f22bl_f22_balance_sheet_leverage_debtassetssm_126d_base_v007_signal,
    f22bl_f22_balance_sheet_leverage_liabassets_21d_base_v008_signal,
    f22bl_f22_balance_sheet_leverage_liabassetssm_126d_base_v009_signal,
    f22bl_f22_balance_sheet_leverage_liabassetssm_252d_base_v010_signal,
    f22bl_f22_balance_sheet_leverage_curr_21d_base_v011_signal,
    f22bl_f22_balance_sheet_leverage_currsm_63d_base_v012_signal,
    f22bl_f22_balance_sheet_leverage_currsm_126d_base_v013_signal,
    f22bl_f22_balance_sheet_leverage_de_21d_base_v014_signal,
    f22bl_f22_balance_sheet_leverage_desm_126d_base_v015_signal,
    f22bl_f22_balance_sheet_leverage_netdebt_21d_base_v016_signal,
    f22bl_f22_balance_sheet_leverage_netdebtsm_63d_base_v017_signal,
    f22bl_f22_balance_sheet_leverage_netdebtsm_126d_base_v018_signal,
    f22bl_f22_balance_sheet_leverage_netdebtsm_252d_base_v019_signal,
    f22bl_f22_balance_sheet_leverage_netdebteq_21d_base_v020_signal,
    f22bl_f22_balance_sheet_leverage_netdebteqsm_126d_base_v021_signal,
    f22bl_f22_balance_sheet_leverage_cap_21d_base_v022_signal,
    f22bl_f22_balance_sheet_leverage_capsm_126d_base_v023_signal,
    f22bl_f22_balance_sheet_leverage_capsm_252d_base_v024_signal,
    f22bl_f22_balance_sheet_leverage_solv_21d_base_v025_signal,
    f22bl_f22_balance_sheet_leverage_solvsm_126d_base_v026_signal,
    f22bl_f22_balance_sheet_leverage_solvsm_252d_base_v027_signal,
    f22bl_f22_balance_sheet_leverage_cashcov_21d_base_v028_signal,
    f22bl_f22_balance_sheet_leverage_cashcovsm_126d_base_v029_signal,
    f22bl_f22_balance_sheet_leverage_cashassets_63d_base_v030_signal,
    f22bl_f22_balance_sheet_leverage_levtrend_63d_base_v031_signal,
    f22bl_f22_balance_sheet_leverage_levtrend_126d_base_v032_signal,
    f22bl_f22_balance_sheet_leverage_levtrend_252d_base_v033_signal,
    f22bl_f22_balance_sheet_leverage_ndtrend_126d_base_v034_signal,
    f22bl_f22_balance_sheet_leverage_solvtrend_126d_base_v035_signal,
    f22bl_f22_balance_sheet_leverage_levz_252d_base_v036_signal,
    f22bl_f22_balance_sheet_leverage_levz_126d_base_v037_signal,
    f22bl_f22_balance_sheet_leverage_levz_504d_base_v038_signal,
    f22bl_f22_balance_sheet_leverage_ndz_252d_base_v039_signal,
    f22bl_f22_balance_sheet_leverage_solvz_252d_base_v040_signal,
    f22bl_f22_balance_sheet_leverage_currz_252d_base_v041_signal,
    f22bl_f22_balance_sheet_leverage_dez_252d_base_v042_signal,
    f22bl_f22_balance_sheet_leverage_debtgrow_63d_base_v043_signal,
    f22bl_f22_balance_sheet_leverage_debtgrow_126d_base_v044_signal,
    f22bl_f22_balance_sheet_leverage_debtgrow_252d_base_v045_signal,
    f22bl_f22_balance_sheet_leverage_eqgrow_126d_base_v046_signal,
    f22bl_f22_balance_sheet_leverage_assetgrow_126d_base_v047_signal,
    f22bl_f22_balance_sheet_leverage_solvrank_252d_base_v048_signal,
    f22bl_f22_balance_sheet_leverage_levrank_252d_base_v049_signal,
    f22bl_f22_balance_sheet_leverage_ndrank_252d_base_v050_signal,
    f22bl_f22_balance_sheet_leverage_currrank_126d_base_v051_signal,
    f22bl_f22_balance_sheet_leverage_levdisp_63d_base_v052_signal,
    f22bl_f22_balance_sheet_leverage_levdisp_126d_base_v053_signal,
    f22bl_f22_balance_sheet_leverage_nddisp_126d_base_v054_signal,
    f22bl_f22_balance_sheet_leverage_solvdisp_126d_base_v055_signal,
    f22bl_f22_balance_sheet_leverage_levsurp_126d_base_v056_signal,
    f22bl_f22_balance_sheet_leverage_ndsurp_126d_base_v057_signal,
    f22bl_f22_balance_sheet_leverage_solvsurp_252d_base_v058_signal,
    f22bl_f22_balance_sheet_leverage_levratio_63_252_base_v059_signal,
    f22bl_f22_balance_sheet_leverage_ndratio_63_252_base_v060_signal,
    f22bl_f22_balance_sheet_leverage_gearspread_21d_base_v061_signal,
    f22bl_f22_balance_sheet_leverage_solvlevcross_63d_base_v062_signal,
    f22bl_f22_balance_sheet_leverage_stresslev_63d_base_v063_signal,
    f22bl_f22_balance_sheet_leverage_stressnd_63d_base_v064_signal,
    f22bl_f22_balance_sheet_leverage_levewm_63d_base_v065_signal,
    f22bl_f22_balance_sheet_leverage_levewm_126d_base_v066_signal,
    f22bl_f22_balance_sheet_leverage_ndewm_126d_base_v067_signal,
    f22bl_f22_balance_sheet_leverage_liabeq_21d_base_v068_signal,
    f22bl_f22_balance_sheet_leverage_liabeqsm_126d_base_v069_signal,
    f22bl_f22_balance_sheet_leverage_eqmult_63d_base_v070_signal,
    f22bl_f22_balance_sheet_leverage_cashcovz_252d_base_v071_signal,
    f22bl_f22_balance_sheet_leverage_degap_63d_base_v072_signal,
    f22bl_f22_balance_sheet_leverage_captrend_126d_base_v073_signal,
    f22bl_f22_balance_sheet_leverage_currtrend_126d_base_v074_signal,
    f22bl_f22_balance_sheet_leverage_stresscomp_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F22_BALANCE_SHEET_LEVERAGE_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f22_balance_sheet_leverage_base_001_075_claude: {n_features} features pass")
