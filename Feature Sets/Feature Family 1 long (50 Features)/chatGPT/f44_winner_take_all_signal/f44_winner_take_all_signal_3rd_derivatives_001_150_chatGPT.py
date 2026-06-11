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


def _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, w):
    owner_value = _m(sf3b_value, w)
    owner_shares = _m(sf3a_shares, w)
    return _z(_safe_div(ev + owner_value, marketcap) + _z(owner_shares, w), w)


# 5d winner_take_all_signal level zscore jerk
def f44wta_f44_winner_take_all_signal_zlevel_5d_jerk_v001_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _z(x, 5)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal level to mean jerk
def f44wta_f44_winner_take_all_signal_mean_ratio_10d_jerk_v002_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x, _m(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal short minus long jerk
def f44wta_f44_winner_take_all_signal_ma_spread_21d_jerk_v003_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _spread(_m(x, 5), _m(x, 42))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal ranked pressure jerk
def f44wta_f44_winner_take_all_signal_rank_pressure_63d_jerk_v004_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x - _mn(x, 63), _mx(x, 63) - _mn(x, 63)) + _z(x, 21) / np.sqrt(63)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal trend strength jerk
def f44wta_f44_winner_take_all_signal_trend_force_126d_jerk_v005_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x.diff(21), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal downside gap jerk
def f44wta_f44_winner_take_all_signal_down_tail_252d_jerk_v006_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x.rolling(252, min_periods=2).quantile(0.20) - x, _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal upside gap jerk
def f44wta_f44_winner_take_all_signal_up_tail_504d_jerk_v007_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x - x.rolling(504, min_periods=2).quantile(0.80), _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal range position jerk
def f44wta_f44_winner_take_all_signal_range_pos_5d_jerk_v008_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal mean reversion jerk
def f44wta_f44_winner_take_all_signal_revert_gap_10d_jerk_v009_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(_m(x, 5) - x, _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal expanding pressure jerk
def f44wta_f44_winner_take_all_signal_std_expand_21d_jerk_v010_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(_s(x, 5), _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal compression ratio jerk
def f44wta_f44_winner_take_all_signal_std_compress_63d_jerk_v011_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(_s(x, 63), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal breakout ratio jerk
def f44wta_f44_winner_take_all_signal_breakout_126d_jerk_v012_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x, _mx(x, 126).shift(1))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal drawdown distance jerk
def f44wta_f44_winner_take_all_signal_drawdown_252d_jerk_v013_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x - _mx(x, 252), _mx(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal recovery distance jerk
def f44wta_f44_winner_take_all_signal_recovery_504d_jerk_v014_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x - _mn(x, 504), _mn(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal persistence share jerk
def f44wta_f44_winner_take_all_signal_persist_share_5d_jerk_v015_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(_m(x.diff(3), 5), _m(x.diff(3).abs(), 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal shock frequency jerk
def f44wta_f44_winner_take_all_signal_shock_freq_10d_jerk_v016_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _m(_z(x.diff(5), 10).abs(), 10)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal tail pressure jerk
def f44wta_f44_winner_take_all_signal_tail_skew_21d_jerk_v017_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x.rolling(21, min_periods=2).skew(), _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal median distance jerk
def f44wta_f44_winner_take_all_signal_median_gap_63d_jerk_v018_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x - x.rolling(63, min_periods=2).median(), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal vol scaled level jerk
def f44wta_f44_winner_take_all_signal_vol_scaled_126d_jerk_v019_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x, _s(x.diff(21), 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal liquidity weight jerk
def f44wta_f44_winner_take_all_signal_abs_rank_weight_252d_jerk_v020_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = x * x.abs().rolling(252, min_periods=2).rank(pct=True)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal dollar weight jerk
def f44wta_f44_winner_take_all_signal_abs_mean_weight_504d_jerk_v021_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _z(x * _m(x.abs(), 21), 504)
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal stability score jerk
def f44wta_f44_winner_take_all_signal_stability_5d_jerk_v022_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(_m(x, 5), _m(x.diff(3).abs(), 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal decay balance jerk
def f44wta_f44_winner_take_all_signal_ewm_balance_10d_jerk_v023_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=10, adjust=False).mean())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal accumulation ratio jerk
def f44wta_f44_winner_take_all_signal_positive_share_21d_jerk_v024_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div((x - _m(x, 21)).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal capitulation ratio jerk
def f44wta_f44_winner_take_all_signal_negative_share_63d_jerk_v025_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div((_m(x, 63) - x).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal level zscore jerk
def f44wta_f44_winner_take_all_signal_zlevel_126d_jerk_v026_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _z(x, 126)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal level to mean jerk
def f44wta_f44_winner_take_all_signal_mean_ratio_252d_jerk_v027_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x, _m(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal short minus long jerk
def f44wta_f44_winner_take_all_signal_ma_spread_504d_jerk_v028_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _spread(_m(x, 21), _m(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal ranked pressure jerk
def f44wta_f44_winner_take_all_signal_rank_pressure_5d_jerk_v029_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5)) + _z(x, 3) / np.sqrt(5)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal trend strength jerk
def f44wta_f44_winner_take_all_signal_trend_force_10d_jerk_v030_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x.diff(5), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal downside gap jerk
def f44wta_f44_winner_take_all_signal_down_tail_21d_jerk_v031_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x.rolling(21, min_periods=2).quantile(0.20) - x, _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal upside gap jerk
def f44wta_f44_winner_take_all_signal_up_tail_63d_jerk_v032_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x - x.rolling(63, min_periods=2).quantile(0.80), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal range position jerk
def f44wta_f44_winner_take_all_signal_range_pos_126d_jerk_v033_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal mean reversion jerk
def f44wta_f44_winner_take_all_signal_revert_gap_252d_jerk_v034_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(_m(x, 21) - x, _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal expanding pressure jerk
def f44wta_f44_winner_take_all_signal_std_expand_504d_jerk_v035_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(_s(x, 21), _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal compression ratio jerk
def f44wta_f44_winner_take_all_signal_std_compress_5d_jerk_v036_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(_s(x, 5), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal breakout ratio jerk
def f44wta_f44_winner_take_all_signal_breakout_10d_jerk_v037_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x, _mx(x, 10).shift(1))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal drawdown distance jerk
def f44wta_f44_winner_take_all_signal_drawdown_21d_jerk_v038_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x - _mx(x, 21), _mx(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal recovery distance jerk
def f44wta_f44_winner_take_all_signal_recovery_63d_jerk_v039_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x - _mn(x, 63), _mn(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal persistence share jerk
def f44wta_f44_winner_take_all_signal_persist_share_126d_jerk_v040_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(_m(x.diff(21), 126), _m(x.diff(21).abs(), 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal shock frequency jerk
def f44wta_f44_winner_take_all_signal_shock_freq_252d_jerk_v041_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _m(_z(x.diff(21), 252).abs(), 252)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal tail pressure jerk
def f44wta_f44_winner_take_all_signal_tail_skew_504d_jerk_v042_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x.rolling(504, min_periods=2).skew(), _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal median distance jerk
def f44wta_f44_winner_take_all_signal_median_gap_5d_jerk_v043_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x - x.rolling(5, min_periods=2).median(), _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal vol scaled level jerk
def f44wta_f44_winner_take_all_signal_vol_scaled_10d_jerk_v044_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x, _s(x.diff(5), 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal liquidity weight jerk
def f44wta_f44_winner_take_all_signal_abs_rank_weight_21d_jerk_v045_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = x * x.abs().rolling(21, min_periods=2).rank(pct=True)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal dollar weight jerk
def f44wta_f44_winner_take_all_signal_abs_mean_weight_63d_jerk_v046_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _z(x * _m(x.abs(), 21), 63)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal stability score jerk
def f44wta_f44_winner_take_all_signal_stability_126d_jerk_v047_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(_m(x, 126), _m(x.diff(21).abs(), 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal decay balance jerk
def f44wta_f44_winner_take_all_signal_ewm_balance_252d_jerk_v048_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=252, adjust=False).mean())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal accumulation ratio jerk
def f44wta_f44_winner_take_all_signal_positive_share_504d_jerk_v049_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div((x - _m(x, 504)).clip(lower=0).rolling(504, min_periods=2).sum(), (x - _m(x, 504)).abs().rolling(504, min_periods=2).sum())
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal capitulation ratio jerk
def f44wta_f44_winner_take_all_signal_negative_share_5d_jerk_v050_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div((_m(x, 5) - x).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal level zscore jerk
def f44wta_f44_winner_take_all_signal_zlevel_10d_jerk_v051_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _z(x, 10)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal level to mean jerk
def f44wta_f44_winner_take_all_signal_mean_ratio_21d_jerk_v052_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x, _m(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal short minus long jerk
def f44wta_f44_winner_take_all_signal_ma_spread_63d_jerk_v053_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _spread(_m(x, 21), _m(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal ranked pressure jerk
def f44wta_f44_winner_take_all_signal_rank_pressure_126d_jerk_v054_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126)) + _z(x, 21) / np.sqrt(126)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal trend strength jerk
def f44wta_f44_winner_take_all_signal_trend_force_252d_jerk_v055_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x.diff(21), _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal downside gap jerk
def f44wta_f44_winner_take_all_signal_down_tail_504d_jerk_v056_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x.rolling(504, min_periods=2).quantile(0.20) - x, _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal upside gap jerk
def f44wta_f44_winner_take_all_signal_up_tail_5d_jerk_v057_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x - x.rolling(5, min_periods=2).quantile(0.80), _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal range position jerk
def f44wta_f44_winner_take_all_signal_range_pos_10d_jerk_v058_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal mean reversion jerk
def f44wta_f44_winner_take_all_signal_revert_gap_21d_jerk_v059_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(_m(x, 5) - x, _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal expanding pressure jerk
def f44wta_f44_winner_take_all_signal_std_expand_63d_jerk_v060_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(_s(x, 21), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal compression ratio jerk
def f44wta_f44_winner_take_all_signal_std_compress_126d_jerk_v061_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(_s(x, 126), _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal breakout ratio jerk
def f44wta_f44_winner_take_all_signal_breakout_252d_jerk_v062_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x, _mx(x, 252).shift(1))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal drawdown distance jerk
def f44wta_f44_winner_take_all_signal_drawdown_504d_jerk_v063_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x - _mx(x, 504), _mx(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal recovery distance jerk
def f44wta_f44_winner_take_all_signal_recovery_5d_jerk_v064_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x - _mn(x, 5), _mn(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal persistence share jerk
def f44wta_f44_winner_take_all_signal_persist_share_10d_jerk_v065_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(_m(x.diff(5), 10), _m(x.diff(5).abs(), 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal shock frequency jerk
def f44wta_f44_winner_take_all_signal_shock_freq_21d_jerk_v066_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _m(_z(x.diff(5), 21).abs(), 21)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal tail pressure jerk
def f44wta_f44_winner_take_all_signal_tail_skew_63d_jerk_v067_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x.rolling(63, min_periods=2).skew(), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal median distance jerk
def f44wta_f44_winner_take_all_signal_median_gap_126d_jerk_v068_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x - x.rolling(126, min_periods=2).median(), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal vol scaled level jerk
def f44wta_f44_winner_take_all_signal_vol_scaled_252d_jerk_v069_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x, _s(x.diff(21), 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal liquidity weight jerk
def f44wta_f44_winner_take_all_signal_abs_rank_weight_504d_jerk_v070_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = x * x.abs().rolling(504, min_periods=2).rank(pct=True)
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal dollar weight jerk
def f44wta_f44_winner_take_all_signal_abs_mean_weight_5d_jerk_v071_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _z(x * _m(x.abs(), 3), 5)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal stability score jerk
def f44wta_f44_winner_take_all_signal_stability_10d_jerk_v072_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(_m(x, 10), _m(x.diff(5).abs(), 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal decay balance jerk
def f44wta_f44_winner_take_all_signal_ewm_balance_21d_jerk_v073_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=21, adjust=False).mean())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal accumulation ratio jerk
def f44wta_f44_winner_take_all_signal_positive_share_63d_jerk_v074_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div((x - _m(x, 63)).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal capitulation ratio jerk
def f44wta_f44_winner_take_all_signal_negative_share_126d_jerk_v075_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div((_m(x, 126) - x).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal level zscore jerk
def f44wta_f44_winner_take_all_signal_zlevel_252d_jerk_v076_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _z(x, 252)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal level to mean jerk
def f44wta_f44_winner_take_all_signal_mean_ratio_504d_jerk_v077_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x, _m(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal short minus long jerk
def f44wta_f44_winner_take_all_signal_ma_spread_5d_jerk_v078_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _spread(_m(x, 3), _m(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal ranked pressure jerk
def f44wta_f44_winner_take_all_signal_rank_pressure_10d_jerk_v079_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10)) + _z(x, 5) / np.sqrt(10)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal trend strength jerk
def f44wta_f44_winner_take_all_signal_trend_force_21d_jerk_v080_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x.diff(5), _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal downside gap jerk
def f44wta_f44_winner_take_all_signal_down_tail_63d_jerk_v081_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x.rolling(63, min_periods=2).quantile(0.20) - x, _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal upside gap jerk
def f44wta_f44_winner_take_all_signal_up_tail_126d_jerk_v082_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x - x.rolling(126, min_periods=2).quantile(0.80), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal range position jerk
def f44wta_f44_winner_take_all_signal_range_pos_252d_jerk_v083_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x - _mn(x, 252), _mx(x, 252) - _mn(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal mean reversion jerk
def f44wta_f44_winner_take_all_signal_revert_gap_504d_jerk_v084_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(_m(x, 21) - x, _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal expanding pressure jerk
def f44wta_f44_winner_take_all_signal_std_expand_5d_jerk_v085_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(_s(x, 3), _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal compression ratio jerk
def f44wta_f44_winner_take_all_signal_std_compress_10d_jerk_v086_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(_s(x, 10), _s(x, 20))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal breakout ratio jerk
def f44wta_f44_winner_take_all_signal_breakout_21d_jerk_v087_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x, _mx(x, 21).shift(1))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal drawdown distance jerk
def f44wta_f44_winner_take_all_signal_drawdown_63d_jerk_v088_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x - _mx(x, 63), _mx(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal recovery distance jerk
def f44wta_f44_winner_take_all_signal_recovery_126d_jerk_v089_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x - _mn(x, 126), _mn(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal persistence share jerk
def f44wta_f44_winner_take_all_signal_persist_share_252d_jerk_v090_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(_m(x.diff(21), 252), _m(x.diff(21).abs(), 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal shock frequency jerk
def f44wta_f44_winner_take_all_signal_shock_freq_504d_jerk_v091_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _m(_z(x.diff(21), 504).abs(), 504)
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal tail pressure jerk
def f44wta_f44_winner_take_all_signal_tail_skew_5d_jerk_v092_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x.rolling(5, min_periods=2).skew(), _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal median distance jerk
def f44wta_f44_winner_take_all_signal_median_gap_10d_jerk_v093_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x - x.rolling(10, min_periods=2).median(), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal vol scaled level jerk
def f44wta_f44_winner_take_all_signal_vol_scaled_21d_jerk_v094_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x, _s(x.diff(5), 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal liquidity weight jerk
def f44wta_f44_winner_take_all_signal_abs_rank_weight_63d_jerk_v095_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = x * x.abs().rolling(63, min_periods=2).rank(pct=True)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal dollar weight jerk
def f44wta_f44_winner_take_all_signal_abs_mean_weight_126d_jerk_v096_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _z(x * _m(x.abs(), 21), 126)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal stability score jerk
def f44wta_f44_winner_take_all_signal_stability_252d_jerk_v097_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(_m(x, 252), _m(x.diff(21).abs(), 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal decay balance jerk
def f44wta_f44_winner_take_all_signal_ewm_balance_504d_jerk_v098_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=504, adjust=False).mean())
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal accumulation ratio jerk
def f44wta_f44_winner_take_all_signal_positive_share_5d_jerk_v099_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div((x - _m(x, 5)).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal capitulation ratio jerk
def f44wta_f44_winner_take_all_signal_negative_share_10d_jerk_v100_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div((_m(x, 10) - x).clip(lower=0).rolling(10, min_periods=2).sum(), (x - _m(x, 10)).abs().rolling(10, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal level zscore jerk
def f44wta_f44_winner_take_all_signal_zlevel_21d_jerk_v101_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _z(x, 21)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal level to mean jerk
def f44wta_f44_winner_take_all_signal_mean_ratio_63d_jerk_v102_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x, _m(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal short minus long jerk
def f44wta_f44_winner_take_all_signal_ma_spread_126d_jerk_v103_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _spread(_m(x, 21), _m(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal ranked pressure jerk
def f44wta_f44_winner_take_all_signal_rank_pressure_252d_jerk_v104_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x - _mn(x, 252), _mx(x, 252) - _mn(x, 252)) + _z(x, 21) / np.sqrt(252)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal trend strength jerk
def f44wta_f44_winner_take_all_signal_trend_force_504d_jerk_v105_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x.diff(21), _s(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal downside gap jerk
def f44wta_f44_winner_take_all_signal_down_tail_5d_jerk_v106_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x.rolling(5, min_periods=2).quantile(0.20) - x, _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal upside gap jerk
def f44wta_f44_winner_take_all_signal_up_tail_10d_jerk_v107_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x - x.rolling(10, min_periods=2).quantile(0.80), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal range position jerk
def f44wta_f44_winner_take_all_signal_range_pos_21d_jerk_v108_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x - _mn(x, 21), _mx(x, 21) - _mn(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal mean reversion jerk
def f44wta_f44_winner_take_all_signal_revert_gap_63d_jerk_v109_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(_m(x, 21) - x, _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal expanding pressure jerk
def f44wta_f44_winner_take_all_signal_std_expand_126d_jerk_v110_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(_s(x, 21), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal compression ratio jerk
def f44wta_f44_winner_take_all_signal_std_compress_252d_jerk_v111_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(_s(x, 252), _s(x, 504))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal breakout ratio jerk
def f44wta_f44_winner_take_all_signal_breakout_504d_jerk_v112_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x, _mx(x, 504).shift(1))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal drawdown distance jerk
def f44wta_f44_winner_take_all_signal_drawdown_5d_jerk_v113_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x - _mx(x, 5), _mx(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal recovery distance jerk
def f44wta_f44_winner_take_all_signal_recovery_10d_jerk_v114_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x - _mn(x, 10), _mn(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal persistence share jerk
def f44wta_f44_winner_take_all_signal_persist_share_21d_jerk_v115_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(_m(x.diff(5), 21), _m(x.diff(5).abs(), 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal shock frequency jerk
def f44wta_f44_winner_take_all_signal_shock_freq_63d_jerk_v116_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _m(_z(x.diff(21), 63).abs(), 63)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal tail pressure jerk
def f44wta_f44_winner_take_all_signal_tail_skew_126d_jerk_v117_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x.rolling(126, min_periods=2).skew(), _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal median distance jerk
def f44wta_f44_winner_take_all_signal_median_gap_252d_jerk_v118_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x - x.rolling(252, min_periods=2).median(), _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal vol scaled level jerk
def f44wta_f44_winner_take_all_signal_vol_scaled_504d_jerk_v119_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x, _s(x.diff(21), 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal liquidity weight jerk
def f44wta_f44_winner_take_all_signal_abs_rank_weight_5d_jerk_v120_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = x * x.abs().rolling(5, min_periods=2).rank(pct=True)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal dollar weight jerk
def f44wta_f44_winner_take_all_signal_abs_mean_weight_10d_jerk_v121_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _z(x * _m(x.abs(), 5), 10)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal stability score jerk
def f44wta_f44_winner_take_all_signal_stability_21d_jerk_v122_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(_m(x, 21), _m(x.diff(5).abs(), 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal decay balance jerk
def f44wta_f44_winner_take_all_signal_ewm_balance_63d_jerk_v123_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=63, adjust=False).mean())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal accumulation ratio jerk
def f44wta_f44_winner_take_all_signal_positive_share_126d_jerk_v124_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div((x - _m(x, 126)).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal capitulation ratio jerk
def f44wta_f44_winner_take_all_signal_negative_share_252d_jerk_v125_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div((_m(x, 252) - x).clip(lower=0).rolling(252, min_periods=2).sum(), (x - _m(x, 252)).abs().rolling(252, min_periods=2).sum())
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal level zscore jerk
def f44wta_f44_winner_take_all_signal_zlevel_504d_jerk_v126_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _z(x, 504)
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal level to mean jerk
def f44wta_f44_winner_take_all_signal_mean_ratio_5d_jerk_v127_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x, _m(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal short minus long jerk
def f44wta_f44_winner_take_all_signal_ma_spread_10d_jerk_v128_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _spread(_m(x, 5), _m(x, 20))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal ranked pressure jerk
def f44wta_f44_winner_take_all_signal_rank_pressure_21d_jerk_v129_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x - _mn(x, 21), _mx(x, 21) - _mn(x, 21)) + _z(x, 5) / np.sqrt(21)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal trend strength jerk
def f44wta_f44_winner_take_all_signal_trend_force_63d_jerk_v130_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x.diff(21), _s(x, 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal downside gap jerk
def f44wta_f44_winner_take_all_signal_down_tail_126d_jerk_v131_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x.rolling(126, min_periods=2).quantile(0.20) - x, _s(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal upside gap jerk
def f44wta_f44_winner_take_all_signal_up_tail_252d_jerk_v132_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x - x.rolling(252, min_periods=2).quantile(0.80), _s(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal range position jerk
def f44wta_f44_winner_take_all_signal_range_pos_504d_jerk_v133_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(x - _mn(x, 504), _mx(x, 504) - _mn(x, 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal mean reversion jerk
def f44wta_f44_winner_take_all_signal_revert_gap_5d_jerk_v134_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(_m(x, 3) - x, _s(x, 5))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal expanding pressure jerk
def f44wta_f44_winner_take_all_signal_std_expand_10d_jerk_v135_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(_s(x, 5), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal compression ratio jerk
def f44wta_f44_winner_take_all_signal_std_compress_21d_jerk_v136_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(_s(x, 21), _s(x, 42))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal breakout ratio jerk
def f44wta_f44_winner_take_all_signal_breakout_63d_jerk_v137_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x, _mx(x, 63).shift(1))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal drawdown distance jerk
def f44wta_f44_winner_take_all_signal_drawdown_126d_jerk_v138_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = _safe_div(x - _mx(x, 126), _mx(x, 126))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal recovery distance jerk
def f44wta_f44_winner_take_all_signal_recovery_252d_jerk_v139_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _safe_div(x - _mn(x, 252), _mn(x, 252))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal persistence share jerk
def f44wta_f44_winner_take_all_signal_persist_share_504d_jerk_v140_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(_m(x.diff(21), 504), _m(x.diff(21).abs(), 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal shock frequency jerk
def f44wta_f44_winner_take_all_signal_shock_freq_5d_jerk_v141_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _m(_z(x.diff(3), 5).abs(), 5)
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal tail pressure jerk
def f44wta_f44_winner_take_all_signal_tail_skew_10d_jerk_v142_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div(x.rolling(10, min_periods=2).skew(), _s(x, 10))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal median distance jerk
def f44wta_f44_winner_take_all_signal_median_gap_21d_jerk_v143_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div(x - x.rolling(21, min_periods=2).median(), _s(x, 21))
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d winner_take_all_signal vol scaled level jerk
def f44wta_f44_winner_take_all_signal_vol_scaled_63d_jerk_v144_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    base = _safe_div(x, _s(x.diff(21), 63))
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d winner_take_all_signal liquidity weight jerk
def f44wta_f44_winner_take_all_signal_abs_rank_weight_126d_jerk_v145_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    base = x * x.abs().rolling(126, min_periods=2).rank(pct=True)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d winner_take_all_signal dollar weight jerk
def f44wta_f44_winner_take_all_signal_abs_mean_weight_252d_jerk_v146_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    base = _z(x * _m(x.abs(), 21), 252)
    result = _roc(base, 21).diff(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d winner_take_all_signal stability score jerk
def f44wta_f44_winner_take_all_signal_stability_504d_jerk_v147_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    base = _safe_div(_m(x, 504), _m(x.diff(21).abs(), 504))
    result = _roc(base, 63).diff(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d winner_take_all_signal decay balance jerk
def f44wta_f44_winner_take_all_signal_ewm_balance_5d_jerk_v148_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    base = _safe_div(x.ewm(span=3, adjust=False).mean(), x.ewm(span=5, adjust=False).mean())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d winner_take_all_signal accumulation ratio jerk
def f44wta_f44_winner_take_all_signal_positive_share_10d_jerk_v149_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    base = _safe_div((x - _m(x, 10)).clip(lower=0).rolling(10, min_periods=2).sum(), (x - _m(x, 10)).abs().rolling(10, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d winner_take_all_signal capitulation ratio jerk
def f44wta_f44_winner_take_all_signal_negative_share_21d_jerk_v150_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f44_winner_take_all_signal_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    base = _safe_div((_m(x, 21) - x).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    result = _roc(base, 5).diff(5)
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f44wta_f44_winner_take_all_signal_zlevel_5d_jerk_v001_signal,
    f44wta_f44_winner_take_all_signal_mean_ratio_10d_jerk_v002_signal,
    f44wta_f44_winner_take_all_signal_ma_spread_21d_jerk_v003_signal,
    f44wta_f44_winner_take_all_signal_rank_pressure_63d_jerk_v004_signal,
    f44wta_f44_winner_take_all_signal_trend_force_126d_jerk_v005_signal,
    f44wta_f44_winner_take_all_signal_down_tail_252d_jerk_v006_signal,
    f44wta_f44_winner_take_all_signal_up_tail_504d_jerk_v007_signal,
    f44wta_f44_winner_take_all_signal_range_pos_5d_jerk_v008_signal,
    f44wta_f44_winner_take_all_signal_revert_gap_10d_jerk_v009_signal,
    f44wta_f44_winner_take_all_signal_std_expand_21d_jerk_v010_signal,
    f44wta_f44_winner_take_all_signal_std_compress_63d_jerk_v011_signal,
    f44wta_f44_winner_take_all_signal_breakout_126d_jerk_v012_signal,
    f44wta_f44_winner_take_all_signal_drawdown_252d_jerk_v013_signal,
    f44wta_f44_winner_take_all_signal_recovery_504d_jerk_v014_signal,
    f44wta_f44_winner_take_all_signal_persist_share_5d_jerk_v015_signal,
    f44wta_f44_winner_take_all_signal_shock_freq_10d_jerk_v016_signal,
    f44wta_f44_winner_take_all_signal_tail_skew_21d_jerk_v017_signal,
    f44wta_f44_winner_take_all_signal_median_gap_63d_jerk_v018_signal,
    f44wta_f44_winner_take_all_signal_vol_scaled_126d_jerk_v019_signal,
    f44wta_f44_winner_take_all_signal_abs_rank_weight_252d_jerk_v020_signal,
    f44wta_f44_winner_take_all_signal_abs_mean_weight_504d_jerk_v021_signal,
    f44wta_f44_winner_take_all_signal_stability_5d_jerk_v022_signal,
    f44wta_f44_winner_take_all_signal_ewm_balance_10d_jerk_v023_signal,
    f44wta_f44_winner_take_all_signal_positive_share_21d_jerk_v024_signal,
    f44wta_f44_winner_take_all_signal_negative_share_63d_jerk_v025_signal,
    f44wta_f44_winner_take_all_signal_zlevel_126d_jerk_v026_signal,
    f44wta_f44_winner_take_all_signal_mean_ratio_252d_jerk_v027_signal,
    f44wta_f44_winner_take_all_signal_ma_spread_504d_jerk_v028_signal,
    f44wta_f44_winner_take_all_signal_rank_pressure_5d_jerk_v029_signal,
    f44wta_f44_winner_take_all_signal_trend_force_10d_jerk_v030_signal,
    f44wta_f44_winner_take_all_signal_down_tail_21d_jerk_v031_signal,
    f44wta_f44_winner_take_all_signal_up_tail_63d_jerk_v032_signal,
    f44wta_f44_winner_take_all_signal_range_pos_126d_jerk_v033_signal,
    f44wta_f44_winner_take_all_signal_revert_gap_252d_jerk_v034_signal,
    f44wta_f44_winner_take_all_signal_std_expand_504d_jerk_v035_signal,
    f44wta_f44_winner_take_all_signal_std_compress_5d_jerk_v036_signal,
    f44wta_f44_winner_take_all_signal_breakout_10d_jerk_v037_signal,
    f44wta_f44_winner_take_all_signal_drawdown_21d_jerk_v038_signal,
    f44wta_f44_winner_take_all_signal_recovery_63d_jerk_v039_signal,
    f44wta_f44_winner_take_all_signal_persist_share_126d_jerk_v040_signal,
    f44wta_f44_winner_take_all_signal_shock_freq_252d_jerk_v041_signal,
    f44wta_f44_winner_take_all_signal_tail_skew_504d_jerk_v042_signal,
    f44wta_f44_winner_take_all_signal_median_gap_5d_jerk_v043_signal,
    f44wta_f44_winner_take_all_signal_vol_scaled_10d_jerk_v044_signal,
    f44wta_f44_winner_take_all_signal_abs_rank_weight_21d_jerk_v045_signal,
    f44wta_f44_winner_take_all_signal_abs_mean_weight_63d_jerk_v046_signal,
    f44wta_f44_winner_take_all_signal_stability_126d_jerk_v047_signal,
    f44wta_f44_winner_take_all_signal_ewm_balance_252d_jerk_v048_signal,
    f44wta_f44_winner_take_all_signal_positive_share_504d_jerk_v049_signal,
    f44wta_f44_winner_take_all_signal_negative_share_5d_jerk_v050_signal,
    f44wta_f44_winner_take_all_signal_zlevel_10d_jerk_v051_signal,
    f44wta_f44_winner_take_all_signal_mean_ratio_21d_jerk_v052_signal,
    f44wta_f44_winner_take_all_signal_ma_spread_63d_jerk_v053_signal,
    f44wta_f44_winner_take_all_signal_rank_pressure_126d_jerk_v054_signal,
    f44wta_f44_winner_take_all_signal_trend_force_252d_jerk_v055_signal,
    f44wta_f44_winner_take_all_signal_down_tail_504d_jerk_v056_signal,
    f44wta_f44_winner_take_all_signal_up_tail_5d_jerk_v057_signal,
    f44wta_f44_winner_take_all_signal_range_pos_10d_jerk_v058_signal,
    f44wta_f44_winner_take_all_signal_revert_gap_21d_jerk_v059_signal,
    f44wta_f44_winner_take_all_signal_std_expand_63d_jerk_v060_signal,
    f44wta_f44_winner_take_all_signal_std_compress_126d_jerk_v061_signal,
    f44wta_f44_winner_take_all_signal_breakout_252d_jerk_v062_signal,
    f44wta_f44_winner_take_all_signal_drawdown_504d_jerk_v063_signal,
    f44wta_f44_winner_take_all_signal_recovery_5d_jerk_v064_signal,
    f44wta_f44_winner_take_all_signal_persist_share_10d_jerk_v065_signal,
    f44wta_f44_winner_take_all_signal_shock_freq_21d_jerk_v066_signal,
    f44wta_f44_winner_take_all_signal_tail_skew_63d_jerk_v067_signal,
    f44wta_f44_winner_take_all_signal_median_gap_126d_jerk_v068_signal,
    f44wta_f44_winner_take_all_signal_vol_scaled_252d_jerk_v069_signal,
    f44wta_f44_winner_take_all_signal_abs_rank_weight_504d_jerk_v070_signal,
    f44wta_f44_winner_take_all_signal_abs_mean_weight_5d_jerk_v071_signal,
    f44wta_f44_winner_take_all_signal_stability_10d_jerk_v072_signal,
    f44wta_f44_winner_take_all_signal_ewm_balance_21d_jerk_v073_signal,
    f44wta_f44_winner_take_all_signal_positive_share_63d_jerk_v074_signal,
    f44wta_f44_winner_take_all_signal_negative_share_126d_jerk_v075_signal,
    f44wta_f44_winner_take_all_signal_zlevel_252d_jerk_v076_signal,
    f44wta_f44_winner_take_all_signal_mean_ratio_504d_jerk_v077_signal,
    f44wta_f44_winner_take_all_signal_ma_spread_5d_jerk_v078_signal,
    f44wta_f44_winner_take_all_signal_rank_pressure_10d_jerk_v079_signal,
    f44wta_f44_winner_take_all_signal_trend_force_21d_jerk_v080_signal,
    f44wta_f44_winner_take_all_signal_down_tail_63d_jerk_v081_signal,
    f44wta_f44_winner_take_all_signal_up_tail_126d_jerk_v082_signal,
    f44wta_f44_winner_take_all_signal_range_pos_252d_jerk_v083_signal,
    f44wta_f44_winner_take_all_signal_revert_gap_504d_jerk_v084_signal,
    f44wta_f44_winner_take_all_signal_std_expand_5d_jerk_v085_signal,
    f44wta_f44_winner_take_all_signal_std_compress_10d_jerk_v086_signal,
    f44wta_f44_winner_take_all_signal_breakout_21d_jerk_v087_signal,
    f44wta_f44_winner_take_all_signal_drawdown_63d_jerk_v088_signal,
    f44wta_f44_winner_take_all_signal_recovery_126d_jerk_v089_signal,
    f44wta_f44_winner_take_all_signal_persist_share_252d_jerk_v090_signal,
    f44wta_f44_winner_take_all_signal_shock_freq_504d_jerk_v091_signal,
    f44wta_f44_winner_take_all_signal_tail_skew_5d_jerk_v092_signal,
    f44wta_f44_winner_take_all_signal_median_gap_10d_jerk_v093_signal,
    f44wta_f44_winner_take_all_signal_vol_scaled_21d_jerk_v094_signal,
    f44wta_f44_winner_take_all_signal_abs_rank_weight_63d_jerk_v095_signal,
    f44wta_f44_winner_take_all_signal_abs_mean_weight_126d_jerk_v096_signal,
    f44wta_f44_winner_take_all_signal_stability_252d_jerk_v097_signal,
    f44wta_f44_winner_take_all_signal_ewm_balance_504d_jerk_v098_signal,
    f44wta_f44_winner_take_all_signal_positive_share_5d_jerk_v099_signal,
    f44wta_f44_winner_take_all_signal_negative_share_10d_jerk_v100_signal,
    f44wta_f44_winner_take_all_signal_zlevel_21d_jerk_v101_signal,
    f44wta_f44_winner_take_all_signal_mean_ratio_63d_jerk_v102_signal,
    f44wta_f44_winner_take_all_signal_ma_spread_126d_jerk_v103_signal,
    f44wta_f44_winner_take_all_signal_rank_pressure_252d_jerk_v104_signal,
    f44wta_f44_winner_take_all_signal_trend_force_504d_jerk_v105_signal,
    f44wta_f44_winner_take_all_signal_down_tail_5d_jerk_v106_signal,
    f44wta_f44_winner_take_all_signal_up_tail_10d_jerk_v107_signal,
    f44wta_f44_winner_take_all_signal_range_pos_21d_jerk_v108_signal,
    f44wta_f44_winner_take_all_signal_revert_gap_63d_jerk_v109_signal,
    f44wta_f44_winner_take_all_signal_std_expand_126d_jerk_v110_signal,
    f44wta_f44_winner_take_all_signal_std_compress_252d_jerk_v111_signal,
    f44wta_f44_winner_take_all_signal_breakout_504d_jerk_v112_signal,
    f44wta_f44_winner_take_all_signal_drawdown_5d_jerk_v113_signal,
    f44wta_f44_winner_take_all_signal_recovery_10d_jerk_v114_signal,
    f44wta_f44_winner_take_all_signal_persist_share_21d_jerk_v115_signal,
    f44wta_f44_winner_take_all_signal_shock_freq_63d_jerk_v116_signal,
    f44wta_f44_winner_take_all_signal_tail_skew_126d_jerk_v117_signal,
    f44wta_f44_winner_take_all_signal_median_gap_252d_jerk_v118_signal,
    f44wta_f44_winner_take_all_signal_vol_scaled_504d_jerk_v119_signal,
    f44wta_f44_winner_take_all_signal_abs_rank_weight_5d_jerk_v120_signal,
    f44wta_f44_winner_take_all_signal_abs_mean_weight_10d_jerk_v121_signal,
    f44wta_f44_winner_take_all_signal_stability_21d_jerk_v122_signal,
    f44wta_f44_winner_take_all_signal_ewm_balance_63d_jerk_v123_signal,
    f44wta_f44_winner_take_all_signal_positive_share_126d_jerk_v124_signal,
    f44wta_f44_winner_take_all_signal_negative_share_252d_jerk_v125_signal,
    f44wta_f44_winner_take_all_signal_zlevel_504d_jerk_v126_signal,
    f44wta_f44_winner_take_all_signal_mean_ratio_5d_jerk_v127_signal,
    f44wta_f44_winner_take_all_signal_ma_spread_10d_jerk_v128_signal,
    f44wta_f44_winner_take_all_signal_rank_pressure_21d_jerk_v129_signal,
    f44wta_f44_winner_take_all_signal_trend_force_63d_jerk_v130_signal,
    f44wta_f44_winner_take_all_signal_down_tail_126d_jerk_v131_signal,
    f44wta_f44_winner_take_all_signal_up_tail_252d_jerk_v132_signal,
    f44wta_f44_winner_take_all_signal_range_pos_504d_jerk_v133_signal,
    f44wta_f44_winner_take_all_signal_revert_gap_5d_jerk_v134_signal,
    f44wta_f44_winner_take_all_signal_std_expand_10d_jerk_v135_signal,
    f44wta_f44_winner_take_all_signal_std_compress_21d_jerk_v136_signal,
    f44wta_f44_winner_take_all_signal_breakout_63d_jerk_v137_signal,
    f44wta_f44_winner_take_all_signal_drawdown_126d_jerk_v138_signal,
    f44wta_f44_winner_take_all_signal_recovery_252d_jerk_v139_signal,
    f44wta_f44_winner_take_all_signal_persist_share_504d_jerk_v140_signal,
    f44wta_f44_winner_take_all_signal_shock_freq_5d_jerk_v141_signal,
    f44wta_f44_winner_take_all_signal_tail_skew_10d_jerk_v142_signal,
    f44wta_f44_winner_take_all_signal_median_gap_21d_jerk_v143_signal,
    f44wta_f44_winner_take_all_signal_vol_scaled_63d_jerk_v144_signal,
    f44wta_f44_winner_take_all_signal_abs_rank_weight_126d_jerk_v145_signal,
    f44wta_f44_winner_take_all_signal_abs_mean_weight_252d_jerk_v146_signal,
    f44wta_f44_winner_take_all_signal_stability_504d_jerk_v147_signal,
    f44wta_f44_winner_take_all_signal_ewm_balance_5d_jerk_v148_signal,
    f44wta_f44_winner_take_all_signal_positive_share_10d_jerk_v149_signal,
    f44wta_f44_winner_take_all_signal_negative_share_21d_jerk_v150_signal,
]
REGISTRY = {fn.__name__: {"inputs": ['marketcap', 'ev', 'sf3a_shares', 'sf3b_value'], "func": fn} for fn in _FEATURES}


if __name__ == "__main__":
    np.random.seed(42)
    n = 800
    idx = pd.RangeIndex(n)
    marketcap = pd.Series(2000.0 + np.cumsum(np.random.normal(8.0, 50.0, n)), index=idx).abs() + 10.0
    ev = marketcap + pd.Series(np.random.normal(200.0, 25.0, n), index=idx)
    sf3a_shares = pd.Series(np.random.lognormal(8.0, 0.25, n), index=idx)
    sf3b_value = pd.Series(np.random.lognormal(13.0, 0.30, n), index=idx)
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
        assert '_f44_winner_take_all_signal_primitive' in inspect.getsource(func)
    assert valid_nan >= int(len(REGISTRY) * 0.80)


F44_WINNER_TAKE_ALL_SIGNAL_REGISTRY_JERK = REGISTRY
