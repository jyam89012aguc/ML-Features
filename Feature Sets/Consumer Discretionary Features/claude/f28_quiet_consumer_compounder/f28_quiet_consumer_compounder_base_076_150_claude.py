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
def _f28_low_vol_signal(closeadj, w):
    rets = closeadj.pct_change()
    return -_std(rets, w)


def _f28_steady_earnings_growth(netinc, w):
    g = netinc.pct_change(periods=w)
    return _mean(g, w) - _std(g, w)


def _f28_compounder_composite(closeadj, netinc, w):
    rets = closeadj.pct_change()
    vol = _std(rets, w)
    g = netinc.pct_change(periods=w)
    return _mean(g, w) / vol.replace(0, np.nan)


# ===== features =====

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_rawx_10d_base_v076_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_mean42d_base_v077_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_std189d_base_v078_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_z378d_base_v079_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_rank252d_base_v080_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_abs10d_base_v081_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_sq42d_base_v082_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_max189d_base_v083_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_min378d_base_v084_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_rng252d_base_v085_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_med10d_base_v086_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_q7542d_base_v087_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_q25189d_base_v088_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_ema378d_base_v089_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_emastd252d_base_v090_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_diff10d_base_v091_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_pct42d_base_v092_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_log189d_base_v093_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_sign378d_base_v094_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_sum252d_base_v095_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_zsq10d_base_v096_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_centered42d_base_v097_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_ratio189d_base_v098_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_skew378d_base_v099_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_lowvolalt_kurt252d_base_v100_signal(closeadj):
    b = _f28_low_vol_signal(closeadj, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_rawx_10d_base_v101_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_mean42d_base_v102_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_std189d_base_v103_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_z378d_base_v104_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_rank252d_base_v105_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_abs10d_base_v106_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_sq42d_base_v107_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_max189d_base_v108_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_min378d_base_v109_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_rng252d_base_v110_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_med10d_base_v111_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_q7542d_base_v112_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_q25189d_base_v113_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_ema378d_base_v114_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_emastd252d_base_v115_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_diff10d_base_v116_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_pct42d_base_v117_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_log189d_base_v118_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_sign378d_base_v119_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_sum252d_base_v120_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_zsq10d_base_v121_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_centered42d_base_v122_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_ratio189d_base_v123_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_skew378d_base_v124_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_egalt_kurt252d_base_v125_signal(netinc, closeadj):
    b = _f28_steady_earnings_growth(netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_rawx_10d_base_v126_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    out = b * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_mean42d_base_v127_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    out = _mean(b, 42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_std189d_base_v128_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    out = _std(b, 189) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_z378d_base_v129_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    out = _z(b, 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_rank252d_base_v130_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).rank(pct=True) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_abs10d_base_v131_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    out = b.abs().rolling(10, min_periods=max(5, 10//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_sq42d_base_v132_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    out = (b * b.abs()).rolling(42, min_periods=max(5, 42//4)).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_max189d_base_v133_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).max() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_min378d_base_v134_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).min() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_rng252d_base_v135_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = (b.rolling(252, min_periods=max(5, 252//4)).max() - b.rolling(252, min_periods=max(5, 252//4)).min()) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_med10d_base_v136_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    out = b.rolling(10, min_periods=max(5, 10//4)).median() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_q7542d_base_v137_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    out = b.rolling(42, min_periods=max(5, 42//4)).quantile(0.75) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_q25189d_base_v138_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    out = b.rolling(189, min_periods=max(5, 189//4)).quantile(0.25) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_ema378d_base_v139_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    out = b.ewm(span=378, adjust=False).mean() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_emastd252d_base_v140_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = b.ewm(span=252, adjust=False).std() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_diff10d_base_v141_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    out = b.diff(periods=10) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_pct42d_base_v142_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    out = b.pct_change(periods=42) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_log189d_base_v143_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    out = np.log(b.abs().replace(0, np.nan)) * closeadj + _mean(b, 189) * 0.0
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_sign378d_base_v144_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    out = np.sign(b) * _mean(b.abs(), 378) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_sum252d_base_v145_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).sum() * closeadj / 252
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_zsq10d_base_v146_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 10)
    out = _z(b, 10) * _z(b, 10).abs() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_centered42d_base_v147_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 42)
    out = (b - _mean(b, 42)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_ratio189d_base_v148_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 189)
    out = (b / _mean(b, 189).replace(0, np.nan)) * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_skew378d_base_v149_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 378)
    out = b.rolling(378, min_periods=max(5, 378//4)).skew() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)

def f28qcc_f28_quiet_consumer_compounder_compalt_kurt252d_base_v150_signal(closeadj, netinc):
    b = _f28_compounder_composite(closeadj, netinc, 252)
    out = b.rolling(252, min_periods=max(5, 252//4)).kurt() * closeadj
    result = out
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_rawx_10d_base_v076_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_mean42d_base_v077_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_std189d_base_v078_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_z378d_base_v079_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_rank252d_base_v080_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_abs10d_base_v081_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_sq42d_base_v082_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_max189d_base_v083_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_min378d_base_v084_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_rng252d_base_v085_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_med10d_base_v086_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_q7542d_base_v087_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_q25189d_base_v088_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_ema378d_base_v089_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_emastd252d_base_v090_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_diff10d_base_v091_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_pct42d_base_v092_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_log189d_base_v093_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_sign378d_base_v094_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_sum252d_base_v095_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_zsq10d_base_v096_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_centered42d_base_v097_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_ratio189d_base_v098_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_skew378d_base_v099_signal,
    f28qcc_f28_quiet_consumer_compounder_lowvolalt_kurt252d_base_v100_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_rawx_10d_base_v101_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_mean42d_base_v102_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_std189d_base_v103_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_z378d_base_v104_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_rank252d_base_v105_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_abs10d_base_v106_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_sq42d_base_v107_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_max189d_base_v108_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_min378d_base_v109_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_rng252d_base_v110_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_med10d_base_v111_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_q7542d_base_v112_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_q25189d_base_v113_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_ema378d_base_v114_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_emastd252d_base_v115_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_diff10d_base_v116_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_pct42d_base_v117_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_log189d_base_v118_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_sign378d_base_v119_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_sum252d_base_v120_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_zsq10d_base_v121_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_centered42d_base_v122_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_ratio189d_base_v123_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_skew378d_base_v124_signal,
    f28qcc_f28_quiet_consumer_compounder_egalt_kurt252d_base_v125_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_rawx_10d_base_v126_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_mean42d_base_v127_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_std189d_base_v128_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_z378d_base_v129_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_rank252d_base_v130_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_abs10d_base_v131_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_sq42d_base_v132_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_max189d_base_v133_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_min378d_base_v134_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_rng252d_base_v135_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_med10d_base_v136_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_q7542d_base_v137_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_q25189d_base_v138_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_ema378d_base_v139_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_emastd252d_base_v140_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_diff10d_base_v141_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_pct42d_base_v142_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_log189d_base_v143_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_sign378d_base_v144_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_sum252d_base_v145_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_zsq10d_base_v146_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_centered42d_base_v147_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_ratio189d_base_v148_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_skew378d_base_v149_signal,
    f28qcc_f28_quiet_consumer_compounder_compalt_kurt252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values() if p.default is inspect.Parameter.empty]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F28_QUIET_CONSUMER_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    netinc = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    ebitda = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    eps    = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1, n+1), name="eps")
    cols = {"closeadj": closeadj, "netinc": netinc, "ebitda": ebitda, "eps": eps}

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f28_low_vol_signal", "_f28_steady_earnings_growth", "_f28_compounder_composite",)
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
    print(f"OK f28_quiet_consumer_compounder_base_076_150_claude: {n_features} features pass")
