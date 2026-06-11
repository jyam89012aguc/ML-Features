import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_FIVEYEAR = 1260
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
    return s.rolling(w, min_periods=max(1, w // 3)).rank(pct=True) - 0.5


def _ewm(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _chg(s, w):
    return s - s.shift(w)


def _slope(s, w):
    # OLS slope of s over a trailing window (per-step)
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float(np.dot(idx, a - a.mean()) / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


# ===== f16 cash-generation domain primitives (LEVEL ratios) =====
def _f16_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _f16_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _f16_cash_conv(ncfo, netinc):
    return (ncfo / netinc.replace(0, np.nan)).clip(-10, 10)


def _f16_fcf_conv(fcf, netinc):
    return (fcf / netinc.replace(0, np.nan)).clip(-10, 10)


def _f16_fcf_ebitda(fcf, ebitda):
    return (fcf / ebitda.replace(0, np.nan)).clip(-10, 10)


def _f16_ocf_ebitda(ncfo, ebitda):
    return (ncfo / ebitda.replace(0, np.nan)).clip(-10, 10)


def _f16_capex_cover(ncfo, capex):
    return (ncfo / capex.replace(0, np.nan)).clip(-20, 20)


def _f16_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _f16_accrual(netinc, ncfo, revenue):
    return (ncfo - netinc) / revenue.replace(0, np.nan)


# ============================================================
# 001 FCF margin (fcf/revenue) — 252d smoothed level
def f16cg_f16_cash_generation_fcfmgn_252d_base_v001_signal(fcf, revenue):
    b = _mean(_f16_fcf_margin(fcf, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 002 FCF margin z-scored vs own 504d history (de-trended level)
def f16cg_f16_cash_generation_fcfmgnz_504d_base_v002_signal(fcf, revenue):
    b = _z(_f16_fcf_margin(fcf, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 003 FCF margin percentile rank vs own 252d history
def f16cg_f16_cash_generation_fcfmgnrank_252d_base_v003_signal(fcf, revenue):
    b = _rank(_f16_fcf_margin(fcf, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 004 OCF margin (ncfo/revenue) — 252d smoothed level
def f16cg_f16_cash_generation_ocfmgn_252d_base_v004_signal(ncfo, revenue):
    b = _mean(_f16_ocf_margin(ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 005 OCF margin z-scored vs own 252d history
def f16cg_f16_cash_generation_ocfmgnz_252d_base_v005_signal(ncfo, revenue):
    b = _z(_f16_ocf_margin(ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 006 Cash conversion (ncfo/netinc) — 126d EWMA level
def f16cg_f16_cash_generation_cashconv_252d_base_v006_signal(ncfo, netinc):
    b = _ewm(_f16_cash_conv(ncfo, netinc), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 007 Cash conversion percentile rank vs own 504d history
def f16cg_f16_cash_generation_cashconvrank_504d_base_v007_signal(ncfo, netinc):
    b = _rank(_f16_cash_conv(ncfo, netinc), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 008 FCF/EBITDA x cash-conversion interaction, ranked (cash quality on two bases)
def f16cg_f16_cash_generation_fcfebitdax_504d_base_v008_signal(fcf, ebitda, ncfo, netinc):
    fe = _f16_fcf_ebitda(fcf, ebitda)
    cc = _f16_cash_conv(ncfo, netinc)
    b = _rank(fe * np.tanh(cc / 3.0), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 009 Rolling correlation of ncfo and netinc over 252d (cash-earnings co-movement quality)
def f16cg_f16_cash_generation_ocfnicorr_252d_base_v009_signal(ncfo, netinc):
    b = ncfo.rolling(252, min_periods=126).corr(netinc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 010 Capex coverage (ncfo/capex) percentile rank vs 252d history (self-funding level)
def f16cg_f16_cash_generation_capexcov_252d_base_v010_signal(ncfo, capex):
    b = _rank(_f16_capex_cover(ncfo, capex), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 011 Capex-cushion OLS slope over 504d (self-funding trend, level of slope)
def f16cg_f16_cash_generation_capexcushion_504d_base_v011_signal(ncfo, capex, revenue):
    cushion = _mean((ncfo - capex) / revenue.replace(0, np.nan), 63)
    b = _slope(cushion, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 012 Accrual-free earnings proxy (ncfo-netinc)/revenue — 252d level
def f16cg_f16_cash_generation_accrual_252d_base_v012_signal(netinc, ncfo, revenue):
    b = _mean(_f16_accrual(netinc, ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 013 FCF-margin information ratio (mean/std over 252d) — quality of cash margin
def f16cg_f16_cash_generation_fcfqual_252d_base_v013_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    b = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 014 Capex drag = (ncfo-fcf)/revenue — 252d level (capex consumption of sales)
def f16cg_f16_cash_generation_capexdrag_252d_base_v014_signal(ncfo, fcf, revenue):
    b = _mean((ncfo - fcf) / revenue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 015 Cash-vs-accounting spread (fcf-netinc)/revenue — 252d level
def f16cg_f16_cash_generation_cashvsacct_252d_base_v015_signal(fcf, netinc, revenue):
    b = _mean((fcf - netinc) / revenue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 016 Cash-conversion stability = |mean|/std of ncfo/netinc over 252d
def f16cg_f16_cash_generation_convstab_252d_base_v016_signal(ncfo, netinc):
    c = _f16_cash_conv(ncfo, netinc)
    b = _mean(c, 252).abs() / _std(c, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 017 FCF-margin change over a quarter (cash-margin momentum, level of slope)
def f16cg_f16_cash_generation_fcfmgnchg_252d_base_v017_signal(fcf, revenue):
    m = _mean(_f16_fcf_margin(fcf, revenue), 252)
    b = _chg(m, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 018 OCF-margin percentile rank vs 504d history
def f16cg_f16_cash_generation_ocfyield_504d_base_v018_signal(ncfo, revenue):
    b = _rank(_f16_ocf_margin(ncfo, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 019 Rolling correlation of fcf and ebitda over 252d (cash-tracks-profit co-movement)
def f16cg_f16_cash_generation_fcfebitdacorr_252d_base_v019_signal(fcf, ebitda):
    b = fcf.rolling(252, min_periods=126).corr(ebitda)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 020 Capex intensity (capex/revenue) z-scored vs 252d history, negated (cash-light extremity)
def f16cg_f16_cash_generation_capexlight_252d_base_v020_signal(capex, revenue):
    b = -_z(_f16_capex_intensity(capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 021 FCF reconciliation gap percentile rank: reconstructed (ncfo-capex)/rev vs reported fcf/rev
def f16cg_f16_cash_generation_fcfrecongap_252d_base_v021_signal(ncfo, capex, fcf, revenue):
    recon = (ncfo - capex) / revenue.replace(0, np.nan)
    rep = _f16_fcf_margin(fcf, revenue)
    b = _rank(recon - rep, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 022 Cash-conversion EWMA term tilt (fast minus slow EMA of ncfo/netinc)
def f16cg_f16_cash_generation_convtilt_252d_base_v022_signal(ncfo, netinc):
    c = _f16_cash_conv(ncfo, netinc)
    b = _ewm(c, 42) - _ewm(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 023 FCF-margin distributional skew over 252d (asymmetry of cash-margin path)
def f16cg_f16_cash_generation_fcfskew_252d_base_v023_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    b = m.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 024 OCF-margin x capex-coverage interaction (cash-rich and self-funding)
def f16cg_f16_cash_generation_ocfxcov_252d_base_v024_signal(ncfo, revenue, capex):
    ocfm = _mean(_f16_ocf_margin(ncfo, revenue), 252)
    cov = _mean(_f16_capex_cover(ncfo, capex), 252)
    b = ocfm * np.tanh(cov / 5.0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 025 EBITDA capex consumption (ncfo-fcf)/ebitda z-scored vs 252d history
def f16cg_f16_cash_generation_ebitdacapex_252d_base_v025_signal(ncfo, fcf, ebitda):
    b = _z(((ncfo - fcf) / ebitda.replace(0, np.nan)).clip(-10, 10), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 026 Cash conversion percentile rank vs a long 1260d history
def f16cg_f16_cash_generation_nicashback_1260d_base_v026_signal(ncfo, netinc):
    b = _rank(_f16_cash_conv(ncfo, netinc), 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 027 FCF-margin dispersion (rolling std) negated — cash-flow smoothness
def f16cg_f16_cash_generation_fcfdisp_252d_base_v027_signal(fcf, revenue):
    b = -_std(_f16_fcf_margin(fcf, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 028 FCF/EBITDA change over a half-year (cash-conversion trajectory level)
def f16cg_f16_cash_generation_fcfebitdachg_252d_base_v028_signal(fcf, ebitda):
    r = _mean(_f16_fcf_ebitda(fcf, ebitda), 252)
    b = _chg(r, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 029 Accrual ratio z-scored vs 504d history (accrual extremity)
def f16cg_f16_cash_generation_accrualz_504d_base_v029_signal(netinc, ncfo, revenue):
    b = _z(_f16_accrual(netinc, ncfo, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 030 Self-funding (ncfo-capex)/ebitda z-scored vs 252d history (self-fund extremity)
def f16cg_f16_cash_generation_selffund_252d_base_v030_signal(ncfo, capex, ebitda):
    s = ((ncfo - capex) / ebitda.replace(0, np.nan)).clip(-10, 10)
    b = _z(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 031 Cash-ROA proxy: fcf-margin x ocf-margin (compounded cash quality level)
def f16cg_f16_cash_generation_cashroa_252d_base_v031_signal(fcf, ncfo, revenue):
    fcfm = _f16_fcf_margin(fcf, revenue)
    ocfm = _f16_ocf_margin(ncfo, revenue).clip(-5, 5)
    b = _mean(fcfm * ocfm, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 032 Capex-coverage surplus margin (ncfo-capex)/(|ncfo|+|capex|) — bounded self-fund
def f16cg_f16_cash_generation_covsurplus_252d_base_v032_signal(ncfo, capex):
    den = (ncfo.abs() + capex.abs()).replace(0, np.nan)
    b = _ewm((ncfo - capex) / den, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 033 OCF-margin gap vs own 504d mean (operating-cash margin vs long baseline)
def f16cg_f16_cash_generation_ocfgap_504d_base_v033_signal(ncfo, revenue):
    m = _f16_ocf_margin(ncfo, revenue)
    b = m - _mean(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 034 OCF-margin change over a half-year (operating-cash margin momentum)
def f16cg_f16_cash_generation_ocfmgnchg_252d_base_v034_signal(ncfo, revenue):
    m = _mean(_f16_ocf_margin(ncfo, revenue), 63)
    b = _chg(m, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 035 Accrual-ratio reversal: 63d mean minus 252d mean (mean-reversion of accruals)
def f16cg_f16_cash_generation_accrualrev_252d_base_v035_signal(netinc, ncfo, revenue):
    a = _f16_accrual(netinc, ncfo, revenue)
    b = _mean(a, 63) - _mean(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 036 FCF/EBITDA downside semi-deviation over 252d (conversion shortfall risk)
def f16cg_f16_cash_generation_fcfebitdadn_252d_base_v036_signal(fcf, ebitda):
    r = _f16_fcf_ebitda(fcf, ebitda)
    dev = (r - _mean(r, 252)).clip(upper=0)
    b = (dev ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 037 Cash-conversion excess over unity (ncfo/netinc - 1), 252d level
def f16cg_f16_cash_generation_convexcess_252d_base_v037_signal(ncfo, netinc):
    c = _f16_cash_conv(ncfo, netinc)
    b = _mean(c - 1.0, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 038 FCF signed-log scale change over a year (cash-generation scale trajectory)
def f16cg_f16_cash_generation_fcflevelchg_252d_base_v038_signal(fcf):
    lv = np.sign(fcf) * np.log1p(fcf.abs())
    b = _chg(_mean(lv, 63), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 039 OCF signed-log scale z-scored vs 504d history (operating-cash scale extremity)
def f16cg_f16_cash_generation_ocflevel_504d_base_v039_signal(ncfo):
    lv = np.sign(ncfo) * np.log1p(ncfo.abs())
    b = _z(lv, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 040 FCF-to-OCF survival ratio (fcf/ncfo) 252d level — share of OCF kept free
def f16cg_f16_cash_generation_fcftoocf_252d_base_v040_signal(fcf, ncfo):
    r = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    b = _mean(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 041 Blended cash margin (avg of fcf-margin and ocf-margin) z-scored vs 504d history
def f16cg_f16_cash_generation_blendmgn_504d_base_v041_signal(fcf, ncfo, revenue):
    fm = _f16_fcf_margin(fcf, revenue)
    om = _f16_ocf_margin(ncfo, revenue)
    b = _z((fm + om) / 2.0, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 042 Cash-margin wedge |fcf-margin - ocf-margin| 252d level (capex-driven gap)
def f16cg_f16_cash_generation_mgnwedge_252d_base_v042_signal(fcf, ncfo, revenue):
    fm = _f16_fcf_margin(fcf, revenue)
    om = _f16_ocf_margin(ncfo, revenue)
    b = _mean((fm - om).abs(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 043 Rolling correlation of ncfo and capex over 252d (co-movement of cash & investment)
def f16cg_f16_cash_generation_ncfocapexcorr_252d_base_v043_signal(ncfo, capex):
    b = ncfo.rolling(252, min_periods=126).corr(capex)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 044 OCF/EBITDA dispersion (rolling 252d std) — operating-cash conversion instability
def f16cg_f16_cash_generation_ebitdaleak_252d_base_v044_signal(ncfo, ebitda):
    r = _f16_ocf_ebitda(ncfo, ebitda)
    b = _std(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 045 Cash earnings power: fcf-margin x tanh(cash-conversion) 252d interaction level
def f16cg_f16_cash_generation_cashpower_252d_base_v045_signal(fcf, revenue, ncfo, netinc):
    fm = _f16_fcf_margin(fcf, revenue)
    cc = _f16_cash_conv(ncfo, netinc)
    b = _mean(fm * np.tanh(cc / 3.0), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 046 FCF-margin rank minus OCF-margin rank (free-vs-operating cash leadership)
def f16cg_f16_cash_generation_mgnrankspr_504d_base_v046_signal(fcf, ncfo, revenue):
    fr = _rank(_f16_fcf_margin(fcf, revenue), 504)
    orr = _rank(_f16_ocf_margin(ncfo, revenue), 504)
    b = fr - orr
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 047 Cash-conversion floor (rolling 252d min of ncfo/netinc) — worst-case backing
def f16cg_f16_cash_generation_convfloor_252d_base_v047_signal(ncfo, netinc):
    c = _f16_cash_conv(ncfo, netinc)
    b = c.rolling(252, min_periods=126).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 048 FCF-margin yearly range (max-min over 252d) — cash-margin variability span
def f16cg_f16_cash_generation_fcfspan_252d_base_v048_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    hi = m.rolling(252, min_periods=126).max()
    lo = m.rolling(252, min_periods=126).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 049 Reinvestment-adjusted cash yield (ncfo-capex)/revenue percentile rank vs 504d
def f16cg_f16_cash_generation_reinvyield_504d_base_v049_signal(ncfo, capex, revenue):
    s = (ncfo - capex) / revenue.replace(0, np.nan)
    b = _rank(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 050 Capex burden on operating cash (capex/ncfo) 252d level
def f16cg_f16_cash_generation_capexburden_252d_base_v050_signal(capex, ncfo):
    r = (capex / ncfo.replace(0, np.nan)).clip(-5, 5)
    b = _mean(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 051 OCF-margin downside semi-deviation (operating-cash shortfall risk over 252d)
def f16cg_f16_cash_generation_ocfdownside_252d_base_v051_signal(ncfo, revenue):
    m = _f16_ocf_margin(ncfo, revenue)
    dev = (m - _mean(m, 252)).clip(upper=0)
    b = (dev ** 2).rolling(252, min_periods=126).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 052 FCF-margin downside semi-deviation negated (cash-margin shortfall risk, inverse)
def f16cg_f16_cash_generation_fcfdownside_252d_base_v052_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    dev = (m - _mean(m, 252)).clip(upper=0)
    b = -((dev ** 2).rolling(252, min_periods=126).mean() ** 0.5)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 053 OCF-margin EWMA-displacement (level minus slow EMA) — operating-cash drift
def f16cg_f16_cash_generation_ocfdisp_252d_base_v053_signal(ncfo, revenue):
    m = _f16_ocf_margin(ncfo, revenue)
    b = m - _ewm(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 054 Cash-conv minus FCF-conv spread (capex wedge in net-income backing) 252d level
def f16cg_f16_cash_generation_convspread_252d_base_v054_signal(ncfo, fcf, netinc):
    cc = _f16_cash_conv(ncfo, netinc)
    fc = _f16_fcf_conv(fcf, netinc)
    b = _mean(cc - fc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 055 FCF conversion of net income (fcf/netinc) 252d level
def f16cg_f16_cash_generation_fcfconv_252d_base_v055_signal(fcf, netinc):
    b = _mean(_f16_fcf_conv(fcf, netinc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 056 OCF/EBITDA change over a quarter (operating-cash conversion trajectory)
def f16cg_f16_cash_generation_ocfebitdachg_252d_base_v056_signal(ncfo, ebitda):
    r = _mean(_f16_ocf_ebitda(ncfo, ebitda), 252)
    b = _chg(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 057 FCF-margin inter-quartile range over 252d (cash-margin dispersion width)
def f16cg_f16_cash_generation_fcfiqr_252d_base_v057_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    q75 = m.rolling(252, min_periods=126).quantile(0.75)
    q25 = m.rolling(252, min_periods=126).quantile(0.25)
    b = q75 - q25
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 058 FCF signed-log scale z-scored vs 1260d history (multi-year cash-scale extremity)
def f16cg_f16_cash_generation_fcfscalez_1260d_base_v058_signal(fcf):
    lv = np.sign(fcf) * np.log1p(fcf.abs())
    b = _z(lv, 1260)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 059 Cash-on-cash spread (fcf/ebitda minus capex/revenue) change over a half-year
def f16cg_f16_cash_generation_cashoncash_252d_base_v059_signal(fcf, ebitda, capex, revenue):
    a = _f16_fcf_ebitda(fcf, ebitda)
    ci = _f16_capex_intensity(capex, revenue)
    s = _mean(a - ci, 63)
    b = _chg(s, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 060 Operating-cash dominance ncfo/(|ncfo|+|capex|) rolling 252d range (regime width)
def f16cg_f16_cash_generation_ocfdominance_252d_base_v060_signal(ncfo, capex):
    den = (ncfo.abs() + capex.abs()).replace(0, np.nan)
    d = ncfo / den
    hi = d.rolling(252, min_periods=126).max()
    lo = d.rolling(252, min_periods=126).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 061 Capex-cushion z-scored vs 252d history (self-funding extremity vs own baseline)
def f16cg_f16_cash_generation_cushionz_252d_base_v061_signal(ncfo, capex, revenue):
    cushion = (ncfo - capex) / revenue.replace(0, np.nan)
    b = _z(cushion, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 062 Cash-quality composite: rank(fcf-margin) + rank(cash-conv) blended (504d)
def f16cg_f16_cash_generation_qualcomposite_504d_base_v062_signal(fcf, revenue, ncfo, netinc):
    r1 = _rank(_f16_fcf_margin(fcf, revenue), 504)
    r2 = _rank(_f16_cash_conv(ncfo, netinc), 504)
    b = (r1 + r2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 063 FCF/EBITDA minus OCF/EBITDA wedge change over a quarter (capex-bite trajectory)
def f16cg_f16_cash_generation_ebitdawedge_252d_base_v063_signal(fcf, ncfo, ebitda):
    fe = _f16_fcf_ebitda(fcf, ebitda)
    oe = _f16_ocf_ebitda(ncfo, ebitda)
    s = _mean(fe - oe, 63)
    b = _chg(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 064 FCF-margin OLS slope over 252d (cash-margin trend, level of slope)
def f16cg_f16_cash_generation_fcfslope_252d_base_v064_signal(fcf, revenue):
    m = _mean(_f16_fcf_margin(fcf, revenue), 63)
    b = _slope(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 065 Capex-coverage signed-log EWMA level (stable self-funding, 252d span)
def f16cg_f16_cash_generation_capexcovlog_504d_base_v065_signal(ncfo, capex):
    cov = _f16_capex_cover(ncfo, capex)
    b = _ewm(np.sign(cov) * np.log1p(cov.abs()), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 066 Cash-conversion term structure (63d mean minus 252d mean)
def f16cg_f16_cash_generation_convterm_252d_base_v066_signal(ncfo, netinc):
    c = _f16_cash_conv(ncfo, netinc)
    b = _mean(c, 63) - _mean(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 067 Self-funded cash quality: rank of cash-conversion x capex-coverage interaction (504d)
def f16cg_f16_cash_generation_selffundqual_504d_base_v067_signal(ncfo, netinc, capex):
    cc = _f16_cash_conv(ncfo, netinc)
    cov = _f16_capex_cover(ncfo, capex)
    b = _rank(np.tanh(cc / 3.0) * np.tanh(cov / 5.0), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 068 Rolling correlation of ncfo and ebitda over 504d (cash-tracks-EBITDA co-movement)
def f16cg_f16_cash_generation_ocfebitdacorr_504d_base_v068_signal(ncfo, ebitda):
    b = ncfo.rolling(504, min_periods=252).corr(ebitda)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 069 OCF-to-size [log(ncfo)-log(revenue)] change over a year (cash-scale-vs-sales drift)
def f16cg_f16_cash_generation_ocfsize_252d_base_v069_signal(ncfo, revenue):
    ln = np.sign(ncfo) * np.log1p(ncfo.abs())
    lr = np.log1p(revenue.abs())
    s = _mean(ln - lr, 63)
    b = _chg(s, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 070 FCF-margin distributional kurtosis over 252d (cash-margin tail-heaviness)
def f16cg_f16_cash_generation_fcfkurt_252d_base_v070_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    b = m.rolling(252, min_periods=126).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 071 Cash-conversion above-unity persistence (smoothed indicator of ncfo>=netinc)
def f16cg_f16_cash_generation_convpersist_252d_base_v071_signal(ncfo, netinc):
    c = _f16_cash_conv(ncfo, netinc)
    soft = np.tanh(3.0 * (c - 1.0))
    b = _ewm(soft, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 072 EBITDA-to-FCF leakage (ebitda-fcf)/ebitda change over a quarter (leakage trajectory)
def f16cg_f16_cash_generation_fcfleak_252d_base_v072_signal(fcf, ebitda):
    r = ((ebitda - fcf) / ebitda.replace(0, np.nan)).clip(-10, 10)
    s = _mean(r, 63)
    b = _chg(s, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 073 Total cash yield (fcf+ncfo)/(2*revenue) z-scored vs 252d history
def f16cg_f16_cash_generation_totcashyield_252d_base_v073_signal(fcf, ncfo, revenue):
    y = (fcf + ncfo) / (2.0 * revenue).replace(0, np.nan)
    b = _z(y, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 074 Accrual-ratio dispersion (rolling 252d std of (ncfo-netinc)/ebitda) — accrual volatility
def f16cg_f16_cash_generation_accrualvol_252d_base_v074_signal(netinc, ncfo, ebitda):
    a = ((ncfo - netinc) / ebitda.replace(0, np.nan)).clip(-10, 10)
    b = _std(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 075 Cash-generation breadth: soft-count of cash tests, de-meaned (composite level)
def f16cg_f16_cash_generation_breadth_252d_base_v075_signal(fcf, revenue, ncfo, netinc, capex):
    t1 = np.tanh(20.0 * _f16_fcf_margin(fcf, revenue))
    t2 = np.tanh(2.0 * (_f16_cash_conv(ncfo, netinc) - 1.0))
    t3 = np.tanh(0.5 * (_f16_capex_cover(ncfo, capex) - 1.0))
    b = _mean((t1 + t2 + t3) / 3.0, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16cg_f16_cash_generation_fcfmgn_252d_base_v001_signal,
    f16cg_f16_cash_generation_fcfmgnz_504d_base_v002_signal,
    f16cg_f16_cash_generation_fcfmgnrank_252d_base_v003_signal,
    f16cg_f16_cash_generation_ocfmgn_252d_base_v004_signal,
    f16cg_f16_cash_generation_ocfmgnz_252d_base_v005_signal,
    f16cg_f16_cash_generation_cashconv_252d_base_v006_signal,
    f16cg_f16_cash_generation_cashconvrank_504d_base_v007_signal,
    f16cg_f16_cash_generation_fcfebitdax_504d_base_v008_signal,
    f16cg_f16_cash_generation_ocfnicorr_252d_base_v009_signal,
    f16cg_f16_cash_generation_capexcov_252d_base_v010_signal,
    f16cg_f16_cash_generation_capexcushion_504d_base_v011_signal,
    f16cg_f16_cash_generation_accrual_252d_base_v012_signal,
    f16cg_f16_cash_generation_fcfqual_252d_base_v013_signal,
    f16cg_f16_cash_generation_capexdrag_252d_base_v014_signal,
    f16cg_f16_cash_generation_cashvsacct_252d_base_v015_signal,
    f16cg_f16_cash_generation_convstab_252d_base_v016_signal,
    f16cg_f16_cash_generation_fcfmgnchg_252d_base_v017_signal,
    f16cg_f16_cash_generation_ocfyield_504d_base_v018_signal,
    f16cg_f16_cash_generation_fcfebitdacorr_252d_base_v019_signal,
    f16cg_f16_cash_generation_capexlight_252d_base_v020_signal,
    f16cg_f16_cash_generation_fcfrecongap_252d_base_v021_signal,
    f16cg_f16_cash_generation_convtilt_252d_base_v022_signal,
    f16cg_f16_cash_generation_fcfskew_252d_base_v023_signal,
    f16cg_f16_cash_generation_ocfxcov_252d_base_v024_signal,
    f16cg_f16_cash_generation_ebitdacapex_252d_base_v025_signal,
    f16cg_f16_cash_generation_nicashback_1260d_base_v026_signal,
    f16cg_f16_cash_generation_fcfdisp_252d_base_v027_signal,
    f16cg_f16_cash_generation_fcfebitdachg_252d_base_v028_signal,
    f16cg_f16_cash_generation_accrualz_504d_base_v029_signal,
    f16cg_f16_cash_generation_selffund_252d_base_v030_signal,
    f16cg_f16_cash_generation_cashroa_252d_base_v031_signal,
    f16cg_f16_cash_generation_covsurplus_252d_base_v032_signal,
    f16cg_f16_cash_generation_ocfgap_504d_base_v033_signal,
    f16cg_f16_cash_generation_ocfmgnchg_252d_base_v034_signal,
    f16cg_f16_cash_generation_accrualrev_252d_base_v035_signal,
    f16cg_f16_cash_generation_fcfebitdadn_252d_base_v036_signal,
    f16cg_f16_cash_generation_convexcess_252d_base_v037_signal,
    f16cg_f16_cash_generation_fcflevelchg_252d_base_v038_signal,
    f16cg_f16_cash_generation_ocflevel_504d_base_v039_signal,
    f16cg_f16_cash_generation_fcftoocf_252d_base_v040_signal,
    f16cg_f16_cash_generation_blendmgn_504d_base_v041_signal,
    f16cg_f16_cash_generation_mgnwedge_252d_base_v042_signal,
    f16cg_f16_cash_generation_ncfocapexcorr_252d_base_v043_signal,
    f16cg_f16_cash_generation_ebitdaleak_252d_base_v044_signal,
    f16cg_f16_cash_generation_cashpower_252d_base_v045_signal,
    f16cg_f16_cash_generation_mgnrankspr_504d_base_v046_signal,
    f16cg_f16_cash_generation_convfloor_252d_base_v047_signal,
    f16cg_f16_cash_generation_fcfspan_252d_base_v048_signal,
    f16cg_f16_cash_generation_reinvyield_504d_base_v049_signal,
    f16cg_f16_cash_generation_capexburden_252d_base_v050_signal,
    f16cg_f16_cash_generation_ocfdownside_252d_base_v051_signal,
    f16cg_f16_cash_generation_fcfdownside_252d_base_v052_signal,
    f16cg_f16_cash_generation_ocfdisp_252d_base_v053_signal,
    f16cg_f16_cash_generation_convspread_252d_base_v054_signal,
    f16cg_f16_cash_generation_fcfconv_252d_base_v055_signal,
    f16cg_f16_cash_generation_ocfebitdachg_252d_base_v056_signal,
    f16cg_f16_cash_generation_fcfiqr_252d_base_v057_signal,
    f16cg_f16_cash_generation_fcfscalez_1260d_base_v058_signal,
    f16cg_f16_cash_generation_cashoncash_252d_base_v059_signal,
    f16cg_f16_cash_generation_ocfdominance_252d_base_v060_signal,
    f16cg_f16_cash_generation_cushionz_252d_base_v061_signal,
    f16cg_f16_cash_generation_qualcomposite_504d_base_v062_signal,
    f16cg_f16_cash_generation_ebitdawedge_252d_base_v063_signal,
    f16cg_f16_cash_generation_fcfslope_252d_base_v064_signal,
    f16cg_f16_cash_generation_capexcovlog_504d_base_v065_signal,
    f16cg_f16_cash_generation_convterm_252d_base_v066_signal,
    f16cg_f16_cash_generation_selffundqual_504d_base_v067_signal,
    f16cg_f16_cash_generation_ocfebitdacorr_504d_base_v068_signal,
    f16cg_f16_cash_generation_ocfsize_252d_base_v069_signal,
    f16cg_f16_cash_generation_fcfkurt_252d_base_v070_signal,
    f16cg_f16_cash_generation_convpersist_252d_base_v071_signal,
    f16cg_f16_cash_generation_fcfleak_252d_base_v072_signal,
    f16cg_f16_cash_generation_totcashyield_252d_base_v073_signal,
    f16cg_f16_cash_generation_accrualvol_252d_base_v074_signal,
    f16cg_f16_cash_generation_breadth_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_CASH_GENERATION_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    revenue = _fund(1, base=1e9, drift=0.02, vol=0.05).rename("revenue")
    ebitda = _fund(2, base=2e8, drift=0.01, vol=0.13).rename("ebitda")
    ncfo = _fund(3, base=1.8e8, drift=-0.04, vol=0.22, allow_neg=True).rename("ncfo")
    netinc = _fund(4, base=1.2e8, drift=-0.06, vol=0.28, allow_neg=True).rename("netinc")
    fcf = _fund(5, base=1.0e8, drift=-0.05, vol=0.25, allow_neg=True).rename("fcf")
    capex = _fund(6, base=8e7, drift=0.03, vol=0.10).rename("capex")

    cols = {"revenue": revenue, "ebitda": ebitda, "ncfo": ncfo,
            "netinc": netinc, "fcf": fcf, "capex": capex}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 50, "%s nunique=%d" % (name, q.nunique())
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

    print("OK f16_cash_generation_base_001_075_claude: %d features pass" % n_features)
