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
    return s.ewm(span=w, min_periods=max(1, w // 2), adjust=False).mean()


# ===== folder domain primitives =====
def _f46_low_vol_signal(close, w):
    r = close.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std()
    inv_vol = 1.0 / vol.replace(0, np.nan)
    return inv_vol * close


def _f46_steady_earnings_growth(netinc, w):
    g = netinc.pct_change(periods=w)
    smooth = g.rolling(w, min_periods=max(1, w // 2)).mean()
    stab = g.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    return smooth / stab


def _f46_compounder_composite(close, netinc, w):
    r = close.pct_change()
    vol = r.rolling(w, min_periods=max(1, w // 2)).std().replace(0, np.nan)
    g = netinc.pct_change(periods=w).rolling(w, min_periods=max(1, w // 2)).mean()
    return (g / vol) * close



# ===== features =====

def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_126d_base_v076_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_126d_base_v077_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_126d_base_v078_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 126)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_189d_base_v079_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_189d_base_v080_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_189d_base_v081_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 189)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_252d_base_v082_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_252d_base_v083_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_252d_base_v084_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 252)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_378d_base_v085_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_378d_base_v086_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_378d_base_v087_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 378)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_504d_base_v088_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 504)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_504d_base_v089_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 504)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_504d_base_v090_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 504)) * _mean(closeadj, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_5d_base_v091_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_5d_base_v092_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_5d_base_v093_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 5)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_10d_base_v094_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_10d_base_v095_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_10d_base_v096_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 10)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_21d_base_v097_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_21d_base_v098_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_21d_base_v099_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 21)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_42d_base_v100_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_42d_base_v101_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_42d_base_v102_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 42)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_63d_base_v103_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_63d_base_v104_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_63d_base_v105_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 63)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_126d_base_v106_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_126d_base_v107_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_126d_base_v108_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 126)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_189d_base_v109_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 189)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_189d_base_v110_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 189)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_189d_base_v111_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 189)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_252d_base_v112_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_252d_base_v113_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_252d_base_v114_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 252)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_378d_base_v115_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 378)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_378d_base_v116_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 378)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_378d_base_v117_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 378)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_504d_base_v118_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 504)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_504d_base_v119_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 504)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_504d_base_v120_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 504)) * _mean(closeadj, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_5d_base_v121_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_5d_base_v122_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_5d_base_v123_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 5)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_10d_base_v124_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_10d_base_v125_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_10d_base_v126_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 10)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_21d_base_v127_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_21d_base_v128_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_21d_base_v129_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 21)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_42d_base_v130_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_42d_base_v131_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_42d_base_v132_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 42)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_63d_base_v133_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_63d_base_v134_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_63d_base_v135_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 63)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_126d_base_v136_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_126d_base_v137_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_126d_base_v138_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 126)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_189d_base_v139_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_189d_base_v140_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_189d_base_v141_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 189)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_252d_base_v142_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_252d_base_v143_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_252d_base_v144_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 252)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_378d_base_v145_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_378d_base_v146_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_378d_base_v147_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 378)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_504d_base_v148_signal(closeadj):
    result = (_f46_low_vol_signal(closeadj, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_504d_base_v149_signal(netinc, closeadj):
    result = (_f46_steady_earnings_growth(netinc, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_504d_base_v150_signal(closeadj, netinc):
    result = (_f46_compounder_composite(closeadj, netinc, 504)) * _mean(closeadj, 126)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_126d_base_v076_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_126d_base_v077_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_126d_base_v078_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_189d_base_v079_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_189d_base_v080_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_189d_base_v081_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_252d_base_v082_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_252d_base_v083_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_252d_base_v084_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_378d_base_v085_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_378d_base_v086_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_378d_base_v087_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose63_504d_base_v088_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose63_504d_base_v089_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose63_504d_base_v090_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_5d_base_v091_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_5d_base_v092_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_5d_base_v093_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_10d_base_v094_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_10d_base_v095_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_10d_base_v096_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_21d_base_v097_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_21d_base_v098_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_21d_base_v099_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_42d_base_v100_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_42d_base_v101_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_42d_base_v102_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_63d_base_v103_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_63d_base_v104_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_63d_base_v105_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_126d_base_v106_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_126d_base_v107_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_126d_base_v108_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_189d_base_v109_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_189d_base_v110_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_189d_base_v111_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_252d_base_v112_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_252d_base_v113_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_252d_base_v114_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_378d_base_v115_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_378d_base_v116_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_378d_base_v117_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose5_504d_base_v118_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose5_504d_base_v119_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose5_504d_base_v120_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_5d_base_v121_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_5d_base_v122_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_5d_base_v123_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_10d_base_v124_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_10d_base_v125_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_10d_base_v126_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_21d_base_v127_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_21d_base_v128_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_21d_base_v129_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_42d_base_v130_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_42d_base_v131_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_42d_base_v132_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_63d_base_v133_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_63d_base_v134_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_63d_base_v135_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_126d_base_v136_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_126d_base_v137_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_126d_base_v138_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_189d_base_v139_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_189d_base_v140_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_189d_base_v141_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_252d_base_v142_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_252d_base_v143_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_252d_base_v144_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_378d_base_v145_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_378d_base_v146_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_378d_base_v147_signal,
    f46qmc_f46_quiet_medtech_compounder_p1_raw_xclose126_504d_base_v148_signal,
    f46qmc_f46_quiet_medtech_compounder_p2_raw_xclose126_504d_base_v149_signal,
    f46qmc_f46_quiet_medtech_compounder_p3_raw_xclose126_504d_base_v150_signal,
]

def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F46_QUIET_MEDTECH_COMPOUNDER_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    high = closeadj * (1.0 + np.abs(np.random.normal(0, 0.01, n)))
    low = closeadj * (1.0 - np.abs(np.random.normal(0, 0.01, n)))
    high = pd.Series(high.values, name="high")
    low = pd.Series(low.values, name="low")
    volume = pd.Series(np.abs(np.random.normal(1e6, 3e5, n)), name="volume")

    revenue = pd.Series(1e9 * np.exp(np.cumsum(np.random.normal(0.0003, 0.01, n))), name="revenue")
    ebitda  = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.012, n))), name="ebitda")
    netinc  = pd.Series(1e8 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="netinc")
    fcf     = pd.Series(8e7 * np.exp(np.cumsum(np.random.normal(0.0003, 0.015, n))), name="fcf")
    eps     = pd.Series(1.0 + 0.5*np.cumsum(np.random.normal(0.0003, 0.01, n))/np.arange(1,n+1), name="eps")
    grossmargin  = pd.Series(0.30 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="grossmargin")
    ebitdamargin = pd.Series(0.20 + 0.05*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="ebitdamargin")
    roic         = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "netinc": netinc, "fcf": fcf,
        "eps": eps, "grossmargin": grossmargin, "ebitdamargin": ebitdamargin, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f46_low_vol_signal", "_f46_steady_earnings_growth", "_f46_compounder_composite")
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
    print(f"OK f46_quiet_medtech_compounder_base_076_150_claude: {n_features} features pass")
