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


def _cover(flow, intexp, w):
    return _mean(flow, w) / _mean(intexp, w).replace(0, np.nan)


def _logcover(flow, intexp, w):
    cov = _mean(flow, w) / _mean(intexp, w).replace(0, np.nan)
    return np.sign(cov) * np.log1p(cov.abs())


def _burden(intexp, base, w):
    return _mean(intexp, w) / _mean(base, w).replace(0, np.nan)


def _effcost(intexp, debt, w):
    return _mean(intexp, w) / _mean(debt, w).replace(0, np.nan)


def _wall(debtc, flow, w):
    return _mean(debtc, w) / _mean(flow, w).replace(0, np.nan)


def _coverz(flow, intexp, w):
    return _z(flow / intexp.replace(0, np.nan), w)


def _dscr(flow, intexp, debtc, w):
    service = intexp + debtc
    r = _mean(flow, w) / _mean(service, w).replace(0, np.nan)
    return np.sign(r) * np.log1p(r.abs())


def _afterint(flow, intexp, w):
    return _mean(flow - intexp, w) / _mean(intexp, w).replace(0, np.nan)


def _covspr(fa, fb, intexp, w):
    return _cover(fa, intexp, w) - _cover(fb, intexp, w)


def _coverrng(flow, intexp, w):
    cov = flow / intexp.replace(0, np.nan)
    return _rmax(cov, w) - _rmin(cov, w)


def _burdspr(intexp, ba, bb, w):
    return _burden(intexp, ba, w) - _burden(intexp, bb, w)


def _rank(s, w):
    return s.rolling(w, min_periods=max(1, w // 4)).rank(pct=True) - 0.5


def _coverrank(flow, intexp, w):
    return _rank(flow / intexp.replace(0, np.nan), w)


def _covertanh(flow, intexp, k):
    return np.tanh(k * (flow / intexp.replace(0, np.nan)))


def _coverdd(flow, intexp, w):
    cov = flow / intexp.replace(0, np.nan)
    return cov / _rmax(cov, w).replace(0, np.nan) - 1.0


def _coverdev2(flow, intexp, w):
    cov = flow / intexp.replace(0, np.nan)
    med = cov.rolling(w, min_periods=max(1, w // 2)).median()
    dev = cov - med
    return np.sign(dev) * (dev ** 2)


def _burdenrank(intexp, base, w):
    return _rank(intexp / base.replace(0, np.nan), w)


def _effcostz(intexp, debt, w):
    return _z(intexp / debt.replace(0, np.nan), w)


def _wallz(debtc, flow, w):
    return _z(debtc / flow.replace(0, np.nan), w)

def f48ic_f48_interest_coverage_ebitcov_126d_slope_v001_signal(ebit, intexp):
    base = _cover(ebit, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcov_252d_slope_v002_signal(ebit, intexp):
    base = _cover(ebit, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcov_504d_slope_v003_signal(ebit, intexp):
    base = _cover(ebit, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacov_126d_slope_v004_signal(ebitda, intexp):
    base = _cover(ebitda, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacov_252d_slope_v005_signal(ebitda, intexp):
    base = _cover(ebitda, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacov_504d_slope_v006_signal(ebitda, intexp):
    base = _cover(ebitda, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocov_126d_slope_v007_signal(ncfo, intexp):
    base = _cover(ncfo, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocov_252d_slope_v008_signal(ncfo, intexp):
    base = _cover(ncfo, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocov_504d_slope_v009_signal(ncfo, intexp):
    base = _cover(ncfo, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcov_126d_slope_v010_signal(fcf, intexp):
    base = _cover(fcf, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcov_252d_slope_v011_signal(fcf, intexp):
    base = _cover(fcf, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcov_504d_slope_v012_signal(fcf, intexp):
    base = _cover(fcf, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovz_126d_slope_v013_signal(ebitda, intexp):
    base = _coverz(ebitda, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovz_252d_slope_v014_signal(ebitda, intexp):
    base = _coverz(ebitda, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovz_504d_slope_v015_signal(ebitda, intexp):
    base = _coverz(ebitda, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovz_126d_slope_v016_signal(ncfo, intexp):
    base = _coverz(ncfo, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovz_252d_slope_v017_signal(ncfo, intexp):
    base = _coverz(ncfo, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovz_504d_slope_v018_signal(ncfo, intexp):
    base = _coverz(ncfo, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovz_126d_slope_v019_signal(ebit, intexp):
    base = _coverz(ebit, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovz_252d_slope_v020_signal(ebit, intexp):
    base = _coverz(ebit, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovz_504d_slope_v021_signal(ebit, intexp):
    base = _coverz(ebit, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovrank_126d_slope_v022_signal(fcf, intexp):
    base = _coverrank(fcf, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovrank_252d_slope_v023_signal(fcf, intexp):
    base = _coverrank(fcf, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovrank_504d_slope_v024_signal(fcf, intexp):
    base = _coverrank(fcf, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovrank_126d_slope_v025_signal(ncfo, intexp):
    base = _coverrank(ncfo, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovrank_252d_slope_v026_signal(ncfo, intexp):
    base = _coverrank(ncfo, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovrank_504d_slope_v027_signal(ncfo, intexp):
    base = _coverrank(ncfo, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovrank_126d_slope_v028_signal(ebitda, intexp):
    base = _coverrank(ebitda, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovrank_252d_slope_v029_signal(ebitda, intexp):
    base = _coverrank(ebitda, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovrank_504d_slope_v030_signal(ebitda, intexp):
    base = _coverrank(ebitda, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovtanh_126d_slope_v031_signal(ebit, intexp):
    base = _covertanh(ebit, intexp, 0.25)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovtanh_252d_slope_v032_signal(ebit, intexp):
    base = _covertanh(ebit, intexp, 0.25)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovtanh_504d_slope_v033_signal(ebit, intexp):
    base = _covertanh(ebit, intexp, 0.25)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovtanh_126d_slope_v034_signal(fcf, intexp):
    base = _covertanh(fcf, intexp, 0.30)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovtanh_252d_slope_v035_signal(fcf, intexp):
    base = _covertanh(fcf, intexp, 0.30)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovtanh_504d_slope_v036_signal(fcf, intexp):
    base = _covertanh(fcf, intexp, 0.30)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovdd_126d_slope_v037_signal(ebitda, intexp):
    base = _coverdd(ebitda, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovdd_252d_slope_v038_signal(ebitda, intexp):
    base = _coverdd(ebitda, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovdd_504d_slope_v039_signal(ebitda, intexp):
    base = _coverdd(ebitda, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovdd_126d_slope_v040_signal(ebit, intexp):
    base = _coverdd(ebit, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovdd_252d_slope_v041_signal(ebit, intexp):
    base = _coverdd(ebit, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovdd_504d_slope_v042_signal(ebit, intexp):
    base = _coverdd(ebit, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovdd_126d_slope_v043_signal(fcf, intexp):
    base = _coverdd(fcf, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovdd_252d_slope_v044_signal(fcf, intexp):
    base = _coverdd(fcf, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfcovdd_504d_slope_v045_signal(fcf, intexp):
    base = _coverdd(fcf, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovdev2_126d_slope_v046_signal(ebit, intexp):
    base = _coverdev2(ebit, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovdev2_252d_slope_v047_signal(ebit, intexp):
    base = _coverdev2(ebit, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitcovdev2_504d_slope_v048_signal(ebit, intexp):
    base = _coverdev2(ebit, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovdev2_126d_slope_v049_signal(ebitda, intexp):
    base = _coverdev2(ebitda, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovdev2_252d_slope_v050_signal(ebitda, intexp):
    base = _coverdev2(ebitda, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdacovdev2_504d_slope_v051_signal(ebitda, intexp):
    base = _coverdev2(ebitda, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_ebitda_126d_slope_v052_signal(ebitda, intexp):
    base = _std(ebitda / intexp.replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_ebitda_252d_slope_v053_signal(ebitda, intexp):
    base = _std(ebitda / intexp.replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_ebitda_504d_slope_v054_signal(ebitda, intexp):
    base = _std(ebitda / intexp.replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_ncfo_126d_slope_v055_signal(ncfo, intexp):
    base = _std(ncfo / intexp.replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_ncfo_252d_slope_v056_signal(ncfo, intexp):
    base = _std(ncfo / intexp.replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_ncfo_504d_slope_v057_signal(ncfo, intexp):
    base = _std(ncfo / intexp.replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_fcf_126d_slope_v058_signal(fcf, intexp):
    base = _std(fcf / intexp.replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_fcf_252d_slope_v059_signal(fcf, intexp):
    base = _std(fcf / intexp.replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covvol_fcf_504d_slope_v060_signal(fcf, intexp):
    base = _std(fcf / intexp.replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovrng_126d_slope_v061_signal(ncfo, intexp):
    base = _coverrng(ncfo, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovrng_252d_slope_v062_signal(ncfo, intexp):
    base = _coverrng(ncfo, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfocovrng_504d_slope_v063_signal(ncfo, intexp):
    base = _coverrng(ncfo, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdaburden_126d_slope_v064_signal(intexp, ebitda):
    base = _burden(intexp, ebitda, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdaburden_252d_slope_v065_signal(intexp, ebitda):
    base = _burden(intexp, ebitda, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdaburden_504d_slope_v066_signal(intexp, ebitda):
    base = _burden(intexp, ebitda, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfoburden_126d_slope_v067_signal(intexp, ncfo):
    base = _burden(intexp, ncfo, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfoburden_252d_slope_v068_signal(intexp, ncfo):
    base = _burden(intexp, ncfo, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfoburden_504d_slope_v069_signal(intexp, ncfo):
    base = _burden(intexp, ncfo, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitburdenrank_126d_slope_v070_signal(intexp, ebit):
    base = _burdenrank(intexp, ebit, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitburdenrank_252d_slope_v071_signal(intexp, ebit):
    base = _burdenrank(intexp, ebit, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitburdenrank_504d_slope_v072_signal(intexp, ebit):
    base = _burdenrank(intexp, ebit, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallebitz_126d_slope_v073_signal(debtc, ebit):
    base = _wallz(debtc, ebit, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallebitz_252d_slope_v074_signal(debtc, ebit):
    base = _wallz(debtc, ebit, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallebitz_504d_slope_v075_signal(debtc, ebit):
    base = _wallz(debtc, ebit, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcost_126d_slope_v076_signal(intexp, debt):
    base = _effcost(intexp, debt, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcost_252d_slope_v077_signal(intexp, debt):
    base = _effcost(intexp, debt, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcost_504d_slope_v078_signal(intexp, debt):
    base = _effcost(intexp, debt, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostz_126d_slope_v079_signal(intexp, debt):
    base = _effcostz(intexp, debt, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostz_252d_slope_v080_signal(intexp, debt):
    base = _effcostz(intexp, debt, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostz_504d_slope_v081_signal(intexp, debt):
    base = _effcostz(intexp, debt, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostc_126d_slope_v082_signal(intexp, debtc):
    base = _effcost(intexp, debtc, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostc_252d_slope_v083_signal(intexp, debtc):
    base = _effcost(intexp, debtc, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostc_504d_slope_v084_signal(intexp, debtc):
    base = _effcost(intexp, debtc, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostvol_126d_slope_v085_signal(intexp, debt):
    base = _std(intexp / debt.replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostvol_252d_slope_v086_signal(intexp, debt):
    base = _std(intexp / debt.replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_effcostvol_504d_slope_v087_signal(intexp, debt):
    base = _std(intexp / debt.replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallncfo_126d_slope_v088_signal(debtc, ncfo):
    base = _wall(debtc, ncfo, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallncfo_252d_slope_v089_signal(debtc, ncfo):
    base = _wall(debtc, ncfo, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallncfo_504d_slope_v090_signal(debtc, ncfo):
    base = _wall(debtc, ncfo, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallfcfz_126d_slope_v091_signal(debtc, fcf):
    base = _wallz(debtc, fcf, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallfcfz_252d_slope_v092_signal(debtc, fcf):
    base = _wallz(debtc, fcf, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallfcfz_504d_slope_v093_signal(debtc, fcf):
    base = _wallz(debtc, fcf, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallebitdarank_126d_slope_v094_signal(debtc, ebitda):
    base = _rank(debtc / ebitda.replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallebitdarank_252d_slope_v095_signal(debtc, ebitda):
    base = _rank(debtc / ebitda.replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_wallebitdarank_504d_slope_v096_signal(debtc, ebitda):
    base = _rank(debtc / ebitda.replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_currshare_126d_slope_v097_signal(debtc, debt):
    base = _wall(debtc, debt, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_currshare_252d_slope_v098_signal(debtc, debt):
    base = _wall(debtc, debt, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_currshare_504d_slope_v099_signal(debtc, debt):
    base = _wall(debtc, debt, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dscrz_126d_slope_v100_signal(ncfo, intexp, debtc):
    base = _z(_dscr(ncfo, intexp, debtc, 126), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dscrz_252d_slope_v101_signal(ncfo, intexp, debtc):
    base = _z(_dscr(ncfo, intexp, debtc, 252), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dscrz_504d_slope_v102_signal(ncfo, intexp, debtc):
    base = _z(_dscr(ncfo, intexp, debtc, 504), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dscrfcfz_126d_slope_v103_signal(fcf, intexp, debtc):
    base = _z(_dscr(fcf, intexp, debtc, 126), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dscrfcfz_252d_slope_v104_signal(fcf, intexp, debtc):
    base = _z(_dscr(fcf, intexp, debtc, 252), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dscrfcfz_504d_slope_v105_signal(fcf, intexp, debtc):
    base = _z(_dscr(fcf, intexp, debtc, 504), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtncfo_126d_slope_v106_signal(debt, ncfo):
    base = _logcover(debt, ncfo, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtncfo_252d_slope_v107_signal(debt, ncfo):
    base = _logcover(debt, ncfo, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtncfo_504d_slope_v108_signal(debt, ncfo):
    base = _logcover(debt, ncfo, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtebitdarank_126d_slope_v109_signal(debt, ebitda):
    base = _rank(debt / ebitda.replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtebitdarank_252d_slope_v110_signal(debt, ebitda):
    base = _rank(debt / ebitda.replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtebitdarank_504d_slope_v111_signal(debt, ebitda):
    base = _rank(debt / ebitda.replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtfcfz_126d_slope_v112_signal(debt, fcf):
    base = _z(debt / fcf.replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtfcfz_252d_slope_v113_signal(debt, fcf):
    base = _z(debt / fcf.replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_debtfcfz_504d_slope_v114_signal(debt, fcf):
    base = _z(debt / fcf.replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issint_126d_slope_v115_signal(ncfdebt, intexp):
    base = _logcover(ncfdebt, intexp, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issint_252d_slope_v116_signal(ncfdebt, intexp):
    base = _logcover(ncfdebt, intexp, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issint_504d_slope_v117_signal(ncfdebt, intexp):
    base = _logcover(ncfdebt, intexp, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issncfo_126d_slope_v118_signal(ncfdebt, ncfo):
    base = _logcover(ncfdebt, ncfo, 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issncfo_252d_slope_v119_signal(ncfdebt, ncfo):
    base = _logcover(ncfdebt, ncfo, 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issncfo_504d_slope_v120_signal(ncfdebt, ncfo):
    base = _logcover(ncfdebt, ncfo, 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_cashaccrsprz_126d_slope_v121_signal(ncfo, ebit, intexp):
    base = _z(_covspr(ncfo, ebit, intexp, 126), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_cashaccrsprz_252d_slope_v122_signal(ncfo, ebit, intexp):
    base = _z(_covspr(ncfo, ebit, intexp, 252), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_cashaccrsprz_504d_slope_v123_signal(ncfo, ebit, intexp):
    base = _z(_covspr(ncfo, ebit, intexp, 504), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfebitdasprz_126d_slope_v124_signal(fcf, ebitda, intexp):
    base = _z(_covspr(fcf, ebitda, intexp, 126), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfebitdasprz_252d_slope_v125_signal(fcf, ebitda, intexp):
    base = _z(_covspr(fcf, ebitda, intexp, 252), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfebitdasprz_504d_slope_v126_signal(fcf, ebitda, intexp):
    base = _z(_covspr(fcf, ebitda, intexp, 504), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdaebitsprz_126d_slope_v127_signal(ebitda, ebit, intexp):
    base = _z(_covspr(ebitda, ebit, intexp, 126), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdaebitsprz_252d_slope_v128_signal(ebitda, ebit, intexp):
    base = _z(_covspr(ebitda, ebit, intexp, 252), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ebitdaebitsprz_504d_slope_v129_signal(ebitda, ebit, intexp):
    base = _z(_covspr(ebitda, ebit, intexp, 504), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covpercostz_126d_slope_v130_signal(ebitda, intexp, debt):
    base = _z(_cover(ebitda, intexp, 126) * _effcost(intexp, debt, 126), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covpercostz_252d_slope_v131_signal(ebitda, intexp, debt):
    base = _z(_cover(ebitda, intexp, 252) * _effcost(intexp, debt, 252), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_covpercostz_504d_slope_v132_signal(ebitda, intexp, debt):
    base = _z(_cover(ebitda, intexp, 504) * _effcost(intexp, debt, 504), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_walltimesburdrank_126d_slope_v133_signal(debtc, ncfo, intexp, ebitda):
    base = _rank((debtc / ncfo.replace(0, np.nan)) * (intexp / ebitda.replace(0, np.nan)), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_walltimesburdrank_252d_slope_v134_signal(debtc, ncfo, intexp, ebitda):
    base = _rank((debtc / ncfo.replace(0, np.nan)) * (intexp / ebitda.replace(0, np.nan)), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_walltimesburdrank_504d_slope_v135_signal(debtc, ncfo, intexp, ebitda):
    base = _rank((debtc / ncfo.replace(0, np.nan)) * (intexp / ebitda.replace(0, np.nan)), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfconvrank_126d_slope_v136_signal(fcf, ncfo):
    base = _rank(_mean(fcf, 126) / _mean(ncfo, 126).replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfconvrank_252d_slope_v137_signal(fcf, ncfo):
    base = _rank(_mean(fcf, 252) / _mean(ncfo, 252).replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_fcfconvrank_504d_slope_v138_signal(fcf, ncfo):
    base = _rank(_mean(fcf, 504) / _mean(ncfo, 504).replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfoafterserv_126d_slope_v139_signal(ncfo, intexp, debtc):
    base = _mean(ncfo - intexp - debtc, 126) / _mean(intexp, 126).replace(0, np.nan)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfoafterserv_252d_slope_v140_signal(ncfo, intexp, debtc):
    base = _mean(ncfo - intexp - debtc, 252) / _mean(intexp, 252).replace(0, np.nan)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_ncfoafterserv_504d_slope_v141_signal(ncfo, intexp, debtc):
    base = _mean(ncfo - intexp - debtc, 504) / _mean(intexp, 504).replace(0, np.nan)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_intexpstretch_126d_slope_v142_signal(intexp):
    base = _mean(intexp, 21) / _mean(intexp, 126).replace(0, np.nan)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_intexpstretch_252d_slope_v143_signal(intexp):
    base = _mean(intexp, 21) / _mean(intexp, 252).replace(0, np.nan)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_intexpstretch_504d_slope_v144_signal(intexp):
    base = _mean(intexp, 21) / _mean(intexp, 504).replace(0, np.nan)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dacushionrank_126d_slope_v145_signal(ebitda, ebit):
    base = _rank((_mean(ebitda, 126) - _mean(ebit, 126)) / _mean(ebitda, 126).replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dacushionrank_252d_slope_v146_signal(ebitda, ebit):
    base = _rank((_mean(ebitda, 252) - _mean(ebit, 252)) / _mean(ebitda, 252).replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_dacushionrank_504d_slope_v147_signal(ebitda, ebit):
    base = _rank((_mean(ebitda, 504) - _mean(ebit, 504)) / _mean(ebitda, 504).replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issdebtcz_126d_slope_v148_signal(ncfdebt, debtc):
    base = _z(ncfdebt / debtc.replace(0, np.nan), 126)
    sl = base.diff(31) / float(31)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issdebtcz_252d_slope_v149_signal(ncfdebt, debtc):
    base = _z(ncfdebt / debtc.replace(0, np.nan), 252)
    sl = base.diff(63) / float(63)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)

def f48ic_f48_interest_coverage_issdebtcz_504d_slope_v150_signal(ncfdebt, debtc):
    base = _z(ncfdebt / debtc.replace(0, np.nan), 504)
    sl = base.diff(126) / float(126)
    result = sl
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f48ic_f48_interest_coverage_ebitcov_126d_slope_v001_signal,
    f48ic_f48_interest_coverage_ebitcov_252d_slope_v002_signal,
    f48ic_f48_interest_coverage_ebitcov_504d_slope_v003_signal,
    f48ic_f48_interest_coverage_ebitdacov_126d_slope_v004_signal,
    f48ic_f48_interest_coverage_ebitdacov_252d_slope_v005_signal,
    f48ic_f48_interest_coverage_ebitdacov_504d_slope_v006_signal,
    f48ic_f48_interest_coverage_ncfocov_126d_slope_v007_signal,
    f48ic_f48_interest_coverage_ncfocov_252d_slope_v008_signal,
    f48ic_f48_interest_coverage_ncfocov_504d_slope_v009_signal,
    f48ic_f48_interest_coverage_fcfcov_126d_slope_v010_signal,
    f48ic_f48_interest_coverage_fcfcov_252d_slope_v011_signal,
    f48ic_f48_interest_coverage_fcfcov_504d_slope_v012_signal,
    f48ic_f48_interest_coverage_ebitdacovz_126d_slope_v013_signal,
    f48ic_f48_interest_coverage_ebitdacovz_252d_slope_v014_signal,
    f48ic_f48_interest_coverage_ebitdacovz_504d_slope_v015_signal,
    f48ic_f48_interest_coverage_ncfocovz_126d_slope_v016_signal,
    f48ic_f48_interest_coverage_ncfocovz_252d_slope_v017_signal,
    f48ic_f48_interest_coverage_ncfocovz_504d_slope_v018_signal,
    f48ic_f48_interest_coverage_ebitcovz_126d_slope_v019_signal,
    f48ic_f48_interest_coverage_ebitcovz_252d_slope_v020_signal,
    f48ic_f48_interest_coverage_ebitcovz_504d_slope_v021_signal,
    f48ic_f48_interest_coverage_fcfcovrank_126d_slope_v022_signal,
    f48ic_f48_interest_coverage_fcfcovrank_252d_slope_v023_signal,
    f48ic_f48_interest_coverage_fcfcovrank_504d_slope_v024_signal,
    f48ic_f48_interest_coverage_ncfocovrank_126d_slope_v025_signal,
    f48ic_f48_interest_coverage_ncfocovrank_252d_slope_v026_signal,
    f48ic_f48_interest_coverage_ncfocovrank_504d_slope_v027_signal,
    f48ic_f48_interest_coverage_ebitdacovrank_126d_slope_v028_signal,
    f48ic_f48_interest_coverage_ebitdacovrank_252d_slope_v029_signal,
    f48ic_f48_interest_coverage_ebitdacovrank_504d_slope_v030_signal,
    f48ic_f48_interest_coverage_ebitcovtanh_126d_slope_v031_signal,
    f48ic_f48_interest_coverage_ebitcovtanh_252d_slope_v032_signal,
    f48ic_f48_interest_coverage_ebitcovtanh_504d_slope_v033_signal,
    f48ic_f48_interest_coverage_fcfcovtanh_126d_slope_v034_signal,
    f48ic_f48_interest_coverage_fcfcovtanh_252d_slope_v035_signal,
    f48ic_f48_interest_coverage_fcfcovtanh_504d_slope_v036_signal,
    f48ic_f48_interest_coverage_ebitdacovdd_126d_slope_v037_signal,
    f48ic_f48_interest_coverage_ebitdacovdd_252d_slope_v038_signal,
    f48ic_f48_interest_coverage_ebitdacovdd_504d_slope_v039_signal,
    f48ic_f48_interest_coverage_ebitcovdd_126d_slope_v040_signal,
    f48ic_f48_interest_coverage_ebitcovdd_252d_slope_v041_signal,
    f48ic_f48_interest_coverage_ebitcovdd_504d_slope_v042_signal,
    f48ic_f48_interest_coverage_fcfcovdd_126d_slope_v043_signal,
    f48ic_f48_interest_coverage_fcfcovdd_252d_slope_v044_signal,
    f48ic_f48_interest_coverage_fcfcovdd_504d_slope_v045_signal,
    f48ic_f48_interest_coverage_ebitcovdev2_126d_slope_v046_signal,
    f48ic_f48_interest_coverage_ebitcovdev2_252d_slope_v047_signal,
    f48ic_f48_interest_coverage_ebitcovdev2_504d_slope_v048_signal,
    f48ic_f48_interest_coverage_ebitdacovdev2_126d_slope_v049_signal,
    f48ic_f48_interest_coverage_ebitdacovdev2_252d_slope_v050_signal,
    f48ic_f48_interest_coverage_ebitdacovdev2_504d_slope_v051_signal,
    f48ic_f48_interest_coverage_covvol_ebitda_126d_slope_v052_signal,
    f48ic_f48_interest_coverage_covvol_ebitda_252d_slope_v053_signal,
    f48ic_f48_interest_coverage_covvol_ebitda_504d_slope_v054_signal,
    f48ic_f48_interest_coverage_covvol_ncfo_126d_slope_v055_signal,
    f48ic_f48_interest_coverage_covvol_ncfo_252d_slope_v056_signal,
    f48ic_f48_interest_coverage_covvol_ncfo_504d_slope_v057_signal,
    f48ic_f48_interest_coverage_covvol_fcf_126d_slope_v058_signal,
    f48ic_f48_interest_coverage_covvol_fcf_252d_slope_v059_signal,
    f48ic_f48_interest_coverage_covvol_fcf_504d_slope_v060_signal,
    f48ic_f48_interest_coverage_ncfocovrng_126d_slope_v061_signal,
    f48ic_f48_interest_coverage_ncfocovrng_252d_slope_v062_signal,
    f48ic_f48_interest_coverage_ncfocovrng_504d_slope_v063_signal,
    f48ic_f48_interest_coverage_ebitdaburden_126d_slope_v064_signal,
    f48ic_f48_interest_coverage_ebitdaburden_252d_slope_v065_signal,
    f48ic_f48_interest_coverage_ebitdaburden_504d_slope_v066_signal,
    f48ic_f48_interest_coverage_ncfoburden_126d_slope_v067_signal,
    f48ic_f48_interest_coverage_ncfoburden_252d_slope_v068_signal,
    f48ic_f48_interest_coverage_ncfoburden_504d_slope_v069_signal,
    f48ic_f48_interest_coverage_ebitburdenrank_126d_slope_v070_signal,
    f48ic_f48_interest_coverage_ebitburdenrank_252d_slope_v071_signal,
    f48ic_f48_interest_coverage_ebitburdenrank_504d_slope_v072_signal,
    f48ic_f48_interest_coverage_wallebitz_126d_slope_v073_signal,
    f48ic_f48_interest_coverage_wallebitz_252d_slope_v074_signal,
    f48ic_f48_interest_coverage_wallebitz_504d_slope_v075_signal,
    f48ic_f48_interest_coverage_effcost_126d_slope_v076_signal,
    f48ic_f48_interest_coverage_effcost_252d_slope_v077_signal,
    f48ic_f48_interest_coverage_effcost_504d_slope_v078_signal,
    f48ic_f48_interest_coverage_effcostz_126d_slope_v079_signal,
    f48ic_f48_interest_coverage_effcostz_252d_slope_v080_signal,
    f48ic_f48_interest_coverage_effcostz_504d_slope_v081_signal,
    f48ic_f48_interest_coverage_effcostc_126d_slope_v082_signal,
    f48ic_f48_interest_coverage_effcostc_252d_slope_v083_signal,
    f48ic_f48_interest_coverage_effcostc_504d_slope_v084_signal,
    f48ic_f48_interest_coverage_effcostvol_126d_slope_v085_signal,
    f48ic_f48_interest_coverage_effcostvol_252d_slope_v086_signal,
    f48ic_f48_interest_coverage_effcostvol_504d_slope_v087_signal,
    f48ic_f48_interest_coverage_wallncfo_126d_slope_v088_signal,
    f48ic_f48_interest_coverage_wallncfo_252d_slope_v089_signal,
    f48ic_f48_interest_coverage_wallncfo_504d_slope_v090_signal,
    f48ic_f48_interest_coverage_wallfcfz_126d_slope_v091_signal,
    f48ic_f48_interest_coverage_wallfcfz_252d_slope_v092_signal,
    f48ic_f48_interest_coverage_wallfcfz_504d_slope_v093_signal,
    f48ic_f48_interest_coverage_wallebitdarank_126d_slope_v094_signal,
    f48ic_f48_interest_coverage_wallebitdarank_252d_slope_v095_signal,
    f48ic_f48_interest_coverage_wallebitdarank_504d_slope_v096_signal,
    f48ic_f48_interest_coverage_currshare_126d_slope_v097_signal,
    f48ic_f48_interest_coverage_currshare_252d_slope_v098_signal,
    f48ic_f48_interest_coverage_currshare_504d_slope_v099_signal,
    f48ic_f48_interest_coverage_dscrz_126d_slope_v100_signal,
    f48ic_f48_interest_coverage_dscrz_252d_slope_v101_signal,
    f48ic_f48_interest_coverage_dscrz_504d_slope_v102_signal,
    f48ic_f48_interest_coverage_dscrfcfz_126d_slope_v103_signal,
    f48ic_f48_interest_coverage_dscrfcfz_252d_slope_v104_signal,
    f48ic_f48_interest_coverage_dscrfcfz_504d_slope_v105_signal,
    f48ic_f48_interest_coverage_debtncfo_126d_slope_v106_signal,
    f48ic_f48_interest_coverage_debtncfo_252d_slope_v107_signal,
    f48ic_f48_interest_coverage_debtncfo_504d_slope_v108_signal,
    f48ic_f48_interest_coverage_debtebitdarank_126d_slope_v109_signal,
    f48ic_f48_interest_coverage_debtebitdarank_252d_slope_v110_signal,
    f48ic_f48_interest_coverage_debtebitdarank_504d_slope_v111_signal,
    f48ic_f48_interest_coverage_debtfcfz_126d_slope_v112_signal,
    f48ic_f48_interest_coverage_debtfcfz_252d_slope_v113_signal,
    f48ic_f48_interest_coverage_debtfcfz_504d_slope_v114_signal,
    f48ic_f48_interest_coverage_issint_126d_slope_v115_signal,
    f48ic_f48_interest_coverage_issint_252d_slope_v116_signal,
    f48ic_f48_interest_coverage_issint_504d_slope_v117_signal,
    f48ic_f48_interest_coverage_issncfo_126d_slope_v118_signal,
    f48ic_f48_interest_coverage_issncfo_252d_slope_v119_signal,
    f48ic_f48_interest_coverage_issncfo_504d_slope_v120_signal,
    f48ic_f48_interest_coverage_cashaccrsprz_126d_slope_v121_signal,
    f48ic_f48_interest_coverage_cashaccrsprz_252d_slope_v122_signal,
    f48ic_f48_interest_coverage_cashaccrsprz_504d_slope_v123_signal,
    f48ic_f48_interest_coverage_fcfebitdasprz_126d_slope_v124_signal,
    f48ic_f48_interest_coverage_fcfebitdasprz_252d_slope_v125_signal,
    f48ic_f48_interest_coverage_fcfebitdasprz_504d_slope_v126_signal,
    f48ic_f48_interest_coverage_ebitdaebitsprz_126d_slope_v127_signal,
    f48ic_f48_interest_coverage_ebitdaebitsprz_252d_slope_v128_signal,
    f48ic_f48_interest_coverage_ebitdaebitsprz_504d_slope_v129_signal,
    f48ic_f48_interest_coverage_covpercostz_126d_slope_v130_signal,
    f48ic_f48_interest_coverage_covpercostz_252d_slope_v131_signal,
    f48ic_f48_interest_coverage_covpercostz_504d_slope_v132_signal,
    f48ic_f48_interest_coverage_walltimesburdrank_126d_slope_v133_signal,
    f48ic_f48_interest_coverage_walltimesburdrank_252d_slope_v134_signal,
    f48ic_f48_interest_coverage_walltimesburdrank_504d_slope_v135_signal,
    f48ic_f48_interest_coverage_fcfconvrank_126d_slope_v136_signal,
    f48ic_f48_interest_coverage_fcfconvrank_252d_slope_v137_signal,
    f48ic_f48_interest_coverage_fcfconvrank_504d_slope_v138_signal,
    f48ic_f48_interest_coverage_ncfoafterserv_126d_slope_v139_signal,
    f48ic_f48_interest_coverage_ncfoafterserv_252d_slope_v140_signal,
    f48ic_f48_interest_coverage_ncfoafterserv_504d_slope_v141_signal,
    f48ic_f48_interest_coverage_intexpstretch_126d_slope_v142_signal,
    f48ic_f48_interest_coverage_intexpstretch_252d_slope_v143_signal,
    f48ic_f48_interest_coverage_intexpstretch_504d_slope_v144_signal,
    f48ic_f48_interest_coverage_dacushionrank_126d_slope_v145_signal,
    f48ic_f48_interest_coverage_dacushionrank_252d_slope_v146_signal,
    f48ic_f48_interest_coverage_dacushionrank_504d_slope_v147_signal,
    f48ic_f48_interest_coverage_issdebtcz_126d_slope_v148_signal,
    f48ic_f48_interest_coverage_issdebtcz_252d_slope_v149_signal,
    f48ic_f48_interest_coverage_issdebtcz_504d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F48_INTEREST_COVERAGE_REGISTRY_2ND_001_150 = REGISTRY


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
        "assetturnover", "invcap", "intexp", "taxexp", "ebt", "sps", "bvps", "tbvps",
        "de", "ncfdiv", "ncfinv", "dps", "divyield", "payoutratio", "prefdivis",
        "netincdis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
        "shrholders", "shrvalue", "shrunits", "totalvalue", "percentoftotal",
        "fndholders", "undholders", "prfholders", "dbtholders", "putholders",
        "putvalue", "cllholders", "cllvalue", "wntholders", "wntvalue", "dbtvalue",
        "fndvalue", "undvalue", "prfvalue", "fndunits", "undunits",
    }

    def _fund(seed, base=1e8, drift=0.03, vol=0.07, allow_neg=False):
        g = np.random.default_rng(seed)
        steps = np.repeat(g.normal(drift, vol, n // 63 + 1), 63)[:n]
        s = base * np.exp(np.cumsum(steps / 63))
        if allow_neg:
            s = s - base * 0.6
        return pd.Series(s, name=None)

    intexp = _fund(101, base=8e6, drift=0.02, vol=0.05).rename("intexp")
    ebit = _fund(102, base=4e7, drift=0.02, vol=0.09, allow_neg=True).rename("ebit")
    ebitda = _fund(103, base=7e7, drift=0.02, vol=0.08, allow_neg=True).rename("ebitda")
    ncfo = _fund(104, base=6e7, drift=0.02, vol=0.09, allow_neg=True).rename("ncfo")
    fcf = _fund(105, base=3e7, drift=0.02, vol=0.11, allow_neg=True).rename("fcf")
    debt = _fund(106, base=5e8, drift=0.025, vol=0.05).rename("debt")
    debtc = _fund(107, base=9e7, drift=0.025, vol=0.07).rename("debtc")
    ncfdebt = _fund(108, base=2e7, drift=0.0, vol=0.13, allow_neg=True).rename("ncfdebt")

    cols = {
        "intexp": intexp, "ebit": ebit, "ebitda": ebitda, "ncfo": ncfo,
        "fcf": fcf, "debt": debt, "debtc": debtc, "ncfdebt": ncfdebt,
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
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK %s: %d features pass" % ("f48_interest_coverage_2nd_derivatives_001_150_claude", n_features))
