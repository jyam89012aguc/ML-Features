"""
124_cross_sectional_distress_rank — Extended Features 001-075
Domain: deeper cross-sectional distress rank variants — tail-position features, regime
        flags, multi-window rank composites, additional peer-relative distress signals
        beyond the base 150.  Covers percentile extremes, skew of peer gaps, and
        compound distress-persistence metrics.
Asset class: US equities | Daily price/volume + fundamental inputs (SEP + SF1-derived)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily pd.Series AND a precomputed
    peer-median Series of the SAME daily DatetimeIndex (peer_median_<field>).
    The pipeline provides sector/industry peer medians universe-wide.

Own inputs:      drawdown, realized_vol, rsi14, marketcap,
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
    return _safe_div(own, peer)


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    ratio = _rel_ratio(own, peer)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def _gap(own: pd.Series, peer: pd.Series) -> pd.Series:
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


# ── Extended Feature Functions 001-075 ───────────────────────────────────────

# --- Group A (001-012): Tail-position and extreme-distress flags ---

def xdr_ext_001_drawdown_ratio_below_p10_flag(drawdown: pd.Series,
                                               peer_median_drawdown: pd.Series) -> pd.Series:
    """Binary: 1 if drawdown ratio is in the bottom 10th pct of its 252-day distribution."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    p10 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return (ratio <= p10).astype(float)


def xdr_ext_002_vol_ratio_above_p90_flag(realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series) -> pd.Series:
    """Binary: 1 if vol ratio is in top 90th pct of its 252-day distribution."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    p90 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (ratio >= p90).astype(float)


def xdr_ext_003_rsi14_peer_gap_below_p10_flag(rsi14: pd.Series,
                                               peer_median_rsi14: pd.Series) -> pd.Series:
    """Binary: 1 if RSI14 peer gap is in the bottom 10th pct of its 252-day distribution."""
    gap = _gap(rsi14, peer_median_rsi14)
    p10 = gap.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return (gap <= p10).astype(float)


def xdr_ext_004_composite_z3_above_p90_flag(drawdown: pd.Series,
                                              peer_median_drawdown: pd.Series,
                                              realized_vol: pd.Series,
                                              peer_median_realized_vol: pd.Series,
                                              rsi14: pd.Series,
                                              peer_median_rsi14: pd.Series) -> pd.Series:
    """Binary: 1 if 3-dim composite z-score is in the top 90th pct (extreme distress tail)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    p90 = composite.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (composite >= p90).astype(float)


def xdr_ext_005_drawdown_ratio_p10_exceedance_depth(drawdown: pd.Series,
                                                      peer_median_drawdown: pd.Series) -> pd.Series:
    """How far below the 10th-pct threshold the drawdown ratio is (0 when above threshold)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    p10 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.10)
    return (p10 - ratio).clip(lower=0.0)


def xdr_ext_006_vol_ratio_p90_exceedance_depth(realized_vol: pd.Series,
                                                 peer_median_realized_vol: pd.Series) -> pd.Series:
    """How far above the 90th-pct threshold the vol ratio is (0 when below)."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    p90 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (ratio - p90).clip(lower=0.0)


def xdr_ext_007_drawdown_ratio_p5_flag(drawdown: pd.Series,
                                        peer_median_drawdown: pd.Series) -> pd.Series:
    """Binary: 1 if drawdown ratio is in the bottom 5th pct (extreme capitulation tail)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    p5 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.05)
    return (ratio <= p5).astype(float)


def xdr_ext_008_composite_z5_p90_exceedance_depth(drawdown: pd.Series,
                                                    peer_median_drawdown: pd.Series,
                                                    realized_vol: pd.Series,
                                                    peer_median_realized_vol: pd.Series,
                                                    rsi14: pd.Series,
                                                    peer_median_rsi14: pd.Series,
                                                    debt_to_equity: pd.Series,
                                                    peer_median_debt_to_equity: pd.Series,
                                                    fcf_yield: pd.Series,
                                                    peer_median_fcf_yield: pd.Series) -> pd.Series:
    """How far above 90th-pct threshold the 5-dim composite distress z-score is."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi + z_de + z_fcf) / 5.0
    p90 = composite.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (composite - p90).clip(lower=0.0)


def xdr_ext_009_drawdown_gap_skew_252d(drawdown: pd.Series,
                                        peer_median_drawdown: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of the drawdown gap distribution."""
    return _gap(drawdown, peer_median_drawdown).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def xdr_ext_010_vol_ratio_skew_252d(realized_vol: pd.Series,
                                     peer_median_realized_vol: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of the vol ratio distribution."""
    return _rel_ratio(realized_vol, peer_median_realized_vol).rolling(
        _TD_YEAR, min_periods=_TD_QTR).skew()


def xdr_ext_011_rsi14_peer_gap_skew_252d(rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series) -> pd.Series:
    """Rolling 252-day skewness of the RSI14 peer gap distribution."""
    return _gap(rsi14, peer_median_rsi14).rolling(_TD_YEAR, min_periods=_TD_QTR).skew()


def xdr_ext_012_de_ratio_p90_flag(debt_to_equity: pd.Series,
                                    peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Binary: 1 if D/E ratio vs peers is in top 90th pct of 252-day distribution."""
    ratio = _rel_ratio(debt_to_equity, peer_median_debt_to_equity)
    p90 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.90)
    return (ratio >= p90).astype(float)


# --- Group B (013-024): Multi-window rank composites ---

def xdr_ext_013_drawdown_pct_rank_21d_63d_mean(drawdown: pd.Series,
                                                 peer_median_drawdown: pd.Series) -> pd.Series:
    """Average of 21d and 63d pct-ranks of drawdown ratio (multi-window rank)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    r21 = ratio.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    r63 = ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    return (r21 + r63) / 2.0


def xdr_ext_014_vol_pct_rank_63d_252d_mean(realized_vol: pd.Series,
                                            peer_median_realized_vol: pd.Series) -> pd.Series:
    """Average of 63d and 252d pct-ranks of vol ratio."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    r63  = ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    r252 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (r63 + r252) / 2.0


def xdr_ext_015_rsi14_peer_gap_pct_rank_21d_252d_mean(rsi14: pd.Series,
                                                        peer_median_rsi14: pd.Series) -> pd.Series:
    """Average of 21d and 252d pct-ranks of RSI14 peer gap."""
    gap = _gap(rsi14, peer_median_rsi14)
    r21  = gap.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)
    r252 = gap.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (r21 + r252) / 2.0


def xdr_ext_016_composite_z3_pct_rank_63d_252d_mean(drawdown: pd.Series,
                                                      peer_median_drawdown: pd.Series,
                                                      realized_vol: pd.Series,
                                                      peer_median_realized_vol: pd.Series,
                                                      rsi14: pd.Series,
                                                      peer_median_rsi14: pd.Series) -> pd.Series:
    """Average of 63d and 252d pct-ranks of 3-dim composite z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    r63  = composite.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    r252 = composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (r63 + r252) / 2.0


def xdr_ext_017_drawdown_ratio_half_yr_pct_rank(drawdown: pd.Series,
                                                  peer_median_drawdown: pd.Series) -> pd.Series:
    """126-day rolling pct-rank of drawdown ratio."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    return ratio.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def xdr_ext_018_vol_ratio_half_yr_pct_rank(realized_vol: pd.Series,
                                            peer_median_realized_vol: pd.Series) -> pd.Series:
    """126-day rolling pct-rank of vol ratio."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    return ratio.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def xdr_ext_019_de_pct_rank_63d_252d_mean(debt_to_equity: pd.Series,
                                           peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Average of 63d and 252d pct-ranks of D/E ratio vs peers."""
    ratio = _rel_ratio(debt_to_equity, peer_median_debt_to_equity)
    r63  = ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    r252 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (r63 + r252) / 2.0


def xdr_ext_020_fcf_pct_rank_63d_252d_mean(fcf_yield: pd.Series,
                                            peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Average of 63d and 252d pct-ranks of FCF yield gap."""
    gap = _gap(fcf_yield, peer_median_fcf_yield)
    r63  = gap.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    r252 = gap.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (r63 + r252) / 2.0


def xdr_ext_021_pb_pct_rank_63d_252d_mean(pb: pd.Series,
                                           peer_median_pb: pd.Series) -> pd.Series:
    """Average of 63d and 252d pct-ranks of P/B ratio vs peers."""
    ratio = _rel_ratio(pb, peer_median_pb)
    r63  = ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    r252 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (r63 + r252) / 2.0


def xdr_ext_022_marketcap_pct_rank_63d_252d_mean(marketcap: pd.Series,
                                                   peer_median_marketcap: pd.Series) -> pd.Series:
    """Average of 63d and 252d pct-ranks of market-cap ratio vs peers."""
    ratio = _rel_ratio(marketcap, peer_median_marketcap)
    r63  = ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)
    r252 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    return (r63 + r252) / 2.0


def xdr_ext_023_drawdown_ratio_2yr_pct_rank(drawdown: pd.Series,
                                             peer_median_drawdown: pd.Series) -> pd.Series:
    """2-year (504-day) rolling pct-rank of drawdown ratio (long-term tail position)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    return ratio.rolling(_TD_2Y, min_periods=_TD_YEAR).rank(pct=True)


def xdr_ext_024_vol_ratio_2yr_pct_rank(realized_vol: pd.Series,
                                        peer_median_realized_vol: pd.Series) -> pd.Series:
    """2-year (504-day) rolling pct-rank of vol ratio."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    return ratio.rolling(_TD_2Y, min_periods=_TD_YEAR).rank(pct=True)


# --- Group C (025-038): Distress-persistence and regime features ---

def xdr_ext_025_drawdown_worse_than_peer_consec_max_252d(drawdown: pd.Series,
                                                           peer_median_drawdown: pd.Series) -> pd.Series:
    """252-day maximum of the consecutive-worse-drawdown streak."""
    streak = _consec_streak(drawdown < peer_median_drawdown)
    return _rolling_max(streak, _TD_YEAR)


def xdr_ext_026_vol_above_peer_consec_max_252d(realized_vol: pd.Series,
                                                peer_median_realized_vol: pd.Series) -> pd.Series:
    """252-day maximum of the consecutive-above-peer-vol streak."""
    streak = _consec_streak(realized_vol > peer_median_realized_vol)
    return _rolling_max(streak, _TD_YEAR)


def xdr_ext_027_rsi14_below_peer_consec_max_252d(rsi14: pd.Series,
                                                   peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day maximum of consecutive-below-peer-RSI14 streak."""
    streak = _consec_streak(rsi14 < peer_median_rsi14)
    return _rolling_max(streak, _TD_YEAR)


def xdr_ext_028_distress_regime_flag_252d(drawdown: pd.Series,
                                           peer_median_drawdown: pd.Series,
                                           realized_vol: pd.Series,
                                           peer_median_realized_vol: pd.Series,
                                           rsi14: pd.Series,
                                           peer_median_rsi14: pd.Series) -> pd.Series:
    """Binary: 1 if 252-day mean 3-dim composite z-score is positive (persistent distress regime)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return (_rolling_mean(composite, _TD_YEAR) > 0.0).astype(float)


def xdr_ext_029_distress_regime_intensity_252d(drawdown: pd.Series,
                                                peer_median_drawdown: pd.Series,
                                                realized_vol: pd.Series,
                                                peer_median_realized_vol: pd.Series,
                                                rsi14: pd.Series,
                                                peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day mean of 3-dim composite z-score (average distress intensity over year)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return _rolling_mean(composite, _TD_YEAR)


def xdr_ext_030_all5_worse_pct_252d(drawdown: pd.Series,
                                     peer_median_drawdown: pd.Series,
                                     realized_vol: pd.Series,
                                     peer_median_realized_vol: pd.Series,
                                     rsi14: pd.Series,
                                     peer_median_rsi14: pd.Series,
                                     debt_to_equity: pd.Series,
                                     peer_median_debt_to_equity: pd.Series,
                                     fcf_yield: pd.Series,
                                     peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Fraction of trailing 252d where all 5 distress dims simultaneously worse than peers."""
    flag = ((drawdown < peer_median_drawdown) &
            (realized_vol > peer_median_realized_vol) &
            (rsi14 < peer_median_rsi14) &
            (debt_to_equity > peer_median_debt_to_equity) &
            (fcf_yield < peer_median_fcf_yield)).astype(float)
    return _rolling_sum(flag, _TD_YEAR) / _TD_YEAR


def xdr_ext_031_drawdown_ratio_ema_vs_sma_21d(drawdown: pd.Series,
                                               peer_median_drawdown: pd.Series) -> pd.Series:
    """EMA(21d) minus SMA(21d) of drawdown ratio (momentum curvature of relative drawdown)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    return _ewm_mean(ratio, _TD_MON) - _rolling_mean(ratio, _TD_MON)


def xdr_ext_032_vol_ratio_ema_vs_sma_21d(realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series) -> pd.Series:
    """EMA(21d) minus SMA(21d) of vol ratio (momentum curvature of relative vol)."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    return _ewm_mean(ratio, _TD_MON) - _rolling_mean(ratio, _TD_MON)


def xdr_ext_033_composite_z3_ema_vs_sma_21d(drawdown: pd.Series,
                                              peer_median_drawdown: pd.Series,
                                              realized_vol: pd.Series,
                                              peer_median_realized_vol: pd.Series,
                                              rsi14: pd.Series,
                                              peer_median_rsi14: pd.Series) -> pd.Series:
    """EMA(21d) minus SMA(21d) of 3-dim composite z-score (curvature of total distress)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return _ewm_mean(composite, _TD_MON) - _rolling_mean(composite, _TD_MON)


def xdr_ext_034_drawdown_gap_IQR_ratio_252d(drawdown: pd.Series,
                                             peer_median_drawdown: pd.Series) -> pd.Series:
    """252-day IQR (Q75-Q25) of drawdown gap — spread of relative drawdown distribution."""
    gap = _gap(drawdown, peer_median_drawdown)
    q75 = gap.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = gap.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return q75 - q25


def xdr_ext_035_vol_ratio_IQR_252d(realized_vol: pd.Series,
                                    peer_median_realized_vol: pd.Series) -> pd.Series:
    """252-day IQR of vol ratio distribution."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    q75 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.75)
    q25 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).quantile(0.25)
    return q75 - q25


def xdr_ext_036_distress_breadth_pct_rank_252d(drawdown: pd.Series,
                                                peer_median_drawdown: pd.Series,
                                                realized_vol: pd.Series,
                                                peer_median_realized_vol: pd.Series,
                                                rsi14: pd.Series,
                                                peer_median_rsi14: pd.Series,
                                                debt_to_equity: pd.Series,
                                                peer_median_debt_to_equity: pd.Series,
                                                fcf_yield: pd.Series,
                                                peer_median_fcf_yield: pd.Series) -> pd.Series:
    """252-day pct-rank of 5-dim distress count (where is today's breadth historically)."""
    count = ((drawdown < peer_median_drawdown).astype(float) +
             (realized_vol > peer_median_realized_vol).astype(float) +
             (rsi14 < peer_median_rsi14).astype(float) +
             (debt_to_equity > peer_median_debt_to_equity).astype(float) +
             (fcf_yield < peer_median_fcf_yield).astype(float))
    return count.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_037_drawdown_ratio_slope_sign_consec(drawdown: pd.Series,
                                                   peer_median_drawdown: pd.Series) -> pd.Series:
    """Consecutive days the 21-day slope of drawdown ratio is negative (worsening trend)."""
    slope = _linslope(_rel_ratio(drawdown, peer_median_drawdown), _TD_MON)
    return _consec_streak(slope < 0.0)


def xdr_ext_038_vol_ratio_slope_sign_consec(realized_vol: pd.Series,
                                             peer_median_realized_vol: pd.Series) -> pd.Series:
    """Consecutive days the 21-day slope of vol ratio is positive (worsening vol trend)."""
    slope = _linslope(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_MON)
    return _consec_streak(slope > 0.0)


# --- Group D (039-052): Cross-dimension log-relative and normalized features ---

def xdr_ext_039_drawdown_log_rel_zscore_252d(drawdown: pd.Series,
                                              peer_median_drawdown: pd.Series) -> pd.Series:
    """Z-score of log-relative drawdown within 252-day window."""
    return _zscore_rolling(_log_rel(drawdown, peer_median_drawdown), _TD_YEAR)


def xdr_ext_040_vol_log_rel_zscore_252d(realized_vol: pd.Series,
                                         peer_median_realized_vol: pd.Series) -> pd.Series:
    """Z-score of log-relative vol within 252-day window."""
    return _zscore_rolling(_log_rel(realized_vol, peer_median_realized_vol), _TD_YEAR)


def xdr_ext_041_de_log_rel_zscore_252d(debt_to_equity: pd.Series,
                                        peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Z-score of log-relative D/E within 252-day window."""
    return _zscore_rolling(_log_rel(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)


def xdr_ext_042_pb_log_rel_zscore_252d(pb: pd.Series,
                                        peer_median_pb: pd.Series) -> pd.Series:
    """Z-score of log-relative P/B within 252-day window."""
    return _zscore_rolling(_log_rel(pb, peer_median_pb), _TD_YEAR)


def xdr_ext_043_ps_log_rel_zscore_252d(ps: pd.Series,
                                        peer_median_ps: pd.Series) -> pd.Series:
    """Z-score of log-relative P/S within 252-day window."""
    return _zscore_rolling(_log_rel(ps, peer_median_ps), _TD_YEAR)


def xdr_ext_044_marketcap_log_rel_pct_rank_252d(marketcap: pd.Series,
                                                  peer_median_marketcap: pd.Series) -> pd.Series:
    """252-day pct-rank of log-relative market cap (size position in distribution)."""
    return _log_rel(marketcap, peer_median_marketcap).rolling(
        _TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_045_fcf_gap_pct_rank_63d(fcf_yield: pd.Series,
                                      peer_median_fcf_yield: pd.Series) -> pd.Series:
    """63-day pct-rank of FCF yield gap vs peers."""
    gap = _gap(fcf_yield, peer_median_fcf_yield)
    return gap.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def xdr_ext_046_drawdown_ratio_median_21d(drawdown: pd.Series,
                                           peer_median_drawdown: pd.Series) -> pd.Series:
    """21-day rolling median of drawdown ratio (robust center of relative drawdown)."""
    return _rolling_median(_rel_ratio(drawdown, peer_median_drawdown), _TD_MON)


def xdr_ext_047_vol_ratio_median_63d(realized_vol: pd.Series,
                                      peer_median_realized_vol: pd.Series) -> pd.Series:
    """63-day rolling median of vol ratio."""
    return _rolling_median(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_QTR)


def xdr_ext_048_composite_z3_median_63d(drawdown: pd.Series,
                                         peer_median_drawdown: pd.Series,
                                         realized_vol: pd.Series,
                                         peer_median_realized_vol: pd.Series,
                                         rsi14: pd.Series,
                                         peer_median_rsi14: pd.Series) -> pd.Series:
    """63-day rolling median of 3-dim composite z-score (robust distress center)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return _rolling_median(composite, _TD_QTR)


def xdr_ext_049_drawdown_ratio_std_63d(drawdown: pd.Series,
                                        peer_median_drawdown: pd.Series) -> pd.Series:
    """63-day rolling std of drawdown ratio (dispersion of relative drawdown)."""
    return _rolling_std(_rel_ratio(drawdown, peer_median_drawdown), _TD_QTR)


def xdr_ext_050_vol_ratio_std_252d(realized_vol: pd.Series,
                                    peer_median_realized_vol: pd.Series) -> pd.Series:
    """252-day rolling std of vol ratio (dispersion of relative vol stress)."""
    return _rolling_std(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)


def xdr_ext_051_rsi14_peer_gap_std_252d(rsi14: pd.Series,
                                         peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day rolling std of RSI14 peer gap (dispersion of relative momentum)."""
    return _rolling_std(_gap(rsi14, peer_median_rsi14), _TD_YEAR)


def xdr_ext_052_composite_z3_std_252d(drawdown: pd.Series,
                                       peer_median_drawdown: pd.Series,
                                       realized_vol: pd.Series,
                                       peer_median_realized_vol: pd.Series,
                                       rsi14: pd.Series,
                                       peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day rolling std of 3-dim composite z-score (volatility of distress score)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return _rolling_std(composite, _TD_YEAR)


# --- Group E (053-075): Additional cross-sectional comparative signals ---

def xdr_ext_053_drawdown_ratio_min_vs_max_252d(drawdown: pd.Series,
                                                peer_median_drawdown: pd.Series) -> pd.Series:
    """Min/max ratio of drawdown ratio over 252 days (compression range as fraction)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    mn = _rolling_min(ratio, _TD_YEAR)
    mx = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(mn, mx.abs())


def xdr_ext_054_vol_ratio_min_vs_max_252d(realized_vol: pd.Series,
                                           peer_median_realized_vol: pd.Series) -> pd.Series:
    """Min/max ratio of vol ratio over 252 days."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    mn = _rolling_min(ratio, _TD_YEAR)
    mx = _rolling_max(ratio, _TD_YEAR)
    return _safe_div(mn, mx.abs())


def xdr_ext_055_drawdown_gap_half_yr_pct_rank(drawdown: pd.Series,
                                               peer_median_drawdown: pd.Series) -> pd.Series:
    """126-day pct-rank of drawdown gap."""
    gap = _gap(drawdown, peer_median_drawdown)
    return gap.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def xdr_ext_056_rsi14_peer_gap_half_yr_pct_rank(rsi14: pd.Series,
                                                  peer_median_rsi14: pd.Series) -> pd.Series:
    """126-day pct-rank of RSI14 peer gap."""
    gap = _gap(rsi14, peer_median_rsi14)
    return gap.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def xdr_ext_057_de_ratio_half_yr_pct_rank(debt_to_equity: pd.Series,
                                           peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """126-day pct-rank of D/E ratio vs peers."""
    ratio = _rel_ratio(debt_to_equity, peer_median_debt_to_equity)
    return ratio.rolling(_TD_HALF, min_periods=max(1, _TD_HALF // 2)).rank(pct=True)


def xdr_ext_058_marketcap_log_rel_zscore_252d(marketcap: pd.Series,
                                               peer_median_marketcap: pd.Series) -> pd.Series:
    """Z-score of log-relative market cap within 252-day window."""
    return _zscore_rolling(_log_rel(marketcap, peer_median_marketcap), _TD_YEAR)


def xdr_ext_059_drawdown_vol_composite_pct_rank_252d(drawdown: pd.Series,
                                                      peer_median_drawdown: pd.Series,
                                                      realized_vol: pd.Series,
                                                      peer_median_realized_vol: pd.Series) -> pd.Series:
    """252-day pct-rank of 2-dim drawdown+vol joint z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    composite = (z_dd + z_vol) / 2.0
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_060_fundamental_distress_z_pct_rank_252d(debt_to_equity: pd.Series,
                                                       peer_median_debt_to_equity: pd.Series,
                                                       fcf_yield: pd.Series,
                                                       peer_median_fcf_yield: pd.Series,
                                                       pb: pd.Series,
                                                       peer_median_pb: pd.Series,
                                                       ps: pd.Series,
                                                       peer_median_ps: pd.Series) -> pd.Series:
    """252-day pct-rank of 4-dim fundamental distress z-score."""
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    z_pb  = -_zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR)
    z_ps  = -_zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR)
    composite = (z_de + z_fcf + z_pb + z_ps) / 4.0
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_061_drawdown_ratio_recovery_from_min_252d(drawdown: pd.Series,
                                                        peer_median_drawdown: pd.Series) -> pd.Series:
    """Current drawdown ratio minus 252-day min (how far off worst relative distress)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    mn = _rolling_min(ratio, _TD_YEAR)
    return ratio - mn


def xdr_ext_062_vol_ratio_recovery_from_max_252d(realized_vol: pd.Series,
                                                   peer_median_realized_vol: pd.Series) -> pd.Series:
    """252-day max vol ratio minus current (how far off worst relative vol stress)."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    mx = _rolling_max(ratio, _TD_YEAR)
    return mx - ratio


def xdr_ext_063_rsi14_peer_gap_recovery_from_min_252d(rsi14: pd.Series,
                                                        peer_median_rsi14: pd.Series) -> pd.Series:
    """Current RSI14 peer gap minus 252-day min (recovery from worst momentum divergence)."""
    gap = _gap(rsi14, peer_median_rsi14)
    return gap - _rolling_min(gap, _TD_YEAR)


def xdr_ext_064_composite_z3_recovery_from_max_252d(drawdown: pd.Series,
                                                      peer_median_drawdown: pd.Series,
                                                      realized_vol: pd.Series,
                                                      peer_median_realized_vol: pd.Series,
                                                      rsi14: pd.Series,
                                                      peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day max composite z3 minus current (how far off peak distress)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return _rolling_max(composite, _TD_YEAR) - composite


def xdr_ext_065_drawdown_ratio_vs_2yr_pct_rank(drawdown: pd.Series,
                                                 peer_median_drawdown: pd.Series) -> pd.Series:
    """252-day pct-rank divided by 2yr pct-rank (short vs long-term rank divergence)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    r252 = ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)
    r2yr = ratio.rolling(_TD_2Y, min_periods=_TD_YEAR).rank(pct=True)
    return _safe_div(r252, r2yr.clip(lower=_EPS))


def xdr_ext_066_de_fcf_composite_pct_rank_252d(debt_to_equity: pd.Series,
                                                 peer_median_debt_to_equity: pd.Series,
                                                 fcf_yield: pd.Series,
                                                 peer_median_fcf_yield: pd.Series) -> pd.Series:
    """252-day pct-rank of D/E+FCF 2-dim composite z-score."""
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    composite = (z_de + z_fcf) / 2.0
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_067_drawdown_ratio_slope_21d_pct_rank_252d(drawdown: pd.Series,
                                                         peer_median_drawdown: pd.Series) -> pd.Series:
    """252-day pct-rank of the 21-day slope of drawdown ratio."""
    slope = _linslope(_rel_ratio(drawdown, peer_median_drawdown), _TD_MON)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_068_vol_ratio_slope_21d_pct_rank_252d(realized_vol: pd.Series,
                                                    peer_median_realized_vol: pd.Series) -> pd.Series:
    """252-day pct-rank of the 21-day slope of vol ratio."""
    slope = _linslope(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_MON)
    return slope.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_069_pb_ps_composite_pct_rank_252d(pb: pd.Series,
                                               peer_median_pb: pd.Series,
                                               ps: pd.Series,
                                               peer_median_ps: pd.Series) -> pd.Series:
    """252-day pct-rank of inverted P/B + inverted P/S composite z-score."""
    z_pb = -_zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR)
    z_ps = -_zscore_rolling(_rel_ratio(ps, peer_median_ps), _TD_YEAR)
    composite = (z_pb + z_ps) / 2.0
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_070_marketcap_drawdown_joint_z_pct_rank_252d(marketcap: pd.Series,
                                                           peer_median_marketcap: pd.Series,
                                                           drawdown: pd.Series,
                                                           peer_median_drawdown: pd.Series) -> pd.Series:
    """252-day pct-rank of market-cap compression + drawdown depth 2-dim z-score."""
    z_cap = -_zscore_rolling(_rel_ratio(marketcap, peer_median_marketcap), _TD_YEAR)
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    composite = (z_cap + z_dd) / 2.0
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_071_composite_z5_expanding_pct_rank(drawdown: pd.Series,
                                                  peer_median_drawdown: pd.Series,
                                                  realized_vol: pd.Series,
                                                  peer_median_realized_vol: pd.Series,
                                                  rsi14: pd.Series,
                                                  peer_median_rsi14: pd.Series,
                                                  debt_to_equity: pd.Series,
                                                  peer_median_debt_to_equity: pd.Series,
                                                  fcf_yield: pd.Series,
                                                  peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Expanding all-time pct-rank of 5-dim composite distress z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi + z_de + z_fcf) / 5.0
    return composite.expanding(min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_072_distress_breadth_expanding_pct_rank(drawdown: pd.Series,
                                                     peer_median_drawdown: pd.Series,
                                                     realized_vol: pd.Series,
                                                     peer_median_realized_vol: pd.Series,
                                                     rsi14: pd.Series,
                                                     peer_median_rsi14: pd.Series,
                                                     debt_to_equity: pd.Series,
                                                     peer_median_debt_to_equity: pd.Series,
                                                     fcf_yield: pd.Series,
                                                     peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Expanding pct-rank of 5-dim distress count."""
    count = ((drawdown < peer_median_drawdown).astype(float) +
             (realized_vol > peer_median_realized_vol).astype(float) +
             (rsi14 < peer_median_rsi14).astype(float) +
             (debt_to_equity > peer_median_debt_to_equity).astype(float) +
             (fcf_yield < peer_median_fcf_yield).astype(float))
    return count.expanding(min_periods=_TD_QTR).rank(pct=True)


def xdr_ext_073_drawdown_ratio_new_low_252d_flag(drawdown: pd.Series,
                                                   peer_median_drawdown: pd.Series) -> pd.Series:
    """Binary: 1 if today's drawdown ratio is the lowest in trailing 252 days."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    prev_min = ratio.shift(1).rolling(_TD_YEAR, min_periods=1).min()
    return (ratio < prev_min).astype(float)


def xdr_ext_074_vol_ratio_new_high_252d_flag(realized_vol: pd.Series,
                                              peer_median_realized_vol: pd.Series) -> pd.Series:
    """Binary: 1 if today's vol ratio is the highest in trailing 252 days."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    prev_max = ratio.shift(1).rolling(_TD_YEAR, min_periods=1).max()
    return (ratio > prev_max).astype(float)


def xdr_ext_075_composite_z5_new_high_252d_flag(drawdown: pd.Series,
                                                  peer_median_drawdown: pd.Series,
                                                  realized_vol: pd.Series,
                                                  peer_median_realized_vol: pd.Series,
                                                  rsi14: pd.Series,
                                                  peer_median_rsi14: pd.Series,
                                                  debt_to_equity: pd.Series,
                                                  peer_median_debt_to_equity: pd.Series,
                                                  fcf_yield: pd.Series,
                                                  peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Binary: 1 if 5-dim composite distress z-score is at a 252-day high (peak distress)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi + z_de + z_fcf) / 5.0
    prev_max = composite.shift(1).rolling(_TD_YEAR, min_periods=1).max()
    return (composite > prev_max).astype(float)


# ── Registry ──────────────────────────────────────────────────────────────────

CROSS_SECTIONAL_DISTRESS_RANK_EXTENDED_REGISTRY_001_075 = {
    "xdr_ext_001_drawdown_ratio_below_p10_flag": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_001_drawdown_ratio_below_p10_flag},
    "xdr_ext_002_vol_ratio_above_p90_flag": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_002_vol_ratio_above_p90_flag},
    "xdr_ext_003_rsi14_peer_gap_below_p10_flag": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_ext_003_rsi14_peer_gap_below_p10_flag},
    "xdr_ext_004_composite_z3_above_p90_flag": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_ext_004_composite_z3_above_p90_flag},
    "xdr_ext_005_drawdown_ratio_p10_exceedance_depth": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_005_drawdown_ratio_p10_exceedance_depth},
    "xdr_ext_006_vol_ratio_p90_exceedance_depth": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_006_vol_ratio_p90_exceedance_depth},
    "xdr_ext_007_drawdown_ratio_p5_flag": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_007_drawdown_ratio_p5_flag},
    "xdr_ext_008_composite_z5_p90_exceedance_depth": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_008_composite_z5_p90_exceedance_depth},
    "xdr_ext_009_drawdown_gap_skew_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_009_drawdown_gap_skew_252d},
    "xdr_ext_010_vol_ratio_skew_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_010_vol_ratio_skew_252d},
    "xdr_ext_011_rsi14_peer_gap_skew_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_ext_011_rsi14_peer_gap_skew_252d},
    "xdr_ext_012_de_ratio_p90_flag": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_ext_012_de_ratio_p90_flag},
    "xdr_ext_013_drawdown_pct_rank_21d_63d_mean": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_013_drawdown_pct_rank_21d_63d_mean},
    "xdr_ext_014_vol_pct_rank_63d_252d_mean": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_014_vol_pct_rank_63d_252d_mean},
    "xdr_ext_015_rsi14_peer_gap_pct_rank_21d_252d_mean": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_ext_015_rsi14_peer_gap_pct_rank_21d_252d_mean},
    "xdr_ext_016_composite_z3_pct_rank_63d_252d_mean": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_ext_016_composite_z3_pct_rank_63d_252d_mean},
    "xdr_ext_017_drawdown_ratio_half_yr_pct_rank": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_017_drawdown_ratio_half_yr_pct_rank},
    "xdr_ext_018_vol_ratio_half_yr_pct_rank": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_018_vol_ratio_half_yr_pct_rank},
    "xdr_ext_019_de_pct_rank_63d_252d_mean": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_ext_019_de_pct_rank_63d_252d_mean},
    "xdr_ext_020_fcf_pct_rank_63d_252d_mean": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_020_fcf_pct_rank_63d_252d_mean},
    "xdr_ext_021_pb_pct_rank_63d_252d_mean": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_ext_021_pb_pct_rank_63d_252d_mean},
    "xdr_ext_022_marketcap_pct_rank_63d_252d_mean": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_ext_022_marketcap_pct_rank_63d_252d_mean},
    "xdr_ext_023_drawdown_ratio_2yr_pct_rank": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_023_drawdown_ratio_2yr_pct_rank},
    "xdr_ext_024_vol_ratio_2yr_pct_rank": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_024_vol_ratio_2yr_pct_rank},
    "xdr_ext_025_drawdown_worse_than_peer_consec_max_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_025_drawdown_worse_than_peer_consec_max_252d},
    "xdr_ext_026_vol_above_peer_consec_max_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_026_vol_above_peer_consec_max_252d},
    "xdr_ext_027_rsi14_below_peer_consec_max_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_ext_027_rsi14_below_peer_consec_max_252d},
    "xdr_ext_028_distress_regime_flag_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_ext_028_distress_regime_flag_252d},
    "xdr_ext_029_distress_regime_intensity_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_ext_029_distress_regime_intensity_252d},
    "xdr_ext_030_all5_worse_pct_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_030_all5_worse_pct_252d},
    "xdr_ext_031_drawdown_ratio_ema_vs_sma_21d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_031_drawdown_ratio_ema_vs_sma_21d},
    "xdr_ext_032_vol_ratio_ema_vs_sma_21d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_032_vol_ratio_ema_vs_sma_21d},
    "xdr_ext_033_composite_z3_ema_vs_sma_21d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_ext_033_composite_z3_ema_vs_sma_21d},
    "xdr_ext_034_drawdown_gap_IQR_ratio_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_034_drawdown_gap_IQR_ratio_252d},
    "xdr_ext_035_vol_ratio_IQR_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_035_vol_ratio_IQR_252d},
    "xdr_ext_036_distress_breadth_pct_rank_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_036_distress_breadth_pct_rank_252d},
    "xdr_ext_037_drawdown_ratio_slope_sign_consec": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_037_drawdown_ratio_slope_sign_consec},
    "xdr_ext_038_vol_ratio_slope_sign_consec": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_038_vol_ratio_slope_sign_consec},
    "xdr_ext_039_drawdown_log_rel_zscore_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_039_drawdown_log_rel_zscore_252d},
    "xdr_ext_040_vol_log_rel_zscore_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_040_vol_log_rel_zscore_252d},
    "xdr_ext_041_de_log_rel_zscore_252d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_ext_041_de_log_rel_zscore_252d},
    "xdr_ext_042_pb_log_rel_zscore_252d": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_ext_042_pb_log_rel_zscore_252d},
    "xdr_ext_043_ps_log_rel_zscore_252d": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_ext_043_ps_log_rel_zscore_252d},
    "xdr_ext_044_marketcap_log_rel_pct_rank_252d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_ext_044_marketcap_log_rel_pct_rank_252d},
    "xdr_ext_045_fcf_gap_pct_rank_63d": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_045_fcf_gap_pct_rank_63d},
    "xdr_ext_046_drawdown_ratio_median_21d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_046_drawdown_ratio_median_21d},
    "xdr_ext_047_vol_ratio_median_63d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_047_vol_ratio_median_63d},
    "xdr_ext_048_composite_z3_median_63d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_ext_048_composite_z3_median_63d},
    "xdr_ext_049_drawdown_ratio_std_63d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_049_drawdown_ratio_std_63d},
    "xdr_ext_050_vol_ratio_std_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_050_vol_ratio_std_252d},
    "xdr_ext_051_rsi14_peer_gap_std_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_ext_051_rsi14_peer_gap_std_252d},
    "xdr_ext_052_composite_z3_std_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_ext_052_composite_z3_std_252d},
    "xdr_ext_053_drawdown_ratio_min_vs_max_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_053_drawdown_ratio_min_vs_max_252d},
    "xdr_ext_054_vol_ratio_min_vs_max_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_054_vol_ratio_min_vs_max_252d},
    "xdr_ext_055_drawdown_gap_half_yr_pct_rank": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_055_drawdown_gap_half_yr_pct_rank},
    "xdr_ext_056_rsi14_peer_gap_half_yr_pct_rank": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_ext_056_rsi14_peer_gap_half_yr_pct_rank},
    "xdr_ext_057_de_ratio_half_yr_pct_rank": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_ext_057_de_ratio_half_yr_pct_rank},
    "xdr_ext_058_marketcap_log_rel_zscore_252d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_ext_058_marketcap_log_rel_zscore_252d},
    "xdr_ext_059_drawdown_vol_composite_pct_rank_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_059_drawdown_vol_composite_pct_rank_252d},
    "xdr_ext_060_fundamental_distress_z_pct_rank_252d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield",
                   "pb", "peer_median_pb",
                   "ps", "peer_median_ps"],
        "func": xdr_ext_060_fundamental_distress_z_pct_rank_252d},
    "xdr_ext_061_drawdown_ratio_recovery_from_min_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_061_drawdown_ratio_recovery_from_min_252d},
    "xdr_ext_062_vol_ratio_recovery_from_max_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_062_vol_ratio_recovery_from_max_252d},
    "xdr_ext_063_rsi14_peer_gap_recovery_from_min_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_ext_063_rsi14_peer_gap_recovery_from_min_252d},
    "xdr_ext_064_composite_z3_recovery_from_max_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_ext_064_composite_z3_recovery_from_max_252d},
    "xdr_ext_065_drawdown_ratio_vs_2yr_pct_rank": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_065_drawdown_ratio_vs_2yr_pct_rank},
    "xdr_ext_066_de_fcf_composite_pct_rank_252d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_066_de_fcf_composite_pct_rank_252d},
    "xdr_ext_067_drawdown_ratio_slope_21d_pct_rank_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_067_drawdown_ratio_slope_21d_pct_rank_252d},
    "xdr_ext_068_vol_ratio_slope_21d_pct_rank_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_068_vol_ratio_slope_21d_pct_rank_252d},
    "xdr_ext_069_pb_ps_composite_pct_rank_252d": {
        "inputs": ["pb", "peer_median_pb",
                   "ps", "peer_median_ps"],
        "func": xdr_ext_069_pb_ps_composite_pct_rank_252d},
    "xdr_ext_070_marketcap_drawdown_joint_z_pct_rank_252d": {
        "inputs": ["marketcap", "peer_median_marketcap",
                   "drawdown", "peer_median_drawdown"],
        "func": xdr_ext_070_marketcap_drawdown_joint_z_pct_rank_252d},
    "xdr_ext_071_composite_z5_expanding_pct_rank": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_071_composite_z5_expanding_pct_rank},
    "xdr_ext_072_distress_breadth_expanding_pct_rank": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_072_distress_breadth_expanding_pct_rank},
    "xdr_ext_073_drawdown_ratio_new_low_252d_flag": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_ext_073_drawdown_ratio_new_low_252d_flag},
    "xdr_ext_074_vol_ratio_new_high_252d_flag": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_ext_074_vol_ratio_new_high_252d_flag},
    "xdr_ext_075_composite_z5_new_high_252d_flag": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_ext_075_composite_z5_new_high_252d_flag},
}
