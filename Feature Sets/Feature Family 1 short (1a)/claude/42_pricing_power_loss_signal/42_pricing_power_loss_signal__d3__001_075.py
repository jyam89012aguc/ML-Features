"""pricing_power_loss_signal D3 features 001-075 — order-3 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff() applied
3 time(s). Self-contained; helpers redefined locally per HANDOFF. PIT-clean.
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
#                    D3 FEATURES 001-075
# ============================================================

def f42_pplo_001_gm_q_d3(revenue, gp):
    return (_safe_div(gp, revenue)).diff().diff().diff()


def f42_pplo_002_gm_ttm_d3(revenue, gp):
    return (_safe_div(_ttm(gp), _ttm(revenue))).diff().diff().diff()


def f42_pplo_003_log_gm_q_d3(revenue, gp):
    return (_safe_log(_safe_div(gp, revenue))).diff().diff().diff()


def f42_pplo_004_log_gm_ttm_d3(revenue, gp):
    return (_safe_log(_safe_div(_ttm(gp), _ttm(revenue)))).diff().diff().diff()


def f42_pplo_005_gm_q_minus_gm_4q_mean_d3(revenue, gp):
    gm = _safe_div(gp, revenue)
    return (gm - gm.rolling(4, min_periods=2).mean()).diff().diff().diff()


def f42_pplo_006_gm_q_minus_gm_12q_mean_d3(revenue, gp):
    gm = _safe_div(gp, revenue)
    return (gm - gm.rolling(12, min_periods=4).mean()).diff().diff().diff()


def f42_pplo_007_gm_q_minus_gm_8q_mean_d3(revenue, gp):
    gm = _safe_div(gp, revenue)
    return (gm - gm.rolling(8, min_periods=3).mean()).diff().diff().diff()


def f42_pplo_008_one_minus_gm_q_d3(revenue, gp):
    return (1.0 - _safe_div(gp, revenue)).diff().diff().diff()


def f42_pplo_009_gm_ttm_compression_4q_d3(revenue, gp):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return (gm - gm.rolling(4, min_periods=2).mean()).diff().diff().diff()


def f42_pplo_010_gm_ttm_compression_8q_d3(revenue, gp):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return (gm - gm.rolling(8, min_periods=3).mean()).diff().diff().diff()


def f42_pplo_011_gm_ttm_compression_12q_d3(revenue, gp):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return (gm - gm.rolling(12, min_periods=4).mean()).diff().diff().diff()


def f42_pplo_012_gm_ttm_compression_pct_4q_d3(revenue, gp):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    base = gm.rolling(4, min_periods=2).mean()
    return (_safe_div(gm - base, base.abs())).diff().diff().diff()


def f42_pplo_013_gm_ttm_minus_4q_max_d3(revenue, gp):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return (gm - gm.rolling(4, min_periods=2).max()).diff().diff().diff()


def f42_pplo_014_gm_ttm_minus_12q_max_d3(revenue, gp):
    gm = _safe_div(_ttm(gp), _ttm(revenue))
    return (gm - gm.rolling(12, min_periods=4).max()).diff().diff().diff()


def f42_pplo_015_cogs_growth_q_minus_rev_growth_q_d3(revenue, cor):
    return (_qoq_pct(cor) - _qoq_pct(revenue)).diff().diff().diff()


def f42_pplo_016_cogs_growth_yoy_minus_rev_growth_yoy_d3(revenue, cor):
    return (_yoy_pct(cor) - _yoy_pct(revenue)).diff().diff().diff()


def f42_pplo_017_cogs_growth_2y_minus_rev_growth_2y_d3(revenue, cor):
    cg = _safe_div(cor - cor.shift(8), cor.shift(8).abs())
    rg = _safe_div(revenue - revenue.shift(8), revenue.shift(8).abs())
    return (cg - rg).diff().diff().diff()


def f42_pplo_018_cogs_yoy_growth_d3(revenue, cor):
    _ = revenue
    return (_yoy_pct(cor)).diff().diff().diff()


def f42_pplo_019_rev_growth_yoy_minus_4q_cogs_growth_mean_d3(revenue, cor):
    return (_yoy_pct(revenue) - _yoy_pct(cor).rolling(4, min_periods=2).mean()).diff().diff().diff()


def f42_pplo_020_cogs_to_rev_growth_ratio_yoy_d3(revenue, cor):
    return (_safe_div(_yoy_pct(cor), _yoy_pct(revenue))).diff().diff().diff()


def f42_pplo_021_gp_yoy_minus_rev_yoy_d3(revenue, gp):
    return (_yoy_pct(gp) - _yoy_pct(revenue)).diff().diff().diff()


def f42_pplo_022_gp_qoq_minus_rev_qoq_d3(revenue, gp):
    return (_qoq_pct(gp) - _qoq_pct(revenue)).diff().diff().diff()


def f42_pplo_023_gp_2y_minus_rev_2y_d3(revenue, gp):
    gg = _safe_div(gp - gp.shift(8), gp.shift(8).abs())
    rg = _safe_div(revenue - revenue.shift(8), revenue.shift(8).abs())
    return (gg - rg).diff().diff().diff()


def f42_pplo_024_gp_ttm_yoy_minus_rev_ttm_yoy_d3(revenue, gp):
    gp_t = _ttm(gp); rv_t = _ttm(revenue)
    return (_safe_div(gp_t - gp_t.shift(4), gp_t.shift(4).abs()) - \
           _safe_div(rv_t - rv_t.shift(4), rv_t.shift(4).abs())).diff().diff().diff()


def f42_pplo_025_rev_per_inventory_d3(revenue, inventory):
    return (_safe_div(revenue, inventory)).diff().diff().diff()


def f42_pplo_026_rev_per_inventory_yoy_change_d3(revenue, inventory):
    return (_safe_div(revenue, inventory).diff(4)).diff().diff().diff()


def f42_pplo_027_value_capture_share_d3(revenue, cor):
    return (_safe_div(revenue, revenue + cor)).diff().diff().diff()


def f42_pplo_028_value_capture_share_qoq_change_d3(revenue, cor):
    return (_safe_div(revenue, revenue + cor).diff()).diff().diff().diff()


def f42_pplo_029_value_capture_share_yoy_change_d3(revenue, cor):
    return (_safe_div(revenue, revenue + cor).diff(4)).diff().diff().diff()


def f42_pplo_030_inventory_turnover_yoy_change_d3(cor, inventory):
    return (_safe_div(cor, inventory).diff(4)).diff().diff().diff()


def f42_pplo_031_dupont_gm_x_at_q_d3(revenue, gp, assets):
    return (_safe_div(gp, revenue) * _safe_div(revenue, assets)).diff().diff().diff()


def f42_pplo_032_dupont_gm_x_at_ttm_d3(revenue, gp, assets):
    return (_safe_div(_ttm(gp), _ttm(revenue)) * _safe_div(_ttm(revenue), assets)).diff().diff().diff()


def f42_pplo_033_dupont_gm_x_at_yoy_change_d3(revenue, gp, assets):
    s = _safe_div(gp, revenue) * _safe_div(revenue, assets)
    return (s.diff(4)).diff().diff().diff()


def f42_pplo_034_dupont_gm_x_at_2y_change_d3(revenue, gp, assets):
    s = _safe_div(gp, revenue) * _safe_div(revenue, assets)
    return (s.diff(8)).diff().diff().diff()


def f42_pplo_035_dupont_gm_x_at_log_d3(revenue, gp, assets):
    return (_safe_log(_safe_div(gp, revenue) * _safe_div(revenue, assets))).diff().diff().diff()


def f42_pplo_036_dupont_gm_x_at_zscore_12q_d3(revenue, gp, assets):
    s = _safe_div(gp, revenue) * _safe_div(revenue, assets)
    return (_rolling_zscore(s, 12, min_periods=4)).diff().diff().diff()


def f42_pplo_037_gm_std_4q_d3(revenue, gp):
    return (_safe_div(gp, revenue).rolling(4, min_periods=2).std()).diff().diff().diff()


def f42_pplo_038_gm_std_8q_d3(revenue, gp):
    return (_safe_div(gp, revenue).rolling(8, min_periods=3).std()).diff().diff().diff()


def f42_pplo_039_gm_std_12q_d3(revenue, gp):
    return (_safe_div(gp, revenue).rolling(12, min_periods=4).std()).diff().diff().diff()


def f42_pplo_040_gm_cv_8q_d3(revenue, gp):
    gm = _safe_div(gp, revenue)
    m = gm.rolling(8, min_periods=3).mean()
    sd = gm.rolling(8, min_periods=3).std()
    return (_safe_div(sd, m.abs())).diff().diff().diff()


def f42_pplo_041_rev_change_minus_ar_change_d3(revenue, receivables):
    return (revenue.diff() - receivables.diff()).diff().diff().diff()


def f42_pplo_042_delta_rev_div_delta_ar_d3(revenue, receivables):
    return (_safe_div(revenue.diff(), receivables.diff())).diff().diff().diff()


def f42_pplo_043_delta_rev_div_delta_ar_yoy_d3(revenue, receivables):
    return (_safe_div(revenue.diff(), receivables.diff()).diff(4)).diff().diff().diff()


def f42_pplo_044_rev_div_lagged_ar_d3(revenue, receivables):
    return (_safe_div(revenue, receivables.shift(1))).diff().diff().diff()


def f42_pplo_045_rev_yoy_minus_ar_yoy_d3(revenue, receivables):
    return (_yoy_pct(revenue) - _yoy_pct(receivables)).diff().diff().diff()


def f42_pplo_046_discount_intensity_proxy_d3(revenue, gp):
    gm = _safe_div(gp, revenue)
    rg = _yoy_pct(revenue)
    return ((-gm.diff()) * rg.clip(lower=0.0)).diff().diff().diff()


def f42_pplo_047_ar_yoy_minus_rev_yoy_d3(revenue, receivables):
    return (_yoy_pct(receivables) - _yoy_pct(revenue)).diff().diff().diff()


def f42_pplo_048_ar_qoq_minus_rev_qoq_d3(revenue, receivables):
    return (_qoq_pct(receivables) - _qoq_pct(revenue)).diff().diff().diff()


def f42_pplo_049_ar_to_rev_slope_8q_d3(revenue, receivables):
    r = _safe_div(receivables, revenue)
    return (_rolling_slope(r, 8, min_periods=3)).diff().diff().diff()


def f42_pplo_050_ar_to_rev_ttm_d3(revenue, receivables):
    return (_safe_div(receivables, _ttm(revenue))).diff().diff().diff()


def f42_pplo_051_ar_to_rev_ttm_yoy_change_d3(revenue, receivables):
    return (_safe_div(receivables, _ttm(revenue)).diff(4)).diff().diff().diff()


def f42_pplo_052_dso_q_d3(revenue, receivables):
    return (_safe_div(receivables, _ttm(revenue)) * 365.0).diff().diff().diff()


def f42_pplo_053_dso_yoy_change_d3(revenue, receivables):
    return ((_safe_div(receivables, _ttm(revenue)) * 365.0).diff(4)).diff().diff().diff()


def f42_pplo_054_dso_zscore_12q_d3(revenue, receivables):
    dso = _safe_div(receivables, _ttm(revenue)) * 365.0
    return (_rolling_zscore(dso, 12, min_periods=4)).diff().diff().diff()


def f42_pplo_055_dio_q_d3(cor, inventory):
    return (_safe_div(inventory, _ttm(cor)) * 365.0).diff().diff().diff()


def f42_pplo_056_dio_yoy_change_d3(cor, inventory):
    return ((_safe_div(inventory, _ttm(cor)) * 365.0).diff(4)).diff().diff().diff()


def f42_pplo_057_dio_zscore_12q_d3(cor, inventory):
    dio = _safe_div(inventory, _ttm(cor)) * 365.0
    return (_rolling_zscore(dio, 12, min_periods=4)).diff().diff().diff()


def f42_pplo_058_inv_yoy_minus_cogs_yoy_d3(cor, inventory):
    return (_yoy_pct(inventory) - _yoy_pct(cor)).diff().diff().diff()


def f42_pplo_059_inv_qoq_minus_cogs_qoq_d3(cor, inventory):
    return (_qoq_pct(inventory) - _qoq_pct(cor)).diff().diff().diff()


def f42_pplo_060_inv_to_rev_slope_8q_d3(revenue, inventory):
    r = _safe_div(inventory, revenue)
    return (_rolling_slope(r, 8, min_periods=3)).diff().diff().diff()


def f42_pplo_061_inv_to_rev_ttm_d3(revenue, inventory):
    return (_safe_div(inventory, _ttm(revenue))).diff().diff().diff()


def f42_pplo_062_inv_to_rev_ttm_yoy_change_d3(revenue, inventory):
    return (_safe_div(inventory, _ttm(revenue)).diff(4)).diff().diff().diff()


def f42_pplo_063_defrev_to_rev_ttm_d3(revenue, deferredrev):
    return (_safe_div(deferredrev, _ttm(revenue))).diff().diff().diff()


def f42_pplo_064_defrev_to_rev_yoy_change_d3(revenue, deferredrev):
    return (_safe_div(deferredrev, _ttm(revenue)).diff(4)).diff().diff().diff()


def f42_pplo_065_defrev_yoy_growth_d3(revenue, deferredrev):
    _ = revenue
    return (_yoy_pct(deferredrev)).diff().diff().diff()


def f42_pplo_066_defrev_growth_minus_rev_growth_yoy_d3(revenue, deferredrev):
    return (_yoy_pct(deferredrev) - _yoy_pct(revenue)).diff().diff().diff()


def f42_pplo_067_gm_minus_sga_share_d3(revenue, gp, sga):
    return (_safe_div(gp, revenue) - _safe_div(sga, revenue)).diff().diff().diff()


def f42_pplo_068_gm_minus_sga_share_yoy_change_d3(revenue, gp, sga):
    s = _safe_div(gp, revenue) - _safe_div(sga, revenue)
    return (s.diff(4)).diff().diff().diff()


def f42_pplo_069_gm_minus_sga_share_zscore_12q_d3(revenue, gp, sga):
    s = _safe_div(gp, revenue) - _safe_div(sga, revenue)
    return (_rolling_zscore(s, 12, min_periods=4)).diff().diff().diff()


def f42_pplo_070_gm_minus_opex_share_d3(revenue, gp, opex):
    return (_safe_div(gp, revenue) - _safe_div(opex, revenue)).diff().diff().diff()


def f42_pplo_071_gm_rolling_skew_8q_d3(revenue, gp):
    return (_safe_div(gp, revenue).rolling(8, min_periods=4).skew()).diff().diff().diff()


def f42_pplo_072_gm_rolling_skew_12q_d3(revenue, gp):
    return (_safe_div(gp, revenue).rolling(12, min_periods=5).skew()).diff().diff().diff()


def f42_pplo_073_gm_rolling_kurt_8q_d3(revenue, gp):
    return (_safe_div(gp, revenue).rolling(8, min_periods=4).kurt()).diff().diff().diff()


def f42_pplo_074_gm_rolling_kurt_12q_d3(revenue, gp):
    return (_safe_div(gp, revenue).rolling(12, min_periods=5).kurt()).diff().diff().diff()


def f42_pplo_075_gm_zscore_8q_d3(revenue, gp):
    return (_rolling_zscore(_safe_div(gp, revenue), 8, min_periods=3)).diff().diff().diff()


# ============================================================
#                        REGISTRY
# ============================================================

PRICING_POWER_LOSS_SIGNAL_D3_REGISTRY_001_075 = {
    "f42_pplo_001_gm_q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_001_gm_q_d3},
    "f42_pplo_002_gm_ttm_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_002_gm_ttm_d3},
    "f42_pplo_003_log_gm_q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_003_log_gm_q_d3},
    "f42_pplo_004_log_gm_ttm_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_004_log_gm_ttm_d3},
    "f42_pplo_005_gm_q_minus_gm_4q_mean_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_005_gm_q_minus_gm_4q_mean_d3},
    "f42_pplo_006_gm_q_minus_gm_12q_mean_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_006_gm_q_minus_gm_12q_mean_d3},
    "f42_pplo_007_gm_q_minus_gm_8q_mean_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_007_gm_q_minus_gm_8q_mean_d3},
    "f42_pplo_008_one_minus_gm_q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_008_one_minus_gm_q_d3},
    "f42_pplo_009_gm_ttm_compression_4q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_009_gm_ttm_compression_4q_d3},
    "f42_pplo_010_gm_ttm_compression_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_010_gm_ttm_compression_8q_d3},
    "f42_pplo_011_gm_ttm_compression_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_011_gm_ttm_compression_12q_d3},
    "f42_pplo_012_gm_ttm_compression_pct_4q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_012_gm_ttm_compression_pct_4q_d3},
    "f42_pplo_013_gm_ttm_minus_4q_max_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_013_gm_ttm_minus_4q_max_d3},
    "f42_pplo_014_gm_ttm_minus_12q_max_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_014_gm_ttm_minus_12q_max_d3},
    "f42_pplo_015_cogs_growth_q_minus_rev_growth_q_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_015_cogs_growth_q_minus_rev_growth_q_d3},
    "f42_pplo_016_cogs_growth_yoy_minus_rev_growth_yoy_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_016_cogs_growth_yoy_minus_rev_growth_yoy_d3},
    "f42_pplo_017_cogs_growth_2y_minus_rev_growth_2y_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_017_cogs_growth_2y_minus_rev_growth_2y_d3},
    "f42_pplo_018_cogs_yoy_growth_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_018_cogs_yoy_growth_d3},
    "f42_pplo_019_rev_growth_yoy_minus_4q_cogs_growth_mean_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_019_rev_growth_yoy_minus_4q_cogs_growth_mean_d3},
    "f42_pplo_020_cogs_to_rev_growth_ratio_yoy_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_020_cogs_to_rev_growth_ratio_yoy_d3},
    "f42_pplo_021_gp_yoy_minus_rev_yoy_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_021_gp_yoy_minus_rev_yoy_d3},
    "f42_pplo_022_gp_qoq_minus_rev_qoq_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_022_gp_qoq_minus_rev_qoq_d3},
    "f42_pplo_023_gp_2y_minus_rev_2y_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_023_gp_2y_minus_rev_2y_d3},
    "f42_pplo_024_gp_ttm_yoy_minus_rev_ttm_yoy_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_024_gp_ttm_yoy_minus_rev_ttm_yoy_d3},
    "f42_pplo_025_rev_per_inventory_d3": {"inputs": ["revenue", "inventory"], "func": f42_pplo_025_rev_per_inventory_d3},
    "f42_pplo_026_rev_per_inventory_yoy_change_d3": {"inputs": ["revenue", "inventory"], "func": f42_pplo_026_rev_per_inventory_yoy_change_d3},
    "f42_pplo_027_value_capture_share_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_027_value_capture_share_d3},
    "f42_pplo_028_value_capture_share_qoq_change_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_028_value_capture_share_qoq_change_d3},
    "f42_pplo_029_value_capture_share_yoy_change_d3": {"inputs": ["revenue", "cor"], "func": f42_pplo_029_value_capture_share_yoy_change_d3},
    "f42_pplo_030_inventory_turnover_yoy_change_d3": {"inputs": ["cor", "inventory"], "func": f42_pplo_030_inventory_turnover_yoy_change_d3},
    "f42_pplo_031_dupont_gm_x_at_q_d3": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_031_dupont_gm_x_at_q_d3},
    "f42_pplo_032_dupont_gm_x_at_ttm_d3": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_032_dupont_gm_x_at_ttm_d3},
    "f42_pplo_033_dupont_gm_x_at_yoy_change_d3": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_033_dupont_gm_x_at_yoy_change_d3},
    "f42_pplo_034_dupont_gm_x_at_2y_change_d3": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_034_dupont_gm_x_at_2y_change_d3},
    "f42_pplo_035_dupont_gm_x_at_log_d3": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_035_dupont_gm_x_at_log_d3},
    "f42_pplo_036_dupont_gm_x_at_zscore_12q_d3": {"inputs": ["revenue", "gp", "assets"], "func": f42_pplo_036_dupont_gm_x_at_zscore_12q_d3},
    "f42_pplo_037_gm_std_4q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_037_gm_std_4q_d3},
    "f42_pplo_038_gm_std_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_038_gm_std_8q_d3},
    "f42_pplo_039_gm_std_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_039_gm_std_12q_d3},
    "f42_pplo_040_gm_cv_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_040_gm_cv_8q_d3},
    "f42_pplo_041_rev_change_minus_ar_change_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_041_rev_change_minus_ar_change_d3},
    "f42_pplo_042_delta_rev_div_delta_ar_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_042_delta_rev_div_delta_ar_d3},
    "f42_pplo_043_delta_rev_div_delta_ar_yoy_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_043_delta_rev_div_delta_ar_yoy_d3},
    "f42_pplo_044_rev_div_lagged_ar_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_044_rev_div_lagged_ar_d3},
    "f42_pplo_045_rev_yoy_minus_ar_yoy_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_045_rev_yoy_minus_ar_yoy_d3},
    "f42_pplo_046_discount_intensity_proxy_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_046_discount_intensity_proxy_d3},
    "f42_pplo_047_ar_yoy_minus_rev_yoy_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_047_ar_yoy_minus_rev_yoy_d3},
    "f42_pplo_048_ar_qoq_minus_rev_qoq_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_048_ar_qoq_minus_rev_qoq_d3},
    "f42_pplo_049_ar_to_rev_slope_8q_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_049_ar_to_rev_slope_8q_d3},
    "f42_pplo_050_ar_to_rev_ttm_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_050_ar_to_rev_ttm_d3},
    "f42_pplo_051_ar_to_rev_ttm_yoy_change_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_051_ar_to_rev_ttm_yoy_change_d3},
    "f42_pplo_052_dso_q_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_052_dso_q_d3},
    "f42_pplo_053_dso_yoy_change_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_053_dso_yoy_change_d3},
    "f42_pplo_054_dso_zscore_12q_d3": {"inputs": ["revenue", "receivables"], "func": f42_pplo_054_dso_zscore_12q_d3},
    "f42_pplo_055_dio_q_d3": {"inputs": ["cor", "inventory"], "func": f42_pplo_055_dio_q_d3},
    "f42_pplo_056_dio_yoy_change_d3": {"inputs": ["cor", "inventory"], "func": f42_pplo_056_dio_yoy_change_d3},
    "f42_pplo_057_dio_zscore_12q_d3": {"inputs": ["cor", "inventory"], "func": f42_pplo_057_dio_zscore_12q_d3},
    "f42_pplo_058_inv_yoy_minus_cogs_yoy_d3": {"inputs": ["cor", "inventory"], "func": f42_pplo_058_inv_yoy_minus_cogs_yoy_d3},
    "f42_pplo_059_inv_qoq_minus_cogs_qoq_d3": {"inputs": ["cor", "inventory"], "func": f42_pplo_059_inv_qoq_minus_cogs_qoq_d3},
    "f42_pplo_060_inv_to_rev_slope_8q_d3": {"inputs": ["revenue", "inventory"], "func": f42_pplo_060_inv_to_rev_slope_8q_d3},
    "f42_pplo_061_inv_to_rev_ttm_d3": {"inputs": ["revenue", "inventory"], "func": f42_pplo_061_inv_to_rev_ttm_d3},
    "f42_pplo_062_inv_to_rev_ttm_yoy_change_d3": {"inputs": ["revenue", "inventory"], "func": f42_pplo_062_inv_to_rev_ttm_yoy_change_d3},
    "f42_pplo_063_defrev_to_rev_ttm_d3": {"inputs": ["revenue", "deferredrev"], "func": f42_pplo_063_defrev_to_rev_ttm_d3},
    "f42_pplo_064_defrev_to_rev_yoy_change_d3": {"inputs": ["revenue", "deferredrev"], "func": f42_pplo_064_defrev_to_rev_yoy_change_d3},
    "f42_pplo_065_defrev_yoy_growth_d3": {"inputs": ["revenue", "deferredrev"], "func": f42_pplo_065_defrev_yoy_growth_d3},
    "f42_pplo_066_defrev_growth_minus_rev_growth_yoy_d3": {"inputs": ["revenue", "deferredrev"], "func": f42_pplo_066_defrev_growth_minus_rev_growth_yoy_d3},
    "f42_pplo_067_gm_minus_sga_share_d3": {"inputs": ["revenue", "gp", "sga"], "func": f42_pplo_067_gm_minus_sga_share_d3},
    "f42_pplo_068_gm_minus_sga_share_yoy_change_d3": {"inputs": ["revenue", "gp", "sga"], "func": f42_pplo_068_gm_minus_sga_share_yoy_change_d3},
    "f42_pplo_069_gm_minus_sga_share_zscore_12q_d3": {"inputs": ["revenue", "gp", "sga"], "func": f42_pplo_069_gm_minus_sga_share_zscore_12q_d3},
    "f42_pplo_070_gm_minus_opex_share_d3": {"inputs": ["revenue", "gp", "opex"], "func": f42_pplo_070_gm_minus_opex_share_d3},
    "f42_pplo_071_gm_rolling_skew_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_071_gm_rolling_skew_8q_d3},
    "f42_pplo_072_gm_rolling_skew_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_072_gm_rolling_skew_12q_d3},
    "f42_pplo_073_gm_rolling_kurt_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_073_gm_rolling_kurt_8q_d3},
    "f42_pplo_074_gm_rolling_kurt_12q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_074_gm_rolling_kurt_12q_d3},
    "f42_pplo_075_gm_zscore_8q_d3": {"inputs": ["revenue", "gp"], "func": f42_pplo_075_gm_zscore_8q_d3},
}
