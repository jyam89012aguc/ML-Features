"""
124_cross_sectional_distress_rank — Base Features 001-075
Domain: cross-sectional distress rank — how distressed is this name vs sector/industry
        peers across MULTIPLE distress dimensions (drawdown, volatility, valuation
        compression, leverage, momentum)
Asset class: US equities | Daily price/volume + fundamental inputs (SEP + SF1-derived)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily pd.Series for a given field AND
    a precomputed peer-median Series of the SAME daily DatetimeIndex named
    peer_median_<field>  (e.g. peer_median_drawdown, peer_median_realized_vol,
    peer_median_rsi14, peer_median_marketcap, peer_median_debt_to_equity,
    peer_median_fcf_yield, peer_median_pb, peer_median_ps).
    The pipeline computes sector/industry medians universe-wide and passes them in.
    All functions are strictly backward-looking.

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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Raw drawdown cross-sectional position ---

def xdr_001_drawdown_ratio_to_peer(drawdown: pd.Series,
                                    peer_median_drawdown: pd.Series) -> pd.Series:
    """Ticker drawdown depth / peer-median drawdown depth (ratio; >1 = worse than peers)."""
    return _rel_ratio(drawdown, peer_median_drawdown)


def xdr_002_drawdown_log_rel_to_peer(drawdown: pd.Series,
                                      peer_median_drawdown: pd.Series) -> pd.Series:
    """Log-relative drawdown vs peer median: log(own / peer)."""
    return _log_rel(drawdown, peer_median_drawdown)


def xdr_003_drawdown_gap_to_peer(drawdown: pd.Series,
                                  peer_median_drawdown: pd.Series) -> pd.Series:
    """Arithmetic gap: ticker drawdown minus peer-median drawdown (negative = worse)."""
    return _gap(drawdown, peer_median_drawdown)


def xdr_004_drawdown_worse_than_peer_flag(drawdown: pd.Series,
                                           peer_median_drawdown: pd.Series) -> pd.Series:
    """Binary flag: 1 if ticker drawdown is deeper (more negative) than peer median."""
    return (drawdown < peer_median_drawdown).astype(float)


def xdr_005_drawdown_ratio_rolling_mean_63d(drawdown: pd.Series,
                                             peer_median_drawdown: pd.Series) -> pd.Series:
    """63-day rolling mean of ticker-vs-peer drawdown ratio."""
    return _rolling_mean(_rel_ratio(drawdown, peer_median_drawdown), _TD_QTR)


def xdr_006_drawdown_ratio_rolling_mean_252d(drawdown: pd.Series,
                                              peer_median_drawdown: pd.Series) -> pd.Series:
    """252-day rolling mean of ticker-vs-peer drawdown ratio."""
    return _rolling_mean(_rel_ratio(drawdown, peer_median_drawdown), _TD_YEAR)


def xdr_007_drawdown_gap_zscore_252d(drawdown: pd.Series,
                                      peer_median_drawdown: pd.Series) -> pd.Series:
    """Z-score of the drawdown gap (own-peer) within its 252-day distribution."""
    return _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)


def xdr_008_drawdown_gap_zscore_63d(drawdown: pd.Series,
                                     peer_median_drawdown: pd.Series) -> pd.Series:
    """Z-score of drawdown gap within trailing 63-day window."""
    return _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_QTR)


def xdr_009_drawdown_excess_depth_21d_mean(drawdown: pd.Series,
                                            peer_median_drawdown: pd.Series) -> pd.Series:
    """21-day mean of the excess drawdown depth vs peers (gap clipped to negative side)."""
    excess = (drawdown - peer_median_drawdown).clip(upper=0.0)
    return _rolling_mean(excess, _TD_MON)


def xdr_010_drawdown_excess_depth_63d_mean(drawdown: pd.Series,
                                            peer_median_drawdown: pd.Series) -> pd.Series:
    """63-day mean of excess drawdown depth vs peers."""
    excess = (drawdown - peer_median_drawdown).clip(upper=0.0)
    return _rolling_mean(excess, _TD_QTR)


def xdr_011_drawdown_pct_rank_21d(drawdown: pd.Series,
                                   peer_median_drawdown: pd.Series) -> pd.Series:
    """21-day rolling pct-rank of the drawdown ratio (low rank = most distressed)."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    return ratio.rolling(_TD_MON, min_periods=max(1, _TD_MON // 2)).rank(pct=True)


def xdr_012_drawdown_pct_rank_252d(drawdown: pd.Series,
                                    peer_median_drawdown: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of the drawdown ratio."""
    ratio = _rel_ratio(drawdown, peer_median_drawdown)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group B (013-024): Volatility cross-sectional position ---

def xdr_013_vol_ratio_to_peer(realized_vol: pd.Series,
                               peer_median_realized_vol: pd.Series) -> pd.Series:
    """Ticker realized volatility / peer-median realized vol (>1 = more volatile than peers)."""
    return _rel_ratio(realized_vol, peer_median_realized_vol)


def xdr_014_vol_log_rel_to_peer(realized_vol: pd.Series,
                                 peer_median_realized_vol: pd.Series) -> pd.Series:
    """Log-relative realized vol vs peers."""
    return _log_rel(realized_vol, peer_median_realized_vol)


def xdr_015_vol_gap_to_peer(realized_vol: pd.Series,
                             peer_median_realized_vol: pd.Series) -> pd.Series:
    """Arithmetic gap: own vol minus peer-median vol."""
    return _gap(realized_vol, peer_median_realized_vol)


def xdr_016_vol_above_peer_flag(realized_vol: pd.Series,
                                 peer_median_realized_vol: pd.Series) -> pd.Series:
    """Binary flag: 1 if ticker vol exceeds peer median."""
    return (realized_vol > peer_median_realized_vol).astype(float)


def xdr_017_vol_ratio_zscore_252d(realized_vol: pd.Series,
                                   peer_median_realized_vol: pd.Series) -> pd.Series:
    """Z-score of vol ratio within trailing 252-day distribution."""
    return _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)


def xdr_018_vol_ratio_zscore_63d(realized_vol: pd.Series,
                                  peer_median_realized_vol: pd.Series) -> pd.Series:
    """Z-score of vol ratio within trailing 63-day window."""
    return _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_QTR)


def xdr_019_vol_ratio_rolling_max_63d(realized_vol: pd.Series,
                                       peer_median_realized_vol: pd.Series) -> pd.Series:
    """63-day rolling maximum of vol ratio (peak vol stress relative to peers)."""
    return _rolling_max(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_QTR)


def xdr_020_vol_ratio_rolling_max_252d(realized_vol: pd.Series,
                                        peer_median_realized_vol: pd.Series) -> pd.Series:
    """252-day rolling maximum of vol ratio."""
    return _rolling_max(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)


def xdr_021_vol_excess_21d_cumsum(realized_vol: pd.Series,
                                   peer_median_realized_vol: pd.Series) -> pd.Series:
    """21-day cumulative sum of excess vol (own - peer), clipped to positive (stress accumulation)."""
    excess = (realized_vol - peer_median_realized_vol).clip(lower=0.0)
    return _rolling_sum(excess, _TD_MON)


def xdr_022_vol_excess_63d_cumsum(realized_vol: pd.Series,
                                   peer_median_realized_vol: pd.Series) -> pd.Series:
    """63-day cumulative sum of excess vol vs peers."""
    excess = (realized_vol - peer_median_realized_vol).clip(lower=0.0)
    return _rolling_sum(excess, _TD_QTR)


def xdr_023_vol_pct_rank_63d(realized_vol: pd.Series,
                              peer_median_realized_vol: pd.Series) -> pd.Series:
    """63-day rolling pct-rank of vol ratio (high rank = most volatility-distressed)."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    return ratio.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def xdr_024_vol_pct_rank_252d(realized_vol: pd.Series,
                               peer_median_realized_vol: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of vol ratio."""
    ratio = _rel_ratio(realized_vol, peer_median_realized_vol)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group C (025-036): Momentum/RSI cross-sectional position ---

def xdr_025_rsi14_gap_to_peer(rsi14: pd.Series,
                               peer_median_rsi14: pd.Series) -> pd.Series:
    """Arithmetic gap: ticker RSI14 minus peer-median RSI14 (negative = weaker momentum)."""
    return _gap(rsi14, peer_median_rsi14)


def xdr_026_rsi14_ratio_to_peer(rsi14: pd.Series,
                                 peer_median_rsi14: pd.Series) -> pd.Series:
    """Ticker RSI14 / peer-median RSI14 ratio."""
    return _rel_ratio(rsi14, peer_median_rsi14)


def xdr_027_rsi14_below_peer_flag(rsi14: pd.Series,
                                   peer_median_rsi14: pd.Series) -> pd.Series:
    """Binary flag: 1 if ticker RSI14 is below peer-median RSI14."""
    return (rsi14 < peer_median_rsi14).astype(float)


def xdr_028_rsi14_peer_gap_zscore_252d(rsi14: pd.Series,
                                        peer_median_rsi14: pd.Series) -> pd.Series:
    """Z-score of RSI14 peer gap within 252-day distribution."""
    return _zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)


def xdr_029_rsi14_peer_gap_zscore_63d(rsi14: pd.Series,
                                       peer_median_rsi14: pd.Series) -> pd.Series:
    """Z-score of RSI14 peer gap within 63-day window."""
    return _zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_QTR)


def xdr_030_rsi14_peer_gap_rolling_min_63d(rsi14: pd.Series,
                                            peer_median_rsi14: pd.Series) -> pd.Series:
    """63-day rolling minimum of RSI14 peer gap (worst relative momentum in quarter)."""
    return _rolling_min(_gap(rsi14, peer_median_rsi14), _TD_QTR)


def xdr_031_rsi14_peer_gap_rolling_min_252d(rsi14: pd.Series,
                                             peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day rolling minimum of RSI14 peer gap."""
    return _rolling_min(_gap(rsi14, peer_median_rsi14), _TD_YEAR)


def xdr_032_rsi14_consec_below_peer_streak(rsi14: pd.Series,
                                            peer_median_rsi14: pd.Series) -> pd.Series:
    """Consecutive days ticker RSI14 has been below peer-median RSI14."""
    return _consec_streak(rsi14 < peer_median_rsi14)


def xdr_033_rsi14_below_peer_days_in_63d(rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series) -> pd.Series:
    """Count of days ticker RSI14 < peer-median RSI14 in trailing 63 days."""
    return _rolling_sum((rsi14 < peer_median_rsi14).astype(float), _TD_QTR)


def xdr_034_rsi14_below_peer_days_in_252d(rsi14: pd.Series,
                                           peer_median_rsi14: pd.Series) -> pd.Series:
    """Count of days ticker RSI14 < peer-median RSI14 in trailing 252 days."""
    return _rolling_sum((rsi14 < peer_median_rsi14).astype(float), _TD_YEAR)


def xdr_035_rsi14_peer_gap_pct_rank_63d(rsi14: pd.Series,
                                         peer_median_rsi14: pd.Series) -> pd.Series:
    """63-day rolling pct-rank of RSI14 peer gap (low = worst relative momentum)."""
    gap = _gap(rsi14, peer_median_rsi14)
    return gap.rolling(_TD_QTR, min_periods=max(1, _TD_QTR // 2)).rank(pct=True)


def xdr_036_rsi14_peer_gap_pct_rank_252d(rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of RSI14 peer gap."""
    gap = _gap(rsi14, peer_median_rsi14)
    return gap.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group D (037-048): Market-cap cross-sectional position ---

def xdr_037_marketcap_ratio_to_peer(marketcap: pd.Series,
                                     peer_median_marketcap: pd.Series) -> pd.Series:
    """Ticker market cap / peer-median market cap (compression = shrinkage vs peers)."""
    return _rel_ratio(marketcap, peer_median_marketcap)


def xdr_038_marketcap_log_rel_to_peer(marketcap: pd.Series,
                                       peer_median_marketcap: pd.Series) -> pd.Series:
    """Log-relative market cap vs peer median."""
    return _log_rel(marketcap, peer_median_marketcap)


def xdr_039_marketcap_ratio_zscore_252d(marketcap: pd.Series,
                                         peer_median_marketcap: pd.Series) -> pd.Series:
    """Z-score of market-cap ratio within 252-day distribution."""
    return _zscore_rolling(_rel_ratio(marketcap, peer_median_marketcap), _TD_YEAR)


def xdr_040_marketcap_ratio_rolling_min_252d(marketcap: pd.Series,
                                              peer_median_marketcap: pd.Series) -> pd.Series:
    """252-day rolling minimum of market-cap ratio (deepest cap compression vs peers)."""
    return _rolling_min(_rel_ratio(marketcap, peer_median_marketcap), _TD_YEAR)


def xdr_041_marketcap_pct_rank_252d(marketcap: pd.Series,
                                     peer_median_marketcap: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of market-cap ratio (low rank = most cap-compressed)."""
    ratio = _rel_ratio(marketcap, peer_median_marketcap)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_042_marketcap_below_peer_flag(marketcap: pd.Series,
                                       peer_median_marketcap: pd.Series) -> pd.Series:
    """Binary flag: 1 if ticker market cap is below peer median."""
    return (marketcap < peer_median_marketcap).astype(float)


def xdr_043_marketcap_ratio_ema_63d(marketcap: pd.Series,
                                     peer_median_marketcap: pd.Series) -> pd.Series:
    """63-day EMA of market-cap ratio (smoothed relative size)."""
    return _ewm_mean(_rel_ratio(marketcap, peer_median_marketcap), _TD_QTR)


def xdr_044_marketcap_log_rel_zscore_252d(marketcap: pd.Series,
                                           peer_median_marketcap: pd.Series) -> pd.Series:
    """Z-score of log-relative market-cap within trailing 252 days."""
    return _zscore_rolling(_log_rel(marketcap, peer_median_marketcap), _TD_YEAR)


# --- Group E (045-056): Leverage (debt-to-equity) cross-sectional position ---

def xdr_045_de_ratio_to_peer(debt_to_equity: pd.Series,
                              peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Ticker D/E ratio / peer-median D/E (>1 = more leveraged than peers)."""
    return _rel_ratio(debt_to_equity, peer_median_debt_to_equity)


def xdr_046_de_log_rel_to_peer(debt_to_equity: pd.Series,
                                peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Log-relative D/E vs peer median."""
    return _log_rel(debt_to_equity, peer_median_debt_to_equity)


def xdr_047_de_gap_to_peer(debt_to_equity: pd.Series,
                            peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Arithmetic gap: own D/E minus peer-median D/E."""
    return _gap(debt_to_equity, peer_median_debt_to_equity)


def xdr_048_de_above_peer_flag(debt_to_equity: pd.Series,
                                peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Binary flag: 1 if ticker D/E is above peer median (more leveraged)."""
    return (debt_to_equity > peer_median_debt_to_equity).astype(float)


def xdr_049_de_ratio_zscore_252d(debt_to_equity: pd.Series,
                                  peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Z-score of D/E ratio within trailing 252-day distribution."""
    return _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)


def xdr_050_de_ratio_rolling_max_252d(debt_to_equity: pd.Series,
                                       peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """252-day rolling maximum of D/E ratio vs peers (leverage peak)."""
    return _rolling_max(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)


def xdr_051_de_pct_rank_252d(debt_to_equity: pd.Series,
                              peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of D/E ratio (high rank = most leveraged vs peers)."""
    ratio = _rel_ratio(debt_to_equity, peer_median_debt_to_equity)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_052_de_excess_21d_days(debt_to_equity: pd.Series,
                                peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Count of days in trailing 21d where D/E exceeds peer median."""
    return _rolling_sum((debt_to_equity > peer_median_debt_to_equity).astype(float), _TD_MON)


# --- Group F (053-063): FCF-yield cross-sectional position ---

def xdr_053_fcf_ratio_to_peer(fcf_yield: pd.Series,
                               peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Ticker FCF yield / peer-median FCF yield (low or negative = cash-flow distressed)."""
    return _rel_ratio(fcf_yield, peer_median_fcf_yield)


def xdr_054_fcf_gap_to_peer(fcf_yield: pd.Series,
                             peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Arithmetic gap: own FCF yield minus peer-median FCF yield."""
    return _gap(fcf_yield, peer_median_fcf_yield)


def xdr_055_fcf_below_peer_flag(fcf_yield: pd.Series,
                                 peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Binary flag: 1 if ticker FCF yield is below peer median."""
    return (fcf_yield < peer_median_fcf_yield).astype(float)


def xdr_056_fcf_gap_zscore_252d(fcf_yield: pd.Series,
                                 peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Z-score of FCF-yield gap within trailing 252-day distribution."""
    return _zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)


def xdr_057_fcf_gap_rolling_min_252d(fcf_yield: pd.Series,
                                      peer_median_fcf_yield: pd.Series) -> pd.Series:
    """252-day rolling minimum of FCF-yield gap (worst cash-flow position vs peers)."""
    return _rolling_min(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)


def xdr_058_fcf_pct_rank_252d(fcf_yield: pd.Series,
                               peer_median_fcf_yield: pd.Series) -> pd.Series:
    """252-day pct-rank of FCF-yield gap (low rank = most cash-flow distressed)."""
    gap = _gap(fcf_yield, peer_median_fcf_yield)
    return gap.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_059_fcf_below_peer_days_63d(fcf_yield: pd.Series,
                                     peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Days ticker FCF yield was below peer median in trailing 63 days."""
    return _rolling_sum((fcf_yield < peer_median_fcf_yield).astype(float), _TD_QTR)


# --- Group G (060-075): Multi-dimension composite distress rank ---

def xdr_060_pb_ratio_to_peer(pb: pd.Series,
                              peer_median_pb: pd.Series) -> pd.Series:
    """Ticker P/B / peer-median P/B (valuation compression vs peers)."""
    return _rel_ratio(pb, peer_median_pb)


def xdr_061_pb_log_rel_to_peer(pb: pd.Series,
                                peer_median_pb: pd.Series) -> pd.Series:
    """Log-relative P/B vs peer median."""
    return _log_rel(pb, peer_median_pb)


def xdr_062_pb_pct_rank_252d(pb: pd.Series,
                              peer_median_pb: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of P/B ratio vs peers (low rank = most compressed)."""
    ratio = _rel_ratio(pb, peer_median_pb)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_063_ps_ratio_to_peer(ps: pd.Series,
                              peer_median_ps: pd.Series) -> pd.Series:
    """Ticker P/S / peer-median P/S."""
    return _rel_ratio(ps, peer_median_ps)


def xdr_064_ps_log_rel_to_peer(ps: pd.Series,
                                peer_median_ps: pd.Series) -> pd.Series:
    """Log-relative P/S vs peer median."""
    return _log_rel(ps, peer_median_ps)


def xdr_065_ps_pct_rank_252d(ps: pd.Series,
                              peer_median_ps: pd.Series) -> pd.Series:
    """252-day rolling pct-rank of P/S ratio vs peers."""
    ratio = _rel_ratio(ps, peer_median_ps)
    return ratio.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_066_composite_distress_rank_3dim(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series,
                                          realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series,
                                          rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series) -> pd.Series:
    """Composite distress rank: average of drawdown gap z-score, vol ratio z-score,
    and inverted RSI gap z-score across 252-day window.  Higher = more distressed."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    return (z_dd + z_vol + z_rsi) / 3.0


def xdr_067_composite_distress_rank_5dim(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series,
                                          realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series,
                                          rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series,
                                          debt_to_equity: pd.Series,
                                          peer_median_debt_to_equity: pd.Series,
                                          fcf_yield: pd.Series,
                                          peer_median_fcf_yield: pd.Series) -> pd.Series:
    """5-dimension composite: drawdown + vol + RSI + leverage + FCF z-scores averaged."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    return (z_dd + z_vol + z_rsi + z_de + z_fcf) / 5.0


def xdr_068_composite_pct_rank_3dim_252d(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series,
                                          realized_vol: pd.Series,
                                          peer_median_realized_vol: pd.Series,
                                          rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series) -> pd.Series:
    """252-day pct-rank of 3-dim composite distress score."""
    composite = xdr_066_composite_distress_rank_3dim(
        drawdown, peer_median_drawdown,
        realized_vol, peer_median_realized_vol,
        rsi14, peer_median_rsi14)
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_069_extreme_distress_all_dims_flag(drawdown: pd.Series,
                                            peer_median_drawdown: pd.Series,
                                            realized_vol: pd.Series,
                                            peer_median_realized_vol: pd.Series,
                                            rsi14: pd.Series,
                                            peer_median_rsi14: pd.Series) -> pd.Series:
    """Binary: 1 if ticker is worse than peer median on ALL three distress dims."""
    dd_worse  = (drawdown < peer_median_drawdown)
    vol_worse = (realized_vol > peer_median_realized_vol)
    rsi_worse = (rsi14 < peer_median_rsi14)
    return (dd_worse & vol_worse & rsi_worse).astype(float)


def xdr_070_distress_dim_count_below_peer(drawdown: pd.Series,
                                           peer_median_drawdown: pd.Series,
                                           realized_vol: pd.Series,
                                           peer_median_realized_vol: pd.Series,
                                           rsi14: pd.Series,
                                           peer_median_rsi14: pd.Series,
                                           debt_to_equity: pd.Series,
                                           peer_median_debt_to_equity: pd.Series,
                                           fcf_yield: pd.Series,
                                           peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Count of distress dimensions where ticker is worse than peer (0-5 scale)."""
    d1 = (drawdown < peer_median_drawdown).astype(float)
    d2 = (realized_vol > peer_median_realized_vol).astype(float)
    d3 = (rsi14 < peer_median_rsi14).astype(float)
    d4 = (debt_to_equity > peer_median_debt_to_equity).astype(float)
    d5 = (fcf_yield < peer_median_fcf_yield).astype(float)
    return d1 + d2 + d3 + d4 + d5


def xdr_071_distress_dim_count_21d_mean(drawdown: pd.Series,
                                         peer_median_drawdown: pd.Series,
                                         realized_vol: pd.Series,
                                         peer_median_realized_vol: pd.Series,
                                         rsi14: pd.Series,
                                         peer_median_rsi14: pd.Series,
                                         debt_to_equity: pd.Series,
                                         peer_median_debt_to_equity: pd.Series,
                                         fcf_yield: pd.Series,
                                         peer_median_fcf_yield: pd.Series) -> pd.Series:
    """21-day rolling mean of 5-dimension distress count."""
    count = xdr_070_distress_dim_count_below_peer(
        drawdown, peer_median_drawdown,
        realized_vol, peer_median_realized_vol,
        rsi14, peer_median_rsi14,
        debt_to_equity, peer_median_debt_to_equity,
        fcf_yield, peer_median_fcf_yield)
    return _rolling_mean(count, _TD_MON)


def xdr_072_drawdown_vol_joint_zscore(drawdown: pd.Series,
                                       peer_median_drawdown: pd.Series,
                                       realized_vol: pd.Series,
                                       peer_median_realized_vol: pd.Series) -> pd.Series:
    """Joint z-score: drawdown gap z + vol ratio z (2-dim price-distress composite)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    return (z_dd + z_vol) / 2.0


def xdr_073_leverage_valuation_joint_zscore(debt_to_equity: pd.Series,
                                             peer_median_debt_to_equity: pd.Series,
                                             pb: pd.Series,
                                             peer_median_pb: pd.Series) -> pd.Series:
    """Joint z-score: D/E ratio z + inverted P/B ratio z (fundamental-distress composite)."""
    z_de = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_pb = -_zscore_rolling(_rel_ratio(pb, peer_median_pb), _TD_YEAR)
    return (z_de + z_pb) / 2.0


def xdr_074_composite_distress_pct_rank_5dim_252d(drawdown: pd.Series,
                                                    peer_median_drawdown: pd.Series,
                                                    realized_vol: pd.Series,
                                                    peer_median_realized_vol: pd.Series,
                                                    rsi14: pd.Series,
                                                    peer_median_rsi14: pd.Series,
                                                    debt_to_equity: pd.Series,
                                                    peer_median_debt_to_equity: pd.Series,
                                                    fcf_yield: pd.Series,
                                                    peer_median_fcf_yield: pd.Series) -> pd.Series:
    """252-day pct-rank of 5-dim composite distress score."""
    composite = xdr_067_composite_distress_rank_5dim(
        drawdown, peer_median_drawdown,
        realized_vol, peer_median_realized_vol,
        rsi14, peer_median_rsi14,
        debt_to_equity, peer_median_debt_to_equity,
        fcf_yield, peer_median_fcf_yield)
    return composite.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


def xdr_075_composite_distress_expanding_pct_rank(drawdown: pd.Series,
                                                    peer_median_drawdown: pd.Series,
                                                    realized_vol: pd.Series,
                                                    peer_median_realized_vol: pd.Series,
                                                    rsi14: pd.Series,
                                                    peer_median_rsi14: pd.Series) -> pd.Series:
    """Expanding all-time pct-rank of 3-dim composite distress score."""
    composite = xdr_066_composite_distress_rank_3dim(
        drawdown, peer_median_drawdown,
        realized_vol, peer_median_realized_vol,
        rsi14, peer_median_rsi14)
    return composite.expanding(min_periods=_TD_QTR).rank(pct=True)


# ── Registry ──────────────────────────────────────────────────────────────────

CROSS_SECTIONAL_DISTRESS_RANK_REGISTRY_001_075 = {
    "xdr_001_drawdown_ratio_to_peer": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_001_drawdown_ratio_to_peer},
    "xdr_002_drawdown_log_rel_to_peer": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_002_drawdown_log_rel_to_peer},
    "xdr_003_drawdown_gap_to_peer": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_003_drawdown_gap_to_peer},
    "xdr_004_drawdown_worse_than_peer_flag": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_004_drawdown_worse_than_peer_flag},
    "xdr_005_drawdown_ratio_rolling_mean_63d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_005_drawdown_ratio_rolling_mean_63d},
    "xdr_006_drawdown_ratio_rolling_mean_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_006_drawdown_ratio_rolling_mean_252d},
    "xdr_007_drawdown_gap_zscore_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_007_drawdown_gap_zscore_252d},
    "xdr_008_drawdown_gap_zscore_63d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_008_drawdown_gap_zscore_63d},
    "xdr_009_drawdown_excess_depth_21d_mean": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_009_drawdown_excess_depth_21d_mean},
    "xdr_010_drawdown_excess_depth_63d_mean": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_010_drawdown_excess_depth_63d_mean},
    "xdr_011_drawdown_pct_rank_21d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_011_drawdown_pct_rank_21d},
    "xdr_012_drawdown_pct_rank_252d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_012_drawdown_pct_rank_252d},
    "xdr_013_vol_ratio_to_peer": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_013_vol_ratio_to_peer},
    "xdr_014_vol_log_rel_to_peer": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_014_vol_log_rel_to_peer},
    "xdr_015_vol_gap_to_peer": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_015_vol_gap_to_peer},
    "xdr_016_vol_above_peer_flag": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_016_vol_above_peer_flag},
    "xdr_017_vol_ratio_zscore_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_017_vol_ratio_zscore_252d},
    "xdr_018_vol_ratio_zscore_63d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_018_vol_ratio_zscore_63d},
    "xdr_019_vol_ratio_rolling_max_63d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_019_vol_ratio_rolling_max_63d},
    "xdr_020_vol_ratio_rolling_max_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_020_vol_ratio_rolling_max_252d},
    "xdr_021_vol_excess_21d_cumsum": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_021_vol_excess_21d_cumsum},
    "xdr_022_vol_excess_63d_cumsum": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_022_vol_excess_63d_cumsum},
    "xdr_023_vol_pct_rank_63d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_023_vol_pct_rank_63d},
    "xdr_024_vol_pct_rank_252d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_024_vol_pct_rank_252d},
    "xdr_025_rsi14_gap_to_peer": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_025_rsi14_gap_to_peer},
    "xdr_026_rsi14_ratio_to_peer": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_026_rsi14_ratio_to_peer},
    "xdr_027_rsi14_below_peer_flag": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_027_rsi14_below_peer_flag},
    "xdr_028_rsi14_peer_gap_zscore_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_028_rsi14_peer_gap_zscore_252d},
    "xdr_029_rsi14_peer_gap_zscore_63d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_029_rsi14_peer_gap_zscore_63d},
    "xdr_030_rsi14_peer_gap_rolling_min_63d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_030_rsi14_peer_gap_rolling_min_63d},
    "xdr_031_rsi14_peer_gap_rolling_min_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_031_rsi14_peer_gap_rolling_min_252d},
    "xdr_032_rsi14_consec_below_peer_streak": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_032_rsi14_consec_below_peer_streak},
    "xdr_033_rsi14_below_peer_days_in_63d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_033_rsi14_below_peer_days_in_63d},
    "xdr_034_rsi14_below_peer_days_in_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_034_rsi14_below_peer_days_in_252d},
    "xdr_035_rsi14_peer_gap_pct_rank_63d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_035_rsi14_peer_gap_pct_rank_63d},
    "xdr_036_rsi14_peer_gap_pct_rank_252d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_036_rsi14_peer_gap_pct_rank_252d},
    "xdr_037_marketcap_ratio_to_peer": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_037_marketcap_ratio_to_peer},
    "xdr_038_marketcap_log_rel_to_peer": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_038_marketcap_log_rel_to_peer},
    "xdr_039_marketcap_ratio_zscore_252d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_039_marketcap_ratio_zscore_252d},
    "xdr_040_marketcap_ratio_rolling_min_252d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_040_marketcap_ratio_rolling_min_252d},
    "xdr_041_marketcap_pct_rank_252d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_041_marketcap_pct_rank_252d},
    "xdr_042_marketcap_below_peer_flag": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_042_marketcap_below_peer_flag},
    "xdr_043_marketcap_ratio_ema_63d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_043_marketcap_ratio_ema_63d},
    "xdr_044_marketcap_log_rel_zscore_252d": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_044_marketcap_log_rel_zscore_252d},
    "xdr_045_de_ratio_to_peer": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_045_de_ratio_to_peer},
    "xdr_046_de_log_rel_to_peer": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_046_de_log_rel_to_peer},
    "xdr_047_de_gap_to_peer": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_047_de_gap_to_peer},
    "xdr_048_de_above_peer_flag": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_048_de_above_peer_flag},
    "xdr_049_de_ratio_zscore_252d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_049_de_ratio_zscore_252d},
    "xdr_050_de_ratio_rolling_max_252d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_050_de_ratio_rolling_max_252d},
    "xdr_051_de_pct_rank_252d": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_051_de_pct_rank_252d},
    "xdr_052_de_excess_21d_days": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_052_de_excess_21d_days},
    "xdr_053_fcf_ratio_to_peer": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_053_fcf_ratio_to_peer},
    "xdr_054_fcf_gap_to_peer": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_054_fcf_gap_to_peer},
    "xdr_055_fcf_below_peer_flag": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_055_fcf_below_peer_flag},
    "xdr_056_fcf_gap_zscore_252d": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_056_fcf_gap_zscore_252d},
    "xdr_057_fcf_gap_rolling_min_252d": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_057_fcf_gap_rolling_min_252d},
    "xdr_058_fcf_pct_rank_252d": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_058_fcf_pct_rank_252d},
    "xdr_059_fcf_below_peer_days_63d": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_059_fcf_below_peer_days_63d},
    "xdr_060_pb_ratio_to_peer": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_060_pb_ratio_to_peer},
    "xdr_061_pb_log_rel_to_peer": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_061_pb_log_rel_to_peer},
    "xdr_062_pb_pct_rank_252d": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_062_pb_pct_rank_252d},
    "xdr_063_ps_ratio_to_peer": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_063_ps_ratio_to_peer},
    "xdr_064_ps_log_rel_to_peer": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_064_ps_log_rel_to_peer},
    "xdr_065_ps_pct_rank_252d": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_065_ps_pct_rank_252d},
    "xdr_066_composite_distress_rank_3dim": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_066_composite_distress_rank_3dim},
    "xdr_067_composite_distress_rank_5dim": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_067_composite_distress_rank_5dim},
    "xdr_068_composite_pct_rank_3dim_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_068_composite_pct_rank_3dim_252d},
    "xdr_069_extreme_distress_all_dims_flag": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_069_extreme_distress_all_dims_flag},
    "xdr_070_distress_dim_count_below_peer": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_070_distress_dim_count_below_peer},
    "xdr_071_distress_dim_count_21d_mean": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_071_distress_dim_count_21d_mean},
    "xdr_072_drawdown_vol_joint_zscore": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol"],
        "func": xdr_072_drawdown_vol_joint_zscore},
    "xdr_073_leverage_valuation_joint_zscore": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity",
                   "pb", "peer_median_pb"],
        "func": xdr_073_leverage_valuation_joint_zscore},
    "xdr_074_composite_distress_pct_rank_5dim_252d": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_074_composite_distress_pct_rank_5dim_252d},
    "xdr_075_composite_distress_expanding_pct_rank": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_075_composite_distress_expanding_pct_rank},
}
