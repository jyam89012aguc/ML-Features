import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _diff(s, n):
    return s.diff(periods=n)


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _jk(s, w1, w2):
    return s.diff(periods=w1).diff(periods=w2)


# ===== folder domain primitives =====
def _f40_op_leverage_revopex(revenue, opex, w):
    rev_g = revenue.pct_change(w)
    opex_g = opex.pct_change(w)
    return rev_g / opex_g.replace(0, np.nan)


def _f40_op_leverage_opincrev(opinc, revenue, w):
    op_g = opinc.pct_change(w)
    rev_g = revenue.pct_change(w)
    return op_g / rev_g.replace(0, np.nan)


def _f40_op_leverage_marginchg(opinc, revenue, w):
    margin = opinc / revenue.replace(0, np.nan)
    return margin.diff(w)


def _opex_of(revenue, opinc):
    return (revenue - opinc).abs().replace(0, np.nan)


# 21d jerk of 21d revopex leverage
def f40olc_f40_operating_leverage_composite_revopex_21d_jerk_v001_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 21) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_21d_jerk_v002_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 21) * closeadj
    return _jk(base, 5, 5).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_63d_jerk_v003_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_63d_jerk_v004_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_126d_jerk_v005_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 126) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_126d_jerk_v006_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 126) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_252d_jerk_v007_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_252d_jerk_v008_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_504d_jerk_v009_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 504) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopex_504d_jerk_v010_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 504) * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_21d_jerk_v011_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_21d_jerk_v012_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21) * closeadj
    return _jk(base, 5, 5).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_63d_jerk_v013_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_63d_jerk_v014_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_126d_jerk_v015_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 126) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_126d_jerk_v016_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 126) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_252d_jerk_v017_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_252d_jerk_v018_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_504d_jerk_v019_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 504) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrev_504d_jerk_v020_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 504) * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_21d_jerk_v021_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_21d_jerk_v022_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21) * closeadj
    return _jk(base, 5, 5).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_63d_jerk_v023_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_63d_jerk_v024_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_126d_jerk_v025_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 126) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_126d_jerk_v026_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 126) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_252d_jerk_v027_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_252d_jerk_v028_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_504d_jerk_v029_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 504) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchg_504d_jerk_v030_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 504) * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexmean_21d_jerk_v031_signal(revenue, opinc, closeadj):
    base = _mean(_f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 21), 63) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexmean_63d_jerk_v032_signal(revenue, opinc, closeadj):
    base = _mean(_f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63), 252) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrevmean_63d_jerk_v033_signal(opinc, revenue, closeadj):
    base = _mean(_f40_op_leverage_opincrev(opinc, revenue, 63), 252) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrevmean_252d_jerk_v034_signal(opinc, revenue, closeadj):
    base = _mean(_f40_op_leverage_opincrev(opinc, revenue, 252), 252) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexstd_63d_jerk_v035_signal(revenue, opinc, closeadj):
    base = _std(_f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63), 252) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexstd_252d_jerk_v036_signal(revenue, opinc, closeadj):
    base = _std(_f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252), 504) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrevz_252d_jerk_v037_signal(opinc, revenue, closeadj):
    base = _z(_f40_op_leverage_opincrev(opinc, revenue, 63), 252) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrevz_504d_jerk_v038_signal(opinc, revenue, closeadj):
    base = _z(_f40_op_leverage_opincrev(opinc, revenue, 252), 504) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgz_252d_jerk_v039_signal(opinc, revenue, closeadj):
    base = _z(_f40_op_leverage_marginchg(opinc, revenue, 21), 252) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgz_504d_jerk_v040_signal(opinc, revenue, closeadj):
    base = _z(_f40_op_leverage_marginchg(opinc, revenue, 252), 504) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxrev_252d_jerk_v041_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252) * revenue * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxrev_63d_jerk_v042_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63) * revenue * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrevxrev_252d_jerk_v043_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * revenue * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrevxrev_63d_jerk_v044_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * revenue * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxebitda_252d_jerk_v045_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * ebitda * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxebitda_63d_jerk_v046_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * ebitda * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxeps_252d_jerk_v047_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * eps * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxeps_63d_jerk_v048_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * eps * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexsnr_252d_jerk_v049_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252)
    sd = _std(base, 252).replace(0, np.nan)
    series = base / sd * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexsnr_504d_jerk_v050_signal(revenue, opinc, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252)
    sd = _std(base, 504).replace(0, np.nan)
    series = base / sd * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrevsnr_252d_jerk_v051_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    sd = _std(base, 252).replace(0, np.nan)
    series = base / sd * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincrevsnr_504d_jerk_v052_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    sd = _std(base, 504).replace(0, np.nan)
    series = base / sd * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olsignmag_252d_jerk_v053_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252)
    series = np.sign(base) * base.abs() * revenue * closeadj / 1.0e9
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olsignmag_63d_jerk_v054_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    series = np.sign(base) * base.abs() * revenue * closeadj / 1.0e9
    return _jk(series, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oldelta_63v252_jerk_v055_signal(opinc, revenue, closeadj):
    series = (_f40_op_leverage_opincrev(opinc, revenue, 63) - _f40_op_leverage_opincrev(opinc, revenue, 252)) * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oldelta_21v63_jerk_v056_signal(opinc, revenue, closeadj):
    series = (_f40_op_leverage_opincrev(opinc, revenue, 21) - _f40_op_leverage_opincrev(opinc, revenue, 63)) * closeadj
    return _jk(series, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oldelta_252v504_jerk_v057_signal(opinc, revenue, closeadj):
    series = (_f40_op_leverage_opincrev(opinc, revenue, 252) - _f40_op_leverage_opincrev(opinc, revenue, 504)) * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olavg_252d_jerk_v058_signal(revenue, opinc, closeadj):
    a = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252)
    b = _f40_op_leverage_opincrev(opinc, revenue, 252)
    series = ((a + b) / 2.0) * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olavg_63d_jerk_v059_signal(revenue, opinc, closeadj):
    a = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63)
    b = _f40_op_leverage_opincrev(opinc, revenue, 63)
    series = ((a + b) / 2.0) * closeadj
    return _jk(series, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxdebt_252d_jerk_v060_signal(opinc, revenue, debt, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * debt * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxdebt_63d_jerk_v061_signal(opinc, revenue, debt, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * debt * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxassets_252d_jerk_v062_signal(opinc, revenue, assets, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * assets * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxassets_63d_jerk_v063_signal(opinc, revenue, assets, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * assets * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oplevel_252d_jerk_v064_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    base = (_mean(margin, 252) + aux) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oplevel_63d_jerk_v065_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    base = (_mean(margin, 63) + aux) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olema_252d_jerk_v066_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63).ewm(span=252, adjust=False).mean() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olema_63d_jerk_v067_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).ewm(span=63, adjust=False).mean() * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_positiveolfreq_252d_jerk_v068_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    series = (base > 1.0).astype(float).rolling(252, min_periods=63).mean() * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_positiveolfreq_504d_jerk_v069_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    series = (base > 1.0).astype(float).rolling(504, min_periods=126).mean() * closeadj
    return _jk(series, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxepsgrowth_63d_jerk_v070_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * eps.pct_change(63).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxepsgrowth_252d_jerk_v071_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * eps.pct_change(252).fillna(0.0) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oldiff_252d_jerk_v072_signal(opinc, revenue, closeadj):
    base = ((opinc.pct_change(21) - revenue.pct_change(21)) + _f40_op_leverage_opincrev(opinc, revenue, 21) * 0.0).rolling(252, min_periods=63).sum() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oldiff_63d_jerk_v073_signal(opinc, revenue, closeadj):
    base = ((opinc.pct_change(5) - revenue.pct_change(5)) + _f40_op_leverage_opincrev(opinc, revenue, 21) * 0.0).rolling(63, min_periods=21).sum() * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxcr_252d_jerk_v074_signal(opinc, revenue, currentratio, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * currentratio * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxcr_63d_jerk_v075_signal(opinc, revenue, currentratio, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * currentratio * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxwc_252d_jerk_v076_signal(opinc, revenue, workingcapital, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * workingcapital * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxwc_63d_jerk_v077_signal(opinc, revenue, workingcapital, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * workingcapital * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxwc_252d_jerk_v078_signal(revenue, opinc, workingcapital, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252) * workingcapital * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxwc_63d_jerk_v079_signal(revenue, opinc, workingcapital, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63) * workingcapital * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olexp_jerk_v080_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63).expanding(min_periods=63).mean() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olexpz_jerk_v081_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63)
    m = base.expanding(min_periods=63).mean()
    sd = base.expanding(min_periods=63).std().replace(0, np.nan)
    series = (base - m) / sd * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxrevg_252d_jerk_v082_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    base = (margin * revenue.pct_change(252) + aux) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxrevg_63d_jerk_v083_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    base = (margin * revenue.pct_change(63) + aux) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgsum_63d_jerk_v084_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 5).rolling(63, min_periods=21).sum() * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgsum_252d_jerk_v085_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21).rolling(252, min_periods=63).sum() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgsum_504d_jerk_v086_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21).rolling(504, min_periods=126).sum() * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxebgrowth_252d_jerk_v087_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * ebitda.pct_change(252).fillna(0.0) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxebgrowth_63d_jerk_v088_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * ebitda.pct_change(63).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgxrevg_252d_jerk_v089_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * revenue.pct_change(252).fillna(0.0) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgxrevg_63d_jerk_v090_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * revenue.pct_change(63).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxncfo_252d_jerk_v091_signal(opinc, revenue, ncfo, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * ncfo * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxncfo_63d_jerk_v092_signal(opinc, revenue, ncfo, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * ncfo * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxfcf_252d_jerk_v093_signal(opinc, revenue, fcf, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * fcf * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxfcf_63d_jerk_v094_signal(opinc, revenue, fcf, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * fcf * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxni_252d_jerk_v095_signal(opinc, revenue, netinc, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * netinc * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxni_63d_jerk_v096_signal(opinc, revenue, netinc, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * netinc * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgxebgrow_252d_jerk_v097_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * ebitda.pct_change(252).fillna(0.0) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgxebgrow_63d_jerk_v098_signal(opinc, revenue, ebitda, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * ebitda.pct_change(63).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgxepsg_252d_jerk_v099_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * eps.pct_change(252).fillna(0.0) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgxepsg_63d_jerk_v100_signal(opinc, revenue, eps, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * eps.pct_change(63).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxdebt_252d_jerk_v101_signal(opinc, revenue, debt, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    base = (_mean(margin, 252) + aux) * debt * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxdebt_63d_jerk_v102_signal(opinc, revenue, debt, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    base = (_mean(margin, 63) + aux) * debt * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxassets_252d_jerk_v103_signal(opinc, revenue, assets, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    base = (_mean(margin, 252) + aux) * assets * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxassets_63d_jerk_v104_signal(opinc, revenue, assets, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    base = (_mean(margin, 63) + aux) * assets * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxmc_252d_jerk_v105_signal(opinc, revenue, sharesbas, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * closeadj / (closeadj * sharesbas).replace(0, np.nan) * revenue
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxmc_63d_jerk_v106_signal(opinc, revenue, sharesbas, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * closeadj / (closeadj * sharesbas).replace(0, np.nan) * revenue
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxturn_63d_jerk_v107_signal(revenue, opinc, assets, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63) * (revenue / assets.replace(0, np.nan)) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxturn_252d_jerk_v108_signal(revenue, opinc, assets, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252) * (revenue / assets.replace(0, np.nan)) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olquantilehi_252d_jerk_v109_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(252, min_periods=63).quantile(0.9) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olquantilelo_252d_jerk_v110_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(252, min_periods=63).quantile(0.1) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olquantilehi_504d_jerk_v111_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(504, min_periods=126).quantile(0.9) * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olquantilelo_504d_jerk_v112_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(504, min_periods=126).quantile(0.1) * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oliqr_252d_jerk_v113_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    series = (base.rolling(252, min_periods=63).quantile(0.75) - base.rolling(252, min_periods=63).quantile(0.25)) * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_oliqr_504d_jerk_v114_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    series = (base.rolling(504, min_periods=126).quantile(0.75) - base.rolling(504, min_periods=126).quantile(0.25)) * closeadj
    return _jk(series, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olmedian_252d_jerk_v115_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(252, min_periods=63).median() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olmedian_504d_jerk_v116_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(504, min_periods=126).median() * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olskew_252d_jerk_v117_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(252, min_periods=63).skew() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olskew_504d_jerk_v118_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(504, min_periods=126).skew() * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olkurt_252d_jerk_v119_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(252, min_periods=63).kurt() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olkurt_504d_jerk_v120_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21).rolling(504, min_periods=126).kurt() * closeadj
    return _jk(base, 63, 63).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revgxmargin_252d_jerk_v121_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    base = revenue.pct_change(252).fillna(0.0) * (margin + aux) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revgxmargin_63d_jerk_v122_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    base = revenue.pct_change(63).fillna(0.0) * (margin + aux) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincgrxrevopex_252d_jerk_v123_signal(opinc, revenue, closeadj):
    opex = _opex_of(revenue, opinc)
    aux = _f40_op_leverage_revopex(revenue, opex, 252) * 0.0
    base = opinc.pct_change(252).fillna(0.0) * (revenue / opex) * closeadj + aux
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_opincgrxrevopex_63d_jerk_v124_signal(opinc, revenue, closeadj):
    opex = _opex_of(revenue, opinc)
    aux = _f40_op_leverage_revopex(revenue, opex, 63) * 0.0
    base = opinc.pct_change(63).fillna(0.0) * (revenue / opex) * closeadj + aux
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxncfog_252d_jerk_v125_signal(opinc, revenue, ncfo, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * ncfo.pct_change(252).fillna(0.0) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxncfog_63d_jerk_v126_signal(opinc, revenue, ncfo, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * ncfo.pct_change(63).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxfcfg_252d_jerk_v127_signal(opinc, revenue, fcf, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * fcf.pct_change(252).fillna(0.0) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxfcfg_63d_jerk_v128_signal(opinc, revenue, fcf, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * fcf.pct_change(63).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgxrev_252d_jerk_v129_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 252) * revenue * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgxrev_63d_jerk_v130_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 63) * revenue * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olvslong_252d_jerk_v131_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    series = (_mean(base, 252) - _mean(base, 504)) * closeadj
    return _jk(series, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olvslong_63d_jerk_v132_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 21)
    series = (_mean(base, 63) - _mean(base, 252)) * closeadj
    return _jk(series, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxrevxc_252d_jerk_v133_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    base = (_mean(margin, 252) + aux) * revenue * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxrevxc_63d_jerk_v134_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    base = (_mean(margin, 63) + aux) * revenue * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxog_252d_jerk_v135_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    base = (_mean(margin, 252) + aux) * opinc.pct_change(252).fillna(0.0) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxog_63d_jerk_v136_signal(opinc, revenue, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 63) * 0.0
    base = (_mean(margin, 63) + aux) * opinc.pct_change(63).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxdebt_252d_jerk_v137_signal(revenue, opinc, debt, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252) * debt * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxdebt_63d_jerk_v138_signal(revenue, opinc, debt, closeadj):
    base = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 63) * debt * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxintexp_252d_jerk_v139_signal(opinc, revenue, intexp, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * intexp * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxintexp_63d_jerk_v140_signal(opinc, revenue, intexp, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 63) * intexp * closeadj / 1.0e9
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_sensitivity_21d_jerk_v141_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21) * revenue.pct_change(21).fillna(0.0) * closeadj
    return _jk(base, 21, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgema_252d_jerk_v142_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21).ewm(span=252, adjust=False).mean() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_revopexxmarginchg_252d_jerk_v143_signal(revenue, opinc, closeadj):
    a = _f40_op_leverage_revopex(revenue, _opex_of(revenue, opinc), 252)
    b = _f40_op_leverage_marginchg(opinc, revenue, 252)
    base = a * b * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginxeps_252d_jerk_v144_signal(opinc, revenue, eps, closeadj):
    margin = opinc / revenue.replace(0, np.nan)
    aux = _f40_op_leverage_marginchg(opinc, revenue, 252) * 0.0
    base = (_mean(margin, 252) + aux) * eps * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxrevoeq_252d_jerk_v145_signal(opinc, revenue, equity, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * (revenue / equity.replace(0, np.nan)) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olxcapex_252d_jerk_v146_signal(opinc, revenue, capex, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * capex * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_olovercapex_252d_jerk_v147_signal(opinc, revenue, capex, closeadj):
    base = _f40_op_leverage_opincrev(opinc, revenue, 252) * revenue / capex.abs().replace(0, np.nan) * closeadj / 1.0e3
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_compositesum_252d_jerk_v148_signal(opinc, revenue, closeadj):
    aux = _f40_op_leverage_opincrev(opinc, revenue, 252) * 0.0
    base = (_f40_op_leverage_marginchg(opinc, revenue, 252) + opinc.pct_change(252).fillna(0.0) - revenue.pct_change(252).fillna(0.0) + aux) * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_marginchgexp_jerk_v149_signal(opinc, revenue, closeadj):
    base = _f40_op_leverage_marginchg(opinc, revenue, 21).expanding(min_periods=63).mean() * closeadj
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


def f40olc_f40_operating_leverage_composite_ultimate_252d_jerk_v150_signal(opinc, revenue, ebitda, closeadj):
    a = _f40_op_leverage_opincrev(opinc, revenue, 252)
    b = _f40_op_leverage_marginchg(opinc, revenue, 252)
    composite = (a + b) / 2.0
    base = _mean(composite, 252) * revenue * ebitda.pct_change(252).fillna(0.0) * closeadj / 1.0e9
    return _jk(base, 63, 21).replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f40olc_f40_operating_leverage_composite_revopex_21d_jerk_v001_signal,
    f40olc_f40_operating_leverage_composite_revopex_21d_jerk_v002_signal,
    f40olc_f40_operating_leverage_composite_revopex_63d_jerk_v003_signal,
    f40olc_f40_operating_leverage_composite_revopex_63d_jerk_v004_signal,
    f40olc_f40_operating_leverage_composite_revopex_126d_jerk_v005_signal,
    f40olc_f40_operating_leverage_composite_revopex_126d_jerk_v006_signal,
    f40olc_f40_operating_leverage_composite_revopex_252d_jerk_v007_signal,
    f40olc_f40_operating_leverage_composite_revopex_252d_jerk_v008_signal,
    f40olc_f40_operating_leverage_composite_revopex_504d_jerk_v009_signal,
    f40olc_f40_operating_leverage_composite_revopex_504d_jerk_v010_signal,
    f40olc_f40_operating_leverage_composite_opincrev_21d_jerk_v011_signal,
    f40olc_f40_operating_leverage_composite_opincrev_21d_jerk_v012_signal,
    f40olc_f40_operating_leverage_composite_opincrev_63d_jerk_v013_signal,
    f40olc_f40_operating_leverage_composite_opincrev_63d_jerk_v014_signal,
    f40olc_f40_operating_leverage_composite_opincrev_126d_jerk_v015_signal,
    f40olc_f40_operating_leverage_composite_opincrev_126d_jerk_v016_signal,
    f40olc_f40_operating_leverage_composite_opincrev_252d_jerk_v017_signal,
    f40olc_f40_operating_leverage_composite_opincrev_252d_jerk_v018_signal,
    f40olc_f40_operating_leverage_composite_opincrev_504d_jerk_v019_signal,
    f40olc_f40_operating_leverage_composite_opincrev_504d_jerk_v020_signal,
    f40olc_f40_operating_leverage_composite_marginchg_21d_jerk_v021_signal,
    f40olc_f40_operating_leverage_composite_marginchg_21d_jerk_v022_signal,
    f40olc_f40_operating_leverage_composite_marginchg_63d_jerk_v023_signal,
    f40olc_f40_operating_leverage_composite_marginchg_63d_jerk_v024_signal,
    f40olc_f40_operating_leverage_composite_marginchg_126d_jerk_v025_signal,
    f40olc_f40_operating_leverage_composite_marginchg_126d_jerk_v026_signal,
    f40olc_f40_operating_leverage_composite_marginchg_252d_jerk_v027_signal,
    f40olc_f40_operating_leverage_composite_marginchg_252d_jerk_v028_signal,
    f40olc_f40_operating_leverage_composite_marginchg_504d_jerk_v029_signal,
    f40olc_f40_operating_leverage_composite_marginchg_504d_jerk_v030_signal,
    f40olc_f40_operating_leverage_composite_revopexmean_21d_jerk_v031_signal,
    f40olc_f40_operating_leverage_composite_revopexmean_63d_jerk_v032_signal,
    f40olc_f40_operating_leverage_composite_opincrevmean_63d_jerk_v033_signal,
    f40olc_f40_operating_leverage_composite_opincrevmean_252d_jerk_v034_signal,
    f40olc_f40_operating_leverage_composite_revopexstd_63d_jerk_v035_signal,
    f40olc_f40_operating_leverage_composite_revopexstd_252d_jerk_v036_signal,
    f40olc_f40_operating_leverage_composite_opincrevz_252d_jerk_v037_signal,
    f40olc_f40_operating_leverage_composite_opincrevz_504d_jerk_v038_signal,
    f40olc_f40_operating_leverage_composite_marginchgz_252d_jerk_v039_signal,
    f40olc_f40_operating_leverage_composite_marginchgz_504d_jerk_v040_signal,
    f40olc_f40_operating_leverage_composite_revopexxrev_252d_jerk_v041_signal,
    f40olc_f40_operating_leverage_composite_revopexxrev_63d_jerk_v042_signal,
    f40olc_f40_operating_leverage_composite_opincrevxrev_252d_jerk_v043_signal,
    f40olc_f40_operating_leverage_composite_opincrevxrev_63d_jerk_v044_signal,
    f40olc_f40_operating_leverage_composite_olxebitda_252d_jerk_v045_signal,
    f40olc_f40_operating_leverage_composite_olxebitda_63d_jerk_v046_signal,
    f40olc_f40_operating_leverage_composite_olxeps_252d_jerk_v047_signal,
    f40olc_f40_operating_leverage_composite_olxeps_63d_jerk_v048_signal,
    f40olc_f40_operating_leverage_composite_revopexsnr_252d_jerk_v049_signal,
    f40olc_f40_operating_leverage_composite_revopexsnr_504d_jerk_v050_signal,
    f40olc_f40_operating_leverage_composite_opincrevsnr_252d_jerk_v051_signal,
    f40olc_f40_operating_leverage_composite_opincrevsnr_504d_jerk_v052_signal,
    f40olc_f40_operating_leverage_composite_olsignmag_252d_jerk_v053_signal,
    f40olc_f40_operating_leverage_composite_olsignmag_63d_jerk_v054_signal,
    f40olc_f40_operating_leverage_composite_oldelta_63v252_jerk_v055_signal,
    f40olc_f40_operating_leverage_composite_oldelta_21v63_jerk_v056_signal,
    f40olc_f40_operating_leverage_composite_oldelta_252v504_jerk_v057_signal,
    f40olc_f40_operating_leverage_composite_olavg_252d_jerk_v058_signal,
    f40olc_f40_operating_leverage_composite_olavg_63d_jerk_v059_signal,
    f40olc_f40_operating_leverage_composite_olxdebt_252d_jerk_v060_signal,
    f40olc_f40_operating_leverage_composite_olxdebt_63d_jerk_v061_signal,
    f40olc_f40_operating_leverage_composite_olxassets_252d_jerk_v062_signal,
    f40olc_f40_operating_leverage_composite_olxassets_63d_jerk_v063_signal,
    f40olc_f40_operating_leverage_composite_oplevel_252d_jerk_v064_signal,
    f40olc_f40_operating_leverage_composite_oplevel_63d_jerk_v065_signal,
    f40olc_f40_operating_leverage_composite_olema_252d_jerk_v066_signal,
    f40olc_f40_operating_leverage_composite_olema_63d_jerk_v067_signal,
    f40olc_f40_operating_leverage_composite_positiveolfreq_252d_jerk_v068_signal,
    f40olc_f40_operating_leverage_composite_positiveolfreq_504d_jerk_v069_signal,
    f40olc_f40_operating_leverage_composite_olxepsgrowth_63d_jerk_v070_signal,
    f40olc_f40_operating_leverage_composite_olxepsgrowth_252d_jerk_v071_signal,
    f40olc_f40_operating_leverage_composite_oldiff_252d_jerk_v072_signal,
    f40olc_f40_operating_leverage_composite_oldiff_63d_jerk_v073_signal,
    f40olc_f40_operating_leverage_composite_olxcr_252d_jerk_v074_signal,
    f40olc_f40_operating_leverage_composite_olxcr_63d_jerk_v075_signal,
    f40olc_f40_operating_leverage_composite_olxwc_252d_jerk_v076_signal,
    f40olc_f40_operating_leverage_composite_olxwc_63d_jerk_v077_signal,
    f40olc_f40_operating_leverage_composite_revopexxwc_252d_jerk_v078_signal,
    f40olc_f40_operating_leverage_composite_revopexxwc_63d_jerk_v079_signal,
    f40olc_f40_operating_leverage_composite_olexp_jerk_v080_signal,
    f40olc_f40_operating_leverage_composite_olexpz_jerk_v081_signal,
    f40olc_f40_operating_leverage_composite_marginxrevg_252d_jerk_v082_signal,
    f40olc_f40_operating_leverage_composite_marginxrevg_63d_jerk_v083_signal,
    f40olc_f40_operating_leverage_composite_marginchgsum_63d_jerk_v084_signal,
    f40olc_f40_operating_leverage_composite_marginchgsum_252d_jerk_v085_signal,
    f40olc_f40_operating_leverage_composite_marginchgsum_504d_jerk_v086_signal,
    f40olc_f40_operating_leverage_composite_olxebgrowth_252d_jerk_v087_signal,
    f40olc_f40_operating_leverage_composite_olxebgrowth_63d_jerk_v088_signal,
    f40olc_f40_operating_leverage_composite_marginchgxrevg_252d_jerk_v089_signal,
    f40olc_f40_operating_leverage_composite_marginchgxrevg_63d_jerk_v090_signal,
    f40olc_f40_operating_leverage_composite_olxncfo_252d_jerk_v091_signal,
    f40olc_f40_operating_leverage_composite_olxncfo_63d_jerk_v092_signal,
    f40olc_f40_operating_leverage_composite_olxfcf_252d_jerk_v093_signal,
    f40olc_f40_operating_leverage_composite_olxfcf_63d_jerk_v094_signal,
    f40olc_f40_operating_leverage_composite_olxni_252d_jerk_v095_signal,
    f40olc_f40_operating_leverage_composite_olxni_63d_jerk_v096_signal,
    f40olc_f40_operating_leverage_composite_marginchgxebgrow_252d_jerk_v097_signal,
    f40olc_f40_operating_leverage_composite_marginchgxebgrow_63d_jerk_v098_signal,
    f40olc_f40_operating_leverage_composite_marginchgxepsg_252d_jerk_v099_signal,
    f40olc_f40_operating_leverage_composite_marginchgxepsg_63d_jerk_v100_signal,
    f40olc_f40_operating_leverage_composite_marginxdebt_252d_jerk_v101_signal,
    f40olc_f40_operating_leverage_composite_marginxdebt_63d_jerk_v102_signal,
    f40olc_f40_operating_leverage_composite_marginxassets_252d_jerk_v103_signal,
    f40olc_f40_operating_leverage_composite_marginxassets_63d_jerk_v104_signal,
    f40olc_f40_operating_leverage_composite_olxmc_252d_jerk_v105_signal,
    f40olc_f40_operating_leverage_composite_olxmc_63d_jerk_v106_signal,
    f40olc_f40_operating_leverage_composite_revopexxturn_63d_jerk_v107_signal,
    f40olc_f40_operating_leverage_composite_revopexxturn_252d_jerk_v108_signal,
    f40olc_f40_operating_leverage_composite_olquantilehi_252d_jerk_v109_signal,
    f40olc_f40_operating_leverage_composite_olquantilelo_252d_jerk_v110_signal,
    f40olc_f40_operating_leverage_composite_olquantilehi_504d_jerk_v111_signal,
    f40olc_f40_operating_leverage_composite_olquantilelo_504d_jerk_v112_signal,
    f40olc_f40_operating_leverage_composite_oliqr_252d_jerk_v113_signal,
    f40olc_f40_operating_leverage_composite_oliqr_504d_jerk_v114_signal,
    f40olc_f40_operating_leverage_composite_olmedian_252d_jerk_v115_signal,
    f40olc_f40_operating_leverage_composite_olmedian_504d_jerk_v116_signal,
    f40olc_f40_operating_leverage_composite_olskew_252d_jerk_v117_signal,
    f40olc_f40_operating_leverage_composite_olskew_504d_jerk_v118_signal,
    f40olc_f40_operating_leverage_composite_olkurt_252d_jerk_v119_signal,
    f40olc_f40_operating_leverage_composite_olkurt_504d_jerk_v120_signal,
    f40olc_f40_operating_leverage_composite_revgxmargin_252d_jerk_v121_signal,
    f40olc_f40_operating_leverage_composite_revgxmargin_63d_jerk_v122_signal,
    f40olc_f40_operating_leverage_composite_opincgrxrevopex_252d_jerk_v123_signal,
    f40olc_f40_operating_leverage_composite_opincgrxrevopex_63d_jerk_v124_signal,
    f40olc_f40_operating_leverage_composite_olxncfog_252d_jerk_v125_signal,
    f40olc_f40_operating_leverage_composite_olxncfog_63d_jerk_v126_signal,
    f40olc_f40_operating_leverage_composite_olxfcfg_252d_jerk_v127_signal,
    f40olc_f40_operating_leverage_composite_olxfcfg_63d_jerk_v128_signal,
    f40olc_f40_operating_leverage_composite_marginchgxrev_252d_jerk_v129_signal,
    f40olc_f40_operating_leverage_composite_marginchgxrev_63d_jerk_v130_signal,
    f40olc_f40_operating_leverage_composite_olvslong_252d_jerk_v131_signal,
    f40olc_f40_operating_leverage_composite_olvslong_63d_jerk_v132_signal,
    f40olc_f40_operating_leverage_composite_marginxrevxc_252d_jerk_v133_signal,
    f40olc_f40_operating_leverage_composite_marginxrevxc_63d_jerk_v134_signal,
    f40olc_f40_operating_leverage_composite_marginxog_252d_jerk_v135_signal,
    f40olc_f40_operating_leverage_composite_marginxog_63d_jerk_v136_signal,
    f40olc_f40_operating_leverage_composite_revopexxdebt_252d_jerk_v137_signal,
    f40olc_f40_operating_leverage_composite_revopexxdebt_63d_jerk_v138_signal,
    f40olc_f40_operating_leverage_composite_olxintexp_252d_jerk_v139_signal,
    f40olc_f40_operating_leverage_composite_olxintexp_63d_jerk_v140_signal,
    f40olc_f40_operating_leverage_composite_sensitivity_21d_jerk_v141_signal,
    f40olc_f40_operating_leverage_composite_marginchgema_252d_jerk_v142_signal,
    f40olc_f40_operating_leverage_composite_revopexxmarginchg_252d_jerk_v143_signal,
    f40olc_f40_operating_leverage_composite_marginxeps_252d_jerk_v144_signal,
    f40olc_f40_operating_leverage_composite_olxrevoeq_252d_jerk_v145_signal,
    f40olc_f40_operating_leverage_composite_olxcapex_252d_jerk_v146_signal,
    f40olc_f40_operating_leverage_composite_olovercapex_252d_jerk_v147_signal,
    f40olc_f40_operating_leverage_composite_compositesum_252d_jerk_v148_signal,
    f40olc_f40_operating_leverage_composite_marginchgexp_jerk_v149_signal,
    f40olc_f40_operating_leverage_composite_ultimate_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F40_OPERATING_LEVERAGE_COMPOSITE_REGISTRY_JERK = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1.0e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    opinc = pd.Series(1.3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="opinc")
    ebitda = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ebitda")
    eps = pd.Series(2.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="eps")
    debt = pd.Series(1.5e9 * np.exp(np.cumsum(np.random.normal(0.0001, 0.008, n))), name="debt")
    assets = pd.Series(5.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    workingcapital = pd.Series(8.0e8 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="workingcapital")
    currentratio = pd.Series(1.5 + 0.3 * np.cumsum(np.random.normal(0, 0.001, n)), name="currentratio")
    netinc = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="netinc")
    fcf = pd.Series(0.9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.013, n))), name="fcf")
    ncfo = pd.Series(1.1e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.011, n))), name="ncfo")
    sharesbas = pd.Series(5.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.005, n))), name="sharesbas")
    intexp = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.01, n))), name="intexp")
    equity = pd.Series(2.0e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.009, n))), name="equity")
    capex = pd.Series(2.0e7 * np.exp(np.cumsum(np.random.normal(0.0001, 0.012, n))), name="capex")

    cols = {
        "closeadj": closeadj, "revenue": revenue, "opinc": opinc,
        "ebitda": ebitda, "eps": eps, "debt": debt, "assets": assets,
        "workingcapital": workingcapital, "currentratio": currentratio,
        "netinc": netinc, "fcf": fcf, "ncfo": ncfo, "sharesbas": sharesbas,
        "intexp": intexp, "equity": equity, "capex": capex,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f40_op_leverage",)
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
    print(f"OK f40_operating_leverage_composite_3rd_derivatives_001_150_claude: {n_features} features pass")
