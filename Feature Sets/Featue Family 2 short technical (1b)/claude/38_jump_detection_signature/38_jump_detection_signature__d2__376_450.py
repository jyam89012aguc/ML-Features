"""38_jump_detection_signature d2 features 376-450 — order-2 difference of corresponding base features.

Each function inlines the base body and wraps the return value with .diff().diff(). Self-contained; helpers redefined locally per HANDOFF."""
import math
import numpy as np
import pandas as pd
YDAYS = 252
QDAYS = 63
MDAYS = 21
WDAYS = 5
DDAYS_2Y = 504
DDAYS_3Y = 756
DDAYS_5Y = 1260

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
    idx = num.index if hasattr(num, 'index') else None
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
        xm = x.mean()
        wm = wv.mean()
        num = ((x - xm) * (wv - wm)).sum()
        den = ((x - xm) ** 2).sum()
        return num / den if den != 0 else np.nan
    return s.rolling(n, min_periods=min_periods).apply(_slope, raw=True)

def _log_ret(close):
    return _safe_log(close).diff()

def _sigma_prior(r, n):
    return r.rolling(n, min_periods=max(n // 3, 2)).std().shift(1)

def _bars_since(ind: pd.Series) -> pd.Series:
    arr = ind.fillna(0).astype(int).values
    out = np.full(len(arr), np.nan)
    bars = np.nan
    for i, x in enumerate(arr):
        if x:
            bars = 0
        elif np.isfinite(bars):
            bars = bars + 1
        out[i] = bars
    return pd.Series(out, index=ind.index)

def _jump_sign_transitions(arr_sign: np.ndarray, target_from: int, target_to: int) -> float:
    sj = arr_sign[arr_sign != 0]
    if len(sj) < 5:
        return np.nan
    from_count = 0
    trans_count = 0
    for i in range(len(sj) - 1):
        if sj[i] == target_from:
            from_count += 1
            if sj[i + 1] == target_to:
                trans_count += 1
    if from_count == 0:
        return np.nan
    return trans_count / from_count

def f38_jpdt_376_expected_time_to_next_jump_252d_d2(close: pd.Series) -> pd.Series:
    """Expected time to next 3σ_21d jump: mean of inter-jump times over 252d (rolling)."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _mean_gap(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 2:
            return np.nan
        return float(np.diff(idx).mean())
    return j.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True).diff().diff()

def f38_jpdt_377_jump_hazard_rate_252d_d2(close: pd.Series) -> pd.Series:
    """Jump hazard rate = 1 / expected inter-jump time over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _mean_gap(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 2:
            return np.nan
        return float(np.diff(idx).mean())
    exp_time = j.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True)
    return _safe_div(pd.Series(1.0, index=close.index), exp_time).diff().diff()

def f38_jpdt_378_survival_prob_no_jump_5d_d2(close: pd.Series) -> pd.Series:
    """Survival probability for next 5 bars (no jump): (1 − hazard_rate)^5 — proxy."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _mean_gap(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 2:
            return np.nan
        return float(np.diff(idx).mean())
    h = _safe_div(pd.Series(1.0, index=close.index), j.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True))
    return ((1.0 - h.clip(upper=0.99, lower=0.0)) ** WDAYS).diff().diff()

def f38_jpdt_379_survival_prob_no_jump_21d_d2(close: pd.Series) -> pd.Series:
    """Survival probability for next 21 bars (no jump): (1 − hazard_rate)^21."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _mean_gap(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 2:
            return np.nan
        return float(np.diff(idx).mean())
    h = _safe_div(pd.Series(1.0, index=close.index), j.rolling(YDAYS, min_periods=QDAYS).apply(_mean_gap, raw=True))
    return ((1.0 - h.clip(upper=0.99, lower=0.0)) ** MDAYS).diff().diff()

def f38_jpdt_380_stale_quiet_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Stale-quiet flag: current quiet-streak > p99 of quiet-streak lengths in 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(int).fillna(0).values
    quiet_now = np.zeros(len(j), dtype=float)
    cur = 0
    for i, v in enumerate(j):
        cur = 0 if v == 1 else cur + 1
        quiet_now[i] = cur
    quiet_now_s = pd.Series(quiet_now, index=close.index)

    def _p99(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        return float(np.quantile(ww, 0.99))
    p99 = quiet_now_s.rolling(YDAYS, min_periods=QDAYS).apply(_p99, raw=True)
    return (quiet_now_s > p99).astype(float).diff().diff()

def f38_jpdt_381_stale_jump_indicator_252d_d2(close: pd.Series) -> pd.Series:
    """Stale-jump flag: current jump-streak > p99 of jump-streak lengths in 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(int).fillna(0).values
    streak_now = np.zeros(len(j), dtype=float)
    cur = 0
    for i, v in enumerate(j):
        cur = cur + 1 if v == 1 else 0
        streak_now[i] = cur
    s_now = pd.Series(streak_now, index=close.index)
    p99 = s_now.rolling(YDAYS, min_periods=QDAYS).quantile(0.99)
    return (s_now > p99).astype(float).diff().diff()

def f38_jpdt_382_bars_since_pos_jump_d2(close: pd.Series) -> pd.Series:
    """Bars since last positive 3σ_21d jump."""
    r = _log_ret(close)
    return _bars_since((r > 3 * _sigma_prior(r, MDAYS)).astype(float)).diff().diff()

def f38_jpdt_383_bars_since_neg_jump_d2(close: pd.Series) -> pd.Series:
    """Bars since last negative 3σ_21d jump."""
    r = _log_ret(close)
    return _bars_since((r < -3 * _sigma_prior(r, MDAYS)).astype(float)).diff().diff()

def f38_jpdt_384_bayes_post_jump_regime_63d_d2(close: pd.Series) -> pd.Series:
    """Bayesian posterior P(jump-regime | recent jump density) via simple two-state likelihood ratio over 63d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    recent = j.rolling(QDAYS, min_periods=MDAYS).mean()
    long_run = j.rolling(YDAYS, min_periods=QDAYS).mean()
    odds = _safe_div(recent, long_run.replace(0.0, 0.01))
    return _safe_div(odds, 1.0 + odds).diff().diff()

def f38_jpdt_385_posterior_odds_jump_regime_63d_d2(close: pd.Series) -> pd.Series:
    """Posterior odds ratio = P(jump_regime) / P(quiet_regime) ≈ recent jump density / long-run."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    recent = j.rolling(QDAYS, min_periods=MDAYS).mean()
    long_run = j.rolling(YDAYS, min_periods=QDAYS).mean()
    return _safe_div(recent, long_run.replace(0.0, 0.01)).diff().diff()

def f38_jpdt_386_log_likelihood_returns_normal_252d_d2(close: pd.Series) -> pd.Series:
    """Mean log-likelihood of recent r under N(0, σ̂_252) over 252d window."""
    r = _log_ret(close)
    sig = r.rolling(YDAYS, min_periods=QDAYS).std()
    ll = -0.5 * (_safe_div(r ** 2, sig ** 2) + 2.0 * _safe_log(sig) + np.log(2.0 * np.pi))
    return ll.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_387_log_likelihood_ratio_thick_vs_thin_252d_d2(close: pd.Series) -> pd.Series:
    """LLR: mean log-likelihood under N(0, 2·σ̂) vs N(0, σ̂) over 252d — favors thick tails when positive."""
    r = _log_ret(close)
    sig = r.rolling(YDAYS, min_periods=QDAYS).std()
    ll_thick = -0.5 * (_safe_div(r ** 2, (2.0 * sig) ** 2) + 2.0 * _safe_log(2.0 * sig) + np.log(2.0 * np.pi))
    ll_thin = -0.5 * (_safe_div(r ** 2, sig ** 2) + 2.0 * _safe_log(sig) + np.log(2.0 * np.pi))
    return (ll_thick - ll_thin).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_388_local_bayes_factor_63d_d2(close: pd.Series) -> pd.Series:
    """Local Bayes factor: ratio of recent r² mean to long-run mean — informal evidence for vol-regime shift."""
    r2 = _log_ret(close) ** 2
    return _safe_div(r2.rolling(QDAYS, min_periods=MDAYS).mean(), r2.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f38_jpdt_389_gap_then_intraday_jump_seq_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-jump followed within 5d by intraday-range jump count over 252d."""
    g = _safe_log(open) - _safe_log(close.shift(1))
    hl = _safe_log(high) - _safe_log(low)
    g_jump = g.abs() > 3 * _sigma_prior(g, MDAYS)
    hl_jump = hl > 3 * _sigma_prior(hl, MDAYS)
    g_lag = g_jump.shift(1).rolling(WDAYS, min_periods=1).max().astype(bool)
    return (g_lag & hl_jump).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_390_intraday_then_gap_jump_seq_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Intraday-range jump followed within 5d by gap-jump count over 252d."""
    g = _safe_log(open) - _safe_log(close.shift(1))
    hl = _safe_log(high) - _safe_log(low)
    g_jump = g.abs() > 3 * _sigma_prior(g, MDAYS)
    hl_jump = hl > 3 * _sigma_prior(hl, MDAYS)
    hl_lag = hl_jump.shift(1).rolling(WDAYS, min_periods=1).max().astype(bool)
    return (hl_lag & g_jump).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_391_c2c_jump_preceded_by_gap_jump_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """c2c jump preceded by gap-jump in prior bar count over 252d."""
    r = _log_ret(close)
    g = _safe_log(open) - _safe_log(close.shift(1))
    c2c_jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    g_lag = (g.shift(1).abs() > 3 * _sigma_prior(g, MDAYS).shift(1)).fillna(False)
    return (c2c_jump & g_lag).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_392_triple_jump_coincident_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Coincident gap+intraday+c2c jump (all three on same bar) count over 252d."""
    r = _log_ret(close)
    g = _safe_log(open) - _safe_log(close.shift(1))
    hl = _safe_log(high) - _safe_log(low)
    c2c = r.abs() > 3 * _sigma_prior(r, MDAYS)
    gj = g.abs() > 3 * _sigma_prior(g, MDAYS)
    hj = hl > 3 * _sigma_prior(hl, MDAYS)
    return (c2c & gj & hj).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_393_gap_up_then_c2c_dn_seq_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-up jump → negative c2c jump within 5d count over 252d (climax-fade signature)."""
    g = _safe_log(open) - _safe_log(close.shift(1))
    r = _log_ret(close)
    sig_g = _sigma_prior(g, MDAYS)
    sig_r = _sigma_prior(r, MDAYS)
    g_up = g > 3 * sig_g
    r_dn = r < -3 * sig_r
    g_lag = g_up.shift(1).rolling(WDAYS, min_periods=1).max().astype(bool)
    return (g_lag & r_dn).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_394_gap_dn_then_c2c_up_seq_252d_d2(open: pd.Series, close: pd.Series) -> pd.Series:
    """Gap-down jump → positive c2c jump within 5d count over 252d (V-recovery signature)."""
    g = _safe_log(open) - _safe_log(close.shift(1))
    r = _log_ret(close)
    sig_g = _sigma_prior(g, MDAYS)
    sig_r = _sigma_prior(r, MDAYS)
    g_dn = g < -3 * sig_g
    r_up = r > 3 * sig_r
    g_lag = g_dn.shift(1).rolling(WDAYS, min_periods=1).max().astype(bool)
    return (g_lag & r_up).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_395_mixed_jump_cooccurrence_rate_252d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Frequency of bars where >=2 of {gap, intraday-range, c2c} jump indicators fire, over 252d."""
    r = _log_ret(close)
    g = _safe_log(open) - _safe_log(close.shift(1))
    hl = _safe_log(high) - _safe_log(low)
    c2c = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(int)
    gj = (g.abs() > 3 * _sigma_prior(g, MDAYS)).astype(int)
    hj = (hl > 3 * _sigma_prior(hl, MDAYS)).astype(int)
    multi = (c2c + gj + hj >= 2).astype(float)
    return multi.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_396_corr_gap_intraday_jumps_63d_d2(open: pd.Series, high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Rolling 63d corr between gap-jump indicator and intraday-range-jump indicator."""
    g = _safe_log(open) - _safe_log(close.shift(1))
    hl = _safe_log(high) - _safe_log(low)
    gj = (g.abs() > 3 * _sigma_prior(g, MDAYS)).astype(float)
    hj = (hl > 3 * _sigma_prior(hl, MDAYS)).astype(float)
    return gj.rolling(QDAYS, min_periods=MDAYS).corr(hj).diff().diff()

def f38_jpdt_397_vpin_proxy_5d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VPIN-style 5d: |Σ sign(r)·v| / Σv over 5d (toxic-flow concentration)."""
    r = _log_ret(close)
    sv = np.sign(r) * volume
    return _safe_div(sv.rolling(WDAYS, min_periods=2).sum().abs(), volume.rolling(WDAYS, min_periods=2).sum()).diff().diff()

def f38_jpdt_398_vpin_proxy_63d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """VPIN-style 63d: |Σ sign(r)·v| / Σv over 63d."""
    r = _log_ret(close)
    sv = np.sign(r) * volume
    return _safe_div(sv.rolling(QDAYS, min_periods=MDAYS).sum().abs(), volume.rolling(QDAYS, min_periods=MDAYS).sum()).diff().diff()

def f38_jpdt_399_pin_style_imbalance_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """PIN-style imbalance: Σ |volume_t − volume_{t-1}| / Σ volume over 21d."""
    return _safe_div(volume.diff().abs().rolling(MDAYS, min_periods=WDAYS).sum(), volume.rolling(MDAYS, min_periods=WDAYS).sum()).diff().diff()

def f38_jpdt_400_vpin_toxicity_shift_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """|VPIN_5d - VPIN_63d| — short-vs-medium toxicity divergence."""
    r = _log_ret(close)
    sv = np.sign(r) * volume
    v5 = _safe_div(sv.rolling(WDAYS, min_periods=2).sum().abs(), volume.rolling(WDAYS, min_periods=2).sum())
    v63 = _safe_div(sv.rolling(QDAYS, min_periods=MDAYS).sum().abs(), volume.rolling(QDAYS, min_periods=MDAYS).sum())
    return (v5 - v63).abs().diff().diff()

def f38_jpdt_401_vpin_acceleration_5d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """ΔVPIN over 5d — toxicity rate-of-change."""
    r = _log_ret(close)
    sv = np.sign(r) * volume
    v = _safe_div(sv.rolling(WDAYS, min_periods=2).sum().abs(), volume.rolling(WDAYS, min_periods=2).sum())
    return (v - v.shift(WDAYS)).diff().diff()

def f38_jpdt_402_order_flow_toxicity_rolling_21d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Order-flow toxicity proxy: rolling 21d mean of |sign(r)·v_z| where v_z is volume z-score."""
    r = _log_ret(close)
    vz = _rolling_zscore(volume, QDAYS)
    return (np.sign(r) * vz).abs().rolling(MDAYS, min_periods=WDAYS).mean().diff().diff()

def f38_jpdt_403_jump_day_signed_skew_252d_d2(close: pd.Series) -> pd.Series:
    """Skew of signed returns on 3σ_21d jump days over 252d."""
    r = _log_ret(close)
    sel = r.where(r.abs() > 3 * _sigma_prior(r, MDAYS), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).skew().diff().diff()

def f38_jpdt_404_nonjump_day_skew_252d_d2(close: pd.Series) -> pd.Series:
    """Skew of returns on non-jump days (|r| ≤ 3σ_21d) over 252d — continuous-component skew."""
    r = _log_ret(close)
    sel = r.where(r.abs() <= 3 * _sigma_prior(r, MDAYS), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).skew().diff().diff()

def f38_jpdt_405_jump_kurtosis_share_252d_d2(close: pd.Series) -> pd.Series:
    """Jump-day contribution to kurtosis: Σ(r⁴·1{|r|>3σ}) / Σ r⁴ over 252d."""
    r = _log_ret(close)
    jmask = r.abs() > 3 * _sigma_prior(r, MDAYS)
    return _safe_div((r ** 4).where(jmask, 0.0).rolling(YDAYS, min_periods=QDAYS).sum(), (r ** 4).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f38_jpdt_406_var_contribution_up_jumps_252d_d2(close: pd.Series) -> pd.Series:
    """Variance contribution from up-jumps (r > 3σ): Σ r²·1{r>3σ} / Σ r² over 252d."""
    r = _log_ret(close)
    up = r > 3 * _sigma_prior(r, MDAYS)
    return _safe_div((r ** 2).where(up, 0.0).rolling(YDAYS, min_periods=QDAYS).sum(), (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f38_jpdt_407_var_contribution_dn_jumps_252d_d2(close: pd.Series) -> pd.Series:
    """Variance contribution from down-jumps (r < −3σ) over 252d."""
    r = _log_ret(close)
    dn = r < -3 * _sigma_prior(r, MDAYS)
    return _safe_div((r ** 2).where(dn, 0.0).rolling(YDAYS, min_periods=QDAYS).sum(), (r ** 2).rolling(YDAYS, min_periods=QDAYS).sum()).diff().diff()

def f38_jpdt_408_asym_realized_4th_moment_252d_d2(close: pd.Series) -> pd.Series:
    """Asymmetric realized 4th moment: Σ r⁴·sign(r) over 252d (signed fourth-moment)."""
    r = _log_ret(close)
    return (r ** 4 * np.sign(r)).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_409_mean_pre_jump_vol_rank_252d_d2(close: pd.Series) -> pd.Series:
    """Mean σ_21 percentile rank in 5 bars before each 3σ_21d jump, over 252d."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    rk = sig.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True)
    pre_rank = rk.rolling(WDAYS, min_periods=2).mean().shift(1)
    jmask = r.abs() > 3 * _sigma_prior(r, MDAYS)
    sel = pre_rank.where(jmask, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_410_natr_release_ratio_at_jump_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (NATR_t / NATR_{t-5}) restricted to 3σ_21d jump days over 252d — compression-release."""
    natr = _safe_div(_atr(high, low, close, MDAYS), close)
    r = _log_ret(close)
    ratio = _safe_div(natr, natr.shift(WDAYS))
    sel = ratio.where(r.abs() > 3 * _sigma_prior(r, MDAYS), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_411_sigma_ratio_at_jump_252d_d2(close: pd.Series) -> pd.Series:
    """Mean (σ_21_t / σ_21_{t-21}) restricted to jump days — pre-jump vol-shift ratio."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    ratio = _safe_div(sig, sig.shift(MDAYS))
    sel = ratio.where(r.abs() > 3 * _sigma_prior(r, MDAYS), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_412_volume_ratio_at_jump_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean (volume_t / 5d-mean-volume) on jump days over 252d — volume amplification at jumps."""
    r = _log_ret(close)
    vol5 = volume.rolling(WDAYS, min_periods=2).mean().shift(1)
    ratio = _safe_div(volume, vol5)
    sel = ratio.where(r.abs() > 3 * _sigma_prior(r, MDAYS), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_413_atr_expansion_5d_pre_jump_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean (ATR_t / ATR_{t-5}) ratio restricted to 3σ_21d jump days over 252d."""
    a = _atr(high, low, close, MDAYS)
    r = _log_ret(close)
    ratio = _safe_div(a, a.shift(WDAYS))
    sel = ratio.where(r.abs() > 3 * _sigma_prior(r, MDAYS), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_414_sigma_shift_after_jump_21d_252d_d2(close: pd.Series) -> pd.Series:
    """Mean (σ_21_post − σ_21_pre) across jump events over 252d (21d post vs 21d pre)."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    post = sig
    pre = sig.shift(MDAYS)
    sel = (post - pre).where(r.shift(MDAYS).abs() > 3 * _sigma_prior(r, MDAYS).shift(MDAYS), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_415_sigma_shift_after_jump_63d_252d_d2(close: pd.Series) -> pd.Series:
    """Mean (σ_21_post − σ_21_pre) for 63d-displaced post vs pre, across jump events over 252d."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    sel = (sig - sig.shift(QDAYS)).where(r.shift(QDAYS).abs() > 3 * _sigma_prior(r, MDAYS).shift(QDAYS), np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_416_natr_shift_after_big_jump_252d_d2(high: pd.Series, low: pd.Series, close: pd.Series) -> pd.Series:
    """Mean ΔNATR around 4σ_252d big-jump events (NATR_t − NATR_{t-21}), summed 252d."""
    natr = _safe_div(_atr(high, low, close, MDAYS), close)
    r = _log_ret(close)
    big_jump_lag = r.shift(MDAYS).abs() > 4 * _sigma_prior(r, YDAYS).shift(MDAYS)
    sel = (natr - natr.shift(MDAYS)).where(big_jump_lag, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_417_avg_post_jump_drift_5d_252d_d2(close: pd.Series) -> pd.Series:
    """Mean 5d-trailing return immediately after jump events, over 252d."""
    r = _log_ret(close)
    trail5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    jmask_lag = r.shift(WDAYS).abs() > 3 * _sigma_prior(r, MDAYS).shift(WDAYS)
    sel = trail5.where(jmask_lag, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_418_post_jump_vol_of_vol_shift_252d_d2(close: pd.Series) -> pd.Series:
    """Mean (σ-of-σ_21d post-jump − pre-jump): vol-of-vol regime change at jumps, over 252d."""
    r = _log_ret(close)
    sig = r.rolling(MDAYS, min_periods=WDAYS).std()
    vov = sig.rolling(QDAYS, min_periods=MDAYS).std()
    jmask_lag = r.shift(MDAYS).abs() > 3 * _sigma_prior(r, MDAYS).shift(MDAYS)
    sel = (vov - vov.shift(MDAYS)).where(jmask_lag, np.nan)
    return sel.rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_419_climax_jump_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Climax jump: 3σ_21d jump AND close in top 5% of 252d range AND positive direction, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    flag = (r > 3 * sig) & (pos >= 0.95)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_420_capitulation_jump_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Capitulation jump: 3σ_21d down-jump AND close in bottom 5% of 252d range, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    h252 = high.rolling(YDAYS, min_periods=QDAYS).max()
    l252 = low.rolling(YDAYS, min_periods=QDAYS).min()
    pos = _safe_div(close - l252, h252 - l252)
    flag = (r < -3 * sig) & (pos <= 0.05)
    return flag.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_421_climax_jump_in_uptrend_count_252d_d2(close: pd.Series) -> pd.Series:
    """Jump + 5d trailing return > 10% (climax-with-trend) over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    trail5_lag = _safe_log(close).shift(1) - _safe_log(close.shift(WDAYS + 1))
    return (jump & (trail5_lag > 0.1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_422_panic_jump_count_252d_d2(close: pd.Series) -> pd.Series:
    """Jump + 5d trailing return < −10% (panic-jump) over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    trail5_lag = _safe_log(close).shift(1) - _safe_log(close.shift(WDAYS + 1))
    return (jump & (trail5_lag < -0.1)).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_423_jump_after_nr4_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Jump on day after NR4 (post-compression jump) over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    rng = high - low
    nr4_prior = (rng.shift(1) == rng.rolling(4, min_periods=4).min().shift(1)).fillna(False)
    return (jump & nr4_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_424_jump_after_wr7_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series) -> pd.Series:
    """Jump on day after WR7 (sequential wide-bar after a climax bar) over 252d."""
    r = _log_ret(close)
    jump = r.abs() > 3 * _sigma_prior(r, MDAYS)
    rng = high - low
    wr7_prior = (rng.shift(1) == rng.rolling(7, min_periods=7).max().shift(1)).fillna(False)
    return (jump & wr7_prior).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_425_jump_storm_count_63d_d2(close: pd.Series) -> pd.Series:
    """Jump-storm: 3+ jumps within any 5d window, count over 63d."""
    r = _log_ret(close)
    jump = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float)
    storm = (jump.rolling(WDAYS, min_periods=1).sum() >= 3).astype(float)
    return storm.rolling(QDAYS, min_periods=MDAYS).sum().diff().diff()

def f38_jpdt_426_full_climax_pattern_count_252d_d2(close: pd.Series, high: pd.Series, low: pd.Series, volume: pd.Series) -> pd.Series:
    """Full-climax pattern: vol_z>2 AND range > 2·ATR_prior AND new 21d-high, count over 252d."""
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    rng = high - low
    atr_prior = _atr(high, low, close, MDAYS).shift(1)
    big_range = rng > 2 * atr_prior
    new_high = high >= high.rolling(MDAYS, min_periods=WDAYS).max()
    return ((vz > 2.0) & big_range & new_high).astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_427_var_inter_jump_times_252d_d2(close: pd.Series) -> pd.Series:
    """Variance of inter-jump times within 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _vg(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 3:
            return np.nan
        return float(np.diff(idx).var())
    return j.rolling(YDAYS, min_periods=QDAYS).apply(_vg, raw=True).diff().diff()

def f38_jpdt_428_cv_jump_magnitudes_252d_d2(close: pd.Series) -> pd.Series:
    """CV of jump magnitudes (|r|·1{|r|>3σ}) over 252d."""
    r = _log_ret(close)
    mag = r.abs().where(r.abs() > 3 * _sigma_prior(r, MDAYS), np.nan)
    return _safe_div(mag.rolling(YDAYS, min_periods=QDAYS).std(), mag.rolling(YDAYS, min_periods=QDAYS).mean()).diff().diff()

def f38_jpdt_429_burstiness_inter_jump_252d_d2(close: pd.Series) -> pd.Series:
    """Burstiness (σ-μ)/(σ+μ) of inter-jump times over 252d — −1 = regular, 0 = Poisson, +1 = bursty."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _b(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 3:
            return np.nan
        g = np.diff(idx)
        m = g.mean()
        s = g.std()
        if m + s == 0:
            return np.nan
        return float((s - m) / (s + m))
    return j.rolling(YDAYS, min_periods=QDAYS).apply(_b, raw=True).diff().diff()

def f38_jpdt_430_memory_inter_jump_lag1_corr_252d_d2(close: pd.Series) -> pd.Series:
    """Memory parameter: corr of inter-jump times at lag 1 over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _mem(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 4:
            return np.nan
        g = np.diff(idx)
        if len(g) < 2:
            return np.nan
        c = np.corrcoef(g[:-1], g[1:])[0, 1]
        return float(c) if np.isfinite(c) else np.nan
    return j.rolling(YDAYS, min_periods=QDAYS).apply(_mem, raw=True).diff().diff()

def f38_jpdt_431_inter_jump_dist_entropy_252d_d2(close: pd.Series) -> pd.Series:
    """Entropy of inter-jump-time histogram (10 bins) over 252d."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _e(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 5:
            return np.nan
        g = np.diff(idx)
        h, _ = np.histogram(g, bins=10)
        p = h.astype(float) / h.sum()
        p = p[p > 0]
        return float(-(p * np.log(p)).sum())
    return j.rolling(YDAYS, min_periods=QDAYS).apply(_e, raw=True).diff().diff()

def f38_jpdt_432_corr_jump_dir_with_5d_trend_252d_d2(close: pd.Series) -> pd.Series:
    """Rolling 252d corr(sign(r) on jump days, sign(5d-trailing-r) on those days)."""
    r = _log_ret(close)
    jmask = r.abs() > 3 * _sigma_prior(r, MDAYS)
    trend = np.sign(_safe_log(close).shift(1) - _safe_log(close.shift(WDAYS + 1)))
    sign_j = np.sign(r).where(jmask, np.nan)
    trend_at_j = trend.where(jmask, np.nan)
    return sign_j.rolling(YDAYS, min_periods=QDAYS).corr(trend_at_j).diff().diff()

def f38_jpdt_433_dn_jump_rate_in_uptrend_252d_d2(close: pd.Series) -> pd.Series:
    """Rate of down-jumps when prior 21d trend is up, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up_trend = _safe_log(close).shift(1) - _safe_log(close.shift(MDAYS + 1)) > 0
    dn_jump = r < -3 * sig
    return (dn_jump & up_trend).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_434_up_jump_rate_in_uptrend_252d_d2(close: pd.Series) -> pd.Series:
    """Rate of up-jumps when prior 21d trend is up, over 252d (in-trend climax)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    up_trend = _safe_log(close).shift(1) - _safe_log(close.shift(MDAYS + 1)) > 0
    up_jump = r > 3 * sig
    return (up_jump & up_trend).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_435_dn_jump_rate_in_downtrend_252d_d2(close: pd.Series) -> pd.Series:
    """Rate of down-jumps when prior 21d trend is down, over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    dn_trend = _safe_log(close).shift(1) - _safe_log(close.shift(MDAYS + 1)) < 0
    dn_jump = r < -3 * sig
    return (dn_jump & dn_trend).astype(float).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_436_net_direction_last_5_jumps_d2(close: pd.Series) -> pd.Series:
    """Sum of signs of last 5 jump events (within 252d window)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    jmask = r.abs() > 3 * sig
    sign_j = np.sign(r).where(jmask, np.nan).fillna(0.0)

    def _last5(w):
        last_signs = w[w != 0][-5:]
        if len(last_signs) < 3:
            return np.nan
        return float(last_signs.sum())
    return sign_j.rolling(YDAYS, min_periods=QDAYS).apply(_last5, raw=True).diff().diff()

def f38_jpdt_437_markov_pneg_given_neg_252d_d2(close: pd.Series) -> pd.Series:
    """Markov P(next-jump=neg | current-jump=neg) over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sign_j = np.sign(r).where(r.abs() > 3 * sig, 0.0).fillna(0.0)
    return sign_j.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _jump_sign_transitions(w, -1, -1), raw=True).diff().diff()

def f38_jpdt_438_markov_ppos_given_neg_252d_d2(close: pd.Series) -> pd.Series:
    """Markov P(next-jump=pos | current-jump=neg) over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sign_j = np.sign(r).where(r.abs() > 3 * sig, 0.0).fillna(0.0)
    return sign_j.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _jump_sign_transitions(w, -1, 1), raw=True).diff().diff()

def f38_jpdt_439_markov_pneg_given_pos_252d_d2(close: pd.Series) -> pd.Series:
    """Markov P(next-jump=neg | current-jump=pos) over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sign_j = np.sign(r).where(r.abs() > 3 * sig, 0.0).fillna(0.0)
    return sign_j.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _jump_sign_transitions(w, 1, -1), raw=True).diff().diff()

def f38_jpdt_440_markov_ppos_given_pos_252d_d2(close: pd.Series) -> pd.Series:
    """Markov P(next-jump=pos | current-jump=pos) over 252d."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sign_j = np.sign(r).where(r.abs() > 3 * sig, 0.0).fillna(0.0)
    return sign_j.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _jump_sign_transitions(w, 1, 1), raw=True).diff().diff()

def f38_jpdt_441_jump_chain_steady_neg_252d_d2(close: pd.Series) -> pd.Series:
    """Steady-state P(neg) from 2-state Markov chain on jump signs over 252d (inlined transitions)."""
    r = _log_ret(close)
    sig = _sigma_prior(r, MDAYS)
    sign_j = np.sign(r).where(r.abs() > 3 * sig, 0.0).fillna(0.0)
    p_neg_given_pos = sign_j.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _jump_sign_transitions(w, 1, -1), raw=True)
    p_neg_given_neg = sign_j.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: _jump_sign_transitions(w, -1, -1), raw=True)
    p_pos_given_neg = 1.0 - p_neg_given_neg
    return _safe_div(p_neg_given_pos, p_neg_given_pos + p_pos_given_neg).diff().diff()

def f38_jpdt_442_realized_5bar_reversal_count_252d_d2(close: pd.Series) -> pd.Series:
    """5-bar momentum reversal: sign(r_t+5_trailing) ≠ sign(r_t-5_trailing) — count over 252d."""
    r5 = _safe_log(close) - _safe_log(close.shift(WDAYS))
    r5_lag = r5.shift(WDAYS)
    reversal = (np.sign(r5) != np.sign(r5_lag)) & (np.sign(r5) != 0)
    return reversal.astype(float).rolling(YDAYS, min_periods=QDAYS).sum().diff().diff()

def f38_jpdt_443_jump_location_entropy_21d_d2(close: pd.Series) -> pd.Series:
    """Jump-location entropy: how uniformly jumps are distributed within trailing 21d (1=uniform)."""
    r = _log_ret(close)
    j = (r.abs() > 3 * _sigma_prior(r, MDAYS)).astype(float).fillna(0.0)

    def _le(w):
        idx = np.where(w > 0.5)[0]
        if len(idx) < 2:
            return np.nan
        n = len(w)
        expected = np.arange(1, len(idx) + 1) * n / (len(idx) + 1)
        d = np.max(np.abs(idx - expected)) / n
        return float(1.0 - d)
    return j.rolling(MDAYS, min_periods=WDAYS).apply(_le, raw=True).diff().diff()

def f38_jpdt_444_rv_5d_over_252d_ratio_d2(close: pd.Series) -> pd.Series:
    """Realized variance in last 5d / last 252d ratio (vol acceleration)."""
    r2 = _log_ret(close) ** 2
    return _safe_div(r2.rolling(WDAYS, min_periods=2).sum() / WDAYS, r2.rolling(YDAYS, min_periods=QDAYS).sum() / YDAYS).diff().diff()

def f38_jpdt_445_mean_abs_r_high_volume_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean |r| restricted to volume z-score > 2 days over 252d."""
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    r = _log_ret(close).abs()
    return r.where(vz > 2.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_446_mean_abs_r_low_volume_252d_d2(close: pd.Series, volume: pd.Series) -> pd.Series:
    """Mean |r| restricted to volume z-score < −1 days over 252d (decoupled magnitude)."""
    vz = _rolling_zscore(volume, QDAYS).shift(1)
    r = _log_ret(close).abs()
    return r.where(vz < -1.0, np.nan).rolling(YDAYS, min_periods=QDAYS).mean().diff().diff()

def f38_jpdt_447_median_abs_r_drift_252d_minus_21d_d2(close: pd.Series) -> pd.Series:
    """Median |r| over 252d − median |r| over 21d — regime drift in central magnitude."""
    a = _log_ret(close).abs()
    return (a.rolling(YDAYS, min_periods=QDAYS).median() - a.rolling(MDAYS, min_periods=WDAYS).median()).diff().diff()

def f38_jpdt_448_mad_returns_252d_over_21d_d2(close: pd.Series) -> pd.Series:
    """MAD of r over 252d / MAD over 21d — long-vs-short central dispersion ratio."""
    r = _log_ret(close)
    mad252 = (r - r.rolling(YDAYS, min_periods=QDAYS).median()).abs().rolling(YDAYS, min_periods=QDAYS).median()
    mad21 = (r - r.rolling(MDAYS, min_periods=WDAYS).median()).abs().rolling(MDAYS, min_periods=WDAYS).median()
    return _safe_div(mad252, mad21).diff().diff()

def f38_jpdt_449_num_magnitude_regimes_252d_d2(close: pd.Series) -> pd.Series:
    """Count of distinct |r|-bins active in 252d: histogram bins with >5% mass."""
    r = _log_ret(close).abs()

    def _n_active(w):
        ww = w[~np.isnan(w)]
        if len(ww) < QDAYS:
            return np.nan
        h, _ = np.histogram(ww, bins=10)
        p = h.astype(float) / h.sum()
        return float((p > 0.05).sum())
    return r.rolling(YDAYS, min_periods=QDAYS).apply(_n_active, raw=True).diff().diff()

def f38_jpdt_450_pct_rank_current_abs_r_252d_d2(close: pd.Series) -> pd.Series:
    """Percentile rank of today's |r| within trailing 252d distribution."""
    a = _log_ret(close).abs()
    return a.rolling(YDAYS, min_periods=QDAYS).apply(lambda w: float((w[-1] >= w).sum() / len(w)) if not np.isnan(w[-1]) else np.nan, raw=True).diff().diff()
JUMP_DETECTION_SIGNATURE_D2_REGISTRY_376_450 = {'f38_jpdt_376_expected_time_to_next_jump_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_376_expected_time_to_next_jump_252d_d2}, 'f38_jpdt_377_jump_hazard_rate_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_377_jump_hazard_rate_252d_d2}, 'f38_jpdt_378_survival_prob_no_jump_5d_d2': {'inputs': ['close'], 'func': f38_jpdt_378_survival_prob_no_jump_5d_d2}, 'f38_jpdt_379_survival_prob_no_jump_21d_d2': {'inputs': ['close'], 'func': f38_jpdt_379_survival_prob_no_jump_21d_d2}, 'f38_jpdt_380_stale_quiet_indicator_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_380_stale_quiet_indicator_252d_d2}, 'f38_jpdt_381_stale_jump_indicator_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_381_stale_jump_indicator_252d_d2}, 'f38_jpdt_382_bars_since_pos_jump_d2': {'inputs': ['close'], 'func': f38_jpdt_382_bars_since_pos_jump_d2}, 'f38_jpdt_383_bars_since_neg_jump_d2': {'inputs': ['close'], 'func': f38_jpdt_383_bars_since_neg_jump_d2}, 'f38_jpdt_384_bayes_post_jump_regime_63d_d2': {'inputs': ['close'], 'func': f38_jpdt_384_bayes_post_jump_regime_63d_d2}, 'f38_jpdt_385_posterior_odds_jump_regime_63d_d2': {'inputs': ['close'], 'func': f38_jpdt_385_posterior_odds_jump_regime_63d_d2}, 'f38_jpdt_386_log_likelihood_returns_normal_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_386_log_likelihood_returns_normal_252d_d2}, 'f38_jpdt_387_log_likelihood_ratio_thick_vs_thin_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_387_log_likelihood_ratio_thick_vs_thin_252d_d2}, 'f38_jpdt_388_local_bayes_factor_63d_d2': {'inputs': ['close'], 'func': f38_jpdt_388_local_bayes_factor_63d_d2}, 'f38_jpdt_389_gap_then_intraday_jump_seq_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_389_gap_then_intraday_jump_seq_252d_d2}, 'f38_jpdt_390_intraday_then_gap_jump_seq_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_390_intraday_then_gap_jump_seq_252d_d2}, 'f38_jpdt_391_c2c_jump_preceded_by_gap_jump_252d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_391_c2c_jump_preceded_by_gap_jump_252d_d2}, 'f38_jpdt_392_triple_jump_coincident_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_392_triple_jump_coincident_252d_d2}, 'f38_jpdt_393_gap_up_then_c2c_dn_seq_252d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_393_gap_up_then_c2c_dn_seq_252d_d2}, 'f38_jpdt_394_gap_dn_then_c2c_up_seq_252d_d2': {'inputs': ['open', 'close'], 'func': f38_jpdt_394_gap_dn_then_c2c_up_seq_252d_d2}, 'f38_jpdt_395_mixed_jump_cooccurrence_rate_252d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_395_mixed_jump_cooccurrence_rate_252d_d2}, 'f38_jpdt_396_corr_gap_intraday_jumps_63d_d2': {'inputs': ['open', 'high', 'low', 'close'], 'func': f38_jpdt_396_corr_gap_intraday_jumps_63d_d2}, 'f38_jpdt_397_vpin_proxy_5d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_397_vpin_proxy_5d_d2}, 'f38_jpdt_398_vpin_proxy_63d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_398_vpin_proxy_63d_d2}, 'f38_jpdt_399_pin_style_imbalance_21d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_399_pin_style_imbalance_21d_d2}, 'f38_jpdt_400_vpin_toxicity_shift_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_400_vpin_toxicity_shift_d2}, 'f38_jpdt_401_vpin_acceleration_5d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_401_vpin_acceleration_5d_d2}, 'f38_jpdt_402_order_flow_toxicity_rolling_21d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_402_order_flow_toxicity_rolling_21d_d2}, 'f38_jpdt_403_jump_day_signed_skew_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_403_jump_day_signed_skew_252d_d2}, 'f38_jpdt_404_nonjump_day_skew_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_404_nonjump_day_skew_252d_d2}, 'f38_jpdt_405_jump_kurtosis_share_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_405_jump_kurtosis_share_252d_d2}, 'f38_jpdt_406_var_contribution_up_jumps_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_406_var_contribution_up_jumps_252d_d2}, 'f38_jpdt_407_var_contribution_dn_jumps_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_407_var_contribution_dn_jumps_252d_d2}, 'f38_jpdt_408_asym_realized_4th_moment_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_408_asym_realized_4th_moment_252d_d2}, 'f38_jpdt_409_mean_pre_jump_vol_rank_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_409_mean_pre_jump_vol_rank_252d_d2}, 'f38_jpdt_410_natr_release_ratio_at_jump_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_410_natr_release_ratio_at_jump_252d_d2}, 'f38_jpdt_411_sigma_ratio_at_jump_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_411_sigma_ratio_at_jump_252d_d2}, 'f38_jpdt_412_volume_ratio_at_jump_252d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_412_volume_ratio_at_jump_252d_d2}, 'f38_jpdt_413_atr_expansion_5d_pre_jump_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_413_atr_expansion_5d_pre_jump_252d_d2}, 'f38_jpdt_414_sigma_shift_after_jump_21d_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_414_sigma_shift_after_jump_21d_252d_d2}, 'f38_jpdt_415_sigma_shift_after_jump_63d_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_415_sigma_shift_after_jump_63d_252d_d2}, 'f38_jpdt_416_natr_shift_after_big_jump_252d_d2': {'inputs': ['high', 'low', 'close'], 'func': f38_jpdt_416_natr_shift_after_big_jump_252d_d2}, 'f38_jpdt_417_avg_post_jump_drift_5d_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_417_avg_post_jump_drift_5d_252d_d2}, 'f38_jpdt_418_post_jump_vol_of_vol_shift_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_418_post_jump_vol_of_vol_shift_252d_d2}, 'f38_jpdt_419_climax_jump_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_419_climax_jump_count_252d_d2}, 'f38_jpdt_420_capitulation_jump_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_420_capitulation_jump_count_252d_d2}, 'f38_jpdt_421_climax_jump_in_uptrend_count_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_421_climax_jump_in_uptrend_count_252d_d2}, 'f38_jpdt_422_panic_jump_count_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_422_panic_jump_count_252d_d2}, 'f38_jpdt_423_jump_after_nr4_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_423_jump_after_nr4_count_252d_d2}, 'f38_jpdt_424_jump_after_wr7_count_252d_d2': {'inputs': ['close', 'high', 'low'], 'func': f38_jpdt_424_jump_after_wr7_count_252d_d2}, 'f38_jpdt_425_jump_storm_count_63d_d2': {'inputs': ['close'], 'func': f38_jpdt_425_jump_storm_count_63d_d2}, 'f38_jpdt_426_full_climax_pattern_count_252d_d2': {'inputs': ['close', 'high', 'low', 'volume'], 'func': f38_jpdt_426_full_climax_pattern_count_252d_d2}, 'f38_jpdt_427_var_inter_jump_times_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_427_var_inter_jump_times_252d_d2}, 'f38_jpdt_428_cv_jump_magnitudes_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_428_cv_jump_magnitudes_252d_d2}, 'f38_jpdt_429_burstiness_inter_jump_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_429_burstiness_inter_jump_252d_d2}, 'f38_jpdt_430_memory_inter_jump_lag1_corr_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_430_memory_inter_jump_lag1_corr_252d_d2}, 'f38_jpdt_431_inter_jump_dist_entropy_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_431_inter_jump_dist_entropy_252d_d2}, 'f38_jpdt_432_corr_jump_dir_with_5d_trend_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_432_corr_jump_dir_with_5d_trend_252d_d2}, 'f38_jpdt_433_dn_jump_rate_in_uptrend_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_433_dn_jump_rate_in_uptrend_252d_d2}, 'f38_jpdt_434_up_jump_rate_in_uptrend_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_434_up_jump_rate_in_uptrend_252d_d2}, 'f38_jpdt_435_dn_jump_rate_in_downtrend_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_435_dn_jump_rate_in_downtrend_252d_d2}, 'f38_jpdt_436_net_direction_last_5_jumps_d2': {'inputs': ['close'], 'func': f38_jpdt_436_net_direction_last_5_jumps_d2}, 'f38_jpdt_437_markov_pneg_given_neg_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_437_markov_pneg_given_neg_252d_d2}, 'f38_jpdt_438_markov_ppos_given_neg_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_438_markov_ppos_given_neg_252d_d2}, 'f38_jpdt_439_markov_pneg_given_pos_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_439_markov_pneg_given_pos_252d_d2}, 'f38_jpdt_440_markov_ppos_given_pos_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_440_markov_ppos_given_pos_252d_d2}, 'f38_jpdt_441_jump_chain_steady_neg_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_441_jump_chain_steady_neg_252d_d2}, 'f38_jpdt_442_realized_5bar_reversal_count_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_442_realized_5bar_reversal_count_252d_d2}, 'f38_jpdt_443_jump_location_entropy_21d_d2': {'inputs': ['close'], 'func': f38_jpdt_443_jump_location_entropy_21d_d2}, 'f38_jpdt_444_rv_5d_over_252d_ratio_d2': {'inputs': ['close'], 'func': f38_jpdt_444_rv_5d_over_252d_ratio_d2}, 'f38_jpdt_445_mean_abs_r_high_volume_252d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_445_mean_abs_r_high_volume_252d_d2}, 'f38_jpdt_446_mean_abs_r_low_volume_252d_d2': {'inputs': ['close', 'volume'], 'func': f38_jpdt_446_mean_abs_r_low_volume_252d_d2}, 'f38_jpdt_447_median_abs_r_drift_252d_minus_21d_d2': {'inputs': ['close'], 'func': f38_jpdt_447_median_abs_r_drift_252d_minus_21d_d2}, 'f38_jpdt_448_mad_returns_252d_over_21d_d2': {'inputs': ['close'], 'func': f38_jpdt_448_mad_returns_252d_over_21d_d2}, 'f38_jpdt_449_num_magnitude_regimes_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_449_num_magnitude_regimes_252d_d2}, 'f38_jpdt_450_pct_rank_current_abs_r_252d_d2': {'inputs': ['close'], 'func': f38_jpdt_450_pct_rank_current_abs_r_252d_d2}}