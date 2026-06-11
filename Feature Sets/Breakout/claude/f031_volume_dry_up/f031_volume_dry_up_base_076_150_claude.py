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
def _f031_vol_ratio(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return volume / avg.replace(0, np.nan)


def _f031_dry_up_signal(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    r = volume / avg.replace(0, np.nan)
    return (1.0 / r.replace(0, np.nan)) - 1.0


def _f031_selling_exhaustion(volume, closeadj, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    ratio = volume / avg.replace(0, np.nan)
    ret = closeadj.pct_change()
    down = (ret < 0).astype(float)
    return (1.0 - ratio).clip(lower=-5, upper=5) * down * closeadj


def f031vdu_f031_volume_dry_up_stdvolratio_126d_base_v076_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    result = _std(r, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_189d_base_v077_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 189)
    result = _std(r, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_252d_base_v078_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    result = _std(r, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_378d_base_v079_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 378)
    result = _std(r, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_stdvolratio_504d_base_v080_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 504)
    result = _std(r, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_5d_base_v081_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 5)
    result = _mean(d, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_10d_base_v082_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 10)
    result = _mean(d, 5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_21d_base_v083_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    result = _mean(d, 7) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_42d_base_v084_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 42)
    result = _mean(d, 14) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_63d_base_v085_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    result = _mean(d, 21) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_126d_base_v086_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    result = _mean(d, 42) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_189d_base_v087_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 189)
    result = _mean(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_252d_base_v088_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    result = _mean(d, 84) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_378d_base_v089_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 378)
    result = _mean(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smdryup_504d_base_v090_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 504)
    result = _mean(d, 168) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_5d_base_v091_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 5)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_10d_base_v092_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 10)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_21d_base_v093_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_42d_base_v094_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 42)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_63d_base_v095_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    result = _z(d, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_126d_base_v096_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    result = _z(d, 126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_189d_base_v097_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 189)
    result = _z(d, 189) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_252d_base_v098_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    result = _z(d, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_378d_base_v099_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 378)
    result = _z(d, 378) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zdryup_504d_base_v100_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 504)
    result = _z(d, 504) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_5d_base_v101_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 5)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_10d_base_v102_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 10)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_21d_base_v103_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_42d_base_v104_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 42)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_63d_base_v105_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_126d_base_v106_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_189d_base_v107_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 189)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_252d_base_v108_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_378d_base_v109_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 378)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_sqdryup_504d_base_v110_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 504)
    result = (d * d) * closeadj * np.sign(d)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_5d_base_v111_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 5)
    result = _mean(s, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_10d_base_v112_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 10)
    result = _mean(s, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_21d_base_v113_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 21)
    result = _mean(s, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_42d_base_v114_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 42)
    result = _mean(s, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_63d_base_v115_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 63)
    result = _mean(s, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_126d_base_v116_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 126)
    result = _mean(s, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_189d_base_v117_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 189)
    result = _mean(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_252d_base_v118_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    result = _mean(s, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_378d_base_v119_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 378)
    result = _mean(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_smsellexh_504d_base_v120_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 504)
    result = _mean(s, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_5d_base_v121_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 5)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_10d_base_v122_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 10)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_21d_base_v123_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 21)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_42d_base_v124_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 42)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_63d_base_v125_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 63)
    result = _z(s, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_126d_base_v126_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 126)
    result = _z(s, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_189d_base_v127_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 189)
    result = _z(s, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_252d_base_v128_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 252)
    result = _z(s, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_378d_base_v129_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 378)
    result = _z(s, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_zsellexh_504d_base_v130_signal(volume, closeadj):
    s = _f031_selling_exhaustion(volume, closeadj, 504)
    result = _z(s, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_5d_base_v131_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 5)
    dv = closeadj * volume
    result = d * _mean(dv, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_10d_base_v132_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 10)
    dv = closeadj * volume
    result = d * _mean(dv, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_21d_base_v133_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 21)
    dv = closeadj * volume
    result = d * _mean(dv, 10)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_42d_base_v134_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 42)
    dv = closeadj * volume
    result = d * _mean(dv, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_63d_base_v135_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 63)
    dv = closeadj * volume
    result = d * _mean(dv, 31)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_126d_base_v136_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 126)
    dv = closeadj * volume
    result = d * _mean(dv, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_189d_base_v137_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 189)
    dv = closeadj * volume
    result = d * _mean(dv, 94)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_252d_base_v138_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 252)
    dv = closeadj * volume
    result = d * _mean(dv, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_378d_base_v139_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 378)
    dv = closeadj * volume
    result = d * _mean(dv, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_dryupxdv_504d_base_v140_signal(volume, closeadj):
    d = _f031_dry_up_signal(volume, 504)
    dv = closeadj * volume
    result = d * _mean(dv, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_5d_base_v141_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 5)
    result = r.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_10d_base_v142_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 10)
    result = r.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_21d_base_v143_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 21)
    result = r.diff(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_42d_base_v144_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 42)
    result = r.diff(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_63d_base_v145_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 63)
    result = r.diff(15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_126d_base_v146_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 126)
    result = r.diff(31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_189d_base_v147_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 189)
    result = r.diff(47) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_252d_base_v148_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 252)
    result = r.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_378d_base_v149_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 378)
    result = r.diff(94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f031vdu_f031_volume_dry_up_diffvolratio_504d_base_v150_signal(volume, closeadj):
    r = _f031_vol_ratio(volume, 504)
    result = r.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f031vdu_f031_volume_dry_up_stdvolratio_126d_base_v076_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_189d_base_v077_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_252d_base_v078_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_378d_base_v079_signal,
    f031vdu_f031_volume_dry_up_stdvolratio_504d_base_v080_signal,
    f031vdu_f031_volume_dry_up_smdryup_5d_base_v081_signal,
    f031vdu_f031_volume_dry_up_smdryup_10d_base_v082_signal,
    f031vdu_f031_volume_dry_up_smdryup_21d_base_v083_signal,
    f031vdu_f031_volume_dry_up_smdryup_42d_base_v084_signal,
    f031vdu_f031_volume_dry_up_smdryup_63d_base_v085_signal,
    f031vdu_f031_volume_dry_up_smdryup_126d_base_v086_signal,
    f031vdu_f031_volume_dry_up_smdryup_189d_base_v087_signal,
    f031vdu_f031_volume_dry_up_smdryup_252d_base_v088_signal,
    f031vdu_f031_volume_dry_up_smdryup_378d_base_v089_signal,
    f031vdu_f031_volume_dry_up_smdryup_504d_base_v090_signal,
    f031vdu_f031_volume_dry_up_zdryup_5d_base_v091_signal,
    f031vdu_f031_volume_dry_up_zdryup_10d_base_v092_signal,
    f031vdu_f031_volume_dry_up_zdryup_21d_base_v093_signal,
    f031vdu_f031_volume_dry_up_zdryup_42d_base_v094_signal,
    f031vdu_f031_volume_dry_up_zdryup_63d_base_v095_signal,
    f031vdu_f031_volume_dry_up_zdryup_126d_base_v096_signal,
    f031vdu_f031_volume_dry_up_zdryup_189d_base_v097_signal,
    f031vdu_f031_volume_dry_up_zdryup_252d_base_v098_signal,
    f031vdu_f031_volume_dry_up_zdryup_378d_base_v099_signal,
    f031vdu_f031_volume_dry_up_zdryup_504d_base_v100_signal,
    f031vdu_f031_volume_dry_up_sqdryup_5d_base_v101_signal,
    f031vdu_f031_volume_dry_up_sqdryup_10d_base_v102_signal,
    f031vdu_f031_volume_dry_up_sqdryup_21d_base_v103_signal,
    f031vdu_f031_volume_dry_up_sqdryup_42d_base_v104_signal,
    f031vdu_f031_volume_dry_up_sqdryup_63d_base_v105_signal,
    f031vdu_f031_volume_dry_up_sqdryup_126d_base_v106_signal,
    f031vdu_f031_volume_dry_up_sqdryup_189d_base_v107_signal,
    f031vdu_f031_volume_dry_up_sqdryup_252d_base_v108_signal,
    f031vdu_f031_volume_dry_up_sqdryup_378d_base_v109_signal,
    f031vdu_f031_volume_dry_up_sqdryup_504d_base_v110_signal,
    f031vdu_f031_volume_dry_up_smsellexh_5d_base_v111_signal,
    f031vdu_f031_volume_dry_up_smsellexh_10d_base_v112_signal,
    f031vdu_f031_volume_dry_up_smsellexh_21d_base_v113_signal,
    f031vdu_f031_volume_dry_up_smsellexh_42d_base_v114_signal,
    f031vdu_f031_volume_dry_up_smsellexh_63d_base_v115_signal,
    f031vdu_f031_volume_dry_up_smsellexh_126d_base_v116_signal,
    f031vdu_f031_volume_dry_up_smsellexh_189d_base_v117_signal,
    f031vdu_f031_volume_dry_up_smsellexh_252d_base_v118_signal,
    f031vdu_f031_volume_dry_up_smsellexh_378d_base_v119_signal,
    f031vdu_f031_volume_dry_up_smsellexh_504d_base_v120_signal,
    f031vdu_f031_volume_dry_up_zsellexh_5d_base_v121_signal,
    f031vdu_f031_volume_dry_up_zsellexh_10d_base_v122_signal,
    f031vdu_f031_volume_dry_up_zsellexh_21d_base_v123_signal,
    f031vdu_f031_volume_dry_up_zsellexh_42d_base_v124_signal,
    f031vdu_f031_volume_dry_up_zsellexh_63d_base_v125_signal,
    f031vdu_f031_volume_dry_up_zsellexh_126d_base_v126_signal,
    f031vdu_f031_volume_dry_up_zsellexh_189d_base_v127_signal,
    f031vdu_f031_volume_dry_up_zsellexh_252d_base_v128_signal,
    f031vdu_f031_volume_dry_up_zsellexh_378d_base_v129_signal,
    f031vdu_f031_volume_dry_up_zsellexh_504d_base_v130_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_5d_base_v131_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_10d_base_v132_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_21d_base_v133_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_42d_base_v134_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_63d_base_v135_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_126d_base_v136_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_189d_base_v137_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_252d_base_v138_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_378d_base_v139_signal,
    f031vdu_f031_volume_dry_up_dryupxdv_504d_base_v140_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_5d_base_v141_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_10d_base_v142_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_21d_base_v143_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_42d_base_v144_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_63d_base_v145_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_126d_base_v146_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_189d_base_v147_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_252d_base_v148_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_378d_base_v149_signal,
    f031vdu_f031_volume_dry_up_diffvolratio_504d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F031_VOLUME_DRY_UP_REGISTRY_076_150 = REGISTRY


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

    cols = {"closeadj": closeadj, "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    domain_primitives = ('_f031_vol_ratio', '_f031_dry_up_signal', '_f031_selling_exhaustion')
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
    print(f"OK f031_volume_dry_up_base_076_150_claude: {n_features} features pass")
