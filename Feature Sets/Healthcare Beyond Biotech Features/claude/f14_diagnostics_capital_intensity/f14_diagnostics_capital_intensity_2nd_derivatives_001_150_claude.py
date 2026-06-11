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


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _ema(s, w):
    return s.ewm(span=w, adjust=False, min_periods=max(1, w // 2)).mean()


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f14_capex_intensity(capex, revenue):
    return capex / revenue.replace(0, np.nan).abs()


def _f14_capex_to_ppe(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan).abs()


def _f14_capital_intensity_score(capex, revenue, w):
    ci = capex / revenue.replace(0, np.nan).abs()
    return ci.rolling(w, min_periods=max(1, w // 2)).mean()

def f14dci_f14_diagnostics_capital_intensity_ci_5d_slope_v001_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 5)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_5d_slope_v002_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 5)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_10d_slope_v003_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 10)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_10d_slope_v004_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 10)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_21d_slope_v005_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 21)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_21d_slope_v006_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 21)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_42d_slope_v007_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 42)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_42d_slope_v008_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 42)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_63d_slope_v009_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 63)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_63d_slope_v010_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 63)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_126d_slope_v011_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 126)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_126d_slope_v012_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 126)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_189d_slope_v013_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 189)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_189d_slope_v014_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 189)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_252d_slope_v015_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 252)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_252d_slope_v016_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 252)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_378d_slope_v017_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 378)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_378d_slope_v018_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 378)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_504d_slope_v019_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 504)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ci_504d_slope_v020_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 504)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_5d_slope_v021_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 5)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_5d_slope_v022_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 5)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_10d_slope_v023_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 10)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_10d_slope_v024_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 10)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_21d_slope_v025_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 21)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_21d_slope_v026_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 21)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_42d_slope_v027_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 42)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_42d_slope_v028_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 42)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_63d_slope_v029_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 63)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_63d_slope_v030_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 63)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_126d_slope_v031_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 126)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_126d_slope_v032_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 126)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_189d_slope_v033_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 189)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_189d_slope_v034_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 189)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_252d_slope_v035_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 252)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_252d_slope_v036_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 252)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_378d_slope_v037_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 378)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_378d_slope_v038_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 378)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_504d_slope_v039_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 504)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cipp_504d_slope_v040_signal(capex, ppnenet, closeadj):
    ppe_w = _mean(ppnenet, 504)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_5d_slope_v041_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 5) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_5d_slope_v042_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 5) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_10d_slope_v043_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 10) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_10d_slope_v044_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 10) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_21d_slope_v045_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_21d_slope_v046_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_42d_slope_v047_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 42) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_42d_slope_v048_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 42) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_63d_slope_v049_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_63d_slope_v050_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 63) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_126d_slope_v051_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 126) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_126d_slope_v052_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 126) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_189d_slope_v053_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 189) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_189d_slope_v054_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 189) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_252d_slope_v055_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_252d_slope_v056_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 252) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_378d_slope_v057_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 378) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_378d_slope_v058_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 378) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_504d_slope_v059_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 504) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cis_504d_slope_v060_signal(capex, revenue, closeadj):
    base = _f14_capital_intensity_score(capex, revenue, 504) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_5d_slope_v061_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 5)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_5d_slope_v062_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 5)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_10d_slope_v063_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 10)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_10d_slope_v064_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 10)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_21d_slope_v065_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 21)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_21d_slope_v066_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 21)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_42d_slope_v067_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 42)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_42d_slope_v068_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 42)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_63d_slope_v069_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 63)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_63d_slope_v070_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 63)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_126d_slope_v071_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 126)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_126d_slope_v072_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 126)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_189d_slope_v073_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 189)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_189d_slope_v074_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 189)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_252d_slope_v075_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 252)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_252d_slope_v076_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 252)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_378d_slope_v077_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 378)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_378d_slope_v078_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 378)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_504d_slope_v079_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 504)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_ciema_504d_slope_v080_signal(capex, revenue, closeadj):
    rev_w = _ema(revenue, 504)
    base = _f14_capex_intensity(capex, rev_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_5d_slope_v081_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 5)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_5d_slope_v082_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 5)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_10d_slope_v083_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 10)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_10d_slope_v084_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 10)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_21d_slope_v085_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 21)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_21d_slope_v086_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 21)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_42d_slope_v087_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 42)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_42d_slope_v088_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 42)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_63d_slope_v089_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 63)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_63d_slope_v090_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 63)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_126d_slope_v091_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 126)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_126d_slope_v092_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 126)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_189d_slope_v093_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 189)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_189d_slope_v094_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 189)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_252d_slope_v095_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 252)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_252d_slope_v096_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 252)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_378d_slope_v097_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 378)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_378d_slope_v098_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 378)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_504d_slope_v099_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 504)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cippema_504d_slope_v100_signal(capex, ppnenet, closeadj):
    ppe_w = _ema(ppnenet, 504)
    base = _f14_capex_to_ppe(capex, ppe_w) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_5d_slope_v101_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 5), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_5d_slope_v102_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 5), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_10d_slope_v103_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 10), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_10d_slope_v104_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 10), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_21d_slope_v105_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_21d_slope_v106_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 21), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_42d_slope_v107_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 42), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_42d_slope_v108_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 42), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_63d_slope_v109_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 63), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_63d_slope_v110_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 63), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_126d_slope_v111_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 126), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_126d_slope_v112_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 126), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_189d_slope_v113_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 189), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_189d_slope_v114_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 189), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_252d_slope_v115_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 252), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_252d_slope_v116_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 252), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_378d_slope_v117_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 378), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_378d_slope_v118_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 378), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_504d_slope_v119_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 504), 21) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cismean_504d_slope_v120_signal(capex, revenue, closeadj):
    base = _mean(_f14_capital_intensity_score(capex, revenue, 504), 21) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_5d_slope_v121_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 5)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_5d_slope_v122_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 5)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_10d_slope_v123_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 10)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_10d_slope_v124_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 10)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_21d_slope_v125_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 21)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_21d_slope_v126_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 21)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_42d_slope_v127_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 42)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_42d_slope_v128_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 42)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_63d_slope_v129_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 63)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_63d_slope_v130_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 63)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_126d_slope_v131_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 126)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_126d_slope_v132_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 126)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_189d_slope_v133_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 189)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_189d_slope_v134_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 189)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_252d_slope_v135_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 252)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_252d_slope_v136_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 252)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_378d_slope_v137_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 378)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_378d_slope_v138_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 378)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_504d_slope_v139_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 504)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cisq_504d_slope_v140_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 504)
    ci = _f14_capex_intensity(capex, rev_w)
    base = ci * ci.abs() * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_5d_slope_v141_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 5)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_5d_slope_v142_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 5)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_10d_slope_v143_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 10)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_10d_slope_v144_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 10)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_21d_slope_v145_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 21)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_21d_slope_v146_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 21)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_42d_slope_v147_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 42)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_42d_slope_v148_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 42)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_63d_slope_v149_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 63)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f14dci_f14_diagnostics_capital_intensity_cieff_63d_slope_v150_signal(capex, revenue, closeadj):
    rev_w = _mean(revenue, 63)
    ci = _f14_capex_intensity(capex, rev_w)
    base = (1.0 / (1.0 + ci.abs())) * closeadj
    result = _slope_diff_norm(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f14dci_f14_diagnostics_capital_intensity_ci_5d_slope_v001_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_5d_slope_v002_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_10d_slope_v003_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_10d_slope_v004_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_21d_slope_v005_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_21d_slope_v006_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_42d_slope_v007_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_42d_slope_v008_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_63d_slope_v009_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_63d_slope_v010_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_126d_slope_v011_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_126d_slope_v012_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_189d_slope_v013_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_189d_slope_v014_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_252d_slope_v015_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_252d_slope_v016_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_378d_slope_v017_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_378d_slope_v018_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_504d_slope_v019_signal,
    f14dci_f14_diagnostics_capital_intensity_ci_504d_slope_v020_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_5d_slope_v021_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_5d_slope_v022_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_10d_slope_v023_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_10d_slope_v024_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_21d_slope_v025_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_21d_slope_v026_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_42d_slope_v027_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_42d_slope_v028_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_63d_slope_v029_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_63d_slope_v030_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_126d_slope_v031_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_126d_slope_v032_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_189d_slope_v033_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_189d_slope_v034_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_252d_slope_v035_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_252d_slope_v036_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_378d_slope_v037_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_378d_slope_v038_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_504d_slope_v039_signal,
    f14dci_f14_diagnostics_capital_intensity_cipp_504d_slope_v040_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_5d_slope_v041_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_5d_slope_v042_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_10d_slope_v043_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_10d_slope_v044_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_21d_slope_v045_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_21d_slope_v046_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_42d_slope_v047_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_42d_slope_v048_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_63d_slope_v049_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_63d_slope_v050_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_126d_slope_v051_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_126d_slope_v052_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_189d_slope_v053_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_189d_slope_v054_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_252d_slope_v055_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_252d_slope_v056_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_378d_slope_v057_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_378d_slope_v058_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_504d_slope_v059_signal,
    f14dci_f14_diagnostics_capital_intensity_cis_504d_slope_v060_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_5d_slope_v061_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_5d_slope_v062_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_10d_slope_v063_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_10d_slope_v064_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_21d_slope_v065_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_21d_slope_v066_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_42d_slope_v067_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_42d_slope_v068_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_63d_slope_v069_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_63d_slope_v070_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_126d_slope_v071_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_126d_slope_v072_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_189d_slope_v073_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_189d_slope_v074_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_252d_slope_v075_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_252d_slope_v076_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_378d_slope_v077_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_378d_slope_v078_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_504d_slope_v079_signal,
    f14dci_f14_diagnostics_capital_intensity_ciema_504d_slope_v080_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_5d_slope_v081_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_5d_slope_v082_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_10d_slope_v083_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_10d_slope_v084_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_21d_slope_v085_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_21d_slope_v086_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_42d_slope_v087_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_42d_slope_v088_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_63d_slope_v089_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_63d_slope_v090_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_126d_slope_v091_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_126d_slope_v092_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_189d_slope_v093_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_189d_slope_v094_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_252d_slope_v095_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_252d_slope_v096_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_378d_slope_v097_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_378d_slope_v098_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_504d_slope_v099_signal,
    f14dci_f14_diagnostics_capital_intensity_cippema_504d_slope_v100_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_5d_slope_v101_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_5d_slope_v102_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_10d_slope_v103_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_10d_slope_v104_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_21d_slope_v105_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_21d_slope_v106_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_42d_slope_v107_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_42d_slope_v108_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_63d_slope_v109_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_63d_slope_v110_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_126d_slope_v111_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_126d_slope_v112_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_189d_slope_v113_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_189d_slope_v114_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_252d_slope_v115_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_252d_slope_v116_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_378d_slope_v117_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_378d_slope_v118_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_504d_slope_v119_signal,
    f14dci_f14_diagnostics_capital_intensity_cismean_504d_slope_v120_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_5d_slope_v121_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_5d_slope_v122_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_10d_slope_v123_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_10d_slope_v124_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_21d_slope_v125_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_21d_slope_v126_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_42d_slope_v127_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_42d_slope_v128_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_63d_slope_v129_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_63d_slope_v130_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_126d_slope_v131_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_126d_slope_v132_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_189d_slope_v133_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_189d_slope_v134_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_252d_slope_v135_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_252d_slope_v136_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_378d_slope_v137_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_378d_slope_v138_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_504d_slope_v139_signal,
    f14dci_f14_diagnostics_capital_intensity_cisq_504d_slope_v140_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_5d_slope_v141_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_5d_slope_v142_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_10d_slope_v143_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_10d_slope_v144_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_21d_slope_v145_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_21d_slope_v146_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_42d_slope_v147_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_42d_slope_v148_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_63d_slope_v149_signal,
    f14dci_f14_diagnostics_capital_intensity_cieff_63d_slope_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F14_DIAGNOSTICS_CAPITAL_INTENSITY_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high, name="high")
    low = pd.Series(low, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    ebit    = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebit")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ncfo    = pd.Series(1.2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.014, n))), name="ncfo")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    depamor = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="depamor")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    gp      = pd.Series(3.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="gp")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")
    rnd     = pd.Series(4e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="rnd")
    assets       = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    assetsc      = pd.Series(8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsc")
    assetsnc     = pd.Series(1.2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assetsnc")
    liabilities  = pd.Series(1.1e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilities")
    liabilitiesc = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesc")
    liabilitiesnc= pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="liabilitiesnc")
    equity       = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equity")
    equityusd    = pd.Series(9e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="equityusd")
    debt         = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    debtc        = pd.Series(1.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtc")
    debtnc       = pd.Series(4.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debtnc")
    cashneq      = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables  = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    payables     = pd.Series(1.8e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="payables")
    deferredrev  = pd.Series(1.0e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="deferredrev")
    workingcapital = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="workingcapital")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    intangibles  = pd.Series(3e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="intangibles")
    tangibles    = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="tangibles")
    invcap       = pd.Series(1.4e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="invcap")
    retearn      = pd.Series(5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="retearn")
    sbcomp       = pd.Series(2e7 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="sbcomp")
    sharesbas    = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="sharesbas")
    shareswa     = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswa")
    shareswadil  = pd.Series(1.02e8 * np.exp(np.cumsum(np.random.normal(-0.00005, 0.003, n))), name="shareswadil")
    eps          = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    epsdil       = pd.Series(0.98 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="epsdil")
    bvps         = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="bvps")
    fcfps        = pd.Series(0.8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="fcfps")
    sps          = pd.Series(10.0 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="sps")
    dps          = pd.Series(0.5 * np.exp(np.cumsum(np.random.normal(0.0002, 0.005, n))), name="dps")
    marketcap    = pd.Series(closeadj * 1e8, name="marketcap")
    ev           = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    pe           = pd.Series(closeadj / eps.replace(0, np.nan).abs(), name="pe")
    pb           = pd.Series(closeadj / bvps.replace(0, np.nan).abs(), name="pb")
    ps           = pd.Series(closeadj / sps.replace(0, np.nan).abs(), name="ps")
    evebit       = pd.Series(ev / ebit.replace(0, np.nan).abs(), name="evebit")
    evebitda     = pd.Series(ev / ebitda.replace(0, np.nan).abs(), name="evebitda")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    netmargin    = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="netmargin")
    roa          = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe          = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ros          = pd.Series(0.08 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ros")
    currentratio = pd.Series(1.5 + 0.3*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="currentratio")
    de           = pd.Series(0.6 + 0.2*np.sin(np.arange(n)/250.0) + 0.05*np.random.randn(n), name="de")
    payoutratio  = pd.Series(0.3 + 0.1*np.sin(np.arange(n)/250.0) + 0.03*np.random.randn(n), name="payoutratio")
    divyield     = pd.Series(0.02 + 0.005*np.sin(np.arange(n)/250.0) + 0.001*np.random.randn(n), name="divyield")
    assetturnover= pd.Series(0.7 + 0.15*np.sin(np.arange(n)/250.0) + 0.02*np.random.randn(n), name="assetturnover")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "assets": assets, "assetsc": assetsc, "assetsnc": assetsnc,
        "liabilities": liabilities, "liabilitiesc": liabilitiesc, "liabilitiesnc": liabilitiesnc,
        "equity": equity, "equityusd": equityusd,
        "debt": debt, "debtc": debtc, "debtnc": debtnc, "cashneq": cashneq,
        "inventory": inventory, "receivables": receivables, "payables": payables,
        "deferredrev": deferredrev, "workingcapital": workingcapital,
        "ppnenet": ppnenet, "intangibles": intangibles, "tangibles": tangibles,
        "invcap": invcap, "retearn": retearn, "sbcomp": sbcomp,
        "sharesbas": sharesbas, "shareswa": shareswa, "shareswadil": shareswadil,
        "eps": eps, "epsdil": epsdil, "bvps": bvps, "fcfps": fcfps, "sps": sps, "dps": dps,
        "marketcap": marketcap, "ev": ev,
        "pe": pe, "pb": pb, "ps": ps, "evebit": evebit, "evebitda": evebitda,
        "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "netmargin": netmargin,
        "roa": roa, "roe": roe, "roic": roic, "ros": ros,
        "currentratio": currentratio, "de": de,
        "payoutratio": payoutratio, "divyield": divyield, "assetturnover": assetturnover,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f14_capex_intensity", "_f14_capex_to_ppe", "_f14_capital_intensity_score",)
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
    print(f"OK f14_diagnostics_capital_intensity_2nd_derivatives_001_150_claude: {n_features} features pass")
