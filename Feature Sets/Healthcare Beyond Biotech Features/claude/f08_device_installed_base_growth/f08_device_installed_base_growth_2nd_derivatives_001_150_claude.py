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


def _ema(s, w):
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _diff(s, n):
    return s.diff(periods=n)


def _slope_pct(s, w):
    return s.pct_change(periods=w)


def _slope_diff_norm(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


# ===== folder domain primitives =====
def _f08_ppe_growth(ppnenet, w):
    return ppnenet.pct_change(periods=w)


def _f08_installed_base_proxy(ppnenet, revenue, w):
    g = ppnenet.pct_change(periods=w)
    return g * (revenue / revenue.rolling(w, min_periods=max(1, w // 2)).mean().replace(0, np.nan))


def _f08_install_acceleration(ppnenet, capex, w):
    return (capex / ppnenet.replace(0, np.nan)).rolling(w, min_periods=max(1, w // 2)).mean()

def f08dib_f08_device_installed_base_growth_p0bw21xclosesw5pct_5d_slope_v001_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xclosesw21norm_21d_slope_v002_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xclosesw63pct_63d_slope_v003_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xclosesw126norm_126d_slope_v004_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xclosesw252pct_252d_slope_v005_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xrevsw5norm_5d_slope_v006_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xrevsw21pct_21d_slope_v007_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xrevsw63norm_63d_slope_v008_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xrevsw126pct_126d_slope_v009_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw21xrevsw252norm_252d_slope_v010_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xclosesw5pct_5d_slope_v011_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xclosesw21norm_21d_slope_v012_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xclosesw63pct_63d_slope_v013_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xclosesw126norm_126d_slope_v014_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xclosesw252pct_252d_slope_v015_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xrevsw5norm_5d_slope_v016_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xrevsw21pct_21d_slope_v017_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xrevsw63norm_63d_slope_v018_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xrevsw126pct_126d_slope_v019_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw63xrevsw252norm_252d_slope_v020_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xclosesw5pct_5d_slope_v021_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xclosesw21norm_21d_slope_v022_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xclosesw63pct_63d_slope_v023_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xclosesw126norm_126d_slope_v024_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xclosesw252pct_252d_slope_v025_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xrevsw5norm_5d_slope_v026_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xrevsw21pct_21d_slope_v027_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xrevsw63norm_63d_slope_v028_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xrevsw126pct_126d_slope_v029_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw126xrevsw252norm_252d_slope_v030_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xclosesw5pct_5d_slope_v031_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xclosesw21norm_21d_slope_v032_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xclosesw63pct_63d_slope_v033_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xclosesw126norm_126d_slope_v034_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xclosesw252pct_252d_slope_v035_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xrevsw5norm_5d_slope_v036_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xrevsw21pct_21d_slope_v037_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xrevsw63norm_63d_slope_v038_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xrevsw126pct_126d_slope_v039_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw252xrevsw252norm_252d_slope_v040_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xclosesw5pct_5d_slope_v041_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xclosesw21norm_21d_slope_v042_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xclosesw63pct_63d_slope_v043_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xclosesw126norm_126d_slope_v044_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xclosesw252pct_252d_slope_v045_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xrevsw5norm_5d_slope_v046_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xrevsw21pct_21d_slope_v047_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xrevsw63norm_63d_slope_v048_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xrevsw126pct_126d_slope_v049_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p0bw504xrevsw252norm_252d_slope_v050_signal(ppnenet, closeadj):
    base = _f08_ppe_growth(ppnenet, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xclosesw5pct_5d_slope_v051_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xclosesw21norm_21d_slope_v052_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xclosesw63pct_63d_slope_v053_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xclosesw126norm_126d_slope_v054_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xclosesw252pct_252d_slope_v055_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xrevsw5norm_5d_slope_v056_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xrevsw21pct_21d_slope_v057_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xrevsw63norm_63d_slope_v058_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xrevsw126pct_126d_slope_v059_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw21xrevsw252norm_252d_slope_v060_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xclosesw5pct_5d_slope_v061_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xclosesw21norm_21d_slope_v062_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xclosesw63pct_63d_slope_v063_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xclosesw126norm_126d_slope_v064_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xclosesw252pct_252d_slope_v065_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xrevsw5norm_5d_slope_v066_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xrevsw21pct_21d_slope_v067_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xrevsw63norm_63d_slope_v068_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xrevsw126pct_126d_slope_v069_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw63xrevsw252norm_252d_slope_v070_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xclosesw5pct_5d_slope_v071_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xclosesw21norm_21d_slope_v072_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xclosesw63pct_63d_slope_v073_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xclosesw126norm_126d_slope_v074_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xclosesw252pct_252d_slope_v075_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xrevsw5norm_5d_slope_v076_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xrevsw21pct_21d_slope_v077_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xrevsw63norm_63d_slope_v078_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xrevsw126pct_126d_slope_v079_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw126xrevsw252norm_252d_slope_v080_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xclosesw5pct_5d_slope_v081_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xclosesw21norm_21d_slope_v082_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xclosesw63pct_63d_slope_v083_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xclosesw126norm_126d_slope_v084_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xclosesw252pct_252d_slope_v085_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xrevsw5norm_5d_slope_v086_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xrevsw21pct_21d_slope_v087_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xrevsw63norm_63d_slope_v088_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xrevsw126pct_126d_slope_v089_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw252xrevsw252norm_252d_slope_v090_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xclosesw5pct_5d_slope_v091_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xclosesw21norm_21d_slope_v092_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xclosesw63pct_63d_slope_v093_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xclosesw126norm_126d_slope_v094_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xclosesw252pct_252d_slope_v095_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xrevsw5norm_5d_slope_v096_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xrevsw21pct_21d_slope_v097_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xrevsw63norm_63d_slope_v098_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xrevsw126pct_126d_slope_v099_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p1bw504xrevsw252norm_252d_slope_v100_signal(ppnenet, revenue, closeadj):
    base = _f08_installed_base_proxy(ppnenet, revenue, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xclosesw5pct_5d_slope_v101_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xclosesw21norm_21d_slope_v102_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xclosesw63pct_63d_slope_v103_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xclosesw126norm_126d_slope_v104_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xclosesw252pct_252d_slope_v105_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21) * closeadj
    base = _mean(base, 21)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xrevsw5norm_5d_slope_v106_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xrevsw21pct_21d_slope_v107_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xrevsw63norm_63d_slope_v108_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xrevsw126pct_126d_slope_v109_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw21xrevsw252norm_252d_slope_v110_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 21)
    base = _ema(base, 21) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xclosesw5pct_5d_slope_v111_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xclosesw21norm_21d_slope_v112_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xclosesw63pct_63d_slope_v113_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xclosesw126norm_126d_slope_v114_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xclosesw252pct_252d_slope_v115_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63) * closeadj
    base = _mean(base, 63)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xrevsw5norm_5d_slope_v116_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xrevsw21pct_21d_slope_v117_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xrevsw63norm_63d_slope_v118_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xrevsw126pct_126d_slope_v119_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw63xrevsw252norm_252d_slope_v120_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 63)
    base = _ema(base, 63) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xclosesw5pct_5d_slope_v121_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xclosesw21norm_21d_slope_v122_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xclosesw63pct_63d_slope_v123_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xclosesw126norm_126d_slope_v124_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xclosesw252pct_252d_slope_v125_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126) * closeadj
    base = _mean(base, 126)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xrevsw5norm_5d_slope_v126_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xrevsw21pct_21d_slope_v127_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xrevsw63norm_63d_slope_v128_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xrevsw126pct_126d_slope_v129_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw126xrevsw252norm_252d_slope_v130_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 126)
    base = _ema(base, 126) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xclosesw5pct_5d_slope_v131_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xclosesw21norm_21d_slope_v132_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xclosesw63pct_63d_slope_v133_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xclosesw126norm_126d_slope_v134_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xclosesw252pct_252d_slope_v135_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252) * closeadj
    base = _mean(base, 252)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xrevsw5norm_5d_slope_v136_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xrevsw21pct_21d_slope_v137_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xrevsw63norm_63d_slope_v138_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xrevsw126pct_126d_slope_v139_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw252xrevsw252norm_252d_slope_v140_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 252)
    base = _ema(base, 252) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xclosesw5pct_5d_slope_v141_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xclosesw21norm_21d_slope_v142_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_diff_norm(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xclosesw63pct_63d_slope_v143_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xclosesw126norm_126d_slope_v144_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_diff_norm(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xclosesw252pct_252d_slope_v145_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504) * closeadj
    base = _mean(base, 504)
    result = _slope_pct(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xrevsw5norm_5d_slope_v146_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xrevsw21pct_21d_slope_v147_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_pct(base, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xrevsw63norm_63d_slope_v148_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xrevsw126pct_126d_slope_v149_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_pct(base, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f08dib_f08_device_installed_base_growth_p2bw504xrevsw252norm_252d_slope_v150_signal(ppnenet, capex, closeadj):
    base = _f08_install_acceleration(ppnenet, capex, 504)
    base = _ema(base, 504) * closeadj
    result = _slope_diff_norm(base, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f08dib_f08_device_installed_base_growth_p0bw21xclosesw5pct_5d_slope_v001_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xclosesw21norm_21d_slope_v002_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xclosesw63pct_63d_slope_v003_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xclosesw126norm_126d_slope_v004_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xclosesw252pct_252d_slope_v005_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xrevsw5norm_5d_slope_v006_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xrevsw21pct_21d_slope_v007_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xrevsw63norm_63d_slope_v008_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xrevsw126pct_126d_slope_v009_signal,
    f08dib_f08_device_installed_base_growth_p0bw21xrevsw252norm_252d_slope_v010_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xclosesw5pct_5d_slope_v011_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xclosesw21norm_21d_slope_v012_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xclosesw63pct_63d_slope_v013_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xclosesw126norm_126d_slope_v014_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xclosesw252pct_252d_slope_v015_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xrevsw5norm_5d_slope_v016_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xrevsw21pct_21d_slope_v017_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xrevsw63norm_63d_slope_v018_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xrevsw126pct_126d_slope_v019_signal,
    f08dib_f08_device_installed_base_growth_p0bw63xrevsw252norm_252d_slope_v020_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xclosesw5pct_5d_slope_v021_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xclosesw21norm_21d_slope_v022_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xclosesw63pct_63d_slope_v023_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xclosesw126norm_126d_slope_v024_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xclosesw252pct_252d_slope_v025_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xrevsw5norm_5d_slope_v026_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xrevsw21pct_21d_slope_v027_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xrevsw63norm_63d_slope_v028_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xrevsw126pct_126d_slope_v029_signal,
    f08dib_f08_device_installed_base_growth_p0bw126xrevsw252norm_252d_slope_v030_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xclosesw5pct_5d_slope_v031_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xclosesw21norm_21d_slope_v032_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xclosesw63pct_63d_slope_v033_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xclosesw126norm_126d_slope_v034_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xclosesw252pct_252d_slope_v035_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xrevsw5norm_5d_slope_v036_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xrevsw21pct_21d_slope_v037_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xrevsw63norm_63d_slope_v038_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xrevsw126pct_126d_slope_v039_signal,
    f08dib_f08_device_installed_base_growth_p0bw252xrevsw252norm_252d_slope_v040_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xclosesw5pct_5d_slope_v041_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xclosesw21norm_21d_slope_v042_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xclosesw63pct_63d_slope_v043_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xclosesw126norm_126d_slope_v044_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xclosesw252pct_252d_slope_v045_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xrevsw5norm_5d_slope_v046_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xrevsw21pct_21d_slope_v047_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xrevsw63norm_63d_slope_v048_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xrevsw126pct_126d_slope_v049_signal,
    f08dib_f08_device_installed_base_growth_p0bw504xrevsw252norm_252d_slope_v050_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xclosesw5pct_5d_slope_v051_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xclosesw21norm_21d_slope_v052_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xclosesw63pct_63d_slope_v053_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xclosesw126norm_126d_slope_v054_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xclosesw252pct_252d_slope_v055_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xrevsw5norm_5d_slope_v056_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xrevsw21pct_21d_slope_v057_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xrevsw63norm_63d_slope_v058_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xrevsw126pct_126d_slope_v059_signal,
    f08dib_f08_device_installed_base_growth_p1bw21xrevsw252norm_252d_slope_v060_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xclosesw5pct_5d_slope_v061_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xclosesw21norm_21d_slope_v062_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xclosesw63pct_63d_slope_v063_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xclosesw126norm_126d_slope_v064_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xclosesw252pct_252d_slope_v065_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xrevsw5norm_5d_slope_v066_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xrevsw21pct_21d_slope_v067_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xrevsw63norm_63d_slope_v068_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xrevsw126pct_126d_slope_v069_signal,
    f08dib_f08_device_installed_base_growth_p1bw63xrevsw252norm_252d_slope_v070_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xclosesw5pct_5d_slope_v071_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xclosesw21norm_21d_slope_v072_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xclosesw63pct_63d_slope_v073_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xclosesw126norm_126d_slope_v074_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xclosesw252pct_252d_slope_v075_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xrevsw5norm_5d_slope_v076_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xrevsw21pct_21d_slope_v077_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xrevsw63norm_63d_slope_v078_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xrevsw126pct_126d_slope_v079_signal,
    f08dib_f08_device_installed_base_growth_p1bw126xrevsw252norm_252d_slope_v080_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xclosesw5pct_5d_slope_v081_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xclosesw21norm_21d_slope_v082_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xclosesw63pct_63d_slope_v083_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xclosesw126norm_126d_slope_v084_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xclosesw252pct_252d_slope_v085_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xrevsw5norm_5d_slope_v086_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xrevsw21pct_21d_slope_v087_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xrevsw63norm_63d_slope_v088_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xrevsw126pct_126d_slope_v089_signal,
    f08dib_f08_device_installed_base_growth_p1bw252xrevsw252norm_252d_slope_v090_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xclosesw5pct_5d_slope_v091_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xclosesw21norm_21d_slope_v092_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xclosesw63pct_63d_slope_v093_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xclosesw126norm_126d_slope_v094_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xclosesw252pct_252d_slope_v095_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xrevsw5norm_5d_slope_v096_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xrevsw21pct_21d_slope_v097_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xrevsw63norm_63d_slope_v098_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xrevsw126pct_126d_slope_v099_signal,
    f08dib_f08_device_installed_base_growth_p1bw504xrevsw252norm_252d_slope_v100_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xclosesw5pct_5d_slope_v101_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xclosesw21norm_21d_slope_v102_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xclosesw63pct_63d_slope_v103_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xclosesw126norm_126d_slope_v104_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xclosesw252pct_252d_slope_v105_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xrevsw5norm_5d_slope_v106_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xrevsw21pct_21d_slope_v107_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xrevsw63norm_63d_slope_v108_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xrevsw126pct_126d_slope_v109_signal,
    f08dib_f08_device_installed_base_growth_p2bw21xrevsw252norm_252d_slope_v110_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xclosesw5pct_5d_slope_v111_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xclosesw21norm_21d_slope_v112_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xclosesw63pct_63d_slope_v113_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xclosesw126norm_126d_slope_v114_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xclosesw252pct_252d_slope_v115_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xrevsw5norm_5d_slope_v116_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xrevsw21pct_21d_slope_v117_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xrevsw63norm_63d_slope_v118_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xrevsw126pct_126d_slope_v119_signal,
    f08dib_f08_device_installed_base_growth_p2bw63xrevsw252norm_252d_slope_v120_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xclosesw5pct_5d_slope_v121_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xclosesw21norm_21d_slope_v122_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xclosesw63pct_63d_slope_v123_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xclosesw126norm_126d_slope_v124_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xclosesw252pct_252d_slope_v125_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xrevsw5norm_5d_slope_v126_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xrevsw21pct_21d_slope_v127_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xrevsw63norm_63d_slope_v128_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xrevsw126pct_126d_slope_v129_signal,
    f08dib_f08_device_installed_base_growth_p2bw126xrevsw252norm_252d_slope_v130_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xclosesw5pct_5d_slope_v131_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xclosesw21norm_21d_slope_v132_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xclosesw63pct_63d_slope_v133_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xclosesw126norm_126d_slope_v134_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xclosesw252pct_252d_slope_v135_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xrevsw5norm_5d_slope_v136_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xrevsw21pct_21d_slope_v137_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xrevsw63norm_63d_slope_v138_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xrevsw126pct_126d_slope_v139_signal,
    f08dib_f08_device_installed_base_growth_p2bw252xrevsw252norm_252d_slope_v140_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xclosesw5pct_5d_slope_v141_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xclosesw21norm_21d_slope_v142_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xclosesw63pct_63d_slope_v143_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xclosesw126norm_126d_slope_v144_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xclosesw252pct_252d_slope_v145_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xrevsw5norm_5d_slope_v146_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xrevsw21pct_21d_slope_v147_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xrevsw63norm_63d_slope_v148_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xrevsw126pct_126d_slope_v149_signal,
    f08dib_f08_device_installed_base_growth_p2bw504xrevsw252norm_252d_slope_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F08_DEVICE_INSTALLED_BASE_GROWTH_REGISTRY_SLOPE_001_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    assets  = pd.Series(2e9 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="assets")
    ppnenet = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")
    capex   = pd.Series(5e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.02, n))), name="capex")
    inventory   = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    receivables = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="receivables")
    cor     = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="cor")

    cols = {
        "closeadj": closeadj,
        "revenue": revenue, "assets": assets, "ppnenet": ppnenet, "capex": capex,
        "inventory": inventory, "receivables": receivables, "cor": cor,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f08_ppe_growth", "_f08_installed_base_proxy", "_f08_install_acceleration",)
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
    print(f"OK f08_device_installed_base_growth_2nd_derivatives_001_150_claude: {n_features} features pass")
