"""
122_capital_access_stress — Base Features 001-075
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

Distinct from: family 70 (dilution_acceleration — share count growth), family 63
(cash_burn — FCF level), family 96 (dividend_distress — dividend cuts as event).
This family measures ACCESS to and RELIANCE on external capital markets.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252          # trading days per year
_TD_HALF = 126          # half-year
_TD_QTR  = 63           # one quarter
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


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-015): Financing cash flow level and reliance ---

def cas_001_ncff_level(ncff: pd.Series) -> pd.Series:
    """Net cash from financing activities (ncff) level — positive = net inflow from external capital."""
    return ncff.copy()


def cas_002_ncff_positive_flag(ncff: pd.Series) -> pd.Series:
    """1 if ncff > 0: firm is net-receiving external capital (equity or debt issuance > repayments)."""
    return (ncff > 0).astype(float)


def cas_003_ncff_4q_sum(ncff: pd.Series) -> pd.Series:
    """Trailing 4-quarter (252 td) sum of financing cash flows — annual external-capital reliance."""
    return _rolling_sum(ncff, _TD_YEAR)


def cas_004_ncff_8q_sum(ncff: pd.Series) -> pd.Series:
    """Trailing 8-quarter (504 td) sum of financing cash flows."""
    return _rolling_sum(ncff, _TD_2YR)


def cas_005_ncff_vs_ncfo_ratio(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """NCFF / |NCFO|: ratio of external-capital inflow to operating cash flow magnitude.
    High positive ratio = firm relies on external capital to offset weak operations."""
    return _safe_div(ncff, ncfo.abs())


def cas_006_ncff_vs_ncfo_ttm_ratio(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """TTM NCFF / |TTM NCFO|: annual external reliance ratio (smoother signal)."""
    ncff4q = _rolling_sum(ncff, _TD_YEAR)
    ncfo4q = _rolling_sum(ncfo, _TD_YEAR)
    return _safe_div(ncff4q, ncfo4q.abs())


def cas_007_external_funding_dependence(ncff: pd.Series, ncfo: pd.Series) -> pd.Series:
    """NCFF / (NCFF + |NCFO|): fraction of total cash inflows sourced externally.
    Near 1 = almost entirely external; near 0 = self-funded."""
    denom = ncff.abs() + ncfo.abs()
    return _safe_div(ncff.clip(lower=0), denom)


def cas_008_ncff_drawdown_from_4q_peak(ncff: pd.Series) -> pd.Series:
    """NCFF drawdown from trailing 4-quarter peak (worsening external access)."""
    peak = _rolling_max(ncff, _TD_YEAR)
    return _safe_div(ncff - peak, peak.abs())


def cas_009_ncff_drawdown_from_2yr_peak(ncff: pd.Series) -> pd.Series:
    """NCFF drawdown from trailing 2-year peak."""
    peak = _rolling_max(ncff, _TD_2YR)
    return _safe_div(ncff - peak, peak.abs())


def cas_010_ncff_qoq_change(ncff: pd.Series) -> pd.Series:
    """QoQ change in NCFF (63 td diff) — deteriorating external capital access."""
    return ncff.diff(_TD_QTR)


def cas_011_ncff_yoy_change(ncff: pd.Series) -> pd.Series:
    """YoY change in NCFF (252 td diff)."""
    return ncff.diff(_TD_YEAR)


def cas_012_ncff_4q_negative_fraction(ncff: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where ncff < 0 (more repayment than issuance)."""
    neg = (ncff < 0).astype(float)
    return _rolling_mean(neg, _TD_YEAR)


def cas_013_ncff_pct_rank_8q(ncff: pd.Series) -> pd.Series:
    """Percentile rank of NCFF within trailing 8-quarter window (low = most reliant)."""
    return ncff.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_014_ncff_zscore_8q(ncff: pd.Series) -> pd.Series:
    """Z-score of NCFF over trailing 8 quarters (extreme positive = peak external reliance)."""
    return _zscore_rolling(ncff, _TD_2YR)


def cas_015_ncff_to_revenue(ncff: pd.Series, revenue: pd.Series) -> pd.Series:
    """NCFF / revenue: external capital raised per dollar of revenue (funding intensity)."""
    return _safe_div(ncff, revenue)


# --- Group B (016-030): Debt issuance vs repayment dynamics (ncfdebt) ---

def cas_016_ncfdebt_level(ncfdebt: pd.Series) -> pd.Series:
    """Net cash from debt issuance/repayment (ncfdebt) — positive = net new borrowing."""
    return ncfdebt.copy()


def cas_017_ncfdebt_positive_flag(ncfdebt: pd.Series) -> pd.Series:
    """1 if ncfdebt > 0: firm is net-borrowing (debt access open)."""
    return (ncfdebt > 0).astype(float)


def cas_018_ncfdebt_negative_flag(ncfdebt: pd.Series) -> pd.Series:
    """1 if ncfdebt < 0: firm is net-repaying debt (possibly forced or optional deleveraging)."""
    return (ncfdebt < 0).astype(float)


def cas_019_ncfdebt_4q_sum(ncfdebt: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of net debt issuance/repayment — annual debt-capital reliance."""
    return _rolling_sum(ncfdebt, _TD_YEAR)


def cas_020_ncfdebt_8q_sum(ncfdebt: pd.Series) -> pd.Series:
    """Trailing 8-quarter cumulative net debt change."""
    return _rolling_sum(ncfdebt, _TD_2YR)


def cas_021_ncfdebt_qoq_change(ncfdebt: pd.Series) -> pd.Series:
    """QoQ change in ncfdebt — shift from borrowing to repaying is a stress signal."""
    return ncfdebt.diff(_TD_QTR)


def cas_022_ncfdebt_yoy_change(ncfdebt: pd.Series) -> pd.Series:
    """YoY change in ncfdebt."""
    return ncfdebt.diff(_TD_YEAR)


def cas_023_ncfdebt_drawdown_from_4q_peak(ncfdebt: pd.Series) -> pd.Series:
    """ncfdebt drawdown from trailing 4-quarter peak (declining access to new debt)."""
    peak = _rolling_max(ncfdebt, _TD_YEAR)
    return _safe_div(ncfdebt - peak, peak.abs())


def cas_024_ncfdebt_pct_rank_8q(ncfdebt: pd.Series) -> pd.Series:
    """Percentile rank of ncfdebt within trailing 8-quarter window."""
    return ncfdebt.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_025_ncfdebt_zscore_8q(ncfdebt: pd.Series) -> pd.Series:
    """Z-score of ncfdebt over trailing 8 quarters."""
    return _zscore_rolling(ncfdebt, _TD_2YR)


def cas_026_debt_issuance_fraction_4q(ncfdebt: pd.Series) -> pd.Series:
    """Fraction of trailing 4 quarters where ncfdebt > 0 (reliance on new debt)."""
    pos = (ncfdebt > 0).astype(float)
    return _rolling_mean(pos, _TD_YEAR)


def cas_027_ncfdebt_to_debt_ratio(ncfdebt: pd.Series, debt: pd.Series) -> pd.Series:
    """Net new borrowing / total outstanding debt — maturity/refinancing pressure proxy."""
    return _safe_div(ncfdebt, debt)


def cas_028_debt_repayment_spike_flag(ncfdebt: pd.Series) -> pd.Series:
    """1 if ncfdebt < -1 SD of its 8-quarter rolling distribution (unusual repayment spike)."""
    m   = _rolling_mean(ncfdebt, _TD_2YR)
    sd  = _rolling_std(ncfdebt, _TD_2YR)
    thr = m - sd
    return (ncfdebt < thr).astype(float)


def cas_029_ncfdebt_negative_4q_count(ncfdebt: pd.Series) -> pd.Series:
    """Count of quarters in trailing year with ncfdebt < 0 (sustained debt repayment pressure)."""
    neg = (ncfdebt < 0).astype(float)
    return _rolling_sum(neg, _TD_YEAR)


def cas_030_ncfdebt_vs_ncfo(ncfdebt: pd.Series, ncfo: pd.Series) -> pd.Series:
    """ncfdebt / |ncfo|: debt-funded operating shortfall ratio.
    Positive and rising = increasingly debt-funded operations."""
    return _safe_div(ncfdebt, ncfo.abs())


# --- Group C (031-045): Equity issuance patterns and buyback cessation (ncfcommon) ---

def cas_031_ncfcommon_level(ncfcommon: pd.Series) -> pd.Series:
    """Net cash from common equity issuance/repurchase — positive = dilutive raise, negative = buyback."""
    return ncfcommon.copy()


def cas_032_ncfcommon_positive_flag(ncfcommon: pd.Series) -> pd.Series:
    """1 if ncfcommon > 0: firm raising equity from market (distress-equity issuance signal)."""
    return (ncfcommon > 0).astype(float)


def cas_033_ncfcommon_negative_flag(ncfcommon: pd.Series) -> pd.Series:
    """1 if ncfcommon < 0: firm buying back shares (capital-return signal)."""
    return (ncfcommon < 0).astype(float)


def cas_034_ncfcommon_4q_sum(ncfcommon: pd.Series) -> pd.Series:
    """Trailing 4-quarter sum of ncfcommon — annual equity capital raised."""
    return _rolling_sum(ncfcommon, _TD_YEAR)


def cas_035_ncfcommon_8q_sum(ncfcommon: pd.Series) -> pd.Series:
    """Trailing 8-quarter cumulative ncfcommon."""
    return _rolling_sum(ncfcommon, _TD_2YR)


def cas_036_buyback_cessation_flag(ncfcommon: pd.Series) -> pd.Series:
    """1 if ncfcommon shifted from negative (buyback) to >=0 in current quarter — buyback cessation."""
    was_buying = (ncfcommon.shift(_TD_QTR) < 0)
    now_stopped = (ncfcommon >= 0)
    return (was_buying & now_stopped).astype(float)


def cas_037_buyback_reversal_flag(ncfcommon: pd.Series) -> pd.Series:
    """1 if ncfcommon shifted from negative to positive — buyback reversed to equity raise (severe stress)."""
    was_buying = (ncfcommon.shift(_TD_QTR) < 0)
    now_issuing = (ncfcommon > 0)
    return (was_buying & now_issuing).astype(float)


def cas_038_ncfcommon_qoq_change(ncfcommon: pd.Series) -> pd.Series:
    """QoQ change in ncfcommon — increasing positive = growing equity reliance."""
    return ncfcommon.diff(_TD_QTR)


def cas_039_ncfcommon_yoy_change(ncfcommon: pd.Series) -> pd.Series:
    """YoY change in ncfcommon."""
    return ncfcommon.diff(_TD_YEAR)


def cas_040_equity_issuance_quarters_4q(ncfcommon: pd.Series) -> pd.Series:
    """Count of quarters in trailing year with equity issuance (ncfcommon > 0)."""
    return _rolling_sum((ncfcommon > 0).astype(float), _TD_YEAR)


def cas_041_ncfcommon_pct_rank_8q(ncfcommon: pd.Series) -> pd.Series:
    """Percentile rank of ncfcommon within 8-quarter window (high rank = peak equity raising)."""
    return ncfcommon.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


def cas_042_ncfcommon_zscore_8q(ncfcommon: pd.Series) -> pd.Series:
    """Z-score of ncfcommon over trailing 8 quarters."""
    return _zscore_rolling(ncfcommon, _TD_2YR)


def cas_043_ncfcommon_to_equity_ratio(ncfcommon: pd.Series, equity: pd.Series) -> pd.Series:
    """TTM equity issuance / book equity — dilutive issuance intensity vs equity base."""
    ttm = _rolling_sum(ncfcommon, _TD_YEAR)
    return _safe_div(ttm, equity.abs())


def cas_044_ncfcommon_to_debt_ratio(ncfcommon: pd.Series, debt: pd.Series) -> pd.Series:
    """TTM equity raised / total debt — equity vs debt as capital source mix."""
    ttm = _rolling_sum(ncfcommon, _TD_YEAR)
    return _safe_div(ttm, debt.abs())


def cas_045_equity_replace_debt_flag(ncfcommon: pd.Series, ncfdebt: pd.Series) -> pd.Series:
    """1 if ncfcommon > 0 and ncfdebt < 0 — firm issuing equity to pay down debt (debt-constrained)."""
    return ((ncfcommon > 0) & (ncfdebt < 0)).astype(float)


# --- Group D (046-060): Dividend cuts as financing stress signals ---

def cas_046_dividends_level(dividends: pd.Series) -> pd.Series:
    """Total cash dividends paid (forward-filled quarterly; 0 = no dividend)."""
    return dividends.copy()


def cas_047_dividends_qoq_change(dividends: pd.Series) -> pd.Series:
    """QoQ change in total dividends paid (negative = cut, positive = increase)."""
    return dividends.diff(_TD_QTR)


def cas_048_dividends_yoy_change(dividends: pd.Series) -> pd.Series:
    """YoY change in total dividends paid."""
    return dividends.diff(_TD_YEAR)


def cas_049_dividend_cut_flag(dividends: pd.Series) -> pd.Series:
    """1 if dividends fell QoQ (dividend cut or suspension as financing stress signal)."""
    return (dividends.diff(_TD_QTR) < 0).astype(float)


def cas_050_dividend_suspension_flag(dividends: pd.Series) -> pd.Series:
    """1 if dividends dropped to zero from positive prior quarter (suspension)."""
    was_paying = (dividends.shift(_TD_QTR) > 0)
    now_zero   = (dividends <= 0)
    return (was_paying & now_zero).astype(float)


def cas_051_dividends_drawdown_from_4q_peak(dividends: pd.Series) -> pd.Series:
    """Dividends drawdown from trailing 4-quarter peak — cumulative cut severity."""
    peak = _rolling_max(dividends, _TD_YEAR)
    return _safe_div(dividends - peak, peak)


def cas_052_dividends_drawdown_from_2yr_peak(dividends: pd.Series) -> pd.Series:
    """Dividends drawdown from trailing 2-year peak."""
    peak = _rolling_max(dividends, _TD_2YR)
    return _safe_div(dividends - peak, peak)


def cas_053_capital_return_cessation_flag(dividends: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    """1 if both dividends <= 0 and ncfcommon >= 0 (no buybacks, no dividends — all capital-return stopped)."""
    return ((dividends <= 0) & (ncfcommon >= 0)).astype(float)


def cas_054_dividends_to_ncfo(dividends: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Dividends / |NCFO|: dividends as fraction of operating cash — sustainability ratio."""
    return _safe_div(dividends, ncfo.abs())


def cas_055_capital_return_to_ncfo(dividends: pd.Series, ncfcommon: pd.Series, ncfo: pd.Series) -> pd.Series:
    """(Dividends + |ncfcommon buybacks|) / |NCFO|: total capital-return burden on operating cash."""
    buybacks = (-ncfcommon).clip(lower=0)
    total_return = dividends + buybacks
    return _safe_div(total_return, ncfo.abs())


def cas_056_dps_level(dps: pd.Series) -> pd.Series:
    """Dividends per share (dps) level — per-share capital return measure."""
    return dps.copy()


def cas_057_dps_qoq_change(dps: pd.Series) -> pd.Series:
    """QoQ change in DPS — per-share dividend cut signal."""
    return dps.diff(_TD_QTR)


def cas_058_dps_yoy_change(dps: pd.Series) -> pd.Series:
    """YoY change in DPS."""
    return dps.diff(_TD_YEAR)


def cas_059_dps_drawdown_from_4q_peak(dps: pd.Series) -> pd.Series:
    """DPS drawdown from trailing 4-quarter peak."""
    peak = _rolling_max(dps, _TD_YEAR)
    return _safe_div(dps - peak, peak)


def cas_060_dps_pct_rank_8q(dps: pd.Series) -> pd.Series:
    """Percentile rank of DPS within 8-quarter window (low = at multi-year DPS low)."""
    return dps.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)


# --- Group E (061-075): Cash-burn vs available capital and debt balance ---

def cas_061_debt_level(debt: pd.Series) -> pd.Series:
    """Total debt outstanding — absolute size of debt financing."""
    return debt.copy()


def cas_062_debt_qoq_change(debt: pd.Series) -> pd.Series:
    """QoQ change in total debt (rising debt = increasing external reliance)."""
    return debt.diff(_TD_QTR)


def cas_063_debt_yoy_change(debt: pd.Series) -> pd.Series:
    """YoY change in total debt."""
    return debt.diff(_TD_YEAR)


def cas_064_debt_to_equity_ratio(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Total debt / book equity (leverage ratio — high = constrained external access)."""
    return _safe_div(debt, equity.abs())


def cas_065_debt_to_assets_ratio(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Total debt / total assets (solvency-adjusted leverage)."""
    return _safe_div(debt, assets)


def cas_066_net_debt(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Net debt: total debt - cash & equivalents (negative = net cash position)."""
    return debt - cashnequiv


def cas_067_net_debt_to_equity(debt: pd.Series, cashnequiv: pd.Series, equity: pd.Series) -> pd.Series:
    """Net debt / book equity — net leverage ratio."""
    net_debt = debt - cashnequiv
    return _safe_div(net_debt, equity.abs())


def cas_068_net_debt_to_ncfo(debt: pd.Series, cashnequiv: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Net debt / TTM operating cash flow — debt coverage in operating-cash years."""
    net_debt = debt - cashnequiv
    ncfo4q   = _rolling_sum(ncfo, _TD_YEAR)
    return _safe_div(net_debt, ncfo4q.abs())


def cas_069_cash_to_debt_ratio(cashnequiv: pd.Series, debt: pd.Series) -> pd.Series:
    """Cash / total debt — liquidity buffer against debt obligations."""
    return _safe_div(cashnequiv, debt)


def cas_070_debt_growth_rate_yoy(debt: pd.Series) -> pd.Series:
    """YoY percent change in total debt — debt accumulation speed."""
    prior = debt.shift(_TD_YEAR)
    return _safe_div(debt - prior, prior.abs())


def cas_071_debt_growth_pct_rank_4q(debt: pd.Series) -> pd.Series:
    """Percentile rank of YoY debt growth within trailing 4-quarter distribution."""
    growth = _safe_div(debt.diff(_TD_YEAR), debt.shift(_TD_YEAR).abs())
    return growth.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).rank(pct=True)


def cas_072_intexp_to_ncfo(intexp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Interest expense / |NCFO|: debt service burden relative to operating cash generation."""
    return _safe_div(intexp.abs(), ncfo.abs())


def cas_073_intexp_to_revenue(intexp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Interest expense / revenue: debt-service cost as fraction of revenue."""
    return _safe_div(intexp.abs(), revenue)


def cas_074_intexp_coverage_ratio(ncfo: pd.Series, intexp: pd.Series) -> pd.Series:
    """NCFO / |intexp|: operating-cash coverage of interest expense.
    < 1 = operating cash insufficient to cover interest (severe stress)."""
    return _safe_div(ncfo, intexp.abs())


def cas_075_external_financing_composite(ncff: pd.Series, ncfdebt: pd.Series,
                                         ncfcommon: pd.Series, debt: pd.Series,
                                         equity: pd.Series) -> pd.Series:
    """Composite external-financing stress: normalized sum of external-capital reliance signals.
    Higher = more external capital stressed (relies heavily on external sources with rising leverage)."""
    ncff_rank    = ncff.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)
    ncfdebt_rank = ncfdebt.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)
    ncfcommon_rank = ncfcommon.rolling(_TD_2YR, min_periods=max(2, _TD_2YR // 4)).rank(pct=True)
    lev = _safe_div(debt, equity.abs()).fillna(0).clip(lower=0, upper=10) / 10.0
    return (0.35 * ncff_rank.fillna(0.5) +
            0.25 * ncfdebt_rank.fillna(0.5) +
            0.25 * ncfcommon_rank.fillna(0.5) +
            0.15 * lev)


# ── Registry ──────────────────────────────────────────────────────────────────

CAPITAL_ACCESS_STRESS_REGISTRY_001_075 = {
    "cas_001_ncff_level":                    {"inputs": ["ncff"],                              "func": cas_001_ncff_level},
    "cas_002_ncff_positive_flag":            {"inputs": ["ncff"],                              "func": cas_002_ncff_positive_flag},
    "cas_003_ncff_4q_sum":                   {"inputs": ["ncff"],                              "func": cas_003_ncff_4q_sum},
    "cas_004_ncff_8q_sum":                   {"inputs": ["ncff"],                              "func": cas_004_ncff_8q_sum},
    "cas_005_ncff_vs_ncfo_ratio":            {"inputs": ["ncff", "ncfo"],                      "func": cas_005_ncff_vs_ncfo_ratio},
    "cas_006_ncff_vs_ncfo_ttm_ratio":        {"inputs": ["ncff", "ncfo"],                      "func": cas_006_ncff_vs_ncfo_ttm_ratio},
    "cas_007_external_funding_dependence":   {"inputs": ["ncff", "ncfo"],                      "func": cas_007_external_funding_dependence},
    "cas_008_ncff_drawdown_from_4q_peak":    {"inputs": ["ncff"],                              "func": cas_008_ncff_drawdown_from_4q_peak},
    "cas_009_ncff_drawdown_from_2yr_peak":   {"inputs": ["ncff"],                              "func": cas_009_ncff_drawdown_from_2yr_peak},
    "cas_010_ncff_qoq_change":               {"inputs": ["ncff"],                              "func": cas_010_ncff_qoq_change},
    "cas_011_ncff_yoy_change":               {"inputs": ["ncff"],                              "func": cas_011_ncff_yoy_change},
    "cas_012_ncff_4q_negative_fraction":     {"inputs": ["ncff"],                              "func": cas_012_ncff_4q_negative_fraction},
    "cas_013_ncff_pct_rank_8q":              {"inputs": ["ncff"],                              "func": cas_013_ncff_pct_rank_8q},
    "cas_014_ncff_zscore_8q":                {"inputs": ["ncff"],                              "func": cas_014_ncff_zscore_8q},
    "cas_015_ncff_to_revenue":               {"inputs": ["ncff", "revenue"],                   "func": cas_015_ncff_to_revenue},
    "cas_016_ncfdebt_level":                 {"inputs": ["ncfdebt"],                           "func": cas_016_ncfdebt_level},
    "cas_017_ncfdebt_positive_flag":         {"inputs": ["ncfdebt"],                           "func": cas_017_ncfdebt_positive_flag},
    "cas_018_ncfdebt_negative_flag":         {"inputs": ["ncfdebt"],                           "func": cas_018_ncfdebt_negative_flag},
    "cas_019_ncfdebt_4q_sum":                {"inputs": ["ncfdebt"],                           "func": cas_019_ncfdebt_4q_sum},
    "cas_020_ncfdebt_8q_sum":                {"inputs": ["ncfdebt"],                           "func": cas_020_ncfdebt_8q_sum},
    "cas_021_ncfdebt_qoq_change":            {"inputs": ["ncfdebt"],                           "func": cas_021_ncfdebt_qoq_change},
    "cas_022_ncfdebt_yoy_change":            {"inputs": ["ncfdebt"],                           "func": cas_022_ncfdebt_yoy_change},
    "cas_023_ncfdebt_drawdown_from_4q_peak": {"inputs": ["ncfdebt"],                           "func": cas_023_ncfdebt_drawdown_from_4q_peak},
    "cas_024_ncfdebt_pct_rank_8q":           {"inputs": ["ncfdebt"],                           "func": cas_024_ncfdebt_pct_rank_8q},
    "cas_025_ncfdebt_zscore_8q":             {"inputs": ["ncfdebt"],                           "func": cas_025_ncfdebt_zscore_8q},
    "cas_026_debt_issuance_fraction_4q":     {"inputs": ["ncfdebt"],                           "func": cas_026_debt_issuance_fraction_4q},
    "cas_027_ncfdebt_to_debt_ratio":         {"inputs": ["ncfdebt", "debt"],                   "func": cas_027_ncfdebt_to_debt_ratio},
    "cas_028_debt_repayment_spike_flag":     {"inputs": ["ncfdebt"],                           "func": cas_028_debt_repayment_spike_flag},
    "cas_029_ncfdebt_negative_4q_count":     {"inputs": ["ncfdebt"],                           "func": cas_029_ncfdebt_negative_4q_count},
    "cas_030_ncfdebt_vs_ncfo":               {"inputs": ["ncfdebt", "ncfo"],                   "func": cas_030_ncfdebt_vs_ncfo},
    "cas_031_ncfcommon_level":               {"inputs": ["ncfcommon"],                         "func": cas_031_ncfcommon_level},
    "cas_032_ncfcommon_positive_flag":       {"inputs": ["ncfcommon"],                         "func": cas_032_ncfcommon_positive_flag},
    "cas_033_ncfcommon_negative_flag":       {"inputs": ["ncfcommon"],                         "func": cas_033_ncfcommon_negative_flag},
    "cas_034_ncfcommon_4q_sum":              {"inputs": ["ncfcommon"],                         "func": cas_034_ncfcommon_4q_sum},
    "cas_035_ncfcommon_8q_sum":              {"inputs": ["ncfcommon"],                         "func": cas_035_ncfcommon_8q_sum},
    "cas_036_buyback_cessation_flag":        {"inputs": ["ncfcommon"],                         "func": cas_036_buyback_cessation_flag},
    "cas_037_buyback_reversal_flag":         {"inputs": ["ncfcommon"],                         "func": cas_037_buyback_reversal_flag},
    "cas_038_ncfcommon_qoq_change":          {"inputs": ["ncfcommon"],                         "func": cas_038_ncfcommon_qoq_change},
    "cas_039_ncfcommon_yoy_change":          {"inputs": ["ncfcommon"],                         "func": cas_039_ncfcommon_yoy_change},
    "cas_040_equity_issuance_quarters_4q":   {"inputs": ["ncfcommon"],                         "func": cas_040_equity_issuance_quarters_4q},
    "cas_041_ncfcommon_pct_rank_8q":         {"inputs": ["ncfcommon"],                         "func": cas_041_ncfcommon_pct_rank_8q},
    "cas_042_ncfcommon_zscore_8q":           {"inputs": ["ncfcommon"],                         "func": cas_042_ncfcommon_zscore_8q},
    "cas_043_ncfcommon_to_equity_ratio":     {"inputs": ["ncfcommon", "equity"],               "func": cas_043_ncfcommon_to_equity_ratio},
    "cas_044_ncfcommon_to_debt_ratio":       {"inputs": ["ncfcommon", "debt"],                 "func": cas_044_ncfcommon_to_debt_ratio},
    "cas_045_equity_replace_debt_flag":      {"inputs": ["ncfcommon", "ncfdebt"],              "func": cas_045_equity_replace_debt_flag},
    "cas_046_dividends_level":               {"inputs": ["dividends"],                         "func": cas_046_dividends_level},
    "cas_047_dividends_qoq_change":          {"inputs": ["dividends"],                         "func": cas_047_dividends_qoq_change},
    "cas_048_dividends_yoy_change":          {"inputs": ["dividends"],                         "func": cas_048_dividends_yoy_change},
    "cas_049_dividend_cut_flag":             {"inputs": ["dividends"],                         "func": cas_049_dividend_cut_flag},
    "cas_050_dividend_suspension_flag":      {"inputs": ["dividends"],                         "func": cas_050_dividend_suspension_flag},
    "cas_051_dividends_drawdown_from_4q_peak": {"inputs": ["dividends"],                       "func": cas_051_dividends_drawdown_from_4q_peak},
    "cas_052_dividends_drawdown_from_2yr_peak": {"inputs": ["dividends"],                      "func": cas_052_dividends_drawdown_from_2yr_peak},
    "cas_053_capital_return_cessation_flag": {"inputs": ["dividends", "ncfcommon"],            "func": cas_053_capital_return_cessation_flag},
    "cas_054_dividends_to_ncfo":             {"inputs": ["dividends", "ncfo"],                 "func": cas_054_dividends_to_ncfo},
    "cas_055_capital_return_to_ncfo":        {"inputs": ["dividends", "ncfcommon", "ncfo"],    "func": cas_055_capital_return_to_ncfo},
    "cas_056_dps_level":                     {"inputs": ["dps"],                               "func": cas_056_dps_level},
    "cas_057_dps_qoq_change":                {"inputs": ["dps"],                               "func": cas_057_dps_qoq_change},
    "cas_058_dps_yoy_change":                {"inputs": ["dps"],                               "func": cas_058_dps_yoy_change},
    "cas_059_dps_drawdown_from_4q_peak":     {"inputs": ["dps"],                               "func": cas_059_dps_drawdown_from_4q_peak},
    "cas_060_dps_pct_rank_8q":               {"inputs": ["dps"],                               "func": cas_060_dps_pct_rank_8q},
    "cas_061_debt_level":                    {"inputs": ["debt"],                              "func": cas_061_debt_level},
    "cas_062_debt_qoq_change":               {"inputs": ["debt"],                              "func": cas_062_debt_qoq_change},
    "cas_063_debt_yoy_change":               {"inputs": ["debt"],                              "func": cas_063_debt_yoy_change},
    "cas_064_debt_to_equity_ratio":          {"inputs": ["debt", "equity"],                    "func": cas_064_debt_to_equity_ratio},
    "cas_065_debt_to_assets_ratio":          {"inputs": ["debt", "assets"],                    "func": cas_065_debt_to_assets_ratio},
    "cas_066_net_debt":                      {"inputs": ["debt", "cashnequiv"],                "func": cas_066_net_debt},
    "cas_067_net_debt_to_equity":            {"inputs": ["debt", "cashnequiv", "equity"],      "func": cas_067_net_debt_to_equity},
    "cas_068_net_debt_to_ncfo":              {"inputs": ["debt", "cashnequiv", "ncfo"],        "func": cas_068_net_debt_to_ncfo},
    "cas_069_cash_to_debt_ratio":            {"inputs": ["cashnequiv", "debt"],                "func": cas_069_cash_to_debt_ratio},
    "cas_070_debt_growth_rate_yoy":          {"inputs": ["debt"],                              "func": cas_070_debt_growth_rate_yoy},
    "cas_071_debt_growth_pct_rank_4q":       {"inputs": ["debt"],                              "func": cas_071_debt_growth_pct_rank_4q},
    "cas_072_intexp_to_ncfo":                {"inputs": ["intexp", "ncfo"],                    "func": cas_072_intexp_to_ncfo},
    "cas_073_intexp_to_revenue":             {"inputs": ["intexp", "revenue"],                 "func": cas_073_intexp_to_revenue},
    "cas_074_intexp_coverage_ratio":         {"inputs": ["ncfo", "intexp"],                    "func": cas_074_intexp_coverage_ratio},
    "cas_075_external_financing_composite":  {"inputs": ["ncff", "ncfdebt", "ncfcommon", "debt", "equity"], "func": cas_075_external_financing_composite},
}
