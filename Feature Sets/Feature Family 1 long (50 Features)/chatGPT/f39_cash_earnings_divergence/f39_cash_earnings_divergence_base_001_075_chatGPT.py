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


def _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, w):
    scale = assets.abs().replace(0, np.nan)
    operating = _safe_div(revenue + netinc + fcf, scale)
    return _z(operating, w)


# 5d cash_earnings_divergence level zscore base
def f39ced_f39_cash_earnings_divergence_zlevel_5d_base_v001_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _z(x, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence level to mean base
def f39ced_f39_cash_earnings_divergence_mean_ratio_10d_base_v002_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(x, _m(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence short minus long base
def f39ced_f39_cash_earnings_divergence_ma_spread_21d_base_v003_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _spread(_m(x, 5), _m(x, 42))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence ranked pressure base
def f39ced_f39_cash_earnings_divergence_rank_pressure_63d_base_v004_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div(x - _mn(x, 63), _mx(x, 63) - _mn(x, 63)) + _z(x, 21) / np.sqrt(63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence trend strength base
def f39ced_f39_cash_earnings_divergence_trend_force_126d_base_v005_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(x.diff(21), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence downside gap base
def f39ced_f39_cash_earnings_divergence_down_tail_252d_base_v006_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _safe_div(x.rolling(252, min_periods=2).quantile(0.20) - x, _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence upside gap base
def f39ced_f39_cash_earnings_divergence_up_tail_504d_base_v007_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _safe_div(x - x.rolling(504, min_periods=2).quantile(0.80), _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence range position base
def f39ced_f39_cash_earnings_divergence_range_pos_5d_base_v008_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence mean reversion base
def f39ced_f39_cash_earnings_divergence_revert_gap_10d_base_v009_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(_m(x, 5) - x, _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence expanding pressure base
def f39ced_f39_cash_earnings_divergence_std_expand_21d_base_v010_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _safe_div(_s(x, 5), _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence compression ratio base
def f39ced_f39_cash_earnings_divergence_std_compress_63d_base_v011_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div(_s(x, 63), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence breakout ratio base
def f39ced_f39_cash_earnings_divergence_breakout_126d_base_v012_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(x, _mx(x, 126).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence drawdown distance base
def f39ced_f39_cash_earnings_divergence_drawdown_252d_base_v013_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _safe_div(x - _mx(x, 252), _mx(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence recovery distance base
def f39ced_f39_cash_earnings_divergence_recovery_504d_base_v014_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _safe_div(x - _mn(x, 504), _mn(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence persistence share base
def f39ced_f39_cash_earnings_divergence_persist_share_5d_base_v015_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div(_m(x.diff(3), 5), _m(x.diff(3).abs(), 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence shock frequency base
def f39ced_f39_cash_earnings_divergence_shock_freq_10d_base_v016_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _m(_z(x.diff(5), 10).abs(), 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence tail pressure base
def f39ced_f39_cash_earnings_divergence_tail_skew_21d_base_v017_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _safe_div(x.rolling(21, min_periods=2).skew(), _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence median distance base
def f39ced_f39_cash_earnings_divergence_median_gap_63d_base_v018_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div(x - x.rolling(63, min_periods=2).median(), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence vol scaled level base
def f39ced_f39_cash_earnings_divergence_vol_scaled_126d_base_v019_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(x, _s(x.diff(21), 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence liquidity weight base
def f39ced_f39_cash_earnings_divergence_abs_rank_weight_252d_base_v020_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = x * x.abs().rolling(252, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence dollar weight base
def f39ced_f39_cash_earnings_divergence_abs_mean_weight_504d_base_v021_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _z(x * _m(x.abs(), 21), 504)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence stability score base
def f39ced_f39_cash_earnings_divergence_stability_5d_base_v022_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div(_m(x, 5), _m(x.diff(3).abs(), 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence decay balance base
def f39ced_f39_cash_earnings_divergence_ewm_balance_10d_base_v023_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=10, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence accumulation ratio base
def f39ced_f39_cash_earnings_divergence_positive_share_21d_base_v024_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _safe_div((x - _m(x, 21)).clip(lower=0).rolling(21, min_periods=2).sum(), (x - _m(x, 21)).abs().rolling(21, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence capitulation ratio base
def f39ced_f39_cash_earnings_divergence_negative_share_63d_base_v025_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div((_m(x, 63) - x).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence level zscore base
def f39ced_f39_cash_earnings_divergence_zlevel_126d_base_v026_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _z(x, 126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence level to mean base
def f39ced_f39_cash_earnings_divergence_mean_ratio_252d_base_v027_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _safe_div(x, _m(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence short minus long base
def f39ced_f39_cash_earnings_divergence_ma_spread_504d_base_v028_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _spread(_m(x, 21), _m(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence ranked pressure base
def f39ced_f39_cash_earnings_divergence_rank_pressure_5d_base_v029_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div(x - _mn(x, 5), _mx(x, 5) - _mn(x, 5)) + _z(x, 3) / np.sqrt(5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence trend strength base
def f39ced_f39_cash_earnings_divergence_trend_force_10d_base_v030_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(x.diff(5), _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence downside gap base
def f39ced_f39_cash_earnings_divergence_down_tail_21d_base_v031_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _safe_div(x.rolling(21, min_periods=2).quantile(0.20) - x, _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence upside gap base
def f39ced_f39_cash_earnings_divergence_up_tail_63d_base_v032_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div(x - x.rolling(63, min_periods=2).quantile(0.80), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence range position base
def f39ced_f39_cash_earnings_divergence_range_pos_126d_base_v033_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence mean reversion base
def f39ced_f39_cash_earnings_divergence_revert_gap_252d_base_v034_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _safe_div(_m(x, 21) - x, _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence expanding pressure base
def f39ced_f39_cash_earnings_divergence_std_expand_504d_base_v035_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _safe_div(_s(x, 21), _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence compression ratio base
def f39ced_f39_cash_earnings_divergence_std_compress_5d_base_v036_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div(_s(x, 5), _s(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence breakout ratio base
def f39ced_f39_cash_earnings_divergence_breakout_10d_base_v037_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(x, _mx(x, 10).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence drawdown distance base
def f39ced_f39_cash_earnings_divergence_drawdown_21d_base_v038_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _safe_div(x - _mx(x, 21), _mx(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence recovery distance base
def f39ced_f39_cash_earnings_divergence_recovery_63d_base_v039_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div(x - _mn(x, 63), _mn(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence persistence share base
def f39ced_f39_cash_earnings_divergence_persist_share_126d_base_v040_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(_m(x.diff(21), 126), _m(x.diff(21).abs(), 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence shock frequency base
def f39ced_f39_cash_earnings_divergence_shock_freq_252d_base_v041_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _m(_z(x.diff(21), 252).abs(), 252)
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence tail pressure base
def f39ced_f39_cash_earnings_divergence_tail_skew_504d_base_v042_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _safe_div(x.rolling(504, min_periods=2).skew(), _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence median distance base
def f39ced_f39_cash_earnings_divergence_median_gap_5d_base_v043_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div(x - x.rolling(5, min_periods=2).median(), _s(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence vol scaled level base
def f39ced_f39_cash_earnings_divergence_vol_scaled_10d_base_v044_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(x, _s(x.diff(5), 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence liquidity weight base
def f39ced_f39_cash_earnings_divergence_abs_rank_weight_21d_base_v045_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = x * x.abs().rolling(21, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence dollar weight base
def f39ced_f39_cash_earnings_divergence_abs_mean_weight_63d_base_v046_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _z(x * _m(x.abs(), 21), 63)
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence stability score base
def f39ced_f39_cash_earnings_divergence_stability_126d_base_v047_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(_m(x, 126), _m(x.diff(21).abs(), 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence decay balance base
def f39ced_f39_cash_earnings_divergence_ewm_balance_252d_base_v048_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _safe_div(x.ewm(span=21, adjust=False).mean(), x.ewm(span=252, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence accumulation ratio base
def f39ced_f39_cash_earnings_divergence_positive_share_504d_base_v049_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _safe_div((x - _m(x, 504)).clip(lower=0).rolling(504, min_periods=2).sum(), (x - _m(x, 504)).abs().rolling(504, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence capitulation ratio base
def f39ced_f39_cash_earnings_divergence_negative_share_5d_base_v050_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div((_m(x, 5) - x).clip(lower=0).rolling(5, min_periods=2).sum(), (x - _m(x, 5)).abs().rolling(5, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence level zscore base
def f39ced_f39_cash_earnings_divergence_zlevel_10d_base_v051_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _z(x, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence level to mean base
def f39ced_f39_cash_earnings_divergence_mean_ratio_21d_base_v052_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _safe_div(x, _m(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence short minus long base
def f39ced_f39_cash_earnings_divergence_ma_spread_63d_base_v053_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _spread(_m(x, 21), _m(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence ranked pressure base
def f39ced_f39_cash_earnings_divergence_rank_pressure_126d_base_v054_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(x - _mn(x, 126), _mx(x, 126) - _mn(x, 126)) + _z(x, 21) / np.sqrt(126)
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence trend strength base
def f39ced_f39_cash_earnings_divergence_trend_force_252d_base_v055_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _safe_div(x.diff(21), _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence downside gap base
def f39ced_f39_cash_earnings_divergence_down_tail_504d_base_v056_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _safe_div(x.rolling(504, min_periods=2).quantile(0.20) - x, _s(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence upside gap base
def f39ced_f39_cash_earnings_divergence_up_tail_5d_base_v057_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div(x - x.rolling(5, min_periods=2).quantile(0.80), _s(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence range position base
def f39ced_f39_cash_earnings_divergence_range_pos_10d_base_v058_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(x - _mn(x, 10), _mx(x, 10) - _mn(x, 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence mean reversion base
def f39ced_f39_cash_earnings_divergence_revert_gap_21d_base_v059_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _safe_div(_m(x, 5) - x, _s(x, 21))
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence expanding pressure base
def f39ced_f39_cash_earnings_divergence_std_expand_63d_base_v060_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div(_s(x, 21), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence compression ratio base
def f39ced_f39_cash_earnings_divergence_std_compress_126d_base_v061_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(_s(x, 126), _s(x, 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence breakout ratio base
def f39ced_f39_cash_earnings_divergence_breakout_252d_base_v062_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _safe_div(x, _mx(x, 252).shift(1))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence drawdown distance base
def f39ced_f39_cash_earnings_divergence_drawdown_504d_base_v063_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = _safe_div(x - _mx(x, 504), _mx(x, 504))
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence recovery distance base
def f39ced_f39_cash_earnings_divergence_recovery_5d_base_v064_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _safe_div(x - _mn(x, 5), _mn(x, 5))
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence persistence share base
def f39ced_f39_cash_earnings_divergence_persist_share_10d_base_v065_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(_m(x.diff(5), 10), _m(x.diff(5).abs(), 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence shock frequency base
def f39ced_f39_cash_earnings_divergence_shock_freq_21d_base_v066_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _m(_z(x.diff(5), 21).abs(), 21)
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence tail pressure base
def f39ced_f39_cash_earnings_divergence_tail_skew_63d_base_v067_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div(x.rolling(63, min_periods=2).skew(), _s(x, 63))
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence median distance base
def f39ced_f39_cash_earnings_divergence_median_gap_126d_base_v068_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div(x - x.rolling(126, min_periods=2).median(), _s(x, 126))
    return result.replace([np.inf, -np.inf], np.nan)


# 252d cash_earnings_divergence vol scaled level base
def f39ced_f39_cash_earnings_divergence_vol_scaled_252d_base_v069_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 252)
    result = _safe_div(x, _s(x.diff(21), 252))
    return result.replace([np.inf, -np.inf], np.nan)


# 504d cash_earnings_divergence liquidity weight base
def f39ced_f39_cash_earnings_divergence_abs_rank_weight_504d_base_v070_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 504)
    result = x * x.abs().rolling(504, min_periods=2).rank(pct=True)
    return result.replace([np.inf, -np.inf], np.nan)


# 5d cash_earnings_divergence dollar weight base
def f39ced_f39_cash_earnings_divergence_abs_mean_weight_5d_base_v071_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 5)
    result = _z(x * _m(x.abs(), 3), 5)
    return result.replace([np.inf, -np.inf], np.nan)


# 10d cash_earnings_divergence stability score base
def f39ced_f39_cash_earnings_divergence_stability_10d_base_v072_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 10)
    result = _safe_div(_m(x, 10), _m(x.diff(5).abs(), 10))
    return result.replace([np.inf, -np.inf], np.nan)


# 21d cash_earnings_divergence decay balance base
def f39ced_f39_cash_earnings_divergence_ewm_balance_21d_base_v073_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 21)
    result = _safe_div(x.ewm(span=5, adjust=False).mean(), x.ewm(span=21, adjust=False).mean())
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cash_earnings_divergence accumulation ratio base
def f39ced_f39_cash_earnings_divergence_positive_share_63d_base_v074_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 63)
    result = _safe_div((x - _m(x, 63)).clip(lower=0).rolling(63, min_periods=2).sum(), (x - _m(x, 63)).abs().rolling(63, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


# 126d cash_earnings_divergence capitulation ratio base
def f39ced_f39_cash_earnings_divergence_negative_share_126d_base_v075_signal(revenue, netinc, fcf, assets):
    x = _f39_cash_earnings_divergence_primitive(revenue, netinc, fcf, assets, 126)
    result = _safe_div((_m(x, 126) - x).clip(lower=0).rolling(126, min_periods=2).sum(), (x - _m(x, 126)).abs().rolling(126, min_periods=2).sum())
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f39ced_f39_cash_earnings_divergence_zlevel_5d_base_v001_signal,
    f39ced_f39_cash_earnings_divergence_mean_ratio_10d_base_v002_signal,
    f39ced_f39_cash_earnings_divergence_ma_spread_21d_base_v003_signal,
    f39ced_f39_cash_earnings_divergence_rank_pressure_63d_base_v004_signal,
    f39ced_f39_cash_earnings_divergence_trend_force_126d_base_v005_signal,
    f39ced_f39_cash_earnings_divergence_down_tail_252d_base_v006_signal,
    f39ced_f39_cash_earnings_divergence_up_tail_504d_base_v007_signal,
    f39ced_f39_cash_earnings_divergence_range_pos_5d_base_v008_signal,
    f39ced_f39_cash_earnings_divergence_revert_gap_10d_base_v009_signal,
    f39ced_f39_cash_earnings_divergence_std_expand_21d_base_v010_signal,
    f39ced_f39_cash_earnings_divergence_std_compress_63d_base_v011_signal,
    f39ced_f39_cash_earnings_divergence_breakout_126d_base_v012_signal,
    f39ced_f39_cash_earnings_divergence_drawdown_252d_base_v013_signal,
    f39ced_f39_cash_earnings_divergence_recovery_504d_base_v014_signal,
    f39ced_f39_cash_earnings_divergence_persist_share_5d_base_v015_signal,
    f39ced_f39_cash_earnings_divergence_shock_freq_10d_base_v016_signal,
    f39ced_f39_cash_earnings_divergence_tail_skew_21d_base_v017_signal,
    f39ced_f39_cash_earnings_divergence_median_gap_63d_base_v018_signal,
    f39ced_f39_cash_earnings_divergence_vol_scaled_126d_base_v019_signal,
    f39ced_f39_cash_earnings_divergence_abs_rank_weight_252d_base_v020_signal,
    f39ced_f39_cash_earnings_divergence_abs_mean_weight_504d_base_v021_signal,
    f39ced_f39_cash_earnings_divergence_stability_5d_base_v022_signal,
    f39ced_f39_cash_earnings_divergence_ewm_balance_10d_base_v023_signal,
    f39ced_f39_cash_earnings_divergence_positive_share_21d_base_v024_signal,
    f39ced_f39_cash_earnings_divergence_negative_share_63d_base_v025_signal,
    f39ced_f39_cash_earnings_divergence_zlevel_126d_base_v026_signal,
    f39ced_f39_cash_earnings_divergence_mean_ratio_252d_base_v027_signal,
    f39ced_f39_cash_earnings_divergence_ma_spread_504d_base_v028_signal,
    f39ced_f39_cash_earnings_divergence_rank_pressure_5d_base_v029_signal,
    f39ced_f39_cash_earnings_divergence_trend_force_10d_base_v030_signal,
    f39ced_f39_cash_earnings_divergence_down_tail_21d_base_v031_signal,
    f39ced_f39_cash_earnings_divergence_up_tail_63d_base_v032_signal,
    f39ced_f39_cash_earnings_divergence_range_pos_126d_base_v033_signal,
    f39ced_f39_cash_earnings_divergence_revert_gap_252d_base_v034_signal,
    f39ced_f39_cash_earnings_divergence_std_expand_504d_base_v035_signal,
    f39ced_f39_cash_earnings_divergence_std_compress_5d_base_v036_signal,
    f39ced_f39_cash_earnings_divergence_breakout_10d_base_v037_signal,
    f39ced_f39_cash_earnings_divergence_drawdown_21d_base_v038_signal,
    f39ced_f39_cash_earnings_divergence_recovery_63d_base_v039_signal,
    f39ced_f39_cash_earnings_divergence_persist_share_126d_base_v040_signal,
    f39ced_f39_cash_earnings_divergence_shock_freq_252d_base_v041_signal,
    f39ced_f39_cash_earnings_divergence_tail_skew_504d_base_v042_signal,
    f39ced_f39_cash_earnings_divergence_median_gap_5d_base_v043_signal,
    f39ced_f39_cash_earnings_divergence_vol_scaled_10d_base_v044_signal,
    f39ced_f39_cash_earnings_divergence_abs_rank_weight_21d_base_v045_signal,
    f39ced_f39_cash_earnings_divergence_abs_mean_weight_63d_base_v046_signal,
    f39ced_f39_cash_earnings_divergence_stability_126d_base_v047_signal,
    f39ced_f39_cash_earnings_divergence_ewm_balance_252d_base_v048_signal,
    f39ced_f39_cash_earnings_divergence_positive_share_504d_base_v049_signal,
    f39ced_f39_cash_earnings_divergence_negative_share_5d_base_v050_signal,
    f39ced_f39_cash_earnings_divergence_zlevel_10d_base_v051_signal,
    f39ced_f39_cash_earnings_divergence_mean_ratio_21d_base_v052_signal,
    f39ced_f39_cash_earnings_divergence_ma_spread_63d_base_v053_signal,
    f39ced_f39_cash_earnings_divergence_rank_pressure_126d_base_v054_signal,
    f39ced_f39_cash_earnings_divergence_trend_force_252d_base_v055_signal,
    f39ced_f39_cash_earnings_divergence_down_tail_504d_base_v056_signal,
    f39ced_f39_cash_earnings_divergence_up_tail_5d_base_v057_signal,
    f39ced_f39_cash_earnings_divergence_range_pos_10d_base_v058_signal,
    f39ced_f39_cash_earnings_divergence_revert_gap_21d_base_v059_signal,
    f39ced_f39_cash_earnings_divergence_std_expand_63d_base_v060_signal,
    f39ced_f39_cash_earnings_divergence_std_compress_126d_base_v061_signal,
    f39ced_f39_cash_earnings_divergence_breakout_252d_base_v062_signal,
    f39ced_f39_cash_earnings_divergence_drawdown_504d_base_v063_signal,
    f39ced_f39_cash_earnings_divergence_recovery_5d_base_v064_signal,
    f39ced_f39_cash_earnings_divergence_persist_share_10d_base_v065_signal,
    f39ced_f39_cash_earnings_divergence_shock_freq_21d_base_v066_signal,
    f39ced_f39_cash_earnings_divergence_tail_skew_63d_base_v067_signal,
    f39ced_f39_cash_earnings_divergence_median_gap_126d_base_v068_signal,
    f39ced_f39_cash_earnings_divergence_vol_scaled_252d_base_v069_signal,
    f39ced_f39_cash_earnings_divergence_abs_rank_weight_504d_base_v070_signal,
    f39ced_f39_cash_earnings_divergence_abs_mean_weight_5d_base_v071_signal,
    f39ced_f39_cash_earnings_divergence_stability_10d_base_v072_signal,
    f39ced_f39_cash_earnings_divergence_ewm_balance_21d_base_v073_signal,
    f39ced_f39_cash_earnings_divergence_positive_share_63d_base_v074_signal,
    f39ced_f39_cash_earnings_divergence_negative_share_126d_base_v075_signal,
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
        assert '_f39_cash_earnings_divergence_primitive' in inspect.getsource(func)
    assert valid_nan >= int(len(REGISTRY) * 0.80)


F39_CASH_EARNINGS_DIVERGENCE_REGISTRY_001_075 = REGISTRY
