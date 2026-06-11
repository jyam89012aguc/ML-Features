# f05_moving_average_envelope_jerk_001_150_gemini.py
import pandas as pd
import numpy as np

def _sma(s, w):
    return s.rolling(w, min_periods=min(w, 5)).mean()

def _ema(s, w):
    return s.ewm(span=w, min_periods=min(w, 5), adjust=False).mean()

def _wma(s, w):
    weights = np.arange(1, w + 1)
    return s.rolling(w, min_periods=min(w, 5)).apply(lambda x: np.dot(x, weights[-len(x):]) / weights[-len(x):].sum(), raw=True)

def _envelope_pos(price, ma, pct):
    upper = ma * (1 + pct)
    lower = ma * (1 - pct)
    return (price - lower) / (upper - lower).replace(0, np.nan)

def _envelope_dist(price, ma, pct, is_upper=True):
    bound = ma * (1 + pct) if is_upper else ma * (1 - pct)
    return (price - bound) / bound.abs().replace(0, np.nan)

def _envelope_width(ma, pct):
    return (2 * ma * pct) / ma.abs().replace(0, np.nan)

# Jerk Features 001-150: ROC of Slope Envelope Features

def f05mae_f05_moving_average_envelope_sma_5d_1pct_pos_jerk_v001_signal(close: pd.Series) -> pd.Series:
    """Jerk of price position in 1% SMA 5d envelope (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_pos(close, ma, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_5pct_pos_jerk_v002_signal(close: pd.Series) -> pd.Series:
    """Jerk of price position in 5% SMA 5d envelope (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_pos(close, ma, 0.05)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_2pct_pos_jerk_v003_signal(close: pd.Series) -> pd.Series:
    """Jerk of price position in 2% SMA 21d envelope (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_pos(close, ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_5pct_pos_jerk_v004_signal(close: pd.Series) -> pd.Series:
    """Jerk of price position in 5% SMA 21d envelope (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_pos(close, ma, 0.05)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_3pct_pos_jerk_v005_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of price position in 3% SMA 63d envelope (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.03)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_10pct_pos_jerk_v006_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of price position in 10% SMA 63d envelope (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.10)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_3pct_pos_jerk_v007_signal(close: pd.Series) -> pd.Series:
    """Jerk of price position in 3% EMA 21d envelope (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_pos(close, ma, 0.03)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_5pct_pos_jerk_v008_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of price position in 5% EMA 63d envelope (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_2pct_pos_jerk_v009_signal(close: pd.Series) -> pd.Series:
    """Jerk of price position in 2% WMA 21d envelope (5d ROC of 5d ROC)."""
    ma = _wma(close, 21)
    base = _envelope_pos(close, ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_5pct_pos_jerk_v010_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of price position in 5% WMA 63d envelope (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_10pct_pos_jerk_v011_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of price position in 10% SMA 252d envelope (63d ROC of 63d ROC)."""
    ma = _sma(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.10)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_10pct_pos_jerk_v012_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of price position in 10% EMA 252d envelope (63d ROC of 63d ROC)."""
    ma = _ema(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.10)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_2pct_width_jerk_v013_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% SMA 5d envelope width (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_width(ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_5pct_width_jerk_v014_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5% EMA 21d envelope width (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_3pct_width_jerk_v015_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 3% WMA 63d envelope width (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 63)
    base = _envelope_width(ma, 0.03)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_3pct_dist_upper_jerk_v016_signal(close: pd.Series) -> pd.Series:
    """Jerk of dist to upper 3% SMA 21d envelope (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_dist(close, ma, 0.03, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_3pct_dist_lower_jerk_v017_signal(close: pd.Series) -> pd.Series:
    """Jerk of dist to lower 3% SMA 21d envelope (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_dist(close, ma, 0.03, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_5pct_dist_upper_jerk_v018_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of dist to upper 5% EMA 63d envelope (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    base = _envelope_dist(closeadj, ma, 0.05, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_5pct_dist_lower_jerk_v019_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of dist to lower 5% EMA 63d envelope (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    base = _envelope_dist(closeadj, ma, 0.05, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_in_21d_5pct_pos_jerk_v020_signal(close: pd.Series) -> pd.Series:
    """Jerk of position of 5d SMA in 21d 5% SMA envelope (5d ROC of 5d ROC)."""
    ma5 = _sma(close, 5)
    ma21 = _sma(close, 21)
    base = _envelope_pos(ma5, ma21, 0.05)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

# Pattern-based generation to reach 150 jerk functions

def f05mae_f05_moving_average_envelope_sma_126d_5pct_pos_jerk_v021_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 126d position (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_5pct_pos_jerk_v022_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% EMA 126d position (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_5pct_pos_jerk_v023_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% WMA 126d position (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_10pct_pos_jerk_v024_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% SMA 5d position (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_pos(close, ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_10pct_pos_jerk_v025_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% EMA 5d position (5d ROC of 5d ROC)."""
    ma = _ema(close, 5)
    base = _envelope_pos(close, ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_10pct_pos_jerk_v026_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% WMA 5d position (5d ROC of 5d ROC)."""
    ma = _wma(close, 5)
    base = _envelope_pos(close, ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_10pct_pos_jerk_v027_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% SMA 21d position (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_pos(close, ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_10pct_pos_jerk_v028_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% EMA 21d position (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_pos(close, ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_10pct_pos_jerk_v029_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% WMA 21d position (5d ROC of 5d ROC)."""
    ma = _wma(close, 21)
    base = _envelope_pos(close, ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_5pct_pos_jerk_v030_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 63d position (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)



def f05mae_f05_moving_average_envelope_sma_126d_10pct_pos_jerk_v033_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% SMA 126d position (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.10)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_10pct_pos_jerk_v034_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% EMA 126d position (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.10)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_10pct_pos_jerk_v035_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% WMA 126d position (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.10)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_5pct_pos_jerk_v036_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 252d position (63d ROC of 63d ROC)."""
    ma = _sma(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_5pct_pos_jerk_v037_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% EMA 252d position (63d ROC of 63d ROC)."""
    ma = _ema(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_5pct_pos_jerk_v038_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% WMA 252d position (63d ROC of 63d ROC)."""
    ma = _wma(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.05)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_1pct_dist_upper_jerk_v039_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% SMA 5d dist upper (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_dist(close, ma, 0.01, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_1pct_dist_upper_jerk_v040_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% EMA 5d dist upper (5d ROC of 5d ROC)."""
    ma = _ema(close, 5)
    base = _envelope_dist(close, ma, 0.01, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_1pct_dist_upper_jerk_v041_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% WMA 5d dist upper (5d ROC of 5d ROC)."""
    ma = _wma(close, 5)
    base = _envelope_dist(close, ma, 0.01, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_2pct_dist_upper_jerk_v042_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% SMA 21d dist upper (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_dist(close, ma, 0.02, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_2pct_dist_upper_jerk_v043_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% EMA 21d dist upper (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_dist(close, ma, 0.02, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_2pct_dist_upper_jerk_v044_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% WMA 21d dist upper (5d ROC of 5d ROC)."""
    ma = _wma(close, 21)
    base = _envelope_dist(close, ma, 0.02, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_5pct_dist_upper_jerk_v045_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 63d dist upper (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_dist(closeadj, ma, 0.05, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f05mae_f05_moving_average_envelope_wma_63d_5pct_dist_upper_jerk_v047_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% WMA 63d dist upper (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 63)
    base = _envelope_dist(closeadj, ma, 0.05, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_1pct_dist_upper_jerk_v048_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% SMA 126d dist upper (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 126)
    base = _envelope_dist(closeadj, ma, 0.01, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_1pct_dist_upper_jerk_v049_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% EMA 126d dist upper (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 126)
    base = _envelope_dist(closeadj, ma, 0.01, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_1pct_dist_upper_jerk_v050_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% WMA 126d dist upper (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 126)
    base = _envelope_dist(closeadj, ma, 0.01, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_3pct_dist_upper_jerk_v051_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 3% SMA 252d dist upper (63d ROC of 63d ROC)."""
    ma = _sma(closeadj, 252)
    base = _envelope_dist(closeadj, ma, 0.03, True)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_3pct_dist_upper_jerk_v052_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 3% EMA 252d dist upper (63d ROC of 63d ROC)."""
    ma = _ema(closeadj, 252)
    base = _envelope_dist(closeadj, ma, 0.03, True)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_3pct_dist_upper_jerk_v053_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 3% WMA 252d dist upper (63d ROC of 63d ROC)."""
    ma = _wma(closeadj, 252)
    base = _envelope_dist(closeadj, ma, 0.03, True)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_2pct_dist_lower_jerk_v054_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% SMA 5d dist lower (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_dist(close, ma, 0.02, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_2pct_dist_lower_jerk_v055_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% EMA 5d dist lower (5d ROC of 5d ROC)."""
    ma = _ema(close, 5)
    base = _envelope_dist(close, ma, 0.02, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_2pct_dist_lower_jerk_v056_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% WMA 5d dist lower (5d ROC of 5d ROC)."""
    ma = _wma(close, 5)
    base = _envelope_dist(close, ma, 0.02, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_5pct_dist_lower_jerk_v057_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 21d dist lower (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_dist(close, ma, 0.05, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_5pct_dist_lower_jerk_v058_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5% EMA 21d dist lower (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_dist(close, ma, 0.05, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_5pct_dist_lower_jerk_v059_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5% WMA 21d dist lower (5d ROC of 5d ROC)."""
    ma = _wma(close, 21)
    base = _envelope_dist(close, ma, 0.05, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_10pct_dist_lower_jerk_v060_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% SMA 63d dist lower (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_dist(closeadj, ma, 0.10, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_10pct_dist_lower_jerk_v061_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% EMA 63d dist lower (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    base = _envelope_dist(closeadj, ma, 0.10, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_10pct_dist_lower_jerk_v062_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% WMA 63d dist lower (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 63)
    base = _envelope_dist(closeadj, ma, 0.10, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_2pct_dist_lower_jerk_v063_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% SMA 126d dist lower (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 126)
    base = _envelope_dist(closeadj, ma, 0.02, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_2pct_dist_lower_jerk_v064_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% EMA 126d dist lower (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 126)
    base = _envelope_dist(closeadj, ma, 0.02, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_2pct_dist_lower_jerk_v065_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% WMA 126d dist lower (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 126)
    base = _envelope_dist(closeadj, ma, 0.02, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_5pct_dist_lower_jerk_v066_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 252d dist lower (63d ROC of 63d ROC)."""
    ma = _sma(closeadj, 252)
    base = _envelope_dist(closeadj, ma, 0.05, False)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_5pct_dist_lower_jerk_v067_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% EMA 252d dist lower (63d ROC of 63d ROC)."""
    ma = _ema(closeadj, 252)
    base = _envelope_dist(closeadj, ma, 0.05, False)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_5pct_dist_lower_jerk_v068_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% WMA 252d dist lower (63d ROC of 63d ROC)."""
    ma = _wma(closeadj, 252)
    base = _envelope_dist(closeadj, ma, 0.05, False)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_5pct_width_jerk_v069_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 5d width (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_5pct_width_jerk_v070_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5% EMA 5d width (5d ROC of 5d ROC)."""
    ma = _ema(close, 5)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_5pct_width_jerk_v071_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5% WMA 5d width (5d ROC of 5d ROC)."""
    ma = _wma(close, 5)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_10pct_width_jerk_v072_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% SMA 21d width (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_width(ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_10pct_width_jerk_v073_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% EMA 21d width (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_width(ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_10pct_width_jerk_v074_signal(close: pd.Series) -> pd.Series:
    """Jerk of 10% WMA 21d width (5d ROC of 5d ROC)."""
    ma = _wma(close, 21)
    base = _envelope_width(ma, 0.10)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_3pct_width_jerk_v075_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 3% SMA 63d width (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_width(ma, 0.03)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_3pct_width_jerk_v076_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 3% EMA 63d width (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    base = _envelope_width(ma, 0.03)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f05mae_f05_moving_average_envelope_sma_126d_5pct_width_jerk_v078_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 126d width (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 126)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_5pct_width_jerk_v079_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% EMA 126d width (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 126)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_5pct_width_jerk_v080_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% WMA 126d width (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 126)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_10pct_width_jerk_v081_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% SMA 252d width (63d ROC of 63d ROC)."""
    ma = _sma(closeadj, 252)
    base = _envelope_width(ma, 0.10)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_10pct_width_jerk_v082_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% EMA 252d width (63d ROC of 63d ROC)."""
    ma = _ema(closeadj, 252)
    base = _envelope_width(ma, 0.10)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_10pct_width_jerk_v083_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% WMA 252d width (63d ROC of 63d ROC)."""
    ma = _wma(closeadj, 252)
    base = _envelope_width(ma, 0.10)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_sqz_21d_5pct_jerk_v084_signal(close: pd.Series) -> pd.Series:
    """Jerk of SMA 21d 5% width squeeze (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    w = _envelope_width(ma, 0.05)
    base = w / _sma(w, 21).replace(0, np.nan)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_sqz_63d_10pct_jerk_v085_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of EMA 63d 10% width squeeze (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    w = _envelope_width(ma, 0.10)
    base = w / _sma(w, 63).replace(0, np.nan)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_in_21d_1pct_pos_jerk_v086_signal(close: pd.Series) -> pd.Series:
    """Jerk of position of 5d SMA in 21d 1% SMA envelope (5d ROC of 5d ROC)."""
    ma5 = _sma(close, 5)
    ma21 = _sma(close, 21)
    base = _envelope_pos(ma5, ma21, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_in_21d_1pct_pos_jerk_v087_signal(close: pd.Series) -> pd.Series:
    """Jerk of position of 5d EMA in 21d 1% EMA envelope (5d ROC of 5d ROC)."""
    ma5 = _ema(close, 5)
    ma21 = _ema(close, 21)
    base = _envelope_pos(ma5, ma21, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_in_21d_1pct_pos_jerk_v088_signal(close: pd.Series) -> pd.Series:
    """Jerk of position of 5d WMA in 21d 1% WMA envelope (5d ROC of 5d ROC)."""
    ma5 = _wma(close, 5)
    ma21 = _wma(close, 21)
    base = _envelope_pos(ma5, ma21, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_in_63d_2pct_pos_jerk_v089_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of position of 21d SMA in 63d 2% SMA envelope (21d ROC of 21d ROC)."""
    ma21 = _sma(closeadj, 21)
    ma63 = _sma(closeadj, 63)
    base = _envelope_pos(ma21, ma63, 0.02)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_in_63d_2pct_pos_jerk_v090_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of position of 21d EMA in 63d 2% EMA envelope (21d ROC of 21d ROC)."""
    ma21 = _ema(closeadj, 21)
    ma63 = _ema(closeadj, 63)
    base = _envelope_pos(ma21, ma63, 0.02)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_in_63d_2pct_pos_jerk_v091_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of position of 21d WMA in 63d 2% WMA envelope (21d ROC of 21d ROC)."""
    ma21 = _wma(closeadj, 21)
    ma63 = _wma(closeadj, 63)
    base = _envelope_pos(ma21, ma63, 0.02)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_in_252d_5pct_pos_jerk_v092_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of position of 63d SMA in 252d 5% SMA envelope (63d ROC of 63d ROC)."""
    ma63 = _sma(closeadj, 63)
    ma252 = _sma(closeadj, 252)
    base = _envelope_pos(ma63, ma252, 0.05)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_in_252d_5pct_pos_jerk_v093_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of position of 63d EMA in 252d 5% EMA envelope (63d ROC of 63d ROC)."""
    ma63 = _ema(closeadj, 63)
    ma252 = _ema(closeadj, 252)
    base = _envelope_pos(ma63, ma252, 0.05)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_in_252d_5pct_pos_jerk_v094_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of position of 63d WMA in 252d 5% WMA envelope (63d ROC of 63d ROC)."""
    ma63 = _wma(closeadj, 63)
    ma252 = _wma(closeadj, 252)
    base = _envelope_pos(ma63, ma252, 0.05)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_dist_upper_21d_1pct_jerk_v095_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5d SMA dist upper 21d 1% SMA (5d ROC of 5d ROC)."""
    ma5 = _sma(close, 5)
    ma21 = _sma(close, 21)
    base = _envelope_dist(ma5, ma21, 0.01, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_dist_upper_21d_1pct_jerk_v096_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5d EMA dist upper 21d 1% EMA (5d ROC of 5d ROC)."""
    ma5 = _ema(close, 5)
    ma21 = _ema(close, 21)
    base = _envelope_dist(ma5, ma21, 0.01, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_dist_upper_21d_1pct_jerk_v097_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5d WMA dist upper 21d 1% WMA (5d ROC of 5d ROC)."""
    ma5 = _wma(close, 5)
    ma21 = _wma(close, 21)
    base = _envelope_dist(ma5, ma21, 0.01, True)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_dist_upper_63d_2pct_jerk_v098_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 21d SMA dist upper 63d 2% SMA (21d ROC of 21d ROC)."""
    ma21 = _sma(closeadj, 21)
    ma63 = _sma(closeadj, 63)
    base = _envelope_dist(ma21, ma63, 0.02, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_dist_upper_63d_2pct_jerk_v099_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 21d EMA dist upper 63d 2% EMA (21d ROC of 21d ROC)."""
    ma21 = _ema(closeadj, 21)
    ma63 = _ema(closeadj, 63)
    base = _envelope_dist(ma21, ma63, 0.02, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_dist_upper_63d_2pct_jerk_v100_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 21d WMA dist upper 63d 2% WMA (21d ROC of 21d ROC)."""
    ma21 = _wma(closeadj, 21)
    ma63 = _wma(closeadj, 63)
    base = _envelope_dist(ma21, ma63, 0.02, True)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_dist_lower_21d_1pct_jerk_v101_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5d SMA dist lower 21d 1% SMA (5d ROC of 5d ROC)."""
    ma5 = _sma(close, 5)
    ma21 = _sma(close, 21)
    base = _envelope_dist(ma5, ma21, 0.01, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_dist_lower_21d_1pct_jerk_v102_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5d EMA dist lower 21d 1% EMA (5d ROC of 5d ROC)."""
    ma5 = _ema(close, 5)
    ma21 = _ema(close, 21)
    base = _envelope_dist(ma5, ma21, 0.01, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_dist_lower_21d_1pct_jerk_v103_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5d WMA dist lower 21d 1% WMA (5d ROC of 5d ROC)."""
    ma5 = _wma(close, 5)
    ma21 = _wma(close, 21)
    base = _envelope_dist(ma5, ma21, 0.01, False)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_dist_lower_63d_2pct_jerk_v104_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 21d SMA dist lower 63d 2% SMA (21d ROC of 21d ROC)."""
    ma21 = _sma(closeadj, 21)
    ma63 = _sma(closeadj, 63)
    base = _envelope_dist(ma21, ma63, 0.02, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_dist_lower_63d_2pct_jerk_v105_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 21d EMA dist lower 63d 2% EMA (21d ROC of 21d ROC)."""
    ma21 = _ema(closeadj, 21)
    ma63 = _ema(closeadj, 63)
    base = _envelope_dist(ma21, ma63, 0.02, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_dist_lower_63d_2pct_jerk_v106_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 21d WMA dist lower 63d 2% WMA (21d ROC of 21d ROC)."""
    ma21 = _wma(closeadj, 21)
    ma63 = _wma(closeadj, 63)
    base = _envelope_dist(ma21, ma63, 0.02, False)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)


def f05mae_f05_moving_average_envelope_sma_5d_2pct_pos_jerk_v108_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% SMA 5d position (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_pos(close, ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_3pct_pos_jerk_v109_signal(close: pd.Series) -> pd.Series:
    """Jerk of 3% SMA 5d position (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_pos(close, ma, 0.03)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_1pct_pos_jerk_v110_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% SMA 21d position (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_pos(close, ma, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_3pct_pos_jerk_v111_signal(close: pd.Series) -> pd.Series:
    """Jerk of 3% SMA 21d position (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_pos(close, ma, 0.03)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_1pct_pos_jerk_v112_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% SMA 63d position (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_2pct_pos_jerk_v113_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% SMA 63d position (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.02)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_1pct_pos_jerk_v114_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% SMA 126d position (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_126d_3pct_pos_jerk_v115_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 3% SMA 126d position (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.03)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_1pct_pos_jerk_v116_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% SMA 252d position (63d ROC of 63d ROC)."""
    ma = _sma(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_252d_2pct_pos_jerk_v117_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% SMA 252d position (63d ROC of 63d ROC)."""
    ma = _sma(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.02)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_1pct_pos_jerk_v118_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% EMA 5d position (5d ROC of 5d ROC)."""
    ma = _ema(close, 5)
    base = _envelope_pos(close, ma, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_2pct_pos_jerk_v119_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% EMA 5d position (5d ROC of 5d ROC)."""
    ma = _ema(close, 5)
    base = _envelope_pos(close, ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_3pct_pos_jerk_v120_signal(close: pd.Series) -> pd.Series:
    """Jerk of 3% EMA 5d position (5d ROC of 5d ROC)."""
    ma = _ema(close, 5)
    base = _envelope_pos(close, ma, 0.03)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_1pct_pos_jerk_v121_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% EMA 21d position (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_pos(close, ma, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_2pct_pos_jerk_v122_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% EMA 21d position (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_pos(close, ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_1pct_pos_jerk_v123_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% EMA 63d position (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_63d_2pct_pos_jerk_v124_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% EMA 63d position (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.02)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_1pct_pos_jerk_v125_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% EMA 126d position (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_2pct_pos_jerk_v126_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% EMA 126d position (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.02)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_1pct_pos_jerk_v127_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% EMA 252d position (63d ROC of 63d ROC)."""
    ma = _ema(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_252d_2pct_pos_jerk_v128_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% EMA 252d position (63d ROC of 63d ROC)."""
    ma = _ema(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.02)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_1pct_pos_jerk_v129_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% WMA 5d position (5d ROC of 5d ROC)."""
    ma = _wma(close, 5)
    base = _envelope_pos(close, ma, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_2pct_pos_jerk_v130_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% WMA 5d position (5d ROC of 5d ROC)."""
    ma = _wma(close, 5)
    base = _envelope_pos(close, ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_1pct_pos_jerk_v131_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% WMA 21d position (5d ROC of 5d ROC)."""
    ma = _wma(close, 21)
    base = _envelope_pos(close, ma, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)


def f05mae_f05_moving_average_envelope_wma_63d_1pct_pos_jerk_v133_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% WMA 63d position (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_63d_2pct_pos_jerk_v134_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% WMA 63d position (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 63)
    base = _envelope_pos(closeadj, ma, 0.02)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_1pct_pos_jerk_v135_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% WMA 126d position (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_126d_2pct_pos_jerk_v136_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% WMA 126d position (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 126)
    base = _envelope_pos(closeadj, ma, 0.02)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_1pct_pos_jerk_v137_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 1% WMA 252d position (63d ROC of 63d ROC)."""
    ma = _wma(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.01)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_252d_2pct_pos_jerk_v138_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 2% WMA 252d position (63d ROC of 63d ROC)."""
    ma = _wma(closeadj, 252)
    base = _envelope_pos(closeadj, ma, 0.02)
    slope = base.pct_change(63)
    res = slope.pct_change(63)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_5d_1pct_width_jerk_v139_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% SMA 5d width (5d ROC of 5d ROC)."""
    ma = _sma(close, 5)
    base = _envelope_width(ma, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_21d_2pct_width_jerk_v140_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% SMA 21d width (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    base = _envelope_width(ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_sma_63d_5pct_width_jerk_v141_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 5% SMA 63d width (21d ROC of 21d ROC)."""
    ma = _sma(closeadj, 63)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_5d_1pct_width_jerk_v142_signal(close: pd.Series) -> pd.Series:
    """Jerk of 1% EMA 5d width (5d ROC of 5d ROC)."""
    ma = _ema(close, 5)
    base = _envelope_width(ma, 0.01)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_21d_3pct_width_jerk_v143_signal(close: pd.Series) -> pd.Series:
    """Jerk of 3% EMA 21d width (5d ROC of 5d ROC)."""
    ma = _ema(close, 21)
    base = _envelope_width(ma, 0.03)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_126d_10pct_width_jerk_v144_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of 10% EMA 126d width (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 126)
    base = _envelope_width(ma, 0.10)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_5d_2pct_width_jerk_v145_signal(close: pd.Series) -> pd.Series:
    """Jerk of 2% WMA 5d width (5d ROC of 5d ROC)."""
    ma = _wma(close, 5)
    base = _envelope_width(ma, 0.02)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_21d_5pct_width_jerk_v146_signal(close: pd.Series) -> pd.Series:
    """Jerk of 5% WMA 21d width (5d ROC of 5d ROC)."""
    ma = _wma(close, 21)
    base = _envelope_width(ma, 0.05)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)


def f05mae_f05_moving_average_envelope_sma_sqz_21d_2pct_jerk_v148_signal(close: pd.Series) -> pd.Series:
    """Jerk of SMA 21d 2% width squeeze (5d ROC of 5d ROC)."""
    ma = _sma(close, 21)
    w = _envelope_width(ma, 0.02)
    base = w / _sma(w, 21).replace(0, np.nan)
    slope = base.pct_change(5)
    res = slope.pct_change(5)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_ema_sqz_63d_5pct_jerk_v149_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of EMA 63d 5% width squeeze (21d ROC of 21d ROC)."""
    ma = _ema(closeadj, 63)
    w = _envelope_width(ma, 0.05)
    base = w / _sma(w, 63).replace(0, np.nan)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

def f05mae_f05_moving_average_envelope_wma_sqz_126d_10pct_jerk_v150_signal(closeadj: pd.Series) -> pd.Series:
    """Jerk of WMA 126d 10% width squeeze (21d ROC of 21d ROC)."""
    ma = _wma(closeadj, 126)
    w = _envelope_width(ma, 0.10)
    base = w / _sma(w, 126).replace(0, np.nan)
    slope = base.pct_change(21)
    res = slope.pct_change(21)
    return res.replace([np.inf, -np.inf], np.nan)

SILVERDB_ACCESS, SOURCE_TABLE, ENTITY_COLUMN, DATE_COLUMN = "read_only", "sep", "ticker", "date"
ORDER_BY, NO_FORWARD_LOOKING = [ENTITY_COLUMN, DATE_COLUMN], True
SOURCE_COLUMNS = {c: f"sep.{c}" for c in ["close", "closeadj"]}

JERK_NAMES = [f for f in globals() if f.startswith("f05mae_") and f.endswith("_signal")]

F05_MOVING_AVERAGE_ENVELOPE_JERK_REGISTRY_001_150 = {
    n: {
        "inputs": (inputs := [v for v in globals()[n].__code__.co_varnames[:globals()[n].__code__.co_argcount]]),
        "source_table": SOURCE_TABLE,
        "source_columns": {c: SOURCE_COLUMNS[c] for c in inputs if c in SOURCE_COLUMNS},
        "entity_column": ENTITY_COLUMN, "date_column": DATE_COLUMN,
        "order_by": ORDER_BY, "no_forward_looking": NO_FORWARD_LOOKING, "func": globals()[n]
    } for n in sorted(JERK_NAMES)
}

if __name__ == "__main__":
    sz = 500
    d = pd.DataFrame({
        "close": np.random.randn(sz).cumsum() + 100,
        "closeadj": np.random.randn(sz).cumsum() + 100,
        "ticker": ["T"] * sz,
        "date": pd.date_range("2020-01-01", periods=sz)
    })
    for n, c in F05_MOVING_AVERAGE_ENVELOPE_JERK_REGISTRY_001_150.items():
        r = c["func"](**{i: d[i] for i in c["inputs"]})
        assert isinstance(r, pd.Series)
    print("jerk 001-150 OK")
