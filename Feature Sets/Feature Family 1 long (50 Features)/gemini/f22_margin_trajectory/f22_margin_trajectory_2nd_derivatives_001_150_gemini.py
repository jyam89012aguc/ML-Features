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
def f22mt_gm_slope_v001_signal(arg_gp, arg_revenue) -> pd.Series:
    base = arg_gp / arg_revenue.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ebitdam
def f22mt_ebitdam_slope_v002_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = arg_ebitda / arg_revenue.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw opm
def f22mt_opm_slope_v003_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = arg_opinc / arg_revenue.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw nm
def f22mt_nm_slope_v004_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = arg_netinc / arg_revenue.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw egm
def f22mt_egm_slope_v005_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = arg_ebitda / arg_gp.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ogm
def f22mt_ogm_slope_v006_signal(arg_opinc, arg_gp) -> pd.Series:
    base = arg_opinc / arg_gp.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw ngm
def f22mt_ngm_slope_v007_signal(arg_netinc, arg_gp) -> pd.Series:
    base = arg_netinc / arg_gp.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw nem
def f22mt_nem_slope_v008_signal(arg_netinc, arg_ebitda) -> pd.Series:
    base = arg_netinc / arg_ebitda.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Raw nom
def f22mt_nom_slope_v009_signal(arg_netinc, arg_opinc) -> pd.Series:
    base = arg_netinc / arg_opinc.replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 63d
def f22mt_olp_63d_slope_v010_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = arg_ebitda.pct_change(63) - arg_revenue.pct_change(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 126d
def f22mt_olp_126d_slope_v011_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = arg_ebitda.pct_change(126) - arg_revenue.pct_change(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 252d
def f22mt_olp_252d_slope_v012_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = arg_ebitda.pct_change(252) - arg_revenue.pct_change(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 504d
def f22mt_olp_504d_slope_v013_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = arg_ebitda.pct_change(504) - arg_revenue.pct_change(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 756d
def f22mt_olp_756d_slope_v014_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = arg_ebitda.pct_change(756) - arg_revenue.pct_change(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Operating Leverage Proxy over 1260d
def f22mt_olp_1260d_slope_v015_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = arg_ebitda.pct_change(1260) - arg_revenue.pct_change(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 63d
def f22mt_gm_delta_63d_slope_v016_signal(arg_gp, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_gp, arg_revenue)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 126d
def f22mt_gm_delta_126d_slope_v017_signal(arg_gp, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_gp, arg_revenue)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 252d
def f22mt_gm_delta_252d_slope_v018_signal(arg_gp, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_gp, arg_revenue)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 504d
def f22mt_gm_delta_504d_slope_v019_signal(arg_gp, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_gp, arg_revenue)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 756d
def f22mt_gm_delta_756d_slope_v020_signal(arg_gp, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_gp, arg_revenue)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of gm over 1260d
def f22mt_gm_delta_1260d_slope_v021_signal(arg_gp, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_gp, arg_revenue)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 63d
def f22mt_ebitdam_delta_63d_slope_v022_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_revenue)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 126d
def f22mt_ebitdam_delta_126d_slope_v023_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_revenue)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 252d
def f22mt_ebitdam_delta_252d_slope_v024_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_revenue)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 504d
def f22mt_ebitdam_delta_504d_slope_v025_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_revenue)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 756d
def f22mt_ebitdam_delta_756d_slope_v026_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_revenue)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ebitdam over 1260d
def f22mt_ebitdam_delta_1260d_slope_v027_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_revenue)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 63d
def f22mt_opm_delta_63d_slope_v028_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_revenue)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 126d
def f22mt_opm_delta_126d_slope_v029_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_revenue)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 252d
def f22mt_opm_delta_252d_slope_v030_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_revenue)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 504d
def f22mt_opm_delta_504d_slope_v031_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_revenue)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 756d
def f22mt_opm_delta_756d_slope_v032_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_revenue)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of opm over 1260d
def f22mt_opm_delta_1260d_slope_v033_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_revenue)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 63d
def f22mt_nm_delta_63d_slope_v034_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_revenue)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 126d
def f22mt_nm_delta_126d_slope_v035_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_revenue)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 252d
def f22mt_nm_delta_252d_slope_v036_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_revenue)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 504d
def f22mt_nm_delta_504d_slope_v037_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_revenue)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 756d
def f22mt_nm_delta_756d_slope_v038_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_revenue)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nm over 1260d
def f22mt_nm_delta_1260d_slope_v039_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_revenue)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 63d
def f22mt_gm_z_63d_slope_v040_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_gp, arg_revenue), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 126d
def f22mt_gm_z_126d_slope_v041_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_gp, arg_revenue), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 252d
def f22mt_gm_z_252d_slope_v042_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_gp, arg_revenue), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 504d
def f22mt_gm_z_504d_slope_v043_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_gp, arg_revenue), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 756d
def f22mt_gm_z_756d_slope_v044_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_gp, arg_revenue), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of gm over 1260d
def f22mt_gm_z_1260d_slope_v045_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_gp, arg_revenue), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 63d
def f22mt_ebitdam_z_63d_slope_v046_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_revenue), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 126d
def f22mt_ebitdam_z_126d_slope_v047_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_revenue), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 252d
def f22mt_ebitdam_z_252d_slope_v048_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_revenue), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 504d
def f22mt_ebitdam_z_504d_slope_v049_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_revenue), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 756d
def f22mt_ebitdam_z_756d_slope_v050_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_revenue), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ebitdam over 1260d
def f22mt_ebitdam_z_1260d_slope_v051_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_revenue), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 63d
def f22mt_opm_z_63d_slope_v052_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_revenue), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 126d
def f22mt_opm_z_126d_slope_v053_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_revenue), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 252d
def f22mt_opm_z_252d_slope_v054_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_revenue), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 504d
def f22mt_opm_z_504d_slope_v055_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_revenue), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 756d
def f22mt_opm_z_756d_slope_v056_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_revenue), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of opm over 1260d
def f22mt_opm_z_1260d_slope_v057_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_revenue), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 63d
def f22mt_nm_z_63d_slope_v058_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_netinc, arg_revenue), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 126d
def f22mt_nm_z_126d_slope_v059_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_netinc, arg_revenue), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 252d
def f22mt_nm_z_252d_slope_v060_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_netinc, arg_revenue), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 504d
def f22mt_nm_z_504d_slope_v061_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_netinc, arg_revenue), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 756d
def f22mt_nm_z_756d_slope_v062_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_netinc, arg_revenue), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of nm over 1260d
def f22mt_nm_z_1260d_slope_v063_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _z(_mt_margin(arg_netinc, arg_revenue), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 63d
def f22mt_gm_cv_63d_slope_v064_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_gp, arg_revenue), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 126d
def f22mt_gm_cv_126d_slope_v065_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_gp, arg_revenue), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 252d
def f22mt_gm_cv_252d_slope_v066_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_gp, arg_revenue), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 504d
def f22mt_gm_cv_504d_slope_v067_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_gp, arg_revenue), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 756d
def f22mt_gm_cv_756d_slope_v068_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_gp, arg_revenue), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of gm over 1260d
def f22mt_gm_cv_1260d_slope_v069_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_gp, arg_revenue), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 63d
def f22mt_ebitdam_cv_63d_slope_v070_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_ebitda, arg_revenue), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 126d
def f22mt_ebitdam_cv_126d_slope_v071_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_ebitda, arg_revenue), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 252d
def f22mt_ebitdam_cv_252d_slope_v072_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_ebitda, arg_revenue), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 504d
def f22mt_ebitdam_cv_504d_slope_v073_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_ebitda, arg_revenue), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 756d
def f22mt_ebitdam_cv_756d_slope_v074_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_ebitda, arg_revenue), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of ebitdam over 1260d
def f22mt_ebitdam_cv_1260d_slope_v075_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_ebitda, arg_revenue), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 63d
def f22mt_opm_cv_63d_slope_v076_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_opinc, arg_revenue), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 126d
def f22mt_opm_cv_126d_slope_v077_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_opinc, arg_revenue), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 252d
def f22mt_opm_cv_252d_slope_v078_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_opinc, arg_revenue), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 504d
def f22mt_opm_cv_504d_slope_v079_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_opinc, arg_revenue), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 756d
def f22mt_opm_cv_756d_slope_v080_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_opinc, arg_revenue), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of opm over 1260d
def f22mt_opm_cv_1260d_slope_v081_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_opinc, arg_revenue), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 63d
def f22mt_nm_cv_63d_slope_v082_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_netinc, arg_revenue), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 126d
def f22mt_nm_cv_126d_slope_v083_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_netinc, arg_revenue), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 252d
def f22mt_nm_cv_252d_slope_v084_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_netinc, arg_revenue), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 504d
def f22mt_nm_cv_504d_slope_v085_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_netinc, arg_revenue), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 756d
def f22mt_nm_cv_756d_slope_v086_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_netinc, arg_revenue), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Coefficient of Variation of nm over 1260d
def f22mt_nm_cv_1260d_slope_v087_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _cv(_mt_margin(arg_netinc, arg_revenue), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 63d SMA
def f22mt_gm_rel_sma_63d_slope_v088_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 63).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 126d SMA
def f22mt_gm_rel_sma_126d_slope_v089_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 126).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 252d SMA
def f22mt_gm_rel_sma_252d_slope_v090_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 252).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 504d SMA
def f22mt_gm_rel_sma_504d_slope_v091_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 504).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 756d SMA
def f22mt_gm_rel_sma_756d_slope_v092_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 756).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# gm relative to 1260d SMA
def f22mt_gm_rel_sma_1260d_slope_v093_signal(arg_gp, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_gp, arg_revenue) / _sma(_mt_margin(arg_gp, arg_revenue), 1260).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 63d SMA
def f22mt_ebitdam_rel_sma_63d_slope_v094_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 63).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 126d SMA
def f22mt_ebitdam_rel_sma_126d_slope_v095_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 126).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 252d SMA
def f22mt_ebitdam_rel_sma_252d_slope_v096_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 252).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 504d SMA
def f22mt_ebitdam_rel_sma_504d_slope_v097_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 504).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 756d SMA
def f22mt_ebitdam_rel_sma_756d_slope_v098_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 756).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# ebitdam relative to 1260d SMA
def f22mt_ebitdam_rel_sma_1260d_slope_v099_signal(arg_ebitda, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_ebitda, arg_revenue) / _sma(_mt_margin(arg_ebitda, arg_revenue), 1260).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 63d SMA
def f22mt_opm_rel_sma_63d_slope_v100_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 63).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 126d SMA
def f22mt_opm_rel_sma_126d_slope_v101_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 126).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 252d SMA
def f22mt_opm_rel_sma_252d_slope_v102_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 252).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 504d SMA
def f22mt_opm_rel_sma_504d_slope_v103_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 504).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 756d SMA
def f22mt_opm_rel_sma_756d_slope_v104_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 756).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# opm relative to 1260d SMA
def f22mt_opm_rel_sma_1260d_slope_v105_signal(arg_opinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_opinc, arg_revenue) / _sma(_mt_margin(arg_opinc, arg_revenue), 1260).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 63d SMA
def f22mt_nm_rel_sma_63d_slope_v106_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 63).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 126d SMA
def f22mt_nm_rel_sma_126d_slope_v107_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 126).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 252d SMA
def f22mt_nm_rel_sma_252d_slope_v108_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 252).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 504d SMA
def f22mt_nm_rel_sma_504d_slope_v109_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 504).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 756d SMA
def f22mt_nm_rel_sma_756d_slope_v110_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 756).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# nm relative to 1260d SMA
def f22mt_nm_rel_sma_1260d_slope_v111_signal(arg_netinc, arg_revenue) -> pd.Series:
    base = _mt_margin(arg_netinc, arg_revenue) / _sma(_mt_margin(arg_netinc, arg_revenue), 1260).replace(0, np.nan)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 63d
def f22mt_egm_delta_63d_slope_v112_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_gp)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 126d
def f22mt_egm_delta_126d_slope_v113_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_gp)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 252d
def f22mt_egm_delta_252d_slope_v114_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_gp)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 504d
def f22mt_egm_delta_504d_slope_v115_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_gp)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 756d
def f22mt_egm_delta_756d_slope_v116_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_gp)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of egm over 1260d
def f22mt_egm_delta_1260d_slope_v117_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_ebitda, arg_gp)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 63d
def f22mt_ogm_delta_63d_slope_v118_signal(arg_opinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_gp)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 126d
def f22mt_ogm_delta_126d_slope_v119_signal(arg_opinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_gp)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 252d
def f22mt_ogm_delta_252d_slope_v120_signal(arg_opinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_gp)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 504d
def f22mt_ogm_delta_504d_slope_v121_signal(arg_opinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_gp)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 756d
def f22mt_ogm_delta_756d_slope_v122_signal(arg_opinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_gp)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ogm over 1260d
def f22mt_ogm_delta_1260d_slope_v123_signal(arg_opinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_opinc, arg_gp)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 63d
def f22mt_ngm_delta_63d_slope_v124_signal(arg_netinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_gp)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 126d
def f22mt_ngm_delta_126d_slope_v125_signal(arg_netinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_gp)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 252d
def f22mt_ngm_delta_252d_slope_v126_signal(arg_netinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_gp)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 504d
def f22mt_ngm_delta_504d_slope_v127_signal(arg_netinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_gp)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 756d
def f22mt_ngm_delta_756d_slope_v128_signal(arg_netinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_gp)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of ngm over 1260d
def f22mt_ngm_delta_1260d_slope_v129_signal(arg_netinc, arg_gp) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_gp)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 63d
def f22mt_nem_delta_63d_slope_v130_signal(arg_netinc, arg_ebitda) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_ebitda)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 126d
def f22mt_nem_delta_126d_slope_v131_signal(arg_netinc, arg_ebitda) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_ebitda)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 252d
def f22mt_nem_delta_252d_slope_v132_signal(arg_netinc, arg_ebitda) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_ebitda)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 504d
def f22mt_nem_delta_504d_slope_v133_signal(arg_netinc, arg_ebitda) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_ebitda)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 756d
def f22mt_nem_delta_756d_slope_v134_signal(arg_netinc, arg_ebitda) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_ebitda)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nem over 1260d
def f22mt_nem_delta_1260d_slope_v135_signal(arg_netinc, arg_ebitda) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_ebitda)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 63d
def f22mt_nom_delta_63d_slope_v136_signal(arg_netinc, arg_opinc) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_opinc)).diff(63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 126d
def f22mt_nom_delta_126d_slope_v137_signal(arg_netinc, arg_opinc) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_opinc)).diff(126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 252d
def f22mt_nom_delta_252d_slope_v138_signal(arg_netinc, arg_opinc) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_opinc)).diff(252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 504d
def f22mt_nom_delta_504d_slope_v139_signal(arg_netinc, arg_opinc) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_opinc)).diff(504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 756d
def f22mt_nom_delta_756d_slope_v140_signal(arg_netinc, arg_opinc) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_opinc)).diff(756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Delta of nom over 1260d
def f22mt_nom_delta_1260d_slope_v141_signal(arg_netinc, arg_opinc) -> pd.Series:
    base = (_mt_margin(arg_netinc, arg_opinc)).diff(1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 63d
def f22mt_egm_z_63d_slope_v142_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_gp), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 126d
def f22mt_egm_z_126d_slope_v143_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_gp), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 252d
def f22mt_egm_z_252d_slope_v144_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_gp), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 504d
def f22mt_egm_z_504d_slope_v145_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_gp), 504)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 756d
def f22mt_egm_z_756d_slope_v146_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_gp), 756)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of egm over 1260d
def f22mt_egm_z_1260d_slope_v147_signal(arg_ebitda, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_ebitda, arg_gp), 1260)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ogm over 63d
def f22mt_ogm_z_63d_slope_v148_signal(arg_opinc, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_gp), 63)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ogm over 126d
def f22mt_ogm_z_126d_slope_v149_signal(arg_opinc, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_gp), 126)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

# Z-score of ogm over 252d
def f22mt_ogm_z_252d_slope_v150_signal(arg_opinc, arg_gp) -> pd.Series:
    base = _z(_mt_margin(arg_opinc, arg_gp), 252)
    res = base.diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

f22mt_SLOPE_001_150_REGISTRY = {
    'f22mt_gm_slope_v001_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_slope_v001_signal'].__code__.co_varnames[:globals()['f22mt_gm_slope_v001_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_slope_v001_signal']
    },
    'f22mt_ebitdam_slope_v002_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_slope_v002_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_slope_v002_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_slope_v002_signal']
    },
    'f22mt_opm_slope_v003_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_slope_v003_signal'].__code__.co_varnames[:globals()['f22mt_opm_slope_v003_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_slope_v003_signal']
    },
    'f22mt_nm_slope_v004_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_slope_v004_signal'].__code__.co_varnames[:globals()['f22mt_nm_slope_v004_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_slope_v004_signal']
    },
    'f22mt_egm_slope_v005_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_slope_v005_signal'].__code__.co_varnames[:globals()['f22mt_egm_slope_v005_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_slope_v005_signal']
    },
    'f22mt_ogm_slope_v006_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_slope_v006_signal'].__code__.co_varnames[:globals()['f22mt_ogm_slope_v006_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_slope_v006_signal']
    },
    'f22mt_ngm_slope_v007_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_slope_v007_signal'].__code__.co_varnames[:globals()['f22mt_ngm_slope_v007_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_slope_v007_signal']
    },
    'f22mt_nem_slope_v008_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_slope_v008_signal'].__code__.co_varnames[:globals()['f22mt_nem_slope_v008_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_slope_v008_signal']
    },
    'f22mt_nom_slope_v009_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_slope_v009_signal'].__code__.co_varnames[:globals()['f22mt_nom_slope_v009_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_slope_v009_signal']
    },
    'f22mt_olp_63d_slope_v010_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_63d_slope_v010_signal'].__code__.co_varnames[:globals()['f22mt_olp_63d_slope_v010_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_63d_slope_v010_signal']
    },
    'f22mt_olp_126d_slope_v011_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_126d_slope_v011_signal'].__code__.co_varnames[:globals()['f22mt_olp_126d_slope_v011_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_126d_slope_v011_signal']
    },
    'f22mt_olp_252d_slope_v012_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_252d_slope_v012_signal'].__code__.co_varnames[:globals()['f22mt_olp_252d_slope_v012_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_252d_slope_v012_signal']
    },
    'f22mt_olp_504d_slope_v013_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_504d_slope_v013_signal'].__code__.co_varnames[:globals()['f22mt_olp_504d_slope_v013_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_504d_slope_v013_signal']
    },
    'f22mt_olp_756d_slope_v014_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_756d_slope_v014_signal'].__code__.co_varnames[:globals()['f22mt_olp_756d_slope_v014_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_756d_slope_v014_signal']
    },
    'f22mt_olp_1260d_slope_v015_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_olp_1260d_slope_v015_signal'].__code__.co_varnames[:globals()['f22mt_olp_1260d_slope_v015_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_olp_1260d_slope_v015_signal']
    },
    'f22mt_gm_delta_63d_slope_v016_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_63d_slope_v016_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_63d_slope_v016_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_63d_slope_v016_signal']
    },
    'f22mt_gm_delta_126d_slope_v017_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_126d_slope_v017_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_126d_slope_v017_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_126d_slope_v017_signal']
    },
    'f22mt_gm_delta_252d_slope_v018_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_252d_slope_v018_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_252d_slope_v018_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_252d_slope_v018_signal']
    },
    'f22mt_gm_delta_504d_slope_v019_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_504d_slope_v019_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_504d_slope_v019_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_504d_slope_v019_signal']
    },
    'f22mt_gm_delta_756d_slope_v020_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_756d_slope_v020_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_756d_slope_v020_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_756d_slope_v020_signal']
    },
    'f22mt_gm_delta_1260d_slope_v021_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_delta_1260d_slope_v021_signal'].__code__.co_varnames[:globals()['f22mt_gm_delta_1260d_slope_v021_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_delta_1260d_slope_v021_signal']
    },
    'f22mt_ebitdam_delta_63d_slope_v022_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_63d_slope_v022_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_63d_slope_v022_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_63d_slope_v022_signal']
    },
    'f22mt_ebitdam_delta_126d_slope_v023_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_126d_slope_v023_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_126d_slope_v023_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_126d_slope_v023_signal']
    },
    'f22mt_ebitdam_delta_252d_slope_v024_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_252d_slope_v024_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_252d_slope_v024_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_252d_slope_v024_signal']
    },
    'f22mt_ebitdam_delta_504d_slope_v025_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_504d_slope_v025_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_504d_slope_v025_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_504d_slope_v025_signal']
    },
    'f22mt_ebitdam_delta_756d_slope_v026_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_756d_slope_v026_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_756d_slope_v026_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_756d_slope_v026_signal']
    },
    'f22mt_ebitdam_delta_1260d_slope_v027_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_delta_1260d_slope_v027_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_delta_1260d_slope_v027_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_delta_1260d_slope_v027_signal']
    },
    'f22mt_opm_delta_63d_slope_v028_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_63d_slope_v028_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_63d_slope_v028_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_63d_slope_v028_signal']
    },
    'f22mt_opm_delta_126d_slope_v029_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_126d_slope_v029_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_126d_slope_v029_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_126d_slope_v029_signal']
    },
    'f22mt_opm_delta_252d_slope_v030_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_252d_slope_v030_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_252d_slope_v030_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_252d_slope_v030_signal']
    },
    'f22mt_opm_delta_504d_slope_v031_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_504d_slope_v031_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_504d_slope_v031_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_504d_slope_v031_signal']
    },
    'f22mt_opm_delta_756d_slope_v032_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_756d_slope_v032_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_756d_slope_v032_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_756d_slope_v032_signal']
    },
    'f22mt_opm_delta_1260d_slope_v033_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_delta_1260d_slope_v033_signal'].__code__.co_varnames[:globals()['f22mt_opm_delta_1260d_slope_v033_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_delta_1260d_slope_v033_signal']
    },
    'f22mt_nm_delta_63d_slope_v034_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_63d_slope_v034_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_63d_slope_v034_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_63d_slope_v034_signal']
    },
    'f22mt_nm_delta_126d_slope_v035_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_126d_slope_v035_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_126d_slope_v035_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_126d_slope_v035_signal']
    },
    'f22mt_nm_delta_252d_slope_v036_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_252d_slope_v036_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_252d_slope_v036_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_252d_slope_v036_signal']
    },
    'f22mt_nm_delta_504d_slope_v037_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_504d_slope_v037_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_504d_slope_v037_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_504d_slope_v037_signal']
    },
    'f22mt_nm_delta_756d_slope_v038_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_756d_slope_v038_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_756d_slope_v038_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_756d_slope_v038_signal']
    },
    'f22mt_nm_delta_1260d_slope_v039_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_delta_1260d_slope_v039_signal'].__code__.co_varnames[:globals()['f22mt_nm_delta_1260d_slope_v039_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_delta_1260d_slope_v039_signal']
    },
    'f22mt_gm_z_63d_slope_v040_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_63d_slope_v040_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_63d_slope_v040_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_63d_slope_v040_signal']
    },
    'f22mt_gm_z_126d_slope_v041_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_126d_slope_v041_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_126d_slope_v041_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_126d_slope_v041_signal']
    },
    'f22mt_gm_z_252d_slope_v042_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_252d_slope_v042_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_252d_slope_v042_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_252d_slope_v042_signal']
    },
    'f22mt_gm_z_504d_slope_v043_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_504d_slope_v043_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_504d_slope_v043_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_504d_slope_v043_signal']
    },
    'f22mt_gm_z_756d_slope_v044_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_756d_slope_v044_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_756d_slope_v044_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_756d_slope_v044_signal']
    },
    'f22mt_gm_z_1260d_slope_v045_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_z_1260d_slope_v045_signal'].__code__.co_varnames[:globals()['f22mt_gm_z_1260d_slope_v045_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_z_1260d_slope_v045_signal']
    },
    'f22mt_ebitdam_z_63d_slope_v046_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_63d_slope_v046_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_63d_slope_v046_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_63d_slope_v046_signal']
    },
    'f22mt_ebitdam_z_126d_slope_v047_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_126d_slope_v047_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_126d_slope_v047_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_126d_slope_v047_signal']
    },
    'f22mt_ebitdam_z_252d_slope_v048_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_252d_slope_v048_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_252d_slope_v048_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_252d_slope_v048_signal']
    },
    'f22mt_ebitdam_z_504d_slope_v049_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_504d_slope_v049_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_504d_slope_v049_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_504d_slope_v049_signal']
    },
    'f22mt_ebitdam_z_756d_slope_v050_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_756d_slope_v050_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_756d_slope_v050_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_756d_slope_v050_signal']
    },
    'f22mt_ebitdam_z_1260d_slope_v051_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_z_1260d_slope_v051_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_z_1260d_slope_v051_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_z_1260d_slope_v051_signal']
    },
    'f22mt_opm_z_63d_slope_v052_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_63d_slope_v052_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_63d_slope_v052_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_63d_slope_v052_signal']
    },
    'f22mt_opm_z_126d_slope_v053_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_126d_slope_v053_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_126d_slope_v053_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_126d_slope_v053_signal']
    },
    'f22mt_opm_z_252d_slope_v054_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_252d_slope_v054_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_252d_slope_v054_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_252d_slope_v054_signal']
    },
    'f22mt_opm_z_504d_slope_v055_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_504d_slope_v055_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_504d_slope_v055_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_504d_slope_v055_signal']
    },
    'f22mt_opm_z_756d_slope_v056_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_756d_slope_v056_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_756d_slope_v056_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_756d_slope_v056_signal']
    },
    'f22mt_opm_z_1260d_slope_v057_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_z_1260d_slope_v057_signal'].__code__.co_varnames[:globals()['f22mt_opm_z_1260d_slope_v057_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_z_1260d_slope_v057_signal']
    },
    'f22mt_nm_z_63d_slope_v058_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_63d_slope_v058_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_63d_slope_v058_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_63d_slope_v058_signal']
    },
    'f22mt_nm_z_126d_slope_v059_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_126d_slope_v059_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_126d_slope_v059_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_126d_slope_v059_signal']
    },
    'f22mt_nm_z_252d_slope_v060_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_252d_slope_v060_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_252d_slope_v060_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_252d_slope_v060_signal']
    },
    'f22mt_nm_z_504d_slope_v061_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_504d_slope_v061_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_504d_slope_v061_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_504d_slope_v061_signal']
    },
    'f22mt_nm_z_756d_slope_v062_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_756d_slope_v062_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_756d_slope_v062_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_756d_slope_v062_signal']
    },
    'f22mt_nm_z_1260d_slope_v063_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_z_1260d_slope_v063_signal'].__code__.co_varnames[:globals()['f22mt_nm_z_1260d_slope_v063_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_z_1260d_slope_v063_signal']
    },
    'f22mt_gm_cv_63d_slope_v064_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_63d_slope_v064_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_63d_slope_v064_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_63d_slope_v064_signal']
    },
    'f22mt_gm_cv_126d_slope_v065_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_126d_slope_v065_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_126d_slope_v065_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_126d_slope_v065_signal']
    },
    'f22mt_gm_cv_252d_slope_v066_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_252d_slope_v066_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_252d_slope_v066_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_252d_slope_v066_signal']
    },
    'f22mt_gm_cv_504d_slope_v067_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_504d_slope_v067_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_504d_slope_v067_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_504d_slope_v067_signal']
    },
    'f22mt_gm_cv_756d_slope_v068_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_756d_slope_v068_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_756d_slope_v068_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_756d_slope_v068_signal']
    },
    'f22mt_gm_cv_1260d_slope_v069_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_cv_1260d_slope_v069_signal'].__code__.co_varnames[:globals()['f22mt_gm_cv_1260d_slope_v069_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_cv_1260d_slope_v069_signal']
    },
    'f22mt_ebitdam_cv_63d_slope_v070_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_63d_slope_v070_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_63d_slope_v070_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_63d_slope_v070_signal']
    },
    'f22mt_ebitdam_cv_126d_slope_v071_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_126d_slope_v071_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_126d_slope_v071_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_126d_slope_v071_signal']
    },
    'f22mt_ebitdam_cv_252d_slope_v072_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_252d_slope_v072_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_252d_slope_v072_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_252d_slope_v072_signal']
    },
    'f22mt_ebitdam_cv_504d_slope_v073_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_504d_slope_v073_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_504d_slope_v073_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_504d_slope_v073_signal']
    },
    'f22mt_ebitdam_cv_756d_slope_v074_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_756d_slope_v074_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_756d_slope_v074_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_756d_slope_v074_signal']
    },
    'f22mt_ebitdam_cv_1260d_slope_v075_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_cv_1260d_slope_v075_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_cv_1260d_slope_v075_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_cv_1260d_slope_v075_signal']
    },
    'f22mt_opm_cv_63d_slope_v076_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_63d_slope_v076_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_63d_slope_v076_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_63d_slope_v076_signal']
    },
    'f22mt_opm_cv_126d_slope_v077_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_126d_slope_v077_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_126d_slope_v077_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_126d_slope_v077_signal']
    },
    'f22mt_opm_cv_252d_slope_v078_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_252d_slope_v078_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_252d_slope_v078_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_252d_slope_v078_signal']
    },
    'f22mt_opm_cv_504d_slope_v079_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_504d_slope_v079_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_504d_slope_v079_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_504d_slope_v079_signal']
    },
    'f22mt_opm_cv_756d_slope_v080_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_756d_slope_v080_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_756d_slope_v080_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_756d_slope_v080_signal']
    },
    'f22mt_opm_cv_1260d_slope_v081_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_cv_1260d_slope_v081_signal'].__code__.co_varnames[:globals()['f22mt_opm_cv_1260d_slope_v081_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_cv_1260d_slope_v081_signal']
    },
    'f22mt_nm_cv_63d_slope_v082_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_63d_slope_v082_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_63d_slope_v082_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_63d_slope_v082_signal']
    },
    'f22mt_nm_cv_126d_slope_v083_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_126d_slope_v083_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_126d_slope_v083_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_126d_slope_v083_signal']
    },
    'f22mt_nm_cv_252d_slope_v084_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_252d_slope_v084_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_252d_slope_v084_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_252d_slope_v084_signal']
    },
    'f22mt_nm_cv_504d_slope_v085_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_504d_slope_v085_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_504d_slope_v085_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_504d_slope_v085_signal']
    },
    'f22mt_nm_cv_756d_slope_v086_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_756d_slope_v086_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_756d_slope_v086_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_756d_slope_v086_signal']
    },
    'f22mt_nm_cv_1260d_slope_v087_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_cv_1260d_slope_v087_signal'].__code__.co_varnames[:globals()['f22mt_nm_cv_1260d_slope_v087_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_cv_1260d_slope_v087_signal']
    },
    'f22mt_gm_rel_sma_63d_slope_v088_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_63d_slope_v088_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_63d_slope_v088_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_63d_slope_v088_signal']
    },
    'f22mt_gm_rel_sma_126d_slope_v089_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_126d_slope_v089_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_126d_slope_v089_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_126d_slope_v089_signal']
    },
    'f22mt_gm_rel_sma_252d_slope_v090_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_252d_slope_v090_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_252d_slope_v090_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_252d_slope_v090_signal']
    },
    'f22mt_gm_rel_sma_504d_slope_v091_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_504d_slope_v091_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_504d_slope_v091_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_504d_slope_v091_signal']
    },
    'f22mt_gm_rel_sma_756d_slope_v092_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_756d_slope_v092_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_756d_slope_v092_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_756d_slope_v092_signal']
    },
    'f22mt_gm_rel_sma_1260d_slope_v093_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_gm_rel_sma_1260d_slope_v093_signal'].__code__.co_varnames[:globals()['f22mt_gm_rel_sma_1260d_slope_v093_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_gm_rel_sma_1260d_slope_v093_signal']
    },
    'f22mt_ebitdam_rel_sma_63d_slope_v094_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_63d_slope_v094_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_63d_slope_v094_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_63d_slope_v094_signal']
    },
    'f22mt_ebitdam_rel_sma_126d_slope_v095_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_126d_slope_v095_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_126d_slope_v095_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_126d_slope_v095_signal']
    },
    'f22mt_ebitdam_rel_sma_252d_slope_v096_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_252d_slope_v096_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_252d_slope_v096_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_252d_slope_v096_signal']
    },
    'f22mt_ebitdam_rel_sma_504d_slope_v097_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_504d_slope_v097_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_504d_slope_v097_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_504d_slope_v097_signal']
    },
    'f22mt_ebitdam_rel_sma_756d_slope_v098_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_756d_slope_v098_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_756d_slope_v098_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_756d_slope_v098_signal']
    },
    'f22mt_ebitdam_rel_sma_1260d_slope_v099_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ebitdam_rel_sma_1260d_slope_v099_signal'].__code__.co_varnames[:globals()['f22mt_ebitdam_rel_sma_1260d_slope_v099_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ebitdam_rel_sma_1260d_slope_v099_signal']
    },
    'f22mt_opm_rel_sma_63d_slope_v100_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_63d_slope_v100_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_63d_slope_v100_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_63d_slope_v100_signal']
    },
    'f22mt_opm_rel_sma_126d_slope_v101_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_126d_slope_v101_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_126d_slope_v101_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_126d_slope_v101_signal']
    },
    'f22mt_opm_rel_sma_252d_slope_v102_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_252d_slope_v102_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_252d_slope_v102_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_252d_slope_v102_signal']
    },
    'f22mt_opm_rel_sma_504d_slope_v103_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_504d_slope_v103_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_504d_slope_v103_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_504d_slope_v103_signal']
    },
    'f22mt_opm_rel_sma_756d_slope_v104_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_756d_slope_v104_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_756d_slope_v104_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_756d_slope_v104_signal']
    },
    'f22mt_opm_rel_sma_1260d_slope_v105_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_opm_rel_sma_1260d_slope_v105_signal'].__code__.co_varnames[:globals()['f22mt_opm_rel_sma_1260d_slope_v105_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_opm_rel_sma_1260d_slope_v105_signal']
    },
    'f22mt_nm_rel_sma_63d_slope_v106_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_63d_slope_v106_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_63d_slope_v106_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_63d_slope_v106_signal']
    },
    'f22mt_nm_rel_sma_126d_slope_v107_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_126d_slope_v107_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_126d_slope_v107_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_126d_slope_v107_signal']
    },
    'f22mt_nm_rel_sma_252d_slope_v108_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_252d_slope_v108_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_252d_slope_v108_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_252d_slope_v108_signal']
    },
    'f22mt_nm_rel_sma_504d_slope_v109_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_504d_slope_v109_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_504d_slope_v109_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_504d_slope_v109_signal']
    },
    'f22mt_nm_rel_sma_756d_slope_v110_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_756d_slope_v110_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_756d_slope_v110_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_756d_slope_v110_signal']
    },
    'f22mt_nm_rel_sma_1260d_slope_v111_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nm_rel_sma_1260d_slope_v111_signal'].__code__.co_varnames[:globals()['f22mt_nm_rel_sma_1260d_slope_v111_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nm_rel_sma_1260d_slope_v111_signal']
    },
    'f22mt_egm_delta_63d_slope_v112_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_63d_slope_v112_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_63d_slope_v112_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_63d_slope_v112_signal']
    },
    'f22mt_egm_delta_126d_slope_v113_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_126d_slope_v113_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_126d_slope_v113_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_126d_slope_v113_signal']
    },
    'f22mt_egm_delta_252d_slope_v114_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_252d_slope_v114_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_252d_slope_v114_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_252d_slope_v114_signal']
    },
    'f22mt_egm_delta_504d_slope_v115_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_504d_slope_v115_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_504d_slope_v115_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_504d_slope_v115_signal']
    },
    'f22mt_egm_delta_756d_slope_v116_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_756d_slope_v116_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_756d_slope_v116_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_756d_slope_v116_signal']
    },
    'f22mt_egm_delta_1260d_slope_v117_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_delta_1260d_slope_v117_signal'].__code__.co_varnames[:globals()['f22mt_egm_delta_1260d_slope_v117_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_delta_1260d_slope_v117_signal']
    },
    'f22mt_ogm_delta_63d_slope_v118_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_63d_slope_v118_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_63d_slope_v118_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_63d_slope_v118_signal']
    },
    'f22mt_ogm_delta_126d_slope_v119_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_126d_slope_v119_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_126d_slope_v119_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_126d_slope_v119_signal']
    },
    'f22mt_ogm_delta_252d_slope_v120_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_252d_slope_v120_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_252d_slope_v120_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_252d_slope_v120_signal']
    },
    'f22mt_ogm_delta_504d_slope_v121_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_504d_slope_v121_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_504d_slope_v121_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_504d_slope_v121_signal']
    },
    'f22mt_ogm_delta_756d_slope_v122_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_756d_slope_v122_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_756d_slope_v122_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_756d_slope_v122_signal']
    },
    'f22mt_ogm_delta_1260d_slope_v123_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_delta_1260d_slope_v123_signal'].__code__.co_varnames[:globals()['f22mt_ogm_delta_1260d_slope_v123_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_delta_1260d_slope_v123_signal']
    },
    'f22mt_ngm_delta_63d_slope_v124_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_63d_slope_v124_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_63d_slope_v124_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_63d_slope_v124_signal']
    },
    'f22mt_ngm_delta_126d_slope_v125_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_126d_slope_v125_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_126d_slope_v125_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_126d_slope_v125_signal']
    },
    'f22mt_ngm_delta_252d_slope_v126_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_252d_slope_v126_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_252d_slope_v126_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_252d_slope_v126_signal']
    },
    'f22mt_ngm_delta_504d_slope_v127_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_504d_slope_v127_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_504d_slope_v127_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_504d_slope_v127_signal']
    },
    'f22mt_ngm_delta_756d_slope_v128_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_756d_slope_v128_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_756d_slope_v128_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_756d_slope_v128_signal']
    },
    'f22mt_ngm_delta_1260d_slope_v129_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ngm_delta_1260d_slope_v129_signal'].__code__.co_varnames[:globals()['f22mt_ngm_delta_1260d_slope_v129_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ngm_delta_1260d_slope_v129_signal']
    },
    'f22mt_nem_delta_63d_slope_v130_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_63d_slope_v130_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_63d_slope_v130_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_63d_slope_v130_signal']
    },
    'f22mt_nem_delta_126d_slope_v131_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_126d_slope_v131_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_126d_slope_v131_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_126d_slope_v131_signal']
    },
    'f22mt_nem_delta_252d_slope_v132_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_252d_slope_v132_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_252d_slope_v132_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_252d_slope_v132_signal']
    },
    'f22mt_nem_delta_504d_slope_v133_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_504d_slope_v133_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_504d_slope_v133_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_504d_slope_v133_signal']
    },
    'f22mt_nem_delta_756d_slope_v134_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_756d_slope_v134_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_756d_slope_v134_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_756d_slope_v134_signal']
    },
    'f22mt_nem_delta_1260d_slope_v135_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nem_delta_1260d_slope_v135_signal'].__code__.co_varnames[:globals()['f22mt_nem_delta_1260d_slope_v135_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nem_delta_1260d_slope_v135_signal']
    },
    'f22mt_nom_delta_63d_slope_v136_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_63d_slope_v136_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_63d_slope_v136_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_63d_slope_v136_signal']
    },
    'f22mt_nom_delta_126d_slope_v137_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_126d_slope_v137_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_126d_slope_v137_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_126d_slope_v137_signal']
    },
    'f22mt_nom_delta_252d_slope_v138_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_252d_slope_v138_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_252d_slope_v138_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_252d_slope_v138_signal']
    },
    'f22mt_nom_delta_504d_slope_v139_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_504d_slope_v139_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_504d_slope_v139_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_504d_slope_v139_signal']
    },
    'f22mt_nom_delta_756d_slope_v140_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_756d_slope_v140_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_756d_slope_v140_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_756d_slope_v140_signal']
    },
    'f22mt_nom_delta_1260d_slope_v141_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_nom_delta_1260d_slope_v141_signal'].__code__.co_varnames[:globals()['f22mt_nom_delta_1260d_slope_v141_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_nom_delta_1260d_slope_v141_signal']
    },
    'f22mt_egm_z_63d_slope_v142_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_63d_slope_v142_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_63d_slope_v142_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_63d_slope_v142_signal']
    },
    'f22mt_egm_z_126d_slope_v143_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_126d_slope_v143_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_126d_slope_v143_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_126d_slope_v143_signal']
    },
    'f22mt_egm_z_252d_slope_v144_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_252d_slope_v144_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_252d_slope_v144_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_252d_slope_v144_signal']
    },
    'f22mt_egm_z_504d_slope_v145_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_504d_slope_v145_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_504d_slope_v145_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_504d_slope_v145_signal']
    },
    'f22mt_egm_z_756d_slope_v146_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_756d_slope_v146_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_756d_slope_v146_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_756d_slope_v146_signal']
    },
    'f22mt_egm_z_1260d_slope_v147_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_egm_z_1260d_slope_v147_signal'].__code__.co_varnames[:globals()['f22mt_egm_z_1260d_slope_v147_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_egm_z_1260d_slope_v147_signal']
    },
    'f22mt_ogm_z_63d_slope_v148_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_z_63d_slope_v148_signal'].__code__.co_varnames[:globals()['f22mt_ogm_z_63d_slope_v148_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_z_63d_slope_v148_signal']
    },
    'f22mt_ogm_z_126d_slope_v149_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_z_126d_slope_v149_signal'].__code__.co_varnames[:globals()['f22mt_ogm_z_126d_slope_v149_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_z_126d_slope_v149_signal']
    },
    'f22mt_ogm_z_252d_slope_v150_signal': {
        'inputs': (inputs := [v for v in globals()['f22mt_ogm_z_252d_slope_v150_signal'].__code__.co_varnames[:globals()['f22mt_ogm_z_252d_slope_v150_signal'].__code__.co_argcount]]),
        'func': globals()['f22mt_ogm_z_252d_slope_v150_signal']
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
    for n, c in f22mt_SLOPE_001_150_REGISTRY.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        q = r.iloc[1260:]
        if len(q.dropna()) > 0:
            assert q.nunique() > 2, f"{n} failed nunique: {q.nunique()}"
            assert q.std() > 0, f"{n} failed std: {q.std()}"
    print("OK")
