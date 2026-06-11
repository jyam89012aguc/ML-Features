"""f10_candle_sequence_patterns jerk features 001-150 (2nd derivative).

Each jerk feature inlines the base formula then takes base - 2*base.shift(k) + base.shift(2k)
where k is chosen by ROC bracket of the base window. Bases use mainly
short windows (multi-bar pattern features are inherently short); k is
varied within bracket to decorrelate similar shapes.
NaN policy: replace([inf,-inf], nan) only at the final return.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

def _j(b,k):
 return b-2*b.shift(k)+b.shift(2*k)

def _f(s):
 return s.replace([np.inf,-np.inf],np.nan)

def _ac1_h(x):
 if np.isnan(x).any():
  return np.nan
 a = x[:-1]; b = x[1:]
 if a.std() == 0 or b.std() == 0:
  return np.nan
 return float(np.corrcoef(a, b)[0, 1])

def _ac2_h(x):
 if np.isnan(x).any() or len(x) < 4:
  return np.nan
 a = x[:-2]; b = x[2:]
 if a.std() == 0 or b.std() == 0:
  return np.nan
 return float(np.corrcoef(a, b)[0, 1])

def _ds_h(x):
 idx = np.where(x > 0.5)[0]
 if idx.size == 0:
  return float(len(x))
 return float(len(x) - 1 - idx[-1])

def _rs_h(x):
 x = x - x.mean()
 c = x.cumsum()
 R = c.max() - c.min()
 S = x.std()
 if S == 0:
  return np.nan
 return float(np.log((R / S) + 1e-12))

def _ent_h(x):
 if np.isnan(x).any():
  return np.nan
 p = float(np.mean(x))
 if p <= 0.0 or p >= 1.0:
  return 0.0
 return -p * np.log(p) - (1.0 - p) * np.log(1.0 - p)

def _mean_run_h(x):
 if np.isnan(x).any() or len(x) < 2:
  return np.nan
 runs = []; cur = 1
 for i in range(1, len(x)):
  if x[i] == x[i-1]:
   cur += 1
  else:
   runs.append(cur); cur = 1
 runs.append(cur)
 return float(np.mean(runs))

def _mono_h(x):
 if np.isnan(x).any() or len(x) < 2:
  return np.nan
 max_up = max_dn = cur = 1; sign = 0
 for i in range(1, len(x)):
  if x[i] == x[i-1] and x[i] != 0:
   cur += 1
  else:
   if sign > 0:
    max_up = max(max_up, cur)
   elif sign < 0:
    max_dn = max(max_dn, cur)
   cur = 1; sign = x[i]
   continue
  sign = x[i]
 if sign > 0:
  max_up = max(max_up, cur)
 elif sign < 0:
  max_dn = max(max_dn, cur)
 return float(max_up - max_dn) / float(len(x))

def f10cs_f10_candle_sequence_patterns_bullengs_2d_jerk_v001_signal(open, close):
 body = close - open
 prev_body = body.shift(1)
 norm = (body.abs() + prev_body.abs()).replace(0.0,np.nan)
 b = (body - prev_body) / norm
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_bearengs_2d_jerk_v002_signal(open, high, low, close):
 body = close - open
 prev_body = body.shift(1)
 full = ((high - low) + (high.shift(1) - low.shift(1))).replace(0.0,np.nan)
 b = (-body * prev_body.abs() - prev_body * body.abs()) / full
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_engratio_2d_jerk_v003_signal(open, close):
 cur = (close - open).abs()
 prev = cur.shift(1).replace(0.0,np.nan)
 b = np.log((cur + 1e-12) / (prev + 1e-12))
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_haramis_2d_jerk_v004_signal(open, high, low, close):
 cur_hi = np.maximum(open, close)
 cur_lo = np.minimum(open, close)
 prv_body = (cur_hi.shift(1) - cur_lo.shift(1)).replace(0.0,np.nan)
 over_h = (cur_hi - cur_hi.shift(1)).clip(lower=0.0) / prv_body
 over_l = (cur_lo.shift(1) - cur_lo).clip(lower=0.0) / prv_body
 b = 1.0 - (over_h + over_l)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_pierces_2d_jerk_v005_signal(open, close):
 prev_open = open.shift(1); prev_close = close.shift(1)
 prev_red = (prev_open - prev_close).clip(lower=0.0).replace(0.0,np.nan)
 prev_mid = (prev_open + prev_close) / 2.0
 score = (close - prev_mid) / prev_red
 soft_gate = ((prev_close - open) / prev_red).clip(lower=-1.0, upper=1.0)
 b = score * soft_gate.clip(lower=0.0)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_darkcs_2d_jerk_v006_signal(open, close):
 prev_open = open.shift(1); prev_close = close.shift(1)
 prev_green = (prev_close - prev_open).clip(lower=0.0).replace(0.0,np.nan)
 prev_mid = (prev_open + prev_close) / 2.0
 score = (prev_mid - close) / prev_green
 soft_gate = ((open - prev_close) / prev_green).clip(lower=-1.0, upper=1.0)
 b = score * soft_gate.clip(lower=0.0)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_tweezerth_2d_jerk_v007_signal(high, low):
 diff = (high - high.shift(1)).abs()
 den = (high + high.shift(1)).replace(0.0,np.nan)
 b = -(diff / den)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_tweezerbl_2d_jerk_v008_signal(low):
 diff = (low - low.shift(1)).abs()
 den = (low + low.shift(1)).replace(0.0,np.nan)
 b = -(diff / den)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_hhpct_10d_jerk_v009_signal(high, low):
 hh = (high > high.shift(1)).astype(float).where(~high.isna() & ~high.shift(1).isna())
 hl = (low > low.shift(1)).astype(float).where(~low.isna() & ~low.shift(1).isna())
 b = (hh * hl).rolling(10, min_periods=10).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_llpct_10d_jerk_v010_signal(high, low):
 lh = (high < high.shift(1)).astype(float).where(~high.isna() & ~high.shift(1).isna())
 ll = (low < low.shift(1)).astype(float).where(~low.isna() & ~low.shift(1).isna())
 b = (lh * ll).rolling(10, min_periods=10).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_whitesold_3d_jerk_v011_signal(open, close):
 body = (close - open) / open.replace(0.0,np.nan)
 s = body + body.shift(1) + body.shift(2)
 b = np.tanh(3.0 * s)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_blackcrow_3d_jerk_v012_signal(open, high, low, close):
 bear = (close < open).astype(float).where(~close.isna() & ~open.isna())
 lower_h = (high < high.shift(1)).astype(float).where(~high.isna() & ~high.shift(1).isna())
 s = (bear + bear.shift(1) + bear.shift(2)) * (lower_h + lower_h.shift(1) + lower_h.shift(2))
 rng_n = (high - low).rolling(10, min_periods=10).mean().replace(0.0,np.nan)
 intensity = -(close - close.shift(2)) / rng_n
 b = s * intensity / 9.0
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_morningst_3d_jerk_v013_signal(open, high, low, close):
 body = close - open
 rng = (high - low).replace(0.0,np.nan)
 b2 = -body.shift(2) / rng.shift(2)
 b1 = 1.0 - (body.shift(1).abs() / rng.shift(1))
 b0 = body / rng
 b = (b2 + b1 + b0) / 3.0
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_eveningst_3d_jerk_v014_signal(open, high, low, close):
 body = close - open
 rng = (high - low).replace(0.0,np.nan)
 b2 = body.shift(2) / rng.shift(2)
 b1 = 1.0 - (body.shift(1).abs() / rng.shift(1))
 b0 = -body / rng
 b = (b2 + b1 + b0) / 3.0
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_threeinup_3d_jerk_v015_signal(open, close):
 body = close - open
 cur_hi = np.maximum(open, close)
 cur_lo = np.minimum(open, close)
 inside = ((cur_hi.shift(1) < cur_hi.shift(2)).astype(float)
     + (cur_lo.shift(1) > cur_lo.shift(2)).astype(float)) / 2.0
 prev_red = (-body.shift(2)).clip(lower=0.0)
 b = inside * np.sign(prev_red) * np.tanh(10.0 * body / close.replace(0.0,np.nan))
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_threeindn_3d_jerk_v016_signal(open, close):
 body = close - open
 cur_hi = np.maximum(open, close)
 cur_lo = np.minimum(open, close)
 inside = ((cur_hi.shift(1) < cur_hi.shift(2)).astype(float)
     + (cur_lo.shift(1) > cur_lo.shift(2)).astype(float)) / 2.0
 prev_green = body.shift(2).clip(lower=0.0)
 b = inside * np.sign(prev_green) * np.tanh(10.0 * (-body) / close.replace(0.0,np.nan))
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_threeoutup_3d_jerk_v017_signal(open, high, low, close):
 body = close - open
 cur_hi = np.maximum(open, close)
 cur_lo = np.minimum(open, close)
 outside = ((cur_hi.shift(1) > cur_hi.shift(2)).astype(float)
      + (cur_lo.shift(1) < cur_lo.shift(2)).astype(float)) / 2.0
 prev_engulf_color = np.sign(body.shift(1))
 confirm = np.sign(body) * (body / close.replace(0.0,np.nan)).abs()
 b = outside * prev_engulf_color * np.tanh(20.0 * confirm)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_inscnt_20d_jerk_v018_signal(high, low):
 inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
 inside = inside.where(~high.isna() & ~high.shift(1).isna())
 b = inside.rolling(20, min_periods=20).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_outcnt_30d_jerk_v019_signal(high, low):
 outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
 outside = outside.where(~high.isna() & ~high.shift(1).isna())
 b = outside.rolling(30, min_periods=30).sum()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_dsinsd_50d_jerk_v022_signal(high, low):
 inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
 inside = inside.where(~high.isna() & ~high.shift(1).isna())
 b = inside.rolling(50, min_periods=50).apply(_ds_h, raw=True)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_dsoutsd_50d_jerk_v023_signal(high, low):
 outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
 outside = outside.where(~high.isna() & ~high.shift(1).isna())
 b = outside.rolling(50, min_periods=50).apply(_ds_h, raw=True)
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_nr4_4d_jerk_v024_signal(high, low):
 rng = high - low
 mn = rng.rolling(4, min_periods=4).min()
 den = rng.rolling(4, min_periods=4).mean().replace(0.0,np.nan)
 b = (rng - mn) / den
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_nr7_7d_jerk_v025_signal(high, low):
 rng = high - low
 mn = rng.rolling(7, min_periods=7).min().replace(0.0,np.nan)
 b = rng / mn
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_wr4_4d_jerk_v026_signal(high, low):
 rng = high - low
 mx = rng.rolling(4, min_periods=4).max().replace(0.0,np.nan)
 b = rng / mx
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_bullstk_2d_jerk_v027_signal(open, close):
 bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
 g = (bull != bull.shift(1)).cumsum()
 streak = bull.groupby(g).cumsum()
 b = streak * bull
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_bearstk_2d_jerk_v028_signal(open, close):
 bear = (close < open).astype(float).where(~close.isna() & ~open.isna())
 g = (bear != bear.shift(1)).cumsum()
 streak = bear.groupby(g).cumsum()
 b = streak * bear
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_colflip_20d_jerk_v029_signal(open, close):
 sgn = np.sign(close - open)
 flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
 b = flip.rolling(20, min_periods=20).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_coltrans_30d_jerk_v030_signal(open, close):
 sgn = np.sign(close - open)
 flip = (sgn != sgn.shift(1)).astype(float).where(~sgn.isna() & ~sgn.shift(1).isna())
 b = flip.rolling(30, min_periods=30).mean()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_markov_40d_jerk_v031_signal(open, close):
 bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
 prev_bull = bull.shift(1)
 both = (bull * prev_bull).rolling(40, min_periods=40).sum()
 pb_count = prev_bull.rolling(40, min_periods=40).sum().replace(0.0,np.nan)
 b = both / pb_count
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_markov_60d_jerk_v032_signal(open, close):
 bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
 bear = 1.0 - bull
 p_bull = bull.rolling(60, min_periods=60).mean()
 cond = (bull * bear.shift(1)).rolling(60, min_periods=60).sum()
 bear_cnt = bear.shift(1).rolling(60, min_periods=60).sum().replace(0.0,np.nan)
 b = p_bull - (cond / bear_cnt)
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_bodyrat_2d_jerk_v033_signal(open, high, low, close):
 body_r = (close - open).abs() / (high - low).replace(0.0,np.nan)
 b = body_r - body_r.shift(1)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_bodymon_5d_jerk_v034_signal(open, close):
 body = (close - open).abs()
 inc = (body > body.shift(1)).astype(float).where(~body.isna() & ~body.shift(1).isna())
 b = inc.rolling(5, min_periods=5).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_bodycum_3d_jerk_v035_signal(open, high, low, close):
 body_r = (close - open) / (high - low).replace(0.0,np.nan)
 b = body_r - body_r.shift(2)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_bodyaccl_4d_jerk_v036_signal(open, close):
 body = (close - open).abs()
 accel = body - 2.0 * body.shift(1) + body.shift(2)
 den = body.rolling(4, min_periods=4).mean().replace(0.0,np.nan)
 b = accel / den
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_rngbull_5d_jerk_v037_signal(open, high, low, close):
 rng = high - low
 rng_ratio = np.log((rng + 1e-12) / (rng.shift(1) + 1e-12))
 color = np.sign(close - open)
 b = (rng_ratio * color).rolling(5, min_periods=5).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_rngbear_5d_jerk_v038_signal(open, high, low, close):
 rng = high - low
 expand = (rng > 1.1 * rng.shift(1)).astype(float)
 bear = (close < open).astype(float)
 feat = (expand * bear).where(~rng.isna() & ~rng.shift(1).isna())
 b = feat.rolling(5, min_periods=5).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_volconf_10d_jerk_v039_signal(open, close, volume):
 body = close - open
 vmean = volume.rolling(10, min_periods=10).mean()
 vstd = volume.rolling(10, min_periods=10).std().replace(0.0,np.nan)
 vz = (volume - vmean) / vstd
 b = (np.sign(body) * vz).rolling(10, min_periods=10).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_rngcontr_5d_jerk_v040_signal(high, low):
 rng = (high - low).replace(0.0,np.nan)
 b = np.log(rng).diff(4)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_hangmans_2d_jerk_v041_signal(open, high, low, close):
 body = (close - open).abs()
 rng = (high - low).replace(0.0,np.nan)
 lower = np.minimum(open, close) - low
 upper = high - np.maximum(open, close)
 shape = (lower / rng) - 2.0 * (body / rng) - (upper / rng)
 prev_color = np.sign(close.shift(1) - open.shift(1))
 b = shape * prev_color
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_hammer_2d_jerk_v042_signal(open, high, low, close):
 rng = (high - low).replace(0.0,np.nan)
 lower = np.minimum(open, close) - low
 shape = lower / rng
 prior_drop = np.log(close.shift(1).replace(0.0,np.nan) / close.shift(3).replace(0.0,np.nan))
 b = shape * (-prior_drop)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_shootst_2d_jerk_v043_signal(open, high, low, close):
 body = (close - open).abs()
 rng = (high - low).replace(0.0,np.nan)
 upper = high - np.maximum(open, close)
 lower = np.minimum(open, close) - low
 shape = (upper / rng) - 2.0 * (body / rng) - (lower / rng)
 prev_color = np.sign(close.shift(1) - open.shift(1))
 b = shape * prev_color
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_invhamr_2d_jerk_v044_signal(open, high, low, close):
 rng = (high - low).replace(0.0,np.nan)
 upper = high - np.maximum(open, close)
 shape = upper / rng
 mom2 = (close.shift(1) - close.shift(3)) / close.shift(3).replace(0.0,np.nan)
 b = shape * (-mom2)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_flag_10d_jerk_v045_signal(open, close):
 move5 = close - close.shift(5)
 move3 = close - close.shift(3)
 b = np.tanh(20.0 * move5 / close.replace(0.0,np.nan)) * np.tanh(-20.0 * move3 / close.replace(0.0,np.nan))
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_pennant_10d_jerk_v046_signal(high, low, close):
 rng = (high - low).replace(0.0,np.nan)
 contr = np.log(rng).rolling(10, min_periods=10).apply(
  lambda x: float(np.polyfit(np.arange(len(x)), x, 1)[0]) if np.isfinite(x).all() else np.nan,
  raw=True,
 )
 trend = (close - close.shift(20)) / close.replace(0.0,np.nan)
 b = -contr * np.tanh(50.0 * trend)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_rise3m_5d_jerk_v047_signal(open, close):
 body = close - open
 rn = close.replace(0.0,np.nan)
 big = body.shift(4) * body
 small = (body.shift(1).abs() + body.shift(2).abs() + body.shift(3).abs())
 b = (big - small) / (rn * rn)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_fall3m_5d_jerk_v048_signal(open, close):
 body = close - open
 rn = close.replace(0.0,np.nan)
 big = (-body.shift(4)) * (-body)
 small = (body.shift(1).abs() + body.shift(2).abs() + body.shift(3).abs())
 s = (big - small) / (rn * rn)
 mask = (np.sign(-body.shift(4)) > 0) & (np.sign(-body) > 0)
 b = s.where(mask, other=0.0)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_pressure_20d_jerk_v049_signal(open, close):
 body = close - open
 s = body.rolling(20, min_periods=20).sum()
 a = body.abs().rolling(20, min_periods=20).sum().replace(0.0,np.nan)
 b = s / a
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_pressure_50d_jerk_v050_signal(open, closeadj):
 body = closeadj - closeadj.shift(1)
 s = body.rolling(50, min_periods=50).sum()
 a = body.abs().rolling(50, min_periods=50).sum().replace(0.0,np.nan)
 b = s / a
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_seqskew_30d_jerk_v051_signal(open, close):
 body = close - open
 b = body.rolling(30, min_periods=30).skew()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_seqkurt_40d_jerk_v052_signal(open, closeadj):
 body = closeadj - closeadj.shift(1)
 b = body.rolling(40, min_periods=40).kurt()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_colac1_30d_jerk_v053_signal(open, close):
 sgn = np.sign(close - open).where(~close.isna() & ~open.isna())
 b = sgn.rolling(30, min_periods=30).apply(_ac1_h, raw=True)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_bodyac2_25d_jerk_v054_signal(open, close):
 body = (close - open).where(~close.isna() & ~open.isna())
 b = body.rolling(25, min_periods=25).apply(_ac2_h, raw=True)
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_engcnt_20d_jerk_v055_signal(open, close):
 body = close - open
 sgn = np.sign(body)
 cond = ((body.abs() > 1.2 * body.shift(1).abs())
   & (sgn != sgn.shift(1))).astype(float)
 cond = cond.where(~body.isna() & ~body.shift(1).isna())
 b = cond.rolling(20, min_periods=20).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_softdoji_30d_jerk_v056_signal(open, high, low, close):
 body = (close - open).abs()
 rng = (high - low).replace(0.0,np.nan)
 score = (1.0 - body / rng).clip(lower=0.0, upper=1.0)
 b = score.rolling(30, min_periods=30).mean()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_engrank_30d_jerk_v057_signal(open, close):
 cur = (close - open).abs()
 prev = cur.shift(1).replace(0.0,np.nan)
 r = cur / prev
 b = r.rolling(30, min_periods=15).rank(pct=True)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_bestbar_20d_jerk_v058_signal(open, close):
 body = (close - open) / close.replace(0.0,np.nan)
 b = body.rolling(20, min_periods=10).rank(pct=True)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_worstbar_20d_jerk_v059_signal(open, high, low, close):
 rng = ((high - low) * ((close < open).astype(float))).replace(0.0,np.nan)
 b = rng.rolling(20, min_periods=10).rank(pct=True)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_overlapr_5d_jerk_v060_signal(high, low):
 cur_hi = high; cur_lo = low
 prv_hi = high.shift(1); prv_lo = low.shift(1)
 ovlp = np.minimum(cur_hi, prv_hi) - np.maximum(cur_lo, prv_lo)
 ovlp = ovlp.clip(lower=0.0)
 avg_r = ((cur_hi - cur_lo) + (prv_hi - prv_lo)) / 2.0
 r = ovlp / avg_r.replace(0.0,np.nan)
 b = r.rolling(5, min_periods=5).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_gapseq_10d_jerk_v061_signal(open, close):
 csign = np.sign(close - close.shift(1))
 osign = np.sign(open - close.shift(1))
 agree = (csign * osign).where(~csign.isna() & ~osign.isna())
 b = agree.rolling(10, min_periods=10).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_seqdrift_15d_jerk_v062_signal(open, close):
 sgn = np.sign(close - open)
 short = sgn.rolling(5, min_periods=5).mean()
 long_ = sgn.rolling(15, min_periods=15).mean()
 b = short - long_
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_volimb_15d_jerk_v063_signal(open, close, volume):
 bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
 bear = 1.0 - bull
 bull_v = (bull * volume).rolling(15, min_periods=15).sum()
 bear_v = (bear * volume).rolling(15, min_periods=15).sum().replace(0.0,np.nan)
 b = np.log((bull_v + 1.0) / (bear_v + 1.0))
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_brkout_20d_jerk_v064_signal(high, low, close):
 rng = high - low
 rng10 = rng.rolling(10, min_periods=10).mean().shift(1)
 contraction = rng.shift(1).rolling(10, min_periods=10).mean() / rng10.replace(0.0,np.nan)
 expansion = rng / rng10.replace(0.0,np.nan)
 b = expansion - contraction
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_revcomb_3d_jerk_v065_signal(open, high, low, close):
 body = close - open
 rng = (high - low).replace(0.0,np.nan)
 lower = np.minimum(open, close) - low
 upper = high - np.maximum(open, close)
 asym = (lower - upper) / rng
 eng = (body - body.shift(1)) / (body.abs() + body.shift(1).abs() + 1e-12)
 b = (eng + asym - asym.shift(1)) / 3.0
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_contcomb_5d_jerk_v066_signal(open, close):
 sgn = np.sign(close - open)
 g = (sgn != sgn.shift(1)).cumsum()
 streak = sgn.groupby(g).cumcount() + 1
 body_mean = (close - open).rolling(5, min_periods=5).mean()
 b = streak * np.sign(body_mean) / 5.0
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_topbot_8d_jerk_v067_signal(high, low, close):
 top1 = high.rolling(4, min_periods=4).max()
 top2 = high.shift(4).rolling(4, min_periods=4).max()
 dev = high.rolling(8, min_periods=8).std().replace(0.0,np.nan)
 b = -(top1 - top2).abs() / dev
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_swing_10d_jerk_v068_signal(high, low):
 mid = (high + low) / 2.0
 d = np.sign(mid.diff()).where(~mid.diff().isna())
 flip = (d != d.shift(1)).astype(float).where(~d.isna() & ~d.shift(1).isna())
 b = flip.rolling(10, min_periods=10).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_bodyimb_10d_jerk_v069_signal(open, close):
 body = close - open
 a = body.rolling(10, min_periods=10).sum()
 bs = body.shift(10).rolling(10, min_periods=10).sum()
 b = (a - bs) / (a.abs() + bs.abs() + 1e-12)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_thrust_3d_jerk_v070_signal(open, close):
 body = close - open
 cross = (close > close.shift(1)).astype(float) - (close < close.shift(1)).astype(float)
 cross = cross.where(~close.isna() & ~close.shift(1).isna())
 consec = cross.rolling(3, min_periods=3).sum()
 b = consec * (body.abs() / close.replace(0.0,np.nan))
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_streakdiff_20d_jerk_v071_signal(open, close):
 bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
 bear = (close < open).astype(float).where(~close.isna() & ~open.isna())
 b = bull.rolling(20, min_periods=20).mean() - bear.rolling(20, min_periods=20).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_rngmom_8d_jerk_v072_signal(high, low):
 rng = high - low
 d = (rng - rng.shift(1)) / rng.rolling(8, min_periods=8).mean().replace(0.0,np.nan)
 b = d.rolling(8, min_periods=8).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_seqsharp_30d_jerk_v073_signal(open, closeadj):
 body_n = np.log(closeadj.replace(0.0,np.nan) / closeadj.shift(1))
 m = body_n.rolling(30, min_periods=30).mean()
 s = body_n.rolling(30, min_periods=30).std().replace(0.0,np.nan)
 b = m / s
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_3bartrk_3d_jerk_v074_signal(close):
 d1 = np.sign(close - close.shift(1))
 d2 = np.sign(close.shift(1) - close.shift(2))
 d3 = np.sign(close.shift(2) - close.shift(3))
 b = (d1 + d2 + d3).where(~close.isna() & ~close.shift(3).isna())
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_pinbar_2d_jerk_v075_signal(open, high, low, close):
 body = (close - open).abs()
 rng = (high - low).replace(0.0,np.nan)
 lower = np.minimum(open, close) - low
 upper = high - np.maximum(open, close)
 pin_up = (upper / rng) - 2.0 * (body / rng) - (lower / rng)
 pin_dn = (lower / rng) - 2.0 * (body / rng) - (upper / rng)
 trend = np.sign((close - close.shift(3)))
 b = trend * pin_up - trend * pin_dn
 return _f(_j(b,5))

# --- Slopes for base 076-150 -------------------------------------

def f10cs_f10_candle_sequence_patterns_bsidvr_2d_jerk_v076_signal(open, high, low, close):
 body = close - open
 same_col = np.sign(body) * np.sign(body.shift(1))
 rng = (high - low).replace(0.0,np.nan)
 rel = (body.abs() - body.shift(1).abs()) / rng
 b = same_col * rel
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_concl3_3d_jerk_v077_signal(close):
 c2 = close - 2.0 * close.shift(1) + close.shift(2)
 den = close.rolling(3, min_periods=3).mean().replace(0.0,np.nan)
 b = c2 / den
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_gap2bdy_2d_jerk_v078_signal(open, close):
 gap = open - close.shift(1)
 den = ((close - open).abs() + (close.shift(1) - open.shift(1)).abs()).replace(0.0,np.nan)
 b = gap / den
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_2bartrk_2d_jerk_v079_signal(close):
 d1 = np.sign(close - close.shift(1))
 d2 = np.sign(close.shift(1) - close.shift(2))
 b = (d1 + d2).where(~close.isna() & ~close.shift(2).isna())
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_bothshad_3d_jerk_v080_signal(open, high, low, close):
 upper = high - np.maximum(open, close)
 lower = np.minimum(open, close) - low
 rng = (high - low).replace(0.0,np.nan)
 asym = (upper - lower) / rng
 b = asym.rolling(3, min_periods=3).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_riseclos_5d_jerk_v081_signal(close):
 up = (close > close.shift(1)).astype(float).where(~close.isna() & ~close.shift(1).isna())
 b = up.rolling(5, min_periods=5).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_clsclose_2d_jerk_v082_signal(open, close):
 s_cur = np.sign(close - open)
 s_prv = np.sign(close.shift(1) - open.shift(1))
 b = (s_cur * s_prv).where(~s_cur.isna() & ~s_prv.isna())
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_thirteenseq_13d_jerk_v083_signal(close):
 flag = (close > close.shift(4)).astype(float).where(~close.isna() & ~close.shift(4).isna())
 b = flag.rolling(13, min_periods=13).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_dnsetup_9d_jerk_v084_signal(close):
 flag = (close < close.shift(4)).astype(float).where(~close.isna() & ~close.shift(4).isna())
 b = flag.rolling(9, min_periods=9).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_islndrev_3d_jerk_v085_signal(open, high, low, close):
 gap_prev = (low.shift(1) - high.shift(2)).clip(lower=0.0) - (low.shift(2) - high.shift(1)).clip(lower=0.0)
 gap_cur = (high - low.shift(1)).clip(lower=0.0) - (high.shift(1) - low).clip(lower=0.0)
 norm = (high - low).rolling(20, min_periods=20).mean().replace(0.0,np.nan)
 b = -(gap_prev * gap_cur) / (norm * norm)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_winflwthru_3d_jerk_v086_signal(open, close):
 body = close - open
 seq = ((body > 0) & (body.shift(1) > 0) & (body.shift(2) > 0)).astype(float)
 seq = seq.where(~body.isna() & ~body.shift(2).isna())
 cum = (body + body.shift(1) + body.shift(2)) / close.replace(0.0,np.nan)
 b = seq * cum
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_losflwthru_3d_jerk_v087_signal(open, close):
 body = close - open
 seq = ((body < 0) & (body.shift(1) < 0) & (body.shift(2) < 0)).astype(float)
 seq = seq.where(~body.isna() & ~body.shift(2).isna())
 cum = (body + body.shift(1) + body.shift(2)) / close.replace(0.0,np.nan)
 b = seq * cum
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_engcnt_40d_jerk_v088_signal(open, close):
 body = close - open
 sgn = np.sign(body)
 cond = ((body.abs() > body.shift(1).abs())
   & (sgn != sgn.shift(1))).astype(float).where(~body.isna() & ~body.shift(1).isna())
 b = cond.rolling(40, min_periods=40).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_haramicnt_30d_jerk_v089_signal(open, close):
 body = close - open
 sgn = np.sign(body)
 cond = ((body.abs() < 0.7 * body.shift(1).abs())
   & (sgn != sgn.shift(1))
   & (body.shift(1).abs() > 1e-12)).astype(float).where(~body.isna() & ~body.shift(1).isna())
 b = cond.rolling(30, min_periods=30).sum()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_dojicnt_25d_jerk_v090_signal(open, high, low, close):
 body_r = (close - open).abs() / (high - low).replace(0.0,np.nan)
 doji = (body_r < 0.15).astype(float)
 non_doji_prev = (body_r.shift(1) >= 0.15).astype(float)
 cond = (doji * non_doji_prev).where(~body_r.isna() & ~body_r.shift(1).isna())
 b = cond.rolling(25, min_periods=25).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_revcnt_20d_jerk_v091_signal(open, close):
 body_s = np.sign(close - open)
 chg = (close - close.shift(1)).abs()
 m = chg.rolling(20, min_periods=20).mean().replace(0.0,np.nan)
 cond = ((body_s != body_s.shift(1)) & (chg > 1.5 * m)).astype(float)
 cond = cond.where(~body_s.isna() & ~body_s.shift(1).isna())
 b = cond.rolling(20, min_periods=20).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_btopcnt_30d_jerk_v092_signal(high, low, close):
 cond = ((high > high.shift(1)) & (close < close.shift(1))).astype(float)
 cond = cond.where(~high.isna() & ~high.shift(1).isna() & ~close.isna())
 b = cond.rolling(30, min_periods=30).sum()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_bbotcnt_30d_jerk_v093_signal(high, low, close):
 cond = ((low < low.shift(1)) & (close > close.shift(1))).astype(float)
 cond = cond.where(~low.isna() & ~low.shift(1).isna() & ~close.isna())
 b = cond.rolling(30, min_periods=30).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_distinsd_10d_jerk_v094_signal(high, low):
 a = high - high.shift(1)
 bb = low.shift(1) - low
 avg_r = (high - low).rolling(10, min_periods=10).mean().replace(0.0,np.nan)
 b = (a - bb) / avg_r
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_distoutsd_10d_jerk_v095_signal(high, low):
 a = high - high.shift(1)
 bb = low - low.shift(1)
 avg_r = (high - low).rolling(10, min_periods=10).mean().replace(0.0,np.nan)
 b = (a - bb) / avg_r
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_disteng_2d_jerk_v096_signal(open, close):
 body = close - open
 sd = body.rolling(20, min_periods=20).std().replace(0.0,np.nan)
 b = (body - body.shift(1)) / sd
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_disthar_2d_jerk_v097_signal(open, close):
 body = close - open
 sgn = np.sign(body)
 raw = np.log((body.abs() + 1e-12) / (body.shift(1).abs() + 1e-12))
 mask = (sgn != sgn.shift(1)).astype(float)
 b = raw * mask
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_engdiff_20d_jerk_v098_signal(open, close):
 body = close - open
 sgn = np.sign(body)
 eng = ((body.abs() > body.shift(1).abs()) & (sgn != sgn.shift(1))).astype(float).where(~body.isna() & ~body.shift(1).isna())
 har = ((body.abs() < body.shift(1).abs()) & (sgn != sgn.shift(1))).astype(float).where(~body.isna() & ~body.shift(1).isna())
 b = eng.rolling(20, min_periods=20).sum() - har.rolling(20, min_periods=20).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_insoutd_30d_jerk_v099_signal(high, low):
 inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float).where(~high.isna() & ~high.shift(1).isna())
 outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float).where(~high.isna() & ~high.shift(1).isna())
 b = inside.rolling(30, min_periods=30).sum() - outside.rolling(30, min_periods=30).sum()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_hhstk_2d_jerk_v100_signal(high):
 hh = (high > high.shift(1)).astype(float).where(~high.isna() & ~high.shift(1).isna())
 g = (hh != hh.shift(1)).cumsum()
 streak = hh.groupby(g).cumsum()
 b = streak * hh
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_llstk_2d_jerk_v101_signal(low):
 ll = (low < low.shift(1)).astype(float).where(~low.isna() & ~low.shift(1).isna())
 g = (ll != ll.shift(1)).cumsum()
 streak = ll.groupby(g).cumsum()
 b = streak * ll
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_upclstk_2d_jerk_v102_signal(close):
 up = (close > close.shift(1)).astype(float).where(~close.isna() & ~close.shift(1).isna())
 g = (up != up.shift(1)).cumsum()
 streak = up.groupby(g).cumsum()
 b = streak * up
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_dnclstk_2d_jerk_v103_signal(close):
 dn = (close < close.shift(1)).astype(float).where(~close.isna() & ~close.shift(1).isna())
 g = (dn != dn.shift(1)).cumsum()
 streak = dn.groupby(g).cumsum()
 b = streak * dn
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_engsmean_20d_jerk_v104_signal(open, close):
 body = close - open
 raw = (body - body.shift(1))
 den = (body.abs() + body.shift(1).abs()).replace(0.0,np.nan)
 s = raw / den
 b = s.rolling(20, min_periods=20).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_harasm_30d_jerk_v105_signal(open, high, low, close):
 cur_hi = np.maximum(open, close)
 cur_lo = np.minimum(open, close)
 prv_hi = cur_hi.shift(1); prv_lo = cur_lo.shift(1)
 body = (prv_hi - prv_lo).replace(0.0,np.nan)
 over_h = (cur_hi - prv_hi).clip(lower=0.0) / body
 over_l = (prv_lo - cur_lo).clip(lower=0.0) / body
 s = 1.0 - (over_h + over_l)
 b = s.rolling(30, min_periods=30).mean()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_tweezm_20d_jerk_v106_signal(high, low):
 diff = (high - high.shift(1)).abs()
 den = (high + high.shift(1)).replace(0.0,np.nan)
 s = -(diff / den)
 b = s.rolling(20, min_periods=20).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_highbrk_10d_jerk_v107_signal(high, close):
 prior_hi = high.shift(1).rolling(5, min_periods=5).max()
 brk = (close > prior_hi).astype(float).where(~prior_hi.isna() & ~close.isna())
 b = brk.rolling(10, min_periods=10).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_lowbrk_10d_jerk_v108_signal(low, close):
 prior_lo = low.shift(1).rolling(5, min_periods=5).min()
 brk = (close < prior_lo).astype(float).where(~prior_lo.isna() & ~close.isna())
 b = brk.rolling(10, min_periods=10).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_failbrk_15d_jerk_v109_signal(high, close):
 prior_hi = high.shift(1).rolling(5, min_periods=5).max()
 cond = ((high > prior_hi) & (close < prior_hi)).astype(float).where(~prior_hi.isna())
 b = cond.rolling(15, min_periods=15).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_colcons_15d_jerk_v110_signal(open, close):
 co = np.sign(close - close.shift(1))
 bo = np.sign(close - open)
 agree = (co == bo).astype(float).where(~co.isna() & ~bo.isna())
 b = agree.rolling(15, min_periods=15).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_oprng_10d_jerk_v111_signal(open, high, low):
 prv_mid = (high.shift(1) + low.shift(1)) / 2.0
 prv_rng = (high.shift(1) - low.shift(1)).replace(0.0,np.nan)
 s = (open - prv_mid) / prv_rng
 b = s.rolling(10, min_periods=10).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_clrng_15d_jerk_v112_signal(high, low, close):
 prv_mid = (high.shift(1) + low.shift(1)) / 2.0
 prv_rng = (high.shift(1) - low.shift(1)).replace(0.0,np.nan)
 s = (close - prv_mid) / prv_rng
 b = s.rolling(15, min_periods=15).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_volup_20d_jerk_v113_signal(open, close, volume):
 bull = (close > open).astype(float)
 vmean = volume.rolling(20, min_periods=20).mean()
 high_v = (volume > vmean).astype(float)
 s = (bull * high_v).where(~bull.isna() & ~high_v.isna())
 b = s.rolling(20, min_periods=20).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_voldn_20d_jerk_v114_signal(open, close, volume):
 bear = (close < open).astype(float)
 vmean = volume.rolling(20, min_periods=20).mean()
 high_v = (volume > vmean).astype(float)
 s = (bear * high_v).where(~bear.isna() & ~high_v.isna())
 b = s.rolling(20, min_periods=20).mean()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_volclmx_30d_jerk_v115_signal(open, close, volume):
 body = close - open
 vmean = volume.rolling(30, min_periods=30).mean()
 vstd = volume.rolling(30, min_periods=30).std().replace(0.0,np.nan)
 vz = (volume - vmean) / vstd
 w = body * vz / close.replace(0.0,np.nan)
 b = w.rolling(30, min_periods=30).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_clseac1_25d_jerk_v116_signal(close):
 s = np.sign(close.diff()).where(~close.isna())
 b = s.rolling(25, min_periods=25).apply(_ac1_h, raw=True)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_rngac1_30d_jerk_v117_signal(high, low):
 rng = (high - low).where(~high.isna() & ~low.isna())
 b = rng.rolling(30, min_periods=30).apply(_ac1_h, raw=True)
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_bodyrs_30d_jerk_v118_signal(open, close):
 s = np.sign(close - open).where(~close.isna() & ~open.isna())
 b = s.rolling(30, min_periods=30).apply(_rs_h, raw=True)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_seqent_30d_jerk_v119_signal(open, close):
 bull = (close > open).astype(float).where(~close.isna() & ~open.isna())
 b = bull.rolling(30, min_periods=30).apply(_ent_h, raw=True)
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_runlen_50d_jerk_v120_signal(open, close):
 sgn = np.sign(close - open)
 b = sgn.rolling(50, min_periods=50).apply(_mean_run_h, raw=True)
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_engrank_50d_jerk_v121_signal(open, close):
 body = (close - open).abs()
 diff = body - body.shift(1)
 b = diff.rolling(50, min_periods=25).rank(pct=True)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_brngrnk_30d_jerk_v122_signal(high, low):
 rng = (high - low)
 ratio = rng / rng.shift(1).replace(0.0,np.nan)
 b = ratio.rolling(30, min_periods=15).rank(pct=True)
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_seqdir_60d_jerk_v123_signal(closeadj):
 s = np.sign(closeadj - closeadj.shift(1)).where(~closeadj.isna())
 b = s.rolling(60, min_periods=60).mean()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_seqac1_80d_jerk_v124_signal(closeadj):
 r = np.log(closeadj.replace(0.0,np.nan) / closeadj.shift(1))
 b = r.rolling(80, min_periods=80).apply(_ac1_h, raw=True)
 return _f(_j(b,63))

def f10cs_f10_candle_sequence_patterns_drmonotn_40d_jerk_v125_signal(closeadj):
 s = np.sign(closeadj.diff()).where(~closeadj.isna())
 b = s.rolling(40, min_periods=40).apply(_mono_h, raw=True)
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_bodyvar_25d_jerk_v126_signal(open, close):
 body = close - open
 s = body.rolling(25, min_periods=25).std()
 m = body.abs().rolling(25, min_periods=25).mean().replace(0.0,np.nan)
 b = s / m
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_seqvar_30d_jerk_v127_signal(high, low):
 rng = high - low
 d = rng - rng.shift(1)
 b = d.rolling(30, min_periods=30).std()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_clmad_20d_jerk_v128_signal(close):
 d = close.diff()
 mad = (d - d.rolling(20, min_periods=20).mean()).abs().rolling(20, min_periods=20).mean()
 sd = d.rolling(20, min_periods=20).std().replace(0.0,np.nan)
 b = mad / sd
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_morncnt_50d_jerk_v129_signal(open, high, low, close):
 body = close - open
 rng = (high - low).replace(0.0,np.nan)
 rel = body / rng
 cond = ((rel.shift(2) < -0.3) & (rel.shift(1).abs() < 0.3) & (rel > 0.3)).astype(float).where(~rel.shift(2).isna() & ~rel.isna())
 b = cond.rolling(50, min_periods=50).sum()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_evencnt_50d_jerk_v130_signal(open, high, low, close):
 body = close - open
 rng = (high - low).replace(0.0,np.nan)
 rel = body / rng
 cond = ((rel.shift(2) > 0.3) & (rel.shift(1).abs() < 0.3) & (rel < -0.3)).astype(float).where(~rel.shift(2).isna() & ~rel.isna())
 b = cond.rolling(50, min_periods=50).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_3soldcnt_40d_jerk_v131_signal(open, close):
 body = close - open
 bull = (body > 0).astype(float)
 rising = (close > close.shift(1)).astype(float)
 cond = (bull * bull.shift(1) * bull.shift(2)
   * rising * rising.shift(1) * rising.shift(2)).where(~body.isna() & ~body.shift(2).isna())
 b = cond.rolling(40, min_periods=40).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_3crowcnt_40d_jerk_v132_signal(open, close):
 body = close - open
 bear = (body < 0).astype(float)
 falling = (close < close.shift(1)).astype(float)
 cond = (bear * bear.shift(1) * bear.shift(2)
   * falling * falling.shift(1) * falling.shift(2)).where(~body.isna() & ~body.shift(2).isna())
 b = cond.rolling(40, min_periods=40).sum()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_acmrange_20d_jerk_v133_signal(high, low):
 rng = high - low
 d = rng - rng.shift(1)
 b = d.rolling(20, min_periods=20).sum() / rng.rolling(20, min_periods=20).mean().replace(0.0,np.nan)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_clseyema_15d_jerk_v134_signal(close, open):
 cond = ((close > open) & (close > close.shift(1))).astype(float).where(~close.isna() & ~open.isna() & ~close.shift(1).isna())
 b = cond.rolling(15, min_periods=15).mean()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_clshema_15d_jerk_v135_signal(close, open):
 cond = ((close < open) & (close < close.shift(1))).astype(float).where(~close.isna() & ~open.isna() & ~close.shift(1).isna())
 b = cond.rolling(15, min_periods=15).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_inssbur_10d_jerk_v136_signal(high, low, close):
 inside = ((high < high.shift(1)) & (low > low.shift(1))).astype(float)
 brk = (close > high.shift(1)).astype(float)
 cond = (inside.shift(1) * brk).where(~inside.isna() & ~brk.isna())
 b = cond.rolling(10, min_periods=10).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_outscont_10d_jerk_v137_signal(high, low, close):
 outside = ((high > high.shift(1)) & (low < low.shift(1))).astype(float)
 cont = (close > close.shift(1)).astype(float)
 cond = (outside.shift(1) * cont).where(~outside.isna() & ~cont.isna())
 b = cond.rolling(10, min_periods=10).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_innbody_3d_jerk_v138_signal(open, close):
 cur_hi = np.maximum(open, close)
 cur_lo = np.minimum(open, close)
 env_hi = cur_hi.rolling(3, min_periods=3).max()
 env_lo = cur_lo.rolling(3, min_periods=3).min()
 env_r = (env_hi - env_lo).replace(0.0,np.nan)
 b = (cur_hi.shift(1) - cur_lo.shift(1)) / env_r
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_clsmag_5d_jerk_v139_signal(close, open):
 body = close - open
 var30 = (body * body).rolling(30, min_periods=30).mean().replace(0.0,np.nan)
 s = (body * body) / var30
 b = s.rolling(5, min_periods=5).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_volpeak_15d_jerk_v140_signal(volume, close, open):
 bull = (close > open).astype(float)
 vm = volume.rolling(5, min_periods=5).mean().replace(0.0,np.nan)
 peak = (volume > 1.5 * vm).astype(float)
 cond = (peak * bull).where(~bull.isna() & ~peak.isna())
 b = cond.rolling(15, min_periods=15).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_voltrough_15d_jerk_v141_signal(volume, close, open):
 bear = (close < open).astype(float)
 vm = volume.rolling(5, min_periods=5).mean().replace(0.0,np.nan)
 trough = (volume < 0.67 * vm).astype(float)
 cond = (trough * bear).where(~bear.isna() & ~trough.isna())
 b = cond.rolling(15, min_periods=15).sum()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_gapfilcnt_20d_jerk_v142_signal(open, high, low, close):
 gap = open - close.shift(1)
 fill = (np.sign(gap) != np.sign(close - close.shift(1))) & (gap.abs() > 0.005 * close)
 fill = fill.astype(float).where(~gap.isna())
 b = fill.rolling(20, min_periods=20).sum()
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_gapfollow_20d_jerk_v143_signal(open, close):
 gap = open - close.shift(1)
 prev_body = (close.shift(1) - open.shift(1))
 cond = ((gap.abs() > 0.5 * prev_body.abs()) &
   (np.sign(gap) == np.sign(prev_body))).astype(float).where(~gap.isna() & ~prev_body.isna())
 b = cond.rolling(20, min_periods=20).sum()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_consec_25d_jerk_v144_signal(open, close):
 body = (close - open).where(~close.isna() & ~open.isna())
 b = body.rolling(25, min_periods=25).apply(_ac1_h, raw=True)
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_pinrng_30d_jerk_v145_signal(open, high, low, close):
 body = (close - open).abs()
 upper = high - np.maximum(open, close)
 lower = np.minimum(open, close) - low
 max_sh = np.maximum(upper, lower)
 cond = (max_sh > 2.0 * body).astype(float)
 prior_move = (close.shift(1) - close.shift(3)).abs() > 0.01 * close.shift(3)
 cond = cond.where(~body.isna()).astype(float) * prior_move.astype(float)
 b = cond.rolling(30, min_periods=30).sum()
 return _f(_j(b,21))

def f10cs_f10_candle_sequence_patterns_emadev_3d_jerk_v146_signal(close, open):
 body = close - open
 ema = body.ewm(span=6, adjust=False, min_periods=6).mean()
 s_short = np.sign(body.rolling(3, min_periods=3).mean())
 s_ema = np.sign(ema)
 b = (s_short - s_ema)
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_hlbal_15d_jerk_v147_signal(high, low):
 a = high - high.shift(1)
 bb = (low.shift(1) - low).replace(0.0,np.nan)
 s = a / bb
 b = s.rolling(15, min_periods=15).apply(
  lambda x: float(np.nanmedian(x[np.isfinite(x)])) if np.isfinite(x).any() else np.nan,
  raw=True,
 )
 return _f(_j(b,10))

def f10cs_f10_candle_sequence_patterns_clseopn_8d_jerk_v148_signal(open, close):
 cond = (close.shift(1) > open).astype(float).where(~close.shift(1).isna() & ~open.isna())
 b = cond.rolling(8, min_periods=8).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_clblopn_8d_jerk_v149_signal(open, high, low, close):
 gap = open - close.shift(1)
 prv_rng = (high.shift(1) - low.shift(1)).replace(0.0,np.nan)
 s = gap / prv_rng
 b = s.rolling(8, min_periods=8).mean()
 return _f(_j(b,5))

def f10cs_f10_candle_sequence_patterns_evenodd_20d_jerk_v150_signal(open, close):
 sgn = np.sign(close - open).where(~close.isna() & ~open.isna())
 target = (-1.0) ** pd.Series(np.arange(len(sgn)), index=sgn.index)
 score = (sgn * target).where(~sgn.isna())
 b = score.rolling(20, min_periods=20).mean()
 return _f(_j(b,10))

# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

_R = [
  ("f10cs_f10_candle_sequence_patterns_bullengs_2d_jerk_v001_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bullengs_2d_jerk_v001_signal),
  ("f10cs_f10_candle_sequence_patterns_bearengs_2d_jerk_v002_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_bearengs_2d_jerk_v002_signal),
  ("f10cs_f10_candle_sequence_patterns_engratio_2d_jerk_v003_signal",["open","close"],f10cs_f10_candle_sequence_patterns_engratio_2d_jerk_v003_signal),
  ("f10cs_f10_candle_sequence_patterns_haramis_2d_jerk_v004_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_haramis_2d_jerk_v004_signal),
  ("f10cs_f10_candle_sequence_patterns_pierces_2d_jerk_v005_signal",["open","close"],f10cs_f10_candle_sequence_patterns_pierces_2d_jerk_v005_signal),
  ("f10cs_f10_candle_sequence_patterns_darkcs_2d_jerk_v006_signal",["open","close"],f10cs_f10_candle_sequence_patterns_darkcs_2d_jerk_v006_signal),
  ("f10cs_f10_candle_sequence_patterns_tweezerth_2d_jerk_v007_signal",["high","low"],f10cs_f10_candle_sequence_patterns_tweezerth_2d_jerk_v007_signal),
  ("f10cs_f10_candle_sequence_patterns_tweezerbl_2d_jerk_v008_signal",["low"],f10cs_f10_candle_sequence_patterns_tweezerbl_2d_jerk_v008_signal),
  ("f10cs_f10_candle_sequence_patterns_hhpct_10d_jerk_v009_signal",["high","low"],f10cs_f10_candle_sequence_patterns_hhpct_10d_jerk_v009_signal),
  ("f10cs_f10_candle_sequence_patterns_llpct_10d_jerk_v010_signal",["high","low"],f10cs_f10_candle_sequence_patterns_llpct_10d_jerk_v010_signal),
  ("f10cs_f10_candle_sequence_patterns_whitesold_3d_jerk_v011_signal",["open","close"],f10cs_f10_candle_sequence_patterns_whitesold_3d_jerk_v011_signal),
  ("f10cs_f10_candle_sequence_patterns_blackcrow_3d_jerk_v012_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_blackcrow_3d_jerk_v012_signal),
  ("f10cs_f10_candle_sequence_patterns_morningst_3d_jerk_v013_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_morningst_3d_jerk_v013_signal),
  ("f10cs_f10_candle_sequence_patterns_eveningst_3d_jerk_v014_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_eveningst_3d_jerk_v014_signal),
  ("f10cs_f10_candle_sequence_patterns_threeinup_3d_jerk_v015_signal",["open","close"],f10cs_f10_candle_sequence_patterns_threeinup_3d_jerk_v015_signal),
  ("f10cs_f10_candle_sequence_patterns_threeindn_3d_jerk_v016_signal",["open","close"],f10cs_f10_candle_sequence_patterns_threeindn_3d_jerk_v016_signal),
  ("f10cs_f10_candle_sequence_patterns_threeoutup_3d_jerk_v017_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_threeoutup_3d_jerk_v017_signal),
  ("f10cs_f10_candle_sequence_patterns_inscnt_20d_jerk_v018_signal",["high","low"],f10cs_f10_candle_sequence_patterns_inscnt_20d_jerk_v018_signal),
  ("f10cs_f10_candle_sequence_patterns_outcnt_30d_jerk_v019_signal",["high","low"],f10cs_f10_candle_sequence_patterns_outcnt_30d_jerk_v019_signal),
  ("f10cs_f10_candle_sequence_patterns_dsinsd_50d_jerk_v022_signal",["high","low"],f10cs_f10_candle_sequence_patterns_dsinsd_50d_jerk_v022_signal),
  ("f10cs_f10_candle_sequence_patterns_dsoutsd_50d_jerk_v023_signal",["high","low"],f10cs_f10_candle_sequence_patterns_dsoutsd_50d_jerk_v023_signal),
  ("f10cs_f10_candle_sequence_patterns_nr4_4d_jerk_v024_signal",["high","low"],f10cs_f10_candle_sequence_patterns_nr4_4d_jerk_v024_signal),
  ("f10cs_f10_candle_sequence_patterns_nr7_7d_jerk_v025_signal",["high","low"],f10cs_f10_candle_sequence_patterns_nr7_7d_jerk_v025_signal),
  ("f10cs_f10_candle_sequence_patterns_wr4_4d_jerk_v026_signal",["high","low"],f10cs_f10_candle_sequence_patterns_wr4_4d_jerk_v026_signal),
  ("f10cs_f10_candle_sequence_patterns_bullstk_2d_jerk_v027_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bullstk_2d_jerk_v027_signal),
  ("f10cs_f10_candle_sequence_patterns_bearstk_2d_jerk_v028_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bearstk_2d_jerk_v028_signal),
  ("f10cs_f10_candle_sequence_patterns_colflip_20d_jerk_v029_signal",["open","close"],f10cs_f10_candle_sequence_patterns_colflip_20d_jerk_v029_signal),
  ("f10cs_f10_candle_sequence_patterns_coltrans_30d_jerk_v030_signal",["open","close"],f10cs_f10_candle_sequence_patterns_coltrans_30d_jerk_v030_signal),
  ("f10cs_f10_candle_sequence_patterns_markov_40d_jerk_v031_signal",["open","close"],f10cs_f10_candle_sequence_patterns_markov_40d_jerk_v031_signal),
  ("f10cs_f10_candle_sequence_patterns_markov_60d_jerk_v032_signal",["open","close"],f10cs_f10_candle_sequence_patterns_markov_60d_jerk_v032_signal),
  ("f10cs_f10_candle_sequence_patterns_bodyrat_2d_jerk_v033_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_bodyrat_2d_jerk_v033_signal),
  ("f10cs_f10_candle_sequence_patterns_bodymon_5d_jerk_v034_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bodymon_5d_jerk_v034_signal),
  ("f10cs_f10_candle_sequence_patterns_bodycum_3d_jerk_v035_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_bodycum_3d_jerk_v035_signal),
  ("f10cs_f10_candle_sequence_patterns_bodyaccl_4d_jerk_v036_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bodyaccl_4d_jerk_v036_signal),
  ("f10cs_f10_candle_sequence_patterns_rngbull_5d_jerk_v037_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_rngbull_5d_jerk_v037_signal),
  ("f10cs_f10_candle_sequence_patterns_rngbear_5d_jerk_v038_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_rngbear_5d_jerk_v038_signal),
  ("f10cs_f10_candle_sequence_patterns_volconf_10d_jerk_v039_signal",["open","close","volume"],f10cs_f10_candle_sequence_patterns_volconf_10d_jerk_v039_signal),
  ("f10cs_f10_candle_sequence_patterns_rngcontr_5d_jerk_v040_signal",["high","low"],f10cs_f10_candle_sequence_patterns_rngcontr_5d_jerk_v040_signal),
  ("f10cs_f10_candle_sequence_patterns_hangmans_2d_jerk_v041_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_hangmans_2d_jerk_v041_signal),
  ("f10cs_f10_candle_sequence_patterns_hammer_2d_jerk_v042_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_hammer_2d_jerk_v042_signal),
  ("f10cs_f10_candle_sequence_patterns_shootst_2d_jerk_v043_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_shootst_2d_jerk_v043_signal),
  ("f10cs_f10_candle_sequence_patterns_invhamr_2d_jerk_v044_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_invhamr_2d_jerk_v044_signal),
  ("f10cs_f10_candle_sequence_patterns_flag_10d_jerk_v045_signal",["open","close"],f10cs_f10_candle_sequence_patterns_flag_10d_jerk_v045_signal),
  ("f10cs_f10_candle_sequence_patterns_pennant_10d_jerk_v046_signal",["high","low","close"],f10cs_f10_candle_sequence_patterns_pennant_10d_jerk_v046_signal),
  ("f10cs_f10_candle_sequence_patterns_rise3m_5d_jerk_v047_signal",["open","close"],f10cs_f10_candle_sequence_patterns_rise3m_5d_jerk_v047_signal),
  ("f10cs_f10_candle_sequence_patterns_fall3m_5d_jerk_v048_signal",["open","close"],f10cs_f10_candle_sequence_patterns_fall3m_5d_jerk_v048_signal),
  ("f10cs_f10_candle_sequence_patterns_pressure_20d_jerk_v049_signal",["open","close"],f10cs_f10_candle_sequence_patterns_pressure_20d_jerk_v049_signal),
  ("f10cs_f10_candle_sequence_patterns_pressure_50d_jerk_v050_signal",["open","closeadj"],f10cs_f10_candle_sequence_patterns_pressure_50d_jerk_v050_signal),
  ("f10cs_f10_candle_sequence_patterns_seqskew_30d_jerk_v051_signal",["open","close"],f10cs_f10_candle_sequence_patterns_seqskew_30d_jerk_v051_signal),
  ("f10cs_f10_candle_sequence_patterns_seqkurt_40d_jerk_v052_signal",["open","closeadj"],f10cs_f10_candle_sequence_patterns_seqkurt_40d_jerk_v052_signal),
  ("f10cs_f10_candle_sequence_patterns_colac1_30d_jerk_v053_signal",["open","close"],f10cs_f10_candle_sequence_patterns_colac1_30d_jerk_v053_signal),
  ("f10cs_f10_candle_sequence_patterns_bodyac2_25d_jerk_v054_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bodyac2_25d_jerk_v054_signal),
  ("f10cs_f10_candle_sequence_patterns_engcnt_20d_jerk_v055_signal",["open","close"],f10cs_f10_candle_sequence_patterns_engcnt_20d_jerk_v055_signal),
  ("f10cs_f10_candle_sequence_patterns_softdoji_30d_jerk_v056_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_softdoji_30d_jerk_v056_signal),
  ("f10cs_f10_candle_sequence_patterns_engrank_30d_jerk_v057_signal",["open","close"],f10cs_f10_candle_sequence_patterns_engrank_30d_jerk_v057_signal),
  ("f10cs_f10_candle_sequence_patterns_bestbar_20d_jerk_v058_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bestbar_20d_jerk_v058_signal),
  ("f10cs_f10_candle_sequence_patterns_worstbar_20d_jerk_v059_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_worstbar_20d_jerk_v059_signal),
  ("f10cs_f10_candle_sequence_patterns_overlapr_5d_jerk_v060_signal",["high","low"],f10cs_f10_candle_sequence_patterns_overlapr_5d_jerk_v060_signal),
  ("f10cs_f10_candle_sequence_patterns_gapseq_10d_jerk_v061_signal",["open","close"],f10cs_f10_candle_sequence_patterns_gapseq_10d_jerk_v061_signal),
  ("f10cs_f10_candle_sequence_patterns_seqdrift_15d_jerk_v062_signal",["open","close"],f10cs_f10_candle_sequence_patterns_seqdrift_15d_jerk_v062_signal),
  ("f10cs_f10_candle_sequence_patterns_volimb_15d_jerk_v063_signal",["open","close","volume"],f10cs_f10_candle_sequence_patterns_volimb_15d_jerk_v063_signal),
  ("f10cs_f10_candle_sequence_patterns_brkout_20d_jerk_v064_signal",["high","low","close"],f10cs_f10_candle_sequence_patterns_brkout_20d_jerk_v064_signal),
  ("f10cs_f10_candle_sequence_patterns_revcomb_3d_jerk_v065_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_revcomb_3d_jerk_v065_signal),
  ("f10cs_f10_candle_sequence_patterns_contcomb_5d_jerk_v066_signal",["open","close"],f10cs_f10_candle_sequence_patterns_contcomb_5d_jerk_v066_signal),
  ("f10cs_f10_candle_sequence_patterns_topbot_8d_jerk_v067_signal",["high","low","close"],f10cs_f10_candle_sequence_patterns_topbot_8d_jerk_v067_signal),
  ("f10cs_f10_candle_sequence_patterns_swing_10d_jerk_v068_signal",["high","low"],f10cs_f10_candle_sequence_patterns_swing_10d_jerk_v068_signal),
  ("f10cs_f10_candle_sequence_patterns_bodyimb_10d_jerk_v069_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bodyimb_10d_jerk_v069_signal),
  ("f10cs_f10_candle_sequence_patterns_thrust_3d_jerk_v070_signal",["open","close"],f10cs_f10_candle_sequence_patterns_thrust_3d_jerk_v070_signal),
  ("f10cs_f10_candle_sequence_patterns_streakdiff_20d_jerk_v071_signal",["open","close"],f10cs_f10_candle_sequence_patterns_streakdiff_20d_jerk_v071_signal),
  ("f10cs_f10_candle_sequence_patterns_rngmom_8d_jerk_v072_signal",["high","low"],f10cs_f10_candle_sequence_patterns_rngmom_8d_jerk_v072_signal),
  ("f10cs_f10_candle_sequence_patterns_seqsharp_30d_jerk_v073_signal",["open","closeadj"],f10cs_f10_candle_sequence_patterns_seqsharp_30d_jerk_v073_signal),
  ("f10cs_f10_candle_sequence_patterns_3bartrk_3d_jerk_v074_signal",["close"],f10cs_f10_candle_sequence_patterns_3bartrk_3d_jerk_v074_signal),
  ("f10cs_f10_candle_sequence_patterns_pinbar_2d_jerk_v075_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_pinbar_2d_jerk_v075_signal),
  ("f10cs_f10_candle_sequence_patterns_bsidvr_2d_jerk_v076_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_bsidvr_2d_jerk_v076_signal),
  ("f10cs_f10_candle_sequence_patterns_concl3_3d_jerk_v077_signal",["close"],f10cs_f10_candle_sequence_patterns_concl3_3d_jerk_v077_signal),
  ("f10cs_f10_candle_sequence_patterns_gap2bdy_2d_jerk_v078_signal",["open","close"],f10cs_f10_candle_sequence_patterns_gap2bdy_2d_jerk_v078_signal),
  ("f10cs_f10_candle_sequence_patterns_2bartrk_2d_jerk_v079_signal",["close"],f10cs_f10_candle_sequence_patterns_2bartrk_2d_jerk_v079_signal),
  ("f10cs_f10_candle_sequence_patterns_bothshad_3d_jerk_v080_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_bothshad_3d_jerk_v080_signal),
  ("f10cs_f10_candle_sequence_patterns_riseclos_5d_jerk_v081_signal",["close"],f10cs_f10_candle_sequence_patterns_riseclos_5d_jerk_v081_signal),
  ("f10cs_f10_candle_sequence_patterns_clsclose_2d_jerk_v082_signal",["open","close"],f10cs_f10_candle_sequence_patterns_clsclose_2d_jerk_v082_signal),
  ("f10cs_f10_candle_sequence_patterns_thirteenseq_13d_jerk_v083_signal",["close"],f10cs_f10_candle_sequence_patterns_thirteenseq_13d_jerk_v083_signal),
  ("f10cs_f10_candle_sequence_patterns_dnsetup_9d_jerk_v084_signal",["close"],f10cs_f10_candle_sequence_patterns_dnsetup_9d_jerk_v084_signal),
  ("f10cs_f10_candle_sequence_patterns_islndrev_3d_jerk_v085_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_islndrev_3d_jerk_v085_signal),
  ("f10cs_f10_candle_sequence_patterns_winflwthru_3d_jerk_v086_signal",["open","close"],f10cs_f10_candle_sequence_patterns_winflwthru_3d_jerk_v086_signal),
  ("f10cs_f10_candle_sequence_patterns_losflwthru_3d_jerk_v087_signal",["open","close"],f10cs_f10_candle_sequence_patterns_losflwthru_3d_jerk_v087_signal),
  ("f10cs_f10_candle_sequence_patterns_engcnt_40d_jerk_v088_signal",["open","close"],f10cs_f10_candle_sequence_patterns_engcnt_40d_jerk_v088_signal),
  ("f10cs_f10_candle_sequence_patterns_haramicnt_30d_jerk_v089_signal",["open","close"],f10cs_f10_candle_sequence_patterns_haramicnt_30d_jerk_v089_signal),
  ("f10cs_f10_candle_sequence_patterns_dojicnt_25d_jerk_v090_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_dojicnt_25d_jerk_v090_signal),
  ("f10cs_f10_candle_sequence_patterns_revcnt_20d_jerk_v091_signal",["open","close"],f10cs_f10_candle_sequence_patterns_revcnt_20d_jerk_v091_signal),
  ("f10cs_f10_candle_sequence_patterns_btopcnt_30d_jerk_v092_signal",["high","low","close"],f10cs_f10_candle_sequence_patterns_btopcnt_30d_jerk_v092_signal),
  ("f10cs_f10_candle_sequence_patterns_bbotcnt_30d_jerk_v093_signal",["high","low","close"],f10cs_f10_candle_sequence_patterns_bbotcnt_30d_jerk_v093_signal),
  ("f10cs_f10_candle_sequence_patterns_distinsd_10d_jerk_v094_signal",["high","low"],f10cs_f10_candle_sequence_patterns_distinsd_10d_jerk_v094_signal),
  ("f10cs_f10_candle_sequence_patterns_distoutsd_10d_jerk_v095_signal",["high","low"],f10cs_f10_candle_sequence_patterns_distoutsd_10d_jerk_v095_signal),
  ("f10cs_f10_candle_sequence_patterns_disteng_2d_jerk_v096_signal",["open","close"],f10cs_f10_candle_sequence_patterns_disteng_2d_jerk_v096_signal),
  ("f10cs_f10_candle_sequence_patterns_disthar_2d_jerk_v097_signal",["open","close"],f10cs_f10_candle_sequence_patterns_disthar_2d_jerk_v097_signal),
  ("f10cs_f10_candle_sequence_patterns_engdiff_20d_jerk_v098_signal",["open","close"],f10cs_f10_candle_sequence_patterns_engdiff_20d_jerk_v098_signal),
  ("f10cs_f10_candle_sequence_patterns_insoutd_30d_jerk_v099_signal",["high","low"],f10cs_f10_candle_sequence_patterns_insoutd_30d_jerk_v099_signal),
  ("f10cs_f10_candle_sequence_patterns_hhstk_2d_jerk_v100_signal",["high"],f10cs_f10_candle_sequence_patterns_hhstk_2d_jerk_v100_signal),
  ("f10cs_f10_candle_sequence_patterns_llstk_2d_jerk_v101_signal",["low"],f10cs_f10_candle_sequence_patterns_llstk_2d_jerk_v101_signal),
  ("f10cs_f10_candle_sequence_patterns_upclstk_2d_jerk_v102_signal",["close"],f10cs_f10_candle_sequence_patterns_upclstk_2d_jerk_v102_signal),
  ("f10cs_f10_candle_sequence_patterns_dnclstk_2d_jerk_v103_signal",["close"],f10cs_f10_candle_sequence_patterns_dnclstk_2d_jerk_v103_signal),
  ("f10cs_f10_candle_sequence_patterns_engsmean_20d_jerk_v104_signal",["open","close"],f10cs_f10_candle_sequence_patterns_engsmean_20d_jerk_v104_signal),
  ("f10cs_f10_candle_sequence_patterns_harasm_30d_jerk_v105_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_harasm_30d_jerk_v105_signal),
  ("f10cs_f10_candle_sequence_patterns_tweezm_20d_jerk_v106_signal",["high","low"],f10cs_f10_candle_sequence_patterns_tweezm_20d_jerk_v106_signal),
  ("f10cs_f10_candle_sequence_patterns_highbrk_10d_jerk_v107_signal",["high","close"],f10cs_f10_candle_sequence_patterns_highbrk_10d_jerk_v107_signal),
  ("f10cs_f10_candle_sequence_patterns_lowbrk_10d_jerk_v108_signal",["low","close"],f10cs_f10_candle_sequence_patterns_lowbrk_10d_jerk_v108_signal),
  ("f10cs_f10_candle_sequence_patterns_failbrk_15d_jerk_v109_signal",["high","close"],f10cs_f10_candle_sequence_patterns_failbrk_15d_jerk_v109_signal),
  ("f10cs_f10_candle_sequence_patterns_colcons_15d_jerk_v110_signal",["open","close"],f10cs_f10_candle_sequence_patterns_colcons_15d_jerk_v110_signal),
  ("f10cs_f10_candle_sequence_patterns_oprng_10d_jerk_v111_signal",["open","high","low"],f10cs_f10_candle_sequence_patterns_oprng_10d_jerk_v111_signal),
  ("f10cs_f10_candle_sequence_patterns_clrng_15d_jerk_v112_signal",["high","low","close"],f10cs_f10_candle_sequence_patterns_clrng_15d_jerk_v112_signal),
  ("f10cs_f10_candle_sequence_patterns_volup_20d_jerk_v113_signal",["open","close","volume"],f10cs_f10_candle_sequence_patterns_volup_20d_jerk_v113_signal),
  ("f10cs_f10_candle_sequence_patterns_voldn_20d_jerk_v114_signal",["open","close","volume"],f10cs_f10_candle_sequence_patterns_voldn_20d_jerk_v114_signal),
  ("f10cs_f10_candle_sequence_patterns_volclmx_30d_jerk_v115_signal",["open","close","volume"],f10cs_f10_candle_sequence_patterns_volclmx_30d_jerk_v115_signal),
  ("f10cs_f10_candle_sequence_patterns_clseac1_25d_jerk_v116_signal",["close"],f10cs_f10_candle_sequence_patterns_clseac1_25d_jerk_v116_signal),
  ("f10cs_f10_candle_sequence_patterns_rngac1_30d_jerk_v117_signal",["high","low"],f10cs_f10_candle_sequence_patterns_rngac1_30d_jerk_v117_signal),
  ("f10cs_f10_candle_sequence_patterns_bodyrs_30d_jerk_v118_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bodyrs_30d_jerk_v118_signal),
  ("f10cs_f10_candle_sequence_patterns_seqent_30d_jerk_v119_signal",["open","close"],f10cs_f10_candle_sequence_patterns_seqent_30d_jerk_v119_signal),
  ("f10cs_f10_candle_sequence_patterns_runlen_50d_jerk_v120_signal",["open","close"],f10cs_f10_candle_sequence_patterns_runlen_50d_jerk_v120_signal),
  ("f10cs_f10_candle_sequence_patterns_engrank_50d_jerk_v121_signal",["open","close"],f10cs_f10_candle_sequence_patterns_engrank_50d_jerk_v121_signal),
  ("f10cs_f10_candle_sequence_patterns_brngrnk_30d_jerk_v122_signal",["high","low"],f10cs_f10_candle_sequence_patterns_brngrnk_30d_jerk_v122_signal),
  ("f10cs_f10_candle_sequence_patterns_seqdir_60d_jerk_v123_signal",["closeadj"],f10cs_f10_candle_sequence_patterns_seqdir_60d_jerk_v123_signal),
  ("f10cs_f10_candle_sequence_patterns_seqac1_80d_jerk_v124_signal",["closeadj"],f10cs_f10_candle_sequence_patterns_seqac1_80d_jerk_v124_signal),
  ("f10cs_f10_candle_sequence_patterns_drmonotn_40d_jerk_v125_signal",["closeadj"],f10cs_f10_candle_sequence_patterns_drmonotn_40d_jerk_v125_signal),
  ("f10cs_f10_candle_sequence_patterns_bodyvar_25d_jerk_v126_signal",["open","close"],f10cs_f10_candle_sequence_patterns_bodyvar_25d_jerk_v126_signal),
  ("f10cs_f10_candle_sequence_patterns_seqvar_30d_jerk_v127_signal",["high","low"],f10cs_f10_candle_sequence_patterns_seqvar_30d_jerk_v127_signal),
  ("f10cs_f10_candle_sequence_patterns_clmad_20d_jerk_v128_signal",["close"],f10cs_f10_candle_sequence_patterns_clmad_20d_jerk_v128_signal),
  ("f10cs_f10_candle_sequence_patterns_morncnt_50d_jerk_v129_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_morncnt_50d_jerk_v129_signal),
  ("f10cs_f10_candle_sequence_patterns_evencnt_50d_jerk_v130_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_evencnt_50d_jerk_v130_signal),
  ("f10cs_f10_candle_sequence_patterns_3soldcnt_40d_jerk_v131_signal",["open","close"],f10cs_f10_candle_sequence_patterns_3soldcnt_40d_jerk_v131_signal),
  ("f10cs_f10_candle_sequence_patterns_3crowcnt_40d_jerk_v132_signal",["open","close"],f10cs_f10_candle_sequence_patterns_3crowcnt_40d_jerk_v132_signal),
  ("f10cs_f10_candle_sequence_patterns_acmrange_20d_jerk_v133_signal",["high","low"],f10cs_f10_candle_sequence_patterns_acmrange_20d_jerk_v133_signal),
  ("f10cs_f10_candle_sequence_patterns_clseyema_15d_jerk_v134_signal",["close","open"],f10cs_f10_candle_sequence_patterns_clseyema_15d_jerk_v134_signal),
  ("f10cs_f10_candle_sequence_patterns_clshema_15d_jerk_v135_signal",["close","open"],f10cs_f10_candle_sequence_patterns_clshema_15d_jerk_v135_signal),
  ("f10cs_f10_candle_sequence_patterns_inssbur_10d_jerk_v136_signal",["high","low","close"],f10cs_f10_candle_sequence_patterns_inssbur_10d_jerk_v136_signal),
  ("f10cs_f10_candle_sequence_patterns_outscont_10d_jerk_v137_signal",["high","low","close"],f10cs_f10_candle_sequence_patterns_outscont_10d_jerk_v137_signal),
  ("f10cs_f10_candle_sequence_patterns_innbody_3d_jerk_v138_signal",["open","close"],f10cs_f10_candle_sequence_patterns_innbody_3d_jerk_v138_signal),
  ("f10cs_f10_candle_sequence_patterns_clsmag_5d_jerk_v139_signal",["close","open"],f10cs_f10_candle_sequence_patterns_clsmag_5d_jerk_v139_signal),
  ("f10cs_f10_candle_sequence_patterns_volpeak_15d_jerk_v140_signal",["volume","close","open"],f10cs_f10_candle_sequence_patterns_volpeak_15d_jerk_v140_signal),
  ("f10cs_f10_candle_sequence_patterns_voltrough_15d_jerk_v141_signal",["volume","close","open"],f10cs_f10_candle_sequence_patterns_voltrough_15d_jerk_v141_signal),
  ("f10cs_f10_candle_sequence_patterns_gapfilcnt_20d_jerk_v142_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_gapfilcnt_20d_jerk_v142_signal),
  ("f10cs_f10_candle_sequence_patterns_gapfollow_20d_jerk_v143_signal",["open","close"],f10cs_f10_candle_sequence_patterns_gapfollow_20d_jerk_v143_signal),
  ("f10cs_f10_candle_sequence_patterns_consec_25d_jerk_v144_signal",["open","close"],f10cs_f10_candle_sequence_patterns_consec_25d_jerk_v144_signal),
  ("f10cs_f10_candle_sequence_patterns_pinrng_30d_jerk_v145_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_pinrng_30d_jerk_v145_signal),
  ("f10cs_f10_candle_sequence_patterns_emadev_3d_jerk_v146_signal",["close","open"],f10cs_f10_candle_sequence_patterns_emadev_3d_jerk_v146_signal),
  ("f10cs_f10_candle_sequence_patterns_hlbal_15d_jerk_v147_signal",["high","low"],f10cs_f10_candle_sequence_patterns_hlbal_15d_jerk_v147_signal),
  ("f10cs_f10_candle_sequence_patterns_clseopn_8d_jerk_v148_signal",["open","close"],f10cs_f10_candle_sequence_patterns_clseopn_8d_jerk_v148_signal),
  ("f10cs_f10_candle_sequence_patterns_clblopn_8d_jerk_v149_signal",["open","high","low","close"],f10cs_f10_candle_sequence_patterns_clblopn_8d_jerk_v149_signal),
  ("f10cs_f10_candle_sequence_patterns_evenodd_20d_jerk_v150_signal",["open","close"],f10cs_f10_candle_sequence_patterns_evenodd_20d_jerk_v150_signal),
]
f10_candle_sequence_patterns_jerk_001_150_REGISTRY = {n: {"inputs": list(i), "func": f} for n, i, f in _R}

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
 for name, entry in f10_candle_sequence_patterns_jerk_001_150_REGISTRY.items():
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
 aligned = aligned.replace([np.inf,-np.inf],np.nan)
 corr = aligned.corr(min_periods=50).abs()
 np.fill_diagonal(corr.values, 0.0)
 max_corr = float(corr.max().max())
 if max_corr > 0.95:
  print(f"FAILING max |corr| = {max_corr:.4f}. Top pairs:")
  s = corr.unstack().sort_values(ascending=False)
  s = s[s > 0.94].head(40)
  seen = set()
  for (a, bb), v in s.items():
   if a < bb and (a, bb) not in seen:
    seen.add((a, bb))
    print(f"  {a}  vs  {bb}  ->  {v:.4f}")
 assert max_corr <= 0.95 + 1e-9, f"max pairwise |corr|={max_corr:.4f} exceeds 0.95"
 print(f"OK jerk_001_150: {len(results)} features, max |corr|={max_corr:.4f}, coverage_ok={frac:.2%}")

if __name__ == "__main__":
 _self_test()
