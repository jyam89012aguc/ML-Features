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


def _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, w):
    owner_value = _m(sf3b_value, w)
    owner_shares = _m(sf3a_shares, w)
    return _z(_safe_div(ev + owner_value, marketcap) + _z(owner_shares, w), w)


# 5d moat_trajectory level zscore base
def f43mt_f43_moat_trajectory_zlevel_5d_base_v001_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _z(x, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory level to mean base
def f43mt_f43_moat_trajectory_mean_ratio_10d_base_v002_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x, _m(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory short minus long base
def f43mt_f43_moat_trajectory_ma_spread_21d_base_v003_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _spread(_m(x, 5), _m(x, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory ranked pressure base
def f43mt_f43_moat_trajectory_rank_pressure_63d_base_v004_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x - _mn(x, 63), _mx(x, 63) - _mn(x, 63)) + _z(x, 21) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory trend strength base
def f43mt_f43_moat_trajectory_trend_force_126d_base_v005_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x.diff(21), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory downside gap base
def f43mt_f43_moat_trajectory_down_tail_252d_base_v006_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x.rolling(252, min_periods=2).quantile(0.20) - x, _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory upside gap base
def f43mt_f43_moat_trajectory_up_tail_504d_base_v007_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x - x.rolling(504, min_periods=2).quantile(0.80), _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory range position base
def f43mt_f43_moat_trajectory_range_pos_5d_base_v008_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory mean reversion base
def f43mt_f43_moat_trajectory_revert_gap_10d_base_v009_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(_m(x, 5) - x, _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory expanding pressure base
def f43mt_f43_moat_trajectory_std_expand_21d_base_v010_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(_s(x, 5), _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory compression ratio base
def f43mt_f43_moat_trajectory_std_compress_63d_base_v011_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(_s(x, 63), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory breakout ratio base
def f43mt_f43_moat_trajectory_breakout_126d_base_v012_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x, _mx(x, 126).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory drawdown distance base
def f43mt_f43_moat_trajectory_drawdown_252d_base_v013_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x - _mx(x, 252), _mx(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory recovery distance base
def f43mt_f43_moat_trajectory_recovery_504d_base_v014_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x - _mn(x, 504), _mn(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory persistence share base
def f43mt_f43_moat_trajectory_persist_share_5d_base_v015_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(_m(x.diff(3), 5), _m(x.diff(3).abs(), 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory shock frequency base
def f43mt_f43_moat_trajectory_shock_freq_10d_base_v016_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _m(_z(x.diff(5), 10).abs(), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory tail pressure base
def f43mt_f43_moat_trajectory_tail_skew_21d_base_v017_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x.rolling(21, min_periods=2).skew(), _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory median distance base
def f43mt_f43_moat_trajectory_median_gap_63d_base_v018_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x - x.rolling(63, min_periods=2).median(), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory vol scaled level base
def f43mt_f43_moat_trajectory_vol_scaled_126d_base_v019_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x, _s(x.diff(21), 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory liquidity weight base
def f43mt_f43_moat_trajectory_abs_rank_weight_252d_base_v020_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = x * x.abs().rolling(252, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory dollar weight base
def f43mt_f43_moat_trajectory_abs_mean_weight_504d_base_v021_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _z(x * _m(x.abs(), 21), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory stability score base
def f43mt_f43_moat_trajectory_stability_5d_base_v022_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(_m(x, 5), _m(x.diff(3).abs(), 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory decay balance base
def f43mt_f43_moat_trajectory_ewm_balance_10d_base_v023_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=10, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory accumulation ratio base
def f43mt_f43_moat_trajectory_positive_share_21d_base_v024_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div((x - _m(x, 21)).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory capitulation ratio base
def f43mt_f43_moat_trajectory_negative_share_63d_base_v025_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div((_m(x, 63) - x).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory level zscore base
def f43mt_f43_moat_trajectory_zlevel_126d_base_v026_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _z(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory level to mean base
def f43mt_f43_moat_trajectory_mean_ratio_252d_base_v027_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x, _m(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory short minus long base
def f43mt_f43_moat_trajectory_ma_spread_504d_base_v028_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _spread(_m(x, 21), _m(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory ranked pressure base
def f43mt_f43_moat_trajectory_rank_pressure_5d_base_v029_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5)) + _z(x, 3) / np.sqrt(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory trend strength base
def f43mt_f43_moat_trajectory_trend_force_10d_base_v030_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x.diff(5), _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory downside gap base
def f43mt_f43_moat_trajectory_down_tail_21d_base_v031_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x.rolling(21, min_periods=2).quantile(0.20) - x, _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory upside gap base
def f43mt_f43_moat_trajectory_up_tail_63d_base_v032_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x - x.rolling(63, min_periods=2).quantile(0.80), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory range position base
def f43mt_f43_moat_trajectory_range_pos_126d_base_v033_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory mean reversion base
def f43mt_f43_moat_trajectory_revert_gap_252d_base_v034_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(_m(x, 21) - x, _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory expanding pressure base
def f43mt_f43_moat_trajectory_std_expand_504d_base_v035_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(_s(x, 21), _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory compression ratio base
def f43mt_f43_moat_trajectory_std_compress_5d_base_v036_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(_s(x, 5), _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory breakout ratio base
def f43mt_f43_moat_trajectory_breakout_10d_base_v037_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x, _mx(x, 10).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory drawdown distance base
def f43mt_f43_moat_trajectory_drawdown_21d_base_v038_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x - _mx(x, 21), _mx(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory recovery distance base
def f43mt_f43_moat_trajectory_recovery_63d_base_v039_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x - _mn(x, 63), _mn(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory persistence share base
def f43mt_f43_moat_trajectory_persist_share_126d_base_v040_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(_m(x.diff(21), 126), _m(x.diff(21).abs(), 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory shock frequency base
def f43mt_f43_moat_trajectory_shock_freq_252d_base_v041_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _m(_z(x.diff(21), 252).abs(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory tail pressure base
def f43mt_f43_moat_trajectory_tail_skew_504d_base_v042_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x.rolling(504, min_periods=2).skew(), _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory median distance base
def f43mt_f43_moat_trajectory_median_gap_5d_base_v043_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x - x.rolling(5, min_periods=2).median(), _s(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory vol scaled level base
def f43mt_f43_moat_trajectory_vol_scaled_10d_base_v044_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x, _s(x.diff(5), 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory liquidity weight base
def f43mt_f43_moat_trajectory_abs_rank_weight_21d_base_v045_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = x * x.abs().rolling(21, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory dollar weight base
def f43mt_f43_moat_trajectory_abs_mean_weight_63d_base_v046_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _z(x * _m(x.abs(), 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory stability score base
def f43mt_f43_moat_trajectory_stability_126d_base_v047_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(_m(x, 126), _m(x.diff(21).abs(), 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory decay balance base
def f43mt_f43_moat_trajectory_ewm_balance_252d_base_v048_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=252, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory accumulation ratio base
def f43mt_f43_moat_trajectory_positive_share_504d_base_v049_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div((x - _m(x, 504)).clip(lower=0).rolling(504, min_periods=2).sum(), (x - _m(x, 504)).abs().rolling(504, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory capitulation ratio base
def f43mt_f43_moat_trajectory_negative_share_5d_base_v050_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div((_m(x, 5) - x).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory level zscore base
def f43mt_f43_moat_trajectory_zlevel_10d_base_v051_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _z(x, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory level to mean base
def f43mt_f43_moat_trajectory_mean_ratio_21d_base_v052_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x, _m(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory short minus long base
def f43mt_f43_moat_trajectory_ma_spread_63d_base_v053_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _spread(_m(x, 21), _m(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory ranked pressure base
def f43mt_f43_moat_trajectory_rank_pressure_126d_base_v054_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126)) + _z(x, 21) / np.sqrt(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory trend strength base
def f43mt_f43_moat_trajectory_trend_force_252d_base_v055_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x.diff(21), _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory downside gap base
def f43mt_f43_moat_trajectory_down_tail_504d_base_v056_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x.rolling(504, min_periods=2).quantile(0.20) - x, _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory upside gap base
def f43mt_f43_moat_trajectory_up_tail_5d_base_v057_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x - x.rolling(5, min_periods=2).quantile(0.80), _s(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory range position base
def f43mt_f43_moat_trajectory_range_pos_10d_base_v058_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory mean reversion base
def f43mt_f43_moat_trajectory_revert_gap_21d_base_v059_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(_m(x, 5) - x, _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory expanding pressure base
def f43mt_f43_moat_trajectory_std_expand_63d_base_v060_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(_s(x, 21), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory compression ratio base
def f43mt_f43_moat_trajectory_std_compress_126d_base_v061_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(_s(x, 126), _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory breakout ratio base
def f43mt_f43_moat_trajectory_breakout_252d_base_v062_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x, _mx(x, 252).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory drawdown distance base
def f43mt_f43_moat_trajectory_drawdown_504d_base_v063_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = _safe_div(x - _mx(x, 504), _mx(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory recovery distance base
def f43mt_f43_moat_trajectory_recovery_5d_base_v064_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _safe_div(x - _mn(x, 5), _mn(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory persistence share base
def f43mt_f43_moat_trajectory_persist_share_10d_base_v065_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(_m(x.diff(5), 10), _m(x.diff(5).abs(), 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory shock frequency base
def f43mt_f43_moat_trajectory_shock_freq_21d_base_v066_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _m(_z(x.diff(5), 21).abs(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory tail pressure base
def f43mt_f43_moat_trajectory_tail_skew_63d_base_v067_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div(x.rolling(63, min_periods=2).skew(), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory median distance base
def f43mt_f43_moat_trajectory_median_gap_126d_base_v068_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div(x - x.rolling(126, min_periods=2).median(), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d moat_trajectory vol scaled level base
def f43mt_f43_moat_trajectory_vol_scaled_252d_base_v069_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 252)
    result = _safe_div(x, _s(x.diff(21), 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d moat_trajectory liquidity weight base
def f43mt_f43_moat_trajectory_abs_rank_weight_504d_base_v070_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 504)
    result = x * x.abs().rolling(504, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d moat_trajectory dollar weight base
def f43mt_f43_moat_trajectory_abs_mean_weight_5d_base_v071_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 5)
    result = _z(x * _m(x.abs(), 3), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d moat_trajectory stability score base
def f43mt_f43_moat_trajectory_stability_10d_base_v072_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 10)
    result = _safe_div(_m(x, 10), _m(x.diff(5).abs(), 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d moat_trajectory decay balance base
def f43mt_f43_moat_trajectory_ewm_balance_21d_base_v073_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 21)
    result = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=21, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d moat_trajectory accumulation ratio base
def f43mt_f43_moat_trajectory_positive_share_63d_base_v074_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 63)
    result = _safe_div((x - _m(x, 63)).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d moat_trajectory capitulation ratio base
def f43mt_f43_moat_trajectory_negative_share_126d_base_v075_signal(marketcap, ev, sf3a_shares, sf3b_value):
    x = _f43_moat_trajectory_primitive(marketcap, ev, sf3a_shares, sf3b_value, 126)
    result = _safe_div((_m(x, 126) - x).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f43mt_f43_moat_trajectory_zlevel_5d_base_v001_signal,
    f43mt_f43_moat_trajectory_mean_ratio_10d_base_v002_signal,
    f43mt_f43_moat_trajectory_ma_spread_21d_base_v003_signal,
    f43mt_f43_moat_trajectory_rank_pressure_63d_base_v004_signal,
    f43mt_f43_moat_trajectory_trend_force_126d_base_v005_signal,
    f43mt_f43_moat_trajectory_down_tail_252d_base_v006_signal,
    f43mt_f43_moat_trajectory_up_tail_504d_base_v007_signal,
    f43mt_f43_moat_trajectory_range_pos_5d_base_v008_signal,
    f43mt_f43_moat_trajectory_revert_gap_10d_base_v009_signal,
    f43mt_f43_moat_trajectory_std_expand_21d_base_v010_signal,
    f43mt_f43_moat_trajectory_std_compress_63d_base_v011_signal,
    f43mt_f43_moat_trajectory_breakout_126d_base_v012_signal,
    f43mt_f43_moat_trajectory_drawdown_252d_base_v013_signal,
    f43mt_f43_moat_trajectory_recovery_504d_base_v014_signal,
    f43mt_f43_moat_trajectory_persist_share_5d_base_v015_signal,
    f43mt_f43_moat_trajectory_shock_freq_10d_base_v016_signal,
    f43mt_f43_moat_trajectory_tail_skew_21d_base_v017_signal,
    f43mt_f43_moat_trajectory_median_gap_63d_base_v018_signal,
    f43mt_f43_moat_trajectory_vol_scaled_126d_base_v019_signal,
    f43mt_f43_moat_trajectory_abs_rank_weight_252d_base_v020_signal,
    f43mt_f43_moat_trajectory_abs_mean_weight_504d_base_v021_signal,
    f43mt_f43_moat_trajectory_stability_5d_base_v022_signal,
    f43mt_f43_moat_trajectory_ewm_balance_10d_base_v023_signal,
    f43mt_f43_moat_trajectory_positive_share_21d_base_v024_signal,
    f43mt_f43_moat_trajectory_negative_share_63d_base_v025_signal,
    f43mt_f43_moat_trajectory_zlevel_126d_base_v026_signal,
    f43mt_f43_moat_trajectory_mean_ratio_252d_base_v027_signal,
    f43mt_f43_moat_trajectory_ma_spread_504d_base_v028_signal,
    f43mt_f43_moat_trajectory_rank_pressure_5d_base_v029_signal,
    f43mt_f43_moat_trajectory_trend_force_10d_base_v030_signal,
    f43mt_f43_moat_trajectory_down_tail_21d_base_v031_signal,
    f43mt_f43_moat_trajectory_up_tail_63d_base_v032_signal,
    f43mt_f43_moat_trajectory_range_pos_126d_base_v033_signal,
    f43mt_f43_moat_trajectory_revert_gap_252d_base_v034_signal,
    f43mt_f43_moat_trajectory_std_expand_504d_base_v035_signal,
    f43mt_f43_moat_trajectory_std_compress_5d_base_v036_signal,
    f43mt_f43_moat_trajectory_breakout_10d_base_v037_signal,
    f43mt_f43_moat_trajectory_drawdown_21d_base_v038_signal,
    f43mt_f43_moat_trajectory_recovery_63d_base_v039_signal,
    f43mt_f43_moat_trajectory_persist_share_126d_base_v040_signal,
    f43mt_f43_moat_trajectory_shock_freq_252d_base_v041_signal,
    f43mt_f43_moat_trajectory_tail_skew_504d_base_v042_signal,
    f43mt_f43_moat_trajectory_median_gap_5d_base_v043_signal,
    f43mt_f43_moat_trajectory_vol_scaled_10d_base_v044_signal,
    f43mt_f43_moat_trajectory_abs_rank_weight_21d_base_v045_signal,
    f43mt_f43_moat_trajectory_abs_mean_weight_63d_base_v046_signal,
    f43mt_f43_moat_trajectory_stability_126d_base_v047_signal,
    f43mt_f43_moat_trajectory_ewm_balance_252d_base_v048_signal,
    f43mt_f43_moat_trajectory_positive_share_504d_base_v049_signal,
    f43mt_f43_moat_trajectory_negative_share_5d_base_v050_signal,
    f43mt_f43_moat_trajectory_zlevel_10d_base_v051_signal,
    f43mt_f43_moat_trajectory_mean_ratio_21d_base_v052_signal,
    f43mt_f43_moat_trajectory_ma_spread_63d_base_v053_signal,
    f43mt_f43_moat_trajectory_rank_pressure_126d_base_v054_signal,
    f43mt_f43_moat_trajectory_trend_force_252d_base_v055_signal,
    f43mt_f43_moat_trajectory_down_tail_504d_base_v056_signal,
    f43mt_f43_moat_trajectory_up_tail_5d_base_v057_signal,
    f43mt_f43_moat_trajectory_range_pos_10d_base_v058_signal,
    f43mt_f43_moat_trajectory_revert_gap_21d_base_v059_signal,
    f43mt_f43_moat_trajectory_std_expand_63d_base_v060_signal,
    f43mt_f43_moat_trajectory_std_compress_126d_base_v061_signal,
    f43mt_f43_moat_trajectory_breakout_252d_base_v062_signal,
    f43mt_f43_moat_trajectory_drawdown_504d_base_v063_signal,
    f43mt_f43_moat_trajectory_recovery_5d_base_v064_signal,
    f43mt_f43_moat_trajectory_persist_share_10d_base_v065_signal,
    f43mt_f43_moat_trajectory_shock_freq_21d_base_v066_signal,
    f43mt_f43_moat_trajectory_tail_skew_63d_base_v067_signal,
    f43mt_f43_moat_trajectory_median_gap_126d_base_v068_signal,
    f43mt_f43_moat_trajectory_vol_scaled_252d_base_v069_signal,
    f43mt_f43_moat_trajectory_abs_rank_weight_504d_base_v070_signal,
    f43mt_f43_moat_trajectory_abs_mean_weight_5d_base_v071_signal,
    f43mt_f43_moat_trajectory_stability_10d_base_v072_signal,
    f43mt_f43_moat_trajectory_ewm_balance_21d_base_v073_signal,
    f43mt_f43_moat_trajectory_positive_share_63d_base_v074_signal,
    f43mt_f43_moat_trajectory_negative_share_126d_base_v075_signal,
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
        assert '_f43_moat_trajectory_primitive' in inspect.getsource(func)
    assert valid_nan >= int(len(REGISTRY) * 0.80)


F43_MOAT_TRAJECTORY_REGISTRY_001_075 = REGISTRY
