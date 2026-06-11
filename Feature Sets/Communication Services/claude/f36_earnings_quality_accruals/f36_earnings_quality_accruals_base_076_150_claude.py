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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== folder domain primitives (earnings quality / accruals) =====
def _f36eq_growth(s, w):
    # fractional growth of a level over w days
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f36eq_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f36eq_accrual(netinc, ncfo, assets):
    # Sloan total accruals: (earnings - operating cash flow) / assets
    return (netinc - ncfo) / assets.replace(0, np.nan)


def _f36eq_cash_spread(ncfo, netinc, scale):
    # cash-earnings spread normalized by a positive scale
    return (ncfo - netinc) / scale.replace(0, np.nan)


def _f36eq_conv(ncfo, netinc):
    # cash conversion: operating cash flow per unit of (positive) earnings
    return ncfo / netinc.where(netinc > 0, np.nan)


def _f36eq_dwc(workingcapital, w, assets):
    # change in working capital over w days, scaled by assets (accrual proxy)
    return (workingcapital - workingcapital.shift(w)) / assets.replace(0, np.nan)


def _f36eq_recv_intensity(receivables, revenue):
    # receivables relative to revenue (collection / DSO proxy)
    return receivables / revenue.replace(0, np.nan)


# receivables-growth minus revenue-growth over 378d (channel-stuffing risk)
def f36eq_f36_earnings_quality_accruals_recvrevg_378d_base_v076_signal(receivables, revenue):
    rg = _f36eq_growth(receivables, 378)
    vg = _f36eq_growth(revenue, 378)
    b = rg - vg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus operating-cashflow-growth over 63d (recognition lead)
def f36eq_f36_earnings_quality_accruals_revcashdiv_63d_base_v077_signal(revenue, ncfo):
    rg = _f36eq_growth(revenue, 63)
    cg = _f36eq_growth(ncfo, 63)
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus operating-cashflow-growth over 126d (recognition lead)
def f36eq_f36_earnings_quality_accruals_revcashdiv_126d_base_v078_signal(revenue, ncfo):
    rg = _f36eq_growth(revenue, 126)
    cg = _f36eq_growth(ncfo, 126)
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus operating-cashflow-growth over 252d (recognition lead)
def f36eq_f36_earnings_quality_accruals_revcashdiv_252d_base_v079_signal(revenue, ncfo):
    rg = _f36eq_growth(revenue, 252)
    cg = _f36eq_growth(ncfo, 252)
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus operating-cashflow-growth over 378d (recognition lead)
def f36eq_f36_earnings_quality_accruals_revcashdiv_378d_base_v080_signal(revenue, ncfo):
    rg = _f36eq_growth(revenue, 378)
    cg = _f36eq_growth(ncfo, 378)
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus operating-cash growth over 63d
def f36eq_f36_earnings_quality_accruals_recvcashdiv_63d_base_v081_signal(receivables, ncfo):
    rg = _f36eq_growth(receivables, 63)
    cg = _f36eq_growth(ncfo, 63)
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus operating-cash growth over 126d
def f36eq_f36_earnings_quality_accruals_recvcashdiv_126d_base_v082_signal(receivables, ncfo):
    rg = _f36eq_growth(receivables, 126)
    cg = _f36eq_growth(ncfo, 126)
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus operating-cash growth over 378d
def f36eq_f36_earnings_quality_accruals_recvcashdiv_378d_base_v083_signal(receivables, ncfo):
    rg = _f36eq_growth(receivables, 378)
    cg = _f36eq_growth(ncfo, 378)
    b = rg - cg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# d(receivables/assets) minus d(WC/assets) over 63d (receivable-led accrual)
def f36eq_f36_earnings_quality_accruals_recvwcdiv_63d_base_v084_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    b = (ra - ra.shift(63)) - (wa - wa.shift(63))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# d(receivables/assets) minus d(WC/assets) over 126d (receivable-led accrual)
def f36eq_f36_earnings_quality_accruals_recvwcdiv_126d_base_v085_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    b = (ra - ra.shift(126)) - (wa - wa.shift(126))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# d(receivables/assets) minus d(WC/assets) over 252d (receivable-led accrual)
def f36eq_f36_earnings_quality_accruals_recvwcdiv_252d_base_v086_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    b = (ra - ra.shift(252)) - (wa - wa.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# d(receivables/assets) minus d(WC/assets) over 378d (receivable-led accrual)
def f36eq_f36_earnings_quality_accruals_recvwcdiv_378d_base_v087_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    b = (ra - ra.shift(378)) - (wa - wa.shift(378))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# delta working-capital over 21d / assets (WC accrual)
def f36eq_f36_earnings_quality_accruals_dwc_21d_base_v088_signal(workingcapital, assets):
    b = _f36eq_dwc(workingcapital, 21, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# delta working-capital over 63d / assets (WC accrual)
def f36eq_f36_earnings_quality_accruals_dwc_63d_base_v089_signal(workingcapital, assets):
    b = _f36eq_dwc(workingcapital, 63, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# delta working-capital over 504d / assets (WC accrual)
def f36eq_f36_earnings_quality_accruals_dwc_504d_base_v090_signal(workingcapital, assets):
    b = _f36eq_dwc(workingcapital, 504, assets)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# delta WC/assets z-scored vs own 252d history
def f36eq_f36_earnings_quality_accruals_dwcz_252d_base_v091_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dWC/assets percentile rank vs own 504d history
def f36eq_f36_earnings_quality_accruals_dwcrank_504d_base_v092_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = _rank(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed-sqrt dWC/assets accrual magnitude over 252d
def f36eq_f36_earnings_quality_accruals_dwcsm_252d_base_v093_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = np.sign(a) * a.abs().pow(0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables build over 126d scaled by assets (working-capital accrual)
def f36eq_f36_earnings_quality_accruals_recvbuild_126d_base_v094_signal(receivables, assets):
    b = (receivables - receivables.shift(126)) / assets.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in WC/assets intensity over 252d
def f36eq_f36_earnings_quality_accruals_wcintchg_252d_base_v095_signal(workingcapital, assets):
    a = workingcapital / assets.replace(0, np.nan)
    b = a - a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in receivables/assets over 126d
def f36eq_f36_earnings_quality_accruals_recvassetschg_126d_base_v096_signal(receivables, assets):
    a = receivables / assets.replace(0, np.nan)
    b = a - a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion gap vs its EMA over 126d (mean-reversion of EQ)
def f36eq_f36_earnings_quality_accruals_convgap_126d_base_v097_signal(ncfo, netinc):
    a = _f36eq_conv(ncfo, netinc)
    sm = a.rolling(126, min_periods=max(1, 126 // 2)).mean()
    b = sm - a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-conversion gap vs its EMA over 252d (mean-reversion of EQ)
def f36eq_f36_earnings_quality_accruals_convgap_252d_base_v098_signal(ncfo, netinc):
    a = _f36eq_conv(ncfo, netinc)
    sm = a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    b = sm - a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded Sloan accrual over 252d
def f36eq_f36_earnings_quality_accruals_accrtanh_252d_base_v099_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets).rolling(252, min_periods=126).mean()
    b = np.tanh(10.0 * a)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EQ score: cash-ROA rank minus accrual rank over 252d
def f36eq_f36_earnings_quality_accruals_eqscore_252d_base_v100_signal(ncfo, assets, netinc):
    cr = (ncfo / assets.replace(0, np.nan))
    ac = _f36eq_accrual(netinc, ncfo, assets)
    b = _rank(cr, 252) - _rank(ac, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual x receivables-intensity-change over 252d (compound EQ risk)
def f36eq_f36_earnings_quality_accruals_accrxrecv_252d_base_v101_signal(netinc, ncfo, assets, receivables, revenue):
    acc = _f36eq_accrual(netinc, ncfo, assets).rolling(252, min_periods=126).mean()
    ri = _f36eq_recv_intensity(receivables, revenue)
    rid = ri - ri.shift(252)
    b = acc * rid
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth minus 0.2*cash-conversion over 252d (accrual-funded growth)
def f36eq_f36_earnings_quality_accruals_accrgrowth_252d_base_v102_signal(revenue, ncfo, netinc):
    vg = _f36eq_growth(revenue, 252)
    cv = _f36eq_conv(ncfo, netinc).rolling(252, min_periods=126).mean()
    b = vg - 0.2 * cv
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-growth times negative cash-ROA-change over 252d
def f36eq_f36_earnings_quality_accruals_growthcash_252d_base_v103_signal(revenue, ncfo, assets):
    vg = _f36eq_growth(revenue, 252)
    cr = (ncfo / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = vg * (-(cr - cr.shift(252)))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating accrual build: dWC/rev + d(receivables/rev) over 252d
def f36eq_f36_earnings_quality_accruals_opaccr_252d_base_v104_signal(workingcapital, revenue, receivables):
    dwc = (workingcapital - workingcapital.shift(252)) / revenue.replace(0, np.nan)
    ri = _f36eq_recv_intensity(receivables, revenue)
    b = dwc + (ri - ri.shift(252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# year-over-year change in smoothed Sloan accrual level (252d)
def f36eq_f36_earnings_quality_accruals_accryoy_252d_base_v105_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    sm = a.rolling(63, min_periods=21).mean()
    b = sm - sm.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual reversal: smoothed accrual times negative of its 252d lag
def f36eq_f36_earnings_quality_accruals_accrrev2_252d_base_v106_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets).rolling(63, min_periods=21).mean()
    b = -a * a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivable-led accrual (d-recv/assets minus d-WC/assets) z-scored vs 252d
def f36eq_f36_earnings_quality_accruals_recvwcz_252d_base_v107_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    a = (ra - ra.shift(63)) - (wa - wa.shift(63))
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual level over 63d (alt window)
def f36eq_f36_earnings_quality_accruals_accrual2_63d_base_v108_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    b = a.rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual level over 504d (alt window)
def f36eq_f36_earnings_quality_accruals_accrual2_504d_base_v109_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    b = a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in cash-conversion over 63d
def f36eq_f36_earnings_quality_accruals_convchg_63d_base_v110_signal(ncfo, netinc):
    a = _f36eq_conv(ncfo, netinc).rolling(21, min_periods=10).mean()
    b = a - a.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in cash-conversion over 504d
def f36eq_f36_earnings_quality_accruals_convchg_504d_base_v111_signal(ncfo, netinc):
    a = _f36eq_conv(ncfo, netinc).rolling(21, min_periods=10).mean()
    b = a - a.shift(504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables build (63d) z-scored vs 63d history
def f36eq_f36_earnings_quality_accruals_recvbuildz_63d_base_v112_signal(receivables, assets):
    a = (receivables - receivables.shift(63)) / assets.replace(0, np.nan)
    b = _z(a, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables build (63d) z-scored vs 504d history
def f36eq_f36_earnings_quality_accruals_recvbuildz_504d_base_v113_signal(receivables, assets):
    a = (receivables - receivables.shift(63)) / assets.replace(0, np.nan)
    b = _z(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# WC accrual (dWC 63d /assets) z-scored vs 126d history
def f36eq_f36_earnings_quality_accruals_wcaccrz_126d_base_v114_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = _z(a, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# (netinc-ncfo)/revenue accrual z-scored vs 126d history
def f36eq_f36_earnings_quality_accruals_accrrevz_126d_base_v115_signal(netinc, ncfo, revenue):
    a = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = _z(a, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-minus-revenue growth (126d) smoothed over 126d
def f36eq_f36_earnings_quality_accruals_recvgrowthlvl_126d_base_v116_signal(receivables, revenue):
    a = _f36eq_growth(receivables, 126) - _f36eq_growth(revenue, 126)
    b = a.rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-minus-revenue growth (126d) smoothed over 504d
def f36eq_f36_earnings_quality_accruals_recvgrowthlvl_504d_base_v117_signal(receivables, revenue):
    a = _f36eq_growth(receivables, 126) - _f36eq_growth(revenue, 126)
    b = a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in cash-ROA over 126d
def f36eq_f36_earnings_quality_accruals_cashroachg_126d_base_v118_signal(ncfo, assets):
    a = (ncfo / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in cash-ROA over 252d
def f36eq_f36_earnings_quality_accruals_cashroachg_252d_base_v119_signal(ncfo, assets):
    a = (ncfo / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in earnings-ROA over 126d
def f36eq_f36_earnings_quality_accruals_earnroachg_126d_base_v120_signal(netinc, assets):
    a = (netinc / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in earnings-ROA over 252d
def f36eq_f36_earnings_quality_accruals_earnroachg_252d_base_v121_signal(netinc, assets):
    a = (netinc / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tanh-bounded (netinc-ncfo)/revenue accrual over 252d
def f36eq_f36_earnings_quality_accruals_netaccrtanh_252d_base_v122_signal(netinc, ncfo, revenue):
    a = ((netinc - ncfo) / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    b = np.tanh(8.0 * a)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual smoothed over 189d (spare)
def f36eq_f36_earnings_quality_accruals_accrualx_189d_base_v123_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    b = a.rolling(189, min_periods=max(1, 189 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual smoothed over 378d (spare)
def f36eq_f36_earnings_quality_accruals_accrualx_378d_base_v124_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    b = a.rolling(378, min_periods=max(1, 378 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-ROA z-scored vs own 126d history (spare)
def f36eq_f36_earnings_quality_accruals_cashroaz_126d_base_v125_signal(ncfo, assets):
    a = ncfo / assets.replace(0, np.nan)
    b = _z(a, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash-ROA z-scored vs own 504d history (spare)
def f36eq_f36_earnings_quality_accruals_cashroaz_504d_base_v126_signal(ncfo, assets):
    a = ncfo / assets.replace(0, np.nan)
    b = _z(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in dWC(63d)/assets accrual over 126d (spare)
def f36eq_f36_earnings_quality_accruals_wcaccrchg_126d_base_v127_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = a - a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in dWC(63d)/assets accrual over 252d (spare)
def f36eq_f36_earnings_quality_accruals_wcaccrchg_252d_base_v128_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = a - a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in receivables/operating-cash over 126d (spare)
def f36eq_f36_earnings_quality_accruals_recvcashchg_126d_base_v129_signal(receivables, ncfo):
    a = (receivables / ncfo.where(ncfo > 0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# change in receivables/operating-cash over 252d (spare)
def f36eq_f36_earnings_quality_accruals_recvcashchg_252d_base_v130_signal(receivables, ncfo):
    a = (receivables / ncfo.where(ncfo > 0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-minus-cashflow growth (126d) z-scored vs 252d (spare)
def f36eq_f36_earnings_quality_accruals_revcashdivz_252d_base_v131_signal(revenue, ncfo):
    a = _f36eq_growth(revenue, 126) - _f36eq_growth(ncfo, 126)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# revenue-minus-cashflow growth (126d) z-scored vs 504d (spare)
def f36eq_f36_earnings_quality_accruals_revcashdivz_504d_base_v132_signal(revenue, ncfo):
    a = _f36eq_growth(revenue, 126) - _f36eq_growth(ncfo, 126)
    b = _z(a, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-revenue over 42d
def f36eq_f36_earnings_quality_accruals_gd_recv_rev_42d_base_v133_signal(receivables, revenue):
    b = _f36eq_growth(receivables, 42) - _f36eq_growth(revenue, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-revenue over 84d
def f36eq_f36_earnings_quality_accruals_gd_recv_rev_84d_base_v134_signal(receivables, revenue):
    b = _f36eq_growth(receivables, 84) - _f36eq_growth(revenue, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-revenue over 168d
def f36eq_f36_earnings_quality_accruals_gd_recv_rev_168d_base_v135_signal(receivables, revenue):
    b = _f36eq_growth(receivables, 168) - _f36eq_growth(revenue, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-ncfo over 42d
def f36eq_f36_earnings_quality_accruals_gd_recv_cash_42d_base_v136_signal(receivables, ncfo):
    b = _f36eq_growth(receivables, 42) - _f36eq_growth(ncfo, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-ncfo over 84d
def f36eq_f36_earnings_quality_accruals_gd_recv_cash_84d_base_v137_signal(receivables, ncfo):
    b = _f36eq_growth(receivables, 84) - _f36eq_growth(ncfo, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-ncfo over 336d
def f36eq_f36_earnings_quality_accruals_gd_recv_cash_336d_base_v138_signal(receivables, ncfo):
    b = _f36eq_growth(receivables, 336) - _f36eq_growth(ncfo, 336)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence revenue-minus-ncfo over 168d
def f36eq_f36_earnings_quality_accruals_gd_rev_cash_168d_base_v139_signal(revenue, ncfo):
    b = _f36eq_growth(revenue, 168) - _f36eq_growth(ncfo, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence revenue-minus-ncfo over 336d
def f36eq_f36_earnings_quality_accruals_gd_rev_cash_336d_base_v140_signal(revenue, ncfo):
    b = _f36eq_growth(revenue, 336) - _f36eq_growth(ncfo, 336)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-netinc over 42d
def f36eq_f36_earnings_quality_accruals_gd_recv_ni_42d_base_v141_signal(receivables, netinc):
    b = _f36eq_growth(receivables, 42) - _f36eq_growth(netinc, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-netinc over 84d
def f36eq_f36_earnings_quality_accruals_gd_recv_ni_84d_base_v142_signal(receivables, netinc):
    b = _f36eq_growth(receivables, 84) - _f36eq_growth(netinc, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-netinc over 168d
def f36eq_f36_earnings_quality_accruals_gd_recv_ni_168d_base_v143_signal(receivables, netinc):
    b = _f36eq_growth(receivables, 168) - _f36eq_growth(netinc, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence receivables-minus-netinc over 336d
def f36eq_f36_earnings_quality_accruals_gd_recv_ni_336d_base_v144_signal(receivables, netinc):
    b = _f36eq_growth(receivables, 336) - _f36eq_growth(netinc, 336)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence workingcapital-minus-revenue over 42d
def f36eq_f36_earnings_quality_accruals_gd_wc_rev_42d_base_v145_signal(workingcapital, revenue):
    b = _f36eq_growth(workingcapital, 42) - _f36eq_growth(revenue, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence workingcapital-minus-revenue over 84d
def f36eq_f36_earnings_quality_accruals_gd_wc_rev_84d_base_v146_signal(workingcapital, revenue):
    b = _f36eq_growth(workingcapital, 84) - _f36eq_growth(revenue, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence workingcapital-minus-revenue over 168d
def f36eq_f36_earnings_quality_accruals_gd_wc_rev_168d_base_v147_signal(workingcapital, revenue):
    b = _f36eq_growth(workingcapital, 168) - _f36eq_growth(revenue, 168)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence workingcapital-minus-revenue over 336d
def f36eq_f36_earnings_quality_accruals_gd_wc_rev_336d_base_v148_signal(workingcapital, revenue):
    b = _f36eq_growth(workingcapital, 336) - _f36eq_growth(revenue, 336)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence workingcapital-minus-ncfo over 42d
def f36eq_f36_earnings_quality_accruals_gd_wc_cash_42d_base_v149_signal(workingcapital, ncfo):
    b = _f36eq_growth(workingcapital, 42) - _f36eq_growth(ncfo, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth divergence workingcapital-minus-ncfo over 84d
def f36eq_f36_earnings_quality_accruals_gd_wc_cash_84d_base_v150_signal(workingcapital, ncfo):
    b = _f36eq_growth(workingcapital, 84) - _f36eq_growth(ncfo, 84)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36eq_f36_earnings_quality_accruals_recvrevg_378d_base_v076_signal,
    f36eq_f36_earnings_quality_accruals_revcashdiv_63d_base_v077_signal,
    f36eq_f36_earnings_quality_accruals_revcashdiv_126d_base_v078_signal,
    f36eq_f36_earnings_quality_accruals_revcashdiv_252d_base_v079_signal,
    f36eq_f36_earnings_quality_accruals_revcashdiv_378d_base_v080_signal,
    f36eq_f36_earnings_quality_accruals_recvcashdiv_63d_base_v081_signal,
    f36eq_f36_earnings_quality_accruals_recvcashdiv_126d_base_v082_signal,
    f36eq_f36_earnings_quality_accruals_recvcashdiv_378d_base_v083_signal,
    f36eq_f36_earnings_quality_accruals_recvwcdiv_63d_base_v084_signal,
    f36eq_f36_earnings_quality_accruals_recvwcdiv_126d_base_v085_signal,
    f36eq_f36_earnings_quality_accruals_recvwcdiv_252d_base_v086_signal,
    f36eq_f36_earnings_quality_accruals_recvwcdiv_378d_base_v087_signal,
    f36eq_f36_earnings_quality_accruals_dwc_21d_base_v088_signal,
    f36eq_f36_earnings_quality_accruals_dwc_63d_base_v089_signal,
    f36eq_f36_earnings_quality_accruals_dwc_504d_base_v090_signal,
    f36eq_f36_earnings_quality_accruals_dwcz_252d_base_v091_signal,
    f36eq_f36_earnings_quality_accruals_dwcrank_504d_base_v092_signal,
    f36eq_f36_earnings_quality_accruals_dwcsm_252d_base_v093_signal,
    f36eq_f36_earnings_quality_accruals_recvbuild_126d_base_v094_signal,
    f36eq_f36_earnings_quality_accruals_wcintchg_252d_base_v095_signal,
    f36eq_f36_earnings_quality_accruals_recvassetschg_126d_base_v096_signal,
    f36eq_f36_earnings_quality_accruals_convgap_126d_base_v097_signal,
    f36eq_f36_earnings_quality_accruals_convgap_252d_base_v098_signal,
    f36eq_f36_earnings_quality_accruals_accrtanh_252d_base_v099_signal,
    f36eq_f36_earnings_quality_accruals_eqscore_252d_base_v100_signal,
    f36eq_f36_earnings_quality_accruals_accrxrecv_252d_base_v101_signal,
    f36eq_f36_earnings_quality_accruals_accrgrowth_252d_base_v102_signal,
    f36eq_f36_earnings_quality_accruals_growthcash_252d_base_v103_signal,
    f36eq_f36_earnings_quality_accruals_opaccr_252d_base_v104_signal,
    f36eq_f36_earnings_quality_accruals_accryoy_252d_base_v105_signal,
    f36eq_f36_earnings_quality_accruals_accrrev2_252d_base_v106_signal,
    f36eq_f36_earnings_quality_accruals_recvwcz_252d_base_v107_signal,
    f36eq_f36_earnings_quality_accruals_accrual2_63d_base_v108_signal,
    f36eq_f36_earnings_quality_accruals_accrual2_504d_base_v109_signal,
    f36eq_f36_earnings_quality_accruals_convchg_63d_base_v110_signal,
    f36eq_f36_earnings_quality_accruals_convchg_504d_base_v111_signal,
    f36eq_f36_earnings_quality_accruals_recvbuildz_63d_base_v112_signal,
    f36eq_f36_earnings_quality_accruals_recvbuildz_504d_base_v113_signal,
    f36eq_f36_earnings_quality_accruals_wcaccrz_126d_base_v114_signal,
    f36eq_f36_earnings_quality_accruals_accrrevz_126d_base_v115_signal,
    f36eq_f36_earnings_quality_accruals_recvgrowthlvl_126d_base_v116_signal,
    f36eq_f36_earnings_quality_accruals_recvgrowthlvl_504d_base_v117_signal,
    f36eq_f36_earnings_quality_accruals_cashroachg_126d_base_v118_signal,
    f36eq_f36_earnings_quality_accruals_cashroachg_252d_base_v119_signal,
    f36eq_f36_earnings_quality_accruals_earnroachg_126d_base_v120_signal,
    f36eq_f36_earnings_quality_accruals_earnroachg_252d_base_v121_signal,
    f36eq_f36_earnings_quality_accruals_netaccrtanh_252d_base_v122_signal,
    f36eq_f36_earnings_quality_accruals_accrualx_189d_base_v123_signal,
    f36eq_f36_earnings_quality_accruals_accrualx_378d_base_v124_signal,
    f36eq_f36_earnings_quality_accruals_cashroaz_126d_base_v125_signal,
    f36eq_f36_earnings_quality_accruals_cashroaz_504d_base_v126_signal,
    f36eq_f36_earnings_quality_accruals_wcaccrchg_126d_base_v127_signal,
    f36eq_f36_earnings_quality_accruals_wcaccrchg_252d_base_v128_signal,
    f36eq_f36_earnings_quality_accruals_recvcashchg_126d_base_v129_signal,
    f36eq_f36_earnings_quality_accruals_recvcashchg_252d_base_v130_signal,
    f36eq_f36_earnings_quality_accruals_revcashdivz_252d_base_v131_signal,
    f36eq_f36_earnings_quality_accruals_revcashdivz_504d_base_v132_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_rev_42d_base_v133_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_rev_84d_base_v134_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_rev_168d_base_v135_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_cash_42d_base_v136_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_cash_84d_base_v137_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_cash_336d_base_v138_signal,
    f36eq_f36_earnings_quality_accruals_gd_rev_cash_168d_base_v139_signal,
    f36eq_f36_earnings_quality_accruals_gd_rev_cash_336d_base_v140_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_ni_42d_base_v141_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_ni_84d_base_v142_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_ni_168d_base_v143_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_ni_336d_base_v144_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_rev_42d_base_v145_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_rev_84d_base_v146_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_rev_168d_base_v147_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_rev_336d_base_v148_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_cash_42d_base_v149_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_cash_84d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_EARNINGS_QUALITY_ACCRUALS_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    netinc = _fund(361, base=4.0e7, drift=0.02, vol=0.10, allow_neg=True).rename("netinc")
    ncfo = _fund(362, base=6.0e7, drift=0.025, vol=0.09, allow_neg=True).rename("ncfo")
    assets = _fund(363, base=8.0e8, drift=0.03, vol=0.05).rename("assets")
    receivables = _fund(364, base=1.2e8, drift=0.035, vol=0.08).rename("receivables")
    revenue = _fund(365, base=2.5e8, drift=0.03, vol=0.07).rename("revenue")
    workingcapital = _fund(366, base=9.0e7, drift=0.02, vol=0.12, allow_neg=True).rename("workingcapital")

    cols = {
        "netinc": netinc, "ncfo": ncfo, "assets": assets,
        "receivables": receivables, "revenue": revenue,
        "workingcapital": workingcapital,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f36_earnings_quality_accruals_base_076_150_claude: %d features pass" % n_features)
