"""
69_equity_erosion — Extended Features 001-075
Domain: shareholders'-equity erosion — deeper variants, EWM trends, z-scores,
        composite distress scores, streak counts, percentile ranks, acceleration
        metrics, cross-input ratios, and multi-window low/high flags.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_TD_QTR  = 63
_TD_2Q   = 126
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    return q_series.reindex(daily_index).ffill()


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


def _consec_true(cond: pd.Series) -> pd.Series:
    c = cond.astype(int)
    grp = (~cond).cumsum()
    return c.groupby(grp).cumsum().astype(float)


def _rolling_skew(s: pd.Series, w: int) -> pd.Series:
    def _skew(x):
        v = x[~np.isnan(x)]
        if len(v) < 3:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd < _EPS:
            return np.nan
        return float(((v - m) ** 3).mean() / sd ** 3)
    return s.rolling(w, min_periods=max(3, w // 4)).apply(_skew, raw=True)


def _rolling_kurt(s: pd.Series, w: int) -> pd.Series:
    def _kurt(x):
        v = x[~np.isnan(x)]
        if len(v) < 4:
            return np.nan
        m = v.mean(); sd = v.std(ddof=1)
        if sd < _EPS:
            return np.nan
        return float(((v - m) ** 4).mean() / sd ** 4) - 3.0
    return s.rolling(w, min_periods=max(4, w // 4)).apply(_kurt, raw=True)


# ── Extended Feature functions 001-075 ────────────────────────────────────────

# --- Group A (001-012): Equity EWM trend and acceleration ---

def eqe_ext_001_equity_ewm_trend_63(equity: pd.Series) -> pd.Series:
    """EWM(63)-smoothed equity level — slow trend tracker."""
    return _ewm_mean(equity, 63)


def eqe_ext_002_equity_ewm_trend_126(equity: pd.Series) -> pd.Series:
    """EWM(126)-smoothed equity level — half-year trend."""
    return _ewm_mean(equity, 126)


def eqe_ext_003_equity_ewm_vs_raw_ratio(equity: pd.Series) -> pd.Series:
    """Equity divided by its EWM(63) — deviation from trend (< 1 = below trend)."""
    return _safe_div_abs(equity, _ewm_mean(equity, 63))


def eqe_ext_004_equity_ewm_slope_63(equity: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) equity — smoothed velocity."""
    e = _ewm_mean(equity, 63)
    return e - e.shift(_TD_QTR)


def eqe_ext_005_equity_ewm_slope_accel(equity: pd.Series) -> pd.Series:
    """2nd derivative of EWM(63) equity over one quarter — acceleration of decline."""
    e = _ewm_mean(equity, 63)
    v = e - e.shift(_TD_QTR)
    return v - v.shift(_TD_QTR)


def eqe_ext_006_equity_rolling_mean_63(equity: pd.Series) -> pd.Series:
    """Rolling 63-day mean of equity — quarter-centered smoothing."""
    return _rolling_mean(equity, _TD_QTR)


def eqe_ext_007_equity_rolling_mean_252(equity: pd.Series) -> pd.Series:
    """Rolling 252-day mean of equity — annual-centered smoothing."""
    return _rolling_mean(equity, _TD_YEAR)


def eqe_ext_008_equity_vs_1y_mean_ratio(equity: pd.Series) -> pd.Series:
    """Equity relative to its 1-year rolling mean (< 1 = deteriorating)."""
    return _safe_div_abs(equity, _rolling_mean(equity, _TD_YEAR))


def eqe_ext_009_equity_vs_3y_mean_ratio(equity: pd.Series) -> pd.Series:
    """Equity relative to its 3-year rolling mean."""
    return _safe_div_abs(equity, _rolling_mean(equity, _TD_3Y))


def eqe_ext_010_equity_rolling_min_2q(equity: pd.Series) -> pd.Series:
    """Rolling 2-quarter (126-day) minimum of equity — near-term trough."""
    return _rolling_min(equity, _TD_2Q)


def eqe_ext_011_equity_at_2y_low_flag(equity: pd.Series) -> pd.Series:
    """Binary: 1 if equity equals its rolling 2-year minimum."""
    return (equity <= _rolling_min(equity, _TD_2Y)).astype(float)


def eqe_ext_012_equity_at_3y_low_flag(equity: pd.Series) -> pd.Series:
    """Binary: 1 if equity equals its rolling 3-year minimum."""
    return (equity <= _rolling_min(equity, _TD_3Y)).astype(float)


# --- Group B (013-022): Retained-earnings deeper variants ---

def eqe_ext_013_retearn_zscore_2y(retearn: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of retained earnings (large negative = severe deficit stress)."""
    return _zscore_rolling(retearn, _TD_2Y)


def eqe_ext_014_retearn_zscore_3y(retearn: pd.Series) -> pd.Series:
    """Rolling 3-year z-score of retained earnings."""
    return _zscore_rolling(retearn, _TD_3Y)


def eqe_ext_015_retearn_pct_rank_2y(retearn: pd.Series) -> pd.Series:
    """Rolling 2-year percentile rank of retained earnings (low = severe deficit)."""
    return _rolling_rank_pct(retearn, _TD_2Y)


def eqe_ext_016_retearn_pct_rank_5y(retearn: pd.Series) -> pd.Series:
    """Rolling 5-year percentile rank of retained earnings."""
    return _rolling_rank_pct(retearn, _TD_5Y)


def eqe_ext_017_retearn_at_5y_low_flag(retearn: pd.Series) -> pd.Series:
    """Binary: 1 if retained earnings equals its 5-year rolling minimum."""
    return (retearn <= _rolling_min(retearn, _TD_5Y)).astype(float)


def eqe_ext_018_retearn_ewm_slope_63(retearn: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) retained earnings — smoothed retearn velocity."""
    e = _ewm_mean(retearn, 63)
    return e - e.shift(_TD_QTR)


def eqe_ext_019_retearn_ewm_accel(retearn: pd.Series) -> pd.Series:
    """2nd derivative of EWM(63) retained earnings — acceleration of deficit growth."""
    e = _ewm_mean(retearn, 63)
    v = e - e.shift(_TD_QTR)
    return v - v.shift(_TD_QTR)


def eqe_ext_020_retearn_5y_pct(retearn: pd.Series) -> pd.Series:
    """Retained earnings 5-year percent change; denominator is abs(prior)."""
    prior = retearn.shift(_TD_5Y)
    return _safe_div_abs(retearn - prior, prior)


def eqe_ext_021_retearn_streak_negative(retearn: pd.Series) -> pd.Series:
    """Consecutive days with retained earnings < 0 (streak counter)."""
    return _consec_true(retearn < 0)


def eqe_ext_022_retearn_to_equity_ratio(retearn: pd.Series, equity: pd.Series) -> pd.Series:
    """Retained earnings as fraction of total equity (negative = most equity is funded by deficit)."""
    return _safe_div(retearn, equity.replace(0, np.nan))


# --- Group C (023-033): Equity-to-liabilities and leverage variants ---

def eqe_ext_023_equity_to_liabilities_ratio(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Total equity divided by total liabilities (low/negative = extreme leverage)."""
    return _safe_div(equity, liabilities.replace(0, np.nan))


def eqe_ext_024_equity_to_liabilities_zscore_2y(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of equity-to-liabilities ratio."""
    r = _safe_div(equity, liabilities.replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def eqe_ext_025_equity_to_liabilities_pct_rank_3y(equity: pd.Series, liabilities: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of equity-to-liabilities ratio (low = stressed)."""
    r = _safe_div(equity, liabilities.replace(0, np.nan))
    return _rolling_rank_pct(r, _TD_3Y)


def eqe_ext_026_debt_to_equity_zscore_2y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of debt-to-equity ratio (high = leverage stress)."""
    r = _safe_div(debt, equity.replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def eqe_ext_027_debtnc_to_equity_ratio(debtnc: pd.Series, equity: pd.Series) -> pd.Series:
    """Long-term (non-current) debt to equity ratio."""
    return _safe_div(debtnc, equity.abs().replace(0, np.nan))


def eqe_ext_028_debtnc_to_equity_pct_rank_3y(debtnc: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of LT debt-to-equity ratio."""
    r = _safe_div(debtnc, equity.abs().replace(0, np.nan))
    return _rolling_rank_pct(r, _TD_3Y)


def eqe_ext_029_liabilities_to_assets_zscore_3y(liabilities: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 3-year z-score of liabilities-to-assets ratio."""
    r = _safe_div(liabilities, assets.replace(0, np.nan))
    return _zscore_rolling(r, _TD_3Y)


def eqe_ext_030_equity_to_assets_ewm_slope(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) of equity-to-assets ratio — smoothed solvency trend."""
    r = _safe_div(equity, assets.replace(0, np.nan))
    e = _ewm_mean(r, 63)
    return e - e.shift(_TD_QTR)


def eqe_ext_031_equity_to_assets_zscore_2y(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of equity-to-assets ratio."""
    r = _safe_div(equity, assets.replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def eqe_ext_032_equity_to_assets_pct_rank_5y(equity: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 5-year percentile rank of equity-to-assets ratio."""
    r = _safe_div(equity, assets.replace(0, np.nan))
    return _rolling_rank_pct(r, _TD_5Y)


def eqe_ext_033_netinc_cumulative_drain_3y(netinc: pd.Series) -> pd.Series:
    """3-year rolling sum of net income losses (clip at 0); cumulative equity drain."""
    losses = netinc.clip(upper=0)
    return _rolling_sum(losses, _TD_3Y)


# --- Group D (034-044): OCI and accoci variants ---

def eqe_ext_034_accoci_zscore_2y(accoci: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of accumulated OCI (large negative = hidden equity impairment)."""
    return _zscore_rolling(accoci, _TD_2Y)


def eqe_ext_035_accoci_pct_rank_3y(accoci: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of accumulated OCI."""
    return _rolling_rank_pct(accoci, _TD_3Y)


def eqe_ext_036_accoci_to_equity_ratio(accoci: pd.Series, equity: pd.Series) -> pd.Series:
    """Accumulated OCI as fraction of total equity (large negative = OCI drags equity)."""
    return _safe_div(accoci, equity.abs().replace(0, np.nan))


def eqe_ext_037_accoci_to_equity_zscore_2y(accoci: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of accoci-to-equity ratio."""
    r = _safe_div(accoci, equity.abs().replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def eqe_ext_038_accoci_qoq_change(accoci: pd.Series) -> pd.Series:
    """QoQ change in accumulated OCI."""
    return accoci - accoci.shift(_TD_QTR)


def eqe_ext_039_accoci_yoy_change(accoci: pd.Series) -> pd.Series:
    """YoY change in accumulated OCI."""
    return accoci - accoci.shift(_TD_YEAR)


def eqe_ext_040_accoci_is_negative_flag(accoci: pd.Series) -> pd.Series:
    """Binary: 1 if accumulated OCI is negative (hidden losses in equity)."""
    return (accoci < 0).astype(float)


def eqe_ext_041_accoci_streak_negative(accoci: pd.Series) -> pd.Series:
    """Consecutive days accumulated OCI has been negative."""
    return _consec_true(accoci < 0)


def eqe_ext_042_accoci_to_assets_ratio(accoci: pd.Series, assets: pd.Series) -> pd.Series:
    """Accumulated OCI divided by total assets (OCI weight relative to asset base)."""
    return _safe_div(accoci, assets.replace(0, np.nan))


def eqe_ext_043_accoci_at_3y_low_flag(accoci: pd.Series) -> pd.Series:
    """Binary: 1 if accoci equals its 3-year rolling minimum (deepest OCI drag)."""
    return (accoci <= _rolling_min(accoci, _TD_3Y)).astype(float)


def eqe_ext_044_accoci_ewm_slope_63(accoci: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) of accumulated OCI — smoothed OCI trend."""
    e = _ewm_mean(accoci, 63)
    return e - e.shift(_TD_QTR)


# --- Group E (045-055): Intangibles and tangible-equity variants ---

def eqe_ext_045_intangibles_to_equity_ratio(intangibles: pd.Series, equity: pd.Series) -> pd.Series:
    """Intangibles divided by total equity (high = goodwill/IP bloating book value)."""
    return _safe_div(intangibles, equity.abs().replace(0, np.nan))


def eqe_ext_046_intangibles_to_equity_pct_rank_3y(intangibles: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of intangibles-to-equity ratio."""
    r = _safe_div(intangibles, equity.abs().replace(0, np.nan))
    return _rolling_rank_pct(r, _TD_3Y)


def eqe_ext_047_intangibles_to_assets_zscore_2y(intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of intangibles-to-assets ratio."""
    r = _safe_div(intangibles, assets.replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def eqe_ext_048_tangible_equity(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Tangible equity = equity minus intangibles (negative = net tangible insolvency)."""
    return equity - intangibles


def eqe_ext_049_tangible_equity_at_1y_low_flag(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Binary: 1 if tangible equity is at its 1-year rolling minimum."""
    te = equity - intangibles
    return (te <= _rolling_min(te, _TD_YEAR)).astype(float)


def eqe_ext_050_tangible_equity_zscore_2y(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of tangible equity."""
    return _zscore_rolling(equity - intangibles, _TD_2Y)


def eqe_ext_051_tangible_equity_pct_rank_3y(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of tangible equity."""
    return _rolling_rank_pct(equity - intangibles, _TD_3Y)


def eqe_ext_052_tangible_equity_is_negative(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Binary: 1 if tangible equity (equity - intangibles) is negative."""
    return ((equity - intangibles) < 0).astype(float)


def eqe_ext_053_tangible_equity_streak_negative(equity: pd.Series, intangibles: pd.Series) -> pd.Series:
    """Consecutive days tangible equity has been negative."""
    return _consec_true((equity - intangibles) < 0)


def eqe_ext_054_tangible_equity_to_assets(equity: pd.Series, intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Tangible equity-to-assets ratio."""
    return _safe_div(equity - intangibles, assets.replace(0, np.nan))


def eqe_ext_055_tangible_equity_to_assets_zscore_2y(equity: pd.Series, intangibles: pd.Series, assets: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of tangible equity-to-assets ratio."""
    r = _safe_div(equity - intangibles, assets.replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


# --- Group F (056-065): Preferred equity and netinc damage composites ---

def eqe_ext_056_prefdivis_to_equity_ratio(prefdivis: pd.Series, equity: pd.Series) -> pd.Series:
    """Preferred dividends as fraction of total equity (large = preferred drain is significant)."""
    return _safe_div(prefdivis, equity.abs().replace(0, np.nan))


def eqe_ext_057_prefdivis_trailing_3y_sum(prefdivis: pd.Series) -> pd.Series:
    """3-year rolling sum of preferred dividends paid out."""
    return _rolling_sum(prefdivis, _TD_3Y)


def eqe_ext_058_prefdivis_pct_rank_3y(prefdivis: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of preferred dividends (high = large preferred load)."""
    return _rolling_rank_pct(prefdivis, _TD_3Y)


def eqe_ext_059_netinc_loss_count_3y(netinc: pd.Series) -> pd.Series:
    """Count of days in trailing 3 years where net income is negative."""
    return _rolling_sum((netinc < 0).astype(float), _TD_3Y)


def eqe_ext_060_netinc_to_equity_ratio(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """Net income divided by abs(equity) — ROE proxy (negative = destroying book value)."""
    return _safe_div(netinc, equity.abs().replace(0, np.nan))


def eqe_ext_061_netinc_to_equity_zscore_2y(netinc: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of net income-to-equity ratio."""
    r = _safe_div(netinc, equity.abs().replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def eqe_ext_062_netinc_cumulative_drain_5y(netinc: pd.Series) -> pd.Series:
    """5-year rolling sum of net income losses (clipped at 0) — long-run equity destruction."""
    return _rolling_sum(netinc.clip(upper=0), _TD_5Y)


def eqe_ext_063_equity_skewness_3y(equity: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of equity level — negative skew = left-tail erosion."""
    return _rolling_skew(equity, _TD_3Y)


def eqe_ext_064_equity_kurtosis_3y(equity: pd.Series) -> pd.Series:
    """Rolling 3-year excess kurtosis of equity — fat tails signal sudden jumps."""
    return _rolling_kurt(equity, _TD_3Y)


def eqe_ext_065_retearn_skewness_3y(retearn: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of retained earnings."""
    return _rolling_skew(retearn, _TD_3Y)


# --- Group G (066-075): Composite distress scores and multi-signal flags ---

def eqe_ext_066_composite_erosion_score(equity: pd.Series, retearn: pd.Series, netinc: pd.Series) -> pd.Series:
    """
    Composite erosion score: average of 3 z-scores (1-year):
    equity z-score, retained earnings z-score, net income z-score.
    Large negative = broad fundamental erosion.
    """
    z1 = _zscore_rolling(equity, _TD_YEAR)
    z2 = _zscore_rolling(retearn, _TD_YEAR)
    z3 = _zscore_rolling(netinc, _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


def eqe_ext_067_double_negative_flag(equity: pd.Series, retearn: pd.Series) -> pd.Series:
    """Binary: 1 when BOTH equity < 0 AND retained earnings < 0 simultaneously."""
    return ((equity < 0) & (retearn < 0)).astype(float)


def eqe_ext_068_triple_distress_flag(equity: pd.Series, retearn: pd.Series, netinc: pd.Series) -> pd.Series:
    """Binary: 1 when equity < 0, retearn < 0, AND net income < 0 simultaneously."""
    return ((equity < 0) & (retearn < 0) & (netinc < 0)).astype(float)


def eqe_ext_069_equity_negative_streak(equity: pd.Series) -> pd.Series:
    """Consecutive days equity has been negative (persistence of insolvency)."""
    return _consec_true(equity < 0)


def eqe_ext_070_equity_new_low_streak(equity: pd.Series) -> pd.Series:
    """Consecutive days equity is at or below prior expanding minimum (ever-new-low streak)."""
    exp_min = equity.expanding(min_periods=1).min()
    return _consec_true(equity <= exp_min)


def eqe_ext_071_retearn_new_low_streak(retearn: pd.Series) -> pd.Series:
    """Consecutive days retained earnings is at or below prior expanding minimum."""
    exp_min = retearn.expanding(min_periods=1).min()
    return _consec_true(retearn <= exp_min)


def eqe_ext_072_equity_pct_rank_5y(equity: pd.Series) -> pd.Series:
    """Rolling 5-year percentile rank of total equity (low = maximum distress reading)."""
    return _rolling_rank_pct(equity, _TD_5Y)


def eqe_ext_073_debt_to_equity_pct_rank_5y(debt: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 5-year percentile rank of total debt-to-equity ratio (high = max leverage)."""
    r = _safe_div(debt, equity.abs().replace(0, np.nan))
    return _rolling_rank_pct(r, _TD_5Y)


def eqe_ext_074_sharesbas_equity_per_share(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Book value per basic share (equity / shares) — dilution-adjusted equity value."""
    return _safe_div(equity, sharesbas.replace(0, np.nan))


def eqe_ext_075_book_per_share_pct_rank_3y(equity: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of book value per share (low = distressed book)."""
    bvps = _safe_div(equity, sharesbas.replace(0, np.nan))
    return _rolling_rank_pct(bvps, _TD_3Y)


# ── Registry ──────────────────────────────────────────────────────────────────

EQUITY_EROSION_EXTENDED_REGISTRY_001_075 = {
    "eqe_ext_001_equity_ewm_trend_63": {
        "inputs": ["equity"],
        "func": eqe_ext_001_equity_ewm_trend_63,
    },
    "eqe_ext_002_equity_ewm_trend_126": {
        "inputs": ["equity"],
        "func": eqe_ext_002_equity_ewm_trend_126,
    },
    "eqe_ext_003_equity_ewm_vs_raw_ratio": {
        "inputs": ["equity"],
        "func": eqe_ext_003_equity_ewm_vs_raw_ratio,
    },
    "eqe_ext_004_equity_ewm_slope_63": {
        "inputs": ["equity"],
        "func": eqe_ext_004_equity_ewm_slope_63,
    },
    "eqe_ext_005_equity_ewm_slope_accel": {
        "inputs": ["equity"],
        "func": eqe_ext_005_equity_ewm_slope_accel,
    },
    "eqe_ext_006_equity_rolling_mean_63": {
        "inputs": ["equity"],
        "func": eqe_ext_006_equity_rolling_mean_63,
    },
    "eqe_ext_007_equity_rolling_mean_252": {
        "inputs": ["equity"],
        "func": eqe_ext_007_equity_rolling_mean_252,
    },
    "eqe_ext_008_equity_vs_1y_mean_ratio": {
        "inputs": ["equity"],
        "func": eqe_ext_008_equity_vs_1y_mean_ratio,
    },
    "eqe_ext_009_equity_vs_3y_mean_ratio": {
        "inputs": ["equity"],
        "func": eqe_ext_009_equity_vs_3y_mean_ratio,
    },
    "eqe_ext_010_equity_rolling_min_2q": {
        "inputs": ["equity"],
        "func": eqe_ext_010_equity_rolling_min_2q,
    },
    "eqe_ext_011_equity_at_2y_low_flag": {
        "inputs": ["equity"],
        "func": eqe_ext_011_equity_at_2y_low_flag,
    },
    "eqe_ext_012_equity_at_3y_low_flag": {
        "inputs": ["equity"],
        "func": eqe_ext_012_equity_at_3y_low_flag,
    },
    "eqe_ext_013_retearn_zscore_2y": {
        "inputs": ["retearn"],
        "func": eqe_ext_013_retearn_zscore_2y,
    },
    "eqe_ext_014_retearn_zscore_3y": {
        "inputs": ["retearn"],
        "func": eqe_ext_014_retearn_zscore_3y,
    },
    "eqe_ext_015_retearn_pct_rank_2y": {
        "inputs": ["retearn"],
        "func": eqe_ext_015_retearn_pct_rank_2y,
    },
    "eqe_ext_016_retearn_pct_rank_5y": {
        "inputs": ["retearn"],
        "func": eqe_ext_016_retearn_pct_rank_5y,
    },
    "eqe_ext_017_retearn_at_5y_low_flag": {
        "inputs": ["retearn"],
        "func": eqe_ext_017_retearn_at_5y_low_flag,
    },
    "eqe_ext_018_retearn_ewm_slope_63": {
        "inputs": ["retearn"],
        "func": eqe_ext_018_retearn_ewm_slope_63,
    },
    "eqe_ext_019_retearn_ewm_accel": {
        "inputs": ["retearn"],
        "func": eqe_ext_019_retearn_ewm_accel,
    },
    "eqe_ext_020_retearn_5y_pct": {
        "inputs": ["retearn"],
        "func": eqe_ext_020_retearn_5y_pct,
    },
    "eqe_ext_021_retearn_streak_negative": {
        "inputs": ["retearn"],
        "func": eqe_ext_021_retearn_streak_negative,
    },
    "eqe_ext_022_retearn_to_equity_ratio": {
        "inputs": ["retearn", "equity"],
        "func": eqe_ext_022_retearn_to_equity_ratio,
    },
    "eqe_ext_023_equity_to_liabilities_ratio": {
        "inputs": ["equity", "liabilities"],
        "func": eqe_ext_023_equity_to_liabilities_ratio,
    },
    "eqe_ext_024_equity_to_liabilities_zscore_2y": {
        "inputs": ["equity", "liabilities"],
        "func": eqe_ext_024_equity_to_liabilities_zscore_2y,
    },
    "eqe_ext_025_equity_to_liabilities_pct_rank_3y": {
        "inputs": ["equity", "liabilities"],
        "func": eqe_ext_025_equity_to_liabilities_pct_rank_3y,
    },
    "eqe_ext_026_debt_to_equity_zscore_2y": {
        "inputs": ["debt", "equity"],
        "func": eqe_ext_026_debt_to_equity_zscore_2y,
    },
    "eqe_ext_027_debtnc_to_equity_ratio": {
        "inputs": ["debtnc", "equity"],
        "func": eqe_ext_027_debtnc_to_equity_ratio,
    },
    "eqe_ext_028_debtnc_to_equity_pct_rank_3y": {
        "inputs": ["debtnc", "equity"],
        "func": eqe_ext_028_debtnc_to_equity_pct_rank_3y,
    },
    "eqe_ext_029_liabilities_to_assets_zscore_3y": {
        "inputs": ["liabilities", "assets"],
        "func": eqe_ext_029_liabilities_to_assets_zscore_3y,
    },
    "eqe_ext_030_equity_to_assets_ewm_slope": {
        "inputs": ["equity", "assets"],
        "func": eqe_ext_030_equity_to_assets_ewm_slope,
    },
    "eqe_ext_031_equity_to_assets_zscore_2y": {
        "inputs": ["equity", "assets"],
        "func": eqe_ext_031_equity_to_assets_zscore_2y,
    },
    "eqe_ext_032_equity_to_assets_pct_rank_5y": {
        "inputs": ["equity", "assets"],
        "func": eqe_ext_032_equity_to_assets_pct_rank_5y,
    },
    "eqe_ext_033_netinc_cumulative_drain_3y": {
        "inputs": ["netinc"],
        "func": eqe_ext_033_netinc_cumulative_drain_3y,
    },
    "eqe_ext_034_accoci_zscore_2y": {
        "inputs": ["accoci"],
        "func": eqe_ext_034_accoci_zscore_2y,
    },
    "eqe_ext_035_accoci_pct_rank_3y": {
        "inputs": ["accoci"],
        "func": eqe_ext_035_accoci_pct_rank_3y,
    },
    "eqe_ext_036_accoci_to_equity_ratio": {
        "inputs": ["accoci", "equity"],
        "func": eqe_ext_036_accoci_to_equity_ratio,
    },
    "eqe_ext_037_accoci_to_equity_zscore_2y": {
        "inputs": ["accoci", "equity"],
        "func": eqe_ext_037_accoci_to_equity_zscore_2y,
    },
    "eqe_ext_038_accoci_qoq_change": {
        "inputs": ["accoci"],
        "func": eqe_ext_038_accoci_qoq_change,
    },
    "eqe_ext_039_accoci_yoy_change": {
        "inputs": ["accoci"],
        "func": eqe_ext_039_accoci_yoy_change,
    },
    "eqe_ext_040_accoci_is_negative_flag": {
        "inputs": ["accoci"],
        "func": eqe_ext_040_accoci_is_negative_flag,
    },
    "eqe_ext_041_accoci_streak_negative": {
        "inputs": ["accoci"],
        "func": eqe_ext_041_accoci_streak_negative,
    },
    "eqe_ext_042_accoci_to_assets_ratio": {
        "inputs": ["accoci", "assets"],
        "func": eqe_ext_042_accoci_to_assets_ratio,
    },
    "eqe_ext_043_accoci_at_3y_low_flag": {
        "inputs": ["accoci"],
        "func": eqe_ext_043_accoci_at_3y_low_flag,
    },
    "eqe_ext_044_accoci_ewm_slope_63": {
        "inputs": ["accoci"],
        "func": eqe_ext_044_accoci_ewm_slope_63,
    },
    "eqe_ext_045_intangibles_to_equity_ratio": {
        "inputs": ["intangibles", "equity"],
        "func": eqe_ext_045_intangibles_to_equity_ratio,
    },
    "eqe_ext_046_intangibles_to_equity_pct_rank_3y": {
        "inputs": ["intangibles", "equity"],
        "func": eqe_ext_046_intangibles_to_equity_pct_rank_3y,
    },
    "eqe_ext_047_intangibles_to_assets_zscore_2y": {
        "inputs": ["intangibles", "assets"],
        "func": eqe_ext_047_intangibles_to_assets_zscore_2y,
    },
    "eqe_ext_048_tangible_equity": {
        "inputs": ["equity", "intangibles"],
        "func": eqe_ext_048_tangible_equity,
    },
    "eqe_ext_049_tangible_equity_at_1y_low_flag": {
        "inputs": ["equity", "intangibles"],
        "func": eqe_ext_049_tangible_equity_at_1y_low_flag,
    },
    "eqe_ext_050_tangible_equity_zscore_2y": {
        "inputs": ["equity", "intangibles"],
        "func": eqe_ext_050_tangible_equity_zscore_2y,
    },
    "eqe_ext_051_tangible_equity_pct_rank_3y": {
        "inputs": ["equity", "intangibles"],
        "func": eqe_ext_051_tangible_equity_pct_rank_3y,
    },
    "eqe_ext_052_tangible_equity_is_negative": {
        "inputs": ["equity", "intangibles"],
        "func": eqe_ext_052_tangible_equity_is_negative,
    },
    "eqe_ext_053_tangible_equity_streak_negative": {
        "inputs": ["equity", "intangibles"],
        "func": eqe_ext_053_tangible_equity_streak_negative,
    },
    "eqe_ext_054_tangible_equity_to_assets": {
        "inputs": ["equity", "intangibles", "assets"],
        "func": eqe_ext_054_tangible_equity_to_assets,
    },
    "eqe_ext_055_tangible_equity_to_assets_zscore_2y": {
        "inputs": ["equity", "intangibles", "assets"],
        "func": eqe_ext_055_tangible_equity_to_assets_zscore_2y,
    },
    "eqe_ext_056_prefdivis_to_equity_ratio": {
        "inputs": ["prefdivis", "equity"],
        "func": eqe_ext_056_prefdivis_to_equity_ratio,
    },
    "eqe_ext_057_prefdivis_trailing_3y_sum": {
        "inputs": ["prefdivis"],
        "func": eqe_ext_057_prefdivis_trailing_3y_sum,
    },
    "eqe_ext_058_prefdivis_pct_rank_3y": {
        "inputs": ["prefdivis"],
        "func": eqe_ext_058_prefdivis_pct_rank_3y,
    },
    "eqe_ext_059_netinc_loss_count_3y": {
        "inputs": ["netinc"],
        "func": eqe_ext_059_netinc_loss_count_3y,
    },
    "eqe_ext_060_netinc_to_equity_ratio": {
        "inputs": ["netinc", "equity"],
        "func": eqe_ext_060_netinc_to_equity_ratio,
    },
    "eqe_ext_061_netinc_to_equity_zscore_2y": {
        "inputs": ["netinc", "equity"],
        "func": eqe_ext_061_netinc_to_equity_zscore_2y,
    },
    "eqe_ext_062_netinc_cumulative_drain_5y": {
        "inputs": ["netinc"],
        "func": eqe_ext_062_netinc_cumulative_drain_5y,
    },
    "eqe_ext_063_equity_skewness_3y": {
        "inputs": ["equity"],
        "func": eqe_ext_063_equity_skewness_3y,
    },
    "eqe_ext_064_equity_kurtosis_3y": {
        "inputs": ["equity"],
        "func": eqe_ext_064_equity_kurtosis_3y,
    },
    "eqe_ext_065_retearn_skewness_3y": {
        "inputs": ["retearn"],
        "func": eqe_ext_065_retearn_skewness_3y,
    },
    "eqe_ext_066_composite_erosion_score": {
        "inputs": ["equity", "retearn", "netinc"],
        "func": eqe_ext_066_composite_erosion_score,
    },
    "eqe_ext_067_double_negative_flag": {
        "inputs": ["equity", "retearn"],
        "func": eqe_ext_067_double_negative_flag,
    },
    "eqe_ext_068_triple_distress_flag": {
        "inputs": ["equity", "retearn", "netinc"],
        "func": eqe_ext_068_triple_distress_flag,
    },
    "eqe_ext_069_equity_negative_streak": {
        "inputs": ["equity"],
        "func": eqe_ext_069_equity_negative_streak,
    },
    "eqe_ext_070_equity_new_low_streak": {
        "inputs": ["equity"],
        "func": eqe_ext_070_equity_new_low_streak,
    },
    "eqe_ext_071_retearn_new_low_streak": {
        "inputs": ["retearn"],
        "func": eqe_ext_071_retearn_new_low_streak,
    },
    "eqe_ext_072_equity_pct_rank_5y": {
        "inputs": ["equity"],
        "func": eqe_ext_072_equity_pct_rank_5y,
    },
    "eqe_ext_073_debt_to_equity_pct_rank_5y": {
        "inputs": ["debt", "equity"],
        "func": eqe_ext_073_debt_to_equity_pct_rank_5y,
    },
    "eqe_ext_074_sharesbas_equity_per_share": {
        "inputs": ["equity", "sharesbas"],
        "func": eqe_ext_074_sharesbas_equity_per_share,
    },
    "eqe_ext_075_book_per_share_pct_rank_3y": {
        "inputs": ["equity", "sharesbas"],
        "func": eqe_ext_075_book_per_share_pct_rank_3y,
    },
}
