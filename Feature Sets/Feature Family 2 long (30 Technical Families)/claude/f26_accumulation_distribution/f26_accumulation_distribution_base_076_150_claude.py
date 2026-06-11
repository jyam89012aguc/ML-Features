"""f26_accumulation_distribution base features 076-150.

These features extend the A/D-line/CLV/Chaikin/Klinger/MFI domain with
structurally distinct expressions vs. base_001_075. Heavy diversity: CLV
quantile features, Chaikin signal-line variants, Klinger histogram, A/D
divergence at different lags, money-flow z/rank features, days-since
crossover, cross-class correlations, CLV regression slope/R^2, A/D
acceleration regimes, CLV-volume IQR/MAD.

Window>21 uses closeadj; <=21 uses close. NaN policy: only final
replace([inf,-inf], nan).
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def _streak_run(x: np.ndarray) -> float:
    c = 0
    for v in x[::-1]:
        if v > 0.5:
            c += 1
        else:
            break
    return float(c)


# === Features 076-150 ======================================================


def f26ad_f26_accumulation_distribution_clv_median_15d_base_v076_signal(high, low, close):
    """Rolling 15d median of CLV. Robust accumulation pressure (median vs. mean of v003)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    return clv.rolling(15, min_periods=15).median().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_iqr_45d_base_v077_signal(high, low, closeadj):
    """Interquartile range of CLV over 45d (Q75-Q25). Dispersion of close-in-range placement."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    q75 = clv.rolling(45, min_periods=45).quantile(0.75)
    q25 = clv.rolling(45, min_periods=45).quantile(0.25)
    return (q75 - q25).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_mad_30d_base_v078_signal(high, low, closeadj):
    """Mean absolute deviation of CLV over 30d (robust dispersion)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    def _mad(x):
        m = np.mean(x)
        return float(np.mean(np.abs(x - m)))
    return clv.rolling(30, min_periods=30).apply(_mad, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_skew_60d_base_v079_signal(high, low, closeadj):
    """Skewness of CLV over 60d. Asymmetry of accumulation/distribution."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return clv.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_kurt_120d_base_v080_signal(high, low, closeadj):
    """Excess kurtosis of CLV over 120d. Tail-event regime in CLV distribution."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return clv.rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_q90_50d_base_v081_signal(high, low, closeadj):
    """90th percentile of CLV over 50d (upper-tail of close-in-range placement)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return clv.rolling(50, min_periods=50).quantile(0.90).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_q10_50d_base_v082_signal(high, low, closeadj):
    """10th percentile of CLV over 50d (lower-tail of close-in-range placement)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return clv.rolling(50, min_periods=50).quantile(0.10).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_hist_3_10_minus_signal_base_v083_signal(high, low, closeadj, volume):
    """Chaikin histogram: (Chaikin Osc) - EMA(Chaikin Osc, 9), normalised by sum vol(10)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sig9 = co.ewm(span=9, adjust=False, min_periods=9).mean()
    den = volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    return ((co - sig9) / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_signal_distance_60d_base_v084_signal(high, low, closeadj, volume):
    """Sign(co - sig9_co): Chaikin minus Chaikin signal — direction state, discrete."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sig9 = co.ewm(span=9, adjust=False, min_periods=9).mean()
    return np.sign(co - sig9).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_pos_minus_neg_count_90d_base_v085_signal(high, low, closeadj):
    """count(CLV>0,90) - count(CLV<0,90). Net accumulation tally."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    pos = (clv > 0.0).astype(float).where(~clv.isna())
    neg = (clv < 0.0).astype(float).where(~clv.isna())
    return (pos.rolling(90, min_periods=90).sum() - neg.rolling(90, min_periods=90).sum()).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_count_strong_pos_60d_base_v086_signal(high, low, closeadj):
    """Count of CLV>0.5 days in 60d. Strong-accumulation bar count."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    flag = (clv > 0.5).astype(float).where(~clv.isna())
    return flag.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_count_strong_neg_60d_base_v087_signal(high, low, closeadj):
    """Count of CLV<-0.5 days in 60d. Strong-distribution bar count."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    flag = (clv < -0.5).astype(float).where(~clv.isna())
    return flag.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_rank_in_60d_base_v088_signal(high, low, closeadj):
    """Percentile rank of current CLV within rolling 60d window."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    def _rank_last(x):
        last = x[-1]
        if not np.isfinite(last):
            return np.nan
        return float((x < last).sum()) / float(len(x))
    return clv.rolling(60, min_periods=60).apply(_rank_last, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_volwtd_median_30d_base_v089_signal(high, low, closeadj, volume):
    """Volume-weighted CLV median approximation: median of (CLV*vol/mean_vol) over 30d.
    Bar-wise normalised flow, robust to outliers, complements CMF (mean-based)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    norm = (clv * volume) / volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    return norm.rolling(30, min_periods=30).median().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_regslope_60d_base_v090_signal(high, low, closeadj, volume):
    """OLS slope of A/D vs time over 60d, normalised by abs(mean A/D) over 60d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx)); vr = np.sum((t - mt) ** 2)
        if vr == 0.0 or not np.isfinite(mx) or mx == 0.0:
            return np.nan
        return float((cov / vr) / abs(mx))
    return ad.rolling(60, min_periods=60).apply(_slope, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_rsq_120d_base_v091_signal(high, low, closeadj, volume):
    """R^2 of OLS A/D vs time over 120d. Goodness-of-fit of A/D linear trend."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        r = cov / np.sqrt(vt * vx)
        return float(r * r)
    return ad.rolling(120, min_periods=120).apply(_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_residstd_50d_base_v092_signal(high, low, closeadj, volume):
    """Residual std of A/D from its 50d OLS line, normalised by abs mean."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    def _resid(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx)); vt = np.sum((t - mt) ** 2)
        if vt == 0.0 or not np.isfinite(mx) or mx == 0.0:
            return np.nan
        bb = cov / vt; a = mx - bb * mt
        return float(np.std(x - (a + bb * t)) / abs(mx))
    return ad.rolling(50, min_periods=50).apply(_resid, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_return_corr_45d_base_v093_signal(high, low, closeadj, volume):
    """Rolling 45d corr of (CLV*vol/vol) and returns. Captures money-flow-vs-return coupling."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ret = closeadj.pct_change(1)
    return clv.rolling(45, min_periods=45).corr(ret).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_vol_corr_30d_base_v094_signal(high, low, closeadj, volume):
    """Rolling 30d corr of CLV with log(volume). Are wide-volume bars also accum bars?"""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    lv = np.log(volume.replace(0.0, np.nan))
    return clv.rolling(30, min_periods=30).corr(lv).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_acc_25d_base_v095_signal(high, low, closeadj, volume):
    """Chaikin Oscillator (3-10) curvature: co - 2*co.shift(12)+co.shift(25) over sum vol(25)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    den = volume.rolling(25, min_periods=25).sum().replace(0.0, np.nan)
    return ((co - 2.0 * co.shift(12) + co.shift(25)) / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_mfi_short_long_diff_base_v096_signal(high, low, closeadj, volume):
    """MFI_7 - MFI_28 (short-vs-long money flow oscillator differential), centered."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf7 = pos.rolling(7, min_periods=7).sum()
    nf7 = neg.rolling(7, min_periods=7).sum().replace(0.0, np.nan)
    pf28 = pos.rolling(28, min_periods=28).sum()
    nf28 = neg.rolling(28, min_periods=28).sum().replace(0.0, np.nan)
    mfi7 = 100.0 - 100.0 / (1.0 + pf7 / nf7)
    mfi28 = 100.0 - 100.0 / (1.0 + pf28 / nf28)
    return (mfi7 - mfi28).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_arctan_mfi_zscore_60d_base_v097_signal(high, low, closeadj, volume):
    """arctan(z-score of MFI_14 over 60d). Compressed bounded MFI deviation."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mr = pf / nf
    mfi = 100.0 - 100.0 / (1.0 + mr)
    mu = mfi.rolling(60, min_periods=60).mean()
    sd = mfi.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return np.arctan((mfi - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_cmf21_minus_cmf50_75d_smoothed_base_v098_signal(high, low, closeadj, volume):
    """EMA(CMF_21 - CMF_50, 10). Smoothed differential between CMF horizons."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    c21 = cv.rolling(21, min_periods=21).sum() / volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    c50 = cv.rolling(50, min_periods=50).sum() / volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (c21 - c50).ewm(span=10, adjust=False, min_periods=10).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_days_since_chaikin_xover_45d_base_v099_signal(high, low, closeadj, volume):
    """Days since Chaikin Osc 3-10 last crossed Chaikin signal line, capped 45d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sig9 = co.ewm(span=9, adjust=False, min_periods=9).mean()
    s = np.sign(co - sig9)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(45, min_periods=45).apply(_streak_run, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_acc_zscore_30d_base_v100_signal(high, low, closeadj, volume):
    """Z-score of A/D second-differences (acceleration) over 30d."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    acc = ad - 2.0 * ad.shift(15) + ad.shift(30)
    mu = acc.rolling(60, min_periods=60).mean()
    sd = acc.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return ((acc - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_extreme_count_120d_base_v101_signal(high, low, closeadj, volume):
    """Count of |Chaikin Osc normalised| > 1 std events in last 120d (extreme-event count)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sd = co.rolling(120, min_periods=120).std(ddof=0).replace(0.0, np.nan)
    z = co / sd
    flag = (z.abs() > 1.0).astype(float).where(~z.isna())
    return flag.rolling(120, min_periods=120).sum().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_vol_weighted_mean_15d_base_v102_signal(high, low, close, volume):
    """sum(CLV*vol,15) / sum(vol,15) — short-horizon volume-weighted CLV (CMF_15)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    num = (clv * volume).rolling(15, min_periods=15).sum()
    den = volume.rolling(15, min_periods=15).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_z_60d_base_v103_signal(high, low, closeadj, volume):
    """Z-score of Chaikin Osc 3-10 over 60d (raw oscillator, no volume normalisation)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    mu = co.rolling(60, min_periods=60).mean()
    sd = co.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return ((co - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_mfi14_rank_120d_base_v104_signal(high, low, closeadj, volume):
    """Percentile rank of MFI_14 within rolling 120d window."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mr = pf / nf
    mfi = 100.0 - 100.0 / (1.0 + mr)
    def _rank_last(x):
        last = x[-1]
        if not np.isfinite(last):
            return np.nan
        return float((x < last).sum()) / float(len(x))
    return mfi.rolling(120, min_periods=120).apply(_rank_last, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_mfi_oversold_frac_45d_base_v105_signal(high, low, closeadj, volume):
    """Fraction of 45d where MFI_14 < 30. Oversold money-flow regime."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mr = pf / nf
    mfi = 100.0 - 100.0 / (1.0 + mr)
    flag = (mfi < 30.0).astype(float).where(~mfi.isna())
    return flag.rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_klinger_oscillator_norm_z_60d_base_v106_signal(high, low, closeadj, volume):
    """Z-score of Klinger Oscillator (EMA(KVF,34)-EMA(KVF,55)) over 60d."""
    hlc = (high + low + closeadj) / 3.0
    trend = np.sign(hlc.diff(1))
    kvf = volume * trend
    e34 = kvf.ewm(span=34, adjust=False, min_periods=34).mean()
    e55 = kvf.ewm(span=55, adjust=False, min_periods=55).mean()
    ko = e34 - e55
    mu = ko.rolling(60, min_periods=60).mean()
    sd = ko.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return ((ko - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_return_div_30d_base_v107_signal(high, low, closeadj, volume):
    """A/D pct-change(30) - close pct-change(30). Divergence magnitude vs price."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    ad_chg = ad.diff(30) / volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    px_chg = closeadj.pct_change(30)
    return (ad_chg - px_chg).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_ac1_45d_base_v108_signal(high, low, closeadj, volume):
    """Autocorr lag-1 of (CLV*volume) over 45d. Persistence of per-bar money flow.
    Structurally distinct from v061 (CLV autocorr; uses volume-weighted bar flow)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    def _ac1(x):
        if len(x) < 3:
            return np.nan
        s = pd.Series(x)
        return float(s.autocorr(lag=1)) if s.std(ddof=0) > 0 else np.nan
    return cv.rolling(45, min_periods=45).apply(_ac1, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_3_10_signal_dist_z_60d_base_v109_signal(high, low, closeadj, volume):
    """Z-score of (Chaikin Osc - Chaikin signal line) over 60d. Histogram-z."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sig9 = co.ewm(span=9, adjust=False, min_periods=9).mean()
    hist = co - sig9
    mu = hist.rolling(60, min_periods=60).mean()
    sd = hist.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return ((hist - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_pos_streak_max_60d_base_v110_signal(high, low, closeadj):
    """Max trailing-window run of CLV>0 days within 60d (longest accumulation streak)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    pos = (clv > 0.0).astype(float).where(~clv.isna())
    def _max_run(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return pos.rolling(60, min_periods=60).apply(_max_run, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_neg_streak_max_60d_base_v111_signal(high, low, closeadj):
    """Max trailing-window run of CLV<0 days within 60d (longest distribution streak)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    neg = (clv < 0.0).astype(float).where(~clv.isna())
    def _max_run(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        best = 0; cur = 0
        for v in x:
            if v > 0.5:
                cur += 1
                if cur > best:
                    best = cur
            else:
                cur = 0
        return float(best)
    return neg.rolling(60, min_periods=60).apply(_max_run, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_price_corr_50d_base_v112_signal(high, low, closeadj, volume):
    """Rolling 50d corr of A/D level vs closeadj. Confirmation/divergence diagnostic."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    return ad.rolling(50, min_periods=50).corr(closeadj).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_price_diff_corr_30d_base_v113_signal(high, low, closeadj, volume):
    """Rolling 30d corr of (A/D 5d-diff) vs (closeadj 5d-diff). Co-movement of changes."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    return ad.diff(5).rolling(30, min_periods=30).corr(closeadj.diff(5)).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_abs_mean_50d_base_v114_signal(high, low, closeadj):
    """Mean of |CLV| over 50d. Bar-intensity measure (close near extreme regardless of direction)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return clv.abs().rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_high_acc_vol_share_50d_base_v115_signal(high, low, closeadj, volume):
    """sum(vol where CLV>0.5, 50) / sum(vol, 50). Volume share captured by strong-acc bars."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    strong_vol = volume.where(clv > 0.5, 0.0)
    den = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (strong_vol.rolling(50, min_periods=50).sum() / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_high_dist_vol_share_50d_base_v116_signal(high, low, closeadj, volume):
    """sum(vol where CLV<-0.5, 50) / sum(vol, 50). Volume share captured by strong-dist bars."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    strong_vol = volume.where(clv < -0.5, 0.0)
    den = volume.rolling(50, min_periods=50).sum().replace(0.0, np.nan)
    return (strong_vol.rolling(50, min_periods=50).sum() / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_max_to_mean_30d_base_v117_signal(high, low, closeadj, volume):
    """max(|CLV*vol|,30) / mean(|CLV*vol|,30). Concentration of money flow in single bars."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = (clv * volume).abs()
    mx = cv.rolling(30, min_periods=30).max()
    mn = cv.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    return (mx / mn).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_above_signal_xover_count_60d_base_v118_signal(high, low, closeadj, volume):
    """Count of (Chaikin Osc - Chaikin signal line) sign-crossovers in 60d window.
    Histogram-zero crossings (different signal than v073 which crosses zero on co)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sig9 = co.ewm(span=9, adjust=False, min_periods=9).mean()
    s = np.sign(co - sig9)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_velocity_norm_60d_base_v119_signal(high, low, closeadj, volume):
    """A/D 1d-velocity (CLV*vol) normalised by 60d std of (CLV*vol). Bar-wise standardised flow."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    sd = cv.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return (cv / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_vol_corr_120d_base_v120_signal(high, low, closeadj, volume):
    """Rolling 120d corr of CLV and log(volume). Long-horizon CLV-volume coupling."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    lv = np.log(volume.replace(0.0, np.nan))
    return clv.rolling(120, min_periods=120).corr(lv).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_arctan_mean_30d_base_v121_signal(high, low, closeadj):
    """arctan(3 * mean(CLV, 30)). Bounded compression of mid-window CLV mean."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    return np.arctan(3.0 * clv.rolling(30, min_periods=30).mean()).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_tanh_clvvol_z_50d_base_v122_signal(high, low, closeadj, volume):
    """tanh of bar-wise (CLV*vol)/std over 50d. Bounded compressed flow."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    sd = cv.rolling(50, min_periods=50).std(ddof=0).replace(0.0, np.nan)
    return np.tanh(cv / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_klinger_signal_dist_norm_base_v123_signal(high, low, closeadj, volume):
    """(Klinger Osc - EMA(Klinger Osc, 13)) normalised by 60d std. Klinger histogram-z."""
    hlc = (high + low + closeadj) / 3.0
    trend = np.sign(hlc.diff(1))
    kvf = volume * trend
    e34 = kvf.ewm(span=34, adjust=False, min_periods=34).mean()
    e55 = kvf.ewm(span=55, adjust=False, min_periods=55).mean()
    ko = e34 - e55
    sig13 = ko.ewm(span=13, adjust=False, min_periods=13).mean()
    hist = ko - sig13
    sd = hist.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return (hist / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_ema_diff_5_20_base_v124_signal(high, low, close, volume):
    """log(EMA(A/D,5) / EMA(A/D,20)) — log-ratio Chaikin variant; differs in scale from v017."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    ad = (clv * volume).cumsum()
    e5 = ad.ewm(span=5, adjust=False, min_periods=5).mean()
    e20 = ad.ewm(span=20, adjust=False, min_periods=20).mean()
    return np.log(e5.abs().replace(0.0, np.nan) / e20.abs().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_obv_zspread_60d_base_v125_signal(high, low, closeadj, volume):
    """z(A/D, 60) - z(OBV, 60). Cross-signal normalised divergence."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    obv = (np.sign(closeadj.diff(1)) * volume).cumsum()
    z_ad = (ad - ad.rolling(60, min_periods=60).mean()) / ad.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    z_obv = (obv - obv.rolling(60, min_periods=60).mean()) / obv.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return (z_ad - z_obv).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_neg_run_count_45d_base_v126_signal(high, low, closeadj):
    """Count of distinct CLV<0 runs within 45d window."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    neg = (clv < 0.0).astype(float).where(~clv.isna())
    def _runs(x):
        x = np.asarray(x, dtype=float)
        if not np.all(np.isfinite(x)):
            return np.nan
        cnt = 0; prev = 0.0
        for v in x:
            if v > 0.5 and prev <= 0.5:
                cnt += 1
            prev = v
        return float(cnt)
    return neg.rolling(45, min_periods=45).apply(_runs, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_log_velocity_30d_base_v127_signal(high, low, closeadj, volume):
    """log(|A/D - A/D.shift(30)|) - log(sum vol,30). Log-magnitude of normalised acc."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    num = (ad - ad.shift(30)).abs()
    den = volume.rolling(30, min_periods=30).sum()
    return (np.log(num.replace(0.0, np.nan)) - np.log(den.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_sign_freq_30d_base_v128_signal(high, low, closeadj, volume):
    """Mean of sign(Chaikin Osc) over 30d. Bounded [-1,+1]; fraction of bars positive-Chaikin."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    s = np.sign(e3 - e10)
    return s.rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_mfi_sign_freq_45d_base_v129_signal(high, low, closeadj, volume):
    """Mean of sign(MFI_14 - 50) over 45d. Bounded; fraction-bullish MFI bars."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + pf / nf)
    s = np.sign(mfi - 50.0)
    return s.rolling(45, min_periods=45).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_skew_60d_base_v130_signal(high, low, closeadj, volume):
    """Skewness of (CLV*vol) over 60d (raw, not volume-weighted). Asymmetric flow concentration."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    return cv.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_obv_diff_zscore_60d_base_v131_signal(high, low, closeadj, volume):
    """Z-score of (A/D - OBV) over 60d. Cross-signal divergence intensity."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    obv = (np.sign(closeadj.diff(1)) * volume).cumsum()
    diff = ad - obv
    mu = diff.rolling(60, min_periods=60).mean()
    sd = diff.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return ((diff - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_above_below_freq_90d_base_v132_signal(high, low, closeadj, volume):
    """Fraction of 90d where A/D > SMA(A/D, 45). Direction-of-trend regime."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    above = (ad > ad.rolling(45, min_periods=45).mean()).astype(float).where(~ad.rolling(45, min_periods=45).mean().isna())
    return above.rolling(90, min_periods=90).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_change_volwtd_45d_base_v133_signal(high, low, closeadj, volume):
    """sum((CLV - CLV.shift(1)) * vol, 45) / sum(vol, 45). Volume-weighted CLV change."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    dclv = clv.diff(1)
    num = (dclv * volume).rolling(45, min_periods=45).sum()
    den = volume.rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_williams_ad_zscore_60d_base_v134_signal(high, low, closeadj, volume):
    """Z-score of cumulative Williams A/D over 60d. Williams uses prior_close-anchored bar range,
    structurally distinct from CLV-based A/D."""
    pc = closeadj.shift(1)
    up_part = closeadj - low.combine(pc, np.minimum)
    dn_part = closeadj - high.combine(pc, np.maximum)
    sgn = np.sign(closeadj - pc)
    wad_bar = np.where(sgn > 0.0, up_part, np.where(sgn < 0.0, dn_part, 0.0))
    wad = pd.Series(wad_bar, index=closeadj.index).cumsum()
    mu = wad.rolling(60, min_periods=60).mean()
    sd = wad.rolling(60, min_periods=60).std(ddof=0).replace(0.0, np.nan)
    return ((wad - mu) / sd).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_klinger_zero_streak_50d_base_v135_signal(high, low, closeadj, volume):
    """Days since Klinger Osc 34-55 last crossed zero, capped 50d."""
    hlc = (high + low + closeadj) / 3.0
    trend = np.sign(hlc.diff(1))
    kvf = volume * trend
    e34 = kvf.ewm(span=34, adjust=False, min_periods=34).mean()
    e55 = kvf.ewm(span=55, adjust=False, min_periods=55).mean()
    s = np.sign(e34 - e55)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(50, min_periods=50).apply(_streak_run, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_skew_rank_120d_base_v136_signal(high, low, closeadj):
    """Percentile rank of CLV skewness (60d window) within rolling 120d (regime of asymmetry)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    sk = clv.rolling(60, min_periods=60).skew()
    def _rank_last(x):
        last = x[-1]
        if not np.isfinite(last):
            return np.nan
        return float((x < last).sum()) / float(len(x))
    return sk.rolling(120, min_periods=120).apply(_rank_last, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_abs_share_50d_base_v137_signal(high, low, closeadj, volume):
    """sum(|CLV*vol|, 50) / sum(vol*|CLV|.rolling_max, 50). Money-flow intensity share —
    fraction of (volume * CLV)-magnitude captured by typical bars vs extreme. Bounded [0,1]."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = (clv * volume).abs()
    num = cv.rolling(50, min_periods=50).sum()
    den = (cv.rolling(50, min_periods=50).max() * 50.0).replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_ema21_minus_sma21_base_v138_signal(high, low, close, volume):
    """EMA(CLV*vol, 21) - SMA(CLV*vol, 21) normalised by mean vol. Tracking-kernel differential."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((close - low) - (high - close)) / rng
    cv = clv * volume
    em = cv.ewm(span=21, adjust=False, min_periods=21).mean()
    sm = cv.rolling(21, min_periods=21).mean()
    den = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    return ((em - sm) / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_path_efficiency_60d_base_v139_signal(high, low, closeadj, volume):
    """|A/D - A/D.shift(60)| / sum(|CLV*vol|, 60). A/D directional efficiency (0..1)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    ad = cv.cumsum()
    net = (ad - ad.shift(60)).abs()
    path = cv.abs().rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (net / path).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_path_efficiency_45d_base_v140_signal(high, low, closeadj, volume):
    """|Chaikin Osc - Chaikin Osc.shift(45)| / sum(|Chaikin Osc.diff|,45). Oscillator path efficiency."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    net = (co - co.shift(45)).abs()
    path = co.diff(1).abs().rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    return (net / path).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_volwtd_q75_30d_base_v141_signal(high, low, closeadj, volume):
    """Volume-weighted CLV 75th percentile approximation via top-vol-share-weighted mean over 30d.
    Uses bars where volume > 60th-percentile within 30d window."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    def _q75ish(s):
        x = np.asarray(s, dtype=float)
        if not np.all(np.isfinite(x)) or len(x) < 5:
            return np.nan
        v_thresh = np.quantile(x, 0.75)
        sel = x[x >= v_thresh]
        if len(sel) == 0:
            return np.nan
        return float(np.mean(sel))
    return cv.rolling(30, min_periods=30).apply(_q75ish, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_volwtd_q25_30d_base_v142_signal(high, low, closeadj, volume):
    """Mean of bars where (CLV*vol) <= 25th-percentile within 30d window. Lower-tail flow."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv = clv * volume
    def _q25ish(s):
        x = np.asarray(s, dtype=float)
        if not np.all(np.isfinite(x)) or len(x) < 5:
            return np.nan
        v_thresh = np.quantile(x, 0.25)
        sel = x[x <= v_thresh]
        if len(sel) == 0:
            return np.nan
        return float(np.mean(sel))
    return cv.rolling(30, min_periods=30).apply(_q25ish, raw=True).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clvvol_volwtd_kurt_120d_base_v143_signal(high, low, closeadj, volume):
    """Excess kurtosis of (CLV*volume / mean_volume) over 120d. Per-bar flow tail-event regime."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    norm = (clv * volume) / volume.rolling(120, min_periods=120).mean().replace(0.0, np.nan)
    return norm.rolling(120, min_periods=120).kurt().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_sign_changes_60d_base_v144_signal(high, low, closeadj, volume):
    """Count of sign-changes in A/D 5d-diff within 60d window (zig-zag count of accumulation flow)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    s = np.sign(ad.diff(5))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(60, min_periods=60).sum().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_sign_changes_30d_base_v145_signal(high, low, closeadj):
    """Count of CLV sign-flips in 30d window (whipsaw frequency)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    s = np.sign(clv)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(30, min_periods=30).sum().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_chaikin_above_signal_freq_40d_base_v146_signal(high, low, closeadj, volume):
    """Mean of (Chaikin Osc > Chaikin signal line) over 40d. Bounded [0,1]; bullish regime frac."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    ad = (clv * volume).cumsum()
    e3 = ad.ewm(span=3, adjust=False, min_periods=3).mean()
    e10 = ad.ewm(span=10, adjust=False, min_periods=10).mean()
    co = e3 - e10
    sig9 = co.ewm(span=9, adjust=False, min_periods=9).mean()
    above = (co > sig9).astype(float).where(~co.isna() & ~sig9.isna())
    return above.rolling(40, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_mfi14_vs_cmf21_diff_base_v147_signal(high, low, closeadj, volume):
    """(2*MFI_14/100 - 1) - CMF_21. Cross-construct money-flow differential."""
    tp = (high + low + closeadj) / 3.0
    rmf = tp * volume
    direction = np.sign(tp.diff(1))
    pos = rmf.where(direction > 0.0, 0.0)
    neg = rmf.where(direction < 0.0, 0.0)
    pf = pos.rolling(14, min_periods=14).sum()
    nf = neg.rolling(14, min_periods=14).sum().replace(0.0, np.nan)
    mfi = 100.0 - 100.0 / (1.0 + pf / nf)
    mfi_c = 2.0 * mfi / 100.0 - 1.0
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    n2 = (clv * volume).rolling(21, min_periods=21).sum()
    d2 = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    cmf = n2 / d2
    return (mfi_c - cmf).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_ad_log_path_30d_base_v148_signal(high, low, closeadj, volume):
    """log(1 + sum(|CLV*vol|, 30) / sum(vol, 30)). Log compressed total flow intensity."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cv_abs = (clv * volume).abs()
    num = cv_abs.rolling(30, min_periods=30).sum()
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return np.log1p(num / den).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_unweighted_75d_base_v149_signal(high, low, closeadj, volume):
    """CMF_75 minus simple CLV mean over 75d. Volume-weight vs. equal-weight differential at long N."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cmf = (clv * volume).rolling(75, min_periods=75).sum() / volume.rolling(75, min_periods=75).sum().replace(0.0, np.nan)
    sw = clv.rolling(75, min_periods=75).mean()
    return (cmf - sw).replace([np.inf, -np.inf], np.nan)


def f26ad_f26_accumulation_distribution_cmf21_arctan_slope_base_v150_signal(high, low, closeadj, volume):
    """arctan(5 * (CMF_21 - CMF_21.shift(15))). Bounded compressed CMF velocity."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    cmf = (clv * volume).rolling(21, min_periods=21).sum() / volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    return np.arctan(5.0 * (cmf - cmf.shift(15))).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f26_accumulation_distribution_base_076_150_REGISTRY = {
    "f26ad_f26_accumulation_distribution_clv_median_15d_base_v076_signal": {"inputs": ["high", "low", "close"], "func": f26ad_f26_accumulation_distribution_clv_median_15d_base_v076_signal},
    "f26ad_f26_accumulation_distribution_clv_iqr_45d_base_v077_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_iqr_45d_base_v077_signal},
    "f26ad_f26_accumulation_distribution_clv_mad_30d_base_v078_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_mad_30d_base_v078_signal},
    "f26ad_f26_accumulation_distribution_clv_skew_60d_base_v079_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_skew_60d_base_v079_signal},
    "f26ad_f26_accumulation_distribution_clv_kurt_120d_base_v080_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_kurt_120d_base_v080_signal},
    "f26ad_f26_accumulation_distribution_clv_q90_50d_base_v081_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_q90_50d_base_v081_signal},
    "f26ad_f26_accumulation_distribution_clv_q10_50d_base_v082_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_q10_50d_base_v082_signal},
    "f26ad_f26_accumulation_distribution_chaikin_hist_3_10_minus_signal_base_v083_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_hist_3_10_minus_signal_base_v083_signal},
    "f26ad_f26_accumulation_distribution_chaikin_signal_distance_60d_base_v084_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_signal_distance_60d_base_v084_signal},
    "f26ad_f26_accumulation_distribution_clv_pos_minus_neg_count_90d_base_v085_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_pos_minus_neg_count_90d_base_v085_signal},
    "f26ad_f26_accumulation_distribution_clv_count_strong_pos_60d_base_v086_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_count_strong_pos_60d_base_v086_signal},
    "f26ad_f26_accumulation_distribution_clv_count_strong_neg_60d_base_v087_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_count_strong_neg_60d_base_v087_signal},
    "f26ad_f26_accumulation_distribution_clv_rank_in_60d_base_v088_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_rank_in_60d_base_v088_signal},
    "f26ad_f26_accumulation_distribution_clv_volwtd_median_30d_base_v089_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_volwtd_median_30d_base_v089_signal},
    "f26ad_f26_accumulation_distribution_ad_regslope_60d_base_v090_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_regslope_60d_base_v090_signal},
    "f26ad_f26_accumulation_distribution_ad_rsq_120d_base_v091_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_rsq_120d_base_v091_signal},
    "f26ad_f26_accumulation_distribution_ad_residstd_50d_base_v092_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_residstd_50d_base_v092_signal},
    "f26ad_f26_accumulation_distribution_clvvol_return_corr_45d_base_v093_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_return_corr_45d_base_v093_signal},
    "f26ad_f26_accumulation_distribution_clv_vol_corr_30d_base_v094_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_vol_corr_30d_base_v094_signal},
    "f26ad_f26_accumulation_distribution_chaikin_acc_25d_base_v095_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_acc_25d_base_v095_signal},
    "f26ad_f26_accumulation_distribution_mfi_short_long_diff_base_v096_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_mfi_short_long_diff_base_v096_signal},
    "f26ad_f26_accumulation_distribution_arctan_mfi_zscore_60d_base_v097_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_arctan_mfi_zscore_60d_base_v097_signal},
    "f26ad_f26_accumulation_distribution_cmf21_minus_cmf50_75d_smoothed_base_v098_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf21_minus_cmf50_75d_smoothed_base_v098_signal},
    "f26ad_f26_accumulation_distribution_days_since_chaikin_xover_45d_base_v099_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_days_since_chaikin_xover_45d_base_v099_signal},
    "f26ad_f26_accumulation_distribution_ad_acc_zscore_30d_base_v100_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_acc_zscore_30d_base_v100_signal},
    "f26ad_f26_accumulation_distribution_chaikin_extreme_count_120d_base_v101_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_extreme_count_120d_base_v101_signal},
    "f26ad_f26_accumulation_distribution_clv_vol_weighted_mean_15d_base_v102_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_clv_vol_weighted_mean_15d_base_v102_signal},
    "f26ad_f26_accumulation_distribution_chaikin_z_60d_base_v103_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_z_60d_base_v103_signal},
    "f26ad_f26_accumulation_distribution_mfi14_rank_120d_base_v104_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_mfi14_rank_120d_base_v104_signal},
    "f26ad_f26_accumulation_distribution_mfi_oversold_frac_45d_base_v105_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_mfi_oversold_frac_45d_base_v105_signal},
    "f26ad_f26_accumulation_distribution_klinger_oscillator_norm_z_60d_base_v106_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_klinger_oscillator_norm_z_60d_base_v106_signal},
    "f26ad_f26_accumulation_distribution_ad_return_div_30d_base_v107_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_return_div_30d_base_v107_signal},
    "f26ad_f26_accumulation_distribution_clvvol_ac1_45d_base_v108_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_ac1_45d_base_v108_signal},
    "f26ad_f26_accumulation_distribution_chaikin_3_10_signal_dist_z_60d_base_v109_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_3_10_signal_dist_z_60d_base_v109_signal},
    "f26ad_f26_accumulation_distribution_clv_pos_streak_max_60d_base_v110_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_pos_streak_max_60d_base_v110_signal},
    "f26ad_f26_accumulation_distribution_clv_neg_streak_max_60d_base_v111_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_neg_streak_max_60d_base_v111_signal},
    "f26ad_f26_accumulation_distribution_ad_price_corr_50d_base_v112_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_price_corr_50d_base_v112_signal},
    "f26ad_f26_accumulation_distribution_ad_price_diff_corr_30d_base_v113_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_price_diff_corr_30d_base_v113_signal},
    "f26ad_f26_accumulation_distribution_clv_abs_mean_50d_base_v114_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_abs_mean_50d_base_v114_signal},
    "f26ad_f26_accumulation_distribution_high_acc_vol_share_50d_base_v115_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_high_acc_vol_share_50d_base_v115_signal},
    "f26ad_f26_accumulation_distribution_high_dist_vol_share_50d_base_v116_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_high_dist_vol_share_50d_base_v116_signal},
    "f26ad_f26_accumulation_distribution_clvvol_max_to_mean_30d_base_v117_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_max_to_mean_30d_base_v117_signal},
    "f26ad_f26_accumulation_distribution_chaikin_above_signal_xover_count_60d_base_v118_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_above_signal_xover_count_60d_base_v118_signal},
    "f26ad_f26_accumulation_distribution_ad_velocity_norm_60d_base_v119_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_velocity_norm_60d_base_v119_signal},
    "f26ad_f26_accumulation_distribution_clv_vol_corr_120d_base_v120_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_vol_corr_120d_base_v120_signal},
    "f26ad_f26_accumulation_distribution_clv_arctan_mean_30d_base_v121_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_arctan_mean_30d_base_v121_signal},
    "f26ad_f26_accumulation_distribution_tanh_clvvol_z_50d_base_v122_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_tanh_clvvol_z_50d_base_v122_signal},
    "f26ad_f26_accumulation_distribution_klinger_signal_dist_norm_base_v123_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_klinger_signal_dist_norm_base_v123_signal},
    "f26ad_f26_accumulation_distribution_ad_ema_diff_5_20_base_v124_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_ad_ema_diff_5_20_base_v124_signal},
    "f26ad_f26_accumulation_distribution_ad_obv_zspread_60d_base_v125_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_obv_zspread_60d_base_v125_signal},
    "f26ad_f26_accumulation_distribution_clv_neg_run_count_45d_base_v126_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_neg_run_count_45d_base_v126_signal},
    "f26ad_f26_accumulation_distribution_ad_log_velocity_30d_base_v127_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_log_velocity_30d_base_v127_signal},
    "f26ad_f26_accumulation_distribution_chaikin_sign_freq_30d_base_v128_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_sign_freq_30d_base_v128_signal},
    "f26ad_f26_accumulation_distribution_mfi_sign_freq_45d_base_v129_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_mfi_sign_freq_45d_base_v129_signal},
    "f26ad_f26_accumulation_distribution_clvvol_skew_60d_base_v130_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_skew_60d_base_v130_signal},
    "f26ad_f26_accumulation_distribution_ad_obv_diff_zscore_60d_base_v131_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_obv_diff_zscore_60d_base_v131_signal},
    "f26ad_f26_accumulation_distribution_ad_above_below_freq_90d_base_v132_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_above_below_freq_90d_base_v132_signal},
    "f26ad_f26_accumulation_distribution_clv_change_volwtd_45d_base_v133_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_change_volwtd_45d_base_v133_signal},
    "f26ad_f26_accumulation_distribution_williams_ad_zscore_60d_base_v134_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_williams_ad_zscore_60d_base_v134_signal},
    "f26ad_f26_accumulation_distribution_klinger_zero_streak_50d_base_v135_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_klinger_zero_streak_50d_base_v135_signal},
    "f26ad_f26_accumulation_distribution_clv_skew_rank_120d_base_v136_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_skew_rank_120d_base_v136_signal},
    "f26ad_f26_accumulation_distribution_clvvol_abs_share_50d_base_v137_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_abs_share_50d_base_v137_signal},
    "f26ad_f26_accumulation_distribution_clvvol_ema21_minus_sma21_base_v138_signal": {"inputs": ["high", "low", "close", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_ema21_minus_sma21_base_v138_signal},
    "f26ad_f26_accumulation_distribution_ad_path_efficiency_60d_base_v139_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_path_efficiency_60d_base_v139_signal},
    "f26ad_f26_accumulation_distribution_chaikin_path_efficiency_45d_base_v140_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_path_efficiency_45d_base_v140_signal},
    "f26ad_f26_accumulation_distribution_clv_volwtd_q75_30d_base_v141_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_volwtd_q75_30d_base_v141_signal},
    "f26ad_f26_accumulation_distribution_clv_volwtd_q25_30d_base_v142_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_volwtd_q25_30d_base_v142_signal},
    "f26ad_f26_accumulation_distribution_clvvol_volwtd_kurt_120d_base_v143_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clvvol_volwtd_kurt_120d_base_v143_signal},
    "f26ad_f26_accumulation_distribution_ad_sign_changes_60d_base_v144_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_sign_changes_60d_base_v144_signal},
    "f26ad_f26_accumulation_distribution_clv_sign_changes_30d_base_v145_signal": {"inputs": ["high", "low", "closeadj"], "func": f26ad_f26_accumulation_distribution_clv_sign_changes_30d_base_v145_signal},
    "f26ad_f26_accumulation_distribution_chaikin_above_signal_freq_40d_base_v146_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_chaikin_above_signal_freq_40d_base_v146_signal},
    "f26ad_f26_accumulation_distribution_mfi14_vs_cmf21_diff_base_v147_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_mfi14_vs_cmf21_diff_base_v147_signal},
    "f26ad_f26_accumulation_distribution_ad_log_path_30d_base_v148_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_ad_log_path_30d_base_v148_signal},
    "f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_unweighted_75d_base_v149_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_clv_volwtd_mean_minus_unweighted_75d_base_v149_signal},
    "f26ad_f26_accumulation_distribution_cmf21_arctan_slope_base_v150_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f26ad_f26_accumulation_distribution_cmf21_arctan_slope_base_v150_signal},
}


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------


def _synthetic_inputs(n: int = 800, seed: int = 42) -> pd.DataFrame:
    rng = np.random.default_rng(seed)
    seg = n // 4
    rest = n - 3 * seg
    ret = np.concatenate([
        rng.normal(0.0012, 0.011, seg),
        rng.normal(-0.0005, 0.018, seg),
        rng.normal(-0.0010, 0.014, seg),
        rng.normal(0.0008, 0.012, rest),
    ])
    close = 50.0 * np.exp(np.cumsum(ret))
    adj_drift = rng.normal(0.0, 0.0003, size=n).cumsum()
    closeadj = close * np.exp(adj_drift)
    intraday = rng.normal(0.0, 0.008, size=n)
    open_ = close * np.exp(-intraday * 0.5)
    high = np.maximum(close, open_) * np.exp(np.abs(rng.normal(0.0, 0.006, size=n)))
    low = np.minimum(close, open_) * np.exp(-np.abs(rng.normal(0.0, 0.006, size=n)))
    volume = rng.lognormal(mean=13.0, sigma=0.6, size=n)
    idx = pd.RangeIndex(n)
    return pd.DataFrame({
        "open": pd.Series(open_, index=idx, dtype=float),
        "high": pd.Series(high, index=idx, dtype=float),
        "low": pd.Series(low, index=idx, dtype=float),
        "close": pd.Series(close, index=idx, dtype=float),
        "closeadj": pd.Series(closeadj, index=idx, dtype=float),
        "volume": pd.Series(volume, index=idx, dtype=float),
    })


def _self_test() -> None:
    df = _synthetic_inputs(n=800, seed=42)
    results: dict[str, pd.Series] = {}
    for name, entry in f26_accumulation_distribution_base_076_150_REGISTRY.items():
        args = [df[col] for col in entry["inputs"]]
        out = entry["func"](*args)
        assert isinstance(out, pd.Series), f"{name}: not a Series"
        assert len(out) == len(df), f"{name}: length mismatch"
        clean = out.dropna()
        assert len(clean) > 0, f"{name}: all NaN"
        assert float(clean.std()) > 0.0 or clean.nunique() > 1, f"{name}: constant/all-zero"
        results[name] = out

    warm = 252
    coverage_ok = sum(1 for s in results.values() if s.iloc[warm:].isna().mean() < 0.5)
    frac = coverage_ok / len(results)
    assert frac >= 0.80, f"NaN-coverage too low: {frac:.2%} have <50% NaN after warm-up"

    aligned = pd.concat({n: results[n] for n in results}, axis=1).iloc[warm:]
    aligned = aligned.replace([np.inf, -np.inf], np.nan)
    corr = aligned.corr(min_periods=50).abs()
    np.fill_diagonal(corr.values, 0.0)
    max_corr = float(corr.max().max())
    if max_corr > 0.95:
        print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
        for i, a in enumerate(corr.columns):
            for j, b in enumerate(corr.columns):
                if j > i and corr.iloc[i, j] > 0.94:
                    print(f"  {a}  vs  {b}  ->  {corr.iloc[i, j]:.4f}")
    assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
    print(f"OK base_076_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
