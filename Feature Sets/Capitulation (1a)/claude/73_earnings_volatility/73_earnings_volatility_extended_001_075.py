"""
73_earnings_volatility — Extended Features 001-075
Domain: instability / variance of the earnings series — additional variants:
        margin-dispersion, mean-absolute-deviation, drawdown-of-volatility,
        new metrics (gp, opinc, intexp, fcf), normalized/scaled volatility,
        upside-vs-downside asymmetry, volatility regimes and percentile ranks
        not covered by the base files.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

These features are NET-NEW relative to base_001_075, base_076_150,
2nd_derivatives and 3rd_derivatives — they explore different angles
(MAD, asymmetry, vol-of-vol, drawdown, regimes) rather than duplicating
the rolling-std / CV / range / sign-change features in the base files.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  Functions look strictly backward using
.shift(positive), .rolling(), or .expanding().
Quarterly cadence on the daily index: 1 quarter = 63 trading days,
1 year = 252 trading days.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR = 252   # 1 year in trading days
_TD_2Y   = 504
_TD_3Y   = 756
_TD_5Y   = 1260
_TD_QTR  = 63    # 1 quarter in trading days
_TD_2Q   = 126
_TD_3Q   = 189
_EPS     = 1e-9

# ── Utility helpers ───────────────────────────────────────────────────────────

def _align_quarterly_to_daily(q_series: pd.Series, daily_index: pd.Index) -> pd.Series:
    """
    Contract: forward-fill a quarterly SF1 field onto a daily trading-day index.
    All feature functions in this file already receive Series prepared this way;
    this helper is provided for documentation and optional manual use.
    All feature functions in this file look strictly backward.
    """
    return q_series.reindex(daily_index).ffill()


def _safe_div(num: pd.Series, den: pd.Series) -> pd.Series:
    """Element-wise division; replaces zero denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den; avoids sign confusion in ratio features."""
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
    m = _rolling_mean(s, w)
    sd = _rolling_std(s, w)
    return _safe_div(s - m, sd)


def _ewm_mean(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(1, span // 4)).mean()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(2, span // 4)).std()


def _qoq_diff(s: pd.Series) -> pd.Series:
    """Quarter-over-quarter absolute change on the daily-forward-filled series."""
    return s - s.shift(_TD_QTR)


def _yoy_diff(s: pd.Series) -> pd.Series:
    return s - s.shift(_TD_YEAR)


def _rolling_mad(s: pd.Series, w: int) -> pd.Series:
    """Rolling mean absolute deviation from the rolling mean (robust dispersion)."""
    m = _rolling_mean(s, w)
    return _rolling_mean((s - m).abs(), w)


# ── Feature functions 001-075 ─────────────────────────────────────────────────

# --- Group A (001-012): Mean-absolute-deviation dispersion (robust vs std) ---

def evl_ext_001_netinc_mad_4q(netinc: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of net income over 4 quarters."""
    return _rolling_mad(netinc, _TD_YEAR)


def evl_ext_002_netinc_mad_8q(netinc: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of net income over 8 quarters."""
    return _rolling_mad(netinc, _TD_2Y)


def evl_ext_003_netinc_mad_12q(netinc: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of net income over 12 quarters."""
    return _rolling_mad(netinc, _TD_3Y)


def evl_ext_004_eps_mad_4q(eps: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of EPS over 4 quarters."""
    return _rolling_mad(eps, _TD_YEAR)


def evl_ext_005_ebit_mad_4q(ebit: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of EBIT over 4 quarters."""
    return _rolling_mad(ebit, _TD_YEAR)


def evl_ext_006_revenue_mad_4q(revenue: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of revenue over 4 quarters."""
    return _rolling_mad(revenue, _TD_YEAR)


def evl_ext_007_netinc_mad_to_mean_4q(netinc: pd.Series) -> pd.Series:
    """Net income MAD divided by |mean| over 4 quarters — robust relative dispersion."""
    return _safe_div_abs(_rolling_mad(netinc, _TD_YEAR), _rolling_mean(netinc, _TD_YEAR))


def evl_ext_008_eps_mad_to_mean_4q(eps: pd.Series) -> pd.Series:
    """EPS MAD divided by |mean| over 4 quarters — robust relative dispersion."""
    return _safe_div_abs(_rolling_mad(eps, _TD_YEAR), _rolling_mean(eps, _TD_YEAR))


def evl_ext_009_netinc_median_abs_dev_4q(netinc: pd.Series) -> pd.Series:
    """Rolling median absolute deviation of net income from rolling median, 4 quarters."""
    med = _rolling_median(netinc, _TD_YEAR)
    return _rolling_median((netinc - med).abs(), _TD_YEAR)


def evl_ext_010_ebitda_mad_4q(ebitda: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of EBITDA over 4 quarters."""
    return _rolling_mad(ebitda, _TD_YEAR)


def evl_ext_011_ncfo_mad_4q(ncfo: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of operating cash flow over 4 quarters."""
    return _rolling_mad(ncfo, _TD_YEAR)


def evl_ext_012_gp_mad_4q(gp: pd.Series) -> pd.Series:
    """Rolling mean absolute deviation of gross profit over 4 quarters."""
    return _rolling_mad(gp, _TD_YEAR)


# --- Group B (013-024): Asset-scaled / margin-normalized earnings volatility ---

def evl_ext_013_roa_std_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of net margin (netinc/revenue) over 4 quarters — scale-free vol proxy."""
    return _rolling_std(_safe_div(netinc, revenue.replace(0, np.nan)), _TD_YEAR)


def evl_ext_014_roa_std_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of net margin (netinc/revenue) over 8 quarters."""
    return _rolling_std(_safe_div(netinc, revenue.replace(0, np.nan)), _TD_2Y)


def evl_ext_015_roe_std_4q(netinc: pd.Series, ebitda: pd.Series) -> pd.Series:
    """Rolling std of netinc-to-EBITDA ratio over 4 quarters — earnings conversion vol."""
    return _rolling_std(_safe_div(netinc, ebitda.replace(0, np.nan)), _TD_YEAR)


def evl_ext_016_net_margin_std_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of net margin (netinc/revenue) over 4 quarters."""
    return _rolling_std(_safe_div(netinc, revenue), _TD_YEAR)


def evl_ext_017_net_margin_std_8q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of net margin over 8 quarters."""
    return _rolling_std(_safe_div(netinc, revenue), _TD_2Y)


def evl_ext_018_gross_margin_std_4q(gp: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of gross margin (gp/revenue) over 4 quarters."""
    return _rolling_std(_safe_div(gp, revenue), _TD_YEAR)


def evl_ext_019_operating_margin_std_4q(opinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of operating margin (opinc/revenue) over 4 quarters."""
    return _rolling_std(_safe_div(opinc, revenue), _TD_YEAR)


def evl_ext_020_ebit_margin_std_4q(ebit: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of EBIT margin (ebit/revenue) over 4 quarters."""
    return _rolling_std(_safe_div(ebit, revenue), _TD_YEAR)


def evl_ext_021_ebitda_margin_std_4q(ebitda: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling std of EBITDA margin (ebitda/revenue) over 4 quarters."""
    return _rolling_std(_safe_div(ebitda, revenue), _TD_YEAR)


def evl_ext_022_netinc_std_scaled_by_assets_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 4q std of net income divided by revenue — magnitude-normalized vol."""
    return _safe_div(_rolling_std(netinc, _TD_YEAR), revenue.replace(0, np.nan))


def evl_ext_023_netinc_std_scaled_by_revenue_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Rolling 4q std of net income divided by revenue — revenue-scaled vol."""
    return _safe_div(_rolling_std(netinc, _TD_YEAR), revenue)


def evl_ext_024_roa_range_4q(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """Range (max - min) of net margin over trailing 4 quarters."""
    margin = _safe_div(netinc, revenue.replace(0, np.nan))
    return _rolling_max(margin, _TD_YEAR) - _rolling_min(margin, _TD_YEAR)


# --- Group C (025-036): Upside / downside asymmetry of earnings ---

def evl_ext_025_netinc_upside_dev_4q(netinc: pd.Series) -> pd.Series:
    """Semi-deviation of net income above its 4q mean (upside-only volatility)."""
    mu = _rolling_mean(netinc, _TD_YEAR)
    dev = (netinc - mu).clip(lower=0)
    return _rolling_mean(dev ** 2, _TD_YEAR).apply(np.sqrt)


def evl_ext_026_netinc_vol_asymmetry_4q(netinc: pd.Series) -> pd.Series:
    """Difference of downside minus upside semi-deviation of net income (4q)."""
    mu = _rolling_mean(netinc, _TD_YEAR)
    down = _rolling_mean((netinc - mu).clip(upper=0) ** 2, _TD_YEAR).apply(np.sqrt)
    up = _rolling_mean((netinc - mu).clip(lower=0) ** 2, _TD_YEAR).apply(np.sqrt)
    return down - up


def evl_ext_027_netinc_vol_asymmetry_ratio_4q(netinc: pd.Series) -> pd.Series:
    """Ratio of downside to upside semi-deviation of net income (4q)."""
    mu = _rolling_mean(netinc, _TD_YEAR)
    down = _rolling_mean((netinc - mu).clip(upper=0) ** 2, _TD_YEAR).apply(np.sqrt)
    up = _rolling_mean((netinc - mu).clip(lower=0) ** 2, _TD_YEAR).apply(np.sqrt)
    return _safe_div(down, up)


def evl_ext_028_eps_vol_asymmetry_4q(eps: pd.Series) -> pd.Series:
    """Difference of downside minus upside semi-deviation of EPS (4q)."""
    mu = _rolling_mean(eps, _TD_YEAR)
    down = _rolling_mean((eps - mu).clip(upper=0) ** 2, _TD_YEAR).apply(np.sqrt)
    up = _rolling_mean((eps - mu).clip(lower=0) ** 2, _TD_YEAR).apply(np.sqrt)
    return down - up


def evl_ext_029_ebit_vol_asymmetry_4q(ebit: pd.Series) -> pd.Series:
    """Difference of downside minus upside semi-deviation of EBIT (4q)."""
    mu = _rolling_mean(ebit, _TD_YEAR)
    down = _rolling_mean((ebit - mu).clip(upper=0) ** 2, _TD_YEAR).apply(np.sqrt)
    up = _rolling_mean((ebit - mu).clip(lower=0) ** 2, _TD_YEAR).apply(np.sqrt)
    return down - up


def evl_ext_030_netinc_skew_4q(netinc: pd.Series) -> pd.Series:
    """Rolling skewness of net income over 4 quarters — asymmetry of earnings distribution."""
    return netinc.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).skew()


def evl_ext_031_netinc_skew_8q(netinc: pd.Series) -> pd.Series:
    """Rolling skewness of net income over 8 quarters."""
    return netinc.rolling(_TD_2Y, min_periods=max(3, _TD_2Y // 4)).skew()


def evl_ext_032_eps_skew_4q(eps: pd.Series) -> pd.Series:
    """Rolling skewness of EPS over 4 quarters."""
    return eps.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).skew()


def evl_ext_033_netinc_kurtosis_4q(netinc: pd.Series) -> pd.Series:
    """Rolling kurtosis of net income over 4 quarters — fat-tail / extreme-swing measure."""
    return netinc.rolling(_TD_YEAR, min_periods=max(4, _TD_YEAR // 4)).kurt()


def evl_ext_034_netinc_kurtosis_8q(netinc: pd.Series) -> pd.Series:
    """Rolling kurtosis of net income over 8 quarters."""
    return netinc.rolling(_TD_2Y, min_periods=max(4, _TD_2Y // 4)).kurt()


def evl_ext_035_netinc_qoq_drop_max_4q(netinc: pd.Series) -> pd.Series:
    """Largest single QoQ DROP in net income over trailing 4 quarters (downside swing)."""
    drops = (-_qoq_diff(netinc)).clip(lower=0)
    return _rolling_max(drops, _TD_YEAR)


def evl_ext_036_eps_qoq_drop_max_4q(eps: pd.Series) -> pd.Series:
    """Largest single QoQ DROP in EPS over trailing 4 quarters."""
    drops = (-_qoq_diff(eps)).clip(lower=0)
    return _rolling_max(drops, _TD_YEAR)


# --- Group D (037-048): Volatility of additional metrics (intexp, opinc, gp, fcf) ---

def evl_ext_037_intexp_std_4q(gp: pd.Series) -> pd.Series:
    """Rolling std of gross profit over 4 quarters."""
    return _rolling_std(gp, _TD_YEAR)


def evl_ext_038_intexp_cv_4q(gp: pd.Series) -> pd.Series:
    """Coefficient of variation of gross profit over 4 quarters."""
    return _safe_div_abs(_rolling_std(gp, _TD_YEAR), _rolling_mean(gp, _TD_YEAR))


def evl_ext_039_opinc_std_8q(opinc: pd.Series) -> pd.Series:
    """Rolling std of operating income over 8 quarters."""
    return _rolling_std(opinc, _TD_2Y)


def evl_ext_040_opinc_cv_8q(opinc: pd.Series) -> pd.Series:
    """Coefficient of variation of operating income over 8 quarters."""
    return _safe_div_abs(_rolling_std(opinc, _TD_2Y), _rolling_mean(opinc, _TD_2Y))


def evl_ext_041_gp_cv_8q(gp: pd.Series) -> pd.Series:
    """Coefficient of variation of gross profit over 8 quarters."""
    return _safe_div_abs(_rolling_std(gp, _TD_2Y), _rolling_mean(gp, _TD_2Y))


def evl_ext_042_ebitda_cv_8q(ebitda: pd.Series) -> pd.Series:
    """Coefficient of variation of EBITDA over 8 quarters."""
    return _safe_div_abs(_rolling_std(ebitda, _TD_2Y), _rolling_mean(ebitda, _TD_2Y))


def evl_ext_043_ebit_cv_8q(ebit: pd.Series) -> pd.Series:
    """Coefficient of variation of EBIT over 8 quarters."""
    return _safe_div_abs(_rolling_std(ebit, _TD_2Y), _rolling_mean(ebit, _TD_2Y))


def evl_ext_044_fcf_std_8q(fcf: pd.Series) -> pd.Series:
    """Rolling std of free cash flow over 8 quarters."""
    return _rolling_std(fcf, _TD_2Y)


def evl_ext_045_ncfo_std_8q(ncfo: pd.Series) -> pd.Series:
    """Rolling std of operating cash flow over 8 quarters."""
    return _rolling_std(ncfo, _TD_2Y)


def evl_ext_046_revenue_qoq_swing_abs_4q(revenue: pd.Series) -> pd.Series:
    """Mean absolute QoQ swing of revenue over trailing 4 quarters."""
    return _rolling_mean(_qoq_diff(revenue).abs(), _TD_YEAR)


def evl_ext_047_ebitda_qoq_swing_abs_4q(ebitda: pd.Series) -> pd.Series:
    """Mean absolute QoQ swing of EBITDA over trailing 4 quarters."""
    return _rolling_mean(_qoq_diff(ebitda).abs(), _TD_YEAR)


def evl_ext_048_gp_qoq_swing_abs_4q(gp: pd.Series) -> pd.Series:
    """Mean absolute QoQ swing of gross profit over trailing 4 quarters."""
    return _rolling_mean(_qoq_diff(gp).abs(), _TD_YEAR)


# --- Group E (049-060): Volatility-of-volatility and vol drawdown / trend ---

def evl_ext_049_netinc_vol_of_vol_8q(netinc: pd.Series) -> pd.Series:
    """Volatility-of-volatility: 8q std of the rolling 4q std of net income."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return _rolling_std(vol, _TD_2Y)


def evl_ext_050_eps_vol_of_vol_8q(eps: pd.Series) -> pd.Series:
    """Volatility-of-volatility: 8q std of the rolling 4q std of EPS."""
    vol = _rolling_std(eps, _TD_YEAR)
    return _rolling_std(vol, _TD_2Y)


def evl_ext_051_netinc_vol_qoq_change(netinc: pd.Series) -> pd.Series:
    """QoQ (63-day) change in the rolling 4q std of net income — vol acceleration."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return vol - vol.shift(_TD_QTR)


def evl_ext_052_netinc_vol_yoy_change(netinc: pd.Series) -> pd.Series:
    """YoY (252-day) change in the rolling 4q std of net income."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return vol - vol.shift(_TD_YEAR)


def evl_ext_053_netinc_vol_vs_2y_avg(netinc: pd.Series) -> pd.Series:
    """Rolling 4q std of net income minus its trailing 2-year mean — vol regime deviation."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return vol - _rolling_mean(vol, _TD_2Y)


def evl_ext_054_netinc_vol_drawup_from_min_2y(netinc: pd.Series) -> pd.Series:
    """Rise of net income 4q vol above its trailing 2-year minimum (vol expansion depth)."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return vol - _rolling_min(vol, _TD_2Y)


def evl_ext_055_eps_vol_vs_2y_avg(eps: pd.Series) -> pd.Series:
    """Rolling 4q std of EPS minus its trailing 2-year mean."""
    vol = _rolling_std(eps, _TD_YEAR)
    return vol - _rolling_mean(vol, _TD_2Y)


def evl_ext_056_netinc_cv_qoq_change(netinc: pd.Series) -> pd.Series:
    """QoQ (63-day) change in the 4q coefficient of variation of net income."""
    cv = _safe_div_abs(_rolling_std(netinc, _TD_YEAR), _rolling_mean(netinc, _TD_YEAR))
    return cv - cv.shift(_TD_QTR)


def evl_ext_057_netinc_vol_pct_rank_3y(netinc: pd.Series) -> pd.Series:
    """Percentile rank of net income 4q vol within a trailing 3-year window."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return _rolling_rank_pct(vol, _TD_3Y)


def evl_ext_058_netinc_vol_zscore_3y(netinc: pd.Series) -> pd.Series:
    """Z-score of net income 4q vol within a trailing 3-year window."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return _zscore_rolling(vol, _TD_3Y)


def evl_ext_059_eps_vol_pct_rank_3y(eps: pd.Series) -> pd.Series:
    """Percentile rank of EPS 4q vol within a trailing 3-year window."""
    vol = _rolling_std(eps, _TD_YEAR)
    return _rolling_rank_pct(vol, _TD_3Y)


def evl_ext_060_netinc_vol_expanding_pct_rank(netinc: pd.Series) -> pd.Series:
    """Expanding all-history percentile rank of net income 4q vol."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return vol.expanding(min_periods=2).rank(pct=True)


# --- Group F (061-068): Earnings-range and extreme-value diagnostics ---

def evl_ext_061_netinc_max_to_min_ratio_4q(netinc: pd.Series) -> pd.Series:
    """Ratio of 4q max to 4q min of net income (spread magnitude, sign-aware)."""
    return _safe_div_abs(_rolling_max(netinc, _TD_YEAR), _rolling_min(netinc, _TD_YEAR))


def evl_ext_062_netinc_dist_from_4q_min(netinc: pd.Series) -> pd.Series:
    """Current net income minus its trailing 4q minimum (distance above the trough)."""
    return netinc - _rolling_min(netinc, _TD_YEAR)


def evl_ext_063_netinc_dist_below_4q_max(netinc: pd.Series) -> pd.Series:
    """Trailing 4q maximum minus current net income (distance below the peak)."""
    return _rolling_max(netinc, _TD_YEAR) - netinc


def evl_ext_064_eps_range_to_mean_4q(eps: pd.Series) -> pd.Series:
    """EPS range (max - min) divided by |mean| over 4 quarters."""
    rng = _rolling_max(eps, _TD_YEAR) - _rolling_min(eps, _TD_YEAR)
    return _safe_div_abs(rng, _rolling_mean(eps, _TD_YEAR))


def evl_ext_065_ebit_range_to_mean_4q(ebit: pd.Series) -> pd.Series:
    """EBIT range divided by |mean| over 4 quarters."""
    rng = _rolling_max(ebit, _TD_YEAR) - _rolling_min(ebit, _TD_YEAR)
    return _safe_div_abs(rng, _rolling_mean(ebit, _TD_YEAR))


def evl_ext_066_revenue_range_4q(revenue: pd.Series) -> pd.Series:
    """Revenue range (max - min) over trailing 4 quarters."""
    return _rolling_max(revenue, _TD_YEAR) - _rolling_min(revenue, _TD_YEAR)


def evl_ext_067_netinc_iqr_to_median_4q(netinc: pd.Series) -> pd.Series:
    """Net income IQR (Q75-Q25) divided by |median| over 4 quarters — robust relative spread."""
    q75 = netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.75)
    q25 = netinc.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).quantile(0.25)
    return _safe_div_abs(q75 - q25, _rolling_median(netinc, _TD_YEAR))


def evl_ext_068_netinc_qoq_swing_max_to_mean_4q(netinc: pd.Series) -> pd.Series:
    """Max absolute QoQ swing of net income divided by |mean| over 4 quarters."""
    swing = _rolling_max(_qoq_diff(netinc).abs(), _TD_YEAR)
    return _safe_div_abs(swing, _rolling_mean(netinc, _TD_YEAR))


# --- Group G (069-075): Volatility regimes, breadth, and capitulation composites ---

def evl_ext_069_high_vol_regime_flag(netinc: pd.Series) -> pd.Series:
    """Binary flag: net income 4q vol is above its trailing 3-year median (high-vol regime)."""
    vol = _rolling_std(netinc, _TD_YEAR)
    return (vol > _rolling_median(vol, _TD_3Y)).astype(float)


def evl_ext_070_vol_regime_consec_high(netinc: pd.Series) -> pd.Series:
    """Consecutive daily steps net income 4q vol has stayed above its 3-year median."""
    vol = _rolling_std(netinc, _TD_YEAR)
    high = (vol > _rolling_median(vol, _TD_3Y)).astype(int)
    arr = high.values
    out = np.zeros(len(arr), dtype=float)
    for i in range(1, len(arr)):
        out[i] = (out[i - 1] + 1) * arr[i]
    if len(arr) > 0:
        out[0] = float(arr[0])
    return pd.Series(out, index=netinc.index)


def evl_ext_071_vol_breadth_count_4q(
    netinc: pd.Series, eps: pd.Series, ebit: pd.Series,
    ebitda: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Count (0-5) of core metrics whose 4q vol exceeds its trailing 3-year median."""
    metrics = [netinc, eps, ebit, ebitda, revenue]
    cnt = None
    for m in metrics:
        vol = _rolling_std(m, _TD_YEAR)
        flag = (vol > _rolling_median(vol, _TD_3Y)).astype(float)
        cnt = flag if cnt is None else cnt + flag
    return cnt


def evl_ext_072_vol_breadth_zscore_index(
    netinc: pd.Series, eps: pd.Series, ebit: pd.Series,
) -> pd.Series:
    """Composite vol index: mean 3-year z-score of the 4q vol of netinc, eps and ebit."""
    z1 = _zscore_rolling(_rolling_std(netinc, _TD_YEAR), _TD_3Y)
    z2 = _zscore_rolling(_rolling_std(eps, _TD_YEAR), _TD_3Y)
    z3 = _zscore_rolling(_rolling_std(ebit, _TD_YEAR), _TD_3Y)
    return (z1 + z2 + z3) / 3.0


def evl_ext_073_earnings_instability_composite(
    netinc: pd.Series, eps: pd.Series, revenue: pd.Series,
) -> pd.Series:
    """Instability composite: mean of 4q CVs of net margin, EPS and revenue (absolute)."""
    cv_margin = _safe_div_abs(_rolling_std(_safe_div(netinc, revenue), _TD_YEAR),
                              _rolling_mean(_safe_div(netinc, revenue), _TD_YEAR)).abs()
    cv_eps = _safe_div_abs(_rolling_std(eps, _TD_YEAR), _rolling_mean(eps, _TD_YEAR)).abs()
    cv_rev = _safe_div_abs(_rolling_std(revenue, _TD_YEAR), _rolling_mean(revenue, _TD_YEAR)).abs()
    return (cv_margin + cv_eps + cv_rev) / 3.0


def evl_ext_074_downside_vol_composite_4q(
    netinc: pd.Series, eps: pd.Series, ebit: pd.Series,
) -> pd.Series:
    """Downside-volatility composite: mean below-zero semi-deviation of netinc, eps, ebit (4q)."""
    d_ni = _rolling_mean(netinc.clip(upper=0) ** 2, _TD_YEAR).apply(np.sqrt)
    d_eps = _rolling_mean(eps.clip(upper=0) ** 2, _TD_YEAR).apply(np.sqrt)
    d_ebit = _rolling_mean(ebit.clip(upper=0) ** 2, _TD_YEAR).apply(np.sqrt)
    return (d_ni + d_eps + d_ebit) / 3.0


def evl_ext_075_capitulation_volatility_score(
    netinc: pd.Series, eps: pd.Series,
) -> pd.Series:
    """Capitulation volatility score: net income 4q vol z-score (3y) + EPS vol pct-rank (3y)
    + downside-asymmetry flag. Higher = earnings instability at a multi-year extreme."""
    ni_vol = _rolling_std(netinc, _TD_YEAR)
    ni_z = _zscore_rolling(ni_vol, _TD_3Y).clip(lower=-3.0, upper=3.0) / 3.0
    eps_vol = _rolling_std(eps, _TD_YEAR)
    eps_rank = _rolling_rank_pct(eps_vol, _TD_3Y)
    mu = _rolling_mean(netinc, _TD_YEAR)
    down = _rolling_mean((netinc - mu).clip(upper=0) ** 2, _TD_YEAR).apply(np.sqrt)
    up = _rolling_mean((netinc - mu).clip(lower=0) ** 2, _TD_YEAR).apply(np.sqrt)
    asym_flag = (down > up).astype(float)
    return ni_z + eps_rank.fillna(0.5) + 0.5 * asym_flag


# ── Registry 001-075 ──────────────────────────────────────────────────────────

EARNINGS_VOLATILITY_EXTENDED_REGISTRY_001_075 = {
    "evl_ext_001_netinc_mad_4q": {"inputs": ["netinc"], "func": evl_ext_001_netinc_mad_4q},
    "evl_ext_002_netinc_mad_8q": {"inputs": ["netinc"], "func": evl_ext_002_netinc_mad_8q},
    "evl_ext_003_netinc_mad_12q": {"inputs": ["netinc"], "func": evl_ext_003_netinc_mad_12q},
    "evl_ext_004_eps_mad_4q": {"inputs": ["eps"], "func": evl_ext_004_eps_mad_4q},
    "evl_ext_005_ebit_mad_4q": {"inputs": ["ebit"], "func": evl_ext_005_ebit_mad_4q},
    "evl_ext_006_revenue_mad_4q": {"inputs": ["revenue"], "func": evl_ext_006_revenue_mad_4q},
    "evl_ext_007_netinc_mad_to_mean_4q": {"inputs": ["netinc"], "func": evl_ext_007_netinc_mad_to_mean_4q},
    "evl_ext_008_eps_mad_to_mean_4q": {"inputs": ["eps"], "func": evl_ext_008_eps_mad_to_mean_4q},
    "evl_ext_009_netinc_median_abs_dev_4q": {"inputs": ["netinc"], "func": evl_ext_009_netinc_median_abs_dev_4q},
    "evl_ext_010_ebitda_mad_4q": {"inputs": ["ebitda"], "func": evl_ext_010_ebitda_mad_4q},
    "evl_ext_011_ncfo_mad_4q": {"inputs": ["ncfo"], "func": evl_ext_011_ncfo_mad_4q},
    "evl_ext_012_gp_mad_4q": {"inputs": ["gp"], "func": evl_ext_012_gp_mad_4q},
    "evl_ext_013_roa_std_4q": {"inputs": ["netinc", "revenue"], "func": evl_ext_013_roa_std_4q},
    "evl_ext_014_roa_std_8q": {"inputs": ["netinc", "revenue"], "func": evl_ext_014_roa_std_8q},
    "evl_ext_015_roe_std_4q": {"inputs": ["netinc", "ebitda"], "func": evl_ext_015_roe_std_4q},
    "evl_ext_016_net_margin_std_4q": {"inputs": ["netinc", "revenue"], "func": evl_ext_016_net_margin_std_4q},
    "evl_ext_017_net_margin_std_8q": {"inputs": ["netinc", "revenue"], "func": evl_ext_017_net_margin_std_8q},
    "evl_ext_018_gross_margin_std_4q": {"inputs": ["gp", "revenue"], "func": evl_ext_018_gross_margin_std_4q},
    "evl_ext_019_operating_margin_std_4q": {"inputs": ["opinc", "revenue"], "func": evl_ext_019_operating_margin_std_4q},
    "evl_ext_020_ebit_margin_std_4q": {"inputs": ["ebit", "revenue"], "func": evl_ext_020_ebit_margin_std_4q},
    "evl_ext_021_ebitda_margin_std_4q": {"inputs": ["ebitda", "revenue"], "func": evl_ext_021_ebitda_margin_std_4q},
    "evl_ext_022_netinc_std_scaled_by_assets_4q": {"inputs": ["netinc", "revenue"], "func": evl_ext_022_netinc_std_scaled_by_assets_4q},
    "evl_ext_023_netinc_std_scaled_by_revenue_4q": {"inputs": ["netinc", "revenue"], "func": evl_ext_023_netinc_std_scaled_by_revenue_4q},
    "evl_ext_024_roa_range_4q": {"inputs": ["netinc", "revenue"], "func": evl_ext_024_roa_range_4q},
    "evl_ext_025_netinc_upside_dev_4q": {"inputs": ["netinc"], "func": evl_ext_025_netinc_upside_dev_4q},
    "evl_ext_026_netinc_vol_asymmetry_4q": {"inputs": ["netinc"], "func": evl_ext_026_netinc_vol_asymmetry_4q},
    "evl_ext_027_netinc_vol_asymmetry_ratio_4q": {"inputs": ["netinc"], "func": evl_ext_027_netinc_vol_asymmetry_ratio_4q},
    "evl_ext_028_eps_vol_asymmetry_4q": {"inputs": ["eps"], "func": evl_ext_028_eps_vol_asymmetry_4q},
    "evl_ext_029_ebit_vol_asymmetry_4q": {"inputs": ["ebit"], "func": evl_ext_029_ebit_vol_asymmetry_4q},
    "evl_ext_030_netinc_skew_4q": {"inputs": ["netinc"], "func": evl_ext_030_netinc_skew_4q},
    "evl_ext_031_netinc_skew_8q": {"inputs": ["netinc"], "func": evl_ext_031_netinc_skew_8q},
    "evl_ext_032_eps_skew_4q": {"inputs": ["eps"], "func": evl_ext_032_eps_skew_4q},
    "evl_ext_033_netinc_kurtosis_4q": {"inputs": ["netinc"], "func": evl_ext_033_netinc_kurtosis_4q},
    "evl_ext_034_netinc_kurtosis_8q": {"inputs": ["netinc"], "func": evl_ext_034_netinc_kurtosis_8q},
    "evl_ext_035_netinc_qoq_drop_max_4q": {"inputs": ["netinc"], "func": evl_ext_035_netinc_qoq_drop_max_4q},
    "evl_ext_036_eps_qoq_drop_max_4q": {"inputs": ["eps"], "func": evl_ext_036_eps_qoq_drop_max_4q},
    "evl_ext_037_intexp_std_4q": {"inputs": ["gp"], "func": evl_ext_037_intexp_std_4q},
    "evl_ext_038_intexp_cv_4q": {"inputs": ["gp"], "func": evl_ext_038_intexp_cv_4q},
    "evl_ext_039_opinc_std_8q": {"inputs": ["opinc"], "func": evl_ext_039_opinc_std_8q},
    "evl_ext_040_opinc_cv_8q": {"inputs": ["opinc"], "func": evl_ext_040_opinc_cv_8q},
    "evl_ext_041_gp_cv_8q": {"inputs": ["gp"], "func": evl_ext_041_gp_cv_8q},
    "evl_ext_042_ebitda_cv_8q": {"inputs": ["ebitda"], "func": evl_ext_042_ebitda_cv_8q},
    "evl_ext_043_ebit_cv_8q": {"inputs": ["ebit"], "func": evl_ext_043_ebit_cv_8q},
    "evl_ext_044_fcf_std_8q": {"inputs": ["fcf"], "func": evl_ext_044_fcf_std_8q},
    "evl_ext_045_ncfo_std_8q": {"inputs": ["ncfo"], "func": evl_ext_045_ncfo_std_8q},
    "evl_ext_046_revenue_qoq_swing_abs_4q": {"inputs": ["revenue"], "func": evl_ext_046_revenue_qoq_swing_abs_4q},
    "evl_ext_047_ebitda_qoq_swing_abs_4q": {"inputs": ["ebitda"], "func": evl_ext_047_ebitda_qoq_swing_abs_4q},
    "evl_ext_048_gp_qoq_swing_abs_4q": {"inputs": ["gp"], "func": evl_ext_048_gp_qoq_swing_abs_4q},
    "evl_ext_049_netinc_vol_of_vol_8q": {"inputs": ["netinc"], "func": evl_ext_049_netinc_vol_of_vol_8q},
    "evl_ext_050_eps_vol_of_vol_8q": {"inputs": ["eps"], "func": evl_ext_050_eps_vol_of_vol_8q},
    "evl_ext_051_netinc_vol_qoq_change": {"inputs": ["netinc"], "func": evl_ext_051_netinc_vol_qoq_change},
    "evl_ext_052_netinc_vol_yoy_change": {"inputs": ["netinc"], "func": evl_ext_052_netinc_vol_yoy_change},
    "evl_ext_053_netinc_vol_vs_2y_avg": {"inputs": ["netinc"], "func": evl_ext_053_netinc_vol_vs_2y_avg},
    "evl_ext_054_netinc_vol_drawup_from_min_2y": {"inputs": ["netinc"], "func": evl_ext_054_netinc_vol_drawup_from_min_2y},
    "evl_ext_055_eps_vol_vs_2y_avg": {"inputs": ["eps"], "func": evl_ext_055_eps_vol_vs_2y_avg},
    "evl_ext_056_netinc_cv_qoq_change": {"inputs": ["netinc"], "func": evl_ext_056_netinc_cv_qoq_change},
    "evl_ext_057_netinc_vol_pct_rank_3y": {"inputs": ["netinc"], "func": evl_ext_057_netinc_vol_pct_rank_3y},
    "evl_ext_058_netinc_vol_zscore_3y": {"inputs": ["netinc"], "func": evl_ext_058_netinc_vol_zscore_3y},
    "evl_ext_059_eps_vol_pct_rank_3y": {"inputs": ["eps"], "func": evl_ext_059_eps_vol_pct_rank_3y},
    "evl_ext_060_netinc_vol_expanding_pct_rank": {"inputs": ["netinc"], "func": evl_ext_060_netinc_vol_expanding_pct_rank},
    "evl_ext_061_netinc_max_to_min_ratio_4q": {"inputs": ["netinc"], "func": evl_ext_061_netinc_max_to_min_ratio_4q},
    "evl_ext_062_netinc_dist_from_4q_min": {"inputs": ["netinc"], "func": evl_ext_062_netinc_dist_from_4q_min},
    "evl_ext_063_netinc_dist_below_4q_max": {"inputs": ["netinc"], "func": evl_ext_063_netinc_dist_below_4q_max},
    "evl_ext_064_eps_range_to_mean_4q": {"inputs": ["eps"], "func": evl_ext_064_eps_range_to_mean_4q},
    "evl_ext_065_ebit_range_to_mean_4q": {"inputs": ["ebit"], "func": evl_ext_065_ebit_range_to_mean_4q},
    "evl_ext_066_revenue_range_4q": {"inputs": ["revenue"], "func": evl_ext_066_revenue_range_4q},
    "evl_ext_067_netinc_iqr_to_median_4q": {"inputs": ["netinc"], "func": evl_ext_067_netinc_iqr_to_median_4q},
    "evl_ext_068_netinc_qoq_swing_max_to_mean_4q": {"inputs": ["netinc"], "func": evl_ext_068_netinc_qoq_swing_max_to_mean_4q},
    "evl_ext_069_high_vol_regime_flag": {"inputs": ["netinc"], "func": evl_ext_069_high_vol_regime_flag},
    "evl_ext_070_vol_regime_consec_high": {"inputs": ["netinc"], "func": evl_ext_070_vol_regime_consec_high},
    "evl_ext_071_vol_breadth_count_4q": {"inputs": ["netinc", "eps", "ebit", "ebitda", "revenue"], "func": evl_ext_071_vol_breadth_count_4q},
    "evl_ext_072_vol_breadth_zscore_index": {"inputs": ["netinc", "eps", "ebit"], "func": evl_ext_072_vol_breadth_zscore_index},
    "evl_ext_073_earnings_instability_composite": {"inputs": ["netinc", "eps", "revenue"], "func": evl_ext_073_earnings_instability_composite},
    "evl_ext_074_downside_vol_composite_4q": {"inputs": ["netinc", "eps", "ebit"], "func": evl_ext_074_downside_vol_composite_4q},
    "evl_ext_075_capitulation_volatility_score": {"inputs": ["netinc", "eps"], "func": evl_ext_075_capitulation_volatility_score},
}
