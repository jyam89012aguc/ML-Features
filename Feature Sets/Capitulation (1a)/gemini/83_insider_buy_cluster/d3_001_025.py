"""
83_83_insider_buy_cluster — 3rd Derivatives 001-025
Domain: 83_insider_buy_cluster
Asset class: Equities
Target context: Capitulation
"""
import numpy as np
import pandas as pd

# ── Utility helpers ──────────────────────────────────────────────────────────
_EPS = 1e-9

def _safe_div(a: pd.Series, b: pd.Series) -> pd.Series:
    return a / b.replace(0, _EPS)

def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).mean()

def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).std().fillna(0)

def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div((s - m), sd)

def _rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).rank(pct=True)

def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).skew().fillna(0)

def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=1).kurt().fillna(0)

# ── Feature functions ────────────────────────────────────────────────────────

def ibcl_d3_001_accel_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 5d to detect blow-off or exhaustion.
    """
    base = insider_buy_value
    return base.diff(5).diff(5)

def ibcl_d3_002_accel_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 21d to detect blow-off or exhaustion.
    """
    base = insider_buy_value
    return base.diff(21).diff(21)

def ibcl_d3_003_accel_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 63d to detect blow-off or exhaustion.
    """
    base = insider_buy_value
    return base.diff(63).diff(63)

def ibcl_d3_004_accel_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 126d to detect blow-off or exhaustion.
    """
    base = insider_buy_value
    return base.diff(126).diff(126)

def ibcl_d3_005_accel_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 252d to detect blow-off or exhaustion.
    """
    base = insider_buy_value
    return base.diff(252).diff(252)

def ibcl_d3_006_accel_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 5d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return base.diff(5).diff(5)

def ibcl_d3_007_accel_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 21d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return base.diff(21).diff(21)

def ibcl_d3_008_accel_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 63d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return base.diff(63).diff(63)

def ibcl_d3_009_accel_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 126d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return base.diff(126).diff(126)

def ibcl_d3_010_accel_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 252d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_value, insider_buy_value + insider_sell_value)
    return base.diff(252).diff(252)

def ibcl_d3_011_accel_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 5d to detect blow-off or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return base.diff(5).diff(5)

def ibcl_d3_012_accel_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 21d to detect blow-off or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return base.diff(21).diff(21)

def ibcl_d3_013_accel_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 63d to detect blow-off or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return base.diff(63).diff(63)

def ibcl_d3_014_accel_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 126d to detect blow-off or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return base.diff(126).diff(126)

def ibcl_d3_015_accel_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 252d to detect blow-off or exhaustion.
    """
    base = ceo_buy_value + cfo_buy_value
    return base.diff(252).diff(252)

def ibcl_d3_016_accel_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 5d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return base.diff(5).diff(5)

def ibcl_d3_017_accel_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 21d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return base.diff(21).diff(21)

def ibcl_d3_018_accel_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 63d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return base.diff(63).diff(63)

def ibcl_d3_019_accel_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 126d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return base.diff(126).diff(126)

def ibcl_d3_020_accel_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 252d to detect blow-off or exhaustion.
    """
    base = _safe_div(insider_buy_shares, insider_shares_held)
    return base.diff(252).diff(252)

def ibcl_d3_021_accel_5d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 5d to detect blow-off or exhaustion.
    """
    base = insider_buy_shares
    return base.diff(5).diff(5)

def ibcl_d3_022_accel_21d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 21d to detect blow-off or exhaustion.
    """
    base = insider_buy_shares
    return base.diff(21).diff(21)

def ibcl_d3_023_accel_63d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 63d to detect blow-off or exhaustion.
    """
    base = insider_buy_shares
    return base.diff(63).diff(63)

def ibcl_d3_024_accel_126d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 126d to detect blow-off or exhaustion.
    """
    base = insider_buy_shares
    return base.diff(126).diff(126)

def ibcl_d3_025_accel_252d(insider_buy_shares: pd.Series, insider_sell_shares: pd.Series, insider_buy_value: pd.Series, insider_sell_value: pd.Series, insider_shares_held: pd.Series, officer_buy_value: pd.Series, director_buy_value: pd.Series, ceo_buy_value: pd.Series, cfo_buy_value: pd.Series) -> pd.Series:
    """
    Economic Rationale: Acceleration of 83_insider_buy_cluster over 252d to detect blow-off or exhaustion.
    """
    base = insider_buy_shares
    return base.diff(252).diff(252)
