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


# slope (roc=42d) of base accruallvl_126d
def f36eq_f36_earnings_quality_accruals_accruallvl_126d_slope_v001_signal(netinc, ncfo, assets):
    b = (_f36eq_accrual(netinc, ncfo, assets)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base accrrevlvl_63d
def f36eq_f36_earnings_quality_accruals_accrrevlvl_63d_slope_v002_signal(netinc, ncfo, revenue):
    b = ((netinc - ncfo) / revenue.replace(0, np.nan)).rolling(63, min_periods=max(1, 63 // 2)).mean()
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base cashroalvl_126d
def f36eq_f36_earnings_quality_accruals_cashroalvl_126d_slope_v003_signal(ncfo, assets):
    b = (ncfo / assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base earnroalvl_252d
def f36eq_f36_earnings_quality_accruals_earnroalvl_252d_slope_v004_signal(netinc, assets):
    b = (netinc / assets.replace(0, np.nan)).rolling(252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvcashlvl_126d
def f36eq_f36_earnings_quality_accruals_recvcashlvl_126d_slope_v005_signal(receivables, ncfo):
    b = (receivables / ncfo.where(ncfo > 0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base recvintlvl_63d
def f36eq_f36_earnings_quality_accruals_recvintlvl_63d_slope_v006_signal(receivables, revenue):
    b = (_f36eq_recv_intensity(receivables, revenue)).rolling(63, min_periods=max(1, 63 // 2)).mean()
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvassetslvl_126d
def f36eq_f36_earnings_quality_accruals_recvassetslvl_126d_slope_v007_signal(receivables, assets):
    b = (receivables / assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base wcintlvl_126d
def f36eq_f36_earnings_quality_accruals_wcintlvl_126d_slope_v008_signal(workingcapital, assets):
    b = (workingcapital / assets.replace(0, np.nan)).rolling(126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcrevintlvl_252d
def f36eq_f36_earnings_quality_accruals_wcrevintlvl_252d_slope_v009_signal(workingcapital, revenue):
    b = (workingcapital / revenue.replace(0, np.nan)).rolling(252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrualz_252d
def f36eq_f36_earnings_quality_accruals_accrualz_252d_slope_v010_signal(netinc, ncfo, assets):
    b = _z((_f36eq_accrual(netinc, ncfo, assets)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base cashroaz_252d
def f36eq_f36_earnings_quality_accruals_cashroaz_252d_slope_v011_signal(ncfo, assets):
    b = _z((ncfo / assets.replace(0, np.nan)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base earnroaz_378d
def f36eq_f36_earnings_quality_accruals_earnroaz_378d_slope_v012_signal(netinc, assets):
    b = _z((netinc / assets.replace(0, np.nan)), 378)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvcashz_252d
def f36eq_f36_earnings_quality_accruals_recvcashz_252d_slope_v013_signal(receivables, ncfo):
    b = _z((receivables / ncfo.where(ncfo > 0, np.nan)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvintz_252d
def f36eq_f36_earnings_quality_accruals_recvintz_252d_slope_v014_signal(receivables, revenue):
    b = _z((_f36eq_recv_intensity(receivables, revenue)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvassetsz_252d
def f36eq_f36_earnings_quality_accruals_recvassetsz_252d_slope_v015_signal(receivables, assets):
    b = _z((receivables / assets.replace(0, np.nan)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcintz_252d
def f36eq_f36_earnings_quality_accruals_wcintz_252d_slope_v016_signal(workingcapital, assets):
    b = _z((workingcapital / assets.replace(0, np.nan)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base wcrevintz_126d
def f36eq_f36_earnings_quality_accruals_wcrevintz_126d_slope_v017_signal(workingcapital, revenue):
    b = _z((workingcapital / revenue.replace(0, np.nan)), 126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base accrualrank_504d
def f36eq_f36_earnings_quality_accruals_accrualrank_504d_slope_v018_signal(netinc, ncfo, assets):
    b = _rank((_f36eq_accrual(netinc, ncfo, assets)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base cashroarank_504d
def f36eq_f36_earnings_quality_accruals_cashroarank_504d_slope_v019_signal(ncfo, assets):
    b = _rank((ncfo / assets.replace(0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base earnroarank_504d
def f36eq_f36_earnings_quality_accruals_earnroarank_504d_slope_v020_signal(netinc, assets):
    b = _rank((netinc / assets.replace(0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvcashrank_504d
def f36eq_f36_earnings_quality_accruals_recvcashrank_504d_slope_v021_signal(receivables, ncfo):
    b = _rank((receivables / ncfo.where(ncfo > 0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvintrank_504d
def f36eq_f36_earnings_quality_accruals_recvintrank_504d_slope_v022_signal(receivables, revenue):
    b = _rank((_f36eq_recv_intensity(receivables, revenue)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvassetsrank_504d
def f36eq_f36_earnings_quality_accruals_recvassetsrank_504d_slope_v023_signal(receivables, assets):
    b = _rank((receivables / assets.replace(0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base wcintrank_504d
def f36eq_f36_earnings_quality_accruals_wcintrank_504d_slope_v024_signal(workingcapital, assets):
    b = _rank((workingcapital / assets.replace(0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base wcrevintrank_504d
def f36eq_f36_earnings_quality_accruals_wcrevintrank_504d_slope_v025_signal(workingcapital, revenue):
    b = _rank((workingcapital / revenue.replace(0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrualchg_252d
def f36eq_f36_earnings_quality_accruals_accrualchg_252d_slope_v026_signal(netinc, ncfo, assets):
    _a = (_f36eq_accrual(netinc, ncfo, assets))
    b = _a - _a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base accrrevchg_126d
def f36eq_f36_earnings_quality_accruals_accrrevchg_126d_slope_v027_signal(netinc, ncfo, revenue):
    _a = ((netinc - ncfo) / revenue.replace(0, np.nan))
    b = _a - _a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base cashroachg_252d
def f36eq_f36_earnings_quality_accruals_cashroachg_252d_slope_v028_signal(ncfo, assets):
    _a = (ncfo / assets.replace(0, np.nan))
    b = _a - _a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base earnroachg_126d
def f36eq_f36_earnings_quality_accruals_earnroachg_126d_slope_v029_signal(netinc, assets):
    _a = (netinc / assets.replace(0, np.nan))
    b = _a - _a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvcashchg_252d
def f36eq_f36_earnings_quality_accruals_recvcashchg_252d_slope_v030_signal(receivables, ncfo):
    _a = (receivables / ncfo.where(ncfo > 0, np.nan))
    b = _a - _a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvintchg_126d
def f36eq_f36_earnings_quality_accruals_recvintchg_126d_slope_v031_signal(receivables, revenue):
    _a = (_f36eq_recv_intensity(receivables, revenue))
    b = _a - _a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvassetschg_252d
def f36eq_f36_earnings_quality_accruals_recvassetschg_252d_slope_v032_signal(receivables, assets):
    _a = (receivables / assets.replace(0, np.nan))
    b = _a - _a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base wcintchg_126d
def f36eq_f36_earnings_quality_accruals_wcintchg_126d_slope_v033_signal(workingcapital, assets):
    _a = (workingcapital / assets.replace(0, np.nan))
    b = _a - _a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcrevintchg_252d
def f36eq_f36_earnings_quality_accruals_wcrevintchg_252d_slope_v034_signal(workingcapital, revenue):
    _a = (workingcapital / revenue.replace(0, np.nan))
    b = _a - _a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base accrualemad_126d
def f36eq_f36_earnings_quality_accruals_accrualemad_126d_slope_v035_signal(netinc, ncfo, assets):
    _a = (_f36eq_accrual(netinc, ncfo, assets))
    b = _a - _a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrrevemad_252d
def f36eq_f36_earnings_quality_accruals_accrrevemad_252d_slope_v036_signal(netinc, ncfo, revenue):
    _a = ((netinc - ncfo) / revenue.replace(0, np.nan))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base cashroaemad_126d
def f36eq_f36_earnings_quality_accruals_cashroaemad_126d_slope_v037_signal(ncfo, assets):
    _a = (ncfo / assets.replace(0, np.nan))
    b = _a - _a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base earnroaemad_252d
def f36eq_f36_earnings_quality_accruals_earnroaemad_252d_slope_v038_signal(netinc, assets):
    _a = (netinc / assets.replace(0, np.nan))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvcashemad_252d
def f36eq_f36_earnings_quality_accruals_recvcashemad_252d_slope_v039_signal(receivables, ncfo):
    _a = (receivables / ncfo.where(ncfo > 0, np.nan))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvintemad_252d
def f36eq_f36_earnings_quality_accruals_recvintemad_252d_slope_v040_signal(receivables, revenue):
    _a = (_f36eq_recv_intensity(receivables, revenue))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvassetsemad_126d
def f36eq_f36_earnings_quality_accruals_recvassetsemad_126d_slope_v041_signal(receivables, assets):
    _a = (receivables / assets.replace(0, np.nan))
    b = _a - _a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcintemad_252d
def f36eq_f36_earnings_quality_accruals_wcintemad_252d_slope_v042_signal(workingcapital, assets):
    _a = (workingcapital / assets.replace(0, np.nan))
    b = _a - _a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base wcrevintemad_126d
def f36eq_f36_earnings_quality_accruals_wcrevintemad_126d_slope_v043_signal(workingcapital, revenue):
    _a = (workingcapital / revenue.replace(0, np.nan))
    b = _a - _a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrualdisp_252d
def f36eq_f36_earnings_quality_accruals_accrualdisp_252d_slope_v044_signal(netinc, ncfo, assets):
    b = _std((_f36eq_accrual(netinc, ncfo, assets)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrrevdisp_252d
def f36eq_f36_earnings_quality_accruals_accrrevdisp_252d_slope_v045_signal(netinc, ncfo, revenue):
    b = _std(((netinc - ncfo) / revenue.replace(0, np.nan)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base cashroadisp_504d
def f36eq_f36_earnings_quality_accruals_cashroadisp_504d_slope_v046_signal(ncfo, assets):
    b = _std((ncfo / assets.replace(0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base earnroadisp_504d
def f36eq_f36_earnings_quality_accruals_earnroadisp_504d_slope_v047_signal(netinc, assets):
    b = _std((netinc / assets.replace(0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base convdisp_252d
def f36eq_f36_earnings_quality_accruals_convdisp_252d_slope_v048_signal(ncfo, netinc):
    b = _std((_f36eq_conv(ncfo, netinc)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvcashdisp_504d
def f36eq_f36_earnings_quality_accruals_recvcashdisp_504d_slope_v049_signal(receivables, ncfo):
    b = _std((receivables / ncfo.where(ncfo > 0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvintdisp_252d
def f36eq_f36_earnings_quality_accruals_recvintdisp_252d_slope_v050_signal(receivables, revenue):
    b = _std((_f36eq_recv_intensity(receivables, revenue)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvassetsdisp_504d
def f36eq_f36_earnings_quality_accruals_recvassetsdisp_504d_slope_v051_signal(receivables, assets):
    b = _std((receivables / assets.replace(0, np.nan)), 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcintdisp_252d
def f36eq_f36_earnings_quality_accruals_wcintdisp_252d_slope_v052_signal(workingcapital, assets):
    b = _std((workingcapital / assets.replace(0, np.nan)), 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base accrualstab_504d
def f36eq_f36_earnings_quality_accruals_accrualstab_504d_slope_v053_signal(netinc, ncfo, assets):
    _a = (_f36eq_accrual(netinc, ncfo, assets))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrrevstab_252d
def f36eq_f36_earnings_quality_accruals_accrrevstab_252d_slope_v054_signal(netinc, ncfo, revenue):
    _a = ((netinc - ncfo) / revenue.replace(0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base cashroastab_252d
def f36eq_f36_earnings_quality_accruals_cashroastab_252d_slope_v055_signal(ncfo, assets):
    _a = (ncfo / assets.replace(0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base earnroastab_504d
def f36eq_f36_earnings_quality_accruals_earnroastab_504d_slope_v056_signal(netinc, assets):
    _a = (netinc / assets.replace(0, np.nan))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base convstab_504d
def f36eq_f36_earnings_quality_accruals_convstab_504d_slope_v057_signal(ncfo, netinc):
    _a = (_f36eq_conv(ncfo, netinc))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvcashstab_252d
def f36eq_f36_earnings_quality_accruals_recvcashstab_252d_slope_v058_signal(receivables, ncfo):
    _a = (receivables / ncfo.where(ncfo > 0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvintstab_504d
def f36eq_f36_earnings_quality_accruals_recvintstab_504d_slope_v059_signal(receivables, revenue):
    _a = (_f36eq_recv_intensity(receivables, revenue))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvassetsstab_252d
def f36eq_f36_earnings_quality_accruals_recvassetsstab_252d_slope_v060_signal(receivables, assets):
    _a = (receivables / assets.replace(0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base wcintstab_504d
def f36eq_f36_earnings_quality_accruals_wcintstab_504d_slope_v061_signal(workingcapital, assets):
    _a = (workingcapital / assets.replace(0, np.nan))
    _m = _a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _sd = _a.rolling(504, min_periods=max(1, 504 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcrevintstab_252d
def f36eq_f36_earnings_quality_accruals_wcrevintstab_252d_slope_v062_signal(workingcapital, revenue):
    _a = (workingcapital / revenue.replace(0, np.nan))
    _m = _a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _sd = _a.rolling(252, min_periods=max(1, 252 // 2)).std()
    b = _m / _sd.replace(0, np.nan)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrualregm_252d
def f36eq_f36_earnings_quality_accruals_accrualregm_252d_slope_v063_signal(netinc, ncfo, assets):
    _a = (_f36eq_accrual(netinc, ncfo, assets))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base accrrevregm_504d
def f36eq_f36_earnings_quality_accruals_accrrevregm_504d_slope_v064_signal(netinc, ncfo, revenue):
    _a = ((netinc - ncfo) / revenue.replace(0, np.nan))
    _med = _a.rolling(504, min_periods=max(1, 504 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base cashroaregm_252d
def f36eq_f36_earnings_quality_accruals_cashroaregm_252d_slope_v065_signal(ncfo, assets):
    _a = (ncfo / assets.replace(0, np.nan))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base earnroaregm_252d
def f36eq_f36_earnings_quality_accruals_earnroaregm_252d_slope_v066_signal(netinc, assets):
    _a = (netinc / assets.replace(0, np.nan))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base convregm_504d
def f36eq_f36_earnings_quality_accruals_convregm_504d_slope_v067_signal(ncfo, netinc):
    _a = (_f36eq_conv(ncfo, netinc))
    _med = _a.rolling(504, min_periods=max(1, 504 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvcashregm_252d
def f36eq_f36_earnings_quality_accruals_recvcashregm_252d_slope_v068_signal(receivables, ncfo):
    _a = (receivables / ncfo.where(ncfo > 0, np.nan))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvintregm_252d
def f36eq_f36_earnings_quality_accruals_recvintregm_252d_slope_v069_signal(receivables, revenue):
    _a = (_f36eq_recv_intensity(receivables, revenue))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvassetsregm_504d
def f36eq_f36_earnings_quality_accruals_recvassetsregm_504d_slope_v070_signal(receivables, assets):
    _a = (receivables / assets.replace(0, np.nan))
    _med = _a.rolling(504, min_periods=max(1, 504 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcintregm_252d
def f36eq_f36_earnings_quality_accruals_wcintregm_252d_slope_v071_signal(workingcapital, assets):
    _a = (workingcapital / assets.replace(0, np.nan))
    _med = _a.rolling(252, min_periods=max(1, 252 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base wcrevintregm_504d
def f36eq_f36_earnings_quality_accruals_wcrevintregm_504d_slope_v072_signal(workingcapital, revenue):
    _a = (workingcapital / revenue.replace(0, np.nan))
    _med = _a.rolling(504, min_periods=max(1, 504 // 2)).median()
    _fl = (_a > _med).astype(float)
    b = _fl.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base recvrevg_63d
def f36eq_f36_earnings_quality_accruals_recvrevg_63d_slope_v073_signal(receivables, revenue):
    rg = _f36eq_growth(receivables, 63)
    vg = _f36eq_growth(revenue, 63)
    b = rg - vg
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvrevg_126d
def f36eq_f36_earnings_quality_accruals_recvrevg_126d_slope_v074_signal(receivables, revenue):
    rg = _f36eq_growth(receivables, 126)
    vg = _f36eq_growth(revenue, 126)
    b = rg - vg
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvrevg_252d
def f36eq_f36_earnings_quality_accruals_recvrevg_252d_slope_v075_signal(receivables, revenue):
    rg = _f36eq_growth(receivables, 252)
    vg = _f36eq_growth(revenue, 252)
    b = rg - vg
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvrevg_378d
def f36eq_f36_earnings_quality_accruals_recvrevg_378d_slope_v076_signal(receivables, revenue):
    rg = _f36eq_growth(receivables, 378)
    vg = _f36eq_growth(revenue, 378)
    b = rg - vg
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base revcashdiv_63d
def f36eq_f36_earnings_quality_accruals_revcashdiv_63d_slope_v077_signal(revenue, ncfo):
    rg = _f36eq_growth(revenue, 63)
    cg = _f36eq_growth(ncfo, 63)
    b = rg - cg
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base revcashdiv_126d
def f36eq_f36_earnings_quality_accruals_revcashdiv_126d_slope_v078_signal(revenue, ncfo):
    rg = _f36eq_growth(revenue, 126)
    cg = _f36eq_growth(ncfo, 126)
    b = rg - cg
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base revcashdiv_252d
def f36eq_f36_earnings_quality_accruals_revcashdiv_252d_slope_v079_signal(revenue, ncfo):
    rg = _f36eq_growth(revenue, 252)
    cg = _f36eq_growth(ncfo, 252)
    b = rg - cg
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base revcashdiv_378d
def f36eq_f36_earnings_quality_accruals_revcashdiv_378d_slope_v080_signal(revenue, ncfo):
    rg = _f36eq_growth(revenue, 378)
    cg = _f36eq_growth(ncfo, 378)
    b = rg - cg
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base recvcashdiv_63d
def f36eq_f36_earnings_quality_accruals_recvcashdiv_63d_slope_v081_signal(receivables, ncfo):
    rg = _f36eq_growth(receivables, 63)
    cg = _f36eq_growth(ncfo, 63)
    b = rg - cg
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvcashdiv_126d
def f36eq_f36_earnings_quality_accruals_recvcashdiv_126d_slope_v082_signal(receivables, ncfo):
    rg = _f36eq_growth(receivables, 126)
    cg = _f36eq_growth(ncfo, 126)
    b = rg - cg
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvcashdiv_378d
def f36eq_f36_earnings_quality_accruals_recvcashdiv_378d_slope_v083_signal(receivables, ncfo):
    rg = _f36eq_growth(receivables, 378)
    cg = _f36eq_growth(ncfo, 378)
    b = rg - cg
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base recvwcdiv_63d
def f36eq_f36_earnings_quality_accruals_recvwcdiv_63d_slope_v084_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    b = (ra - ra.shift(63)) - (wa - wa.shift(63))
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvwcdiv_126d
def f36eq_f36_earnings_quality_accruals_recvwcdiv_126d_slope_v085_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    b = (ra - ra.shift(126)) - (wa - wa.shift(126))
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvwcdiv_252d
def f36eq_f36_earnings_quality_accruals_recvwcdiv_252d_slope_v086_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    b = (ra - ra.shift(252)) - (wa - wa.shift(252))
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvwcdiv_378d
def f36eq_f36_earnings_quality_accruals_recvwcdiv_378d_slope_v087_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    b = (ra - ra.shift(378)) - (wa - wa.shift(378))
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=10d) of base dwc_21d
def f36eq_f36_earnings_quality_accruals_dwc_21d_slope_v088_signal(workingcapital, assets):
    b = _f36eq_dwc(workingcapital, 21, assets)
    _d = (b - b.shift(10)) / 10.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base dwc_63d
def f36eq_f36_earnings_quality_accruals_dwc_63d_slope_v089_signal(workingcapital, assets):
    b = _f36eq_dwc(workingcapital, 63, assets)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base dwc_504d
def f36eq_f36_earnings_quality_accruals_dwc_504d_slope_v090_signal(workingcapital, assets):
    b = _f36eq_dwc(workingcapital, 504, assets)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base dwcz_252d
def f36eq_f36_earnings_quality_accruals_dwcz_252d_slope_v091_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = _z(a, 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base dwcrank_504d
def f36eq_f36_earnings_quality_accruals_dwcrank_504d_slope_v092_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = _rank(a, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base dwcsm_252d
def f36eq_f36_earnings_quality_accruals_dwcsm_252d_slope_v093_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = np.sign(a) * a.abs().pow(0.5)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvbuild_126d
def f36eq_f36_earnings_quality_accruals_recvbuild_126d_slope_v094_signal(receivables, assets):
    b = (receivables - receivables.shift(126)) / assets.replace(0, np.nan)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcintchg_252d
def f36eq_f36_earnings_quality_accruals_wcintchg_252d_slope_v095_signal(workingcapital, assets):
    a = workingcapital / assets.replace(0, np.nan)
    b = a - a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvassetschg_126d
def f36eq_f36_earnings_quality_accruals_recvassetschg_126d_slope_v096_signal(receivables, assets):
    a = receivables / assets.replace(0, np.nan)
    b = a - a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base convgap_126d
def f36eq_f36_earnings_quality_accruals_convgap_126d_slope_v097_signal(ncfo, netinc):
    a = _f36eq_conv(ncfo, netinc)
    sm = a.rolling(126, min_periods=max(1, 126 // 2)).mean()
    b = sm - a.ewm(span=126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base convgap_252d
def f36eq_f36_earnings_quality_accruals_convgap_252d_slope_v098_signal(ncfo, netinc):
    a = _f36eq_conv(ncfo, netinc)
    sm = a.rolling(252, min_periods=max(1, 252 // 2)).mean()
    b = sm - a.ewm(span=252, min_periods=max(1, 252 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrtanh_252d
def f36eq_f36_earnings_quality_accruals_accrtanh_252d_slope_v099_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets).rolling(252, min_periods=126).mean()
    b = np.tanh(10.0 * a)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base eqscore_252d
def f36eq_f36_earnings_quality_accruals_eqscore_252d_slope_v100_signal(ncfo, assets, netinc):
    cr = (ncfo / assets.replace(0, np.nan))
    ac = _f36eq_accrual(netinc, ncfo, assets)
    b = _rank(cr, 252) - _rank(ac, 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrxrecv_252d
def f36eq_f36_earnings_quality_accruals_accrxrecv_252d_slope_v101_signal(netinc, ncfo, assets, receivables, revenue):
    acc = _f36eq_accrual(netinc, ncfo, assets).rolling(252, min_periods=126).mean()
    ri = _f36eq_recv_intensity(receivables, revenue)
    rid = ri - ri.shift(252)
    b = acc * rid
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrgrowth_252d
def f36eq_f36_earnings_quality_accruals_accrgrowth_252d_slope_v102_signal(revenue, ncfo, netinc):
    vg = _f36eq_growth(revenue, 252)
    cv = _f36eq_conv(ncfo, netinc).rolling(252, min_periods=126).mean()
    b = vg - 0.2 * cv
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base growthcash_252d
def f36eq_f36_earnings_quality_accruals_growthcash_252d_slope_v103_signal(revenue, ncfo, assets):
    vg = _f36eq_growth(revenue, 252)
    cr = (ncfo / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = vg * (-(cr - cr.shift(252)))
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base opaccr_252d
def f36eq_f36_earnings_quality_accruals_opaccr_252d_slope_v104_signal(workingcapital, revenue, receivables):
    dwc = (workingcapital - workingcapital.shift(252)) / revenue.replace(0, np.nan)
    ri = _f36eq_recv_intensity(receivables, revenue)
    b = dwc + (ri - ri.shift(252))
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accryoy_252d
def f36eq_f36_earnings_quality_accruals_accryoy_252d_slope_v105_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    sm = a.rolling(63, min_periods=21).mean()
    b = sm - sm.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrrev2_252d
def f36eq_f36_earnings_quality_accruals_accrrev2_252d_slope_v106_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets).rolling(63, min_periods=21).mean()
    b = -a * a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvwcz_252d
def f36eq_f36_earnings_quality_accruals_recvwcz_252d_slope_v107_signal(receivables, workingcapital, assets):
    ra = (receivables / assets.replace(0, np.nan))
    wa = (workingcapital / assets.replace(0, np.nan))
    a = (ra - ra.shift(63)) - (wa - wa.shift(63))
    b = _z(a, 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base accrual2_63d
def f36eq_f36_earnings_quality_accruals_accrual2_63d_slope_v108_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    b = a.rolling(63, min_periods=max(1, 63 // 2)).mean()
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base accrual2_504d
def f36eq_f36_earnings_quality_accruals_accrual2_504d_slope_v109_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    b = a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base convchg_63d
def f36eq_f36_earnings_quality_accruals_convchg_63d_slope_v110_signal(ncfo, netinc):
    a = _f36eq_conv(ncfo, netinc).rolling(21, min_periods=10).mean()
    b = a - a.shift(63)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base convchg_504d
def f36eq_f36_earnings_quality_accruals_convchg_504d_slope_v111_signal(ncfo, netinc):
    a = _f36eq_conv(ncfo, netinc).rolling(21, min_periods=10).mean()
    b = a - a.shift(504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base recvbuildz_63d
def f36eq_f36_earnings_quality_accruals_recvbuildz_63d_slope_v112_signal(receivables, assets):
    a = (receivables - receivables.shift(63)) / assets.replace(0, np.nan)
    b = _z(a, 63)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvbuildz_504d
def f36eq_f36_earnings_quality_accruals_recvbuildz_504d_slope_v113_signal(receivables, assets):
    a = (receivables - receivables.shift(63)) / assets.replace(0, np.nan)
    b = _z(a, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base wcaccrz_126d
def f36eq_f36_earnings_quality_accruals_wcaccrz_126d_slope_v114_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = _z(a, 126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base accrrevz_126d
def f36eq_f36_earnings_quality_accruals_accrrevz_126d_slope_v115_signal(netinc, ncfo, revenue):
    a = (netinc - ncfo) / revenue.replace(0, np.nan)
    b = _z(a, 126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvgrowthlvl_126d
def f36eq_f36_earnings_quality_accruals_recvgrowthlvl_126d_slope_v116_signal(receivables, revenue):
    a = _f36eq_growth(receivables, 126) - _f36eq_growth(revenue, 126)
    b = a.rolling(126, min_periods=max(1, 126 // 2)).mean()
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base recvgrowthlvl_504d
def f36eq_f36_earnings_quality_accruals_recvgrowthlvl_504d_slope_v117_signal(receivables, revenue):
    a = _f36eq_growth(receivables, 126) - _f36eq_growth(revenue, 126)
    b = a.rolling(504, min_periods=max(1, 504 // 2)).mean()
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base cashroachg_126d
def f36eq_f36_earnings_quality_accruals_cashroachg_126d_slope_v118_signal(ncfo, assets):
    a = (ncfo / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base cashroachg_252d
def f36eq_f36_earnings_quality_accruals_cashroachg_252d_slope_v119_signal(ncfo, assets):
    a = (ncfo / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base earnroachg_126d
def f36eq_f36_earnings_quality_accruals_earnroachg_126d_slope_v120_signal(netinc, assets):
    a = (netinc / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base earnroachg_252d
def f36eq_f36_earnings_quality_accruals_earnroachg_252d_slope_v121_signal(netinc, assets):
    a = (netinc / assets.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base netaccrtanh_252d
def f36eq_f36_earnings_quality_accruals_netaccrtanh_252d_slope_v122_signal(netinc, ncfo, revenue):
    a = ((netinc - ncfo) / revenue.replace(0, np.nan)).rolling(252, min_periods=126).mean()
    b = np.tanh(8.0 * a)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base accrualx_189d
def f36eq_f36_earnings_quality_accruals_accrualx_189d_slope_v123_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    b = a.rolling(189, min_periods=max(1, 189 // 2)).mean()
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base accrualx_378d
def f36eq_f36_earnings_quality_accruals_accrualx_378d_slope_v124_signal(netinc, ncfo, assets):
    a = _f36eq_accrual(netinc, ncfo, assets)
    b = a.rolling(378, min_periods=max(1, 378 // 2)).mean()
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base cashroaz_126d
def f36eq_f36_earnings_quality_accruals_cashroaz_126d_slope_v125_signal(ncfo, assets):
    a = ncfo / assets.replace(0, np.nan)
    b = _z(a, 126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base cashroaz_504d
def f36eq_f36_earnings_quality_accruals_cashroaz_504d_slope_v126_signal(ncfo, assets):
    a = ncfo / assets.replace(0, np.nan)
    b = _z(a, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base wcaccrchg_126d
def f36eq_f36_earnings_quality_accruals_wcaccrchg_126d_slope_v127_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = a - a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base wcaccrchg_252d
def f36eq_f36_earnings_quality_accruals_wcaccrchg_252d_slope_v128_signal(workingcapital, assets):
    a = _f36eq_dwc(workingcapital, 63, assets)
    b = a - a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base recvcashchg_126d
def f36eq_f36_earnings_quality_accruals_recvcashchg_126d_slope_v129_signal(receivables, ncfo):
    a = (receivables / ncfo.where(ncfo > 0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(126)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base recvcashchg_252d
def f36eq_f36_earnings_quality_accruals_recvcashchg_252d_slope_v130_signal(receivables, ncfo):
    a = (receivables / ncfo.where(ncfo > 0, np.nan)).rolling(63, min_periods=21).mean()
    b = a - a.shift(252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base revcashdivz_252d
def f36eq_f36_earnings_quality_accruals_revcashdivz_252d_slope_v131_signal(revenue, ncfo):
    a = _f36eq_growth(revenue, 126) - _f36eq_growth(ncfo, 126)
    b = _z(a, 252)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base revcashdivz_504d
def f36eq_f36_earnings_quality_accruals_revcashdivz_504d_slope_v132_signal(revenue, ncfo):
    a = _f36eq_growth(revenue, 126) - _f36eq_growth(ncfo, 126)
    b = _z(a, 504)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base gd_recv_rev_42d
def f36eq_f36_earnings_quality_accruals_gd_recv_rev_42d_slope_v133_signal(receivables, revenue):
    b = _f36eq_growth(receivables, 42) - _f36eq_growth(revenue, 42)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base gd_recv_rev_84d
def f36eq_f36_earnings_quality_accruals_gd_recv_rev_84d_slope_v134_signal(receivables, revenue):
    b = _f36eq_growth(receivables, 84) - _f36eq_growth(revenue, 84)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base gd_recv_rev_168d
def f36eq_f36_earnings_quality_accruals_gd_recv_rev_168d_slope_v135_signal(receivables, revenue):
    b = _f36eq_growth(receivables, 168) - _f36eq_growth(revenue, 168)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base gd_recv_cash_42d
def f36eq_f36_earnings_quality_accruals_gd_recv_cash_42d_slope_v136_signal(receivables, ncfo):
    b = _f36eq_growth(receivables, 42) - _f36eq_growth(ncfo, 42)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base gd_recv_cash_84d
def f36eq_f36_earnings_quality_accruals_gd_recv_cash_84d_slope_v137_signal(receivables, ncfo):
    b = _f36eq_growth(receivables, 84) - _f36eq_growth(ncfo, 84)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base gd_recv_cash_336d
def f36eq_f36_earnings_quality_accruals_gd_recv_cash_336d_slope_v138_signal(receivables, ncfo):
    b = _f36eq_growth(receivables, 336) - _f36eq_growth(ncfo, 336)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base gd_rev_cash_168d
def f36eq_f36_earnings_quality_accruals_gd_rev_cash_168d_slope_v139_signal(revenue, ncfo):
    b = _f36eq_growth(revenue, 168) - _f36eq_growth(ncfo, 168)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base gd_rev_cash_336d
def f36eq_f36_earnings_quality_accruals_gd_rev_cash_336d_slope_v140_signal(revenue, ncfo):
    b = _f36eq_growth(revenue, 336) - _f36eq_growth(ncfo, 336)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base gd_recv_ni_42d
def f36eq_f36_earnings_quality_accruals_gd_recv_ni_42d_slope_v141_signal(receivables, netinc):
    b = _f36eq_growth(receivables, 42) - _f36eq_growth(netinc, 42)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base gd_recv_ni_84d
def f36eq_f36_earnings_quality_accruals_gd_recv_ni_84d_slope_v142_signal(receivables, netinc):
    b = _f36eq_growth(receivables, 84) - _f36eq_growth(netinc, 84)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base gd_recv_ni_168d
def f36eq_f36_earnings_quality_accruals_gd_recv_ni_168d_slope_v143_signal(receivables, netinc):
    b = _f36eq_growth(receivables, 168) - _f36eq_growth(netinc, 168)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base gd_recv_ni_336d
def f36eq_f36_earnings_quality_accruals_gd_recv_ni_336d_slope_v144_signal(receivables, netinc):
    b = _f36eq_growth(receivables, 336) - _f36eq_growth(netinc, 336)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base gd_wc_rev_42d
def f36eq_f36_earnings_quality_accruals_gd_wc_rev_42d_slope_v145_signal(workingcapital, revenue):
    b = _f36eq_growth(workingcapital, 42) - _f36eq_growth(revenue, 42)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base gd_wc_rev_84d
def f36eq_f36_earnings_quality_accruals_gd_wc_rev_84d_slope_v146_signal(workingcapital, revenue):
    b = _f36eq_growth(workingcapital, 84) - _f36eq_growth(revenue, 84)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=63d) of base gd_wc_rev_168d
def f36eq_f36_earnings_quality_accruals_gd_wc_rev_168d_slope_v147_signal(workingcapital, revenue):
    b = _f36eq_growth(workingcapital, 168) - _f36eq_growth(revenue, 168)
    _d = (b - b.shift(63)) / 63.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=126d) of base gd_wc_rev_336d
def f36eq_f36_earnings_quality_accruals_gd_wc_rev_336d_slope_v148_signal(workingcapital, revenue):
    b = _f36eq_growth(workingcapital, 336) - _f36eq_growth(revenue, 336)
    _d = (b - b.shift(126)) / 126.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=21d) of base gd_wc_cash_42d
def f36eq_f36_earnings_quality_accruals_gd_wc_cash_42d_slope_v149_signal(workingcapital, ncfo):
    b = _f36eq_growth(workingcapital, 42) - _f36eq_growth(ncfo, 42)
    _d = (b - b.shift(21)) / 21.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


# slope (roc=42d) of base gd_wc_cash_84d
def f36eq_f36_earnings_quality_accruals_gd_wc_cash_84d_slope_v150_signal(workingcapital, ncfo):
    b = _f36eq_growth(workingcapital, 84) - _f36eq_growth(ncfo, 84)
    _d = (b - b.shift(42)) / 42.0
    result = _d
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f36eq_f36_earnings_quality_accruals_accruallvl_126d_slope_v001_signal,
    f36eq_f36_earnings_quality_accruals_accrrevlvl_63d_slope_v002_signal,
    f36eq_f36_earnings_quality_accruals_cashroalvl_126d_slope_v003_signal,
    f36eq_f36_earnings_quality_accruals_earnroalvl_252d_slope_v004_signal,
    f36eq_f36_earnings_quality_accruals_recvcashlvl_126d_slope_v005_signal,
    f36eq_f36_earnings_quality_accruals_recvintlvl_63d_slope_v006_signal,
    f36eq_f36_earnings_quality_accruals_recvassetslvl_126d_slope_v007_signal,
    f36eq_f36_earnings_quality_accruals_wcintlvl_126d_slope_v008_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintlvl_252d_slope_v009_signal,
    f36eq_f36_earnings_quality_accruals_accrualz_252d_slope_v010_signal,
    f36eq_f36_earnings_quality_accruals_cashroaz_252d_slope_v011_signal,
    f36eq_f36_earnings_quality_accruals_earnroaz_378d_slope_v012_signal,
    f36eq_f36_earnings_quality_accruals_recvcashz_252d_slope_v013_signal,
    f36eq_f36_earnings_quality_accruals_recvintz_252d_slope_v014_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsz_252d_slope_v015_signal,
    f36eq_f36_earnings_quality_accruals_wcintz_252d_slope_v016_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintz_126d_slope_v017_signal,
    f36eq_f36_earnings_quality_accruals_accrualrank_504d_slope_v018_signal,
    f36eq_f36_earnings_quality_accruals_cashroarank_504d_slope_v019_signal,
    f36eq_f36_earnings_quality_accruals_earnroarank_504d_slope_v020_signal,
    f36eq_f36_earnings_quality_accruals_recvcashrank_504d_slope_v021_signal,
    f36eq_f36_earnings_quality_accruals_recvintrank_504d_slope_v022_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsrank_504d_slope_v023_signal,
    f36eq_f36_earnings_quality_accruals_wcintrank_504d_slope_v024_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintrank_504d_slope_v025_signal,
    f36eq_f36_earnings_quality_accruals_accrualchg_252d_slope_v026_signal,
    f36eq_f36_earnings_quality_accruals_accrrevchg_126d_slope_v027_signal,
    f36eq_f36_earnings_quality_accruals_cashroachg_252d_slope_v028_signal,
    f36eq_f36_earnings_quality_accruals_earnroachg_126d_slope_v029_signal,
    f36eq_f36_earnings_quality_accruals_recvcashchg_252d_slope_v030_signal,
    f36eq_f36_earnings_quality_accruals_recvintchg_126d_slope_v031_signal,
    f36eq_f36_earnings_quality_accruals_recvassetschg_252d_slope_v032_signal,
    f36eq_f36_earnings_quality_accruals_wcintchg_126d_slope_v033_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintchg_252d_slope_v034_signal,
    f36eq_f36_earnings_quality_accruals_accrualemad_126d_slope_v035_signal,
    f36eq_f36_earnings_quality_accruals_accrrevemad_252d_slope_v036_signal,
    f36eq_f36_earnings_quality_accruals_cashroaemad_126d_slope_v037_signal,
    f36eq_f36_earnings_quality_accruals_earnroaemad_252d_slope_v038_signal,
    f36eq_f36_earnings_quality_accruals_recvcashemad_252d_slope_v039_signal,
    f36eq_f36_earnings_quality_accruals_recvintemad_252d_slope_v040_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsemad_126d_slope_v041_signal,
    f36eq_f36_earnings_quality_accruals_wcintemad_252d_slope_v042_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintemad_126d_slope_v043_signal,
    f36eq_f36_earnings_quality_accruals_accrualdisp_252d_slope_v044_signal,
    f36eq_f36_earnings_quality_accruals_accrrevdisp_252d_slope_v045_signal,
    f36eq_f36_earnings_quality_accruals_cashroadisp_504d_slope_v046_signal,
    f36eq_f36_earnings_quality_accruals_earnroadisp_504d_slope_v047_signal,
    f36eq_f36_earnings_quality_accruals_convdisp_252d_slope_v048_signal,
    f36eq_f36_earnings_quality_accruals_recvcashdisp_504d_slope_v049_signal,
    f36eq_f36_earnings_quality_accruals_recvintdisp_252d_slope_v050_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsdisp_504d_slope_v051_signal,
    f36eq_f36_earnings_quality_accruals_wcintdisp_252d_slope_v052_signal,
    f36eq_f36_earnings_quality_accruals_accrualstab_504d_slope_v053_signal,
    f36eq_f36_earnings_quality_accruals_accrrevstab_252d_slope_v054_signal,
    f36eq_f36_earnings_quality_accruals_cashroastab_252d_slope_v055_signal,
    f36eq_f36_earnings_quality_accruals_earnroastab_504d_slope_v056_signal,
    f36eq_f36_earnings_quality_accruals_convstab_504d_slope_v057_signal,
    f36eq_f36_earnings_quality_accruals_recvcashstab_252d_slope_v058_signal,
    f36eq_f36_earnings_quality_accruals_recvintstab_504d_slope_v059_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsstab_252d_slope_v060_signal,
    f36eq_f36_earnings_quality_accruals_wcintstab_504d_slope_v061_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintstab_252d_slope_v062_signal,
    f36eq_f36_earnings_quality_accruals_accrualregm_252d_slope_v063_signal,
    f36eq_f36_earnings_quality_accruals_accrrevregm_504d_slope_v064_signal,
    f36eq_f36_earnings_quality_accruals_cashroaregm_252d_slope_v065_signal,
    f36eq_f36_earnings_quality_accruals_earnroaregm_252d_slope_v066_signal,
    f36eq_f36_earnings_quality_accruals_convregm_504d_slope_v067_signal,
    f36eq_f36_earnings_quality_accruals_recvcashregm_252d_slope_v068_signal,
    f36eq_f36_earnings_quality_accruals_recvintregm_252d_slope_v069_signal,
    f36eq_f36_earnings_quality_accruals_recvassetsregm_504d_slope_v070_signal,
    f36eq_f36_earnings_quality_accruals_wcintregm_252d_slope_v071_signal,
    f36eq_f36_earnings_quality_accruals_wcrevintregm_504d_slope_v072_signal,
    f36eq_f36_earnings_quality_accruals_recvrevg_63d_slope_v073_signal,
    f36eq_f36_earnings_quality_accruals_recvrevg_126d_slope_v074_signal,
    f36eq_f36_earnings_quality_accruals_recvrevg_252d_slope_v075_signal,
    f36eq_f36_earnings_quality_accruals_recvrevg_378d_slope_v076_signal,
    f36eq_f36_earnings_quality_accruals_revcashdiv_63d_slope_v077_signal,
    f36eq_f36_earnings_quality_accruals_revcashdiv_126d_slope_v078_signal,
    f36eq_f36_earnings_quality_accruals_revcashdiv_252d_slope_v079_signal,
    f36eq_f36_earnings_quality_accruals_revcashdiv_378d_slope_v080_signal,
    f36eq_f36_earnings_quality_accruals_recvcashdiv_63d_slope_v081_signal,
    f36eq_f36_earnings_quality_accruals_recvcashdiv_126d_slope_v082_signal,
    f36eq_f36_earnings_quality_accruals_recvcashdiv_378d_slope_v083_signal,
    f36eq_f36_earnings_quality_accruals_recvwcdiv_63d_slope_v084_signal,
    f36eq_f36_earnings_quality_accruals_recvwcdiv_126d_slope_v085_signal,
    f36eq_f36_earnings_quality_accruals_recvwcdiv_252d_slope_v086_signal,
    f36eq_f36_earnings_quality_accruals_recvwcdiv_378d_slope_v087_signal,
    f36eq_f36_earnings_quality_accruals_dwc_21d_slope_v088_signal,
    f36eq_f36_earnings_quality_accruals_dwc_63d_slope_v089_signal,
    f36eq_f36_earnings_quality_accruals_dwc_504d_slope_v090_signal,
    f36eq_f36_earnings_quality_accruals_dwcz_252d_slope_v091_signal,
    f36eq_f36_earnings_quality_accruals_dwcrank_504d_slope_v092_signal,
    f36eq_f36_earnings_quality_accruals_dwcsm_252d_slope_v093_signal,
    f36eq_f36_earnings_quality_accruals_recvbuild_126d_slope_v094_signal,
    f36eq_f36_earnings_quality_accruals_wcintchg_252d_slope_v095_signal,
    f36eq_f36_earnings_quality_accruals_recvassetschg_126d_slope_v096_signal,
    f36eq_f36_earnings_quality_accruals_convgap_126d_slope_v097_signal,
    f36eq_f36_earnings_quality_accruals_convgap_252d_slope_v098_signal,
    f36eq_f36_earnings_quality_accruals_accrtanh_252d_slope_v099_signal,
    f36eq_f36_earnings_quality_accruals_eqscore_252d_slope_v100_signal,
    f36eq_f36_earnings_quality_accruals_accrxrecv_252d_slope_v101_signal,
    f36eq_f36_earnings_quality_accruals_accrgrowth_252d_slope_v102_signal,
    f36eq_f36_earnings_quality_accruals_growthcash_252d_slope_v103_signal,
    f36eq_f36_earnings_quality_accruals_opaccr_252d_slope_v104_signal,
    f36eq_f36_earnings_quality_accruals_accryoy_252d_slope_v105_signal,
    f36eq_f36_earnings_quality_accruals_accrrev2_252d_slope_v106_signal,
    f36eq_f36_earnings_quality_accruals_recvwcz_252d_slope_v107_signal,
    f36eq_f36_earnings_quality_accruals_accrual2_63d_slope_v108_signal,
    f36eq_f36_earnings_quality_accruals_accrual2_504d_slope_v109_signal,
    f36eq_f36_earnings_quality_accruals_convchg_63d_slope_v110_signal,
    f36eq_f36_earnings_quality_accruals_convchg_504d_slope_v111_signal,
    f36eq_f36_earnings_quality_accruals_recvbuildz_63d_slope_v112_signal,
    f36eq_f36_earnings_quality_accruals_recvbuildz_504d_slope_v113_signal,
    f36eq_f36_earnings_quality_accruals_wcaccrz_126d_slope_v114_signal,
    f36eq_f36_earnings_quality_accruals_accrrevz_126d_slope_v115_signal,
    f36eq_f36_earnings_quality_accruals_recvgrowthlvl_126d_slope_v116_signal,
    f36eq_f36_earnings_quality_accruals_recvgrowthlvl_504d_slope_v117_signal,
    f36eq_f36_earnings_quality_accruals_cashroachg_126d_slope_v118_signal,
    f36eq_f36_earnings_quality_accruals_cashroachg_252d_slope_v119_signal,
    f36eq_f36_earnings_quality_accruals_earnroachg_126d_slope_v120_signal,
    f36eq_f36_earnings_quality_accruals_earnroachg_252d_slope_v121_signal,
    f36eq_f36_earnings_quality_accruals_netaccrtanh_252d_slope_v122_signal,
    f36eq_f36_earnings_quality_accruals_accrualx_189d_slope_v123_signal,
    f36eq_f36_earnings_quality_accruals_accrualx_378d_slope_v124_signal,
    f36eq_f36_earnings_quality_accruals_cashroaz_126d_slope_v125_signal,
    f36eq_f36_earnings_quality_accruals_cashroaz_504d_slope_v126_signal,
    f36eq_f36_earnings_quality_accruals_wcaccrchg_126d_slope_v127_signal,
    f36eq_f36_earnings_quality_accruals_wcaccrchg_252d_slope_v128_signal,
    f36eq_f36_earnings_quality_accruals_recvcashchg_126d_slope_v129_signal,
    f36eq_f36_earnings_quality_accruals_recvcashchg_252d_slope_v130_signal,
    f36eq_f36_earnings_quality_accruals_revcashdivz_252d_slope_v131_signal,
    f36eq_f36_earnings_quality_accruals_revcashdivz_504d_slope_v132_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_rev_42d_slope_v133_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_rev_84d_slope_v134_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_rev_168d_slope_v135_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_cash_42d_slope_v136_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_cash_84d_slope_v137_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_cash_336d_slope_v138_signal,
    f36eq_f36_earnings_quality_accruals_gd_rev_cash_168d_slope_v139_signal,
    f36eq_f36_earnings_quality_accruals_gd_rev_cash_336d_slope_v140_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_ni_42d_slope_v141_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_ni_84d_slope_v142_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_ni_168d_slope_v143_signal,
    f36eq_f36_earnings_quality_accruals_gd_recv_ni_336d_slope_v144_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_rev_42d_slope_v145_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_rev_84d_slope_v146_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_rev_168d_slope_v147_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_rev_336d_slope_v148_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_cash_42d_slope_v149_signal,
    f36eq_f36_earnings_quality_accruals_gd_wc_cash_84d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F36_EARNINGS_QUALITY_ACCRUALS_REGISTRY_2ND_001_150 = REGISTRY


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

    print("OK f36_earnings_quality_accruals_2nd_derivatives_001_150_claude: %d features pass" % n_features)
