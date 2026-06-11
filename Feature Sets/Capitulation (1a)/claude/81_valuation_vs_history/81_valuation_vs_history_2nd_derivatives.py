"""
81_valuation_vs_history — 2nd Derivatives (Features drv2_001-075)
Domain: rate of change of base valuation-vs-history concepts — captures
        acceleration / velocity of cheapening in own-history statistical
        positioning (diff, slope, pct-change of base-level features).
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


# ── 2nd-Derivative Feature Functions ─────────────────────────────────────────

def vvh_drv2_001_pe_pctrank_252d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day first difference of P/E 252d percentile rank (velocity of cheapening)."""
    rank = _rolling_rank_pct(pe, _TD_YEAR)
    return rank.diff(5)


def vvh_drv2_002_pb_pctrank_252d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day first difference of P/B 252d percentile rank."""
    rank = _rolling_rank_pct(pb, _TD_YEAR)
    return rank.diff(5)


def vvh_drv2_003_ps_pctrank_252d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day first difference of P/S 252d percentile rank."""
    rank = _rolling_rank_pct(ps, _TD_YEAR)
    return rank.diff(5)


def vvh_drv2_004_evebitda_pctrank_252d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day first difference of EV/EBITDA 252d percentile rank."""
    rank = _rolling_rank_pct(evebitda, _TD_YEAR)
    return rank.diff(5)


def vvh_drv2_005_pe_zscore_252d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E 252d z-score (acceleration of statistical cheapening)."""
    z = _zscore_rolling(pe, _TD_YEAR)
    return z.diff(5)


def vvh_drv2_006_pb_zscore_252d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B 252d z-score."""
    z = _zscore_rolling(pb, _TD_YEAR)
    return z.diff(5)


def vvh_drv2_007_evebitda_zscore_252d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA 252d z-score."""
    z = _zscore_rolling(evebitda, _TD_YEAR)
    return z.diff(5)


def vvh_drv2_008_pe_rangepos_252d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E range position (speed of collapse within own range)."""
    rp = _range_pos(pe, _TD_YEAR)
    return rp.diff(5)


def vvh_drv2_009_pb_rangepos_252d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B range position."""
    rp = _range_pos(pb, _TD_YEAR)
    return rp.diff(5)


def vvh_drv2_010_pe_vs_median_252d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E-vs-252d-median ratio (pace of moving below median)."""
    med = _rolling_median(pe, _TD_YEAR)
    ratio = _safe_div(pe, med)
    return ratio.diff(5)


def vvh_drv2_011_pe_pctrank_1260d_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of P/E 1260d percentile rank (monthly velocity in long-history rank)."""
    rank = _rolling_rank_pct(pe, _TD_5Y)
    return rank.diff(_TD_MON)


def vvh_drv2_012_pb_pctrank_1260d_21d_diff(pb: pd.Series) -> pd.Series:
    """21-day diff of P/B 1260d percentile rank."""
    rank = _rolling_rank_pct(pb, _TD_5Y)
    return rank.diff(_TD_MON)


def vvh_drv2_013_composite_cheapness_4metric_252d_5d_diff(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of composite 4-metric cheapness score (252d) — velocity of multi-metric cheapening."""
    s1 = 1.0 - _rolling_rank_pct(pe, _TD_YEAR)
    s2 = 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
    s3 = 1.0 - _rolling_rank_pct(ps, _TD_YEAR)
    s4 = 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)
    composite = (s1 + s2 + s3 + s4) / 4.0
    return composite.diff(5)


def vvh_drv2_014_pe_expanding_zscore_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E expanding z-score (acceleration of all-history cheapening)."""
    m = pe.expanding(min_periods=5).mean()
    sd = pe.expanding(min_periods=5).std()
    z = _safe_div(pe - m, sd)
    return z.diff(5)


def vvh_drv2_015_pb_expanding_zscore_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B expanding z-score."""
    m = pb.expanding(min_periods=5).mean()
    sd = pb.expanding(min_periods=5).std()
    z = _safe_div(pb - m, sd)
    return z.diff(5)


def vvh_drv2_016_evebitda_rangepos_1260d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA 1260d range position."""
    rp = _range_pos(evebitda, _TD_5Y)
    return rp.diff(5)


def vvh_drv2_017_pe_zscore_252d_21d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of P/E 252d z-score over trailing 21 days (short-term trend)."""
    z = _zscore_rolling(pe, _TD_YEAR)
    return _linslope(z, _TD_MON)


def vvh_drv2_018_pb_zscore_252d_63d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope of P/B 252d z-score over trailing 63 days."""
    z = _zscore_rolling(pb, _TD_YEAR)
    return _linslope(z, _TD_QTR)


def vvh_drv2_019_pe_pctrank_252d_21d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of P/E 252d pctrank over trailing 21 days."""
    rank = _rolling_rank_pct(pe, _TD_YEAR)
    return _linslope(rank, _TD_MON)


def vvh_drv2_020_pe_momentum_63d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E 63d momentum (acceleration of multiple compression)."""
    mom = _safe_div(pe - pe.shift(_TD_QTR), pe.shift(_TD_QTR).abs())
    return mom.diff(5)


def vvh_drv2_021_ps_zscore_252d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of P/S 252d z-score."""
    z = _zscore_rolling(ps, _TD_YEAR)
    return z.diff(5)


def vvh_drv2_022_divyield_pctrank_252d_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of dividend yield 252d percentile rank (speed of yield surge)."""
    rank = _rolling_rank_pct(divyield, _TD_YEAR)
    return rank.diff(5)


def vvh_drv2_023_marketcap_zscore_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of marketcap 252d z-score (velocity of cap compression)."""
    z = _zscore_rolling(marketcap, _TD_YEAR)
    return z.diff(5)


def vvh_drv2_024_evebit_pctrank_252d_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of EV/EBIT 252d percentile rank."""
    rank = _rolling_rank_pct(evebit, _TD_YEAR)
    return rank.diff(5)


def vvh_drv2_025_pe_pctrank_252d_pct_change_21d(pe: pd.Series) -> pd.Series:
    """21-day percent change of P/E 252d pctrank (relative pace of rank collapse)."""
    rank = _rolling_rank_pct(pe, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(rank - rank.shift(_TD_MON), rank.shift(_TD_MON))


# ── 2nd-Derivative Feature Functions 026-075 ─────────────────────────────────

def vvh_drv2_026_pe_pctrank_252d_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of P/E 252d percentile rank (monthly velocity of rank change)."""
    return _rolling_rank_pct(pe, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_027_pb_pctrank_252d_21d_diff(pb: pd.Series) -> pd.Series:
    """21-day diff of P/B 252d percentile rank."""
    return _rolling_rank_pct(pb, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_028_ps_pctrank_252d_21d_diff(ps: pd.Series) -> pd.Series:
    """21-day diff of P/S 252d percentile rank."""
    return _rolling_rank_pct(ps, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_029_evebitda_pctrank_252d_21d_diff(evebitda: pd.Series) -> pd.Series:
    """21-day diff of EV/EBITDA 252d percentile rank."""
    return _rolling_rank_pct(evebitda, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_030_evebit_pctrank_252d_21d_diff(evebit: pd.Series) -> pd.Series:
    """21-day diff of EV/EBIT 252d percentile rank."""
    return _rolling_rank_pct(evebit, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_031_divyield_pctrank_252d_21d_diff(divyield: pd.Series) -> pd.Series:
    """21-day diff of dividend yield 252d percentile rank."""
    return _rolling_rank_pct(divyield, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_032_marketcap_pctrank_252d_5d_diff(marketcap: pd.Series) -> pd.Series:
    """5-day diff of marketcap 252d percentile rank."""
    return _rolling_rank_pct(marketcap, _TD_YEAR).diff(5)


def vvh_drv2_033_pe_rangepos_1260d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E 1260d range position (velocity of collapse in long-range)."""
    return _range_pos(pe, _TD_5Y).diff(5)


def vvh_drv2_034_pb_rangepos_1260d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B 1260d range position."""
    return _range_pos(pb, _TD_5Y).diff(5)


def vvh_drv2_035_ps_rangepos_252d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of P/S 252d range position."""
    return _range_pos(ps, _TD_YEAR).diff(5)


def vvh_drv2_036_ev_zscore_252d_5d_diff(ev: pd.Series) -> pd.Series:
    """5-day diff of EV 252d z-score."""
    return _zscore_rolling(ev, _TD_YEAR).diff(5)


def vvh_drv2_037_pe_zscore_1260d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E 1260d z-score."""
    return _zscore_rolling(pe, _TD_5Y).diff(5)


def vvh_drv2_038_pb_zscore_1260d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B 1260d z-score."""
    return _zscore_rolling(pb, _TD_5Y).diff(5)


def vvh_drv2_039_evebitda_zscore_1260d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA 1260d z-score."""
    return _zscore_rolling(evebitda, _TD_5Y).diff(5)


def vvh_drv2_040_ps_zscore_252d_21d_diff(ps: pd.Series) -> pd.Series:
    """21-day diff of P/S 252d z-score."""
    return _zscore_rolling(ps, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_041_pe_pctrank_252d_63d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of P/E 252d pctrank over trailing 63 days (quarterly trend)."""
    return _linslope(_rolling_rank_pct(pe, _TD_YEAR), _TD_QTR)


def vvh_drv2_042_pb_pctrank_252d_63d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope of P/B 252d pctrank over trailing 63 days."""
    return _linslope(_rolling_rank_pct(pb, _TD_YEAR), _TD_QTR)


def vvh_drv2_043_ps_pctrank_252d_63d_slope(ps: pd.Series) -> pd.Series:
    """OLS slope of P/S 252d pctrank over trailing 63 days."""
    return _linslope(_rolling_rank_pct(ps, _TD_YEAR), _TD_QTR)


def vvh_drv2_044_evebitda_pctrank_252d_63d_slope(evebitda: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA 252d pctrank over trailing 63 days."""
    return _linslope(_rolling_rank_pct(evebitda, _TD_YEAR), _TD_QTR)


def vvh_drv2_045_divyield_zscore_252d_5d_diff(divyield: pd.Series) -> pd.Series:
    """5-day diff of div yield 252d z-score."""
    return _zscore_rolling(divyield, _TD_YEAR).diff(5)


def vvh_drv2_046_pe_rangepos_252d_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of P/E 252d range position."""
    return _range_pos(pe, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_047_pb_rangepos_252d_21d_diff(pb: pd.Series) -> pd.Series:
    """21-day diff of P/B 252d range position."""
    return _range_pos(pb, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_048_pe_vs_median_252d_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of P/E-vs-252d-median ratio."""
    med = _rolling_median(pe, _TD_YEAR)
    return _safe_div(pe, med).diff(_TD_MON)


def vvh_drv2_049_evebitda_vs_median_252d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA-vs-252d-median ratio."""
    med = _rolling_median(evebitda, _TD_YEAR)
    return _safe_div(evebitda, med).diff(5)


def vvh_drv2_050_pb_vs_median_252d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B-vs-252d-median ratio."""
    med = _rolling_median(pb, _TD_YEAR)
    return _safe_div(pb, med).diff(5)


def vvh_drv2_051_pe_expanding_zscore_21d_diff(pe: pd.Series) -> pd.Series:
    """21-day diff of P/E expanding z-score."""
    m = pe.expanding(min_periods=5).mean()
    sd = pe.expanding(min_periods=5).std()
    return _safe_div(pe - m, sd).diff(_TD_MON)


def vvh_drv2_052_evebitda_expanding_zscore_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA expanding z-score."""
    m = evebitda.expanding(min_periods=5).mean()
    sd = evebitda.expanding(min_periods=5).std()
    return _safe_div(evebitda - m, sd).diff(5)


def vvh_drv2_053_marketcap_zscore_252d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of marketcap 252d z-score."""
    return _zscore_rolling(marketcap, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_054_composite_cheapness_4metric_252d_21d_diff(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """21-day diff of 4-metric composite cheapness score (252d)."""
    s = (1.0 - _rolling_rank_pct(pe, _TD_YEAR) + 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
         + 1.0 - _rolling_rank_pct(ps, _TD_YEAR) + 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)) / 4.0
    return s.diff(_TD_MON)


def vvh_drv2_055_pe_zscore_252d_pct_change_21d(pe: pd.Series) -> pd.Series:
    """21-day pct change of P/E 252d z-score."""
    z = _zscore_rolling(pe, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(z - z.shift(_TD_MON), z.shift(_TD_MON).abs())


def vvh_drv2_056_pb_pctrank_252d_pct_change_21d(pb: pd.Series) -> pd.Series:
    """21-day pct change of P/B 252d pctrank."""
    r = _rolling_rank_pct(pb, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(r - r.shift(_TD_MON), r.shift(_TD_MON))


def vvh_drv2_057_evebitda_pctrank_252d_pct_change_21d(evebitda: pd.Series) -> pd.Series:
    """21-day pct change of EV/EBITDA 252d pctrank."""
    r = _rolling_rank_pct(evebitda, _TD_YEAR).clip(lower=_EPS)
    return _safe_div(r - r.shift(_TD_MON), r.shift(_TD_MON))


def vvh_drv2_058_pe_pctrank_1260d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E 1260d percentile rank."""
    return _rolling_rank_pct(pe, _TD_5Y).diff(5)


def vvh_drv2_059_pb_pctrank_1260d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B 1260d percentile rank."""
    return _rolling_rank_pct(pb, _TD_5Y).diff(5)


def vvh_drv2_060_ps_pctrank_1260d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of P/S 1260d percentile rank."""
    return _rolling_rank_pct(ps, _TD_5Y).diff(5)


def vvh_drv2_061_pe_zscore_252d_63d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of P/E 252d z-score over trailing 63 days (quarterly trend of z-score)."""
    return _linslope(_zscore_rolling(pe, _TD_YEAR), _TD_QTR)


def vvh_drv2_062_evebitda_zscore_252d_21d_slope(evebitda: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA 252d z-score over trailing 21 days."""
    return _linslope(_zscore_rolling(evebitda, _TD_YEAR), _TD_MON)


def vvh_drv2_063_divyield_pctrank_252d_21d_slope(divyield: pd.Series) -> pd.Series:
    """OLS slope of div yield 252d pctrank over trailing 21 days."""
    return _linslope(_rolling_rank_pct(divyield, _TD_YEAR), _TD_MON)


def vvh_drv2_064_evebit_zscore_252d_5d_diff(evebit: pd.Series) -> pd.Series:
    """5-day diff of EV/EBIT 252d z-score."""
    return _zscore_rolling(evebit, _TD_YEAR).diff(5)


def vvh_drv2_065_marketcap_pctrank_252d_21d_diff(marketcap: pd.Series) -> pd.Series:
    """21-day diff of marketcap 252d percentile rank."""
    return _rolling_rank_pct(marketcap, _TD_YEAR).diff(_TD_MON)


def vvh_drv2_066_pe_rangepos_252d_63d_slope(pe: pd.Series) -> pd.Series:
    """OLS slope of P/E 252d range position over trailing 63 days."""
    return _linslope(_range_pos(pe, _TD_YEAR), _TD_QTR)


def vvh_drv2_067_pb_rangepos_252d_63d_slope(pb: pd.Series) -> pd.Series:
    """OLS slope of P/B 252d range position over trailing 63 days."""
    return _linslope(_range_pos(pb, _TD_YEAR), _TD_QTR)


def vvh_drv2_068_pb_momentum_63d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B 63d momentum (acceleration of P/B compression)."""
    mom = _safe_div(pb - pb.shift(_TD_QTR), pb.shift(_TD_QTR).abs())
    return mom.diff(5)


def vvh_drv2_069_ps_momentum_63d_5d_diff(ps: pd.Series) -> pd.Series:
    """5-day diff of P/S 63d momentum."""
    mom = _safe_div(ps - ps.shift(_TD_QTR), ps.shift(_TD_QTR).abs())
    return mom.diff(5)


def vvh_drv2_070_evebitda_momentum_63d_5d_diff(evebitda: pd.Series) -> pd.Series:
    """5-day diff of EV/EBITDA 63d momentum (acceleration of EV/EBITDA compression)."""
    mom = _safe_div(evebitda - evebitda.shift(_TD_QTR), evebitda.shift(_TD_QTR).abs())
    return mom.diff(5)


def vvh_drv2_071_pe_pctrank_half_126d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E 126d percentile rank."""
    return _rolling_rank_pct(pe, _TD_HALF).diff(5)


def vvh_drv2_072_pb_pctrank_half_126d_5d_diff(pb: pd.Series) -> pd.Series:
    """5-day diff of P/B 126d percentile rank."""
    return _rolling_rank_pct(pb, _TD_HALF).diff(5)


def vvh_drv2_073_pe_zscore_half_126d_5d_diff(pe: pd.Series) -> pd.Series:
    """5-day diff of P/E 126d z-score."""
    return _zscore_rolling(pe, _TD_HALF).diff(5)


def vvh_drv2_074_divyield_zscore_252d_21d_slope(divyield: pd.Series) -> pd.Series:
    """OLS slope of div yield 252d z-score over trailing 21 days."""
    return _linslope(_zscore_rolling(divyield, _TD_YEAR), _TD_MON)


def vvh_drv2_075_composite_cheapness_4metric_1260d_5d_diff(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """5-day diff of 4-metric composite cheapness score (1260d) — long-horizon cheapening velocity."""
    s = (1.0 - _rolling_rank_pct(pe, _TD_5Y) + 1.0 - _rolling_rank_pct(pb, _TD_5Y)
         + 1.0 - _rolling_rank_pct(ps, _TD_5Y) + 1.0 - _rolling_rank_pct(evebitda, _TD_5Y)) / 4.0
    return s.diff(5)


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_HISTORY_REGISTRY_2ND_DERIVATIVES = {
    "vvh_drv2_001_pe_pctrank_252d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_001_pe_pctrank_252d_5d_diff},
    "vvh_drv2_002_pb_pctrank_252d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_002_pb_pctrank_252d_5d_diff},
    "vvh_drv2_003_ps_pctrank_252d_5d_diff": {"inputs": ["ps"], "func": vvh_drv2_003_ps_pctrank_252d_5d_diff},
    "vvh_drv2_004_evebitda_pctrank_252d_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv2_004_evebitda_pctrank_252d_5d_diff},
    "vvh_drv2_005_pe_zscore_252d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_005_pe_zscore_252d_5d_diff},
    "vvh_drv2_006_pb_zscore_252d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_006_pb_zscore_252d_5d_diff},
    "vvh_drv2_007_evebitda_zscore_252d_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv2_007_evebitda_zscore_252d_5d_diff},
    "vvh_drv2_008_pe_rangepos_252d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_008_pe_rangepos_252d_5d_diff},
    "vvh_drv2_009_pb_rangepos_252d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_009_pb_rangepos_252d_5d_diff},
    "vvh_drv2_010_pe_vs_median_252d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_010_pe_vs_median_252d_5d_diff},
    "vvh_drv2_011_pe_pctrank_1260d_21d_diff": {"inputs": ["pe"], "func": vvh_drv2_011_pe_pctrank_1260d_21d_diff},
    "vvh_drv2_012_pb_pctrank_1260d_21d_diff": {"inputs": ["pb"], "func": vvh_drv2_012_pb_pctrank_1260d_21d_diff},
    "vvh_drv2_013_composite_cheapness_4metric_252d_5d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_drv2_013_composite_cheapness_4metric_252d_5d_diff},
    "vvh_drv2_014_pe_expanding_zscore_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_014_pe_expanding_zscore_5d_diff},
    "vvh_drv2_015_pb_expanding_zscore_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_015_pb_expanding_zscore_5d_diff},
    "vvh_drv2_016_evebitda_rangepos_1260d_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv2_016_evebitda_rangepos_1260d_5d_diff},
    "vvh_drv2_017_pe_zscore_252d_21d_slope": {"inputs": ["pe"], "func": vvh_drv2_017_pe_zscore_252d_21d_slope},
    "vvh_drv2_018_pb_zscore_252d_63d_slope": {"inputs": ["pb"], "func": vvh_drv2_018_pb_zscore_252d_63d_slope},
    "vvh_drv2_019_pe_pctrank_252d_21d_slope": {"inputs": ["pe"], "func": vvh_drv2_019_pe_pctrank_252d_21d_slope},
    "vvh_drv2_020_pe_momentum_63d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_020_pe_momentum_63d_5d_diff},
    "vvh_drv2_021_ps_zscore_252d_5d_diff": {"inputs": ["ps"], "func": vvh_drv2_021_ps_zscore_252d_5d_diff},
    "vvh_drv2_022_divyield_pctrank_252d_5d_diff": {"inputs": ["divyield"], "func": vvh_drv2_022_divyield_pctrank_252d_5d_diff},
    "vvh_drv2_023_marketcap_zscore_252d_5d_diff": {"inputs": ["marketcap"], "func": vvh_drv2_023_marketcap_zscore_252d_5d_diff},
    "vvh_drv2_024_evebit_pctrank_252d_5d_diff": {"inputs": ["evebit"], "func": vvh_drv2_024_evebit_pctrank_252d_5d_diff},
    "vvh_drv2_025_pe_pctrank_252d_pct_change_21d": {"inputs": ["pe"], "func": vvh_drv2_025_pe_pctrank_252d_pct_change_21d},
    "vvh_drv2_026_pe_pctrank_252d_21d_diff": {"inputs": ["pe"], "func": vvh_drv2_026_pe_pctrank_252d_21d_diff},
    "vvh_drv2_027_pb_pctrank_252d_21d_diff": {"inputs": ["pb"], "func": vvh_drv2_027_pb_pctrank_252d_21d_diff},
    "vvh_drv2_028_ps_pctrank_252d_21d_diff": {"inputs": ["ps"], "func": vvh_drv2_028_ps_pctrank_252d_21d_diff},
    "vvh_drv2_029_evebitda_pctrank_252d_21d_diff": {"inputs": ["evebitda"], "func": vvh_drv2_029_evebitda_pctrank_252d_21d_diff},
    "vvh_drv2_030_evebit_pctrank_252d_21d_diff": {"inputs": ["evebit"], "func": vvh_drv2_030_evebit_pctrank_252d_21d_diff},
    "vvh_drv2_031_divyield_pctrank_252d_21d_diff": {"inputs": ["divyield"], "func": vvh_drv2_031_divyield_pctrank_252d_21d_diff},
    "vvh_drv2_032_marketcap_pctrank_252d_5d_diff": {"inputs": ["marketcap"], "func": vvh_drv2_032_marketcap_pctrank_252d_5d_diff},
    "vvh_drv2_033_pe_rangepos_1260d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_033_pe_rangepos_1260d_5d_diff},
    "vvh_drv2_034_pb_rangepos_1260d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_034_pb_rangepos_1260d_5d_diff},
    "vvh_drv2_035_ps_rangepos_252d_5d_diff": {"inputs": ["ps"], "func": vvh_drv2_035_ps_rangepos_252d_5d_diff},
    "vvh_drv2_036_ev_zscore_252d_5d_diff": {"inputs": ["ev"], "func": vvh_drv2_036_ev_zscore_252d_5d_diff},
    "vvh_drv2_037_pe_zscore_1260d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_037_pe_zscore_1260d_5d_diff},
    "vvh_drv2_038_pb_zscore_1260d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_038_pb_zscore_1260d_5d_diff},
    "vvh_drv2_039_evebitda_zscore_1260d_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv2_039_evebitda_zscore_1260d_5d_diff},
    "vvh_drv2_040_ps_zscore_252d_21d_diff": {"inputs": ["ps"], "func": vvh_drv2_040_ps_zscore_252d_21d_diff},
    "vvh_drv2_041_pe_pctrank_252d_63d_slope": {"inputs": ["pe"], "func": vvh_drv2_041_pe_pctrank_252d_63d_slope},
    "vvh_drv2_042_pb_pctrank_252d_63d_slope": {"inputs": ["pb"], "func": vvh_drv2_042_pb_pctrank_252d_63d_slope},
    "vvh_drv2_043_ps_pctrank_252d_63d_slope": {"inputs": ["ps"], "func": vvh_drv2_043_ps_pctrank_252d_63d_slope},
    "vvh_drv2_044_evebitda_pctrank_252d_63d_slope": {"inputs": ["evebitda"], "func": vvh_drv2_044_evebitda_pctrank_252d_63d_slope},
    "vvh_drv2_045_divyield_zscore_252d_5d_diff": {"inputs": ["divyield"], "func": vvh_drv2_045_divyield_zscore_252d_5d_diff},
    "vvh_drv2_046_pe_rangepos_252d_21d_diff": {"inputs": ["pe"], "func": vvh_drv2_046_pe_rangepos_252d_21d_diff},
    "vvh_drv2_047_pb_rangepos_252d_21d_diff": {"inputs": ["pb"], "func": vvh_drv2_047_pb_rangepos_252d_21d_diff},
    "vvh_drv2_048_pe_vs_median_252d_21d_diff": {"inputs": ["pe"], "func": vvh_drv2_048_pe_vs_median_252d_21d_diff},
    "vvh_drv2_049_evebitda_vs_median_252d_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv2_049_evebitda_vs_median_252d_5d_diff},
    "vvh_drv2_050_pb_vs_median_252d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_050_pb_vs_median_252d_5d_diff},
    "vvh_drv2_051_pe_expanding_zscore_21d_diff": {"inputs": ["pe"], "func": vvh_drv2_051_pe_expanding_zscore_21d_diff},
    "vvh_drv2_052_evebitda_expanding_zscore_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv2_052_evebitda_expanding_zscore_5d_diff},
    "vvh_drv2_053_marketcap_zscore_252d_21d_diff": {"inputs": ["marketcap"], "func": vvh_drv2_053_marketcap_zscore_252d_21d_diff},
    "vvh_drv2_054_composite_cheapness_4metric_252d_21d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_drv2_054_composite_cheapness_4metric_252d_21d_diff},
    "vvh_drv2_055_pe_zscore_252d_pct_change_21d": {"inputs": ["pe"], "func": vvh_drv2_055_pe_zscore_252d_pct_change_21d},
    "vvh_drv2_056_pb_pctrank_252d_pct_change_21d": {"inputs": ["pb"], "func": vvh_drv2_056_pb_pctrank_252d_pct_change_21d},
    "vvh_drv2_057_evebitda_pctrank_252d_pct_change_21d": {"inputs": ["evebitda"], "func": vvh_drv2_057_evebitda_pctrank_252d_pct_change_21d},
    "vvh_drv2_058_pe_pctrank_1260d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_058_pe_pctrank_1260d_5d_diff},
    "vvh_drv2_059_pb_pctrank_1260d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_059_pb_pctrank_1260d_5d_diff},
    "vvh_drv2_060_ps_pctrank_1260d_5d_diff": {"inputs": ["ps"], "func": vvh_drv2_060_ps_pctrank_1260d_5d_diff},
    "vvh_drv2_061_pe_zscore_252d_63d_slope": {"inputs": ["pe"], "func": vvh_drv2_061_pe_zscore_252d_63d_slope},
    "vvh_drv2_062_evebitda_zscore_252d_21d_slope": {"inputs": ["evebitda"], "func": vvh_drv2_062_evebitda_zscore_252d_21d_slope},
    "vvh_drv2_063_divyield_pctrank_252d_21d_slope": {"inputs": ["divyield"], "func": vvh_drv2_063_divyield_pctrank_252d_21d_slope},
    "vvh_drv2_064_evebit_zscore_252d_5d_diff": {"inputs": ["evebit"], "func": vvh_drv2_064_evebit_zscore_252d_5d_diff},
    "vvh_drv2_065_marketcap_pctrank_252d_21d_diff": {"inputs": ["marketcap"], "func": vvh_drv2_065_marketcap_pctrank_252d_21d_diff},
    "vvh_drv2_066_pe_rangepos_252d_63d_slope": {"inputs": ["pe"], "func": vvh_drv2_066_pe_rangepos_252d_63d_slope},
    "vvh_drv2_067_pb_rangepos_252d_63d_slope": {"inputs": ["pb"], "func": vvh_drv2_067_pb_rangepos_252d_63d_slope},
    "vvh_drv2_068_pb_momentum_63d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_068_pb_momentum_63d_5d_diff},
    "vvh_drv2_069_ps_momentum_63d_5d_diff": {"inputs": ["ps"], "func": vvh_drv2_069_ps_momentum_63d_5d_diff},
    "vvh_drv2_070_evebitda_momentum_63d_5d_diff": {"inputs": ["evebitda"], "func": vvh_drv2_070_evebitda_momentum_63d_5d_diff},
    "vvh_drv2_071_pe_pctrank_half_126d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_071_pe_pctrank_half_126d_5d_diff},
    "vvh_drv2_072_pb_pctrank_half_126d_5d_diff": {"inputs": ["pb"], "func": vvh_drv2_072_pb_pctrank_half_126d_5d_diff},
    "vvh_drv2_073_pe_zscore_half_126d_5d_diff": {"inputs": ["pe"], "func": vvh_drv2_073_pe_zscore_half_126d_5d_diff},
    "vvh_drv2_074_divyield_zscore_252d_21d_slope": {"inputs": ["divyield"], "func": vvh_drv2_074_divyield_zscore_252d_21d_slope},
    "vvh_drv2_075_composite_cheapness_4metric_1260d_5d_diff": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_drv2_075_composite_cheapness_4metric_1260d_5d_diff},
}
