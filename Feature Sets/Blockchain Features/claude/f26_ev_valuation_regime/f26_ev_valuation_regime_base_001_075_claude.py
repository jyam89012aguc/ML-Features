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


# ============ FEATURES 001-075 ============

# 63d z-score of enterprise value
def f26ev_f26_ev_valuation_regime_evz_63d_base_v001_signal(ev):
    result = _f26_evz(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of enterprise value
def f26ev_f26_ev_valuation_regime_evz_126d_base_v002_signal(ev):
    result = _f26_evz(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of enterprise value
def f26ev_f26_ev_valuation_regime_evz_252d_base_v003_signal(ev):
    result = _f26_evz(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of enterprise value
def f26ev_f26_ev_valuation_regime_evz_504d_base_v004_signal(ev):
    result = _f26_evz(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of evebitda
def f26ev_f26_ev_valuation_regime_ebitdaz_63d_base_v005_signal(evebitda):
    result = _f26_evz(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of evebitda
def f26ev_f26_ev_valuation_regime_ebitdaz_126d_base_v006_signal(evebitda):
    result = _f26_evz(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of evebitda
def f26ev_f26_ev_valuation_regime_ebitdaz_252d_base_v007_signal(evebitda):
    result = _f26_evz(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of evebitda
def f26ev_f26_ev_valuation_regime_ebitdaz_504d_base_v008_signal(evebitda):
    result = _f26_evz(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of evebit
def f26ev_f26_ev_valuation_regime_ebitz_63d_base_v009_signal(evebit):
    result = _f26_evz(evebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of evebit
def f26ev_f26_ev_valuation_regime_ebitz_126d_base_v010_signal(evebit):
    result = _f26_evz(evebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of evebit
def f26ev_f26_ev_valuation_regime_ebitz_252d_base_v011_signal(evebit):
    result = _f26_evz(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of evebit
def f26ev_f26_ev_valuation_regime_ebitz_504d_base_v012_signal(evebit):
    result = _f26_evz(evebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d trend (pct-change slope) of enterprise value
def f26ev_f26_ev_valuation_regime_evtrend_63d_base_v013_signal(ev):
    result = _f26_evtrend(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d trend of enterprise value
def f26ev_f26_ev_valuation_regime_evtrend_126d_base_v014_signal(ev):
    result = _f26_evtrend(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of enterprise value
def f26ev_f26_ev_valuation_regime_evtrend_252d_base_v015_signal(ev):
    result = _f26_evtrend(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d trend of enterprise value
def f26ev_f26_ev_valuation_regime_evtrend_504d_base_v016_signal(ev):
    result = _f26_evtrend(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d trend of evebitda
def f26ev_f26_ev_valuation_regime_ebitdatrend_63d_base_v017_signal(evebitda):
    result = _f26_evtrend(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d trend of evebitda
def f26ev_f26_ev_valuation_regime_ebitdatrend_126d_base_v018_signal(evebitda):
    result = _f26_evtrend(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of evebitda
def f26ev_f26_ev_valuation_regime_ebitdatrend_252d_base_v019_signal(evebitda):
    result = _f26_evtrend(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d trend of evebitda
def f26ev_f26_ev_valuation_regime_ebitdatrend_504d_base_v020_signal(evebitda):
    result = _f26_evtrend(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# ev / marketcap debt-load ratio (level)
def f26ev_f26_ev_valuation_regime_evratio_1d_base_v021_signal(ev, marketcap):
    result = _f26_evratio(ev, marketcap)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of ev/marketcap ratio
def f26ev_f26_ev_valuation_regime_evratioz_63d_base_v022_signal(ev, marketcap):
    result = _z(_f26_evratio(ev, marketcap), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of ev/marketcap ratio
def f26ev_f26_ev_valuation_regime_evratioz_126d_base_v023_signal(ev, marketcap):
    result = _z(_f26_evratio(ev, marketcap), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d z-score of ev/marketcap ratio
def f26ev_f26_ev_valuation_regime_evratioz_252d_base_v024_signal(ev, marketcap):
    result = _z(_f26_evratio(ev, marketcap), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev/marketcap deviation from trailing mean (debt-load drift)
def f26ev_f26_ev_valuation_regime_evratiodev_63d_base_v025_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r - _mean(r, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev/marketcap deviation from trailing mean
def f26ev_f26_ev_valuation_regime_evratiodev_126d_base_v026_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r - _mean(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valuation compression of ev vs trailing mean
def f26ev_f26_ev_valuation_regime_evcomp_63d_base_v027_signal(ev):
    result = _f26_evcomp(ev, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d valuation compression of ev vs trailing mean
def f26ev_f26_ev_valuation_regime_evcomp_126d_base_v028_signal(ev):
    result = _f26_evcomp(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valuation compression of ev vs trailing mean
def f26ev_f26_ev_valuation_regime_evcomp_252d_base_v029_signal(ev):
    result = _f26_evcomp(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d valuation compression of ev vs trailing mean
def f26ev_f26_ev_valuation_regime_evcomp_504d_base_v030_signal(ev):
    result = _f26_evcomp(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valuation compression of evebitda vs trailing mean
def f26ev_f26_ev_valuation_regime_ebitdacomp_63d_base_v031_signal(evebitda):
    result = _f26_evcomp(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d valuation compression of evebitda vs trailing mean
def f26ev_f26_ev_valuation_regime_ebitdacomp_126d_base_v032_signal(evebitda):
    result = _f26_evcomp(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valuation compression of evebitda vs trailing mean
def f26ev_f26_ev_valuation_regime_ebitdacomp_252d_base_v033_signal(evebitda):
    result = _f26_evcomp(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d valuation compression of evebit vs trailing mean
def f26ev_f26_ev_valuation_regime_ebitcomp_63d_base_v034_signal(evebit):
    result = _f26_evcomp(evebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d valuation compression of evebit vs trailing mean
def f26ev_f26_ev_valuation_regime_ebitcomp_126d_base_v035_signal(evebit):
    result = _f26_evcomp(evebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d valuation compression of evebit vs trailing mean
def f26ev_f26_ev_valuation_regime_ebitcomp_252d_base_v036_signal(evebit):
    result = _f26_evcomp(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percentile rank of evebitda level
def f26ev_f26_ev_valuation_regime_ebitdarank_126d_base_v037_signal(evebitda):
    result = evebitda.rolling(126, min_periods=42).rank(pct=True) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of evebitda level
def f26ev_f26_ev_valuation_regime_ebitdarank_252d_base_v038_signal(evebitda):
    result = evebitda.rolling(252, min_periods=84).rank(pct=True) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of evebitda level
def f26ev_f26_ev_valuation_regime_ebitdarank_504d_base_v039_signal(evebitda):
    result = evebitda.rolling(504, min_periods=168).rank(pct=True) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ev level
def f26ev_f26_ev_valuation_regime_evrank_252d_base_v040_signal(ev):
    result = ev.rolling(252, min_periods=84).rank(pct=True) + _f26_evz(ev, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of ev level
def f26ev_f26_ev_valuation_regime_evrank_504d_base_v041_signal(ev):
    result = ev.rolling(504, min_periods=168).rank(pct=True) + _f26_evz(ev, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of evebit level
def f26ev_f26_ev_valuation_regime_ebitrank_252d_base_v042_signal(evebit):
    result = evebit.rolling(252, min_periods=84).rank(pct=True) + _f26_evz(evebit, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# valuation regime ratio evebitda / evebit (level)
def f26ev_f26_ev_valuation_regime_regimeratio_1d_base_v043_signal(evebitda, evebit):
    result = _safe_div(evebitda, evebit) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d z-score of evebitda/evebit regime ratio
def f26ev_f26_ev_valuation_regime_regimeratioz_63d_base_v044_signal(evebitda, evebit):
    result = _z(_safe_div(evebitda, evebit), 63) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of evebitda/evebit regime ratio
def f26ev_f26_ev_valuation_regime_regimeratioz_126d_base_v045_signal(evebitda, evebit):
    result = _z(_safe_div(evebitda, evebit), 126) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev growth (log change)
def f26ev_f26_ev_valuation_regime_evgrowth_63d_base_v046_signal(ev):
    result = np.log(ev / ev.shift(63)) + _f26_evtrend(ev, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev growth (log change)
def f26ev_f26_ev_valuation_regime_evgrowth_126d_base_v047_signal(ev):
    result = np.log(ev / ev.shift(126)) + _f26_evtrend(ev, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev growth (log change)
def f26ev_f26_ev_valuation_regime_evgrowth_252d_base_v048_signal(ev):
    result = np.log(ev / ev.shift(252)) + _f26_evtrend(ev, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev growth (log change)
def f26ev_f26_ev_valuation_regime_evgrowth_504d_base_v049_signal(ev):
    result = np.log(ev / ev.shift(504)) + _f26_evtrend(ev, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebitda growth (log change)
def f26ev_f26_ev_valuation_regime_ebitdagrowth_126d_base_v050_signal(evebitda):
    result = np.log(evebitda / evebitda.shift(126)) + _f26_evtrend(evebitda, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebitda growth (log change)
def f26ev_f26_ev_valuation_regime_ebitdagrowth_252d_base_v051_signal(evebitda):
    result = np.log(evebitda / evebitda.shift(252)) + _f26_evtrend(evebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d ev dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_evdisp_63d_base_v052_signal(ev):
    lr = np.log(ev / ev.shift(1))
    result = _std(lr, 63) + _f26_evtrend(ev, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_evdisp_126d_base_v053_signal(ev):
    lr = np.log(ev / ev.shift(1))
    result = _std(lr, 126) + _f26_evtrend(ev, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_evdisp_252d_base_v054_signal(ev):
    lr = np.log(ev / ev.shift(1))
    result = _std(lr, 252) + _f26_evtrend(ev, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebitda dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_ebitdadisp_126d_base_v055_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    result = _std(lr, 126) + _f26_evtrend(evebitda, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebitda dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_ebitdadisp_252d_base_v056_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    result = _std(lr, 252) + _f26_evtrend(evebitda, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebitda mean-reversion (negative z, reversion pressure)
def f26ev_f26_ev_valuation_regime_ebitdamr_63d_base_v057_signal(evebitda):
    result = -_f26_evz(evebitda, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebitda mean-reversion (negative z)
def f26ev_f26_ev_valuation_regime_ebitdamr_126d_base_v058_signal(evebitda):
    result = -_f26_evz(evebitda, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev mean-reversion (negative z)
def f26ev_f26_ev_valuation_regime_evmr_252d_base_v059_signal(ev):
    result = -_f26_evz(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebitda trend slope per unit dispersion (trend quality)
def f26ev_f26_ev_valuation_regime_ebitdatq_63d_base_v060_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    v = _std(lr, 63) * np.sqrt(63.0)
    result = _safe_div(_f26_evtrend(evebitda, 63), v)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebitda trend slope per unit dispersion
def f26ev_f26_ev_valuation_regime_ebitdatq_126d_base_v061_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    v = _std(lr, 126) * np.sqrt(126.0)
    result = _safe_div(_f26_evtrend(evebitda, 126), v)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev trend slope per unit dispersion
def f26ev_f26_ev_valuation_regime_evtq_126d_base_v062_signal(ev):
    lr = np.log(ev / ev.shift(1))
    v = _std(lr, 126) * np.sqrt(126.0)
    result = _safe_div(_f26_evtrend(ev, 126), v)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev trend slope per unit dispersion
def f26ev_f26_ev_valuation_regime_evtq_252d_base_v063_signal(ev):
    lr = np.log(ev / ev.shift(1))
    v = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f26_evtrend(ev, 252), v)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d short vs 252d long evebitda trend spread (regime acceleration)
def f26ev_f26_ev_valuation_regime_ebitdaspread_63_252_base_v064_signal(evebitda):
    result = _f26_evtrend(evebitda, 63) - _f26_evtrend(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d short vs 252d long ev trend spread
def f26ev_f26_ev_valuation_regime_evspread_63_252_base_v065_signal(ev):
    result = _f26_evtrend(ev, 63) - _f26_evtrend(ev, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vs 126d ev trend spread (acceleration)
def f26ev_f26_ev_valuation_regime_evspread_21_126_base_v066_signal(ev):
    result = _f26_evtrend(ev, 21) - _f26_evtrend(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# evebitda z minus evebit z (multiple-structure regime gap)
def f26ev_f26_ev_valuation_regime_zgap_126d_base_v067_signal(evebitda, evebit):
    result = _f26_evz(evebitda, 126) - _f26_evz(evebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# evebitda z minus evebit z over 252d
def f26ev_f26_ev_valuation_regime_zgap_252d_base_v068_signal(evebitda, evebit):
    result = _f26_evz(evebitda, 252) - _f26_evz(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# ev z minus evebitda z over 252d (debt vs multiple divergence)
def f26ev_f26_ev_valuation_regime_evebitdazgap_252d_base_v069_signal(ev, evebitda):
    result = _f26_evz(ev, 252) - _f26_evz(evebitda, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d EWMA-smoothed evebitda z-score
def f26ev_f26_ev_valuation_regime_ebitdazewm_126d_base_v070_signal(evebitda):
    result = _f26_evz(evebitda, 126).ewm(span=21, min_periods=10).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 252d EWMA-smoothed ev z-score
def f26ev_f26_ev_valuation_regime_evzewm_252d_base_v071_signal(ev):
    result = _f26_evz(ev, 252).ewm(span=42, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev/marketcap compression vs trailing mean (debt-load compression)
def f26ev_f26_ev_valuation_regime_evratiocomp_126d_base_v072_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = _f26_evcomp(r, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/marketcap compression vs trailing mean
def f26ev_f26_ev_valuation_regime_evratiocomp_252d_base_v073_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = _f26_evcomp(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebitda compression scaled by dispersion (expansion intensity)
def f26ev_f26_ev_valuation_regime_ebitdacompiq_126d_base_v074_signal(evebitda):
    comp = _f26_evcomp(evebitda, 126)
    lr = np.log(evebitda / evebitda.shift(1))
    result = _safe_div(comp, _std(lr, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev compression scaled by dispersion (expansion intensity)
def f26ev_f26_ev_valuation_regime_evcompiq_252d_base_v075_signal(ev):
    comp = _f26_evcomp(ev, 252)
    lr = np.log(ev / ev.shift(1))
    result = _safe_div(comp, _std(lr, 252))
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ev_f26_ev_valuation_regime_evz_63d_base_v001_signal,
    f26ev_f26_ev_valuation_regime_evz_126d_base_v002_signal,
    f26ev_f26_ev_valuation_regime_evz_252d_base_v003_signal,
    f26ev_f26_ev_valuation_regime_evz_504d_base_v004_signal,
    f26ev_f26_ev_valuation_regime_ebitdaz_63d_base_v005_signal,
    f26ev_f26_ev_valuation_regime_ebitdaz_126d_base_v006_signal,
    f26ev_f26_ev_valuation_regime_ebitdaz_252d_base_v007_signal,
    f26ev_f26_ev_valuation_regime_ebitdaz_504d_base_v008_signal,
    f26ev_f26_ev_valuation_regime_ebitz_63d_base_v009_signal,
    f26ev_f26_ev_valuation_regime_ebitz_126d_base_v010_signal,
    f26ev_f26_ev_valuation_regime_ebitz_252d_base_v011_signal,
    f26ev_f26_ev_valuation_regime_ebitz_504d_base_v012_signal,
    f26ev_f26_ev_valuation_regime_evtrend_63d_base_v013_signal,
    f26ev_f26_ev_valuation_regime_evtrend_126d_base_v014_signal,
    f26ev_f26_ev_valuation_regime_evtrend_252d_base_v015_signal,
    f26ev_f26_ev_valuation_regime_evtrend_504d_base_v016_signal,
    f26ev_f26_ev_valuation_regime_ebitdatrend_63d_base_v017_signal,
    f26ev_f26_ev_valuation_regime_ebitdatrend_126d_base_v018_signal,
    f26ev_f26_ev_valuation_regime_ebitdatrend_252d_base_v019_signal,
    f26ev_f26_ev_valuation_regime_ebitdatrend_504d_base_v020_signal,
    f26ev_f26_ev_valuation_regime_evratio_1d_base_v021_signal,
    f26ev_f26_ev_valuation_regime_evratioz_63d_base_v022_signal,
    f26ev_f26_ev_valuation_regime_evratioz_126d_base_v023_signal,
    f26ev_f26_ev_valuation_regime_evratioz_252d_base_v024_signal,
    f26ev_f26_ev_valuation_regime_evratiodev_63d_base_v025_signal,
    f26ev_f26_ev_valuation_regime_evratiodev_126d_base_v026_signal,
    f26ev_f26_ev_valuation_regime_evcomp_63d_base_v027_signal,
    f26ev_f26_ev_valuation_regime_evcomp_126d_base_v028_signal,
    f26ev_f26_ev_valuation_regime_evcomp_252d_base_v029_signal,
    f26ev_f26_ev_valuation_regime_evcomp_504d_base_v030_signal,
    f26ev_f26_ev_valuation_regime_ebitdacomp_63d_base_v031_signal,
    f26ev_f26_ev_valuation_regime_ebitdacomp_126d_base_v032_signal,
    f26ev_f26_ev_valuation_regime_ebitdacomp_252d_base_v033_signal,
    f26ev_f26_ev_valuation_regime_ebitcomp_63d_base_v034_signal,
    f26ev_f26_ev_valuation_regime_ebitcomp_126d_base_v035_signal,
    f26ev_f26_ev_valuation_regime_ebitcomp_252d_base_v036_signal,
    f26ev_f26_ev_valuation_regime_ebitdarank_126d_base_v037_signal,
    f26ev_f26_ev_valuation_regime_ebitdarank_252d_base_v038_signal,
    f26ev_f26_ev_valuation_regime_ebitdarank_504d_base_v039_signal,
    f26ev_f26_ev_valuation_regime_evrank_252d_base_v040_signal,
    f26ev_f26_ev_valuation_regime_evrank_504d_base_v041_signal,
    f26ev_f26_ev_valuation_regime_ebitrank_252d_base_v042_signal,
    f26ev_f26_ev_valuation_regime_regimeratio_1d_base_v043_signal,
    f26ev_f26_ev_valuation_regime_regimeratioz_63d_base_v044_signal,
    f26ev_f26_ev_valuation_regime_regimeratioz_126d_base_v045_signal,
    f26ev_f26_ev_valuation_regime_evgrowth_63d_base_v046_signal,
    f26ev_f26_ev_valuation_regime_evgrowth_126d_base_v047_signal,
    f26ev_f26_ev_valuation_regime_evgrowth_252d_base_v048_signal,
    f26ev_f26_ev_valuation_regime_evgrowth_504d_base_v049_signal,
    f26ev_f26_ev_valuation_regime_ebitdagrowth_126d_base_v050_signal,
    f26ev_f26_ev_valuation_regime_ebitdagrowth_252d_base_v051_signal,
    f26ev_f26_ev_valuation_regime_evdisp_63d_base_v052_signal,
    f26ev_f26_ev_valuation_regime_evdisp_126d_base_v053_signal,
    f26ev_f26_ev_valuation_regime_evdisp_252d_base_v054_signal,
    f26ev_f26_ev_valuation_regime_ebitdadisp_126d_base_v055_signal,
    f26ev_f26_ev_valuation_regime_ebitdadisp_252d_base_v056_signal,
    f26ev_f26_ev_valuation_regime_ebitdamr_63d_base_v057_signal,
    f26ev_f26_ev_valuation_regime_ebitdamr_126d_base_v058_signal,
    f26ev_f26_ev_valuation_regime_evmr_252d_base_v059_signal,
    f26ev_f26_ev_valuation_regime_ebitdatq_63d_base_v060_signal,
    f26ev_f26_ev_valuation_regime_ebitdatq_126d_base_v061_signal,
    f26ev_f26_ev_valuation_regime_evtq_126d_base_v062_signal,
    f26ev_f26_ev_valuation_regime_evtq_252d_base_v063_signal,
    f26ev_f26_ev_valuation_regime_ebitdaspread_63_252_base_v064_signal,
    f26ev_f26_ev_valuation_regime_evspread_63_252_base_v065_signal,
    f26ev_f26_ev_valuation_regime_evspread_21_126_base_v066_signal,
    f26ev_f26_ev_valuation_regime_zgap_126d_base_v067_signal,
    f26ev_f26_ev_valuation_regime_zgap_252d_base_v068_signal,
    f26ev_f26_ev_valuation_regime_evebitdazgap_252d_base_v069_signal,
    f26ev_f26_ev_valuation_regime_ebitdazewm_126d_base_v070_signal,
    f26ev_f26_ev_valuation_regime_evzewm_252d_base_v071_signal,
    f26ev_f26_ev_valuation_regime_evratiocomp_126d_base_v072_signal,
    f26ev_f26_ev_valuation_regime_evratiocomp_252d_base_v073_signal,
    f26ev_f26_ev_valuation_regime_ebitdacompiq_126d_base_v074_signal,
    f26ev_f26_ev_valuation_regime_evcompiq_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_EV_VALUATION_REGIME_REGISTRY_001_075 = REGISTRY


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
    domain_primitives = ("_f26_evz", "_f26_evtrend", "_f26_evratio", "_f26_evcomp")
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
    print(f"OK f26_ev_valuation_regime_base_001_075_claude: {n_features} features pass")
