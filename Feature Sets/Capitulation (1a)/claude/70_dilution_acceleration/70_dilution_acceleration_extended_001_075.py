"""
70_dilution_acceleration — Extended Features 001-075
Domain: share-count dilution — deeper variants, EWM trends, z-scores,
        acceleration metrics, cross-input ratios, streak counters, percentile
        ranks, composite dilution distress scores, and multi-window flags.
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


# ── Extended Feature functions 001-075 ────────────────────────────────────────

# --- Group A (001-012): Sharesbas EWM trends and acceleration ---

def dla_ext_001_sharesbas_ewm_63(sharesbas: pd.Series) -> pd.Series:
    """EWM(63)-smoothed basic shares — slow trend of share count."""
    return _ewm_mean(sharesbas, 63)


def dla_ext_002_sharesbas_ewm_slope_63(sharesbas: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) basic shares — smoothed dilution velocity."""
    e = _ewm_mean(sharesbas, 63)
    return e - e.shift(_TD_QTR)


def dla_ext_003_sharesbas_ewm_accel(sharesbas: pd.Series) -> pd.Series:
    """2nd derivative of EWM(63) basic shares — acceleration of dilution."""
    e = _ewm_mean(sharesbas, 63)
    v = e - e.shift(_TD_QTR)
    return v - v.shift(_TD_QTR)


def dla_ext_004_sharesbas_zscore_1y(sharesbas: pd.Series) -> pd.Series:
    """Rolling 1-year z-score of basic shares outstanding."""
    return _zscore_rolling(sharesbas, _TD_YEAR)


def dla_ext_005_sharesbas_zscore_3y(sharesbas: pd.Series) -> pd.Series:
    """Rolling 3-year z-score of basic shares outstanding (high = extreme dilution level)."""
    return _zscore_rolling(sharesbas, _TD_3Y)


def dla_ext_006_sharesbas_pct_rank_2y(sharesbas: pd.Series) -> pd.Series:
    """Rolling 2-year percentile rank of basic shares (high rank = dilution peak)."""
    return _rolling_rank_pct(sharesbas, _TD_2Y)


def dla_ext_007_sharesbas_pct_rank_5y(sharesbas: pd.Series) -> pd.Series:
    """Rolling 5-year percentile rank of basic shares."""
    return _rolling_rank_pct(sharesbas, _TD_5Y)


def dla_ext_008_sharesbas_at_5y_high_zscore(sharesbas: pd.Series) -> pd.Series:
    """Z-score of basic shares at 5-year window — how extreme is current dilution level."""
    return _zscore_rolling(sharesbas, _TD_5Y)


def dla_ext_009_sharesbas_vs_5y_mean_ratio(sharesbas: pd.Series) -> pd.Series:
    """Basic shares divided by rolling 5-year mean — dilution relative to history."""
    return _safe_div(sharesbas, _rolling_mean(sharesbas, _TD_5Y))


def dla_ext_010_sharesbas_5y_pct_change(sharesbas: pd.Series) -> pd.Series:
    """Basic shares 5-year percent change (cumulative dilution over 5 years)."""
    prior = sharesbas.shift(_TD_5Y)
    return _safe_div(sharesbas - prior, prior.replace(0, np.nan))


def dla_ext_011_sharesbas_qoq_pct_rank_2y(sharesbas: pd.Series) -> pd.Series:
    """Rolling 2-year percentile rank of QoQ basic-share growth rate."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    return _rolling_rank_pct(pct, _TD_2Y)


def dla_ext_012_sharesbas_yoy_pct_zscore_3y(sharesbas: pd.Series) -> pd.Series:
    """Rolling 3-year z-score of YoY basic share growth rate."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_YEAR), sharesbas.shift(_TD_YEAR).replace(0, np.nan))
    return _zscore_rolling(pct, _TD_3Y)


# --- Group B (013-024): Shareswa and diluted shares extended ---

def dla_ext_013_shareswa_zscore_2y(shareswa: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of weighted-average basic shares."""
    return _zscore_rolling(shareswa, _TD_2Y)


def dla_ext_014_shareswa_pct_rank_3y(shareswa: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of weighted-average basic shares."""
    return _rolling_rank_pct(shareswa, _TD_3Y)


def dla_ext_015_shareswa_ewm_slope_63(shareswa: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) of WA basic shares — smoothed WA dilution velocity."""
    e = _ewm_mean(shareswa, 63)
    return e - e.shift(_TD_QTR)


def dla_ext_016_shareswadil_zscore_2y(shareswadil: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of diluted WA shares."""
    return _zscore_rolling(shareswadil, _TD_2Y)


def dla_ext_017_shareswadil_pct_rank_3y(shareswadil: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of diluted WA shares."""
    return _rolling_rank_pct(shareswadil, _TD_3Y)


def dla_ext_018_shareswadil_ewm_slope_63(shareswadil: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) diluted WA shares."""
    e = _ewm_mean(shareswadil, 63)
    return e - e.shift(_TD_QTR)


def dla_ext_019_shareswadil_5y_pct(shareswadil: pd.Series) -> pd.Series:
    """Diluted WA shares 5-year percent change."""
    prior = shareswadil.shift(_TD_5Y)
    return _safe_div(shareswadil - prior, prior.replace(0, np.nan))


def dla_ext_020_diluted_basic_gap_zscore_3y(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Rolling 3-year z-score of the diluted-vs-basic share gap (high = extreme overhang)."""
    gap = shareswadil - shareswa
    return _zscore_rolling(gap, _TD_3Y)


def dla_ext_021_diluted_basic_gap_5y_pct_rank(shareswadil: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Rolling 5-year percentile rank of diluted-vs-basic gap."""
    gap = shareswadil - shareswa
    return _rolling_rank_pct(gap, _TD_5Y)


def dla_ext_022_shareswadil_vs_sharesbas_zscore_3y(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Rolling 3-year z-score of diluted WA minus basic shares outstanding gap."""
    gap = shareswadil - sharesbas
    return _zscore_rolling(gap, _TD_3Y)


def dla_ext_023_shareswadil_growth_streak(shareswadil: pd.Series) -> pd.Series:
    """Consecutive days diluted WA shares are higher than 1 quarter ago (dilution streak)."""
    return _consec_true(shareswadil > shareswadil.shift(_TD_QTR))


def dla_ext_024_sharesbas_growth_streak(sharesbas: pd.Series) -> pd.Series:
    """Consecutive days basic shares are higher than 1 quarter ago (issuance streak)."""
    return _consec_true(sharesbas > sharesbas.shift(_TD_QTR))


# --- Group C (025-036): ncfcommon extended variants ---

def dla_ext_025_ncfcommon_zscore_2y(ncfcommon: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of net cash from common equity issuance."""
    return _zscore_rolling(ncfcommon, _TD_2Y)


def dla_ext_026_ncfcommon_pct_rank_3y(ncfcommon: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of ncfcommon (high = large equity raise)."""
    return _rolling_rank_pct(ncfcommon, _TD_3Y)


def dla_ext_027_ncfcommon_to_assets_ratio(ncfcommon: pd.Series, assets: pd.Series) -> pd.Series:
    """TTM equity issuance as fraction of total assets."""
    ttm = _rolling_sum(ncfcommon, _TD_YEAR)
    return _safe_div(ttm, assets.replace(0, np.nan))


def dla_ext_028_ncfcommon_to_equity_zscore_2y(ncfcommon: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of TTM ncfcommon-to-equity ratio."""
    ttm = _rolling_sum(ncfcommon, _TD_YEAR)
    r = _safe_div(ttm, equity.abs().replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def dla_ext_029_ncfcommon_to_ncfo_ratio(ncfcommon: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Equity issuance relative to operating cash flow (high = funding via equity, not ops)."""
    return _safe_div(ncfcommon.clip(lower=0), ncfo.abs().replace(0, np.nan))


def dla_ext_030_ncfcommon_trailing_5y_sum(ncfcommon: pd.Series) -> pd.Series:
    """5-year cumulative equity issuance proceeds."""
    return _rolling_sum(ncfcommon, _TD_5Y)


def dla_ext_031_issuance_count_3y(ncfcommon: pd.Series) -> pd.Series:
    """Count of days in trailing 3 years where equity was raised (ncfcommon > 0)."""
    return _rolling_sum((ncfcommon > 0).astype(float), _TD_3Y)


def dla_ext_032_issuance_count_5y(ncfcommon: pd.Series) -> pd.Series:
    """Count of days in trailing 5 years where equity was raised."""
    return _rolling_sum((ncfcommon > 0).astype(float), _TD_5Y)


def dla_ext_033_ncfcommon_ewm_slope_63(ncfcommon: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) ncfcommon — trend in equity-raise pace."""
    e = _ewm_mean(ncfcommon, 63)
    return e - e.shift(_TD_QTR)


def dla_ext_034_ncfcommon_issuance_streak(ncfcommon: pd.Series) -> pd.Series:
    """Consecutive days ncfcommon > 0 (unbroken equity-raise streak)."""
    return _consec_true(ncfcommon > 0)


def dla_ext_035_ncfcommon_large_raise_flag(ncfcommon: pd.Series, assets: pd.Series) -> pd.Series:
    """Binary: 1 when ncfcommon > 5% of total assets — large dilutive equity raise."""
    return (ncfcommon > 0.05 * assets).astype(float)


def dla_ext_036_ncfcommon_to_revenue_ratio(ncfcommon: pd.Series, revenue: pd.Series) -> pd.Series:
    """Equity issuance as fraction of revenue (high = company relies on capital markets, not sales)."""
    return _safe_div(ncfcommon.clip(lower=0), revenue.replace(0, np.nan))


# --- Group D (037-048): Stock-based comp dilution extended ---

def dla_ext_037_sbcomp_zscore_2y(sbcomp: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of stock-based compensation (high = extreme SBC dilution)."""
    return _zscore_rolling(sbcomp, _TD_2Y)


def dla_ext_038_sbcomp_pct_rank_3y(sbcomp: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of SBC."""
    return _rolling_rank_pct(sbcomp, _TD_3Y)


def dla_ext_039_sbcomp_trailing_3y_sum(sbcomp: pd.Series) -> pd.Series:
    """3-year cumulative stock-based compensation."""
    return _rolling_sum(sbcomp, _TD_3Y)


def dla_ext_040_sbcomp_trailing_5y_sum(sbcomp: pd.Series) -> pd.Series:
    """5-year cumulative stock-based compensation."""
    return _rolling_sum(sbcomp, _TD_5Y)


def dla_ext_041_sbcomp_to_revenue_zscore_2y(sbcomp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of SBC-to-revenue ratio."""
    r = _safe_div(sbcomp, revenue.replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def dla_ext_042_sbcomp_to_equity_ratio(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """SBC as fraction of equity book value (high = SBC is large relative to equity base)."""
    return _safe_div(sbcomp, equity.abs().replace(0, np.nan))


def dla_ext_043_sbcomp_to_equity_zscore_2y(sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of SBC-to-equity ratio."""
    r = _safe_div(sbcomp, equity.abs().replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def dla_ext_044_sbcomp_to_assets_ratio(sbcomp: pd.Series, assets: pd.Series) -> pd.Series:
    """SBC as fraction of total assets."""
    return _safe_div(sbcomp, assets.replace(0, np.nan))


def dla_ext_045_sbcomp_ewm_slope_63(sbcomp: pd.Series) -> pd.Series:
    """1-quarter change in EWM(63) SBC — acceleration of compensation dilution."""
    e = _ewm_mean(sbcomp, 63)
    return e - e.shift(_TD_QTR)


def dla_ext_046_sbcomp_ncfcommon_combined(sbcomp: pd.Series, ncfcommon: pd.Series) -> pd.Series:
    """TTM combined dilution: SBC + positive ncfcommon (total equity-funded cost)."""
    return _rolling_sum(sbcomp + ncfcommon.clip(lower=0), _TD_YEAR)


def dla_ext_047_sbcomp_ncfcommon_to_revenue(sbcomp: pd.Series, ncfcommon: pd.Series, revenue: pd.Series) -> pd.Series:
    """TTM (SBC + positive ncfcommon) as fraction of revenue — total dilution burden."""
    combo = _rolling_sum(sbcomp + ncfcommon.clip(lower=0), _TD_YEAR)
    return _safe_div(combo, revenue.replace(0, np.nan))


def dla_ext_048_sbcomp_to_ncfo_ratio(sbcomp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """SBC as fraction of operating cash flow (high = SBC is large vs operating performance)."""
    return _safe_div(sbcomp, ncfo.abs().replace(0, np.nan))


# --- Group E (049-060): Multi-input dilution composites and ratios ---

def dla_ext_049_dilution_intensity_score(sharesbas: pd.Series, shareswa: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """
    Composite dilution intensity: average of 3 z-scores (1-year) for
    basic shares, WA shares, and diluted WA shares.
    """
    z1 = _zscore_rolling(sharesbas, _TD_YEAR)
    z2 = _zscore_rolling(shareswa, _TD_YEAR)
    z3 = _zscore_rolling(shareswadil, _TD_YEAR)
    return (z1 + z2 + z3) / 3.0


def dla_ext_050_sharesbas_to_assets_ratio(sharesbas: pd.Series, assets: pd.Series) -> pd.Series:
    """Basic shares divided by assets (shares per dollar of assets — dilution density)."""
    return _safe_div(sharesbas, assets.replace(0, np.nan))


def dla_ext_051_sharesbas_to_equity_ratio(sharesbas: pd.Series, equity: pd.Series) -> pd.Series:
    """Basic shares per dollar of equity (shares per book-value dollar)."""
    return _safe_div(sharesbas, equity.abs().replace(0, np.nan))


def dla_ext_052_shareswa_yoy_pct_rank_3y(shareswa: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of YoY WA share growth rate."""
    pct = _safe_div(shareswa - shareswa.shift(_TD_YEAR), shareswa.shift(_TD_YEAR).replace(0, np.nan))
    return _rolling_rank_pct(pct, _TD_3Y)


def dla_ext_053_shareswadil_to_sharesbas_pct_rank_3y(shareswadil: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of diluted-to-basic ratio (high = extreme option overhang)."""
    r = _safe_div(shareswadil, sharesbas.replace(0, np.nan))
    return _rolling_rank_pct(r, _TD_3Y)


def dla_ext_054_ncfcommon_to_ncfo_zscore_2y(ncfcommon: pd.Series, ncfo: pd.Series) -> pd.Series:
    """Rolling 2-year z-score of equity-issuance to operating-cash-flow ratio."""
    r = _safe_div(ncfcommon.clip(lower=0), ncfo.abs().replace(0, np.nan))
    return _zscore_rolling(r, _TD_2Y)


def dla_ext_055_sharesbas_ewm_accel(sharesbas: pd.Series) -> pd.Series:
    """2nd derivative of EWM(63) basic shares — acceleration of issuance pace."""
    e = _ewm_mean(sharesbas, 63)
    v = e - e.shift(_TD_QTR)
    return v - v.shift(_TD_QTR)


def dla_ext_056_dilution_vs_revenue_growth(sharesbas: pd.Series, revenue: pd.Series) -> pd.Series:
    """YoY share dilution minus YoY revenue growth — dilution outpacing growth signal."""
    shr_g = _safe_div(sharesbas - sharesbas.shift(_TD_YEAR), sharesbas.shift(_TD_YEAR).replace(0, np.nan))
    rev_g = _safe_div(revenue - revenue.shift(_TD_YEAR), revenue.shift(_TD_YEAR).replace(0, np.nan))
    return shr_g - rev_g


def dla_ext_057_ncfcommon_skew_3y(ncfcommon: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of ncfcommon (right skew = sporadic large raises)."""
    return _rolling_skew(ncfcommon, _TD_3Y)


def dla_ext_058_large_jump_streak(sharesbas: pd.Series) -> pd.Series:
    """Consecutive days basic shares grew >5% QoQ (sustained issuance streak)."""
    pct = _safe_div(sharesbas - sharesbas.shift(_TD_QTR), sharesbas.shift(_TD_QTR).replace(0, np.nan))
    return _consec_true(pct > 0.05)


def dla_ext_059_diluted_at_5y_high_flag(shareswadil: pd.Series) -> pd.Series:
    """Binary: 1 if diluted WA shares are at their 5-year rolling maximum."""
    return (shareswadil >= _rolling_max(shareswadil, _TD_5Y)).astype(float)


def dla_ext_060_sharesbas_drawdown_from_3y_high(sharesbas: pd.Series) -> pd.Series:
    """Basic shares minus their 3-year rolling maximum (positive = shares at all-time high)."""
    return sharesbas - _rolling_max(sharesbas, _TD_3Y)


# --- Group F (061-075): Composite and cross-signal extended features ---

def dla_ext_061_dilution_burden_score(sharesbas: pd.Series, ncfcommon: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """
    Composite dilution burden: z-score of basic shares + positive ncfcommon flag + SBC z-score.
    All within 1-year rolling window.
    """
    z_shr = _zscore_rolling(sharesbas, _TD_YEAR)
    z_sbc = _zscore_rolling(sbcomp, _TD_YEAR)
    issue_flag = (ncfcommon > 0).astype(float)
    return z_shr + z_sbc + issue_flag


def dla_ext_062_ncfcommon_5y_pct_rank(ncfcommon: pd.Series) -> pd.Series:
    """Rolling 5-year percentile rank of ncfcommon."""
    return _rolling_rank_pct(ncfcommon, _TD_5Y)


def dla_ext_063_sharesbas_skew_3y(sharesbas: pd.Series) -> pd.Series:
    """Rolling 3-year skewness of basic shares (right skew = step-jump dilution events)."""
    return _rolling_skew(sharesbas, _TD_3Y)


def dla_ext_064_shareswa_2y_pct(shareswa: pd.Series) -> pd.Series:
    """WA basic shares 2-year percent change."""
    prior = shareswa.shift(_TD_2Y)
    return _safe_div(shareswa - prior, prior.replace(0, np.nan))


def dla_ext_065_shareswadil_2y_pct(shareswadil: pd.Series) -> pd.Series:
    """Diluted WA shares 2-year percent change."""
    prior = shareswadil.shift(_TD_2Y)
    return _safe_div(shareswadil - prior, prior.replace(0, np.nan))


def dla_ext_066_diluted_accel_flag(shareswadil: pd.Series) -> pd.Series:
    """Binary: 1 if diluted share growth is accelerating (current QoQ growth > prior QoQ growth)."""
    pct_now  = _safe_div(shareswadil - shareswadil.shift(_TD_QTR), shareswadil.shift(_TD_QTR).replace(0, np.nan))
    pct_prev = _safe_div(shareswadil.shift(_TD_QTR) - shareswadil.shift(2 * _TD_QTR),
                         shareswadil.shift(2 * _TD_QTR).replace(0, np.nan))
    return (pct_now > pct_prev).astype(float)


def dla_ext_067_ncfcommon_yoy_pct_rank_3y(ncfcommon: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of YoY change in ncfcommon."""
    yoy = ncfcommon - ncfcommon.shift(_TD_YEAR)
    return _rolling_rank_pct(yoy, _TD_3Y)


def dla_ext_068_sbcomp_yoy_pct(sbcomp: pd.Series) -> pd.Series:
    """YoY percent change in SBC (acceleration = rising dilution from compensation)."""
    prior = sbcomp.shift(_TD_YEAR)
    return _safe_div(sbcomp - prior, prior.replace(0, np.nan))


def dla_ext_069_sbcomp_yoy_pct_rank_3y(sbcomp: pd.Series) -> pd.Series:
    """Rolling 3-year percentile rank of YoY SBC growth rate."""
    pct = _safe_div(sbcomp - sbcomp.shift(_TD_YEAR), sbcomp.shift(_TD_YEAR).replace(0, np.nan))
    return _rolling_rank_pct(pct, _TD_3Y)


def dla_ext_070_sharesbas_new_high_streak(sharesbas: pd.Series) -> pd.Series:
    """Consecutive days basic shares are at or above expanding maximum (ever-new-high issuance)."""
    exp_max = sharesbas.expanding(min_periods=1).max()
    return _consec_true(sharesbas >= exp_max)


def dla_ext_071_ncfcommon_plus_sbcomp_to_equity(ncfcommon: pd.Series, sbcomp: pd.Series, equity: pd.Series) -> pd.Series:
    """TTM total equity dilution cost (ncfcommon + SBC) as fraction of book equity."""
    combo = _rolling_sum(ncfcommon.clip(lower=0) + sbcomp, _TD_YEAR)
    return _safe_div(combo, equity.abs().replace(0, np.nan))


def dla_ext_072_dilution_vs_ncfo(ncfcommon: pd.Series, sbcomp: pd.Series, ncfo: pd.Series) -> pd.Series:
    """TTM dilution cost relative to operating cash flow (high = ops can't fund dilution cost)."""
    combo = _rolling_sum(ncfcommon.clip(lower=0) + sbcomp, _TD_YEAR)
    return _safe_div(combo, ncfo.abs().replace(0, np.nan))


def dla_ext_073_sharesbas_2q_change(sharesbas: pd.Series) -> pd.Series:
    """Basic shares outstanding change over 2 quarters (126-day lag)."""
    return sharesbas - sharesbas.shift(_TD_2Q)


def dla_ext_074_shareswadil_2q_pct(shareswadil: pd.Series) -> pd.Series:
    """Diluted WA shares 2-quarter percent change."""
    prior = shareswadil.shift(_TD_2Q)
    return _safe_div(shareswadil - prior, prior.replace(0, np.nan))


def dla_ext_075_dilution_composite_rank_3y(sharesbas: pd.Series, shareswadil: pd.Series, sbcomp: pd.Series) -> pd.Series:
    """
    Composite: average of 3-year percentile ranks of basic shares, diluted shares, and SBC.
    High value = historically extreme dilution across all three dimensions.
    """
    r1 = _rolling_rank_pct(sharesbas, _TD_3Y)
    r2 = _rolling_rank_pct(shareswadil, _TD_3Y)
    r3 = _rolling_rank_pct(sbcomp, _TD_3Y)
    return (r1 + r2 + r3) / 3.0


# ── Registry ──────────────────────────────────────────────────────────────────

DILUTION_ACCELERATION_EXTENDED_REGISTRY_001_075 = {
    "dla_ext_001_sharesbas_ewm_63": {
        "inputs": ["sharesbas"],
        "func": dla_ext_001_sharesbas_ewm_63,
    },
    "dla_ext_002_sharesbas_ewm_slope_63": {
        "inputs": ["sharesbas"],
        "func": dla_ext_002_sharesbas_ewm_slope_63,
    },
    "dla_ext_003_sharesbas_ewm_accel": {
        "inputs": ["sharesbas"],
        "func": dla_ext_003_sharesbas_ewm_accel,
    },
    "dla_ext_004_sharesbas_zscore_1y": {
        "inputs": ["sharesbas"],
        "func": dla_ext_004_sharesbas_zscore_1y,
    },
    "dla_ext_005_sharesbas_zscore_3y": {
        "inputs": ["sharesbas"],
        "func": dla_ext_005_sharesbas_zscore_3y,
    },
    "dla_ext_006_sharesbas_pct_rank_2y": {
        "inputs": ["sharesbas"],
        "func": dla_ext_006_sharesbas_pct_rank_2y,
    },
    "dla_ext_007_sharesbas_pct_rank_5y": {
        "inputs": ["sharesbas"],
        "func": dla_ext_007_sharesbas_pct_rank_5y,
    },
    "dla_ext_008_sharesbas_at_5y_high_zscore": {
        "inputs": ["sharesbas"],
        "func": dla_ext_008_sharesbas_at_5y_high_zscore,
    },
    "dla_ext_009_sharesbas_vs_5y_mean_ratio": {
        "inputs": ["sharesbas"],
        "func": dla_ext_009_sharesbas_vs_5y_mean_ratio,
    },
    "dla_ext_010_sharesbas_5y_pct_change": {
        "inputs": ["sharesbas"],
        "func": dla_ext_010_sharesbas_5y_pct_change,
    },
    "dla_ext_011_sharesbas_qoq_pct_rank_2y": {
        "inputs": ["sharesbas"],
        "func": dla_ext_011_sharesbas_qoq_pct_rank_2y,
    },
    "dla_ext_012_sharesbas_yoy_pct_zscore_3y": {
        "inputs": ["sharesbas"],
        "func": dla_ext_012_sharesbas_yoy_pct_zscore_3y,
    },
    "dla_ext_013_shareswa_zscore_2y": {
        "inputs": ["shareswa"],
        "func": dla_ext_013_shareswa_zscore_2y,
    },
    "dla_ext_014_shareswa_pct_rank_3y": {
        "inputs": ["shareswa"],
        "func": dla_ext_014_shareswa_pct_rank_3y,
    },
    "dla_ext_015_shareswa_ewm_slope_63": {
        "inputs": ["shareswa"],
        "func": dla_ext_015_shareswa_ewm_slope_63,
    },
    "dla_ext_016_shareswadil_zscore_2y": {
        "inputs": ["shareswadil"],
        "func": dla_ext_016_shareswadil_zscore_2y,
    },
    "dla_ext_017_shareswadil_pct_rank_3y": {
        "inputs": ["shareswadil"],
        "func": dla_ext_017_shareswadil_pct_rank_3y,
    },
    "dla_ext_018_shareswadil_ewm_slope_63": {
        "inputs": ["shareswadil"],
        "func": dla_ext_018_shareswadil_ewm_slope_63,
    },
    "dla_ext_019_shareswadil_5y_pct": {
        "inputs": ["shareswadil"],
        "func": dla_ext_019_shareswadil_5y_pct,
    },
    "dla_ext_020_diluted_basic_gap_zscore_3y": {
        "inputs": ["shareswadil", "shareswa"],
        "func": dla_ext_020_diluted_basic_gap_zscore_3y,
    },
    "dla_ext_021_diluted_basic_gap_5y_pct_rank": {
        "inputs": ["shareswadil", "shareswa"],
        "func": dla_ext_021_diluted_basic_gap_5y_pct_rank,
    },
    "dla_ext_022_shareswadil_vs_sharesbas_zscore_3y": {
        "inputs": ["shareswadil", "sharesbas"],
        "func": dla_ext_022_shareswadil_vs_sharesbas_zscore_3y,
    },
    "dla_ext_023_shareswadil_growth_streak": {
        "inputs": ["shareswadil"],
        "func": dla_ext_023_shareswadil_growth_streak,
    },
    "dla_ext_024_sharesbas_growth_streak": {
        "inputs": ["sharesbas"],
        "func": dla_ext_024_sharesbas_growth_streak,
    },
    "dla_ext_025_ncfcommon_zscore_2y": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_025_ncfcommon_zscore_2y,
    },
    "dla_ext_026_ncfcommon_pct_rank_3y": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_026_ncfcommon_pct_rank_3y,
    },
    "dla_ext_027_ncfcommon_to_assets_ratio": {
        "inputs": ["ncfcommon", "assets"],
        "func": dla_ext_027_ncfcommon_to_assets_ratio,
    },
    "dla_ext_028_ncfcommon_to_equity_zscore_2y": {
        "inputs": ["ncfcommon", "equity"],
        "func": dla_ext_028_ncfcommon_to_equity_zscore_2y,
    },
    "dla_ext_029_ncfcommon_to_ncfo_ratio": {
        "inputs": ["ncfcommon", "ncfo"],
        "func": dla_ext_029_ncfcommon_to_ncfo_ratio,
    },
    "dla_ext_030_ncfcommon_trailing_5y_sum": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_030_ncfcommon_trailing_5y_sum,
    },
    "dla_ext_031_issuance_count_3y": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_031_issuance_count_3y,
    },
    "dla_ext_032_issuance_count_5y": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_032_issuance_count_5y,
    },
    "dla_ext_033_ncfcommon_ewm_slope_63": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_033_ncfcommon_ewm_slope_63,
    },
    "dla_ext_034_ncfcommon_issuance_streak": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_034_ncfcommon_issuance_streak,
    },
    "dla_ext_035_ncfcommon_large_raise_flag": {
        "inputs": ["ncfcommon", "assets"],
        "func": dla_ext_035_ncfcommon_large_raise_flag,
    },
    "dla_ext_036_ncfcommon_to_revenue_ratio": {
        "inputs": ["ncfcommon", "revenue"],
        "func": dla_ext_036_ncfcommon_to_revenue_ratio,
    },
    "dla_ext_037_sbcomp_zscore_2y": {
        "inputs": ["sbcomp"],
        "func": dla_ext_037_sbcomp_zscore_2y,
    },
    "dla_ext_038_sbcomp_pct_rank_3y": {
        "inputs": ["sbcomp"],
        "func": dla_ext_038_sbcomp_pct_rank_3y,
    },
    "dla_ext_039_sbcomp_trailing_3y_sum": {
        "inputs": ["sbcomp"],
        "func": dla_ext_039_sbcomp_trailing_3y_sum,
    },
    "dla_ext_040_sbcomp_trailing_5y_sum": {
        "inputs": ["sbcomp"],
        "func": dla_ext_040_sbcomp_trailing_5y_sum,
    },
    "dla_ext_041_sbcomp_to_revenue_zscore_2y": {
        "inputs": ["sbcomp", "revenue"],
        "func": dla_ext_041_sbcomp_to_revenue_zscore_2y,
    },
    "dla_ext_042_sbcomp_to_equity_ratio": {
        "inputs": ["sbcomp", "equity"],
        "func": dla_ext_042_sbcomp_to_equity_ratio,
    },
    "dla_ext_043_sbcomp_to_equity_zscore_2y": {
        "inputs": ["sbcomp", "equity"],
        "func": dla_ext_043_sbcomp_to_equity_zscore_2y,
    },
    "dla_ext_044_sbcomp_to_assets_ratio": {
        "inputs": ["sbcomp", "assets"],
        "func": dla_ext_044_sbcomp_to_assets_ratio,
    },
    "dla_ext_045_sbcomp_ewm_slope_63": {
        "inputs": ["sbcomp"],
        "func": dla_ext_045_sbcomp_ewm_slope_63,
    },
    "dla_ext_046_sbcomp_ncfcommon_combined": {
        "inputs": ["sbcomp", "ncfcommon"],
        "func": dla_ext_046_sbcomp_ncfcommon_combined,
    },
    "dla_ext_047_sbcomp_ncfcommon_to_revenue": {
        "inputs": ["sbcomp", "ncfcommon", "revenue"],
        "func": dla_ext_047_sbcomp_ncfcommon_to_revenue,
    },
    "dla_ext_048_sbcomp_to_ncfo_ratio": {
        "inputs": ["sbcomp", "ncfo"],
        "func": dla_ext_048_sbcomp_to_ncfo_ratio,
    },
    "dla_ext_049_dilution_intensity_score": {
        "inputs": ["sharesbas", "shareswa", "shareswadil"],
        "func": dla_ext_049_dilution_intensity_score,
    },
    "dla_ext_050_sharesbas_to_assets_ratio": {
        "inputs": ["sharesbas", "assets"],
        "func": dla_ext_050_sharesbas_to_assets_ratio,
    },
    "dla_ext_051_sharesbas_to_equity_ratio": {
        "inputs": ["sharesbas", "equity"],
        "func": dla_ext_051_sharesbas_to_equity_ratio,
    },
    "dla_ext_052_shareswa_yoy_pct_rank_3y": {
        "inputs": ["shareswa"],
        "func": dla_ext_052_shareswa_yoy_pct_rank_3y,
    },
    "dla_ext_053_shareswadil_to_sharesbas_pct_rank_3y": {
        "inputs": ["shareswadil", "sharesbas"],
        "func": dla_ext_053_shareswadil_to_sharesbas_pct_rank_3y,
    },
    "dla_ext_054_ncfcommon_to_ncfo_zscore_2y": {
        "inputs": ["ncfcommon", "ncfo"],
        "func": dla_ext_054_ncfcommon_to_ncfo_zscore_2y,
    },
    "dla_ext_055_sharesbas_ewm_accel": {
        "inputs": ["sharesbas"],
        "func": dla_ext_055_sharesbas_ewm_accel,
    },
    "dla_ext_056_dilution_vs_revenue_growth": {
        "inputs": ["sharesbas", "revenue"],
        "func": dla_ext_056_dilution_vs_revenue_growth,
    },
    "dla_ext_057_ncfcommon_skew_3y": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_057_ncfcommon_skew_3y,
    },
    "dla_ext_058_large_jump_streak": {
        "inputs": ["sharesbas"],
        "func": dla_ext_058_large_jump_streak,
    },
    "dla_ext_059_diluted_at_5y_high_flag": {
        "inputs": ["shareswadil"],
        "func": dla_ext_059_diluted_at_5y_high_flag,
    },
    "dla_ext_060_sharesbas_drawdown_from_3y_high": {
        "inputs": ["sharesbas"],
        "func": dla_ext_060_sharesbas_drawdown_from_3y_high,
    },
    "dla_ext_061_dilution_burden_score": {
        "inputs": ["sharesbas", "ncfcommon", "sbcomp"],
        "func": dla_ext_061_dilution_burden_score,
    },
    "dla_ext_062_ncfcommon_5y_pct_rank": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_062_ncfcommon_5y_pct_rank,
    },
    "dla_ext_063_sharesbas_skew_3y": {
        "inputs": ["sharesbas"],
        "func": dla_ext_063_sharesbas_skew_3y,
    },
    "dla_ext_064_shareswa_2y_pct": {
        "inputs": ["shareswa"],
        "func": dla_ext_064_shareswa_2y_pct,
    },
    "dla_ext_065_shareswadil_2y_pct": {
        "inputs": ["shareswadil"],
        "func": dla_ext_065_shareswadil_2y_pct,
    },
    "dla_ext_066_diluted_accel_flag": {
        "inputs": ["shareswadil"],
        "func": dla_ext_066_diluted_accel_flag,
    },
    "dla_ext_067_ncfcommon_yoy_pct_rank_3y": {
        "inputs": ["ncfcommon"],
        "func": dla_ext_067_ncfcommon_yoy_pct_rank_3y,
    },
    "dla_ext_068_sbcomp_yoy_pct": {
        "inputs": ["sbcomp"],
        "func": dla_ext_068_sbcomp_yoy_pct,
    },
    "dla_ext_069_sbcomp_yoy_pct_rank_3y": {
        "inputs": ["sbcomp"],
        "func": dla_ext_069_sbcomp_yoy_pct_rank_3y,
    },
    "dla_ext_070_sharesbas_new_high_streak": {
        "inputs": ["sharesbas"],
        "func": dla_ext_070_sharesbas_new_high_streak,
    },
    "dla_ext_071_ncfcommon_plus_sbcomp_to_equity": {
        "inputs": ["ncfcommon", "sbcomp", "equity"],
        "func": dla_ext_071_ncfcommon_plus_sbcomp_to_equity,
    },
    "dla_ext_072_dilution_vs_ncfo": {
        "inputs": ["ncfcommon", "sbcomp", "ncfo"],
        "func": dla_ext_072_dilution_vs_ncfo,
    },
    "dla_ext_073_sharesbas_2q_change": {
        "inputs": ["sharesbas"],
        "func": dla_ext_073_sharesbas_2q_change,
    },
    "dla_ext_074_shareswadil_2q_pct": {
        "inputs": ["shareswadil"],
        "func": dla_ext_074_shareswadil_2q_pct,
    },
    "dla_ext_075_dilution_composite_rank_3y": {
        "inputs": ["sharesbas", "shareswadil", "sbcomp"],
        "func": dla_ext_075_dilution_composite_rank_3y,
    },
}
