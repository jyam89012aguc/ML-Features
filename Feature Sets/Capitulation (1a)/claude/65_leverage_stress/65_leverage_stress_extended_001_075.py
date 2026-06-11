"""
65_leverage_stress — Extended Features 001-075
Domain: debt/equity and debt/assets escalation, capital-structure stress —
        deeper variants, additional windows, EWM deviations, z-scores,
        percentile ranks, streaks, acceleration, composites.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract: inputs are already daily-frequency
Series forward-filled from the most recent quarterly SF1 report. Functions
look strictly backward. 1 quarter = 63 trading days, 1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ──────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_HALF = 126
_TD_QTR  = 63
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_EPS     = 1e-9

# ── Alignment helper ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    return q_series.reindex(daily_index).ffill()

# ── Utility helpers ────────────────────────────────────────────────────────────

def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    return num / den.abs().replace(0, np.nan)


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


def _rolling_rank_pct(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).rank(pct=True)


def _zscore_rolling(s: pd.Series, w: int) -> pd.Series:
    m  = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _linslope(s: pd.Series, w: int) -> pd.Series:
    def _slope(x):
        vals = x[~np.isnan(x)]
        n = len(vals)
        if n < 2: return np.nan
        xi = np.arange(n, dtype=float)
        xm = xi.mean(); vm = vals.mean()
        num = ((xi - xm) * (vals - vm)).sum()
        den = ((xi - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(w, min_periods=max(2, w // 4)).apply(_slope, raw=False)


# ── Feature functions 001-075 ──────────────────────────────────────────────────

# --- Group A (001-012): Additional windows and smoothings for D/E and D/A ---

def lvs_ext_001_debt_to_equity_min_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Minimum (best case) D/E in trailing 4Q window — how low leverage has been recently."""
    return _rolling_min(_safe_div(debt, equity), _TD_YEAR)


def lvs_ext_002_debt_to_equity_max_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Maximum (worst case) D/E in trailing 8Q window."""
    return _rolling_max(_safe_div(debt, equity), _TD_2Y)


def lvs_ext_003_debt_to_equity_max_12q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Maximum D/E in trailing 12Q (3-year) window."""
    return _rolling_max(_safe_div(debt, equity), _TD_3Y)


def lvs_ext_004_debt_to_equity_expanding_max(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """All-history expanding maximum D/E ratio (worst-ever leverage level)."""
    ratio = _safe_div(debt, equity)
    return ratio.expanding(min_periods=1).max()


def lvs_ext_005_debt_to_equity_median_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Trailing 4Q median D/E ratio (robust central tendency of leverage)."""
    return _rolling_median(_safe_div(debt, equity), _TD_YEAR)


def lvs_ext_006_debt_to_assets_max_8q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Maximum D/A ratio in trailing 8Q window."""
    return _rolling_max(_safe_div(debt, assets), _TD_2Y)


def lvs_ext_007_debt_to_assets_max_12q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Maximum D/A ratio in trailing 12Q window."""
    return _rolling_max(_safe_div(debt, assets), _TD_3Y)


def lvs_ext_008_debt_to_assets_expanding_max(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """All-history expanding maximum D/A ratio."""
    ratio = _safe_div(debt, assets)
    return ratio.expanding(min_periods=1).max()


def lvs_ext_009_liabilities_to_assets_max_8q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Maximum L/A ratio in trailing 8Q window."""
    return _rolling_max(_safe_div(liabilities, assets), _TD_2Y)


def lvs_ext_010_liabilities_to_equity_max_4q(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Maximum liabilities/equity in trailing 4Q window."""
    return _rolling_max(_safe_div(liabilities, equity), _TD_YEAR)


def lvs_ext_011_net_debt_to_ebitda_max_8q(debt: pd.Series, cashnequiv: pd.Series,
                                           ebitda: pd.Series) -> pd.Series:
    """Maximum net-D/EBITDA in trailing 8Q window."""
    ratio = _safe_div(debt - cashnequiv, ebitda)
    return _rolling_max(ratio, _TD_2Y)


def lvs_ext_012_debt_to_equity_range_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """8Q range of D/E ratio: max - min (leverage volatility)."""
    ratio = _safe_div(debt, equity)
    return _rolling_max(ratio, _TD_2Y) - _rolling_min(ratio, _TD_2Y)


# --- Group B (013-024): Z-score extensions ---

def lvs_ext_013_debt_to_equity_zscore_12q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of D/E ratio within trailing 12-quarter (3-year) window."""
    return _zscore_rolling(_safe_div(debt, equity), _TD_3Y)


def lvs_ext_014_debt_to_equity_expanding_zscore(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """All-history expanding z-score of D/E ratio."""
    ratio = _safe_div(debt, equity)
    m  = ratio.expanding(min_periods=2).mean()
    sd = ratio.expanding(min_periods=2).std()
    return _safe_div(ratio - m, sd)


def lvs_ext_015_debt_to_assets_zscore_8q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of D/A ratio within trailing 8Q window."""
    return _zscore_rolling(_safe_div(debt, assets), _TD_2Y)


def lvs_ext_016_debt_to_assets_zscore_12q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of D/A ratio within trailing 12Q window."""
    return _zscore_rolling(_safe_div(debt, assets), _TD_3Y)


def lvs_ext_017_liabilities_to_assets_zscore_4q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of L/A ratio within 4-quarter window."""
    return _zscore_rolling(_safe_div(liabilities, assets), _TD_YEAR)


def lvs_ext_018_liabilities_to_assets_zscore_8q(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Z-score of L/A ratio within 8-quarter window."""
    return _zscore_rolling(_safe_div(liabilities, assets), _TD_2Y)


def lvs_ext_019_net_debt_to_ebitda_zscore_8q(debt: pd.Series, cashnequiv: pd.Series,
                                              ebitda: pd.Series) -> pd.Series:
    """Z-score of net-D/EBITDA within 8-quarter window."""
    ratio = _safe_div(debt - cashnequiv, ebitda)
    return _zscore_rolling(ratio, _TD_2Y)


def lvs_ext_020_financial_leverage_zscore_8q(assets: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of financial leverage (assets/equity) within 8-quarter window."""
    return _zscore_rolling(_safe_div(assets, equity), _TD_2Y)


def lvs_ext_021_liabilities_to_equity_zscore_4q(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of liabilities/equity within 4-quarter window."""
    return _zscore_rolling(_safe_div(liabilities, equity), _TD_YEAR)


def lvs_ext_022_liabilities_to_equity_zscore_8q(liabilities: pd.Series, equity: pd.Series) -> pd.Series:
    """Z-score of liabilities/equity within 8-quarter window."""
    return _zscore_rolling(_safe_div(liabilities, equity), _TD_2Y)


def lvs_ext_023_debt_to_equity_expanding_pct_rank(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """All-history expanding percentile rank of D/E ratio."""
    ratio = _safe_div(debt, equity)
    return ratio.expanding(min_periods=2).rank(pct=True)


def lvs_ext_024_debt_to_assets_pct_rank_8q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Percentile rank of D/A ratio within trailing 8Q window."""
    return _rolling_rank_pct(_safe_div(debt, assets), _TD_2Y)


# --- Group C (025-036): Additional flags, streaks, and regime signals ---

def lvs_ext_025_leverage_above_1x_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Binary: 1 if D/E > 1.0."""
    return (_safe_div(debt, equity) > 1.0).astype(float)


def lvs_ext_026_leverage_above_3x_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Binary: 1 if D/E > 3.0."""
    return (_safe_div(debt, equity) > 3.0).astype(float)


def lvs_ext_027_leverage_above_6x_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Binary: 1 if D/E > 6.0 (extreme leverage)."""
    return (_safe_div(debt, equity) > 6.0).astype(float)


def lvs_ext_028_debt_to_assets_above_60pct_flag(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Binary: 1 if D/A > 0.60."""
    return (_safe_div(debt, assets) > 0.60).astype(float)


def lvs_ext_029_debt_to_assets_above_80pct_flag(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Binary: 1 if D/A > 0.80 (very high asset leverage)."""
    return (_safe_div(debt, assets) > 0.80).astype(float)


def lvs_ext_030_liabilities_to_assets_above_80pct_flag(liabilities: pd.Series,
                                                        assets: pd.Series) -> pd.Series:
    """Binary: 1 if L/A > 0.80."""
    return (_safe_div(liabilities, assets) > 0.80).astype(float)


def lvs_ext_031_leverage_above_4x_fraction_1y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Fraction of trailing 252-day window where D/E > 4.0."""
    above = (_safe_div(debt, equity) > 4.0).astype(float)
    return _rolling_mean(above, _TD_YEAR)


def lvs_ext_032_leverage_above_4x_fraction_3y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Fraction of trailing 756-day window where D/E > 4.0."""
    above = (_safe_div(debt, equity) > 4.0).astype(float)
    return _rolling_mean(above, _TD_3Y)


def lvs_ext_033_negative_equity_fraction_2y(equity: pd.Series) -> pd.Series:
    """Fraction of trailing 2-year window with negative equity."""
    return _rolling_mean((equity < 0).astype(float), _TD_2Y)


def lvs_ext_034_consecutive_rising_da_qtrs(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """Consecutive quarters where D/A ratio has risen (streak length)."""
    ratio = _safe_div(debt, assets)
    rose  = (ratio > ratio.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(rose), dtype=float)
    arr = rose.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=debt.index)


def lvs_ext_035_consecutive_rising_liab_equity_qtrs(liabilities: pd.Series,
                                                     equity: pd.Series) -> pd.Series:
    """Consecutive quarters where liabilities/equity ratio has risen."""
    ratio = _safe_div(liabilities, equity)
    rose  = (ratio > ratio.shift(_TD_QTR)).astype(int)
    streak = np.zeros(len(rose), dtype=float)
    arr = rose.values
    for i in range(1, len(arr)):
        streak[i] = (streak[i - 1] + 1) * arr[i]
    return pd.Series(streak, index=liabilities.index)


def lvs_ext_036_debt_grew_equity_fell_2y_flag(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """1 if debt rose over 2 years AND equity fell over 2 years simultaneously."""
    debt_grew   = (debt   > debt.shift(_TD_2Y)).astype(float)
    equity_fell = (equity < equity.shift(_TD_2Y)).astype(float)
    return debt_grew * equity_fell


# --- Group D (037-048): Trend slope and acceleration ---

def lvs_ext_037_debt_to_equity_trend_slope_4q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """OLS slope of D/E ratio over trailing 4 quarters."""
    return _linslope(_safe_div(debt, equity), _TD_YEAR)


def lvs_ext_038_debt_to_equity_trend_slope_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """OLS slope of D/E ratio over trailing 8 quarters."""
    return _linslope(_safe_div(debt, equity), _TD_2Y)


def lvs_ext_039_debt_to_assets_trend_slope_4q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """OLS slope of D/A ratio over trailing 4 quarters."""
    return _linslope(_safe_div(debt, assets), _TD_YEAR)


def lvs_ext_040_net_debt_trend_slope_4q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """OLS slope of net debt level over trailing 4 quarters."""
    return _linslope(debt - cashnequiv, _TD_YEAR)


def lvs_ext_041_debt_to_equity_qoq_acceleration(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Second difference of D/E ratio (QoQ change in QoQ change = acceleration)."""
    ratio = _safe_div(debt, equity)
    d1    = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_ext_042_debt_to_assets_qoq_acceleration(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """QoQ acceleration of D/A ratio (second difference)."""
    ratio = _safe_div(debt, assets)
    d1    = ratio - ratio.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_ext_043_net_debt_qoq_acceleration(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """QoQ acceleration of net debt level (second difference)."""
    nd = debt - cashnequiv
    d1 = nd - nd.shift(_TD_QTR)
    return d1 - d1.shift(_TD_QTR)


def lvs_ext_044_debt_to_ebitda_zscore_8q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Z-score of D/EBITDA within trailing 8-quarter window."""
    return _zscore_rolling(_safe_div(debt, ebitda), _TD_2Y)


def lvs_ext_045_debt_to_ebitda_pct_rank_4q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Pct rank of D/EBITDA within trailing 4-quarter window."""
    return _rolling_rank_pct(_safe_div(debt, ebitda), _TD_YEAR)


def lvs_ext_046_debt_to_ebitda_pct_rank_8q(debt: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Pct rank of D/EBITDA within trailing 8-quarter window."""
    return _rolling_rank_pct(_safe_div(debt, ebitda), _TD_2Y)


def lvs_ext_047_leverage_ewm_deviation_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio minus its 8-quarter EWM (span=504) — slow-momentum deviation."""
    ratio = _safe_div(debt, equity)
    ewm   = _ewm_mean(ratio, _TD_2Y)
    return ratio - ewm


def lvs_ext_048_debt_to_assets_ewm_deviation_8q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """D/A ratio minus its 8-quarter EWM (span=504)."""
    ratio = _safe_div(debt, assets)
    ewm   = _ewm_mean(ratio, _TD_2Y)
    return ratio - ewm


# --- Group E (049-060): Net debt extended and cross-ratios ---

def lvs_ext_049_net_debt_pct_rank_4q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Pct rank of net debt level within trailing 4-quarter window."""
    nd = debt - cashnequiv
    return _rolling_rank_pct(nd, _TD_YEAR)


def lvs_ext_050_net_debt_pct_rank_8q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Pct rank of net debt level within trailing 8-quarter window."""
    nd = debt - cashnequiv
    return _rolling_rank_pct(nd, _TD_2Y)


def lvs_ext_051_net_debt_zscore_4q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Z-score of net debt level within trailing 4-quarter window."""
    nd = debt - cashnequiv
    return _zscore_rolling(nd, _TD_YEAR)


def lvs_ext_052_net_debt_zscore_8q(debt: pd.Series, cashnequiv: pd.Series) -> pd.Series:
    """Z-score of net debt level within trailing 8-quarter window."""
    nd = debt - cashnequiv
    return _zscore_rolling(nd, _TD_2Y)


def lvs_ext_053_net_debt_to_equity_pct_rank_4q(debt: pd.Series, cashnequiv: pd.Series,
                                                equity: pd.Series) -> pd.Series:
    """Pct rank of net-D/E ratio within trailing 4-quarter window."""
    ratio = _safe_div(debt - cashnequiv, equity)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def lvs_ext_054_net_debt_to_equity_pct_rank_8q(debt: pd.Series, cashnequiv: pd.Series,
                                                equity: pd.Series) -> pd.Series:
    """Pct rank of net-D/E ratio within trailing 8-quarter window."""
    ratio = _safe_div(debt - cashnequiv, equity)
    return _rolling_rank_pct(ratio, _TD_2Y)


def lvs_ext_055_short_term_debt_mix_zscore_4q(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """Z-score of short-term debt fraction within 4-quarter window."""
    ratio = _safe_div(debtc, debt)
    return _zscore_rolling(ratio, _TD_YEAR)


def lvs_ext_056_short_term_debt_mix_pct_rank_4q(debtc: pd.Series, debt: pd.Series) -> pd.Series:
    """Pct rank of short-term debt fraction within 4-quarter window."""
    ratio = _safe_div(debtc, debt)
    return _rolling_rank_pct(ratio, _TD_YEAR)


def lvs_ext_057_debt_to_equity_range_position_8q(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio position within its 8-quarter [min, max] range: (ratio-min)/(max-min)."""
    ratio = _safe_div(debt, equity)
    lo = _rolling_min(ratio, _TD_2Y)
    hi = _rolling_max(ratio, _TD_2Y)
    return _safe_div(ratio - lo, hi - lo)


def lvs_ext_058_debt_to_assets_range_position_8q(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """D/A ratio position within its 8-quarter [min, max] range."""
    ratio = _safe_div(debt, assets)
    lo = _rolling_min(ratio, _TD_2Y)
    hi = _rolling_max(ratio, _TD_2Y)
    return _safe_div(ratio - lo, hi - lo)


def lvs_ext_059_noncurrent_liab_to_assets_zscore_4q(liabilitiesnc: pd.Series,
                                                     assets: pd.Series) -> pd.Series:
    """Z-score of non-current liabilities/assets within 4-quarter window."""
    return _zscore_rolling(_safe_div(liabilitiesnc, assets), _TD_YEAR)


def lvs_ext_060_debtnc_to_debt_yoy_change(debtnc: pd.Series, debt: pd.Series) -> pd.Series:
    """YoY change in long-term debt mix (debtnc/debt)."""
    ratio = _safe_div(debtnc, debt)
    return ratio - ratio.shift(_TD_YEAR)


# --- Group F (061-070): Expanding metrics and cross-cycle ---

def lvs_ext_061_debt_to_assets_expanding_pct_rank(debt: pd.Series, assets: pd.Series) -> pd.Series:
    """All-history expanding pct rank of D/A ratio."""
    ratio = _safe_div(debt, assets)
    return ratio.expanding(min_periods=2).rank(pct=True)


def lvs_ext_062_liabilities_to_assets_expanding_pct_rank(liabilities: pd.Series,
                                                          assets: pd.Series) -> pd.Series:
    """All-history expanding pct rank of L/A ratio."""
    ratio = _safe_div(liabilities, assets)
    return ratio.expanding(min_periods=2).rank(pct=True)


def lvs_ext_063_net_debt_to_ebitda_expanding_pct_rank(debt: pd.Series, cashnequiv: pd.Series,
                                                       ebitda: pd.Series) -> pd.Series:
    """All-history expanding pct rank of net-D/EBITDA."""
    ratio = _safe_div(debt - cashnequiv, ebitda)
    return ratio.expanding(min_periods=2).rank(pct=True)


def lvs_ext_064_debt_to_equity_4y_change(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E ratio change over approx 4 years (1008 days, 16 quarters)."""
    ratio = _safe_div(debt, equity)
    return ratio - ratio.shift(4 * _TD_YEAR // 4 * 4)  # ~1008 days


def lvs_ext_065_debt_yoy_pct_rank_4q(debt: pd.Series) -> pd.Series:
    """Pct rank of YoY debt growth rate within trailing 4-quarter window."""
    pct  = _safe_div_abs(debt - debt.shift(_TD_YEAR), debt.shift(_TD_YEAR))
    return _rolling_rank_pct(pct, _TD_YEAR)


def lvs_ext_066_equity_yoy_change(equity: pd.Series) -> pd.Series:
    """YoY absolute change in equity (declining equity = capital erosion)."""
    return equity - equity.shift(_TD_YEAR)


def lvs_ext_067_equity_pct_rank_4q(equity: pd.Series) -> pd.Series:
    """Pct rank of equity level within trailing 4-quarter window."""
    return _rolling_rank_pct(equity, _TD_YEAR)


def lvs_ext_068_equity_pct_rank_8q(equity: pd.Series) -> pd.Series:
    """Pct rank of equity level within trailing 8-quarter window."""
    return _rolling_rank_pct(equity, _TD_2Y)


def lvs_ext_069_equity_drawdown_from_4q_peak(equity: pd.Series) -> pd.Series:
    """Equity level drawdown from its 4-quarter rolling peak."""
    peak = _rolling_max(equity, _TD_YEAR)
    return _safe_div_abs(equity - peak, peak)


def lvs_ext_070_equity_drawdown_from_expanding_peak(equity: pd.Series) -> pd.Series:
    """Equity percent drawdown from its all-history expanding peak."""
    peak = equity.expanding(min_periods=1).max()
    return _safe_div_abs(equity - peak, peak)


# --- Group G (071-075): Multi-signal composites ---

def lvs_ext_071_leverage_stress_composite_8q(debt: pd.Series, equity: pd.Series,
                                             assets: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Composite leverage-stress score (z-scores in 8Q window).
    (z_DE + z_DA + z_D_EBITDA) / 3. Positive = leverage above 2-year norm."""
    z_de  = _zscore_rolling(_safe_div(debt, equity),  _TD_2Y)
    z_da  = _zscore_rolling(_safe_div(debt, assets),  _TD_2Y)
    z_deb = _zscore_rolling(_safe_div(debt, ebitda),  _TD_2Y)
    return (z_de + z_da + z_deb) / 3.0


def lvs_ext_072_leverage_capitulation_composite(debt: pd.Series, equity: pd.Series,
                                                assets: pd.Series) -> pd.Series:
    """Weighted composite pct-rank: 0.5*(DE_rank) + 0.3*(DA_rank) + 0.2*(L/A_rank)
    in 8Q window. Higher = leverage near worst recent level."""
    r_de  = _rolling_rank_pct(_safe_div(debt, equity),  _TD_2Y)
    r_da  = _rolling_rank_pct(_safe_div(debt, assets),  _TD_2Y)
    r_la  = _rolling_rank_pct(_safe_div(debt + equity - assets, assets), _TD_2Y)
    return 0.5 * r_de + 0.3 * r_da + 0.2 * r_la


def lvs_ext_073_leverage_multi_flag_score(debt: pd.Series, equity: pd.Series,
                                          assets: pd.Series) -> pd.Series:
    """Count of simultaneous stress flags: D/E>2, D/A>0.5, L/A>0.7.
    0-3 scale; 3 = all flags triggered (maximum leverage stress)."""
    f1 = (_safe_div(debt, equity) > 2.0).astype(float)
    f2 = (_safe_div(debt, assets) > 0.5).astype(float)
    la = _safe_div(debt + (assets - debt - equity).abs(), assets)
    f3 = (la > 0.7).astype(float)
    return f1 + f2 + f3


def lvs_ext_074_net_debt_to_equity_expanding_zscore(debt: pd.Series, cashnequiv: pd.Series,
                                                    equity: pd.Series) -> pd.Series:
    """All-history expanding z-score of net-D/E ratio."""
    ratio = _safe_div(debt - cashnequiv, equity)
    m  = ratio.expanding(min_periods=2).mean()
    sd = ratio.expanding(min_periods=2).std()
    return _safe_div(ratio - m, sd)


def lvs_ext_075_leverage_cycle_position(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """D/E position within its 12-quarter [min, max] range: (ratio-min)/(max-min).
    1.0 = at 3-year leverage high (worst level); 0.0 = at 3-year low."""
    ratio = _safe_div(debt, equity)
    lo = _rolling_min(ratio, _TD_3Y)
    hi = _rolling_max(ratio, _TD_3Y)
    return _safe_div(ratio - lo, hi - lo)


# ── Registry ───────────────────────────────────────────────────────────────────

LEVERAGE_STRESS_EXTENDED_REGISTRY_001_075 = {
    "lvs_ext_001_debt_to_equity_min_4q":               {"inputs": ["debt", "equity"],                           "func": lvs_ext_001_debt_to_equity_min_4q},
    "lvs_ext_002_debt_to_equity_max_8q":               {"inputs": ["debt", "equity"],                           "func": lvs_ext_002_debt_to_equity_max_8q},
    "lvs_ext_003_debt_to_equity_max_12q":              {"inputs": ["debt", "equity"],                           "func": lvs_ext_003_debt_to_equity_max_12q},
    "lvs_ext_004_debt_to_equity_expanding_max":        {"inputs": ["debt", "equity"],                           "func": lvs_ext_004_debt_to_equity_expanding_max},
    "lvs_ext_005_debt_to_equity_median_4q":            {"inputs": ["debt", "equity"],                           "func": lvs_ext_005_debt_to_equity_median_4q},
    "lvs_ext_006_debt_to_assets_max_8q":               {"inputs": ["debt", "assets"],                           "func": lvs_ext_006_debt_to_assets_max_8q},
    "lvs_ext_007_debt_to_assets_max_12q":              {"inputs": ["debt", "assets"],                           "func": lvs_ext_007_debt_to_assets_max_12q},
    "lvs_ext_008_debt_to_assets_expanding_max":        {"inputs": ["debt", "assets"],                           "func": lvs_ext_008_debt_to_assets_expanding_max},
    "lvs_ext_009_liabilities_to_assets_max_8q":        {"inputs": ["liabilities", "assets"],                    "func": lvs_ext_009_liabilities_to_assets_max_8q},
    "lvs_ext_010_liabilities_to_equity_max_4q":        {"inputs": ["liabilities", "equity"],                    "func": lvs_ext_010_liabilities_to_equity_max_4q},
    "lvs_ext_011_net_debt_to_ebitda_max_8q":           {"inputs": ["debt", "cashnequiv", "ebitda"],             "func": lvs_ext_011_net_debt_to_ebitda_max_8q},
    "lvs_ext_012_debt_to_equity_range_8q":             {"inputs": ["debt", "equity"],                           "func": lvs_ext_012_debt_to_equity_range_8q},
    "lvs_ext_013_debt_to_equity_zscore_12q":           {"inputs": ["debt", "equity"],                           "func": lvs_ext_013_debt_to_equity_zscore_12q},
    "lvs_ext_014_debt_to_equity_expanding_zscore":     {"inputs": ["debt", "equity"],                           "func": lvs_ext_014_debt_to_equity_expanding_zscore},
    "lvs_ext_015_debt_to_assets_zscore_8q":            {"inputs": ["debt", "assets"],                           "func": lvs_ext_015_debt_to_assets_zscore_8q},
    "lvs_ext_016_debt_to_assets_zscore_12q":           {"inputs": ["debt", "assets"],                           "func": lvs_ext_016_debt_to_assets_zscore_12q},
    "lvs_ext_017_liabilities_to_assets_zscore_4q":     {"inputs": ["liabilities", "assets"],                    "func": lvs_ext_017_liabilities_to_assets_zscore_4q},
    "lvs_ext_018_liabilities_to_assets_zscore_8q":     {"inputs": ["liabilities", "assets"],                    "func": lvs_ext_018_liabilities_to_assets_zscore_8q},
    "lvs_ext_019_net_debt_to_ebitda_zscore_8q":        {"inputs": ["debt", "cashnequiv", "ebitda"],             "func": lvs_ext_019_net_debt_to_ebitda_zscore_8q},
    "lvs_ext_020_financial_leverage_zscore_8q":        {"inputs": ["assets", "equity"],                         "func": lvs_ext_020_financial_leverage_zscore_8q},
    "lvs_ext_021_liabilities_to_equity_zscore_4q":     {"inputs": ["liabilities", "equity"],                    "func": lvs_ext_021_liabilities_to_equity_zscore_4q},
    "lvs_ext_022_liabilities_to_equity_zscore_8q":     {"inputs": ["liabilities", "equity"],                    "func": lvs_ext_022_liabilities_to_equity_zscore_8q},
    "lvs_ext_023_debt_to_equity_expanding_pct_rank":   {"inputs": ["debt", "equity"],                           "func": lvs_ext_023_debt_to_equity_expanding_pct_rank},
    "lvs_ext_024_debt_to_assets_pct_rank_8q":          {"inputs": ["debt", "assets"],                           "func": lvs_ext_024_debt_to_assets_pct_rank_8q},
    "lvs_ext_025_leverage_above_1x_flag":              {"inputs": ["debt", "equity"],                           "func": lvs_ext_025_leverage_above_1x_flag},
    "lvs_ext_026_leverage_above_3x_flag":              {"inputs": ["debt", "equity"],                           "func": lvs_ext_026_leverage_above_3x_flag},
    "lvs_ext_027_leverage_above_6x_flag":              {"inputs": ["debt", "equity"],                           "func": lvs_ext_027_leverage_above_6x_flag},
    "lvs_ext_028_debt_to_assets_above_60pct_flag":     {"inputs": ["debt", "assets"],                           "func": lvs_ext_028_debt_to_assets_above_60pct_flag},
    "lvs_ext_029_debt_to_assets_above_80pct_flag":     {"inputs": ["debt", "assets"],                           "func": lvs_ext_029_debt_to_assets_above_80pct_flag},
    "lvs_ext_030_liabilities_to_assets_above_80pct":   {"inputs": ["liabilities", "assets"],                    "func": lvs_ext_030_liabilities_to_assets_above_80pct_flag},
    "lvs_ext_031_leverage_above_4x_fraction_1y":       {"inputs": ["debt", "equity"],                           "func": lvs_ext_031_leverage_above_4x_fraction_1y},
    "lvs_ext_032_leverage_above_4x_fraction_3y":       {"inputs": ["debt", "equity"],                           "func": lvs_ext_032_leverage_above_4x_fraction_3y},
    "lvs_ext_033_negative_equity_fraction_2y":         {"inputs": ["equity"],                                   "func": lvs_ext_033_negative_equity_fraction_2y},
    "lvs_ext_034_consecutive_rising_da_qtrs":          {"inputs": ["debt", "assets"],                           "func": lvs_ext_034_consecutive_rising_da_qtrs},
    "lvs_ext_035_consecutive_rising_liab_equity_qtrs": {"inputs": ["liabilities", "equity"],                    "func": lvs_ext_035_consecutive_rising_liab_equity_qtrs},
    "lvs_ext_036_debt_grew_equity_fell_2y_flag":       {"inputs": ["debt", "equity"],                           "func": lvs_ext_036_debt_grew_equity_fell_2y_flag},
    "lvs_ext_037_debt_to_equity_trend_slope_4q":       {"inputs": ["debt", "equity"],                           "func": lvs_ext_037_debt_to_equity_trend_slope_4q},
    "lvs_ext_038_debt_to_equity_trend_slope_8q":       {"inputs": ["debt", "equity"],                           "func": lvs_ext_038_debt_to_equity_trend_slope_8q},
    "lvs_ext_039_debt_to_assets_trend_slope_4q":       {"inputs": ["debt", "assets"],                           "func": lvs_ext_039_debt_to_assets_trend_slope_4q},
    "lvs_ext_040_net_debt_trend_slope_4q":             {"inputs": ["debt", "cashnequiv"],                       "func": lvs_ext_040_net_debt_trend_slope_4q},
    "lvs_ext_041_debt_to_equity_qoq_acceleration":     {"inputs": ["debt", "equity"],                           "func": lvs_ext_041_debt_to_equity_qoq_acceleration},
    "lvs_ext_042_debt_to_assets_qoq_acceleration":     {"inputs": ["debt", "assets"],                           "func": lvs_ext_042_debt_to_assets_qoq_acceleration},
    "lvs_ext_043_net_debt_qoq_acceleration":           {"inputs": ["debt", "cashnequiv"],                       "func": lvs_ext_043_net_debt_qoq_acceleration},
    "lvs_ext_044_debt_to_ebitda_zscore_8q":            {"inputs": ["debt", "ebitda"],                           "func": lvs_ext_044_debt_to_ebitda_zscore_8q},
    "lvs_ext_045_debt_to_ebitda_pct_rank_4q":          {"inputs": ["debt", "ebitda"],                           "func": lvs_ext_045_debt_to_ebitda_pct_rank_4q},
    "lvs_ext_046_debt_to_ebitda_pct_rank_8q":          {"inputs": ["debt", "ebitda"],                           "func": lvs_ext_046_debt_to_ebitda_pct_rank_8q},
    "lvs_ext_047_leverage_ewm_deviation_8q":           {"inputs": ["debt", "equity"],                           "func": lvs_ext_047_leverage_ewm_deviation_8q},
    "lvs_ext_048_debt_to_assets_ewm_deviation_8q":     {"inputs": ["debt", "assets"],                           "func": lvs_ext_048_debt_to_assets_ewm_deviation_8q},
    "lvs_ext_049_net_debt_pct_rank_4q":                {"inputs": ["debt", "cashnequiv"],                       "func": lvs_ext_049_net_debt_pct_rank_4q},
    "lvs_ext_050_net_debt_pct_rank_8q":                {"inputs": ["debt", "cashnequiv"],                       "func": lvs_ext_050_net_debt_pct_rank_8q},
    "lvs_ext_051_net_debt_zscore_4q":                  {"inputs": ["debt", "cashnequiv"],                       "func": lvs_ext_051_net_debt_zscore_4q},
    "lvs_ext_052_net_debt_zscore_8q":                  {"inputs": ["debt", "cashnequiv"],                       "func": lvs_ext_052_net_debt_zscore_8q},
    "lvs_ext_053_net_debt_to_equity_pct_rank_4q":      {"inputs": ["debt", "cashnequiv", "equity"],             "func": lvs_ext_053_net_debt_to_equity_pct_rank_4q},
    "lvs_ext_054_net_debt_to_equity_pct_rank_8q":      {"inputs": ["debt", "cashnequiv", "equity"],             "func": lvs_ext_054_net_debt_to_equity_pct_rank_8q},
    "lvs_ext_055_short_term_debt_mix_zscore_4q":       {"inputs": ["debtc", "debt"],                            "func": lvs_ext_055_short_term_debt_mix_zscore_4q},
    "lvs_ext_056_short_term_debt_mix_pct_rank_4q":     {"inputs": ["debtc", "debt"],                            "func": lvs_ext_056_short_term_debt_mix_pct_rank_4q},
    "lvs_ext_057_debt_to_equity_range_position_8q":    {"inputs": ["debt", "equity"],                           "func": lvs_ext_057_debt_to_equity_range_position_8q},
    "lvs_ext_058_debt_to_assets_range_position_8q":    {"inputs": ["debt", "assets"],                           "func": lvs_ext_058_debt_to_assets_range_position_8q},
    "lvs_ext_059_noncurrent_liab_to_assets_zscore_4q": {"inputs": ["liabilitiesnc", "assets"],                  "func": lvs_ext_059_noncurrent_liab_to_assets_zscore_4q},
    "lvs_ext_060_debtnc_to_debt_yoy_change":           {"inputs": ["debtnc", "debt"],                           "func": lvs_ext_060_debtnc_to_debt_yoy_change},
    "lvs_ext_061_debt_to_assets_expanding_pct_rank":   {"inputs": ["debt", "assets"],                           "func": lvs_ext_061_debt_to_assets_expanding_pct_rank},
    "lvs_ext_062_liabilities_to_assets_expanding_rank":{"inputs": ["liabilities", "assets"],                    "func": lvs_ext_062_liabilities_to_assets_expanding_pct_rank},
    "lvs_ext_063_net_debt_to_ebitda_expanding_rank":   {"inputs": ["debt", "cashnequiv", "ebitda"],             "func": lvs_ext_063_net_debt_to_ebitda_expanding_pct_rank},
    "lvs_ext_064_debt_to_equity_4y_change":            {"inputs": ["debt", "equity"],                           "func": lvs_ext_064_debt_to_equity_4y_change},
    "lvs_ext_065_debt_yoy_pct_rank_4q":                {"inputs": ["debt"],                                     "func": lvs_ext_065_debt_yoy_pct_rank_4q},
    "lvs_ext_066_equity_yoy_change":                   {"inputs": ["equity"],                                   "func": lvs_ext_066_equity_yoy_change},
    "lvs_ext_067_equity_pct_rank_4q":                  {"inputs": ["equity"],                                   "func": lvs_ext_067_equity_pct_rank_4q},
    "lvs_ext_068_equity_pct_rank_8q":                  {"inputs": ["equity"],                                   "func": lvs_ext_068_equity_pct_rank_8q},
    "lvs_ext_069_equity_drawdown_from_4q_peak":        {"inputs": ["equity"],                                   "func": lvs_ext_069_equity_drawdown_from_4q_peak},
    "lvs_ext_070_equity_drawdown_from_expanding_peak": {"inputs": ["equity"],                                   "func": lvs_ext_070_equity_drawdown_from_expanding_peak},
    "lvs_ext_071_leverage_stress_composite_8q":        {"inputs": ["debt", "equity", "assets", "ebitda"],       "func": lvs_ext_071_leverage_stress_composite_8q},
    "lvs_ext_072_leverage_capitulation_composite":     {"inputs": ["debt", "equity", "assets"],                 "func": lvs_ext_072_leverage_capitulation_composite},
    "lvs_ext_073_leverage_multi_flag_score":           {"inputs": ["debt", "equity", "assets"],                 "func": lvs_ext_073_leverage_multi_flag_score},
    "lvs_ext_074_net_debt_to_equity_expanding_zscore": {"inputs": ["debt", "cashnequiv", "equity"],             "func": lvs_ext_074_net_debt_to_equity_expanding_zscore},
    "lvs_ext_075_leverage_cycle_position":             {"inputs": ["debt", "equity"],                           "func": lvs_ext_075_leverage_cycle_position},
}
