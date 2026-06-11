"""blowoff_climax_composite d1 features 376-450 — Pipeline 1b-technical.

75 distinct INDIVIDUAL signal hypotheses extending the 375 existing features.
Themes: Lee-Mykland / Aït-Sahalia-Jacod jumps / BNS bipower variation /
Bekaert-Engstrom leverage / GJR asymmetry / realized higher moments /
vol-term-structure cascades / anchoring / conditional vol asymmetry.

Inputs: SEP OHLCV. PIT-clean. Self-contained helpers.
"""
import numpy as np
import pandas as pd

YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504


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


def _true_range(high, low, close):
    pc = close.shift(1)
    return pd.concat([high - low, (high - pc).abs(), (low - pc).abs()], axis=1).max(axis=1)


def _atr(high, low, close, n=21):
    return _true_range(high, low, close).rolling(n, min_periods=max(n // 3, 2)).mean()


def _rolling_pct_rank(s, window, min_periods=None):
    if min_periods is None:
        min_periods = max(window // 3, 2)
    def _rk(w):
        if np.isnan(w).all():
            return np.nan
        last = w[-1]
        if np.isnan(last):
            return np.nan
        v = w[~np.isnan(w)]
        if v.size == 0:
            return np.nan
        return float((v <= last).sum()) / float(v.size)
    return s.rolling(window, min_periods=min_periods).apply(_rk, raw=True)


def f49_bcco_376_lee_mykland_L_stat_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)
    L = _safe_div(r.abs(), bpv.pow(0.5))
    out = L.rolling(252, min_periods=84).max()
    return out.diff()


def f49_bcco_377_lee_mykland_L_max_21d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)
    L = _safe_div(r.abs(), bpv.pow(0.5))
    out = L.rolling(21, min_periods=7).max()
    return out.diff()


def f49_bcco_378_lee_mykland_jump_count_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)
    L = _safe_div(r.abs(), bpv.pow(0.5))
    jump = (L > 4.6).astype(float).where(L.notna(), np.nan)
    out = jump.rolling(252, min_periods=84).sum()
    return out.diff()


def f49_bcco_379_asj_quarticity_over_var2_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    fourth = (r ** 4).rolling(63, min_periods=21).sum()
    var2 = (r ** 2).rolling(63, min_periods=21).sum() ** 2
    out = _safe_div(fourth, var2)
    return out.diff()


def f49_bcco_380_bns_bpv_over_rv_ratio_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bpv = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum() * (np.pi / 2.0)
    rv = (r ** 2).rolling(63, min_periods=21).sum()
    out = _safe_div(bpv, rv)
    return out.diff()


def f49_bcco_381_bns_jump_share_normalized_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bpv = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum() * (np.pi / 2.0)
    rv = (r ** 2).rolling(63, min_periods=21).sum()
    out = _safe_div((rv - bpv).clip(lower=0), rv)
    return out.diff()


def f49_bcco_382_bns_rj_test_zstat_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    n = 63.0
    bpv = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum() * (np.pi / 2.0)
    rv = (r ** 2).rolling(63, min_periods=21).sum()
    rq = (r ** 4).rolling(63, min_periods=21).sum() * (n / 3.0)
    mu1_2 = (np.pi / 2.0) ** 2
    theta = mu1_2 + np.pi - 5.0
    rj = (rv - bpv) / rv
    se = np.sqrt(theta * (rq / (bpv ** 2)) / n)
    out = _safe_div(rj, se)
    return out.diff()


def f49_bcco_383_bns_negative_jump_var_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    neg_jumps = (r ** 2).where(r < -2.0 * r.rolling(63, min_periods=21).std(), 0.0)
    out = neg_jumps.rolling(63, min_periods=21).sum()
    return out.diff()


def f49_bcco_384_bns_positive_jump_var_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    pos_jumps = (r ** 2).where(r > 2.0 * r.rolling(63, min_periods=21).std(), 0.0)
    out = pos_jumps.rolling(63, min_periods=21).sum()
    return out.diff()


def f49_bcco_385_neg_jump_share_of_total_jump_var_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    pos = (r ** 2).where(r > 2.0 * sd, 0.0).rolling(63, min_periods=21).sum()
    neg = (r ** 2).where(r < -2.0 * sd, 0.0).rolling(63, min_periods=21).sum()
    out = _safe_div(neg, neg + pos)
    return out.diff()


def f49_bcco_386_large_jump_4sigma_density_per_year_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    ev = (r.abs() > 4.0 * sd).astype(float).where(sd.notna(), np.nan)
    out = ev.rolling(252, min_periods=84).sum()
    return out.diff()


def f49_bcco_387_mean_gap_between_lm_jumps_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)
    L = _safe_div(r.abs(), bpv.pow(0.5))
    jump = (L > 4.6).astype(float).where(L.notna(), np.nan)
    def _f(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        idx = np.where(v > 0.5)[0]
        if idx.size < 2:
            return np.nan
        return float(np.mean(np.diff(idx)))
    out = jump.rolling(252, min_periods=84).apply(_f, raw=True)
    return out.diff()


def f49_bcco_388_jump_clustering_within_5d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    bpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)
    L = _safe_div(r.abs(), bpv.pow(0.5))
    jump = (L > 4.6).astype(float).where(L.notna(), np.nan)
    follows = jump * jump.shift(1).rolling(5, min_periods=1).max()
    out = follows.rolling(252, min_periods=84).sum() / jump.rolling(252, min_periods=84).sum().replace(0, np.nan)
    return out.diff()


def f49_bcco_389_bns_rj_zstat_above_2_indicator_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    n = 63.0
    bpv = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum() * (np.pi / 2.0)
    rv = (r ** 2).rolling(63, min_periods=21).sum()
    rq = (r ** 4).rolling(63, min_periods=21).sum() * (n / 3.0)
    theta = (np.pi / 2.0) ** 2 + np.pi - 5.0
    rj = (rv - bpv) / rv
    se = np.sqrt(theta * (rq / (bpv ** 2)) / n)
    z = _safe_div(rj, se)
    out = (z > 2.0).astype(float).where(z.notna(), np.nan)
    return out.diff()


def f49_bcco_390_jump_count_pos_minus_neg_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(63, min_periods=21).std()
    pos = (r > 3.0 * sd).astype(float).where(sd.notna(), np.nan).rolling(252, min_periods=84).sum()
    neg = (r < -3.0 * sd).astype(float).where(sd.notna(), np.nan).rolling(252, min_periods=84).sum()
    out = pos - neg
    return out.diff()


def f49_bcco_391_be_asym_vol_response_neg_shock_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = (r ** 2).rolling(21, min_periods=7).mean()
    neg = r.where(r < 0, 0.0)
    out = rv.rolling(252, min_periods=84).cov(neg ** 2) / (neg ** 2).rolling(252, min_periods=84).var().replace(0, np.nan)
    return out.diff()


def f49_bcco_392_gjr_asym_gamma_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = (r ** 2).rolling(5, min_periods=3).mean()
    neg_sq = (r.shift(1) ** 2).where(r.shift(1) < 0, 0.0)
    pos_sq = (r.shift(1) ** 2).where(r.shift(1) > 0, 0.0)
    # rv = a*pos_sq + (a+gamma)*neg_sq + ... approx via diff in coefficients
    cov_n = rv.rolling(252, min_periods=84).cov(neg_sq)
    cov_p = rv.rolling(252, min_periods=84).cov(pos_sq)
    var_n = neg_sq.rolling(252, min_periods=84).var().replace(0, np.nan)
    var_p = pos_sq.rolling(252, min_periods=84).var().replace(0, np.nan)
    out = _safe_div(cov_n, var_n) - _safe_div(cov_p, var_p)
    return out.diff()


def f49_bcco_393_return_to_future_vol_corr_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    fut_rv = r.rolling(21, min_periods=7).std().shift(21)
    out = r.rolling(252, min_periods=84).corr(fut_rv)
    return out.diff()


def f49_bcco_394_return_to_future_63d_vol_corr_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    fut_rv = r.rolling(63, min_periods=21).std().shift(63)
    out = r.rolling(252, min_periods=84).corr(fut_rv)
    return out.diff()


def f49_bcco_395_cond_vol_given_prior_up_minus_down_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv_up = r.where(r.shift(1) > 0, np.nan).rolling(252, min_periods=84).std()
    rv_dn = r.where(r.shift(1) < 0, np.nan).rolling(252, min_periods=84).std()
    out = rv_up - rv_dn
    return out.diff()


def f49_bcco_396_cond_vol_dn_over_up_ratio_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv_up = r.where(r.shift(1) > 0, np.nan).rolling(252, min_periods=84).std()
    rv_dn = r.where(r.shift(1) < 0, np.nan).rolling(252, min_periods=84).std()
    out = _safe_div(rv_dn, rv_up)
    return out.diff()


def f49_bcco_397_semivar_ratio_lag5_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lag5_neg = r.where(r.shift(5) < 0, np.nan)
    lag5_pos = r.where(r.shift(5) > 0, np.nan)
    sv_n = (lag5_neg ** 2).rolling(252, min_periods=84).mean()
    sv_p = (lag5_pos ** 2).rolling(252, min_periods=84).mean()
    out = _safe_div(sv_n, sv_p)
    return out.diff()


def f49_bcco_398_instant_leverage_cov_ret_dvar_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = (r ** 2).rolling(5, min_periods=3).mean()
    drv = rv - rv.shift(1)
    out = r.rolling(252, min_periods=84).cov(drv)
    return out.diff()


def f49_bcco_399_vol_feedback_cov_dsigma_to_next_ret_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = r.rolling(21, min_periods=7).std()
    drv = rv - rv.shift(1)
    out = drv.rolling(252, min_periods=84).cov(r.shift(1))
    return out.diff()


def f49_bcco_400_cond_kurt_given_neg_shock_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sd = r.rolling(252, min_periods=84).std()
    cond_r = r.where(r.shift(1) < -sd.shift(1), np.nan)
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); ss = v.std(ddof=1)
        if ss <= 0:
            return np.nan
        return float(np.mean(((v - m) / ss) ** 4) - 3.0)
    out = cond_r.rolling(252, min_periods=84).apply(_kt, raw=True)
    return out.diff()


def f49_bcco_401_sharpe_decay_21d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    sh21 = r.rolling(21, min_periods=7).mean() / r.rolling(21, min_periods=7).std().replace(0, np.nan)
    out = sh21 - sh21.rolling(252, min_periods=84).mean()
    return out.diff()


def f49_bcco_402_cond_mean_ret_high_vol_regime_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    cond_r = r.where(rv21 > med_rv, np.nan)
    out = cond_r.rolling(252, min_periods=84).mean()
    return out.diff()


def f49_bcco_403_cond_mean_ret_low_vol_regime_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    med_rv = rv21.rolling(252, min_periods=84).median()
    cond_r = r.where(rv21 < med_rv, np.nan)
    out = cond_r.rolling(252, min_periods=84).mean()
    return out.diff()


def f49_bcco_404_asym_vol_zscore_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv_up = r.where(r.shift(1) > 0, np.nan).rolling(252, min_periods=84).std()
    rv_dn = r.where(r.shift(1) < 0, np.nan).rolling(252, min_periods=84).std()
    spread = rv_dn - rv_up
    out = _rolling_zscore(spread, 504, min_periods=168)
    return out.diff()


def f49_bcco_405_vol_shock_half_life_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = (r ** 2).rolling(5, min_periods=3).mean()
    def _hl(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = (w[valid] if not valid.all() else w).astype(float)
        m = v.mean(); vc = v - m
        den = float((vc ** 2).sum())
        if den == 0:
            return np.nan
        rho = float((vc[1:] * vc[:-1]).sum() / den)
        if rho <= 0 or rho >= 1:
            return np.nan
        return float(-np.log(2) / np.log(rho))
    out = rv.rolling(252, min_periods=84).apply(_hl, raw=True)
    return out.diff()


def f49_bcco_406_realized_intraday_skew_OHLC_21d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 7:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3))
    out = intr.rolling(21, min_periods=7).apply(_sk, raw=True)
    return out.diff()


def f49_bcco_407_realized_intraday_skew_OHLC_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3))
    out = intr.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f49_bcco_408_realized_intraday_kurt_OHLC_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 4) - 3.0)
    out = intr.rolling(252, min_periods=84).apply(_kt, raw=True)
    return out.diff()


def f49_bcco_409_daily_vs_intraday_skew_agreement_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    day = _safe_log(close).diff()
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3))
    sk_intr = intr.rolling(252, min_periods=84).apply(_sk, raw=True)
    sk_day = day.rolling(252, min_periods=84).apply(_sk, raw=True)
    out = (np.sign(sk_intr) == np.sign(sk_day)).astype(float).where(sk_intr.notna() & sk_day.notna(), np.nan)
    return out.diff()


def f49_bcco_410_coskew_ret_vol_252d_d1(close: pd.Series, volume: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v = _safe_log(volume.replace(0, np.nan))
    r_dev = r - r.rolling(252, min_periods=84).mean()
    v_dev = v - v.rolling(252, min_periods=84).mean()
    out = (r_dev ** 2 * v_dev).rolling(252, min_periods=84).mean()
    return out.diff()


def f49_bcco_411_realized_quarticity_intraday_63d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    out = (intr ** 4).rolling(63, min_periods=21).sum()
    return out.diff()


def f49_bcco_412_realized_intraday_hyperskew_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    def _h(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 5))
    out = intr.rolling(252, min_periods=84).apply(_h, raw=True)
    return out.diff()


def f49_bcco_413_cokurt_intraday_with_lag1_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    intr_lag = intr.shift(1)
    m_r = intr.rolling(252, min_periods=84).mean()
    m_l = intr_lag.rolling(252, min_periods=84).mean()
    s_r = intr.rolling(252, min_periods=84).std()
    s_l = intr_lag.rolling(252, min_periods=84).std()
    x_r = intr - m_r; x_l = intr_lag - m_l
    ck = (x_r * x_r * x_l * x_l).rolling(252, min_periods=84).mean()
    out = _safe_div(ck, (s_r * s_r * s_l * s_l))
    return out.diff()


def f49_bcco_414_realized_signed_jump_intraday_pos_63d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    sd = intr.rolling(63, min_periods=21).std()
    pos = (intr ** 2).where(intr > 2.0 * sd, 0.0)
    out = pos.rolling(63, min_periods=21).sum()
    return out.diff()


def f49_bcco_415_realized_signed_jump_intraday_neg_63d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    sd = intr.rolling(63, min_periods=21).std()
    neg = (intr ** 2).where(intr < -2.0 * sd, 0.0)
    out = neg.rolling(63, min_periods=21).sum()
    return out.diff()


def f49_bcco_416_intraday_vol_of_vol_63d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    rv5 = intr.rolling(5, min_periods=3).std()
    out = rv5.rolling(63, min_periods=21).std()
    return out.diff()


def f49_bcco_417_cross_oc_hl_corr_63d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    oc = _safe_log(close) - _safe_log(open)
    hl = _safe_log(high) - _safe_log(low)
    out = oc.rolling(63, min_periods=21).corr(hl)
    return out.diff()


def f49_bcco_418_realized_intraday_skew_squared_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3) ** 2)
    out = intr.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f49_bcco_419_realized_skew_log_hl_252d_d1(high: pd.Series, low: pd.Series) -> pd.Series:
    hl = _safe_log(high) - _safe_log(low)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3))
    out = hl.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f49_bcco_420_intraday_skew_sq_plus_kurt_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    tp = (high + low + close) / 3.0
    intr = _safe_log(tp) - _safe_log(open)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3))
    def _kt(w):
        valid = ~np.isnan(w)
        if valid.sum() < 30:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 4) - 3.0)
    sk = intr.rolling(252, min_periods=84).apply(_sk, raw=True)
    kt = intr.rolling(252, min_periods=84).apply(_kt, raw=True)
    out = sk ** 2 + kt
    return out.diff()


def f49_bcco_421_rv_5d_over_21d_ratio_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = _safe_div(r.rolling(5, min_periods=3).std(), r.rolling(21, min_periods=7).std())
    return out.diff()


def f49_bcco_422_rv_21d_over_63d_ratio_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = _safe_div(r.rolling(21, min_periods=7).std(), r.rolling(63, min_periods=21).std())
    return out.diff()


def f49_bcco_423_rv_63d_over_252d_ratio_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    out = _safe_div(r.rolling(63, min_periods=21).std(), r.rolling(252, min_periods=84).std())
    return out.diff()


def f49_bcco_424_vol_term_structure_slope_3pt_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v5 = r.rolling(5, min_periods=3).std()
    v21 = r.rolling(21, min_periods=7).std()
    v63 = r.rolling(63, min_periods=21).std()
    x = np.log([5.0, 21.0, 63.0])
    lv5 = _safe_log(v5); lv21 = _safe_log(v21); lv63 = _safe_log(v63)
    stk = pd.concat([lv5.rename(0), lv21.rename(1), lv63.rename(2)], axis=1)
    def _slope(row):
        a = row.values
        if np.isnan(a).any():
            return np.nan
        xm = x.mean(); ym = a.mean()
        den = float(((x - xm) ** 2).sum())
        if den == 0:
            return np.nan
        return float(((x - xm) * (a - ym)).sum() / den)
    out = stk.apply(_slope, axis=1)
    return out.diff()


def f49_bcco_425_vol_term_inversion_21d_above_63d_indicator_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v21 = r.rolling(21, min_periods=7).std()
    v63 = r.rolling(63, min_periods=21).std()
    out = (v21 > v63).astype(float).where(v63.notna(), np.nan)
    return out.diff()


def f49_bcco_426_vol_of_vol_of_vol_63d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = r.rolling(5, min_periods=3).std()
    vov = rv.rolling(21, min_periods=7).std()
    out = vov.rolling(63, min_periods=21).std()
    return out.diff()


def f49_bcco_427_vol_decay_log_log_slope_21_252_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v21 = r.rolling(21, min_periods=7).std()
    v252 = r.rolling(252, min_periods=84).std()
    ratio = _safe_log(_safe_div(v21, v252))
    out = ratio / np.log(21.0 / 252.0)
    return out.diff()


def f49_bcco_428_log_vol_shift_above_05_event_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v21 = r.rolling(21, min_periods=7).std()
    lv = _safe_log(v21)
    out = ((lv - lv.shift(21)).abs() > 0.5).astype(float).where(lv.shift(21).notna(), np.nan).rolling(252, min_periods=84).sum()
    return out.diff()


def f49_bcco_429_log_vol_corr_5d_63d_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lv5 = _safe_log(r.rolling(5, min_periods=3).std())
    lv63 = _safe_log(r.rolling(63, min_periods=21).std())
    out = lv5.rolling(252, min_periods=84).corr(lv63)
    return out.diff()


def f49_bcco_430_vol_term_curve_concavity_2nd_diff_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lv5 = _safe_log(r.rolling(5, min_periods=3).std())
    lv21 = _safe_log(r.rolling(21, min_periods=7).std())
    lv63 = _safe_log(r.rolling(63, min_periods=21).std())
    out = lv5 - 2.0 * lv21 + lv63
    return out.diff()


def f49_bcco_431_cross_horizon_vol_spike_density_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    z5 = _rolling_zscore(r.rolling(5, min_periods=3).std(), 252, min_periods=84)
    z21 = _rolling_zscore(r.rolling(21, min_periods=7).std(), 252, min_periods=84)
    z63 = _rolling_zscore(r.rolling(63, min_periods=21).std(), 252, min_periods=84)
    spike = ((z5 > 1.5).astype(float) + (z21 > 1.5).astype(float) + (z63 > 1.5).astype(float)).rolling(252, min_periods=84).sum()
    out = spike
    return out.diff()


def f49_bcco_432_vol_of_vol_21d_zscore_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv21 = r.rolling(21, min_periods=7).std()
    vov = rv21.rolling(21, min_periods=7).std()
    out = _rolling_zscore(vov, 252, min_periods=84)
    return out.diff()


def f49_bcco_433_vol_of_vol_accel_21d_in_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = r.rolling(21, min_periods=7).std()
    vov = rv.rolling(21, min_periods=7).std()
    out = vov - vov.shift(21)
    return out.diff()


def f49_bcco_434_vol_curve_max_minus_min_4pt_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    v5 = r.rolling(5, min_periods=3).std()
    v21 = r.rolling(21, min_periods=7).std()
    v63 = r.rolling(63, min_periods=21).std()
    v252 = r.rolling(252, min_periods=84).std()
    stk = pd.concat([v5.rename(0), v21.rename(1), v63.rename(2), v252.rename(3)], axis=1)
    out = stk.max(axis=1) - stk.min(axis=1)
    return out.diff()


def f49_bcco_435_vol_curve_slope_sign_flip_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lv21 = _safe_log(r.rolling(21, min_periods=7).std())
    lv63 = _safe_log(r.rolling(63, min_periods=21).std())
    slope = lv21 - lv63
    sg = np.sign(slope)
    out = (sg != sg.shift(21)).astype(float).where(sg.notna() & sg.shift(21).notna(), np.nan).rolling(252, min_periods=84).sum()
    return out.diff()


def f49_bcco_436_anchor_distance_to_52w_high_pct_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    out = _safe_div(rmax - close, rmax)
    return out.diff()


def f49_bcco_437_anchor_distance_to_52w_low_pct_d1(low: pd.Series, close: pd.Series) -> pd.Series:
    rmin = low.rolling(252, min_periods=84).min()
    out = _safe_div(close - rmin, close)
    return out.diff()


def f49_bcco_438_round_5dollar_attraction_freq_252d_d1(close: pd.Series) -> pd.Series:
    remainder = (close - (close / 5.0).round() * 5.0).abs()
    near = (remainder < 0.05).astype(float).where(close.notna(), np.nan)
    out = near.rolling(252, min_periods=84).mean()
    return out.diff()


def f49_bcco_439_round_dollar_rejection_freq_252d_d1(close: pd.Series) -> pd.Series:
    cents = (close * 100.0).round().astype(float)
    at_round = ((cents % 100) == 0).astype(float)
    down_next = (close.shift(1) < close).astype(float)
    rej = at_round * down_next
    out = rej.rolling(252, min_periods=84).mean()
    return out.diff()


def f49_bcco_440_anchor_distance_to_21d_prior_high_pct_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax21 = high.shift(21).rolling(21, min_periods=7).max()
    out = _safe_div(rmax21 - close, rmax21)
    return out.diff()


def f49_bcco_441_anchor_distance_to_21d_prior_close_pct_d1(close: pd.Series) -> pd.Series:
    out = _safe_div(close - close.shift(21), close.shift(21))
    return out.diff()


def f49_bcco_442_cond_skew_given_21d_up_trend_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ret21 = _safe_log(close).diff(21)
    cond_r = r.where(ret21 > 0, np.nan)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3))
    out = cond_r.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f49_bcco_443_cond_skew_given_21d_down_trend_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ret21 = _safe_log(close).diff(21)
    cond_r = r.where(ret21 < 0, np.nan)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3))
    out = cond_r.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f49_bcco_444_cond_skew_up_minus_down_regime_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    ret21 = _safe_log(close).diff(21)
    up = r.where(ret21 > 0, np.nan)
    dn = r.where(ret21 < 0, np.nan)
    def _sk(w):
        valid = ~np.isnan(w)
        if valid.sum() < 10:
            return np.nan
        v = w[valid]
        m = v.mean(); s = v.std(ddof=1)
        if s <= 0:
            return np.nan
        return float(np.mean(((v - m) / s) ** 3))
    out = up.rolling(252, min_periods=84).apply(_sk, raw=True) - dn.rolling(252, min_periods=84).apply(_sk, raw=True)
    return out.diff()


def f49_bcco_445_max_dd_from_21d_high_decay_5d_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax21 = high.rolling(21, min_periods=7).max()
    dd = _safe_log(rmax21) - _safe_log(close)
    out = (dd - dd.shift(5)).rolling(252, min_periods=84).max()
    return out.diff()


def f49_bcco_446_pos_vs_neg_vol_shock_count_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rv = r.rolling(5, min_periods=3).std()
    drv = rv - rv.shift(5)
    z = _rolling_zscore(drv, 252, min_periods=84)
    pos = (z > 2.0).astype(float).where(z.notna(), np.nan).rolling(252, min_periods=84).sum()
    neg = (z < -2.0).astype(float).where(z.notna(), np.nan).rolling(252, min_periods=84).sum()
    out = pos - neg
    return out.diff()


def f49_bcco_447_drift_away_from_252d_high_63d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    rmax = high.rolling(252, min_periods=84).max()
    dist = _safe_div(rmax - close, rmax)
    out = dist - dist.shift(63)
    return out.diff()


def f49_bcco_448_cond_vol_given_large_down_at_252d_high_252d_d1(high: pd.Series, close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    rmax = high.rolling(252, min_periods=84).max()
    at_high = (high >= 0.95 * rmax).astype(bool)
    sd = r.rolling(63, min_periods=21).std()
    large_dn = r.where((r < -2.0 * sd) & at_high, np.nan)
    out = large_dn.rolling(252, min_periods=84).std()
    return out.diff()


def f49_bcco_449_idiosyncratic_vol_proxy_252d_d1(close: pd.Series) -> pd.Series:
    r = _safe_log(close).diff()
    lag5 = _safe_log(close).diff(5).shift(1)
    b = r.rolling(252, min_periods=84).cov(lag5) / lag5.rolling(252, min_periods=84).var().replace(0, np.nan)
    resid = r - b * lag5
    out = resid.rolling(252, min_periods=84).std()
    return out.diff()


def f49_bcco_450_max_bar_return_over_range_252d_d1(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    bar_ret = (_safe_log(close) - _safe_log(open)).abs()
    bar_rng = _safe_log(high) - _safe_log(low)
    eff = _safe_div(bar_ret, bar_rng)
    out = eff.rolling(252, min_periods=84).max()
    return out.diff()


# ============================================================
#                         REGISTRY 376_450 (d1)
# ============================================================

BLOWOFF_CLIMAX_COMPOSITE_D1_REGISTRY_376_450 = {
    "f49_bcco_376_lee_mykland_L_stat_252d_d1": {"inputs": ["close"], "func": f49_bcco_376_lee_mykland_L_stat_252d_d1},
    "f49_bcco_377_lee_mykland_L_max_21d_d1": {"inputs": ["close"], "func": f49_bcco_377_lee_mykland_L_max_21d_d1},
    "f49_bcco_378_lee_mykland_jump_count_252d_d1": {"inputs": ["close"], "func": f49_bcco_378_lee_mykland_jump_count_252d_d1},
    "f49_bcco_379_asj_quarticity_over_var2_63d_d1": {"inputs": ["close"], "func": f49_bcco_379_asj_quarticity_over_var2_63d_d1},
    "f49_bcco_380_bns_bpv_over_rv_ratio_63d_d1": {"inputs": ["close"], "func": f49_bcco_380_bns_bpv_over_rv_ratio_63d_d1},
    "f49_bcco_381_bns_jump_share_normalized_63d_d1": {"inputs": ["close"], "func": f49_bcco_381_bns_jump_share_normalized_63d_d1},
    "f49_bcco_382_bns_rj_test_zstat_63d_d1": {"inputs": ["close"], "func": f49_bcco_382_bns_rj_test_zstat_63d_d1},
    "f49_bcco_383_bns_negative_jump_var_63d_d1": {"inputs": ["close"], "func": f49_bcco_383_bns_negative_jump_var_63d_d1},
    "f49_bcco_384_bns_positive_jump_var_63d_d1": {"inputs": ["close"], "func": f49_bcco_384_bns_positive_jump_var_63d_d1},
    "f49_bcco_385_neg_jump_share_of_total_jump_var_63d_d1": {"inputs": ["close"], "func": f49_bcco_385_neg_jump_share_of_total_jump_var_63d_d1},
    "f49_bcco_386_large_jump_4sigma_density_per_year_252d_d1": {"inputs": ["close"], "func": f49_bcco_386_large_jump_4sigma_density_per_year_252d_d1},
    "f49_bcco_387_mean_gap_between_lm_jumps_252d_d1": {"inputs": ["close"], "func": f49_bcco_387_mean_gap_between_lm_jumps_252d_d1},
    "f49_bcco_388_jump_clustering_within_5d_252d_d1": {"inputs": ["close"], "func": f49_bcco_388_jump_clustering_within_5d_252d_d1},
    "f49_bcco_389_bns_rj_zstat_above_2_indicator_63d_d1": {"inputs": ["close"], "func": f49_bcco_389_bns_rj_zstat_above_2_indicator_63d_d1},
    "f49_bcco_390_jump_count_pos_minus_neg_252d_d1": {"inputs": ["close"], "func": f49_bcco_390_jump_count_pos_minus_neg_252d_d1},
    "f49_bcco_391_be_asym_vol_response_neg_shock_252d_d1": {"inputs": ["close"], "func": f49_bcco_391_be_asym_vol_response_neg_shock_252d_d1},
    "f49_bcco_392_gjr_asym_gamma_proxy_252d_d1": {"inputs": ["close"], "func": f49_bcco_392_gjr_asym_gamma_proxy_252d_d1},
    "f49_bcco_393_return_to_future_vol_corr_252d_d1": {"inputs": ["close"], "func": f49_bcco_393_return_to_future_vol_corr_252d_d1},
    "f49_bcco_394_return_to_future_63d_vol_corr_252d_d1": {"inputs": ["close"], "func": f49_bcco_394_return_to_future_63d_vol_corr_252d_d1},
    "f49_bcco_395_cond_vol_given_prior_up_minus_down_252d_d1": {"inputs": ["close"], "func": f49_bcco_395_cond_vol_given_prior_up_minus_down_252d_d1},
    "f49_bcco_396_cond_vol_dn_over_up_ratio_252d_d1": {"inputs": ["close"], "func": f49_bcco_396_cond_vol_dn_over_up_ratio_252d_d1},
    "f49_bcco_397_semivar_ratio_lag5_252d_d1": {"inputs": ["close"], "func": f49_bcco_397_semivar_ratio_lag5_252d_d1},
    "f49_bcco_398_instant_leverage_cov_ret_dvar_252d_d1": {"inputs": ["close"], "func": f49_bcco_398_instant_leverage_cov_ret_dvar_252d_d1},
    "f49_bcco_399_vol_feedback_cov_dsigma_to_next_ret_252d_d1": {"inputs": ["close"], "func": f49_bcco_399_vol_feedback_cov_dsigma_to_next_ret_252d_d1},
    "f49_bcco_400_cond_kurt_given_neg_shock_252d_d1": {"inputs": ["close"], "func": f49_bcco_400_cond_kurt_given_neg_shock_252d_d1},
    "f49_bcco_401_sharpe_decay_21d_in_252d_d1": {"inputs": ["close"], "func": f49_bcco_401_sharpe_decay_21d_in_252d_d1},
    "f49_bcco_402_cond_mean_ret_high_vol_regime_252d_d1": {"inputs": ["close"], "func": f49_bcco_402_cond_mean_ret_high_vol_regime_252d_d1},
    "f49_bcco_403_cond_mean_ret_low_vol_regime_252d_d1": {"inputs": ["close"], "func": f49_bcco_403_cond_mean_ret_low_vol_regime_252d_d1},
    "f49_bcco_404_asym_vol_zscore_252d_d1": {"inputs": ["close"], "func": f49_bcco_404_asym_vol_zscore_252d_d1},
    "f49_bcco_405_vol_shock_half_life_252d_d1": {"inputs": ["close"], "func": f49_bcco_405_vol_shock_half_life_252d_d1},
    "f49_bcco_406_realized_intraday_skew_OHLC_21d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_406_realized_intraday_skew_OHLC_21d_d1},
    "f49_bcco_407_realized_intraday_skew_OHLC_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_407_realized_intraday_skew_OHLC_252d_d1},
    "f49_bcco_408_realized_intraday_kurt_OHLC_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_408_realized_intraday_kurt_OHLC_252d_d1},
    "f49_bcco_409_daily_vs_intraday_skew_agreement_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_409_daily_vs_intraday_skew_agreement_252d_d1},
    "f49_bcco_410_coskew_ret_vol_252d_d1": {"inputs": ["close", "volume"], "func": f49_bcco_410_coskew_ret_vol_252d_d1},
    "f49_bcco_411_realized_quarticity_intraday_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_411_realized_quarticity_intraday_63d_d1},
    "f49_bcco_412_realized_intraday_hyperskew_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_412_realized_intraday_hyperskew_252d_d1},
    "f49_bcco_413_cokurt_intraday_with_lag1_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_413_cokurt_intraday_with_lag1_252d_d1},
    "f49_bcco_414_realized_signed_jump_intraday_pos_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_414_realized_signed_jump_intraday_pos_63d_d1},
    "f49_bcco_415_realized_signed_jump_intraday_neg_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_415_realized_signed_jump_intraday_neg_63d_d1},
    "f49_bcco_416_intraday_vol_of_vol_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_416_intraday_vol_of_vol_63d_d1},
    "f49_bcco_417_cross_oc_hl_corr_63d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_417_cross_oc_hl_corr_63d_d1},
    "f49_bcco_418_realized_intraday_skew_squared_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_418_realized_intraday_skew_squared_252d_d1},
    "f49_bcco_419_realized_skew_log_hl_252d_d1": {"inputs": ["high", "low"], "func": f49_bcco_419_realized_skew_log_hl_252d_d1},
    "f49_bcco_420_intraday_skew_sq_plus_kurt_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_420_intraday_skew_sq_plus_kurt_252d_d1},
    "f49_bcco_421_rv_5d_over_21d_ratio_d1": {"inputs": ["close"], "func": f49_bcco_421_rv_5d_over_21d_ratio_d1},
    "f49_bcco_422_rv_21d_over_63d_ratio_d1": {"inputs": ["close"], "func": f49_bcco_422_rv_21d_over_63d_ratio_d1},
    "f49_bcco_423_rv_63d_over_252d_ratio_d1": {"inputs": ["close"], "func": f49_bcco_423_rv_63d_over_252d_ratio_d1},
    "f49_bcco_424_vol_term_structure_slope_3pt_252d_d1": {"inputs": ["close"], "func": f49_bcco_424_vol_term_structure_slope_3pt_252d_d1},
    "f49_bcco_425_vol_term_inversion_21d_above_63d_indicator_d1": {"inputs": ["close"], "func": f49_bcco_425_vol_term_inversion_21d_above_63d_indicator_d1},
    "f49_bcco_426_vol_of_vol_of_vol_63d_d1": {"inputs": ["close"], "func": f49_bcco_426_vol_of_vol_of_vol_63d_d1},
    "f49_bcco_427_vol_decay_log_log_slope_21_252_d1": {"inputs": ["close"], "func": f49_bcco_427_vol_decay_log_log_slope_21_252_d1},
    "f49_bcco_428_log_vol_shift_above_05_event_252d_d1": {"inputs": ["close"], "func": f49_bcco_428_log_vol_shift_above_05_event_252d_d1},
    "f49_bcco_429_log_vol_corr_5d_63d_252d_d1": {"inputs": ["close"], "func": f49_bcco_429_log_vol_corr_5d_63d_252d_d1},
    "f49_bcco_430_vol_term_curve_concavity_2nd_diff_d1": {"inputs": ["close"], "func": f49_bcco_430_vol_term_curve_concavity_2nd_diff_d1},
    "f49_bcco_431_cross_horizon_vol_spike_density_252d_d1": {"inputs": ["close"], "func": f49_bcco_431_cross_horizon_vol_spike_density_252d_d1},
    "f49_bcco_432_vol_of_vol_21d_zscore_252d_d1": {"inputs": ["close"], "func": f49_bcco_432_vol_of_vol_21d_zscore_252d_d1},
    "f49_bcco_433_vol_of_vol_accel_21d_in_252d_d1": {"inputs": ["close"], "func": f49_bcco_433_vol_of_vol_accel_21d_in_252d_d1},
    "f49_bcco_434_vol_curve_max_minus_min_4pt_d1": {"inputs": ["close"], "func": f49_bcco_434_vol_curve_max_minus_min_4pt_d1},
    "f49_bcco_435_vol_curve_slope_sign_flip_252d_d1": {"inputs": ["close"], "func": f49_bcco_435_vol_curve_slope_sign_flip_252d_d1},
    "f49_bcco_436_anchor_distance_to_52w_high_pct_d1": {"inputs": ["high", "close"], "func": f49_bcco_436_anchor_distance_to_52w_high_pct_d1},
    "f49_bcco_437_anchor_distance_to_52w_low_pct_d1": {"inputs": ["low", "close"], "func": f49_bcco_437_anchor_distance_to_52w_low_pct_d1},
    "f49_bcco_438_round_5dollar_attraction_freq_252d_d1": {"inputs": ["close"], "func": f49_bcco_438_round_5dollar_attraction_freq_252d_d1},
    "f49_bcco_439_round_dollar_rejection_freq_252d_d1": {"inputs": ["close"], "func": f49_bcco_439_round_dollar_rejection_freq_252d_d1},
    "f49_bcco_440_anchor_distance_to_21d_prior_high_pct_d1": {"inputs": ["high", "close"], "func": f49_bcco_440_anchor_distance_to_21d_prior_high_pct_d1},
    "f49_bcco_441_anchor_distance_to_21d_prior_close_pct_d1": {"inputs": ["close"], "func": f49_bcco_441_anchor_distance_to_21d_prior_close_pct_d1},
    "f49_bcco_442_cond_skew_given_21d_up_trend_252d_d1": {"inputs": ["close"], "func": f49_bcco_442_cond_skew_given_21d_up_trend_252d_d1},
    "f49_bcco_443_cond_skew_given_21d_down_trend_252d_d1": {"inputs": ["close"], "func": f49_bcco_443_cond_skew_given_21d_down_trend_252d_d1},
    "f49_bcco_444_cond_skew_up_minus_down_regime_252d_d1": {"inputs": ["close"], "func": f49_bcco_444_cond_skew_up_minus_down_regime_252d_d1},
    "f49_bcco_445_max_dd_from_21d_high_decay_5d_252d_d1": {"inputs": ["high", "close"], "func": f49_bcco_445_max_dd_from_21d_high_decay_5d_252d_d1},
    "f49_bcco_446_pos_vs_neg_vol_shock_count_252d_d1": {"inputs": ["close"], "func": f49_bcco_446_pos_vs_neg_vol_shock_count_252d_d1},
    "f49_bcco_447_drift_away_from_252d_high_63d_d1": {"inputs": ["high", "close"], "func": f49_bcco_447_drift_away_from_252d_high_63d_d1},
    "f49_bcco_448_cond_vol_given_large_down_at_252d_high_252d_d1": {"inputs": ["high", "close"], "func": f49_bcco_448_cond_vol_given_large_down_at_252d_high_252d_d1},
    "f49_bcco_449_idiosyncratic_vol_proxy_252d_d1": {"inputs": ["close"], "func": f49_bcco_449_idiosyncratic_vol_proxy_252d_d1},
    "f49_bcco_450_max_bar_return_over_range_252d_d1": {"inputs": ["open", "high", "low", "close"], "func": f49_bcco_450_max_bar_return_over_range_252d_d1},
}
