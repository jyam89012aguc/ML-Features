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
    # overnight gap: today's open vs prior close (drill-result / news gap), unadjusted
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _f12_loggap(openp, close):
    pc = close.shift(1)
    return np.log(openp.replace(0, np.nan) / pc.replace(0, np.nan))


def _f12_intraday(openp, close):
    # intraday (open-to-close) return
    return close / openp.replace(0, np.nan) - 1.0


def _f12_overnight_ret(openp, close):
    # overnight return = gap; alias kept distinct for clarity
    pc = close.shift(1)
    return openp / pc.replace(0, np.nan) - 1.0


def _f12_gap_up_fill(openp, high, low, close):
    # for an up-gap, how much of the gap got filled intraday (traded back toward prior close)
    pc = close.shift(1)
    gap = openp - pc
    filled = (openp - low).clip(lower=0.0)
    return (filled / gap.replace(0, np.nan)).where(gap > 0, np.nan)


def _f12_gap_dn_fill(openp, high, low, close):
    # for a down-gap, fraction of the gap recovered intraday (rose back toward prior close)
    pc = close.shift(1)
    gap = pc - openp
    recovered = (high - openp).clip(lower=0.0)
    return (recovered / gap.replace(0, np.nan)).where(gap > 0, np.nan)


def _f12_true_gap(openp, high, low, close):
    # gap that survives intraday: signed distance open keeps beyond prior day's range
    ph = high.shift(1)
    pl = low.shift(1)
    up = (openp - ph).clip(lower=0.0)
    dn = (pl - openp).clip(lower=0.0)
    return (up - dn) / close.shift(1).replace(0, np.nan)


def _f12_abs_gap(openp, close):
    return (_f12_gap(openp, close)).abs()


# ============================================================
# raw overnight gap (open vs prior close) — core news-gap signal
def f12gn_f12_gap_news_shock_gap_1d_base_v001_signal(open, close):
    b = _f12_gap(open, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap percentile rank within its own trailing 63d history (ordinal shock position)
def f12gn_f12_gap_news_shock_loggap_1d_base_v002_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(63, min_periods=21).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute gap magnitude (size of the shock irrespective of direction)
def f12gn_f12_gap_news_shock_absgap_1d_base_v003_signal(open, close):
    b = _f12_abs_gap(open, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday (open-to-close) return — the session reaction after the gap
def f12gn_f12_gap_news_shock_intraday_1d_base_v004_signal(open, close):
    b = _f12_intraday(open, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-vs-intraday tug-of-war, bounded (which leg drove the day, normalized)
def f12gn_f12_gap_news_shock_onvsintra_1d_base_v005_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    b = (on - intra) / (on.abs() + intra.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of the daily move that came overnight (gap dominance of total return)
def f12gn_f12_gap_news_shock_ondom_1d_base_v006_signal(open, close):
    on = _f12_overnight_ret(open, close)
    pc = close.shift(1)
    tot = close / pc.replace(0, np.nan) - 1.0
    b = on / (on.abs() + (tot - on).abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 2-day cumulative gap z-scored vs 63d (consecutive-overnight news clustering)
def f12gn_f12_gap_news_shock_gapz_63d_base_v007_signal(open, close):
    g = _f12_gap(open, close)
    g2 = g + g.shift(1)
    b = _z(g2, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap acceleration: today's gap minus yesterday's gap, scaled by 21d gap std
def f12gn_f12_gap_news_shock_gapz_21d_base_v008_signal(open, close):
    g = _f12_gap(open, close)
    accel = g - g.shift(1)
    b = accel / _std(g, 21).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# shock-size regime: 21d typical |gap| vs 126d typical |gap| (rising/falling shock baseline)
def f12gn_f12_gap_news_shock_gapmult_63d_base_v009_signal(open, close):
    ag = _f12_abs_gap(open, close)
    short = ag.rolling(21, min_periods=10).median()
    long = ag.rolling(126, min_periods=63).median()
    b = short / long.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-to-intraday absolute-move ratio over 5d (which leg carries the shock)
def f12gn_f12_gap_news_shock_gapsigma_21d_base_v010_signal(open, close):
    on = _f12_overnight_ret(open, close).abs()
    intra = _f12_intraday(open, close).abs()
    onsum = on.rolling(5, min_periods=3).sum()
    insum = intra.rolling(5, min_periods=3).sum()
    b = np.log((onsum + 1e-6) / (insum + 1e-6))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-up fill fraction (how much of an up-gap was given back intraday)
def f12gn_f12_gap_news_shock_upfill_1d_base_v011_signal(open, high, low, close):
    b = _f12_gap_up_fill(open, high, low, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-down recovery fraction (how much of a down-gap recovered intraday)
def f12gn_f12_gap_news_shock_dnfill_1d_base_v012_signal(open, high, low, close):
    b = _f12_gap_dn_fill(open, high, low, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# true gap that survived prior-day range (signed, normalized by prior close)
def f12gn_f12_gap_news_shock_truegap_1d_base_v013_signal(open, high, low, close):
    b = _f12_true_gap(open, high, low, close)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-frequency intensity 21d: magnitude-weighted excess of |gap| over its 126d 80th pct
def f12gn_f12_gap_news_shock_gapfreq_21d_base_v014_signal(open, close):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(126, min_periods=63).quantile(0.80)
    excess = (ag - thr).clip(lower=0)
    b = excess.rolling(21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained shock regime 63d: mean tail-excess of |gap| over its trailing 252d 90th pct
def f12gn_f12_gap_news_shock_gapfreq_63d_base_v015_signal(open, close):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(252, min_periods=126).quantile(0.90)
    excess = (ag - thr).clip(lower=0)
    b = excess.rolling(63, min_periods=21).mean() / thr.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-gap vs down-gap count imbalance over 63d, gated by own 80th-pct gap (directional news)
def f12gn_f12_gap_news_shock_gapbal_63d_base_v016_signal(open, close):
    g = _f12_gap(open, close)
    thr = g.abs().rolling(126, min_periods=63).quantile(0.80)
    up = (g >= thr).astype(float).rolling(63, min_periods=21).sum()
    dn = (g <= -thr).astype(float).rolling(63, min_periods=21).sum()
    b = (up - dn) / (up + dn).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# news-shock recency: days since the last gap above the own 90th-pct (recency of shock)
def f12gn_f12_gap_news_shock_recency_63d_base_v017_signal(open, close):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(252, min_periods=126).quantile(0.90)
    big = (ag >= thr).astype(float)

    def _dsl(a):
        idx = np.where(a > 0.5)[0]
        if len(idx) == 0:
            return float(len(a))
        return float(len(a) - 1 - idx[-1])
    b = big.rolling(63, min_periods=21).apply(_dsl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# news-shock recency for up-gaps only (days since last large up-gap, own 90th pct)
def f12gn_f12_gap_news_shock_uprecency_63d_base_v018_signal(open, close):
    g = _f12_gap(open, close)
    thr = g.abs().rolling(252, min_periods=126).quantile(0.90)
    big = (g >= thr).astype(float)

    def _dsl(a):
        idx = np.where(a > 0.5)[0]
        if len(idx) == 0:
            return float(len(a))
        return float(len(a) - 1 - idx[-1])
    b = big.rolling(63, min_periods=21).apply(_dsl, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-with-volume-spike: today's gap weighted by volume surge vs 21d avg
def f12gn_f12_gap_news_shock_gapvol_21d_base_v019_signal(open, close, volume):
    g = _f12_gap(open, close)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)
    b = g * vsurge
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# absolute gap weighted by volume z-score (conviction shock)
def f12gn_f12_gap_news_shock_absgapvol_63d_base_v020_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    vz = _z(volume, 63)
    b = ag * vz.clip(lower=0)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative signed gap over the last week (overnight drift component)
def f12gn_f12_gap_news_shock_cumgap_5d_base_v021_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(5, min_periods=3).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# cumulative signed gap over 21d (monthly overnight drift)
def f12gn_f12_gap_news_shock_cumgap_21d_base_v022_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight vs intraday cumulative spread over 21d (gap-driven vs session-driven trend)
def f12gn_f12_gap_news_shock_onintraspr_21d_base_v023_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    b = on.rolling(21, min_periods=10).sum() - intra.rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single absolute gap in the last 21d (peak shock magnitude)
def f12gn_f12_gap_news_shock_maxgap_21d_base_v024_signal(open, close):
    ag = _f12_abs_gap(open, close)
    b = ag.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest absolute gap in 63d, ranked vs its own 252d history (extremity)
def f12gn_f12_gap_news_shock_maxgaprank_63d_base_v025_signal(open, close):
    ag = _f12_abs_gap(open, close)
    mx = ag.rolling(63, min_periods=21).max()
    b = mx.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap dispersion: std of daily gaps over 21d (overnight noise level)
def f12gn_f12_gap_news_shock_gapstd_21d_base_v026_signal(open, close):
    g = _f12_gap(open, close)
    b = _std(g, 21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap dispersion 63d, ranked vs 252d (shock-regime percentile)
def f12gn_f12_gap_news_shock_gapstdrank_63d_base_v027_signal(open, close):
    g = _f12_gap(open, close)
    sd = _std(g, 63)
    b = sd.rolling(252, min_periods=63).rank(pct=True) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap skew over 63d (asymmetry of news flow: up-shocks vs down-shocks)
def f12gn_f12_gap_news_shock_gapskew_63d_base_v028_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(63, min_periods=21).skew()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap kurtosis over 63d (fat-tail / event-driven gap distribution)
def f12gn_f12_gap_news_shock_gapkurt_63d_base_v029_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(63, min_periods=21).kurt()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# mean up-gap minus mean down-gap magnitude over 63d (shock asymmetry size)
def f12gn_f12_gap_news_shock_gapasym_63d_base_v030_signal(open, close):
    g = _f12_gap(open, close)
    up = g.clip(lower=0).rolling(63, min_periods=21).mean()
    dn = (-g.clip(upper=0)).rolling(63, min_periods=21).mean()
    b = up - dn
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of up-gaps that held into the close (gap-and-go vs gap-and-fade)
def f12gn_f12_gap_news_shock_gapgo_63d_base_v031_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    held = ((g > 0.0) & (intra > 0)).astype(float)
    upg = (g > 0.0).astype(float)
    b = held.rolling(63, min_periods=21).sum() / upg.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# fraction of down-gaps that bounced into the close (capitulation reversal)
def f12gn_f12_gap_news_shock_gapbounce_63d_base_v032_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    bounced = ((g < 0.0) & (intra > 0)).astype(float)
    dng = (g < 0.0).astype(float)
    b = bounced.rolling(63, min_periods=21).sum() / dng.rolling(63, min_periods=21).sum().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average gap-up fill over 21d (persistence of fade behaviour)
def f12gn_f12_gap_news_shock_avgupfill_21d_base_v033_signal(open, high, low, close):
    f = _f12_gap_up_fill(open, high, low, close)
    b = f.rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# average gap-down recovery over 21d
def f12gn_f12_gap_news_shock_avgdnfill_21d_base_v034_signal(open, high, low, close):
    f = _f12_gap_dn_fill(open, high, low, close)
    b = f.rolling(21, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap momentum: today's gap vs the average gap over the prior week (acceleration of news)
def f12gn_f12_gap_news_shock_gapmom_5d_base_v035_signal(open, close):
    g = _f12_gap(open, close)
    b = g - g.shift(1).rolling(5, min_periods=3).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight return contribution share of 21d total return (overnight alpha)
def f12gn_f12_gap_news_shock_onshare_21d_base_v036_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    onsum = on.rolling(21, min_periods=10).sum()
    insum = intra.rolling(21, min_periods=10).sum()
    b = onsum / (onsum.abs() + insum.abs()).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-volume co-spike intensity over 21d (sum of tail-gap-excess weighted by volume surge)
def f12gn_f12_gap_news_shock_newsdays_21d_base_v037_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(63, min_periods=21).quantile(0.70)
    excess = (ag - thr).clip(lower=0)
    vsurge = (volume / _mean(volume, 21).replace(0, np.nan)).clip(lower=0)
    b = (excess * vsurge).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# sustained news intensity 63d: volume-weighted tail-gap energy normalized by gap count
def f12gn_f12_gap_news_shock_newsdays_63d_base_v038_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(126, min_periods=63).quantile(0.80)
    excess = (ag - thr).clip(lower=0)
    vz = _z(volume, 63).clip(lower=0)
    b = (excess * (1.0 + vz)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# 21d covariance of overnight gap with contemporaneous volume change (informed-flow gap)
def f12gn_f12_gap_news_shock_infgap_1d_base_v039_signal(open, close, volume):
    g = _f12_gap(open, close)
    dvol = volume.pct_change()
    b = g.rolling(21, min_periods=10).cov(dvol)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight downside semivol share over 21d (overnight tail risk skew)
def f12gn_f12_gap_news_shock_onvol_21d_base_v040_signal(open, close):
    on = _f12_overnight_ret(open, close)
    down = on.clip(upper=0.0)
    dn_sv = (down ** 2).rolling(21, min_periods=10).mean() ** 0.5
    tot = (on ** 2).rolling(21, min_periods=10).mean() ** 0.5
    b = dn_sv / tot.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# ratio of overnight vol to intraday vol over 63d (where the risk lives)
def f12gn_f12_gap_news_shock_onintravolr_63d_base_v041_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    b = _std(on, 63) / _std(intra, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap reversal tendency: corr of gap with same-day intraday over 63d (fade vs follow)
def f12gn_f12_gap_news_shock_gapreverse_63d_base_v042_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    b = g.rolling(63, min_periods=21).corr(intra)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# next-day gap autocorrelation over 63d (gap clustering / momentum of overnight news)
def f12gn_f12_gap_news_shock_gapautocorr_63d_base_v043_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(63, min_periods=21).corr(g.shift(1))
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-fade signal: does today's session reverse yesterday's overnight gap (mean-reversion)
def f12gn_f12_gap_news_shock_gaptanh_1d_base_v044_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    b = -np.sign(g.shift(1)) * intra
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# rolling-sum of squared gaps over 21d (overnight quadratic variation)
def f12gn_f12_gap_news_shock_gapqv_21d_base_v045_signal(open, close):
    g = _f12_gap(open, close)
    b = (g ** 2).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# share of 21d quadratic variation due to overnight gaps vs intraday moves
def f12gn_f12_gap_news_shock_qvshare_21d_base_v046_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    onqv = (on ** 2).rolling(21, min_periods=10).sum()
    inqv = (intra ** 2).rolling(21, min_periods=10).sum()
    b = onqv / (onqv + inqv).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# biggest up-gap minus biggest down-gap over 63d (range of shocks)
def f12gn_f12_gap_news_shock_gaprange_63d_base_v047_signal(open, close):
    g = _f12_gap(open, close)
    b = g.rolling(63, min_periods=21).max() - g.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# recency of the peak shock: days since the largest |gap| within the trailing 63d window
def f12gn_f12_gap_news_shock_gapvsmax_63d_base_v048_signal(open, close):
    ag = _f12_abs_gap(open, close)

    def _dsmax(a):
        return float(len(a) - 1 - int(np.argmax(a)))
    b = ag.rolling(63, min_periods=21).apply(_dsmax, raw=True)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-open extension: how far open sits above prior high vs prior close (breakaway)
def f12gn_f12_gap_news_shock_breakaway_1d_base_v049_signal(open, high, close):
    ph = high.shift(1)
    pc = close.shift(1)
    b = (open - ph).clip(lower=0) / pc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-down breakdown: how far open sits below prior low relative to prior close
def f12gn_f12_gap_news_shock_breakdown_1d_base_v050_signal(open, low, close):
    pl = low.shift(1)
    pc = close.shift(1)
    b = (pl - open).clip(lower=0) / pc.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# breakaway-gap intensity 63d: mean distance open clears prior high, normalized by close
def f12gn_f12_gap_news_shock_breakawayfreq_63d_base_v051_signal(open, high, close):
    ph = high.shift(1)
    pc = close.shift(1)
    dist = (open - ph).clip(lower=0) / pc.replace(0, np.nan)
    b = dist.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap energy: abs gap times volume surge, summed over 21d (cumulative news energy)
def f12gn_f12_gap_news_shock_gapenergy_21d_base_v052_signal(open, close, volume):
    ag = _f12_abs_gap(open, close)
    vsurge = volume / _mean(volume, 21).replace(0, np.nan)
    b = (ag * vsurge).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight equity-curve MAR over 63d (cumulative gap drift vs its worst overnight drawdown)
def f12gn_f12_gap_news_shock_ondrift_63d_base_v053_signal(open, close):
    on = _f12_overnight_ret(open, close)
    eq = on.rolling(63, min_periods=21).sum()
    peak = eq.rolling(63, min_periods=21).max()
    dd = (eq - peak)
    b = eq / (-dd).rolling(63, min_periods=21).max().replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# intraday-return mean over 63d (session-bias, complement to overnight drift)
def f12gn_f12_gap_news_shock_intradrift_63d_base_v054_signal(open, close):
    intra = _f12_intraday(open, close)
    b = _mean(intra, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight-return Sharpe over 63d, de-meaned by intraday Sharpe (overnight edge premium)
def f12gn_f12_gap_news_shock_onsharpe_63d_base_v055_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    on_sh = _mean(on, 63) / _std(on, 63).replace(0, np.nan)
    in_sh = _mean(intra, 63) / _std(intra, 63).replace(0, np.nan)
    b = on_sh - in_sh
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap fill asymmetry: avg up-fill minus avg down-recovery over 63d
def f12gn_f12_gap_news_shock_fillasym_63d_base_v056_signal(open, high, low, close):
    uf = _f12_gap_up_fill(open, high, low, close).rolling(63, min_periods=15).mean()
    df = _f12_gap_dn_fill(open, high, low, close).rolling(63, min_periods=15).mean()
    b = uf - df
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-gap non-fill strength over 63d (mean unfilled fraction across up-gap days)
def f12gn_f12_gap_news_shock_unfilled_63d_base_v057_signal(open, high, low, close):
    uf = _f12_gap_up_fill(open, high, low, close)
    held = (1.0 - uf).clip(lower=0.0)
    b = held.rolling(63, min_periods=15).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# position of the latest gap within its trailing 126d min-max range (gap range position)
def f12gn_f12_gap_news_shock_gapz_126d_base_v058_signal(open, close):
    g = _f12_gap(open, close)
    gmax = g.rolling(126, min_periods=63).max()
    gmin = g.rolling(126, min_periods=63).min()
    b = (g - gmin) / (gmax - gmin).replace(0, np.nan) - 0.5
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs-gap EMA (persistent shock level, smoothed)
def f12gn_f12_gap_news_shock_absgapema_21d_base_v059_signal(open, close):
    ag = _f12_abs_gap(open, close)
    b = ag.ewm(span=21, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# abs-gap regime ratio: fast vs slow EMA of |gap| (shock-regime expansion/contraction)
def f12gn_f12_gap_news_shock_absgapdisp_1d_base_v060_signal(open, close):
    ag = _f12_abs_gap(open, close)
    fast = ag.ewm(span=10, min_periods=5).mean()
    slow = ag.ewm(span=63, min_periods=21).mean()
    b = fast / slow.replace(0, np.nan) - 1.0
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-day intraday follow-through strength (intraday move on big-gap days, 63d mean)
def f12gn_f12_gap_news_shock_gapfollow_63d_base_v061_signal(open, close):
    g = _f12_gap(open, close)
    intra = _f12_intraday(open, close)
    thr = g.abs().rolling(63, min_periods=21).quantile(0.70)
    follow = (np.sign(g) * intra).where(g.abs() >= thr, np.nan)
    b = follow.rolling(63, min_periods=10).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight drawdown via gaps: most negative cumulative gap over 21d (overnight stress)
def f12gn_f12_gap_news_shock_ondd_21d_base_v062_signal(open, close):
    on = _f12_overnight_ret(open, close)
    cum = on.rolling(21, min_periods=10).sum()
    b = cum.rolling(63, min_periods=21).min()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# proportion of total realized vol explained by gaps over 63d (gap-vol ratio)
def f12gn_f12_gap_news_shock_gapvolratio_63d_base_v063_signal(open, close):
    g = _f12_gap(open, close)
    tot = close.pct_change()
    b = _std(g, 63) / _std(tot, 63).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# signed gap streak: consecutive same-direction gaps (overnight trend run-length)
def f12gn_f12_gap_news_shock_gapstreak_1d_base_v064_signal(open, close):
    g = _f12_gap(open, close)
    sign = np.sign(g)
    grp = (sign != sign.shift(1)).cumsum()
    streak = sign.groupby(grp).cumcount() + 1
    b = (streak * sign).astype(float)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# largest single news-day return (max abs total return) over 21d (event magnitude)
def f12gn_f12_gap_news_shock_eventmag_21d_base_v065_signal(open, close):
    pc = close.shift(1)
    tot = (close / pc.replace(0, np.nan) - 1.0).abs()
    b = tot.rolling(21, min_periods=10).max()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap clustering index: variability of rolling gap frequency over 63d
def f12gn_f12_gap_news_shock_gapcluster_63d_base_v066_signal(open, close):
    ag = _f12_abs_gap(open, close)
    thr = ag.rolling(126, min_periods=63).quantile(0.80)
    big = (ag >= thr).astype(float)
    freq21 = big.rolling(21, min_periods=10).mean()
    b = _std(freq21, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# net overnight-gap pressure weighted by volume over 21d (volume-weighted gap drift)
def f12gn_f12_gap_news_shock_vwgap_21d_base_v067_signal(open, close, volume):
    g = _f12_gap(open, close)
    num = (g * volume).rolling(21, min_periods=10).sum()
    den = volume.rolling(21, min_periods=10).sum()
    b = num / den.replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-open position within prior-day range (where open landed: gap context)
def f12gn_f12_gap_news_shock_openinrange_1d_base_v068_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    b = (open - pl) / (ph - pl).replace(0, np.nan)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# out-of-range gap intensity over 63d (mean distance open lands beyond prior-day range)
def f12gn_f12_gap_news_shock_outrangefreq_63d_base_v069_signal(open, high, low, close):
    ph = high.shift(1)
    pl = low.shift(1)
    pc = close.shift(1)
    out = (open - ph).clip(lower=0) + (pl - open).clip(lower=0)
    b = (out / pc.replace(0, np.nan)).rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# smoothed absolute-gap level minus its value 21d ago (shock-level change)
def f12gn_f12_gap_news_shock_shockchg_21d_base_v070_signal(open, close):
    ag = _f12_abs_gap(open, close)
    sm = ag.rolling(5, min_periods=3).mean()
    b = sm - sm.shift(21)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# down-gap intensity: sum of negative gaps over 21d (overnight bleed)
def f12gn_f12_gap_news_shock_dngapsum_21d_base_v071_signal(open, close):
    g = _f12_gap(open, close)
    b = g.clip(upper=0).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# up-gap intensity: sum of positive gaps over 21d (overnight pops)
def f12gn_f12_gap_news_shock_upgapsum_21d_base_v072_signal(open, close):
    g = _f12_gap(open, close)
    b = g.clip(lower=0).rolling(21, min_periods=10).sum()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# exponentially-decayed signed-gap pressure (recent overnight news momentum, halflife 5d)
def f12gn_f12_gap_news_shock_decayshock_21d_base_v073_signal(open, close):
    g = _f12_gap(open, close)
    b = g.ewm(halflife=5, min_periods=5).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# overnight/intraday confirmation over 63d (magnitude-weighted sign agreement of gap & session)
def f12gn_f12_gap_news_shock_signagree_63d_base_v074_signal(open, close):
    on = _f12_overnight_ret(open, close)
    intra = _f12_intraday(open, close)
    conf = np.sign(on) * np.sign(intra) * (on.abs() + intra.abs())
    b = conf.rolling(63, min_periods=21).mean()
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


# gap-magnitude trend: 21d mean abs gap minus 63d mean abs gap (rising shock intensity)
def f12gn_f12_gap_news_shock_shocktrend_base_v075_signal(open, close):
    ag = _f12_abs_gap(open, close)
    b = _mean(ag, 21) - _mean(ag, 63)
    result = b
    return result.replace([np.inf, -np.inf], np.nan)


_FEATURES = [
    f12gn_f12_gap_news_shock_gap_1d_base_v001_signal,
    f12gn_f12_gap_news_shock_loggap_1d_base_v002_signal,
    f12gn_f12_gap_news_shock_absgap_1d_base_v003_signal,
    f12gn_f12_gap_news_shock_intraday_1d_base_v004_signal,
    f12gn_f12_gap_news_shock_onvsintra_1d_base_v005_signal,
    f12gn_f12_gap_news_shock_ondom_1d_base_v006_signal,
    f12gn_f12_gap_news_shock_gapz_63d_base_v007_signal,
    f12gn_f12_gap_news_shock_gapz_21d_base_v008_signal,
    f12gn_f12_gap_news_shock_gapmult_63d_base_v009_signal,
    f12gn_f12_gap_news_shock_gapsigma_21d_base_v010_signal,
    f12gn_f12_gap_news_shock_upfill_1d_base_v011_signal,
    f12gn_f12_gap_news_shock_dnfill_1d_base_v012_signal,
    f12gn_f12_gap_news_shock_truegap_1d_base_v013_signal,
    f12gn_f12_gap_news_shock_gapfreq_21d_base_v014_signal,
    f12gn_f12_gap_news_shock_gapfreq_63d_base_v015_signal,
    f12gn_f12_gap_news_shock_gapbal_63d_base_v016_signal,
    f12gn_f12_gap_news_shock_recency_63d_base_v017_signal,
    f12gn_f12_gap_news_shock_uprecency_63d_base_v018_signal,
    f12gn_f12_gap_news_shock_gapvol_21d_base_v019_signal,
    f12gn_f12_gap_news_shock_absgapvol_63d_base_v020_signal,
    f12gn_f12_gap_news_shock_cumgap_5d_base_v021_signal,
    f12gn_f12_gap_news_shock_cumgap_21d_base_v022_signal,
    f12gn_f12_gap_news_shock_onintraspr_21d_base_v023_signal,
    f12gn_f12_gap_news_shock_maxgap_21d_base_v024_signal,
    f12gn_f12_gap_news_shock_maxgaprank_63d_base_v025_signal,
    f12gn_f12_gap_news_shock_gapstd_21d_base_v026_signal,
    f12gn_f12_gap_news_shock_gapstdrank_63d_base_v027_signal,
    f12gn_f12_gap_news_shock_gapskew_63d_base_v028_signal,
    f12gn_f12_gap_news_shock_gapkurt_63d_base_v029_signal,
    f12gn_f12_gap_news_shock_gapasym_63d_base_v030_signal,
    f12gn_f12_gap_news_shock_gapgo_63d_base_v031_signal,
    f12gn_f12_gap_news_shock_gapbounce_63d_base_v032_signal,
    f12gn_f12_gap_news_shock_avgupfill_21d_base_v033_signal,
    f12gn_f12_gap_news_shock_avgdnfill_21d_base_v034_signal,
    f12gn_f12_gap_news_shock_gapmom_5d_base_v035_signal,
    f12gn_f12_gap_news_shock_onshare_21d_base_v036_signal,
    f12gn_f12_gap_news_shock_newsdays_21d_base_v037_signal,
    f12gn_f12_gap_news_shock_newsdays_63d_base_v038_signal,
    f12gn_f12_gap_news_shock_infgap_1d_base_v039_signal,
    f12gn_f12_gap_news_shock_onvol_21d_base_v040_signal,
    f12gn_f12_gap_news_shock_onintravolr_63d_base_v041_signal,
    f12gn_f12_gap_news_shock_gapreverse_63d_base_v042_signal,
    f12gn_f12_gap_news_shock_gapautocorr_63d_base_v043_signal,
    f12gn_f12_gap_news_shock_gaptanh_1d_base_v044_signal,
    f12gn_f12_gap_news_shock_gapqv_21d_base_v045_signal,
    f12gn_f12_gap_news_shock_qvshare_21d_base_v046_signal,
    f12gn_f12_gap_news_shock_gaprange_63d_base_v047_signal,
    f12gn_f12_gap_news_shock_gapvsmax_63d_base_v048_signal,
    f12gn_f12_gap_news_shock_breakaway_1d_base_v049_signal,
    f12gn_f12_gap_news_shock_breakdown_1d_base_v050_signal,
    f12gn_f12_gap_news_shock_breakawayfreq_63d_base_v051_signal,
    f12gn_f12_gap_news_shock_gapenergy_21d_base_v052_signal,
    f12gn_f12_gap_news_shock_ondrift_63d_base_v053_signal,
    f12gn_f12_gap_news_shock_intradrift_63d_base_v054_signal,
    f12gn_f12_gap_news_shock_onsharpe_63d_base_v055_signal,
    f12gn_f12_gap_news_shock_fillasym_63d_base_v056_signal,
    f12gn_f12_gap_news_shock_unfilled_63d_base_v057_signal,
    f12gn_f12_gap_news_shock_gapz_126d_base_v058_signal,
    f12gn_f12_gap_news_shock_absgapema_21d_base_v059_signal,
    f12gn_f12_gap_news_shock_absgapdisp_1d_base_v060_signal,
    f12gn_f12_gap_news_shock_gapfollow_63d_base_v061_signal,
    f12gn_f12_gap_news_shock_ondd_21d_base_v062_signal,
    f12gn_f12_gap_news_shock_gapvolratio_63d_base_v063_signal,
    f12gn_f12_gap_news_shock_gapstreak_1d_base_v064_signal,
    f12gn_f12_gap_news_shock_eventmag_21d_base_v065_signal,
    f12gn_f12_gap_news_shock_gapcluster_63d_base_v066_signal,
    f12gn_f12_gap_news_shock_vwgap_21d_base_v067_signal,
    f12gn_f12_gap_news_shock_openinrange_1d_base_v068_signal,
    f12gn_f12_gap_news_shock_outrangefreq_63d_base_v069_signal,
    f12gn_f12_gap_news_shock_shockchg_21d_base_v070_signal,
    f12gn_f12_gap_news_shock_dngapsum_21d_base_v071_signal,
    f12gn_f12_gap_news_shock_upgapsum_21d_base_v072_signal,
    f12gn_f12_gap_news_shock_decayshock_21d_base_v073_signal,
    f12gn_f12_gap_news_shock_signagree_63d_base_v074_signal,
    f12gn_f12_gap_news_shock_shocktrend_base_v075_signal,
]


def _inputs_for(fn):
    sig = inspect.signature(fn)
    return [p.name for p in sig.parameters.values()]


REGISTRY = {fn.__name__: {"inputs": _inputs_for(fn), "func": fn} for fn in _FEATURES}
F12_GAP_NEWS_SHOCK_REGISTRY_001_075 = REGISTRY


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

    print("OK f12_gap_news_shock_base_001_075_claude: %d features pass" % n_features)
