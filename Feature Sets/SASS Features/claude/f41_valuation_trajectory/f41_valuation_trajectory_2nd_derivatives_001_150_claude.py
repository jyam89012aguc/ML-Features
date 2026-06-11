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


def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True) - 0.5


def _logmult(m):
    return np.log(m.replace(0, np.nan).clip(lower=1e-9))


def _rerate(m, w):
    lm = _logmult(m)
    return lm - lm.shift(w)


def _revgap(m, w):
    lm = _logmult(m)
    return lm - lm.rolling(w, min_periods=max(2, w // 2)).mean()



def f41vj_f41_valuation_trajectory_rer_pe_63d_slope_v001_signal(pe):
    base = _rerate(pe, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_pe_126d_slope_v002_signal(pe):
    base = _rerate(pe, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_pe_252d_slope_v003_signal(pe):
    base = _rerate(pe, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_pb_63d_slope_v004_signal(pb):
    base = _rerate(pb, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_pb_126d_slope_v005_signal(pb):
    base = _rerate(pb, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_pb_252d_slope_v006_signal(pb):
    base = _rerate(pb, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_ps_63d_slope_v007_signal(ps):
    base = _rerate(ps, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_ps_126d_slope_v008_signal(ps):
    base = _rerate(ps, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_ps_252d_slope_v009_signal(ps):
    base = _rerate(ps, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_evebitda_63d_slope_v010_signal(evebitda):
    base = _rerate(evebitda, 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_evebitda_126d_slope_v011_signal(evebitda):
    base = _rerate(evebitda, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer_evebitda_252d_slope_v012_signal(evebitda):
    base = _rerate(evebitda, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_pe_126d_slope_v013_signal(pe):
    base = _z(pe, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_pe_252d_slope_v014_signal(pe):
    base = _z(pe, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_pe_504d_slope_v015_signal(pe):
    base = _z(pe, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_pb_126d_slope_v016_signal(pb):
    base = _z(pb, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_pb_252d_slope_v017_signal(pb):
    base = _z(pb, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_pb_504d_slope_v018_signal(pb):
    base = _z(pb, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_ps_126d_slope_v019_signal(ps):
    base = _z(ps, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_ps_252d_slope_v020_signal(ps):
    base = _z(ps, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_ps_504d_slope_v021_signal(ps):
    base = _z(ps, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_evebitda_126d_slope_v022_signal(evebitda):
    base = _z(evebitda, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_evebitda_252d_slope_v023_signal(evebitda):
    base = _z(evebitda, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_zhist_evebitda_504d_slope_v024_signal(evebitda):
    base = _z(evebitda, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap_pe_126d_slope_v025_signal(pe):
    base = _revgap(pe, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap_pe_252d_slope_v026_signal(pe):
    base = _revgap(pe, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap_pb_126d_slope_v027_signal(pb):
    base = _revgap(pb, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap_pb_252d_slope_v028_signal(pb):
    base = _revgap(pb, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap_ps_126d_slope_v029_signal(ps):
    base = _revgap(ps, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap_ps_252d_slope_v030_signal(ps):
    base = _revgap(ps, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap_evebitda_126d_slope_v031_signal(evebitda):
    base = _revgap(evebitda, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap_evebitda_252d_slope_v032_signal(evebitda):
    base = _revgap(evebitda, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_band_pe_504d_slope_v033_signal(pe):
    hi = _rmax(pe, 504)
    lo = _rmin(pe, 504)
    base = (pe - lo) / (hi - lo).replace(0, np.nan) - 0.5
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_band_pb_504d_slope_v034_signal(pb):
    hi = _rmax(pb, 504)
    lo = _rmin(pb, 504)
    base = (pb - lo) / (hi - lo).replace(0, np.nan) - 0.5
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_band_ps_504d_slope_v035_signal(ps):
    hi = _rmax(ps, 504)
    lo = _rmin(ps, 504)
    base = (ps - lo) / (hi - lo).replace(0, np.nan) - 0.5
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_band_evebitda_504d_slope_v036_signal(evebitda):
    hi = _rmax(evebitda, 504)
    lo = _rmin(evebitda, 504)
    base = (evebitda - lo) / (hi - lo).replace(0, np.nan) - 0.5
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_ddpain_pe_252d_slope_v037_signal(pe):
    hi = _rmax(pe, 252)
    uw = (pe / hi.replace(0, np.nan) - 1.0)
    base = uw.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_ddpain_pb_252d_slope_v038_signal(pb):
    hi = _rmax(pb, 252)
    uw = (pb / hi.replace(0, np.nan) - 1.0)
    base = uw.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_ddpain_ps_252d_slope_v039_signal(ps):
    hi = _rmax(ps, 252)
    uw = (ps / hi.replace(0, np.nan) - 1.0)
    base = uw.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_ddpain_evebitda_252d_slope_v040_signal(evebitda):
    hi = _rmax(evebitda, 252)
    uw = (evebitda / hi.replace(0, np.nan) - 1.0)
    base = uw.rolling(63, min_periods=21).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rank_pe_504d_slope_v041_signal(pe):
    base = _rank(pe, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rank_pb_504d_slope_v042_signal(pb):
    base = _rank(pb, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rank_ps_504d_slope_v043_signal(ps):
    base = _rank(ps, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rank_evebitda_504d_slope_v044_signal(evebitda):
    base = _rank(evebitda, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rervol_pe_126d_slope_v045_signal(pe):
    base = _std(_logmult(pe).diff(), 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rervol_pe_252d_slope_v046_signal(pe):
    base = _std(_logmult(pe).diff(), 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rervol_pb_126d_slope_v047_signal(pb):
    base = _std(_logmult(pb).diff(), 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rervol_pb_252d_slope_v048_signal(pb):
    base = _std(_logmult(pb).diff(), 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rervol_ps_126d_slope_v049_signal(ps):
    base = _std(_logmult(ps).diff(), 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rervol_ps_252d_slope_v050_signal(ps):
    base = _std(_logmult(ps).diff(), 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rervol_evebitda_126d_slope_v051_signal(evebitda):
    base = _std(_logmult(evebitda).diff(), 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rervol_evebitda_252d_slope_v052_signal(evebitda):
    base = _std(_logmult(evebitda).diff(), 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_emax_pe_63d_slope_v053_signal(pe):
    lm = _logmult(pe)
    base = lm.ewm(span=5, min_periods=3).mean() - lm.ewm(span=42, min_periods=14).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_emax_pb_63d_slope_v054_signal(pb):
    lm = _logmult(pb)
    base = lm.ewm(span=5, min_periods=3).mean() - lm.ewm(span=42, min_periods=14).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_emax_ps_63d_slope_v055_signal(ps):
    lm = _logmult(ps)
    base = lm.ewm(span=5, min_periods=3).mean() - lm.ewm(span=42, min_periods=14).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_emax_evebitda_63d_slope_v056_signal(evebitda):
    lm = _logmult(evebitda)
    base = lm.ewm(span=5, min_periods=3).mean() - lm.ewm(span=42, min_periods=14).mean()
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_signmag_pe_252d_slope_v057_signal(pe):
    r = _rerate(pe, 252)
    base = np.sign(r) * (r.abs() ** 0.5)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_signmag_pb_252d_slope_v058_signal(pb):
    r = _rerate(pb, 252)
    base = np.sign(r) * (r.abs() ** 0.5)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_signmag_ps_252d_slope_v059_signal(ps):
    r = _rerate(ps, 252)
    base = np.sign(r) * (r.abs() ** 0.5)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_signmag_evebitda_252d_slope_v060_signal(evebitda):
    r = _rerate(evebitda, 252)
    base = np.sign(r) * (r.abs() ** 0.5)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_eff_pe_126d_slope_v061_signal(pe):
    lm = _logmult(pe)
    net = (lm - lm.shift(126)).abs()
    path = lm.diff().abs().rolling(126, min_periods=63).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_eff_pb_126d_slope_v062_signal(pb):
    lm = _logmult(pb)
    net = (lm - lm.shift(126)).abs()
    path = lm.diff().abs().rolling(126, min_periods=63).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_eff_ps_126d_slope_v063_signal(ps):
    lm = _logmult(ps)
    net = (lm - lm.shift(126)).abs()
    path = lm.diff().abs().rolling(126, min_periods=63).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_eff_evebitda_126d_slope_v064_signal(evebitda):
    lm = _logmult(evebitda)
    net = (lm - lm.shift(126)).abs()
    path = lm.diff().abs().rolling(126, min_periods=63).sum()
    base = net / path.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_semir_pe_252d_slope_v065_signal(pe):
    chg = _logmult(pe).diff()
    up = chg.clip(lower=0).rolling(252, min_periods=126).std()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).std()
    base = up / dn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_semir_pb_252d_slope_v066_signal(pb):
    chg = _logmult(pb).diff()
    up = chg.clip(lower=0).rolling(252, min_periods=126).std()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).std()
    base = up / dn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_semir_ps_252d_slope_v067_signal(ps):
    chg = _logmult(ps).diff()
    up = chg.clip(lower=0).rolling(252, min_periods=126).std()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).std()
    base = up / dn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_semir_evebitda_252d_slope_v068_signal(evebitda):
    chg = _logmult(evebitda).diff()
    up = chg.clip(lower=0).rolling(252, min_periods=126).std()
    dn = (-chg.clip(upper=0)).rolling(252, min_periods=126).std()
    base = up / dn.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_amp_pe_252d_slope_v069_signal(pe):
    lm = _logmult(pe)
    span = _rmax(lm, 252) - _rmin(lm, 252)
    base = span - span.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_amp_pb_252d_slope_v070_signal(pb):
    lm = _logmult(pb)
    span = _rmax(lm, 252) - _rmin(lm, 252)
    base = span - span.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_amp_ps_252d_slope_v071_signal(ps):
    lm = _logmult(ps)
    span = _rmax(lm, 252) - _rmin(lm, 252)
    base = span - span.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_amp_evebitda_252d_slope_v072_signal(evebitda):
    lm = _logmult(evebitda)
    span = _rmax(lm, 252) - _rmin(lm, 252)
    base = span - span.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_volreg_pe_126d_slope_v073_signal(pe):
    chg = _logmult(pe).diff()
    base = _std(chg, 21) / _std(chg, 126).replace(0, np.nan) - 1.0
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_volreg_pb_126d_slope_v074_signal(pb):
    chg = _logmult(pb).diff()
    base = _std(chg, 21) / _std(chg, 126).replace(0, np.nan) - 1.0
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_volreg_ps_126d_slope_v075_signal(ps):
    chg = _logmult(ps).diff()
    base = _std(chg, 21) / _std(chg, 126).replace(0, np.nan) - 1.0
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_volreg_evebitda_126d_slope_v076_signal(evebitda):
    chg = _logmult(evebitda).diff()
    base = _std(chg, 21) / _std(chg, 126).replace(0, np.nan) - 1.0
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evprem_252d_slope_v077_signal(ev, marketcap):
    base = _logmult(ev) - _logmult(marketcap)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evpremgap_252d_slope_v078_signal(ev, marketcap):
    prem = _logmult(ev) - _logmult(marketcap)
    base = prem - prem.rolling(252, min_periods=126).mean()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evtrend_252d_slope_v079_signal(ev):
    base = _logmult(ev) - _logmult(ev).shift(252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_eqshare_252d_slope_v080_signal(marketcap, ev):
    base = marketcap / ev.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_eqsharez_252d_slope_v081_signal(marketcap, ev):
    share = marketcap / ev.replace(0, np.nan)
    base = _z(share, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_mcaprer_252d_slope_v082_signal(marketcap):
    base = _logmult(marketcap) - _logmult(marketcap).shift(252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evprem_h_126d_slope_v083_signal(ev, marketcap):
    base = _logmult(ev) - _logmult(marketcap)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evtrend_h_126d_slope_v084_signal(ev):
    base = _logmult(ev) - _logmult(ev).shift(126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_peeveb_spr_252d_slope_v085_signal(pe, evebitda):
    base = _rerate(pe, 252) - _rerate(evebitda, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pbps_spr_252d_slope_v086_signal(pb, ps):
    base = _rerate(pb, 252) - _rerate(ps, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pevsps_spr_126d_slope_v087_signal(pe, ps):
    base = _rerate(pe, 126) - _rerate(ps, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_peeveb_gapspr_252d_slope_v088_signal(pe, evebitda):
    base = _revgap(pe, 252) - _revgap(evebitda, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_pseveb_sprh_126d_slope_v089_signal(ps, evebitda):
    base = _rerate(ps, 126) - _rerate(evebitda, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_blendrer63_63d_slope_v090_signal(pe, pb, ps, evebitda):
    base = pd.concat([_rerate(pe, 63), _rerate(pb, 63), _rerate(ps, 63), _rerate(evebitda, 63)], axis=1).mean(axis=1)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_blendrer252_252d_slope_v091_signal(pe, pb, ps, evebitda):
    base = pd.concat([_rerate(pe, 252), _rerate(pb, 252), _rerate(ps, 252), _rerate(evebitda, 252)], axis=1).mean(axis=1)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_blendz252_252d_slope_v092_signal(pe, pb, ps, evebitda):
    base = pd.concat([_z(pe, 252), _z(pb, 252), _z(ps, 252), _z(evebitda, 252)], axis=1).mean(axis=1)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_blenddisp63_63d_slope_v093_signal(pe, pb, ps, evebitda):
    base = pd.concat([_rerate(pe, 63), _rerate(pb, 63), _rerate(ps, 63), _rerate(evebitda, 63)], axis=1).std(axis=1)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_blendgap252_252d_slope_v094_signal(pe, pb, ps, evebitda):
    base = pd.concat([_revgap(pe, 252), _revgap(pb, 252), _revgap(ps, 252), _revgap(evebitda, 252)], axis=1).mean(axis=1)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_trendqual_pe_252d_slope_v095_signal(pe):
    lm = _logmult(pe)
    net = lm - lm.shift(252)
    path = lm.diff().abs().rolling(252, min_periods=126).sum()
    base = net * net / path.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_trendqual_evebitda_252d_slope_v096_signal(evebitda):
    lm = _logmult(evebitda)
    net = lm - lm.shift(252)
    path = lm.diff().abs().rolling(252, min_periods=126).sum()
    base = net * net / path.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_trendqual_ps_126d_slope_v097_signal(ps):
    lm = _logmult(ps)
    net = lm - lm.shift(126)
    path = lm.diff().abs().rolling(126, min_periods=63).sum()
    base = net * net / path.replace(0, np.nan)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_trendqual_pb_252d_slope_v098_signal(pb):
    lm = _logmult(pb)
    net = lm - lm.shift(252)
    path = lm.diff().abs().rolling(252, min_periods=126).sum()
    base = net * net / path.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_skew_pe_252d_slope_v099_signal(pe):
    base = _logmult(pe).diff().rolling(252, min_periods=126).skew()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_skew_ps_252d_slope_v100_signal(ps):
    base = _logmult(ps).diff().rolling(252, min_periods=126).skew()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer504_pe_504d_slope_v101_signal(pe):
    base = _rerate(pe, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer504_evebitda_504d_slope_v102_signal(evebitda):
    base = _rerate(evebitda, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer504_ps_504d_slope_v103_signal(ps):
    base = _rerate(ps, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rer504_pb_504d_slope_v104_signal(pb):
    base = _rerate(pb, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rerkurt_pe_252d_slope_v105_signal(pe):
    base = _logmult(pe).diff().rolling(252, min_periods=126).kurt()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rerkurt_pb_252d_slope_v106_signal(pb):
    base = _logmult(pb).diff().rolling(252, min_periods=126).kurt()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rerkurt_ps_252d_slope_v107_signal(ps):
    base = _logmult(ps).diff().rolling(252, min_periods=126).kurt()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rerkurt_evebitda_252d_slope_v108_signal(evebitda):
    base = _logmult(evebitda).diff().rolling(252, min_periods=126).kurt()
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_lvlrec_pe_252d_slope_v109_signal(pe):
    lo = _rmin(pe, 252)
    base = pe / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_lvlrec_pb_252d_slope_v110_signal(pb):
    lo = _rmin(pb, 252)
    base = pb / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_lvlrec_ps_252d_slope_v111_signal(ps):
    lo = _rmin(ps, 252)
    base = ps / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_lvlrec_evebitda_252d_slope_v112_signal(evebitda):
    lo = _rmin(evebitda, 252)
    base = evebitda / lo.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_hitr_pe_252d_slope_v113_signal(pe):
    up = (_logmult(pe).diff() > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean() - 0.5
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_hitr_pb_252d_slope_v114_signal(pb):
    up = (_logmult(pb).diff() > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean() - 0.5
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_hitr_ps_252d_slope_v115_signal(ps):
    up = (_logmult(ps).diff() > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean() - 0.5
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_hitr_evebitda_252d_slope_v116_signal(evebitda):
    up = (_logmult(evebitda).diff() > 0).astype(float)
    base = up.rolling(252, min_periods=126).mean() - 0.5
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_respr_pe_252d_slope_v117_signal(pe):
    base = _rerate(pe, 63) - _rerate(pe, 252) / 4.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_respr_pb_252d_slope_v118_signal(pb):
    base = _rerate(pb, 63) - _rerate(pb, 252) / 4.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_respr_ps_252d_slope_v119_signal(ps):
    base = _rerate(ps, 63) - _rerate(ps, 252) / 4.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_respr_evebitda_252d_slope_v120_signal(evebitda):
    base = _rerate(evebitda, 63) - _rerate(evebitda, 252) / 4.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_reradj_pe_252d_slope_v121_signal(pe):
    r = _rerate(pe, 252)
    vol = _std(_logmult(pe).diff(), 252) * np.sqrt(252.0)
    base = r / vol.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_reradj_pb_252d_slope_v122_signal(pb):
    r = _rerate(pb, 252)
    vol = _std(_logmult(pb).diff(), 252) * np.sqrt(252.0)
    base = r / vol.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_reradj_ps_252d_slope_v123_signal(ps):
    r = _rerate(ps, 252)
    vol = _std(_logmult(ps).diff(), 252) * np.sqrt(252.0)
    base = r / vol.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_reradj_evebitda_252d_slope_v124_signal(evebitda):
    r = _rerate(evebitda, 252)
    vol = _std(_logmult(evebitda).diff(), 252) * np.sqrt(252.0)
    base = r / vol.replace(0, np.nan)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rerac_pe_252d_slope_v125_signal(pe):
    chg = _logmult(pe).diff()
    base = chg.rolling(252, min_periods=126).corr(chg.shift(1))
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rerac_pb_252d_slope_v126_signal(pb):
    chg = _logmult(pb).diff()
    base = chg.rolling(252, min_periods=126).corr(chg.shift(1))
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rerac_ps_252d_slope_v127_signal(ps):
    chg = _logmult(ps).diff()
    base = chg.rolling(252, min_periods=126).corr(chg.shift(1))
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_rerac_evebitda_252d_slope_v128_signal(evebitda):
    chg = _logmult(evebitda).diff()
    base = chg.rolling(252, min_periods=126).corr(chg.shift(1))
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_band126_pe_126d_slope_v129_signal(pe):
    hi = _rmax(pe, 126)
    lo = _rmin(pe, 126)
    base = (pe - lo) / (hi - lo).replace(0, np.nan) - 0.5
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_band126_evebitda_126d_slope_v130_signal(evebitda):
    hi = _rmax(evebitda, 126)
    lo = _rmin(evebitda, 126)
    base = (evebitda - lo) / (hi - lo).replace(0, np.nan) - 0.5
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap504_pe_504d_slope_v131_signal(pe):
    base = _revgap(pe, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap504_evebitda_504d_slope_v132_signal(evebitda):
    base = _revgap(evebitda, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap504_ps_504d_slope_v133_signal(ps):
    base = _revgap(ps, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_gap504_pb_504d_slope_v134_signal(pb):
    base = _revgap(pb, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_tension_pe_252d_slope_v135_signal(pe):
    base = _rerate(pe, 126) + _revgap(pe, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_tension_evebitda_252d_slope_v136_signal(evebitda):
    base = _rerate(evebitda, 126) + _revgap(evebitda, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_mcapdd_504d_slope_v137_signal(marketcap):
    hi = _rmax(marketcap, 504)
    base = _logmult(marketcap) - _logmult(hi)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evpremrank_504d_slope_v138_signal(ev, marketcap):
    prem = _logmult(ev) - _logmult(marketcap)
    base = _rank(prem, 504)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_varratio_pe_252d_slope_v139_signal(pe):
    lm = _logmult(pe)
    v1 = _std(lm.diff(), 252) ** 2
    v5 = _std(lm.diff(5), 252) ** 2 / 5.0
    base = v5 / v1.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_varratio_pb_252d_slope_v140_signal(pb):
    lm = _logmult(pb)
    v1 = _std(lm.diff(), 252) ** 2
    v5 = _std(lm.diff(5), 252) ** 2 / 5.0
    base = v5 / v1.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_varratio_ps_252d_slope_v141_signal(ps):
    lm = _logmult(ps)
    v1 = _std(lm.diff(), 252) ** 2
    v5 = _std(lm.diff(5), 252) ** 2 / 5.0
    base = v5 / v1.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_varratio_evebitda_252d_slope_v142_signal(evebitda):
    lm = _logmult(evebitda)
    v1 = _std(lm.diff(), 252) ** 2
    v5 = _std(lm.diff(5), 252) ** 2 / 5.0
    base = v5 / v1.replace(0, np.nan) - 1.0
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_impulse_pe_63d_slope_v143_signal(pe):
    base = _z(_logmult(pe).diff(), 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_impulse_pb_63d_slope_v144_signal(pb):
    base = _z(_logmult(pb).diff(), 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_impulse_ps_63d_slope_v145_signal(ps):
    base = _z(_logmult(ps).diff(), 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_impulse_evebitda_63d_slope_v146_signal(evebitda):
    base = _z(_logmult(evebitda).diff(), 63)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evdenomdiv_252d_slope_v147_signal(ev, evebitda):
    base = _rerate(ev, 252) - _rerate(evebitda, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evdenomdiv_h_126d_slope_v148_signal(ev, evebitda):
    base = _rerate(ev, 126) - _rerate(evebitda, 126)
    deriv = base - base.shift(21)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_mcappsdiv_252d_slope_v149_signal(marketcap, ps):
    base = _rerate(marketcap, 252) - _rerate(ps, 252)
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


def f41vj_f41_valuation_trajectory_evpremcurv_252d_slope_v150_signal(ev, marketcap):
    prem = _logmult(ev) - _logmult(marketcap)
    base = (prem - prem.shift(126)) - (prem.shift(126) - prem.shift(252))
    deriv = base - base.shift(63)
    result = deriv
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41vj_f41_valuation_trajectory_rer_pe_63d_slope_v001_signal,
    f41vj_f41_valuation_trajectory_rer_pe_126d_slope_v002_signal,
    f41vj_f41_valuation_trajectory_rer_pe_252d_slope_v003_signal,
    f41vj_f41_valuation_trajectory_rer_pb_63d_slope_v004_signal,
    f41vj_f41_valuation_trajectory_rer_pb_126d_slope_v005_signal,
    f41vj_f41_valuation_trajectory_rer_pb_252d_slope_v006_signal,
    f41vj_f41_valuation_trajectory_rer_ps_63d_slope_v007_signal,
    f41vj_f41_valuation_trajectory_rer_ps_126d_slope_v008_signal,
    f41vj_f41_valuation_trajectory_rer_ps_252d_slope_v009_signal,
    f41vj_f41_valuation_trajectory_rer_evebitda_63d_slope_v010_signal,
    f41vj_f41_valuation_trajectory_rer_evebitda_126d_slope_v011_signal,
    f41vj_f41_valuation_trajectory_rer_evebitda_252d_slope_v012_signal,
    f41vj_f41_valuation_trajectory_zhist_pe_126d_slope_v013_signal,
    f41vj_f41_valuation_trajectory_zhist_pe_252d_slope_v014_signal,
    f41vj_f41_valuation_trajectory_zhist_pe_504d_slope_v015_signal,
    f41vj_f41_valuation_trajectory_zhist_pb_126d_slope_v016_signal,
    f41vj_f41_valuation_trajectory_zhist_pb_252d_slope_v017_signal,
    f41vj_f41_valuation_trajectory_zhist_pb_504d_slope_v018_signal,
    f41vj_f41_valuation_trajectory_zhist_ps_126d_slope_v019_signal,
    f41vj_f41_valuation_trajectory_zhist_ps_252d_slope_v020_signal,
    f41vj_f41_valuation_trajectory_zhist_ps_504d_slope_v021_signal,
    f41vj_f41_valuation_trajectory_zhist_evebitda_126d_slope_v022_signal,
    f41vj_f41_valuation_trajectory_zhist_evebitda_252d_slope_v023_signal,
    f41vj_f41_valuation_trajectory_zhist_evebitda_504d_slope_v024_signal,
    f41vj_f41_valuation_trajectory_gap_pe_126d_slope_v025_signal,
    f41vj_f41_valuation_trajectory_gap_pe_252d_slope_v026_signal,
    f41vj_f41_valuation_trajectory_gap_pb_126d_slope_v027_signal,
    f41vj_f41_valuation_trajectory_gap_pb_252d_slope_v028_signal,
    f41vj_f41_valuation_trajectory_gap_ps_126d_slope_v029_signal,
    f41vj_f41_valuation_trajectory_gap_ps_252d_slope_v030_signal,
    f41vj_f41_valuation_trajectory_gap_evebitda_126d_slope_v031_signal,
    f41vj_f41_valuation_trajectory_gap_evebitda_252d_slope_v032_signal,
    f41vj_f41_valuation_trajectory_band_pe_504d_slope_v033_signal,
    f41vj_f41_valuation_trajectory_band_pb_504d_slope_v034_signal,
    f41vj_f41_valuation_trajectory_band_ps_504d_slope_v035_signal,
    f41vj_f41_valuation_trajectory_band_evebitda_504d_slope_v036_signal,
    f41vj_f41_valuation_trajectory_ddpain_pe_252d_slope_v037_signal,
    f41vj_f41_valuation_trajectory_ddpain_pb_252d_slope_v038_signal,
    f41vj_f41_valuation_trajectory_ddpain_ps_252d_slope_v039_signal,
    f41vj_f41_valuation_trajectory_ddpain_evebitda_252d_slope_v040_signal,
    f41vj_f41_valuation_trajectory_rank_pe_504d_slope_v041_signal,
    f41vj_f41_valuation_trajectory_rank_pb_504d_slope_v042_signal,
    f41vj_f41_valuation_trajectory_rank_ps_504d_slope_v043_signal,
    f41vj_f41_valuation_trajectory_rank_evebitda_504d_slope_v044_signal,
    f41vj_f41_valuation_trajectory_rervol_pe_126d_slope_v045_signal,
    f41vj_f41_valuation_trajectory_rervol_pe_252d_slope_v046_signal,
    f41vj_f41_valuation_trajectory_rervol_pb_126d_slope_v047_signal,
    f41vj_f41_valuation_trajectory_rervol_pb_252d_slope_v048_signal,
    f41vj_f41_valuation_trajectory_rervol_ps_126d_slope_v049_signal,
    f41vj_f41_valuation_trajectory_rervol_ps_252d_slope_v050_signal,
    f41vj_f41_valuation_trajectory_rervol_evebitda_126d_slope_v051_signal,
    f41vj_f41_valuation_trajectory_rervol_evebitda_252d_slope_v052_signal,
    f41vj_f41_valuation_trajectory_emax_pe_63d_slope_v053_signal,
    f41vj_f41_valuation_trajectory_emax_pb_63d_slope_v054_signal,
    f41vj_f41_valuation_trajectory_emax_ps_63d_slope_v055_signal,
    f41vj_f41_valuation_trajectory_emax_evebitda_63d_slope_v056_signal,
    f41vj_f41_valuation_trajectory_signmag_pe_252d_slope_v057_signal,
    f41vj_f41_valuation_trajectory_signmag_pb_252d_slope_v058_signal,
    f41vj_f41_valuation_trajectory_signmag_ps_252d_slope_v059_signal,
    f41vj_f41_valuation_trajectory_signmag_evebitda_252d_slope_v060_signal,
    f41vj_f41_valuation_trajectory_eff_pe_126d_slope_v061_signal,
    f41vj_f41_valuation_trajectory_eff_pb_126d_slope_v062_signal,
    f41vj_f41_valuation_trajectory_eff_ps_126d_slope_v063_signal,
    f41vj_f41_valuation_trajectory_eff_evebitda_126d_slope_v064_signal,
    f41vj_f41_valuation_trajectory_semir_pe_252d_slope_v065_signal,
    f41vj_f41_valuation_trajectory_semir_pb_252d_slope_v066_signal,
    f41vj_f41_valuation_trajectory_semir_ps_252d_slope_v067_signal,
    f41vj_f41_valuation_trajectory_semir_evebitda_252d_slope_v068_signal,
    f41vj_f41_valuation_trajectory_amp_pe_252d_slope_v069_signal,
    f41vj_f41_valuation_trajectory_amp_pb_252d_slope_v070_signal,
    f41vj_f41_valuation_trajectory_amp_ps_252d_slope_v071_signal,
    f41vj_f41_valuation_trajectory_amp_evebitda_252d_slope_v072_signal,
    f41vj_f41_valuation_trajectory_volreg_pe_126d_slope_v073_signal,
    f41vj_f41_valuation_trajectory_volreg_pb_126d_slope_v074_signal,
    f41vj_f41_valuation_trajectory_volreg_ps_126d_slope_v075_signal,
    f41vj_f41_valuation_trajectory_volreg_evebitda_126d_slope_v076_signal,
    f41vj_f41_valuation_trajectory_evprem_252d_slope_v077_signal,
    f41vj_f41_valuation_trajectory_evpremgap_252d_slope_v078_signal,
    f41vj_f41_valuation_trajectory_evtrend_252d_slope_v079_signal,
    f41vj_f41_valuation_trajectory_eqshare_252d_slope_v080_signal,
    f41vj_f41_valuation_trajectory_eqsharez_252d_slope_v081_signal,
    f41vj_f41_valuation_trajectory_mcaprer_252d_slope_v082_signal,
    f41vj_f41_valuation_trajectory_evprem_h_126d_slope_v083_signal,
    f41vj_f41_valuation_trajectory_evtrend_h_126d_slope_v084_signal,
    f41vj_f41_valuation_trajectory_peeveb_spr_252d_slope_v085_signal,
    f41vj_f41_valuation_trajectory_pbps_spr_252d_slope_v086_signal,
    f41vj_f41_valuation_trajectory_pevsps_spr_126d_slope_v087_signal,
    f41vj_f41_valuation_trajectory_peeveb_gapspr_252d_slope_v088_signal,
    f41vj_f41_valuation_trajectory_pseveb_sprh_126d_slope_v089_signal,
    f41vj_f41_valuation_trajectory_blendrer63_63d_slope_v090_signal,
    f41vj_f41_valuation_trajectory_blendrer252_252d_slope_v091_signal,
    f41vj_f41_valuation_trajectory_blendz252_252d_slope_v092_signal,
    f41vj_f41_valuation_trajectory_blenddisp63_63d_slope_v093_signal,
    f41vj_f41_valuation_trajectory_blendgap252_252d_slope_v094_signal,
    f41vj_f41_valuation_trajectory_trendqual_pe_252d_slope_v095_signal,
    f41vj_f41_valuation_trajectory_trendqual_evebitda_252d_slope_v096_signal,
    f41vj_f41_valuation_trajectory_trendqual_ps_126d_slope_v097_signal,
    f41vj_f41_valuation_trajectory_trendqual_pb_252d_slope_v098_signal,
    f41vj_f41_valuation_trajectory_skew_pe_252d_slope_v099_signal,
    f41vj_f41_valuation_trajectory_skew_ps_252d_slope_v100_signal,
    f41vj_f41_valuation_trajectory_rer504_pe_504d_slope_v101_signal,
    f41vj_f41_valuation_trajectory_rer504_evebitda_504d_slope_v102_signal,
    f41vj_f41_valuation_trajectory_rer504_ps_504d_slope_v103_signal,
    f41vj_f41_valuation_trajectory_rer504_pb_504d_slope_v104_signal,
    f41vj_f41_valuation_trajectory_rerkurt_pe_252d_slope_v105_signal,
    f41vj_f41_valuation_trajectory_rerkurt_pb_252d_slope_v106_signal,
    f41vj_f41_valuation_trajectory_rerkurt_ps_252d_slope_v107_signal,
    f41vj_f41_valuation_trajectory_rerkurt_evebitda_252d_slope_v108_signal,
    f41vj_f41_valuation_trajectory_lvlrec_pe_252d_slope_v109_signal,
    f41vj_f41_valuation_trajectory_lvlrec_pb_252d_slope_v110_signal,
    f41vj_f41_valuation_trajectory_lvlrec_ps_252d_slope_v111_signal,
    f41vj_f41_valuation_trajectory_lvlrec_evebitda_252d_slope_v112_signal,
    f41vj_f41_valuation_trajectory_hitr_pe_252d_slope_v113_signal,
    f41vj_f41_valuation_trajectory_hitr_pb_252d_slope_v114_signal,
    f41vj_f41_valuation_trajectory_hitr_ps_252d_slope_v115_signal,
    f41vj_f41_valuation_trajectory_hitr_evebitda_252d_slope_v116_signal,
    f41vj_f41_valuation_trajectory_respr_pe_252d_slope_v117_signal,
    f41vj_f41_valuation_trajectory_respr_pb_252d_slope_v118_signal,
    f41vj_f41_valuation_trajectory_respr_ps_252d_slope_v119_signal,
    f41vj_f41_valuation_trajectory_respr_evebitda_252d_slope_v120_signal,
    f41vj_f41_valuation_trajectory_reradj_pe_252d_slope_v121_signal,
    f41vj_f41_valuation_trajectory_reradj_pb_252d_slope_v122_signal,
    f41vj_f41_valuation_trajectory_reradj_ps_252d_slope_v123_signal,
    f41vj_f41_valuation_trajectory_reradj_evebitda_252d_slope_v124_signal,
    f41vj_f41_valuation_trajectory_rerac_pe_252d_slope_v125_signal,
    f41vj_f41_valuation_trajectory_rerac_pb_252d_slope_v126_signal,
    f41vj_f41_valuation_trajectory_rerac_ps_252d_slope_v127_signal,
    f41vj_f41_valuation_trajectory_rerac_evebitda_252d_slope_v128_signal,
    f41vj_f41_valuation_trajectory_band126_pe_126d_slope_v129_signal,
    f41vj_f41_valuation_trajectory_band126_evebitda_126d_slope_v130_signal,
    f41vj_f41_valuation_trajectory_gap504_pe_504d_slope_v131_signal,
    f41vj_f41_valuation_trajectory_gap504_evebitda_504d_slope_v132_signal,
    f41vj_f41_valuation_trajectory_gap504_ps_504d_slope_v133_signal,
    f41vj_f41_valuation_trajectory_gap504_pb_504d_slope_v134_signal,
    f41vj_f41_valuation_trajectory_tension_pe_252d_slope_v135_signal,
    f41vj_f41_valuation_trajectory_tension_evebitda_252d_slope_v136_signal,
    f41vj_f41_valuation_trajectory_mcapdd_504d_slope_v137_signal,
    f41vj_f41_valuation_trajectory_evpremrank_504d_slope_v138_signal,
    f41vj_f41_valuation_trajectory_varratio_pe_252d_slope_v139_signal,
    f41vj_f41_valuation_trajectory_varratio_pb_252d_slope_v140_signal,
    f41vj_f41_valuation_trajectory_varratio_ps_252d_slope_v141_signal,
    f41vj_f41_valuation_trajectory_varratio_evebitda_252d_slope_v142_signal,
    f41vj_f41_valuation_trajectory_impulse_pe_63d_slope_v143_signal,
    f41vj_f41_valuation_trajectory_impulse_pb_63d_slope_v144_signal,
    f41vj_f41_valuation_trajectory_impulse_ps_63d_slope_v145_signal,
    f41vj_f41_valuation_trajectory_impulse_evebitda_63d_slope_v146_signal,
    f41vj_f41_valuation_trajectory_evdenomdiv_252d_slope_v147_signal,
    f41vj_f41_valuation_trajectory_evdenomdiv_h_126d_slope_v148_signal,
    f41vj_f41_valuation_trajectory_mcappsdiv_252d_slope_v149_signal,
    f41vj_f41_valuation_trajectory_evpremcurv_252d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F41_VALUATION_TRAJECTORY_REGISTRY_001_150 = REGISTRY


def _build_synth():
    np.random.seed(42)
    n = 1500

    def _fund(seed, base=1e8, drift=0.02, vol=0.05, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.3
        return pd.Series(s, name=None)

    # near-zero drift, higher quarterly vol so multiples genuinely re-rate up AND down
    # (oscillating trajectories) -- exercises trend/reversion/shape features distinctly
    pe = _fund(101, base=18.0, drift=0.0, vol=0.14).rename("pe")
    pb = _fund(102, base=2.5, drift=0.0, vol=0.12).rename("pb")
    ps = _fund(103, base=3.0, drift=0.0, vol=0.13).rename("ps")
    evebitda = _fund(104, base=11.0, drift=0.0, vol=0.12).rename("evebitda")
    ev = _fund(105, base=5e9, drift=0.005, vol=0.12).rename("ev")
    marketcap = _fund(106, base=4e9, drift=0.005, vol=0.12).rename("marketcap")
    return {"pe": pe, "pb": pb, "ps": ps, "evebitda": evebitda,
            "ev": ev, "marketcap": marketcap}


if __name__ == "__main__":
    cols = _build_synth()
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

    print("OK f41_valuation_trajectory_2nd_derivatives_001_150_claude: %d features pass" % n_features)