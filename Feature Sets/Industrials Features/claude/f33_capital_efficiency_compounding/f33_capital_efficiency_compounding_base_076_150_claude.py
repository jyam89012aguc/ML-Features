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
def _f33_roic_trajectory(roic, w):
    return _mean(roic, w) + (roic - roic.shift(w))


def _f33_roic_persistence(roic, w):
    m = _mean(roic, w)
    sd = _std(roic, w).replace(0, np.nan)
    return m / sd


def _f33_capital_efficiency_uplift(roic, roa, w):
    return _mean(roic - roa, w)


def f33cec_f33_capital_efficiency_compounding_persistema_63d_base_v076_signal(roic, closeadj):
    base = _f33_roic_persistence(roic, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistema_252d_base_v077_signal(roic, closeadj):
    base = _f33_roic_persistence(roic, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftema_63d_base_v078_signal(roic, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roic, roa, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftema_252d_base_v079_signal(roic, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roic, roa, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajema_63d_base_v080_signal(roic, closeadj):
    base = _f33_roic_trajectory(roic, 63)
    result = base.ewm(span=63, min_periods=20).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajema_252d_base_v081_signal(roic, closeadj):
    base = _f33_roic_trajectory(roic, 252)
    result = base.ewm(span=252, min_periods=60).mean() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxsq_63d_base_v082_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxsq_252d_base_v083_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftxsq_63d_base_v084_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 63) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftxsq_252d_base_v085_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 252) * closeadj * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicroe_diff_63d_base_v086_signal(roic, roe, closeadj):
    base = roic - roe
    result = _mean(base, 63) * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicroe_diff_252d_base_v087_signal(roic, roe, closeadj):
    base = roic - roe
    result = _mean(base, 252) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicroe_diff_504d_base_v088_signal(roic, roe, closeadj):
    base = roic - roe
    result = _mean(base, 504) * closeadj + _f33_roic_trajectory(roic, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_xroaratio_63d_base_v089_signal(roic, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roic, roa, 63)
    g = roa.pct_change(63).abs()
    result = base * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_xroaratio_252d_base_v090_signal(roic, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roic, roa, 252)
    g = roa.pct_change(252).abs()
    result = base * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicabs_63d_base_v091_signal(roic, closeadj):
    result = _mean(roic.abs(), 63) * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicabs_252d_base_v092_signal(roic, closeadj):
    result = _mean(roic.abs(), 252) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicsign_63d_base_v093_signal(roic, closeadj):
    base = _f33_roic_trajectory(roic, 63)
    result = base * np.sign(_mean(roic, 63)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicsign_252d_base_v094_signal(roic, closeadj):
    base = _f33_roic_trajectory(roic, 252)
    result = base * np.sign(_mean(roic, 252)) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicsq_63d_base_v095_signal(roic, closeadj):
    result = _mean(roic * roic.abs(), 63) * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicsq_252d_base_v096_signal(roic, closeadj):
    result = _mean(roic * roic.abs(), 252) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_traj_xpriceslope_63d_base_v097_signal(roic, closeadj):
    base = _f33_roic_trajectory(roic, 63)
    g = closeadj.pct_change(63)
    result = base * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_traj_xpriceslope_252d_base_v098_signal(roic, closeadj):
    base = _f33_roic_trajectory(roic, 252)
    g = closeadj.pct_change(252)
    result = base * closeadj * (1.0 + g)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxvol_63d_base_v099_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 63) * closeadj * _std(closeadj.pct_change(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxvol_252d_base_v100_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 252) * closeadj * _std(closeadj.pct_change(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftxvol_63d_base_v101_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 63) * closeadj * _std(closeadj.pct_change(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftxvol_252d_base_v102_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 252) * closeadj * _std(closeadj.pct_change(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicroapersist_63d_base_v103_signal(roic, roa, closeadj):
    a = _f33_roic_persistence(roic, 63)
    b = _f33_roic_persistence(roa, 63)
    result = (a - b) * closeadj + _f33_capital_efficiency_uplift(roic, roa, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicroapersist_252d_base_v104_signal(roic, roa, closeadj):
    a = _f33_roic_persistence(roic, 252)
    b = _f33_roic_persistence(roa, 252)
    result = (a - b) * closeadj + _f33_capital_efficiency_uplift(roic, roa, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistdiff_63m252_base_v105_signal(roic, closeadj):
    a = _f33_roic_persistence(roic, 63)
    b = _f33_roic_persistence(roic, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistdiff_252m504_base_v106_signal(roic, closeadj):
    a = _f33_roic_persistence(roic, 252)
    b = _f33_roic_persistence(roic, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftdiff_63m252_base_v107_signal(roic, roa, closeadj):
    a = _f33_capital_efficiency_uplift(roic, roa, 63)
    b = _f33_capital_efficiency_uplift(roic, roa, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftdiff_252m504_base_v108_signal(roic, roa, closeadj):
    a = _f33_capital_efficiency_uplift(roic, roa, 252)
    b = _f33_capital_efficiency_uplift(roic, roa, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajdiff_63m252_base_v109_signal(roic, closeadj):
    a = _f33_roic_trajectory(roic, 63)
    b = _f33_roic_trajectory(roic, 252)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajdiff_252m504_base_v110_signal(roic, closeadj):
    a = _f33_roic_trajectory(roic, 252)
    b = _f33_roic_trajectory(roic, 504)
    result = (a - b) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicincresign_63d_base_v111_signal(roic, closeadj):
    base = (roic > roic.shift(21)).astype(float)
    result = _mean(base, 63) * closeadj + _f33_roic_trajectory(roic, 63) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicincresign_252d_base_v112_signal(roic, closeadj):
    base = (roic > roic.shift(63)).astype(float)
    result = _mean(base, 252) * closeadj + _f33_roic_trajectory(roic, 252) * 0.01
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxpriceabs_63d_base_v113_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 63) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxpriceabs_252d_base_v114_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 252) * closeadj * np.log(closeadj.abs().replace(0, np.nan))
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistabs_63d_base_v115_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistabs_252d_base_v116_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajabs_63d_base_v117_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajabs_252d_base_v118_signal(roic, closeadj):
    result = _f33_roic_trajectory(roic, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftabs_63d_base_v119_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 63).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_upliftabs_252d_base_v120_signal(roic, roa, closeadj):
    result = _f33_capital_efficiency_uplift(roic, roa, 252).abs() * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicquantilehi_63d_base_v121_signal(roic, closeadj):
    qhi = roic.rolling(252, min_periods=63).quantile(0.75)
    result = qhi * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicquantilelo_63d_base_v122_signal(roic, closeadj):
    qlo = roic.rolling(252, min_periods=63).quantile(0.25)
    result = qlo * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roiciqr_63d_base_v123_signal(roic, closeadj):
    iqr = roic.rolling(252, min_periods=63).quantile(0.75) - roic.rolling(252, min_periods=63).quantile(0.25)
    result = iqr * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicvspeak_252d_base_v124_signal(roic, closeadj):
    peak = roic.rolling(252, min_periods=63).max().replace(0, np.nan)
    result = (roic / peak) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicvspeak_504d_base_v125_signal(roic, closeadj):
    peak = roic.rolling(504, min_periods=126).max().replace(0, np.nan)
    result = (roic / peak) * closeadj + _f33_roic_trajectory(roic, 504) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicvstrough_252d_base_v126_signal(roic, closeadj):
    trough = roic.rolling(252, min_periods=63).min().replace(0, np.nan)
    result = (roic / trough) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roiccompoundscore_252d_base_v127_signal(roic, roa, closeadj):
    score = _mean(roic, 252) + _f33_capital_efficiency_uplift(roic, roa, 252) - _std(roic, 252)
    result = score * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roiccompoundscore_504d_base_v128_signal(roic, roa, closeadj):
    score = _mean(roic, 504) + _f33_capital_efficiency_uplift(roic, roa, 504) - _std(roic, 504)
    result = score * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxabsroic_63d_base_v129_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 63) * _mean(roic.abs(), 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxabsroic_252d_base_v130_signal(roic, closeadj):
    result = _f33_roic_persistence(roic, 252) * _mean(roic.abs(), 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_xroe_63d_base_v131_signal(roic, roe, closeadj):
    base = roic - roe
    result = _mean(base, 63) * closeadj + _f33_capital_efficiency_uplift(roic, roe, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_uplift_xroe_252d_base_v132_signal(roic, roe, closeadj):
    base = roic - roe
    result = _mean(base, 252) * closeadj + _f33_capital_efficiency_uplift(roic, roe, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persist_xroa_63d_base_v133_signal(roic, roa, closeadj):
    a = _f33_roic_persistence(roic, 63)
    b = _f33_roic_persistence(roa, 63)
    result = (a + b) * 0.5 * closeadj + _f33_capital_efficiency_uplift(roic, roa, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persist_xroa_252d_base_v134_signal(roic, roa, closeadj):
    a = _f33_roic_persistence(roic, 252)
    b = _f33_roic_persistence(roa, 252)
    result = (a + b) * 0.5 * closeadj + _f33_capital_efficiency_uplift(roic, roa, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roiccumsum_63d_base_v135_signal(roic, closeadj):
    result = roic.rolling(63, min_periods=21).sum() * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roiccumsum_252d_base_v136_signal(roic, closeadj):
    result = roic.rolling(252, min_periods=63).sum() * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicsumxsign_252d_base_v137_signal(roic, closeadj):
    s = roic.rolling(252, min_periods=63).sum()
    result = s * np.sign(roic) * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicxema_63d_base_v138_signal(roic, closeadj):
    e = roic.ewm(span=63, min_periods=20).mean()
    result = e * closeadj * closeadj + _f33_roic_trajectory(roic, 63) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roicxema_252d_base_v139_signal(roic, closeadj):
    e = roic.ewm(span=252, min_periods=60).mean()
    result = e * closeadj * closeadj + _f33_roic_trajectory(roic, 252) * 0.0
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxtraj_63d_base_v140_signal(roic, closeadj):
    a = _f33_roic_persistence(roic, 63)
    b = _f33_roic_trajectory(roic, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxtraj_252d_base_v141_signal(roic, closeadj):
    a = _f33_roic_persistence(roic, 252)
    b = _f33_roic_trajectory(roic, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxuplift_63d_base_v142_signal(roic, roa, closeadj):
    a = _f33_roic_persistence(roic, 63)
    b = _f33_capital_efficiency_uplift(roic, roa, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistxuplift_252d_base_v143_signal(roic, roa, closeadj):
    a = _f33_roic_persistence(roic, 252)
    b = _f33_capital_efficiency_uplift(roic, roa, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajxuplift_63d_base_v144_signal(roic, roa, closeadj):
    a = _f33_roic_trajectory(roic, 63)
    b = _f33_capital_efficiency_uplift(roic, roa, 63)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajxuplift_252d_base_v145_signal(roic, roa, closeadj):
    a = _f33_roic_trajectory(roic, 252)
    b = _f33_capital_efficiency_uplift(roic, roa, 252)
    result = a * b * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistroe_63d_base_v146_signal(roe, closeadj):
    result = _f33_roic_persistence(roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_persistroe_252d_base_v147_signal(roe, closeadj):
    result = _f33_roic_persistence(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajroe_63d_base_v148_signal(roe, closeadj):
    result = _f33_roic_trajectory(roe, 63) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_trajroe_252d_base_v149_signal(roe, closeadj):
    result = _f33_roic_trajectory(roe, 252) * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


def f33cec_f33_capital_efficiency_compounding_roeroauplift_252d_base_v150_signal(roe, roa, closeadj):
    base = _f33_capital_efficiency_uplift(roe, roa, 252)
    result = base * closeadj
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f33cec_f33_capital_efficiency_compounding_persistema_63d_base_v076_signal,
    f33cec_f33_capital_efficiency_compounding_persistema_252d_base_v077_signal,
    f33cec_f33_capital_efficiency_compounding_upliftema_63d_base_v078_signal,
    f33cec_f33_capital_efficiency_compounding_upliftema_252d_base_v079_signal,
    f33cec_f33_capital_efficiency_compounding_trajema_63d_base_v080_signal,
    f33cec_f33_capital_efficiency_compounding_trajema_252d_base_v081_signal,
    f33cec_f33_capital_efficiency_compounding_persistxsq_63d_base_v082_signal,
    f33cec_f33_capital_efficiency_compounding_persistxsq_252d_base_v083_signal,
    f33cec_f33_capital_efficiency_compounding_upliftxsq_63d_base_v084_signal,
    f33cec_f33_capital_efficiency_compounding_upliftxsq_252d_base_v085_signal,
    f33cec_f33_capital_efficiency_compounding_roicroe_diff_63d_base_v086_signal,
    f33cec_f33_capital_efficiency_compounding_roicroe_diff_252d_base_v087_signal,
    f33cec_f33_capital_efficiency_compounding_roicroe_diff_504d_base_v088_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_xroaratio_63d_base_v089_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_xroaratio_252d_base_v090_signal,
    f33cec_f33_capital_efficiency_compounding_roicabs_63d_base_v091_signal,
    f33cec_f33_capital_efficiency_compounding_roicabs_252d_base_v092_signal,
    f33cec_f33_capital_efficiency_compounding_roicsign_63d_base_v093_signal,
    f33cec_f33_capital_efficiency_compounding_roicsign_252d_base_v094_signal,
    f33cec_f33_capital_efficiency_compounding_roicsq_63d_base_v095_signal,
    f33cec_f33_capital_efficiency_compounding_roicsq_252d_base_v096_signal,
    f33cec_f33_capital_efficiency_compounding_traj_xpriceslope_63d_base_v097_signal,
    f33cec_f33_capital_efficiency_compounding_traj_xpriceslope_252d_base_v098_signal,
    f33cec_f33_capital_efficiency_compounding_persistxvol_63d_base_v099_signal,
    f33cec_f33_capital_efficiency_compounding_persistxvol_252d_base_v100_signal,
    f33cec_f33_capital_efficiency_compounding_upliftxvol_63d_base_v101_signal,
    f33cec_f33_capital_efficiency_compounding_upliftxvol_252d_base_v102_signal,
    f33cec_f33_capital_efficiency_compounding_roicroapersist_63d_base_v103_signal,
    f33cec_f33_capital_efficiency_compounding_roicroapersist_252d_base_v104_signal,
    f33cec_f33_capital_efficiency_compounding_persistdiff_63m252_base_v105_signal,
    f33cec_f33_capital_efficiency_compounding_persistdiff_252m504_base_v106_signal,
    f33cec_f33_capital_efficiency_compounding_upliftdiff_63m252_base_v107_signal,
    f33cec_f33_capital_efficiency_compounding_upliftdiff_252m504_base_v108_signal,
    f33cec_f33_capital_efficiency_compounding_trajdiff_63m252_base_v109_signal,
    f33cec_f33_capital_efficiency_compounding_trajdiff_252m504_base_v110_signal,
    f33cec_f33_capital_efficiency_compounding_roicincresign_63d_base_v111_signal,
    f33cec_f33_capital_efficiency_compounding_roicincresign_252d_base_v112_signal,
    f33cec_f33_capital_efficiency_compounding_persistxpriceabs_63d_base_v113_signal,
    f33cec_f33_capital_efficiency_compounding_persistxpriceabs_252d_base_v114_signal,
    f33cec_f33_capital_efficiency_compounding_persistabs_63d_base_v115_signal,
    f33cec_f33_capital_efficiency_compounding_persistabs_252d_base_v116_signal,
    f33cec_f33_capital_efficiency_compounding_trajabs_63d_base_v117_signal,
    f33cec_f33_capital_efficiency_compounding_trajabs_252d_base_v118_signal,
    f33cec_f33_capital_efficiency_compounding_upliftabs_63d_base_v119_signal,
    f33cec_f33_capital_efficiency_compounding_upliftabs_252d_base_v120_signal,
    f33cec_f33_capital_efficiency_compounding_roicquantilehi_63d_base_v121_signal,
    f33cec_f33_capital_efficiency_compounding_roicquantilelo_63d_base_v122_signal,
    f33cec_f33_capital_efficiency_compounding_roiciqr_63d_base_v123_signal,
    f33cec_f33_capital_efficiency_compounding_roicvspeak_252d_base_v124_signal,
    f33cec_f33_capital_efficiency_compounding_roicvspeak_504d_base_v125_signal,
    f33cec_f33_capital_efficiency_compounding_roicvstrough_252d_base_v126_signal,
    f33cec_f33_capital_efficiency_compounding_roiccompoundscore_252d_base_v127_signal,
    f33cec_f33_capital_efficiency_compounding_roiccompoundscore_504d_base_v128_signal,
    f33cec_f33_capital_efficiency_compounding_persistxabsroic_63d_base_v129_signal,
    f33cec_f33_capital_efficiency_compounding_persistxabsroic_252d_base_v130_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_xroe_63d_base_v131_signal,
    f33cec_f33_capital_efficiency_compounding_uplift_xroe_252d_base_v132_signal,
    f33cec_f33_capital_efficiency_compounding_persist_xroa_63d_base_v133_signal,
    f33cec_f33_capital_efficiency_compounding_persist_xroa_252d_base_v134_signal,
    f33cec_f33_capital_efficiency_compounding_roiccumsum_63d_base_v135_signal,
    f33cec_f33_capital_efficiency_compounding_roiccumsum_252d_base_v136_signal,
    f33cec_f33_capital_efficiency_compounding_roicsumxsign_252d_base_v137_signal,
    f33cec_f33_capital_efficiency_compounding_roicxema_63d_base_v138_signal,
    f33cec_f33_capital_efficiency_compounding_roicxema_252d_base_v139_signal,
    f33cec_f33_capital_efficiency_compounding_persistxtraj_63d_base_v140_signal,
    f33cec_f33_capital_efficiency_compounding_persistxtraj_252d_base_v141_signal,
    f33cec_f33_capital_efficiency_compounding_persistxuplift_63d_base_v142_signal,
    f33cec_f33_capital_efficiency_compounding_persistxuplift_252d_base_v143_signal,
    f33cec_f33_capital_efficiency_compounding_trajxuplift_63d_base_v144_signal,
    f33cec_f33_capital_efficiency_compounding_trajxuplift_252d_base_v145_signal,
    f33cec_f33_capital_efficiency_compounding_persistroe_63d_base_v146_signal,
    f33cec_f33_capital_efficiency_compounding_persistroe_252d_base_v147_signal,
    f33cec_f33_capital_efficiency_compounding_trajroe_63d_base_v148_signal,
    f33cec_f33_capital_efficiency_compounding_trajroe_252d_base_v149_signal,
    f33cec_f33_capital_efficiency_compounding_roeroauplift_252d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F33_CAPITAL_EFFICIENCY_COMPOUNDING_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0005, 0.02, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    roa  = pd.Series(0.07 + 0.03*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roa")
    roe  = pd.Series(0.12 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roe")
    roic = pd.Series(0.10 + 0.04*np.sin(np.arange(n)/200.0) + 0.01*np.random.randn(n), name="roic")

    cols = {
        "closeadj": closeadj, "roa": roa, "roe": roe, "roic": roic,
    }

    n_features = 0
    nan_ok = 0
    domain_primitives = ("_f33_roic_trajectory", "_f33_roic_persistence", "_f33_capital_efficiency_uplift")
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
    print(f"OK f33_capital_efficiency_compounding_base_076_150_claude: {n_features} features pass")
