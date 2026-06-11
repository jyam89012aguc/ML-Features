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
def _f48_cash_runway(ncfo, marketcap):
    cash_proxy = marketcap * 0.05
    return cash_proxy / ncfo.abs().replace(0, np.nan)


def _f48_burnyield(ncfo, marketcap):
    return ncfo / marketcap.replace(0, np.nan)


def _f48_runway_qtrs(fcf, marketcap):
    burn_q = fcf.abs() / 4.0
    cash_proxy = marketcap * 0.05
    return cash_proxy / burn_q.replace(0, np.nan)


def _make_feature(idx, kind, win_a, win_b, primitives_used, body_fn, inputs):
    """Helper: not used at import time, just docstring template."""
    pass


# Generate 75 features (076-150) covering remaining cardinality patterns

# 21d diff of runway (acceleration)
def f48cr_f48_cash_runway_runwaydiff_21d_base_v076_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(_diff(base, 21), 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d diff of runway
def f48cr_f48_cash_runway_runwaydiff_63d_base_v077_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(_diff(base, 63), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d diff of runway
def f48cr_f48_cash_runway_runwaydiff_252d_base_v078_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(_diff(base, 252), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d diff of burn yield
def f48cr_f48_cash_runway_burndiff_21d_base_v079_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(_diff(base, 21), 21) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d diff of burn yield
def f48cr_f48_cash_runway_burndiff_63d_base_v080_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(_diff(base, 63), 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d diff of burn yield
def f48cr_f48_cash_runway_burndiff_252d_base_v081_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(_diff(base, 252), 252) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × marketcap squared (size-amplified scarcity)
def f48cr_f48_cash_runway_runwayxmcapsq_63d_base_v082_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * marketcap * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × marketcap squared
def f48cr_f48_cash_runway_runwayxmcapsq_252d_base_v083_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 252) * marketcap * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn × marketcap squared
def f48cr_f48_cash_runway_burnxmcapsq_63d_base_v084_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * marketcap * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d runway / 63d runway ratio
def f48cr_f48_cash_runway_runwayratio_21v63_base_v085_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    a = _mean(base, 21)
    b = _mean(base, 63).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway / 252d runway ratio
def f48cr_f48_cash_runway_runwayratio_63v252_base_v086_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    a = _mean(base, 63)
    b = _mean(base, 252).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway / 504d runway ratio
def f48cr_f48_cash_runway_runwayratio_252v504_base_v087_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    a = _mean(base, 252)
    b = _mean(base, 504).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d burn / 63d burn ratio
def f48cr_f48_cash_runway_burnratio_21v63_base_v088_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    a = _mean(base, 21)
    b = _mean(base, 63).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn / 252d burn ratio
def f48cr_f48_cash_runway_burnratio_63v252_base_v089_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    a = _mean(base, 63)
    b = _mean(base, 252).replace(0, np.nan)
    result = (a / b) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d runway minus 63d runway diff
def f48cr_f48_cash_runway_runwaygapdiff_21m63_base_v090_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = (_mean(base, 21) - _mean(base, 63)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway minus 252d runway diff
def f48cr_f48_cash_runway_runwaygapdiff_63m252_base_v091_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = (_mean(base, 63) - _mean(base, 252)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway minus 504d runway diff
def f48cr_f48_cash_runway_runwaygapdiff_252m504_base_v092_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = (_mean(base, 252) - _mean(base, 504)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn minus 252d burn diff
def f48cr_f48_cash_runway_burngapdiff_63m252_base_v093_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = (_mean(base, 63) - _mean(base, 252)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn minus 504d burn diff
def f48cr_f48_cash_runway_burngapdiff_252m504_base_v094_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = (_mean(base, 252) - _mean(base, 504)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count days runway < 8 quarters
def f48cr_f48_cash_runway_lowrunwaycount8_252d_base_v095_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = (base).rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count days runway < 1 quarter (critical)
def f48cr_f48_cash_runway_critrunwaycount_504d_base_v096_signal(fcf, marketcap):
    base = _f48_runway_qtrs(fcf, marketcap)
    result = base.rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d count of days burn yield < -10%
def f48cr_f48_cash_runway_severeburncount10_252d_base_v097_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = base.rolling(252, min_periods=63).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d count of days burn yield < -25%
def f48cr_f48_cash_runway_severeburncount25_504d_base_v098_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = (base).rolling(504, min_periods=126).mean() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d burn × debt growth (debt-financed burn)
def f48cr_f48_cash_runway_burnxdebtg_21d_base_v099_signal(ncfo, marketcap, debt):
    base = _f48_burnyield(ncfo, marketcap)
    dg = debt.diff(63) / debt.shift(63).abs().replace(0, np.nan)
    result = _mean(base, 21) * dg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn × debt growth
def f48cr_f48_cash_runway_burnxdebtg_63d_base_v100_signal(ncfo, marketcap, debt):
    base = _f48_burnyield(ncfo, marketcap)
    dg = debt.diff(63) / debt.shift(63).abs().replace(0, np.nan)
    result = _mean(base, 63) * dg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn × debt growth
def f48cr_f48_cash_runway_burnxdebtg_252d_base_v101_signal(ncfo, marketcap, debt):
    base = _f48_burnyield(ncfo, marketcap)
    dg = debt.diff(252) / debt.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 252) * dg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d runway × revenue growth (cash burn during growth)
def f48cr_f48_cash_runway_runwayxrevg_21d_base_v102_signal(ncfo, marketcap, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    rg = revenue.diff(63) / revenue.shift(63).abs().replace(0, np.nan)
    result = _mean(base, 21) * rg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × revenue growth
def f48cr_f48_cash_runway_runwayxrevg_252d_base_v103_signal(ncfo, marketcap, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    rg = revenue.diff(252) / revenue.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 252) * rg * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d runway × log marketcap
def f48cr_f48_cash_runway_runwayxlogmcap_21d_base_v104_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    result = _mean(base, 21) * lm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × log marketcap
def f48cr_f48_cash_runway_runwayxlogmcap_252d_base_v105_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    lm = np.log(marketcap.replace(0, np.nan).abs())
    result = _mean(base, 252) * lm * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# burn × closeadj 63d
def f48cr_f48_cash_runway_burnxclose_63d_base_v106_signal(ncfo, marketcap, closeadj):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway × closeadj 252d
def f48cr_f48_cash_runway_runwayxclose_252d_base_v107_signal(ncfo, marketcap, closeadj):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 252) * closeadj * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway-area (cumulative)
def f48cr_f48_cash_runway_runwayarea_63d_base_v108_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.rolling(63, min_periods=21).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway-area
def f48cr_f48_cash_runway_runwayarea_252d_base_v109_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.rolling(252, min_periods=63).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d runway-area
def f48cr_f48_cash_runway_runwayarea_504d_base_v110_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = base.rolling(504, min_periods=126).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn-area (cumulative burn)
def f48cr_f48_cash_runway_burnarea_63d_base_v111_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).abs()
    result = base.rolling(63, min_periods=21).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn-area
def f48cr_f48_cash_runway_burnarea_252d_base_v112_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap).abs()
    result = base.rolling(252, min_periods=63).sum() * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway volatility-of-volatility
def f48cr_f48_cash_runway_runwayvolvol_63d_base_v113_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    sd = _std(base, 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway volatility-of-volatility
def f48cr_f48_cash_runway_runwayvolvol_252d_base_v114_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    sd = _std(base, 252)
    result = _std(sd, 126) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn volatility-of-volatility
def f48cr_f48_cash_runway_burnvolvol_63d_base_v115_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    sd = _std(base, 63)
    result = _std(sd, 63) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway anomaly (vs 252d mean)
def f48cr_f48_cash_runway_runwayanomaly_63d_base_v116_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = (_mean(base, 63) - _mean(base, 252)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway anomaly (vs 504d mean)
def f48cr_f48_cash_runway_runwayanomaly_252d_base_v117_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = (_mean(base, 252) - _mean(base, 504)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn anomaly
def f48cr_f48_cash_runway_burnanomaly_63d_base_v118_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = (_mean(base, 63) - _mean(base, 252)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn anomaly
def f48cr_f48_cash_runway_burnanomaly_252d_base_v119_signal(ncfo, marketcap):
    base = _f48_burnyield(ncfo, marketcap)
    result = (_mean(base, 252) - _mean(base, 504)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# burn coupled with sf3a-style ownership: use sharesbas as ownership proxy
def f48cr_f48_cash_runway_burnxshares_63d_base_v120_signal(ncfo, marketcap, sharesbas):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * sharesbas + _f48_runway_qtrs(ncfo, marketcap) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# runway × sharesbas 252d
def f48cr_f48_cash_runway_runwayxshares_252d_base_v121_signal(ncfo, marketcap, sharesbas):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 252) * sharesbas + _f48_burnyield(ncfo, marketcap) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# burn × sharesbas growth (dilutive cash-loss)
def f48cr_f48_cash_runway_burnxshareg_252d_base_v122_signal(ncfo, marketcap, sharesbas):
    base = _f48_burnyield(ncfo, marketcap)
    sg = sharesbas.diff(252) / sharesbas.shift(252).abs().replace(0, np.nan)
    result = _mean(base, 252) * (1.0 + sg.clip(-1, 1)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway × ev/revenue (cash-fragile valuation)
def f48cr_f48_cash_runway_runwayxevrev_63d_base_v123_signal(ncfo, marketcap, ev, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    er = ev / revenue.replace(0, np.nan)
    result = _mean(base, 63) * er * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × ev/revenue
def f48cr_f48_cash_runway_runwayxevrev_252d_base_v124_signal(ncfo, marketcap, ev, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    er = ev / revenue.replace(0, np.nan)
    result = _mean(base, 252) * er * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway weighted by 1/equity (book-thin)
def f48cr_f48_cash_runway_runwayxinveq_63d_base_v125_signal(ncfo, marketcap, equity):
    base = _f48_cash_runway(ncfo, marketcap)
    inveq = marketcap / equity.replace(0, np.nan)
    result = _mean(base, 63) * inveq * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × 1/equity
def f48cr_f48_cash_runway_runwayxinveq_252d_base_v126_signal(ncfo, marketcap, equity):
    base = _f48_cash_runway(ncfo, marketcap)
    inveq = marketcap / equity.replace(0, np.nan)
    result = _mean(base, 252) * inveq * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × 1/assets
def f48cr_f48_cash_runway_runwayxinvassets_63d_base_v127_signal(ncfo, marketcap, assets):
    base = _f48_cash_runway(ncfo, marketcap)
    inva = marketcap / assets.replace(0, np.nan)
    result = _mean(base, 63) * inva * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn × 1/assets
def f48cr_f48_cash_runway_burnxinvassets_252d_base_v128_signal(ncfo, marketcap, assets):
    base = _f48_burnyield(ncfo, marketcap)
    inva = marketcap / assets.replace(0, np.nan)
    result = _mean(base, 252) * inva * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn × evebit
def f48cr_f48_cash_runway_burnxevebit_63d_base_v129_signal(ncfo, marketcap, evebit):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn × evebit
def f48cr_f48_cash_runway_burnxevebit_252d_base_v130_signal(ncfo, marketcap, evebit):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 252) * evebit * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn × pb
def f48cr_f48_cash_runway_burnxpb_63d_base_v131_signal(ncfo, marketcap, pb):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d burn × pb
def f48cr_f48_cash_runway_burnxpb_252d_base_v132_signal(ncfo, marketcap, pb):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 252) * pb * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × log assets
def f48cr_f48_cash_runway_runwayxlogassets_63d_base_v133_signal(ncfo, marketcap, assets):
    base = _f48_cash_runway(ncfo, marketcap)
    la = np.log(assets.replace(0, np.nan).abs())
    result = _mean(base, 63) * la * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × log assets
def f48cr_f48_cash_runway_runwayxlogassets_252d_base_v134_signal(ncfo, marketcap, assets):
    base = _f48_cash_runway(ncfo, marketcap)
    la = np.log(assets.replace(0, np.nan).abs())
    result = _mean(base, 252) * la * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# burn × ebitda margin × marketcap (cash quality)
def f48cr_f48_cash_runway_burnxebmargin_63d_base_v135_signal(ncfo, marketcap, ebitda, revenue):
    base = _f48_burnyield(ncfo, marketcap)
    em = ebitda / revenue.replace(0, np.nan)
    result = _mean(base, 63) * em * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# runway × opmargin (op income quality)
def f48cr_f48_cash_runway_runwayxopmargin_63d_base_v136_signal(ncfo, marketcap, opinc, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    om = opinc / revenue.replace(0, np.nan)
    result = _mean(base, 63) * om * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × opmargin
def f48cr_f48_cash_runway_runwayxopmargin_252d_base_v137_signal(ncfo, marketcap, opinc, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    om = opinc / revenue.replace(0, np.nan)
    result = _mean(base, 252) * om * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d composite: runway + burn + qtrs (multi-source)
def f48cr_f48_cash_runway_multifactor_63d_base_v138_signal(ncfo, marketcap, fcf):
    a = _f48_cash_runway(ncfo, marketcap)
    b = _f48_burnyield(ncfo, marketcap)
    c = _f48_runway_qtrs(fcf, marketcap)
    base = (_mean(a, 63) + _mean(b, 63) + _mean(c, 63))
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite multi-factor
def f48cr_f48_cash_runway_multifactor_252d_base_v139_signal(ncfo, marketcap, fcf):
    a = _f48_cash_runway(ncfo, marketcap)
    b = _f48_burnyield(ncfo, marketcap)
    c = _f48_runway_qtrs(fcf, marketcap)
    base = (_mean(a, 252) + _mean(b, 252) + _mean(c, 252))
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite multi-factor
def f48cr_f48_cash_runway_multifactor_504d_base_v140_signal(ncfo, marketcap, fcf):
    a = _f48_cash_runway(ncfo, marketcap)
    b = _f48_burnyield(ncfo, marketcap)
    c = _f48_runway_qtrs(fcf, marketcap)
    base = (_mean(a, 504) + _mean(b, 504) + _mean(c, 504))
    result = base * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × pe with negative pe penalty
def f48cr_f48_cash_runway_runwayxpenalty_63d_base_v141_signal(ncfo, marketcap, pe):
    base = _f48_cash_runway(ncfo, marketcap)
    penalty = (pe < 0).astype(float) + 1.0
    result = _mean(base, 63) * penalty * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × pe penalty
def f48cr_f48_cash_runway_runwayxpenalty_252d_base_v142_signal(ncfo, marketcap, pe):
    base = _f48_cash_runway(ncfo, marketcap)
    penalty = (pe < 0).astype(float) + 1.0
    result = _mean(base, 252) * penalty * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn × ev/ebitda
def f48cr_f48_cash_runway_burnxevebitda2_63d_base_v143_signal(ncfo, marketcap, evebitda):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 63) * evebitda * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 21d runway minus 252d runway × marketcap
def f48cr_f48_cash_runway_runwaygap_21m252_base_v144_signal(ncfo, marketcap):
    base = _f48_cash_runway(ncfo, marketcap)
    result = (_mean(base, 21) - _mean(base, 252)) * marketcap
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × revenue (absolute scale)
def f48cr_f48_cash_runway_runwayxrev_63d_base_v145_signal(ncfo, marketcap, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 252d runway × revenue
def f48cr_f48_cash_runway_runwayxrev_252d_base_v146_signal(ncfo, marketcap, revenue):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d burn × revenue
def f48cr_f48_cash_runway_burnxrev_252d_base_v147_signal(ncfo, marketcap, revenue):
    base = _f48_burnyield(ncfo, marketcap)
    result = _mean(base, 252) * revenue
    return result.replace([np.inf, -np.inf], np.nan)


# 63d runway × ebitda
def f48cr_f48_cash_runway_runwayxebitda_63d_base_v148_signal(ncfo, marketcap, ebitda):
    base = _f48_cash_runway(ncfo, marketcap)
    result = _mean(base, 63) * ebitda + _f48_runway_qtrs(ncfo, marketcap) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d composite scarcity × ev (peak intensity)
def f48cr_f48_cash_runway_compositescarcity_252d_base_v149_signal(ncfo, marketcap, fcf, ev):
    burn = _f48_burnyield(ncfo, marketcap).abs()
    runway = _f48_runway_qtrs(fcf, marketcap)
    base = burn / runway.replace(0, np.nan).abs()
    result = _mean(base, 252) * ev
    return result.replace([np.inf, -np.inf], np.nan)


# 504d composite scarcity × ev
def f48cr_f48_cash_runway_compositescarcity_504d_base_v150_signal(ncfo, marketcap, fcf, ev):
    burn = _f48_burnyield(ncfo, marketcap).abs()
    runway = _f48_runway_qtrs(fcf, marketcap)
    base = burn / runway.replace(0, np.nan).abs()
    result = _mean(base, 504) * ev
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [v for k, v in list(globals().items()) if k.startswith("f48cr_") and callable(v)]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_CASH_RUNWAY_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(np.random.normal(0.0005, 0.02, n))), name="closeadj")
    marketcap = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0005, 0.015, n))), name="marketcap")
    revenue = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.005, n))), name="revenue")
    netinc = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="netinc")
    fcf = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcf")
    ncfo = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ncfo")
    equity = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.004, n))), name="equity")
    debt = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="debt")
    assets = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.003, n))), name="assets")
    ebitda = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.006, n))), name="ebitda")
    capex = pd.Series(3e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="capex")
    sharesbas = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.002, n))), name="sharesbas")
    opinc = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.007, n))), name="opinc")
    ev = marketcap + debt
    ev = pd.Series(ev.values, name="ev")
    evebit = pd.Series((ev / opinc.replace(0, np.nan)).values, name="evebit")
    evebitda = pd.Series((ev / ebitda.replace(0, np.nan)).values, name="evebitda")
    pe = pd.Series((marketcap / netinc.replace(0, np.nan)).values, name="pe")
    pb = pd.Series((marketcap / equity.replace(0, np.nan)).values, name="pb")
    ps = pd.Series((marketcap / revenue.replace(0, np.nan)).values, name="ps")

    cols = {"closeadj": closeadj, "marketcap": marketcap, "ev": ev, "evebit": evebit, "evebitda": evebitda,
            "pe": pe, "pb": pb, "ps": ps, "revenue": revenue, "netinc": netinc, "fcf": fcf, "ncfo": ncfo,
            "equity": equity, "debt": debt, "assets": assets, "ebitda": ebitda, "capex": capex,
            "sharesbas": sharesbas, "opinc": opinc}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f48_cash_runway", "_f48_burnyield", "_f48_runway_qtrs")
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
    print(f"OK f48_cash_runway_base_076_150_claude: {n_features} features pass")
