"""Generator EXTENSION for 49_blowoff_climax_composite (376-450).

Produces 4 new files: base/d1/d2/d3 x (376-450). 75 distinct INDIVIDUAL signals
targeting concepts NOT in the 375 existing features (mostly composites,
fractal-highs, momentum-at-peak combos).

INDIVIDUAL SIGNAL focus: each is ONE clean calculation, distinct math, not
a multi-criteria score.

Themes:
- Lee-Mykland jump-test statistic (formal jump test)
- Aït-Sahalia-Jacod jump-test (multipower variation ratio)
- BNS jump-variation (bipower vs realized) — log-form
- Bekaert-Engstrom asymmetric volatility-feedback regression
- GJR-GARCH asymmetric leverage indicator
- Realized higher-moments from intraday OHLC
- Vol-term-structure cascade slopes
- Anchoring proxies (52w-high distance, round-cents clustering)
- Conditional vol asymmetry up vs down (Wright-style)
"""
import os

ROOT = r"C:\Users\jyama\Desktop\short_technical_features_1b\49_blowoff_climax_composite"

HEADER_FMT = '''"""blowoff_climax_composite {order} features {lo:03d}-{hi:03d} — Pipeline 1b-technical.

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
'''

FEATS = []


def add(idx, suffix, inputs, body):
    lines = []
    for ln in body.splitlines():
        if ln.strip() == "":
            lines.append("")
        else:
            lines.append("    " + ln)
    FEATS.append((idx, suffix, inputs, "\n".join(lines)))


# ==================================================================
# Group A (376-390) — Lee-Mykland & Aït-Sahalia-Jacod jump tests
# ==================================================================

# 376 Lee-Mykland L stat: r_t / sqrt(bipower-var_(t-K,t-1))
add(376, "lee_mykland_L_stat_252d", "close",
    "r = _safe_log(close).diff()\nbpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)\nL = _safe_div(r.abs(), bpv.pow(0.5))\nout = L.rolling(252, min_periods=84).max()\n")

# 377 Lee-Mykland L stat max in 21d (jump-density proxy)
add(377, "lee_mykland_L_max_21d", "close",
    "r = _safe_log(close).diff()\nbpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)\nL = _safe_div(r.abs(), bpv.pow(0.5))\nout = L.rolling(21, min_periods=7).max()\n")

# 378 Lee-Mykland L > 4.6 (jump threshold ~95% bound for L stat) count 252d
add(378, "lee_mykland_jump_count_252d", "close",
    "r = _safe_log(close).diff()\nbpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)\nL = _safe_div(r.abs(), bpv.pow(0.5))\njump = (L > 4.6).astype(float).where(L.notna(), np.nan)\nout = jump.rolling(252, min_periods=84).sum()\n")

# 379 Aït-Sahalia-Jacod ratio: realized-fourth-power / (realized-variance^2)
add(379, "asj_quarticity_over_var2_63d", "close",
    "r = _safe_log(close).diff()\nfourth = (r ** 4).rolling(63, min_periods=21).sum()\nvar2 = (r ** 2).rolling(63, min_periods=21).sum() ** 2\nout = _safe_div(fourth, var2)\n")

# 380 BNS bipower-vs-realized variance ratio (formal jump detection)
add(380, "bns_bpv_over_rv_ratio_63d", "close",
    "r = _safe_log(close).diff()\nbpv = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum() * (np.pi / 2.0)\nrv = (r ** 2).rolling(63, min_periods=21).sum()\nout = _safe_div(bpv, rv)\n")

# 381 BNS jump component (rv - bpv) normalized 63d
add(381, "bns_jump_share_normalized_63d", "close",
    "r = _safe_log(close).diff()\nbpv = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum() * (np.pi / 2.0)\nrv = (r ** 2).rolling(63, min_periods=21).sum()\nout = _safe_div((rv - bpv).clip(lower=0), rv)\n")

# 382 BNS jump test Z-statistic (BNS-RJ)
add(382, "bns_rj_test_zstat_63d", "close",
    "r = _safe_log(close).diff()\nn = 63.0\nbpv = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum() * (np.pi / 2.0)\nrv = (r ** 2).rolling(63, min_periods=21).sum()\nrq = (r ** 4).rolling(63, min_periods=21).sum() * (n / 3.0)\nmu1_2 = (np.pi / 2.0) ** 2\ntheta = mu1_2 + np.pi - 5.0\nrj = (rv - bpv) / rv\nse = np.sqrt(theta * (rq / (bpv ** 2)) / n)\nout = _safe_div(rj, se)\n")

# 383 negative-jump-only (downside) BNS variation 63d
add(383, "bns_negative_jump_var_63d", "close",
    "r = _safe_log(close).diff()\nneg_jumps = (r ** 2).where(r < -2.0 * r.rolling(63, min_periods=21).std(), 0.0)\nout = neg_jumps.rolling(63, min_periods=21).sum()\n")

# 384 positive-jump variation 63d
add(384, "bns_positive_jump_var_63d", "close",
    "r = _safe_log(close).diff()\npos_jumps = (r ** 2).where(r > 2.0 * r.rolling(63, min_periods=21).std(), 0.0)\nout = pos_jumps.rolling(63, min_periods=21).sum()\n")

# 385 negative-jump-share over total jump variation 63d (downside-jump dominance)
add(385, "neg_jump_share_of_total_jump_var_63d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\npos = (r ** 2).where(r > 2.0 * sd, 0.0).rolling(63, min_periods=21).sum()\nneg = (r ** 2).where(r < -2.0 * sd, 0.0).rolling(63, min_periods=21).sum()\nout = _safe_div(neg, neg + pos)\n")

# 386 large-jump-density per day (jumps > 4σ) 252d
add(386, "large_jump_4sigma_density_per_year_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\nev = (r.abs() > 4.0 * sd).astype(float).where(sd.notna(), np.nan)\nout = ev.rolling(252, min_periods=84).sum()\n")

# 387 time-between-jumps (Lee-Mykland L>4.6) mean gap 252d
add(387, "mean_gap_between_lm_jumps_252d", "close",
    "r = _safe_log(close).diff()\nbpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)\nL = _safe_div(r.abs(), bpv.pow(0.5))\njump = (L > 4.6).astype(float).where(L.notna(), np.nan)\ndef _f(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = (w[valid] if not valid.all() else w).astype(float)\n    idx = np.where(v > 0.5)[0]\n    if idx.size < 2:\n        return np.nan\n    return float(np.mean(np.diff(idx)))\nout = jump.rolling(252, min_periods=84).apply(_f, raw=True)\n")

# 388 jump-clustering coefficient (jumps within 5d of prior jump / total jumps)
add(388, "jump_clustering_within_5d_252d", "close",
    "r = _safe_log(close).diff()\nbpv = (r.abs() * r.shift(1).abs()).rolling(21, min_periods=7).mean() * (np.pi / 2.0)\nL = _safe_div(r.abs(), bpv.pow(0.5))\njump = (L > 4.6).astype(float).where(L.notna(), np.nan)\nfollows = jump * jump.shift(1).rolling(5, min_periods=1).max()\nout = follows.rolling(252, min_periods=84).sum() / jump.rolling(252, min_periods=84).sum().replace(0, np.nan)\n")

# 389 BNS RJ-Z above 2 (jump regime indicator)
add(389, "bns_rj_zstat_above_2_indicator_63d", "close",
    "r = _safe_log(close).diff()\nn = 63.0\nbpv = (r.abs() * r.shift(1).abs()).rolling(63, min_periods=21).sum() * (np.pi / 2.0)\nrv = (r ** 2).rolling(63, min_periods=21).sum()\nrq = (r ** 4).rolling(63, min_periods=21).sum() * (n / 3.0)\ntheta = (np.pi / 2.0) ** 2 + np.pi - 5.0\nrj = (rv - bpv) / rv\nse = np.sqrt(theta * (rq / (bpv ** 2)) / n)\nz = _safe_div(rj, se)\nout = (z > 2.0).astype(float).where(z.notna(), np.nan)\n")

# 390 jump-direction-asymmetry: pos-jumps - neg-jumps count 252d
add(390, "jump_count_pos_minus_neg_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(63, min_periods=21).std()\npos = (r > 3.0 * sd).astype(float).where(sd.notna(), np.nan).rolling(252, min_periods=84).sum()\nneg = (r < -3.0 * sd).astype(float).where(sd.notna(), np.nan).rolling(252, min_periods=84).sum()\nout = pos - neg\n")


# ==================================================================
# Group B (391-405) — Asymmetric leverage / GJR / volatility-feedback
# ==================================================================

# 391 Bekaert-Engstrom asymmetric vol response: regression of σ² on neg-shock
add(391, "be_asym_vol_response_neg_shock_252d", "close",
    "r = _safe_log(close).diff()\nrv = (r ** 2).rolling(21, min_periods=7).mean()\nneg = r.where(r < 0, 0.0)\nout = rv.rolling(252, min_periods=84).cov(neg ** 2) / (neg ** 2).rolling(252, min_periods=84).var().replace(0, np.nan)\n")

# 392 GJR-GARCH asymmetric coefficient gamma: lagged neg-return-squared loading
add(392, "gjr_asym_gamma_proxy_252d", "close",
    "r = _safe_log(close).diff()\nrv = (r ** 2).rolling(5, min_periods=3).mean()\nneg_sq = (r.shift(1) ** 2).where(r.shift(1) < 0, 0.0)\npos_sq = (r.shift(1) ** 2).where(r.shift(1) > 0, 0.0)\n# rv = a*pos_sq + (a+gamma)*neg_sq + ... approx via diff in coefficients\ncov_n = rv.rolling(252, min_periods=84).cov(neg_sq)\ncov_p = rv.rolling(252, min_periods=84).cov(pos_sq)\nvar_n = neg_sq.rolling(252, min_periods=84).var().replace(0, np.nan)\nvar_p = pos_sq.rolling(252, min_periods=84).var().replace(0, np.nan)\nout = _safe_div(cov_n, var_n) - _safe_div(cov_p, var_p)\n")

# 393 leverage effect: correlation of return with future 21d-vol
add(393, "return_to_future_vol_corr_252d", "close",
    "r = _safe_log(close).diff()\nfut_rv = r.rolling(21, min_periods=7).std().shift(-21)\nout = r.rolling(252, min_periods=84).corr(fut_rv)\n")

# 394 leverage at 63d horizon
add(394, "return_to_future_63d_vol_corr_252d", "close",
    "r = _safe_log(close).diff()\nfut_rv = r.rolling(63, min_periods=21).std().shift(-63)\nout = r.rolling(252, min_periods=84).corr(fut_rv)\n")

# 395 Wright-style conditional vol given prior up vs down
add(395, "cond_vol_given_prior_up_minus_down_252d", "close",
    "r = _safe_log(close).diff()\nrv_up = r.where(r.shift(1) > 0, np.nan).rolling(252, min_periods=84).std()\nrv_dn = r.where(r.shift(1) < 0, np.nan).rolling(252, min_periods=84).std()\nout = rv_up - rv_dn\n")

# 396 vol-asymmetry ratio (rv_dn / rv_up)
add(396, "cond_vol_dn_over_up_ratio_252d", "close",
    "r = _safe_log(close).diff()\nrv_up = r.where(r.shift(1) > 0, np.nan).rolling(252, min_periods=84).std()\nrv_dn = r.where(r.shift(1) < 0, np.nan).rolling(252, min_periods=84).std()\nout = _safe_div(rv_dn, rv_up)\n")

# 397 asymmetric semivariance ratio at lag 5 (longer leverage)
add(397, "semivar_ratio_lag5_252d", "close",
    "r = _safe_log(close).diff()\nlag5_neg = r.where(r.shift(5) < 0, np.nan)\nlag5_pos = r.where(r.shift(5) > 0, np.nan)\nsv_n = (lag5_neg ** 2).rolling(252, min_periods=84).mean()\nsv_p = (lag5_pos ** 2).rolling(252, min_periods=84).mean()\nout = _safe_div(sv_n, sv_p)\n")

# 398 sign-flip-of-volatility regime: cov(return, Δσ²) — leverage instantaneous
add(398, "instant_leverage_cov_ret_dvar_252d", "close",
    "r = _safe_log(close).diff()\nrv = (r ** 2).rolling(5, min_periods=3).mean()\ndrv = rv - rv.shift(1)\nout = r.rolling(252, min_periods=84).cov(drv)\n")

# 399 volatility feedback: cov(Δσ, return.shift(-1)) — vol predicts return sign
add(399, "vol_feedback_cov_dsigma_to_next_ret_252d", "close",
    "r = _safe_log(close).diff()\nrv = r.rolling(21, min_periods=7).std()\ndrv = rv - rv.shift(1)\nout = drv.rolling(252, min_periods=84).cov(r.shift(-1))\n")

# 400 conditional kurt given large negative-shock 252d
add(400, "cond_kurt_given_neg_shock_252d", "close",
    "r = _safe_log(close).diff()\nsd = r.rolling(252, min_periods=84).std()\ncond_r = r.where(r.shift(1) < -sd.shift(1), np.nan)\ndef _kt(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 10:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); ss = v.std(ddof=1)\n    if ss <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / ss) ** 4) - 3.0)\nout = cond_r.rolling(252, min_periods=84).apply(_kt, raw=True)\n")

# 401 risk-premium-decay proxy: 21d-mean-return / 21d-vol (Sharpe-like decay)
add(401, "sharpe_decay_21d_in_252d", "close",
    "r = _safe_log(close).diff()\nsh21 = r.rolling(21, min_periods=7).mean() / r.rolling(21, min_periods=7).std().replace(0, np.nan)\nout = sh21 - sh21.rolling(252, min_periods=84).mean()\n")

# 402 cond-return given high-vol regime 252d (downside-bias under stress)
add(402, "cond_mean_ret_high_vol_regime_252d", "close",
    "r = _safe_log(close).diff()\nrv21 = r.rolling(21, min_periods=7).std()\nmed_rv = rv21.rolling(252, min_periods=84).median()\ncond_r = r.where(rv21 > med_rv, np.nan)\nout = cond_r.rolling(252, min_periods=84).mean()\n")

# 403 cond-return given low-vol regime (relative regime mean)
add(403, "cond_mean_ret_low_vol_regime_252d", "close",
    "r = _safe_log(close).diff()\nrv21 = r.rolling(21, min_periods=7).std()\nmed_rv = rv21.rolling(252, min_periods=84).median()\ncond_r = r.where(rv21 < med_rv, np.nan)\nout = cond_r.rolling(252, min_periods=84).mean()\n")

# 404 asymmetric-vol asymmetry-z: zscore of vol_dn vs vol_up 252d
add(404, "asym_vol_zscore_252d", "close",
    "r = _safe_log(close).diff()\nrv_up = r.where(r.shift(1) > 0, np.nan).rolling(252, min_periods=84).std()\nrv_dn = r.where(r.shift(1) < 0, np.nan).rolling(252, min_periods=84).std()\nspread = rv_dn - rv_up\nout = _rolling_zscore(spread, 504, min_periods=168)\n")

# 405 mean-half-life-of-vol-shock (autocorr-based proxy on rv)
add(405, "vol_shock_half_life_252d", "close",
    "r = _safe_log(close).diff()\nrv = (r ** 2).rolling(5, min_periods=3).mean()\ndef _hl(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = (w[valid] if not valid.all() else w).astype(float)\n    m = v.mean(); vc = v - m\n    den = float((vc ** 2).sum())\n    if den == 0:\n        return np.nan\n    rho = float((vc[1:] * vc[:-1]).sum() / den)\n    if rho <= 0 or rho >= 1:\n        return np.nan\n    return float(-np.log(2) / np.log(rho))\nout = rv.rolling(252, min_periods=84).apply(_hl, raw=True)\n")


# ==================================================================
# Group C (406-420) — Realized higher moments from OHLC
# ==================================================================

# 406 realized skew (intraday OHLC-implied) 21d
add(406, "realized_intraday_skew_OHLC_21d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 7:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3))\nout = intr.rolling(21, min_periods=7).apply(_sk, raw=True)\n")

# 407 realized skew at 252d
add(407, "realized_intraday_skew_OHLC_252d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3))\nout = intr.rolling(252, min_periods=84).apply(_sk, raw=True)\n")

# 408 realized kurt 252d
add(408, "realized_intraday_kurt_OHLC_252d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\ndef _kt(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 4) - 3.0)\nout = intr.rolling(252, min_periods=84).apply(_kt, raw=True)\n")

# 409 daily-skew vs intraday-skew agreement (regime test)
add(409, "daily_vs_intraday_skew_agreement_252d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\nday = _safe_log(close).diff()\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3))\nsk_intr = intr.rolling(252, min_periods=84).apply(_sk, raw=True)\nsk_day = day.rolling(252, min_periods=84).apply(_sk, raw=True)\nout = (np.sign(sk_intr) == np.sign(sk_day)).astype(float).where(sk_intr.notna() & sk_day.notna(), np.nan)\n")

# 410 cross-moment of return and volume (return-volume co-skew) 252d
add(410, "coskew_ret_vol_252d", "close,volume",
    "r = _safe_log(close).diff()\nv = _safe_log(volume.replace(0, np.nan))\nr_dev = r - r.rolling(252, min_periods=84).mean()\nv_dev = v - v.rolling(252, min_periods=84).mean()\nout = (r_dev ** 2 * v_dev).rolling(252, min_periods=84).mean()\n")

# 411 realized fourth-moment (raw quarticity) of intraday-return 63d
add(411, "realized_quarticity_intraday_63d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\nout = (intr ** 4).rolling(63, min_periods=21).sum()\n")

# 412 hyper-skewness intraday 252d (5th standardized moment)
add(412, "realized_intraday_hyperskew_252d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\ndef _h(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 5))\nout = intr.rolling(252, min_periods=84).apply(_h, raw=True)\n")

# 413 cokurt with own lag(1) intraday 252d
add(413, "cokurt_intraday_with_lag1_252d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\nintr_lag = intr.shift(1)\nm_r = intr.rolling(252, min_periods=84).mean()\nm_l = intr_lag.rolling(252, min_periods=84).mean()\ns_r = intr.rolling(252, min_periods=84).std()\ns_l = intr_lag.rolling(252, min_periods=84).std()\nx_r = intr - m_r; x_l = intr_lag - m_l\nck = (x_r * x_r * x_l * x_l).rolling(252, min_periods=84).mean()\nout = _safe_div(ck, (s_r * s_r * s_l * s_l))\n")

# 414 realized signed-jump-variation OHLC 63d positive
add(414, "realized_signed_jump_intraday_pos_63d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\nsd = intr.rolling(63, min_periods=21).std()\npos = (intr ** 2).where(intr > 2.0 * sd, 0.0)\nout = pos.rolling(63, min_periods=21).sum()\n")

# 415 realized signed-jump-variation OHLC 63d negative
add(415, "realized_signed_jump_intraday_neg_63d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\nsd = intr.rolling(63, min_periods=21).std()\nneg = (intr ** 2).where(intr < -2.0 * sd, 0.0)\nout = neg.rolling(63, min_periods=21).sum()\n")

# 416 high-frequency vol-of-vol from intraday OHLC
add(416, "intraday_vol_of_vol_63d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\nrv5 = intr.rolling(5, min_periods=3).std()\nout = rv5.rolling(63, min_periods=21).std()\n")

# 417 cross-moment of close-vs-open and high-vs-low (intra-bar correlation)
add(417, "cross_oc_hl_corr_63d", "open,high,low,close",
    "oc = _safe_log(close) - _safe_log(open)\nhl = _safe_log(high) - _safe_log(low)\nout = oc.rolling(63, min_periods=21).corr(hl)\n")

# 418 realized squared-skew OHLC (vol-jump asymmetry)
add(418, "realized_intraday_skew_squared_252d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3) ** 2)\nout = intr.rolling(252, min_periods=84).apply(_sk, raw=True)\n")

# 419 realized skew of high-to-low daily distance 252d
add(419, "realized_skew_log_hl_252d", "high,low",
    "hl = _safe_log(high) - _safe_log(low)\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3))\nout = hl.rolling(252, min_periods=84).apply(_sk, raw=True)\n")

# 420 realized higher-moment-balance: skew^2 + kurt = total non-normality
add(420, "intraday_skew_sq_plus_kurt_252d", "open,high,low,close",
    "tp = (high + low + close) / 3.0\nintr = _safe_log(tp) - _safe_log(open)\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3))\ndef _kt(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 30:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 4) - 3.0)\nsk = intr.rolling(252, min_periods=84).apply(_sk, raw=True)\nkt = intr.rolling(252, min_periods=84).apply(_kt, raw=True)\nout = sk ** 2 + kt\n")


# ==================================================================
# Group D (421-435) — Vol-term-structure cascades
# ==================================================================

# 421 5d-vol / 21d-vol (short cycle vs monthly)
add(421, "rv_5d_over_21d_ratio", "close",
    "r = _safe_log(close).diff()\nout = _safe_div(r.rolling(5, min_periods=3).std(), r.rolling(21, min_periods=7).std())\n")

# 422 21d-vol / 63d-vol
add(422, "rv_21d_over_63d_ratio", "close",
    "r = _safe_log(close).diff()\nout = _safe_div(r.rolling(21, min_periods=7).std(), r.rolling(63, min_periods=21).std())\n")

# 423 63d-vol / 252d-vol
add(423, "rv_63d_over_252d_ratio", "close",
    "r = _safe_log(close).diff()\nout = _safe_div(r.rolling(63, min_periods=21).std(), r.rolling(252, min_periods=84).std())\n")

# 424 vol-term-structure-slope (regression slope of log-vol vs log-horizon)
add(424, "vol_term_structure_slope_3pt_252d", "close",
    "r = _safe_log(close).diff()\nv5 = r.rolling(5, min_periods=3).std()\nv21 = r.rolling(21, min_periods=7).std()\nv63 = r.rolling(63, min_periods=21).std()\nx = np.log([5.0, 21.0, 63.0])\nlv5 = _safe_log(v5); lv21 = _safe_log(v21); lv63 = _safe_log(v63)\nstk = pd.concat([lv5.rename(0), lv21.rename(1), lv63.rename(2)], axis=1)\ndef _slope(row):\n    a = row.values\n    if np.isnan(a).any():\n        return np.nan\n    xm = x.mean(); ym = a.mean()\n    den = float(((x - xm) ** 2).sum())\n    if den == 0:\n        return np.nan\n    return float(((x - xm) * (a - ym)).sum() / den)\nout = stk.apply(_slope, axis=1)\n")

# 425 vol-term-structure inversion indicator (short > long)
add(425, "vol_term_inversion_21d_above_63d_indicator", "close",
    "r = _safe_log(close).diff()\nv21 = r.rolling(21, min_periods=7).std()\nv63 = r.rolling(63, min_periods=21).std()\nout = (v21 > v63).astype(float).where(v63.notna(), np.nan)\n")

# 426 vol-of-vol-of-vol (3rd-order vol persistence)
add(426, "vol_of_vol_of_vol_63d", "close",
    "r = _safe_log(close).diff()\nrv = r.rolling(5, min_periods=3).std()\nvov = rv.rolling(21, min_periods=7).std()\nout = vov.rolling(63, min_periods=21).std()\n")

# 427 vol decay rate: log(v21 / v252) / log(21/252)
add(427, "vol_decay_log_log_slope_21_252", "close",
    "r = _safe_log(close).diff()\nv21 = r.rolling(21, min_periods=7).std()\nv252 = r.rolling(252, min_periods=84).std()\nratio = _safe_log(_safe_div(v21, v252))\nout = ratio / np.log(21.0 / 252.0)\n")

# 428 vol regime shift event: |Δlog-21d-vol| > 0.5
add(428, "log_vol_shift_above_05_event_252d", "close",
    "r = _safe_log(close).diff()\nv21 = r.rolling(21, min_periods=7).std()\nlv = _safe_log(v21)\nout = ((lv - lv.shift(21)).abs() > 0.5).astype(float).where(lv.shift(21).notna(), np.nan).rolling(252, min_periods=84).sum()\n")

# 429 cross-horizon vol correlation (5d vs 63d log-vol)
add(429, "log_vol_corr_5d_63d_252d", "close",
    "r = _safe_log(close).diff()\nlv5 = _safe_log(r.rolling(5, min_periods=3).std())\nlv63 = _safe_log(r.rolling(63, min_periods=21).std())\nout = lv5.rolling(252, min_periods=84).corr(lv63)\n")

# 430 vol-term-structure-skew (curve concavity)
add(430, "vol_term_curve_concavity_2nd_diff", "close",
    "r = _safe_log(close).diff()\nlv5 = _safe_log(r.rolling(5, min_periods=3).std())\nlv21 = _safe_log(r.rolling(21, min_periods=7).std())\nlv63 = _safe_log(r.rolling(63, min_periods=21).std())\nout = lv5 - 2.0 * lv21 + lv63\n")

# 431 cross-vol-spike-density at multiple horizons
add(431, "cross_horizon_vol_spike_density_252d", "close",
    "r = _safe_log(close).diff()\nz5 = _rolling_zscore(r.rolling(5, min_periods=3).std(), 252, min_periods=84)\nz21 = _rolling_zscore(r.rolling(21, min_periods=7).std(), 252, min_periods=84)\nz63 = _rolling_zscore(r.rolling(63, min_periods=21).std(), 252, min_periods=84)\nspike = ((z5 > 1.5).astype(float) + (z21 > 1.5).astype(float) + (z63 > 1.5).astype(float)).rolling(252, min_periods=84).sum()\nout = spike\n")

# 432 vol-of-21d-vol z-score in 252d (vol-of-vol regime)
add(432, "vol_of_vol_21d_zscore_252d", "close",
    "r = _safe_log(close).diff()\nrv21 = r.rolling(21, min_periods=7).std()\nvov = rv21.rolling(21, min_periods=7).std()\nout = _rolling_zscore(vov, 252, min_periods=84)\n")

# 433 vol-of-vol acceleration (Δ vol-of-vol)
add(433, "vol_of_vol_accel_21d_in_252d", "close",
    "r = _safe_log(close).diff()\nrv = r.rolling(21, min_periods=7).std()\nvov = rv.rolling(21, min_periods=7).std()\nout = vov - vov.shift(21)\n")

# 434 spread-of-vol-curve: max-vol-horizon - min-vol-horizon
add(434, "vol_curve_max_minus_min_4pt", "close",
    "r = _safe_log(close).diff()\nv5 = r.rolling(5, min_periods=3).std()\nv21 = r.rolling(21, min_periods=7).std()\nv63 = r.rolling(63, min_periods=21).std()\nv252 = r.rolling(252, min_periods=84).std()\nstk = pd.concat([v5.rename(0), v21.rename(1), v63.rename(2), v252.rename(3)], axis=1)\nout = stk.max(axis=1) - stk.min(axis=1)\n")

# 435 vol-curve-rotation (slope sign change)
add(435, "vol_curve_slope_sign_flip_252d", "close",
    "r = _safe_log(close).diff()\nlv21 = _safe_log(r.rolling(21, min_periods=7).std())\nlv63 = _safe_log(r.rolling(63, min_periods=21).std())\nslope = lv21 - lv63\nsg = np.sign(slope)\nout = (sg != sg.shift(21)).astype(float).where(sg.notna() & sg.shift(21).notna(), np.nan).rolling(252, min_periods=84).sum()\n")


# ==================================================================
# Group E (436-450) — Anchoring, conditional asymmetry, residual signals
# ==================================================================

# 436 52w-high anchoring distance: (52wh - close) / 52wh
add(436, "anchor_distance_to_52w_high_pct", "high,close",
    "rmax = high.rolling(252, min_periods=84).max()\nout = _safe_div(rmax - close, rmax)\n")

# 437 52w-low anchoring distance
add(437, "anchor_distance_to_52w_low_pct", "low,close",
    "rmin = low.rolling(252, min_periods=84).min()\nout = _safe_div(close - rmin, close)\n")

# 438 round-cent attraction (close within 1c of $5 multiple)
add(438, "round_5dollar_attraction_freq_252d", "close",
    "remainder = (close - (close / 5.0).round() * 5.0).abs()\nnear = (remainder < 0.05).astype(float).where(close.notna(), np.nan)\nout = near.rolling(252, min_periods=84).mean()\n")

# 439 round-cent rejection (close at round AND lower next day)
add(439, "round_dollar_rejection_freq_252d", "close",
    "cents = (close * 100.0).round().astype(float)\nat_round = ((cents % 100) == 0).astype(float)\ndown_next = (close.shift(-1) < close).astype(float)\nrej = at_round * down_next\nout = rej.rolling(252, min_periods=84).mean()\n")

# 440 prior-high anchor: distance to 21d prior-high
add(440, "anchor_distance_to_21d_prior_high_pct", "high,close",
    "rmax21 = high.shift(21).rolling(21, min_periods=7).max()\nout = _safe_div(rmax21 - close, rmax21)\n")

# 441 prior-close anchoring: dist from 21d-prior close
add(441, "anchor_distance_to_21d_prior_close_pct", "close",
    "out = _safe_div(close - close.shift(21), close.shift(21))\n")

# 442 conditional skew given prior-21d-up trend (acceleration regime)
add(442, "cond_skew_given_21d_up_trend_252d", "close",
    "r = _safe_log(close).diff()\nret21 = _safe_log(close).diff(21)\ncond_r = r.where(ret21 > 0, np.nan)\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 10:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3))\nout = cond_r.rolling(252, min_periods=84).apply(_sk, raw=True)\n")

# 443 conditional skew given prior-21d-down trend
add(443, "cond_skew_given_21d_down_trend_252d", "close",
    "r = _safe_log(close).diff()\nret21 = _safe_log(close).diff(21)\ncond_r = r.where(ret21 < 0, np.nan)\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 10:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3))\nout = cond_r.rolling(252, min_periods=84).apply(_sk, raw=True)\n")

# 444 skew-conditional-on-regime difference (up-skew - down-skew)
add(444, "cond_skew_up_minus_down_regime_252d", "close",
    "r = _safe_log(close).diff()\nret21 = _safe_log(close).diff(21)\nup = r.where(ret21 > 0, np.nan)\ndn = r.where(ret21 < 0, np.nan)\ndef _sk(w):\n    valid = ~np.isnan(w)\n    if valid.sum() < 10:\n        return np.nan\n    v = w[valid]\n    m = v.mean(); s = v.std(ddof=1)\n    if s <= 0:\n        return np.nan\n    return float(np.mean(((v - m) / s) ** 3))\nout = up.rolling(252, min_periods=84).apply(_sk, raw=True) - dn.rolling(252, min_periods=84).apply(_sk, raw=True)\n")

# 445 max-drawdown-from-prior-21d-high speed
add(445, "max_dd_from_21d_high_decay_5d_252d", "high,close",
    "rmax21 = high.rolling(21, min_periods=7).max()\ndd = _safe_log(rmax21) - _safe_log(close)\nout = (dd - dd.shift(5)).rolling(252, min_periods=84).max()\n")

# 446 vol-shock-asymmetric: pos-vol-shock vs neg-vol-shock count
add(446, "pos_vs_neg_vol_shock_count_252d", "close",
    "r = _safe_log(close).diff()\nrv = r.rolling(5, min_periods=3).std()\ndrv = rv - rv.shift(5)\nz = _rolling_zscore(drv, 252, min_periods=84)\npos = (z > 2.0).astype(float).where(z.notna(), np.nan).rolling(252, min_periods=84).sum()\nneg = (z < -2.0).astype(float).where(z.notna(), np.nan).rolling(252, min_periods=84).sum()\nout = pos - neg\n")

# 447 anchoring drift: rate close drifts away from 252d-high
add(447, "drift_away_from_252d_high_63d", "high,close",
    "rmax = high.rolling(252, min_periods=84).max()\ndist = _safe_div(rmax - close, rmax)\nout = dist - dist.shift(63)\n")

# 448 conditional vol given large-down day at peak
add(448, "cond_vol_given_large_down_at_252d_high_252d", "high,close",
    "r = _safe_log(close).diff()\nrmax = high.rolling(252, min_periods=84).max()\nat_high = (high >= 0.95 * rmax).astype(bool)\nsd = r.rolling(63, min_periods=21).std()\nlarge_dn = r.where((r < -2.0 * sd) & at_high, np.nan)\nout = large_dn.rolling(252, min_periods=84).std()\n")

# 449 idiosyncratic vol proxy: residual of return on prior-5d-return regression 252d
add(449, "idiosyncratic_vol_proxy_252d", "close",
    "r = _safe_log(close).diff()\nlag5 = _safe_log(close).diff(5).shift(1)\nb = r.rolling(252, min_periods=84).cov(lag5) / lag5.rolling(252, min_periods=84).var().replace(0, np.nan)\nresid = r - b * lag5\nout = resid.rolling(252, min_periods=84).std()\n")

# 450 max-bar-return / max-bar-range ratio (efficiency of move)
add(450, "max_bar_return_over_range_252d", "open,high,low,close",
    "bar_ret = (_safe_log(close) - _safe_log(open)).abs()\nbar_rng = _safe_log(high) - _safe_log(low)\neff = _safe_div(bar_ret, bar_rng)\nout = eff.rolling(252, min_periods=84).max()\n")


# ==================================================================
# Writer
# ==================================================================

def _build_function_source(idx, suffix, inputs_csv, body, order):
    fname_base = f"f49_bcco_{idx:03d}_{suffix}"
    fname = fname_base if order == "base" else f"{fname_base}_{order}"
    in_names = [i.strip() for i in inputs_csv.split(",")]
    arg_sig = ", ".join([f"{n}: pd.Series" for n in in_names])
    if order == "base":
        ret_chain = "out"
    elif order == "d1":
        ret_chain = "out.diff()"
    elif order == "d2":
        ret_chain = "out.diff().diff()"
    elif order == "d3":
        ret_chain = "out.diff().diff().diff()"
    else:
        raise ValueError(order)
    return f"def {fname}({arg_sig}) -> pd.Series:\n{body}\n    return {ret_chain}\n"


def _write_file(order, lo, hi):
    src = HEADER_FMT.format(order=order, lo=lo, hi=hi) + "\n"
    in_range = [f for f in FEATS if lo <= f[0] <= hi]
    in_range.sort(key=lambda x: x[0])
    for idx, suffix, inputs_csv, body in in_range:
        src += "\n" + _build_function_source(idx, suffix, inputs_csv, body, order) + "\n"
    reg_name = f"BLOWOFF_CLIMAX_COMPOSITE_{order.upper()}_REGISTRY_{lo:03d}_{hi:03d}"
    src += f"\n# ============================================================\n#                         REGISTRY {lo:03d}_{hi:03d} ({order})\n# ============================================================\n\n{reg_name} = {{\n"
    for idx, suffix, inputs_csv, _ in in_range:
        fname_base = f"f49_bcco_{idx:03d}_{suffix}"
        fname = fname_base if order == "base" else f"{fname_base}_{order}"
        in_list = [i.strip() for i in inputs_csv.split(",")]
        in_repr = "[" + ", ".join([f'"{x}"' for x in in_list]) + "]"
        src += f'    "{fname}": {{"inputs": {in_repr}, "func": {fname}}},\n'
    src += "}\n"
    out_path = os.path.join(ROOT, f"49_blowoff_climax_composite__{order}__{lo:03d}_{hi:03d}.py")
    os.makedirs(ROOT, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(src)
    return out_path


def main():
    seen = set()
    for f in FEATS:
        if f[0] in seen:
            raise SystemExit(f"DUPLICATE index {f[0]}")
        seen.add(f[0])
    missing = [i for i in range(376, 451) if i not in seen]
    if missing:
        raise SystemExit(f"MISSING indices: {missing}")
    print(f"OK: {len(FEATS)} features, indices 376-450 all present.")
    for order in ("base", "d1", "d2", "d3"):
        p = _write_file(order, 376, 450)
        print(f"wrote {p} ({os.path.getsize(p)} bytes)")
    print("DONE")


if __name__ == "__main__":
    main()
