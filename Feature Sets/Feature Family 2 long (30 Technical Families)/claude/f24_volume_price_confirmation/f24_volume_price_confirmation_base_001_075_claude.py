"""f24_volume_price_confirmation base features 001-075.

Domain: features that quantify whether volume CONFIRMS price moves —
agreement/magnitude focus (distinct from f28 which emphasizes divergence,
f21 volume alone, f22 volume trend, f23 OBV, f25 VWAP, f26 A/D-CLV).

Confirmation = high volume on big price moves; unconfirmed = low volume on
big moves. Every feature explicitly couples |return| (or signed return)
with volume in some agreement form. NaN policy: only replace([inf,-inf],
nan) at the final return; never fillna(<value>). Windows > 21 use
closeadj; <=21 use close. Each function spells its formula inline.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Helpers (mean kernels + simple utilities used inside expanded formulas).
# Each feature still spells its own confirmation formula inline.
# ---------------------------------------------------------------------------


def _sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).mean()


def _ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False, min_periods=n).mean()


def _rstd(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n, min_periods=n).std()


def _zscore(s: pd.Series, n: int) -> pd.Series:
    m = s.rolling(n, min_periods=n).mean()
    sd = s.rolling(n, min_periods=n).std()
    return (s - m) / sd.replace(0.0, np.nan)


# ---------------------------------------------------------------------------
# Features 001-075
# ---------------------------------------------------------------------------


# === A. Magnitude product: vol * |return| in different forms =============


def f24vp_f24_volume_price_confirmation_volabsret_sma_15d_base_v001_signal(close, volume):
    """SMA(15, vol * |close.pct_change(1)|). Average daily price-volume energy."""
    r = close.pct_change(1).abs()
    energy = volume * r
    return energy.rolling(15, min_periods=15).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volabsret_logsum_30d_base_v002_signal(closeadj, volume):
    """log(sum(vol * |ret|, 30) / sum(vol, 30)). Volume-weighted |return|.
    Long-window confirmation-density measure."""
    r = closeadj.pct_change(1).abs()
    num = (volume * r).rolling(30, min_periods=30).sum()
    den = volume.rolling(30, min_periods=30).sum().replace(0.0, np.nan)
    return np.log(num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_logvol_absret_50d_base_v003_signal(closeadj, volume):
    """SMA(50, |ret| * log(vol/SMA(vol,50))). Excess-volume weighted return magnitude."""
    n = 50
    r = closeadj.pct_change(1).abs()
    vol_ratio = volume / volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    prod = r * np.log(vol_ratio)
    return prod.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volz_absret_25d_base_v004_signal(close, volume):
    """SMA(25, volume_z(63) * |close.pct_change(1)|).
    Standardized volume scaled by daily |return|."""
    vol_z = (volume - volume.rolling(63, min_periods=63).mean()) / volume.rolling(63, min_periods=63).std().replace(0.0, np.nan)
    r = close.pct_change(1).abs()
    return (vol_z * r).rolling(25, min_periods=25).mean().replace([np.inf, -np.inf], np.nan)


# === B. Top-decile big-move volume score ===================================


def f24vp_f24_volume_price_confirmation_topdec_volz_60d_base_v005_signal(closeadj, volume):
    """Mean vol-z on top-decile |return| days within trailing 60d.
    High = strong confirmation regime."""
    n = 60
    r = closeadj.pct_change(1).abs()
    vol_z = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    thresh = r.rolling(n, min_periods=n).quantile(0.9)
    mask = (r >= thresh).astype(float).where(~thresh.isna())
    num = (vol_z * mask).rolling(n, min_periods=n).sum()
    den = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_botdec_volz_60d_base_v006_signal(closeadj, volume):
    """Mean vol-z on bottom-decile |return| (quiet) days within trailing 60d.
    Low values = quiet days indeed have low volume (consistent regime)."""
    n = 60
    r = closeadj.pct_change(1).abs()
    vol_z = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    thresh = r.rolling(n, min_periods=n).quantile(0.1)
    mask = (r <= thresh).astype(float).where(~thresh.isna())
    num = (vol_z * mask).rolling(n, min_periods=n).sum()
    den = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_topbot_volz_diff_80d_base_v007_signal(closeadj, volume):
    """topdec(volz | big-move) - botdec(volz | quiet) over 80d window.
    Direct confirmation strength: bigger = clearer agreement."""
    n = 80
    r = closeadj.pct_change(1).abs()
    vol_z = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    hi = r.rolling(n, min_periods=n).quantile(0.9)
    lo = r.rolling(n, min_periods=n).quantile(0.1)
    hi_mask = (r >= hi).astype(float).where(~hi.isna())
    lo_mask = (r <= lo).astype(float).where(~lo.isna())
    hi_avg = (vol_z * hi_mask).rolling(n, min_periods=n).sum() / hi_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    lo_avg = (vol_z * lo_mask).rolling(n, min_periods=n).sum() / lo_mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (hi_avg - lo_avg).replace([np.inf, -np.inf], np.nan)


# === C. Signed-flow / cumulative directional volume ========================


def f24vp_f24_volume_price_confirmation_signed_vol_sum_20d_base_v008_signal(close, volume):
    """sum(sign(ret) * vol, 20). Net volume in direction of price."""
    s = np.sign(close.pct_change(1))
    return (s * volume).rolling(20, min_periods=20).sum().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signed_vol_ratio_50d_base_v009_signal(closeadj, volume):
    """sum(sign(ret) * vol, 50) / sum(vol, 50). Normalized net directional flow."""
    n = 50
    s = np.sign(closeadj.pct_change(1))
    num = (s * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_money_flow_30d_base_v010_signal(closeadj, volume):
    """SMA(30, ret * vol). Average daily signed dollar-energy."""
    r = closeadj.pct_change(1)
    return (r * volume).rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_money_flow_120d_base_v011_signal(closeadj, volume):
    """SMA(120, ret * vol). Long-window signed dollar flow."""
    r = closeadj.pct_change(1)
    return (r * volume).rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vwret_15d_base_v012_signal(close, volume):
    """Volume-weighted return over 15d: sum(ret * vol) / sum(vol). Effective signed
    direction with volume confidence."""
    n = 15
    r = close.pct_change(1)
    num = (r * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vwret_100d_base_v013_signal(closeadj, volume):
    """Volume-weighted return over 100d."""
    n = 100
    r = closeadj.pct_change(1)
    num = (r * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


# === D. Up-vs-down volume balance (Granville-style) ========================


def f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_30d_base_v014_signal(closeadj, volume):
    """log( sum(vol|up,30) / sum(vol|dn,30) ). Up/down volume balance."""
    n = 30
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    su = up.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sd = dn.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(su / sd).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_updn_vol_balance_15d_base_v015_signal(close, volume):
    """(sum(vol|up) - sum(vol|dn)) / total vol over 15d."""
    n = 15
    r = close.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    su = up.rolling(n, min_periods=n).sum()
    sd = dn.rolling(n, min_periods=n).sum()
    tot = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return ((su - sd) / tot).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_updn_vol_balance_80d_base_v016_signal(closeadj, volume):
    """(up - dn) / total over 80d. Mid/long-window participation balance."""
    n = 80
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    su = up.rolling(n, min_periods=n).sum()
    sd = dn.rolling(n, min_periods=n).sum()
    tot = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return ((su - sd) / tot).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_180d_base_v017_signal(closeadj, volume):
    """log(up/dn) over 180d. Very long-window participation skew."""
    n = 180
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    su = up.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sd = dn.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(su / sd).replace([np.inf, -np.inf], np.nan)


# === E. Discrete: big/small move x big/small vol counts ====================


def f24vp_f24_volume_price_confirmation_count_bigmove_bigvol_60d_base_v018_signal(closeadj, volume):
    """Count of days within 60d where |ret| > median(|ret|,60) AND vol > median(vol,60).
    Concordant days. Discrete output decorrelates from continuous flow features."""
    n = 60
    r = closeadj.pct_change(1).abs()
    r_med = r.rolling(n, min_periods=n).median()
    v_med = volume.rolling(n, min_periods=n).median()
    cond = ((r > r_med) & (volume > v_med)).astype(float).where(~r_med.isna() & ~v_med.isna())
    return cond.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_count_bigmove_smallvol_60d_base_v019_signal(closeadj, volume):
    """Count of UNCONFIRMED days within 60d: |ret| > median but vol <= median."""
    n = 60
    r = closeadj.pct_change(1).abs()
    r_med = r.rolling(n, min_periods=n).median()
    v_med = volume.rolling(n, min_periods=n).median()
    cond = ((r > r_med) & (volume <= v_med)).astype(float).where(~r_med.isna() & ~v_med.isna())
    return cond.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_confirm_streak_50d_base_v020_signal(closeadj, volume):
    """Days since last NON-confirmed day in 50d (|ret| > median AND vol > median = OK
    else streak resets). Bounded by 50."""
    n = 50
    r = closeadj.pct_change(1).abs()
    r_med = r.rolling(n, min_periods=n).median()
    v_med = volume.rolling(n, min_periods=n).median()
    bad = ((r > r_med) & (volume <= v_med)).astype(float).where(~r_med.isna() & ~v_med.isna())

    def _f(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return bad.rolling(n, min_periods=n).apply(_f, raw=True).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_confirm_xor_sign_30d_base_v021_signal(close, volume):
    """SMA(30, sign(vol.pct_change(5)) * sign(close.pct_change(5))).
    +1 when vol expansion meets price expansion (or both contraction)."""
    sv = np.sign(volume.pct_change(5))
    sp = np.sign(close.pct_change(5))
    return (sv * sp).rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_confirm_xor_sign_120d_base_v022_signal(closeadj, volume):
    """SMA(120, sign(vol.pct_change(10)) * sign(close.pct_change(10))). Long-window."""
    sv = np.sign(volume.pct_change(10))
    sp = np.sign(closeadj.pct_change(10))
    return (sv * sp).rolling(120, min_periods=120).mean().replace([np.inf, -np.inf], np.nan)


# === F. Rolling correlation of |return| with volume (confirmation regime) ==


def f24vp_f24_volume_price_confirmation_corr_absret_vol_45d_base_v023_signal(closeadj, volume):
    """Rolling Pearson corr(|ret|, vol, 45). High = strong confirmation regime."""
    n = 45
    r = closeadj.pct_change(1).abs()
    return r.rolling(n, min_periods=n).corr(volume).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_absret_logvol_120d_base_v024_signal(closeadj, volume):
    """Rolling Pearson corr(|ret|, log(vol), 120). Long-window confirmation regime."""
    n = 120
    r = closeadj.pct_change(1).abs()
    return r.rolling(n, min_periods=n).corr(np.log(volume.replace(0.0, np.nan))).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_signret_vol_60d_base_v025_signal(closeadj, volume):
    """Rolling corr(sign(ret), vol, 60). Directional confirmation."""
    n = 60
    s = np.sign(closeadj.pct_change(1))
    return s.rolling(n, min_periods=n).corr(volume).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_spearman_absret_vol_70d_base_v026_signal(closeadj, volume):
    """Spearman rank corr of |ret| & vol over 70d. Robust nonlinear confirmation."""
    n = 70
    r = closeadj.pct_change(1).abs()
    rk_r = r.rolling(n, min_periods=n).apply(lambda x: float(pd.Series(x).rank().iloc[-1]), raw=False)
    rk_v = volume.rolling(n, min_periods=n).apply(lambda x: float(pd.Series(x).rank().iloc[-1]), raw=False)
    # Build Spearman via Pearson on ranks computed in rolling windows
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    r_vals = r.values; v_vals = volume.values
    for i in range(n - 1, len(closeadj)):
        rs = r_vals[i - n + 1:i + 1]
        vs = v_vals[i - n + 1:i + 1]
        if np.any(~np.isfinite(rs)) or np.any(~np.isfinite(vs)):
            continue
        rr = pd.Series(rs).rank().values
        rv = pd.Series(vs).rank().values
        sd_rr = rr.std(); sd_rv = rv.std()
        if sd_rr == 0.0 or sd_rv == 0.0:
            continue
        out.iat[i] = float(np.corrcoef(rr, rv)[0, 1])
    # neutralize unused vars
    _ = rk_r; _ = rk_v
    return out.replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_absret_vol_lag1_45d_base_v027_signal(closeadj, volume):
    """corr(|ret|, vol.shift(1), 45). Lagged volume confirmation (does prior-day volume
    predict next-day move magnitude?)."""
    n = 45
    r = closeadj.pct_change(1).abs()
    return r.rolling(n, min_periods=n).corr(volume.shift(1)).replace([np.inf, -np.inf], np.nan)


# === G. Vol-return product statistical moments =============================


def f24vp_f24_volume_price_confirmation_volret_prod_std_40d_base_v028_signal(closeadj, volume):
    """std of (ret * vol) over 40d. Dispersion of signed dollar flow."""
    n = 40
    p = closeadj.pct_change(1) * volume
    return p.rolling(n, min_periods=n).std().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volret_prod_skew_75d_base_v029_signal(closeadj, volume):
    """skew of (ret * vol) over 75d. Asymmetric signed flow (positive = right-skew)."""
    n = 75
    p = closeadj.pct_change(1) * volume
    return p.rolling(n, min_periods=n).skew().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volret_prod_kurt_100d_base_v030_signal(closeadj, volume):
    """kurtosis of (ret * vol) over 100d. Tail-fatness of dollar-flow."""
    n = 100
    p = closeadj.pct_change(1) * volume
    return p.rolling(n, min_periods=n).kurt().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volret_prod_max_25d_base_v031_signal(close, volume):
    """log(max |ret*vol| over 25d / median |ret*vol| over 25d). Extreme flow event ratio."""
    n = 25
    p = (close.pct_change(1) * volume).abs()
    mx = p.rolling(n, min_periods=n).max()
    md = p.rolling(n, min_periods=n).median().replace(0.0, np.nan)
    return np.log(mx / md).replace([np.inf, -np.inf], np.nan)


# === H. Cumulative dollar-energy and total-confirmation ====================


def f24vp_f24_volume_price_confirmation_cum_absret_vol_50d_base_v032_signal(closeadj, volume):
    """log(sum(|ret|*vol, 50)). Total dollar-energy expended over window."""
    n = 50
    e = closeadj.pct_change(1).abs() * volume
    return np.log(e.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_log_cumret_x_cumvol_60d_base_v033_signal(closeadj, volume):
    """log(|cum_return(60)|) * log(sum(vol,60)). Magnitude * participation product."""
    n = 60
    cret = (closeadj / closeadj.shift(n)) - 1.0
    cvol = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (np.log(cret.abs().replace(0.0, np.nan)) * np.log(cvol)).replace([np.inf, -np.inf], np.nan)


# === I. Beta of volume on |return| (regression slope) =====================


def f24vp_f24_volume_price_confirmation_beta_vol_on_absret_50d_base_v034_signal(closeadj, volume):
    """Rolling regression slope of vol on |ret| over 50d. Sensitivity of vol to mag."""
    n = 50
    r = closeadj.pct_change(1).abs()
    cov = r.rolling(n, min_periods=n).cov(volume)
    var = r.rolling(n, min_periods=n).var().replace(0.0, np.nan)
    return (cov / var).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_beta_logvol_on_signret_70d_base_v035_signal(closeadj, volume):
    """Rolling slope of log(vol) on SIGNED ret over 70d. Directional (not |.|) — uses
    a different signal axis from v034 (which uses |ret|)."""
    n = 70
    r = closeadj.pct_change(1)
    lv = np.log(volume.replace(0.0, np.nan))
    cov = r.rolling(n, min_periods=n).cov(lv)
    var = r.rolling(n, min_periods=n).var().replace(0.0, np.nan)
    return (cov / var).replace([np.inf, -np.inf], np.nan)


# === J. Bounded transforms (arctan/tanh) on raw confirmation scores ========


def f24vp_f24_volume_price_confirmation_arctan_corr_volz_signret_40d_base_v036_signal(close, volume):
    """arctan(rolling_corr(vol_z(40), sign(ret), 40)). Bounded confirmation."""
    n = 40
    vol_z = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    s = np.sign(close.pct_change(1))
    c = vol_z.rolling(n, min_periods=n).corr(s)
    return np.arctan(c).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_tanh_vwret_norm_60d_base_v037_signal(closeadj, volume):
    """tanh( vwret(60) / std(ret,60) ). Bounded volume-weighted return."""
    n = 60
    r = closeadj.pct_change(1)
    vw = (r * volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sd = r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return np.tanh(vw / sd).replace([np.inf, -np.inf], np.nan)


# === K. EMA-style smoothing of confirmation ===============================


def f24vp_f24_volume_price_confirmation_ema_volabsret_20d_base_v038_signal(close, volume):
    """EMA(20, vol * |ret|). Exponentially smoothed daily energy."""
    e = volume * close.pct_change(1).abs()
    return e.ewm(span=20, adjust=False, min_periods=20).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_ema_signed_vol_80d_base_v039_signal(closeadj, volume):
    """EMA(80, sign(ret) * vol). Smoothed net directional flow."""
    s = np.sign(closeadj.pct_change(1))
    return (s * volume).ewm(span=80, adjust=False, min_periods=80).mean().replace([np.inf, -np.inf], np.nan)


# === L. Volume thrust (Granville-style net thrust) ========================


def f24vp_f24_volume_price_confirmation_thrust_updn_25d_base_v040_signal(close, volume):
    """sum( (vol|up) - (vol|dn), 25). Raw thrust in dollar-share units."""
    n = 25
    r = close.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    return (up - dn).rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_thrust_updn_log_100d_base_v041_signal(closeadj, volume):
    """log( (1 + sum(up,100)) / (1 + sum(dn,100)) ) — long-window log thrust."""
    n = 100
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    su = up.rolling(n, min_periods=n).sum()
    sd = dn.rolling(n, min_periods=n).sum()
    return np.log((1.0 + su) / (1.0 + sd)).replace([np.inf, -np.inf], np.nan)


# === M. Volume-weighted realized vol (vol expansion under participation) ===


def f24vp_f24_volume_price_confirmation_vw_real_vol_45d_base_v042_signal(close, volume):
    """sqrt( sum(vol*ret^2,45)/sum(vol,45) ). Volume-weighted realized vol."""
    n = 45
    r = close.pct_change(1)
    num = (volume * r * r).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.sqrt(num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vw_real_vol_diff_logstd_60d_base_v043_signal(closeadj, volume):
    """log(VW-realized-vol(60) / std(ret,60)). >0 => big moves on big volume."""
    n = 60
    r = closeadj.pct_change(1)
    num = (volume * r * r).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    vw_sd = np.sqrt(num / den)
    raw_sd = r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return np.log(vw_sd / raw_sd).replace([np.inf, -np.inf], np.nan)


# === N. Confirmation indicator (OBV-slope aligned with price-slope) ========


def f24vp_f24_volume_price_confirmation_obv_priceslope_align_30d_base_v044_signal(closeadj, volume):
    """SMA(30, sign(OBV.diff(5)) * sign(close.diff(5))). OBV-price slope alignment.
    Not OBV itself — explicitly an alignment ratio over time."""
    s = np.sign(closeadj.diff(1))
    obv = (s * volume).cumsum()
    return (np.sign(obv.diff(5)) * np.sign(closeadj.diff(5))).rolling(30, min_periods=30).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_obv_priceslope_align_150d_base_v045_signal(closeadj, volume):
    """Long-window OBV-price slope alignment fraction over 150d."""
    s = np.sign(closeadj.diff(1))
    obv = (s * volume).cumsum()
    return (np.sign(obv.diff(21)) * np.sign(closeadj.diff(21))).rolling(150, min_periods=150).mean().replace([np.inf, -np.inf], np.nan)


# === O. Vol-of-vol-weighted returns =======================================


def f24vp_f24_volume_price_confirmation_vol_of_vwret_50d_base_v046_signal(closeadj, volume):
    """std over 50d of vw_ret_5d series — vol of recent VW return windows."""
    n = 50
    r = closeadj.pct_change(1)
    # vw_ret over rolling 5d window for each t
    vw5 = (r * volume).rolling(5, min_periods=5).sum() / volume.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    return vw5.rolling(n, min_periods=n).std().replace([np.inf, -np.inf], np.nan)


# === P. Rank/percentile of confirmation scores ============================


def f24vp_f24_volume_price_confirmation_rank_volabsret_60d_base_v047_signal(close, volume):
    """Percent rank of today's vol*|ret| within trailing 60d."""
    n = 60
    e = volume * close.pct_change(1).abs()
    return e.rolling(n, min_periods=n).apply(lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, len(x) - 1)), raw=True).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_rank_signed_volflow_120d_base_v048_signal(closeadj, volume):
    """Percent rank of today's signed-vol-flow (sum signed vol over 20d) within 120d."""
    n = 120
    s = np.sign(closeadj.pct_change(1))
    sv = (s * volume).rolling(20, min_periods=20).sum()
    return sv.rolling(n, min_periods=n).apply(lambda x: float((np.sum(x <= x[-1]) - 1) / max(1, len(x) - 1)), raw=True).replace([np.inf, -np.inf], np.nan)


# === Q. Cross-frequency confirmation differentials =========================


def f24vp_f24_volume_price_confirmation_short_minus_long_vwret_base_v049_signal(closeadj, volume):
    """vw_ret(10) - vw_ret(60). Short-horizon directional flow minus long-horizon."""
    r = closeadj.pct_change(1)
    s = (r * volume).rolling(10, min_periods=10).sum() / volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    l = (r * volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (s - l).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_short_minus_long_corr_base_v050_signal(closeadj, volume):
    """corr(|ret|,vol,20) - corr(|ret|,vol,150). Confirmation-regime momentum."""
    r = closeadj.pct_change(1).abs()
    cs = r.rolling(20, min_periods=20).corr(volume)
    cl = r.rolling(150, min_periods=150).corr(volume)
    return (cs - cl).replace([np.inf, -np.inf], np.nan)


# === R. ATR-vol agreement (confirmed expansion) ============================


def f24vp_f24_volume_price_confirmation_atr_vol_agree_50d_base_v051_signal(closeadj, volume, high, low):
    """vol_z(50) * sign(ATR(14).diff(10)) — confirmed expansion: +1 if both vol & range up."""
    n = 50
    tr = pd.concat([(high - low).abs(),
                    (high - closeadj.shift(1)).abs(),
                    (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    vol_z = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (vol_z * np.sign(atr.diff(10))).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_atr_vol_corr_80d_base_v052_signal(closeadj, volume, high, low):
    """corr(ATR(14), vol, 80). Are range and volume co-moving?"""
    n = 80
    tr = pd.concat([(high - low).abs(),
                    (high - closeadj.shift(1)).abs(),
                    (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    atr = tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()
    return atr.rolling(n, min_periods=n).corr(volume).replace([np.inf, -np.inf], np.nan)


# === S. Discrete: sign of dollar flow ======================================


def f24vp_f24_volume_price_confirmation_sign_money_flow_30d_base_v053_signal(close, volume):
    """sign of sum(ret*vol, 30). Discrete net dollar flow direction."""
    r = close.pct_change(1)
    return np.sign((r * volume).rolling(30, min_periods=30).sum()).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sign_thrust_80d_base_v054_signal(closeadj, volume):
    """sign of sum( (up-dn), 80 ). Long-window thrust direction (discrete)."""
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    return np.sign((up - dn).rolling(80, min_periods=80).sum()).replace([np.inf, -np.inf], np.nan)


# === T. Concordance count weighted by magnitude ============================


def f24vp_f24_volume_price_confirmation_concordance_weighted_40d_base_v055_signal(closeadj, volume):
    """SMA(40, sign( |ret| - median|ret|,40 ) * sign( vol - median(vol),40 )).
    +1 when |ret| and vol both above or both below their medians."""
    n = 40
    r = closeadj.pct_change(1).abs()
    r_med = r.rolling(n, min_periods=n).median()
    v_med = volume.rolling(n, min_periods=n).median()
    c = np.sign(r - r_med) * np.sign(volume - v_med)
    return c.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_concordance_weighted_180d_base_v056_signal(closeadj, volume):
    """Long-window concordance. SMA(180)."""
    n = 180
    r = closeadj.pct_change(1).abs()
    r_med = r.rolling(n, min_periods=n).median()
    v_med = volume.rolling(n, min_periods=n).median()
    c = np.sign(r - r_med) * np.sign(volume - v_med)
    return c.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === U. Big-move volume excess (decile-based magnitude) ===================


def f24vp_f24_volume_price_confirmation_bigmove_vol_excess_60d_base_v057_signal(closeadj, volume):
    """log(avg_vol_on_top10%_|ret|_days(60) / avg_vol_overall(60))."""
    n = 60
    r = closeadj.pct_change(1).abs()
    th = r.rolling(n, min_periods=n).quantile(0.9)
    mask = (r >= th).astype(float).where(~th.isna())
    num = (volume * mask).rolling(n, min_periods=n).sum() / mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    den = volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return np.log(num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_quietmove_vol_deficit_60d_base_v058_signal(closeadj, volume):
    """log(avg_vol_on_bottom10%_|ret|_days(60) / avg_vol_overall(60))."""
    n = 60
    r = closeadj.pct_change(1).abs()
    th = r.rolling(n, min_periods=n).quantile(0.1)
    mask = (r <= th).astype(float).where(~th.isna())
    num = (volume * mask).rolling(n, min_periods=n).sum() / mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    den = volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return np.log(num / den).replace([np.inf, -np.inf], np.nan)


# === V. Volume / |return| efficiency (inverse of confirmation) =============


def f24vp_f24_volume_price_confirmation_unconfirmed_count_streak_30d_base_v059_signal(close, volume):
    """Count of days within 30d where vol > q70 but |ret| <= q40 (volume churn no
    price progress — unconfirmed congestion)."""
    n = 30
    r = close.pct_change(1).abs()
    v_q = volume.rolling(n, min_periods=n).quantile(0.7)
    r_q = r.rolling(n, min_periods=n).quantile(0.4)
    cond = ((volume > v_q) & (r <= r_q)).astype(float).where(~v_q.isna() & ~r_q.isna())
    return cond.rolling(n, min_periods=n).sum().replace([np.inf, -np.inf], np.nan)


# === W. Days-since last big-vol big-move confirmed event ==================


def f24vp_f24_volume_price_confirmation_daysince_confirmed_120d_base_v060_signal(closeadj, volume):
    """Days since last day with vol > q80 AND |ret| > q80 over trailing 120d."""
    n = 120
    r = closeadj.pct_change(1).abs()
    vq = volume.rolling(n, min_periods=n).quantile(0.8)
    rq = r.rolling(n, min_periods=n).quantile(0.8)
    flag = ((volume > vq) & (r > rq)).astype(float).where(~vq.isna() & ~rq.isna())

    def _f(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(n, min_periods=n).apply(_f, raw=True).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_daysince_unconfirmed_60d_base_v061_signal(closeadj, volume):
    """Days since last day with |ret| > q80 AND vol < q40 (unconfirmed move) over 60d."""
    n = 60
    r = closeadj.pct_change(1).abs()
    vq = volume.rolling(n, min_periods=n).quantile(0.4)
    rq = r.rolling(n, min_periods=n).quantile(0.8)
    flag = ((volume < vq) & (r > rq)).astype(float).where(~vq.isna() & ~rq.isna())

    def _f(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0:
            return float(len(x))
        return float(len(x) - 1 - idx[-1])
    return flag.rolling(n, min_periods=n).apply(_f, raw=True).replace([np.inf, -np.inf], np.nan)


# === X. OHLC-leveraged confirmation ========================================


def f24vp_f24_volume_price_confirmation_range_vol_corr_50d_base_v062_signal(close, volume, high, low):
    """corr( (high-low)/close, vol, 50 ). Daily range vs volume."""
    n = 50
    rng = (high - low) / close.replace(0.0, np.nan)
    return rng.rolling(n, min_periods=n).corr(volume).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_body_vol_corr_60d_base_v063_signal(closeadj, volume, open):
    """corr( |close-open|/close, vol, 60 ). Body size vs volume — directional bar agreement."""
    n = 60
    body = (closeadj - open).abs() / closeadj.replace(0.0, np.nan)
    return body.rolling(n, min_periods=n).corr(volume).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signed_body_x_vol_30d_base_v064_signal(close, volume, open):
    """SMA(30, sign(close-open) * vol). Net intraday directional flow."""
    n = 30
    return (np.sign(close - open) * volume).rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === Y. Volume z-score on signed-return days only =========================


def f24vp_f24_volume_price_confirmation_volz_up_mean_50d_base_v065_signal(closeadj, volume):
    """Mean of vol_z(50) on up-days within trailing 50d."""
    n = 50
    vol_z = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    mask = (closeadj.pct_change(1) > 0.0).astype(float).where(~vol_z.isna())
    num = (vol_z * mask).rolling(n, min_periods=n).sum()
    den = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volz_dn_mean_50d_base_v066_signal(closeadj, volume):
    """Mean of vol_z(50) on down-days within trailing 50d."""
    n = 50
    vol_z = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    mask = (closeadj.pct_change(1) < 0.0).astype(float).where(~vol_z.isna())
    num = (vol_z * mask).rolling(n, min_periods=n).sum()
    den = mask.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volz_up_minus_dn_180d_base_v067_signal(closeadj, volume):
    """volz_up_mean(180) - volz_dn_mean(180). Up-bias of volume excess."""
    n = 180
    vol_z = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    up = (closeadj.pct_change(1) > 0.0).astype(float).where(~vol_z.isna())
    dn = (closeadj.pct_change(1) < 0.0).astype(float).where(~vol_z.isna())
    up_mean = (vol_z * up).rolling(n, min_periods=n).sum() / up.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    dn_mean = (vol_z * dn).rolling(n, min_periods=n).sum() / dn.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (up_mean - dn_mean).replace([np.inf, -np.inf], np.nan)


# === Z. Confirmation regime persistence ===================================


def f24vp_f24_volume_price_confirmation_corr_change_regime_60d_base_v068_signal(closeadj, volume):
    """corr(|ret|,vol,30).diff(20). Change in confirmation regime intensity."""
    r = closeadj.pct_change(1).abs()
    c = r.rolling(30, min_periods=30).corr(volume)
    return c.diff(20).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_concordance_persistence_100d_base_v069_signal(closeadj, volume):
    """std over 100d of concordance(40) — regime persistence (low = stable confirmation)."""
    n = 40
    r = closeadj.pct_change(1).abs()
    r_med = r.rolling(n, min_periods=n).median()
    v_med = volume.rolling(n, min_periods=n).median()
    c = (np.sign(r - r_med) * np.sign(volume - v_med)).rolling(n, min_periods=n).mean()
    return c.rolling(100, min_periods=100).std().replace([np.inf, -np.inf], np.nan)


# === AA. Beta of (vol pct-change) on (ret) ================================


def f24vp_f24_volume_price_confirmation_beta_volpct_on_ret_40d_base_v070_signal(close, volume):
    """slope of vol.pct_change on close.pct_change over 40d."""
    n = 40
    x = close.pct_change(1)
    y = volume.pct_change(1)
    cov = x.rolling(n, min_periods=n).cov(y)
    var = x.rolling(n, min_periods=n).var().replace(0.0, np.nan)
    return (cov / var).replace([np.inf, -np.inf], np.nan)


# === AB. Volume thrust slope ==============================================


def f24vp_f24_volume_price_confirmation_thrust_slope_140d_base_v071_signal(closeadj, volume):
    """( thrust(30) - thrust(30).shift(63) ) / 63. Long-window thrust slope.
    Thrust uses cross-window confirmation construction."""
    n = 30
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0)
    dn = volume.where(r < 0.0, 0.0)
    th = (up - dn).rolling(n, min_periods=n).sum()
    return ((th - th.shift(63)) / 63.0).replace([np.inf, -np.inf], np.nan)


# === AC. Vol-weighted return autocorrelation ==============================


def f24vp_f24_volume_price_confirmation_vwret_autocorr_60d_base_v072_signal(closeadj, volume):
    """corr( vw_ret_5d(t), vw_ret_5d(t-5), 60 ). Persistence of vw-flow direction."""
    n = 60
    r = closeadj.pct_change(1)
    vw5 = (r * volume).rolling(5, min_periods=5).sum() / volume.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    return vw5.rolling(n, min_periods=n).corr(vw5.shift(5)).replace([np.inf, -np.inf], np.nan)


# === AD. Vol expansion AND price expansion conjunction ====================


def f24vp_f24_volume_price_confirmation_dual_expansion_count_50d_base_v073_signal(closeadj, volume):
    """Fraction of days within 50d where vol > SMA(vol,50) AND |ret| > SMA(|ret|,50)."""
    n = 50
    r = closeadj.pct_change(1).abs()
    cond = ((volume > volume.rolling(n, min_periods=n).mean()) & (r > r.rolling(n, min_periods=n).mean())).astype(float).where(~volume.rolling(n, min_periods=n).mean().isna())
    return cond.rolling(n, min_periods=n).mean().replace([np.inf, -np.inf], np.nan)


# === AE. Sigmoid of normalized concordance score ==========================


def f24vp_f24_volume_price_confirmation_sigmoid_concordance_60d_base_v074_signal(closeadj, volume):
    """sigmoid( 3 * SMA(60, sign(|ret|-med)*sign(vol-med)) ). Bounded smooth concord."""
    n = 60
    r = closeadj.pct_change(1).abs()
    r_med = r.rolling(n, min_periods=n).median()
    v_med = volume.rolling(n, min_periods=n).median()
    c = (np.sign(r - r_med) * np.sign(volume - v_med)).rolling(n, min_periods=n).mean()
    out = 1.0 / (1.0 + np.exp(-3.0 * c))
    return out.replace([np.inf, -np.inf], np.nan)


# === AF. Total participation index =========================================


def f24vp_f24_volume_price_confirmation_log_total_dollar_energy_40d_base_v075_signal(close, volume, high, low):
    """log( sum( vol * (high-low), 40 ) ). Total participation-x-range energy."""
    n = 40
    e = volume * (high - low)
    return np.log(e.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------


f24_volume_price_confirmation_base_001_075_REGISTRY = {
    "f24vp_f24_volume_price_confirmation_volabsret_sma_15d_base_v001_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_volabsret_sma_15d_base_v001_signal},
    "f24vp_f24_volume_price_confirmation_volabsret_logsum_30d_base_v002_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volabsret_logsum_30d_base_v002_signal},
    "f24vp_f24_volume_price_confirmation_logvol_absret_50d_base_v003_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_logvol_absret_50d_base_v003_signal},
    "f24vp_f24_volume_price_confirmation_volz_absret_25d_base_v004_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_volz_absret_25d_base_v004_signal},
    "f24vp_f24_volume_price_confirmation_topdec_volz_60d_base_v005_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_topdec_volz_60d_base_v005_signal},
    "f24vp_f24_volume_price_confirmation_botdec_volz_60d_base_v006_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_botdec_volz_60d_base_v006_signal},
    "f24vp_f24_volume_price_confirmation_topbot_volz_diff_80d_base_v007_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_topbot_volz_diff_80d_base_v007_signal},
    "f24vp_f24_volume_price_confirmation_signed_vol_sum_20d_base_v008_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_signed_vol_sum_20d_base_v008_signal},
    "f24vp_f24_volume_price_confirmation_signed_vol_ratio_50d_base_v009_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_signed_vol_ratio_50d_base_v009_signal},
    "f24vp_f24_volume_price_confirmation_money_flow_30d_base_v010_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_money_flow_30d_base_v010_signal},
    "f24vp_f24_volume_price_confirmation_money_flow_120d_base_v011_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_money_flow_120d_base_v011_signal},
    "f24vp_f24_volume_price_confirmation_vwret_15d_base_v012_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_vwret_15d_base_v012_signal},
    "f24vp_f24_volume_price_confirmation_vwret_100d_base_v013_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vwret_100d_base_v013_signal},
    "f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_30d_base_v014_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_30d_base_v014_signal},
    "f24vp_f24_volume_price_confirmation_updn_vol_balance_15d_base_v015_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_updn_vol_balance_15d_base_v015_signal},
    "f24vp_f24_volume_price_confirmation_updn_vol_balance_80d_base_v016_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_updn_vol_balance_80d_base_v016_signal},
    "f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_180d_base_v017_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_180d_base_v017_signal},
    "f24vp_f24_volume_price_confirmation_count_bigmove_bigvol_60d_base_v018_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_count_bigmove_bigvol_60d_base_v018_signal},
    "f24vp_f24_volume_price_confirmation_count_bigmove_smallvol_60d_base_v019_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_count_bigmove_smallvol_60d_base_v019_signal},
    "f24vp_f24_volume_price_confirmation_confirm_streak_50d_base_v020_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_confirm_streak_50d_base_v020_signal},
    "f24vp_f24_volume_price_confirmation_confirm_xor_sign_30d_base_v021_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_confirm_xor_sign_30d_base_v021_signal},
    "f24vp_f24_volume_price_confirmation_confirm_xor_sign_120d_base_v022_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_confirm_xor_sign_120d_base_v022_signal},
    "f24vp_f24_volume_price_confirmation_corr_absret_vol_45d_base_v023_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_corr_absret_vol_45d_base_v023_signal},
    "f24vp_f24_volume_price_confirmation_corr_absret_logvol_120d_base_v024_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_corr_absret_logvol_120d_base_v024_signal},
    "f24vp_f24_volume_price_confirmation_corr_signret_vol_60d_base_v025_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_corr_signret_vol_60d_base_v025_signal},
    "f24vp_f24_volume_price_confirmation_spearman_absret_vol_70d_base_v026_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_spearman_absret_vol_70d_base_v026_signal},
    "f24vp_f24_volume_price_confirmation_corr_absret_vol_lag1_45d_base_v027_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_corr_absret_vol_lag1_45d_base_v027_signal},
    "f24vp_f24_volume_price_confirmation_volret_prod_std_40d_base_v028_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volret_prod_std_40d_base_v028_signal},
    "f24vp_f24_volume_price_confirmation_volret_prod_skew_75d_base_v029_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volret_prod_skew_75d_base_v029_signal},
    "f24vp_f24_volume_price_confirmation_volret_prod_kurt_100d_base_v030_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volret_prod_kurt_100d_base_v030_signal},
    "f24vp_f24_volume_price_confirmation_volret_prod_max_25d_base_v031_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_volret_prod_max_25d_base_v031_signal},
    "f24vp_f24_volume_price_confirmation_cum_absret_vol_50d_base_v032_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_cum_absret_vol_50d_base_v032_signal},
    "f24vp_f24_volume_price_confirmation_log_cumret_x_cumvol_60d_base_v033_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_log_cumret_x_cumvol_60d_base_v033_signal},
    "f24vp_f24_volume_price_confirmation_beta_vol_on_absret_50d_base_v034_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_beta_vol_on_absret_50d_base_v034_signal},
    "f24vp_f24_volume_price_confirmation_beta_logvol_on_signret_70d_base_v035_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_beta_logvol_on_signret_70d_base_v035_signal},
    "f24vp_f24_volume_price_confirmation_arctan_corr_volz_signret_40d_base_v036_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_arctan_corr_volz_signret_40d_base_v036_signal},
    "f24vp_f24_volume_price_confirmation_tanh_vwret_norm_60d_base_v037_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_tanh_vwret_norm_60d_base_v037_signal},
    "f24vp_f24_volume_price_confirmation_ema_volabsret_20d_base_v038_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_ema_volabsret_20d_base_v038_signal},
    "f24vp_f24_volume_price_confirmation_ema_signed_vol_80d_base_v039_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_ema_signed_vol_80d_base_v039_signal},
    "f24vp_f24_volume_price_confirmation_thrust_updn_25d_base_v040_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_thrust_updn_25d_base_v040_signal},
    "f24vp_f24_volume_price_confirmation_thrust_updn_log_100d_base_v041_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_thrust_updn_log_100d_base_v041_signal},
    "f24vp_f24_volume_price_confirmation_vw_real_vol_45d_base_v042_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_vw_real_vol_45d_base_v042_signal},
    "f24vp_f24_volume_price_confirmation_vw_real_vol_diff_logstd_60d_base_v043_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vw_real_vol_diff_logstd_60d_base_v043_signal},
    "f24vp_f24_volume_price_confirmation_obv_priceslope_align_30d_base_v044_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_obv_priceslope_align_30d_base_v044_signal},
    "f24vp_f24_volume_price_confirmation_obv_priceslope_align_150d_base_v045_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_obv_priceslope_align_150d_base_v045_signal},
    "f24vp_f24_volume_price_confirmation_vol_of_vwret_50d_base_v046_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vol_of_vwret_50d_base_v046_signal},
    "f24vp_f24_volume_price_confirmation_rank_volabsret_60d_base_v047_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_rank_volabsret_60d_base_v047_signal},
    "f24vp_f24_volume_price_confirmation_rank_signed_volflow_120d_base_v048_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_rank_signed_volflow_120d_base_v048_signal},
    "f24vp_f24_volume_price_confirmation_short_minus_long_vwret_base_v049_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_short_minus_long_vwret_base_v049_signal},
    "f24vp_f24_volume_price_confirmation_short_minus_long_corr_base_v050_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_short_minus_long_corr_base_v050_signal},
    "f24vp_f24_volume_price_confirmation_atr_vol_agree_50d_base_v051_signal": {"inputs": ["closeadj", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_atr_vol_agree_50d_base_v051_signal},
    "f24vp_f24_volume_price_confirmation_atr_vol_corr_80d_base_v052_signal": {"inputs": ["closeadj", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_atr_vol_corr_80d_base_v052_signal},
    "f24vp_f24_volume_price_confirmation_sign_money_flow_30d_base_v053_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_sign_money_flow_30d_base_v053_signal},
    "f24vp_f24_volume_price_confirmation_sign_thrust_80d_base_v054_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_sign_thrust_80d_base_v054_signal},
    "f24vp_f24_volume_price_confirmation_concordance_weighted_40d_base_v055_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_concordance_weighted_40d_base_v055_signal},
    "f24vp_f24_volume_price_confirmation_concordance_weighted_180d_base_v056_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_concordance_weighted_180d_base_v056_signal},
    "f24vp_f24_volume_price_confirmation_bigmove_vol_excess_60d_base_v057_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_bigmove_vol_excess_60d_base_v057_signal},
    "f24vp_f24_volume_price_confirmation_quietmove_vol_deficit_60d_base_v058_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_quietmove_vol_deficit_60d_base_v058_signal},
    "f24vp_f24_volume_price_confirmation_unconfirmed_count_streak_30d_base_v059_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_unconfirmed_count_streak_30d_base_v059_signal},
    "f24vp_f24_volume_price_confirmation_daysince_confirmed_120d_base_v060_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_daysince_confirmed_120d_base_v060_signal},
    "f24vp_f24_volume_price_confirmation_daysince_unconfirmed_60d_base_v061_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_daysince_unconfirmed_60d_base_v061_signal},
    "f24vp_f24_volume_price_confirmation_range_vol_corr_50d_base_v062_signal": {"inputs": ["close", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_range_vol_corr_50d_base_v062_signal},
    "f24vp_f24_volume_price_confirmation_body_vol_corr_60d_base_v063_signal": {"inputs": ["closeadj", "volume", "open"], "func": f24vp_f24_volume_price_confirmation_body_vol_corr_60d_base_v063_signal},
    "f24vp_f24_volume_price_confirmation_signed_body_x_vol_30d_base_v064_signal": {"inputs": ["close", "volume", "open"], "func": f24vp_f24_volume_price_confirmation_signed_body_x_vol_30d_base_v064_signal},
    "f24vp_f24_volume_price_confirmation_volz_up_mean_50d_base_v065_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volz_up_mean_50d_base_v065_signal},
    "f24vp_f24_volume_price_confirmation_volz_dn_mean_50d_base_v066_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volz_dn_mean_50d_base_v066_signal},
    "f24vp_f24_volume_price_confirmation_volz_up_minus_dn_180d_base_v067_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_volz_up_minus_dn_180d_base_v067_signal},
    "f24vp_f24_volume_price_confirmation_corr_change_regime_60d_base_v068_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_corr_change_regime_60d_base_v068_signal},
    "f24vp_f24_volume_price_confirmation_concordance_persistence_100d_base_v069_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_concordance_persistence_100d_base_v069_signal},
    "f24vp_f24_volume_price_confirmation_beta_volpct_on_ret_40d_base_v070_signal": {"inputs": ["close", "volume"], "func": f24vp_f24_volume_price_confirmation_beta_volpct_on_ret_40d_base_v070_signal},
    "f24vp_f24_volume_price_confirmation_thrust_slope_140d_base_v071_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_thrust_slope_140d_base_v071_signal},
    "f24vp_f24_volume_price_confirmation_vwret_autocorr_60d_base_v072_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_vwret_autocorr_60d_base_v072_signal},
    "f24vp_f24_volume_price_confirmation_dual_expansion_count_50d_base_v073_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_dual_expansion_count_50d_base_v073_signal},
    "f24vp_f24_volume_price_confirmation_sigmoid_concordance_60d_base_v074_signal": {"inputs": ["closeadj", "volume"], "func": f24vp_f24_volume_price_confirmation_sigmoid_concordance_60d_base_v074_signal},
    "f24vp_f24_volume_price_confirmation_log_total_dollar_energy_40d_base_v075_signal": {"inputs": ["close", "volume", "high", "low"], "func": f24vp_f24_volume_price_confirmation_log_total_dollar_energy_40d_base_v075_signal},
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
    for name, entry in f24_volume_price_confirmation_base_001_075_REGISTRY.items():
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
    print(f"OK base_001_075: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
