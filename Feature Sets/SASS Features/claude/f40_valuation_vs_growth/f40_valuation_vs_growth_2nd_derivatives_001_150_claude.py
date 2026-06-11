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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


# ===== GARP domain primitives =====
def _grw(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _peg(mult, growth_pct):
    g = (growth_pct * 100.0).replace(0, np.nan)
    return mult / g


def _evsales(ev, revenue):
    return _safe_div(ev, revenue)


def _earnyield(netinc, marketcap):
    return _safe_div(netinc, marketcap)


def _fcfyield(fcf, marketcap):
    return _safe_div(fcf, marketcap)


def _ebitda_yield(ebitda, ev):
    return _safe_div(ebitda, ev)


def f40vg_f40_valuation_vs_growth_pevrev_252d_slope_v001_signal(pe, revenue):
    base = -_z(pe, 252) + _z(_grw(revenue, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_pevni_252d_slope_v002_signal(pe, netinc):
    base = -_z(pe, 126) + _z(_grw(netinc, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_pevfcf_252d_slope_v003_signal(pe, fcf):
    base = -_z(pe, 252) + _z(_grw(fcf, 504), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_pevebitda_126d_slope_v004_signal(pe, ebitda):
    base = -_z(pe, 126) + _z(_grw(ebitda, 126), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evebvrev_252d_slope_v005_signal(evebitda, revenue):
    base = -_z(evebitda, 252) + _z(_grw(revenue, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evebveb_252d_slope_v006_signal(evebitda, ebitda):
    base = -_z(evebitda, 126) + _z(_grw(ebitda, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evebvfcf_252d_slope_v007_signal(evebitda, fcf):
    base = -_z(evebitda, 252) + _z(_grw(fcf, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evebvni_126d_slope_v008_signal(evebitda, netinc):
    base = -_z(evebitda, 126) + _z(_grw(netinc, 126), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_psvrev_252d_slope_v009_signal(ps, revenue):
    base = -_z(ps, 252) + _z(_grw(revenue, 504), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_psveb_252d_slope_v010_signal(ps, ebitda):
    base = -_z(ps, 126) + _z(_grw(ebitda, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_psvni_252d_slope_v011_signal(ps, netinc):
    base = -_z(ps, 252) + _z(_grw(netinc, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evsvrev_252d_slope_v012_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    base = -_z(evs, 252) + _z(_grw(revenue, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evsveb_252d_slope_v013_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    base = -_z(evs, 126) + _z(_grw(ebitda, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evsvfcf_252d_slope_v014_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    base = -_z(evs, 252) + _z(_grw(fcf, 504), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_eyr40rev_252d_slope_v015_signal(netinc, marketcap, revenue):
    base = _z(_earnyield(netinc, marketcap), 252) + _z(_grw(revenue, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_eyr40ni_252d_slope_v016_signal(netinc, marketcap):
    base = _z(_earnyield(netinc, marketcap), 126) + _z(_grw(netinc, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fyr40rev_252d_slope_v017_signal(fcf, marketcap, revenue):
    base = _z(_fcfyield(fcf, marketcap), 252) + _z(_grw(revenue, 504), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fyr40eb_252d_slope_v018_signal(fcf, marketcap, ebitda):
    base = _z(_fcfyield(fcf, marketcap), 126) + _z(_grw(ebitda, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fyr40fcf_252d_slope_v019_signal(fcf, marketcap):
    base = _z(_fcfyield(fcf, marketcap), 252) + _z(_grw(fcf, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ebyr40eb_252d_slope_v020_signal(ebitda, ev):
    base = _z(_ebitda_yield(ebitda, ev), 252) + _z(_grw(ebitda, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ebyr40rev_252d_slope_v021_signal(ebitda, ev, revenue):
    base = _z(_ebitda_yield(ebitda, ev), 126) + _z(_grw(revenue, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_syr40rev_252d_slope_v022_signal(marketcap, revenue):
    base = _z(_safe_div(revenue, marketcap), 252) + _z(_grw(revenue, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_syr40eb_252d_slope_v023_signal(marketcap, revenue, ebitda):
    base = _z(_safe_div(revenue, marketcap), 126) + _z(_grw(ebitda, 504), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_divpe_252d_slope_v024_signal(pe, revenue):
    base = _z(_grw(revenue, 252), 126) - _z(pe, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_diveveb_252d_slope_v025_signal(evebitda, ebitda):
    base = _z(_grw(ebitda, 504), 252) - _z(evebitda, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_divps_252d_slope_v026_signal(ps, revenue):
    base = _z(_grw(revenue, 126), 126) - _z(ps, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_divevs_252d_slope_v027_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    base = _z(_grw(ebitda, 504), 252) - _z(evs, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_diveyrev_252d_slope_v028_signal(netinc, marketcap, revenue):
    base = _z(_earnyield(netinc, marketcap), 252) - _z(_grw(revenue, 252), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_divfyeb_252d_slope_v029_signal(fcf, marketcap, ebitda):
    base = _z(_fcfyield(fcf, marketcap), 126) - _z(_grw(ebitda, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_oplevev_252d_slope_v030_signal(evebitda, ebitda, revenue):
    base = _z(_grw(ebitda, 252) - _grw(revenue, 252), 126) - _z(evebitda, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_cashqualpe_252d_slope_v031_signal(pe, fcf, netinc):
    base = _z(_grw(fcf, 252) - _grw(netinc, 252), 126) - _z(pe, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_grwsprps_252d_slope_v032_signal(ps, revenue, netinc):
    base = _z(_grw(netinc, 252) - _grw(revenue, 252), 126) - _z(ps, 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_grwsprev_252d_slope_v033_signal(ev, revenue, ebitda, netinc):
    evs = _evsales(ev, revenue)
    base = _z(_grw(netinc, 504) - _grw(ebitda, 252), 126) - _z(evs, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_accelpe_252d_slope_v034_signal(pe, revenue):
    g = _grw(revenue, 126)
    base = _z(g - g.shift(63), 126) - _z(pe, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_acceleveb_252d_slope_v035_signal(evebitda, ebitda):
    g = _grw(ebitda, 126)
    base = _z(g - g.shift(63), 126) - _z(evebitda, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_accelps_252d_slope_v036_signal(ps, revenue):
    g = _grw(revenue, 63)
    base = _z(g - g.shift(21), 63) - _z(ps, 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_marginvgeb_252d_slope_v037_signal(ebitda, revenue, evebitda):
    margin = _safe_div(ebitda, revenue)
    base = _z(margin, 252) + _z(_grw(ebitda, 252), 126) - _z(evebitda, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_nmvgpe_252d_slope_v038_signal(netinc, revenue, pe):
    nm = _safe_div(netinc, revenue)
    base = _z(nm, 126) + _z(_grw(netinc, 252), 252) - _z(pe, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fmvgevs_252d_slope_v039_signal(fcf, revenue, ev):
    fm = _safe_div(fcf, revenue)
    evs = _evsales(ev, revenue)
    base = _z(fm, 252) + _z(_grw(fcf, 252), 126) - _z(evs, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ranksumpe_252d_slope_v040_signal(pe, revenue):
    base = _rank(_grw(revenue, 252), 504) - _rank(pe, 504)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ranksumeveb_252d_slope_v041_signal(evebitda, ebitda):
    base = _rank(_grw(ebitda, 252), 504) - _rank(evebitda, 504)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ranksumps_252d_slope_v042_signal(ps, netinc):
    base = _rank(_grw(netinc, 252), 504) - _rank(ps, 504)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ranksumevs_252d_slope_v043_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    base = _rank(_grw(fcf, 252), 504) - _rank(evs, 504)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_megapevrev_252d_slope_v044_signal(pe, evebitda, revenue, ebitda):
    base = -(_z(pe, 252) + _z(evebitda, 252)) + (_z(_grw(revenue, 252), 252) + _z(_grw(ebitda, 252), 252))
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_megapsfcf_252d_slope_v045_signal(ps, ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    base = -(_z(ps, 252) + _z(evs, 252)) + (_z(_grw(revenue, 504), 252) + _z(_grw(fcf, 252), 252))
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_megayield_252d_slope_v046_signal(netinc, fcf, marketcap, revenue, ebitda):
    base = _z(_earnyield(netinc, marketcap), 252) + _z(_fcfyield(fcf, marketcap), 252) + _z(_grw(revenue, 252), 126) + _z(_grw(ebitda, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_sizepe_252d_slope_v047_signal(pe, revenue, marketcap):
    base = (-_z(pe, 252) + _z(_grw(revenue, 252), 252)) * (0.5 - _rank(np.log(marketcap.replace(0, np.nan)), 504))
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_sizeeveb_252d_slope_v048_signal(evebitda, ebitda, marketcap):
    base = (-_z(evebitda, 252) + _z(_grw(ebitda, 252), 252)) - _rank(np.log(marketcap.replace(0, np.nan)), 504)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_tanhpe_252d_slope_v049_signal(pe, revenue):
    base = np.tanh(0.5 * (-_z(pe, 252) + _z(_grw(revenue, 252), 252)))
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_tanheveb_252d_slope_v050_signal(evebitda, ebitda):
    base = np.tanh(0.5 * (-_z(evebitda, 252) + _z(_grw(ebitda, 252), 252)))
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_tanhfcf_252d_slope_v051_signal(pe, fcf, marketcap):
    base = np.tanh(0.4 * (_z(_fcfyield(fcf, marketcap), 252) + _z(_grw(fcf, 252), 252) - _z(pe, 252)))
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fairpez_252d_slope_v052_signal(pe, revenue):
    base = _z(pe - _grw(revenue, 252) * 100.0, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fairevebz_252d_slope_v053_signal(evebitda, ebitda):
    base = _z(evebitda - 0.5 * _grw(ebitda, 252) * 100.0, 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fairpsz_252d_slope_v054_signal(ps, revenue):
    base = _z(ps - 0.2 * _grw(revenue, 504) * 100.0, 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fairevsz_252d_slope_v055_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    base = _z(evs - (1.0 + 2.0 * _grw(fcf, 252)), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_consistpe_252d_slope_v056_signal(pe, revenue):
    g = _grw(revenue, 63)
    consist = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    base = consist - _z(pe, 252) * 0.5
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_consisteveb_252d_slope_v057_signal(evebitda, ebitda):
    g = _grw(ebitda, 63)
    consist = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    base = consist - _z(evebitda, 252) * 0.5
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_horizpe_252d_slope_v058_signal(pe, revenue):
    base = (-_z(pe, 252) + _z(_grw(revenue, 504), 252)) - (-_z(pe, 252) + _z(_grw(revenue, 252), 252))
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_horizeveb_252d_slope_v059_signal(evebitda, ebitda):
    base = (-_z(evebitda, 252) + _z(_grw(ebitda, 504), 252)) - (-_z(evebitda, 252) + _z(_grw(ebitda, 252), 252))
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_durpe_504d_slope_v060_signal(pe, revenue):
    base = -_z(_mean(pe, 252), 252) + _z(_grw(revenue, 504), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_dureveb_504d_slope_v061_signal(evebitda, ebitda):
    base = -_z(_mean(evebitda, 252), 252) + _z(_grw(ebitda, 504), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_yielddisp_252d_slope_v062_signal(netinc, fcf, ebitda, marketcap, ev):
    ey = _z(_earnyield(netinc, marketcap), 252)
    fy = _z(_fcfyield(fcf, marketcap), 252)
    eby = _z(_ebitda_yield(ebitda, ev), 252)
    base = pd.concat([ey, fy, eby], axis=1).std(axis=1)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_compintz_252d_slope_v063_signal(marketcap, revenue, ebitda):
    sy = _safe_div(revenue, marketcap)
    margin = _safe_div(ebitda, revenue)
    base = _z(sy * margin * (1.0 + _grw(revenue, 252)), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_qualintz_252d_slope_v064_signal(netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    nm = _safe_div(netinc, revenue)
    base = _z(ey * (1.0 + nm) * (1.0 + _grw(netinc, 252)), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_cashintz_252d_slope_v065_signal(fcf, marketcap, revenue):
    fy = _fcfyield(fcf, marketcap)
    fm = _safe_div(fcf, revenue)
    base = _z(fy * (1.0 + fm) * (1.0 + _grw(fcf, 252)), 252)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_reratepe_252d_slope_v066_signal(pe, netinc):
    base = _z(pe / pe.shift(63) - 1.0, 126) - _z(_grw(netinc, 63), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_rerateeveb_252d_slope_v067_signal(evebitda, ebitda):
    base = _z(evebitda / evebitda.shift(63) - 1.0, 126) - _z(_grw(ebitda, 63), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_rerateevs_252d_slope_v068_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    base = _z(evs / evs.shift(63) - 1.0, 126) - _z(_grw(revenue, 63), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastpe_63d_slope_v069_signal(pe, revenue):
    base = -_z(pe, 63) + _z(_grw(revenue, 63), 63)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fasteveb_63d_slope_v070_signal(evebitda, ebitda):
    base = -_z(evebitda, 63) + _z(_grw(ebitda, 63), 63)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastps_63d_slope_v071_signal(ps, revenue):
    base = -_z(ps, 63) + _z(_grw(revenue, 63), 63)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastni_63d_slope_v072_signal(pe, netinc):
    base = -_z(pe, 63) + _z(_grw(netinc, 63), 63)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastevs_63d_slope_v073_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    base = -_z(evs, 63) + _z(_grw(revenue, 63), 63)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastfcf_63d_slope_v074_signal(pe, fcf):
    base = -_z(pe, 63) + _z(_grw(fcf, 63), 63)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_psvfcf_252d_slope_v075_signal(ps, fcf):
    base = -_z(ps, 252) + _z(_grw(fcf, 252), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_pevrev2_252d_slope_v076_signal(pe, revenue):
    base = -_z(pe, 252) + _z(_grw(revenue, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_pevni2_252d_slope_v077_signal(pe, netinc):
    base = -_z(pe, 126) + _z(_grw(netinc, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_pevfcf2_252d_slope_v078_signal(pe, fcf):
    base = -_z(pe, 252) + _z(_grw(fcf, 504), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_pevebitda2_126d_slope_v079_signal(pe, ebitda):
    base = -_z(pe, 126) + _z(_grw(ebitda, 126), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evebvrev2_252d_slope_v080_signal(evebitda, revenue):
    base = -_z(evebitda, 252) + _z(_grw(revenue, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evebveb2_252d_slope_v081_signal(evebitda, ebitda):
    base = -_z(evebitda, 126) + _z(_grw(ebitda, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evebvfcf2_252d_slope_v082_signal(evebitda, fcf):
    base = -_z(evebitda, 252) + _z(_grw(fcf, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evebvni2_126d_slope_v083_signal(evebitda, netinc):
    base = -_z(evebitda, 126) + _z(_grw(netinc, 126), 126)
    result = (base - base.shift(63)) / 63.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_psvrev2_252d_slope_v084_signal(ps, revenue):
    base = -_z(ps, 252) + _z(_grw(revenue, 504), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_psveb2_252d_slope_v085_signal(ps, ebitda):
    base = -_z(ps, 126) + _z(_grw(ebitda, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_psvni2_252d_slope_v086_signal(ps, netinc):
    base = -_z(ps, 252) + _z(_grw(netinc, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evsvrev2_252d_slope_v087_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    base = -_z(evs, 252) + _z(_grw(revenue, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evsveb2_252d_slope_v088_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    base = -_z(evs, 126) + _z(_grw(ebitda, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_evsvfcf2_252d_slope_v089_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    base = -_z(evs, 252) + _z(_grw(fcf, 504), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_eyr40rev2_252d_slope_v090_signal(netinc, marketcap, revenue):
    base = _z(_earnyield(netinc, marketcap), 252) + _z(_grw(revenue, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_eyr40ni2_252d_slope_v091_signal(netinc, marketcap):
    base = _z(_earnyield(netinc, marketcap), 126) + _z(_grw(netinc, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fyr40rev2_252d_slope_v092_signal(fcf, marketcap, revenue):
    base = _z(_fcfyield(fcf, marketcap), 252) + _z(_grw(revenue, 504), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fyr40eb2_252d_slope_v093_signal(fcf, marketcap, ebitda):
    base = _z(_fcfyield(fcf, marketcap), 126) + _z(_grw(ebitda, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fyr40fcf2_252d_slope_v094_signal(fcf, marketcap):
    base = _z(_fcfyield(fcf, marketcap), 252) + _z(_grw(fcf, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ebyr40eb2_252d_slope_v095_signal(ebitda, ev):
    base = _z(_ebitda_yield(ebitda, ev), 252) + _z(_grw(ebitda, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ebyr40rev2_252d_slope_v096_signal(ebitda, ev, revenue):
    base = _z(_ebitda_yield(ebitda, ev), 126) + _z(_grw(revenue, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_syr40rev2_252d_slope_v097_signal(marketcap, revenue):
    base = _z(_safe_div(revenue, marketcap), 252) + _z(_grw(revenue, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_syr40eb2_252d_slope_v098_signal(marketcap, revenue, ebitda):
    base = _z(_safe_div(revenue, marketcap), 126) + _z(_grw(ebitda, 504), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_divpe2_252d_slope_v099_signal(pe, revenue):
    base = _z(_grw(revenue, 252), 126) - _z(pe, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_diveveb2_252d_slope_v100_signal(evebitda, ebitda):
    base = _z(_grw(ebitda, 504), 252) - _z(evebitda, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_divps2_252d_slope_v101_signal(ps, revenue):
    base = _z(_grw(revenue, 126), 126) - _z(ps, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_divevs2_252d_slope_v102_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    base = _z(_grw(ebitda, 504), 252) - _z(evs, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_diveyrev2_252d_slope_v103_signal(netinc, marketcap, revenue):
    base = _z(_earnyield(netinc, marketcap), 252) - _z(_grw(revenue, 252), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_divfyeb2_252d_slope_v104_signal(fcf, marketcap, ebitda):
    base = _z(_fcfyield(fcf, marketcap), 126) - _z(_grw(ebitda, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_oplevev2_252d_slope_v105_signal(evebitda, ebitda, revenue):
    base = _z(_grw(ebitda, 252) - _grw(revenue, 252), 126) - _z(evebitda, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_cashqualpe2_252d_slope_v106_signal(pe, fcf, netinc):
    base = _z(_grw(fcf, 252) - _grw(netinc, 252), 126) - _z(pe, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_grwsprps2_252d_slope_v107_signal(ps, revenue, netinc):
    base = _z(_grw(netinc, 252) - _grw(revenue, 252), 126) - _z(ps, 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_grwsprev2_252d_slope_v108_signal(ev, revenue, ebitda, netinc):
    evs = _evsales(ev, revenue)
    base = _z(_grw(netinc, 504) - _grw(ebitda, 252), 126) - _z(evs, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_accelpe2_252d_slope_v109_signal(pe, revenue):
    g = _grw(revenue, 126)
    base = _z(g - g.shift(63), 126) - _z(pe, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_acceleveb2_252d_slope_v110_signal(evebitda, ebitda):
    g = _grw(ebitda, 126)
    base = _z(g - g.shift(63), 126) - _z(evebitda, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_accelps2_252d_slope_v111_signal(ps, revenue):
    g = _grw(revenue, 63)
    base = _z(g - g.shift(21), 63) - _z(ps, 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_marginvgeb2_252d_slope_v112_signal(ebitda, revenue, evebitda):
    margin = _safe_div(ebitda, revenue)
    base = _z(margin, 252) + _z(_grw(ebitda, 252), 126) - _z(evebitda, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_nmvgpe2_252d_slope_v113_signal(netinc, revenue, pe):
    nm = _safe_div(netinc, revenue)
    base = _z(nm, 126) + _z(_grw(netinc, 252), 252) - _z(pe, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fmvgevs2_252d_slope_v114_signal(fcf, revenue, ev):
    fm = _safe_div(fcf, revenue)
    evs = _evsales(ev, revenue)
    base = _z(fm, 252) + _z(_grw(fcf, 252), 126) - _z(evs, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ranksumpe2_252d_slope_v115_signal(pe, revenue):
    base = _rank(_grw(revenue, 252), 504) - _rank(pe, 504)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ranksumeveb2_252d_slope_v116_signal(evebitda, ebitda):
    base = _rank(_grw(ebitda, 252), 504) - _rank(evebitda, 504)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ranksumps2_252d_slope_v117_signal(ps, netinc):
    base = _rank(_grw(netinc, 252), 504) - _rank(ps, 504)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_ranksumevs2_252d_slope_v118_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    base = _rank(_grw(fcf, 252), 504) - _rank(evs, 504)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_megapevrev2_252d_slope_v119_signal(pe, evebitda, revenue, ebitda):
    base = -(_z(pe, 252) + _z(evebitda, 252)) + (_z(_grw(revenue, 252), 252) + _z(_grw(ebitda, 252), 252))
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_megapsfcf2_252d_slope_v120_signal(ps, ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    base = -(_z(ps, 252) + _z(evs, 252)) + (_z(_grw(revenue, 504), 252) + _z(_grw(fcf, 252), 252))
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_megayield2_252d_slope_v121_signal(netinc, fcf, marketcap, revenue, ebitda):
    base = _z(_earnyield(netinc, marketcap), 252) + _z(_fcfyield(fcf, marketcap), 252) + _z(_grw(revenue, 252), 126) + _z(_grw(ebitda, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_sizepe2_252d_slope_v122_signal(pe, revenue, marketcap):
    base = (-_z(pe, 252) + _z(_grw(revenue, 252), 252)) * (0.5 - _rank(np.log(marketcap.replace(0, np.nan)), 504))
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_sizeeveb2_252d_slope_v123_signal(evebitda, ebitda, marketcap):
    base = (-_z(evebitda, 252) + _z(_grw(ebitda, 252), 252)) - _rank(np.log(marketcap.replace(0, np.nan)), 504)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_tanhpe2_252d_slope_v124_signal(pe, revenue):
    base = np.tanh(0.5 * (-_z(pe, 252) + _z(_grw(revenue, 252), 252)))
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_tanheveb2_252d_slope_v125_signal(evebitda, ebitda):
    base = np.tanh(0.5 * (-_z(evebitda, 252) + _z(_grw(ebitda, 252), 252)))
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_tanhfcf2_252d_slope_v126_signal(pe, fcf, marketcap):
    base = np.tanh(0.4 * (_z(_fcfyield(fcf, marketcap), 252) + _z(_grw(fcf, 252), 252) - _z(pe, 252)))
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fairpez2_252d_slope_v127_signal(pe, revenue):
    base = _z(pe - _grw(revenue, 252) * 100.0, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fairevebz2_252d_slope_v128_signal(evebitda, ebitda):
    base = _z(evebitda - 0.5 * _grw(ebitda, 252) * 100.0, 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fairpsz2_252d_slope_v129_signal(ps, revenue):
    base = _z(ps - 0.2 * _grw(revenue, 504) * 100.0, 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fairevsz2_252d_slope_v130_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    base = _z(evs - (1.0 + 2.0 * _grw(fcf, 252)), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_consistpe2_252d_slope_v131_signal(pe, revenue):
    g = _grw(revenue, 63)
    consist = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    base = consist - _z(pe, 252) * 0.5
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_consisteveb2_252d_slope_v132_signal(evebitda, ebitda):
    g = _grw(ebitda, 63)
    consist = (g > 0).astype(float).rolling(252, min_periods=126).mean()
    base = consist - _z(evebitda, 252) * 0.5
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_horizpe2_252d_slope_v133_signal(pe, revenue):
    base = (-_z(pe, 252) + _z(_grw(revenue, 504), 252)) - (-_z(pe, 252) + _z(_grw(revenue, 252), 252))
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_horizeveb2_252d_slope_v134_signal(evebitda, ebitda):
    base = (-_z(evebitda, 252) + _z(_grw(ebitda, 504), 252)) - (-_z(evebitda, 252) + _z(_grw(ebitda, 252), 252))
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_durpe2_504d_slope_v135_signal(pe, revenue):
    base = -_z(_mean(pe, 252), 252) + _z(_grw(revenue, 504), 252)
    result = (base - base.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_dureveb2_504d_slope_v136_signal(evebitda, ebitda):
    base = -_z(_mean(evebitda, 252), 252) + _z(_grw(ebitda, 504), 252)
    result = (base - base.shift(126)) / 126.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_yielddisp2_252d_slope_v137_signal(netinc, fcf, ebitda, marketcap, ev):
    ey = _z(_earnyield(netinc, marketcap), 252)
    fy = _z(_fcfyield(fcf, marketcap), 252)
    eby = _z(_ebitda_yield(ebitda, ev), 252)
    base = pd.concat([ey, fy, eby], axis=1).std(axis=1)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_compintz2_252d_slope_v138_signal(marketcap, revenue, ebitda):
    sy = _safe_div(revenue, marketcap)
    margin = _safe_div(ebitda, revenue)
    base = _z(sy * margin * (1.0 + _grw(revenue, 252)), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_qualintz2_252d_slope_v139_signal(netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    nm = _safe_div(netinc, revenue)
    base = _z(ey * (1.0 + nm) * (1.0 + _grw(netinc, 252)), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_cashintz2_252d_slope_v140_signal(fcf, marketcap, revenue):
    fy = _fcfyield(fcf, marketcap)
    fm = _safe_div(fcf, revenue)
    base = _z(fy * (1.0 + fm) * (1.0 + _grw(fcf, 252)), 252)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_reratepe2_252d_slope_v141_signal(pe, netinc):
    base = _z(pe / pe.shift(63) - 1.0, 126) - _z(_grw(netinc, 63), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_rerateeveb2_252d_slope_v142_signal(evebitda, ebitda):
    base = _z(evebitda / evebitda.shift(63) - 1.0, 126) - _z(_grw(ebitda, 63), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_rerateevs2_252d_slope_v143_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    base = _z(evs / evs.shift(63) - 1.0, 126) - _z(_grw(revenue, 63), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastpe2_63d_slope_v144_signal(pe, revenue):
    base = -_z(pe, 63) + _z(_grw(revenue, 63), 63)
    result = (base - base.shift(5)) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fasteveb2_63d_slope_v145_signal(evebitda, ebitda):
    base = -_z(evebitda, 63) + _z(_grw(ebitda, 63), 63)
    result = (base - base.shift(5)) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastps2_63d_slope_v146_signal(ps, revenue):
    base = -_z(ps, 63) + _z(_grw(revenue, 63), 63)
    result = (base - base.shift(5)) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastni2_63d_slope_v147_signal(pe, netinc):
    base = -_z(pe, 63) + _z(_grw(netinc, 63), 63)
    result = (base - base.shift(5)) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastevs2_63d_slope_v148_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    base = -_z(evs, 63) + _z(_grw(revenue, 63), 63)
    result = (base - base.shift(5)) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_fastfcf2_63d_slope_v149_signal(pe, fcf):
    base = -_z(pe, 63) + _z(_grw(fcf, 63), 63)
    result = (base - base.shift(5)) / 5.0
    return result.replace([np.inf, -np.inf], np.nan)


def f40vg_f40_valuation_vs_growth_psvfcf2_252d_slope_v150_signal(ps, fcf):
    base = -_z(ps, 252) + _z(_grw(fcf, 252), 126)
    result = (base - base.shift(21)) / 21.0
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40vg_f40_valuation_vs_growth_pevrev_252d_slope_v001_signal,
    f40vg_f40_valuation_vs_growth_pevni_252d_slope_v002_signal,
    f40vg_f40_valuation_vs_growth_pevfcf_252d_slope_v003_signal,
    f40vg_f40_valuation_vs_growth_pevebitda_126d_slope_v004_signal,
    f40vg_f40_valuation_vs_growth_evebvrev_252d_slope_v005_signal,
    f40vg_f40_valuation_vs_growth_evebveb_252d_slope_v006_signal,
    f40vg_f40_valuation_vs_growth_evebvfcf_252d_slope_v007_signal,
    f40vg_f40_valuation_vs_growth_evebvni_126d_slope_v008_signal,
    f40vg_f40_valuation_vs_growth_psvrev_252d_slope_v009_signal,
    f40vg_f40_valuation_vs_growth_psveb_252d_slope_v010_signal,
    f40vg_f40_valuation_vs_growth_psvni_252d_slope_v011_signal,
    f40vg_f40_valuation_vs_growth_evsvrev_252d_slope_v012_signal,
    f40vg_f40_valuation_vs_growth_evsveb_252d_slope_v013_signal,
    f40vg_f40_valuation_vs_growth_evsvfcf_252d_slope_v014_signal,
    f40vg_f40_valuation_vs_growth_eyr40rev_252d_slope_v015_signal,
    f40vg_f40_valuation_vs_growth_eyr40ni_252d_slope_v016_signal,
    f40vg_f40_valuation_vs_growth_fyr40rev_252d_slope_v017_signal,
    f40vg_f40_valuation_vs_growth_fyr40eb_252d_slope_v018_signal,
    f40vg_f40_valuation_vs_growth_fyr40fcf_252d_slope_v019_signal,
    f40vg_f40_valuation_vs_growth_ebyr40eb_252d_slope_v020_signal,
    f40vg_f40_valuation_vs_growth_ebyr40rev_252d_slope_v021_signal,
    f40vg_f40_valuation_vs_growth_syr40rev_252d_slope_v022_signal,
    f40vg_f40_valuation_vs_growth_syr40eb_252d_slope_v023_signal,
    f40vg_f40_valuation_vs_growth_divpe_252d_slope_v024_signal,
    f40vg_f40_valuation_vs_growth_diveveb_252d_slope_v025_signal,
    f40vg_f40_valuation_vs_growth_divps_252d_slope_v026_signal,
    f40vg_f40_valuation_vs_growth_divevs_252d_slope_v027_signal,
    f40vg_f40_valuation_vs_growth_diveyrev_252d_slope_v028_signal,
    f40vg_f40_valuation_vs_growth_divfyeb_252d_slope_v029_signal,
    f40vg_f40_valuation_vs_growth_oplevev_252d_slope_v030_signal,
    f40vg_f40_valuation_vs_growth_cashqualpe_252d_slope_v031_signal,
    f40vg_f40_valuation_vs_growth_grwsprps_252d_slope_v032_signal,
    f40vg_f40_valuation_vs_growth_grwsprev_252d_slope_v033_signal,
    f40vg_f40_valuation_vs_growth_accelpe_252d_slope_v034_signal,
    f40vg_f40_valuation_vs_growth_acceleveb_252d_slope_v035_signal,
    f40vg_f40_valuation_vs_growth_accelps_252d_slope_v036_signal,
    f40vg_f40_valuation_vs_growth_marginvgeb_252d_slope_v037_signal,
    f40vg_f40_valuation_vs_growth_nmvgpe_252d_slope_v038_signal,
    f40vg_f40_valuation_vs_growth_fmvgevs_252d_slope_v039_signal,
    f40vg_f40_valuation_vs_growth_ranksumpe_252d_slope_v040_signal,
    f40vg_f40_valuation_vs_growth_ranksumeveb_252d_slope_v041_signal,
    f40vg_f40_valuation_vs_growth_ranksumps_252d_slope_v042_signal,
    f40vg_f40_valuation_vs_growth_ranksumevs_252d_slope_v043_signal,
    f40vg_f40_valuation_vs_growth_megapevrev_252d_slope_v044_signal,
    f40vg_f40_valuation_vs_growth_megapsfcf_252d_slope_v045_signal,
    f40vg_f40_valuation_vs_growth_megayield_252d_slope_v046_signal,
    f40vg_f40_valuation_vs_growth_sizepe_252d_slope_v047_signal,
    f40vg_f40_valuation_vs_growth_sizeeveb_252d_slope_v048_signal,
    f40vg_f40_valuation_vs_growth_tanhpe_252d_slope_v049_signal,
    f40vg_f40_valuation_vs_growth_tanheveb_252d_slope_v050_signal,
    f40vg_f40_valuation_vs_growth_tanhfcf_252d_slope_v051_signal,
    f40vg_f40_valuation_vs_growth_fairpez_252d_slope_v052_signal,
    f40vg_f40_valuation_vs_growth_fairevebz_252d_slope_v053_signal,
    f40vg_f40_valuation_vs_growth_fairpsz_252d_slope_v054_signal,
    f40vg_f40_valuation_vs_growth_fairevsz_252d_slope_v055_signal,
    f40vg_f40_valuation_vs_growth_consistpe_252d_slope_v056_signal,
    f40vg_f40_valuation_vs_growth_consisteveb_252d_slope_v057_signal,
    f40vg_f40_valuation_vs_growth_horizpe_252d_slope_v058_signal,
    f40vg_f40_valuation_vs_growth_horizeveb_252d_slope_v059_signal,
    f40vg_f40_valuation_vs_growth_durpe_504d_slope_v060_signal,
    f40vg_f40_valuation_vs_growth_dureveb_504d_slope_v061_signal,
    f40vg_f40_valuation_vs_growth_yielddisp_252d_slope_v062_signal,
    f40vg_f40_valuation_vs_growth_compintz_252d_slope_v063_signal,
    f40vg_f40_valuation_vs_growth_qualintz_252d_slope_v064_signal,
    f40vg_f40_valuation_vs_growth_cashintz_252d_slope_v065_signal,
    f40vg_f40_valuation_vs_growth_reratepe_252d_slope_v066_signal,
    f40vg_f40_valuation_vs_growth_rerateeveb_252d_slope_v067_signal,
    f40vg_f40_valuation_vs_growth_rerateevs_252d_slope_v068_signal,
    f40vg_f40_valuation_vs_growth_fastpe_63d_slope_v069_signal,
    f40vg_f40_valuation_vs_growth_fasteveb_63d_slope_v070_signal,
    f40vg_f40_valuation_vs_growth_fastps_63d_slope_v071_signal,
    f40vg_f40_valuation_vs_growth_fastni_63d_slope_v072_signal,
    f40vg_f40_valuation_vs_growth_fastevs_63d_slope_v073_signal,
    f40vg_f40_valuation_vs_growth_fastfcf_63d_slope_v074_signal,
    f40vg_f40_valuation_vs_growth_psvfcf_252d_slope_v075_signal,
    f40vg_f40_valuation_vs_growth_pevrev2_252d_slope_v076_signal,
    f40vg_f40_valuation_vs_growth_pevni2_252d_slope_v077_signal,
    f40vg_f40_valuation_vs_growth_pevfcf2_252d_slope_v078_signal,
    f40vg_f40_valuation_vs_growth_pevebitda2_126d_slope_v079_signal,
    f40vg_f40_valuation_vs_growth_evebvrev2_252d_slope_v080_signal,
    f40vg_f40_valuation_vs_growth_evebveb2_252d_slope_v081_signal,
    f40vg_f40_valuation_vs_growth_evebvfcf2_252d_slope_v082_signal,
    f40vg_f40_valuation_vs_growth_evebvni2_126d_slope_v083_signal,
    f40vg_f40_valuation_vs_growth_psvrev2_252d_slope_v084_signal,
    f40vg_f40_valuation_vs_growth_psveb2_252d_slope_v085_signal,
    f40vg_f40_valuation_vs_growth_psvni2_252d_slope_v086_signal,
    f40vg_f40_valuation_vs_growth_evsvrev2_252d_slope_v087_signal,
    f40vg_f40_valuation_vs_growth_evsveb2_252d_slope_v088_signal,
    f40vg_f40_valuation_vs_growth_evsvfcf2_252d_slope_v089_signal,
    f40vg_f40_valuation_vs_growth_eyr40rev2_252d_slope_v090_signal,
    f40vg_f40_valuation_vs_growth_eyr40ni2_252d_slope_v091_signal,
    f40vg_f40_valuation_vs_growth_fyr40rev2_252d_slope_v092_signal,
    f40vg_f40_valuation_vs_growth_fyr40eb2_252d_slope_v093_signal,
    f40vg_f40_valuation_vs_growth_fyr40fcf2_252d_slope_v094_signal,
    f40vg_f40_valuation_vs_growth_ebyr40eb2_252d_slope_v095_signal,
    f40vg_f40_valuation_vs_growth_ebyr40rev2_252d_slope_v096_signal,
    f40vg_f40_valuation_vs_growth_syr40rev2_252d_slope_v097_signal,
    f40vg_f40_valuation_vs_growth_syr40eb2_252d_slope_v098_signal,
    f40vg_f40_valuation_vs_growth_divpe2_252d_slope_v099_signal,
    f40vg_f40_valuation_vs_growth_diveveb2_252d_slope_v100_signal,
    f40vg_f40_valuation_vs_growth_divps2_252d_slope_v101_signal,
    f40vg_f40_valuation_vs_growth_divevs2_252d_slope_v102_signal,
    f40vg_f40_valuation_vs_growth_diveyrev2_252d_slope_v103_signal,
    f40vg_f40_valuation_vs_growth_divfyeb2_252d_slope_v104_signal,
    f40vg_f40_valuation_vs_growth_oplevev2_252d_slope_v105_signal,
    f40vg_f40_valuation_vs_growth_cashqualpe2_252d_slope_v106_signal,
    f40vg_f40_valuation_vs_growth_grwsprps2_252d_slope_v107_signal,
    f40vg_f40_valuation_vs_growth_grwsprev2_252d_slope_v108_signal,
    f40vg_f40_valuation_vs_growth_accelpe2_252d_slope_v109_signal,
    f40vg_f40_valuation_vs_growth_acceleveb2_252d_slope_v110_signal,
    f40vg_f40_valuation_vs_growth_accelps2_252d_slope_v111_signal,
    f40vg_f40_valuation_vs_growth_marginvgeb2_252d_slope_v112_signal,
    f40vg_f40_valuation_vs_growth_nmvgpe2_252d_slope_v113_signal,
    f40vg_f40_valuation_vs_growth_fmvgevs2_252d_slope_v114_signal,
    f40vg_f40_valuation_vs_growth_ranksumpe2_252d_slope_v115_signal,
    f40vg_f40_valuation_vs_growth_ranksumeveb2_252d_slope_v116_signal,
    f40vg_f40_valuation_vs_growth_ranksumps2_252d_slope_v117_signal,
    f40vg_f40_valuation_vs_growth_ranksumevs2_252d_slope_v118_signal,
    f40vg_f40_valuation_vs_growth_megapevrev2_252d_slope_v119_signal,
    f40vg_f40_valuation_vs_growth_megapsfcf2_252d_slope_v120_signal,
    f40vg_f40_valuation_vs_growth_megayield2_252d_slope_v121_signal,
    f40vg_f40_valuation_vs_growth_sizepe2_252d_slope_v122_signal,
    f40vg_f40_valuation_vs_growth_sizeeveb2_252d_slope_v123_signal,
    f40vg_f40_valuation_vs_growth_tanhpe2_252d_slope_v124_signal,
    f40vg_f40_valuation_vs_growth_tanheveb2_252d_slope_v125_signal,
    f40vg_f40_valuation_vs_growth_tanhfcf2_252d_slope_v126_signal,
    f40vg_f40_valuation_vs_growth_fairpez2_252d_slope_v127_signal,
    f40vg_f40_valuation_vs_growth_fairevebz2_252d_slope_v128_signal,
    f40vg_f40_valuation_vs_growth_fairpsz2_252d_slope_v129_signal,
    f40vg_f40_valuation_vs_growth_fairevsz2_252d_slope_v130_signal,
    f40vg_f40_valuation_vs_growth_consistpe2_252d_slope_v131_signal,
    f40vg_f40_valuation_vs_growth_consisteveb2_252d_slope_v132_signal,
    f40vg_f40_valuation_vs_growth_horizpe2_252d_slope_v133_signal,
    f40vg_f40_valuation_vs_growth_horizeveb2_252d_slope_v134_signal,
    f40vg_f40_valuation_vs_growth_durpe2_504d_slope_v135_signal,
    f40vg_f40_valuation_vs_growth_dureveb2_504d_slope_v136_signal,
    f40vg_f40_valuation_vs_growth_yielddisp2_252d_slope_v137_signal,
    f40vg_f40_valuation_vs_growth_compintz2_252d_slope_v138_signal,
    f40vg_f40_valuation_vs_growth_qualintz2_252d_slope_v139_signal,
    f40vg_f40_valuation_vs_growth_cashintz2_252d_slope_v140_signal,
    f40vg_f40_valuation_vs_growth_reratepe2_252d_slope_v141_signal,
    f40vg_f40_valuation_vs_growth_rerateeveb2_252d_slope_v142_signal,
    f40vg_f40_valuation_vs_growth_rerateevs2_252d_slope_v143_signal,
    f40vg_f40_valuation_vs_growth_fastpe2_63d_slope_v144_signal,
    f40vg_f40_valuation_vs_growth_fasteveb2_63d_slope_v145_signal,
    f40vg_f40_valuation_vs_growth_fastps2_63d_slope_v146_signal,
    f40vg_f40_valuation_vs_growth_fastni2_63d_slope_v147_signal,
    f40vg_f40_valuation_vs_growth_fastevs2_63d_slope_v148_signal,
    f40vg_f40_valuation_vs_growth_fastfcf2_63d_slope_v149_signal,
    f40vg_f40_valuation_vs_growth_psvfcf2_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_VALUATION_VS_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False, n=1500):
    g = np.random.default_rng(seed)
    steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
    s = base * np.exp(np.cumsum(steps / 63))
    if allow_neg:
        s = s - base * 0.3
    return pd.Series(s, name=None)


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    pe = _fund(1, base=20.0, drift=0.01, vol=0.06).rename("pe")
    evebitda = _fund(2, base=12.0, drift=0.01, vol=0.06).rename("evebitda")
    ps = _fund(3, base=4.0, drift=0.01, vol=0.06).rename("ps")
    marketcap = _fund(4, base=5e9, drift=0.02, vol=0.05).rename("marketcap")
    ev = _fund(5, base=6e9, drift=0.02, vol=0.05).rename("ev")
    revenue = _fund(6, base=1e9, drift=0.03, vol=0.04).rename("revenue")
    ebitda = _fund(7, base=2e8, drift=0.03, vol=0.05).rename("ebitda")
    netinc = _fund(8, base=1.2e8, drift=0.025, vol=0.06, allow_neg=True).rename("netinc")
    fcf = _fund(9, base=1e8, drift=0.025, vol=0.06, allow_neg=True).rename("fcf")

    cols = {"pe": pe, "evebitda": evebitda, "ps": ps, "marketcap": marketcap,
            "ev": ev, "revenue": revenue, "ebitda": ebitda, "netinc": netinc,
            "fcf": fcf}

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

    print("OK f40_valuation_vs_growth_2nd_derivatives_001_150_claude: %d features pass" % n_features)
