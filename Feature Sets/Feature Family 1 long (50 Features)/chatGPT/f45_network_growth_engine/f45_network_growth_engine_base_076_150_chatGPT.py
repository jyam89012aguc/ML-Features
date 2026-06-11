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


def _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, w):
    owner_value = _m(sf3b_value, w)
    owner_shares = _m(sf3a_shares, w)
    return _z(_safe_div(ev + owner_value, marketcap) + _z(owner_shares, w), w)


# 252d network_growth_engine level zscore base
def f45nge_f45_network_growth_engine_zlevel_252d_base_v076_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _z(x, 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine level to mean base
def f45nge_f45_network_growth_engine_mean_ratio_504d_base_v077_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x, _m(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine short minus long base
def f45nge_f45_network_growth_engine_ma_spread_5d_base_v078_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _spread(_m(x, 3), _m(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine ranked pressure base
def f45nge_f45_network_growth_engine_rank_pressure_10d_base_v079_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10)) + _z(x, 5) / np.sqrt(10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine trend strength base
def f45nge_f45_network_growth_engine_trend_force_21d_base_v080_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x.diff(5), _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine downside gap base
def f45nge_f45_network_growth_engine_down_tail_63d_base_v081_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x.rolling(63, min_periods=2).quantile(0.20) - x, _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine upside gap base
def f45nge_f45_network_growth_engine_up_tail_126d_base_v082_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x - x.rolling(126, min_periods=2).quantile(0.80), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine range position base
def f45nge_f45_network_growth_engine_range_pos_252d_base_v083_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x - _mn(x, 252), _mx(x, 252) - _mn(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine mean reversion base
def f45nge_f45_network_growth_engine_revert_gap_504d_base_v084_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(_m(x, 21) - x, _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine expanding pressure base
def f45nge_f45_network_growth_engine_std_expand_5d_base_v085_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(_s(x, 3), _s(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine compression ratio base
def f45nge_f45_network_growth_engine_std_compress_10d_base_v086_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(_s(x, 10), _s(x, 20))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine breakout ratio base
def f45nge_f45_network_growth_engine_breakout_21d_base_v087_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x, _mx(x, 21).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine drawdown distance base
def f45nge_f45_network_growth_engine_drawdown_63d_base_v088_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x - _mx(x, 63), _mx(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine recovery distance base
def f45nge_f45_network_growth_engine_recovery_126d_base_v089_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x - _mn(x, 126), _mn(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine persistence share base
def f45nge_f45_network_growth_engine_persist_share_252d_base_v090_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(_m(x.diff(21), 252), _m(x.diff(21).abs(), 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine shock frequency base
def f45nge_f45_network_growth_engine_shock_freq_504d_base_v091_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _m(_z(x.diff(21), 504).abs(), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine tail pressure base
def f45nge_f45_network_growth_engine_tail_skew_5d_base_v092_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x.rolling(5, min_periods=2).skew(), _s(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine median distance base
def f45nge_f45_network_growth_engine_median_gap_10d_base_v093_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x - x.rolling(10, min_periods=2).median(), _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine vol scaled level base
def f45nge_f45_network_growth_engine_vol_scaled_21d_base_v094_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x, _s(x.diff(5), 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine liquidity weight base
def f45nge_f45_network_growth_engine_abs_rank_weight_63d_base_v095_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = x * x.abs().rolling(63, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine dollar weight base
def f45nge_f45_network_growth_engine_abs_mean_weight_126d_base_v096_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _z(x * _m(x.abs(), 21), 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine stability score base
def f45nge_f45_network_growth_engine_stability_252d_base_v097_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(_m(x, 252), _m(x.diff(21).abs(), 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine decay balance base
def f45nge_f45_network_growth_engine_ewm_balance_504d_base_v098_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=504, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine accumulation ratio base
def f45nge_f45_network_growth_engine_positive_share_5d_base_v099_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div((x - _m(x, 5)).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine capitulation ratio base
def f45nge_f45_network_growth_engine_negative_share_10d_base_v100_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div((_m(x, 10) - x).clip(lower=0).rolling(10, min_periods=2).sum(), (x - _m(x, 10)).abs().rolling(10, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine level zscore base
def f45nge_f45_network_growth_engine_zlevel_21d_base_v101_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _z(x, 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine level to mean base
def f45nge_f45_network_growth_engine_mean_ratio_63d_base_v102_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x, _m(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine short minus long base
def f45nge_f45_network_growth_engine_ma_spread_126d_base_v103_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _spread(_m(x, 21), _m(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine ranked pressure base
def f45nge_f45_network_growth_engine_rank_pressure_252d_base_v104_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x - _mn(x, 252), _mx(x, 252) - _mn(x, 252)) + _z(x, 21) / np.sqrt(252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine trend strength base
def f45nge_f45_network_growth_engine_trend_force_504d_base_v105_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x.diff(21), _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine downside gap base
def f45nge_f45_network_growth_engine_down_tail_5d_base_v106_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x.rolling(5, min_periods=2).quantile(0.20) - x, _s(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine upside gap base
def f45nge_f45_network_growth_engine_up_tail_10d_base_v107_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x - x.rolling(10, min_periods=2).quantile(0.80), _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine range position base
def f45nge_f45_network_growth_engine_range_pos_21d_base_v108_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x - _mn(x, 21), _mx(x, 21) - _mn(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine mean reversion base
def f45nge_f45_network_growth_engine_revert_gap_63d_base_v109_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(_m(x, 21) - x, _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine expanding pressure base
def f45nge_f45_network_growth_engine_std_expand_126d_base_v110_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(_s(x, 21), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine compression ratio base
def f45nge_f45_network_growth_engine_std_compress_252d_base_v111_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(_s(x, 252), _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine breakout ratio base
def f45nge_f45_network_growth_engine_breakout_504d_base_v112_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x, _mx(x, 504).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine drawdown distance base
def f45nge_f45_network_growth_engine_drawdown_5d_base_v113_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x - _mx(x, 5), _mx(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine recovery distance base
def f45nge_f45_network_growth_engine_recovery_10d_base_v114_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x - _mn(x, 10), _mn(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine persistence share base
def f45nge_f45_network_growth_engine_persist_share_21d_base_v115_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(_m(x.diff(5), 21), _m(x.diff(5).abs(), 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine shock frequency base
def f45nge_f45_network_growth_engine_shock_freq_63d_base_v116_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _m(_z(x.diff(21), 63).abs(), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine tail pressure base
def f45nge_f45_network_growth_engine_tail_skew_126d_base_v117_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x.rolling(126, min_periods=2).skew(), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine median distance base
def f45nge_f45_network_growth_engine_median_gap_252d_base_v118_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x - x.rolling(252, min_periods=2).median(), _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine vol scaled level base
def f45nge_f45_network_growth_engine_vol_scaled_504d_base_v119_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x, _s(x.diff(21), 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine liquidity weight base
def f45nge_f45_network_growth_engine_abs_rank_weight_5d_base_v120_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = x * x.abs().rolling(5, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine dollar weight base
def f45nge_f45_network_growth_engine_abs_mean_weight_10d_base_v121_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _z(x * _m(x.abs(), 5), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine stability score base
def f45nge_f45_network_growth_engine_stability_21d_base_v122_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(_m(x, 21), _m(x.diff(5).abs(), 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine decay balance base
def f45nge_f45_network_growth_engine_ewm_balance_63d_base_v123_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=63, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine accumulation ratio base
def f45nge_f45_network_growth_engine_positive_share_126d_base_v124_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div((x - _m(x, 126)).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine capitulation ratio base
def f45nge_f45_network_growth_engine_negative_share_252d_base_v125_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div((_m(x, 252) - x).clip(lower=0).rolling(252, min_periods=2).sum(), (x - _m(x, 252)).abs().rolling(252, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine level zscore base
def f45nge_f45_network_growth_engine_zlevel_504d_base_v126_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _z(x, 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine level to mean base
def f45nge_f45_network_growth_engine_mean_ratio_5d_base_v127_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x, _m(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine short minus long base
def f45nge_f45_network_growth_engine_ma_spread_10d_base_v128_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _spread(_m(x, 5), _m(x, 20))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine ranked pressure base
def f45nge_f45_network_growth_engine_rank_pressure_21d_base_v129_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x - _mn(x, 21), _mx(x, 21) - _mn(x, 21)) + _z(x, 5) / np.sqrt(21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine trend strength base
def f45nge_f45_network_growth_engine_trend_force_63d_base_v130_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x.diff(21), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine downside gap base
def f45nge_f45_network_growth_engine_down_tail_126d_base_v131_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x.rolling(126, min_periods=2).quantile(0.20) - x, _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine upside gap base
def f45nge_f45_network_growth_engine_up_tail_252d_base_v132_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x - x.rolling(252, min_periods=2).quantile(0.80), _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine range position base
def f45nge_f45_network_growth_engine_range_pos_504d_base_v133_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x - _mn(x, 504), _mx(x, 504) - _mn(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine mean reversion base
def f45nge_f45_network_growth_engine_revert_gap_5d_base_v134_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(_m(x, 3) - x, _s(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine expanding pressure base
def f45nge_f45_network_growth_engine_std_expand_10d_base_v135_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(_s(x, 5), _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine compression ratio base
def f45nge_f45_network_growth_engine_std_compress_21d_base_v136_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(_s(x, 21), _s(x, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine breakout ratio base
def f45nge_f45_network_growth_engine_breakout_63d_base_v137_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x, _mx(x, 63).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine drawdown distance base
def f45nge_f45_network_growth_engine_drawdown_126d_base_v138_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x - _mx(x, 126), _mx(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine recovery distance base
def f45nge_f45_network_growth_engine_recovery_252d_base_v139_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x - _mn(x, 252), _mn(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine persistence share base
def f45nge_f45_network_growth_engine_persist_share_504d_base_v140_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(_m(x.diff(21), 504), _m(x.diff(21).abs(), 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine shock frequency base
def f45nge_f45_network_growth_engine_shock_freq_5d_base_v141_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _m(_z(x.diff(3), 5).abs(), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine tail pressure base
def f45nge_f45_network_growth_engine_tail_skew_10d_base_v142_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x.rolling(10, min_periods=2).skew(), _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine median distance base
def f45nge_f45_network_growth_engine_median_gap_21d_base_v143_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x - x.rolling(21, min_periods=2).median(), _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d network_growth_engine vol scaled level base
def f45nge_f45_network_growth_engine_vol_scaled_63d_base_v144_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x, _s(x.diff(21), 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d network_growth_engine liquidity weight base
def f45nge_f45_network_growth_engine_abs_rank_weight_126d_base_v145_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = x * x.abs().rolling(126, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d network_growth_engine dollar weight base
def f45nge_f45_network_growth_engine_abs_mean_weight_252d_base_v146_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _z(x * _m(x.abs(), 21), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d network_growth_engine stability score base
def f45nge_f45_network_growth_engine_stability_504d_base_v147_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(_m(x, 504), _m(x.diff(21).abs(), 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d network_growth_engine decay balance base
def f45nge_f45_network_growth_engine_ewm_balance_5d_base_v148_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x.ewm(span=3, adjust=False).mean(), x.ewm(span=5, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 10d network_growth_engine accumulation ratio base
def f45nge_f45_network_growth_engine_positive_share_10d_base_v149_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div((x - _m(x, 10)).clip(lower=0).rolling(10, min_periods=2).sum(), (x - _m(x, 10)).abs().rolling(10, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d network_growth_engine capitulation ratio base
def f45nge_f45_network_growth_engine_negative_share_21d_base_v150_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f45_network_growth_engine_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div((_m(x, 21) - x).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f45nge_f45_network_growth_engine_zlevel_252d_base_v076_signal,
    f45nge_f45_network_growth_engine_mean_ratio_504d_base_v077_signal,
    f45nge_f45_network_growth_engine_ma_spread_5d_base_v078_signal,
    f45nge_f45_network_growth_engine_rank_pressure_10d_base_v079_signal,
    f45nge_f45_network_growth_engine_trend_force_21d_base_v080_signal,
    f45nge_f45_network_growth_engine_down_tail_63d_base_v081_signal,
    f45nge_f45_network_growth_engine_up_tail_126d_base_v082_signal,
    f45nge_f45_network_growth_engine_range_pos_252d_base_v083_signal,
    f45nge_f45_network_growth_engine_revert_gap_504d_base_v084_signal,
    f45nge_f45_network_growth_engine_std_expand_5d_base_v085_signal,
    f45nge_f45_network_growth_engine_std_compress_10d_base_v086_signal,
    f45nge_f45_network_growth_engine_breakout_21d_base_v087_signal,
    f45nge_f45_network_growth_engine_drawdown_63d_base_v088_signal,
    f45nge_f45_network_growth_engine_recovery_126d_base_v089_signal,
    f45nge_f45_network_growth_engine_persist_share_252d_base_v090_signal,
    f45nge_f45_network_growth_engine_shock_freq_504d_base_v091_signal,
    f45nge_f45_network_growth_engine_tail_skew_5d_base_v092_signal,
    f45nge_f45_network_growth_engine_median_gap_10d_base_v093_signal,
    f45nge_f45_network_growth_engine_vol_scaled_21d_base_v094_signal,
    f45nge_f45_network_growth_engine_abs_rank_weight_63d_base_v095_signal,
    f45nge_f45_network_growth_engine_abs_mean_weight_126d_base_v096_signal,
    f45nge_f45_network_growth_engine_stability_252d_base_v097_signal,
    f45nge_f45_network_growth_engine_ewm_balance_504d_base_v098_signal,
    f45nge_f45_network_growth_engine_positive_share_5d_base_v099_signal,
    f45nge_f45_network_growth_engine_negative_share_10d_base_v100_signal,
    f45nge_f45_network_growth_engine_zlevel_21d_base_v101_signal,
    f45nge_f45_network_growth_engine_mean_ratio_63d_base_v102_signal,
    f45nge_f45_network_growth_engine_ma_spread_126d_base_v103_signal,
    f45nge_f45_network_growth_engine_rank_pressure_252d_base_v104_signal,
    f45nge_f45_network_growth_engine_trend_force_504d_base_v105_signal,
    f45nge_f45_network_growth_engine_down_tail_5d_base_v106_signal,
    f45nge_f45_network_growth_engine_up_tail_10d_base_v107_signal,
    f45nge_f45_network_growth_engine_range_pos_21d_base_v108_signal,
    f45nge_f45_network_growth_engine_revert_gap_63d_base_v109_signal,
    f45nge_f45_network_growth_engine_std_expand_126d_base_v110_signal,
    f45nge_f45_network_growth_engine_std_compress_252d_base_v111_signal,
    f45nge_f45_network_growth_engine_breakout_504d_base_v112_signal,
    f45nge_f45_network_growth_engine_drawdown_5d_base_v113_signal,
    f45nge_f45_network_growth_engine_recovery_10d_base_v114_signal,
    f45nge_f45_network_growth_engine_persist_share_21d_base_v115_signal,
    f45nge_f45_network_growth_engine_shock_freq_63d_base_v116_signal,
    f45nge_f45_network_growth_engine_tail_skew_126d_base_v117_signal,
    f45nge_f45_network_growth_engine_median_gap_252d_base_v118_signal,
    f45nge_f45_network_growth_engine_vol_scaled_504d_base_v119_signal,
    f45nge_f45_network_growth_engine_abs_rank_weight_5d_base_v120_signal,
    f45nge_f45_network_growth_engine_abs_mean_weight_10d_base_v121_signal,
    f45nge_f45_network_growth_engine_stability_21d_base_v122_signal,
    f45nge_f45_network_growth_engine_ewm_balance_63d_base_v123_signal,
    f45nge_f45_network_growth_engine_positive_share_126d_base_v124_signal,
    f45nge_f45_network_growth_engine_negative_share_252d_base_v125_signal,
    f45nge_f45_network_growth_engine_zlevel_504d_base_v126_signal,
    f45nge_f45_network_growth_engine_mean_ratio_5d_base_v127_signal,
    f45nge_f45_network_growth_engine_ma_spread_10d_base_v128_signal,
    f45nge_f45_network_growth_engine_rank_pressure_21d_base_v129_signal,
    f45nge_f45_network_growth_engine_trend_force_63d_base_v130_signal,
    f45nge_f45_network_growth_engine_down_tail_126d_base_v131_signal,
    f45nge_f45_network_growth_engine_up_tail_252d_base_v132_signal,
    f45nge_f45_network_growth_engine_range_pos_504d_base_v133_signal,
    f45nge_f45_network_growth_engine_revert_gap_5d_base_v134_signal,
    f45nge_f45_network_growth_engine_std_expand_10d_base_v135_signal,
    f45nge_f45_network_growth_engine_std_compress_21d_base_v136_signal,
    f45nge_f45_network_growth_engine_breakout_63d_base_v137_signal,
    f45nge_f45_network_growth_engine_drawdown_126d_base_v138_signal,
    f45nge_f45_network_growth_engine_recovery_252d_base_v139_signal,
    f45nge_f45_network_growth_engine_persist_share_504d_base_v140_signal,
    f45nge_f45_network_growth_engine_shock_freq_5d_base_v141_signal,
    f45nge_f45_network_growth_engine_tail_skew_10d_base_v142_signal,
    f45nge_f45_network_growth_engine_median_gap_21d_base_v143_signal,
    f45nge_f45_network_growth_engine_vol_scaled_63d_base_v144_signal,
    f45nge_f45_network_growth_engine_abs_rank_weight_126d_base_v145_signal,
    f45nge_f45_network_growth_engine_abs_mean_weight_252d_base_v146_signal,
    f45nge_f45_network_growth_engine_stability_504d_base_v147_signal,
    f45nge_f45_network_growth_engine_ewm_balance_5d_base_v148_signal,
    f45nge_f45_network_growth_engine_positive_share_10d_base_v149_signal,
    f45nge_f45_network_growth_engine_negative_share_21d_base_v150_signal,
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
        assert '_f45_network_growth_engine_primitive' in inspect.getsource(func)
    assert valid_nan >= int(len(REGISTRY) * 0.80)


F45_NETWORK_GROWTH_ENGINE_REGISTRY_076_150 = REGISTRY
