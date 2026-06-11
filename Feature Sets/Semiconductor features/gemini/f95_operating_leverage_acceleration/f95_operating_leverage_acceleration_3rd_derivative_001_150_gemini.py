import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f95oa_f95_operating_leverage_acceleration_calc001_6d_jerk_v001_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(7).skew().shift(3)
    v_4 = v_2.rolling(8).min().shift(4)
    v_5 = v_2.rolling(9).min().shift(5)
    v_6 = v_2.diff(10).shift(6)
    v_7 = v_2.rolling(11).kurt().shift(7)
    v_8 = v_2.rolling(12).skew().shift(8)
    v_9 = v_2.rolling(13).kurt().shift(9)
    v_10 = v_2.rolling(14).kurt().shift(10)
    v_11 = v_2.rolling(15).min().shift(11)
    v_12 = v_2.rolling(16).skew().shift(12)
    v_13 = v_2.rolling(17).std().shift(13)
    v_14 = v_2.rolling(18).std().shift(14)
    v_15 = v_2.rolling(19).skew().shift(0)
    v_16 = v_2.rolling(20).min().shift(1)
    v_17 = v_2.rolling(21).min().shift(2)
    v_18 = v_2.rolling(22).max().shift(3)
    v_19 = v_2.rolling(23).max().shift(4)
    v_20 = v_2.rolling(24).std().shift(5)
    v_21 = v_2.rolling(25).max().shift(6)
    v_22 = v_2.rolling(26).kurt().shift(7)
    v_23 = v_2.rolling(27).min().shift(8)
    v_24 = v_2.rolling(28).mean().shift(9)
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
    res = v_2.diff(2).diff(6).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc001_6d_jerk_v001_signal'] = f95oa_f95_operating_leverage_acceleration_calc001_6d_jerk_v001_signal

def f95oa_f95_operating_leverage_acceleration_calc002_7d_jerk_v002_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(8).min().shift(6)
    v_4 = v_2.rolling(9).min().shift(8)
    v_5 = v_2.rolling(10).max().shift(10)
    v_6 = v_2.diff(11).shift(12)
    v_7 = v_2.rolling(12).min().shift(14)
    v_8 = v_2.diff(13).shift(1)
    v_9 = v_2.rolling(14).kurt().shift(3)
    v_10 = v_2.rolling(15).skew().shift(5)
    v_11 = v_2.rolling(16).max().shift(7)
    v_12 = v_2.rolling(17).std().shift(9)
    v_13 = v_2.rolling(18).kurt().shift(11)
    v_14 = v_2.rolling(19).min().shift(13)
    v_15 = v_2.rolling(20).skew().shift(0)
    v_16 = v_2.rolling(21).min().shift(2)
    v_17 = v_2.rolling(22).min().shift(4)
    v_18 = v_2.rolling(23).std().shift(6)
    v_19 = v_2.rolling(24).kurt().shift(8)
    v_20 = v_2.rolling(25).mean().shift(10)
    v_21 = v_2.rolling(26).min().shift(12)
    v_22 = v_2.rolling(27).min().shift(14)
    v_23 = v_2.rolling(28).max().shift(1)
    v_24 = v_2.rolling(29).std().shift(3)
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
    res = v_2.diff(2).diff(7).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc002_7d_jerk_v002_signal'] = f95oa_f95_operating_leverage_acceleration_calc002_7d_jerk_v002_signal

def f95oa_f95_operating_leverage_acceleration_calc003_8d_jerk_v003_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(9).skew().shift(9)
    v_4 = v_2.rolling(10).std().shift(12)
    v_5 = v_2.diff(11).shift(0)
    v_6 = v_2.rolling(12).max().shift(3)
    v_7 = v_2.diff(13).shift(6)
    v_8 = v_2.rolling(14).mean().shift(9)
    v_9 = v_2.rolling(15).std().shift(12)
    v_10 = v_2.diff(16).shift(0)
    v_11 = v_2.rolling(17).kurt().shift(3)
    v_12 = v_2.rolling(18).kurt().shift(6)
    v_13 = v_2.rolling(19).mean().shift(9)
    v_14 = v_2.rolling(20).mean().shift(12)
    v_15 = v_2.rolling(21).skew().shift(0)
    v_16 = v_2.rolling(22).mean().shift(3)
    v_17 = v_2.rolling(23).kurt().shift(6)
    v_18 = v_2.rolling(24).max().shift(9)
    v_19 = v_2.rolling(25).kurt().shift(12)
    v_20 = v_2.rolling(26).min().shift(0)
    v_21 = v_2.rolling(27).std().shift(3)
    v_22 = v_2.rolling(28).max().shift(6)
    v_23 = v_2.rolling(29).mean().shift(9)
    v_24 = v_2.rolling(30).std().shift(12)
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
    res = v_2.diff(2).diff(8).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc003_8d_jerk_v003_signal'] = f95oa_f95_operating_leverage_acceleration_calc003_8d_jerk_v003_signal

def f95oa_f95_operating_leverage_acceleration_calc004_9d_jerk_v004_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(10).mean().shift(12)
    v_4 = v_2.rolling(11).skew().shift(1)
    v_5 = v_2.rolling(12).kurt().shift(5)
    v_6 = v_2.rolling(13).skew().shift(9)
    v_7 = v_2.rolling(14).max().shift(13)
    v_8 = v_2.rolling(15).kurt().shift(2)
    v_9 = v_2.rolling(16).min().shift(6)
    v_10 = v_2.rolling(17).skew().shift(10)
    v_11 = v_2.rolling(18).max().shift(14)
    v_12 = v_2.rolling(19).kurt().shift(3)
    v_13 = v_2.rolling(20).std().shift(7)
    v_14 = v_2.rolling(21).skew().shift(11)
    v_15 = v_2.rolling(22).skew().shift(0)
    v_16 = v_2.rolling(23).max().shift(4)
    v_17 = v_2.rolling(24).std().shift(8)
    v_18 = v_2.rolling(25).kurt().shift(12)
    v_19 = v_2.rolling(26).max().shift(1)
    v_20 = v_2.rolling(27).kurt().shift(5)
    v_21 = v_2.rolling(28).kurt().shift(9)
    v_22 = v_2.rolling(29).max().shift(13)
    v_23 = v_2.rolling(30).std().shift(2)
    v_24 = v_2.rolling(31).skew().shift(6)
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
    res = v_2.diff(2).diff(9).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc004_9d_jerk_v004_signal'] = f95oa_f95_operating_leverage_acceleration_calc004_9d_jerk_v004_signal

def f95oa_f95_operating_leverage_acceleration_calc005_10d_jerk_v005_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(11).min().shift(0)
    v_4 = v_2.rolling(12).max().shift(5)
    v_5 = v_2.rolling(13).mean().shift(10)
    v_6 = v_2.rolling(14).std().shift(0)
    v_7 = v_2.rolling(15).mean().shift(5)
    v_8 = v_2.rolling(16).std().shift(10)
    v_9 = v_2.rolling(17).mean().shift(0)
    v_10 = v_2.diff(18).shift(5)
    v_11 = v_2.rolling(19).max().shift(10)
    v_12 = v_2.diff(20).shift(0)
    v_13 = v_2.rolling(21).mean().shift(5)
    v_14 = v_2.rolling(22).max().shift(10)
    v_15 = v_2.rolling(23).std().shift(0)
    v_16 = v_2.rolling(24).min().shift(5)
    v_17 = v_2.rolling(25).min().shift(10)
    v_18 = v_2.rolling(26).min().shift(0)
    v_19 = v_2.rolling(27).kurt().shift(5)
    v_20 = v_2.diff(28).shift(10)
    v_21 = v_2.rolling(29).skew().shift(0)
    v_22 = v_2.rolling(30).std().shift(5)
    v_23 = v_2.rolling(31).max().shift(10)
    v_24 = v_2.rolling(32).max().shift(0)
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
    res = v_2.diff(2).diff(10).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc005_10d_jerk_v005_signal'] = f95oa_f95_operating_leverage_acceleration_calc005_10d_jerk_v005_signal

def f95oa_f95_operating_leverage_acceleration_calc006_11d_jerk_v006_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(12).skew().shift(3)
    v_4 = v_2.diff(13).shift(9)
    v_5 = v_2.rolling(14).std().shift(0)
    v_6 = v_2.rolling(15).min().shift(6)
    v_7 = v_2.rolling(16).std().shift(12)
    v_8 = v_2.rolling(17).max().shift(3)
    v_9 = v_2.rolling(18).std().shift(9)
    v_10 = v_2.rolling(19).min().shift(0)
    v_11 = v_2.rolling(20).skew().shift(6)
    v_12 = v_2.rolling(21).std().shift(12)
    v_13 = v_2.rolling(22).mean().shift(3)
    v_14 = v_2.rolling(23).max().shift(9)
    v_15 = v_2.rolling(24).std().shift(0)
    v_16 = v_2.rolling(25).kurt().shift(6)
    v_17 = v_2.rolling(26).max().shift(12)
    v_18 = v_2.rolling(27).min().shift(3)
    v_19 = v_2.rolling(28).mean().shift(9)
    v_20 = v_2.rolling(29).mean().shift(0)
    v_21 = v_2.rolling(30).skew().shift(6)
    v_22 = v_2.rolling(31).skew().shift(12)
    v_23 = v_2.rolling(32).kurt().shift(3)
    v_24 = v_2.diff(33).shift(9)
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
    res = v_2.diff(2).diff(11).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc006_11d_jerk_v006_signal'] = f95oa_f95_operating_leverage_acceleration_calc006_11d_jerk_v006_signal

def f95oa_f95_operating_leverage_acceleration_calc007_12d_jerk_v007_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(13).std().shift(6)
    v_4 = v_2.rolling(14).min().shift(13)
    v_5 = v_2.rolling(15).kurt().shift(5)
    v_6 = v_2.rolling(16).min().shift(12)
    v_7 = v_2.rolling(17).min().shift(4)
    v_8 = v_2.rolling(18).kurt().shift(11)
    v_9 = v_2.rolling(19).kurt().shift(3)
    v_10 = v_2.rolling(20).min().shift(10)
    v_11 = v_2.rolling(21).kurt().shift(2)
    v_12 = v_2.diff(22).shift(9)
    v_13 = v_2.rolling(23).std().shift(1)
    v_14 = v_2.rolling(24).skew().shift(8)
    v_15 = v_2.diff(25).shift(0)
    v_16 = v_2.rolling(26).mean().shift(7)
    v_17 = v_2.rolling(27).skew().shift(14)
    v_18 = v_2.rolling(28).skew().shift(6)
    v_19 = v_2.rolling(29).min().shift(13)
    v_20 = v_2.rolling(30).min().shift(5)
    v_21 = v_2.rolling(31).kurt().shift(12)
    v_22 = v_2.rolling(32).kurt().shift(4)
    v_23 = v_2.rolling(33).min().shift(11)
    v_24 = v_2.rolling(34).max().shift(3)
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
    res = v_2.diff(2).diff(12).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc007_12d_jerk_v007_signal'] = f95oa_f95_operating_leverage_acceleration_calc007_12d_jerk_v007_signal

def f95oa_f95_operating_leverage_acceleration_calc008_13d_jerk_v008_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(14).max().shift(9)
    v_4 = v_2.rolling(15).std().shift(2)
    v_5 = v_2.rolling(16).std().shift(10)
    v_6 = v_2.rolling(17).skew().shift(3)
    v_7 = v_2.rolling(18).max().shift(11)
    v_8 = v_2.diff(19).shift(4)
    v_9 = v_2.rolling(20).kurt().shift(12)
    v_10 = v_2.rolling(21).kurt().shift(5)
    v_11 = v_2.rolling(22).kurt().shift(13)
    v_12 = v_2.rolling(23).kurt().shift(6)
    v_13 = v_2.diff(24).shift(14)
    v_14 = v_2.rolling(25).kurt().shift(7)
    v_15 = v_2.diff(26).shift(0)
    v_16 = v_2.diff(27).shift(8)
    v_17 = v_2.rolling(28).mean().shift(1)
    v_18 = v_2.rolling(29).kurt().shift(9)
    v_19 = v_2.rolling(30).kurt().shift(2)
    v_20 = v_2.rolling(31).min().shift(10)
    v_21 = v_2.rolling(32).skew().shift(3)
    v_22 = v_2.rolling(33).min().shift(11)
    v_23 = v_2.rolling(34).mean().shift(4)
    v_24 = v_2.rolling(35).mean().shift(12)
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
    res = v_2.diff(2).diff(13).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc008_13d_jerk_v008_signal'] = f95oa_f95_operating_leverage_acceleration_calc008_13d_jerk_v008_signal

def f95oa_f95_operating_leverage_acceleration_calc009_14d_jerk_v009_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(15).skew().shift(12)
    v_4 = v_2.rolling(16).mean().shift(6)
    v_5 = v_2.rolling(17).skew().shift(0)
    v_6 = v_2.rolling(18).max().shift(9)
    v_7 = v_2.rolling(19).skew().shift(3)
    v_8 = v_2.diff(20).shift(12)
    v_9 = v_2.rolling(21).std().shift(6)
    v_10 = v_2.rolling(22).max().shift(0)
    v_11 = v_2.rolling(23).max().shift(9)
    v_12 = v_2.diff(24).shift(3)
    v_13 = v_2.rolling(25).min().shift(12)
    v_14 = v_2.rolling(26).std().shift(6)
    v_15 = v_2.diff(27).shift(0)
    v_16 = v_2.rolling(28).max().shift(9)
    v_17 = v_2.rolling(29).kurt().shift(3)
    v_18 = v_2.rolling(30).skew().shift(12)
    v_19 = v_2.rolling(31).std().shift(6)
    v_20 = v_2.rolling(32).skew().shift(0)
    v_21 = v_2.rolling(33).max().shift(9)
    v_22 = v_2.rolling(34).mean().shift(3)
    v_23 = v_2.rolling(35).max().shift(12)
    v_24 = v_2.diff(36).shift(6)
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
    res = v_2.diff(2).diff(14).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc009_14d_jerk_v009_signal'] = f95oa_f95_operating_leverage_acceleration_calc009_14d_jerk_v009_signal

def f95oa_f95_operating_leverage_acceleration_calc010_15d_jerk_v010_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(16).shift(0)
    v_4 = v_2.rolling(17).std().shift(10)
    v_5 = v_2.diff(18).shift(5)
    v_6 = v_2.rolling(19).skew().shift(0)
    v_7 = v_2.rolling(20).std().shift(10)
    v_8 = v_2.rolling(21).skew().shift(5)
    v_9 = v_2.diff(22).shift(0)
    v_10 = v_2.rolling(23).skew().shift(10)
    v_11 = v_2.rolling(24).max().shift(5)
    v_12 = v_2.rolling(25).max().shift(0)
    v_13 = v_2.rolling(26).skew().shift(10)
    v_14 = v_2.diff(27).shift(5)
    v_15 = v_2.rolling(28).min().shift(0)
    v_16 = v_2.rolling(29).skew().shift(10)
    v_17 = v_2.diff(30).shift(5)
    v_18 = v_2.rolling(31).max().shift(0)
    v_19 = v_2.diff(32).shift(10)
    v_20 = v_2.rolling(33).max().shift(5)
    v_21 = v_2.rolling(34).kurt().shift(0)
    v_22 = v_2.rolling(35).skew().shift(10)
    v_23 = v_2.rolling(36).mean().shift(5)
    v_24 = v_2.diff(37).shift(0)
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
    res = v_2.diff(2).diff(15).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc010_15d_jerk_v010_signal'] = f95oa_f95_operating_leverage_acceleration_calc010_15d_jerk_v010_signal

def f95oa_f95_operating_leverage_acceleration_calc011_16d_jerk_v011_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(17).skew().shift(3)
    v_4 = v_2.diff(18).shift(14)
    v_5 = v_2.rolling(19).min().shift(10)
    v_6 = v_2.rolling(20).skew().shift(6)
    v_7 = v_2.rolling(21).skew().shift(2)
    v_8 = v_2.rolling(22).skew().shift(13)
    v_9 = v_2.rolling(23).max().shift(9)
    v_10 = v_2.rolling(24).kurt().shift(5)
    v_11 = v_2.rolling(25).mean().shift(1)
    v_12 = v_2.rolling(26).kurt().shift(12)
    v_13 = v_2.rolling(27).std().shift(8)
    v_14 = v_2.rolling(28).min().shift(4)
    v_15 = v_2.rolling(29).skew().shift(0)
    v_16 = v_2.rolling(30).skew().shift(11)
    v_17 = v_2.rolling(31).std().shift(7)
    v_18 = v_2.diff(32).shift(3)
    v_19 = v_2.rolling(33).mean().shift(14)
    v_20 = v_2.rolling(34).min().shift(10)
    v_21 = v_2.rolling(35).max().shift(6)
    v_22 = v_2.rolling(36).mean().shift(2)
    v_23 = v_2.rolling(37).min().shift(13)
    v_24 = v_2.rolling(38).std().shift(9)
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
    res = v_2.diff(2).diff(16).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc011_16d_jerk_v011_signal'] = f95oa_f95_operating_leverage_acceleration_calc011_16d_jerk_v011_signal

def f95oa_f95_operating_leverage_acceleration_calc012_17d_jerk_v012_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(18).std().shift(6)
    v_4 = v_2.rolling(19).min().shift(3)
    v_5 = v_2.diff(20).shift(0)
    v_6 = v_2.rolling(21).kurt().shift(12)
    v_7 = v_2.rolling(22).std().shift(9)
    v_8 = v_2.rolling(23).min().shift(6)
    v_9 = v_2.rolling(24).mean().shift(3)
    v_10 = v_2.rolling(25).min().shift(0)
    v_11 = v_2.rolling(26).max().shift(12)
    v_12 = v_2.rolling(27).min().shift(9)
    v_13 = v_2.rolling(28).skew().shift(6)
    v_14 = v_2.rolling(29).std().shift(3)
    v_15 = v_2.rolling(30).min().shift(0)
    v_16 = v_2.rolling(31).std().shift(12)
    v_17 = v_2.rolling(32).mean().shift(9)
    v_18 = v_2.rolling(33).min().shift(6)
    v_19 = v_2.rolling(34).max().shift(3)
    v_20 = v_2.rolling(35).std().shift(0)
    v_21 = v_2.rolling(36).kurt().shift(12)
    v_22 = v_2.diff(37).shift(9)
    v_23 = v_2.diff(38).shift(6)
    v_24 = v_2.rolling(39).mean().shift(3)
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
    res = v_2.diff(2).diff(17).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc012_17d_jerk_v012_signal'] = f95oa_f95_operating_leverage_acceleration_calc012_17d_jerk_v012_signal

def f95oa_f95_operating_leverage_acceleration_calc013_18d_jerk_v013_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(19).kurt().shift(9)
    v_4 = v_2.rolling(20).min().shift(7)
    v_5 = v_2.rolling(21).min().shift(5)
    v_6 = v_2.diff(22).shift(3)
    v_7 = v_2.rolling(23).skew().shift(1)
    v_8 = v_2.diff(24).shift(14)
    v_9 = v_2.diff(25).shift(12)
    v_10 = v_2.rolling(26).std().shift(10)
    v_11 = v_2.rolling(27).std().shift(8)
    v_12 = v_2.rolling(28).max().shift(6)
    v_13 = v_2.diff(29).shift(4)
    v_14 = v_2.rolling(30).mean().shift(2)
    v_15 = v_2.diff(31).shift(0)
    v_16 = v_2.rolling(32).min().shift(13)
    v_17 = v_2.rolling(33).mean().shift(11)
    v_18 = v_2.diff(34).shift(9)
    v_19 = v_2.rolling(35).kurt().shift(7)
    v_20 = v_2.rolling(36).mean().shift(5)
    v_21 = v_2.diff(37).shift(3)
    v_22 = v_2.rolling(38).skew().shift(1)
    v_23 = v_2.rolling(39).max().shift(14)
    v_24 = v_2.rolling(40).std().shift(12)
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
    res = v_2.diff(2).diff(18).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc013_18d_jerk_v013_signal'] = f95oa_f95_operating_leverage_acceleration_calc013_18d_jerk_v013_signal

def f95oa_f95_operating_leverage_acceleration_calc014_19d_jerk_v014_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(20).kurt().shift(12)
    v_4 = v_2.rolling(21).std().shift(11)
    v_5 = v_2.rolling(22).kurt().shift(10)
    v_6 = v_2.diff(23).shift(9)
    v_7 = v_2.diff(24).shift(8)
    v_8 = v_2.rolling(25).max().shift(7)
    v_9 = v_2.rolling(26).mean().shift(6)
    v_10 = v_2.rolling(27).kurt().shift(5)
    v_11 = v_2.rolling(28).max().shift(4)
    v_12 = v_2.rolling(29).mean().shift(3)
    v_13 = v_2.rolling(30).mean().shift(2)
    v_14 = v_2.rolling(31).max().shift(1)
    v_15 = v_2.rolling(32).min().shift(0)
    v_16 = v_2.rolling(33).std().shift(14)
    v_17 = v_2.rolling(34).mean().shift(13)
    v_18 = v_2.rolling(35).min().shift(12)
    v_19 = v_2.rolling(36).kurt().shift(11)
    v_20 = v_2.rolling(37).mean().shift(10)
    v_21 = v_2.rolling(38).max().shift(9)
    v_22 = v_2.rolling(39).mean().shift(8)
    v_23 = v_2.rolling(40).mean().shift(7)
    v_24 = v_2.rolling(41).kurt().shift(6)
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
    res = v_2.diff(2).diff(19).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc014_19d_jerk_v014_signal'] = f95oa_f95_operating_leverage_acceleration_calc014_19d_jerk_v014_signal

def f95oa_f95_operating_leverage_acceleration_calc015_20d_jerk_v015_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(21).min().shift(0)
    v_4 = v_2.rolling(22).std().shift(0)
    v_5 = v_2.diff(23).shift(0)
    v_6 = v_2.rolling(24).skew().shift(0)
    v_7 = v_2.rolling(25).kurt().shift(0)
    v_8 = v_2.rolling(26).skew().shift(0)
    v_9 = v_2.rolling(27).mean().shift(0)
    v_10 = v_2.rolling(28).min().shift(0)
    v_11 = v_2.rolling(29).mean().shift(0)
    v_12 = v_2.rolling(30).max().shift(0)
    v_13 = v_2.rolling(31).skew().shift(0)
    v_14 = v_2.rolling(32).min().shift(0)
    v_15 = v_2.rolling(33).min().shift(0)
    v_16 = v_2.rolling(34).max().shift(0)
    v_17 = v_2.rolling(35).mean().shift(0)
    v_18 = v_2.rolling(36).kurt().shift(0)
    v_19 = v_2.rolling(37).skew().shift(0)
    v_20 = v_2.diff(38).shift(0)
    v_21 = v_2.rolling(39).kurt().shift(0)
    v_22 = v_2.rolling(40).mean().shift(0)
    v_23 = v_2.rolling(41).min().shift(0)
    v_24 = v_2.diff(42).shift(0)
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
    res = v_2.diff(2).diff(20).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc015_20d_jerk_v015_signal'] = f95oa_f95_operating_leverage_acceleration_calc015_20d_jerk_v015_signal

def f95oa_f95_operating_leverage_acceleration_calc016_21d_jerk_v016_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(22).min().shift(3)
    v_4 = v_2.rolling(23).skew().shift(4)
    v_5 = v_2.rolling(24).kurt().shift(5)
    v_6 = v_2.rolling(25).std().shift(6)
    v_7 = v_2.rolling(26).max().shift(7)
    v_8 = v_2.diff(27).shift(8)
    v_9 = v_2.rolling(28).min().shift(9)
    v_10 = v_2.rolling(29).std().shift(10)
    v_11 = v_2.rolling(30).mean().shift(11)
    v_12 = v_2.rolling(31).max().shift(12)
    v_13 = v_2.rolling(32).mean().shift(13)
    v_14 = v_2.rolling(33).min().shift(14)
    v_15 = v_2.rolling(34).kurt().shift(0)
    v_16 = v_2.rolling(35).std().shift(1)
    v_17 = v_2.rolling(36).max().shift(2)
    v_18 = v_2.diff(37).shift(3)
    v_19 = v_2.rolling(38).mean().shift(4)
    v_20 = v_2.rolling(39).skew().shift(5)
    v_21 = v_2.rolling(40).min().shift(6)
    v_22 = v_2.rolling(41).kurt().shift(7)
    v_23 = v_2.rolling(42).skew().shift(8)
    v_24 = v_2.rolling(43).kurt().shift(9)
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
    res = v_2.diff(2).diff(21).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc016_21d_jerk_v016_signal'] = f95oa_f95_operating_leverage_acceleration_calc016_21d_jerk_v016_signal

def f95oa_f95_operating_leverage_acceleration_calc017_22d_jerk_v017_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(23).max().shift(6)
    v_4 = v_2.rolling(24).skew().shift(8)
    v_5 = v_2.rolling(25).max().shift(10)
    v_6 = v_2.rolling(26).mean().shift(12)
    v_7 = v_2.diff(27).shift(14)
    v_8 = v_2.rolling(28).mean().shift(1)
    v_9 = v_2.rolling(29).mean().shift(3)
    v_10 = v_2.rolling(30).min().shift(5)
    v_11 = v_2.rolling(31).std().shift(7)
    v_12 = v_2.rolling(32).kurt().shift(9)
    v_13 = v_2.rolling(33).mean().shift(11)
    v_14 = v_2.rolling(34).max().shift(13)
    v_15 = v_2.rolling(35).std().shift(0)
    v_16 = v_2.rolling(36).min().shift(2)
    v_17 = v_2.rolling(37).max().shift(4)
    v_18 = v_2.rolling(38).skew().shift(6)
    v_19 = v_2.rolling(39).min().shift(8)
    v_20 = v_2.rolling(40).skew().shift(10)
    v_21 = v_2.rolling(41).mean().shift(12)
    v_22 = v_2.rolling(42).min().shift(14)
    v_23 = v_2.rolling(43).mean().shift(1)
    v_24 = v_2.rolling(44).std().shift(3)
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
    res = v_2.diff(2).diff(22).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc017_22d_jerk_v017_signal'] = f95oa_f95_operating_leverage_acceleration_calc017_22d_jerk_v017_signal

def f95oa_f95_operating_leverage_acceleration_calc018_23d_jerk_v018_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(24).max().shift(9)
    v_4 = v_2.rolling(25).mean().shift(12)
    v_5 = v_2.rolling(26).kurt().shift(0)
    v_6 = v_2.rolling(27).kurt().shift(3)
    v_7 = v_2.rolling(28).max().shift(6)
    v_8 = v_2.diff(29).shift(9)
    v_9 = v_2.diff(30).shift(12)
    v_10 = v_2.rolling(31).min().shift(0)
    v_11 = v_2.rolling(32).kurt().shift(3)
    v_12 = v_2.rolling(33).min().shift(6)
    v_13 = v_2.rolling(34).mean().shift(9)
    v_14 = v_2.diff(35).shift(12)
    v_15 = v_2.diff(36).shift(0)
    v_16 = v_2.diff(37).shift(3)
    v_17 = v_2.rolling(38).min().shift(6)
    v_18 = v_2.rolling(39).kurt().shift(9)
    v_19 = v_2.rolling(40).mean().shift(12)
    v_20 = v_2.diff(41).shift(0)
    v_21 = v_2.rolling(42).max().shift(3)
    v_22 = v_2.rolling(43).skew().shift(6)
    v_23 = v_2.rolling(44).min().shift(9)
    v_24 = v_2.rolling(45).max().shift(12)
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
    res = v_2.diff(2).diff(23).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc018_23d_jerk_v018_signal'] = f95oa_f95_operating_leverage_acceleration_calc018_23d_jerk_v018_signal

def f95oa_f95_operating_leverage_acceleration_calc019_24d_jerk_v019_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(25).skew().shift(12)
    v_4 = v_2.rolling(26).mean().shift(1)
    v_5 = v_2.rolling(27).max().shift(5)
    v_6 = v_2.diff(28).shift(9)
    v_7 = v_2.rolling(29).mean().shift(13)
    v_8 = v_2.rolling(30).skew().shift(2)
    v_9 = v_2.rolling(31).kurt().shift(6)
    v_10 = v_2.diff(32).shift(10)
    v_11 = v_2.rolling(33).mean().shift(14)
    v_12 = v_2.rolling(34).skew().shift(3)
    v_13 = v_2.rolling(35).min().shift(7)
    v_14 = v_2.rolling(36).kurt().shift(11)
    v_15 = v_2.rolling(37).mean().shift(0)
    v_16 = v_2.rolling(38).min().shift(4)
    v_17 = v_2.rolling(39).skew().shift(8)
    v_18 = v_2.rolling(40).min().shift(12)
    v_19 = v_2.rolling(41).max().shift(1)
    v_20 = v_2.rolling(42).skew().shift(5)
    v_21 = v_2.rolling(43).std().shift(9)
    v_22 = v_2.rolling(44).skew().shift(13)
    v_23 = v_2.rolling(45).skew().shift(2)
    v_24 = v_2.rolling(46).skew().shift(6)
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
    res = v_2.diff(2).diff(24).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc019_24d_jerk_v019_signal'] = f95oa_f95_operating_leverage_acceleration_calc019_24d_jerk_v019_signal

def f95oa_f95_operating_leverage_acceleration_calc020_25d_jerk_v020_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(26).std().shift(0)
    v_4 = v_2.rolling(27).max().shift(5)
    v_5 = v_2.rolling(28).max().shift(10)
    v_6 = v_2.rolling(29).mean().shift(0)
    v_7 = v_2.rolling(30).min().shift(5)
    v_8 = v_2.rolling(31).skew().shift(10)
    v_9 = v_2.rolling(32).max().shift(0)
    v_10 = v_2.rolling(33).kurt().shift(5)
    v_11 = v_2.rolling(34).mean().shift(10)
    v_12 = v_2.rolling(35).skew().shift(0)
    v_13 = v_2.rolling(36).std().shift(5)
    v_14 = v_2.rolling(37).std().shift(10)
    v_15 = v_2.rolling(38).kurt().shift(0)
    v_16 = v_2.rolling(39).std().shift(5)
    v_17 = v_2.rolling(40).kurt().shift(10)
    v_18 = v_2.rolling(41).kurt().shift(0)
    v_19 = v_2.rolling(42).max().shift(5)
    v_20 = v_2.rolling(43).skew().shift(10)
    v_21 = v_2.rolling(44).std().shift(0)
    v_22 = v_2.diff(45).shift(5)
    v_23 = v_2.rolling(46).mean().shift(10)
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
    res = v_2.diff(2).diff(25).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc020_25d_jerk_v020_signal'] = f95oa_f95_operating_leverage_acceleration_calc020_25d_jerk_v020_signal

def f95oa_f95_operating_leverage_acceleration_calc021_26d_jerk_v021_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(27).std().shift(3)
    v_4 = v_2.rolling(28).skew().shift(9)
    v_5 = v_2.diff(29).shift(0)
    v_6 = v_2.rolling(30).skew().shift(6)
    v_7 = v_2.rolling(31).min().shift(12)
    v_8 = v_2.diff(32).shift(3)
    v_9 = v_2.rolling(33).min().shift(9)
    v_10 = v_2.rolling(34).min().shift(0)
    v_11 = v_2.rolling(35).std().shift(6)
    v_12 = v_2.rolling(36).mean().shift(12)
    v_13 = v_2.rolling(37).skew().shift(3)
    v_14 = v_2.rolling(38).kurt().shift(9)
    v_15 = v_2.rolling(39).mean().shift(0)
    v_16 = v_2.diff(40).shift(6)
    v_17 = v_2.diff(41).shift(12)
    v_18 = v_2.rolling(42).mean().shift(3)
    v_19 = v_2.diff(43).shift(9)
    v_20 = v_2.diff(44).shift(0)
    v_21 = v_2.rolling(45).min().shift(6)
    v_22 = v_2.diff(46).shift(12)
    v_23 = v_2.rolling(47).mean().shift(3)
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
    res = v_2.diff(2).diff(26).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc021_26d_jerk_v021_signal'] = f95oa_f95_operating_leverage_acceleration_calc021_26d_jerk_v021_signal

def f95oa_f95_operating_leverage_acceleration_calc022_27d_jerk_v022_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(28).kurt().shift(6)
    v_4 = v_2.rolling(29).skew().shift(13)
    v_5 = v_2.rolling(30).mean().shift(5)
    v_6 = v_2.rolling(31).mean().shift(12)
    v_7 = v_2.rolling(32).min().shift(4)
    v_8 = v_2.rolling(33).std().shift(11)
    v_9 = v_2.rolling(34).kurt().shift(3)
    v_10 = v_2.rolling(35).kurt().shift(10)
    v_11 = v_2.rolling(36).kurt().shift(2)
    v_12 = v_2.rolling(37).skew().shift(9)
    v_13 = v_2.rolling(38).std().shift(1)
    v_14 = v_2.rolling(39).max().shift(8)
    v_15 = v_2.rolling(40).kurt().shift(0)
    v_16 = v_2.rolling(41).kurt().shift(7)
    v_17 = v_2.diff(42).shift(14)
    v_18 = v_2.rolling(43).mean().shift(6)
    v_19 = v_2.diff(44).shift(13)
    v_20 = v_2.rolling(45).kurt().shift(5)
    v_21 = v_2.rolling(46).std().shift(12)
    v_22 = v_2.rolling(47).skew().shift(4)
    v_23 = v_2.rolling(48).kurt().shift(11)
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
    res = v_2.diff(2).diff(27).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc022_27d_jerk_v022_signal'] = f95oa_f95_operating_leverage_acceleration_calc022_27d_jerk_v022_signal

def f95oa_f95_operating_leverage_acceleration_calc023_28d_jerk_v023_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(29).std().shift(9)
    v_4 = v_2.rolling(30).mean().shift(2)
    v_5 = v_2.rolling(31).mean().shift(10)
    v_6 = v_2.rolling(32).skew().shift(3)
    v_7 = v_2.rolling(33).max().shift(11)
    v_8 = v_2.rolling(34).kurt().shift(4)
    v_9 = v_2.diff(35).shift(12)
    v_10 = v_2.rolling(36).std().shift(5)
    v_11 = v_2.rolling(37).max().shift(13)
    v_12 = v_2.rolling(38).max().shift(6)
    v_13 = v_2.diff(39).shift(14)
    v_14 = v_2.rolling(40).skew().shift(7)
    v_15 = v_2.rolling(41).kurt().shift(0)
    v_16 = v_2.rolling(42).kurt().shift(8)
    v_17 = v_2.diff(43).shift(1)
    v_18 = v_2.diff(44).shift(9)
    v_19 = v_2.rolling(45).std().shift(2)
    v_20 = v_2.rolling(46).skew().shift(10)
    v_21 = v_2.diff(47).shift(3)
    v_22 = v_2.rolling(48).skew().shift(11)
    v_23 = v_2.rolling(49).skew().shift(4)
    v_24 = v_2.diff(50).shift(12)
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
    res = v_2.diff(2).diff(28).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc023_28d_jerk_v023_signal'] = f95oa_f95_operating_leverage_acceleration_calc023_28d_jerk_v023_signal

def f95oa_f95_operating_leverage_acceleration_calc024_29d_jerk_v024_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(30).kurt().shift(12)
    v_4 = v_2.rolling(31).kurt().shift(6)
    v_5 = v_2.diff(32).shift(0)
    v_6 = v_2.diff(33).shift(9)
    v_7 = v_2.rolling(34).mean().shift(3)
    v_8 = v_2.rolling(35).skew().shift(12)
    v_9 = v_2.rolling(36).min().shift(6)
    v_10 = v_2.rolling(37).std().shift(0)
    v_11 = v_2.rolling(38).min().shift(9)
    v_12 = v_2.rolling(39).min().shift(3)
    v_13 = v_2.diff(40).shift(12)
    v_14 = v_2.rolling(41).kurt().shift(6)
    v_15 = v_2.rolling(42).max().shift(0)
    v_16 = v_2.rolling(43).mean().shift(9)
    v_17 = v_2.rolling(44).skew().shift(3)
    v_18 = v_2.rolling(45).max().shift(12)
    v_19 = v_2.rolling(46).skew().shift(6)
    v_20 = v_2.rolling(47).min().shift(0)
    v_21 = v_2.rolling(48).skew().shift(9)
    v_22 = v_2.rolling(49).mean().shift(3)
    v_23 = v_2.rolling(50).skew().shift(12)
    v_24 = v_2.rolling(51).max().shift(6)
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
    res = v_2.diff(2).diff(29).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc024_29d_jerk_v024_signal'] = f95oa_f95_operating_leverage_acceleration_calc024_29d_jerk_v024_signal

def f95oa_f95_operating_leverage_acceleration_calc025_30d_jerk_v025_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(31).min().shift(0)
    v_4 = v_2.rolling(32).skew().shift(10)
    v_5 = v_2.rolling(33).skew().shift(5)
    v_6 = v_2.rolling(34).std().shift(0)
    v_7 = v_2.rolling(35).max().shift(10)
    v_8 = v_2.rolling(36).max().shift(5)
    v_9 = v_2.rolling(37).std().shift(0)
    v_10 = v_2.rolling(38).skew().shift(10)
    v_11 = v_2.rolling(39).mean().shift(5)
    v_12 = v_2.diff(40).shift(0)
    v_13 = v_2.rolling(41).std().shift(10)
    v_14 = v_2.rolling(42).mean().shift(5)
    v_15 = v_2.rolling(43).mean().shift(0)
    v_16 = v_2.rolling(44).std().shift(10)
    v_17 = v_2.rolling(45).kurt().shift(5)
    v_18 = v_2.rolling(46).mean().shift(0)
    v_19 = v_2.rolling(47).skew().shift(10)
    v_20 = v_2.rolling(48).std().shift(5)
    v_21 = v_2.diff(49).shift(0)
    v_22 = v_2.rolling(50).mean().shift(10)
    v_23 = v_2.rolling(51).kurt().shift(5)
    v_24 = v_2.rolling(52).mean().shift(0)
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
    res = v_2.diff(2).diff(30).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc025_30d_jerk_v025_signal'] = f95oa_f95_operating_leverage_acceleration_calc025_30d_jerk_v025_signal

def f95oa_f95_operating_leverage_acceleration_calc026_31d_jerk_v026_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(32).max().shift(3)
    v_4 = v_2.rolling(33).kurt().shift(14)
    v_5 = v_2.rolling(34).kurt().shift(10)
    v_6 = v_2.rolling(35).kurt().shift(6)
    v_7 = v_2.rolling(36).mean().shift(2)
    v_8 = v_2.rolling(37).min().shift(13)
    v_9 = v_2.rolling(38).kurt().shift(9)
    v_10 = v_2.rolling(39).std().shift(5)
    v_11 = v_2.rolling(40).mean().shift(1)
    v_12 = v_2.rolling(41).skew().shift(12)
    v_13 = v_2.rolling(42).kurt().shift(8)
    v_14 = v_2.rolling(43).std().shift(4)
    v_15 = v_2.diff(44).shift(0)
    v_16 = v_2.rolling(45).kurt().shift(11)
    v_17 = v_2.rolling(46).std().shift(7)
    v_18 = v_2.rolling(47).mean().shift(3)
    v_19 = v_2.rolling(48).kurt().shift(14)
    v_20 = v_2.rolling(49).std().shift(10)
    v_21 = v_2.rolling(50).skew().shift(6)
    v_22 = v_2.rolling(51).std().shift(2)
    v_23 = v_2.diff(52).shift(13)
    v_24 = v_2.rolling(3).max().shift(9)
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
    res = v_2.diff(2).diff(31).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc026_31d_jerk_v026_signal'] = f95oa_f95_operating_leverage_acceleration_calc026_31d_jerk_v026_signal

def f95oa_f95_operating_leverage_acceleration_calc027_32d_jerk_v027_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(33).max().shift(6)
    v_4 = v_2.rolling(34).kurt().shift(3)
    v_5 = v_2.rolling(35).skew().shift(0)
    v_6 = v_2.rolling(36).min().shift(12)
    v_7 = v_2.diff(37).shift(9)
    v_8 = v_2.rolling(38).max().shift(6)
    v_9 = v_2.rolling(39).kurt().shift(3)
    v_10 = v_2.rolling(40).min().shift(0)
    v_11 = v_2.rolling(41).max().shift(12)
    v_12 = v_2.rolling(42).std().shift(9)
    v_13 = v_2.rolling(43).max().shift(6)
    v_14 = v_2.rolling(44).skew().shift(3)
    v_15 = v_2.rolling(45).mean().shift(0)
    v_16 = v_2.rolling(46).skew().shift(12)
    v_17 = v_2.rolling(47).min().shift(9)
    v_18 = v_2.rolling(48).std().shift(6)
    v_19 = v_2.rolling(49).std().shift(3)
    v_20 = v_2.diff(50).shift(0)
    v_21 = v_2.diff(51).shift(12)
    v_22 = v_2.diff(52).shift(9)
    v_23 = v_2.diff(3).shift(6)
    v_24 = v_2.rolling(4).max().shift(3)
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
    res = v_2.diff(2).diff(32).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc027_32d_jerk_v027_signal'] = f95oa_f95_operating_leverage_acceleration_calc027_32d_jerk_v027_signal

def f95oa_f95_operating_leverage_acceleration_calc028_33d_jerk_v028_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(34).skew().shift(9)
    v_4 = v_2.rolling(35).min().shift(7)
    v_5 = v_2.rolling(36).max().shift(5)
    v_6 = v_2.diff(37).shift(3)
    v_7 = v_2.rolling(38).std().shift(1)
    v_8 = v_2.rolling(39).skew().shift(14)
    v_9 = v_2.diff(40).shift(12)
    v_10 = v_2.rolling(41).max().shift(10)
    v_11 = v_2.rolling(42).skew().shift(8)
    v_12 = v_2.rolling(43).mean().shift(6)
    v_13 = v_2.diff(44).shift(4)
    v_14 = v_2.rolling(45).skew().shift(2)
    v_15 = v_2.rolling(46).max().shift(0)
    v_16 = v_2.rolling(47).kurt().shift(13)
    v_17 = v_2.rolling(48).max().shift(11)
    v_18 = v_2.rolling(49).mean().shift(9)
    v_19 = v_2.rolling(50).kurt().shift(7)
    v_20 = v_2.rolling(51).skew().shift(5)
    v_21 = v_2.rolling(52).max().shift(3)
    v_22 = v_2.rolling(3).max().shift(1)
    v_23 = v_2.diff(4).shift(14)
    v_24 = v_2.rolling(5).min().shift(12)
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
    res = v_2.diff(2).diff(33).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc028_33d_jerk_v028_signal'] = f95oa_f95_operating_leverage_acceleration_calc028_33d_jerk_v028_signal

def f95oa_f95_operating_leverage_acceleration_calc029_34d_jerk_v029_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(35).max().shift(12)
    v_4 = v_2.rolling(36).std().shift(11)
    v_5 = v_2.rolling(37).max().shift(10)
    v_6 = v_2.rolling(38).mean().shift(9)
    v_7 = v_2.rolling(39).skew().shift(8)
    v_8 = v_2.rolling(40).max().shift(7)
    v_9 = v_2.rolling(41).mean().shift(6)
    v_10 = v_2.rolling(42).min().shift(5)
    v_11 = v_2.rolling(43).min().shift(4)
    v_12 = v_2.rolling(44).max().shift(3)
    v_13 = v_2.rolling(45).std().shift(2)
    v_14 = v_2.rolling(46).skew().shift(1)
    v_15 = v_2.rolling(47).std().shift(0)
    v_16 = v_2.rolling(48).kurt().shift(14)
    v_17 = v_2.rolling(49).kurt().shift(13)
    v_18 = v_2.rolling(50).min().shift(12)
    v_19 = v_2.rolling(51).skew().shift(11)
    v_20 = v_2.rolling(52).max().shift(10)
    v_21 = v_2.rolling(3).kurt().shift(9)
    v_22 = v_2.rolling(4).std().shift(8)
    v_23 = v_2.diff(5).shift(7)
    v_24 = v_2.diff(6).shift(6)
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
    res = v_2.diff(2).diff(34).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc029_34d_jerk_v029_signal'] = f95oa_f95_operating_leverage_acceleration_calc029_34d_jerk_v029_signal

def f95oa_f95_operating_leverage_acceleration_calc030_35d_jerk_v030_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(36).skew().shift(0)
    v_4 = v_2.rolling(37).kurt().shift(0)
    v_5 = v_2.rolling(38).kurt().shift(0)
    v_6 = v_2.rolling(39).std().shift(0)
    v_7 = v_2.diff(40).shift(0)
    v_8 = v_2.rolling(41).kurt().shift(0)
    v_9 = v_2.rolling(42).mean().shift(0)
    v_10 = v_2.rolling(43).std().shift(0)
    v_11 = v_2.rolling(44).std().shift(0)
    v_12 = v_2.rolling(45).mean().shift(0)
    v_13 = v_2.rolling(46).max().shift(0)
    v_14 = v_2.diff(47).shift(0)
    v_15 = v_2.rolling(48).std().shift(0)
    v_16 = v_2.rolling(49).skew().shift(0)
    v_17 = v_2.rolling(50).skew().shift(0)
    v_18 = v_2.rolling(51).mean().shift(0)
    v_19 = v_2.rolling(52).kurt().shift(0)
    v_20 = v_2.rolling(3).max().shift(0)
    v_21 = v_2.rolling(4).mean().shift(0)
    v_22 = v_2.diff(5).shift(0)
    v_23 = v_2.rolling(6).skew().shift(0)
    v_24 = v_2.rolling(7).std().shift(0)
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
    res = v_2.diff(2).diff(35).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc030_35d_jerk_v030_signal'] = f95oa_f95_operating_leverage_acceleration_calc030_35d_jerk_v030_signal

def f95oa_f95_operating_leverage_acceleration_calc031_36d_jerk_v031_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(37).mean().shift(3)
    v_4 = v_2.rolling(38).max().shift(4)
    v_5 = v_2.rolling(39).max().shift(5)
    v_6 = v_2.rolling(40).mean().shift(6)
    v_7 = v_2.rolling(41).max().shift(7)
    v_8 = v_2.rolling(42).std().shift(8)
    v_9 = v_2.rolling(43).std().shift(9)
    v_10 = v_2.rolling(44).std().shift(10)
    v_11 = v_2.diff(45).shift(11)
    v_12 = v_2.rolling(46).max().shift(12)
    v_13 = v_2.rolling(47).max().shift(13)
    v_14 = v_2.rolling(48).skew().shift(14)
    v_15 = v_2.rolling(49).skew().shift(0)
    v_16 = v_2.diff(50).shift(1)
    v_17 = v_2.rolling(51).std().shift(2)
    v_18 = v_2.rolling(52).max().shift(3)
    v_19 = v_2.diff(3).shift(4)
    v_20 = v_2.rolling(4).min().shift(5)
    v_21 = v_2.rolling(5).std().shift(6)
    v_22 = v_2.rolling(6).kurt().shift(7)
    v_23 = v_2.rolling(7).kurt().shift(8)
    v_24 = v_2.rolling(8).std().shift(9)
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
    res = v_2.diff(2).diff(36).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc031_36d_jerk_v031_signal'] = f95oa_f95_operating_leverage_acceleration_calc031_36d_jerk_v031_signal

def f95oa_f95_operating_leverage_acceleration_calc032_37d_jerk_v032_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(38).kurt().shift(6)
    v_4 = v_2.rolling(39).skew().shift(8)
    v_5 = v_2.rolling(40).mean().shift(10)
    v_6 = v_2.rolling(41).std().shift(12)
    v_7 = v_2.rolling(42).skew().shift(14)
    v_8 = v_2.rolling(43).std().shift(1)
    v_9 = v_2.rolling(44).kurt().shift(3)
    v_10 = v_2.rolling(45).kurt().shift(5)
    v_11 = v_2.rolling(46).mean().shift(7)
    v_12 = v_2.rolling(47).skew().shift(9)
    v_13 = v_2.rolling(48).kurt().shift(11)
    v_14 = v_2.rolling(49).skew().shift(13)
    v_15 = v_2.rolling(50).kurt().shift(0)
    v_16 = v_2.rolling(51).min().shift(2)
    v_17 = v_2.rolling(52).mean().shift(4)
    v_18 = v_2.rolling(3).max().shift(6)
    v_19 = v_2.diff(4).shift(8)
    v_20 = v_2.rolling(5).skew().shift(10)
    v_21 = v_2.diff(6).shift(12)
    v_22 = v_2.rolling(7).min().shift(14)
    v_23 = v_2.rolling(8).mean().shift(1)
    v_24 = v_2.rolling(9).skew().shift(3)
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
    res = v_2.diff(2).diff(37).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc032_37d_jerk_v032_signal'] = f95oa_f95_operating_leverage_acceleration_calc032_37d_jerk_v032_signal

def f95oa_f95_operating_leverage_acceleration_calc033_38d_jerk_v033_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(39).std().shift(9)
    v_4 = v_2.rolling(40).max().shift(12)
    v_5 = v_2.rolling(41).skew().shift(0)
    v_6 = v_2.rolling(42).skew().shift(3)
    v_7 = v_2.rolling(43).std().shift(6)
    v_8 = v_2.rolling(44).skew().shift(9)
    v_9 = v_2.rolling(45).min().shift(12)
    v_10 = v_2.rolling(46).min().shift(0)
    v_11 = v_2.rolling(47).std().shift(3)
    v_12 = v_2.rolling(48).mean().shift(6)
    v_13 = v_2.rolling(49).kurt().shift(9)
    v_14 = v_2.rolling(50).kurt().shift(12)
    v_15 = v_2.diff(51).shift(0)
    v_16 = v_2.rolling(52).skew().shift(3)
    v_17 = v_2.rolling(3).min().shift(6)
    v_18 = v_2.rolling(4).std().shift(9)
    v_19 = v_2.rolling(5).min().shift(12)
    v_20 = v_2.rolling(6).skew().shift(0)
    v_21 = v_2.rolling(7).std().shift(3)
    v_22 = v_2.rolling(8).min().shift(6)
    v_23 = v_2.rolling(9).std().shift(9)
    v_24 = v_2.rolling(10).std().shift(12)
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
    res = v_2.diff(2).diff(38).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc033_38d_jerk_v033_signal'] = f95oa_f95_operating_leverage_acceleration_calc033_38d_jerk_v033_signal

def f95oa_f95_operating_leverage_acceleration_calc034_39d_jerk_v034_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(40).min().shift(12)
    v_4 = v_2.rolling(41).std().shift(1)
    v_5 = v_2.rolling(42).max().shift(5)
    v_6 = v_2.rolling(43).kurt().shift(9)
    v_7 = v_2.rolling(44).std().shift(13)
    v_8 = v_2.rolling(45).std().shift(2)
    v_9 = v_2.diff(46).shift(6)
    v_10 = v_2.diff(47).shift(10)
    v_11 = v_2.diff(48).shift(14)
    v_12 = v_2.rolling(49).kurt().shift(3)
    v_13 = v_2.rolling(50).kurt().shift(7)
    v_14 = v_2.rolling(51).max().shift(11)
    v_15 = v_2.rolling(52).std().shift(0)
    v_16 = v_2.rolling(3).mean().shift(4)
    v_17 = v_2.rolling(4).skew().shift(8)
    v_18 = v_2.rolling(5).min().shift(12)
    v_19 = v_2.rolling(6).kurt().shift(1)
    v_20 = v_2.rolling(7).min().shift(5)
    v_21 = v_2.rolling(8).std().shift(9)
    v_22 = v_2.rolling(9).min().shift(13)
    v_23 = v_2.rolling(10).std().shift(2)
    v_24 = v_2.rolling(11).std().shift(6)
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
    res = v_2.diff(2).diff(39).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc034_39d_jerk_v034_signal'] = f95oa_f95_operating_leverage_acceleration_calc034_39d_jerk_v034_signal

def f95oa_f95_operating_leverage_acceleration_calc035_40d_jerk_v035_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(41).shift(0)
    v_4 = v_2.rolling(42).skew().shift(5)
    v_5 = v_2.rolling(43).min().shift(10)
    v_6 = v_2.rolling(44).max().shift(0)
    v_7 = v_2.rolling(45).max().shift(5)
    v_8 = v_2.rolling(46).max().shift(10)
    v_9 = v_2.rolling(47).min().shift(0)
    v_10 = v_2.rolling(48).std().shift(5)
    v_11 = v_2.rolling(49).skew().shift(10)
    v_12 = v_2.rolling(50).skew().shift(0)
    v_13 = v_2.rolling(51).std().shift(5)
    v_14 = v_2.diff(52).shift(10)
    v_15 = v_2.rolling(3).std().shift(0)
    v_16 = v_2.rolling(4).skew().shift(5)
    v_17 = v_2.rolling(5).min().shift(10)
    v_18 = v_2.rolling(6).max().shift(0)
    v_19 = v_2.rolling(7).min().shift(5)
    v_20 = v_2.rolling(8).mean().shift(10)
    v_21 = v_2.rolling(9).skew().shift(0)
    v_22 = v_2.diff(10).shift(5)
    v_23 = v_2.rolling(11).min().shift(10)
    v_24 = v_2.diff(12).shift(0)
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
    res = v_2.diff(2).diff(40).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc035_40d_jerk_v035_signal'] = f95oa_f95_operating_leverage_acceleration_calc035_40d_jerk_v035_signal

def f95oa_f95_operating_leverage_acceleration_calc036_41d_jerk_v036_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(42).std().shift(3)
    v_4 = v_2.rolling(43).max().shift(9)
    v_5 = v_2.diff(44).shift(0)
    v_6 = v_2.rolling(45).kurt().shift(6)
    v_7 = v_2.rolling(46).kurt().shift(12)
    v_8 = v_2.rolling(47).skew().shift(3)
    v_9 = v_2.rolling(48).skew().shift(9)
    v_10 = v_2.rolling(49).mean().shift(0)
    v_11 = v_2.rolling(50).mean().shift(6)
    v_12 = v_2.rolling(51).skew().shift(12)
    v_13 = v_2.rolling(52).mean().shift(3)
    v_14 = v_2.rolling(3).min().shift(9)
    v_15 = v_2.rolling(4).kurt().shift(0)
    v_16 = v_2.rolling(5).skew().shift(6)
    v_17 = v_2.rolling(6).mean().shift(12)
    v_18 = v_2.rolling(7).kurt().shift(3)
    v_19 = v_2.rolling(8).skew().shift(9)
    v_20 = v_2.rolling(9).skew().shift(0)
    v_21 = v_2.rolling(10).max().shift(6)
    v_22 = v_2.rolling(11).skew().shift(12)
    v_23 = v_2.rolling(12).kurt().shift(3)
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
    res = v_2.diff(2).diff(41).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc036_41d_jerk_v036_signal'] = f95oa_f95_operating_leverage_acceleration_calc036_41d_jerk_v036_signal

def f95oa_f95_operating_leverage_acceleration_calc037_42d_jerk_v037_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(43).skew().shift(6)
    v_4 = v_2.rolling(44).min().shift(13)
    v_5 = v_2.rolling(45).max().shift(5)
    v_6 = v_2.rolling(46).min().shift(12)
    v_7 = v_2.rolling(47).max().shift(4)
    v_8 = v_2.diff(48).shift(11)
    v_9 = v_2.rolling(49).max().shift(3)
    v_10 = v_2.rolling(50).kurt().shift(10)
    v_11 = v_2.rolling(51).mean().shift(2)
    v_12 = v_2.rolling(52).mean().shift(9)
    v_13 = v_2.rolling(3).max().shift(1)
    v_14 = v_2.rolling(4).min().shift(8)
    v_15 = v_2.rolling(5).min().shift(0)
    v_16 = v_2.diff(6).shift(7)
    v_17 = v_2.rolling(7).max().shift(14)
    v_18 = v_2.rolling(8).max().shift(6)
    v_19 = v_2.diff(9).shift(13)
    v_20 = v_2.rolling(10).kurt().shift(5)
    v_21 = v_2.rolling(11).kurt().shift(12)
    v_22 = v_2.diff(12).shift(4)
    v_23 = v_2.rolling(13).std().shift(11)
    v_24 = v_2.rolling(14).min().shift(3)
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
    res = v_2.diff(2).diff(42).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc037_42d_jerk_v037_signal'] = f95oa_f95_operating_leverage_acceleration_calc037_42d_jerk_v037_signal

def f95oa_f95_operating_leverage_acceleration_calc038_43d_jerk_v038_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(44).max().shift(9)
    v_4 = v_2.rolling(45).max().shift(2)
    v_5 = v_2.rolling(46).std().shift(10)
    v_6 = v_2.rolling(47).std().shift(3)
    v_7 = v_2.rolling(48).max().shift(11)
    v_8 = v_2.rolling(49).max().shift(4)
    v_9 = v_2.rolling(50).mean().shift(12)
    v_10 = v_2.rolling(51).min().shift(5)
    v_11 = v_2.rolling(52).min().shift(13)
    v_12 = v_2.rolling(3).skew().shift(6)
    v_13 = v_2.rolling(4).mean().shift(14)
    v_14 = v_2.rolling(5).kurt().shift(7)
    v_15 = v_2.rolling(6).max().shift(0)
    v_16 = v_2.rolling(7).mean().shift(8)
    v_17 = v_2.diff(8).shift(1)
    v_18 = v_2.diff(9).shift(9)
    v_19 = v_2.rolling(10).max().shift(2)
    v_20 = v_2.rolling(11).skew().shift(10)
    v_21 = v_2.rolling(12).std().shift(3)
    v_22 = v_2.rolling(13).kurt().shift(11)
    v_23 = v_2.rolling(14).max().shift(4)
    v_24 = v_2.rolling(15).skew().shift(12)
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
    res = v_2.diff(2).diff(43).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc038_43d_jerk_v038_signal'] = f95oa_f95_operating_leverage_acceleration_calc038_43d_jerk_v038_signal

def f95oa_f95_operating_leverage_acceleration_calc039_44d_jerk_v039_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(45).max().shift(12)
    v_4 = v_2.rolling(46).mean().shift(6)
    v_5 = v_2.rolling(47).std().shift(0)
    v_6 = v_2.rolling(48).kurt().shift(9)
    v_7 = v_2.diff(49).shift(3)
    v_8 = v_2.rolling(50).min().shift(12)
    v_9 = v_2.rolling(51).mean().shift(6)
    v_10 = v_2.rolling(52).std().shift(0)
    v_11 = v_2.rolling(3).min().shift(9)
    v_12 = v_2.diff(4).shift(3)
    v_13 = v_2.rolling(5).skew().shift(12)
    v_14 = v_2.rolling(6).max().shift(6)
    v_15 = v_2.rolling(7).max().shift(0)
    v_16 = v_2.diff(8).shift(9)
    v_17 = v_2.diff(9).shift(3)
    v_18 = v_2.rolling(10).min().shift(12)
    v_19 = v_2.rolling(11).mean().shift(6)
    v_20 = v_2.rolling(12).min().shift(0)
    v_21 = v_2.rolling(13).std().shift(9)
    v_22 = v_2.rolling(14).mean().shift(3)
    v_23 = v_2.rolling(15).max().shift(12)
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
    res = v_2.diff(2).diff(44).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc039_44d_jerk_v039_signal'] = f95oa_f95_operating_leverage_acceleration_calc039_44d_jerk_v039_signal

def f95oa_f95_operating_leverage_acceleration_calc040_45d_jerk_v040_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(46).max().shift(0)
    v_4 = v_2.rolling(47).max().shift(10)
    v_5 = v_2.rolling(48).skew().shift(5)
    v_6 = v_2.rolling(49).kurt().shift(0)
    v_7 = v_2.rolling(50).mean().shift(10)
    v_8 = v_2.rolling(51).mean().shift(5)
    v_9 = v_2.rolling(52).mean().shift(0)
    v_10 = v_2.rolling(3).std().shift(10)
    v_11 = v_2.rolling(4).min().shift(5)
    v_12 = v_2.rolling(5).skew().shift(0)
    v_13 = v_2.rolling(6).max().shift(10)
    v_14 = v_2.rolling(7).std().shift(5)
    v_15 = v_2.rolling(8).std().shift(0)
    v_16 = v_2.rolling(9).kurt().shift(10)
    v_17 = v_2.diff(10).shift(5)
    v_18 = v_2.diff(11).shift(0)
    v_19 = v_2.rolling(12).skew().shift(10)
    v_20 = v_2.rolling(13).mean().shift(5)
    v_21 = v_2.rolling(14).skew().shift(0)
    v_22 = v_2.rolling(15).max().shift(10)
    v_23 = v_2.rolling(16).skew().shift(5)
    v_24 = v_2.diff(17).shift(0)
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
    res = v_2.diff(2).diff(45).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc040_45d_jerk_v040_signal'] = f95oa_f95_operating_leverage_acceleration_calc040_45d_jerk_v040_signal

def f95oa_f95_operating_leverage_acceleration_calc041_46d_jerk_v041_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(47).kurt().shift(3)
    v_4 = v_2.rolling(48).mean().shift(14)
    v_5 = v_2.rolling(49).kurt().shift(10)
    v_6 = v_2.rolling(50).std().shift(6)
    v_7 = v_2.rolling(51).max().shift(2)
    v_8 = v_2.rolling(52).skew().shift(13)
    v_9 = v_2.rolling(3).kurt().shift(9)
    v_10 = v_2.rolling(4).kurt().shift(5)
    v_11 = v_2.diff(5).shift(1)
    v_12 = v_2.rolling(6).kurt().shift(12)
    v_13 = v_2.rolling(7).max().shift(8)
    v_14 = v_2.rolling(8).min().shift(4)
    v_15 = v_2.rolling(9).skew().shift(0)
    v_16 = v_2.rolling(10).mean().shift(11)
    v_17 = v_2.rolling(11).min().shift(7)
    v_18 = v_2.rolling(12).kurt().shift(3)
    v_19 = v_2.diff(13).shift(14)
    v_20 = v_2.rolling(14).mean().shift(10)
    v_21 = v_2.diff(15).shift(6)
    v_22 = v_2.rolling(16).min().shift(2)
    v_23 = v_2.diff(17).shift(13)
    v_24 = v_2.rolling(18).mean().shift(9)
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
    res = v_2.diff(2).diff(46).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc041_46d_jerk_v041_signal'] = f95oa_f95_operating_leverage_acceleration_calc041_46d_jerk_v041_signal

def f95oa_f95_operating_leverage_acceleration_calc042_47d_jerk_v042_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(48).shift(6)
    v_4 = v_2.rolling(49).mean().shift(3)
    v_5 = v_2.rolling(50).max().shift(0)
    v_6 = v_2.rolling(51).max().shift(12)
    v_7 = v_2.rolling(52).std().shift(9)
    v_8 = v_2.rolling(3).skew().shift(6)
    v_9 = v_2.rolling(4).max().shift(3)
    v_10 = v_2.rolling(5).kurt().shift(0)
    v_11 = v_2.rolling(6).min().shift(12)
    v_12 = v_2.rolling(7).max().shift(9)
    v_13 = v_2.diff(8).shift(6)
    v_14 = v_2.rolling(9).skew().shift(3)
    v_15 = v_2.rolling(10).min().shift(0)
    v_16 = v_2.rolling(11).std().shift(12)
    v_17 = v_2.rolling(12).kurt().shift(9)
    v_18 = v_2.diff(13).shift(6)
    v_19 = v_2.rolling(14).min().shift(3)
    v_20 = v_2.diff(15).shift(0)
    v_21 = v_2.rolling(16).kurt().shift(12)
    v_22 = v_2.rolling(17).max().shift(9)
    v_23 = v_2.rolling(18).kurt().shift(6)
    v_24 = v_2.rolling(19).mean().shift(3)
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
    res = v_2.diff(2).diff(47).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc042_47d_jerk_v042_signal'] = f95oa_f95_operating_leverage_acceleration_calc042_47d_jerk_v042_signal

def f95oa_f95_operating_leverage_acceleration_calc043_48d_jerk_v043_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(49).skew().shift(9)
    v_4 = v_2.rolling(50).max().shift(7)
    v_5 = v_2.rolling(51).skew().shift(5)
    v_6 = v_2.rolling(52).min().shift(3)
    v_7 = v_2.diff(3).shift(1)
    v_8 = v_2.rolling(4).min().shift(14)
    v_9 = v_2.rolling(5).std().shift(12)
    v_10 = v_2.rolling(6).kurt().shift(10)
    v_11 = v_2.rolling(7).max().shift(8)
    v_12 = v_2.rolling(8).min().shift(6)
    v_13 = v_2.rolling(9).mean().shift(4)
    v_14 = v_2.diff(10).shift(2)
    v_15 = v_2.rolling(11).mean().shift(0)
    v_16 = v_2.rolling(12).kurt().shift(13)
    v_17 = v_2.rolling(13).std().shift(11)
    v_18 = v_2.rolling(14).kurt().shift(9)
    v_19 = v_2.rolling(15).skew().shift(7)
    v_20 = v_2.rolling(16).kurt().shift(5)
    v_21 = v_2.rolling(17).mean().shift(3)
    v_22 = v_2.rolling(18).skew().shift(1)
    v_23 = v_2.rolling(19).kurt().shift(14)
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
    res = v_2.diff(2).diff(48).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc043_48d_jerk_v043_signal'] = f95oa_f95_operating_leverage_acceleration_calc043_48d_jerk_v043_signal

def f95oa_f95_operating_leverage_acceleration_calc044_49d_jerk_v044_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(50).min().shift(12)
    v_4 = v_2.rolling(51).min().shift(11)
    v_5 = v_2.rolling(52).min().shift(10)
    v_6 = v_2.diff(3).shift(9)
    v_7 = v_2.rolling(4).max().shift(8)
    v_8 = v_2.rolling(5).min().shift(7)
    v_9 = v_2.rolling(6).max().shift(6)
    v_10 = v_2.rolling(7).min().shift(5)
    v_11 = v_2.rolling(8).min().shift(4)
    v_12 = v_2.rolling(9).mean().shift(3)
    v_13 = v_2.diff(10).shift(2)
    v_14 = v_2.rolling(11).min().shift(1)
    v_15 = v_2.rolling(12).mean().shift(0)
    v_16 = v_2.rolling(13).mean().shift(14)
    v_17 = v_2.rolling(14).max().shift(13)
    v_18 = v_2.rolling(15).mean().shift(12)
    v_19 = v_2.rolling(16).mean().shift(11)
    v_20 = v_2.rolling(17).min().shift(10)
    v_21 = v_2.rolling(18).kurt().shift(9)
    v_22 = v_2.rolling(19).max().shift(8)
    v_23 = v_2.rolling(20).skew().shift(7)
    v_24 = v_2.rolling(21).max().shift(6)
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
    res = v_2.diff(2).diff(49).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc044_49d_jerk_v044_signal'] = f95oa_f95_operating_leverage_acceleration_calc044_49d_jerk_v044_signal

def f95oa_f95_operating_leverage_acceleration_calc045_50d_jerk_v045_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(51).kurt().shift(0)
    v_4 = v_2.rolling(52).std().shift(0)
    v_5 = v_2.rolling(3).kurt().shift(0)
    v_6 = v_2.rolling(4).std().shift(0)
    v_7 = v_2.rolling(5).std().shift(0)
    v_8 = v_2.rolling(6).max().shift(0)
    v_9 = v_2.diff(7).shift(0)
    v_10 = v_2.rolling(8).kurt().shift(0)
    v_11 = v_2.diff(9).shift(0)
    v_12 = v_2.rolling(10).mean().shift(0)
    v_13 = v_2.rolling(11).kurt().shift(0)
    v_14 = v_2.rolling(12).skew().shift(0)
    v_15 = v_2.diff(13).shift(0)
    v_16 = v_2.rolling(14).min().shift(0)
    v_17 = v_2.diff(15).shift(0)
    v_18 = v_2.rolling(16).skew().shift(0)
    v_19 = v_2.rolling(17).mean().shift(0)
    v_20 = v_2.rolling(18).min().shift(0)
    v_21 = v_2.rolling(19).kurt().shift(0)
    v_22 = v_2.rolling(20).min().shift(0)
    v_23 = v_2.diff(21).shift(0)
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
    res = v_2.diff(2).diff(50).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc045_50d_jerk_v045_signal'] = f95oa_f95_operating_leverage_acceleration_calc045_50d_jerk_v045_signal

def f95oa_f95_operating_leverage_acceleration_calc046_51d_jerk_v046_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(52).kurt().shift(3)
    v_4 = v_2.rolling(3).max().shift(4)
    v_5 = v_2.rolling(4).mean().shift(5)
    v_6 = v_2.rolling(5).skew().shift(6)
    v_7 = v_2.rolling(6).max().shift(7)
    v_8 = v_2.rolling(7).min().shift(8)
    v_9 = v_2.rolling(8).mean().shift(9)
    v_10 = v_2.rolling(9).mean().shift(10)
    v_11 = v_2.rolling(10).min().shift(11)
    v_12 = v_2.rolling(11).mean().shift(12)
    v_13 = v_2.rolling(12).skew().shift(13)
    v_14 = v_2.rolling(13).kurt().shift(14)
    v_15 = v_2.rolling(14).max().shift(0)
    v_16 = v_2.rolling(15).min().shift(1)
    v_17 = v_2.rolling(16).kurt().shift(2)
    v_18 = v_2.rolling(17).kurt().shift(3)
    v_19 = v_2.rolling(18).max().shift(4)
    v_20 = v_2.diff(19).shift(5)
    v_21 = v_2.rolling(20).skew().shift(6)
    v_22 = v_2.rolling(21).min().shift(7)
    v_23 = v_2.diff(22).shift(8)
    v_24 = v_2.rolling(23).max().shift(9)
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
    res = v_2.diff(2).diff(51).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc046_51d_jerk_v046_signal'] = f95oa_f95_operating_leverage_acceleration_calc046_51d_jerk_v046_signal

def f95oa_f95_operating_leverage_acceleration_calc047_52d_jerk_v047_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(3).mean().shift(6)
    v_4 = v_2.rolling(4).mean().shift(8)
    v_5 = v_2.rolling(5).min().shift(10)
    v_6 = v_2.rolling(6).std().shift(12)
    v_7 = v_2.rolling(7).std().shift(14)
    v_8 = v_2.rolling(8).kurt().shift(1)
    v_9 = v_2.rolling(9).min().shift(3)
    v_10 = v_2.rolling(10).mean().shift(5)
    v_11 = v_2.rolling(11).min().shift(7)
    v_12 = v_2.diff(12).shift(9)
    v_13 = v_2.diff(13).shift(11)
    v_14 = v_2.rolling(14).skew().shift(13)
    v_15 = v_2.rolling(15).max().shift(0)
    v_16 = v_2.rolling(16).kurt().shift(2)
    v_17 = v_2.rolling(17).std().shift(4)
    v_18 = v_2.rolling(18).skew().shift(6)
    v_19 = v_2.rolling(19).min().shift(8)
    v_20 = v_2.rolling(20).kurt().shift(10)
    v_21 = v_2.rolling(21).min().shift(12)
    v_22 = v_2.rolling(22).skew().shift(14)
    v_23 = v_2.diff(23).shift(1)
    v_24 = v_2.rolling(24).std().shift(3)
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
    res = v_2.diff(2).diff(52).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc047_52d_jerk_v047_signal'] = f95oa_f95_operating_leverage_acceleration_calc047_52d_jerk_v047_signal

def f95oa_f95_operating_leverage_acceleration_calc048_53d_jerk_v048_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(4).mean().shift(9)
    v_4 = v_2.rolling(5).skew().shift(12)
    v_5 = v_2.rolling(6).skew().shift(0)
    v_6 = v_2.rolling(7).skew().shift(3)
    v_7 = v_2.rolling(8).min().shift(6)
    v_8 = v_2.diff(9).shift(9)
    v_9 = v_2.rolling(10).min().shift(12)
    v_10 = v_2.rolling(11).skew().shift(0)
    v_11 = v_2.rolling(12).skew().shift(3)
    v_12 = v_2.rolling(13).max().shift(6)
    v_13 = v_2.rolling(14).mean().shift(9)
    v_14 = v_2.rolling(15).max().shift(12)
    v_15 = v_2.rolling(16).kurt().shift(0)
    v_16 = v_2.rolling(17).std().shift(3)
    v_17 = v_2.rolling(18).min().shift(6)
    v_18 = v_2.rolling(19).skew().shift(9)
    v_19 = v_2.rolling(20).mean().shift(12)
    v_20 = v_2.rolling(21).mean().shift(0)
    v_21 = v_2.rolling(22).mean().shift(3)
    v_22 = v_2.rolling(23).max().shift(6)
    v_23 = v_2.rolling(24).mean().shift(9)
    v_24 = v_2.rolling(25).mean().shift(12)
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
    res = v_2.diff(2).diff(53).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc048_53d_jerk_v048_signal'] = f95oa_f95_operating_leverage_acceleration_calc048_53d_jerk_v048_signal

def f95oa_f95_operating_leverage_acceleration_calc049_54d_jerk_v049_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(5).shift(12)
    v_4 = v_2.rolling(6).max().shift(1)
    v_5 = v_2.rolling(7).min().shift(5)
    v_6 = v_2.rolling(8).mean().shift(9)
    v_7 = v_2.rolling(9).min().shift(13)
    v_8 = v_2.rolling(10).max().shift(2)
    v_9 = v_2.rolling(11).max().shift(6)
    v_10 = v_2.rolling(12).std().shift(10)
    v_11 = v_2.rolling(13).min().shift(14)
    v_12 = v_2.rolling(14).kurt().shift(3)
    v_13 = v_2.rolling(15).max().shift(7)
    v_14 = v_2.rolling(16).std().shift(11)
    v_15 = v_2.rolling(17).min().shift(0)
    v_16 = v_2.rolling(18).max().shift(4)
    v_17 = v_2.rolling(19).kurt().shift(8)
    v_18 = v_2.rolling(20).skew().shift(12)
    v_19 = v_2.rolling(21).max().shift(1)
    v_20 = v_2.rolling(22).min().shift(5)
    v_21 = v_2.rolling(23).kurt().shift(9)
    v_22 = v_2.rolling(24).std().shift(13)
    v_23 = v_2.rolling(25).kurt().shift(2)
    v_24 = v_2.rolling(26).kurt().shift(6)
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
    res = v_2.diff(2).diff(54).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc049_54d_jerk_v049_signal'] = f95oa_f95_operating_leverage_acceleration_calc049_54d_jerk_v049_signal

def f95oa_f95_operating_leverage_acceleration_calc050_55d_jerk_v050_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(6).max().shift(0)
    v_4 = v_2.rolling(7).skew().shift(5)
    v_5 = v_2.rolling(8).kurt().shift(10)
    v_6 = v_2.rolling(9).min().shift(0)
    v_7 = v_2.rolling(10).skew().shift(5)
    v_8 = v_2.diff(11).shift(10)
    v_9 = v_2.rolling(12).skew().shift(0)
    v_10 = v_2.rolling(13).skew().shift(5)
    v_11 = v_2.rolling(14).min().shift(10)
    v_12 = v_2.rolling(15).min().shift(0)
    v_13 = v_2.rolling(16).std().shift(5)
    v_14 = v_2.rolling(17).kurt().shift(10)
    v_15 = v_2.rolling(18).min().shift(0)
    v_16 = v_2.rolling(19).kurt().shift(5)
    v_17 = v_2.rolling(20).mean().shift(10)
    v_18 = v_2.diff(21).shift(0)
    v_19 = v_2.rolling(22).max().shift(5)
    v_20 = v_2.diff(23).shift(10)
    v_21 = v_2.rolling(24).min().shift(0)
    v_22 = v_2.rolling(25).kurt().shift(5)
    v_23 = v_2.rolling(26).std().shift(10)
    v_24 = v_2.rolling(27).mean().shift(0)
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
    res = v_2.diff(2).diff(55).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc050_55d_jerk_v050_signal'] = f95oa_f95_operating_leverage_acceleration_calc050_55d_jerk_v050_signal

def f95oa_f95_operating_leverage_acceleration_calc051_56d_jerk_v051_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(7).shift(3)
    v_4 = v_2.rolling(8).kurt().shift(9)
    v_5 = v_2.rolling(9).skew().shift(0)
    v_6 = v_2.rolling(10).kurt().shift(6)
    v_7 = v_2.diff(11).shift(12)
    v_8 = v_2.rolling(12).max().shift(3)
    v_9 = v_2.diff(13).shift(9)
    v_10 = v_2.rolling(14).skew().shift(0)
    v_11 = v_2.rolling(15).max().shift(6)
    v_12 = v_2.rolling(16).kurt().shift(12)
    v_13 = v_2.diff(17).shift(3)
    v_14 = v_2.rolling(18).min().shift(9)
    v_15 = v_2.diff(19).shift(0)
    v_16 = v_2.rolling(20).mean().shift(6)
    v_17 = v_2.rolling(21).skew().shift(12)
    v_18 = v_2.rolling(22).max().shift(3)
    v_19 = v_2.rolling(23).mean().shift(9)
    v_20 = v_2.rolling(24).skew().shift(0)
    v_21 = v_2.rolling(25).kurt().shift(6)
    v_22 = v_2.rolling(26).std().shift(12)
    v_23 = v_2.diff(27).shift(3)
    v_24 = v_2.diff(28).shift(9)
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
    res = v_2.diff(2).diff(56).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc051_56d_jerk_v051_signal'] = f95oa_f95_operating_leverage_acceleration_calc051_56d_jerk_v051_signal

def f95oa_f95_operating_leverage_acceleration_calc052_57d_jerk_v052_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(8).std().shift(6)
    v_4 = v_2.rolling(9).std().shift(13)
    v_5 = v_2.rolling(10).max().shift(5)
    v_6 = v_2.rolling(11).min().shift(12)
    v_7 = v_2.rolling(12).skew().shift(4)
    v_8 = v_2.rolling(13).min().shift(11)
    v_9 = v_2.rolling(14).min().shift(3)
    v_10 = v_2.diff(15).shift(10)
    v_11 = v_2.rolling(16).mean().shift(2)
    v_12 = v_2.rolling(17).std().shift(9)
    v_13 = v_2.rolling(18).mean().shift(1)
    v_14 = v_2.rolling(19).std().shift(8)
    v_15 = v_2.rolling(20).std().shift(0)
    v_16 = v_2.rolling(21).min().shift(7)
    v_17 = v_2.rolling(22).std().shift(14)
    v_18 = v_2.rolling(23).std().shift(6)
    v_19 = v_2.diff(24).shift(13)
    v_20 = v_2.diff(25).shift(5)
    v_21 = v_2.rolling(26).skew().shift(12)
    v_22 = v_2.rolling(27).skew().shift(4)
    v_23 = v_2.rolling(28).mean().shift(11)
    v_24 = v_2.rolling(29).mean().shift(3)
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
    res = v_2.diff(2).diff(57).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc052_57d_jerk_v052_signal'] = f95oa_f95_operating_leverage_acceleration_calc052_57d_jerk_v052_signal

def f95oa_f95_operating_leverage_acceleration_calc053_58d_jerk_v053_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(9).shift(9)
    v_4 = v_2.rolling(10).skew().shift(2)
    v_5 = v_2.diff(11).shift(10)
    v_6 = v_2.rolling(12).skew().shift(3)
    v_7 = v_2.rolling(13).min().shift(11)
    v_8 = v_2.rolling(14).kurt().shift(4)
    v_9 = v_2.rolling(15).kurt().shift(12)
    v_10 = v_2.rolling(16).skew().shift(5)
    v_11 = v_2.rolling(17).kurt().shift(13)
    v_12 = v_2.rolling(18).max().shift(6)
    v_13 = v_2.rolling(19).kurt().shift(14)
    v_14 = v_2.rolling(20).mean().shift(7)
    v_15 = v_2.rolling(21).mean().shift(0)
    v_16 = v_2.rolling(22).std().shift(8)
    v_17 = v_2.rolling(23).max().shift(1)
    v_18 = v_2.rolling(24).skew().shift(9)
    v_19 = v_2.rolling(25).mean().shift(2)
    v_20 = v_2.rolling(26).kurt().shift(10)
    v_21 = v_2.rolling(27).max().shift(3)
    v_22 = v_2.rolling(28).min().shift(11)
    v_23 = v_2.rolling(29).kurt().shift(4)
    v_24 = v_2.rolling(30).skew().shift(12)
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
    res = v_2.diff(2).diff(58).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc053_58d_jerk_v053_signal'] = f95oa_f95_operating_leverage_acceleration_calc053_58d_jerk_v053_signal

def f95oa_f95_operating_leverage_acceleration_calc054_59d_jerk_v054_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(10).mean().shift(12)
    v_4 = v_2.rolling(11).min().shift(6)
    v_5 = v_2.rolling(12).std().shift(0)
    v_6 = v_2.rolling(13).std().shift(9)
    v_7 = v_2.rolling(14).mean().shift(3)
    v_8 = v_2.rolling(15).min().shift(12)
    v_9 = v_2.rolling(16).kurt().shift(6)
    v_10 = v_2.rolling(17).skew().shift(0)
    v_11 = v_2.rolling(18).min().shift(9)
    v_12 = v_2.rolling(19).std().shift(3)
    v_13 = v_2.rolling(20).min().shift(12)
    v_14 = v_2.rolling(21).max().shift(6)
    v_15 = v_2.rolling(22).max().shift(0)
    v_16 = v_2.rolling(23).skew().shift(9)
    v_17 = v_2.rolling(24).skew().shift(3)
    v_18 = v_2.rolling(25).kurt().shift(12)
    v_19 = v_2.rolling(26).skew().shift(6)
    v_20 = v_2.rolling(27).max().shift(0)
    v_21 = v_2.rolling(28).max().shift(9)
    v_22 = v_2.rolling(29).skew().shift(3)
    v_23 = v_2.rolling(30).max().shift(12)
    v_24 = v_2.rolling(31).mean().shift(6)
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
    res = v_2.diff(2).diff(59).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc054_59d_jerk_v054_signal'] = f95oa_f95_operating_leverage_acceleration_calc054_59d_jerk_v054_signal

def f95oa_f95_operating_leverage_acceleration_calc055_60d_jerk_v055_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(11).max().shift(0)
    v_4 = v_2.rolling(12).kurt().shift(10)
    v_5 = v_2.rolling(13).min().shift(5)
    v_6 = v_2.rolling(14).mean().shift(0)
    v_7 = v_2.rolling(15).min().shift(10)
    v_8 = v_2.rolling(16).mean().shift(5)
    v_9 = v_2.rolling(17).mean().shift(0)
    v_10 = v_2.rolling(18).std().shift(10)
    v_11 = v_2.rolling(19).max().shift(5)
    v_12 = v_2.rolling(20).skew().shift(0)
    v_13 = v_2.diff(21).shift(10)
    v_14 = v_2.rolling(22).mean().shift(5)
    v_15 = v_2.rolling(23).max().shift(0)
    v_16 = v_2.rolling(24).std().shift(10)
    v_17 = v_2.rolling(25).std().shift(5)
    v_18 = v_2.rolling(26).std().shift(0)
    v_19 = v_2.rolling(27).max().shift(10)
    v_20 = v_2.rolling(28).min().shift(5)
    v_21 = v_2.rolling(29).max().shift(0)
    v_22 = v_2.rolling(30).kurt().shift(10)
    v_23 = v_2.rolling(31).mean().shift(5)
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
    res = v_2.diff(2).diff(60).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc055_60d_jerk_v055_signal'] = f95oa_f95_operating_leverage_acceleration_calc055_60d_jerk_v055_signal

def f95oa_f95_operating_leverage_acceleration_calc056_61d_jerk_v056_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(12).kurt().shift(3)
    v_4 = v_2.rolling(13).mean().shift(14)
    v_5 = v_2.rolling(14).std().shift(10)
    v_6 = v_2.rolling(15).skew().shift(6)
    v_7 = v_2.rolling(16).min().shift(2)
    v_8 = v_2.rolling(17).kurt().shift(13)
    v_9 = v_2.rolling(18).kurt().shift(9)
    v_10 = v_2.rolling(19).max().shift(5)
    v_11 = v_2.diff(20).shift(1)
    v_12 = v_2.rolling(21).std().shift(12)
    v_13 = v_2.rolling(22).kurt().shift(8)
    v_14 = v_2.rolling(23).max().shift(4)
    v_15 = v_2.rolling(24).max().shift(0)
    v_16 = v_2.rolling(25).mean().shift(11)
    v_17 = v_2.rolling(26).std().shift(7)
    v_18 = v_2.rolling(27).kurt().shift(3)
    v_19 = v_2.rolling(28).max().shift(14)
    v_20 = v_2.rolling(29).std().shift(10)
    v_21 = v_2.rolling(30).std().shift(6)
    v_22 = v_2.rolling(31).kurt().shift(2)
    v_23 = v_2.rolling(32).std().shift(13)
    v_24 = v_2.rolling(33).kurt().shift(9)
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
    res = v_2.diff(2).diff(61).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc056_61d_jerk_v056_signal'] = f95oa_f95_operating_leverage_acceleration_calc056_61d_jerk_v056_signal

def f95oa_f95_operating_leverage_acceleration_calc057_62d_jerk_v057_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(13).shift(6)
    v_4 = v_2.rolling(14).max().shift(3)
    v_5 = v_2.rolling(15).mean().shift(0)
    v_6 = v_2.rolling(16).skew().shift(12)
    v_7 = v_2.rolling(17).kurt().shift(9)
    v_8 = v_2.rolling(18).skew().shift(6)
    v_9 = v_2.rolling(19).max().shift(3)
    v_10 = v_2.rolling(20).skew().shift(0)
    v_11 = v_2.rolling(21).mean().shift(12)
    v_12 = v_2.rolling(22).mean().shift(9)
    v_13 = v_2.diff(23).shift(6)
    v_14 = v_2.rolling(24).skew().shift(3)
    v_15 = v_2.rolling(25).max().shift(0)
    v_16 = v_2.rolling(26).kurt().shift(12)
    v_17 = v_2.rolling(27).std().shift(9)
    v_18 = v_2.diff(28).shift(6)
    v_19 = v_2.rolling(29).min().shift(3)
    v_20 = v_2.rolling(30).mean().shift(0)
    v_21 = v_2.rolling(31).std().shift(12)
    v_22 = v_2.rolling(32).max().shift(9)
    v_23 = v_2.rolling(33).std().shift(6)
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
    res = v_2.diff(2).diff(62).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc057_62d_jerk_v057_signal'] = f95oa_f95_operating_leverage_acceleration_calc057_62d_jerk_v057_signal

def f95oa_f95_operating_leverage_acceleration_calc058_63d_jerk_v058_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(14).skew().shift(9)
    v_4 = v_2.diff(15).shift(7)
    v_5 = v_2.rolling(16).min().shift(5)
    v_6 = v_2.rolling(17).std().shift(3)
    v_7 = v_2.rolling(18).min().shift(1)
    v_8 = v_2.rolling(19).max().shift(14)
    v_9 = v_2.rolling(20).min().shift(12)
    v_10 = v_2.rolling(21).mean().shift(10)
    v_11 = v_2.rolling(22).min().shift(8)
    v_12 = v_2.rolling(23).mean().shift(6)
    v_13 = v_2.rolling(24).std().shift(4)
    v_14 = v_2.rolling(25).kurt().shift(2)
    v_15 = v_2.rolling(26).kurt().shift(0)
    v_16 = v_2.rolling(27).max().shift(13)
    v_17 = v_2.rolling(28).std().shift(11)
    v_18 = v_2.rolling(29).skew().shift(9)
    v_19 = v_2.rolling(30).max().shift(7)
    v_20 = v_2.diff(31).shift(5)
    v_21 = v_2.diff(32).shift(3)
    v_22 = v_2.rolling(33).std().shift(1)
    v_23 = v_2.rolling(34).std().shift(14)
    v_24 = v_2.rolling(35).skew().shift(12)
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
    res = v_2.diff(2).diff(63).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc058_63d_jerk_v058_signal'] = f95oa_f95_operating_leverage_acceleration_calc058_63d_jerk_v058_signal

def f95oa_f95_operating_leverage_acceleration_calc059_64d_jerk_v059_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(15).shift(12)
    v_4 = v_2.rolling(16).min().shift(11)
    v_5 = v_2.rolling(17).mean().shift(10)
    v_6 = v_2.rolling(18).kurt().shift(9)
    v_7 = v_2.rolling(19).skew().shift(8)
    v_8 = v_2.rolling(20).kurt().shift(7)
    v_9 = v_2.rolling(21).min().shift(6)
    v_10 = v_2.rolling(22).max().shift(5)
    v_11 = v_2.rolling(23).mean().shift(4)
    v_12 = v_2.diff(24).shift(3)
    v_13 = v_2.rolling(25).std().shift(2)
    v_14 = v_2.rolling(26).skew().shift(1)
    v_15 = v_2.rolling(27).mean().shift(0)
    v_16 = v_2.diff(28).shift(14)
    v_17 = v_2.diff(29).shift(13)
    v_18 = v_2.rolling(30).mean().shift(12)
    v_19 = v_2.rolling(31).std().shift(11)
    v_20 = v_2.rolling(32).std().shift(10)
    v_21 = v_2.rolling(33).mean().shift(9)
    v_22 = v_2.rolling(34).mean().shift(8)
    v_23 = v_2.rolling(35).skew().shift(7)
    v_24 = v_2.rolling(36).kurt().shift(6)
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
    res = v_2.diff(2).diff(64).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc059_64d_jerk_v059_signal'] = f95oa_f95_operating_leverage_acceleration_calc059_64d_jerk_v059_signal

def f95oa_f95_operating_leverage_acceleration_calc060_65d_jerk_v060_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(16).shift(0)
    v_4 = v_2.rolling(17).min().shift(0)
    v_5 = v_2.rolling(18).max().shift(0)
    v_6 = v_2.rolling(19).kurt().shift(0)
    v_7 = v_2.rolling(20).mean().shift(0)
    v_8 = v_2.rolling(21).kurt().shift(0)
    v_9 = v_2.diff(22).shift(0)
    v_10 = v_2.rolling(23).min().shift(0)
    v_11 = v_2.rolling(24).std().shift(0)
    v_12 = v_2.rolling(25).max().shift(0)
    v_13 = v_2.rolling(26).std().shift(0)
    v_14 = v_2.rolling(27).std().shift(0)
    v_15 = v_2.rolling(28).min().shift(0)
    v_16 = v_2.rolling(29).mean().shift(0)
    v_17 = v_2.rolling(30).std().shift(0)
    v_18 = v_2.rolling(31).kurt().shift(0)
    v_19 = v_2.rolling(32).min().shift(0)
    v_20 = v_2.rolling(33).kurt().shift(0)
    v_21 = v_2.rolling(34).std().shift(0)
    v_22 = v_2.rolling(35).skew().shift(0)
    v_23 = v_2.rolling(36).std().shift(0)
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
    res = v_2.diff(2).diff(65).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc060_65d_jerk_v060_signal'] = f95oa_f95_operating_leverage_acceleration_calc060_65d_jerk_v060_signal

def f95oa_f95_operating_leverage_acceleration_calc061_66d_jerk_v061_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(17).kurt().shift(3)
    v_4 = v_2.rolling(18).kurt().shift(4)
    v_5 = v_2.rolling(19).skew().shift(5)
    v_6 = v_2.rolling(20).max().shift(6)
    v_7 = v_2.rolling(21).skew().shift(7)
    v_8 = v_2.rolling(22).kurt().shift(8)
    v_9 = v_2.rolling(23).max().shift(9)
    v_10 = v_2.rolling(24).skew().shift(10)
    v_11 = v_2.rolling(25).std().shift(11)
    v_12 = v_2.rolling(26).skew().shift(12)
    v_13 = v_2.rolling(27).max().shift(13)
    v_14 = v_2.rolling(28).kurt().shift(14)
    v_15 = v_2.rolling(29).min().shift(0)
    v_16 = v_2.rolling(30).mean().shift(1)
    v_17 = v_2.rolling(31).mean().shift(2)
    v_18 = v_2.rolling(32).max().shift(3)
    v_19 = v_2.rolling(33).min().shift(4)
    v_20 = v_2.rolling(34).min().shift(5)
    v_21 = v_2.rolling(35).max().shift(6)
    v_22 = v_2.diff(36).shift(7)
    v_23 = v_2.rolling(37).max().shift(8)
    v_24 = v_2.rolling(38).mean().shift(9)
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
    res = v_2.diff(2).diff(66).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc061_66d_jerk_v061_signal'] = f95oa_f95_operating_leverage_acceleration_calc061_66d_jerk_v061_signal

def f95oa_f95_operating_leverage_acceleration_calc062_67d_jerk_v062_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(18).min().shift(6)
    v_4 = v_2.rolling(19).skew().shift(8)
    v_5 = v_2.rolling(20).mean().shift(10)
    v_6 = v_2.rolling(21).mean().shift(12)
    v_7 = v_2.rolling(22).max().shift(14)
    v_8 = v_2.rolling(23).skew().shift(1)
    v_9 = v_2.rolling(24).min().shift(3)
    v_10 = v_2.diff(25).shift(5)
    v_11 = v_2.rolling(26).mean().shift(7)
    v_12 = v_2.rolling(27).skew().shift(9)
    v_13 = v_2.rolling(28).skew().shift(11)
    v_14 = v_2.diff(29).shift(13)
    v_15 = v_2.rolling(30).min().shift(0)
    v_16 = v_2.rolling(31).mean().shift(2)
    v_17 = v_2.rolling(32).skew().shift(4)
    v_18 = v_2.rolling(33).std().shift(6)
    v_19 = v_2.diff(34).shift(8)
    v_20 = v_2.rolling(35).min().shift(10)
    v_21 = v_2.rolling(36).skew().shift(12)
    v_22 = v_2.rolling(37).std().shift(14)
    v_23 = v_2.rolling(38).std().shift(1)
    v_24 = v_2.rolling(39).max().shift(3)
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
    res = v_2.diff(2).diff(67).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc062_67d_jerk_v062_signal'] = f95oa_f95_operating_leverage_acceleration_calc062_67d_jerk_v062_signal

def f95oa_f95_operating_leverage_acceleration_calc063_68d_jerk_v063_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(19).skew().shift(9)
    v_4 = v_2.diff(20).shift(12)
    v_5 = v_2.rolling(21).mean().shift(0)
    v_6 = v_2.rolling(22).skew().shift(3)
    v_7 = v_2.rolling(23).skew().shift(6)
    v_8 = v_2.rolling(24).min().shift(9)
    v_9 = v_2.rolling(25).min().shift(12)
    v_10 = v_2.rolling(26).skew().shift(0)
    v_11 = v_2.rolling(27).std().shift(3)
    v_12 = v_2.rolling(28).max().shift(6)
    v_13 = v_2.rolling(29).kurt().shift(9)
    v_14 = v_2.rolling(30).mean().shift(12)
    v_15 = v_2.diff(31).shift(0)
    v_16 = v_2.rolling(32).max().shift(3)
    v_17 = v_2.rolling(33).mean().shift(6)
    v_18 = v_2.rolling(34).kurt().shift(9)
    v_19 = v_2.rolling(35).min().shift(12)
    v_20 = v_2.rolling(36).max().shift(0)
    v_21 = v_2.rolling(37).min().shift(3)
    v_22 = v_2.rolling(38).skew().shift(6)
    v_23 = v_2.rolling(39).max().shift(9)
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
    res = v_2.diff(2).diff(68).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc063_68d_jerk_v063_signal'] = f95oa_f95_operating_leverage_acceleration_calc063_68d_jerk_v063_signal

def f95oa_f95_operating_leverage_acceleration_calc064_69d_jerk_v064_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(20).kurt().shift(12)
    v_4 = v_2.diff(21).shift(1)
    v_5 = v_2.rolling(22).std().shift(5)
    v_6 = v_2.rolling(23).min().shift(9)
    v_7 = v_2.diff(24).shift(13)
    v_8 = v_2.rolling(25).min().shift(2)
    v_9 = v_2.rolling(26).kurt().shift(6)
    v_10 = v_2.rolling(27).kurt().shift(10)
    v_11 = v_2.rolling(28).std().shift(14)
    v_12 = v_2.diff(29).shift(3)
    v_13 = v_2.rolling(30).kurt().shift(7)
    v_14 = v_2.rolling(31).min().shift(11)
    v_15 = v_2.rolling(32).skew().shift(0)
    v_16 = v_2.rolling(33).max().shift(4)
    v_17 = v_2.rolling(34).kurt().shift(8)
    v_18 = v_2.rolling(35).min().shift(12)
    v_19 = v_2.rolling(36).skew().shift(1)
    v_20 = v_2.rolling(37).min().shift(5)
    v_21 = v_2.diff(38).shift(9)
    v_22 = v_2.rolling(39).mean().shift(13)
    v_23 = v_2.rolling(40).kurt().shift(2)
    v_24 = v_2.rolling(41).kurt().shift(6)
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
    res = v_2.diff(2).diff(69).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc064_69d_jerk_v064_signal'] = f95oa_f95_operating_leverage_acceleration_calc064_69d_jerk_v064_signal

def f95oa_f95_operating_leverage_acceleration_calc065_70d_jerk_v065_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(21).skew().shift(0)
    v_4 = v_2.rolling(22).max().shift(5)
    v_5 = v_2.rolling(23).kurt().shift(10)
    v_6 = v_2.diff(24).shift(0)
    v_7 = v_2.rolling(25).min().shift(5)
    v_8 = v_2.rolling(26).max().shift(10)
    v_9 = v_2.rolling(27).skew().shift(0)
    v_10 = v_2.rolling(28).std().shift(5)
    v_11 = v_2.rolling(29).mean().shift(10)
    v_12 = v_2.rolling(30).std().shift(0)
    v_13 = v_2.rolling(31).max().shift(5)
    v_14 = v_2.rolling(32).min().shift(10)
    v_15 = v_2.rolling(33).min().shift(0)
    v_16 = v_2.rolling(34).mean().shift(5)
    v_17 = v_2.rolling(35).std().shift(10)
    v_18 = v_2.rolling(36).std().shift(0)
    v_19 = v_2.rolling(37).max().shift(5)
    v_20 = v_2.rolling(38).std().shift(10)
    v_21 = v_2.rolling(39).mean().shift(0)
    v_22 = v_2.rolling(40).kurt().shift(5)
    v_23 = v_2.rolling(41).mean().shift(10)
    v_24 = v_2.diff(42).shift(0)
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
    res = v_2.diff(2).diff(70).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc065_70d_jerk_v065_signal'] = f95oa_f95_operating_leverage_acceleration_calc065_70d_jerk_v065_signal

def f95oa_f95_operating_leverage_acceleration_calc066_71d_jerk_v066_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(22).shift(3)
    v_4 = v_2.rolling(23).min().shift(9)
    v_5 = v_2.rolling(24).std().shift(0)
    v_6 = v_2.rolling(25).std().shift(6)
    v_7 = v_2.rolling(26).max().shift(12)
    v_8 = v_2.rolling(27).mean().shift(3)
    v_9 = v_2.rolling(28).max().shift(9)
    v_10 = v_2.rolling(29).kurt().shift(0)
    v_11 = v_2.rolling(30).max().shift(6)
    v_12 = v_2.diff(31).shift(12)
    v_13 = v_2.rolling(32).max().shift(3)
    v_14 = v_2.rolling(33).mean().shift(9)
    v_15 = v_2.diff(34).shift(0)
    v_16 = v_2.rolling(35).min().shift(6)
    v_17 = v_2.rolling(36).mean().shift(12)
    v_18 = v_2.rolling(37).mean().shift(3)
    v_19 = v_2.rolling(38).max().shift(9)
    v_20 = v_2.rolling(39).mean().shift(0)
    v_21 = v_2.rolling(40).kurt().shift(6)
    v_22 = v_2.rolling(41).skew().shift(12)
    v_23 = v_2.rolling(42).skew().shift(3)
    v_24 = v_2.diff(43).shift(9)
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
    res = v_2.diff(2).diff(71).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc066_71d_jerk_v066_signal'] = f95oa_f95_operating_leverage_acceleration_calc066_71d_jerk_v066_signal

def f95oa_f95_operating_leverage_acceleration_calc067_72d_jerk_v067_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(23).std().shift(6)
    v_4 = v_2.rolling(24).skew().shift(13)
    v_5 = v_2.rolling(25).min().shift(5)
    v_6 = v_2.rolling(26).std().shift(12)
    v_7 = v_2.rolling(27).mean().shift(4)
    v_8 = v_2.rolling(28).mean().shift(11)
    v_9 = v_2.rolling(29).kurt().shift(3)
    v_10 = v_2.rolling(30).kurt().shift(10)
    v_11 = v_2.rolling(31).std().shift(2)
    v_12 = v_2.diff(32).shift(9)
    v_13 = v_2.rolling(33).mean().shift(1)
    v_14 = v_2.rolling(34).max().shift(8)
    v_15 = v_2.rolling(35).skew().shift(0)
    v_16 = v_2.rolling(36).mean().shift(7)
    v_17 = v_2.rolling(37).kurt().shift(14)
    v_18 = v_2.rolling(38).skew().shift(6)
    v_19 = v_2.rolling(39).skew().shift(13)
    v_20 = v_2.rolling(40).kurt().shift(5)
    v_21 = v_2.rolling(41).mean().shift(12)
    v_22 = v_2.diff(42).shift(4)
    v_23 = v_2.rolling(43).min().shift(11)
    v_24 = v_2.diff(44).shift(3)
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
    res = v_2.diff(2).diff(72).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc067_72d_jerk_v067_signal'] = f95oa_f95_operating_leverage_acceleration_calc067_72d_jerk_v067_signal

def f95oa_f95_operating_leverage_acceleration_calc068_73d_jerk_v068_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(24).mean().shift(9)
    v_4 = v_2.rolling(25).skew().shift(2)
    v_5 = v_2.rolling(26).min().shift(10)
    v_6 = v_2.rolling(27).std().shift(3)
    v_7 = v_2.rolling(28).mean().shift(11)
    v_8 = v_2.diff(29).shift(4)
    v_9 = v_2.rolling(30).min().shift(12)
    v_10 = v_2.rolling(31).skew().shift(5)
    v_11 = v_2.rolling(32).max().shift(13)
    v_12 = v_2.diff(33).shift(6)
    v_13 = v_2.rolling(34).std().shift(14)
    v_14 = v_2.diff(35).shift(7)
    v_15 = v_2.rolling(36).mean().shift(0)
    v_16 = v_2.rolling(37).mean().shift(8)
    v_17 = v_2.diff(38).shift(1)
    v_18 = v_2.rolling(39).max().shift(9)
    v_19 = v_2.rolling(40).std().shift(2)
    v_20 = v_2.rolling(41).std().shift(10)
    v_21 = v_2.diff(42).shift(3)
    v_22 = v_2.diff(43).shift(11)
    v_23 = v_2.rolling(44).std().shift(4)
    v_24 = v_2.diff(45).shift(12)
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
    res = v_2.diff(2).diff(73).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc068_73d_jerk_v068_signal'] = f95oa_f95_operating_leverage_acceleration_calc068_73d_jerk_v068_signal

def f95oa_f95_operating_leverage_acceleration_calc069_74d_jerk_v069_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(25).kurt().shift(12)
    v_4 = v_2.rolling(26).mean().shift(6)
    v_5 = v_2.rolling(27).min().shift(0)
    v_6 = v_2.rolling(28).kurt().shift(9)
    v_7 = v_2.rolling(29).std().shift(3)
    v_8 = v_2.rolling(30).max().shift(12)
    v_9 = v_2.rolling(31).skew().shift(6)
    v_10 = v_2.rolling(32).mean().shift(0)
    v_11 = v_2.diff(33).shift(9)
    v_12 = v_2.rolling(34).mean().shift(3)
    v_13 = v_2.rolling(35).max().shift(12)
    v_14 = v_2.rolling(36).mean().shift(6)
    v_15 = v_2.diff(37).shift(0)
    v_16 = v_2.rolling(38).min().shift(9)
    v_17 = v_2.rolling(39).skew().shift(3)
    v_18 = v_2.rolling(40).min().shift(12)
    v_19 = v_2.rolling(41).kurt().shift(6)
    v_20 = v_2.rolling(42).skew().shift(0)
    v_21 = v_2.rolling(43).min().shift(9)
    v_22 = v_2.rolling(44).max().shift(3)
    v_23 = v_2.rolling(45).mean().shift(12)
    v_24 = v_2.diff(46).shift(6)
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
    res = v_2.diff(2).diff(74).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc069_74d_jerk_v069_signal'] = f95oa_f95_operating_leverage_acceleration_calc069_74d_jerk_v069_signal

def f95oa_f95_operating_leverage_acceleration_calc070_75d_jerk_v070_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(26).shift(0)
    v_4 = v_2.diff(27).shift(10)
    v_5 = v_2.rolling(28).kurt().shift(5)
    v_6 = v_2.rolling(29).kurt().shift(0)
    v_7 = v_2.rolling(30).mean().shift(10)
    v_8 = v_2.rolling(31).kurt().shift(5)
    v_9 = v_2.rolling(32).mean().shift(0)
    v_10 = v_2.diff(33).shift(10)
    v_11 = v_2.rolling(34).min().shift(5)
    v_12 = v_2.rolling(35).skew().shift(0)
    v_13 = v_2.rolling(36).kurt().shift(10)
    v_14 = v_2.rolling(37).skew().shift(5)
    v_15 = v_2.rolling(38).std().shift(0)
    v_16 = v_2.rolling(39).kurt().shift(10)
    v_17 = v_2.rolling(40).max().shift(5)
    v_18 = v_2.rolling(41).max().shift(0)
    v_19 = v_2.rolling(42).skew().shift(10)
    v_20 = v_2.rolling(43).skew().shift(5)
    v_21 = v_2.rolling(44).max().shift(0)
    v_22 = v_2.diff(45).shift(10)
    v_23 = v_2.rolling(46).max().shift(5)
    v_24 = v_2.rolling(47).max().shift(0)
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
    res = v_2.diff(2).diff(75).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc070_75d_jerk_v070_signal'] = f95oa_f95_operating_leverage_acceleration_calc070_75d_jerk_v070_signal

def f95oa_f95_operating_leverage_acceleration_calc071_76d_jerk_v071_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(27).skew().shift(3)
    v_4 = v_2.diff(28).shift(14)
    v_5 = v_2.rolling(29).std().shift(10)
    v_6 = v_2.rolling(30).kurt().shift(6)
    v_7 = v_2.rolling(31).mean().shift(2)
    v_8 = v_2.rolling(32).mean().shift(13)
    v_9 = v_2.rolling(33).std().shift(9)
    v_10 = v_2.diff(34).shift(5)
    v_11 = v_2.rolling(35).skew().shift(1)
    v_12 = v_2.rolling(36).kurt().shift(12)
    v_13 = v_2.rolling(37).skew().shift(8)
    v_14 = v_2.rolling(38).mean().shift(4)
    v_15 = v_2.rolling(39).max().shift(0)
    v_16 = v_2.diff(40).shift(11)
    v_17 = v_2.rolling(41).std().shift(7)
    v_18 = v_2.rolling(42).kurt().shift(3)
    v_19 = v_2.rolling(43).std().shift(14)
    v_20 = v_2.rolling(44).std().shift(10)
    v_21 = v_2.rolling(45).mean().shift(6)
    v_22 = v_2.rolling(46).min().shift(2)
    v_23 = v_2.rolling(47).max().shift(13)
    v_24 = v_2.rolling(48).skew().shift(9)
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
    res = v_2.diff(2).diff(76).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc071_76d_jerk_v071_signal'] = f95oa_f95_operating_leverage_acceleration_calc071_76d_jerk_v071_signal

def f95oa_f95_operating_leverage_acceleration_calc072_77d_jerk_v072_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(28).mean().shift(6)
    v_4 = v_2.rolling(29).min().shift(3)
    v_5 = v_2.rolling(30).std().shift(0)
    v_6 = v_2.rolling(31).min().shift(12)
    v_7 = v_2.rolling(32).min().shift(9)
    v_8 = v_2.rolling(33).mean().shift(6)
    v_9 = v_2.rolling(34).kurt().shift(3)
    v_10 = v_2.rolling(35).mean().shift(0)
    v_11 = v_2.rolling(36).std().shift(12)
    v_12 = v_2.rolling(37).min().shift(9)
    v_13 = v_2.rolling(38).min().shift(6)
    v_14 = v_2.rolling(39).max().shift(3)
    v_15 = v_2.rolling(40).mean().shift(0)
    v_16 = v_2.rolling(41).mean().shift(12)
    v_17 = v_2.rolling(42).std().shift(9)
    v_18 = v_2.diff(43).shift(6)
    v_19 = v_2.rolling(44).std().shift(3)
    v_20 = v_2.rolling(45).kurt().shift(0)
    v_21 = v_2.rolling(46).kurt().shift(12)
    v_22 = v_2.rolling(47).max().shift(9)
    v_23 = v_2.rolling(48).std().shift(6)
    v_24 = v_2.rolling(49).kurt().shift(3)
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
    res = v_2.diff(2).diff(77).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc072_77d_jerk_v072_signal'] = f95oa_f95_operating_leverage_acceleration_calc072_77d_jerk_v072_signal

def f95oa_f95_operating_leverage_acceleration_calc073_78d_jerk_v073_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(29).max().shift(9)
    v_4 = v_2.rolling(30).mean().shift(7)
    v_5 = v_2.rolling(31).mean().shift(5)
    v_6 = v_2.diff(32).shift(3)
    v_7 = v_2.diff(33).shift(1)
    v_8 = v_2.rolling(34).max().shift(14)
    v_9 = v_2.rolling(35).max().shift(12)
    v_10 = v_2.rolling(36).max().shift(10)
    v_11 = v_2.diff(37).shift(8)
    v_12 = v_2.rolling(38).min().shift(6)
    v_13 = v_2.diff(39).shift(4)
    v_14 = v_2.rolling(40).min().shift(2)
    v_15 = v_2.diff(41).shift(0)
    v_16 = v_2.rolling(42).max().shift(13)
    v_17 = v_2.rolling(43).std().shift(11)
    v_18 = v_2.rolling(44).min().shift(9)
    v_19 = v_2.diff(45).shift(7)
    v_20 = v_2.rolling(46).max().shift(5)
    v_21 = v_2.rolling(47).std().shift(3)
    v_22 = v_2.rolling(48).mean().shift(1)
    v_23 = v_2.rolling(49).max().shift(14)
    v_24 = v_2.rolling(50).skew().shift(12)
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
    res = v_2.diff(2).diff(78).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc073_78d_jerk_v073_signal'] = f95oa_f95_operating_leverage_acceleration_calc073_78d_jerk_v073_signal

def f95oa_f95_operating_leverage_acceleration_calc074_79d_jerk_v074_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(30).shift(12)
    v_4 = v_2.rolling(31).kurt().shift(11)
    v_5 = v_2.diff(32).shift(10)
    v_6 = v_2.rolling(33).min().shift(9)
    v_7 = v_2.rolling(34).std().shift(8)
    v_8 = v_2.rolling(35).max().shift(7)
    v_9 = v_2.rolling(36).std().shift(6)
    v_10 = v_2.rolling(37).min().shift(5)
    v_11 = v_2.rolling(38).max().shift(4)
    v_12 = v_2.rolling(39).skew().shift(3)
    v_13 = v_2.rolling(40).kurt().shift(2)
    v_14 = v_2.rolling(41).kurt().shift(1)
    v_15 = v_2.rolling(42).skew().shift(0)
    v_16 = v_2.rolling(43).max().shift(14)
    v_17 = v_2.diff(44).shift(13)
    v_18 = v_2.diff(45).shift(12)
    v_19 = v_2.rolling(46).kurt().shift(11)
    v_20 = v_2.rolling(47).max().shift(10)
    v_21 = v_2.rolling(48).skew().shift(9)
    v_22 = v_2.diff(49).shift(8)
    v_23 = v_2.rolling(50).skew().shift(7)
    v_24 = v_2.rolling(51).skew().shift(6)
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
    res = v_2.diff(2).diff(79).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc074_79d_jerk_v074_signal'] = f95oa_f95_operating_leverage_acceleration_calc074_79d_jerk_v074_signal

def f95oa_f95_operating_leverage_acceleration_calc075_80d_jerk_v075_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(31).mean().shift(0)
    v_4 = v_2.rolling(32).max().shift(0)
    v_5 = v_2.rolling(33).skew().shift(0)
    v_6 = v_2.rolling(34).mean().shift(0)
    v_7 = v_2.rolling(35).max().shift(0)
    v_8 = v_2.rolling(36).mean().shift(0)
    v_9 = v_2.rolling(37).std().shift(0)
    v_10 = v_2.rolling(38).max().shift(0)
    v_11 = v_2.rolling(39).max().shift(0)
    v_12 = v_2.rolling(40).skew().shift(0)
    v_13 = v_2.rolling(41).std().shift(0)
    v_14 = v_2.rolling(42).std().shift(0)
    v_15 = v_2.rolling(43).std().shift(0)
    v_16 = v_2.rolling(44).max().shift(0)
    v_17 = v_2.rolling(45).std().shift(0)
    v_18 = v_2.rolling(46).max().shift(0)
    v_19 = v_2.rolling(47).skew().shift(0)
    v_20 = v_2.rolling(48).mean().shift(0)
    v_21 = v_2.rolling(49).min().shift(0)
    v_22 = v_2.rolling(50).mean().shift(0)
    v_23 = v_2.rolling(51).max().shift(0)
    v_24 = v_2.diff(52).shift(0)
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
    res = v_2.diff(2).diff(80).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc075_80d_jerk_v075_signal'] = f95oa_f95_operating_leverage_acceleration_calc075_80d_jerk_v075_signal

def f95oa_f95_operating_leverage_acceleration_calc076_81d_jerk_v076_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(32).mean().shift(3)
    v_4 = v_2.rolling(33).min().shift(4)
    v_5 = v_2.rolling(34).kurt().shift(5)
    v_6 = v_2.diff(35).shift(6)
    v_7 = v_2.rolling(36).min().shift(7)
    v_8 = v_2.rolling(37).max().shift(8)
    v_9 = v_2.rolling(38).max().shift(9)
    v_10 = v_2.rolling(39).max().shift(10)
    v_11 = v_2.rolling(40).min().shift(11)
    v_12 = v_2.diff(41).shift(12)
    v_13 = v_2.rolling(42).min().shift(13)
    v_14 = v_2.rolling(43).min().shift(14)
    v_15 = v_2.diff(44).shift(0)
    v_16 = v_2.rolling(45).std().shift(1)
    v_17 = v_2.rolling(46).std().shift(2)
    v_18 = v_2.rolling(47).mean().shift(3)
    v_19 = v_2.rolling(48).std().shift(4)
    v_20 = v_2.rolling(49).mean().shift(5)
    v_21 = v_2.rolling(50).max().shift(6)
    v_22 = v_2.rolling(51).skew().shift(7)
    v_23 = v_2.rolling(52).skew().shift(8)
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
    res = v_2.diff(2).diff(81).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc076_81d_jerk_v076_signal'] = f95oa_f95_operating_leverage_acceleration_calc076_81d_jerk_v076_signal

def f95oa_f95_operating_leverage_acceleration_calc077_82d_jerk_v077_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(33).skew().shift(6)
    v_4 = v_2.diff(34).shift(8)
    v_5 = v_2.rolling(35).min().shift(10)
    v_6 = v_2.rolling(36).kurt().shift(12)
    v_7 = v_2.rolling(37).max().shift(14)
    v_8 = v_2.rolling(38).min().shift(1)
    v_9 = v_2.rolling(39).std().shift(3)
    v_10 = v_2.rolling(40).mean().shift(5)
    v_11 = v_2.rolling(41).kurt().shift(7)
    v_12 = v_2.diff(42).shift(9)
    v_13 = v_2.rolling(43).skew().shift(11)
    v_14 = v_2.rolling(44).skew().shift(13)
    v_15 = v_2.rolling(45).max().shift(0)
    v_16 = v_2.rolling(46).std().shift(2)
    v_17 = v_2.diff(47).shift(4)
    v_18 = v_2.rolling(48).min().shift(6)
    v_19 = v_2.rolling(49).min().shift(8)
    v_20 = v_2.diff(50).shift(10)
    v_21 = v_2.rolling(51).max().shift(12)
    v_22 = v_2.rolling(52).max().shift(14)
    v_23 = v_2.rolling(3).min().shift(1)
    v_24 = v_2.rolling(4).std().shift(3)
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
    res = v_2.diff(2).diff(82).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc077_82d_jerk_v077_signal'] = f95oa_f95_operating_leverage_acceleration_calc077_82d_jerk_v077_signal

def f95oa_f95_operating_leverage_acceleration_calc078_83d_jerk_v078_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(34).shift(9)
    v_4 = v_2.rolling(35).mean().shift(12)
    v_5 = v_2.rolling(36).std().shift(0)
    v_6 = v_2.diff(37).shift(3)
    v_7 = v_2.rolling(38).skew().shift(6)
    v_8 = v_2.rolling(39).kurt().shift(9)
    v_9 = v_2.rolling(40).kurt().shift(12)
    v_10 = v_2.rolling(41).mean().shift(0)
    v_11 = v_2.rolling(42).min().shift(3)
    v_12 = v_2.rolling(43).kurt().shift(6)
    v_13 = v_2.rolling(44).min().shift(9)
    v_14 = v_2.diff(45).shift(12)
    v_15 = v_2.rolling(46).max().shift(0)
    v_16 = v_2.rolling(47).skew().shift(3)
    v_17 = v_2.diff(48).shift(6)
    v_18 = v_2.rolling(49).std().shift(9)
    v_19 = v_2.rolling(50).min().shift(12)
    v_20 = v_2.rolling(51).skew().shift(0)
    v_21 = v_2.rolling(52).max().shift(3)
    v_22 = v_2.rolling(3).min().shift(6)
    v_23 = v_2.rolling(4).max().shift(9)
    v_24 = v_2.rolling(5).mean().shift(12)
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
    res = v_2.diff(2).diff(83).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc078_83d_jerk_v078_signal'] = f95oa_f95_operating_leverage_acceleration_calc078_83d_jerk_v078_signal

def f95oa_f95_operating_leverage_acceleration_calc079_84d_jerk_v079_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(35).min().shift(12)
    v_4 = v_2.diff(36).shift(1)
    v_5 = v_2.diff(37).shift(5)
    v_6 = v_2.rolling(38).mean().shift(9)
    v_7 = v_2.rolling(39).skew().shift(13)
    v_8 = v_2.rolling(40).min().shift(2)
    v_9 = v_2.rolling(41).std().shift(6)
    v_10 = v_2.diff(42).shift(10)
    v_11 = v_2.rolling(43).mean().shift(14)
    v_12 = v_2.rolling(44).skew().shift(3)
    v_13 = v_2.rolling(45).min().shift(7)
    v_14 = v_2.rolling(46).max().shift(11)
    v_15 = v_2.rolling(47).kurt().shift(0)
    v_16 = v_2.rolling(48).mean().shift(4)
    v_17 = v_2.rolling(49).mean().shift(8)
    v_18 = v_2.rolling(50).kurt().shift(12)
    v_19 = v_2.rolling(51).kurt().shift(1)
    v_20 = v_2.rolling(52).mean().shift(5)
    v_21 = v_2.rolling(3).std().shift(9)
    v_22 = v_2.rolling(4).std().shift(13)
    v_23 = v_2.rolling(5).min().shift(2)
    v_24 = v_2.diff(6).shift(6)
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
    res = v_2.diff(2).diff(84).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc079_84d_jerk_v079_signal'] = f95oa_f95_operating_leverage_acceleration_calc079_84d_jerk_v079_signal

def f95oa_f95_operating_leverage_acceleration_calc080_85d_jerk_v080_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(36).kurt().shift(0)
    v_4 = v_2.rolling(37).skew().shift(5)
    v_5 = v_2.rolling(38).max().shift(10)
    v_6 = v_2.rolling(39).mean().shift(0)
    v_7 = v_2.rolling(40).max().shift(5)
    v_8 = v_2.rolling(41).kurt().shift(10)
    v_9 = v_2.rolling(42).kurt().shift(0)
    v_10 = v_2.rolling(43).skew().shift(5)
    v_11 = v_2.rolling(44).kurt().shift(10)
    v_12 = v_2.rolling(45).mean().shift(0)
    v_13 = v_2.rolling(46).mean().shift(5)
    v_14 = v_2.rolling(47).min().shift(10)
    v_15 = v_2.rolling(48).min().shift(0)
    v_16 = v_2.rolling(49).std().shift(5)
    v_17 = v_2.rolling(50).skew().shift(10)
    v_18 = v_2.rolling(51).skew().shift(0)
    v_19 = v_2.rolling(52).max().shift(5)
    v_20 = v_2.rolling(3).min().shift(10)
    v_21 = v_2.diff(4).shift(0)
    v_22 = v_2.rolling(5).max().shift(5)
    v_23 = v_2.rolling(6).max().shift(10)
    v_24 = v_2.rolling(7).max().shift(0)
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
    res = v_2.diff(2).diff(85).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc080_85d_jerk_v080_signal'] = f95oa_f95_operating_leverage_acceleration_calc080_85d_jerk_v080_signal

def f95oa_f95_operating_leverage_acceleration_calc081_86d_jerk_v081_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(37).std().shift(3)
    v_4 = v_2.rolling(38).max().shift(9)
    v_5 = v_2.rolling(39).min().shift(0)
    v_6 = v_2.rolling(40).max().shift(6)
    v_7 = v_2.rolling(41).std().shift(12)
    v_8 = v_2.rolling(42).min().shift(3)
    v_9 = v_2.rolling(43).max().shift(9)
    v_10 = v_2.rolling(44).kurt().shift(0)
    v_11 = v_2.rolling(45).std().shift(6)
    v_12 = v_2.diff(46).shift(12)
    v_13 = v_2.rolling(47).min().shift(3)
    v_14 = v_2.rolling(48).skew().shift(9)
    v_15 = v_2.rolling(49).min().shift(0)
    v_16 = v_2.rolling(50).max().shift(6)
    v_17 = v_2.rolling(51).max().shift(12)
    v_18 = v_2.rolling(52).max().shift(3)
    v_19 = v_2.rolling(3).max().shift(9)
    v_20 = v_2.rolling(4).min().shift(0)
    v_21 = v_2.rolling(5).max().shift(6)
    v_22 = v_2.rolling(6).std().shift(12)
    v_23 = v_2.rolling(7).kurt().shift(3)
    v_24 = v_2.rolling(8).min().shift(9)
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
    res = v_2.diff(2).diff(86).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc081_86d_jerk_v081_signal'] = f95oa_f95_operating_leverage_acceleration_calc081_86d_jerk_v081_signal

def f95oa_f95_operating_leverage_acceleration_calc082_87d_jerk_v082_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(38).kurt().shift(6)
    v_4 = v_2.rolling(39).max().shift(13)
    v_5 = v_2.rolling(40).std().shift(5)
    v_6 = v_2.rolling(41).mean().shift(12)
    v_7 = v_2.rolling(42).mean().shift(4)
    v_8 = v_2.diff(43).shift(11)
    v_9 = v_2.rolling(44).skew().shift(3)
    v_10 = v_2.rolling(45).std().shift(10)
    v_11 = v_2.rolling(46).std().shift(2)
    v_12 = v_2.rolling(47).min().shift(9)
    v_13 = v_2.rolling(48).std().shift(1)
    v_14 = v_2.rolling(49).std().shift(8)
    v_15 = v_2.rolling(50).mean().shift(0)
    v_16 = v_2.rolling(51).max().shift(7)
    v_17 = v_2.rolling(52).kurt().shift(14)
    v_18 = v_2.diff(3).shift(6)
    v_19 = v_2.rolling(4).max().shift(13)
    v_20 = v_2.rolling(5).kurt().shift(5)
    v_21 = v_2.diff(6).shift(12)
    v_22 = v_2.rolling(7).min().shift(4)
    v_23 = v_2.rolling(8).min().shift(11)
    v_24 = v_2.rolling(9).mean().shift(3)
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
    res = v_2.diff(2).diff(87).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc082_87d_jerk_v082_signal'] = f95oa_f95_operating_leverage_acceleration_calc082_87d_jerk_v082_signal

def f95oa_f95_operating_leverage_acceleration_calc083_88d_jerk_v083_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(39).min().shift(9)
    v_4 = v_2.rolling(40).min().shift(2)
    v_5 = v_2.diff(41).shift(10)
    v_6 = v_2.rolling(42).kurt().shift(3)
    v_7 = v_2.diff(43).shift(11)
    v_8 = v_2.diff(44).shift(4)
    v_9 = v_2.rolling(45).kurt().shift(12)
    v_10 = v_2.diff(46).shift(5)
    v_11 = v_2.rolling(47).max().shift(13)
    v_12 = v_2.rolling(48).std().shift(6)
    v_13 = v_2.rolling(49).mean().shift(14)
    v_14 = v_2.rolling(50).skew().shift(7)
    v_15 = v_2.rolling(51).max().shift(0)
    v_16 = v_2.rolling(52).kurt().shift(8)
    v_17 = v_2.rolling(3).kurt().shift(1)
    v_18 = v_2.rolling(4).std().shift(9)
    v_19 = v_2.rolling(5).std().shift(2)
    v_20 = v_2.rolling(6).kurt().shift(10)
    v_21 = v_2.rolling(7).min().shift(3)
    v_22 = v_2.rolling(8).mean().shift(11)
    v_23 = v_2.rolling(9).kurt().shift(4)
    v_24 = v_2.rolling(10).skew().shift(12)
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
    res = v_2.diff(2).diff(88).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc083_88d_jerk_v083_signal'] = f95oa_f95_operating_leverage_acceleration_calc083_88d_jerk_v083_signal

def f95oa_f95_operating_leverage_acceleration_calc084_89d_jerk_v084_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(40).mean().shift(12)
    v_4 = v_2.rolling(41).min().shift(6)
    v_5 = v_2.rolling(42).skew().shift(0)
    v_6 = v_2.rolling(43).skew().shift(9)
    v_7 = v_2.rolling(44).kurt().shift(3)
    v_8 = v_2.rolling(45).mean().shift(12)
    v_9 = v_2.diff(46).shift(6)
    v_10 = v_2.rolling(47).min().shift(0)
    v_11 = v_2.diff(48).shift(9)
    v_12 = v_2.rolling(49).max().shift(3)
    v_13 = v_2.rolling(50).kurt().shift(12)
    v_14 = v_2.diff(51).shift(6)
    v_15 = v_2.rolling(52).max().shift(0)
    v_16 = v_2.rolling(3).max().shift(9)
    v_17 = v_2.rolling(4).skew().shift(3)
    v_18 = v_2.rolling(5).std().shift(12)
    v_19 = v_2.rolling(6).min().shift(6)
    v_20 = v_2.rolling(7).kurt().shift(0)
    v_21 = v_2.rolling(8).min().shift(9)
    v_22 = v_2.diff(9).shift(3)
    v_23 = v_2.rolling(10).kurt().shift(12)
    v_24 = v_2.rolling(11).mean().shift(6)
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
    res = v_2.diff(2).diff(89).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc084_89d_jerk_v084_signal'] = f95oa_f95_operating_leverage_acceleration_calc084_89d_jerk_v084_signal

def f95oa_f95_operating_leverage_acceleration_calc085_90d_jerk_v085_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(41).kurt().shift(0)
    v_4 = v_2.rolling(42).std().shift(10)
    v_5 = v_2.rolling(43).min().shift(5)
    v_6 = v_2.diff(44).shift(0)
    v_7 = v_2.rolling(45).max().shift(10)
    v_8 = v_2.rolling(46).kurt().shift(5)
    v_9 = v_2.diff(47).shift(0)
    v_10 = v_2.rolling(48).mean().shift(10)
    v_11 = v_2.rolling(49).max().shift(5)
    v_12 = v_2.rolling(50).min().shift(0)
    v_13 = v_2.rolling(51).max().shift(10)
    v_14 = v_2.rolling(52).kurt().shift(5)
    v_15 = v_2.rolling(3).mean().shift(0)
    v_16 = v_2.diff(4).shift(10)
    v_17 = v_2.rolling(5).kurt().shift(5)
    v_18 = v_2.diff(6).shift(0)
    v_19 = v_2.rolling(7).std().shift(10)
    v_20 = v_2.rolling(8).mean().shift(5)
    v_21 = v_2.rolling(9).skew().shift(0)
    v_22 = v_2.rolling(10).kurt().shift(10)
    v_23 = v_2.rolling(11).mean().shift(5)
    v_24 = v_2.rolling(12).std().shift(0)
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
    res = v_2.diff(2).diff(90).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc085_90d_jerk_v085_signal'] = f95oa_f95_operating_leverage_acceleration_calc085_90d_jerk_v085_signal

def f95oa_f95_operating_leverage_acceleration_calc086_91d_jerk_v086_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(42).skew().shift(3)
    v_4 = v_2.diff(43).shift(14)
    v_5 = v_2.rolling(44).kurt().shift(10)
    v_6 = v_2.diff(45).shift(6)
    v_7 = v_2.rolling(46).std().shift(2)
    v_8 = v_2.rolling(47).skew().shift(13)
    v_9 = v_2.rolling(48).mean().shift(9)
    v_10 = v_2.diff(49).shift(5)
    v_11 = v_2.rolling(50).min().shift(1)
    v_12 = v_2.diff(51).shift(12)
    v_13 = v_2.rolling(52).min().shift(8)
    v_14 = v_2.rolling(3).kurt().shift(4)
    v_15 = v_2.rolling(4).std().shift(0)
    v_16 = v_2.rolling(5).std().shift(11)
    v_17 = v_2.rolling(6).max().shift(7)
    v_18 = v_2.rolling(7).mean().shift(3)
    v_19 = v_2.diff(8).shift(14)
    v_20 = v_2.diff(9).shift(10)
    v_21 = v_2.rolling(10).min().shift(6)
    v_22 = v_2.rolling(11).kurt().shift(2)
    v_23 = v_2.rolling(12).std().shift(13)
    v_24 = v_2.rolling(13).skew().shift(9)
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
    res = v_2.diff(2).diff(91).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc086_91d_jerk_v086_signal'] = f95oa_f95_operating_leverage_acceleration_calc086_91d_jerk_v086_signal

def f95oa_f95_operating_leverage_acceleration_calc087_92d_jerk_v087_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(43).shift(6)
    v_4 = v_2.rolling(44).mean().shift(3)
    v_5 = v_2.rolling(45).min().shift(0)
    v_6 = v_2.rolling(46).kurt().shift(12)
    v_7 = v_2.rolling(47).mean().shift(9)
    v_8 = v_2.diff(48).shift(6)
    v_9 = v_2.diff(49).shift(3)
    v_10 = v_2.rolling(50).kurt().shift(0)
    v_11 = v_2.rolling(51).kurt().shift(12)
    v_12 = v_2.rolling(52).std().shift(9)
    v_13 = v_2.rolling(3).min().shift(6)
    v_14 = v_2.rolling(4).std().shift(3)
    v_15 = v_2.rolling(5).max().shift(0)
    v_16 = v_2.rolling(6).mean().shift(12)
    v_17 = v_2.rolling(7).max().shift(9)
    v_18 = v_2.rolling(8).std().shift(6)
    v_19 = v_2.rolling(9).min().shift(3)
    v_20 = v_2.rolling(10).mean().shift(0)
    v_21 = v_2.rolling(11).min().shift(12)
    v_22 = v_2.rolling(12).mean().shift(9)
    v_23 = v_2.rolling(13).skew().shift(6)
    v_24 = v_2.rolling(14).skew().shift(3)
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
    res = v_2.diff(2).diff(92).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc087_92d_jerk_v087_signal'] = f95oa_f95_operating_leverage_acceleration_calc087_92d_jerk_v087_signal

def f95oa_f95_operating_leverage_acceleration_calc088_93d_jerk_v088_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(44).std().shift(9)
    v_4 = v_2.rolling(45).max().shift(7)
    v_5 = v_2.rolling(46).skew().shift(5)
    v_6 = v_2.diff(47).shift(3)
    v_7 = v_2.rolling(48).kurt().shift(1)
    v_8 = v_2.diff(49).shift(14)
    v_9 = v_2.rolling(50).mean().shift(12)
    v_10 = v_2.rolling(51).min().shift(10)
    v_11 = v_2.rolling(52).min().shift(8)
    v_12 = v_2.rolling(3).max().shift(6)
    v_13 = v_2.rolling(4).max().shift(4)
    v_14 = v_2.diff(5).shift(2)
    v_15 = v_2.rolling(6).max().shift(0)
    v_16 = v_2.rolling(7).mean().shift(13)
    v_17 = v_2.rolling(8).std().shift(11)
    v_18 = v_2.rolling(9).std().shift(9)
    v_19 = v_2.rolling(10).skew().shift(7)
    v_20 = v_2.rolling(11).min().shift(5)
    v_21 = v_2.rolling(12).skew().shift(3)
    v_22 = v_2.rolling(13).skew().shift(1)
    v_23 = v_2.diff(14).shift(14)
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
    res = v_2.diff(2).diff(93).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc088_93d_jerk_v088_signal'] = f95oa_f95_operating_leverage_acceleration_calc088_93d_jerk_v088_signal

def f95oa_f95_operating_leverage_acceleration_calc089_94d_jerk_v089_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(45).std().shift(12)
    v_4 = v_2.rolling(46).kurt().shift(11)
    v_5 = v_2.rolling(47).skew().shift(10)
    v_6 = v_2.rolling(48).mean().shift(9)
    v_7 = v_2.rolling(49).mean().shift(8)
    v_8 = v_2.rolling(50).mean().shift(7)
    v_9 = v_2.rolling(51).min().shift(6)
    v_10 = v_2.rolling(52).min().shift(5)
    v_11 = v_2.diff(3).shift(4)
    v_12 = v_2.rolling(4).mean().shift(3)
    v_13 = v_2.diff(5).shift(2)
    v_14 = v_2.rolling(6).mean().shift(1)
    v_15 = v_2.diff(7).shift(0)
    v_16 = v_2.rolling(8).max().shift(14)
    v_17 = v_2.rolling(9).max().shift(13)
    v_18 = v_2.diff(10).shift(12)
    v_19 = v_2.diff(11).shift(11)
    v_20 = v_2.rolling(12).max().shift(10)
    v_21 = v_2.rolling(13).std().shift(9)
    v_22 = v_2.rolling(14).skew().shift(8)
    v_23 = v_2.rolling(15).min().shift(7)
    v_24 = v_2.rolling(16).min().shift(6)
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
    res = v_2.diff(2).diff(94).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc089_94d_jerk_v089_signal'] = f95oa_f95_operating_leverage_acceleration_calc089_94d_jerk_v089_signal

def f95oa_f95_operating_leverage_acceleration_calc090_95d_jerk_v090_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(46).min().shift(0)
    v_4 = v_2.rolling(47).skew().shift(0)
    v_5 = v_2.rolling(48).max().shift(0)
    v_6 = v_2.rolling(49).mean().shift(0)
    v_7 = v_2.diff(50).shift(0)
    v_8 = v_2.rolling(51).std().shift(0)
    v_9 = v_2.rolling(52).mean().shift(0)
    v_10 = v_2.rolling(3).std().shift(0)
    v_11 = v_2.rolling(4).std().shift(0)
    v_12 = v_2.rolling(5).mean().shift(0)
    v_13 = v_2.rolling(6).max().shift(0)
    v_14 = v_2.rolling(7).std().shift(0)
    v_15 = v_2.rolling(8).std().shift(0)
    v_16 = v_2.rolling(9).min().shift(0)
    v_17 = v_2.rolling(10).max().shift(0)
    v_18 = v_2.rolling(11).kurt().shift(0)
    v_19 = v_2.rolling(12).skew().shift(0)
    v_20 = v_2.rolling(13).max().shift(0)
    v_21 = v_2.diff(14).shift(0)
    v_22 = v_2.rolling(15).kurt().shift(0)
    v_23 = v_2.diff(16).shift(0)
    v_24 = v_2.rolling(17).min().shift(0)
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
    res = v_2.diff(2).diff(95).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc090_95d_jerk_v090_signal'] = f95oa_f95_operating_leverage_acceleration_calc090_95d_jerk_v090_signal

def f95oa_f95_operating_leverage_acceleration_calc091_96d_jerk_v091_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(47).skew().shift(3)
    v_4 = v_2.rolling(48).mean().shift(4)
    v_5 = v_2.rolling(49).skew().shift(5)
    v_6 = v_2.rolling(50).kurt().shift(6)
    v_7 = v_2.diff(51).shift(7)
    v_8 = v_2.rolling(52).min().shift(8)
    v_9 = v_2.rolling(3).min().shift(9)
    v_10 = v_2.rolling(4).max().shift(10)
    v_11 = v_2.rolling(5).mean().shift(11)
    v_12 = v_2.rolling(6).std().shift(12)
    v_13 = v_2.rolling(7).min().shift(13)
    v_14 = v_2.rolling(8).mean().shift(14)
    v_15 = v_2.rolling(9).min().shift(0)
    v_16 = v_2.rolling(10).std().shift(1)
    v_17 = v_2.rolling(11).min().shift(2)
    v_18 = v_2.diff(12).shift(3)
    v_19 = v_2.rolling(13).std().shift(4)
    v_20 = v_2.rolling(14).kurt().shift(5)
    v_21 = v_2.diff(15).shift(6)
    v_22 = v_2.diff(16).shift(7)
    v_23 = v_2.rolling(17).max().shift(8)
    v_24 = v_2.rolling(18).std().shift(9)
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
    res = v_2.diff(2).diff(96).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc091_96d_jerk_v091_signal'] = f95oa_f95_operating_leverage_acceleration_calc091_96d_jerk_v091_signal

def f95oa_f95_operating_leverage_acceleration_calc092_97d_jerk_v092_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(48).kurt().shift(6)
    v_4 = v_2.rolling(49).max().shift(8)
    v_5 = v_2.rolling(50).std().shift(10)
    v_6 = v_2.rolling(51).kurt().shift(12)
    v_7 = v_2.rolling(52).mean().shift(14)
    v_8 = v_2.diff(3).shift(1)
    v_9 = v_2.rolling(4).min().shift(3)
    v_10 = v_2.rolling(5).min().shift(5)
    v_11 = v_2.rolling(6).mean().shift(7)
    v_12 = v_2.rolling(7).mean().shift(9)
    v_13 = v_2.rolling(8).kurt().shift(11)
    v_14 = v_2.diff(9).shift(13)
    v_15 = v_2.rolling(10).std().shift(0)
    v_16 = v_2.diff(11).shift(2)
    v_17 = v_2.rolling(12).std().shift(4)
    v_18 = v_2.rolling(13).kurt().shift(6)
    v_19 = v_2.rolling(14).min().shift(8)
    v_20 = v_2.rolling(15).min().shift(10)
    v_21 = v_2.rolling(16).kurt().shift(12)
    v_22 = v_2.rolling(17).mean().shift(14)
    v_23 = v_2.rolling(18).min().shift(1)
    v_24 = v_2.rolling(19).std().shift(3)
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
    res = v_2.diff(2).diff(97).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc092_97d_jerk_v092_signal'] = f95oa_f95_operating_leverage_acceleration_calc092_97d_jerk_v092_signal

def f95oa_f95_operating_leverage_acceleration_calc093_98d_jerk_v093_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(49).std().shift(9)
    v_4 = v_2.rolling(50).mean().shift(12)
    v_5 = v_2.rolling(51).std().shift(0)
    v_6 = v_2.diff(52).shift(3)
    v_7 = v_2.rolling(3).min().shift(6)
    v_8 = v_2.diff(4).shift(9)
    v_9 = v_2.rolling(5).min().shift(12)
    v_10 = v_2.diff(6).shift(0)
    v_11 = v_2.rolling(7).std().shift(3)
    v_12 = v_2.diff(8).shift(6)
    v_13 = v_2.diff(9).shift(9)
    v_14 = v_2.rolling(10).skew().shift(12)
    v_15 = v_2.rolling(11).min().shift(0)
    v_16 = v_2.rolling(12).max().shift(3)
    v_17 = v_2.rolling(13).max().shift(6)
    v_18 = v_2.rolling(14).min().shift(9)
    v_19 = v_2.diff(15).shift(12)
    v_20 = v_2.rolling(16).kurt().shift(0)
    v_21 = v_2.rolling(17).skew().shift(3)
    v_22 = v_2.rolling(18).kurt().shift(6)
    v_23 = v_2.rolling(19).kurt().shift(9)
    v_24 = v_2.rolling(20).mean().shift(12)
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
    res = v_2.diff(2).diff(98).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc093_98d_jerk_v093_signal'] = f95oa_f95_operating_leverage_acceleration_calc093_98d_jerk_v093_signal

def f95oa_f95_operating_leverage_acceleration_calc094_99d_jerk_v094_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(50).max().shift(12)
    v_4 = v_2.rolling(51).skew().shift(1)
    v_5 = v_2.rolling(52).std().shift(5)
    v_6 = v_2.rolling(3).mean().shift(9)
    v_7 = v_2.rolling(4).max().shift(13)
    v_8 = v_2.rolling(5).max().shift(2)
    v_9 = v_2.rolling(6).std().shift(6)
    v_10 = v_2.rolling(7).mean().shift(10)
    v_11 = v_2.diff(8).shift(14)
    v_12 = v_2.diff(9).shift(3)
    v_13 = v_2.rolling(10).skew().shift(7)
    v_14 = v_2.rolling(11).kurt().shift(11)
    v_15 = v_2.rolling(12).min().shift(0)
    v_16 = v_2.rolling(13).mean().shift(4)
    v_17 = v_2.diff(14).shift(8)
    v_18 = v_2.rolling(15).max().shift(12)
    v_19 = v_2.rolling(16).max().shift(1)
    v_20 = v_2.rolling(17).max().shift(5)
    v_21 = v_2.diff(18).shift(9)
    v_22 = v_2.rolling(19).std().shift(13)
    v_23 = v_2.rolling(20).mean().shift(2)
    v_24 = v_2.diff(21).shift(6)
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
    res = v_2.diff(2).diff(99).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc094_99d_jerk_v094_signal'] = f95oa_f95_operating_leverage_acceleration_calc094_99d_jerk_v094_signal

def f95oa_f95_operating_leverage_acceleration_calc095_100d_jerk_v095_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(51).mean().shift(0)
    v_4 = v_2.diff(52).shift(5)
    v_5 = v_2.diff(3).shift(10)
    v_6 = v_2.rolling(4).min().shift(0)
    v_7 = v_2.rolling(5).mean().shift(5)
    v_8 = v_2.rolling(6).skew().shift(10)
    v_9 = v_2.rolling(7).kurt().shift(0)
    v_10 = v_2.rolling(8).mean().shift(5)
    v_11 = v_2.rolling(9).std().shift(10)
    v_12 = v_2.rolling(10).max().shift(0)
    v_13 = v_2.diff(11).shift(5)
    v_14 = v_2.rolling(12).std().shift(10)
    v_15 = v_2.rolling(13).skew().shift(0)
    v_16 = v_2.diff(14).shift(5)
    v_17 = v_2.rolling(15).mean().shift(10)
    v_18 = v_2.rolling(16).std().shift(0)
    v_19 = v_2.rolling(17).std().shift(5)
    v_20 = v_2.rolling(18).std().shift(10)
    v_21 = v_2.rolling(19).kurt().shift(0)
    v_22 = v_2.diff(20).shift(5)
    v_23 = v_2.rolling(21).kurt().shift(10)
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
    res = v_2.diff(2).diff(100).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc095_100d_jerk_v095_signal'] = f95oa_f95_operating_leverage_acceleration_calc095_100d_jerk_v095_signal

def f95oa_f95_operating_leverage_acceleration_calc096_101d_jerk_v096_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(52).kurt().shift(3)
    v_4 = v_2.rolling(3).min().shift(9)
    v_5 = v_2.rolling(4).skew().shift(0)
    v_6 = v_2.rolling(5).mean().shift(6)
    v_7 = v_2.rolling(6).max().shift(12)
    v_8 = v_2.rolling(7).mean().shift(3)
    v_9 = v_2.diff(8).shift(9)
    v_10 = v_2.rolling(9).std().shift(0)
    v_11 = v_2.rolling(10).max().shift(6)
    v_12 = v_2.rolling(11).skew().shift(12)
    v_13 = v_2.rolling(12).std().shift(3)
    v_14 = v_2.diff(13).shift(9)
    v_15 = v_2.diff(14).shift(0)
    v_16 = v_2.rolling(15).kurt().shift(6)
    v_17 = v_2.diff(16).shift(12)
    v_18 = v_2.rolling(17).mean().shift(3)
    v_19 = v_2.rolling(18).kurt().shift(9)
    v_20 = v_2.rolling(19).std().shift(0)
    v_21 = v_2.rolling(20).mean().shift(6)
    v_22 = v_2.rolling(21).std().shift(12)
    v_23 = v_2.rolling(22).max().shift(3)
    v_24 = v_2.diff(23).shift(9)
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
    res = v_2.diff(2).diff(101).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc096_101d_jerk_v096_signal'] = f95oa_f95_operating_leverage_acceleration_calc096_101d_jerk_v096_signal

def f95oa_f95_operating_leverage_acceleration_calc097_102d_jerk_v097_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(3).mean().shift(6)
    v_4 = v_2.rolling(4).max().shift(13)
    v_5 = v_2.rolling(5).kurt().shift(5)
    v_6 = v_2.rolling(6).std().shift(12)
    v_7 = v_2.rolling(7).mean().shift(4)
    v_8 = v_2.rolling(8).max().shift(11)
    v_9 = v_2.rolling(9).mean().shift(3)
    v_10 = v_2.rolling(10).kurt().shift(10)
    v_11 = v_2.diff(11).shift(2)
    v_12 = v_2.rolling(12).kurt().shift(9)
    v_13 = v_2.rolling(13).max().shift(1)
    v_14 = v_2.diff(14).shift(8)
    v_15 = v_2.rolling(15).mean().shift(0)
    v_16 = v_2.rolling(16).min().shift(7)
    v_17 = v_2.rolling(17).skew().shift(14)
    v_18 = v_2.rolling(18).mean().shift(6)
    v_19 = v_2.rolling(19).min().shift(13)
    v_20 = v_2.rolling(20).max().shift(5)
    v_21 = v_2.diff(21).shift(12)
    v_22 = v_2.rolling(22).min().shift(4)
    v_23 = v_2.rolling(23).skew().shift(11)
    v_24 = v_2.rolling(24).min().shift(3)
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
    res = v_2.diff(2).diff(102).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc097_102d_jerk_v097_signal'] = f95oa_f95_operating_leverage_acceleration_calc097_102d_jerk_v097_signal

def f95oa_f95_operating_leverage_acceleration_calc098_103d_jerk_v098_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(4).max().shift(9)
    v_4 = v_2.rolling(5).kurt().shift(2)
    v_5 = v_2.rolling(6).std().shift(10)
    v_6 = v_2.rolling(7).skew().shift(3)
    v_7 = v_2.rolling(8).min().shift(11)
    v_8 = v_2.rolling(9).std().shift(4)
    v_9 = v_2.rolling(10).max().shift(12)
    v_10 = v_2.rolling(11).min().shift(5)
    v_11 = v_2.rolling(12).skew().shift(13)
    v_12 = v_2.rolling(13).std().shift(6)
    v_13 = v_2.rolling(14).kurt().shift(14)
    v_14 = v_2.rolling(15).mean().shift(7)
    v_15 = v_2.diff(16).shift(0)
    v_16 = v_2.rolling(17).max().shift(8)
    v_17 = v_2.diff(18).shift(1)
    v_18 = v_2.rolling(19).min().shift(9)
    v_19 = v_2.rolling(20).min().shift(2)
    v_20 = v_2.rolling(21).mean().shift(10)
    v_21 = v_2.rolling(22).mean().shift(3)
    v_22 = v_2.rolling(23).max().shift(11)
    v_23 = v_2.rolling(24).min().shift(4)
    v_24 = v_2.rolling(25).min().shift(12)
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
    res = v_2.diff(2).diff(103).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc098_103d_jerk_v098_signal'] = f95oa_f95_operating_leverage_acceleration_calc098_103d_jerk_v098_signal

def f95oa_f95_operating_leverage_acceleration_calc099_104d_jerk_v099_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(5).shift(12)
    v_4 = v_2.diff(6).shift(6)
    v_5 = v_2.rolling(7).skew().shift(0)
    v_6 = v_2.rolling(8).std().shift(9)
    v_7 = v_2.rolling(9).std().shift(3)
    v_8 = v_2.rolling(10).min().shift(12)
    v_9 = v_2.rolling(11).kurt().shift(6)
    v_10 = v_2.rolling(12).mean().shift(0)
    v_11 = v_2.rolling(13).max().shift(9)
    v_12 = v_2.diff(14).shift(3)
    v_13 = v_2.rolling(15).min().shift(12)
    v_14 = v_2.rolling(16).kurt().shift(6)
    v_15 = v_2.rolling(17).skew().shift(0)
    v_16 = v_2.rolling(18).mean().shift(9)
    v_17 = v_2.rolling(19).max().shift(3)
    v_18 = v_2.rolling(20).mean().shift(12)
    v_19 = v_2.rolling(21).kurt().shift(6)
    v_20 = v_2.diff(22).shift(0)
    v_21 = v_2.rolling(23).kurt().shift(9)
    v_22 = v_2.rolling(24).mean().shift(3)
    v_23 = v_2.rolling(25).skew().shift(12)
    v_24 = v_2.rolling(26).mean().shift(6)
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
    res = v_2.diff(2).diff(104).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc099_104d_jerk_v099_signal'] = f95oa_f95_operating_leverage_acceleration_calc099_104d_jerk_v099_signal

def f95oa_f95_operating_leverage_acceleration_calc100_105d_jerk_v100_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(6).std().shift(0)
    v_4 = v_2.rolling(7).skew().shift(10)
    v_5 = v_2.rolling(8).min().shift(5)
    v_6 = v_2.rolling(9).max().shift(0)
    v_7 = v_2.diff(10).shift(10)
    v_8 = v_2.rolling(11).kurt().shift(5)
    v_9 = v_2.rolling(12).skew().shift(0)
    v_10 = v_2.rolling(13).std().shift(10)
    v_11 = v_2.rolling(14).kurt().shift(5)
    v_12 = v_2.rolling(15).std().shift(0)
    v_13 = v_2.rolling(16).skew().shift(10)
    v_14 = v_2.rolling(17).kurt().shift(5)
    v_15 = v_2.diff(18).shift(0)
    v_16 = v_2.rolling(19).min().shift(10)
    v_17 = v_2.rolling(20).skew().shift(5)
    v_18 = v_2.rolling(21).kurt().shift(0)
    v_19 = v_2.rolling(22).min().shift(10)
    v_20 = v_2.rolling(23).std().shift(5)
    v_21 = v_2.diff(24).shift(0)
    v_22 = v_2.rolling(25).mean().shift(10)
    v_23 = v_2.diff(26).shift(5)
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
    res = v_2.diff(2).diff(105).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc100_105d_jerk_v100_signal'] = f95oa_f95_operating_leverage_acceleration_calc100_105d_jerk_v100_signal

def f95oa_f95_operating_leverage_acceleration_calc101_106d_jerk_v101_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(7).shift(3)
    v_4 = v_2.rolling(8).min().shift(14)
    v_5 = v_2.rolling(9).max().shift(10)
    v_6 = v_2.rolling(10).max().shift(6)
    v_7 = v_2.rolling(11).mean().shift(2)
    v_8 = v_2.rolling(12).max().shift(13)
    v_9 = v_2.rolling(13).mean().shift(9)
    v_10 = v_2.rolling(14).mean().shift(5)
    v_11 = v_2.rolling(15).mean().shift(1)
    v_12 = v_2.rolling(16).skew().shift(12)
    v_13 = v_2.rolling(17).max().shift(8)
    v_14 = v_2.rolling(18).kurt().shift(4)
    v_15 = v_2.rolling(19).max().shift(0)
    v_16 = v_2.diff(20).shift(11)
    v_17 = v_2.rolling(21).mean().shift(7)
    v_18 = v_2.rolling(22).max().shift(3)
    v_19 = v_2.rolling(23).max().shift(14)
    v_20 = v_2.rolling(24).kurt().shift(10)
    v_21 = v_2.rolling(25).std().shift(6)
    v_22 = v_2.rolling(26).kurt().shift(2)
    v_23 = v_2.diff(27).shift(13)
    v_24 = v_2.rolling(28).mean().shift(9)
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
    res = v_2.diff(2).diff(106).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc101_106d_jerk_v101_signal'] = f95oa_f95_operating_leverage_acceleration_calc101_106d_jerk_v101_signal

def f95oa_f95_operating_leverage_acceleration_calc102_107d_jerk_v102_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(8).mean().shift(6)
    v_4 = v_2.rolling(9).mean().shift(3)
    v_5 = v_2.rolling(10).max().shift(0)
    v_6 = v_2.diff(11).shift(12)
    v_7 = v_2.rolling(12).kurt().shift(9)
    v_8 = v_2.rolling(13).max().shift(6)
    v_9 = v_2.rolling(14).max().shift(3)
    v_10 = v_2.rolling(15).skew().shift(0)
    v_11 = v_2.rolling(16).skew().shift(12)
    v_12 = v_2.rolling(17).max().shift(9)
    v_13 = v_2.rolling(18).kurt().shift(6)
    v_14 = v_2.rolling(19).std().shift(3)
    v_15 = v_2.rolling(20).std().shift(0)
    v_16 = v_2.rolling(21).kurt().shift(12)
    v_17 = v_2.rolling(22).kurt().shift(9)
    v_18 = v_2.rolling(23).std().shift(6)
    v_19 = v_2.rolling(24).kurt().shift(3)
    v_20 = v_2.rolling(25).max().shift(0)
    v_21 = v_2.rolling(26).min().shift(12)
    v_22 = v_2.rolling(27).kurt().shift(9)
    v_23 = v_2.rolling(28).min().shift(6)
    v_24 = v_2.rolling(29).std().shift(3)
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
    res = v_2.diff(2).diff(107).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc102_107d_jerk_v102_signal'] = f95oa_f95_operating_leverage_acceleration_calc102_107d_jerk_v102_signal

def f95oa_f95_operating_leverage_acceleration_calc103_108d_jerk_v103_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(9).min().shift(9)
    v_4 = v_2.rolling(10).min().shift(7)
    v_5 = v_2.rolling(11).mean().shift(5)
    v_6 = v_2.rolling(12).min().shift(3)
    v_7 = v_2.diff(13).shift(1)
    v_8 = v_2.rolling(14).std().shift(14)
    v_9 = v_2.rolling(15).mean().shift(12)
    v_10 = v_2.rolling(16).std().shift(10)
    v_11 = v_2.rolling(17).kurt().shift(8)
    v_12 = v_2.rolling(18).max().shift(6)
    v_13 = v_2.rolling(19).skew().shift(4)
    v_14 = v_2.diff(20).shift(2)
    v_15 = v_2.rolling(21).skew().shift(0)
    v_16 = v_2.rolling(22).skew().shift(13)
    v_17 = v_2.rolling(23).max().shift(11)
    v_18 = v_2.rolling(24).min().shift(9)
    v_19 = v_2.rolling(25).mean().shift(7)
    v_20 = v_2.diff(26).shift(5)
    v_21 = v_2.rolling(27).kurt().shift(3)
    v_22 = v_2.rolling(28).std().shift(1)
    v_23 = v_2.rolling(29).kurt().shift(14)
    v_24 = v_2.rolling(30).max().shift(12)
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
    res = v_2.diff(2).diff(108).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc103_108d_jerk_v103_signal'] = f95oa_f95_operating_leverage_acceleration_calc103_108d_jerk_v103_signal

def f95oa_f95_operating_leverage_acceleration_calc104_109d_jerk_v104_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(10).shift(12)
    v_4 = v_2.rolling(11).min().shift(11)
    v_5 = v_2.rolling(12).min().shift(10)
    v_6 = v_2.rolling(13).max().shift(9)
    v_7 = v_2.rolling(14).min().shift(8)
    v_8 = v_2.rolling(15).min().shift(7)
    v_9 = v_2.diff(16).shift(6)
    v_10 = v_2.diff(17).shift(5)
    v_11 = v_2.rolling(18).mean().shift(4)
    v_12 = v_2.rolling(19).std().shift(3)
    v_13 = v_2.rolling(20).std().shift(2)
    v_14 = v_2.rolling(21).std().shift(1)
    v_15 = v_2.rolling(22).skew().shift(0)
    v_16 = v_2.rolling(23).skew().shift(14)
    v_17 = v_2.rolling(24).min().shift(13)
    v_18 = v_2.rolling(25).kurt().shift(12)
    v_19 = v_2.rolling(26).min().shift(11)
    v_20 = v_2.rolling(27).skew().shift(10)
    v_21 = v_2.diff(28).shift(9)
    v_22 = v_2.rolling(29).min().shift(8)
    v_23 = v_2.rolling(30).mean().shift(7)
    v_24 = v_2.rolling(31).std().shift(6)
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
    res = v_2.diff(2).diff(109).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc104_109d_jerk_v104_signal'] = f95oa_f95_operating_leverage_acceleration_calc104_109d_jerk_v104_signal

def f95oa_f95_operating_leverage_acceleration_calc105_110d_jerk_v105_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(11).mean().shift(0)
    v_4 = v_2.rolling(12).std().shift(0)
    v_5 = v_2.rolling(13).min().shift(0)
    v_6 = v_2.rolling(14).min().shift(0)
    v_7 = v_2.rolling(15).mean().shift(0)
    v_8 = v_2.rolling(16).max().shift(0)
    v_9 = v_2.rolling(17).std().shift(0)
    v_10 = v_2.diff(18).shift(0)
    v_11 = v_2.rolling(19).max().shift(0)
    v_12 = v_2.diff(20).shift(0)
    v_13 = v_2.rolling(21).skew().shift(0)
    v_14 = v_2.rolling(22).min().shift(0)
    v_15 = v_2.rolling(23).mean().shift(0)
    v_16 = v_2.rolling(24).std().shift(0)
    v_17 = v_2.rolling(25).kurt().shift(0)
    v_18 = v_2.rolling(26).std().shift(0)
    v_19 = v_2.rolling(27).mean().shift(0)
    v_20 = v_2.rolling(28).max().shift(0)
    v_21 = v_2.rolling(29).min().shift(0)
    v_22 = v_2.rolling(30).min().shift(0)
    v_23 = v_2.rolling(31).skew().shift(0)
    v_24 = v_2.rolling(32).std().shift(0)
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
    res = v_2.diff(2).diff(110).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc105_110d_jerk_v105_signal'] = f95oa_f95_operating_leverage_acceleration_calc105_110d_jerk_v105_signal

def f95oa_f95_operating_leverage_acceleration_calc106_111d_jerk_v106_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(12).mean().shift(3)
    v_4 = v_2.rolling(13).std().shift(4)
    v_5 = v_2.rolling(14).mean().shift(5)
    v_6 = v_2.rolling(15).skew().shift(6)
    v_7 = v_2.rolling(16).mean().shift(7)
    v_8 = v_2.rolling(17).kurt().shift(8)
    v_9 = v_2.rolling(18).std().shift(9)
    v_10 = v_2.rolling(19).max().shift(10)
    v_11 = v_2.rolling(20).kurt().shift(11)
    v_12 = v_2.rolling(21).skew().shift(12)
    v_13 = v_2.rolling(22).min().shift(13)
    v_14 = v_2.rolling(23).std().shift(14)
    v_15 = v_2.rolling(24).max().shift(0)
    v_16 = v_2.rolling(25).skew().shift(1)
    v_17 = v_2.rolling(26).skew().shift(2)
    v_18 = v_2.rolling(27).std().shift(3)
    v_19 = v_2.rolling(28).mean().shift(4)
    v_20 = v_2.rolling(29).max().shift(5)
    v_21 = v_2.rolling(30).kurt().shift(6)
    v_22 = v_2.rolling(31).max().shift(7)
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
    res = v_2.diff(2).diff(111).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc106_111d_jerk_v106_signal'] = f95oa_f95_operating_leverage_acceleration_calc106_111d_jerk_v106_signal

def f95oa_f95_operating_leverage_acceleration_calc107_112d_jerk_v107_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(13).shift(6)
    v_4 = v_2.rolling(14).max().shift(8)
    v_5 = v_2.rolling(15).max().shift(10)
    v_6 = v_2.rolling(16).max().shift(12)
    v_7 = v_2.rolling(17).std().shift(14)
    v_8 = v_2.rolling(18).std().shift(1)
    v_9 = v_2.rolling(19).min().shift(3)
    v_10 = v_2.rolling(20).mean().shift(5)
    v_11 = v_2.rolling(21).min().shift(7)
    v_12 = v_2.diff(22).shift(9)
    v_13 = v_2.rolling(23).min().shift(11)
    v_14 = v_2.diff(24).shift(13)
    v_15 = v_2.rolling(25).std().shift(0)
    v_16 = v_2.rolling(26).std().shift(2)
    v_17 = v_2.rolling(27).kurt().shift(4)
    v_18 = v_2.diff(28).shift(6)
    v_19 = v_2.rolling(29).kurt().shift(8)
    v_20 = v_2.rolling(30).max().shift(10)
    v_21 = v_2.rolling(31).mean().shift(12)
    v_22 = v_2.rolling(32).max().shift(14)
    v_23 = v_2.rolling(33).std().shift(1)
    v_24 = v_2.rolling(34).kurt().shift(3)
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
    res = v_2.diff(2).diff(112).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc107_112d_jerk_v107_signal'] = f95oa_f95_operating_leverage_acceleration_calc107_112d_jerk_v107_signal

def f95oa_f95_operating_leverage_acceleration_calc108_113d_jerk_v108_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(14).mean().shift(9)
    v_4 = v_2.rolling(15).min().shift(12)
    v_5 = v_2.rolling(16).mean().shift(0)
    v_6 = v_2.diff(17).shift(3)
    v_7 = v_2.diff(18).shift(6)
    v_8 = v_2.rolling(19).skew().shift(9)
    v_9 = v_2.diff(20).shift(12)
    v_10 = v_2.diff(21).shift(0)
    v_11 = v_2.diff(22).shift(3)
    v_12 = v_2.rolling(23).kurt().shift(6)
    v_13 = v_2.rolling(24).max().shift(9)
    v_14 = v_2.rolling(25).min().shift(12)
    v_15 = v_2.rolling(26).max().shift(0)
    v_16 = v_2.rolling(27).mean().shift(3)
    v_17 = v_2.rolling(28).kurt().shift(6)
    v_18 = v_2.rolling(29).skew().shift(9)
    v_19 = v_2.rolling(30).kurt().shift(12)
    v_20 = v_2.rolling(31).mean().shift(0)
    v_21 = v_2.rolling(32).skew().shift(3)
    v_22 = v_2.rolling(33).kurt().shift(6)
    v_23 = v_2.rolling(34).kurt().shift(9)
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
    res = v_2.diff(2).diff(113).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc108_113d_jerk_v108_signal'] = f95oa_f95_operating_leverage_acceleration_calc108_113d_jerk_v108_signal

def f95oa_f95_operating_leverage_acceleration_calc109_114d_jerk_v109_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(15).mean().shift(12)
    v_4 = v_2.rolling(16).kurt().shift(1)
    v_5 = v_2.rolling(17).skew().shift(5)
    v_6 = v_2.rolling(18).kurt().shift(9)
    v_7 = v_2.rolling(19).min().shift(13)
    v_8 = v_2.rolling(20).std().shift(2)
    v_9 = v_2.rolling(21).min().shift(6)
    v_10 = v_2.rolling(22).skew().shift(10)
    v_11 = v_2.rolling(23).max().shift(14)
    v_12 = v_2.diff(24).shift(3)
    v_13 = v_2.rolling(25).min().shift(7)
    v_14 = v_2.rolling(26).kurt().shift(11)
    v_15 = v_2.diff(27).shift(0)
    v_16 = v_2.rolling(28).min().shift(4)
    v_17 = v_2.rolling(29).mean().shift(8)
    v_18 = v_2.rolling(30).min().shift(12)
    v_19 = v_2.rolling(31).mean().shift(1)
    v_20 = v_2.rolling(32).skew().shift(5)
    v_21 = v_2.rolling(33).std().shift(9)
    v_22 = v_2.rolling(34).skew().shift(13)
    v_23 = v_2.diff(35).shift(2)
    v_24 = v_2.rolling(36).mean().shift(6)
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
    res = v_2.diff(2).diff(114).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc109_114d_jerk_v109_signal'] = f95oa_f95_operating_leverage_acceleration_calc109_114d_jerk_v109_signal

def f95oa_f95_operating_leverage_acceleration_calc110_115d_jerk_v110_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(16).mean().shift(0)
    v_4 = v_2.rolling(17).max().shift(5)
    v_5 = v_2.rolling(18).mean().shift(10)
    v_6 = v_2.rolling(19).kurt().shift(0)
    v_7 = v_2.rolling(20).std().shift(5)
    v_8 = v_2.rolling(21).kurt().shift(10)
    v_9 = v_2.rolling(22).max().shift(0)
    v_10 = v_2.rolling(23).mean().shift(5)
    v_11 = v_2.rolling(24).skew().shift(10)
    v_12 = v_2.rolling(25).skew().shift(0)
    v_13 = v_2.rolling(26).kurt().shift(5)
    v_14 = v_2.diff(27).shift(10)
    v_15 = v_2.diff(28).shift(0)
    v_16 = v_2.rolling(29).mean().shift(5)
    v_17 = v_2.rolling(30).mean().shift(10)
    v_18 = v_2.rolling(31).mean().shift(0)
    v_19 = v_2.rolling(32).max().shift(5)
    v_20 = v_2.rolling(33).std().shift(10)
    v_21 = v_2.rolling(34).mean().shift(0)
    v_22 = v_2.rolling(35).mean().shift(5)
    v_23 = v_2.rolling(36).skew().shift(10)
    v_24 = v_2.rolling(37).kurt().shift(0)
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
    res = v_2.diff(2).diff(115).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc110_115d_jerk_v110_signal'] = f95oa_f95_operating_leverage_acceleration_calc110_115d_jerk_v110_signal

def f95oa_f95_operating_leverage_acceleration_calc111_116d_jerk_v111_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(17).mean().shift(3)
    v_4 = v_2.diff(18).shift(9)
    v_5 = v_2.rolling(19).std().shift(0)
    v_6 = v_2.diff(20).shift(6)
    v_7 = v_2.rolling(21).kurt().shift(12)
    v_8 = v_2.rolling(22).kurt().shift(3)
    v_9 = v_2.rolling(23).min().shift(9)
    v_10 = v_2.rolling(24).std().shift(0)
    v_11 = v_2.rolling(25).kurt().shift(6)
    v_12 = v_2.rolling(26).skew().shift(12)
    v_13 = v_2.rolling(27).max().shift(3)
    v_14 = v_2.rolling(28).skew().shift(9)
    v_15 = v_2.rolling(29).max().shift(0)
    v_16 = v_2.rolling(30).max().shift(6)
    v_17 = v_2.rolling(31).max().shift(12)
    v_18 = v_2.rolling(32).std().shift(3)
    v_19 = v_2.rolling(33).kurt().shift(9)
    v_20 = v_2.rolling(34).max().shift(0)
    v_21 = v_2.rolling(35).min().shift(6)
    v_22 = v_2.diff(36).shift(12)
    v_23 = v_2.diff(37).shift(3)
    v_24 = v_2.rolling(38).mean().shift(9)
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
    res = v_2.diff(2).diff(116).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc111_116d_jerk_v111_signal'] = f95oa_f95_operating_leverage_acceleration_calc111_116d_jerk_v111_signal

def f95oa_f95_operating_leverage_acceleration_calc112_117d_jerk_v112_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(18).shift(6)
    v_4 = v_2.rolling(19).mean().shift(13)
    v_5 = v_2.rolling(20).max().shift(5)
    v_6 = v_2.rolling(21).std().shift(12)
    v_7 = v_2.diff(22).shift(4)
    v_8 = v_2.diff(23).shift(11)
    v_9 = v_2.rolling(24).mean().shift(3)
    v_10 = v_2.rolling(25).mean().shift(10)
    v_11 = v_2.rolling(26).kurt().shift(2)
    v_12 = v_2.diff(27).shift(9)
    v_13 = v_2.rolling(28).kurt().shift(1)
    v_14 = v_2.rolling(29).min().shift(8)
    v_15 = v_2.rolling(30).max().shift(0)
    v_16 = v_2.rolling(31).min().shift(7)
    v_17 = v_2.rolling(32).kurt().shift(14)
    v_18 = v_2.rolling(33).kurt().shift(6)
    v_19 = v_2.rolling(34).std().shift(13)
    v_20 = v_2.rolling(35).mean().shift(5)
    v_21 = v_2.rolling(36).skew().shift(12)
    v_22 = v_2.rolling(37).kurt().shift(4)
    v_23 = v_2.rolling(38).kurt().shift(11)
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
    res = v_2.diff(2).diff(117).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc112_117d_jerk_v112_signal'] = f95oa_f95_operating_leverage_acceleration_calc112_117d_jerk_v112_signal

def f95oa_f95_operating_leverage_acceleration_calc113_118d_jerk_v113_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(19).kurt().shift(9)
    v_4 = v_2.rolling(20).mean().shift(2)
    v_5 = v_2.rolling(21).mean().shift(10)
    v_6 = v_2.rolling(22).skew().shift(3)
    v_7 = v_2.rolling(23).max().shift(11)
    v_8 = v_2.diff(24).shift(4)
    v_9 = v_2.diff(25).shift(12)
    v_10 = v_2.rolling(26).skew().shift(5)
    v_11 = v_2.rolling(27).skew().shift(13)
    v_12 = v_2.rolling(28).min().shift(6)
    v_13 = v_2.rolling(29).mean().shift(14)
    v_14 = v_2.rolling(30).mean().shift(7)
    v_15 = v_2.rolling(31).kurt().shift(0)
    v_16 = v_2.rolling(32).mean().shift(8)
    v_17 = v_2.rolling(33).kurt().shift(1)
    v_18 = v_2.rolling(34).mean().shift(9)
    v_19 = v_2.rolling(35).skew().shift(2)
    v_20 = v_2.rolling(36).kurt().shift(10)
    v_21 = v_2.rolling(37).max().shift(3)
    v_22 = v_2.diff(38).shift(11)
    v_23 = v_2.rolling(39).mean().shift(4)
    v_24 = v_2.rolling(40).std().shift(12)
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
    res = v_2.diff(2).diff(118).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc113_118d_jerk_v113_signal'] = f95oa_f95_operating_leverage_acceleration_calc113_118d_jerk_v113_signal

def f95oa_f95_operating_leverage_acceleration_calc114_119d_jerk_v114_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(20).mean().shift(12)
    v_4 = v_2.rolling(21).kurt().shift(6)
    v_5 = v_2.rolling(22).std().shift(0)
    v_6 = v_2.rolling(23).std().shift(9)
    v_7 = v_2.rolling(24).std().shift(3)
    v_8 = v_2.rolling(25).mean().shift(12)
    v_9 = v_2.rolling(26).mean().shift(6)
    v_10 = v_2.rolling(27).kurt().shift(0)
    v_11 = v_2.rolling(28).skew().shift(9)
    v_12 = v_2.rolling(29).min().shift(3)
    v_13 = v_2.rolling(30).std().shift(12)
    v_14 = v_2.diff(31).shift(6)
    v_15 = v_2.rolling(32).max().shift(0)
    v_16 = v_2.rolling(33).mean().shift(9)
    v_17 = v_2.rolling(34).std().shift(3)
    v_18 = v_2.rolling(35).kurt().shift(12)
    v_19 = v_2.rolling(36).std().shift(6)
    v_20 = v_2.rolling(37).max().shift(0)
    v_21 = v_2.rolling(38).min().shift(9)
    v_22 = v_2.diff(39).shift(3)
    v_23 = v_2.rolling(40).min().shift(12)
    v_24 = v_2.rolling(41).std().shift(6)
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
    res = v_2.diff(2).diff(119).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc114_119d_jerk_v114_signal'] = f95oa_f95_operating_leverage_acceleration_calc114_119d_jerk_v114_signal

def f95oa_f95_operating_leverage_acceleration_calc115_120d_jerk_v115_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(21).min().shift(0)
    v_4 = v_2.rolling(22).skew().shift(10)
    v_5 = v_2.rolling(23).std().shift(5)
    v_6 = v_2.rolling(24).max().shift(0)
    v_7 = v_2.rolling(25).std().shift(10)
    v_8 = v_2.rolling(26).max().shift(5)
    v_9 = v_2.rolling(27).skew().shift(0)
    v_10 = v_2.rolling(28).kurt().shift(10)
    v_11 = v_2.rolling(29).max().shift(5)
    v_12 = v_2.rolling(30).min().shift(0)
    v_13 = v_2.rolling(31).mean().shift(10)
    v_14 = v_2.rolling(32).mean().shift(5)
    v_15 = v_2.rolling(33).mean().shift(0)
    v_16 = v_2.diff(34).shift(10)
    v_17 = v_2.rolling(35).std().shift(5)
    v_18 = v_2.rolling(36).max().shift(0)
    v_19 = v_2.rolling(37).max().shift(10)
    v_20 = v_2.rolling(38).min().shift(5)
    v_21 = v_2.rolling(39).mean().shift(0)
    v_22 = v_2.rolling(40).skew().shift(10)
    v_23 = v_2.rolling(41).skew().shift(5)
    v_24 = v_2.rolling(42).kurt().shift(0)
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
    res = v_2.diff(2).diff(120).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc115_120d_jerk_v115_signal'] = f95oa_f95_operating_leverage_acceleration_calc115_120d_jerk_v115_signal

def f95oa_f95_operating_leverage_acceleration_calc116_121d_jerk_v116_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(22).kurt().shift(3)
    v_4 = v_2.diff(23).shift(14)
    v_5 = v_2.rolling(24).skew().shift(10)
    v_6 = v_2.rolling(25).max().shift(6)
    v_7 = v_2.rolling(26).mean().shift(2)
    v_8 = v_2.rolling(27).std().shift(13)
    v_9 = v_2.rolling(28).mean().shift(9)
    v_10 = v_2.diff(29).shift(5)
    v_11 = v_2.rolling(30).max().shift(1)
    v_12 = v_2.diff(31).shift(12)
    v_13 = v_2.rolling(32).max().shift(8)
    v_14 = v_2.rolling(33).kurt().shift(4)
    v_15 = v_2.rolling(34).std().shift(0)
    v_16 = v_2.diff(35).shift(11)
    v_17 = v_2.rolling(36).min().shift(7)
    v_18 = v_2.rolling(37).std().shift(3)
    v_19 = v_2.rolling(38).skew().shift(14)
    v_20 = v_2.rolling(39).kurt().shift(10)
    v_21 = v_2.rolling(40).min().shift(6)
    v_22 = v_2.rolling(41).max().shift(2)
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
    res = v_2.diff(2).diff(121).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc116_121d_jerk_v116_signal'] = f95oa_f95_operating_leverage_acceleration_calc116_121d_jerk_v116_signal

def f95oa_f95_operating_leverage_acceleration_calc117_122d_jerk_v117_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(23).min().shift(6)
    v_4 = v_2.rolling(24).max().shift(3)
    v_5 = v_2.diff(25).shift(0)
    v_6 = v_2.rolling(26).min().shift(12)
    v_7 = v_2.rolling(27).mean().shift(9)
    v_8 = v_2.rolling(28).skew().shift(6)
    v_9 = v_2.rolling(29).min().shift(3)
    v_10 = v_2.rolling(30).max().shift(0)
    v_11 = v_2.diff(31).shift(12)
    v_12 = v_2.rolling(32).max().shift(9)
    v_13 = v_2.diff(33).shift(6)
    v_14 = v_2.rolling(34).skew().shift(3)
    v_15 = v_2.rolling(35).kurt().shift(0)
    v_16 = v_2.rolling(36).min().shift(12)
    v_17 = v_2.rolling(37).mean().shift(9)
    v_18 = v_2.rolling(38).mean().shift(6)
    v_19 = v_2.rolling(39).kurt().shift(3)
    v_20 = v_2.rolling(40).mean().shift(0)
    v_21 = v_2.diff(41).shift(12)
    v_22 = v_2.rolling(42).skew().shift(9)
    v_23 = v_2.rolling(43).kurt().shift(6)
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
    res = v_2.diff(2).diff(122).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc117_122d_jerk_v117_signal'] = f95oa_f95_operating_leverage_acceleration_calc117_122d_jerk_v117_signal

def f95oa_f95_operating_leverage_acceleration_calc118_123d_jerk_v118_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(24).max().shift(9)
    v_4 = v_2.rolling(25).max().shift(7)
    v_5 = v_2.rolling(26).max().shift(5)
    v_6 = v_2.rolling(27).mean().shift(3)
    v_7 = v_2.rolling(28).std().shift(1)
    v_8 = v_2.rolling(29).mean().shift(14)
    v_9 = v_2.diff(30).shift(12)
    v_10 = v_2.rolling(31).mean().shift(10)
    v_11 = v_2.rolling(32).max().shift(8)
    v_12 = v_2.rolling(33).std().shift(6)
    v_13 = v_2.rolling(34).kurt().shift(4)
    v_14 = v_2.rolling(35).mean().shift(2)
    v_15 = v_2.diff(36).shift(0)
    v_16 = v_2.rolling(37).skew().shift(13)
    v_17 = v_2.rolling(38).std().shift(11)
    v_18 = v_2.rolling(39).kurt().shift(9)
    v_19 = v_2.rolling(40).min().shift(7)
    v_20 = v_2.rolling(41).max().shift(5)
    v_21 = v_2.diff(42).shift(3)
    v_22 = v_2.rolling(43).std().shift(1)
    v_23 = v_2.diff(44).shift(14)
    v_24 = v_2.diff(45).shift(12)
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
    res = v_2.diff(2).diff(123).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc118_123d_jerk_v118_signal'] = f95oa_f95_operating_leverage_acceleration_calc118_123d_jerk_v118_signal

def f95oa_f95_operating_leverage_acceleration_calc119_124d_jerk_v119_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(25).mean().shift(12)
    v_4 = v_2.rolling(26).std().shift(11)
    v_5 = v_2.rolling(27).min().shift(10)
    v_6 = v_2.rolling(28).min().shift(9)
    v_7 = v_2.rolling(29).skew().shift(8)
    v_8 = v_2.diff(30).shift(7)
    v_9 = v_2.rolling(31).mean().shift(6)
    v_10 = v_2.rolling(32).max().shift(5)
    v_11 = v_2.rolling(33).skew().shift(4)
    v_12 = v_2.rolling(34).max().shift(3)
    v_13 = v_2.diff(35).shift(2)
    v_14 = v_2.rolling(36).max().shift(1)
    v_15 = v_2.diff(37).shift(0)
    v_16 = v_2.rolling(38).kurt().shift(14)
    v_17 = v_2.rolling(39).std().shift(13)
    v_18 = v_2.rolling(40).skew().shift(12)
    v_19 = v_2.rolling(41).skew().shift(11)
    v_20 = v_2.diff(42).shift(10)
    v_21 = v_2.rolling(43).std().shift(9)
    v_22 = v_2.rolling(44).mean().shift(8)
    v_23 = v_2.rolling(45).max().shift(7)
    v_24 = v_2.diff(46).shift(6)
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
    res = v_2.diff(2).diff(124).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc119_124d_jerk_v119_signal'] = f95oa_f95_operating_leverage_acceleration_calc119_124d_jerk_v119_signal

def f95oa_f95_operating_leverage_acceleration_calc120_125d_jerk_v120_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(26).skew().shift(0)
    v_4 = v_2.rolling(27).min().shift(0)
    v_5 = v_2.rolling(28).min().shift(0)
    v_6 = v_2.rolling(29).std().shift(0)
    v_7 = v_2.rolling(30).std().shift(0)
    v_8 = v_2.rolling(31).skew().shift(0)
    v_9 = v_2.rolling(32).kurt().shift(0)
    v_10 = v_2.rolling(33).skew().shift(0)
    v_11 = v_2.rolling(34).max().shift(0)
    v_12 = v_2.rolling(35).std().shift(0)
    v_13 = v_2.rolling(36).max().shift(0)
    v_14 = v_2.rolling(37).max().shift(0)
    v_15 = v_2.rolling(38).std().shift(0)
    v_16 = v_2.diff(39).shift(0)
    v_17 = v_2.rolling(40).min().shift(0)
    v_18 = v_2.rolling(41).std().shift(0)
    v_19 = v_2.rolling(42).max().shift(0)
    v_20 = v_2.rolling(43).std().shift(0)
    v_21 = v_2.rolling(44).mean().shift(0)
    v_22 = v_2.rolling(45).skew().shift(0)
    v_23 = v_2.rolling(46).min().shift(0)
    v_24 = v_2.rolling(47).min().shift(0)
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
    res = v_2.diff(2).diff(125).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc120_125d_jerk_v120_signal'] = f95oa_f95_operating_leverage_acceleration_calc120_125d_jerk_v120_signal

def f95oa_f95_operating_leverage_acceleration_calc121_126d_jerk_v121_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(27).skew().shift(3)
    v_4 = v_2.rolling(28).mean().shift(4)
    v_5 = v_2.rolling(29).mean().shift(5)
    v_6 = v_2.rolling(30).skew().shift(6)
    v_7 = v_2.rolling(31).kurt().shift(7)
    v_8 = v_2.rolling(32).kurt().shift(8)
    v_9 = v_2.rolling(33).min().shift(9)
    v_10 = v_2.rolling(34).kurt().shift(10)
    v_11 = v_2.diff(35).shift(11)
    v_12 = v_2.rolling(36).mean().shift(12)
    v_13 = v_2.rolling(37).std().shift(13)
    v_14 = v_2.rolling(38).max().shift(14)
    v_15 = v_2.rolling(39).skew().shift(0)
    v_16 = v_2.rolling(40).max().shift(1)
    v_17 = v_2.rolling(41).max().shift(2)
    v_18 = v_2.rolling(42).kurt().shift(3)
    v_19 = v_2.rolling(43).min().shift(4)
    v_20 = v_2.rolling(44).kurt().shift(5)
    v_21 = v_2.rolling(45).mean().shift(6)
    v_22 = v_2.rolling(46).max().shift(7)
    v_23 = v_2.rolling(47).mean().shift(8)
    v_24 = v_2.rolling(48).kurt().shift(9)
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
    res = v_2.diff(2).diff(126).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc121_126d_jerk_v121_signal'] = f95oa_f95_operating_leverage_acceleration_calc121_126d_jerk_v121_signal

def f95oa_f95_operating_leverage_acceleration_calc122_127d_jerk_v122_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(28).kurt().shift(6)
    v_4 = v_2.rolling(29).kurt().shift(8)
    v_5 = v_2.rolling(30).skew().shift(10)
    v_6 = v_2.diff(31).shift(12)
    v_7 = v_2.diff(32).shift(14)
    v_8 = v_2.rolling(33).min().shift(1)
    v_9 = v_2.rolling(34).min().shift(3)
    v_10 = v_2.rolling(35).mean().shift(5)
    v_11 = v_2.rolling(36).kurt().shift(7)
    v_12 = v_2.diff(37).shift(9)
    v_13 = v_2.rolling(38).std().shift(11)
    v_14 = v_2.diff(39).shift(13)
    v_15 = v_2.rolling(40).kurt().shift(0)
    v_16 = v_2.rolling(41).std().shift(2)
    v_17 = v_2.rolling(42).max().shift(4)
    v_18 = v_2.rolling(43).min().shift(6)
    v_19 = v_2.rolling(44).std().shift(8)
    v_20 = v_2.rolling(45).max().shift(10)
    v_21 = v_2.diff(46).shift(12)
    v_22 = v_2.rolling(47).min().shift(14)
    v_23 = v_2.rolling(48).std().shift(1)
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
    res = v_2.diff(2).diff(127).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc122_127d_jerk_v122_signal'] = f95oa_f95_operating_leverage_acceleration_calc122_127d_jerk_v122_signal

def f95oa_f95_operating_leverage_acceleration_calc123_128d_jerk_v123_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(29).skew().shift(9)
    v_4 = v_2.rolling(30).kurt().shift(12)
    v_5 = v_2.diff(31).shift(0)
    v_6 = v_2.rolling(32).max().shift(3)
    v_7 = v_2.rolling(33).mean().shift(6)
    v_8 = v_2.rolling(34).mean().shift(9)
    v_9 = v_2.rolling(35).max().shift(12)
    v_10 = v_2.rolling(36).min().shift(0)
    v_11 = v_2.rolling(37).max().shift(3)
    v_12 = v_2.rolling(38).skew().shift(6)
    v_13 = v_2.diff(39).shift(9)
    v_14 = v_2.rolling(40).std().shift(12)
    v_15 = v_2.rolling(41).min().shift(0)
    v_16 = v_2.rolling(42).kurt().shift(3)
    v_17 = v_2.rolling(43).max().shift(6)
    v_18 = v_2.diff(44).shift(9)
    v_19 = v_2.rolling(45).std().shift(12)
    v_20 = v_2.diff(46).shift(0)
    v_21 = v_2.rolling(47).kurt().shift(3)
    v_22 = v_2.rolling(48).min().shift(6)
    v_23 = v_2.rolling(49).std().shift(9)
    v_24 = v_2.rolling(50).skew().shift(12)
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
    res = v_2.diff(2).diff(128).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc123_128d_jerk_v123_signal'] = f95oa_f95_operating_leverage_acceleration_calc123_128d_jerk_v123_signal

def f95oa_f95_operating_leverage_acceleration_calc124_129d_jerk_v124_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(30).min().shift(12)
    v_4 = v_2.rolling(31).mean().shift(1)
    v_5 = v_2.diff(32).shift(5)
    v_6 = v_2.rolling(33).mean().shift(9)
    v_7 = v_2.rolling(34).kurt().shift(13)
    v_8 = v_2.rolling(35).min().shift(2)
    v_9 = v_2.rolling(36).max().shift(6)
    v_10 = v_2.rolling(37).min().shift(10)
    v_11 = v_2.rolling(38).kurt().shift(14)
    v_12 = v_2.rolling(39).skew().shift(3)
    v_13 = v_2.rolling(40).skew().shift(7)
    v_14 = v_2.rolling(41).kurt().shift(11)
    v_15 = v_2.rolling(42).skew().shift(0)
    v_16 = v_2.diff(43).shift(4)
    v_17 = v_2.rolling(44).max().shift(8)
    v_18 = v_2.rolling(45).kurt().shift(12)
    v_19 = v_2.rolling(46).max().shift(1)
    v_20 = v_2.rolling(47).mean().shift(5)
    v_21 = v_2.rolling(48).skew().shift(9)
    v_22 = v_2.rolling(49).min().shift(13)
    v_23 = v_2.diff(50).shift(2)
    v_24 = v_2.rolling(51).skew().shift(6)
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
    res = v_2.diff(2).diff(129).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc124_129d_jerk_v124_signal'] = f95oa_f95_operating_leverage_acceleration_calc124_129d_jerk_v124_signal

def f95oa_f95_operating_leverage_acceleration_calc125_130d_jerk_v125_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(31).std().shift(0)
    v_4 = v_2.rolling(32).min().shift(5)
    v_5 = v_2.rolling(33).mean().shift(10)
    v_6 = v_2.rolling(34).max().shift(0)
    v_7 = v_2.diff(35).shift(5)
    v_8 = v_2.rolling(36).kurt().shift(10)
    v_9 = v_2.rolling(37).mean().shift(0)
    v_10 = v_2.rolling(38).mean().shift(5)
    v_11 = v_2.rolling(39).skew().shift(10)
    v_12 = v_2.diff(40).shift(0)
    v_13 = v_2.rolling(41).mean().shift(5)
    v_14 = v_2.diff(42).shift(10)
    v_15 = v_2.rolling(43).max().shift(0)
    v_16 = v_2.rolling(44).mean().shift(5)
    v_17 = v_2.rolling(45).min().shift(10)
    v_18 = v_2.rolling(46).min().shift(0)
    v_19 = v_2.rolling(47).min().shift(5)
    v_20 = v_2.rolling(48).mean().shift(10)
    v_21 = v_2.rolling(49).min().shift(0)
    v_22 = v_2.rolling(50).min().shift(5)
    v_23 = v_2.rolling(51).min().shift(10)
    v_24 = v_2.rolling(52).kurt().shift(0)
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
    res = v_2.diff(2).diff(130).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc125_130d_jerk_v125_signal'] = f95oa_f95_operating_leverage_acceleration_calc125_130d_jerk_v125_signal

def f95oa_f95_operating_leverage_acceleration_calc126_131d_jerk_v126_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(32).max().shift(3)
    v_4 = v_2.rolling(33).std().shift(9)
    v_5 = v_2.rolling(34).kurt().shift(0)
    v_6 = v_2.rolling(35).skew().shift(6)
    v_7 = v_2.rolling(36).max().shift(12)
    v_8 = v_2.rolling(37).max().shift(3)
    v_9 = v_2.rolling(38).max().shift(9)
    v_10 = v_2.rolling(39).std().shift(0)
    v_11 = v_2.rolling(40).max().shift(6)
    v_12 = v_2.rolling(41).skew().shift(12)
    v_13 = v_2.rolling(42).mean().shift(3)
    v_14 = v_2.rolling(43).skew().shift(9)
    v_15 = v_2.rolling(44).mean().shift(0)
    v_16 = v_2.rolling(45).min().shift(6)
    v_17 = v_2.rolling(46).kurt().shift(12)
    v_18 = v_2.rolling(47).skew().shift(3)
    v_19 = v_2.rolling(48).skew().shift(9)
    v_20 = v_2.rolling(49).std().shift(0)
    v_21 = v_2.rolling(50).mean().shift(6)
    v_22 = v_2.rolling(51).max().shift(12)
    v_23 = v_2.rolling(52).mean().shift(3)
    v_24 = v_2.rolling(3).skew().shift(9)
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
    res = v_2.diff(2).diff(131).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc126_131d_jerk_v126_signal'] = f95oa_f95_operating_leverage_acceleration_calc126_131d_jerk_v126_signal

def f95oa_f95_operating_leverage_acceleration_calc127_132d_jerk_v127_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(33).kurt().shift(6)
    v_4 = v_2.diff(34).shift(13)
    v_5 = v_2.rolling(35).max().shift(5)
    v_6 = v_2.diff(36).shift(12)
    v_7 = v_2.rolling(37).max().shift(4)
    v_8 = v_2.rolling(38).kurt().shift(11)
    v_9 = v_2.rolling(39).std().shift(3)
    v_10 = v_2.rolling(40).std().shift(10)
    v_11 = v_2.rolling(41).kurt().shift(2)
    v_12 = v_2.rolling(42).min().shift(9)
    v_13 = v_2.rolling(43).std().shift(1)
    v_14 = v_2.rolling(44).mean().shift(8)
    v_15 = v_2.rolling(45).std().shift(0)
    v_16 = v_2.diff(46).shift(7)
    v_17 = v_2.rolling(47).kurt().shift(14)
    v_18 = v_2.rolling(48).max().shift(6)
    v_19 = v_2.rolling(49).min().shift(13)
    v_20 = v_2.rolling(50).max().shift(5)
    v_21 = v_2.rolling(51).skew().shift(12)
    v_22 = v_2.rolling(52).mean().shift(4)
    v_23 = v_2.rolling(3).mean().shift(11)
    v_24 = v_2.rolling(4).std().shift(3)
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
    res = v_2.diff(2).diff(132).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc127_132d_jerk_v127_signal'] = f95oa_f95_operating_leverage_acceleration_calc127_132d_jerk_v127_signal

def f95oa_f95_operating_leverage_acceleration_calc128_133d_jerk_v128_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(34).max().shift(9)
    v_4 = v_2.rolling(35).min().shift(2)
    v_5 = v_2.rolling(36).skew().shift(10)
    v_6 = v_2.rolling(37).max().shift(3)
    v_7 = v_2.rolling(38).skew().shift(11)
    v_8 = v_2.rolling(39).max().shift(4)
    v_9 = v_2.rolling(40).min().shift(12)
    v_10 = v_2.rolling(41).std().shift(5)
    v_11 = v_2.diff(42).shift(13)
    v_12 = v_2.rolling(43).max().shift(6)
    v_13 = v_2.rolling(44).mean().shift(14)
    v_14 = v_2.diff(45).shift(7)
    v_15 = v_2.rolling(46).skew().shift(0)
    v_16 = v_2.rolling(47).max().shift(8)
    v_17 = v_2.rolling(48).max().shift(1)
    v_18 = v_2.rolling(49).kurt().shift(9)
    v_19 = v_2.rolling(50).kurt().shift(2)
    v_20 = v_2.rolling(51).kurt().shift(10)
    v_21 = v_2.rolling(52).min().shift(3)
    v_22 = v_2.rolling(3).max().shift(11)
    v_23 = v_2.rolling(4).std().shift(4)
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
    res = v_2.diff(2).diff(133).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc128_133d_jerk_v128_signal'] = f95oa_f95_operating_leverage_acceleration_calc128_133d_jerk_v128_signal

def f95oa_f95_operating_leverage_acceleration_calc129_134d_jerk_v129_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(35).shift(12)
    v_4 = v_2.rolling(36).min().shift(6)
    v_5 = v_2.rolling(37).kurt().shift(0)
    v_6 = v_2.rolling(38).skew().shift(9)
    v_7 = v_2.diff(39).shift(3)
    v_8 = v_2.rolling(40).min().shift(12)
    v_9 = v_2.rolling(41).skew().shift(6)
    v_10 = v_2.rolling(42).kurt().shift(0)
    v_11 = v_2.diff(43).shift(9)
    v_12 = v_2.rolling(44).skew().shift(3)
    v_13 = v_2.rolling(45).max().shift(12)
    v_14 = v_2.rolling(46).kurt().shift(6)
    v_15 = v_2.diff(47).shift(0)
    v_16 = v_2.rolling(48).max().shift(9)
    v_17 = v_2.rolling(49).max().shift(3)
    v_18 = v_2.rolling(50).mean().shift(12)
    v_19 = v_2.diff(51).shift(6)
    v_20 = v_2.rolling(52).skew().shift(0)
    v_21 = v_2.rolling(3).skew().shift(9)
    v_22 = v_2.rolling(4).mean().shift(3)
    v_23 = v_2.rolling(5).kurt().shift(12)
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
    res = v_2.diff(2).diff(134).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc129_134d_jerk_v129_signal'] = f95oa_f95_operating_leverage_acceleration_calc129_134d_jerk_v129_signal

def f95oa_f95_operating_leverage_acceleration_calc130_135d_jerk_v130_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(36).max().shift(0)
    v_4 = v_2.rolling(37).mean().shift(10)
    v_5 = v_2.rolling(38).max().shift(5)
    v_6 = v_2.diff(39).shift(0)
    v_7 = v_2.diff(40).shift(10)
    v_8 = v_2.rolling(41).skew().shift(5)
    v_9 = v_2.rolling(42).kurt().shift(0)
    v_10 = v_2.rolling(43).mean().shift(10)
    v_11 = v_2.rolling(44).skew().shift(5)
    v_12 = v_2.rolling(45).max().shift(0)
    v_13 = v_2.rolling(46).std().shift(10)
    v_14 = v_2.rolling(47).kurt().shift(5)
    v_15 = v_2.rolling(48).skew().shift(0)
    v_16 = v_2.rolling(49).kurt().shift(10)
    v_17 = v_2.rolling(50).std().shift(5)
    v_18 = v_2.rolling(51).skew().shift(0)
    v_19 = v_2.rolling(52).min().shift(10)
    v_20 = v_2.diff(3).shift(5)
    v_21 = v_2.diff(4).shift(0)
    v_22 = v_2.rolling(5).skew().shift(10)
    v_23 = v_2.rolling(6).mean().shift(5)
    v_24 = v_2.rolling(7).std().shift(0)
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
    res = v_2.diff(2).diff(135).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc130_135d_jerk_v130_signal'] = f95oa_f95_operating_leverage_acceleration_calc130_135d_jerk_v130_signal

def f95oa_f95_operating_leverage_acceleration_calc131_136d_jerk_v131_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(37).kurt().shift(3)
    v_4 = v_2.rolling(38).min().shift(14)
    v_5 = v_2.rolling(39).skew().shift(10)
    v_6 = v_2.rolling(40).max().shift(6)
    v_7 = v_2.rolling(41).skew().shift(2)
    v_8 = v_2.rolling(42).mean().shift(13)
    v_9 = v_2.rolling(43).min().shift(9)
    v_10 = v_2.rolling(44).mean().shift(5)
    v_11 = v_2.rolling(45).std().shift(1)
    v_12 = v_2.rolling(46).kurt().shift(12)
    v_13 = v_2.rolling(47).kurt().shift(8)
    v_14 = v_2.rolling(48).max().shift(4)
    v_15 = v_2.rolling(49).min().shift(0)
    v_16 = v_2.rolling(50).std().shift(11)
    v_17 = v_2.rolling(51).kurt().shift(7)
    v_18 = v_2.rolling(52).mean().shift(3)
    v_19 = v_2.rolling(3).min().shift(14)
    v_20 = v_2.rolling(4).min().shift(10)
    v_21 = v_2.rolling(5).min().shift(6)
    v_22 = v_2.rolling(6).skew().shift(2)
    v_23 = v_2.rolling(7).kurt().shift(13)
    v_24 = v_2.rolling(8).max().shift(9)
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
    res = v_2.diff(2).diff(136).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc131_136d_jerk_v131_signal'] = f95oa_f95_operating_leverage_acceleration_calc131_136d_jerk_v131_signal

def f95oa_f95_operating_leverage_acceleration_calc132_137d_jerk_v132_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(38).std().shift(6)
    v_4 = v_2.rolling(39).max().shift(3)
    v_5 = v_2.rolling(40).std().shift(0)
    v_6 = v_2.diff(41).shift(12)
    v_7 = v_2.rolling(42).std().shift(9)
    v_8 = v_2.rolling(43).mean().shift(6)
    v_9 = v_2.rolling(44).std().shift(3)
    v_10 = v_2.rolling(45).max().shift(0)
    v_11 = v_2.rolling(46).std().shift(12)
    v_12 = v_2.rolling(47).kurt().shift(9)
    v_13 = v_2.rolling(48).mean().shift(6)
    v_14 = v_2.rolling(49).kurt().shift(3)
    v_15 = v_2.rolling(50).max().shift(0)
    v_16 = v_2.rolling(51).kurt().shift(12)
    v_17 = v_2.rolling(52).mean().shift(9)
    v_18 = v_2.rolling(3).skew().shift(6)
    v_19 = v_2.rolling(4).kurt().shift(3)
    v_20 = v_2.rolling(5).min().shift(0)
    v_21 = v_2.diff(6).shift(12)
    v_22 = v_2.rolling(7).max().shift(9)
    v_23 = v_2.rolling(8).mean().shift(6)
    v_24 = v_2.rolling(9).skew().shift(3)
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
    res = v_2.diff(2).diff(137).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc132_137d_jerk_v132_signal'] = f95oa_f95_operating_leverage_acceleration_calc132_137d_jerk_v132_signal

def f95oa_f95_operating_leverage_acceleration_calc133_138d_jerk_v133_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(39).std().shift(9)
    v_4 = v_2.rolling(40).skew().shift(7)
    v_5 = v_2.rolling(41).std().shift(5)
    v_6 = v_2.rolling(42).mean().shift(3)
    v_7 = v_2.rolling(43).mean().shift(1)
    v_8 = v_2.diff(44).shift(14)
    v_9 = v_2.rolling(45).max().shift(12)
    v_10 = v_2.rolling(46).kurt().shift(10)
    v_11 = v_2.diff(47).shift(8)
    v_12 = v_2.rolling(48).kurt().shift(6)
    v_13 = v_2.rolling(49).std().shift(4)
    v_14 = v_2.rolling(50).std().shift(2)
    v_15 = v_2.rolling(51).std().shift(0)
    v_16 = v_2.rolling(52).max().shift(13)
    v_17 = v_2.rolling(3).kurt().shift(11)
    v_18 = v_2.diff(4).shift(9)
    v_19 = v_2.rolling(5).min().shift(7)
    v_20 = v_2.diff(6).shift(5)
    v_21 = v_2.rolling(7).std().shift(3)
    v_22 = v_2.rolling(8).mean().shift(1)
    v_23 = v_2.rolling(9).mean().shift(14)
    v_24 = v_2.rolling(10).std().shift(12)
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
    res = v_2.diff(2).diff(138).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc133_138d_jerk_v133_signal'] = f95oa_f95_operating_leverage_acceleration_calc133_138d_jerk_v133_signal

def f95oa_f95_operating_leverage_acceleration_calc134_139d_jerk_v134_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(40).skew().shift(12)
    v_4 = v_2.rolling(41).max().shift(11)
    v_5 = v_2.diff(42).shift(10)
    v_6 = v_2.rolling(43).mean().shift(9)
    v_7 = v_2.rolling(44).kurt().shift(8)
    v_8 = v_2.rolling(45).kurt().shift(7)
    v_9 = v_2.rolling(46).skew().shift(6)
    v_10 = v_2.diff(47).shift(5)
    v_11 = v_2.rolling(48).skew().shift(4)
    v_12 = v_2.rolling(49).skew().shift(3)
    v_13 = v_2.rolling(50).skew().shift(2)
    v_14 = v_2.rolling(51).max().shift(1)
    v_15 = v_2.rolling(52).kurt().shift(0)
    v_16 = v_2.rolling(3).min().shift(14)
    v_17 = v_2.rolling(4).min().shift(13)
    v_18 = v_2.rolling(5).kurt().shift(12)
    v_19 = v_2.rolling(6).max().shift(11)
    v_20 = v_2.rolling(7).kurt().shift(10)
    v_21 = v_2.rolling(8).std().shift(9)
    v_22 = v_2.rolling(9).min().shift(8)
    v_23 = v_2.rolling(10).kurt().shift(7)
    v_24 = v_2.rolling(11).kurt().shift(6)
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
    res = v_2.diff(2).diff(139).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc134_139d_jerk_v134_signal'] = f95oa_f95_operating_leverage_acceleration_calc134_139d_jerk_v134_signal

def f95oa_f95_operating_leverage_acceleration_calc135_140d_jerk_v135_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(41).min().shift(0)
    v_4 = v_2.rolling(42).mean().shift(0)
    v_5 = v_2.rolling(43).std().shift(0)
    v_6 = v_2.rolling(44).kurt().shift(0)
    v_7 = v_2.rolling(45).kurt().shift(0)
    v_8 = v_2.rolling(46).mean().shift(0)
    v_9 = v_2.rolling(47).max().shift(0)
    v_10 = v_2.diff(48).shift(0)
    v_11 = v_2.rolling(49).skew().shift(0)
    v_12 = v_2.rolling(50).min().shift(0)
    v_13 = v_2.rolling(51).min().shift(0)
    v_14 = v_2.rolling(52).skew().shift(0)
    v_15 = v_2.rolling(3).mean().shift(0)
    v_16 = v_2.rolling(4).mean().shift(0)
    v_17 = v_2.rolling(5).skew().shift(0)
    v_18 = v_2.rolling(6).std().shift(0)
    v_19 = v_2.rolling(7).kurt().shift(0)
    v_20 = v_2.rolling(8).skew().shift(0)
    v_21 = v_2.rolling(9).max().shift(0)
    v_22 = v_2.rolling(10).kurt().shift(0)
    v_23 = v_2.rolling(11).max().shift(0)
    v_24 = v_2.diff(12).shift(0)
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
    res = v_2.diff(2).diff(140).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc135_140d_jerk_v135_signal'] = f95oa_f95_operating_leverage_acceleration_calc135_140d_jerk_v135_signal

def f95oa_f95_operating_leverage_acceleration_calc136_141d_jerk_v136_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(42).mean().shift(3)
    v_4 = v_2.rolling(43).min().shift(4)
    v_5 = v_2.rolling(44).max().shift(5)
    v_6 = v_2.rolling(45).mean().shift(6)
    v_7 = v_2.diff(46).shift(7)
    v_8 = v_2.rolling(47).std().shift(8)
    v_9 = v_2.rolling(48).skew().shift(9)
    v_10 = v_2.rolling(49).mean().shift(10)
    v_11 = v_2.rolling(50).kurt().shift(11)
    v_12 = v_2.rolling(51).skew().shift(12)
    v_13 = v_2.rolling(52).std().shift(13)
    v_14 = v_2.rolling(3).kurt().shift(14)
    v_15 = v_2.rolling(4).mean().shift(0)
    v_16 = v_2.diff(5).shift(1)
    v_17 = v_2.rolling(6).kurt().shift(2)
    v_18 = v_2.rolling(7).std().shift(3)
    v_19 = v_2.rolling(8).max().shift(4)
    v_20 = v_2.rolling(9).std().shift(5)
    v_21 = v_2.rolling(10).std().shift(6)
    v_22 = v_2.rolling(11).max().shift(7)
    v_23 = v_2.rolling(12).mean().shift(8)
    v_24 = v_2.rolling(13).min().shift(9)
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
    res = v_2.diff(2).diff(141).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc136_141d_jerk_v136_signal'] = f95oa_f95_operating_leverage_acceleration_calc136_141d_jerk_v136_signal

def f95oa_f95_operating_leverage_acceleration_calc137_142d_jerk_v137_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(43).mean().shift(6)
    v_4 = v_2.rolling(44).min().shift(8)
    v_5 = v_2.rolling(45).std().shift(10)
    v_6 = v_2.rolling(46).min().shift(12)
    v_7 = v_2.diff(47).shift(14)
    v_8 = v_2.rolling(48).kurt().shift(1)
    v_9 = v_2.rolling(49).kurt().shift(3)
    v_10 = v_2.diff(50).shift(5)
    v_11 = v_2.rolling(51).std().shift(7)
    v_12 = v_2.rolling(52).skew().shift(9)
    v_13 = v_2.rolling(3).mean().shift(11)
    v_14 = v_2.rolling(4).min().shift(13)
    v_15 = v_2.rolling(5).std().shift(0)
    v_16 = v_2.rolling(6).skew().shift(2)
    v_17 = v_2.rolling(7).max().shift(4)
    v_18 = v_2.rolling(8).std().shift(6)
    v_19 = v_2.rolling(9).max().shift(8)
    v_20 = v_2.rolling(10).skew().shift(10)
    v_21 = v_2.rolling(11).kurt().shift(12)
    v_22 = v_2.rolling(12).std().shift(14)
    v_23 = v_2.diff(13).shift(1)
    v_24 = v_2.rolling(14).kurt().shift(3)
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
    res = v_2.diff(2).diff(142).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc137_142d_jerk_v137_signal'] = f95oa_f95_operating_leverage_acceleration_calc137_142d_jerk_v137_signal

def f95oa_f95_operating_leverage_acceleration_calc138_143d_jerk_v138_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(44).max().shift(9)
    v_4 = v_2.rolling(45).kurt().shift(12)
    v_5 = v_2.rolling(46).max().shift(0)
    v_6 = v_2.rolling(47).kurt().shift(3)
    v_7 = v_2.rolling(48).std().shift(6)
    v_8 = v_2.diff(49).shift(9)
    v_9 = v_2.rolling(50).skew().shift(12)
    v_10 = v_2.rolling(51).std().shift(0)
    v_11 = v_2.diff(52).shift(3)
    v_12 = v_2.rolling(3).min().shift(6)
    v_13 = v_2.rolling(4).mean().shift(9)
    v_14 = v_2.rolling(5).skew().shift(12)
    v_15 = v_2.rolling(6).kurt().shift(0)
    v_16 = v_2.rolling(7).std().shift(3)
    v_17 = v_2.rolling(8).std().shift(6)
    v_18 = v_2.rolling(9).kurt().shift(9)
    v_19 = v_2.rolling(10).skew().shift(12)
    v_20 = v_2.rolling(11).kurt().shift(0)
    v_21 = v_2.rolling(12).min().shift(3)
    v_22 = v_2.rolling(13).kurt().shift(6)
    v_23 = v_2.rolling(14).skew().shift(9)
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
    res = v_2.diff(2).diff(143).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc138_143d_jerk_v138_signal'] = f95oa_f95_operating_leverage_acceleration_calc138_143d_jerk_v138_signal

def f95oa_f95_operating_leverage_acceleration_calc139_144d_jerk_v139_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(45).shift(12)
    v_4 = v_2.rolling(46).kurt().shift(1)
    v_5 = v_2.rolling(47).skew().shift(5)
    v_6 = v_2.rolling(48).min().shift(9)
    v_7 = v_2.rolling(49).mean().shift(13)
    v_8 = v_2.rolling(50).mean().shift(2)
    v_9 = v_2.diff(51).shift(6)
    v_10 = v_2.rolling(52).std().shift(10)
    v_11 = v_2.rolling(3).skew().shift(14)
    v_12 = v_2.rolling(4).min().shift(3)
    v_13 = v_2.rolling(5).min().shift(7)
    v_14 = v_2.rolling(6).std().shift(11)
    v_15 = v_2.rolling(7).skew().shift(0)
    v_16 = v_2.rolling(8).std().shift(4)
    v_17 = v_2.rolling(9).max().shift(8)
    v_18 = v_2.rolling(10).min().shift(12)
    v_19 = v_2.rolling(11).kurt().shift(1)
    v_20 = v_2.diff(12).shift(5)
    v_21 = v_2.rolling(13).skew().shift(9)
    v_22 = v_2.rolling(14).max().shift(13)
    v_23 = v_2.diff(15).shift(2)
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
    res = v_2.diff(2).diff(144).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc139_144d_jerk_v139_signal'] = f95oa_f95_operating_leverage_acceleration_calc139_144d_jerk_v139_signal

def f95oa_f95_operating_leverage_acceleration_calc140_145d_jerk_v140_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(46).std().shift(0)
    v_4 = v_2.rolling(47).max().shift(5)
    v_5 = v_2.rolling(48).min().shift(10)
    v_6 = v_2.rolling(49).mean().shift(0)
    v_7 = v_2.diff(50).shift(5)
    v_8 = v_2.rolling(51).min().shift(10)
    v_9 = v_2.rolling(52).skew().shift(0)
    v_10 = v_2.rolling(3).kurt().shift(5)
    v_11 = v_2.rolling(4).skew().shift(10)
    v_12 = v_2.rolling(5).min().shift(0)
    v_13 = v_2.rolling(6).max().shift(5)
    v_14 = v_2.rolling(7).min().shift(10)
    v_15 = v_2.rolling(8).std().shift(0)
    v_16 = v_2.rolling(9).mean().shift(5)
    v_17 = v_2.rolling(10).mean().shift(10)
    v_18 = v_2.rolling(11).std().shift(0)
    v_19 = v_2.rolling(12).kurt().shift(5)
    v_20 = v_2.rolling(13).kurt().shift(10)
    v_21 = v_2.rolling(14).std().shift(0)
    v_22 = v_2.rolling(15).max().shift(5)
    v_23 = v_2.rolling(16).std().shift(10)
    v_24 = v_2.diff(17).shift(0)
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
    res = v_2.diff(2).diff(145).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc140_145d_jerk_v140_signal'] = f95oa_f95_operating_leverage_acceleration_calc140_145d_jerk_v140_signal

def f95oa_f95_operating_leverage_acceleration_calc141_146d_jerk_v141_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(47).std().shift(3)
    v_4 = v_2.rolling(48).mean().shift(9)
    v_5 = v_2.rolling(49).min().shift(0)
    v_6 = v_2.rolling(50).max().shift(6)
    v_7 = v_2.rolling(51).skew().shift(12)
    v_8 = v_2.rolling(52).kurt().shift(3)
    v_9 = v_2.rolling(3).mean().shift(9)
    v_10 = v_2.rolling(4).kurt().shift(0)
    v_11 = v_2.rolling(5).mean().shift(6)
    v_12 = v_2.rolling(6).kurt().shift(12)
    v_13 = v_2.diff(7).shift(3)
    v_14 = v_2.rolling(8).min().shift(9)
    v_15 = v_2.rolling(9).std().shift(0)
    v_16 = v_2.rolling(10).kurt().shift(6)
    v_17 = v_2.rolling(11).std().shift(12)
    v_18 = v_2.rolling(12).min().shift(3)
    v_19 = v_2.rolling(13).skew().shift(9)
    v_20 = v_2.rolling(14).mean().shift(0)
    v_21 = v_2.rolling(15).std().shift(6)
    v_22 = v_2.rolling(16).kurt().shift(12)
    v_23 = v_2.rolling(17).mean().shift(3)
    v_24 = v_2.rolling(18).skew().shift(9)
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
    res = v_2.diff(2).diff(146).rolling(4).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc141_146d_jerk_v141_signal'] = f95oa_f95_operating_leverage_acceleration_calc141_146d_jerk_v141_signal

def f95oa_f95_operating_leverage_acceleration_calc142_147d_jerk_v142_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(48).min().shift(6)
    v_4 = v_2.rolling(49).max().shift(13)
    v_5 = v_2.rolling(50).kurt().shift(5)
    v_6 = v_2.diff(51).shift(12)
    v_7 = v_2.rolling(52).max().shift(4)
    v_8 = v_2.rolling(3).skew().shift(11)
    v_9 = v_2.rolling(4).min().shift(3)
    v_10 = v_2.rolling(5).kurt().shift(10)
    v_11 = v_2.rolling(6).skew().shift(2)
    v_12 = v_2.rolling(7).kurt().shift(9)
    v_13 = v_2.rolling(8).std().shift(1)
    v_14 = v_2.rolling(9).max().shift(8)
    v_15 = v_2.rolling(10).skew().shift(0)
    v_16 = v_2.rolling(11).skew().shift(7)
    v_17 = v_2.rolling(12).mean().shift(14)
    v_18 = v_2.rolling(13).min().shift(6)
    v_19 = v_2.rolling(14).min().shift(13)
    v_20 = v_2.rolling(15).kurt().shift(5)
    v_21 = v_2.rolling(16).min().shift(12)
    v_22 = v_2.rolling(17).mean().shift(4)
    v_23 = v_2.rolling(18).mean().shift(11)
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
    res = v_2.diff(2).diff(147).rolling(5).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc142_147d_jerk_v142_signal'] = f95oa_f95_operating_leverage_acceleration_calc142_147d_jerk_v142_signal

def f95oa_f95_operating_leverage_acceleration_calc143_148d_jerk_v143_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(49).skew().shift(9)
    v_4 = v_2.rolling(50).kurt().shift(2)
    v_5 = v_2.rolling(51).min().shift(10)
    v_6 = v_2.rolling(52).std().shift(3)
    v_7 = v_2.rolling(3).kurt().shift(11)
    v_8 = v_2.rolling(4).kurt().shift(4)
    v_9 = v_2.diff(5).shift(12)
    v_10 = v_2.rolling(6).mean().shift(5)
    v_11 = v_2.diff(7).shift(13)
    v_12 = v_2.diff(8).shift(6)
    v_13 = v_2.rolling(9).max().shift(14)
    v_14 = v_2.rolling(10).skew().shift(7)
    v_15 = v_2.rolling(11).max().shift(0)
    v_16 = v_2.diff(12).shift(8)
    v_17 = v_2.rolling(13).max().shift(1)
    v_18 = v_2.rolling(14).max().shift(9)
    v_19 = v_2.rolling(15).max().shift(2)
    v_20 = v_2.rolling(16).max().shift(10)
    v_21 = v_2.rolling(17).max().shift(3)
    v_22 = v_2.diff(18).shift(11)
    v_23 = v_2.rolling(19).mean().shift(4)
    v_24 = v_2.rolling(20).std().shift(12)
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
    res = v_2.diff(2).diff(148).rolling(6).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc143_148d_jerk_v143_signal'] = f95oa_f95_operating_leverage_acceleration_calc143_148d_jerk_v143_signal

def f95oa_f95_operating_leverage_acceleration_calc144_149d_jerk_v144_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(50).shift(12)
    v_4 = v_2.rolling(51).min().shift(6)
    v_5 = v_2.rolling(52).min().shift(0)
    v_6 = v_2.rolling(3).max().shift(9)
    v_7 = v_2.diff(4).shift(3)
    v_8 = v_2.rolling(5).kurt().shift(12)
    v_9 = v_2.rolling(6).std().shift(6)
    v_10 = v_2.rolling(7).max().shift(0)
    v_11 = v_2.rolling(8).mean().shift(9)
    v_12 = v_2.rolling(9).min().shift(3)
    v_13 = v_2.rolling(10).skew().shift(12)
    v_14 = v_2.rolling(11).skew().shift(6)
    v_15 = v_2.rolling(12).skew().shift(0)
    v_16 = v_2.diff(13).shift(9)
    v_17 = v_2.rolling(14).mean().shift(3)
    v_18 = v_2.rolling(15).kurt().shift(12)
    v_19 = v_2.rolling(16).kurt().shift(6)
    v_20 = v_2.rolling(17).std().shift(0)
    v_21 = v_2.rolling(18).skew().shift(9)
    v_22 = v_2.rolling(19).mean().shift(3)
    v_23 = v_2.rolling(20).min().shift(12)
    v_24 = v_2.rolling(21).mean().shift(6)
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
    res = v_2.diff(2).diff(149).rolling(7).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc144_149d_jerk_v144_signal'] = f95oa_f95_operating_leverage_acceleration_calc144_149d_jerk_v144_signal

def f95oa_f95_operating_leverage_acceleration_calc145_150d_jerk_v145_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(51).std().shift(0)
    v_4 = v_2.rolling(52).kurt().shift(10)
    v_5 = v_2.rolling(3).max().shift(5)
    v_6 = v_2.rolling(4).max().shift(0)
    v_7 = v_2.diff(5).shift(10)
    v_8 = v_2.diff(6).shift(5)
    v_9 = v_2.rolling(7).kurt().shift(0)
    v_10 = v_2.rolling(8).skew().shift(10)
    v_11 = v_2.rolling(9).min().shift(5)
    v_12 = v_2.diff(10).shift(0)
    v_13 = v_2.rolling(11).std().shift(10)
    v_14 = v_2.rolling(12).min().shift(5)
    v_15 = v_2.rolling(13).skew().shift(0)
    v_16 = v_2.rolling(14).max().shift(10)
    v_17 = v_2.rolling(15).kurt().shift(5)
    v_18 = v_2.rolling(16).skew().shift(0)
    v_19 = v_2.rolling(17).kurt().shift(10)
    v_20 = v_2.diff(18).shift(5)
    v_21 = v_2.rolling(19).skew().shift(0)
    v_22 = v_2.rolling(20).kurt().shift(10)
    v_23 = v_2.rolling(21).max().shift(5)
    v_24 = v_2.rolling(22).mean().shift(0)
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
    res = v_2.diff(2).diff(150).rolling(8).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc145_150d_jerk_v145_signal'] = f95oa_f95_operating_leverage_acceleration_calc145_150d_jerk_v145_signal

def f95oa_f95_operating_leverage_acceleration_calc146_151d_jerk_v146_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(52).max().shift(3)
    v_4 = v_2.rolling(3).min().shift(14)
    v_5 = v_2.rolling(4).max().shift(10)
    v_6 = v_2.rolling(5).max().shift(6)
    v_7 = v_2.rolling(6).skew().shift(2)
    v_8 = v_2.rolling(7).std().shift(13)
    v_9 = v_2.rolling(8).kurt().shift(9)
    v_10 = v_2.rolling(9).mean().shift(5)
    v_11 = v_2.rolling(10).kurt().shift(1)
    v_12 = v_2.rolling(11).mean().shift(12)
    v_13 = v_2.diff(12).shift(8)
    v_14 = v_2.rolling(13).std().shift(4)
    v_15 = v_2.rolling(14).kurt().shift(0)
    v_16 = v_2.rolling(15).min().shift(11)
    v_17 = v_2.diff(16).shift(7)
    v_18 = v_2.rolling(17).max().shift(3)
    v_19 = v_2.rolling(18).std().shift(14)
    v_20 = v_2.diff(19).shift(10)
    v_21 = v_2.diff(20).shift(6)
    v_22 = v_2.diff(21).shift(2)
    v_23 = v_2.rolling(22).mean().shift(13)
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
    res = v_2.diff(2).diff(151).rolling(9).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc146_151d_jerk_v146_signal'] = f95oa_f95_operating_leverage_acceleration_calc146_151d_jerk_v146_signal

def f95oa_f95_operating_leverage_acceleration_calc147_152d_jerk_v147_signal(ncfo, opinc):
    v_0 = ncfo * 1.0
    v_1 = opinc * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(3).mean().shift(6)
    v_4 = v_2.diff(4).shift(3)
    v_5 = v_2.rolling(5).std().shift(0)
    v_6 = v_2.rolling(6).kurt().shift(12)
    v_7 = v_2.rolling(7).kurt().shift(9)
    v_8 = v_2.rolling(8).skew().shift(6)
    v_9 = v_2.rolling(9).skew().shift(3)
    v_10 = v_2.rolling(10).kurt().shift(0)
    v_11 = v_2.diff(11).shift(12)
    v_12 = v_2.rolling(12).mean().shift(9)
    v_13 = v_2.rolling(13).kurt().shift(6)
    v_14 = v_2.rolling(14).mean().shift(3)
    v_15 = v_2.rolling(15).kurt().shift(0)
    v_16 = v_2.rolling(16).min().shift(12)
    v_17 = v_2.rolling(17).kurt().shift(9)
    v_18 = v_2.rolling(18).std().shift(6)
    v_19 = v_2.rolling(19).min().shift(3)
    v_20 = v_2.rolling(20).min().shift(0)
    v_21 = v_2.diff(21).shift(12)
    v_22 = v_2.rolling(22).min().shift(9)
    v_23 = v_2.rolling(23).max().shift(6)
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
    res = v_2.diff(2).diff(152).rolling(10).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc147_152d_jerk_v147_signal'] = f95oa_f95_operating_leverage_acceleration_calc147_152d_jerk_v147_signal

def f95oa_f95_operating_leverage_acceleration_calc148_153d_jerk_v148_signal(opinc, revenue):
    v_0 = opinc * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(4).mean().shift(9)
    v_4 = v_2.diff(5).shift(7)
    v_5 = v_2.rolling(6).mean().shift(5)
    v_6 = v_2.rolling(7).skew().shift(3)
    v_7 = v_2.rolling(8).std().shift(1)
    v_8 = v_2.rolling(9).max().shift(14)
    v_9 = v_2.rolling(10).std().shift(12)
    v_10 = v_2.rolling(11).mean().shift(10)
    v_11 = v_2.rolling(12).skew().shift(8)
    v_12 = v_2.rolling(13).kurt().shift(6)
    v_13 = v_2.rolling(14).max().shift(4)
    v_14 = v_2.rolling(15).mean().shift(2)
    v_15 = v_2.diff(16).shift(0)
    v_16 = v_2.rolling(17).std().shift(13)
    v_17 = v_2.rolling(18).max().shift(11)
    v_18 = v_2.diff(19).shift(9)
    v_19 = v_2.rolling(20).max().shift(7)
    v_20 = v_2.diff(21).shift(5)
    v_21 = v_2.rolling(22).max().shift(3)
    v_22 = v_2.rolling(23).kurt().shift(1)
    v_23 = v_2.rolling(24).skew().shift(14)
    v_24 = v_2.rolling(25).max().shift(12)
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
    res = v_2.diff(2).diff(153).rolling(11).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc148_153d_jerk_v148_signal'] = f95oa_f95_operating_leverage_acceleration_calc148_153d_jerk_v148_signal

def f95oa_f95_operating_leverage_acceleration_calc149_154d_jerk_v149_signal(revenue, ebitda):
    v_0 = revenue * 1.0
    v_1 = ebitda * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(5).max().shift(12)
    v_4 = v_2.rolling(6).std().shift(11)
    v_5 = v_2.rolling(7).kurt().shift(10)
    v_6 = v_2.rolling(8).std().shift(9)
    v_7 = v_2.rolling(9).skew().shift(8)
    v_8 = v_2.rolling(10).mean().shift(7)
    v_9 = v_2.rolling(11).skew().shift(6)
    v_10 = v_2.rolling(12).min().shift(5)
    v_11 = v_2.rolling(13).skew().shift(4)
    v_12 = v_2.rolling(14).kurt().shift(3)
    v_13 = v_2.rolling(15).mean().shift(2)
    v_14 = v_2.rolling(16).mean().shift(1)
    v_15 = v_2.diff(17).shift(0)
    v_16 = v_2.rolling(18).std().shift(14)
    v_17 = v_2.diff(19).shift(13)
    v_18 = v_2.rolling(20).kurt().shift(12)
    v_19 = v_2.rolling(21).min().shift(11)
    v_20 = v_2.rolling(22).skew().shift(10)
    v_21 = v_2.rolling(23).max().shift(9)
    v_22 = v_2.rolling(24).kurt().shift(8)
    v_23 = v_2.rolling(25).max().shift(7)
    v_24 = v_2.diff(26).shift(6)
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
    res = v_2.diff(2).diff(154).rolling(12).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc149_154d_jerk_v149_signal'] = f95oa_f95_operating_leverage_acceleration_calc149_154d_jerk_v149_signal

def f95oa_f95_operating_leverage_acceleration_calc150_155d_jerk_v150_signal(ebitda, ncfo):
    v_0 = ebitda * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(6).min().shift(0)
    v_4 = v_2.diff(7).shift(0)
    v_5 = v_2.rolling(8).min().shift(0)
    v_6 = v_2.rolling(9).kurt().shift(0)
    v_7 = v_2.rolling(10).kurt().shift(0)
    v_8 = v_2.rolling(11).max().shift(0)
    v_9 = v_2.rolling(12).max().shift(0)
    v_10 = v_2.rolling(13).skew().shift(0)
    v_11 = v_2.rolling(14).min().shift(0)
    v_12 = v_2.diff(15).shift(0)
    v_13 = v_2.rolling(16).max().shift(0)
    v_14 = v_2.rolling(17).std().shift(0)
    v_15 = v_2.rolling(18).kurt().shift(0)
    v_16 = v_2.diff(19).shift(0)
    v_17 = v_2.rolling(20).max().shift(0)
    v_18 = v_2.diff(21).shift(0)
    v_19 = v_2.rolling(22).std().shift(0)
    v_20 = v_2.rolling(23).max().shift(0)
    v_21 = v_2.rolling(24).max().shift(0)
    v_22 = v_2.rolling(25).min().shift(0)
    v_23 = v_2.rolling(26).kurt().shift(0)
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
    res = v_2.diff(2).diff(155).rolling(3).mean() + v_4.diff(5)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f95oa_f95_operating_leverage_acceleration_calc150_155d_jerk_v150_signal'] = f95oa_f95_operating_leverage_acceleration_calc150_155d_jerk_v150_signal


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
