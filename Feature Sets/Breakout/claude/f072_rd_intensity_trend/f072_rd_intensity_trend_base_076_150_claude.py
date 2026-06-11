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
def _f072_rd_ratio(rnd, revenue):
    return rnd / revenue.replace(0, np.nan).abs() * rnd


def _f072_rd_trend(rnd, revenue, w):
    ratio = rnd / revenue.replace(0, np.nan).abs()
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean() * rnd


def _f072_investment_growth(rnd, revenue, w):
    rnd_growth = rnd.pct_change(periods=w)
    rev_growth = revenue.pct_change(periods=w)
    return (rnd_growth - rev_growth) * rnd

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v076_signal(rnd, revenue, closeadj):
    result = _z(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), 5) * _z(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v077_signal(rnd, revenue, closeadj):
    result = _mean(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), 5) * _std(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v078_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v079_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()).clip(lower=-1e10, upper=1e10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v080_signal(rnd, revenue, closeadj):
    result = (_mean(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), 5) - _mean(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), max(2, 5 * 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v081_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v082_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).ewm(span=max(2, 21 * 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v083_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).ewm(span=21, adjust=False).mean() * (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).ewm(span=21, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v084_signal(rnd, revenue, closeadj):
    result = _std(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), max(2, 21 // 2)) * _mean(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v085_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v086_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v087_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.75) - (_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v088_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()).rolling(63, min_periods=max(1, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v089_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()) - _mean(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v090_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()) - _mean(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), 63)) / _std(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v091_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).rolling(126, min_periods=max(1, 126 // 2)).apply(lambda x: x[-1] - x[0], raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v092_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).shift(1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v093_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()) - (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).shift(max(1, 126 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v094_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()) + (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).shift(126)) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v095_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()) * closeadj).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v096_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()) * closeadj).rolling(252, min_periods=max(1, 252 // 2)).std()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v097_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).abs() * closeadj).rolling(max(2, 252 // 4), min_periods=max(1, 252 // 8)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v098_signal(rnd, revenue, closeadj):
    result = np.cbrt((_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean())) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v099_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).ewm(halflife=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v100_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).ewm(halflife=252, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v101_signal(rnd, revenue, closeadj):
    result = _z(_f072_rd_trend(rnd, revenue, 5), 5) * _z(_f072_rd_trend(rnd, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v102_signal(rnd, revenue, closeadj):
    result = _mean(_f072_rd_trend(rnd, revenue, 5), 5) * _std(_f072_rd_trend(rnd, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v103_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f072_rd_trend(rnd, revenue, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v104_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 5)).clip(lower=-1e10, upper=1e10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v105_signal(rnd, revenue, closeadj):
    result = (_mean(_f072_rd_trend(rnd, revenue, 5), 5) - _mean(_f072_rd_trend(rnd, revenue, 5), max(2, 5 * 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v106_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v107_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 21)).ewm(span=max(2, 21 * 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v108_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 21)).ewm(span=21, adjust=False).mean() * (_f072_rd_trend(rnd, revenue, 21)).ewm(span=21, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v109_signal(rnd, revenue, closeadj):
    result = _std(_f072_rd_trend(rnd, revenue, 21), max(2, 21 // 2)) * _mean(_f072_rd_trend(rnd, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v110_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 21)).rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v111_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v112_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.75) - (_f072_rd_trend(rnd, revenue, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v113_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 63)).rolling(63, min_periods=max(1, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v114_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 63)) - _mean(_f072_rd_trend(rnd, revenue, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v115_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 63)) - _mean(_f072_rd_trend(rnd, revenue, 63), 63)) / _std(_f072_rd_trend(rnd, revenue, 63), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v116_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).apply(lambda x: x[-1] - x[0], raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v117_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 126)).shift(1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v118_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 126)) - (_f072_rd_trend(rnd, revenue, 126)).shift(max(1, 126 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v119_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 126)) + (_f072_rd_trend(rnd, revenue, 126)).shift(126)) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v120_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 126)) * closeadj).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v121_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 252)) * closeadj).rolling(252, min_periods=max(1, 252 // 2)).std()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v122_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 252)).abs() * closeadj).rolling(max(2, 252 // 4), min_periods=max(1, 252 // 8)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v123_signal(rnd, revenue, closeadj):
    result = np.cbrt((_f072_rd_trend(rnd, revenue, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v124_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 252)).ewm(halflife=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v125_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 252)).ewm(halflife=252, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v126_signal(rnd, revenue, closeadj):
    result = _z(_f072_investment_growth(rnd, revenue, 5), 5) * _z(_f072_investment_growth(rnd, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v127_signal(rnd, revenue, closeadj):
    result = _mean(_f072_investment_growth(rnd, revenue, 5), 5) * _std(_f072_investment_growth(rnd, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v128_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 5)).rolling(5, min_periods=max(1, 5 // 2)).max() - (_f072_investment_growth(rnd, revenue, 5)).rolling(5, min_periods=max(1, 5 // 2)).min()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v129_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 5)).clip(lower=-1e10, upper=1e10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v130_signal(rnd, revenue, closeadj):
    result = (_mean(_f072_investment_growth(rnd, revenue, 5), 5) - _mean(_f072_investment_growth(rnd, revenue, 5), max(2, 5 * 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v131_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 21)).ewm(span=max(2, 21 // 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v132_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 21)).ewm(span=max(2, 21 * 2), adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v133_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 21)).ewm(span=21, adjust=False).mean() * (_f072_investment_growth(rnd, revenue, 21)).ewm(span=21, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v134_signal(rnd, revenue, closeadj):
    result = _std(_f072_investment_growth(rnd, revenue, 21), max(2, 21 // 2)) * _mean(_f072_investment_growth(rnd, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v135_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 21)).rolling(21, min_periods=max(1, 21 // 2)).quantile(0.75) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v136_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v137_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.75) - (_f072_investment_growth(rnd, revenue, 63)).rolling(63, min_periods=max(1, 63 // 2)).quantile(0.25)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v138_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 63)).rolling(63, min_periods=max(1, 63 // 2)).var() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v139_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 63)) - _mean(_f072_investment_growth(rnd, revenue, 63), 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v140_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 63)) - _mean(_f072_investment_growth(rnd, revenue, 63), 63)) / _std(_f072_investment_growth(rnd, revenue, 63), 63).replace(0, np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v141_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).apply(lambda x: x[-1] - x[0], raw=True) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v142_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 126)).shift(1)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v143_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 126)) - (_f072_investment_growth(rnd, revenue, 126)).shift(max(1, 126 // 2))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v144_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 126)) + (_f072_investment_growth(rnd, revenue, 126)).shift(126)) * 0.5 * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v145_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 126)) * closeadj).rolling(126, min_periods=max(1, 126 // 2)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v146_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 252)) * closeadj).rolling(252, min_periods=max(1, 252 // 2)).std()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v147_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 252)).abs() * closeadj).rolling(max(2, 252 // 4), min_periods=max(1, 252 // 8)).mean()
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v148_signal(rnd, revenue, closeadj):
    result = np.cbrt((_f072_investment_growth(rnd, revenue, 252))) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v149_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 252)).ewm(halflife=252, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v150_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 252)).ewm(halflife=252, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v076_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v077_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v078_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v079_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v080_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v081_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v082_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v083_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v084_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v085_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v086_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v087_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v088_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v089_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v090_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v091_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v092_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v093_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v094_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v095_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v096_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v097_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v098_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v099_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v100_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v101_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v102_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v103_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v104_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v105_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v106_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v107_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v108_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v109_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v110_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v111_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v112_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v113_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v114_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v115_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v116_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v117_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v118_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v119_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v120_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v121_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v122_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v123_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v124_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v125_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v126_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v127_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v128_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v129_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v130_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v131_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v132_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v133_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v134_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v135_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v136_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v137_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v138_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v139_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v140_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v141_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v142_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v143_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v144_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v145_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v146_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v147_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v148_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v149_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F072_RD_INTENSITY_TREND_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    rnd = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    cols = {"rnd": rnd, "revenue": revenue, "closeadj": closeadj}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f072_rd_ratio", "_f072_rd_trend", "_f072_investment_growth")
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
    print(f"OK f072_rd_intensity_trend_076_150_claude: {n_features} features pass")
