"""volatility_regime_at_peak d3 features 001_075 — short blowup pipeline 1a-inverse.

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
#                    D3 FEATURES 001-075
# ============================================================

def f10_vrap_001_rvol_63_pctrank_504d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_realized_vol(close, QDAYS), 504)).diff().diff().diff()


def f10_vrap_002_rvol_63_pctrank_1260d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_realized_vol(close, QDAYS), 1260)).diff().diff().diff()


def f10_vrap_003_rvol_252_pctrank_1260d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_realized_vol(close, YDAYS), 1260)).diff().diff().diff()


def f10_vrap_004_park_63_pctrank_504d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_parkinson(high, low, QDAYS), 504)).diff().diff().diff()


def f10_vrap_005_park_252_pctrank_1260d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_parkinson(high, low, YDAYS), 1260)).diff().diff().diff()


def f10_vrap_006_gk_63_pctrank_504d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_gk(open, high, low, close, QDAYS), 504)).diff().diff().diff()


def f10_vrap_007_yz_63_pctrank_504d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_yang_zhang(open, high, low, close, QDAYS), 504)).diff().diff().diff()


def f10_vrap_008_yz_252_pctrank_1260d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_yang_zhang(open, high, low, close, YDAYS), 1260)).diff().diff().diff()


def f10_vrap_009_atr_21_pctrank_504d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_atr(high, low, close, MDAYS), 504)).diff().diff().diff()


def f10_vrap_010_atr_252_pctrank_1260d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_atr(high, low, close, YDAYS), 1260)).diff().diff().diff()


def f10_vrap_011_dollar_volvol_pctrank_504d_d3(close: pd.Series, volume: pd.Series) -> pd.Series:
    dv = close * volume
    return (_rolling_pctrank(dv.rolling(QDAYS, min_periods=MDAYS).std(), 504)).diff().diff().diff()


def f10_vrap_012_rvol_63_zscore_1260d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_zscore(_realized_vol(close, QDAYS), 1260)).diff().diff().diff()


def f10_vrap_013_park_63_zscore_1260d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    return (_rolling_zscore(_parkinson(high, low, QDAYS), 1260)).diff().diff().diff()


def f10_vrap_014_rvol_252_zscore_1260d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_zscore(_realized_vol(close, YDAYS), 1260)).diff().diff().diff()


def f10_vrap_015_rvol_5_pctrank_252d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_realized_vol(close, 5), YDAYS)).diff().diff().diff()


def f10_vrap_016_rvol_21_pctrank_504d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_realized_vol(close, MDAYS), 504)).diff().diff().diff()


def f10_vrap_017_park_21_pctrank_252d_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_parkinson(high, low, MDAYS), YDAYS)).diff().diff().diff()


def f10_vrap_018_atr_63_pctrank_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_atr(high, low, close, QDAYS), YDAYS)).diff().diff().diff()


def f10_vrap_019_atr_21_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_zscore(_atr(high, low, close, MDAYS), YDAYS)).diff().diff().diff()


def f10_vrap_020_realized_var_63_pctrank_504d_d3(close: pd.Series) -> pd.Series:
    return (_rolling_pctrank(_realized_var(close, QDAYS), 504)).diff().diff().diff()


def f10_vrap_021_sq_ret_autocorr_lag1_63d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).pow(2)
    return (s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(1))).diff().diff().diff()


def f10_vrap_022_sq_ret_autocorr_lag5_63d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).pow(2)
    return (s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(5))).diff().diff().diff()


def f10_vrap_023_sq_ret_autocorr_lag21_252d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).pow(2)
    return (s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(MDAYS))).diff().diff().diff()


def f10_vrap_024_abs_ret_autocorr_lag1_63d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).abs()
    return (s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(1))).diff().diff().diff()


def f10_vrap_025_abs_ret_autocorr_lag5_63d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).abs()
    return (s.rolling(QDAYS, min_periods=MDAYS).corr(s.shift(5))).diff().diff().diff()


def f10_vrap_026_abs_ret_autocorr_lag21_252d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).abs()
    return (s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(MDAYS))).diff().diff().diff()


def f10_vrap_027_garch_alpha_beta_proxy_252d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).pow(2)
    rv = _realized_var(close, MDAYS)
    a = s.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))
    b = s.rolling(YDAYS, min_periods=QDAYS).corr(rv.shift(1))
    return (a.fillna(0) + b.fillna(0)).diff().diff().diff()


def f10_vrap_028_vol_persistence_halflife_63d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).abs()
    lag = s.shift(1)
    cov = (s * lag).rolling(QDAYS, min_periods=MDAYS).mean() - s.rolling(QDAYS, min_periods=MDAYS).mean() * lag.rolling(QDAYS, min_periods=MDAYS).mean()
    var = lag.rolling(QDAYS, min_periods=MDAYS).var()
    phi = _safe_div(cov, var).clip(-0.999, 0.999)
    return (-np.log(2.0) / np.log(phi.abs().replace(0, np.nan))).diff().diff().diff()


def f10_vrap_029_volvol_autocorr_lag1_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv.rolling(QDAYS, min_periods=MDAYS).corr(rv.shift(1))).diff().diff().diff()


def f10_vrap_030_vol_meanrev_speed_proxy_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    m = rv.rolling(YDAYS, min_periods=QDAYS).mean()
    dem = rv - m
    lag = dem.shift(1)
    cov = (dem * lag).rolling(QDAYS, min_periods=MDAYS).mean() - dem.rolling(QDAYS, min_periods=MDAYS).mean() * lag.rolling(QDAYS, min_periods=MDAYS).mean()
    var = lag.rolling(QDAYS, min_periods=MDAYS).var()
    return (_safe_div(cov, var)).diff().diff().diff()


def f10_vrap_031_long_memory_exponent_absret_252d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).abs()
    def _h(w):
        v = w[~np.isnan(w)]
        if len(v) < 30:
            return np.nan
        try:
            mean = v.mean(); dev = np.cumsum(v - mean)
            rng = dev.max() - dev.min(); sd = v.std()
            if sd == 0 or rng == 0:
                return np.nan
            return float(np.log(rng / sd) / np.log(len(v)))
        except Exception:
            return np.nan
    return (s.rolling(YDAYS, min_periods=QDAYS).apply(_h, raw=True)).diff().diff().diff()


def f10_vrap_032_squared_ret_corr_with_vol_63d_d3(close: pd.Series) -> pd.Series:
    s = _log_ret(close).pow(2)
    rv = _realized_vol(close, MDAYS)
    return (s.rolling(QDAYS, min_periods=MDAYS).corr(rv)).diff().diff().diff()


def f10_vrap_033_clustering_score_intensity_63d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close).abs()
    med = r.rolling(QDAYS, min_periods=MDAYS).median()
    big = (r > med)
    pair = (big & big.shift(1).fillna(False)).astype(float)
    return (pair.rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()


def f10_vrap_034_vol_acceleration_zscore_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (_rolling_zscore(rv.diff(), QDAYS)).diff().diff().diff()


def f10_vrap_035_vol_regime_change_count_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    s = np.sign(rv.diff().fillna(0))
    flips = ((s != s.shift(1)) & s.shift(1).ne(0)).astype(float)
    return (flips.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f10_vrap_036_persistent_low_vol_streak_max_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    q25 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.25)
    low = (rv < q25).astype(int)
    grp = (low.diff().ne(0)).cumsum()
    streak = low.groupby(grp).cumsum() * low
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff().diff().diff()


def f10_vrap_037_persistent_high_vol_streak_max_252d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    q75 = rv.rolling(YDAYS, min_periods=QDAYS).quantile(0.75)
    high_ = (rv > q75).astype(int)
    grp = (high_.diff().ne(0)).cumsum()
    streak = high_.groupby(grp).cumsum() * high_
    return (streak.rolling(YDAYS, min_periods=QDAYS).max().astype(float)).diff().diff().diff()


def f10_vrap_038_vol_change_corr_with_return_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv.diff().rolling(QDAYS, min_periods=MDAYS).corr(_log_ret(close))).diff().diff().diff()


def f10_vrap_039_volvol_pctrank_504d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    vov = rv.rolling(MDAYS, min_periods=5).std()
    return (_rolling_pctrank(vov, 504)).diff().diff().diff()


def f10_vrap_040_vol_clustering_index_intensity_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close).abs()
    pair = (r * r.shift(1))
    norm = (_log_ret(close).rolling(YDAYS, min_periods=QDAYS).std()) ** 2
    return (_safe_div(pair.rolling(YDAYS, min_periods=QDAYS).mean(), norm)).diff().diff().diff()


def f10_vrap_041_downside_semivar_63d_d3(close: pd.Series) -> pd.Series:
    return (_semi_var(close, QDAYS, 'down')).diff().diff().diff()


def f10_vrap_042_upside_semivar_63d_d3(close: pd.Series) -> pd.Series:
    return (_semi_var(close, QDAYS, 'up')).diff().diff().diff()


def f10_vrap_043_semivar_ratio_down_up_63d_d3(close: pd.Series) -> pd.Series:
    return (_safe_div(_semi_var(close, QDAYS, 'down'), _semi_var(close, QDAYS, 'up'))).diff().diff().diff()


def f10_vrap_044_downside_semivar_252d_d3(close: pd.Series) -> pd.Series:
    return (_semi_var(close, YDAYS, 'down')).diff().diff().diff()


def f10_vrap_045_upside_semivar_252d_d3(close: pd.Series) -> pd.Series:
    return (_semi_var(close, YDAYS, 'up')).diff().diff().diff()


def f10_vrap_046_semivar_ratio_down_up_252d_d3(close: pd.Series) -> pd.Series:
    return (_safe_div(_semi_var(close, YDAYS, 'down'), _semi_var(close, YDAYS, 'up'))).diff().diff().diff()


def f10_vrap_047_leverage_effect_corr_63d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    return (r.shift(1).rolling(QDAYS, min_periods=MDAYS).corr(r.abs())).diff().diff().diff()


def f10_vrap_048_leverage_effect_corr_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    return (r.shift(1).rolling(YDAYS, min_periods=QDAYS).corr(r.abs())).diff().diff().diff()


def f10_vrap_049_down_move_vol_given_drawdown_5pct_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    dd = (close / close.rolling(MDAYS, min_periods=5).max()) - 1
    cond = dd <= -0.05
    masked = r.where(cond, np.nan)
    return (masked.rolling(QDAYS, min_periods=5).std() * np.sqrt(YDAYS)).diff().diff().diff()


def f10_vrap_050_downside_deviation_minus_upside_dev_63d_d3(close: pd.Series) -> pd.Series:
    return (np.sqrt(_semi_var(close, QDAYS, 'down')) - np.sqrt(_semi_var(close, QDAYS, 'up'))).diff().diff().diff()


def f10_vrap_051_vol_given_down_move_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    cond = r.shift(1) < 0
    return (r.abs().where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f10_vrap_052_vol_given_up_move_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    cond = r.shift(1) > 0
    return (r.abs().where(cond, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f10_vrap_053_asym_vol_response_ratio_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    dn = r.abs().where(r.shift(1) < 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    up = r.abs().where(r.shift(1) > 0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean()
    return (_safe_div(dn, up)).diff().diff().diff()


def f10_vrap_054_vol_skewness_distribution_63d_d3(close: pd.Series) -> pd.Series:
    rv = _realized_vol(close, MDAYS)
    return (rv.rolling(QDAYS, min_periods=MDAYS).skew()).diff().diff().diff()


def f10_vrap_055_pelaez_asym_vol_63d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    em = r.clip(upper=0).rolling(QDAYS, min_periods=MDAYS).mean()
    ep = r.clip(lower=0).rolling(QDAYS, min_periods=MDAYS).mean()
    return (em.pow(2) - ep.pow(2)).diff().diff().diff()


def f10_vrap_056_neg_ret_share_of_total_var_63d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    neg = r.where(r < 0, 0).pow(2).rolling(QDAYS, min_periods=MDAYS).sum()
    tot = r.pow(2).rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(neg, tot)).diff().diff().diff()


def f10_vrap_057_pos_ret_share_of_total_var_63d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    pos = r.where(r > 0, 0).pow(2).rolling(QDAYS, min_periods=MDAYS).sum()
    tot = r.pow(2).rolling(QDAYS, min_periods=MDAYS).sum()
    return (_safe_div(pos, tot)).diff().diff().diff()


def f10_vrap_058_max_down_move_vs_max_up_move_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    mx_dn = (-r).rolling(YDAYS, min_periods=QDAYS).max()
    mx_up = r.rolling(YDAYS, min_periods=QDAYS).max()
    return (_safe_div(mx_dn, mx_up)).diff().diff().diff()


def f10_vrap_059_downside_skew_63d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    neg = r.where(r < 0, np.nan)
    return (neg.rolling(QDAYS, min_periods=MDAYS).skew()).diff().diff().diff()


def f10_vrap_060_garch_asym_proxy_252d_d3(close: pd.Series) -> pd.Series:
    r = _log_ret(close)
    s = r.pow(2)
    neg = s.where(r.shift(1) < 0, np.nan)
    pos = s.where(r.shift(1) > 0, np.nan)
    a_neg = neg.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))
    a_pos = pos.rolling(YDAYS, min_periods=QDAYS).corr(s.shift(1))
    return (a_neg.fillna(0) - a_pos.fillna(0)).diff().diff().diff()


def f10_vrap_061_yz_63_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_yang_zhang(open, high, low, close, QDAYS)).diff().diff().diff()


def f10_vrap_062_yz_252_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_yang_zhang(open, high, low, close, YDAYS)).diff().diff().diff()


def f10_vrap_063_yz_504_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_yang_zhang(open, high, low, close, 504)).diff().diff().diff()


def f10_vrap_064_overnight_var_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    log_oc = np.log(open / close.shift(1).replace(0, np.nan))
    return (log_oc.rolling(QDAYS, min_periods=MDAYS).var()).diff().diff().diff()


def f10_vrap_065_intraday_var_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    log_co = np.log(close / open.replace(0, np.nan))
    return (log_co.rolling(QDAYS, min_periods=MDAYS).var()).diff().diff().diff()


def f10_vrap_066_overnight_to_intraday_var_ratio_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    log_oc = np.log(open / close.shift(1).replace(0, np.nan))
    log_co = np.log(close / open.replace(0, np.nan))
    return (_safe_div(log_oc.rolling(QDAYS, min_periods=MDAYS).var(), log_co.rolling(QDAYS, min_periods=MDAYS).var())).diff().diff().diff()


def f10_vrap_067_gap_share_of_total_var_252d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    log_oc = np.log(open / close.shift(1).replace(0, np.nan))
    cc = _safe_log(close).diff()
    return (_safe_div(log_oc.rolling(YDAYS, min_periods=QDAYS).var(), cc.rolling(YDAYS, min_periods=QDAYS).var())).diff().diff().diff()


def f10_vrap_068_range_to_close_mean_ratio_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (((high - low) / close).rolling(QDAYS, min_periods=MDAYS).mean()).diff().diff().diff()


def f10_vrap_069_range_to_close_zscore_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_rolling_zscore((high - low) / close, YDAYS)).diff().diff().diff()


def f10_vrap_070_range_expansion_bar_count_252d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tr = _true_range(high, low, close)
    atr = _atr(high, low, close, MDAYS)
    big = (tr > 1.5 * atr).astype(float)
    return (big.rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff().diff()


def f10_vrap_071_schwartz_smith_proxy_252d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    yz = _yang_zhang(open, high, low, close, QDAYS)
    gk = _gk(open, high, low, close, QDAYS)
    return (_safe_div(yz, gk).rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff().diff()


def f10_vrap_072_intraday_vol_persistence_63d_d3(open: pd.Series, close: pd.Series) -> pd.Series:
    intr = np.log(close / open.replace(0, np.nan))
    return (intr.rolling(QDAYS, min_periods=MDAYS).corr(intr.shift(1))).diff().diff().diff()


def f10_vrap_073_range_truncation_index_21_63_d3(high: pd.Series, low: pd.Series) -> pd.Series:
    r = (high - low)
    return (_safe_div(r.rolling(MDAYS, min_periods=5).mean(), r.rolling(QDAYS, min_periods=MDAYS).mean())).diff().diff().diff()


def f10_vrap_074_park_to_realized_ratio_63d_d3(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_safe_div(_parkinson(high, low, QDAYS), _realized_vol(close, QDAYS))).diff().diff().diff()


def f10_vrap_075_gk_to_realized_ratio_63d_d3(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    return (_safe_div(_gk(open, high, low, close, QDAYS), _realized_vol(close, QDAYS))).diff().diff().diff()


VOLATILITY_REGIME_AT_PEAK_D3_REGISTRY_001_075 = {
    "f10_vrap_001_rvol_63_pctrank_504d_d3": {"inputs": ["close"], "func": f10_vrap_001_rvol_63_pctrank_504d_d3},
    "f10_vrap_002_rvol_63_pctrank_1260d_d3": {"inputs": ["close"], "func": f10_vrap_002_rvol_63_pctrank_1260d_d3},
    "f10_vrap_003_rvol_252_pctrank_1260d_d3": {"inputs": ["close"], "func": f10_vrap_003_rvol_252_pctrank_1260d_d3},
    "f10_vrap_004_park_63_pctrank_504d_d3": {"inputs": ["high", "low"], "func": f10_vrap_004_park_63_pctrank_504d_d3},
    "f10_vrap_005_park_252_pctrank_1260d_d3": {"inputs": ["high", "low"], "func": f10_vrap_005_park_252_pctrank_1260d_d3},
    "f10_vrap_006_gk_63_pctrank_504d_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_006_gk_63_pctrank_504d_d3},
    "f10_vrap_007_yz_63_pctrank_504d_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_007_yz_63_pctrank_504d_d3},
    "f10_vrap_008_yz_252_pctrank_1260d_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_008_yz_252_pctrank_1260d_d3},
    "f10_vrap_009_atr_21_pctrank_504d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_009_atr_21_pctrank_504d_d3},
    "f10_vrap_010_atr_252_pctrank_1260d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_010_atr_252_pctrank_1260d_d3},
    "f10_vrap_011_dollar_volvol_pctrank_504d_d3": {"inputs": ["close", "volume"], "func": f10_vrap_011_dollar_volvol_pctrank_504d_d3},
    "f10_vrap_012_rvol_63_zscore_1260d_d3": {"inputs": ["close"], "func": f10_vrap_012_rvol_63_zscore_1260d_d3},
    "f10_vrap_013_park_63_zscore_1260d_d3": {"inputs": ["high", "low"], "func": f10_vrap_013_park_63_zscore_1260d_d3},
    "f10_vrap_014_rvol_252_zscore_1260d_d3": {"inputs": ["close"], "func": f10_vrap_014_rvol_252_zscore_1260d_d3},
    "f10_vrap_015_rvol_5_pctrank_252d_d3": {"inputs": ["close"], "func": f10_vrap_015_rvol_5_pctrank_252d_d3},
    "f10_vrap_016_rvol_21_pctrank_504d_d3": {"inputs": ["close"], "func": f10_vrap_016_rvol_21_pctrank_504d_d3},
    "f10_vrap_017_park_21_pctrank_252d_d3": {"inputs": ["high", "low"], "func": f10_vrap_017_park_21_pctrank_252d_d3},
    "f10_vrap_018_atr_63_pctrank_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_018_atr_63_pctrank_252d_d3},
    "f10_vrap_019_atr_21_zscore_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_019_atr_21_zscore_252d_d3},
    "f10_vrap_020_realized_var_63_pctrank_504d_d3": {"inputs": ["close"], "func": f10_vrap_020_realized_var_63_pctrank_504d_d3},
    "f10_vrap_021_sq_ret_autocorr_lag1_63d_d3": {"inputs": ["close"], "func": f10_vrap_021_sq_ret_autocorr_lag1_63d_d3},
    "f10_vrap_022_sq_ret_autocorr_lag5_63d_d3": {"inputs": ["close"], "func": f10_vrap_022_sq_ret_autocorr_lag5_63d_d3},
    "f10_vrap_023_sq_ret_autocorr_lag21_252d_d3": {"inputs": ["close"], "func": f10_vrap_023_sq_ret_autocorr_lag21_252d_d3},
    "f10_vrap_024_abs_ret_autocorr_lag1_63d_d3": {"inputs": ["close"], "func": f10_vrap_024_abs_ret_autocorr_lag1_63d_d3},
    "f10_vrap_025_abs_ret_autocorr_lag5_63d_d3": {"inputs": ["close"], "func": f10_vrap_025_abs_ret_autocorr_lag5_63d_d3},
    "f10_vrap_026_abs_ret_autocorr_lag21_252d_d3": {"inputs": ["close"], "func": f10_vrap_026_abs_ret_autocorr_lag21_252d_d3},
    "f10_vrap_027_garch_alpha_beta_proxy_252d_d3": {"inputs": ["close"], "func": f10_vrap_027_garch_alpha_beta_proxy_252d_d3},
    "f10_vrap_028_vol_persistence_halflife_63d_d3": {"inputs": ["close"], "func": f10_vrap_028_vol_persistence_halflife_63d_d3},
    "f10_vrap_029_volvol_autocorr_lag1_63d_d3": {"inputs": ["close"], "func": f10_vrap_029_volvol_autocorr_lag1_63d_d3},
    "f10_vrap_030_vol_meanrev_speed_proxy_63d_d3": {"inputs": ["close"], "func": f10_vrap_030_vol_meanrev_speed_proxy_63d_d3},
    "f10_vrap_031_long_memory_exponent_absret_252d_d3": {"inputs": ["close"], "func": f10_vrap_031_long_memory_exponent_absret_252d_d3},
    "f10_vrap_032_squared_ret_corr_with_vol_63d_d3": {"inputs": ["close"], "func": f10_vrap_032_squared_ret_corr_with_vol_63d_d3},
    "f10_vrap_033_clustering_score_intensity_63d_d3": {"inputs": ["close"], "func": f10_vrap_033_clustering_score_intensity_63d_d3},
    "f10_vrap_034_vol_acceleration_zscore_63d_d3": {"inputs": ["close"], "func": f10_vrap_034_vol_acceleration_zscore_63d_d3},
    "f10_vrap_035_vol_regime_change_count_252d_d3": {"inputs": ["close"], "func": f10_vrap_035_vol_regime_change_count_252d_d3},
    "f10_vrap_036_persistent_low_vol_streak_max_252d_d3": {"inputs": ["close"], "func": f10_vrap_036_persistent_low_vol_streak_max_252d_d3},
    "f10_vrap_037_persistent_high_vol_streak_max_252d_d3": {"inputs": ["close"], "func": f10_vrap_037_persistent_high_vol_streak_max_252d_d3},
    "f10_vrap_038_vol_change_corr_with_return_63d_d3": {"inputs": ["close"], "func": f10_vrap_038_vol_change_corr_with_return_63d_d3},
    "f10_vrap_039_volvol_pctrank_504d_d3": {"inputs": ["close"], "func": f10_vrap_039_volvol_pctrank_504d_d3},
    "f10_vrap_040_vol_clustering_index_intensity_252d_d3": {"inputs": ["close"], "func": f10_vrap_040_vol_clustering_index_intensity_252d_d3},
    "f10_vrap_041_downside_semivar_63d_d3": {"inputs": ["close"], "func": f10_vrap_041_downside_semivar_63d_d3},
    "f10_vrap_042_upside_semivar_63d_d3": {"inputs": ["close"], "func": f10_vrap_042_upside_semivar_63d_d3},
    "f10_vrap_043_semivar_ratio_down_up_63d_d3": {"inputs": ["close"], "func": f10_vrap_043_semivar_ratio_down_up_63d_d3},
    "f10_vrap_044_downside_semivar_252d_d3": {"inputs": ["close"], "func": f10_vrap_044_downside_semivar_252d_d3},
    "f10_vrap_045_upside_semivar_252d_d3": {"inputs": ["close"], "func": f10_vrap_045_upside_semivar_252d_d3},
    "f10_vrap_046_semivar_ratio_down_up_252d_d3": {"inputs": ["close"], "func": f10_vrap_046_semivar_ratio_down_up_252d_d3},
    "f10_vrap_047_leverage_effect_corr_63d_d3": {"inputs": ["close"], "func": f10_vrap_047_leverage_effect_corr_63d_d3},
    "f10_vrap_048_leverage_effect_corr_252d_d3": {"inputs": ["close"], "func": f10_vrap_048_leverage_effect_corr_252d_d3},
    "f10_vrap_049_down_move_vol_given_drawdown_5pct_d3": {"inputs": ["close"], "func": f10_vrap_049_down_move_vol_given_drawdown_5pct_d3},
    "f10_vrap_050_downside_deviation_minus_upside_dev_63d_d3": {"inputs": ["close"], "func": f10_vrap_050_downside_deviation_minus_upside_dev_63d_d3},
    "f10_vrap_051_vol_given_down_move_252d_d3": {"inputs": ["close"], "func": f10_vrap_051_vol_given_down_move_252d_d3},
    "f10_vrap_052_vol_given_up_move_252d_d3": {"inputs": ["close"], "func": f10_vrap_052_vol_given_up_move_252d_d3},
    "f10_vrap_053_asym_vol_response_ratio_252d_d3": {"inputs": ["close"], "func": f10_vrap_053_asym_vol_response_ratio_252d_d3},
    "f10_vrap_054_vol_skewness_distribution_63d_d3": {"inputs": ["close"], "func": f10_vrap_054_vol_skewness_distribution_63d_d3},
    "f10_vrap_055_pelaez_asym_vol_63d_d3": {"inputs": ["close"], "func": f10_vrap_055_pelaez_asym_vol_63d_d3},
    "f10_vrap_056_neg_ret_share_of_total_var_63d_d3": {"inputs": ["close"], "func": f10_vrap_056_neg_ret_share_of_total_var_63d_d3},
    "f10_vrap_057_pos_ret_share_of_total_var_63d_d3": {"inputs": ["close"], "func": f10_vrap_057_pos_ret_share_of_total_var_63d_d3},
    "f10_vrap_058_max_down_move_vs_max_up_move_252d_d3": {"inputs": ["close"], "func": f10_vrap_058_max_down_move_vs_max_up_move_252d_d3},
    "f10_vrap_059_downside_skew_63d_d3": {"inputs": ["close"], "func": f10_vrap_059_downside_skew_63d_d3},
    "f10_vrap_060_garch_asym_proxy_252d_d3": {"inputs": ["close"], "func": f10_vrap_060_garch_asym_proxy_252d_d3},
    "f10_vrap_061_yz_63_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_061_yz_63_d3},
    "f10_vrap_062_yz_252_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_062_yz_252_d3},
    "f10_vrap_063_yz_504_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_063_yz_504_d3},
    "f10_vrap_064_overnight_var_63d_d3": {"inputs": ["open", "close"], "func": f10_vrap_064_overnight_var_63d_d3},
    "f10_vrap_065_intraday_var_63d_d3": {"inputs": ["open", "close"], "func": f10_vrap_065_intraday_var_63d_d3},
    "f10_vrap_066_overnight_to_intraday_var_ratio_63d_d3": {"inputs": ["open", "close"], "func": f10_vrap_066_overnight_to_intraday_var_ratio_63d_d3},
    "f10_vrap_067_gap_share_of_total_var_252d_d3": {"inputs": ["open", "close"], "func": f10_vrap_067_gap_share_of_total_var_252d_d3},
    "f10_vrap_068_range_to_close_mean_ratio_63d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_068_range_to_close_mean_ratio_63d_d3},
    "f10_vrap_069_range_to_close_zscore_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_069_range_to_close_zscore_252d_d3},
    "f10_vrap_070_range_expansion_bar_count_252d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_070_range_expansion_bar_count_252d_d3},
    "f10_vrap_071_schwartz_smith_proxy_252d_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_071_schwartz_smith_proxy_252d_d3},
    "f10_vrap_072_intraday_vol_persistence_63d_d3": {"inputs": ["open", "close"], "func": f10_vrap_072_intraday_vol_persistence_63d_d3},
    "f10_vrap_073_range_truncation_index_21_63_d3": {"inputs": ["high", "low"], "func": f10_vrap_073_range_truncation_index_21_63_d3},
    "f10_vrap_074_park_to_realized_ratio_63d_d3": {"inputs": ["high", "low", "close"], "func": f10_vrap_074_park_to_realized_ratio_63d_d3},
    "f10_vrap_075_gk_to_realized_ratio_63d_d3": {"inputs": ["open", "high", "low", "close"], "func": f10_vrap_075_gk_to_realized_ratio_63d_d3},
}
