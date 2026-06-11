import inspect
import numpy as np
import pandas as pd


def _safe_div(num, den):
    return num / den.abs().replace(0, np.nan)


def _z(x, w):
    m = x.rolling(w, min_periods=2).mean()
    s = x.rolling(w, min_periods=2).std()
    return _safe_div(x - m, s)


def _spread(short, long):
    return _safe_div(short - long, long)


def _m(x, w):
    return x.rolling(w, min_periods=2).mean()


def _s(x, w):
    return x.rolling(w, min_periods=2).std()


def _mn(x, w):
    return x.rolling(w, min_periods=2).min()


def _mx(x, w):
    return x.rolling(w, min_periods=2).max()


def _roc(x, w):
    return _safe_div(x.diff(w), x.abs())


def _f23_cash_flow_trajectory_primitive(closeadj, volume, w):
    ret = closeadj.pct_change(max(1, min(w, 21)))
    liq = _m(closeadj * volume, w)
    return _z(ret, max(5, min(w, 63))) + _z(liq, w)


# 5d cash_flow_trajectory level zscore slope
def f23cft_f23_cash_flow_trajectory_zlevel_5d_slope_v001_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _z(x, 5)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory level to mean slope
def f23cft_f23_cash_flow_trajectory_mean_ratio_10d_slope_v002_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x, _m(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory short minus long slope
def f23cft_f23_cash_flow_trajectory_ma_spread_21d_slope_v003_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _spread(_m(x, 5), _m(x, 42))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory ranked pressure slope
def f23cft_f23_cash_flow_trajectory_rank_pressure_63d_slope_v004_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x - _mn(x, 63), _mx(x, 63) - _mn(x, 63)) + _z(x, 21) / np.sqrt(63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory trend strength slope
def f23cft_f23_cash_flow_trajectory_trend_force_126d_slope_v005_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x.diff(21), _s(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory downside gap slope
def f23cft_f23_cash_flow_trajectory_down_tail_252d_slope_v006_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x.rolling(252, min_periods=2).quantile(0.20) - x, _s(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory upside gap slope
def f23cft_f23_cash_flow_trajectory_up_tail_504d_slope_v007_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x - x.rolling(504, min_periods=2).quantile(0.80), _s(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory range position slope
def f23cft_f23_cash_flow_trajectory_range_pos_5d_slope_v008_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory mean reversion slope
def f23cft_f23_cash_flow_trajectory_revert_gap_10d_slope_v009_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(_m(x, 5) - x, _s(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory expanding pressure slope
def f23cft_f23_cash_flow_trajectory_std_expand_21d_slope_v010_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(_s(x, 5), _s(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory compression ratio slope
def f23cft_f23_cash_flow_trajectory_std_compress_63d_slope_v011_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(_s(x, 63), _s(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory breakout ratio slope
def f23cft_f23_cash_flow_trajectory_breakout_126d_slope_v012_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x, _mx(x, 126).shift(1))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory drawdown distance slope
def f23cft_f23_cash_flow_trajectory_drawdown_252d_slope_v013_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x - _mx(x, 252), _mx(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory recovery distance slope
def f23cft_f23_cash_flow_trajectory_recovery_504d_slope_v014_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x - _mn(x, 504), _mn(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory persistence share slope
def f23cft_f23_cash_flow_trajectory_persist_share_5d_slope_v015_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(_m(x.diff(3), 5), _m(x.diff(3).abs(), 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory shock frequency slope
def f23cft_f23_cash_flow_trajectory_shock_freq_10d_slope_v016_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _m(_z(x.diff(5), 10).abs(), 10)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory tail pressure slope
def f23cft_f23_cash_flow_trajectory_tail_skew_21d_slope_v017_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x.rolling(21, min_periods=2).skew(), _s(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory median distance slope
def f23cft_f23_cash_flow_trajectory_median_gap_63d_slope_v018_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x - x.rolling(63, min_periods=2).median(), _s(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory vol scaled level slope
def f23cft_f23_cash_flow_trajectory_vol_scaled_126d_slope_v019_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x, _s(x.diff(21), 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory liquidity weight slope
def f23cft_f23_cash_flow_trajectory_abs_rank_weight_252d_slope_v020_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = x * x.abs().rolling(252, min_periods=2).rank(pct=True)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory dollar weight slope
def f23cft_f23_cash_flow_trajectory_abs_mean_weight_504d_slope_v021_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _z(x * _m(x.abs(), 21), 504)
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory stability score slope
def f23cft_f23_cash_flow_trajectory_stability_5d_slope_v022_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(_m(x, 5), _m(x.diff(3).abs(), 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory decay balance slope
def f23cft_f23_cash_flow_trajectory_ewm_balance_10d_slope_v023_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=10, adjust=False).mean())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory accumulation ratio slope
def f23cft_f23_cash_flow_trajectory_positive_share_21d_slope_v024_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div((x - _m(x, 21)).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory capitulation ratio slope
def f23cft_f23_cash_flow_trajectory_negative_share_63d_slope_v025_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div((_m(x, 63) - x).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory level zscore slope
def f23cft_f23_cash_flow_trajectory_zlevel_126d_slope_v026_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _z(x, 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory level to mean slope
def f23cft_f23_cash_flow_trajectory_mean_ratio_252d_slope_v027_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x, _m(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory short minus long slope
def f23cft_f23_cash_flow_trajectory_ma_spread_504d_slope_v028_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _spread(_m(x, 21), _m(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory ranked pressure slope
def f23cft_f23_cash_flow_trajectory_rank_pressure_5d_slope_v029_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5)) + _z(x, 3) / np.sqrt(5)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory trend strength slope
def f23cft_f23_cash_flow_trajectory_trend_force_10d_slope_v030_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x.diff(5), _s(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory downside gap slope
def f23cft_f23_cash_flow_trajectory_down_tail_21d_slope_v031_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x.rolling(21, min_periods=2).quantile(0.20) - x, _s(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory upside gap slope
def f23cft_f23_cash_flow_trajectory_up_tail_63d_slope_v032_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x - x.rolling(63, min_periods=2).quantile(0.80), _s(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory range position slope
def f23cft_f23_cash_flow_trajectory_range_pos_126d_slope_v033_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory mean reversion slope
def f23cft_f23_cash_flow_trajectory_revert_gap_252d_slope_v034_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(_m(x, 21) - x, _s(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory expanding pressure slope
def f23cft_f23_cash_flow_trajectory_std_expand_504d_slope_v035_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(_s(x, 21), _s(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory compression ratio slope
def f23cft_f23_cash_flow_trajectory_std_compress_5d_slope_v036_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(_s(x, 5), _s(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory breakout ratio slope
def f23cft_f23_cash_flow_trajectory_breakout_10d_slope_v037_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x, _mx(x, 10).shift(1))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory drawdown distance slope
def f23cft_f23_cash_flow_trajectory_drawdown_21d_slope_v038_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x - _mx(x, 21), _mx(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory recovery distance slope
def f23cft_f23_cash_flow_trajectory_recovery_63d_slope_v039_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x - _mn(x, 63), _mn(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory persistence share slope
def f23cft_f23_cash_flow_trajectory_persist_share_126d_slope_v040_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(_m(x.diff(21), 126), _m(x.diff(21).abs(), 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory shock frequency slope
def f23cft_f23_cash_flow_trajectory_shock_freq_252d_slope_v041_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _m(_z(x.diff(21), 252).abs(), 252)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory tail pressure slope
def f23cft_f23_cash_flow_trajectory_tail_skew_504d_slope_v042_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x.rolling(504, min_periods=2).skew(), _s(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory median distance slope
def f23cft_f23_cash_flow_trajectory_median_gap_5d_slope_v043_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x - x.rolling(5, min_periods=2).median(), _s(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory vol scaled level slope
def f23cft_f23_cash_flow_trajectory_vol_scaled_10d_slope_v044_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x, _s(x.diff(5), 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory liquidity weight slope
def f23cft_f23_cash_flow_trajectory_abs_rank_weight_21d_slope_v045_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = x * x.abs().rolling(21, min_periods=2).rank(pct=True)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory dollar weight slope
def f23cft_f23_cash_flow_trajectory_abs_mean_weight_63d_slope_v046_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _z(x * _m(x.abs(), 21), 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory stability score slope
def f23cft_f23_cash_flow_trajectory_stability_126d_slope_v047_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(_m(x, 126), _m(x.diff(21).abs(), 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory decay balance slope
def f23cft_f23_cash_flow_trajectory_ewm_balance_252d_slope_v048_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=252, adjust=False).mean())
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory accumulation ratio slope
def f23cft_f23_cash_flow_trajectory_positive_share_504d_slope_v049_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div((x - _m(x, 504)).clip(lower=0).rolling(504, min_periods=2).sum(), (x - _m(x, 504)).abs().rolling(504, min_periods=2).sum())
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory capitulation ratio slope
def f23cft_f23_cash_flow_trajectory_negative_share_5d_slope_v050_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div((_m(x, 5) - x).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory level zscore slope
def f23cft_f23_cash_flow_trajectory_zlevel_10d_slope_v051_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _z(x, 10)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory level to mean slope
def f23cft_f23_cash_flow_trajectory_mean_ratio_21d_slope_v052_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x, _m(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory short minus long slope
def f23cft_f23_cash_flow_trajectory_ma_spread_63d_slope_v053_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _spread(_m(x, 21), _m(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory ranked pressure slope
def f23cft_f23_cash_flow_trajectory_rank_pressure_126d_slope_v054_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126)) + _z(x, 21) / np.sqrt(126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory trend strength slope
def f23cft_f23_cash_flow_trajectory_trend_force_252d_slope_v055_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x.diff(21), _s(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory downside gap slope
def f23cft_f23_cash_flow_trajectory_down_tail_504d_slope_v056_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x.rolling(504, min_periods=2).quantile(0.20) - x, _s(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory upside gap slope
def f23cft_f23_cash_flow_trajectory_up_tail_5d_slope_v057_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x - x.rolling(5, min_periods=2).quantile(0.80), _s(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory range position slope
def f23cft_f23_cash_flow_trajectory_range_pos_10d_slope_v058_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory mean reversion slope
def f23cft_f23_cash_flow_trajectory_revert_gap_21d_slope_v059_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(_m(x, 5) - x, _s(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory expanding pressure slope
def f23cft_f23_cash_flow_trajectory_std_expand_63d_slope_v060_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(_s(x, 21), _s(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory compression ratio slope
def f23cft_f23_cash_flow_trajectory_std_compress_126d_slope_v061_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(_s(x, 126), _s(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory breakout ratio slope
def f23cft_f23_cash_flow_trajectory_breakout_252d_slope_v062_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x, _mx(x, 252).shift(1))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory drawdown distance slope
def f23cft_f23_cash_flow_trajectory_drawdown_504d_slope_v063_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x - _mx(x, 504), _mx(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory recovery distance slope
def f23cft_f23_cash_flow_trajectory_recovery_5d_slope_v064_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x - _mn(x, 5), _mn(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory persistence share slope
def f23cft_f23_cash_flow_trajectory_persist_share_10d_slope_v065_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(_m(x.diff(5), 10), _m(x.diff(5).abs(), 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory shock frequency slope
def f23cft_f23_cash_flow_trajectory_shock_freq_21d_slope_v066_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _m(_z(x.diff(5), 21).abs(), 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory tail pressure slope
def f23cft_f23_cash_flow_trajectory_tail_skew_63d_slope_v067_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x.rolling(63, min_periods=2).skew(), _s(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory median distance slope
def f23cft_f23_cash_flow_trajectory_median_gap_126d_slope_v068_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x - x.rolling(126, min_periods=2).median(), _s(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory vol scaled level slope
def f23cft_f23_cash_flow_trajectory_vol_scaled_252d_slope_v069_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x, _s(x.diff(21), 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory liquidity weight slope
def f23cft_f23_cash_flow_trajectory_abs_rank_weight_504d_slope_v070_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = x * x.abs().rolling(504, min_periods=2).rank(pct=True)
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory dollar weight slope
def f23cft_f23_cash_flow_trajectory_abs_mean_weight_5d_slope_v071_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _z(x * _m(x.abs(), 3), 5)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory stability score slope
def f23cft_f23_cash_flow_trajectory_stability_10d_slope_v072_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(_m(x, 10), _m(x.diff(5).abs(), 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory decay balance slope
def f23cft_f23_cash_flow_trajectory_ewm_balance_21d_slope_v073_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=21, adjust=False).mean())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory accumulation ratio slope
def f23cft_f23_cash_flow_trajectory_positive_share_63d_slope_v074_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div((x - _m(x, 63)).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory capitulation ratio slope
def f23cft_f23_cash_flow_trajectory_negative_share_126d_slope_v075_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div((_m(x, 126) - x).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory level zscore slope
def f23cft_f23_cash_flow_trajectory_zlevel_252d_slope_v076_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _z(x, 252)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory level to mean slope
def f23cft_f23_cash_flow_trajectory_mean_ratio_504d_slope_v077_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x, _m(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory short minus long slope
def f23cft_f23_cash_flow_trajectory_ma_spread_5d_slope_v078_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _spread(_m(x, 3), _m(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory ranked pressure slope
def f23cft_f23_cash_flow_trajectory_rank_pressure_10d_slope_v079_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10)) + _z(x, 5) / np.sqrt(10)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory trend strength slope
def f23cft_f23_cash_flow_trajectory_trend_force_21d_slope_v080_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x.diff(5), _s(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory downside gap slope
def f23cft_f23_cash_flow_trajectory_down_tail_63d_slope_v081_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x.rolling(63, min_periods=2).quantile(0.20) - x, _s(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory upside gap slope
def f23cft_f23_cash_flow_trajectory_up_tail_126d_slope_v082_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x - x.rolling(126, min_periods=2).quantile(0.80), _s(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory range position slope
def f23cft_f23_cash_flow_trajectory_range_pos_252d_slope_v083_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x - _mn(x, 252), _mx(x, 252) - _mn(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory mean reversion slope
def f23cft_f23_cash_flow_trajectory_revert_gap_504d_slope_v084_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(_m(x, 21) - x, _s(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory expanding pressure slope
def f23cft_f23_cash_flow_trajectory_std_expand_5d_slope_v085_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(_s(x, 3), _s(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory compression ratio slope
def f23cft_f23_cash_flow_trajectory_std_compress_10d_slope_v086_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(_s(x, 10), _s(x, 20))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory breakout ratio slope
def f23cft_f23_cash_flow_trajectory_breakout_21d_slope_v087_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x, _mx(x, 21).shift(1))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory drawdown distance slope
def f23cft_f23_cash_flow_trajectory_drawdown_63d_slope_v088_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x - _mx(x, 63), _mx(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory recovery distance slope
def f23cft_f23_cash_flow_trajectory_recovery_126d_slope_v089_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x - _mn(x, 126), _mn(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory persistence share slope
def f23cft_f23_cash_flow_trajectory_persist_share_252d_slope_v090_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(_m(x.diff(21), 252), _m(x.diff(21).abs(), 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory shock frequency slope
def f23cft_f23_cash_flow_trajectory_shock_freq_504d_slope_v091_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _m(_z(x.diff(21), 504).abs(), 504)
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory tail pressure slope
def f23cft_f23_cash_flow_trajectory_tail_skew_5d_slope_v092_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x.rolling(5, min_periods=2).skew(), _s(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory median distance slope
def f23cft_f23_cash_flow_trajectory_median_gap_10d_slope_v093_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x - x.rolling(10, min_periods=2).median(), _s(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory vol scaled level slope
def f23cft_f23_cash_flow_trajectory_vol_scaled_21d_slope_v094_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x, _s(x.diff(5), 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory liquidity weight slope
def f23cft_f23_cash_flow_trajectory_abs_rank_weight_63d_slope_v095_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = x * x.abs().rolling(63, min_periods=2).rank(pct=True)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory dollar weight slope
def f23cft_f23_cash_flow_trajectory_abs_mean_weight_126d_slope_v096_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _z(x * _m(x.abs(), 21), 126)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory stability score slope
def f23cft_f23_cash_flow_trajectory_stability_252d_slope_v097_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(_m(x, 252), _m(x.diff(21).abs(), 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory decay balance slope
def f23cft_f23_cash_flow_trajectory_ewm_balance_504d_slope_v098_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=504, adjust=False).mean())
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory accumulation ratio slope
def f23cft_f23_cash_flow_trajectory_positive_share_5d_slope_v099_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div((x - _m(x, 5)).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory capitulation ratio slope
def f23cft_f23_cash_flow_trajectory_negative_share_10d_slope_v100_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div((_m(x, 10) - x).clip(lower=0).rolling(10, min_periods=2).sum(), (x - _m(x, 10)).abs().rolling(10, min_periods=2).sum())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory level zscore slope
def f23cft_f23_cash_flow_trajectory_zlevel_21d_slope_v101_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _z(x, 21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory level to mean slope
def f23cft_f23_cash_flow_trajectory_mean_ratio_63d_slope_v102_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x, _m(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory short minus long slope
def f23cft_f23_cash_flow_trajectory_ma_spread_126d_slope_v103_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _spread(_m(x, 21), _m(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory ranked pressure slope
def f23cft_f23_cash_flow_trajectory_rank_pressure_252d_slope_v104_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x - _mn(x, 252), _mx(x, 252) - _mn(x, 252)) + _z(x, 21) / np.sqrt(252)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory trend strength slope
def f23cft_f23_cash_flow_trajectory_trend_force_504d_slope_v105_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x.diff(21), _s(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory downside gap slope
def f23cft_f23_cash_flow_trajectory_down_tail_5d_slope_v106_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x.rolling(5, min_periods=2).quantile(0.20) - x, _s(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory upside gap slope
def f23cft_f23_cash_flow_trajectory_up_tail_10d_slope_v107_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x - x.rolling(10, min_periods=2).quantile(0.80), _s(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory range position slope
def f23cft_f23_cash_flow_trajectory_range_pos_21d_slope_v108_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x - _mn(x, 21), _mx(x, 21) - _mn(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory mean reversion slope
def f23cft_f23_cash_flow_trajectory_revert_gap_63d_slope_v109_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(_m(x, 21) - x, _s(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory expanding pressure slope
def f23cft_f23_cash_flow_trajectory_std_expand_126d_slope_v110_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(_s(x, 21), _s(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory compression ratio slope
def f23cft_f23_cash_flow_trajectory_std_compress_252d_slope_v111_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(_s(x, 252), _s(x, 504))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory breakout ratio slope
def f23cft_f23_cash_flow_trajectory_breakout_504d_slope_v112_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x, _mx(x, 504).shift(1))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory drawdown distance slope
def f23cft_f23_cash_flow_trajectory_drawdown_5d_slope_v113_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x - _mx(x, 5), _mx(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory recovery distance slope
def f23cft_f23_cash_flow_trajectory_recovery_10d_slope_v114_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x - _mn(x, 10), _mn(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory persistence share slope
def f23cft_f23_cash_flow_trajectory_persist_share_21d_slope_v115_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(_m(x.diff(5), 21), _m(x.diff(5).abs(), 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory shock frequency slope
def f23cft_f23_cash_flow_trajectory_shock_freq_63d_slope_v116_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _m(_z(x.diff(21), 63).abs(), 63)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory tail pressure slope
def f23cft_f23_cash_flow_trajectory_tail_skew_126d_slope_v117_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x.rolling(126, min_periods=2).skew(), _s(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory median distance slope
def f23cft_f23_cash_flow_trajectory_median_gap_252d_slope_v118_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x - x.rolling(252, min_periods=2).median(), _s(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory vol scaled level slope
def f23cft_f23_cash_flow_trajectory_vol_scaled_504d_slope_v119_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x, _s(x.diff(21), 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory liquidity weight slope
def f23cft_f23_cash_flow_trajectory_abs_rank_weight_5d_slope_v120_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = x * x.abs().rolling(5, min_periods=2).rank(pct=True)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory dollar weight slope
def f23cft_f23_cash_flow_trajectory_abs_mean_weight_10d_slope_v121_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _z(x * _m(x.abs(), 5), 10)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory stability score slope
def f23cft_f23_cash_flow_trajectory_stability_21d_slope_v122_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(_m(x, 21), _m(x.diff(5).abs(), 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory decay balance slope
def f23cft_f23_cash_flow_trajectory_ewm_balance_63d_slope_v123_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=63, adjust=False).mean())
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory accumulation ratio slope
def f23cft_f23_cash_flow_trajectory_positive_share_126d_slope_v124_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div((x - _m(x, 126)).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory capitulation ratio slope
def f23cft_f23_cash_flow_trajectory_negative_share_252d_slope_v125_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div((_m(x, 252) - x).clip(lower=0).rolling(252, min_periods=2).sum(), (x - _m(x, 252)).abs().rolling(252, min_periods=2).sum())
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory level zscore slope
def f23cft_f23_cash_flow_trajectory_zlevel_504d_slope_v126_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _z(x, 504)
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory level to mean slope
def f23cft_f23_cash_flow_trajectory_mean_ratio_5d_slope_v127_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x, _m(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory short minus long slope
def f23cft_f23_cash_flow_trajectory_ma_spread_10d_slope_v128_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _spread(_m(x, 5), _m(x, 20))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory ranked pressure slope
def f23cft_f23_cash_flow_trajectory_rank_pressure_21d_slope_v129_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x - _mn(x, 21), _mx(x, 21) - _mn(x, 21)) + _z(x, 5) / np.sqrt(21)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory trend strength slope
def f23cft_f23_cash_flow_trajectory_trend_force_63d_slope_v130_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x.diff(21), _s(x, 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory downside gap slope
def f23cft_f23_cash_flow_trajectory_down_tail_126d_slope_v131_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x.rolling(126, min_periods=2).quantile(0.20) - x, _s(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory upside gap slope
def f23cft_f23_cash_flow_trajectory_up_tail_252d_slope_v132_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x - x.rolling(252, min_periods=2).quantile(0.80), _s(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory range position slope
def f23cft_f23_cash_flow_trajectory_range_pos_504d_slope_v133_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(x - _mn(x, 504), _mx(x, 504) - _mn(x, 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory mean reversion slope
def f23cft_f23_cash_flow_trajectory_revert_gap_5d_slope_v134_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(_m(x, 3) - x, _s(x, 5))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory expanding pressure slope
def f23cft_f23_cash_flow_trajectory_std_expand_10d_slope_v135_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(_s(x, 5), _s(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory compression ratio slope
def f23cft_f23_cash_flow_trajectory_std_compress_21d_slope_v136_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(_s(x, 21), _s(x, 42))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory breakout ratio slope
def f23cft_f23_cash_flow_trajectory_breakout_63d_slope_v137_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x, _mx(x, 63).shift(1))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory drawdown distance slope
def f23cft_f23_cash_flow_trajectory_drawdown_126d_slope_v138_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = _safe_div(x - _mx(x, 126), _mx(x, 126))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory recovery distance slope
def f23cft_f23_cash_flow_trajectory_recovery_252d_slope_v139_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _safe_div(x - _mn(x, 252), _mn(x, 252))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory persistence share slope
def f23cft_f23_cash_flow_trajectory_persist_share_504d_slope_v140_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(_m(x.diff(21), 504), _m(x.diff(21).abs(), 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory shock frequency slope
def f23cft_f23_cash_flow_trajectory_shock_freq_5d_slope_v141_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _m(_z(x.diff(3), 5).abs(), 5)
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory tail pressure slope
def f23cft_f23_cash_flow_trajectory_tail_skew_10d_slope_v142_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div(x.rolling(10, min_periods=2).skew(), _s(x, 10))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory median distance slope
def f23cft_f23_cash_flow_trajectory_median_gap_21d_slope_v143_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div(x - x.rolling(21, min_periods=2).median(), _s(x, 21))
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_flow_trajectory vol scaled level slope
def f23cft_f23_cash_flow_trajectory_vol_scaled_63d_slope_v144_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 63)
    base = _safe_div(x, _s(x.diff(21), 63))
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_flow_trajectory liquidity weight slope
def f23cft_f23_cash_flow_trajectory_abs_rank_weight_126d_slope_v145_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 126)
    base = x * x.abs().rolling(126, min_periods=2).rank(pct=True)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_flow_trajectory dollar weight slope
def f23cft_f23_cash_flow_trajectory_abs_mean_weight_252d_slope_v146_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 252)
    base = _z(x * _m(x.abs(), 21), 252)
    result = _roc(base, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_flow_trajectory stability score slope
def f23cft_f23_cash_flow_trajectory_stability_504d_slope_v147_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 504)
    base = _safe_div(_m(x, 504), _m(x.diff(21).abs(), 504))
    result = _roc(base, 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_flow_trajectory decay balance slope
def f23cft_f23_cash_flow_trajectory_ewm_balance_5d_slope_v148_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 5)
    base = _safe_div(x.ewm(span=3, adjust=False).mean(), x.ewm(span=5, adjust=False).mean())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_flow_trajectory accumulation ratio slope
def f23cft_f23_cash_flow_trajectory_positive_share_10d_slope_v149_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 10)
    base = _safe_div((x - _m(x, 10)).clip(lower=0).rolling(10, min_periods=2).sum(), (x - _m(x, 10)).abs().rolling(10, min_periods=2).sum())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_flow_trajectory capitulation ratio slope
def f23cft_f23_cash_flow_trajectory_negative_share_21d_slope_v150_signal(closeadj, volume):
    x = _f23_cash_flow_trajectory_primitive(closeadj, volume, 21)
    base = _safe_div((_m(x, 21) - x).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    result = _roc(base, 5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f23cft_f23_cash_flow_trajectory_zlevel_5d_slope_v001_signal,
    f23cft_f23_cash_flow_trajectory_mean_ratio_10d_slope_v002_signal,
    f23cft_f23_cash_flow_trajectory_ma_spread_21d_slope_v003_signal,
    f23cft_f23_cash_flow_trajectory_rank_pressure_63d_slope_v004_signal,
    f23cft_f23_cash_flow_trajectory_trend_force_126d_slope_v005_signal,
    f23cft_f23_cash_flow_trajectory_down_tail_252d_slope_v006_signal,
    f23cft_f23_cash_flow_trajectory_up_tail_504d_slope_v007_signal,
    f23cft_f23_cash_flow_trajectory_range_pos_5d_slope_v008_signal,
    f23cft_f23_cash_flow_trajectory_revert_gap_10d_slope_v009_signal,
    f23cft_f23_cash_flow_trajectory_std_expand_21d_slope_v010_signal,
    f23cft_f23_cash_flow_trajectory_std_compress_63d_slope_v011_signal,
    f23cft_f23_cash_flow_trajectory_breakout_126d_slope_v012_signal,
    f23cft_f23_cash_flow_trajectory_drawdown_252d_slope_v013_signal,
    f23cft_f23_cash_flow_trajectory_recovery_504d_slope_v014_signal,
    f23cft_f23_cash_flow_trajectory_persist_share_5d_slope_v015_signal,
    f23cft_f23_cash_flow_trajectory_shock_freq_10d_slope_v016_signal,
    f23cft_f23_cash_flow_trajectory_tail_skew_21d_slope_v017_signal,
    f23cft_f23_cash_flow_trajectory_median_gap_63d_slope_v018_signal,
    f23cft_f23_cash_flow_trajectory_vol_scaled_126d_slope_v019_signal,
    f23cft_f23_cash_flow_trajectory_abs_rank_weight_252d_slope_v020_signal,
    f23cft_f23_cash_flow_trajectory_abs_mean_weight_504d_slope_v021_signal,
    f23cft_f23_cash_flow_trajectory_stability_5d_slope_v022_signal,
    f23cft_f23_cash_flow_trajectory_ewm_balance_10d_slope_v023_signal,
    f23cft_f23_cash_flow_trajectory_positive_share_21d_slope_v024_signal,
    f23cft_f23_cash_flow_trajectory_negative_share_63d_slope_v025_signal,
    f23cft_f23_cash_flow_trajectory_zlevel_126d_slope_v026_signal,
    f23cft_f23_cash_flow_trajectory_mean_ratio_252d_slope_v027_signal,
    f23cft_f23_cash_flow_trajectory_ma_spread_504d_slope_v028_signal,
    f23cft_f23_cash_flow_trajectory_rank_pressure_5d_slope_v029_signal,
    f23cft_f23_cash_flow_trajectory_trend_force_10d_slope_v030_signal,
    f23cft_f23_cash_flow_trajectory_down_tail_21d_slope_v031_signal,
    f23cft_f23_cash_flow_trajectory_up_tail_63d_slope_v032_signal,
    f23cft_f23_cash_flow_trajectory_range_pos_126d_slope_v033_signal,
    f23cft_f23_cash_flow_trajectory_revert_gap_252d_slope_v034_signal,
    f23cft_f23_cash_flow_trajectory_std_expand_504d_slope_v035_signal,
    f23cft_f23_cash_flow_trajectory_std_compress_5d_slope_v036_signal,
    f23cft_f23_cash_flow_trajectory_breakout_10d_slope_v037_signal,
    f23cft_f23_cash_flow_trajectory_drawdown_21d_slope_v038_signal,
    f23cft_f23_cash_flow_trajectory_recovery_63d_slope_v039_signal,
    f23cft_f23_cash_flow_trajectory_persist_share_126d_slope_v040_signal,
    f23cft_f23_cash_flow_trajectory_shock_freq_252d_slope_v041_signal,
    f23cft_f23_cash_flow_trajectory_tail_skew_504d_slope_v042_signal,
    f23cft_f23_cash_flow_trajectory_median_gap_5d_slope_v043_signal,
    f23cft_f23_cash_flow_trajectory_vol_scaled_10d_slope_v044_signal,
    f23cft_f23_cash_flow_trajectory_abs_rank_weight_21d_slope_v045_signal,
    f23cft_f23_cash_flow_trajectory_abs_mean_weight_63d_slope_v046_signal,
    f23cft_f23_cash_flow_trajectory_stability_126d_slope_v047_signal,
    f23cft_f23_cash_flow_trajectory_ewm_balance_252d_slope_v048_signal,
    f23cft_f23_cash_flow_trajectory_positive_share_504d_slope_v049_signal,
    f23cft_f23_cash_flow_trajectory_negative_share_5d_slope_v050_signal,
    f23cft_f23_cash_flow_trajectory_zlevel_10d_slope_v051_signal,
    f23cft_f23_cash_flow_trajectory_mean_ratio_21d_slope_v052_signal,
    f23cft_f23_cash_flow_trajectory_ma_spread_63d_slope_v053_signal,
    f23cft_f23_cash_flow_trajectory_rank_pressure_126d_slope_v054_signal,
    f23cft_f23_cash_flow_trajectory_trend_force_252d_slope_v055_signal,
    f23cft_f23_cash_flow_trajectory_down_tail_504d_slope_v056_signal,
    f23cft_f23_cash_flow_trajectory_up_tail_5d_slope_v057_signal,
    f23cft_f23_cash_flow_trajectory_range_pos_10d_slope_v058_signal,
    f23cft_f23_cash_flow_trajectory_revert_gap_21d_slope_v059_signal,
    f23cft_f23_cash_flow_trajectory_std_expand_63d_slope_v060_signal,
    f23cft_f23_cash_flow_trajectory_std_compress_126d_slope_v061_signal,
    f23cft_f23_cash_flow_trajectory_breakout_252d_slope_v062_signal,
    f23cft_f23_cash_flow_trajectory_drawdown_504d_slope_v063_signal,
    f23cft_f23_cash_flow_trajectory_recovery_5d_slope_v064_signal,
    f23cft_f23_cash_flow_trajectory_persist_share_10d_slope_v065_signal,
    f23cft_f23_cash_flow_trajectory_shock_freq_21d_slope_v066_signal,
    f23cft_f23_cash_flow_trajectory_tail_skew_63d_slope_v067_signal,
    f23cft_f23_cash_flow_trajectory_median_gap_126d_slope_v068_signal,
    f23cft_f23_cash_flow_trajectory_vol_scaled_252d_slope_v069_signal,
    f23cft_f23_cash_flow_trajectory_abs_rank_weight_504d_slope_v070_signal,
    f23cft_f23_cash_flow_trajectory_abs_mean_weight_5d_slope_v071_signal,
    f23cft_f23_cash_flow_trajectory_stability_10d_slope_v072_signal,
    f23cft_f23_cash_flow_trajectory_ewm_balance_21d_slope_v073_signal,
    f23cft_f23_cash_flow_trajectory_positive_share_63d_slope_v074_signal,
    f23cft_f23_cash_flow_trajectory_negative_share_126d_slope_v075_signal,
    f23cft_f23_cash_flow_trajectory_zlevel_252d_slope_v076_signal,
    f23cft_f23_cash_flow_trajectory_mean_ratio_504d_slope_v077_signal,
    f23cft_f23_cash_flow_trajectory_ma_spread_5d_slope_v078_signal,
    f23cft_f23_cash_flow_trajectory_rank_pressure_10d_slope_v079_signal,
    f23cft_f23_cash_flow_trajectory_trend_force_21d_slope_v080_signal,
    f23cft_f23_cash_flow_trajectory_down_tail_63d_slope_v081_signal,
    f23cft_f23_cash_flow_trajectory_up_tail_126d_slope_v082_signal,
    f23cft_f23_cash_flow_trajectory_range_pos_252d_slope_v083_signal,
    f23cft_f23_cash_flow_trajectory_revert_gap_504d_slope_v084_signal,
    f23cft_f23_cash_flow_trajectory_std_expand_5d_slope_v085_signal,
    f23cft_f23_cash_flow_trajectory_std_compress_10d_slope_v086_signal,
    f23cft_f23_cash_flow_trajectory_breakout_21d_slope_v087_signal,
    f23cft_f23_cash_flow_trajectory_drawdown_63d_slope_v088_signal,
    f23cft_f23_cash_flow_trajectory_recovery_126d_slope_v089_signal,
    f23cft_f23_cash_flow_trajectory_persist_share_252d_slope_v090_signal,
    f23cft_f23_cash_flow_trajectory_shock_freq_504d_slope_v091_signal,
    f23cft_f23_cash_flow_trajectory_tail_skew_5d_slope_v092_signal,
    f23cft_f23_cash_flow_trajectory_median_gap_10d_slope_v093_signal,
    f23cft_f23_cash_flow_trajectory_vol_scaled_21d_slope_v094_signal,
    f23cft_f23_cash_flow_trajectory_abs_rank_weight_63d_slope_v095_signal,
    f23cft_f23_cash_flow_trajectory_abs_mean_weight_126d_slope_v096_signal,
    f23cft_f23_cash_flow_trajectory_stability_252d_slope_v097_signal,
    f23cft_f23_cash_flow_trajectory_ewm_balance_504d_slope_v098_signal,
    f23cft_f23_cash_flow_trajectory_positive_share_5d_slope_v099_signal,
    f23cft_f23_cash_flow_trajectory_negative_share_10d_slope_v100_signal,
    f23cft_f23_cash_flow_trajectory_zlevel_21d_slope_v101_signal,
    f23cft_f23_cash_flow_trajectory_mean_ratio_63d_slope_v102_signal,
    f23cft_f23_cash_flow_trajectory_ma_spread_126d_slope_v103_signal,
    f23cft_f23_cash_flow_trajectory_rank_pressure_252d_slope_v104_signal,
    f23cft_f23_cash_flow_trajectory_trend_force_504d_slope_v105_signal,
    f23cft_f23_cash_flow_trajectory_down_tail_5d_slope_v106_signal,
    f23cft_f23_cash_flow_trajectory_up_tail_10d_slope_v107_signal,
    f23cft_f23_cash_flow_trajectory_range_pos_21d_slope_v108_signal,
    f23cft_f23_cash_flow_trajectory_revert_gap_63d_slope_v109_signal,
    f23cft_f23_cash_flow_trajectory_std_expand_126d_slope_v110_signal,
    f23cft_f23_cash_flow_trajectory_std_compress_252d_slope_v111_signal,
    f23cft_f23_cash_flow_trajectory_breakout_504d_slope_v112_signal,
    f23cft_f23_cash_flow_trajectory_drawdown_5d_slope_v113_signal,
    f23cft_f23_cash_flow_trajectory_recovery_10d_slope_v114_signal,
    f23cft_f23_cash_flow_trajectory_persist_share_21d_slope_v115_signal,
    f23cft_f23_cash_flow_trajectory_shock_freq_63d_slope_v116_signal,
    f23cft_f23_cash_flow_trajectory_tail_skew_126d_slope_v117_signal,
    f23cft_f23_cash_flow_trajectory_median_gap_252d_slope_v118_signal,
    f23cft_f23_cash_flow_trajectory_vol_scaled_504d_slope_v119_signal,
    f23cft_f23_cash_flow_trajectory_abs_rank_weight_5d_slope_v120_signal,
    f23cft_f23_cash_flow_trajectory_abs_mean_weight_10d_slope_v121_signal,
    f23cft_f23_cash_flow_trajectory_stability_21d_slope_v122_signal,
    f23cft_f23_cash_flow_trajectory_ewm_balance_63d_slope_v123_signal,
    f23cft_f23_cash_flow_trajectory_positive_share_126d_slope_v124_signal,
    f23cft_f23_cash_flow_trajectory_negative_share_252d_slope_v125_signal,
    f23cft_f23_cash_flow_trajectory_zlevel_504d_slope_v126_signal,
    f23cft_f23_cash_flow_trajectory_mean_ratio_5d_slope_v127_signal,
    f23cft_f23_cash_flow_trajectory_ma_spread_10d_slope_v128_signal,
    f23cft_f23_cash_flow_trajectory_rank_pressure_21d_slope_v129_signal,
    f23cft_f23_cash_flow_trajectory_trend_force_63d_slope_v130_signal,
    f23cft_f23_cash_flow_trajectory_down_tail_126d_slope_v131_signal,
    f23cft_f23_cash_flow_trajectory_up_tail_252d_slope_v132_signal,
    f23cft_f23_cash_flow_trajectory_range_pos_504d_slope_v133_signal,
    f23cft_f23_cash_flow_trajectory_revert_gap_5d_slope_v134_signal,
    f23cft_f23_cash_flow_trajectory_std_expand_10d_slope_v135_signal,
    f23cft_f23_cash_flow_trajectory_std_compress_21d_slope_v136_signal,
    f23cft_f23_cash_flow_trajectory_breakout_63d_slope_v137_signal,
    f23cft_f23_cash_flow_trajectory_drawdown_126d_slope_v138_signal,
    f23cft_f23_cash_flow_trajectory_recovery_252d_slope_v139_signal,
    f23cft_f23_cash_flow_trajectory_persist_share_504d_slope_v140_signal,
    f23cft_f23_cash_flow_trajectory_shock_freq_5d_slope_v141_signal,
    f23cft_f23_cash_flow_trajectory_tail_skew_10d_slope_v142_signal,
    f23cft_f23_cash_flow_trajectory_median_gap_21d_slope_v143_signal,
    f23cft_f23_cash_flow_trajectory_vol_scaled_63d_slope_v144_signal,
    f23cft_f23_cash_flow_trajectory_abs_rank_weight_126d_slope_v145_signal,
    f23cft_f23_cash_flow_trajectory_abs_mean_weight_252d_slope_v146_signal,
    f23cft_f23_cash_flow_trajectory_stability_504d_slope_v147_signal,
    f23cft_f23_cash_flow_trajectory_ewm_balance_5d_slope_v148_signal,
    f23cft_f23_cash_flow_trajectory_positive_share_10d_slope_v149_signal,
    f23cft_f23_cash_flow_trajectory_negative_share_21d_slope_v150_signal,
]
REGISTRY = {fn.__name__: {"inputs": ['closeadj', 'volume'], "func": fn} for fn in _FEATURES}


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    idx = pd.RangeIndex(n)
    closeadj = pd.Series(50.0 + np.cumsum(np.random.normal(0.05, 1.0, n)), index=idx).abs() + 1.0
    volume = pd.Series(np.random.lognormal(12.0, 0.35, n), index=idx)
    namespace = locals()
    valid_nan = 0
    for name, meta in REGISTRY.items():
        func = meta["func"]
        args = [namespace[col] for col in meta["inputs"]]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 50
        assert q.std() > 0
        assert not q.isna().all()
        valid_nan += int(y1.iloc[504:].isna().mean() < 0.50)
        assert '_f23_cash_flow_trajectory_primitive' in inspect.getsource(func)
    assert valid_nan >= int(len(REGISTRY) * 0.80)


F23_CASH_FLOW_TRAJECTORY_REGISTRY_SLOPE = REGISTRY
