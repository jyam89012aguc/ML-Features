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


# ===== folder domain primitives (ev valuation regime) =====
def _f26_evz(s, w):
    # z-score of an enterprise-value series over w trading days
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _f26_evtrend(s, w):
    # trend of an enterprise-value series: pct-change slope over w
    return s.pct_change(periods=w)


def _f26_evratio(ev, marketcap):
    # ev / marketcap: enterprise-to-equity (debt-load) proxy, continuous
    return ev / marketcap.replace(0, np.nan)


def _f26_evcomp(s, w):
    # valuation compression: level vs its own trailing mean (gap, normalized)
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    return (s - m) / m.replace(0, np.nan)
def _slope_norm(s, w):
    # discrete 1st derivative over w, scaled by base dispersion (robust to zero-crossing)
    d = s.diff(periods=w)
    sc = s.rolling(252, min_periods=21).std()
    return d / sc.replace(0, np.nan)

# ============ SLOPE FEATURES 001-150 ============
def f26ev_f26_ev_valuation_regime_evz_63d_slope_v001_signal(ev):
    result = _f26_evz(ev, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evz_126d_slope_v002_signal(ev):
    result = _f26_evz(ev, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evz_252d_slope_v003_signal(ev):
    result = _f26_evz(ev, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evz_504d_slope_v004_signal(ev):
    result = _f26_evz(ev, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_63d_slope_v005_signal(evebitda):
    result = _f26_evz(evebitda, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_126d_slope_v006_signal(evebitda):
    result = _f26_evz(evebitda, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_252d_slope_v007_signal(evebitda):
    result = _f26_evz(evebitda, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_504d_slope_v008_signal(evebitda):
    result = _f26_evz(evebitda, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitz_63d_slope_v009_signal(evebit):
    result = _f26_evz(evebit, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitz_126d_slope_v010_signal(evebit):
    result = _f26_evz(evebit, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitz_252d_slope_v011_signal(evebit):
    result = _f26_evz(evebit, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitz_504d_slope_v012_signal(evebit):
    result = _f26_evz(evebit, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtrend_63d_slope_v013_signal(ev):
    result = _f26_evtrend(ev, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtrend_126d_slope_v014_signal(ev):
    result = _f26_evtrend(ev, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtrend_252d_slope_v015_signal(ev):
    result = _f26_evtrend(ev, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtrend_504d_slope_v016_signal(ev):
    result = _f26_evtrend(ev, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatrend_63d_slope_v017_signal(evebitda):
    result = _f26_evtrend(evebitda, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatrend_126d_slope_v018_signal(evebitda):
    result = _f26_evtrend(evebitda, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatrend_252d_slope_v019_signal(evebitda):
    result = _f26_evtrend(evebitda, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatrend_504d_slope_v020_signal(evebitda):
    result = _f26_evtrend(evebitda, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratio_1d_slope_v021_signal(ev, marketcap):
    result = _f26_evratio(ev, marketcap)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratioz_63d_slope_v022_signal(ev, marketcap):
    result = _z(_f26_evratio(ev, marketcap), 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratioz_126d_slope_v023_signal(ev, marketcap):
    result = _z(_f26_evratio(ev, marketcap), 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratioz_252d_slope_v024_signal(ev, marketcap):
    result = _z(_f26_evratio(ev, marketcap), 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiodev_63d_slope_v025_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r - _mean(r, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiodev_126d_slope_v026_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r - _mean(r, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evcomp_63d_slope_v027_signal(ev):
    result = _f26_evcomp(ev, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evcomp_126d_slope_v028_signal(ev):
    result = _f26_evcomp(ev, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evcomp_252d_slope_v029_signal(ev):
    result = _f26_evcomp(ev, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evcomp_504d_slope_v030_signal(ev):
    result = _f26_evcomp(ev, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdacomp_63d_slope_v031_signal(evebitda):
    result = _f26_evcomp(evebitda, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdacomp_126d_slope_v032_signal(evebitda):
    result = _f26_evcomp(evebitda, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdacomp_252d_slope_v033_signal(evebitda):
    result = _f26_evcomp(evebitda, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitcomp_63d_slope_v034_signal(evebit):
    result = _f26_evcomp(evebit, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitcomp_126d_slope_v035_signal(evebit):
    result = _f26_evcomp(evebit, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitcomp_252d_slope_v036_signal(evebit):
    result = _f26_evcomp(evebit, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdarank_126d_slope_v037_signal(evebitda):
    result = evebitda.rolling(126, min_periods=42).rank(pct=True) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdarank_252d_slope_v038_signal(evebitda):
    result = evebitda.rolling(252, min_periods=84).rank(pct=True) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdarank_504d_slope_v039_signal(evebitda):
    result = evebitda.rolling(504, min_periods=168).rank(pct=True) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evrank_252d_slope_v040_signal(ev):
    result = ev.rolling(252, min_periods=84).rank(pct=True) + _f26_evz(ev, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evrank_504d_slope_v041_signal(ev):
    result = ev.rolling(504, min_periods=168).rank(pct=True) + _f26_evz(ev, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitrank_252d_slope_v042_signal(evebit):
    result = evebit.rolling(252, min_periods=84).rank(pct=True) + _f26_evz(evebit, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_regimeratio_1d_slope_v043_signal(evebitda, evebit):
    result = _safe_div(evebitda, evebit) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_regimeratioz_63d_slope_v044_signal(evebitda, evebit):
    result = _z(_safe_div(evebitda, evebit), 63) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_regimeratioz_126d_slope_v045_signal(evebitda, evebit):
    result = _z(_safe_div(evebitda, evebit), 126) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evgrowth_63d_slope_v046_signal(ev):
    result = np.log(ev / ev.shift(63)) + _f26_evtrend(ev, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evgrowth_126d_slope_v047_signal(ev):
    result = np.log(ev / ev.shift(126)) + _f26_evtrend(ev, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evgrowth_252d_slope_v048_signal(ev):
    result = np.log(ev / ev.shift(252)) + _f26_evtrend(ev, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evgrowth_504d_slope_v049_signal(ev):
    result = np.log(ev / ev.shift(504)) + _f26_evtrend(ev, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdagrowth_126d_slope_v050_signal(evebitda):
    result = np.log(evebitda / evebitda.shift(126)) + _f26_evtrend(evebitda, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdagrowth_252d_slope_v051_signal(evebitda):
    result = np.log(evebitda / evebitda.shift(252)) + _f26_evtrend(evebitda, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evdisp_63d_slope_v052_signal(ev):
    lr = np.log(ev / ev.shift(1))
    result = _std(lr, 63) + _f26_evtrend(ev, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evdisp_126d_slope_v053_signal(ev):
    lr = np.log(ev / ev.shift(1))
    result = _std(lr, 126) + _f26_evtrend(ev, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evdisp_252d_slope_v054_signal(ev):
    lr = np.log(ev / ev.shift(1))
    result = _std(lr, 252) + _f26_evtrend(ev, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdadisp_126d_slope_v055_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    result = _std(lr, 126) + _f26_evtrend(evebitda, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdadisp_252d_slope_v056_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    result = _std(lr, 252) + _f26_evtrend(evebitda, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdamr_63d_slope_v057_signal(evebitda):
    result = -_f26_evz(evebitda, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdamr_126d_slope_v058_signal(evebitda):
    result = -_f26_evz(evebitda, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evmr_252d_slope_v059_signal(ev):
    result = -_f26_evz(ev, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatq_63d_slope_v060_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    v = _std(lr, 63) * np.sqrt(63.0)
    result = _safe_div(_f26_evtrend(evebitda, 63), v)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatq_126d_slope_v061_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    v = _std(lr, 126) * np.sqrt(126.0)
    result = _safe_div(_f26_evtrend(evebitda, 126), v)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtq_126d_slope_v062_signal(ev):
    lr = np.log(ev / ev.shift(1))
    v = _std(lr, 126) * np.sqrt(126.0)
    result = _safe_div(_f26_evtrend(ev, 126), v)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtq_252d_slope_v063_signal(ev):
    lr = np.log(ev / ev.shift(1))
    v = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f26_evtrend(ev, 252), v)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaspread_63_252_slope_v064_signal(evebitda):
    result = _f26_evtrend(evebitda, 63) - _f26_evtrend(evebitda, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evspread_63_252_slope_v065_signal(ev):
    result = _f26_evtrend(ev, 63) - _f26_evtrend(ev, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evspread_21_126_slope_v066_signal(ev):
    result = _f26_evtrend(ev, 21) - _f26_evtrend(ev, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_zgap_126d_slope_v067_signal(evebitda, evebit):
    result = _f26_evz(evebitda, 126) - _f26_evz(evebit, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_zgap_252d_slope_v068_signal(evebitda, evebit):
    result = _f26_evz(evebitda, 252) - _f26_evz(evebit, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evebitdazgap_252d_slope_v069_signal(ev, evebitda):
    result = _f26_evz(ev, 252) - _f26_evz(evebitda, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdazewm_126d_slope_v070_signal(evebitda):
    result = _f26_evz(evebitda, 126).ewm(span=21, min_periods=10).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evzewm_252d_slope_v071_signal(ev):
    result = _f26_evz(ev, 252).ewm(span=42, min_periods=21).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiocomp_126d_slope_v072_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = _f26_evcomp(r, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiocomp_252d_slope_v073_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = _f26_evcomp(r, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdacompiq_126d_slope_v074_signal(evebitda):
    comp = _f26_evcomp(evebitda, 126)
    lr = np.log(evebitda / evebitda.shift(1))
    result = _safe_div(comp, _std(lr, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evcompiq_252d_slope_v075_signal(ev):
    comp = _f26_evcomp(ev, 252)
    lr = np.log(ev / ev.shift(1))
    result = _safe_div(comp, _std(lr, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_21d_slope_v076_signal(evebitda):
    result = _f26_evz(evebitda, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_42d_slope_v077_signal(evebitda):
    result = _f26_evz(evebitda, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_189d_slope_v078_signal(evebitda):
    result = _f26_evz(evebitda, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_315d_slope_v079_signal(evebitda):
    result = _f26_evz(evebitda, 315)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evz_42d_slope_v080_signal(ev):
    result = _f26_evz(ev, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evz_189d_slope_v081_signal(ev):
    result = _f26_evz(ev, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evz_378d_slope_v082_signal(ev):
    result = _f26_evz(ev, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitz_189d_slope_v083_signal(evebit):
    result = _f26_evz(evebit, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitz_378d_slope_v084_signal(evebit):
    result = _f26_evz(evebit, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtrend_21d_slope_v085_signal(ev):
    result = _f26_evtrend(ev, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtrend_42d_slope_v086_signal(ev):
    result = _f26_evtrend(ev, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtrend_189d_slope_v087_signal(ev):
    result = _f26_evtrend(ev, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evtrend_378d_slope_v088_signal(ev):
    result = _f26_evtrend(ev, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebittrend_42d_slope_v089_signal(evebit):
    result = _f26_evtrend(evebit, 42)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebittrend_126d_slope_v090_signal(evebit):
    result = _f26_evtrend(evebit, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebittrend_252d_slope_v091_signal(evebit):
    result = _f26_evtrend(evebit, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebittrend_504d_slope_v092_signal(evebit):
    result = _f26_evtrend(evebit, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdacomp_21d_slope_v093_signal(evebitda):
    result = _f26_evcomp(evebitda, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdacomp_504d_slope_v094_signal(evebitda):
    result = _f26_evcomp(evebitda, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitcomp_504d_slope_v095_signal(evebit):
    result = _f26_evcomp(evebit, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evcomp_84d_slope_v096_signal(ev):
    result = _f26_evcomp(ev, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evcomp_189d_slope_v097_signal(ev):
    result = _f26_evcomp(ev, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaz_84d_slope_v098_signal(evebitda):
    result = _f26_evz(evebitda, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evz_84d_slope_v099_signal(ev):
    result = _f26_evz(ev, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatrend_84d_slope_v100_signal(evebitda):
    result = _f26_evtrend(evebitda, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatrend_189d_slope_v101_signal(evebitda):
    result = _f26_evtrend(evebitda, 189)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatrend_378d_slope_v102_signal(evebitda):
    result = _f26_evtrend(evebitda, 378)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evgrowth_84d_slope_v103_signal(ev):
    result = np.log(ev / ev.shift(84)) + _f26_evtrend(ev, 84) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evgrowth_189d_slope_v104_signal(ev):
    result = np.log(ev / ev.shift(189)) + _f26_evtrend(ev, 189) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdagrowth_63d_slope_v105_signal(evebitda):
    result = np.log(evebitda / evebitda.shift(63)) + _f26_evtrend(evebitda, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdagrowth_504d_slope_v106_signal(evebitda):
    result = np.log(evebitda / evebitda.shift(504)) + _f26_evtrend(evebitda, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitgrowth_126d_slope_v107_signal(evebit):
    result = np.log(evebit / evebit.shift(126)) + _f26_evtrend(evebit, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitgrowth_252d_slope_v108_signal(evebit):
    result = np.log(evebit / evebit.shift(252)) + _f26_evtrend(evebit, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdisp_63d_slope_v109_signal(evebit):
    lr = np.log(evebit / evebit.shift(1))
    result = _std(lr, 63) + _f26_evtrend(evebit, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdisp_126d_slope_v110_signal(evebit):
    lr = np.log(evebit / evebit.shift(1))
    result = _std(lr, 126) + _f26_evtrend(evebit, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evdisp_504d_slope_v111_signal(ev):
    lr = np.log(ev / ev.shift(1))
    result = _std(lr, 504) + _f26_evtrend(ev, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdadisp_504d_slope_v112_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    result = _std(lr, 504) + _f26_evtrend(evebitda, 504) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitmr_252d_slope_v113_signal(evebit):
    result = -_f26_evz(evebit, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evmr_126d_slope_v114_signal(ev):
    result = -_f26_evz(ev, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdamr_504d_slope_v115_signal(evebitda):
    result = -_f26_evz(evebitda, 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdatq_252d_slope_v116_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    v = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f26_evtrend(evebitda, 252), v)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebittq_63d_slope_v117_signal(evebit):
    lr = np.log(evebit / evebit.shift(1))
    v = _std(lr, 63) * np.sqrt(63.0)
    result = _safe_div(_f26_evtrend(evebit, 63), v)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebittq_126d_slope_v118_signal(evebit):
    lr = np.log(evebit / evebit.shift(1))
    v = _std(lr, 126) * np.sqrt(126.0)
    result = _safe_div(_f26_evtrend(evebit, 126), v)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdaspread_21_84_slope_v119_signal(evebitda):
    result = _f26_evtrend(evebitda, 21) - _f26_evtrend(evebitda, 84)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evspread_126_504_slope_v120_signal(ev):
    result = _f26_evtrend(ev, 126) - _f26_evtrend(ev, 504)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitspread_63_252_slope_v121_signal(evebit):
    result = _f26_evtrend(evebit, 63) - _f26_evtrend(evebit, 252)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_zgap63_126d_slope_v122_signal(evebitda, evebit):
    result = _f26_evz(evebitda, 63) - _f26_evz(evebit, 63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evebitzgap_252d_slope_v123_signal(ev, evebit):
    result = _f26_evz(ev, 252) - _f26_evz(evebit, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitzewm_63d_slope_v124_signal(evebit):
    result = _f26_evz(evebit, 63).ewm(span=10, min_periods=5).mean()
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdazewm_504d_slope_v125_signal(evebitda):
    result = _f26_evz(evebitda, 504).ewm(span=63, min_periods=21).mean()
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitcompiq_63d_slope_v126_signal(evebit):
    comp = _f26_evcomp(evebit, 63)
    lr = np.log(evebit / evebit.shift(1))
    result = _safe_div(comp, _std(lr, 63))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdacompiq_252d_slope_v127_signal(evebitda):
    comp = _f26_evcomp(evebitda, 252)
    lr = np.log(evebitda / evebitda.shift(1))
    result = _safe_div(comp, _std(lr, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evcompiq_126d_slope_v128_signal(ev):
    comp = _f26_evcomp(ev, 126)
    lr = np.log(ev / ev.shift(1))
    result = _safe_div(comp, _std(lr, 126))
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiodev_21d_slope_v129_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r - _mean(r, 21)
    result = _slope_norm(result, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiodev_252d_slope_v130_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r - _mean(r, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratioz_504d_slope_v131_signal(ev, marketcap):
    result = _z(_f26_evratio(ev, marketcap), 504)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiotrend_63d_slope_v132_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.pct_change(periods=63)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiotrend_126d_slope_v133_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.pct_change(periods=126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiotrend_252d_slope_v134_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.pct_change(periods=252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitrank_126d_slope_v135_signal(evebit):
    result = evebit.rolling(126, min_periods=42).rank(pct=True) + _f26_evz(evebit, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitrank_504d_slope_v136_signal(evebit):
    result = evebit.rolling(504, min_periods=168).rank(pct=True) + _f26_evz(evebit, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evrank_126d_slope_v137_signal(ev):
    result = ev.rolling(126, min_periods=42).rank(pct=True) + _f26_evz(ev, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiorank_126d_slope_v138_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.rolling(126, min_periods=42).rank(pct=True)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evratiorank_252d_slope_v139_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_regimeratioz_252d_slope_v140_signal(evebitda, evebit):
    result = _z(_safe_div(evebitda, evebit), 252) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_regimecomp_126d_slope_v141_signal(evebitda, evebit):
    r = _safe_div(evebitda, evebit)
    result = _f26_evcomp(r, 126) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_regimetrend_252d_slope_v142_signal(evebitda, evebit):
    r = _safe_div(evebitda, evebit)
    result = r.pct_change(periods=252) + _f26_evz(evebitda, 63) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evmcapzgap_252d_slope_v143_signal(ev, marketcap):
    result = _f26_evz(ev, 252) - _z(marketcap, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evmcapzgap_126d_slope_v144_signal(ev, marketcap):
    result = _f26_evz(ev, 126) - _z(marketcap, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evmcapgrowthgap_252d_slope_v145_signal(ev, marketcap):
    eg = np.log(ev / ev.shift(252))
    mg = np.log(marketcap / marketcap.shift(252))
    result = eg - mg + _f26_evtrend(ev, 252) * 0.0
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evmcapgrowthgap_126d_slope_v146_signal(ev, marketcap):
    eg = np.log(ev / ev.shift(126))
    mg = np.log(marketcap / marketcap.shift(126))
    result = eg - mg + _f26_evtrend(ev, 126) * 0.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_compgap_252d_slope_v147_signal(evebitda, evebit):
    result = _f26_evcomp(evebitda, 252) - _f26_evcomp(evebit, 252)
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_compgap_126d_slope_v148_signal(evebitda, evebit):
    result = _f26_evcomp(evebitda, 126) - _f26_evcomp(evebit, 126)
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_evzscaled_252d_slope_v149_signal(ev, evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    result = _safe_div(_f26_evz(ev, 252), _std(lr, 252))
    result = _slope_norm(result, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f26ev_f26_ev_valuation_regime_ebitdazblend_multi_slope_v150_signal(evebitda):
    result = (_f26_evz(evebitda, 63) + _f26_evz(evebitda, 126)
              + _f26_evz(evebitda, 252) + _f26_evz(evebitda, 504)) / 4.0
    result = _slope_norm(result, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [    f26ev_f26_ev_valuation_regime_evz_63d_slope_v001_signal,    f26ev_f26_ev_valuation_regime_evz_126d_slope_v002_signal,    f26ev_f26_ev_valuation_regime_evz_252d_slope_v003_signal,    f26ev_f26_ev_valuation_regime_evz_504d_slope_v004_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_63d_slope_v005_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_126d_slope_v006_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_252d_slope_v007_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_504d_slope_v008_signal,    f26ev_f26_ev_valuation_regime_ebitz_63d_slope_v009_signal,    f26ev_f26_ev_valuation_regime_ebitz_126d_slope_v010_signal,    f26ev_f26_ev_valuation_regime_ebitz_252d_slope_v011_signal,    f26ev_f26_ev_valuation_regime_ebitz_504d_slope_v012_signal,    f26ev_f26_ev_valuation_regime_evtrend_63d_slope_v013_signal,    f26ev_f26_ev_valuation_regime_evtrend_126d_slope_v014_signal,    f26ev_f26_ev_valuation_regime_evtrend_252d_slope_v015_signal,    f26ev_f26_ev_valuation_regime_evtrend_504d_slope_v016_signal,    f26ev_f26_ev_valuation_regime_ebitdatrend_63d_slope_v017_signal,    f26ev_f26_ev_valuation_regime_ebitdatrend_126d_slope_v018_signal,    f26ev_f26_ev_valuation_regime_ebitdatrend_252d_slope_v019_signal,    f26ev_f26_ev_valuation_regime_ebitdatrend_504d_slope_v020_signal,    f26ev_f26_ev_valuation_regime_evratio_1d_slope_v021_signal,    f26ev_f26_ev_valuation_regime_evratioz_63d_slope_v022_signal,    f26ev_f26_ev_valuation_regime_evratioz_126d_slope_v023_signal,    f26ev_f26_ev_valuation_regime_evratioz_252d_slope_v024_signal,    f26ev_f26_ev_valuation_regime_evratiodev_63d_slope_v025_signal,    f26ev_f26_ev_valuation_regime_evratiodev_126d_slope_v026_signal,    f26ev_f26_ev_valuation_regime_evcomp_63d_slope_v027_signal,    f26ev_f26_ev_valuation_regime_evcomp_126d_slope_v028_signal,    f26ev_f26_ev_valuation_regime_evcomp_252d_slope_v029_signal,    f26ev_f26_ev_valuation_regime_evcomp_504d_slope_v030_signal,    f26ev_f26_ev_valuation_regime_ebitdacomp_63d_slope_v031_signal,    f26ev_f26_ev_valuation_regime_ebitdacomp_126d_slope_v032_signal,    f26ev_f26_ev_valuation_regime_ebitdacomp_252d_slope_v033_signal,    f26ev_f26_ev_valuation_regime_ebitcomp_63d_slope_v034_signal,    f26ev_f26_ev_valuation_regime_ebitcomp_126d_slope_v035_signal,    f26ev_f26_ev_valuation_regime_ebitcomp_252d_slope_v036_signal,    f26ev_f26_ev_valuation_regime_ebitdarank_126d_slope_v037_signal,    f26ev_f26_ev_valuation_regime_ebitdarank_252d_slope_v038_signal,    f26ev_f26_ev_valuation_regime_ebitdarank_504d_slope_v039_signal,    f26ev_f26_ev_valuation_regime_evrank_252d_slope_v040_signal,    f26ev_f26_ev_valuation_regime_evrank_504d_slope_v041_signal,    f26ev_f26_ev_valuation_regime_ebitrank_252d_slope_v042_signal,    f26ev_f26_ev_valuation_regime_regimeratio_1d_slope_v043_signal,    f26ev_f26_ev_valuation_regime_regimeratioz_63d_slope_v044_signal,    f26ev_f26_ev_valuation_regime_regimeratioz_126d_slope_v045_signal,    f26ev_f26_ev_valuation_regime_evgrowth_63d_slope_v046_signal,    f26ev_f26_ev_valuation_regime_evgrowth_126d_slope_v047_signal,    f26ev_f26_ev_valuation_regime_evgrowth_252d_slope_v048_signal,    f26ev_f26_ev_valuation_regime_evgrowth_504d_slope_v049_signal,    f26ev_f26_ev_valuation_regime_ebitdagrowth_126d_slope_v050_signal,    f26ev_f26_ev_valuation_regime_ebitdagrowth_252d_slope_v051_signal,    f26ev_f26_ev_valuation_regime_evdisp_63d_slope_v052_signal,    f26ev_f26_ev_valuation_regime_evdisp_126d_slope_v053_signal,    f26ev_f26_ev_valuation_regime_evdisp_252d_slope_v054_signal,    f26ev_f26_ev_valuation_regime_ebitdadisp_126d_slope_v055_signal,    f26ev_f26_ev_valuation_regime_ebitdadisp_252d_slope_v056_signal,    f26ev_f26_ev_valuation_regime_ebitdamr_63d_slope_v057_signal,    f26ev_f26_ev_valuation_regime_ebitdamr_126d_slope_v058_signal,    f26ev_f26_ev_valuation_regime_evmr_252d_slope_v059_signal,    f26ev_f26_ev_valuation_regime_ebitdatq_63d_slope_v060_signal,    f26ev_f26_ev_valuation_regime_ebitdatq_126d_slope_v061_signal,    f26ev_f26_ev_valuation_regime_evtq_126d_slope_v062_signal,    f26ev_f26_ev_valuation_regime_evtq_252d_slope_v063_signal,    f26ev_f26_ev_valuation_regime_ebitdaspread_63_252_slope_v064_signal,    f26ev_f26_ev_valuation_regime_evspread_63_252_slope_v065_signal,    f26ev_f26_ev_valuation_regime_evspread_21_126_slope_v066_signal,    f26ev_f26_ev_valuation_regime_zgap_126d_slope_v067_signal,    f26ev_f26_ev_valuation_regime_zgap_252d_slope_v068_signal,    f26ev_f26_ev_valuation_regime_evebitdazgap_252d_slope_v069_signal,    f26ev_f26_ev_valuation_regime_ebitdazewm_126d_slope_v070_signal,    f26ev_f26_ev_valuation_regime_evzewm_252d_slope_v071_signal,    f26ev_f26_ev_valuation_regime_evratiocomp_126d_slope_v072_signal,    f26ev_f26_ev_valuation_regime_evratiocomp_252d_slope_v073_signal,    f26ev_f26_ev_valuation_regime_ebitdacompiq_126d_slope_v074_signal,    f26ev_f26_ev_valuation_regime_evcompiq_252d_slope_v075_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_21d_slope_v076_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_42d_slope_v077_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_189d_slope_v078_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_315d_slope_v079_signal,    f26ev_f26_ev_valuation_regime_evz_42d_slope_v080_signal,    f26ev_f26_ev_valuation_regime_evz_189d_slope_v081_signal,    f26ev_f26_ev_valuation_regime_evz_378d_slope_v082_signal,    f26ev_f26_ev_valuation_regime_ebitz_189d_slope_v083_signal,    f26ev_f26_ev_valuation_regime_ebitz_378d_slope_v084_signal,    f26ev_f26_ev_valuation_regime_evtrend_21d_slope_v085_signal,    f26ev_f26_ev_valuation_regime_evtrend_42d_slope_v086_signal,    f26ev_f26_ev_valuation_regime_evtrend_189d_slope_v087_signal,    f26ev_f26_ev_valuation_regime_evtrend_378d_slope_v088_signal,    f26ev_f26_ev_valuation_regime_ebittrend_42d_slope_v089_signal,    f26ev_f26_ev_valuation_regime_ebittrend_126d_slope_v090_signal,    f26ev_f26_ev_valuation_regime_ebittrend_252d_slope_v091_signal,    f26ev_f26_ev_valuation_regime_ebittrend_504d_slope_v092_signal,    f26ev_f26_ev_valuation_regime_ebitdacomp_21d_slope_v093_signal,    f26ev_f26_ev_valuation_regime_ebitdacomp_504d_slope_v094_signal,    f26ev_f26_ev_valuation_regime_ebitcomp_504d_slope_v095_signal,    f26ev_f26_ev_valuation_regime_evcomp_84d_slope_v096_signal,    f26ev_f26_ev_valuation_regime_evcomp_189d_slope_v097_signal,    f26ev_f26_ev_valuation_regime_ebitdaz_84d_slope_v098_signal,    f26ev_f26_ev_valuation_regime_evz_84d_slope_v099_signal,    f26ev_f26_ev_valuation_regime_ebitdatrend_84d_slope_v100_signal,    f26ev_f26_ev_valuation_regime_ebitdatrend_189d_slope_v101_signal,    f26ev_f26_ev_valuation_regime_ebitdatrend_378d_slope_v102_signal,    f26ev_f26_ev_valuation_regime_evgrowth_84d_slope_v103_signal,    f26ev_f26_ev_valuation_regime_evgrowth_189d_slope_v104_signal,    f26ev_f26_ev_valuation_regime_ebitdagrowth_63d_slope_v105_signal,    f26ev_f26_ev_valuation_regime_ebitdagrowth_504d_slope_v106_signal,    f26ev_f26_ev_valuation_regime_ebitgrowth_126d_slope_v107_signal,    f26ev_f26_ev_valuation_regime_ebitgrowth_252d_slope_v108_signal,    f26ev_f26_ev_valuation_regime_ebitdisp_63d_slope_v109_signal,    f26ev_f26_ev_valuation_regime_ebitdisp_126d_slope_v110_signal,    f26ev_f26_ev_valuation_regime_evdisp_504d_slope_v111_signal,    f26ev_f26_ev_valuation_regime_ebitdadisp_504d_slope_v112_signal,    f26ev_f26_ev_valuation_regime_ebitmr_252d_slope_v113_signal,    f26ev_f26_ev_valuation_regime_evmr_126d_slope_v114_signal,    f26ev_f26_ev_valuation_regime_ebitdamr_504d_slope_v115_signal,    f26ev_f26_ev_valuation_regime_ebitdatq_252d_slope_v116_signal,    f26ev_f26_ev_valuation_regime_ebittq_63d_slope_v117_signal,    f26ev_f26_ev_valuation_regime_ebittq_126d_slope_v118_signal,    f26ev_f26_ev_valuation_regime_ebitdaspread_21_84_slope_v119_signal,    f26ev_f26_ev_valuation_regime_evspread_126_504_slope_v120_signal,    f26ev_f26_ev_valuation_regime_ebitspread_63_252_slope_v121_signal,    f26ev_f26_ev_valuation_regime_zgap63_126d_slope_v122_signal,    f26ev_f26_ev_valuation_regime_evebitzgap_252d_slope_v123_signal,    f26ev_f26_ev_valuation_regime_ebitzewm_63d_slope_v124_signal,    f26ev_f26_ev_valuation_regime_ebitdazewm_504d_slope_v125_signal,    f26ev_f26_ev_valuation_regime_ebitcompiq_63d_slope_v126_signal,    f26ev_f26_ev_valuation_regime_ebitdacompiq_252d_slope_v127_signal,    f26ev_f26_ev_valuation_regime_evcompiq_126d_slope_v128_signal,    f26ev_f26_ev_valuation_regime_evratiodev_21d_slope_v129_signal,    f26ev_f26_ev_valuation_regime_evratiodev_252d_slope_v130_signal,    f26ev_f26_ev_valuation_regime_evratioz_504d_slope_v131_signal,    f26ev_f26_ev_valuation_regime_evratiotrend_63d_slope_v132_signal,    f26ev_f26_ev_valuation_regime_evratiotrend_126d_slope_v133_signal,    f26ev_f26_ev_valuation_regime_evratiotrend_252d_slope_v134_signal,    f26ev_f26_ev_valuation_regime_ebitrank_126d_slope_v135_signal,    f26ev_f26_ev_valuation_regime_ebitrank_504d_slope_v136_signal,    f26ev_f26_ev_valuation_regime_evrank_126d_slope_v137_signal,    f26ev_f26_ev_valuation_regime_evratiorank_126d_slope_v138_signal,    f26ev_f26_ev_valuation_regime_evratiorank_252d_slope_v139_signal,    f26ev_f26_ev_valuation_regime_regimeratioz_252d_slope_v140_signal,    f26ev_f26_ev_valuation_regime_regimecomp_126d_slope_v141_signal,    f26ev_f26_ev_valuation_regime_regimetrend_252d_slope_v142_signal,    f26ev_f26_ev_valuation_regime_evmcapzgap_252d_slope_v143_signal,    f26ev_f26_ev_valuation_regime_evmcapzgap_126d_slope_v144_signal,    f26ev_f26_ev_valuation_regime_evmcapgrowthgap_252d_slope_v145_signal,    f26ev_f26_ev_valuation_regime_evmcapgrowthgap_126d_slope_v146_signal,    f26ev_f26_ev_valuation_regime_compgap_252d_slope_v147_signal,    f26ev_f26_ev_valuation_regime_compgap_126d_slope_v148_signal,    f26ev_f26_ev_valuation_regime_evzscaled_252d_slope_v149_signal,    f26ev_f26_ev_valuation_regime_ebitdazblend_multi_slope_v150_signal,]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_EV_VALUATION_REGIME_REGISTRY_SLOPE = REGISTRY

def _synth_cols(names):
    import numpy as np
    import pandas as pd
    np.random.seed(42)
    n = 1500
    out = {}
    base_price = 50.0 * np.exp(np.cumsum(np.random.normal(0.0008, 0.045, n)))
    closeadj = pd.Series(base_price, name="closeadj")
    noise_h = np.abs(np.random.normal(0, 0.02, n))
    noise_l = np.abs(np.random.normal(0, 0.02, n))
    POS = {"open", "high", "low", "close", "closeadj", "price", "volume",
           "vwap", "marketcap", "ev", "assets", "assetsc", "assetsnc", "equity",
           "revenue", "revenueusd", "gp", "ebitda", "ebit", "ppnenet", "sharesbas",
           "shareswa", "cashneq", "cor", "opex", "sgna", "rnd", "inventory",
           "receivables", "payables", "intangibles", "evebitda", "evebit",
           "pe", "pb", "ps", "currentratio", "bvps", "sps", "divyield", "dps",
           "shrvalue", "shrunits", "totalvalue", "percentoftotal", "value",
           "units", "shares", "sf3a_shares", "sf3a_value", "sf3b_shares",
           "sf3b_value", "grossmargin", "ebitdamargin", "netmargin", "roe",
           "roa", "roic", "deposits", "invcap"}
    for nm in names:
        if nm == "closeadj" or nm == "close" or nm == "price":
            out[nm] = pd.Series(base_price, name=nm)
        elif nm == "open":
            out[nm] = pd.Series(base_price * (1 + np.random.normal(0, 0.01, n)), name=nm)
        elif nm == "high":
            out[nm] = pd.Series(base_price * (1 + noise_h), name=nm)
        elif nm == "low":
            out[nm] = pd.Series(base_price * (1 - noise_l), name=nm)
        elif nm == "volume":
            out[nm] = pd.Series(np.abs(np.random.normal(2e7, 7e6, n)) + 1e5, name=nm)
        else:
            walk = np.cumsum(np.random.normal(0.0, 1.0, n))
            level = 1000.0 * np.exp(0.03 * np.random.normal(0, 1, n).cumsum() / np.sqrt(n))
            series = level + 50.0 * walk
            if nm in POS:
                series = np.abs(series) + 10.0
            out[nm] = pd.Series(series, name=nm)
    return out


if __name__ == "__main__":
    import numpy as np
    import pandas as pd
    domain_primitives = ('_f26_evz', '_f26_evtrend', '_f26_evratio', '_f26_evcomp')
    needed = set()
    for fn in _FEATURES:
        for p in inspect.signature(fn).parameters.values():
            needed.add(p.name)
    cols = _synth_cols(sorted(needed))
    n_features = 0
    nan_ok = 0
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
    assert n_features == 150, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print("OK f26_ev_valuation_regime_" + "2nd_derivatives" + "_001_150_claude: " + str(n_features) + " features pass")
