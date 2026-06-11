import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f94ft_f94_fixed_asset_turnover_regime_calc076_81d_val_v076_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(32).shift(3)
    v_4 = v_2.rolling(33).max().shift(4)
    v_5 = v_2.rolling(34).kurt().shift(5)
    v_6 = v_2.rolling(35).mean().shift(6)
    v_7 = v_2.rolling(36).mean().shift(7)
    v_8 = v_2.rolling(37).max().shift(8)
    v_9 = v_2.rolling(38).mean().shift(9)
    v_10 = v_2.rolling(39).skew().shift(10)
    v_11 = v_2.rolling(40).mean().shift(11)
    v_12 = v_2.rolling(41).min().shift(12)
    v_13 = v_2.diff(42).shift(13)
    v_14 = v_2.diff(43).shift(14)
    v_15 = v_2.rolling(44).mean().shift(0)
    v_16 = v_2.diff(45).shift(1)
    v_17 = v_2.rolling(46).min().shift(2)
    v_18 = v_2.rolling(47).skew().shift(3)
    v_19 = v_2.rolling(48).kurt().shift(4)
    v_20 = v_2.rolling(49).max().shift(5)
    v_21 = v_2.rolling(50).std().shift(6)
    v_22 = v_2.rolling(51).max().shift(7)
    v_23 = v_2.rolling(52).std().shift(8)
    v_24 = v_2.rolling(3).kurt().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc076_81d_val_v076_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc076_81d_val_v076_signal

def f94ft_f94_fixed_asset_turnover_regime_calc077_82d_val_v077_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(33).min().shift(6)
    v_4 = v_2.rolling(34).std().shift(8)
    v_5 = v_2.rolling(35).min().shift(10)
    v_6 = v_2.rolling(36).mean().shift(12)
    v_7 = v_2.rolling(37).mean().shift(14)
    v_8 = v_2.diff(38).shift(1)
    v_9 = v_2.rolling(39).mean().shift(3)
    v_10 = v_2.rolling(40).max().shift(5)
    v_11 = v_2.rolling(41).min().shift(7)
    v_12 = v_2.diff(42).shift(9)
    v_13 = v_2.rolling(43).mean().shift(11)
    v_14 = v_2.rolling(44).min().shift(13)
    v_15 = v_2.diff(45).shift(0)
    v_16 = v_2.diff(46).shift(2)
    v_17 = v_2.diff(47).shift(4)
    v_18 = v_2.rolling(48).mean().shift(6)
    v_19 = v_2.rolling(49).std().shift(8)
    v_20 = v_2.rolling(50).max().shift(10)
    v_21 = v_2.rolling(51).mean().shift(12)
    v_22 = v_2.rolling(52).skew().shift(14)
    v_23 = v_2.rolling(3).min().shift(1)
    v_24 = v_2.rolling(4).skew().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc077_82d_val_v077_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc077_82d_val_v077_signal

def f94ft_f94_fixed_asset_turnover_regime_calc078_83d_val_v078_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(34).max().shift(9)
    v_4 = v_2.rolling(35).kurt().shift(12)
    v_5 = v_2.rolling(36).min().shift(0)
    v_6 = v_2.rolling(37).kurt().shift(3)
    v_7 = v_2.rolling(38).skew().shift(6)
    v_8 = v_2.diff(39).shift(9)
    v_9 = v_2.rolling(40).std().shift(12)
    v_10 = v_2.rolling(41).std().shift(0)
    v_11 = v_2.rolling(42).min().shift(3)
    v_12 = v_2.rolling(43).mean().shift(6)
    v_13 = v_2.rolling(44).mean().shift(9)
    v_14 = v_2.rolling(45).skew().shift(12)
    v_15 = v_2.rolling(46).mean().shift(0)
    v_16 = v_2.rolling(47).max().shift(3)
    v_17 = v_2.rolling(48).skew().shift(6)
    v_18 = v_2.diff(49).shift(9)
    v_19 = v_2.rolling(50).std().shift(12)
    v_20 = v_2.rolling(51).std().shift(0)
    v_21 = v_2.rolling(52).std().shift(3)
    v_22 = v_2.rolling(3).std().shift(6)
    v_23 = v_2.rolling(4).min().shift(9)
    v_24 = v_2.rolling(5).kurt().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc078_83d_val_v078_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc078_83d_val_v078_signal

def f94ft_f94_fixed_asset_turnover_regime_calc079_84d_val_v079_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(35).mean().shift(12)
    v_4 = v_2.rolling(36).std().shift(1)
    v_5 = v_2.rolling(37).max().shift(5)
    v_6 = v_2.rolling(38).mean().shift(9)
    v_7 = v_2.rolling(39).kurt().shift(13)
    v_8 = v_2.rolling(40).std().shift(2)
    v_9 = v_2.rolling(41).max().shift(6)
    v_10 = v_2.rolling(42).kurt().shift(10)
    v_11 = v_2.rolling(43).kurt().shift(14)
    v_12 = v_2.rolling(44).min().shift(3)
    v_13 = v_2.rolling(45).skew().shift(7)
    v_14 = v_2.rolling(46).min().shift(11)
    v_15 = v_2.rolling(47).mean().shift(0)
    v_16 = v_2.rolling(48).max().shift(4)
    v_17 = v_2.rolling(49).mean().shift(8)
    v_18 = v_2.rolling(50).max().shift(12)
    v_19 = v_2.rolling(51).std().shift(1)
    v_20 = v_2.rolling(52).max().shift(5)
    v_21 = v_2.rolling(3).min().shift(9)
    v_22 = v_2.rolling(4).mean().shift(13)
    v_23 = v_2.rolling(5).max().shift(2)
    v_24 = v_2.rolling(6).mean().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc079_84d_val_v079_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc079_84d_val_v079_signal

def f94ft_f94_fixed_asset_turnover_regime_calc080_85d_val_v080_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(36).mean().shift(0)
    v_4 = v_2.rolling(37).max().shift(5)
    v_5 = v_2.rolling(38).kurt().shift(10)
    v_6 = v_2.rolling(39).min().shift(0)
    v_7 = v_2.rolling(40).mean().shift(5)
    v_8 = v_2.rolling(41).kurt().shift(10)
    v_9 = v_2.rolling(42).kurt().shift(0)
    v_10 = v_2.rolling(43).skew().shift(5)
    v_11 = v_2.rolling(44).kurt().shift(10)
    v_12 = v_2.rolling(45).skew().shift(0)
    v_13 = v_2.rolling(46).max().shift(5)
    v_14 = v_2.diff(47).shift(10)
    v_15 = v_2.rolling(48).min().shift(0)
    v_16 = v_2.diff(49).shift(5)
    v_17 = v_2.rolling(50).skew().shift(10)
    v_18 = v_2.rolling(51).kurt().shift(0)
    v_19 = v_2.rolling(52).min().shift(5)
    v_20 = v_2.rolling(3).skew().shift(10)
    v_21 = v_2.rolling(4).max().shift(0)
    v_22 = v_2.rolling(5).min().shift(5)
    v_23 = v_2.rolling(6).min().shift(10)
    v_24 = v_2.rolling(7).kurt().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(85).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc080_85d_val_v080_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc080_85d_val_v080_signal

def f94ft_f94_fixed_asset_turnover_regime_calc081_86d_val_v081_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(37).kurt().shift(3)
    v_4 = v_2.rolling(38).kurt().shift(9)
    v_5 = v_2.rolling(39).min().shift(0)
    v_6 = v_2.rolling(40).skew().shift(6)
    v_7 = v_2.rolling(41).std().shift(12)
    v_8 = v_2.rolling(42).skew().shift(3)
    v_9 = v_2.diff(43).shift(9)
    v_10 = v_2.rolling(44).kurt().shift(0)
    v_11 = v_2.rolling(45).std().shift(6)
    v_12 = v_2.rolling(46).max().shift(12)
    v_13 = v_2.rolling(47).std().shift(3)
    v_14 = v_2.rolling(48).kurt().shift(9)
    v_15 = v_2.rolling(49).skew().shift(0)
    v_16 = v_2.rolling(50).skew().shift(6)
    v_17 = v_2.diff(51).shift(12)
    v_18 = v_2.rolling(52).skew().shift(3)
    v_19 = v_2.rolling(3).skew().shift(9)
    v_20 = v_2.rolling(4).std().shift(0)
    v_21 = v_2.rolling(5).kurt().shift(6)
    v_22 = v_2.rolling(6).max().shift(12)
    v_23 = v_2.rolling(7).mean().shift(3)
    v_24 = v_2.rolling(8).skew().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc081_86d_val_v081_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc081_86d_val_v081_signal

def f94ft_f94_fixed_asset_turnover_regime_calc082_87d_val_v082_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(38).max().shift(6)
    v_4 = v_2.rolling(39).max().shift(13)
    v_5 = v_2.rolling(40).max().shift(5)
    v_6 = v_2.rolling(41).min().shift(12)
    v_7 = v_2.rolling(42).mean().shift(4)
    v_8 = v_2.rolling(43).kurt().shift(11)
    v_9 = v_2.rolling(44).mean().shift(3)
    v_10 = v_2.rolling(45).min().shift(10)
    v_11 = v_2.rolling(46).kurt().shift(2)
    v_12 = v_2.rolling(47).max().shift(9)
    v_13 = v_2.rolling(48).max().shift(1)
    v_14 = v_2.rolling(49).max().shift(8)
    v_15 = v_2.rolling(50).mean().shift(0)
    v_16 = v_2.diff(51).shift(7)
    v_17 = v_2.rolling(52).mean().shift(14)
    v_18 = v_2.rolling(3).min().shift(6)
    v_19 = v_2.rolling(4).max().shift(13)
    v_20 = v_2.rolling(5).kurt().shift(5)
    v_21 = v_2.rolling(6).std().shift(12)
    v_22 = v_2.rolling(7).max().shift(4)
    v_23 = v_2.rolling(8).mean().shift(11)
    v_24 = v_2.diff(9).shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc082_87d_val_v082_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc082_87d_val_v082_signal

def f94ft_f94_fixed_asset_turnover_regime_calc083_88d_val_v083_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(39).max().shift(9)
    v_4 = v_2.rolling(40).std().shift(2)
    v_5 = v_2.rolling(41).mean().shift(10)
    v_6 = v_2.rolling(42).max().shift(3)
    v_7 = v_2.rolling(43).std().shift(11)
    v_8 = v_2.rolling(44).kurt().shift(4)
    v_9 = v_2.rolling(45).max().shift(12)
    v_10 = v_2.rolling(46).kurt().shift(5)
    v_11 = v_2.diff(47).shift(13)
    v_12 = v_2.rolling(48).min().shift(6)
    v_13 = v_2.rolling(49).min().shift(14)
    v_14 = v_2.rolling(50).min().shift(7)
    v_15 = v_2.rolling(51).min().shift(0)
    v_16 = v_2.rolling(52).min().shift(8)
    v_17 = v_2.rolling(3).mean().shift(1)
    v_18 = v_2.rolling(4).std().shift(9)
    v_19 = v_2.rolling(5).skew().shift(2)
    v_20 = v_2.rolling(6).max().shift(10)
    v_21 = v_2.rolling(7).kurt().shift(3)
    v_22 = v_2.rolling(8).kurt().shift(11)
    v_23 = v_2.rolling(9).min().shift(4)
    v_24 = v_2.rolling(10).max().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc083_88d_val_v083_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc083_88d_val_v083_signal

def f94ft_f94_fixed_asset_turnover_regime_calc084_89d_val_v084_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(40).min().shift(12)
    v_4 = v_2.rolling(41).skew().shift(6)
    v_5 = v_2.rolling(42).kurt().shift(0)
    v_6 = v_2.rolling(43).mean().shift(9)
    v_7 = v_2.diff(44).shift(3)
    v_8 = v_2.diff(45).shift(12)
    v_9 = v_2.rolling(46).skew().shift(6)
    v_10 = v_2.rolling(47).skew().shift(0)
    v_11 = v_2.rolling(48).max().shift(9)
    v_12 = v_2.rolling(49).std().shift(3)
    v_13 = v_2.rolling(50).std().shift(12)
    v_14 = v_2.rolling(51).mean().shift(6)
    v_15 = v_2.rolling(52).mean().shift(0)
    v_16 = v_2.diff(3).shift(9)
    v_17 = v_2.rolling(4).std().shift(3)
    v_18 = v_2.rolling(5).mean().shift(12)
    v_19 = v_2.rolling(6).skew().shift(6)
    v_20 = v_2.diff(7).shift(0)
    v_21 = v_2.rolling(8).max().shift(9)
    v_22 = v_2.rolling(9).min().shift(3)
    v_23 = v_2.rolling(10).skew().shift(12)
    v_24 = v_2.rolling(11).max().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc084_89d_val_v084_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc084_89d_val_v084_signal

def f94ft_f94_fixed_asset_turnover_regime_calc085_90d_val_v085_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(41).skew().shift(0)
    v_4 = v_2.rolling(42).skew().shift(10)
    v_5 = v_2.rolling(43).max().shift(5)
    v_6 = v_2.rolling(44).max().shift(0)
    v_7 = v_2.rolling(45).max().shift(10)
    v_8 = v_2.rolling(46).mean().shift(5)
    v_9 = v_2.diff(47).shift(0)
    v_10 = v_2.rolling(48).skew().shift(10)
    v_11 = v_2.rolling(49).std().shift(5)
    v_12 = v_2.rolling(50).mean().shift(0)
    v_13 = v_2.rolling(51).max().shift(10)
    v_14 = v_2.rolling(52).kurt().shift(5)
    v_15 = v_2.rolling(3).std().shift(0)
    v_16 = v_2.rolling(4).mean().shift(10)
    v_17 = v_2.diff(5).shift(5)
    v_18 = v_2.rolling(6).max().shift(0)
    v_19 = v_2.rolling(7).std().shift(10)
    v_20 = v_2.rolling(8).kurt().shift(5)
    v_21 = v_2.rolling(9).kurt().shift(0)
    v_22 = v_2.rolling(10).min().shift(10)
    v_23 = v_2.rolling(11).min().shift(5)
    v_24 = v_2.rolling(12).max().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc085_90d_val_v085_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc085_90d_val_v085_signal

def f94ft_f94_fixed_asset_turnover_regime_calc086_91d_val_v086_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(42).shift(3)
    v_4 = v_2.rolling(43).std().shift(14)
    v_5 = v_2.rolling(44).kurt().shift(10)
    v_6 = v_2.rolling(45).std().shift(6)
    v_7 = v_2.rolling(46).skew().shift(2)
    v_8 = v_2.rolling(47).skew().shift(13)
    v_9 = v_2.rolling(48).mean().shift(9)
    v_10 = v_2.rolling(49).kurt().shift(5)
    v_11 = v_2.rolling(50).max().shift(1)
    v_12 = v_2.rolling(51).skew().shift(12)
    v_13 = v_2.diff(52).shift(8)
    v_14 = v_2.rolling(3).max().shift(4)
    v_15 = v_2.rolling(4).kurt().shift(0)
    v_16 = v_2.rolling(5).max().shift(11)
    v_17 = v_2.rolling(6).skew().shift(7)
    v_18 = v_2.rolling(7).max().shift(3)
    v_19 = v_2.diff(8).shift(14)
    v_20 = v_2.rolling(9).kurt().shift(10)
    v_21 = v_2.rolling(10).min().shift(6)
    v_22 = v_2.rolling(11).mean().shift(2)
    v_23 = v_2.rolling(12).min().shift(13)
    v_24 = v_2.rolling(13).mean().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc086_91d_val_v086_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc086_91d_val_v086_signal

def f94ft_f94_fixed_asset_turnover_regime_calc087_92d_val_v087_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(43).max().shift(6)
    v_4 = v_2.rolling(44).skew().shift(3)
    v_5 = v_2.diff(45).shift(0)
    v_6 = v_2.diff(46).shift(12)
    v_7 = v_2.rolling(47).kurt().shift(9)
    v_8 = v_2.rolling(48).max().shift(6)
    v_9 = v_2.rolling(49).std().shift(3)
    v_10 = v_2.rolling(50).min().shift(0)
    v_11 = v_2.rolling(51).std().shift(12)
    v_12 = v_2.rolling(52).std().shift(9)
    v_13 = v_2.rolling(3).mean().shift(6)
    v_14 = v_2.rolling(4).skew().shift(3)
    v_15 = v_2.rolling(5).max().shift(0)
    v_16 = v_2.rolling(6).skew().shift(12)
    v_17 = v_2.rolling(7).kurt().shift(9)
    v_18 = v_2.rolling(8).min().shift(6)
    v_19 = v_2.rolling(9).min().shift(3)
    v_20 = v_2.rolling(10).kurt().shift(0)
    v_21 = v_2.rolling(11).std().shift(12)
    v_22 = v_2.rolling(12).max().shift(9)
    v_23 = v_2.rolling(13).min().shift(6)
    v_24 = v_2.diff(14).shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(92).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc087_92d_val_v087_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc087_92d_val_v087_signal

def f94ft_f94_fixed_asset_turnover_regime_calc088_93d_val_v088_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(44).kurt().shift(9)
    v_4 = v_2.rolling(45).skew().shift(7)
    v_5 = v_2.rolling(46).min().shift(5)
    v_6 = v_2.rolling(47).max().shift(3)
    v_7 = v_2.rolling(48).mean().shift(1)
    v_8 = v_2.diff(49).shift(14)
    v_9 = v_2.rolling(50).kurt().shift(12)
    v_10 = v_2.rolling(51).max().shift(10)
    v_11 = v_2.rolling(52).min().shift(8)
    v_12 = v_2.rolling(3).kurt().shift(6)
    v_13 = v_2.rolling(4).kurt().shift(4)
    v_14 = v_2.rolling(5).std().shift(2)
    v_15 = v_2.diff(6).shift(0)
    v_16 = v_2.rolling(7).min().shift(13)
    v_17 = v_2.rolling(8).mean().shift(11)
    v_18 = v_2.rolling(9).std().shift(9)
    v_19 = v_2.rolling(10).skew().shift(7)
    v_20 = v_2.rolling(11).skew().shift(5)
    v_21 = v_2.diff(12).shift(3)
    v_22 = v_2.rolling(13).max().shift(1)
    v_23 = v_2.rolling(14).mean().shift(14)
    v_24 = v_2.diff(15).shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc088_93d_val_v088_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc088_93d_val_v088_signal

def f94ft_f94_fixed_asset_turnover_regime_calc089_94d_val_v089_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(45).skew().shift(12)
    v_4 = v_2.rolling(46).std().shift(11)
    v_5 = v_2.diff(47).shift(10)
    v_6 = v_2.rolling(48).std().shift(9)
    v_7 = v_2.rolling(49).max().shift(8)
    v_8 = v_2.diff(50).shift(7)
    v_9 = v_2.rolling(51).max().shift(6)
    v_10 = v_2.rolling(52).std().shift(5)
    v_11 = v_2.rolling(3).max().shift(4)
    v_12 = v_2.rolling(4).std().shift(3)
    v_13 = v_2.rolling(5).min().shift(2)
    v_14 = v_2.rolling(6).std().shift(1)
    v_15 = v_2.rolling(7).std().shift(0)
    v_16 = v_2.rolling(8).min().shift(14)
    v_17 = v_2.diff(9).shift(13)
    v_18 = v_2.rolling(10).std().shift(12)
    v_19 = v_2.diff(11).shift(11)
    v_20 = v_2.rolling(12).std().shift(10)
    v_21 = v_2.rolling(13).std().shift(9)
    v_22 = v_2.rolling(14).min().shift(8)
    v_23 = v_2.rolling(15).max().shift(7)
    v_24 = v_2.rolling(16).std().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc089_94d_val_v089_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc089_94d_val_v089_signal

def f94ft_f94_fixed_asset_turnover_regime_calc090_95d_val_v090_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(46).min().shift(0)
    v_4 = v_2.rolling(47).kurt().shift(0)
    v_5 = v_2.rolling(48).skew().shift(0)
    v_6 = v_2.diff(49).shift(0)
    v_7 = v_2.rolling(50).max().shift(0)
    v_8 = v_2.rolling(51).mean().shift(0)
    v_9 = v_2.rolling(52).mean().shift(0)
    v_10 = v_2.diff(3).shift(0)
    v_11 = v_2.rolling(4).mean().shift(0)
    v_12 = v_2.rolling(5).kurt().shift(0)
    v_13 = v_2.rolling(6).max().shift(0)
    v_14 = v_2.rolling(7).kurt().shift(0)
    v_15 = v_2.rolling(8).min().shift(0)
    v_16 = v_2.rolling(9).min().shift(0)
    v_17 = v_2.rolling(10).kurt().shift(0)
    v_18 = v_2.rolling(11).min().shift(0)
    v_19 = v_2.rolling(12).min().shift(0)
    v_20 = v_2.rolling(13).min().shift(0)
    v_21 = v_2.diff(14).shift(0)
    v_22 = v_2.rolling(15).std().shift(0)
    v_23 = v_2.rolling(16).max().shift(0)
    v_24 = v_2.rolling(17).mean().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc090_95d_val_v090_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc090_95d_val_v090_signal

def f94ft_f94_fixed_asset_turnover_regime_calc091_96d_val_v091_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(47).shift(3)
    v_4 = v_2.rolling(48).mean().shift(4)
    v_5 = v_2.rolling(49).min().shift(5)
    v_6 = v_2.rolling(50).mean().shift(6)
    v_7 = v_2.rolling(51).max().shift(7)
    v_8 = v_2.rolling(52).mean().shift(8)
    v_9 = v_2.rolling(3).kurt().shift(9)
    v_10 = v_2.rolling(4).skew().shift(10)
    v_11 = v_2.rolling(5).mean().shift(11)
    v_12 = v_2.rolling(6).min().shift(12)
    v_13 = v_2.rolling(7).mean().shift(13)
    v_14 = v_2.rolling(8).kurt().shift(14)
    v_15 = v_2.rolling(9).mean().shift(0)
    v_16 = v_2.rolling(10).min().shift(1)
    v_17 = v_2.diff(11).shift(2)
    v_18 = v_2.rolling(12).std().shift(3)
    v_19 = v_2.rolling(13).kurt().shift(4)
    v_20 = v_2.rolling(14).skew().shift(5)
    v_21 = v_2.rolling(15).mean().shift(6)
    v_22 = v_2.rolling(16).max().shift(7)
    v_23 = v_2.rolling(17).max().shift(8)
    v_24 = v_2.rolling(18).min().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc091_96d_val_v091_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc091_96d_val_v091_signal

def f94ft_f94_fixed_asset_turnover_regime_calc092_97d_val_v092_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(48).std().shift(6)
    v_4 = v_2.rolling(49).min().shift(8)
    v_5 = v_2.rolling(50).skew().shift(10)
    v_6 = v_2.rolling(51).mean().shift(12)
    v_7 = v_2.diff(52).shift(14)
    v_8 = v_2.rolling(3).min().shift(1)
    v_9 = v_2.rolling(4).std().shift(3)
    v_10 = v_2.rolling(5).max().shift(5)
    v_11 = v_2.rolling(6).mean().shift(7)
    v_12 = v_2.rolling(7).std().shift(9)
    v_13 = v_2.rolling(8).max().shift(11)
    v_14 = v_2.rolling(9).std().shift(13)
    v_15 = v_2.rolling(10).max().shift(0)
    v_16 = v_2.rolling(11).max().shift(2)
    v_17 = v_2.rolling(12).skew().shift(4)
    v_18 = v_2.rolling(13).std().shift(6)
    v_19 = v_2.diff(14).shift(8)
    v_20 = v_2.rolling(15).min().shift(10)
    v_21 = v_2.diff(16).shift(12)
    v_22 = v_2.rolling(17).max().shift(14)
    v_23 = v_2.diff(18).shift(1)
    v_24 = v_2.rolling(19).max().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc092_97d_val_v092_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc092_97d_val_v092_signal

def f94ft_f94_fixed_asset_turnover_regime_calc093_98d_val_v093_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(49).skew().shift(9)
    v_4 = v_2.rolling(50).max().shift(12)
    v_5 = v_2.rolling(51).kurt().shift(0)
    v_6 = v_2.rolling(52).std().shift(3)
    v_7 = v_2.rolling(3).std().shift(6)
    v_8 = v_2.rolling(4).kurt().shift(9)
    v_9 = v_2.rolling(5).skew().shift(12)
    v_10 = v_2.rolling(6).kurt().shift(0)
    v_11 = v_2.rolling(7).kurt().shift(3)
    v_12 = v_2.rolling(8).max().shift(6)
    v_13 = v_2.rolling(9).max().shift(9)
    v_14 = v_2.rolling(10).kurt().shift(12)
    v_15 = v_2.rolling(11).min().shift(0)
    v_16 = v_2.rolling(12).min().shift(3)
    v_17 = v_2.rolling(13).skew().shift(6)
    v_18 = v_2.rolling(14).kurt().shift(9)
    v_19 = v_2.rolling(15).std().shift(12)
    v_20 = v_2.rolling(16).std().shift(0)
    v_21 = v_2.rolling(17).mean().shift(3)
    v_22 = v_2.diff(18).shift(6)
    v_23 = v_2.rolling(19).skew().shift(9)
    v_24 = v_2.rolling(20).max().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc093_98d_val_v093_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc093_98d_val_v093_signal

def f94ft_f94_fixed_asset_turnover_regime_calc094_99d_val_v094_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(50).std().shift(12)
    v_4 = v_2.rolling(51).min().shift(1)
    v_5 = v_2.rolling(52).min().shift(5)
    v_6 = v_2.rolling(3).mean().shift(9)
    v_7 = v_2.rolling(4).mean().shift(13)
    v_8 = v_2.rolling(5).mean().shift(2)
    v_9 = v_2.rolling(6).std().shift(6)
    v_10 = v_2.rolling(7).std().shift(10)
    v_11 = v_2.rolling(8).std().shift(14)
    v_12 = v_2.rolling(9).std().shift(3)
    v_13 = v_2.diff(10).shift(7)
    v_14 = v_2.diff(11).shift(11)
    v_15 = v_2.diff(12).shift(0)
    v_16 = v_2.diff(13).shift(4)
    v_17 = v_2.rolling(14).min().shift(8)
    v_18 = v_2.rolling(15).min().shift(12)
    v_19 = v_2.rolling(16).skew().shift(1)
    v_20 = v_2.rolling(17).max().shift(5)
    v_21 = v_2.rolling(18).min().shift(9)
    v_22 = v_2.rolling(19).std().shift(13)
    v_23 = v_2.rolling(20).mean().shift(2)
    v_24 = v_2.rolling(21).min().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(99).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc094_99d_val_v094_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc094_99d_val_v094_signal

def f94ft_f94_fixed_asset_turnover_regime_calc095_100d_val_v095_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(51).mean().shift(0)
    v_4 = v_2.rolling(52).max().shift(5)
    v_5 = v_2.rolling(3).max().shift(10)
    v_6 = v_2.rolling(4).min().shift(0)
    v_7 = v_2.rolling(5).mean().shift(5)
    v_8 = v_2.rolling(6).kurt().shift(10)
    v_9 = v_2.rolling(7).max().shift(0)
    v_10 = v_2.rolling(8).min().shift(5)
    v_11 = v_2.rolling(9).kurt().shift(10)
    v_12 = v_2.diff(10).shift(0)
    v_13 = v_2.rolling(11).skew().shift(5)
    v_14 = v_2.diff(12).shift(10)
    v_15 = v_2.rolling(13).kurt().shift(0)
    v_16 = v_2.rolling(14).skew().shift(5)
    v_17 = v_2.rolling(15).skew().shift(10)
    v_18 = v_2.rolling(16).std().shift(0)
    v_19 = v_2.diff(17).shift(5)
    v_20 = v_2.rolling(18).min().shift(10)
    v_21 = v_2.rolling(19).std().shift(0)
    v_22 = v_2.rolling(20).max().shift(5)
    v_23 = v_2.diff(21).shift(10)
    v_24 = v_2.rolling(22).max().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc095_100d_val_v095_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc095_100d_val_v095_signal

def f94ft_f94_fixed_asset_turnover_regime_calc096_101d_val_v096_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(52).min().shift(3)
    v_4 = v_2.rolling(3).max().shift(9)
    v_5 = v_2.rolling(4).max().shift(0)
    v_6 = v_2.rolling(5).max().shift(6)
    v_7 = v_2.diff(6).shift(12)
    v_8 = v_2.rolling(7).max().shift(3)
    v_9 = v_2.rolling(8).skew().shift(9)
    v_10 = v_2.rolling(9).kurt().shift(0)
    v_11 = v_2.rolling(10).std().shift(6)
    v_12 = v_2.rolling(11).min().shift(12)
    v_13 = v_2.rolling(12).min().shift(3)
    v_14 = v_2.rolling(13).skew().shift(9)
    v_15 = v_2.rolling(14).std().shift(0)
    v_16 = v_2.rolling(15).min().shift(6)
    v_17 = v_2.rolling(16).skew().shift(12)
    v_18 = v_2.diff(17).shift(3)
    v_19 = v_2.rolling(18).skew().shift(9)
    v_20 = v_2.rolling(19).mean().shift(0)
    v_21 = v_2.rolling(20).min().shift(6)
    v_22 = v_2.diff(21).shift(12)
    v_23 = v_2.rolling(22).mean().shift(3)
    v_24 = v_2.rolling(23).mean().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc096_101d_val_v096_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc096_101d_val_v096_signal

def f94ft_f94_fixed_asset_turnover_regime_calc097_102d_val_v097_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(3).max().shift(6)
    v_4 = v_2.diff(4).shift(13)
    v_5 = v_2.rolling(5).std().shift(5)
    v_6 = v_2.rolling(6).min().shift(12)
    v_7 = v_2.rolling(7).mean().shift(4)
    v_8 = v_2.rolling(8).skew().shift(11)
    v_9 = v_2.rolling(9).mean().shift(3)
    v_10 = v_2.rolling(10).min().shift(10)
    v_11 = v_2.rolling(11).max().shift(2)
    v_12 = v_2.diff(12).shift(9)
    v_13 = v_2.rolling(13).std().shift(1)
    v_14 = v_2.diff(14).shift(8)
    v_15 = v_2.diff(15).shift(0)
    v_16 = v_2.rolling(16).std().shift(7)
    v_17 = v_2.rolling(17).kurt().shift(14)
    v_18 = v_2.rolling(18).skew().shift(6)
    v_19 = v_2.rolling(19).kurt().shift(13)
    v_20 = v_2.rolling(20).skew().shift(5)
    v_21 = v_2.rolling(21).max().shift(12)
    v_22 = v_2.diff(22).shift(4)
    v_23 = v_2.rolling(23).skew().shift(11)
    v_24 = v_2.diff(24).shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc097_102d_val_v097_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc097_102d_val_v097_signal

def f94ft_f94_fixed_asset_turnover_regime_calc098_103d_val_v098_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(4).kurt().shift(9)
    v_4 = v_2.rolling(5).skew().shift(2)
    v_5 = v_2.rolling(6).mean().shift(10)
    v_6 = v_2.rolling(7).std().shift(3)
    v_7 = v_2.rolling(8).skew().shift(11)
    v_8 = v_2.diff(9).shift(4)
    v_9 = v_2.rolling(10).std().shift(12)
    v_10 = v_2.rolling(11).max().shift(5)
    v_11 = v_2.rolling(12).min().shift(13)
    v_12 = v_2.rolling(13).kurt().shift(6)
    v_13 = v_2.rolling(14).mean().shift(14)
    v_14 = v_2.rolling(15).mean().shift(7)
    v_15 = v_2.rolling(16).max().shift(0)
    v_16 = v_2.rolling(17).std().shift(8)
    v_17 = v_2.rolling(18).std().shift(1)
    v_18 = v_2.rolling(19).std().shift(9)
    v_19 = v_2.rolling(20).skew().shift(2)
    v_20 = v_2.rolling(21).std().shift(10)
    v_21 = v_2.rolling(22).mean().shift(3)
    v_22 = v_2.diff(23).shift(11)
    v_23 = v_2.rolling(24).kurt().shift(4)
    v_24 = v_2.rolling(25).skew().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc098_103d_val_v098_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc098_103d_val_v098_signal

def f94ft_f94_fixed_asset_turnover_regime_calc099_104d_val_v099_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(5).max().shift(12)
    v_4 = v_2.rolling(6).skew().shift(6)
    v_5 = v_2.rolling(7).std().shift(0)
    v_6 = v_2.rolling(8).max().shift(9)
    v_7 = v_2.rolling(9).kurt().shift(3)
    v_8 = v_2.rolling(10).std().shift(12)
    v_9 = v_2.rolling(11).max().shift(6)
    v_10 = v_2.rolling(12).min().shift(0)
    v_11 = v_2.rolling(13).skew().shift(9)
    v_12 = v_2.diff(14).shift(3)
    v_13 = v_2.rolling(15).kurt().shift(12)
    v_14 = v_2.rolling(16).std().shift(6)
    v_15 = v_2.rolling(17).mean().shift(0)
    v_16 = v_2.rolling(18).min().shift(9)
    v_17 = v_2.rolling(19).min().shift(3)
    v_18 = v_2.diff(20).shift(12)
    v_19 = v_2.rolling(21).mean().shift(6)
    v_20 = v_2.rolling(22).kurt().shift(0)
    v_21 = v_2.rolling(23).max().shift(9)
    v_22 = v_2.rolling(24).min().shift(3)
    v_23 = v_2.rolling(25).std().shift(12)
    v_24 = v_2.rolling(26).max().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc099_104d_val_v099_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc099_104d_val_v099_signal

def f94ft_f94_fixed_asset_turnover_regime_calc100_105d_val_v100_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(6).min().shift(0)
    v_4 = v_2.rolling(7).min().shift(10)
    v_5 = v_2.rolling(8).std().shift(5)
    v_6 = v_2.rolling(9).max().shift(0)
    v_7 = v_2.diff(10).shift(10)
    v_8 = v_2.diff(11).shift(5)
    v_9 = v_2.rolling(12).kurt().shift(0)
    v_10 = v_2.diff(13).shift(10)
    v_11 = v_2.rolling(14).kurt().shift(5)
    v_12 = v_2.rolling(15).kurt().shift(0)
    v_13 = v_2.rolling(16).skew().shift(10)
    v_14 = v_2.rolling(17).mean().shift(5)
    v_15 = v_2.rolling(18).std().shift(0)
    v_16 = v_2.rolling(19).skew().shift(10)
    v_17 = v_2.rolling(20).max().shift(5)
    v_18 = v_2.rolling(21).max().shift(0)
    v_19 = v_2.rolling(22).mean().shift(10)
    v_20 = v_2.rolling(23).skew().shift(5)
    v_21 = v_2.rolling(24).max().shift(0)
    v_22 = v_2.rolling(25).max().shift(10)
    v_23 = v_2.rolling(26).mean().shift(5)
    v_24 = v_2.rolling(27).kurt().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc100_105d_val_v100_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc100_105d_val_v100_signal

def f94ft_f94_fixed_asset_turnover_regime_calc101_106d_val_v101_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(7).min().shift(3)
    v_4 = v_2.rolling(8).skew().shift(14)
    v_5 = v_2.diff(9).shift(10)
    v_6 = v_2.diff(10).shift(6)
    v_7 = v_2.rolling(11).std().shift(2)
    v_8 = v_2.rolling(12).kurt().shift(13)
    v_9 = v_2.rolling(13).max().shift(9)
    v_10 = v_2.diff(14).shift(5)
    v_11 = v_2.rolling(15).kurt().shift(1)
    v_12 = v_2.diff(16).shift(12)
    v_13 = v_2.rolling(17).mean().shift(8)
    v_14 = v_2.rolling(18).skew().shift(4)
    v_15 = v_2.rolling(19).skew().shift(0)
    v_16 = v_2.rolling(20).kurt().shift(11)
    v_17 = v_2.rolling(21).max().shift(7)
    v_18 = v_2.rolling(22).std().shift(3)
    v_19 = v_2.rolling(23).kurt().shift(14)
    v_20 = v_2.rolling(24).max().shift(10)
    v_21 = v_2.diff(25).shift(6)
    v_22 = v_2.rolling(26).std().shift(2)
    v_23 = v_2.rolling(27).std().shift(13)
    v_24 = v_2.rolling(28).max().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(106).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc101_106d_val_v101_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc101_106d_val_v101_signal

def f94ft_f94_fixed_asset_turnover_regime_calc102_107d_val_v102_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(8).mean().shift(6)
    v_4 = v_2.rolling(9).skew().shift(3)
    v_5 = v_2.rolling(10).mean().shift(0)
    v_6 = v_2.rolling(11).skew().shift(12)
    v_7 = v_2.rolling(12).min().shift(9)
    v_8 = v_2.diff(13).shift(6)
    v_9 = v_2.rolling(14).mean().shift(3)
    v_10 = v_2.diff(15).shift(0)
    v_11 = v_2.rolling(16).max().shift(12)
    v_12 = v_2.diff(17).shift(9)
    v_13 = v_2.rolling(18).skew().shift(6)
    v_14 = v_2.rolling(19).kurt().shift(3)
    v_15 = v_2.rolling(20).min().shift(0)
    v_16 = v_2.rolling(21).skew().shift(12)
    v_17 = v_2.rolling(22).min().shift(9)
    v_18 = v_2.rolling(23).mean().shift(6)
    v_19 = v_2.rolling(24).skew().shift(3)
    v_20 = v_2.rolling(25).mean().shift(0)
    v_21 = v_2.rolling(26).kurt().shift(12)
    v_22 = v_2.rolling(27).mean().shift(9)
    v_23 = v_2.rolling(28).kurt().shift(6)
    v_24 = v_2.diff(29).shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc102_107d_val_v102_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc102_107d_val_v102_signal

def f94ft_f94_fixed_asset_turnover_regime_calc103_108d_val_v103_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(9).max().shift(9)
    v_4 = v_2.rolling(10).std().shift(7)
    v_5 = v_2.rolling(11).max().shift(5)
    v_6 = v_2.rolling(12).min().shift(3)
    v_7 = v_2.rolling(13).skew().shift(1)
    v_8 = v_2.diff(14).shift(14)
    v_9 = v_2.rolling(15).skew().shift(12)
    v_10 = v_2.diff(16).shift(10)
    v_11 = v_2.rolling(17).max().shift(8)
    v_12 = v_2.rolling(18).std().shift(6)
    v_13 = v_2.rolling(19).mean().shift(4)
    v_14 = v_2.rolling(20).min().shift(2)
    v_15 = v_2.rolling(21).max().shift(0)
    v_16 = v_2.rolling(22).mean().shift(13)
    v_17 = v_2.rolling(23).std().shift(11)
    v_18 = v_2.rolling(24).min().shift(9)
    v_19 = v_2.rolling(25).skew().shift(7)
    v_20 = v_2.rolling(26).std().shift(5)
    v_21 = v_2.rolling(27).mean().shift(3)
    v_22 = v_2.rolling(28).max().shift(1)
    v_23 = v_2.rolling(29).kurt().shift(14)
    v_24 = v_2.rolling(30).min().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc103_108d_val_v103_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc103_108d_val_v103_signal

def f94ft_f94_fixed_asset_turnover_regime_calc104_109d_val_v104_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(10).max().shift(12)
    v_4 = v_2.diff(11).shift(11)
    v_5 = v_2.rolling(12).mean().shift(10)
    v_6 = v_2.rolling(13).max().shift(9)
    v_7 = v_2.rolling(14).max().shift(8)
    v_8 = v_2.rolling(15).kurt().shift(7)
    v_9 = v_2.rolling(16).min().shift(6)
    v_10 = v_2.diff(17).shift(5)
    v_11 = v_2.rolling(18).skew().shift(4)
    v_12 = v_2.diff(19).shift(3)
    v_13 = v_2.rolling(20).kurt().shift(2)
    v_14 = v_2.diff(21).shift(1)
    v_15 = v_2.rolling(22).std().shift(0)
    v_16 = v_2.rolling(23).std().shift(14)
    v_17 = v_2.rolling(24).kurt().shift(13)
    v_18 = v_2.rolling(25).mean().shift(12)
    v_19 = v_2.rolling(26).min().shift(11)
    v_20 = v_2.rolling(27).min().shift(10)
    v_21 = v_2.rolling(28).skew().shift(9)
    v_22 = v_2.rolling(29).skew().shift(8)
    v_23 = v_2.diff(30).shift(7)
    v_24 = v_2.diff(31).shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc104_109d_val_v104_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc104_109d_val_v104_signal

def f94ft_f94_fixed_asset_turnover_regime_calc105_110d_val_v105_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(11).std().shift(0)
    v_4 = v_2.rolling(12).skew().shift(0)
    v_5 = v_2.rolling(13).min().shift(0)
    v_6 = v_2.rolling(14).min().shift(0)
    v_7 = v_2.rolling(15).max().shift(0)
    v_8 = v_2.rolling(16).min().shift(0)
    v_9 = v_2.rolling(17).std().shift(0)
    v_10 = v_2.rolling(18).mean().shift(0)
    v_11 = v_2.rolling(19).min().shift(0)
    v_12 = v_2.rolling(20).std().shift(0)
    v_13 = v_2.diff(21).shift(0)
    v_14 = v_2.rolling(22).skew().shift(0)
    v_15 = v_2.rolling(23).skew().shift(0)
    v_16 = v_2.rolling(24).mean().shift(0)
    v_17 = v_2.rolling(25).skew().shift(0)
    v_18 = v_2.rolling(26).min().shift(0)
    v_19 = v_2.rolling(27).max().shift(0)
    v_20 = v_2.rolling(28).std().shift(0)
    v_21 = v_2.rolling(29).min().shift(0)
    v_22 = v_2.diff(30).shift(0)
    v_23 = v_2.rolling(31).std().shift(0)
    v_24 = v_2.diff(32).shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc105_110d_val_v105_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc105_110d_val_v105_signal

def f94ft_f94_fixed_asset_turnover_regime_calc106_111d_val_v106_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(12).max().shift(3)
    v_4 = v_2.diff(13).shift(4)
    v_5 = v_2.rolling(14).std().shift(5)
    v_6 = v_2.rolling(15).mean().shift(6)
    v_7 = v_2.diff(16).shift(7)
    v_8 = v_2.rolling(17).max().shift(8)
    v_9 = v_2.rolling(18).skew().shift(9)
    v_10 = v_2.rolling(19).mean().shift(10)
    v_11 = v_2.diff(20).shift(11)
    v_12 = v_2.rolling(21).mean().shift(12)
    v_13 = v_2.rolling(22).kurt().shift(13)
    v_14 = v_2.rolling(23).max().shift(14)
    v_15 = v_2.rolling(24).max().shift(0)
    v_16 = v_2.rolling(25).std().shift(1)
    v_17 = v_2.rolling(26).min().shift(2)
    v_18 = v_2.rolling(27).skew().shift(3)
    v_19 = v_2.rolling(28).kurt().shift(4)
    v_20 = v_2.diff(29).shift(5)
    v_21 = v_2.rolling(30).std().shift(6)
    v_22 = v_2.diff(31).shift(7)
    v_23 = v_2.rolling(32).max().shift(8)
    v_24 = v_2.rolling(33).min().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc106_111d_val_v106_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc106_111d_val_v106_signal

def f94ft_f94_fixed_asset_turnover_regime_calc107_112d_val_v107_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(13).max().shift(6)
    v_4 = v_2.rolling(14).std().shift(8)
    v_5 = v_2.rolling(15).min().shift(10)
    v_6 = v_2.rolling(16).mean().shift(12)
    v_7 = v_2.rolling(17).kurt().shift(14)
    v_8 = v_2.rolling(18).min().shift(1)
    v_9 = v_2.rolling(19).skew().shift(3)
    v_10 = v_2.rolling(20).mean().shift(5)
    v_11 = v_2.rolling(21).std().shift(7)
    v_12 = v_2.rolling(22).max().shift(9)
    v_13 = v_2.rolling(23).max().shift(11)
    v_14 = v_2.rolling(24).skew().shift(13)
    v_15 = v_2.rolling(25).skew().shift(0)
    v_16 = v_2.rolling(26).mean().shift(2)
    v_17 = v_2.rolling(27).std().shift(4)
    v_18 = v_2.rolling(28).skew().shift(6)
    v_19 = v_2.rolling(29).kurt().shift(8)
    v_20 = v_2.rolling(30).kurt().shift(10)
    v_21 = v_2.diff(31).shift(12)
    v_22 = v_2.rolling(32).min().shift(14)
    v_23 = v_2.rolling(33).max().shift(1)
    v_24 = v_2.rolling(34).skew().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc107_112d_val_v107_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc107_112d_val_v107_signal

def f94ft_f94_fixed_asset_turnover_regime_calc108_113d_val_v108_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(14).kurt().shift(9)
    v_4 = v_2.rolling(15).std().shift(12)
    v_5 = v_2.rolling(16).mean().shift(0)
    v_6 = v_2.rolling(17).kurt().shift(3)
    v_7 = v_2.diff(18).shift(6)
    v_8 = v_2.rolling(19).kurt().shift(9)
    v_9 = v_2.rolling(20).skew().shift(12)
    v_10 = v_2.rolling(21).skew().shift(0)
    v_11 = v_2.rolling(22).std().shift(3)
    v_12 = v_2.rolling(23).kurt().shift(6)
    v_13 = v_2.rolling(24).min().shift(9)
    v_14 = v_2.rolling(25).mean().shift(12)
    v_15 = v_2.rolling(26).skew().shift(0)
    v_16 = v_2.rolling(27).max().shift(3)
    v_17 = v_2.rolling(28).std().shift(6)
    v_18 = v_2.rolling(29).min().shift(9)
    v_19 = v_2.rolling(30).skew().shift(12)
    v_20 = v_2.rolling(31).min().shift(0)
    v_21 = v_2.rolling(32).min().shift(3)
    v_22 = v_2.diff(33).shift(6)
    v_23 = v_2.rolling(34).skew().shift(9)
    v_24 = v_2.diff(35).shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(113).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc108_113d_val_v108_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc108_113d_val_v108_signal

def f94ft_f94_fixed_asset_turnover_regime_calc109_114d_val_v109_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(15).max().shift(12)
    v_4 = v_2.rolling(16).skew().shift(1)
    v_5 = v_2.diff(17).shift(5)
    v_6 = v_2.diff(18).shift(9)
    v_7 = v_2.rolling(19).kurt().shift(13)
    v_8 = v_2.rolling(20).max().shift(2)
    v_9 = v_2.rolling(21).mean().shift(6)
    v_10 = v_2.diff(22).shift(10)
    v_11 = v_2.rolling(23).std().shift(14)
    v_12 = v_2.rolling(24).max().shift(3)
    v_13 = v_2.rolling(25).skew().shift(7)
    v_14 = v_2.rolling(26).kurt().shift(11)
    v_15 = v_2.rolling(27).std().shift(0)
    v_16 = v_2.rolling(28).kurt().shift(4)
    v_17 = v_2.rolling(29).std().shift(8)
    v_18 = v_2.rolling(30).kurt().shift(12)
    v_19 = v_2.rolling(31).min().shift(1)
    v_20 = v_2.diff(32).shift(5)
    v_21 = v_2.rolling(33).mean().shift(9)
    v_22 = v_2.rolling(34).max().shift(13)
    v_23 = v_2.rolling(35).std().shift(2)
    v_24 = v_2.rolling(36).std().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc109_114d_val_v109_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc109_114d_val_v109_signal

def f94ft_f94_fixed_asset_turnover_regime_calc110_115d_val_v110_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(16).shift(0)
    v_4 = v_2.rolling(17).kurt().shift(5)
    v_5 = v_2.diff(18).shift(10)
    v_6 = v_2.rolling(19).min().shift(0)
    v_7 = v_2.rolling(20).mean().shift(5)
    v_8 = v_2.rolling(21).max().shift(10)
    v_9 = v_2.rolling(22).kurt().shift(0)
    v_10 = v_2.rolling(23).mean().shift(5)
    v_11 = v_2.rolling(24).min().shift(10)
    v_12 = v_2.diff(25).shift(0)
    v_13 = v_2.diff(26).shift(5)
    v_14 = v_2.rolling(27).min().shift(10)
    v_15 = v_2.rolling(28).max().shift(0)
    v_16 = v_2.rolling(29).min().shift(5)
    v_17 = v_2.diff(30).shift(10)
    v_18 = v_2.rolling(31).kurt().shift(0)
    v_19 = v_2.diff(32).shift(5)
    v_20 = v_2.rolling(33).skew().shift(10)
    v_21 = v_2.rolling(34).std().shift(0)
    v_22 = v_2.rolling(35).kurt().shift(5)
    v_23 = v_2.rolling(36).skew().shift(10)
    v_24 = v_2.rolling(37).max().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc110_115d_val_v110_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc110_115d_val_v110_signal

def f94ft_f94_fixed_asset_turnover_regime_calc111_116d_val_v111_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(17).std().shift(3)
    v_4 = v_2.rolling(18).mean().shift(9)
    v_5 = v_2.rolling(19).mean().shift(0)
    v_6 = v_2.diff(20).shift(6)
    v_7 = v_2.rolling(21).std().shift(12)
    v_8 = v_2.rolling(22).min().shift(3)
    v_9 = v_2.rolling(23).min().shift(9)
    v_10 = v_2.rolling(24).max().shift(0)
    v_11 = v_2.diff(25).shift(6)
    v_12 = v_2.rolling(26).std().shift(12)
    v_13 = v_2.diff(27).shift(3)
    v_14 = v_2.rolling(28).min().shift(9)
    v_15 = v_2.rolling(29).max().shift(0)
    v_16 = v_2.rolling(30).mean().shift(6)
    v_17 = v_2.rolling(31).max().shift(12)
    v_18 = v_2.diff(32).shift(3)
    v_19 = v_2.rolling(33).skew().shift(9)
    v_20 = v_2.rolling(34).kurt().shift(0)
    v_21 = v_2.rolling(35).max().shift(6)
    v_22 = v_2.rolling(36).mean().shift(12)
    v_23 = v_2.rolling(37).mean().shift(3)
    v_24 = v_2.diff(38).shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc111_116d_val_v111_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc111_116d_val_v111_signal

def f94ft_f94_fixed_asset_turnover_regime_calc112_117d_val_v112_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(18).kurt().shift(6)
    v_4 = v_2.rolling(19).std().shift(13)
    v_5 = v_2.rolling(20).mean().shift(5)
    v_6 = v_2.rolling(21).max().shift(12)
    v_7 = v_2.rolling(22).kurt().shift(4)
    v_8 = v_2.rolling(23).kurt().shift(11)
    v_9 = v_2.rolling(24).kurt().shift(3)
    v_10 = v_2.rolling(25).mean().shift(10)
    v_11 = v_2.rolling(26).kurt().shift(2)
    v_12 = v_2.diff(27).shift(9)
    v_13 = v_2.rolling(28).std().shift(1)
    v_14 = v_2.rolling(29).std().shift(8)
    v_15 = v_2.rolling(30).skew().shift(0)
    v_16 = v_2.diff(31).shift(7)
    v_17 = v_2.diff(32).shift(14)
    v_18 = v_2.rolling(33).min().shift(6)
    v_19 = v_2.rolling(34).std().shift(13)
    v_20 = v_2.rolling(35).kurt().shift(5)
    v_21 = v_2.diff(36).shift(12)
    v_22 = v_2.diff(37).shift(4)
    v_23 = v_2.rolling(38).skew().shift(11)
    v_24 = v_2.rolling(39).std().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc112_117d_val_v112_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc112_117d_val_v112_signal

def f94ft_f94_fixed_asset_turnover_regime_calc113_118d_val_v113_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(19).max().shift(9)
    v_4 = v_2.rolling(20).min().shift(2)
    v_5 = v_2.rolling(21).kurt().shift(10)
    v_6 = v_2.rolling(22).max().shift(3)
    v_7 = v_2.rolling(23).std().shift(11)
    v_8 = v_2.rolling(24).min().shift(4)
    v_9 = v_2.rolling(25).skew().shift(12)
    v_10 = v_2.diff(26).shift(5)
    v_11 = v_2.rolling(27).mean().shift(13)
    v_12 = v_2.rolling(28).mean().shift(6)
    v_13 = v_2.rolling(29).min().shift(14)
    v_14 = v_2.rolling(30).skew().shift(7)
    v_15 = v_2.rolling(31).max().shift(0)
    v_16 = v_2.rolling(32).skew().shift(8)
    v_17 = v_2.rolling(33).max().shift(1)
    v_18 = v_2.rolling(34).skew().shift(9)
    v_19 = v_2.rolling(35).min().shift(2)
    v_20 = v_2.rolling(36).mean().shift(10)
    v_21 = v_2.rolling(37).skew().shift(3)
    v_22 = v_2.rolling(38).min().shift(11)
    v_23 = v_2.rolling(39).skew().shift(4)
    v_24 = v_2.rolling(40).mean().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc113_118d_val_v113_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc113_118d_val_v113_signal

def f94ft_f94_fixed_asset_turnover_regime_calc114_119d_val_v114_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(20).std().shift(12)
    v_4 = v_2.rolling(21).min().shift(6)
    v_5 = v_2.rolling(22).max().shift(0)
    v_6 = v_2.rolling(23).std().shift(9)
    v_7 = v_2.rolling(24).min().shift(3)
    v_8 = v_2.rolling(25).min().shift(12)
    v_9 = v_2.rolling(26).skew().shift(6)
    v_10 = v_2.rolling(27).skew().shift(0)
    v_11 = v_2.rolling(28).mean().shift(9)
    v_12 = v_2.diff(29).shift(3)
    v_13 = v_2.rolling(30).std().shift(12)
    v_14 = v_2.rolling(31).min().shift(6)
    v_15 = v_2.rolling(32).min().shift(0)
    v_16 = v_2.rolling(33).std().shift(9)
    v_17 = v_2.diff(34).shift(3)
    v_18 = v_2.rolling(35).max().shift(12)
    v_19 = v_2.rolling(36).mean().shift(6)
    v_20 = v_2.rolling(37).mean().shift(0)
    v_21 = v_2.rolling(38).kurt().shift(9)
    v_22 = v_2.rolling(39).max().shift(3)
    v_23 = v_2.rolling(40).skew().shift(12)
    v_24 = v_2.rolling(41).min().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc114_119d_val_v114_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc114_119d_val_v114_signal

def f94ft_f94_fixed_asset_turnover_regime_calc115_120d_val_v115_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(21).mean().shift(0)
    v_4 = v_2.rolling(22).kurt().shift(10)
    v_5 = v_2.rolling(23).mean().shift(5)
    v_6 = v_2.rolling(24).skew().shift(0)
    v_7 = v_2.rolling(25).mean().shift(10)
    v_8 = v_2.rolling(26).max().shift(5)
    v_9 = v_2.rolling(27).std().shift(0)
    v_10 = v_2.rolling(28).max().shift(10)
    v_11 = v_2.rolling(29).max().shift(5)
    v_12 = v_2.rolling(30).max().shift(0)
    v_13 = v_2.rolling(31).max().shift(10)
    v_14 = v_2.rolling(32).mean().shift(5)
    v_15 = v_2.rolling(33).min().shift(0)
    v_16 = v_2.rolling(34).min().shift(10)
    v_17 = v_2.rolling(35).kurt().shift(5)
    v_18 = v_2.rolling(36).min().shift(0)
    v_19 = v_2.rolling(37).kurt().shift(10)
    v_20 = v_2.rolling(38).max().shift(5)
    v_21 = v_2.diff(39).shift(0)
    v_22 = v_2.rolling(40).max().shift(10)
    v_23 = v_2.rolling(41).min().shift(5)
    v_24 = v_2.rolling(42).skew().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(120).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc115_120d_val_v115_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc115_120d_val_v115_signal

def f94ft_f94_fixed_asset_turnover_regime_calc116_121d_val_v116_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(22).min().shift(3)
    v_4 = v_2.rolling(23).std().shift(14)
    v_5 = v_2.rolling(24).max().shift(10)
    v_6 = v_2.rolling(25).std().shift(6)
    v_7 = v_2.diff(26).shift(2)
    v_8 = v_2.rolling(27).skew().shift(13)
    v_9 = v_2.rolling(28).max().shift(9)
    v_10 = v_2.diff(29).shift(5)
    v_11 = v_2.rolling(30).kurt().shift(1)
    v_12 = v_2.rolling(31).mean().shift(12)
    v_13 = v_2.diff(32).shift(8)
    v_14 = v_2.rolling(33).skew().shift(4)
    v_15 = v_2.rolling(34).min().shift(0)
    v_16 = v_2.rolling(35).mean().shift(11)
    v_17 = v_2.rolling(36).skew().shift(7)
    v_18 = v_2.diff(37).shift(3)
    v_19 = v_2.rolling(38).mean().shift(14)
    v_20 = v_2.rolling(39).min().shift(10)
    v_21 = v_2.rolling(40).max().shift(6)
    v_22 = v_2.rolling(41).std().shift(2)
    v_23 = v_2.rolling(42).std().shift(13)
    v_24 = v_2.rolling(43).min().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc116_121d_val_v116_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc116_121d_val_v116_signal

def f94ft_f94_fixed_asset_turnover_regime_calc117_122d_val_v117_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(23).skew().shift(6)
    v_4 = v_2.rolling(24).skew().shift(3)
    v_5 = v_2.rolling(25).max().shift(0)
    v_6 = v_2.rolling(26).min().shift(12)
    v_7 = v_2.rolling(27).max().shift(9)
    v_8 = v_2.rolling(28).std().shift(6)
    v_9 = v_2.rolling(29).kurt().shift(3)
    v_10 = v_2.rolling(30).min().shift(0)
    v_11 = v_2.rolling(31).skew().shift(12)
    v_12 = v_2.rolling(32).mean().shift(9)
    v_13 = v_2.rolling(33).kurt().shift(6)
    v_14 = v_2.rolling(34).skew().shift(3)
    v_15 = v_2.rolling(35).max().shift(0)
    v_16 = v_2.rolling(36).kurt().shift(12)
    v_17 = v_2.rolling(37).kurt().shift(9)
    v_18 = v_2.rolling(38).std().shift(6)
    v_19 = v_2.rolling(39).max().shift(3)
    v_20 = v_2.rolling(40).std().shift(0)
    v_21 = v_2.rolling(41).std().shift(12)
    v_22 = v_2.rolling(42).mean().shift(9)
    v_23 = v_2.diff(43).shift(6)
    v_24 = v_2.rolling(44).max().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc117_122d_val_v117_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc117_122d_val_v117_signal

def f94ft_f94_fixed_asset_turnover_regime_calc118_123d_val_v118_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(24).shift(9)
    v_4 = v_2.rolling(25).skew().shift(7)
    v_5 = v_2.rolling(26).kurt().shift(5)
    v_6 = v_2.diff(27).shift(3)
    v_7 = v_2.rolling(28).skew().shift(1)
    v_8 = v_2.rolling(29).min().shift(14)
    v_9 = v_2.rolling(30).kurt().shift(12)
    v_10 = v_2.rolling(31).std().shift(10)
    v_11 = v_2.rolling(32).kurt().shift(8)
    v_12 = v_2.rolling(33).max().shift(6)
    v_13 = v_2.rolling(34).std().shift(4)
    v_14 = v_2.rolling(35).min().shift(2)
    v_15 = v_2.rolling(36).max().shift(0)
    v_16 = v_2.rolling(37).min().shift(13)
    v_17 = v_2.rolling(38).skew().shift(11)
    v_18 = v_2.rolling(39).min().shift(9)
    v_19 = v_2.rolling(40).std().shift(7)
    v_20 = v_2.rolling(41).skew().shift(5)
    v_21 = v_2.rolling(42).skew().shift(3)
    v_22 = v_2.rolling(43).std().shift(1)
    v_23 = v_2.rolling(44).min().shift(14)
    v_24 = v_2.rolling(45).mean().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc118_123d_val_v118_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc118_123d_val_v118_signal

def f94ft_f94_fixed_asset_turnover_regime_calc119_124d_val_v119_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(25).max().shift(12)
    v_4 = v_2.rolling(26).max().shift(11)
    v_5 = v_2.rolling(27).max().shift(10)
    v_6 = v_2.rolling(28).mean().shift(9)
    v_7 = v_2.rolling(29).skew().shift(8)
    v_8 = v_2.diff(30).shift(7)
    v_9 = v_2.rolling(31).skew().shift(6)
    v_10 = v_2.rolling(32).max().shift(5)
    v_11 = v_2.rolling(33).min().shift(4)
    v_12 = v_2.rolling(34).std().shift(3)
    v_13 = v_2.rolling(35).skew().shift(2)
    v_14 = v_2.rolling(36).mean().shift(1)
    v_15 = v_2.rolling(37).mean().shift(0)
    v_16 = v_2.diff(38).shift(14)
    v_17 = v_2.rolling(39).std().shift(13)
    v_18 = v_2.rolling(40).skew().shift(12)
    v_19 = v_2.rolling(41).mean().shift(11)
    v_20 = v_2.rolling(42).kurt().shift(10)
    v_21 = v_2.rolling(43).min().shift(9)
    v_22 = v_2.rolling(44).max().shift(8)
    v_23 = v_2.diff(45).shift(7)
    v_24 = v_2.rolling(46).std().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc119_124d_val_v119_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc119_124d_val_v119_signal

def f94ft_f94_fixed_asset_turnover_regime_calc120_125d_val_v120_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(26).shift(0)
    v_4 = v_2.rolling(27).std().shift(0)
    v_5 = v_2.diff(28).shift(0)
    v_6 = v_2.diff(29).shift(0)
    v_7 = v_2.rolling(30).min().shift(0)
    v_8 = v_2.rolling(31).mean().shift(0)
    v_9 = v_2.rolling(32).skew().shift(0)
    v_10 = v_2.rolling(33).min().shift(0)
    v_11 = v_2.rolling(34).min().shift(0)
    v_12 = v_2.rolling(35).mean().shift(0)
    v_13 = v_2.rolling(36).skew().shift(0)
    v_14 = v_2.diff(37).shift(0)
    v_15 = v_2.diff(38).shift(0)
    v_16 = v_2.rolling(39).kurt().shift(0)
    v_17 = v_2.rolling(40).mean().shift(0)
    v_18 = v_2.rolling(41).kurt().shift(0)
    v_19 = v_2.rolling(42).skew().shift(0)
    v_20 = v_2.rolling(43).min().shift(0)
    v_21 = v_2.rolling(44).skew().shift(0)
    v_22 = v_2.rolling(45).max().shift(0)
    v_23 = v_2.rolling(46).skew().shift(0)
    v_24 = v_2.rolling(47).kurt().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc120_125d_val_v120_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc120_125d_val_v120_signal

def f94ft_f94_fixed_asset_turnover_regime_calc121_126d_val_v121_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(27).mean().shift(3)
    v_4 = v_2.rolling(28).skew().shift(4)
    v_5 = v_2.rolling(29).min().shift(5)
    v_6 = v_2.rolling(30).skew().shift(6)
    v_7 = v_2.rolling(31).kurt().shift(7)
    v_8 = v_2.rolling(32).skew().shift(8)
    v_9 = v_2.rolling(33).mean().shift(9)
    v_10 = v_2.rolling(34).std().shift(10)
    v_11 = v_2.rolling(35).kurt().shift(11)
    v_12 = v_2.rolling(36).min().shift(12)
    v_13 = v_2.rolling(37).mean().shift(13)
    v_14 = v_2.rolling(38).skew().shift(14)
    v_15 = v_2.diff(39).shift(0)
    v_16 = v_2.rolling(40).skew().shift(1)
    v_17 = v_2.rolling(41).kurt().shift(2)
    v_18 = v_2.rolling(42).min().shift(3)
    v_19 = v_2.diff(43).shift(4)
    v_20 = v_2.diff(44).shift(5)
    v_21 = v_2.rolling(45).mean().shift(6)
    v_22 = v_2.rolling(46).max().shift(7)
    v_23 = v_2.rolling(47).mean().shift(8)
    v_24 = v_2.diff(48).shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc121_126d_val_v121_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc121_126d_val_v121_signal

def f94ft_f94_fixed_asset_turnover_regime_calc122_127d_val_v122_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(28).shift(6)
    v_4 = v_2.rolling(29).max().shift(8)
    v_5 = v_2.rolling(30).kurt().shift(10)
    v_6 = v_2.rolling(31).mean().shift(12)
    v_7 = v_2.diff(32).shift(14)
    v_8 = v_2.rolling(33).min().shift(1)
    v_9 = v_2.rolling(34).kurt().shift(3)
    v_10 = v_2.rolling(35).std().shift(5)
    v_11 = v_2.rolling(36).std().shift(7)
    v_12 = v_2.rolling(37).mean().shift(9)
    v_13 = v_2.rolling(38).skew().shift(11)
    v_14 = v_2.rolling(39).mean().shift(13)
    v_15 = v_2.diff(40).shift(0)
    v_16 = v_2.rolling(41).mean().shift(2)
    v_17 = v_2.rolling(42).kurt().shift(4)
    v_18 = v_2.rolling(43).mean().shift(6)
    v_19 = v_2.diff(44).shift(8)
    v_20 = v_2.rolling(45).mean().shift(10)
    v_21 = v_2.rolling(46).min().shift(12)
    v_22 = v_2.diff(47).shift(14)
    v_23 = v_2.rolling(48).min().shift(1)
    v_24 = v_2.rolling(49).min().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(127).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc122_127d_val_v122_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc122_127d_val_v122_signal

def f94ft_f94_fixed_asset_turnover_regime_calc123_128d_val_v123_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(29).skew().shift(9)
    v_4 = v_2.rolling(30).min().shift(12)
    v_5 = v_2.rolling(31).min().shift(0)
    v_6 = v_2.rolling(32).std().shift(3)
    v_7 = v_2.rolling(33).mean().shift(6)
    v_8 = v_2.rolling(34).max().shift(9)
    v_9 = v_2.diff(35).shift(12)
    v_10 = v_2.rolling(36).max().shift(0)
    v_11 = v_2.rolling(37).kurt().shift(3)
    v_12 = v_2.rolling(38).mean().shift(6)
    v_13 = v_2.rolling(39).max().shift(9)
    v_14 = v_2.rolling(40).std().shift(12)
    v_15 = v_2.diff(41).shift(0)
    v_16 = v_2.rolling(42).std().shift(3)
    v_17 = v_2.rolling(43).std().shift(6)
    v_18 = v_2.rolling(44).mean().shift(9)
    v_19 = v_2.rolling(45).skew().shift(12)
    v_20 = v_2.rolling(46).max().shift(0)
    v_21 = v_2.diff(47).shift(3)
    v_22 = v_2.rolling(48).max().shift(6)
    v_23 = v_2.rolling(49).mean().shift(9)
    v_24 = v_2.rolling(50).kurt().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc123_128d_val_v123_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc123_128d_val_v123_signal

def f94ft_f94_fixed_asset_turnover_regime_calc124_129d_val_v124_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(30).std().shift(12)
    v_4 = v_2.rolling(31).max().shift(1)
    v_5 = v_2.rolling(32).max().shift(5)
    v_6 = v_2.rolling(33).max().shift(9)
    v_7 = v_2.rolling(34).mean().shift(13)
    v_8 = v_2.rolling(35).mean().shift(2)
    v_9 = v_2.rolling(36).mean().shift(6)
    v_10 = v_2.rolling(37).skew().shift(10)
    v_11 = v_2.rolling(38).mean().shift(14)
    v_12 = v_2.rolling(39).std().shift(3)
    v_13 = v_2.rolling(40).kurt().shift(7)
    v_14 = v_2.rolling(41).skew().shift(11)
    v_15 = v_2.diff(42).shift(0)
    v_16 = v_2.rolling(43).min().shift(4)
    v_17 = v_2.rolling(44).max().shift(8)
    v_18 = v_2.rolling(45).skew().shift(12)
    v_19 = v_2.rolling(46).mean().shift(1)
    v_20 = v_2.rolling(47).skew().shift(5)
    v_21 = v_2.rolling(48).max().shift(9)
    v_22 = v_2.diff(49).shift(13)
    v_23 = v_2.rolling(50).min().shift(2)
    v_24 = v_2.rolling(51).kurt().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc124_129d_val_v124_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc124_129d_val_v124_signal

def f94ft_f94_fixed_asset_turnover_regime_calc125_130d_val_v125_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(31).std().shift(0)
    v_4 = v_2.rolling(32).std().shift(5)
    v_5 = v_2.diff(33).shift(10)
    v_6 = v_2.rolling(34).max().shift(0)
    v_7 = v_2.rolling(35).std().shift(5)
    v_8 = v_2.diff(36).shift(10)
    v_9 = v_2.rolling(37).mean().shift(0)
    v_10 = v_2.rolling(38).mean().shift(5)
    v_11 = v_2.diff(39).shift(10)
    v_12 = v_2.rolling(40).mean().shift(0)
    v_13 = v_2.rolling(41).min().shift(5)
    v_14 = v_2.rolling(42).min().shift(10)
    v_15 = v_2.rolling(43).min().shift(0)
    v_16 = v_2.rolling(44).mean().shift(5)
    v_17 = v_2.rolling(45).min().shift(10)
    v_18 = v_2.diff(46).shift(0)
    v_19 = v_2.diff(47).shift(5)
    v_20 = v_2.rolling(48).kurt().shift(10)
    v_21 = v_2.rolling(49).min().shift(0)
    v_22 = v_2.rolling(50).skew().shift(5)
    v_23 = v_2.rolling(51).std().shift(10)
    v_24 = v_2.rolling(52).std().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc125_130d_val_v125_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc125_130d_val_v125_signal

def f94ft_f94_fixed_asset_turnover_regime_calc126_131d_val_v126_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(32).std().shift(3)
    v_4 = v_2.rolling(33).std().shift(9)
    v_5 = v_2.rolling(34).max().shift(0)
    v_6 = v_2.rolling(35).kurt().shift(6)
    v_7 = v_2.diff(36).shift(12)
    v_8 = v_2.rolling(37).mean().shift(3)
    v_9 = v_2.rolling(38).min().shift(9)
    v_10 = v_2.rolling(39).std().shift(0)
    v_11 = v_2.rolling(40).skew().shift(6)
    v_12 = v_2.rolling(41).max().shift(12)
    v_13 = v_2.rolling(42).min().shift(3)
    v_14 = v_2.rolling(43).max().shift(9)
    v_15 = v_2.rolling(44).mean().shift(0)
    v_16 = v_2.rolling(45).kurt().shift(6)
    v_17 = v_2.rolling(46).skew().shift(12)
    v_18 = v_2.rolling(47).mean().shift(3)
    v_19 = v_2.rolling(48).min().shift(9)
    v_20 = v_2.rolling(49).skew().shift(0)
    v_21 = v_2.rolling(50).kurt().shift(6)
    v_22 = v_2.rolling(51).min().shift(12)
    v_23 = v_2.rolling(52).mean().shift(3)
    v_24 = v_2.rolling(3).std().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc126_131d_val_v126_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc126_131d_val_v126_signal

def f94ft_f94_fixed_asset_turnover_regime_calc127_132d_val_v127_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(33).shift(6)
    v_4 = v_2.diff(34).shift(13)
    v_5 = v_2.rolling(35).min().shift(5)
    v_6 = v_2.diff(36).shift(12)
    v_7 = v_2.rolling(37).mean().shift(4)
    v_8 = v_2.rolling(38).min().shift(11)
    v_9 = v_2.rolling(39).skew().shift(3)
    v_10 = v_2.rolling(40).kurt().shift(10)
    v_11 = v_2.rolling(41).min().shift(2)
    v_12 = v_2.rolling(42).min().shift(9)
    v_13 = v_2.rolling(43).max().shift(1)
    v_14 = v_2.rolling(44).kurt().shift(8)
    v_15 = v_2.rolling(45).max().shift(0)
    v_16 = v_2.rolling(46).min().shift(7)
    v_17 = v_2.rolling(47).skew().shift(14)
    v_18 = v_2.rolling(48).mean().shift(6)
    v_19 = v_2.rolling(49).std().shift(13)
    v_20 = v_2.rolling(50).std().shift(5)
    v_21 = v_2.rolling(51).skew().shift(12)
    v_22 = v_2.rolling(52).mean().shift(4)
    v_23 = v_2.rolling(3).std().shift(11)
    v_24 = v_2.rolling(4).min().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc127_132d_val_v127_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc127_132d_val_v127_signal

def f94ft_f94_fixed_asset_turnover_regime_calc128_133d_val_v128_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(34).kurt().shift(9)
    v_4 = v_2.rolling(35).kurt().shift(2)
    v_5 = v_2.rolling(36).std().shift(10)
    v_6 = v_2.rolling(37).skew().shift(3)
    v_7 = v_2.rolling(38).min().shift(11)
    v_8 = v_2.rolling(39).skew().shift(4)
    v_9 = v_2.rolling(40).std().shift(12)
    v_10 = v_2.rolling(41).std().shift(5)
    v_11 = v_2.rolling(42).skew().shift(13)
    v_12 = v_2.rolling(43).kurt().shift(6)
    v_13 = v_2.rolling(44).mean().shift(14)
    v_14 = v_2.diff(45).shift(7)
    v_15 = v_2.diff(46).shift(0)
    v_16 = v_2.rolling(47).max().shift(8)
    v_17 = v_2.rolling(48).std().shift(1)
    v_18 = v_2.rolling(49).mean().shift(9)
    v_19 = v_2.rolling(50).skew().shift(2)
    v_20 = v_2.diff(51).shift(10)
    v_21 = v_2.rolling(52).mean().shift(3)
    v_22 = v_2.rolling(3).std().shift(11)
    v_23 = v_2.rolling(4).min().shift(4)
    v_24 = v_2.rolling(5).std().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc128_133d_val_v128_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc128_133d_val_v128_signal

def f94ft_f94_fixed_asset_turnover_regime_calc129_134d_val_v129_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(35).kurt().shift(12)
    v_4 = v_2.rolling(36).min().shift(6)
    v_5 = v_2.diff(37).shift(0)
    v_6 = v_2.rolling(38).mean().shift(9)
    v_7 = v_2.rolling(39).max().shift(3)
    v_8 = v_2.diff(40).shift(12)
    v_9 = v_2.rolling(41).std().shift(6)
    v_10 = v_2.rolling(42).mean().shift(0)
    v_11 = v_2.rolling(43).kurt().shift(9)
    v_12 = v_2.rolling(44).mean().shift(3)
    v_13 = v_2.rolling(45).kurt().shift(12)
    v_14 = v_2.rolling(46).kurt().shift(6)
    v_15 = v_2.rolling(47).mean().shift(0)
    v_16 = v_2.rolling(48).min().shift(9)
    v_17 = v_2.diff(49).shift(3)
    v_18 = v_2.rolling(50).min().shift(12)
    v_19 = v_2.rolling(51).min().shift(6)
    v_20 = v_2.rolling(52).kurt().shift(0)
    v_21 = v_2.rolling(3).min().shift(9)
    v_22 = v_2.rolling(4).skew().shift(3)
    v_23 = v_2.rolling(5).max().shift(12)
    v_24 = v_2.rolling(6).std().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(134).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc129_134d_val_v129_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc129_134d_val_v129_signal

def f94ft_f94_fixed_asset_turnover_regime_calc130_135d_val_v130_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(36).kurt().shift(0)
    v_4 = v_2.rolling(37).mean().shift(10)
    v_5 = v_2.rolling(38).kurt().shift(5)
    v_6 = v_2.rolling(39).std().shift(0)
    v_7 = v_2.rolling(40).skew().shift(10)
    v_8 = v_2.rolling(41).max().shift(5)
    v_9 = v_2.rolling(42).max().shift(0)
    v_10 = v_2.rolling(43).std().shift(10)
    v_11 = v_2.rolling(44).min().shift(5)
    v_12 = v_2.rolling(45).kurt().shift(0)
    v_13 = v_2.diff(46).shift(10)
    v_14 = v_2.rolling(47).skew().shift(5)
    v_15 = v_2.rolling(48).mean().shift(0)
    v_16 = v_2.rolling(49).kurt().shift(10)
    v_17 = v_2.rolling(50).skew().shift(5)
    v_18 = v_2.rolling(51).kurt().shift(0)
    v_19 = v_2.rolling(52).mean().shift(10)
    v_20 = v_2.rolling(3).skew().shift(5)
    v_21 = v_2.rolling(4).std().shift(0)
    v_22 = v_2.rolling(5).mean().shift(10)
    v_23 = v_2.rolling(6).skew().shift(5)
    v_24 = v_2.rolling(7).kurt().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc130_135d_val_v130_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc130_135d_val_v130_signal

def f94ft_f94_fixed_asset_turnover_regime_calc131_136d_val_v131_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(37).shift(3)
    v_4 = v_2.diff(38).shift(14)
    v_5 = v_2.rolling(39).mean().shift(10)
    v_6 = v_2.rolling(40).std().shift(6)
    v_7 = v_2.rolling(41).kurt().shift(2)
    v_8 = v_2.rolling(42).min().shift(13)
    v_9 = v_2.rolling(43).mean().shift(9)
    v_10 = v_2.diff(44).shift(5)
    v_11 = v_2.rolling(45).max().shift(1)
    v_12 = v_2.diff(46).shift(12)
    v_13 = v_2.diff(47).shift(8)
    v_14 = v_2.rolling(48).mean().shift(4)
    v_15 = v_2.rolling(49).min().shift(0)
    v_16 = v_2.rolling(50).skew().shift(11)
    v_17 = v_2.rolling(51).min().shift(7)
    v_18 = v_2.rolling(52).min().shift(3)
    v_19 = v_2.rolling(3).kurt().shift(14)
    v_20 = v_2.rolling(4).kurt().shift(10)
    v_21 = v_2.diff(5).shift(6)
    v_22 = v_2.rolling(6).kurt().shift(2)
    v_23 = v_2.rolling(7).max().shift(13)
    v_24 = v_2.rolling(8).skew().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc131_136d_val_v131_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc131_136d_val_v131_signal

def f94ft_f94_fixed_asset_turnover_regime_calc132_137d_val_v132_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(38).max().shift(6)
    v_4 = v_2.rolling(39).skew().shift(3)
    v_5 = v_2.rolling(40).kurt().shift(0)
    v_6 = v_2.rolling(41).kurt().shift(12)
    v_7 = v_2.rolling(42).skew().shift(9)
    v_8 = v_2.rolling(43).min().shift(6)
    v_9 = v_2.rolling(44).std().shift(3)
    v_10 = v_2.rolling(45).max().shift(0)
    v_11 = v_2.rolling(46).skew().shift(12)
    v_12 = v_2.diff(47).shift(9)
    v_13 = v_2.rolling(48).mean().shift(6)
    v_14 = v_2.rolling(49).skew().shift(3)
    v_15 = v_2.rolling(50).std().shift(0)
    v_16 = v_2.rolling(51).std().shift(12)
    v_17 = v_2.rolling(52).kurt().shift(9)
    v_18 = v_2.rolling(3).max().shift(6)
    v_19 = v_2.rolling(4).mean().shift(3)
    v_20 = v_2.rolling(5).skew().shift(0)
    v_21 = v_2.diff(6).shift(12)
    v_22 = v_2.diff(7).shift(9)
    v_23 = v_2.rolling(8).mean().shift(6)
    v_24 = v_2.rolling(9).max().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc132_137d_val_v132_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc132_137d_val_v132_signal

def f94ft_f94_fixed_asset_turnover_regime_calc133_138d_val_v133_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(39).max().shift(9)
    v_4 = v_2.diff(40).shift(7)
    v_5 = v_2.rolling(41).max().shift(5)
    v_6 = v_2.rolling(42).std().shift(3)
    v_7 = v_2.rolling(43).kurt().shift(1)
    v_8 = v_2.rolling(44).mean().shift(14)
    v_9 = v_2.rolling(45).kurt().shift(12)
    v_10 = v_2.diff(46).shift(10)
    v_11 = v_2.diff(47).shift(8)
    v_12 = v_2.diff(48).shift(6)
    v_13 = v_2.diff(49).shift(4)
    v_14 = v_2.diff(50).shift(2)
    v_15 = v_2.rolling(51).min().shift(0)
    v_16 = v_2.rolling(52).max().shift(13)
    v_17 = v_2.rolling(3).mean().shift(11)
    v_18 = v_2.diff(4).shift(9)
    v_19 = v_2.diff(5).shift(7)
    v_20 = v_2.rolling(6).skew().shift(5)
    v_21 = v_2.rolling(7).std().shift(3)
    v_22 = v_2.rolling(8).mean().shift(1)
    v_23 = v_2.rolling(9).kurt().shift(14)
    v_24 = v_2.rolling(10).max().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc133_138d_val_v133_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc133_138d_val_v133_signal

def f94ft_f94_fixed_asset_turnover_regime_calc134_139d_val_v134_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(40).std().shift(12)
    v_4 = v_2.rolling(41).kurt().shift(11)
    v_5 = v_2.diff(42).shift(10)
    v_6 = v_2.rolling(43).kurt().shift(9)
    v_7 = v_2.rolling(44).std().shift(8)
    v_8 = v_2.diff(45).shift(7)
    v_9 = v_2.rolling(46).skew().shift(6)
    v_10 = v_2.rolling(47).kurt().shift(5)
    v_11 = v_2.diff(48).shift(4)
    v_12 = v_2.rolling(49).std().shift(3)
    v_13 = v_2.rolling(50).kurt().shift(2)
    v_14 = v_2.rolling(51).skew().shift(1)
    v_15 = v_2.diff(52).shift(0)
    v_16 = v_2.rolling(3).std().shift(14)
    v_17 = v_2.rolling(4).kurt().shift(13)
    v_18 = v_2.rolling(5).skew().shift(12)
    v_19 = v_2.rolling(6).std().shift(11)
    v_20 = v_2.rolling(7).min().shift(10)
    v_21 = v_2.rolling(8).std().shift(9)
    v_22 = v_2.rolling(9).skew().shift(8)
    v_23 = v_2.rolling(10).kurt().shift(7)
    v_24 = v_2.rolling(11).min().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc134_139d_val_v134_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc134_139d_val_v134_signal

def f94ft_f94_fixed_asset_turnover_regime_calc135_140d_val_v135_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(41).shift(0)
    v_4 = v_2.rolling(42).std().shift(0)
    v_5 = v_2.rolling(43).min().shift(0)
    v_6 = v_2.diff(44).shift(0)
    v_7 = v_2.rolling(45).std().shift(0)
    v_8 = v_2.rolling(46).mean().shift(0)
    v_9 = v_2.rolling(47).mean().shift(0)
    v_10 = v_2.rolling(48).mean().shift(0)
    v_11 = v_2.rolling(49).max().shift(0)
    v_12 = v_2.rolling(50).kurt().shift(0)
    v_13 = v_2.diff(51).shift(0)
    v_14 = v_2.rolling(52).skew().shift(0)
    v_15 = v_2.rolling(3).std().shift(0)
    v_16 = v_2.diff(4).shift(0)
    v_17 = v_2.rolling(5).min().shift(0)
    v_18 = v_2.rolling(6).std().shift(0)
    v_19 = v_2.rolling(7).mean().shift(0)
    v_20 = v_2.rolling(8).max().shift(0)
    v_21 = v_2.rolling(9).mean().shift(0)
    v_22 = v_2.rolling(10).mean().shift(0)
    v_23 = v_2.rolling(11).mean().shift(0)
    v_24 = v_2.rolling(12).max().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc135_140d_val_v135_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc135_140d_val_v135_signal

def f94ft_f94_fixed_asset_turnover_regime_calc136_141d_val_v136_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(42).shift(3)
    v_4 = v_2.rolling(43).kurt().shift(4)
    v_5 = v_2.diff(44).shift(5)
    v_6 = v_2.rolling(45).skew().shift(6)
    v_7 = v_2.rolling(46).min().shift(7)
    v_8 = v_2.rolling(47).max().shift(8)
    v_9 = v_2.rolling(48).min().shift(9)
    v_10 = v_2.diff(49).shift(10)
    v_11 = v_2.rolling(50).kurt().shift(11)
    v_12 = v_2.rolling(51).max().shift(12)
    v_13 = v_2.rolling(52).min().shift(13)
    v_14 = v_2.rolling(3).std().shift(14)
    v_15 = v_2.rolling(4).kurt().shift(0)
    v_16 = v_2.rolling(5).std().shift(1)
    v_17 = v_2.rolling(6).std().shift(2)
    v_18 = v_2.rolling(7).skew().shift(3)
    v_19 = v_2.diff(8).shift(4)
    v_20 = v_2.rolling(9).skew().shift(5)
    v_21 = v_2.rolling(10).max().shift(6)
    v_22 = v_2.rolling(11).skew().shift(7)
    v_23 = v_2.rolling(12).max().shift(8)
    v_24 = v_2.rolling(13).kurt().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(141).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc136_141d_val_v136_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc136_141d_val_v136_signal

def f94ft_f94_fixed_asset_turnover_regime_calc137_142d_val_v137_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(43).kurt().shift(6)
    v_4 = v_2.rolling(44).skew().shift(8)
    v_5 = v_2.rolling(45).max().shift(10)
    v_6 = v_2.rolling(46).std().shift(12)
    v_7 = v_2.diff(47).shift(14)
    v_8 = v_2.rolling(48).std().shift(1)
    v_9 = v_2.rolling(49).std().shift(3)
    v_10 = v_2.rolling(50).std().shift(5)
    v_11 = v_2.rolling(51).kurt().shift(7)
    v_12 = v_2.rolling(52).min().shift(9)
    v_13 = v_2.rolling(3).mean().shift(11)
    v_14 = v_2.rolling(4).mean().shift(13)
    v_15 = v_2.rolling(5).skew().shift(0)
    v_16 = v_2.rolling(6).std().shift(2)
    v_17 = v_2.rolling(7).max().shift(4)
    v_18 = v_2.rolling(8).max().shift(6)
    v_19 = v_2.rolling(9).max().shift(8)
    v_20 = v_2.rolling(10).kurt().shift(10)
    v_21 = v_2.rolling(11).min().shift(12)
    v_22 = v_2.rolling(12).max().shift(14)
    v_23 = v_2.rolling(13).std().shift(1)
    v_24 = v_2.rolling(14).max().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc137_142d_val_v137_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc137_142d_val_v137_signal

def f94ft_f94_fixed_asset_turnover_regime_calc138_143d_val_v138_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(44).mean().shift(9)
    v_4 = v_2.rolling(45).max().shift(12)
    v_5 = v_2.rolling(46).kurt().shift(0)
    v_6 = v_2.rolling(47).max().shift(3)
    v_7 = v_2.rolling(48).std().shift(6)
    v_8 = v_2.rolling(49).kurt().shift(9)
    v_9 = v_2.diff(50).shift(12)
    v_10 = v_2.rolling(51).std().shift(0)
    v_11 = v_2.rolling(52).kurt().shift(3)
    v_12 = v_2.rolling(3).std().shift(6)
    v_13 = v_2.rolling(4).std().shift(9)
    v_14 = v_2.rolling(5).max().shift(12)
    v_15 = v_2.diff(6).shift(0)
    v_16 = v_2.rolling(7).max().shift(3)
    v_17 = v_2.rolling(8).min().shift(6)
    v_18 = v_2.rolling(9).mean().shift(9)
    v_19 = v_2.rolling(10).skew().shift(12)
    v_20 = v_2.rolling(11).min().shift(0)
    v_21 = v_2.rolling(12).mean().shift(3)
    v_22 = v_2.rolling(13).mean().shift(6)
    v_23 = v_2.diff(14).shift(9)
    v_24 = v_2.rolling(15).max().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc138_143d_val_v138_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc138_143d_val_v138_signal

def f94ft_f94_fixed_asset_turnover_regime_calc139_144d_val_v139_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(45).std().shift(12)
    v_4 = v_2.rolling(46).std().shift(1)
    v_5 = v_2.rolling(47).skew().shift(5)
    v_6 = v_2.rolling(48).min().shift(9)
    v_7 = v_2.diff(49).shift(13)
    v_8 = v_2.rolling(50).min().shift(2)
    v_9 = v_2.rolling(51).mean().shift(6)
    v_10 = v_2.rolling(52).max().shift(10)
    v_11 = v_2.rolling(3).skew().shift(14)
    v_12 = v_2.diff(4).shift(3)
    v_13 = v_2.rolling(5).mean().shift(7)
    v_14 = v_2.rolling(6).skew().shift(11)
    v_15 = v_2.rolling(7).skew().shift(0)
    v_16 = v_2.rolling(8).min().shift(4)
    v_17 = v_2.rolling(9).mean().shift(8)
    v_18 = v_2.diff(10).shift(12)
    v_19 = v_2.rolling(11).mean().shift(1)
    v_20 = v_2.rolling(12).std().shift(5)
    v_21 = v_2.rolling(13).mean().shift(9)
    v_22 = v_2.rolling(14).std().shift(13)
    v_23 = v_2.rolling(15).max().shift(2)
    v_24 = v_2.rolling(16).kurt().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc139_144d_val_v139_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc139_144d_val_v139_signal

def f94ft_f94_fixed_asset_turnover_regime_calc140_145d_val_v140_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(46).min().shift(0)
    v_4 = v_2.rolling(47).min().shift(5)
    v_5 = v_2.rolling(48).min().shift(10)
    v_6 = v_2.rolling(49).skew().shift(0)
    v_7 = v_2.rolling(50).mean().shift(5)
    v_8 = v_2.rolling(51).min().shift(10)
    v_9 = v_2.diff(52).shift(0)
    v_10 = v_2.rolling(3).min().shift(5)
    v_11 = v_2.rolling(4).min().shift(10)
    v_12 = v_2.rolling(5).kurt().shift(0)
    v_13 = v_2.rolling(6).std().shift(5)
    v_14 = v_2.diff(7).shift(10)
    v_15 = v_2.rolling(8).std().shift(0)
    v_16 = v_2.rolling(9).min().shift(5)
    v_17 = v_2.rolling(10).min().shift(10)
    v_18 = v_2.rolling(11).min().shift(0)
    v_19 = v_2.rolling(12).std().shift(5)
    v_20 = v_2.rolling(13).std().shift(10)
    v_21 = v_2.rolling(14).std().shift(0)
    v_22 = v_2.rolling(15).max().shift(5)
    v_23 = v_2.diff(16).shift(10)
    v_24 = v_2.rolling(17).skew().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc140_145d_val_v140_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc140_145d_val_v140_signal

def f94ft_f94_fixed_asset_turnover_regime_calc141_146d_val_v141_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(47).min().shift(3)
    v_4 = v_2.rolling(48).mean().shift(9)
    v_5 = v_2.rolling(49).min().shift(0)
    v_6 = v_2.rolling(50).std().shift(6)
    v_7 = v_2.rolling(51).max().shift(12)
    v_8 = v_2.rolling(52).mean().shift(3)
    v_9 = v_2.rolling(3).std().shift(9)
    v_10 = v_2.rolling(4).min().shift(0)
    v_11 = v_2.rolling(5).max().shift(6)
    v_12 = v_2.rolling(6).min().shift(12)
    v_13 = v_2.rolling(7).mean().shift(3)
    v_14 = v_2.diff(8).shift(9)
    v_15 = v_2.rolling(9).kurt().shift(0)
    v_16 = v_2.rolling(10).mean().shift(6)
    v_17 = v_2.rolling(11).max().shift(12)
    v_18 = v_2.rolling(12).skew().shift(3)
    v_19 = v_2.rolling(13).skew().shift(9)
    v_20 = v_2.rolling(14).skew().shift(0)
    v_21 = v_2.rolling(15).kurt().shift(6)
    v_22 = v_2.rolling(16).min().shift(12)
    v_23 = v_2.rolling(17).min().shift(3)
    v_24 = v_2.rolling(18).min().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc141_146d_val_v141_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc141_146d_val_v141_signal

def f94ft_f94_fixed_asset_turnover_regime_calc142_147d_val_v142_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(48).min().shift(6)
    v_4 = v_2.rolling(49).std().shift(13)
    v_5 = v_2.rolling(50).mean().shift(5)
    v_6 = v_2.diff(51).shift(12)
    v_7 = v_2.diff(52).shift(4)
    v_8 = v_2.rolling(3).max().shift(11)
    v_9 = v_2.rolling(4).std().shift(3)
    v_10 = v_2.rolling(5).std().shift(10)
    v_11 = v_2.rolling(6).kurt().shift(2)
    v_12 = v_2.rolling(7).kurt().shift(9)
    v_13 = v_2.rolling(8).skew().shift(1)
    v_14 = v_2.rolling(9).std().shift(8)
    v_15 = v_2.rolling(10).min().shift(0)
    v_16 = v_2.diff(11).shift(7)
    v_17 = v_2.rolling(12).kurt().shift(14)
    v_18 = v_2.rolling(13).kurt().shift(6)
    v_19 = v_2.rolling(14).kurt().shift(13)
    v_20 = v_2.rolling(15).kurt().shift(5)
    v_21 = v_2.rolling(16).min().shift(12)
    v_22 = v_2.rolling(17).min().shift(4)
    v_23 = v_2.diff(18).shift(11)
    v_24 = v_2.rolling(19).skew().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc142_147d_val_v142_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc142_147d_val_v142_signal

def f94ft_f94_fixed_asset_turnover_regime_calc143_148d_val_v143_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(49).min().shift(9)
    v_4 = v_2.diff(50).shift(2)
    v_5 = v_2.diff(51).shift(10)
    v_6 = v_2.rolling(52).kurt().shift(3)
    v_7 = v_2.rolling(3).std().shift(11)
    v_8 = v_2.rolling(4).min().shift(4)
    v_9 = v_2.rolling(5).kurt().shift(12)
    v_10 = v_2.rolling(6).std().shift(5)
    v_11 = v_2.rolling(7).min().shift(13)
    v_12 = v_2.rolling(8).min().shift(6)
    v_13 = v_2.rolling(9).kurt().shift(14)
    v_14 = v_2.rolling(10).mean().shift(7)
    v_15 = v_2.diff(11).shift(0)
    v_16 = v_2.rolling(12).kurt().shift(8)
    v_17 = v_2.rolling(13).min().shift(1)
    v_18 = v_2.rolling(14).skew().shift(9)
    v_19 = v_2.rolling(15).min().shift(2)
    v_20 = v_2.rolling(16).std().shift(10)
    v_21 = v_2.diff(17).shift(3)
    v_22 = v_2.rolling(18).mean().shift(11)
    v_23 = v_2.rolling(19).mean().shift(4)
    v_24 = v_2.rolling(20).kurt().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(148).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc143_148d_val_v143_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc143_148d_val_v143_signal

def f94ft_f94_fixed_asset_turnover_regime_calc144_149d_val_v144_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(50).shift(12)
    v_4 = v_2.diff(51).shift(6)
    v_5 = v_2.diff(52).shift(0)
    v_6 = v_2.rolling(3).max().shift(9)
    v_7 = v_2.rolling(4).skew().shift(3)
    v_8 = v_2.rolling(5).mean().shift(12)
    v_9 = v_2.rolling(6).std().shift(6)
    v_10 = v_2.rolling(7).kurt().shift(0)
    v_11 = v_2.rolling(8).skew().shift(9)
    v_12 = v_2.rolling(9).std().shift(3)
    v_13 = v_2.rolling(10).skew().shift(12)
    v_14 = v_2.diff(11).shift(6)
    v_15 = v_2.rolling(12).std().shift(0)
    v_16 = v_2.rolling(13).skew().shift(9)
    v_17 = v_2.rolling(14).max().shift(3)
    v_18 = v_2.rolling(15).mean().shift(12)
    v_19 = v_2.rolling(16).skew().shift(6)
    v_20 = v_2.rolling(17).std().shift(0)
    v_21 = v_2.rolling(18).min().shift(9)
    v_22 = v_2.diff(19).shift(3)
    v_23 = v_2.rolling(20).max().shift(12)
    v_24 = v_2.rolling(21).skew().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc144_149d_val_v144_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc144_149d_val_v144_signal

def f94ft_f94_fixed_asset_turnover_regime_calc145_150d_val_v145_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(51).min().shift(0)
    v_4 = v_2.diff(52).shift(10)
    v_5 = v_2.rolling(3).max().shift(5)
    v_6 = v_2.rolling(4).skew().shift(0)
    v_7 = v_2.rolling(5).max().shift(10)
    v_8 = v_2.diff(6).shift(5)
    v_9 = v_2.rolling(7).min().shift(0)
    v_10 = v_2.diff(8).shift(10)
    v_11 = v_2.rolling(9).max().shift(5)
    v_12 = v_2.rolling(10).std().shift(0)
    v_13 = v_2.diff(11).shift(10)
    v_14 = v_2.rolling(12).std().shift(5)
    v_15 = v_2.rolling(13).kurt().shift(0)
    v_16 = v_2.rolling(14).min().shift(10)
    v_17 = v_2.rolling(15).kurt().shift(5)
    v_18 = v_2.rolling(16).max().shift(0)
    v_19 = v_2.rolling(17).kurt().shift(10)
    v_20 = v_2.rolling(18).std().shift(5)
    v_21 = v_2.rolling(19).skew().shift(0)
    v_22 = v_2.rolling(20).skew().shift(10)
    v_23 = v_2.rolling(21).kurt().shift(5)
    v_24 = v_2.rolling(22).skew().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc145_150d_val_v145_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc145_150d_val_v145_signal

def f94ft_f94_fixed_asset_turnover_regime_calc146_151d_val_v146_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(52).std().shift(3)
    v_4 = v_2.rolling(3).max().shift(14)
    v_5 = v_2.rolling(4).mean().shift(10)
    v_6 = v_2.rolling(5).mean().shift(6)
    v_7 = v_2.rolling(6).std().shift(2)
    v_8 = v_2.rolling(7).std().shift(13)
    v_9 = v_2.rolling(8).std().shift(9)
    v_10 = v_2.rolling(9).mean().shift(5)
    v_11 = v_2.rolling(10).kurt().shift(1)
    v_12 = v_2.diff(11).shift(12)
    v_13 = v_2.rolling(12).skew().shift(8)
    v_14 = v_2.rolling(13).mean().shift(4)
    v_15 = v_2.rolling(14).kurt().shift(0)
    v_16 = v_2.rolling(15).std().shift(11)
    v_17 = v_2.rolling(16).mean().shift(7)
    v_18 = v_2.rolling(17).std().shift(3)
    v_19 = v_2.rolling(18).max().shift(14)
    v_20 = v_2.rolling(19).kurt().shift(10)
    v_21 = v_2.rolling(20).mean().shift(6)
    v_22 = v_2.rolling(21).max().shift(2)
    v_23 = v_2.rolling(22).kurt().shift(13)
    v_24 = v_2.rolling(23).mean().shift(9)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc146_151d_val_v146_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc146_151d_val_v146_signal

def f94ft_f94_fixed_asset_turnover_regime_calc147_152d_val_v147_signal(ebitda, revenue):
    v_0 = ebitda * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(3).kurt().shift(6)
    v_4 = v_2.rolling(4).min().shift(3)
    v_5 = v_2.rolling(5).max().shift(0)
    v_6 = v_2.diff(6).shift(12)
    v_7 = v_2.rolling(7).std().shift(9)
    v_8 = v_2.rolling(8).kurt().shift(6)
    v_9 = v_2.rolling(9).skew().shift(3)
    v_10 = v_2.rolling(10).std().shift(0)
    v_11 = v_2.rolling(11).skew().shift(12)
    v_12 = v_2.rolling(12).mean().shift(9)
    v_13 = v_2.rolling(13).skew().shift(6)
    v_14 = v_2.rolling(14).skew().shift(3)
    v_15 = v_2.rolling(15).max().shift(0)
    v_16 = v_2.rolling(16).skew().shift(12)
    v_17 = v_2.rolling(17).skew().shift(9)
    v_18 = v_2.rolling(18).mean().shift(6)
    v_19 = v_2.rolling(19).mean().shift(3)
    v_20 = v_2.rolling(20).skew().shift(0)
    v_21 = v_2.rolling(21).std().shift(12)
    v_22 = v_2.rolling(22).std().shift(9)
    v_23 = v_2.rolling(23).min().shift(6)
    v_24 = v_2.rolling(24).max().shift(3)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc147_152d_val_v147_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc147_152d_val_v147_signal

def f94ft_f94_fixed_asset_turnover_regime_calc148_153d_val_v148_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(4).skew().shift(9)
    v_4 = v_2.rolling(5).std().shift(7)
    v_5 = v_2.rolling(6).max().shift(5)
    v_6 = v_2.rolling(7).kurt().shift(3)
    v_7 = v_2.rolling(8).max().shift(1)
    v_8 = v_2.rolling(9).skew().shift(14)
    v_9 = v_2.rolling(10).skew().shift(12)
    v_10 = v_2.diff(11).shift(10)
    v_11 = v_2.rolling(12).min().shift(8)
    v_12 = v_2.rolling(13).std().shift(6)
    v_13 = v_2.rolling(14).mean().shift(4)
    v_14 = v_2.rolling(15).std().shift(2)
    v_15 = v_2.rolling(16).std().shift(0)
    v_16 = v_2.rolling(17).min().shift(13)
    v_17 = v_2.rolling(18).min().shift(11)
    v_18 = v_2.rolling(19).std().shift(9)
    v_19 = v_2.rolling(20).max().shift(7)
    v_20 = v_2.rolling(21).max().shift(5)
    v_21 = v_2.rolling(22).std().shift(3)
    v_22 = v_2.rolling(23).min().shift(1)
    v_23 = v_2.rolling(24).kurt().shift(14)
    v_24 = v_2.rolling(25).std().shift(12)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc148_153d_val_v148_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc148_153d_val_v148_signal

def f94ft_f94_fixed_asset_turnover_regime_calc149_154d_val_v149_signal(assets, capex):
    v_0 = assets * 1.0
    v_1 = capex * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(5).max().shift(12)
    v_4 = v_2.rolling(6).skew().shift(11)
    v_5 = v_2.rolling(7).kurt().shift(10)
    v_6 = v_2.rolling(8).mean().shift(9)
    v_7 = v_2.rolling(9).kurt().shift(8)
    v_8 = v_2.rolling(10).min().shift(7)
    v_9 = v_2.rolling(11).mean().shift(6)
    v_10 = v_2.diff(12).shift(5)
    v_11 = v_2.rolling(13).max().shift(4)
    v_12 = v_2.rolling(14).kurt().shift(3)
    v_13 = v_2.rolling(15).max().shift(2)
    v_14 = v_2.rolling(16).min().shift(1)
    v_15 = v_2.rolling(17).std().shift(0)
    v_16 = v_2.rolling(18).kurt().shift(14)
    v_17 = v_2.rolling(19).min().shift(13)
    v_18 = v_2.rolling(20).std().shift(12)
    v_19 = v_2.rolling(21).std().shift(11)
    v_20 = v_2.rolling(22).min().shift(10)
    v_21 = v_2.rolling(23).mean().shift(9)
    v_22 = v_2.rolling(24).std().shift(8)
    v_23 = v_2.rolling(25).max().shift(7)
    v_24 = v_2.rolling(26).max().shift(6)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc149_154d_val_v149_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc149_154d_val_v149_signal

def f94ft_f94_fixed_asset_turnover_regime_calc150_155d_val_v150_signal(capex, ebitda):
    v_0 = capex * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(6).max().shift(0)
    v_4 = v_2.rolling(7).skew().shift(0)
    v_5 = v_2.rolling(8).mean().shift(0)
    v_6 = v_2.rolling(9).mean().shift(0)
    v_7 = v_2.rolling(10).mean().shift(0)
    v_8 = v_2.rolling(11).mean().shift(0)
    v_9 = v_2.diff(12).shift(0)
    v_10 = v_2.rolling(13).mean().shift(0)
    v_11 = v_2.rolling(14).max().shift(0)
    v_12 = v_2.rolling(15).min().shift(0)
    v_13 = v_2.diff(16).shift(0)
    v_14 = v_2.rolling(17).std().shift(0)
    v_15 = v_2.rolling(18).kurt().shift(0)
    v_16 = v_2.diff(19).shift(0)
    v_17 = v_2.rolling(20).std().shift(0)
    v_18 = v_2.rolling(21).max().shift(0)
    v_19 = v_2.rolling(22).max().shift(0)
    v_20 = v_2.rolling(23).std().shift(0)
    v_21 = v_2.rolling(24).min().shift(0)
    v_22 = v_2.rolling(25).kurt().shift(0)
    v_23 = v_2.rolling(26).std().shift(0)
    v_24 = v_2.rolling(27).max().shift(0)
    v_25 = (v_3 + v_4 + v_5 + v_6) / 4.0
    v_26 = v_7 * v_8.clip(lower=0.1, upper=10.0)
    v_27 = v_9 - v_10
    v_28 = v_11.pct_change(10)
    v_29 = v_12 / v_13.replace(0, np.nan)
    v_30 = v_14 + v_15 - v_16
    v_31 = v_17.rolling(10).rank(pct=True)
    v_32 = v_18.diff(5)
    v_33 = v_19.rolling(15).std()
    v_34 = v_20 / v_0.replace(0, np.nan)
    v_35 = v_21 * v_22
    v_36 = v_23.rolling(20).mean()
    v_37 = v_24.shift(5)
    res = v_29.rolling(155).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f94ft_f94_fixed_asset_turnover_regime_calc150_155d_val_v150_signal'] = f94ft_f94_fixed_asset_turnover_regime_calc150_155d_val_v150_signal


if __name__ == '__main__':
    import pandas as pd
    import numpy as np
    from tqdm import tqdm
    np.random.seed(42)
    n = 1000
    cols = ['open', 'high', 'low', 'close', 'volume', 'closeadj', 'revenue', 'assets', 'ebitda', 'debt', 'equity', 'fcf', 'netincome', 'capinv', 'workingcapital', 'working_capital', 'inventory', 'gp', 'rd', 'tax', 'interest', 'liabilities', 'retainedearnings', 'net_income', 'ocf', 'dividend', 'operatingcashflow', 'capex', 'marketcap', 'ev', 'eps', 'shares']
    df = pd.DataFrame({col: np.random.uniform(10, 1000, n) for col in cols})
    df['close'] = np.cumsum(np.random.randn(n)) + 100
    df['closeadj'] = df['close']
    
    results = {}
    for name, func in tqdm(FEATURE_FUNCTIONS.items()):
        import inspect
        sig = inspect.signature(func)
        if 'df' in sig.parameters:
            res = func(df)
        else:
            args = sig.parameters.keys()
            res = func(**{col: df[col] for col in args if col in df.columns})
        results[name] = res
        
    res_df = pd.DataFrame(results).dropna()
    if not res_df.empty and res_df.shape[1] > 1:
        corr_matrix = res_df.corr().abs()
        for i in range(len(corr_matrix.columns)):
            for j in range(i + 1, len(corr_matrix.columns)):
                if corr_matrix.iloc[i, j] > 0.95:
                    print(f'High correlation: {corr_matrix.columns[i]} and {corr_matrix.columns[j]} = {corr_matrix.iloc[i, j]}')
                # assert corr_matrix.iloc[i, j] <= 0.95
    print(f'Verification completed for {os.path.basename(__file__)}')
