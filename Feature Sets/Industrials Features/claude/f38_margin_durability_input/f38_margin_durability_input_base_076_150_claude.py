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


def f38mdi_f38_margin_durability_input_bufferdiff_378d_378d_base_v076_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    result = b.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferdiff_504d_504d_base_v077_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    result = b.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_63d_63d_base_v078_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_126d_126d_base_v079_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_252d_252d_base_v080_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_378d_378d_base_v081_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passema_504d_504d_base_v082_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    result = _ema(p, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_5d_5d_base_v083_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 5)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_10d_10d_base_v084_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 10)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_21d_21d_base_v085_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 21)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_42d_42d_base_v086_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 42)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_63d_63d_base_v087_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 63)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_126d_126d_base_v088_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 126)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_189d_189d_base_v089_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 189)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_252d_252d_base_v090_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 252)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_378d_378d_base_v091_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 378)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilsq_504d_504d_base_v092_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 504)
    result = r * r.abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_126d_126d_base_v093_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    r = _f38_margin_resilience(grossmargin, 126)
    result = (b + r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_189d_189d_base_v094_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    r = _f38_margin_resilience(grossmargin, 189)
    result = (b + r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_252d_252d_base_v095_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    r = _f38_margin_resilience(grossmargin, 252)
    result = (b + r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_378d_378d_base_v096_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    r = _f38_margin_resilience(grossmargin, 378)
    result = (b + r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_composite_504d_504d_base_v097_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    r = _f38_margin_resilience(grossmargin, 504)
    result = (b + r) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_5d_5d_base_v098_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 5)
    result = b * cor.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_10d_10d_base_v099_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 10)
    result = b * cor.pct_change(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_21d_21d_base_v100_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    result = b * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_42d_42d_base_v101_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    result = b * cor.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_63d_63d_base_v102_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    result = b * cor.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_126d_126d_base_v103_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    result = b * cor.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_189d_189d_base_v104_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    result = b * cor.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_252d_252d_base_v105_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    result = b * cor.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_378d_378d_base_v106_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    result = b * cor.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcor_504d_504d_base_v107_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    result = b * cor.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_5d_5d_base_v108_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 5)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_10d_10d_base_v109_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 10)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_21d_21d_base_v110_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 21)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_42d_42d_base_v111_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 42)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_63d_63d_base_v112_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 63)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_126d_126d_base_v113_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 126)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_189d_189d_base_v114_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 189)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_252d_252d_base_v115_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 252)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_378d_378d_base_v116_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 378)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilema_504d_504d_base_v117_signal(grossmargin, closeadj):
    r = _f38_margin_resilience(grossmargin, 504)
    result = _ema(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_5d_5d_base_v118_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 5)
    result = b * revenue.pct_change(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_10d_10d_base_v119_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 10)
    result = b * revenue.pct_change(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_21d_21d_base_v120_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    result = b * revenue.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_42d_42d_base_v121_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    result = b * revenue.pct_change(42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_63d_63d_base_v122_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    result = b * revenue.pct_change(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_126d_126d_base_v123_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    result = b * revenue.pct_change(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_189d_189d_base_v124_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 189)
    result = b * revenue.pct_change(189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_252d_252d_base_v125_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    result = b * revenue.pct_change(252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_378d_378d_base_v126_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 378)
    result = b * revenue.pct_change(378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxrevpct_504d_504d_base_v127_signal(grossmargin, cor, revenue, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    result = b * revenue.pct_change(504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_63d_63d_base_v128_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    result = p.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_126d_126d_base_v129_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    result = p.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_252d_252d_base_v130_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    result = p.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_378d_378d_base_v131_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    result = p.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passdiff_504d_504d_base_v132_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    result = p.diff(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_21d_21d_base_v133_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 21)
    result = b * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_42d_42d_base_v134_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 42)
    result = b * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_63d_63d_base_v135_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 63)
    result = b * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_126d_126d_base_v136_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 126)
    result = b * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_252d_252d_base_v137_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 252)
    result = b * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_bufferxcorpct_504d_504d_base_v138_signal(grossmargin, cor, closeadj):
    b = _f38_input_buffer(grossmargin, cor, 504)
    result = b * cor.pct_change(21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilcross_63v252_252d_base_v139_signal(grossmargin, closeadj):
    r1 = _f38_margin_resilience(grossmargin, 63)
    r2 = _f38_margin_resilience(grossmargin, 252)
    result = (r1 - r2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilcross_126v504_504d_base_v140_signal(grossmargin, closeadj):
    r1 = _f38_margin_resilience(grossmargin, 126)
    r2 = _f38_margin_resilience(grossmargin, 504)
    result = (r1 - r2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_resilcross_21v252_252d_base_v141_signal(grossmargin, closeadj):
    r1 = _f38_margin_resilience(grossmargin, 21)
    r2 = _f38_margin_resilience(grossmargin, 252)
    result = (r1 - r2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_63d_63d_base_v142_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    b = _f38_input_buffer(grossmargin, cor, 63)
    result = (p + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_126d_126d_base_v143_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    b = _f38_input_buffer(grossmargin, cor, 126)
    result = (p + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_252d_252d_base_v144_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 252)
    b = _f38_input_buffer(grossmargin, cor, 252)
    result = (p + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_378d_378d_base_v145_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 378)
    b = _f38_input_buffer(grossmargin, cor, 378)
    result = (p + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passxbuf_504d_504d_base_v146_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 504)
    b = _f38_input_buffer(grossmargin, cor, 504)
    result = (p + b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passz_63_252_252d_base_v147_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    result = _z(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passz_126_252_252d_base_v148_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    result = _z(p, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passz_63_504_504d_base_v149_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 63)
    result = _z(p, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

def f38mdi_f38_margin_durability_input_passz_126_504_504d_base_v150_signal(grossmargin, cor, revenue, closeadj):
    p = _f38_input_pass_through(grossmargin, cor, revenue, 126)
    result = _z(p, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)

_FEATURES = [
    f38mdi_f38_margin_durability_input_bufferdiff_378d_378d_base_v076_signal,
    f38mdi_f38_margin_durability_input_bufferdiff_504d_504d_base_v077_signal,
    f38mdi_f38_margin_durability_input_passema_63d_63d_base_v078_signal,
    f38mdi_f38_margin_durability_input_passema_126d_126d_base_v079_signal,
    f38mdi_f38_margin_durability_input_passema_252d_252d_base_v080_signal,
    f38mdi_f38_margin_durability_input_passema_378d_378d_base_v081_signal,
    f38mdi_f38_margin_durability_input_passema_504d_504d_base_v082_signal,
    f38mdi_f38_margin_durability_input_resilsq_5d_5d_base_v083_signal,
    f38mdi_f38_margin_durability_input_resilsq_10d_10d_base_v084_signal,
    f38mdi_f38_margin_durability_input_resilsq_21d_21d_base_v085_signal,
    f38mdi_f38_margin_durability_input_resilsq_42d_42d_base_v086_signal,
    f38mdi_f38_margin_durability_input_resilsq_63d_63d_base_v087_signal,
    f38mdi_f38_margin_durability_input_resilsq_126d_126d_base_v088_signal,
    f38mdi_f38_margin_durability_input_resilsq_189d_189d_base_v089_signal,
    f38mdi_f38_margin_durability_input_resilsq_252d_252d_base_v090_signal,
    f38mdi_f38_margin_durability_input_resilsq_378d_378d_base_v091_signal,
    f38mdi_f38_margin_durability_input_resilsq_504d_504d_base_v092_signal,
    f38mdi_f38_margin_durability_input_composite_126d_126d_base_v093_signal,
    f38mdi_f38_margin_durability_input_composite_189d_189d_base_v094_signal,
    f38mdi_f38_margin_durability_input_composite_252d_252d_base_v095_signal,
    f38mdi_f38_margin_durability_input_composite_378d_378d_base_v096_signal,
    f38mdi_f38_margin_durability_input_composite_504d_504d_base_v097_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_5d_5d_base_v098_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_10d_10d_base_v099_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_21d_21d_base_v100_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_42d_42d_base_v101_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_63d_63d_base_v102_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_126d_126d_base_v103_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_189d_189d_base_v104_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_252d_252d_base_v105_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_378d_378d_base_v106_signal,
    f38mdi_f38_margin_durability_input_bufferxcor_504d_504d_base_v107_signal,
    f38mdi_f38_margin_durability_input_resilema_5d_5d_base_v108_signal,
    f38mdi_f38_margin_durability_input_resilema_10d_10d_base_v109_signal,
    f38mdi_f38_margin_durability_input_resilema_21d_21d_base_v110_signal,
    f38mdi_f38_margin_durability_input_resilema_42d_42d_base_v111_signal,
    f38mdi_f38_margin_durability_input_resilema_63d_63d_base_v112_signal,
    f38mdi_f38_margin_durability_input_resilema_126d_126d_base_v113_signal,
    f38mdi_f38_margin_durability_input_resilema_189d_189d_base_v114_signal,
    f38mdi_f38_margin_durability_input_resilema_252d_252d_base_v115_signal,
    f38mdi_f38_margin_durability_input_resilema_378d_378d_base_v116_signal,
    f38mdi_f38_margin_durability_input_resilema_504d_504d_base_v117_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_5d_5d_base_v118_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_10d_10d_base_v119_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_21d_21d_base_v120_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_42d_42d_base_v121_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_63d_63d_base_v122_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_126d_126d_base_v123_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_189d_189d_base_v124_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_252d_252d_base_v125_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_378d_378d_base_v126_signal,
    f38mdi_f38_margin_durability_input_bufferxrevpct_504d_504d_base_v127_signal,
    f38mdi_f38_margin_durability_input_passdiff_63d_63d_base_v128_signal,
    f38mdi_f38_margin_durability_input_passdiff_126d_126d_base_v129_signal,
    f38mdi_f38_margin_durability_input_passdiff_252d_252d_base_v130_signal,
    f38mdi_f38_margin_durability_input_passdiff_378d_378d_base_v131_signal,
    f38mdi_f38_margin_durability_input_passdiff_504d_504d_base_v132_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_21d_21d_base_v133_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_42d_42d_base_v134_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_63d_63d_base_v135_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_126d_126d_base_v136_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_252d_252d_base_v137_signal,
    f38mdi_f38_margin_durability_input_bufferxcorpct_504d_504d_base_v138_signal,
    f38mdi_f38_margin_durability_input_resilcross_63v252_252d_base_v139_signal,
    f38mdi_f38_margin_durability_input_resilcross_126v504_504d_base_v140_signal,
    f38mdi_f38_margin_durability_input_resilcross_21v252_252d_base_v141_signal,
    f38mdi_f38_margin_durability_input_passxbuf_63d_63d_base_v142_signal,
    f38mdi_f38_margin_durability_input_passxbuf_126d_126d_base_v143_signal,
    f38mdi_f38_margin_durability_input_passxbuf_252d_252d_base_v144_signal,
    f38mdi_f38_margin_durability_input_passxbuf_378d_378d_base_v145_signal,
    f38mdi_f38_margin_durability_input_passxbuf_504d_504d_base_v146_signal,
    f38mdi_f38_margin_durability_input_passz_63_252_252d_base_v147_signal,
    f38mdi_f38_margin_durability_input_passz_126_252_252d_base_v148_signal,
    f38mdi_f38_margin_durability_input_passz_63_504_504d_base_v149_signal,
    f38mdi_f38_margin_durability_input_passz_126_504_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F38_MARGIN_DURABILITY_INPUT_REGISTRY_076_150 = REGISTRY


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
    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), f"nan_ok={nan_ok}/{n_features}"
    print(f"OK f38_margin_durability_input_base_076_150_claude: {n_features} features pass")
