"""
124_cross_sectional_distress_rank — 3rd Derivatives (Features xdr_drv3_001-025)
Domain: rate of change of 2nd-derivative cross-sectional distress rank features —
        acceleration of relative distress positioning velocity vs peers
Asset class: US equities | Daily price/volume + fundamental inputs (SEP + SF1-derived)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily pd.Series AND a precomputed
    peer-median Series of the SAME daily DatetimeIndex (peer_median_<field>).
    3rd-derivative = diff or slope applied to a 2nd-derivative concept.
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


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────
# Each 3rd-derivative = diff/slope applied to a 2nd-derivative concept.

def xdr_drv3_001_drawdown_ratio_5d_diff_5d_diff(drawdown: pd.Series,
                                                  peer_median_drawdown: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown ratio (acceleration of relative drawdown velocity)."""
    vel = _rel_ratio(drawdown, peer_median_drawdown).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_002_drawdown_ratio_21d_diff_5d_diff(drawdown: pd.Series,
                                                   peer_median_drawdown: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of drawdown ratio (jerk in monthly relative drawdown)."""
    vel21 = _rel_ratio(drawdown, peer_median_drawdown).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def xdr_drv3_003_vol_ratio_5d_diff_5d_diff(realized_vol: pd.Series,
                                            peer_median_realized_vol: pd.Series) -> pd.Series:
    """Second 5-day diff of vol ratio (acceleration of relative vol stress)."""
    vel = _rel_ratio(realized_vol, peer_median_realized_vol).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_004_vol_ratio_21d_diff_5d_diff(realized_vol: pd.Series,
                                              peer_median_realized_vol: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of vol ratio."""
    vel21 = _rel_ratio(realized_vol, peer_median_realized_vol).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def xdr_drv3_005_rsi14_peer_gap_5d_diff_5d_diff(rsi14: pd.Series,
                                                  peer_median_rsi14: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI14 peer gap (acceleration of momentum divergence)."""
    vel = _gap(rsi14, peer_median_rsi14).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_006_rsi14_peer_gap_21d_diff_5d_diff(rsi14: pd.Series,
                                                   peer_median_rsi14: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of RSI14 peer gap."""
    vel21 = _gap(rsi14, peer_median_rsi14).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def xdr_drv3_007_drawdown_gap_zscore_5d_diff_5d_diff(drawdown: pd.Series,
                                                       peer_median_drawdown: pd.Series) -> pd.Series:
    """Second 5-day diff of drawdown gap z-score (acceleration of z-score velocity)."""
    z = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_008_vol_ratio_zscore_5d_diff_5d_diff(realized_vol: pd.Series,
                                                    peer_median_realized_vol: pd.Series) -> pd.Series:
    """Second 5-day diff of vol ratio z-score."""
    z = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_009_rsi14_peer_gap_zscore_5d_diff_5d_diff(rsi14: pd.Series,
                                                         peer_median_rsi14: pd.Series) -> pd.Series:
    """Second 5-day diff of RSI14 peer gap z-score."""
    z = _zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    vel = z.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_010_de_ratio_5d_diff_5d_diff(debt_to_equity: pd.Series,
                                            peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """Second 5-day diff of D/E ratio vs peers (acceleration of leverage velocity)."""
    vel = _rel_ratio(debt_to_equity, peer_median_debt_to_equity).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_011_fcf_gap_5d_diff_5d_diff(fcf_yield: pd.Series,
                                           peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Second 5-day diff of FCF yield gap (acceleration of cash-flow divergence)."""
    vel = _gap(fcf_yield, peer_median_fcf_yield).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_012_pb_ratio_5d_diff_5d_diff(pb: pd.Series,
                                            peer_median_pb: pd.Series) -> pd.Series:
    """Second 5-day diff of P/B ratio vs peers (acceleration of valuation compression)."""
    vel = _rel_ratio(pb, peer_median_pb).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_013_composite_z3_5d_diff_5d_diff(drawdown: pd.Series,
                                                peer_median_drawdown: pd.Series,
                                                realized_vol: pd.Series,
                                                peer_median_realized_vol: pd.Series,
                                                rsi14: pd.Series,
                                                peer_median_rsi14: pd.Series) -> pd.Series:
    """Second 5-day diff of 3-dim composite distress z-score (acceleration of total distress)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_014_composite_z3_21d_diff_5d_diff(drawdown: pd.Series,
                                                 peer_median_drawdown: pd.Series,
                                                 realized_vol: pd.Series,
                                                 peer_median_realized_vol: pd.Series,
                                                 rsi14: pd.Series,
                                                 peer_median_rsi14: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of 3-dim composite z-score."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi) / 3.0
    vel21 = composite.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def xdr_drv3_015_drawdown_ratio_slope_5d_slope_21d(drawdown: pd.Series,
                                                     peer_median_drawdown: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day slope of drawdown ratio."""
    slope5 = _linslope(_rel_ratio(drawdown, peer_median_drawdown), _TD_WEEK)
    return _linslope(slope5, _TD_MON)


def xdr_drv3_016_vol_ratio_slope_5d_slope_21d(realized_vol: pd.Series,
                                                peer_median_realized_vol: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day slope of vol ratio."""
    slope5 = _linslope(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_WEEK)
    return _linslope(slope5, _TD_MON)


def xdr_drv3_017_rsi14_peer_gap_slope_5d_slope_21d(rsi14: pd.Series,
                                                     peer_median_rsi14: pd.Series) -> pd.Series:
    """OLS slope over 21 days of the 5-day slope of RSI14 peer gap."""
    slope5 = _linslope(_gap(rsi14, peer_median_rsi14), _TD_WEEK)
    return _linslope(slope5, _TD_MON)


def xdr_drv3_018_marketcap_ratio_5d_diff_5d_diff(marketcap: pd.Series,
                                                   peer_median_marketcap: pd.Series) -> pd.Series:
    """Second 5-day diff of market-cap ratio (acceleration of cap compression)."""
    vel = _rel_ratio(marketcap, peer_median_marketcap).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_019_drawdown_ratio_21d_diff_21d_diff(drawdown: pd.Series,
                                                    peer_median_drawdown: pd.Series) -> pd.Series:
    """Second 21-day diff of drawdown ratio (monthly acceleration)."""
    vel21 = _rel_ratio(drawdown, peer_median_drawdown).diff(_TD_MON)
    return vel21.diff(_TD_MON)


def xdr_drv3_020_vol_ratio_21d_diff_21d_diff(realized_vol: pd.Series,
                                              peer_median_realized_vol: pd.Series) -> pd.Series:
    """Second 21-day diff of vol ratio (monthly acceleration of vol stress)."""
    vel21 = _rel_ratio(realized_vol, peer_median_realized_vol).diff(_TD_MON)
    return vel21.diff(_TD_MON)


def xdr_drv3_021_de_ratio_21d_diff_5d_diff(debt_to_equity: pd.Series,
                                             peer_median_debt_to_equity: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of D/E ratio vs peers."""
    vel21 = _rel_ratio(debt_to_equity, peer_median_debt_to_equity).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def xdr_drv3_022_fcf_gap_21d_diff_5d_diff(fcf_yield: pd.Series,
                                            peer_median_fcf_yield: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of FCF yield gap."""
    vel21 = _gap(fcf_yield, peer_median_fcf_yield).diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


def xdr_drv3_023_ps_ratio_5d_diff_5d_diff(ps: pd.Series,
                                            peer_median_ps: pd.Series) -> pd.Series:
    """Second 5-day diff of P/S ratio vs peers."""
    vel = _rel_ratio(ps, peer_median_ps).diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_024_composite_z5_5d_diff_5d_diff(drawdown: pd.Series,
                                                peer_median_drawdown: pd.Series,
                                                realized_vol: pd.Series,
                                                peer_median_realized_vol: pd.Series,
                                                rsi14: pd.Series,
                                                peer_median_rsi14: pd.Series,
                                                debt_to_equity: pd.Series,
                                                peer_median_debt_to_equity: pd.Series,
                                                fcf_yield: pd.Series,
                                                peer_median_fcf_yield: pd.Series) -> pd.Series:
    """Second 5-day diff of 5-dim composite z-score (acceleration of total distress)."""
    z_dd  = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    z_vol = _zscore_rolling(_rel_ratio(realized_vol, peer_median_realized_vol), _TD_YEAR)
    z_rsi = -_zscore_rolling(_gap(rsi14, peer_median_rsi14), _TD_YEAR)
    z_de  = _zscore_rolling(_rel_ratio(debt_to_equity, peer_median_debt_to_equity), _TD_YEAR)
    z_fcf = -_zscore_rolling(_gap(fcf_yield, peer_median_fcf_yield), _TD_YEAR)
    composite = (z_dd + z_vol + z_rsi + z_de + z_fcf) / 5.0
    vel = composite.diff(_TD_WEEK)
    return vel.diff(_TD_WEEK)


def xdr_drv3_025_drawdown_gap_zscore_21d_diff_5d_diff(drawdown: pd.Series,
                                                        peer_median_drawdown: pd.Series) -> pd.Series:
    """5-day diff of the 21-day velocity of drawdown gap z-score."""
    z = _zscore_rolling(_gap(drawdown, peer_median_drawdown), _TD_YEAR)
    vel21 = z.diff(_TD_MON)
    return vel21.diff(_TD_WEEK)


# ── Registry ──────────────────────────────────────────────────────────────────

CROSS_SECTIONAL_DISTRESS_RANK_REGISTRY_3RD_DERIVATIVES = {
    "xdr_drv3_001_drawdown_ratio_5d_diff_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv3_001_drawdown_ratio_5d_diff_5d_diff},
    "xdr_drv3_002_drawdown_ratio_21d_diff_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv3_002_drawdown_ratio_21d_diff_5d_diff},
    "xdr_drv3_003_vol_ratio_5d_diff_5d_diff": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv3_003_vol_ratio_5d_diff_5d_diff},
    "xdr_drv3_004_vol_ratio_21d_diff_5d_diff": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv3_004_vol_ratio_21d_diff_5d_diff},
    "xdr_drv3_005_rsi14_peer_gap_5d_diff_5d_diff": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_drv3_005_rsi14_peer_gap_5d_diff_5d_diff},
    "xdr_drv3_006_rsi14_peer_gap_21d_diff_5d_diff": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_drv3_006_rsi14_peer_gap_21d_diff_5d_diff},
    "xdr_drv3_007_drawdown_gap_zscore_5d_diff_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv3_007_drawdown_gap_zscore_5d_diff_5d_diff},
    "xdr_drv3_008_vol_ratio_zscore_5d_diff_5d_diff": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv3_008_vol_ratio_zscore_5d_diff_5d_diff},
    "xdr_drv3_009_rsi14_peer_gap_zscore_5d_diff_5d_diff": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_drv3_009_rsi14_peer_gap_zscore_5d_diff_5d_diff},
    "xdr_drv3_010_de_ratio_5d_diff_5d_diff": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_drv3_010_de_ratio_5d_diff_5d_diff},
    "xdr_drv3_011_fcf_gap_5d_diff_5d_diff": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_drv3_011_fcf_gap_5d_diff_5d_diff},
    "xdr_drv3_012_pb_ratio_5d_diff_5d_diff": {
        "inputs": ["pb", "peer_median_pb"],
        "func": xdr_drv3_012_pb_ratio_5d_diff_5d_diff},
    "xdr_drv3_013_composite_z3_5d_diff_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_drv3_013_composite_z3_5d_diff_5d_diff},
    "xdr_drv3_014_composite_z3_21d_diff_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14"],
        "func": xdr_drv3_014_composite_z3_21d_diff_5d_diff},
    "xdr_drv3_015_drawdown_ratio_slope_5d_slope_21d": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv3_015_drawdown_ratio_slope_5d_slope_21d},
    "xdr_drv3_016_vol_ratio_slope_5d_slope_21d": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv3_016_vol_ratio_slope_5d_slope_21d},
    "xdr_drv3_017_rsi14_peer_gap_slope_5d_slope_21d": {
        "inputs": ["rsi14", "peer_median_rsi14"],
        "func": xdr_drv3_017_rsi14_peer_gap_slope_5d_slope_21d},
    "xdr_drv3_018_marketcap_ratio_5d_diff_5d_diff": {
        "inputs": ["marketcap", "peer_median_marketcap"],
        "func": xdr_drv3_018_marketcap_ratio_5d_diff_5d_diff},
    "xdr_drv3_019_drawdown_ratio_21d_diff_21d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv3_019_drawdown_ratio_21d_diff_21d_diff},
    "xdr_drv3_020_vol_ratio_21d_diff_21d_diff": {
        "inputs": ["realized_vol", "peer_median_realized_vol"],
        "func": xdr_drv3_020_vol_ratio_21d_diff_21d_diff},
    "xdr_drv3_021_de_ratio_21d_diff_5d_diff": {
        "inputs": ["debt_to_equity", "peer_median_debt_to_equity"],
        "func": xdr_drv3_021_de_ratio_21d_diff_5d_diff},
    "xdr_drv3_022_fcf_gap_21d_diff_5d_diff": {
        "inputs": ["fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_drv3_022_fcf_gap_21d_diff_5d_diff},
    "xdr_drv3_023_ps_ratio_5d_diff_5d_diff": {
        "inputs": ["ps", "peer_median_ps"],
        "func": xdr_drv3_023_ps_ratio_5d_diff_5d_diff},
    "xdr_drv3_024_composite_z5_5d_diff_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown",
                   "realized_vol", "peer_median_realized_vol",
                   "rsi14", "peer_median_rsi14",
                   "debt_to_equity", "peer_median_debt_to_equity",
                   "fcf_yield", "peer_median_fcf_yield"],
        "func": xdr_drv3_024_composite_z5_5d_diff_5d_diff},
    "xdr_drv3_025_drawdown_gap_zscore_21d_diff_5d_diff": {
        "inputs": ["drawdown", "peer_median_drawdown"],
        "func": xdr_drv3_025_drawdown_gap_zscore_21d_diff_5d_diff},
}
