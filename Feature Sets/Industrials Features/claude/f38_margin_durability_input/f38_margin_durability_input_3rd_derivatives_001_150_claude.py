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


def _slope(s, w):
    return s.diff(periods=w) / s.abs().replace(0, np.nan)


def _jerk(s, w):
    sl = s.diff(periods=w) / s.abs().replace(0, np.nan)
    return sl.diff(periods=w)


# ===== folder domain primitives =====
def _f38_input_pass_through(grossmargin, cor, revenue, w):
    """Pass-through: covariance(gm change, cor/rev change) / var(cor/rev change)."""
    cor_ratio = cor / revenue.replace(0, np.nan)
    dcr = cor_ratio.diff()
    dgm = grossmargin.diff()
    cov = dgm.rolling(w, min_periods=max(2, w // 2)).cov(dcr)
    var = dcr.rolling(w, min_periods=max(2, w // 2)).var()
    return cov / var.replace(0, np.nan)


def _f38_margin_resilience(grossmargin, w):
    """Resilience: rolling mean / rolling std of gross margin."""
    m = grossmargin.rolling(w, min_periods=max(2, w // 2)).mean()
    s = grossmargin.rolling(w, min_periods=max(2, w // 2)).std()
    return m / s.replace(0, np.nan)


def _f38_input_buffer(grossmargin, cor, w):
    """Buffer: rolling gm minus rolling cor pct change."""
    gm_smooth = grossmargin.rolling(w, min_periods=max(2, w // 2)).mean()
    cor_pct = cor.pct_change(periods=w)
    return gm_smooth - cor_pct


def f38mdi_f38_margin_durability_input_passthrough_63d_5d_jerk_v001_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    base_ = p * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthrough_126d_21d_jerk_v002_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    base_ = p * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthrough_189d_63d_jerk_v003_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 189)
    base_ = p * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthrough_252d_126d_jerk_v004_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    base_ = p * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthrough_378d_252d_jerk_v005_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    base_ = p * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthrough_504d_5d_jerk_v006_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    base_ = p * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_5d_21d_jerk_v007_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 5)
    base_ = r * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_10d_63d_jerk_v008_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 10)
    base_ = r * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_21d_126d_jerk_v009_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 21)
    base_ = r * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_42d_252d_jerk_v010_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 42)
    base_ = r * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_63d_5d_jerk_v011_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 63)
    base_ = r * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_126d_21d_jerk_v012_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 126)
    base_ = r * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_189d_63d_jerk_v013_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 189)
    base_ = r * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_252d_126d_jerk_v014_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 252)
    base_ = r * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_378d_252d_jerk_v015_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 378)
    base_ = r * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilience_504d_5d_jerk_v016_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 504)
    base_ = r * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_5d_21d_jerk_v017_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 5)
    base_ = b * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_10d_63d_jerk_v018_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 10)
    base_ = b * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_21d_126d_jerk_v019_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = b * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_42d_252d_jerk_v020_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    base_ = b * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_63d_5d_jerk_v021_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    base_ = b * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_126d_21d_jerk_v022_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    base_ = b * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_189d_63d_jerk_v023_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    base_ = b * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_252d_126d_jerk_v024_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    base_ = b * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_378d_252d_jerk_v025_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    base_ = b * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_buffer_504d_5d_jerk_v026_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    base_ = b * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxres_126d_21d_jerk_v027_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    r = _f38_margin_resilience(grossmargin, 126)
    base_ = (p * r) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxres_189d_63d_jerk_v028_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 189)
    r = _f38_margin_resilience(grossmargin, 189)
    base_ = (p * r) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxres_252d_126d_jerk_v029_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    r = _f38_margin_resilience(grossmargin, 252)
    base_ = (p * r) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxres_378d_252d_jerk_v030_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    r = _f38_margin_resilience(grossmargin, 378)
    base_ = (p * r) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxres_504d_5d_jerk_v031_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    r = _f38_margin_resilience(grossmargin, 504)
    base_ = (p * r) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilz_21_252_21d_jerk_v032_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 21)
    base_ = _z(r, 252) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilz_63_252_63d_jerk_v033_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 63)
    base_ = _z(r, 252) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilz_126_252_126d_jerk_v034_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 126)
    base_ = _z(r, 252) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilz_21_504_252d_jerk_v035_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 21)
    base_ = _z(r, 504) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilz_63_504_5d_jerk_v036_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 63)
    base_ = _z(r, 504) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilz_126_504_21d_jerk_v037_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 126)
    base_ = _z(r, 504) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_5d_63d_jerk_v038_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 5)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_10d_126d_jerk_v039_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 10)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_21d_252d_jerk_v040_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_42d_5d_jerk_v041_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_63d_21d_jerk_v042_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_126d_63d_jerk_v043_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_189d_126d_jerk_v044_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_252d_252d_jerk_v045_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_378d_5d_jerk_v046_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrev_504d_21d_jerk_v047_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    base_ = b * _safe_div(revenue, revenue.shift(252)) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthroughsm_63d_63d_jerk_v048_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    base_ = _mean(p, 21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthroughsm_126d_126d_jerk_v049_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    base_ = _mean(p, 21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthroughsm_252d_252d_jerk_v050_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    base_ = _mean(p, 21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthroughsm_378d_5d_jerk_v051_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    base_ = _mean(p, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passthroughsm_504d_21d_jerk_v052_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    base_ = _mean(p, 21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferstd_63d_63d_jerk_v053_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = _std(b, 63) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferstd_126d_126d_jerk_v054_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = _std(b, 126) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferstd_252d_252d_jerk_v055_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = _std(b, 252) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferstd_378d_5d_jerk_v056_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = _std(b, 378) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferstd_504d_21d_jerk_v057_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = _std(b, 504) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_5d_63d_jerk_v058_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 5)
    b = _f38_input_buffer(grossmargin, cor, 5)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_10d_126d_jerk_v059_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 10)
    b = _f38_input_buffer(grossmargin, cor, 10)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_21d_252d_jerk_v060_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 21)
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_42d_5d_jerk_v061_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 42)
    b = _f38_input_buffer(grossmargin, cor, 42)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_63d_21d_jerk_v062_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 63)
    b = _f38_input_buffer(grossmargin, cor, 63)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_126d_63d_jerk_v063_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 126)
    b = _f38_input_buffer(grossmargin, cor, 126)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_189d_126d_jerk_v064_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 189)
    b = _f38_input_buffer(grossmargin, cor, 189)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_252d_252d_jerk_v065_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 252)
    b = _f38_input_buffer(grossmargin, cor, 252)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_378d_5d_jerk_v066_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 378)
    b = _f38_input_buffer(grossmargin, cor, 378)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resxbuf_504d_21d_jerk_v067_signal(grossmargin, cor, closeadj):
    r = _f38_margin_resilience(grossmargin, 504)
    b = _f38_input_buffer(grossmargin, cor, 504)
    base_ = (r * b) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_5d_63d_jerk_v068_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 5)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_10d_126d_jerk_v069_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 10)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_21d_252d_jerk_v070_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_42d_5d_jerk_v071_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_63d_21d_jerk_v072_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_126d_63d_jerk_v073_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_189d_126d_jerk_v074_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_252d_252d_jerk_v075_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_378d_5d_jerk_v076_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_504d_21d_jerk_v077_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    base_ = b.diff(21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_63d_63d_jerk_v078_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    base_ = _ema(p, 21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_126d_126d_jerk_v079_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    base_ = _ema(p, 21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_252d_252d_jerk_v080_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    base_ = _ema(p, 21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_378d_5d_jerk_v081_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    base_ = _ema(p, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_504d_21d_jerk_v082_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    base_ = _ema(p, 21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_5d_63d_jerk_v083_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 5)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_10d_126d_jerk_v084_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 10)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_21d_252d_jerk_v085_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 21)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_42d_5d_jerk_v086_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 42)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_63d_21d_jerk_v087_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 63)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_126d_63d_jerk_v088_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 126)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_189d_126d_jerk_v089_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 189)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_252d_252d_jerk_v090_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 252)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_378d_5d_jerk_v091_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 378)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_504d_21d_jerk_v092_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 504)
    base_ = r * r.abs() * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_126d_63d_jerk_v093_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    r = _f38_margin_resilience(grossmargin, 126)
    base_ = (b + r) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_189d_126d_jerk_v094_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    r = _f38_margin_resilience(grossmargin, 189)
    base_ = (b + r) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_252d_252d_jerk_v095_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    r = _f38_margin_resilience(grossmargin, 252)
    base_ = (b + r) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_378d_5d_jerk_v096_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    r = _f38_margin_resilience(grossmargin, 378)
    base_ = (b + r) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_504d_21d_jerk_v097_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    r = _f38_margin_resilience(grossmargin, 504)
    base_ = (b + r) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_5d_63d_jerk_v098_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 5)
    base_ = b * cor.pct_change(5) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_10d_126d_jerk_v099_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 10)
    base_ = b * cor.pct_change(10) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_21d_252d_jerk_v100_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = b * cor.pct_change(21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_42d_5d_jerk_v101_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    base_ = b * cor.pct_change(42) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_63d_21d_jerk_v102_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    base_ = b * cor.pct_change(63) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_126d_63d_jerk_v103_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    base_ = b * cor.pct_change(126) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_189d_126d_jerk_v104_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    base_ = b * cor.pct_change(189) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_252d_252d_jerk_v105_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    base_ = b * cor.pct_change(252) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_378d_5d_jerk_v106_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    base_ = b * cor.pct_change(378) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_504d_21d_jerk_v107_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    base_ = b * cor.pct_change(504) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_5d_63d_jerk_v108_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 5)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_10d_126d_jerk_v109_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 10)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_21d_252d_jerk_v110_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 21)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_42d_5d_jerk_v111_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 42)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_63d_21d_jerk_v112_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 63)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_126d_63d_jerk_v113_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 126)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_189d_126d_jerk_v114_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 189)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_252d_252d_jerk_v115_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 252)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_378d_5d_jerk_v116_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 378)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_504d_21d_jerk_v117_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 504)
    base_ = _ema(r, 21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_5d_63d_jerk_v118_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 5)
    base_ = b * revenue.pct_change(5) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_10d_126d_jerk_v119_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 10)
    base_ = b * revenue.pct_change(10) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_21d_252d_jerk_v120_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = b * revenue.pct_change(21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_42d_5d_jerk_v121_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    base_ = b * revenue.pct_change(42) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_63d_21d_jerk_v122_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    base_ = b * revenue.pct_change(63) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_126d_63d_jerk_v123_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    base_ = b * revenue.pct_change(126) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_189d_126d_jerk_v124_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    base_ = b * revenue.pct_change(189) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_252d_252d_jerk_v125_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    base_ = b * revenue.pct_change(252) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_378d_5d_jerk_v126_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    base_ = b * revenue.pct_change(378) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_504d_21d_jerk_v127_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    base_ = b * revenue.pct_change(504) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_63d_63d_jerk_v128_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    base_ = p.diff(21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_126d_126d_jerk_v129_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    base_ = p.diff(21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_252d_252d_jerk_v130_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    base_ = p.diff(21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_378d_5d_jerk_v131_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    base_ = p.diff(21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_504d_21d_jerk_v132_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    base_ = p.diff(21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_21d_63d_jerk_v133_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    base_ = b * cor.pct_change(21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_42d_126d_jerk_v134_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    base_ = b * cor.pct_change(21) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_63d_252d_jerk_v135_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    base_ = b * cor.pct_change(21) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_126d_5d_jerk_v136_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    base_ = b * cor.pct_change(21) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_252d_21d_jerk_v137_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    base_ = b * cor.pct_change(21) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_504d_63d_jerk_v138_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    base_ = b * cor.pct_change(21) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilcross_63v252_126d_jerk_v139_signal(grossmargin, closeadj):
    r1 = _f38_margin_resilience(grossmargin, 63)
    r2 = _f38_margin_resilience(grossmargin, 252)
    base_ = (r1 - r2) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilcross_126v504_252d_jerk_v140_signal(grossmargin, closeadj):
    r1 = _f38_margin_resilience(grossmargin, 126)
    r2 = _f38_margin_resilience(grossmargin, 504)
    base_ = (r1 - r2) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilcross_21v252_5d_jerk_v141_signal(grossmargin, closeadj):
    r1 = _f38_margin_resilience(grossmargin, 21)
    r2 = _f38_margin_resilience(grossmargin, 252)
    base_ = (r1 - r2) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_63d_21d_jerk_v142_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    b = _f38_input_buffer(grossmargin, cor, 63)
    base_ = (p + b) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_126d_63d_jerk_v143_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    b = _f38_input_buffer(grossmargin, cor, 126)
    base_ = (p + b) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_252d_126d_jerk_v144_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    b = _f38_input_buffer(grossmargin, cor, 252)
    base_ = (p + b) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_378d_252d_jerk_v145_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    b = _f38_input_buffer(grossmargin, cor, 378)
    base_ = (p + b) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_504d_5d_jerk_v146_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    b = _f38_input_buffer(grossmargin, cor, 504)
    base_ = (p + b) * closeadj
    result = _jerk(base_, 5)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passz_63_252_21d_jerk_v147_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    base_ = _z(p, 252) * closeadj
    result = _jerk(base_, 21)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passz_126_252_63d_jerk_v148_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    base_ = _z(p, 252) * closeadj
    result = _jerk(base_, 63)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passz_63_504_126d_jerk_v149_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    base_ = _z(p, 504) * closeadj
    result = _jerk(base_, 126)
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passz_126_504_252d_jerk_v150_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    base_ = _z(p, 504) * closeadj
    result = _jerk(base_, 252)
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f38mdi_f38_margin_durability_input_passthrough_63d_5d_jerk_v001_signal,
    f38mdi_f38_margin_durability_input_passthrough_126d_21d_jerk_v002_signal,
    f38mdi_f38_margin_durability_input_passthrough_189d_63d_jerk_v003_signal,
    f38mdi_f38_margin_durability_input_passthrough_252d_126d_jerk_v004_signal,
    f38mdi_f38_margin_durability_input_passthrough_378d_252d_jerk_v005_signal,
    f38mdi_f38_margin_durability_input_passthrough_504d_5d_jerk_v006_signal,
    f38mdi_f38_margin_durability_input_resilience_5d_21d_jerk_v007_signal,
    f38mdi_f38_margin_durability_input_resilience_10d_63d_jerk_v008_signal,
    f38mdi_f38_margin_durability_input_resilience_21d_126d_jerk_v009_signal,
    f38mdi_f38_margin_durability_input_resilience_42d_252d_jerk_v010_signal,
    f38mdi_f38_margin_durability_input_resilience_63d_5d_jerk_v011_signal,
    f38mdi_f38_margin_durability_input_resilience_126d_21d_jerk_v012_signal,
    f38mdi_f38_margin_durability_input_resilience_189d_63d_jerk_v013_signal,
    f38mdi_f38_margin_durability_input_resilience_252d_126d_jerk_v014_signal,
    f38mdi_f38_margin_durability_input_resilience_378d_252d_jerk_v015_signal,
    f38mdi_f38_margin_durability_input_resilience_504d_5d_jerk_v016_signal,
    f38mdi_f38_margin_durability_input_buffer_5d_21d_jerk_v017_signal,
    f38mdi_f38_margin_durability_input_buffer_10d_63d_jerk_v018_signal,
    f38mdi_f38_margin_durability_input_buffer_21d_126d_jerk_v019_signal,
    f38mdi_f38_margin_durability_input_buffer_42d_252d_jerk_v020_signal,
    f38mdi_f38_margin_durability_input_buffer_63d_5d_jerk_v021_signal,
    f38mdi_f38_margin_durability_input_buffer_126d_21d_jerk_v022_signal,
    f38mdi_f38_margin_durability_input_buffer_189d_63d_jerk_v023_signal,
    f38mdi_f38_margin_durability_input_buffer_252d_126d_jerk_v024_signal,
    f38mdi_f38_margin_durability_input_buffer_378d_252d_jerk_v025_signal,
    f38mdi_f38_margin_durability_input_buffer_504d_5d_jerk_v026_signal,
    f38mdi_f38_margin_durability_input_passxres_126d_21d_jerk_v027_signal,
    f38mdi_f38_margin_durability_input_passxres_189d_63d_jerk_v028_signal,
    f38mdi_f38_margin_durability_input_passxres_252d_126d_jerk_v029_signal,
    f38mdi_f38_margin_durability_input_passxres_378d_252d_jerk_v030_signal,
    f38mdi_f38_margin_durability_input_passxres_504d_5d_jerk_v031_signal,
    f38mdi_f38_margin_durability_input_resilz_21_252_21d_jerk_v032_signal,
    f38mdi_f38_margin_durability_input_resilz_63_252_63d_jerk_v033_signal,
    f38mdi_f38_margin_durability_input_resilz_126_252_126d_jerk_v034_signal,
    f38mdi_f38_margin_durability_input_resilz_21_504_252d_jerk_v035_signal,
    f38mdi_f38_margin_durability_input_resilz_63_504_5d_jerk_v036_signal,
    f38mdi_f38_margin_durability_input_resilz_126_504_21d_jerk_v037_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_5d_63d_jerk_v038_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_10d_126d_jerk_v039_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_21d_252d_jerk_v040_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_42d_5d_jerk_v041_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_63d_21d_jerk_v042_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_126d_63d_jerk_v043_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_189d_126d_jerk_v044_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_252d_252d_jerk_v045_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_378d_5d_jerk_v046_signal,
    f38mdi_f38_margin_durability_input_bufferxrev_504d_21d_jerk_v047_signal,
    f38mdi_f38_margin_durability_input_passthroughsm_63d_63d_jerk_v048_signal,
    f38mdi_f38_margin_durability_input_passthroughsm_126d_126d_jerk_v049_signal,
    f38mdi_f38_margin_durability_input_passthroughsm_252d_252d_jerk_v050_signal,
    f38mdi_f38_margin_durability_input_passthroughsm_378d_5d_jerk_v051_signal,
    f38mdi_f38_margin_durability_input_passthroughsm_504d_21d_jerk_v052_signal,
    f38mdi_f38_margin_durability_input_bufferstd_63d_63d_jerk_v053_signal,
    f38mdi_f38_margin_durability_input_bufferstd_126d_126d_jerk_v054_signal,
    f38mdi_f38_margin_durability_input_bufferstd_252d_252d_jerk_v055_signal,
    f38mdi_f38_margin_durability_input_bufferstd_378d_5d_jerk_v056_signal,
    f38mdi_f38_margin_durability_input_bufferstd_504d_21d_jerk_v057_signal,
    f38mdi_f38_margin_durability_input_resxbuf_5d_63d_jerk_v058_signal,
    f38mdi_f38_margin_durability_input_resxbuf_10d_126d_jerk_v059_signal,
    f38mdi_f38_margin_durability_input_resxbuf_21d_252d_jerk_v060_signal,
    f38mdi_f38_margin_durability_input_resxbuf_42d_5d_jerk_v061_signal,
    f38mdi_f38_margin_durability_input_resxbuf_63d_21d_jerk_v062_signal,
    f38mdi_f38_margin_durability_input_resxbuf_126d_63d_jerk_v063_signal,
    f38mdi_f38_margin_durability_input_resxbuf_189d_126d_jerk_v064_signal,
    f38mdi_f38_margin_durability_input_resxbuf_252d_252d_jerk_v065_signal,
    f38mdi_f38_margin_durability_input_resxbuf_378d_5d_jerk_v066_signal,
    f38mdi_f38_margin_durability_input_resxbuf_504d_21d_jerk_v067_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_5d_63d_jerk_v068_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_10d_126d_jerk_v069_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_21d_252d_jerk_v070_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_42d_5d_jerk_v071_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_63d_21d_jerk_v072_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_126d_63d_jerk_v073_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_189d_126d_jerk_v074_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_252d_252d_jerk_v075_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_378d_5d_jerk_v076_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_504d_21d_jerk_v077_signal,
    f38mdi_f38_margin_durability_input_passema_63d_63d_jerk_v078_signal,
    f38mdi_f38_margin_durability_input_passema_126d_126d_jerk_v079_signal,
    f38mdi_f38_margin_durability_input_passema_252d_252d_jerk_v080_signal,
    f38mdi_f38_margin_durability_input_passema_378d_5d_jerk_v081_signal,
    f38mdi_f38_margin_durability_input_passema_504d_21d_jerk_v082_signal,
    f38mdi_f38_margin_durability_input_resilsq_5d_63d_jerk_v083_signal,
    f38mdi_f38_margin_durability_input_resilsq_10d_126d_jerk_v084_signal,
    f38mdi_f38_margin_durability_input_resilsq_21d_252d_jerk_v085_signal,
    f38mdi_f38_margin_durability_input_resilsq_42d_5d_jerk_v086_signal,
    f38mdi_f38_margin_durability_input_resilsq_63d_21d_jerk_v087_signal,
    f38mdi_f38_margin_durability_input_resilsq_126d_63d_jerk_v088_signal,
    f38mdi_f38_margin_durability_input_resilsq_189d_126d_jerk_v089_signal,
    f38mdi_f38_margin_durability_input_resilsq_252d_252d_jerk_v090_signal,
    f38mdi_f38_margin_durability_input_resilsq_378d_5d_jerk_v091_signal,
    f38mdi_f38_margin_durability_input_resilsq_504d_21d_jerk_v092_signal,
    f38mdi_f38_margin_durability_input_composite_126d_63d_jerk_v093_signal,
    f38mdi_f38_margin_durability_input_composite_189d_126d_jerk_v094_signal,
    f38mdi_f38_margin_durability_input_composite_252d_252d_jerk_v095_signal,
    f38mdi_f38_margin_durability_input_composite_378d_5d_jerk_v096_signal,
    f38mdi_f38_margin_durability_input_composite_504d_21d_jerk_v097_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_5d_63d_jerk_v098_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_10d_126d_jerk_v099_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_21d_252d_jerk_v100_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_42d_5d_jerk_v101_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_63d_21d_jerk_v102_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_126d_63d_jerk_v103_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_189d_126d_jerk_v104_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_252d_252d_jerk_v105_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_378d_5d_jerk_v106_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_504d_21d_jerk_v107_signal,
    f38mdi_f38_margin_durability_input_resilema_5d_63d_jerk_v108_signal,
    f38mdi_f38_margin_durability_input_resilema_10d_126d_jerk_v109_signal,
    f38mdi_f38_margin_durability_input_resilema_21d_252d_jerk_v110_signal,
    f38mdi_f38_margin_durability_input_resilema_42d_5d_jerk_v111_signal,
    f38mdi_f38_margin_durability_input_resilema_63d_21d_jerk_v112_signal,
    f38mdi_f38_margin_durability_input_resilema_126d_63d_jerk_v113_signal,
    f38mdi_f38_margin_durability_input_resilema_189d_126d_jerk_v114_signal,
    f38mdi_f38_margin_durability_input_resilema_252d_252d_jerk_v115_signal,
    f38mdi_f38_margin_durability_input_resilema_378d_5d_jerk_v116_signal,
    f38mdi_f38_margin_durability_input_resilema_504d_21d_jerk_v117_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_5d_63d_jerk_v118_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_10d_126d_jerk_v119_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_21d_252d_jerk_v120_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_42d_5d_jerk_v121_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_63d_21d_jerk_v122_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_126d_63d_jerk_v123_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_189d_126d_jerk_v124_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_252d_252d_jerk_v125_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_378d_5d_jerk_v126_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_504d_21d_jerk_v127_signal,
    f38mdi_f38_margin_durability_input_passdiff_63d_63d_jerk_v128_signal,
    f38mdi_f38_margin_durability_input_passdiff_126d_126d_jerk_v129_signal,
    f38mdi_f38_margin_durability_input_passdiff_252d_252d_jerk_v130_signal,
    f38mdi_f38_margin_durability_input_passdiff_378d_5d_jerk_v131_signal,
    f38mdi_f38_margin_durability_input_passdiff_504d_21d_jerk_v132_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_21d_63d_jerk_v133_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_42d_126d_jerk_v134_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_63d_252d_jerk_v135_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_126d_5d_jerk_v136_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_252d_21d_jerk_v137_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_504d_63d_jerk_v138_signal,
    f38mdi_f38_margin_durability_input_resilcross_63v252_126d_jerk_v139_signal,
    f38mdi_f38_margin_durability_input_resilcross_126v504_252d_jerk_v140_signal,
    f38mdi_f38_margin_durability_input_resilcross_21v252_5d_jerk_v141_signal,
    f38mdi_f38_margin_durability_input_passxbuf_63d_21d_jerk_v142_signal,
    f38mdi_f38_margin_durability_input_passxbuf_126d_63d_jerk_v143_signal,
    f38mdi_f38_margin_durability_input_passxbuf_252d_126d_jerk_v144_signal,
    f38mdi_f38_margin_durability_input_passxbuf_378d_252d_jerk_v145_signal,
    f38mdi_f38_margin_durability_input_passxbuf_504d_5d_jerk_v146_signal,
    f38mdi_f38_margin_durability_input_passz_63_252_21d_jerk_v147_signal,
    f38mdi_f38_margin_durability_input_passz_126_252_63d_jerk_v148_signal,
    f38mdi_f38_margin_durability_input_passz_63_504_126d_jerk_v149_signal,
    f38mdi_f38_margin_durability_input_passz_126_504_252d_jerk_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_MARGIN_DURABILITY_INPUT_REGISTRY_JERK_001_150 = REGISTRY


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
    domain_primitives = ("_f38_input_pass_through", "_f38_margin_resilience", "_f38_input_buffer")
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
    print(f"OK f38_margin_durability_input_3rd_derivatives_001_150_claude: {n_features} features pass")
