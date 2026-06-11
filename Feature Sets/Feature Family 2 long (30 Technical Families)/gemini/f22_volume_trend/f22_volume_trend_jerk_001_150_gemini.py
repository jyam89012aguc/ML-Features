# f22_volume_trend_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _vol_ma_trend(v, w_fast, w_slow):
    """Calculates the relative difference between a fast and slow volume moving average."""
    return (v.rolling(w_fast).mean() - v.rolling(w_slow).mean()) / v.rolling(w_slow).mean().replace(0, np.nan)

def _vol_roc(v, w):
    """Calculates the rate of change of volume over a specified window."""
    return (v - v.shift(w)) / v.shift(w).abs().replace(0, np.nan)

def _vol_force(v, c, w):
    """Calculates the Force Index: volume multiplied by the change in price, smoothed over a window."""
    force = v * (c - c.shift(1))
    return force.rolling(w).mean()

def _sma(s, w): 
    """Simple Moving Average helper."""
    return s.rolling(w, min_periods=min(w, 5)).mean()

# JERK FEATURES 001-150
# Jerk is defined as the rate of change of the slope: (Base).pct_change(w).diff(w)

def f22vt_f22_volume_trend_ma_trend_5_21_jerk_v001_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 5/21 volume MA trend. 
    Identifies second-order acceleration changes in short-term volume flows.
    """
    base = _vol_ma_trend(volume, 5, 21)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_10_42_jerk_v002_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 10/42 volume MA trend.
    Helps detect momentum shifts in medium-term participation acceleration.
    """
    base = _vol_ma_trend(volume, 10, 42)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_21_63_jerk_v003_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 21/63 volume MA trend.
    Analyzes second-order changes in institutional quarterly volume accumulation.
    """
    base = _vol_ma_trend(volume, 21, 63)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_5_jerk_v004_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 5-day volume ROC.
    Sensitive to rapid inflection points in short-term volume momentum.
    """
    base = _vol_roc(volume, 5)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_21_jerk_v005_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 21-day volume ROC.
    Identifies sudden changes in monthly volume growth acceleration.
    """
    base = _vol_roc(volume, 21)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_5_jerk_v006_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 5-day Force Index.
    Measures the second-order rate of conviction shifts in short-term price-volume trends.
    """
    base = _vol_force(volume, close, 5)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_21_jerk_v007_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 21-day Force Index.
    Evaluates shifts in the acceleration of medium-term conviction pressure.
    """
    base = _vol_force(volume, close, 21)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_63_jerk_v008_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 63-day Force Index using adjusted data.
    Analyzes turning points in quarterly conviction momentum.
    """
    base = _vol_force(volume, closeadj, 63)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_5_63_jerk_v009_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 5/63 volume MA trend.
    Monitors inflection in tactical participation relative to quarterly flows.
    """
    base = _vol_ma_trend(volume, 5, 63)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_63_jerk_v010_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 63-day volume ROC.
    Detects structural shifts in the acceleration of cyclical participation.
    """
    base = _vol_roc(volume, 63)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_126_jerk_v011_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 126-day Force Index.
    Measures second-order conviction changes over semi-annual horizons.
    """
    base = _vol_force(volume, closeadj, 126)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_21_126_jerk_v012_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 21/126 volume MA trend.
    Identifies momentum acceleration shifts in monthly vs semi-annual flows.
    """
    base = _vol_ma_trend(volume, 21, 126)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_126_jerk_v013_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 126-day volume ROC.
    Analyzes the second derivative of institutional interest over semi-annual periods.
    """
    base = _vol_roc(volume, 126)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_252_jerk_v014_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 252-day Force Index.
    Evaluates acceleration shifts in long-term structural conviction.
    """
    base = _vol_force(volume, closeadj, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_63_252_jerk_v015_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 63/252 volume MA trend.
    Monitors inflection points in quarterly vs annual volume regimes.
    """
    base = _vol_ma_trend(volume, 63, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_252_jerk_v016_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 252-day volume ROC.
    Detects the second-order rate of change in secular volume growth.
    """
    base = _vol_roc(volume, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_126_504_jerk_v017_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 126/504 volume MA trend.
    Analyzes long-term structural transitions in the volume hierarchy.
    """
    base = _vol_ma_trend(volume, 126, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_2_10_jerk_v018_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 2/10 volume MA trend.
    Extremely sensitive to short-term participation shocks and reversals.
    """
    base = _vol_ma_trend(volume, 2, 10)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_1_jerk_v019_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 1-day volume ROC.
    Targets very high-frequency acceleration shifts in daily volume.
    """
    base = _vol_roc(volume, 1)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_3_jerk_v020_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 3-day Force Index.
    Identifies rapid conviction inflection points over very short windows.
    """
    base = _vol_force(volume, close, 3)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_5_42_jerk_v021_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 5/42 volume MA trend.
    Monitors tactical acceleration relative to bi-monthly participation baselines.
    """
    base = _vol_ma_trend(volume, 5, 42)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_10_jerk_v022_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 10-day volume ROC.
    Focuses on acceleration changes in bi-weekly volume cycles.
    """
    base = _vol_roc(volume, 10)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_10_jerk_v023_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 10-day Force Index.
    Analyzes second-order momentum of bi-weekly conviction accumulation.
    """
    base = _vol_force(volume, close, 10)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_21_42_jerk_v024_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 21/42 volume MA trend.
    Identifies turning points in monthly vs bi-monthly participation acceleration.
    """
    base = _vol_ma_trend(volume, 21, 42)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_42_jerk_v025_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 42-day volume ROC.
    Monitors acceleration shifts in bi-monthly institutional cycles.
    """
    base = _vol_roc(volume, 42)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_42_jerk_v026_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 42-day Force Index.
    Targets second-order conviction shifts over quarterly investment horizons.
    """
    base = _vol_force(volume, closeadj, 42)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_10_126_jerk_v027_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 10/126 volume MA trend.
    Monitors bi-weekly flows relative to semi-annual participation.
    """
    base = _vol_ma_trend(volume, 10, 126)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_force_50_jerk_v029_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 50-day Force Index.
    Identifies second-order momentum shifts in long-term 'smart money' conviction.
    """
    base = _vol_force(volume, closeadj, 50)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_5_126_jerk_v030_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 5/126 volume MA trend.
    Analyzes acceleration changes of tactical participation within broad flows.
    """
    base = _vol_ma_trend(volume, 5, 126)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_force_15_jerk_v032_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 15-day Force Index.
    Second-order conviction timing for medium-term tactical entries.
    """
    base = _vol_force(volume, close, 15)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_3_15_jerk_v033_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 3/15 volume MA trend.
    Designed to find very short-term momentum acceleration shifts.
    """
    base = _vol_ma_trend(volume, 3, 15)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_15_jerk_v034_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 15-day volume ROC.
    Captures the acceleration of participation expansion over three weeks.
    """
    base = _vol_roc(volume, 15)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_ma_trend_21_252_jerk_v036_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 21/252 volume MA trend.
    Second-order analysis of long-term asset adoption cycles.
    """
    base = _vol_ma_trend(volume, 21, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_10_21_jerk_v039_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 10/21 volume MA trend.
    Monitors inflection in bi-weekly volume flows relative to monthly mean.
    """
    base = _vol_ma_trend(volume, 10, 21)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_42_126_jerk_v042_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 42/126 volume MA trend.
    Analyzes the acceleration of quarterly participation shifts.
    """
    base = _vol_ma_trend(volume, 42, 126)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_force_100_jerk_v044_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 100-day Force Index.
    Secular conviction momentum acceleration analysis over 21-day periods.
    """
    base = _vol_force(volume, closeadj, 100)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_5_10_jerk_v045_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 5/10 volume MA trend.
    Extremely reactive feature for catching participation shocks in weekly flows.
    """
    base = _vol_ma_trend(volume, 5, 10)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_63_126_jerk_v048_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 63/126 volume MA trend.
    Tracks acceleration changes in major quarterly cycles relative to semi-annual flows.
    """
    base = _vol_ma_trend(volume, 63, 126)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_ma_trend_10_63_jerk_v054_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 10/63 volume trend.
    Monitors inflection of quarterly liquidity growth using bi-weekly inputs.
    """
    base = _vol_ma_trend(volume, 10, 63)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_ma_trend_5_252_jerk_v060_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 5/252 volume trend.
    Identifies tactical acceleration inflection relative to the secular volume baseline.
    """
    base = _vol_ma_trend(volume, 5, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_10_252_jerk_v063_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 10/252 volume trend.
    Analyzes acceleration changes in bi-weekly flows relative to secular trends.
    """
    base = _vol_ma_trend(volume, 10, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_ma_trend_42_252_jerk_v069_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 42/252 volume trend.
    Analyzes acceleration changes in bi-monthly flows relative to secular baselines.
    """
    base = _vol_ma_trend(volume, 42, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_ma_trend_126_252_jerk_v075_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 126/252 volume trend.
    Analyzes semi-annual vs annual volume flow acceleration.
    """
    base = _vol_ma_trend(volume, 126, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_5_504_jerk_v078_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 5/504 volume trend.
    Analyzes tactical participation shifts relative to two-year structural baselines.
    """
    base = _vol_ma_trend(volume, 5, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_10_504_jerk_v081_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 10/504 volume trend.
    Analyzes acceleration changes in bi-weekly flows relative to structural baselines.
    """
    base = _vol_ma_trend(volume, 10, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_21_504_jerk_v084_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 21/504 volume trend.
    Analyzes acceleration changes in monthly flows relative to two-year structural cycles.
    """
    base = _vol_ma_trend(volume, 21, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_42_504_jerk_v087_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 42/504 volume trend.
    Monitors structural transitions in bi-monthly flows relative to two-year cycles.
    """
    base = _vol_ma_trend(volume, 42, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_63_504_jerk_v090_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 63/504 volume trend.
    Analyzes acceleration changes in quarterly institutional flows relative to secular baselines.
    """
    base = _vol_ma_trend(volume, 63, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)






def f22vt_f22_volume_trend_ma_trend_252_504_jerk_v096_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 252/504 volume trend.
    Analyzes acceleration changes in annual flows relative to structural two-year cycles.
    """
    base = _vol_ma_trend(volume, 252, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_1_5_jerk_v099_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 1/5 volume MA trend.
    Identifies extremely high-frequency acceleration shifts in tactical volume flows.
    """
    base = _vol_ma_trend(volume, 1, 5)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_force_1_jerk_v101_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 1-day force index.
    Captures rapid second-order shifts in conviction pressure at a daily frequency.
    """
    base = _vol_force(volume, close, 1)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_1_21_jerk_v102_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 1/21 volume MA trend.
    Monitors inflection in daily participation relative to the monthly mean.
    """
    base = _vol_ma_trend(volume, 1, 21)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_1_63_jerk_v105_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 1/63 volume MA trend.
    Analyzes daily participation shifts relative to quarterly institutional flows.
    """
    base = _vol_ma_trend(volume, 1, 63)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_force_1_v3_jerk_v107_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 1-day force index using adjusted data.
    Monitors monthly conviction acceleration cycles at a daily resolution.
    """
    base = _vol_force(volume, closeadj, 1)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_1_126_jerk_v108_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 1/126 volume MA trend.
    Analyzes daily flows relative to institutional semi-annual baselines.
    """
    base = _vol_ma_trend(volume, 1, 126)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_1_252_jerk_v111_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 1/252 volume MA trend.
    Analyzes daily shifts relative to structural annual volume regimes.
    """
    base = _vol_ma_trend(volume, 1, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f22vt_f22_volume_trend_ma_trend_1_504_jerk_v114_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 1/504 volume trend.
    Analyzes daily flows relative to structural two-year cycles.
    """
    base = _vol_ma_trend(volume, 1, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_force_1_v6_jerk_v116_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 1-day force index.
    Monitors long-term acceleration changes in structural conviction pressure.
    """
    base = _vol_force(volume, closeadj, 1)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_100_200_jerk_v117_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 100/200 volume trend.
    Analyzes structural shifts in semi-annual vs annual institutional flows.
    """
    base = _vol_ma_trend(volume, 100, 200)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_200_jerk_v118_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 200-day volume ROC.
    Monitors acceleration shifts in long-term annual institutional interest.
    """
    base = _vol_roc(volume, 200)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_200_jerk_v119_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 200-day force index.
    Targets second-order conviction shifts over annual investment horizons.
    """
    base = _vol_force(volume, closeadj, 200)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_200_504_jerk_v120_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 200/504 volume trend.
    Analyzes acceleration shifts in annual flows relative to structural multi-year cycles.
    """
    base = _vol_ma_trend(volume, 200, 504)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_500_jerk_v121_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 500-day volume ROC.
    Analyzes structural transitions in secular volume growth acceleration.
    """
    base = _vol_roc(volume, 500)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_500_jerk_v122_signal(volume: pd.Series, closeadj: pd.Series) -> pd.Series:
    """Calculates the 63-day jerk of the 500-day force index.
    Targets second-order conviction shifts over secular accumulation cycles.
    """
    base = _vol_force(volume, closeadj, 500)
    res = base.pct_change(63).diff(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_2_5_v2_jerk_v123_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 2/5 volume trend.
    Refined short-term participation acceleration measurement.
    """
    base = _vol_ma_trend(volume, 2, 5)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_2_jerk_v124_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 2-day volume ROC.
    Targets extremely short-term acceleration shifts in volume momentum.
    """
    base = _vol_roc(volume, 2)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_force_2_jerk_v125_signal(volume: pd.Series, close: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 2-day force index.
    Identifies rapid conviction inflection points over very short periods.
    """
    base = _vol_force(volume, close, 2)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_ma_trend_3_10_v2_jerk_v126_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 3/10 volume trend.
    Monitors tactical acceleration relative to bi-weekly participation means.
    """
    base = _vol_ma_trend(volume, 3, 10)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_3_jerk_v127_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 5-day jerk of the 3-day volume ROC.
    Targets short-term acceleration shifts in multi-day volume growth.
    """
    base = _vol_roc(volume, 3)
    res = base.pct_change(5).diff(5)
    return res.replace([np.inf, -np.inf], np.nan)




















def f22vt_f22_volume_trend_ma_trend_50_100_jerk_v147_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 50/100 volume trend.
    Identifies second-order momentum shifts in long-term participation flows.
    """
    base = _vol_ma_trend(volume, 50, 100)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f22vt_f22_volume_trend_roc_50_jerk_v148_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 50-day volume ROC.
    Monitors acceleration shifts in multi-month institutional participation growth.
    """
    base = _vol_roc(volume, 50)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f22vt_f22_volume_trend_ma_trend_100_252_jerk_v150_signal(volume: pd.Series) -> pd.Series:
    """Calculates the 21-day jerk of the 100/252 volume trend.
    Analyzes structural shifts in the acceleration of institutional semi-annual interest.
    """
    base = _vol_ma_trend(volume, 100, 252)
    res = base.pct_change(21).diff(21)
    return res.replace([np.inf, -np.inf], np.nan)

# REGISTRY AND METADATA
SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj", "volume"]}

JERK_NAMES = [f for f in globals() if f.startswith("f22vt_") and f.endswith("_signal")]

F22_VOLUME_TREND_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == "__main__":
    import pandas as pd; import numpy as np
    sz = 1000; d = pd.DataFrame({"close": np.random.randn(sz).cumsum()+100, "closeadj": np.random.randn(sz).cumsum()+100, "volume": np.random.rand(sz)*1000000, "ticker": ["T"]*sz, "date": pd.date_range("2020-01-01", periods=sz)})
    for n, c in F22_VOLUME_TREND_JERK_REGISTRY_001_150.items():
        kwargs = {i: d[i] for i in c["inputs"] if i in d.columns}
        r = c["func"](**kwargs)
        assert isinstance(r, pd.Series)
    print("jerk 001-150 OK")
