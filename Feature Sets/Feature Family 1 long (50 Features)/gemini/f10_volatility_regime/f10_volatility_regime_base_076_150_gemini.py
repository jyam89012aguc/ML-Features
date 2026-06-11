import pandas as pd
import numpy as np

def _vol_realized(c, w): return c.pct_change().rolling(w, min_periods=min(w, 5)).std()
def _vol_parkinson(h, l, w): return np.sqrt((np.log(h / l.replace(0, np.nan))**2).rolling(w, min_periods=min(w, 5)).mean() / (4 * np.log(2)))

def f10_volatility_regime_vol_zscore_parkinson_w10_w42_v083(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10).rolling(42, min_periods=min(42, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10).rolling(42, min_periods=min(42, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w10_w126_v074(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 10) - _vol_realized(arg_closeadj, 10).rolling(126, min_periods=min(126, 5)).mean()) / _vol_realized(arg_closeadj, 10).rolling(126, min_periods=min(126, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w10_w126_v084(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10).rolling(126, min_periods=min(126, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10).rolling(126, min_periods=min(126, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w21_w63_v075(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 21) - _vol_realized(arg_closeadj, 21).rolling(63, min_periods=min(63, 5)).mean()) / _vol_realized(arg_closeadj, 21).rolling(63, min_periods=min(63, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w21_w63_v085(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(63, min_periods=min(63, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(63, min_periods=min(63, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w21_w126_v076(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 21) - _vol_realized(arg_closeadj, 21).rolling(126, min_periods=min(126, 5)).mean()) / _vol_realized(arg_closeadj, 21).rolling(126, min_periods=min(126, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w21_w126_v086(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(126, min_periods=min(126, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(126, min_periods=min(126, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w21_w252_v077(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 21) - _vol_realized(arg_closeadj, 21).rolling(252, min_periods=min(252, 5)).mean()) / _vol_realized(arg_closeadj, 21).rolling(252, min_periods=min(252, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w21_w252_v087(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(252, min_periods=min(252, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(252, min_periods=min(252, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w42_w126_v078(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 42) - _vol_realized(arg_closeadj, 42).rolling(126, min_periods=min(126, 5)).mean()) / _vol_realized(arg_closeadj, 42).rolling(126, min_periods=min(126, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w42_w126_v088(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42).rolling(126, min_periods=min(126, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42).rolling(126, min_periods=min(126, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w42_w252_v079(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 42) - _vol_realized(arg_closeadj, 42).rolling(252, min_periods=min(252, 5)).mean()) / _vol_realized(arg_closeadj, 42).rolling(252, min_periods=min(252, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w42_w252_v089(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42).rolling(252, min_periods=min(252, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42).rolling(252, min_periods=min(252, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w63_w252_v080(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 63) - _vol_realized(arg_closeadj, 63).rolling(252, min_periods=min(252, 5)).mean()) / _vol_realized(arg_closeadj, 63).rolling(252, min_periods=min(252, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w63_w252_v090(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63).rolling(252, min_periods=min(252, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63).rolling(252, min_periods=min(252, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w5_v091(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series) -> pd.Series:
    res = (pd.concat([arg_high - arg_low, (arg_high - arg_close.shift(1)).abs(), (arg_low - arg_close.shift(1)).abs()], axis=1).max(axis=1).rolling(5, min_periods=min(5, 5)).mean() / arg_close.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w10_v092(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series) -> pd.Series:
    res = (pd.concat([arg_high - arg_low, (arg_high - arg_close.shift(1)).abs(), (arg_low - arg_close.shift(1)).abs()], axis=1).max(axis=1).rolling(10, min_periods=min(10, 5)).mean() / arg_close.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w21_v093(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series) -> pd.Series:
    res = (pd.concat([arg_high - arg_low, (arg_high - arg_close.shift(1)).abs(), (arg_low - arg_close.shift(1)).abs()], axis=1).max(axis=1).rolling(21, min_periods=min(21, 5)).mean() / arg_close.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w42_v094(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(42, min_periods=min(42, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w63_v095(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(63, min_periods=min(63, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w84_v096(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(84, min_periods=min(84, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w105_v097(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(105, min_periods=min(105, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w126_v098(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(126, min_periods=min(126, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w150_v099(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(150, min_periods=min(150, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w180_v100(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(180, min_periods=min(180, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w200_v101(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(200, min_periods=min(200, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w220_v102(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(220, min_periods=min(220, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w240_v103(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(240, min_periods=min(240, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w252_v104(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(252, min_periods=min(252, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_atr_norm_w300_v105(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (pd.concat([(arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - (arg_low * (arg_closeadj / arg_close.replace(0, np.nan))), ((arg_high * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs(), ((arg_low * (arg_closeadj / arg_close.replace(0, np.nan))) - arg_closeadj.shift(1)).abs()], axis=1).max(axis=1).rolling(300, min_periods=min(300, 5)).mean() / arg_closeadj.replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w5_v106(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series) -> pd.Series:
    res = _vol_parkinson(arg_high, arg_low, 5) / _vol_realized(arg_close, 5).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w10_v107(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series) -> pd.Series:
    res = _vol_parkinson(arg_high, arg_low, 10) / _vol_realized(arg_close, 10).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w21_v108(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series) -> pd.Series:
    res = _vol_parkinson(arg_high, arg_low, 21) / _vol_realized(arg_close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w42_v109(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42) / _vol_realized(arg_closeadj, 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w63_v110(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63) / _vol_realized(arg_closeadj, 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w84_v111(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 84) / _vol_realized(arg_closeadj, 84).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w105_v112(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 105) / _vol_realized(arg_closeadj, 105).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w126_v113(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 126) / _vol_realized(arg_closeadj, 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w150_v114(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 150) / _vol_realized(arg_closeadj, 150).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w180_v115(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 180) / _vol_realized(arg_closeadj, 180).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w200_v116(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 200) / _vol_realized(arg_closeadj, 200).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w220_v117(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 220) / _vol_realized(arg_closeadj, 220).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w240_v118(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 240) / _vol_realized(arg_closeadj, 240).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w252_v119(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 252) / _vol_realized(arg_closeadj, 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_efficiency_w300_v120(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 300) / _vol_realized(arg_closeadj, 300).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w21_v121(arg_close: pd.Series) -> pd.Series:
    res = ((arg_close.pct_change().abs() > 2.0 * _vol_realized(arg_close, 21)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w42_v122(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 42).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w63_v123(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 63).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w84_v124(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 84).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w105_v125(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 105).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w126_v126(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 126).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w150_v127(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 150).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w180_v128(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 180).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w200_v129(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 200).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w220_v130(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 220).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w240_v131(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 240).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w252_v132(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 252).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w300_v133(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 300).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w400_v134(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 400).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_spike_count_w21_w500_v135(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = ((arg_closeadj.pct_change().abs() > 2.0 * _vol_realized(arg_closeadj, 500).shift(1)).rolling(21, min_periods=1).sum())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w21_v136(arg_close: pd.Series) -> pd.Series:
    res = _vol_realized(arg_close, 21).rolling(21, min_periods=min(21, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w42_v137(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(42, min_periods=min(42, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w63_v138(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(63, min_periods=min(63, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w84_v139(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(84, min_periods=min(84, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w105_v140(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(105, min_periods=min(105, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w126_v141(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(126, min_periods=min(126, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w150_v142(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(150, min_periods=min(150, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w180_v143(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(180, min_periods=min(180, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w200_v144(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(200, min_periods=min(200, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w220_v145(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(220, min_periods=min(220, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w240_v146(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(240, min_periods=min(240, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w252_v147(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(252, min_periods=min(252, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w300_v148(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(300, min_periods=min(300, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w400_v149(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(400, min_periods=min(400, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_max_w21_w500_v150(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(500, min_periods=min(500, 5)).max()
    return res.replace([np.inf, -np.inf], np.nan)


SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["open", "high", "low", "close", "closeadj"]}

BASE_NAMES = [f for f in globals() if f.startswith("f10_volatility_regime_") and f.endswith("_signal") or f.startswith("f10_volatility_regime_")]

F10_VOLATILITY_REGIME_BASE_REGISTRY = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(BASE_NAMES) if callable(globals().get(n))
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1000
    np.random.seed(42)
    d = pd.DataFrame({
        "arg_open": (o := np.random.randn(sz).cumsum() + 100),
        "arg_high": o + np.abs(np.random.rand(sz)),
        "arg_low": o - np.abs(np.random.rand(sz)),
        "arg_close": o + np.random.randn(sz) * 0.1,
        "arg_closeadj": (o + np.random.randn(sz) * 0.1) * 1.1,
        "ticker": ["T"]*sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F10_VOLATILITY_REGIME_BASE_REGISTRY.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert len(r) > 0, f"{n} failed len"
        assert r.nunique() > 2, f"{n} failed nunique: {r.nunique()}"
        assert r.std() > 0, f"{n} failed std: {r.std()}"
    print(f"BASE OK")
