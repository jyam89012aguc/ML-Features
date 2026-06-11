"""volatility_regime_at_peak d3 features 076_150 — short blowup pipeline 1a-inverse.

Volatility regime characterization at multi-year peaks: percentile rank, clustering, asymmetry, jumps, term structure, conditional vol, tail vol.
PIT-clean: right-anchored rolling, explicit min_periods, no centered windows.
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


def _rolling_pctrank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    return s.rolling(window, min_periods=min_periods).rank(pct=True)


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


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


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()


def _wilder_rma(s, n):
    return s.ewm(alpha=1.0 / n, adjust=False, min_periods=max(n // 3, 2)).mean()



def _log_ret(close):
    return _safe_log(close).diff()


def _realized_vol(close, n):
    return _log_ret(close).rolling(n, min_periods=max(n // 3, 2)).std() * np.sqrt(YDAYS)


def _parkinson(high, low, n):
    rs = (np.log(high / low.replace(0, np.nan)) ** 2) / (4.0 * np.log(2.0))
    return np.sqrt(rs.rolling(n, min_periods=max(n // 3, 2)).mean() * YDAYS)


def _gk(open_, high, low, close, n):
    hl = 0.5 * (np.log(high / low.replace(0, np.nan)) ** 2)
    co = (2.0 * np.log(2.0) - 1.0) * (np.log(close / open_.replace(0, np.nan)) ** 2)
    return np.sqrt((hl - co).rolling(n, min_periods=max(n // 3, 2)).mean() * YDAYS)


def _rs(open_, high, low, close, n):
    rs = (np.log(high / close.replace(0, np.nan)) * np.log(high / open_.replace(0, np.nan))
          + np.log(low / close.replace(0, np.nan)) * np.log(low / open_.replace(0, np.nan)))
    return np.sqrt(rs.rolling(n, min_periods=max(n // 3, 2)).mean() * YDAYS)


def _yang_zhang(open_, high, low, close, n):
    log_oc = np.log(open_ / close.shift(1).replace(0, np.nan))
    log_co = np.log(close / open_.replace(0, np.nan))
    log_hc = np.log(high / close.replace(0, np.nan))
    log_ho = np.log(high / open_.replace(0, np.nan))
    log_lc = np.log(low / close.replace(0, np.nan))
    log_lo = np.log(low / open_.replace(0, np.nan))
    overnight = log_oc.rolling(n, min_periods=max(n // 3, 2)).var()
    open_to_close = log_co.rolling(n, min_periods=max(n // 3, 2)).var()
    rs = (log_hc * log_ho + log_lc * log_lo).rolling(n, min_periods=max(n // 3, 2)).mean()
    k = 0.34 / (1.34 + (n + 1) / (n - 1))
    return np.sqrt((overnight + k * open_to_close + (1 - k) * rs) * YDAYS)


def _semi_var(close, n, side="down"):
    r = _log_ret(close)
    if side == "down":
        r = r.where(r < 0, 0)
    else:
        r = r.where(r > 0, 0)
    return r.pow(2).rolling(n, min_periods=max(n // 3, 2)).mean() * YDAYS


def _quarticity(close, n):
    return _log_ret(close).pow(4).rolling(n, min_periods=max(n // 3, 2)).sum() * (n / 3.0)


def _bipower_var(close, n):
    r = _log_ret(close).abs()
    bp = r * r.shift(1)
    return (np.pi / 2) * bp.rolling(n, min_periods=max(n // 3, 2)).sum() * (YDAYS / n)


def _realized_var(close, n):
    r = _log_ret(close)
    return r.pow(2).rolling(n, min_periods=max(n // 3, 2)).sum() * (YDAYS / n)


def _jump_var(close, n):
    return (_realized_var(close, n) - _bipower_var(close, n)).clip(lower=0)


def _ema(s, span):
    return s.ewm(span=span, adjust=False, min_periods=max(span // 3, 2)).mean()

# ============================================================
#                    D3 FEATURES 076-150
# ============================================================

def f10_vrap_076_yz_to_realized_ratio_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_safe_div(_yang_zhang(open, high, low, close, QDAYS), _realized_vol(close, QDAYS))).diff().diff().diff()


def f10_vrap_077_rs_252_value_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rs(open, high, low, close, YDAYS)).diff().diff().diff()


def f10_vrap_078_max_tr_pctrank_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_true_range(high, low, close), YDAYS)).diff().diff().diff()


def f10_vrap_079_intraday_overnight_corr_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    on = np.log(open / close.shift(1).replace(0, np.nan))
    intr = np.log(close / open.replace(0, np.nan))
    return (on.rolling(QDAYS, min_periods=MDAYS).corr(intr)).diff().diff().diff()


def f10_vrap_080_range_skew_distribution_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (((high - low) / close).rolling(QDAYS, min_periods=MDAYS).skew()).diff().diff().diff()


def f10_vrap_081_realized_quarticity_63d_d3(close: pd.Series) -> pd.Series:
    return (_quarticity(close, QDAYS)).diff().diff().diff()


def f10_vrap_082_bipower_var_63d_d3(close: pd.Series) -> pd.Series:
    return (_bipower_var(close, QDAYS)).diff().diff().diff()


def f10_vrap_083_jump_var_63d_d3(close: pd.Series) -> pd.Series:
    return (_jump_var(close, QDAYS)).diff().diff().diff()


def f10_vrap_084_jump_to_realized_ratio_63d_d3(close: pd.Series) -> pd.Series:
    return (_safe_div(_jump_var(close, QDAYS), _realized_var(close, QDAYS))).diff().diff().diff()


def f10_vrap_085_jump_var_252d_d3(close: pd.Series) -> pd.Series:
    return (_jump_var(close, YDAYS)).diff().diff().diff()


def f10_vrap_086_count_abs_ret_gt_3sigma_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r.abs() > 3 * sd).astype(float)
    return (cnt.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f10_vrap_087_count_abs_ret_gt_4sigma_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r.abs() > 4 * sd).astype(float)
    return (cnt.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f10_vrap_088_count_abs_ret_gt_5sigma_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r.abs() > 5 * sd).astype(float)
    return (cnt.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f10_vrap_089_largest_abs_ret_63d_d3(close: pd.Series) -> pd.Series:
    return (_log_ret(close).abs().rolling(QDAYS, min_periods=MDAYS).max()).diff().diff().diff()


def f10_vrap_090_largest_abs_ret_252d_pctrank_1260d_d3(close: pd.Series) -> pd.Series:
    mx = _log_ret(close).abs().rolling(YDAYS, min_periods=QDAYS).max()
    return (_rolling_pctrank(mx, 1260)).diff().diff().diff()


def f10_vrap_091_jump_clustering_lag1_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j = (r.abs() > 3 * sd).astype(float)
    return (j.rolling(YDAYS, min_periods=QDAYS).corr(j.shift(1))).diff().diff().diff()


def f10_vrap_092_jump_skewness_63d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    masked = r.where(r.abs() > 2 * sd, np.nan)
    return (masked.rolling(QDAYS, min_periods=MDAYS).skew()).diff().diff().diff()


def f10_vrap_093_jump_to_continuous_ratio_252d_d3(close: pd.Series) -> pd.Series:
    return (_safe_div(_jump_var(close, YDAYS), _bipower_var(close, YDAYS))).diff().diff().diff()


def f10_vrap_094_negative_jump_count_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r < -3 * sd).astype(float)
    return (cnt.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f10_vrap_095_positive_jump_count_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r > 3 * sd).astype(float)
    return (cnt.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f10_vrap_096_quarticity_zscore_252d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_zscore(_quarticity(close, QDAYS), YDAYS)).diff().diff().diff()


def f10_vrap_097_signed_jump_var_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j_pos = r.where(r > 3 * sd, 0).pow(2).rolling(YDAYS, min_periods=QDAYS).sum()
    j_neg = r.where(r < -3 * sd, 0).pow(2).rolling(YDAYS, min_periods=QDAYS).sum()
    return (j_pos - j_neg).diff().diff().diff()


def f10_vrap_098_largest_neg_ret_minus_largest_pos_ret_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    return ((-r.rolling(YDAYS, min_periods=QDAYS).min()) - r.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff().diff()


def f10_vrap_099_jump_size_avg_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j = r.abs().where(r.abs() > 3 * sd, np.nan)
    return (j.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f10_vrap_100_max_jump_size_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j = r.abs().where(r.abs() > 3 * sd, np.nan)
    return (j.rolling(YDAYS, min_periods=QDAYS).max()).diff().diff().diff()


def f10_vrap_101_vol_of_vol_21d_realized_pctrank_504d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(MDAYS, min_periods=5).std()
    return (_rolling_pctrank(vov, 504)).diff().diff().diff()


def f10_vrap_102_vol_of_vol_252d_expansion_velocity_21d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(YDAYS, min_periods=QDAYS).std()
    return (vov.diff(MDAYS)).diff().diff().diff()


def f10_vrap_103_vov_regime_above_75pct_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    q75 = vov.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return ((vov > q75).astype(float)).diff().diff().diff()


def f10_vrap_104_realized_vol_2nd_deriv_streak_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    acc = rv.diff().diff()
    pos = (acc > 0).astype(int)
    grp = (pos.diff().ne(0)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    return (streak.rolling(QDAYS, min_periods=MDAYS).max().astype(float)).diff().diff().diff()


def f10_vrap_105_vol_acceleration_zscore_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (_rolling_zscore(rv.diff().diff(), YDAYS)).diff().diff().diff()


def f10_vrap_106_vol_persistence_index_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    lag = rv.shift(1)
    cov = (rv * lag).rolling(QDAYS, min_periods=MDAYS).mean() - rv.rolling(QDAYS, min_periods=MDAYS).mean() * lag.rolling(QDAYS, min_periods=MDAYS).mean()
    var = lag.rolling(QDAYS, min_periods=MDAYS).var()
    return (_safe_div(cov, var)).diff().diff().diff()


def f10_vrap_107_vol_range_max_minus_min_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv.rolling(YDAYS, min_periods=QDAYS).max() - rv.rolling(YDAYS, min_periods=QDAYS).min()).diff().diff().diff()


def f10_vrap_108_vol_max_over_min_ratio_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (_safe_div(rv.rolling(YDAYS, min_periods=QDAYS).max(), rv.rolling(YDAYS, min_periods=QDAYS).min())).diff().diff().diff()


def f10_vrap_109_vol_curvature_d2_zscore_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (_rolling_zscore(_ema(rv, 5).diff().diff(), YDAYS)).diff().diff().diff()


def f10_vrap_110_vov_to_vol_ratio_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    return (_safe_div(vov, rv.rolling(YDAYS, min_periods=QDAYS).mean())).diff().diff().diff()


def f10_vrap_111_max_rvol_in_63d_minus_current_rvol_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv.rolling(QDAYS, min_periods=MDAYS).max() - rv).diff().diff().diff()


def f10_vrap_112_min_rvol_in_63d_minus_current_rvol_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv - rv.rolling(QDAYS, min_periods=MDAYS).min()).diff().diff().diff()


def f10_vrap_113_vov_streak_above_median_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    med = vov.rolling(QDAYS, min_periods=MDAYS).median()
    above = (vov > med).astype(int)
    grp = (above.diff().ne(0)).cumsum()
    streak = above.groupby(grp).cumsum() * above
    return (streak.rolling(QDAYS, min_periods=MDAYS).max().astype(float)).diff().diff().diff()


def f10_vrap_114_vol_diff_zscore_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (_rolling_zscore(rv.diff(), QDAYS)).diff().diff().diff()


def f10_vrap_115_vol_change_sign_persistence_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    s = np.sign(rv.diff().fillna(0))
    return (s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(1))).diff().diff().diff()


def f10_vrap_116_max_d_vol_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv.diff().abs().rolling(YDAYS, min_periods=QDAYS).max()).diff().diff().diff()


def f10_vrap_117_vov_pctrank_1260d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    return (_rolling_pctrank(vov, 1260)).diff().diff().diff()


def f10_vrap_118_vol_dispersion_index_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (_safe_div(rv.rolling(YDAYS, min_periods=QDAYS).std(), rv.rolling(YDAYS, min_periods=QDAYS).mean())).diff().diff().diff()


def f10_vrap_119_vol_iqr_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    q75 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q25 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return (q75 - q25).diff().diff().diff()


def f10_vrap_120_vol_kurtosis_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv.rolling(YDAYS, min_periods=QDAYS).kurt()).diff().diff().diff()


def f10_vrap_121_vol_term_structure_slope_21_252_d3(close: pd.Series) -> pd.Series:
    rv21 = _realized_vol(close, MDAYS)
    rv252 = _realized_vol(close, YDAYS)
    return (_safe_log(rv21) - _safe_log(rv252)).diff().diff().diff()


def f10_vrap_122_vol_term_structure_slope_21_63_d3(close: pd.Series) -> pd.Series:
    rv21 = _realized_vol(close, MDAYS)
    rv63 = _realized_vol(close, QDAYS)
    return (_safe_log(rv21) - _safe_log(rv63)).diff().diff().diff()


def f10_vrap_123_vol_term_structure_curvature_21_63_252_d3(close: pd.Series) -> pd.Series:
    rv21 = _realized_vol(close, MDAYS)
    rv63 = _realized_vol(close, QDAYS)
    rv252 = _realized_vol(close, YDAYS)
    return (2 * _safe_log(rv63) - _safe_log(rv21) - _safe_log(rv252)).diff().diff().diff()


def f10_vrap_124_vol_term_structure_level_avg_3point_d3(close: pd.Series) -> pd.Series:
    rv21 = _realized_vol(close, MDAYS)
    rv63 = _realized_vol(close, QDAYS)
    rv252 = _realized_vol(close, YDAYS)
    return ((_safe_log(rv21) + _safe_log(rv63) + _safe_log(rv252)) / 3.0).diff().diff().diff()


def f10_vrap_125_vol_term_structure_slope_zscore_504d_d3(close: pd.Series) -> pd.Series:
    slope = _safe_log(_realized_vol(close, MDAYS)) - _safe_log(_realized_vol(close, YDAYS))
    return (_rolling_zscore(slope, 504)).diff().diff().diff()


def f10_vrap_126_tail_vol_5pct_abs_ret_63d_d3(close: pd.Series) -> pd.Series:
    return (_log_ret(close).abs().rolling(QDAYS, min_periods=MDAYS).quantile(0.05)).diff().diff().diff()


def f10_vrap_127_tail_vol_95pct_abs_ret_63d_d3(close: pd.Series) -> pd.Series:
    return (_log_ret(close).abs().rolling(QDAYS, min_periods=MDAYS).quantile(0.95)).diff().diff().diff()


def f10_vrap_128_tail_vol_99pct_abs_ret_252d_d3(close: pd.Series) -> pd.Series:
    return (_log_ret(close).abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.99)).diff().diff().diff()


def f10_vrap_129_extreme_tail_concentration_ratio_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close).abs()
    def _conc(w):
        v = w[~np.isnan(w)]
        if len(v) < 30:
            return np.nan
        k = max(int(len(v) * 0.05), 1)
        top = np.sort(v)[-k:].sum()
        tot = v.sum()
        return float(top / tot) if tot > 0 else np.nan
    return (r.rolling(YDAYS, min_periods=QDAYS).apply(_conc, raw=True)).diff().diff().diff()


def f10_vrap_130_conditional_vol_given_dd_5pct_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    dd = (close / close.rolling(MDAYS, min_periods=5).max()) - 1
    cond = dd <= -0.05
    masked = r.where(cond, np.nan)
    return (masked.rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(YDAYS)).diff().diff().diff()


def f10_vrap_131_conditional_vol_given_dd_10pct_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    dd = (close / close.rolling(MDAYS, min_periods=5).max()) - 1
    cond = dd <= -0.10
    masked = r.where(cond, np.nan)
    return (masked.rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(YDAYS)).diff().diff().diff()


def f10_vrap_132_conditional_vol_given_new_high_252d_d3(close: pd.Series) -> pd.Series:
    hh = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    r = _log_ret(close).abs()
    masked = r.where(hh, np.nan)
    return (masked.rolling(YDAYS, min_periods=QDAYS).std()).diff().diff().diff()


def f10_vrap_133_max_drawdown_conditional_vol_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    dd = (close / close.rolling(YDAYS, min_periods=QDAYS).max()) - 1
    dd_max = dd.rolling(YDAYS, min_periods=QDAYS).min()
    cond = dd <= dd_max + 1e-12
    return (rv.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f10_vrap_134_vol_during_uptrend_minus_downtrend_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    s50 = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    s200 = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    up = rv.where(s50 > s200, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = rv.where(s50 <= s200, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (up - dn).diff().diff().diff()


def f10_vrap_135_vol_flatness_index_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    rng = rv.rolling(YDAYS, min_periods=QDAYS).max() - rv.rolling(YDAYS, min_periods=QDAYS).min()
    return (1.0 - _safe_div(rng, rv.rolling(YDAYS, min_periods=QDAYS).mean())).diff().diff().diff()


def f10_vrap_136_vol_shape_entropy_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    def _h(w):
        v = w[~np.isnan(w)]
        if len(v) < 20:
            return np.nan
        bins = np.histogram(v, bins=5)[0].astype(float)
        s = bins.sum()
        if s == 0:
            return np.nan
        p = bins / s
        p = p[p > 0]
        return float(-(p * np.log(p)).sum()) if len(p) else np.nan
    return (rv.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)).diff().diff().diff()


def f10_vrap_137_realized_var_to_quarticity_ratio_252d_d3(close: pd.Series) -> pd.Series:
    return (_safe_div(_realized_var(close, YDAYS), np.sqrt(_quarticity(close, YDAYS) * 3))).diff().diff().diff()


def f10_vrap_138_vol_pctrank_minus_trend_pctrank_504d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    mom = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (_rolling_pctrank(rv, 504) - _rolling_pctrank(mom, 504)).diff().diff().diff()


def f10_vrap_139_low_vol_with_high_trend_composite_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    mom = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return ((1.0 - _rolling_pctrank(rv, YDAYS)) + _rolling_pctrank(mom, YDAYS)).diff().diff().diff()


def f10_vrap_140_vol_term_structure_inversion_count_252d_d3(close: pd.Series) -> pd.Series:
    rv21 = _realized_vol(close, MDAYS)
    rv252 = _realized_vol(close, YDAYS)
    inv = (rv21 > rv252).astype(float)
    return (inv.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f10_vrap_141_vol_term_structure_inversion_streak_252d_d3(close: pd.Series) -> pd.Series:
    rv21 = _realized_vol(close, MDAYS)
    rv252 = _realized_vol(close, YDAYS)
    inv = (rv21 > rv252).astype(int)
    grp = (inv.diff().ne(0)).cumsum()
    streak = inv.groupby(grp).cumsum() * inv
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff().diff().diff()


def f10_vrap_142_neg_tail_es_5pct_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    q05 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    masked = r.where(r <= q05, np.nan)
    return (masked.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f10_vrap_143_pos_tail_es_95pct_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    q95 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    masked = r.where(r >= q95, np.nan)
    return (masked.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f10_vrap_144_vol_change_to_return_corr_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv.diff().rolling(YDAYS, min_periods=QDAYS).corr(_log_ret(close))).diff().diff().diff()


def f10_vrap_145_realized_skew_252d_d3(close: pd.Series) -> pd.Series:
    return (_log_ret(close).rolling(YDAYS, min_periods=QDAYS).skew()).diff().diff().diff()


def f10_vrap_146_realized_kurt_252d_d3(close: pd.Series) -> pd.Series:
    return (_log_ret(close).rolling(YDAYS, min_periods=QDAYS).kurt()).diff().diff().diff()


def f10_vrap_147_tail_ratio_99_1_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close).abs()
    q99 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    q01 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.01).replace(0, np.nan)
    return (_safe_div(q99, q01)).diff().diff().diff()


def f10_vrap_148_composite_regime_score_vol_clustering_asym_d3(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    p1 = _rolling_pctrank(_realized_vol(close, YDAYS), 1260)
    s = _log_ret(close).pow(2)
    ac = s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(1))
    a = _safe_div(_semi_var(close, YDAYS, 'down'), _semi_var(close, YDAYS, 'up'))
    return (_rolling_zscore(p1, YDAYS) + _rolling_zscore(ac, YDAYS) + _rolling_zscore(a, YDAYS)).diff().diff().diff()


def f10_vrap_149_composite_jump_persistence_score_252d_d3(close: pd.Series) -> pd.Series:
    jv = _jump_var(close, YDAYS)
    r = _log_ret(close); sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j = (r.abs() > 3 * sd).astype(float)
    jc = j.rolling(YDAYS, min_periods=QDAYS).corr(j.shift(1))
    q = _quarticity(close, YDAYS)
    return (_rolling_zscore(jv, YDAYS) + _rolling_zscore(jc, YDAYS) + _rolling_zscore(q, YDAYS)).diff().diff().diff()


def f10_vrap_150_composite_vol_fragility_aggregate_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    p1 = _rolling_pctrank(_realized_vol(close, YDAYS), 1260)
    rv = _realized_vol(close, MDAYS); vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    p2 = _rolling_pctrank(vov, 504)
    p3 = _safe_div(_yang_zhang(open, high, low, close, QDAYS), _realized_vol(close, QDAYS))
    inv = (rv > _realized_vol(close, YDAYS)).astype(int)
    grp = (inv.diff().ne(0)).cumsum()
    streak = inv.groupby(grp).cumsum() * inv
    sk = streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)
    return (_rolling_zscore(p1, YDAYS) + _rolling_zscore(p2, YDAYS) + _rolling_zscore(p3, YDAYS) + _rolling_zscore(sk, YDAYS)).diff().diff().diff()


VOLATILITY_REGIME_AT_PEAK_D3_REGISTRY_076_150 = {
    "f10_vrap_076_yz_to_realized_ratio_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_076_yz_to_realized_ratio_63d_d3},
    "f10_vrap_077_rs_252_value_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_077_rs_252_value_d3},
    "f10_vrap_078_max_tr_pctrank_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_078_max_tr_pctrank_252d_d3},
    "f10_vrap_079_intraday_overnight_corr_63d_d3": {"inputs": ["open", "close"], "func": f10_vrap_079_intraday_overnight_corr_63d_d3},
    "f10_vrap_080_range_skew_distribution_63d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_080_range_skew_distribution_63d_d3},
    "f10_vrap_081_realized_quarticity_63d_d3": {"inputs": ["close"], "func": f10_vrap_081_realized_quarticity_63d_d3},
    "f10_vrap_082_bipower_var_63d_d3": {"inputs": ["close"], "func": f10_vrap_082_bipower_var_63d_d3},
    "f10_vrap_083_jump_var_63d_d3": {"inputs": ["close"], "func": f10_vrap_083_jump_var_63d_d3},
    "f10_vrap_084_jump_to_realized_ratio_63d_d3": {"inputs": ["close"], "func": f10_vrap_084_jump_to_realized_ratio_63d_d3},
    "f10_vrap_085_jump_var_252d_d3": {"inputs": ["close"], "func": f10_vrap_085_jump_var_252d_d3},
    "f10_vrap_086_count_abs_ret_gt_3sigma_252d_d3": {"inputs": ["close"], "func": f10_vrap_086_count_abs_ret_gt_3sigma_252d_d3},
    "f10_vrap_087_count_abs_ret_gt_4sigma_252d_d3": {"inputs": ["close"], "func": f10_vrap_087_count_abs_ret_gt_4sigma_252d_d3},
    "f10_vrap_088_count_abs_ret_gt_5sigma_252d_d3": {"inputs": ["close"], "func": f10_vrap_088_count_abs_ret_gt_5sigma_252d_d3},
    "f10_vrap_089_largest_abs_ret_63d_d3": {"inputs": ["close"], "func": f10_vrap_089_largest_abs_ret_63d_d3},
    "f10_vrap_090_largest_abs_ret_252d_pctrank_1260d_d3": {"inputs": ["close"], "func": f10_vrap_090_largest_abs_ret_252d_pctrank_1260d_d3},
    "f10_vrap_091_jump_clustering_lag1_252d_d3": {"inputs": ["close"], "func": f10_vrap_091_jump_clustering_lag1_252d_d3},
    "f10_vrap_092_jump_skewness_63d_d3": {"inputs": ["close"], "func": f10_vrap_092_jump_skewness_63d_d3},
    "f10_vrap_093_jump_to_continuous_ratio_252d_d3": {"inputs": ["close"], "func": f10_vrap_093_jump_to_continuous_ratio_252d_d3},
    "f10_vrap_094_negative_jump_count_252d_d3": {"inputs": ["close"], "func": f10_vrap_094_negative_jump_count_252d_d3},
    "f10_vrap_095_positive_jump_count_252d_d3": {"inputs": ["close"], "func": f10_vrap_095_positive_jump_count_252d_d3},
    "f10_vrap_096_quarticity_zscore_252d_d3": {"inputs": ["close"], "func": f10_vrap_096_quarticity_zscore_252d_d3},
    "f10_vrap_097_signed_jump_var_252d_d3": {"inputs": ["close"], "func": f10_vrap_097_signed_jump_var_252d_d3},
    "f10_vrap_098_largest_neg_ret_minus_largest_pos_ret_252d_d3": {"inputs": ["close"], "func": f10_vrap_098_largest_neg_ret_minus_largest_pos_ret_252d_d3},
    "f10_vrap_099_jump_size_avg_252d_d3": {"inputs": ["close"], "func": f10_vrap_099_jump_size_avg_252d_d3},
    "f10_vrap_100_max_jump_size_252d_d3": {"inputs": ["close"], "func": f10_vrap_100_max_jump_size_252d_d3},
    "f10_vrap_101_vol_of_vol_21d_realized_pctrank_504d_d3": {"inputs": ["close"], "func": f10_vrap_101_vol_of_vol_21d_realized_pctrank_504d_d3},
    "f10_vrap_102_vol_of_vol_252d_expansion_velocity_21d_d3": {"inputs": ["close"], "func": f10_vrap_102_vol_of_vol_252d_expansion_velocity_21d_d3},
    "f10_vrap_103_vov_regime_above_75pct_252d_d3": {"inputs": ["close"], "func": f10_vrap_103_vov_regime_above_75pct_252d_d3},
    "f10_vrap_104_realized_vol_2nd_deriv_streak_63d_d3": {"inputs": ["close"], "func": f10_vrap_104_realized_vol_2nd_deriv_streak_63d_d3},
    "f10_vrap_105_vol_acceleration_zscore_252d_d3": {"inputs": ["close"], "func": f10_vrap_105_vol_acceleration_zscore_252d_d3},
    "f10_vrap_106_vol_persistence_index_63d_d3": {"inputs": ["close"], "func": f10_vrap_106_vol_persistence_index_63d_d3},
    "f10_vrap_107_vol_range_max_minus_min_252d_d3": {"inputs": ["close"], "func": f10_vrap_107_vol_range_max_minus_min_252d_d3},
    "f10_vrap_108_vol_max_over_min_ratio_252d_d3": {"inputs": ["close"], "func": f10_vrap_108_vol_max_over_min_ratio_252d_d3},
    "f10_vrap_109_vol_curvature_d2_zscore_252d_d3": {"inputs": ["close"], "func": f10_vrap_109_vol_curvature_d2_zscore_252d_d3},
    "f10_vrap_110_vov_to_vol_ratio_252d_d3": {"inputs": ["close"], "func": f10_vrap_110_vov_to_vol_ratio_252d_d3},
    "f10_vrap_111_max_rvol_in_63d_minus_current_rvol_d3": {"inputs": ["close"], "func": f10_vrap_111_max_rvol_in_63d_minus_current_rvol_d3},
    "f10_vrap_112_min_rvol_in_63d_minus_current_rvol_d3": {"inputs": ["close"], "func": f10_vrap_112_min_rvol_in_63d_minus_current_rvol_d3},
    "f10_vrap_113_vov_streak_above_median_63d_d3": {"inputs": ["close"], "func": f10_vrap_113_vov_streak_above_median_63d_d3},
    "f10_vrap_114_vol_diff_zscore_63d_d3": {"inputs": ["close"], "func": f10_vrap_114_vol_diff_zscore_63d_d3},
    "f10_vrap_115_vol_change_sign_persistence_63d_d3": {"inputs": ["close"], "func": f10_vrap_115_vol_change_sign_persistence_63d_d3},
    "f10_vrap_116_max_d_vol_252d_d3": {"inputs": ["close"], "func": f10_vrap_116_max_d_vol_252d_d3},
    "f10_vrap_117_vov_pctrank_1260d_d3": {"inputs": ["close"], "func": f10_vrap_117_vov_pctrank_1260d_d3},
    "f10_vrap_118_vol_dispersion_index_252d_d3": {"inputs": ["close"], "func": f10_vrap_118_vol_dispersion_index_252d_d3},
    "f10_vrap_119_vol_iqr_252d_d3": {"inputs": ["close"], "func": f10_vrap_119_vol_iqr_252d_d3},
    "f10_vrap_120_vol_kurtosis_252d_d3": {"inputs": ["close"], "func": f10_vrap_120_vol_kurtosis_252d_d3},
    "f10_vrap_121_vol_term_structure_slope_21_252_d3": {"inputs": ["close"], "func": f10_vrap_121_vol_term_structure_slope_21_252_d3},
    "f10_vrap_122_vol_term_structure_slope_21_63_d3": {"inputs": ["close"], "func": f10_vrap_122_vol_term_structure_slope_21_63_d3},
    "f10_vrap_123_vol_term_structure_curvature_21_63_252_d3": {"inputs": ["close"], "func": f10_vrap_123_vol_term_structure_curvature_21_63_252_d3},
    "f10_vrap_124_vol_term_structure_level_avg_3point_d3": {"inputs": ["close"], "func": f10_vrap_124_vol_term_structure_level_avg_3point_d3},
    "f10_vrap_125_vol_term_structure_slope_zscore_504d_d3": {"inputs": ["close"], "func": f10_vrap_125_vol_term_structure_slope_zscore_504d_d3},
    "f10_vrap_126_tail_vol_5pct_abs_ret_63d_d3": {"inputs": ["close"], "func": f10_vrap_126_tail_vol_5pct_abs_ret_63d_d3},
    "f10_vrap_127_tail_vol_95pct_abs_ret_63d_d3": {"inputs": ["close"], "func": f10_vrap_127_tail_vol_95pct_abs_ret_63d_d3},
    "f10_vrap_128_tail_vol_99pct_abs_ret_252d_d3": {"inputs": ["close"], "func": f10_vrap_128_tail_vol_99pct_abs_ret_252d_d3},
    "f10_vrap_129_extreme_tail_concentration_ratio_252d_d3": {"inputs": ["close"], "func": f10_vrap_129_extreme_tail_concentration_ratio_252d_d3},
    "f10_vrap_130_conditional_vol_given_dd_5pct_252d_d3": {"inputs": ["close"], "func": f10_vrap_130_conditional_vol_given_dd_5pct_252d_d3},
    "f10_vrap_131_conditional_vol_given_dd_10pct_252d_d3": {"inputs": ["close"], "func": f10_vrap_131_conditional_vol_given_dd_10pct_252d_d3},
    "f10_vrap_132_conditional_vol_given_new_high_252d_d3": {"inputs": ["close"], "func": f10_vrap_132_conditional_vol_given_new_high_252d_d3},
    "f10_vrap_133_max_drawdown_conditional_vol_252d_d3": {"inputs": ["close"], "func": f10_vrap_133_max_drawdown_conditional_vol_252d_d3},
    "f10_vrap_134_vol_during_uptrend_minus_downtrend_252d_d3": {"inputs": ["close"], "func": f10_vrap_134_vol_during_uptrend_minus_downtrend_252d_d3},
    "f10_vrap_135_vol_flatness_index_252d_d3": {"inputs": ["close"], "func": f10_vrap_135_vol_flatness_index_252d_d3},
    "f10_vrap_136_vol_shape_entropy_252d_d3": {"inputs": ["close"], "func": f10_vrap_136_vol_shape_entropy_252d_d3},
    "f10_vrap_137_realized_var_to_quarticity_ratio_252d_d3": {"inputs": ["close"], "func": f10_vrap_137_realized_var_to_quarticity_ratio_252d_d3},
    "f10_vrap_138_vol_pctrank_minus_trend_pctrank_504d_d3": {"inputs": ["close"], "func": f10_vrap_138_vol_pctrank_minus_trend_pctrank_504d_d3},
    "f10_vrap_139_low_vol_with_high_trend_composite_252d_d3": {"inputs": ["close"], "func": f10_vrap_139_low_vol_with_high_trend_composite_252d_d3},
    "f10_vrap_140_vol_term_structure_inversion_count_252d_d3": {"inputs": ["close"], "func": f10_vrap_140_vol_term_structure_inversion_count_252d_d3},
    "f10_vrap_141_vol_term_structure_inversion_streak_252d_d3": {"inputs": ["close"], "func": f10_vrap_141_vol_term_structure_inversion_streak_252d_d3},
    "f10_vrap_142_neg_tail_es_5pct_252d_d3": {"inputs": ["close"], "func": f10_vrap_142_neg_tail_es_5pct_252d_d3},
    "f10_vrap_143_pos_tail_es_95pct_252d_d3": {"inputs": ["close"], "func": f10_vrap_143_pos_tail_es_95pct_252d_d3},
    "f10_vrap_144_vol_change_to_return_corr_252d_d3": {"inputs": ["close"], "func": f10_vrap_144_vol_change_to_return_corr_252d_d3},
    "f10_vrap_145_realized_skew_252d_d3": {"inputs": ["close"], "func": f10_vrap_145_realized_skew_252d_d3},
    "f10_vrap_146_realized_kurt_252d_d3": {"inputs": ["close"], "func": f10_vrap_146_realized_kurt_252d_d3},
    "f10_vrap_147_tail_ratio_99_1_252d_d3": {"inputs": ["close"], "func": f10_vrap_147_tail_ratio_99_1_252d_d3},
    "f10_vrap_148_composite_regime_score_vol_clustering_asym_d3": {"inputs": ["close", "high", "low"], "func": f10_vrap_148_composite_regime_score_vol_clustering_asym_d3},
    "f10_vrap_149_composite_jump_persistence_score_252d_d3": {"inputs": ["close"], "func": f10_vrap_149_composite_jump_persistence_score_252d_d3},
    "f10_vrap_150_composite_vol_fragility_aggregate_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_150_composite_vol_fragility_aggregate_d3},
}
