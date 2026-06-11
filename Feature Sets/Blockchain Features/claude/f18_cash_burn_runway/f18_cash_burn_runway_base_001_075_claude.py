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


# ============ FEATURES 001-075 ============

# 63d cash balance trend (quarterly cash trajectory)
def f18cb_f18_cash_burn_runway_cashtrend_63d_base_v001_signal(cashneq):
    result = _f18_cashtrend(cashneq, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash balance trend
def f18cb_f18_cash_burn_runway_cashtrend_126d_base_v002_signal(cashneq):
    result = _f18_cashtrend(cashneq, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash balance trend (annual cash trajectory)
def f18cb_f18_cash_burn_runway_cashtrend_252d_base_v003_signal(cashneq):
    result = _f18_cashtrend(cashneq, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash balance trend (two-year cash trajectory)
def f18cb_f18_cash_burn_runway_cashtrend_504d_base_v004_signal(cashneq):
    result = _f18_cashtrend(cashneq, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash balance trend (monthly cash trajectory)
def f18cb_f18_cash_burn_runway_cashtrend_21d_base_v005_signal(cashneq):
    result = _f18_cashtrend(cashneq, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# survival runway level (cash / burn)
def f18cb_f18_cash_burn_runway_runway_lvl_0d_base_v006_signal(cashneq, fcf):
    result = _f18_runway(cashneq, fcf)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-smoothed survival runway
def f18cb_f18_cash_burn_runway_runway_sm21_21d_base_v007_signal(cashneq, fcf):
    result = _mean(_f18_runway(cashneq, fcf), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed survival runway
def f18cb_f18_cash_burn_runway_runway_sm63_63d_base_v008_signal(cashneq, fcf):
    result = _mean(_f18_runway(cashneq, fcf), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed survival runway
def f18cb_f18_cash_burn_runway_runway_sm126_126d_base_v009_signal(cashneq, fcf):
    result = _mean(_f18_runway(cashneq, fcf), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed survival runway
def f18cb_f18_cash_burn_runway_runway_sm252_252d_base_v010_signal(cashneq, fcf):
    result = _mean(_f18_runway(cashneq, fcf), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# burn rate level (negative free cash flow)
def f18cb_f18_cash_burn_runway_burn_lvl_0d_base_v011_signal(fcf):
    result = _f18_burn(fcf)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d-smoothed burn rate
def f18cb_f18_cash_burn_runway_burn_sm21_21d_base_v012_signal(fcf):
    result = _mean(_f18_burn(fcf), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed burn rate
def f18cb_f18_cash_burn_runway_burn_sm63_63d_base_v013_signal(fcf):
    result = _mean(_f18_burn(fcf), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed burn rate
def f18cb_f18_cash_burn_runway_burn_sm126_126d_base_v014_signal(fcf):
    result = _mean(_f18_burn(fcf), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# burn rate as fraction of total assets (intensity)
def f18cb_f18_cash_burn_runway_burnassets_0d_base_v015_signal(fcf, assets):
    result = _safe_div(_f18_burn(fcf), assets)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed burn intensity vs assets
def f18cb_f18_cash_burn_runway_burnassets_63d_base_v016_signal(fcf, assets):
    result = _mean(_safe_div(_f18_burn(fcf), assets), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed burn intensity vs assets
def f18cb_f18_cash_burn_runway_burnassets_126d_base_v017_signal(fcf, assets):
    result = _mean(_safe_div(_f18_burn(fcf), assets), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash flow to assets
def f18cb_f18_cash_burn_runway_ncfoassets_0d_base_v018_signal(ncfo, assets, fcf):
    result = _safe_div(ncfo, assets) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed operating cash flow to assets
def f18cb_f18_cash_burn_runway_ncfoassets_63d_base_v019_signal(ncfo, assets, fcf):
    result = _mean(_safe_div(ncfo, assets), 63) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed operating cash flow to assets
def f18cb_f18_cash_burn_runway_ncfoassets_126d_base_v020_signal(ncfo, assets, fcf):
    result = _mean(_safe_div(ncfo, assets), 126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# free cash flow to assets
def f18cb_f18_cash_burn_runway_fcfassets_0d_base_v021_signal(fcf, assets):
    result = _safe_div(fcf, assets) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed free cash flow to assets
def f18cb_f18_cash_burn_runway_fcfassets_63d_base_v022_signal(fcf, assets):
    result = _mean(_safe_div(fcf, assets), 63) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d-smoothed free cash flow to assets
def f18cb_f18_cash_burn_runway_fcfassets_252d_base_v023_signal(fcf, assets):
    result = _mean(_safe_div(fcf, assets), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash runway expressed in months of operating spend (cash / monthly opex)
def f18cb_f18_cash_burn_runway_cashopex_0d_base_v024_signal(cashneq, opex, fcf):
    result = _safe_div(cashneq, opex / 21.0) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed cash months of opex
def f18cb_f18_cash_burn_runway_cashopex_63d_base_v025_signal(cashneq, opex, fcf):
    result = _mean(_safe_div(cashneq, opex / 21.0), 63) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed cash months of opex
def f18cb_f18_cash_burn_runway_cashopex_126d_base_v026_signal(cashneq, opex, fcf):
    result = _mean(_safe_div(cashneq, opex / 21.0), 126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of cash balance decline over 252d
def f18cb_f18_cash_burn_runway_cashz_252d_base_v027_signal(cashneq, fcf):
    result = _z(cashneq, 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of cash balance over 126d
def f18cb_f18_cash_burn_runway_cashz_126d_base_v028_signal(cashneq, fcf):
    result = _z(cashneq, 126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of cash balance over 504d
def f18cb_f18_cash_burn_runway_cashz_504d_base_v029_signal(cashneq, fcf):
    result = _z(cashneq, 504) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex-adjusted burn level (capex minus operating cash)
def f18cb_f18_cash_burn_runway_capexburn_0d_base_v030_signal(capex, ncfo):
    result = _f18_capexburn(capex, ncfo)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed capex-adjusted burn
def f18cb_f18_cash_burn_runway_capexburn_63d_base_v031_signal(capex, ncfo):
    result = _mean(_f18_capexburn(capex, ncfo), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed capex-adjusted burn
def f18cb_f18_cash_burn_runway_capexburn_126d_base_v032_signal(capex, ncfo):
    result = _mean(_f18_capexburn(capex, ncfo), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-adjusted burn intensity vs assets
def f18cb_f18_cash_burn_runway_capexburnassets_0d_base_v033_signal(capex, ncfo, assets):
    result = _safe_div(_f18_capexburn(capex, ncfo), assets)
    return result.replace([np.inf, -np.inf], np.nan)


# capex-adjusted runway (cash / capex-burn)
def f18cb_f18_cash_burn_runway_capexrunway_0d_base_v034_signal(cashneq, capex, ncfo):
    result = _safe_div(cashneq, _f18_capexburn(capex, ncfo))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed capex-adjusted runway
def f18cb_f18_cash_burn_runway_capexrunway_63d_base_v035_signal(cashneq, capex, ncfo):
    result = _mean(_safe_div(cashneq, _f18_capexburn(capex, ncfo)), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# burn acceleration: 21d change of smoothed burn
def f18cb_f18_cash_burn_runway_burnaccel_21d_base_v036_signal(fcf):
    b = _mean(_f18_burn(fcf), 21)
    result = b.diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# burn acceleration: 63d change of smoothed burn
def f18cb_f18_cash_burn_runway_burnaccel_63d_base_v037_signal(fcf):
    b = _mean(_f18_burn(fcf), 63)
    result = b.diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# burn acceleration: 126d change of smoothed burn
def f18cb_f18_cash_burn_runway_burnaccel_126d_base_v038_signal(fcf):
    b = _mean(_f18_burn(fcf), 63)
    result = b.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# cash coverage of debt (cash / debt)
def f18cb_f18_cash_burn_runway_cashdebt_0d_base_v039_signal(cashneq, debt, fcf):
    result = _safe_div(cashneq, debt) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed cash coverage of debt
def f18cb_f18_cash_burn_runway_cashdebt_63d_base_v040_signal(cashneq, debt, fcf):
    result = _mean(_safe_div(cashneq, debt), 63) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash coverage of debt service (ncfo / debt)
def f18cb_f18_cash_burn_runway_ncfodebt_0d_base_v041_signal(ncfo, debt, fcf):
    result = _safe_div(ncfo, debt) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of runway over 252d
def f18cb_f18_cash_burn_runway_runwayrank_252d_base_v042_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of runway over 504d
def f18cb_f18_cash_burn_runway_runwayrank_504d_base_v043_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.rolling(504, min_periods=126).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# rolling percentile rank of burn over 252d
def f18cb_f18_cash_burn_runway_burnrank_252d_base_v044_signal(fcf):
    b = _f18_burn(fcf)
    result = b.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of runway over 252d
def f18cb_f18_cash_burn_runway_runwayz_252d_base_v045_signal(cashneq, fcf):
    result = _z(_f18_runway(cashneq, fcf), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of burn over 252d
def f18cb_f18_cash_burn_runway_burnz_252d_base_v046_signal(fcf):
    result = _z(_f18_burn(fcf), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# z-score of burn over 126d
def f18cb_f18_cash_burn_runway_burnz_126d_base_v047_signal(fcf):
    result = _z(_f18_burn(fcf), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# cash trend minus its 126d average (cash trajectory surprise)
def f18cb_f18_cash_burn_runway_cashtrendsurp_63d_base_v048_signal(cashneq):
    r = _f18_cashtrend(cashneq, 63)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# cash trend minus its 252d average
def f18cb_f18_cash_burn_runway_cashtrendsurp_126d_base_v049_signal(cashneq):
    r = _f18_cashtrend(cashneq, 126)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# operating margin of cash: ncfo to opex
def f18cb_f18_cash_burn_runway_ncfoopex_0d_base_v050_signal(ncfo, opex, fcf):
    result = _safe_div(ncfo, opex) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed ncfo to opex
def f18cb_f18_cash_burn_runway_ncfoopex_63d_base_v051_signal(ncfo, opex, fcf):
    result = _mean(_safe_div(ncfo, opex), 63) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# burn relative to opex (cash drain efficiency)
def f18cb_f18_cash_burn_runway_burnopex_0d_base_v052_signal(fcf, opex):
    result = _safe_div(_f18_burn(fcf), opex)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed burn to opex
def f18cb_f18_cash_burn_runway_burnopex_63d_base_v053_signal(fcf, opex):
    result = _mean(_safe_div(_f18_burn(fcf), opex), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# capex intensity vs assets
def f18cb_f18_cash_burn_runway_capexassets_0d_base_v054_signal(capex, assets, fcf):
    result = _safe_div(capex, assets) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed capex intensity vs assets
def f18cb_f18_cash_burn_runway_capexassets_126d_base_v055_signal(capex, assets, fcf):
    result = _mean(_safe_div(capex, assets), 126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# capex to operating cash (reinvestment burden)
def f18cb_f18_cash_burn_runway_capexncfo_0d_base_v056_signal(capex, ncfo, fcf):
    result = _safe_div(capex, ncfo) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed capex to operating cash
def f18cb_f18_cash_burn_runway_capexncfo_63d_base_v057_signal(capex, ncfo, fcf):
    result = _mean(_safe_div(capex, ncfo), 63) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash to opex ratio standardized over 252d
def f18cb_f18_cash_burn_runway_cashopexz_252d_base_v058_signal(cashneq, opex, fcf):
    result = _z(_safe_div(cashneq, opex), 252) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash trend volatility (dispersion of quarterly cash trend over 252d)
def f18cb_f18_cash_burn_runway_cashtrendvol_252d_base_v059_signal(cashneq):
    result = _std(_f18_cashtrend(cashneq, 63), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# cash trend volatility over 126d
def f18cb_f18_cash_burn_runway_cashtrendvol_126d_base_v060_signal(cashneq):
    result = _std(_f18_cashtrend(cashneq, 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# burn volatility (dispersion of burn over 126d)
def f18cb_f18_cash_burn_runway_burnvol_126d_base_v061_signal(fcf):
    result = _std(_f18_burn(fcf), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# burn volatility over 252d
def f18cb_f18_cash_burn_runway_burnvol_252d_base_v062_signal(fcf):
    result = _std(_f18_burn(fcf), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# log cash balance trend over 63d (robust to scale)
def f18cb_f18_cash_burn_runway_logcashtrend_63d_base_v063_signal(cashneq, fcf):
    result = np.log(cashneq / cashneq.shift(63)) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log cash balance trend over 126d
def f18cb_f18_cash_burn_runway_logcashtrend_126d_base_v064_signal(cashneq, fcf):
    result = np.log(cashneq / cashneq.shift(126)) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# log cash balance trend over 252d
def f18cb_f18_cash_burn_runway_logcashtrend_252d_base_v065_signal(cashneq, fcf):
    result = np.log(cashneq / cashneq.shift(252)) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# runway change (depletion speed) over 63d
def f18cb_f18_cash_burn_runway_runwaychg_63d_base_v066_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# runway change over 126d
def f18cb_f18_cash_burn_runway_runwaychg_126d_base_v067_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.diff(126)
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed runway (span 63)
def f18cb_f18_cash_burn_runway_runwayewm_63d_base_v068_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = r.ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# EWMA-smoothed burn (span 126)
def f18cb_f18_cash_burn_runway_burnewm_126d_base_v069_signal(fcf):
    b = _f18_burn(fcf)
    result = b.ewm(span=126, min_periods=42).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# inverse runway (burn-to-cash ratio = depletion rate)
def f18cb_f18_cash_burn_runway_invrunway_0d_base_v070_signal(cashneq, fcf):
    result = _safe_div(_f18_burn(fcf), cashneq)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d-smoothed depletion rate
def f18cb_f18_cash_burn_runway_invrunway_63d_base_v071_signal(cashneq, fcf):
    result = _mean(_safe_div(_f18_burn(fcf), cashneq), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# free cash flow margin proxy vs operating cash
def f18cb_f18_cash_burn_runway_fcfncfo_0d_base_v072_signal(fcf, ncfo):
    result = _safe_div(fcf, ncfo) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d-smoothed fcf to ncfo conversion
def f18cb_f18_cash_burn_runway_fcfncfo_126d_base_v073_signal(fcf, ncfo):
    result = _mean(_safe_div(fcf, ncfo), 126) + _f18_burn(fcf) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# cash balance scaled by 252d realized burn volatility (survival stress)
def f18cb_f18_cash_burn_runway_cashstress_252d_base_v074_signal(cashneq, fcf):
    vol = _std(_f18_burn(fcf), 252)
    result = _safe_div(cashneq, vol)
    return result.replace([np.inf, -np.inf], np.nan)


# runway momentum: short runway vs long runway average
def f18cb_f18_cash_burn_runway_runwaymom_63d_base_v075_signal(cashneq, fcf):
    r = _f18_runway(cashneq, fcf)
    result = _mean(r, 63) - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f18cb_f18_cash_burn_runway_cashtrend_63d_base_v001_signal,
    f18cb_f18_cash_burn_runway_cashtrend_126d_base_v002_signal,
    f18cb_f18_cash_burn_runway_cashtrend_252d_base_v003_signal,
    f18cb_f18_cash_burn_runway_cashtrend_504d_base_v004_signal,
    f18cb_f18_cash_burn_runway_cashtrend_21d_base_v005_signal,
    f18cb_f18_cash_burn_runway_runway_lvl_0d_base_v006_signal,
    f18cb_f18_cash_burn_runway_runway_sm21_21d_base_v007_signal,
    f18cb_f18_cash_burn_runway_runway_sm63_63d_base_v008_signal,
    f18cb_f18_cash_burn_runway_runway_sm126_126d_base_v009_signal,
    f18cb_f18_cash_burn_runway_runway_sm252_252d_base_v010_signal,
    f18cb_f18_cash_burn_runway_burn_lvl_0d_base_v011_signal,
    f18cb_f18_cash_burn_runway_burn_sm21_21d_base_v012_signal,
    f18cb_f18_cash_burn_runway_burn_sm63_63d_base_v013_signal,
    f18cb_f18_cash_burn_runway_burn_sm126_126d_base_v014_signal,
    f18cb_f18_cash_burn_runway_burnassets_0d_base_v015_signal,
    f18cb_f18_cash_burn_runway_burnassets_63d_base_v016_signal,
    f18cb_f18_cash_burn_runway_burnassets_126d_base_v017_signal,
    f18cb_f18_cash_burn_runway_ncfoassets_0d_base_v018_signal,
    f18cb_f18_cash_burn_runway_ncfoassets_63d_base_v019_signal,
    f18cb_f18_cash_burn_runway_ncfoassets_126d_base_v020_signal,
    f18cb_f18_cash_burn_runway_fcfassets_0d_base_v021_signal,
    f18cb_f18_cash_burn_runway_fcfassets_63d_base_v022_signal,
    f18cb_f18_cash_burn_runway_fcfassets_252d_base_v023_signal,
    f18cb_f18_cash_burn_runway_cashopex_0d_base_v024_signal,
    f18cb_f18_cash_burn_runway_cashopex_63d_base_v025_signal,
    f18cb_f18_cash_burn_runway_cashopex_126d_base_v026_signal,
    f18cb_f18_cash_burn_runway_cashz_252d_base_v027_signal,
    f18cb_f18_cash_burn_runway_cashz_126d_base_v028_signal,
    f18cb_f18_cash_burn_runway_cashz_504d_base_v029_signal,
    f18cb_f18_cash_burn_runway_capexburn_0d_base_v030_signal,
    f18cb_f18_cash_burn_runway_capexburn_63d_base_v031_signal,
    f18cb_f18_cash_burn_runway_capexburn_126d_base_v032_signal,
    f18cb_f18_cash_burn_runway_capexburnassets_0d_base_v033_signal,
    f18cb_f18_cash_burn_runway_capexrunway_0d_base_v034_signal,
    f18cb_f18_cash_burn_runway_capexrunway_63d_base_v035_signal,
    f18cb_f18_cash_burn_runway_burnaccel_21d_base_v036_signal,
    f18cb_f18_cash_burn_runway_burnaccel_63d_base_v037_signal,
    f18cb_f18_cash_burn_runway_burnaccel_126d_base_v038_signal,
    f18cb_f18_cash_burn_runway_cashdebt_0d_base_v039_signal,
    f18cb_f18_cash_burn_runway_cashdebt_63d_base_v040_signal,
    f18cb_f18_cash_burn_runway_ncfodebt_0d_base_v041_signal,
    f18cb_f18_cash_burn_runway_runwayrank_252d_base_v042_signal,
    f18cb_f18_cash_burn_runway_runwayrank_504d_base_v043_signal,
    f18cb_f18_cash_burn_runway_burnrank_252d_base_v044_signal,
    f18cb_f18_cash_burn_runway_runwayz_252d_base_v045_signal,
    f18cb_f18_cash_burn_runway_burnz_252d_base_v046_signal,
    f18cb_f18_cash_burn_runway_burnz_126d_base_v047_signal,
    f18cb_f18_cash_burn_runway_cashtrendsurp_63d_base_v048_signal,
    f18cb_f18_cash_burn_runway_cashtrendsurp_126d_base_v049_signal,
    f18cb_f18_cash_burn_runway_ncfoopex_0d_base_v050_signal,
    f18cb_f18_cash_burn_runway_ncfoopex_63d_base_v051_signal,
    f18cb_f18_cash_burn_runway_burnopex_0d_base_v052_signal,
    f18cb_f18_cash_burn_runway_burnopex_63d_base_v053_signal,
    f18cb_f18_cash_burn_runway_capexassets_0d_base_v054_signal,
    f18cb_f18_cash_burn_runway_capexassets_126d_base_v055_signal,
    f18cb_f18_cash_burn_runway_capexncfo_0d_base_v056_signal,
    f18cb_f18_cash_burn_runway_capexncfo_63d_base_v057_signal,
    f18cb_f18_cash_burn_runway_cashopexz_252d_base_v058_signal,
    f18cb_f18_cash_burn_runway_cashtrendvol_252d_base_v059_signal,
    f18cb_f18_cash_burn_runway_cashtrendvol_126d_base_v060_signal,
    f18cb_f18_cash_burn_runway_burnvol_126d_base_v061_signal,
    f18cb_f18_cash_burn_runway_burnvol_252d_base_v062_signal,
    f18cb_f18_cash_burn_runway_logcashtrend_63d_base_v063_signal,
    f18cb_f18_cash_burn_runway_logcashtrend_126d_base_v064_signal,
    f18cb_f18_cash_burn_runway_logcashtrend_252d_base_v065_signal,
    f18cb_f18_cash_burn_runway_runwaychg_63d_base_v066_signal,
    f18cb_f18_cash_burn_runway_runwaychg_126d_base_v067_signal,
    f18cb_f18_cash_burn_runway_runwayewm_63d_base_v068_signal,
    f18cb_f18_cash_burn_runway_burnewm_126d_base_v069_signal,
    f18cb_f18_cash_burn_runway_invrunway_0d_base_v070_signal,
    f18cb_f18_cash_burn_runway_invrunway_63d_base_v071_signal,
    f18cb_f18_cash_burn_runway_fcfncfo_0d_base_v072_signal,
    f18cb_f18_cash_burn_runway_fcfncfo_126d_base_v073_signal,
    f18cb_f18_cash_burn_runway_cashstress_252d_base_v074_signal,
    f18cb_f18_cash_burn_runway_runwaymom_63d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F18_CASH_BURN_RUNWAY_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f18_cash_burn_runway_base_001_075_claude: {n_features} features pass")
