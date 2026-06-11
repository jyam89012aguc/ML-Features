"""f15_cross_sectional_momentum slope features 001-150 (1st derivative).
Slope_i = base_i computed inline, then .diff(k) where k is chosen from the
ROC bracket of the base's primary window. Window > 21 uses closeadj. NaN
policy: replace([inf,-inf], nan) at return.
"""
from __future__ import annotations
import numpy as np
import pandas as pd
def f15xm_f15_cross_sectional_momentum_pctrnk_252d_slope_v001_signal(closeadj):
    b = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_pctrnk_126d_slope_v002_signal(closeadj):
    b = closeadj.pct_change(5).rolling(126, min_periods=100).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_pctrnk_504d_slope_v003_signal(closeadj):
    b = closeadj.pct_change(63).rolling(504, min_periods=300).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_pctrnk_60d_slope_v004_signal(close):
    b = close.pct_change(1).rolling(60, min_periods=50).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_pctrnk_252b_slope_v005_signal(closeadj):
    b = closeadj.pct_change(126).rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_zmom_42d_slope_v006_signal(closeadj):
    r = np.log(closeadj).diff(42)
    mu = r.rolling(504, min_periods=300).mean()
    sd = r.rolling(504, min_periods=300).std(ddof=1)
    b = (r - mu) / sd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_zmom_10d_slope_v007_signal(closeadj):
    r = closeadj.pct_change(10)
    b = (r - r.rolling(60, min_periods=50).mean()) / r.rolling(60, min_periods=50).std(ddof=1).replace(0.0, np.nan)
    d = b.diff(5)
    return (d / b.abs().rolling(5, min_periods=3).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_zmom_189d_slope_v008_signal(closeadj):
    r = closeadj.pct_change(189)
    b = (r - r.rolling(504, min_periods=300).mean()) / r.rolling(504, min_periods=300).std(ddof=1).replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_zlogm_30d_slope_v009_signal(closeadj):
    r = np.log(closeadj).diff(30)
    b = (r - r.rolling(90, min_periods=70).mean()) / r.rolling(90, min_periods=70).std(ddof=1).replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_quint_42d_slope_v010_signal(closeadj):
    rk = closeadj.pct_change(42).rolling(504, min_periods=300).rank(pct=True)
    b = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_topdec_252d_slope_v011_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    b = (rk >= 0.9).astype(float).where(~rk.isna())
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_botdec_252d_slope_v012_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    b = (rk <= 0.1).astype(float).where(~rk.isna())
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_topqnt_30d_slope_v013_signal(closeadj):
    rk = closeadj.pct_change(30).rolling(360, min_periods=250).rank(pct=True)
    b = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_umd_252d_slope_v014_signal(closeadj):
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(252))
    sd = closeadj.pct_change().rolling(252, min_periods=200).std(ddof=1) * np.sqrt(231.0)
    b = r / sd.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_umdrnk_252d_slope_v015_signal(closeadj):
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(252))
    b = r.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_umd6_126d_slope_v016_signal(closeadj):
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(126))
    sd = closeadj.pct_change().rolling(126, min_periods=100).std(ddof=1) * np.sqrt(105.0)
    b = r / sd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_sharpe_63d_slope_v017_signal(closeadj):
    r = np.log(closeadj).diff()
    b = r.rolling(63, min_periods=50).sum() / r.rolling(63, min_periods=50).std(ddof=1).replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_sharpe_252d_slope_v018_signal(closeadj):
    r = np.log(closeadj).diff()
    b = np.sqrt(252.0) * r.rolling(252, min_periods=200).mean() / r.rolling(252, min_periods=200).std(ddof=1).replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_sharprng_252d_slope_v019_signal(closeadj):
    r = np.log(closeadj).diff()
    sh20 = r.rolling(20, min_periods=15).sum() / r.rolling(20, min_periods=15).std(ddof=1).replace(0.0, np.nan)
    b = sh20.rolling(252, min_periods=200).max() - sh20.rolling(252, min_periods=200).min()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_skew_120d_slope_v020_signal(closeadj):
    b = np.log(closeadj).diff().rolling(120, min_periods=100).skew()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_kurt_120d_slope_v021_signal(closeadj):
    b = np.log(closeadj).diff().rolling(120, min_periods=100).kurt()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_tailrat_252d_slope_v022_signal(closeadj):
    r = np.log(closeadj).diff()
    def _tr(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        q1 = np.quantile(x, 0.9); q2 = np.quantile(x, 0.1)
        top = x[x >= q1].mean(); bot = x[x <= q2].mean()
        if bot == 0:
            return np.nan
        return float(top / abs(bot))
    b = r.rolling(252, min_periods=200).apply(_tr, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_winfrac_60d_slope_v023_signal(close):
    r = close.pct_change()
    w = (r > 0.0).astype(float).where(~r.isna())
    b = w.rolling(60, min_periods=50).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_outperf_120d_slope_v024_signal(closeadj):
    r = closeadj.pct_change(5)
    mu = r.rolling(120, min_periods=100).mean()
    flag = (r > mu).astype(float).where(~mu.isna())
    b = flag.rolling(120, min_periods=100).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_netwins_252d_slope_v025_signal(closeadj):
    b = np.sign(closeadj.pct_change()).rolling(252, min_periods=200).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_topqstrk_252d_slope_v026_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.8).astype(float).where(~rk.isna())
    def _s(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5: c += 1
            else: break
        return float(c)
    b = flag.rolling(100, min_periods=20).apply(_s, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_botqstrk_252d_slope_v027_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.2).astype(float).where(~rk.isna())
    def _s(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5: c += 1
            else: break
        return float(c)
    b = flag.rolling(100, min_periods=20).apply(_s, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_qtrans_60d_slope_v028_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    chg = (q != q.shift(1)).astype(float).where(~q.isna() & ~q.shift(1).isna())
    b = chg.rolling(60, min_periods=40).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_exret_3d_slope_v029_signal(close):
    r = close.pct_change(3)
    b = r - r.rolling(21, min_periods=15).mean()
    return b.diff(5).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_exretpath_60d_slope_v030_signal(closeadj):
    r = closeadj.pct_change(7)
    b = r - r.rolling(60, min_periods=50).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_spread_5_63_slope_v031_signal(closeadj):
    r = closeadj.pct_change(5)
    b = r - r.rolling(63, min_periods=50).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_spread_q1q5_60d_slope_v032_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(504, min_periods=300).rank(pct=True)
    out = pd.Series(0.0, index=closeadj.index)
    out = out.where(rk5.notna() & rk252.notna())
    cond_pos = (rk5 > 0.8) & (rk252 < 0.2)
    cond_neg = (rk5 < 0.2) & (rk252 > 0.8)
    out = out.where(~cond_pos, 1.0)
    out = out.where(~cond_neg, -1.0)
    return out.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_spread_rnk_252d_slope_v033_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    b = rk5 - rk63
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_revdis_252d_slope_v034_signal(closeadj):
    ss = np.sign(closeadj.pct_change(5)); sl = np.sign(closeadj.pct_change(252))
    b = (ss * sl).where(~ss.isna() & ~sl.isna())
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_strev_zdif_15d_slope_v035_signal(close):
    r = close.pct_change(1)
    z15 = (r - r.rolling(15, min_periods=15).mean()) / r.rolling(15, min_periods=15).std(ddof=1).replace(0.0, np.nan)
    z5 = (r - r.rolling(5, min_periods=5).mean()) / r.rolling(5, min_periods=5).std(ddof=1).replace(0.0, np.nan)
    b = -(z15 - z5)
    return b.diff(5).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_arctan_15d_slope_v036_signal(close):
    s = np.sign(close.pct_change()).rolling(15, min_periods=15).sum() / np.sqrt(15.0)
    b = np.arctan(s)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_tanh_top_60d_slope_v037_signal(closeadj):
    r = closeadj.pct_change(5)
    rk = r.rolling(60, min_periods=50).rank(pct=True)
    top = (rk >= 0.9).astype(float).where(~rk.isna())
    bot = (rk <= 0.1).astype(float).where(~rk.isna())
    diff_b = top.rolling(60, min_periods=50).sum() - bot.rolling(60, min_periods=50).sum()
    b = np.tanh(diff_b / 6.0)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_sigm_rkjmp_252d_slope_v038_signal(closeadj):
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    d = rk21 - rk63
    b = 1.0 / (1.0 + np.exp(-5.0 * d))
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_drawup_252d_slope_v039_signal(closeadj):
    mn = closeadj.rolling(252, min_periods=200).min()
    du = closeadj / mn.replace(0.0, np.nan) - 1.0
    b = du.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_drawdn_252d_slope_v040_signal(closeadj):
    mx = closeadj.rolling(252, min_periods=200).max()
    dd = closeadj / mx.replace(0.0, np.nan) - 1.0
    b = dd.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_athgap_120d_slope_v041_signal(closeadj):
    def _ds(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)):
            return np.nan
        return float(len(x) - 1 - int(np.argmax(x)))
    b = closeadj.rolling(120, min_periods=100).apply(_ds, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rough_120d_slope_v042_signal(closeadj):
    r = closeadj.pct_change()
    num = r.abs().rolling(120, min_periods=100).sum()
    den = (closeadj / closeadj.shift(120) - 1.0).abs()
    b = num / den.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_horizonslp_252d_slope_v043_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk126 = closeadj.pct_change(126).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    lw = np.log(np.array([5.0, 21.0, 63.0, 126.0, 252.0])); lw_m = lw.mean()
    den = float(((lw - lw_m) ** 2).sum())
    df = pd.concat([rk5, rk21, rk63, rk126, rk252], axis=1)
    def _row(arr):
        if np.any(~np.isfinite(arr)): return np.nan
        ym = arr.mean()
        return float(((lw - lw_m) * (arr - ym)).sum() / den)
    b = df.apply(lambda row: _row(row.to_numpy(dtype=float)), axis=1)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_avgabsret_30d_slope_v044_signal(closeadj):
    r = np.log(closeadj).diff().abs()
    b = r.rolling(30, min_periods=25).mean() / r.rolling(252, min_periods=200).mean().replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_volnormatr_30d_slope_v045_signal(high, low, closeadj):
    r = np.log(closeadj).diff(30)
    atr = (high - low).rolling(30, min_periods=25).mean() / closeadj
    b = r / atr.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_mks_60d_slope_v046_signal(closeadj):
    n = 60
    r = np.log(closeadj).diff()
    norm = n * (n - 1) / 2.0
    def _mk(x):
        if np.any(~np.isfinite(x)): return np.nan
        s = 0
        for i in range(n - 1):
            d = x[i + 1:] - x[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return s / norm
    b = r.rolling(n, min_periods=n).apply(_mk, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_timeintop_252d_slope_v047_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.9).astype(float).where(~rk.isna())
    b = flag.rolling(252, min_periods=200).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_timeinbot_252d_slope_v048_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.1).astype(float).where(~rk.isna())
    b = flag.rolling(252, min_periods=200).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_decnet_252d_slope_v049_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    top = (rk >= 0.9).astype(float).where(~rk.isna())
    bot = (rk <= 0.1).astype(float).where(~rk.isna())
    b = (top - bot).rolling(252, min_periods=200).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_dssup_252d_slope_v050_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.9).astype(float).where(~rk.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 252.0
        return float(len(x) - 1 - idx[-1])
    b = flag.rolling(252, min_periods=200).apply(_ds, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_dssdn_252d_slope_v051_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.1).astype(float).where(~rk.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 252.0
        return float(len(x) - 1 - idx[-1])
    b = flag.rolling(252, min_periods=200).apply(_ds, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rkretvol_252d_slope_v052_signal(closeadj):
    r = closeadj.pct_change(21); v = closeadj.pct_change().rolling(60, min_periods=50).std(ddof=1)
    rkr = r.rolling(252, min_periods=200).rank(pct=True); rkv = v.rolling(252, min_periods=200).rank(pct=True)
    b = rkr / (rkv + 0.05)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_idiosig_252d_slope_v053_signal(closeadj):
    def _c(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)): return np.nan
        n = len(x); t = np.arange(n, dtype=float)
        tm = t.mean(); xm = x.mean()
        slp = float(((t - tm) * (x - xm)).sum() / ((t - tm) ** 2).sum())
        resid = x - (xm + slp * (t - tm))
        sd = resid.std(ddof=1)
        if sd <= 0: return np.nan
        return float(resid[-1] / sd)
    b = np.log(closeadj).rolling(252, min_periods=200).apply(_c, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_perswinr_252d_slope_v054_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    top = (q >= 5.0).astype(float).where(~q.isna()); bot = (q <= 1.0).astype(float).where(~q.isna())
    t60 = top.rolling(60, min_periods=50).sum(); b60 = bot.rolling(60, min_periods=50).sum()
    b = np.sign(t60 - b60)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_qjump_60d_slope_v055_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    jmp = (q - q.shift(1)).abs()
    b = jmp.rolling(60, min_periods=50).mean()
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_avgrnk_252d_slope_v056_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    b = (rk5 + rk21 + rk63 + rk252) / 4.0
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_minrnk_252d_slope_v057_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    b = pd.concat([rk5, rk21, rk63, rk252], axis=1).min(axis=1)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_maxrnk_252d_slope_v058_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    b = pd.concat([rk5, rk21, rk63, rk252], axis=1).max(axis=1)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rkdisp_252d_slope_v059_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(252, min_periods=200).rank(pct=True)
    b = pd.concat([rk5, rk21, rk63, rk252], axis=1).std(axis=1, ddof=1)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_cumrkmean_60d_slope_v060_signal(closeadj):
    rk = closeadj.pct_change().rolling(60, min_periods=50).rank(pct=True)
    b = rk.rolling(60, min_periods=50).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_matrnk_85d_slope_v061_signal(high, low, closeadj):
    r = closeadj.pct_change(85)
    prev = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    atr = tr.rolling(85, min_periods=60).mean()
    ratio = r / atr.replace(0.0, np.nan) * closeadj
    b = ratio.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_winstrk_60d_slope_v062_signal(close):
    r = close.pct_change()
    flag = (r > 0.0).astype(float).where(~r.isna())
    def _s(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5: c += 1
            else: break
        return float(c)
    b = flag.rolling(60, min_periods=10).apply(_s, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_losstrk_60d_slope_v063_signal(close):
    r = close.pct_change()
    flag = (r < 0.0).astype(float).where(~r.isna())
    def _s(x):
        c = 0
        for v in x[::-1]:
            if v > 0.5: c += 1
            else: break
        return float(c)
    b = flag.rolling(60, min_periods=10).apply(_s, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_madz_36d_slope_v064_signal(closeadj):
    r = closeadj.pct_change(15)
    med = r.rolling(36, min_periods=30).median()
    mad = (r - med).abs().rolling(36, min_periods=30).median()
    b = (r - med) / (1.4826 * mad).replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_skewret_60d_slope_v065_signal(closeadj):
    b = closeadj.pct_change(5).rolling(60, min_periods=50).skew()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_trimrnk_170d_slope_v066_signal(closeadj):
    r = closeadj.pct_change(170)
    def _wrnk(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)): return np.nan
        q05, q95 = np.quantile(x, 0.05), np.quantile(x, 0.95)
        xw = np.clip(x, q05, q95); v = xw[-1]
        return float((xw < v).sum() / len(xw))
    b = r.rolling(252, min_periods=200).apply(_wrnk, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_sortino_120d_slope_v067_signal(closeadj):
    r = np.log(closeadj).diff()
    num = r.rolling(120, min_periods=100).sum()
    neg = r.where(r < 0.0)
    dsd = neg.rolling(120, min_periods=50).std(ddof=1)
    b = num / dsd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_calmar_252d_slope_v068_signal(closeadj):
    r = np.log(closeadj).diff(252)
    mx = closeadj.rolling(252, min_periods=200).max()
    dd = (closeadj / mx - 1.0).rolling(252, min_periods=200).min().abs()
    b = r / dd.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_skewrnk_252d_slope_v069_signal(closeadj):
    sk = np.log(closeadj).diff().rolling(120, min_periods=100).skew()
    b = sk.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_tstatdiff_120d_slope_v070_signal(closeadj):
    r = np.log(closeadj).diff()
    t30 = np.sqrt(30.0) * r.rolling(30, min_periods=25).mean() / r.rolling(30, min_periods=25).std(ddof=1).replace(0.0, np.nan)
    t120 = np.sqrt(120.0) * r.rolling(120, min_periods=100).mean() / r.rolling(120, min_periods=100).std(ddof=1).replace(0.0, np.nan)
    b = t30 - t120
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_updnvol_252d_slope_v071_signal(closeadj):
    r = closeadj.pct_change(5)
    su = r.where(r > 0.0).rolling(252, min_periods=100).std(ddof=1)
    sd = r.where(r < 0.0).rolling(252, min_periods=100).std(ddof=1)
    ratio = su / sd.replace(0.0, np.nan)
    b = ratio.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_cmomag_120d_slope_v072_signal(closeadj):
    r = closeadj.diff()
    g = r.where(r > 0.0, 0.0).rolling(40, min_periods=30).sum()
    l = (-r.where(r < 0.0, 0.0)).rolling(40, min_periods=30).sum()
    cmo = 100.0 * (g - l) / (g + l).replace(0.0, np.nan)
    b = cmo.abs().rolling(120, min_periods=100).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_selfbeta_120d_slope_v073_signal(closeadj):
    r = closeadj.pct_change()
    lr = r.shift(1)
    mu_x = lr.rolling(120, min_periods=100).mean()
    mu_y = r.rolling(120, min_periods=100).mean()
    cov = (r * lr).rolling(120, min_periods=100).mean() - mu_x * mu_y
    var = (lr * lr).rolling(120, min_periods=100).mean() - mu_x * mu_x
    b = cov / var.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_decagree_252d_slope_v074_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(252, min_periods=200).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    bt = ((rk5 >= 0.8) & (rk21 >= 0.8)).astype(float).where(~rk5.isna() & ~rk21.isna())
    bb = ((rk5 <= 0.2) & (rk21 <= 0.2)).astype(float).where(~rk5.isna() & ~rk21.isna())
    b = (bt - bb).rolling(60, min_periods=40).sum()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_shrink_q5q1_252d_slope_v075_signal(closeadj):
    r = np.log(closeadj).diff(63)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.8).astype(float).where(~rk.isna()) - (rk <= 0.2).astype(float).where(~rk.isna())
    v = closeadj.pct_change().rolling(63, min_periods=50).std(ddof=1) * np.sqrt(252.0)
    w = 252.0 / (252.0 + 5.0 * v)
    b = flag * r * w
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_aboverm_120d_slope_v076_signal(closeadj):
    med = closeadj.rolling(120, min_periods=100).median()
    flag = (closeadj > med).astype(float).where(~med.isna())
    b = flag.rolling(120, min_periods=100).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_abovemean_252d_slope_v077_signal(closeadj):
    r = closeadj.pct_change(21); mu = r.rolling(252, min_periods=200).mean()
    flag = (r > mu).astype(float).where(~mu.isna())
    b = flag.rolling(252, min_periods=200).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_aboveewma_60d_slope_v078_signal(closeadj):
    ema = closeadj.ewm(span=30, adjust=False, min_periods=25).mean()
    flag = (closeadj > ema).astype(float).where(~ema.isna())
    b = flag.rolling(60, min_periods=50).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_skewlog_60d_slope_v079_signal(closeadj):
    b = np.log(closeadj).diff().rolling(60, min_periods=50).skew()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_kurtlog_60d_slope_v080_signal(closeadj):
    b = np.log(closeadj).diff().rolling(60, min_periods=50).kurt()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_iqr_60d_slope_v081_signal(closeadj):
    r = np.log(closeadj).diff()
    q75 = r.rolling(60, min_periods=50).quantile(0.75)
    q25 = r.rolling(60, min_periods=50).quantile(0.25)
    sd = r.rolling(60, min_periods=50).std(ddof=1)
    b = (q75 - q25) / sd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_cumupret_60d_slope_v082_signal(closeadj):
    r = np.log(closeadj).diff()
    pos = r.where(r > 0.0, 0.0).rolling(60, min_periods=50).sum()
    tot = r.abs().rolling(60, min_periods=50).sum()
    b = pos / tot.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_dnconc_60d_slope_v083_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0.0)
    sq = (neg ** 2).rolling(60, min_periods=15).sum()
    abs_sum = neg.abs().rolling(60, min_periods=15).sum()
    b = sq / (abs_sum ** 2).replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_zeroret_120d_slope_v084_signal(closeadj):
    sg = np.sign(closeadj.diff())
    flip = (sg != sg.shift(1)).astype(float).where(~sg.isna() & ~sg.shift(1).isna())
    b = flip.rolling(120, min_periods=100).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_medxr_252d_slope_v085_signal(closeadj):
    r = closeadj.pct_change(21); med = r.rolling(252, min_periods=200).median()
    sg = np.sign(r - med)
    flip = (sg != sg.shift(1)).astype(float).where(~sg.isna() & ~sg.shift(1).isna())
    b = flip.rolling(252, min_periods=200).sum()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rrk21_252d_slope_v086_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    b = rk.rolling(252, min_periods=200).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rrkstd_252d_slope_v087_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    b = rk.rolling(252, min_periods=200).std(ddof=1)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_umd9_189d_slope_v088_signal(closeadj):
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(189))
    sd = closeadj.pct_change().rolling(189, min_periods=150).std(ddof=1) * np.sqrt(168.0)
    b = r / sd.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_umd3_84d_slope_v089_signal(closeadj):
    r = np.log(closeadj.shift(21)) - np.log(closeadj.shift(84))
    sd = closeadj.pct_change().rolling(84, min_periods=63).std(ddof=1) * np.sqrt(63.0)
    b = r / sd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_umdcheap_504d_slope_v090_signal(closeadj):
    r1 = np.log(closeadj).diff(21); r12 = np.log(closeadj).diff(252)
    b = r12 - r1
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_volofrnk_252d_slope_v091_signal(closeadj):
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    b = rk.rolling(252, min_periods=200).std(ddof=1)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_volofz_120d_slope_v092_signal(closeadj):
    r = closeadj.pct_change(21)
    z = (r - r.rolling(60, min_periods=50).mean()) / r.rolling(60, min_periods=50).std(ddof=1).replace(0.0, np.nan)
    b = z.rolling(120, min_periods=100).std(ddof=1)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_lpm_120d_slope_v093_signal(closeadj):
    r = closeadj.pct_change()
    neg = r.where(r < 0.0, 0.0) ** 2
    b = neg.rolling(120, min_periods=100).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_upmratio_120d_slope_v094_signal(closeadj):
    r = closeadj.pct_change()
    upm = (r.where(r > 0.0, 0.0) ** 2).rolling(120, min_periods=100).mean()
    lpm = (r.where(r < 0.0, 0.0) ** 2).rolling(120, min_periods=100).mean()
    b = upm / lpm.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_skipmo_126d_slope_v095_signal(closeadj):
    b = np.log(closeadj.shift(5)) - np.log(closeadj.shift(126))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_skipmovrnk_252d_slope_v096_signal(closeadj):
    r = np.log(closeadj.shift(10)) - np.log(closeadj.shift(252))
    v = np.log(closeadj).diff().rolling(252, min_periods=200).std(ddof=1) * np.sqrt(242.0)
    sig = r / v.replace(0.0, np.nan)
    b = sig.rolling(504, min_periods=300).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_ewmaratio_60d_slope_v097_signal(closeadj):
    ema = closeadj.ewm(span=60, adjust=False, min_periods=40).mean()
    b = np.log(closeadj / ema.replace(0.0, np.nan)).rolling(252, min_periods=200).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_topqdays_120d_slope_v098_signal(closeadj):
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    flag = (rk >= 0.8).astype(float).where(~rk.isna())
    b = flag.rolling(120, min_periods=100).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_botqdays_120d_slope_v099_signal(closeadj):
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    flag = (rk <= 0.2).astype(float).where(~rk.isna())
    b = flag.rolling(120, min_periods=100).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rkmkscore_60d_slope_v100_signal(closeadj):
    n = 60
    rk = closeadj.pct_change().rolling(60, min_periods=50).rank(pct=True)
    norm = n * (n - 1) / 2.0
    def _mk(x):
        if np.any(~np.isfinite(x)): return np.nan
        s = 0
        for i in range(n - 1):
            d = x[i + 1:] - x[i]
            s += int(np.sum(d > 0) - np.sum(d < 0))
        return s / norm
    b = rk.rolling(n, min_periods=n).apply(_mk, raw=True)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_atrnorm_63d_slope_v101_signal(high, low, closeadj):
    r = np.log(closeadj).diff(63)
    prev = closeadj.shift(1)
    tr = pd.concat([(high - low).abs(), (high - prev).abs(), (low - prev).abs()], axis=1).max(axis=1)
    avgtr = (tr / closeadj).rolling(63, min_periods=50).mean()
    ratio = r / avgtr.replace(0.0, np.nan)
    b = ratio.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_signmom_60d_slope_v102_signal(closeadj):
    r = closeadj.pct_change()
    pos = r.where(r > 0.0, 0.0).rolling(60, min_periods=50).sum()
    neg = (-r.where(r < 0.0, 0.0)).rolling(60, min_periods=50).sum()
    tot = pos + neg
    sig = (pos - neg) / tot.replace(0.0, np.nan)
    mu = sig.rolling(252, min_periods=200).mean(); sd = sig.rolling(252, min_periods=200).std(ddof=1)
    b = (sig - mu) / sd.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_winsize_60d_slope_v103_signal(closeadj):
    r = closeadj.pct_change()
    up = r.where(r > 0.0).abs().rolling(60, min_periods=15).mean()
    dn = r.where(r < 0.0).abs().rolling(60, min_periods=15).mean()
    b = up / dn.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_pathq_252d_slope_v104_signal(closeadj):
    r = closeadj.pct_change(21)
    pos = (r > 0.0).astype(float).where(~r.isna())
    b = pos.rolling(252, min_periods=200).mean()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_state_252d_slope_v105_signal(closeadj):
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(504, min_periods=300).rank(pct=True)
    def _bk(x):
        out = pd.Series(0.0, index=x.index)
        out = out.where(x.isna(), 1.0)
        out = out.where(~(x >= 0.66), 3.0)
        out = out.where(~((x >= 0.33) & (x < 0.66)), 2.0)
        return out
    b1 = _bk(rk21); b2 = _bk(rk252)
    b = (b1 - 1.0) * 3.0 + b2
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_ddmag_252d_slope_v106_signal(closeadj):
    mx = closeadj.rolling(252, min_periods=200).max()
    dd = closeadj / mx - 1.0
    sd = np.log(closeadj).diff().rolling(252, min_periods=200).std(ddof=1) * np.sqrt(252.0)
    b = dd / sd.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_volwret_21d_slope_v108_signal(close, volume):
    r = np.log(close).diff()
    rv = (r * volume).rolling(21, min_periods=15).sum()
    v = volume.rolling(21, min_periods=15).sum()
    b = rv / v.replace(0.0, np.nan)
    return b.diff(10).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_volwretrnk_63d_slope_v109_signal(closeadj, volume):
    r = np.log(closeadj).diff()
    rv = (r * volume).rolling(63, min_periods=50).sum()
    v = volume.rolling(63, min_periods=50).sum()
    sig = rv / v.replace(0.0, np.nan)
    b = sig.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_q90_120d_slope_v110_signal(closeadj):
    b = np.log(closeadj).diff().rolling(120, min_periods=100).quantile(0.9)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_q10_120d_slope_v111_signal(closeadj):
    b = np.log(closeadj).diff().rolling(120, min_periods=100).quantile(0.1)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_q90q10_120d_slope_v112_signal(closeadj):
    r = np.log(closeadj).diff()
    b = r.rolling(120, min_periods=100).quantile(0.9) + r.rolling(120, min_periods=100).quantile(0.1)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_persisttrend_60d_slope_v113_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(60, min_periods=50).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(126, min_periods=100).rank(pct=True)
    pos = ((rk5 > 0.5) & (rk21 > 0.5) & (rk63 > 0.5)).astype(float)
    neg = ((rk5 < 0.5) & (rk21 < 0.5) & (rk63 < 0.5)).astype(float)
    mask = rk5.isna() | rk21.isna() | rk63.isna()
    b = (pos - neg).where(~mask)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_maxddrnk_252d_slope_v114_signal(closeadj):
    mx = closeadj.rolling(60, min_periods=50).max()
    dd = closeadj / mx - 1.0
    minDD = dd.rolling(60, min_periods=50).min().abs()
    b = minDD.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_dsbq_252d_slope_v115_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk >= 0.8).astype(float).where(~rk.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 252.0
        return float(len(x) - 1 - idx[-1])
    b = flag.rolling(252, min_periods=200).apply(_ds, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_dswq_252d_slope_v116_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    flag = (rk <= 0.2).astype(float).where(~rk.isna())
    def _ds(x):
        idx = np.where(x > 0.5)[0]
        if idx.size == 0: return 252.0
        return float(len(x) - 1 - idx[-1])
    b = flag.rolling(252, min_periods=200).apply(_ds, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_xhagree_60d_slope_v117_signal(closeadj):
    s5 = np.sign(closeadj.pct_change(5)); s21 = np.sign(closeadj.pct_change(21)); s63 = np.sign(closeadj.pct_change(63))
    agree = (s5 == s21).astype(float) + (s21 == s63).astype(float) + (s5 == s63).astype(float)
    sgn_total = s5 + s21 + s63
    out = (agree - 1.5) * np.sign(sgn_total)
    mask = s5.isna() | s21.isna() | s63.isna()
    b = out.where(~mask).rolling(60, min_periods=50).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rcumrnk_60d_slope_v118_signal(closeadj):
    n = 60
    def _rc(x):
        if np.any(~np.isfinite(x)): return np.nan
        rx = pd.Series(x).rank().to_numpy()
        rt = np.arange(1, n + 1, dtype=float)
        if rx.std() <= 0: return np.nan
        return float(np.corrcoef(rx, rt)[0, 1])
    b = closeadj.rolling(n, min_periods=n).apply(_rc, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_tailloss_252d_slope_v119_signal(closeadj):
    r = np.log(closeadj).diff()
    def _cv(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)): return np.nan
        q = np.quantile(x, 0.05); return float(x[x <= q].mean())
    b = r.rolling(252, min_periods=200).apply(_cv, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_tailgain_252d_slope_v120_signal(closeadj):
    r = np.log(closeadj).diff()
    def _cv(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)): return np.nan
        q = np.quantile(x, 0.95); return float(x[x >= q].mean())
    b = r.rolling(252, min_periods=200).apply(_cv, raw=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_geoarith_rnk_252d_slope_v121_signal(closeadj):
    r_simple = closeadj.pct_change(); r_log = np.log(closeadj).diff()
    drag = r_simple.rolling(60, min_periods=50).mean() - r_log.rolling(60, min_periods=50).mean()
    b = drag.rolling(504, min_periods=300).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_negskewreg_120d_slope_v122_signal(closeadj):
    sk = np.log(closeadj).diff().rolling(120, min_periods=100).skew()
    med = sk.rolling(252, min_periods=200).median()
    b = np.sign(sk - med)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_hilopos_252d_slope_v123_signal(high, low, closeadj):
    hh = high.rolling(252, min_periods=200).max(); ll = low.rolling(252, min_periods=200).min()
    pos = (closeadj - ll) / (hh - ll).replace(0.0, np.nan)
    b = pos.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_trendbeta_120d_slope_v124_signal(closeadj):
    n = 120
    sma60 = closeadj.rolling(60, min_periods=50).mean()
    mu_x = sma60.rolling(n, min_periods=100).mean(); mu_y = closeadj.rolling(n, min_periods=100).mean()
    cov = (closeadj * sma60).rolling(n, min_periods=100).mean() - mu_x * mu_y
    var = (sma60 * sma60).rolling(n, min_periods=100).mean() - mu_x * mu_x
    b = cov / var.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_accelrnk_60d_slope_v125_signal(closeadj):
    r = closeadj.pct_change(21)
    accel = r - r.shift(21)
    b = accel.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_horizoncoh_120d_slope_v126_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(60, min_periods=50).rank(pct=True)
    rk63 = closeadj.pct_change(63).rolling(126, min_periods=100).rank(pct=True)
    comp = (rk5 + rk21 + rk63 - 1.5)
    sd = comp.rolling(120, min_periods=100).std(ddof=1)
    b = comp / sd.replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_maxruna_120d_slope_v127_signal(close):
    r = close.pct_change()
    flag = (r > 0.0).astype(float).where(~r.isna())
    def _mr(x):
        m = 0; c = 0
        for v in x:
            if v > 0.5:
                c += 1
                if c > m: m = c
            else:
                c = 0
        return float(m)
    b = flag.rolling(120, min_periods=100).apply(_mr, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_maxrunb_120d_slope_v128_signal(close):
    r = close.pct_change()
    flag = (r < 0.0).astype(float).where(~r.isna())
    def _mr(x):
        m = 0; c = 0
        for v in x:
            if v > 0.5:
                c += 1
                if c > m: m = c
            else:
                c = 0
        return float(m)
    b = flag.rolling(120, min_periods=100).apply(_mr, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_signac_60d_slope_v129_signal(closeadj):
    sg = np.sign(closeadj.diff())
    def _ac(x):
        x = np.asarray(x, dtype=float)
        if np.any(~np.isfinite(x)): return np.nan
        a = x[:-1]; b2 = x[1:]
        if a.std() <= 0 or b2.std() <= 0: return np.nan
        return float(np.corrcoef(a, b2)[0, 1])
    b = sg.rolling(60, min_periods=50).apply(_ac, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_wtrnk_60d_slope_v130_signal(closeadj):
    rk = closeadj.pct_change().rolling(60, min_periods=50).rank(pct=True)
    w = np.arange(1, 61, dtype=float); wsum = w.sum()
    def _wm(x):
        if np.any(~np.isfinite(x)): return np.nan
        return float((x * w).sum() / wsum)
    b = rk.rolling(60, min_periods=60).apply(_wm, raw=True)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_riskp_120d_slope_v131_signal(closeadj):
    r5 = closeadj.pct_change(5)
    sd = closeadj.pct_change().rolling(5, min_periods=5).std(ddof=1)
    sig = r5 / sd.replace(0.0, np.nan)
    b = sig.rolling(252, min_periods=200).rank(pct=True)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_largeret_60d_slope_v132_signal(closeadj):
    r = closeadj.pct_change().abs()
    q90 = r.rolling(60, min_periods=50).quantile(0.9)
    flag = (r > q90).astype(float).where(~q90.isna())
    b = flag.rolling(60, min_periods=50).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_above2sd_120d_slope_v133_signal(closeadj):
    r = closeadj.pct_change()
    sd = r.rolling(120, min_periods=100).std(ddof=1)
    flag = (r > 2.0 * sd).astype(float).where(~sd.isna())
    b = flag.rolling(120, min_periods=100).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_below2sd_120d_slope_v134_signal(closeadj):
    r = closeadj.pct_change()
    sd = r.rolling(120, min_periods=100).std(ddof=1)
    flag = (r < -2.0 * sd).astype(float).where(~sd.isna())
    b = flag.rolling(120, min_periods=100).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_geoexcess_120d_slope_v135_signal(closeadj):
    b = np.log(closeadj) - 2.0 * np.log(closeadj.shift(63)) + np.log(closeadj.shift(126))
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_cagrdiff_252d_slope_v136_signal(closeadj):
    c63 = (np.log(closeadj) - np.log(closeadj.shift(63))) * (252.0 / 63.0)
    c252 = np.log(closeadj) - np.log(closeadj.shift(252))
    b = c63 - c252
    d = b.diff(63)
    return (d / b.abs().rolling(63, min_periods=30).mean().replace(0.0, np.nan)).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_zewma_252d_slope_v137_signal(closeadj):
    r = closeadj.pct_change(21)
    mu = r.ewm(span=60, adjust=False, min_periods=40).mean()
    sd = r.ewm(span=60, adjust=False, min_periods=40).std(bias=False)
    b = (r - mu) / sd.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_volqret_252d_slope_v138_signal(closeadj):
    rkr = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    rkv = closeadj.pct_change().rolling(60, min_periods=50).std(ddof=1).rolling(252, min_periods=200).rank(pct=True)
    b = rkr - rkv
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_qmeanrun_60d_slope_v139_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    q = np.ceil(rk * 5.0).clip(lower=1.0, upper=5.0)
    b = q.rolling(60, min_periods=40).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_contrev_60d_slope_v140_signal(closeadj):
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    dist_now = (rk - 0.5).abs(); dist_prev = (rk.shift(1) - 0.5).abs()
    inc = (dist_now > dist_prev).astype(float).where(~dist_now.isna() & ~dist_prev.isna())
    dec = (dist_now < dist_prev).astype(float).where(~dist_now.isna() & ~dist_prev.isna())
    b = (inc - dec).rolling(60, min_periods=50).sum()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_zerox_252d_slope_v141_signal(closeadj):
    r = closeadj.pct_change(21)
    centered = r - r.rolling(252, min_periods=200).mean()
    sg = np.sign(centered)
    flip = (sg != sg.shift(1)).astype(float).where(~sg.isna() & ~sg.shift(1).isna())
    b = flip.rolling(252, min_periods=200).sum()
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rkdev_60d_slope_v142_signal(closeadj):
    rk = closeadj.pct_change().rolling(60, min_periods=50).rank(pct=True)
    b = (rk - 0.5).abs()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_condrkpos_120d_slope_v143_signal(closeadj):
    r = closeadj.pct_change(21)
    rk = r.rolling(252, min_periods=200).rank(pct=True)
    masked = rk.where(r > 0.0)
    b = masked.rolling(120, min_periods=20).mean()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_xhcorr_60d_slope_v144_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(126, min_periods=100).rank(pct=True)
    mu5 = rk5.rolling(60, min_periods=50).mean(); mu21 = rk21.rolling(60, min_periods=50).mean()
    cov = (rk5 * rk21).rolling(60, min_periods=50).mean() - mu5 * mu21
    s5 = rk5.rolling(60, min_periods=50).std(ddof=1); s21 = rk21.rolling(60, min_periods=50).std(ddof=1)
    b = cov / (s5 * s21).replace(0.0, np.nan)
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_skewp_252d_slope_v145_signal(closeadj):
    r = np.log(closeadj).diff()
    mu = r.rolling(252, min_periods=200).mean(); md = r.rolling(252, min_periods=200).median()
    sd = r.rolling(252, min_periods=200).std(ddof=1)
    b = 3.0 * (mu - md) / sd.replace(0.0, np.nan)
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rkgap_5_21_slope_v146_signal(closeadj):
    rk5 = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    b = rk5 - rk21
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rkgap_63_252_slope_v147_signal(closeadj):
    rk63 = closeadj.pct_change(63).rolling(252, min_periods=200).rank(pct=True)
    rk252 = closeadj.pct_change(252).rolling(504, min_periods=300).rank(pct=True)
    b = rk63 - rk252
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_blendrk_252d_slope_v148_signal(closeadj):
    rk252 = closeadj.pct_change(252).rolling(504, min_periods=300).rank(pct=True)
    rk21 = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    b = 0.7 * rk252 + 0.3 * rk21
    return b.diff(63).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_minrkdis_252d_slope_v149_signal(closeadj):
    rk = closeadj.pct_change(21).rolling(252, min_periods=200).rank(pct=True)
    b = rk - rk.rolling(252, min_periods=200).min()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
def f15xm_f15_cross_sectional_momentum_rkrng_120d_slope_v150_signal(closeadj):
    rk = closeadj.pct_change(5).rolling(60, min_periods=50).rank(pct=True)
    b = rk.rolling(120, min_periods=100).max() - rk.rolling(120, min_periods=100).min()
    return b.diff(21).replace([np.inf, -np.inf], np.nan)
_FUNCS = [
    (f15xm_f15_cross_sectional_momentum_pctrnk_252d_slope_v001_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_pctrnk_126d_slope_v002_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_pctrnk_504d_slope_v003_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_pctrnk_60d_slope_v004_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_pctrnk_252b_slope_v005_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_zmom_42d_slope_v006_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_zmom_10d_slope_v007_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_zmom_189d_slope_v008_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_zlogm_30d_slope_v009_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_quint_42d_slope_v010_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_topdec_252d_slope_v011_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_botdec_252d_slope_v012_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_topqnt_30d_slope_v013_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_umd_252d_slope_v014_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_umdrnk_252d_slope_v015_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_umd6_126d_slope_v016_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_sharpe_63d_slope_v017_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_sharpe_252d_slope_v018_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_sharprng_252d_slope_v019_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_skew_120d_slope_v020_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_kurt_120d_slope_v021_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_tailrat_252d_slope_v022_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_winfrac_60d_slope_v023_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_outperf_120d_slope_v024_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_netwins_252d_slope_v025_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_topqstrk_252d_slope_v026_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_botqstrk_252d_slope_v027_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_qtrans_60d_slope_v028_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_exret_3d_slope_v029_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_exretpath_60d_slope_v030_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_spread_5_63_slope_v031_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_spread_q1q5_60d_slope_v032_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_spread_rnk_252d_slope_v033_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_revdis_252d_slope_v034_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_strev_zdif_15d_slope_v035_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_arctan_15d_slope_v036_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_tanh_top_60d_slope_v037_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_sigm_rkjmp_252d_slope_v038_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_drawup_252d_slope_v039_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_drawdn_252d_slope_v040_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_athgap_120d_slope_v041_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rough_120d_slope_v042_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_horizonslp_252d_slope_v043_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_avgabsret_30d_slope_v044_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_volnormatr_30d_slope_v045_signal, ["high", "low", "closeadj"]),
    (f15xm_f15_cross_sectional_momentum_mks_60d_slope_v046_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_timeintop_252d_slope_v047_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_timeinbot_252d_slope_v048_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_decnet_252d_slope_v049_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_dssup_252d_slope_v050_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_dssdn_252d_slope_v051_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rkretvol_252d_slope_v052_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_idiosig_252d_slope_v053_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_perswinr_252d_slope_v054_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_qjump_60d_slope_v055_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_avgrnk_252d_slope_v056_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_minrnk_252d_slope_v057_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_maxrnk_252d_slope_v058_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rkdisp_252d_slope_v059_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_cumrkmean_60d_slope_v060_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_matrnk_85d_slope_v061_signal, ["high", "low", "closeadj"]),
    (f15xm_f15_cross_sectional_momentum_winstrk_60d_slope_v062_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_losstrk_60d_slope_v063_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_madz_36d_slope_v064_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_skewret_60d_slope_v065_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_trimrnk_170d_slope_v066_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_sortino_120d_slope_v067_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_calmar_252d_slope_v068_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_skewrnk_252d_slope_v069_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_tstatdiff_120d_slope_v070_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_updnvol_252d_slope_v071_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_cmomag_120d_slope_v072_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_selfbeta_120d_slope_v073_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_decagree_252d_slope_v074_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_shrink_q5q1_252d_slope_v075_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_aboverm_120d_slope_v076_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_abovemean_252d_slope_v077_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_aboveewma_60d_slope_v078_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_skewlog_60d_slope_v079_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_kurtlog_60d_slope_v080_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_iqr_60d_slope_v081_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_cumupret_60d_slope_v082_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_dnconc_60d_slope_v083_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_zeroret_120d_slope_v084_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_medxr_252d_slope_v085_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rrk21_252d_slope_v086_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rrkstd_252d_slope_v087_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_umd9_189d_slope_v088_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_umd3_84d_slope_v089_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_umdcheap_504d_slope_v090_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_volofrnk_252d_slope_v091_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_volofz_120d_slope_v092_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_lpm_120d_slope_v093_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_upmratio_120d_slope_v094_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_skipmo_126d_slope_v095_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_skipmovrnk_252d_slope_v096_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_ewmaratio_60d_slope_v097_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_topqdays_120d_slope_v098_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_botqdays_120d_slope_v099_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rkmkscore_60d_slope_v100_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_atrnorm_63d_slope_v101_signal, ["high", "low", "closeadj"]),
    (f15xm_f15_cross_sectional_momentum_signmom_60d_slope_v102_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_winsize_60d_slope_v103_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_pathq_252d_slope_v104_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_state_252d_slope_v105_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_ddmag_252d_slope_v106_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_volwret_21d_slope_v108_signal, ["close", "volume"]),
    (f15xm_f15_cross_sectional_momentum_volwretrnk_63d_slope_v109_signal, ["closeadj", "volume"]),
    (f15xm_f15_cross_sectional_momentum_q90_120d_slope_v110_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_q10_120d_slope_v111_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_q90q10_120d_slope_v112_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_persisttrend_60d_slope_v113_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_maxddrnk_252d_slope_v114_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_dsbq_252d_slope_v115_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_dswq_252d_slope_v116_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_xhagree_60d_slope_v117_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rcumrnk_60d_slope_v118_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_tailloss_252d_slope_v119_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_tailgain_252d_slope_v120_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_geoarith_rnk_252d_slope_v121_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_negskewreg_120d_slope_v122_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_hilopos_252d_slope_v123_signal, ["high", "low", "closeadj"]),
    (f15xm_f15_cross_sectional_momentum_trendbeta_120d_slope_v124_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_accelrnk_60d_slope_v125_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_horizoncoh_120d_slope_v126_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_maxruna_120d_slope_v127_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_maxrunb_120d_slope_v128_signal, ["close"]),
    (f15xm_f15_cross_sectional_momentum_signac_60d_slope_v129_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_wtrnk_60d_slope_v130_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_riskp_120d_slope_v131_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_largeret_60d_slope_v132_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_above2sd_120d_slope_v133_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_below2sd_120d_slope_v134_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_geoexcess_120d_slope_v135_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_cagrdiff_252d_slope_v136_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_zewma_252d_slope_v137_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_volqret_252d_slope_v138_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_qmeanrun_60d_slope_v139_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_contrev_60d_slope_v140_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_zerox_252d_slope_v141_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rkdev_60d_slope_v142_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_condrkpos_120d_slope_v143_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_xhcorr_60d_slope_v144_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_skewp_252d_slope_v145_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rkgap_5_21_slope_v146_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rkgap_63_252_slope_v147_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_blendrk_252d_slope_v148_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_minrkdis_252d_slope_v149_signal, ["closeadj"]),
    (f15xm_f15_cross_sectional_momentum_rkrng_120d_slope_v150_signal, ["closeadj"]),
]
f15_cross_sectional_momentum_slope_001_150_REGISTRY = {fn.__name__: {"inputs": ins, "func": fn} for fn, ins in _FUNCS}
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
    for name, entry in f15_cross_sectional_momentum_slope_001_150_REGISTRY.items():
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
