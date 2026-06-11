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


# ===== folder domain primitives (earnings quality / accruals) =====
def _f36eq_growth(s, w):
    # fractional growth of a level over w days
    return s / s.shift(w).replace(0, np.nan) - 1.0


def _f36eq_loggrowth(s, w):
    return np.log(s.replace(0, np.nan) / s.shift(w).replace(0, np.nan))


def _f36eq_accrual(netinc, ncfo, assets):
    # Sloan total accruals: (earnings - operating cash flow) / assets
    return (netinc - ncfo) / assets.replace(0, np.nan)


def _f36eq_cash_spread(ncfo, netinc, scale):
    # cash-earnings spread normalized by a positive scale
    return (ncfo - netinc) / scale.replace(0, np.nan)


def _f36eq_conv(ncfo, netinc):
    # cash conversion: operating cash flow per unit of (positive) earnings
    return ncfo / netinc.where(netinc > 0, np.nan)


def _f36eq_dwc(workingcapital, w, assets):
    # change in working capital over w days, scaled by assets (accrual proxy)
    return (workingcapital - workingcapital.shift(w)) / assets.replace(0, np.nan)


def _f36eq_recv_intensity(receivables, revenue):
    # receivables relative to revenue (collection / DSO proxy)
    return receivables / revenue.replace(0, np.nan)


# Sloan accrual (netinc-ncfo)/assets, level over 126d
def f36eq_f36_earnings_quality_accruals_accruallvl_126d_base_v001_signal(netinc, ncfo, assets):
    b = (_f36eq_accrual(netinc, ncfo, assets)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual (netinc-ncfo)/revenue, level over 63d
def f36eq_f36_earnings_quality_accruals_accrrevlvl_63d_base_v002_signal(netinc, ncfo, revenue):
    b = ((netinc - ncfo) / revenue.replace(0, np.nan)).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash return on assets ncfo/assets, level over 126d
def f36eq_f36_earnings_quality_accruals_cashroalvl_126d_base_v003_signal(ncfo, assets):
    b = (ncfo / assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings return on assets netinc/assets, level over 252d
def f36eq_f36_earnings_quality_accruals_earnroalvl_252d_base_v004_signal(netinc, assets):
    b = (netinc / assets.replace(0, np.nan)).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/operating-cash intensity, level over 126d
def f36eq_f36_earnings_quality_accruals_recvcashlvl_126d_base_v005_signal(receivables, ncfo):
    b = (receivables / ncfo.where(ncfo > 0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue intensity (DSO proxy), level over 63d
def f36eq_f36_earnings_quality_accruals_recvintlvl_63d_base_v006_signal(receivables, revenue):
    b = (_f36eq_recv_intensity(receivables, revenue)).rolling(63, min_periods=max(1, 63 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/assets intensity, level over 126d
def f36eq_f36_earnings_quality_accruals_recvassetslvl_126d_base_v007_signal(receivables, assets):
    b = (receivables / assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets intensity, level over 126d
def f36eq_f36_earnings_quality_accruals_wcintlvl_126d_base_v008_signal(workingcapital, assets):
    b = (workingcapital / assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/revenue intensity, level over 252d
def f36eq_f36_earnings_quality_accruals_wcrevintlvl_252d_base_v009_signal(workingcapital, revenue):
    b = (workingcapital / revenue.replace(0, np.nan)).rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual (netinc-ncfo)/assets, z-score over 252d
def f36eq_f36_earnings_quality_accruals_accrualz_252d_base_v010_signal(netinc, ncfo, assets):
    b = _z((_f36eq_accrual(netinc, ncfo, assets)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash return on assets ncfo/assets, z-score over 252d
def f36eq_f36_earnings_quality_accruals_cashroaz_252d_base_v011_signal(ncfo, assets):
    b = _z((ncfo / assets.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings return on assets netinc/assets, z-score over 378d
def f36eq_f36_earnings_quality_accruals_earnroaz_378d_base_v012_signal(netinc, assets):
    b = _z((netinc / assets.replace(0, np.nan)), 378)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/operating-cash intensity, z-score over 252d
def f36eq_f36_earnings_quality_accruals_recvcashz_252d_base_v013_signal(receivables, ncfo):
    b = _z((receivables / ncfo.where(ncfo > 0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue intensity (DSO proxy), z-score over 252d
def f36eq_f36_earnings_quality_accruals_recvintz_252d_base_v014_signal(receivables, revenue):
    b = _z((_f36eq_recv_intensity(receivables, revenue)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/assets intensity, z-score over 252d
def f36eq_f36_earnings_quality_accruals_recvassetsz_252d_base_v015_signal(receivables, assets):
    b = _z((receivables / assets.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets intensity, z-score over 252d
def f36eq_f36_earnings_quality_accruals_wcintz_252d_base_v016_signal(workingcapital, assets):
    b = _z((workingcapital / assets.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/revenue intensity, z-score over 126d
def f36eq_f36_earnings_quality_accruals_wcrevintz_126d_base_v017_signal(workingcapital, revenue):
    b = _z((workingcapital / revenue.replace(0, np.nan)), 126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual (netinc-ncfo)/assets, percentile rank over 504d
def f36eq_f36_earnings_quality_accruals_accrualrank_504d_base_v018_signal(netinc, ncfo, assets):
    b = _rank((_f36eq_accrual(netinc, ncfo, assets)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash return on assets ncfo/assets, percentile rank over 504d
def f36eq_f36_earnings_quality_accruals_cashroarank_504d_base_v019_signal(ncfo, assets):
    b = _rank((ncfo / assets.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings return on assets netinc/assets, percentile rank over 504d
def f36eq_f36_earnings_quality_accruals_earnroarank_504d_base_v020_signal(netinc, assets):
    b = _rank((netinc / assets.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/operating-cash intensity, percentile rank over 504d
def f36eq_f36_earnings_quality_accruals_recvcashrank_504d_base_v021_signal(receivables, ncfo):
    b = _rank((receivables / ncfo.where(ncfo > 0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue intensity (DSO proxy), percentile rank over 504d
def f36eq_f36_earnings_quality_accruals_recvintrank_504d_base_v022_signal(receivables, revenue):
    b = _rank((_f36eq_recv_intensity(receivables, revenue)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/assets intensity, percentile rank over 504d
def f36eq_f36_earnings_quality_accruals_recvassetsrank_504d_base_v023_signal(receivables, assets):
    b = _rank((receivables / assets.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets intensity, percentile rank over 504d
def f36eq_f36_earnings_quality_accruals_wcintrank_504d_base_v024_signal(workingcapital, assets):
    b = _rank((workingcapital / assets.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/revenue intensity, percentile rank over 504d
def f36eq_f36_earnings_quality_accruals_wcrevintrank_504d_base_v025_signal(workingcapital, revenue):
    b = _rank((workingcapital / revenue.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual (netinc-ncfo)/assets, change over 252d
def f36eq_f36_earnings_quality_accruals_accrualchg_252d_base_v026_signal(netinc, ncfo, assets):
    _a = (_f36eq_accrual(netinc, ncfo, assets))
    b = _a - _a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual (netinc-ncfo)/revenue, change over 126d
def f36eq_f36_earnings_quality_accruals_accrrevchg_126d_base_v027_signal(netinc, ncfo, revenue):
    _a = ((netinc - ncfo) / revenue.replace(0, np.nan))
    b = _a - _a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash return on assets ncfo/assets, change over 252d
def f36eq_f36_earnings_quality_accruals_cashroachg_252d_base_v028_signal(ncfo, assets):
    _a = (ncfo / assets.replace(0, np.nan))
    b = _a - _a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings return on assets netinc/assets, change over 126d
def f36eq_f36_earnings_quality_accruals_earnroachg_126d_base_v029_signal(netinc, assets):
    _a = (netinc / assets.replace(0, np.nan))
    b = _a - _a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/operating-cash intensity, change over 252d
def f36eq_f36_earnings_quality_accruals_recvcashchg_252d_base_v030_signal(receivables, ncfo):
    _a = (receivables / ncfo.where(ncfo > 0, np.nan))
    b = _a - _a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue intensity (DSO proxy), change over 126d
def f36eq_f36_earnings_quality_accruals_recvintchg_126d_base_v031_signal(receivables, revenue):
    _a = (_f36eq_recv_intensity(receivables, revenue))
    b = _a - _a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/assets intensity, change over 252d
def f36eq_f36_earnings_quality_accruals_recvassetschg_252d_base_v032_signal(receivables, assets):
    _a = (receivables / assets.replace(0, np.nan))
    b = _a - _a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets intensity, change over 126d
def f36eq_f36_earnings_quality_accruals_wcintchg_126d_base_v033_signal(workingcapital, assets):
    _a = (workingcapital / assets.replace(0, np.nan))
    b = _a - _a.shift(126)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/revenue intensity, change over 252d
def f36eq_f36_earnings_quality_accruals_wcrevintchg_252d_base_v034_signal(workingcapital, revenue):
    _a = (workingcapital / revenue.replace(0, np.nan))
    b = _a - _a.shift(252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual (netinc-ncfo)/assets, EMA displacement over 126d
def f36eq_f36_earnings_quality_accruals_accrualemad_126d_base_v035_signal(netinc, ncfo, assets):
    _a = (_f36eq_accrual(netinc, ncfo, assets))
    b = _a - _a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual (netinc-ncfo)/revenue, EMA displacement over 252d
def f36eq_f36_earnings_quality_accruals_accrrevemad_252d_base_v036_signal(netinc, ncfo, revenue):
    _a = ((netinc - ncfo) / revenue.replace(0, np.nan))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash return on assets ncfo/assets, EMA displacement over 126d
def f36eq_f36_earnings_quality_accruals_cashroaemad_126d_base_v037_signal(ncfo, assets):
    _a = (ncfo / assets.replace(0, np.nan))
    b = _a - _a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings return on assets netinc/assets, EMA displacement over 252d
def f36eq_f36_earnings_quality_accruals_earnroaemad_252d_base_v038_signal(netinc, assets):
    _a = (netinc / assets.replace(0, np.nan))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/operating-cash intensity, EMA displacement over 252d
def f36eq_f36_earnings_quality_accruals_recvcashemad_252d_base_v039_signal(receivables, ncfo):
    _a = (receivables / ncfo.where(ncfo > 0, np.nan))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue intensity (DSO proxy), EMA displacement over 252d
def f36eq_f36_earnings_quality_accruals_recvintemad_252d_base_v040_signal(receivables, revenue):
    _a = (_f36eq_recv_intensity(receivables, revenue))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/assets intensity, EMA displacement over 126d
def f36eq_f36_earnings_quality_accruals_recvassetsemad_126d_base_v041_signal(receivables, assets):
    _a = (receivables / assets.replace(0, np.nan))
    b = _a - _a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets intensity, EMA displacement over 252d
def f36eq_f36_earnings_quality_accruals_wcintemad_252d_base_v042_signal(workingcapital, assets):
    _a = (workingcapital / assets.replace(0, np.nan))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/revenue intensity, EMA displacement over 126d
def f36eq_f36_earnings_quality_accruals_wcrevintemad_126d_base_v043_signal(workingcapital, revenue):
    _a = (workingcapital / revenue.replace(0, np.nan))
    b = _a - _a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual (netinc-ncfo)/assets, dispersion over 252d
def f36eq_f36_earnings_quality_accruals_accrualdisp_252d_base_v044_signal(netinc, ncfo, assets):
    b = _std((_f36eq_accrual(netinc, ncfo, assets)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual (netinc-ncfo)/revenue, dispersion over 252d
def f36eq_f36_earnings_quality_accruals_accrrevdisp_252d_base_v045_signal(netinc, ncfo, revenue):
    b = _std(((netinc - ncfo) / revenue.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash return on assets ncfo/assets, dispersion over 504d
def f36eq_f36_earnings_quality_accruals_cashroadisp_504d_base_v046_signal(ncfo, assets):
    b = _std((ncfo / assets.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings return on assets netinc/assets, dispersion over 504d
def f36eq_f36_earnings_quality_accruals_earnroadisp_504d_base_v047_signal(netinc, assets):
    b = _std((netinc / assets.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion ncfo/positive-netinc, dispersion over 252d
def f36eq_f36_earnings_quality_accruals_convdisp_252d_base_v048_signal(ncfo, netinc):
    b = _std((_f36eq_conv(ncfo, netinc)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/operating-cash intensity, dispersion over 504d
def f36eq_f36_earnings_quality_accruals_recvcashdisp_504d_base_v049_signal(receivables, ncfo):
    b = _std((receivables / ncfo.where(ncfo > 0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue intensity (DSO proxy), dispersion over 252d
def f36eq_f36_earnings_quality_accruals_recvintdisp_252d_base_v050_signal(receivables, revenue):
    b = _std((_f36eq_recv_intensity(receivables, revenue)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/assets intensity, dispersion over 504d
def f36eq_f36_earnings_quality_accruals_recvassetsdisp_504d_base_v051_signal(receivables, assets):
    b = _std((receivables / assets.replace(0, np.nan)), 504)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets intensity, dispersion over 252d
def f36eq_f36_earnings_quality_accruals_wcintdisp_252d_base_v052_signal(workingcapital, assets):
    b = _std((workingcapital / assets.replace(0, np.nan)), 252)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual (netinc-ncfo)/assets, stability (mean/std) over 504d
def f36eq_f36_earnings_quality_accruals_accrualstab_504d_base_v053_signal(netinc, ncfo, assets):
    _a = (_f36eq_accrual(netinc, ncfo, assets))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual (netinc-ncfo)/revenue, stability (mean/std) over 252d
def f36eq_f36_earnings_quality_accruals_accrrevstab_252d_base_v054_signal(netinc, ncfo, revenue):
    _a = ((netinc - ncfo) / revenue.replace(0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash return on assets ncfo/assets, stability (mean/std) over 252d
def f36eq_f36_earnings_quality_accruals_cashroastab_252d_base_v055_signal(ncfo, assets):
    _a = (ncfo / assets.replace(0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings return on assets netinc/assets, stability (mean/std) over 504d
def f36eq_f36_earnings_quality_accruals_earnroastab_504d_base_v056_signal(netinc, assets):
    _a = (netinc / assets.replace(0, np.nan))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion ncfo/positive-netinc, stability (mean/std) over 504d
def f36eq_f36_earnings_quality_accruals_convstab_504d_base_v057_signal(ncfo, netinc):
    _a = (_f36eq_conv(ncfo, netinc))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/operating-cash intensity, stability (mean/std) over 252d
def f36eq_f36_earnings_quality_accruals_recvcashstab_252d_base_v058_signal(receivables, ncfo):
    _a = (receivables / ncfo.where(ncfo > 0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue intensity (DSO proxy), stability (mean/std) over 504d
def f36eq_f36_earnings_quality_accruals_recvintstab_504d_base_v059_signal(receivables, revenue):
    _a = (_f36eq_recv_intensity(receivables, revenue))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/assets intensity, stability (mean/std) over 252d
def f36eq_f36_earnings_quality_accruals_recvassetsstab_252d_base_v060_signal(receivables, assets):
    _a = (receivables / assets.replace(0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets intensity, stability (mean/std) over 504d
def f36eq_f36_earnings_quality_accruals_wcintstab_504d_base_v061_signal(workingcapital, assets):
    _a = (workingcapital / assets.replace(0, np.nan))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/revenue intensity, stability (mean/std) over 252d
def f36eq_f36_earnings_quality_accruals_wcrevintstab_252d_base_v062_signal(workingcapital, revenue):
    _a = (workingcapital / revenue.replace(0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# Sloan accrual (netinc-ncfo)/assets, above-median regime fraction over 252d
def f36eq_f36_earnings_quality_accruals_accrualregm_252d_base_v063_signal(netinc, ncfo, assets):
    _a = (_f36eq_accrual(netinc, ncfo, assets))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# accrual (netinc-ncfo)/revenue, above-median regime fraction over 504d
def f36eq_f36_earnings_quality_accruals_accrrevregm_504d_base_v064_signal(netinc, ncfo, revenue):
    _a = ((netinc - ncfo) / revenue.replace(0, np.nan))
    _med = _a.rolling(504, min_periods=max(1, 504 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# operating cash return on assets ncfo/assets, above-median regime fraction over 252d
def f36eq_f36_earnings_quality_accruals_cashroaregm_252d_base_v065_signal(ncfo, assets):
    _a = (ncfo / assets.replace(0, np.nan))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# earnings return on assets netinc/assets, above-median regime fraction over 252d
def f36eq_f36_earnings_quality_accruals_earnroaregm_252d_base_v066_signal(netinc, assets):
    _a = (netinc / assets.replace(0, np.nan))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cash conversion ncfo/positive-netinc, above-median regime fraction over 504d
def f36eq_f36_earnings_quality_accruals_convregm_504d_base_v067_signal(ncfo, netinc):
    _a = (_f36eq_conv(ncfo, netinc))
    _med = _a.rolling(504, min_periods=max(1, 504 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/operating-cash intensity, above-median regime fraction over 252d
def f36eq_f36_earnings_quality_accruals_recvcashregm_252d_base_v068_signal(receivables, ncfo):
    _a = (receivables / ncfo.where(ncfo > 0, np.nan))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/revenue intensity (DSO proxy), above-median regime fraction over 252d
def f36eq_f36_earnings_quality_accruals_recvintregm_252d_base_v069_signal(receivables, revenue):
    _a = (_f36eq_recv_intensity(receivables, revenue))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables/assets intensity, above-median regime fraction over 504d
def f36eq_f36_earnings_quality_accruals_recvassetsregm_504d_base_v070_signal(receivables, assets):
    _a = (receivables / assets.replace(0, np.nan))
    _med = _a.rolling(504, min_periods=max(1, 504 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/assets intensity, above-median regime fraction over 252d
def f36eq_f36_earnings_quality_accruals_wcintregm_252d_base_v071_signal(workingcapital, assets):
    _a = (workingcapital / assets.replace(0, np.nan))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# working-capital/revenue intensity, above-median regime fraction over 504d
def f36eq_f36_earnings_quality_accruals_wcrevintregm_504d_base_v072_signal(workingcapital, revenue):
    _a = (workingcapital / revenue.replace(0, np.nan))
    _med = _a.rolling(504, min_periods=max(1, 504 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(504, min_periods=max(1, 504 // 2)).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus revenue-growth over 63d (channel-stuffing risk)
def f36eq_f36_earnings_quality_accruals_recvrevg_63d_base_v073_signal(receivables, revenue):
    rg = _f36eq_growth(receivables, 63)
    vg = _f36eq_growth(revenue, 63)
    b = rg - vg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus revenue-growth over 126d (channel-stuffing risk)
def f36eq_f36_earnings_quality_accruals_recvrevg_126d_base_v074_signal(receivables, revenue):
    rg = _f36eq_growth(receivables, 126)
    vg = _f36eq_growth(revenue, 126)
    b = rg - vg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# receivables-growth minus revenue-growth over 252d (channel-stuffing risk)
def f36eq_f36_earnings_quality_accruals_recvrevg_252d_base_v075_signal(receivables, revenue):
    rg = _f36eq_growth(receivables, 252)
    vg = _f36eq_growth(revenue, 252)
    b = rg - vg
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36eq_f36_earnings_quality_accruals_accruallvl_126d_base_v001_signal,
    f36eq_f36_earnings_quality_accruals_accrrevlvl_63d_base_v002_signal,
    f36eq_f36_earnings_quality_accruals_cashroalvl_126d_base_v003_signal,
    f36eq_f36_earnings_quality_accruals_earnroalvl_252d_base_v004_signal,
    f36eq_f36_earnings_quality_accruals_recvcashlvl_126d_base_v005_signal,
    f36eq_f36_earnings_quality_accruals_recvintlvl_63d_base_v006_signal,
    f36eq_f36_earnings_quality_accruals_recvassetslvl_126d_base_v007_signal,
    f36eq_f36_earnings_quality_accruals_wcintlvl_126d_base_v008_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintlvl_252d_base_v009_signal,
    f36eq_f36_earnings_quality_accruals_accrualz_252d_base_v010_signal,
    f36eq_f36_earnings_quality_accruals_cashroaz_252d_base_v011_signal,
    f36eq_f36_earnings_quality_accruals_earnroaz_378d_base_v012_signal,
    f36eq_f36_earnings_quality_accruals_recvcashz_252d_base_v013_signal,
    f36eq_f36_earnings_quality_accruals_recvintz_252d_base_v014_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsz_252d_base_v015_signal,
    f36eq_f36_earnings_quality_accruals_wcintz_252d_base_v016_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintz_126d_base_v017_signal,
    f36eq_f36_earnings_quality_accruals_accrualrank_504d_base_v018_signal,
    f36eq_f36_earnings_quality_accruals_cashroarank_504d_base_v019_signal,
    f36eq_f36_earnings_quality_accruals_earnroarank_504d_base_v020_signal,
    f36eq_f36_earnings_quality_accruals_recvcashrank_504d_base_v021_signal,
    f36eq_f36_earnings_quality_accruals_recvintrank_504d_base_v022_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsrank_504d_base_v023_signal,
    f36eq_f36_earnings_quality_accruals_wcintrank_504d_base_v024_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintrank_504d_base_v025_signal,
    f36eq_f36_earnings_quality_accruals_accrualchg_252d_base_v026_signal,
    f36eq_f36_earnings_quality_accruals_accrrevchg_126d_base_v027_signal,
    f36eq_f36_earnings_quality_accruals_cashroachg_252d_base_v028_signal,
    f36eq_f36_earnings_quality_accruals_earnroachg_126d_base_v029_signal,
    f36eq_f36_earnings_quality_accruals_recvcashchg_252d_base_v030_signal,
    f36eq_f36_earnings_quality_accruals_recvintchg_126d_base_v031_signal,
    f36eq_f36_earnings_quality_accruals_recvassetschg_252d_base_v032_signal,
    f36eq_f36_earnings_quality_accruals_wcintchg_126d_base_v033_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintchg_252d_base_v034_signal,
    f36eq_f36_earnings_quality_accruals_accrualemad_126d_base_v035_signal,
    f36eq_f36_earnings_quality_accruals_accrrevemad_252d_base_v036_signal,
    f36eq_f36_earnings_quality_accruals_cashroaemad_126d_base_v037_signal,
    f36eq_f36_earnings_quality_accruals_earnroaemad_252d_base_v038_signal,
    f36eq_f36_earnings_quality_accruals_recvcashemad_252d_base_v039_signal,
    f36eq_f36_earnings_quality_accruals_recvintemad_252d_base_v040_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsemad_126d_base_v041_signal,
    f36eq_f36_earnings_quality_accruals_wcintemad_252d_base_v042_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintemad_126d_base_v043_signal,
    f36eq_f36_earnings_quality_accruals_accrualdisp_252d_base_v044_signal,
    f36eq_f36_earnings_quality_accruals_accrrevdisp_252d_base_v045_signal,
    f36eq_f36_earnings_quality_accruals_cashroadisp_504d_base_v046_signal,
    f36eq_f36_earnings_quality_accruals_earnroadisp_504d_base_v047_signal,
    f36eq_f36_earnings_quality_accruals_convdisp_252d_base_v048_signal,
    f36eq_f36_earnings_quality_accruals_recvcashdisp_504d_base_v049_signal,
    f36eq_f36_earnings_quality_accruals_recvintdisp_252d_base_v050_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsdisp_504d_base_v051_signal,
    f36eq_f36_earnings_quality_accruals_wcintdisp_252d_base_v052_signal,
    f36eq_f36_earnings_quality_accruals_accrualstab_504d_base_v053_signal,
    f36eq_f36_earnings_quality_accruals_accrrevstab_252d_base_v054_signal,
    f36eq_f36_earnings_quality_accruals_cashroastab_252d_base_v055_signal,
    f36eq_f36_earnings_quality_accruals_earnroastab_504d_base_v056_signal,
    f36eq_f36_earnings_quality_accruals_convstab_504d_base_v057_signal,
    f36eq_f36_earnings_quality_accruals_recvcashstab_252d_base_v058_signal,
    f36eq_f36_earnings_quality_accruals_recvintstab_504d_base_v059_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsstab_252d_base_v060_signal,
    f36eq_f36_earnings_quality_accruals_wcintstab_504d_base_v061_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintstab_252d_base_v062_signal,
    f36eq_f36_earnings_quality_accruals_accrualregm_252d_base_v063_signal,
    f36eq_f36_earnings_quality_accruals_accrrevregm_504d_base_v064_signal,
    f36eq_f36_earnings_quality_accruals_cashroaregm_252d_base_v065_signal,
    f36eq_f36_earnings_quality_accruals_earnroaregm_252d_base_v066_signal,
    f36eq_f36_earnings_quality_accruals_convregm_504d_base_v067_signal,
    f36eq_f36_earnings_quality_accruals_recvcashregm_252d_base_v068_signal,
    f36eq_f36_earnings_quality_accruals_recvintregm_252d_base_v069_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsregm_504d_base_v070_signal,
    f36eq_f36_earnings_quality_accruals_wcintregm_252d_base_v071_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintregm_504d_base_v072_signal,
    f36eq_f36_earnings_quality_accruals_recvrevg_63d_base_v073_signal,
    f36eq_f36_earnings_quality_accruals_recvrevg_126d_base_v074_signal,
    f36eq_f36_earnings_quality_accruals_recvrevg_252d_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_EARNINGS_QUALITY_ACCRUALS_REGISTRY_001_075 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500

    ALLOW = {
        "open", "high", "low", "close", "closeadj", "volume",
        "revenue", "revenueusd", "deferredrev", "gp", "grossmargin", "opinc",
        "opex", "sgna", "cor", "rnd", "sbcomp", "ebit", "ebitda", "ebitdamargin",
        "netinc", "netinccmn", "netmargin", "eps", "epsdil", "fcf", "fcfps",
        "ncfo", "ncff", "ncfi", "ncfcommon", "ncfdebt", "ncfbus", "capex",
        "depamor", "sharesbas", "shareswa", "shareswadil", "assets", "assetsc",
        "tangibles", "intangibles", "ppnenet", "investments", "inventory",
        "receivables", "payables", "equity", "retearn", "workingcapital", "debt",
        "debtc", "debtnc", "liabilities", "liabilitiesc", "cashneq", "currentratio",
        "roic", "roe", "roa", "ros", "assetturnover", "invcap", "intexp", "taxexp",
        "ebt", "sps", "bvps", "de", "ncfdiv", "dps", "divyield", "payoutratio",
        "prefdivis", "marketcap", "ev", "evebit", "evebitda", "pe", "pb", "ps",
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

    netinc = _fund(361, base=4.0e7, drift=0.02, vol=0.10, allow_neg=True).rename("netinc")
    ncfo = _fund(362, base=6.0e7, drift=0.025, vol=0.09, allow_neg=True).rename("ncfo")
    assets = _fund(363, base=8.0e8, drift=0.03, vol=0.05).rename("assets")
    receivables = _fund(364, base=1.2e8, drift=0.035, vol=0.08).rename("receivables")
    revenue = _fund(365, base=2.5e8, drift=0.03, vol=0.07).rename("revenue")
    workingcapital = _fund(366, base=9.0e7, drift=0.02, vol=0.12, allow_neg=True).rename("workingcapital")

    cols = {
        "netinc": netinc, "ncfo": ncfo, "assets": assets,
        "receivables": receivables, "revenue": revenue,
        "workingcapital": workingcapital,
    }

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        assert set(meta["inputs"]) <= ALLOW, "%s inputs %s" % (name, meta["inputs"])
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

    print("OK f36_earnings_quality_accruals_base_001_075_claude: %d features pass" % n_features)
