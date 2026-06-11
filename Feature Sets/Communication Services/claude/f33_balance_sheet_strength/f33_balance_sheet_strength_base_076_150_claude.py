import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
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


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (balance-sheet strength) =====
def _f33_net_cash(cashneq, debt):
    return cashneq - debt


def _f33_de(debt, equity):
    return debt / equity.replace(0, np.nan)


def _f33_da(debt, assets):
    return debt / assets.replace(0, np.nan)


def _f33_ea(equity, assets):
    return equity / assets.replace(0, np.nan)


def _f33_wca(workingcapital, assets):
    return workingcapital / assets.replace(0, np.nan)


def _f33_cash_assets(cashneq, assets):
    return cashneq / assets.replace(0, np.nan)


def _f33_liab_assets(liabilities, assets):
    return liabilities / assets.replace(0, np.nan)


# ============================================================
# net-cash/assets level over half-year window (slower cushion)
def f33bs_f33_balance_sheet_strength_netcashassets_126d_base_v076_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = _mean(nc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity level over monthly window (fast leverage)
def f33bs_f33_balance_sheet_strength_de_21d_base_v077_signal(debt, equity):
    b = _mean(_f33_de(debt, equity), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets level over half-year window
def f33bs_f33_balance_sheet_strength_da_126d_base_v078_signal(debt, assets):
    b = _mean(_f33_da(debt, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets level over monthly window
def f33bs_f33_balance_sheet_strength_ea_21d_base_v079_signal(equity, assets):
    b = _mean(_f33_ea(equity, assets), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets level over half-year window
def f33bs_f33_balance_sheet_strength_wca_126d_base_v080_signal(workingcapital, assets):
    b = _mean(_f33_wca(workingcapital, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/liabilities level over half-year window (slow solvency buffer)
def f33bs_f33_balance_sheet_strength_cashliab_126d_base_v081_signal(cashneq, liabilities):
    b = _mean(cashneq / liabilities.replace(0, np.nan), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash/assets z-scored vs 126d history (faster de-trend)
def f33bs_f33_balance_sheet_strength_netcashassetsz_126d_base_v082_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = _z(nc, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets z-scored vs 504d history (long de-trend)
def f33bs_f33_balance_sheet_strength_daz_504d_base_v083_signal(debt, assets):
    b = _z(_f33_da(debt, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets z-scored vs 126d history
def f33bs_f33_balance_sheet_strength_eaz_126d_base_v084_signal(equity, assets):
    b = _z(_f33_ea(equity, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets z-scored vs 504d history
def f33bs_f33_balance_sheet_strength_cashassetsz_504d_base_v085_signal(cashneq, assets):
    b = _z(_f33_cash_assets(cashneq, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets z-scored vs 126d history
def f33bs_f33_balance_sheet_strength_liabassetsz_126d_base_v086_signal(liabilities, assets):
    b = _z(_f33_liab_assets(liabilities, assets), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio z-scored vs 126d history
def f33bs_f33_balance_sheet_strength_currz_126d_base_v087_signal(currentratio):
    b = _z(currentratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity percentile-rank vs 504d history
def f33bs_f33_balance_sheet_strength_derank_504d_base_v088_signal(debt, equity):
    b = _rank(_f33_de(debt, equity), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets percentile-rank vs 504d history
def f33bs_f33_balance_sheet_strength_earank_504d_base_v089_signal(equity, assets):
    b = _rank(_f33_ea(equity, assets), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets percentile-rank vs 252d history
def f33bs_f33_balance_sheet_strength_cashrank_252d_base_v090_signal(cashneq, assets):
    b = _rank(_f33_cash_assets(cashneq, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/assets percentile-rank vs 252d history
def f33bs_f33_balance_sheet_strength_liabrank_252d_base_v091_signal(liabilities, assets):
    b = _rank(_f33_liab_assets(liabilities, assets), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in net-cash/assets over a month (fast cushion impulse)
def f33bs_f33_balance_sheet_strength_netcashchg_21d_base_v092_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = nc - nc.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in debt/assets over a month
def f33bs_f33_balance_sheet_strength_dachg_21d_base_v093_signal(debt, assets):
    da = _f33_da(debt, assets)
    b = da - da.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in cash/assets over a month
def f33bs_f33_balance_sheet_strength_cashchg_21d_base_v094_signal(cashneq, assets):
    ca = _f33_cash_assets(cashneq, assets)
    b = ca - ca.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in liabilities/assets over a quarter
def f33bs_f33_balance_sheet_strength_liabchg_63d_base_v095_signal(liabilities, assets):
    la = _f33_liab_assets(liabilities, assets)
    b = la - la.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in current ratio over a month
def f33bs_f33_balance_sheet_strength_currchg_21d_base_v096_signal(currentratio):
    b = currentratio - currentratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in net-cash/assets
def f33bs_f33_balance_sheet_strength_netcashyoy_252d_base_v097_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    b = nc - nc.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in working-capital/assets
def f33bs_f33_balance_sheet_strength_wcayoy_252d_base_v098_signal(workingcapital, assets):
    wca = _f33_wca(workingcapital, assets)
    b = wca - wca.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in current ratio
def f33bs_f33_balance_sheet_strength_curryoy_252d_base_v099_signal(currentratio):
    b = currentratio - currentratio.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# log growth of liabilities (obligation build)
def f33bs_f33_balance_sheet_strength_liabgrow_252d_base_v100_signal(liabilities):
    l = liabilities.where(liabilities > 0)
    b = np.log(l / l.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash growth minus asset growth (liquidity intensifying within the balance sheet)
def f33bs_f33_balance_sheet_strength_cashvsasset_252d_base_v101_signal(cashneq, assets):
    c = cashneq.where(cashneq > 0)
    a = assets.where(assets > 0)
    b = np.log(c / c.shift(252)) - np.log(a / a.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity growth minus asset growth (capitalization improving)
def f33bs_f33_balance_sheet_strength_eqvsasset_252d_base_v102_signal(equity, assets):
    e = equity.where(equity > 0)
    a = assets.where(assets > 0)
    b = np.log(e / e.shift(252)) - np.log(a / a.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash strength regime over a quarter (fraction above own 126d median)
def f33bs_f33_balance_sheet_strength_netcashregime_63d_base_v103_signal(cashneq, debt):
    nc = _f33_net_cash(cashneq, debt)
    thr = nc.rolling(126, min_periods=63).median()
    flag = (nc > thr).astype(float)
    b = flag.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of half-year debt/assets sits below its 252d median (low-gearing persistence)
def f33bs_f33_balance_sheet_strength_lowgear_126d_base_v104_signal(debt, assets):
    da = _f33_da(debt, assets)
    thr = da.rolling(252, min_periods=126).median()
    flag = (da < thr).astype(float)
    b = flag.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of half-year current ratio above its 252d median (liquidity persistence)
def f33bs_f33_balance_sheet_strength_currpersist_126d_base_v105_signal(currentratio):
    thr = currentratio.rolling(252, min_periods=126).median()
    flag = (currentratio > thr).astype(float)
    b = flag.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current-ratio distance from a 2.0 hurdle scaled by 252d dispersion (strong-liquidity distance)
def f33bs_f33_balance_sheet_strength_currhurdle2_252d_base_v106_signal(currentratio):
    sd = _std(currentratio, 252)
    b = (currentratio - 2.0) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets distance from a 0.5 hurdle scaled by dispersion (well-capitalized distance)
def f33bs_f33_balance_sheet_strength_eahurdle_252d_base_v107_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    sd = _std(ea, 252)
    b = (ea - 0.5) / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity buffer (cash+wc)/assets z-scored vs 504d history (de-trended buffer strength)
def f33bs_f33_balance_sheet_strength_liqbufferassets_126d_base_v108_signal(cashneq, workingcapital, assets):
    buf = (cashneq + workingcapital) / assets.replace(0, np.nan)
    b = _z(buf, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# solvency score (equity-debt)/assets z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_solvencyz_252d_base_v109_signal(equity, debt, assets):
    sc = (equity - debt) / assets.replace(0, np.nan)
    b = _z(sc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# total liquidity (cash-debt+wc)/assets z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_totliqz_252d_base_v110_signal(cashneq, debt, workingcapital, assets):
    tl = (cashneq - debt + workingcapital) / assets.replace(0, np.nan)
    b = _z(tl, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interaction: equity/assets times current ratio z-scored (capitalized-liquidity regime)
def f33bs_f33_balance_sheet_strength_capliqz_252d_base_v111_signal(equity, assets, currentratio):
    inter = _f33_ea(equity, assets) * currentratio
    b = _z(inter, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# interaction: cash/assets times current ratio level (cash-backed liquidity, half-year)
def f33bs_f33_balance_sheet_strength_cashbacked_126d_base_v112_signal(cashneq, assets, currentratio):
    inter = _f33_cash_assets(cashneq, assets) * currentratio
    b = _mean(inter, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sign x magnitude of equity/assets minus 0.4 (compressed capitalization extremity)
def f33bs_f33_balance_sheet_strength_easm_126d_base_v113_signal(equity, assets):
    ea = _f33_ea(equity, assets) - 0.4
    b = np.sign(ea) * (ea.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of debt/equity over half a year (leverage instability)
def f33bs_f33_balance_sheet_strength_dedisp_126d_base_v114_signal(debt, equity):
    de = _f33_de(debt, equity)
    b = _std(de, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of cash/assets over a quarter (liquidity instability)
def f33bs_f33_balance_sheet_strength_cashdisp_63d_base_v115_signal(cashneq, assets):
    ca = _f33_cash_assets(cashneq, assets)
    b = _std(ca, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dispersion of working-capital/assets over half a year
def f33bs_f33_balance_sheet_strength_wcadisp_126d_base_v116_signal(workingcapital, assets):
    wca = _f33_wca(workingcapital, assets)
    b = _std(wca, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets short vs long mean spread (gearing drift)
def f33bs_f33_balance_sheet_strength_dadrift_base_v117_signal(debt, assets):
    da = _f33_da(debt, assets)
    b = _mean(da, 21) - _mean(da, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets short vs long mean spread (capitalization drift)
def f33bs_f33_balance_sheet_strength_eadrift_base_v118_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    b = _mean(ea, 21) - _mean(ea, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets minus its slow EMA (gearing displacement)
def f33bs_f33_balance_sheet_strength_dadisplace_base_v119_signal(debt, assets):
    da = _f33_da(debt, assets)
    b = da - da.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets minus its slow EMA (liquidity displacement)
def f33bs_f33_balance_sheet_strength_cashdisplace_base_v120_signal(cashneq, assets):
    ca = _f33_cash_assets(cashneq, assets)
    b = ca - ca.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity distance to its own 252d max (peak-leverage proximity)
def f33bs_f33_balance_sheet_strength_depeak_252d_base_v121_signal(debt, equity):
    de = _f33_de(debt, equity)
    mx = _rmax(de, 252)
    b = de / mx.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity/assets distance above its own 252d min (capitalization recovery off trough)
def f33bs_f33_balance_sheet_strength_eatrough_252d_base_v122_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    mn = _rmin(ea, 252)
    b = ea / mn.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash/assets position within its own 252d range (liquidity range position)
def f33bs_f33_balance_sheet_strength_cashpos_252d_base_v123_signal(cashneq, assets):
    ca = _f33_cash_assets(cashneq, assets)
    hi = _rmax(ca, 252)
    lo = _rmin(ca, 252)
    b = (ca - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/assets position within its own 252d range (gearing range position)
def f33bs_f33_balance_sheet_strength_dapos_252d_base_v124_signal(debt, assets):
    da = _f33_da(debt, assets)
    hi = _rmax(da, 252)
    lo = _rmin(da, 252)
    b = (da - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-squashed cash/assets deviation from its 252d median (bounded liquidity regime distance)
def f33bs_f33_balance_sheet_strength_cashtanh_252d_base_v125_signal(cashneq, assets):
    ca = _f33_cash_assets(cashneq, assets)
    med = ca.rolling(252, min_periods=126).median()
    b = np.tanh(5.0 * (ca - med))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt per unit of cash (leverage vs liquid reserves)
def f33bs_f33_balance_sheet_strength_debtcash_63d_base_v126_signal(debt, cashneq):
    ratio = debt / cashneq.replace(0, np.nan)
    b = _mean(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities per unit of cash, change over a quarter (obligation-coverage erosion impulse)
def f33bs_f33_balance_sheet_strength_liabcash_63d_base_v127_signal(liabilities, cashneq):
    ratio = liabilities / cashneq.replace(0, np.nan)
    b = ratio - ratio.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working capital per unit of debt, z-scored vs 252d history (liquidity-vs-leverage de-trend)
def f33bs_f33_balance_sheet_strength_wcdebt_126d_base_v128_signal(workingcapital, debt):
    ratio = workingcapital / debt.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity coverage of liabilities, z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_eqliabz_252d_base_v129_signal(equity, liabilities):
    ratio = equity / liabilities.replace(0, np.nan)
    b = _z(ratio, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash/equity change over a quarter (book-relative cushion impulse)
def f33bs_f33_balance_sheet_strength_netcasheqchg_63d_base_v130_signal(cashneq, debt, equity):
    nc = _f33_net_cash(cashneq, debt) / equity.replace(0, np.nan)
    b = nc - nc.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite strength rank over 504d: rank(cash/assets)+rank(currentratio)-rank(liab/assets)
def f33bs_f33_balance_sheet_strength_composite_504d_base_v131_signal(cashneq, assets, currentratio, liabilities):
    r1 = _rank(_f33_cash_assets(cashneq, assets), 504)
    r2 = _rank(currentratio, 504)
    r3 = _rank(_f33_liab_assets(liabilities, assets), 504)
    b = r1 + r2 - r3
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-buffer trend over a month: change in (cash+wc)/liabilities
def f33bs_f33_balance_sheet_strength_liqtrend_21d_base_v132_signal(cashneq, workingcapital, liabilities):
    buf = (cashneq + workingcapital) / liabilities.replace(0, np.nan)
    b = buf - buf.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gearing acceleration sign x magnitude: debt/assets change vs prior change
def f33bs_f33_balance_sheet_strength_daaccel_63d_base_v133_signal(debt, assets):
    da = _f33_da(debt, assets)
    accel = (da - da.shift(63)) - (da.shift(63) - da.shift(126))
    b = np.sign(accel) * (accel.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization acceleration: second difference of equity/assets over quarters
def f33bs_f33_balance_sheet_strength_eaaccel_63d_base_v134_signal(equity, assets):
    ea = _f33_ea(equity, assets)
    b = (ea - ea.shift(63)) - (ea.shift(63) - ea.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity slack: current ratio minus working-capital/assets, change over a quarter (composition shift)
def f33bs_f33_balance_sheet_strength_liqslack_63d_base_v135_signal(currentratio, workingcapital, assets):
    slack = currentratio - _f33_wca(workingcapital, assets)
    b = slack - slack.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash buffer relative to liabilities (worst-case coverage)
def f33bs_f33_balance_sheet_strength_netcashliab_63d_base_v136_signal(cashneq, debt, liabilities):
    nc = _f33_net_cash(cashneq, debt) / liabilities.replace(0, np.nan)
    b = _mean(nc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# equity cushion against debt: (equity-debt)/equity (deleverage headroom)
def f33bs_f33_balance_sheet_strength_eqcushion_63d_base_v137_signal(equity, debt):
    cush = (equity - debt) / equity.replace(0, np.nan)
    b = _mean(cush, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# asset-backed leverage safety: (assets-debt)/assets (unencumbered asset share)
def f33bs_f33_balance_sheet_strength_unencumbered_63d_base_v138_signal(assets, debt):
    safe = (assets - debt) / assets.replace(0, np.nan)
    b = _mean(safe, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liability runoff vs cash funding gap normalized by assets, z-scored vs 252d history
def f33bs_f33_balance_sheet_strength_fundgap_63d_base_v139_signal(liabilities, cashneq, assets):
    gap = (liabilities - cashneq) / assets.replace(0, np.nan)
    b = _z(gap, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# current ratio acceleration sign x magnitude (liquidity impulse)
def f33bs_f33_balance_sheet_strength_curraccel_63d_base_v140_signal(currentratio):
    accel = (currentratio - currentratio.shift(63)) - (currentratio.shift(63) - currentratio.shift(126))
    b = np.sign(accel) * (accel.abs() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-cash/assets multi-window dispersion (anchoring disagreement across timescales)
def f33bs_f33_balance_sheet_strength_netcashmulti_base_v141_signal(cashneq, debt, assets):
    nc = _f33_net_cash(cashneq, debt) / assets.replace(0, np.nan)
    m1 = _mean(nc, 21)
    m2 = _mean(nc, 63)
    m3 = _mean(nc, 252)
    b = pd.concat([m1, m2, m3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# debt/equity year-over-year change (slow leverage trend)
def f33bs_f33_balance_sheet_strength_deyoy_252d_base_v142_signal(debt, equity):
    de = _f33_de(debt, equity)
    b = de - de.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liabilities/equity year-over-year change (financial-leverage trend)
def f33bs_f33_balance_sheet_strength_liabeqyoy_252d_base_v143_signal(liabilities, equity):
    le = liabilities / equity.replace(0, np.nan)
    b = le - le.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-to-liabilities position within own 252d range (solvency range position)
def f33bs_f33_balance_sheet_strength_cashliabpos_252d_base_v144_signal(cashneq, liabilities):
    ratio = cashneq / liabilities.replace(0, np.nan)
    hi = _rmax(ratio, 252)
    lo = _rmin(ratio, 252)
    b = (ratio - lo) / (hi - lo).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/liabilities z-scored vs 126d history (short-term solvency de-trend)
def f33bs_f33_balance_sheet_strength_wcliabz_126d_base_v145_signal(workingcapital, liabilities):
    ratio = workingcapital / liabilities.replace(0, np.nan)
    b = _z(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-buffer rank vs 252d history (cash+wc)/assets percentile
def f33bs_f33_balance_sheet_strength_liqbufrank_252d_base_v146_signal(cashneq, workingcapital, assets):
    buf = (cashneq + workingcapital) / assets.replace(0, np.nan)
    b = _rank(buf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-leverage (net-debt)/assets minus its slow EMA (net-gearing displacement)
def f33bs_f33_balance_sheet_strength_netdadisplace_base_v147_signal(debt, cashneq, assets):
    nd = (debt - cashneq) / assets.replace(0, np.nan)
    b = nd - nd.ewm(span=126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# capitalization-quality composite: equity/assets times (1 - debt/assets)
def f33bs_f33_balance_sheet_strength_capquality_63d_base_v148_signal(equity, assets, debt):
    cq = _f33_ea(equity, assets) * (1.0 - _f33_da(debt, assets))
    b = _mean(cq, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# liquidity-coverage skew: (currentratio - 1) clipped, weighted by cash/assets
def f33bs_f33_balance_sheet_strength_liqskew_63d_base_v149_signal(currentratio, cashneq, assets):
    skew = (currentratio - 1.0).clip(lower=0) * _f33_cash_assets(cashneq, assets)
    b = _mean(skew, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# balance-sheet fortress score: rank(equity/assets)+rank(cash/assets)+rank(currentratio)-rank(debt/equity)
def f33bs_f33_balance_sheet_strength_fortress_252d_base_v150_signal(equity, assets, cashneq, currentratio, debt):
    r1 = _rank(_f33_ea(equity, assets), 252)
    r2 = _rank(_f33_cash_assets(cashneq, assets), 252)
    r3 = _rank(currentratio, 252)
    r4 = _rank(_f33_de(debt, equity), 252)
    b = r1 + r2 + r3 - r4
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33bs_f33_balance_sheet_strength_netcashassets_126d_base_v076_signal,
    f33bs_f33_balance_sheet_strength_de_21d_base_v077_signal,
    f33bs_f33_balance_sheet_strength_da_126d_base_v078_signal,
    f33bs_f33_balance_sheet_strength_ea_21d_base_v079_signal,
    f33bs_f33_balance_sheet_strength_wca_126d_base_v080_signal,
    f33bs_f33_balance_sheet_strength_cashliab_126d_base_v081_signal,
    f33bs_f33_balance_sheet_strength_netcashassetsz_126d_base_v082_signal,
    f33bs_f33_balance_sheet_strength_daz_504d_base_v083_signal,
    f33bs_f33_balance_sheet_strength_eaz_126d_base_v084_signal,
    f33bs_f33_balance_sheet_strength_cashassetsz_504d_base_v085_signal,
    f33bs_f33_balance_sheet_strength_liabassetsz_126d_base_v086_signal,
    f33bs_f33_balance_sheet_strength_currz_126d_base_v087_signal,
    f33bs_f33_balance_sheet_strength_derank_504d_base_v088_signal,
    f33bs_f33_balance_sheet_strength_earank_504d_base_v089_signal,
    f33bs_f33_balance_sheet_strength_cashrank_252d_base_v090_signal,
    f33bs_f33_balance_sheet_strength_liabrank_252d_base_v091_signal,
    f33bs_f33_balance_sheet_strength_netcashchg_21d_base_v092_signal,
    f33bs_f33_balance_sheet_strength_dachg_21d_base_v093_signal,
    f33bs_f33_balance_sheet_strength_cashchg_21d_base_v094_signal,
    f33bs_f33_balance_sheet_strength_liabchg_63d_base_v095_signal,
    f33bs_f33_balance_sheet_strength_currchg_21d_base_v096_signal,
    f33bs_f33_balance_sheet_strength_netcashyoy_252d_base_v097_signal,
    f33bs_f33_balance_sheet_strength_wcayoy_252d_base_v098_signal,
    f33bs_f33_balance_sheet_strength_curryoy_252d_base_v099_signal,
    f33bs_f33_balance_sheet_strength_liabgrow_252d_base_v100_signal,
    f33bs_f33_balance_sheet_strength_cashvsasset_252d_base_v101_signal,
    f33bs_f33_balance_sheet_strength_eqvsasset_252d_base_v102_signal,
    f33bs_f33_balance_sheet_strength_netcashregime_63d_base_v103_signal,
    f33bs_f33_balance_sheet_strength_lowgear_126d_base_v104_signal,
    f33bs_f33_balance_sheet_strength_currpersist_126d_base_v105_signal,
    f33bs_f33_balance_sheet_strength_currhurdle2_252d_base_v106_signal,
    f33bs_f33_balance_sheet_strength_eahurdle_252d_base_v107_signal,
    f33bs_f33_balance_sheet_strength_liqbufferassets_126d_base_v108_signal,
    f33bs_f33_balance_sheet_strength_solvencyz_252d_base_v109_signal,
    f33bs_f33_balance_sheet_strength_totliqz_252d_base_v110_signal,
    f33bs_f33_balance_sheet_strength_capliqz_252d_base_v111_signal,
    f33bs_f33_balance_sheet_strength_cashbacked_126d_base_v112_signal,
    f33bs_f33_balance_sheet_strength_easm_126d_base_v113_signal,
    f33bs_f33_balance_sheet_strength_dedisp_126d_base_v114_signal,
    f33bs_f33_balance_sheet_strength_cashdisp_63d_base_v115_signal,
    f33bs_f33_balance_sheet_strength_wcadisp_126d_base_v116_signal,
    f33bs_f33_balance_sheet_strength_dadrift_base_v117_signal,
    f33bs_f33_balance_sheet_strength_eadrift_base_v118_signal,
    f33bs_f33_balance_sheet_strength_dadisplace_base_v119_signal,
    f33bs_f33_balance_sheet_strength_cashdisplace_base_v120_signal,
    f33bs_f33_balance_sheet_strength_depeak_252d_base_v121_signal,
    f33bs_f33_balance_sheet_strength_eatrough_252d_base_v122_signal,
    f33bs_f33_balance_sheet_strength_cashpos_252d_base_v123_signal,
    f33bs_f33_balance_sheet_strength_dapos_252d_base_v124_signal,
    f33bs_f33_balance_sheet_strength_cashtanh_252d_base_v125_signal,
    f33bs_f33_balance_sheet_strength_debtcash_63d_base_v126_signal,
    f33bs_f33_balance_sheet_strength_liabcash_63d_base_v127_signal,
    f33bs_f33_balance_sheet_strength_wcdebt_126d_base_v128_signal,
    f33bs_f33_balance_sheet_strength_eqliabz_252d_base_v129_signal,
    f33bs_f33_balance_sheet_strength_netcasheqchg_63d_base_v130_signal,
    f33bs_f33_balance_sheet_strength_composite_504d_base_v131_signal,
    f33bs_f33_balance_sheet_strength_liqtrend_21d_base_v132_signal,
    f33bs_f33_balance_sheet_strength_daaccel_63d_base_v133_signal,
    f33bs_f33_balance_sheet_strength_eaaccel_63d_base_v134_signal,
    f33bs_f33_balance_sheet_strength_liqslack_63d_base_v135_signal,
    f33bs_f33_balance_sheet_strength_netcashliab_63d_base_v136_signal,
    f33bs_f33_balance_sheet_strength_eqcushion_63d_base_v137_signal,
    f33bs_f33_balance_sheet_strength_unencumbered_63d_base_v138_signal,
    f33bs_f33_balance_sheet_strength_fundgap_63d_base_v139_signal,
    f33bs_f33_balance_sheet_strength_curraccel_63d_base_v140_signal,
    f33bs_f33_balance_sheet_strength_netcashmulti_base_v141_signal,
    f33bs_f33_balance_sheet_strength_deyoy_252d_base_v142_signal,
    f33bs_f33_balance_sheet_strength_liabeqyoy_252d_base_v143_signal,
    f33bs_f33_balance_sheet_strength_cashliabpos_252d_base_v144_signal,
    f33bs_f33_balance_sheet_strength_wcliabz_126d_base_v145_signal,
    f33bs_f33_balance_sheet_strength_liqbufrank_252d_base_v146_signal,
    f33bs_f33_balance_sheet_strength_netdadisplace_base_v147_signal,
    f33bs_f33_balance_sheet_strength_capquality_63d_base_v148_signal,
    f33bs_f33_balance_sheet_strength_liqskew_63d_base_v149_signal,
    f33bs_f33_balance_sheet_strength_fortress_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_BALANCE_SHEET_STRENGTH_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    debt = _fund(101, base=6e7, drift=0.02, vol=0.06).rename("debt")
    equity = _fund(102, base=1.2e8, drift=0.015, vol=0.08, allow_neg=True).rename("equity")
    assets = _fund(103, base=3e8, drift=0.02, vol=0.05).rename("assets")
    liabilities = _fund(104, base=1.4e8, drift=0.02, vol=0.06).rename("liabilities")
    workingcapital = _fund(105, base=5e7, drift=0.01, vol=0.09, allow_neg=True).rename("workingcapital")
    cashneq = _fund(106, base=8e7, drift=0.025, vol=0.08).rename("cashneq")
    g = np.random.default_rng(108)
    cr_steps = np.repeat(g.normal(0.0, 0.06, n // 63 + 1), 63)[:n]
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(cr_steps / 63)), name="currentratio")

    cols = {
        "debt": debt, "equity": equity, "assets": assets, "liabilities": liabilities,
        "workingcapital": workingcapital, "cashneq": cashneq, "currentratio": currentratio,
    }

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff", "ncfi",
        "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas", "shareswa",
        "shareswadil", "assets", "assetsc", "tangibles", "intangibles", "ppnenet",
        "investments", "inventory", "receivables", "payables", "equity", "retearn",
        "workingcapital", "debt", "debtc", "debtnc", "liabilities", "liabilitiesc",
        "cashneq", "currentratio", "roic", "roe", "roa", "ros", "assetturnover", "invcap",
        "intexp", "taxexp", "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield",
        "payoutratio", "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal", "fndholders",
        "undholders", "prfholders", "dbtholders", "putholders", "putvalue", "cllholders",
        "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (name, meta["inputs"])
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f33_balance_sheet_strength_base_076_150_claude: %d features pass" % n_features)
