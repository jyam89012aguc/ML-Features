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

# ===== folder domain primitives =====
def _f075_gm_yoy(grossmargin, w):
    return grossmargin.diff(periods=w) * grossmargin


def _f075_gm_expansion(grossmargin, w):
    avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    return (grossmargin - avg) * grossmargin


def _f075_pricing_power(grossmargin, w):
    avg = grossmargin.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = grossmargin.rolling(w, min_periods=max(1, w // 2)).std()
    return (grossmargin - avg) / sd.replace(0, np.nan) * grossmargin

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v076_signal(grossmargin, closeadj):
    result = _z(_f075_gm_yoy(grossmargin, 5), 5) * _z(_f075_gm_yoy(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v077_signal(grossmargin, closeadj):
    result = _mean(_f075_gm_yoy(grossmargin, 5), 5) * _std(_f075_gm_yoy(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v078_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f075_gm_yoy(grossmargin, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v079_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 5)).clip(lower=-1e10, upper=1e10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v080_signal(grossmargin, closeadj):
    result = (_mean(_f075_gm_yoy(grossmargin, 5), 5) - _mean(_f075_gm_yoy(grossmargin, 5), max(2, 5 * 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v081_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v082_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 21)).ewm(span=max(2, 21 * 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v083_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 21)).ewm(span=21, adjust=False).mean() * (_f075_gm_yoy(grossmargin, 21)).ewm(span=21, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v084_signal(grossmargin, closeadj):
    result = _std(_f075_gm_yoy(grossmargin, 21), max(2, 21 // 2)) * _mean(_f075_gm_yoy(grossmargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v085_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 21)).rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v086_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v087_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.75) - (_f075_gm_yoy(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v088_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v089_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 63)) - _mean(_f075_gm_yoy(grossmargin, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v090_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 63)) - _mean(_f075_gm_yoy(grossmargin, 63), 63)) / _std(_f075_gm_yoy(grossmargin, 63), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v091_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).apply(lambda x: x[-1] - x[0], raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v092_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 126)).shift(1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v093_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 126)) - (_f075_gm_yoy(grossmargin, 126)).shift(max(1, 126 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v094_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 126)) + (_f075_gm_yoy(grossmargin, 126)).shift(126)) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v095_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 126)) * closeadj).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v096_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 252)) * closeadj).rolling(252, min_periods=max(1, 252 // 2)).std()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v097_signal(grossmargin, closeadj):
    result = ((_f075_gm_yoy(grossmargin, 252)).abs() * closeadj).rolling(max(2, 252 // 4), min_periods=max(1, 252 // 8)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v098_signal(grossmargin, closeadj):
    result = np.cbrt((_f075_gm_yoy(grossmargin, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v099_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 252)).ewm(halflife=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v100_signal(grossmargin, closeadj):
    result = (_f075_gm_yoy(grossmargin, 252)).ewm(halflife=252, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v101_signal(grossmargin, closeadj):
    result = _z(_f075_gm_expansion(grossmargin, 5), 5) * _z(_f075_gm_expansion(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v102_signal(grossmargin, closeadj):
    result = _mean(_f075_gm_expansion(grossmargin, 5), 5) * _std(_f075_gm_expansion(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v103_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f075_gm_expansion(grossmargin, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v104_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 5)).clip(lower=-1e10, upper=1e10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_5d_base_v105_signal(grossmargin, closeadj):
    result = (_mean(_f075_gm_expansion(grossmargin, 5), 5) - _mean(_f075_gm_expansion(grossmargin, 5), max(2, 5 * 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v106_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v107_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 21)).ewm(span=max(2, 21 * 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v108_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 21)).ewm(span=21, adjust=False).mean() * (_f075_gm_expansion(grossmargin, 21)).ewm(span=21, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v109_signal(grossmargin, closeadj):
    result = _std(_f075_gm_expansion(grossmargin, 21), max(2, 21 // 2)) * _mean(_f075_gm_expansion(grossmargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_21d_base_v110_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 21)).rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v111_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v112_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.75) - (_f075_gm_expansion(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v113_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v114_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 63)) - _mean(_f075_gm_expansion(grossmargin, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_63d_base_v115_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 63)) - _mean(_f075_gm_expansion(grossmargin, 63), 63)) / _std(_f075_gm_expansion(grossmargin, 63), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v116_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).apply(lambda x: x[-1] - x[0], raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v117_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 126)).shift(1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v118_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 126)) - (_f075_gm_expansion(grossmargin, 126)).shift(max(1, 126 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v119_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 126)) + (_f075_gm_expansion(grossmargin, 126)).shift(126)) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_126d_base_v120_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 126)) * closeadj).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v121_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 252)) * closeadj).rolling(252, min_periods=max(1, 252 // 2)).std()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v122_signal(grossmargin, closeadj):
    result = ((_f075_gm_expansion(grossmargin, 252)).abs() * closeadj).rolling(max(2, 252 // 4), min_periods=max(1, 252 // 8)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v123_signal(grossmargin, closeadj):
    result = np.cbrt((_f075_gm_expansion(grossmargin, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v124_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 252)).ewm(halflife=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_gmexp_252d_base_v125_signal(grossmargin, closeadj):
    result = (_f075_gm_expansion(grossmargin, 252)).ewm(halflife=252, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v126_signal(grossmargin, closeadj):
    result = _z(_f075_pricing_power(grossmargin, 5), 5) * _z(_f075_pricing_power(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v127_signal(grossmargin, closeadj):
    result = _mean(_f075_pricing_power(grossmargin, 5), 5) * _std(_f075_pricing_power(grossmargin, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v128_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f075_pricing_power(grossmargin, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v129_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 5)).clip(lower=-1e10, upper=1e10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_5d_base_v130_signal(grossmargin, closeadj):
    result = (_mean(_f075_pricing_power(grossmargin, 5), 5) - _mean(_f075_pricing_power(grossmargin, 5), max(2, 5 * 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v131_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v132_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 21)).ewm(span=max(2, 21 * 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v133_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 21)).ewm(span=21, adjust=False).mean() * (_f075_pricing_power(grossmargin, 21)).ewm(span=21, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v134_signal(grossmargin, closeadj):
    result = _std(_f075_pricing_power(grossmargin, 21), max(2, 21 // 2)) * _mean(_f075_pricing_power(grossmargin, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_21d_base_v135_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 21)).rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v136_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v137_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.75) - (_f075_pricing_power(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v138_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 63)).rolling(63, min_periods=max(1, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v139_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 63)) - _mean(_f075_pricing_power(grossmargin, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_63d_base_v140_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 63)) - _mean(_f075_pricing_power(grossmargin, 63), 63)) / _std(_f075_pricing_power(grossmargin, 63), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v141_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 126)).rolling(126, min_periods=max(1, 126 // 2)).apply(lambda x: x[-1] - x[0], raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v142_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 126)).shift(1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v143_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 126)) - (_f075_pricing_power(grossmargin, 126)).shift(max(1, 126 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v144_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 126)) + (_f075_pricing_power(grossmargin, 126)).shift(126)) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_126d_base_v145_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 126)) * closeadj).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v146_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 252)) * closeadj).rolling(252, min_periods=max(1, 252 // 2)).std()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v147_signal(grossmargin, closeadj):
    result = ((_f075_pricing_power(grossmargin, 252)).abs() * closeadj).rolling(max(2, 252 // 4), min_periods=max(1, 252 // 8)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v148_signal(grossmargin, closeadj):
    result = np.cbrt((_f075_pricing_power(grossmargin, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v149_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 252)).ewm(halflife=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f075gme_f075_gross_margin_expansion_pricepw_252d_base_v150_signal(grossmargin, closeadj):
    result = (_f075_pricing_power(grossmargin, 252)).ewm(halflife=252, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v076_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v077_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v078_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v079_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_5d_base_v080_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v081_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v082_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v083_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v084_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_21d_base_v085_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v086_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v087_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v088_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v089_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_63d_base_v090_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v091_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v092_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v093_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v094_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_126d_base_v095_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v096_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v097_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v098_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v099_signal,
    f075gme_f075_gross_margin_expansion_gmyoy_252d_base_v100_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v101_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v102_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v103_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v104_signal,
    f075gme_f075_gross_margin_expansion_gmexp_5d_base_v105_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v106_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v107_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v108_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v109_signal,
    f075gme_f075_gross_margin_expansion_gmexp_21d_base_v110_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v111_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v112_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v113_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v114_signal,
    f075gme_f075_gross_margin_expansion_gmexp_63d_base_v115_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v116_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v117_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v118_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v119_signal,
    f075gme_f075_gross_margin_expansion_gmexp_126d_base_v120_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v121_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v122_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v123_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v124_signal,
    f075gme_f075_gross_margin_expansion_gmexp_252d_base_v125_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v126_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v127_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v128_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v129_signal,
    f075gme_f075_gross_margin_expansion_pricepw_5d_base_v130_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v131_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v132_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v133_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v134_signal,
    f075gme_f075_gross_margin_expansion_pricepw_21d_base_v135_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v136_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v137_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v138_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v139_signal,
    f075gme_f075_gross_margin_expansion_pricepw_63d_base_v140_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v141_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v142_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v143_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v144_signal,
    f075gme_f075_gross_margin_expansion_pricepw_126d_base_v145_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v146_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v147_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v148_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v149_signal,
    f075gme_f075_gross_margin_expansion_pricepw_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F075_GROSS_MARGIN_EXPANSION_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    grossmargin = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    cols = {"grossmargin": grossmargin, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f075_gm_yoy", "_f075_gm_expansion", "_f075_pricing_power")
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
    print(f"OK f075_gross_margin_expansion_076_150_claude: {n_features} features pass")
