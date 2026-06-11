"""
81_valuation_vs_history — Base Features 076-200
Domain: statistical positioning of current valuation multiples relative to the
        ticker's own trailing distribution (own-history percentile, z-score,
        range position, distance from trailing min/max, cheapness counts, etc.)
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


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _range_pos(s: pd.Series, w: int) -> pd.Series:
    """Position within rolling range: (s - min) / (max - min)."""
    lo = _rolling_min(s, w)
    hi = _rolling_max(s, w)
    return _safe_div(s - lo, hi - lo)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.clip(lower=_EPS))


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


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group H (076-085): Historical cheapness score across metrics ---

def vvh_076_historical_cheapness_pe_252d(pe: pd.Series) -> pd.Series:
    """Historical cheapness score for P/E: 1 - percentile rank (252d).
    Score=1 means at all-time cheapness extreme; 0 means most expensive."""
    return 1.0 - _rolling_rank_pct(pe, _TD_YEAR)


def vvh_077_historical_cheapness_pb_252d(pb: pd.Series) -> pd.Series:
    """Historical cheapness score for P/B: 1 - percentile rank (252d)."""
    return 1.0 - _rolling_rank_pct(pb, _TD_YEAR)


def vvh_078_historical_cheapness_ps_252d(ps: pd.Series) -> pd.Series:
    """Historical cheapness score for P/S: 1 - percentile rank (252d)."""
    return 1.0 - _rolling_rank_pct(ps, _TD_YEAR)


def vvh_079_historical_cheapness_evebitda_252d(evebitda: pd.Series) -> pd.Series:
    """Historical cheapness score for EV/EBITDA: 1 - percentile rank (252d)."""
    return 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)


def vvh_080_historical_cheapness_evebit_252d(evebit: pd.Series) -> pd.Series:
    """Historical cheapness score for EV/EBIT: 1 - percentile rank (252d)."""
    return 1.0 - _rolling_rank_pct(evebit, _TD_YEAR)


def vvh_081_historical_cheapness_pe_1260d(pe: pd.Series) -> pd.Series:
    """Historical cheapness score for P/E: 1 - percentile rank (1260d/5y)."""
    return 1.0 - _rolling_rank_pct(pe, _TD_5Y)


def vvh_082_historical_cheapness_pb_1260d(pb: pd.Series) -> pd.Series:
    """Historical cheapness score for P/B: 1 - percentile rank (1260d/5y)."""
    return 1.0 - _rolling_rank_pct(pb, _TD_5Y)


def vvh_083_historical_cheapness_evebitda_1260d(evebitda: pd.Series) -> pd.Series:
    """Historical cheapness score for EV/EBITDA: 1 - percentile rank (1260d/5y)."""
    return 1.0 - _rolling_rank_pct(evebitda, _TD_5Y)


def vvh_084_composite_cheapness_4metric_252d(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Composite cheapness score (4 metrics): mean of 1-pctrank across pe, pb, ps, evebitda (252d)."""
    s1 = 1.0 - _rolling_rank_pct(pe, _TD_YEAR)
    s2 = 1.0 - _rolling_rank_pct(pb, _TD_YEAR)
    s3 = 1.0 - _rolling_rank_pct(ps, _TD_YEAR)
    s4 = 1.0 - _rolling_rank_pct(evebitda, _TD_YEAR)
    return (s1 + s2 + s3 + s4) / 4.0


def vvh_085_composite_cheapness_4metric_1260d(pe: pd.Series, pb: pd.Series, ps: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Composite cheapness score (4 metrics): mean of 1-pctrank across pe, pb, ps, evebitda (1260d)."""
    s1 = 1.0 - _rolling_rank_pct(pe, _TD_5Y)
    s2 = 1.0 - _rolling_rank_pct(pb, _TD_5Y)
    s3 = 1.0 - _rolling_rank_pct(ps, _TD_5Y)
    s4 = 1.0 - _rolling_rank_pct(evebitda, _TD_5Y)
    return (s1 + s2 + s3 + s4) / 4.0


# --- Group I (086-095): Time since multiple was last this low ---

def vvh_086_pe_days_since_current_low_252d(pe: pd.Series) -> pd.Series:
    """Days since P/E was equal to or below current level (within 252d window).
    Low value = near multi-year low."""
    def days_since_low(x):
        cur = x[-1]
        idx_low = np.where(x[:-1] <= cur)[0]
        if len(idx_low) == 0:
            return float(len(x))
        return float(len(x) - 1 - idx_low[-1])
    return pe.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).apply(days_since_low, raw=True)


def vvh_087_pb_days_since_current_low_252d(pb: pd.Series) -> pd.Series:
    """Days since P/B was equal to or below current level (within 252d window)."""
    def days_since_low(x):
        cur = x[-1]
        idx_low = np.where(x[:-1] <= cur)[0]
        if len(idx_low) == 0:
            return float(len(x))
        return float(len(x) - 1 - idx_low[-1])
    return pb.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).apply(days_since_low, raw=True)


def vvh_088_ps_days_since_current_low_252d(ps: pd.Series) -> pd.Series:
    """Days since P/S was equal to or below current level (within 252d window)."""
    def days_since_low(x):
        cur = x[-1]
        idx_low = np.where(x[:-1] <= cur)[0]
        if len(idx_low) == 0:
            return float(len(x))
        return float(len(x) - 1 - idx_low[-1])
    return ps.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).apply(days_since_low, raw=True)


def vvh_089_evebitda_days_since_current_low_252d(evebitda: pd.Series) -> pd.Series:
    """Days since EV/EBITDA was equal to or below current level (within 252d window)."""
    def days_since_low(x):
        cur = x[-1]
        idx_low = np.where(x[:-1] <= cur)[0]
        if len(idx_low) == 0:
            return float(len(x))
        return float(len(x) - 1 - idx_low[-1])
    return evebitda.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 2)).apply(days_since_low, raw=True)


def vvh_090_pe_frac_cheaper_1260d(pe: pd.Series) -> pd.Series:
    """Fraction of trailing 1260-day window during which P/E was cheaper than today."""
    def frac_cheaper(x):
        cur = x[-1]
        return float((x[:-1] < cur).sum()) / max(1, len(x) - 1)
    return pe.rolling(_TD_5Y, min_periods=max(2, _TD_5Y // 2)).apply(frac_cheaper, raw=True)


def vvh_091_pb_frac_cheaper_1260d(pb: pd.Series) -> pd.Series:
    """Fraction of trailing 1260-day window during which P/B was cheaper than today."""
    def frac_cheaper(x):
        cur = x[-1]
        return float((x[:-1] < cur).sum()) / max(1, len(x) - 1)
    return pb.rolling(_TD_5Y, min_periods=max(2, _TD_5Y // 2)).apply(frac_cheaper, raw=True)


def vvh_092_ps_frac_cheaper_1260d(ps: pd.Series) -> pd.Series:
    """Fraction of trailing 1260-day window during which P/S was cheaper than today."""
    def frac_cheaper(x):
        cur = x[-1]
        return float((x[:-1] < cur).sum()) / max(1, len(x) - 1)
    return ps.rolling(_TD_5Y, min_periods=max(2, _TD_5Y // 2)).apply(frac_cheaper, raw=True)


def vvh_093_evebitda_frac_cheaper_1260d(evebitda: pd.Series) -> pd.Series:
    """Fraction of trailing 1260-day window during which EV/EBITDA was cheaper than today."""
    def frac_cheaper(x):
        cur = x[-1]
        return float((x[:-1] < cur).sum()) / max(1, len(x) - 1)
    return evebitda.rolling(_TD_5Y, min_periods=max(2, _TD_5Y // 2)).apply(frac_cheaper, raw=True)


def vvh_094_pe_below_10th_pctile_252d_flag(pe: pd.Series) -> pd.Series:
    """1 if P/E is below the 10th percentile of its trailing 252-day distribution."""
    q10 = pe.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.10)
    return (pe <= q10).astype(float)


def vvh_095_pe_below_10th_pctile_1260d_flag(pe: pd.Series) -> pd.Series:
    """1 if P/E is below the 10th percentile of its trailing 1260-day distribution."""
    q10 = pe.rolling(_TD_5Y, min_periods=max(1, _TD_5Y // 2)).quantile(0.10)
    return (pe <= q10).astype(float)


# --- Group J (096-105): EV and MarketCap own-history stats ---

def vvh_096_ev_pctrank_252d(ev: pd.Series) -> pd.Series:
    """Percentile rank of EV within trailing 252-day window."""
    return _rolling_rank_pct(ev, _TD_YEAR)


def vvh_097_ev_pctrank_1260d(ev: pd.Series) -> pd.Series:
    """Percentile rank of EV within trailing 1260-day window."""
    return _rolling_rank_pct(ev, _TD_5Y)


def vvh_098_ev_zscore_252d(ev: pd.Series) -> pd.Series:
    """Z-score of EV vs trailing 252-day mean and std."""
    return _zscore_rolling(ev, _TD_YEAR)


def vvh_099_ev_zscore_1260d(ev: pd.Series) -> pd.Series:
    """Z-score of EV vs trailing 1260-day mean and std."""
    return _zscore_rolling(ev, _TD_5Y)


def vvh_100_ev_rangepos_252d(ev: pd.Series) -> pd.Series:
    """EV position within its trailing 252-day min-max range."""
    return _range_pos(ev, _TD_YEAR)


def vvh_101_ev_rangepos_1260d(ev: pd.Series) -> pd.Series:
    """EV position within its trailing 1260-day min-max range."""
    return _range_pos(ev, _TD_5Y)


def vvh_102_marketcap_pctrank_252d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of market cap within trailing 252-day window."""
    return _rolling_rank_pct(marketcap, _TD_YEAR)


def vvh_103_marketcap_pctrank_1260d(marketcap: pd.Series) -> pd.Series:
    """Percentile rank of market cap within trailing 1260-day window."""
    return _rolling_rank_pct(marketcap, _TD_5Y)


def vvh_104_marketcap_zscore_252d(marketcap: pd.Series) -> pd.Series:
    """Z-score of market cap vs trailing 252-day mean and std."""
    return _zscore_rolling(marketcap, _TD_YEAR)


def vvh_105_marketcap_zscore_1260d(marketcap: pd.Series) -> pd.Series:
    """Z-score of market cap vs trailing 1260-day mean and std."""
    return _zscore_rolling(marketcap, _TD_5Y)


# --- Group K (106-115): DivYield own-history stats and evebit stats ---

def vvh_106_divyield_zscore_252d(divyield: pd.Series) -> pd.Series:
    """Z-score of div yield vs trailing 252-day mean and std."""
    return _zscore_rolling(divyield, _TD_YEAR)


def vvh_107_divyield_zscore_1260d(divyield: pd.Series) -> pd.Series:
    """Z-score of div yield vs trailing 1260-day mean and std."""
    return _zscore_rolling(divyield, _TD_5Y)


def vvh_108_divyield_rangepos_252d(divyield: pd.Series) -> pd.Series:
    """Div yield position within its trailing 252-day min-max range (high = cheap)."""
    return _range_pos(divyield, _TD_YEAR)


def vvh_109_divyield_rangepos_1260d(divyield: pd.Series) -> pd.Series:
    """Div yield position within its trailing 1260-day min-max range."""
    return _range_pos(divyield, _TD_5Y)


def vvh_110_divyield_expanding_zscore(divyield: pd.Series) -> pd.Series:
    """Expanding z-score of div yield (how extreme vs own full history)."""
    m = divyield.expanding(min_periods=5).mean()
    sd = divyield.expanding(min_periods=5).std()
    return _safe_div(divyield - m, sd)


def vvh_111_evebit_zscore_1260d(evebit: pd.Series) -> pd.Series:
    """Z-score of EV/EBIT vs trailing 1260-day mean and std."""
    return _zscore_rolling(evebit, _TD_5Y)


def vvh_112_evebit_rangepos_252d(evebit: pd.Series) -> pd.Series:
    """EV/EBIT position within its trailing 252-day min-max range."""
    return _range_pos(evebit, _TD_YEAR)


def vvh_113_evebit_rangepos_1260d(evebit: pd.Series) -> pd.Series:
    """EV/EBIT position within its trailing 1260-day min-max range."""
    return _range_pos(evebit, _TD_5Y)


def vvh_114_evebit_expanding_zscore(evebit: pd.Series) -> pd.Series:
    """Expanding z-score of EV/EBIT."""
    m = evebit.expanding(min_periods=5).mean()
    sd = evebit.expanding(min_periods=5).std()
    return _safe_div(evebit - m, sd)


def vvh_115_evebitda_expanding_pctrank(evebitda: pd.Series) -> pd.Series:
    """Expanding (all-history) percentile rank of EV/EBITDA."""
    return evebitda.expanding(min_periods=5).rank(pct=True)


# --- Group L (116-125): Trailing CV (coefficient of variation) & volatility of multiples ---

def vvh_116_pe_cv_252d(pe: pd.Series) -> pd.Series:
    """Coefficient of variation of P/E over trailing 252 days (std/mean)."""
    return _safe_div(_rolling_std(pe, _TD_YEAR), _rolling_mean(pe, _TD_YEAR).abs())


def vvh_117_pb_cv_252d(pb: pd.Series) -> pd.Series:
    """Coefficient of variation of P/B over trailing 252 days."""
    return _safe_div(_rolling_std(pb, _TD_YEAR), _rolling_mean(pb, _TD_YEAR).abs())


def vvh_118_ps_cv_252d(ps: pd.Series) -> pd.Series:
    """Coefficient of variation of P/S over trailing 252 days."""
    return _safe_div(_rolling_std(ps, _TD_YEAR), _rolling_mean(ps, _TD_YEAR).abs())


def vvh_119_evebitda_cv_252d(evebitda: pd.Series) -> pd.Series:
    """Coefficient of variation of EV/EBITDA over trailing 252 days."""
    return _safe_div(_rolling_std(evebitda, _TD_YEAR), _rolling_mean(evebitda, _TD_YEAR).abs())


def vvh_120_pe_std_252d(pe: pd.Series) -> pd.Series:
    """Rolling 252-day std dev of P/E (dispersion of the multiple)."""
    return _rolling_std(pe, _TD_YEAR)


def vvh_121_pb_std_252d(pb: pd.Series) -> pd.Series:
    """Rolling 252-day std dev of P/B."""
    return _rolling_std(pb, _TD_YEAR)


def vvh_122_ps_std_252d(ps: pd.Series) -> pd.Series:
    """Rolling 252-day std dev of P/S."""
    return _rolling_std(ps, _TD_YEAR)


def vvh_123_evebitda_std_252d(evebitda: pd.Series) -> pd.Series:
    """Rolling 252-day std dev of EV/EBITDA."""
    return _rolling_std(evebitda, _TD_YEAR)


def vvh_124_pe_iqr_252d(pe: pd.Series) -> pd.Series:
    """Rolling 252-day interquartile range (Q75 - Q25) of P/E."""
    q75 = pe.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = pe.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


def vvh_125_pb_iqr_252d(pb: pd.Series) -> pd.Series:
    """Rolling 252-day interquartile range (Q75 - Q25) of P/B."""
    q75 = pb.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = pb.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


# --- Group M (126-135): Slopes and trends of multiples ---

def vvh_126_pe_slope_63d(pe: pd.Series) -> pd.Series:
    """OLS slope of P/E over trailing 63 days (directional trend of multiple)."""
    return _linslope(pe, _TD_QTR)


def vvh_127_pe_slope_252d(pe: pd.Series) -> pd.Series:
    """OLS slope of P/E over trailing 252 days."""
    return _linslope(pe, _TD_YEAR)


def vvh_128_pb_slope_63d(pb: pd.Series) -> pd.Series:
    """OLS slope of P/B over trailing 63 days."""
    return _linslope(pb, _TD_QTR)


def vvh_129_pb_slope_252d(pb: pd.Series) -> pd.Series:
    """OLS slope of P/B over trailing 252 days."""
    return _linslope(pb, _TD_YEAR)


def vvh_130_ps_slope_63d(ps: pd.Series) -> pd.Series:
    """OLS slope of P/S over trailing 63 days."""
    return _linslope(ps, _TD_QTR)


def vvh_131_evebitda_slope_63d(evebitda: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA over trailing 63 days."""
    return _linslope(evebitda, _TD_QTR)


def vvh_132_evebitda_slope_252d(evebitda: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA over trailing 252 days."""
    return _linslope(evebitda, _TD_YEAR)


def vvh_133_ev_slope_63d(ev: pd.Series) -> pd.Series:
    """OLS slope of EV over trailing 63 days."""
    return _linslope(ev, _TD_QTR)


def vvh_134_marketcap_slope_63d(marketcap: pd.Series) -> pd.Series:
    """OLS slope of market cap over trailing 63 days."""
    return _linslope(marketcap, _TD_QTR)


def vvh_135_divyield_slope_63d(divyield: pd.Series) -> pd.Series:
    """OLS slope of dividend yield over trailing 63 days."""
    return _linslope(divyield, _TD_QTR)


# --- Group N (136-145): Cross-metric ratio own-history stats ---

def vvh_136_pe_to_pb_ratio_zscore_252d(pe: pd.Series, pb: pd.Series) -> pd.Series:
    """Z-score of P/E-to-P/B ratio vs trailing 252-day history."""
    ratio = _safe_div(pe, pb)
    return _zscore_rolling(ratio, _TD_YEAR)


def vvh_137_pe_to_ps_ratio_zscore_252d(pe: pd.Series, ps: pd.Series) -> pd.Series:
    """Z-score of P/E-to-P/S ratio vs trailing 252-day history."""
    ratio = _safe_div(pe, ps)
    return _zscore_rolling(ratio, _TD_YEAR)


def vvh_138_evebitda_to_pb_ratio_zscore_252d(evebitda: pd.Series, pb: pd.Series) -> pd.Series:
    """Z-score of EV/EBITDA-to-P/B ratio vs trailing 252-day history."""
    ratio = _safe_div(evebitda, pb)
    return _zscore_rolling(ratio, _TD_YEAR)


def vvh_139_ev_to_marketcap_zscore_252d(ev: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Z-score of EV/marketcap vs trailing 252-day history (leverage proxy)."""
    ratio = _safe_div(ev, marketcap)
    return _zscore_rolling(ratio, _TD_YEAR)


def vvh_140_divyield_to_ps_ratio_zscore_252d(divyield: pd.Series, ps: pd.Series) -> pd.Series:
    """Z-score of divyield/P/S ratio vs trailing 252-day history."""
    ratio = _safe_div(divyield, ps)
    return _zscore_rolling(ratio, _TD_YEAR)


def vvh_141_pe_momentum_63d(pe: pd.Series) -> pd.Series:
    """63-day pct change of P/E (momentum/compression of the multiple)."""
    return _safe_div(pe - pe.shift(_TD_QTR), pe.shift(_TD_QTR).abs())


def vvh_142_pb_momentum_63d(pb: pd.Series) -> pd.Series:
    """63-day pct change of P/B."""
    return _safe_div(pb - pb.shift(_TD_QTR), pb.shift(_TD_QTR).abs())


def vvh_143_evebitda_momentum_63d(evebitda: pd.Series) -> pd.Series:
    """63-day pct change of EV/EBITDA."""
    return _safe_div(evebitda - evebitda.shift(_TD_QTR), evebitda.shift(_TD_QTR).abs())


def vvh_144_ps_momentum_252d(ps: pd.Series) -> pd.Series:
    """252-day pct change of P/S (annual compression of the multiple)."""
    return _safe_div(ps - ps.shift(_TD_YEAR), ps.shift(_TD_YEAR).abs())


def vvh_145_pe_momentum_252d(pe: pd.Series) -> pd.Series:
    """252-day pct change of P/E."""
    return _safe_div(pe - pe.shift(_TD_YEAR), pe.shift(_TD_YEAR).abs())


# --- Group O (146-150): EWM-based own-history stats ---

def vvh_146_pe_vs_ewm_126(pe: pd.Series) -> pd.Series:
    """P/E as fraction of its 126-day EWM (exponential deviation from trend)."""
    ewm = _ewm_mean(pe, _TD_HALF)
    return _safe_div(pe, ewm)


def vvh_147_pb_vs_ewm_126(pb: pd.Series) -> pd.Series:
    """P/B as fraction of its 126-day EWM."""
    ewm = _ewm_mean(pb, _TD_HALF)
    return _safe_div(pb, ewm)


def vvh_148_evebitda_vs_ewm_252(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA as fraction of its 252-day EWM."""
    ewm = _ewm_mean(evebitda, _TD_YEAR)
    return _safe_div(evebitda, ewm)


def vvh_149_ps_vs_ewm_252(ps: pd.Series) -> pd.Series:
    """P/S as fraction of its 252-day EWM."""
    ewm = _ewm_mean(ps, _TD_YEAR)
    return _safe_div(ps, ewm)


def vvh_150_pe_below_q25_1260d_fraction_504d(pe: pd.Series) -> pd.Series:
    """Fraction of trailing 504d window where P/E was below its 1260d 25th percentile.
    High score = persistently at historical cheapness extreme."""
    q25 = pe.rolling(_TD_5Y, min_periods=max(1, _TD_5Y // 2)).quantile(0.25)
    below = (pe < q25).astype(float)
    return _rolling_mean(below, _TD_2Y)


# --- Group P (176-200): Additional own-history stats: IQR, quantiles, log-range, composite, time-since ---

def vvh_176_ps_iqr_252d(ps: pd.Series) -> pd.Series:
    """Rolling 252-day interquartile range (Q75 - Q25) of P/S."""
    q75 = ps.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = ps.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


def vvh_177_evebitda_iqr_252d(evebitda: pd.Series) -> pd.Series:
    """Rolling 252-day interquartile range of EV/EBITDA."""
    q75 = evebitda.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = evebitda.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


def vvh_178_divyield_iqr_252d(divyield: pd.Series) -> pd.Series:
    """Rolling 252-day interquartile range of dividend yield."""
    q75 = divyield.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.75)
    q25 = divyield.rolling(_TD_YEAR, min_periods=max(1, _TD_YEAR // 2)).quantile(0.25)
    return q75 - q25


def vvh_179_pe_zscore_half_126d(pe: pd.Series) -> pd.Series:
    """Z-score of P/E vs trailing 126-day mean and std."""
    return _zscore_rolling(pe, _TD_HALF)


def vvh_180_pb_zscore_half_126d(pb: pd.Series) -> pd.Series:
    """Z-score of P/B vs trailing 126-day mean and std."""
    return _zscore_rolling(pb, _TD_HALF)


def vvh_181_ps_zscore_half_126d(ps: pd.Series) -> pd.Series:
    """Z-score of P/S vs trailing 126-day mean and std."""
    return _zscore_rolling(ps, _TD_HALF)


def vvh_182_evebitda_zscore_half_126d(evebitda: pd.Series) -> pd.Series:
    """Z-score of EV/EBITDA vs trailing 126-day mean and std."""
    return _zscore_rolling(evebitda, _TD_HALF)


def vvh_183_marketcap_rangepos_1260d(marketcap: pd.Series) -> pd.Series:
    """Market cap position within its trailing 1260-day min-max range."""
    return _range_pos(marketcap, _TD_5Y)


def vvh_184_ev_rangepos_504d(ev: pd.Series) -> pd.Series:
    """EV position within its trailing 504-day min-max range."""
    return _range_pos(ev, _TD_2Y)


def vvh_185_pe_dist_from_504d_min(pe: pd.Series) -> pd.Series:
    """P/E percent above trailing 504-day minimum."""
    lo = _rolling_min(pe, _TD_2Y)
    return _safe_div(pe - lo, lo.abs())


def vvh_186_evebitda_dist_from_504d_min(evebitda: pd.Series) -> pd.Series:
    """EV/EBITDA percent above trailing 504-day minimum."""
    lo = _rolling_min(evebitda, _TD_2Y)
    return _safe_div(evebitda - lo, lo.abs())


def vvh_187_pb_dist_from_504d_min(pb: pd.Series) -> pd.Series:
    """P/B percent above trailing 504-day minimum."""
    lo = _rolling_min(pb, _TD_2Y)
    return _safe_div(pb - lo, lo.abs())


def vvh_188_pe_slope_126d(pe: pd.Series) -> pd.Series:
    """OLS slope of P/E over trailing 126 days (semi-annual trend of multiple)."""
    return _linslope(pe, _TD_HALF)


def vvh_189_pb_slope_126d(pb: pd.Series) -> pd.Series:
    """OLS slope of P/B over trailing 126 days."""
    return _linslope(pb, _TD_HALF)


def vvh_190_ps_slope_252d(ps: pd.Series) -> pd.Series:
    """OLS slope of P/S over trailing 252 days."""
    return _linslope(ps, _TD_YEAR)


def vvh_191_divyield_slope_252d(divyield: pd.Series) -> pd.Series:
    """OLS slope of dividend yield over trailing 252 days."""
    return _linslope(divyield, _TD_YEAR)


def vvh_192_pe_to_evebitda_ratio_zscore_252d(pe: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Z-score of P/E-to-EV/EBITDA ratio vs trailing 252-day history."""
    ratio = _safe_div(pe, evebitda)
    return _zscore_rolling(ratio, _TD_YEAR)


def vvh_193_pb_to_ps_ratio_zscore_252d(pb: pd.Series, ps: pd.Series) -> pd.Series:
    """Z-score of P/B-to-P/S ratio vs trailing 252-day history."""
    ratio = _safe_div(pb, ps)
    return _zscore_rolling(ratio, _TD_YEAR)


def vvh_194_evebit_to_evebitda_ratio_zscore_252d(evebit: pd.Series, evebitda: pd.Series) -> pd.Series:
    """Z-score of EV/EBIT-to-EV/EBITDA ratio vs trailing 252-day history."""
    ratio = _safe_div(evebit, evebitda)
    return _zscore_rolling(ratio, _TD_YEAR)


def vvh_195_pe_momentum_126d(pe: pd.Series) -> pd.Series:
    """126-day pct change of P/E (semi-annual compression of the multiple)."""
    return _safe_div(pe - pe.shift(_TD_HALF), pe.shift(_TD_HALF).abs())


def vvh_196_evebitda_momentum_252d(evebitda: pd.Series) -> pd.Series:
    """252-day pct change of EV/EBITDA (annual compression of the multiple)."""
    return _safe_div(evebitda - evebitda.shift(_TD_YEAR), evebitda.shift(_TD_YEAR).abs())


def vvh_197_pb_momentum_252d(pb: pd.Series) -> pd.Series:
    """252-day pct change of P/B."""
    return _safe_div(pb - pb.shift(_TD_YEAR), pb.shift(_TD_YEAR).abs())


def vvh_198_marketcap_vs_trailing_median_252d(marketcap: pd.Series) -> pd.Series:
    """Market cap as fraction of its trailing 252-day median."""
    med = _rolling_median(marketcap, _TD_YEAR)
    return _safe_div(marketcap, med)


def vvh_199_ev_vs_trailing_median_252d(ev: pd.Series) -> pd.Series:
    """EV as fraction of its trailing 252-day median."""
    med = _rolling_median(ev, _TD_YEAR)
    return _safe_div(ev, med)


def vvh_200_composite_cheapness_evebit_divyield_252d(evebit: pd.Series, divyield: pd.Series) -> pd.Series:
    """Composite cheapness: EV/EBIT cheapness (1-rank) averaged with divyield rank (252d)."""
    s1 = 1.0 - _rolling_rank_pct(evebit, _TD_YEAR)
    s2 = _rolling_rank_pct(divyield, _TD_YEAR)
    return (s1 + s2) / 2.0


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_HISTORY_REGISTRY_076_150 = {
    "vvh_076_historical_cheapness_pe_252d": {"inputs": ["pe"], "func": vvh_076_historical_cheapness_pe_252d},
    "vvh_077_historical_cheapness_pb_252d": {"inputs": ["pb"], "func": vvh_077_historical_cheapness_pb_252d},
    "vvh_078_historical_cheapness_ps_252d": {"inputs": ["ps"], "func": vvh_078_historical_cheapness_ps_252d},
    "vvh_079_historical_cheapness_evebitda_252d": {"inputs": ["evebitda"], "func": vvh_079_historical_cheapness_evebitda_252d},
    "vvh_080_historical_cheapness_evebit_252d": {"inputs": ["evebit"], "func": vvh_080_historical_cheapness_evebit_252d},
    "vvh_081_historical_cheapness_pe_1260d": {"inputs": ["pe"], "func": vvh_081_historical_cheapness_pe_1260d},
    "vvh_082_historical_cheapness_pb_1260d": {"inputs": ["pb"], "func": vvh_082_historical_cheapness_pb_1260d},
    "vvh_083_historical_cheapness_evebitda_1260d": {"inputs": ["evebitda"], "func": vvh_083_historical_cheapness_evebitda_1260d},
    "vvh_084_composite_cheapness_4metric_252d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_084_composite_cheapness_4metric_252d},
    "vvh_085_composite_cheapness_4metric_1260d": {"inputs": ["pe", "pb", "ps", "evebitda"], "func": vvh_085_composite_cheapness_4metric_1260d},
    "vvh_086_pe_days_since_current_low_252d": {"inputs": ["pe"], "func": vvh_086_pe_days_since_current_low_252d},
    "vvh_087_pb_days_since_current_low_252d": {"inputs": ["pb"], "func": vvh_087_pb_days_since_current_low_252d},
    "vvh_088_ps_days_since_current_low_252d": {"inputs": ["ps"], "func": vvh_088_ps_days_since_current_low_252d},
    "vvh_089_evebitda_days_since_current_low_252d": {"inputs": ["evebitda"], "func": vvh_089_evebitda_days_since_current_low_252d},
    "vvh_090_pe_frac_cheaper_1260d": {"inputs": ["pe"], "func": vvh_090_pe_frac_cheaper_1260d},
    "vvh_091_pb_frac_cheaper_1260d": {"inputs": ["pb"], "func": vvh_091_pb_frac_cheaper_1260d},
    "vvh_092_ps_frac_cheaper_1260d": {"inputs": ["ps"], "func": vvh_092_ps_frac_cheaper_1260d},
    "vvh_093_evebitda_frac_cheaper_1260d": {"inputs": ["evebitda"], "func": vvh_093_evebitda_frac_cheaper_1260d},
    "vvh_094_pe_below_10th_pctile_252d_flag": {"inputs": ["pe"], "func": vvh_094_pe_below_10th_pctile_252d_flag},
    "vvh_095_pe_below_10th_pctile_1260d_flag": {"inputs": ["pe"], "func": vvh_095_pe_below_10th_pctile_1260d_flag},
    "vvh_096_ev_pctrank_252d": {"inputs": ["ev"], "func": vvh_096_ev_pctrank_252d},
    "vvh_097_ev_pctrank_1260d": {"inputs": ["ev"], "func": vvh_097_ev_pctrank_1260d},
    "vvh_098_ev_zscore_252d": {"inputs": ["ev"], "func": vvh_098_ev_zscore_252d},
    "vvh_099_ev_zscore_1260d": {"inputs": ["ev"], "func": vvh_099_ev_zscore_1260d},
    "vvh_100_ev_rangepos_252d": {"inputs": ["ev"], "func": vvh_100_ev_rangepos_252d},
    "vvh_101_ev_rangepos_1260d": {"inputs": ["ev"], "func": vvh_101_ev_rangepos_1260d},
    "vvh_102_marketcap_pctrank_252d": {"inputs": ["marketcap"], "func": vvh_102_marketcap_pctrank_252d},
    "vvh_103_marketcap_pctrank_1260d": {"inputs": ["marketcap"], "func": vvh_103_marketcap_pctrank_1260d},
    "vvh_104_marketcap_zscore_252d": {"inputs": ["marketcap"], "func": vvh_104_marketcap_zscore_252d},
    "vvh_105_marketcap_zscore_1260d": {"inputs": ["marketcap"], "func": vvh_105_marketcap_zscore_1260d},
    "vvh_106_divyield_zscore_252d": {"inputs": ["divyield"], "func": vvh_106_divyield_zscore_252d},
    "vvh_107_divyield_zscore_1260d": {"inputs": ["divyield"], "func": vvh_107_divyield_zscore_1260d},
    "vvh_108_divyield_rangepos_252d": {"inputs": ["divyield"], "func": vvh_108_divyield_rangepos_252d},
    "vvh_109_divyield_rangepos_1260d": {"inputs": ["divyield"], "func": vvh_109_divyield_rangepos_1260d},
    "vvh_110_divyield_expanding_zscore": {"inputs": ["divyield"], "func": vvh_110_divyield_expanding_zscore},
    "vvh_111_evebit_zscore_1260d": {"inputs": ["evebit"], "func": vvh_111_evebit_zscore_1260d},
    "vvh_112_evebit_rangepos_252d": {"inputs": ["evebit"], "func": vvh_112_evebit_rangepos_252d},
    "vvh_113_evebit_rangepos_1260d": {"inputs": ["evebit"], "func": vvh_113_evebit_rangepos_1260d},
    "vvh_114_evebit_expanding_zscore": {"inputs": ["evebit"], "func": vvh_114_evebit_expanding_zscore},
    "vvh_115_evebitda_expanding_pctrank": {"inputs": ["evebitda"], "func": vvh_115_evebitda_expanding_pctrank},
    "vvh_116_pe_cv_252d": {"inputs": ["pe"], "func": vvh_116_pe_cv_252d},
    "vvh_117_pb_cv_252d": {"inputs": ["pb"], "func": vvh_117_pb_cv_252d},
    "vvh_118_ps_cv_252d": {"inputs": ["ps"], "func": vvh_118_ps_cv_252d},
    "vvh_119_evebitda_cv_252d": {"inputs": ["evebitda"], "func": vvh_119_evebitda_cv_252d},
    "vvh_120_pe_std_252d": {"inputs": ["pe"], "func": vvh_120_pe_std_252d},
    "vvh_121_pb_std_252d": {"inputs": ["pb"], "func": vvh_121_pb_std_252d},
    "vvh_122_ps_std_252d": {"inputs": ["ps"], "func": vvh_122_ps_std_252d},
    "vvh_123_evebitda_std_252d": {"inputs": ["evebitda"], "func": vvh_123_evebitda_std_252d},
    "vvh_124_pe_iqr_252d": {"inputs": ["pe"], "func": vvh_124_pe_iqr_252d},
    "vvh_125_pb_iqr_252d": {"inputs": ["pb"], "func": vvh_125_pb_iqr_252d},
    "vvh_126_pe_slope_63d": {"inputs": ["pe"], "func": vvh_126_pe_slope_63d},
    "vvh_127_pe_slope_252d": {"inputs": ["pe"], "func": vvh_127_pe_slope_252d},
    "vvh_128_pb_slope_63d": {"inputs": ["pb"], "func": vvh_128_pb_slope_63d},
    "vvh_129_pb_slope_252d": {"inputs": ["pb"], "func": vvh_129_pb_slope_252d},
    "vvh_130_ps_slope_63d": {"inputs": ["ps"], "func": vvh_130_ps_slope_63d},
    "vvh_131_evebitda_slope_63d": {"inputs": ["evebitda"], "func": vvh_131_evebitda_slope_63d},
    "vvh_132_evebitda_slope_252d": {"inputs": ["evebitda"], "func": vvh_132_evebitda_slope_252d},
    "vvh_133_ev_slope_63d": {"inputs": ["ev"], "func": vvh_133_ev_slope_63d},
    "vvh_134_marketcap_slope_63d": {"inputs": ["marketcap"], "func": vvh_134_marketcap_slope_63d},
    "vvh_135_divyield_slope_63d": {"inputs": ["divyield"], "func": vvh_135_divyield_slope_63d},
    "vvh_136_pe_to_pb_ratio_zscore_252d": {"inputs": ["pe", "pb"], "func": vvh_136_pe_to_pb_ratio_zscore_252d},
    "vvh_137_pe_to_ps_ratio_zscore_252d": {"inputs": ["pe", "ps"], "func": vvh_137_pe_to_ps_ratio_zscore_252d},
    "vvh_138_evebitda_to_pb_ratio_zscore_252d": {"inputs": ["evebitda", "pb"], "func": vvh_138_evebitda_to_pb_ratio_zscore_252d},
    "vvh_139_ev_to_marketcap_zscore_252d": {"inputs": ["ev", "marketcap"], "func": vvh_139_ev_to_marketcap_zscore_252d},
    "vvh_140_divyield_to_ps_ratio_zscore_252d": {"inputs": ["divyield", "ps"], "func": vvh_140_divyield_to_ps_ratio_zscore_252d},
    "vvh_141_pe_momentum_63d": {"inputs": ["pe"], "func": vvh_141_pe_momentum_63d},
    "vvh_142_pb_momentum_63d": {"inputs": ["pb"], "func": vvh_142_pb_momentum_63d},
    "vvh_143_evebitda_momentum_63d": {"inputs": ["evebitda"], "func": vvh_143_evebitda_momentum_63d},
    "vvh_144_ps_momentum_252d": {"inputs": ["ps"], "func": vvh_144_ps_momentum_252d},
    "vvh_145_pe_momentum_252d": {"inputs": ["pe"], "func": vvh_145_pe_momentum_252d},
    "vvh_146_pe_vs_ewm_126": {"inputs": ["pe"], "func": vvh_146_pe_vs_ewm_126},
    "vvh_147_pb_vs_ewm_126": {"inputs": ["pb"], "func": vvh_147_pb_vs_ewm_126},
    "vvh_148_evebitda_vs_ewm_252": {"inputs": ["evebitda"], "func": vvh_148_evebitda_vs_ewm_252},
    "vvh_149_ps_vs_ewm_252": {"inputs": ["ps"], "func": vvh_149_ps_vs_ewm_252},
    "vvh_150_pe_below_q25_1260d_fraction_504d": {"inputs": ["pe"], "func": vvh_150_pe_below_q25_1260d_fraction_504d},
    "vvh_176_ps_iqr_252d": {"inputs": ["ps"], "func": vvh_176_ps_iqr_252d},
    "vvh_177_evebitda_iqr_252d": {"inputs": ["evebitda"], "func": vvh_177_evebitda_iqr_252d},
    "vvh_178_divyield_iqr_252d": {"inputs": ["divyield"], "func": vvh_178_divyield_iqr_252d},
    "vvh_179_pe_zscore_half_126d": {"inputs": ["pe"], "func": vvh_179_pe_zscore_half_126d},
    "vvh_180_pb_zscore_half_126d": {"inputs": ["pb"], "func": vvh_180_pb_zscore_half_126d},
    "vvh_181_ps_zscore_half_126d": {"inputs": ["ps"], "func": vvh_181_ps_zscore_half_126d},
    "vvh_182_evebitda_zscore_half_126d": {"inputs": ["evebitda"], "func": vvh_182_evebitda_zscore_half_126d},
    "vvh_183_marketcap_rangepos_1260d": {"inputs": ["marketcap"], "func": vvh_183_marketcap_rangepos_1260d},
    "vvh_184_ev_rangepos_504d": {"inputs": ["ev"], "func": vvh_184_ev_rangepos_504d},
    "vvh_185_pe_dist_from_504d_min": {"inputs": ["pe"], "func": vvh_185_pe_dist_from_504d_min},
    "vvh_186_evebitda_dist_from_504d_min": {"inputs": ["evebitda"], "func": vvh_186_evebitda_dist_from_504d_min},
    "vvh_187_pb_dist_from_504d_min": {"inputs": ["pb"], "func": vvh_187_pb_dist_from_504d_min},
    "vvh_188_pe_slope_126d": {"inputs": ["pe"], "func": vvh_188_pe_slope_126d},
    "vvh_189_pb_slope_126d": {"inputs": ["pb"], "func": vvh_189_pb_slope_126d},
    "vvh_190_ps_slope_252d": {"inputs": ["ps"], "func": vvh_190_ps_slope_252d},
    "vvh_191_divyield_slope_252d": {"inputs": ["divyield"], "func": vvh_191_divyield_slope_252d},
    "vvh_192_pe_to_evebitda_ratio_zscore_252d": {"inputs": ["pe", "evebitda"], "func": vvh_192_pe_to_evebitda_ratio_zscore_252d},
    "vvh_193_pb_to_ps_ratio_zscore_252d": {"inputs": ["pb", "ps"], "func": vvh_193_pb_to_ps_ratio_zscore_252d},
    "vvh_194_evebit_to_evebitda_ratio_zscore_252d": {"inputs": ["evebit", "evebitda"], "func": vvh_194_evebit_to_evebitda_ratio_zscore_252d},
    "vvh_195_pe_momentum_126d": {"inputs": ["pe"], "func": vvh_195_pe_momentum_126d},
    "vvh_196_evebitda_momentum_252d": {"inputs": ["evebitda"], "func": vvh_196_evebitda_momentum_252d},
    "vvh_197_pb_momentum_252d": {"inputs": ["pb"], "func": vvh_197_pb_momentum_252d},
    "vvh_198_marketcap_vs_trailing_median_252d": {"inputs": ["marketcap"], "func": vvh_198_marketcap_vs_trailing_median_252d},
    "vvh_199_ev_vs_trailing_median_252d": {"inputs": ["ev"], "func": vvh_199_ev_vs_trailing_median_252d},
    "vvh_200_composite_cheapness_evebit_divyield_252d": {"inputs": ["evebit", "divyield"], "func": vvh_200_composite_cheapness_evebit_divyield_252d},
}
