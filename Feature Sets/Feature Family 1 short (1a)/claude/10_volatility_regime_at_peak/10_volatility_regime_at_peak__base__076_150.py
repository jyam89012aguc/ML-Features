"""volatility_regime_at_peak base features 076_150 — short blowup pipeline 1a-inverse.

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
#                    BASE FEATURES 076-150
# ============================================================

def f10_vrap_076_yz_to_realized_ratio_63d(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """YZ(63) / Realized vol(63) — overnight contribution proxy."""
    return _safe_div(_yang_zhang(open, high, low, close, QDAYS), _realized_vol(close, QDAYS))


def f10_vrap_077_rs_252_value(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rogers-Satchell 252d vol estimator."""
    return _rs(open, high, low, close, YDAYS)


def f10_vrap_078_max_tr_pctrank_252d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Percentile rank of single-bar TR within 252d."""
    return _rolling_pctrank(_true_range(high, low, close), YDAYS)


def f10_vrap_079_intraday_overnight_corr_63d(open: pd.Series, close: pd.Series) -> pd.Series:
    """63d corr of overnight log-return with same-day intraday log-return."""
    on = np.log(open / close.shift(1).replace(0, np.nan))
    intr = np.log(close / open.replace(0, np.nan))
    return on.rolling(QDAYS, min_periods=MDAYS).corr(intr)


def f10_vrap_080_range_skew_distribution_63d(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Skewness of (H-L)/Close distribution over 63d."""
    return ((high - low) / close).rolling(QDAYS, min_periods=MDAYS).skew()


def f10_vrap_081_realized_quarticity_63d(close: pd.Series) -> pd.Series:
    """Realized quarticity over 63d."""
    return _quarticity(close, QDAYS)


def f10_vrap_082_bipower_var_63d(close: pd.Series) -> pd.Series:
    """Bipower variation over 63d (continuous-part vol proxy)."""
    return _bipower_var(close, QDAYS)


def f10_vrap_083_jump_var_63d(close: pd.Series) -> pd.Series:
    """Jump variation = RV - BV over 63d (clipped at 0)."""
    return _jump_var(close, QDAYS)


def f10_vrap_084_jump_to_realized_ratio_63d(close: pd.Series) -> pd.Series:
    """Jump variation share of realized variance over 63d."""
    return _safe_div(_jump_var(close, QDAYS), _realized_var(close, QDAYS))


def f10_vrap_085_jump_var_252d(close: pd.Series) -> pd.Series:
    """Jump variation over 252d."""
    return _jump_var(close, YDAYS)


def f10_vrap_086_count_abs_ret_gt_3sigma_252d(close: pd.Series) -> pd.Series:
    """Count of bars where |r| > 3*sigma(252d) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r.abs() > 3 * sd).astype(float)
    return cnt.rolling(YDAYS, min_periods=QDAYS).sum()


def f10_vrap_087_count_abs_ret_gt_4sigma_252d(close: pd.Series) -> pd.Series:
    """Count of bars where |r| > 4*sigma(252d) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r.abs() > 4 * sd).astype(float)
    return cnt.rolling(YDAYS, min_periods=QDAYS).sum()


def f10_vrap_088_count_abs_ret_gt_5sigma_252d(close: pd.Series) -> pd.Series:
    """Count of bars where |r| > 5*sigma(252d) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r.abs() > 5 * sd).astype(float)
    return cnt.rolling(YDAYS, min_periods=QDAYS).sum()


def f10_vrap_089_largest_abs_ret_63d(close: pd.Series) -> pd.Series:
    """Max |log return| over 63d."""
    return _log_ret(close).abs().rolling(QDAYS, min_periods=MDAYS).max()


def f10_vrap_090_largest_abs_ret_252d_pctrank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of (max |r| in 252d) within 1260d."""
    mx = _log_ret(close).abs().rolling(YDAYS, min_periods=QDAYS).max()
    return _rolling_pctrank(mx, 1260)


def f10_vrap_091_jump_clustering_lag1_252d(close: pd.Series) -> pd.Series:
    """Autocorr (lag 1) of jump-indicator (|r|>3sigma) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j = (r.abs() > 3 * sd).astype(float)
    return j.rolling(YDAYS, min_periods=QDAYS).corr(j.shift(1))


def f10_vrap_092_jump_skewness_63d(close: pd.Series) -> pd.Series:
    """Skewness of the subset of returns flagged as jumps (|r|>2sigma) over 63d."""
    r = _log_ret(close)
    sd = r.rolling(QDAYS, min_periods=MDAYS).std()
    masked = r.where(r.abs() > 2 * sd, np.nan)
    return masked.rolling(QDAYS, min_periods=MDAYS).skew()


def f10_vrap_093_jump_to_continuous_ratio_252d(close: pd.Series) -> pd.Series:
    """Jump var(252d) / Bipower var(252d)."""
    return _safe_div(_jump_var(close, YDAYS), _bipower_var(close, YDAYS))


def f10_vrap_094_negative_jump_count_252d(close: pd.Series) -> pd.Series:
    """Count over 252d where r < -3*sigma(252d)."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r < -3 * sd).astype(float)
    return cnt.rolling(YDAYS, min_periods=QDAYS).sum()


def f10_vrap_095_positive_jump_count_252d(close: pd.Series) -> pd.Series:
    """Count over 252d where r > 3*sigma(252d)."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    cnt = (r > 3 * sd).astype(float)
    return cnt.rolling(YDAYS, min_periods=QDAYS).sum()


def f10_vrap_096_quarticity_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of 63d realized quarticity within 252d."""
    return _rolling_zscore(_quarticity(close, QDAYS), YDAYS)


def f10_vrap_097_signed_jump_var_252d(close: pd.Series) -> pd.Series:
    """Signed jump var: positive-jump var minus negative-jump var over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j_pos = r.where(r > 3 * sd, 0).pow(2).rolling(YDAYS, min_periods=QDAYS).sum()
    j_neg = r.where(r < -3 * sd, 0).pow(2).rolling(YDAYS, min_periods=QDAYS).sum()
    return j_pos - j_neg


def f10_vrap_098_largest_neg_ret_minus_largest_pos_ret_252d(close: pd.Series) -> pd.Series:
    """(-min r) - (max r) over 252d."""
    r = _log_ret(close)
    return (-r.rolling(YDAYS, min_periods=QDAYS).min()) - r.rolling(YDAYS, min_periods=QDAYS).max()


def f10_vrap_099_jump_size_avg_252d(close: pd.Series) -> pd.Series:
    """Mean absolute return of bars flagged as jumps (|r|>3sigma) over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j = r.abs().where(r.abs() > 3 * sd, np.nan)
    return j.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_vrap_100_max_jump_size_252d(close: pd.Series) -> pd.Series:
    """Max |r| among jump-flagged bars over 252d."""
    r = _log_ret(close)
    sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j = r.abs().where(r.abs() > 3 * sd, np.nan)
    return j.rolling(YDAYS, min_periods=QDAYS).max()


def f10_vrap_101_vol_of_vol_21d_realized_pctrank_504d(close: pd.Series) -> pd.Series:
    """Percentile rank of std-of-21d-realized-vol over 504d."""
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(MDAYS, min_periods=5).std()
    return _rolling_pctrank(vov, 504)


def f10_vrap_102_vol_of_vol_252d_expansion_velocity_21d(close: pd.Series) -> pd.Series:
    """21d change in (std of 21d-realized-vol over 252d)."""
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(YDAYS, min_periods=QDAYS).std()
    return vov.diff(MDAYS)


def f10_vrap_103_vov_regime_above_75pct_252d(close: pd.Series) -> pd.Series:
    """Binary: vol-of-21d-realized-vol (63d std) above its 252d 75th percentile."""
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    q75 = vov.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    return (vov > q75).astype(float)


def f10_vrap_104_realized_vol_2nd_deriv_streak_63d(close: pd.Series) -> pd.Series:
    """Max consecutive bars with d²(21d-realized-vol) > 0 over 63d (vol accelerating)."""
    rv = _realized_vol(close, MDAYS)
    acc = rv.diff().diff()
    pos = (acc > 0).astype(int)
    grp = (pos.diff().ne(0)).cumsum()
    streak = pos.groupby(grp).cumsum() * pos
    return streak.rolling(QDAYS, min_periods=MDAYS).max().astype(float)


def f10_vrap_105_vol_acceleration_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of d²(21d-realized-vol) within 252d."""
    rv = _realized_vol(close, MDAYS)
    return _rolling_zscore(rv.diff().diff(), YDAYS)


def f10_vrap_106_vol_persistence_index_63d(close: pd.Series) -> pd.Series:
    """AR(1) coef of 21d-realized-vol over 63d (vol persistence)."""
    rv = _realized_vol(close, MDAYS)
    lag = rv.shift(1)
    cov = (rv * lag).rolling(QDAYS, min_periods=MDAYS).mean() - rv.rolling(QDAYS, min_periods=MDAYS).mean() * lag.rolling(QDAYS, min_periods=MDAYS).mean()
    var = lag.rolling(QDAYS, min_periods=MDAYS).var()
    return _safe_div(cov, var)


def f10_vrap_107_vol_range_max_minus_min_252d(close: pd.Series) -> pd.Series:
    """Max minus min of 21d-realized-vol over 252d."""
    rv = _realized_vol(close, MDAYS)
    return rv.rolling(YDAYS, min_periods=QDAYS).max() - rv.rolling(YDAYS, min_periods=QDAYS).min()


def f10_vrap_108_vol_max_over_min_ratio_252d(close: pd.Series) -> pd.Series:
    """Max/min of 21d-realized-vol over 252d."""
    rv = _realized_vol(close, MDAYS)
    return _safe_div(rv.rolling(YDAYS, min_periods=QDAYS).max(), rv.rolling(YDAYS, min_periods=QDAYS).min())


def f10_vrap_109_vol_curvature_d2_zscore_252d(close: pd.Series) -> pd.Series:
    """Z-score of second-difference of EMA-smoothed 21d-realized-vol within 252d."""
    rv = _realized_vol(close, MDAYS)
    return _rolling_zscore(_ema(rv, 5).diff().diff(), YDAYS)


def f10_vrap_110_vov_to_vol_ratio_252d(close: pd.Series) -> pd.Series:
    """vol-of-vol(63d std) / mean(21d-realized-vol) over 252d."""
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    return _safe_div(vov, rv.rolling(YDAYS, min_periods=QDAYS).mean())


def f10_vrap_111_max_rvol_in_63d_minus_current_rvol(close: pd.Series) -> pd.Series:
    """Max 21d-realized-vol in 63d minus current."""
    rv = _realized_vol(close, MDAYS)
    return rv.rolling(QDAYS, min_periods=MDAYS).max() - rv


def f10_vrap_112_min_rvol_in_63d_minus_current_rvol(close: pd.Series) -> pd.Series:
    """Current 21d-realized-vol minus 63d-min."""
    rv = _realized_vol(close, MDAYS)
    return rv - rv.rolling(QDAYS, min_periods=MDAYS).min()


def f10_vrap_113_vov_streak_above_median_63d(close: pd.Series) -> pd.Series:
    """Max consecutive bars with vol-of-vol > 63d median over 63d."""
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    med = vov.rolling(QDAYS, min_periods=MDAYS).median()
    above = (vov > med).astype(int)
    grp = (above.diff().ne(0)).cumsum()
    streak = above.groupby(grp).cumsum() * above
    return streak.rolling(QDAYS, min_periods=MDAYS).max().astype(float)


def f10_vrap_114_vol_diff_zscore_63d(close: pd.Series) -> pd.Series:
    """Z-score of 1-day change in 21d-realized-vol over 63d."""
    rv = _realized_vol(close, MDAYS)
    return _rolling_zscore(rv.diff(), QDAYS)


def f10_vrap_115_vol_change_sign_persistence_63d(close: pd.Series) -> pd.Series:
    """63d rolling autocorr (lag 1) of sign(d-vol)."""
    rv = _realized_vol(close, MDAYS)
    s = np.sign(rv.diff().fillna(0))
    return s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(1))


def f10_vrap_116_max_d_vol_252d(close: pd.Series) -> pd.Series:
    """Max |day-over-day change in 21d-realized-vol| over 252d."""
    rv = _realized_vol(close, MDAYS)
    return rv.diff().abs().rolling(YDAYS, min_periods=QDAYS).max()


def f10_vrap_117_vov_pctrank_1260d(close: pd.Series) -> pd.Series:
    """Percentile rank of 63d-vol-of-21d-vol within 1260d."""
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    return _rolling_pctrank(vov, 1260)


def f10_vrap_118_vol_dispersion_index_252d(close: pd.Series) -> pd.Series:
    """(std/mean) of 21d-realized-vol over 252d — CoV of vol."""
    rv = _realized_vol(close, MDAYS)
    return _safe_div(rv.rolling(YDAYS, min_periods=QDAYS).std(), rv.rolling(YDAYS, min_periods=QDAYS).mean())


def f10_vrap_119_vol_iqr_252d(close: pd.Series) -> pd.Series:
    """Inter-quartile range of 21d-realized-vol over 252d."""
    rv = _realized_vol(close, MDAYS)
    q75 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    q25 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    return q75 - q25


def f10_vrap_120_vol_kurtosis_252d(close: pd.Series) -> pd.Series:
    """Kurtosis of 21d-realized-vol over 252d."""
    rv = _realized_vol(close, MDAYS)
    return rv.rolling(YDAYS, min_periods=QDAYS).kurt()


def f10_vrap_121_vol_term_structure_slope_21_252(close: pd.Series) -> pd.Series:
    """Log ratio of 21d-vol to 252d-vol — short-vs-long term-structure slope."""
    rv21 = _realized_vol(close, MDAYS)
    rv252 = _realized_vol(close, YDAYS)
    return _safe_log(rv21) - _safe_log(rv252)


def f10_vrap_122_vol_term_structure_slope_21_63(close: pd.Series) -> pd.Series:
    """Log ratio of 21d-vol to 63d-vol."""
    rv21 = _realized_vol(close, MDAYS)
    rv63 = _realized_vol(close, QDAYS)
    return _safe_log(rv21) - _safe_log(rv63)


def f10_vrap_123_vol_term_structure_curvature_21_63_252(close: pd.Series) -> pd.Series:
    """2*log(63d-vol) - log(21d-vol) - log(252d-vol) — TS curvature."""
    rv21 = _realized_vol(close, MDAYS)
    rv63 = _realized_vol(close, QDAYS)
    rv252 = _realized_vol(close, YDAYS)
    return 2 * _safe_log(rv63) - _safe_log(rv21) - _safe_log(rv252)


def f10_vrap_124_vol_term_structure_level_avg_3point(close: pd.Series) -> pd.Series:
    """Mean of log(21d/63d/252d vol) — vol-level proxy."""
    rv21 = _realized_vol(close, MDAYS)
    rv63 = _realized_vol(close, QDAYS)
    rv252 = _realized_vol(close, YDAYS)
    return (_safe_log(rv21) + _safe_log(rv63) + _safe_log(rv252)) / 3.0


def f10_vrap_125_vol_term_structure_slope_zscore_504d(close: pd.Series) -> pd.Series:
    """Z-score of (log 21d-vol - log 252d-vol) within 504d."""
    slope = _safe_log(_realized_vol(close, MDAYS)) - _safe_log(_realized_vol(close, YDAYS))
    return _rolling_zscore(slope, 504)


def f10_vrap_126_tail_vol_5pct_abs_ret_63d(close: pd.Series) -> pd.Series:
    """5% quantile of |log returns| over 63d (left-tail abs return)."""
    return _log_ret(close).abs().rolling(QDAYS, min_periods=MDAYS).quantile(0.05)


def f10_vrap_127_tail_vol_95pct_abs_ret_63d(close: pd.Series) -> pd.Series:
    """95% quantile of |log returns| over 63d (right-tail abs return)."""
    return _log_ret(close).abs().rolling(QDAYS, min_periods=MDAYS).quantile(0.95)


def f10_vrap_128_tail_vol_99pct_abs_ret_252d(close: pd.Series) -> pd.Series:
    """99% quantile of |log returns| over 252d."""
    return _log_ret(close).abs().rolling(YDAYS, min_periods=QDAYS).quantile(0.99)


def f10_vrap_129_extreme_tail_concentration_ratio_252d(close: pd.Series) -> pd.Series:
    """Sum of |r| for top 5% of bars divided by total |r| over 252d."""
    r = _log_ret(close).abs()
    def _conc(w):
        v = w[~np.isnan(w)]
        if len(v) < 30:
            return np.nan
        k = max(int(len(v) * 0.05), 1)
        top = np.sort(v)[-k:].sum()
        tot = v.sum()
        return float(top / tot) if tot > 0 else np.nan
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_conc, raw=True)


def f10_vrap_130_conditional_vol_given_dd_5pct_252d(close: pd.Series) -> pd.Series:
    """21d-realized-vol of returns on days where 21d drawdown <= -5%."""
    r = _log_ret(close)
    dd = (close / close.rolling(MDAYS, min_periods=5).max()) - 1
    cond = dd <= -0.05
    masked = r.where(cond, np.nan)
    return masked.rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(YDAYS)


def f10_vrap_131_conditional_vol_given_dd_10pct_252d(close: pd.Series) -> pd.Series:
    """21d-realized-vol of returns on days where 21d drawdown <= -10%."""
    r = _log_ret(close)
    dd = (close / close.rolling(MDAYS, min_periods=5).max()) - 1
    cond = dd <= -0.10
    masked = r.where(cond, np.nan)
    return masked.rolling(YDAYS, min_periods=QDAYS).std() * np.sqrt(YDAYS)


def f10_vrap_132_conditional_vol_given_new_high_252d(close: pd.Series) -> pd.Series:
    """Std of |r| on bars at new 63d highs over 252d."""
    hh = close >= close.rolling(QDAYS, min_periods=MDAYS).max()
    r = _log_ret(close).abs()
    masked = r.where(hh, np.nan)
    return masked.rolling(YDAYS, min_periods=QDAYS).std()


def f10_vrap_133_max_drawdown_conditional_vol_252d(close: pd.Series) -> pd.Series:
    """Mean of 21d-realized-vol on days where rolling-252d drawdown is at its 252d max."""
    rv = _realized_vol(close, MDAYS)
    dd = (close / close.rolling(YDAYS, min_periods=QDAYS).max()) - 1
    dd_max = dd.rolling(YDAYS, min_periods=QDAYS).min()
    cond = dd <= dd_max + 1e-12
    return rv.where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()


def f10_vrap_134_vol_during_uptrend_minus_downtrend_252d(close: pd.Series) -> pd.Series:
    """Mean 21d-vol on up-trend (SMA50>SMA200) days minus down-trend days, over 252d."""
    rv = _realized_vol(close, MDAYS)
    s50 = close.rolling(50, min_periods=max(50 // 3, 2)).mean()
    s200 = close.rolling(200, min_periods=max(200 // 3, 2)).mean()
    up = rv.where(s50 > s200, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    dn = rv.where(s50 <= s200, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return up - dn


def f10_vrap_135_vol_flatness_index_252d(close: pd.Series) -> pd.Series:
    """1 minus normalized range of 21d-realized-vol over 252d (lower = more peaked)."""
    rv = _realized_vol(close, MDAYS)
    rng = rv.rolling(YDAYS, min_periods=QDAYS).max() - rv.rolling(YDAYS, min_periods=QDAYS).min()
    return 1.0 - _safe_div(rng, rv.rolling(YDAYS, min_periods=QDAYS).mean())


def f10_vrap_136_vol_shape_entropy_252d(close: pd.Series) -> pd.Series:
    """Shannon entropy of 5-bin distribution of 21d-realized-vol over 252d."""
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
    return rv.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)


def f10_vrap_137_realized_var_to_quarticity_ratio_252d(close: pd.Series) -> pd.Series:
    """Realized var(252d) / sqrt(realized quarticity(252d) * 3) — Jarque-Bera-like vol consistency."""
    return _safe_div(_realized_var(close, YDAYS), np.sqrt(_quarticity(close, YDAYS) * 3))


def f10_vrap_138_vol_pctrank_minus_trend_pctrank_504d(close: pd.Series) -> pd.Series:
    """Pctrank(21d-vol) minus pctrank(252d log-return), within 504d."""
    rv = _realized_vol(close, MDAYS)
    mom = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return _rolling_pctrank(rv, 504) - _rolling_pctrank(mom, 504)


def f10_vrap_139_low_vol_with_high_trend_composite_252d(close: pd.Series) -> pd.Series:
    """1 minus pctrank(21d-vol) plus pctrank(252d mom), 252d — silent-grind regime."""
    rv = _realized_vol(close, MDAYS)
    mom = _safe_log(close) - _safe_log(close.shift(YDAYS))
    return (1.0 - _rolling_pctrank(rv, YDAYS)) + _rolling_pctrank(mom, YDAYS)


def f10_vrap_140_vol_term_structure_inversion_count_252d(close: pd.Series) -> pd.Series:
    """Count days where 21d-vol > 252d-vol over 252d (short>long inversion)."""
    rv21 = _realized_vol(close, MDAYS)
    rv252 = _realized_vol(close, YDAYS)
    inv = (rv21 > rv252).astype(float)
    return inv.rolling(YDAYS, min_periods=QDAYS).sum()


def f10_vrap_141_vol_term_structure_inversion_streak_252d(close: pd.Series) -> pd.Series:
    """Max consecutive bars 21d-vol > 252d-vol over 252d."""
    rv21 = _realized_vol(close, MDAYS)
    rv252 = _realized_vol(close, YDAYS)
    inv = (rv21 > rv252).astype(int)
    grp = (inv.diff().ne(0)).cumsum()
    streak = inv.groupby(grp).cumsum() * inv
    return streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)


def f10_vrap_142_neg_tail_es_5pct_252d(close: pd.Series) -> pd.Series:
    """Expected Shortfall (mean of returns <= 5% quantile) over 252d."""
    r = _log_ret(close)
    q05 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.05)
    masked = r.where(r <= q05, np.nan)
    return masked.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_vrap_143_pos_tail_es_95pct_252d(close: pd.Series) -> pd.Series:
    """Expected upside (mean of returns >= 95% quantile) over 252d."""
    r = _log_ret(close)
    q95 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.95)
    masked = r.where(r >= q95, np.nan)
    return masked.rolling(YDAYS, min_periods=QDAYS).mean()


def f10_vrap_144_vol_change_to_return_corr_252d(close: pd.Series) -> pd.Series:
    """252d corr of (21d-vol diff) with same-day log-return."""
    rv = _realized_vol(close, MDAYS)
    return rv.diff().rolling(YDAYS, min_periods=QDAYS).corr(_log_ret(close))


def f10_vrap_145_realized_skew_252d(close: pd.Series) -> pd.Series:
    """Skewness of log returns over 252d."""
    return _log_ret(close).rolling(YDAYS, min_periods=QDAYS).skew()


def f10_vrap_146_realized_kurt_252d(close: pd.Series) -> pd.Series:
    """Kurtosis of log returns over 252d."""
    return _log_ret(close).rolling(YDAYS, min_periods=QDAYS).kurt()


def f10_vrap_147_tail_ratio_99_1_252d(close: pd.Series) -> pd.Series:
    """Long-horizon 99/1 quantile ratio of |log ret| over 252d."""
    r = _log_ret(close).abs()
    q99 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    q01 = r.rolling(YDAYS, min_periods=QDAYS).quantile(0.01).replace(0, np.nan)
    return _safe_div(q99, q01)


def f10_vrap_148_composite_regime_score_vol_clustering_asym(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """z(rvol_252_pctrank_1260) + z(sq_ret_autocorr_lag1_63) + z(semivar ratio down/up 252d)."""
    p1 = _rolling_pctrank(_realized_vol(close, YDAYS), 1260)
    s = _log_ret(close).pow(2)
    ac = s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(1))
    a = _safe_div(_semi_var(close, YDAYS, 'down'), _semi_var(close, YDAYS, 'up'))
    return _rolling_zscore(p1, YDAYS) + _rolling_zscore(ac, YDAYS) + _rolling_zscore(a, YDAYS)


def f10_vrap_149_composite_jump_persistence_score_252d(close: pd.Series) -> pd.Series:
    """z(jump_var_252d) + z(jump_clustering_lag1) + z(quarticity)."""
    jv = _jump_var(close, YDAYS)
    r = _log_ret(close); sd = r.rolling(YDAYS, min_periods=QDAYS).std()
    j = (r.abs() > 3 * sd).astype(float)
    jc = j.rolling(YDAYS, min_periods=QDAYS).corr(j.shift(1))
    q = _quarticity(close, YDAYS)
    return _rolling_zscore(jv, YDAYS) + _rolling_zscore(jc, YDAYS) + _rolling_zscore(q, YDAYS)


def f10_vrap_150_composite_vol_fragility_aggregate(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Aggregate: z(vol_pctrank_1260) + z(vov_pctrank_504) + z(yz_to_realized_ratio_63d) + z(term_struct_inv_streak)."""
    p1 = _rolling_pctrank(_realized_vol(close, YDAYS), 1260)
    rv = _realized_vol(close, MDAYS); vov = rv.rolling(QDAYS, min_periods=MDAYS).std()
    p2 = _rolling_pctrank(vov, 504)
    p3 = _safe_div(_yang_zhang(open, high, low, close, QDAYS), _realized_vol(close, QDAYS))
    inv = (rv > _realized_vol(close, YDAYS)).astype(int)
    grp = (inv.diff().ne(0)).cumsum()
    streak = inv.groupby(grp).cumsum() * inv
    sk = streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)
    return _rolling_zscore(p1, YDAYS) + _rolling_zscore(p2, YDAYS) + _rolling_zscore(p3, YDAYS) + _rolling_zscore(sk, YDAYS)


VOLATILITY_REGIME_AT_PEAK_BASE_REGISTRY_076_150 = {
    "f10_vrap_076_yz_to_realized_ratio_63d": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_076_yz_to_realized_ratio_63d},
    "f10_vrap_077_rs_252_value": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_077_rs_252_value},
    "f10_vrap_078_max_tr_pctrank_252d": {"inputs": ["high", "low", "close"], "func": f10_vrap_078_max_tr_pctrank_252d},
    "f10_vrap_079_intraday_overnight_corr_63d": {"inputs": ["open", "close"], "func": f10_vrap_079_intraday_overnight_corr_63d},
    "f10_vrap_080_range_skew_distribution_63d": {"inputs": ["high", "low", "close"], "func": f10_vrap_080_range_skew_distribution_63d},
    "f10_vrap_081_realized_quarticity_63d": {"inputs": ["close"], "func": f10_vrap_081_realized_quarticity_63d},
    "f10_vrap_082_bipower_var_63d": {"inputs": ["close"], "func": f10_vrap_082_bipower_var_63d},
    "f10_vrap_083_jump_var_63d": {"inputs": ["close"], "func": f10_vrap_083_jump_var_63d},
    "f10_vrap_084_jump_to_realized_ratio_63d": {"inputs": ["close"], "func": f10_vrap_084_jump_to_realized_ratio_63d},
    "f10_vrap_085_jump_var_252d": {"inputs": ["close"], "func": f10_vrap_085_jump_var_252d},
    "f10_vrap_086_count_abs_ret_gt_3sigma_252d": {"inputs": ["close"], "func": f10_vrap_086_count_abs_ret_gt_3sigma_252d},
    "f10_vrap_087_count_abs_ret_gt_4sigma_252d": {"inputs": ["close"], "func": f10_vrap_087_count_abs_ret_gt_4sigma_252d},
    "f10_vrap_088_count_abs_ret_gt_5sigma_252d": {"inputs": ["close"], "func": f10_vrap_088_count_abs_ret_gt_5sigma_252d},
    "f10_vrap_089_largest_abs_ret_63d": {"inputs": ["close"], "func": f10_vrap_089_largest_abs_ret_63d},
    "f10_vrap_090_largest_abs_ret_252d_pctrank_1260d": {"inputs": ["close"], "func": f10_vrap_090_largest_abs_ret_252d_pctrank_1260d},
    "f10_vrap_091_jump_clustering_lag1_252d": {"inputs": ["close"], "func": f10_vrap_091_jump_clustering_lag1_252d},
    "f10_vrap_092_jump_skewness_63d": {"inputs": ["close"], "func": f10_vrap_092_jump_skewness_63d},
    "f10_vrap_093_jump_to_continuous_ratio_252d": {"inputs": ["close"], "func": f10_vrap_093_jump_to_continuous_ratio_252d},
    "f10_vrap_094_negative_jump_count_252d": {"inputs": ["close"], "func": f10_vrap_094_negative_jump_count_252d},
    "f10_vrap_095_positive_jump_count_252d": {"inputs": ["close"], "func": f10_vrap_095_positive_jump_count_252d},
    "f10_vrap_096_quarticity_zscore_252d": {"inputs": ["close"], "func": f10_vrap_096_quarticity_zscore_252d},
    "f10_vrap_097_signed_jump_var_252d": {"inputs": ["close"], "func": f10_vrap_097_signed_jump_var_252d},
    "f10_vrap_098_largest_neg_ret_minus_largest_pos_ret_252d": {"inputs": ["close"], "func": f10_vrap_098_largest_neg_ret_minus_largest_pos_ret_252d},
    "f10_vrap_099_jump_size_avg_252d": {"inputs": ["close"], "func": f10_vrap_099_jump_size_avg_252d},
    "f10_vrap_100_max_jump_size_252d": {"inputs": ["close"], "func": f10_vrap_100_max_jump_size_252d},
    "f10_vrap_101_vol_of_vol_21d_realized_pctrank_504d": {"inputs": ["close"], "func": f10_vrap_101_vol_of_vol_21d_realized_pctrank_504d},
    "f10_vrap_102_vol_of_vol_252d_expansion_velocity_21d": {"inputs": ["close"], "func": f10_vrap_102_vol_of_vol_252d_expansion_velocity_21d},
    "f10_vrap_103_vov_regime_above_75pct_252d": {"inputs": ["close"], "func": f10_vrap_103_vov_regime_above_75pct_252d},
    "f10_vrap_104_realized_vol_2nd_deriv_streak_63d": {"inputs": ["close"], "func": f10_vrap_104_realized_vol_2nd_deriv_streak_63d},
    "f10_vrap_105_vol_acceleration_zscore_252d": {"inputs": ["close"], "func": f10_vrap_105_vol_acceleration_zscore_252d},
    "f10_vrap_106_vol_persistence_index_63d": {"inputs": ["close"], "func": f10_vrap_106_vol_persistence_index_63d},
    "f10_vrap_107_vol_range_max_minus_min_252d": {"inputs": ["close"], "func": f10_vrap_107_vol_range_max_minus_min_252d},
    "f10_vrap_108_vol_max_over_min_ratio_252d": {"inputs": ["close"], "func": f10_vrap_108_vol_max_over_min_ratio_252d},
    "f10_vrap_109_vol_curvature_d2_zscore_252d": {"inputs": ["close"], "func": f10_vrap_109_vol_curvature_d2_zscore_252d},
    "f10_vrap_110_vov_to_vol_ratio_252d": {"inputs": ["close"], "func": f10_vrap_110_vov_to_vol_ratio_252d},
    "f10_vrap_111_max_rvol_in_63d_minus_current_rvol": {"inputs": ["close"], "func": f10_vrap_111_max_rvol_in_63d_minus_current_rvol},
    "f10_vrap_112_min_rvol_in_63d_minus_current_rvol": {"inputs": ["close"], "func": f10_vrap_112_min_rvol_in_63d_minus_current_rvol},
    "f10_vrap_113_vov_streak_above_median_63d": {"inputs": ["close"], "func": f10_vrap_113_vov_streak_above_median_63d},
    "f10_vrap_114_vol_diff_zscore_63d": {"inputs": ["close"], "func": f10_vrap_114_vol_diff_zscore_63d},
    "f10_vrap_115_vol_change_sign_persistence_63d": {"inputs": ["close"], "func": f10_vrap_115_vol_change_sign_persistence_63d},
    "f10_vrap_116_max_d_vol_252d": {"inputs": ["close"], "func": f10_vrap_116_max_d_vol_252d},
    "f10_vrap_117_vov_pctrank_1260d": {"inputs": ["close"], "func": f10_vrap_117_vov_pctrank_1260d},
    "f10_vrap_118_vol_dispersion_index_252d": {"inputs": ["close"], "func": f10_vrap_118_vol_dispersion_index_252d},
    "f10_vrap_119_vol_iqr_252d": {"inputs": ["close"], "func": f10_vrap_119_vol_iqr_252d},
    "f10_vrap_120_vol_kurtosis_252d": {"inputs": ["close"], "func": f10_vrap_120_vol_kurtosis_252d},
    "f10_vrap_121_vol_term_structure_slope_21_252": {"inputs": ["close"], "func": f10_vrap_121_vol_term_structure_slope_21_252},
    "f10_vrap_122_vol_term_structure_slope_21_63": {"inputs": ["close"], "func": f10_vrap_122_vol_term_structure_slope_21_63},
    "f10_vrap_123_vol_term_structure_curvature_21_63_252": {"inputs": ["close"], "func": f10_vrap_123_vol_term_structure_curvature_21_63_252},
    "f10_vrap_124_vol_term_structure_level_avg_3point": {"inputs": ["close"], "func": f10_vrap_124_vol_term_structure_level_avg_3point},
    "f10_vrap_125_vol_term_structure_slope_zscore_504d": {"inputs": ["close"], "func": f10_vrap_125_vol_term_structure_slope_zscore_504d},
    "f10_vrap_126_tail_vol_5pct_abs_ret_63d": {"inputs": ["close"], "func": f10_vrap_126_tail_vol_5pct_abs_ret_63d},
    "f10_vrap_127_tail_vol_95pct_abs_ret_63d": {"inputs": ["close"], "func": f10_vrap_127_tail_vol_95pct_abs_ret_63d},
    "f10_vrap_128_tail_vol_99pct_abs_ret_252d": {"inputs": ["close"], "func": f10_vrap_128_tail_vol_99pct_abs_ret_252d},
    "f10_vrap_129_extreme_tail_concentration_ratio_252d": {"inputs": ["close"], "func": f10_vrap_129_extreme_tail_concentration_ratio_252d},
    "f10_vrap_130_conditional_vol_given_dd_5pct_252d": {"inputs": ["close"], "func": f10_vrap_130_conditional_vol_given_dd_5pct_252d},
    "f10_vrap_131_conditional_vol_given_dd_10pct_252d": {"inputs": ["close"], "func": f10_vrap_131_conditional_vol_given_dd_10pct_252d},
    "f10_vrap_132_conditional_vol_given_new_high_252d": {"inputs": ["close"], "func": f10_vrap_132_conditional_vol_given_new_high_252d},
    "f10_vrap_133_max_drawdown_conditional_vol_252d": {"inputs": ["close"], "func": f10_vrap_133_max_drawdown_conditional_vol_252d},
    "f10_vrap_134_vol_during_uptrend_minus_downtrend_252d": {"inputs": ["close"], "func": f10_vrap_134_vol_during_uptrend_minus_downtrend_252d},
    "f10_vrap_135_vol_flatness_index_252d": {"inputs": ["close"], "func": f10_vrap_135_vol_flatness_index_252d},
    "f10_vrap_136_vol_shape_entropy_252d": {"inputs": ["close"], "func": f10_vrap_136_vol_shape_entropy_252d},
    "f10_vrap_137_realized_var_to_quarticity_ratio_252d": {"inputs": ["close"], "func": f10_vrap_137_realized_var_to_quarticity_ratio_252d},
    "f10_vrap_138_vol_pctrank_minus_trend_pctrank_504d": {"inputs": ["close"], "func": f10_vrap_138_vol_pctrank_minus_trend_pctrank_504d},
    "f10_vrap_139_low_vol_with_high_trend_composite_252d": {"inputs": ["close"], "func": f10_vrap_139_low_vol_with_high_trend_composite_252d},
    "f10_vrap_140_vol_term_structure_inversion_count_252d": {"inputs": ["close"], "func": f10_vrap_140_vol_term_structure_inversion_count_252d},
    "f10_vrap_141_vol_term_structure_inversion_streak_252d": {"inputs": ["close"], "func": f10_vrap_141_vol_term_structure_inversion_streak_252d},
    "f10_vrap_142_neg_tail_es_5pct_252d": {"inputs": ["close"], "func": f10_vrap_142_neg_tail_es_5pct_252d},
    "f10_vrap_143_pos_tail_es_95pct_252d": {"inputs": ["close"], "func": f10_vrap_143_pos_tail_es_95pct_252d},
    "f10_vrap_144_vol_change_to_return_corr_252d": {"inputs": ["close"], "func": f10_vrap_144_vol_change_to_return_corr_252d},
    "f10_vrap_145_realized_skew_252d": {"inputs": ["close"], "func": f10_vrap_145_realized_skew_252d},
    "f10_vrap_146_realized_kurt_252d": {"inputs": ["close"], "func": f10_vrap_146_realized_kurt_252d},
    "f10_vrap_147_tail_ratio_99_1_252d": {"inputs": ["close"], "func": f10_vrap_147_tail_ratio_99_1_252d},
    "f10_vrap_148_composite_regime_score_vol_clustering_asym": {"inputs": ["close", "high", "low"], "func": f10_vrap_148_composite_regime_score_vol_clustering_asym},
    "f10_vrap_149_composite_jump_persistence_score_252d": {"inputs": ["close"], "func": f10_vrap_149_composite_jump_persistence_score_252d},
    "f10_vrap_150_composite_vol_fragility_aggregate": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_150_composite_vol_fragility_aggregate},
}
