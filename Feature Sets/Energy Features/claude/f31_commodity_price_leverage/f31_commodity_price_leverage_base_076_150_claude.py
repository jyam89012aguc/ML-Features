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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=max(2, w), adjust=False, min_periods=max(1, w // 2)).mean()

# ===== folder domain primitives =====
def _f31_revenue_sensitivity(revenue, w):
    pc = revenue.pct_change(periods=w)
    base = pc.rolling(w, min_periods=max(1, w // 2)).std()
    return base * revenue / revenue.abs().replace(0, np.nan)

def _f31_price_leverage(revenue, ebitdamargin, w):
    r = revenue.pct_change(periods=w)
    m = ebitdamargin.diff(periods=w)
    return (r * m) * 100.0

def _f31_leverage_score(revenue, w):
    m = revenue.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = revenue.rolling(w, min_periods=max(1, w // 2)).std()
    return (revenue - m) / sd.replace(0, np.nan)


def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_42d_base_v076_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_42d_base_v077_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_42d_base_v078_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xc_63d_base_v079_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_63d_base_v080_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_63d_base_v081_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_63d_base_v082_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_63d_base_v083_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_63d_base_v084_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xc_126d_base_v085_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_126d_base_v086_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_126d_base_v087_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_126d_base_v088_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_126d_base_v089_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_126d_base_v090_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xc_189d_base_v091_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_189d_base_v092_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_189d_base_v093_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_189d_base_v094_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_189d_base_v095_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_189d_base_v096_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xc_252d_base_v097_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 252)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_252d_base_v098_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 252)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_252d_base_v099_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 252)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_252d_base_v100_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 252)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_252d_base_v101_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 252)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_252d_base_v102_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 252)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xc_378d_base_v103_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 378)
    result = base.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_378d_base_v104_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 378)
    result = base.abs() * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_378d_base_v105_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 378)
    result = base.abs() * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_378d_base_v106_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 378)
    result = base.abs() * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_378d_base_v107_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 378)
    result = base.abs() * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_378d_base_v108_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 378)
    result = base.abs() * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xc_5d_base_v109_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 5)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_5d_base_v110_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 5)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_5d_base_v111_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 5)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_5d_base_v112_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 5)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_5d_base_v113_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 5)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_5d_base_v114_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 5)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xc_10d_base_v115_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 10)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_10d_base_v116_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 10)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_10d_base_v117_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 10)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_10d_base_v118_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 10)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_10d_base_v119_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 10)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_10d_base_v120_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 10)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xc_21d_base_v121_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 21)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_21d_base_v122_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 21)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_21d_base_v123_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 21)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_21d_base_v124_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 21)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_21d_base_v125_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 21)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_21d_base_v126_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 21)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xc_42d_base_v127_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_42d_base_v128_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_42d_base_v129_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_42d_base_v130_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_42d_base_v131_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_42d_base_v132_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 42)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xc_63d_base_v133_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_63d_base_v134_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_63d_base_v135_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_63d_base_v136_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_63d_base_v137_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_63d_base_v138_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 63)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xc_126d_base_v139_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_126d_base_v140_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_126d_base_v141_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_126d_base_v142_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_126d_base_v143_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_126d_base_v144_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 126)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xc_189d_base_v145_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = (base * base) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_189d_base_v146_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = (base * base) * _mean(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_189d_base_v147_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = (base * base) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_189d_base_v148_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = (base * base) * _mean(closeadj, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_189d_base_v149_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = (base * base) * _ema(closeadj, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_189d_base_v150_signal(revenue, closeadj):
    base = _f31_revenue_sensitivity(revenue, 189)
    result = (base * base) * _ema(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_42d_base_v076_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_42d_base_v077_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_42d_base_v078_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xc_63d_base_v079_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_63d_base_v080_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_63d_base_v081_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_63d_base_v082_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_63d_base_v083_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_63d_base_v084_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xc_126d_base_v085_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_126d_base_v086_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_126d_base_v087_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_126d_base_v088_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_126d_base_v089_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_126d_base_v090_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xc_189d_base_v091_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_189d_base_v092_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_189d_base_v093_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_189d_base_v094_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_189d_base_v095_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_189d_base_v096_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xc_252d_base_v097_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_252d_base_v098_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_252d_base_v099_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_252d_base_v100_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_252d_base_v101_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_252d_base_v102_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xc_378d_base_v103_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc21_378d_base_v104_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc63_378d_base_v105_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xmc252_378d_base_v106_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema21c_378d_base_v107_signal,
    f31cpl_f31_commodity_price_leverage_revsens_absv_xema63c_378d_base_v108_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xc_5d_base_v109_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_5d_base_v110_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_5d_base_v111_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_5d_base_v112_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_5d_base_v113_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_5d_base_v114_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xc_10d_base_v115_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_10d_base_v116_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_10d_base_v117_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_10d_base_v118_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_10d_base_v119_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_10d_base_v120_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xc_21d_base_v121_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_21d_base_v122_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_21d_base_v123_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_21d_base_v124_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_21d_base_v125_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_21d_base_v126_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xc_42d_base_v127_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_42d_base_v128_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_42d_base_v129_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_42d_base_v130_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_42d_base_v131_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_42d_base_v132_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xc_63d_base_v133_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_63d_base_v134_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_63d_base_v135_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_63d_base_v136_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_63d_base_v137_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_63d_base_v138_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xc_126d_base_v139_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_126d_base_v140_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_126d_base_v141_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_126d_base_v142_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_126d_base_v143_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_126d_base_v144_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xc_189d_base_v145_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc21_189d_base_v146_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc63_189d_base_v147_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xmc252_189d_base_v148_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema21c_189d_base_v149_signal,
    f31cpl_f31_commodity_price_leverage_revsens_sq_xema63c_189d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F31_COMMODITY_PRICE_LEVERAGE_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    debt    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    de = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue,
        "ebitda": ebitda,
        "netinc": netinc,
        "fcf": fcf,
        "capex": capex,
        "debt": debt,
        "ebitdamargin": ebitdamargin,
        "de": de,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f31_revenue_sensitivity", "_f31_price_leverage", "_f31_leverage_score",)
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
    print(f"OK f31_commodity_price_leverage_076_150_claude: {n_features} features pass")
