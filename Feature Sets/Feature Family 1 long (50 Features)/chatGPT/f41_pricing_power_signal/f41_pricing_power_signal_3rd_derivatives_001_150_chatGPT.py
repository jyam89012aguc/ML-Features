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


def _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, w):
    scale = assets.abs().replace(0, np.nan)
    operating = _safe_div(revenue + netinc + fcf, scale)
    return _z(operating, w)


# 5d pricing_power_signal level zscore jerk
def f41pps_f41_pricing_power_signal_zlevel_5d_jerk_v001_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _z(x, 5)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal level to mean jerk
def f41pps_f41_pricing_power_signal_mean_ratio_10d_jerk_v002_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x, _m(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal short minus long jerk
def f41pps_f41_pricing_power_signal_ma_spread_21d_jerk_v003_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _spread(_m(x, 5), _m(x, 42))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal ranked pressure jerk
def f41pps_f41_pricing_power_signal_rank_pressure_63d_jerk_v004_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x - _mn(x, 63), _mx(x, 63) - _mn(x, 63)) + _z(x, 21) / np.sqrt(63)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal trend strength jerk
def f41pps_f41_pricing_power_signal_trend_force_126d_jerk_v005_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x.diff(21), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal downside gap jerk
def f41pps_f41_pricing_power_signal_down_tail_252d_jerk_v006_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x.rolling(252, min_periods=2).quantile(0.20) - x, _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal upside gap jerk
def f41pps_f41_pricing_power_signal_up_tail_504d_jerk_v007_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x - x.rolling(504, min_periods=2).quantile(0.80), _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal range position jerk
def f41pps_f41_pricing_power_signal_range_pos_5d_jerk_v008_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal mean reversion jerk
def f41pps_f41_pricing_power_signal_revert_gap_10d_jerk_v009_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(_m(x, 5) - x, _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal expanding pressure jerk
def f41pps_f41_pricing_power_signal_std_expand_21d_jerk_v010_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(_s(x, 5), _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal compression ratio jerk
def f41pps_f41_pricing_power_signal_std_compress_63d_jerk_v011_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(_s(x, 63), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal breakout ratio jerk
def f41pps_f41_pricing_power_signal_breakout_126d_jerk_v012_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x, _mx(x, 126).shift(1))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal drawdown distance jerk
def f41pps_f41_pricing_power_signal_drawdown_252d_jerk_v013_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x - _mx(x, 252), _mx(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal recovery distance jerk
def f41pps_f41_pricing_power_signal_recovery_504d_jerk_v014_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x - _mn(x, 504), _mn(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal persistence share jerk
def f41pps_f41_pricing_power_signal_persist_share_5d_jerk_v015_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(_m(x.diff(3), 5), _m(x.diff(3).abs(), 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal shock frequency jerk
def f41pps_f41_pricing_power_signal_shock_freq_10d_jerk_v016_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _m(_z(x.diff(5), 10).abs(), 10)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal tail pressure jerk
def f41pps_f41_pricing_power_signal_tail_skew_21d_jerk_v017_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x.rolling(21, min_periods=2).skew(), _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal median distance jerk
def f41pps_f41_pricing_power_signal_median_gap_63d_jerk_v018_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x - x.rolling(63, min_periods=2).median(), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal vol scaled level jerk
def f41pps_f41_pricing_power_signal_vol_scaled_126d_jerk_v019_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x, _s(x.diff(21), 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal liquidity weight jerk
def f41pps_f41_pricing_power_signal_abs_rank_weight_252d_jerk_v020_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = x * x.abs().rolling(252, min_periods=2).rank(pct=True)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal dollar weight jerk
def f41pps_f41_pricing_power_signal_abs_mean_weight_504d_jerk_v021_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _z(x * _m(x.abs(), 21), 504)
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal stability score jerk
def f41pps_f41_pricing_power_signal_stability_5d_jerk_v022_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(_m(x, 5), _m(x.diff(3).abs(), 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal decay balance jerk
def f41pps_f41_pricing_power_signal_ewm_balance_10d_jerk_v023_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=10, adjust=False).mean())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal accumulation ratio jerk
def f41pps_f41_pricing_power_signal_positive_share_21d_jerk_v024_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div((x - _m(x, 21)).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal capitulation ratio jerk
def f41pps_f41_pricing_power_signal_negative_share_63d_jerk_v025_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div((_m(x, 63) - x).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal level zscore jerk
def f41pps_f41_pricing_power_signal_zlevel_126d_jerk_v026_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _z(x, 126)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal level to mean jerk
def f41pps_f41_pricing_power_signal_mean_ratio_252d_jerk_v027_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x, _m(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal short minus long jerk
def f41pps_f41_pricing_power_signal_ma_spread_504d_jerk_v028_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _spread(_m(x, 21), _m(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal ranked pressure jerk
def f41pps_f41_pricing_power_signal_rank_pressure_5d_jerk_v029_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5)) + _z(x, 3) / np.sqrt(5)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal trend strength jerk
def f41pps_f41_pricing_power_signal_trend_force_10d_jerk_v030_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x.diff(5), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal downside gap jerk
def f41pps_f41_pricing_power_signal_down_tail_21d_jerk_v031_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x.rolling(21, min_periods=2).quantile(0.20) - x, _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal upside gap jerk
def f41pps_f41_pricing_power_signal_up_tail_63d_jerk_v032_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x - x.rolling(63, min_periods=2).quantile(0.80), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal range position jerk
def f41pps_f41_pricing_power_signal_range_pos_126d_jerk_v033_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal mean reversion jerk
def f41pps_f41_pricing_power_signal_revert_gap_252d_jerk_v034_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(_m(x, 21) - x, _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal expanding pressure jerk
def f41pps_f41_pricing_power_signal_std_expand_504d_jerk_v035_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(_s(x, 21), _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal compression ratio jerk
def f41pps_f41_pricing_power_signal_std_compress_5d_jerk_v036_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(_s(x, 5), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal breakout ratio jerk
def f41pps_f41_pricing_power_signal_breakout_10d_jerk_v037_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x, _mx(x, 10).shift(1))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal drawdown distance jerk
def f41pps_f41_pricing_power_signal_drawdown_21d_jerk_v038_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x - _mx(x, 21), _mx(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal recovery distance jerk
def f41pps_f41_pricing_power_signal_recovery_63d_jerk_v039_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x - _mn(x, 63), _mn(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal persistence share jerk
def f41pps_f41_pricing_power_signal_persist_share_126d_jerk_v040_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(_m(x.diff(21), 126), _m(x.diff(21).abs(), 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal shock frequency jerk
def f41pps_f41_pricing_power_signal_shock_freq_252d_jerk_v041_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _m(_z(x.diff(21), 252).abs(), 252)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal tail pressure jerk
def f41pps_f41_pricing_power_signal_tail_skew_504d_jerk_v042_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x.rolling(504, min_periods=2).skew(), _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal median distance jerk
def f41pps_f41_pricing_power_signal_median_gap_5d_jerk_v043_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x - x.rolling(5, min_periods=2).median(), _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal vol scaled level jerk
def f41pps_f41_pricing_power_signal_vol_scaled_10d_jerk_v044_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x, _s(x.diff(5), 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal liquidity weight jerk
def f41pps_f41_pricing_power_signal_abs_rank_weight_21d_jerk_v045_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = x * x.abs().rolling(21, min_periods=2).rank(pct=True)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal dollar weight jerk
def f41pps_f41_pricing_power_signal_abs_mean_weight_63d_jerk_v046_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _z(x * _m(x.abs(), 21), 63)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal stability score jerk
def f41pps_f41_pricing_power_signal_stability_126d_jerk_v047_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(_m(x, 126), _m(x.diff(21).abs(), 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal decay balance jerk
def f41pps_f41_pricing_power_signal_ewm_balance_252d_jerk_v048_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=252, adjust=False).mean())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal accumulation ratio jerk
def f41pps_f41_pricing_power_signal_positive_share_504d_jerk_v049_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div((x - _m(x, 504)).clip(lower=0).rolling(504, min_periods=2).sum(), (x - _m(x, 504)).abs().rolling(504, min_periods=2).sum())
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal capitulation ratio jerk
def f41pps_f41_pricing_power_signal_negative_share_5d_jerk_v050_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div((_m(x, 5) - x).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal level zscore jerk
def f41pps_f41_pricing_power_signal_zlevel_10d_jerk_v051_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _z(x, 10)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal level to mean jerk
def f41pps_f41_pricing_power_signal_mean_ratio_21d_jerk_v052_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x, _m(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal short minus long jerk
def f41pps_f41_pricing_power_signal_ma_spread_63d_jerk_v053_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _spread(_m(x, 21), _m(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal ranked pressure jerk
def f41pps_f41_pricing_power_signal_rank_pressure_126d_jerk_v054_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126)) + _z(x, 21) / np.sqrt(126)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal trend strength jerk
def f41pps_f41_pricing_power_signal_trend_force_252d_jerk_v055_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x.diff(21), _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal downside gap jerk
def f41pps_f41_pricing_power_signal_down_tail_504d_jerk_v056_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x.rolling(504, min_periods=2).quantile(0.20) - x, _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal upside gap jerk
def f41pps_f41_pricing_power_signal_up_tail_5d_jerk_v057_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x - x.rolling(5, min_periods=2).quantile(0.80), _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal range position jerk
def f41pps_f41_pricing_power_signal_range_pos_10d_jerk_v058_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal mean reversion jerk
def f41pps_f41_pricing_power_signal_revert_gap_21d_jerk_v059_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(_m(x, 5) - x, _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal expanding pressure jerk
def f41pps_f41_pricing_power_signal_std_expand_63d_jerk_v060_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(_s(x, 21), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal compression ratio jerk
def f41pps_f41_pricing_power_signal_std_compress_126d_jerk_v061_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(_s(x, 126), _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal breakout ratio jerk
def f41pps_f41_pricing_power_signal_breakout_252d_jerk_v062_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x, _mx(x, 252).shift(1))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal drawdown distance jerk
def f41pps_f41_pricing_power_signal_drawdown_504d_jerk_v063_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x - _mx(x, 504), _mx(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal recovery distance jerk
def f41pps_f41_pricing_power_signal_recovery_5d_jerk_v064_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x - _mn(x, 5), _mn(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal persistence share jerk
def f41pps_f41_pricing_power_signal_persist_share_10d_jerk_v065_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(_m(x.diff(5), 10), _m(x.diff(5).abs(), 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal shock frequency jerk
def f41pps_f41_pricing_power_signal_shock_freq_21d_jerk_v066_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _m(_z(x.diff(5), 21).abs(), 21)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal tail pressure jerk
def f41pps_f41_pricing_power_signal_tail_skew_63d_jerk_v067_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x.rolling(63, min_periods=2).skew(), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal median distance jerk
def f41pps_f41_pricing_power_signal_median_gap_126d_jerk_v068_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x - x.rolling(126, min_periods=2).median(), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal vol scaled level jerk
def f41pps_f41_pricing_power_signal_vol_scaled_252d_jerk_v069_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x, _s(x.diff(21), 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal liquidity weight jerk
def f41pps_f41_pricing_power_signal_abs_rank_weight_504d_jerk_v070_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = x * x.abs().rolling(504, min_periods=2).rank(pct=True)
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal dollar weight jerk
def f41pps_f41_pricing_power_signal_abs_mean_weight_5d_jerk_v071_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _z(x * _m(x.abs(), 3), 5)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal stability score jerk
def f41pps_f41_pricing_power_signal_stability_10d_jerk_v072_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(_m(x, 10), _m(x.diff(5).abs(), 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal decay balance jerk
def f41pps_f41_pricing_power_signal_ewm_balance_21d_jerk_v073_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=21, adjust=False).mean())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal accumulation ratio jerk
def f41pps_f41_pricing_power_signal_positive_share_63d_jerk_v074_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div((x - _m(x, 63)).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal capitulation ratio jerk
def f41pps_f41_pricing_power_signal_negative_share_126d_jerk_v075_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div((_m(x, 126) - x).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal level zscore jerk
def f41pps_f41_pricing_power_signal_zlevel_252d_jerk_v076_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _z(x, 252)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal level to mean jerk
def f41pps_f41_pricing_power_signal_mean_ratio_504d_jerk_v077_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x, _m(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal short minus long jerk
def f41pps_f41_pricing_power_signal_ma_spread_5d_jerk_v078_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _spread(_m(x, 3), _m(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal ranked pressure jerk
def f41pps_f41_pricing_power_signal_rank_pressure_10d_jerk_v079_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10)) + _z(x, 5) / np.sqrt(10)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal trend strength jerk
def f41pps_f41_pricing_power_signal_trend_force_21d_jerk_v080_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x.diff(5), _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal downside gap jerk
def f41pps_f41_pricing_power_signal_down_tail_63d_jerk_v081_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x.rolling(63, min_periods=2).quantile(0.20) - x, _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal upside gap jerk
def f41pps_f41_pricing_power_signal_up_tail_126d_jerk_v082_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x - x.rolling(126, min_periods=2).quantile(0.80), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal range position jerk
def f41pps_f41_pricing_power_signal_range_pos_252d_jerk_v083_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x - _mn(x, 252), _mx(x, 252) - _mn(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal mean reversion jerk
def f41pps_f41_pricing_power_signal_revert_gap_504d_jerk_v084_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(_m(x, 21) - x, _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal expanding pressure jerk
def f41pps_f41_pricing_power_signal_std_expand_5d_jerk_v085_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(_s(x, 3), _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal compression ratio jerk
def f41pps_f41_pricing_power_signal_std_compress_10d_jerk_v086_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(_s(x, 10), _s(x, 20))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal breakout ratio jerk
def f41pps_f41_pricing_power_signal_breakout_21d_jerk_v087_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x, _mx(x, 21).shift(1))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal drawdown distance jerk
def f41pps_f41_pricing_power_signal_drawdown_63d_jerk_v088_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x - _mx(x, 63), _mx(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal recovery distance jerk
def f41pps_f41_pricing_power_signal_recovery_126d_jerk_v089_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x - _mn(x, 126), _mn(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal persistence share jerk
def f41pps_f41_pricing_power_signal_persist_share_252d_jerk_v090_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(_m(x.diff(21), 252), _m(x.diff(21).abs(), 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal shock frequency jerk
def f41pps_f41_pricing_power_signal_shock_freq_504d_jerk_v091_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _m(_z(x.diff(21), 504).abs(), 504)
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal tail pressure jerk
def f41pps_f41_pricing_power_signal_tail_skew_5d_jerk_v092_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x.rolling(5, min_periods=2).skew(), _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal median distance jerk
def f41pps_f41_pricing_power_signal_median_gap_10d_jerk_v093_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x - x.rolling(10, min_periods=2).median(), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal vol scaled level jerk
def f41pps_f41_pricing_power_signal_vol_scaled_21d_jerk_v094_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x, _s(x.diff(5), 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal liquidity weight jerk
def f41pps_f41_pricing_power_signal_abs_rank_weight_63d_jerk_v095_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = x * x.abs().rolling(63, min_periods=2).rank(pct=True)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal dollar weight jerk
def f41pps_f41_pricing_power_signal_abs_mean_weight_126d_jerk_v096_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _z(x * _m(x.abs(), 21), 126)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal stability score jerk
def f41pps_f41_pricing_power_signal_stability_252d_jerk_v097_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(_m(x, 252), _m(x.diff(21).abs(), 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal decay balance jerk
def f41pps_f41_pricing_power_signal_ewm_balance_504d_jerk_v098_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=504, adjust=False).mean())
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal accumulation ratio jerk
def f41pps_f41_pricing_power_signal_positive_share_5d_jerk_v099_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div((x - _m(x, 5)).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal capitulation ratio jerk
def f41pps_f41_pricing_power_signal_negative_share_10d_jerk_v100_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div((_m(x, 10) - x).clip(lower=0).rolling(10, min_periods=2).sum(), (x - _m(x, 10)).abs().rolling(10, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal level zscore jerk
def f41pps_f41_pricing_power_signal_zlevel_21d_jerk_v101_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _z(x, 21)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal level to mean jerk
def f41pps_f41_pricing_power_signal_mean_ratio_63d_jerk_v102_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x, _m(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal short minus long jerk
def f41pps_f41_pricing_power_signal_ma_spread_126d_jerk_v103_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _spread(_m(x, 21), _m(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal ranked pressure jerk
def f41pps_f41_pricing_power_signal_rank_pressure_252d_jerk_v104_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x - _mn(x, 252), _mx(x, 252) - _mn(x, 252)) + _z(x, 21) / np.sqrt(252)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal trend strength jerk
def f41pps_f41_pricing_power_signal_trend_force_504d_jerk_v105_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x.diff(21), _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal downside gap jerk
def f41pps_f41_pricing_power_signal_down_tail_5d_jerk_v106_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x.rolling(5, min_periods=2).quantile(0.20) - x, _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal upside gap jerk
def f41pps_f41_pricing_power_signal_up_tail_10d_jerk_v107_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x - x.rolling(10, min_periods=2).quantile(0.80), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal range position jerk
def f41pps_f41_pricing_power_signal_range_pos_21d_jerk_v108_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x - _mn(x, 21), _mx(x, 21) - _mn(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal mean reversion jerk
def f41pps_f41_pricing_power_signal_revert_gap_63d_jerk_v109_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(_m(x, 21) - x, _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal expanding pressure jerk
def f41pps_f41_pricing_power_signal_std_expand_126d_jerk_v110_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(_s(x, 21), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal compression ratio jerk
def f41pps_f41_pricing_power_signal_std_compress_252d_jerk_v111_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(_s(x, 252), _s(x, 504))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal breakout ratio jerk
def f41pps_f41_pricing_power_signal_breakout_504d_jerk_v112_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x, _mx(x, 504).shift(1))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal drawdown distance jerk
def f41pps_f41_pricing_power_signal_drawdown_5d_jerk_v113_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x - _mx(x, 5), _mx(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal recovery distance jerk
def f41pps_f41_pricing_power_signal_recovery_10d_jerk_v114_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x - _mn(x, 10), _mn(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal persistence share jerk
def f41pps_f41_pricing_power_signal_persist_share_21d_jerk_v115_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(_m(x.diff(5), 21), _m(x.diff(5).abs(), 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal shock frequency jerk
def f41pps_f41_pricing_power_signal_shock_freq_63d_jerk_v116_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _m(_z(x.diff(21), 63).abs(), 63)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal tail pressure jerk
def f41pps_f41_pricing_power_signal_tail_skew_126d_jerk_v117_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x.rolling(126, min_periods=2).skew(), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal median distance jerk
def f41pps_f41_pricing_power_signal_median_gap_252d_jerk_v118_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x - x.rolling(252, min_periods=2).median(), _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal vol scaled level jerk
def f41pps_f41_pricing_power_signal_vol_scaled_504d_jerk_v119_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x, _s(x.diff(21), 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal liquidity weight jerk
def f41pps_f41_pricing_power_signal_abs_rank_weight_5d_jerk_v120_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = x * x.abs().rolling(5, min_periods=2).rank(pct=True)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal dollar weight jerk
def f41pps_f41_pricing_power_signal_abs_mean_weight_10d_jerk_v121_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _z(x * _m(x.abs(), 5), 10)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal stability score jerk
def f41pps_f41_pricing_power_signal_stability_21d_jerk_v122_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(_m(x, 21), _m(x.diff(5).abs(), 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal decay balance jerk
def f41pps_f41_pricing_power_signal_ewm_balance_63d_jerk_v123_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=63, adjust=False).mean())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal accumulation ratio jerk
def f41pps_f41_pricing_power_signal_positive_share_126d_jerk_v124_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div((x - _m(x, 126)).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal capitulation ratio jerk
def f41pps_f41_pricing_power_signal_negative_share_252d_jerk_v125_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div((_m(x, 252) - x).clip(lower=0).rolling(252, min_periods=2).sum(), (x - _m(x, 252)).abs().rolling(252, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal level zscore jerk
def f41pps_f41_pricing_power_signal_zlevel_504d_jerk_v126_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _z(x, 504)
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal level to mean jerk
def f41pps_f41_pricing_power_signal_mean_ratio_5d_jerk_v127_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x, _m(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal short minus long jerk
def f41pps_f41_pricing_power_signal_ma_spread_10d_jerk_v128_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _spread(_m(x, 5), _m(x, 20))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal ranked pressure jerk
def f41pps_f41_pricing_power_signal_rank_pressure_21d_jerk_v129_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x - _mn(x, 21), _mx(x, 21) - _mn(x, 21)) + _z(x, 5) / np.sqrt(21)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal trend strength jerk
def f41pps_f41_pricing_power_signal_trend_force_63d_jerk_v130_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x.diff(21), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal downside gap jerk
def f41pps_f41_pricing_power_signal_down_tail_126d_jerk_v131_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x.rolling(126, min_periods=2).quantile(0.20) - x, _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal upside gap jerk
def f41pps_f41_pricing_power_signal_up_tail_252d_jerk_v132_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x - x.rolling(252, min_periods=2).quantile(0.80), _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal range position jerk
def f41pps_f41_pricing_power_signal_range_pos_504d_jerk_v133_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(x - _mn(x, 504), _mx(x, 504) - _mn(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal mean reversion jerk
def f41pps_f41_pricing_power_signal_revert_gap_5d_jerk_v134_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(_m(x, 3) - x, _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal expanding pressure jerk
def f41pps_f41_pricing_power_signal_std_expand_10d_jerk_v135_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(_s(x, 5), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal compression ratio jerk
def f41pps_f41_pricing_power_signal_std_compress_21d_jerk_v136_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(_s(x, 21), _s(x, 42))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal breakout ratio jerk
def f41pps_f41_pricing_power_signal_breakout_63d_jerk_v137_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x, _mx(x, 63).shift(1))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal drawdown distance jerk
def f41pps_f41_pricing_power_signal_drawdown_126d_jerk_v138_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = _safe_div(x - _mx(x, 126), _mx(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal recovery distance jerk
def f41pps_f41_pricing_power_signal_recovery_252d_jerk_v139_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _safe_div(x - _mn(x, 252), _mn(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal persistence share jerk
def f41pps_f41_pricing_power_signal_persist_share_504d_jerk_v140_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(_m(x.diff(21), 504), _m(x.diff(21).abs(), 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal shock frequency jerk
def f41pps_f41_pricing_power_signal_shock_freq_5d_jerk_v141_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _m(_z(x.diff(3), 5).abs(), 5)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal tail pressure jerk
def f41pps_f41_pricing_power_signal_tail_skew_10d_jerk_v142_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div(x.rolling(10, min_periods=2).skew(), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal median distance jerk
def f41pps_f41_pricing_power_signal_median_gap_21d_jerk_v143_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div(x - x.rolling(21, min_periods=2).median(), _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d pricing_power_signal vol scaled level jerk
def f41pps_f41_pricing_power_signal_vol_scaled_63d_jerk_v144_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 63)
    base = _safe_div(x, _s(x.diff(21), 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d pricing_power_signal liquidity weight jerk
def f41pps_f41_pricing_power_signal_abs_rank_weight_126d_jerk_v145_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 126)
    base = x * x.abs().rolling(126, min_periods=2).rank(pct=True)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d pricing_power_signal dollar weight jerk
def f41pps_f41_pricing_power_signal_abs_mean_weight_252d_jerk_v146_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 252)
    base = _z(x * _m(x.abs(), 21), 252)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d pricing_power_signal stability score jerk
def f41pps_f41_pricing_power_signal_stability_504d_jerk_v147_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 504)
    base = _safe_div(_m(x, 504), _m(x.diff(21).abs(), 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d pricing_power_signal decay balance jerk
def f41pps_f41_pricing_power_signal_ewm_balance_5d_jerk_v148_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 5)
    base = _safe_div(x.ewm(span=3, adjust=False).mean(), x.ewm(span=5, adjust=False).mean())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d pricing_power_signal accumulation ratio jerk
def f41pps_f41_pricing_power_signal_positive_share_10d_jerk_v149_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 10)
    base = _safe_div((x - _m(x, 10)).clip(lower=0).rolling(10, min_periods=2).sum(), (x - _m(x, 10)).abs().rolling(10, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d pricing_power_signal capitulation ratio jerk
def f41pps_f41_pricing_power_signal_negative_share_21d_jerk_v150_signal(revenue, netinc, fcf, assets):
    x = _f41_pricing_power_signal_primitive(revenue, netinc, fcf, assets, 21)
    base = _safe_div((_m(x, 21) - x).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f41pps_f41_pricing_power_signal_zlevel_5d_jerk_v001_signal,
    f41pps_f41_pricing_power_signal_mean_ratio_10d_jerk_v002_signal,
    f41pps_f41_pricing_power_signal_ma_spread_21d_jerk_v003_signal,
    f41pps_f41_pricing_power_signal_rank_pressure_63d_jerk_v004_signal,
    f41pps_f41_pricing_power_signal_trend_force_126d_jerk_v005_signal,
    f41pps_f41_pricing_power_signal_down_tail_252d_jerk_v006_signal,
    f41pps_f41_pricing_power_signal_up_tail_504d_jerk_v007_signal,
    f41pps_f41_pricing_power_signal_range_pos_5d_jerk_v008_signal,
    f41pps_f41_pricing_power_signal_revert_gap_10d_jerk_v009_signal,
    f41pps_f41_pricing_power_signal_std_expand_21d_jerk_v010_signal,
    f41pps_f41_pricing_power_signal_std_compress_63d_jerk_v011_signal,
    f41pps_f41_pricing_power_signal_breakout_126d_jerk_v012_signal,
    f41pps_f41_pricing_power_signal_drawdown_252d_jerk_v013_signal,
    f41pps_f41_pricing_power_signal_recovery_504d_jerk_v014_signal,
    f41pps_f41_pricing_power_signal_persist_share_5d_jerk_v015_signal,
    f41pps_f41_pricing_power_signal_shock_freq_10d_jerk_v016_signal,
    f41pps_f41_pricing_power_signal_tail_skew_21d_jerk_v017_signal,
    f41pps_f41_pricing_power_signal_median_gap_63d_jerk_v018_signal,
    f41pps_f41_pricing_power_signal_vol_scaled_126d_jerk_v019_signal,
    f41pps_f41_pricing_power_signal_abs_rank_weight_252d_jerk_v020_signal,
    f41pps_f41_pricing_power_signal_abs_mean_weight_504d_jerk_v021_signal,
    f41pps_f41_pricing_power_signal_stability_5d_jerk_v022_signal,
    f41pps_f41_pricing_power_signal_ewm_balance_10d_jerk_v023_signal,
    f41pps_f41_pricing_power_signal_positive_share_21d_jerk_v024_signal,
    f41pps_f41_pricing_power_signal_negative_share_63d_jerk_v025_signal,
    f41pps_f41_pricing_power_signal_zlevel_126d_jerk_v026_signal,
    f41pps_f41_pricing_power_signal_mean_ratio_252d_jerk_v027_signal,
    f41pps_f41_pricing_power_signal_ma_spread_504d_jerk_v028_signal,
    f41pps_f41_pricing_power_signal_rank_pressure_5d_jerk_v029_signal,
    f41pps_f41_pricing_power_signal_trend_force_10d_jerk_v030_signal,
    f41pps_f41_pricing_power_signal_down_tail_21d_jerk_v031_signal,
    f41pps_f41_pricing_power_signal_up_tail_63d_jerk_v032_signal,
    f41pps_f41_pricing_power_signal_range_pos_126d_jerk_v033_signal,
    f41pps_f41_pricing_power_signal_revert_gap_252d_jerk_v034_signal,
    f41pps_f41_pricing_power_signal_std_expand_504d_jerk_v035_signal,
    f41pps_f41_pricing_power_signal_std_compress_5d_jerk_v036_signal,
    f41pps_f41_pricing_power_signal_breakout_10d_jerk_v037_signal,
    f41pps_f41_pricing_power_signal_drawdown_21d_jerk_v038_signal,
    f41pps_f41_pricing_power_signal_recovery_63d_jerk_v039_signal,
    f41pps_f41_pricing_power_signal_persist_share_126d_jerk_v040_signal,
    f41pps_f41_pricing_power_signal_shock_freq_252d_jerk_v041_signal,
    f41pps_f41_pricing_power_signal_tail_skew_504d_jerk_v042_signal,
    f41pps_f41_pricing_power_signal_median_gap_5d_jerk_v043_signal,
    f41pps_f41_pricing_power_signal_vol_scaled_10d_jerk_v044_signal,
    f41pps_f41_pricing_power_signal_abs_rank_weight_21d_jerk_v045_signal,
    f41pps_f41_pricing_power_signal_abs_mean_weight_63d_jerk_v046_signal,
    f41pps_f41_pricing_power_signal_stability_126d_jerk_v047_signal,
    f41pps_f41_pricing_power_signal_ewm_balance_252d_jerk_v048_signal,
    f41pps_f41_pricing_power_signal_positive_share_504d_jerk_v049_signal,
    f41pps_f41_pricing_power_signal_negative_share_5d_jerk_v050_signal,
    f41pps_f41_pricing_power_signal_zlevel_10d_jerk_v051_signal,
    f41pps_f41_pricing_power_signal_mean_ratio_21d_jerk_v052_signal,
    f41pps_f41_pricing_power_signal_ma_spread_63d_jerk_v053_signal,
    f41pps_f41_pricing_power_signal_rank_pressure_126d_jerk_v054_signal,
    f41pps_f41_pricing_power_signal_trend_force_252d_jerk_v055_signal,
    f41pps_f41_pricing_power_signal_down_tail_504d_jerk_v056_signal,
    f41pps_f41_pricing_power_signal_up_tail_5d_jerk_v057_signal,
    f41pps_f41_pricing_power_signal_range_pos_10d_jerk_v058_signal,
    f41pps_f41_pricing_power_signal_revert_gap_21d_jerk_v059_signal,
    f41pps_f41_pricing_power_signal_std_expand_63d_jerk_v060_signal,
    f41pps_f41_pricing_power_signal_std_compress_126d_jerk_v061_signal,
    f41pps_f41_pricing_power_signal_breakout_252d_jerk_v062_signal,
    f41pps_f41_pricing_power_signal_drawdown_504d_jerk_v063_signal,
    f41pps_f41_pricing_power_signal_recovery_5d_jerk_v064_signal,
    f41pps_f41_pricing_power_signal_persist_share_10d_jerk_v065_signal,
    f41pps_f41_pricing_power_signal_shock_freq_21d_jerk_v066_signal,
    f41pps_f41_pricing_power_signal_tail_skew_63d_jerk_v067_signal,
    f41pps_f41_pricing_power_signal_median_gap_126d_jerk_v068_signal,
    f41pps_f41_pricing_power_signal_vol_scaled_252d_jerk_v069_signal,
    f41pps_f41_pricing_power_signal_abs_rank_weight_504d_jerk_v070_signal,
    f41pps_f41_pricing_power_signal_abs_mean_weight_5d_jerk_v071_signal,
    f41pps_f41_pricing_power_signal_stability_10d_jerk_v072_signal,
    f41pps_f41_pricing_power_signal_ewm_balance_21d_jerk_v073_signal,
    f41pps_f41_pricing_power_signal_positive_share_63d_jerk_v074_signal,
    f41pps_f41_pricing_power_signal_negative_share_126d_jerk_v075_signal,
    f41pps_f41_pricing_power_signal_zlevel_252d_jerk_v076_signal,
    f41pps_f41_pricing_power_signal_mean_ratio_504d_jerk_v077_signal,
    f41pps_f41_pricing_power_signal_ma_spread_5d_jerk_v078_signal,
    f41pps_f41_pricing_power_signal_rank_pressure_10d_jerk_v079_signal,
    f41pps_f41_pricing_power_signal_trend_force_21d_jerk_v080_signal,
    f41pps_f41_pricing_power_signal_down_tail_63d_jerk_v081_signal,
    f41pps_f41_pricing_power_signal_up_tail_126d_jerk_v082_signal,
    f41pps_f41_pricing_power_signal_range_pos_252d_jerk_v083_signal,
    f41pps_f41_pricing_power_signal_revert_gap_504d_jerk_v084_signal,
    f41pps_f41_pricing_power_signal_std_expand_5d_jerk_v085_signal,
    f41pps_f41_pricing_power_signal_std_compress_10d_jerk_v086_signal,
    f41pps_f41_pricing_power_signal_breakout_21d_jerk_v087_signal,
    f41pps_f41_pricing_power_signal_drawdown_63d_jerk_v088_signal,
    f41pps_f41_pricing_power_signal_recovery_126d_jerk_v089_signal,
    f41pps_f41_pricing_power_signal_persist_share_252d_jerk_v090_signal,
    f41pps_f41_pricing_power_signal_shock_freq_504d_jerk_v091_signal,
    f41pps_f41_pricing_power_signal_tail_skew_5d_jerk_v092_signal,
    f41pps_f41_pricing_power_signal_median_gap_10d_jerk_v093_signal,
    f41pps_f41_pricing_power_signal_vol_scaled_21d_jerk_v094_signal,
    f41pps_f41_pricing_power_signal_abs_rank_weight_63d_jerk_v095_signal,
    f41pps_f41_pricing_power_signal_abs_mean_weight_126d_jerk_v096_signal,
    f41pps_f41_pricing_power_signal_stability_252d_jerk_v097_signal,
    f41pps_f41_pricing_power_signal_ewm_balance_504d_jerk_v098_signal,
    f41pps_f41_pricing_power_signal_positive_share_5d_jerk_v099_signal,
    f41pps_f41_pricing_power_signal_negative_share_10d_jerk_v100_signal,
    f41pps_f41_pricing_power_signal_zlevel_21d_jerk_v101_signal,
    f41pps_f41_pricing_power_signal_mean_ratio_63d_jerk_v102_signal,
    f41pps_f41_pricing_power_signal_ma_spread_126d_jerk_v103_signal,
    f41pps_f41_pricing_power_signal_rank_pressure_252d_jerk_v104_signal,
    f41pps_f41_pricing_power_signal_trend_force_504d_jerk_v105_signal,
    f41pps_f41_pricing_power_signal_down_tail_5d_jerk_v106_signal,
    f41pps_f41_pricing_power_signal_up_tail_10d_jerk_v107_signal,
    f41pps_f41_pricing_power_signal_range_pos_21d_jerk_v108_signal,
    f41pps_f41_pricing_power_signal_revert_gap_63d_jerk_v109_signal,
    f41pps_f41_pricing_power_signal_std_expand_126d_jerk_v110_signal,
    f41pps_f41_pricing_power_signal_std_compress_252d_jerk_v111_signal,
    f41pps_f41_pricing_power_signal_breakout_504d_jerk_v112_signal,
    f41pps_f41_pricing_power_signal_drawdown_5d_jerk_v113_signal,
    f41pps_f41_pricing_power_signal_recovery_10d_jerk_v114_signal,
    f41pps_f41_pricing_power_signal_persist_share_21d_jerk_v115_signal,
    f41pps_f41_pricing_power_signal_shock_freq_63d_jerk_v116_signal,
    f41pps_f41_pricing_power_signal_tail_skew_126d_jerk_v117_signal,
    f41pps_f41_pricing_power_signal_median_gap_252d_jerk_v118_signal,
    f41pps_f41_pricing_power_signal_vol_scaled_504d_jerk_v119_signal,
    f41pps_f41_pricing_power_signal_abs_rank_weight_5d_jerk_v120_signal,
    f41pps_f41_pricing_power_signal_abs_mean_weight_10d_jerk_v121_signal,
    f41pps_f41_pricing_power_signal_stability_21d_jerk_v122_signal,
    f41pps_f41_pricing_power_signal_ewm_balance_63d_jerk_v123_signal,
    f41pps_f41_pricing_power_signal_positive_share_126d_jerk_v124_signal,
    f41pps_f41_pricing_power_signal_negative_share_252d_jerk_v125_signal,
    f41pps_f41_pricing_power_signal_zlevel_504d_jerk_v126_signal,
    f41pps_f41_pricing_power_signal_mean_ratio_5d_jerk_v127_signal,
    f41pps_f41_pricing_power_signal_ma_spread_10d_jerk_v128_signal,
    f41pps_f41_pricing_power_signal_rank_pressure_21d_jerk_v129_signal,
    f41pps_f41_pricing_power_signal_trend_force_63d_jerk_v130_signal,
    f41pps_f41_pricing_power_signal_down_tail_126d_jerk_v131_signal,
    f41pps_f41_pricing_power_signal_up_tail_252d_jerk_v132_signal,
    f41pps_f41_pricing_power_signal_range_pos_504d_jerk_v133_signal,
    f41pps_f41_pricing_power_signal_revert_gap_5d_jerk_v134_signal,
    f41pps_f41_pricing_power_signal_std_expand_10d_jerk_v135_signal,
    f41pps_f41_pricing_power_signal_std_compress_21d_jerk_v136_signal,
    f41pps_f41_pricing_power_signal_breakout_63d_jerk_v137_signal,
    f41pps_f41_pricing_power_signal_drawdown_126d_jerk_v138_signal,
    f41pps_f41_pricing_power_signal_recovery_252d_jerk_v139_signal,
    f41pps_f41_pricing_power_signal_persist_share_504d_jerk_v140_signal,
    f41pps_f41_pricing_power_signal_shock_freq_5d_jerk_v141_signal,
    f41pps_f41_pricing_power_signal_tail_skew_10d_jerk_v142_signal,
    f41pps_f41_pricing_power_signal_median_gap_21d_jerk_v143_signal,
    f41pps_f41_pricing_power_signal_vol_scaled_63d_jerk_v144_signal,
    f41pps_f41_pricing_power_signal_abs_rank_weight_126d_jerk_v145_signal,
    f41pps_f41_pricing_power_signal_abs_mean_weight_252d_jerk_v146_signal,
    f41pps_f41_pricing_power_signal_stability_504d_jerk_v147_signal,
    f41pps_f41_pricing_power_signal_ewm_balance_5d_jerk_v148_signal,
    f41pps_f41_pricing_power_signal_positive_share_10d_jerk_v149_signal,
    f41pps_f41_pricing_power_signal_negative_share_21d_jerk_v150_signal,
]
REGISTRY = {fn.__name__: {"inputs": ['revenue', 'netinc', 'fcf', 'assets'], "func": fn} for fn in _FEATURES}


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    idx = pd.RangeIndex(n)
    revenue = pd.Series(1000.0 + np.cumsum(np.random.normal(5.0, 30.0, n)), index=idx).abs() + 10.0
    netinc = pd.Series(80.0 + np.cumsum(np.random.normal(0.5, 8.0, n)), index=idx)
    fcf = pd.Series(60.0 + np.cumsum(np.random.normal(0.4, 7.0, n)), index=idx)
    assets = pd.Series(2500.0 + np.cumsum(np.random.normal(8.0, 20.0, n)), index=idx).abs() + 10.0
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
        assert '_f41_pricing_power_signal_primitive' in inspect.getsource(func)
    assert valid_nan >= int(len(REGISTRY) * 0.80)


F41_PRICING_POWER_SIGNAL_REGISTRY_JERK = REGISTRY
