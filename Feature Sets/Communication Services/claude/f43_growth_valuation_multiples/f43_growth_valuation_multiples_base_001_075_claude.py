import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(2, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(2, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rank(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).rank(pct=True) - 0.5


def _slope(s, w):
    return (s - s.shift(w)) / float(w)


def _pctl_of_last(s, w):
    return s.rolling(w, min_periods=max(2, w // 2)).apply(
        lambda a: (a <= a[-1]).mean(), raw=True)


# ===== folder domain primitives (growth valuation multiples) =====
def _f43gv_evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _f43gv_ps(ps):
    return ps.clip(lower=0)


def _f43gv_evebitda(evebitda):
    return evebitda


def _f43gv_pe(pe):
    return pe


def _f43gv_mcap_sales(marketcap, revenue):
    return marketcap / revenue.replace(0, np.nan)


def _f43gv_ev_ebitda_raw(ev, ebitda):
    return ev / ebitda.replace(0, np.nan)


def _f43gv_cheap_z(level, w):
    # cheapness z: low multiple -> high cheapness; invert the z-score sign
    return -_z(level, w)


def _f43gv_cheap_rank(level, w):
    # low multiple -> high cheapness rank
    return -(_rank(level, w))


# ============================================================
# EV/Sales level (log) -- core unprofitable-growth multiple
def f43gv_f43_growth_valuation_multiples_evsales_lvl_252d_base_v001_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = np.log(es.clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness z vs own 252d history
def f43gv_f43_growth_valuation_multiples_evsales_cheapz_252d_base_v002_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = _f43gv_cheap_z(es, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness z vs own 504d history (longer memory)
def f43gv_f43_growth_valuation_multiples_evsales_cheapz_504d_base_v003_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = _f43gv_cheap_z(es, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness percentile rank vs own 252d history
def f43gv_f43_growth_valuation_multiples_evsales_cheaprank_252d_base_v004_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = _f43gv_cheap_rank(es, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales 63d trend (re-rating slope)
def f43gv_f43_growth_valuation_multiples_evsales_trend_63d_base_v005_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    b = _slope(es, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales 126d trend
def f43gv_f43_growth_valuation_multiples_evsales_trend_126d_base_v006_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    b = _slope(es, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales displacement from its own slow EMA (short-term re-rate)
def f43gv_f43_growth_valuation_multiples_evsales_disp_63d_base_v007_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    b = es - es.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales richness-momentum: short (126d) percentile minus long (504d) percentile
def f43gv_f43_growth_valuation_multiples_evsales_pctl_504d_base_v008_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = _pctl_of_last(es, 126) - _pctl_of_last(es, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S level (log)
def f43gv_f43_growth_valuation_multiples_ps_lvl_base_v009_signal(ps):
    b = np.log(_f43gv_ps(ps).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S cheapness z vs own 252d history
def f43gv_f43_growth_valuation_multiples_ps_cheapz_252d_base_v010_signal(ps):
    b = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S cheapness z vs own 126d history
def f43gv_f43_growth_valuation_multiples_ps_cheapz_126d_base_v011_signal(ps):
    b = _f43gv_cheap_z(_f43gv_ps(ps), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S cheapness rank vs own 504d history
def f43gv_f43_growth_valuation_multiples_ps_cheaprank_504d_base_v012_signal(ps):
    b = _f43gv_cheap_rank(_f43gv_ps(ps), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S 63d trend (re-rating)
def f43gv_f43_growth_valuation_multiples_ps_trend_63d_base_v013_signal(ps):
    lps = np.log(_f43gv_ps(ps).clip(lower=1e-6))
    b = _slope(lps, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S 252d trend (slow re-rating)
def f43gv_f43_growth_valuation_multiples_ps_trend_252d_base_v014_signal(ps):
    lps = np.log(_f43gv_ps(ps).clip(lower=1e-6))
    b = _slope(lps, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S richness-momentum: 63d percentile minus 252d percentile (short vs medium)
def f43gv_f43_growth_valuation_multiples_ps_pctl_252d_base_v015_signal(ps):
    p = _f43gv_ps(ps)
    b = _pctl_of_last(p, 63) - _pctl_of_last(p, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# market-cap/sales (price-to-sales proxy) level (log)
def f43gv_f43_growth_valuation_multiples_mcapsales_lvl_base_v016_signal(marketcap, revenue):
    ms = _f43gv_mcap_sales(marketcap, revenue)
    b = np.log(ms.clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# market-cap/sales cheapness z vs own 252d history
def f43gv_f43_growth_valuation_multiples_mcapsales_cheapz_252d_base_v017_signal(marketcap, revenue):
    ms = _f43gv_mcap_sales(marketcap, revenue)
    b = _f43gv_cheap_z(ms, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# market-cap/sales trend over a quarter
def f43gv_f43_growth_valuation_multiples_mcapsales_trend_63d_base_v018_signal(marketcap, revenue):
    ms = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    b = _slope(ms, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA level (log of clipped multiple)
def f43gv_f43_growth_valuation_multiples_evebitda_lvl_base_v019_signal(evebitda):
    b = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness z vs own 252d history
def f43gv_f43_growth_valuation_multiples_evebitda_cheapz_252d_base_v020_signal(evebitda):
    b = _f43gv_cheap_z(_f43gv_evebitda(evebitda), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness z vs own 504d history
def f43gv_f43_growth_valuation_multiples_evebitda_cheapz_504d_base_v021_signal(evebitda):
    b = _f43gv_cheap_z(_f43gv_evebitda(evebitda), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheapness rank spread: 126d rank minus 504d rank (rank re-rating)
def f43gv_f43_growth_valuation_multiples_evebitda_cheaprank_252d_base_v022_signal(evebitda):
    r_short = _f43gv_cheap_rank(_f43gv_evebitda(evebitda), 126)
    r_long = _f43gv_cheap_rank(_f43gv_evebitda(evebitda), 504)
    b = r_short - r_long
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA 63d trend
def f43gv_f43_growth_valuation_multiples_evebitda_trend_63d_base_v023_signal(evebitda):
    le = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    b = _slope(le, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA 126d trend
def f43gv_f43_growth_valuation_multiples_evebitda_trend_126d_base_v024_signal(evebitda):
    le = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    b = _slope(le, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA richness-momentum: 252d percentile minus 504d percentile
def f43gv_f43_growth_valuation_multiples_evebitda_pctl_504d_base_v025_signal(evebitda):
    e = _f43gv_evebitda(evebitda)
    b = _pctl_of_last(e, 252) - _pctl_of_last(e, 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA built from ev & ebitda directly (negative-EBITDA aware), cheapness z
def f43gv_f43_growth_valuation_multiples_evebitdaraw_cheapz_252d_base_v026_signal(ev, ebitda):
    raw = _f43gv_ev_ebitda_raw(ev, ebitda)
    raw = raw.where(ebitda > 0)
    b = _f43gv_cheap_z(raw, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E level (log of clipped multiple)
def f43gv_f43_growth_valuation_multiples_pe_lvl_base_v027_signal(pe):
    b = np.log(_f43gv_pe(pe).clip(lower=1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E cheapness z vs own 252d history
def f43gv_f43_growth_valuation_multiples_pe_cheapz_252d_base_v028_signal(pe):
    b = _f43gv_cheap_z(_f43gv_pe(pe), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E cheapness rank vs own 504d history
def f43gv_f43_growth_valuation_multiples_pe_cheaprank_504d_base_v029_signal(pe):
    b = _f43gv_cheap_rank(_f43gv_pe(pe), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E 126d trend
def f43gv_f43_growth_valuation_multiples_pe_trend_126d_base_v030_signal(pe):
    lpe = np.log(_f43gv_pe(pe).clip(lower=1e-6))
    b = _slope(lpe, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness rank: average of EV/Sales + P/S cheapness ranks
def f43gv_f43_growth_valuation_multiples_blend_evs_ps_rank_252d_base_v031_signal(ev, revenue, ps):
    r1 = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    r2 = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    b = (r1 + r2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness rank: EV/Sales + EV/EBITDA
def f43gv_f43_growth_valuation_multiples_blend_evs_evebitda_rank_252d_base_v032_signal(ev, revenue, evebitda):
    r1 = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    r2 = _f43gv_cheap_rank(_f43gv_evebitda(evebitda), 252)
    b = (r1 + r2) / 2.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness z: EV/Sales + P/S + EV/EBITDA + P/E (composite cheapness)
def f43gv_f43_growth_valuation_multiples_blend_quad_z_252d_base_v033_signal(ev, revenue, ps, evebitda, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(_f43gv_evebitda(evebitda), 252)
    z4 = _f43gv_cheap_z(_f43gv_pe(pe), 252)
    b = (z1 + z2 + z3 + z4) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales minus P/S divergence (EV premium over equity multiple = net debt signal)
def f43gv_f43_growth_valuation_multiples_evs_ps_spread_base_v034_signal(ev, revenue, ps):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    lps = np.log(_f43gv_ps(ps).clip(lower=1e-6))
    b = es - lps
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA minus EV/Sales spread (margin-implied multiple gap)
def f43gv_f43_growth_valuation_multiples_evebitda_evs_spread_base_v035_signal(evebitda, ev, revenue):
    le = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    b = le - es
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E minus P/S spread (earnings-vs-sales multiple gap)
def f43gv_f43_growth_valuation_multiples_pe_ps_spread_base_v036_signal(pe, ps):
    lpe = np.log(_f43gv_pe(pe).clip(lower=1e-6))
    lps = np.log(_f43gv_ps(ps).clip(lower=1e-6))
    b = lpe - lps
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales re-rating relative to its 252d band (z of short trend)
def f43gv_f43_growth_valuation_multiples_evsales_trendz_base_v037_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    tr = _slope(es, 63)
    b = _z(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA re-rating relative to its 252d band
def f43gv_f43_growth_valuation_multiples_evebitda_trendz_base_v038_signal(evebitda):
    le = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    tr = _slope(le, 63)
    b = _z(tr, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales acceleration of cheapness (cheapz now vs a quarter ago)
def f43gv_f43_growth_valuation_multiples_evsales_cheapzchg_base_v039_signal(ev, revenue):
    cz = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    b = cz - cz.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S cheapness change over a quarter
def f43gv_f43_growth_valuation_multiples_ps_cheapzchg_base_v040_signal(ps):
    cz = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    b = cz - cz.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales tanh-squashed re-rate momentum (bounded)
def f43gv_f43_growth_valuation_multiples_evsales_tanhmom_base_v041_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    chg = es - es.shift(21)
    b = np.tanh(5.0 * chg)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales dispersion (instability of the multiple) over 252d
def f43gv_f43_growth_valuation_multiples_evsales_dispersion_base_v042_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    b = _std(es, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA dispersion over 252d
def f43gv_f43_growth_valuation_multiples_evebitda_dispersion_base_v043_signal(evebitda):
    le = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    b = _std(le, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S vs EV/Sales rank disagreement (capital-structure tilt of cheapness)
def f43gv_f43_growth_valuation_multiples_ps_evs_rankgap_base_v044_signal(ps, ev, revenue):
    r1 = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    r2 = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    b = r1 - r2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied EBITDA margin from multiples (EV/Sales over EV/EBITDA), z-scored vs own 252d band
def f43gv_f43_growth_valuation_multiples_implied_margin_base_v045_signal(ev, revenue, evebitda):
    es = _f43gv_evsales(ev, revenue)
    margin = (es / _f43gv_evebitda(evebitda).replace(0, np.nan)).clip(-2, 2)
    b = _z(margin, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# implied margin trend over a quarter (margin re-rating)
def f43gv_f43_growth_valuation_multiples_implied_margin_trend_base_v046_signal(ev, revenue, evebitda):
    es = _f43gv_evsales(ev, revenue)
    margin = es / _f43gv_evebitda(evebitda).replace(0, np.nan)
    b = _slope(margin.clip(-2, 2), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales vs market-cap/sales gap (net-debt richness, log)
def f43gv_f43_growth_valuation_multiples_ev_mcap_salesgap_base_v047_signal(ev, marketcap, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    ms = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    b = es - ms
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness z minus EV/EBITDA cheapness z (growth-vs-profit cheapness tilt)
def f43gv_f43_growth_valuation_multiples_evs_evebitda_cheapzgap_base_v048_signal(ev, revenue, evebitda):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_evebitda(evebitda), 252)
    b = z1 - z2
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales smoothed EMA level
def f43gv_f43_growth_valuation_multiples_evsales_ema_base_v049_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    b = es.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E cheapness z vs own 126d history
def f43gv_f43_growth_valuation_multiples_pe_cheapz_126d_base_v050_signal(pe):
    b = _f43gv_cheap_z(_f43gv_pe(pe), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales percentile rank vs 126d (short richness)
def f43gv_f43_growth_valuation_multiples_evsales_pctl_126d_base_v051_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    b = _pctl_of_last(es, 126) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S richness convexity: how far the 504d percentile sits from the neutral 0.5 band, squared-signed
def f43gv_f43_growth_valuation_multiples_ps_pctl_504d_base_v052_signal(ps):
    pct = _pctl_of_last(_f43gv_ps(ps), 504)
    dev = pct - 0.5
    b = np.sign(dev) * (dev ** 2) * 4.0 - dev.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA richness convexity vs its 63d-smoothed percentile (displacement)
def f43gv_f43_growth_valuation_multiples_evebitda_pctl_252d_base_v053_signal(evebitda):
    pct = _pctl_of_last(_f43gv_evebitda(evebitda), 252)
    b = pct - pct.ewm(span=63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness rank across all four multiples (full composite rank)
def f43gv_f43_growth_valuation_multiples_blend_all_rank_base_v054_signal(ev, revenue, ps, evebitda, pe):
    r1 = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    r2 = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    r3 = _f43gv_cheap_rank(_f43gv_evebitda(evebitda), 252)
    r4 = _f43gv_cheap_rank(_f43gv_pe(pe), 252)
    b = (r1 + r2 + r3 + r4) / 4.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales mean-reversion gap: level minus its 252d mean
def f43gv_f43_growth_valuation_multiples_evsales_revgap_base_v055_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    b = es - _mean(es, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA mean-reversion gap
def f43gv_f43_growth_valuation_multiples_evebitda_revgap_base_v056_signal(evebitda):
    le = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    b = le - _mean(le, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E mean-reversion gap
def f43gv_f43_growth_valuation_multiples_pe_revgap_base_v057_signal(pe):
    lpe = np.log(_f43gv_pe(pe).clip(lower=1e-6))
    b = lpe - _mean(lpe, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year EV/Sales sat below its 252d mean (persistent cheap regime)
def f43gv_f43_growth_valuation_multiples_evsales_cheapfrac_base_v058_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    cheap = (es < _mean(es, 252)).astype(float)
    b = cheap.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of last year P/S sat above its 252d mean (persistent rich regime)
def f43gv_f43_growth_valuation_multiples_ps_richfrac_base_v059_signal(ps):
    lps = np.log(_f43gv_ps(ps).clip(lower=1e-6))
    rich = (lps > _mean(lps, 252)).astype(float)
    b = rich.rolling(252, min_periods=126).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales year-over-year change (re-rating regime, log)
def f43gv_f43_growth_valuation_multiples_evsales_yoy_base_v060_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    b = es - es.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/S re-rating acceleration: year-over-year change now vs a quarter ago
def f43gv_f43_growth_valuation_multiples_ps_yoy_base_v061_signal(ps):
    lps = np.log(_f43gv_ps(ps).clip(lower=1e-6))
    yoy = lps - lps.shift(252)
    b = yoy - yoy.shift(63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA year-over-year change
def f43gv_f43_growth_valuation_multiples_evebitda_yoy_base_v062_signal(evebitda):
    le = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    b = le - le.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cheapness composite z change over a year (re-rating direction)
def f43gv_f43_growth_valuation_multiples_blend_z_yoy_base_v063_signal(ev, revenue, ps, evebitda):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(_f43gv_evebitda(evebitda), 252)
    comp = (z1 + z2 + z3) / 3.0
    b = comp - comp.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness vs its own short-window cheapness (regime-shift skew)
def f43gv_f43_growth_valuation_multiples_evsales_signmag_base_v064_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    long_cz = _f43gv_cheap_z(es, 504)
    short_cz = _f43gv_cheap_z(es, 63)
    b = long_cz - short_cz
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales interaction: cheapness rank x re-rating trend (cheap & improving)
def f43gv_f43_growth_valuation_multiples_evsales_cheapxtrend_base_v065_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    cr = -(_rank(es, 252))
    tr = _slope(es, 63)
    b = cr * np.tanh(5.0 * tr)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# multiple dispersion across the four cheapness z's (valuation disagreement)
def f43gv_f43_growth_valuation_multiples_blend_zdispersion_base_v066_signal(ev, revenue, ps, evebitda, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(_f43gv_evebitda(evebitda), 252)
    z4 = _f43gv_cheap_z(_f43gv_pe(pe), 252)
    b = pd.concat([z1, z2, z3, z4], axis=1).std(axis=1)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales rich-extreme persistence: smoothed depth above the 70th percentile
def f43gv_f43_growth_valuation_multiples_evsales_richtime_base_v067_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    pct = _pctl_of_last(es, 252)
    rich = (pct - 0.7).clip(lower=0)
    b = rich.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/EBITDA cheap-extreme persistence: smoothed depth below the 30th percentile
def f43gv_f43_growth_valuation_multiples_evebitda_cheaptime_base_v068_signal(evebitda):
    pct = _pctl_of_last(_f43gv_evebitda(evebitda), 252)
    cheap = (0.3 - pct).clip(lower=0)
    b = cheap.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales re-rating information ratio: 126d drift of the multiple per unit of its noise
def f43gv_f43_growth_valuation_multiples_evsales_cheapz_riskadj_base_v069_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    drift = es.diff()
    mu = drift.rolling(126, min_periods=63).mean()
    sd = drift.rolling(126, min_periods=63).std().replace(0, np.nan)
    b = -(mu / sd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# P/E to EV/EBITDA spread (equity vs enterprise earnings multiple)
def f43gv_f43_growth_valuation_multiples_pe_evebitda_spread_base_v070_signal(pe, evebitda):
    lpe = np.log(_f43gv_pe(pe).clip(lower=1e-6))
    le = np.log(_f43gv_evebitda(evebitda).clip(lower=1e-6))
    b = lpe - le
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales momentum curvature: 21d momentum minus 63d momentum (re-rate convexity)
def f43gv_f43_growth_valuation_multiples_evsales_mom_21d_base_v071_signal(ev, revenue):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    m_fast = es - es.shift(21)
    m_slow = (es - es.shift(63)) / 3.0
    b = m_fast - m_slow
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# blended cheapness rank slope (cheapness improving across multiples)
def f43gv_f43_growth_valuation_multiples_blend_rank_slope_base_v072_signal(ev, revenue, ps, evebitda):
    r1 = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    r2 = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    r3 = _f43gv_cheap_rank(_f43gv_evebitda(evebitda), 252)
    comp = (r1 + r2 + r3) / 3.0
    b = _slope(comp, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# EV/Sales cheapness z (504d) change over half a year (memory)
def f43gv_f43_growth_valuation_multiples_evsales_cheapz_lag_base_v073_signal(ev, revenue):
    es = _f43gv_evsales(ev, revenue)
    cz = _f43gv_cheap_z(es, 504)
    b = cz - cz.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# market-cap/sales cheapness rank vs 252d
def f43gv_f43_growth_valuation_multiples_mcapsales_cheaprank_base_v074_signal(marketcap, revenue):
    ms = _f43gv_mcap_sales(marketcap, revenue)
    b = _f43gv_cheap_rank(ms, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite cheapness z (EV/Sales + P/S) interacted with low absolute level
def f43gv_f43_growth_valuation_multiples_blend_z_x_level_base_v075_signal(ev, revenue, ps):
    es = np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))
    z1 = -_z(es, 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    comp = (z1 + z2) / 2.0
    lowlvl = -_rank(es, 504)
    b = comp * (0.5 + lowlvl)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43gv_f43_growth_valuation_multiples_evsales_lvl_252d_base_v001_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapz_252d_base_v002_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapz_504d_base_v003_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheaprank_252d_base_v004_signal,
    f43gv_f43_growth_valuation_multiples_evsales_trend_63d_base_v005_signal,
    f43gv_f43_growth_valuation_multiples_evsales_trend_126d_base_v006_signal,
    f43gv_f43_growth_valuation_multiples_evsales_disp_63d_base_v007_signal,
    f43gv_f43_growth_valuation_multiples_evsales_pctl_504d_base_v008_signal,
    f43gv_f43_growth_valuation_multiples_ps_lvl_base_v009_signal,
    f43gv_f43_growth_valuation_multiples_ps_cheapz_252d_base_v010_signal,
    f43gv_f43_growth_valuation_multiples_ps_cheapz_126d_base_v011_signal,
    f43gv_f43_growth_valuation_multiples_ps_cheaprank_504d_base_v012_signal,
    f43gv_f43_growth_valuation_multiples_ps_trend_63d_base_v013_signal,
    f43gv_f43_growth_valuation_multiples_ps_trend_252d_base_v014_signal,
    f43gv_f43_growth_valuation_multiples_ps_pctl_252d_base_v015_signal,
    f43gv_f43_growth_valuation_multiples_mcapsales_lvl_base_v016_signal,
    f43gv_f43_growth_valuation_multiples_mcapsales_cheapz_252d_base_v017_signal,
    f43gv_f43_growth_valuation_multiples_mcapsales_trend_63d_base_v018_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_lvl_base_v019_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheapz_252d_base_v020_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheapz_504d_base_v021_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheaprank_252d_base_v022_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_trend_63d_base_v023_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_trend_126d_base_v024_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_pctl_504d_base_v025_signal,
    f43gv_f43_growth_valuation_multiples_evebitdaraw_cheapz_252d_base_v026_signal,
    f43gv_f43_growth_valuation_multiples_pe_lvl_base_v027_signal,
    f43gv_f43_growth_valuation_multiples_pe_cheapz_252d_base_v028_signal,
    f43gv_f43_growth_valuation_multiples_pe_cheaprank_504d_base_v029_signal,
    f43gv_f43_growth_valuation_multiples_pe_trend_126d_base_v030_signal,
    f43gv_f43_growth_valuation_multiples_blend_evs_ps_rank_252d_base_v031_signal,
    f43gv_f43_growth_valuation_multiples_blend_evs_evebitda_rank_252d_base_v032_signal,
    f43gv_f43_growth_valuation_multiples_blend_quad_z_252d_base_v033_signal,
    f43gv_f43_growth_valuation_multiples_evs_ps_spread_base_v034_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_evs_spread_base_v035_signal,
    f43gv_f43_growth_valuation_multiples_pe_ps_spread_base_v036_signal,
    f43gv_f43_growth_valuation_multiples_evsales_trendz_base_v037_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_trendz_base_v038_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapzchg_base_v039_signal,
    f43gv_f43_growth_valuation_multiples_ps_cheapzchg_base_v040_signal,
    f43gv_f43_growth_valuation_multiples_evsales_tanhmom_base_v041_signal,
    f43gv_f43_growth_valuation_multiples_evsales_dispersion_base_v042_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_dispersion_base_v043_signal,
    f43gv_f43_growth_valuation_multiples_ps_evs_rankgap_base_v044_signal,
    f43gv_f43_growth_valuation_multiples_implied_margin_base_v045_signal,
    f43gv_f43_growth_valuation_multiples_implied_margin_trend_base_v046_signal,
    f43gv_f43_growth_valuation_multiples_ev_mcap_salesgap_base_v047_signal,
    f43gv_f43_growth_valuation_multiples_evs_evebitda_cheapzgap_base_v048_signal,
    f43gv_f43_growth_valuation_multiples_evsales_ema_base_v049_signal,
    f43gv_f43_growth_valuation_multiples_pe_cheapz_126d_base_v050_signal,
    f43gv_f43_growth_valuation_multiples_evsales_pctl_126d_base_v051_signal,
    f43gv_f43_growth_valuation_multiples_ps_pctl_504d_base_v052_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_pctl_252d_base_v053_signal,
    f43gv_f43_growth_valuation_multiples_blend_all_rank_base_v054_signal,
    f43gv_f43_growth_valuation_multiples_evsales_revgap_base_v055_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_revgap_base_v056_signal,
    f43gv_f43_growth_valuation_multiples_pe_revgap_base_v057_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapfrac_base_v058_signal,
    f43gv_f43_growth_valuation_multiples_ps_richfrac_base_v059_signal,
    f43gv_f43_growth_valuation_multiples_evsales_yoy_base_v060_signal,
    f43gv_f43_growth_valuation_multiples_ps_yoy_base_v061_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_yoy_base_v062_signal,
    f43gv_f43_growth_valuation_multiples_blend_z_yoy_base_v063_signal,
    f43gv_f43_growth_valuation_multiples_evsales_signmag_base_v064_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapxtrend_base_v065_signal,
    f43gv_f43_growth_valuation_multiples_blend_zdispersion_base_v066_signal,
    f43gv_f43_growth_valuation_multiples_evsales_richtime_base_v067_signal,
    f43gv_f43_growth_valuation_multiples_evebitda_cheaptime_base_v068_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapz_riskadj_base_v069_signal,
    f43gv_f43_growth_valuation_multiples_pe_evebitda_spread_base_v070_signal,
    f43gv_f43_growth_valuation_multiples_evsales_mom_21d_base_v071_signal,
    f43gv_f43_growth_valuation_multiples_blend_rank_slope_base_v072_signal,
    f43gv_f43_growth_valuation_multiples_evsales_cheapz_lag_base_v073_signal,
    f43gv_f43_growth_valuation_multiples_mcapsales_cheaprank_base_v074_signal,
    f43gv_f43_growth_valuation_multiples_blend_z_x_level_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_GROWTH_VALUATION_MULTIPLES_REGISTRY_001_075 = REGISTRY


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

    # multiples wander (mean-revert) rather than trend so rank/z/pctl facets stay distinct
    ps = _fund(1, base=8.0, drift=0.0, vol=0.16).clip(lower=0.5).rename("ps")
    evebitda = _fund(2, base=18.0, drift=0.0, vol=0.18).clip(lower=1.0).rename("evebitda")
    pe = _fund(3, base=28.0, drift=0.0, vol=0.20).clip(lower=1.0).rename("pe")
    ev = _fund(4, base=1.2e9, drift=0.02, vol=0.10).rename("ev")
    marketcap = _fund(5, base=1.0e9, drift=0.02, vol=0.10).rename("marketcap")
    revenue = _fund(6, base=2.0e8, drift=0.02, vol=0.07).clip(lower=1e6).rename("revenue")
    ebitda = _fund(7, base=3.0e7, drift=0.01, vol=0.14, allow_neg=True).rename("ebitda")

    cols = {"ps": ps, "evebitda": evebitda, "pe": pe, "ev": ev,
            "marketcap": marketcap, "revenue": revenue, "ebitda": ebitda}

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

    print("OK f43_growth_valuation_multiples_base_001_075_claude: %d features pass" % n_features)
