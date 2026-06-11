"""f23_on_balance_volume_family base features 076-150.

Domain: On-Balance Volume (OBV) family — cumulative signed volume and its
derivatives/variants. Every feature here references OBV or an OBV-variant
cumulative-signed-volume construction (ADL, PVT, NVI/PVI, Force Index,
Klinger Volume Force, high-low signed cumulative volume, close-open signed
cumulative volume, Chaikin Oscillator, Money-Flow-Volume).

Structurally distinct from base_001_075 — no shared expression up to a
window-size change. NaN policy: never fillna(<value>); only replace
([inf,-inf], nan) at the final return. Window > 21d uses closeadj;
<= 21d uses close. Each function spells its formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers — kept short. Each feature spells its OBV-variant inline.
# ---------------------------------------------------------------------------


def _sma(s, n):
    return s.rolling(n, min_periods=n).mean()


def _ema(s, n):
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _streak_consec(x):
    c = 0
    for v in x[::-1]:
        if v > 0.5:
            c += 1
        else:
            break
    return float(c)


def _streak_days_since(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


# ---------------------------------------------------------------------------
# Features 076-150
# ---------------------------------------------------------------------------


# === CHAIKIN OSCILLATOR (EMA3 - EMA10 of ADL) ==============================




def f23ob_f23_on_balance_volume_family_chaikin_osc_norm_base_v077_signal(high, low, closeadj, volume):
    """Chaikin Osc / SMA(volume, 21). Normalized — window 21 -> closeadj boundary."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    osc = adl.ewm(span=3, adjust=False, min_periods=3).mean() - adl.ewm(span=10, adjust=False, min_periods=10).mean()
    v = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    return (osc / v).replace([np.inf, -np.inf], np.nan)




# === MONEY FLOW VOLUME (CLV*vol — non-cumulative) — short-window ============




def f23ob_f23_on_balance_volume_family_mfv_sma63_norm_base_v080_signal(high, low, closeadj, volume):
    """SMA(MFV, 63) / SMA(volume, 63). Long-horizon money-flow per unit volume."""
    rng = (high - low).replace(0.0, np.nan)
    mfv = ((closeadj - low) - (high - closeadj)) / rng * volume
    sm = mfv.rolling(63, min_periods=63).mean()
    v = volume.rolling(63, min_periods=63).mean().replace(0.0, np.nan)
    return (sm / v).replace([np.inf, -np.inf], np.nan)


# === OBV SHORT-DIFFERENTIAL of MAs (cross-window slope) ====================


def f23ob_f23_on_balance_volume_family_obv_ma_short_minus_long_30_90_base_v081_signal(closeadj, volume):
    """(SMA(OBV,30) - SMA(OBV,90)) / SMA(volume, 90). Slow-fast OBV MA spread."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    diff = obv.rolling(30, min_periods=30).mean() - obv.rolling(90, min_periods=90).mean()
    v = volume.rolling(90, min_periods=90).mean().replace(0.0, np.nan)
    return (diff / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_ema_short_minus_long_10_40_base_v082_signal(closeadj, volume):
    """(EMA(OBV,10) - EMA(OBV,40)) / SMA(volume, 40). Short EMA cross differential."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    diff = obv.ewm(span=10, adjust=False, min_periods=10).mean() - obv.ewm(span=40, adjust=False, min_periods=40).mean()
    v = volume.rolling(40, min_periods=40).mean().replace(0.0, np.nan)
    return (diff / v).replace([np.inf, -np.inf], np.nan)


# === OBV SIGN-AGREEMENT among multiple windows =============================


def f23ob_f23_on_balance_volume_family_obv_multi_sign_count_base_v083_signal(closeadj, volume):
    """Count of {SMA(OBV,10), SMA(OBV,30), SMA(OBV,60), SMA(OBV,120)} that OBV exceeds.
    Distinct from v067 ribbon (different windows). Range 0-4."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    mas = [obv.rolling(k, min_periods=k).mean() for k in (10, 30, 60, 120)]
    cnt = pd.Series(0.0, index=obv.index)
    mask = ~mas[0].isna()
    for m in mas:
        cnt = cnt + (obv > m).astype(float)
        mask = mask & ~m.isna()
    return cnt.where(mask).replace([np.inf, -np.inf], np.nan)


# === OBV "Bollinger-like" %B style =========================================


def f23ob_f23_on_balance_volume_family_obv_pctB_50d_base_v084_signal(closeadj, volume):
    """%B of OBV around SMA(OBV,50) +/- 2*std. Position of OBV in its own band."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    m = obv.rolling(50, min_periods=50).mean()
    sd = obv.rolling(50, min_periods=50).std()
    upper = m + 2.0 * sd; lower = m - 2.0 * sd
    return ((obv - lower) / (upper - lower).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_bandwidth_50d_base_v085_signal(closeadj, volume):
    """OBV-Bollinger band-width: 4*std(OBV,50) / SMA(volume, 50). Width-only measure."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    sd = obv.rolling(50, min_periods=50).std()
    v = volume.rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    return (4.0 * sd / v).replace([np.inf, -np.inf], np.nan)


# === ADL OSCILLATOR-style (ADL vs its own EMA) =============================


def f23ob_f23_on_balance_volume_family_adl_velocity_30d_base_v086_signal(high, low, closeadj, volume):
    """ADL.diff(5) / SMA(volume, 5) at boundary — kept short with 30d-mean denom for stability.
    Distinct from ADL.diff(30): inner k=5, outer normalization 30."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    v = volume.rolling(30, min_periods=30).mean().replace(0.0, np.nan)
    return (adl.diff(5) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_adl_curv_60d_base_v087_signal(high, low, closeadj, volume):
    """ADL curvature: ADL - 2*ADL.shift(30) + ADL.shift(60), normalized by SMA(vol, 60)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    c = adl - 2.0 * adl.shift(30) + adl.shift(60)
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    return (c / v).replace([np.inf, -np.inf], np.nan)


# === OBV vs PRICE RANK DIVERGENCE ==========================================


def f23ob_f23_on_balance_volume_family_obv_close_rank_diff_60d_base_v088_signal(closeadj, volume):
    """OBV.pctrank(60) - closeadj.pctrank(60). Rank-level divergence between accumulation and price."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return (obv.rolling(60, min_periods=60).rank(pct=True)
            - closeadj.rolling(60, min_periods=60).rank(pct=True)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_close_rank_diff_180d_base_v089_signal(closeadj, volume):
    """OBV.pctrank(180) - closeadj.pctrank(180). Long-window rank divergence."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return (obv.rolling(180, min_periods=180).rank(pct=True)
            - closeadj.rolling(180, min_periods=180).rank(pct=True)).replace([np.inf, -np.inf], np.nan)


# === OBV-DIFFUSION (variance per bar) =======================================


def f23ob_f23_on_balance_volume_family_obv_diff_std_45d_base_v090_signal(closeadj, volume):
    """45d rolling std of OBV.diff(). Daily signed-volume dispersion magnitude."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.diff().rolling(45, min_periods=45).std().replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_diff_std_norm_45d_base_v091_signal(closeadj, volume):
    """45d std(OBV.diff()) / SMA(volume, 45). Normalized accumulation volatility."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    sd = obv.diff().rolling(45, min_periods=45).std()
    v = volume.rolling(45, min_periods=45).mean().replace(0.0, np.nan)
    return (sd / v).replace([np.inf, -np.inf], np.nan)


# === CO-OBV "intraday accumulation" features ===============================


def f23ob_f23_on_balance_volume_family_obvco_dist_sma25_base_v092_signal(open, closeadj, volume):
    """(OBV_CO - SMA(OBV_CO, 25)) / SMA(volume, 25). OBV_CO distance from MA."""
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    m = obvco.rolling(25, min_periods=25).mean()
    v = volume.rolling(25, min_periods=25).mean().replace(0.0, np.nan)
    return ((obvco - m) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obvco_efficiency_45d_base_v093_signal(open, closeadj, volume):
    """|sum(co-signed vol, 45)| / sum(|co-signed vol|, 45). Intra-bar accumulation efficiency."""
    sv = np.sign(closeadj - open) * volume
    num = sv.rolling(45, min_periods=45).sum().abs()
    den = sv.abs().rolling(45, min_periods=45).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === HL-OBV "high-direction" features ======================================


def f23ob_f23_on_balance_volume_family_obvhl_dist_sma60_base_v094_signal(high, volume):
    """(OBV_HL - SMA(OBV_HL, 60)) / SMA(volume, 60). OBV_HL distance from MA."""
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    m = obvhl.rolling(60, min_periods=60).mean()
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    return ((obvhl - m) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obvhl_efficiency_80d_base_v095_signal(high, volume):
    """|sum(hl-signed vol, 80)| / sum(|hl-signed vol|, 80). High-pivot accumulation efficiency."""
    sv = np.sign(high.diff()) * volume
    num = sv.rolling(80, min_periods=80).sum().abs()
    den = sv.abs().rolling(80, min_periods=80).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === OBV LAGGED-CORR (lead-lag with price) =================================


def f23ob_f23_on_balance_volume_family_obv_lag_corr_5d_60d_base_v096_signal(closeadj, volume):
    """60d corr between OBV.diff(5) and closeadj.pct_change(5).shift(5). OBV LAGS price."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.diff(5).rolling(60, min_periods=60).corr(closeadj.pct_change(5).shift(5)).replace([np.inf, -np.inf], np.nan)


# === NVI/PVI ratios and slopes =============================================


def f23ob_f23_on_balance_volume_family_nvi_slope_63d_base_v097_signal(closeadj, volume):
    """NVI.pct_change(63). 3-month NVI growth rate."""
    r = closeadj.pct_change()
    v_down = volume < volume.shift(1)
    factor = np.where(v_down, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    nvi = pd.Series(np.cumprod(factor), index=closeadj.index); nvi.iloc[0] = np.nan
    return nvi.pct_change(63).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_pvi_slope_63d_base_v098_signal(closeadj, volume):
    """PVI.pct_change(63). 3-month PVI growth rate."""
    r = closeadj.pct_change()
    v_up = volume > volume.shift(1)
    factor = np.where(v_up, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    pvi = pd.Series(np.cumprod(factor), index=closeadj.index); pvi.iloc[0] = np.nan
    return pvi.pct_change(63).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_sign_nvi_ema100_base_v099_signal(closeadj, volume):
    """sign(NVI - EMA(NVI, 100)). NVI above/below long EMA."""
    r = closeadj.pct_change()
    v_down = volume < volume.shift(1)
    factor = np.where(v_down, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    nvi = pd.Series(np.cumprod(factor), index=closeadj.index); nvi.iloc[0] = np.nan
    e = nvi.ewm(span=100, adjust=False, min_periods=100).mean()
    return np.sign(nvi - e).replace([np.inf, -np.inf], np.nan)


# === KVO derivatives and rolling stats =====================================


def f23ob_f23_on_balance_volume_family_kvo_zscore_120d_base_v100_signal(high, low, closeadj, volume):
    """z-score of KVO over 120d. Standardized Klinger oscillator level."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    kvo = (vf.ewm(span=34, adjust=False, min_periods=34).mean()
           - vf.ewm(span=55, adjust=False, min_periods=55).mean())
    mu = kvo.rolling(120, min_periods=120).mean()
    sd = kvo.rolling(120, min_periods=120).std()
    return ((kvo - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_vf_corr_close_60d_base_v101_signal(high, low, closeadj, volume):
    """60d corr between Klinger volume-force (vf=vol*sign(tp.diff)) and closeadj.diff().
    Direct volume-force vs price-change agreement."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    return vf.rolling(60, min_periods=60).corr(closeadj.diff()).replace([np.inf, -np.inf], np.nan)


# === FORCE INDEX (long EMA) and pure FI mean ===============================


def f23ob_f23_on_balance_volume_family_fi_ema_100d_norm_base_v102_signal(closeadj, volume):
    """EMA(FI, 100) / SMA(volume*|close.diff|, 100). Long-term smoothed force normalized."""
    fi = closeadj.diff() * volume
    e = fi.ewm(span=100, adjust=False, min_periods=100).mean()
    sm = (volume * closeadj.diff().abs()).rolling(100, min_periods=100).mean().replace(0.0, np.nan)
    return (e / sm).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_fi_skew_60d_base_v103_signal(closeadj, volume):
    """60d skew of raw FI (close.diff*vol). Distributional asymmetry of force."""
    fi = closeadj.diff() * volume
    return fi.rolling(60, min_periods=60).skew().replace([np.inf, -np.inf], np.nan)


# === OBV-DIFF (level vs slope) at various windows ==========================


def f23ob_f23_on_balance_volume_family_obv_diff5_diff21_ratio_base_v104_signal(close, volume):
    """OBV.diff(5)/OBV.diff(21). Short-vs-mid OBV slope ratio."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    return (obv.diff(5) / obv.diff(21).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obv_diff21_pct_of_voltotal_base_v105_signal(closeadj, volume):
    """OBV.diff(21) / volume.rolling(21).sum(). Net accumulation fraction over 21d."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    den = volume.rolling(21, min_periods=21).sum().replace(0.0, np.nan)
    return (obv.diff(21) / den).replace([np.inf, -np.inf], np.nan)


# === OBV REGRESSION SLOPE at LONG window ===================================


def f23ob_f23_on_balance_volume_family_obv_regslope_120d_base_v106_signal(closeadj, volume):
    """OLS slope of OBV vs time over 120 bars, normalized by SMA(vol, 120)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    v = volume.rolling(120, min_periods=120).mean().replace(0.0, np.nan)
    def _slope(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        var = np.sum((t - mt) ** 2)
        if var == 0.0 or not np.isfinite(mx):
            return np.nan
        return float(cov / var)
    sl = obv.rolling(120, min_periods=120).apply(_slope, raw=True)
    return (sl / v).replace([np.inf, -np.inf], np.nan)


# === ADL REGRESSION SLOPE ==================================================


def f23ob_f23_on_balance_volume_family_adl_rsq_100d_base_v107_signal(high, low, closeadj, volume):
    """R^2 of OLS fit ADL vs time over 100 bars. Trend purity of CLV-weighted accumulation."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    def _rsq(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2); vx = np.sum((x - mx) ** 2)
        if vt == 0.0 or vx == 0.0:
            return np.nan
        r = cov / np.sqrt(vt * vx)
        return float(r * r)
    return adl.rolling(100, min_periods=100).apply(_rsq, raw=True).replace([np.inf, -np.inf], np.nan)


# === DAYS-SINCE OBV crossed shift-N reference ==============================


def f23ob_f23_on_balance_volume_family_daysince_obv_shift42_80d_base_v108_signal(closeadj, volume):
    """Bars since last sign-change of (OBV - OBV.shift(42)), capped 80."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    s = np.sign(obv - obv.shift(42))
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(80, min_periods=80).apply(_streak_days_since, raw=True).replace([np.inf, -np.inf], np.nan)


# === STREAK below OBV MA ===================================================


def f23ob_f23_on_balance_volume_family_obv_below_ema60_streak_80d_base_v109_signal(closeadj, volume):
    """Consecutive bars (cap 80) where OBV < EMA(OBV, 60)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    e = obv.ewm(span=60, adjust=False, min_periods=60).mean()
    sgn = (obv < e).astype(float).where(~e.isna())
    return sgn.rolling(80, min_periods=80).apply(_streak_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === OBV SECTIONAL diversity (cross-method cumulative-signed comparisons) ==


def f23ob_f23_on_balance_volume_family_obvco_vs_obv_corr_60d_base_v110_signal(open, closeadj, volume):
    """60d corr between OBV_CO.diff(5) and OBV.diff(5). Intra-bar vs prev-close-bar agreement."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    return obvco.diff(5).rolling(60, min_periods=60).corr(obv.diff(5)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_obvhl_vs_obv_corr_90d_base_v111_signal(high, closeadj, volume):
    """90d corr between OBV_HL.diff(10) and OBV.diff(10). High-pivot vs close-pivot signal agreement."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    return obvhl.diff(10).rolling(90, min_periods=90).corr(obv.diff(10)).replace([np.inf, -np.inf], np.nan)


# === OBV vs FORCE-INDEX correlation ========================================


def f23ob_f23_on_balance_volume_family_obv_fi_corr_60d_base_v112_signal(closeadj, volume):
    """60d Pearson corr between OBV.diff(5) and Force Index (close.diff*vol).
    Signed-volume vs price-weighted-volume agreement."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    fi = closeadj.diff() * volume
    return obv.diff(5).rolling(60, min_periods=60).corr(fi).replace([np.inf, -np.inf], np.nan)


# === CO-OBV STOCHASTIC (intra-bar signed) ==================================


def f23ob_f23_on_balance_volume_family_obvco_stoch_50d_base_v113_signal(open, closeadj, volume):
    """Stoch %K of OBV_CO over 50d. Intra-bar accumulation in own range."""
    obvco = (np.sign(closeadj - open) * volume).cumsum()
    hi = obvco.rolling(50, min_periods=50).max()
    lo = obvco.rolling(50, min_periods=50).min()
    return ((obvco - lo) / (hi - lo).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === OBV SHIFT-RATIO (path-dependence) =====================================


def f23ob_f23_on_balance_volume_family_obv_shiftratio_30_90_base_v114_signal(closeadj, volume):
    """(OBV - OBV.shift(30)) / (OBV - OBV.shift(90)). Short impulse fraction of long impulse."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return ((obv - obv.shift(30)) / (obv - obv.shift(90)).replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === OBV-DETRENDED (residual from OLS line) ================================


def f23ob_f23_on_balance_volume_family_obv_detrended_z_80d_base_v115_signal(closeadj, volume):
    """Final residual / SMA(vol,80) of OLS fit OBV vs time. Detrended OBV impulse."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    v = volume.rolling(80, min_periods=80).mean().replace(0.0, np.nan)
    def _resid_last(x):
        n = len(x); t = np.arange(n, dtype=float)
        mt = t.mean(); mx = x.mean()
        cov = np.sum((t - mt) * (x - mx))
        vt = np.sum((t - mt) ** 2)
        if vt == 0.0:
            return np.nan
        b = cov / vt; a = mx - b * mt
        return float(x[-1] - (a + b * t[-1]))
    rs = obv.rolling(80, min_periods=80).apply(_resid_last, raw=True)
    return (rs / v).replace([np.inf, -np.inf], np.nan)


# === SIGNED-VOLUME DAILY (non-cumulative — different shape) ================


def f23ob_f23_on_balance_volume_family_signed_vol_emaratio_5_20_base_v116_signal(close, volume):
    """EMA(signed_vol, 5) / EMA(signed_vol, 20). Short-vs-mid signed-flow ratio.
    signed_vol = sign(close.diff)*volume (the OBV increment series, non-cumulative)."""
    sv = np.sign(close.diff()) * volume
    e_s = sv.ewm(span=5, adjust=False, min_periods=5).mean()
    e_l = sv.ewm(span=20, adjust=False, min_periods=20).mean()
    return (e_s / e_l.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_signed_vol_zscore_50d_base_v117_signal(closeadj, volume):
    """z-score of signed_vol over 50d. Standardized daily accumulation."""
    sv = np.sign(closeadj.diff()) * volume
    mu = sv.rolling(50, min_periods=50).mean()
    sd = sv.rolling(50, min_periods=50).std()
    return ((sv - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === OBV cumulative-ratio (cumulative / cumulative_volume) ================


def f23ob_f23_on_balance_volume_family_obv_cumvolume_ratio_base_v118_signal(close, volume):
    """OBV / cumsum(volume). Lifetime net accumulation fraction in [-1,1]."""
    obv = (np.sign(close.diff()) * volume).cumsum()
    return (obv / volume.cumsum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ADL z-score in window =================================================


def f23ob_f23_on_balance_volume_family_adl_zscore_70d_base_v119_signal(high, low, closeadj, volume):
    """z-score of ADL over 70d trailing window."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    mu = adl.rolling(70, min_periods=70).mean()
    sd = adl.rolling(70, min_periods=70).std()
    return ((adl - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === ADL fraction-above-MA =================================================


def f23ob_f23_on_balance_volume_family_adl_fracabove_sma40_50d_base_v120_signal(high, low, closeadj, volume):
    """Frac of 50 bars where ADL > SMA(ADL, 40)."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    m = adl.rolling(40, min_periods=40).mean()
    sgn = (adl > m).astype(float).where(~m.isna())
    return sgn.rolling(50, min_periods=50).mean().replace([np.inf, -np.inf], np.nan)


# === PVT z-score and pctrank ===============================================


def f23ob_f23_on_balance_volume_family_pvt_zscore_70d_base_v121_signal(closeadj, volume):
    """z-score of PVT over 70d window."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    mu = pvt.rolling(70, min_periods=70).mean()
    sd = pvt.rolling(70, min_periods=70).std()
    return ((pvt - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_pvt_pctrank_180d_base_v122_signal(closeadj, volume):
    """180d percentile rank of PVT."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    return pvt.rolling(180, min_periods=180).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === FORCE-INDEX RATIO and BOUNDED transform ===============================


def f23ob_f23_on_balance_volume_family_fi_short_long_ratio_base_v123_signal(close, volume):
    """EMA(FI, 5) / EMA(FI, 20). Short vs mid force-index ratio."""
    fi = close.diff() * volume
    s = fi.ewm(span=5, adjust=False, min_periods=5).mean()
    l = fi.ewm(span=20, adjust=False, min_periods=20).mean()
    return (s / l.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_fi_arctan_z_30d_base_v124_signal(close, volume):
    """arctan of z-score of FI (raw) over 30d. Bounded force-index magnitude."""
    fi = close.diff() * volume
    mu = fi.rolling(30, min_periods=30).mean()
    sd = fi.rolling(30, min_periods=30).std()
    z = (fi - mu) / sd.replace(0.0, np.nan)
    return np.arctan(z).replace([np.inf, -np.inf], np.nan)


# === KLINGER SHORT-vs-LONG VF differential and bounded ====================


def f23ob_f23_on_balance_volume_family_kvo_ema_slope_42d_base_v125_signal(high, low, closeadj, volume):
    """KVO.diff(21) / SMA(vol, 21). Slope of Klinger."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    kvo = (vf.ewm(span=34, adjust=False, min_periods=34).mean()
           - vf.ewm(span=55, adjust=False, min_periods=55).mean())
    v = volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)
    return (kvo.diff(21) / v).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_kvo_signal_distance_base_v126_signal(high, low, closeadj, volume):
    """(KVO - EMA(KVO,13)) / SMA(volume, 13). Distance from Klinger signal line, normalized."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    kvo = (vf.ewm(span=34, adjust=False, min_periods=34).mean()
           - vf.ewm(span=55, adjust=False, min_periods=55).mean())
    sig = kvo.ewm(span=13, adjust=False, min_periods=13).mean()
    v = volume.rolling(13, min_periods=13).mean().replace(0.0, np.nan)
    return ((kvo - sig) / v).replace([np.inf, -np.inf], np.nan)


# === CHAIKIN OSC pctrank ====================================================


def f23ob_f23_on_balance_volume_family_chaikin_osc_pctrank_120d_base_v127_signal(high, low, closeadj, volume):
    """120d percentile rank of Chaikin Oscillator."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    osc = adl.ewm(span=3, adjust=False, min_periods=3).mean() - adl.ewm(span=10, adjust=False, min_periods=10).mean()
    return osc.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === NVI/PVI relative to themselves' MA =====================================


def f23ob_f23_on_balance_volume_family_nvi_pctrank_60d_base_v128_signal(closeadj, volume):
    """60d percentile rank of NVI. Short-horizon NVI rank."""
    r = closeadj.pct_change()
    v_down = volume < volume.shift(1)
    factor = np.where(v_down, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    nvi = pd.Series(np.cumprod(factor), index=closeadj.index); nvi.iloc[0] = np.nan
    return nvi.rolling(60, min_periods=60).rank(pct=True).replace([np.inf, -np.inf], np.nan)


def f23ob_f23_on_balance_volume_family_pvi_pctrank_120d_base_v129_signal(closeadj, volume):
    """120d percentile rank of PVI."""
    r = closeadj.pct_change()
    v_up = volume > volume.shift(1)
    factor = np.where(v_up, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    pvi = pd.Series(np.cumprod(factor), index=closeadj.index); pvi.iloc[0] = np.nan
    return pvi.rolling(120, min_periods=120).rank(pct=True).replace([np.inf, -np.inf], np.nan)


# === NVI z-score ==========================================================


def f23ob_f23_on_balance_volume_family_nvi_zscore_90d_base_v130_signal(closeadj, volume):
    """z-score of NVI over 90d window."""
    r = closeadj.pct_change()
    v_down = volume < volume.shift(1)
    factor = np.where(v_down, 1.0 + r, 1.0)
    factor = np.where(np.isfinite(factor), factor, 1.0)
    nvi = pd.Series(np.cumprod(factor), index=closeadj.index); nvi.iloc[0] = np.nan
    mu = nvi.rolling(90, min_periods=90).mean()
    sd = nvi.rolling(90, min_periods=90).std()
    return ((nvi - mu) / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === OBV ENTROPY-style (Shannon of binary up/down) =========================


def f23ob_f23_on_balance_volume_family_obv_direction_entropy_50d_base_v131_signal(closeadj, volume):
    """Shannon entropy of binary {OBV.diff>0} fraction p over 50d:
    H = -p*log2(p) - (1-p)*log2(1-p). Choppiness measure."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    bn = (obv.diff() > 0).astype(float).where(~obv.diff().isna())
    p = bn.rolling(50, min_periods=50).mean()
    p_clip = p.clip(1e-9, 1.0 - 1e-9)
    h = -(p_clip * np.log2(p_clip) + (1.0 - p_clip) * np.log2(1.0 - p_clip))
    return h.where(~p.isna()).replace([np.inf, -np.inf], np.nan)


# === SAFE LOG-OBV (signed) ==================================================


def f23ob_f23_on_balance_volume_family_obv_signedlog_level_norm_base_v132_signal(closeadj, volume):
    """signed-log(OBV / SMA(volume, 50)). Sign-preserving compression of OBV level."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    v = volume.rolling(50, min_periods=50).mean().replace(0.0, np.nan)
    r = obv / v
    return (np.sign(r) * np.log1p(r.abs())).replace([np.inf, -np.inf], np.nan)


# === ADL SHORT-vs-LONG kernel ratio =========================================


def f23ob_f23_on_balance_volume_family_adl_revrate_sma30_60d_base_v133_signal(high, low, closeadj, volume):
    """60d count of sign-flips of (ADL - SMA(ADL,30)) / 60. ADL mean-reversion frequency."""
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    diff = adl - adl.rolling(30, min_periods=30).mean()
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return (flip.rolling(60, min_periods=60).sum() / 60.0).replace([np.inf, -np.inf], np.nan)


# === PVT MA-distance =======================================================


def f23ob_f23_on_balance_volume_family_pvt_ma_short_long_diff_base_v134_signal(closeadj, volume):
    """SMA(PVT,20) - SMA(PVT,80), normalized by SMA(volume,80). PVT MA differential."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    diff = pvt.rolling(20, min_periods=20).mean() - pvt.rolling(80, min_periods=80).mean()
    v = volume.rolling(80, min_periods=80).mean().replace(0.0, np.nan)
    return (diff / v).replace([np.inf, -np.inf], np.nan)


# === PVT-derivative bounded ================================================


def f23ob_f23_on_balance_volume_family_pvt_tanh_slope_30d_base_v135_signal(closeadj, volume):
    """tanh of PVT.diff(30)/std(PVT.diff(30), 60). Bounded PVT impulse."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    d = pvt.diff(30)
    sd = d.rolling(60, min_periods=60).std()
    return np.tanh(d / sd.replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# === OBV-DIFF AUTOCORR-LAG-5 (different lag) ================================


def f23ob_f23_on_balance_volume_family_obv_diff_autocorr5_90d_base_v136_signal(closeadj, volume):
    """90d lag-5 autocorrelation of OBV.diff(). Weekly persistence pattern of accumulation."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    d = obv.diff()
    return d.rolling(90, min_periods=90).apply(
        lambda x: float(pd.Series(x).autocorr(lag=5)) if pd.Series(x).std() > 0 else np.nan,
        raw=False,
    ).replace([np.inf, -np.inf], np.nan)


# === OBV vs PRICE z-score difference =======================================


def f23ob_f23_on_balance_volume_family_obv_close_zscore_diff_45d_base_v137_signal(closeadj, volume):
    """z(OBV,45) - z(closeadj,45). Standardized-level divergence between accumulation and price."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    mu_o = obv.rolling(45, min_periods=45).mean(); sd_o = obv.rolling(45, min_periods=45).std()
    mu_c = closeadj.rolling(45, min_periods=45).mean(); sd_c = closeadj.rolling(45, min_periods=45).std()
    z_o = (obv - mu_o) / sd_o.replace(0.0, np.nan)
    z_c = (closeadj - mu_c) / sd_c.replace(0.0, np.nan)
    return (z_o - z_c).replace([np.inf, -np.inf], np.nan)


# === OBV WINDOW SIGN-PROFILE ===============================================


def f23ob_f23_on_balance_volume_family_obv_uppct_60d_base_v138_signal(closeadj, volume):
    """Fraction of last 60 bars where OBV.diff() > 0. Up-bar frequency of accumulation."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    bn = (obv.diff() > 0).astype(float).where(~obv.diff().isna())
    return bn.rolling(60, min_periods=60).mean().replace([np.inf, -np.inf], np.nan)


# === OBV DRAWDOWN (rolling max - current OBV) ==============================


def f23ob_f23_on_balance_volume_family_obv_drawdown_120d_base_v139_signal(closeadj, volume):
    """(rolling_max(OBV,120) - OBV) / SMA(volume, 120). Drawdown from peak accumulation."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    peak = obv.rolling(120, min_periods=120).max()
    v = volume.rolling(120, min_periods=120).mean().replace(0.0, np.nan)
    return ((peak - obv) / v).replace([np.inf, -np.inf], np.nan)


# === OBV WINSORIZED-MEAN of daily increments ==============================


def f23ob_f23_on_balance_volume_family_obv_diff_winsor_60d_base_v140_signal(closeadj, volume):
    """Winsorized 10%-trimmed mean of OBV.diff() over 60d, normalized by SMA(volume,60)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    d = obv.diff()
    def _wins(x):
        if len(x) < 5:
            return np.nan
        lo = np.quantile(x, 0.1); hi = np.quantile(x, 0.9)
        return float(np.mean(np.clip(x, lo, hi)))
    sm = d.rolling(60, min_periods=60).apply(_wins, raw=True)
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    return (sm / v).replace([np.inf, -np.inf], np.nan)


# === ADL/PVT/OBV TRIPLE-SIGN agreement count ===============================


def f23ob_f23_on_balance_volume_family_obv_adl_pvt_sign_agreement_base_v141_signal(high, low, closeadj, volume):
    """Sum of sign({OBV.diff(10), ADL.diff(10), PVT.diff(10)}) — range -3..+3."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    rng = (high - low).replace(0.0, np.nan)
    clv = ((closeadj - low) - (high - closeadj)) / rng
    adl = (clv * volume).cumsum()
    pvt = (closeadj.pct_change() * volume).cumsum()
    sgn = np.sign(obv.diff(10)) + np.sign(adl.diff(10)) + np.sign(pvt.diff(10))
    return sgn.replace([np.inf, -np.inf], np.nan)


# === OBV-MEDIAN comparison (robust) ========================================


def f23ob_f23_on_balance_volume_family_obv_iqr_60d_norm_base_v142_signal(closeadj, volume):
    """(Q75-Q25)(OBV, 60) / SMA(volume, 60). Interquartile range of OBV, normalized.
    Distinct robust dispersion measure of OBV history."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    q75 = obv.rolling(60, min_periods=60).quantile(0.75)
    q25 = obv.rolling(60, min_periods=60).quantile(0.25)
    v = volume.rolling(60, min_periods=60).mean().replace(0.0, np.nan)
    return ((q75 - q25) / v).replace([np.inf, -np.inf], np.nan)


# === OBV cross-corr LAG (asymmetric) =======================================


def f23ob_f23_on_balance_volume_family_close_lag_obv_corr_42d_base_v143_signal(closeadj, volume):
    """42d corr between closeadj.pct_change(5) and OBV.diff(5).shift(5). Price lags OBV."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return closeadj.pct_change(5).rolling(42, min_periods=42).corr(obv.diff(5).shift(5)).replace([np.inf, -np.inf], np.nan)


# === OBV-RANGE / OBV-MEAN (coefficient of variation) =======================


def f23ob_f23_on_balance_volume_family_obv_cv_30d_base_v144_signal(closeadj, volume):
    """std(OBV, 30) / |mean(OBV, 30)|. OBV coefficient of variation (path stability)."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    sd = obv.rolling(30, min_periods=30).std()
    mu = obv.rolling(30, min_periods=30).mean().abs().replace(0.0, np.nan)
    return (sd / mu).replace([np.inf, -np.inf], np.nan)


# === KVO above zero line (regime) ==========================================


def f23ob_f23_on_balance_volume_family_kvo_fracpos_40d_base_v145_signal(high, low, closeadj, volume):
    """Frac of last 40 bars where KVO > 0. Klinger positive regime fraction."""
    tp = (high + low + closeadj) / 3.0
    vf = volume * np.sign(tp.diff())
    kvo = (vf.ewm(span=34, adjust=False, min_periods=34).mean()
           - vf.ewm(span=55, adjust=False, min_periods=55).mean())
    sgn = (kvo > 0).astype(float).where(~kvo.isna())
    return sgn.rolling(40, min_periods=40).mean().replace([np.inf, -np.inf], np.nan)


# === Closing-on-strength (CO sign × volume rolling sum / closing-on-weakness)


def f23ob_f23_on_balance_volume_family_obvco_upvol_downvol_logratio_base_v146_signal(open, closeadj, volume):
    """log(sum(vol on close>open, 30) / sum(vol on close<open, 30)).
    OBV-CO style up/down volume log ratio."""
    upv = volume.where(closeadj > open, 0.0)
    dnv = volume.where(closeadj < open, 0.0)
    u = upv.rolling(30, min_periods=30).sum()
    d = dnv.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return np.log(u / d).replace([np.inf, -np.inf], np.nan)


# === HL-OBV streak above its MA ============================================


def f23ob_f23_on_balance_volume_family_obvhl_streak_above_sma40_50d_base_v147_signal(high, volume):
    """Consecutive bars (cap 50) where OBV_HL > SMA(OBV_HL, 40)."""
    obvhl = (np.sign(high.diff()) * volume).cumsum()
    m = obvhl.rolling(40, min_periods=40).mean()
    sgn = (obvhl > m).astype(float).where(~m.isna())
    return sgn.rolling(50, min_periods=50).apply(_streak_consec, raw=True).replace([np.inf, -np.inf], np.nan)


# === DAYS-SINCE PVT MA crossover ===========================================


def f23ob_f23_on_balance_volume_family_daysince_pvt_sma50_70d_base_v148_signal(closeadj, volume):
    """Bars since last sign-change of (PVT - SMA(PVT, 50)), capped 70."""
    pvt = (closeadj.pct_change() * volume).cumsum()
    diff = pvt - pvt.rolling(50, min_periods=50).mean()
    s = np.sign(diff)
    flip = (s != s.shift(1)).astype(float).where(~s.isna() & ~s.shift(1).isna())
    return flip.rolling(70, min_periods=70).apply(_streak_days_since, raw=True).replace([np.inf, -np.inf], np.nan)


# === OBV-DIFF CORR with closeadj.diff (raw not pctchange) ==================


def f23ob_f23_on_balance_volume_family_obvdiff_closediff_corr_30d_base_v149_signal(closeadj, volume):
    """30d corr between OBV.diff() and closeadj.diff(). Daily price-volume sign relation."""
    obv = (np.sign(closeadj.diff()) * volume).cumsum()
    return obv.diff().rolling(30, min_periods=30).corr(closeadj.diff()).replace([np.inf, -np.inf], np.nan)


# === SUMMED CO-OBV / SUMMED OBV ratio (cross-construction efficiency) =====


def f23ob_f23_on_balance_volume_family_obv_co_ratio_120d_base_v150_signal(open, closeadj, volume):
    """sum(co_signed_vol, 120) / sum(obv_signed_vol, 120). Intra-vs-inter bar accumulation ratio."""
    sv_co = np.sign(closeadj - open) * volume
    sv_obv = np.sign(closeadj.diff()) * volume
    num = sv_co.rolling(120, min_periods=120).sum()
    den = sv_obv.rolling(120, min_periods=120).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f23_on_balance_volume_family_base_076_150_REGISTRY = {
    "f23ob_f23_on_balance_volume_family_chaikin_osc_norm_base_v077_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_chaikin_osc_norm_base_v077_signal},
    "f23ob_f23_on_balance_volume_family_mfv_sma63_norm_base_v080_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_mfv_sma63_norm_base_v080_signal},
    "f23ob_f23_on_balance_volume_family_obv_ma_short_minus_long_30_90_base_v081_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_ma_short_minus_long_30_90_base_v081_signal},
    "f23ob_f23_on_balance_volume_family_obv_ema_short_minus_long_10_40_base_v082_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_ema_short_minus_long_10_40_base_v082_signal},
    "f23ob_f23_on_balance_volume_family_obv_multi_sign_count_base_v083_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_multi_sign_count_base_v083_signal},
    "f23ob_f23_on_balance_volume_family_obv_pctB_50d_base_v084_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_pctB_50d_base_v084_signal},
    "f23ob_f23_on_balance_volume_family_obv_bandwidth_50d_base_v085_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_bandwidth_50d_base_v085_signal},
    "f23ob_f23_on_balance_volume_family_adl_velocity_30d_base_v086_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_velocity_30d_base_v086_signal},
    "f23ob_f23_on_balance_volume_family_adl_curv_60d_base_v087_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_curv_60d_base_v087_signal},
    "f23ob_f23_on_balance_volume_family_obv_close_rank_diff_60d_base_v088_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_close_rank_diff_60d_base_v088_signal},
    "f23ob_f23_on_balance_volume_family_obv_close_rank_diff_180d_base_v089_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_close_rank_diff_180d_base_v089_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff_std_45d_base_v090_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff_std_45d_base_v090_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff_std_norm_45d_base_v091_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff_std_norm_45d_base_v091_signal},
    "f23ob_f23_on_balance_volume_family_obvco_dist_sma25_base_v092_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_dist_sma25_base_v092_signal},
    "f23ob_f23_on_balance_volume_family_obvco_efficiency_45d_base_v093_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_efficiency_45d_base_v093_signal},
    "f23ob_f23_on_balance_volume_family_obvhl_dist_sma60_base_v094_signal": {"inputs": ["high", "volume"], "func": f23ob_f23_on_balance_volume_family_obvhl_dist_sma60_base_v094_signal},
    "f23ob_f23_on_balance_volume_family_obvhl_efficiency_80d_base_v095_signal": {"inputs": ["high", "volume"], "func": f23ob_f23_on_balance_volume_family_obvhl_efficiency_80d_base_v095_signal},
    "f23ob_f23_on_balance_volume_family_obv_lag_corr_5d_60d_base_v096_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_lag_corr_5d_60d_base_v096_signal},
    "f23ob_f23_on_balance_volume_family_nvi_slope_63d_base_v097_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_nvi_slope_63d_base_v097_signal},
    "f23ob_f23_on_balance_volume_family_pvi_slope_63d_base_v098_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvi_slope_63d_base_v098_signal},
    "f23ob_f23_on_balance_volume_family_sign_nvi_ema100_base_v099_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_sign_nvi_ema100_base_v099_signal},
    "f23ob_f23_on_balance_volume_family_kvo_zscore_120d_base_v100_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_kvo_zscore_120d_base_v100_signal},
    "f23ob_f23_on_balance_volume_family_vf_corr_close_60d_base_v101_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_vf_corr_close_60d_base_v101_signal},
    "f23ob_f23_on_balance_volume_family_fi_ema_100d_norm_base_v102_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_fi_ema_100d_norm_base_v102_signal},
    "f23ob_f23_on_balance_volume_family_fi_skew_60d_base_v103_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_fi_skew_60d_base_v103_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff5_diff21_ratio_base_v104_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff5_diff21_ratio_base_v104_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff21_pct_of_voltotal_base_v105_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff21_pct_of_voltotal_base_v105_signal},
    "f23ob_f23_on_balance_volume_family_obv_regslope_120d_base_v106_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_regslope_120d_base_v106_signal},
    "f23ob_f23_on_balance_volume_family_adl_rsq_100d_base_v107_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_rsq_100d_base_v107_signal},
    "f23ob_f23_on_balance_volume_family_daysince_obv_shift42_80d_base_v108_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_daysince_obv_shift42_80d_base_v108_signal},
    "f23ob_f23_on_balance_volume_family_obv_below_ema60_streak_80d_base_v109_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_below_ema60_streak_80d_base_v109_signal},
    "f23ob_f23_on_balance_volume_family_obvco_vs_obv_corr_60d_base_v110_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_vs_obv_corr_60d_base_v110_signal},
    "f23ob_f23_on_balance_volume_family_obvhl_vs_obv_corr_90d_base_v111_signal": {"inputs": ["high", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvhl_vs_obv_corr_90d_base_v111_signal},
    "f23ob_f23_on_balance_volume_family_obv_fi_corr_60d_base_v112_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_fi_corr_60d_base_v112_signal},
    "f23ob_f23_on_balance_volume_family_obvco_stoch_50d_base_v113_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_stoch_50d_base_v113_signal},
    "f23ob_f23_on_balance_volume_family_obv_shiftratio_30_90_base_v114_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_shiftratio_30_90_base_v114_signal},
    "f23ob_f23_on_balance_volume_family_obv_detrended_z_80d_base_v115_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_detrended_z_80d_base_v115_signal},
    "f23ob_f23_on_balance_volume_family_signed_vol_emaratio_5_20_base_v116_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_signed_vol_emaratio_5_20_base_v116_signal},
    "f23ob_f23_on_balance_volume_family_signed_vol_zscore_50d_base_v117_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_signed_vol_zscore_50d_base_v117_signal},
    "f23ob_f23_on_balance_volume_family_obv_cumvolume_ratio_base_v118_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_cumvolume_ratio_base_v118_signal},
    "f23ob_f23_on_balance_volume_family_adl_zscore_70d_base_v119_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_zscore_70d_base_v119_signal},
    "f23ob_f23_on_balance_volume_family_adl_fracabove_sma40_50d_base_v120_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_fracabove_sma40_50d_base_v120_signal},
    "f23ob_f23_on_balance_volume_family_pvt_zscore_70d_base_v121_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_zscore_70d_base_v121_signal},
    "f23ob_f23_on_balance_volume_family_pvt_pctrank_180d_base_v122_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_pctrank_180d_base_v122_signal},
    "f23ob_f23_on_balance_volume_family_fi_short_long_ratio_base_v123_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_fi_short_long_ratio_base_v123_signal},
    "f23ob_f23_on_balance_volume_family_fi_arctan_z_30d_base_v124_signal": {"inputs": ["close", "volume"], "func": f23ob_f23_on_balance_volume_family_fi_arctan_z_30d_base_v124_signal},
    "f23ob_f23_on_balance_volume_family_kvo_ema_slope_42d_base_v125_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_kvo_ema_slope_42d_base_v125_signal},
    "f23ob_f23_on_balance_volume_family_kvo_signal_distance_base_v126_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_kvo_signal_distance_base_v126_signal},
    "f23ob_f23_on_balance_volume_family_chaikin_osc_pctrank_120d_base_v127_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_chaikin_osc_pctrank_120d_base_v127_signal},
    "f23ob_f23_on_balance_volume_family_nvi_pctrank_60d_base_v128_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_nvi_pctrank_60d_base_v128_signal},
    "f23ob_f23_on_balance_volume_family_pvi_pctrank_120d_base_v129_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvi_pctrank_120d_base_v129_signal},
    "f23ob_f23_on_balance_volume_family_nvi_zscore_90d_base_v130_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_nvi_zscore_90d_base_v130_signal},
    "f23ob_f23_on_balance_volume_family_obv_direction_entropy_50d_base_v131_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_direction_entropy_50d_base_v131_signal},
    "f23ob_f23_on_balance_volume_family_obv_signedlog_level_norm_base_v132_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_signedlog_level_norm_base_v132_signal},
    "f23ob_f23_on_balance_volume_family_adl_revrate_sma30_60d_base_v133_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_adl_revrate_sma30_60d_base_v133_signal},
    "f23ob_f23_on_balance_volume_family_pvt_ma_short_long_diff_base_v134_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_ma_short_long_diff_base_v134_signal},
    "f23ob_f23_on_balance_volume_family_pvt_tanh_slope_30d_base_v135_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_pvt_tanh_slope_30d_base_v135_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff_autocorr5_90d_base_v136_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff_autocorr5_90d_base_v136_signal},
    "f23ob_f23_on_balance_volume_family_obv_close_zscore_diff_45d_base_v137_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_close_zscore_diff_45d_base_v137_signal},
    "f23ob_f23_on_balance_volume_family_obv_uppct_60d_base_v138_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_uppct_60d_base_v138_signal},
    "f23ob_f23_on_balance_volume_family_obv_drawdown_120d_base_v139_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_drawdown_120d_base_v139_signal},
    "f23ob_f23_on_balance_volume_family_obv_diff_winsor_60d_base_v140_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_diff_winsor_60d_base_v140_signal},
    "f23ob_f23_on_balance_volume_family_obv_adl_pvt_sign_agreement_base_v141_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_adl_pvt_sign_agreement_base_v141_signal},
    "f23ob_f23_on_balance_volume_family_obv_iqr_60d_norm_base_v142_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_iqr_60d_norm_base_v142_signal},
    "f23ob_f23_on_balance_volume_family_close_lag_obv_corr_42d_base_v143_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_close_lag_obv_corr_42d_base_v143_signal},
    "f23ob_f23_on_balance_volume_family_obv_cv_30d_base_v144_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_cv_30d_base_v144_signal},
    "f23ob_f23_on_balance_volume_family_kvo_fracpos_40d_base_v145_signal": {"inputs": ["high", "low", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_kvo_fracpos_40d_base_v145_signal},
    "f23ob_f23_on_balance_volume_family_obvco_upvol_downvol_logratio_base_v146_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvco_upvol_downvol_logratio_base_v146_signal},
    "f23ob_f23_on_balance_volume_family_obvhl_streak_above_sma40_50d_base_v147_signal": {"inputs": ["high", "volume"], "func": f23ob_f23_on_balance_volume_family_obvhl_streak_above_sma40_50d_base_v147_signal},
    "f23ob_f23_on_balance_volume_family_daysince_pvt_sma50_70d_base_v148_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_daysince_pvt_sma50_70d_base_v148_signal},
    "f23ob_f23_on_balance_volume_family_obvdiff_closediff_corr_30d_base_v149_signal": {"inputs": ["closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obvdiff_closediff_corr_30d_base_v149_signal},
    "f23ob_f23_on_balance_volume_family_obv_co_ratio_120d_base_v150_signal": {"inputs": ["open", "closeadj", "volume"], "func": f23ob_f23_on_balance_volume_family_obv_co_ratio_120d_base_v150_signal},
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
    for name, entry in f23_on_balance_volume_family_base_076_150_REGISTRY.items():
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
