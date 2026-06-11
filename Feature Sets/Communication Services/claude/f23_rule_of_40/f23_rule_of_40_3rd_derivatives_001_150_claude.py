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
    # 2nd math derivative (jerk): discrete second difference over horizon w
    d = s - s.shift(w)
    return d - d.shift(w)


def _slope_norm(s, w, wn):
    # jerk (second difference) normalized by the base's own rolling volatility
    d = s - s.shift(w)
    j = d - d.shift(w)
    return j / _std(s, wn).replace(0, np.nan)


def _slope_lr(s, w):
    # acceleration of the trend = change in the rolling regression slope (jerk form)
    idx = pd.Series(np.arange(len(s), dtype=float), index=s.index)
    cov = s.rolling(w, min_periods=max(2, w // 2)).cov(idx)
    var = idx.rolling(w, min_periods=max(2, w // 2)).var()
    lr = cov / var.replace(0, np.nan)
    return lr - lr.shift(w)


# ===== folder domain primitives (Rule-of-40 = growth + profitability) =====
def _r40_growth(revenue, w):
    return revenue / revenue.shift(w).replace(0, np.nan) - 1.0


def _r40_loggrowth(revenue, w):
    return np.log(revenue.replace(0, np.nan) / revenue.shift(w).replace(0, np.nan))


def _r40_fcf_margin(fcf, revenue):
    return fcf / revenue.replace(0, np.nan)


def _r40_ocf_margin(ncfo, revenue):
    return ncfo / revenue.replace(0, np.nan)


def _r40_score_fcf(revenue, fcf, w):
    return _r40_growth(revenue, w) + _r40_fcf_margin(fcf, revenue)


def _r40_score_ocf(revenue, ncfo, w):
    return _r40_growth(revenue, w) + _r40_ocf_margin(ncfo, revenue)


def _r40_score_ebitda(revenue, ebitdamargin, w):
    return _r40_growth(revenue, w) + ebitdamargin


def _r40_score_gross(revenue, grossmargin, w):
    return _r40_growth(revenue, w) + grossmargin


def _r40_balance(g, m):
    return (g - m) / (g.abs() + m.abs()).replace(0, np.nan)


def _r40_share(g, m):
    return m / (g.abs() + m.abs()).replace(0, np.nan)


# ============================================================
# Each feature = 2nd math derivative (jerk) of a Rule-of-40 base construct.
# Bases are diversified (margin legs / balances / shares / spreads / z / ranks)
# and volatility-normalized so the shared growth-slope does not dominate.

# vol-normalized jerk (acceleration of the slope) of the classic fcf Rule-of-40 score over a quarter
def f23r40_f23_rule_of_40_r40fcf_252d_jerk_v001_signal(revenue, fcf):
    base = _r40_score_fcf(revenue, fcf, 252)
    b = _slope_norm(base, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the ocf Rule-of-40 score over a quarter
def f23r40_f23_rule_of_40_r40ocf_252d_jerk_v002_signal(revenue, ncfo):
    base = _r40_score_ocf(revenue, ncfo, 252)
    b = _slope_norm(base, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the ebitda Rule-of-40 score over a quarter
def f23r40_f23_rule_of_40_r40ebd_252d_jerk_v003_signal(revenue, ebitdamargin):
    base = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = _slope_norm(base, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the gross Rule-of-40 score over a quarter
def f23r40_f23_rule_of_40_r40grs_252d_jerk_v004_signal(revenue, grossmargin):
    base = _r40_score_gross(revenue, grossmargin, 252)
    b = _slope_norm(base, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-margin leg over a 42-day horizon (profitability-leg velocity)
def f23r40_f23_rule_of_40_fcfmgn_jerk_v005_signal(revenue, fcf):
    base = _r40_fcf_margin(fcf, revenue)
    b = _slope(base, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-margin leg over a quarter
def f23r40_f23_rule_of_40_ocfmgn_jerk_v006_signal(revenue, ncfo):
    base = _r40_ocf_margin(ncfo, revenue)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ebitda-margin leg over a quarter
def f23r40_f23_rule_of_40_ebdmgn_jerk_v007_signal(ebitdamargin):
    b = _slope(ebitdamargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross-margin leg over a 42-day horizon
def f23r40_f23_rule_of_40_grsmgn_jerk_v008_signal(grossmargin):
    b = _slope(grossmargin, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# slope of revenue growth (the growth leg) over a quarter
def f23r40_f23_rule_of_40_grow_jerk_v009_signal(revenue):
    base = _r40_growth(revenue, 252)
    b = _slope(base, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-minus-fcf-margin balance over a quarter
def f23r40_f23_rule_of_40_balfcf_jerk_v010_signal(revenue, fcf):
    bal = _r40_balance(_r40_growth(revenue, 252), _r40_fcf_margin(fcf, revenue))
    b = _slope(bal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-minus-ocf-margin balance over a quarter
def f23r40_f23_rule_of_40_balocf_jerk_v011_signal(revenue, ncfo):
    bal = _r40_balance(_r40_growth(revenue, 252), _r40_ocf_margin(ncfo, revenue))
    b = _slope(bal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-minus-ebitda-margin balance over a quarter
def f23r40_f23_rule_of_40_balebd_jerk_v012_signal(revenue, ebitdamargin):
    bal = _r40_balance(_r40_growth(revenue, 252), ebitdamargin)
    b = _slope(bal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-minus-gross-margin balance over a quarter
def f23r40_f23_rule_of_40_balgrs_jerk_v013_signal(revenue, grossmargin):
    bal = _r40_balance(_r40_growth(revenue, 252), grossmargin)
    b = _slope(bal, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-margin share of the absolute fcf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_fcfshare_jerk_v014_signal(revenue, fcf):
    share = _r40_share(_r40_growth(revenue, 252), _r40_fcf_margin(fcf, revenue))
    b = _slope(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-margin share of the absolute ocf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_ocfshare_jerk_v015_signal(revenue, ncfo):
    share = _r40_share(_r40_growth(revenue, 252), _r40_ocf_margin(ncfo, revenue))
    b = _slope(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ebitda-margin share of the absolute ebitda Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_ebdshare_jerk_v016_signal(revenue, ebitdamargin):
    share = _r40_share(_r40_growth(revenue, 252), ebitdamargin)
    b = _slope(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross-margin share of the absolute gross Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_grsshare_jerk_v017_signal(revenue, grossmargin):
    share = _r40_share(_r40_growth(revenue, 252), grossmargin)
    b = _slope(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-minus-ebitda Rule-of-40 spread over a quarter (cash vs accrual)
def f23r40_f23_rule_of_40_sprfcfebd_jerk_v018_signal(revenue, fcf, ebitdamargin):
    spr = _r40_fcf_margin(fcf, revenue) - ebitdamargin
    b = _slope(spr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-minus-fcf margin spread over a quarter (capex drag)
def f23r40_f23_rule_of_40_sprocffcf_jerk_v019_signal(revenue, ncfo, fcf):
    spr = _r40_ocf_margin(ncfo, revenue) - _r40_fcf_margin(fcf, revenue)
    b = _slope(spr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross-minus-ebitda margin spread over a quarter (opex absorption)
def f23r40_f23_rule_of_40_sprgrsebd_jerk_v020_signal(grossmargin, ebitdamargin):
    spr = grossmargin - ebitdamargin
    b = _slope(spr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the z-scored fcf Rule-of-40 score over a month
def f23r40_f23_rule_of_40_r40fcfz_jerk_v021_signal(revenue, fcf):
    z = _z(_r40_score_fcf(revenue, fcf, 252), 252)
    b = _slope(z, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the z-scored ocf Rule-of-40 score over a month
def f23r40_f23_rule_of_40_r40ocfz_jerk_v022_signal(revenue, ncfo):
    z = _z(_r40_score_ocf(revenue, ncfo, 252), 252)
    b = _slope(z, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the z-scored ebitda Rule-of-40 score over a month
def f23r40_f23_rule_of_40_r40ebdz_jerk_v023_signal(revenue, ebitdamargin):
    z = _z(_r40_score_ebitda(revenue, ebitdamargin, 252), 252)
    b = _slope(z, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked fcf-margin over a quarter
def f23r40_f23_rule_of_40_fcfpct_jerk_v024_signal(revenue, fcf):
    pct = _rank(_r40_fcf_margin(fcf, revenue), 504)
    b = _slope(pct, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked ebitda-margin over a quarter
def f23r40_f23_rule_of_40_ebdpct_jerk_v025_signal(ebitdamargin):
    pct = _rank(ebitdamargin, 504)
    b = _slope(pct, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the fcf Rule-of-40 score over a half-year
def f23r40_f23_rule_of_40_r40fcf_slow_jerk_v026_signal(revenue, fcf):
    base = _r40_score_fcf(revenue, fcf, 252)
    b = _slope_norm(base, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the ocf Rule-of-40 score over a half-year
def f23r40_f23_rule_of_40_r40ocf_slow_jerk_v027_signal(revenue, ncfo):
    base = _r40_score_ocf(revenue, ncfo, 252)
    b = _slope_norm(base, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the ebitda Rule-of-40 score over a half-year
def f23r40_f23_rule_of_40_r40ebd_slow_jerk_v028_signal(revenue, ebitdamargin):
    base = _r40_score_ebitda(revenue, ebitdamargin, 252)
    b = _slope_norm(base, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the gross Rule-of-40 score over a half-year
def f23r40_f23_rule_of_40_r40grs_slow_jerk_v029_signal(revenue, grossmargin):
    base = _r40_score_gross(revenue, grossmargin, 252)
    b = _slope_norm(base, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-margin leg over a month (fast profitability velocity)
def f23r40_f23_rule_of_40_fcfmgn_fast_jerk_v030_signal(revenue, fcf):
    base = _r40_fcf_margin(fcf, revenue)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-margin leg over a month
def f23r40_f23_rule_of_40_ocfmgn_fast_jerk_v031_signal(revenue, ncfo):
    base = _r40_ocf_margin(ncfo, revenue)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ebitda-margin leg over a month
def f23r40_f23_rule_of_40_ebdmgn_fast_jerk_v032_signal(ebitdamargin):
    b = _slope(ebitdamargin, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross-margin leg over a month
def f23r40_f23_rule_of_40_grsmgn_fast_jerk_v033_signal(grossmargin):
    b = _slope(grossmargin, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-margin leg over a half-year (slow profitability trend)
def f23r40_f23_rule_of_40_fcfmgn_slow_jerk_v034_signal(revenue, fcf):
    base = _r40_fcf_margin(fcf, revenue)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-margin leg over a half-year
def f23r40_f23_rule_of_40_ocfmgn_slow_jerk_v035_signal(revenue, ncfo):
    base = _r40_ocf_margin(ncfo, revenue)
    b = _slope(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ebitda-margin leg over a half-year
def f23r40_f23_rule_of_40_ebdmgn_slow_jerk_v036_signal(ebitdamargin):
    b = _slope(ebitdamargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross-margin leg over a half-year
def f23r40_f23_rule_of_40_grsmgn_slow_jerk_v037_signal(grossmargin):
    b = _slope(grossmargin, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-margin deviation-from-EMA over a quarter (mean-reversion velocity)
def f23r40_f23_rule_of_40_fcfmgndev_jerk_v038_signal(revenue, fcf):
    m = _r40_fcf_margin(fcf, revenue)
    dev = m - m.ewm(span=126, min_periods=42).mean()
    b = _slope(dev, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-margin deviation-from-EMA over a quarter
def f23r40_f23_rule_of_40_ocfmgndev_jerk_v039_signal(revenue, ncfo):
    m = _r40_ocf_margin(ncfo, revenue)
    dev = m - m.ewm(span=126, min_periods=42).mean()
    b = _slope(dev, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ebitda-margin deviation-from-EMA over a quarter
def f23r40_f23_rule_of_40_ebdmgndev_jerk_v040_signal(ebitdamargin):
    dev = ebitdamargin - ebitdamargin.ewm(span=126, min_periods=42).mean()
    b = _slope(dev, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross-margin deviation-from-EMA over a quarter
def f23r40_f23_rule_of_40_grsmgndev_jerk_v041_signal(grossmargin):
    dev = grossmargin - grossmargin.ewm(span=126, min_periods=42).mean()
    b = _slope(dev, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the reinvestment ratio (fcf-margin / ocf-margin) over a quarter
def f23r40_f23_rule_of_40_reinv_jerk_v042_signal(revenue, ncfo, fcf):
    fm = _r40_fcf_margin(fcf, revenue)
    om = _r40_ocf_margin(ncfo, revenue)
    ratio = np.log((fm.abs() + 1e-6) / (om.abs() + 1e-6))
    b = _slope(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the dual-quality (fcf-margin x ebitda-margin) leg over a quarter
def f23r40_f23_rule_of_40_dualfe_jerk_v043_signal(revenue, fcf, ebitdamargin):
    dual = _r40_fcf_margin(fcf, revenue) * ebitdamargin
    b = _slope(dual, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the cohesion of the three margin legs over a quarter
def f23r40_f23_rule_of_40_cohesion_jerk_v044_signal(revenue, fcf, ncfo, ebitdamargin):
    legs = pd.concat([_r40_fcf_margin(fcf, revenue), _r40_ocf_margin(ncfo, revenue), ebitdamargin], axis=1)
    cohesion = legs.mean(axis=1) - (legs.max(axis=1) - legs.min(axis=1))
    b = _slope(cohesion, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the dispersion of the three margin legs over a quarter
def f23r40_f23_rule_of_40_mgndisp_jerk_v045_signal(revenue, fcf, ncfo, ebitdamargin):
    legs = pd.concat([_r40_fcf_margin(fcf, revenue), _r40_ocf_margin(ncfo, revenue), ebitdamargin], axis=1)
    b = _slope(legs.std(axis=1), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the fast-growth + slow-fcf-margin mixed R40 over a month
def f23r40_f23_rule_of_40_mixfcf_jerk_v046_signal(revenue, fcf):
    score = _r40_growth(revenue, 63) + _mean(_r40_fcf_margin(fcf, revenue), 252)
    b = _slope_norm(score, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the fast-growth + slow-ebitda-margin mixed R40 over a month
def f23r40_f23_rule_of_40_mixebd_jerk_v047_signal(revenue, ebitdamargin):
    score = _r40_growth(revenue, 63) + _mean(ebitdamargin, 252)
    b = _slope_norm(score, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-curvature (quarterly-minus-annual growth) over a quarter
def f23r40_f23_rule_of_40_growcurv_jerk_v048_signal(revenue):
    curv = _r40_growth(revenue, 63) - _r40_growth(revenue, 252)
    b = _slope(curv, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked growth x avg-margin quality composite over a quarter
def f23r40_f23_rule_of_40_growqual_jerk_v049_signal(revenue, fcf, ncfo, ebitdamargin):
    g = _r40_growth(revenue, 252)
    qual = (_r40_fcf_margin(fcf, revenue) + _r40_ocf_margin(ncfo, revenue) + ebitdamargin) / 3.0
    rscore = _rank(g * (0.5 + qual), 504)
    b = _slope(rscore, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked gross-margin-scaled ocf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_grsmult_jerk_v050_signal(revenue, ncfo, grossmargin):
    rscore = _rank(_r40_score_ocf(revenue, ncfo, 252) * (0.5 + grossmargin), 504)
    b = _slope(rscore, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the standardized-growth + standardized-fcf-margin sum over a month
def f23r40_f23_rule_of_40_zsumfcf_jerk_v051_signal(revenue, fcf):
    zsum = _z(_r40_growth(revenue, 252), 252) + _z(_r40_fcf_margin(fcf, revenue), 252)
    b = _slope(zsum, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the standardized-growth + standardized-ebitda-margin sum over a month
def f23r40_f23_rule_of_40_zsumebd_jerk_v052_signal(revenue, ebitdamargin):
    zsum = _z(_r40_growth(revenue, 252), 252) + _z(ebitdamargin, 252)
    b = _slope(zsum, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the standardized-growth minus standardized-fcf-margin spread over a month
def f23r40_f23_rule_of_40_zsprfcf_jerk_v053_signal(revenue, fcf):
    zspr = _z(_r40_growth(revenue, 252), 252) - _z(_r40_fcf_margin(fcf, revenue), 252)
    b = _slope(zspr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the standardized-growth minus standardized-ocf-margin spread over a month
def f23r40_f23_rule_of_40_zsprocf_jerk_v054_signal(revenue, ncfo):
    zspr = _z(_r40_growth(revenue, 252), 252) - _z(_r40_ocf_margin(ncfo, revenue), 252)
    b = _slope(zspr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the standardized-growth minus standardized-ebitda-margin spread over a month
def f23r40_f23_rule_of_40_zsprebd_jerk_v055_signal(revenue, ebitdamargin):
    zspr = _z(_r40_growth(revenue, 252), 252) - _z(ebitdamargin, 252)
    b = _slope(zspr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf retention ratio (fcf as a fraction of ocf) over a quarter
def f23r40_f23_rule_of_40_cashconv_jerk_v056_signal(fcf, ncfo):
    ratio = (fcf.abs() / (ncfo.abs() + fcf.abs())).clip(0, 1)
    b = _slope(ratio, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the capex-retention (ebitda/gross margin) ratio over a quarter
def f23r40_f23_rule_of_40_retain_jerk_v057_signal(grossmargin, ebitdamargin):
    retain = ebitdamargin / grossmargin.replace(0, np.nan)
    b = _slope(retain, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the efficiency (growth per fcf burn) composite over a quarter
def f23r40_f23_rule_of_40_effburn_jerk_v058_signal(revenue, fcf):
    g = _r40_growth(revenue, 252).clip(lower=0)
    burn = (-_r40_fcf_margin(fcf, revenue)).clip(lower=0)
    eff = (g - burn) / (g + burn + 0.05)
    b = _slope(eff, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the signed-root growth-minus-fcf-margin gap over a quarter
def f23r40_f23_rule_of_40_signgapfcf_jerk_v059_signal(revenue, fcf):
    gap = _r40_growth(revenue, 252) - _r40_fcf_margin(fcf, revenue)
    sr = np.sign(gap) * (gap.abs() ** 0.5)
    b = _slope(sr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the signed-root growth-minus-ocf-margin gap over a quarter
def f23r40_f23_rule_of_40_signgapocf_jerk_v060_signal(revenue, ncfo):
    gap = _r40_growth(revenue, 252) - _r40_ocf_margin(ncfo, revenue)
    sr = np.sign(gap) * (gap.abs() ** 0.5)
    b = _slope(sr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the harmonic growth-margin quality (fcf) over a quarter
def f23r40_f23_rule_of_40_harmfcf_jerk_v061_signal(revenue, fcf):
    g = _r40_growth(revenue, 252).clip(lower=0) + 0.01
    m = _r40_fcf_margin(fcf, revenue).clip(lower=0) + 0.01
    harm = 2.0 * g * m / (g + m)
    b = _slope(harm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the harmonic growth-margin quality (ocf) over a quarter
def f23r40_f23_rule_of_40_harmocf_jerk_v062_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252).clip(lower=0) + 0.01
    m = _r40_ocf_margin(ncfo, revenue).clip(lower=0) + 0.01
    harm = 2.0 * g * m / (g + m)
    b = _slope(harm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth x fcf-margin-trend interaction over a quarter
def f23r40_f23_rule_of_40_growxtrend_jerk_v063_signal(revenue, fcf):
    g = _r40_growth(revenue, 252)
    mtrend = _r40_fcf_margin(fcf, revenue) - _r40_fcf_margin(fcf, revenue).shift(126)
    b = _slope(g * mtrend, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth x ebitda-margin-trend interaction over a quarter
def f23r40_f23_rule_of_40_growxebdtrend_jerk_v064_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 252)
    mtrend = ebitdamargin - ebitdamargin.shift(126)
    b = _slope(g * mtrend, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth x fcf-margin interaction over a half-year
def f23r40_f23_rule_of_40_qfcf_slow_jerk_v065_signal(revenue, fcf):
    q = _r40_growth(revenue, 252) * _r40_fcf_margin(fcf, revenue)
    b = _slope_norm(q, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked growth x ebitda-margin interaction over a quarter
def f23r40_f23_rule_of_40_qebd_slow_jerk_v066_signal(revenue, ebitdamargin):
    q = _r40_growth(revenue, 252) * ebitdamargin
    b = _slope(_rank(q, 504), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth x gross-margin interaction over a half-year
def f23r40_f23_rule_of_40_qgrs_slow_jerk_v067_signal(revenue, grossmargin):
    q = _r40_growth(revenue, 252) * grossmargin
    b = _slope_norm(q, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth x ocf-margin interaction over a half-year
def f23r40_f23_rule_of_40_qocf_slow_jerk_v068_signal(revenue, ncfo):
    q = _r40_growth(revenue, 252) * _r40_ocf_margin(ncfo, revenue)
    b = _slope_norm(q, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-margin to semiannual-growth lead over a month (profit-vs-fast-growth)
def f23r40_f23_rule_of_40_qualpurefcf_jerk_v069_signal(revenue, fcf):
    lead = _r40_fcf_margin(fcf, revenue) - _r40_growth(revenue, 126)
    b = _slope(lead, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-margin to semiannual-growth lead over a month
def f23r40_f23_rule_of_40_qualpureocf_jerk_v070_signal(revenue, ncfo):
    lead = _r40_ocf_margin(ncfo, revenue) - _r40_growth(revenue, 126)
    b = _slope(lead, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-acceleration leg over a quarter
def f23r40_f23_rule_of_40_growacc_jerk_v071_signal(revenue):
    gacc = _r40_growth(revenue, 252) - _r40_growth(revenue, 252).shift(252)
    b = _slope(gacc, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked gross Rule-of-40 score over a quarter
def f23r40_f23_rule_of_40_r40grsrank_jerk_v072_signal(revenue, grossmargin):
    base = _rank(_r40_score_gross(revenue, grossmargin, 252), 504)
    b = _slope(base, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the dual-quality (gross x ocf-margin) leg over a quarter
def f23r40_f23_rule_of_40_dualgo_jerk_v073_signal(revenue, ncfo, grossmargin):
    dual = grossmargin * _r40_ocf_margin(ncfo, revenue)
    b = _slope_norm(dual, 63, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the dual-quality (fcf x gross-margin) leg over a quarter
def f23r40_f23_rule_of_40_dualfg_jerk_v074_signal(revenue, fcf, grossmargin):
    dual = _r40_fcf_margin(fcf, revenue) * grossmargin
    b = _slope(dual, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the EMA-smoothed fcf Rule-of-40 score over a month, vol-normalized
def f23r40_f23_rule_of_40_r40fcfema_jerk_v075_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    ema = score.ewm(span=63, min_periods=21).mean()
    b = _slope_norm(ema, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the EMA-smoothed ebitda Rule-of-40 score over a month, vol-normalized
def f23r40_f23_rule_of_40_r40ebdema_jerk_v076_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    ema = score.ewm(span=63, min_periods=21).mean()
    b = _slope_norm(ema, 21, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the dual ebitda x gross margin quality over a quarter
def f23r40_f23_rule_of_40_dualeg_jerk_v077_signal(ebitdamargin, grossmargin):
    dual = ebitdamargin * grossmargin
    b = _slope(dual, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-vs-ebitda consensus gap (which Rule-of-40 definition is binding) over a quarter
def f23r40_f23_rule_of_40_consmin_jerk_v078_signal(revenue, fcf, ebitdamargin):
    sf = _r40_score_fcf(revenue, fcf, 252)
    se = _r40_score_ebitda(revenue, ebitdamargin, 252)
    gap = pd.concat([sf, se], axis=1).min(axis=1) - 0.5 * (sf + se)
    b = _slope(gap, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-vs-gross consensus headroom (best definition over the average) over a quarter
def f23r40_f23_rule_of_40_consmax_jerk_v079_signal(revenue, ncfo, grossmargin):
    so = _r40_score_ocf(revenue, ncfo, 252)
    sg = _r40_score_gross(revenue, grossmargin, 252)
    headroom = pd.concat([so, sg], axis=1).max(axis=1) - 0.5 * (so + sg)
    b = _slope(headroom, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the consensus range (max-minus-min) across Rule-of-40 variants over a month
def f23r40_f23_rule_of_40_consrange_jerk_v080_signal(revenue, fcf, ncfo, ebitdamargin):
    sf = _r40_score_fcf(revenue, fcf, 252)
    so = _r40_score_ocf(revenue, ncfo, 252)
    se = _r40_score_ebitda(revenue, ebitdamargin, 252)
    stacked = pd.concat([sf, so, se], axis=1)
    rng = stacked.max(axis=1) - stacked.min(axis=1)
    b = _slope(rng, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the log-growth minus fcf-margin tradeoff over a quarter
def f23r40_f23_rule_of_40_loggapfcf_jerk_v081_signal(revenue, fcf):
    gap = _r40_loggrowth(revenue, 252) - _r40_fcf_margin(fcf, revenue)
    b = _slope(gap, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the log-growth minus ocf-margin tradeoff over a half-year (slow trade-off)
def f23r40_f23_rule_of_40_loggapocf_jerk_v082_signal(revenue, ncfo):
    gap = _r40_loggrowth(revenue, 252) - _r40_ocf_margin(ncfo, revenue)
    b = _slope(gap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked ocf-margin over a quarter
def f23r40_f23_rule_of_40_ocfpct_jerk_v083_signal(revenue, ncfo):
    pct = _rank(_r40_ocf_margin(ncfo, revenue), 504)
    b = _slope(pct, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked gross-margin over a quarter
def f23r40_f23_rule_of_40_grspct_jerk_v084_signal(grossmargin):
    pct = _rank(grossmargin, 504)
    b = _slope(pct, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the rank-space fcf Rule-of-40 (avg of growth & margin ranks) over a quarter
def f23r40_f23_rule_of_40_rankblendfcf_jerk_v085_signal(revenue, fcf):
    rb = 0.5 * (_rank(_r40_growth(revenue, 252), 504) + _rank(_r40_fcf_margin(fcf, revenue), 504))
    b = _slope(rb, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the rank-space ebitda Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_rankblendebd_jerk_v086_signal(revenue, ebitdamargin):
    rb = 0.5 * (_rank(_r40_growth(revenue, 252), 504) + _rank(ebitdamargin, 504))
    b = _slope(rb, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-minus-fcf-margin balance over a month (fast tradeoff velocity)
def f23r40_f23_rule_of_40_balfcf_fast_jerk_v087_signal(revenue, fcf):
    bal = _r40_balance(_r40_growth(revenue, 252), _r40_fcf_margin(fcf, revenue))
    b = _slope(bal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-minus-ebitda-margin balance over a month
def f23r40_f23_rule_of_40_balebd_fast_jerk_v088_signal(revenue, ebitdamargin):
    bal = _r40_balance(_r40_growth(revenue, 252), ebitdamargin)
    b = _slope(bal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the worst-leg margin relative to the leg mean (downside-leg gap) over a quarter
def f23r40_f23_rule_of_40_worstleg_jerk_v089_signal(revenue, fcf, ncfo, ebitdamargin):
    legs = pd.concat([_r40_fcf_margin(fcf, revenue), _r40_ocf_margin(ncfo, revenue), ebitdamargin], axis=1)
    rel = legs.min(axis=1) - legs.mean(axis=1)
    b = _slope(rel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the best-leg margin relative to the leg mean (upside-leg gap) over a quarter
def f23r40_f23_rule_of_40_bestleg_jerk_v090_signal(revenue, fcf, ncfo, ebitdamargin):
    legs = pd.concat([_r40_fcf_margin(fcf, revenue), _r40_ocf_margin(ncfo, revenue), ebitdamargin], axis=1)
    rel = legs.max(axis=1) - legs.mean(axis=1)
    b = _slope(rel, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the leg spread (max-minus-min margin) over a quarter
def f23r40_f23_rule_of_40_legspread_jerk_v091_signal(revenue, fcf, ncfo, ebitdamargin):
    legs = pd.concat([_r40_fcf_margin(fcf, revenue), _r40_ocf_margin(ncfo, revenue), ebitdamargin], axis=1)
    spread = legs.max(axis=1) - legs.min(axis=1)
    b = _slope(spread, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the dual fcf x ebitda over a half-year
def f23r40_f23_rule_of_40_dualfe_slow_jerk_v092_signal(revenue, fcf, ebitdamargin):
    dual = _r40_fcf_margin(fcf, revenue) * ebitdamargin
    b = _slope(dual, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the reinvestment gap over a half-year
def f23r40_f23_rule_of_40_reinv_slow_jerk_v093_signal(revenue, ncfo, fcf):
    fm = _r40_fcf_margin(fcf, revenue)
    om = _r40_ocf_margin(ncfo, revenue)
    reinvest = (om - fm) / (om.abs() + fm.abs()).replace(0, np.nan)
    b = _slope(reinvest, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression jerk (acceleration of the slope) of the fcf-margin leg over a half-year
def f23r40_f23_rule_of_40_fcfmgnlr_slow_jerk_v094_signal(revenue, fcf):
    base = _r40_fcf_margin(fcf, revenue)
    b = _slope_lr(base, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression jerk (acceleration of the slope) of the ocf-margin leg over a half-year
def f23r40_f23_rule_of_40_ocfmgnlr_slow_jerk_v095_signal(revenue, ncfo):
    base = _r40_ocf_margin(ncfo, revenue)
    b = _slope_lr(base, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# regression jerk (acceleration of the slope) of the ebitda-margin leg over a half-year
def f23r40_f23_rule_of_40_ebdmgnlr_slow_jerk_v096_signal(ebitdamargin):
    b = _slope_lr(ebitdamargin, 189)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross-margin deviation-from-EMA over a half-year
def f23r40_f23_rule_of_40_grsmgndev_slow_jerk_v097_signal(grossmargin):
    dev = grossmargin - grossmargin.ewm(span=189, min_periods=63).mean()
    b = _slope(dev, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked four-leg blended Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_blendall_jerk_v098_signal(revenue, fcf, ncfo, ebitdamargin):
    g = _r40_growth(revenue, 252)
    m = (_r40_fcf_margin(fcf, revenue) + _r40_ocf_margin(ncfo, revenue) + ebitdamargin) / 3.0
    b = _slope(_rank(g + m, 504), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-vs-burn efficiency (ocf) over a quarter
def f23r40_f23_rule_of_40_effocfburn_jerk_v099_signal(revenue, ncfo):
    g = _r40_growth(revenue, 252).clip(lower=0)
    burn = (-_r40_ocf_margin(ncfo, revenue)).clip(lower=0)
    eff = (g - burn) / (g + burn + 0.05)
    b = _slope(eff, 42)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the signed-root growth-minus-ebitda gap over a quarter
def f23r40_f23_rule_of_40_signgapebd_jerk_v100_signal(revenue, ebitdamargin):
    gap = _r40_growth(revenue, 252) - ebitdamargin
    sr = np.sign(gap) * (gap.abs() ** 0.5)
    b = _slope(sr, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross-margin-share over a month (fast profitability-contribution velocity)
def f23r40_f23_rule_of_40_grsshare_fast_jerk_v101_signal(revenue, grossmargin):
    share = _r40_share(_r40_growth(revenue, 252), grossmargin)
    b = _slope(share, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-margin-share over a month
def f23r40_f23_rule_of_40_ocfshare_fast_jerk_v102_signal(revenue, ncfo):
    share = _r40_share(_r40_growth(revenue, 252), _r40_ocf_margin(ncfo, revenue))
    b = _slope(share, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the z-scored gross Rule-of-40 score over a month
def f23r40_f23_rule_of_40_r40grsz_jerk_v103_signal(revenue, grossmargin):
    z = _z(_r40_score_gross(revenue, grossmargin, 252), 252)
    b = _slope(z, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth x ocf-margin interaction over a quarter
def f23r40_f23_rule_of_40_qocf_jerk_v104_signal(revenue, ncfo):
    q = _r40_growth(revenue, 252) * _r40_ocf_margin(ncfo, revenue)
    b = _slope(q, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the standardized-growth + standardized-ocf-margin sum over a month
def f23r40_f23_rule_of_40_zsumocf_jerk_v105_signal(revenue, ncfo):
    zsum = _z(_r40_growth(revenue, 252), 252) + _z(_r40_ocf_margin(ncfo, revenue), 252)
    b = _slope(zsum, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the durability (mean-minus-std) fcf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_durfcf_jerk_v106_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    dur = _mean(score, 252) - _std(score, 252)
    b = _slope(dur, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the durability (mean-minus-std) ocf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_durocf_jerk_v107_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    dur = _mean(score, 252) - _std(score, 252)
    b = _slope(dur, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf Rule-of-40 score volatility over a quarter
def f23r40_f23_rule_of_40_volfcf_jerk_v108_signal(revenue, fcf):
    vol = _std(_r40_score_fcf(revenue, fcf, 252), 252)
    b = _slope(vol, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross x ocf dual quality, vol-normalized over a half-year
def f23r40_f23_rule_of_40_dualgo_slow_jerk_v109_signal(revenue, ncfo, grossmargin):
    dual = grossmargin * _r40_ocf_margin(ncfo, revenue)
    b = _slope_norm(dual, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the capex-retention ratio over a half-year
def f23r40_f23_rule_of_40_retain_slow_jerk_v110_signal(grossmargin, ebitdamargin):
    retain = ebitdamargin / grossmargin.replace(0, np.nan)
    b = _slope(retain, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# vol-normalized jerk (acceleration of the slope) of the fast-growth + slow-ocf-margin mixed R40 over a month
def f23r40_f23_rule_of_40_mixocf_jerk_v111_signal(revenue, ncfo):
    score = _r40_growth(revenue, 63) + _mean(_r40_ocf_margin(ncfo, revenue), 252)
    b = _slope_norm(score, 21, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-tilted ebitda Rule-of-40 balance (growth-vs-margin), over a quarter
def f23r40_f23_rule_of_40_grtiltebd_jerk_v112_signal(revenue, ebitdamargin):
    g = _r40_growth(revenue, 252)
    share = (0.5 * ebitdamargin) / (1.5 * g.abs() + 0.5 * ebitdamargin.abs()).replace(0, np.nan)
    b = _slope(share, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the margin-tilted fcf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_mgtiltfcf_jerk_v113_signal(revenue, fcf):
    score = 0.5 * _r40_growth(revenue, 252) + 1.5 * _r40_fcf_margin(fcf, revenue)
    b = _slope(score, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the margin-tilted ocf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_mgtiltocf_jerk_v114_signal(revenue, ncfo):
    score = 0.5 * _r40_growth(revenue, 252) + 1.5 * _r40_ocf_margin(ncfo, revenue)
    b = _slope(score, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the dual fcf x gross margin quality over a half-year
def f23r40_f23_rule_of_40_dualfg_slow_jerk_v115_signal(revenue, fcf, grossmargin):
    dual = _r40_fcf_margin(fcf, revenue) * grossmargin
    b = _slope(dual, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked convertible cash-weighted fcf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_convwt_jerk_v116_signal(revenue, fcf, ncfo):
    score = _r40_score_fcf(revenue, fcf, 252)
    conv = (fcf / ncfo.replace(0, np.nan)).clip(-1, 2)
    b = _slope(_rank(score * (0.5 + 0.5 * conv), 504), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the off-peak distance of the fcf Rule-of-40 over a month
def f23r40_f23_rule_of_40_offpeak_jerk_v117_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    offpeak = score - score.rolling(252, min_periods=126).max()
    b = _slope(offpeak, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the recovery from trough of the ebitda Rule-of-40 over a month
def f23r40_f23_rule_of_40_offtrough_jerk_v118_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    offtrough = score - score.rolling(252, min_periods=126).min()
    b = _slope(offtrough, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the score-position-in-range of the fcf Rule-of-40 over a month
def f23r40_f23_rule_of_40_r40fcfpos_jerk_v119_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    lo = score.rolling(252, min_periods=126).min()
    hi = score.rolling(252, min_periods=126).max()
    pos = (score - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(pos, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the score-position-in-range of the ocf Rule-of-40 over a month
def f23r40_f23_rule_of_40_r40ocfpos_jerk_v120_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    lo = score.rolling(252, min_periods=126).min()
    hi = score.rolling(252, min_periods=126).max()
    pos = (score - lo) / (hi - lo).replace(0, np.nan)
    b = _slope(pos, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-minus-ocf-margin balance over a month
def f23r40_f23_rule_of_40_balocf_fast_jerk_v121_signal(revenue, ncfo):
    bal = _r40_balance(_r40_growth(revenue, 252), _r40_ocf_margin(ncfo, revenue))
    b = _slope(bal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf retention ratio (fcf as a fraction of ocf) over a half-year
def f23r40_f23_rule_of_40_cashconv_slow_jerk_v122_signal(fcf, ncfo):
    ratio = (fcf.abs() / (ncfo.abs() + fcf.abs())).clip(0, 1)
    b = _slope(ratio, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-minus-grossmargin balance over a month
def f23r40_f23_rule_of_40_balgrs_fast_jerk_v123_signal(revenue, grossmargin):
    bal = _r40_balance(_r40_growth(revenue, 252), grossmargin)
    b = _slope(bal, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-margin share over a half-year (slow profitability-contribution trend)
def f23r40_f23_rule_of_40_fcfshare_slow_jerk_v124_signal(revenue, fcf):
    share = _r40_share(_r40_growth(revenue, 252), _r40_fcf_margin(fcf, revenue))
    b = _slope(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ebitda-margin share over a half-year
def f23r40_f23_rule_of_40_ebdshare_slow_jerk_v125_signal(revenue, ebitdamargin):
    share = _r40_share(_r40_growth(revenue, 252), ebitdamargin)
    b = _slope(share, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the sharpe-of-quality (fcf mean/std) over a quarter
def f23r40_f23_rule_of_40_sharpefcf_jerk_v126_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    sharpe = _mean(score, 252) / _std(score, 252).replace(0, np.nan)
    b = _slope(sharpe, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the sharpe-of-quality (ocf mean/std) over a quarter
def f23r40_f23_rule_of_40_sharpeocf_jerk_v127_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    sharpe = _mean(score, 252) / _std(score, 252).replace(0, np.nan)
    b = _slope(sharpe, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf-margin x growth (gross-weighted) over a quarter
def f23r40_f23_rule_of_40_qfcfgrs_jerk_v128_signal(revenue, fcf, grossmargin):
    q = _r40_growth(revenue, 252) * _r40_fcf_margin(fcf, revenue) * (0.5 + grossmargin)
    b = _slope(q, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf-margin x growth (gross-weighted) over a half-year
def f23r40_f23_rule_of_40_qocfgrs_jerk_v129_signal(revenue, ncfo, grossmargin):
    q = _r40_ocf_margin(ncfo, revenue) * grossmargin + 0.3 * _r40_growth(revenue, 252)
    b = _slope(_rank(q, 504), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the log-growth + ocf-margin composite, ranked, over a quarter
def f23r40_f23_rule_of_40_logocf_rank_jerk_v130_signal(revenue, ncfo):
    score = _r40_loggrowth(revenue, 252) + _r40_ocf_margin(ncfo, revenue)
    b = _slope(_rank(score, 504), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-curvature + fcf-margin composite over a quarter
def f23r40_f23_rule_of_40_growcurvfcf_jerk_v131_signal(revenue, fcf):
    curv = _r40_growth(revenue, 63) - _r40_growth(revenue, 252)
    b = _slope(curv + _r40_fcf_margin(fcf, revenue), 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-curvature + ebitda-margin composite over a quarter
def f23r40_f23_rule_of_40_growcurvebd_jerk_v132_signal(revenue, ebitdamargin):
    curv = _r40_growth(revenue, 63) - _r40_growth(revenue, 252)
    b = _slope(curv + ebitdamargin, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf Rule-of-40 minus its two-year mean over a quarter
def f23r40_f23_rule_of_40_reldevocf_jerk_v133_signal(revenue, ncfo):
    score = _r40_score_ocf(revenue, ncfo, 252)
    dev = score - _mean(score, 504)
    b = _slope(dev, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the fcf Rule-of-40 minus its two-year mean over a quarter
def f23r40_f23_rule_of_40_reldevfcf_jerk_v134_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    dev = score - _mean(score, 504)
    b = _slope(dev, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the growth-per-margin-volatility composite over a quarter
def f23r40_f23_rule_of_40_growpermvol_jerk_v135_signal(revenue, ebitdamargin):
    gpm = _r40_growth(revenue, 252) / (_std(ebitdamargin, 126) + 0.02)
    b = _slope(gpm, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the four-leg margin-trend composite over a month
def f23r40_f23_rule_of_40_mgntrendall_jerk_v136_signal(revenue, fcf, ncfo, ebitdamargin, grossmargin):
    fm = _r40_fcf_margin(fcf, revenue)
    om = _r40_ocf_margin(ncfo, revenue)
    t = ((fm - fm.shift(126)) + (om - om.shift(126))
         + (ebitdamargin - ebitdamargin.shift(126)) + (grossmargin - grossmargin.shift(126))) / 4.0
    b = _slope(t, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the cohesion of margin legs over a half-year
def f23r40_f23_rule_of_40_cohesion_slow_jerk_v137_signal(revenue, fcf, ncfo, ebitdamargin):
    legs = pd.concat([_r40_fcf_margin(fcf, revenue), _r40_ocf_margin(ncfo, revenue), ebitdamargin], axis=1)
    cohesion = legs.mean(axis=1) - (legs.max(axis=1) - legs.min(axis=1))
    b = _slope(cohesion, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the info-ratio of fcf Rule-of-40 quality over a quarter
def f23r40_f23_rule_of_40_inforatiofcf_jerk_v138_signal(revenue, fcf):
    score = _r40_score_fcf(revenue, fcf, 252)
    ir = (score - score.shift(126)) / _std(score, 126).replace(0, np.nan)
    b = _slope(ir, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the info-ratio of ebitda Rule-of-40 quality over a quarter
def f23r40_f23_rule_of_40_inforatioebd_jerk_v139_signal(revenue, ebitdamargin):
    score = _r40_score_ebitda(revenue, ebitdamargin, 252)
    ir = (score - score.shift(126)) / _std(score, 126).replace(0, np.nan)
    b = _slope(ir, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the ocf Rule-of-40 (two-year growth) over a half-year, vol-normalized
def f23r40_f23_rule_of_40_r40ocf2y_jerk_v140_signal(revenue, ncfo):
    base = _r40_score_ocf(revenue, ncfo, 504)
    b = _slope_norm(base, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the gross Rule-of-40 (two-year growth) over a half-year, vol-normalized
def f23r40_f23_rule_of_40_r40grs2y_jerk_v141_signal(revenue, grossmargin):
    base = _r40_score_gross(revenue, grossmargin, 504)
    b = _slope_norm(base, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the dual ebitda x gross margin over a half-year
def f23r40_f23_rule_of_40_dualeg_slow_jerk_v142_signal(ebitdamargin, grossmargin):
    dual = ebitdamargin * grossmargin
    b = _slope(dual, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the standardized-growth minus standardized-grossmargin spread over a month
def f23r40_f23_rule_of_40_zsprgrs_jerk_v143_signal(revenue, grossmargin):
    zspr = _z(_r40_growth(revenue, 252), 252) - _z(grossmargin, 252)
    b = _slope(zspr, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the standardized-growth + standardized-grossmargin sum over a month
def f23r40_f23_rule_of_40_zsumgrs_jerk_v144_signal(revenue, grossmargin):
    zsum = _z(_r40_growth(revenue, 252), 252) + _z(grossmargin, 252)
    b = _slope(zsum, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the rank-space ocf Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_rankblendocf_jerk_v145_signal(revenue, ncfo):
    rb = 0.5 * (_rank(_r40_growth(revenue, 252), 504) + _rank(_r40_ocf_margin(ncfo, revenue), 504))
    b = _slope(rb, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the rank-space gross Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_rankblendgrs_jerk_v146_signal(revenue, grossmargin):
    rb = 0.5 * (_rank(_r40_growth(revenue, 252), 504) + _rank(grossmargin, 504))
    b = _slope(rb, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the blended-cash Rule-of-40 over a half-year, vol-normalized
def f23r40_f23_rule_of_40_blendcash_slow_jerk_v147_signal(revenue, fcf, ncfo):
    g = _r40_growth(revenue, 252)
    m = 0.5 * (_r40_fcf_margin(fcf, revenue) + _r40_ocf_margin(ncfo, revenue))
    b = _slope_norm(g + m, 126, 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the percentile-ranked blended-margin Rule-of-40 over a quarter
def f23r40_f23_rule_of_40_blendmgn_slow_jerk_v148_signal(revenue, ebitdamargin, grossmargin):
    g = _r40_growth(revenue, 252)
    m = 0.5 * (ebitdamargin + grossmargin)
    b = _slope(_rank(g + m, 504), 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the log-growth fcf Rule-of-40 score, ranked, over a quarter
def f23r40_f23_rule_of_40_logfcf_rank_jerk_v149_signal(revenue, fcf):
    score = _r40_loggrowth(revenue, 252) + _r40_fcf_margin(fcf, revenue)
    b = _slope(_rank(score, 504), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# jerk (acceleration of the slope) of the opex-absorption (gross-ebitda) over a half-year
def f23r40_f23_rule_of_40_opexgap_slow_jerk_v150_signal(grossmargin, ebitdamargin):
    gap = grossmargin - ebitdamargin
    b = _slope(gap, 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23r40_f23_rule_of_40_r40fcf_252d_jerk_v001_signal,
    f23r40_f23_rule_of_40_r40ocf_252d_jerk_v002_signal,
    f23r40_f23_rule_of_40_r40ebd_252d_jerk_v003_signal,
    f23r40_f23_rule_of_40_r40grs_252d_jerk_v004_signal,
    f23r40_f23_rule_of_40_fcfmgn_jerk_v005_signal,
    f23r40_f23_rule_of_40_ocfmgn_jerk_v006_signal,
    f23r40_f23_rule_of_40_ebdmgn_jerk_v007_signal,
    f23r40_f23_rule_of_40_grsmgn_jerk_v008_signal,
    f23r40_f23_rule_of_40_grow_jerk_v009_signal,
    f23r40_f23_rule_of_40_balfcf_jerk_v010_signal,
    f23r40_f23_rule_of_40_balocf_jerk_v011_signal,
    f23r40_f23_rule_of_40_balebd_jerk_v012_signal,
    f23r40_f23_rule_of_40_balgrs_jerk_v013_signal,
    f23r40_f23_rule_of_40_fcfshare_jerk_v014_signal,
    f23r40_f23_rule_of_40_ocfshare_jerk_v015_signal,
    f23r40_f23_rule_of_40_ebdshare_jerk_v016_signal,
    f23r40_f23_rule_of_40_grsshare_jerk_v017_signal,
    f23r40_f23_rule_of_40_sprfcfebd_jerk_v018_signal,
    f23r40_f23_rule_of_40_sprocffcf_jerk_v019_signal,
    f23r40_f23_rule_of_40_sprgrsebd_jerk_v020_signal,
    f23r40_f23_rule_of_40_r40fcfz_jerk_v021_signal,
    f23r40_f23_rule_of_40_r40ocfz_jerk_v022_signal,
    f23r40_f23_rule_of_40_r40ebdz_jerk_v023_signal,
    f23r40_f23_rule_of_40_fcfpct_jerk_v024_signal,
    f23r40_f23_rule_of_40_ebdpct_jerk_v025_signal,
    f23r40_f23_rule_of_40_r40fcf_slow_jerk_v026_signal,
    f23r40_f23_rule_of_40_r40ocf_slow_jerk_v027_signal,
    f23r40_f23_rule_of_40_r40ebd_slow_jerk_v028_signal,
    f23r40_f23_rule_of_40_r40grs_slow_jerk_v029_signal,
    f23r40_f23_rule_of_40_fcfmgn_fast_jerk_v030_signal,
    f23r40_f23_rule_of_40_ocfmgn_fast_jerk_v031_signal,
    f23r40_f23_rule_of_40_ebdmgn_fast_jerk_v032_signal,
    f23r40_f23_rule_of_40_grsmgn_fast_jerk_v033_signal,
    f23r40_f23_rule_of_40_fcfmgn_slow_jerk_v034_signal,
    f23r40_f23_rule_of_40_ocfmgn_slow_jerk_v035_signal,
    f23r40_f23_rule_of_40_ebdmgn_slow_jerk_v036_signal,
    f23r40_f23_rule_of_40_grsmgn_slow_jerk_v037_signal,
    f23r40_f23_rule_of_40_fcfmgndev_jerk_v038_signal,
    f23r40_f23_rule_of_40_ocfmgndev_jerk_v039_signal,
    f23r40_f23_rule_of_40_ebdmgndev_jerk_v040_signal,
    f23r40_f23_rule_of_40_grsmgndev_jerk_v041_signal,
    f23r40_f23_rule_of_40_reinv_jerk_v042_signal,
    f23r40_f23_rule_of_40_dualfe_jerk_v043_signal,
    f23r40_f23_rule_of_40_cohesion_jerk_v044_signal,
    f23r40_f23_rule_of_40_mgndisp_jerk_v045_signal,
    f23r40_f23_rule_of_40_mixfcf_jerk_v046_signal,
    f23r40_f23_rule_of_40_mixebd_jerk_v047_signal,
    f23r40_f23_rule_of_40_growcurv_jerk_v048_signal,
    f23r40_f23_rule_of_40_growqual_jerk_v049_signal,
    f23r40_f23_rule_of_40_grsmult_jerk_v050_signal,
    f23r40_f23_rule_of_40_zsumfcf_jerk_v051_signal,
    f23r40_f23_rule_of_40_zsumebd_jerk_v052_signal,
    f23r40_f23_rule_of_40_zsprfcf_jerk_v053_signal,
    f23r40_f23_rule_of_40_zsprocf_jerk_v054_signal,
    f23r40_f23_rule_of_40_zsprebd_jerk_v055_signal,
    f23r40_f23_rule_of_40_cashconv_jerk_v056_signal,
    f23r40_f23_rule_of_40_retain_jerk_v057_signal,
    f23r40_f23_rule_of_40_effburn_jerk_v058_signal,
    f23r40_f23_rule_of_40_signgapfcf_jerk_v059_signal,
    f23r40_f23_rule_of_40_signgapocf_jerk_v060_signal,
    f23r40_f23_rule_of_40_harmfcf_jerk_v061_signal,
    f23r40_f23_rule_of_40_harmocf_jerk_v062_signal,
    f23r40_f23_rule_of_40_growxtrend_jerk_v063_signal,
    f23r40_f23_rule_of_40_growxebdtrend_jerk_v064_signal,
    f23r40_f23_rule_of_40_qfcf_slow_jerk_v065_signal,
    f23r40_f23_rule_of_40_qebd_slow_jerk_v066_signal,
    f23r40_f23_rule_of_40_qgrs_slow_jerk_v067_signal,
    f23r40_f23_rule_of_40_qocf_slow_jerk_v068_signal,
    f23r40_f23_rule_of_40_qualpurefcf_jerk_v069_signal,
    f23r40_f23_rule_of_40_qualpureocf_jerk_v070_signal,
    f23r40_f23_rule_of_40_growacc_jerk_v071_signal,
    f23r40_f23_rule_of_40_r40grsrank_jerk_v072_signal,
    f23r40_f23_rule_of_40_dualgo_jerk_v073_signal,
    f23r40_f23_rule_of_40_dualfg_jerk_v074_signal,
    f23r40_f23_rule_of_40_r40fcfema_jerk_v075_signal,
    f23r40_f23_rule_of_40_r40ebdema_jerk_v076_signal,
    f23r40_f23_rule_of_40_dualeg_jerk_v077_signal,
    f23r40_f23_rule_of_40_consmin_jerk_v078_signal,
    f23r40_f23_rule_of_40_consmax_jerk_v079_signal,
    f23r40_f23_rule_of_40_consrange_jerk_v080_signal,
    f23r40_f23_rule_of_40_loggapfcf_jerk_v081_signal,
    f23r40_f23_rule_of_40_loggapocf_jerk_v082_signal,
    f23r40_f23_rule_of_40_ocfpct_jerk_v083_signal,
    f23r40_f23_rule_of_40_grspct_jerk_v084_signal,
    f23r40_f23_rule_of_40_rankblendfcf_jerk_v085_signal,
    f23r40_f23_rule_of_40_rankblendebd_jerk_v086_signal,
    f23r40_f23_rule_of_40_balfcf_fast_jerk_v087_signal,
    f23r40_f23_rule_of_40_balebd_fast_jerk_v088_signal,
    f23r40_f23_rule_of_40_worstleg_jerk_v089_signal,
    f23r40_f23_rule_of_40_bestleg_jerk_v090_signal,
    f23r40_f23_rule_of_40_legspread_jerk_v091_signal,
    f23r40_f23_rule_of_40_dualfe_slow_jerk_v092_signal,
    f23r40_f23_rule_of_40_reinv_slow_jerk_v093_signal,
    f23r40_f23_rule_of_40_fcfmgnlr_slow_jerk_v094_signal,
    f23r40_f23_rule_of_40_ocfmgnlr_slow_jerk_v095_signal,
    f23r40_f23_rule_of_40_ebdmgnlr_slow_jerk_v096_signal,
    f23r40_f23_rule_of_40_grsmgndev_slow_jerk_v097_signal,
    f23r40_f23_rule_of_40_blendall_jerk_v098_signal,
    f23r40_f23_rule_of_40_effocfburn_jerk_v099_signal,
    f23r40_f23_rule_of_40_signgapebd_jerk_v100_signal,
    f23r40_f23_rule_of_40_grsshare_fast_jerk_v101_signal,
    f23r40_f23_rule_of_40_ocfshare_fast_jerk_v102_signal,
    f23r40_f23_rule_of_40_r40grsz_jerk_v103_signal,
    f23r40_f23_rule_of_40_qocf_jerk_v104_signal,
    f23r40_f23_rule_of_40_zsumocf_jerk_v105_signal,
    f23r40_f23_rule_of_40_durfcf_jerk_v106_signal,
    f23r40_f23_rule_of_40_durocf_jerk_v107_signal,
    f23r40_f23_rule_of_40_volfcf_jerk_v108_signal,
    f23r40_f23_rule_of_40_dualgo_slow_jerk_v109_signal,
    f23r40_f23_rule_of_40_retain_slow_jerk_v110_signal,
    f23r40_f23_rule_of_40_mixocf_jerk_v111_signal,
    f23r40_f23_rule_of_40_grtiltebd_jerk_v112_signal,
    f23r40_f23_rule_of_40_mgtiltfcf_jerk_v113_signal,
    f23r40_f23_rule_of_40_mgtiltocf_jerk_v114_signal,
    f23r40_f23_rule_of_40_dualfg_slow_jerk_v115_signal,
    f23r40_f23_rule_of_40_convwt_jerk_v116_signal,
    f23r40_f23_rule_of_40_offpeak_jerk_v117_signal,
    f23r40_f23_rule_of_40_offtrough_jerk_v118_signal,
    f23r40_f23_rule_of_40_r40fcfpos_jerk_v119_signal,
    f23r40_f23_rule_of_40_r40ocfpos_jerk_v120_signal,
    f23r40_f23_rule_of_40_balocf_fast_jerk_v121_signal,
    f23r40_f23_rule_of_40_cashconv_slow_jerk_v122_signal,
    f23r40_f23_rule_of_40_balgrs_fast_jerk_v123_signal,
    f23r40_f23_rule_of_40_fcfshare_slow_jerk_v124_signal,
    f23r40_f23_rule_of_40_ebdshare_slow_jerk_v125_signal,
    f23r40_f23_rule_of_40_sharpefcf_jerk_v126_signal,
    f23r40_f23_rule_of_40_sharpeocf_jerk_v127_signal,
    f23r40_f23_rule_of_40_qfcfgrs_jerk_v128_signal,
    f23r40_f23_rule_of_40_qocfgrs_jerk_v129_signal,
    f23r40_f23_rule_of_40_logocf_rank_jerk_v130_signal,
    f23r40_f23_rule_of_40_growcurvfcf_jerk_v131_signal,
    f23r40_f23_rule_of_40_growcurvebd_jerk_v132_signal,
    f23r40_f23_rule_of_40_reldevocf_jerk_v133_signal,
    f23r40_f23_rule_of_40_reldevfcf_jerk_v134_signal,
    f23r40_f23_rule_of_40_growpermvol_jerk_v135_signal,
    f23r40_f23_rule_of_40_mgntrendall_jerk_v136_signal,
    f23r40_f23_rule_of_40_cohesion_slow_jerk_v137_signal,
    f23r40_f23_rule_of_40_inforatiofcf_jerk_v138_signal,
    f23r40_f23_rule_of_40_inforatioebd_jerk_v139_signal,
    f23r40_f23_rule_of_40_r40ocf2y_jerk_v140_signal,
    f23r40_f23_rule_of_40_r40grs2y_jerk_v141_signal,
    f23r40_f23_rule_of_40_dualeg_slow_jerk_v142_signal,
    f23r40_f23_rule_of_40_zsprgrs_jerk_v143_signal,
    f23r40_f23_rule_of_40_zsumgrs_jerk_v144_signal,
    f23r40_f23_rule_of_40_rankblendocf_jerk_v145_signal,
    f23r40_f23_rule_of_40_rankblendgrs_jerk_v146_signal,
    f23r40_f23_rule_of_40_blendcash_slow_jerk_v147_signal,
    f23r40_f23_rule_of_40_blendmgn_slow_jerk_v148_signal,
    f23r40_f23_rule_of_40_logfcf_rank_jerk_v149_signal,
    f23r40_f23_rule_of_40_opexgap_slow_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F23_RULE_OF_40_REGISTRY_JERK_001_150 = REGISTRY


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
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    revenue = _fund(101, base=1e8, drift=0.04, vol=0.06).rename("revenue")
    fcf = _fund(102, base=2e7, drift=0.0, vol=0.18, allow_neg=True).rename("fcf")
    ncfo = _fund(103, base=2.5e7, drift=0.01, vol=0.16, allow_neg=True).rename("ncfo")
    ebitdamargin = (_fund(104, base=1.0, drift=0.0, vol=0.12) * 0.18).clip(-0.3, 0.6).rename("ebitdamargin")
    grossmargin = (_fund(105, base=1.0, drift=0.0, vol=0.07) * 0.45).clip(0.1, 0.85).rename("grossmargin")

    cols = {
        "revenue": revenue, "fcf": fcf, "ncfo": ncfo,
        "ebitdamargin": ebitdamargin, "grossmargin": grossmargin,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs not in allowlist: %s" % (name, meta["inputs"])
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

    print("OK f23_rule_of_40_3rd_derivatives_001_150_claude: %d features pass" % n_features)
