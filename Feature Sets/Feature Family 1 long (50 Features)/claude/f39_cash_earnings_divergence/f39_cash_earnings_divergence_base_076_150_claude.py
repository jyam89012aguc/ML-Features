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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


# ===== folder domain primitives =====
def _f39_cash_earnings_div(fcf, netinc):
    return fcf - netinc


def _f39_cash_earnings_div_norm(fcf, netinc, scale):
    return (fcf - netinc) / scale.abs().replace(0, np.nan)


def _f39_fcf_minus_netinc_roll(fcf, netinc, w):
    gap = fcf - netinc
    return gap.rolling(w, min_periods=max(1, w // 2)).mean()


def _f39_ncfo_minus_netinc(ncfo, netinc):
    return ncfo - netinc


# 21d gap zscore over 63d window scaled by closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapz_63d_base_v076_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _z(_mean(gap, 21), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap zscore over 126d window
def f39ced_f39_cash_earnings_divergence_fcfgapz_126d_base_v077_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _z(_mean(gap, 63), 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d count of days where fcf > netinc (positive divergence frequency)
def f39ced_f39_cash_earnings_divergence_posdivfreq_252d_base_v078_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    pos = (gap > 0).astype(float)
    result = pos.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 504d count of days where fcf > netinc
def f39ced_f39_cash_earnings_divergence_posdivfreq_504d_base_v079_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    pos = (gap > 0).astype(float)
    result = pos.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d frequency where ncfo > netinc
def f39ced_f39_cash_earnings_divergence_posncfofreq_252d_base_v080_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    pos = (gap > 0).astype(float)
    result = pos.rolling(252, min_periods=63).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 504d frequency where ncfo > netinc
def f39ced_f39_cash_earnings_divergence_posncfofreq_504d_base_v081_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    pos = (gap > 0).astype(float)
    result = pos.rolling(504, min_periods=126).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap mean / 252d gap mean (positive only) ratio (skewness of divergence)
def f39ced_f39_cash_earnings_divergence_fcfposnegratio_252d_base_v082_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    pos = gap.where(gap > 0, 0.0).rolling(252, min_periods=63).mean()
    neg = gap.where(gap < 0, 0.0).abs().rolling(252, min_periods=63).mean().replace(0, np.nan)
    result = pos / neg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap pos vs neg ratio
def f39ced_f39_cash_earnings_divergence_fcfposnegratio_63d_base_v083_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    pos = gap.where(gap > 0, 0.0).rolling(63, min_periods=21).mean()
    neg = gap.where(gap < 0, 0.0).abs().rolling(63, min_periods=21).mean().replace(0, np.nan)
    result = pos / neg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# rolling 252d slope-like change of (fcf-netinc) gap
def f39ced_f39_cash_earnings_divergence_fcfgapchg_252d_base_v084_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    rolling_gap = _mean(gap, 63)
    result = _diff(rolling_gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d change of fcf-netinc gap
def f39ced_f39_cash_earnings_divergence_fcfgapchg_63d_base_v085_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    rolling_gap = _mean(gap, 21)
    result = _diff(rolling_gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo-netinc gap level relative to 504d level (recent quality vs persistent)
def f39ced_f39_cash_earnings_divergence_ncfogapdelta_252d_base_v086_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    short = _mean(gap, 252)
    long_ = _mean(gap, 504)
    result = (short - long_) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo-netinc level vs 252d
def f39ced_f39_cash_earnings_divergence_ncfogapdelta_63d_base_v087_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    short = _mean(gap, 63)
    long_ = _mean(gap, 252)
    result = (short - long_) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# fcf gap as fraction of opinc (operating cash conversion proxy)
def f39ced_f39_cash_earnings_divergence_fcfgapopinc_252d_base_v088_signal(fcf, netinc, opinc, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, opinc)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf gap as fraction of opinc
def f39ced_f39_cash_earnings_divergence_fcfgapopinc_63d_base_v089_signal(fcf, netinc, opinc, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, opinc)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d fcf-netinc gap as fraction of gp (gross profit)
def f39ced_f39_cash_earnings_divergence_fcfgapgp_252d_base_v090_signal(fcf, netinc, gp, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, gp)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d fcf-netinc gap as fraction of gp
def f39ced_f39_cash_earnings_divergence_fcfgapgp_63d_base_v091_signal(fcf, netinc, gp, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, gp)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap area (sum of magnitudes)
def f39ced_f39_cash_earnings_divergence_fcfgaparea_252d_base_v092_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc).abs()
    result = gap.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap area
def f39ced_f39_cash_earnings_divergence_fcfgaparea_63d_base_v093_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc).abs()
    result = gap.rolling(63, min_periods=21).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap area
def f39ced_f39_cash_earnings_divergence_fcfgaparea_504d_base_v094_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc).abs()
    result = gap.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d max gap value (worst positive divergence)
def f39ced_f39_cash_earnings_divergence_fcfgapquantilehi_252d_base_v095_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(252, min_periods=63).quantile(0.9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d min gap value (worst negative divergence)
def f39ced_f39_cash_earnings_divergence_fcfgapquantilelo_252d_base_v096_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(252, min_periods=63).quantile(0.1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d high quantile of gap
def f39ced_f39_cash_earnings_divergence_fcfgapquantilehi_504d_base_v097_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(504, min_periods=126).quantile(0.9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d low quantile of gap
def f39ced_f39_cash_earnings_divergence_fcfgapquantilelo_504d_base_v098_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(504, min_periods=126).quantile(0.1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo gap high quantile
def f39ced_f39_cash_earnings_divergence_ncfogapquantilehi_252d_base_v099_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = gap.rolling(252, min_periods=63).quantile(0.9) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo gap low quantile
def f39ced_f39_cash_earnings_divergence_ncfogapquantilelo_252d_base_v100_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    result = gap.rolling(252, min_periods=63).quantile(0.1) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap interquartile range
def f39ced_f39_cash_earnings_divergence_fcfgapiqr_252d_base_v101_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    hi = gap.rolling(252, min_periods=63).quantile(0.75)
    lo = gap.rolling(252, min_periods=63).quantile(0.25)
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap interquartile range
def f39ced_f39_cash_earnings_divergence_fcfgapiqr_504d_base_v102_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    hi = gap.rolling(504, min_periods=126).quantile(0.75)
    lo = gap.rolling(504, min_periods=126).quantile(0.25)
    result = (hi - lo) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap median
def f39ced_f39_cash_earnings_divergence_fcfgapmedian_252d_base_v103_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(252, min_periods=63).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap median
def f39ced_f39_cash_earnings_divergence_fcfgapmedian_504d_base_v104_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(504, min_periods=126).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d skew of gap distribution
def f39ced_f39_cash_earnings_divergence_fcfgapskew_252d_base_v105_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(252, min_periods=63).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d skew of gap
def f39ced_f39_cash_earnings_divergence_fcfgapskew_504d_base_v106_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(504, min_periods=126).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d kurtosis of gap distribution
def f39ced_f39_cash_earnings_divergence_fcfgapkurt_252d_base_v107_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(252, min_periods=63).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d kurtosis of gap
def f39ced_f39_cash_earnings_divergence_fcfgapkurt_504d_base_v108_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = gap.rolling(504, min_periods=126).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap standard deviation normalized by mean (CV of divergence)
def f39ced_f39_cash_earnings_divergence_fcfgapcv_252d_base_v109_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    sd = _std(gap, 252)
    m = _mean(gap.abs(), 252).replace(0, np.nan)
    result = (sd / m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d gap CV
def f39ced_f39_cash_earnings_divergence_fcfgapcv_504d_base_v110_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    sd = _std(gap, 504)
    m = _mean(gap.abs(), 504).replace(0, np.nan)
    result = (sd / m) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative netinc minus cumulative fcf (cumulative quality drag)
def f39ced_f39_cash_earnings_divergence_qualitydrag_252d_base_v111_signal(fcf, netinc, closeadj):
    drag = -(_f39_cash_earnings_div(fcf, netinc))
    result = drag.rolling(252, min_periods=63).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative netinc minus cumulative fcf
def f39ced_f39_cash_earnings_divergence_qualitydrag_504d_base_v112_signal(fcf, netinc, closeadj):
    drag = -(_f39_cash_earnings_div(fcf, netinc))
    result = drag.rolling(504, min_periods=126).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × marketcap-like proxy (closeadj × sharesbas)
def f39ced_f39_cash_earnings_divergence_fcfgapxmc_252d_base_v113_signal(fcf, netinc, sharesbas, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    mc = closeadj * sharesbas
    result = _mean(gap, 252) * closeadj / mc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × marketcap-like proxy
def f39ced_f39_cash_earnings_divergence_fcfgapxmc_63d_base_v114_signal(fcf, netinc, sharesbas, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    mc = closeadj * sharesbas
    result = _mean(gap, 63) * closeadj / mc.replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap interaction with currentratio (liquidity-cash quality)
def f39ced_f39_cash_earnings_divergence_fcfgapxcr_252d_base_v115_signal(fcf, netinc, currentratio, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap interaction with currentratio
def f39ced_f39_cash_earnings_divergence_fcfgapxcr_63d_base_v116_signal(fcf, netinc, currentratio, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) * currentratio * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ratio of |fcf-netinc| sum to |netinc| sum (relative gap intensity)
def f39ced_f39_cash_earnings_divergence_relgapintensity_252d_base_v117_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc).abs()
    base = netinc.abs()
    result = gap.rolling(252, min_periods=63).sum() / base.rolling(252, min_periods=63).sum().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d relative gap intensity
def f39ced_f39_cash_earnings_divergence_relgapintensity_63d_base_v118_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc).abs()
    base = netinc.abs()
    result = gap.rolling(63, min_periods=21).sum() / base.rolling(63, min_periods=21).sum().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo-netinc relative gap intensity
def f39ced_f39_cash_earnings_divergence_ncforelintensity_252d_base_v119_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc).abs()
    base = netinc.abs()
    result = gap.rolling(252, min_periods=63).sum() / base.rolling(252, min_periods=63).sum().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo-netinc relative gap intensity
def f39ced_f39_cash_earnings_divergence_ncforelintensity_63d_base_v120_signal(ncfo, netinc, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc).abs()
    base = netinc.abs()
    result = gap.rolling(63, min_periods=21).sum() / base.rolling(63, min_periods=21).sum().replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d divergence persistence: rolling 252 std of gap mean changes
def f39ced_f39_cash_earnings_divergence_fcfgappersist_252d_base_v121_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    delta = _diff(_mean(gap, 63), 21)
    result = _std(delta, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d divergence persistence
def f39ced_f39_cash_earnings_divergence_fcfgappersist_504d_base_v122_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    delta = _diff(_mean(gap, 126), 63)
    result = _std(delta, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative ncfo to cumulative netinc ratio minus 1 (rolling cash coverage ratio)
def f39ced_f39_cash_earnings_divergence_ncforatiocum_252d_base_v123_signal(ncfo, netinc, closeadj):
    cum_ncfo = ncfo.rolling(252, min_periods=63).sum()
    cum_ni = netinc.rolling(252, min_periods=63).sum()
    coverage = cum_ncfo / cum_ni.abs().replace(0, np.nan) - 1.0
    aux = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    result = (coverage + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative ncfo to netinc ratio
def f39ced_f39_cash_earnings_divergence_ncforatiocum_504d_base_v124_signal(ncfo, netinc, closeadj):
    cum_ncfo = ncfo.rolling(504, min_periods=126).sum()
    cum_ni = netinc.rolling(504, min_periods=126).sum()
    coverage = cum_ncfo / cum_ni.abs().replace(0, np.nan) - 1.0
    aux = _f39_ncfo_minus_netinc(ncfo, netinc) * 0.0
    result = (coverage + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative fcf to cumulative netinc ratio minus 1
def f39ced_f39_cash_earnings_divergence_fcfratiocum_252d_base_v125_signal(fcf, netinc, closeadj):
    cum_fcf = fcf.rolling(252, min_periods=63).sum()
    cum_ni = netinc.rolling(252, min_periods=63).sum()
    coverage = cum_fcf / cum_ni.abs().replace(0, np.nan) - 1.0
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    result = (coverage + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cumulative fcf to netinc ratio
def f39ced_f39_cash_earnings_divergence_fcfratiocum_504d_base_v126_signal(fcf, netinc, closeadj):
    cum_fcf = fcf.rolling(504, min_periods=126).sum()
    cum_ni = netinc.rolling(504, min_periods=126).sum()
    coverage = cum_fcf / cum_ni.abs().replace(0, np.nan) - 1.0
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    result = (coverage + aux) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EMA of fcf-netinc ratio
def f39ced_f39_cash_earnings_divergence_fcfratioema_252d_base_v127_signal(fcf, netinc, closeadj):
    ratio = _safe_div(fcf, netinc) - 1.0
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    result = (ratio + aux).ewm(span=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EMA of fcf-netinc ratio
def f39ced_f39_cash_earnings_divergence_fcfratioema_63d_base_v128_signal(fcf, netinc, closeadj):
    ratio = _safe_div(fcf, netinc) - 1.0
    aux = _f39_cash_earnings_div(fcf, netinc) * 0.0
    result = (ratio + aux).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × ebitda growth (cash-quality with growth)
def f39ced_f39_cash_earnings_divergence_fcfgapebgrow_252d_base_v129_signal(fcf, netinc, ebitda, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    growth = ebitda.pct_change(252).fillna(0.0)
    result = _mean(gap, 252) * growth * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × ebitda growth
def f39ced_f39_cash_earnings_divergence_fcfgapebgrow_63d_base_v130_signal(fcf, netinc, ebitda, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    growth = ebitda.pct_change(63).fillna(0.0)
    result = _mean(gap, 63) * growth * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cumulative ncfo - cumulative netinc gap weighted by closeadj × eps
def f39ced_f39_cash_earnings_divergence_ncfocumxeps_252d_base_v131_signal(ncfo, netinc, eps, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    cum = gap.rolling(252, min_periods=63).sum()
    result = cum * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative ncfo gap × eps
def f39ced_f39_cash_earnings_divergence_ncfocumxeps_63d_base_v132_signal(ncfo, netinc, eps, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    cum = gap.rolling(63, min_periods=21).sum()
    result = cum * eps * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × debt change interaction (deteriorating quality + leverage)
def f39ced_f39_cash_earnings_divergence_fcfgapdebtchg_252d_base_v133_signal(fcf, netinc, debt, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    debt_chg = debt.pct_change(252).fillna(0.0)
    result = _mean(gap, 252) * debt_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × debt change
def f39ced_f39_cash_earnings_divergence_fcfgapdebtchg_63d_base_v134_signal(fcf, netinc, debt, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    debt_chg = debt.pct_change(63).fillna(0.0)
    result = _mean(gap, 63) * debt_chg * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap relative to liabilities scaled
def f39ced_f39_cash_earnings_divergence_fcfgaplia_252d_base_v135_signal(fcf, netinc, liabilities, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, liabilities)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap relative to liabilities scaled
def f39ced_f39_cash_earnings_divergence_fcfgaplia_63d_base_v136_signal(fcf, netinc, liabilities, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, liabilities)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap relative to retained earnings (longer-term cash quality)
def f39ced_f39_cash_earnings_divergence_fcfgapretearn_252d_base_v137_signal(fcf, netinc, retearn, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, retearn)
    result = _mean(gap, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap relative to retained earnings
def f39ced_f39_cash_earnings_divergence_fcfgapretearn_63d_base_v138_signal(fcf, netinc, retearn, closeadj):
    gap = _f39_cash_earnings_div_norm(fcf, netinc, retearn)
    result = _mean(gap, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: cash-earnings gap z-score × ebitda growth
def f39ced_f39_cash_earnings_divergence_fcfgapzxgrow_252d_base_v139_signal(fcf, netinc, ebitda, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    z = _z(_mean(gap, 63), 252)
    growth = ebitda.pct_change(252).fillna(0.0)
    result = z * growth * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: cash-earnings gap z × revenue growth
def f39ced_f39_cash_earnings_divergence_fcfgapzxrev_63d_base_v140_signal(fcf, netinc, revenue, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    z = _z(_mean(gap, 21), 63)
    growth = revenue.pct_change(63).fillna(0.0)
    result = z * growth * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ncfo gap × revenue growth × closeadj (quality-adjusted growth)
def f39ced_f39_cash_earnings_divergence_ncfogapxrevgrow_252d_base_v141_signal(ncfo, netinc, revenue, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    growth = revenue.pct_change(252).fillna(0.0)
    result = _mean(gap, 252) * growth * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ncfo gap × revenue growth
def f39ced_f39_cash_earnings_divergence_ncfogapxrevgrow_63d_base_v142_signal(ncfo, netinc, revenue, closeadj):
    gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    growth = revenue.pct_change(63).fillna(0.0)
    result = _mean(gap, 63) * growth * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d combined gap (fcf+ncfo - 2*netinc) average, scaled
def f39ced_f39_cash_earnings_divergence_combinedgap_252d_base_v143_signal(fcf, ncfo, netinc, closeadj):
    fcf_gap = _f39_cash_earnings_div(fcf, netinc)
    ncfo_gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    combined = fcf_gap + ncfo_gap
    result = _mean(combined, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d combined gap (fcf+ncfo gaps)
def f39ced_f39_cash_earnings_divergence_combinedgap_63d_base_v144_signal(fcf, ncfo, netinc, closeadj):
    fcf_gap = _f39_cash_earnings_div(fcf, netinc)
    ncfo_gap = _f39_ncfo_minus_netinc(ncfo, netinc)
    combined = fcf_gap + ncfo_gap
    result = _mean(combined, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d net-of-capex cash quality (ncfo - capex - netinc gap)
def f39ced_f39_cash_earnings_divergence_netofcapex_252d_base_v145_signal(ncfo, netinc, capex, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc) - capex.abs()
    result = _mean(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 63d net-of-capex cash quality
def f39ced_f39_cash_earnings_divergence_netofcapex_63d_base_v146_signal(ncfo, netinc, capex, closeadj):
    base = _f39_ncfo_minus_netinc(ncfo, netinc) - capex.abs()
    result = _mean(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d gap × current netinc magnitude × closeadj (notional divergence)
def f39ced_f39_cash_earnings_divergence_fcfgapnotional_252d_base_v147_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 252) * closeadj * netinc.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d gap × current netinc magnitude × closeadj
def f39ced_f39_cash_earnings_divergence_fcfgapnotional_63d_base_v148_signal(fcf, netinc, closeadj):
    gap = _f39_cash_earnings_div(fcf, netinc)
    result = _mean(gap, 63) * closeadj * netinc.abs()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite: average of fcf gap normalized by assets and ncfo gap normalized by assets
def f39ced_f39_cash_earnings_divergence_dualgapassets_252d_base_v149_signal(fcf, ncfo, netinc, assets, closeadj):
    fcf_gap = _f39_cash_earnings_div_norm(fcf, netinc, assets)
    ncfo_gap = _f39_ncfo_minus_netinc(ncfo, netinc) / assets.abs().replace(0, np.nan)
    combined = (fcf_gap + ncfo_gap) / 2.0
    result = _mean(combined, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ultimate cash-earnings divergence composite (avg gap scaled by revenue, weighted)
def f39ced_f39_cash_earnings_divergence_ultimatecomposite_252d_base_v150_signal(fcf, ncfo, netinc, revenue, closeadj):
    fcf_gap = _f39_cash_earnings_div_norm(fcf, netinc, revenue)
    ncfo_gap = _f39_ncfo_minus_netinc(ncfo, netinc) / revenue.abs().replace(0, np.nan)
    combined = fcf_gap + ncfo_gap
    growth = revenue.pct_change(252).fillna(0.0)
    result = _mean(combined, 252) * growth * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ced_f39_cash_earnings_divergence_fcfgapz_63d_base_v076_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapz_126d_base_v077_signal,
    f39ced_f39_cash_earnings_divergence_posdivfreq_252d_base_v078_signal,
    f39ced_f39_cash_earnings_divergence_posdivfreq_504d_base_v079_signal,
    f39ced_f39_cash_earnings_divergence_posncfofreq_252d_base_v080_signal,
    f39ced_f39_cash_earnings_divergence_posncfofreq_504d_base_v081_signal,
    f39ced_f39_cash_earnings_divergence_fcfposnegratio_252d_base_v082_signal,
    f39ced_f39_cash_earnings_divergence_fcfposnegratio_63d_base_v083_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapchg_252d_base_v084_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapchg_63d_base_v085_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapdelta_252d_base_v086_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapdelta_63d_base_v087_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapopinc_252d_base_v088_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapopinc_63d_base_v089_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapgp_252d_base_v090_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapgp_63d_base_v091_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaparea_252d_base_v092_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaparea_63d_base_v093_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaparea_504d_base_v094_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapquantilehi_252d_base_v095_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapquantilelo_252d_base_v096_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapquantilehi_504d_base_v097_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapquantilelo_504d_base_v098_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapquantilehi_252d_base_v099_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapquantilelo_252d_base_v100_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapiqr_252d_base_v101_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapiqr_504d_base_v102_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapmedian_252d_base_v103_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapmedian_504d_base_v104_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapskew_252d_base_v105_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapskew_504d_base_v106_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapkurt_252d_base_v107_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapkurt_504d_base_v108_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapcv_252d_base_v109_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapcv_504d_base_v110_signal,
    f39ced_f39_cash_earnings_divergence_qualitydrag_252d_base_v111_signal,
    f39ced_f39_cash_earnings_divergence_qualitydrag_504d_base_v112_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxmc_252d_base_v113_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxmc_63d_base_v114_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxcr_252d_base_v115_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapxcr_63d_base_v116_signal,
    f39ced_f39_cash_earnings_divergence_relgapintensity_252d_base_v117_signal,
    f39ced_f39_cash_earnings_divergence_relgapintensity_63d_base_v118_signal,
    f39ced_f39_cash_earnings_divergence_ncforelintensity_252d_base_v119_signal,
    f39ced_f39_cash_earnings_divergence_ncforelintensity_63d_base_v120_signal,
    f39ced_f39_cash_earnings_divergence_fcfgappersist_252d_base_v121_signal,
    f39ced_f39_cash_earnings_divergence_fcfgappersist_504d_base_v122_signal,
    f39ced_f39_cash_earnings_divergence_ncforatiocum_252d_base_v123_signal,
    f39ced_f39_cash_earnings_divergence_ncforatiocum_504d_base_v124_signal,
    f39ced_f39_cash_earnings_divergence_fcfratiocum_252d_base_v125_signal,
    f39ced_f39_cash_earnings_divergence_fcfratiocum_504d_base_v126_signal,
    f39ced_f39_cash_earnings_divergence_fcfratioema_252d_base_v127_signal,
    f39ced_f39_cash_earnings_divergence_fcfratioema_63d_base_v128_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapebgrow_252d_base_v129_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapebgrow_63d_base_v130_signal,
    f39ced_f39_cash_earnings_divergence_ncfocumxeps_252d_base_v131_signal,
    f39ced_f39_cash_earnings_divergence_ncfocumxeps_63d_base_v132_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapdebtchg_252d_base_v133_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapdebtchg_63d_base_v134_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaplia_252d_base_v135_signal,
    f39ced_f39_cash_earnings_divergence_fcfgaplia_63d_base_v136_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapretearn_252d_base_v137_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapretearn_63d_base_v138_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapzxgrow_252d_base_v139_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapzxrev_63d_base_v140_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapxrevgrow_252d_base_v141_signal,
    f39ced_f39_cash_earnings_divergence_ncfogapxrevgrow_63d_base_v142_signal,
    f39ced_f39_cash_earnings_divergence_combinedgap_252d_base_v143_signal,
    f39ced_f39_cash_earnings_divergence_combinedgap_63d_base_v144_signal,
    f39ced_f39_cash_earnings_divergence_netofcapex_252d_base_v145_signal,
    f39ced_f39_cash_earnings_divergence_netofcapex_63d_base_v146_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapnotional_252d_base_v147_signal,
    f39ced_f39_cash_earnings_divergence_fcfgapnotional_63d_base_v148_signal,
    f39ced_f39_cash_earnings_divergence_dualgapassets_252d_base_v149_signal,
    f39ced_f39_cash_earnings_divergence_ultimatecomposite_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F39_CASH_EARNINGS_DIVERGENCE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1.0e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    netinc = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="netinc")
    fcf = pd.Series(0.9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.013, n))), name="fcf")
    ncfo = pd.Series(1.1e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ncfo")
    assets = pd.Series(5.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    equity = pd.Series(2.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="equity")
    debt = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="debt")
    capex = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.012, n))), name="capex")
    eps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="eps")
    sharesbas = pd.Series(5.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="sharesbas")
    ebitda = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ebitda")
    workingcapital = pd.Series(8.0e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="workingcapital")
    opinc = pd.Series(1.3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="opinc")
    gp = pd.Series(4.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="gp")
    liabilities = pd.Series(3.0e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="liabilities")
    retearn = pd.Series(2.5e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="retearn")
    currentratio = pd.Series(1.5 + 0.3 * np.cumsum(np.random.normal(0, 0.001, n)), name="currentratio")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "assets": assets, "equity": equity, "debt": debt,
        "capex": capex, "eps": eps, "sharesbas": sharesbas, "ebitda": ebitda,
        "workingcapital": workingcapital, "opinc": opinc, "gp": gp,
        "liabilities": liabilities, "retearn": retearn, "currentratio": currentratio,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f39_cash_earnings_div", "_f39_fcf_minus_netinc", "_f39_ncfo_minus_netinc")
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
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        src = inspect.getsource(fn)
        assert any(p in src for p in domain_primitives), name
        n_features += 1
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f39_cash_earnings_divergence_base_076_150_claude: {n_features} features pass")
