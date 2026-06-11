"""
63_cash_burn — Base Features 076-150
Domain: negative free cash flow, operating cash burn, cash runway depletion
Asset class: US equities | Sharadar SF1 fundamentals (FUNDAMENTAL folder)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly cadence on daily index:
  1 quarter = 63 trading days, 1 year = 252 td.
  QoQ change = .diff(63) or .shift(63); YoY = 252.
  Forward-filled quarterly data steps 4x/year — expected and correct.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_2YR  = 504
_TD_3YR  = 756
_TD_5YR  = 1260
_EPS     = 1e-9

# ── Alignment helper ──────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: All inputs to feature functions in this file are daily-frequency
    Series, forward-filled from the most recent quarterly Sharadar SF1 report
    known as of each date.  Functions look strictly backward.

    This helper re-aligns a quarterly Series onto a daily trading-day index
    using forward-fill, replicating what the pipeline already does upstream.
    It is provided for completeness; feature functions receive already-aligned
    daily Series and do NOT need to call this internally.
    """
    return q_series.reindex(daily_index).ffill()


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


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 2)).median()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 2)).mean()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    """Rolling OLS slope over w periods."""
    def _slope(x):
        n = len(x)
        if n < 2:
            return np.nan
        xi = np.arange(n, dtype=float)
        xi_m = xi.mean()
        x_m  = x.mean()
        num  = ((xi - xi_m) * (x - x_m)).sum()
        den  = ((xi - xi_m) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 2)).apply(_slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group G (076-090): Multi-year FCF trend and worsening signals ---

def cbr_076_fcf_3yr_rolling_sum(fcf: pd.Series) -> pd.Series:
    """Trailing 3-year (756 td) sum of FCF — long-term cumulative burn."""
    return _rolling_sum(fcf, _TD_3YR)


def cbr_077_fcf_5yr_rolling_sum(fcf: pd.Series) -> pd.Series:
    """Trailing 5-year (1260 td) sum of FCF — very long-term cumulative burn."""
    return _rolling_sum(fcf, _TD_5YR)


def cbr_078_fcf_2yr_change(fcf: pd.Series) -> pd.Series:
    """2-year change in FCF (504 td diff) — medium-term deterioration."""
    return fcf.diff(_TD_2YR)


def cbr_079_fcf_3yr_change(fcf: pd.Series) -> pd.Series:
    """3-year change in FCF (756 td diff)."""
    return fcf.diff(_TD_3YR)


def cbr_080_fcf_trend_slope_8q(fcf: pd.Series) -> pd.Series:
    """OLS slope of FCF over trailing 8 quarters (504 td)."""
    return _linslope(fcf, _TD_2YR)


def cbr_081_ncfo_trend_slope_4q(ncfo: pd.Series) -> pd.Series:
    """OLS slope of NCFO over trailing 4 quarters (252 td)."""
    return _linslope(ncfo, _TD_YEAR)


def cbr_082_ncfo_trend_slope_8q(ncfo: pd.Series) -> pd.Series:
    """OLS slope of NCFO over trailing 8 quarters (504 td)."""
    return _linslope(ncfo, _TD_2YR)


def cbr_083_fcf_min_4q(fcf: pd.Series) -> pd.Series:
    """Minimum FCF over trailing 4 quarters — worst single quarter burn."""
    return _rolling_min(fcf, _TD_YEAR)


def cbr_084_fcf_min_8q(fcf: pd.Series) -> pd.Series:
    """Minimum FCF over trailing 8 quarters."""
    return _rolling_min(fcf, _TD_2YR)


def cbr_085_fcf_min_12q(fcf: pd.Series) -> pd.Series:
    """Minimum FCF over trailing 12 quarters (3 years)."""
    return _rolling_min(fcf, _TD_3YR)


def cbr_086_fcf_vs_4q_mean(fcf: pd.Series) -> pd.Series:
    """Current FCF minus 4-quarter mean (deviation from recent trend)."""
    return fcf - _rolling_mean(fcf, _TD_YEAR)


def cbr_087_fcf_vs_8q_mean(fcf: pd.Series) -> pd.Series:
    """Current FCF minus 8-quarter mean."""
    return fcf - _rolling_mean(fcf, _TD_2YR)


def cbr_088_fcf_at_4q_low_flag(fcf: pd.Series) -> pd.Series:
    """1 if current FCF is at its 4-quarter minimum (fresh trough)."""
    return (fcf == _rolling_min(fcf, _TD_YEAR)).astype(float)


def cbr_089_fcf_at_8q_low_flag(fcf: pd.Series) -> pd.Series:
    """1 if current FCF is at its 8-quarter minimum."""
    return (fcf == _rolling_min(fcf, _TD_2YR)).astype(float)


def cbr_090_ncfo_4q_pct_rank(ncfo: pd.Series) -> pd.Series:
    """Percentile rank of NCFO within trailing 4-quarter window."""
    return ncfo.rolling(_TD_YEAR, min_periods=_TD_QTR).rank(pct=True)


# --- Group H (091-105): Cash balance persistence and trend ---

def cbr_091_cashnequiv_trend_slope_4q(cashnequiv: pd.Series) -> pd.Series:
    """OLS slope of cash balance over trailing 4 quarters."""
    return _linslope(cashnequiv, _TD_YEAR)


def cbr_092_cashnequiv_trend_slope_8q(cashnequiv: pd.Series) -> pd.Series:
    """OLS slope of cash balance over trailing 8 quarters."""
    return _linslope(cashnequiv, _TD_2YR)


def cbr_093_cashnequiv_min_4q(cashnequiv: pd.Series) -> pd.Series:
    """Minimum cash balance over trailing 4 quarters."""
    return _rolling_min(cashnequiv, _TD_YEAR)


def cbr_094_cashnequiv_min_8q(cashnequiv: pd.Series) -> pd.Series:
    """Minimum cash balance over trailing 8 quarters."""
    return _rolling_min(cashnequiv, _TD_2YR)


def cbr_095_cashnequiv_declining_4q_flag(cashnequiv: pd.Series) -> pd.Series:
    """1 if cash balance is lower than it was 4 quarters ago."""
    return (cashnequiv < cashnequiv.shift(_TD_YEAR)).astype(float)


def cbr_096_cashnequiv_declining_8q_flag(cashnequiv: pd.Series) -> pd.Series:
    """1 if cash balance is lower than it was 8 quarters ago."""
    return (cashnequiv < cashnequiv.shift(_TD_2YR)).astype(float)


def cbr_097_cashnequiv_pct_rank_8q(cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of cash balance within trailing 8-quarter window."""
    return cashnequiv.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)


def cbr_098_cashnequiv_vs_4q_mean(cashnequiv: pd.Series) -> pd.Series:
    """Cash balance deviation from 4-quarter mean (below mean = deteriorating)."""
    return cashnequiv - _rolling_mean(cashnequiv, _TD_YEAR)


def cbr_099_cashnequiv_cv_4q(cashnequiv: pd.Series) -> pd.Series:
    """Coefficient of variation of cash balance over 4 quarters (instability)."""
    return _safe_div(_rolling_std(cashnequiv, _TD_YEAR), _rolling_mean(cashnequiv, _TD_YEAR).abs())


def cbr_100_cashnequiv_3yr_change(cashnequiv: pd.Series) -> pd.Series:
    """3-year change in cash balance (long-term depletion)."""
    return cashnequiv.diff(_TD_3YR)


def cbr_101_cashnequiv_drawdown_from_3yr_peak(cashnequiv: pd.Series) -> pd.Series:
    """Cash drawdown from 3-year peak cash balance."""
    peak = _rolling_max(cashnequiv, _TD_3YR)
    return _safe_div(cashnequiv - peak, peak.abs())


def cbr_102_cash_depletion_speed_8q(cashnequiv: pd.Series) -> pd.Series:
    """Annualized cash depletion speed over 8 quarters: % decline per year."""
    delta = cashnequiv.diff(_TD_2YR)
    return _safe_div(-delta / 2.0, cashnequiv.shift(_TD_2YR).abs())


def cbr_103_cashnequiv_negative_flag(cashnequiv: pd.Series) -> pd.Series:
    """1 if cash balance is negative (technically insolvent cash position)."""
    return (cashnequiv < 0).astype(float)


def cbr_104_cashnequiv_below_1q_burn_flag(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 if cash < 1 quarter of burn (imminent liquidity crisis)."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    ratio = _safe_div(cashnequiv, burn)
    return (ratio < 1.0).astype(float)


def cbr_105_cash_coverage_ncfo_4q(cashnequiv: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Cash balance / |4q sum of NCFO| where NCFO < 0 (cash coverage of ops)."""
    ncfo4q = _rolling_sum(ncfo, _TD_YEAR)
    burn   = (-ncfo4q).where(ncfo4q < 0, other=np.nan)
    return _safe_div(cashnequiv, burn)


# --- Group I (106-118): Operating cash flow vs capex distress ---

def cbr_106_ncfo_below_capex_flag(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """1 if NCFO < |capex| (operating cash insufficient to fund investment)."""
    return (ncfo < capex.abs()).astype(float)


def cbr_107_ncfo_capex_deficit(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """Magnitude of NCFO shortfall vs capex: max(0, |capex| - NCFO)."""
    return (capex.abs() - ncfo).clip(lower=0)


def cbr_108_capex_pct_of_ncfo(capex: pd.Series, ncfo: pd.Series) -> pd.Series:
    """|capex| as percent of NCFO (>100% = NCFO doesn't cover investment)."""
    return _safe_div(capex.abs(), ncfo.abs())


def cbr_109_ncfo_to_capex_ratio_pct_rank_8q(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """Percentile rank of NCFO/|capex| coverage ratio within trailing 8-quarter window.
    Low rank signals operating cash coverage of capex is at a multi-year low."""
    ratio = _safe_div(ncfo, capex.abs())
    return ratio.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 2)).rank(pct=True)


def cbr_110_ncfo_to_capex_ratio_yoy_change(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """YoY change in NCFO/|capex| coverage ratio."""
    ratio = _safe_div(ncfo, capex.abs())
    return ratio.diff(_TD_YEAR)


def cbr_111_capex_rising_while_burning_flag(capex: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 if capex rising QoQ while FCF is negative (double distress)."""
    capex_rising = (capex.abs() > capex.abs().shift(_TD_QTR)).astype(float)
    burning      = (fcf < 0).astype(float)
    return capex_rising * burning


def cbr_112_fcf_ex_capex_trend(ncfo: pd.Series, capex: pd.Series) -> pd.Series:
    """OLS slope of (NCFO - |capex|) over 4 quarters — FCF trend direction."""
    fcf_proxy = ncfo - capex.abs()
    return _linslope(fcf_proxy, _TD_YEAR)


def cbr_113_capex_intensity_4q_mean(capex: pd.Series, revenue: pd.Series) -> pd.Series:
    """4-quarter mean of capex/revenue ratio (capex intensity persistence)."""
    ratio = _safe_div(capex.abs(), revenue)
    return _rolling_mean(ratio, _TD_YEAR)


def cbr_114_capex_trend_slope_4q(capex: pd.Series) -> pd.Series:
    """OLS slope of capex over 4 quarters (growing capex accelerates burn)."""
    return _linslope(capex.abs(), _TD_YEAR)


def cbr_115_depamor_to_capex_ratio(depamor: pd.Series, capex: pd.Series) -> pd.Series:
    """D&A / |capex|: < 1 means company is investing more than depreciating."""
    return _safe_div(depamor, capex.abs())


def cbr_116_maintenance_capex_proxy(depamor: pd.Series, capex: pd.Series) -> pd.Series:
    """Growth capex proxy: |capex| - D&A (excess of capex over maintenance)."""
    return (capex.abs() - depamor).clip(lower=0)


def cbr_117_ncfo_less_maintenance_capex(ncfo: pd.Series, depamor: pd.Series) -> pd.Series:
    """Maintenance FCF: NCFO - D&A (owner earnings proxy)."""
    return ncfo - depamor


def cbr_118_true_burn_rate(ncfo: pd.Series, capex: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """True burn rate: NCFO - |capex| - SBC (cash burn ex non-cash comp)."""
    return ncfo - capex.abs() - sbcomp.abs()


# --- Group J (119-130): SBC-adjusted and debt-funded burn signals ---

def cbr_119_sbcomp_to_ncfo_ratio(sbcomp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """SBC / |NCFO|: how much of reported operating cash is SBC non-cash add-back."""
    return _safe_div(sbcomp.abs(), ncfo.abs())


def cbr_120_sbcomp_4q_sum(sbcomp: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of SBC (dilutive cash-burn proxy)."""
    return _rolling_sum(sbcomp, _TD_YEAR)


def cbr_121_sbcomp_adjusted_ncfo(ncfo: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """NCFO adjusted for SBC: NCFO - SBC (cash burn stripping non-cash comp)."""
    return ncfo - sbcomp.abs()


def cbr_122_sbcomp_qoq_change(sbcomp: pd.Series) -> pd.Series:
    """QoQ change in SBC (rising SBC = rising hidden dilutive cost)."""
    return sbcomp.diff(_TD_QTR)


def cbr_123_sbcomp_yoy_change(sbcomp: pd.Series) -> pd.Series:
    """YoY change in SBC."""
    return sbcomp.diff(_TD_YEAR)


def cbr_124_debt_funded_burn_flag(ncf: pd.Series, ncff: pd.Series, fcf: pd.Series) -> pd.Series:
    """1 if FCF negative AND financing cash flow positive (borrowing to fund burn)."""
    return ((fcf < 0) & (ncff > 0)).astype(float)


def cbr_125_ncff_level(ncff: pd.Series) -> pd.Series:
    """Net cash from financing — positive = net borrowing or equity issuance."""
    return ncff.copy()


def cbr_126_ncff_4q_sum(ncff: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of financing cash flows."""
    return _rolling_sum(ncff, _TD_YEAR)


def cbr_127_ncfi_level(ncfi: pd.Series) -> pd.Series:
    """Net cash from investing activities (typically negative = investing)."""
    return ncfi.copy()


def cbr_128_ncfi_4q_sum(ncfi: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of investing cash flows."""
    return _rolling_sum(ncfi, _TD_YEAR)


def cbr_129_ops_burn_not_covered_by_financing(ncfo: pd.Series, ncff: pd.Series) -> pd.Series:
    """NCFO + NCFF: residual after financing; negative = neither ops nor financing covers."""
    return ncfo + ncff


def cbr_130_total_cash_activities_4q(ncfo: pd.Series, ncfi: pd.Series, ncff: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of (NCFO + NCFI + NCFF) = total cash generation."""
    total = ncfo + ncfi + ncff
    return _rolling_sum(total, _TD_YEAR)


# --- Group K (131-143): Advanced runway, distress scoring, z-scores ---

def cbr_131_runway_under_4q_flag(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """Acute-distress state flag: estimated cash runway is under 4 quarters."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    runway = _safe_div(cashnequiv, burn)
    runway[runway < 0] = np.nan
    return (runway < 4.0).astype(float)


def cbr_132_runway_pct_rank_8q(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """Percentile rank of runway within trailing 8-quarter window."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    runway = _safe_div(cashnequiv, burn)
    runway[runway < 0] = np.nan
    return runway.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)


def cbr_133_burn_intensity_zscore_4q(fcf: pd.Series) -> pd.Series:
    """Z-score of FCF over trailing 4 quarters (how extreme is current burn)."""
    return _zscore_rolling(fcf, _TD_YEAR)


def cbr_134_cash_draw_zscore_8q(cashnequiv: pd.Series) -> pd.Series:
    """Z-score of cash balance over trailing 8 quarters (how depleted is cash)."""
    return _zscore_rolling(cashnequiv, _TD_2YR)


def cbr_135_fcf_ewm_3q(fcf: pd.Series) -> pd.Series:
    """Exponentially-weighted mean of FCF over ~3-quarter span."""
    return _ewm_mean(fcf, 3 * _TD_QTR)


def cbr_136_ncfo_ewm_3q(ncfo: pd.Series) -> pd.Series:
    """Exponentially-weighted mean of NCFO over ~3-quarter span."""
    return _ewm_mean(ncfo, 3 * _TD_QTR)


def cbr_137_fcf_ewm_trend(fcf: pd.Series) -> pd.Series:
    """Difference between EWM(1q) and EWM(4q) of FCF — short vs long burn trend."""
    fast = _ewm_mean(fcf, _TD_QTR)
    slow = _ewm_mean(fcf, _TD_YEAR)
    return fast - slow


def cbr_138_burn_regime_score(fcf: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Composite regime score: (negative fcf rank) * (low cash rank).
    Both in 0-1 scale; product near 1 = worst regime."""
    fcf_neg_rank = 1.0 - fcf.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    low_cash_rank = 1.0 - cashnequiv.rolling(_TD_2YR, min_periods=_TD_QTR).rank(pct=True)
    return fcf_neg_rank * low_cash_rank


def cbr_139_cash_burn_days_remaining(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """Estimated cash burn in trading days: runway_quarters * 63."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    runway_q = _safe_div(cashnequiv, burn)
    runway_q[runway_q < 0] = np.nan
    return runway_q * _TD_QTR


def cbr_140_cashnequiv_to_debt_ratio(cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """Cash / total debt — net cash position proxy (low = debt-stressed)."""
    return _safe_div(cashnequiv, debt)


def cbr_141_cash_net_of_debt(cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """Net cash: cashnequiv - debt (negative = net debt)."""
    return cashnequiv - debt


def cbr_142_debt_funded_burn_scale(ncff: pd.Series, fcf: pd.Series) -> pd.Series:
    """NCFF / |FCF| when FCF < 0: how much of the burn is debt-funded.
    >1 = borrowing more than burning (aggressive leverage-funded growth)."""
    burn = (-fcf).where(fcf < 0, other=np.nan)
    ratio = _safe_div(ncff, burn)
    return ratio


def cbr_143_opex_to_ncfo_ratio(opex: pd.Series, ncfo: pd.Series) -> pd.Series:
    """|opex| / |NCFO|: operating cost per unit of operating cash (efficiency)."""
    return _safe_div(opex.abs(), ncfo.abs())


# --- Group L (144-150): Persistence, breadth, composite final features ---

def cbr_144_all_cf_negative_8q_frac(fcf: pd.Series, ncfo: pd.Series, ncf: pd.Series) -> pd.Series:
    """Fraction of trailing 8q window where FCF, NCFO, and NCF all negative simultaneously."""
    all_neg = ((fcf < 0) & (ncfo < 0) & (ncf < 0)).astype(float)
    return _rolling_mean(all_neg, _TD_2YR)


def cbr_145_cash_burn_persistence_score(fcf: pd.Series) -> pd.Series:
    """Weighted persistence: 4q neg-frac * |4q avg FCF| normalized by 8q std."""
    neg_frac = _rolling_mean((fcf < 0).astype(float), _TD_YEAR)
    avg_burn = -_rolling_mean(fcf, _TD_YEAR)
    std8q    = _rolling_std(fcf, _TD_2YR)
    return neg_frac * _safe_div(avg_burn, std8q.abs())


def cbr_146_fcf_worst_quarter_ratio(fcf: pd.Series) -> pd.Series:
    """Worst single quarter FCF / 4q average FCF (tail severity vs average burn)."""
    worst = _rolling_min(fcf, _TD_YEAR)
    avg   = _rolling_mean(fcf, _TD_YEAR)
    return _safe_div(worst, avg.abs())


def cbr_147_cash_vs_burn_momentum(cashnequiv: pd.Series, fcf: pd.Series) -> pd.Series:
    """QoQ change in (cash_balance / trailing_4q_burn) — runway momentum."""
    burn4q = (-_rolling_sum(fcf, _TD_YEAR)).where(
        _rolling_sum(fcf, _TD_YEAR) < 0, other=np.nan
    )
    ratio = _safe_div(cashnequiv, burn4q)
    return ratio.diff(_TD_QTR)


def cbr_148_ncfo_below_opex_flag(ncfo: pd.Series, opex: pd.Series) -> pd.Series:
    """1 if NCFO < |opex| * 0.5 — operating cash severely lagging operating costs."""
    return (ncfo < opex.abs() * 0.5).astype(float)


def cbr_149_multi_signal_burn_count(fcf: pd.Series, ncfo: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Count of distress signals: [FCF<0] + [NCFO<0] + [cash declining YoY].
    Range 0-3; 3 = maximum concurrent distress."""
    s1 = (fcf < 0).astype(float)
    s2 = (ncfo < 0).astype(float)
    s3 = (cashnequiv < cashnequiv.shift(_TD_YEAR)).astype(float)
    return s1 + s2 + s3


def cbr_150_cash_burn_severity_index(fcf: pd.Series, cashnequiv: pd.Series,
                                      ncfo: pd.Series, revenue: pd.Series) -> pd.Series:
    """Aggregate severity index: equal-weighted combination of 4 normalized signals.
    (1) FCF margin rank (inverted), (2) cash drawdown from 2yr peak,
    (3) NCFO margin rank (inverted), (4) cash-to-revenue rank (inverted)."""
    w = _TD_2YR
    mp = max(1, _TD_QTR)
    fcf_marg  = _safe_div(fcf, revenue.abs())
    ncfo_marg = _safe_div(ncfo, revenue.abs())
    cash_rev  = _safe_div(cashnequiv, revenue.abs())
    peak2y    = _rolling_max(cashnequiv, _TD_2YR)
    cash_dd   = _safe_div(peak2y - cashnequiv, peak2y.abs()).clip(lower=0)

    r1 = 1.0 - fcf_marg.rolling(w,  min_periods=mp).rank(pct=True)
    r3 = 1.0 - ncfo_marg.rolling(w, min_periods=mp).rank(pct=True)
    r4 = 1.0 - cash_rev.rolling(w,  min_periods=mp).rank(pct=True)
    return (r1 + cash_dd + r3 + r4) / 4.0


# ── Registry ──────────────────────────────────────────────────────────────────

CASH_BURN_REGISTRY_076_150 = {
    "cbr_076_fcf_3yr_rolling_sum":             {"inputs": ["fcf"],                        "func": cbr_076_fcf_3yr_rolling_sum},
    "cbr_077_fcf_5yr_rolling_sum":             {"inputs": ["fcf"],                        "func": cbr_077_fcf_5yr_rolling_sum},
    "cbr_078_fcf_2yr_change":                  {"inputs": ["fcf"],                        "func": cbr_078_fcf_2yr_change},
    "cbr_079_fcf_3yr_change":                  {"inputs": ["fcf"],                        "func": cbr_079_fcf_3yr_change},
    "cbr_080_fcf_trend_slope_8q":              {"inputs": ["fcf"],                        "func": cbr_080_fcf_trend_slope_8q},
    "cbr_081_ncfo_trend_slope_4q":             {"inputs": ["ncfo"],                       "func": cbr_081_ncfo_trend_slope_4q},
    "cbr_082_ncfo_trend_slope_8q":             {"inputs": ["ncfo"],                       "func": cbr_082_ncfo_trend_slope_8q},
    "cbr_083_fcf_min_4q":                      {"inputs": ["fcf"],                        "func": cbr_083_fcf_min_4q},
    "cbr_084_fcf_min_8q":                      {"inputs": ["fcf"],                        "func": cbr_084_fcf_min_8q},
    "cbr_085_fcf_min_12q":                     {"inputs": ["fcf"],                        "func": cbr_085_fcf_min_12q},
    "cbr_086_fcf_vs_4q_mean":                  {"inputs": ["fcf"],                        "func": cbr_086_fcf_vs_4q_mean},
    "cbr_087_fcf_vs_8q_mean":                  {"inputs": ["fcf"],                        "func": cbr_087_fcf_vs_8q_mean},
    "cbr_088_fcf_at_4q_low_flag":              {"inputs": ["fcf"],                        "func": cbr_088_fcf_at_4q_low_flag},
    "cbr_089_fcf_at_8q_low_flag":              {"inputs": ["fcf"],                        "func": cbr_089_fcf_at_8q_low_flag},
    "cbr_090_ncfo_4q_pct_rank":                {"inputs": ["ncfo"],                       "func": cbr_090_ncfo_4q_pct_rank},
    "cbr_091_cashnequiv_trend_slope_4q":       {"inputs": ["cashnequiv"],                 "func": cbr_091_cashnequiv_trend_slope_4q},
    "cbr_092_cashnequiv_trend_slope_8q":       {"inputs": ["cashnequiv"],                 "func": cbr_092_cashnequiv_trend_slope_8q},
    "cbr_093_cashnequiv_min_4q":               {"inputs": ["cashnequiv"],                 "func": cbr_093_cashnequiv_min_4q},
    "cbr_094_cashnequiv_min_8q":               {"inputs": ["cashnequiv"],                 "func": cbr_094_cashnequiv_min_8q},
    "cbr_095_cashnequiv_declining_4q_flag":    {"inputs": ["cashnequiv"],                 "func": cbr_095_cashnequiv_declining_4q_flag},
    "cbr_096_cashnequiv_declining_8q_flag":    {"inputs": ["cashnequiv"],                 "func": cbr_096_cashnequiv_declining_8q_flag},
    "cbr_097_cashnequiv_pct_rank_8q":          {"inputs": ["cashnequiv"],                 "func": cbr_097_cashnequiv_pct_rank_8q},
    "cbr_098_cashnequiv_vs_4q_mean":           {"inputs": ["cashnequiv"],                 "func": cbr_098_cashnequiv_vs_4q_mean},
    "cbr_099_cashnequiv_cv_4q":                {"inputs": ["cashnequiv"],                 "func": cbr_099_cashnequiv_cv_4q},
    "cbr_100_cashnequiv_3yr_change":           {"inputs": ["cashnequiv"],                 "func": cbr_100_cashnequiv_3yr_change},
    "cbr_101_cashnequiv_drawdown_from_3yr_peak": {"inputs": ["cashnequiv"],               "func": cbr_101_cashnequiv_drawdown_from_3yr_peak},
    "cbr_102_cash_depletion_speed_8q":         {"inputs": ["cashnequiv"],                 "func": cbr_102_cash_depletion_speed_8q},
    "cbr_103_cashnequiv_negative_flag":        {"inputs": ["cashnequiv"],                 "func": cbr_103_cashnequiv_negative_flag},
    "cbr_104_cashnequiv_below_1q_burn_flag":   {"inputs": ["cashnequiv", "fcf"],          "func": cbr_104_cashnequiv_below_1q_burn_flag},
    "cbr_105_cash_coverage_ncfo_4q":           {"inputs": ["cashnequiv", "ncfo"],         "func": cbr_105_cash_coverage_ncfo_4q},
    "cbr_106_ncfo_below_capex_flag":           {"inputs": ["ncfo", "capex"],              "func": cbr_106_ncfo_below_capex_flag},
    "cbr_107_ncfo_capex_deficit":              {"inputs": ["ncfo", "capex"],              "func": cbr_107_ncfo_capex_deficit},
    "cbr_108_capex_pct_of_ncfo":               {"inputs": ["capex", "ncfo"],              "func": cbr_108_capex_pct_of_ncfo},
    "cbr_109_ncfo_to_capex_ratio_pct_rank_8q": {"inputs": ["ncfo", "capex"],              "func": cbr_109_ncfo_to_capex_ratio_pct_rank_8q},
    "cbr_110_ncfo_to_capex_ratio_yoy_change":  {"inputs": ["ncfo", "capex"],              "func": cbr_110_ncfo_to_capex_ratio_yoy_change},
    "cbr_111_capex_rising_while_burning_flag": {"inputs": ["capex", "fcf"],               "func": cbr_111_capex_rising_while_burning_flag},
    "cbr_112_fcf_ex_capex_trend":              {"inputs": ["ncfo", "capex"],              "func": cbr_112_fcf_ex_capex_trend},
    "cbr_113_capex_intensity_4q_mean":         {"inputs": ["capex", "revenue"],           "func": cbr_113_capex_intensity_4q_mean},
    "cbr_114_capex_trend_slope_4q":            {"inputs": ["capex"],                      "func": cbr_114_capex_trend_slope_4q},
    "cbr_115_depamor_to_capex_ratio":          {"inputs": ["depamor", "capex"],           "func": cbr_115_depamor_to_capex_ratio},
    "cbr_116_maintenance_capex_proxy":         {"inputs": ["depamor", "capex"],           "func": cbr_116_maintenance_capex_proxy},
    "cbr_117_ncfo_less_maintenance_capex":     {"inputs": ["ncfo", "depamor"],            "func": cbr_117_ncfo_less_maintenance_capex},
    "cbr_118_true_burn_rate":                  {"inputs": ["ncfo", "capex", "sbcomp"],    "func": cbr_118_true_burn_rate},
    "cbr_119_sbcomp_to_ncfo_ratio":            {"inputs": ["sbcomp", "ncfo"],             "func": cbr_119_sbcomp_to_ncfo_ratio},
    "cbr_120_sbcomp_4q_sum":                   {"inputs": ["sbcomp"],                     "func": cbr_120_sbcomp_4q_sum},
    "cbr_121_sbcomp_adjusted_ncfo":            {"inputs": ["ncfo", "sbcomp"],             "func": cbr_121_sbcomp_adjusted_ncfo},
    "cbr_122_sbcomp_qoq_change":               {"inputs": ["sbcomp"],                     "func": cbr_122_sbcomp_qoq_change},
    "cbr_123_sbcomp_yoy_change":               {"inputs": ["sbcomp"],                     "func": cbr_123_sbcomp_yoy_change},
    "cbr_124_debt_funded_burn_flag":           {"inputs": ["ncf", "ncff", "fcf"],         "func": cbr_124_debt_funded_burn_flag},
    "cbr_125_ncff_level":                      {"inputs": ["ncff"],                       "func": cbr_125_ncff_level},
    "cbr_126_ncff_4q_sum":                     {"inputs": ["ncff"],                       "func": cbr_126_ncff_4q_sum},
    "cbr_127_ncfi_level":                      {"inputs": ["ncfi"],                       "func": cbr_127_ncfi_level},
    "cbr_128_ncfi_4q_sum":                     {"inputs": ["ncfi"],                       "func": cbr_128_ncfi_4q_sum},
    "cbr_129_ops_burn_not_covered_by_financing": {"inputs": ["ncfo", "ncff"],             "func": cbr_129_ops_burn_not_covered_by_financing},
    "cbr_130_total_cash_activities_4q":        {"inputs": ["ncfo", "ncfi", "ncff"],       "func": cbr_130_total_cash_activities_4q},
    "cbr_131_runway_under_4q_flag":            {"inputs": ["cashnequiv", "fcf"],          "func": cbr_131_runway_under_4q_flag},
    "cbr_132_runway_pct_rank_8q":              {"inputs": ["cashnequiv", "fcf"],          "func": cbr_132_runway_pct_rank_8q},
    "cbr_133_burn_intensity_zscore_4q":        {"inputs": ["fcf"],                        "func": cbr_133_burn_intensity_zscore_4q},
    "cbr_134_cash_draw_zscore_8q":             {"inputs": ["cashnequiv"],                 "func": cbr_134_cash_draw_zscore_8q},
    "cbr_135_fcf_ewm_3q":                      {"inputs": ["fcf"],                        "func": cbr_135_fcf_ewm_3q},
    "cbr_136_ncfo_ewm_3q":                     {"inputs": ["ncfo"],                       "func": cbr_136_ncfo_ewm_3q},
    "cbr_137_fcf_ewm_trend":                   {"inputs": ["fcf"],                        "func": cbr_137_fcf_ewm_trend},
    "cbr_138_burn_regime_score":               {"inputs": ["fcf", "cashnequiv"],          "func": cbr_138_burn_regime_score},
    "cbr_139_cash_burn_days_remaining":        {"inputs": ["cashnequiv", "fcf"],          "func": cbr_139_cash_burn_days_remaining},
    "cbr_140_cashnequiv_to_debt_ratio":        {"inputs": ["cashnequiv", "debt"],         "func": cbr_140_cashnequiv_to_debt_ratio},
    "cbr_141_cash_net_of_debt":                {"inputs": ["cashnequiv", "debt"],         "func": cbr_141_cash_net_of_debt},
    "cbr_142_debt_funded_burn_scale":          {"inputs": ["ncff", "fcf"],                "func": cbr_142_debt_funded_burn_scale},
    "cbr_143_opex_to_ncfo_ratio":              {"inputs": ["opex", "ncfo"],               "func": cbr_143_opex_to_ncfo_ratio},
    "cbr_144_all_cf_negative_8q_frac":         {"inputs": ["fcf", "ncfo", "ncf"],         "func": cbr_144_all_cf_negative_8q_frac},
    "cbr_145_cash_burn_persistence_score":     {"inputs": ["fcf"],                        "func": cbr_145_cash_burn_persistence_score},
    "cbr_146_fcf_worst_quarter_ratio":         {"inputs": ["fcf"],                        "func": cbr_146_fcf_worst_quarter_ratio},
    "cbr_147_cash_vs_burn_momentum":           {"inputs": ["cashnequiv", "fcf"],          "func": cbr_147_cash_vs_burn_momentum},
    "cbr_148_ncfo_below_opex_flag":            {"inputs": ["ncfo", "opex"],               "func": cbr_148_ncfo_below_opex_flag},
    "cbr_149_multi_signal_burn_count":         {"inputs": ["fcf", "ncfo", "cashnequiv"],  "func": cbr_149_multi_signal_burn_count},
    "cbr_150_cash_burn_severity_index":        {"inputs": ["fcf", "cashnequiv", "ncfo", "revenue"], "func": cbr_150_cash_burn_severity_index},
}
