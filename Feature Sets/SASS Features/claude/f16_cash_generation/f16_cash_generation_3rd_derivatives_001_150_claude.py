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


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _ewm(s, span):
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _cash_conv(ncfo, netinc):
    return (ncfo / netinc.replace(0, np.nan)).clip(-10, 10)


def _fcf_conv(fcf, netinc):
    return (fcf / netinc.replace(0, np.nan)).clip(-10, 10)


def _fcf_ebitda(fcf, ebitda):
    return (fcf / ebitda.replace(0, np.nan)).clip(-10, 10)


def _ocf_ebitda(ncfo, ebitda):
    return (ncfo / ebitda.replace(0, np.nan)).clip(-10, 10)


def _capex_cover(ncfo, capex):
    cov = (ncfo / capex.replace(0, np.nan)).clip(-20, 20)
    return np.sign(cov) * np.log1p(cov.abs())


def _capex_int(capex, revenue):
    return capex / revenue.replace(0, np.nan)


def _accrual(netinc, ncfo, revenue):
    return (ncfo - netinc) / revenue.replace(0, np.nan)


def _reinv_yield(ncfo, capex, revenue):
    return (ncfo - capex) / revenue.replace(0, np.nan)


def _selffund(ncfo, capex, ebitda):
    return ((ncfo - capex) / ebitda.replace(0, np.nan)).clip(-10, 10)


def _tot_cash(fcf, ncfo, revenue):
    return (fcf + ncfo) / (2.0 * revenue).replace(0, np.nan)

# v001 jerk[z] 5d-roc 21d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_z_5d_jerk_v001_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    sd = _std(slope, 20)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v002 jerk[relsecond] 21d-roc 63d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_relsecond_21d_jerk_v002_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 63)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    scale = base.abs().rolling(84, min_periods=max(1, 42)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v003 jerk[ranksecond] 63d-roc 126d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_ranksecond_63d_jerk_v003_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 126)
    rk = base.rolling(504, min_periods=max(1, 168)).rank(pct=True)
    sl = rk - rk.shift(63)
    b = sl - sl.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v004 jerk[ewmadiff] 63d-roc 252d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_ewmadiff_63d_jerk_v004_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 252)
    fast = _ewm(base, 63) - _ewm(base, 252)
    b = fast - fast.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v005 jerk[signaccel] 126d-roc 504d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_signaccel_126d_jerk_v005_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 504)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126))
    b = np.tanh(jerk * 126)
    return b.replace([np.inf, -np.inf], np.nan)

# v006 jerk[raw] 126d-roc 252d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_raw_126d_jerk_v006_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 252)
    slope = (base - base.shift(126)) / float(126)
    b = (slope - slope.shift(126)) / float(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v007 jerk[z] 21d-roc 126d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_z_21d_jerk_v007_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 126)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v008 jerk[relsecond] 5d-roc 63d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_relsecond_5d_jerk_v008_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 63)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    scale = base.abs().rolling(20, min_periods=max(1, 10)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v009 jerk[ranksecond] 21d-roc 252d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_ranksecond_21d_jerk_v009_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 252)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v010 jerk[ewmadiff] 126d-roc 126d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_ewmadiff_126d_jerk_v010_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 126)
    fast = _ewm(base, 126) - _ewm(base, 504)
    b = fast - fast.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v011 jerk[signaccel] 63d-roc 504d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_signaccel_63d_jerk_v011_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 504)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63))
    b = np.tanh(jerk * 63)
    return b.replace([np.inf, -np.inf], np.nan)

# v012 jerk[raw] 63d-roc 63d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_raw_63d_jerk_v012_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 63)
    slope = (base - base.shift(63)) / float(63)
    b = (slope - slope.shift(63)) / float(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v013 jerk[z] 21d-roc 21d-sm fcfmgn
def f16cg_f16_cash_generation_fcfmgn_z_21d_jerk_v013_signal(fcf, revenue):
    base = _mean(_fcf_margin(fcf, revenue), 21)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v014 jerk[relsecond] 126d-roc 252d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_relsecond_126d_jerk_v014_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 252)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v015 jerk[ranksecond] 21d-roc 126d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_ranksecond_21d_jerk_v015_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 126)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v016 jerk[ewmadiff] 5d-roc 63d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_ewmadiff_5d_jerk_v016_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 63)
    fast = _ewm(base, 5) - _ewm(base, 20)
    b = fast - fast.shift(5)
    return b.replace([np.inf, -np.inf], np.nan)

# v017 jerk[signaccel] 21d-roc 252d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_signaccel_21d_jerk_v017_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 252)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v018 jerk[raw] 126d-roc 126d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_raw_126d_jerk_v018_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 126)
    slope = (base - base.shift(126)) / float(126)
    b = (slope - slope.shift(126)) / float(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v019 jerk[z] 63d-roc 504d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_z_63d_jerk_v019_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 504)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    sd = _std(slope, 252)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v020 jerk[relsecond] 63d-roc 63d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_relsecond_63d_jerk_v020_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 63)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    scale = base.abs().rolling(252, min_periods=max(1, 126)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v021 jerk[ranksecond] 21d-roc 21d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_ranksecond_21d_jerk_v021_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 21)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v022 jerk[z] 5d-roc 21d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_z_5d_jerk_v022_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    sd = _std(slope, 20)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v023 jerk[ewmadiff] 21d-roc 63d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_ewmadiff_21d_jerk_v023_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 63)
    fast = _ewm(base, 21) - _ewm(base, 84)
    b = fast - fast.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v024 jerk[signaccel] 63d-roc 126d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_signaccel_63d_jerk_v024_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 126)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63))
    b = np.tanh(jerk * 63)
    return b.replace([np.inf, -np.inf], np.nan)

# v025 jerk[raw] 63d-roc 252d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_raw_63d_jerk_v025_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 252)
    slope = (base - base.shift(63)) / float(63)
    b = (slope - slope.shift(63)) / float(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v026 jerk[z] 126d-roc 504d-sm ocfmgn
def f16cg_f16_cash_generation_ocfmgn_z_126d_jerk_v026_signal(ncfo, revenue):
    base = _mean(_ocf_margin(ncfo, revenue), 504)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    sd = _std(slope, 504)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v027 jerk[ranksecond] 63d-roc 504d-sm cashconv
def f16cg_f16_cash_generation_cashconv_ranksecond_63d_jerk_v027_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 504)
    rk = base.rolling(504, min_periods=max(1, 168)).rank(pct=True)
    sl = rk - rk.shift(63)
    b = sl - sl.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v028 jerk[ewmadiff] 63d-roc 63d-sm cashconv
def f16cg_f16_cash_generation_cashconv_ewmadiff_63d_jerk_v028_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 63)
    fast = _ewm(base, 63) - _ewm(base, 252)
    b = fast - fast.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v029 jerk[signaccel] 21d-roc 21d-sm cashconv
def f16cg_f16_cash_generation_cashconv_signaccel_21d_jerk_v029_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 21)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v030 jerk[signaccel] 5d-roc 21d-sm cashconv
def f16cg_f16_cash_generation_cashconv_signaccel_5d_jerk_v030_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5))
    b = np.tanh(jerk * 5)
    return b.replace([np.inf, -np.inf], np.nan)

# v031 jerk[raw] 21d-roc 63d-sm cashconv
def f16cg_f16_cash_generation_cashconv_raw_21d_jerk_v031_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 63)
    slope = (base - base.shift(21)) / float(21)
    b = (slope - slope.shift(21)) / float(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v032 jerk[z] 63d-roc 126d-sm cashconv
def f16cg_f16_cash_generation_cashconv_z_63d_jerk_v032_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 126)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    sd = _std(slope, 252)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v033 jerk[relsecond] 63d-roc 252d-sm cashconv
def f16cg_f16_cash_generation_cashconv_relsecond_63d_jerk_v033_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 252)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    scale = base.abs().rolling(252, min_periods=max(1, 126)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v034 jerk[ranksecond] 126d-roc 504d-sm cashconv
def f16cg_f16_cash_generation_cashconv_ranksecond_126d_jerk_v034_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 504)
    rk = base.rolling(1008, min_periods=max(1, 336)).rank(pct=True)
    sl = rk - rk.shift(126)
    b = sl - sl.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v035 jerk[ewmadiff] 126d-roc 252d-sm cashconv
def f16cg_f16_cash_generation_cashconv_ewmadiff_126d_jerk_v035_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 252)
    fast = _ewm(base, 126) - _ewm(base, 504)
    b = fast - fast.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v036 jerk[signaccel] 21d-roc 126d-sm cashconv
def f16cg_f16_cash_generation_cashconv_signaccel_21d_jerk_v036_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 126)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v037 jerk[raw] 5d-roc 63d-sm cashconv
def f16cg_f16_cash_generation_cashconv_raw_5d_jerk_v037_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 63)
    slope = (base - base.shift(5)) / float(5)
    b = (slope - slope.shift(5)) / float(5)
    return b.replace([np.inf, -np.inf], np.nan)

# v038 jerk[z] 21d-roc 252d-sm cashconv
def f16cg_f16_cash_generation_cashconv_z_21d_jerk_v038_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 252)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v039 jerk[relsecond] 126d-roc 126d-sm cashconv
def f16cg_f16_cash_generation_cashconv_relsecond_126d_jerk_v039_signal(ncfo, netinc):
    base = _mean(_cash_conv(ncfo, netinc), 126)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v040 jerk[ranksecond] 63d-roc 126d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_ranksecond_63d_jerk_v040_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 126)
    rk = base.rolling(504, min_periods=max(1, 168)).rank(pct=True)
    sl = rk - rk.shift(63)
    b = sl - sl.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v041 jerk[ewmadiff] 63d-roc 252d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_ewmadiff_63d_jerk_v041_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 252)
    fast = _ewm(base, 63) - _ewm(base, 252)
    b = fast - fast.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v042 jerk[signaccel] 126d-roc 504d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_signaccel_126d_jerk_v042_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 504)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126))
    b = np.tanh(jerk * 126)
    return b.replace([np.inf, -np.inf], np.nan)

# v043 jerk[raw] 126d-roc 252d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_raw_126d_jerk_v043_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 252)
    slope = (base - base.shift(126)) / float(126)
    b = (slope - slope.shift(126)) / float(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v044 jerk[z] 21d-roc 126d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_z_21d_jerk_v044_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 126)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v045 jerk[relsecond] 5d-roc 63d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_relsecond_5d_jerk_v045_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 63)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    scale = base.abs().rolling(20, min_periods=max(1, 10)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v046 jerk[ranksecond] 21d-roc 252d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_ranksecond_21d_jerk_v046_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 252)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v047 jerk[ewmadiff] 126d-roc 126d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_ewmadiff_126d_jerk_v047_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 126)
    fast = _ewm(base, 126) - _ewm(base, 504)
    b = fast - fast.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v048 jerk[signaccel] 63d-roc 504d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_signaccel_63d_jerk_v048_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 504)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63))
    b = np.tanh(jerk * 63)
    return b.replace([np.inf, -np.inf], np.nan)

# v049 jerk[raw] 63d-roc 63d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_raw_63d_jerk_v049_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 63)
    slope = (base - base.shift(63)) / float(63)
    b = (slope - slope.shift(63)) / float(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v050 jerk[z] 21d-roc 21d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_z_21d_jerk_v050_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 21)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v051 jerk[z] 5d-roc 21d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_z_5d_jerk_v051_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    sd = _std(slope, 20)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v052 jerk[relsecond] 21d-roc 63d-sm fcfconv
def f16cg_f16_cash_generation_fcfconv_relsecond_21d_jerk_v052_signal(fcf, netinc):
    base = _mean(_fcf_conv(fcf, netinc), 63)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    scale = base.abs().rolling(84, min_periods=max(1, 42)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v053 jerk[ewmadiff] 5d-roc 63d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_ewmadiff_5d_jerk_v053_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 63)
    fast = _ewm(base, 5) - _ewm(base, 20)
    b = fast - fast.shift(5)
    return b.replace([np.inf, -np.inf], np.nan)

# v054 jerk[signaccel] 21d-roc 252d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_signaccel_21d_jerk_v054_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 252)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v055 jerk[raw] 126d-roc 126d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_raw_126d_jerk_v055_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 126)
    slope = (base - base.shift(126)) / float(126)
    b = (slope - slope.shift(126)) / float(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v056 jerk[z] 63d-roc 504d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_z_63d_jerk_v056_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 504)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    sd = _std(slope, 252)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v057 jerk[relsecond] 63d-roc 63d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_relsecond_63d_jerk_v057_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 63)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    scale = base.abs().rolling(252, min_periods=max(1, 126)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v058 jerk[ranksecond] 21d-roc 21d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_ranksecond_21d_jerk_v058_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 21)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v059 jerk[z] 5d-roc 21d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_z_5d_jerk_v059_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    sd = _std(slope, 20)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v060 jerk[ewmadiff] 21d-roc 63d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_ewmadiff_21d_jerk_v060_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 63)
    fast = _ewm(base, 21) - _ewm(base, 84)
    b = fast - fast.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v061 jerk[signaccel] 63d-roc 126d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_signaccel_63d_jerk_v061_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 126)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63))
    b = np.tanh(jerk * 63)
    return b.replace([np.inf, -np.inf], np.nan)

# v062 jerk[raw] 63d-roc 252d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_raw_63d_jerk_v062_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 252)
    slope = (base - base.shift(63)) / float(63)
    b = (slope - slope.shift(63)) / float(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v063 jerk[relsecond] 126d-roc 504d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_relsecond_126d_jerk_v063_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 504)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v064 jerk[relsecond] 126d-roc 252d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_relsecond_126d_jerk_v064_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 252)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v065 jerk[ranksecond] 21d-roc 126d-sm fcfebitda
def f16cg_f16_cash_generation_fcfebitda_ranksecond_21d_jerk_v065_signal(fcf, ebitda):
    base = _mean(_fcf_ebitda(fcf, ebitda), 126)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v066 jerk[signaccel] 21d-roc 21d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_signaccel_21d_jerk_v066_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 21)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v067 jerk[signaccel] 5d-roc 21d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_signaccel_5d_jerk_v067_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5))
    b = np.tanh(jerk * 5)
    return b.replace([np.inf, -np.inf], np.nan)

# v068 jerk[raw] 21d-roc 63d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_raw_21d_jerk_v068_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 63)
    slope = (base - base.shift(21)) / float(21)
    b = (slope - slope.shift(21)) / float(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v069 jerk[z] 63d-roc 126d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_z_63d_jerk_v069_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 126)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    sd = _std(slope, 252)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v070 jerk[relsecond] 63d-roc 252d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_relsecond_63d_jerk_v070_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 252)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    scale = base.abs().rolling(252, min_periods=max(1, 126)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v071 jerk[ranksecond] 126d-roc 504d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_ranksecond_126d_jerk_v071_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 504)
    rk = base.rolling(1008, min_periods=max(1, 336)).rank(pct=True)
    sl = rk - rk.shift(126)
    b = sl - sl.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v072 jerk[ewmadiff] 126d-roc 252d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_ewmadiff_126d_jerk_v072_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 252)
    fast = _ewm(base, 126) - _ewm(base, 504)
    b = fast - fast.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v073 jerk[signaccel] 21d-roc 126d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_signaccel_21d_jerk_v073_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 126)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v074 jerk[raw] 5d-roc 63d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_raw_5d_jerk_v074_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 63)
    slope = (base - base.shift(5)) / float(5)
    b = (slope - slope.shift(5)) / float(5)
    return b.replace([np.inf, -np.inf], np.nan)

# v075 jerk[z] 21d-roc 252d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_z_21d_jerk_v075_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 252)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v076 jerk[relsecond] 126d-roc 126d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_relsecond_126d_jerk_v076_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 126)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v077 jerk[ranksecond] 63d-roc 504d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_ranksecond_63d_jerk_v077_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 504)
    rk = base.rolling(504, min_periods=max(1, 168)).rank(pct=True)
    sl = rk - rk.shift(63)
    b = sl - sl.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v078 jerk[ewmadiff] 63d-roc 63d-sm capexwedge
def f16cg_f16_cash_generation_capexwedge_ewmadiff_63d_jerk_v078_signal(ncfo, fcf, ebitda):
    base = _mean((_ocf_ebitda(ncfo, ebitda) - _fcf_ebitda(fcf, ebitda)), 63)
    fast = _ewm(base, 63) - _ewm(base, 252)
    b = fast - fast.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v079 jerk[signaccel] 126d-roc 504d-sm capexcov
def f16cg_f16_cash_generation_capexcov_signaccel_126d_jerk_v079_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 504)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126))
    b = np.tanh(jerk * 126)
    return b.replace([np.inf, -np.inf], np.nan)

# v080 jerk[raw] 126d-roc 252d-sm capexcov
def f16cg_f16_cash_generation_capexcov_raw_126d_jerk_v080_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 252)
    slope = (base - base.shift(126)) / float(126)
    b = (slope - slope.shift(126)) / float(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v081 jerk[z] 21d-roc 126d-sm capexcov
def f16cg_f16_cash_generation_capexcov_z_21d_jerk_v081_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 126)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v082 jerk[relsecond] 5d-roc 63d-sm capexcov
def f16cg_f16_cash_generation_capexcov_relsecond_5d_jerk_v082_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 63)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    scale = base.abs().rolling(20, min_periods=max(1, 10)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v083 jerk[ranksecond] 21d-roc 252d-sm capexcov
def f16cg_f16_cash_generation_capexcov_ranksecond_21d_jerk_v083_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 252)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v084 jerk[ewmadiff] 126d-roc 126d-sm capexcov
def f16cg_f16_cash_generation_capexcov_ewmadiff_126d_jerk_v084_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 126)
    fast = _ewm(base, 126) - _ewm(base, 504)
    b = fast - fast.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v085 jerk[signaccel] 63d-roc 504d-sm capexcov
def f16cg_f16_cash_generation_capexcov_signaccel_63d_jerk_v085_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 504)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63))
    b = np.tanh(jerk * 63)
    return b.replace([np.inf, -np.inf], np.nan)

# v086 jerk[raw] 63d-roc 63d-sm capexcov
def f16cg_f16_cash_generation_capexcov_raw_63d_jerk_v086_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 63)
    slope = (base - base.shift(63)) / float(63)
    b = (slope - slope.shift(63)) / float(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v087 jerk[z] 21d-roc 21d-sm capexcov
def f16cg_f16_cash_generation_capexcov_z_21d_jerk_v087_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 21)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v088 jerk[z] 5d-roc 21d-sm capexcov
def f16cg_f16_cash_generation_capexcov_z_5d_jerk_v088_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    sd = _std(slope, 20)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v089 jerk[relsecond] 21d-roc 63d-sm capexcov
def f16cg_f16_cash_generation_capexcov_relsecond_21d_jerk_v089_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 63)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    scale = base.abs().rolling(84, min_periods=max(1, 42)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v090 jerk[ranksecond] 63d-roc 126d-sm capexcov
def f16cg_f16_cash_generation_capexcov_ranksecond_63d_jerk_v090_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 126)
    rk = base.rolling(504, min_periods=max(1, 168)).rank(pct=True)
    sl = rk - rk.shift(63)
    b = sl - sl.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v091 jerk[ewmadiff] 63d-roc 252d-sm capexcov
def f16cg_f16_cash_generation_capexcov_ewmadiff_63d_jerk_v091_signal(ncfo, capex):
    base = _mean(_capex_cover(ncfo, capex), 252)
    fast = _ewm(base, 63) - _ewm(base, 252)
    b = fast - fast.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v092 jerk[raw] 126d-roc 126d-sm capexint
def f16cg_f16_cash_generation_capexint_raw_126d_jerk_v092_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 126)
    slope = (base - base.shift(126)) / float(126)
    b = (slope - slope.shift(126)) / float(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v093 jerk[z] 63d-roc 504d-sm capexint
def f16cg_f16_cash_generation_capexint_z_63d_jerk_v093_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 504)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    sd = _std(slope, 252)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v094 jerk[relsecond] 63d-roc 63d-sm capexint
def f16cg_f16_cash_generation_capexint_relsecond_63d_jerk_v094_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 63)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    scale = base.abs().rolling(252, min_periods=max(1, 126)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v095 jerk[ranksecond] 21d-roc 21d-sm capexint
def f16cg_f16_cash_generation_capexint_ranksecond_21d_jerk_v095_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 21)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v096 jerk[z] 5d-roc 21d-sm capexint
def f16cg_f16_cash_generation_capexint_z_5d_jerk_v096_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    sd = _std(slope, 20)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v097 jerk[ewmadiff] 21d-roc 63d-sm capexint
def f16cg_f16_cash_generation_capexint_ewmadiff_21d_jerk_v097_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 63)
    fast = _ewm(base, 21) - _ewm(base, 84)
    b = fast - fast.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v098 jerk[signaccel] 63d-roc 126d-sm capexint
def f16cg_f16_cash_generation_capexint_signaccel_63d_jerk_v098_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 126)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63))
    b = np.tanh(jerk * 63)
    return b.replace([np.inf, -np.inf], np.nan)

# v099 jerk[raw] 63d-roc 252d-sm capexint
def f16cg_f16_cash_generation_capexint_raw_63d_jerk_v099_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 252)
    slope = (base - base.shift(63)) / float(63)
    b = (slope - slope.shift(63)) / float(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v100 jerk[z] 126d-roc 504d-sm capexint
def f16cg_f16_cash_generation_capexint_z_126d_jerk_v100_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 504)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    sd = _std(slope, 504)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v101 jerk[relsecond] 126d-roc 252d-sm capexint
def f16cg_f16_cash_generation_capexint_relsecond_126d_jerk_v101_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 252)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v102 jerk[ranksecond] 21d-roc 126d-sm capexint
def f16cg_f16_cash_generation_capexint_ranksecond_21d_jerk_v102_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 126)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v103 jerk[ewmadiff] 5d-roc 63d-sm capexint
def f16cg_f16_cash_generation_capexint_ewmadiff_5d_jerk_v103_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 63)
    fast = _ewm(base, 5) - _ewm(base, 20)
    b = fast - fast.shift(5)
    return b.replace([np.inf, -np.inf], np.nan)

# v104 jerk[signaccel] 21d-roc 252d-sm capexint
def f16cg_f16_cash_generation_capexint_signaccel_21d_jerk_v104_signal(capex, revenue):
    base = _mean(_capex_int(capex, revenue), 252)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v105 jerk[raw] 21d-roc 63d-sm accrual
def f16cg_f16_cash_generation_accrual_raw_21d_jerk_v105_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 63)
    slope = (base - base.shift(21)) / float(21)
    b = (slope - slope.shift(21)) / float(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v106 jerk[z] 63d-roc 126d-sm accrual
def f16cg_f16_cash_generation_accrual_z_63d_jerk_v106_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 126)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    sd = _std(slope, 252)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v107 jerk[relsecond] 63d-roc 252d-sm accrual
def f16cg_f16_cash_generation_accrual_relsecond_63d_jerk_v107_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 252)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    scale = base.abs().rolling(252, min_periods=max(1, 126)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v108 jerk[ranksecond] 126d-roc 504d-sm accrual
def f16cg_f16_cash_generation_accrual_ranksecond_126d_jerk_v108_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 504)
    rk = base.rolling(1008, min_periods=max(1, 336)).rank(pct=True)
    sl = rk - rk.shift(126)
    b = sl - sl.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v109 jerk[ewmadiff] 126d-roc 252d-sm accrual
def f16cg_f16_cash_generation_accrual_ewmadiff_126d_jerk_v109_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 252)
    fast = _ewm(base, 126) - _ewm(base, 504)
    b = fast - fast.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v110 jerk[signaccel] 21d-roc 126d-sm accrual
def f16cg_f16_cash_generation_accrual_signaccel_21d_jerk_v110_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 126)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v111 jerk[raw] 5d-roc 63d-sm accrual
def f16cg_f16_cash_generation_accrual_raw_5d_jerk_v111_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 63)
    slope = (base - base.shift(5)) / float(5)
    b = (slope - slope.shift(5)) / float(5)
    return b.replace([np.inf, -np.inf], np.nan)

# v112 jerk[z] 21d-roc 252d-sm accrual
def f16cg_f16_cash_generation_accrual_z_21d_jerk_v112_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 252)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v113 jerk[relsecond] 126d-roc 126d-sm accrual
def f16cg_f16_cash_generation_accrual_relsecond_126d_jerk_v113_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 126)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v114 jerk[ranksecond] 63d-roc 504d-sm accrual
def f16cg_f16_cash_generation_accrual_ranksecond_63d_jerk_v114_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 504)
    rk = base.rolling(504, min_periods=max(1, 168)).rank(pct=True)
    sl = rk - rk.shift(63)
    b = sl - sl.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v115 jerk[ewmadiff] 63d-roc 63d-sm accrual
def f16cg_f16_cash_generation_accrual_ewmadiff_63d_jerk_v115_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 63)
    fast = _ewm(base, 63) - _ewm(base, 252)
    b = fast - fast.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v116 jerk[signaccel] 21d-roc 21d-sm accrual
def f16cg_f16_cash_generation_accrual_signaccel_21d_jerk_v116_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 21)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v117 jerk[signaccel] 5d-roc 21d-sm accrual
def f16cg_f16_cash_generation_accrual_signaccel_5d_jerk_v117_signal(netinc, ncfo, revenue):
    base = _mean(_accrual(netinc, ncfo, revenue), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5))
    b = np.tanh(jerk * 5)
    return b.replace([np.inf, -np.inf], np.nan)

# v118 jerk[z] 21d-roc 126d-sm cashacct
def f16cg_f16_cash_generation_cashacct_z_21d_jerk_v118_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 126)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v119 jerk[relsecond] 5d-roc 63d-sm cashacct
def f16cg_f16_cash_generation_cashacct_relsecond_5d_jerk_v119_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 63)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    scale = base.abs().rolling(20, min_periods=max(1, 10)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v120 jerk[ranksecond] 21d-roc 252d-sm cashacct
def f16cg_f16_cash_generation_cashacct_ranksecond_21d_jerk_v120_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 252)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v121 jerk[ewmadiff] 126d-roc 126d-sm cashacct
def f16cg_f16_cash_generation_cashacct_ewmadiff_126d_jerk_v121_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 126)
    fast = _ewm(base, 126) - _ewm(base, 504)
    b = fast - fast.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v122 jerk[signaccel] 63d-roc 504d-sm cashacct
def f16cg_f16_cash_generation_cashacct_signaccel_63d_jerk_v122_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 504)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63))
    b = np.tanh(jerk * 63)
    return b.replace([np.inf, -np.inf], np.nan)

# v123 jerk[raw] 63d-roc 63d-sm cashacct
def f16cg_f16_cash_generation_cashacct_raw_63d_jerk_v123_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 63)
    slope = (base - base.shift(63)) / float(63)
    b = (slope - slope.shift(63)) / float(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v124 jerk[z] 21d-roc 21d-sm cashacct
def f16cg_f16_cash_generation_cashacct_z_21d_jerk_v124_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 21)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v125 jerk[z] 5d-roc 21d-sm cashacct
def f16cg_f16_cash_generation_cashacct_z_5d_jerk_v125_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    sd = _std(slope, 20)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v126 jerk[relsecond] 21d-roc 63d-sm cashacct
def f16cg_f16_cash_generation_cashacct_relsecond_21d_jerk_v126_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 63)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    scale = base.abs().rolling(84, min_periods=max(1, 42)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v127 jerk[ranksecond] 63d-roc 126d-sm cashacct
def f16cg_f16_cash_generation_cashacct_ranksecond_63d_jerk_v127_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 126)
    rk = base.rolling(504, min_periods=max(1, 168)).rank(pct=True)
    sl = rk - rk.shift(63)
    b = sl - sl.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v128 jerk[ewmadiff] 63d-roc 252d-sm cashacct
def f16cg_f16_cash_generation_cashacct_ewmadiff_63d_jerk_v128_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 252)
    fast = _ewm(base, 63) - _ewm(base, 252)
    b = fast - fast.shift(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v129 jerk[signaccel] 126d-roc 504d-sm cashacct
def f16cg_f16_cash_generation_cashacct_signaccel_126d_jerk_v129_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 504)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126))
    b = np.tanh(jerk * 126)
    return b.replace([np.inf, -np.inf], np.nan)

# v130 jerk[raw] 126d-roc 252d-sm cashacct
def f16cg_f16_cash_generation_cashacct_raw_126d_jerk_v130_signal(fcf, netinc, revenue):
    base = _mean(((fcf - netinc) / revenue.replace(0, np.nan)), 252)
    slope = (base - base.shift(126)) / float(126)
    b = (slope - slope.shift(126)) / float(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v131 jerk[relsecond] 63d-roc 63d-sm selffund
def f16cg_f16_cash_generation_selffund_relsecond_63d_jerk_v131_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 63)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    scale = base.abs().rolling(252, min_periods=max(1, 126)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v132 jerk[ranksecond] 21d-roc 21d-sm selffund
def f16cg_f16_cash_generation_selffund_ranksecond_21d_jerk_v132_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 21)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v133 jerk[z] 5d-roc 21d-sm selffund
def f16cg_f16_cash_generation_selffund_z_5d_jerk_v133_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 21)
    slope = (base - base.shift(5)) / float(5)
    jerk = (slope - slope.shift(5)) / float(5)
    sd = _std(slope, 20)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v134 jerk[ewmadiff] 21d-roc 63d-sm selffund
def f16cg_f16_cash_generation_selffund_ewmadiff_21d_jerk_v134_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 63)
    fast = _ewm(base, 21) - _ewm(base, 84)
    b = fast - fast.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v135 jerk[signaccel] 63d-roc 126d-sm selffund
def f16cg_f16_cash_generation_selffund_signaccel_63d_jerk_v135_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 126)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63))
    b = np.tanh(jerk * 63)
    return b.replace([np.inf, -np.inf], np.nan)

# v136 jerk[raw] 63d-roc 252d-sm selffund
def f16cg_f16_cash_generation_selffund_raw_63d_jerk_v136_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 252)
    slope = (base - base.shift(63)) / float(63)
    b = (slope - slope.shift(63)) / float(63)
    return b.replace([np.inf, -np.inf], np.nan)

# v137 jerk[z] 126d-roc 504d-sm selffund
def f16cg_f16_cash_generation_selffund_z_126d_jerk_v137_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 504)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    sd = _std(slope, 504)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v138 jerk[relsecond] 126d-roc 252d-sm selffund
def f16cg_f16_cash_generation_selffund_relsecond_126d_jerk_v138_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 252)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v139 jerk[ranksecond] 21d-roc 126d-sm selffund
def f16cg_f16_cash_generation_selffund_ranksecond_21d_jerk_v139_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 126)
    rk = base.rolling(168, min_periods=max(1, 56)).rank(pct=True)
    sl = rk - rk.shift(21)
    b = sl - sl.shift(21)
    return b.replace([np.inf, -np.inf], np.nan)

# v140 jerk[ewmadiff] 5d-roc 63d-sm selffund
def f16cg_f16_cash_generation_selffund_ewmadiff_5d_jerk_v140_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 63)
    fast = _ewm(base, 5) - _ewm(base, 20)
    b = fast - fast.shift(5)
    return b.replace([np.inf, -np.inf], np.nan)

# v141 jerk[signaccel] 21d-roc 252d-sm selffund
def f16cg_f16_cash_generation_selffund_signaccel_21d_jerk_v141_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 252)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v142 jerk[raw] 126d-roc 126d-sm selffund
def f16cg_f16_cash_generation_selffund_raw_126d_jerk_v142_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 126)
    slope = (base - base.shift(126)) / float(126)
    b = (slope - slope.shift(126)) / float(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v143 jerk[z] 63d-roc 504d-sm selffund
def f16cg_f16_cash_generation_selffund_z_63d_jerk_v143_signal(ncfo, capex, ebitda):
    base = _mean(_selffund(ncfo, capex, ebitda), 504)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    sd = _std(slope, 252)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v144 jerk[relsecond] 63d-roc 252d-sm totcash
def f16cg_f16_cash_generation_totcash_relsecond_63d_jerk_v144_signal(fcf, ncfo, revenue):
    base = _mean(_tot_cash(fcf, ncfo, revenue), 252)
    slope = (base - base.shift(63)) / float(63)
    jerk = (slope - slope.shift(63)) / float(63)
    scale = base.abs().rolling(252, min_periods=max(1, 126)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v145 jerk[ranksecond] 126d-roc 504d-sm totcash
def f16cg_f16_cash_generation_totcash_ranksecond_126d_jerk_v145_signal(fcf, ncfo, revenue):
    base = _mean(_tot_cash(fcf, ncfo, revenue), 504)
    rk = base.rolling(1008, min_periods=max(1, 336)).rank(pct=True)
    sl = rk - rk.shift(126)
    b = sl - sl.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v146 jerk[ewmadiff] 126d-roc 252d-sm totcash
def f16cg_f16_cash_generation_totcash_ewmadiff_126d_jerk_v146_signal(fcf, ncfo, revenue):
    base = _mean(_tot_cash(fcf, ncfo, revenue), 252)
    fast = _ewm(base, 126) - _ewm(base, 504)
    b = fast - fast.shift(126)
    return b.replace([np.inf, -np.inf], np.nan)

# v147 jerk[signaccel] 21d-roc 126d-sm totcash
def f16cg_f16_cash_generation_totcash_signaccel_21d_jerk_v147_signal(fcf, ncfo, revenue):
    base = _mean(_tot_cash(fcf, ncfo, revenue), 126)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21))
    b = np.tanh(jerk * 21)
    return b.replace([np.inf, -np.inf], np.nan)

# v148 jerk[raw] 5d-roc 63d-sm totcash
def f16cg_f16_cash_generation_totcash_raw_5d_jerk_v148_signal(fcf, ncfo, revenue):
    base = _mean(_tot_cash(fcf, ncfo, revenue), 63)
    slope = (base - base.shift(5)) / float(5)
    b = (slope - slope.shift(5)) / float(5)
    return b.replace([np.inf, -np.inf], np.nan)

# v149 jerk[z] 21d-roc 252d-sm totcash
def f16cg_f16_cash_generation_totcash_z_21d_jerk_v149_signal(fcf, ncfo, revenue):
    base = _mean(_tot_cash(fcf, ncfo, revenue), 252)
    slope = (base - base.shift(21)) / float(21)
    jerk = (slope - slope.shift(21)) / float(21)
    sd = _std(slope, 84)
    b = jerk / sd.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)

# v150 jerk[relsecond] 126d-roc 126d-sm totcash
def f16cg_f16_cash_generation_totcash_relsecond_126d_jerk_v150_signal(fcf, ncfo, revenue):
    base = _mean(_tot_cash(fcf, ncfo, revenue), 126)
    slope = (base - base.shift(126)) / float(126)
    jerk = (slope - slope.shift(126)) / float(126)
    scale = base.abs().rolling(504, min_periods=max(1, 252)).mean()
    b = jerk / scale.replace(0, np.nan)
    return b.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f16cg_f16_cash_generation_fcfmgn_z_5d_jerk_v001_signal,
    f16cg_f16_cash_generation_fcfmgn_relsecond_21d_jerk_v002_signal,
    f16cg_f16_cash_generation_fcfmgn_ranksecond_63d_jerk_v003_signal,
    f16cg_f16_cash_generation_fcfmgn_ewmadiff_63d_jerk_v004_signal,
    f16cg_f16_cash_generation_fcfmgn_signaccel_126d_jerk_v005_signal,
    f16cg_f16_cash_generation_fcfmgn_raw_126d_jerk_v006_signal,
    f16cg_f16_cash_generation_fcfmgn_z_21d_jerk_v007_signal,
    f16cg_f16_cash_generation_fcfmgn_relsecond_5d_jerk_v008_signal,
    f16cg_f16_cash_generation_fcfmgn_ranksecond_21d_jerk_v009_signal,
    f16cg_f16_cash_generation_fcfmgn_ewmadiff_126d_jerk_v010_signal,
    f16cg_f16_cash_generation_fcfmgn_signaccel_63d_jerk_v011_signal,
    f16cg_f16_cash_generation_fcfmgn_raw_63d_jerk_v012_signal,
    f16cg_f16_cash_generation_fcfmgn_z_21d_jerk_v013_signal,
    f16cg_f16_cash_generation_ocfmgn_relsecond_126d_jerk_v014_signal,
    f16cg_f16_cash_generation_ocfmgn_ranksecond_21d_jerk_v015_signal,
    f16cg_f16_cash_generation_ocfmgn_ewmadiff_5d_jerk_v016_signal,
    f16cg_f16_cash_generation_ocfmgn_signaccel_21d_jerk_v017_signal,
    f16cg_f16_cash_generation_ocfmgn_raw_126d_jerk_v018_signal,
    f16cg_f16_cash_generation_ocfmgn_z_63d_jerk_v019_signal,
    f16cg_f16_cash_generation_ocfmgn_relsecond_63d_jerk_v020_signal,
    f16cg_f16_cash_generation_ocfmgn_ranksecond_21d_jerk_v021_signal,
    f16cg_f16_cash_generation_ocfmgn_z_5d_jerk_v022_signal,
    f16cg_f16_cash_generation_ocfmgn_ewmadiff_21d_jerk_v023_signal,
    f16cg_f16_cash_generation_ocfmgn_signaccel_63d_jerk_v024_signal,
    f16cg_f16_cash_generation_ocfmgn_raw_63d_jerk_v025_signal,
    f16cg_f16_cash_generation_ocfmgn_z_126d_jerk_v026_signal,
    f16cg_f16_cash_generation_cashconv_ranksecond_63d_jerk_v027_signal,
    f16cg_f16_cash_generation_cashconv_ewmadiff_63d_jerk_v028_signal,
    f16cg_f16_cash_generation_cashconv_signaccel_21d_jerk_v029_signal,
    f16cg_f16_cash_generation_cashconv_signaccel_5d_jerk_v030_signal,
    f16cg_f16_cash_generation_cashconv_raw_21d_jerk_v031_signal,
    f16cg_f16_cash_generation_cashconv_z_63d_jerk_v032_signal,
    f16cg_f16_cash_generation_cashconv_relsecond_63d_jerk_v033_signal,
    f16cg_f16_cash_generation_cashconv_ranksecond_126d_jerk_v034_signal,
    f16cg_f16_cash_generation_cashconv_ewmadiff_126d_jerk_v035_signal,
    f16cg_f16_cash_generation_cashconv_signaccel_21d_jerk_v036_signal,
    f16cg_f16_cash_generation_cashconv_raw_5d_jerk_v037_signal,
    f16cg_f16_cash_generation_cashconv_z_21d_jerk_v038_signal,
    f16cg_f16_cash_generation_cashconv_relsecond_126d_jerk_v039_signal,
    f16cg_f16_cash_generation_fcfconv_ranksecond_63d_jerk_v040_signal,
    f16cg_f16_cash_generation_fcfconv_ewmadiff_63d_jerk_v041_signal,
    f16cg_f16_cash_generation_fcfconv_signaccel_126d_jerk_v042_signal,
    f16cg_f16_cash_generation_fcfconv_raw_126d_jerk_v043_signal,
    f16cg_f16_cash_generation_fcfconv_z_21d_jerk_v044_signal,
    f16cg_f16_cash_generation_fcfconv_relsecond_5d_jerk_v045_signal,
    f16cg_f16_cash_generation_fcfconv_ranksecond_21d_jerk_v046_signal,
    f16cg_f16_cash_generation_fcfconv_ewmadiff_126d_jerk_v047_signal,
    f16cg_f16_cash_generation_fcfconv_signaccel_63d_jerk_v048_signal,
    f16cg_f16_cash_generation_fcfconv_raw_63d_jerk_v049_signal,
    f16cg_f16_cash_generation_fcfconv_z_21d_jerk_v050_signal,
    f16cg_f16_cash_generation_fcfconv_z_5d_jerk_v051_signal,
    f16cg_f16_cash_generation_fcfconv_relsecond_21d_jerk_v052_signal,
    f16cg_f16_cash_generation_fcfebitda_ewmadiff_5d_jerk_v053_signal,
    f16cg_f16_cash_generation_fcfebitda_signaccel_21d_jerk_v054_signal,
    f16cg_f16_cash_generation_fcfebitda_raw_126d_jerk_v055_signal,
    f16cg_f16_cash_generation_fcfebitda_z_63d_jerk_v056_signal,
    f16cg_f16_cash_generation_fcfebitda_relsecond_63d_jerk_v057_signal,
    f16cg_f16_cash_generation_fcfebitda_ranksecond_21d_jerk_v058_signal,
    f16cg_f16_cash_generation_fcfebitda_z_5d_jerk_v059_signal,
    f16cg_f16_cash_generation_fcfebitda_ewmadiff_21d_jerk_v060_signal,
    f16cg_f16_cash_generation_fcfebitda_signaccel_63d_jerk_v061_signal,
    f16cg_f16_cash_generation_fcfebitda_raw_63d_jerk_v062_signal,
    f16cg_f16_cash_generation_fcfebitda_relsecond_126d_jerk_v063_signal,
    f16cg_f16_cash_generation_fcfebitda_relsecond_126d_jerk_v064_signal,
    f16cg_f16_cash_generation_fcfebitda_ranksecond_21d_jerk_v065_signal,
    f16cg_f16_cash_generation_capexwedge_signaccel_21d_jerk_v066_signal,
    f16cg_f16_cash_generation_capexwedge_signaccel_5d_jerk_v067_signal,
    f16cg_f16_cash_generation_capexwedge_raw_21d_jerk_v068_signal,
    f16cg_f16_cash_generation_capexwedge_z_63d_jerk_v069_signal,
    f16cg_f16_cash_generation_capexwedge_relsecond_63d_jerk_v070_signal,
    f16cg_f16_cash_generation_capexwedge_ranksecond_126d_jerk_v071_signal,
    f16cg_f16_cash_generation_capexwedge_ewmadiff_126d_jerk_v072_signal,
    f16cg_f16_cash_generation_capexwedge_signaccel_21d_jerk_v073_signal,
    f16cg_f16_cash_generation_capexwedge_raw_5d_jerk_v074_signal,
    f16cg_f16_cash_generation_capexwedge_z_21d_jerk_v075_signal,
    f16cg_f16_cash_generation_capexwedge_relsecond_126d_jerk_v076_signal,
    f16cg_f16_cash_generation_capexwedge_ranksecond_63d_jerk_v077_signal,
    f16cg_f16_cash_generation_capexwedge_ewmadiff_63d_jerk_v078_signal,
    f16cg_f16_cash_generation_capexcov_signaccel_126d_jerk_v079_signal,
    f16cg_f16_cash_generation_capexcov_raw_126d_jerk_v080_signal,
    f16cg_f16_cash_generation_capexcov_z_21d_jerk_v081_signal,
    f16cg_f16_cash_generation_capexcov_relsecond_5d_jerk_v082_signal,
    f16cg_f16_cash_generation_capexcov_ranksecond_21d_jerk_v083_signal,
    f16cg_f16_cash_generation_capexcov_ewmadiff_126d_jerk_v084_signal,
    f16cg_f16_cash_generation_capexcov_signaccel_63d_jerk_v085_signal,
    f16cg_f16_cash_generation_capexcov_raw_63d_jerk_v086_signal,
    f16cg_f16_cash_generation_capexcov_z_21d_jerk_v087_signal,
    f16cg_f16_cash_generation_capexcov_z_5d_jerk_v088_signal,
    f16cg_f16_cash_generation_capexcov_relsecond_21d_jerk_v089_signal,
    f16cg_f16_cash_generation_capexcov_ranksecond_63d_jerk_v090_signal,
    f16cg_f16_cash_generation_capexcov_ewmadiff_63d_jerk_v091_signal,
    f16cg_f16_cash_generation_capexint_raw_126d_jerk_v092_signal,
    f16cg_f16_cash_generation_capexint_z_63d_jerk_v093_signal,
    f16cg_f16_cash_generation_capexint_relsecond_63d_jerk_v094_signal,
    f16cg_f16_cash_generation_capexint_ranksecond_21d_jerk_v095_signal,
    f16cg_f16_cash_generation_capexint_z_5d_jerk_v096_signal,
    f16cg_f16_cash_generation_capexint_ewmadiff_21d_jerk_v097_signal,
    f16cg_f16_cash_generation_capexint_signaccel_63d_jerk_v098_signal,
    f16cg_f16_cash_generation_capexint_raw_63d_jerk_v099_signal,
    f16cg_f16_cash_generation_capexint_z_126d_jerk_v100_signal,
    f16cg_f16_cash_generation_capexint_relsecond_126d_jerk_v101_signal,
    f16cg_f16_cash_generation_capexint_ranksecond_21d_jerk_v102_signal,
    f16cg_f16_cash_generation_capexint_ewmadiff_5d_jerk_v103_signal,
    f16cg_f16_cash_generation_capexint_signaccel_21d_jerk_v104_signal,
    f16cg_f16_cash_generation_accrual_raw_21d_jerk_v105_signal,
    f16cg_f16_cash_generation_accrual_z_63d_jerk_v106_signal,
    f16cg_f16_cash_generation_accrual_relsecond_63d_jerk_v107_signal,
    f16cg_f16_cash_generation_accrual_ranksecond_126d_jerk_v108_signal,
    f16cg_f16_cash_generation_accrual_ewmadiff_126d_jerk_v109_signal,
    f16cg_f16_cash_generation_accrual_signaccel_21d_jerk_v110_signal,
    f16cg_f16_cash_generation_accrual_raw_5d_jerk_v111_signal,
    f16cg_f16_cash_generation_accrual_z_21d_jerk_v112_signal,
    f16cg_f16_cash_generation_accrual_relsecond_126d_jerk_v113_signal,
    f16cg_f16_cash_generation_accrual_ranksecond_63d_jerk_v114_signal,
    f16cg_f16_cash_generation_accrual_ewmadiff_63d_jerk_v115_signal,
    f16cg_f16_cash_generation_accrual_signaccel_21d_jerk_v116_signal,
    f16cg_f16_cash_generation_accrual_signaccel_5d_jerk_v117_signal,
    f16cg_f16_cash_generation_cashacct_z_21d_jerk_v118_signal,
    f16cg_f16_cash_generation_cashacct_relsecond_5d_jerk_v119_signal,
    f16cg_f16_cash_generation_cashacct_ranksecond_21d_jerk_v120_signal,
    f16cg_f16_cash_generation_cashacct_ewmadiff_126d_jerk_v121_signal,
    f16cg_f16_cash_generation_cashacct_signaccel_63d_jerk_v122_signal,
    f16cg_f16_cash_generation_cashacct_raw_63d_jerk_v123_signal,
    f16cg_f16_cash_generation_cashacct_z_21d_jerk_v124_signal,
    f16cg_f16_cash_generation_cashacct_z_5d_jerk_v125_signal,
    f16cg_f16_cash_generation_cashacct_relsecond_21d_jerk_v126_signal,
    f16cg_f16_cash_generation_cashacct_ranksecond_63d_jerk_v127_signal,
    f16cg_f16_cash_generation_cashacct_ewmadiff_63d_jerk_v128_signal,
    f16cg_f16_cash_generation_cashacct_signaccel_126d_jerk_v129_signal,
    f16cg_f16_cash_generation_cashacct_raw_126d_jerk_v130_signal,
    f16cg_f16_cash_generation_selffund_relsecond_63d_jerk_v131_signal,
    f16cg_f16_cash_generation_selffund_ranksecond_21d_jerk_v132_signal,
    f16cg_f16_cash_generation_selffund_z_5d_jerk_v133_signal,
    f16cg_f16_cash_generation_selffund_ewmadiff_21d_jerk_v134_signal,
    f16cg_f16_cash_generation_selffund_signaccel_63d_jerk_v135_signal,
    f16cg_f16_cash_generation_selffund_raw_63d_jerk_v136_signal,
    f16cg_f16_cash_generation_selffund_z_126d_jerk_v137_signal,
    f16cg_f16_cash_generation_selffund_relsecond_126d_jerk_v138_signal,
    f16cg_f16_cash_generation_selffund_ranksecond_21d_jerk_v139_signal,
    f16cg_f16_cash_generation_selffund_ewmadiff_5d_jerk_v140_signal,
    f16cg_f16_cash_generation_selffund_signaccel_21d_jerk_v141_signal,
    f16cg_f16_cash_generation_selffund_raw_126d_jerk_v142_signal,
    f16cg_f16_cash_generation_selffund_z_63d_jerk_v143_signal,
    f16cg_f16_cash_generation_totcash_relsecond_63d_jerk_v144_signal,
    f16cg_f16_cash_generation_totcash_ranksecond_126d_jerk_v145_signal,
    f16cg_f16_cash_generation_totcash_ewmadiff_126d_jerk_v146_signal,
    f16cg_f16_cash_generation_totcash_signaccel_21d_jerk_v147_signal,
    f16cg_f16_cash_generation_totcash_raw_5d_jerk_v148_signal,
    f16cg_f16_cash_generation_totcash_z_21d_jerk_v149_signal,
    f16cg_f16_cash_generation_totcash_relsecond_126d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F16_CASH_GENERATION_REGISTRY_JERK_001_150 = REGISTRY


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

    assert n_features == 150, n_features
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

    print("OK f16_cash_generation_3rd_derivatives_001_150_claude: %d features pass" % n_features)
