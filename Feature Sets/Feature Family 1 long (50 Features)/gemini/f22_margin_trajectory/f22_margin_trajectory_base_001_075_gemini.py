import pandas as pd
import numpy as np
import inspect

def _mt_margin(num, den): return num / den.replace(0, np.nan)
def _mt_delta(s, w): return s.diff(w)
def _sma(s, w): return s.rolling(w, min_periods=min(w, 20)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)
def _cv(s, w): return _std(s, w) / _sma(s, w).replace(0, np.nan)

# Raw gm
def f22mt_gm_base_v001_signal(arg_gp, arg_revenue) -> pd.Series:
    res = arg_gp / arg_revenue.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ebitdam
def f22mt_ebitdam_base_v002_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = arg_ebitda / arg_revenue.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw opm
def f22mt_opm_base_v003_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = arg_opinc / arg_revenue.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw nm
def f22mt_nm_base_v004_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = arg_netinc / arg_revenue.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw egm
def f22mt_egm_base_v005_signal(arg_ebitda, arg_gp) -> pd.Series:
    res = arg_ebitda / arg_gp.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ogm
def f22mt_ogm_base_v006_signal(arg_opinc, arg_gp) -> pd.Series:
    res = arg_opinc / arg_gp.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ngm
def f22mt_ngm_base_v007_signal(arg_netinc, arg_gp) -> pd.Series:
    res = arg_netinc / arg_gp.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw nem
def f22mt_nem_base_v008_signal(arg_netinc, arg_ebitda) -> pd.Series:
    res = arg_netinc / arg_ebitda.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw nom
def f22mt_nom_base_v009_signal(arg_netinc, arg_opinc) -> pd.Series:
    res = arg_netinc / arg_opinc.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 63d
def f22mt_olp_63d_base_v010_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = arg_ebitda.pct_change(63) - arg_revenue.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 126d
def f22mt_olp_126d_base_v011_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = arg_ebitda.pct_change(126) - arg_revenue.pct_change(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 252d
def f22mt_olp_252d_base_v012_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = arg_ebitda.pct_change(252) - arg_revenue.pct_change(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 504d
def f22mt_olp_504d_base_v013_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = arg_ebitda.pct_change(504) - arg_revenue.pct_change(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 756d
def f22mt_olp_756d_base_v014_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = arg_ebitda.pct_change(756) - arg_revenue.pct_change(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 1260d
def f22mt_olp_1260d_base_v015_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = arg_ebitda.pct_change(1260) - arg_revenue.pct_change(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 63d
def f22mt_gm_delta_63d_base_v016_signal(arg_gp, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_gp, arg_revenue)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 126d
def f22mt_gm_delta_126d_base_v017_signal(arg_gp, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_gp, arg_revenue)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 252d
def f22mt_gm_delta_252d_base_v018_signal(arg_gp, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_gp, arg_revenue)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 504d
def f22mt_gm_delta_504d_base_v019_signal(arg_gp, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_gp, arg_revenue)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 756d
def f22mt_gm_delta_756d_base_v020_signal(arg_gp, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_gp, arg_revenue)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 1260d
def f22mt_gm_delta_1260d_base_v021_signal(arg_gp, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_gp, arg_revenue)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 63d
def f22mt_ebitdam_delta_63d_base_v022_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_revenue)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 126d
def f22mt_ebitdam_delta_126d_base_v023_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_revenue)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 252d
def f22mt_ebitdam_delta_252d_base_v024_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_revenue)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 504d
def f22mt_ebitdam_delta_504d_base_v025_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_revenue)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 756d
def f22mt_ebitdam_delta_756d_base_v026_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_revenue)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 1260d
def f22mt_ebitdam_delta_1260d_base_v027_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_ebitda, arg_revenue)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 63d
def f22mt_opm_delta_63d_base_v028_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_revenue)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 126d
def f22mt_opm_delta_126d_base_v029_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_revenue)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 252d
def f22mt_opm_delta_252d_base_v030_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_revenue)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 504d
def f22mt_opm_delta_504d_base_v031_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_revenue)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 756d
def f22mt_opm_delta_756d_base_v032_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_revenue)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 1260d
def f22mt_opm_delta_1260d_base_v033_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_opinc, arg_revenue)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 63d
def f22mt_nm_delta_63d_base_v034_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_revenue)).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 126d
def f22mt_nm_delta_126d_base_v035_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_revenue)).diff(126)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 252d
def f22mt_nm_delta_252d_base_v036_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_revenue)).diff(252)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 504d
def f22mt_nm_delta_504d_base_v037_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_revenue)).diff(504)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 756d
def f22mt_nm_delta_756d_base_v038_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_revenue)).diff(756)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 1260d
def f22mt_nm_delta_1260d_base_v039_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = (_mt_margin(arg_netinc, arg_revenue)).diff(1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 63d
def f22mt_gm_z_63d_base_v040_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_gp, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 126d
def f22mt_gm_z_126d_base_v041_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_gp, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 252d
def f22mt_gm_z_252d_base_v042_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_gp, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 504d
def f22mt_gm_z_504d_base_v043_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_gp, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 756d
def f22mt_gm_z_756d_base_v044_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_gp, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 1260d
def f22mt_gm_z_1260d_base_v045_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_gp, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 63d
def f22mt_ebitdam_z_63d_base_v046_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 126d
def f22mt_ebitdam_z_126d_base_v047_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 252d
def f22mt_ebitdam_z_252d_base_v048_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 504d
def f22mt_ebitdam_z_504d_base_v049_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 756d
def f22mt_ebitdam_z_756d_base_v050_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 1260d
def f22mt_ebitdam_z_1260d_base_v051_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_ebitda, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 63d
def f22mt_opm_z_63d_base_v052_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 126d
def f22mt_opm_z_126d_base_v053_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 252d
def f22mt_opm_z_252d_base_v054_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 504d
def f22mt_opm_z_504d_base_v055_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 756d
def f22mt_opm_z_756d_base_v056_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 1260d
def f22mt_opm_z_1260d_base_v057_signal(arg_opinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_opinc, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 63d
def f22mt_nm_z_63d_base_v058_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_netinc, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 126d
def f22mt_nm_z_126d_base_v059_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_netinc, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 252d
def f22mt_nm_z_252d_base_v060_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_netinc, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 504d
def f22mt_nm_z_504d_base_v061_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_netinc, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 756d
def f22mt_nm_z_756d_base_v062_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_netinc, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 1260d
def f22mt_nm_z_1260d_base_v063_signal(arg_netinc, arg_revenue) -> pd.Series:
    res = _z(_mt_margin(arg_netinc, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 63d
def f22mt_gm_cv_63d_base_v064_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_gp, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 126d
def f22mt_gm_cv_126d_base_v065_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_gp, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 252d
def f22mt_gm_cv_252d_base_v066_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_gp, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 504d
def f22mt_gm_cv_504d_base_v067_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_gp, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 756d
def f22mt_gm_cv_756d_base_v068_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_gp, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 1260d
def f22mt_gm_cv_1260d_base_v069_signal(arg_gp, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_gp, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 63d
def f22mt_ebitdam_cv_63d_base_v070_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_ebitda, arg_revenue), 63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 126d
def f22mt_ebitdam_cv_126d_base_v071_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_ebitda, arg_revenue), 126)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 252d
def f22mt_ebitdam_cv_252d_base_v072_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_ebitda, arg_revenue), 252)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 504d
def f22mt_ebitdam_cv_504d_base_v073_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_ebitda, arg_revenue), 504)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 756d
def f22mt_ebitdam_cv_756d_base_v074_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_ebitda, arg_revenue), 756)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 1260d
def f22mt_ebitdam_cv_1260d_base_v075_signal(arg_ebitda, arg_revenue) -> pd.Series:
    res = _cv(_mt_margin(arg_ebitda, arg_revenue), 1260)
    return res.replace([np.inf, -np.inf], np.nan)

f22mt_BASE_001_075_REGISTRY = {
    'f22mt_gm_base_v001_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_base_v001_signal'].__code__.co_varnames[:globals()['f22mt_gm_base_v001_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_base_v001_signal']
    },
    'f22mt_ebitdam_base_v002_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_base_v002_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_base_v002_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_base_v002_signal']
    },
    'f22mt_opm_base_v003_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_base_v003_signal'].__code__.co_varnames[:globals()['f22mt_opm_base_v003_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_base_v003_signal']
    },
    'f22mt_nm_base_v004_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_base_v004_signal'].__code__.co_varnames[:globals()['f22mt_nm_base_v004_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_base_v004_signal']
    },
    'f22mt_egm_base_v005_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_base_v005_signal'].__code__.co_varnames[:globals()['f22mt_egm_base_v005_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_base_v005_signal']
    },
    'f22mt_ogm_base_v006_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_base_v006_signal'].__code__.co_varnames[:globals()['f22mt_ogm_base_v006_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_base_v006_signal']
    },
    'f22mt_ngm_base_v007_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_base_v007_signal'].__code__.co_varnames[:globals()['f22mt_ngm_base_v007_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_base_v007_signal']
    },
    'f22mt_nem_base_v008_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_base_v008_signal'].__code__.co_varnames[:globals()['f22mt_nem_base_v008_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_base_v008_signal']
    },
    'f22mt_nom_base_v009_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_base_v009_signal'].__code__.co_varnames[:globals()['f22mt_nom_base_v009_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_base_v009_signal']
    },
    'f22mt_olp_63d_base_v010_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_63d_base_v010_signal'].__code__.co_varnames[:globals()['f22mt_olp_63d_base_v010_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_63d_base_v010_signal']
    },
    'f22mt_olp_126d_base_v011_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_126d_base_v011_signal'].__code__.co_varnames[:globals()['f22mt_olp_126d_base_v011_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_126d_base_v011_signal']
    },
    'f22mt_olp_252d_base_v012_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_252d_base_v012_signal'].__code__.co_varnames[:globals()['f22mt_olp_252d_base_v012_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_252d_base_v012_signal']
    },
    'f22mt_olp_504d_base_v013_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_504d_base_v013_signal'].__code__.co_varnames[:globals()['f22mt_olp_504d_base_v013_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_504d_base_v013_signal']
    },
    'f22mt_olp_756d_base_v014_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_756d_base_v014_signal'].__code__.co_varnames[:globals()['f22mt_olp_756d_base_v014_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_756d_base_v014_signal']
    },
    'f22mt_olp_1260d_base_v015_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_1260d_base_v015_signal'].__code__.co_varnames[:globals()['f22mt_olp_1260d_base_v015_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_1260d_base_v015_signal']
    },
    'f22mt_gm_delta_63d_base_v016_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_63d_base_v016_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_63d_base_v016_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_63d_base_v016_signal']
    },
    'f22mt_gm_delta_126d_base_v017_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_126d_base_v017_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_126d_base_v017_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_126d_base_v017_signal']
    },
    'f22mt_gm_delta_252d_base_v018_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_252d_base_v018_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_252d_base_v018_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_252d_base_v018_signal']
    },
    'f22mt_gm_delta_504d_base_v019_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_504d_base_v019_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_504d_base_v019_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_504d_base_v019_signal']
    },
    'f22mt_gm_delta_756d_base_v020_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_756d_base_v020_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_756d_base_v020_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_756d_base_v020_signal']
    },
    'f22mt_gm_delta_1260d_base_v021_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_1260d_base_v021_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_1260d_base_v021_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_1260d_base_v021_signal']
    },
    'f22mt_ebitdam_delta_63d_base_v022_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_63d_base_v022_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_63d_base_v022_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_63d_base_v022_signal']
    },
    'f22mt_ebitdam_delta_126d_base_v023_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_126d_base_v023_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_126d_base_v023_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_126d_base_v023_signal']
    },
    'f22mt_ebitdam_delta_252d_base_v024_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_252d_base_v024_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_252d_base_v024_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_252d_base_v024_signal']
    },
    'f22mt_ebitdam_delta_504d_base_v025_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_504d_base_v025_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_504d_base_v025_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_504d_base_v025_signal']
    },
    'f22mt_ebitdam_delta_756d_base_v026_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_756d_base_v026_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_756d_base_v026_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_756d_base_v026_signal']
    },
    'f22mt_ebitdam_delta_1260d_base_v027_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_1260d_base_v027_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_1260d_base_v027_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_1260d_base_v027_signal']
    },
    'f22mt_opm_delta_63d_base_v028_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_63d_base_v028_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_63d_base_v028_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_63d_base_v028_signal']
    },
    'f22mt_opm_delta_126d_base_v029_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_126d_base_v029_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_126d_base_v029_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_126d_base_v029_signal']
    },
    'f22mt_opm_delta_252d_base_v030_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_252d_base_v030_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_252d_base_v030_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_252d_base_v030_signal']
    },
    'f22mt_opm_delta_504d_base_v031_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_504d_base_v031_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_504d_base_v031_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_504d_base_v031_signal']
    },
    'f22mt_opm_delta_756d_base_v032_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_756d_base_v032_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_756d_base_v032_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_756d_base_v032_signal']
    },
    'f22mt_opm_delta_1260d_base_v033_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_1260d_base_v033_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_1260d_base_v033_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_1260d_base_v033_signal']
    },
    'f22mt_nm_delta_63d_base_v034_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_63d_base_v034_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_63d_base_v034_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_63d_base_v034_signal']
    },
    'f22mt_nm_delta_126d_base_v035_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_126d_base_v035_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_126d_base_v035_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_126d_base_v035_signal']
    },
    'f22mt_nm_delta_252d_base_v036_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_252d_base_v036_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_252d_base_v036_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_252d_base_v036_signal']
    },
    'f22mt_nm_delta_504d_base_v037_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_504d_base_v037_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_504d_base_v037_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_504d_base_v037_signal']
    },
    'f22mt_nm_delta_756d_base_v038_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_756d_base_v038_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_756d_base_v038_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_756d_base_v038_signal']
    },
    'f22mt_nm_delta_1260d_base_v039_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_1260d_base_v039_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_1260d_base_v039_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_1260d_base_v039_signal']
    },
    'f22mt_gm_z_63d_base_v040_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_63d_base_v040_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_63d_base_v040_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_63d_base_v040_signal']
    },
    'f22mt_gm_z_126d_base_v041_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_126d_base_v041_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_126d_base_v041_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_126d_base_v041_signal']
    },
    'f22mt_gm_z_252d_base_v042_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_252d_base_v042_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_252d_base_v042_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_252d_base_v042_signal']
    },
    'f22mt_gm_z_504d_base_v043_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_504d_base_v043_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_504d_base_v043_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_504d_base_v043_signal']
    },
    'f22mt_gm_z_756d_base_v044_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_756d_base_v044_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_756d_base_v044_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_756d_base_v044_signal']
    },
    'f22mt_gm_z_1260d_base_v045_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_1260d_base_v045_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_1260d_base_v045_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_1260d_base_v045_signal']
    },
    'f22mt_ebitdam_z_63d_base_v046_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_63d_base_v046_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_63d_base_v046_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_63d_base_v046_signal']
    },
    'f22mt_ebitdam_z_126d_base_v047_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_126d_base_v047_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_126d_base_v047_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_126d_base_v047_signal']
    },
    'f22mt_ebitdam_z_252d_base_v048_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_252d_base_v048_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_252d_base_v048_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_252d_base_v048_signal']
    },
    'f22mt_ebitdam_z_504d_base_v049_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_504d_base_v049_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_504d_base_v049_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_504d_base_v049_signal']
    },
    'f22mt_ebitdam_z_756d_base_v050_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_756d_base_v050_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_756d_base_v050_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_756d_base_v050_signal']
    },
    'f22mt_ebitdam_z_1260d_base_v051_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_1260d_base_v051_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_1260d_base_v051_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_1260d_base_v051_signal']
    },
    'f22mt_opm_z_63d_base_v052_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_63d_base_v052_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_63d_base_v052_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_63d_base_v052_signal']
    },
    'f22mt_opm_z_126d_base_v053_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_126d_base_v053_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_126d_base_v053_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_126d_base_v053_signal']
    },
    'f22mt_opm_z_252d_base_v054_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_252d_base_v054_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_252d_base_v054_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_252d_base_v054_signal']
    },
    'f22mt_opm_z_504d_base_v055_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_504d_base_v055_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_504d_base_v055_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_504d_base_v055_signal']
    },
    'f22mt_opm_z_756d_base_v056_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_756d_base_v056_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_756d_base_v056_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_756d_base_v056_signal']
    },
    'f22mt_opm_z_1260d_base_v057_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_1260d_base_v057_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_1260d_base_v057_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_1260d_base_v057_signal']
    },
    'f22mt_nm_z_63d_base_v058_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_63d_base_v058_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_63d_base_v058_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_63d_base_v058_signal']
    },
    'f22mt_nm_z_126d_base_v059_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_126d_base_v059_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_126d_base_v059_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_126d_base_v059_signal']
    },
    'f22mt_nm_z_252d_base_v060_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_252d_base_v060_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_252d_base_v060_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_252d_base_v060_signal']
    },
    'f22mt_nm_z_504d_base_v061_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_504d_base_v061_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_504d_base_v061_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_504d_base_v061_signal']
    },
    'f22mt_nm_z_756d_base_v062_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_756d_base_v062_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_756d_base_v062_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_756d_base_v062_signal']
    },
    'f22mt_nm_z_1260d_base_v063_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_1260d_base_v063_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_1260d_base_v063_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_1260d_base_v063_signal']
    },
    'f22mt_gm_cv_63d_base_v064_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_63d_base_v064_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_63d_base_v064_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_63d_base_v064_signal']
    },
    'f22mt_gm_cv_126d_base_v065_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_126d_base_v065_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_126d_base_v065_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_126d_base_v065_signal']
    },
    'f22mt_gm_cv_252d_base_v066_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_252d_base_v066_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_252d_base_v066_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_252d_base_v066_signal']
    },
    'f22mt_gm_cv_504d_base_v067_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_504d_base_v067_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_504d_base_v067_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_504d_base_v067_signal']
    },
    'f22mt_gm_cv_756d_base_v068_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_756d_base_v068_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_756d_base_v068_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_756d_base_v068_signal']
    },
    'f22mt_gm_cv_1260d_base_v069_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_1260d_base_v069_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_1260d_base_v069_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_1260d_base_v069_signal']
    },
    'f22mt_ebitdam_cv_63d_base_v070_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_63d_base_v070_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_63d_base_v070_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_63d_base_v070_signal']
    },
    'f22mt_ebitdam_cv_126d_base_v071_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_126d_base_v071_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_126d_base_v071_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_126d_base_v071_signal']
    },
    'f22mt_ebitdam_cv_252d_base_v072_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_252d_base_v072_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_252d_base_v072_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_252d_base_v072_signal']
    },
    'f22mt_ebitdam_cv_504d_base_v073_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_504d_base_v073_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_504d_base_v073_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_504d_base_v073_signal']
    },
    'f22mt_ebitdam_cv_756d_base_v074_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_756d_base_v074_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_756d_base_v074_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_756d_base_v074_signal']
    },
    'f22mt_ebitdam_cv_1260d_base_v075_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_1260d_base_v075_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_1260d_base_v075_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_1260d_base_v075_signal']
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
    for n, c in f22mt_BASE_001_075_REGISTRY.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        q = r.iloc[1260:]
        if len(q.dropna()) > 0:
            assert q.nunique() > 2, f"{n} failed nunique: {q.nunique()}"
            assert q.std() > 0, f"{n} failed std: {q.std()}"
    print("OK")
