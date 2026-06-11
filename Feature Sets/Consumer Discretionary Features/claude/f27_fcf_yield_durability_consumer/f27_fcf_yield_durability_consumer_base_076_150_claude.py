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
def _f27_fcf_yield(fcf, ev):
    return fcf / ev.replace(0, np.nan)


def _f27_fcf_yield_stability(fcf, ev, w):
    y = fcf / ev.replace(0, np.nan)
    return _mean(y, w) / _std(y, w).replace(0, np.nan)


def _f27_fcf_compound_quality(fcf, marketcap, w):
    yld = fcf / marketcap.replace(0, np.nan)
    return _mean(yld, w) - _std(yld, w)


# ===== features =====

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_rawx_10d_base_v076_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_mean42d_base_v077_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_std189d_base_v078_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_z378d_base_v079_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_rank252d_base_v080_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_abs10d_base_v081_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_sq42d_base_v082_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_max189d_base_v083_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_min378d_base_v084_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_rng252d_base_v085_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_med10d_base_v086_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_q7542d_base_v087_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_q25189d_base_v088_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_ema378d_base_v089_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_emastd252d_base_v090_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_diff10d_base_v091_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_pct42d_base_v092_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_log189d_base_v093_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_sign378d_base_v094_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_sum252d_base_v095_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_zsq10d_base_v096_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_centered42d_base_v097_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_ratio189d_base_v098_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_skew378d_base_v099_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_yldalt_kurt252d_base_v100_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield(fcf, ev)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_rawx_10d_base_v101_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_mean42d_base_v102_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_std189d_base_v103_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_z378d_base_v104_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_rank252d_base_v105_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_abs10d_base_v106_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_sq42d_base_v107_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_max189d_base_v108_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_min378d_base_v109_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_rng252d_base_v110_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_med10d_base_v111_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_q7542d_base_v112_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_q25189d_base_v113_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_ema378d_base_v114_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_emastd252d_base_v115_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_diff10d_base_v116_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_pct42d_base_v117_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_log189d_base_v118_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_sign378d_base_v119_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_sum252d_base_v120_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_zsq10d_base_v121_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_centered42d_base_v122_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_ratio189d_base_v123_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_skew378d_base_v124_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_stabalt_kurt252d_base_v125_signal(fcf, ev, closeadj):
    b = _f27_fcf_yield_stability(fcf, ev, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_rawx_10d_base_v126_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_mean42d_base_v127_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_std189d_base_v128_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_z378d_base_v129_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_rank252d_base_v130_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_abs10d_base_v131_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_sq42d_base_v132_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_max189d_base_v133_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_min378d_base_v134_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_rng252d_base_v135_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_med10d_base_v136_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_q7542d_base_v137_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_q25189d_base_v138_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_ema378d_base_v139_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_emastd252d_base_v140_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_diff10d_base_v141_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_pct42d_base_v142_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_log189d_base_v143_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_sign378d_base_v144_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_sum252d_base_v145_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_zsq10d_base_v146_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_centered42d_base_v147_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_ratio189d_base_v148_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_skew378d_base_v149_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f27fyd_f27_fcf_yield_durability_consumer_compalt_kurt252d_base_v150_signal(fcf, marketcap, closeadj):
    b = _f27_fcf_compound_quality(fcf, marketcap, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_rawx_10d_base_v076_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_mean42d_base_v077_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_std189d_base_v078_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_z378d_base_v079_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_rank252d_base_v080_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_abs10d_base_v081_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_sq42d_base_v082_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_max189d_base_v083_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_min378d_base_v084_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_rng252d_base_v085_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_med10d_base_v086_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_q7542d_base_v087_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_q25189d_base_v088_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_ema378d_base_v089_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_emastd252d_base_v090_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_diff10d_base_v091_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_pct42d_base_v092_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_log189d_base_v093_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_sign378d_base_v094_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_sum252d_base_v095_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_zsq10d_base_v096_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_centered42d_base_v097_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_ratio189d_base_v098_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_skew378d_base_v099_signal,
    f27fyd_f27_fcf_yield_durability_consumer_yldalt_kurt252d_base_v100_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_rawx_10d_base_v101_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_mean42d_base_v102_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_std189d_base_v103_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_z378d_base_v104_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_rank252d_base_v105_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_abs10d_base_v106_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_sq42d_base_v107_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_max189d_base_v108_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_min378d_base_v109_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_rng252d_base_v110_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_med10d_base_v111_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_q7542d_base_v112_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_q25189d_base_v113_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_ema378d_base_v114_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_emastd252d_base_v115_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_diff10d_base_v116_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_pct42d_base_v117_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_log189d_base_v118_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_sign378d_base_v119_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_sum252d_base_v120_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_zsq10d_base_v121_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_centered42d_base_v122_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_ratio189d_base_v123_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_skew378d_base_v124_signal,
    f27fyd_f27_fcf_yield_durability_consumer_stabalt_kurt252d_base_v125_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_rawx_10d_base_v126_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_mean42d_base_v127_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_std189d_base_v128_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_z378d_base_v129_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_rank252d_base_v130_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_abs10d_base_v131_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_sq42d_base_v132_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_max189d_base_v133_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_min378d_base_v134_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_rng252d_base_v135_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_med10d_base_v136_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_q7542d_base_v137_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_q25189d_base_v138_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_ema378d_base_v139_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_emastd252d_base_v140_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_diff10d_base_v141_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_pct42d_base_v142_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_log189d_base_v143_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_sign378d_base_v144_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_sum252d_base_v145_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_zsq10d_base_v146_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_centered42d_base_v147_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_ratio189d_base_v148_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_skew378d_base_v149_signal,
    f27fyd_f27_fcf_yield_durability_consumer_compalt_kurt252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F27_FCF_YIELD_DURABILITY_CONSUMER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    fcf       = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    debt      = pd.Series(6e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="debt")
    cashneq   = pd.Series(2.5e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.012, n))), name="cashneq")
    marketcap = pd.Series(closeadj * 1e8, name="marketcap")
    ev        = pd.Series(closeadj * 1.2e8 + debt - cashneq, name="ev")
    cols = {"closeadj": closeadj, "fcf": fcf, "ev": ev, "marketcap": marketcap}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f27_fcf_yield", "_f27_fcf_yield_stability", "_f27_fcf_compound_quality",)
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
    print(f"OK f27_fcf_yield_durability_consumer_base_076_150_claude: {n_features} features pass")
