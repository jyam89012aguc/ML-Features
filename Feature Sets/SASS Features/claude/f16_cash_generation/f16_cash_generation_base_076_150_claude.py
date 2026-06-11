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
    idx = np.arange(w, dtype=float)
    idx = idx - idx.mean()
    denom = (idx ** 2).sum()

    def _f(a):
        if np.isnan(a).any():
            return np.nan
        return float(np.dot(idx, a - a.mean()) / denom)
    return s.rolling(w, min_periods=w).apply(_f, raw=True)


def _semidn(s, w):
    dev = (s - _mean(s, w)).clip(upper=0)
    return (dev ** 2).rolling(w, min_periods=max(1, w // 2)).mean() ** 0.5


def _semiup(s, w):
    dev = (s - _mean(s, w)).clip(lower=0)
    return (dev ** 2).rolling(w, min_periods=max(1, w // 2)).mean() ** 0.5


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
# 076 FCF margin EWMA level (126d span) — persistent cash margin
def f16cg_f16_cash_generation_fcfmgnema_126d_base_v076_signal(fcf, revenue):
    b = _ewm(_f16_fcf_margin(fcf, revenue), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 077 FCF margin OLS slope over 504d (long cash-margin trend)
def f16cg_f16_cash_generation_fcfmgnslope_504d_base_v077_signal(fcf, revenue):
    m = _mean(_f16_fcf_margin(fcf, revenue), 63)
    b = _slope(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 078 FCF margin rolling 126d range (max-min) — short cash-margin variability
def f16cg_f16_cash_generation_fcfmgnrange_126d_base_v078_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    hi = m.rolling(126, min_periods=63).max()
    lo = m.rolling(126, min_periods=63).min()
    b = hi - lo
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 079 OCF margin percentile rank vs 252d history (operating-cash margin percentile)
def f16cg_f16_cash_generation_ocfmgnrank_252d_base_v079_signal(ncfo, revenue):
    b = _rank(_f16_ocf_margin(ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 080 OCF margin upside semi-deviation (operating-cash positive surprises)
def f16cg_f16_cash_generation_ocfupside_252d_base_v080_signal(ncfo, revenue):
    b = _semiup(_f16_ocf_margin(ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 081 Cash conversion (ncfo/netinc) 252d mean level
def f16cg_f16_cash_generation_cashconvmean_252d_base_v081_signal(ncfo, netinc):
    b = _mean(_f16_cash_conv(ncfo, netinc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 082 Cash conversion z-scored vs 252d history (conversion extremity)
def f16cg_f16_cash_generation_cashconvz_252d_base_v082_signal(ncfo, netinc):
    b = _z(_f16_cash_conv(ncfo, netinc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 083 Cash conversion OLS slope over 252d (conversion trend)
def f16cg_f16_cash_generation_cashconvslope_252d_base_v083_signal(ncfo, netinc):
    c = _mean(_f16_cash_conv(ncfo, netinc), 21)
    b = _slope(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 084 Cash conversion dispersion (rolling 252d std) — backing instability
def f16cg_f16_cash_generation_cashconvstd_252d_base_v084_signal(ncfo, netinc):
    b = _std(_f16_cash_conv(ncfo, netinc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 085 FCF conversion (fcf/netinc) z-scored vs 252d (free-cash backing extremity)
def f16cg_f16_cash_generation_fcfconvz_252d_base_v085_signal(fcf, netinc):
    b = _z(_f16_fcf_conv(fcf, netinc), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 086 FCF conversion percentile rank vs 504d history
def f16cg_f16_cash_generation_fcfconvrank_504d_base_v086_signal(fcf, netinc):
    b = _rank(_f16_fcf_conv(fcf, netinc), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 087 FCF/EBITDA percentile rank vs 252d (cash-conversion percentile)
def f16cg_f16_cash_generation_fcfebitdarank_252d_base_v087_signal(fcf, ebitda):
    b = _rank(_f16_fcf_ebitda(fcf, ebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 088 FCF/EBITDA OLS slope over 252d (cash-conversion trend)
def f16cg_f16_cash_generation_fcfebitdaslope_252d_base_v088_signal(fcf, ebitda):
    r = _mean(_f16_fcf_ebitda(fcf, ebitda), 21)
    b = _slope(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 089 OCF/EBITDA 252d mean level (operating-cash backing of profit)
def f16cg_f16_cash_generation_ocfebitdamean_252d_base_v089_signal(ncfo, ebitda):
    b = _mean(_f16_ocf_ebitda(ncfo, ebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 090 OCF/EBITDA OLS slope over 504d (long operating-cash conversion trend)
def f16cg_f16_cash_generation_ocfebitdaslope_504d_base_v090_signal(ncfo, ebitda):
    r = _mean(_f16_ocf_ebitda(ncfo, ebitda), 63)
    b = _slope(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 091 Capex coverage (ncfo/capex) percentile rank vs 504d (self-funding percentile)
def f16cg_f16_cash_generation_capexcovrank_504d_base_v091_signal(ncfo, capex):
    b = _rank(_f16_capex_cover(ncfo, capex), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 092 Capex coverage OLS slope over 252d (self-funding trajectory)
def f16cg_f16_cash_generation_capexcovslope_252d_base_v092_signal(ncfo, capex):
    cov = _f16_capex_cover(ncfo, capex)
    lg = _mean(np.sign(cov) * np.log1p(cov.abs()), 21)
    b = _slope(lg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 093 Capex coverage distributional skew over 252d (self-funding asymmetry)
def f16cg_f16_cash_generation_capexcovskew_252d_base_v093_signal(ncfo, capex):
    cov = _f16_capex_cover(ncfo, capex)
    lg = np.sign(cov) * np.log1p(cov.abs())
    b = lg.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 094 Capex intensity (capex/revenue) 252d mean level
def f16cg_f16_cash_generation_capexint_252d_base_v094_signal(capex, revenue):
    b = _mean(_f16_capex_intensity(capex, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 095 Capex intensity OLS slope over 252d (rising/falling reinvestment burden)
def f16cg_f16_cash_generation_capexintslope_252d_base_v095_signal(capex, revenue):
    ci = _mean(_f16_capex_intensity(capex, revenue), 21)
    b = _slope(ci, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 096 Accrual ratio (ncfo-netinc)/revenue OLS slope over 252d (accrual-quality trend)
def f16cg_f16_cash_generation_accrualslope_252d_base_v096_signal(netinc, ncfo, revenue):
    a = _mean(_f16_accrual(netinc, ncfo, revenue), 21)
    b = _slope(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 097 Accrual ratio percentile rank vs 504d (accrual-quality percentile)
def f16cg_f16_cash_generation_accrualrank_504d_base_v097_signal(netinc, ncfo, revenue):
    b = _rank(_f16_accrual(netinc, ncfo, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 098 Accrual ratio dispersion (rolling 252d std) — accrual volatility
def f16cg_f16_cash_generation_accrualstd_252d_base_v098_signal(netinc, ncfo, revenue):
    b = _std(_f16_accrual(netinc, ncfo, revenue), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 099 Cash-vs-accounting spread (fcf-netinc)/revenue z-scored vs 252d
def f16cg_f16_cash_generation_cashvsacctz_252d_base_v099_signal(fcf, netinc, revenue):
    spread = (fcf - netinc) / revenue.replace(0, np.nan)
    b = _z(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 100 Cash-vs-accounting spread OLS slope over 252d (cash-quality trajectory)
def f16cg_f16_cash_generation_cashvsacctslope_252d_base_v100_signal(fcf, netinc, revenue):
    spread = _mean((fcf - netinc) / revenue.replace(0, np.nan), 21)
    b = _slope(spread, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 101 Capex drag (ncfo-fcf)/revenue z-scored vs 252d (capex-consumption extremity)
def f16cg_f16_cash_generation_capexdragz_252d_base_v101_signal(ncfo, fcf, revenue):
    drag = (ncfo - fcf) / revenue.replace(0, np.nan)
    b = _z(drag, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 102 Reinvestment cash yield (ncfo-capex)/revenue percentile rank vs 252d
def f16cg_f16_cash_generation_reinvyieldrank_252d_base_v102_signal(ncfo, capex, revenue):
    b = _rank((ncfo - capex) / revenue.replace(0, np.nan), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 103 Reinvestment cash yield OLS slope over 504d (free-cash-generation trend)
def f16cg_f16_cash_generation_reinvyieldslope_504d_base_v103_signal(ncfo, capex, revenue):
    s = _mean((ncfo - capex) / revenue.replace(0, np.nan), 63)
    b = _slope(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 104 Self-funding (ncfo-capex)/ebitda z-scored vs 504d (self-funding extremity, long)
def f16cg_f16_cash_generation_selffundz_504d_base_v104_signal(ncfo, capex, ebitda):
    s = ((ncfo - capex) / ebitda.replace(0, np.nan)).clip(-10, 10)
    b = _z(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 105 Total cash yield (fcf+ncfo)/(2*revenue) 252d mean level
def f16cg_f16_cash_generation_totcashmean_252d_base_v105_signal(fcf, ncfo, revenue):
    y = (fcf + ncfo) / (2.0 * revenue).replace(0, np.nan)
    b = _mean(y, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 106 Total cash yield percentile rank vs 504d (blended cash-yield percentile)
def f16cg_f16_cash_generation_totcashrank_504d_base_v106_signal(fcf, ncfo, revenue):
    y = (fcf + ncfo) / (2.0 * revenue).replace(0, np.nan)
    b = _rank(y, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 107 FCF-to-OCF survival ratio (fcf/ncfo) z-scored vs 252d
def f16cg_f16_cash_generation_fcftoocfz_252d_base_v107_signal(fcf, ncfo):
    r = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 108 FCF-to-OCF survival ratio percentile rank vs 504d
def f16cg_f16_cash_generation_fcftoocfrank_504d_base_v108_signal(fcf, ncfo):
    r = (fcf / ncfo.replace(0, np.nan)).clip(-5, 5)
    b = _rank(r, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 109 Cash-margin wedge |fcf-margin - ocf-margin| z-scored vs 252d
def f16cg_f16_cash_generation_mgnwedgez_252d_base_v109_signal(fcf, ncfo, revenue):
    fm = _f16_fcf_margin(fcf, revenue)
    om = _f16_ocf_margin(ncfo, revenue)
    b = _z((fm - om).abs(), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 110 Cash-margin wedge OLS slope over 252d (widening/narrowing capex wedge)
def f16cg_f16_cash_generation_mgnwedgeslope_252d_base_v110_signal(fcf, ncfo, revenue):
    fm = _f16_fcf_margin(fcf, revenue)
    om = _f16_ocf_margin(ncfo, revenue)
    w = _mean((fm - om).abs(), 21)
    b = _slope(w, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 111 Cash-conversion vs FCF-conversion spread z-scored vs 252d
def f16cg_f16_cash_generation_convspreadz_252d_base_v111_signal(ncfo, fcf, netinc):
    cc = _f16_cash_conv(ncfo, netinc)
    fc = _f16_fcf_conv(fcf, netinc)
    b = _z(cc - fc, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 112 Cash earnings power: ocf-margin x tanh(capex-coverage) 252d mean (self-funded margin)
def f16cg_f16_cash_generation_ocfselffund_252d_base_v112_signal(ncfo, revenue, capex):
    om = _f16_ocf_margin(ncfo, revenue)
    cov = _f16_capex_cover(ncfo, capex)
    b = _mean(om * np.tanh(cov / 5.0), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 113 FCF-margin x accrual interaction 252d mean (cash margin with low accrual)
def f16cg_f16_cash_generation_fcfaccrualx_252d_base_v113_signal(fcf, revenue, netinc, ncfo):
    fm = _f16_fcf_margin(fcf, revenue)
    a = _f16_accrual(netinc, ncfo, revenue)
    b = _mean(fm * np.tanh(10.0 * a), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 114 Cash-quality composite rank: rank(fcf/ebitda)+rank(ocf-margin) blended (504d)
def f16cg_f16_cash_generation_qualcomp2_504d_base_v114_signal(fcf, ebitda, ncfo, revenue):
    r1 = _rank(_f16_fcf_ebitda(fcf, ebitda), 504)
    r2 = _rank(_f16_ocf_margin(ncfo, revenue), 504)
    b = (r1 + r2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 115 Rolling correlation of fcf and revenue over 252d (cash-tracks-sales co-movement)
def f16cg_f16_cash_generation_fcfrevcorr_252d_base_v115_signal(fcf, revenue):
    b = fcf.rolling(252, min_periods=126).corr(revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 116 Rolling correlation of fcf and netinc over 252d (cash-vs-earnings tracking)
def f16cg_f16_cash_generation_fcfnicorr_252d_base_v116_signal(fcf, netinc):
    b = fcf.rolling(252, min_periods=126).corr(netinc)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 117 Rolling correlation of ncfo and revenue over 504d (operating-cash-vs-sales tracking)
def f16cg_f16_cash_generation_ocfrevcorr_504d_base_v117_signal(ncfo, revenue):
    b = ncfo.rolling(504, min_periods=252).corr(revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 118 Rolling correlation of capex and revenue over 252d (investment-vs-sales scaling)
def f16cg_f16_cash_generation_capexrevcorr_252d_base_v118_signal(capex, revenue):
    b = capex.rolling(252, min_periods=126).corr(revenue)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 119 FCF signed-log scale z-scored vs 252d (cash-generation magnitude extremity)
def f16cg_f16_cash_generation_fcfscalez_252d_base_v119_signal(fcf):
    lv = np.sign(fcf) * np.log1p(fcf.abs())
    b = _z(lv, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 120 OCF signed-log scale OLS slope over 504d (operating-cash-scale trend)
def f16cg_f16_cash_generation_ocfscaleslope_504d_base_v120_signal(ncfo):
    lv = np.sign(ncfo) * np.log1p(ncfo.abs())
    s = _mean(lv, 63)
    b = _slope(s, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 121 FCF margin acceleration (change of the 63d-change) — cash-margin momentum shift
def f16cg_f16_cash_generation_fcfmgnaccel_base_v121_signal(fcf, revenue):
    m = _mean(_f16_fcf_margin(fcf, revenue), 21)
    ch = _chg(m, 63)
    b = _chg(ch, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 122 OCF margin year-over-year change (252d) — annual operating-cash margin shift
def f16cg_f16_cash_generation_ocfmgnyoy_252d_base_v122_signal(ncfo, revenue):
    m = _mean(_f16_ocf_margin(ncfo, revenue), 63)
    b = _chg(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 123 Cash conversion year-over-year change (252d) — annual backing shift
def f16cg_f16_cash_generation_convyoy_252d_base_v123_signal(ncfo, netinc):
    c = _mean(_f16_cash_conv(ncfo, netinc), 63)
    b = _chg(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 124 Capex coverage quarterly change (63d) — short-horizon self-funding momentum
def f16cg_f16_cash_generation_covchg_63d_base_v124_signal(ncfo, capex):
    cov = _f16_capex_cover(ncfo, capex)
    lg = _mean(np.sign(cov) * np.log1p(cov.abs()), 21)
    b = _chg(lg, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 125 FCF margin term structure (63d mean minus 252d mean) — short vs long cash margin
def f16cg_f16_cash_generation_fcfmgnterm_252d_base_v125_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    b = _mean(m, 63) - _mean(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 126 OCF margin term structure (126d mean minus 504d mean)
def f16cg_f16_cash_generation_ocfmgnterm_504d_base_v126_signal(ncfo, revenue):
    m = _f16_ocf_margin(ncfo, revenue)
    b = _mean(m, 126) - _mean(m, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 127 OCF/EBITDA term structure (63d mean minus 252d mean) — operating-cash conversion tilt
def f16cg_f16_cash_generation_ocfebitdaterm_252d_base_v127_signal(ncfo, ebitda):
    r = _f16_ocf_ebitda(ncfo, ebitda)
    b = _mean(r, 63) - _mean(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 128 Capex intensity term structure (63d mean minus 252d mean) — reinvestment pace shift
def f16cg_f16_cash_generation_capexintterm_252d_base_v128_signal(capex, revenue):
    ci = _f16_capex_intensity(capex, revenue)
    b = _mean(ci, 63) - _mean(ci, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 129 FCF margin information ratio over 504d (long-horizon cash-margin reliability)
def f16cg_f16_cash_generation_fcfir_504d_base_v129_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    b = _mean(m, 504) / _std(m, 504).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 130 OCF margin information ratio over 252d (operating-cash reliability)
def f16cg_f16_cash_generation_ocfir_252d_base_v130_signal(ncfo, revenue):
    m = _f16_ocf_margin(ncfo, revenue)
    b = _mean(m, 252) / _std(m, 252).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 131 FCF/EBITDA downside semi-deviation over 252d (conversion shortfall risk)
def f16cg_f16_cash_generation_fcfebitdadn_252d_base_v131_signal(fcf, ebitda):
    b = _semidn(_f16_fcf_ebitda(fcf, ebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 132 OCF/EBITDA dispersion (rolling 252d std) — operating-cash conversion instability
def f16cg_f16_cash_generation_ocfebitdastd_252d_base_v132_signal(ncfo, ebitda):
    b = _std(_f16_ocf_ebitda(ncfo, ebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 133 Capex coverage downside semi-deviation over 252d (self-funding shortfall risk)
def f16cg_f16_cash_generation_covdn_252d_base_v133_signal(ncfo, capex):
    cov = _f16_capex_cover(ncfo, capex)
    lg = np.sign(cov) * np.log1p(cov.abs())
    b = _semidn(lg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 134 FCF margin distributional skew over 504d (long cash-margin asymmetry)
def f16cg_f16_cash_generation_fcfmgnskew_504d_base_v134_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    b = m.rolling(504, min_periods=252).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 135 OCF margin distributional skew over 252d (operating-cash asymmetry)
def f16cg_f16_cash_generation_ocfmgnskew_252d_base_v135_signal(ncfo, revenue):
    m = _f16_ocf_margin(ncfo, revenue)
    b = m.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 136 Cash conversion distributional skew over 252d (backing asymmetry)
def f16cg_f16_cash_generation_convskew_252d_base_v136_signal(ncfo, netinc):
    c = _f16_cash_conv(ncfo, netinc)
    b = c.rolling(252, min_periods=126).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 137 FCF margin rolling 504d percentile rank (long cash-margin percentile)
def f16cg_f16_cash_generation_fcfmgnrank504_base_v137_signal(fcf, revenue):
    b = _rank(_f16_fcf_margin(fcf, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 138 OCF/revenue minus FCF/revenue capex wedge percentile rank vs 504d
def f16cg_f16_cash_generation_capexwedgerank_504d_base_v138_signal(ncfo, fcf, revenue):
    wedge = (ncfo - fcf) / revenue.replace(0, np.nan)
    b = _rank(wedge, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 139 FCF margin EWMA displacement (level minus slow EMA) — cash-margin drift
def f16cg_f16_cash_generation_fcfmgndisp_252d_base_v139_signal(fcf, revenue):
    m = _f16_fcf_margin(fcf, revenue)
    b = m - _ewm(m, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 140 Cash conversion EWMA displacement (level minus slow EMA) — backing drift
def f16cg_f16_cash_generation_convdisp_252d_base_v140_signal(ncfo, netinc):
    c = _f16_cash_conv(ncfo, netinc)
    b = c - _ewm(c, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 141 FCF/EBITDA quarterly change (63d) — short-horizon conversion momentum
def f16cg_f16_cash_generation_fcfebitdachg_63d_base_v141_signal(fcf, ebitda):
    r = _mean(_f16_fcf_ebitda(fcf, ebitda), 21)
    b = _chg(r, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 142 Capex burden (capex/ncfo) z-scored vs 252d (reinvestment-intensity extremity)
def f16cg_f16_cash_generation_capexburdenz_252d_base_v142_signal(capex, ncfo):
    r = (capex / ncfo.replace(0, np.nan)).clip(-5, 5)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 143 Reinvestment rate capex/(ncfo) 252d mean level (share of OCF reinvested)
def f16cg_f16_cash_generation_reinvrate_252d_base_v143_signal(capex, ncfo):
    r = (capex / ncfo.replace(0, np.nan)).clip(-5, 5)
    b = _mean(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 144 Cash-on-cash spread (fcf/ebitda minus capex/revenue) z-scored vs 252d
def f16cg_f16_cash_generation_cashoncashz_252d_base_v144_signal(fcf, ebitda, capex, revenue):
    a = _f16_fcf_ebitda(fcf, ebitda)
    ci = _f16_capex_intensity(capex, revenue)
    b = _z(a - ci, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 145 FCF margin downside semi-deviation over 504d (long cash-margin shortfall risk)
def f16cg_f16_cash_generation_fcfmgndn_504d_base_v145_signal(fcf, revenue):
    b = _semidn(_f16_fcf_margin(fcf, revenue), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 146 OCF margin best-quarter max over 252d (operating-cash ceiling)
def f16cg_f16_cash_generation_ocfceiling_252d_base_v146_signal(ncfo, revenue):
    q = _mean(_f16_ocf_margin(ncfo, revenue), 63)
    b = q.rolling(252, min_periods=126).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 147 Accrual-free proxy (ncfo-netinc)/ebitda z-scored vs 252d
def f16cg_f16_cash_generation_accrualebz_252d_base_v147_signal(netinc, ncfo, ebitda):
    a = ((ncfo - netinc) / ebitda.replace(0, np.nan)).clip(-10, 10)
    b = _z(a, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 148 Cash-generation composite slope: slope of (fcf+ncfo)/(2*rev) over 504d
def f16cg_f16_cash_generation_totcashslope_504d_base_v148_signal(fcf, ncfo, revenue):
    y = _mean((fcf + ncfo) / (2.0 * revenue).replace(0, np.nan), 63)
    b = _slope(y, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 149 EBITDA-to-FCF leakage (ebitda-fcf)/ebitda z-scored vs 252d (leakage extremity)
def f16cg_f16_cash_generation_fcfleakz_252d_base_v149_signal(fcf, ebitda):
    r = ((ebitda - fcf) / ebitda.replace(0, np.nan)).clip(-10, 10)
    b = _z(r, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 150 Cash-generation breadth soft-score over 504d (durable multi-test composite)
def f16cg_f16_cash_generation_breadth_504d_base_v150_signal(fcf, revenue, ncfo, netinc, capex):
    t1 = np.tanh(20.0 * _f16_fcf_margin(fcf, revenue))
    t2 = np.tanh(2.0 * (_f16_cash_conv(ncfo, netinc) - 1.0))
    t3 = np.tanh(0.5 * (_f16_capex_cover(ncfo, capex) - 1.0))
    b = _mean((t1 + t2 + t3) / 3.0, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16cg_f16_cash_generation_fcfmgnema_126d_base_v076_signal,
    f16cg_f16_cash_generation_fcfmgnslope_504d_base_v077_signal,
    f16cg_f16_cash_generation_fcfmgnrange_126d_base_v078_signal,
    f16cg_f16_cash_generation_ocfmgnrank_252d_base_v079_signal,
    f16cg_f16_cash_generation_ocfupside_252d_base_v080_signal,
    f16cg_f16_cash_generation_cashconvmean_252d_base_v081_signal,
    f16cg_f16_cash_generation_cashconvz_252d_base_v082_signal,
    f16cg_f16_cash_generation_cashconvslope_252d_base_v083_signal,
    f16cg_f16_cash_generation_cashconvstd_252d_base_v084_signal,
    f16cg_f16_cash_generation_fcfconvz_252d_base_v085_signal,
    f16cg_f16_cash_generation_fcfconvrank_504d_base_v086_signal,
    f16cg_f16_cash_generation_fcfebitdarank_252d_base_v087_signal,
    f16cg_f16_cash_generation_fcfebitdaslope_252d_base_v088_signal,
    f16cg_f16_cash_generation_ocfebitdamean_252d_base_v089_signal,
    f16cg_f16_cash_generation_ocfebitdaslope_504d_base_v090_signal,
    f16cg_f16_cash_generation_capexcovrank_504d_base_v091_signal,
    f16cg_f16_cash_generation_capexcovslope_252d_base_v092_signal,
    f16cg_f16_cash_generation_capexcovskew_252d_base_v093_signal,
    f16cg_f16_cash_generation_capexint_252d_base_v094_signal,
    f16cg_f16_cash_generation_capexintslope_252d_base_v095_signal,
    f16cg_f16_cash_generation_accrualslope_252d_base_v096_signal,
    f16cg_f16_cash_generation_accrualrank_504d_base_v097_signal,
    f16cg_f16_cash_generation_accrualstd_252d_base_v098_signal,
    f16cg_f16_cash_generation_cashvsacctz_252d_base_v099_signal,
    f16cg_f16_cash_generation_cashvsacctslope_252d_base_v100_signal,
    f16cg_f16_cash_generation_capexdragz_252d_base_v101_signal,
    f16cg_f16_cash_generation_reinvyieldrank_252d_base_v102_signal,
    f16cg_f16_cash_generation_reinvyieldslope_504d_base_v103_signal,
    f16cg_f16_cash_generation_selffundz_504d_base_v104_signal,
    f16cg_f16_cash_generation_totcashmean_252d_base_v105_signal,
    f16cg_f16_cash_generation_totcashrank_504d_base_v106_signal,
    f16cg_f16_cash_generation_fcftoocfz_252d_base_v107_signal,
    f16cg_f16_cash_generation_fcftoocfrank_504d_base_v108_signal,
    f16cg_f16_cash_generation_mgnwedgez_252d_base_v109_signal,
    f16cg_f16_cash_generation_mgnwedgeslope_252d_base_v110_signal,
    f16cg_f16_cash_generation_convspreadz_252d_base_v111_signal,
    f16cg_f16_cash_generation_ocfselffund_252d_base_v112_signal,
    f16cg_f16_cash_generation_fcfaccrualx_252d_base_v113_signal,
    f16cg_f16_cash_generation_qualcomp2_504d_base_v114_signal,
    f16cg_f16_cash_generation_fcfrevcorr_252d_base_v115_signal,
    f16cg_f16_cash_generation_fcfnicorr_252d_base_v116_signal,
    f16cg_f16_cash_generation_ocfrevcorr_504d_base_v117_signal,
    f16cg_f16_cash_generation_capexrevcorr_252d_base_v118_signal,
    f16cg_f16_cash_generation_fcfscalez_252d_base_v119_signal,
    f16cg_f16_cash_generation_ocfscaleslope_504d_base_v120_signal,
    f16cg_f16_cash_generation_fcfmgnaccel_base_v121_signal,
    f16cg_f16_cash_generation_ocfmgnyoy_252d_base_v122_signal,
    f16cg_f16_cash_generation_convyoy_252d_base_v123_signal,
    f16cg_f16_cash_generation_covchg_63d_base_v124_signal,
    f16cg_f16_cash_generation_fcfmgnterm_252d_base_v125_signal,
    f16cg_f16_cash_generation_ocfmgnterm_504d_base_v126_signal,
    f16cg_f16_cash_generation_ocfebitdaterm_252d_base_v127_signal,
    f16cg_f16_cash_generation_capexintterm_252d_base_v128_signal,
    f16cg_f16_cash_generation_fcfir_504d_base_v129_signal,
    f16cg_f16_cash_generation_ocfir_252d_base_v130_signal,
    f16cg_f16_cash_generation_fcfebitdadn_252d_base_v131_signal,
    f16cg_f16_cash_generation_ocfebitdastd_252d_base_v132_signal,
    f16cg_f16_cash_generation_covdn_252d_base_v133_signal,
    f16cg_f16_cash_generation_fcfmgnskew_504d_base_v134_signal,
    f16cg_f16_cash_generation_ocfmgnskew_252d_base_v135_signal,
    f16cg_f16_cash_generation_convskew_252d_base_v136_signal,
    f16cg_f16_cash_generation_fcfmgnrank504_base_v137_signal,
    f16cg_f16_cash_generation_capexwedgerank_504d_base_v138_signal,
    f16cg_f16_cash_generation_fcfmgndisp_252d_base_v139_signal,
    f16cg_f16_cash_generation_convdisp_252d_base_v140_signal,
    f16cg_f16_cash_generation_fcfebitdachg_63d_base_v141_signal,
    f16cg_f16_cash_generation_capexburdenz_252d_base_v142_signal,
    f16cg_f16_cash_generation_reinvrate_252d_base_v143_signal,
    f16cg_f16_cash_generation_cashoncashz_252d_base_v144_signal,
    f16cg_f16_cash_generation_fcfmgndn_504d_base_v145_signal,
    f16cg_f16_cash_generation_ocfceiling_252d_base_v146_signal,
    f16cg_f16_cash_generation_accrualebz_252d_base_v147_signal,
    f16cg_f16_cash_generation_totcashslope_504d_base_v148_signal,
    f16cg_f16_cash_generation_fcfleakz_252d_base_v149_signal,
    f16cg_f16_cash_generation_breadth_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_CASH_GENERATION_REGISTRY_076_150 = REGISTRY


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

    print("OK f16_cash_generation_base_076_150_claude: %d features pass" % n_features)
