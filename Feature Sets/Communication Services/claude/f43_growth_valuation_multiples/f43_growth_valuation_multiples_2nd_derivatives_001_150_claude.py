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


def _roc(s, w):
    return (s - s.shift(w)) / float(w)


# ===== folder domain primitives (growth valuation multiples) =====
def _f43gv_evsales(ev, revenue):
    return ev / revenue.replace(0, np.nan)


def _f43gv_ps(ps):
    return ps.clip(lower=0)


def _f43gv_mcap_sales(marketcap, revenue):
    return marketcap / revenue.replace(0, np.nan)


def _f43gv_log_evsales(ev, revenue):
    return np.log(_f43gv_evsales(ev, revenue).clip(lower=1e-6))


def _f43gv_log_ps(ps):
    return np.log(_f43gv_ps(ps).clip(lower=1e-6))


def _f43gv_log_evebitda(evebitda):
    return np.log(evebitda.clip(lower=1e-6))


def _f43gv_log_pe(pe):
    return np.log(pe.clip(lower=1e-6))


def _f43gv_cheap_z(level, w):
    return -_z(level, w)


def _f43gv_cheap_rank(level, w):
    return -(_rank(level, w))


def f43gv_f43_growth_valuation_multiples_evslog_raw_21d_slope_v001_signal(ev, revenue):
    base = _f43gv_log_evsales(ev, revenue)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz252_raw_63d_slope_v002_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz504_raw_126d_slope_v003_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 504)
    d = _roc(base, 126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscr252_raw_63d_slope_v004_signal(ev, revenue):
    base = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsbandpos_raw_21d_slope_v005_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    hi = es.rolling(252, min_periods=126).max()
    lo = es.rolling(252, min_periods=126).min()
    base = (es - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pslog_raw_21d_slope_v006_signal(ps):
    base = _f43gv_log_ps(ps)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscz252_raw_63d_slope_v007_signal(ps):
    base = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscr252_raw_63d_slope_v008_signal(ps):
    base = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_psbandpos_raw_21d_slope_v009_signal(ps):
    lps = _f43gv_log_ps(ps)
    hi = lps.rolling(252, min_periods=126).max()
    lo = lps.rolling(252, min_periods=126).min()
    base = (lps - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitlog_raw_21d_slope_v010_signal(evebitda):
    base = _f43gv_log_evebitda(evebitda)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcz252_raw_63d_slope_v011_signal(evebitda):
    base = _f43gv_cheap_z(evebitda, 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcr252_raw_63d_slope_v012_signal(evebitda):
    base = _f43gv_cheap_rank(evebitda, 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitbandpos_raw_21d_slope_v013_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    hi = le.rolling(252, min_periods=126).max()
    lo = le.rolling(252, min_periods=126).min()
    base = (le - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pelog_raw_21d_slope_v014_signal(pe):
    base = _f43gv_log_pe(pe)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecz252_raw_63d_slope_v015_signal(pe):
    base = _f43gv_cheap_z(pe, 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecr252_raw_63d_slope_v016_signal(pe):
    base = _f43gv_cheap_rank(pe, 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_mcaplog_raw_21d_slope_v017_signal(marketcap, revenue):
    base = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_mcapcz252_raw_63d_slope_v018_signal(marketcap, revenue):
    base = _f43gv_cheap_z(_f43gv_mcap_sales(marketcap, revenue), 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsps_spr_raw_21d_slope_v019_signal(ev, revenue, ps):
    base = _f43gv_log_evsales(ev, revenue) - _f43gv_log_ps(ps)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebs_spr_raw_63d_slope_v020_signal(evebitda, ev, revenue):
    base = _f43gv_log_evebitda(evebitda) - _f43gv_log_evsales(ev, revenue)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_peps_spr_raw_63d_slope_v021_signal(pe, ps):
    base = _f43gv_log_pe(pe) - _f43gv_log_ps(ps)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pevb_spr_raw_63d_slope_v022_signal(pe, evebitda):
    base = _f43gv_log_pe(pe) - _f43gv_log_evebitda(evebitda)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsmcap_spr_raw_63d_slope_v023_signal(ev, marketcap, revenue):
    base = _f43gv_log_evsales(ev, revenue) - np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendz3_raw_63d_slope_v024_signal(ev, revenue, ps, evebitda):
    base = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(evebitda, 252)) / 3.0
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendr4_raw_63d_slope_v025_signal(ev, revenue, ps, evebitda, pe):
    base = (_f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_rank(_f43gv_ps(ps), 252) + _f43gv_cheap_rank(evebitda, 252) + _f43gv_cheap_rank(pe, 252)) / 4.0
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_entz_raw_63d_slope_v026_signal(ev, revenue, evebitda):
    base = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(evebitda, 252)) / 2.0
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_eqz_raw_63d_slope_v027_signal(ps, pe):
    base = (_f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(pe, 252)) / 2.0
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_enteqgap_raw_63d_slope_v028_signal(ev, revenue, evebitda, ps, pe):
    ent = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(evebitda, 252)) / 2.0
    eq = (_f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(pe, 252)) / 2.0
    base = ent - eq
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evspe_ratio_raw_63d_slope_v029_signal(ev, revenue, pe):
    base = _f43gv_log_evsales(ev, revenue) - _f43gv_log_pe(pe)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_implmarginz_raw_63d_slope_v030_signal(ev, revenue, evebitda):
    m = (_f43gv_evsales(ev, revenue) / evebitda.replace(0, np.nan)).clip(-2, 2)
    base = _z(m, 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz126_raw_21d_slope_v031_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 126)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscz126_raw_21d_slope_v032_signal(ps):
    base = _f43gv_cheap_z(_f43gv_ps(ps), 126)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcz126_raw_21d_slope_v033_signal(evebitda):
    base = _f43gv_cheap_z(evebitda, 126)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecz126_raw_21d_slope_v034_signal(pe):
    base = _f43gv_cheap_z(pe, 126)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsdisp_raw_21d_slope_v035_signal(ev, revenue):
    base = _std(_f43gv_log_evsales(ev, revenue), 126)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_psdisp_raw_21d_slope_v036_signal(ps):
    base = _std(_f43gv_log_ps(ps), 126)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitdisp_raw_21d_slope_v037_signal(evebitda):
    base = _std(_f43gv_log_evebitda(evebitda), 126)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsps_rankgap_raw_63d_slope_v038_signal(ev, revenue, ps):
    base = _f43gv_cheap_rank(_f43gv_ps(ps), 252) - _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendzdisp_raw_21d_slope_v039_signal(ev, revenue, ps, evebitda, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(evebitda, 252)
    z4 = _f43gv_cheap_z(pe, 252)
    base = pd.concat([z1, z2, z3, z4], axis=1).std(axis=1)
    d = _roc(base, 21)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evslog_rank63_21d_slope_v040_signal(ev, revenue):
    base = _f43gv_log_evsales(ev, revenue)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz252_rank63_63d_slope_v041_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz504_rank63_126d_slope_v042_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 504)
    d = _roc(base, 126)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscr252_rank63_63d_slope_v043_signal(ev, revenue):
    base = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsbandpos_rank63_21d_slope_v044_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    hi = es.rolling(252, min_periods=126).max()
    lo = es.rolling(252, min_periods=126).min()
    base = (es - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pslog_rank63_21d_slope_v045_signal(ps):
    base = _f43gv_log_ps(ps)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscz252_rank63_63d_slope_v046_signal(ps):
    base = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscr252_rank63_63d_slope_v047_signal(ps):
    base = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_psbandpos_rank63_21d_slope_v048_signal(ps):
    lps = _f43gv_log_ps(ps)
    hi = lps.rolling(252, min_periods=126).max()
    lo = lps.rolling(252, min_periods=126).min()
    base = (lps - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitlog_rank63_21d_slope_v049_signal(evebitda):
    base = _f43gv_log_evebitda(evebitda)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcz252_rank63_63d_slope_v050_signal(evebitda):
    base = _f43gv_cheap_z(evebitda, 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcr252_rank63_63d_slope_v051_signal(evebitda):
    base = _f43gv_cheap_rank(evebitda, 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitbandpos_rank63_21d_slope_v052_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    hi = le.rolling(252, min_periods=126).max()
    lo = le.rolling(252, min_periods=126).min()
    base = (le - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pelog_rank63_21d_slope_v053_signal(pe):
    base = _f43gv_log_pe(pe)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecz252_rank63_63d_slope_v054_signal(pe):
    base = _f43gv_cheap_z(pe, 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecr252_rank63_63d_slope_v055_signal(pe):
    base = _f43gv_cheap_rank(pe, 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_mcaplog_rank63_21d_slope_v056_signal(marketcap, revenue):
    base = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_mcapcz252_rank63_63d_slope_v057_signal(marketcap, revenue):
    base = _f43gv_cheap_z(_f43gv_mcap_sales(marketcap, revenue), 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsps_spr_rank63_21d_slope_v058_signal(ev, revenue, ps):
    base = _f43gv_log_evsales(ev, revenue) - _f43gv_log_ps(ps)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebs_spr_rank63_63d_slope_v059_signal(evebitda, ev, revenue):
    base = _f43gv_log_evebitda(evebitda) - _f43gv_log_evsales(ev, revenue)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_peps_spr_rank63_63d_slope_v060_signal(pe, ps):
    base = _f43gv_log_pe(pe) - _f43gv_log_ps(ps)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pevb_spr_rank63_63d_slope_v061_signal(pe, evebitda):
    base = _f43gv_log_pe(pe) - _f43gv_log_evebitda(evebitda)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsmcap_spr_rank63_63d_slope_v062_signal(ev, marketcap, revenue):
    base = _f43gv_log_evsales(ev, revenue) - np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendz3_rank63_63d_slope_v063_signal(ev, revenue, ps, evebitda):
    base = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(evebitda, 252)) / 3.0
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendr4_rank63_63d_slope_v064_signal(ev, revenue, ps, evebitda, pe):
    base = (_f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_rank(_f43gv_ps(ps), 252) + _f43gv_cheap_rank(evebitda, 252) + _f43gv_cheap_rank(pe, 252)) / 4.0
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_entz_rank63_63d_slope_v065_signal(ev, revenue, evebitda):
    base = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(evebitda, 252)) / 2.0
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_eqz_rank63_63d_slope_v066_signal(ps, pe):
    base = (_f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(pe, 252)) / 2.0
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_enteqgap_rank63_63d_slope_v067_signal(ev, revenue, evebitda, ps, pe):
    ent = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(evebitda, 252)) / 2.0
    eq = (_f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(pe, 252)) / 2.0
    base = ent - eq
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evspe_ratio_rank63_63d_slope_v068_signal(ev, revenue, pe):
    base = _f43gv_log_evsales(ev, revenue) - _f43gv_log_pe(pe)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_implmarginz_rank63_63d_slope_v069_signal(ev, revenue, evebitda):
    m = (_f43gv_evsales(ev, revenue) / evebitda.replace(0, np.nan)).clip(-2, 2)
    base = _z(m, 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz126_rank63_21d_slope_v070_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 126)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscz126_rank63_21d_slope_v071_signal(ps):
    base = _f43gv_cheap_z(_f43gv_ps(ps), 126)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcz126_rank63_21d_slope_v072_signal(evebitda):
    base = _f43gv_cheap_z(evebitda, 126)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecz126_rank63_21d_slope_v073_signal(pe):
    base = _f43gv_cheap_z(pe, 126)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsdisp_rank63_21d_slope_v074_signal(ev, revenue):
    base = _std(_f43gv_log_evsales(ev, revenue), 126)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_psdisp_rank63_21d_slope_v075_signal(ps):
    base = _std(_f43gv_log_ps(ps), 126)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitdisp_rank63_21d_slope_v076_signal(evebitda):
    base = _std(_f43gv_log_evebitda(evebitda), 126)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsps_rankgap_rank63_63d_slope_v077_signal(ev, revenue, ps):
    base = _f43gv_cheap_rank(_f43gv_ps(ps), 252) - _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendzdisp_rank63_21d_slope_v078_signal(ev, revenue, ps, evebitda, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(evebitda, 252)
    z4 = _f43gv_cheap_z(pe, 252)
    base = pd.concat([z1, z2, z3, z4], axis=1).std(axis=1)
    d = _roc(base, 21)
    d = _rank(d, 63)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evslog_acc126_21d_slope_v079_signal(ev, revenue):
    base = _f43gv_log_evsales(ev, revenue)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz252_acc126_63d_slope_v080_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz504_acc126_126d_slope_v081_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 504)
    d = _roc(base, 126)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscr252_acc126_63d_slope_v082_signal(ev, revenue):
    base = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsbandpos_acc126_21d_slope_v083_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    hi = es.rolling(252, min_periods=126).max()
    lo = es.rolling(252, min_periods=126).min()
    base = (es - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pslog_acc126_21d_slope_v084_signal(ps):
    base = _f43gv_log_ps(ps)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscz252_acc126_63d_slope_v085_signal(ps):
    base = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscr252_acc126_63d_slope_v086_signal(ps):
    base = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_psbandpos_acc126_21d_slope_v087_signal(ps):
    lps = _f43gv_log_ps(ps)
    hi = lps.rolling(252, min_periods=126).max()
    lo = lps.rolling(252, min_periods=126).min()
    base = (lps - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitlog_acc126_21d_slope_v088_signal(evebitda):
    base = _f43gv_log_evebitda(evebitda)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcz252_acc126_63d_slope_v089_signal(evebitda):
    base = _f43gv_cheap_z(evebitda, 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcr252_acc126_63d_slope_v090_signal(evebitda):
    base = _f43gv_cheap_rank(evebitda, 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitbandpos_acc126_21d_slope_v091_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    hi = le.rolling(252, min_periods=126).max()
    lo = le.rolling(252, min_periods=126).min()
    base = (le - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pelog_acc126_21d_slope_v092_signal(pe):
    base = _f43gv_log_pe(pe)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecz252_acc126_63d_slope_v093_signal(pe):
    base = _f43gv_cheap_z(pe, 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecr252_acc126_63d_slope_v094_signal(pe):
    base = _f43gv_cheap_rank(pe, 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_mcaplog_acc126_21d_slope_v095_signal(marketcap, revenue):
    base = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_mcapcz252_acc126_63d_slope_v096_signal(marketcap, revenue):
    base = _f43gv_cheap_z(_f43gv_mcap_sales(marketcap, revenue), 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsps_spr_acc126_21d_slope_v097_signal(ev, revenue, ps):
    base = _f43gv_log_evsales(ev, revenue) - _f43gv_log_ps(ps)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebs_spr_acc126_63d_slope_v098_signal(evebitda, ev, revenue):
    base = _f43gv_log_evebitda(evebitda) - _f43gv_log_evsales(ev, revenue)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_peps_spr_acc126_63d_slope_v099_signal(pe, ps):
    base = _f43gv_log_pe(pe) - _f43gv_log_ps(ps)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pevb_spr_acc126_63d_slope_v100_signal(pe, evebitda):
    base = _f43gv_log_pe(pe) - _f43gv_log_evebitda(evebitda)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsmcap_spr_acc126_63d_slope_v101_signal(ev, marketcap, revenue):
    base = _f43gv_log_evsales(ev, revenue) - np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendz3_acc126_63d_slope_v102_signal(ev, revenue, ps, evebitda):
    base = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(evebitda, 252)) / 3.0
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendr4_acc126_63d_slope_v103_signal(ev, revenue, ps, evebitda, pe):
    base = (_f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_rank(_f43gv_ps(ps), 252) + _f43gv_cheap_rank(evebitda, 252) + _f43gv_cheap_rank(pe, 252)) / 4.0
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_entz_acc126_63d_slope_v104_signal(ev, revenue, evebitda):
    base = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(evebitda, 252)) / 2.0
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_eqz_acc126_63d_slope_v105_signal(ps, pe):
    base = (_f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(pe, 252)) / 2.0
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_enteqgap_acc126_63d_slope_v106_signal(ev, revenue, evebitda, ps, pe):
    ent = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(evebitda, 252)) / 2.0
    eq = (_f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(pe, 252)) / 2.0
    base = ent - eq
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evspe_ratio_acc126_63d_slope_v107_signal(ev, revenue, pe):
    base = _f43gv_log_evsales(ev, revenue) - _f43gv_log_pe(pe)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_implmarginz_acc126_63d_slope_v108_signal(ev, revenue, evebitda):
    m = (_f43gv_evsales(ev, revenue) / evebitda.replace(0, np.nan)).clip(-2, 2)
    base = _z(m, 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz126_acc126_21d_slope_v109_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 126)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscz126_acc126_21d_slope_v110_signal(ps):
    base = _f43gv_cheap_z(_f43gv_ps(ps), 126)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcz126_acc126_21d_slope_v111_signal(evebitda):
    base = _f43gv_cheap_z(evebitda, 126)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecz126_acc126_21d_slope_v112_signal(pe):
    base = _f43gv_cheap_z(pe, 126)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsdisp_acc126_21d_slope_v113_signal(ev, revenue):
    base = _std(_f43gv_log_evsales(ev, revenue), 126)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_psdisp_acc126_21d_slope_v114_signal(ps):
    base = _std(_f43gv_log_ps(ps), 126)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitdisp_acc126_21d_slope_v115_signal(evebitda):
    base = _std(_f43gv_log_evebitda(evebitda), 126)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsps_rankgap_acc126_63d_slope_v116_signal(ev, revenue, ps):
    base = _f43gv_cheap_rank(_f43gv_ps(ps), 252) - _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendzdisp_acc126_21d_slope_v117_signal(ev, revenue, ps, evebitda, pe):
    z1 = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    z2 = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    z3 = _f43gv_cheap_z(evebitda, 252)
    z4 = _f43gv_cheap_z(pe, 252)
    base = pd.concat([z1, z2, z3, z4], axis=1).std(axis=1)
    d = _roc(base, 21)
    d = d - d.shift(126)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evslog_smz_21d_slope_v118_signal(ev, revenue):
    base = _f43gv_log_evsales(ev, revenue)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz252_smz_63d_slope_v119_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz504_smz_126d_slope_v120_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 504)
    d = _roc(base, 126)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscr252_smz_63d_slope_v121_signal(ev, revenue):
    base = _f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsbandpos_smz_21d_slope_v122_signal(ev, revenue):
    es = _f43gv_log_evsales(ev, revenue)
    hi = es.rolling(252, min_periods=126).max()
    lo = es.rolling(252, min_periods=126).min()
    base = (es - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pslog_smz_21d_slope_v123_signal(ps):
    base = _f43gv_log_ps(ps)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscz252_smz_63d_slope_v124_signal(ps):
    base = _f43gv_cheap_z(_f43gv_ps(ps), 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscr252_smz_63d_slope_v125_signal(ps):
    base = _f43gv_cheap_rank(_f43gv_ps(ps), 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_psbandpos_smz_21d_slope_v126_signal(ps):
    lps = _f43gv_log_ps(ps)
    hi = lps.rolling(252, min_periods=126).max()
    lo = lps.rolling(252, min_periods=126).min()
    base = (lps - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitlog_smz_21d_slope_v127_signal(evebitda):
    base = _f43gv_log_evebitda(evebitda)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcz252_smz_63d_slope_v128_signal(evebitda):
    base = _f43gv_cheap_z(evebitda, 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcr252_smz_63d_slope_v129_signal(evebitda):
    base = _f43gv_cheap_rank(evebitda, 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitbandpos_smz_21d_slope_v130_signal(evebitda):
    le = _f43gv_log_evebitda(evebitda)
    hi = le.rolling(252, min_periods=126).max()
    lo = le.rolling(252, min_periods=126).min()
    base = (le - lo) / (hi - lo).replace(0, np.nan)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pelog_smz_21d_slope_v131_signal(pe):
    base = _f43gv_log_pe(pe)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecz252_smz_63d_slope_v132_signal(pe):
    base = _f43gv_cheap_z(pe, 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pecr252_smz_63d_slope_v133_signal(pe):
    base = _f43gv_cheap_rank(pe, 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_mcaplog_smz_21d_slope_v134_signal(marketcap, revenue):
    base = np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_mcapcz252_smz_63d_slope_v135_signal(marketcap, revenue):
    base = _f43gv_cheap_z(_f43gv_mcap_sales(marketcap, revenue), 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsps_spr_smz_21d_slope_v136_signal(ev, revenue, ps):
    base = _f43gv_log_evsales(ev, revenue) - _f43gv_log_ps(ps)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebs_spr_smz_63d_slope_v137_signal(evebitda, ev, revenue):
    base = _f43gv_log_evebitda(evebitda) - _f43gv_log_evsales(ev, revenue)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_peps_spr_smz_63d_slope_v138_signal(pe, ps):
    base = _f43gv_log_pe(pe) - _f43gv_log_ps(ps)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pevb_spr_smz_63d_slope_v139_signal(pe, evebitda):
    base = _f43gv_log_pe(pe) - _f43gv_log_evebitda(evebitda)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evsmcap_spr_smz_63d_slope_v140_signal(ev, marketcap, revenue):
    base = _f43gv_log_evsales(ev, revenue) - np.log(_f43gv_mcap_sales(marketcap, revenue).clip(lower=1e-6))
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendz3_smz_63d_slope_v141_signal(ev, revenue, ps, evebitda):
    base = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(evebitda, 252)) / 3.0
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_blendr4_smz_63d_slope_v142_signal(ev, revenue, ps, evebitda, pe):
    base = (_f43gv_cheap_rank(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_rank(_f43gv_ps(ps), 252) + _f43gv_cheap_rank(evebitda, 252) + _f43gv_cheap_rank(pe, 252)) / 4.0
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_entz_smz_63d_slope_v143_signal(ev, revenue, evebitda):
    base = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(evebitda, 252)) / 2.0
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_eqz_smz_63d_slope_v144_signal(ps, pe):
    base = (_f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(pe, 252)) / 2.0
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_enteqgap_smz_63d_slope_v145_signal(ev, revenue, evebitda, ps, pe):
    ent = (_f43gv_cheap_z(_f43gv_evsales(ev, revenue), 252) + _f43gv_cheap_z(evebitda, 252)) / 2.0
    eq = (_f43gv_cheap_z(_f43gv_ps(ps), 252) + _f43gv_cheap_z(pe, 252)) / 2.0
    base = ent - eq
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evspe_ratio_smz_63d_slope_v146_signal(ev, revenue, pe):
    base = _f43gv_log_evsales(ev, revenue) - _f43gv_log_pe(pe)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_implmarginz_smz_63d_slope_v147_signal(ev, revenue, evebitda):
    m = (_f43gv_evsales(ev, revenue) / evebitda.replace(0, np.nan)).clip(-2, 2)
    base = _z(m, 252)
    d = _roc(base, 63)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evscz126_smz_21d_slope_v148_signal(ev, revenue):
    base = _f43gv_cheap_z(_f43gv_evsales(ev, revenue), 126)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_pscz126_smz_21d_slope_v149_signal(ps):
    base = _f43gv_cheap_z(_f43gv_ps(ps), 126)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

def f43gv_f43_growth_valuation_multiples_evebitcz126_smz_21d_slope_v150_signal(evebitda):
    base = _f43gv_cheap_z(evebitda, 126)
    d = _roc(base, 21)
    d = _z(d.ewm(span=21, min_periods=10).mean(), 252)
    result = d
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f43gv_f43_growth_valuation_multiples_evslog_raw_21d_slope_v001_signal,
    f43gv_f43_growth_valuation_multiples_evscz252_raw_63d_slope_v002_signal,
    f43gv_f43_growth_valuation_multiples_evscz504_raw_126d_slope_v003_signal,
    f43gv_f43_growth_valuation_multiples_evscr252_raw_63d_slope_v004_signal,
    f43gv_f43_growth_valuation_multiples_evsbandpos_raw_21d_slope_v005_signal,
    f43gv_f43_growth_valuation_multiples_pslog_raw_21d_slope_v006_signal,
    f43gv_f43_growth_valuation_multiples_pscz252_raw_63d_slope_v007_signal,
    f43gv_f43_growth_valuation_multiples_pscr252_raw_63d_slope_v008_signal,
    f43gv_f43_growth_valuation_multiples_psbandpos_raw_21d_slope_v009_signal,
    f43gv_f43_growth_valuation_multiples_evebitlog_raw_21d_slope_v010_signal,
    f43gv_f43_growth_valuation_multiples_evebitcz252_raw_63d_slope_v011_signal,
    f43gv_f43_growth_valuation_multiples_evebitcr252_raw_63d_slope_v012_signal,
    f43gv_f43_growth_valuation_multiples_evebitbandpos_raw_21d_slope_v013_signal,
    f43gv_f43_growth_valuation_multiples_pelog_raw_21d_slope_v014_signal,
    f43gv_f43_growth_valuation_multiples_pecz252_raw_63d_slope_v015_signal,
    f43gv_f43_growth_valuation_multiples_pecr252_raw_63d_slope_v016_signal,
    f43gv_f43_growth_valuation_multiples_mcaplog_raw_21d_slope_v017_signal,
    f43gv_f43_growth_valuation_multiples_mcapcz252_raw_63d_slope_v018_signal,
    f43gv_f43_growth_valuation_multiples_evsps_spr_raw_21d_slope_v019_signal,
    f43gv_f43_growth_valuation_multiples_evebs_spr_raw_63d_slope_v020_signal,
    f43gv_f43_growth_valuation_multiples_peps_spr_raw_63d_slope_v021_signal,
    f43gv_f43_growth_valuation_multiples_pevb_spr_raw_63d_slope_v022_signal,
    f43gv_f43_growth_valuation_multiples_evsmcap_spr_raw_63d_slope_v023_signal,
    f43gv_f43_growth_valuation_multiples_blendz3_raw_63d_slope_v024_signal,
    f43gv_f43_growth_valuation_multiples_blendr4_raw_63d_slope_v025_signal,
    f43gv_f43_growth_valuation_multiples_entz_raw_63d_slope_v026_signal,
    f43gv_f43_growth_valuation_multiples_eqz_raw_63d_slope_v027_signal,
    f43gv_f43_growth_valuation_multiples_enteqgap_raw_63d_slope_v028_signal,
    f43gv_f43_growth_valuation_multiples_evspe_ratio_raw_63d_slope_v029_signal,
    f43gv_f43_growth_valuation_multiples_implmarginz_raw_63d_slope_v030_signal,
    f43gv_f43_growth_valuation_multiples_evscz126_raw_21d_slope_v031_signal,
    f43gv_f43_growth_valuation_multiples_pscz126_raw_21d_slope_v032_signal,
    f43gv_f43_growth_valuation_multiples_evebitcz126_raw_21d_slope_v033_signal,
    f43gv_f43_growth_valuation_multiples_pecz126_raw_21d_slope_v034_signal,
    f43gv_f43_growth_valuation_multiples_evsdisp_raw_21d_slope_v035_signal,
    f43gv_f43_growth_valuation_multiples_psdisp_raw_21d_slope_v036_signal,
    f43gv_f43_growth_valuation_multiples_evebitdisp_raw_21d_slope_v037_signal,
    f43gv_f43_growth_valuation_multiples_evsps_rankgap_raw_63d_slope_v038_signal,
    f43gv_f43_growth_valuation_multiples_blendzdisp_raw_21d_slope_v039_signal,
    f43gv_f43_growth_valuation_multiples_evslog_rank63_21d_slope_v040_signal,
    f43gv_f43_growth_valuation_multiples_evscz252_rank63_63d_slope_v041_signal,
    f43gv_f43_growth_valuation_multiples_evscz504_rank63_126d_slope_v042_signal,
    f43gv_f43_growth_valuation_multiples_evscr252_rank63_63d_slope_v043_signal,
    f43gv_f43_growth_valuation_multiples_evsbandpos_rank63_21d_slope_v044_signal,
    f43gv_f43_growth_valuation_multiples_pslog_rank63_21d_slope_v045_signal,
    f43gv_f43_growth_valuation_multiples_pscz252_rank63_63d_slope_v046_signal,
    f43gv_f43_growth_valuation_multiples_pscr252_rank63_63d_slope_v047_signal,
    f43gv_f43_growth_valuation_multiples_psbandpos_rank63_21d_slope_v048_signal,
    f43gv_f43_growth_valuation_multiples_evebitlog_rank63_21d_slope_v049_signal,
    f43gv_f43_growth_valuation_multiples_evebitcz252_rank63_63d_slope_v050_signal,
    f43gv_f43_growth_valuation_multiples_evebitcr252_rank63_63d_slope_v051_signal,
    f43gv_f43_growth_valuation_multiples_evebitbandpos_rank63_21d_slope_v052_signal,
    f43gv_f43_growth_valuation_multiples_pelog_rank63_21d_slope_v053_signal,
    f43gv_f43_growth_valuation_multiples_pecz252_rank63_63d_slope_v054_signal,
    f43gv_f43_growth_valuation_multiples_pecr252_rank63_63d_slope_v055_signal,
    f43gv_f43_growth_valuation_multiples_mcaplog_rank63_21d_slope_v056_signal,
    f43gv_f43_growth_valuation_multiples_mcapcz252_rank63_63d_slope_v057_signal,
    f43gv_f43_growth_valuation_multiples_evsps_spr_rank63_21d_slope_v058_signal,
    f43gv_f43_growth_valuation_multiples_evebs_spr_rank63_63d_slope_v059_signal,
    f43gv_f43_growth_valuation_multiples_peps_spr_rank63_63d_slope_v060_signal,
    f43gv_f43_growth_valuation_multiples_pevb_spr_rank63_63d_slope_v061_signal,
    f43gv_f43_growth_valuation_multiples_evsmcap_spr_rank63_63d_slope_v062_signal,
    f43gv_f43_growth_valuation_multiples_blendz3_rank63_63d_slope_v063_signal,
    f43gv_f43_growth_valuation_multiples_blendr4_rank63_63d_slope_v064_signal,
    f43gv_f43_growth_valuation_multiples_entz_rank63_63d_slope_v065_signal,
    f43gv_f43_growth_valuation_multiples_eqz_rank63_63d_slope_v066_signal,
    f43gv_f43_growth_valuation_multiples_enteqgap_rank63_63d_slope_v067_signal,
    f43gv_f43_growth_valuation_multiples_evspe_ratio_rank63_63d_slope_v068_signal,
    f43gv_f43_growth_valuation_multiples_implmarginz_rank63_63d_slope_v069_signal,
    f43gv_f43_growth_valuation_multiples_evscz126_rank63_21d_slope_v070_signal,
    f43gv_f43_growth_valuation_multiples_pscz126_rank63_21d_slope_v071_signal,
    f43gv_f43_growth_valuation_multiples_evebitcz126_rank63_21d_slope_v072_signal,
    f43gv_f43_growth_valuation_multiples_pecz126_rank63_21d_slope_v073_signal,
    f43gv_f43_growth_valuation_multiples_evsdisp_rank63_21d_slope_v074_signal,
    f43gv_f43_growth_valuation_multiples_psdisp_rank63_21d_slope_v075_signal,
    f43gv_f43_growth_valuation_multiples_evebitdisp_rank63_21d_slope_v076_signal,
    f43gv_f43_growth_valuation_multiples_evsps_rankgap_rank63_63d_slope_v077_signal,
    f43gv_f43_growth_valuation_multiples_blendzdisp_rank63_21d_slope_v078_signal,
    f43gv_f43_growth_valuation_multiples_evslog_acc126_21d_slope_v079_signal,
    f43gv_f43_growth_valuation_multiples_evscz252_acc126_63d_slope_v080_signal,
    f43gv_f43_growth_valuation_multiples_evscz504_acc126_126d_slope_v081_signal,
    f43gv_f43_growth_valuation_multiples_evscr252_acc126_63d_slope_v082_signal,
    f43gv_f43_growth_valuation_multiples_evsbandpos_acc126_21d_slope_v083_signal,
    f43gv_f43_growth_valuation_multiples_pslog_acc126_21d_slope_v084_signal,
    f43gv_f43_growth_valuation_multiples_pscz252_acc126_63d_slope_v085_signal,
    f43gv_f43_growth_valuation_multiples_pscr252_acc126_63d_slope_v086_signal,
    f43gv_f43_growth_valuation_multiples_psbandpos_acc126_21d_slope_v087_signal,
    f43gv_f43_growth_valuation_multiples_evebitlog_acc126_21d_slope_v088_signal,
    f43gv_f43_growth_valuation_multiples_evebitcz252_acc126_63d_slope_v089_signal,
    f43gv_f43_growth_valuation_multiples_evebitcr252_acc126_63d_slope_v090_signal,
    f43gv_f43_growth_valuation_multiples_evebitbandpos_acc126_21d_slope_v091_signal,
    f43gv_f43_growth_valuation_multiples_pelog_acc126_21d_slope_v092_signal,
    f43gv_f43_growth_valuation_multiples_pecz252_acc126_63d_slope_v093_signal,
    f43gv_f43_growth_valuation_multiples_pecr252_acc126_63d_slope_v094_signal,
    f43gv_f43_growth_valuation_multiples_mcaplog_acc126_21d_slope_v095_signal,
    f43gv_f43_growth_valuation_multiples_mcapcz252_acc126_63d_slope_v096_signal,
    f43gv_f43_growth_valuation_multiples_evsps_spr_acc126_21d_slope_v097_signal,
    f43gv_f43_growth_valuation_multiples_evebs_spr_acc126_63d_slope_v098_signal,
    f43gv_f43_growth_valuation_multiples_peps_spr_acc126_63d_slope_v099_signal,
    f43gv_f43_growth_valuation_multiples_pevb_spr_acc126_63d_slope_v100_signal,
    f43gv_f43_growth_valuation_multiples_evsmcap_spr_acc126_63d_slope_v101_signal,
    f43gv_f43_growth_valuation_multiples_blendz3_acc126_63d_slope_v102_signal,
    f43gv_f43_growth_valuation_multiples_blendr4_acc126_63d_slope_v103_signal,
    f43gv_f43_growth_valuation_multiples_entz_acc126_63d_slope_v104_signal,
    f43gv_f43_growth_valuation_multiples_eqz_acc126_63d_slope_v105_signal,
    f43gv_f43_growth_valuation_multiples_enteqgap_acc126_63d_slope_v106_signal,
    f43gv_f43_growth_valuation_multiples_evspe_ratio_acc126_63d_slope_v107_signal,
    f43gv_f43_growth_valuation_multiples_implmarginz_acc126_63d_slope_v108_signal,
    f43gv_f43_growth_valuation_multiples_evscz126_acc126_21d_slope_v109_signal,
    f43gv_f43_growth_valuation_multiples_pscz126_acc126_21d_slope_v110_signal,
    f43gv_f43_growth_valuation_multiples_evebitcz126_acc126_21d_slope_v111_signal,
    f43gv_f43_growth_valuation_multiples_pecz126_acc126_21d_slope_v112_signal,
    f43gv_f43_growth_valuation_multiples_evsdisp_acc126_21d_slope_v113_signal,
    f43gv_f43_growth_valuation_multiples_psdisp_acc126_21d_slope_v114_signal,
    f43gv_f43_growth_valuation_multiples_evebitdisp_acc126_21d_slope_v115_signal,
    f43gv_f43_growth_valuation_multiples_evsps_rankgap_acc126_63d_slope_v116_signal,
    f43gv_f43_growth_valuation_multiples_blendzdisp_acc126_21d_slope_v117_signal,
    f43gv_f43_growth_valuation_multiples_evslog_smz_21d_slope_v118_signal,
    f43gv_f43_growth_valuation_multiples_evscz252_smz_63d_slope_v119_signal,
    f43gv_f43_growth_valuation_multiples_evscz504_smz_126d_slope_v120_signal,
    f43gv_f43_growth_valuation_multiples_evscr252_smz_63d_slope_v121_signal,
    f43gv_f43_growth_valuation_multiples_evsbandpos_smz_21d_slope_v122_signal,
    f43gv_f43_growth_valuation_multiples_pslog_smz_21d_slope_v123_signal,
    f43gv_f43_growth_valuation_multiples_pscz252_smz_63d_slope_v124_signal,
    f43gv_f43_growth_valuation_multiples_pscr252_smz_63d_slope_v125_signal,
    f43gv_f43_growth_valuation_multiples_psbandpos_smz_21d_slope_v126_signal,
    f43gv_f43_growth_valuation_multiples_evebitlog_smz_21d_slope_v127_signal,
    f43gv_f43_growth_valuation_multiples_evebitcz252_smz_63d_slope_v128_signal,
    f43gv_f43_growth_valuation_multiples_evebitcr252_smz_63d_slope_v129_signal,
    f43gv_f43_growth_valuation_multiples_evebitbandpos_smz_21d_slope_v130_signal,
    f43gv_f43_growth_valuation_multiples_pelog_smz_21d_slope_v131_signal,
    f43gv_f43_growth_valuation_multiples_pecz252_smz_63d_slope_v132_signal,
    f43gv_f43_growth_valuation_multiples_pecr252_smz_63d_slope_v133_signal,
    f43gv_f43_growth_valuation_multiples_mcaplog_smz_21d_slope_v134_signal,
    f43gv_f43_growth_valuation_multiples_mcapcz252_smz_63d_slope_v135_signal,
    f43gv_f43_growth_valuation_multiples_evsps_spr_smz_21d_slope_v136_signal,
    f43gv_f43_growth_valuation_multiples_evebs_spr_smz_63d_slope_v137_signal,
    f43gv_f43_growth_valuation_multiples_peps_spr_smz_63d_slope_v138_signal,
    f43gv_f43_growth_valuation_multiples_pevb_spr_smz_63d_slope_v139_signal,
    f43gv_f43_growth_valuation_multiples_evsmcap_spr_smz_63d_slope_v140_signal,
    f43gv_f43_growth_valuation_multiples_blendz3_smz_63d_slope_v141_signal,
    f43gv_f43_growth_valuation_multiples_blendr4_smz_63d_slope_v142_signal,
    f43gv_f43_growth_valuation_multiples_entz_smz_63d_slope_v143_signal,
    f43gv_f43_growth_valuation_multiples_eqz_smz_63d_slope_v144_signal,
    f43gv_f43_growth_valuation_multiples_enteqgap_smz_63d_slope_v145_signal,
    f43gv_f43_growth_valuation_multiples_evspe_ratio_smz_63d_slope_v146_signal,
    f43gv_f43_growth_valuation_multiples_implmarginz_smz_63d_slope_v147_signal,
    f43gv_f43_growth_valuation_multiples_evscz126_smz_21d_slope_v148_signal,
    f43gv_f43_growth_valuation_multiples_pscz126_smz_21d_slope_v149_signal,
    f43gv_f43_growth_valuation_multiples_evebitcz126_smz_21d_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F43_GROWTH_VALUATION_MULTIPLES_REGISTRY_001_150_SLOPE = REGISTRY


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

    print("OK f43_growth_valuation_multiples_2nd_derivatives_001_150_claude: %d features pass" % n_features)
