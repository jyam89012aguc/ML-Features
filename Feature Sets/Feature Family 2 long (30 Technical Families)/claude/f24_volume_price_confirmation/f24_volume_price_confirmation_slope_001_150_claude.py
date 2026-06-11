"""f24_volume_price_confirmation slope features 001-150 (1st derivative).
Each slope SPELLS its base inline then applies .diff(k).replace([inf,-inf],nan).
k follows ROC bracket of base's primary window. NaN policy: only final replace.
"""
from __future__ import annotations
import numpy as np
import pandas as pd


def _atr(closeadj, high, low):
    tr = pd.concat([(high - low).abs(),
                    (high - closeadj.shift(1)).abs(),
                    (low - closeadj.shift(1)).abs()], axis=1).max(axis=1)
    return tr.ewm(alpha=1.0 / 14.0, adjust=False, min_periods=14).mean()


def _pct_rank(x):
    return float((np.sum(x <= x[-1]) - 1) / max(1, len(x) - 1))


def _streak_since(x):
    idx = np.where(x > 0.5)[0]
    if idx.size == 0:
        return float(len(x))
    return float(len(x) - 1 - idx[-1])


def f24vp_f24_volume_price_confirmation_volabsret_sma_15d_slope_v001_signal(close, volume):
    n=15; k=5
    return (volume * close.pct_change(1).abs()).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volabsret_logsum_30d_slope_v002_signal(closeadj, volume):
    n=30; k=10
    r = closeadj.pct_change(1).abs()
    return np.log((volume*r).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_logvol_absret_50d_slope_v003_signal(closeadj, volume):
    n=50; k=21
    r = closeadj.pct_change(1).abs()
    vr = volume / volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return (r * np.log(vr)).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volz_absret_25d_slope_v004_signal(close, volume):
    n=25; k=10
    vz = (volume - volume.rolling(63, min_periods=63).mean()) / volume.rolling(63, min_periods=63).std().replace(0.0, np.nan)
    return (vz * close.pct_change(1).abs()).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_topdec_volz_60d_slope_v005_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    th = r.rolling(n, min_periods=n).quantile(0.9)
    m = (r >= th).astype(float).where(~th.isna())
    base = (vz*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_botdec_volz_60d_slope_v006_signal(closeadj, volume):
    n=60; k=10
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    th = r.rolling(n, min_periods=n).quantile(0.1)
    m = (r <= th).astype(float).where(~th.isna())
    base = (vz*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_topbot_volz_diff_80d_slope_v007_signal(closeadj, volume):
    n=80; k=63
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    hi = r.rolling(n, min_periods=n).quantile(0.9); lo = r.rolling(n, min_periods=n).quantile(0.1)
    hm = (r >= hi).astype(float).where(~hi.isna()); lm = (r <= lo).astype(float).where(~lo.isna())
    h = (vz*hm).rolling(n, min_periods=n).sum() / hm.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    l = (vz*lm).rolling(n, min_periods=n).sum() / lm.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (h - l).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signed_vol_sum_20d_slope_v008_signal(close, volume):
    n=20; k=5
    return (np.sign(close.pct_change(1)) * volume).rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signed_vol_ratio_50d_slope_v009_signal(closeadj, volume):
    n=50; k=21
    s = np.sign(closeadj.pct_change(1))
    base = (s*volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_money_flow_30d_slope_v010_signal(closeadj, volume):
    n=30; k=10
    return (closeadj.pct_change(1) * volume).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_money_flow_120d_slope_v011_signal(closeadj, volume):
    n=120; k=63
    return (closeadj.pct_change(1) * volume).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vwret_15d_slope_v012_signal(close, volume):
    n=15; k=10
    r = close.pct_change(1)
    base = (r*volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vwret_100d_slope_v013_signal(closeadj, volume):
    n=100; k=21
    r = closeadj.pct_change(1)
    base = (r*volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_30d_slope_v014_signal(closeadj, volume):
    n=30; k=10
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    base = np.log(up.rolling(n, min_periods=n).sum().replace(0.0, np.nan) / dn.rolling(n, min_periods=n).sum().replace(0.0, np.nan))
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_updn_vol_balance_15d_slope_v015_signal(close, volume):
    n=15; k=5
    r = close.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    base = (up.rolling(n, min_periods=n).sum() - dn.rolling(n, min_periods=n).sum()) / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_updn_vol_balance_80d_slope_v016_signal(closeadj, volume):
    n=80; k=21
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    base = (up.rolling(n, min_periods=n).sum() - dn.rolling(n, min_periods=n).sum()) / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_180d_slope_v017_signal(closeadj, volume):
    n=180; k=63
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    base = np.log(up.rolling(n, min_periods=n).sum().replace(0.0, np.nan) / dn.rolling(n, min_periods=n).sum().replace(0.0, np.nan))
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_count_bigmove_bigvol_60d_slope_v018_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1).abs()
    rm = r.rolling(n, min_periods=n).median(); vm = volume.rolling(n, min_periods=n).median()
    cond = ((r > rm) & (volume > vm)).astype(float).where(~rm.isna() & ~vm.isna())
    return cond.rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_count_bigmove_smallvol_60d_slope_v019_signal(closeadj, volume):
    n=60; k=10
    r = closeadj.pct_change(1).abs()
    rm = r.rolling(n, min_periods=n).median(); vm = volume.rolling(n, min_periods=n).median()
    cond = ((r > rm) & (volume <= vm)).astype(float).where(~rm.isna() & ~vm.isna())
    return cond.rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_confirm_streak_50d_slope_v020_signal(closeadj, volume):
    n=50; k=21
    r = closeadj.pct_change(1).abs()
    rm = r.rolling(n, min_periods=n).median(); vm = volume.rolling(n, min_periods=n).median()
    bad = ((r > rm) & (volume <= vm)).astype(float).where(~rm.isna() & ~vm.isna())
    return bad.rolling(n, min_periods=n).apply(_streak_since, raw=True).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_confirm_xor_sign_30d_slope_v021_signal(close, volume):
    n=30; k=10
    return (np.sign(volume.pct_change(5)) * np.sign(close.pct_change(5))).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_confirm_xor_sign_120d_slope_v022_signal(closeadj, volume):
    n=120; k=63
    return (np.sign(volume.pct_change(10)) * np.sign(closeadj.pct_change(10))).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_absret_vol_45d_slope_v023_signal(closeadj, volume):
    n=45; k=10
    return closeadj.pct_change(1).abs().rolling(n, min_periods=n).corr(volume).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_absret_logvol_120d_slope_v024_signal(closeadj, volume):
    n=120; k=63
    return closeadj.pct_change(1).abs().rolling(n, min_periods=n).corr(np.log(volume.replace(0.0, np.nan))).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_signret_vol_60d_slope_v025_signal(closeadj, volume):
    n=60; k=21
    return np.sign(closeadj.pct_change(1)).rolling(n, min_periods=n).corr(volume).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_spearman_absret_vol_70d_slope_v026_signal(closeadj, volume):
    n=70; k=21
    r = closeadj.pct_change(1).abs()
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    rv = r.values; vv = volume.values
    for i in range(n - 1, len(closeadj)):
        rs = rv[i - n + 1:i + 1]; vs = vv[i - n + 1:i + 1]
        if np.any(~np.isfinite(rs)) or np.any(~np.isfinite(vs)):
            continue
        rr = pd.Series(rs).rank().values; rvk = pd.Series(vs).rank().values
        if rr.std() == 0.0 or rvk.std() == 0.0:
            continue
        out.iat[i] = float(np.corrcoef(rr, rvk)[0, 1])
    return out.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_absret_vol_lag1_45d_slope_v027_signal(closeadj, volume):
    n=45; k=21
    return closeadj.pct_change(1).abs().rolling(n, min_periods=n).corr(volume.shift(1)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volret_prod_std_40d_slope_v028_signal(closeadj, volume):
    n=40; k=10
    return (closeadj.pct_change(1) * volume).rolling(n, min_periods=n).std().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volret_prod_skew_75d_slope_v029_signal(closeadj, volume):
    n=75; k=21
    return (closeadj.pct_change(1) * volume).rolling(n, min_periods=n).skew().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volret_prod_kurt_100d_slope_v030_signal(closeadj, volume):
    n=100; k=63
    return (closeadj.pct_change(1) * volume).rolling(n, min_periods=n).kurt().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volret_prod_max_25d_slope_v031_signal(close, volume):
    n=25; k=10
    p = (close.pct_change(1) * volume).abs()
    base = np.log(p.rolling(n, min_periods=n).max() / p.rolling(n, min_periods=n).median().replace(0.0, np.nan))
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_cum_absret_vol_50d_slope_v032_signal(closeadj, volume):
    n=50; k=21
    e = closeadj.pct_change(1).abs() * volume
    return np.log(e.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_log_cumret_x_cumvol_60d_slope_v033_signal(closeadj, volume):
    n=60; k=21
    cret = (closeadj / closeadj.shift(n)) - 1.0
    cvol = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (np.log(cret.abs().replace(0.0, np.nan)) * np.log(cvol)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_beta_vol_on_absret_50d_slope_v034_signal(closeadj, volume):
    n=50; k=21
    r = closeadj.pct_change(1).abs()
    base = r.rolling(n, min_periods=n).cov(volume) / r.rolling(n, min_periods=n).var().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_beta_logvol_on_signret_70d_slope_v035_signal(closeadj, volume):
    n=70; k=10
    r = closeadj.pct_change(1); lv = np.log(volume.replace(0.0, np.nan))
    base = r.rolling(n, min_periods=n).cov(lv) / r.rolling(n, min_periods=n).var().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_arctan_corr_volz_signret_40d_slope_v036_signal(close, volume):
    n=40; k=21
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    s = np.sign(close.pct_change(1))
    return np.arctan(vz.rolling(n, min_periods=n).corr(s)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_tanh_vwret_norm_60d_slope_v037_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1)
    vw = (r*volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sd = r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return np.tanh(vw / sd).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_ema_volabsret_20d_slope_v038_signal(close, volume):
    n=20; k=5
    return (volume * close.pct_change(1).abs()).ewm(span=n, adjust=False, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_ema_signed_vol_80d_slope_v039_signal(closeadj, volume):
    n=80; k=63
    return (np.sign(closeadj.pct_change(1)) * volume).ewm(span=n, adjust=False, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_thrust_updn_25d_slope_v040_signal(close, volume):
    n=25; k=10
    r = close.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    return (up - dn).rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_thrust_updn_log_100d_slope_v041_signal(closeadj, volume):
    n=100; k=21
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    base = np.log((1.0 + up.rolling(n, min_periods=n).sum()) / (1.0 + dn.rolling(n, min_periods=n).sum()))
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vw_real_vol_45d_slope_v042_signal(close, volume):
    n=45; k=21
    r = close.pct_change(1)
    base = np.sqrt((volume*r*r).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan))
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vw_real_vol_diff_logstd_60d_slope_v043_signal(closeadj, volume):
    n=60; k=10
    r = closeadj.pct_change(1)
    vw = np.sqrt((volume*r*r).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan))
    raw = r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return np.log(vw / raw).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_obv_priceslope_align_30d_slope_v044_signal(closeadj, volume):
    n=30; k=10
    obv = (np.sign(closeadj.diff(1)) * volume).cumsum()
    base = (np.sign(obv.diff(5)) * np.sign(closeadj.diff(5))).rolling(n, min_periods=n).mean()
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_obv_priceslope_align_150d_slope_v045_signal(closeadj, volume):
    n=150; k=63
    obv = (np.sign(closeadj.diff(1)) * volume).cumsum()
    base = (np.sign(obv.diff(21)) * np.sign(closeadj.diff(21))).rolling(n, min_periods=n).mean()
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_of_vwret_50d_slope_v046_signal(closeadj, volume):
    n=50; k=21
    r = closeadj.pct_change(1)
    vw5 = (r*volume).rolling(5, min_periods=5).sum() / volume.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    return vw5.rolling(n, min_periods=n).std().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_rank_volabsret_60d_slope_v047_signal(close, volume):
    n=60; k=21
    e = volume * close.pct_change(1).abs()
    return e.rolling(n, min_periods=n).apply(_pct_rank, raw=True).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_rank_signed_volflow_120d_slope_v048_signal(closeadj, volume):
    n=120; k=63
    sv = (np.sign(closeadj.pct_change(1)) * volume).rolling(20, min_periods=20).sum()
    return sv.rolling(n, min_periods=n).apply(_pct_rank, raw=True).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_short_minus_long_vwret_slope_v049_signal(closeadj, volume):
    k=21
    r = closeadj.pct_change(1)
    s = (r*volume).rolling(10, min_periods=10).sum() / volume.rolling(10, min_periods=10).sum().replace(0.0, np.nan)
    l = (r*volume).rolling(60, min_periods=60).sum() / volume.rolling(60, min_periods=60).sum().replace(0.0, np.nan)
    return (s - l).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_short_minus_long_corr_slope_v050_signal(closeadj, volume):
    k=21
    r = closeadj.pct_change(1).abs()
    return (r.rolling(20, min_periods=20).corr(volume) - r.rolling(150, min_periods=150).corr(volume)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_atr_vol_agree_50d_slope_v051_signal(closeadj, volume, high, low):
    n=50; k=21
    atr = _atr(closeadj, high, low)
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    base = (vz * np.sign(atr.diff(10))).rolling(n, min_periods=n).mean()
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_atr_vol_corr_80d_slope_v052_signal(closeadj, volume, high, low):
    n=80; k=21
    return _atr(closeadj, high, low).rolling(n, min_periods=n).corr(volume).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sign_money_flow_30d_slope_v053_signal(close, volume):
    n=30; k=5
    return np.sign((close.pct_change(1) * volume).rolling(n, min_periods=n).sum()).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sign_thrust_80d_slope_v054_signal(closeadj, volume):
    n=80; k=63
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    return np.sign((up - dn).rolling(n, min_periods=n).sum()).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_concordance_weighted_40d_slope_v055_signal(closeadj, volume):
    n=40; k=10
    r = closeadj.pct_change(1).abs()
    rm = r.rolling(n, min_periods=n).median(); vm = volume.rolling(n, min_periods=n).median()
    base = (np.sign(r - rm) * np.sign(volume - vm)).rolling(n, min_periods=n).mean()
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_concordance_weighted_180d_slope_v056_signal(closeadj, volume):
    n=180; k=63
    r = closeadj.pct_change(1).abs()
    rm = r.rolling(n, min_periods=n).median(); vm = volume.rolling(n, min_periods=n).median()
    base = (np.sign(r - rm) * np.sign(volume - vm)).rolling(n, min_periods=n).mean()
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_bigmove_vol_excess_60d_slope_v057_signal(closeadj, volume):
    n=60; k=10
    r = closeadj.pct_change(1).abs()
    th = r.rolling(n, min_periods=n).quantile(0.9)
    m = (r >= th).astype(float).where(~th.isna())
    num = (volume*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    den = volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return np.log(num / den).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_quietmove_vol_deficit_60d_slope_v058_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1).abs()
    th = r.rolling(n, min_periods=n).quantile(0.1)
    m = (r <= th).astype(float).where(~th.isna())
    num = (volume*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    den = volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return np.log(num / den).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_unconfirmed_count_streak_30d_slope_v059_signal(close, volume):
    n=30; k=5
    r = close.pct_change(1).abs()
    vq = volume.rolling(n, min_periods=n).quantile(0.7); rq = r.rolling(n, min_periods=n).quantile(0.4)
    cond = ((volume > vq) & (r <= rq)).astype(float).where(~vq.isna() & ~rq.isna())
    return cond.rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_daysince_confirmed_120d_slope_v060_signal(closeadj, volume):
    n=120; k=21
    r = closeadj.pct_change(1).abs()
    vq = volume.rolling(n, min_periods=n).quantile(0.8); rq = r.rolling(n, min_periods=n).quantile(0.8)
    flag = ((volume > vq) & (r > rq)).astype(float).where(~vq.isna() & ~rq.isna())
    return flag.rolling(n, min_periods=n).apply(_streak_since, raw=True).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_daysince_unconfirmed_60d_slope_v061_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1).abs()
    vq = volume.rolling(n, min_periods=n).quantile(0.4); rq = r.rolling(n, min_periods=n).quantile(0.8)
    flag = ((volume < vq) & (r > rq)).astype(float).where(~vq.isna() & ~rq.isna())
    return flag.rolling(n, min_periods=n).apply(_streak_since, raw=True).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_range_vol_corr_50d_slope_v062_signal(close, volume, high, low):
    n=50; k=10
    rng = (high - low) / close.replace(0.0, np.nan)
    return rng.rolling(n, min_periods=n).corr(volume).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_body_vol_corr_60d_slope_v063_signal(closeadj, volume, open):
    n=60; k=21
    body = (closeadj - open).abs() / closeadj.replace(0.0, np.nan)
    return body.rolling(n, min_periods=n).corr(volume).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signed_body_x_vol_30d_slope_v064_signal(close, volume, open):
    n=30; k=5
    return (np.sign(close - open) * volume).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volz_up_mean_50d_slope_v065_signal(closeadj, volume):
    n=50; k=10
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    m = (closeadj.pct_change(1) > 0.0).astype(float).where(~vz.isna())
    base = (vz*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volz_dn_mean_50d_slope_v066_signal(closeadj, volume):
    n=50; k=21
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    m = (closeadj.pct_change(1) < 0.0).astype(float).where(~vz.isna())
    base = (vz*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volz_up_minus_dn_180d_slope_v067_signal(closeadj, volume):
    n=180; k=63
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    up = (closeadj.pct_change(1) > 0.0).astype(float).where(~vz.isna())
    dn = (closeadj.pct_change(1) < 0.0).astype(float).where(~vz.isna())
    um = (vz*up).rolling(n, min_periods=n).sum() / up.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    dm = (vz*dn).rolling(n, min_periods=n).sum() / dn.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (um - dm).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_change_regime_60d_slope_v068_signal(closeadj, volume):
    k=10
    c = closeadj.pct_change(1).abs().rolling(30, min_periods=30).corr(volume)
    return c.diff(20).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_concordance_persistence_100d_slope_v069_signal(closeadj, volume):
    n=40; k=21
    r = closeadj.pct_change(1).abs()
    rm = r.rolling(n, min_periods=n).median(); vm = volume.rolling(n, min_periods=n).median()
    c = (np.sign(r - rm) * np.sign(volume - vm)).rolling(n, min_periods=n).mean()
    return c.rolling(100, min_periods=100).std().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_beta_volpct_on_ret_40d_slope_v070_signal(close, volume):
    n=40; k=10
    x = close.pct_change(1); y = volume.pct_change(1)
    return (x.rolling(n, min_periods=n).cov(y) / x.rolling(n, min_periods=n).var().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_thrust_slope_140d_slope_v071_signal(closeadj, volume):
    k=21
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    th = (up - dn).rolling(30, min_periods=30).sum()
    return ((th - th.shift(63)) / 63.0).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vwret_autocorr_60d_slope_v072_signal(closeadj, volume):
    n=60; k=10
    r = closeadj.pct_change(1)
    vw5 = (r*volume).rolling(5, min_periods=5).sum() / volume.rolling(5, min_periods=5).sum().replace(0.0, np.nan)
    return vw5.rolling(n, min_periods=n).corr(vw5.shift(5)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_dual_expansion_count_50d_slope_v073_signal(closeadj, volume):
    n=50; k=21
    r = closeadj.pct_change(1).abs()
    cond = ((volume > volume.rolling(n, min_periods=n).mean()) & (r > r.rolling(n, min_periods=n).mean())).astype(float).where(~volume.rolling(n, min_periods=n).mean().isna())
    return cond.rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sigmoid_concordance_60d_slope_v074_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1).abs()
    rm = r.rolling(n, min_periods=n).median(); vm = volume.rolling(n, min_periods=n).median()
    c = (np.sign(r - rm) * np.sign(volume - vm)).rolling(n, min_periods=n).mean()
    return (1.0 / (1.0 + np.exp(-3.0 * c))).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_log_total_dollar_energy_40d_slope_v075_signal(close, volume, high, low):
    n=40; k=10
    e = volume * (high - low)
    return np.log(e.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vwret_sharpe_30d_slope_v076_signal(closeadj, volume):
    n=30; k=10
    r = closeadj.pct_change(1)
    mn = (r*volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sd = (r*volume).rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (mn / sd).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_dollar_flow_sharpe_80d_slope_v077_signal(closeadj, volume):
    n=80; k=21
    p = closeadj.pct_change(1) * volume
    return (p.rolling(n, min_periods=n).mean() / p.rolling(n, min_periods=n).std().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_ewma_corr_absret_vol_alpha20_slope_v078_signal(closeadj, volume):
    n=40; k=10
    r = closeadj.pct_change(1).abs()
    rd = (r - r.rolling(n, min_periods=n).mean()) / r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    vd = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (rd * vd).ewm(span=20, adjust=False, min_periods=20).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_ewma_signed_dollar_alpha40_slope_v079_signal(closeadj, volume):
    k=21
    s = np.sign(closeadj.pct_change(1))
    e = np.log(volume / volume.rolling(40, min_periods=40).mean().replace(0.0, np.nan))
    return (s * e).ewm(span=40, adjust=False, min_periods=40).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_q75_volabsret_45d_slope_v080_signal(close, volume):
    n=45; k=10
    e = volume * close.pct_change(1).abs()
    return e.rolling(n, min_periods=n).quantile(0.75).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_iqr_signed_volflow_100d_slope_v081_signal(closeadj, volume):
    n=100; k=21
    f = np.sign(closeadj.pct_change(1)) * volume
    return (f.rolling(n, min_periods=n).quantile(0.75) - f.rolling(n, min_periods=n).quantile(0.25)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signpair_concord_30d_slope_v082_signal(close, volume):
    n=30; k=5
    return (np.sign(close.diff(1)) * np.sign(volume.diff(1))).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signpair_concord_5d_lag_80d_slope_v083_signal(closeadj, volume):
    n=80; k=21
    return (np.sign(closeadj.diff(5)) * np.sign(volume.diff(5))).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_q4_minus_q1_by_absret_90d_slope_v084_signal(closeadj, volume):
    n=90; k=21
    r = closeadj.pct_change(1).abs()
    q75 = r.rolling(n, min_periods=n).quantile(0.75); q25 = r.rolling(n, min_periods=n).quantile(0.25)
    mh = (r >= q75).astype(float).where(~q75.isna()); ml = (r <= q25).astype(float).where(~q25.isna())
    vh = (volume*mh).rolling(n, min_periods=n).sum() / mh.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    vl = (volume*ml).rolling(n, min_periods=n).sum() / ml.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(vh / vl).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_logsum_v_on_up_log_55d_slope_v085_signal(closeadj, volume):
    k=21
    r = closeadj.pct_change(1)
    up_vol = volume.where(r > 0.0, 0.0)
    num = up_vol.ewm(span=55, adjust=False, min_periods=55).mean()
    den = volume.ewm(span=55, adjust=False, min_periods=55).mean().replace(0.0, np.nan)
    return np.log(num / den).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_count_vol_q90_per_decade_180d_slope_v086_signal(closeadj, volume):
    n=180; k=63
    r = closeadj.pct_change(1).abs()
    vq = volume.rolling(n, min_periods=n).quantile(0.9); rq = r.rolling(n, min_periods=n).quantile(0.9)
    joint = ((volume > vq) & (r > rq)).astype(float).where(~vq.isna() & ~rq.isna())
    return joint.rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_atr_vol_product_30d_slope_v087_signal(close, volume, high, low):
    n=30; k=10
    rng = (high - low) / close.replace(0.0, np.nan)
    return (volume * rng).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_corr_absret_vol_30d_lag_diff_slope_v088_signal(closeadj, volume):
    k=21
    c = closeadj.pct_change(1).abs().rolling(30, min_periods=30).corr(volume)
    return (c - c.shift(63)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_var_ratio_volret_short_long_slope_v089_signal(closeadj, volume):
    k=21
    p = closeadj.pct_change(1) * volume
    return (p.rolling(20, min_periods=20).var() / p.rolling(100, min_periods=100).var().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_relvol_x_ret_50d_slope_v090_signal(closeadj, volume):
    n=50; k=10
    rv = volume / volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return (rv * closeadj.pct_change(1)).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_relvol_x_absret_120d_slope_v091_signal(closeadj, volume):
    n=120; k=63
    rv = volume / volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return (rv * closeadj.pct_change(1).abs()).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_topdec_vol_absret_mean_70d_slope_v092_signal(closeadj, volume):
    n=70; k=21
    r = closeadj.pct_change(1).abs()
    th = volume.rolling(n, min_periods=n).quantile(0.9)
    m = (volume >= th).astype(float).where(~th.isna())
    return ((r*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_botdec_vol_absret_mean_70d_slope_v093_signal(closeadj, volume):
    n=70; k=21
    r = closeadj.pct_change(1).abs()
    th = volume.rolling(n, min_periods=n).quantile(0.1)
    m = (volume <= th).astype(float).where(~th.isna())
    return ((r*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_qrank_volabsret_score_50d_slope_v094_signal(close, volume):
    n=50; k=10
    r = close.pct_change(1).abs()
    rr = r.rolling(n, min_periods=n).apply(_pct_rank, raw=True)
    rv = volume.rolling(n, min_periods=n).apply(_pct_rank, raw=True)
    return (rr * rv).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_netvol_div_norm_80d_slope_v095_signal(closeadj, volume):
    n=80; k=63
    r = closeadj.pct_change(1)
    num = (np.sign(r) * volume).rolling(n, min_periods=n).sum()
    den = (r.abs() * volume).rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    base = num / den
    normer = base.abs().rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    return (base.diff(k) / normer).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_netvol_div_norm_25d_slope_v096_signal(close, volume):
    n=25; k=5
    r = close.pct_change(1)
    num = (np.sign(r) * volume).rolling(n, min_periods=n).sum()
    den = (r.abs() * volume).rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    base = num / den
    sd = base.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (base.diff(k) / sd).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_thrust_change_20d_slope_v097_signal(close, volume):
    k=5
    r = close.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    th = (up - dn).rolling(20, min_periods=20).sum()
    return th.diff(10).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_ewmcov_logvol_ret_alpha30_slope_v098_signal(closeadj, volume):
    k=10
    r = closeadj.pct_change(1); lv = np.log(volume.replace(0.0, np.nan))
    return r.ewm(span=30, adjust=False, min_periods=30).cov(lv).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volz_x_atrz_45d_slope_v099_signal(closeadj, volume, high, low):
    n=45; k=10
    atr = _atr(closeadj, high, low)
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    az = (atr - atr.rolling(n, min_periods=n).mean()) / atr.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (vz * az).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_body_to_range_volwt_60d_slope_v100_signal(closeadj, volume, high, low, open):
    n=60; k=21
    num = (volume * (closeadj - open).abs()).rolling(n, min_periods=n).sum()
    den = (volume * (high - low)).rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return (num / den).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_granville_confirmed_frac_75d_slope_v101_signal(closeadj, volume):
    n=75; k=21
    sr = np.sign(closeadj.pct_change(1)); sv = np.sign(volume.diff(1))
    flag = (sr == sv).astype(float).where(~sr.isna() & ~sv.isna())
    nz = ((sr != 0.0) & (sv != 0.0)).astype(float).where(~sr.isna() & ~sv.isna())
    base = (flag*nz).rolling(n, min_periods=n).sum() / nz.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_lead_absret_corr_50d_slope_v102_signal(closeadj, volume):
    n=50; k=10
    return volume.rolling(n, min_periods=n).corr(closeadj.pct_change(1).abs().shift(-1)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_p_bigmove_given_bigvol_60d_slope_v103_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1).abs()
    rq = r.rolling(n, min_periods=n).quantile(0.7); vq = volume.rolling(n, min_periods=n).quantile(0.7)
    bv = (volume > vq).astype(float).where(~vq.isna()); br = (r > rq).astype(float).where(~rq.isna())
    base = (bv*br).rolling(n, min_periods=n).sum() / bv.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_p_bigvol_given_bigmove_60d_slope_v104_signal(closeadj, volume):
    n=60; k=10
    r = closeadj.pct_change(1).abs()
    rq = r.rolling(n, min_periods=n).quantile(0.7); vq = volume.rolling(n, min_periods=n).quantile(0.7)
    bv = (volume > vq).astype(float).where(~vq.isna()); br = (r > rq).astype(float).where(~rq.isna())
    base = (bv*br).rolling(n, min_periods=n).sum() / br.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return base.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_phi_coef_signv_signret_50d_slope_v105_signal(closeadj, volume):
    n=50; k=21
    a = np.sign(closeadj.diff(1)); b = np.sign(volume.diff(1))
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    av = a.values; bv = b.values
    for i in range(n - 1, len(closeadj)):
        aw = av[i - n + 1:i + 1]; bw = bv[i - n + 1:i + 1]
        msk = np.isfinite(aw) & np.isfinite(bw) & (aw != 0.0) & (bw != 0.0)
        if msk.sum() < 10:
            continue
        x = (aw[msk] > 0).astype(float); y = (bw[msk] > 0).astype(float)
        if x.std() == 0.0 or y.std() == 0.0:
            continue
        out.iat[i] = float(np.corrcoef(x, y)[0, 1])
    return out.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_logvol_slope_x_signret_40d_slope_v106_signal(closeadj, volume):
    n=40; k=21
    s = np.sign(closeadj.pct_change(1)); lvs = np.log(volume.replace(0.0, np.nan)).diff(5)
    return (s * lvs).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_cum_signed_vol_to_total_45d_slope_v107_signal(closeadj, volume):
    n=45; k=10
    s = np.sign(closeadj.pct_change(1))
    num = (s * volume).rolling(n, min_periods=n).sum()
    den = volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    med = num.rolling(n, min_periods=n).median()
    return ((num - med) / den).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_range_signed_vol_40d_slope_v108_signal(close, volume, high, low):
    n=40; k=10
    rng = (high - low) / close.replace(0.0, np.nan)
    return (np.sign(close.pct_change(1)) * volume * rng).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sign_corr_absret_vol_60d_slope_v109_signal(closeadj, volume):
    n=60; k=10
    return np.sign(closeadj.pct_change(1).abs().rolling(n, min_periods=n).corr(volume)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sign_corr_signret_vol_30d_slope_v110_signal(close, volume):
    n=30; k=5
    return np.sign(np.sign(close.pct_change(1)).rolling(n, min_periods=n).corr(volume)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volprice_kurtcorr_90d_slope_v111_signal(closeadj, volume):
    n=90; k=21
    r = closeadj.pct_change(1)
    dev4 = (r - r.rolling(n, min_periods=n).mean()) ** 4
    return dev4.rolling(n, min_periods=n).corr(volume).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_share_of_trend_leg_60d_slope_v112_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1)
    trend = np.sign(r.rolling(5, min_periods=5).mean())
    agree = (np.sign(r) == trend).astype(float).where(~trend.isna() & ~np.isnan(r))
    return ((agree*volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_weighted_ret_skew_70d_slope_v113_signal(closeadj, volume):
    n=70; k=21
    r = closeadj.pct_change(1); w = volume
    sw = w.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu = (w*r).rolling(n, min_periods=n).sum() / sw
    dev = r - mu
    m2 = (w*dev*dev).rolling(n, min_periods=n).sum() / sw
    m3 = (w*dev*dev*dev).rolling(n, min_periods=n).sum() / sw
    sig = np.sqrt(m2)
    return (m3 / (sig*sig*sig).replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_weighted_ret_kurt_120d_slope_v114_signal(closeadj, volume):
    n=120; k=63
    r = closeadj.pct_change(1); w = volume
    sw = w.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    mu = (w*r).rolling(n, min_periods=n).sum() / sw
    dev = r - mu
    m2 = (w*dev*dev).rolling(n, min_periods=n).sum() / sw
    m4 = (w*dev*dev*dev*dev).rolling(n, min_periods=n).sum() / sw
    return ((m4 / (m2*m2).replace(0.0, np.nan)) - 3.0).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_ema_thrust_convexity_50d_slope_v115_signal(closeadj, volume):
    k=21
    s = np.sign(closeadj.pct_change(1))
    et = (s * volume).ewm(span=50, adjust=False, min_periods=50).mean()
    d = et.diff(5)
    return (d - d.shift(5)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_confirmed_ret_mean_80d_slope_v116_signal(closeadj, volume):
    n=80; k=21
    r = closeadj.pct_change(1)
    vmed = volume.rolling(n, min_periods=n).median()
    m = (volume > vmed).astype(float).where(~vmed.isna())
    return ((r*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_unconfirmed_ret_mean_80d_slope_v117_signal(closeadj, volume):
    n=80; k=63
    r = closeadj.pct_change(1)
    vmed = volume.rolling(n, min_periods=n).median()
    m = (volume <= vmed).astype(float).where(~vmed.isna())
    return ((r*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_volspike_moveaspike_align_45d_slope_v118_signal(closeadj, volume):
    n=45; k=21
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    rz = (r - r.rolling(n, min_periods=n).mean()) / r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    flag = ((vz > 1.0) & (rz > 1.0)).astype(float).where(~vz.isna() & ~rz.isna())
    return flag.rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sign_body_volz_30d_slope_v119_signal(close, volume, open):
    n=30; k=5
    sb = np.sign(close - open); sv = np.sign(volume - volume.rolling(n, min_periods=n).mean())
    return (sb * sv).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vpt_slope_norm_60d_slope_v120_signal(closeadj, volume):
    k=21
    vpt = (volume * closeadj.pct_change(1)).cumsum()
    return (vpt.diff(21) / volume.rolling(21, min_periods=21).mean().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vpt_to_price_slope_corr_120d_slope_v121_signal(closeadj, volume):
    n=120; k=63
    vpt = (volume * closeadj.pct_change(1)).cumsum()
    return vpt.diff(5).rolling(n, min_periods=n).corr(closeadj.diff(5)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_logvolz_on_signret_corr_75d_slope_v122_signal(closeadj, volume):
    n=75; k=21
    lv = np.log(volume.replace(0.0, np.nan))
    lvz = (lv - lv.rolling(n, min_periods=n).mean()) / lv.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return lvz.rolling(n, min_periods=n).corr(np.sign(closeadj.diff(1))).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_n_confirmed_bursts_150d_slope_v123_signal(closeadj, volume):
    n=150; k=63
    vz = (volume - volume.rolling(60, min_periods=60).mean()) / volume.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    r = closeadj.pct_change(1).abs()
    rz = (r - r.rolling(60, min_periods=60).mean()) / r.rolling(60, min_periods=60).std().replace(0.0, np.nan)
    flag = ((vz > 1.0) & (rz > 1.0)).astype(float).where(~vz.isna() & ~rz.isna())
    burst = ((flag > 0.5) & (flag.shift(1) < 0.5)).astype(float).where(~flag.shift(1).isna())
    return burst.rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_log_vol_total_per_abs_move_40d_slope_v124_signal(close, volume):
    n=40; k=10
    r = close.pct_change(1).abs()
    lv = np.log(volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan))
    lr = np.log(r.rolling(n, min_periods=n).sum().replace(0.0, np.nan))
    return (lv / lr).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_asym_idx_volz_ret_55d_slope_v125_signal(closeadj, volume):
    n=55; k=21
    vexc = volume - volume.rolling(n, min_periods=n).mean()
    r = closeadj.pct_change(1)
    return (vexc * r * r * r).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_acc_price_acc_align_30d_slope_v126_signal(close, volume):
    n=30; k=5
    return (np.sign(volume.diff().diff()) * np.sign(close.diff().diff())).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_tanh_money_flow_norm_45d_slope_v127_signal(closeadj, volume):
    n=45; k=21
    r = closeadj.pct_change(1)
    flow = (r*volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).mean().replace(0.0, np.nan)
    sd = r.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return np.tanh(flow / sd).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_arctan_topdec_volz_75d_slope_v128_signal(closeadj, volume):
    n=75; k=10
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    th = r.rolling(n, min_periods=n).quantile(0.9)
    m = (r >= th).astype(float).where(~th.isna())
    avg = (vz*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.arctan(avg).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vw_absret_autocorr_60d_slope_v129_signal(closeadj, volume):
    n=60; k=21
    e = closeadj.pct_change(1).abs() * volume
    return e.rolling(n, min_periods=n).corr(e.shift(5)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_trend_vol_share_200d_slope_v130_signal(closeadj, volume):
    n=200; k=63
    r = closeadj.pct_change(1)
    trend = np.sign(r.rolling(21, min_periods=21).mean())
    agree = (np.sign(r) == trend).astype(float).where(~trend.isna() & ~np.isnan(r))
    return ((agree*volume).rolling(n, min_periods=n).sum() / volume.rolling(n, min_periods=n).sum().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_atrvolz_diff_40d_slope_v131_signal(closeadj, volume, high, low):
    n=40; k=10
    prod = (volume * _atr(closeadj, high, low)).ewm(span=n, adjust=False, min_periods=n).mean()
    return prod.diff(10).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_count_upday_highvol_50d_slope_v132_signal(closeadj, volume):
    n=50; k=21
    up = (closeadj.diff(1) > 0.0).astype(float)
    vq = volume.rolling(n, min_periods=n).quantile(0.6)
    cond = (up.astype(bool) & (volume > vq)).astype(float).where(~vq.isna())
    return cond.rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_count_dnday_highvol_50d_slope_v133_signal(closeadj, volume):
    n=50; k=10
    dn = (closeadj.diff(1) < 0.0).astype(float)
    vq = volume.rolling(n, min_periods=n).quantile(0.6)
    cond = (dn.astype(bool) & (volume > vq)).astype(float).where(~vq.isna())
    return cond.rolling(n, min_periods=n).sum().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_up_dn_highvol_imbalance_50d_slope_v134_signal(closeadj, volume):
    n=50; k=21
    up = (closeadj.diff(1) > 0.0).astype(float); dn = (closeadj.diff(1) < 0.0).astype(float)
    vq = volume.rolling(n, min_periods=n).quantile(0.6)
    cu = (up.astype(bool) & (volume > vq)).astype(float).where(~vq.isna())
    cd = (dn.astype(bool) & (volume > vq)).astype(float).where(~vq.isna())
    return ((cu - cd).rolling(n, min_periods=n).sum() / float(n)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_entropy_signret_60d_slope_v135_signal(closeadj, volume):
    n=60; k=21
    s = np.sign(closeadj.pct_change(1))
    out = pd.Series(np.nan, index=closeadj.index, dtype=float)
    sv = s.values; vv = volume.values
    for i in range(n - 1, len(closeadj)):
        sw = sv[i - n + 1:i + 1]; vw = vv[i - n + 1:i + 1]
        if np.any(~np.isfinite(sw)) or np.any(~np.isfinite(vw)):
            continue
        tot = vw.sum()
        if tot <= 0.0:
            continue
        sums = []
        for bv in (-1.0, 0.0, 1.0):
            sums.append(vw[sw == bv].sum())
        p = np.asarray(sums) / tot
        p = p[p > 0.0]
        out.iat[i] = float(-(p * np.log(p)).sum())
    return out.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_topdec_volz_slope_100d_slope_v136_signal(closeadj, volume):
    n=100; k=21
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    th = r.rolling(n, min_periods=n).quantile(0.9)
    m = (r >= th).astype(float).where(~th.isna())
    avg = (vz*m).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return avg.diff(21).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_gap_volz_align_45d_slope_v137_signal(closeadj, volume, open):
    n=45; k=10
    gap = open / closeadj.shift(1) - 1.0
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (np.sign(gap) * vz).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_rsq_vol_explains_absret_70d_slope_v138_signal(closeadj, volume):
    n=70; k=21
    r = closeadj.pct_change(1).abs(); lv = np.log(volume.replace(0.0, np.nan))
    c = r.rolling(n, min_periods=n).corr(lv)
    return (c*c).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_macd_x_price_macd_60d_slope_v139_signal(closeadj, volume):
    n=60; k=21
    vm = np.sign(volume.ewm(span=12, adjust=False, min_periods=12).mean() - volume.ewm(span=26, adjust=False, min_periods=26).mean())
    pm = np.sign(closeadj.ewm(span=12, adjust=False, min_periods=12).mean() - closeadj.ewm(span=26, adjust=False, min_periods=26).mean())
    return (vm * pm).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_force_index_norm_25d_slope_v140_signal(close, volume):
    n=25; k=10
    f = close.diff(1) * volume
    return (f.rolling(n, min_periods=n).mean() / f.abs().rolling(n, min_periods=n).mean().replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_rank_topdec_volz_180d_slope_v141_signal(closeadj, volume):
    no=180; ni=60; k=63
    r = closeadj.pct_change(1).abs()
    vz = (volume - volume.rolling(ni, min_periods=ni).mean()) / volume.rolling(ni, min_periods=ni).std().replace(0.0, np.nan)
    th = r.rolling(ni, min_periods=ni).quantile(0.9)
    m = (r >= th).astype(float).where(~th.isna())
    avg = (vz*m).rolling(ni, min_periods=ni).sum() / m.rolling(ni, min_periods=ni).sum().replace(0.0, np.nan)
    return avg.rolling(no, min_periods=no).apply(_pct_rank, raw=True).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_bipolar_pn_diff_50d_slope_v142_signal(closeadj, volume):
    n=50; k=21
    r = closeadj.pct_change(1)
    vq = volume.rolling(n, min_periods=n).quantile(0.7); rq = r.abs().rolling(n, min_periods=n).quantile(0.7)
    bu = ((r > 0.0) & (r.abs() > rq) & (volume > vq)).astype(float).where(~vq.isna() & ~rq.isna())
    bd = ((r < 0.0) & (r.abs() > rq) & (volume > vq)).astype(float).where(~vq.isna() & ~rq.isna())
    return (bu - bd).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_sharpe_highvol_ret_60d_slope_v143_signal(closeadj, volume):
    n=60; k=21
    r = closeadj.pct_change(1)
    vq = volume.rolling(n, min_periods=n).quantile(0.7)
    m = (volume > vq).astype(float).where(~vq.isna())
    cr = r * m
    mn = cr.rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sq = (cr*cr).rolling(n, min_periods=n).sum() / m.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    sd = np.sqrt(sq - mn*mn)
    return (mn / sd.replace(0.0, np.nan)).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_rank_concord_score_120d_slope_v144_signal(closeadj, volume):
    no=120; ni=40; k=63
    r = closeadj.pct_change(1).abs()
    rm = r.rolling(ni, min_periods=ni).median(); vm = volume.rolling(ni, min_periods=ni).median()
    c = (np.sign(r - rm) * np.sign(volume - vm)).rolling(ni, min_periods=ni).mean()
    return c.rolling(no, min_periods=no).apply(_pct_rank, raw=True).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_double_ema_signed_flow_55d_slope_v145_signal(closeadj, volume):
    k=21
    s = np.sign(closeadj.pct_change(1)); lv = np.log(volume.replace(0.0, np.nan))
    inner = (s * lv).ewm(span=55, adjust=False, min_periods=55).mean()
    return inner.ewm(span=20, adjust=False, min_periods=20).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_logratio_bigmove_vol_125d_slope_v146_signal(closeadj, volume):
    n=125; k=63
    r = closeadj.pct_change(1).abs()
    med = r.rolling(n, min_periods=n).median()
    big = volume.where(r > med, 0.0); small = volume.where(r <= med, 0.0)
    sb = big.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    ss = small.rolling(n, min_periods=n).sum().replace(0.0, np.nan)
    return np.log(sb / ss).diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_thrust_z_70d_slope_v147_signal(closeadj, volume):
    no=70; ni=30; k=21
    r = closeadj.pct_change(1)
    up = volume.where(r > 0.0, 0.0); dn = volume.where(r < 0.0, 0.0)
    th = (up - dn).rolling(ni, min_periods=ni).sum()
    z = (th - th.rolling(no, min_periods=no).mean()) / th.rolling(no, min_periods=no).std().replace(0.0, np.nan)
    return z.diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_signed_vol_x_range_z_40d_slope_v148_signal(close, volume, high, low):
    n=40; k=10
    s = np.sign(close.pct_change(1))
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    rng = (high - low) / close.replace(0.0, np.nan)
    rzz = (rng - rng.rolling(n, min_periods=n).mean()) / rng.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (s * (vz + rzz)).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_vol_residual_after_absret_90d_slope_v149_signal(closeadj, volume):
    n=90; k=21
    r = closeadj.pct_change(1).abs()
    beta = r.rolling(n, min_periods=n).cov(volume) / r.rolling(n, min_periods=n).var().replace(0.0, np.nan)
    alpha = volume.rolling(n, min_periods=n).mean() - beta * r.rolling(n, min_periods=n).mean()
    resid = volume - alpha - beta * r
    return resid.rolling(n, min_periods=n).std().diff(k).replace([np.inf, -np.inf], np.nan)


def f24vp_f24_volume_price_confirmation_compound_confirm_score_85d_slope_v150_signal(closeadj, volume):
    n=85; k=21
    r = closeadj.pct_change(1); s = np.sign(r)
    vz = (volume - volume.rolling(n, min_periods=n).mean()) / volume.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    ar = r.abs()
    rz = (ar - ar.rolling(n, min_periods=n).mean()) / ar.rolling(n, min_periods=n).std().replace(0.0, np.nan)
    return (s * vz * rz).rolling(n, min_periods=n).mean().diff(k).replace([np.inf, -np.inf], np.nan)


_REG = f24_volume_price_confirmation_slope_001_150_REGISTRY = {}
for _fn in [
    f24vp_f24_volume_price_confirmation_volabsret_sma_15d_slope_v001_signal,
    f24vp_f24_volume_price_confirmation_volabsret_logsum_30d_slope_v002_signal,
    f24vp_f24_volume_price_confirmation_logvol_absret_50d_slope_v003_signal,
    f24vp_f24_volume_price_confirmation_volz_absret_25d_slope_v004_signal,
    f24vp_f24_volume_price_confirmation_topdec_volz_60d_slope_v005_signal,
    f24vp_f24_volume_price_confirmation_botdec_volz_60d_slope_v006_signal,
    f24vp_f24_volume_price_confirmation_topbot_volz_diff_80d_slope_v007_signal,
    f24vp_f24_volume_price_confirmation_signed_vol_sum_20d_slope_v008_signal,
    f24vp_f24_volume_price_confirmation_signed_vol_ratio_50d_slope_v009_signal,
    f24vp_f24_volume_price_confirmation_money_flow_30d_slope_v010_signal,
    f24vp_f24_volume_price_confirmation_money_flow_120d_slope_v011_signal,
    f24vp_f24_volume_price_confirmation_vwret_15d_slope_v012_signal,
    f24vp_f24_volume_price_confirmation_vwret_100d_slope_v013_signal,
    f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_30d_slope_v014_signal,
    f24vp_f24_volume_price_confirmation_updn_vol_balance_15d_slope_v015_signal,
    f24vp_f24_volume_price_confirmation_updn_vol_balance_80d_slope_v016_signal,
    f24vp_f24_volume_price_confirmation_updn_vol_ratio_log_180d_slope_v017_signal,
    f24vp_f24_volume_price_confirmation_count_bigmove_bigvol_60d_slope_v018_signal,
    f24vp_f24_volume_price_confirmation_count_bigmove_smallvol_60d_slope_v019_signal,
    f24vp_f24_volume_price_confirmation_confirm_streak_50d_slope_v020_signal,
    f24vp_f24_volume_price_confirmation_confirm_xor_sign_30d_slope_v021_signal,
    f24vp_f24_volume_price_confirmation_confirm_xor_sign_120d_slope_v022_signal,
    f24vp_f24_volume_price_confirmation_corr_absret_vol_45d_slope_v023_signal,
    f24vp_f24_volume_price_confirmation_corr_absret_logvol_120d_slope_v024_signal,
    f24vp_f24_volume_price_confirmation_corr_signret_vol_60d_slope_v025_signal,
    f24vp_f24_volume_price_confirmation_spearman_absret_vol_70d_slope_v026_signal,
    f24vp_f24_volume_price_confirmation_corr_absret_vol_lag1_45d_slope_v027_signal,
    f24vp_f24_volume_price_confirmation_volret_prod_std_40d_slope_v028_signal,
    f24vp_f24_volume_price_confirmation_volret_prod_skew_75d_slope_v029_signal,
    f24vp_f24_volume_price_confirmation_volret_prod_kurt_100d_slope_v030_signal,
    f24vp_f24_volume_price_confirmation_volret_prod_max_25d_slope_v031_signal,
    f24vp_f24_volume_price_confirmation_cum_absret_vol_50d_slope_v032_signal,
    f24vp_f24_volume_price_confirmation_log_cumret_x_cumvol_60d_slope_v033_signal,
    f24vp_f24_volume_price_confirmation_beta_vol_on_absret_50d_slope_v034_signal,
    f24vp_f24_volume_price_confirmation_beta_logvol_on_signret_70d_slope_v035_signal,
    f24vp_f24_volume_price_confirmation_arctan_corr_volz_signret_40d_slope_v036_signal,
    f24vp_f24_volume_price_confirmation_tanh_vwret_norm_60d_slope_v037_signal,
    f24vp_f24_volume_price_confirmation_ema_volabsret_20d_slope_v038_signal,
    f24vp_f24_volume_price_confirmation_ema_signed_vol_80d_slope_v039_signal,
    f24vp_f24_volume_price_confirmation_thrust_updn_25d_slope_v040_signal,
    f24vp_f24_volume_price_confirmation_thrust_updn_log_100d_slope_v041_signal,
    f24vp_f24_volume_price_confirmation_vw_real_vol_45d_slope_v042_signal,
    f24vp_f24_volume_price_confirmation_vw_real_vol_diff_logstd_60d_slope_v043_signal,
    f24vp_f24_volume_price_confirmation_obv_priceslope_align_30d_slope_v044_signal,
    f24vp_f24_volume_price_confirmation_obv_priceslope_align_150d_slope_v045_signal,
    f24vp_f24_volume_price_confirmation_vol_of_vwret_50d_slope_v046_signal,
    f24vp_f24_volume_price_confirmation_rank_volabsret_60d_slope_v047_signal,
    f24vp_f24_volume_price_confirmation_rank_signed_volflow_120d_slope_v048_signal,
    f24vp_f24_volume_price_confirmation_short_minus_long_vwret_slope_v049_signal,
    f24vp_f24_volume_price_confirmation_short_minus_long_corr_slope_v050_signal,
    f24vp_f24_volume_price_confirmation_atr_vol_agree_50d_slope_v051_signal,
    f24vp_f24_volume_price_confirmation_atr_vol_corr_80d_slope_v052_signal,
    f24vp_f24_volume_price_confirmation_sign_money_flow_30d_slope_v053_signal,
    f24vp_f24_volume_price_confirmation_sign_thrust_80d_slope_v054_signal,
    f24vp_f24_volume_price_confirmation_concordance_weighted_40d_slope_v055_signal,
    f24vp_f24_volume_price_confirmation_concordance_weighted_180d_slope_v056_signal,
    f24vp_f24_volume_price_confirmation_bigmove_vol_excess_60d_slope_v057_signal,
    f24vp_f24_volume_price_confirmation_quietmove_vol_deficit_60d_slope_v058_signal,
    f24vp_f24_volume_price_confirmation_unconfirmed_count_streak_30d_slope_v059_signal,
    f24vp_f24_volume_price_confirmation_daysince_confirmed_120d_slope_v060_signal,
    f24vp_f24_volume_price_confirmation_daysince_unconfirmed_60d_slope_v061_signal,
    f24vp_f24_volume_price_confirmation_range_vol_corr_50d_slope_v062_signal,
    f24vp_f24_volume_price_confirmation_body_vol_corr_60d_slope_v063_signal,
    f24vp_f24_volume_price_confirmation_signed_body_x_vol_30d_slope_v064_signal,
    f24vp_f24_volume_price_confirmation_volz_up_mean_50d_slope_v065_signal,
    f24vp_f24_volume_price_confirmation_volz_dn_mean_50d_slope_v066_signal,
    f24vp_f24_volume_price_confirmation_volz_up_minus_dn_180d_slope_v067_signal,
    f24vp_f24_volume_price_confirmation_corr_change_regime_60d_slope_v068_signal,
    f24vp_f24_volume_price_confirmation_concordance_persistence_100d_slope_v069_signal,
    f24vp_f24_volume_price_confirmation_beta_volpct_on_ret_40d_slope_v070_signal,
    f24vp_f24_volume_price_confirmation_thrust_slope_140d_slope_v071_signal,
    f24vp_f24_volume_price_confirmation_vwret_autocorr_60d_slope_v072_signal,
    f24vp_f24_volume_price_confirmation_dual_expansion_count_50d_slope_v073_signal,
    f24vp_f24_volume_price_confirmation_sigmoid_concordance_60d_slope_v074_signal,
    f24vp_f24_volume_price_confirmation_log_total_dollar_energy_40d_slope_v075_signal,
    f24vp_f24_volume_price_confirmation_vwret_sharpe_30d_slope_v076_signal,
    f24vp_f24_volume_price_confirmation_dollar_flow_sharpe_80d_slope_v077_signal,
    f24vp_f24_volume_price_confirmation_ewma_corr_absret_vol_alpha20_slope_v078_signal,
    f24vp_f24_volume_price_confirmation_ewma_signed_dollar_alpha40_slope_v079_signal,
    f24vp_f24_volume_price_confirmation_q75_volabsret_45d_slope_v080_signal,
    f24vp_f24_volume_price_confirmation_iqr_signed_volflow_100d_slope_v081_signal,
    f24vp_f24_volume_price_confirmation_signpair_concord_30d_slope_v082_signal,
    f24vp_f24_volume_price_confirmation_signpair_concord_5d_lag_80d_slope_v083_signal,
    f24vp_f24_volume_price_confirmation_vol_q4_minus_q1_by_absret_90d_slope_v084_signal,
    f24vp_f24_volume_price_confirmation_logsum_v_on_up_log_55d_slope_v085_signal,
    f24vp_f24_volume_price_confirmation_count_vol_q90_per_decade_180d_slope_v086_signal,
    f24vp_f24_volume_price_confirmation_atr_vol_product_30d_slope_v087_signal,
    f24vp_f24_volume_price_confirmation_corr_absret_vol_30d_lag_diff_slope_v088_signal,
    f24vp_f24_volume_price_confirmation_var_ratio_volret_short_long_slope_v089_signal,
    f24vp_f24_volume_price_confirmation_relvol_x_ret_50d_slope_v090_signal,
    f24vp_f24_volume_price_confirmation_relvol_x_absret_120d_slope_v091_signal,
    f24vp_f24_volume_price_confirmation_topdec_vol_absret_mean_70d_slope_v092_signal,
    f24vp_f24_volume_price_confirmation_botdec_vol_absret_mean_70d_slope_v093_signal,
    f24vp_f24_volume_price_confirmation_qrank_volabsret_score_50d_slope_v094_signal,
    f24vp_f24_volume_price_confirmation_netvol_div_norm_80d_slope_v095_signal,
    f24vp_f24_volume_price_confirmation_netvol_div_norm_25d_slope_v096_signal,
    f24vp_f24_volume_price_confirmation_thrust_change_20d_slope_v097_signal,
    f24vp_f24_volume_price_confirmation_ewmcov_logvol_ret_alpha30_slope_v098_signal,
    f24vp_f24_volume_price_confirmation_volz_x_atrz_45d_slope_v099_signal,
    f24vp_f24_volume_price_confirmation_body_to_range_volwt_60d_slope_v100_signal,
    f24vp_f24_volume_price_confirmation_granville_confirmed_frac_75d_slope_v101_signal,
    f24vp_f24_volume_price_confirmation_vol_lead_absret_corr_50d_slope_v102_signal,
    f24vp_f24_volume_price_confirmation_p_bigmove_given_bigvol_60d_slope_v103_signal,
    f24vp_f24_volume_price_confirmation_p_bigvol_given_bigmove_60d_slope_v104_signal,
    f24vp_f24_volume_price_confirmation_phi_coef_signv_signret_50d_slope_v105_signal,
    f24vp_f24_volume_price_confirmation_logvol_slope_x_signret_40d_slope_v106_signal,
    f24vp_f24_volume_price_confirmation_cum_signed_vol_to_total_45d_slope_v107_signal,
    f24vp_f24_volume_price_confirmation_range_signed_vol_40d_slope_v108_signal,
    f24vp_f24_volume_price_confirmation_sign_corr_absret_vol_60d_slope_v109_signal,
    f24vp_f24_volume_price_confirmation_sign_corr_signret_vol_30d_slope_v110_signal,
    f24vp_f24_volume_price_confirmation_volprice_kurtcorr_90d_slope_v111_signal,
    f24vp_f24_volume_price_confirmation_vol_share_of_trend_leg_60d_slope_v112_signal,
    f24vp_f24_volume_price_confirmation_vol_weighted_ret_skew_70d_slope_v113_signal,
    f24vp_f24_volume_price_confirmation_vol_weighted_ret_kurt_120d_slope_v114_signal,
    f24vp_f24_volume_price_confirmation_ema_thrust_convexity_50d_slope_v115_signal,
    f24vp_f24_volume_price_confirmation_confirmed_ret_mean_80d_slope_v116_signal,
    f24vp_f24_volume_price_confirmation_unconfirmed_ret_mean_80d_slope_v117_signal,
    f24vp_f24_volume_price_confirmation_volspike_moveaspike_align_45d_slope_v118_signal,
    f24vp_f24_volume_price_confirmation_sign_body_volz_30d_slope_v119_signal,
    f24vp_f24_volume_price_confirmation_vpt_slope_norm_60d_slope_v120_signal,
    f24vp_f24_volume_price_confirmation_vpt_to_price_slope_corr_120d_slope_v121_signal,
    f24vp_f24_volume_price_confirmation_logvolz_on_signret_corr_75d_slope_v122_signal,
    f24vp_f24_volume_price_confirmation_n_confirmed_bursts_150d_slope_v123_signal,
    f24vp_f24_volume_price_confirmation_log_vol_total_per_abs_move_40d_slope_v124_signal,
    f24vp_f24_volume_price_confirmation_asym_idx_volz_ret_55d_slope_v125_signal,
    f24vp_f24_volume_price_confirmation_vol_acc_price_acc_align_30d_slope_v126_signal,
    f24vp_f24_volume_price_confirmation_tanh_money_flow_norm_45d_slope_v127_signal,
    f24vp_f24_volume_price_confirmation_arctan_topdec_volz_75d_slope_v128_signal,
    f24vp_f24_volume_price_confirmation_vw_absret_autocorr_60d_slope_v129_signal,
    f24vp_f24_volume_price_confirmation_trend_vol_share_200d_slope_v130_signal,
    f24vp_f24_volume_price_confirmation_atrvolz_diff_40d_slope_v131_signal,
    f24vp_f24_volume_price_confirmation_count_upday_highvol_50d_slope_v132_signal,
    f24vp_f24_volume_price_confirmation_count_dnday_highvol_50d_slope_v133_signal,
    f24vp_f24_volume_price_confirmation_up_dn_highvol_imbalance_50d_slope_v134_signal,
    f24vp_f24_volume_price_confirmation_vol_entropy_signret_60d_slope_v135_signal,
    f24vp_f24_volume_price_confirmation_topdec_volz_slope_100d_slope_v136_signal,
    f24vp_f24_volume_price_confirmation_gap_volz_align_45d_slope_v137_signal,
    f24vp_f24_volume_price_confirmation_rsq_vol_explains_absret_70d_slope_v138_signal,
    f24vp_f24_volume_price_confirmation_vol_macd_x_price_macd_60d_slope_v139_signal,
    f24vp_f24_volume_price_confirmation_force_index_norm_25d_slope_v140_signal,
    f24vp_f24_volume_price_confirmation_rank_topdec_volz_180d_slope_v141_signal,
    f24vp_f24_volume_price_confirmation_bipolar_pn_diff_50d_slope_v142_signal,
    f24vp_f24_volume_price_confirmation_sharpe_highvol_ret_60d_slope_v143_signal,
    f24vp_f24_volume_price_confirmation_rank_concord_score_120d_slope_v144_signal,
    f24vp_f24_volume_price_confirmation_double_ema_signed_flow_55d_slope_v145_signal,
    f24vp_f24_volume_price_confirmation_logratio_bigmove_vol_125d_slope_v146_signal,
    f24vp_f24_volume_price_confirmation_thrust_z_70d_slope_v147_signal,
    f24vp_f24_volume_price_confirmation_signed_vol_x_range_z_40d_slope_v148_signal,
    f24vp_f24_volume_price_confirmation_vol_residual_after_absret_90d_slope_v149_signal,
    f24vp_f24_volume_price_confirmation_compound_confirm_score_85d_slope_v150_signal,
]:
    # Map by introspecting parameter names — count varargs of underlying function.
    import inspect
    _params = list(inspect.signature(_fn).parameters.keys())
    _REG[_fn.__name__] = {"inputs": _params, "func": _fn}


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
    for name, entry in f24_volume_price_confirmation_slope_001_150_REGISTRY.items():
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
    print(f"OK slope_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")


if __name__ == "__main__":
    _self_test()
