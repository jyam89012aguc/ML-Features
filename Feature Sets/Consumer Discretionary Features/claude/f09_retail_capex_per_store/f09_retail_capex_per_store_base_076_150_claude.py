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
    return s.ewm(span=w, min_periods=max(1, w // 2)).mean()


# ===== folder domain primitives =====
def _f09_capex_to_ppe(capex, ppnenet):
    return capex / ppnenet.replace(0, np.nan)


def _f09_renewal_intensity(capex, ppnenet, depamor):
    return (capex - depamor) / ppnenet.replace(0, np.nan)


def _f09_capex_store_ratio(capex, ppnenet, w):
    ratio = capex / ppnenet.replace(0, np.nan)
    return ratio.rolling(w, min_periods=max(1, w // 2)).mean()

def f09rcs_f09_retail_capex_per_store_renew_z_126d_base_v076_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _z(ri, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_189d_base_v077_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _z(ri, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_252d_base_v078_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _z(ri, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_378d_base_v079_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _z(ri, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_z_504d_base_v080_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _z(ri, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_5d_base_v081_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_10d_base_v082_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_21d_base_v083_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_42d_base_v084_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_63d_base_v085_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_126d_base_v086_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_189d_base_v087_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_252d_base_v088_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_378d_base_v089_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_ema_504d_base_v090_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = _ema(ri, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_5d_base_v091_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(5)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_10d_base_v092_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(10)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_21d_base_v093_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_42d_base_v094_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(42)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_63d_base_v095_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_126d_base_v096_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(126)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_189d_base_v097_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(189)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_252d_base_v098_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_378d_base_v099_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(378)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_renew_diff_504d_base_v100_signal(capex, ppnenet, depamor, closeadj):
    ri = _f09_renewal_intensity(capex, ppnenet, depamor)
    result = (ri - ri.shift(504)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_5d_base_v101_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_10d_base_v102_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_21d_base_v103_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_42d_base_v104_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_63d_base_v105_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_126d_base_v106_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_189d_base_v107_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_252d_base_v108_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_378d_base_v109_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_504d_base_v110_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    result = r * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_5d_base_v111_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_10d_base_v112_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_21d_base_v113_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_42d_base_v114_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_63d_base_v115_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_126d_base_v116_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_189d_base_v117_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_252d_base_v118_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_378d_base_v119_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_std_504d_base_v120_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    result = _std(r, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_5d_base_v121_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_10d_base_v122_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_21d_base_v123_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_42d_base_v124_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_63d_base_v125_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_126d_base_v126_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_189d_base_v127_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_252d_base_v128_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_378d_base_v129_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_z_504d_base_v130_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    result = _z(r, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_5d_base_v131_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_10d_base_v132_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_21d_base_v133_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_42d_base_v134_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_63d_base_v135_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_126d_base_v136_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_189d_base_v137_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_252d_base_v138_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_378d_base_v139_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_xdep_504d_base_v140_signal(capex, ppnenet, depamor, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    result = r * (depamor / 1e7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_5d_base_v141_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 5)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_10d_base_v142_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 10)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_21d_base_v143_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 21)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_42d_base_v144_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 42)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_63d_base_v145_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 63)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_126d_base_v146_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 126)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_189d_base_v147_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 189)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_252d_base_v148_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 252)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_378d_base_v149_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 378)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f09rcs_f09_retail_capex_per_store_csr_diff_504d_base_v150_signal(capex, ppnenet, closeadj):
    r = _f09_capex_store_ratio(capex, ppnenet, 504)
    result = (r - r.shift(21)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)



_FEATURES = [
    f09rcs_f09_retail_capex_per_store_renew_z_126d_base_v076_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_189d_base_v077_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_252d_base_v078_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_378d_base_v079_signal,
    f09rcs_f09_retail_capex_per_store_renew_z_504d_base_v080_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_5d_base_v081_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_10d_base_v082_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_21d_base_v083_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_42d_base_v084_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_63d_base_v085_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_126d_base_v086_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_189d_base_v087_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_252d_base_v088_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_378d_base_v089_signal,
    f09rcs_f09_retail_capex_per_store_renew_ema_504d_base_v090_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_5d_base_v091_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_10d_base_v092_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_21d_base_v093_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_42d_base_v094_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_63d_base_v095_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_126d_base_v096_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_189d_base_v097_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_252d_base_v098_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_378d_base_v099_signal,
    f09rcs_f09_retail_capex_per_store_renew_diff_504d_base_v100_signal,
    f09rcs_f09_retail_capex_per_store_csr_5d_base_v101_signal,
    f09rcs_f09_retail_capex_per_store_csr_10d_base_v102_signal,
    f09rcs_f09_retail_capex_per_store_csr_21d_base_v103_signal,
    f09rcs_f09_retail_capex_per_store_csr_42d_base_v104_signal,
    f09rcs_f09_retail_capex_per_store_csr_63d_base_v105_signal,
    f09rcs_f09_retail_capex_per_store_csr_126d_base_v106_signal,
    f09rcs_f09_retail_capex_per_store_csr_189d_base_v107_signal,
    f09rcs_f09_retail_capex_per_store_csr_252d_base_v108_signal,
    f09rcs_f09_retail_capex_per_store_csr_378d_base_v109_signal,
    f09rcs_f09_retail_capex_per_store_csr_504d_base_v110_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_5d_base_v111_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_10d_base_v112_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_21d_base_v113_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_42d_base_v114_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_63d_base_v115_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_126d_base_v116_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_189d_base_v117_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_252d_base_v118_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_378d_base_v119_signal,
    f09rcs_f09_retail_capex_per_store_csr_std_504d_base_v120_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_5d_base_v121_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_10d_base_v122_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_21d_base_v123_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_42d_base_v124_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_63d_base_v125_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_126d_base_v126_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_189d_base_v127_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_252d_base_v128_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_378d_base_v129_signal,
    f09rcs_f09_retail_capex_per_store_csr_z_504d_base_v130_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_5d_base_v131_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_10d_base_v132_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_21d_base_v133_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_42d_base_v134_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_63d_base_v135_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_126d_base_v136_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_189d_base_v137_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_252d_base_v138_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_378d_base_v139_signal,
    f09rcs_f09_retail_capex_per_store_csr_xdep_504d_base_v140_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_5d_base_v141_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_10d_base_v142_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_21d_base_v143_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_42d_base_v144_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_63d_base_v145_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_126d_base_v146_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_189d_base_v147_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_252d_base_v148_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_378d_base_v149_signal,
    f09rcs_f09_retail_capex_per_store_csr_diff_504d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F09_RETAIL_CAPEX_PER_STORE_REGISTRY_076_150 = REGISTRY


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
    inventory    = pd.Series(2e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.01, n))), name="inventory")
    ppnenet      = pd.Series(7e8 * np.exp(np.cumsum(np.random.normal(0.0002, 0.008, n))), name="ppnenet")

    cols = {
        "closeadj": closeadj, "high": high, "low": low, "volume": volume,
        "revenue": revenue, "ebitda": ebitda, "ebit": ebit, "netinc": netinc, "fcf": fcf,
        "ncfo": ncfo, "capex": capex, "depamor": depamor, "sgna": sgna, "opex": opex,
        "gp": gp, "cor": cor, "rnd": rnd,
        "inventory": inventory, "ppnenet": ppnenet,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f09_capex_to_ppe", "_f09_renewal_intensity", "_f09_capex_store_ratio")
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
    print(f"OK f09_retail_capex_per_store_076_150_claude: {n_features} features pass")
