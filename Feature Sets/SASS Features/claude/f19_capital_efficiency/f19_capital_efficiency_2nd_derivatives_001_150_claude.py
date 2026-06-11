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


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _roc(s, w):
    return s - s.shift(w)


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


def _jerk(s, w):
    return (s - 2.0 * s.shift(w) + s.shift(2 * w)) / float(w * w)


# ===== folder domain primitives (capital efficiency / turnover levels) =====
def _f19_asset_turn(revenue, assets):
    return revenue / assets.replace(0, np.nan)


def _f19_invcap_turn(revenue, invcap):
    return revenue / invcap.replace(0, np.nan)


def _f19_fixed_turn(revenue, ppnenet):
    return revenue / ppnenet.replace(0, np.nan)


def _f19_equity_turn(revenue, equity):
    return revenue / equity.replace(0, np.nan)


def _f19_capint(ppnenet, assets):
    return ppnenet / assets.replace(0, np.nan)


# ========================================================
# slope (1st deriv) of base aturn under raw norm, ROC 5d
def f19ce_f19_capital_efficiency_aturnraw_21d_slope_v001_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    b = bq
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under z252 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnz252_252d_slope_v002_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under rank504 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnrank504_504d_slope_v003_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under relmed252 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnrelmed252_252d_slope_v004_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under emadisp126 norm, ROC 5d
def f19ce_f19_capital_efficiency_aturnemadisp126_126d_slope_v005_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under pos252 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnpos252_252d_slope_v006_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under z126 norm, ROC 5d
def f19ce_f19_capital_efficiency_aturnz126_126d_slope_v007_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under rank252 norm, ROC 5d
def f19ce_f19_capital_efficiency_aturnrank252_252d_slope_v008_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under relmed126 norm, ROC 5d
def f19ce_f19_capital_efficiency_aturnrelmed126_126d_slope_v009_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturn under emadisp63 norm, ROC 5d
def f19ce_f19_capital_efficiency_aturnemadisp63_63d_slope_v010_signal(revenue, assets):
    bq = revenue / assets.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under raw norm, ROC 21d
def f19ce_f19_capital_efficiency_icturnraw_21d_slope_v011_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    b = bq
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under z252 norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnz252_252d_slope_v012_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under rank504 norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnrank504_504d_slope_v013_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under relmed252 norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnrelmed252_252d_slope_v014_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under emadisp126 norm, ROC 21d
def f19ce_f19_capital_efficiency_icturnemadisp126_126d_slope_v015_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under pos252 norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnpos252_252d_slope_v016_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under z126 norm, ROC 21d
def f19ce_f19_capital_efficiency_icturnz126_126d_slope_v017_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under rank252 norm, ROC 21d
def f19ce_f19_capital_efficiency_icturnrank252_252d_slope_v018_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under relmed126 norm, ROC 21d
def f19ce_f19_capital_efficiency_icturnrelmed126_126d_slope_v019_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturn under emadisp63 norm, ROC 21d
def f19ce_f19_capital_efficiency_icturnemadisp63_63d_slope_v020_signal(revenue, invcap):
    bq = revenue / invcap.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under raw norm, ROC 63d
def f19ce_f19_capital_efficiency_fturnraw_21d_slope_v021_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    b = bq
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under z252 norm, ROC 126d
def f19ce_f19_capital_efficiency_fturnz252_252d_slope_v022_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under rank504 norm, ROC 126d
def f19ce_f19_capital_efficiency_fturnrank504_504d_slope_v023_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under relmed252 norm, ROC 126d
def f19ce_f19_capital_efficiency_fturnrelmed252_252d_slope_v024_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under emadisp126 norm, ROC 63d
def f19ce_f19_capital_efficiency_fturnemadisp126_126d_slope_v025_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under pos252 norm, ROC 126d
def f19ce_f19_capital_efficiency_fturnpos252_252d_slope_v026_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under z126 norm, ROC 63d
def f19ce_f19_capital_efficiency_fturnz126_126d_slope_v027_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under rank252 norm, ROC 63d
def f19ce_f19_capital_efficiency_fturnrank252_252d_slope_v028_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under relmed126 norm, ROC 63d
def f19ce_f19_capital_efficiency_fturnrelmed126_126d_slope_v029_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fturn under emadisp63 norm, ROC 42d
def f19ce_f19_capital_efficiency_fturnemadisp63_63d_slope_v030_signal(revenue, ppnenet):
    bq = revenue / ppnenet.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under raw norm, ROC 5d
def f19ce_f19_capital_efficiency_eturnraw_21d_slope_v031_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    b = bq
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under z252 norm, ROC 21d
def f19ce_f19_capital_efficiency_eturnz252_252d_slope_v032_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under rank504 norm, ROC 21d
def f19ce_f19_capital_efficiency_eturnrank504_504d_slope_v033_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under relmed252 norm, ROC 21d
def f19ce_f19_capital_efficiency_eturnrelmed252_252d_slope_v034_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under emadisp126 norm, ROC 5d
def f19ce_f19_capital_efficiency_eturnemadisp126_126d_slope_v035_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under pos252 norm, ROC 21d
def f19ce_f19_capital_efficiency_eturnpos252_252d_slope_v036_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under z126 norm, ROC 5d
def f19ce_f19_capital_efficiency_eturnz126_126d_slope_v037_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under rank252 norm, ROC 5d
def f19ce_f19_capital_efficiency_eturnrank252_252d_slope_v038_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under relmed126 norm, ROC 5d
def f19ce_f19_capital_efficiency_eturnrelmed126_126d_slope_v039_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eturn under emadisp63 norm, ROC 5d
def f19ce_f19_capital_efficiency_eturnemadisp63_63d_slope_v040_signal(revenue, equity):
    bq = revenue / equity.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under raw norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnavgraw_21d_slope_v041_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    b = bq
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under z252 norm, ROC 63d
def f19ce_f19_capital_efficiency_aturnavgz252_252d_slope_v042_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under rank504 norm, ROC 63d
def f19ce_f19_capital_efficiency_aturnavgrank504_504d_slope_v043_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under relmed252 norm, ROC 63d
def f19ce_f19_capital_efficiency_aturnavgrelmed252_252d_slope_v044_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under emadisp126 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnavgemadisp126_126d_slope_v045_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under pos252 norm, ROC 63d
def f19ce_f19_capital_efficiency_aturnavgpos252_252d_slope_v046_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under z126 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnavgz126_126d_slope_v047_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under rank252 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnavgrank252_252d_slope_v048_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under relmed126 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnavgrelmed126_126d_slope_v049_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aturnavg under emadisp63 norm, ROC 21d
def f19ce_f19_capital_efficiency_aturnavgemadisp63_63d_slope_v050_signal(revenue, assetsavg):
    bq = revenue / assetsavg.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under raw norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnavgraw_21d_slope_v051_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    b = bq
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under z252 norm, ROC 126d
def f19ce_f19_capital_efficiency_icturnavgz252_252d_slope_v052_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under rank504 norm, ROC 126d
def f19ce_f19_capital_efficiency_icturnavgrank504_504d_slope_v053_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under relmed252 norm, ROC 126d
def f19ce_f19_capital_efficiency_icturnavgrelmed252_252d_slope_v054_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under emadisp126 norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnavgemadisp126_126d_slope_v055_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under pos252 norm, ROC 126d
def f19ce_f19_capital_efficiency_icturnavgpos252_252d_slope_v056_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under z126 norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnavgz126_126d_slope_v057_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under rank252 norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnavgrank252_252d_slope_v058_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under relmed126 norm, ROC 63d
def f19ce_f19_capital_efficiency_icturnavgrelmed126_126d_slope_v059_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icturnavg under emadisp63 norm, ROC 42d
def f19ce_f19_capital_efficiency_icturnavgemadisp63_63d_slope_v060_signal(revenue, invcapavg):
    bq = revenue / invcapavg.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under raw norm, ROC 5d
def f19ce_f19_capital_efficiency_capintraw_21d_slope_v061_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    b = bq
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under z252 norm, ROC 21d
def f19ce_f19_capital_efficiency_capintz252_252d_slope_v062_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under rank504 norm, ROC 21d
def f19ce_f19_capital_efficiency_capintrank504_504d_slope_v063_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under relmed252 norm, ROC 21d
def f19ce_f19_capital_efficiency_capintrelmed252_252d_slope_v064_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under emadisp126 norm, ROC 5d
def f19ce_f19_capital_efficiency_capintemadisp126_126d_slope_v065_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under pos252 norm, ROC 21d
def f19ce_f19_capital_efficiency_capintpos252_252d_slope_v066_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under z126 norm, ROC 5d
def f19ce_f19_capital_efficiency_capintz126_126d_slope_v067_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under rank252 norm, ROC 5d
def f19ce_f19_capital_efficiency_capintrank252_252d_slope_v068_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under relmed126 norm, ROC 5d
def f19ce_f19_capital_efficiency_capintrelmed126_126d_slope_v069_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base capint under emadisp63 norm, ROC 5d
def f19ce_f19_capital_efficiency_capintemadisp63_63d_slope_v070_signal(ppnenet, assets):
    bq = ppnenet / assets.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under raw norm, ROC 21d
def f19ce_f19_capital_efficiency_icshareraw_21d_slope_v071_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    b = bq
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under z252 norm, ROC 63d
def f19ce_f19_capital_efficiency_icsharez252_252d_slope_v072_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under rank504 norm, ROC 63d
def f19ce_f19_capital_efficiency_icsharerank504_504d_slope_v073_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under relmed252 norm, ROC 63d
def f19ce_f19_capital_efficiency_icsharerelmed252_252d_slope_v074_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under emadisp126 norm, ROC 21d
def f19ce_f19_capital_efficiency_icshareemadisp126_126d_slope_v075_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under pos252 norm, ROC 63d
def f19ce_f19_capital_efficiency_icsharepos252_252d_slope_v076_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under z126 norm, ROC 21d
def f19ce_f19_capital_efficiency_icsharez126_126d_slope_v077_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under rank252 norm, ROC 21d
def f19ce_f19_capital_efficiency_icsharerank252_252d_slope_v078_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under relmed126 norm, ROC 21d
def f19ce_f19_capital_efficiency_icsharerelmed126_126d_slope_v079_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icshare under emadisp63 norm, ROC 21d
def f19ce_f19_capital_efficiency_icshareemadisp63_63d_slope_v080_signal(invcap, assets):
    bq = invcap / assets.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under raw norm, ROC 63d
def f19ce_f19_capital_efficiency_levraw_21d_slope_v081_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    b = bq
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under z252 norm, ROC 126d
def f19ce_f19_capital_efficiency_levz252_252d_slope_v082_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under rank504 norm, ROC 126d
def f19ce_f19_capital_efficiency_levrank504_504d_slope_v083_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under relmed252 norm, ROC 126d
def f19ce_f19_capital_efficiency_levrelmed252_252d_slope_v084_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under emadisp126 norm, ROC 63d
def f19ce_f19_capital_efficiency_levemadisp126_126d_slope_v085_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under pos252 norm, ROC 126d
def f19ce_f19_capital_efficiency_levpos252_252d_slope_v086_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under z126 norm, ROC 63d
def f19ce_f19_capital_efficiency_levz126_126d_slope_v087_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under rank252 norm, ROC 63d
def f19ce_f19_capital_efficiency_levrank252_252d_slope_v088_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under relmed126 norm, ROC 63d
def f19ce_f19_capital_efficiency_levrelmed126_126d_slope_v089_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base lev under emadisp63 norm, ROC 42d
def f19ce_f19_capital_efficiency_levemadisp63_63d_slope_v090_signal(assets, equity):
    bq = assets / equity.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under raw norm, ROC 5d
def f19ce_f19_capital_efficiency_eqicraw_21d_slope_v091_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    b = bq
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under z252 norm, ROC 21d
def f19ce_f19_capital_efficiency_eqicz252_252d_slope_v092_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under rank504 norm, ROC 21d
def f19ce_f19_capital_efficiency_eqicrank504_504d_slope_v093_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under relmed252 norm, ROC 21d
def f19ce_f19_capital_efficiency_eqicrelmed252_252d_slope_v094_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under emadisp126 norm, ROC 5d
def f19ce_f19_capital_efficiency_eqicemadisp126_126d_slope_v095_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under pos252 norm, ROC 21d
def f19ce_f19_capital_efficiency_eqicpos252_252d_slope_v096_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under z126 norm, ROC 5d
def f19ce_f19_capital_efficiency_eqicz126_126d_slope_v097_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under rank252 norm, ROC 5d
def f19ce_f19_capital_efficiency_eqicrank252_252d_slope_v098_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under relmed126 norm, ROC 5d
def f19ce_f19_capital_efficiency_eqicrelmed126_126d_slope_v099_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base eqic under emadisp63 norm, ROC 5d
def f19ce_f19_capital_efficiency_eqicemadisp63_63d_slope_v100_signal(equity, invcap):
    bq = equity / invcap.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under raw norm, ROC 21d
def f19ce_f19_capital_efficiency_aicsprraw_21d_slope_v101_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    b = bq
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under z252 norm, ROC 63d
def f19ce_f19_capital_efficiency_aicsprz252_252d_slope_v102_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under rank504 norm, ROC 63d
def f19ce_f19_capital_efficiency_aicsprrank504_504d_slope_v103_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under relmed252 norm, ROC 63d
def f19ce_f19_capital_efficiency_aicsprrelmed252_252d_slope_v104_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under emadisp126 norm, ROC 5d
def f19ce_f19_capital_efficiency_aicspremadisp126_126d_slope_v105_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under pos252 norm, ROC 63d
def f19ce_f19_capital_efficiency_aicsprpos252_252d_slope_v106_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under z126 norm, ROC 21d
def f19ce_f19_capital_efficiency_aicsprz126_126d_slope_v107_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under rank252 norm, ROC 21d
def f19ce_f19_capital_efficiency_aicsprrank252_252d_slope_v108_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under relmed126 norm, ROC 21d
def f19ce_f19_capital_efficiency_aicsprrelmed126_126d_slope_v109_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base aicspr under emadisp63 norm, ROC 5d
def f19ce_f19_capital_efficiency_aicspremadisp63_63d_slope_v110_signal(revenue, assets, invcap):
    bq = revenue / assets.replace(0, np.nan) - revenue / invcap.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under raw norm, ROC 63d
def f19ce_f19_capital_efficiency_fesprraw_21d_slope_v111_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    b = bq
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under z252 norm, ROC 126d
def f19ce_f19_capital_efficiency_fesprz252_252d_slope_v112_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under rank504 norm, ROC 126d
def f19ce_f19_capital_efficiency_fesprrank504_504d_slope_v113_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under relmed252 norm, ROC 126d
def f19ce_f19_capital_efficiency_fesprrelmed252_252d_slope_v114_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under emadisp126 norm, ROC 63d
def f19ce_f19_capital_efficiency_fespremadisp126_126d_slope_v115_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under pos252 norm, ROC 126d
def f19ce_f19_capital_efficiency_fesprpos252_252d_slope_v116_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under z126 norm, ROC 63d
def f19ce_f19_capital_efficiency_fesprz126_126d_slope_v117_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under rank252 norm, ROC 63d
def f19ce_f19_capital_efficiency_fesprrank252_252d_slope_v118_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under relmed126 norm, ROC 63d
def f19ce_f19_capital_efficiency_fesprrelmed126_126d_slope_v119_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base fespr under emadisp63 norm, ROC 42d
def f19ce_f19_capital_efficiency_fespremadisp63_63d_slope_v120_signal(revenue, ppnenet, equity):
    bq = revenue / ppnenet.replace(0, np.nan) - revenue / equity.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under raw norm, ROC 5d
def f19ce_f19_capital_efficiency_easprraw_21d_slope_v121_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    b = bq
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under z252 norm, ROC 21d
def f19ce_f19_capital_efficiency_easprz252_252d_slope_v122_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under rank504 norm, ROC 21d
def f19ce_f19_capital_efficiency_easprrank504_504d_slope_v123_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under relmed252 norm, ROC 21d
def f19ce_f19_capital_efficiency_easprrelmed252_252d_slope_v124_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under emadisp126 norm, ROC 5d
def f19ce_f19_capital_efficiency_easpremadisp126_126d_slope_v125_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under pos252 norm, ROC 21d
def f19ce_f19_capital_efficiency_easprpos252_252d_slope_v126_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under z126 norm, ROC 5d
def f19ce_f19_capital_efficiency_easprz126_126d_slope_v127_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under rank252 norm, ROC 5d
def f19ce_f19_capital_efficiency_easprrank252_252d_slope_v128_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under relmed126 norm, ROC 5d
def f19ce_f19_capital_efficiency_easprrelmed126_126d_slope_v129_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base easpr under emadisp63 norm, ROC 5d
def f19ce_f19_capital_efficiency_easpremadisp63_63d_slope_v130_signal(revenue, equity, assets):
    bq = revenue / equity.replace(0, np.nan) - revenue / assets.replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under raw norm, ROC 5d
def f19ce_f19_capital_efficiency_icaratioraw_21d_slope_v131_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    b = bq
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under z252 norm, ROC 5d
def f19ce_f19_capital_efficiency_icaratioz252_252d_slope_v132_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    b = _z(bq, 252)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under rank504 norm, ROC 5d
def f19ce_f19_capital_efficiency_icaratiorank504_504d_slope_v133_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    b = _rank(bq, 504)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under relmed252 norm, ROC 5d
def f19ce_f19_capital_efficiency_icaratiorelmed252_252d_slope_v134_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under emadisp126 norm, ROC 42d
def f19ce_f19_capital_efficiency_icaratioemadisp126_126d_slope_v135_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under pos252 norm, ROC 5d
def f19ce_f19_capital_efficiency_icaratiopos252_252d_slope_v136_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under z126 norm, ROC 5d
def f19ce_f19_capital_efficiency_icaratioz126_126d_slope_v137_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    b = _z(bq, 126)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under rank252 norm, ROC 5d
def f19ce_f19_capital_efficiency_icaratiorank252_252d_slope_v138_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    b = _rank(bq, 252)
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under relmed126 norm, ROC 5d
def f19ce_f19_capital_efficiency_icaratiorelmed126_126d_slope_v139_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 5)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base icaratio under emadisp63 norm, ROC 42d
def f19ce_f19_capital_efficiency_icaratioemadisp63_63d_slope_v140_signal(revenue, invcap, assets):
    bq = (revenue / invcap.replace(0, np.nan)) / (revenue / assets.replace(0, np.nan)).replace(0, np.nan)
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under raw norm, ROC 63d
def f19ce_f19_capital_efficiency_harmafraw_21d_slope_v141_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    b = bq
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under z252 norm, ROC 126d
def f19ce_f19_capital_efficiency_harmafz252_252d_slope_v142_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    b = _z(bq, 252)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under rank504 norm, ROC 126d
def f19ce_f19_capital_efficiency_harmafrank504_504d_slope_v143_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    b = _rank(bq, 504)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under relmed252 norm, ROC 126d
def f19ce_f19_capital_efficiency_harmafrelmed252_252d_slope_v144_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    _med = bq.rolling(252, min_periods=max(1, 252 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under emadisp126 norm, ROC 63d
def f19ce_f19_capital_efficiency_harmafemadisp126_126d_slope_v145_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    b = bq - bq.ewm(span=126, min_periods=max(2, 126 // 3)).mean()
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under pos252 norm, ROC 126d
def f19ce_f19_capital_efficiency_harmafpos252_252d_slope_v146_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    _hi = bq.rolling(252, min_periods=max(1, 252 // 2)).max()
    _lo = bq.rolling(252, min_periods=max(1, 252 // 2)).min()
    b = (bq - _lo) / (_hi - _lo).replace(0, np.nan)
    d = _slope(b, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under z126 norm, ROC 63d
def f19ce_f19_capital_efficiency_harmafz126_126d_slope_v147_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    b = _z(bq, 126)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under rank252 norm, ROC 63d
def f19ce_f19_capital_efficiency_harmafrank252_252d_slope_v148_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    b = _rank(bq, 252)
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under relmed126 norm, ROC 63d
def f19ce_f19_capital_efficiency_harmafrelmed126_126d_slope_v149_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    _med = bq.rolling(126, min_periods=max(1, 126 // 2)).median()
    b = bq / _med.replace(0, np.nan) - 1.0
    d = _slope(b, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (1st deriv) of base harmaf under emadisp63 norm, ROC 42d
def f19ce_f19_capital_efficiency_harmafemadisp63_63d_slope_v150_signal(revenue, assets, ppnenet):
    _a = revenue / assets.replace(0, np.nan)
    _f = revenue / ppnenet.replace(0, np.nan)
    bq = 2.0 / (1.0 / _a.replace(0, np.nan) + 1.0 / _f.replace(0, np.nan))
    b = bq - bq.ewm(span=63, min_periods=max(2, 63 // 3)).mean()
    d = _slope(b, 42)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f19ce_f19_capital_efficiency_aturnraw_21d_slope_v001_signal,
    f19ce_f19_capital_efficiency_aturnz252_252d_slope_v002_signal,
    f19ce_f19_capital_efficiency_aturnrank504_504d_slope_v003_signal,
    f19ce_f19_capital_efficiency_aturnrelmed252_252d_slope_v004_signal,
    f19ce_f19_capital_efficiency_aturnemadisp126_126d_slope_v005_signal,
    f19ce_f19_capital_efficiency_aturnpos252_252d_slope_v006_signal,
    f19ce_f19_capital_efficiency_aturnz126_126d_slope_v007_signal,
    f19ce_f19_capital_efficiency_aturnrank252_252d_slope_v008_signal,
    f19ce_f19_capital_efficiency_aturnrelmed126_126d_slope_v009_signal,
    f19ce_f19_capital_efficiency_aturnemadisp63_63d_slope_v010_signal,
    f19ce_f19_capital_efficiency_icturnraw_21d_slope_v011_signal,
    f19ce_f19_capital_efficiency_icturnz252_252d_slope_v012_signal,
    f19ce_f19_capital_efficiency_icturnrank504_504d_slope_v013_signal,
    f19ce_f19_capital_efficiency_icturnrelmed252_252d_slope_v014_signal,
    f19ce_f19_capital_efficiency_icturnemadisp126_126d_slope_v015_signal,
    f19ce_f19_capital_efficiency_icturnpos252_252d_slope_v016_signal,
    f19ce_f19_capital_efficiency_icturnz126_126d_slope_v017_signal,
    f19ce_f19_capital_efficiency_icturnrank252_252d_slope_v018_signal,
    f19ce_f19_capital_efficiency_icturnrelmed126_126d_slope_v019_signal,
    f19ce_f19_capital_efficiency_icturnemadisp63_63d_slope_v020_signal,
    f19ce_f19_capital_efficiency_fturnraw_21d_slope_v021_signal,
    f19ce_f19_capital_efficiency_fturnz252_252d_slope_v022_signal,
    f19ce_f19_capital_efficiency_fturnrank504_504d_slope_v023_signal,
    f19ce_f19_capital_efficiency_fturnrelmed252_252d_slope_v024_signal,
    f19ce_f19_capital_efficiency_fturnemadisp126_126d_slope_v025_signal,
    f19ce_f19_capital_efficiency_fturnpos252_252d_slope_v026_signal,
    f19ce_f19_capital_efficiency_fturnz126_126d_slope_v027_signal,
    f19ce_f19_capital_efficiency_fturnrank252_252d_slope_v028_signal,
    f19ce_f19_capital_efficiency_fturnrelmed126_126d_slope_v029_signal,
    f19ce_f19_capital_efficiency_fturnemadisp63_63d_slope_v030_signal,
    f19ce_f19_capital_efficiency_eturnraw_21d_slope_v031_signal,
    f19ce_f19_capital_efficiency_eturnz252_252d_slope_v032_signal,
    f19ce_f19_capital_efficiency_eturnrank504_504d_slope_v033_signal,
    f19ce_f19_capital_efficiency_eturnrelmed252_252d_slope_v034_signal,
    f19ce_f19_capital_efficiency_eturnemadisp126_126d_slope_v035_signal,
    f19ce_f19_capital_efficiency_eturnpos252_252d_slope_v036_signal,
    f19ce_f19_capital_efficiency_eturnz126_126d_slope_v037_signal,
    f19ce_f19_capital_efficiency_eturnrank252_252d_slope_v038_signal,
    f19ce_f19_capital_efficiency_eturnrelmed126_126d_slope_v039_signal,
    f19ce_f19_capital_efficiency_eturnemadisp63_63d_slope_v040_signal,
    f19ce_f19_capital_efficiency_aturnavgraw_21d_slope_v041_signal,
    f19ce_f19_capital_efficiency_aturnavgz252_252d_slope_v042_signal,
    f19ce_f19_capital_efficiency_aturnavgrank504_504d_slope_v043_signal,
    f19ce_f19_capital_efficiency_aturnavgrelmed252_252d_slope_v044_signal,
    f19ce_f19_capital_efficiency_aturnavgemadisp126_126d_slope_v045_signal,
    f19ce_f19_capital_efficiency_aturnavgpos252_252d_slope_v046_signal,
    f19ce_f19_capital_efficiency_aturnavgz126_126d_slope_v047_signal,
    f19ce_f19_capital_efficiency_aturnavgrank252_252d_slope_v048_signal,
    f19ce_f19_capital_efficiency_aturnavgrelmed126_126d_slope_v049_signal,
    f19ce_f19_capital_efficiency_aturnavgemadisp63_63d_slope_v050_signal,
    f19ce_f19_capital_efficiency_icturnavgraw_21d_slope_v051_signal,
    f19ce_f19_capital_efficiency_icturnavgz252_252d_slope_v052_signal,
    f19ce_f19_capital_efficiency_icturnavgrank504_504d_slope_v053_signal,
    f19ce_f19_capital_efficiency_icturnavgrelmed252_252d_slope_v054_signal,
    f19ce_f19_capital_efficiency_icturnavgemadisp126_126d_slope_v055_signal,
    f19ce_f19_capital_efficiency_icturnavgpos252_252d_slope_v056_signal,
    f19ce_f19_capital_efficiency_icturnavgz126_126d_slope_v057_signal,
    f19ce_f19_capital_efficiency_icturnavgrank252_252d_slope_v058_signal,
    f19ce_f19_capital_efficiency_icturnavgrelmed126_126d_slope_v059_signal,
    f19ce_f19_capital_efficiency_icturnavgemadisp63_63d_slope_v060_signal,
    f19ce_f19_capital_efficiency_capintraw_21d_slope_v061_signal,
    f19ce_f19_capital_efficiency_capintz252_252d_slope_v062_signal,
    f19ce_f19_capital_efficiency_capintrank504_504d_slope_v063_signal,
    f19ce_f19_capital_efficiency_capintrelmed252_252d_slope_v064_signal,
    f19ce_f19_capital_efficiency_capintemadisp126_126d_slope_v065_signal,
    f19ce_f19_capital_efficiency_capintpos252_252d_slope_v066_signal,
    f19ce_f19_capital_efficiency_capintz126_126d_slope_v067_signal,
    f19ce_f19_capital_efficiency_capintrank252_252d_slope_v068_signal,
    f19ce_f19_capital_efficiency_capintrelmed126_126d_slope_v069_signal,
    f19ce_f19_capital_efficiency_capintemadisp63_63d_slope_v070_signal,
    f19ce_f19_capital_efficiency_icshareraw_21d_slope_v071_signal,
    f19ce_f19_capital_efficiency_icsharez252_252d_slope_v072_signal,
    f19ce_f19_capital_efficiency_icsharerank504_504d_slope_v073_signal,
    f19ce_f19_capital_efficiency_icsharerelmed252_252d_slope_v074_signal,
    f19ce_f19_capital_efficiency_icshareemadisp126_126d_slope_v075_signal,
    f19ce_f19_capital_efficiency_icsharepos252_252d_slope_v076_signal,
    f19ce_f19_capital_efficiency_icsharez126_126d_slope_v077_signal,
    f19ce_f19_capital_efficiency_icsharerank252_252d_slope_v078_signal,
    f19ce_f19_capital_efficiency_icsharerelmed126_126d_slope_v079_signal,
    f19ce_f19_capital_efficiency_icshareemadisp63_63d_slope_v080_signal,
    f19ce_f19_capital_efficiency_levraw_21d_slope_v081_signal,
    f19ce_f19_capital_efficiency_levz252_252d_slope_v082_signal,
    f19ce_f19_capital_efficiency_levrank504_504d_slope_v083_signal,
    f19ce_f19_capital_efficiency_levrelmed252_252d_slope_v084_signal,
    f19ce_f19_capital_efficiency_levemadisp126_126d_slope_v085_signal,
    f19ce_f19_capital_efficiency_levpos252_252d_slope_v086_signal,
    f19ce_f19_capital_efficiency_levz126_126d_slope_v087_signal,
    f19ce_f19_capital_efficiency_levrank252_252d_slope_v088_signal,
    f19ce_f19_capital_efficiency_levrelmed126_126d_slope_v089_signal,
    f19ce_f19_capital_efficiency_levemadisp63_63d_slope_v090_signal,
    f19ce_f19_capital_efficiency_eqicraw_21d_slope_v091_signal,
    f19ce_f19_capital_efficiency_eqicz252_252d_slope_v092_signal,
    f19ce_f19_capital_efficiency_eqicrank504_504d_slope_v093_signal,
    f19ce_f19_capital_efficiency_eqicrelmed252_252d_slope_v094_signal,
    f19ce_f19_capital_efficiency_eqicemadisp126_126d_slope_v095_signal,
    f19ce_f19_capital_efficiency_eqicpos252_252d_slope_v096_signal,
    f19ce_f19_capital_efficiency_eqicz126_126d_slope_v097_signal,
    f19ce_f19_capital_efficiency_eqicrank252_252d_slope_v098_signal,
    f19ce_f19_capital_efficiency_eqicrelmed126_126d_slope_v099_signal,
    f19ce_f19_capital_efficiency_eqicemadisp63_63d_slope_v100_signal,
    f19ce_f19_capital_efficiency_aicsprraw_21d_slope_v101_signal,
    f19ce_f19_capital_efficiency_aicsprz252_252d_slope_v102_signal,
    f19ce_f19_capital_efficiency_aicsprrank504_504d_slope_v103_signal,
    f19ce_f19_capital_efficiency_aicsprrelmed252_252d_slope_v104_signal,
    f19ce_f19_capital_efficiency_aicspremadisp126_126d_slope_v105_signal,
    f19ce_f19_capital_efficiency_aicsprpos252_252d_slope_v106_signal,
    f19ce_f19_capital_efficiency_aicsprz126_126d_slope_v107_signal,
    f19ce_f19_capital_efficiency_aicsprrank252_252d_slope_v108_signal,
    f19ce_f19_capital_efficiency_aicsprrelmed126_126d_slope_v109_signal,
    f19ce_f19_capital_efficiency_aicspremadisp63_63d_slope_v110_signal,
    f19ce_f19_capital_efficiency_fesprraw_21d_slope_v111_signal,
    f19ce_f19_capital_efficiency_fesprz252_252d_slope_v112_signal,
    f19ce_f19_capital_efficiency_fesprrank504_504d_slope_v113_signal,
    f19ce_f19_capital_efficiency_fesprrelmed252_252d_slope_v114_signal,
    f19ce_f19_capital_efficiency_fespremadisp126_126d_slope_v115_signal,
    f19ce_f19_capital_efficiency_fesprpos252_252d_slope_v116_signal,
    f19ce_f19_capital_efficiency_fesprz126_126d_slope_v117_signal,
    f19ce_f19_capital_efficiency_fesprrank252_252d_slope_v118_signal,
    f19ce_f19_capital_efficiency_fesprrelmed126_126d_slope_v119_signal,
    f19ce_f19_capital_efficiency_fespremadisp63_63d_slope_v120_signal,
    f19ce_f19_capital_efficiency_easprraw_21d_slope_v121_signal,
    f19ce_f19_capital_efficiency_easprz252_252d_slope_v122_signal,
    f19ce_f19_capital_efficiency_easprrank504_504d_slope_v123_signal,
    f19ce_f19_capital_efficiency_easprrelmed252_252d_slope_v124_signal,
    f19ce_f19_capital_efficiency_easpremadisp126_126d_slope_v125_signal,
    f19ce_f19_capital_efficiency_easprpos252_252d_slope_v126_signal,
    f19ce_f19_capital_efficiency_easprz126_126d_slope_v127_signal,
    f19ce_f19_capital_efficiency_easprrank252_252d_slope_v128_signal,
    f19ce_f19_capital_efficiency_easprrelmed126_126d_slope_v129_signal,
    f19ce_f19_capital_efficiency_easpremadisp63_63d_slope_v130_signal,
    f19ce_f19_capital_efficiency_icaratioraw_21d_slope_v131_signal,
    f19ce_f19_capital_efficiency_icaratioz252_252d_slope_v132_signal,
    f19ce_f19_capital_efficiency_icaratiorank504_504d_slope_v133_signal,
    f19ce_f19_capital_efficiency_icaratiorelmed252_252d_slope_v134_signal,
    f19ce_f19_capital_efficiency_icaratioemadisp126_126d_slope_v135_signal,
    f19ce_f19_capital_efficiency_icaratiopos252_252d_slope_v136_signal,
    f19ce_f19_capital_efficiency_icaratioz126_126d_slope_v137_signal,
    f19ce_f19_capital_efficiency_icaratiorank252_252d_slope_v138_signal,
    f19ce_f19_capital_efficiency_icaratiorelmed126_126d_slope_v139_signal,
    f19ce_f19_capital_efficiency_icaratioemadisp63_63d_slope_v140_signal,
    f19ce_f19_capital_efficiency_harmafraw_21d_slope_v141_signal,
    f19ce_f19_capital_efficiency_harmafz252_252d_slope_v142_signal,
    f19ce_f19_capital_efficiency_harmafrank504_504d_slope_v143_signal,
    f19ce_f19_capital_efficiency_harmafrelmed252_252d_slope_v144_signal,
    f19ce_f19_capital_efficiency_harmafemadisp126_126d_slope_v145_signal,
    f19ce_f19_capital_efficiency_harmafpos252_252d_slope_v146_signal,
    f19ce_f19_capital_efficiency_harmafz126_126d_slope_v147_signal,
    f19ce_f19_capital_efficiency_harmafrank252_252d_slope_v148_signal,
    f19ce_f19_capital_efficiency_harmafrelmed126_126d_slope_v149_signal,
    f19ce_f19_capital_efficiency_harmafemadisp63_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F19_CAPITAL_EFFICIENCY_REGISTRY_2ND_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
    n = 1500
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    revenue = _fund(1, base=5e8, drift=0.03, vol=0.06).rename("revenue")
    assets = _fund(2, base=2e9, drift=0.02, vol=0.04).rename("assets")
    assetsavg = _fund(3, base=2e9, drift=0.02, vol=0.04).rename("assetsavg")
    invcap = _fund(4, base=1.2e9, drift=0.02, vol=0.05).rename("invcap")
    invcapavg = _fund(5, base=1.2e9, drift=0.02, vol=0.05).rename("invcapavg")
    equity = _fund(6, base=8e8, drift=0.02, vol=0.05).rename("equity")
    ppnenet = _fund(7, base=6e8, drift=0.015, vol=0.05).rename("ppnenet")

    cols = {"revenue": revenue, "assets": assets, "assetsavg": assetsavg,
            "invcap": invcap, "invcapavg": invcapavg, "equity": equity,
            "ppnenet": ppnenet}

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
        assert q.nunique() > 50, "NUNIQUE %s=%d" % (name, q.nunique())
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

    print("OK f19_capital_efficiency_2nd_derivatives_001_150_claude: %d features pass" % n_features)
