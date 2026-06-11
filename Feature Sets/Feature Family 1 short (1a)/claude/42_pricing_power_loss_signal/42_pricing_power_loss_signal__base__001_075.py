"""pricing_power_loss_signal base features 001-075 — Pipeline 1a-inverse short-side blowup family.

75 distinct hypotheses about pricing-power erosion at peak (continued in __base__076_150.py
for 150 total). Inputs: SF1 quarterly fundamentals. PIT-clean: right-anchored rolling,
explicit min_periods, no centered windows, no forward-looking shifts. Functions consume
named pandas Series whose index is the family-agnostic time index supplied by the harness.

Lane: gross-margin level/compression, COGS-revenue divergence, ASP/volume decomposition
proxies, DuPont pricing power, sticky-vs-volatile margins, discount intensity, channel-
stuffing detection, days-inventory rising, deferred-revenue weakness, GM convexity, GM
z-score vs own history, GM rank, recency of GM peak, negative-pricing-power flags,
GM-vs-EBIT spread, SBC-burden adjustment, composite scores.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5


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


def _safe_log(s, eps=1e-12):
    if isinstance(s, pd.Series):
        return np.log(s.where(s > eps, np.nan))
    arr = np.where(s > eps, s, np.nan)
    return np.log(arr)


def _rolling_zscore(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    m = s.rolling(window, min_periods=min_periods).mean()
    sd = s.rolling(window, min_periods=min_periods).std()
    return (s - m) / sd.replace(0, np.nan)


def _winsorize(s, lo=0.01, hi=0.99):
    if not isinstance(s, pd.Series):
        return s
    q_lo = s.quantile(lo)
    q_hi = s.quantile(hi)
    return s.clip(lower=q_lo, upper=q_hi)


def _ttm(s):
    return s.rolling(4, min_periods=1).sum()


def _avg4(s):
    return s.rolling(4, min_periods=1).mean()


def _yoy_pct(s):
    return _safe_div(s - s.shift(4), s.shift(4).abs())


def _qoq_pct(s):
    return _safe_div(s.diff(), s.shift(1).abs())


def _quarters_since_max(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _qsm(w):
        if np.all(np.isnan(w)):
            return np.nan
        return (len(w) - 1) - int(np.nanargmax(w))
    return s.rolling(n, min_periods=min_periods).apply(_qsm, raw=True)


def _pct_rank(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 2)
    def _pr(w):
        if np.all(np.isnan(w)):
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        valid = w[~np.isnan(w)]
        if len(valid) < 2:
            return np.nan
        return (valid <= last).sum() / len(valid)
    return s.rolling(n, min_periods=min_periods).apply(_pr, raw=True)


def _autocorr_lag1(s, n, min_periods=None):
    if min_periods is None:
        min_periods = max(n // 3, 3)
    def _ac(w):
        if np.isnan(w).any():
            valid = ~np.isnan(w)
            if valid.sum() < min_periods:
                return np.nan
            wv = w[valid]
        else:
            wv = w
        if len(wv) < 3:
            return np.nan
        a = wv[:-1]; b = wv[1:]
        am = a.mean(); bm = b.mean()
        num = ((a - am) * (b - bm)).sum()
        da = ((a - am) ** 2).sum()
        db = ((b - bm) ** 2).sum()
        den = np.sqrt(da * db)
        if den == 0 or np.isnan(den):
            return np.nan
        return num / den
    return s.rolling(n, min_periods=min_periods).apply(_ac, raw=True)


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


# ============================================================
#                    FEATURES 001-075
# ============================================================

# ---- Block A: Gross-margin LEVEL at peak (001-008) ----

def f42_pplo_001_gm_q(revenue, gp):
    """Quarterly gross margin = gp / revenue."""
    return _safe_div(gp, revenue)


def f42_pplo_002_gm_ttm(revenue, gp):
    """Trailing-4Q gross margin = sum(gp,4) / sum(rev,4)."""
    return _safe_div(_ttm(gp), _ttm(revenue))


def f42_pplo_003_log_gm_q(revenue, gp):
    """Log of quarterly gross margin — symmetric scale for compression."""
    return _safe_log(_safe_div(gp, revenue))


def f42_pplo_004_log_gm_ttm(revenue, gp):
    """Log of TTM gross margin."""
    return _safe_log(_safe_div(_ttm(gp), _ttm(revenue)))


def f42_pplo_005_gm_q_minus_gm_4q_mean(revenue, gp):
    """GM_q minus its trailing-4Q mean — near-term compression vs own year."""
    gm = _safe_div(gp, revenue)
    return gm - gm.rolling(4, min_periods=2).mean()


def f42_pplo_006_gm_q_minus_gm_12q_mean(revenue, gp):
    """GM_q minus its 12Q mean — multi-year regime compression."""
    gm = _safe_div(gp, revenue)
    return gm - gm.rolling(12, min_periods=4).mean()


def f42_pplo_007_gm_q_minus_gm_8q_mean(revenue, gp):
    """GM_q minus its 8Q mean — medium-horizon regime compression."""
    gm = _safe_div(gp, revenue)
    return gm - gm.rolling(8, min_periods=3).mean()


def f42_pplo_008_one_minus_gm_q(revenue, gp):
    """COGS share of revenue (1 - GM)."""
    return 1.0 - _safe_div(gp, revenue)


# ---- Block B: GM compression signals (009-014) ----

def f42_pplo_009_gm_ttm_compression_4q(revenue, gp):
    """GM_ttm minus its trailing 4Q mean."""
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return gm - gm.rolling(4, min_periods=2).mean()


def f42_pplo_010_gm_ttm_compression_8q(revenue, gp):
    """GM_ttm minus its trailing 8Q mean."""
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return gm - gm.rolling(8, min_periods=3).mean()


def f42_pplo_011_gm_ttm_compression_12q(revenue, gp):
    """GM_ttm minus its trailing 12Q mean."""
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return gm - gm.rolling(12, min_periods=4).mean()


def f42_pplo_012_gm_ttm_compression_pct_4q(revenue, gp):
    """GM_ttm compression normalized by 4Q mean — % deviation."""
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    base = gm.rolling(4, min_periods=2).mean()
    return _safe_div(gm - base, base.abs())


def f42_pplo_013_gm_ttm_minus_4q_max(revenue, gp):
    """Distance below trailing-year max GM_ttm — recent peak compression."""
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return gm - gm.rolling(4, min_periods=2).max()


def f42_pplo_014_gm_ttm_minus_12q_max(revenue, gp):
    """Distance below 12Q max GM_ttm — multi-year peak compression."""
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return gm - gm.rolling(12, min_periods=4).max()


# ---- Block C: COGS-revenue divergence (015-020) ----

def f42_pplo_015_cogs_growth_q_minus_rev_growth_q(revenue, cor):
    """QoQ COGS growth − QoQ revenue growth (positive = pricing power loss)."""
    return _qoq_pct(cor) - _qoq_pct(revenue)


def f42_pplo_016_cogs_growth_yoy_minus_rev_growth_yoy(revenue, cor):
    """YoY COGS growth − YoY revenue growth (cost outpacing pricing)."""
    return _yoy_pct(cor) - _yoy_pct(revenue)


def f42_pplo_017_cogs_growth_2y_minus_rev_growth_2y(revenue, cor):
    """2y COGS growth − 2y revenue growth — secular pricing erosion."""
    cg = _safe_div(cor - cor.shift(8), cor.shift(8).abs())
    rg = _safe_div(revenue - revenue.shift(8), revenue.shift(8).abs())
    return cg - rg


def f42_pplo_018_cogs_yoy_growth(revenue, cor):
    """Raw YoY COGS growth (sanity-check on cost trajectory). Revenue param unused."""
    _ = revenue
    return _yoy_pct(cor)


def f42_pplo_019_rev_growth_yoy_minus_4q_cogs_growth_mean(revenue, cor):
    """Revenue YoY growth − mean(COGS YoY growth, 4Q) — sustained gap measure."""
    return _yoy_pct(revenue) - _yoy_pct(cor).rolling(4, min_periods=2).mean()


def f42_pplo_020_cogs_to_rev_growth_ratio_yoy(revenue, cor):
    """Ratio of COGS YoY growth to revenue YoY growth — >1 = pricing weakness."""
    return _safe_div(_yoy_pct(cor), _yoy_pct(revenue))


# ---- Block D: GP growth vs Rev growth gap (021-024) ----

def f42_pplo_021_gp_yoy_minus_rev_yoy(revenue, gp):
    """YoY gross-profit growth − YoY revenue growth."""
    return _yoy_pct(gp) - _yoy_pct(revenue)


def f42_pplo_022_gp_qoq_minus_rev_qoq(revenue, gp):
    """QoQ GP growth − QoQ revenue growth — near-term pricing-power shift."""
    return _qoq_pct(gp) - _qoq_pct(revenue)


def f42_pplo_023_gp_2y_minus_rev_2y(revenue, gp):
    """2y GP growth − 2y revenue growth."""
    gg = _safe_div(gp - gp.shift(8), gp.shift(8).abs())
    rg = _safe_div(revenue - revenue.shift(8), revenue.shift(8).abs())
    return gg - rg


def f42_pplo_024_gp_ttm_yoy_minus_rev_ttm_yoy(revenue, gp):
    """TTM-smoothed GP YoY growth − TTM-smoothed revenue YoY growth."""
    gp_t = _ttm(gp); rv_t = _ttm(revenue)
    return _safe_div(gp_t - gp_t.shift(4), gp_t.shift(4).abs()) - \
           _safe_div(rv_t - rv_t.shift(4), rv_t.shift(4).abs())


# ---- Block E: ASP / volume decomposition proxies (025-030) ----

def f42_pplo_025_rev_per_inventory(revenue, inventory):
    """Revenue / inventory — volume-proxy turnover (higher = stronger ASP × volume)."""
    return _safe_div(revenue, inventory)


def f42_pplo_026_rev_per_inventory_yoy_change(revenue, inventory):
    """YoY change in revenue/inventory — pricing-power degradation if falling."""
    return _safe_div(revenue, inventory).diff(4)


def f42_pplo_027_value_capture_share(revenue, cor):
    """ASP-like proxy = revenue / (revenue + COGS) — share of value capture."""
    return _safe_div(revenue, revenue + cor)


def f42_pplo_028_value_capture_share_qoq_change(revenue, cor):
    """QoQ change in ASP proxy."""
    return _safe_div(revenue, revenue + cor).diff()


def f42_pplo_029_value_capture_share_yoy_change(revenue, cor):
    """YoY change in ASP proxy."""
    return _safe_div(revenue, revenue + cor).diff(4)


def f42_pplo_030_inventory_turnover_yoy_change(cor, inventory):
    """Inventory turnover = COGS / inventory; YoY change."""
    return _safe_div(cor, inventory).diff(4)


# ---- Block F: DuPont pricing power: GM × asset turnover (031-036) ----

def f42_pplo_031_dupont_gm_x_at_q(revenue, gp, assets):
    """Quarterly (GM)×(asset turnover) — pricing power × velocity."""
    return _safe_div(gp, revenue) * _safe_div(revenue, assets)


def f42_pplo_032_dupont_gm_x_at_ttm(revenue, gp, assets):
    """TTM (GM_ttm)×(rev_ttm / assets)."""
    return _safe_div(_ttm(gp), _ttm(revenue)) * _safe_div(_ttm(revenue), assets)


def f42_pplo_033_dupont_gm_x_at_yoy_change(revenue, gp, assets):
    """YoY change in DuPont GM × asset turnover."""
    s = _safe_div(gp, revenue) * _safe_div(revenue, assets)
    return s.diff(4)


def f42_pplo_034_dupont_gm_x_at_2y_change(revenue, gp, assets):
    """2y change in DuPont GM × asset turnover."""
    s = _safe_div(gp, revenue) * _safe_div(revenue, assets)
    return s.diff(8)


def f42_pplo_035_dupont_gm_x_at_log(revenue, gp, assets):
    """Log of DuPont GM × asset turnover — symmetric scale."""
    return _safe_log(_safe_div(gp, revenue) * _safe_div(revenue, assets))


def f42_pplo_036_dupont_gm_x_at_zscore_12q(revenue, gp, assets):
    """Z-score of DuPont GM×AT vs its trailing 12Q distribution."""
    s = _safe_div(gp, revenue) * _safe_div(revenue, assets)
    return _rolling_zscore(s, 12, min_periods=4)


# ---- Block G: Sticky vs volatile margins (037-040) ----

def f42_pplo_037_gm_std_4q(revenue, gp):
    """Rolling std of quarterly GM over 4Q."""
    return _safe_div(gp, revenue).rolling(4, min_periods=2).std()


def f42_pplo_038_gm_std_8q(revenue, gp):
    """Rolling std of quarterly GM over 8Q."""
    return _safe_div(gp, revenue).rolling(8, min_periods=3).std()


def f42_pplo_039_gm_std_12q(revenue, gp):
    """Rolling std of quarterly GM over 12Q."""
    return _safe_div(gp, revenue).rolling(12, min_periods=4).std()


def f42_pplo_040_gm_cv_8q(revenue, gp):
    """Coefficient of variation of GM over 8Q (std/|mean|)."""
    gm = _safe_div(gp, revenue)
    m = gm.rolling(8, min_periods=3).mean()
    sd = gm.rolling(8, min_periods=3).std()
    return _safe_div(sd, m.abs())


# ---- Block H: Discount intensity proxies (041-046) ----

def f42_pplo_041_rev_change_minus_ar_change(revenue, receivables):
    """ΔRevenue − ΔAR — cash-collected revenue proxy (negative = AR-driven sales)."""
    return revenue.diff() - receivables.diff()


def f42_pplo_042_delta_rev_div_delta_ar(revenue, receivables):
    """ΔRevenue / ΔAR — high = cash sales; low/<0 = revenue from receivables."""
    return _safe_div(revenue.diff(), receivables.diff())


def f42_pplo_043_delta_rev_div_delta_ar_yoy(revenue, receivables):
    """YoY change in ΔRev/ΔAR — discount-intensity drift."""
    return _safe_div(revenue.diff(), receivables.diff()).diff(4)


def f42_pplo_044_rev_div_lagged_ar(revenue, receivables):
    """Revenue / AR(t-1) — collection efficiency proxy."""
    return _safe_div(revenue, receivables.shift(1))


def f42_pplo_045_rev_yoy_minus_ar_yoy(revenue, receivables):
    """Revenue YoY growth − AR YoY growth — gap = collection discipline."""
    return _yoy_pct(revenue) - _yoy_pct(receivables)


def f42_pplo_046_discount_intensity_proxy(revenue, gp):
    """(-ΔGM_q) × max(rev_yoy_growth,0) — margin sacrificed for top-line."""
    gm = _safe_div(gp, revenue)
    rg = _yoy_pct(revenue)
    return (-gm.diff()) * rg.clip(lower=0.0)


# ---- Block I: Channel-stuffing detection (047-054) ----

def f42_pplo_047_ar_yoy_minus_rev_yoy(revenue, receivables):
    """AR YoY growth − revenue YoY growth — positive = stuffing."""
    return _yoy_pct(receivables) - _yoy_pct(revenue)


def f42_pplo_048_ar_qoq_minus_rev_qoq(revenue, receivables):
    """AR QoQ growth − revenue QoQ growth — near-term stuffing."""
    return _qoq_pct(receivables) - _qoq_pct(revenue)


def f42_pplo_049_ar_to_rev_slope_8q(revenue, receivables):
    """Slope of AR/revenue ratio over 8Q — rising slope = stuffing trend."""
    r = _safe_div(receivables, revenue)
    return _rolling_slope(r, 8, min_periods=3)


def f42_pplo_050_ar_to_rev_ttm(revenue, receivables):
    """AR / revenue_ttm — normalized AR burden."""
    return _safe_div(receivables, _ttm(revenue))


def f42_pplo_051_ar_to_rev_ttm_yoy_change(revenue, receivables):
    """YoY change in AR / rev_ttm."""
    return _safe_div(receivables, _ttm(revenue)).diff(4)


def f42_pplo_052_dso_q(revenue, receivables):
    """DSO = (AR / rev_ttm) × 365 — days sales outstanding."""
    return _safe_div(receivables, _ttm(revenue)) * 365.0


def f42_pplo_053_dso_yoy_change(revenue, receivables):
    """YoY change in DSO."""
    return (_safe_div(receivables, _ttm(revenue)) * 365.0).diff(4)


def f42_pplo_054_dso_zscore_12q(revenue, receivables):
    """Z-score of DSO vs 12Q history."""
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    return _rolling_zscore(dso, 12, min_periods=4)


# ---- Block J: Days inventory rising / demand softness (055-062) ----

def f42_pplo_055_dio_q(cor, inventory):
    """DIO = (inventory / COGS_ttm) × 365."""
    return _safe_div(inventory, _ttm(cor)) * 365.0


def f42_pplo_056_dio_yoy_change(cor, inventory):
    """YoY change in DIO — demand softness if rising."""
    return (_safe_div(inventory, _ttm(cor)) * 365.0).diff(4)


def f42_pplo_057_dio_zscore_12q(cor, inventory):
    """Z-score of DIO vs 12Q history."""
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    return _rolling_zscore(dio, 12, min_periods=4)


def f42_pplo_058_inv_yoy_minus_cogs_yoy(cor, inventory):
    """Inventory YoY growth − COGS YoY growth — building unsold stock."""
    return _yoy_pct(inventory) - _yoy_pct(cor)


def f42_pplo_059_inv_qoq_minus_cogs_qoq(cor, inventory):
    """Inventory QoQ growth − COGS QoQ growth — near-term inventory bloat."""
    return _qoq_pct(inventory) - _qoq_pct(cor)


def f42_pplo_060_inv_to_rev_slope_8q(revenue, inventory):
    """Slope of inventory/revenue over 8Q — demand softening if rising."""
    r = _safe_div(inventory, revenue)
    return _rolling_slope(r, 8, min_periods=3)


def f42_pplo_061_inv_to_rev_ttm(revenue, inventory):
    """Inventory / rev_ttm — normalized inventory burden."""
    return _safe_div(inventory, _ttm(revenue))


def f42_pplo_062_inv_to_rev_ttm_yoy_change(revenue, inventory):
    """YoY change in inventory / rev_ttm."""
    return _safe_div(inventory, _ttm(revenue)).diff(4)


# ---- Block K: Deferred revenue dynamics (063-066) ----

def f42_pplo_063_defrev_to_rev_ttm(revenue, deferredrev):
    """Deferred revenue / rev_ttm — backlog cushion ratio."""
    return _safe_div(deferredrev, _ttm(revenue))


def f42_pplo_064_defrev_to_rev_yoy_change(revenue, deferredrev):
    """YoY change in DefRev/rev_ttm — falling = future-bookings weakness."""
    return _safe_div(deferredrev, _ttm(revenue)).diff(4)


def f42_pplo_065_defrev_yoy_growth(revenue, deferredrev):
    """DefRev YoY growth (revenue param unused but kept for harness symmetry)."""
    _ = revenue
    return _yoy_pct(deferredrev)


def f42_pplo_066_defrev_growth_minus_rev_growth_yoy(revenue, deferredrev):
    """DefRev YoY growth − revenue YoY growth — bookings vs recognized rev gap."""
    return _yoy_pct(deferredrev) - _yoy_pct(revenue)


# ---- Block L: Operating margin contribution from GM only (067-070) ----

def f42_pplo_067_gm_minus_sga_share(revenue, gp, sga):
    """GM − SGA/revenue — operating margin from GM only."""
    return _safe_div(gp, revenue) - _safe_div(sga, revenue)


def f42_pplo_068_gm_minus_sga_share_yoy_change(revenue, gp, sga):
    """YoY change in (GM − SGA/rev)."""
    s = _safe_div(gp, revenue) - _safe_div(sga, revenue)
    return s.diff(4)


def f42_pplo_069_gm_minus_sga_share_zscore_12q(revenue, gp, sga):
    """Z-score of (GM − SGA/rev) vs 12Q."""
    s = _safe_div(gp, revenue) - _safe_div(sga, revenue)
    return _rolling_zscore(s, 12, min_periods=4)


def f42_pplo_070_gm_minus_opex_share(revenue, gp, opex):
    """GM − opex/revenue — broader operating-margin-from-GM proxy."""
    return _safe_div(gp, revenue) - _safe_div(opex, revenue)


# ---- Block M: Gross-margin convexity (071-074) ----

def f42_pplo_071_gm_rolling_skew_8q(revenue, gp):
    """Rolling skew of GM over 8Q."""
    return _safe_div(gp, revenue).rolling(8, min_periods=4).skew()


def f42_pplo_072_gm_rolling_skew_12q(revenue, gp):
    """Rolling skew of GM over 12Q."""
    return _safe_div(gp, revenue).rolling(12, min_periods=5).skew()


def f42_pplo_073_gm_rolling_kurt_8q(revenue, gp):
    """Rolling kurtosis of GM over 8Q."""
    return _safe_div(gp, revenue).rolling(8, min_periods=4).kurt()


def f42_pplo_074_gm_rolling_kurt_12q(revenue, gp):
    """Rolling kurtosis of GM over 12Q."""
    return _safe_div(gp, revenue).rolling(12, min_periods=5).kurt()


# ---- Block N: GM z-score vs own history (075) ----

def f42_pplo_075_gm_zscore_8q(revenue, gp):
    """GM z-score vs its own trailing 8Q — short regime."""
    return _rolling_zscore(_safe_div(gp, revenue), 8, min_periods=3)


# ============================================================
#                        REGISTRY
# ============================================================

PRICING_POWER_LOSS_SIGNAL_BASE_REGISTRY_001_075 = {
    "f42_pplo_001_gm_q": {"inputs": ["revenue", "gp"], "func": f42_pplo_001_gm_q},
    "f42_pplo_002_gm_ttm": {"inputs": ["revenue", "gp"], "func": f42_pplo_002_gm_ttm},
    "f42_pplo_003_log_gm_q": {"inputs": ["revenue", "gp"], "func": f42_pplo_003_log_gm_q},
    "f42_pplo_004_log_gm_ttm": {"inputs": ["revenue", "gp"], "func": f42_pplo_004_log_gm_ttm},
    "f42_pplo_005_gm_q_minus_gm_4q_mean": {"inputs": ["revenue", "gp"], "func": f42_pplo_005_gm_q_minus_gm_4q_mean},
    "f42_pplo_006_gm_q_minus_gm_12q_mean": {"inputs": ["revenue", "gp"], "func": f42_pplo_006_gm_q_minus_gm_12q_mean},
    "f42_pplo_007_gm_q_minus_gm_8q_mean": {"inputs": ["revenue", "gp"], "func": f42_pplo_007_gm_q_minus_gm_8q_mean},
    "f42_pplo_008_one_minus_gm_q": {"inputs": ["revenue", "gp"], "func": f42_pplo_008_one_minus_gm_q},
    "f42_pplo_009_gm_ttm_compression_4q": {"inputs": ["revenue", "gp"], "func": f42_pplo_009_gm_ttm_compression_4q},
    "f42_pplo_010_gm_ttm_compression_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_010_gm_ttm_compression_8q},
    "f42_pplo_011_gm_ttm_compression_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_011_gm_ttm_compression_12q},
    "f42_pplo_012_gm_ttm_compression_pct_4q": {"inputs": ["revenue", "gp"], "func": f42_pplo_012_gm_ttm_compression_pct_4q},
    "f42_pplo_013_gm_ttm_minus_4q_max": {"inputs": ["revenue", "gp"], "func": f42_pplo_013_gm_ttm_minus_4q_max},
    "f42_pplo_014_gm_ttm_minus_12q_max": {"inputs": ["revenue", "gp"], "func": f42_pplo_014_gm_ttm_minus_12q_max},
    "f42_pplo_015_cogs_growth_q_minus_rev_growth_q": {"inputs": ["revenue", "cor"], "func": f42_pplo_015_cogs_growth_q_minus_rev_growth_q},
    "f42_pplo_016_cogs_growth_yoy_minus_rev_growth_yoy": {"inputs": ["revenue", "cor"], "func": f42_pplo_016_cogs_growth_yoy_minus_rev_growth_yoy},
    "f42_pplo_017_cogs_growth_2y_minus_rev_growth_2y": {"inputs": ["revenue", "cor"], "func": f42_pplo_017_cogs_growth_2y_minus_rev_growth_2y},
    "f42_pplo_018_cogs_yoy_growth": {"inputs": ["revenue", "cor"], "func": f42_pplo_018_cogs_yoy_growth},
    "f42_pplo_019_rev_growth_yoy_minus_4q_cogs_growth_mean": {"inputs": ["revenue", "cor"], "func": f42_pplo_019_rev_growth_yoy_minus_4q_cogs_growth_mean},
    "f42_pplo_020_cogs_to_rev_growth_ratio_yoy": {"inputs": ["revenue", "cor"], "func": f42_pplo_020_cogs_to_rev_growth_ratio_yoy},
    "f42_pplo_021_gp_yoy_minus_rev_yoy": {"inputs": ["revenue", "gp"], "func": f42_pplo_021_gp_yoy_minus_rev_yoy},
    "f42_pplo_022_gp_qoq_minus_rev_qoq": {"inputs": ["revenue", "gp"], "func": f42_pplo_022_gp_qoq_minus_rev_qoq},
    "f42_pplo_023_gp_2y_minus_rev_2y": {"inputs": ["revenue", "gp"], "func": f42_pplo_023_gp_2y_minus_rev_2y},
    "f42_pplo_024_gp_ttm_yoy_minus_rev_ttm_yoy": {"inputs": ["revenue", "gp"], "func": f42_pplo_024_gp_ttm_yoy_minus_rev_ttm_yoy},
    "f42_pplo_025_rev_per_inventory": {"inputs": ["revenue", "inventory"], "func": f42_pplo_025_rev_per_inventory},
    "f42_pplo_026_rev_per_inventory_yoy_change": {"inputs": ["revenue", "inventory"], "func": f42_pplo_026_rev_per_inventory_yoy_change},
    "f42_pplo_027_value_capture_share": {"inputs": ["revenue", "cor"], "func": f42_pplo_027_value_capture_share},
    "f42_pplo_028_value_capture_share_qoq_change": {"inputs": ["revenue", "cor"], "func": f42_pplo_028_value_capture_share_qoq_change},
    "f42_pplo_029_value_capture_share_yoy_change": {"inputs": ["revenue", "cor"], "func": f42_pplo_029_value_capture_share_yoy_change},
    "f42_pplo_030_inventory_turnover_yoy_change": {"inputs": ["cor", "inventory"], "func": f42_pplo_030_inventory_turnover_yoy_change},
    "f42_pplo_031_dupont_gm_x_at_q": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_031_dupont_gm_x_at_q},
    "f42_pplo_032_dupont_gm_x_at_ttm": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_032_dupont_gm_x_at_ttm},
    "f42_pplo_033_dupont_gm_x_at_yoy_change": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_033_dupont_gm_x_at_yoy_change},
    "f42_pplo_034_dupont_gm_x_at_2y_change": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_034_dupont_gm_x_at_2y_change},
    "f42_pplo_035_dupont_gm_x_at_log": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_035_dupont_gm_x_at_log},
    "f42_pplo_036_dupont_gm_x_at_zscore_12q": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_036_dupont_gm_x_at_zscore_12q},
    "f42_pplo_037_gm_std_4q": {"inputs": ["revenue", "gp"], "func": f42_pplo_037_gm_std_4q},
    "f42_pplo_038_gm_std_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_038_gm_std_8q},
    "f42_pplo_039_gm_std_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_039_gm_std_12q},
    "f42_pplo_040_gm_cv_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_040_gm_cv_8q},
    "f42_pplo_041_rev_change_minus_ar_change": {"inputs": ["revenue", "receivables"], "func": f42_pplo_041_rev_change_minus_ar_change},
    "f42_pplo_042_delta_rev_div_delta_ar": {"inputs": ["revenue", "receivables"], "func": f42_pplo_042_delta_rev_div_delta_ar},
    "f42_pplo_043_delta_rev_div_delta_ar_yoy": {"inputs": ["revenue", "receivables"], "func": f42_pplo_043_delta_rev_div_delta_ar_yoy},
    "f42_pplo_044_rev_div_lagged_ar": {"inputs": ["revenue", "receivables"], "func": f42_pplo_044_rev_div_lagged_ar},
    "f42_pplo_045_rev_yoy_minus_ar_yoy": {"inputs": ["revenue", "receivables"], "func": f42_pplo_045_rev_yoy_minus_ar_yoy},
    "f42_pplo_046_discount_intensity_proxy": {"inputs": ["revenue", "gp"], "func": f42_pplo_046_discount_intensity_proxy},
    "f42_pplo_047_ar_yoy_minus_rev_yoy": {"inputs": ["revenue", "receivables"], "func": f42_pplo_047_ar_yoy_minus_rev_yoy},
    "f42_pplo_048_ar_qoq_minus_rev_qoq": {"inputs": ["revenue", "receivables"], "func": f42_pplo_048_ar_qoq_minus_rev_qoq},
    "f42_pplo_049_ar_to_rev_slope_8q": {"inputs": ["revenue", "receivables"], "func": f42_pplo_049_ar_to_rev_slope_8q},
    "f42_pplo_050_ar_to_rev_ttm": {"inputs": ["revenue", "receivables"], "func": f42_pplo_050_ar_to_rev_ttm},
    "f42_pplo_051_ar_to_rev_ttm_yoy_change": {"inputs": ["revenue", "receivables"], "func": f42_pplo_051_ar_to_rev_ttm_yoy_change},
    "f42_pplo_052_dso_q": {"inputs": ["revenue", "receivables"], "func": f42_pplo_052_dso_q},
    "f42_pplo_053_dso_yoy_change": {"inputs": ["revenue", "receivables"], "func": f42_pplo_053_dso_yoy_change},
    "f42_pplo_054_dso_zscore_12q": {"inputs": ["revenue", "receivables"], "func": f42_pplo_054_dso_zscore_12q},
    "f42_pplo_055_dio_q": {"inputs": ["cor", "inventory"], "func": f42_pplo_055_dio_q},
    "f42_pplo_056_dio_yoy_change": {"inputs": ["cor", "inventory"], "func": f42_pplo_056_dio_yoy_change},
    "f42_pplo_057_dio_zscore_12q": {"inputs": ["cor", "inventory"], "func": f42_pplo_057_dio_zscore_12q},
    "f42_pplo_058_inv_yoy_minus_cogs_yoy": {"inputs": ["cor", "inventory"], "func": f42_pplo_058_inv_yoy_minus_cogs_yoy},
    "f42_pplo_059_inv_qoq_minus_cogs_qoq": {"inputs": ["cor", "inventory"], "func": f42_pplo_059_inv_qoq_minus_cogs_qoq},
    "f42_pplo_060_inv_to_rev_slope_8q": {"inputs": ["revenue", "inventory"], "func": f42_pplo_060_inv_to_rev_slope_8q},
    "f42_pplo_061_inv_to_rev_ttm": {"inputs": ["revenue", "inventory"], "func": f42_pplo_061_inv_to_rev_ttm},
    "f42_pplo_062_inv_to_rev_ttm_yoy_change": {"inputs": ["revenue", "inventory"], "func": f42_pplo_062_inv_to_rev_ttm_yoy_change},
    "f42_pplo_063_defrev_to_rev_ttm": {"inputs": ["revenue", "deferredrev"], "func": f42_pplo_063_defrev_to_rev_ttm},
    "f42_pplo_064_defrev_to_rev_yoy_change": {"inputs": ["revenue", "deferredrev"], "func": f42_pplo_064_defrev_to_rev_yoy_change},
    "f42_pplo_065_defrev_yoy_growth": {"inputs": ["revenue", "deferredrev"], "func": f42_pplo_065_defrev_yoy_growth},
    "f42_pplo_066_defrev_growth_minus_rev_growth_yoy": {"inputs": ["revenue", "deferredrev"], "func": f42_pplo_066_defrev_growth_minus_rev_growth_yoy},
    "f42_pplo_067_gm_minus_sga_share": {"inputs": ["revenue", "gp", "sga"], "func": f42_pplo_067_gm_minus_sga_share},
    "f42_pplo_068_gm_minus_sga_share_yoy_change": {"inputs": ["revenue", "gp", "sga"], "func": f42_pplo_068_gm_minus_sga_share_yoy_change},
    "f42_pplo_069_gm_minus_sga_share_zscore_12q": {"inputs": ["revenue", "gp", "sga"], "func": f42_pplo_069_gm_minus_sga_share_zscore_12q},
    "f42_pplo_070_gm_minus_opex_share": {"inputs": ["revenue", "gp", "opex"], "func": f42_pplo_070_gm_minus_opex_share},
    "f42_pplo_071_gm_rolling_skew_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_071_gm_rolling_skew_8q},
    "f42_pplo_072_gm_rolling_skew_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_072_gm_rolling_skew_12q},
    "f42_pplo_073_gm_rolling_kurt_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_073_gm_rolling_kurt_8q},
    "f42_pplo_074_gm_rolling_kurt_12q": {"inputs": ["revenue", "gp"], "func": f42_pplo_074_gm_rolling_kurt_12q},
    "f42_pplo_075_gm_zscore_8q": {"inputs": ["revenue", "gp"], "func": f42_pplo_075_gm_zscore_8q},
}
