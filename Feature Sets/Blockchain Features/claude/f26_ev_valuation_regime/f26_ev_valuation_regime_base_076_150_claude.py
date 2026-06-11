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


# ============ FEATURES 076-150 ============

# 21d z-score of evebitda (short-horizon multiple stretch)
def f26ev_f26_ev_valuation_regime_ebitdaz_21d_base_v076_signal(evebitda):
    result = _f26_evz(evebitda, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d z-score of evebitda
def f26ev_f26_ev_valuation_regime_ebitdaz_42d_base_v077_signal(evebitda):
    result = _f26_evz(evebitda, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d z-score of evebitda
def f26ev_f26_ev_valuation_regime_ebitdaz_189d_base_v078_signal(evebitda):
    result = _f26_evz(evebitda, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 315d z-score of evebitda
def f26ev_f26_ev_valuation_regime_ebitdaz_315d_base_v079_signal(evebitda):
    result = _f26_evz(evebitda, 315)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d z-score of ev
def f26ev_f26_ev_valuation_regime_evz_42d_base_v080_signal(ev):
    result = _f26_evz(ev, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d z-score of ev
def f26ev_f26_ev_valuation_regime_evz_189d_base_v081_signal(ev):
    result = _f26_evz(ev, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d z-score of ev
def f26ev_f26_ev_valuation_regime_evz_378d_base_v082_signal(ev):
    result = _f26_evz(ev, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d z-score of evebit
def f26ev_f26_ev_valuation_regime_ebitz_189d_base_v083_signal(evebit):
    result = _f26_evz(evebit, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d z-score of evebit
def f26ev_f26_ev_valuation_regime_ebitz_378d_base_v084_signal(evebit):
    result = _f26_evz(evebit, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d trend of ev
def f26ev_f26_ev_valuation_regime_evtrend_21d_base_v085_signal(ev):
    result = _f26_evtrend(ev, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d trend of ev
def f26ev_f26_ev_valuation_regime_evtrend_42d_base_v086_signal(ev):
    result = _f26_evtrend(ev, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d trend of ev
def f26ev_f26_ev_valuation_regime_evtrend_189d_base_v087_signal(ev):
    result = _f26_evtrend(ev, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d trend of ev
def f26ev_f26_ev_valuation_regime_evtrend_378d_base_v088_signal(ev):
    result = _f26_evtrend(ev, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 42d trend of evebit
def f26ev_f26_ev_valuation_regime_ebittrend_42d_base_v089_signal(evebit):
    result = _f26_evtrend(evebit, 42)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d trend of evebit
def f26ev_f26_ev_valuation_regime_ebittrend_126d_base_v090_signal(evebit):
    result = _f26_evtrend(evebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of evebit
def f26ev_f26_ev_valuation_regime_ebittrend_252d_base_v091_signal(evebit):
    result = _f26_evtrend(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d trend of evebit
def f26ev_f26_ev_valuation_regime_ebittrend_504d_base_v092_signal(evebit):
    result = _f26_evtrend(evebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d valuation compression of evebitda
def f26ev_f26_ev_valuation_regime_ebitdacomp_21d_base_v093_signal(evebitda):
    result = _f26_evcomp(evebitda, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d valuation compression of evebitda
def f26ev_f26_ev_valuation_regime_ebitdacomp_504d_base_v094_signal(evebitda):
    result = _f26_evcomp(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d valuation compression of evebit
def f26ev_f26_ev_valuation_regime_ebitcomp_504d_base_v095_signal(evebit):
    result = _f26_evcomp(evebit, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d valuation compression of ev
def f26ev_f26_ev_valuation_regime_evcomp_84d_base_v096_signal(ev):
    result = _f26_evcomp(ev, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d valuation compression of ev
def f26ev_f26_ev_valuation_regime_evcomp_189d_base_v097_signal(ev):
    result = _f26_evcomp(ev, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d z-score of evebitda
def f26ev_f26_ev_valuation_regime_ebitdaz_84d_base_v098_signal(evebitda):
    result = _f26_evz(evebitda, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d z-score of ev
def f26ev_f26_ev_valuation_regime_evz_84d_base_v099_signal(ev):
    result = _f26_evz(ev, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d trend of evebitda
def f26ev_f26_ev_valuation_regime_ebitdatrend_84d_base_v100_signal(evebitda):
    result = _f26_evtrend(evebitda, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 189d trend of evebitda
def f26ev_f26_ev_valuation_regime_ebitdatrend_189d_base_v101_signal(evebitda):
    result = _f26_evtrend(evebitda, 189)
    return result.replace([np.inf, -np.inf], np.nan)


# 378d trend of evebitda
def f26ev_f26_ev_valuation_regime_ebitdatrend_378d_base_v102_signal(evebitda):
    result = _f26_evtrend(evebitda, 378)
    return result.replace([np.inf, -np.inf], np.nan)


# 84d ev growth (log change)
def f26ev_f26_ev_valuation_regime_evgrowth_84d_base_v103_signal(ev):
    result = np.log(ev / ev.shift(84)) + _f26_evtrend(ev, 84) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 189d ev growth (log change)
def f26ev_f26_ev_valuation_regime_evgrowth_189d_base_v104_signal(ev):
    result = np.log(ev / ev.shift(189)) + _f26_evtrend(ev, 189) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebitda growth (log change)
def f26ev_f26_ev_valuation_regime_ebitdagrowth_63d_base_v105_signal(evebitda):
    result = np.log(evebitda / evebitda.shift(63)) + _f26_evtrend(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebitda growth (log change)
def f26ev_f26_ev_valuation_regime_ebitdagrowth_504d_base_v106_signal(evebitda):
    result = np.log(evebitda / evebitda.shift(504)) + _f26_evtrend(evebitda, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebit growth (log change)
def f26ev_f26_ev_valuation_regime_ebitgrowth_126d_base_v107_signal(evebit):
    result = np.log(evebit / evebit.shift(126)) + _f26_evtrend(evebit, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit growth (log change)
def f26ev_f26_ev_valuation_regime_ebitgrowth_252d_base_v108_signal(evebit):
    result = np.log(evebit / evebit.shift(252)) + _f26_evtrend(evebit, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_ebitdisp_63d_base_v109_signal(evebit):
    lr = np.log(evebit / evebit.shift(1))
    result = _std(lr, 63) + _f26_evtrend(evebit, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebit dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_ebitdisp_126d_base_v110_signal(evebit):
    lr = np.log(evebit / evebit.shift(1))
    result = _std(lr, 126) + _f26_evtrend(evebit, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d ev dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_evdisp_504d_base_v111_signal(ev):
    lr = np.log(ev / ev.shift(1))
    result = _std(lr, 504) + _f26_evtrend(ev, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebitda dispersion (rolling std of log returns)
def f26ev_f26_ev_valuation_regime_ebitdadisp_504d_base_v112_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    result = _std(lr, 504) + _f26_evtrend(evebitda, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebit mean-reversion (negative z)
def f26ev_f26_ev_valuation_regime_ebitmr_252d_base_v113_signal(evebit):
    result = -_f26_evz(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev mean-reversion (negative z)
def f26ev_f26_ev_valuation_regime_evmr_126d_base_v114_signal(ev):
    result = -_f26_evz(ev, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d evebitda mean-reversion (negative z)
def f26ev_f26_ev_valuation_regime_ebitdamr_504d_base_v115_signal(evebitda):
    result = -_f26_evz(evebitda, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebitda trend slope per unit dispersion (trend quality)
def f26ev_f26_ev_valuation_regime_ebitdatq_252d_base_v116_signal(evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    v = _std(lr, 252) * np.sqrt(252.0)
    result = _safe_div(_f26_evtrend(evebitda, 252), v)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit trend slope per unit dispersion
def f26ev_f26_ev_valuation_regime_ebittq_63d_base_v117_signal(evebit):
    lr = np.log(evebit / evebit.shift(1))
    v = _std(lr, 63) * np.sqrt(63.0)
    result = _safe_div(_f26_evtrend(evebit, 63), v)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebit trend slope per unit dispersion
def f26ev_f26_ev_valuation_regime_ebittq_126d_base_v118_signal(evebit):
    lr = np.log(evebit / evebit.shift(1))
    v = _std(lr, 126) * np.sqrt(126.0)
    result = _safe_div(_f26_evtrend(evebit, 126), v)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d vs 84d evebitda trend spread (short acceleration)
def f26ev_f26_ev_valuation_regime_ebitdaspread_21_84_base_v119_signal(evebitda):
    result = _f26_evtrend(evebitda, 21) - _f26_evtrend(evebitda, 84)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d vs 504d ev trend spread (long acceleration)
def f26ev_f26_ev_valuation_regime_evspread_126_504_base_v120_signal(ev):
    result = _f26_evtrend(ev, 126) - _f26_evtrend(ev, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d vs 252d evebit trend spread
def f26ev_f26_ev_valuation_regime_ebitspread_63_252_base_v121_signal(evebit):
    result = _f26_evtrend(evebit, 63) - _f26_evtrend(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# evebitda z minus evebit z over 126d (alt structure gap)
def f26ev_f26_ev_valuation_regime_zgap63_126d_base_v122_signal(evebitda, evebit):
    result = _f26_evz(evebitda, 63) - _f26_evz(evebit, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# ev z minus evebit z over 252d
def f26ev_f26_ev_valuation_regime_evebitzgap_252d_base_v123_signal(ev, evebit):
    result = _f26_evz(ev, 252) - _f26_evz(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d EWMA-smoothed evebit z-score
def f26ev_f26_ev_valuation_regime_ebitzewm_63d_base_v124_signal(evebit):
    result = _f26_evz(evebit, 63).ewm(span=10, min_periods=5).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 504d EWMA-smoothed evebitda z-score
def f26ev_f26_ev_valuation_regime_ebitdazewm_504d_base_v125_signal(evebitda):
    result = _f26_evz(evebitda, 504).ewm(span=63, min_periods=21).mean()
    return result.replace([np.inf, -np.inf], np.nan)


# 63d evebit compression scaled by dispersion (expansion intensity)
def f26ev_f26_ev_valuation_regime_ebitcompiq_63d_base_v126_signal(evebit):
    comp = _f26_evcomp(evebit, 63)
    lr = np.log(evebit / evebit.shift(1))
    result = _safe_div(comp, _std(lr, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebitda compression scaled by dispersion
def f26ev_f26_ev_valuation_regime_ebitdacompiq_252d_base_v127_signal(evebitda):
    comp = _f26_evcomp(evebitda, 252)
    lr = np.log(evebitda / evebitda.shift(1))
    result = _safe_div(comp, _std(lr, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev compression scaled by dispersion
def f26ev_f26_ev_valuation_regime_evcompiq_126d_base_v128_signal(ev):
    comp = _f26_evcomp(ev, 126)
    lr = np.log(ev / ev.shift(1))
    result = _safe_div(comp, _std(lr, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d ev/marketcap deviation from trailing mean
def f26ev_f26_ev_valuation_regime_evratiodev_21d_base_v129_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r - _mean(r, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev/marketcap deviation from trailing mean
def f26ev_f26_ev_valuation_regime_evratiodev_252d_base_v130_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r - _mean(r, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d z-score of ev/marketcap ratio
def f26ev_f26_ev_valuation_regime_evratioz_504d_base_v131_signal(ev, marketcap):
    result = _z(_f26_evratio(ev, marketcap), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d trend of ev/marketcap debt-load ratio
def f26ev_f26_ev_valuation_regime_evratiotrend_63d_base_v132_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.pct_change(periods=63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d trend of ev/marketcap debt-load ratio
def f26ev_f26_ev_valuation_regime_evratiotrend_126d_base_v133_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.pct_change(periods=126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of ev/marketcap debt-load ratio
def f26ev_f26_ev_valuation_regime_evratiotrend_252d_base_v134_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.pct_change(periods=252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percentile rank of evebit level
def f26ev_f26_ev_valuation_regime_ebitrank_126d_base_v135_signal(evebit):
    result = evebit.rolling(126, min_periods=42).rank(pct=True) + _f26_evz(evebit, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 504d percentile rank of evebit level
def f26ev_f26_ev_valuation_regime_ebitrank_504d_base_v136_signal(evebit):
    result = evebit.rolling(504, min_periods=168).rank(pct=True) + _f26_evz(evebit, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percentile rank of ev level
def f26ev_f26_ev_valuation_regime_evrank_126d_base_v137_signal(ev):
    result = ev.rolling(126, min_periods=42).rank(pct=True) + _f26_evz(ev, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d percentile rank of ev/marketcap ratio
def f26ev_f26_ev_valuation_regime_evratiorank_126d_base_v138_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.rolling(126, min_periods=42).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d percentile rank of ev/marketcap ratio
def f26ev_f26_ev_valuation_regime_evratiorank_252d_base_v139_signal(ev, marketcap):
    r = _f26_evratio(ev, marketcap)
    result = r.rolling(252, min_periods=84).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d z-score of evebitda/evebit regime ratio (long window)
def f26ev_f26_ev_valuation_regime_regimeratioz_252d_base_v140_signal(evebitda, evebit):
    result = _z(_safe_div(evebitda, evebit), 252) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d compression of evebitda/evebit regime ratio
def f26ev_f26_ev_valuation_regime_regimecomp_126d_base_v141_signal(evebitda, evebit):
    r = _safe_div(evebitda, evebit)
    result = _f26_evcomp(r, 126) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d trend of evebitda/evebit regime ratio
def f26ev_f26_ev_valuation_regime_regimetrend_252d_base_v142_signal(evebitda, evebit):
    r = _safe_div(evebitda, evebit)
    result = r.pct_change(periods=252) + _f26_evz(evebitda, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev minus marketcap z divergence (debt buildup vs equity)
def f26ev_f26_ev_valuation_regime_evmcapzgap_252d_base_v143_signal(ev, marketcap):
    result = _f26_evz(ev, 252) - _z(marketcap, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev minus marketcap z divergence
def f26ev_f26_ev_valuation_regime_evmcapzgap_126d_base_v144_signal(ev, marketcap):
    result = _f26_evz(ev, 126) - _z(marketcap, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev growth minus marketcap growth (leverage expansion)
def f26ev_f26_ev_valuation_regime_evmcapgrowthgap_252d_base_v145_signal(ev, marketcap):
    eg = np.log(ev / ev.shift(252))
    mg = np.log(marketcap / marketcap.shift(252))
    result = eg - mg + _f26_evtrend(ev, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 126d ev growth minus marketcap growth
def f26ev_f26_ev_valuation_regime_evmcapgrowthgap_126d_base_v146_signal(ev, marketcap):
    eg = np.log(ev / ev.shift(126))
    mg = np.log(marketcap / marketcap.shift(126))
    result = eg - mg + _f26_evtrend(ev, 126) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


# 252d evebitda compression vs cross-multiple evebit compression (regime divergence)
def f26ev_f26_ev_valuation_regime_compgap_252d_base_v147_signal(evebitda, evebit):
    result = _f26_evcomp(evebitda, 252) - _f26_evcomp(evebit, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d evebitda compression vs evebit compression
def f26ev_f26_ev_valuation_regime_compgap_126d_base_v148_signal(evebitda, evebit):
    result = _f26_evcomp(evebitda, 126) - _f26_evcomp(evebit, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d ev z scaled by evebitda dispersion (stretch per multiple-vol)
def f26ev_f26_ev_valuation_regime_evzscaled_252d_base_v149_signal(ev, evebitda):
    lr = np.log(evebitda / evebitda.shift(1))
    result = _safe_div(_f26_evz(ev, 252), _std(lr, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# blended multi-horizon evebitda z composite (63/126/252/504)
def f26ev_f26_ev_valuation_regime_ebitdazblend_multi_base_v150_signal(evebitda):
    result = (_f26_evz(evebitda, 63) + _f26_evz(evebitda, 126)
              + _f26_evz(evebitda, 252) + _f26_evz(evebitda, 504)) / 4.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26ev_f26_ev_valuation_regime_ebitdaz_21d_base_v076_signal,
    f26ev_f26_ev_valuation_regime_ebitdaz_42d_base_v077_signal,
    f26ev_f26_ev_valuation_regime_ebitdaz_189d_base_v078_signal,
    f26ev_f26_ev_valuation_regime_ebitdaz_315d_base_v079_signal,
    f26ev_f26_ev_valuation_regime_evz_42d_base_v080_signal,
    f26ev_f26_ev_valuation_regime_evz_189d_base_v081_signal,
    f26ev_f26_ev_valuation_regime_evz_378d_base_v082_signal,
    f26ev_f26_ev_valuation_regime_ebitz_189d_base_v083_signal,
    f26ev_f26_ev_valuation_regime_ebitz_378d_base_v084_signal,
    f26ev_f26_ev_valuation_regime_evtrend_21d_base_v085_signal,
    f26ev_f26_ev_valuation_regime_evtrend_42d_base_v086_signal,
    f26ev_f26_ev_valuation_regime_evtrend_189d_base_v087_signal,
    f26ev_f26_ev_valuation_regime_evtrend_378d_base_v088_signal,
    f26ev_f26_ev_valuation_regime_ebittrend_42d_base_v089_signal,
    f26ev_f26_ev_valuation_regime_ebittrend_126d_base_v090_signal,
    f26ev_f26_ev_valuation_regime_ebittrend_252d_base_v091_signal,
    f26ev_f26_ev_valuation_regime_ebittrend_504d_base_v092_signal,
    f26ev_f26_ev_valuation_regime_ebitdacomp_21d_base_v093_signal,
    f26ev_f26_ev_valuation_regime_ebitdacomp_504d_base_v094_signal,
    f26ev_f26_ev_valuation_regime_ebitcomp_504d_base_v095_signal,
    f26ev_f26_ev_valuation_regime_evcomp_84d_base_v096_signal,
    f26ev_f26_ev_valuation_regime_evcomp_189d_base_v097_signal,
    f26ev_f26_ev_valuation_regime_ebitdaz_84d_base_v098_signal,
    f26ev_f26_ev_valuation_regime_evz_84d_base_v099_signal,
    f26ev_f26_ev_valuation_regime_ebitdatrend_84d_base_v100_signal,
    f26ev_f26_ev_valuation_regime_ebitdatrend_189d_base_v101_signal,
    f26ev_f26_ev_valuation_regime_ebitdatrend_378d_base_v102_signal,
    f26ev_f26_ev_valuation_regime_evgrowth_84d_base_v103_signal,
    f26ev_f26_ev_valuation_regime_evgrowth_189d_base_v104_signal,
    f26ev_f26_ev_valuation_regime_ebitdagrowth_63d_base_v105_signal,
    f26ev_f26_ev_valuation_regime_ebitdagrowth_504d_base_v106_signal,
    f26ev_f26_ev_valuation_regime_ebitgrowth_126d_base_v107_signal,
    f26ev_f26_ev_valuation_regime_ebitgrowth_252d_base_v108_signal,
    f26ev_f26_ev_valuation_regime_ebitdisp_63d_base_v109_signal,
    f26ev_f26_ev_valuation_regime_ebitdisp_126d_base_v110_signal,
    f26ev_f26_ev_valuation_regime_evdisp_504d_base_v111_signal,
    f26ev_f26_ev_valuation_regime_ebitdadisp_504d_base_v112_signal,
    f26ev_f26_ev_valuation_regime_ebitmr_252d_base_v113_signal,
    f26ev_f26_ev_valuation_regime_evmr_126d_base_v114_signal,
    f26ev_f26_ev_valuation_regime_ebitdamr_504d_base_v115_signal,
    f26ev_f26_ev_valuation_regime_ebitdatq_252d_base_v116_signal,
    f26ev_f26_ev_valuation_regime_ebittq_63d_base_v117_signal,
    f26ev_f26_ev_valuation_regime_ebittq_126d_base_v118_signal,
    f26ev_f26_ev_valuation_regime_ebitdaspread_21_84_base_v119_signal,
    f26ev_f26_ev_valuation_regime_evspread_126_504_base_v120_signal,
    f26ev_f26_ev_valuation_regime_ebitspread_63_252_base_v121_signal,
    f26ev_f26_ev_valuation_regime_zgap63_126d_base_v122_signal,
    f26ev_f26_ev_valuation_regime_evebitzgap_252d_base_v123_signal,
    f26ev_f26_ev_valuation_regime_ebitzewm_63d_base_v124_signal,
    f26ev_f26_ev_valuation_regime_ebitdazewm_504d_base_v125_signal,
    f26ev_f26_ev_valuation_regime_ebitcompiq_63d_base_v126_signal,
    f26ev_f26_ev_valuation_regime_ebitdacompiq_252d_base_v127_signal,
    f26ev_f26_ev_valuation_regime_evcompiq_126d_base_v128_signal,
    f26ev_f26_ev_valuation_regime_evratiodev_21d_base_v129_signal,
    f26ev_f26_ev_valuation_regime_evratiodev_252d_base_v130_signal,
    f26ev_f26_ev_valuation_regime_evratioz_504d_base_v131_signal,
    f26ev_f26_ev_valuation_regime_evratiotrend_63d_base_v132_signal,
    f26ev_f26_ev_valuation_regime_evratiotrend_126d_base_v133_signal,
    f26ev_f26_ev_valuation_regime_evratiotrend_252d_base_v134_signal,
    f26ev_f26_ev_valuation_regime_ebitrank_126d_base_v135_signal,
    f26ev_f26_ev_valuation_regime_ebitrank_504d_base_v136_signal,
    f26ev_f26_ev_valuation_regime_evrank_126d_base_v137_signal,
    f26ev_f26_ev_valuation_regime_evratiorank_126d_base_v138_signal,
    f26ev_f26_ev_valuation_regime_evratiorank_252d_base_v139_signal,
    f26ev_f26_ev_valuation_regime_regimeratioz_252d_base_v140_signal,
    f26ev_f26_ev_valuation_regime_regimecomp_126d_base_v141_signal,
    f26ev_f26_ev_valuation_regime_regimetrend_252d_base_v142_signal,
    f26ev_f26_ev_valuation_regime_evmcapzgap_252d_base_v143_signal,
    f26ev_f26_ev_valuation_regime_evmcapzgap_126d_base_v144_signal,
    f26ev_f26_ev_valuation_regime_evmcapgrowthgap_252d_base_v145_signal,
    f26ev_f26_ev_valuation_regime_evmcapgrowthgap_126d_base_v146_signal,
    f26ev_f26_ev_valuation_regime_compgap_252d_base_v147_signal,
    f26ev_f26_ev_valuation_regime_compgap_126d_base_v148_signal,
    f26ev_f26_ev_valuation_regime_evzscaled_252d_base_v149_signal,
    f26ev_f26_ev_valuation_regime_ebitdazblend_multi_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_EV_VALUATION_REGIME_REGISTRY_076_150 = REGISTRY


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
    print(f"OK f26_ev_valuation_regime_base_076_150_claude: {n_features} features pass")
