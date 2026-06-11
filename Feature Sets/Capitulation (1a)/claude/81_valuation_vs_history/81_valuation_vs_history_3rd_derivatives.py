"""
81_valuation_vs_history — 3rd Derivatives (Features drv3_001-075)
Domain: rate of change of 2nd-derivative valuation-vs-history concepts —
        captures the curvature / acceleration-of-acceleration of cheapening
        in own-history statistical positioning (diff/slope/pct-change of
        2nd-derivative-level features).
Inputs: daily-frequency Sharadar DAILY/METRICS valuation fields only —
        pe, pb, ps, ev, marketcap, evebit, evebitda, divyield
All feature functions are strictly backward-looking (rolling/expanding windows
over trailing data only). No negative shifts, no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y = 504
_TD_3Y = 756
_TD_5Y = 1260
_TD_HALF = 126
_TD_QTR = 63
_TD_MON = 21
_EPS = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominator with NaN."""
    return num / den.replace(0, np.nan)


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).rank(pct=True)


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _range_pos(s: pd.Series, w: int) -> pd.Series:
    lo = _rolling_min(s, w)
    hi = _rolling_max(s, w)
    return _safe_div(s - lo, hi - lo)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        denom = ((xi - xi_m) ** 2).sum()
        if denom == 0:
            return np.nan
        return ((xi - xi_m) * (x - x_m)).sum() / denom
    return s.rolling(w, min_periods=max(2, w // 2)).apply(slope, raw=False)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


# ── 3rd-Derivative Feature Functions ─────────────────────────────────────────

def vvh_drv3_001_pe_pctrank_252d_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """Second difference (diff of diff) of P/E 252d pctrank — curvature of rank collapse."""
    rank = _rolling_rank_pct(pe, _TD_YEAR)
    d1 = rank.diff(5)
    return d1.diff(5)


def vvh_drv3_002_pb_pctrank_252d_5d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """Second difference of P/B 252d pctrank — curvature of rank collapse."""
    rank = _rolling_rank_pct(pb, _TD_YEAR)
    d1 = rank.diff(5)
    return d1.diff(5)


def vvh_drv3_003_evebitda_pctrank_252d_5d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """Second difference of EV/EBITDA 252d pctrank."""
    rank = _rolling_rank_pct(evebitda, _TD_YEAR)
    d1 = rank.diff(5)
    return d1.diff(5)


def vvh_drv3_004_pe_zscore_252d_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """Second difference of P/E 252d z-score — curvature of statistical cheapening."""
    z = _zscore_rolling(pe, _TD_YEAR)
    d1 = z.diff(5)
    return d1.diff(5)


def vvh_drv3_005_pb_zscore_252d_5d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """Second difference of P/B 252d z-score."""
    z = _zscore_rolling(pb, _TD_YEAR)
    d1 = z.diff(5)
    return d1.diff(5)


def vvh_drv3_006_ps_pctrank_252d_5d_diff_5d_diff(ps: pd.Series) -> pd.Series:
    """Second difference of P/S 252d pctrank."""
    rank = _rolling_rank_pct(ps, _TD_YEAR)
    d1 = rank.diff(5)
    return d1.diff(5)


def vvh_drv3_007_pe_rangepos_252d_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """Second difference of P/E 252d range position — curvature of range collapse."""
    rp = _range_pos(pe, _TD_YEAR)
    d1 = rp.diff(5)
    return d1.diff(5)


def vvh_drv3_008_composite_cheapness_4metric_252d_5d_diff_5d_diff(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Second difference of composite 4-metric cheapness score — curvature of multi-metric cheapening."""
    s1 = 1.0 - _rolling_rank_pct(pe, _TD_YEAR)
    s2 = 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
    s3 = 1.0 - _rolling_rank_pct(ps, _TD_YEAR)
    s4 = 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)
    composite = (s1 + s2 + s3 + s4) / 4.0
    d1 = composite.diff(5)
    return d1.diff(5)


def vvh_drv3_009_pe_pctrank_252d_5d_diff_21d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/E 252d pctrank 5d-diff — trend in velocity of rank collapse."""
    rank = _rolling_rank_pct(pe, _TD_YEAR)
    d1 = rank.diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_010_pb_pctrank_252d_5d_diff_21d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/B 252d pctrank 5d-diff."""
    rank = _rolling_rank_pct(pb, _TD_YEAR)
    d1 = rank.diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_011_pe_zscore_252d_5d_diff_21d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/E 252d z-score 5d-diff."""
    z = _zscore_rolling(pe, _TD_YEAR)
    d1 = z.diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_012_evebitda_zscore_252d_5d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """Second difference of EV/EBITDA 252d z-score."""
    z = _zscore_rolling(evebitda, _TD_YEAR)
    d1 = z.diff(5)
    return d1.diff(5)


def vvh_drv3_013_pe_pctrank_1260d_21d_diff_21d_diff(pe: pd.Series) -> pd.Series:
    """Second 21d-difference of P/E 1260d pctrank — curvature of long-history rank descent."""
    rank = _rolling_rank_pct(pe, _TD_5Y)
    d1 = rank.diff(_TD_MON)
    return d1.diff(_TD_MON)


def vvh_drv3_014_pb_pctrank_1260d_21d_diff_21d_diff(pb: pd.Series) -> pd.Series:
    """Second 21d-difference of P/B 1260d pctrank."""
    rank = _rolling_rank_pct(pb, _TD_5Y)
    d1 = rank.diff(_TD_MON)
    return d1.diff(_TD_MON)


def vvh_drv3_015_pe_expanding_zscore_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """Second difference of P/E expanding z-score — curvature of all-history cheapening."""
    m = pe.expanding(min_periods=5).mean()
    sd = pe.expanding(min_periods=5).std()
    z = _safe_div(pe - m, sd)
    d1 = z.diff(5)
    return d1.diff(5)


def vvh_drv3_016_divyield_pctrank_252d_5d_diff_5d_diff(divyield: pd.Series) -> pd.Series:
    """Second difference of div yield 252d pctrank — curvature of yield surge."""
    rank = _rolling_rank_pct(divyield, _TD_YEAR)
    d1 = rank.diff(5)
    return d1.diff(5)


def vvh_drv3_017_marketcap_zscore_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """Second difference of marketcap 252d z-score."""
    z = _zscore_rolling(marketcap, _TD_YEAR)
    d1 = z.diff(5)
    return d1.diff(5)


def vvh_drv3_018_pe_momentum_63d_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """Second difference of P/E 63d momentum — curvature of multiple compression."""
    mom = _safe_div(pe - pe.shift(_TD_QTR), pe.shift(_TD_QTR).abs())
    d1 = mom.diff(5)
    return d1.diff(5)


def vvh_drv3_019_pe_rangepos_252d_5d_diff_21d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/E range position 5d-diff — trend in speed of range collapse."""
    rp = _range_pos(pe, _TD_YEAR)
    d1 = rp.diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_020_evebitda_rangepos_252d_5d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """Second difference of EV/EBITDA 252d range position."""
    rp = _range_pos(evebitda, _TD_YEAR)
    d1 = rp.diff(5)
    return d1.diff(5)


def vvh_drv3_021_ps_zscore_252d_5d_diff_5d_diff(ps: pd.Series) -> pd.Series:
    """Second difference of P/S 252d z-score."""
    z = _zscore_rolling(ps, _TD_YEAR)
    d1 = z.diff(5)
    return d1.diff(5)


def vvh_drv3_022_evebit_pctrank_252d_5d_diff_5d_diff(evebit: pd.Series) -> pd.Series:
    """Second difference of EV/EBIT 252d pctrank."""
    rank = _rolling_rank_pct(evebit, _TD_YEAR)
    d1 = rank.diff(5)
    return d1.diff(5)


def vvh_drv3_023_pe_zscore_252d_5d_diff_zscore_63d(pe: pd.Series) -> pd.Series:
    """Z-score (over 63d) of P/E 252d z-score 5d-diff — statistical extremity of velocity."""
    z = _zscore_rolling(pe, _TD_YEAR)
    d1 = z.diff(5)
    return _zscore_rolling(d1, _TD_QTR)


def vvh_drv3_024_composite_cheapness_4metric_252d_5d_diff_21d_slope(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """OLS slope over 21d of 4-metric composite cheapness 5d-diff — trend in cheapening velocity."""
    s1 = 1.0 - _rolling_rank_pct(pe, _TD_YEAR)
    s2 = 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
    s3 = 1.0 - _rolling_rank_pct(ps, _TD_YEAR)
    s4 = 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)
    composite = (s1 + s2 + s3 + s4) / 4.0
    d1 = composite.diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_025_pe_pctrank_252d_5d_diff_zscore_63d(pe: pd.Series) -> pd.Series:
    """Z-score (over 63d) of P/E 252d pctrank 5d-diff — how extreme the current velocity is."""
    rank = _rolling_rank_pct(pe, _TD_YEAR)
    d1 = rank.diff(5)
    return _zscore_rolling(d1, _TD_QTR)


# ── 3rd-Derivative Feature Functions 026-075 ─────────────────────────────────

def vvh_drv3_026_ps_pctrank_252d_5d_diff_21d_slope(ps: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/S 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(ps, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_027_evebitda_pctrank_252d_5d_diff_21d_slope(evebitda: pd.Series) -> pd.Series:
    """OLS slope over 21d of EV/EBITDA 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(evebitda, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_028_divyield_pctrank_252d_5d_diff_21d_slope(divyield: pd.Series) -> pd.Series:
    """OLS slope over 21d of div yield 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(divyield, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_029_marketcap_zscore_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """Second difference of marketcap 252d z-score."""
    d1 = _zscore_rolling(marketcap, _TD_YEAR).diff(5)
    return d1.diff(5)


def vvh_drv3_030_evebit_pctrank_252d_5d_diff_21d_slope(evebit: pd.Series) -> pd.Series:
    """OLS slope over 21d of EV/EBIT 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(evebit, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_031_pb_zscore_252d_5d_diff_21d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/B 252d z-score 5d-diff."""
    d1 = _zscore_rolling(pb, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_032_ps_zscore_252d_5d_diff_21d_slope(ps: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/S 252d z-score 5d-diff."""
    d1 = _zscore_rolling(ps, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_033_pe_pctrank_252d_21d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """5d diff of P/E 252d pctrank 21d-diff (acceleration of monthly rank velocity)."""
    d1 = _rolling_rank_pct(pe, _TD_YEAR).diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_034_pb_pctrank_252d_21d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """5d diff of P/B 252d pctrank 21d-diff."""
    d1 = _rolling_rank_pct(pb, _TD_YEAR).diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_035_evebitda_pctrank_252d_21d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5d diff of EV/EBITDA 252d pctrank 21d-diff."""
    d1 = _rolling_rank_pct(evebitda, _TD_YEAR).diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_036_pe_rangepos_252d_5d_diff_zscore_63d(pe: pd.Series) -> pd.Series:
    """Z-score (63d) of P/E 252d range position 5d-diff."""
    d1 = _range_pos(pe, _TD_YEAR).diff(5)
    return _zscore_rolling(d1, _TD_QTR)


def vvh_drv3_037_pb_rangepos_252d_5d_diff_zscore_63d(pb: pd.Series) -> pd.Series:
    """Z-score (63d) of P/B 252d range position 5d-diff."""
    d1 = _range_pos(pb, _TD_YEAR).diff(5)
    return _zscore_rolling(d1, _TD_QTR)


def vvh_drv3_038_evebitda_zscore_252d_5d_diff_21d_slope(evebitda: pd.Series) -> pd.Series:
    """OLS slope over 21d of EV/EBITDA 252d z-score 5d-diff."""
    d1 = _zscore_rolling(evebitda, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_039_pe_pctrank_1260d_21d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """5d diff of P/E 1260d pctrank 21d-diff (short-term acceleration of long-rank descent)."""
    d1 = _rolling_rank_pct(pe, _TD_5Y).diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_040_pb_pctrank_1260d_21d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """5d diff of P/B 1260d pctrank 21d-diff."""
    d1 = _rolling_rank_pct(pb, _TD_5Y).diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_041_ps_pctrank_252d_5d_diff_zscore_63d(ps: pd.Series) -> pd.Series:
    """Z-score (63d) of P/S 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(ps, _TD_YEAR).diff(5)
    return _zscore_rolling(d1, _TD_QTR)


def vvh_drv3_042_divyield_pctrank_252d_5d_diff_zscore_63d(divyield: pd.Series) -> pd.Series:
    """Z-score (63d) of div yield 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(divyield, _TD_YEAR).diff(5)
    return _zscore_rolling(d1, _TD_QTR)


def vvh_drv3_043_marketcap_pctrank_252d_5d_diff_5d_diff(marketcap: pd.Series) -> pd.Series:
    """Second difference of marketcap 252d pctrank."""
    d1 = _rolling_rank_pct(marketcap, _TD_YEAR).diff(5)
    return d1.diff(5)


def vvh_drv3_044_pb_expanding_zscore_5d_diff_21d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/B expanding z-score 5d-diff."""
    m = pb.expanding(min_periods=5).mean()
    sd = pb.expanding(min_periods=5).std()
    d1 = _safe_div(pb - m, sd).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_045_pe_zscore_1260d_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """Second difference of P/E 1260d z-score."""
    d1 = _zscore_rolling(pe, _TD_5Y).diff(5)
    return d1.diff(5)


def vvh_drv3_046_evebitda_rangepos_1260d_5d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """Second difference of EV/EBITDA 1260d range position."""
    d1 = _range_pos(evebitda, _TD_5Y).diff(5)
    return d1.diff(5)


def vvh_drv3_047_pe_pctrank_252d_5d_diff_63d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope over 63d of P/E 252d pctrank 5d-diff (quarterly trend of velocity)."""
    d1 = _rolling_rank_pct(pe, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_QTR)


def vvh_drv3_048_pb_pctrank_252d_5d_diff_63d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope over 63d of P/B 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(pb, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_QTR)


def vvh_drv3_049_evebitda_pctrank_252d_5d_diff_63d_slope(evebitda: pd.Series) -> pd.Series:
    """OLS slope over 63d of EV/EBITDA 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(evebitda, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_QTR)


def vvh_drv3_050_composite_cheapness_4metric_252d_5d_diff_zscore_63d(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Z-score (63d) of 4-metric composite cheapness 5d-diff — extremity of cheapening velocity."""
    s = (1.0 - _rolling_rank_pct(pe, _TD_YEAR) + 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
         + 1.0 - _rolling_rank_pct(ps, _TD_YEAR) + 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)) / 4.0
    d1 = s.diff(5)
    return _zscore_rolling(d1, _TD_QTR)


def vvh_drv3_051_pe_zscore_252d_21d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """5d diff of P/E 252d z-score 21d-diff (acceleration of monthly z-score velocity)."""
    d1 = _zscore_rolling(pe, _TD_YEAR).diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_052_pb_zscore_252d_5d_diff_zscore_63d(pb: pd.Series) -> pd.Series:
    """Z-score (63d) of P/B 252d z-score 5d-diff."""
    d1 = _zscore_rolling(pb, _TD_YEAR).diff(5)
    return _zscore_rolling(d1, _TD_QTR)


def vvh_drv3_053_evebitda_pctrank_252d_5d_diff_zscore_63d(evebitda: pd.Series) -> pd.Series:
    """Z-score (63d) of EV/EBITDA 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(evebitda, _TD_YEAR).diff(5)
    return _zscore_rolling(d1, _TD_QTR)


def vvh_drv3_054_ps_rangepos_252d_5d_diff_5d_diff(ps: pd.Series) -> pd.Series:
    """Second difference of P/S 252d range position."""
    d1 = _range_pos(ps, _TD_YEAR).diff(5)
    return d1.diff(5)


def vvh_drv3_055_pe_rangepos_252d_21d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """5d diff of P/E 252d range position 21d-diff."""
    d1 = _range_pos(pe, _TD_YEAR).diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_056_pe_pctrank_252d_21d_diff_21d_diff(pe: pd.Series) -> pd.Series:
    """Second 21d-diff of P/E 252d pctrank — curvature of monthly rank descent."""
    d1 = _rolling_rank_pct(pe, _TD_YEAR).diff(_TD_MON)
    return d1.diff(_TD_MON)


def vvh_drv3_057_pb_pctrank_252d_21d_diff_21d_diff(pb: pd.Series) -> pd.Series:
    """Second 21d-diff of P/B 252d pctrank."""
    d1 = _rolling_rank_pct(pb, _TD_YEAR).diff(_TD_MON)
    return d1.diff(_TD_MON)


def vvh_drv3_058_evebitda_zscore_252d_21d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5d diff of EV/EBITDA 252d z-score 21d-diff."""
    d1 = _zscore_rolling(evebitda, _TD_YEAR).diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_059_divyield_pctrank_252d_5d_diff_5d_diff_zscore_63d(divyield: pd.Series) -> pd.Series:
    """Z-score (63d) of div yield 252d pctrank second difference."""
    d1 = _rolling_rank_pct(divyield, _TD_YEAR).diff(5)
    d2 = d1.diff(5)
    return _zscore_rolling(d2, _TD_QTR)


def vvh_drv3_060_pe_momentum_63d_5d_diff_21d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/E 63d momentum 5d-diff (trend in compression acceleration)."""
    mom = _safe_div(pe - pe.shift(_TD_QTR), pe.shift(_TD_QTR).abs())
    d1 = mom.diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_061_pb_momentum_63d_5d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """Second difference of P/B 63d momentum."""
    mom = _safe_div(pb - pb.shift(_TD_QTR), pb.shift(_TD_QTR).abs())
    d1 = mom.diff(5)
    return d1.diff(5)


def vvh_drv3_062_evebitda_momentum_63d_5d_diff_5d_diff(evebitda: pd.Series) -> pd.Series:
    """Second difference of EV/EBITDA 63d momentum."""
    mom = _safe_div(evebitda - evebitda.shift(_TD_QTR), evebitda.shift(_TD_QTR).abs())
    d1 = mom.diff(5)
    return d1.diff(5)


def vvh_drv3_063_pe_zscore_252d_5d_diff_63d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope over 63d of P/E 252d z-score 5d-diff (quarterly trend of cheapening velocity)."""
    d1 = _zscore_rolling(pe, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_QTR)


def vvh_drv3_064_pb_zscore_252d_5d_diff_63d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope over 63d of P/B 252d z-score 5d-diff."""
    d1 = _zscore_rolling(pb, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_QTR)


def vvh_drv3_065_composite_cheapness_4metric_252d_21d_diff_5d_diff(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5d diff of 4-metric composite cheapness 21d-diff."""
    s = (1.0 - _rolling_rank_pct(pe, _TD_YEAR) + 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
         + 1.0 - _rolling_rank_pct(ps, _TD_YEAR) + 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)) / 4.0
    d1 = s.diff(_TD_MON)
    return d1.diff(5)


def vvh_drv3_066_pe_pctrank_252d_5d_diff_pct_change_21d(pe: pd.Series) -> pd.Series:
    """21d pct change of P/E 252d pctrank 5d-diff (relative acceleration of velocity)."""
    d1 = _rolling_rank_pct(pe, _TD_YEAR).diff(5).clip(lower=_EPS)
    return _safe_div(d1 - d1.shift(_TD_MON), d1.shift(_TD_MON).abs())


def vvh_drv3_067_ps_pctrank_252d_5d_diff_5d_diff(ps: pd.Series) -> pd.Series:
    """Second difference of P/S 252d pctrank (already exists for pe/pb/evebitda — covers ps)."""
    d1 = _rolling_rank_pct(ps, _TD_YEAR).diff(5)
    return d1.diff(5)


def vvh_drv3_068_evebit_zscore_252d_5d_diff_5d_diff(evebit: pd.Series) -> pd.Series:
    """Second difference of EV/EBIT 252d z-score."""
    d1 = _zscore_rolling(evebit, _TD_YEAR).diff(5)
    return d1.diff(5)


def vvh_drv3_069_pe_expanding_zscore_5d_diff_21d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope over 21d of P/E expanding z-score 5d-diff."""
    m = pe.expanding(min_periods=5).mean()
    sd = pe.expanding(min_periods=5).std()
    d1 = _safe_div(pe - m, sd).diff(5)
    return _linslope(d1, _TD_MON)


def vvh_drv3_070_evebitda_pctrank_1260d_21d_diff_21d_diff(evebitda: pd.Series) -> pd.Series:
    """Second 21d-diff of EV/EBITDA 1260d pctrank — curvature of long-rank descent."""
    d1 = _rolling_rank_pct(evebitda, _TD_5Y).diff(_TD_MON)
    return d1.diff(_TD_MON)


def vvh_drv3_071_pe_rangepos_1260d_5d_diff_5d_diff(pe: pd.Series) -> pd.Series:
    """Second difference of P/E 1260d range position."""
    d1 = _range_pos(pe, _TD_5Y).diff(5)
    return d1.diff(5)


def vvh_drv3_072_pb_rangepos_1260d_5d_diff_5d_diff(pb: pd.Series) -> pd.Series:
    """Second difference of P/B 1260d range position."""
    d1 = _range_pos(pb, _TD_5Y).diff(5)
    return d1.diff(5)


def vvh_drv3_073_composite_cheapness_4metric_252d_5d_diff_5d_diff_zscore_21d(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Z-score (21d) of 4-metric composite cheapness second difference."""
    s = (1.0 - _rolling_rank_pct(pe, _TD_YEAR) + 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
         + 1.0 - _rolling_rank_pct(ps, _TD_YEAR) + 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)) / 4.0
    d2 = s.diff(5).diff(5)
    return _zscore_rolling(d2, _TD_MON)


def vvh_drv3_074_divyield_zscore_252d_5d_diff_5d_diff(divyield: pd.Series) -> pd.Series:
    """Second difference of div yield 252d z-score — curvature of yield-surge velocity."""
    d1 = _zscore_rolling(divyield, _TD_YEAR).diff(5)
    return d1.diff(5)


def vvh_drv3_075_marketcap_pctrank_252d_5d_diff_21d_slope(marketcap: pd.Series) -> pd.Series:
    """OLS slope over 21d of marketcap 252d pctrank 5d-diff."""
    d1 = _rolling_rank_pct(marketcap, _TD_YEAR).diff(5)
    return _linslope(d1, _TD_MON)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_HISTORY_REGISTRY_3RD_DERIVATIVES = {
    "vvh_drv3_001_pe_pctrank_252d_5d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_001_pe_pctrank_252d_5d_diff_5d_diff},
    "vvh_drv3_002_pb_pctrank_252d_5d_diff_5d_diff": {"inputs": ["pb"], "func": vvh_drv3_002_pb_pctrank_252d_5d_diff_5d_diff},
    "vvh_drv3_003_evebitda_pctrank_252d_5d_diff_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv3_003_evebitda_pctrank_252d_5d_diff_5d_diff},
    "vvh_drv3_004_pe_zscore_252d_5d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_004_pe_zscore_252d_5d_diff_5d_diff},
    "vvh_drv3_005_pb_zscore_252d_5d_diff_5d_diff": {"inputs": ["pb"], "func": vvh_drv3_005_pb_zscore_252d_5d_diff_5d_diff},
    "vvh_drv3_006_ps_pctrank_252d_5d_diff_5d_diff": {"inputs": ["ps"], "func": vvh_drv3_006_ps_pctrank_252d_5d_diff_5d_diff},
    "vvh_drv3_007_pe_rangepos_252d_5d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_007_pe_rangepos_252d_5d_diff_5d_diff},
    "vvh_drv3_008_composite_cheapness_4metric_252d_5d_diff_5d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_drv3_008_composite_cheapness_4metric_252d_5d_diff_5d_diff},
    "vvh_drv3_009_pe_pctrank_252d_5d_diff_21d_slope": {"inputs": ["pe"], "func": vvh_drv3_009_pe_pctrank_252d_5d_diff_21d_slope},
    "vvh_drv3_010_pb_pctrank_252d_5d_diff_21d_slope": {"inputs": ["pb"], "func": vvh_drv3_010_pb_pctrank_252d_5d_diff_21d_slope},
    "vvh_drv3_011_pe_zscore_252d_5d_diff_21d_slope": {"inputs": ["pe"], "func": vvh_drv3_011_pe_zscore_252d_5d_diff_21d_slope},
    "vvh_drv3_012_evebitda_zscore_252d_5d_diff_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv3_012_evebitda_zscore_252d_5d_diff_5d_diff},
    "vvh_drv3_013_pe_pctrank_1260d_21d_diff_21d_diff": {"inputs": ["pe"], "func": vvh_drv3_013_pe_pctrank_1260d_21d_diff_21d_diff},
    "vvh_drv3_014_pb_pctrank_1260d_21d_diff_21d_diff": {"inputs": ["pb"], "func": vvh_drv3_014_pb_pctrank_1260d_21d_diff_21d_diff},
    "vvh_drv3_015_pe_expanding_zscore_5d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_015_pe_expanding_zscore_5d_diff_5d_diff},
    "vvh_drv3_016_divyield_pctrank_252d_5d_diff_5d_diff": {"inputs": ["divyield"], "func": vvh_drv3_016_divyield_pctrank_252d_5d_diff_5d_diff},
    "vvh_drv3_017_marketcap_zscore_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": vvh_drv3_017_marketcap_zscore_252d_5d_diff_5d_diff},
    "vvh_drv3_018_pe_momentum_63d_5d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_018_pe_momentum_63d_5d_diff_5d_diff},
    "vvh_drv3_019_pe_rangepos_252d_5d_diff_21d_slope": {"inputs": ["pe"], "func": vvh_drv3_019_pe_rangepos_252d_5d_diff_21d_slope},
    "vvh_drv3_020_evebitda_rangepos_252d_5d_diff_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv3_020_evebitda_rangepos_252d_5d_diff_5d_diff},
    "vvh_drv3_021_ps_zscore_252d_5d_diff_5d_diff": {"inputs": ["ps"], "func": vvh_drv3_021_ps_zscore_252d_5d_diff_5d_diff},
    "vvh_drv3_022_evebit_pctrank_252d_5d_diff_5d_diff": {"inputs": ["evebit"], "func": vvh_drv3_022_evebit_pctrank_252d_5d_diff_5d_diff},
    "vvh_drv3_023_pe_zscore_252d_5d_diff_zscore_63d": {"inputs": ["pe"], "func": vvh_drv3_023_pe_zscore_252d_5d_diff_zscore_63d},
    "vvh_drv3_024_composite_cheapness_4metric_252d_5d_diff_21d_slope": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_drv3_024_composite_cheapness_4metric_252d_5d_diff_21d_slope},
    "vvh_drv3_025_pe_pctrank_252d_5d_diff_zscore_63d": {"inputs": ["pe"], "func": vvh_drv3_025_pe_pctrank_252d_5d_diff_zscore_63d},
    "vvh_drv3_026_ps_pctrank_252d_5d_diff_21d_slope": {"inputs": ["ps"], "func": vvh_drv3_026_ps_pctrank_252d_5d_diff_21d_slope},
    "vvh_drv3_027_evebitda_pctrank_252d_5d_diff_21d_slope": {"inputs": ["evebitda"], "func": vvh_drv3_027_evebitda_pctrank_252d_5d_diff_21d_slope},
    "vvh_drv3_028_divyield_pctrank_252d_5d_diff_21d_slope": {"inputs": ["divyield"], "func": vvh_drv3_028_divyield_pctrank_252d_5d_diff_21d_slope},
    "vvh_drv3_029_marketcap_zscore_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": vvh_drv3_029_marketcap_zscore_252d_5d_diff_5d_diff},
    "vvh_drv3_030_evebit_pctrank_252d_5d_diff_21d_slope": {"inputs": ["evebit"], "func": vvh_drv3_030_evebit_pctrank_252d_5d_diff_21d_slope},
    "vvh_drv3_031_pb_zscore_252d_5d_diff_21d_slope": {"inputs": ["pb"], "func": vvh_drv3_031_pb_zscore_252d_5d_diff_21d_slope},
    "vvh_drv3_032_ps_zscore_252d_5d_diff_21d_slope": {"inputs": ["ps"], "func": vvh_drv3_032_ps_zscore_252d_5d_diff_21d_slope},
    "vvh_drv3_033_pe_pctrank_252d_21d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_033_pe_pctrank_252d_21d_diff_5d_diff},
    "vvh_drv3_034_pb_pctrank_252d_21d_diff_5d_diff": {"inputs": ["pb"], "func": vvh_drv3_034_pb_pctrank_252d_21d_diff_5d_diff},
    "vvh_drv3_035_evebitda_pctrank_252d_21d_diff_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv3_035_evebitda_pctrank_252d_21d_diff_5d_diff},
    "vvh_drv3_036_pe_rangepos_252d_5d_diff_zscore_63d": {"inputs": ["pe"], "func": vvh_drv3_036_pe_rangepos_252d_5d_diff_zscore_63d},
    "vvh_drv3_037_pb_rangepos_252d_5d_diff_zscore_63d": {"inputs": ["pb"], "func": vvh_drv3_037_pb_rangepos_252d_5d_diff_zscore_63d},
    "vvh_drv3_038_evebitda_zscore_252d_5d_diff_21d_slope": {"inputs": ["evebitda"], "func": vvh_drv3_038_evebitda_zscore_252d_5d_diff_21d_slope},
    "vvh_drv3_039_pe_pctrank_1260d_21d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_039_pe_pctrank_1260d_21d_diff_5d_diff},
    "vvh_drv3_040_pb_pctrank_1260d_21d_diff_5d_diff": {"inputs": ["pb"], "func": vvh_drv3_040_pb_pctrank_1260d_21d_diff_5d_diff},
    "vvh_drv3_041_ps_pctrank_252d_5d_diff_zscore_63d": {"inputs": ["ps"], "func": vvh_drv3_041_ps_pctrank_252d_5d_diff_zscore_63d},
    "vvh_drv3_042_divyield_pctrank_252d_5d_diff_zscore_63d": {"inputs": ["divyield"], "func": vvh_drv3_042_divyield_pctrank_252d_5d_diff_zscore_63d},
    "vvh_drv3_043_marketcap_pctrank_252d_5d_diff_5d_diff": {"inputs": ["marketcap"], "func": vvh_drv3_043_marketcap_pctrank_252d_5d_diff_5d_diff},
    "vvh_drv3_044_pb_expanding_zscore_5d_diff_21d_slope": {"inputs": ["pb"], "func": vvh_drv3_044_pb_expanding_zscore_5d_diff_21d_slope},
    "vvh_drv3_045_pe_zscore_1260d_5d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_045_pe_zscore_1260d_5d_diff_5d_diff},
    "vvh_drv3_046_evebitda_rangepos_1260d_5d_diff_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv3_046_evebitda_rangepos_1260d_5d_diff_5d_diff},
    "vvh_drv3_047_pe_pctrank_252d_5d_diff_63d_slope": {"inputs": ["pe"], "func": vvh_drv3_047_pe_pctrank_252d_5d_diff_63d_slope},
    "vvh_drv3_048_pb_pctrank_252d_5d_diff_63d_slope": {"inputs": ["pb"], "func": vvh_drv3_048_pb_pctrank_252d_5d_diff_63d_slope},
    "vvh_drv3_049_evebitda_pctrank_252d_5d_diff_63d_slope": {"inputs": ["evebitda"], "func": vvh_drv3_049_evebitda_pctrank_252d_5d_diff_63d_slope},
    "vvh_drv3_050_composite_cheapness_4metric_252d_5d_diff_zscore_63d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_drv3_050_composite_cheapness_4metric_252d_5d_diff_zscore_63d},
    "vvh_drv3_051_pe_zscore_252d_21d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_051_pe_zscore_252d_21d_diff_5d_diff},
    "vvh_drv3_052_pb_zscore_252d_5d_diff_zscore_63d": {"inputs": ["pb"], "func": vvh_drv3_052_pb_zscore_252d_5d_diff_zscore_63d},
    "vvh_drv3_053_evebitda_pctrank_252d_5d_diff_zscore_63d": {"inputs": ["evebitda"], "func": vvh_drv3_053_evebitda_pctrank_252d_5d_diff_zscore_63d},
    "vvh_drv3_054_ps_rangepos_252d_5d_diff_5d_diff": {"inputs": ["ps"], "func": vvh_drv3_054_ps_rangepos_252d_5d_diff_5d_diff},
    "vvh_drv3_055_pe_rangepos_252d_21d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_055_pe_rangepos_252d_21d_diff_5d_diff},
    "vvh_drv3_056_pe_pctrank_252d_21d_diff_21d_diff": {"inputs": ["pe"], "func": vvh_drv3_056_pe_pctrank_252d_21d_diff_21d_diff},
    "vvh_drv3_057_pb_pctrank_252d_21d_diff_21d_diff": {"inputs": ["pb"], "func": vvh_drv3_057_pb_pctrank_252d_21d_diff_21d_diff},
    "vvh_drv3_058_evebitda_zscore_252d_21d_diff_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv3_058_evebitda_zscore_252d_21d_diff_5d_diff},
    "vvh_drv3_059_divyield_pctrank_252d_5d_diff_5d_diff_zscore_63d": {"inputs": ["divyield"], "func": vvh_drv3_059_divyield_pctrank_252d_5d_diff_5d_diff_zscore_63d},
    "vvh_drv3_060_pe_momentum_63d_5d_diff_21d_slope": {"inputs": ["pe"], "func": vvh_drv3_060_pe_momentum_63d_5d_diff_21d_slope},
    "vvh_drv3_061_pb_momentum_63d_5d_diff_5d_diff": {"inputs": ["pb"], "func": vvh_drv3_061_pb_momentum_63d_5d_diff_5d_diff},
    "vvh_drv3_062_evebitda_momentum_63d_5d_diff_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv3_062_evebitda_momentum_63d_5d_diff_5d_diff},
    "vvh_drv3_063_pe_zscore_252d_5d_diff_63d_slope": {"inputs": ["pe"], "func": vvh_drv3_063_pe_zscore_252d_5d_diff_63d_slope},
    "vvh_drv3_064_pb_zscore_252d_5d_diff_63d_slope": {"inputs": ["pb"], "func": vvh_drv3_064_pb_zscore_252d_5d_diff_63d_slope},
    "vvh_drv3_065_composite_cheapness_4metric_252d_21d_diff_5d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_drv3_065_composite_cheapness_4metric_252d_21d_diff_5d_diff},
    "vvh_drv3_066_pe_pctrank_252d_5d_diff_pct_change_21d": {"inputs": ["pe"], "func": vvh_drv3_066_pe_pctrank_252d_5d_diff_pct_change_21d},
    "vvh_drv3_067_ps_pctrank_252d_5d_diff_5d_diff": {"inputs": ["ps"], "func": vvh_drv3_067_ps_pctrank_252d_5d_diff_5d_diff},
    "vvh_drv3_068_evebit_zscore_252d_5d_diff_5d_diff": {"inputs": ["evebit"], "func": vvh_drv3_068_evebit_zscore_252d_5d_diff_5d_diff},
    "vvh_drv3_069_pe_expanding_zscore_5d_diff_21d_slope": {"inputs": ["pe"], "func": vvh_drv3_069_pe_expanding_zscore_5d_diff_21d_slope},
    "vvh_drv3_070_evebitda_pctrank_1260d_21d_diff_21d_diff": {"inputs": ["evebitda"], "func": vvh_drv3_070_evebitda_pctrank_1260d_21d_diff_21d_diff},
    "vvh_drv3_071_pe_rangepos_1260d_5d_diff_5d_diff": {"inputs": ["pe"], "func": vvh_drv3_071_pe_rangepos_1260d_5d_diff_5d_diff},
    "vvh_drv3_072_pb_rangepos_1260d_5d_diff_5d_diff": {"inputs": ["pb"], "func": vvh_drv3_072_pb_rangepos_1260d_5d_diff_5d_diff},
    "vvh_drv3_073_composite_cheapness_4metric_252d_5d_diff_5d_diff_zscore_21d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_drv3_073_composite_cheapness_4metric_252d_5d_diff_5d_diff_zscore_21d},
    "vvh_drv3_074_divyield_zscore_252d_5d_diff_5d_diff": {"inputs": ["divyield"], "func": vvh_drv3_074_divyield_zscore_252d_5d_diff_5d_diff},
    "vvh_drv3_075_marketcap_pctrank_252d_5d_diff_21d_slope": {"inputs": ["marketcap"], "func": vvh_drv3_075_marketcap_pctrank_252d_5d_diff_21d_slope},
}
