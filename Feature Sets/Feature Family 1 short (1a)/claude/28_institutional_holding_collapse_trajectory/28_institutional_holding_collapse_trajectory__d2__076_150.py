"""institutional_holding_collapse_trajectory d2 features 076-150 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5

def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, 'index') else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)

def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)

def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)

def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())

def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())

def _runlen_pos(s):
    pos = (s > 0).astype(float)
    grp = (pos != pos.shift()).cumsum()
    return pos.groupby(grp).cumsum() * pos

def _runlen_neg(s):
    neg = (s < 0).astype(float)
    grp = (neg != neg.shift()).cumsum()
    return neg.groupby(grp).cumsum() * neg

def _ema(s, span):
    return s.ewm(span=span, min_periods=max(span // 3, 2), adjust=False).mean()

def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def f28_ihct_076_inst_new_buyers_qoq_d2(inst_new_buyers):
    return inst_new_buyers.diff().diff().diff()

def f28_ihct_077_inst_new_buyers_yoy_d2(inst_new_buyers):
    return (inst_new_buyers - inst_new_buyers.shift(4)).diff().diff()

def f28_ihct_078_inst_new_buyers_dryup_4q_d2(inst_new_buyers):
    return inst_new_buyers.rolling(4, min_periods=2).mean().diff().diff()

def f28_ihct_079_inst_new_buyers_zero_streak_d2(inst_new_buyers):
    zero = (inst_new_buyers == 0).astype(float)
    grp = (zero != zero.shift()).cumsum()
    return (zero.groupby(grp).cumsum() * zero).diff().diff()

def f28_ihct_080_inst_full_sellers_qoq_d2(inst_full_sellers):
    return inst_full_sellers.diff().diff().diff()

def f28_ihct_081_inst_full_sellers_yoy_d2(inst_full_sellers):
    return (inst_full_sellers - inst_full_sellers.shift(4)).diff().diff()

def f28_ihct_082_inst_full_sellers_above_8q_avg_flag_d2(inst_full_sellers):
    avg = inst_full_sellers.rolling(8, min_periods=3).mean()
    return (inst_full_sellers > avg).astype(float).diff().diff()

def f28_ihct_083_inst_full_sellers_streak_d2(inst_full_sellers):
    return _runlen_pos(inst_full_sellers.diff()).diff().diff()

def f28_ihct_084_inst_net_new_minus_full_sellers_d2(inst_new_buyers, inst_full_sellers):
    return (inst_new_buyers - inst_full_sellers).diff().diff()

def f28_ihct_085_inst_net_new_minus_full_sellers_yoy_change_d2(inst_new_buyers, inst_full_sellers):
    d = inst_new_buyers - inst_full_sellers
    return (d - d.shift(4)).diff().diff()

def f28_ihct_086_inst_net_new_minus_full_sellers_drawdown_8q_d2(inst_new_buyers, inst_full_sellers):
    d = inst_new_buyers - inst_full_sellers
    hi = d.rolling(8, min_periods=3).max()
    return (d - hi).diff().diff()

def f28_ihct_087_inst_full_sellers_to_holders_ratio_d2(inst_full_sellers, inst_holders):
    return _safe_div(inst_full_sellers, inst_holders).diff().diff()

def f28_ihct_088_inst_full_sellers_to_holders_ratio_yoy_change_d2(inst_full_sellers, inst_holders):
    r = _safe_div(inst_full_sellers, inst_holders)
    return (r - r.shift(4)).diff().diff()

def f28_ihct_089_inst_new_buyers_to_holders_ratio_d2(inst_new_buyers, inst_holders):
    return _safe_div(inst_new_buyers, inst_holders).diff().diff()

def f28_ihct_090_inst_new_buyer_drought_8q_d2(inst_new_buyers):
    return (inst_new_buyers == 0).astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f28_ihct_091_hf_holders_qoq_pct_d2(hf_holders):
    return _qoq_pct(hf_holders).diff().diff()

def f28_ihct_092_hf_holders_yoy_pct_d2(hf_holders):
    return _yoy_pct(hf_holders).diff().diff()

def f28_ihct_093_mf_holders_qoq_pct_d2(mf_holders):
    return _qoq_pct(mf_holders).diff().diff()

def f28_ihct_094_mf_holders_yoy_pct_d2(mf_holders):
    return _yoy_pct(mf_holders).diff().diff()

def f28_ihct_095_pension_holders_qoq_pct_d2(pension_holders):
    return _qoq_pct(pension_holders).diff().diff()

def f28_ihct_096_hf_minus_mf_holders_growth_yoy_d2(hf_holders, mf_holders):
    return (_yoy_pct(hf_holders) - _yoy_pct(mf_holders)).diff().diff()

def f28_ihct_097_hf_holders_drawdown_8q_d2(hf_holders):
    hi = hf_holders.rolling(8, min_periods=3).max()
    return _safe_div(hf_holders - hi, hi.abs()).diff().diff()

def f28_ihct_098_mf_holders_drawdown_8q_d2(mf_holders):
    hi = mf_holders.rolling(8, min_periods=3).max()
    return _safe_div(mf_holders - hi, hi.abs()).diff().diff()

def f28_ihct_099_hf_share_of_total_holders_d2(hf_holders, inst_holders):
    return _safe_div(hf_holders, inst_holders).diff().diff()

def f28_ihct_100_hf_share_change_yoy_d2(hf_holders, inst_holders):
    r = _safe_div(hf_holders, inst_holders)
    return (r - r.shift(4)).diff().diff()

def f28_ihct_101_mf_share_of_total_holders_yoy_change_d2(mf_holders, inst_holders):
    r = _safe_div(mf_holders, inst_holders)
    return (r - r.shift(4)).diff().diff()

def f28_ihct_102_hf_share_acceleration_8q_d2(hf_holders, inst_holders):
    r = _safe_div(hf_holders, inst_holders)
    return r.diff().rolling(8, min_periods=3).sum().diff().diff()

def f28_ihct_103_hf_holders_growth_minus_total_growth_yoy_d2(hf_holders, inst_holders):
    return (_yoy_pct(hf_holders) - _yoy_pct(inst_holders)).diff().diff()

def f28_ihct_104_mf_holders_growth_minus_total_growth_yoy_d2(mf_holders, inst_holders):
    return (_yoy_pct(mf_holders) - _yoy_pct(inst_holders)).diff().diff()

def f28_ihct_105_hf_capitulation_signature_d2(hf_holders, inst_holders):
    return (_yoy_pct(hf_holders) < _yoy_pct(inst_holders)).astype(float).diff().diff()

def f28_ihct_106_inst_holders_high_water_drawdown_16q_d2(inst_holders):
    hi = inst_holders.rolling(16, min_periods=4).max()
    return _safe_div(inst_holders - hi, hi.abs()).diff().diff()

def f28_ihct_107_inst_holders_high_water_drawdown_20q_d2(inst_holders):
    hi = inst_holders.rolling(20, min_periods=5).max()
    return _safe_div(inst_holders - hi, hi.abs()).diff().diff()

def f28_ihct_108_inst_units_high_water_drawdown_16q_d2(inst_units):
    hi = inst_units.rolling(16, min_periods=4).max()
    return _safe_div(inst_units - hi, hi.abs()).diff().diff()

def f28_ihct_109_inst_value_high_water_drawdown_16q_d2(inst_value):
    hi = inst_value.rolling(16, min_periods=4).max()
    return _safe_div(inst_value - hi, hi.abs()).diff().diff()

def f28_ihct_110_inst_ownership_pct_high_water_drawdown_16q_d2(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    hi = own.rolling(16, min_periods=4).max()
    return (own - hi).diff().diff()

def f28_ihct_111_inst_holders_hwm_recovery_distance_16q_d2(inst_holders):
    hi = inst_holders.rolling(16, min_periods=4).max()
    return (hi - inst_holders).diff().diff()

def f28_ihct_112_inst_units_hwm_recovery_distance_16q_d2(inst_units):
    hi = inst_units.rolling(16, min_periods=4).max()
    return _safe_div(hi - inst_units, hi.abs()).diff().diff()

def f28_ihct_113_inst_holders_below_hwm_persistence_8q_d2(inst_holders):
    hi = inst_holders.rolling(16, min_periods=4).max()
    return (inst_holders < hi).astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f28_ihct_114_inst_units_below_hwm_persistence_8q_d2(inst_units):
    hi = inst_units.rolling(16, min_periods=4).max()
    return (inst_units < hi).astype(float).rolling(8, min_periods=3).sum().diff().diff()

def f28_ihct_115_inst_value_drawdown_to_8q_cagr_d2(inst_value):
    hi = inst_value.rolling(16, min_periods=4).max()
    dd = _safe_div(inst_value - hi, hi.abs())
    cagr = _safe_div(inst_value, inst_value.shift(8)) ** 0.5 - 1.0
    return _safe_div(dd, cagr.abs() + 0.01).diff().diff()

def f28_ihct_116_inst_holders_max_window_decline_8q_d2(inst_holders):
    return inst_holders.diff().rolling(8, min_periods=3).min().diff().diff()

def f28_ihct_117_inst_holders_max_window_decline_16q_d2(inst_holders):
    return inst_holders.diff().rolling(16, min_periods=4).min().diff().diff()

def f28_ihct_118_inst_units_cliff_event_max_q_d2(inst_units):
    return _qoq_pct(inst_units).rolling(16, min_periods=4).min().diff().diff()

def f28_ihct_119_inst_holders_cliff_event_max_q_d2(inst_holders):
    return _qoq_pct(inst_holders).rolling(16, min_periods=4).min().diff().diff()

def f28_ihct_120_inst_ownership_pct_cliff_event_max_q_d2(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return own.diff().rolling(16, min_periods=4).min().diff().diff()

def f28_ihct_121_inst_holders_zscore_qoq_minus_avg_d2(inst_holders):
    q = _qoq_pct(inst_holders)
    return _rolling_zscore(q, 8).diff().diff()

def f28_ihct_122_inst_units_zscore_qoq_minus_avg_d2(inst_units):
    q = _qoq_pct(inst_units)
    return _rolling_zscore(q, 8).diff().diff()

def f28_ihct_123_inst_full_sellers_zscore_8q_d2(inst_full_sellers):
    return _rolling_zscore(inst_full_sellers, 8).diff().diff()

def f28_ihct_124_inst_dec_count_zscore_8q_d2(inst_dec_count):
    return _rolling_zscore(inst_dec_count, 8).diff().diff()

def f28_ihct_125_inst_holders_compound_decline_8q_d2(inst_holders):
    neg = inst_holders.diff().clip(upper=0)
    return neg.rolling(8, min_periods=3).sum().diff().diff()

def f28_ihct_126_inst_units_compound_decline_8q_d2(inst_units):
    neg = inst_units.diff().clip(upper=0)
    return neg.rolling(8, min_periods=3).sum().diff().diff()

def f28_ihct_127_inst_value_compound_decline_8q_d2(inst_value):
    neg = inst_value.diff().clip(upper=0)
    return neg.rolling(8, min_periods=3).sum().diff().diff()

def f28_ihct_128_inst_holders_step_break_8q_d2(inst_holders):
    a = inst_holders.rolling(4, min_periods=2).mean()
    b = inst_holders.shift(4).rolling(4, min_periods=2).mean()
    return _safe_div(a - b, b.abs()).diff().diff()

def f28_ihct_129_inst_units_step_break_8q_d2(inst_units):
    a = inst_units.rolling(4, min_periods=2).mean()
    b = inst_units.shift(4).rolling(4, min_periods=2).mean()
    return _safe_div(a - b, b.abs()).diff().diff()

def f28_ihct_130_inst_full_sellers_step_break_8q_d2(inst_full_sellers):
    a = inst_full_sellers.rolling(4, min_periods=2).mean()
    b = inst_full_sellers.shift(4).rolling(4, min_periods=2).mean()
    return (a - b).diff().diff()

def f28_ihct_131_inst_inc_dryup_with_dec_surge_d2(inst_inc_count, inst_dec_count):
    inc_drop = (inst_inc_count - inst_inc_count.shift(4)).clip(upper=0)
    dec_rise = (inst_dec_count - inst_dec_count.shift(4)).clip(lower=0)
    return (dec_rise - inc_drop).diff().diff()

def f28_ihct_132_inst_collapse_signature_8q_d2(inst_holders, inst_units, inst_value):
    return ((inst_holders.diff(8) < 0).astype(float) + (inst_units.diff(8) < 0).astype(float) + (inst_value.diff(8) < 0).astype(float)).diff().diff()

def f28_ihct_133_inst_collapse_score_q_d2(inst_holders, inst_units, inst_value):
    return (-(_qoq_pct(inst_holders).clip(upper=0) + _qoq_pct(inst_units).clip(upper=0) + _qoq_pct(inst_value).clip(upper=0))).diff().diff()

def f28_ihct_134_inst_concentration_collapse_signature_d2(inst_top10_share, inst_holders):
    return ((inst_top10_share.diff() < 0) & (inst_holders.diff() < 0)).astype(float).diff().diff()

def f28_ihct_135_inst_distressed_exodus_signature_d2(inst_full_sellers, inst_inc_count):
    return (inst_full_sellers > inst_inc_count).astype(float).diff().diff()

def f28_ihct_136_inst_holders_trend_slope_12q_d2(inst_holders):
    return _rolling_slope(inst_holders, 12).diff().diff()

def f28_ihct_137_inst_units_trend_slope_12q_d2(inst_units):
    return _rolling_slope(inst_units, 12).diff().diff()

def f28_ihct_138_inst_value_trend_slope_12q_d2(inst_value):
    return _rolling_slope(inst_value, 12).diff().diff()

def f28_ihct_139_inst_ownership_pct_trend_slope_12q_d2(inst_units, sharesbas):
    own = _safe_div(inst_units, sharesbas)
    return _rolling_slope(own, 12).diff().diff()

def f28_ihct_140_inst_holders_smoothed_minus_raw_d2(inst_holders):
    return (_ema(inst_holders, 4) - inst_holders).diff().diff()

def f28_ihct_141_inst_units_smoothed_minus_raw_d2(inst_units):
    return (_ema(inst_units, 4) - inst_units).diff().diff()

def f28_ihct_142_inst_holders_log_residual_12q_d2(inst_holders):
    s = _safe_log(inst_holders)
    return (s - s.rolling(12, min_periods=4).mean()).diff().diff()

def f28_ihct_143_inst_units_chow_break_8q_d2(inst_units):
    rec = inst_units.diff().rolling(4, min_periods=2).var()
    full = inst_units.diff().rolling(8, min_periods=3).var()
    return _safe_div(rec, full).diff().diff()

def f28_ihct_144_inst_holders_long_window_yoy_minus_4q_yoy_d2(inst_holders):
    y4 = _yoy_pct(inst_holders)
    y8 = _safe_div(inst_holders - inst_holders.shift(8), inst_holders.shift(8).abs()) / 2.0
    return (y4 - y8).diff().diff()

def f28_ihct_145_inst_holders_step_drop_4q_after_peak_d2(inst_holders):
    hi = inst_holders.rolling(8, min_periods=3).max()
    at_peak = (inst_holders == hi).astype(float)
    return (inst_holders - inst_holders.where(at_peak.shift(4) == 1).ffill()).diff().diff()

def f28_ihct_146_inst_units_persistence_decline_index_12q_d2(inst_units):
    return (inst_units.diff() < 0).astype(float).rolling(12, min_periods=4).sum().diff().diff()

def f28_ihct_147_inst_value_persistence_decline_index_12q_d2(inst_value):
    return (inst_value.diff() < 0).astype(float).rolling(12, min_periods=4).sum().diff().diff()

def f28_ihct_148_inst_breadth_collapse_acceleration_8q_d2(inst_holders):
    a = _qoq_pct(inst_holders).rolling(4, min_periods=2).mean()
    b = _qoq_pct(inst_holders).shift(4).rolling(4, min_periods=2).mean()
    return (a - b).diff().diff()

def f28_ihct_149_inst_holder_collapse_terminal_score_d2(inst_holders, inst_units, inst_value, inst_full_sellers):
    return (-(_yoy_pct(inst_holders).clip(upper=0) + _yoy_pct(inst_units).clip(upper=0) + _yoy_pct(inst_value).clip(upper=0)) + _yoy_pct(inst_full_sellers).clip(lower=0)).diff().diff()

def f28_ihct_150_inst_holder_collapse_signature_persistence_d2(inst_holders, inst_units, inst_value):
    trig = ((inst_holders.diff() < 0) & (inst_units.diff() < 0) & (inst_value.diff() < 0)).astype(int)
    grp = (trig != trig.shift()).cumsum()
    return (trig.groupby(grp).cumsum() * trig).diff().diff()
INSTITUTIONAL_HOLDING_COLLAPSE_TRAJECTORY_D2_REGISTRY_076_150 = {'f28_ihct_076_inst_new_buyers_qoq_d2': {'inputs': ['inst_new_buyers'], 'func': f28_ihct_076_inst_new_buyers_qoq_d2}, 'f28_ihct_077_inst_new_buyers_yoy_d2': {'inputs': ['inst_new_buyers'], 'func': f28_ihct_077_inst_new_buyers_yoy_d2}, 'f28_ihct_078_inst_new_buyers_dryup_4q_d2': {'inputs': ['inst_new_buyers'], 'func': f28_ihct_078_inst_new_buyers_dryup_4q_d2}, 'f28_ihct_079_inst_new_buyers_zero_streak_d2': {'inputs': ['inst_new_buyers'], 'func': f28_ihct_079_inst_new_buyers_zero_streak_d2}, 'f28_ihct_080_inst_full_sellers_qoq_d2': {'inputs': ['inst_full_sellers'], 'func': f28_ihct_080_inst_full_sellers_qoq_d2}, 'f28_ihct_081_inst_full_sellers_yoy_d2': {'inputs': ['inst_full_sellers'], 'func': f28_ihct_081_inst_full_sellers_yoy_d2}, 'f28_ihct_082_inst_full_sellers_above_8q_avg_flag_d2': {'inputs': ['inst_full_sellers'], 'func': f28_ihct_082_inst_full_sellers_above_8q_avg_flag_d2}, 'f28_ihct_083_inst_full_sellers_streak_d2': {'inputs': ['inst_full_sellers'], 'func': f28_ihct_083_inst_full_sellers_streak_d2}, 'f28_ihct_084_inst_net_new_minus_full_sellers_d2': {'inputs': ['inst_new_buyers', 'inst_full_sellers'], 'func': f28_ihct_084_inst_net_new_minus_full_sellers_d2}, 'f28_ihct_085_inst_net_new_minus_full_sellers_yoy_change_d2': {'inputs': ['inst_new_buyers', 'inst_full_sellers'], 'func': f28_ihct_085_inst_net_new_minus_full_sellers_yoy_change_d2}, 'f28_ihct_086_inst_net_new_minus_full_sellers_drawdown_8q_d2': {'inputs': ['inst_new_buyers', 'inst_full_sellers'], 'func': f28_ihct_086_inst_net_new_minus_full_sellers_drawdown_8q_d2}, 'f28_ihct_087_inst_full_sellers_to_holders_ratio_d2': {'inputs': ['inst_full_sellers', 'inst_holders'], 'func': f28_ihct_087_inst_full_sellers_to_holders_ratio_d2}, 'f28_ihct_088_inst_full_sellers_to_holders_ratio_yoy_change_d2': {'inputs': ['inst_full_sellers', 'inst_holders'], 'func': f28_ihct_088_inst_full_sellers_to_holders_ratio_yoy_change_d2}, 'f28_ihct_089_inst_new_buyers_to_holders_ratio_d2': {'inputs': ['inst_new_buyers', 'inst_holders'], 'func': f28_ihct_089_inst_new_buyers_to_holders_ratio_d2}, 'f28_ihct_090_inst_new_buyer_drought_8q_d2': {'inputs': ['inst_new_buyers'], 'func': f28_ihct_090_inst_new_buyer_drought_8q_d2}, 'f28_ihct_091_hf_holders_qoq_pct_d2': {'inputs': ['hf_holders'], 'func': f28_ihct_091_hf_holders_qoq_pct_d2}, 'f28_ihct_092_hf_holders_yoy_pct_d2': {'inputs': ['hf_holders'], 'func': f28_ihct_092_hf_holders_yoy_pct_d2}, 'f28_ihct_093_mf_holders_qoq_pct_d2': {'inputs': ['mf_holders'], 'func': f28_ihct_093_mf_holders_qoq_pct_d2}, 'f28_ihct_094_mf_holders_yoy_pct_d2': {'inputs': ['mf_holders'], 'func': f28_ihct_094_mf_holders_yoy_pct_d2}, 'f28_ihct_095_pension_holders_qoq_pct_d2': {'inputs': ['pension_holders'], 'func': f28_ihct_095_pension_holders_qoq_pct_d2}, 'f28_ihct_096_hf_minus_mf_holders_growth_yoy_d2': {'inputs': ['hf_holders', 'mf_holders'], 'func': f28_ihct_096_hf_minus_mf_holders_growth_yoy_d2}, 'f28_ihct_097_hf_holders_drawdown_8q_d2': {'inputs': ['hf_holders'], 'func': f28_ihct_097_hf_holders_drawdown_8q_d2}, 'f28_ihct_098_mf_holders_drawdown_8q_d2': {'inputs': ['mf_holders'], 'func': f28_ihct_098_mf_holders_drawdown_8q_d2}, 'f28_ihct_099_hf_share_of_total_holders_d2': {'inputs': ['hf_holders', 'inst_holders'], 'func': f28_ihct_099_hf_share_of_total_holders_d2}, 'f28_ihct_100_hf_share_change_yoy_d2': {'inputs': ['hf_holders', 'inst_holders'], 'func': f28_ihct_100_hf_share_change_yoy_d2}, 'f28_ihct_101_mf_share_of_total_holders_yoy_change_d2': {'inputs': ['mf_holders', 'inst_holders'], 'func': f28_ihct_101_mf_share_of_total_holders_yoy_change_d2}, 'f28_ihct_102_hf_share_acceleration_8q_d2': {'inputs': ['hf_holders', 'inst_holders'], 'func': f28_ihct_102_hf_share_acceleration_8q_d2}, 'f28_ihct_103_hf_holders_growth_minus_total_growth_yoy_d2': {'inputs': ['hf_holders', 'inst_holders'], 'func': f28_ihct_103_hf_holders_growth_minus_total_growth_yoy_d2}, 'f28_ihct_104_mf_holders_growth_minus_total_growth_yoy_d2': {'inputs': ['mf_holders', 'inst_holders'], 'func': f28_ihct_104_mf_holders_growth_minus_total_growth_yoy_d2}, 'f28_ihct_105_hf_capitulation_signature_d2': {'inputs': ['hf_holders', 'inst_holders'], 'func': f28_ihct_105_hf_capitulation_signature_d2}, 'f28_ihct_106_inst_holders_high_water_drawdown_16q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_106_inst_holders_high_water_drawdown_16q_d2}, 'f28_ihct_107_inst_holders_high_water_drawdown_20q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_107_inst_holders_high_water_drawdown_20q_d2}, 'f28_ihct_108_inst_units_high_water_drawdown_16q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_108_inst_units_high_water_drawdown_16q_d2}, 'f28_ihct_109_inst_value_high_water_drawdown_16q_d2': {'inputs': ['inst_value'], 'func': f28_ihct_109_inst_value_high_water_drawdown_16q_d2}, 'f28_ihct_110_inst_ownership_pct_high_water_drawdown_16q_d2': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_110_inst_ownership_pct_high_water_drawdown_16q_d2}, 'f28_ihct_111_inst_holders_hwm_recovery_distance_16q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_111_inst_holders_hwm_recovery_distance_16q_d2}, 'f28_ihct_112_inst_units_hwm_recovery_distance_16q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_112_inst_units_hwm_recovery_distance_16q_d2}, 'f28_ihct_113_inst_holders_below_hwm_persistence_8q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_113_inst_holders_below_hwm_persistence_8q_d2}, 'f28_ihct_114_inst_units_below_hwm_persistence_8q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_114_inst_units_below_hwm_persistence_8q_d2}, 'f28_ihct_115_inst_value_drawdown_to_8q_cagr_d2': {'inputs': ['inst_value'], 'func': f28_ihct_115_inst_value_drawdown_to_8q_cagr_d2}, 'f28_ihct_116_inst_holders_max_window_decline_8q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_116_inst_holders_max_window_decline_8q_d2}, 'f28_ihct_117_inst_holders_max_window_decline_16q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_117_inst_holders_max_window_decline_16q_d2}, 'f28_ihct_118_inst_units_cliff_event_max_q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_118_inst_units_cliff_event_max_q_d2}, 'f28_ihct_119_inst_holders_cliff_event_max_q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_119_inst_holders_cliff_event_max_q_d2}, 'f28_ihct_120_inst_ownership_pct_cliff_event_max_q_d2': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_120_inst_ownership_pct_cliff_event_max_q_d2}, 'f28_ihct_121_inst_holders_zscore_qoq_minus_avg_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_121_inst_holders_zscore_qoq_minus_avg_d2}, 'f28_ihct_122_inst_units_zscore_qoq_minus_avg_d2': {'inputs': ['inst_units'], 'func': f28_ihct_122_inst_units_zscore_qoq_minus_avg_d2}, 'f28_ihct_123_inst_full_sellers_zscore_8q_d2': {'inputs': ['inst_full_sellers'], 'func': f28_ihct_123_inst_full_sellers_zscore_8q_d2}, 'f28_ihct_124_inst_dec_count_zscore_8q_d2': {'inputs': ['inst_dec_count'], 'func': f28_ihct_124_inst_dec_count_zscore_8q_d2}, 'f28_ihct_125_inst_holders_compound_decline_8q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_125_inst_holders_compound_decline_8q_d2}, 'f28_ihct_126_inst_units_compound_decline_8q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_126_inst_units_compound_decline_8q_d2}, 'f28_ihct_127_inst_value_compound_decline_8q_d2': {'inputs': ['inst_value'], 'func': f28_ihct_127_inst_value_compound_decline_8q_d2}, 'f28_ihct_128_inst_holders_step_break_8q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_128_inst_holders_step_break_8q_d2}, 'f28_ihct_129_inst_units_step_break_8q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_129_inst_units_step_break_8q_d2}, 'f28_ihct_130_inst_full_sellers_step_break_8q_d2': {'inputs': ['inst_full_sellers'], 'func': f28_ihct_130_inst_full_sellers_step_break_8q_d2}, 'f28_ihct_131_inst_inc_dryup_with_dec_surge_d2': {'inputs': ['inst_inc_count', 'inst_dec_count'], 'func': f28_ihct_131_inst_inc_dryup_with_dec_surge_d2}, 'f28_ihct_132_inst_collapse_signature_8q_d2': {'inputs': ['inst_holders', 'inst_units', 'inst_value'], 'func': f28_ihct_132_inst_collapse_signature_8q_d2}, 'f28_ihct_133_inst_collapse_score_q_d2': {'inputs': ['inst_holders', 'inst_units', 'inst_value'], 'func': f28_ihct_133_inst_collapse_score_q_d2}, 'f28_ihct_134_inst_concentration_collapse_signature_d2': {'inputs': ['inst_top10_share', 'inst_holders'], 'func': f28_ihct_134_inst_concentration_collapse_signature_d2}, 'f28_ihct_135_inst_distressed_exodus_signature_d2': {'inputs': ['inst_full_sellers', 'inst_inc_count'], 'func': f28_ihct_135_inst_distressed_exodus_signature_d2}, 'f28_ihct_136_inst_holders_trend_slope_12q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_136_inst_holders_trend_slope_12q_d2}, 'f28_ihct_137_inst_units_trend_slope_12q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_137_inst_units_trend_slope_12q_d2}, 'f28_ihct_138_inst_value_trend_slope_12q_d2': {'inputs': ['inst_value'], 'func': f28_ihct_138_inst_value_trend_slope_12q_d2}, 'f28_ihct_139_inst_ownership_pct_trend_slope_12q_d2': {'inputs': ['inst_units', 'sharesbas'], 'func': f28_ihct_139_inst_ownership_pct_trend_slope_12q_d2}, 'f28_ihct_140_inst_holders_smoothed_minus_raw_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_140_inst_holders_smoothed_minus_raw_d2}, 'f28_ihct_141_inst_units_smoothed_minus_raw_d2': {'inputs': ['inst_units'], 'func': f28_ihct_141_inst_units_smoothed_minus_raw_d2}, 'f28_ihct_142_inst_holders_log_residual_12q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_142_inst_holders_log_residual_12q_d2}, 'f28_ihct_143_inst_units_chow_break_8q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_143_inst_units_chow_break_8q_d2}, 'f28_ihct_144_inst_holders_long_window_yoy_minus_4q_yoy_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_144_inst_holders_long_window_yoy_minus_4q_yoy_d2}, 'f28_ihct_145_inst_holders_step_drop_4q_after_peak_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_145_inst_holders_step_drop_4q_after_peak_d2}, 'f28_ihct_146_inst_units_persistence_decline_index_12q_d2': {'inputs': ['inst_units'], 'func': f28_ihct_146_inst_units_persistence_decline_index_12q_d2}, 'f28_ihct_147_inst_value_persistence_decline_index_12q_d2': {'inputs': ['inst_value'], 'func': f28_ihct_147_inst_value_persistence_decline_index_12q_d2}, 'f28_ihct_148_inst_breadth_collapse_acceleration_8q_d2': {'inputs': ['inst_holders'], 'func': f28_ihct_148_inst_breadth_collapse_acceleration_8q_d2}, 'f28_ihct_149_inst_holder_collapse_terminal_score_d2': {'inputs': ['inst_holders', 'inst_units', 'inst_value', 'inst_full_sellers'], 'func': f28_ihct_149_inst_holder_collapse_terminal_score_d2}, 'f28_ihct_150_inst_holder_collapse_signature_persistence_d2': {'inputs': ['inst_holders', 'inst_units', 'inst_value'], 'func': f28_ihct_150_inst_holder_collapse_signature_persistence_d2}}
