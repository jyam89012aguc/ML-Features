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


# ===== folder domain primitives =====
def _f26_sga_to_revenue(sgna, revenue):
    return sgna / revenue.replace(0, np.nan)


def _f26_sga_growth_gap(sgna, revenue, w):
    g_sga = sgna.pct_change(periods=w)
    g_rev = revenue.pct_change(periods=w)
    return g_sga - g_rev


def _f26_sga_leverage(sgna, revenue, w):
    ratio = sgna / revenue.replace(0, np.nan)
    return _mean(ratio, w) - _std(ratio, w)


# ===== features =====

def f26slc_f26_sga_leverage_consumer_sgarevalt_rawx_10d_base_v076_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_mean42d_base_v077_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_std189d_base_v078_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_z378d_base_v079_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_rank252d_base_v080_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_abs10d_base_v081_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_sq42d_base_v082_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_max189d_base_v083_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_min378d_base_v084_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_rng252d_base_v085_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_med10d_base_v086_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_q7542d_base_v087_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_q25189d_base_v088_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_ema378d_base_v089_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_emastd252d_base_v090_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_diff10d_base_v091_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_pct42d_base_v092_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_log189d_base_v093_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_sign378d_base_v094_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_sum252d_base_v095_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_zsq10d_base_v096_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_centered42d_base_v097_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_ratio189d_base_v098_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_skew378d_base_v099_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_sgarevalt_kurt252d_base_v100_signal(sgna, revenue, closeadj):
    b = _f26_sga_to_revenue(sgna, revenue)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_rawx_10d_base_v101_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_mean42d_base_v102_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_std189d_base_v103_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_z378d_base_v104_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_rank252d_base_v105_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_abs10d_base_v106_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_sq42d_base_v107_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_max189d_base_v108_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_min378d_base_v109_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_rng252d_base_v110_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_med10d_base_v111_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_q7542d_base_v112_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_q25189d_base_v113_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_ema378d_base_v114_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_emastd252d_base_v115_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_diff10d_base_v116_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_pct42d_base_v117_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_log189d_base_v118_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_sign378d_base_v119_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_sum252d_base_v120_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_zsq10d_base_v121_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_centered42d_base_v122_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_ratio189d_base_v123_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_skew378d_base_v124_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_gapalt_kurt252d_base_v125_signal(sgna, revenue, closeadj):
    b = _f26_sga_growth_gap(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_rawx_10d_base_v126_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_mean42d_base_v127_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_std189d_base_v128_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_z378d_base_v129_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_rank252d_base_v130_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_abs10d_base_v131_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_sq42d_base_v132_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_max189d_base_v133_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_min378d_base_v134_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_rng252d_base_v135_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_med10d_base_v136_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_q7542d_base_v137_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_q25189d_base_v138_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_ema378d_base_v139_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_emastd252d_base_v140_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_diff10d_base_v141_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_pct42d_base_v142_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_log189d_base_v143_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_sign378d_base_v144_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_sum252d_base_v145_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_zsq10d_base_v146_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_centered42d_base_v147_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_ratio189d_base_v148_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_skew378d_base_v149_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f26slc_f26_sga_leverage_consumer_levalt_kurt252d_base_v150_signal(sgna, revenue, closeadj):
    b = _f26_sga_leverage(sgna, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f26slc_f26_sga_leverage_consumer_sgarevalt_rawx_10d_base_v076_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_mean42d_base_v077_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_std189d_base_v078_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_z378d_base_v079_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_rank252d_base_v080_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_abs10d_base_v081_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_sq42d_base_v082_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_max189d_base_v083_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_min378d_base_v084_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_rng252d_base_v085_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_med10d_base_v086_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_q7542d_base_v087_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_q25189d_base_v088_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_ema378d_base_v089_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_emastd252d_base_v090_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_diff10d_base_v091_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_pct42d_base_v092_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_log189d_base_v093_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_sign378d_base_v094_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_sum252d_base_v095_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_zsq10d_base_v096_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_centered42d_base_v097_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_ratio189d_base_v098_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_skew378d_base_v099_signal,
    f26slc_f26_sga_leverage_consumer_sgarevalt_kurt252d_base_v100_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_rawx_10d_base_v101_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_mean42d_base_v102_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_std189d_base_v103_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_z378d_base_v104_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_rank252d_base_v105_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_abs10d_base_v106_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_sq42d_base_v107_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_max189d_base_v108_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_min378d_base_v109_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_rng252d_base_v110_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_med10d_base_v111_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_q7542d_base_v112_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_q25189d_base_v113_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_ema378d_base_v114_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_emastd252d_base_v115_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_diff10d_base_v116_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_pct42d_base_v117_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_log189d_base_v118_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_sign378d_base_v119_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_sum252d_base_v120_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_zsq10d_base_v121_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_centered42d_base_v122_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_ratio189d_base_v123_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_skew378d_base_v124_signal,
    f26slc_f26_sga_leverage_consumer_gapalt_kurt252d_base_v125_signal,
    f26slc_f26_sga_leverage_consumer_levalt_rawx_10d_base_v126_signal,
    f26slc_f26_sga_leverage_consumer_levalt_mean42d_base_v127_signal,
    f26slc_f26_sga_leverage_consumer_levalt_std189d_base_v128_signal,
    f26slc_f26_sga_leverage_consumer_levalt_z378d_base_v129_signal,
    f26slc_f26_sga_leverage_consumer_levalt_rank252d_base_v130_signal,
    f26slc_f26_sga_leverage_consumer_levalt_abs10d_base_v131_signal,
    f26slc_f26_sga_leverage_consumer_levalt_sq42d_base_v132_signal,
    f26slc_f26_sga_leverage_consumer_levalt_max189d_base_v133_signal,
    f26slc_f26_sga_leverage_consumer_levalt_min378d_base_v134_signal,
    f26slc_f26_sga_leverage_consumer_levalt_rng252d_base_v135_signal,
    f26slc_f26_sga_leverage_consumer_levalt_med10d_base_v136_signal,
    f26slc_f26_sga_leverage_consumer_levalt_q7542d_base_v137_signal,
    f26slc_f26_sga_leverage_consumer_levalt_q25189d_base_v138_signal,
    f26slc_f26_sga_leverage_consumer_levalt_ema378d_base_v139_signal,
    f26slc_f26_sga_leverage_consumer_levalt_emastd252d_base_v140_signal,
    f26slc_f26_sga_leverage_consumer_levalt_diff10d_base_v141_signal,
    f26slc_f26_sga_leverage_consumer_levalt_pct42d_base_v142_signal,
    f26slc_f26_sga_leverage_consumer_levalt_log189d_base_v143_signal,
    f26slc_f26_sga_leverage_consumer_levalt_sign378d_base_v144_signal,
    f26slc_f26_sga_leverage_consumer_levalt_sum252d_base_v145_signal,
    f26slc_f26_sga_leverage_consumer_levalt_zsq10d_base_v146_signal,
    f26slc_f26_sga_leverage_consumer_levalt_centered42d_base_v147_signal,
    f26slc_f26_sga_leverage_consumer_levalt_ratio189d_base_v148_signal,
    f26slc_f26_sga_leverage_consumer_levalt_skew378d_base_v149_signal,
    f26slc_f26_sga_leverage_consumer_levalt_kurt252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F26_SGA_LEVERAGE_CONSUMER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    sgna    = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="sgna")
    opex    = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="opex")
    cols = {"closeadj": closeadj, "sgna": sgna, "revenue": revenue, "opex": opex}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f26_sga_to_revenue", "_f26_sga_growth_gap", "_f26_sga_leverage",)
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
    print(f"OK f26_sga_leverage_consumer_base_076_150_claude: {n_features} features pass")
