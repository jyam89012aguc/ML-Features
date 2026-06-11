"""
82_valuation_vs_peers — Base Features 076-200
Domain: multiples vs sector/industry peer medians (cross-sectional valuation)
Asset class: US equities | Daily valuation metrics (SF1-derived, daily frequency)
Target context: capitulation — absolute multi-year low / maximum distress

PEER-MEDIAN INPUT CONTRACT:
    Each function receives the ticker's own daily metric Series and a precomputed
    sector/industry peer-median Series of the same daily index named
    peer_median_<metric>  (e.g. peer_median_pe, peer_median_pb, peer_median_ps,
    peer_median_ev, peer_median_marketcap, peer_median_evebit, peer_median_evebitda,
    peer_median_divyield).  The pipeline computes these universe-wide sector/industry
    medians and passes them in.  All functions look strictly backward.

Inputs available (16 total):
    Own metrics:         pe, pb, ps, ev, marketcap, evebit, evebitda, divyield
    Peer-median series:  peer_median_pe, peer_median_pb, peer_median_ps,
                         peer_median_ev, peer_median_marketcap, peer_median_evebit,
                         peer_median_evebitda, peer_median_divyield
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_HALF  = 126
_TD_QTR   = 63
_TD_MON   = 21
_TD_WEEK  = 5
_EPS      = 1e-9

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


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _log_safe(s: pd.Series) -> pd.Series:
    return np.log(s.abs().clip(lower=_EPS))


def _rel_ratio(own: pd.Series, peer: pd.Series) -> pd.Series:
    d = peer.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return own / d


def _log_rel(own: pd.Series, peer: pd.Series) -> pd.Series:
    ratio = _rel_ratio(own, peer)
    return np.log(ratio.abs().clip(lower=_EPS)) * np.sign(ratio)


def _gap(own: pd.Series, peer: pd.Series) -> pd.Series:
    return own - peer


def _discount_flag(own: pd.Series, peer: pd.Series) -> pd.Series:
    return (own < peer).astype(float)


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods (scalar per window)."""
    def _slope(x):
        n = len(x)
        if n < max(2, w // 2):
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m = x.mean()
        num = ((xi - xi_m) * (x - x_m)).sum()
        den = ((xi - xi_m) ** 2).sum()
        if den == 0:
            return np.nan
        return num / den
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group J (076-085): Trend / velocity of relative-valuation ratio ---

def vvp_076_pe_rel_ratio_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day change in P/E relative ratio (weekly velocity of de-rating vs peers)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.diff(5)


def vvp_077_pb_rel_ratio_21d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """21-day change in P/B relative ratio (monthly velocity of relative re/de-rating)."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.diff(21)


def vvp_078_ps_rel_ratio_63d_diff(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """63-day change in P/S relative ratio (quarterly drift vs peers)."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.diff(63)


def vvp_079_evebitda_rel_ratio_21d_diff(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """21-day change in EV/EBITDA relative ratio."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r.diff(21)


def vvp_080_log_pe_5d_diff(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """5-day change in log(P/E / peer) — log-velocity of relative de-rating."""
    r = _log_rel(pe, peer_median_pe)
    return r.diff(5)


def vvp_081_log_pb_21d_diff(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """21-day change in log(P/B / peer)."""
    r = _log_rel(pb, peer_median_pb)
    return r.diff(21)


def vvp_082_pe_rel_ratio_linslope_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """OLS slope of P/E relative ratio over 63-day window (trend of relative re/de-rating)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _linslope(r, _TD_QTR)


def vvp_083_pb_rel_ratio_linslope_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """OLS slope of P/B relative ratio over 252-day window."""
    r = _rel_ratio(pb, peer_median_pb)
    return _linslope(r, _TD_YEAR)


def vvp_084_ps_rel_ratio_linslope_63d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """OLS slope of P/S relative ratio over 63-day window."""
    r = _rel_ratio(ps, peer_median_ps)
    return _linslope(r, _TD_QTR)


def vvp_085_log_evebitda_linslope_63d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """OLS slope of log(EV/EBITDA / peer) over 63-day window."""
    r = _log_rel(evebitda, peer_median_evebitda)
    return _linslope(r, _TD_QTR)


# --- Group K (086-095): EWM-smoothed relative positions ---

def vvp_086_pe_rel_ratio_ewm21(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """EWM(21) of P/E relative ratio (smooth short-run relative valuation)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _ewm_mean(r, 21)


def vvp_087_pb_rel_ratio_ewm63(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """EWM(63) of P/B relative ratio (smooth quarterly relative valuation)."""
    r = _rel_ratio(pb, peer_median_pb)
    return _ewm_mean(r, 63)


def vvp_088_ps_rel_ratio_ewm63(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """EWM(63) of P/S relative ratio."""
    r = _rel_ratio(ps, peer_median_ps)
    return _ewm_mean(r, 63)


def vvp_089_log_pe_ewm21(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """EWM(21) of log(P/E / peer) (exponentially smoothed log-relative valuation)."""
    r = _log_rel(pe, peer_median_pe)
    return _ewm_mean(r, 21)


def vvp_090_evebitda_rel_ratio_ewm21(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """EWM(21) of EV/EBITDA relative ratio."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return _ewm_mean(r, 21)


def vvp_091_log_pb_ewm63(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """EWM(63) of log(P/B / peer)."""
    r = _log_rel(pb, peer_median_pb)
    return _ewm_mean(r, 63)


def vvp_092_divyield_rel_ratio_ewm21(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """EWM(21) of div-yield relative ratio (smoothed yield advantage vs peers)."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return _ewm_mean(r, 21)


def vvp_093_pe_ewm_vs_rolling_gap(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """EWM(21) minus SMA(63) of P/E relative ratio (short-run vs medium-run convergence)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _ewm_mean(r, 21) - _rolling_mean(r, _TD_QTR)


def vvp_094_log_ps_ewm21(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """EWM(21) of log(P/S / peer)."""
    r = _log_rel(ps, peer_median_ps)
    return _ewm_mean(r, 21)


def vvp_095_evebit_rel_ratio_ewm63(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """EWM(63) of EV/EBIT relative ratio."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return _ewm_mean(r, 63)


# --- Group L (096-105): Relative-discount streaks and sign runs ---

def vvp_096_pe_discount_streak(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Consecutive days below peer P/E median (current below-peer streak length)."""
    below = _discount_flag(pe, peer_median_pe)
    def _streak(x):
        # x is a numpy array (raw=True)
        if x[-1] == 0:
            return 0.0
        n = 0
        for v in x[::-1]:
            if v == 1:
                n += 1
            else:
                break
        return float(n)
    return below.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def vvp_097_pb_discount_streak(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Consecutive days below peer P/B median."""
    below = _discount_flag(pb, peer_median_pb)
    def _streak(x):
        if x[-1] == 0:
            return 0.0
        n = 0
        for v in x[::-1]:
            if v == 1:
                n += 1
            else:
                break
        return float(n)
    return below.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def vvp_098_ps_discount_streak(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Consecutive days below peer P/S median."""
    below = _discount_flag(ps, peer_median_ps)
    def _streak(x):
        if x[-1] == 0:
            return 0.0
        n = 0
        for v in x[::-1]:
            if v == 1:
                n += 1
            else:
                break
        return float(n)
    return below.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def vvp_099_evebitda_discount_streak(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Consecutive days below peer EV/EBITDA median."""
    below = _discount_flag(evebitda, peer_median_evebitda)
    def _streak(x):
        if x[-1] == 0:
            return 0.0
        n = 0
        for v in x[::-1]:
            if v == 1:
                n += 1
            else:
                break
        return float(n)
    return below.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def vvp_100_pe_sign_change_rate_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Rate of sign changes in P/E discount flag over 63 days (regime instability)."""
    below = _discount_flag(pe, peer_median_pe)
    changes = below.diff(1).abs()
    return _rolling_sum(changes, _TD_QTR)


def vvp_101_pb_sign_change_rate_63d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Rate of sign changes in P/B discount flag over 63 days."""
    below = _discount_flag(pb, peer_median_pb)
    changes = below.diff(1).abs()
    return _rolling_sum(changes, _TD_QTR)


def vvp_102_log_pe_sign_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Sign of log(P/E / peer) smoothed over 63 days (sustained discount direction)."""
    r = _log_rel(pe, peer_median_pe)
    return np.sign(_rolling_mean(r, _TD_QTR))


def vvp_103_pe_discount_streak_norm_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """P/E below-peer streak normalized by 252 days (fraction of year in below-peer run)."""
    below = _discount_flag(pe, peer_median_pe)
    def _streak(x):
        if x[-1] == 0:
            return 0.0
        n = 0
        for v in x[::-1]:
            if v == 1:
                n += 1
            else:
                break
        return float(n)
    streak = below.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)
    return streak / _TD_YEAR


def vvp_104_multi_metric_discount_streak(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """Consecutive days where ALL of PE/PB/PS are below peer medians simultaneously."""
    all_below = (
        _discount_flag(pe, peer_median_pe) *
        _discount_flag(pb, peer_median_pb) *
        _discount_flag(ps, peer_median_ps)
    )
    def _streak(x):
        if x[-1] == 0:
            return 0.0
        n = 0
        for v in x[::-1]:
            if v == 1:
                n += 1
            else:
                break
        return float(n)
    return all_below.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


def vvp_105_divyield_above_peer_streak(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Consecutive days where div yield exceeds peer median (yield-advantage streak)."""
    above = (divyield > peer_median_divyield).astype(float)
    def _streak(x):
        if x[-1] == 0:
            return 0.0
        n = 0
        for v in x[::-1]:
            if v == 1:
                n += 1
            else:
                break
        return float(n)
    return above.rolling(_TD_2Y, min_periods=1).apply(_streak, raw=True)


# --- Group M (106-115): Relative-discount rolling volatility and range ---

def vvp_106_pe_rel_ratio_std_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """63-day rolling std of P/E relative ratio (instability of relative valuation)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _rolling_std(r, _TD_QTR)


def vvp_107_pb_rel_ratio_std_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """252-day rolling std of P/B relative ratio."""
    r = _rel_ratio(pb, peer_median_pb)
    return _rolling_std(r, _TD_YEAR)


def vvp_108_log_pe_std_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """252-day rolling std of log(P/E / peer) (log-relative volatility)."""
    r = _log_rel(pe, peer_median_pe)
    return _rolling_std(r, _TD_YEAR)


def vvp_109_ps_rel_ratio_range_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """252-day range (max - min) of P/S relative ratio (valuation spread vs peers)."""
    r = _rel_ratio(ps, peer_median_ps)
    return _rolling_max(r, _TD_YEAR) - _rolling_min(r, _TD_YEAR)


def vvp_110_evebitda_rel_ratio_std_63d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """63-day rolling std of EV/EBITDA relative ratio."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return _rolling_std(r, _TD_QTR)


def vvp_111_pe_rel_ratio_cv_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Coefficient of variation of P/E relative ratio over 252 days (relative dispersion)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _safe_div(_rolling_std(r, _TD_YEAR), _rolling_mean(r, _TD_YEAR).abs())


def vvp_112_log_pb_std_63d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """63-day rolling std of log(P/B / peer)."""
    r = _log_rel(pb, peer_median_pb)
    return _rolling_std(r, _TD_QTR)


def vvp_113_pe_rel_ratio_range_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """63-day range of P/E relative ratio (short-run relative valuation spread)."""
    r = _rel_ratio(pe, peer_median_pe)
    return _rolling_max(r, _TD_QTR) - _rolling_min(r, _TD_QTR)


def vvp_114_divyield_rel_ratio_std_252d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """252-day rolling std of div-yield relative ratio."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return _rolling_std(r, _TD_YEAR)


def vvp_115_evebit_rel_ratio_std_252d(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """252-day rolling std of EV/EBIT relative ratio."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return _rolling_std(r, _TD_YEAR)


# --- Group N (116-125): Cross-metric relative-cheapness composites ---

def vvp_116_price_multiples_avg_rel_ratio(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """Mean of PE/PB/PS relative-to-peer ratios (average price-multiple relative position)."""
    r_pe = _rel_ratio(pe, peer_median_pe)
    r_pb = _rel_ratio(pb, peer_median_pb)
    r_ps = _rel_ratio(ps, peer_median_ps)
    return (r_pe + r_pb + r_ps) / 3.0


def vvp_117_ev_multiples_avg_rel_ratio(
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """Mean of EV/EBIT and EV/EBITDA relative ratios (enterprise-multiple composite)."""
    r_eb  = _rel_ratio(evebit, peer_median_evebit)
    r_ebd = _rel_ratio(evebitda, peer_median_evebitda)
    return (r_eb + r_ebd) / 2.0


def vvp_118_all_multiples_avg_log_rel(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """Mean of log-relative for PE/PB/PS/EVEBITDA (composite log-discount signal)."""
    l_pe  = _log_rel(pe, peer_median_pe)
    l_pb  = _log_rel(pb, peer_median_pb)
    l_ps  = _log_rel(ps, peer_median_ps)
    l_evd = _log_rel(evebitda, peer_median_evebitda)
    return (l_pe + l_pb + l_ps + l_evd) / 4.0


def vvp_119_price_minus_ev_composite_rel(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """Price-multiples composite minus EV-multiple (mismatch: cheap price vs EV)."""
    price_rel = (_rel_ratio(pe, peer_median_pe) + _rel_ratio(pb, peer_median_pb)) / 2.0
    ev_rel    = _rel_ratio(evebitda, peer_median_evebitda)
    return price_rel - ev_rel


def vvp_120_divyield_vs_pe_composite(
    divyield: pd.Series, peer_median_divyield: pd.Series,
    pe: pd.Series, peer_median_pe: pd.Series
) -> pd.Series:
    """Div yield relative ratio minus P/E relative ratio (yield richness vs price cheapness)."""
    return _rel_ratio(divyield, peer_median_divyield) - _rel_ratio(pe, peer_median_pe)


def vvp_121_cheap_on_all_5_flag(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """1 if ticker is cheaper than peers on all 5 multiples: PE/PB/PS/EVEBIT/EVEBITDA."""
    return (
        _discount_flag(pe, peer_median_pe) *
        _discount_flag(pb, peer_median_pb) *
        _discount_flag(ps, peer_median_ps) *
        _discount_flag(evebit, peer_median_evebit) *
        _discount_flag(evebitda, peer_median_evebitda)
    )


def vvp_122_discount_count_5metrics(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """Count of metrics (0-5) where ticker trades below peer median."""
    return (
        _discount_flag(pe, peer_median_pe) +
        _discount_flag(pb, peer_median_pb) +
        _discount_flag(ps, peer_median_ps) +
        _discount_flag(evebit, peer_median_evebit) +
        _discount_flag(evebitda, peer_median_evebitda)
    )


def vvp_123_avg_depth_3metrics(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """Average discount depth across PE/PB/PS relative ratios (mean cheapness below 1)."""
    r_pe = (_rel_ratio(pe, peer_median_pe) - 1.0).clip(upper=0.0)
    r_pb = (_rel_ratio(pb, peer_median_pb) - 1.0).clip(upper=0.0)
    r_ps = (_rel_ratio(ps, peer_median_ps) - 1.0).clip(upper=0.0)
    return (r_pe + r_pb + r_ps) / 3.0


def vvp_124_cross_multiple_dispersion(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """Std of PE/PB/EVEBITDA relative ratios cross-sectionally within the day."""
    r_pe  = _rel_ratio(pe, peer_median_pe)
    r_pb  = _rel_ratio(pb, peer_median_pb)
    r_evd = _rel_ratio(evebitda, peer_median_evebitda)
    mean  = (r_pe + r_pb + r_evd) / 3.0
    var   = ((r_pe - mean)**2 + (r_pb - mean)**2 + (r_evd - mean)**2) / 3.0
    return var.apply(lambda x: x**0.5 if pd.notna(x) and x >= 0 else np.nan)


def vvp_125_pe_pb_relative_agreement(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series
) -> pd.Series:
    """1 if both P/E and P/B are below peer median (agreement of two cheapness signals)."""
    return _discount_flag(pe, peer_median_pe) * _discount_flag(pb, peer_median_pb)


# --- Group O (126-135): Peer-adjusted valuation vs own history ---

def vvp_126_pe_rel_ratio_vs_own_252d_mean(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Current P/E relative ratio vs its 252-day own mean (is discount deeper than usual?)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r - _rolling_mean(r, _TD_YEAR)


def vvp_127_pb_rel_ratio_vs_own_252d_mean(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Current P/B relative ratio vs its 252-day own mean."""
    r = _rel_ratio(pb, peer_median_pb)
    return r - _rolling_mean(r, _TD_YEAR)


def vvp_128_ps_rel_ratio_vs_own_252d_mean(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Current P/S relative ratio vs its 252-day own mean."""
    r = _rel_ratio(ps, peer_median_ps)
    return r - _rolling_mean(r, _TD_YEAR)


def vvp_129_evebitda_rel_ratio_vs_own_252d_mean(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Current EV/EBITDA relative ratio vs its 252-day own mean."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r - _rolling_mean(r, _TD_YEAR)


def vvp_130_pe_rel_ratio_vs_own_504d_mean(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Current P/E relative ratio vs its 504-day mean (long-run vs peers divergence)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r - _rolling_mean(r, _TD_2Y)


def vvp_131_pe_rel_ratio_vs_own_expanding_mean(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """P/E relative ratio minus its all-time expanding mean (deviation from lifetime avg)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r - r.expanding(min_periods=21).mean()


def vvp_132_pb_rel_ratio_vs_own_expanding_mean(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """P/B relative ratio minus its all-time expanding mean."""
    r = _rel_ratio(pb, peer_median_pb)
    return r - r.expanding(min_periods=21).mean()


def vvp_133_log_pe_vs_own_252d_mean(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Log-relative P/E minus its 252-day rolling mean (log-level deviation)."""
    r = _log_rel(pe, peer_median_pe)
    return r - _rolling_mean(r, _TD_YEAR)


def vvp_134_evebit_rel_ratio_vs_own_252d_mean(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """EV/EBIT relative ratio vs its 252-day mean."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return r - _rolling_mean(r, _TD_YEAR)


def vvp_135_divyield_rel_vs_own_252d_mean(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """Div-yield relative ratio vs its 252-day mean (higher than usual yield advantage?)."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return r - _rolling_mean(r, _TD_YEAR)


# --- Group P (136-145): De-rating speed and peer-relative momentum ---

def vvp_136_pe_derate_speed_21d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """21-day pct change in P/E relative ratio (de-rating speed vs peers)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.pct_change(21)


def vvp_137_pb_derate_speed_21d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """21-day pct change in P/B relative ratio."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.pct_change(21)


def vvp_138_ps_derate_speed_63d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """63-day pct change in P/S relative ratio (quarterly de-rating speed vs peers)."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.pct_change(63)


def vvp_139_evebitda_derate_speed_63d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """63-day pct change in EV/EBITDA relative ratio."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r.pct_change(63)


def vvp_140_pe_derate_faster_than_peer(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """1 if P/E fell faster than peer median P/E over 21 days (de-rating faster than sector)."""
    pe_ret    = pe.pct_change(21)
    peer_ret  = peer_median_pe.pct_change(21)
    return (pe_ret < peer_ret).astype(float)


def vvp_141_pb_derate_faster_than_peer(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """1 if P/B fell faster than peer median P/B over 21 days."""
    pb_ret   = pb.pct_change(21)
    peer_ret = peer_median_pb.pct_change(21)
    return (pb_ret < peer_ret).astype(float)


def vvp_142_pe_derate_speed_vs_peer_21d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """21d pct-change of P/E minus 21d pct-change of peer-median P/E (excess de-rating)."""
    return pe.pct_change(21) - peer_median_pe.pct_change(21)


def vvp_143_pb_derate_speed_vs_peer_63d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """63d pct-change of P/B minus 63d pct-change of peer-median P/B."""
    return pb.pct_change(63) - peer_median_pb.pct_change(63)


def vvp_144_log_pe_momentum_63d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """63-day diff in log(P/E / peer) — log-momentum of relative valuation."""
    r = _log_rel(pe, peer_median_pe)
    return r.diff(63)


def vvp_145_log_pb_momentum_126d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """126-day diff in log(P/B / peer) — half-year log-momentum of relative valuation."""
    r = _log_rel(pb, peer_median_pb)
    return r.diff(126)


# --- Group Q (146-150): Long-run and composite de-rating persistence measures ---

def vvp_146_pe_rel_ratio_3y_pctrank(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of P/E relative ratio (3-year historical rank)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r.rolling(_TD_3Y, min_periods=_TD_HALF).rank(pct=True)


def vvp_147_log_pe_3y_zscore(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Z-score of log(P/E / peer) over 756-day window (3-year discount extremity)."""
    r = _log_rel(pe, peer_median_pe)
    return _zscore_rolling(r, _TD_3Y)


def vvp_148_pb_rel_ratio_3y_pctrank(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of P/B relative ratio."""
    r = _rel_ratio(pb, peer_median_pb)
    return r.rolling(_TD_3Y, min_periods=_TD_HALF).rank(pct=True)


def vvp_149_discount_persistence_score_252d(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series
) -> pd.Series:
    """Mean of 252-day below-peer fractions for PE/PB/PS (discount persistence composite)."""
    f_pe = _rolling_mean(_discount_flag(pe, peer_median_pe), _TD_YEAR)
    f_pb = _rolling_mean(_discount_flag(pb, peer_median_pb), _TD_YEAR)
    f_ps = _rolling_mean(_discount_flag(ps, peer_median_ps), _TD_YEAR)
    return (f_pe + f_pb + f_ps) / 3.0


def vvp_150_composite_derate_score(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """Composite de-rating score: mean of 63d excess de-rating for PE/PB/EVEBITDA vs peers."""
    dr_pe  = pe.pct_change(63)  - peer_median_pe.pct_change(63)
    dr_pb  = pb.pct_change(63)  - peer_median_pb.pct_change(63)
    dr_evd = evebitda.pct_change(63) - peer_median_evebitda.pct_change(63)
    return (dr_pe + dr_pb + dr_evd) / 3.0


# --- Group R2 (176-185): Long-window OLS slopes of relative ratios ---

def vvp_176_pe_rel_ratio_linslope_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """OLS slope of P/E relative ratio over 252-day window (annual trend of relative rating)."""
    return _linslope(_rel_ratio(pe, peer_median_pe), _TD_YEAR)


def vvp_177_ps_rel_ratio_linslope_252d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """OLS slope of P/S relative ratio over 252-day window."""
    return _linslope(_rel_ratio(ps, peer_median_ps), _TD_YEAR)


def vvp_178_evebit_rel_ratio_linslope_63d(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """OLS slope of EV/EBIT relative ratio over 63-day window."""
    return _linslope(_rel_ratio(evebit, peer_median_evebit), _TD_QTR)


def vvp_179_log_ps_linslope_63d(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """OLS slope of log(P/S/peer) over 63-day window."""
    return _linslope(_log_rel(ps, peer_median_ps), _TD_QTR)


def vvp_180_log_pe_linslope_252d(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """OLS slope of log(P/E/peer) over 252-day window."""
    return _linslope(_log_rel(pe, peer_median_pe), _TD_YEAR)


def vvp_181_log_pb_linslope_252d(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """OLS slope of log(P/B/peer) over 252-day window."""
    return _linslope(_log_rel(pb, peer_median_pb), _TD_YEAR)


def vvp_182_divyield_rel_ratio_linslope_63d(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """OLS slope of div-yield relative ratio over 63-day window."""
    return _linslope(_rel_ratio(divyield, peer_median_divyield), _TD_QTR)


def vvp_183_marketcap_rel_ratio_linslope_63d(marketcap: pd.Series, peer_median_marketcap: pd.Series) -> pd.Series:
    """OLS slope of market-cap relative ratio over 63-day window."""
    return _linslope(_rel_ratio(marketcap, peer_median_marketcap), _TD_QTR)


def vvp_184_evebitda_rel_ratio_linslope_252d(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """OLS slope of EV/EBITDA relative ratio over 252-day window."""
    return _linslope(_rel_ratio(evebitda, peer_median_evebitda), _TD_YEAR)


def vvp_185_log_evebit_linslope_252d(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """OLS slope of log(EV/EBIT/peer) over 252-day window."""
    return _linslope(_log_rel(evebit, peer_median_evebit), _TD_YEAR)


# --- Group S2 (186-193): Percentile rank over 3-year window for more metrics ---

def vvp_186_ps_rel_ratio_3y_pctrank(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of P/S relative ratio (3-year historical rank)."""
    r = _rel_ratio(ps, peer_median_ps)
    return r.rolling(_TD_3Y, min_periods=_TD_HALF).rank(pct=True)


def vvp_187_evebitda_rel_ratio_3y_pctrank(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of EV/EBITDA relative ratio."""
    r = _rel_ratio(evebitda, peer_median_evebitda)
    return r.rolling(_TD_3Y, min_periods=_TD_HALF).rank(pct=True)


def vvp_188_evebit_rel_ratio_3y_pctrank(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of EV/EBIT relative ratio."""
    r = _rel_ratio(evebit, peer_median_evebit)
    return r.rolling(_TD_3Y, min_periods=_TD_HALF).rank(pct=True)


def vvp_189_divyield_rel_ratio_3y_pctrank(divyield: pd.Series, peer_median_divyield: pd.Series) -> pd.Series:
    """756-day rolling percentile rank of div-yield relative ratio."""
    r = _rel_ratio(divyield, peer_median_divyield)
    return r.rolling(_TD_3Y, min_periods=_TD_HALF).rank(pct=True)


def vvp_190_log_pb_3y_zscore(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Z-score of log(P/B/peer) over 756-day window (3-year P/B discount extremity)."""
    return _zscore_rolling(_log_rel(pb, peer_median_pb), _TD_3Y)


def vvp_191_log_ps_3y_zscore(ps: pd.Series, peer_median_ps: pd.Series) -> pd.Series:
    """Z-score of log(P/S/peer) over 756-day window."""
    return _zscore_rolling(_log_rel(ps, peer_median_ps), _TD_3Y)


def vvp_192_evebitda_rel_ratio_3y_zscore(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Z-score of EV/EBITDA relative ratio over 756-day window."""
    return _zscore_rolling(_rel_ratio(evebitda, peer_median_evebitda), _TD_3Y)


def vvp_193_composite_pctrank_3y_5metric(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """Mean 3-year pct-rank across PE/PB/PS/EVEBIT/EVEBITDA relative ratios."""
    def _rank3y(s):
        return s.rolling(_TD_3Y, min_periods=_TD_HALF).rank(pct=True)
    return (
        _rank3y(_rel_ratio(pe, peer_median_pe)) +
        _rank3y(_rel_ratio(pb, peer_median_pb)) +
        _rank3y(_rel_ratio(ps, peer_median_ps)) +
        _rank3y(_rel_ratio(evebit, peer_median_evebit)) +
        _rank3y(_rel_ratio(evebitda, peer_median_evebitda))
    ) / 5.0


# --- Group T2 (194-200): Discount depth, drawdown and floor for more metrics ---

def vvp_194_evebit_discount_depth(evebit: pd.Series, peer_median_evebit: pd.Series) -> pd.Series:
    """Depth of EV/EBIT discount: (own - peer) / |peer|, clipped to <=0."""
    depth = _safe_div(evebit - peer_median_evebit, peer_median_evebit.abs())
    return depth.clip(upper=0.0)


def vvp_195_evebitda_discount_depth(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Depth of EV/EBITDA discount: (own - peer) / |peer|, clipped to <=0."""
    depth = _safe_div(evebitda - peer_median_evebitda, peer_median_evebitda.abs())
    return depth.clip(upper=0.0)


def vvp_196_pb_rel_ratio_ath_drawdown(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Drawdown of P/B relative ratio from expanding ATH (how much relative discount deepened)."""
    r    = _rel_ratio(pb, peer_median_pb)
    peak = r.expanding(min_periods=1).max()
    return _safe_div(r - peak, peak.abs())


def vvp_197_pe_rel_ratio_distance_from_504d_min(pe: pd.Series, peer_median_pe: pd.Series) -> pd.Series:
    """Distance of P/E relative ratio above its 504-day min (how far above 2-year floor)."""
    r = _rel_ratio(pe, peer_median_pe)
    return r - _rolling_min(r, _TD_2Y)


def vvp_198_pb_rel_ratio_distance_from_252d_min(pb: pd.Series, peer_median_pb: pd.Series) -> pd.Series:
    """Distance of P/B relative ratio above its 252-day min (how far above 1-year floor)."""
    r = _rel_ratio(pb, peer_median_pb)
    return r - _rolling_min(r, _TD_YEAR)


def vvp_199_evebitda_rel_ratio_ath_drawdown(evebitda: pd.Series, peer_median_evebitda: pd.Series) -> pd.Series:
    """Drawdown of EV/EBITDA relative ratio from expanding ATH."""
    r    = _rel_ratio(evebitda, peer_median_evebitda)
    peak = r.expanding(min_periods=1).max()
    return _safe_div(r - peak, peak.abs())


def vvp_200_avg_discount_depth_5metrics(
    pe: pd.Series, peer_median_pe: pd.Series,
    pb: pd.Series, peer_median_pb: pd.Series,
    ps: pd.Series, peer_median_ps: pd.Series,
    evebit: pd.Series, peer_median_evebit: pd.Series,
    evebitda: pd.Series, peer_median_evebitda: pd.Series
) -> pd.Series:
    """Mean discount depth (clipped at 0) across all 5 multiples — composite cheapness depth."""
    def _depth(own, peer):
        return _safe_div(own - peer, peer.abs()).clip(upper=0.0)
    return (
        _depth(pe, peer_median_pe) +
        _depth(pb, peer_median_pb) +
        _depth(ps, peer_median_ps) +
        _depth(evebit, peer_median_evebit) +
        _depth(evebitda, peer_median_evebitda)
    ) / 5.0


# ── Registry ──────────────────────────────────────────────────────────────────

VALUATION_VS_PEERS_REGISTRY_076_150 = {
    "vvp_076_pe_rel_ratio_5d_diff":                  {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_076_pe_rel_ratio_5d_diff},
    "vvp_077_pb_rel_ratio_21d_diff":                  {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_077_pb_rel_ratio_21d_diff},
    "vvp_078_ps_rel_ratio_63d_diff":                  {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_078_ps_rel_ratio_63d_diff},
    "vvp_079_evebitda_rel_ratio_21d_diff":            {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_079_evebitda_rel_ratio_21d_diff},
    "vvp_080_log_pe_5d_diff":                         {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_080_log_pe_5d_diff},
    "vvp_081_log_pb_21d_diff":                        {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_081_log_pb_21d_diff},
    "vvp_082_pe_rel_ratio_linslope_63d":              {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_082_pe_rel_ratio_linslope_63d},
    "vvp_083_pb_rel_ratio_linslope_252d":             {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_083_pb_rel_ratio_linslope_252d},
    "vvp_084_ps_rel_ratio_linslope_63d":              {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_084_ps_rel_ratio_linslope_63d},
    "vvp_085_log_evebitda_linslope_63d":              {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_085_log_evebitda_linslope_63d},
    "vvp_086_pe_rel_ratio_ewm21":                     {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_086_pe_rel_ratio_ewm21},
    "vvp_087_pb_rel_ratio_ewm63":                     {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_087_pb_rel_ratio_ewm63},
    "vvp_088_ps_rel_ratio_ewm63":                     {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_088_ps_rel_ratio_ewm63},
    "vvp_089_log_pe_ewm21":                           {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_089_log_pe_ewm21},
    "vvp_090_evebitda_rel_ratio_ewm21":               {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_090_evebitda_rel_ratio_ewm21},
    "vvp_091_log_pb_ewm63":                           {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_091_log_pb_ewm63},
    "vvp_092_divyield_rel_ratio_ewm21":               {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_092_divyield_rel_ratio_ewm21},
    "vvp_093_pe_ewm_vs_rolling_gap":                  {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_093_pe_ewm_vs_rolling_gap},
    "vvp_094_log_ps_ewm21":                           {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_094_log_ps_ewm21},
    "vvp_095_evebit_rel_ratio_ewm63":                 {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_095_evebit_rel_ratio_ewm63},
    "vvp_096_pe_discount_streak":                     {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_096_pe_discount_streak},
    "vvp_097_pb_discount_streak":                     {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_097_pb_discount_streak},
    "vvp_098_ps_discount_streak":                     {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_098_ps_discount_streak},
    "vvp_099_evebitda_discount_streak":               {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_099_evebitda_discount_streak},
    "vvp_100_pe_sign_change_rate_63d":                {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_100_pe_sign_change_rate_63d},
    "vvp_101_pb_sign_change_rate_63d":                {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_101_pb_sign_change_rate_63d},
    "vvp_102_log_pe_sign_63d":                        {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_102_log_pe_sign_63d},
    "vvp_103_pe_discount_streak_norm_252d":           {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_103_pe_discount_streak_norm_252d},
    "vvp_104_multi_metric_discount_streak":           {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                    "func": vvp_104_multi_metric_discount_streak},
    "vvp_105_divyield_above_peer_streak":             {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_105_divyield_above_peer_streak},
    "vvp_106_pe_rel_ratio_std_63d":                   {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_106_pe_rel_ratio_std_63d},
    "vvp_107_pb_rel_ratio_std_252d":                  {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_107_pb_rel_ratio_std_252d},
    "vvp_108_log_pe_std_252d":                        {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_108_log_pe_std_252d},
    "vvp_109_ps_rel_ratio_range_252d":                {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_109_ps_rel_ratio_range_252d},
    "vvp_110_evebitda_rel_ratio_std_63d":             {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_110_evebitda_rel_ratio_std_63d},
    "vvp_111_pe_rel_ratio_cv_252d":                   {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_111_pe_rel_ratio_cv_252d},
    "vvp_112_log_pb_std_63d":                         {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_112_log_pb_std_63d},
    "vvp_113_pe_rel_ratio_range_63d":                 {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_113_pe_rel_ratio_range_63d},
    "vvp_114_divyield_rel_ratio_std_252d":            {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_114_divyield_rel_ratio_std_252d},
    "vvp_115_evebit_rel_ratio_std_252d":              {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_115_evebit_rel_ratio_std_252d},
    "vvp_116_price_multiples_avg_rel_ratio":          {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                    "func": vvp_116_price_multiples_avg_rel_ratio},
    "vvp_117_ev_multiples_avg_rel_ratio":             {"inputs": ["evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"],                                                        "func": vvp_117_ev_multiples_avg_rel_ratio},
    "vvp_118_all_multiples_avg_log_rel":              {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebitda", "peer_median_evebitda"],               "func": vvp_118_all_multiples_avg_log_rel},
    "vvp_119_price_minus_ev_composite_rel":           {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "evebitda", "peer_median_evebitda"],                                        "func": vvp_119_price_minus_ev_composite_rel},
    "vvp_120_divyield_vs_pe_composite":               {"inputs": ["divyield", "peer_median_divyield", "pe", "peer_median_pe"],                                                                "func": vvp_120_divyield_vs_pe_composite},
    "vvp_121_cheap_on_all_5_flag":                    {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"], "func": vvp_121_cheap_on_all_5_flag},
    "vvp_122_discount_count_5metrics":                {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"], "func": vvp_122_discount_count_5metrics},
    "vvp_123_avg_depth_3metrics":                     {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                    "func": vvp_123_avg_depth_3metrics},
    "vvp_124_cross_multiple_dispersion":              {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "evebitda", "peer_median_evebitda"],                                        "func": vvp_124_cross_multiple_dispersion},
    "vvp_125_pe_pb_relative_agreement":               {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb"],                                                                            "func": vvp_125_pe_pb_relative_agreement},
    "vvp_126_pe_rel_ratio_vs_own_252d_mean":          {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_126_pe_rel_ratio_vs_own_252d_mean},
    "vvp_127_pb_rel_ratio_vs_own_252d_mean":          {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_127_pb_rel_ratio_vs_own_252d_mean},
    "vvp_128_ps_rel_ratio_vs_own_252d_mean":          {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_128_ps_rel_ratio_vs_own_252d_mean},
    "vvp_129_evebitda_rel_ratio_vs_own_252d_mean":    {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_129_evebitda_rel_ratio_vs_own_252d_mean},
    "vvp_130_pe_rel_ratio_vs_own_504d_mean":          {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_130_pe_rel_ratio_vs_own_504d_mean},
    "vvp_131_pe_rel_ratio_vs_own_expanding_mean":     {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_131_pe_rel_ratio_vs_own_expanding_mean},
    "vvp_132_pb_rel_ratio_vs_own_expanding_mean":     {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_132_pb_rel_ratio_vs_own_expanding_mean},
    "vvp_133_log_pe_vs_own_252d_mean":                {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_133_log_pe_vs_own_252d_mean},
    "vvp_134_evebit_rel_ratio_vs_own_252d_mean":      {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_134_evebit_rel_ratio_vs_own_252d_mean},
    "vvp_135_divyield_rel_vs_own_252d_mean":          {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_135_divyield_rel_vs_own_252d_mean},
    "vvp_136_pe_derate_speed_21d":                    {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_136_pe_derate_speed_21d},
    "vvp_137_pb_derate_speed_21d":                    {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_137_pb_derate_speed_21d},
    "vvp_138_ps_derate_speed_63d":                    {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_138_ps_derate_speed_63d},
    "vvp_139_evebitda_derate_speed_63d":              {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_139_evebitda_derate_speed_63d},
    "vvp_140_pe_derate_faster_than_peer":             {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_140_pe_derate_faster_than_peer},
    "vvp_141_pb_derate_faster_than_peer":             {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_141_pb_derate_faster_than_peer},
    "vvp_142_pe_derate_speed_vs_peer_21d":            {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_142_pe_derate_speed_vs_peer_21d},
    "vvp_143_pb_derate_speed_vs_peer_63d":            {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_143_pb_derate_speed_vs_peer_63d},
    "vvp_144_log_pe_momentum_63d":                    {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_144_log_pe_momentum_63d},
    "vvp_145_log_pb_momentum_126d":                   {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_145_log_pb_momentum_126d},
    "vvp_146_pe_rel_ratio_3y_pctrank":                {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_146_pe_rel_ratio_3y_pctrank},
    "vvp_147_log_pe_3y_zscore":                       {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_147_log_pe_3y_zscore},
    "vvp_148_pb_rel_ratio_3y_pctrank":                {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_148_pb_rel_ratio_3y_pctrank},
    "vvp_149_discount_persistence_score_252d":        {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps"],                                                    "func": vvp_149_discount_persistence_score_252d},
    "vvp_150_composite_derate_score":                 {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "evebitda", "peer_median_evebitda"],                                        "func": vvp_150_composite_derate_score},
    "vvp_176_pe_rel_ratio_linslope_252d":             {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_176_pe_rel_ratio_linslope_252d},
    "vvp_177_ps_rel_ratio_linslope_252d":             {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_177_ps_rel_ratio_linslope_252d},
    "vvp_178_evebit_rel_ratio_linslope_63d":          {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_178_evebit_rel_ratio_linslope_63d},
    "vvp_179_log_ps_linslope_63d":                    {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_179_log_ps_linslope_63d},
    "vvp_180_log_pe_linslope_252d":                   {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_180_log_pe_linslope_252d},
    "vvp_181_log_pb_linslope_252d":                   {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_181_log_pb_linslope_252d},
    "vvp_182_divyield_rel_ratio_linslope_63d":        {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_182_divyield_rel_ratio_linslope_63d},
    "vvp_183_marketcap_rel_ratio_linslope_63d":       {"inputs": ["marketcap", "peer_median_marketcap"],                                                                                      "func": vvp_183_marketcap_rel_ratio_linslope_63d},
    "vvp_184_evebitda_rel_ratio_linslope_252d":       {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_184_evebitda_rel_ratio_linslope_252d},
    "vvp_185_log_evebit_linslope_252d":               {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_185_log_evebit_linslope_252d},
    "vvp_186_ps_rel_ratio_3y_pctrank":                {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_186_ps_rel_ratio_3y_pctrank},
    "vvp_187_evebitda_rel_ratio_3y_pctrank":          {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_187_evebitda_rel_ratio_3y_pctrank},
    "vvp_188_evebit_rel_ratio_3y_pctrank":            {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_188_evebit_rel_ratio_3y_pctrank},
    "vvp_189_divyield_rel_ratio_3y_pctrank":          {"inputs": ["divyield", "peer_median_divyield"],                                                                                        "func": vvp_189_divyield_rel_ratio_3y_pctrank},
    "vvp_190_log_pb_3y_zscore":                       {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_190_log_pb_3y_zscore},
    "vvp_191_log_ps_3y_zscore":                       {"inputs": ["ps", "peer_median_ps"],                                                                                                    "func": vvp_191_log_ps_3y_zscore},
    "vvp_192_evebitda_rel_ratio_3y_zscore":           {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_192_evebitda_rel_ratio_3y_zscore},
    "vvp_193_composite_pctrank_3y_5metric":           {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"], "func": vvp_193_composite_pctrank_3y_5metric},
    "vvp_194_evebit_discount_depth":                  {"inputs": ["evebit", "peer_median_evebit"],                                                                                            "func": vvp_194_evebit_discount_depth},
    "vvp_195_evebitda_discount_depth":                {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_195_evebitda_discount_depth},
    "vvp_196_pb_rel_ratio_ath_drawdown":              {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_196_pb_rel_ratio_ath_drawdown},
    "vvp_197_pe_rel_ratio_distance_from_504d_min":    {"inputs": ["pe", "peer_median_pe"],                                                                                                    "func": vvp_197_pe_rel_ratio_distance_from_504d_min},
    "vvp_198_pb_rel_ratio_distance_from_252d_min":    {"inputs": ["pb", "peer_median_pb"],                                                                                                    "func": vvp_198_pb_rel_ratio_distance_from_252d_min},
    "vvp_199_evebitda_rel_ratio_ath_drawdown":        {"inputs": ["evebitda", "peer_median_evebitda"],                                                                                        "func": vvp_199_evebitda_rel_ratio_ath_drawdown},
    "vvp_200_avg_discount_depth_5metrics":            {"inputs": ["pe", "peer_median_pe", "pb", "peer_median_pb", "ps", "peer_median_ps", "evebit", "peer_median_evebit", "evebitda", "peer_median_evebitda"], "func": vvp_200_avg_discount_depth_5metrics},
}
