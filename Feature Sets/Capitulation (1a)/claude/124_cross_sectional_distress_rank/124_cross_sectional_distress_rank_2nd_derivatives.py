"""
124_cross_sectional_distress_rank — 2nd Derivatives (Features xdr_drv2_001-025)
Domain: rate of change of base cross-sectional distress rank features — velocity of
        relative distress positioning vs peers (drawdown, vol, RSI, leverage, valuation)
Asset class: US equities | Daily price/volume + fundamental inputs (SEP + SF1-derived)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily pd.Series AND a precomputed
    peer-median Series of the SAME daily DatetimeIndex (peer_median_<field>).
    2nd-derivative = diff or slope applied to a base feature value.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    return _safe_div(own, peer)


def _gap(own: pd.Series, peer: pd.Series) -> pd.Series:
    return own - peer


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def xdr_drv2_001_drawdown_ratio_5d_diff(drawdown: pd.Series,
                                         peer_median_drawdown: pd.Series) -> pd.Series:
    """5-day diff of drawdown ratio (velocity of relative drawdown stress)."""
    return _rel_ratio(drawdown, peer_median_drawdown).diff(_TD_WEEK)


def xdr_drv2_002_drawdown_ratio_21d_diff(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series) -> pd.Series:
    """21-day diff of drawdown ratio vs peers."""
    return _rel_ratio(drawdown, peer_median_drawdown).diff(_TD_MON)


def xdr_drv2_003_drawdown_gap_zscore_5d_diff(drawdown: pd.Series,
                                              peer_median_drawdown: pd.Series) -> pd.Series:
    """5-day diff of drawdown gap z-score (velocity of relative drawdown z-score)."""
    z = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    return z.diff(_TD_WEEK)


def xdr_drv2_004_vol_ratio_5d_diff(realized_vol: pd.Series,
                                    peer_median_realized_vol: pd.Series) -> pd.Series:
    """5-day diff of vol ratio (velocity of relative vol stress)."""
    return _rel_ratio(realized_vol, peer_median_realized_vol).diff(_TD_WEEK)


def xdr_drv2_005_vol_ratio_21d_diff(realized_vol: pd.Series,
                                     peer_median_realized_vol: pd.Series) -> pd.Series:
    """21-day diff of vol ratio vs peers."""
    return _rel_ratio(realized_vol, peer_median_realized_vol).diff(_TD_MON)


def xdr_drv2_006_vol_ratio_zscore_5d_diff(realized_vol: pd.Series,
                                           peer_median_realized_vol: pd.Series) -> pd.Series:
    """5-day diff of vol ratio z-score."""
    z = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    return z.diff(_TD_WEEK)


def xdr_drv2_007_rsi14_peer_gap_5d_diff(rsi14: pd.Series,
                                          peer_median_rsi14: pd.Series) -> pd.Series:
    """5-day diff of RSI14 peer gap (velocity of relative momentum divergence)."""
    return _gap(rsi14, peer_median_rsi14).diff(_TD_WEEK)


def xdr_drv2_008_rsi14_peer_gap_21d_diff(rsi14: pd.Series,
                                           peer_median_rsi14: pd.Series) -> pd.Series:
    """21-day diff of RSI14 peer gap."""
    return _gap(rsi14, peer_median_rsi14).diff(_TD_MON)


def xdr_drv2_009_rsi14_peer_gap_zscore_5d_diff(rsi14: pd.Series,
                                                 peer_median_rsi14: pd.Series) -> pd.Series:
    """5-day diff of RSI14 peer-gap z-score."""
    z = _zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    return z.diff(_TD_WEEK)


def xdr_drv2_010_de_ratio_5d_diff(debt_to_equity: pd.Series,
                                    peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """5-day diff of D/E ratio vs peers (velocity of leverage distress)."""
    return _rel_ratio(debt_to_equity, peer_median_debt_to_equity).diff(_TD_WEEK)


def xdr_drv2_011_de_ratio_21d_diff(debt_to_equity: pd.Series,
                                    peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """21-day diff of D/E ratio vs peers."""
    return _rel_ratio(debt_to_equity, peer_median_debt_to_equity).diff(_TD_MON)


def xdr_drv2_012_fcf_gap_5d_diff(fcf_yield: pd.Series,
                                   peer_median_fcf_yield: pd.Series) -> pd.Series:
    """5-day diff of FCF yield gap vs peers (velocity of cash-flow distress)."""
    return _gap(fcf_yield, peer_median_fcf_yield).diff(_TD_WEEK)


def xdr_drv2_013_pb_ratio_5d_diff(pb: pd.Series,
                                    peer_median_pb: pd.Series) -> pd.Series:
    """5-day diff of P/B ratio vs peers (velocity of valuation compression)."""
    return _rel_ratio(pb, peer_median_pb).diff(_TD_WEEK)


def xdr_drv2_014_composite_z3_5d_diff(drawdown: pd.Series,
                                        peer_median_drawdown: pd.Series,
                                        realized_vol: pd.Series,
                                        peer_median_realized_vol: pd.Series,
                                        rsi14: pd.Series,
                                        peer_median_rsi14: pd.Series) -> pd.Series:
    """5-day diff of 3-dim composite distress z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return composite.diff(_TD_WEEK)


def xdr_drv2_015_composite_z3_21d_diff(drawdown: pd.Series,
                                         peer_median_drawdown: pd.Series,
                                         realized_vol: pd.Series,
                                         peer_median_realized_vol: pd.Series,
                                         rsi14: pd.Series,
                                         peer_median_rsi14: pd.Series) -> pd.Series:
    """21-day diff of 3-dim composite distress z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    return composite.diff(_TD_MON)


def xdr_drv2_016_drawdown_ratio_slope_5d(drawdown: pd.Series,
                                          peer_median_drawdown: pd.Series) -> pd.Series:
    """OLS slope over 5 days of drawdown ratio (instantaneous velocity)."""
    return _linslope(_rel_ratio(drawdown, peer_median_drawdown), _TD_WEEK)


def xdr_drv2_017_vol_ratio_slope_5d(realized_vol: pd.Series,
                                     peer_median_realized_vol: pd.Series) -> pd.Series:
    """OLS slope over 5 days of vol ratio vs peers."""
    return _linslope(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_WEEK)


def xdr_drv2_018_rsi14_peer_gap_slope_5d(rsi14: pd.Series,
                                           peer_median_rsi14: pd.Series) -> pd.Series:
    """OLS slope over 5 days of RSI14 peer gap."""
    return _linslope(_gap(rsi14, peer_median_rsi14), _TD_WEEK)


def xdr_drv2_019_marketcap_ratio_5d_diff(marketcap: pd.Series,
                                          peer_median_marketcap: pd.Series) -> pd.Series:
    """5-day diff of market-cap ratio vs peers (velocity of size compression)."""
    return _rel_ratio(marketcap, peer_median_marketcap).diff(_TD_WEEK)


def xdr_drv2_020_marketcap_ratio_21d_diff(marketcap: pd.Series,
                                           peer_median_marketcap: pd.Series) -> pd.Series:
    """21-day diff of market-cap ratio vs peers."""
    return _rel_ratio(marketcap, peer_median_marketcap).diff(_TD_MON)


def xdr_drv2_021_drawdown_gap_zscore_21d_diff(drawdown: pd.Series,
                                               peer_median_drawdown: pd.Series) -> pd.Series:
    """21-day diff of drawdown gap z-score."""
    z = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    return z.diff(_TD_MON)


def xdr_drv2_022_distress_dim_count_5d_diff(drawdown: pd.Series,
                                             peer_median_drawdown: pd.Series,
                                             realized_vol: pd.Series,
                                             peer_median_realized_vol: pd.Series,
                                             rsi14: pd.Series,
                                             peer_median_rsi14: pd.Series,
                                             debt_to_equity: pd.Series,
                                             peer_median_debt_to_equity: pd.Series,
                                             fcf_yield: pd.Series,
                                             peer_median_fcf_yield: pd.Series) -> pd.Series:
    """5-day diff of 5-dim distress count (velocity of breadth change)."""
    count = ((drawdown < peer_median_drawdown).astype(float) +
             (realized_vol > peer_median_realized_vol).astype(float) +
             (rsi14 < peer_median_rsi14).astype(float) +
             (debt_to_equity > peer_median_debt_to_equity).astype(float) +
             (fcf_yield < peer_median_fcf_yield).astype(float))
    return count.diff(_TD_WEEK)


def xdr_drv2_023_pb_ratio_21d_diff(pb: pd.Series,
                                    peer_median_pb: pd.Series) -> pd.Series:
    """21-day diff of P/B ratio vs peers."""
    return _rel_ratio(pb, peer_median_pb).diff(_TD_MON)


def xdr_drv2_024_ps_ratio_5d_diff(ps: pd.Series,
                                   peer_median_ps: pd.Series) -> pd.Series:
    """5-day diff of P/S ratio vs peers (velocity of revenue-multiple compression)."""
    return _rel_ratio(ps, peer_median_ps).diff(_TD_WEEK)


def xdr_drv2_025_composite_z5_5d_diff(drawdown: pd.Series,
                                        peer_median_drawdown: pd.Series,
                                        realized_vol: pd.Series,
                                        peer_median_realized_vol: pd.Series,
                                        rsi14: pd.Series,
                                        peer_median_rsi14: pd.Series,
                                        debt_to_equity: pd.Series,
                                        peer_median_debt_to_equity: pd.Series,
                                        fcf_yield: pd.Series,
                                        peer_median_fcf_yield: pd.Series) -> pd.Series:
    """5-day diff of 5-dim composite distress z-score (velocity of total distress)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi + z_de + z_fcf) / 5.0
    return composite.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CROSS_SECTIONAL_DISTRESS_RANK_REGISTRY_2ND_DERIVATIVES = {
    "xdr_drv2_001_drawdown_ratio_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv2_001_drawdown_ratio_5d_diff},
    "xdr_drv2_002_drawdown_ratio_21d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv2_002_drawdown_ratio_21d_diff},
    "xdr_drv2_003_drawdown_gap_zscore_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv2_003_drawdown_gap_zscore_5d_diff},
    "xdr_drv2_004_vol_ratio_5d_diff": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv2_004_vol_ratio_5d_diff},
    "xdr_drv2_005_vol_ratio_21d_diff": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv2_005_vol_ratio_21d_diff},
    "xdr_drv2_006_vol_ratio_zscore_5d_diff": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv2_006_vol_ratio_zscore_5d_diff},
    "xdr_drv2_007_rsi14_peer_gap_5d_diff": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_drv2_007_rsi14_peer_gap_5d_diff},
    "xdr_drv2_008_rsi14_peer_gap_21d_diff": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_drv2_008_rsi14_peer_gap_21d_diff},
    "xdr_drv2_009_rsi14_peer_gap_zscore_5d_diff": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_drv2_009_rsi14_peer_gap_zscore_5d_diff},
    "xdr_drv2_010_de_ratio_5d_diff": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_drv2_010_de_ratio_5d_diff},
    "xdr_drv2_011_de_ratio_21d_diff": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_drv2_011_de_ratio_21d_diff},
    "xdr_drv2_012_fcf_gap_5d_diff": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_drv2_012_fcf_gap_5d_diff},
    "xdr_drv2_013_pb_ratio_5d_diff": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_drv2_013_pb_ratio_5d_diff},
    "xdr_drv2_014_composite_z3_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_drv2_014_composite_z3_5d_diff},
    "xdr_drv2_015_composite_z3_21d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_drv2_015_composite_z3_21d_diff},
    "xdr_drv2_016_drawdown_ratio_slope_5d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv2_016_drawdown_ratio_slope_5d},
    "xdr_drv2_017_vol_ratio_slope_5d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv2_017_vol_ratio_slope_5d},
    "xdr_drv2_018_rsi14_peer_gap_slope_5d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_drv2_018_rsi14_peer_gap_slope_5d},
    "xdr_drv2_019_marketcap_ratio_5d_diff": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_drv2_019_marketcap_ratio_5d_diff},
    "xdr_drv2_020_marketcap_ratio_21d_diff": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_drv2_020_marketcap_ratio_21d_diff},
    "xdr_drv2_021_drawdown_gap_zscore_21d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv2_021_drawdown_gap_zscore_21d_diff},
    "xdr_drv2_022_distress_dim_count_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_drv2_022_distress_dim_count_5d_diff},
    "xdr_drv2_023_pb_ratio_21d_diff": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_drv2_023_pb_ratio_21d_diff},
    "xdr_drv2_024_ps_ratio_5d_diff": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_drv2_024_ps_ratio_5d_diff},
    "xdr_drv2_025_composite_z5_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_drv2_025_composite_z5_5d_diff},
}
