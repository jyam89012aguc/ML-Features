import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _median(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).median()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _growth(s, w):
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _log_growth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _peg(mult, growth_pct):
    return mult / (growth_pct * 100.0).replace(0, np.nan)


def _fcf_yield(fcf, marketcap):
    return fcf / marketcap.replace(0, np.nan)


def _rule40_mult(mult, growth_pct, margin):
    r40 = growth_pct + margin
    return mult / (1.0 + r40)


def _roc(s, w):
    return s - s.shift(w)


def f44vg_f44_valuation_vs_growth_d001_63d_slope_v001_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    b = _peg(evs, g)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d002_63d_slope_v002_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 126)
    b = _z(_peg(evs, g), 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d003_126d_slope_v003_signal(ps, revenue):
    g = _growth(revenue, 252)
    b = _rank(_peg(ps, g), 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d004_21d_slope_v004_signal(ps, revenue):
    g = _growth(revenue, 63)
    peg = _peg(ps, g)
    b = peg - peg.shift(21)
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d005_63d_slope_v005_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    b = _peg(evebitda, g)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d006_63d_slope_v006_signal(evebitda, revenue):
    g = _growth(revenue, 252)
    b = _z(_peg(evebitda, g), 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d007_63d_slope_v007_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    b = yld + g
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d008_63d_slope_v008_signal(fcf, marketcap, ebitda):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(ebitda, 252)
    b = _z(yld + g, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d009_63d_slope_v009_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    b = _rule40_mult(evs, g, margin)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d010_63d_slope_v010_signal(ps, revenue, fcf):
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    r = _rule40_mult(ps, g, margin)
    b = r - r.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d011_63d_slope_v011_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    b = g - _z(evs, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d012_63d_slope_v012_signal(ps, revenue):
    g = _z(_growth(revenue, 252), 252)
    v = -_z(ps, 252)
    b = np.sign(g + v) * (g.abs() + v.abs())
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d013_63d_slope_v013_signal(evebitda, ebitda):
    g = _z(_growth(ebitda, 252), 252)
    b = g - _z(evebitda, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d014_63d_slope_v014_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    p1 = _peg(evs, _growth(revenue, 63))
    p2 = _peg(evs, _growth(revenue, 126))
    p3 = _peg(evs, _growth(revenue, 252))
    b = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d015_63d_slope_v015_signal(ps, revenue):
    g = _growth(revenue, 252)
    peg = _peg(ps, g)
    sub1 = ((peg > 0) & (peg < 1.0)).astype(float)
    b = sub1.rolling(252, min_periods=63).mean()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d016_63d_slope_v016_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    peg = _peg(evs, g)
    b = peg - peg.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d017_63d_slope_v017_signal(ps, revenue):
    g = _growth(revenue, 252)
    peg = _peg(ps, g)
    b = peg - 2.0 * peg.shift(42) + peg.shift(84)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d018_21d_slope_v018_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    dmult = _log_growth(evs, 63)
    dgro = _log_growth(revenue, 63)
    b = dmult - dgro
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d019_63d_slope_v019_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    implied = (1.0 + g).clip(lower=0.0) * _mean(evs, 252)
    b = (evs - implied) / implied.replace(0, np.nan)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d020_63d_slope_v020_signal(ev, ps, revenue):
    evs = _evsales(ev, revenue)
    gz = _z(_growth(revenue, 252), 252)
    b = gz - (_z(evs, 252) + _z(ps, 252)) / 2.0
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d021_63d_slope_v021_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    inv = (g * 100.0) / evs.replace(0, np.nan)
    b = inv - _mean(inv, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d022_126d_slope_v022_signal(ps, revenue):
    g = _growth(revenue, 252)
    inv = (g * 100.0) / ps.replace(0, np.nan)
    b = _rank(inv, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d023_126d_slope_v023_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    inv = (g * 100.0) / evebitda.replace(0, np.nan)
    b = _rank(inv, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d024_63d_slope_v024_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    cg = yld + g
    b = cg - cg.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d025_63d_slope_v025_signal(revenue, fcf):
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    r40 = g + margin
    excess = r40 - 0.40
    b = excess.ewm(span=63, min_periods=21).mean()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d026_126d_slope_v026_signal(ev, revenue, fcf):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    r = (g + margin) / evs.replace(0, np.nan)
    b = _rank(r, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d027_42d_slope_v027_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = (g_now - g_prev)
    b = evs / (accel * 100.0).replace(0, np.nan)
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d028_63d_slope_v028_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    sign = (g > 0).astype(float)
    b = -_z(evs, 126) * sign
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d029_63d_slope_v029_signal(evebitda, ebitda, revenue):
    geb = _growth(ebitda, 252)
    g = geb.where(geb.abs() > 0.01, _growth(revenue, 252))
    peg = _peg(evebitda, g)
    b = peg - peg.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d030_63d_slope_v030_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    gz = _z(_growth(revenue, 126), 252)
    vz = _z(evs, 252)
    b = gz - vz
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d031_63d_slope_v031_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    b = yld / (g.abs() + 0.05) * np.sign(g)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d032_63d_slope_v032_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    cheap = ((evs < _median(evs, 252)) & (g > 0)).astype(float)
    b = cheap.rolling(63, min_periods=21).mean()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d033_63d_slope_v033_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    disc = _mean(evs, 252) / evs.replace(0, np.nan) - 1.0
    b = disc * (1.0 + g.clip(lower=0))
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d034_63d_slope_v034_signal(ps, ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    b = (evs - ps) / (g.abs() * 100.0 + 1.0)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d035_126d_slope_v035_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    disc = _mean(evebitda, 504) / evebitda.replace(0, np.nan) - 1.0
    score = disc + g
    b = score - score.shift(63)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d036_126d_slope_v036_signal(ev, revenue):
    g = _growth(revenue, 252)
    fwd_rev = revenue * (1.0 + g)
    evs_fwd = ev / fwd_rev.replace(0, np.nan)
    b = _rank(evs_fwd, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d037_63d_slope_v037_signal(ps, revenue):
    g = _growth(revenue, 252)
    fwd_ps = ps / (1.0 + g).replace(0, np.nan)
    comp = (ps - fwd_ps) / ps.replace(0, np.nan)
    b = _z(comp, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d038_63d_slope_v038_signal(ev, revenue, evebitda, ebitda):
    evs = _evsales(ev, revenue)
    gz = (_z(_growth(revenue, 252), 252) + _z(_growth(ebitda, 252), 252)) / 2.0
    vz = (_z(evs, 252) + _z(evebitda, 252)) / 2.0
    b = gz - vz
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d039_126d_slope_v039_signal(ev, ps, revenue):
    evs = _evsales(ev, revenue)
    p1 = _peg(evs, _growth(revenue, 63))
    p2 = _peg(evs, _growth(revenue, 126))
    p3 = _peg(ps, _growth(revenue, 252))
    disp = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    b = _rank(disp, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d040_63d_slope_v040_signal(fcf, marketcap, ebitda):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(ebitda, 252)
    pos = (yld + g > 0).astype(float)
    b = pos.rolling(252, min_periods=63).mean() - 0.5
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d041_126d_slope_v041_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    cagr = (revenue / revenue.shift(504).replace(0, np.nan)) ** (252.0 / 504.0) - 1.0
    b = _peg(evs, cagr)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d042_126d_slope_v042_signal(ps, revenue):
    cagr = (revenue / revenue.shift(504).replace(0, np.nan)) ** (252.0 / 504.0) - 1.0
    peg = _peg(ps, cagr)
    b = peg - peg.shift(63)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d043_63d_slope_v043_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 63)
    gvol = _std(g, 252)
    b = -evs / (1.0 + gvol * 5.0)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d044_126d_slope_v044_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    required = evs / _mean(evs, 504).replace(0, np.nan) - 1.0
    delivered = _growth(revenue, 252)
    b = delivered - required
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d045_63d_slope_v045_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    peg = _peg(evebitda, g)
    b = peg - 2.0 * peg.shift(42) + peg.shift(84)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d046_126d_slope_v046_signal(fcf, marketcap, revenue, ev):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    evs = _evsales(ev, revenue)
    raw = (yld + g) - _z(evs, 252)
    b = _rank(raw, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d047_126d_slope_v047_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    med = _median(peg, 504)
    sd = _std(peg, 504)
    b = (peg - med) / sd.replace(0, np.nan)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d048_63d_slope_v048_signal(marketcap, revenue):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    inv = (g * 100.0) / mc_rev.replace(0, np.nan)
    b = inv - inv.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d049_63d_slope_v049_signal(evebitda, ebitda, revenue):
    margin = _safe_div(ebitda, revenue)
    dmargin = margin - margin.shift(252)
    b = -evebitda / (1.0 + (dmargin * 10.0).clip(lower=-0.9))
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d050_126d_slope_v050_signal(evebitda, revenue):
    g = _growth(revenue, 252)
    cross = (g * 100.0) / evebitda.replace(0, np.nan)
    b = (cross - _median(cross, 504)) / _std(cross, 504).replace(0, np.nan)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d051_63d_slope_v051_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    depth = (1.0 - peg).where(peg > 0, np.nan).clip(lower=0)
    b = depth.rolling(126, min_periods=42).mean()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d052_63d_slope_v052_signal(ev, revenue):
    g = _log_growth(revenue, 252)
    de = _log_growth(ev, 252)
    b = g - de
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d053_63d_slope_v053_signal(ps, revenue):
    cheap = -_z(ps, 252)
    g = _z(_growth(revenue, 252), 252)
    b = np.sign(cheap) * np.sign(g) * (cheap.abs() * g.abs()) ** 0.5
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d054_42d_slope_v054_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = g_now - g_prev
    b = yld * (1.0 + accel.clip(lower=-0.5))
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d055_63d_slope_v055_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    b = _std(peg.pct_change(), 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d056_42d_slope_v056_signal(ps, evebitda, revenue, ebitda):
    vz = (_z(ps, 126) + _z(evebitda, 126)) / 2.0
    gz = (_z(_growth(revenue, 126), 126) + _z(_growth(ebitda, 126), 126)) / 2.0
    b = gz - vz
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d057_126d_slope_v057_signal(ps, revenue):
    g = _growth(revenue, 252)
    peg = _peg(ps, g)
    above = (peg > _median(peg, 504)).astype(float)
    b = above.rolling(252, min_periods=63).mean() - 0.5
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d058_63d_slope_v058_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    implied = (1.0 + g).clip(lower=0.0) * _mean(evebitda, 252)
    b = (evebitda - implied) / implied.replace(0, np.nan)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d059_63d_slope_v059_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    raw = g - _z(evs, 252)
    b = raw.ewm(span=42, min_periods=21).mean()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d060_63d_slope_v060_signal(evebitda, ebitda, revenue):
    g = _growth(ebitda, 252)
    margin = _safe_div(ebitda, revenue)
    r = _rule40_mult(evebitda, g, margin)
    b = r - r.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d061_63d_slope_v061_signal(marketcap, revenue, fcf):
    g = _growth(revenue, 252)
    mc_rev = _safe_div(marketcap, revenue)
    yld = _fcf_yield(fcf, marketcap)
    raw = (g / mc_rev.replace(0, np.nan)) + yld
    b = _z(raw, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d062_126d_slope_v062_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    b = _rank(peg, 504) - _rank(peg, 63)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d063_63d_slope_v063_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    vz = _z(evs, 252)
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = g_now - g_prev
    b = (-vz).clip(lower=0) * accel
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d064_126d_slope_v064_signal(marketcap, fcf, revenue):
    pfcf = _safe_div(marketcap, fcf)
    g = _growth(revenue, 252)
    peg = pfcf / (g * 100.0).replace(0, np.nan)
    b = _rank(peg, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d065_63d_slope_v065_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    disc = -_z(evs, 252)
    margin = _safe_div(ebitda, revenue)
    dmargin = margin - margin.shift(126)
    b = disc * np.sign(dmargin) * (dmargin.abs() * 10.0)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d066_126d_slope_v066_signal(ev, revenue):
    rev_grow = revenue - revenue.shift(252)
    yld = _safe_div(rev_grow, ev)
    b = _z(yld, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d067_63d_slope_v067_signal(ev, ps, evebitda, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    p1 = _peg(evs, g)
    p2 = _peg(ps, g)
    p3 = _peg(evebitda, g)
    stk = pd.concat([p1, p2, p3], axis=1)
    cv = stk.std(axis=1) / stk.mean(axis=1).replace(0, np.nan)
    b = _z(cv, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d068_63d_slope_v068_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 63)
    stability = 1.0 / (1.0 + _std(g, 252) * 5.0)
    raw = stability * (-_z(evs, 252))
    b = raw - raw.ewm(span=63, min_periods=21).mean()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d069_63d_slope_v069_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    peg = _peg(evebitda, g)
    b = np.tanh(peg / 2.0)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d070_126d_slope_v070_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    cg = yld + g
    b = cg - _mean(cg, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d071_63d_slope_v071_signal(marketcap, revenue):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    peg = mc_rev / (g * 100.0).replace(0, np.nan)
    b = np.tanh((peg - 1.0) / 3.0)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d072_63d_slope_v072_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    inv = (g * 100.0) / evs.replace(0, np.nan)
    b = inv - inv.shift(252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d073_63d_slope_v073_signal(evebitda, ebitda):
    gz = _z(_growth(ebitda, 126), 252)
    vz = _z(evebitda, 252)
    b = gz - vz
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d074_63d_slope_v074_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    score = g - _z(evs, 252)
    b = score - score.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d075_126d_slope_v075_signal(ev, ps, evebitda, revenue, ebitda):
    g_rev = _growth(revenue, 252) * 100.0
    g_eb = _growth(ebitda, 252) * 100.0
    evs = _evsales(ev, revenue)
    a = g_rev / evs.replace(0, np.nan)
    b = g_rev / ps.replace(0, np.nan)
    c = g_eb / evebitda.replace(0, np.nan)
    blended = (a + b + c) / 3.0
    b = _rank(blended, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d076_126d_slope_v076_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 126)
    b = _rank(_peg(evs, g), 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d077_126d_slope_v077_signal(ps, revenue):
    g = _growth(revenue, 126)
    b = _z(_peg(ps, g), 252)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d078_42d_slope_v078_signal(evebitda, ebitda):
    g = _growth(ebitda, 126)
    b = _peg(evebitda, g)
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d079_21d_slope_v079_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 504)
    b = _peg(evs, g)
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d080_126d_slope_v080_signal(marketcap, revenue):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    b = _rank(_peg(mc_rev, g), 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d081_42d_slope_v081_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 126)
    b = yld + g
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d082_63d_slope_v082_signal(ev, evebitda, revenue, ebitda):
    p_sales = _peg(_evsales(ev, revenue), _growth(revenue, 252))
    p_prof = _peg(evebitda, _growth(ebitda, 252))
    b = p_prof - p_sales
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d083_42d_slope_v083_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 126)
    b = g - _z(evs, 126)
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d084_63d_slope_v084_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    b = peg - peg.shift(21)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d085_126d_slope_v085_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 252))
    lo = peg.rolling(504, min_periods=126).min()
    b = (peg - lo) / lo.abs().replace(0, np.nan)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d086_126d_slope_v086_signal(evebitda, ebitda):
    peg = _peg(evebitda, _growth(ebitda, 252))
    hi = peg.rolling(504, min_periods=126).max()
    b = (hi - peg) / hi.abs().replace(0, np.nan)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d087_63d_slope_v087_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 126)
    inv = (g * 100.0) / evs.replace(0, np.nan)
    b = _z(inv, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d088_42d_slope_v088_signal(ps, revenue):
    g = _growth(revenue, 126)
    inv = (g * 100.0) / ps.replace(0, np.nan)
    b = inv - inv.shift(63)
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d089_126d_slope_v089_signal(ev, marketcap, revenue):
    g = _growth(revenue, 252)
    p_ev = _peg(_evsales(ev, revenue), g)
    p_mc = _peg(_safe_div(marketcap, revenue), g)
    spread = p_ev - p_mc
    b = spread - spread.shift(63)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d090_42d_slope_v090_signal(ps, evebitda, revenue):
    gz = _z(_growth(revenue, 126), 126)
    vz = (_z(ps, 126) + _z(evebitda, 126)) / 2.0
    b = gz - vz
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d091_63d_slope_v091_signal(revenue, ebitda):
    g = _growth(revenue, 252)
    margin = _safe_div(ebitda, revenue)
    b = g + margin
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d092_126d_slope_v092_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    margin = _safe_div(ebitda, revenue)
    r = (g + margin) / evs.replace(0, np.nan)
    b = _rank(r, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d093_63d_slope_v093_signal(fcf, marketcap):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(fcf, 252)
    b = yld + np.tanh(g)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d094_126d_slope_v094_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = _growth(ebitda, 252)
    b = g - _z(evs, 252)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d095_126d_slope_v095_signal(ps, ebitda):
    g = _growth(ebitda, 252)
    raw = g - _z(ps, 252)
    b = _rank(raw, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d096_63d_slope_v096_signal(evebitda, revenue):
    g = _growth(revenue, 252)
    b = g - _z(evebitda, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d097_42d_slope_v097_signal(ev, revenue):
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = g_now - g_prev
    evs = _evsales(ev, revenue)
    rerate = _log_growth(evs, 126)
    b = accel - rerate
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d098_21d_slope_v098_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 63) * 4.0
    b = _peg(evs, g)
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d099_63d_slope_v099_signal(fcf, marketcap, revenue, ebitda):
    yld = _fcf_yield(fcf, marketcap)
    a = yld + _growth(revenue, 252)
    b = yld + _growth(ebitda, 252)
    b = (a - b).abs()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d100_63d_slope_v100_signal(ev, ps, revenue):
    g = _growth(revenue, 252)
    p1 = _peg(_evsales(ev, revenue), g)
    p2 = _peg(ps, g)
    b = p1 / p2.replace(0, np.nan)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d101_63d_slope_v101_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    raw = g - _z(evs, 252)
    b = raw.ewm(span=21, min_periods=10).mean() - raw.ewm(span=84, min_periods=21).mean()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d102_126d_slope_v102_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 504)
    implied = (1.0 + g).clip(lower=0.0) * _mean(evs, 504)
    b = (evs - implied) / implied.replace(0, np.nan)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d103_126d_slope_v103_signal(evebitda, ebitda, revenue):
    margin = _safe_div(ebitda, revenue)
    dmargin = margin - margin.shift(252)
    cheap = -_z(evebitda, 252)
    b = cheap + dmargin * 8.0
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d104_63d_slope_v104_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    good = ((yld > 0) & (g > 0)).astype(float)
    b = good.rolling(252, min_periods=63).mean() - 0.5
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d105_63d_slope_v105_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    b = peg - 2.0 * peg.shift(63) + peg.shift(126)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d106_63d_slope_v106_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    inv = (g * 100.0) / evebitda.replace(0, np.nan)
    b = inv - inv.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d107_63d_slope_v107_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    disc = _mean(evs, 252) / evs.replace(0, np.nan) - 1.0
    g = _growth(ebitda, 252)
    b = disc * (1.0 + g.clip(lower=0))
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d108_63d_slope_v108_signal(ev, evebitda, revenue, ebitda):
    p1 = _peg(_evsales(ev, revenue), _growth(revenue, 252))
    p2 = _peg(evebitda, _growth(ebitda, 252))
    b = (p1 + p2) / 2.0
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d109_126d_slope_v109_signal(ev, ps, revenue):
    g = _growth(revenue, 252)
    p1 = _peg(_evsales(ev, revenue), g)
    p2 = _peg(ps, g)
    blended = (p1 + p2) / 2.0
    b = _z(blended, 252)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d110_21d_slope_v110_signal(fcf, marketcap, ebitda, evebitda):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(ebitda, 252)
    b = (yld + g) - _z(evebitda, 252)
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d111_63d_slope_v111_signal(ev, ebitda):
    g = _log_growth(ebitda, 252)
    de = _log_growth(ev, 252)
    b = g - de
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d112_63d_slope_v112_signal(ps, revenue):
    cheap = -_z(ps, 252)
    g_now = _growth(revenue, 126)
    g_prev = _growth(revenue.shift(126), 126)
    accel = g_now - g_prev
    b = cheap * accel
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d113_63d_slope_v113_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    above = (peg > _median(peg, 252)).astype(float)
    b = above.rolling(63, min_periods=21).mean() - 0.5
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d114_126d_slope_v114_signal(marketcap, revenue):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    inv = (g * 100.0) / mc_rev.replace(0, np.nan)
    b = _z(inv, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d115_63d_slope_v115_signal(marketcap, revenue, fcf):
    mc_rev = _safe_div(marketcap, revenue)
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    b = _rule40_mult(mc_rev, g, margin)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d116_21d_slope_v116_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    b = np.tanh((peg - 1.0) / 3.0)
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d117_63d_slope_v117_signal(evebitda, ebitda):
    g63 = _growth(ebitda, 63)
    durability = 1.0 / (1.0 + _std(g63, 252) * 5.0)
    cheap = -_z(evebitda, 252)
    raw = cheap * durability
    b = raw - raw.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d118_63d_slope_v118_signal(evebitda, ebitda):
    p1 = _peg(evebitda, _growth(ebitda, 63))
    p2 = _peg(evebitda, _growth(ebitda, 126))
    p3 = _peg(evebitda, _growth(ebitda, 252))
    b = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d119_126d_slope_v119_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    b = (_rank(yld, 504) + _rank(g, 504))
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d120_126d_slope_v120_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    required = evs / _mean(evs, 504).replace(0, np.nan) - 1.0
    delivered = _growth(revenue, 252)
    gap = delivered - required
    b = _rank(gap, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d121_63d_slope_v121_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    score = g - _z(evs, 252)
    b = score - score.shift(252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d122_126d_slope_v122_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 252))
    below = (peg < _median(peg, 504)).astype(float)
    b = below.rolling(252, min_periods=63).mean() - 0.5
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d123_126d_slope_v123_signal(evebitda, ebitda, revenue):
    margin = _safe_div(ebitda, revenue)
    gmarg = margin - margin.shift(252)
    b = _rank(gmarg, 504) - _rank(evebitda, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d124_63d_slope_v124_signal(ev, evebitda, revenue, ebitda):
    a = (_growth(revenue, 252) * 100.0) / _evsales(ev, revenue).replace(0, np.nan)
    b = (_growth(ebitda, 252) * 100.0) / evebitda.replace(0, np.nan)
    b = a - b
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d125_21d_slope_v125_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    b = _rank(yld + g, 504)
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d126_63d_slope_v126_signal(ev, ps, revenue):
    g = _growth(revenue, 252)
    ratio = np.log(_peg(_evsales(ev, revenue), g).abs().replace(0, np.nan)
                   / _peg(ps, g).abs().replace(0, np.nan))
    b = ratio - ratio.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d127_63d_slope_v127_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    cheap = (-_z(evs, 252)).clip(lower=0)
    g = _growth(revenue, 252)
    b = cheap * g
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d128_63d_slope_v128_signal(evebitda, ebitda):
    cheap = (-_z(evebitda, 252)).clip(lower=0)
    g = _growth(ebitda, 252)
    b = cheap * g
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d129_21d_slope_v129_signal(evebitda, ebitda):
    g = _growth(ebitda, 252)
    fwd = evebitda / (1.0 + g).replace(0, np.nan)
    b = (evebitda - fwd) / evebitda.replace(0, np.nan)
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d130_63d_slope_v130_signal(revenue, fcf, evebitda):
    g = _growth(revenue, 252)
    margin = _safe_div(fcf, revenue)
    raw = (g + margin) - _z(evebitda, 252)
    b = raw.ewm(span=42, min_periods=21).mean() - raw
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d131_63d_slope_v131_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    b = _rank(peg, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d132_63d_slope_v132_signal(fcf, marketcap, revenue):
    gfcf = np.tanh(_growth(fcf, 252))
    cheap = -_z(_safe_div(marketcap, revenue), 252)
    b = gfcf + cheap
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d133_63d_slope_v133_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 252))
    disp = peg - peg.ewm(span=126, min_periods=42).mean()
    b = np.tanh(disp / _std(peg, 252).replace(0, np.nan))
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d134_63d_slope_v134_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 252))
    lo = peg.rolling(126, min_periods=42).min()
    gap = (peg - lo) / lo.abs().replace(0, np.nan)
    b = _rank(gap, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d135_126d_slope_v135_signal(ev, revenue):
    g = _log_growth(revenue, 252)
    de = _log_growth(ev, 252)
    b = _rank(g - de, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d136_63d_slope_v136_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _growth(revenue, 252)
    depth = (_mean(evs, 252) - evs).where(g > 0, np.nan)
    b = depth.rolling(126, min_periods=42).mean() / _mean(evs, 252).replace(0, np.nan)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d137_42d_slope_v137_signal(evebitda, ebitda):
    gz = _z(_growth(ebitda, 126), 126)
    vz = _z(evebitda, 126)
    b = gz - vz
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d138_63d_slope_v138_signal(ev, revenue, evebitda, ebitda):
    a = _growth(revenue, 252) - _z(_evsales(ev, revenue), 252)
    b = _growth(ebitda, 252) - _z(evebitda, 252)
    b = (a + b) / 2.0
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d139_126d_slope_v139_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 252))
    b = _rank(peg, 504) - _rank(peg, 63)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d140_63d_slope_v140_signal(fcf, marketcap, revenue):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    garp = yld * (1.0 + g.clip(lower=0))
    b = garp - garp.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d141_126d_slope_v141_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    peg = _peg(evs, _growth(revenue, 504))
    b = _rank(peg, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d142_42d_slope_v142_signal(ps, revenue):
    peg = _peg(ps, _growth(revenue, 126))
    b = peg - 2.0 * peg.shift(42) + peg.shift(84)
    result = _roc(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d143_63d_slope_v143_signal(ev, revenue):
    g = _growth(revenue, 63)
    stability = -_std(g, 252)
    evs = _evsales(ev, revenue)
    b = _z(stability, 252) - _z(evs, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d144_63d_slope_v144_signal(evebitda, ebitda):
    peg = _peg(evebitda, _growth(ebitda, 252))
    b = np.tanh(peg / 2.0)
    b = b - b.shift(63)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d145_126d_slope_v145_signal(ps, evebitda, revenue, ebitda):
    gz = (_z(_growth(revenue, 252), 252) + _z(_growth(ebitda, 252), 252)) / 2.0
    vz = (_z(ps, 252) + _z(evebitda, 252)) / 2.0
    b = _rank(gz - vz, 504)
    result = _roc(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d146_63d_slope_v146_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = pd.concat([_growth(revenue, 252), _growth(ebitda, 252)], axis=1).max(axis=1)
    b = _peg(evs, g)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d147_63d_slope_v147_signal(fcf, marketcap, revenue, ps):
    yld = _fcf_yield(fcf, marketcap)
    g = _growth(revenue, 252)
    b = (yld + g) - _z(ps, 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d148_63d_slope_v148_signal(ev, evebitda, revenue, ebitda):
    p1 = _peg(_evsales(ev, revenue), _growth(revenue, 252))
    p2 = _peg(evebitda, _growth(ebitda, 252))
    spread = p1 - p2
    b = spread.ewm(span=63, min_periods=21).mean()
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d149_63d_slope_v149_signal(ev, ps, revenue):
    g = _growth(revenue, 252) * 100.0
    a = g / _evsales(ev, revenue).replace(0, np.nan)
    b = g / ps.replace(0, np.nan)
    b = _z((a - b).abs(), 252)
    result = _roc(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f44vg_f44_valuation_vs_growth_d150_21d_slope_v150_signal(ev, ps, evebitda, revenue, ebitda, fcf, marketcap):
    g_rev = _growth(revenue, 252) * 100.0
    g_eb = _growth(ebitda, 252) * 100.0
    a = g_rev / _evsales(ev, revenue).replace(0, np.nan)
    b = g_rev / ps.replace(0, np.nan)
    c = g_eb / evebitda.replace(0, np.nan)
    yld = _fcf_yield(fcf, marketcap)
    composite = (a + b + c) / 3.0 + yld * 100.0
    b = _rank(composite, 504)
    result = _roc(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f44vg_f44_valuation_vs_growth_d001_63d_slope_v001_signal,
    f44vg_f44_valuation_vs_growth_d002_63d_slope_v002_signal,
    f44vg_f44_valuation_vs_growth_d003_126d_slope_v003_signal,
    f44vg_f44_valuation_vs_growth_d004_21d_slope_v004_signal,
    f44vg_f44_valuation_vs_growth_d005_63d_slope_v005_signal,
    f44vg_f44_valuation_vs_growth_d006_63d_slope_v006_signal,
    f44vg_f44_valuation_vs_growth_d007_63d_slope_v007_signal,
    f44vg_f44_valuation_vs_growth_d008_63d_slope_v008_signal,
    f44vg_f44_valuation_vs_growth_d009_63d_slope_v009_signal,
    f44vg_f44_valuation_vs_growth_d010_63d_slope_v010_signal,
    f44vg_f44_valuation_vs_growth_d011_63d_slope_v011_signal,
    f44vg_f44_valuation_vs_growth_d012_63d_slope_v012_signal,
    f44vg_f44_valuation_vs_growth_d013_63d_slope_v013_signal,
    f44vg_f44_valuation_vs_growth_d014_63d_slope_v014_signal,
    f44vg_f44_valuation_vs_growth_d015_63d_slope_v015_signal,
    f44vg_f44_valuation_vs_growth_d016_63d_slope_v016_signal,
    f44vg_f44_valuation_vs_growth_d017_63d_slope_v017_signal,
    f44vg_f44_valuation_vs_growth_d018_21d_slope_v018_signal,
    f44vg_f44_valuation_vs_growth_d019_63d_slope_v019_signal,
    f44vg_f44_valuation_vs_growth_d020_63d_slope_v020_signal,
    f44vg_f44_valuation_vs_growth_d021_63d_slope_v021_signal,
    f44vg_f44_valuation_vs_growth_d022_126d_slope_v022_signal,
    f44vg_f44_valuation_vs_growth_d023_126d_slope_v023_signal,
    f44vg_f44_valuation_vs_growth_d024_63d_slope_v024_signal,
    f44vg_f44_valuation_vs_growth_d025_63d_slope_v025_signal,
    f44vg_f44_valuation_vs_growth_d026_126d_slope_v026_signal,
    f44vg_f44_valuation_vs_growth_d027_42d_slope_v027_signal,
    f44vg_f44_valuation_vs_growth_d028_63d_slope_v028_signal,
    f44vg_f44_valuation_vs_growth_d029_63d_slope_v029_signal,
    f44vg_f44_valuation_vs_growth_d030_63d_slope_v030_signal,
    f44vg_f44_valuation_vs_growth_d031_63d_slope_v031_signal,
    f44vg_f44_valuation_vs_growth_d032_63d_slope_v032_signal,
    f44vg_f44_valuation_vs_growth_d033_63d_slope_v033_signal,
    f44vg_f44_valuation_vs_growth_d034_63d_slope_v034_signal,
    f44vg_f44_valuation_vs_growth_d035_126d_slope_v035_signal,
    f44vg_f44_valuation_vs_growth_d036_126d_slope_v036_signal,
    f44vg_f44_valuation_vs_growth_d037_63d_slope_v037_signal,
    f44vg_f44_valuation_vs_growth_d038_63d_slope_v038_signal,
    f44vg_f44_valuation_vs_growth_d039_126d_slope_v039_signal,
    f44vg_f44_valuation_vs_growth_d040_63d_slope_v040_signal,
    f44vg_f44_valuation_vs_growth_d041_126d_slope_v041_signal,
    f44vg_f44_valuation_vs_growth_d042_126d_slope_v042_signal,
    f44vg_f44_valuation_vs_growth_d043_63d_slope_v043_signal,
    f44vg_f44_valuation_vs_growth_d044_126d_slope_v044_signal,
    f44vg_f44_valuation_vs_growth_d045_63d_slope_v045_signal,
    f44vg_f44_valuation_vs_growth_d046_126d_slope_v046_signal,
    f44vg_f44_valuation_vs_growth_d047_126d_slope_v047_signal,
    f44vg_f44_valuation_vs_growth_d048_63d_slope_v048_signal,
    f44vg_f44_valuation_vs_growth_d049_63d_slope_v049_signal,
    f44vg_f44_valuation_vs_growth_d050_126d_slope_v050_signal,
    f44vg_f44_valuation_vs_growth_d051_63d_slope_v051_signal,
    f44vg_f44_valuation_vs_growth_d052_63d_slope_v052_signal,
    f44vg_f44_valuation_vs_growth_d053_63d_slope_v053_signal,
    f44vg_f44_valuation_vs_growth_d054_42d_slope_v054_signal,
    f44vg_f44_valuation_vs_growth_d055_63d_slope_v055_signal,
    f44vg_f44_valuation_vs_growth_d056_42d_slope_v056_signal,
    f44vg_f44_valuation_vs_growth_d057_126d_slope_v057_signal,
    f44vg_f44_valuation_vs_growth_d058_63d_slope_v058_signal,
    f44vg_f44_valuation_vs_growth_d059_63d_slope_v059_signal,
    f44vg_f44_valuation_vs_growth_d060_63d_slope_v060_signal,
    f44vg_f44_valuation_vs_growth_d061_63d_slope_v061_signal,
    f44vg_f44_valuation_vs_growth_d062_126d_slope_v062_signal,
    f44vg_f44_valuation_vs_growth_d063_63d_slope_v063_signal,
    f44vg_f44_valuation_vs_growth_d064_126d_slope_v064_signal,
    f44vg_f44_valuation_vs_growth_d065_63d_slope_v065_signal,
    f44vg_f44_valuation_vs_growth_d066_126d_slope_v066_signal,
    f44vg_f44_valuation_vs_growth_d067_63d_slope_v067_signal,
    f44vg_f44_valuation_vs_growth_d068_63d_slope_v068_signal,
    f44vg_f44_valuation_vs_growth_d069_63d_slope_v069_signal,
    f44vg_f44_valuation_vs_growth_d070_126d_slope_v070_signal,
    f44vg_f44_valuation_vs_growth_d071_63d_slope_v071_signal,
    f44vg_f44_valuation_vs_growth_d072_63d_slope_v072_signal,
    f44vg_f44_valuation_vs_growth_d073_63d_slope_v073_signal,
    f44vg_f44_valuation_vs_growth_d074_63d_slope_v074_signal,
    f44vg_f44_valuation_vs_growth_d075_126d_slope_v075_signal,
    f44vg_f44_valuation_vs_growth_d076_126d_slope_v076_signal,
    f44vg_f44_valuation_vs_growth_d077_126d_slope_v077_signal,
    f44vg_f44_valuation_vs_growth_d078_42d_slope_v078_signal,
    f44vg_f44_valuation_vs_growth_d079_21d_slope_v079_signal,
    f44vg_f44_valuation_vs_growth_d080_126d_slope_v080_signal,
    f44vg_f44_valuation_vs_growth_d081_42d_slope_v081_signal,
    f44vg_f44_valuation_vs_growth_d082_63d_slope_v082_signal,
    f44vg_f44_valuation_vs_growth_d083_42d_slope_v083_signal,
    f44vg_f44_valuation_vs_growth_d084_63d_slope_v084_signal,
    f44vg_f44_valuation_vs_growth_d085_126d_slope_v085_signal,
    f44vg_f44_valuation_vs_growth_d086_126d_slope_v086_signal,
    f44vg_f44_valuation_vs_growth_d087_63d_slope_v087_signal,
    f44vg_f44_valuation_vs_growth_d088_42d_slope_v088_signal,
    f44vg_f44_valuation_vs_growth_d089_126d_slope_v089_signal,
    f44vg_f44_valuation_vs_growth_d090_42d_slope_v090_signal,
    f44vg_f44_valuation_vs_growth_d091_63d_slope_v091_signal,
    f44vg_f44_valuation_vs_growth_d092_126d_slope_v092_signal,
    f44vg_f44_valuation_vs_growth_d093_63d_slope_v093_signal,
    f44vg_f44_valuation_vs_growth_d094_126d_slope_v094_signal,
    f44vg_f44_valuation_vs_growth_d095_126d_slope_v095_signal,
    f44vg_f44_valuation_vs_growth_d096_63d_slope_v096_signal,
    f44vg_f44_valuation_vs_growth_d097_42d_slope_v097_signal,
    f44vg_f44_valuation_vs_growth_d098_21d_slope_v098_signal,
    f44vg_f44_valuation_vs_growth_d099_63d_slope_v099_signal,
    f44vg_f44_valuation_vs_growth_d100_63d_slope_v100_signal,
    f44vg_f44_valuation_vs_growth_d101_63d_slope_v101_signal,
    f44vg_f44_valuation_vs_growth_d102_126d_slope_v102_signal,
    f44vg_f44_valuation_vs_growth_d103_126d_slope_v103_signal,
    f44vg_f44_valuation_vs_growth_d104_63d_slope_v104_signal,
    f44vg_f44_valuation_vs_growth_d105_63d_slope_v105_signal,
    f44vg_f44_valuation_vs_growth_d106_63d_slope_v106_signal,
    f44vg_f44_valuation_vs_growth_d107_63d_slope_v107_signal,
    f44vg_f44_valuation_vs_growth_d108_63d_slope_v108_signal,
    f44vg_f44_valuation_vs_growth_d109_126d_slope_v109_signal,
    f44vg_f44_valuation_vs_growth_d110_21d_slope_v110_signal,
    f44vg_f44_valuation_vs_growth_d111_63d_slope_v111_signal,
    f44vg_f44_valuation_vs_growth_d112_63d_slope_v112_signal,
    f44vg_f44_valuation_vs_growth_d113_63d_slope_v113_signal,
    f44vg_f44_valuation_vs_growth_d114_126d_slope_v114_signal,
    f44vg_f44_valuation_vs_growth_d115_63d_slope_v115_signal,
    f44vg_f44_valuation_vs_growth_d116_21d_slope_v116_signal,
    f44vg_f44_valuation_vs_growth_d117_63d_slope_v117_signal,
    f44vg_f44_valuation_vs_growth_d118_63d_slope_v118_signal,
    f44vg_f44_valuation_vs_growth_d119_126d_slope_v119_signal,
    f44vg_f44_valuation_vs_growth_d120_126d_slope_v120_signal,
    f44vg_f44_valuation_vs_growth_d121_63d_slope_v121_signal,
    f44vg_f44_valuation_vs_growth_d122_126d_slope_v122_signal,
    f44vg_f44_valuation_vs_growth_d123_126d_slope_v123_signal,
    f44vg_f44_valuation_vs_growth_d124_63d_slope_v124_signal,
    f44vg_f44_valuation_vs_growth_d125_21d_slope_v125_signal,
    f44vg_f44_valuation_vs_growth_d126_63d_slope_v126_signal,
    f44vg_f44_valuation_vs_growth_d127_63d_slope_v127_signal,
    f44vg_f44_valuation_vs_growth_d128_63d_slope_v128_signal,
    f44vg_f44_valuation_vs_growth_d129_21d_slope_v129_signal,
    f44vg_f44_valuation_vs_growth_d130_63d_slope_v130_signal,
    f44vg_f44_valuation_vs_growth_d131_63d_slope_v131_signal,
    f44vg_f44_valuation_vs_growth_d132_63d_slope_v132_signal,
    f44vg_f44_valuation_vs_growth_d133_63d_slope_v133_signal,
    f44vg_f44_valuation_vs_growth_d134_63d_slope_v134_signal,
    f44vg_f44_valuation_vs_growth_d135_126d_slope_v135_signal,
    f44vg_f44_valuation_vs_growth_d136_63d_slope_v136_signal,
    f44vg_f44_valuation_vs_growth_d137_42d_slope_v137_signal,
    f44vg_f44_valuation_vs_growth_d138_63d_slope_v138_signal,
    f44vg_f44_valuation_vs_growth_d139_126d_slope_v139_signal,
    f44vg_f44_valuation_vs_growth_d140_63d_slope_v140_signal,
    f44vg_f44_valuation_vs_growth_d141_126d_slope_v141_signal,
    f44vg_f44_valuation_vs_growth_d142_42d_slope_v142_signal,
    f44vg_f44_valuation_vs_growth_d143_63d_slope_v143_signal,
    f44vg_f44_valuation_vs_growth_d144_63d_slope_v144_signal,
    f44vg_f44_valuation_vs_growth_d145_126d_slope_v145_signal,
    f44vg_f44_valuation_vs_growth_d146_63d_slope_v146_signal,
    f44vg_f44_valuation_vs_growth_d147_63d_slope_v147_signal,
    f44vg_f44_valuation_vs_growth_d148_63d_slope_v148_signal,
    f44vg_f44_valuation_vs_growth_d149_63d_slope_v149_signal,
    f44vg_f44_valuation_vs_growth_d150_21d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F44_VALUATION_VS_GROWTH_REGISTRY_SLOPE = REGISTRY

if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc", "opex",
        "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin", "netinc",
        "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps", "ncfo", "ncff",
        "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex", "depamor", "sharesbas",
        "shareswa", "shareswadil", "assets", "assetsc", "tangibles", "intangibles",
        "ppnenet", "investments", "inventory", "receivables", "payables", "equity",
        "retearn", "workingcapital", "debt", "debtc", "debtnc", "liabilities",
        "liabilitiesc", "cashneq", "currentratio", "roic", "roe", "roa", "ros",
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "de",
        "ncfdiv", "dps", "divyield", "payoutratio", "prefdivis",
        "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    ps = _fund(1, base=6.0, drift=0.01, vol=0.05).rename("ps")
    evebitda = _fund(2, base=18.0, drift=0.01, vol=0.05).rename("evebitda")
    ev = _fund(3, base=2.0e9, drift=0.035, vol=0.08).rename("ev")
    marketcap = _fund(4, base=1.8e9, drift=0.035, vol=0.08).rename("marketcap")
    revenue = _fund(5, base=5.0e8, drift=0.04, vol=0.06).rename("revenue")
    ebitda = _fund(6, base=8.0e7, drift=0.03, vol=0.10).rename("ebitda")
    fcf = _fund(7, base=4.0e7, drift=0.03, vol=0.12, allow_neg=True).rename("fcf")

    cols = {
        "ps": ps, "evebitda": evebitda, "ev": ev, "marketcap": marketcap,
        "revenue": revenue, "ebitda": ebitda, "fcf": fcf,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (
            name, set(meta["inputs"]) - ALLOW)
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
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
            ix = ai.index.intersection(aj.index)
            if len(ix) < 30:
                continue
            c = ai.loc[ix].corr(aj.loc[ix])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f44_valuation_vs_growth_2nd_derivatives_001_150_claude: %d features pass" % n_features)
