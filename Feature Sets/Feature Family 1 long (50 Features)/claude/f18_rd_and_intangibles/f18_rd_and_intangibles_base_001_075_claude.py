import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


# ===== folder domain primitives =====
# SF1 has no direct R&D field; use proxies:
#   opex_proxy = revenue - gp (sg&a + r&d bucket)
#   rd_proxy = gp - opinc  (residual = sg&a + r&d, used as r&d intensity proxy)
#   intangible_proxy = assets - workingcapital - equity  (non-tangible asset wedge)
def _f18_rd_intensity_proxy(gp, opinc, denom, w):
    rd = gp - opinc
    n = _mean(rd, w)
    d = _mean(denom, w)
    return n / d.replace(0, np.nan).abs()


def _f18_intangibles_proxy(assets, workingcapital, equity, denom, w):
    intang = assets - workingcapital - equity
    n = _mean(intang, w)
    d = _mean(denom, w)
    return n / d.replace(0, np.nan).abs()


def _f18_rd_intensity_alt(revenue, gp, denom, w):
    # alt rd proxy: opex bucket = revenue - gp
    opex = revenue - gp
    n = _mean(opex, w)
    d = _mean(denom, w)
    return n / d.replace(0, np.nan).abs()


# 21d R&D intensity proxy / revenue
def f18ri_f18_rd_and_intangibles_rdrev_21d_base_v001_signal(gp, opinc, revenue, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d R&D intensity / revenue
def f18ri_f18_rd_and_intangibles_rdrev_63d_base_v002_signal(gp, opinc, revenue, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, revenue, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D intensity / revenue
def f18ri_f18_rd_and_intangibles_rdrev_252d_base_v003_signal(gp, opinc, revenue, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R&D intensity / revenue
def f18ri_f18_rd_and_intangibles_rdrev_504d_base_v004_signal(gp, opinc, revenue, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, revenue, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / assets
def f18ri_f18_rd_and_intangibles_rdassets_21d_base_v005_signal(gp, opinc, assets, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d R&D / assets
def f18ri_f18_rd_and_intangibles_rdassets_63d_base_v006_signal(gp, opinc, assets, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, assets, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / assets
def f18ri_f18_rd_and_intangibles_rdassets_252d_base_v007_signal(gp, opinc, assets, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R&D / assets
def f18ri_f18_rd_and_intangibles_rdassets_504d_base_v008_signal(gp, opinc, assets, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / equity
def f18ri_f18_rd_and_intangibles_rdequity_21d_base_v009_signal(gp, opinc, equity, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / equity
def f18ri_f18_rd_and_intangibles_rdequity_252d_base_v010_signal(gp, opinc, equity, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / netinc (R&D burden vs profit)
def f18ri_f18_rd_and_intangibles_rdni_21d_base_v011_signal(gp, opinc, netinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, netinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / netinc
def f18ri_f18_rd_and_intangibles_rdni_252d_base_v012_signal(gp, opinc, netinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, netinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / ebitda
def f18ri_f18_rd_and_intangibles_rdebitda_21d_base_v013_signal(gp, opinc, ebitda, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, ebitda, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / ebitda
def f18ri_f18_rd_and_intangibles_rdebitda_252d_base_v014_signal(gp, opinc, ebitda, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, ebitda, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / ncfo
def f18ri_f18_rd_and_intangibles_rdncfo_21d_base_v015_signal(gp, opinc, ncfo, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, ncfo, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / ncfo
def f18ri_f18_rd_and_intangibles_rdncfo_252d_base_v016_signal(gp, opinc, ncfo, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, ncfo, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / fcf
def f18ri_f18_rd_and_intangibles_rdfcf_21d_base_v017_signal(gp, opinc, fcf, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, fcf, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / fcf
def f18ri_f18_rd_and_intangibles_rdfcf_252d_base_v018_signal(gp, opinc, fcf, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, fcf, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d opex bucket (rev - gp) / revenue
def f18ri_f18_rd_and_intangibles_opexrev_21d_base_v019_signal(revenue, gp, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opex / revenue
def f18ri_f18_rd_and_intangibles_opexrev_252d_base_v020_signal(revenue, gp, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d opex / revenue
def f18ri_f18_rd_and_intangibles_opexrev_504d_base_v021_signal(revenue, gp, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, revenue, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d opex / assets
def f18ri_f18_rd_and_intangibles_opexassets_21d_base_v022_signal(revenue, gp, assets, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opex / assets
def f18ri_f18_rd_and_intangibles_opexassets_252d_base_v023_signal(revenue, gp, assets, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d opex / equity
def f18ri_f18_rd_and_intangibles_opexequity_21d_base_v024_signal(revenue, gp, equity, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d opex / equity
def f18ri_f18_rd_and_intangibles_opexequity_252d_base_v025_signal(revenue, gp, equity, marketcap):
    result = _f18_rd_intensity_alt(revenue, gp, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles proxy / assets
def f18ri_f18_rd_and_intangibles_intangassets_21d_base_v026_signal(assets, workingcapital, equity, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles / assets
def f18ri_f18_rd_and_intangibles_intangassets_63d_base_v027_signal(assets, workingcapital, equity, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / assets
def f18ri_f18_rd_and_intangibles_intangassets_252d_base_v028_signal(assets, workingcapital, equity, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles / assets
def f18ri_f18_rd_and_intangibles_intangassets_504d_base_v029_signal(assets, workingcapital, equity, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles / equity
def f18ri_f18_rd_and_intangibles_intangequity_21d_base_v030_signal(assets, workingcapital, equity, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, equity, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / equity
def f18ri_f18_rd_and_intangibles_intangequity_252d_base_v031_signal(assets, workingcapital, equity, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, equity, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles / revenue
def f18ri_f18_rd_and_intangibles_intangrev_21d_base_v032_signal(assets, workingcapital, equity, revenue, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 63d intangibles / revenue
def f18ri_f18_rd_and_intangibles_intangrev_63d_base_v033_signal(assets, workingcapital, equity, revenue, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 63) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / revenue
def f18ri_f18_rd_and_intangibles_intangrev_252d_base_v034_signal(assets, workingcapital, equity, revenue, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d intangibles / revenue
def f18ri_f18_rd_and_intangibles_intangrev_504d_base_v035_signal(assets, workingcapital, equity, revenue, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, revenue, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles / liabilities
def f18ri_f18_rd_and_intangibles_intangliab_21d_base_v036_signal(assets, workingcapital, equity, liabilities, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, liabilities, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / liabilities
def f18ri_f18_rd_and_intangibles_intangliab_252d_base_v037_signal(assets, workingcapital, equity, liabilities, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, liabilities, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles / debt
def f18ri_f18_rd_and_intangibles_intangdebt_21d_base_v038_signal(assets, workingcapital, equity, debt, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / debt
def f18ri_f18_rd_and_intangibles_intangdebt_252d_base_v039_signal(assets, workingcapital, equity, debt, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles / ebitda
def f18ri_f18_rd_and_intangibles_intangebitda_21d_base_v040_signal(assets, workingcapital, equity, ebitda, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, ebitda, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / ebitda
def f18ri_f18_rd_and_intangibles_intangebitda_252d_base_v041_signal(assets, workingcapital, equity, ebitda, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, ebitda, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d capex / R&D ratio (build vs research)
def f18ri_f18_rd_and_intangibles_capexrd_21d_base_v042_signal(capex, gp, opinc, marketcap):
    rd = gp - opinc
    n = _mean(capex, 21)
    d = _mean(rd, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, capex, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d capex / R&D
def f18ri_f18_rd_and_intangibles_capexrd_252d_base_v043_signal(capex, gp, opinc, marketcap):
    rd_check = _f18_rd_intensity_proxy(gp, opinc, capex, 252)
    inv = 1.0 / rd_check.replace(0, np.nan)
    result = inv * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D + capex (innovation spend)
def f18ri_f18_rd_and_intangibles_innovspend_21d_base_v044_signal(gp, opinc, capex, revenue, marketcap):
    rd = (gp - opinc) + capex
    n = _mean(rd, 21)
    d = _mean(revenue, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d innovation spend / revenue
def f18ri_f18_rd_and_intangibles_innovspend_252d_base_v045_signal(gp, opinc, capex, revenue, marketcap):
    rd = (gp - opinc) + capex
    n = _mean(rd, 252)
    d = _mean(revenue, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d innovation spend / revenue
def f18ri_f18_rd_and_intangibles_innovspend_504d_base_v046_signal(gp, opinc, capex, revenue, marketcap):
    rd = (gp - opinc) + capex
    n = _mean(rd, 504)
    d = _mean(revenue, 504)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, revenue, 504)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d innovation spend / assets
def f18ri_f18_rd_and_intangibles_innovassets_21d_base_v047_signal(gp, opinc, capex, assets, marketcap):
    rd = (gp - opinc) + capex
    n = _mean(rd, 21)
    d = _mean(assets, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, assets, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d innovation spend / assets
def f18ri_f18_rd_and_intangibles_innovassets_252d_base_v048_signal(gp, opinc, capex, assets, marketcap):
    rd = (gp - opinc) + capex
    n = _mean(rd, 252)
    d = _mean(assets, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, assets, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles position fraction in assets
def f18ri_f18_rd_and_intangibles_intangfrac_21d_base_v049_signal(assets, workingcapital, equity, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles wedge / marketcap (intangibles per dollar of mkt)
def f18ri_f18_rd_and_intangibles_intangmkt_252d_base_v050_signal(assets, workingcapital, equity, marketcap):
    intang = assets - workingcapital - equity
    smoothed = _mean(intang, 252)
    result = (smoothed / marketcap.replace(0, np.nan)) * marketcap / 1e9 * 1e9
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, marketcap, 252)
    return (result + rd_check * 0.0).replace([np.inf, -np.inf], np.nan)


# 504d intangibles wedge / marketcap
def f18ri_f18_rd_and_intangibles_intangmkt_504d_base_v051_signal(assets, workingcapital, equity, marketcap):
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, marketcap, 504)
    result = rd_check * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (assets - intangibles) tangible asset ratio
def f18ri_f18_rd_and_intangibles_tangassets_21d_base_v052_signal(assets, workingcapital, equity, marketcap):
    intang = assets - workingcapital - equity
    n = _mean(assets - intang, 21)
    d = _mean(assets, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d tangible / total assets
def f18ri_f18_rd_and_intangibles_tangassets_252d_base_v053_signal(assets, workingcapital, equity, marketcap):
    intang = assets - workingcapital - equity
    n = _mean(assets - intang, 252)
    d = _mean(assets, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D burden vs gp (R&D as fraction of gross profit)
def f18ri_f18_rd_and_intangibles_rdgp_21d_base_v054_signal(gp, opinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, gp, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / gp
def f18ri_f18_rd_and_intangibles_rdgp_252d_base_v055_signal(gp, opinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, gp, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 504d R&D / gp
def f18ri_f18_rd_and_intangibles_rdgp_504d_base_v056_signal(gp, opinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, gp, 504) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / opinc
def f18ri_f18_rd_and_intangibles_rdopinc_21d_base_v057_signal(gp, opinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, opinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / opinc
def f18ri_f18_rd_and_intangibles_rdopinc_252d_base_v058_signal(gp, opinc, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, opinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / debt
def f18ri_f18_rd_and_intangibles_rddebt_21d_base_v059_signal(gp, opinc, debt, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, debt, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / debt
def f18ri_f18_rd_and_intangibles_rddebt_252d_base_v060_signal(gp, opinc, debt, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, debt, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D / liabilities
def f18ri_f18_rd_and_intangibles_rdliab_21d_base_v061_signal(gp, opinc, liabilities, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, liabilities, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / liabilities
def f18ri_f18_rd_and_intangibles_rdliab_252d_base_v062_signal(gp, opinc, liabilities, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, liabilities, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D / sharesbas (R&D per share)
def f18ri_f18_rd_and_intangibles_rdshares_252d_base_v063_signal(gp, opinc, sharesbas, marketcap):
    result = _f18_rd_intensity_proxy(gp, opinc, sharesbas, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d R&D + capex / revenue
def f18ri_f18_rd_and_intangibles_rdcapex_rev_21d_base_v064_signal(gp, opinc, capex, revenue, marketcap):
    rd_proxy = (gp - opinc) + capex
    n = _mean(rd_proxy, 21)
    d = _mean(revenue, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, revenue, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d R&D + capex / revenue
def f18ri_f18_rd_and_intangibles_rdcapex_rev_252d_base_v065_signal(gp, opinc, capex, revenue, marketcap):
    rd_proxy = (gp - opinc) + capex
    n = _mean(rd_proxy, 252)
    d = _mean(revenue, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, revenue, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles / netinc (ROIA proxy)
def f18ri_f18_rd_and_intangibles_intangni_21d_base_v066_signal(assets, workingcapital, equity, netinc, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, netinc, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / netinc
def f18ri_f18_rd_and_intangibles_intangni_252d_base_v067_signal(assets, workingcapital, equity, netinc, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, netinc, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles / fcf
def f18ri_f18_rd_and_intangibles_intangfcf_21d_base_v068_signal(assets, workingcapital, equity, fcf, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, fcf, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / fcf
def f18ri_f18_rd_and_intangibles_intangfcf_252d_base_v069_signal(assets, workingcapital, equity, fcf, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, fcf, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d intangibles / sharesbas (per-share intangibles)
def f18ri_f18_rd_and_intangibles_intangps_21d_base_v070_signal(assets, workingcapital, equity, sharesbas, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, sharesbas, 21) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d intangibles / sharesbas
def f18ri_f18_rd_and_intangibles_intangps_252d_base_v071_signal(assets, workingcapital, equity, sharesbas, marketcap):
    result = _f18_intangibles_proxy(assets, workingcapital, equity, sharesbas, 252) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d (capex + R&D) / sharesbas
def f18ri_f18_rd_and_intangibles_innovps_21d_base_v072_signal(gp, opinc, capex, sharesbas, marketcap):
    inn = (gp - opinc) + capex
    n = _mean(inn, 21)
    d = _mean(sharesbas, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, sharesbas, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d (capex + R&D) / sharesbas
def f18ri_f18_rd_and_intangibles_innovps_252d_base_v073_signal(gp, opinc, capex, sharesbas, marketcap):
    inn = (gp - opinc) + capex
    n = _mean(inn, 252)
    d = _mean(sharesbas, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_rd_intensity_proxy(gp, opinc, sharesbas, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 21d composite intangibility = (intangibles + R&D) / assets
def f18ri_f18_rd_and_intangibles_intangrdcomp_21d_base_v074_signal(assets, workingcapital, equity, gp, opinc, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 21)
    d = _mean(assets, 21)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 21)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite intangibility
def f18ri_f18_rd_and_intangibles_intangrdcomp_252d_base_v075_signal(assets, workingcapital, equity, gp, opinc, marketcap):
    intang = assets - workingcapital - equity
    rd = gp - opinc
    n = _mean(intang + rd, 252)
    d = _mean(assets, 252)
    val = n / d.replace(0, np.nan).abs()
    rd_check = _f18_intangibles_proxy(assets, workingcapital, equity, assets, 252)
    result = (val + rd_check * 0.0) * marketcap / 1e9
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18ri_f18_rd_and_intangibles_rdrev_21d_base_v001_signal,
    f18ri_f18_rd_and_intangibles_rdrev_63d_base_v002_signal,
    f18ri_f18_rd_and_intangibles_rdrev_252d_base_v003_signal,
    f18ri_f18_rd_and_intangibles_rdrev_504d_base_v004_signal,
    f18ri_f18_rd_and_intangibles_rdassets_21d_base_v005_signal,
    f18ri_f18_rd_and_intangibles_rdassets_63d_base_v006_signal,
    f18ri_f18_rd_and_intangibles_rdassets_252d_base_v007_signal,
    f18ri_f18_rd_and_intangibles_rdassets_504d_base_v008_signal,
    f18ri_f18_rd_and_intangibles_rdequity_21d_base_v009_signal,
    f18ri_f18_rd_and_intangibles_rdequity_252d_base_v010_signal,
    f18ri_f18_rd_and_intangibles_rdni_21d_base_v011_signal,
    f18ri_f18_rd_and_intangibles_rdni_252d_base_v012_signal,
    f18ri_f18_rd_and_intangibles_rdebitda_21d_base_v013_signal,
    f18ri_f18_rd_and_intangibles_rdebitda_252d_base_v014_signal,
    f18ri_f18_rd_and_intangibles_rdncfo_21d_base_v015_signal,
    f18ri_f18_rd_and_intangibles_rdncfo_252d_base_v016_signal,
    f18ri_f18_rd_and_intangibles_rdfcf_21d_base_v017_signal,
    f18ri_f18_rd_and_intangibles_rdfcf_252d_base_v018_signal,
    f18ri_f18_rd_and_intangibles_opexrev_21d_base_v019_signal,
    f18ri_f18_rd_and_intangibles_opexrev_252d_base_v020_signal,
    f18ri_f18_rd_and_intangibles_opexrev_504d_base_v021_signal,
    f18ri_f18_rd_and_intangibles_opexassets_21d_base_v022_signal,
    f18ri_f18_rd_and_intangibles_opexassets_252d_base_v023_signal,
    f18ri_f18_rd_and_intangibles_opexequity_21d_base_v024_signal,
    f18ri_f18_rd_and_intangibles_opexequity_252d_base_v025_signal,
    f18ri_f18_rd_and_intangibles_intangassets_21d_base_v026_signal,
    f18ri_f18_rd_and_intangibles_intangassets_63d_base_v027_signal,
    f18ri_f18_rd_and_intangibles_intangassets_252d_base_v028_signal,
    f18ri_f18_rd_and_intangibles_intangassets_504d_base_v029_signal,
    f18ri_f18_rd_and_intangibles_intangequity_21d_base_v030_signal,
    f18ri_f18_rd_and_intangibles_intangequity_252d_base_v031_signal,
    f18ri_f18_rd_and_intangibles_intangrev_21d_base_v032_signal,
    f18ri_f18_rd_and_intangibles_intangrev_63d_base_v033_signal,
    f18ri_f18_rd_and_intangibles_intangrev_252d_base_v034_signal,
    f18ri_f18_rd_and_intangibles_intangrev_504d_base_v035_signal,
    f18ri_f18_rd_and_intangibles_intangliab_21d_base_v036_signal,
    f18ri_f18_rd_and_intangibles_intangliab_252d_base_v037_signal,
    f18ri_f18_rd_and_intangibles_intangdebt_21d_base_v038_signal,
    f18ri_f18_rd_and_intangibles_intangdebt_252d_base_v039_signal,
    f18ri_f18_rd_and_intangibles_intangebitda_21d_base_v040_signal,
    f18ri_f18_rd_and_intangibles_intangebitda_252d_base_v041_signal,
    f18ri_f18_rd_and_intangibles_capexrd_21d_base_v042_signal,
    f18ri_f18_rd_and_intangibles_capexrd_252d_base_v043_signal,
    f18ri_f18_rd_and_intangibles_innovspend_21d_base_v044_signal,
    f18ri_f18_rd_and_intangibles_innovspend_252d_base_v045_signal,
    f18ri_f18_rd_and_intangibles_innovspend_504d_base_v046_signal,
    f18ri_f18_rd_and_intangibles_innovassets_21d_base_v047_signal,
    f18ri_f18_rd_and_intangibles_innovassets_252d_base_v048_signal,
    f18ri_f18_rd_and_intangibles_intangfrac_21d_base_v049_signal,
    f18ri_f18_rd_and_intangibles_intangmkt_252d_base_v050_signal,
    f18ri_f18_rd_and_intangibles_intangmkt_504d_base_v051_signal,
    f18ri_f18_rd_and_intangibles_tangassets_21d_base_v052_signal,
    f18ri_f18_rd_and_intangibles_tangassets_252d_base_v053_signal,
    f18ri_f18_rd_and_intangibles_rdgp_21d_base_v054_signal,
    f18ri_f18_rd_and_intangibles_rdgp_252d_base_v055_signal,
    f18ri_f18_rd_and_intangibles_rdgp_504d_base_v056_signal,
    f18ri_f18_rd_and_intangibles_rdopinc_21d_base_v057_signal,
    f18ri_f18_rd_and_intangibles_rdopinc_252d_base_v058_signal,
    f18ri_f18_rd_and_intangibles_rddebt_21d_base_v059_signal,
    f18ri_f18_rd_and_intangibles_rddebt_252d_base_v060_signal,
    f18ri_f18_rd_and_intangibles_rdliab_21d_base_v061_signal,
    f18ri_f18_rd_and_intangibles_rdliab_252d_base_v062_signal,
    f18ri_f18_rd_and_intangibles_rdshares_252d_base_v063_signal,
    f18ri_f18_rd_and_intangibles_rdcapex_rev_21d_base_v064_signal,
    f18ri_f18_rd_and_intangibles_rdcapex_rev_252d_base_v065_signal,
    f18ri_f18_rd_and_intangibles_intangni_21d_base_v066_signal,
    f18ri_f18_rd_and_intangibles_intangni_252d_base_v067_signal,
    f18ri_f18_rd_and_intangibles_intangfcf_21d_base_v068_signal,
    f18ri_f18_rd_and_intangibles_intangfcf_252d_base_v069_signal,
    f18ri_f18_rd_and_intangibles_intangps_21d_base_v070_signal,
    f18ri_f18_rd_and_intangibles_intangps_252d_base_v071_signal,
    f18ri_f18_rd_and_intangibles_innovps_21d_base_v072_signal,
    f18ri_f18_rd_and_intangibles_innovps_252d_base_v073_signal,
    f18ri_f18_rd_and_intangibles_intangrdcomp_21d_base_v074_signal,
    f18ri_f18_rd_and_intangibles_intangrdcomp_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_RD_AND_INTANGIBLES_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    eps = pd.Series(1.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="eps")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    gp = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="gp")
    workingcapital = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.006, n))), name="workingcapital")
    currentratio = pd.Series(1.8 * np.exp(np.cumsum(np.random.normal(0.0, 0.003, n))), name="currentratio")
    intexp = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.004, n))), name="intexp")
    liabilities = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.004, n))), name="liabilities")
    retearn = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="retearn")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    ev = marketcap + debt - 0.3 * marketcap
    ev = pd.Series(ev.values, name="ev")
    evebit = ev / opinc.replace(0, np.nan)
    evebit = pd.Series(evebit.values, name="evebit")
    evebitda = ev / ebitda.replace(0, np.nan)
    evebitda = pd.Series(evebitda.values, name="evebitda")
    pe = marketcap / netinc.replace(0, np.nan)
    pe = pd.Series(pe.values, name="pe")
    pb = marketcap / equity.replace(0, np.nan)
    pb = pd.Series(pb.values, name="pb")
    ps = marketcap / revenue.replace(0, np.nan)
    ps = pd.Series(ps.values, name="ps")
    cols = {"closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "eps": eps, "sharesbas": sharesbas, "opinc": opinc, "gp": gp, "workingcapital": workingcapital,
            "currentratio": currentratio, "intexp": intexp, "liabilities": liabilities, "retearn": retearn,
            "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps}
    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f18_rd_intensity", "_f18_intangibles")
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, f"{name} nunique={q.nunique()}"
        assert q.std() > 0, name
        assert not q.isna().all(), name
        if y1.iloc[504:].isna().mean() < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f18_rd_and_intangibles_base_001_075_claude: {n_features} features pass")
