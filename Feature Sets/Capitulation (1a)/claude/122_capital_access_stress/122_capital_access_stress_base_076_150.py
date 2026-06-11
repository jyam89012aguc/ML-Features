"""
122_capital_access_stress — Base Features 076-150
Domain: stress on the firm's access to external capital — reliance on external financing
        (financing cash flows vs operating cash flows), debt-issuance vs debt-repayment
        dynamics, secondary equity issuance patterns, share-buyback cessation/reversal,
        dividend cuts as financing-stress signals, cash-burn rate vs available capital,
        refinancing-need proxies, internal-vs-external funding mix.
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
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions already receive Series prepared this way; this helper
    is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


# ── Utility helpers ───────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero/near-zero denominator with NaN."""
    d = den.copy().astype(float)
    d[d.abs() < _EPS] = np.nan
    return num / d


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_sum(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).sum()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_median(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).median()


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


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
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=False)


# ── Feature functions 076-150 ─────────────────────────────────────────────────

# --- Group F (076-090): Short-term debt, current debt, refinancing risk ---

def cas_076_debtc_level(debtc: pd.Series) -> pd.Series:
    """Current (short-term) debt outstanding — near-term refinancing exposure."""
    return debtc.copy()


def cas_077_debtnc_level(debtnc: pd.Series) -> pd.Series:
    """Non-current (long-term) debt outstanding."""
    return debtnc.copy()


def cas_078_debtc_to_debt_ratio(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """Current debt / total debt: fraction of debt due near-term (high = refinancing risk)."""
    return _safe_div(debtc, debt)


def cas_079_debtc_to_equity_ratio(debtc: pd.Series, equity: pd.Series) -> pd.Series:
    """Current debt / book equity: near-term refinancing risk relative to equity cushion."""
    return _safe_div(debtc, equity.abs())


def cas_080_debtc_to_cashnequiv_ratio(debtc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Current debt / cash: immediate liquidity vs near-term debt obligations (>1 = stress)."""
    return _safe_div(debtc, cashnequiv)


def cas_081_debtc_exceeds_cash_flag(debtc: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """1 if current debt exceeds cash holdings (refinancing stress threshold)."""
    return (debtc > cashnequiv).astype(float)


def cas_082_debtc_qoq_change(debtc: pd.Series) -> pd.Series:
    """QoQ change in current debt — rising short-term debt = imminent refinancing need."""
    return debtc.diff(_TD_QTR)


def cas_083_debtc_yoy_change(debtc: pd.Series) -> pd.Series:
    """YoY change in current debt."""
    return debtc.diff(_TD_YEAR)


def cas_084_debtc_pct_rank_8q(debtc: pd.Series) -> pd.Series:
    """Percentile rank of current debt within 8-quarter window."""
    return debtc.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_085_debtnc_qoq_change(debtnc: pd.Series) -> pd.Series:
    """QoQ change in long-term debt (rising = more long-term borrowing or reclassification)."""
    return debtnc.diff(_TD_QTR)


def cas_086_debtnc_to_assets_ratio(debtnc: pd.Series, assets: pd.Series) -> pd.Series:
    """Long-term debt / total assets: structural leverage ratio."""
    return _safe_div(debtnc, assets)


def cas_087_debt_maturity_pressure(debtc: pd.Series, debtnc: pd.Series) -> pd.Series:
    """debtc / (debtc + debtnc): near-term maturity concentration (high = wall of maturities)."""
    total = debtc + debtnc
    return _safe_div(debtc, total)


def cas_088_debtc_vs_ncfo_ratio(debtc: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Current debt / |TTM NCFO|: how many years of operating cash to repay near-term debt."""
    ncfo4q = _rolling_sum(ncfo, _TD_YEAR)
    return _safe_div(debtc, ncfo4q.abs())


def cas_089_refinancing_gap(debtc: pd.Series, cashnequiv: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Refinancing gap: debtc - cashnequiv - TTM_NCFO (cash deficit to cover near-term debt).
    Positive = must access external capital to meet near-term obligations."""
    ncfo4q = _rolling_sum(ncfo, _TD_YEAR)
    return (debtc - cashnequiv - ncfo4q.clip(lower=0))


def cas_090_refinancing_gap_to_assets(debtc: pd.Series, cashnequiv: pd.Series,
                                       ncfo: pd.Series, assets: pd.Series) -> pd.Series:
    """Refinancing gap (debtc - cash - TTM NCFO) / total assets — scaled severity."""
    ncfo4q = _rolling_sum(ncfo, _TD_YEAR)
    gap    = debtc - cashnequiv - ncfo4q.clip(lower=0)
    return _safe_div(gap, assets)


# --- Group G (091-105): Internal vs external funding mix and trends ---

def cas_091_ncfo_to_ncff_ratio(ncfo: pd.Series, ncff: pd.Series) -> pd.Series:
    """TTM NCFO / |TTM NCFF|: internal funding coverage of external capital need.
    > 1 = operations fund more than external financing; < 1 = reliant on external."""
    ncfo4q = _rolling_sum(ncfo, _TD_YEAR)
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    return _safe_div(ncfo4q, ncff4q.abs())


def cas_092_ncfo_minus_ncff(ncfo: pd.Series, ncff: pd.Series) -> pd.Series:
    """TTM (NCFO - NCFF): net internal funding surplus/deficit after external capital."""
    ncfo4q = _rolling_sum(ncfo, _TD_YEAR)
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    return ncfo4q - ncff4q


def cas_093_ncff_ncfo_sum(ncfo: pd.Series, ncff: pd.Series) -> pd.Series:
    """NCFO + NCFF (TTM): combined operating and financing cash flows — total liquidity signal."""
    return _rolling_sum(ncfo + ncff, _TD_YEAR)


def cas_094_internal_vs_external_trend(ncfo: pd.Series, ncff: pd.Series) -> pd.Series:
    """Slope of (NCFO/|NCFF|) over 4 quarters — trending toward external reliance."""
    ratio = _safe_div(ncfo, ncff.abs())
    return _linslope(ratio, _TD_YEAR)


def cas_095_ncff_exceeds_ncfo_flag(ncfo: pd.Series, ncff: pd.Series) -> pd.Series:
    """1 if |ncff| > |ncfo|: firm raises more externally than it generates operationally."""
    return (ncff.abs() > ncfo.abs()).astype(float)


def cas_096_ncff_positive_ncfo_negative_flag(ncfo: pd.Series, ncff: pd.Series) -> pd.Series:
    """1 if ncff > 0 and ncfo < 0: firm borrowing/issuing to cover operating cash loss (severe stress)."""
    return ((ncff > 0) & (ncfo < 0)).astype(float)


def cas_097_total_financing_reliance_4q(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Count of quarters in trailing year where ncff > 0 and ncfo < 0 (external-financing required)."""
    flag = ((ncff > 0) & (ncfo < 0)).astype(float)
    return _rolling_sum(flag, _TD_YEAR)


def cas_098_ncff_to_assets(ncff: pd.Series, assets: pd.Series) -> pd.Series:
    """TTM NCFF / total assets: external capital inflow scaled by asset base."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    return _safe_div(ncff4q, assets)


def cas_099_ncff_to_equity(ncff: pd.Series, equity: pd.Series) -> pd.Series:
    """TTM NCFF / book equity: external capital inflow relative to equity cushion."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    return _safe_div(ncff4q, equity.abs())


def cas_100_funding_mix_shift_qoq(ncfo: pd.Series, ncff: pd.Series) -> pd.Series:
    """QoQ change in (ncff / (ncff + ncfo)) — shifting toward external funding."""
    total = ncff.abs() + ncfo.abs()
    mix   = _safe_div(ncff.clip(lower=0), total)
    return mix.diff(_TD_QTR)


def cas_101_ncff_slope_4q(ncff: pd.Series) -> pd.Series:
    """OLS slope of NCFF over trailing 4 quarters (252 td) — trend in external capital reliance."""
    return _linslope(ncff, _TD_YEAR)


def cas_102_ncff_slope_8q(ncff: pd.Series) -> pd.Series:
    """OLS slope of NCFF over trailing 8 quarters (504 td)."""
    return _linslope(ncff, _TD_2YR)


def cas_103_ncfdebt_slope_4q(ncfdebt: pd.Series) -> pd.Series:
    """OLS slope of ncfdebt over trailing 4 quarters — trend in debt capital reliance."""
    return _linslope(ncfdebt, _TD_YEAR)


def cas_104_ncfcommon_slope_4q(ncfcommon: pd.Series) -> pd.Series:
    """OLS slope of ncfcommon over trailing 4 quarters — trend in equity-raise activity."""
    return _linslope(ncfcommon, _TD_YEAR)


def cas_105_combined_external_flow_4q(ncfdebt: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    """TTM sum of (ncfdebt + ncfcommon): total external capital (debt + equity) raised annually."""
    return _rolling_sum(ncfdebt + ncfcommon, _TD_YEAR)


# --- Group H (106-120): Equity and leverage deterioration indicators ---

def cas_106_equity_level(equity: pd.Series) -> pd.Series:
    """Book equity level — declining equity signals capital destruction."""
    return equity.copy()


def cas_107_equity_qoq_change(equity: pd.Series) -> pd.Series:
    """QoQ change in book equity."""
    return equity.diff(_TD_QTR)


def cas_108_equity_yoy_change(equity: pd.Series) -> pd.Series:
    """YoY change in book equity."""
    return equity.diff(_TD_YEAR)


def cas_109_equity_negative_flag(equity: pd.Series) -> pd.Series:
    """1 if book equity is negative (insolvency threshold — external capital fully lost)."""
    return (equity < 0).astype(float)


def cas_110_equity_drawdown_from_2yr_peak(equity: pd.Series) -> pd.Series:
    """Book equity drawdown from trailing 2-year peak (capital erosion signal)."""
    peak = _rolling_max(equity, _TD_2YR)
    return _safe_div(equity - peak, peak.abs())


def cas_111_equity_drawdown_from_alltime_peak(equity: pd.Series) -> pd.Series:
    """Book equity drawdown from all-time expanding peak."""
    peak = equity.expanding(min_periods=1).max()
    return _safe_div(equity - peak, peak.abs())


def cas_112_equity_pct_rank_8q(equity: pd.Series) -> pd.Series:
    """Percentile rank of equity in trailing 8-quarter window (low = at multi-year equity low)."""
    return equity.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_113_leverage_qoq_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """QoQ change in debt/equity leverage ratio."""
    lev = _safe_div(debt, equity.abs())
    return lev.diff(_TD_QTR)


def cas_114_leverage_yoy_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """YoY change in debt/equity leverage ratio."""
    lev = _safe_div(debt, equity.abs())
    return lev.diff(_TD_YEAR)


def cas_115_leverage_pct_rank_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Percentile rank of leverage (debt/equity) within 8-quarter window."""
    lev = _safe_div(debt, equity.abs())
    return lev.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_116_leverage_zscore_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of leverage within 8-quarter window."""
    lev = _safe_div(debt, equity.abs())
    return _zscore_rolling(lev, _TD_2YR)


def cas_117_debt_above_equity_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 if total debt > book equity (leverage > 1x) — constrained external access zone."""
    return (debt > equity.abs()).astype(float)


def cas_118_ncfo_to_intexp_coverage(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """TTM NCFO / |intexp|: operating cash interest coverage (< 1 = cannot service interest operationally)."""
    ncfo4q   = _rolling_sum(ncfo, _TD_YEAR)
    intexp4q = _rolling_sum(intexp.abs(), _TD_YEAR)
    return _safe_div(ncfo4q, intexp4q)


def cas_119_intexp_growth_rate_yoy(intexp: pd.Series) -> pd.Series:
    """YoY percent growth in interest expense (rising intexp = new or more expensive debt)."""
    prior = intexp.shift(_TD_YEAR)
    return _safe_div(intexp.abs() - prior.abs(), prior.abs())


def cas_120_intexp_pct_rank_8q(intexp: pd.Series) -> pd.Series:
    """Percentile rank of interest expense within 8-quarter window (high = peak debt cost)."""
    return intexp.abs().rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


# --- Group I (121-135): Capital return vs distress indicators ---

def cas_121_buyback_magnitude_4q(ncfcommon: pd.Series) -> pd.Series:
    """TTM buyback magnitude: sum of |ncfcommon| where ncfcommon < 0."""
    buyback = (-ncfcommon).clip(lower=0)
    return _rolling_sum(buyback, _TD_YEAR)


def cas_122_buyback_vs_earnings_ratio(ncfcommon: pd.Series, netinc: pd.Series) -> pd.Series:
    """TTM buyback / TTM net income: capital returned vs earnings (negative net = unsustainable)."""
    buybacks = _rolling_sum((-ncfcommon).clip(lower=0), _TD_YEAR)
    earnings = _rolling_sum(netinc, _TD_YEAR)
    return _safe_div(buybacks, earnings.abs())


def cas_123_total_capital_return_4q(ncfcommon: pd.Series, dividends: pd.Series) -> pd.Series:
    """TTM total capital return: buybacks + dividends (measuring how much was returned)."""
    buybacks = (-ncfcommon).clip(lower=0)
    return _rolling_sum(buybacks + dividends, _TD_YEAR)


def cas_124_capital_return_pct_rank_8q(ncfcommon: pd.Series, dividends: pd.Series) -> pd.Series:
    """Percentile rank of total capital return (buybacks + dividends) within 8 quarters."""
    buybacks = (-ncfcommon).clip(lower=0)
    total    = buybacks + dividends
    return total.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_125_capital_return_drawdown_from_2yr_peak(ncfcommon: pd.Series, dividends: pd.Series) -> pd.Series:
    """Total capital return drawdown from 2-year peak (cessation/reduction severity)."""
    buybacks = (-ncfcommon).clip(lower=0)
    total    = buybacks + dividends
    peak     = _rolling_max(total, _TD_2YR)
    return _safe_div(total - peak, peak.abs())


def cas_126_no_capital_return_flag(ncfcommon: pd.Series, dividends: pd.Series) -> pd.Series:
    """1 if no capital is being returned (ncfcommon >= 0 AND dividends == 0)."""
    return ((ncfcommon >= 0) & (dividends <= 0)).astype(float)


def cas_127_capital_return_negative_flag(ncfcommon: pd.Series, dividends: pd.Series,
                                          ncfo: pd.Series) -> pd.Series:
    """1 if capital return exceeds operating cash (burning balance sheet to return capital)."""
    buybacks = (-ncfcommon).clip(lower=0)
    total    = buybacks + dividends
    return (total > ncfo.clip(lower=0)).astype(float)


def cas_128_sbcomp_to_ncfo_ratio(sbcomp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Stock-based comp / |ncfo|: non-cash comp as fraction of operating cash (high = low real cash income)."""
    return _safe_div(sbcomp.abs(), ncfo.abs())


def cas_129_sbcomp_to_revenue(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    """SBC / revenue: non-cash comp intensity relative to revenue."""
    return _safe_div(sbcomp.abs(), revenue)


def cas_130_sbcomp_pct_rank_8q(sbcomp: pd.Series) -> pd.Series:
    """Percentile rank of SBC within 8-quarter window (high = peak non-cash comp)."""
    return sbcomp.abs().rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_131_ncfcommon_plus_dividends_yoy_change(ncfcommon: pd.Series, dividends: pd.Series) -> pd.Series:
    """YoY change in (ncfcommon + dividends): total financing flows to shareholders."""
    total = ncfcommon + dividends
    return total.diff(_TD_YEAR)


def cas_132_dividends_pct_rank_8q(dividends: pd.Series) -> pd.Series:
    """Percentile rank of dividends within 8-quarter window."""
    return dividends.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_133_dps_zscore_8q(dps: pd.Series) -> pd.Series:
    """Z-score of DPS within 8-quarter window (negative = DPS at historic low)."""
    return _zscore_rolling(dps, _TD_2YR)


def cas_134_prefdivis_level(prefdivis: pd.Series) -> pd.Series:
    """Preferred dividends (prefdivis) — obligation that ranks above common equity return."""
    return prefdivis.copy()


def cas_135_prefdivis_to_ncfo(prefdivis: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Preferred dividends / |NCFO|: preferred obligation burden on operating cash."""
    return _safe_div(prefdivis.abs(), ncfo.abs())


# --- Group J (136-150): Composite and multi-signal stress indicators ---

def cas_136_ncff_ncfdebt_ncfcommon_decomp_flag(ncff: pd.Series, ncfdebt: pd.Series,
                                                ncfcommon: pd.Series) -> pd.Series:
    """1 if all three financing components positive simultaneously (all external channels open = maximum reliance)."""
    return ((ncff > 0) & (ncfdebt > 0) & (ncfcommon > 0)).astype(float)


def cas_137_debt_equity_issuance_both_flag(ncfdebt: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    """1 if both ncfdebt > 0 and ncfcommon > 0 simultaneously (dual-channel external capital stress)."""
    return ((ncfdebt > 0) & (ncfcommon > 0)).astype(float)


def cas_138_ncff_acceleration_qoq(ncff: pd.Series) -> pd.Series:
    """QoQ change in QoQ change in ncff (acceleration of external capital reliance)."""
    qoq = ncff.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def cas_139_ncfdebt_acceleration_qoq(ncfdebt: pd.Series) -> pd.Series:
    """QoQ acceleration in ncfdebt — accelerating debt issuance = mounting distress."""
    qoq = ncfdebt.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def cas_140_ncfcommon_acceleration_qoq(ncfcommon: pd.Series) -> pd.Series:
    """QoQ acceleration in ncfcommon — accelerating equity issuance signals severe distress."""
    qoq = ncfcommon.diff(_TD_QTR)
    return qoq.diff(_TD_QTR)


def cas_141_external_capital_intensity(ncff: pd.Series, assets: pd.Series) -> pd.Series:
    """TTM |NCFF| / total assets: volume of external capital activity relative to firm size."""
    return _safe_div(_rolling_sum(ncff.abs(), _TD_YEAR), assets)


def cas_142_financing_vs_investing_ratio(ncff: pd.Series, ncfi: pd.Series) -> pd.Series:
    """|NCFF| / |NCFI|: how much external capital finances investment activity.
    > 1 = external capital exceeds investing outflows (over-financed or distress-funded)."""
    return _safe_div(ncff.abs(), ncfi.abs())


def cas_143_ncfi_level(ncfi: pd.Series) -> pd.Series:
    """Net cash from investing activities — investing outflows signal asset-acquisition mode."""
    return ncfi.copy()


def cas_144_ncfi_vs_ncff_sum(ncfi: pd.Series, ncff: pd.Series) -> pd.Series:
    """NCFI + NCFF: net capital activity (investing + financing); very negative = capital trap."""
    return _rolling_sum(ncfi + ncff, _TD_YEAR)


def cas_145_all_three_flows_negative_flag(ncfo: pd.Series, ncfi: pd.Series, ncff: pd.Series) -> pd.Series:
    """1 if NCFO, NCFI, and NCFF are all negative (no external access and burning operations)."""
    return ((ncfo < 0) & (ncfi < 0) & (ncff < 0)).astype(float)


def cas_146_leverage_trend_slope_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """OLS slope of debt/equity leverage over trailing 4 quarters."""
    lev = _safe_div(debt, equity.abs())
    return _linslope(lev, _TD_YEAR)


def cas_147_leverage_trend_slope_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """OLS slope of debt/equity leverage over trailing 8 quarters."""
    lev = _safe_div(debt, equity.abs())
    return _linslope(lev, _TD_2YR)


def cas_148_net_debt_pct_rank_8q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Percentile rank of net debt (debt - cash) within 8-quarter window."""
    net_debt = debt - cashnequiv
    return net_debt.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_149_cash_coverage_of_debtc_and_intexp(cashnequiv: pd.Series, debtc: pd.Series,
                                               intexp: pd.Series) -> pd.Series:
    """Cash / (debtc + annualized intexp): composite near-term liquidity coverage.
    < 1 = external capital required for near-term obligations."""
    annual_intexp = _rolling_sum(intexp.abs(), _TD_YEAR)
    obligations   = debtc + annual_intexp
    return _safe_div(cashnequiv, obligations)


def cas_150_capital_access_stress_composite(ncff: pd.Series, ncfdebt: pd.Series,
                                             ncfcommon: pd.Series, debt: pd.Series,
                                             equity: pd.Series, cashnequiv: pd.Series,
                                             intexp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Comprehensive capital access stress composite.
    Weighted combination: NCFF reliance rank + leverage rank + interest coverage (inverted) + net-debt rank.
    Higher = more severe external capital stress."""
    ncff_r  = ncff.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    lev     = _safe_div(debt, equity.abs()).fillna(0)
    lev_r   = lev.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    ncfo4q  = _rolling_sum(ncfo, _TD_YEAR)
    int4q   = _rolling_sum(intexp.abs(), _TD_YEAR)
    cov     = _safe_div(ncfo4q, int4q).fillna(1.0).clip(-5, 5)
    cov_n   = 1.0 - (cov + 5.0) / 10.0   # invert: high coverage = low stress
    net_d   = debt - cashnequiv
    nd_r    = net_d.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True).fillna(0.5)
    return 0.30 * ncff_r + 0.25 * lev_r + 0.25 * cov_n + 0.20 * nd_r


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITAL_ACCESS_STRESS_REGISTRY_076_150 = {
    "cas_076_debtc_level":                       {"inputs": ["debtc"],                                      "func": cas_076_debtc_level},
    "cas_077_debtnc_level":                      {"inputs": ["debtnc"],                                     "func": cas_077_debtnc_level},
    "cas_078_debtc_to_debt_ratio":               {"inputs": ["debtc", "debt"],                              "func": cas_078_debtc_to_debt_ratio},
    "cas_079_debtc_to_equity_ratio":             {"inputs": ["debtc", "equity"],                            "func": cas_079_debtc_to_equity_ratio},
    "cas_080_debtc_to_cashnequiv_ratio":         {"inputs": ["debtc", "cashnequiv"],                        "func": cas_080_debtc_to_cashnequiv_ratio},
    "cas_081_debtc_exceeds_cash_flag":           {"inputs": ["debtc", "cashnequiv"],                        "func": cas_081_debtc_exceeds_cash_flag},
    "cas_082_debtc_qoq_change":                  {"inputs": ["debtc"],                                      "func": cas_082_debtc_qoq_change},
    "cas_083_debtc_yoy_change":                  {"inputs": ["debtc"],                                      "func": cas_083_debtc_yoy_change},
    "cas_084_debtc_pct_rank_8q":                 {"inputs": ["debtc"],                                      "func": cas_084_debtc_pct_rank_8q},
    "cas_085_debtnc_qoq_change":                 {"inputs": ["debtnc"],                                     "func": cas_085_debtnc_qoq_change},
    "cas_086_debtnc_to_assets_ratio":            {"inputs": ["debtnc", "assets"],                           "func": cas_086_debtnc_to_assets_ratio},
    "cas_087_debt_maturity_pressure":            {"inputs": ["debtc", "debtnc"],                            "func": cas_087_debt_maturity_pressure},
    "cas_088_debtc_vs_ncfo_ratio":               {"inputs": ["debtc", "ncfo"],                              "func": cas_088_debtc_vs_ncfo_ratio},
    "cas_089_refinancing_gap":                   {"inputs": ["debtc", "cashnequiv", "ncfo"],                "func": cas_089_refinancing_gap},
    "cas_090_refinancing_gap_to_assets":         {"inputs": ["debtc", "cashnequiv", "ncfo", "assets"],     "func": cas_090_refinancing_gap_to_assets},
    "cas_091_ncfo_to_ncff_ratio":                {"inputs": ["ncfo", "ncff"],                               "func": cas_091_ncfo_to_ncff_ratio},
    "cas_092_ncfo_minus_ncff":                   {"inputs": ["ncfo", "ncff"],                               "func": cas_092_ncfo_minus_ncff},
    "cas_093_ncff_ncfo_sum":                     {"inputs": ["ncfo", "ncff"],                               "func": cas_093_ncff_ncfo_sum},
    "cas_094_internal_vs_external_trend":        {"inputs": ["ncfo", "ncff"],                               "func": cas_094_internal_vs_external_trend},
    "cas_095_ncff_exceeds_ncfo_flag":            {"inputs": ["ncfo", "ncff"],                               "func": cas_095_ncff_exceeds_ncfo_flag},
    "cas_096_ncff_positive_ncfo_negative_flag":  {"inputs": ["ncfo", "ncff"],                               "func": cas_096_ncff_positive_ncfo_negative_flag},
    "cas_097_total_financing_reliance_4q":       {"inputs": ["ncff", "ncfo"],                               "func": cas_097_total_financing_reliance_4q},
    "cas_098_ncff_to_assets":                    {"inputs": ["ncff", "assets"],                             "func": cas_098_ncff_to_assets},
    "cas_099_ncff_to_equity":                    {"inputs": ["ncff", "equity"],                             "func": cas_099_ncff_to_equity},
    "cas_100_funding_mix_shift_qoq":             {"inputs": ["ncfo", "ncff"],                               "func": cas_100_funding_mix_shift_qoq},
    "cas_101_ncff_slope_4q":                     {"inputs": ["ncff"],                                       "func": cas_101_ncff_slope_4q},
    "cas_102_ncff_slope_8q":                     {"inputs": ["ncff"],                                       "func": cas_102_ncff_slope_8q},
    "cas_103_ncfdebt_slope_4q":                  {"inputs": ["ncfdebt"],                                    "func": cas_103_ncfdebt_slope_4q},
    "cas_104_ncfcommon_slope_4q":                {"inputs": ["ncfcommon"],                                  "func": cas_104_ncfcommon_slope_4q},
    "cas_105_combined_external_flow_4q":         {"inputs": ["ncfdebt", "ncfcommon"],                       "func": cas_105_combined_external_flow_4q},
    "cas_106_equity_level":                      {"inputs": ["equity"],                                     "func": cas_106_equity_level},
    "cas_107_equity_qoq_change":                 {"inputs": ["equity"],                                     "func": cas_107_equity_qoq_change},
    "cas_108_equity_yoy_change":                 {"inputs": ["equity"],                                     "func": cas_108_equity_yoy_change},
    "cas_109_equity_negative_flag":              {"inputs": ["equity"],                                     "func": cas_109_equity_negative_flag},
    "cas_110_equity_drawdown_from_2yr_peak":     {"inputs": ["equity"],                                     "func": cas_110_equity_drawdown_from_2yr_peak},
    "cas_111_equity_drawdown_from_alltime_peak": {"inputs": ["equity"],                                     "func": cas_111_equity_drawdown_from_alltime_peak},
    "cas_112_equity_pct_rank_8q":                {"inputs": ["equity"],                                     "func": cas_112_equity_pct_rank_8q},
    "cas_113_leverage_qoq_change":               {"inputs": ["debt", "equity"],                             "func": cas_113_leverage_qoq_change},
    "cas_114_leverage_yoy_change":               {"inputs": ["debt", "equity"],                             "func": cas_114_leverage_yoy_change},
    "cas_115_leverage_pct_rank_8q":              {"inputs": ["debt", "equity"],                             "func": cas_115_leverage_pct_rank_8q},
    "cas_116_leverage_zscore_8q":                {"inputs": ["debt", "equity"],                             "func": cas_116_leverage_zscore_8q},
    "cas_117_debt_above_equity_flag":            {"inputs": ["debt", "equity"],                             "func": cas_117_debt_above_equity_flag},
    "cas_118_ncfo_to_intexp_coverage":           {"inputs": ["ncfo", "intexp"],                             "func": cas_118_ncfo_to_intexp_coverage},
    "cas_119_intexp_growth_rate_yoy":            {"inputs": ["intexp"],                                     "func": cas_119_intexp_growth_rate_yoy},
    "cas_120_intexp_pct_rank_8q":                {"inputs": ["intexp"],                                     "func": cas_120_intexp_pct_rank_8q},
    "cas_121_buyback_magnitude_4q":              {"inputs": ["ncfcommon"],                                  "func": cas_121_buyback_magnitude_4q},
    "cas_122_buyback_vs_earnings_ratio":         {"inputs": ["ncfcommon", "netinc"],                        "func": cas_122_buyback_vs_earnings_ratio},
    "cas_123_total_capital_return_4q":           {"inputs": ["ncfcommon", "dividends"],                     "func": cas_123_total_capital_return_4q},
    "cas_124_capital_return_pct_rank_8q":        {"inputs": ["ncfcommon", "dividends"],                     "func": cas_124_capital_return_pct_rank_8q},
    "cas_125_capital_return_drawdown_from_2yr_peak": {"inputs": ["ncfcommon", "dividends"],                 "func": cas_125_capital_return_drawdown_from_2yr_peak},
    "cas_126_no_capital_return_flag":            {"inputs": ["ncfcommon", "dividends"],                     "func": cas_126_no_capital_return_flag},
    "cas_127_capital_return_negative_flag":      {"inputs": ["ncfcommon", "dividends", "ncfo"],             "func": cas_127_capital_return_negative_flag},
    "cas_128_sbcomp_to_ncfo_ratio":              {"inputs": ["sbcomp", "ncfo"],                             "func": cas_128_sbcomp_to_ncfo_ratio},
    "cas_129_sbcomp_to_revenue":                 {"inputs": ["sbcomp", "revenue"],                          "func": cas_129_sbcomp_to_revenue},
    "cas_130_sbcomp_pct_rank_8q":                {"inputs": ["sbcomp"],                                     "func": cas_130_sbcomp_pct_rank_8q},
    "cas_131_ncfcommon_plus_dividends_yoy_change": {"inputs": ["ncfcommon", "dividends"],                   "func": cas_131_ncfcommon_plus_dividends_yoy_change},
    "cas_132_dividends_pct_rank_8q":             {"inputs": ["dividends"],                                  "func": cas_132_dividends_pct_rank_8q},
    "cas_133_dps_zscore_8q":                     {"inputs": ["dps"],                                        "func": cas_133_dps_zscore_8q},
    "cas_134_prefdivis_level":                   {"inputs": ["prefdivis"],                                  "func": cas_134_prefdivis_level},
    "cas_135_prefdivis_to_ncfo":                 {"inputs": ["prefdivis", "ncfo"],                          "func": cas_135_prefdivis_to_ncfo},
    "cas_136_ncff_ncfdebt_ncfcommon_decomp_flag": {"inputs": ["ncff", "ncfdebt", "ncfcommon"],             "func": cas_136_ncff_ncfdebt_ncfcommon_decomp_flag},
    "cas_137_debt_equity_issuance_both_flag":    {"inputs": ["ncfdebt", "ncfcommon"],                       "func": cas_137_debt_equity_issuance_both_flag},
    "cas_138_ncff_acceleration_qoq":             {"inputs": ["ncff"],                                       "func": cas_138_ncff_acceleration_qoq},
    "cas_139_ncfdebt_acceleration_qoq":          {"inputs": ["ncfdebt"],                                    "func": cas_139_ncfdebt_acceleration_qoq},
    "cas_140_ncfcommon_acceleration_qoq":        {"inputs": ["ncfcommon"],                                  "func": cas_140_ncfcommon_acceleration_qoq},
    "cas_141_external_capital_intensity":        {"inputs": ["ncff", "assets"],                             "func": cas_141_external_capital_intensity},
    "cas_142_financing_vs_investing_ratio":      {"inputs": ["ncff", "ncfi"],                               "func": cas_142_financing_vs_investing_ratio},
    "cas_143_ncfi_level":                        {"inputs": ["ncfi"],                                       "func": cas_143_ncfi_level},
    "cas_144_ncfi_vs_ncff_sum":                  {"inputs": ["ncfi", "ncff"],                               "func": cas_144_ncfi_vs_ncff_sum},
    "cas_145_all_three_flows_negative_flag":     {"inputs": ["ncfo", "ncfi", "ncff"],                       "func": cas_145_all_three_flows_negative_flag},
    "cas_146_leverage_trend_slope_4q":           {"inputs": ["debt", "equity"],                             "func": cas_146_leverage_trend_slope_4q},
    "cas_147_leverage_trend_slope_8q":           {"inputs": ["debt", "equity"],                             "func": cas_147_leverage_trend_slope_8q},
    "cas_148_net_debt_pct_rank_8q":              {"inputs": ["debt", "cashnequiv"],                         "func": cas_148_net_debt_pct_rank_8q},
    "cas_149_cash_coverage_of_debtc_and_intexp": {"inputs": ["cashnequiv", "debtc", "intexp"],              "func": cas_149_cash_coverage_of_debtc_and_intexp},
    "cas_150_capital_access_stress_composite":   {"inputs": ["ncff", "ncfdebt", "ncfcommon", "debt", "equity", "cashnequiv", "intexp", "ncfo"], "func": cas_150_capital_access_stress_composite},
}
