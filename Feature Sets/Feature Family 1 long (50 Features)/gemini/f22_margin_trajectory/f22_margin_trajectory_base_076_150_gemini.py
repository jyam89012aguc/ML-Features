import pandas as pd
import numpy as np
import inspect

def _mt_margin(num, den): return num / den.replace(0, np.nan)
def _mt_delta(s, w): return s.diff(w)
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _cv(s, w): return _std(s, w) / _sma(s, w).replace(0, np.nan)

# Coefficient of Variation of opm over 63d
def f22mt_opm_cv_63d_base_v076_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_opinc, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 126d
def f22mt_opm_cv_126d_base_v077_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_opinc, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 252d
def f22mt_opm_cv_252d_base_v078_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_opinc, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 504d
def f22mt_opm_cv_504d_base_v079_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_opinc, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 756d
def f22mt_opm_cv_756d_base_v080_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_opinc, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 1260d
def f22mt_opm_cv_1260d_base_v081_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_opinc, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 63d
def f22mt_nm_cv_63d_base_v082_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_netinc, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 126d
def f22mt_nm_cv_126d_base_v083_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_netinc, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 252d
def f22mt_nm_cv_252d_base_v084_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_netinc, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 504d
def f22mt_nm_cv_504d_base_v085_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_netinc, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 756d
def f22mt_nm_cv_756d_base_v086_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_netinc, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 1260d
def f22mt_nm_cv_1260d_base_v087_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_netinc, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 63d SMA
def f22mt_gm_rel_sma_63d_base_v088_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 126d SMA
def f22mt_gm_rel_sma_126d_base_v089_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 252d SMA
def f22mt_gm_rel_sma_252d_base_v090_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 504d SMA
def f22mt_gm_rel_sma_504d_base_v091_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 756d SMA
def f22mt_gm_rel_sma_756d_base_v092_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 756).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 1260d SMA
def f22mt_gm_rel_sma_1260d_base_v093_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 1260).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 63d SMA
def f22mt_ebitdam_rel_sma_63d_base_v094_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 126d SMA
def f22mt_ebitdam_rel_sma_126d_base_v095_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 252d SMA
def f22mt_ebitdam_rel_sma_252d_base_v096_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 504d SMA
def f22mt_ebitdam_rel_sma_504d_base_v097_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 756d SMA
def f22mt_ebitdam_rel_sma_756d_base_v098_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 756).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 1260d SMA
def f22mt_ebitdam_rel_sma_1260d_base_v099_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 1260).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 63d SMA
def f22mt_opm_rel_sma_63d_base_v100_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 126d SMA
def f22mt_opm_rel_sma_126d_base_v101_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 252d SMA
def f22mt_opm_rel_sma_252d_base_v102_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 504d SMA
def f22mt_opm_rel_sma_504d_base_v103_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 756d SMA
def f22mt_opm_rel_sma_756d_base_v104_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 756).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 1260d SMA
def f22mt_opm_rel_sma_1260d_base_v105_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 1260).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 63d SMA
def f22mt_nm_rel_sma_63d_base_v106_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 126d SMA
def f22mt_nm_rel_sma_126d_base_v107_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 252d SMA
def f22mt_nm_rel_sma_252d_base_v108_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 504d SMA
def f22mt_nm_rel_sma_504d_base_v109_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 504).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 756d SMA
def f22mt_nm_rel_sma_756d_base_v110_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 756).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 1260d SMA
def f22mt_nm_rel_sma_1260d_base_v111_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 1260).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 63d
def f22mt_egm_delta_63d_base_v112_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_gp)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 126d
def f22mt_egm_delta_126d_base_v113_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_gp)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 252d
def f22mt_egm_delta_252d_base_v114_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_gp)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 504d
def f22mt_egm_delta_504d_base_v115_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_gp)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 756d
def f22mt_egm_delta_756d_base_v116_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_gp)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 1260d
def f22mt_egm_delta_1260d_base_v117_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_gp)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 63d
def f22mt_ogm_delta_63d_base_v118_signal(arg_opinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_gp)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 126d
def f22mt_ogm_delta_126d_base_v119_signal(arg_opinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_gp)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 252d
def f22mt_ogm_delta_252d_base_v120_signal(arg_opinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_gp)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 504d
def f22mt_ogm_delta_504d_base_v121_signal(arg_opinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_gp)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 756d
def f22mt_ogm_delta_756d_base_v122_signal(arg_opinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_gp)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 1260d
def f22mt_ogm_delta_1260d_base_v123_signal(arg_opinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_gp)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 63d
def f22mt_ngm_delta_63d_base_v124_signal(arg_netinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_gp)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 126d
def f22mt_ngm_delta_126d_base_v125_signal(arg_netinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_gp)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 252d
def f22mt_ngm_delta_252d_base_v126_signal(arg_netinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_gp)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 504d
def f22mt_ngm_delta_504d_base_v127_signal(arg_netinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_gp)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 756d
def f22mt_ngm_delta_756d_base_v128_signal(arg_netinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_gp)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 1260d
def f22mt_ngm_delta_1260d_base_v129_signal(arg_netinc, arg_gp) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_gp)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 63d
def f22mt_nem_delta_63d_base_v130_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_ebitda)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 126d
def f22mt_nem_delta_126d_base_v131_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_ebitda)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 252d
def f22mt_nem_delta_252d_base_v132_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_ebitda)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 504d
def f22mt_nem_delta_504d_base_v133_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_ebitda)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 756d
def f22mt_nem_delta_756d_base_v134_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_ebitda)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 1260d
def f22mt_nem_delta_1260d_base_v135_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_ebitda)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 63d
def f22mt_nom_delta_63d_base_v136_signal(arg_netinc, arg_opinc) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_opinc)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 126d
def f22mt_nom_delta_126d_base_v137_signal(arg_netinc, arg_opinc) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_opinc)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 252d
def f22mt_nom_delta_252d_base_v138_signal(arg_netinc, arg_opinc) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_opinc)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 504d
def f22mt_nom_delta_504d_base_v139_signal(arg_netinc, arg_opinc) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_opinc)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 756d
def f22mt_nom_delta_756d_base_v140_signal(arg_netinc, arg_opinc) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_opinc)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 1260d
def f22mt_nom_delta_1260d_base_v141_signal(arg_netinc, arg_opinc) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_opinc)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 63d
def f22mt_egm_z_63d_base_v142_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_gp), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 126d
def f22mt_egm_z_126d_base_v143_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_gp), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 252d
def f22mt_egm_z_252d_base_v144_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_gp), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 504d
def f22mt_egm_z_504d_base_v145_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_gp), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 756d
def f22mt_egm_z_756d_base_v146_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_gp), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 1260d
def f22mt_egm_z_1260d_base_v147_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_gp), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ogm over 63d
def f22mt_ogm_z_63d_base_v148_signal(arg_opinc, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_gp), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ogm over 126d
def f22mt_ogm_z_126d_base_v149_signal(arg_opinc, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_gp), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ogm over 252d
def f22mt_ogm_z_252d_base_v150_signal(arg_opinc, arg_gp) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_gp), 252)
    return res.replace([np.inf, -np.inf], np.nan)

f22mt_BASE_076_150_REGISTRY = {
    'f22mt_opm_cv_63d_base_v076_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_63d_base_v076_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_63d_base_v076_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_63d_base_v076_signal']
    },
    'f22mt_opm_cv_126d_base_v077_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_126d_base_v077_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_126d_base_v077_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_126d_base_v077_signal']
    },
    'f22mt_opm_cv_252d_base_v078_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_252d_base_v078_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_252d_base_v078_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_252d_base_v078_signal']
    },
    'f22mt_opm_cv_504d_base_v079_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_504d_base_v079_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_504d_base_v079_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_504d_base_v079_signal']
    },
    'f22mt_opm_cv_756d_base_v080_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_756d_base_v080_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_756d_base_v080_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_756d_base_v080_signal']
    },
    'f22mt_opm_cv_1260d_base_v081_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_1260d_base_v081_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_1260d_base_v081_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_1260d_base_v081_signal']
    },
    'f22mt_nm_cv_63d_base_v082_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_63d_base_v082_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_63d_base_v082_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_63d_base_v082_signal']
    },
    'f22mt_nm_cv_126d_base_v083_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_126d_base_v083_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_126d_base_v083_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_126d_base_v083_signal']
    },
    'f22mt_nm_cv_252d_base_v084_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_252d_base_v084_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_252d_base_v084_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_252d_base_v084_signal']
    },
    'f22mt_nm_cv_504d_base_v085_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_504d_base_v085_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_504d_base_v085_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_504d_base_v085_signal']
    },
    'f22mt_nm_cv_756d_base_v086_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_756d_base_v086_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_756d_base_v086_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_756d_base_v086_signal']
    },
    'f22mt_nm_cv_1260d_base_v087_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_1260d_base_v087_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_1260d_base_v087_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_1260d_base_v087_signal']
    },
    'f22mt_gm_rel_sma_63d_base_v088_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_63d_base_v088_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_63d_base_v088_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_63d_base_v088_signal']
    },
    'f22mt_gm_rel_sma_126d_base_v089_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_126d_base_v089_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_126d_base_v089_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_126d_base_v089_signal']
    },
    'f22mt_gm_rel_sma_252d_base_v090_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_252d_base_v090_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_252d_base_v090_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_252d_base_v090_signal']
    },
    'f22mt_gm_rel_sma_504d_base_v091_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_504d_base_v091_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_504d_base_v091_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_504d_base_v091_signal']
    },
    'f22mt_gm_rel_sma_756d_base_v092_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_756d_base_v092_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_756d_base_v092_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_756d_base_v092_signal']
    },
    'f22mt_gm_rel_sma_1260d_base_v093_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_1260d_base_v093_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_1260d_base_v093_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_1260d_base_v093_signal']
    },
    'f22mt_ebitdam_rel_sma_63d_base_v094_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_63d_base_v094_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_63d_base_v094_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_63d_base_v094_signal']
    },
    'f22mt_ebitdam_rel_sma_126d_base_v095_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_126d_base_v095_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_126d_base_v095_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_126d_base_v095_signal']
    },
    'f22mt_ebitdam_rel_sma_252d_base_v096_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_252d_base_v096_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_252d_base_v096_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_252d_base_v096_signal']
    },
    'f22mt_ebitdam_rel_sma_504d_base_v097_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_504d_base_v097_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_504d_base_v097_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_504d_base_v097_signal']
    },
    'f22mt_ebitdam_rel_sma_756d_base_v098_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_756d_base_v098_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_756d_base_v098_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_756d_base_v098_signal']
    },
    'f22mt_ebitdam_rel_sma_1260d_base_v099_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_1260d_base_v099_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_1260d_base_v099_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_1260d_base_v099_signal']
    },
    'f22mt_opm_rel_sma_63d_base_v100_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_63d_base_v100_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_63d_base_v100_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_63d_base_v100_signal']
    },
    'f22mt_opm_rel_sma_126d_base_v101_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_126d_base_v101_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_126d_base_v101_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_126d_base_v101_signal']
    },
    'f22mt_opm_rel_sma_252d_base_v102_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_252d_base_v102_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_252d_base_v102_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_252d_base_v102_signal']
    },
    'f22mt_opm_rel_sma_504d_base_v103_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_504d_base_v103_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_504d_base_v103_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_504d_base_v103_signal']
    },
    'f22mt_opm_rel_sma_756d_base_v104_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_756d_base_v104_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_756d_base_v104_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_756d_base_v104_signal']
    },
    'f22mt_opm_rel_sma_1260d_base_v105_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_1260d_base_v105_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_1260d_base_v105_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_1260d_base_v105_signal']
    },
    'f22mt_nm_rel_sma_63d_base_v106_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_63d_base_v106_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_63d_base_v106_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_63d_base_v106_signal']
    },
    'f22mt_nm_rel_sma_126d_base_v107_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_126d_base_v107_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_126d_base_v107_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_126d_base_v107_signal']
    },
    'f22mt_nm_rel_sma_252d_base_v108_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_252d_base_v108_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_252d_base_v108_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_252d_base_v108_signal']
    },
    'f22mt_nm_rel_sma_504d_base_v109_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_504d_base_v109_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_504d_base_v109_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_504d_base_v109_signal']
    },
    'f22mt_nm_rel_sma_756d_base_v110_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_756d_base_v110_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_756d_base_v110_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_756d_base_v110_signal']
    },
    'f22mt_nm_rel_sma_1260d_base_v111_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_1260d_base_v111_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_1260d_base_v111_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_1260d_base_v111_signal']
    },
    'f22mt_egm_delta_63d_base_v112_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_63d_base_v112_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_63d_base_v112_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_63d_base_v112_signal']
    },
    'f22mt_egm_delta_126d_base_v113_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_126d_base_v113_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_126d_base_v113_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_126d_base_v113_signal']
    },
    'f22mt_egm_delta_252d_base_v114_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_252d_base_v114_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_252d_base_v114_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_252d_base_v114_signal']
    },
    'f22mt_egm_delta_504d_base_v115_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_504d_base_v115_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_504d_base_v115_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_504d_base_v115_signal']
    },
    'f22mt_egm_delta_756d_base_v116_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_756d_base_v116_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_756d_base_v116_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_756d_base_v116_signal']
    },
    'f22mt_egm_delta_1260d_base_v117_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_1260d_base_v117_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_1260d_base_v117_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_1260d_base_v117_signal']
    },
    'f22mt_ogm_delta_63d_base_v118_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_63d_base_v118_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_63d_base_v118_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_63d_base_v118_signal']
    },
    'f22mt_ogm_delta_126d_base_v119_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_126d_base_v119_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_126d_base_v119_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_126d_base_v119_signal']
    },
    'f22mt_ogm_delta_252d_base_v120_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_252d_base_v120_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_252d_base_v120_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_252d_base_v120_signal']
    },
    'f22mt_ogm_delta_504d_base_v121_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_504d_base_v121_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_504d_base_v121_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_504d_base_v121_signal']
    },
    'f22mt_ogm_delta_756d_base_v122_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_756d_base_v122_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_756d_base_v122_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_756d_base_v122_signal']
    },
    'f22mt_ogm_delta_1260d_base_v123_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_1260d_base_v123_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_1260d_base_v123_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_1260d_base_v123_signal']
    },
    'f22mt_ngm_delta_63d_base_v124_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_63d_base_v124_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_63d_base_v124_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_63d_base_v124_signal']
    },
    'f22mt_ngm_delta_126d_base_v125_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_126d_base_v125_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_126d_base_v125_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_126d_base_v125_signal']
    },
    'f22mt_ngm_delta_252d_base_v126_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_252d_base_v126_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_252d_base_v126_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_252d_base_v126_signal']
    },
    'f22mt_ngm_delta_504d_base_v127_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_504d_base_v127_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_504d_base_v127_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_504d_base_v127_signal']
    },
    'f22mt_ngm_delta_756d_base_v128_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_756d_base_v128_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_756d_base_v128_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_756d_base_v128_signal']
    },
    'f22mt_ngm_delta_1260d_base_v129_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_1260d_base_v129_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_1260d_base_v129_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_1260d_base_v129_signal']
    },
    'f22mt_nem_delta_63d_base_v130_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_63d_base_v130_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_63d_base_v130_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_63d_base_v130_signal']
    },
    'f22mt_nem_delta_126d_base_v131_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_126d_base_v131_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_126d_base_v131_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_126d_base_v131_signal']
    },
    'f22mt_nem_delta_252d_base_v132_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_252d_base_v132_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_252d_base_v132_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_252d_base_v132_signal']
    },
    'f22mt_nem_delta_504d_base_v133_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_504d_base_v133_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_504d_base_v133_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_504d_base_v133_signal']
    },
    'f22mt_nem_delta_756d_base_v134_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_756d_base_v134_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_756d_base_v134_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_756d_base_v134_signal']
    },
    'f22mt_nem_delta_1260d_base_v135_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_1260d_base_v135_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_1260d_base_v135_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_1260d_base_v135_signal']
    },
    'f22mt_nom_delta_63d_base_v136_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_63d_base_v136_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_63d_base_v136_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_63d_base_v136_signal']
    },
    'f22mt_nom_delta_126d_base_v137_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_126d_base_v137_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_126d_base_v137_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_126d_base_v137_signal']
    },
    'f22mt_nom_delta_252d_base_v138_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_252d_base_v138_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_252d_base_v138_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_252d_base_v138_signal']
    },
    'f22mt_nom_delta_504d_base_v139_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_504d_base_v139_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_504d_base_v139_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_504d_base_v139_signal']
    },
    'f22mt_nom_delta_756d_base_v140_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_756d_base_v140_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_756d_base_v140_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_756d_base_v140_signal']
    },
    'f22mt_nom_delta_1260d_base_v141_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_1260d_base_v141_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_1260d_base_v141_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_1260d_base_v141_signal']
    },
    'f22mt_egm_z_63d_base_v142_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_63d_base_v142_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_63d_base_v142_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_63d_base_v142_signal']
    },
    'f22mt_egm_z_126d_base_v143_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_126d_base_v143_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_126d_base_v143_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_126d_base_v143_signal']
    },
    'f22mt_egm_z_252d_base_v144_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_252d_base_v144_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_252d_base_v144_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_252d_base_v144_signal']
    },
    'f22mt_egm_z_504d_base_v145_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_504d_base_v145_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_504d_base_v145_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_504d_base_v145_signal']
    },
    'f22mt_egm_z_756d_base_v146_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_756d_base_v146_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_756d_base_v146_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_756d_base_v146_signal']
    },
    'f22mt_egm_z_1260d_base_v147_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_1260d_base_v147_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_1260d_base_v147_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_1260d_base_v147_signal']
    },
    'f22mt_ogm_z_63d_base_v148_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_z_63d_base_v148_signal'].__code__.co_varnames[:globals()['f22mt_ogm_z_63d_base_v148_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_z_63d_base_v148_signal']
    },
    'f22mt_ogm_z_126d_base_v149_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_z_126d_base_v149_signal'].__code__.co_varnames[:globals()['f22mt_ogm_z_126d_base_v149_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_z_126d_base_v149_signal']
    },
    'f22mt_ogm_z_252d_base_v150_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_z_252d_base_v150_signal'].__code__.co_varnames[:globals()['f22mt_ogm_z_252d_base_v150_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_z_252d_base_v150_signal']
    },
}

if __name__ == "__main__":
    sz = 1500
    np.random.seed(42)
    d = pd.DataFrame({
        "arg_gp": pd.Series(np.random.lognormal(10, 1, sz)),
        "arg_ebitda": pd.Series(np.random.lognormal(9, 1, sz)),
        "arg_opinc": pd.Series(np.random.lognormal(8.5, 1, sz)),
        "arg_netinc": pd.Series(np.random.lognormal(8, 1, sz)),
        "arg_revenue": pd.Series(np.random.lognormal(11, 1, sz)),
    })
    for n, c in f22mt_BASE_076_150_REGISTRY.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        q = r.iloc[1260:]
        if len(q.dropna()) > 0:
            assert q.nunique() > 2, f"{n} failed nunique: {q.nunique()}"
            assert q.std() > 0, f"{n} failed std: {q.std()}"
    print("OK")
