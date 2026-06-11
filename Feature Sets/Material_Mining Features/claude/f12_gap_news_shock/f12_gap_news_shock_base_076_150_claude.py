import inspect
import numpy as np
import pandas as pd

TRADING_DAYS_YEAR = 252
TRADING_DAYS_TWOYEAR = 504
TRADING_DAYS_HALF = 126
TRADING_DAYS_QUARTER = 63
TRADING_DAYS_MONTH = 21
TRADING_DAYS_WEEK = 5


# ===== generic helpers =====
def _z(s, w):
    m = s.rolling(w, min_periods=max(1, w // 2)).mean()
    sd = s.rolling(w, min_periods=max(1, w // 2)).std()
    return (s - m) / sd.replace(0, np.nan)


def _mean(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).mean()


def _std(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).std()


def _safe_div(a, b):
    return a / b.replace(0, np.nan)


def _rmax(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).max()


def _rmin(s, w):
    return s.rolling(w, min_periods=max(1, w // 2)).min()


# ===== folder domain primitives (gap / news shock) =====
def _f12_gap(openp, close):
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _f12_intraday(openp, close):
    return close / openp.replace(0, np.nan) - 1.0


def _f12_overnight_ret(openp, close):
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _f12_abs_gap(openp, close):
    return (_f12_gap(openp, close)).abs()


def _f12_gap_up_fill(openp, high, low, close):
    pc = close.shift(1)
    gap = openp - pc
    filled = (openp - low).clip(lower=0.0)
    return (filled / gap.replace(0, np.nan)).where(gap > 0, np.nan)


def _f12_gap_dn_fill(openp, high, low, close):
    pc = close.shift(1)
    gap = pc - openp
    recovered = (high - openp).clip(lower=0.0)
    return (recovered / gap.replace(0, np.nan)).where(gap > 0, np.nan)


# ============================================================
# 3-day cumulative overnight gap (multi-session news drift)
def f12gn_f12_gap_news_shock_cumgap_3d_base_v076_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(3, min_periods=2).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 63d cumulative overnight gap (quarter overnight drift)
def f12gn_f12_gap_news_shock_cumgap_63d_base_v077_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of 5d overnight drift to 63d overnight drift (overnight momentum term-structure)
def f12gn_f12_gap_news_shock_ondriftratio_base_v078_signal(open, close):
    g = _f12_gap(open, close)
    s = g.rolling(5, min_periods=3).mean()
    l = g.rolling(63, min_periods=21).mean()
    b = s - l
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drift acceleration: 21d gap mean now vs 21d ago (news regime change)
def f12gn_f12_gap_news_shock_ondriftaccel_base_v079_signal(open, close):
    g = _f12_gap(open, close)
    m = g.rolling(21, min_periods=10).mean()
    b = m - m.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d realized overnight QV minus intraday QV (overnight-dominance of variance)
def f12gn_f12_gap_news_shock_qvdiff_21d_base_v080_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    b = (on ** 2).rolling(21, min_periods=10).sum() - (intra ** 2).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap energy concentration: max squared gap over sum of squared gaps in 21d (single-event share)
def f12gn_f12_gap_news_shock_gapconc_21d_base_v081_signal(open, close):
    g2 = _f12_gap(open, close) ** 2
    b = g2.rolling(21, min_periods=10).max() / g2.rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap Herfindahl over 63d (concentration of overnight variance in few events)
def f12gn_f12_gap_news_shock_gaphhi_63d_base_v082_signal(open, close):
    g2 = _f12_gap(open, close) ** 2
    tot = g2.rolling(63, min_periods=21).sum()
    share = g2 / tot.replace(0, np.nan)
    b = (share ** 2).rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of overnight sign flips over 21d (overnight choppiness / news whipsaw)
def f12gn_f12_gap_news_shock_signflip_21d_base_v083_signal(open, close):
    g = _f12_gap(open, close)
    flip = (np.sign(g) != np.sign(g.shift(1))).astype(float)
    b = (flip * g.abs()).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average gap magnitude on volume-spike days minus on quiet days over 63d (news premium)
def f12gn_f12_gap_news_shock_gapvolpremium_63d_base_v084_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    vmed = volume.rolling(63, min_periods=21).median()
    spike = ag.where(volume > vmed).rolling(63, min_periods=15).mean()
    quiet = ag.where(volume <= vmed).rolling(63, min_periods=15).mean()
    b = spike - quiet
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# correlation of |gap| with volume over 63d (do shocks come with volume? news confirmation)
def f12gn_f12_gap_news_shock_gapvolcorr_63d_base_v085_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    b = ag.rolling(63, min_periods=21).corr(volume)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# dollar-flow-weighted overnight drift over 21d (where volume agrees with gaps)
def f12gn_f12_gap_news_shock_vwdrift_21d_base_v086_signal(open, close, volume):
    g = _f12_gap(open, close)
    w = volume / _mean(volume, 21).replace(0, np.nan)
    b = (g * w).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# volume surge on the single largest-|gap| day in trailing 21d (news-day volume signature)
def f12gn_f12_gap_news_shock_shockvol_21d_base_v087_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)

    def _pick(idx_vals):
        return idx_vals
    big_day = (ag == ag.rolling(21, min_periods=10).max()).astype(float)
    b = (vsurge * big_day).rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up follow vs gap-down follow asymmetry in intraday over 63d (directional reaction)
def f12gn_f12_gap_news_shock_reactionasym_63d_base_v088_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    up_react = intra.where(g > 0).rolling(63, min_periods=15).mean()
    dn_react = intra.where(g < 0).rolling(63, min_periods=15).mean()
    b = up_react - dn_react
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average up-gap fill minus average down-gap fill over 21d (fade asymmetry, short window)
def f12gn_f12_gap_news_shock_fillasym_21d_base_v089_signal(open, high, low, close):
    uf = _f12_gap_up_fill(open, high, low, close).rolling(21, min_periods=5).mean()
    df = _f12_gap_dn_fill(open, high, low, close).rolling(21, min_periods=5).mean()
    b = uf - df
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net gap closed by end of day: (close - prior close) sign vs gap sign agreement over 63d
def f12gn_f12_gap_news_shock_gapclose_63d_base_v090_signal(open, close):
    g = _f12_gap(open, close)
    pc = close.shift(1)
    tot = close / pc.replace(0, np.nan) - 1.0
    fade = (np.sign(g) != np.sign(tot)).astype(float)
    b = (fade * g.abs()).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean overshoot past prior close when a gap fully reverses intraday, 63d (reversal force)
def f12gn_f12_gap_news_shock_fullreverse_63d_base_v091_signal(open, close):
    g = _f12_gap(open, close)
    pc = close.shift(1)
    tot = close / pc.replace(0, np.nan) - 1.0
    overshoot = (-np.sign(g) * tot).clip(lower=0.0)
    b = overshoot.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-return autocorrelation at lag 1 over 126d (overnight predictability)
def f12gn_f12_gap_news_shock_onautocorr_126d_base_v092_signal(open, close):
    on = _f12_overnight_ret(open, close)
    b = on.rolling(126, min_periods=63).corr(on.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cross-corr: today's gap vs yesterday's intraday over 63d (session-to-overnight spillover)
def f12gn_f12_gap_news_shock_spillover_63d_base_v093_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    b = g.rolling(63, min_periods=21).corr(intra.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap dispersion ratio: 21d gap std over 126d gap std (overnight vol expansion)
def f12gn_f12_gap_news_shock_gapvolexp_base_v094_signal(open, close):
    g = _f12_gap(open, close)
    b = _std(g, 21) / _std(g, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vol-of-vol: std of the 21d rolling gap std over 63d (shock-regime instability)
def f12gn_f12_gap_news_shock_gapvov_63d_base_v095_signal(open, close):
    g = _f12_gap(open, close)
    v = _std(g, 21)
    b = _std(v, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# tail-gap count over 63d above own 95th-pct, normalized (extreme-shock frequency)
def f12gn_f12_gap_news_shock_tailgap_63d_base_v096_signal(open, close):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(252, min_periods=126).quantile(0.95)
    excess = (ag - thr).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# expected-shortfall of overnight returns over 63d (mean of worst-decile overnight gaps)
def f12gn_f12_gap_news_shock_ones_63d_base_v097_signal(open, close):
    on = _f12_overnight_ret(open, close)

    def _es(a):
        k = max(1, int(len(a) * 0.10))
        return float(np.mean(np.sort(a)[:k]))
    b = on.rolling(63, min_periods=21).apply(_es, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# upside overnight tail: mean of best-decile overnight gaps over 63d (positive-news magnitude)
def f12gn_f12_gap_news_shock_onesup_63d_base_v098_signal(open, close):
    on = _f12_overnight_ret(open, close)

    def _esup(a):
        k = max(1, int(len(a) * 0.10))
        return float(np.mean(np.sort(a)[-k:]))
    b = on.rolling(63, min_periods=21).apply(_esup, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight tail asymmetry: upside ES plus downside ES over 63d (net tail bias)
def f12gn_f12_gap_news_shock_tailasym_63d_base_v099_signal(open, close):
    on = _f12_overnight_ret(open, close)

    def _asym(a):
        k = max(1, int(len(a) * 0.10))
        s = np.sort(a)
        return float(np.mean(s[-k:]) + np.mean(s[:k]))
    b = on.rolling(63, min_periods=21).apply(_asym, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of total 21d return delivered overnight while market closed (overnight capture)
def f12gn_f12_gap_news_shock_oncapture_21d_base_v100_signal(open, close):
    on = _f12_overnight_ret(open, close)
    pc = close.shift(1)
    tot = close / pc.replace(0, np.nan) - 1.0
    onsum = on.rolling(21, min_periods=10).sum()
    totsum = tot.rolling(21, min_periods=10).sum()
    b = onsum / totsum.replace(0, np.nan)
    result = b
    result = result.clip(-5, 5)
    return result.replace([np.inf, -np.inf], np.nan)


# gap-then-trend: does a big up-gap precede continued 5d strength (post-shock drift) 63d corr
def f12gn_f12_gap_news_shock_postdrift_63d_base_v101_signal(open, close):
    g = _f12_gap(open, close)
    fwd = close.shift(-5) / close - 1.0
    b = g.rolling(63, min_periods=21).corr(fwd)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest absolute gap in 21d expressed in 63d gap-std units (shock z-extreme)
def f12gn_f12_gap_news_shock_maxgapz_21d_base_v102_signal(open, close):
    ag = _f12_abs_gap(open, close)
    mx = ag.rolling(21, min_periods=10).max()
    sd = _std(_f12_gap(open, close), 63)
    b = mx / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# number of distinct up-gap episodes (entries) over 63d above own 80th pct
def f12gn_f12_gap_news_shock_upepisodes_63d_base_v103_signal(open, close):
    g = _f12_gap(open, close)
    thr = g.abs().rolling(126, min_periods=63).quantile(0.80)
    flag = (g >= thr).astype(float)
    entry = ((flag == 1) & (flag.shift(1) == 0)).astype(float)
    b = entry.rolling(63, min_periods=21).sum() + g.clip(lower=0).rolling(21, min_periods=10).mean() * 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-gap episode entries over 63d (distress-news clustering)
def f12gn_f12_gap_news_shock_dnepisodes_63d_base_v104_signal(open, close):
    g = _f12_gap(open, close)
    thr = g.abs().rolling(126, min_periods=63).quantile(0.80)
    flag = (g <= -thr).astype(float)
    entry = ((flag == 1) & (flag.shift(1) == 0)).astype(float)
    b = entry.rolling(63, min_periods=21).sum() + (-g.clip(upper=0)).rolling(21, min_periods=10).mean() * 50.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drawdown duration: fraction of 63d the overnight equity curve is below its peak
def f12gn_f12_gap_news_shock_onunderwater_63d_base_v105_signal(open, close):
    on = _f12_overnight_ret(open, close)
    eq = on.cumsum()
    peak = eq.rolling(252, min_periods=63).max()
    under = (eq < peak).astype(float)
    b = under.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recovery quality after a down-gap: avg 3d forward return following down-gaps, 63d
def f12gn_f12_gap_news_shock_dngaprebound_63d_base_v106_signal(open, close):
    g = _f12_gap(open, close)
    fwd = close.shift(-3) / close - 1.0
    rb = fwd.where(g < 0)
    b = rb.rolling(63, min_periods=15).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# follow-through after an up-gap: avg 3d forward return following up-gaps, 63d
def f12gn_f12_gap_news_shock_upgapfollow_63d_base_v107_signal(open, close):
    g = _f12_gap(open, close)
    fwd = close.shift(-3) / close - 1.0
    ft = fwd.where(g > 0)
    b = ft.rolling(63, min_periods=15).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-open extremity within prior-week range (open vs prior 5d high/low position)
def f12gn_f12_gap_news_shock_openvswk_1d_base_v108_signal(open, high, low):
    hi = high.shift(1).rolling(5, min_periods=3).max()
    lo = low.shift(1).rolling(5, min_periods=3).min()
    b = (open - lo) / (hi - lo).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap jump beyond prior 5d range, normalized by prior close (weekly breakaway shock)
def f12gn_f12_gap_news_shock_wkbreak_1d_base_v109_signal(open, high, low, close):
    hi = high.shift(1).rolling(5, min_periods=3).max()
    lo = low.shift(1).rolling(5, min_periods=3).min()
    pc = close.shift(1)
    up = (open - hi).clip(lower=0)
    dn = (lo - open).clip(lower=0)
    b = (up - dn) / pc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap magnitude relative to prior-day intraday range (gap vs yesterday's range)
def f12gn_f12_gap_news_shock_gapvsrange_1d_base_v110_signal(open, high, low, close):
    pc = close.shift(1)
    pr = (high.shift(1) - low.shift(1))
    b = (open - pc) / pr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d mean of gap-to-prior-range ratio (persistent gap-vs-range regime)
def f12gn_f12_gap_news_shock_gapvsrange_21d_base_v111_signal(open, high, low, close):
    pc = close.shift(1)
    pr = (high.shift(1) - low.shift(1))
    r = (open - pc) / pr.replace(0, np.nan)
    b = r.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight contribution to 63d high: did new highs come from gaps? (gap-led breakout)
def f12gn_f12_gap_news_shock_gapledhigh_63d_base_v112_signal(open, close):
    g = _f12_gap(open, close)
    at_high = (close >= close.rolling(63, min_periods=21).max() * 0.999).astype(float)
    gap_at_high = (g * at_high)
    b = gap_at_high.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight contribution to 63d low: gap-led breakdowns (capitulation gaps)
def f12gn_f12_gap_news_shock_gapledlow_63d_base_v113_signal(open, close):
    g = _f12_gap(open, close)
    at_low = (close <= close.rolling(63, min_periods=21).min() * 1.001).astype(float)
    gap_at_low = (g * at_low)
    b = gap_at_low.rolling(63, min_periods=21).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight skewness over 126d (long-horizon news asymmetry)
def f12gn_f12_gap_news_shock_onskew_126d_base_v114_signal(open, close):
    on = _f12_overnight_ret(open, close)
    b = on.rolling(126, min_periods=63).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight kurtosis over 126d (long-horizon event-tail intensity)
def f12gn_f12_gap_news_shock_onkurt_126d_base_v115_signal(open, close):
    on = _f12_overnight_ret(open, close)
    b = on.rolling(126, min_periods=63).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap directional balance over 63d (net sign bias of overnight gaps, news one-sidedness)
def f12gn_f12_gap_news_shock_gapsignbal_21d_base_v116_signal(open, close):
    g = _f12_gap(open, close)
    s = np.sign(g)
    b = s.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# weighted overnight momentum: gaps weighted by linear recency over 21d
def f12gn_f12_gap_news_shock_recentgap_21d_base_v117_signal(open, close):
    g = _f12_gap(open, close)
    w = np.arange(1, 22)

    def _wsum(a):
        return float(np.dot(a, w) / w.sum())
    b = g.rolling(21, min_periods=21).apply(_wsum, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap consistency: 21d gap mean divided by 21d gap mean-abs (directional purity)
def f12gn_f12_gap_news_shock_gappurity_21d_base_v118_signal(open, close):
    g = _f12_gap(open, close)
    m = g.rolling(21, min_periods=10).mean()
    ma = g.abs().rolling(21, min_periods=10).mean()
    b = m / ma.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest down-gap (worst single overnight) over 63d (max overnight loss)
def f12gn_f12_gap_news_shock_worstgap_63d_base_v119_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest up-gap (best single overnight) over 63d (max overnight pop)
def f12gn_f12_gap_news_shock_bestgap_63d_base_v120_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(63, min_periods=21).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap range over mean abs gap (peak-to-typical shock multiple) 63d
def f12gn_f12_gap_news_shock_gappeakratio_63d_base_v121_signal(open, close):
    g = _f12_gap(open, close)
    rng = g.rolling(63, min_periods=21).max() - g.rolling(63, min_periods=21).min()
    typ = g.abs().rolling(63, min_periods=21).mean()
    b = rng / typ.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight downside semideviation level over 63d (raw overnight downside risk)
def f12gn_f12_gap_news_shock_onsortino_63d_base_v122_signal(open, close):
    on = _f12_overnight_ret(open, close)
    dn = on.clip(upper=0.0)
    b = (dn ** 2).rolling(63, min_periods=21).mean() ** 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight information ratio over 126d (medium-horizon overnight drift per unit gap-vol)
def f12gn_f12_gap_news_shock_onwinrate_63d_base_v123_signal(open, close):
    g = _f12_gap(open, close)
    b = _mean(g, 126) / _std(g, 126).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# news intensity index: product of |gap| z and volume z, 63d mean (joint-shock score)
def f12gn_f12_gap_news_shock_newsintensity_63d_base_v124_signal(open, close, volume):
    agz = _z(_f12_abs_gap(open, close), 63)
    vz = _z(volume, 63)
    b = (agz * vz).rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# days since last volume-confirmed gap (|gap| & volume both above own 80th pct), 126d
def f12gn_f12_gap_news_shock_confgaprecency_base_v125_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    gthr = ag.rolling(126, min_periods=63).quantile(0.80)
    vthr = volume.rolling(126, min_periods=63).quantile(0.80)
    flag = ((ag >= gthr) & (volume >= vthr)).astype(float)

    def _dsl(a):
        idx = np.where(a > 0.5)[0]
        if len(idx) == 0:
            return float(len(a))
        return float(len(a) - 1 - idx[-1])
    b = flag.rolling(63, min_periods=21).apply(_dsl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vs intraday vol-ratio change over 21d (shifting risk location)
def f12gn_f12_gap_news_shock_riskshift_21d_base_v126_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    ratio = _std(on, 21) / _std(intra, 21).replace(0, np.nan)
    b = ratio - ratio.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of up days that gapped up (gap-led up days) over 63d
def f12gn_f12_gap_news_shock_gapledup_63d_base_v127_signal(open, close):
    g = _f12_gap(open, close)
    pc = close.shift(1)
    upday = (close > pc).astype(float)
    gapled = ((close > pc) & (g > 0)).astype(float)
    b = gapled.rolling(63, min_periods=21).sum() / upday.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative overnight-vs-intraday equity divergence over 126d (structural overnight alpha)
def f12gn_f12_gap_news_shock_eqdiverge_126d_base_v128_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    b = on.rolling(126, min_periods=63).sum() - intra.rolling(126, min_periods=63).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-gap range compression: 5d gap range over 63d gap range (gap-range squeeze)
def f12gn_f12_gap_news_shock_gapsurprise_base_v129_signal(open, close):
    g = _f12_gap(open, close)
    r5 = g.rolling(5, min_periods=3).max() - g.rolling(5, min_periods=3).min()
    r63 = g.rolling(63, min_periods=21).max() - g.rolling(63, min_periods=21).min()
    b = r5 / r63.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs-gap percentile of latest day within trailing 252d (long-horizon shock extremity)
def f12gn_f12_gap_news_shock_absgaprank_252d_base_v130_signal(open, close):
    ag = _f12_abs_gap(open, close)
    b = ag.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-fill speed proxy: average (high-low)/|gap| on gap days 63d (intraday reaction range)
def f12gn_f12_gap_news_shock_reactrange_63d_base_v131_signal(open, high, low, close):
    ag = _f12_abs_gap(open, close)
    rng = (high - low) / close.shift(1).replace(0, np.nan)
    ratio = (rng / ag.replace(0, np.nan)).where(ag > 0)
    b = ratio.rolling(63, min_periods=15).median()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# close position within day's range on big-gap days 63d (gap-day strength of close)
def f12gn_f12_gap_news_shock_gapcloseloc_63d_base_v132_signal(open, high, low, close):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(126, min_periods=63).quantile(0.70)
    loc = (close - low) / (high - low).replace(0, np.nan)
    b = loc.where(ag >= thr).rolling(63, min_periods=10).mean() - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversion half-life proxy: 63d corr of gap with next-day -gap (mean reversion strength)
def f12gn_f12_gap_news_shock_gapmeanrev_63d_base_v133_signal(open, close):
    g = _f12_gap(open, close)
    b = -g.rolling(63, min_periods=21).corr(g.shift(-1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of 21d absolute return that occurred via the single biggest gap (event dominance)
def f12gn_f12_gap_news_shock_eventdom_21d_base_v134_signal(open, close):
    ag = _f12_abs_gap(open, close)
    pc = close.shift(1)
    tot = (close / pc.replace(0, np.nan) - 1.0).abs()
    b = ag.rolling(21, min_periods=10).max() / tot.rolling(21, min_periods=10).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight beta to its own lagged abs-gap (volatility clustering of shocks) 63d
def f12gn_f12_gap_news_shock_volcluster_63d_base_v135_signal(open, close):
    ag = _f12_abs_gap(open, close)
    b = ag.rolling(63, min_periods=21).corr(ag.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net gap drift sign-stability: 63d mean of sign(5d cum gap) (persistent overnight direction)
def f12gn_f12_gap_news_shock_driftstable_63d_base_v136_signal(open, close):
    g = _f12_gap(open, close)
    cg = g.rolling(5, min_periods=3).sum()
    b = np.sign(cg).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed gap on the single highest-volume day in trailing 21d (peak news-day gap direction)
def f12gn_f12_gap_news_shock_vwshockskew_63d_base_v137_signal(open, close, volume):
    g = _f12_gap(open, close)
    peakvol = (volume == volume.rolling(21, min_periods=10).max()).astype(float)
    weighted = (g * peakvol)
    b = weighted.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of overnight variance in last 5d vs trailing 63d (acute overnight stress burst)
def f12gn_f12_gap_news_shock_acuteburst_base_v138_signal(open, close):
    on2 = _f12_overnight_ret(open, close) ** 2
    recent = on2.rolling(5, min_periods=3).mean()
    base = on2.rolling(63, min_periods=21).mean()
    b = recent / base.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-and-go quality: mean (gap + same-day intraday in gap direction) on up-gaps 63d
def f12gn_f12_gap_news_shock_gapgoqual_63d_base_v139_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    qual = (g + intra).where(g > 0)
    b = qual.rolling(63, min_periods=15).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-gap capitulation depth: mean (gap + intraday) on down-gaps 63d (full-day damage)
def f12gn_f12_gap_news_shock_capitdepth_63d_base_v140_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    dmg = (g + intra).where(g < 0)
    b = dmg.rolling(63, min_periods=15).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight MACD: fast minus slow EMA of overnight returns, vol-normalized (drift turn)
def f12gn_f12_gap_news_shock_ondriftz_base_v141_signal(open, close):
    on = _f12_overnight_ret(open, close)
    macd = on.ewm(span=10, min_periods=5).mean() - on.ewm(span=42, min_periods=21).mean()
    sd = on.rolling(63, min_periods=21).std()
    b = macd / sd.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# count of two-sided gap days (gap then opposite intraday) over 63d (whipsaw news days)
def f12gn_f12_gap_news_shock_whipsaw_63d_base_v142_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    whip = (((g.abs() > g.abs().rolling(63, min_periods=21).quantile(0.6)) &
            (np.sign(g) != np.sign(intra))).astype(float)) * (g.abs() + intra.abs())
    b = whip.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight variance ratio: var of 5d-summed gaps vs 5x var of 1d gaps (trend vs noise)
def f12gn_f12_gap_news_shock_driftconsist_63d_base_v143_signal(open, close):
    g = _f12_gap(open, close)
    v1 = _std(g, 63) ** 2
    v5 = _std(g.rolling(5, min_periods=3).sum(), 63) ** 2
    b = v5 / (5.0 * v1).replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap impulse-response: ratio of 3d post-gap cum return to the gap itself, 63d median
def f12gn_f12_gap_news_shock_impulse_63d_base_v144_signal(open, close):
    g = _f12_gap(open, close)
    fwd = close.shift(-3) / close - 1.0
    ratio = (fwd / g.replace(0, np.nan)).where(g.abs() > g.abs().rolling(63, min_periods=21).quantile(0.7))
    b = ratio.rolling(63, min_periods=10).median()
    result = b
    result = result.clip(-10, 10)
    return result.replace([np.inf, -np.inf], np.nan)


# overnight max drawdown of cumulative gaps over 126d (worst overnight regime)
def f12gn_f12_gap_news_shock_onmaxdd_126d_base_v145_signal(open, close):
    on = _f12_overnight_ret(open, close)
    eq = on.cumsum()
    peak = eq.rolling(126, min_periods=63).max()
    b = (eq - peak).rolling(126, min_periods=63).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap volatility term-structure slope: 63d gap std minus 21d gap std (overnight vol curve)
def f12gn_f12_gap_news_shock_gapvolterm_base_v146_signal(open, close):
    g = _f12_gap(open, close)
    b = _std(g, 63) - _std(g, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average absolute gap on the day after a large gap (echo-shock magnitude) 63d
def f12gn_f12_gap_news_shock_echoshock_63d_base_v147_signal(open, close):
    ag = _f12_abs_gap(open, close)
    big_prev = (ag.shift(1) >= ag.shift(1).rolling(126, min_periods=63).quantile(0.85))
    echo = ag.where(big_prev)
    b = echo.rolling(63, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average up-gap size vs average down-gap size over 63d (per-event payoff asymmetry)
def f12gn_f12_gap_news_shock_omega_63d_base_v148_signal(open, close):
    g = _f12_gap(open, close)
    up_mean = g.where(g > 0).rolling(63, min_periods=15).mean()
    dn_mean = (-g.where(g < 0)).rolling(63, min_periods=15).mean()
    b = up_mean / dn_mean.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-frequency trend: 21d tail-gap rate minus 126d tail-gap rate (news intensity ramp)
def f12gn_f12_gap_news_shock_freqtrend_base_v149_signal(open, close):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(126, min_periods=63).quantile(0.80)
    flag = (ag >= thr).astype(float)
    b = flag.rolling(21, min_periods=10).mean() - flag.rolling(126, min_periods=63).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# composite shock score: blended |gap| z, volume z, and gap-vs-range over 21d (news composite)
def f12gn_f12_gap_news_shock_shockscore_21d_base_v150_signal(open, high, low, close, volume):
    agz = _z(_f12_abs_gap(open, close), 63)
    vz = _z(volume, 63)
    pr = (high.shift(1) - low.shift(1))
    gr = (_f12_abs_gap(open, close) * close.shift(1)) / pr.replace(0, np.nan)
    blended = (agz + vz + _z(gr, 63)) / 3.0
    b = blended.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12gn_f12_gap_news_shock_cumgap_3d_base_v076_signal,
    f12gn_f12_gap_news_shock_cumgap_63d_base_v077_signal,
    f12gn_f12_gap_news_shock_ondriftratio_base_v078_signal,
    f12gn_f12_gap_news_shock_ondriftaccel_base_v079_signal,
    f12gn_f12_gap_news_shock_qvdiff_21d_base_v080_signal,
    f12gn_f12_gap_news_shock_gapconc_21d_base_v081_signal,
    f12gn_f12_gap_news_shock_gaphhi_63d_base_v082_signal,
    f12gn_f12_gap_news_shock_signflip_21d_base_v083_signal,
    f12gn_f12_gap_news_shock_gapvolpremium_63d_base_v084_signal,
    f12gn_f12_gap_news_shock_gapvolcorr_63d_base_v085_signal,
    f12gn_f12_gap_news_shock_vwdrift_21d_base_v086_signal,
    f12gn_f12_gap_news_shock_shockvol_21d_base_v087_signal,
    f12gn_f12_gap_news_shock_reactionasym_63d_base_v088_signal,
    f12gn_f12_gap_news_shock_fillasym_21d_base_v089_signal,
    f12gn_f12_gap_news_shock_gapclose_63d_base_v090_signal,
    f12gn_f12_gap_news_shock_fullreverse_63d_base_v091_signal,
    f12gn_f12_gap_news_shock_onautocorr_126d_base_v092_signal,
    f12gn_f12_gap_news_shock_spillover_63d_base_v093_signal,
    f12gn_f12_gap_news_shock_gapvolexp_base_v094_signal,
    f12gn_f12_gap_news_shock_gapvov_63d_base_v095_signal,
    f12gn_f12_gap_news_shock_tailgap_63d_base_v096_signal,
    f12gn_f12_gap_news_shock_ones_63d_base_v097_signal,
    f12gn_f12_gap_news_shock_onesup_63d_base_v098_signal,
    f12gn_f12_gap_news_shock_tailasym_63d_base_v099_signal,
    f12gn_f12_gap_news_shock_oncapture_21d_base_v100_signal,
    f12gn_f12_gap_news_shock_postdrift_63d_base_v101_signal,
    f12gn_f12_gap_news_shock_maxgapz_21d_base_v102_signal,
    f12gn_f12_gap_news_shock_upepisodes_63d_base_v103_signal,
    f12gn_f12_gap_news_shock_dnepisodes_63d_base_v104_signal,
    f12gn_f12_gap_news_shock_onunderwater_63d_base_v105_signal,
    f12gn_f12_gap_news_shock_dngaprebound_63d_base_v106_signal,
    f12gn_f12_gap_news_shock_upgapfollow_63d_base_v107_signal,
    f12gn_f12_gap_news_shock_openvswk_1d_base_v108_signal,
    f12gn_f12_gap_news_shock_wkbreak_1d_base_v109_signal,
    f12gn_f12_gap_news_shock_gapvsrange_1d_base_v110_signal,
    f12gn_f12_gap_news_shock_gapvsrange_21d_base_v111_signal,
    f12gn_f12_gap_news_shock_gapledhigh_63d_base_v112_signal,
    f12gn_f12_gap_news_shock_gapledlow_63d_base_v113_signal,
    f12gn_f12_gap_news_shock_onskew_126d_base_v114_signal,
    f12gn_f12_gap_news_shock_onkurt_126d_base_v115_signal,
    f12gn_f12_gap_news_shock_gapsignbal_21d_base_v116_signal,
    f12gn_f12_gap_news_shock_recentgap_21d_base_v117_signal,
    f12gn_f12_gap_news_shock_gappurity_21d_base_v118_signal,
    f12gn_f12_gap_news_shock_worstgap_63d_base_v119_signal,
    f12gn_f12_gap_news_shock_bestgap_63d_base_v120_signal,
    f12gn_f12_gap_news_shock_gappeakratio_63d_base_v121_signal,
    f12gn_f12_gap_news_shock_onsortino_63d_base_v122_signal,
    f12gn_f12_gap_news_shock_onwinrate_63d_base_v123_signal,
    f12gn_f12_gap_news_shock_newsintensity_63d_base_v124_signal,
    f12gn_f12_gap_news_shock_confgaprecency_base_v125_signal,
    f12gn_f12_gap_news_shock_riskshift_21d_base_v126_signal,
    f12gn_f12_gap_news_shock_gapledup_63d_base_v127_signal,
    f12gn_f12_gap_news_shock_eqdiverge_126d_base_v128_signal,
    f12gn_f12_gap_news_shock_gapsurprise_base_v129_signal,
    f12gn_f12_gap_news_shock_absgaprank_252d_base_v130_signal,
    f12gn_f12_gap_news_shock_reactrange_63d_base_v131_signal,
    f12gn_f12_gap_news_shock_gapcloseloc_63d_base_v132_signal,
    f12gn_f12_gap_news_shock_gapmeanrev_63d_base_v133_signal,
    f12gn_f12_gap_news_shock_eventdom_21d_base_v134_signal,
    f12gn_f12_gap_news_shock_volcluster_63d_base_v135_signal,
    f12gn_f12_gap_news_shock_driftstable_63d_base_v136_signal,
    f12gn_f12_gap_news_shock_vwshockskew_63d_base_v137_signal,
    f12gn_f12_gap_news_shock_acuteburst_base_v138_signal,
    f12gn_f12_gap_news_shock_gapgoqual_63d_base_v139_signal,
    f12gn_f12_gap_news_shock_capitdepth_63d_base_v140_signal,
    f12gn_f12_gap_news_shock_ondriftz_base_v141_signal,
    f12gn_f12_gap_news_shock_whipsaw_63d_base_v142_signal,
    f12gn_f12_gap_news_shock_driftconsist_63d_base_v143_signal,
    f12gn_f12_gap_news_shock_impulse_63d_base_v144_signal,
    f12gn_f12_gap_news_shock_onmaxdd_126d_base_v145_signal,
    f12gn_f12_gap_news_shock_gapvolterm_base_v146_signal,
    f12gn_f12_gap_news_shock_echoshock_63d_base_v147_signal,
    f12gn_f12_gap_news_shock_omega_63d_base_v148_signal,
    f12gn_f12_gap_news_shock_freqtrend_base_v149_signal,
    f12gn_f12_gap_news_shock_shockscore_21d_base_v150_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_GAP_NEWS_SHOCK_REGISTRY_076_150 = REGISTRY


if __name__ == "__main__":
    np.random.seed(42)
    n = 1500
    rets = np.random.normal(0.0003, 0.035, n)
    closeadj = pd.Series(100.0 * np.exp(np.cumsum(rets)), name="closeadj")
    close = pd.Series(closeadj.values, name="close")
    openp = pd.Series(close.shift(1).fillna(close.iloc[0]).values
                      * (1 + np.random.normal(0, 0.01, n)), name="open")
    high = pd.Series(np.maximum(close, openp)
                     * (1 + np.abs(np.random.normal(0, 0.02, n))), name="high")
    low = pd.Series(np.minimum(close, openp)
                    * (1 - np.abs(np.random.normal(0, 0.02, n))), name="low")
    volume = pd.Series(np.abs(np.random.normal(8e5, 5e5, n)) + 1e4, name="volume")

    cols = {"closeadj": closeadj, "close": close, "open": openp,
            "high": high, "low": low, "volume": volume}

    n_features = 0
    nan_ok = 0
    results = {}
    for name, meta in REGISTRY.items():
        fn = meta["func"]
        args = [cols[c] for c in meta["inputs"]]
        y1 = fn(*args)
        y2 = fn(*args)
        pd.testing.assert_series_equal(y1, y2)
        q = y1.iloc[504:].dropna()
        assert len(q) > 0, name
        assert q.nunique() > 20, "%s nunique=%d" % (name, q.nunique())
        assert q.std() > 0, name
        assert not q.isna().all(), name
        nan_ratio = y1.iloc[504:].isna().mean()
        if nan_ratio < 0.5:
            nan_ok += 1
        results[name] = y1.iloc[504:]
        n_features += 1

    assert n_features == 75, n_features
    assert nan_ok >= int(0.8 * n_features), "nan_ok=%d/%d" % (nan_ok, n_features)

    items = list(results.items())
    for i in range(len(items)):
        ni, si = items[i]
        ai = si.dropna()
        for j in range(i + 1, len(items)):
            nj, sj = items[j]
            aj = sj.dropna()
            idx = ai.index.intersection(aj.index)
            if len(idx) < 30:
                continue
            c = ai.loc[idx].corr(aj.loc[idx])
            if c is None or np.isnan(c):
                continue
            assert abs(c) <= 0.97, "CORR %s vs %s = %.4f" % (ni, nj, c)

    print("OK f12_gap_news_shock_base_076_150_claude: %d features pass" % n_features)
