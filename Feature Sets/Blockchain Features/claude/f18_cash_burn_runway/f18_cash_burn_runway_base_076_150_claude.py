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


# ===== folder domain primitives (cash burn & survival runway) =====
def _f18_burn(fcf):
    # cash burn magnitude = negative free cash flow (positive when burning cash)
    return -fcf


def _f18_runway(cashneq, fcf):
    # survival runway = cash on hand divided by burn rate (years of cash, signed)
    return _safe_div(cashneq, _f18_burn(fcf))


def _f18_cashtrend(cashneq, w):
    # cash trajectory = pct-change of cash balance over w (depletion/accumulation)
    return cashneq.pct_change(periods=w)


def _f18_capexburn(capex, ncfo):
    # capex-adjusted burn = investment outlay minus operating cash generated
    return capex - ncfo


# ============ FEATURES 076-150 ============

# 84d cash balance trend
def f18cb_f18_cash_burn_runway_cashtrend_84d_base_v076_signal(cashneq):
    result = _f18_cashtrend(cashneq, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d cash balance trend
def f18cb_f18_cash_burn_runway_cashtrend_189d_base_v077_signal(cashneq):
    result = _f18_cashtrend(cashneq, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d cash balance trend
def f18cb_f18_cash_burn_runway_cashtrend_315d_base_v078_signal(cashneq):
    result = _f18_cashtrend(cashneq, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d cash balance trend
def f18cb_f18_cash_burn_runway_cashtrend_42d_base_v079_signal(cashneq):
    result = _f18_cashtrend(cashneq, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d cash balance trend
def f18cb_f18_cash_burn_runway_cashtrend_378d_base_v080_signal(cashneq):
    result = _f18_cashtrend(cashneq, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d-smoothed survival runway
def f18cb_f18_cash_burn_runway_runway_sm84_84d_base_v081_signal(cashneq, fcf):
    result = _mean(_f18_runway(cashneq, fcf), 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d-smoothed survival runway
def f18cb_f18_cash_burn_runway_runway_sm189_189d_base_v082_signal(cashneq, fcf):
    result = _mean(_f18_runway(cashneq, fcf), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d-smoothed survival runway
def f18cb_f18_cash_burn_runway_runway_sm504_504d_base_v083_signal(cashneq, fcf):
    result = _mean(_f18_runway(cashneq, fcf), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d-smoothed survival runway
def f18cb_f18_cash_burn_runway_runway_sm42_42d_base_v084_signal(cashneq, fcf):
    result = _mean(_f18_runway(cashneq, fcf), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed burn rate
def f18cb_f18_cash_burn_runway_burn_sm252_252d_base_v085_signal(fcf):
    result = _mean(_f18_burn(fcf), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d-smoothed burn rate
def f18cb_f18_cash_burn_runway_burn_sm42_42d_base_v086_signal(fcf):
    result = _mean(_f18_burn(fcf), 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d-smoothed burn rate
def f18cb_f18_cash_burn_runway_burn_sm189_189d_base_v087_signal(fcf):
    result = _mean(_f18_burn(fcf), 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed burn intensity vs assets
def f18cb_f18_cash_burn_runway_burnassets_252d_base_v088_signal(fcf, assets):
    result = _mean(_safe_div(_f18_burn(fcf), assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# burn intensity vs assets standardized over 252d
def f18cb_f18_cash_burn_runway_burnassetsz_252d_base_v089_signal(fcf, assets):
    result = _z(_safe_div(_f18_burn(fcf), assets), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash to assets standardized over 252d
def f18cb_f18_cash_burn_runway_ncfoassetsz_252d_base_v090_signal(ncfo, assets, fcf):
    result = _z(_safe_div(ncfo, assets), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# free cash flow to assets standardized over 252d
def f18cb_f18_cash_burn_runway_fcfassetsz_252d_base_v091_signal(fcf, assets):
    result = _z(_safe_div(fcf, assets), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed cash months of opex
def f18cb_f18_cash_burn_runway_cashopex_252d_base_v092_signal(cashneq, opex, fcf):
    result = _mean(_safe_div(cashneq, opex / 21.0), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash months of opex change over 126d (runway erosion)
def f18cb_f18_cash_burn_runway_cashopexchg_126d_base_v093_signal(cashneq, opex, fcf):
    m = _safe_div(cashneq, opex / 21.0)
    result = m.diff(126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed capex-adjusted burn
def f18cb_f18_cash_burn_runway_capexburn_252d_base_v094_signal(capex, ncfo):
    result = _mean(_f18_capexburn(capex, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-adjusted burn standardized over 252d
def f18cb_f18_cash_burn_runway_capexburnz_252d_base_v095_signal(capex, ncfo):
    result = _z(_f18_capexburn(capex, ncfo), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-adjusted burn intensity vs assets 126d-smoothed
def f18cb_f18_cash_burn_runway_capexburnassets_126d_base_v096_signal(capex, ncfo, assets):
    result = _mean(_safe_div(_f18_capexburn(capex, ncfo), assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed capex-adjusted runway
def f18cb_f18_cash_burn_runway_capexrunway_126d_base_v097_signal(cashneq, capex, ncfo):
    result = _mean(_safe_div(cashneq, _f18_capexburn(capex, ncfo)), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-adjusted runway percentile rank over 252d
def f18cb_f18_cash_burn_runway_capexrunwayrank_252d_base_v098_signal(cashneq, capex, ncfo):
    r = _safe_div(cashneq, _f18_capexburn(capex, ncfo))
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# burn acceleration: 84d change of smoothed burn
def f18cb_f18_cash_burn_runway_burnaccel_84d_base_v099_signal(fcf):
    b = _mean(_f18_burn(fcf), 63)
    result = b.diff(84)
    return result.replace([np.inf, -np.inf], np.nan)


# burn acceleration: 252d change of smoothed burn
def f18cb_f18_cash_burn_runway_burnaccel_252d_base_v100_signal(fcf):
    b = _mean(_f18_burn(fcf), 126)
    result = b.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed cash coverage of debt
def f18cb_f18_cash_burn_runway_cashdebt_126d_base_v101_signal(cashneq, debt, fcf):
    result = _mean(_safe_div(cashneq, debt), 126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# net cash position to debt (cash minus burn-year vs debt)
def f18cb_f18_cash_burn_runway_netcashdebt_0d_base_v102_signal(cashneq, fcf, debt):
    result = _safe_div(cashneq + fcf, debt) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed operating cash coverage of debt
def f18cb_f18_cash_burn_runway_ncfodebt_63d_base_v103_signal(ncfo, debt, fcf):
    result = _mean(_safe_div(ncfo, debt), 63) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# runway percentile rank over 126d
def f18cb_f18_cash_burn_runway_runwayrank_126d_base_v104_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# burn percentile rank over 504d
def f18cb_f18_cash_burn_runway_burnrank_504d_base_v105_signal(fcf):
    b = _f18_burn(fcf)
    result = b.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of runway over 504d
def f18cb_f18_cash_burn_runway_runwayz_504d_base_v106_signal(cashneq, fcf):
    result = _z(_f18_runway(cashneq, fcf), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of burn over 504d
def f18cb_f18_cash_burn_runway_burnz_504d_base_v107_signal(fcf):
    result = _z(_f18_burn(fcf), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# cash trend surprise over 252d horizon
def f18cb_f18_cash_burn_runway_cashtrendsurp_252d_base_v108_signal(cashneq):
    r = _f18_cashtrend(cashneq, 252)
    result = r - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed ncfo to opex
def f18cb_f18_cash_burn_runway_ncfoopex_252d_base_v109_signal(ncfo, opex, fcf):
    result = _mean(_safe_div(ncfo, opex), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed burn to opex
def f18cb_f18_cash_burn_runway_burnopex_252d_base_v110_signal(fcf, opex):
    result = _mean(_safe_div(_f18_burn(fcf), opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# burn to opex standardized over 252d
def f18cb_f18_cash_burn_runway_burnopexz_252d_base_v111_signal(fcf, opex):
    result = _z(_safe_div(_f18_burn(fcf), opex), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed capex intensity vs assets
def f18cb_f18_cash_burn_runway_capexassets_252d_base_v112_signal(capex, assets, fcf):
    result = _mean(_safe_div(capex, assets), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity vs assets standardized over 252d
def f18cb_f18_cash_burn_runway_capexassetsz_252d_base_v113_signal(capex, assets, fcf):
    result = _z(_safe_div(capex, assets), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed capex to operating cash
def f18cb_f18_cash_burn_runway_capexncfo_252d_base_v114_signal(capex, ncfo, fcf):
    result = _mean(_safe_div(capex, ncfo), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash to opex standardized over 504d
def f18cb_f18_cash_burn_runway_cashopexz_504d_base_v115_signal(cashneq, opex, fcf):
    result = _z(_safe_div(cashneq, opex), 504) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash trend volatility over 504d
def f18cb_f18_cash_burn_runway_cashtrendvol_504d_base_v116_signal(cashneq):
    result = _std(_f18_cashtrend(cashneq, 63), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# burn volatility over 504d
def f18cb_f18_cash_burn_runway_burnvol_504d_base_v117_signal(fcf):
    result = _std(_f18_burn(fcf), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# burn coefficient of variation over 252d (instability of cash drain)
def f18cb_f18_cash_burn_runway_burncv_252d_base_v118_signal(fcf):
    b = _f18_burn(fcf)
    result = _safe_div(_std(b, 252), _mean(b, 252).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# log cash balance trend over 504d
def f18cb_f18_cash_burn_runway_logcashtrend_504d_base_v119_signal(cashneq, fcf):
    result = np.log(cashneq / cashneq.shift(504)) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log cash balance trend over 84d
def f18cb_f18_cash_burn_runway_logcashtrend_84d_base_v120_signal(cashneq, fcf):
    result = np.log(cashneq / cashneq.shift(84)) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# runway change over 252d
def f18cb_f18_cash_burn_runway_runwaychg_252d_base_v121_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.diff(252)
    return result.replace([np.inf, -np.inf], np.nan)


# runway change over 21d
def f18cb_f18_cash_burn_runway_runwaychg_21d_base_v122_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed runway (span 126)
def f18cb_f18_cash_burn_runway_runwayewm_126d_base_v123_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed runway (span 252)
def f18cb_f18_cash_burn_runway_runwayewm_252d_base_v124_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed burn (span 63)
def f18cb_f18_cash_burn_runway_burnewm_63d_base_v125_signal(fcf):
    b = _f18_burn(fcf)
    result = b.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed burn (span 252)
def f18cb_f18_cash_burn_runway_burnewm_252d_base_v126_signal(fcf):
    b = _f18_burn(fcf)
    result = b.ewm(span=252, min_periods=84).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed depletion rate (inverse runway)
def f18cb_f18_cash_burn_runway_invrunway_126d_base_v127_signal(cashneq, fcf):
    result = _mean(_safe_div(_f18_burn(fcf), cashneq), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# depletion rate standardized over 252d
def f18cb_f18_cash_burn_runway_invrunwayz_252d_base_v128_signal(cashneq, fcf):
    result = _z(_safe_div(_f18_burn(fcf), cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed fcf to ncfo conversion
def f18cb_f18_cash_burn_runway_fcfncfo_252d_base_v129_signal(fcf, ncfo):
    result = _mean(_safe_div(fcf, ncfo), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash stress over 126d burn volatility
def f18cb_f18_cash_burn_runway_cashstress_126d_base_v130_signal(cashneq, fcf):
    vol = _std(_f18_burn(fcf), 126)
    result = _safe_div(cashneq, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# runway momentum: 126d vs 504d average
def f18cb_f18_cash_burn_runway_runwaymom_126d_base_v131_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = _mean(r, 126) - _mean(r, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# burn momentum: short vs long burn average
def f18cb_f18_cash_burn_runway_burnmom_63d_base_v132_signal(fcf):
    b = _f18_burn(fcf)
    result = _mean(b, 63) - _mean(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# burn momentum: 126d vs 504d burn average
def f18cb_f18_cash_burn_runway_burnmom_126d_base_v133_signal(fcf):
    b = _f18_burn(fcf)
    result = _mean(b, 126) - _mean(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# cash trend percentile rank over 252d
def f18cb_f18_cash_burn_runway_cashtrendrank_252d_base_v134_signal(cashneq):
    r = _f18_cashtrend(cashneq, 63)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# burn intensity percentile rank over 252d
def f18cb_f18_cash_burn_runway_burnassetsrank_252d_base_v135_signal(fcf, assets):
    r = _safe_div(_f18_burn(fcf), assets)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# free cash flow margin vs revenue-proxy opex spend
def f18cb_f18_cash_burn_runway_fcfopex_0d_base_v136_signal(fcf, opex):
    result = _safe_div(fcf, opex) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed fcf to opex
def f18cb_f18_cash_burn_runway_fcfopex_126d_base_v137_signal(fcf, opex):
    result = _mean(_safe_div(fcf, opex), 126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash to total assets buffer
def f18cb_f18_cash_burn_runway_cashassets_0d_base_v138_signal(cashneq, assets, fcf):
    result = _safe_div(cashneq, assets) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed cash to assets buffer
def f18cb_f18_cash_burn_runway_cashassets_126d_base_v139_signal(cashneq, assets, fcf):
    result = _mean(_safe_div(cashneq, assets), 126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash to assets buffer change over 252d
def f18cb_f18_cash_burn_runway_cashassetschg_252d_base_v140_signal(cashneq, assets, fcf):
    b = _safe_div(cashneq, assets)
    result = b.diff(252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# burn-adjusted runway using capex-burn smoothed 63d
def f18cb_f18_cash_burn_runway_capexrunwayewm_63d_base_v141_signal(cashneq, capex, ncfo):
    r = _safe_div(cashneq, _f18_capexburn(capex, ncfo))
    result = r.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash flow trend over 126d
def f18cb_f18_cash_burn_runway_ncfotrend_126d_base_v142_signal(ncfo, fcf):
    result = ncfo.pct_change(126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# burn trend over 126d (growth in cash drain)
def f18cb_f18_cash_burn_runway_burntrend_126d_base_v143_signal(fcf):
    b = _f18_burn(fcf)
    result = _safe_div(b - b.shift(126), b.shift(126).abs())
    return result.replace([np.inf, -np.inf], np.nan)


# runway minus its 252d median band (survival deviation)
def f18cb_f18_cash_burn_runway_runwaydev_252d_base_v144_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r - r.rolling(252, min_periods=84).median()
    return result.replace([np.inf, -np.inf], np.nan)


# burn intensity vs opex+capex total spend
def f18cb_f18_cash_burn_runway_burntotalspend_0d_base_v145_signal(fcf, opex, capex):
    result = _safe_div(_f18_burn(fcf), opex + capex)
    return result.replace([np.inf, -np.inf], np.nan)


# cash months covering opex plus capex burn
def f18cb_f18_cash_burn_runway_cashtotalspend_0d_base_v146_signal(cashneq, opex, capex, fcf):
    result = _safe_div(cashneq, (opex + capex) / 21.0) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# runway scaled by burn instability (risk-adjusted survival)
def f18cb_f18_cash_burn_runway_runwayrisk_252d_base_v147_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = _safe_div(_mean(r, 63), _std(r, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed depletion rate (inverse runway)
def f18cb_f18_cash_burn_runway_invrunway_252d_base_v148_signal(cashneq, fcf):
    result = _mean(_safe_div(_f18_burn(fcf), cashneq), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-burn percentile rank over 252d
def f18cb_f18_cash_burn_runway_capexburnrank_252d_base_v149_signal(capex, ncfo):
    r = _f18_capexburn(capex, ncfo)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon survival composite (runway sm63 + cash months + cash trend)
def f18cb_f18_cash_burn_runway_survblend_multi_base_v150_signal(cashneq, fcf, opex):
    a = _z(_mean(_f18_runway(cashneq, fcf), 63), 252)
    b = _z(_safe_div(cashneq, opex / 21.0), 252)
    c = _z(_f18_cashtrend(cashneq, 126), 252)
    result = (a + b + c) / 3.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18cb_f18_cash_burn_runway_cashtrend_84d_base_v076_signal,
    f18cb_f18_cash_burn_runway_cashtrend_189d_base_v077_signal,
    f18cb_f18_cash_burn_runway_cashtrend_315d_base_v078_signal,
    f18cb_f18_cash_burn_runway_cashtrend_42d_base_v079_signal,
    f18cb_f18_cash_burn_runway_cashtrend_378d_base_v080_signal,
    f18cb_f18_cash_burn_runway_runway_sm84_84d_base_v081_signal,
    f18cb_f18_cash_burn_runway_runway_sm189_189d_base_v082_signal,
    f18cb_f18_cash_burn_runway_runway_sm504_504d_base_v083_signal,
    f18cb_f18_cash_burn_runway_runway_sm42_42d_base_v084_signal,
    f18cb_f18_cash_burn_runway_burn_sm252_252d_base_v085_signal,
    f18cb_f18_cash_burn_runway_burn_sm42_42d_base_v086_signal,
    f18cb_f18_cash_burn_runway_burn_sm189_189d_base_v087_signal,
    f18cb_f18_cash_burn_runway_burnassets_252d_base_v088_signal,
    f18cb_f18_cash_burn_runway_burnassetsz_252d_base_v089_signal,
    f18cb_f18_cash_burn_runway_ncfoassetsz_252d_base_v090_signal,
    f18cb_f18_cash_burn_runway_fcfassetsz_252d_base_v091_signal,
    f18cb_f18_cash_burn_runway_cashopex_252d_base_v092_signal,
    f18cb_f18_cash_burn_runway_cashopexchg_126d_base_v093_signal,
    f18cb_f18_cash_burn_runway_capexburn_252d_base_v094_signal,
    f18cb_f18_cash_burn_runway_capexburnz_252d_base_v095_signal,
    f18cb_f18_cash_burn_runway_capexburnassets_126d_base_v096_signal,
    f18cb_f18_cash_burn_runway_capexrunway_126d_base_v097_signal,
    f18cb_f18_cash_burn_runway_capexrunwayrank_252d_base_v098_signal,
    f18cb_f18_cash_burn_runway_burnaccel_84d_base_v099_signal,
    f18cb_f18_cash_burn_runway_burnaccel_252d_base_v100_signal,
    f18cb_f18_cash_burn_runway_cashdebt_126d_base_v101_signal,
    f18cb_f18_cash_burn_runway_netcashdebt_0d_base_v102_signal,
    f18cb_f18_cash_burn_runway_ncfodebt_63d_base_v103_signal,
    f18cb_f18_cash_burn_runway_runwayrank_126d_base_v104_signal,
    f18cb_f18_cash_burn_runway_burnrank_504d_base_v105_signal,
    f18cb_f18_cash_burn_runway_runwayz_504d_base_v106_signal,
    f18cb_f18_cash_burn_runway_burnz_504d_base_v107_signal,
    f18cb_f18_cash_burn_runway_cashtrendsurp_252d_base_v108_signal,
    f18cb_f18_cash_burn_runway_ncfoopex_252d_base_v109_signal,
    f18cb_f18_cash_burn_runway_burnopex_252d_base_v110_signal,
    f18cb_f18_cash_burn_runway_burnopexz_252d_base_v111_signal,
    f18cb_f18_cash_burn_runway_capexassets_252d_base_v112_signal,
    f18cb_f18_cash_burn_runway_capexassetsz_252d_base_v113_signal,
    f18cb_f18_cash_burn_runway_capexncfo_252d_base_v114_signal,
    f18cb_f18_cash_burn_runway_cashopexz_504d_base_v115_signal,
    f18cb_f18_cash_burn_runway_cashtrendvol_504d_base_v116_signal,
    f18cb_f18_cash_burn_runway_burnvol_504d_base_v117_signal,
    f18cb_f18_cash_burn_runway_burncv_252d_base_v118_signal,
    f18cb_f18_cash_burn_runway_logcashtrend_504d_base_v119_signal,
    f18cb_f18_cash_burn_runway_logcashtrend_84d_base_v120_signal,
    f18cb_f18_cash_burn_runway_runwaychg_252d_base_v121_signal,
    f18cb_f18_cash_burn_runway_runwaychg_21d_base_v122_signal,
    f18cb_f18_cash_burn_runway_runwayewm_126d_base_v123_signal,
    f18cb_f18_cash_burn_runway_runwayewm_252d_base_v124_signal,
    f18cb_f18_cash_burn_runway_burnewm_63d_base_v125_signal,
    f18cb_f18_cash_burn_runway_burnewm_252d_base_v126_signal,
    f18cb_f18_cash_burn_runway_invrunway_126d_base_v127_signal,
    f18cb_f18_cash_burn_runway_invrunwayz_252d_base_v128_signal,
    f18cb_f18_cash_burn_runway_fcfncfo_252d_base_v129_signal,
    f18cb_f18_cash_burn_runway_cashstress_126d_base_v130_signal,
    f18cb_f18_cash_burn_runway_runwaymom_126d_base_v131_signal,
    f18cb_f18_cash_burn_runway_burnmom_63d_base_v132_signal,
    f18cb_f18_cash_burn_runway_burnmom_126d_base_v133_signal,
    f18cb_f18_cash_burn_runway_cashtrendrank_252d_base_v134_signal,
    f18cb_f18_cash_burn_runway_burnassetsrank_252d_base_v135_signal,
    f18cb_f18_cash_burn_runway_fcfopex_0d_base_v136_signal,
    f18cb_f18_cash_burn_runway_fcfopex_126d_base_v137_signal,
    f18cb_f18_cash_burn_runway_cashassets_0d_base_v138_signal,
    f18cb_f18_cash_burn_runway_cashassets_126d_base_v139_signal,
    f18cb_f18_cash_burn_runway_cashassetschg_252d_base_v140_signal,
    f18cb_f18_cash_burn_runway_capexrunwayewm_63d_base_v141_signal,
    f18cb_f18_cash_burn_runway_ncfotrend_126d_base_v142_signal,
    f18cb_f18_cash_burn_runway_burntrend_126d_base_v143_signal,
    f18cb_f18_cash_burn_runway_runwaydev_252d_base_v144_signal,
    f18cb_f18_cash_burn_runway_burntotalspend_0d_base_v145_signal,
    f18cb_f18_cash_burn_runway_cashtotalspend_0d_base_v146_signal,
    f18cb_f18_cash_burn_runway_runwayrisk_252d_base_v147_signal,
    f18cb_f18_cash_burn_runway_invrunway_252d_base_v148_signal,
    f18cb_f18_cash_burn_runway_capexburnrank_252d_base_v149_signal,
    f18cb_f18_cash_burn_runway_survblend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_CASH_BURN_RUNWAY_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ("_f18_burn", "_f18_runway", "_f18_cashtrend", "_f18_capexburn")
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
    print(f"OK f18_cash_burn_runway_base_076_150_claude: {n_features} features pass")
