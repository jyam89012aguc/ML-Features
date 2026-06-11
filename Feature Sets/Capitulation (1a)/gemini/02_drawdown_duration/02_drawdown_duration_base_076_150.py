"""
Drawdown Duration — Base Features 076–150
Domain: time spent in drawdown, days since high
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_TD_WEEK = 5
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).max()

def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).min()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).sum()

def _ewm_mean(s: pd.Series, w: int) -> pd.Series:
    return s.ewm(span=w, min_periods=1).mean()

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))

def _daily_ret(s: pd.Series) -> pd.Series:
    return s.pct_change().fillna(0)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).median()

# Domain Specific Additions
def _days_since_high(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).apply(lambda x: len(x) - 1 - np.argmax(x), raw=True)

def _days_since_expanding_high(s: pd.Series) -> pd.Series:
    cummax = s.cummax()
    new_highs = (s == cummax)
    high_indices = pd.Series(np.arange(len(s)), index=s.index).where(new_highs).ffill()
    return pd.Series(np.arange(len(s)), index=s.index) - high_indices

def _pct_change(s: pd.Series, periods: int = 1) -> pd.Series:
    prev = s.shift(periods)
    return _safe_div(s - prev, prev.abs())

# ── Feature functions ────────────────────────────────────────────────────────

def ddur_076_days_since_ebitda_ath(ebitda: pd.Series) -> pd.Series:
    """ddur_076_days_since_ebitda_ath"""
    return _days_since_expanding_high(ebitda)

def ddur_077_days_since_netinc_ath(netinc: pd.Series) -> pd.Series:
    """ddur_077_days_since_netinc_ath"""
    return _days_since_expanding_high(netinc)

def ddur_078_days_since_fcf_ath(fcf: pd.Series) -> pd.Series:
    """ddur_078_days_since_fcf_ath"""
    return _days_since_expanding_high(fcf)

def ddur_079_days_since_assets_ath(assets: pd.Series) -> pd.Series:
    """ddur_079_days_since_assets_ath"""
    return _days_since_expanding_high(assets)

def ddur_080_days_since_working_capital_ath(workingcapital: pd.Series) -> pd.Series:
    """ddur_080_days_since_working_capital_ath"""
    return _days_since_expanding_high(workingcapital)

def ddur_081_days_since_gross_margin_ath(grossmargin: pd.Series) -> pd.Series:
    """ddur_081_days_since_gross_margin_ath"""
    return _days_since_expanding_high(grossmargin)

def ddur_082_days_since_operating_margin_ath(opmargin: pd.Series) -> pd.Series:
    """ddur_082_days_since_operating_margin_ath"""
    return _days_since_expanding_high(opmargin)

def ddur_083_days_since_ps_ratio_ath(close: pd.Series, revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_083_days_since_ps_ratio_ath"""
    ps = (close * sharesbas) / revenue
    return _days_since_expanding_high(ps)

def ddur_084_days_since_pb_ratio_ath(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """ddur_084_days_since_pb_ratio_ath"""
    pb = close / (equity / sharesbas)
    return _days_since_expanding_high(pb)

def ddur_085_days_since_ev_revenue_ath(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """ddur_085_days_since_ev_revenue_ath"""
    ev = (close * sharesbas) + debt - cashnequiv
    return _days_since_expanding_high(ev / revenue)


# 086-105: Acceleration/Dynamics of duration

def ddur_086_days_since_high_acceleration_63d(close: pd.Series) -> pd.Series:
    """ddur_086_days_since_high_acceleration_63d feature"""
    dsh = _days_since_high(close, 252)
    return dsh.diff(63)

def ddur_087_days_since_high_velocity_21d(close: pd.Series) -> pd.Series:
    """ddur_087_days_since_high_velocity_21d"""
    dsh = _days_since_high(close, 252)
    return dsh.diff(21)

def ddur_088_days_since_high_rolling_std_252d(close: pd.Series) -> pd.Series:
    """ddur_088_days_since_high_rolling_std_252d"""
    dsh = _days_since_high(close, 252)
    return dsh.rolling(252).std()

def ddur_089_days_since_high_vs_mean_252d(close: pd.Series) -> pd.Series:
    """ddur_089_days_since_high_vs_mean_252d"""
    dsh = _days_since_high(close, 252)
    return dsh - dsh.rolling(252).mean()

def ddur_090_days_since_high_to_max_duration_ratio_ath(close: pd.Series) -> pd.Series:
    """ddur_090_days_since_high_to_max_duration_ratio_ath"""
    dsh = _days_since_expanding_high(close)
    return dsh / dsh.cummax()


# 091-110: Duration relative to volatility and regime

def ddur_091_duration_to_vol_adjusted_ath(close: pd.Series) -> pd.Series:
    """ddur_091_duration_to_vol_adjusted_ath feature"""
    dsh = _days_since_expanding_high(close)
    vol = close.pct_change().expanding().std() * np.sqrt(252)
    return dsh * vol

def ddur_092_duration_to_drawdown_depth_ratio_252d(close: pd.Series) -> pd.Series:
    """ddur_092_duration_to_drawdown_depth_ratio_252d"""
    dsh = _days_since_high(close, 252)
    h = _rolling_max(close, 252)
    dd = (h - close) / h
    return _safe_div(dsh, dd)

def ddur_093_duration_to_drawdown_depth_ratio_ath(close: pd.Series) -> pd.Series:
    """ddur_093_duration_to_drawdown_depth_ratio_ath"""
    dsh = _days_since_expanding_high(close)
    h = close.cummax()
    dd = (h - close) / h
    return _safe_div(dsh, dd)

def ddur_094_days_since_high_norm_by_ath_duration(close: pd.Series) -> pd.Series:
    """ddur_094_days_since_high_norm_by_ath_duration"""
    dsh = _days_since_high(close, 252)
    max_dsh = _days_since_expanding_high(close).cummax()
    return _safe_div(dsh, max_dsh)

def ddur_095_days_since_last_recovery_ath(close: pd.Series) -> pd.Series:
    """ddur_095_days_since_last_recovery_ath"""
    # Days since close last was >= prior high
    h = close.cummax()
    is_recovery = (close >= h.shift(1))
    indices = pd.Series(np.arange(len(close)), index=close.index).where(is_recovery).ffill()
    return pd.Series(np.arange(len(close)), index=close.index) - indices


# 111-130: Time-weighted drawdown areas

def ddur_111_time_weighted_drawdown_252d(close: pd.Series) -> pd.Series:
    """ddur_111_time_weighted_drawdown_252d feature"""
    h = _rolling_max(close, 252)
    dd = (h - close) / h
    dsh = _days_since_high(close, 252)
    return dd * dsh

def ddur_112_time_weighted_drawdown_ath(close: pd.Series) -> pd.Series:
    """ddur_112_time_weighted_drawdown_ath"""
    h = close.cummax()
    dd = (h - close) / h
    dsh = _days_since_expanding_high(close)
    return dd * dsh

def ddur_113_integral_of_drawdown_depth_63d(close: pd.Series) -> pd.Series:
    """ddur_113_integral_of_drawdown_depth_63d"""
    h = _rolling_max(close, 63)
    dd = (h - close) / h
    return dd.rolling(63).sum()

def ddur_114_integral_of_drawdown_depth_252d(close: pd.Series) -> pd.Series:
    """ddur_114_integral_of_drawdown_depth_252d"""
    h = _rolling_max(close, 252)
    dd = (h - close) / h
    return dd.rolling(252).sum()

def ddur_115_duration_decay_index_252d(close: pd.Series) -> pd.Series:
    """ddur_115_duration_decay_index_252d"""
    # exponential decay of being in drawdown
    dsh = _days_since_high(close, 252)
    return np.exp(-dsh / 252.0)


# 131-150: Final set of duration features

def ddur_131_days_since_last_52w_high(close: pd.Series) -> pd.Series:
    """ddur_131_days_since_last_52w_high feature"""
    return _days_since_high(close, 252)

def ddur_132_days_since_last_52w_low(close: pd.Series) -> pd.Series:
    """ddur_132_days_since_last_52w_low"""
    return _days_since_high(-close, 252)

def ddur_133_days_since_last_3y_high(close: pd.Series) -> pd.Series:
    """ddur_133_days_since_last_3y_high"""
    return _days_since_high(close, 252 * 3)

def ddur_134_days_since_last_3y_low(close: pd.Series) -> pd.Series:
    """ddur_134_days_since_last_3y_low"""
    return _days_since_high(-close, 252 * 3)

def ddur_135_days_since_last_5y_high(close: pd.Series) -> pd.Series:
    """ddur_135_days_since_last_5y_high"""
    return _days_since_high(close, 252 * 5)

def ddur_136_days_since_last_5y_low(close: pd.Series) -> pd.Series:
    """ddur_136_days_since_last_5y_low"""
    return _days_since_high(-close, 252 * 5)

def ddur_137_ratio_days_since_high_to_days_since_low_252d(close: pd.Series) -> pd.Series:
    """ddur_137_ratio_days_since_high_to_days_since_low_252d"""
    return _safe_div(_days_since_high(close, 252), _days_since_high(-close, 252))

def ddur_138_ratio_days_since_high_to_days_since_low_ath(close: pd.Series) -> pd.Series:
    """ddur_138_ratio_days_since_high_to_days_since_low_ath"""
    return _safe_div(_days_since_expanding_high(close), _days_since_expanding_high(-close))

def ddur_139_days_under_ma_50_last_252d(close: pd.Series) -> pd.Series:
    """ddur_139_days_under_ma_50_last_252d"""
    ma = _rolling_mean(close, 50)
    return (close < ma).rolling(252).sum()

def ddur_140_days_under_ma_200_last_252d(close: pd.Series) -> pd.Series:
    """ddur_140_days_under_ma_200_last_252d"""
    ma = _rolling_mean(close, 200)
    return (close < ma).rolling(252).sum()

def ddur_141_days_since_last_insider_sell_ath(insider_sells: pd.Series) -> pd.Series:
    """ddur_141_days_since_last_insider_sell_ath"""
    indices = pd.Series(np.arange(len(insider_sells)), index=insider_sells.index).where(insider_sells > 0).ffill()
    return pd.Series(np.arange(len(insider_sells)), index=insider_sells.index) - indices

def ddur_142_days_since_last_inst_holder_increase(inst_holders: pd.Series) -> pd.Series:
    """ddur_142_days_since_last_inst_holder_increase"""
    diff = inst_holders.diff()
    indices = pd.Series(np.arange(len(inst_holders)), index=inst_holders.index).where(diff > 0).ffill()
    return pd.Series(np.arange(len(inst_holders)), index=inst_holders.index) - indices

def ddur_143_days_since_last_inst_holder_decrease(inst_holders: pd.Series) -> pd.Series:
    """ddur_143_days_since_last_inst_holder_decrease"""
    diff = inst_holders.diff()
    indices = pd.Series(np.arange(len(inst_holders)), index=inst_holders.index).where(diff < 0).ffill()
    return pd.Series(np.arange(len(inst_holders)), index=inst_holders.index) - indices

def ddur_144_days_since_last_share_buyback(sharesbas: pd.Series) -> pd.Series:
    """ddur_144_days_since_last_share_buyback"""
    diff = sharesbas.diff()
    indices = pd.Series(np.arange(len(sharesbas)), index=sharesbas.index).where(diff < 0).ffill()
    return pd.Series(np.arange(len(sharesbas)), index=sharesbas.index) - indices

def ddur_145_days_since_last_share_issuance(sharesbas: pd.Series) -> pd.Series:
    """ddur_145_days_since_last_share_issuance"""
    diff = sharesbas.diff()
    indices = pd.Series(np.arange(len(sharesbas)), index=sharesbas.index).where(diff > 0).ffill()
    return pd.Series(np.arange(len(sharesbas)), index=sharesbas.index) - indices

def ddur_146_days_since_last_positive_earnings_surprise(surprise: pd.Series) -> pd.Series:
    """ddur_146_days_since_last_positive_earnings_surprise"""
    # Assuming surprise is a series of actual-estimate values
    indices = pd.Series(np.arange(len(surprise)), index=surprise.index).where(surprise > 0).ffill()
    return pd.Series(np.arange(len(surprise)), index=surprise.index) - indices

def ddur_147_days_since_last_negative_earnings_surprise(surprise: pd.Series) -> pd.Series:
    """ddur_147_days_since_last_negative_earnings_surprise"""
    indices = pd.Series(np.arange(len(surprise)), index=surprise.index).where(surprise < 0).ffill()
    return pd.Series(np.arange(len(surprise)), index=surprise.index) - indices

def ddur_148_days_since_ath_duration_zscore_5y(close: pd.Series) -> pd.Series:
    """ddur_148_days_since_ath_duration_zscore_5y"""
    dsh = _days_since_expanding_high(close)
    return (dsh - _rolling_mean(dsh, 1260)) / _rolling_std(dsh, 1260)

def ddur_149_days_since_ath_duration_pct_rank_5y(close: pd.Series) -> pd.Series:
    """ddur_149_days_since_ath_duration_pct_rank_5y"""
    dsh = _days_since_expanding_high(close)
    return dsh.rolling(1260).rank(pct=True)

def ddur_150_days_since_ath_composite_score(close: pd.Series) -> pd.Series:
    """ddur_150_days_since_ath_composite_score"""
    dsh = _days_since_expanding_high(close)
    d252 = _days_since_high(close, 252)
    return (0.7 * dsh + 0.3 * d252)

def ddur_117_variation_0(ebitda: pd.Series) -> pd.Series:
    """zscore variation of ddur_076_days_since_ebitda_ath"""
    base_feat = ddur_076_days_since_ebitda_ath(ebitda)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_118_variation_1(netinc: pd.Series) -> pd.Series:
    """rank variation of ddur_077_days_since_netinc_ath"""
    base_feat = ddur_077_days_since_netinc_ath(netinc)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_119_variation_2(fcf: pd.Series) -> pd.Series:
    """zscore variation of ddur_078_days_since_fcf_ath"""
    base_feat = ddur_078_days_since_fcf_ath(fcf)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_120_variation_3(assets: pd.Series) -> pd.Series:
    """rank variation of ddur_079_days_since_assets_ath"""
    base_feat = ddur_079_days_since_assets_ath(assets)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_121_variation_4(workingcapital: pd.Series) -> pd.Series:
    """zscore variation of ddur_080_days_since_working_capital_ath"""
    base_feat = ddur_080_days_since_working_capital_ath(workingcapital)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_122_variation_5(grossmargin: pd.Series) -> pd.Series:
    """rank variation of ddur_081_days_since_gross_margin_ath"""
    base_feat = ddur_081_days_since_gross_margin_ath(grossmargin)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_123_variation_6(opmargin: pd.Series) -> pd.Series:
    """zscore variation of ddur_082_days_since_operating_margin_ath"""
    base_feat = ddur_082_days_since_operating_margin_ath(opmargin)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_124_variation_7(close: pd.Series, revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """rank variation of ddur_083_days_since_ps_ratio_ath"""
    base_feat = ddur_083_days_since_ps_ratio_ath(close,revenue,sharesbas)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_125_variation_8(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """zscore variation of ddur_084_days_since_pb_ratio_ath"""
    base_feat = ddur_084_days_since_pb_ratio_ath(close,equity,sharesbas)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_126_variation_9(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """rank variation of ddur_085_days_since_ev_revenue_ath"""
    base_feat = ddur_085_days_since_ev_revenue_ath(close,sharesbas,debt,cashnequiv,revenue)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_127_variation_10(ebitda: pd.Series) -> pd.Series:
    """zscore variation of ddur_076_days_since_ebitda_ath"""
    base_feat = ddur_076_days_since_ebitda_ath(ebitda)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_128_variation_11(netinc: pd.Series) -> pd.Series:
    """rank variation of ddur_077_days_since_netinc_ath"""
    base_feat = ddur_077_days_since_netinc_ath(netinc)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_129_variation_12(fcf: pd.Series) -> pd.Series:
    """zscore variation of ddur_078_days_since_fcf_ath"""
    base_feat = ddur_078_days_since_fcf_ath(fcf)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_130_variation_13(assets: pd.Series) -> pd.Series:
    """rank variation of ddur_079_days_since_assets_ath"""
    base_feat = ddur_079_days_since_assets_ath(assets)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_131_variation_14(workingcapital: pd.Series) -> pd.Series:
    """zscore variation of ddur_080_days_since_working_capital_ath"""
    base_feat = ddur_080_days_since_working_capital_ath(workingcapital)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_132_variation_15(grossmargin: pd.Series) -> pd.Series:
    """rank variation of ddur_081_days_since_gross_margin_ath"""
    base_feat = ddur_081_days_since_gross_margin_ath(grossmargin)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_133_variation_16(opmargin: pd.Series) -> pd.Series:
    """zscore variation of ddur_082_days_since_operating_margin_ath"""
    base_feat = ddur_082_days_since_operating_margin_ath(opmargin)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_134_variation_17(close: pd.Series, revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """rank variation of ddur_083_days_since_ps_ratio_ath"""
    base_feat = ddur_083_days_since_ps_ratio_ath(close,revenue,sharesbas)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_135_variation_18(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """zscore variation of ddur_084_days_since_pb_ratio_ath"""
    base_feat = ddur_084_days_since_pb_ratio_ath(close,equity,sharesbas)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_136_variation_19(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """rank variation of ddur_085_days_since_ev_revenue_ath"""
    base_feat = ddur_085_days_since_ev_revenue_ath(close,sharesbas,debt,cashnequiv,revenue)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_137_variation_20(ebitda: pd.Series) -> pd.Series:
    """zscore variation of ddur_076_days_since_ebitda_ath"""
    base_feat = ddur_076_days_since_ebitda_ath(ebitda)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_138_variation_21(netinc: pd.Series) -> pd.Series:
    """rank variation of ddur_077_days_since_netinc_ath"""
    base_feat = ddur_077_days_since_netinc_ath(netinc)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_139_variation_22(fcf: pd.Series) -> pd.Series:
    """zscore variation of ddur_078_days_since_fcf_ath"""
    base_feat = ddur_078_days_since_fcf_ath(fcf)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_140_variation_23(assets: pd.Series) -> pd.Series:
    """rank variation of ddur_079_days_since_assets_ath"""
    base_feat = ddur_079_days_since_assets_ath(assets)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_141_variation_24(workingcapital: pd.Series) -> pd.Series:
    """zscore variation of ddur_080_days_since_working_capital_ath"""
    base_feat = ddur_080_days_since_working_capital_ath(workingcapital)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_142_variation_25(grossmargin: pd.Series) -> pd.Series:
    """rank variation of ddur_081_days_since_gross_margin_ath"""
    base_feat = ddur_081_days_since_gross_margin_ath(grossmargin)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_143_variation_26(opmargin: pd.Series) -> pd.Series:
    """zscore variation of ddur_082_days_since_operating_margin_ath"""
    base_feat = ddur_082_days_since_operating_margin_ath(opmargin)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_144_variation_27(close: pd.Series, revenue: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """rank variation of ddur_083_days_since_ps_ratio_ath"""
    base_feat = ddur_083_days_since_ps_ratio_ath(close,revenue,sharesbas)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_145_variation_28(close: pd.Series, equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """zscore variation of ddur_084_days_since_pb_ratio_ath"""
    base_feat = ddur_084_days_since_pb_ratio_ath(close,equity,sharesbas)
    if "zscore" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

def ddur_146_variation_29(close: pd.Series, sharesbas: pd.Series, debt: pd.Series, cashnequiv: pd.Series, revenue: pd.Series) -> pd.Series:
    """rank variation of ddur_085_days_since_ev_revenue_ath"""
    base_feat = ddur_085_days_since_ev_revenue_ath(close,sharesbas,debt,cashnequiv,revenue)
    if "rank" == "zscore":
        return _zscore_rolling(base_feat, _TD_YEAR)
    else:
        return _rank_pct(base_feat, _TD_YEAR)

# ── Registry ──────────────────────────────────────────────────────────────────

V02_REGISTRY = {
    "ddur_076_days_since_ebitda_ath": {"inputs": ["ebitda"], "func": ddur_076_days_since_ebitda_ath},
    "ddur_077_days_since_netinc_ath": {"inputs": ["netinc"], "func": ddur_077_days_since_netinc_ath},
    "ddur_078_days_since_fcf_ath": {"inputs": ["fcf"], "func": ddur_078_days_since_fcf_ath},
    "ddur_079_days_since_assets_ath": {"inputs": ["assets"], "func": ddur_079_days_since_assets_ath},
    "ddur_080_days_since_working_capital_ath": {"inputs": ["workingcapital"], "func": ddur_080_days_since_working_capital_ath},
    "ddur_081_days_since_gross_margin_ath": {"inputs": ["grossmargin"], "func": ddur_081_days_since_gross_margin_ath},
    "ddur_082_days_since_operating_margin_ath": {"inputs": ["opmargin"], "func": ddur_082_days_since_operating_margin_ath},
    "ddur_083_days_since_ps_ratio_ath": {"inputs": ["close", "revenue", "sharesbas"], "func": ddur_083_days_since_ps_ratio_ath},
    "ddur_084_days_since_pb_ratio_ath": {"inputs": ["close", "equity", "sharesbas"], "func": ddur_084_days_since_pb_ratio_ath},
    "ddur_085_days_since_ev_revenue_ath": {"inputs": ["close", "sharesbas", "debt", "cashnequiv", "revenue"], "func": ddur_085_days_since_ev_revenue_ath},
    "ddur_086_days_since_high_acceleration_63d": {"inputs": ["close"], "func": ddur_086_days_since_high_acceleration_63d},
    "ddur_087_days_since_high_velocity_21d": {"inputs": ["close"], "func": ddur_087_days_since_high_velocity_21d},
    "ddur_088_days_since_high_rolling_std_252d": {"inputs": ["close"], "func": ddur_088_days_since_high_rolling_std_252d},
    "ddur_089_days_since_high_vs_mean_252d": {"inputs": ["close"], "func": ddur_089_days_since_high_vs_mean_252d},
    "ddur_090_days_since_high_to_max_duration_ratio_ath": {"inputs": ["close"], "func": ddur_090_days_since_high_to_max_duration_ratio_ath},
    "ddur_091_duration_to_vol_adjusted_ath": {"inputs": ["close"], "func": ddur_091_duration_to_vol_adjusted_ath},
    "ddur_092_duration_to_drawdown_depth_ratio_252d": {"inputs": ["close"], "func": ddur_092_duration_to_drawdown_depth_ratio_252d},
    "ddur_093_duration_to_drawdown_depth_ratio_ath": {"inputs": ["close"], "func": ddur_093_duration_to_drawdown_depth_ratio_ath},
    "ddur_094_days_since_high_norm_by_ath_duration": {"inputs": ["close"], "func": ddur_094_days_since_high_norm_by_ath_duration},
    "ddur_095_days_since_last_recovery_ath": {"inputs": ["close"], "func": ddur_095_days_since_last_recovery_ath},
    "ddur_111_time_weighted_drawdown_252d": {"inputs": ["close"], "func": ddur_111_time_weighted_drawdown_252d},
    "ddur_112_time_weighted_drawdown_ath": {"inputs": ["close"], "func": ddur_112_time_weighted_drawdown_ath},
    "ddur_113_integral_of_drawdown_depth_63d": {"inputs": ["close"], "func": ddur_113_integral_of_drawdown_depth_63d},
    "ddur_114_integral_of_drawdown_depth_252d": {"inputs": ["close"], "func": ddur_114_integral_of_drawdown_depth_252d},
    "ddur_115_duration_decay_index_252d": {"inputs": ["close"], "func": ddur_115_duration_decay_index_252d},
    "ddur_131_days_since_last_52w_high": {"inputs": ["close"], "func": ddur_131_days_since_last_52w_high},
    "ddur_132_days_since_last_52w_low": {"inputs": ["close"], "func": ddur_132_days_since_last_52w_low},
    "ddur_133_days_since_last_3y_high": {"inputs": ["close"], "func": ddur_133_days_since_last_3y_high},
    "ddur_134_days_since_last_3y_low": {"inputs": ["close"], "func": ddur_134_days_since_last_3y_low},
    "ddur_135_days_since_last_5y_high": {"inputs": ["close"], "func": ddur_135_days_since_last_5y_high},
    "ddur_136_days_since_last_5y_low": {"inputs": ["close"], "func": ddur_136_days_since_last_5y_low},
    "ddur_137_ratio_days_since_high_to_days_since_low_252d": {"inputs": ["close"], "func": ddur_137_ratio_days_since_high_to_days_since_low_252d},
    "ddur_138_ratio_days_since_high_to_days_since_low_ath": {"inputs": ["close"], "func": ddur_138_ratio_days_since_high_to_days_since_low_ath},
    "ddur_139_days_under_ma_50_last_252d": {"inputs": ["close"], "func": ddur_139_days_under_ma_50_last_252d},
    "ddur_140_days_under_ma_200_last_252d": {"inputs": ["close"], "func": ddur_140_days_under_ma_200_last_252d},
    "ddur_141_days_since_last_insider_sell_ath": {"inputs": ["insider_sells"], "func": ddur_141_days_since_last_insider_sell_ath},
    "ddur_142_days_since_last_inst_holder_increase": {"inputs": ["inst_holders"], "func": ddur_142_days_since_last_inst_holder_increase},
    "ddur_143_days_since_last_inst_holder_decrease": {"inputs": ["inst_holders"], "func": ddur_143_days_since_last_inst_holder_decrease},
    "ddur_144_days_since_last_share_buyback": {"inputs": ["sharesbas"], "func": ddur_144_days_since_last_share_buyback},
    "ddur_145_days_since_last_share_issuance": {"inputs": ["sharesbas"], "func": ddur_145_days_since_last_share_issuance},
    "ddur_146_days_since_last_positive_earnings_surprise": {"inputs": ["surprise"], "func": ddur_146_days_since_last_positive_earnings_surprise},
    "ddur_147_days_since_last_negative_earnings_surprise": {"inputs": ["surprise"], "func": ddur_147_days_since_last_negative_earnings_surprise},
    "ddur_148_days_since_ath_duration_zscore_5y": {"inputs": ["close"], "func": ddur_148_days_since_ath_duration_zscore_5y},
    "ddur_149_days_since_ath_duration_pct_rank_5y": {"inputs": ["close"], "func": ddur_149_days_since_ath_duration_pct_rank_5y},
    "ddur_150_days_since_ath_composite_score": {"inputs": ["close"], "func": ddur_150_days_since_ath_composite_score},
    "ddur_117_variation_0": {"inputs": ["ebitda"], "func": ddur_117_variation_0},
    "ddur_118_variation_1": {"inputs": ["netinc"], "func": ddur_118_variation_1},
    "ddur_119_variation_2": {"inputs": ["fcf"], "func": ddur_119_variation_2},
    "ddur_120_variation_3": {"inputs": ["assets"], "func": ddur_120_variation_3},
    "ddur_121_variation_4": {"inputs": ["workingcapital"], "func": ddur_121_variation_4},
    "ddur_122_variation_5": {"inputs": ["grossmargin"], "func": ddur_122_variation_5},
    "ddur_123_variation_6": {"inputs": ["opmargin"], "func": ddur_123_variation_6},
    "ddur_124_variation_7": {"inputs": ["close", "revenue", "sharesbas"], "func": ddur_124_variation_7},
    "ddur_125_variation_8": {"inputs": ["close", "equity", "sharesbas"], "func": ddur_125_variation_8},
    "ddur_126_variation_9": {"inputs": ["close", "sharesbas", "debt", "cashnequiv", "revenue"], "func": ddur_126_variation_9},
    "ddur_127_variation_10": {"inputs": ["ebitda"], "func": ddur_127_variation_10},
    "ddur_128_variation_11": {"inputs": ["netinc"], "func": ddur_128_variation_11},
    "ddur_129_variation_12": {"inputs": ["fcf"], "func": ddur_129_variation_12},
    "ddur_130_variation_13": {"inputs": ["assets"], "func": ddur_130_variation_13},
    "ddur_131_variation_14": {"inputs": ["workingcapital"], "func": ddur_131_variation_14},
    "ddur_132_variation_15": {"inputs": ["grossmargin"], "func": ddur_132_variation_15},
    "ddur_133_variation_16": {"inputs": ["opmargin"], "func": ddur_133_variation_16},
    "ddur_134_variation_17": {"inputs": ["close", "revenue", "sharesbas"], "func": ddur_134_variation_17},
    "ddur_135_variation_18": {"inputs": ["close", "equity", "sharesbas"], "func": ddur_135_variation_18},
    "ddur_136_variation_19": {"inputs": ["close", "sharesbas", "debt", "cashnequiv", "revenue"], "func": ddur_136_variation_19},
    "ddur_137_variation_20": {"inputs": ["ebitda"], "func": ddur_137_variation_20},
    "ddur_138_variation_21": {"inputs": ["netinc"], "func": ddur_138_variation_21},
    "ddur_139_variation_22": {"inputs": ["fcf"], "func": ddur_139_variation_22},
    "ddur_140_variation_23": {"inputs": ["assets"], "func": ddur_140_variation_23},
    "ddur_141_variation_24": {"inputs": ["workingcapital"], "func": ddur_141_variation_24},
    "ddur_142_variation_25": {"inputs": ["grossmargin"], "func": ddur_142_variation_25},
    "ddur_143_variation_26": {"inputs": ["opmargin"], "func": ddur_143_variation_26},
    "ddur_144_variation_27": {"inputs": ["close", "revenue", "sharesbas"], "func": ddur_144_variation_27},
    "ddur_145_variation_28": {"inputs": ["close", "equity", "sharesbas"], "func": ddur_145_variation_28},
    "ddur_146_variation_29": {"inputs": ["close", "sharesbas", "debt", "cashnequiv", "revenue"], "func": ddur_146_variation_29},
}
