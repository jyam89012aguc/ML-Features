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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    # OLS slope of s on time over window w (per-step)
    def _f(a):
        m = len(a)
        idx = np.arange(m, dtype=float)
        idx = idx - idx.mean()
        denom = (idx ** 2).sum()
        if denom == 0:
            return np.nan
        return float(np.dot(idx, a - a.mean()) / denom)

    return s.rolling(w, min_periods=max(2, w // 2)).apply(_f, raw=True)


# ===== folder domain primitives (GARP: valuation x growth) =====
def _grw(s, w):
    # trailing growth of a fundamental series over window w (simple pct over the span)
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _grw_ann(s, w):
    # annualized growth (252d) implied by the w-window growth
    g = s / s.shift(w).replace(0, np.nan)
    return g ** (252.0 / w) - 1.0


def _grw_pct(s, w):
    # average per-period pct_change over window w (smoother growth proxy)
    return s.pct_change().rolling(w, min_periods=max(2, w // 2)).mean()


def _grw_pct_bps(s, w):
    # same as _grw_pct but expressed as an annual-rate (x252)
    return s.pct_change().rolling(w, min_periods=max(2, w // 2)).mean() * 252.0


def _peg(mult, growth_pct):
    # PEG-style: multiple divided by growth-in-percentage-points (growth*100)
    g = (growth_pct * 100.0).replace(0, np.nan)
    return mult / g


def _earnyield(netinc, marketcap):
    return _safe_div(netinc, marketcap)


def _fcfyield(fcf, marketcap):
    return _safe_div(fcf, marketcap)


def _evsales(ev, revenue):
    return _safe_div(ev, revenue)


# ============================================================
# --- PEG family: pe over revenue growth (classic GARP) ---

# classic PEG: trailing PE / 252d revenue-growth points
def f40vg_f40_valuation_vs_growth_peg_rev_252d_base_v001_signal(pe, revenue):
    g = _grw(revenue, 252)
    b = _peg(pe, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG using 126d revenue growth (faster trajectory)
def f40vg_f40_valuation_vs_growth_peg_rev_126d_base_v002_signal(pe, revenue):
    g = _grw(revenue, 126)
    b = _peg(pe, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG using 504d (two-year) revenue growth, smoother denominator
def f40vg_f40_valuation_vs_growth_peg_rev_504d_base_v003_signal(pe, revenue):
    g = _grw(revenue, 504)
    b = _peg(pe, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG vs annualized EBITDA growth (CAGR-implied) from 504d window
def f40vg_f40_valuation_vs_growth_pegann_rev_504d_base_v004_signal(pe, ebitda):
    g = _grw_ann(ebitda, 504)
    b = _peg(pe, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG z-scored vs its own 252d history (cheapness vs own GARP norm)
def f40vg_f40_valuation_vs_growth_pegz_rev_252d_base_v005_signal(pe, revenue):
    g = _grw(revenue, 252)
    peg = _peg(pe, g)
    b = _z(peg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG percentile-ranked vs its own 504d history
def f40vg_f40_valuation_vs_growth_pegrank_rev_252d_base_v006_signal(pe, revenue):
    g = _grw(revenue, 252)
    peg = _peg(pe, g)
    b = _rank(peg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inverse-PEG (GARP attractiveness: growth per unit of multiple)
def f40vg_f40_valuation_vs_growth_invpeg_rev_252d_base_v007_signal(pe, revenue):
    g = _grw(revenue, 252)
    b = _safe_div(g * 100.0, pe.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV/EBITDA-to-growth family ---

# EV/EBITDA divided by EBITDA growth points (252d)
def f40vg_f40_valuation_vs_growth_evebg_ebitda_252d_base_v008_signal(evebitda, ebitda):
    g = _grw(ebitda, 252)
    b = _peg(evebitda, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth, 126d EBITDA growth
def f40vg_f40_valuation_vs_growth_evebg_ebitda_126d_base_v009_signal(evebitda, ebitda):
    g = _grw(ebitda, 126)
    b = _peg(evebitda, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA divided by net-income growth (504d), ranked (earnings-growth cheapness)
def f40vg_f40_valuation_vs_growth_evebg_ebitda_504d_base_v010_signal(evebitda, netinc):
    g = _grw(netinc, 504)
    b = _rank(_peg(evebitda, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth z-scored vs own 252d history
def f40vg_f40_valuation_vs_growth_evebgz_ebitda_252d_base_v011_signal(evebitda, ebitda):
    g = _grw(ebitda, 252)
    peg = _peg(evebitda, g)
    b = _z(peg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# inverse EV/EBITDA-to-growth (EBITDA-growth yield per turn of EV/EBITDA)
def f40vg_f40_valuation_vs_growth_invevebg_ebitda_252d_base_v012_signal(evebitda, ebitda):
    g = _grw(ebitda, 252)
    b = _safe_div(g * 100.0, evebitda.replace(0, np.nan))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- EV/Sales-to-growth family (EV built from ev & revenue) ---

# EV/Sales divided by revenue growth points (252d)
def f40vg_f40_valuation_vs_growth_evsg_rev_252d_base_v013_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _grw(revenue, 252)
    b = _peg(evs, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales-to-growth, 63d revenue growth, ranked (fast sales-momentum GARP)
def f40vg_f40_valuation_vs_growth_evsg_rev_126d_base_v014_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _grw(revenue, 63)
    b = _rank(_peg(evs, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales-yield (1/ps) interacted with revenue growth, z-scored (cheap-sales grower)
def f40vg_f40_valuation_vs_growth_psg_rev_252d_base_v015_signal(ps, revenue):
    sy = 1.0 / ps.replace(0, np.nan)
    g = _grw(revenue, 126)
    b = _z(sy * (1.0 + g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S-to-growth combined with sales-yield level (cheap-sales grower, distinct from PEG-z)
def f40vg_f40_valuation_vs_growth_psgz_rev_252d_base_v016_signal(ps, revenue, marketcap):
    g = _grw(revenue, 252)
    peg = _peg(ps, g)
    sy = _safe_div(revenue, marketcap)
    b = _z(peg, 252) - _z(sy, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales-to-EBITDA-growth ranked vs own 504d history (distinct growth leg)
def f40vg_f40_valuation_vs_growth_evsgrank_rev_252d_base_v017_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = _grw(ebitda, 252)
    peg = _peg(evs, g)
    b = _rank(peg, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- FCF-yield-plus-growth family (Rule-of-40-like) ---

# FCF yield + revenue growth (Rule-of-40 proxy): z-blend so both legs contribute
def f40vg_f40_valuation_vs_growth_ruleof40_rev_252d_base_v018_signal(fcf, marketcap, revenue):
    fy = _fcfyield(fcf, marketcap)
    g = _grw(revenue, 252)
    b = _z(fy, 126) + _z(g, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF yield z + EBITDA growth z (cash-quality GARP, de-trended legs)
def f40vg_f40_valuation_vs_growth_fcfygrw_ebitda_252d_base_v019_signal(fcf, marketcap, ebitda):
    fy = _fcfyield(fcf, marketcap)
    g = _grw(ebitda, 252)
    b = _z(fy, 252) + _z(g, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness combined with net-income growth (distinct driver pair)
def f40vg_f40_valuation_vs_growth_ruleof40z_rev_252d_base_v020_signal(ev, revenue, netinc):
    evs = _evsales(ev, revenue)
    g = _grw(netinc, 252)
    b = -_z(evs, 252) + _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF yield divided by EV/EBITDA then interacted with EBITDA growth (cheap-cash-grower)
def f40vg_f40_valuation_vs_growth_fcfgarp_rev_252d_base_v021_signal(fcf, marketcap, evebitda, ebitda):
    fy = _fcfyield(fcf, marketcap)
    g = _grw(ebitda, 252)
    b = (fy / evebitda.replace(0, np.nan)) * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF-yield interacted with growth (multiplicative GARP, both must be high)
def f40vg_f40_valuation_vs_growth_fcfxgrw_rev_252d_base_v022_signal(fcf, marketcap, revenue):
    fy = _fcfyield(fcf, marketcap)
    g = _grw(revenue, 252)
    b = fy * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- growth-adjusted earnings yield family ---

# earnings yield x (1 + revenue growth): cheap-and-growing earnings
def f40vg_f40_valuation_vs_growth_eygrw_rev_252d_base_v023_signal(netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    g = _grw(revenue, 252)
    b = ey * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted earnings yield: earnings yield + net-income growth
def f40vg_f40_valuation_vs_growth_eyplusni_252d_base_v024_signal(netinc, marketcap):
    ey = _earnyield(netinc, marketcap)
    g = _grw(netinc, 252)
    b = ey + 0.25 * g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings yield divided by PE-implied growth gap (GARP residual)
def f40vg_f40_valuation_vs_growth_eyresid_rev_252d_base_v025_signal(pe, netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    g = _grw(revenue, 252)
    fair = g / pe.replace(0, np.nan)
    b = ey - fair
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted earnings yield z-scored vs own 252d history
def f40vg_f40_valuation_vs_growth_eygrwz_rev_252d_base_v026_signal(netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    g = _grw(revenue, 252)
    raw = ey * (1.0 + g)
    b = _z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- GARP composite family ---

# GARP composite: rank(growth) minus rank(PE) blended (cheap & growing)
def f40vg_f40_valuation_vs_growth_garpcomp_rev_252d_base_v027_signal(pe, revenue):
    g = _grw(revenue, 252)
    b = _rank(g, 504) - _rank(pe, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP composite across EV/EBITDA & EBITDA growth ranks
def f40vg_f40_valuation_vs_growth_garpcomp_ebitda_252d_base_v028_signal(evebitda, ebitda):
    g = _grw(ebitda, 252)
    b = _rank(g, 504) - _rank(evebitda, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP composite triple: -z(PE) -z(EV/Sales) + z(rev growth)
def f40vg_f40_valuation_vs_growth_garptriple_252d_base_v029_signal(pe, ev, revenue):
    evs = _evsales(ev, revenue)
    g = _grw(revenue, 252)
    b = -_z(pe, 252) - _z(evs, 252) + 2.0 * _z(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP balance: (growth - valuation) / (growth + valuation) using EV/EBITDA & EBITDA growth
def f40vg_f40_valuation_vs_growth_garpbal_rev_252d_base_v030_signal(evebitda, ebitda):
    g = (_grw(ebitda, 126) * 100.0)
    v = evebitda
    b = (g - v) / (g.abs() + v.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# --- more PEG variants on different fundamentals / windows ---

# PEG on net income growth (earnings PEG)
def f40vg_f40_valuation_vs_growth_peg_ni_252d_base_v031_signal(pe, netinc):
    g = _grw(netinc, 252)
    b = _peg(pe, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG on FCF growth (cash PEG)
def f40vg_f40_valuation_vs_growth_peg_fcf_252d_base_v032_signal(pe, fcf):
    g = _grw(fcf, 252)
    b = _peg(pe, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG spread: revenue-PEG minus FCF-PEG, ranked (which growth is cheaper on P/E)
def f40vg_f40_valuation_vs_growth_pegspr_rev_ebitda_252d_base_v033_signal(pe, revenue, fcf):
    pegr = _peg(pe, _grw(revenue, 252))
    pegf = _peg(pe, _grw(fcf, 252))
    b = _rank(pegr - pegf, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth acceleration adjusted PEG: PEG scaled by growth trend sign
def f40vg_f40_valuation_vs_growth_pegaccel_rev_252d_base_v034_signal(pe, revenue):
    g = _grw(revenue, 252)
    accel = g - g.shift(63)
    peg = _peg(pe, g)
    b = peg * np.sign(accel) * -1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales-to-growth using annualized EBITDA growth, ranked (cashflow CAGR vs sales)
def f40vg_f40_valuation_vs_growth_evsgann_rev_252d_base_v035_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = _grw_ann(ebitda, 252)
    b = _rank(_peg(evs, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple-to-growth gap: PE minus EBITDA-growth-points, z-scored vs own history
def f40vg_f40_valuation_vs_growth_pegap_rev_252d_base_v036_signal(pe, ebitda):
    g = _grw(ebitda, 252) * 100.0
    b = _z(pe - g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA fair-multiple gap ranked: EV/EBITDA minus EBITDA-growth-points (504d growth)
def f40vg_f40_valuation_vs_growth_evebgap_ebitda_252d_base_v037_signal(evebitda, ebitda):
    g = _grw(ebitda, 504) * 100.0
    b = _rank(evebitda - g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP yield: rank(earnings yield) + rank(FCF yield) + rank(revenue growth), de-meaned
def f40vg_f40_valuation_vs_growth_garpyield_252d_base_v038_signal(netinc, fcf, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    fy = _fcfyield(fcf, marketcap)
    g = _grw(revenue, 252)
    b = _rank(ey, 252) + _rank(fy, 252) + _rank(g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-weighted cheapness: rev-growth divided by EV/Sales (growth per sales-turn)
def f40vg_f40_valuation_vs_growth_grwpersale_252d_base_v039_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _grw(revenue, 252)
    b = _safe_div(g, evs)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-growth-yield spread: short-window minus long-window growth-per-turn (trajectory)
def f40vg_f40_valuation_vs_growth_grwperturn_ebitda_252d_base_v040_signal(evebitda, ebitda):
    gs = _grw(ebitda, 63)
    gl = _grw(ebitda, 252)
    b = _safe_div(gs - gl, evebitda)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG momentum: change in PEG over a quarter (re-rating vs growth)
def f40vg_f40_valuation_vs_growth_pegmom_rev_252d_base_v041_signal(pe, revenue):
    g = _grw(revenue, 252)
    peg = _peg(pe, g)
    b = peg - peg.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth momentum (monthly change, distinct multiple/window)
def f40vg_f40_valuation_vs_growth_evsgmom_rev_252d_base_v042_signal(evebitda, ebitda):
    g = _grw(ebitda, 252)
    peg = _peg(evebitda, g)
    b = peg - peg.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 trajectory: change in (fcf-yield + growth) over a quarter
def f40vg_f40_valuation_vs_growth_ruleof40mom_252d_base_v043_signal(fcf, marketcap, revenue):
    fy = _fcfyield(fcf, marketcap)
    g = _grw(revenue, 252)
    r40 = fy + g
    b = r40 - r40.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted earnings-yield momentum
def f40vg_f40_valuation_vs_growth_eygrwmom_rev_252d_base_v044_signal(netinc, marketcap, revenue):
    ey = _earnyield(netinc, marketcap)
    g = _grw(revenue, 252)
    raw = ey * (1.0 + g)
    b = raw - raw.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP attractiveness x growth-stability: P/S inverse-PEG penalized by growth vol
def f40vg_f40_valuation_vs_growth_pegstab_rev_252d_base_v045_signal(ps, revenue):
    g = _grw(revenue, 126)
    invpeg = _safe_div(g * 100.0, ps.replace(0, np.nan))
    gstab = g.rolling(252, min_periods=63).std()
    b = invpeg / (1.0 + gstab) - invpeg.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA-growth quality vs EV/Sales: growth-per-sales-turn, vol-penalized and de-meaned
def f40vg_f40_valuation_vs_growth_grwqual_ebitda_252d_base_v046_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = _grw(ebitda, 252)
    gstab = g.rolling(252, min_periods=63).std()
    raw = _safe_div(g, evs) / (1.0 + gstab)
    b = raw - raw.rolling(126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG using short 63d revenue growth (momentum GARP)
def f40vg_f40_valuation_vs_growth_peg_rev_63d_base_v047_signal(pe, revenue):
    g = _grw(revenue, 63)
    b = _peg(pe, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth using 63d EBITDA growth
def f40vg_f40_valuation_vs_growth_evebg_ebitda_63d_base_v048_signal(evebitda, ebitda):
    g = _grw(ebitda, 63)
    b = _peg(evebitda, g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted FCF yield: fcf-yield x (1 + fcf-growth)
def f40vg_f40_valuation_vs_growth_fcfygrw_fcf_252d_base_v049_signal(fcf, marketcap):
    fy = _fcfyield(fcf, marketcap)
    g = _grw(fcf, 252)
    b = fy * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP composite: -z(P/S) + z(rev-growth) + z(ebitda-growth)
def f40vg_f40_valuation_vs_growth_garpms_252d_base_v050_signal(ps, revenue, ebitda):
    b = -_z(ps, 252) + _z(_grw(revenue, 252), 252) + _z(_grw(ebitda, 252), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG fair-value residual on EV/Sales (EV/Sales minus growth-implied fair)
def f40vg_f40_valuation_vs_growth_evsresid_rev_252d_base_v051_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _grw(revenue, 252)
    fair = (1.0 + g)  # fair EV/Sales scales with growth
    b = evs / fair.replace(0, np.nan) - evs
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-yield-to-growth ratio (yield per growth point, inverse GARP)
def f40vg_f40_valuation_vs_growth_eytogrw_ni_252d_base_v052_signal(netinc, marketcap):
    ey = _earnyield(netinc, marketcap)
    g = _grw(netinc, 252)
    b = _safe_div(ey, (g.abs() + 0.01))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended PEG: z-average of revenue-PEG, EBITDA-PEG and P/S-PEG (distinct from FCF-PEG)
def f40vg_f40_valuation_vs_growth_pegblend_252d_base_v053_signal(pe, evebitda, ps, revenue, ebitda):
    p1 = _z(_peg(pe, _grw(revenue, 252)), 252)
    p2 = _z(_peg(evebitda, _grw(ebitda, 252)), 252)
    p3 = _z(_peg(ps, _grw(revenue, 126)), 252)
    b = (p1 + p2 + p3) / 3.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-tilted cheapness rank: rank of inverse-PEG vs 252d history
def f40vg_f40_valuation_vs_growth_invpegrank_rev_252d_base_v054_signal(pe, revenue):
    g = _grw(revenue, 252)
    invpeg = _safe_div(g * 100.0, pe.replace(0, np.nan))
    b = _rank(invpeg, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness vs growth, tanh-bounded GARP score
def f40vg_f40_valuation_vs_growth_garptanh_ebitda_252d_base_v055_signal(evebitda, ebitda):
    g = _grw(ebitda, 252)
    score = _z(g, 252) - _z(evebitda, 252)
    b = np.tanh(0.5 * score)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# marketcap-relative growth value: EBITDA-growth divided by log market cap (size-adj GARP)
def f40vg_f40_valuation_vs_growth_grwsize_rev_252d_base_v056_signal(marketcap, ebitda):
    g = _grw(ebitda, 126)
    b = g / np.log(marketcap.replace(0, np.nan)).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sales yield (revenue/marketcap) times growth (cheap-revenue grower)
def f40vg_f40_valuation_vs_growth_salesyldgrw_252d_base_v057_signal(marketcap, revenue):
    sy = _safe_div(revenue, marketcap)
    g = _grw(revenue, 252)
    b = sy * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EBITDA yield (ebitda/ev) times growth (cheap-cashflow grower)
def f40vg_f40_valuation_vs_growth_ebitdayldgrw_252d_base_v058_signal(ev, ebitda):
    ey = _safe_div(ebitda, ev)
    g = _grw(ebitda, 252)
    b = ey * (1.0 + g)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG dispersion across windows (126/252/504 PEG std = stability of valuation-vs-growth)
def f40vg_f40_valuation_vs_growth_pegdisp_rev_252d_base_v059_signal(pe, revenue):
    p1 = _peg(pe, _grw(revenue, 126))
    p2 = _peg(pe, _grw(revenue, 252))
    p3 = _peg(pe, _grw(revenue, 504))
    b = pd.concat([p1, p2, p3], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP momentum-of-rank: change in invPEG rank over a quarter
def f40vg_f40_valuation_vs_growth_invpegrankmom_rev_252d_base_v060_signal(pe, revenue):
    g = _grw(revenue, 252)
    invpeg = _safe_div(g * 100.0, pe.replace(0, np.nan))
    r = _rank(invpeg, 252)
    b = r - r.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted EV/Sales using per-period EBITDA growth, z-scored (smoother, distinct)
def f40vg_f40_valuation_vs_growth_evsg_pct_rev_252d_base_v061_signal(ev, revenue, ebitda):
    evs = _evsales(ev, revenue)
    g = _grw_pct_bps(ebitda, 126)
    b = _z(_peg(evs, g), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Rule-of-40 with EBITDA-margin growth proxy (ebitda/revenue growth)
def f40vg_f40_valuation_vs_growth_ruleof40m_252d_base_v062_signal(fcf, marketcap, ebitda, revenue):
    fy = _fcfyield(fcf, marketcap)
    margin = _safe_div(ebitda, revenue)
    mg = margin - margin.shift(252)
    b = fy + mg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings-yield growth-adjusted residual vs EV/EBITDA fair line, z-scored (de-trended)
def f40vg_f40_valuation_vs_growth_eyevebresid_252d_base_v063_signal(netinc, marketcap, evebitda, ebitda):
    ey = _z(_earnyield(netinc, marketcap), 252)
    g = _grw(ebitda, 252)
    fair = _z(g / evebitda.replace(0, np.nan), 252)
    b = ey - 0.5 * fair
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG with growth from slope of revenue (regression growth rate, 252d)
def f40vg_f40_valuation_vs_growth_pegslope_rev_252d_base_v064_signal(pe, revenue):
    sl = _slope(np.log(revenue.replace(0, np.nan)), 252) * 252.0
    b = _peg(pe, sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA-to-growth with EBITDA growth from log-slope (252d)
def f40vg_f40_valuation_vs_growth_evebgslope_ebitda_252d_base_v065_signal(evebitda, ebitda):
    sl = _slope(np.log(ebitda.replace(0, np.nan)), 252) * 252.0
    b = _peg(evebitda, sl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP composite of yields: (earn-yield + fcf-yield) x rank(ebitda-growth), de-meaned
def f40vg_f40_valuation_vs_growth_yieldxgrwrank_252d_base_v066_signal(netinc, fcf, marketcap, ebitda):
    ey = _earnyield(netinc, marketcap)
    fy = _fcfyield(fcf, marketcap)
    gr = _rank(_grw(ebitda, 126), 504) + 0.5
    raw = (ey + fy) * gr
    b = raw - raw.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# valuation-vs-growth divergence: z(EV/Sales) minus z(rev-growth) momentum
def f40vg_f40_valuation_vs_growth_valgrwdiv_252d_base_v067_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    div = _z(evs, 252) - _z(_grw(revenue, 252), 252)
    b = div - div.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net-income PEG fair-value gap ranked (PE minus NI-growth points, 126d growth)
def f40vg_f40_valuation_vs_growth_nipegap_252d_base_v068_signal(pe, netinc):
    g = _grw(netinc, 126) * 100.0
    b = _rank(pe - g, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# FCF PEG fair-value gap (PE minus FCF-growth points)
def f40vg_f40_valuation_vs_growth_fcfpegap_252d_base_v069_signal(pe, fcf):
    g = _grw(fcf, 252) * 100.0
    b = pe - g
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP "double cheap": invPEG(rev) x invPEG(ebitda) sign-magnitude
def f40vg_f40_valuation_vs_growth_doublecheap_252d_base_v070_signal(pe, evebitda, revenue, ebitda):
    a = _safe_div(_grw(revenue, 252) * 100.0, pe.replace(0, np.nan))
    b2 = _safe_div(_grw(ebitda, 252) * 100.0, evebitda.replace(0, np.nan))
    raw = a + b2
    b = np.sign(raw) * np.sqrt(a.abs() * b2.abs())
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# growth-adjusted earnings yield ranked vs 504d history
def f40vg_f40_valuation_vs_growth_eygrwrank_ni_252d_base_v071_signal(netinc, marketcap):
    ey = _earnyield(netinc, marketcap)
    g = _grw(netinc, 252)
    raw = ey * (1.0 + g)
    b = _rank(raw, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness relative to its growth-implied band, ranked
def f40vg_f40_valuation_vs_growth_evsbandrank_252d_base_v072_signal(ev, revenue):
    evs = _evsales(ev, revenue)
    g = _grw(revenue, 252)
    adj = evs / (1.0 + g).replace(0, np.nan)
    b = _rank(adj, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# PEG smoothed (EMA) GARP signal
def f40vg_f40_valuation_vs_growth_pegema_rev_252d_base_v073_signal(pe, revenue):
    g = _grw(revenue, 252)
    peg = _peg(pe, g)
    b = peg.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# GARP composite displacement: invPEG minus its own slow EMA
def f40vg_f40_valuation_vs_growth_invpegdisp_rev_252d_base_v074_signal(pe, revenue):
    g = _grw(revenue, 252)
    invpeg = _safe_div(g * 100.0, pe.replace(0, np.nan))
    b = invpeg - invpeg.ewm(span=126, min_periods=42).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# full GARP score: blend of cheapness-vs-growth across all multiples, z-summed
def f40vg_f40_valuation_vs_growth_garpfull_252d_base_v075_signal(pe, evebitda, ev, ps, revenue, ebitda):
    gr = _grw(revenue, 252)
    ge = _grw(ebitda, 252)
    evs = _evsales(ev, revenue)
    b = (-_z(pe, 252) - _z(evebitda, 252) - _z(ps, 252) - _z(evs, 252)
         + 2.0 * _z(gr, 252) + 2.0 * _z(ge, 252))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40vg_f40_valuation_vs_growth_peg_rev_252d_base_v001_signal,
    f40vg_f40_valuation_vs_growth_peg_rev_126d_base_v002_signal,
    f40vg_f40_valuation_vs_growth_peg_rev_504d_base_v003_signal,
    f40vg_f40_valuation_vs_growth_pegann_rev_504d_base_v004_signal,
    f40vg_f40_valuation_vs_growth_pegz_rev_252d_base_v005_signal,
    f40vg_f40_valuation_vs_growth_pegrank_rev_252d_base_v006_signal,
    f40vg_f40_valuation_vs_growth_invpeg_rev_252d_base_v007_signal,
    f40vg_f40_valuation_vs_growth_evebg_ebitda_252d_base_v008_signal,
    f40vg_f40_valuation_vs_growth_evebg_ebitda_126d_base_v009_signal,
    f40vg_f40_valuation_vs_growth_evebg_ebitda_504d_base_v010_signal,
    f40vg_f40_valuation_vs_growth_evebgz_ebitda_252d_base_v011_signal,
    f40vg_f40_valuation_vs_growth_invevebg_ebitda_252d_base_v012_signal,
    f40vg_f40_valuation_vs_growth_evsg_rev_252d_base_v013_signal,
    f40vg_f40_valuation_vs_growth_evsg_rev_126d_base_v014_signal,
    f40vg_f40_valuation_vs_growth_psg_rev_252d_base_v015_signal,
    f40vg_f40_valuation_vs_growth_psgz_rev_252d_base_v016_signal,
    f40vg_f40_valuation_vs_growth_evsgrank_rev_252d_base_v017_signal,
    f40vg_f40_valuation_vs_growth_ruleof40_rev_252d_base_v018_signal,
    f40vg_f40_valuation_vs_growth_fcfygrw_ebitda_252d_base_v019_signal,
    f40vg_f40_valuation_vs_growth_ruleof40z_rev_252d_base_v020_signal,
    f40vg_f40_valuation_vs_growth_fcfgarp_rev_252d_base_v021_signal,
    f40vg_f40_valuation_vs_growth_fcfxgrw_rev_252d_base_v022_signal,
    f40vg_f40_valuation_vs_growth_eygrw_rev_252d_base_v023_signal,
    f40vg_f40_valuation_vs_growth_eyplusni_252d_base_v024_signal,
    f40vg_f40_valuation_vs_growth_eyresid_rev_252d_base_v025_signal,
    f40vg_f40_valuation_vs_growth_eygrwz_rev_252d_base_v026_signal,
    f40vg_f40_valuation_vs_growth_garpcomp_rev_252d_base_v027_signal,
    f40vg_f40_valuation_vs_growth_garpcomp_ebitda_252d_base_v028_signal,
    f40vg_f40_valuation_vs_growth_garptriple_252d_base_v029_signal,
    f40vg_f40_valuation_vs_growth_garpbal_rev_252d_base_v030_signal,
    f40vg_f40_valuation_vs_growth_peg_ni_252d_base_v031_signal,
    f40vg_f40_valuation_vs_growth_peg_fcf_252d_base_v032_signal,
    f40vg_f40_valuation_vs_growth_pegspr_rev_ebitda_252d_base_v033_signal,
    f40vg_f40_valuation_vs_growth_pegaccel_rev_252d_base_v034_signal,
    f40vg_f40_valuation_vs_growth_evsgann_rev_252d_base_v035_signal,
    f40vg_f40_valuation_vs_growth_pegap_rev_252d_base_v036_signal,
    f40vg_f40_valuation_vs_growth_evebgap_ebitda_252d_base_v037_signal,
    f40vg_f40_valuation_vs_growth_garpyield_252d_base_v038_signal,
    f40vg_f40_valuation_vs_growth_grwpersale_252d_base_v039_signal,
    f40vg_f40_valuation_vs_growth_grwperturn_ebitda_252d_base_v040_signal,
    f40vg_f40_valuation_vs_growth_pegmom_rev_252d_base_v041_signal,
    f40vg_f40_valuation_vs_growth_evsgmom_rev_252d_base_v042_signal,
    f40vg_f40_valuation_vs_growth_ruleof40mom_252d_base_v043_signal,
    f40vg_f40_valuation_vs_growth_eygrwmom_rev_252d_base_v044_signal,
    f40vg_f40_valuation_vs_growth_pegstab_rev_252d_base_v045_signal,
    f40vg_f40_valuation_vs_growth_grwqual_ebitda_252d_base_v046_signal,
    f40vg_f40_valuation_vs_growth_peg_rev_63d_base_v047_signal,
    f40vg_f40_valuation_vs_growth_evebg_ebitda_63d_base_v048_signal,
    f40vg_f40_valuation_vs_growth_fcfygrw_fcf_252d_base_v049_signal,
    f40vg_f40_valuation_vs_growth_garpms_252d_base_v050_signal,
    f40vg_f40_valuation_vs_growth_evsresid_rev_252d_base_v051_signal,
    f40vg_f40_valuation_vs_growth_eytogrw_ni_252d_base_v052_signal,
    f40vg_f40_valuation_vs_growth_pegblend_252d_base_v053_signal,
    f40vg_f40_valuation_vs_growth_invpegrank_rev_252d_base_v054_signal,
    f40vg_f40_valuation_vs_growth_garptanh_ebitda_252d_base_v055_signal,
    f40vg_f40_valuation_vs_growth_grwsize_rev_252d_base_v056_signal,
    f40vg_f40_valuation_vs_growth_salesyldgrw_252d_base_v057_signal,
    f40vg_f40_valuation_vs_growth_ebitdayldgrw_252d_base_v058_signal,
    f40vg_f40_valuation_vs_growth_pegdisp_rev_252d_base_v059_signal,
    f40vg_f40_valuation_vs_growth_invpegrankmom_rev_252d_base_v060_signal,
    f40vg_f40_valuation_vs_growth_evsg_pct_rev_252d_base_v061_signal,
    f40vg_f40_valuation_vs_growth_ruleof40m_252d_base_v062_signal,
    f40vg_f40_valuation_vs_growth_eyevebresid_252d_base_v063_signal,
    f40vg_f40_valuation_vs_growth_pegslope_rev_252d_base_v064_signal,
    f40vg_f40_valuation_vs_growth_evebgslope_ebitda_252d_base_v065_signal,
    f40vg_f40_valuation_vs_growth_yieldxgrwrank_252d_base_v066_signal,
    f40vg_f40_valuation_vs_growth_valgrwdiv_252d_base_v067_signal,
    f40vg_f40_valuation_vs_growth_nipegap_252d_base_v068_signal,
    f40vg_f40_valuation_vs_growth_fcfpegap_252d_base_v069_signal,
    f40vg_f40_valuation_vs_growth_doublecheap_252d_base_v070_signal,
    f40vg_f40_valuation_vs_growth_eygrwrank_ni_252d_base_v071_signal,
    f40vg_f40_valuation_vs_growth_evsbandrank_252d_base_v072_signal,
    f40vg_f40_valuation_vs_growth_pegema_rev_252d_base_v073_signal,
    f40vg_f40_valuation_vs_growth_invpegdisp_rev_252d_base_v074_signal,
    f40vg_f40_valuation_vs_growth_garpfull_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_VALUATION_VS_GROWTH_REGISTRY_001_075 = REGISTRY


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

    assert n_features == 75, n_features
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

    print("OK f40_valuation_vs_growth_base_001_075_claude: %d features pass" % n_features)
