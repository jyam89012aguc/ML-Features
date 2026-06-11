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

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v001_signal(rnd, revenue, closeadj):
    result = _f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v002_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v003_signal(rnd, revenue, closeadj):
    result = np.sign(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v004_signal(rnd, revenue, closeadj):
    result = _mean(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v005_signal(rnd, revenue, closeadj):
    result = _std(_f072_rd_ratio(rnd, revenue).rolling(5, min_periods=max(1, 5 // 2)).mean(), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v006_signal(rnd, revenue, closeadj):
    result = _z(_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean(), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v007_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()) * (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v008_signal(rnd, revenue, closeadj):
    result = np.sqrt((_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v009_signal(rnd, revenue, closeadj):
    result = np.log1p((_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v010_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(21, min_periods=max(1, 21 // 2)).mean()).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v011_signal(rnd, revenue, closeadj):
    result = _mean(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v012_signal(rnd, revenue, closeadj):
    result = _std(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v013_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v014_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean()).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v015_signal(rnd, revenue, closeadj):
    result = _z(_f072_rd_ratio(rnd, revenue).rolling(63, min_periods=max(1, 63 // 2)).mean(), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v016_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v017_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v018_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v019_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v020_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(126, min_periods=max(1, 126 // 2)).mean()).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v021_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v022_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()) * (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()) * (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v023_signal(rnd, revenue, closeadj):
    result = (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v024_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()) - (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v025_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()) / (_f072_rd_ratio(rnd, revenue).rolling(252, min_periods=max(1, 252 // 2)).mean()).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v026_signal(rnd, revenue, closeadj):
    result = _f072_rd_trend(rnd, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v027_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v028_signal(rnd, revenue, closeadj):
    result = np.sign(_f072_rd_trend(rnd, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v029_signal(rnd, revenue, closeadj):
    result = _mean(_f072_rd_trend(rnd, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v030_signal(rnd, revenue, closeadj):
    result = _std(_f072_rd_trend(rnd, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v031_signal(rnd, revenue, closeadj):
    result = _z(_f072_rd_trend(rnd, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v032_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 21)) * (_f072_rd_trend(rnd, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v033_signal(rnd, revenue, closeadj):
    result = np.sqrt((_f072_rd_trend(rnd, revenue, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v034_signal(rnd, revenue, closeadj):
    result = np.log1p((_f072_rd_trend(rnd, revenue, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v035_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v036_signal(rnd, revenue, closeadj):
    result = _mean(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v037_signal(rnd, revenue, closeadj):
    result = _std(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v038_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v039_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v040_signal(rnd, revenue, closeadj):
    result = _z(_f072_rd_trend(rnd, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v041_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v042_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v043_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v044_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v045_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v046_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v047_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 252)) * (_f072_rd_trend(rnd, revenue, 252)) * (_f072_rd_trend(rnd, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v048_signal(rnd, revenue, closeadj):
    result = (_f072_rd_trend(rnd, revenue, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v049_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 252)) - (_f072_rd_trend(rnd, revenue, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v050_signal(rnd, revenue, closeadj):
    result = ((_f072_rd_trend(rnd, revenue, 252)) / (_f072_rd_trend(rnd, revenue, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v051_signal(rnd, revenue, closeadj):
    result = _f072_investment_growth(rnd, revenue, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v052_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 5)).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v053_signal(rnd, revenue, closeadj):
    result = np.sign(_f072_investment_growth(rnd, revenue, 5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v054_signal(rnd, revenue, closeadj):
    result = _mean(_f072_investment_growth(rnd, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v055_signal(rnd, revenue, closeadj):
    result = _std(_f072_investment_growth(rnd, revenue, 5), 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v056_signal(rnd, revenue, closeadj):
    result = _z(_f072_investment_growth(rnd, revenue, 21), 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v057_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 21)) * (_f072_investment_growth(rnd, revenue, 21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v058_signal(rnd, revenue, closeadj):
    result = np.sqrt((_f072_investment_growth(rnd, revenue, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v059_signal(rnd, revenue, closeadj):
    result = np.log1p((_f072_investment_growth(rnd, revenue, 21)).abs()) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v060_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 21)).diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v061_signal(rnd, revenue, closeadj):
    result = _mean(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v062_signal(rnd, revenue, closeadj):
    result = _std(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v063_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 63)).ewm(span=63, adjust=False).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v064_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 63)).ewm(span=63, adjust=False).std() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v065_signal(rnd, revenue, closeadj):
    result = _z(_f072_investment_growth(rnd, revenue, 63), max(2, 63 // 2)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v066_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).sum() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v067_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).max() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v068_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).min() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v069_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 126)).rolling(126, min_periods=max(1, 126 // 2)).median() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v070_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 126)).rolling(126, min_periods=max(2, 126 // 2)).skew() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v071_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 252)).rolling(252, min_periods=max(4, 252 // 2)).kurt() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v072_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 252)) * (_f072_investment_growth(rnd, revenue, 252)) * (_f072_investment_growth(rnd, revenue, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v073_signal(rnd, revenue, closeadj):
    result = (_f072_investment_growth(rnd, revenue, 252)).pct_change(252).replace([np.inf, -np.inf], np.nan) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v074_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 252)) - (_f072_investment_growth(rnd, revenue, 252)).shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v075_signal(rnd, revenue, closeadj):
    result = ((_f072_investment_growth(rnd, revenue, 252)) / (_f072_investment_growth(rnd, revenue, 252)).shift(252).replace(0, np.nan)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v001_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v002_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v003_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v004_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_5d_base_v005_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v006_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v007_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v008_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v009_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_21d_base_v010_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v011_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v012_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v013_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v014_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_63d_base_v015_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v016_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v017_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v018_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v019_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_126d_base_v020_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v021_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v022_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v023_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v024_signal,
    f072rdt_f072_rd_intensity_trend_rdratio_252d_base_v025_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v026_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v027_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v028_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v029_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_5d_base_v030_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v031_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v032_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v033_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v034_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_21d_base_v035_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v036_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v037_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v038_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v039_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_63d_base_v040_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v041_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v042_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v043_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v044_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_126d_base_v045_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v046_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v047_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v048_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v049_signal,
    f072rdt_f072_rd_intensity_trend_rdtrend_252d_base_v050_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v051_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v052_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v053_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v054_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_5d_base_v055_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v056_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v057_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v058_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v059_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_21d_base_v060_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v061_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v062_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v063_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v064_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_63d_base_v065_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v066_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v067_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v068_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v069_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_126d_base_v070_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v071_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v072_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v073_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v074_signal,
    f072rdt_f072_rd_intensity_trend_invgrowth_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F072_RD_INTENSITY_TREND_REGISTRY_001_075 = REGISTRY


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
    print(f"OK f072_rd_intensity_trend_001_075_claude: {n_features} features pass")
