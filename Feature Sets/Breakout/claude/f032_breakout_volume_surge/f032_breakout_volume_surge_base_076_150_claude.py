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
def _f032_vol_surge(volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    return volume / avg.replace(0, np.nan)


def _f032_breakout_volume(closeadj, volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    surge = volume / avg.replace(0, np.nan)
    hi = closeadj.rolling(w, min_periods=max(1, w // 2)).max()
    break_flag = (closeadj >= hi).astype(float)
    return surge * break_flag * closeadj


def _f032_confirmation_score(closeadj, volume, w):
    avg = volume.rolling(w, min_periods=max(1, w // 2)).mean()
    surge = volume / avg.replace(0, np.nan)
    ret = closeadj.pct_change(w)
    return surge * ret * closeadj


def f032bvs_f032_breakout_volume_surge_confirmxdv_126d_base_v076_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    dv = closeadj * volume
    result = c * _mean(dv, 63) / _mean(dv, 126).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_189d_base_v077_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 189)
    dv = closeadj * volume
    result = c * _mean(dv, 94) / _mean(dv, 189).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_252d_base_v078_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    dv = closeadj * volume
    result = c * _mean(dv, 126) / _mean(dv, 252).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_378d_base_v079_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 378)
    dv = closeadj * volume
    result = c * _mean(dv, 189) / _mean(dv, 378).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_confirmxdv_504d_base_v080_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 504)
    dv = closeadj * volume
    result = c * _mean(dv, 252) / _mean(dv, 504).replace(0, np.nan)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_5d_base_v081_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 5)
    result = _mean(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_10d_base_v082_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 10)
    result = _mean(b, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_21d_base_v083_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    result = _mean(b, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_42d_base_v084_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 42)
    result = _mean(b, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_63d_base_v085_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    result = _mean(b, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_126d_base_v086_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    result = _mean(b, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_189d_base_v087_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 189)
    result = _mean(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_252d_base_v088_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    result = _mean(b, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_378d_base_v089_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 378)
    result = _mean(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smbovol_504d_base_v090_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 504)
    result = _mean(b, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_5d_base_v091_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 5)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_10d_base_v092_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 10)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_21d_base_v093_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 21)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_42d_base_v094_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 42)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_63d_base_v095_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 63)
    result = _z(b, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_126d_base_v096_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 126)
    result = _z(b, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_189d_base_v097_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 189)
    result = _z(b, 189)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_252d_base_v098_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 252)
    result = _z(b, 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_378d_base_v099_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 378)
    result = _z(b, 378)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_zbovol_504d_base_v100_signal(closeadj, volume):
    b = _f032_breakout_volume(closeadj, volume, 504)
    result = _z(b, 504)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_5d_base_v101_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 5)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_10d_base_v102_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 10)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_21d_base_v103_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_42d_base_v104_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 42)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_63d_base_v105_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_126d_base_v106_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_189d_base_v107_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 189)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_252d_base_v108_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_378d_base_v109_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 378)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_sqconfirm_504d_base_v110_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 504)
    result = (c * c) * np.sign(c)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_5d_base_v111_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 5)
    ret = closeadj.pct_change(1)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_10d_base_v112_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 10)
    ret = closeadj.pct_change(2)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_21d_base_v113_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    ret = closeadj.pct_change(4)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_42d_base_v114_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 42)
    ret = closeadj.pct_change(8)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_63d_base_v115_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    ret = closeadj.pct_change(12)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_126d_base_v116_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    ret = closeadj.pct_change(25)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_189d_base_v117_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 189)
    ret = closeadj.pct_change(37)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_252d_base_v118_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    ret = closeadj.pct_change(50)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_378d_base_v119_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 378)
    ret = closeadj.pct_change(75)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_surgexsign_504d_base_v120_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 504)
    ret = closeadj.pct_change(100)
    result = s * np.sign(ret).fillna(0.0) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_5d_base_v121_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 5)
    ret = closeadj.pct_change(1)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_10d_base_v122_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 10)
    ret = closeadj.pct_change(2)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_21d_base_v123_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    ret = closeadj.pct_change(4)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_42d_base_v124_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 42)
    ret = closeadj.pct_change(8)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_63d_base_v125_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    ret = closeadj.pct_change(12)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_126d_base_v126_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    ret = closeadj.pct_change(25)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_189d_base_v127_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 189)
    ret = closeadj.pct_change(37)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_252d_base_v128_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    ret = closeadj.pct_change(50)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_378d_base_v129_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 378)
    ret = closeadj.pct_change(75)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_upsurge_504d_base_v130_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 504)
    ret = closeadj.pct_change(100)
    up = (ret > 0).astype(float)
    result = s * up * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_5d_base_v131_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 5)
    result = _mean(c, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_10d_base_v132_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 10)
    result = _mean(c, 5)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_21d_base_v133_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 21)
    result = _mean(c, 7)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_42d_base_v134_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 42)
    result = _mean(c, 14)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_63d_base_v135_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 63)
    result = _mean(c, 21)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_126d_base_v136_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 126)
    result = _mean(c, 42)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_189d_base_v137_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 189)
    result = _mean(c, 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_252d_base_v138_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 252)
    result = _mean(c, 84)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_378d_base_v139_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 378)
    result = _mean(c, 126)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_smconfirm_504d_base_v140_signal(closeadj, volume):
    c = _f032_confirmation_score(closeadj, volume, 504)
    result = _mean(c, 168)
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_5d_base_v141_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 5)
    result = s.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_10d_base_v142_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 10)
    result = s.diff(2) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_21d_base_v143_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 21)
    result = s.diff(5) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_42d_base_v144_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 42)
    result = s.diff(10) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_63d_base_v145_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 63)
    result = s.diff(15) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_126d_base_v146_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 126)
    result = s.diff(31) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_189d_base_v147_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 189)
    result = s.diff(47) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_252d_base_v148_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 252)
    result = s.diff(63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_378d_base_v149_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 378)
    result = s.diff(94) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f032bvs_f032_breakout_volume_surge_diffsurge_504d_base_v150_signal(closeadj, volume):
    s = _f032_vol_surge(volume, 504)
    result = s.diff(126) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f032bvs_f032_breakout_volume_surge_confirmxdv_126d_base_v076_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_189d_base_v077_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_252d_base_v078_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_378d_base_v079_signal,
    f032bvs_f032_breakout_volume_surge_confirmxdv_504d_base_v080_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_5d_base_v081_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_10d_base_v082_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_21d_base_v083_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_42d_base_v084_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_63d_base_v085_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_126d_base_v086_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_189d_base_v087_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_252d_base_v088_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_378d_base_v089_signal,
    f032bvs_f032_breakout_volume_surge_smbovol_504d_base_v090_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_5d_base_v091_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_10d_base_v092_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_21d_base_v093_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_42d_base_v094_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_63d_base_v095_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_126d_base_v096_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_189d_base_v097_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_252d_base_v098_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_378d_base_v099_signal,
    f032bvs_f032_breakout_volume_surge_zbovol_504d_base_v100_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_5d_base_v101_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_10d_base_v102_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_21d_base_v103_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_42d_base_v104_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_63d_base_v105_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_126d_base_v106_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_189d_base_v107_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_252d_base_v108_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_378d_base_v109_signal,
    f032bvs_f032_breakout_volume_surge_sqconfirm_504d_base_v110_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_5d_base_v111_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_10d_base_v112_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_21d_base_v113_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_42d_base_v114_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_63d_base_v115_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_126d_base_v116_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_189d_base_v117_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_252d_base_v118_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_378d_base_v119_signal,
    f032bvs_f032_breakout_volume_surge_surgexsign_504d_base_v120_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_5d_base_v121_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_10d_base_v122_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_21d_base_v123_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_42d_base_v124_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_63d_base_v125_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_126d_base_v126_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_189d_base_v127_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_252d_base_v128_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_378d_base_v129_signal,
    f032bvs_f032_breakout_volume_surge_upsurge_504d_base_v130_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_5d_base_v131_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_10d_base_v132_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_21d_base_v133_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_42d_base_v134_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_63d_base_v135_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_126d_base_v136_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_189d_base_v137_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_252d_base_v138_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_378d_base_v139_signal,
    f032bvs_f032_breakout_volume_surge_smconfirm_504d_base_v140_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_5d_base_v141_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_10d_base_v142_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_21d_base_v143_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_42d_base_v144_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_63d_base_v145_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_126d_base_v146_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_189d_base_v147_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_252d_base_v148_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_378d_base_v149_signal,
    f032bvs_f032_breakout_volume_surge_diffsurge_504d_base_v150_signal,
]



def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F032_BREAKOUT_VOLUME_SURGE_REGISTRY_076_150 = REGISTRY


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
    domain_primitives = ('_f032_vol_surge', '_f032_breakout_volume', '_f032_confirmation_score')
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
    print(f"OK f032_breakout_volume_surge_base_076_150_claude: {n_features} features pass")
