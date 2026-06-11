"""institutional_ownership_snapshot base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses (continued in __base__076_150.py for 150 total).
Inputs: Sharadar SF3/SF3A institutional aggregates plus SF1 share counts and
quarter-end SEP marketcap/close. Cadence is quarterly. PIT-clean: right-anchored
rolling with explicit min_periods, no centered windows, no .shift(-N).
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


def _safe_log(s, eps=1e-12):
    return np.log(s.where(s > eps, np.nan))


def _safe_div(num, den):
    if isinstance(den, pd.Series):
        d = den.replace(0, np.nan)
    else:
        d = np.where(den == 0, np.nan, den)
    out = num / d
    if isinstance(out, pd.Series):
        return out.replace([np.inf, -np.inf], np.nan)
    idx = num.index if hasattr(num, "index") else None
    return pd.Series(out, index=idx).replace([np.inf, -np.inf], np.nan)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _qoq(s):
    return s.diff()


def _yoy(s):
    return s.diff(4)


def _qoq_pct(s):
    prev = s.shift(1)
    return _safe_div(s - prev, prev.abs())


def _yoy_pct(s):
    prev = s.shift(4)
    return _safe_div(s - prev, prev.abs())


def _rolling_slope(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _slope(w):
        valid = ~np.isnan(w)
        if valid.sum() < min_periods:
            return np.nan
        x = np.arange(len(w), dtype=float)
        if valid.all():
            wv = w
        else:
            x = x[valid]
            wv = w[valid]
        xm = x.mean(); wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)


def _rolling_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _r(w):
        if np.isnan(w).any():
            valid = w[~np.isnan(w)]
            if len(valid) < min_periods:
                return np.nan
            last = w[-1]
            if np.isnan(last):
                return np.nan
            return float((valid <= last).sum() - 1) / max(len(valid) - 1, 1)
        last = w[-1]
        return float((w <= last).sum() - 1) / max(len(w) - 1, 1)
    return s.rolling(window, min_periods=min_periods).apply(_r, raw=True)


def _max_consec_neg_streak(diffs, window):
    def _f(w):
        if np.isnan(w).all():
            return np.nan
        best = 0
        cur = 0
        for v in w:
            if not np.isnan(v) and v < 0:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return diffs.rolling(window, min_periods=2).apply(_f, raw=True)


# ============================================================
#                    FEATURES 001-075
# ============================================================

def f20_iosp_001_inst_pct_of_float(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Institutional units divided by basic shares outstanding."""
    return _safe_div(inst_units, sharesbas)


def f20_iosp_002_inst_value_to_marketcap(inst_value: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Institutional dollar holdings divided by market cap."""
    return _safe_div(inst_value, marketcap)


def f20_iosp_003_log_inst_investors(inst_investors: pd.Series) -> pd.Series:
    """Natural log of institutional investor count."""
    return _safe_log(inst_investors)


def f20_iosp_004_avg_position_value(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Mean dollar position size per institutional holder."""
    return _safe_div(inst_value, inst_investors)


def f20_iosp_005_avg_position_units(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Mean share count per institutional holder."""
    return _safe_div(inst_units, inst_investors)


def f20_iosp_006_log_avg_position_value(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Log of mean dollar position size per holder."""
    return _safe_log(_safe_div(inst_value, inst_investors))


def f20_iosp_007_inst_units_per_million_shares_outstanding(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Institutional units per million shares outstanding."""
    return _safe_div(inst_units, sharesbas / 1.0e6)


def f20_iosp_008_holder_density_log(inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """log(investors) - log(marketcap) — holder count per dollar of market cap."""
    return _safe_log(inst_investors) - _safe_log(marketcap)


def f20_iosp_009_inverse_sqrt_investors(inst_investors: pd.Series) -> pd.Series:
    """1/sqrt(investors) — Herfindahl-style concentration proxy."""
    s = inst_investors.where(inst_investors > 0, np.nan)
    return 1.0 / np.sqrt(s)


def f20_iosp_010_inst_pct_diluted(inst_units: pd.Series, shareswadil: pd.Series) -> pd.Series:
    """Institutional units divided by diluted weighted-average shares."""
    return _safe_div(inst_units, shareswadil)


def f20_iosp_011_avg_position_value_zscore_8q(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """8q rolling z-score of average position value."""
    avg = _safe_div(inst_value, inst_investors)
    return _rolling_zscore(avg, 8)


def f20_iosp_012_log_inst_total_value(inst_value: pd.Series) -> pd.Series:
    """Log of total institutional dollar holdings."""
    return _safe_log(inst_value)


def f20_iosp_013_log_inst_total_units(inst_units: pd.Series) -> pd.Series:
    """Log of total institutional units held."""
    return _safe_log(inst_units)


def f20_iosp_014_underownership_gap_50pct(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """max(0, 0.5 - inst_pct_of_float) — distance below 50% sponsorship."""
    pct = _safe_div(inst_units, sharesbas)
    return (0.5 - pct).clip(lower=0.0)


def f20_iosp_015_inst_pct_capped_99(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Institutional pct of float capped at 0.99."""
    pct = _safe_div(inst_units, sharesbas)
    return pct.clip(upper=0.99)


def f20_iosp_016_inst_pct_of_basic_shares(inst_units: pd.Series, shareswa: pd.Series) -> pd.Series:
    """Institutional units divided by basic weighted-average shares."""
    return _safe_div(inst_units, shareswa)


def f20_iosp_017_value_units_implied_price(inst_value: pd.Series, inst_units: pd.Series) -> pd.Series:
    """Implied institutional cost basis price = value / units."""
    return _safe_div(inst_value, inst_units)


def f20_iosp_018_implied_price_to_close_ratio(inst_value: pd.Series, inst_units: pd.Series, close: pd.Series) -> pd.Series:
    """Implied institutional price divided by quarter-end close."""
    impl = _safe_div(inst_value, inst_units)
    return _safe_div(impl, close)


def f20_iosp_019_inst_value_per_share_outstanding(inst_value: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """Institutional dollar holdings per basic share outstanding."""
    return _safe_div(inst_value, sharesbas)


def f20_iosp_020_inst_pct_8q_rank(inst_units: pd.Series, sharesbas: pd.Series) -> pd.Series:
    """8q rolling rank (0..1) of institutional pct of float."""
    pct = _safe_div(inst_units, sharesbas)
    return _rolling_rank(pct, 8)


def f20_iosp_021_inst_units_qoq_pct(inst_units: pd.Series) -> pd.Series:
    """Quarter-over-quarter percent change in institutional units."""
    return _qoq_pct(inst_units)


def f20_iosp_022_inst_units_yoy_pct(inst_units: pd.Series) -> pd.Series:
    """Year-over-year (4q) percent change in institutional units."""
    return _yoy_pct(inst_units)


def f20_iosp_023_inst_units_2y_pct(inst_units: pd.Series) -> pd.Series:
    """2-year (8q) percent change in institutional units."""
    prev = inst_units.shift(8)
    return _safe_div(inst_units - prev, prev.abs())


def f20_iosp_024_inst_units_3y_pct(inst_units: pd.Series) -> pd.Series:
    """3-year (12q) percent change in institutional units."""
    prev = inst_units.shift(12)
    return _safe_div(inst_units - prev, prev.abs())


def f20_iosp_025_inst_units_qoq_signed_diff(inst_units: pd.Series) -> pd.Series:
    """Signed quarter-over-quarter change in institutional units."""
    return inst_units.diff()


def f20_iosp_026_inst_units_yoy_signed_diff(inst_units: pd.Series) -> pd.Series:
    """Signed year-over-year change in institutional units."""
    return inst_units.diff(4)


def f20_iosp_027_inst_investors_qoq_pct(inst_investors: pd.Series) -> pd.Series:
    """QoQ percent change in institutional investor count."""
    return _qoq_pct(inst_investors)


def f20_iosp_028_inst_investors_yoy_pct(inst_investors: pd.Series) -> pd.Series:
    """YoY percent change in institutional investor count."""
    return _yoy_pct(inst_investors)


def f20_iosp_029_inst_investors_qoq_signed_diff(inst_investors: pd.Series) -> pd.Series:
    """Signed QoQ change in institutional investor count."""
    return inst_investors.diff()


def f20_iosp_030_inst_investors_yoy_signed_diff(inst_investors: pd.Series) -> pd.Series:
    """Signed YoY change in institutional investor count."""
    return inst_investors.diff(4)


def f20_iosp_031_inst_investors_2y_signed_diff(inst_investors: pd.Series) -> pd.Series:
    """Signed 2-year change in institutional investor count."""
    return inst_investors.diff(8)


def f20_iosp_032_inst_value_qoq_pct(inst_value: pd.Series) -> pd.Series:
    """QoQ percent change in institutional dollar holdings."""
    return _qoq_pct(inst_value)


def f20_iosp_033_inst_value_yoy_pct(inst_value: pd.Series) -> pd.Series:
    """YoY percent change in institutional dollar holdings."""
    return _yoy_pct(inst_value)


def f20_iosp_034_inst_value_qoq_signed_diff(inst_value: pd.Series) -> pd.Series:
    """Signed QoQ change in institutional dollar holdings."""
    return inst_value.diff()


def f20_iosp_035_inst_value_yoy_signed_diff(inst_value: pd.Series) -> pd.Series:
    """Signed YoY change in institutional dollar holdings."""
    return inst_value.diff(4)


def f20_iosp_036_avg_position_value_qoq_pct(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """QoQ percent change in average position value."""
    avg = _safe_div(inst_value, inst_investors)
    return _qoq_pct(avg)


def f20_iosp_037_avg_position_value_yoy_pct(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """YoY percent change in average position value."""
    avg = _safe_div(inst_value, inst_investors)
    return _yoy_pct(avg)


def f20_iosp_038_avg_position_units_qoq_pct(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """QoQ percent change in average position units."""
    avg = _safe_div(inst_units, inst_investors)
    return _qoq_pct(avg)


def f20_iosp_039_avg_position_units_yoy_pct(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """YoY percent change in average position units."""
    avg = _safe_div(inst_units, inst_investors)
    return _yoy_pct(avg)


def f20_iosp_040_cumulative_4q_inst_units_change_pct(inst_units: pd.Series) -> pd.Series:
    """Cumulative 4q (1 year) percent change in inst units vs 4q ago."""
    prev = inst_units.shift(4)
    return _safe_div(inst_units - prev, prev.abs())


def f20_iosp_041_cumulative_4q_inst_investors_change_pct(inst_investors: pd.Series) -> pd.Series:
    """Cumulative 4q percent change in inst investors vs 4q ago."""
    prev = inst_investors.shift(4)
    return _safe_div(inst_investors - prev, prev.abs())


def f20_iosp_042_inst_units_8q_slope_zscored(inst_units: pd.Series) -> pd.Series:
    """8q linear-regression slope divided by 8q rolling std of units."""
    slope = _rolling_slope(inst_units, 8)
    sd = inst_units.rolling(8, min_periods=3).std()
    return slope / sd.replace(0, np.nan)


def f20_iosp_043_inst_investors_8q_slope_zscored(inst_investors: pd.Series) -> pd.Series:
    """8q linear-regression slope of investors divided by 8q rolling std."""
    slope = _rolling_slope(inst_investors, 8)
    sd = inst_investors.rolling(8, min_periods=3).std()
    return slope / sd.replace(0, np.nan)


def f20_iosp_044_inst_units_flow_acceleration(inst_units: pd.Series) -> pd.Series:
    """Second difference of inst units — flow acceleration."""
    return inst_units.diff().diff()


def f20_iosp_045_inst_investors_flow_acceleration(inst_investors: pd.Series) -> pd.Series:
    """Second difference of inst investors — flow acceleration."""
    return inst_investors.diff().diff()


def f20_iosp_046_avg_position_value_qoq_change(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Signed QoQ change in average position value."""
    avg = _safe_div(inst_value, inst_investors)
    return avg.diff()


def f20_iosp_047_avg_position_value_yoy_change(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """Signed YoY change in average position value."""
    avg = _safe_div(inst_value, inst_investors)
    return avg.diff(4)


def f20_iosp_048_position_size_intensity(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Average position value divided by market cap — per-holder ownership intensity."""
    avg = _safe_div(inst_value, inst_investors)
    return _safe_div(avg, marketcap)


def f20_iosp_049_position_size_intensity_qoq_pct(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """QoQ percent change in position size intensity."""
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return _qoq_pct(ints)


def f20_iosp_050_position_size_intensity_yoy_pct(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """YoY percent change in position size intensity."""
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return _yoy_pct(ints)


def f20_iosp_051_herfindahl_concentration_proxy_4q_mean(inst_investors: pd.Series) -> pd.Series:
    """Rolling 4q mean of (1/investors) — Herfindahl concentration proxy."""
    inv = 1.0 / inst_investors.where(inst_investors > 0, np.nan)
    return inv.rolling(4, min_periods=2).mean()


def f20_iosp_052_log_position_size_zscore_8q(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """8q z-score of log average position value."""
    lp = _safe_log(_safe_div(inst_value, inst_investors))
    return _rolling_zscore(lp, 8)


def f20_iosp_053_position_size_intensity_4q_mean(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """4q rolling mean of position size intensity."""
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return ints.rolling(4, min_periods=2).mean()


def f20_iosp_054_avg_position_value_zscore_12q(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """12q rolling z-score of average position value."""
    avg = _safe_div(inst_value, inst_investors)
    return _rolling_zscore(avg, 12)


def f20_iosp_055_avg_position_units_zscore_8q(inst_units: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """8q rolling z-score of average position units."""
    avg = _safe_div(inst_units, inst_investors)
    return _rolling_zscore(avg, 8)


def f20_iosp_056_position_value_volatility_8q(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """8q std of QoQ percent change in average position value."""
    avg = _safe_div(inst_value, inst_investors)
    q = _qoq_pct(avg)
    return q.rolling(8, min_periods=3).std()


def f20_iosp_057_position_count_volatility_8q(inst_investors: pd.Series) -> pd.Series:
    """8q std of QoQ percent change in investor count."""
    q = _qoq_pct(inst_investors)
    return q.rolling(8, min_periods=3).std()


def f20_iosp_058_concentration_acceleration(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """Second difference of position size intensity — concentration acceleration."""
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return ints.diff().diff()


def f20_iosp_059_concentration_4q_slope(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """4q linear-regression slope of position size intensity."""
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return _rolling_slope(ints, 4)


def f20_iosp_060_dispersion_divergence_sign(inst_value: pd.Series, inst_investors: pd.Series) -> pd.Series:
    """sign(avg position value qoq) - sign(investor count qoq) — dispersion divergence."""
    avg = _safe_div(inst_value, inst_investors)
    return np.sign(avg.diff()) - np.sign(inst_investors.diff())


def f20_iosp_061_positioncount_to_marketcap_log(inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """log(investors) - log(marketcap) — investor count per unit log-marketcap."""
    return _safe_log(inst_investors) - _safe_log(marketcap)


def f20_iosp_062_units_to_value_ratio_zscore_8q(inst_units: pd.Series, inst_value: pd.Series) -> pd.Series:
    """8q z-score of units-per-dollar (inverse of implied price)."""
    ratio = _safe_div(inst_units, inst_value)
    return _rolling_zscore(ratio, 8)


def f20_iosp_063_liquidity_burden_per_holder(inst_units: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """(units/investors) / log(marketcap) — burden of shares each holder must move."""
    per_holder = _safe_div(inst_units, inst_investors)
    return _safe_div(per_holder, _safe_log(marketcap))


def f20_iosp_064_ownership_concentration_index(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """inst_value / (investors * marketcap) — overall concentration index."""
    return _safe_div(inst_value, inst_investors * marketcap)


def f20_iosp_065_concentration_8q_trend_slope(inst_value: pd.Series, inst_investors: pd.Series, marketcap: pd.Series) -> pd.Series:
    """8q linear-regression slope of position size intensity."""
    avg = _safe_div(inst_value, inst_investors)
    ints = _safe_div(avg, marketcap)
    return _rolling_slope(ints, 8)


def f20_iosp_066_inst_call_to_units_ratio(inst_calls: pd.Series, inst_units: pd.Series) -> pd.Series:
    """Institutional calls held divided by institutional units."""
    return _safe_div(inst_calls, inst_units)


def f20_iosp_067_inst_put_to_units_ratio(inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    """Institutional puts held divided by institutional units."""
    return _safe_div(inst_puts, inst_units)


def f20_iosp_068_inst_put_call_skew(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """(puts - calls) / (puts + calls) — institutional options skew."""
    return _safe_div(inst_puts - inst_calls, inst_puts + inst_calls)


def f20_iosp_069_inst_put_call_skew_qoq_change(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """QoQ signed change in institutional put-call skew."""
    skew = _safe_div(inst_puts - inst_calls, inst_puts + inst_calls)
    return skew.diff()


def f20_iosp_070_inst_put_call_skew_yoy_change(inst_puts: pd.Series, inst_calls: pd.Series) -> pd.Series:
    """YoY signed change in institutional put-call skew."""
    skew = _safe_div(inst_puts - inst_calls, inst_puts + inst_calls)
    return skew.diff(4)


def f20_iosp_071_total_options_intensity(inst_calls: pd.Series, inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    """(calls + puts) / units — total options leverage per share."""
    return _safe_div(inst_calls + inst_puts, inst_units)


def f20_iosp_072_total_options_intensity_qoq_pct(inst_calls: pd.Series, inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    """QoQ percent change in total options intensity."""
    ints = _safe_div(inst_calls + inst_puts, inst_units)
    return _qoq_pct(ints)


def f20_iosp_073_total_options_intensity_yoy_pct(inst_calls: pd.Series, inst_puts: pd.Series, inst_units: pd.Series) -> pd.Series:
    """YoY percent change in total options intensity."""
    ints = _safe_div(inst_calls + inst_puts, inst_units)
    return _yoy_pct(ints)


def f20_iosp_074_options_to_value_ratio(inst_calls: pd.Series, inst_puts: pd.Series, inst_value: pd.Series) -> pd.Series:
    """(calls + puts) / inst_value — options exposure relative to dollar holdings."""
    return _safe_div(inst_calls + inst_puts, inst_value)


def f20_iosp_075_inst_calls_qoq_pct(inst_calls: pd.Series) -> pd.Series:
    """QoQ percent change in institutional calls held."""
    return _qoq_pct(inst_calls)


# ============================================================
#                        REGISTRY
# ============================================================

INSTITUTIONAL_OWNERSHIP_SNAPSHOT_BASE_REGISTRY_001_075 = {
    "f20_iosp_001_inst_pct_of_float": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_001_inst_pct_of_float},
    "f20_iosp_002_inst_value_to_marketcap": {"inputs": ["inst_value", "marketcap"], "func": f20_iosp_002_inst_value_to_marketcap},
    "f20_iosp_003_log_inst_investors": {"inputs": ["inst_investors"], "func": f20_iosp_003_log_inst_investors},
    "f20_iosp_004_avg_position_value": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_004_avg_position_value},
    "f20_iosp_005_avg_position_units": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_005_avg_position_units},
    "f20_iosp_006_log_avg_position_value": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_006_log_avg_position_value},
    "f20_iosp_007_inst_units_per_million_shares_outstanding": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_007_inst_units_per_million_shares_outstanding},
    "f20_iosp_008_holder_density_log": {"inputs": ["inst_investors", "marketcap"], "func": f20_iosp_008_holder_density_log},
    "f20_iosp_009_inverse_sqrt_investors": {"inputs": ["inst_investors"], "func": f20_iosp_009_inverse_sqrt_investors},
    "f20_iosp_010_inst_pct_diluted": {"inputs": ["inst_units", "shareswadil"], "func": f20_iosp_010_inst_pct_diluted},
    "f20_iosp_011_avg_position_value_zscore_8q": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_011_avg_position_value_zscore_8q},
    "f20_iosp_012_log_inst_total_value": {"inputs": ["inst_value"], "func": f20_iosp_012_log_inst_total_value},
    "f20_iosp_013_log_inst_total_units": {"inputs": ["inst_units"], "func": f20_iosp_013_log_inst_total_units},
    "f20_iosp_014_underownership_gap_50pct": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_014_underownership_gap_50pct},
    "f20_iosp_015_inst_pct_capped_99": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_015_inst_pct_capped_99},
    "f20_iosp_016_inst_pct_of_basic_shares": {"inputs": ["inst_units", "shareswa"], "func": f20_iosp_016_inst_pct_of_basic_shares},
    "f20_iosp_017_value_units_implied_price": {"inputs": ["inst_value", "inst_units"], "func": f20_iosp_017_value_units_implied_price},
    "f20_iosp_018_implied_price_to_close_ratio": {"inputs": ["inst_value", "inst_units", "close"], "func": f20_iosp_018_implied_price_to_close_ratio},
    "f20_iosp_019_inst_value_per_share_outstanding": {"inputs": ["inst_value", "sharesbas"], "func": f20_iosp_019_inst_value_per_share_outstanding},
    "f20_iosp_020_inst_pct_8q_rank": {"inputs": ["inst_units", "sharesbas"], "func": f20_iosp_020_inst_pct_8q_rank},
    "f20_iosp_021_inst_units_qoq_pct": {"inputs": ["inst_units"], "func": f20_iosp_021_inst_units_qoq_pct},
    "f20_iosp_022_inst_units_yoy_pct": {"inputs": ["inst_units"], "func": f20_iosp_022_inst_units_yoy_pct},
    "f20_iosp_023_inst_units_2y_pct": {"inputs": ["inst_units"], "func": f20_iosp_023_inst_units_2y_pct},
    "f20_iosp_024_inst_units_3y_pct": {"inputs": ["inst_units"], "func": f20_iosp_024_inst_units_3y_pct},
    "f20_iosp_025_inst_units_qoq_signed_diff": {"inputs": ["inst_units"], "func": f20_iosp_025_inst_units_qoq_signed_diff},
    "f20_iosp_026_inst_units_yoy_signed_diff": {"inputs": ["inst_units"], "func": f20_iosp_026_inst_units_yoy_signed_diff},
    "f20_iosp_027_inst_investors_qoq_pct": {"inputs": ["inst_investors"], "func": f20_iosp_027_inst_investors_qoq_pct},
    "f20_iosp_028_inst_investors_yoy_pct": {"inputs": ["inst_investors"], "func": f20_iosp_028_inst_investors_yoy_pct},
    "f20_iosp_029_inst_investors_qoq_signed_diff": {"inputs": ["inst_investors"], "func": f20_iosp_029_inst_investors_qoq_signed_diff},
    "f20_iosp_030_inst_investors_yoy_signed_diff": {"inputs": ["inst_investors"], "func": f20_iosp_030_inst_investors_yoy_signed_diff},
    "f20_iosp_031_inst_investors_2y_signed_diff": {"inputs": ["inst_investors"], "func": f20_iosp_031_inst_investors_2y_signed_diff},
    "f20_iosp_032_inst_value_qoq_pct": {"inputs": ["inst_value"], "func": f20_iosp_032_inst_value_qoq_pct},
    "f20_iosp_033_inst_value_yoy_pct": {"inputs": ["inst_value"], "func": f20_iosp_033_inst_value_yoy_pct},
    "f20_iosp_034_inst_value_qoq_signed_diff": {"inputs": ["inst_value"], "func": f20_iosp_034_inst_value_qoq_signed_diff},
    "f20_iosp_035_inst_value_yoy_signed_diff": {"inputs": ["inst_value"], "func": f20_iosp_035_inst_value_yoy_signed_diff},
    "f20_iosp_036_avg_position_value_qoq_pct": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_036_avg_position_value_qoq_pct},
    "f20_iosp_037_avg_position_value_yoy_pct": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_037_avg_position_value_yoy_pct},
    "f20_iosp_038_avg_position_units_qoq_pct": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_038_avg_position_units_qoq_pct},
    "f20_iosp_039_avg_position_units_yoy_pct": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_039_avg_position_units_yoy_pct},
    "f20_iosp_040_cumulative_4q_inst_units_change_pct": {"inputs": ["inst_units"], "func": f20_iosp_040_cumulative_4q_inst_units_change_pct},
    "f20_iosp_041_cumulative_4q_inst_investors_change_pct": {"inputs": ["inst_investors"], "func": f20_iosp_041_cumulative_4q_inst_investors_change_pct},
    "f20_iosp_042_inst_units_8q_slope_zscored": {"inputs": ["inst_units"], "func": f20_iosp_042_inst_units_8q_slope_zscored},
    "f20_iosp_043_inst_investors_8q_slope_zscored": {"inputs": ["inst_investors"], "func": f20_iosp_043_inst_investors_8q_slope_zscored},
    "f20_iosp_044_inst_units_flow_acceleration": {"inputs": ["inst_units"], "func": f20_iosp_044_inst_units_flow_acceleration},
    "f20_iosp_045_inst_investors_flow_acceleration": {"inputs": ["inst_investors"], "func": f20_iosp_045_inst_investors_flow_acceleration},
    "f20_iosp_046_avg_position_value_qoq_change": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_046_avg_position_value_qoq_change},
    "f20_iosp_047_avg_position_value_yoy_change": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_047_avg_position_value_yoy_change},
    "f20_iosp_048_position_size_intensity": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_048_position_size_intensity},
    "f20_iosp_049_position_size_intensity_qoq_pct": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_049_position_size_intensity_qoq_pct},
    "f20_iosp_050_position_size_intensity_yoy_pct": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_050_position_size_intensity_yoy_pct},
    "f20_iosp_051_herfindahl_concentration_proxy_4q_mean": {"inputs": ["inst_investors"], "func": f20_iosp_051_herfindahl_concentration_proxy_4q_mean},
    "f20_iosp_052_log_position_size_zscore_8q": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_052_log_position_size_zscore_8q},
    "f20_iosp_053_position_size_intensity_4q_mean": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_053_position_size_intensity_4q_mean},
    "f20_iosp_054_avg_position_value_zscore_12q": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_054_avg_position_value_zscore_12q},
    "f20_iosp_055_avg_position_units_zscore_8q": {"inputs": ["inst_units", "inst_investors"], "func": f20_iosp_055_avg_position_units_zscore_8q},
    "f20_iosp_056_position_value_volatility_8q": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_056_position_value_volatility_8q},
    "f20_iosp_057_position_count_volatility_8q": {"inputs": ["inst_investors"], "func": f20_iosp_057_position_count_volatility_8q},
    "f20_iosp_058_concentration_acceleration": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_058_concentration_acceleration},
    "f20_iosp_059_concentration_4q_slope": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_059_concentration_4q_slope},
    "f20_iosp_060_dispersion_divergence_sign": {"inputs": ["inst_value", "inst_investors"], "func": f20_iosp_060_dispersion_divergence_sign},
    "f20_iosp_061_positioncount_to_marketcap_log": {"inputs": ["inst_investors", "marketcap"], "func": f20_iosp_061_positioncount_to_marketcap_log},
    "f20_iosp_062_units_to_value_ratio_zscore_8q": {"inputs": ["inst_units", "inst_value"], "func": f20_iosp_062_units_to_value_ratio_zscore_8q},
    "f20_iosp_063_liquidity_burden_per_holder": {"inputs": ["inst_units", "inst_investors", "marketcap"], "func": f20_iosp_063_liquidity_burden_per_holder},
    "f20_iosp_064_ownership_concentration_index": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_064_ownership_concentration_index},
    "f20_iosp_065_concentration_8q_trend_slope": {"inputs": ["inst_value", "inst_investors", "marketcap"], "func": f20_iosp_065_concentration_8q_trend_slope},
    "f20_iosp_066_inst_call_to_units_ratio": {"inputs": ["inst_calls", "inst_units"], "func": f20_iosp_066_inst_call_to_units_ratio},
    "f20_iosp_067_inst_put_to_units_ratio": {"inputs": ["inst_puts", "inst_units"], "func": f20_iosp_067_inst_put_to_units_ratio},
    "f20_iosp_068_inst_put_call_skew": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_068_inst_put_call_skew},
    "f20_iosp_069_inst_put_call_skew_qoq_change": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_069_inst_put_call_skew_qoq_change},
    "f20_iosp_070_inst_put_call_skew_yoy_change": {"inputs": ["inst_puts", "inst_calls"], "func": f20_iosp_070_inst_put_call_skew_yoy_change},
    "f20_iosp_071_total_options_intensity": {"inputs": ["inst_calls", "inst_puts", "inst_units"], "func": f20_iosp_071_total_options_intensity},
    "f20_iosp_072_total_options_intensity_qoq_pct": {"inputs": ["inst_calls", "inst_puts", "inst_units"], "func": f20_iosp_072_total_options_intensity_qoq_pct},
    "f20_iosp_073_total_options_intensity_yoy_pct": {"inputs": ["inst_calls", "inst_puts", "inst_units"], "func": f20_iosp_073_total_options_intensity_yoy_pct},
    "f20_iosp_074_options_to_value_ratio": {"inputs": ["inst_calls", "inst_puts", "inst_value"], "func": f20_iosp_074_options_to_value_ratio},
    "f20_iosp_075_inst_calls_qoq_pct": {"inputs": ["inst_calls"], "func": f20_iosp_075_inst_calls_qoq_pct},
}
