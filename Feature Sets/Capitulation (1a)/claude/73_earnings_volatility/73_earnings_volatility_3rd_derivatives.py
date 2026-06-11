"""
73_earnings_volatility — 3rd-Derivative Features 001-025
Domain: rate of change of 2nd-derivative earnings-volatility features — QoQ diff /
        slope / pct-change of the already-differentiated volatility concepts, as
        well as higher-order acceleration of rolling-std, CV, swing and residual
        measures.
Asset class: US equities | Sharadar SF1 fundamentals (quarterly -> daily)
Target context: capitulation — absolute multi-year low / maximum distress
All features are backward-looking only; no forward information.

Quarterly -> Daily alignment contract
--------------------------------------
All inputs to feature functions in this file are daily-frequency pandas
Series, forward-filled from the most recent quarterly Sharadar SF1 report
known as of each date.  A forward-filled quarterly series steps at most
4 times per year; flat stretches between report dates are correct and expected.
The 3rd-derivative series are sparse/stepwise on a daily index because the
underlying data is quarterly — this is correct and expected.
Functions look strictly backward using .shift(positive), .rolling(), or
.expanding().  Quarterly cadence on the daily index: 1 quarter = 63 trading
days, 1 year = 252 trading days.  All feature functions in this file look
strictly backward.
"""
import numpy as np
import pandas as pd

# ── Constants ─────────────────────────────────────────────────────────────────
_TD_YEAR  = 252
_TD_2Y    = 504
_TD_3Y    = 756
_TD_QTR   = 63
_EPS      = 1e-9

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
    """Element-wise division; replaces zero (and NaN-producing) denominators with NaN."""
    return num / den.replace(0, np.nan)


def _safe_div_abs(num: pd.Series, den: pd.Series) -> pd.Series:
    """Divide by absolute value of den."""
    return num / den.abs().replace(0, np.nan)


def _rolling_mean(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).mean()


def _rolling_std(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(2, w // 4)).std()


def _rolling_max(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).max()


def _rolling_min(s: pd.Series, w: int) -> pd.Series:
    return s.rolling(w, min_periods=max(1, w // 4)).min()


def _ewm_std(s: pd.Series, span: int) -> pd.Series:
    return s.ewm(span=span, min_periods=max(2, span // 4)).std()


def _qoq_diff(s: pd.Series) -> pd.Series:
    return s - s.shift(_TD_QTR)


def _cv(s: pd.Series, w: int) -> pd.Series:
    return _safe_div_abs(_rolling_std(s, w), _rolling_mean(s, w))


def _ols_slope(arr: np.ndarray) -> float:
    """Scalar OLS slope for rolling.apply(raw=True)."""
    n = len(arr)
    if n < 2:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = float(((x - xm) ** 2).sum())
    if denom == 0.0:
        return np.nan
    return float(((x - xm) * (arr - ym)).sum() / denom)


def _residual_std(arr: np.ndarray) -> float:
    """Scalar residual std of linear trend; for rolling.apply(raw=True)."""
    n = len(arr)
    if n < 3:
        return np.nan
    x = np.arange(n, dtype=float)
    xm = x.mean()
    ym = arr.mean()
    denom = float(((x - xm) ** 2).sum())
    if denom == 0.0:
        s = float(arr.std())
        return s if s > 0 else np.nan
    slope = float(((x - xm) * (arr - ym)).sum() / denom)
    intercept = ym - slope * xm
    resid = arr - (slope * x + intercept)
    return float(resid.std())


# ── Base and 2nd-derivative concept re-computations ──────────────────────────
# Self-contained; no cross-file imports required.

def _b_netinc_std_4q(netinc):
    return _rolling_std(netinc, _TD_YEAR)

def _b_eps_std_4q(eps):
    return _rolling_std(eps, _TD_YEAR)

def _b_ebit_std_4q(ebit):
    return _rolling_std(ebit, _TD_YEAR)

def _b_netinc_cv_4q(netinc):
    return _cv(netinc, _TD_YEAR)

def _b_eps_cv_4q(eps):
    return _cv(eps, _TD_YEAR)

def _b_netinc_range_4q(netinc):
    return _rolling_max(netinc, _TD_YEAR) - _rolling_min(netinc, _TD_YEAR)

def _b_netinc_swing_abs_4q(netinc):
    return _rolling_mean(_qoq_diff(netinc).abs(), _TD_YEAR)

def _b_netinc_downside_dev_4q(netinc):
    below = netinc.clip(upper=0)
    return _rolling_mean(below ** 2, _TD_YEAR).apply(np.sqrt)

def _b_netinc_resid_std_4q(netinc):
    return netinc.rolling(_TD_YEAR, min_periods=max(3, _TD_YEAR // 4)).apply(
        _residual_std, raw=True
    )

def _b_net_margin_std_4q(netinc, revenue):
    m = _safe_div(netinc, revenue.abs().replace(0, np.nan))
    return _rolling_std(m, _TD_YEAR)

def _b_ncfo_std_4q(ncfo):
    return _rolling_std(ncfo, _TD_YEAR)

def _b_vol_of_vol(netinc):
    return _rolling_std(_rolling_std(netinc, _TD_YEAR), _TD_2Y)

# ── 2nd-derivative re-computations (for 3rd-derivative differencing) ─────────

def _d2_netinc_std_qoq(netinc):
    base = _b_netinc_std_4q(netinc)
    return base - base.shift(_TD_QTR)

def _d2_netinc_cv_qoq(netinc):
    base = _b_netinc_cv_4q(netinc)
    return base - base.shift(_TD_QTR)

def _d2_eps_std_qoq(eps):
    base = _b_eps_std_4q(eps)
    return base - base.shift(_TD_QTR)

def _d2_ebit_std_qoq(ebit):
    base = _b_ebit_std_4q(ebit)
    return base - base.shift(_TD_QTR)

def _d2_netinc_range_qoq(netinc):
    base = _b_netinc_range_4q(netinc)
    return base - base.shift(_TD_QTR)

def _d2_netinc_swing_qoq(netinc):
    base = _b_netinc_swing_abs_4q(netinc)
    return base - base.shift(_TD_QTR)

def _d2_netinc_downside_dev_qoq(netinc):
    base = _b_netinc_downside_dev_4q(netinc)
    return base - base.shift(_TD_QTR)

def _d2_netinc_resid_std_qoq(netinc):
    base = _b_netinc_resid_std_4q(netinc)
    return base - base.shift(_TD_QTR)


# ── 3rd-derivative feature functions ─────────────────────────────────────────

def evl_drv3_001_netinc_std_4q_qoq_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q-std of net income (3rd-order acceleration)."""
    d2 = _d2_netinc_std_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_002_netinc_std_4q_qoq_diff_yoy(netinc: pd.Series) -> pd.Series:
    """YoY change in the QoQ-change of 4q-std of net income."""
    d2 = _d2_netinc_std_qoq(netinc)
    return d2 - d2.shift(_TD_YEAR)


def evl_drv3_003_netinc_cv_4q_qoq_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q CV of net income."""
    d2 = _d2_netinc_cv_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_004_eps_std_4q_qoq_diff_qoq(eps: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q-std of EPS."""
    d2 = _d2_eps_std_qoq(eps)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_005_ebit_std_4q_qoq_diff_qoq(ebit: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q-std of EBIT."""
    d2 = _d2_ebit_std_qoq(ebit)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_006_netinc_range_4q_qoq_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q earnings range of net income."""
    d2 = _d2_netinc_range_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_007_netinc_swing_abs_qoq_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of mean-absolute QoQ-swing of net income."""
    d2 = _d2_netinc_swing_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_008_netinc_downside_dev_qoq_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q downside semi-deviation of net income."""
    d2 = _d2_netinc_downside_dev_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_009_netinc_resid_std_qoq_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of trend-residual std of net income (4q)."""
    d2 = _d2_netinc_resid_std_qoq(netinc)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_010_netinc_std_4q_slope_qoq_diff(netinc: pd.Series) -> pd.Series:
    """
    QoQ change in the OLS slope of the 4q-std series (slope-of-slope).
    Positive = the slope of the volatility trend is itself increasing.
    """
    vol = _b_netinc_std_4q(netinc)
    slope = vol.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True
    )
    return slope - slope.shift(_TD_QTR)


def evl_drv3_011_netinc_cv_4q_slope_qoq_diff(netinc: pd.Series) -> pd.Series:
    """QoQ change in the OLS slope of the 4q CV series of net income."""
    cv_series = _b_netinc_cv_4q(netinc)
    slope = cv_series.rolling(_TD_YEAR, min_periods=max(2, _TD_YEAR // 4)).apply(
        _ols_slope, raw=True
    )
    return slope - slope.shift(_TD_QTR)


def evl_drv3_012_netinc_vol_of_vol_qoq_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of volatility-of-volatility of net income."""
    vov = _b_vol_of_vol(netinc)
    d2  = vov - vov.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_013_eps_cv_4q_qoq_diff_qoq(eps: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q CV of EPS."""
    base = _b_eps_cv_4q(eps)
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_014_ncfo_std_4q_qoq_diff_qoq(ncfo: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q rolling std of operating cash flow."""
    d2 = _b_ncfo_std_4q(ncfo)
    d2c = d2 - d2.shift(_TD_QTR)
    return d2c - d2c.shift(_TD_QTR)


def evl_drv3_015_netinc_std_pct_chg_qoq_diff(netinc: pd.Series) -> pd.Series:
    """
    QoQ change in the QoQ percent-change of the 4q-std of net income.
    3rd-order relative acceleration of earnings volatility.
    """
    vol   = _b_netinc_std_4q(netinc)
    prior = vol.shift(_TD_QTR)
    pct_chg = _safe_div_abs(vol - prior, prior)
    return pct_chg - pct_chg.shift(_TD_QTR)


def evl_drv3_016_netinc_std_4q_yoy_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of the 4q-std of net income."""
    vol    = _b_netinc_std_4q(netinc)
    d2_yoy = vol - vol.shift(_TD_YEAR)
    return d2_yoy - d2_yoy.shift(_TD_QTR)


def evl_drv3_017_netinc_cv_4q_yoy_diff_qoq(netinc: pd.Series) -> pd.Series:
    """QoQ change in the YoY-diff of the 4q CV of net income."""
    cv     = _b_netinc_cv_4q(netinc)
    d2_yoy = cv - cv.shift(_TD_YEAR)
    return d2_yoy - d2_yoy.shift(_TD_QTR)


def evl_drv3_018_net_margin_std_qoq_diff_qoq(netinc: pd.Series, revenue: pd.Series) -> pd.Series:
    """QoQ change in the QoQ-change of 4q net-margin std."""
    base = _b_net_margin_std_4q(netinc, revenue)
    d2   = base - base.shift(_TD_QTR)
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_019_netinc_std_ewm_diff_qoq_diff(netinc: pd.Series) -> pd.Series:
    """
    QoQ change in (4q-std minus its own EWM) — how the departure of current
    volatility from its rolling average is itself evolving quarter over quarter.
    """
    vol = _b_netinc_std_4q(netinc)
    ewm = vol.ewm(span=_TD_YEAR, min_periods=max(1, _TD_YEAR // 4)).mean()
    d2  = vol - ewm
    return d2 - d2.shift(_TD_QTR)


def evl_drv3_020_netinc_range_qoq_diff_yoy(netinc: pd.Series) -> pd.Series:
    """YoY change in the QoQ-change of 4q earnings range of net income."""
    d2 = _d2_netinc_range_qoq(netinc)
    return d2 - d2.shift(_TD_YEAR)


def evl_drv3_021_netinc_downside_dev_qoq_yoy(netinc: pd.Series) -> pd.Series:
    """YoY change in the QoQ-change of 4q downside semi-deviation of net income."""
    d2 = _d2_netinc_downside_dev_qoq(netinc)
    return d2 - d2.shift(_TD_YEAR)


def evl_drv3_022_eps_std_4q_qoq_diff_yoy(eps: pd.Series) -> pd.Series:
    """YoY change in the QoQ-change of 4q EPS std."""
    d2 = _d2_eps_std_qoq(eps)
    return d2 - d2.shift(_TD_YEAR)


def evl_drv3_023_netinc_resid_std_qoq_diff_yoy(netinc: pd.Series) -> pd.Series:
    """YoY change in the QoQ-change of trend-residual std of net income."""
    d2 = _d2_netinc_resid_std_qoq(netinc)
    return d2 - d2.shift(_TD_YEAR)


def evl_drv3_024_netinc_vol_z_score_qoq_diff(netinc: pd.Series) -> pd.Series:
    """
    QoQ change in the expanding z-score of the 4q-std of net income.
    Measures whether the current volatility is becoming MORE extreme vs history.
    """
    vol = _b_netinc_std_4q(netinc)
    mu  = vol.expanding(min_periods=2).mean()
    sd  = vol.expanding(min_periods=2).std()
    z   = _safe_div(vol - mu, sd)
    return z - z.shift(_TD_QTR)


def evl_drv3_025_earnings_instability_3rd_composite(
    netinc: pd.Series,
    eps: pd.Series,
    ebit: pd.Series,
) -> pd.Series:
    """
    Composite 3rd-derivative instability: average of QoQ-changes of the
    2nd-derivative (QoQ-of-QoQ) std for netinc, eps, and ebit.
    Three-field 3rd-order volatility acceleration signal.
    """
    d3_ni   = _d2_netinc_std_qoq(netinc) - _d2_netinc_std_qoq(netinc).shift(_TD_QTR)
    d3_eps  = _d2_eps_std_qoq(eps)       - _d2_eps_std_qoq(eps).shift(_TD_QTR)
    d3_ebit = _d2_ebit_std_qoq(ebit)     - _d2_ebit_std_qoq(ebit).shift(_TD_QTR)
    return (d3_ni + d3_eps + d3_ebit) / 3.0


# ── Registry 3rd Derivatives ──────────────────────────────────────────────────

EARNINGS_VOLATILITY_REGISTRY_3RD_DERIVATIVES = {
    "evl_drv3_001_netinc_std_4q_qoq_diff_qoq":       {"inputs": ["netinc"],              "func": evl_drv3_001_netinc_std_4q_qoq_diff_qoq},
    "evl_drv3_002_netinc_std_4q_qoq_diff_yoy":       {"inputs": ["netinc"],              "func": evl_drv3_002_netinc_std_4q_qoq_diff_yoy},
    "evl_drv3_003_netinc_cv_4q_qoq_diff_qoq":        {"inputs": ["netinc"],              "func": evl_drv3_003_netinc_cv_4q_qoq_diff_qoq},
    "evl_drv3_004_eps_std_4q_qoq_diff_qoq":          {"inputs": ["eps"],                 "func": evl_drv3_004_eps_std_4q_qoq_diff_qoq},
    "evl_drv3_005_ebit_std_4q_qoq_diff_qoq":         {"inputs": ["ebit"],                "func": evl_drv3_005_ebit_std_4q_qoq_diff_qoq},
    "evl_drv3_006_netinc_range_4q_qoq_diff_qoq":     {"inputs": ["netinc"],              "func": evl_drv3_006_netinc_range_4q_qoq_diff_qoq},
    "evl_drv3_007_netinc_swing_abs_qoq_diff_qoq":    {"inputs": ["netinc"],              "func": evl_drv3_007_netinc_swing_abs_qoq_diff_qoq},
    "evl_drv3_008_netinc_downside_dev_qoq_diff_qoq": {"inputs": ["netinc"],              "func": evl_drv3_008_netinc_downside_dev_qoq_diff_qoq},
    "evl_drv3_009_netinc_resid_std_qoq_diff_qoq":    {"inputs": ["netinc"],              "func": evl_drv3_009_netinc_resid_std_qoq_diff_qoq},
    "evl_drv3_010_netinc_std_4q_slope_qoq_diff":     {"inputs": ["netinc"],              "func": evl_drv3_010_netinc_std_4q_slope_qoq_diff},
    "evl_drv3_011_netinc_cv_4q_slope_qoq_diff":      {"inputs": ["netinc"],              "func": evl_drv3_011_netinc_cv_4q_slope_qoq_diff},
    "evl_drv3_012_netinc_vol_of_vol_qoq_diff_qoq":   {"inputs": ["netinc"],              "func": evl_drv3_012_netinc_vol_of_vol_qoq_diff_qoq},
    "evl_drv3_013_eps_cv_4q_qoq_diff_qoq":           {"inputs": ["eps"],                 "func": evl_drv3_013_eps_cv_4q_qoq_diff_qoq},
    "evl_drv3_014_ncfo_std_4q_qoq_diff_qoq":         {"inputs": ["ncfo"],                "func": evl_drv3_014_ncfo_std_4q_qoq_diff_qoq},
    "evl_drv3_015_netinc_std_pct_chg_qoq_diff":      {"inputs": ["netinc"],              "func": evl_drv3_015_netinc_std_pct_chg_qoq_diff},
    "evl_drv3_016_netinc_std_4q_yoy_diff_qoq":       {"inputs": ["netinc"],              "func": evl_drv3_016_netinc_std_4q_yoy_diff_qoq},
    "evl_drv3_017_netinc_cv_4q_yoy_diff_qoq":        {"inputs": ["netinc"],              "func": evl_drv3_017_netinc_cv_4q_yoy_diff_qoq},
    "evl_drv3_018_net_margin_std_qoq_diff_qoq":      {"inputs": ["netinc", "revenue"],   "func": evl_drv3_018_net_margin_std_qoq_diff_qoq},
    "evl_drv3_019_netinc_std_ewm_diff_qoq_diff":     {"inputs": ["netinc"],              "func": evl_drv3_019_netinc_std_ewm_diff_qoq_diff},
    "evl_drv3_020_netinc_range_qoq_diff_yoy":        {"inputs": ["netinc"],              "func": evl_drv3_020_netinc_range_qoq_diff_yoy},
    "evl_drv3_021_netinc_downside_dev_qoq_yoy":      {"inputs": ["netinc"],              "func": evl_drv3_021_netinc_downside_dev_qoq_yoy},
    "evl_drv3_022_eps_std_4q_qoq_diff_yoy":          {"inputs": ["eps"],                 "func": evl_drv3_022_eps_std_4q_qoq_diff_yoy},
    "evl_drv3_023_netinc_resid_std_qoq_diff_yoy":    {"inputs": ["netinc"],              "func": evl_drv3_023_netinc_resid_std_qoq_diff_yoy},
    "evl_drv3_024_netinc_vol_z_score_qoq_diff":      {"inputs": ["netinc"],              "func": evl_drv3_024_netinc_vol_z_score_qoq_diff},
    "evl_drv3_025_earnings_instability_3rd_composite": {"inputs": ["netinc", "eps", "ebit"], "func": evl_drv3_025_earnings_instability_3rd_composite},
}
