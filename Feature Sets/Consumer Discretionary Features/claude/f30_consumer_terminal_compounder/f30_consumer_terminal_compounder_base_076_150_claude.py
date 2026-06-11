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
def _f30_quality_composite(roic, fcf, revenue, w):
    fcfm = fcf / revenue.replace(0, np.nan)
    return _mean(roic, w) + _mean(fcfm, w) + _mean(revenue.pct_change(periods=w), w)


def _f30_terminal_score(roic, ebitdamargin, w):
    return _mean(roic, w) * _mean(ebitdamargin, w)


def _f30_terminal_quality(fcf, revenue, roic, w):
    fcfm = fcf / revenue.replace(0, np.nan)
    return _mean(fcfm, w) * _mean(roic, w)


# ===== features =====

def f30ctc_f30_consumer_terminal_compounder_qcompalt_rawx_10d_base_v076_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_mean42d_base_v077_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_std189d_base_v078_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_z378d_base_v079_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_rank252d_base_v080_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_abs10d_base_v081_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_sq42d_base_v082_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_max189d_base_v083_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_min378d_base_v084_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_rng252d_base_v085_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_med10d_base_v086_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_q7542d_base_v087_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_q25189d_base_v088_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_ema378d_base_v089_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_emastd252d_base_v090_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_diff10d_base_v091_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_pct42d_base_v092_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_log189d_base_v093_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_sign378d_base_v094_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_sum252d_base_v095_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_zsq10d_base_v096_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_centered42d_base_v097_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_ratio189d_base_v098_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_skew378d_base_v099_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_qcompalt_kurt252d_base_v100_signal(roic, fcf, revenue, closeadj):
    b = _f30_quality_composite(roic, fcf, revenue, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_rawx_10d_base_v101_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_mean42d_base_v102_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_std189d_base_v103_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_z378d_base_v104_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_rank252d_base_v105_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_abs10d_base_v106_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_sq42d_base_v107_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_max189d_base_v108_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_min378d_base_v109_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_rng252d_base_v110_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_med10d_base_v111_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_q7542d_base_v112_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_q25189d_base_v113_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_ema378d_base_v114_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_emastd252d_base_v115_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_diff10d_base_v116_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_pct42d_base_v117_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_log189d_base_v118_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_sign378d_base_v119_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_sum252d_base_v120_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_zsq10d_base_v121_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_centered42d_base_v122_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_ratio189d_base_v123_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_skew378d_base_v124_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tscralt_kurt252d_base_v125_signal(roic, ebitdamargin, closeadj):
    b = _f30_terminal_score(roic, ebitdamargin, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_rawx_10d_base_v126_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_mean42d_base_v127_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_std189d_base_v128_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_z378d_base_v129_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_rank252d_base_v130_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_abs10d_base_v131_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_sq42d_base_v132_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_max189d_base_v133_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_min378d_base_v134_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_rng252d_base_v135_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_med10d_base_v136_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_q7542d_base_v137_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_q25189d_base_v138_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_ema378d_base_v139_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_emastd252d_base_v140_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_diff10d_base_v141_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_pct42d_base_v142_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_log189d_base_v143_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_sign378d_base_v144_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_sum252d_base_v145_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_zsq10d_base_v146_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_centered42d_base_v147_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_ratio189d_base_v148_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_skew378d_base_v149_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f30ctc_f30_consumer_terminal_compounder_tqualalt_kurt252d_base_v150_signal(fcf, revenue, roic, closeadj):
    b = _f30_terminal_quality(fcf, revenue, roic, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f30ctc_f30_consumer_terminal_compounder_qcompalt_rawx_10d_base_v076_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_mean42d_base_v077_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_std189d_base_v078_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_z378d_base_v079_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_rank252d_base_v080_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_abs10d_base_v081_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_sq42d_base_v082_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_max189d_base_v083_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_min378d_base_v084_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_rng252d_base_v085_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_med10d_base_v086_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_q7542d_base_v087_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_q25189d_base_v088_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_ema378d_base_v089_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_emastd252d_base_v090_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_diff10d_base_v091_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_pct42d_base_v092_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_log189d_base_v093_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_sign378d_base_v094_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_sum252d_base_v095_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_zsq10d_base_v096_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_centered42d_base_v097_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_ratio189d_base_v098_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_skew378d_base_v099_signal,
    f30ctc_f30_consumer_terminal_compounder_qcompalt_kurt252d_base_v100_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_rawx_10d_base_v101_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_mean42d_base_v102_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_std189d_base_v103_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_z378d_base_v104_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_rank252d_base_v105_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_abs10d_base_v106_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_sq42d_base_v107_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_max189d_base_v108_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_min378d_base_v109_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_rng252d_base_v110_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_med10d_base_v111_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_q7542d_base_v112_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_q25189d_base_v113_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_ema378d_base_v114_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_emastd252d_base_v115_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_diff10d_base_v116_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_pct42d_base_v117_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_log189d_base_v118_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_sign378d_base_v119_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_sum252d_base_v120_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_zsq10d_base_v121_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_centered42d_base_v122_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_ratio189d_base_v123_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_skew378d_base_v124_signal,
    f30ctc_f30_consumer_terminal_compounder_tscralt_kurt252d_base_v125_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_rawx_10d_base_v126_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_mean42d_base_v127_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_std189d_base_v128_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_z378d_base_v129_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_rank252d_base_v130_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_abs10d_base_v131_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_sq42d_base_v132_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_max189d_base_v133_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_min378d_base_v134_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_rng252d_base_v135_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_med10d_base_v136_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_q7542d_base_v137_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_q25189d_base_v138_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_ema378d_base_v139_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_emastd252d_base_v140_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_diff10d_base_v141_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_pct42d_base_v142_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_log189d_base_v143_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_sign378d_base_v144_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_sum252d_base_v145_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_zsq10d_base_v146_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_centered42d_base_v147_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_ratio189d_base_v148_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_skew378d_base_v149_signal,
    f30ctc_f30_consumer_terminal_compounder_tqualalt_kurt252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F30_CONSUMER_TERMINAL_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    revenue      = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    fcf          = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    ebitda       = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    cols = {"closeadj": closeadj, "revenue": revenue, "fcf": fcf, "ebitda": ebitda, "roic": roic, "ebitdamargin": ebitdamargin}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f30_quality_composite", "_f30_terminal_score", "_f30_terminal_quality",)
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
    print(f"OK f30_consumer_terminal_compounder_base_076_150_claude: {n_features} features pass")
