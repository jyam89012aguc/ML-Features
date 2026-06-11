import numpy as np
import pandas as pd
from technology_helpers import _to_num, _clean, _safe_div, _log, _mean, _std, _sum, _min, _max, _z, _pct_change, _diff, _rank, _skew, _kurt, _autocorr, _corr, _slope, _ewm, _event_flag, _event_count, _event_rate, _clip_z


# core00 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_base_v076_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_base_v077_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_base_v078_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_base_v079_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_base_v080_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = beta5y
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_base_v081_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_base_v082_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_base_v083_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_base_v084_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_base_v085_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta1y, 63)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_base_v086_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_base_v087_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_base_v088_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_base_v089_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_base_v090_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _diff(beta5y, 252)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_base_v091_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_base_v092_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_base_v093_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_base_v094_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_base_v095_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) > 0, 0)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_base_v096_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_base_v097_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_base_v098_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_base_v099_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_base_v100_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_diff(rate_10y, 21) < 0, 0)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_base_v101_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_base_v102_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_base_v103_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_base_v104_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_base_v105_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(dxy, 21) > 0, 0)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_base_v106_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_base_v107_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_base_v108_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_base_v109_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_base_v110_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(ixic, 21) > 0, 0)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_base_v111_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_base_v112_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_base_v113_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_base_v114_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_base_v115_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _pct_change(closeadj, 21).where(_pct_change(sox, 21) > 0, 0)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_base_v116_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_base_v117_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_base_v118_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_base_v119_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_base_v120_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(ixic, 21), 252)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_base_v121_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_base_v122_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_base_v123_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_base_v124_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_base_v125_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _z(_pct_change(closeadj, 21) - _pct_change(sox, 21), 252)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_base_v126_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_base_v127_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_base_v128_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_base_v129_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_base_v130_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(rate_10y, 5), 63), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_base_v131_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_base_v132_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_base_v133_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_base_v134_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_base_v135_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _slope(_corr(_pct_change(closeadj, 5), _pct_change(ixic, 5), 63), 63)
    result = _ewm(series, 252)
    return _clean(result)

# core00 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core00_ewm_5d_base_v136_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core01 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core01_ewm_21d_base_v137_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core02 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core02_ewm_63d_base_v138_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core03 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core03_ewm_126d_base_v139_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core04 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core04_ewm_252d_base_v140_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(ixic, 63).abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core05 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core05_ewm_5d_base_v141_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    result = _ewm(series, 5)
    return _clean(result)

# core06 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core06_ewm_21d_base_v142_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    result = _ewm(series, 21)
    return _clean(result)

# core07 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core07_ewm_63d_base_v143_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    result = _ewm(series, 63)
    return _clean(result)

# core08 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core08_ewm_126d_base_v144_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    result = _ewm(series, 126)
    return _clean(result)

# core09 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core09_ewm_252d_base_v145_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = _safe_div(_pct_change(closeadj, 63), _pct_change(sox, 63).abs()+1e-9)
    result = _ewm(series, 252)
    return _clean(result)

# core10 ewm 5d
def cg_f104_technology_f104_macro_rates_sensitivity_core10_ewm_5d_base_v146_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    result = _ewm(series, 5)
    return _clean(result)

# core11 ewm 21d
def cg_f104_technology_f104_macro_rates_sensitivity_core11_ewm_21d_base_v147_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    result = _ewm(series, 21)
    return _clean(result)

# core12 ewm 63d
def cg_f104_technology_f104_macro_rates_sensitivity_core12_ewm_63d_base_v148_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    result = _ewm(series, 63)
    return _clean(result)

# core13 ewm 126d
def cg_f104_technology_f104_macro_rates_sensitivity_core13_ewm_126d_base_v149_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    result = _ewm(series, 126)
    return _clean(result)

# core14 ewm 252d
def cg_f104_technology_f104_macro_rates_sensitivity_core14_ewm_252d_base_v150_signal(closeadj, volume, beta1y, beta5y, rate_10y, dxy, ixic, sox, return1y):
    series = return1y - _pct_change(ixic, 252)
    result = _ewm(series, 252)
    return _clean(result)

