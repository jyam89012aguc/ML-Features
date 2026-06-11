"""
124_cross_sectional_distress_rank — Base Features 076-150
Domain: cross-sectional distress rank — how distressed is this name vs sector/industry
        peers across MULTIPLE distress dimensions (drawdown, volatility, valuation
        compression, leverage, momentum)
Asset class: US equities | Daily price/volume + fundamental inputs (SEP + SF1-derived)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily pd.Series for a given field AND
    a precomputed peer-median Series of the SAME daily DatetimeIndex named
    peer_median_<field>.  The pipeline computes sector/industry medians universe-wide
    and passes them in.  All functions are strictly backward-looking.

Own inputs:      close, drawdown, realized_vol, rsi14, marketcap,
                 debt_to_equity, fcf_yield, pb, ps
Peer-median:     peer_median_drawdown, peer_median_realized_vol, peer_median_rsi14,
                 peer_median_marketcap, peer_median_debt_to_equity,
                 peer_median_fcf_yield, peer_median_pb, peer_median_ps
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y   = 504
_TD_HALF = 126
_TD_QTR  = 63
_TD_MON  = 21
_TD_WEEK = 5
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/near-zero denominator with NaN."""
    d = den.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return num / d


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 2)).std()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    """own / peer_median ratio; NaN where peer is near-zero."""
    return _safe_div(own, peer)


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    """log(own / peer) — signed log-relative deviation."""
    ratio = _rel_ratio(own, peer)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def _gap(own: pd.Series, peer: pd.Series) -> pd.Series:
    """Arithmetic gap: own - peer_median."""
    return own - peer


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _consec_streak(cond: pd.Series) -> pd.Series:
    """Count consecutive True values up to each row (backward-looking)."""
    c = cond.astype(int)
    group = (~cond).cumsum()
    streak = c.groupby(group).cumsum()
    return streak.astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        if len(x) < max(2, w // 2):
            return np.nan
        xi = np.arange(len(x), dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-087): Drawdown temporal dynamics vs peers ---

def xdr_076_drawdown_gap_5d_change(drawdown: pd.Series,
                                    peer_median_drawdown: pd.Series) -> pd.Series:
    """5-day change in drawdown gap (own - peer); negative = rapidly worsening vs peers."""
    return _gap(drawdown, peer_median_drawdown).diff(_TD_WEEK)


def xdr_077_drawdown_gap_21d_change(drawdown: pd.Series,
                                     peer_median_drawdown: pd.Series) -> pd.Series:
    """21-day change in drawdown gap."""
    return _gap(drawdown, peer_median_drawdown).diff(_TD_MON)


def xdr_078_drawdown_ratio_5d_change(drawdown: pd.Series,
                                      peer_median_drawdown: pd.Series) -> pd.Series:
    """5-day change in drawdown ratio (own/peer)."""
    return _rel_ratio(drawdown, peer_median_drawdown).diff(_TD_WEEK)


def xdr_079_drawdown_ratio_slope_21d(drawdown: pd.Series,
                                      peer_median_drawdown: pd.Series) -> pd.Series:
    """OLS slope of drawdown ratio over 21 days (trend in relative drawdown)."""
    return _linslope(_rel_ratio(drawdown, peer_median_drawdown), _TD_MON)


def xdr_080_drawdown_ratio_slope_63d(drawdown: pd.Series,
                                      peer_median_drawdown: pd.Series) -> pd.Series:
    """OLS slope of drawdown ratio over 63 days."""
    return _linslope(_rel_ratio(drawdown, peer_median_drawdown), _TD_QTR)


def xdr_081_drawdown_gap_ewm_21d(drawdown: pd.Series,
                                   peer_median_drawdown: pd.Series) -> pd.Series:
    """21-day EMA of drawdown gap (smoothed relative drawdown position)."""
    return _ewm_mean(_gap(drawdown, peer_median_drawdown), _TD_MON)


def xdr_082_drawdown_gap_ewm_63d(drawdown: pd.Series,
                                   peer_median_drawdown: pd.Series) -> pd.Series:
    """63-day EMA of drawdown gap."""
    return _ewm_mean(_gap(drawdown, peer_median_drawdown), _TD_QTR)


def xdr_083_drawdown_ratio_zscore_half(drawdown: pd.Series,
                                        peer_median_drawdown: pd.Series) -> pd.Series:
    """Z-score of drawdown ratio within trailing 126-day (half-year) window."""
    return _zscore_rolling(_rel_ratio(drawdown, peer_median_drawdown), _TD_HALF)


def xdr_084_drawdown_below_peer_pct_252d(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where ticker drawdown is worse than peer median."""
    flag = (drawdown < peer_median_drawdown).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def xdr_085_drawdown_below_peer_pct_126d(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days where ticker drawdown is worse than peer median."""
    flag = (drawdown < peer_median_drawdown).astype(float)
    return _rolling_sum(flag, _TD_HALF) / _TD_HALF


def xdr_086_drawdown_ratio_expanding_min(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series) -> pd.Series:
    """Expanding all-time minimum of drawdown ratio (how extreme vs peers ever gotten)."""
    return _rel_ratio(drawdown, peer_median_drawdown).expanding(min_periods=_TD_QTR).min()


def xdr_087_drawdown_current_vs_expanding_min(drawdown: pd.Series,
                                               peer_median_drawdown: pd.Series) -> pd.Series:
    """Current drawdown ratio divided by expanding min ratio (1.0 = at all-time worst vs peers)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    exp_min = ratio.expanding(min_periods=_TD_QTR).min()
    return _safe_div(ratio, exp_min.abs())


# --- Group I (088-099): Volatility temporal dynamics vs peers ---

def xdr_088_vol_ratio_5d_change(realized_vol: pd.Series,
                                  peer_median_realized_vol: pd.Series) -> pd.Series:
    """5-day change in vol ratio (own/peer): rising = volatility stress worsening vs peers."""
    return _rel_ratio(realized_vol, peer_median_realized_vol).diff(_TD_WEEK)


def xdr_089_vol_ratio_21d_change(realized_vol: pd.Series,
                                   peer_median_realized_vol: pd.Series) -> pd.Series:
    """21-day change in vol ratio vs peers."""
    return _rel_ratio(realized_vol, peer_median_realized_vol).diff(_TD_MON)


def xdr_090_vol_ratio_slope_21d(realized_vol: pd.Series,
                                  peer_median_realized_vol: pd.Series) -> pd.Series:
    """OLS slope of vol ratio over 21 days."""
    return _linslope(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_MON)


def xdr_091_vol_ratio_slope_63d(realized_vol: pd.Series,
                                  peer_median_realized_vol: pd.Series) -> pd.Series:
    """OLS slope of vol ratio over 63 days."""
    return _linslope(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_QTR)


def xdr_092_vol_above_peer_pct_252d(realized_vol: pd.Series,
                                     peer_median_realized_vol: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where ticker vol exceeded peer median."""
    flag = (realized_vol > peer_median_realized_vol).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def xdr_093_vol_above_peer_pct_63d(realized_vol: pd.Series,
                                    peer_median_realized_vol: pd.Series) -> pd.Series:
    """Fraction of trailing 63 days where ticker vol exceeded peer median."""
    flag = (realized_vol > peer_median_realized_vol).astype(float)
    return _rolling_sum(flag, _TD_QTR) / _TD_QTR


def xdr_094_vol_ratio_ewm_21d(realized_vol: pd.Series,
                                peer_median_realized_vol: pd.Series) -> pd.Series:
    """21-day EMA of vol ratio."""
    return _ewm_mean(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_MON)


def xdr_095_vol_ratio_expanding_max(realized_vol: pd.Series,
                                     peer_median_realized_vol: pd.Series) -> pd.Series:
    """Expanding all-time maximum of vol ratio (worst historical vol stress vs peers)."""
    return _rel_ratio(realized_vol, peer_median_realized_vol).expanding(min_periods=_TD_QTR).max()


def xdr_096_vol_current_vs_expanding_max(realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series) -> pd.Series:
    """Current vol ratio / expanding max (1.0 = at all-time peak vol vs peers)."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    exp_max = ratio.expanding(min_periods=_TD_QTR).max()
    return _safe_div(ratio, exp_max.clip(lower=_EPS))


def xdr_097_vol_ratio_half_yr_zscore(realized_vol: pd.Series,
                                      peer_median_realized_vol: pd.Series) -> pd.Series:
    """Z-score of vol ratio within trailing 126-day window."""
    return _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_HALF)


def xdr_098_vol_gap_zscore_63d(realized_vol: pd.Series,
                                 peer_median_realized_vol: pd.Series) -> pd.Series:
    """Z-score of arithmetic vol gap within 63-day window."""
    return _zscore_rolling(_gap(realized_vol, peer_median_realized_vol), _TD_QTR)


def xdr_099_vol_gap_zscore_252d(realized_vol: pd.Series,
                                  peer_median_realized_vol: pd.Series) -> pd.Series:
    """Z-score of arithmetic vol gap within 252-day window."""
    return _zscore_rolling(_gap(realized_vol, peer_median_realized_vol), _TD_YEAR)


# --- Group J (100-110): RSI / momentum temporal dynamics vs peers ---

def xdr_100_rsi14_peer_gap_5d_change(rsi14: pd.Series,
                                      peer_median_rsi14: pd.Series) -> pd.Series:
    """5-day change in RSI14 peer gap (deteriorating = more relative weakness)."""
    return _gap(rsi14, peer_median_rsi14).diff(_TD_WEEK)


def xdr_101_rsi14_peer_gap_21d_change(rsi14: pd.Series,
                                       peer_median_rsi14: pd.Series) -> pd.Series:
    """21-day change in RSI14 peer gap."""
    return _gap(rsi14, peer_median_rsi14).diff(_TD_MON)


def xdr_102_rsi14_peer_gap_slope_21d(rsi14: pd.Series,
                                      peer_median_rsi14: pd.Series) -> pd.Series:
    """OLS slope of RSI14 peer gap over 21 days (momentum divergence trend)."""
    return _linslope(_gap(rsi14, peer_median_rsi14), _TD_MON)


def xdr_103_rsi14_peer_gap_slope_63d(rsi14: pd.Series,
                                      peer_median_rsi14: pd.Series) -> pd.Series:
    """OLS slope of RSI14 peer gap over 63 days."""
    return _linslope(_gap(rsi14, peer_median_rsi14), _TD_QTR)


def xdr_104_rsi14_peer_gap_ewm_21d(rsi14: pd.Series,
                                    peer_median_rsi14: pd.Series) -> pd.Series:
    """21-day EMA of RSI14 peer gap (smoothed relative momentum position)."""
    return _ewm_mean(_gap(rsi14, peer_median_rsi14), _TD_MON)


def xdr_105_rsi14_peer_gap_half_yr_zscore(rsi14: pd.Series,
                                           peer_median_rsi14: pd.Series) -> pd.Series:
    """Z-score of RSI14 peer gap within 126-day window."""
    return _zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_HALF)


def xdr_106_rsi14_below_peer_frac_126d(rsi14: pd.Series,
                                        peer_median_rsi14: pd.Series) -> pd.Series:
    """Fraction of trailing 126 days where ticker RSI14 < peer median RSI14."""
    flag = (rsi14 < peer_median_rsi14).astype(float)
    return _rolling_sum(flag, _TD_HALF) / _TD_HALF


def xdr_107_rsi14_consec_below_peer_streak_max_63d(rsi14: pd.Series,
                                                     peer_median_rsi14: pd.Series) -> pd.Series:
    """63-day rolling maximum of the consecutive-below-peer-RSI14 streak."""
    streak = _consec_streak(rsi14 < peer_median_rsi14)
    return _rolling_max(streak, _TD_QTR)


def xdr_108_rsi14_peer_gap_expanding_min(rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series) -> pd.Series:
    """Expanding all-time minimum of RSI14 peer gap (worst ever relative momentum)."""
    return _gap(rsi14, peer_median_rsi14).expanding(min_periods=_TD_QTR).min()


def xdr_109_rsi14_peer_gap_expanding_pct_rank(rsi14: pd.Series,
                                               peer_median_rsi14: pd.Series) -> pd.Series:
    """Expanding all-time pct-rank of RSI14 peer gap (low = historically worst momentum vs peers)."""
    return _gap(rsi14, peer_median_rsi14).expanding(min_periods=_TD_QTR).rank(pct=True)


def xdr_110_rsi14_peer_gap_min_252d(rsi14: pd.Series,
                                     peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day rolling minimum RSI14 peer gap (worst quarter relative momentum in a year)."""
    return _rolling_min(_gap(rsi14, peer_median_rsi14), _TD_YEAR)


# --- Group K (111-122): Leverage & valuation temporal dynamics vs peers ---

def xdr_111_de_ratio_5d_change(debt_to_equity: pd.Series,
                                peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """5-day change in D/E ratio vs peers (rising = leverage distress worsening)."""
    return _rel_ratio(debt_to_equity, peer_median_debt_to_equity).diff(_TD_WEEK)


def xdr_112_de_ratio_21d_change(debt_to_equity: pd.Series,
                                 peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """21-day change in D/E ratio vs peers."""
    return _rel_ratio(debt_to_equity, peer_median_debt_to_equity).diff(_TD_MON)


def xdr_113_de_ratio_slope_63d(debt_to_equity: pd.Series,
                                peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """OLS slope of D/E ratio over 63 days."""
    return _linslope(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_QTR)


def xdr_114_de_above_peer_pct_252d(debt_to_equity: pd.Series,
                                    peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where D/E exceeded peer median."""
    flag = (debt_to_equity > peer_median_debt_to_equity).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def xdr_115_pb_ratio_5d_change(pb: pd.Series,
                                peer_median_pb: pd.Series) -> pd.Series:
    """5-day change in P/B ratio vs peers (falling = valuation compression deepening)."""
    return _rel_ratio(pb, peer_median_pb).diff(_TD_WEEK)


def xdr_116_pb_ratio_21d_change(pb: pd.Series,
                                 peer_median_pb: pd.Series) -> pd.Series:
    """21-day change in P/B ratio vs peers."""
    return _rel_ratio(pb, peer_median_pb).diff(_TD_MON)


def xdr_117_pb_ratio_slope_63d(pb: pd.Series,
                                peer_median_pb: pd.Series) -> pd.Series:
    """OLS slope of P/B ratio vs peers over 63 days."""
    return _linslope(_rel_ratio(pb, peer_median_pb), _TD_QTR)


def xdr_118_pb_below_peer_pct_252d(pb: pd.Series,
                                    peer_median_pb: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where P/B is below peer median."""
    flag = (pb < peer_median_pb).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def xdr_119_pb_ratio_expanding_min(pb: pd.Series,
                                    peer_median_pb: pd.Series) -> pd.Series:
    """Expanding all-time minimum of P/B ratio vs peers (deepest valuation compression)."""
    return _rel_ratio(pb, peer_median_pb).expanding(min_periods=_TD_QTR).min()


def xdr_120_ps_ratio_slope_63d(ps: pd.Series,
                                peer_median_ps: pd.Series) -> pd.Series:
    """OLS slope of P/S ratio vs peers over 63 days."""
    return _linslope(_rel_ratio(ps, peer_median_ps), _TD_QTR)


def xdr_121_ps_below_peer_pct_252d(ps: pd.Series,
                                    peer_median_ps: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where P/S is below peer median."""
    flag = (ps < peer_median_ps).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def xdr_122_ps_ratio_zscore_252d(ps: pd.Series,
                                  peer_median_ps: pd.Series) -> pd.Series:
    """Z-score of P/S ratio vs peers within trailing 252 days."""
    return _zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR)


# --- Group L (123-138): Cross-dimension interaction features ---

def xdr_123_drawdown_vol_both_worse_flag(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series,
                                          realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series) -> pd.Series:
    """Binary: 1 if both drawdown deeper AND vol higher than peer median."""
    return ((drawdown < peer_median_drawdown) &
            (realized_vol > peer_median_realized_vol)).astype(float)


def xdr_124_drawdown_rsi_both_worse_flag(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series,
                                          rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series) -> pd.Series:
    """Binary: 1 if both drawdown deeper AND RSI14 lower than peer median."""
    return ((drawdown < peer_median_drawdown) &
            (rsi14 < peer_median_rsi14)).astype(float)


def xdr_125_vol_leverage_both_worse_flag(realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series,
                                          debt_to_equity: pd.Series,
                                          peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Binary: 1 if vol higher AND D/E higher than peer median (risk amplification)."""
    return ((realized_vol > peer_median_realized_vol) &
            (debt_to_equity > peer_median_debt_to_equity)).astype(float)


def xdr_126_valuation_fcf_both_worse_flag(pb: pd.Series,
                                            peer_median_pb: pd.Series,
                                            fcf_yield: pd.Series,
                                            peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Binary: 1 if P/B compressed AND FCF yield below peer median."""
    return ((pb < peer_median_pb) &
            (fcf_yield < peer_median_fcf_yield)).astype(float)


def xdr_127_dual_distress_days_63d(drawdown: pd.Series,
                                    peer_median_drawdown: pd.Series,
                                    realized_vol: pd.Series,
                                    peer_median_realized_vol: pd.Series) -> pd.Series:
    """Days in trailing 63d where both drawdown worse AND vol higher than peers."""
    flag = ((drawdown < peer_median_drawdown) &
            (realized_vol > peer_median_realized_vol)).astype(float)
    return _rolling_sum(flag, _TD_QTR)


def xdr_128_triple_distress_days_252d(drawdown: pd.Series,
                                       peer_median_drawdown: pd.Series,
                                       realized_vol: pd.Series,
                                       peer_median_realized_vol: pd.Series,
                                       rsi14: pd.Series,
                                       peer_median_rsi14: pd.Series) -> pd.Series:
    """Days in trailing 252d where drawdown, vol, AND RSI all worse than peers."""
    flag = ((drawdown < peer_median_drawdown) &
            (realized_vol > peer_median_realized_vol) &
            (rsi14 < peer_median_rsi14)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def xdr_129_drawdown_gap_times_vol_ratio(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series,
                                          realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series) -> pd.Series:
    """Interaction: drawdown gap (own-peer) multiplied by vol ratio; amplifies joint distress."""
    dd_gap = _gap(drawdown, peer_median_drawdown)
    vol_ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    return dd_gap * vol_ratio


def xdr_130_rsi14_gap_times_de_ratio(rsi14: pd.Series,
                                      peer_median_rsi14: pd.Series,
                                      debt_to_equity: pd.Series,
                                      peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Interaction: RSI14 gap (own-peer) multiplied by D/E ratio; leveraged momentum distress."""
    rsi_gap = _gap(rsi14, peer_median_rsi14)
    de_ratio = _rel_ratio(debt_to_equity, peer_median_debt_to_equity)
    return rsi_gap * de_ratio


def xdr_131_all5_worse_consec_streak(drawdown: pd.Series,
                                      peer_median_drawdown: pd.Series,
                                      realized_vol: pd.Series,
                                      peer_median_realized_vol: pd.Series,
                                      rsi14: pd.Series,
                                      peer_median_rsi14: pd.Series,
                                      debt_to_equity: pd.Series,
                                      peer_median_debt_to_equity: pd.Series,
                                      fcf_yield: pd.Series,
                                      peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Consecutive days where all 5 distress dimensions are worse than peer median."""
    cond = ((drawdown < peer_median_drawdown) &
            (realized_vol > peer_median_realized_vol) &
            (rsi14 < peer_median_rsi14) &
            (debt_to_equity > peer_median_debt_to_equity) &
            (fcf_yield < peer_median_fcf_yield))
    return _consec_streak(cond)


def xdr_132_composite_z5_rolling_max_252d(drawdown: pd.Series,
                                            peer_median_drawdown: pd.Series,
                                            realized_vol: pd.Series,
                                            peer_median_realized_vol: pd.Series,
                                            rsi14: pd.Series,
                                            peer_median_rsi14: pd.Series,
                                            debt_to_equity: pd.Series,
                                            peer_median_debt_to_equity: pd.Series,
                                            fcf_yield: pd.Series,
                                            peer_median_fcf_yield: pd.Series) -> pd.Series:
    """252-day rolling maximum of 5-dim composite distress z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi + z_de + z_fcf) / 5.0
    return _rolling_max(composite, _TD_YEAR)


def xdr_133_composite_z3_ewm_21d(drawdown: pd.Series,
                                   peer_median_drawdown: pd.Series,
                                   realized_vol: pd.Series,
                                   peer_median_realized_vol: pd.Series,
                                   rsi14: pd.Series,
                                   peer_median_rsi14: pd.Series) -> pd.Series:
    """21-day EMA of 3-dim composite z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return _ewm_mean(composite, _TD_MON)


def xdr_134_composite_z3_ewm_63d(drawdown: pd.Series,
                                   peer_median_drawdown: pd.Series,
                                   realized_vol: pd.Series,
                                   peer_median_realized_vol: pd.Series,
                                   rsi14: pd.Series,
                                   peer_median_rsi14: pd.Series) -> pd.Series:
    """63-day EMA of 3-dim composite z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return _ewm_mean(composite, _TD_QTR)


def xdr_135_distress_breadth_21d(drawdown: pd.Series,
                                   peer_median_drawdown: pd.Series,
                                   realized_vol: pd.Series,
                                   peer_median_realized_vol: pd.Series,
                                   rsi14: pd.Series,
                                   peer_median_rsi14: pd.Series,
                                   debt_to_equity: pd.Series,
                                   peer_median_debt_to_equity: pd.Series,
                                   fcf_yield: pd.Series,
                                   peer_median_fcf_yield: pd.Series) -> pd.Series:
    """21-day rolling mean of 5-dim distress count (distress breadth score, 0-5)."""
    count = ((drawdown < peer_median_drawdown).astype(float) +
             (realized_vol > peer_median_realized_vol).astype(float) +
             (rsi14 < peer_median_rsi14).astype(float) +
             (debt_to_equity > peer_median_debt_to_equity).astype(float) +
             (fcf_yield < peer_median_fcf_yield).astype(float))
    return _rolling_mean(count, _TD_MON)


def xdr_136_distress_breadth_63d(drawdown: pd.Series,
                                   peer_median_drawdown: pd.Series,
                                   realized_vol: pd.Series,
                                   peer_median_realized_vol: pd.Series,
                                   rsi14: pd.Series,
                                   peer_median_rsi14: pd.Series,
                                   debt_to_equity: pd.Series,
                                   peer_median_debt_to_equity: pd.Series,
                                   fcf_yield: pd.Series,
                                   peer_median_fcf_yield: pd.Series) -> pd.Series:
    """63-day rolling mean of 5-dim distress count."""
    count = ((drawdown < peer_median_drawdown).astype(float) +
             (realized_vol > peer_median_realized_vol).astype(float) +
             (rsi14 < peer_median_rsi14).astype(float) +
             (debt_to_equity > peer_median_debt_to_equity).astype(float) +
             (fcf_yield < peer_median_fcf_yield).astype(float))
    return _rolling_mean(count, _TD_QTR)


# --- Group M (137-150): FCF, P/S, market-cap temporal dynamics vs peers ---

def xdr_137_fcf_gap_5d_change(fcf_yield: pd.Series,
                               peer_median_fcf_yield: pd.Series) -> pd.Series:
    """5-day change in FCF yield gap vs peers."""
    return _gap(fcf_yield, peer_median_fcf_yield).diff(_TD_WEEK)


def xdr_138_fcf_gap_21d_change(fcf_yield: pd.Series,
                                peer_median_fcf_yield: pd.Series) -> pd.Series:
    """21-day change in FCF yield gap vs peers."""
    return _gap(fcf_yield, peer_median_fcf_yield).diff(_TD_MON)


def xdr_139_fcf_gap_slope_63d(fcf_yield: pd.Series,
                               peer_median_fcf_yield: pd.Series) -> pd.Series:
    """OLS slope of FCF yield gap over 63 days."""
    return _linslope(_gap(fcf_yield, peer_median_fcf_yield), _TD_QTR)


def xdr_140_fcf_gap_ewm_63d(fcf_yield: pd.Series,
                             peer_median_fcf_yield: pd.Series) -> pd.Series:
    """63-day EMA of FCF yield gap vs peers."""
    return _ewm_mean(_gap(fcf_yield, peer_median_fcf_yield), _TD_QTR)


def xdr_141_marketcap_ratio_5d_change(marketcap: pd.Series,
                                       peer_median_marketcap: pd.Series) -> pd.Series:
    """5-day change in market-cap ratio vs peers (shrinkage signal)."""
    return _rel_ratio(marketcap, peer_median_marketcap).diff(_TD_WEEK)


def xdr_142_marketcap_ratio_21d_change(marketcap: pd.Series,
                                        peer_median_marketcap: pd.Series) -> pd.Series:
    """21-day change in market-cap ratio vs peers."""
    return _rel_ratio(marketcap, peer_median_marketcap).diff(_TD_MON)


def xdr_143_marketcap_ratio_slope_63d(marketcap: pd.Series,
                                       peer_median_marketcap: pd.Series) -> pd.Series:
    """OLS slope of market-cap ratio over 63 days."""
    return _linslope(_rel_ratio(marketcap, peer_median_marketcap), _TD_QTR)


def xdr_144_marketcap_below_peer_pct_252d(marketcap: pd.Series,
                                           peer_median_marketcap: pd.Series) -> pd.Series:
    """Fraction of trailing 252 days where market cap is below peer median."""
    flag = (marketcap < peer_median_marketcap).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def xdr_145_marketcap_ratio_expanding_pct_rank(marketcap: pd.Series,
                                                peer_median_marketcap: pd.Series) -> pd.Series:
    """Expanding pct-rank of market-cap ratio (historical relative size position)."""
    return _rel_ratio(marketcap, peer_median_marketcap).expanding(min_periods=_TD_QTR).rank(pct=True)


def xdr_146_pb_ps_joint_discount_flag(pb: pd.Series,
                                       peer_median_pb: pd.Series,
                                       ps: pd.Series,
                                       peer_median_ps: pd.Series) -> pd.Series:
    """Binary: 1 if both P/B and P/S are below peer median (dual valuation discount)."""
    return ((pb < peer_median_pb) & (ps < peer_median_ps)).astype(float)


def xdr_147_pb_ps_joint_discount_days_252d(pb: pd.Series,
                                            peer_median_pb: pd.Series,
                                            ps: pd.Series,
                                            peer_median_ps: pd.Series) -> pd.Series:
    """Days in trailing 252d where both P/B and P/S are below peer median."""
    flag = ((pb < peer_median_pb) & (ps < peer_median_ps)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def xdr_148_de_fcf_joint_stress_flag(debt_to_equity: pd.Series,
                                      peer_median_debt_to_equity: pd.Series,
                                      fcf_yield: pd.Series,
                                      peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Binary: 1 if D/E above peer AND FCF below peer (high-leverage low-cash-flow)."""
    return ((debt_to_equity > peer_median_debt_to_equity) &
            (fcf_yield < peer_median_fcf_yield)).astype(float)


def xdr_149_de_fcf_joint_stress_days_252d(debt_to_equity: pd.Series,
                                           peer_median_debt_to_equity: pd.Series,
                                           fcf_yield: pd.Series,
                                           peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Days in trailing 252d where D/E above AND FCF below peer median."""
    flag = ((debt_to_equity > peer_median_debt_to_equity) &
            (fcf_yield < peer_median_fcf_yield)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def xdr_150_composite_fundamental_distress_z(debt_to_equity: pd.Series,
                                              peer_median_debt_to_equity: pd.Series,
                                              fcf_yield: pd.Series,
                                              peer_median_fcf_yield: pd.Series,
                                              pb: pd.Series,
                                              peer_median_pb: pd.Series,
                                              ps: pd.Series,
                                              peer_median_ps: pd.Series) -> pd.Series:
    """4-dim fundamental distress composite z: D/E + inverted FCF + inverted P/B + inverted P/S."""
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    z_pb  = -_zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR)
    z_ps  = -_zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR)
    return (z_de + z_fcf + z_pb + z_ps) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

CROSS_SECTIONAL_DISTRESS_RANK_REGISTRY_076_150 = {
    "xdr_076_drawdown_gap_5d_change": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_076_drawdown_gap_5d_change},
    "xdr_077_drawdown_gap_21d_change": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_077_drawdown_gap_21d_change},
    "xdr_078_drawdown_ratio_5d_change": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_078_drawdown_ratio_5d_change},
    "xdr_079_drawdown_ratio_slope_21d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_079_drawdown_ratio_slope_21d},
    "xdr_080_drawdown_ratio_slope_63d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_080_drawdown_ratio_slope_63d},
    "xdr_081_drawdown_gap_ewm_21d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_081_drawdown_gap_ewm_21d},
    "xdr_082_drawdown_gap_ewm_63d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_082_drawdown_gap_ewm_63d},
    "xdr_083_drawdown_ratio_zscore_half": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_083_drawdown_ratio_zscore_half},
    "xdr_084_drawdown_below_peer_pct_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_084_drawdown_below_peer_pct_252d},
    "xdr_085_drawdown_below_peer_pct_126d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_085_drawdown_below_peer_pct_126d},
    "xdr_086_drawdown_ratio_expanding_min": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_086_drawdown_ratio_expanding_min},
    "xdr_087_drawdown_current_vs_expanding_min": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_087_drawdown_current_vs_expanding_min},
    "xdr_088_vol_ratio_5d_change": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_088_vol_ratio_5d_change},
    "xdr_089_vol_ratio_21d_change": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_089_vol_ratio_21d_change},
    "xdr_090_vol_ratio_slope_21d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_090_vol_ratio_slope_21d},
    "xdr_091_vol_ratio_slope_63d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_091_vol_ratio_slope_63d},
    "xdr_092_vol_above_peer_pct_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_092_vol_above_peer_pct_252d},
    "xdr_093_vol_above_peer_pct_63d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_093_vol_above_peer_pct_63d},
    "xdr_094_vol_ratio_ewm_21d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_094_vol_ratio_ewm_21d},
    "xdr_095_vol_ratio_expanding_max": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_095_vol_ratio_expanding_max},
    "xdr_096_vol_current_vs_expanding_max": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_096_vol_current_vs_expanding_max},
    "xdr_097_vol_ratio_half_yr_zscore": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_097_vol_ratio_half_yr_zscore},
    "xdr_098_vol_gap_zscore_63d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_098_vol_gap_zscore_63d},
    "xdr_099_vol_gap_zscore_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_099_vol_gap_zscore_252d},
    "xdr_100_rsi14_peer_gap_5d_change": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_100_rsi14_peer_gap_5d_change},
    "xdr_101_rsi14_peer_gap_21d_change": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_101_rsi14_peer_gap_21d_change},
    "xdr_102_rsi14_peer_gap_slope_21d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_102_rsi14_peer_gap_slope_21d},
    "xdr_103_rsi14_peer_gap_slope_63d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_103_rsi14_peer_gap_slope_63d},
    "xdr_104_rsi14_peer_gap_ewm_21d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_104_rsi14_peer_gap_ewm_21d},
    "xdr_105_rsi14_peer_gap_half_yr_zscore": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_105_rsi14_peer_gap_half_yr_zscore},
    "xdr_106_rsi14_below_peer_frac_126d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_106_rsi14_below_peer_frac_126d},
    "xdr_107_rsi14_consec_below_peer_streak_max_63d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_107_rsi14_consec_below_peer_streak_max_63d},
    "xdr_108_rsi14_peer_gap_expanding_min": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_108_rsi14_peer_gap_expanding_min},
    "xdr_109_rsi14_peer_gap_expanding_pct_rank": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_109_rsi14_peer_gap_expanding_pct_rank},
    "xdr_110_rsi14_peer_gap_min_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_110_rsi14_peer_gap_min_252d},
    "xdr_111_de_ratio_5d_change": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_111_de_ratio_5d_change},
    "xdr_112_de_ratio_21d_change": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_112_de_ratio_21d_change},
    "xdr_113_de_ratio_slope_63d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_113_de_ratio_slope_63d},
    "xdr_114_de_above_peer_pct_252d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_114_de_above_peer_pct_252d},
    "xdr_115_pb_ratio_5d_change": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_115_pb_ratio_5d_change},
    "xdr_116_pb_ratio_21d_change": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_116_pb_ratio_21d_change},
    "xdr_117_pb_ratio_slope_63d": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_117_pb_ratio_slope_63d},
    "xdr_118_pb_below_peer_pct_252d": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_118_pb_below_peer_pct_252d},
    "xdr_119_pb_ratio_expanding_min": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_119_pb_ratio_expanding_min},
    "xdr_120_ps_ratio_slope_63d": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_120_ps_ratio_slope_63d},
    "xdr_121_ps_below_peer_pct_252d": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_121_ps_below_peer_pct_252d},
    "xdr_122_ps_ratio_zscore_252d": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_122_ps_ratio_zscore_252d},
    "xdr_123_drawdown_vol_both_worse_flag": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol"],
        "func": xdr_123_drawdown_vol_both_worse_flag},
    "xdr_124_drawdown_rsi_both_worse_flag": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_124_drawdown_rsi_both_worse_flag},
    "xdr_125_vol_leverage_both_worse_flag": {
        "inputs": ["realized_vol", "peer_median_realized_vol",
                   "debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_125_vol_leverage_both_worse_flag},
    "xdr_126_valuation_fcf_both_worse_flag": {
        "inputs": ["pb", "peer_median_pb",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_126_valuation_fcf_both_worse_flag},
    "xdr_127_dual_distress_days_63d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol"],
        "func": xdr_127_dual_distress_days_63d},
    "xdr_128_triple_distress_days_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_128_triple_distress_days_252d},
    "xdr_129_drawdown_gap_times_vol_ratio": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol"],
        "func": xdr_129_drawdown_gap_times_vol_ratio},
    "xdr_130_rsi14_gap_times_de_ratio": {
        "inputs": ["rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_130_rsi14_gap_times_de_ratio},
    "xdr_131_all5_worse_consec_streak": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_131_all5_worse_consec_streak},
    "xdr_132_composite_z5_rolling_max_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_132_composite_z5_rolling_max_252d},
    "xdr_133_composite_z3_ewm_21d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_133_composite_z3_ewm_21d},
    "xdr_134_composite_z3_ewm_63d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_134_composite_z3_ewm_63d},
    "xdr_135_distress_breadth_21d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_135_distress_breadth_21d},
    "xdr_136_distress_breadth_63d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_136_distress_breadth_63d},
    "xdr_137_fcf_gap_5d_change": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_137_fcf_gap_5d_change},
    "xdr_138_fcf_gap_21d_change": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_138_fcf_gap_21d_change},
    "xdr_139_fcf_gap_slope_63d": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_139_fcf_gap_slope_63d},
    "xdr_140_fcf_gap_ewm_63d": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_140_fcf_gap_ewm_63d},
    "xdr_141_marketcap_ratio_5d_change": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_141_marketcap_ratio_5d_change},
    "xdr_142_marketcap_ratio_21d_change": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_142_marketcap_ratio_21d_change},
    "xdr_143_marketcap_ratio_slope_63d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_143_marketcap_ratio_slope_63d},
    "xdr_144_marketcap_below_peer_pct_252d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_144_marketcap_below_peer_pct_252d},
    "xdr_145_marketcap_ratio_expanding_pct_rank": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_145_marketcap_ratio_expanding_pct_rank},
    "xdr_146_pb_ps_joint_discount_flag": {
        "inputs": ["pb", "peer_median_pb",
                   "ps", "peer_median_ps"],
        "func": xdr_146_pb_ps_joint_discount_flag},
    "xdr_147_pb_ps_joint_discount_days_252d": {
        "inputs": ["pb", "peer_median_pb",
                   "ps", "peer_median_ps"],
        "func": xdr_147_pb_ps_joint_discount_days_252d},
    "xdr_148_de_fcf_joint_stress_flag": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_148_de_fcf_joint_stress_flag},
    "xdr_149_de_fcf_joint_stress_days_252d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_149_de_fcf_joint_stress_days_252d},
    "xdr_150_composite_fundamental_distress_z": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield",
                   "pb", "peer_median_pb",
                   "ps", "peer_median_ps"],
        "func": xdr_150_composite_fundamental_distress_z},
}
