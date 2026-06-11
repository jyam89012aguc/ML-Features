import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z

# core75-150 sweep
# Block 75-79: pct 4q (continued)
def cg_f049_revenue_durability_core75_pct_4q_v076_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_pct_change(drawdown, 4))
def cg_f049_revenue_durability_core76_pct_4q_v077_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_kurt(revenue, 8), 4))
def cg_f049_revenue_durability_core77_pct_4q_v078_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_skew(revenue, 8), 4))
def cg_f049_revenue_durability_core78_pct_4q_v079_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_std(_pct_change(revenue, 4), 8), 4))
def cg_f049_revenue_durability_core79_pct_4q_v080_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_pct_change(_std(revenue, 8), 4))

# Block 80-89: std 8q
def cg_f049_revenue_durability_core80_std_8q_v081_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    down_mask = (revenue < 0).astype(int)
    return _clean(_std(_mean(down_mask, 4), 8))
def cg_f049_revenue_durability_core81_std_8q_v082_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy_decline = (_pct_change(revenue, 4) < 0).astype(int)
    return _clean(_std(_mean(yoy_decline, 4), 8))
def cg_f049_revenue_durability_core82_std_8q_v083_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_std(sr, 8))
def cg_f049_revenue_durability_core83_std_8q_v084_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_std(_mean(downside.abs(), 4), 8))
def cg_f049_revenue_durability_core84_std_8q_v085_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_std(omega, 8))
def cg_f049_revenue_durability_core85_std_8q_v086_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_std(_autocorr(revenue, 4), 8))
def cg_f049_revenue_durability_core86_std_8q_v087_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_std(_autocorr(_pct_change(revenue, 4), 4), 8))
def cg_f049_revenue_durability_core87_std_8q_v088_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_std(drawdown, 8))
def cg_f049_revenue_durability_core88_std_8q_v089_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_std(_kurt(revenue, 8), 8))
def cg_f049_revenue_durability_core89_std_8q_v090_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_std(_skew(revenue, 8), 8))

# Block 90-99: log
def cg_f049_revenue_durability_core90_log_v091_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    down_mask = (revenue < 0).astype(int)
    return _clean(_log(_mean(down_mask, 4).clip(lower=0.001)))
def cg_f049_revenue_durability_core91_log_v092_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy_decline = (_pct_change(revenue, 4) < 0).astype(int)
    return _clean(_log(_mean(yoy_decline, 4).clip(lower=0.001)))
def cg_f049_revenue_durability_core92_log_v093_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_log(sr.clip(lower=-0.9) + 1.1))
def cg_f049_revenue_durability_core93_log_v094_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_log(_mean(downside.abs(), 4).clip(lower=0.0001)))
def cg_f049_revenue_durability_core94_log_v095_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_log(omega.clip(lower=0.001)))
def cg_f049_revenue_durability_core95_log_v096_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_log(_autocorr(revenue, 4).clip(lower=-0.9) + 1.1))
def cg_f049_revenue_durability_core96_log_v097_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_log(_autocorr(_pct_change(revenue, 4), 4).clip(lower=-0.9) + 1.1))
def cg_f049_revenue_durability_core97_log_v098_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_log(drawdown.abs().clip(lower=0.001)))
def cg_f049_revenue_durability_core98_log_v099_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_log(_kurt(revenue, 8).clip(lower=0.001)))
def cg_f049_revenue_durability_core99_log_v100_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_log(_skew(revenue, 8).clip(lower=-0.9) + 1.1))

# Block 100-109: diff 1q
def cg_f049_revenue_durability_core100_diff_1q_v101_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_diff(sr, 1))
def cg_f049_revenue_durability_core101_diff_1q_v102_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_diff(_mean(downside.abs(), 4), 1))
def cg_f049_revenue_durability_core102_diff_1q_v103_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_diff(omega, 1))
def cg_f049_revenue_durability_core103_diff_1q_v104_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_diff(_autocorr(revenue, 4), 1))
def cg_f049_revenue_durability_core104_diff_1q_v105_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_diff(_autocorr(_pct_change(revenue, 4), 4), 1))
def cg_f049_revenue_durability_core105_diff_1q_v106_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_diff(drawdown, 1))
def cg_f049_revenue_durability_core106_diff_1q_v107_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_diff(_kurt(revenue, 8), 1))
def cg_f049_revenue_durability_core107_diff_1q_v108_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_diff(_skew(revenue, 8), 1))
def cg_f049_revenue_durability_core108_diff_1q_v109_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_diff(_std(_pct_change(revenue, 4), 8), 1))
def cg_f049_revenue_durability_core109_diff_1q_v110_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_diff(_std(revenue, 8), 1))

# Block 110-119: slope 4q
def cg_f049_revenue_durability_core110_slope_4q_v111_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_slope(sr, 4))
def cg_f049_revenue_durability_core111_slope_4q_v112_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_slope(_mean(downside.abs(), 4), 4))
def cg_f049_revenue_durability_core112_slope_4q_v113_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_slope(omega, 4))
def cg_f049_revenue_durability_core113_slope_4q_v114_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_slope(_autocorr(revenue, 4), 4))
def cg_f049_revenue_durability_core114_slope_4q_v115_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_slope(_autocorr(_pct_change(revenue, 4), 4), 4))
def cg_f049_revenue_durability_core115_slope_4q_v116_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_slope(drawdown, 4))
def cg_f049_revenue_durability_core116_slope_4q_v117_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_slope(_kurt(revenue, 8), 4))
def cg_f049_revenue_durability_core117_slope_4q_v118_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_slope(_skew(revenue, 8), 4))
def cg_f049_revenue_durability_core118_slope_4q_v119_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_slope(_std(_pct_change(revenue, 4), 8), 4))
def cg_f049_revenue_durability_core119_slope_4q_v120_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_slope(_std(revenue, 8), 4))

# Block 120-129: ewm 8q
def cg_f049_revenue_durability_core120_ewm_8q_v121_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    sr = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_ewm(sr, 8))
def cg_f049_revenue_durability_core121_ewm_8q_v122_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_ewm(_mean(downside.abs(), 4), 8))
def cg_f049_revenue_durability_core122_ewm_8q_v123_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    omega = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_ewm(omega, 8))
def cg_f049_revenue_durability_core123_ewm_8q_v124_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_ewm(_autocorr(revenue, 4), 8))
def cg_f049_revenue_durability_core124_ewm_8q_v125_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_ewm(_autocorr(_pct_change(revenue, 4), 4), 8))
def cg_f049_revenue_durability_core125_ewm_8q_v126_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    drawdown = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_ewm(drawdown, 8))
def cg_f049_revenue_durability_core126_ewm_8q_v127_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_ewm(_kurt(revenue, 8), 8))
def cg_f049_revenue_durability_core127_ewm_8q_v128_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_ewm(_skew(revenue, 8), 8))
def cg_f049_revenue_durability_core128_ewm_8q_v129_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_ewm(_std(_pct_change(revenue, 4), 8), 8))
def cg_f049_revenue_durability_core129_ewm_8q_v130_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_ewm(_std(revenue, 8), 8))

# Block 130-139: stability 12q
def cg_f049_revenue_durability_core130_stability_12q_v131_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    base = _safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core131_stability_12q_v132_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    base = _mean(downside.abs(), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core132_stability_12q_v133_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    base = _safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core133_stability_12q_v134_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    base = _autocorr(revenue, 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core134_stability_12q_v135_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    base = _autocorr(_pct_change(revenue, 4), 4)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core135_stability_12q_v136_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    base = _safe_div(revenue - rolling_max, rolling_max.abs() + 1.0)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core136_stability_12q_v137_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    base = _kurt(revenue, 8)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core137_stability_12q_v138_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    base = _skew(revenue, 8)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core138_stability_12q_v139_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    base = _std(_pct_change(revenue, 4), 8)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))
def cg_f049_revenue_durability_core139_stability_12q_v140_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    base = _std(revenue, 8)
    return _clean(_safe_div(_std(base, 12), _mean(base, 12).abs() + 1.0))

# Block 140-149: levels
def cg_f049_revenue_durability_core140_sr_v141_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    return _clean(_safe_div(_mean(yoy, 4), _std(yoy, 4).abs() + 1e-9))
def cg_f049_revenue_durability_core141_downside_v142_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    downside = np.minimum(yoy, 0)
    return _clean(_mean(downside.abs(), 4))
def cg_f049_revenue_durability_core142_omega_v143_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    yoy = _pct_change(revenue, 4)
    upside = np.maximum(yoy, 0)
    downside = np.minimum(yoy, 0).abs()
    return _clean(_safe_div(_mean(upside, 4), _mean(downside, 4) + 1e-9))
def cg_f049_revenue_durability_core143_autocorr_rev_v144_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_autocorr(revenue, 4))
def cg_f049_revenue_durability_core144_autocorr_yoy_v145_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_autocorr(_pct_change(revenue, 4), 4))
def cg_f049_revenue_durability_core145_drawdown_v146_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    rolling_max = _max(revenue, 12)
    return _clean(_safe_div(revenue - rolling_max, rolling_max.abs() + 1.0))
def cg_f049_revenue_durability_core146_kurt_v147_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_kurt(revenue, 8))
def cg_f049_revenue_durability_core147_skew_v148_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_skew(revenue, 8))
def cg_f049_revenue_durability_core148_vol_yoy_v149_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_std(_pct_change(revenue, 4), 8))
def cg_f049_revenue_durability_core149_vol_rev_v150_signal(revenue, assets, marketcap, opex, cor, equity, ebitda, netinc):
    return _clean(_std(revenue, 8))
