import pandas as pd
import numpy as np

def _vol_realized(c, w): return c.pct_change().rolling(w, min_periods=min(w, 5)).std()
def _vol_parkinson(h, l, w): return np.sqrt((np.log(h / l.replace(0, np.nan))**2).rolling(w, min_periods=min(w, 5)).mean() / (4 * np.log(2)))

def f10_volatility_regime_vol_realized_w5_v001(arg_close: pd.Series) -> pd.Series:
    res = _vol_realized(arg_close, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w10_v002(arg_close: pd.Series) -> pd.Series:
    res = _vol_realized(arg_close, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w21_v003(arg_close: pd.Series) -> pd.Series:
    res = _vol_realized(arg_close, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w42_v004(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 42)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w63_v005(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 63)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w84_v006(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 84)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w105_v007(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 105)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w126_v008(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 126)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w150_v009(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 150)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w180_v010(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 180)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w200_v011(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 200)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w220_v012(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 220)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w240_v013(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 240)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w252_v014(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 252)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_w300_v015(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 300)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w5_v016(arg_high: pd.Series, arg_low: pd.Series) -> pd.Series:
    res = _vol_parkinson(arg_high, arg_low, 5)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w10_v017(arg_high: pd.Series, arg_low: pd.Series) -> pd.Series:
    res = _vol_parkinson(arg_high, arg_low, 10)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w21_v018(arg_high: pd.Series, arg_low: pd.Series) -> pd.Series:
    res = _vol_parkinson(arg_high, arg_low, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w42_v019(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w63_v020(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w84_v021(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 84))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w105_v022(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 105))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w126_v023(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 126))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w150_v024(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 150))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w180_v025(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 180))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w200_v026(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 200))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w220_v027(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 220))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w240_v028(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 240))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w252_v029(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 252))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_w300_v030(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 300))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w5_w21_v031(arg_close: pd.Series) -> pd.Series:
    res = _vol_realized(arg_close, 5) / _vol_realized(arg_close, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w5_w21_v041(arg_high: pd.Series, arg_low: pd.Series) -> pd.Series:
    res = _vol_parkinson(arg_high, arg_low, 5) / _vol_parkinson(arg_high, arg_low, 21).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w5_w63_v032(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 5) / _vol_realized(arg_closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w5_w63_v042(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 5) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w10_w42_v033(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 10) / _vol_realized(arg_closeadj, 42).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w10_w42_v043(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w10_w126_v034(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 10) / _vol_realized(arg_closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w10_w126_v044(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w21_w63_v035(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21) / _vol_realized(arg_closeadj, 63).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w21_w63_v045(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w21_w126_v036(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21) / _vol_realized(arg_closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w21_w126_v046(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w21_w252_v037(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21) / _vol_realized(arg_closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w21_w252_v047(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w42_w126_v038(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 42) / _vol_realized(arg_closeadj, 126).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w42_w126_v048(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 126).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w42_w252_v039(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 42) / _vol_realized(arg_closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w42_w252_v049(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_realized_ratio_w63_w252_v040(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 63) / _vol_realized(arg_closeadj, 252).replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_parkinson_ratio_w63_w252_v050(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 252).replace(0, np.nan))
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w5_w21_v051(arg_close: pd.Series) -> pd.Series:
    res = _vol_realized(arg_close, 5).rolling(21, min_periods=min(21, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w5_w21_v061(arg_high: pd.Series, arg_low: pd.Series) -> pd.Series:
    res = _vol_parkinson(arg_high, arg_low, 5).rolling(21, min_periods=min(21, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w5_w63_v052(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 5).rolling(63, min_periods=min(63, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w5_w63_v062(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 5).rolling(63, min_periods=min(63, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w10_w42_v053(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 10).rolling(42, min_periods=min(42, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w10_w42_v063(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10).rolling(42, min_periods=min(42, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w10_w126_v054(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 10).rolling(126, min_periods=min(126, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w10_w126_v064(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 10).rolling(126, min_periods=min(126, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w21_w63_v055(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(63, min_periods=min(63, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w21_w63_v065(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(63, min_periods=min(63, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w21_w126_v056(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(126, min_periods=min(126, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w21_w126_v066(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(126, min_periods=min(126, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w21_w252_v057(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 21).rolling(252, min_periods=min(252, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w21_w252_v067(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 21).rolling(252, min_periods=min(252, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w42_w126_v058(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 42).rolling(126, min_periods=min(126, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w42_w126_v068(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42).rolling(126, min_periods=min(126, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w42_w252_v059(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 42).rolling(252, min_periods=min(252, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w42_w252_v069(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 42).rolling(252, min_periods=min(252, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_realized_w63_w252_v060(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = _vol_realized(arg_closeadj, 63).rolling(252, min_periods=min(252, 5)).std()
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_of_vol_parkinson_w63_w252_v070(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 63).rolling(252, min_periods=min(252, 5)).std())
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w5_w21_v071(arg_close: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_close, 5) - _vol_realized(arg_close, 5).rolling(21, min_periods=min(21, 5)).mean()) / _vol_realized(arg_close, 5).rolling(21, min_periods=min(21, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w5_w21_v081(arg_high: pd.Series, arg_low: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high, arg_low, 5) - _vol_parkinson(arg_high, arg_low, 5).rolling(21, min_periods=min(21, 5)).mean()) / _vol_parkinson(arg_high, arg_low, 5).rolling(21, min_periods=min(21, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w5_w63_v072(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 5) - _vol_realized(arg_closeadj, 5).rolling(63, min_periods=min(63, 5)).mean()) / _vol_realized(arg_closeadj, 5).rolling(63, min_periods=min(63, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_parkinson_w5_w63_v082(arg_high: pd.Series, arg_low: pd.Series, arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 5) - _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 5).rolling(63, min_periods=min(63, 5)).mean()) / _vol_parkinson(arg_high * (arg_closeadj / arg_close.replace(0, np.nan)), arg_low * (arg_closeadj / arg_close.replace(0, np.nan)), 5).rolling(63, min_periods=min(63, 5)).std().replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)

def f10_volatility_regime_vol_zscore_realized_w10_w42_v073(arg_close: pd.Series, arg_closeadj: pd.Series) -> pd.Series:
    res = (_vol_realized(arg_closeadj, 10) - _vol_realized(arg_closeadj, 10).rolling(42, min_periods=min(42, 5)).mean()) / _vol_realized(arg_closeadj, 10).rolling(42, min_periods=min(42, 5)).std().replace(0, np.nan)
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
