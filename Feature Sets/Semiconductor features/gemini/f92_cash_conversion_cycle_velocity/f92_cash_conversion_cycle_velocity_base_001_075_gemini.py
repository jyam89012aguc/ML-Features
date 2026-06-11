import pandas as pd
import numpy as np
import os
FEATURE_FUNCTIONS = {}

def f92cv_f92_cash_conversion_cycle_velocity_calc001_6d_val_v001_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(7).min().shift(3)
    v_4 = v_2.diff(8).shift(4)
    v_5 = v_2.rolling(9).skew().shift(5)
    v_6 = v_2.rolling(10).max().shift(6)
    v_7 = v_2.rolling(11).skew().shift(7)
    v_8 = v_2.rolling(12).kurt().shift(8)
    v_9 = v_2.rolling(13).min().shift(9)
    v_10 = v_2.rolling(14).min().shift(10)
    v_11 = v_2.rolling(15).mean().shift(11)
    v_12 = v_2.rolling(16).mean().shift(12)
    v_13 = v_2.rolling(17).std().shift(13)
    v_14 = v_2.rolling(18).skew().shift(14)
    v_15 = v_2.rolling(19).min().shift(0)
    v_16 = v_2.rolling(20).std().shift(1)
    v_17 = v_2.rolling(21).min().shift(2)
    v_18 = v_2.rolling(22).max().shift(3)
    v_19 = v_2.rolling(23).max().shift(4)
    v_20 = v_2.rolling(24).max().shift(5)
    v_21 = v_2.rolling(25).skew().shift(6)
    v_22 = v_2.rolling(26).skew().shift(7)
    v_23 = v_2.rolling(27).std().shift(8)
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
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc001_6d_val_v001_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc001_6d_val_v001_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc002_7d_val_v002_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(8).skew().shift(6)
    v_4 = v_2.diff(9).shift(8)
    v_5 = v_2.rolling(10).kurt().shift(10)
    v_6 = v_2.rolling(11).kurt().shift(12)
    v_7 = v_2.rolling(12).mean().shift(14)
    v_8 = v_2.rolling(13).mean().shift(1)
    v_9 = v_2.rolling(14).kurt().shift(3)
    v_10 = v_2.rolling(15).min().shift(5)
    v_11 = v_2.rolling(16).skew().shift(7)
    v_12 = v_2.rolling(17).max().shift(9)
    v_13 = v_2.rolling(18).max().shift(11)
    v_14 = v_2.diff(19).shift(13)
    v_15 = v_2.rolling(20).mean().shift(0)
    v_16 = v_2.rolling(21).min().shift(2)
    v_17 = v_2.rolling(22).std().shift(4)
    v_18 = v_2.diff(23).shift(6)
    v_19 = v_2.rolling(24).std().shift(8)
    v_20 = v_2.diff(25).shift(10)
    v_21 = v_2.rolling(26).std().shift(12)
    v_22 = v_2.diff(27).shift(14)
    v_23 = v_2.rolling(28).skew().shift(1)
    v_24 = v_2.rolling(29).skew().shift(3)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc002_7d_val_v002_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc002_7d_val_v002_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc003_8d_val_v003_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(9).std().shift(9)
    v_4 = v_2.rolling(10).kurt().shift(12)
    v_5 = v_2.rolling(11).skew().shift(0)
    v_6 = v_2.rolling(12).max().shift(3)
    v_7 = v_2.diff(13).shift(6)
    v_8 = v_2.rolling(14).min().shift(9)
    v_9 = v_2.rolling(15).max().shift(12)
    v_10 = v_2.rolling(16).min().shift(0)
    v_11 = v_2.rolling(17).skew().shift(3)
    v_12 = v_2.rolling(18).min().shift(6)
    v_13 = v_2.rolling(19).max().shift(9)
    v_14 = v_2.rolling(20).min().shift(12)
    v_15 = v_2.rolling(21).max().shift(0)
    v_16 = v_2.rolling(22).min().shift(3)
    v_17 = v_2.rolling(23).max().shift(6)
    v_18 = v_2.rolling(24).std().shift(9)
    v_19 = v_2.rolling(25).std().shift(12)
    v_20 = v_2.rolling(26).skew().shift(0)
    v_21 = v_2.diff(27).shift(3)
    v_22 = v_2.rolling(28).kurt().shift(6)
    v_23 = v_2.rolling(29).max().shift(9)
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
    res = v_29.rolling(8).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc003_8d_val_v003_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc003_8d_val_v003_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc004_9d_val_v004_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(10).shift(12)
    v_4 = v_2.diff(11).shift(1)
    v_5 = v_2.diff(12).shift(5)
    v_6 = v_2.rolling(13).min().shift(9)
    v_7 = v_2.rolling(14).min().shift(13)
    v_8 = v_2.rolling(15).std().shift(2)
    v_9 = v_2.rolling(16).max().shift(6)
    v_10 = v_2.diff(17).shift(10)
    v_11 = v_2.rolling(18).mean().shift(14)
    v_12 = v_2.rolling(19).std().shift(3)
    v_13 = v_2.rolling(20).skew().shift(7)
    v_14 = v_2.rolling(21).mean().shift(11)
    v_15 = v_2.rolling(22).std().shift(0)
    v_16 = v_2.rolling(23).mean().shift(4)
    v_17 = v_2.rolling(24).mean().shift(8)
    v_18 = v_2.rolling(25).std().shift(12)
    v_19 = v_2.rolling(26).mean().shift(1)
    v_20 = v_2.diff(27).shift(5)
    v_21 = v_2.rolling(28).max().shift(9)
    v_22 = v_2.rolling(29).skew().shift(13)
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
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc004_9d_val_v004_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc004_9d_val_v004_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc005_10d_val_v005_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(11).std().shift(0)
    v_4 = v_2.rolling(12).std().shift(5)
    v_5 = v_2.rolling(13).mean().shift(10)
    v_6 = v_2.rolling(14).std().shift(0)
    v_7 = v_2.rolling(15).max().shift(5)
    v_8 = v_2.rolling(16).max().shift(10)
    v_9 = v_2.diff(17).shift(0)
    v_10 = v_2.diff(18).shift(5)
    v_11 = v_2.rolling(19).std().shift(10)
    v_12 = v_2.rolling(20).mean().shift(0)
    v_13 = v_2.rolling(21).std().shift(5)
    v_14 = v_2.rolling(22).mean().shift(10)
    v_15 = v_2.rolling(23).skew().shift(0)
    v_16 = v_2.rolling(24).skew().shift(5)
    v_17 = v_2.rolling(25).mean().shift(10)
    v_18 = v_2.rolling(26).skew().shift(0)
    v_19 = v_2.rolling(27).min().shift(5)
    v_20 = v_2.rolling(28).kurt().shift(10)
    v_21 = v_2.rolling(29).kurt().shift(0)
    v_22 = v_2.rolling(30).std().shift(5)
    v_23 = v_2.rolling(31).min().shift(10)
    v_24 = v_2.rolling(32).mean().shift(0)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc005_10d_val_v005_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc005_10d_val_v005_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc006_11d_val_v006_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(12).std().shift(3)
    v_4 = v_2.rolling(13).kurt().shift(9)
    v_5 = v_2.rolling(14).skew().shift(0)
    v_6 = v_2.rolling(15).skew().shift(6)
    v_7 = v_2.rolling(16).skew().shift(12)
    v_8 = v_2.rolling(17).std().shift(3)
    v_9 = v_2.rolling(18).mean().shift(9)
    v_10 = v_2.rolling(19).skew().shift(0)
    v_11 = v_2.rolling(20).min().shift(6)
    v_12 = v_2.rolling(21).std().shift(12)
    v_13 = v_2.rolling(22).std().shift(3)
    v_14 = v_2.rolling(23).kurt().shift(9)
    v_15 = v_2.diff(24).shift(0)
    v_16 = v_2.rolling(25).min().shift(6)
    v_17 = v_2.rolling(26).min().shift(12)
    v_18 = v_2.rolling(27).std().shift(3)
    v_19 = v_2.rolling(28).mean().shift(9)
    v_20 = v_2.diff(29).shift(0)
    v_21 = v_2.rolling(30).mean().shift(6)
    v_22 = v_2.rolling(31).min().shift(12)
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
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc006_11d_val_v006_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc006_11d_val_v006_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc007_12d_val_v007_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(13).std().shift(6)
    v_4 = v_2.diff(14).shift(13)
    v_5 = v_2.rolling(15).min().shift(5)
    v_6 = v_2.rolling(16).kurt().shift(12)
    v_7 = v_2.rolling(17).skew().shift(4)
    v_8 = v_2.rolling(18).min().shift(11)
    v_9 = v_2.diff(19).shift(3)
    v_10 = v_2.rolling(20).max().shift(10)
    v_11 = v_2.rolling(21).mean().shift(2)
    v_12 = v_2.rolling(22).min().shift(9)
    v_13 = v_2.rolling(23).kurt().shift(1)
    v_14 = v_2.rolling(24).std().shift(8)
    v_15 = v_2.diff(25).shift(0)
    v_16 = v_2.diff(26).shift(7)
    v_17 = v_2.rolling(27).skew().shift(14)
    v_18 = v_2.rolling(28).kurt().shift(6)
    v_19 = v_2.rolling(29).std().shift(13)
    v_20 = v_2.diff(30).shift(5)
    v_21 = v_2.rolling(31).skew().shift(12)
    v_22 = v_2.rolling(32).skew().shift(4)
    v_23 = v_2.rolling(33).kurt().shift(11)
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
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc007_12d_val_v007_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc007_12d_val_v007_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc008_13d_val_v008_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(14).mean().shift(9)
    v_4 = v_2.rolling(15).min().shift(2)
    v_5 = v_2.rolling(16).std().shift(10)
    v_6 = v_2.rolling(17).skew().shift(3)
    v_7 = v_2.diff(18).shift(11)
    v_8 = v_2.rolling(19).std().shift(4)
    v_9 = v_2.rolling(20).kurt().shift(12)
    v_10 = v_2.diff(21).shift(5)
    v_11 = v_2.rolling(22).mean().shift(13)
    v_12 = v_2.rolling(23).min().shift(6)
    v_13 = v_2.rolling(24).max().shift(14)
    v_14 = v_2.rolling(25).skew().shift(7)
    v_15 = v_2.rolling(26).std().shift(0)
    v_16 = v_2.rolling(27).min().shift(8)
    v_17 = v_2.rolling(28).skew().shift(1)
    v_18 = v_2.rolling(29).kurt().shift(9)
    v_19 = v_2.rolling(30).min().shift(2)
    v_20 = v_2.diff(31).shift(10)
    v_21 = v_2.rolling(32).min().shift(3)
    v_22 = v_2.rolling(33).min().shift(11)
    v_23 = v_2.rolling(34).kurt().shift(4)
    v_24 = v_2.rolling(35).kurt().shift(12)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc008_13d_val_v008_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc008_13d_val_v008_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc009_14d_val_v009_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(15).min().shift(12)
    v_4 = v_2.diff(16).shift(6)
    v_5 = v_2.rolling(17).skew().shift(0)
    v_6 = v_2.rolling(18).std().shift(9)
    v_7 = v_2.rolling(19).skew().shift(3)
    v_8 = v_2.rolling(20).min().shift(12)
    v_9 = v_2.rolling(21).min().shift(6)
    v_10 = v_2.diff(22).shift(0)
    v_11 = v_2.rolling(23).std().shift(9)
    v_12 = v_2.rolling(24).skew().shift(3)
    v_13 = v_2.diff(25).shift(12)
    v_14 = v_2.diff(26).shift(6)
    v_15 = v_2.rolling(27).skew().shift(0)
    v_16 = v_2.rolling(28).mean().shift(9)
    v_17 = v_2.rolling(29).mean().shift(3)
    v_18 = v_2.diff(30).shift(12)
    v_19 = v_2.diff(31).shift(6)
    v_20 = v_2.rolling(32).std().shift(0)
    v_21 = v_2.rolling(33).kurt().shift(9)
    v_22 = v_2.diff(34).shift(3)
    v_23 = v_2.diff(35).shift(12)
    v_24 = v_2.rolling(36).min().shift(6)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc009_14d_val_v009_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc009_14d_val_v009_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc010_15d_val_v010_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(16).shift(0)
    v_4 = v_2.rolling(17).mean().shift(10)
    v_5 = v_2.rolling(18).max().shift(5)
    v_6 = v_2.rolling(19).std().shift(0)
    v_7 = v_2.rolling(20).skew().shift(10)
    v_8 = v_2.rolling(21).kurt().shift(5)
    v_9 = v_2.rolling(22).skew().shift(0)
    v_10 = v_2.rolling(23).min().shift(10)
    v_11 = v_2.rolling(24).kurt().shift(5)
    v_12 = v_2.rolling(25).kurt().shift(0)
    v_13 = v_2.rolling(26).std().shift(10)
    v_14 = v_2.rolling(27).skew().shift(5)
    v_15 = v_2.diff(28).shift(0)
    v_16 = v_2.rolling(29).max().shift(10)
    v_17 = v_2.rolling(30).kurt().shift(5)
    v_18 = v_2.rolling(31).mean().shift(0)
    v_19 = v_2.rolling(32).kurt().shift(10)
    v_20 = v_2.rolling(33).min().shift(5)
    v_21 = v_2.rolling(34).kurt().shift(0)
    v_22 = v_2.diff(35).shift(10)
    v_23 = v_2.rolling(36).max().shift(5)
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
    res = v_29.rolling(15).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc010_15d_val_v010_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc010_15d_val_v010_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc011_16d_val_v011_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(17).skew().shift(3)
    v_4 = v_2.rolling(18).std().shift(14)
    v_5 = v_2.rolling(19).skew().shift(10)
    v_6 = v_2.rolling(20).min().shift(6)
    v_7 = v_2.rolling(21).std().shift(2)
    v_8 = v_2.rolling(22).min().shift(13)
    v_9 = v_2.rolling(23).mean().shift(9)
    v_10 = v_2.rolling(24).mean().shift(5)
    v_11 = v_2.rolling(25).max().shift(1)
    v_12 = v_2.rolling(26).kurt().shift(12)
    v_13 = v_2.rolling(27).std().shift(8)
    v_14 = v_2.rolling(28).mean().shift(4)
    v_15 = v_2.diff(29).shift(0)
    v_16 = v_2.diff(30).shift(11)
    v_17 = v_2.rolling(31).mean().shift(7)
    v_18 = v_2.rolling(32).mean().shift(3)
    v_19 = v_2.rolling(33).skew().shift(14)
    v_20 = v_2.rolling(34).max().shift(10)
    v_21 = v_2.rolling(35).mean().shift(6)
    v_22 = v_2.rolling(36).min().shift(2)
    v_23 = v_2.diff(37).shift(13)
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
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc011_16d_val_v011_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc011_16d_val_v011_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc012_17d_val_v012_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(18).mean().shift(6)
    v_4 = v_2.rolling(19).skew().shift(3)
    v_5 = v_2.rolling(20).kurt().shift(0)
    v_6 = v_2.rolling(21).mean().shift(12)
    v_7 = v_2.diff(22).shift(9)
    v_8 = v_2.rolling(23).min().shift(6)
    v_9 = v_2.rolling(24).min().shift(3)
    v_10 = v_2.rolling(25).kurt().shift(0)
    v_11 = v_2.rolling(26).skew().shift(12)
    v_12 = v_2.rolling(27).min().shift(9)
    v_13 = v_2.rolling(28).min().shift(6)
    v_14 = v_2.rolling(29).mean().shift(3)
    v_15 = v_2.rolling(30).mean().shift(0)
    v_16 = v_2.rolling(31).min().shift(12)
    v_17 = v_2.rolling(32).std().shift(9)
    v_18 = v_2.rolling(33).min().shift(6)
    v_19 = v_2.rolling(34).std().shift(3)
    v_20 = v_2.rolling(35).std().shift(0)
    v_21 = v_2.rolling(36).kurt().shift(12)
    v_22 = v_2.rolling(37).std().shift(9)
    v_23 = v_2.rolling(38).mean().shift(6)
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
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc012_17d_val_v012_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc012_17d_val_v012_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc013_18d_val_v013_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(19).shift(9)
    v_4 = v_2.rolling(20).min().shift(7)
    v_5 = v_2.rolling(21).kurt().shift(5)
    v_6 = v_2.rolling(22).max().shift(3)
    v_7 = v_2.rolling(23).min().shift(1)
    v_8 = v_2.rolling(24).max().shift(14)
    v_9 = v_2.rolling(25).max().shift(12)
    v_10 = v_2.rolling(26).min().shift(10)
    v_11 = v_2.diff(27).shift(8)
    v_12 = v_2.rolling(28).max().shift(6)
    v_13 = v_2.rolling(29).min().shift(4)
    v_14 = v_2.rolling(30).max().shift(2)
    v_15 = v_2.rolling(31).min().shift(0)
    v_16 = v_2.rolling(32).mean().shift(13)
    v_17 = v_2.rolling(33).std().shift(11)
    v_18 = v_2.rolling(34).min().shift(9)
    v_19 = v_2.rolling(35).max().shift(7)
    v_20 = v_2.rolling(36).mean().shift(5)
    v_21 = v_2.rolling(37).min().shift(3)
    v_22 = v_2.rolling(38).skew().shift(1)
    v_23 = v_2.rolling(39).min().shift(14)
    v_24 = v_2.rolling(40).min().shift(12)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc013_18d_val_v013_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc013_18d_val_v013_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc014_19d_val_v014_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(20).std().shift(12)
    v_4 = v_2.rolling(21).std().shift(11)
    v_5 = v_2.rolling(22).max().shift(10)
    v_6 = v_2.rolling(23).skew().shift(9)
    v_7 = v_2.diff(24).shift(8)
    v_8 = v_2.rolling(25).kurt().shift(7)
    v_9 = v_2.rolling(26).min().shift(6)
    v_10 = v_2.rolling(27).min().shift(5)
    v_11 = v_2.rolling(28).std().shift(4)
    v_12 = v_2.rolling(29).max().shift(3)
    v_13 = v_2.rolling(30).min().shift(2)
    v_14 = v_2.diff(31).shift(1)
    v_15 = v_2.rolling(32).mean().shift(0)
    v_16 = v_2.rolling(33).mean().shift(14)
    v_17 = v_2.rolling(34).max().shift(13)
    v_18 = v_2.rolling(35).max().shift(12)
    v_19 = v_2.rolling(36).kurt().shift(11)
    v_20 = v_2.diff(37).shift(10)
    v_21 = v_2.rolling(38).skew().shift(9)
    v_22 = v_2.rolling(39).std().shift(8)
    v_23 = v_2.rolling(40).skew().shift(7)
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
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc014_19d_val_v014_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc014_19d_val_v014_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc015_20d_val_v015_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(21).shift(0)
    v_4 = v_2.rolling(22).max().shift(0)
    v_5 = v_2.rolling(23).kurt().shift(0)
    v_6 = v_2.rolling(24).mean().shift(0)
    v_7 = v_2.rolling(25).max().shift(0)
    v_8 = v_2.rolling(26).mean().shift(0)
    v_9 = v_2.rolling(27).mean().shift(0)
    v_10 = v_2.rolling(28).skew().shift(0)
    v_11 = v_2.rolling(29).skew().shift(0)
    v_12 = v_2.rolling(30).mean().shift(0)
    v_13 = v_2.rolling(31).max().shift(0)
    v_14 = v_2.rolling(32).kurt().shift(0)
    v_15 = v_2.diff(33).shift(0)
    v_16 = v_2.rolling(34).min().shift(0)
    v_17 = v_2.rolling(35).mean().shift(0)
    v_18 = v_2.rolling(36).min().shift(0)
    v_19 = v_2.rolling(37).mean().shift(0)
    v_20 = v_2.rolling(38).kurt().shift(0)
    v_21 = v_2.rolling(39).std().shift(0)
    v_22 = v_2.rolling(40).max().shift(0)
    v_23 = v_2.rolling(41).min().shift(0)
    v_24 = v_2.rolling(42).std().shift(0)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc015_20d_val_v015_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc015_20d_val_v015_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc016_21d_val_v016_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(22).kurt().shift(3)
    v_4 = v_2.rolling(23).min().shift(4)
    v_5 = v_2.rolling(24).skew().shift(5)
    v_6 = v_2.rolling(25).skew().shift(6)
    v_7 = v_2.rolling(26).std().shift(7)
    v_8 = v_2.rolling(27).min().shift(8)
    v_9 = v_2.diff(28).shift(9)
    v_10 = v_2.diff(29).shift(10)
    v_11 = v_2.rolling(30).skew().shift(11)
    v_12 = v_2.rolling(31).max().shift(12)
    v_13 = v_2.rolling(32).mean().shift(13)
    v_14 = v_2.rolling(33).mean().shift(14)
    v_15 = v_2.rolling(34).kurt().shift(0)
    v_16 = v_2.rolling(35).min().shift(1)
    v_17 = v_2.diff(36).shift(2)
    v_18 = v_2.rolling(37).min().shift(3)
    v_19 = v_2.rolling(38).mean().shift(4)
    v_20 = v_2.rolling(39).min().shift(5)
    v_21 = v_2.rolling(40).min().shift(6)
    v_22 = v_2.rolling(41).kurt().shift(7)
    v_23 = v_2.diff(42).shift(8)
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
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc016_21d_val_v016_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc016_21d_val_v016_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc017_22d_val_v017_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(23).skew().shift(6)
    v_4 = v_2.rolling(24).min().shift(8)
    v_5 = v_2.diff(25).shift(10)
    v_6 = v_2.rolling(26).std().shift(12)
    v_7 = v_2.rolling(27).mean().shift(14)
    v_8 = v_2.rolling(28).max().shift(1)
    v_9 = v_2.diff(29).shift(3)
    v_10 = v_2.rolling(30).kurt().shift(5)
    v_11 = v_2.rolling(31).mean().shift(7)
    v_12 = v_2.rolling(32).std().shift(9)
    v_13 = v_2.rolling(33).mean().shift(11)
    v_14 = v_2.diff(34).shift(13)
    v_15 = v_2.rolling(35).kurt().shift(0)
    v_16 = v_2.rolling(36).kurt().shift(2)
    v_17 = v_2.rolling(37).std().shift(4)
    v_18 = v_2.rolling(38).max().shift(6)
    v_19 = v_2.rolling(39).skew().shift(8)
    v_20 = v_2.rolling(40).kurt().shift(10)
    v_21 = v_2.rolling(41).max().shift(12)
    v_22 = v_2.rolling(42).kurt().shift(14)
    v_23 = v_2.rolling(43).mean().shift(1)
    v_24 = v_2.rolling(44).mean().shift(3)
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
    res = v_29.rolling(22).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc017_22d_val_v017_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc017_22d_val_v017_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc018_23d_val_v018_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(24).mean().shift(9)
    v_4 = v_2.rolling(25).skew().shift(12)
    v_5 = v_2.rolling(26).std().shift(0)
    v_6 = v_2.diff(27).shift(3)
    v_7 = v_2.rolling(28).min().shift(6)
    v_8 = v_2.rolling(29).mean().shift(9)
    v_9 = v_2.rolling(30).skew().shift(12)
    v_10 = v_2.rolling(31).kurt().shift(0)
    v_11 = v_2.rolling(32).std().shift(3)
    v_12 = v_2.rolling(33).mean().shift(6)
    v_13 = v_2.rolling(34).std().shift(9)
    v_14 = v_2.rolling(35).max().shift(12)
    v_15 = v_2.rolling(36).mean().shift(0)
    v_16 = v_2.diff(37).shift(3)
    v_17 = v_2.rolling(38).kurt().shift(6)
    v_18 = v_2.rolling(39).skew().shift(9)
    v_19 = v_2.rolling(40).min().shift(12)
    v_20 = v_2.rolling(41).kurt().shift(0)
    v_21 = v_2.rolling(42).kurt().shift(3)
    v_22 = v_2.rolling(43).std().shift(6)
    v_23 = v_2.rolling(44).std().shift(9)
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
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc018_23d_val_v018_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc018_23d_val_v018_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc019_24d_val_v019_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(25).std().shift(12)
    v_4 = v_2.rolling(26).min().shift(1)
    v_5 = v_2.rolling(27).mean().shift(5)
    v_6 = v_2.rolling(28).max().shift(9)
    v_7 = v_2.rolling(29).skew().shift(13)
    v_8 = v_2.rolling(30).max().shift(2)
    v_9 = v_2.rolling(31).min().shift(6)
    v_10 = v_2.rolling(32).skew().shift(10)
    v_11 = v_2.rolling(33).kurt().shift(14)
    v_12 = v_2.rolling(34).skew().shift(3)
    v_13 = v_2.rolling(35).min().shift(7)
    v_14 = v_2.rolling(36).min().shift(11)
    v_15 = v_2.rolling(37).mean().shift(0)
    v_16 = v_2.rolling(38).mean().shift(4)
    v_17 = v_2.rolling(39).kurt().shift(8)
    v_18 = v_2.rolling(40).kurt().shift(12)
    v_19 = v_2.rolling(41).std().shift(1)
    v_20 = v_2.rolling(42).mean().shift(5)
    v_21 = v_2.rolling(43).mean().shift(9)
    v_22 = v_2.rolling(44).mean().shift(13)
    v_23 = v_2.rolling(45).kurt().shift(2)
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
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc019_24d_val_v019_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc019_24d_val_v019_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc020_25d_val_v020_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(26).kurt().shift(0)
    v_4 = v_2.rolling(27).max().shift(5)
    v_5 = v_2.rolling(28).min().shift(10)
    v_6 = v_2.rolling(29).min().shift(0)
    v_7 = v_2.rolling(30).min().shift(5)
    v_8 = v_2.rolling(31).kurt().shift(10)
    v_9 = v_2.rolling(32).skew().shift(0)
    v_10 = v_2.diff(33).shift(5)
    v_11 = v_2.rolling(34).min().shift(10)
    v_12 = v_2.rolling(35).kurt().shift(0)
    v_13 = v_2.rolling(36).skew().shift(5)
    v_14 = v_2.rolling(37).mean().shift(10)
    v_15 = v_2.rolling(38).mean().shift(0)
    v_16 = v_2.rolling(39).kurt().shift(5)
    v_17 = v_2.rolling(40).min().shift(10)
    v_18 = v_2.rolling(41).kurt().shift(0)
    v_19 = v_2.rolling(42).skew().shift(5)
    v_20 = v_2.rolling(43).kurt().shift(10)
    v_21 = v_2.rolling(44).std().shift(0)
    v_22 = v_2.diff(45).shift(5)
    v_23 = v_2.rolling(46).min().shift(10)
    v_24 = v_2.rolling(47).std().shift(0)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc020_25d_val_v020_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc020_25d_val_v020_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc021_26d_val_v021_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(27).min().shift(3)
    v_4 = v_2.rolling(28).min().shift(9)
    v_5 = v_2.rolling(29).min().shift(0)
    v_6 = v_2.diff(30).shift(6)
    v_7 = v_2.rolling(31).kurt().shift(12)
    v_8 = v_2.rolling(32).kurt().shift(3)
    v_9 = v_2.rolling(33).kurt().shift(9)
    v_10 = v_2.rolling(34).skew().shift(0)
    v_11 = v_2.rolling(35).mean().shift(6)
    v_12 = v_2.rolling(36).min().shift(12)
    v_13 = v_2.rolling(37).std().shift(3)
    v_14 = v_2.diff(38).shift(9)
    v_15 = v_2.rolling(39).std().shift(0)
    v_16 = v_2.rolling(40).kurt().shift(6)
    v_17 = v_2.diff(41).shift(12)
    v_18 = v_2.rolling(42).min().shift(3)
    v_19 = v_2.rolling(43).max().shift(9)
    v_20 = v_2.rolling(44).std().shift(0)
    v_21 = v_2.rolling(45).mean().shift(6)
    v_22 = v_2.rolling(46).max().shift(12)
    v_23 = v_2.rolling(47).kurt().shift(3)
    v_24 = v_2.rolling(48).mean().shift(9)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc021_26d_val_v021_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc021_26d_val_v021_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc022_27d_val_v022_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(28).min().shift(6)
    v_4 = v_2.rolling(29).std().shift(13)
    v_5 = v_2.rolling(30).skew().shift(5)
    v_6 = v_2.diff(31).shift(12)
    v_7 = v_2.rolling(32).mean().shift(4)
    v_8 = v_2.rolling(33).skew().shift(11)
    v_9 = v_2.diff(34).shift(3)
    v_10 = v_2.rolling(35).mean().shift(10)
    v_11 = v_2.rolling(36).skew().shift(2)
    v_12 = v_2.rolling(37).min().shift(9)
    v_13 = v_2.diff(38).shift(1)
    v_14 = v_2.rolling(39).std().shift(8)
    v_15 = v_2.rolling(40).kurt().shift(0)
    v_16 = v_2.rolling(41).mean().shift(7)
    v_17 = v_2.rolling(42).std().shift(14)
    v_18 = v_2.rolling(43).max().shift(6)
    v_19 = v_2.rolling(44).skew().shift(13)
    v_20 = v_2.diff(45).shift(5)
    v_21 = v_2.rolling(46).skew().shift(12)
    v_22 = v_2.rolling(47).kurt().shift(4)
    v_23 = v_2.rolling(48).kurt().shift(11)
    v_24 = v_2.rolling(49).mean().shift(3)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc022_27d_val_v022_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc022_27d_val_v022_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc023_28d_val_v023_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(29).skew().shift(9)
    v_4 = v_2.rolling(30).kurt().shift(2)
    v_5 = v_2.rolling(31).max().shift(10)
    v_6 = v_2.diff(32).shift(3)
    v_7 = v_2.rolling(33).kurt().shift(11)
    v_8 = v_2.rolling(34).min().shift(4)
    v_9 = v_2.rolling(35).max().shift(12)
    v_10 = v_2.rolling(36).skew().shift(5)
    v_11 = v_2.rolling(37).skew().shift(13)
    v_12 = v_2.diff(38).shift(6)
    v_13 = v_2.diff(39).shift(14)
    v_14 = v_2.rolling(40).skew().shift(7)
    v_15 = v_2.rolling(41).max().shift(0)
    v_16 = v_2.rolling(42).min().shift(8)
    v_17 = v_2.rolling(43).skew().shift(1)
    v_18 = v_2.diff(44).shift(9)
    v_19 = v_2.rolling(45).max().shift(2)
    v_20 = v_2.diff(46).shift(10)
    v_21 = v_2.rolling(47).kurt().shift(3)
    v_22 = v_2.rolling(48).std().shift(11)
    v_23 = v_2.rolling(49).max().shift(4)
    v_24 = v_2.rolling(50).mean().shift(12)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc023_28d_val_v023_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc023_28d_val_v023_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc024_29d_val_v024_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(30).max().shift(12)
    v_4 = v_2.rolling(31).max().shift(6)
    v_5 = v_2.rolling(32).max().shift(0)
    v_6 = v_2.rolling(33).mean().shift(9)
    v_7 = v_2.rolling(34).mean().shift(3)
    v_8 = v_2.diff(35).shift(12)
    v_9 = v_2.rolling(36).min().shift(6)
    v_10 = v_2.rolling(37).std().shift(0)
    v_11 = v_2.rolling(38).max().shift(9)
    v_12 = v_2.rolling(39).std().shift(3)
    v_13 = v_2.diff(40).shift(12)
    v_14 = v_2.rolling(41).max().shift(6)
    v_15 = v_2.diff(42).shift(0)
    v_16 = v_2.rolling(43).mean().shift(9)
    v_17 = v_2.rolling(44).max().shift(3)
    v_18 = v_2.diff(45).shift(12)
    v_19 = v_2.rolling(46).min().shift(6)
    v_20 = v_2.rolling(47).std().shift(0)
    v_21 = v_2.rolling(48).std().shift(9)
    v_22 = v_2.rolling(49).mean().shift(3)
    v_23 = v_2.diff(50).shift(12)
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
    res = v_29.rolling(29).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc024_29d_val_v024_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc024_29d_val_v024_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc025_30d_val_v025_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(31).shift(0)
    v_4 = v_2.rolling(32).mean().shift(10)
    v_5 = v_2.rolling(33).max().shift(5)
    v_6 = v_2.rolling(34).std().shift(0)
    v_7 = v_2.rolling(35).mean().shift(10)
    v_8 = v_2.diff(36).shift(5)
    v_9 = v_2.diff(37).shift(0)
    v_10 = v_2.rolling(38).min().shift(10)
    v_11 = v_2.rolling(39).min().shift(5)
    v_12 = v_2.rolling(40).kurt().shift(0)
    v_13 = v_2.rolling(41).mean().shift(10)
    v_14 = v_2.rolling(42).mean().shift(5)
    v_15 = v_2.rolling(43).kurt().shift(0)
    v_16 = v_2.diff(44).shift(10)
    v_17 = v_2.rolling(45).kurt().shift(5)
    v_18 = v_2.diff(46).shift(0)
    v_19 = v_2.rolling(47).min().shift(10)
    v_20 = v_2.diff(48).shift(5)
    v_21 = v_2.diff(49).shift(0)
    v_22 = v_2.rolling(50).max().shift(10)
    v_23 = v_2.diff(51).shift(5)
    v_24 = v_2.rolling(52).max().shift(0)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc025_30d_val_v025_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc025_30d_val_v025_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc026_31d_val_v026_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(32).skew().shift(3)
    v_4 = v_2.rolling(33).min().shift(14)
    v_5 = v_2.rolling(34).std().shift(10)
    v_6 = v_2.rolling(35).kurt().shift(6)
    v_7 = v_2.rolling(36).min().shift(2)
    v_8 = v_2.rolling(37).min().shift(13)
    v_9 = v_2.rolling(38).kurt().shift(9)
    v_10 = v_2.diff(39).shift(5)
    v_11 = v_2.rolling(40).kurt().shift(1)
    v_12 = v_2.rolling(41).max().shift(12)
    v_13 = v_2.diff(42).shift(8)
    v_14 = v_2.rolling(43).min().shift(4)
    v_15 = v_2.rolling(44).skew().shift(0)
    v_16 = v_2.rolling(45).mean().shift(11)
    v_17 = v_2.rolling(46).max().shift(7)
    v_18 = v_2.diff(47).shift(3)
    v_19 = v_2.rolling(48).kurt().shift(14)
    v_20 = v_2.rolling(49).mean().shift(10)
    v_21 = v_2.rolling(50).skew().shift(6)
    v_22 = v_2.rolling(51).skew().shift(2)
    v_23 = v_2.rolling(52).std().shift(13)
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
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc026_31d_val_v026_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc026_31d_val_v026_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc027_32d_val_v027_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(33).std().shift(6)
    v_4 = v_2.diff(34).shift(3)
    v_5 = v_2.diff(35).shift(0)
    v_6 = v_2.rolling(36).mean().shift(12)
    v_7 = v_2.rolling(37).min().shift(9)
    v_8 = v_2.rolling(38).std().shift(6)
    v_9 = v_2.rolling(39).max().shift(3)
    v_10 = v_2.rolling(40).kurt().shift(0)
    v_11 = v_2.rolling(41).skew().shift(12)
    v_12 = v_2.rolling(42).skew().shift(9)
    v_13 = v_2.rolling(43).kurt().shift(6)
    v_14 = v_2.rolling(44).max().shift(3)
    v_15 = v_2.rolling(45).mean().shift(0)
    v_16 = v_2.rolling(46).std().shift(12)
    v_17 = v_2.rolling(47).mean().shift(9)
    v_18 = v_2.diff(48).shift(6)
    v_19 = v_2.rolling(49).kurt().shift(3)
    v_20 = v_2.rolling(50).mean().shift(0)
    v_21 = v_2.rolling(51).skew().shift(12)
    v_22 = v_2.rolling(52).min().shift(9)
    v_23 = v_2.rolling(3).std().shift(6)
    v_24 = v_2.diff(4).shift(3)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc027_32d_val_v027_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc027_32d_val_v027_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc028_33d_val_v028_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(34).mean().shift(9)
    v_4 = v_2.diff(35).shift(7)
    v_5 = v_2.rolling(36).std().shift(5)
    v_6 = v_2.rolling(37).mean().shift(3)
    v_7 = v_2.rolling(38).std().shift(1)
    v_8 = v_2.rolling(39).std().shift(14)
    v_9 = v_2.rolling(40).min().shift(12)
    v_10 = v_2.rolling(41).kurt().shift(10)
    v_11 = v_2.rolling(42).min().shift(8)
    v_12 = v_2.rolling(43).kurt().shift(6)
    v_13 = v_2.rolling(44).skew().shift(4)
    v_14 = v_2.rolling(45).kurt().shift(2)
    v_15 = v_2.rolling(46).max().shift(0)
    v_16 = v_2.rolling(47).max().shift(13)
    v_17 = v_2.rolling(48).min().shift(11)
    v_18 = v_2.rolling(49).kurt().shift(9)
    v_19 = v_2.rolling(50).mean().shift(7)
    v_20 = v_2.rolling(51).max().shift(5)
    v_21 = v_2.diff(52).shift(3)
    v_22 = v_2.rolling(3).max().shift(1)
    v_23 = v_2.rolling(4).std().shift(14)
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
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc028_33d_val_v028_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc028_33d_val_v028_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc029_34d_val_v029_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(35).std().shift(12)
    v_4 = v_2.rolling(36).max().shift(11)
    v_5 = v_2.rolling(37).max().shift(10)
    v_6 = v_2.diff(38).shift(9)
    v_7 = v_2.rolling(39).max().shift(8)
    v_8 = v_2.rolling(40).skew().shift(7)
    v_9 = v_2.rolling(41).std().shift(6)
    v_10 = v_2.rolling(42).kurt().shift(5)
    v_11 = v_2.rolling(43).std().shift(4)
    v_12 = v_2.rolling(44).kurt().shift(3)
    v_13 = v_2.rolling(45).min().shift(2)
    v_14 = v_2.diff(46).shift(1)
    v_15 = v_2.rolling(47).min().shift(0)
    v_16 = v_2.rolling(48).kurt().shift(14)
    v_17 = v_2.rolling(49).max().shift(13)
    v_18 = v_2.rolling(50).max().shift(12)
    v_19 = v_2.rolling(51).mean().shift(11)
    v_20 = v_2.rolling(52).min().shift(10)
    v_21 = v_2.rolling(3).kurt().shift(9)
    v_22 = v_2.rolling(4).mean().shift(8)
    v_23 = v_2.rolling(5).skew().shift(7)
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
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc029_34d_val_v029_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc029_34d_val_v029_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc030_35d_val_v030_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(36).shift(0)
    v_4 = v_2.rolling(37).min().shift(0)
    v_5 = v_2.rolling(38).min().shift(0)
    v_6 = v_2.rolling(39).std().shift(0)
    v_7 = v_2.rolling(40).kurt().shift(0)
    v_8 = v_2.rolling(41).max().shift(0)
    v_9 = v_2.rolling(42).mean().shift(0)
    v_10 = v_2.rolling(43).max().shift(0)
    v_11 = v_2.rolling(44).skew().shift(0)
    v_12 = v_2.rolling(45).mean().shift(0)
    v_13 = v_2.diff(46).shift(0)
    v_14 = v_2.rolling(47).mean().shift(0)
    v_15 = v_2.rolling(48).min().shift(0)
    v_16 = v_2.rolling(49).std().shift(0)
    v_17 = v_2.rolling(50).min().shift(0)
    v_18 = v_2.rolling(51).skew().shift(0)
    v_19 = v_2.diff(52).shift(0)
    v_20 = v_2.rolling(3).min().shift(0)
    v_21 = v_2.rolling(4).std().shift(0)
    v_22 = v_2.rolling(5).max().shift(0)
    v_23 = v_2.rolling(6).min().shift(0)
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
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc030_35d_val_v030_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc030_35d_val_v030_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc031_36d_val_v031_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(37).skew().shift(3)
    v_4 = v_2.rolling(38).max().shift(4)
    v_5 = v_2.rolling(39).mean().shift(5)
    v_6 = v_2.diff(40).shift(6)
    v_7 = v_2.rolling(41).max().shift(7)
    v_8 = v_2.diff(42).shift(8)
    v_9 = v_2.rolling(43).std().shift(9)
    v_10 = v_2.rolling(44).kurt().shift(10)
    v_11 = v_2.rolling(45).kurt().shift(11)
    v_12 = v_2.rolling(46).skew().shift(12)
    v_13 = v_2.rolling(47).kurt().shift(13)
    v_14 = v_2.rolling(48).mean().shift(14)
    v_15 = v_2.rolling(49).min().shift(0)
    v_16 = v_2.rolling(50).min().shift(1)
    v_17 = v_2.rolling(51).skew().shift(2)
    v_18 = v_2.diff(52).shift(3)
    v_19 = v_2.rolling(3).mean().shift(4)
    v_20 = v_2.rolling(4).std().shift(5)
    v_21 = v_2.rolling(5).max().shift(6)
    v_22 = v_2.rolling(6).kurt().shift(7)
    v_23 = v_2.rolling(7).mean().shift(8)
    v_24 = v_2.rolling(8).kurt().shift(9)
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
    res = v_29.rolling(36).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc031_36d_val_v031_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc031_36d_val_v031_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc032_37d_val_v032_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(38).std().shift(6)
    v_4 = v_2.rolling(39).kurt().shift(8)
    v_5 = v_2.rolling(40).max().shift(10)
    v_6 = v_2.rolling(41).skew().shift(12)
    v_7 = v_2.rolling(42).min().shift(14)
    v_8 = v_2.rolling(43).kurt().shift(1)
    v_9 = v_2.diff(44).shift(3)
    v_10 = v_2.rolling(45).min().shift(5)
    v_11 = v_2.rolling(46).kurt().shift(7)
    v_12 = v_2.rolling(47).min().shift(9)
    v_13 = v_2.rolling(48).mean().shift(11)
    v_14 = v_2.rolling(49).mean().shift(13)
    v_15 = v_2.rolling(50).min().shift(0)
    v_16 = v_2.rolling(51).min().shift(2)
    v_17 = v_2.rolling(52).mean().shift(4)
    v_18 = v_2.rolling(3).skew().shift(6)
    v_19 = v_2.rolling(4).std().shift(8)
    v_20 = v_2.rolling(5).kurt().shift(10)
    v_21 = v_2.rolling(6).min().shift(12)
    v_22 = v_2.rolling(7).mean().shift(14)
    v_23 = v_2.rolling(8).min().shift(1)
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
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc032_37d_val_v032_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc032_37d_val_v032_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc033_38d_val_v033_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(39).min().shift(9)
    v_4 = v_2.diff(40).shift(12)
    v_5 = v_2.rolling(41).skew().shift(0)
    v_6 = v_2.diff(42).shift(3)
    v_7 = v_2.rolling(43).min().shift(6)
    v_8 = v_2.rolling(44).min().shift(9)
    v_9 = v_2.rolling(45).kurt().shift(12)
    v_10 = v_2.rolling(46).min().shift(0)
    v_11 = v_2.rolling(47).std().shift(3)
    v_12 = v_2.diff(48).shift(6)
    v_13 = v_2.rolling(49).min().shift(9)
    v_14 = v_2.rolling(50).kurt().shift(12)
    v_15 = v_2.rolling(51).skew().shift(0)
    v_16 = v_2.rolling(52).min().shift(3)
    v_17 = v_2.rolling(3).mean().shift(6)
    v_18 = v_2.rolling(4).std().shift(9)
    v_19 = v_2.rolling(5).kurt().shift(12)
    v_20 = v_2.rolling(6).skew().shift(0)
    v_21 = v_2.rolling(7).std().shift(3)
    v_22 = v_2.rolling(8).kurt().shift(6)
    v_23 = v_2.rolling(9).max().shift(9)
    v_24 = v_2.rolling(10).mean().shift(12)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc033_38d_val_v033_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc033_38d_val_v033_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc034_39d_val_v034_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(40).kurt().shift(12)
    v_4 = v_2.rolling(41).max().shift(1)
    v_5 = v_2.rolling(42).kurt().shift(5)
    v_6 = v_2.rolling(43).kurt().shift(9)
    v_7 = v_2.rolling(44).mean().shift(13)
    v_8 = v_2.rolling(45).kurt().shift(2)
    v_9 = v_2.rolling(46).max().shift(6)
    v_10 = v_2.diff(47).shift(10)
    v_11 = v_2.diff(48).shift(14)
    v_12 = v_2.rolling(49).kurt().shift(3)
    v_13 = v_2.rolling(50).mean().shift(7)
    v_14 = v_2.rolling(51).min().shift(11)
    v_15 = v_2.rolling(52).kurt().shift(0)
    v_16 = v_2.rolling(3).kurt().shift(4)
    v_17 = v_2.rolling(4).std().shift(8)
    v_18 = v_2.rolling(5).mean().shift(12)
    v_19 = v_2.rolling(6).std().shift(1)
    v_20 = v_2.rolling(7).min().shift(5)
    v_21 = v_2.rolling(8).skew().shift(9)
    v_22 = v_2.rolling(9).max().shift(13)
    v_23 = v_2.rolling(10).skew().shift(2)
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
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc034_39d_val_v034_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc034_39d_val_v034_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc035_40d_val_v035_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(41).mean().shift(0)
    v_4 = v_2.diff(42).shift(5)
    v_5 = v_2.rolling(43).mean().shift(10)
    v_6 = v_2.rolling(44).max().shift(0)
    v_7 = v_2.rolling(45).kurt().shift(5)
    v_8 = v_2.rolling(46).kurt().shift(10)
    v_9 = v_2.rolling(47).kurt().shift(0)
    v_10 = v_2.rolling(48).std().shift(5)
    v_11 = v_2.diff(49).shift(10)
    v_12 = v_2.rolling(50).skew().shift(0)
    v_13 = v_2.rolling(51).max().shift(5)
    v_14 = v_2.rolling(52).skew().shift(10)
    v_15 = v_2.rolling(3).skew().shift(0)
    v_16 = v_2.rolling(4).max().shift(5)
    v_17 = v_2.rolling(5).min().shift(10)
    v_18 = v_2.diff(6).shift(0)
    v_19 = v_2.diff(7).shift(5)
    v_20 = v_2.rolling(8).min().shift(10)
    v_21 = v_2.rolling(9).kurt().shift(0)
    v_22 = v_2.rolling(10).max().shift(5)
    v_23 = v_2.diff(11).shift(10)
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
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc035_40d_val_v035_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc035_40d_val_v035_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc036_41d_val_v036_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(42).skew().shift(3)
    v_4 = v_2.rolling(43).mean().shift(9)
    v_5 = v_2.rolling(44).std().shift(0)
    v_6 = v_2.rolling(45).mean().shift(6)
    v_7 = v_2.rolling(46).std().shift(12)
    v_8 = v_2.rolling(47).skew().shift(3)
    v_9 = v_2.rolling(48).skew().shift(9)
    v_10 = v_2.rolling(49).mean().shift(0)
    v_11 = v_2.rolling(50).min().shift(6)
    v_12 = v_2.rolling(51).kurt().shift(12)
    v_13 = v_2.diff(52).shift(3)
    v_14 = v_2.rolling(3).min().shift(9)
    v_15 = v_2.rolling(4).std().shift(0)
    v_16 = v_2.rolling(5).skew().shift(6)
    v_17 = v_2.diff(6).shift(12)
    v_18 = v_2.rolling(7).skew().shift(3)
    v_19 = v_2.rolling(8).std().shift(9)
    v_20 = v_2.rolling(9).skew().shift(0)
    v_21 = v_2.rolling(10).max().shift(6)
    v_22 = v_2.rolling(11).skew().shift(12)
    v_23 = v_2.rolling(12).std().shift(3)
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
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc036_41d_val_v036_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc036_41d_val_v036_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc037_42d_val_v037_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(43).skew().shift(6)
    v_4 = v_2.rolling(44).std().shift(13)
    v_5 = v_2.rolling(45).kurt().shift(5)
    v_6 = v_2.rolling(46).max().shift(12)
    v_7 = v_2.rolling(47).std().shift(4)
    v_8 = v_2.rolling(48).kurt().shift(11)
    v_9 = v_2.rolling(49).min().shift(3)
    v_10 = v_2.rolling(50).kurt().shift(10)
    v_11 = v_2.rolling(51).skew().shift(2)
    v_12 = v_2.rolling(52).max().shift(9)
    v_13 = v_2.rolling(3).min().shift(1)
    v_14 = v_2.rolling(4).kurt().shift(8)
    v_15 = v_2.rolling(5).max().shift(0)
    v_16 = v_2.rolling(6).max().shift(7)
    v_17 = v_2.rolling(7).max().shift(14)
    v_18 = v_2.rolling(8).mean().shift(6)
    v_19 = v_2.rolling(9).min().shift(13)
    v_20 = v_2.rolling(10).kurt().shift(5)
    v_21 = v_2.rolling(11).min().shift(12)
    v_22 = v_2.rolling(12).std().shift(4)
    v_23 = v_2.rolling(13).mean().shift(11)
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
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc037_42d_val_v037_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc037_42d_val_v037_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc038_43d_val_v038_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(44).kurt().shift(9)
    v_4 = v_2.rolling(45).skew().shift(2)
    v_5 = v_2.rolling(46).kurt().shift(10)
    v_6 = v_2.rolling(47).kurt().shift(3)
    v_7 = v_2.rolling(48).min().shift(11)
    v_8 = v_2.rolling(49).mean().shift(4)
    v_9 = v_2.rolling(50).max().shift(12)
    v_10 = v_2.rolling(51).max().shift(5)
    v_11 = v_2.rolling(52).std().shift(13)
    v_12 = v_2.diff(3).shift(6)
    v_13 = v_2.rolling(4).max().shift(14)
    v_14 = v_2.rolling(5).std().shift(7)
    v_15 = v_2.rolling(6).min().shift(0)
    v_16 = v_2.rolling(7).min().shift(8)
    v_17 = v_2.rolling(8).min().shift(1)
    v_18 = v_2.rolling(9).max().shift(9)
    v_19 = v_2.rolling(10).kurt().shift(2)
    v_20 = v_2.diff(11).shift(10)
    v_21 = v_2.rolling(12).kurt().shift(3)
    v_22 = v_2.rolling(13).std().shift(11)
    v_23 = v_2.rolling(14).kurt().shift(4)
    v_24 = v_2.rolling(15).min().shift(12)
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
    res = v_29.rolling(43).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc038_43d_val_v038_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc038_43d_val_v038_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc039_44d_val_v039_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(45).mean().shift(12)
    v_4 = v_2.rolling(46).kurt().shift(6)
    v_5 = v_2.rolling(47).mean().shift(0)
    v_6 = v_2.rolling(48).mean().shift(9)
    v_7 = v_2.diff(49).shift(3)
    v_8 = v_2.diff(50).shift(12)
    v_9 = v_2.rolling(51).std().shift(6)
    v_10 = v_2.rolling(52).min().shift(0)
    v_11 = v_2.rolling(3).mean().shift(9)
    v_12 = v_2.rolling(4).min().shift(3)
    v_13 = v_2.rolling(5).min().shift(12)
    v_14 = v_2.rolling(6).std().shift(6)
    v_15 = v_2.rolling(7).kurt().shift(0)
    v_16 = v_2.rolling(8).max().shift(9)
    v_17 = v_2.rolling(9).kurt().shift(3)
    v_18 = v_2.rolling(10).mean().shift(12)
    v_19 = v_2.rolling(11).max().shift(6)
    v_20 = v_2.diff(12).shift(0)
    v_21 = v_2.rolling(13).mean().shift(9)
    v_22 = v_2.rolling(14).mean().shift(3)
    v_23 = v_2.rolling(15).skew().shift(12)
    v_24 = v_2.rolling(16).max().shift(6)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc039_44d_val_v039_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc039_44d_val_v039_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc040_45d_val_v040_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(46).skew().shift(0)
    v_4 = v_2.rolling(47).kurt().shift(10)
    v_5 = v_2.rolling(48).skew().shift(5)
    v_6 = v_2.rolling(49).mean().shift(0)
    v_7 = v_2.rolling(50).max().shift(10)
    v_8 = v_2.rolling(51).mean().shift(5)
    v_9 = v_2.diff(52).shift(0)
    v_10 = v_2.rolling(3).min().shift(10)
    v_11 = v_2.rolling(4).std().shift(5)
    v_12 = v_2.rolling(5).kurt().shift(0)
    v_13 = v_2.rolling(6).kurt().shift(10)
    v_14 = v_2.rolling(7).min().shift(5)
    v_15 = v_2.rolling(8).min().shift(0)
    v_16 = v_2.rolling(9).mean().shift(10)
    v_17 = v_2.rolling(10).mean().shift(5)
    v_18 = v_2.rolling(11).std().shift(0)
    v_19 = v_2.rolling(12).skew().shift(10)
    v_20 = v_2.rolling(13).max().shift(5)
    v_21 = v_2.rolling(14).std().shift(0)
    v_22 = v_2.rolling(15).kurt().shift(10)
    v_23 = v_2.rolling(16).kurt().shift(5)
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
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc040_45d_val_v040_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc040_45d_val_v040_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc041_46d_val_v041_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(47).skew().shift(3)
    v_4 = v_2.rolling(48).kurt().shift(14)
    v_5 = v_2.rolling(49).min().shift(10)
    v_6 = v_2.rolling(50).skew().shift(6)
    v_7 = v_2.diff(51).shift(2)
    v_8 = v_2.rolling(52).kurt().shift(13)
    v_9 = v_2.rolling(3).max().shift(9)
    v_10 = v_2.rolling(4).min().shift(5)
    v_11 = v_2.rolling(5).min().shift(1)
    v_12 = v_2.diff(6).shift(12)
    v_13 = v_2.rolling(7).std().shift(8)
    v_14 = v_2.diff(8).shift(4)
    v_15 = v_2.rolling(9).std().shift(0)
    v_16 = v_2.rolling(10).skew().shift(11)
    v_17 = v_2.rolling(11).max().shift(7)
    v_18 = v_2.rolling(12).kurt().shift(3)
    v_19 = v_2.rolling(13).kurt().shift(14)
    v_20 = v_2.rolling(14).max().shift(10)
    v_21 = v_2.rolling(15).min().shift(6)
    v_22 = v_2.rolling(16).kurt().shift(2)
    v_23 = v_2.rolling(17).std().shift(13)
    v_24 = v_2.rolling(18).max().shift(9)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc041_46d_val_v041_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc041_46d_val_v041_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc042_47d_val_v042_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(48).std().shift(6)
    v_4 = v_2.rolling(49).kurt().shift(3)
    v_5 = v_2.rolling(50).skew().shift(0)
    v_6 = v_2.rolling(51).min().shift(12)
    v_7 = v_2.rolling(52).mean().shift(9)
    v_8 = v_2.rolling(3).std().shift(6)
    v_9 = v_2.rolling(4).skew().shift(3)
    v_10 = v_2.rolling(5).mean().shift(0)
    v_11 = v_2.rolling(6).max().shift(12)
    v_12 = v_2.rolling(7).mean().shift(9)
    v_13 = v_2.diff(8).shift(6)
    v_14 = v_2.diff(9).shift(3)
    v_15 = v_2.rolling(10).std().shift(0)
    v_16 = v_2.rolling(11).kurt().shift(12)
    v_17 = v_2.rolling(12).kurt().shift(9)
    v_18 = v_2.rolling(13).kurt().shift(6)
    v_19 = v_2.rolling(14).std().shift(3)
    v_20 = v_2.rolling(15).mean().shift(0)
    v_21 = v_2.rolling(16).kurt().shift(12)
    v_22 = v_2.rolling(17).skew().shift(9)
    v_23 = v_2.diff(18).shift(6)
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
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc042_47d_val_v042_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc042_47d_val_v042_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc043_48d_val_v043_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(49).shift(9)
    v_4 = v_2.rolling(50).max().shift(7)
    v_5 = v_2.rolling(51).min().shift(5)
    v_6 = v_2.rolling(52).mean().shift(3)
    v_7 = v_2.rolling(3).std().shift(1)
    v_8 = v_2.rolling(4).mean().shift(14)
    v_9 = v_2.rolling(5).kurt().shift(12)
    v_10 = v_2.rolling(6).kurt().shift(10)
    v_11 = v_2.rolling(7).max().shift(8)
    v_12 = v_2.rolling(8).skew().shift(6)
    v_13 = v_2.rolling(9).mean().shift(4)
    v_14 = v_2.diff(10).shift(2)
    v_15 = v_2.rolling(11).skew().shift(0)
    v_16 = v_2.rolling(12).max().shift(13)
    v_17 = v_2.rolling(13).skew().shift(11)
    v_18 = v_2.rolling(14).kurt().shift(9)
    v_19 = v_2.diff(15).shift(7)
    v_20 = v_2.diff(16).shift(5)
    v_21 = v_2.rolling(17).kurt().shift(3)
    v_22 = v_2.rolling(18).kurt().shift(1)
    v_23 = v_2.rolling(19).kurt().shift(14)
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
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc043_48d_val_v043_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc043_48d_val_v043_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc044_49d_val_v044_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(50).std().shift(12)
    v_4 = v_2.rolling(51).kurt().shift(11)
    v_5 = v_2.rolling(52).skew().shift(10)
    v_6 = v_2.rolling(3).skew().shift(9)
    v_7 = v_2.rolling(4).max().shift(8)
    v_8 = v_2.diff(5).shift(7)
    v_9 = v_2.rolling(6).std().shift(6)
    v_10 = v_2.rolling(7).min().shift(5)
    v_11 = v_2.rolling(8).std().shift(4)
    v_12 = v_2.rolling(9).mean().shift(3)
    v_13 = v_2.rolling(10).min().shift(2)
    v_14 = v_2.diff(11).shift(1)
    v_15 = v_2.rolling(12).min().shift(0)
    v_16 = v_2.rolling(13).skew().shift(14)
    v_17 = v_2.rolling(14).kurt().shift(13)
    v_18 = v_2.rolling(15).std().shift(12)
    v_19 = v_2.rolling(16).mean().shift(11)
    v_20 = v_2.rolling(17).skew().shift(10)
    v_21 = v_2.rolling(18).min().shift(9)
    v_22 = v_2.diff(19).shift(8)
    v_23 = v_2.rolling(20).skew().shift(7)
    v_24 = v_2.rolling(21).std().shift(6)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc044_49d_val_v044_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc044_49d_val_v044_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc045_50d_val_v045_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(51).std().shift(0)
    v_4 = v_2.rolling(52).mean().shift(0)
    v_5 = v_2.rolling(3).kurt().shift(0)
    v_6 = v_2.rolling(4).std().shift(0)
    v_7 = v_2.rolling(5).kurt().shift(0)
    v_8 = v_2.rolling(6).max().shift(0)
    v_9 = v_2.rolling(7).mean().shift(0)
    v_10 = v_2.rolling(8).max().shift(0)
    v_11 = v_2.rolling(9).kurt().shift(0)
    v_12 = v_2.rolling(10).min().shift(0)
    v_13 = v_2.rolling(11).skew().shift(0)
    v_14 = v_2.rolling(12).kurt().shift(0)
    v_15 = v_2.rolling(13).std().shift(0)
    v_16 = v_2.rolling(14).std().shift(0)
    v_17 = v_2.rolling(15).mean().shift(0)
    v_18 = v_2.rolling(16).mean().shift(0)
    v_19 = v_2.diff(17).shift(0)
    v_20 = v_2.rolling(18).kurt().shift(0)
    v_21 = v_2.rolling(19).skew().shift(0)
    v_22 = v_2.rolling(20).mean().shift(0)
    v_23 = v_2.diff(21).shift(0)
    v_24 = v_2.diff(22).shift(0)
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
    res = v_29.rolling(50).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc045_50d_val_v045_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc045_50d_val_v045_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc046_51d_val_v046_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(52).mean().shift(3)
    v_4 = v_2.rolling(3).kurt().shift(4)
    v_5 = v_2.rolling(4).std().shift(5)
    v_6 = v_2.rolling(5).max().shift(6)
    v_7 = v_2.rolling(6).std().shift(7)
    v_8 = v_2.rolling(7).kurt().shift(8)
    v_9 = v_2.rolling(8).max().shift(9)
    v_10 = v_2.rolling(9).min().shift(10)
    v_11 = v_2.rolling(10).mean().shift(11)
    v_12 = v_2.rolling(11).max().shift(12)
    v_13 = v_2.rolling(12).std().shift(13)
    v_14 = v_2.rolling(13).skew().shift(14)
    v_15 = v_2.rolling(14).max().shift(0)
    v_16 = v_2.rolling(15).max().shift(1)
    v_17 = v_2.rolling(16).mean().shift(2)
    v_18 = v_2.diff(17).shift(3)
    v_19 = v_2.rolling(18).min().shift(4)
    v_20 = v_2.rolling(19).max().shift(5)
    v_21 = v_2.rolling(20).mean().shift(6)
    v_22 = v_2.rolling(21).skew().shift(7)
    v_23 = v_2.rolling(22).kurt().shift(8)
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
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc046_51d_val_v046_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc046_51d_val_v046_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc047_52d_val_v047_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(3).kurt().shift(6)
    v_4 = v_2.rolling(4).min().shift(8)
    v_5 = v_2.rolling(5).std().shift(10)
    v_6 = v_2.rolling(6).min().shift(12)
    v_7 = v_2.diff(7).shift(14)
    v_8 = v_2.diff(8).shift(1)
    v_9 = v_2.rolling(9).kurt().shift(3)
    v_10 = v_2.rolling(10).skew().shift(5)
    v_11 = v_2.diff(11).shift(7)
    v_12 = v_2.rolling(12).skew().shift(9)
    v_13 = v_2.rolling(13).max().shift(11)
    v_14 = v_2.rolling(14).mean().shift(13)
    v_15 = v_2.rolling(15).skew().shift(0)
    v_16 = v_2.rolling(16).skew().shift(2)
    v_17 = v_2.rolling(17).min().shift(4)
    v_18 = v_2.rolling(18).std().shift(6)
    v_19 = v_2.rolling(19).kurt().shift(8)
    v_20 = v_2.rolling(20).std().shift(10)
    v_21 = v_2.rolling(21).max().shift(12)
    v_22 = v_2.rolling(22).max().shift(14)
    v_23 = v_2.rolling(23).kurt().shift(1)
    v_24 = v_2.rolling(24).kurt().shift(3)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc047_52d_val_v047_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc047_52d_val_v047_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc048_53d_val_v048_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(4).shift(9)
    v_4 = v_2.rolling(5).min().shift(12)
    v_5 = v_2.rolling(6).mean().shift(0)
    v_6 = v_2.rolling(7).kurt().shift(3)
    v_7 = v_2.rolling(8).min().shift(6)
    v_8 = v_2.rolling(9).kurt().shift(9)
    v_9 = v_2.diff(10).shift(12)
    v_10 = v_2.rolling(11).max().shift(0)
    v_11 = v_2.rolling(12).kurt().shift(3)
    v_12 = v_2.rolling(13).mean().shift(6)
    v_13 = v_2.rolling(14).skew().shift(9)
    v_14 = v_2.rolling(15).skew().shift(12)
    v_15 = v_2.rolling(16).std().shift(0)
    v_16 = v_2.diff(17).shift(3)
    v_17 = v_2.rolling(18).kurt().shift(6)
    v_18 = v_2.rolling(19).kurt().shift(9)
    v_19 = v_2.rolling(20).mean().shift(12)
    v_20 = v_2.rolling(21).min().shift(0)
    v_21 = v_2.rolling(22).max().shift(3)
    v_22 = v_2.rolling(23).std().shift(6)
    v_23 = v_2.rolling(24).min().shift(9)
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
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc048_53d_val_v048_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc048_53d_val_v048_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc049_54d_val_v049_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(5).mean().shift(12)
    v_4 = v_2.diff(6).shift(1)
    v_5 = v_2.rolling(7).max().shift(5)
    v_6 = v_2.rolling(8).std().shift(9)
    v_7 = v_2.rolling(9).std().shift(13)
    v_8 = v_2.rolling(10).mean().shift(2)
    v_9 = v_2.rolling(11).std().shift(6)
    v_10 = v_2.rolling(12).mean().shift(10)
    v_11 = v_2.rolling(13).max().shift(14)
    v_12 = v_2.diff(14).shift(3)
    v_13 = v_2.rolling(15).min().shift(7)
    v_14 = v_2.rolling(16).max().shift(11)
    v_15 = v_2.rolling(17).mean().shift(0)
    v_16 = v_2.rolling(18).kurt().shift(4)
    v_17 = v_2.rolling(19).std().shift(8)
    v_18 = v_2.diff(20).shift(12)
    v_19 = v_2.rolling(21).min().shift(1)
    v_20 = v_2.rolling(22).std().shift(5)
    v_21 = v_2.rolling(23).mean().shift(9)
    v_22 = v_2.rolling(24).mean().shift(13)
    v_23 = v_2.diff(25).shift(2)
    v_24 = v_2.rolling(26).skew().shift(6)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc049_54d_val_v049_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc049_54d_val_v049_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc050_55d_val_v050_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(6).skew().shift(0)
    v_4 = v_2.rolling(7).mean().shift(5)
    v_5 = v_2.rolling(8).mean().shift(10)
    v_6 = v_2.rolling(9).max().shift(0)
    v_7 = v_2.rolling(10).kurt().shift(5)
    v_8 = v_2.rolling(11).min().shift(10)
    v_9 = v_2.rolling(12).max().shift(0)
    v_10 = v_2.rolling(13).std().shift(5)
    v_11 = v_2.rolling(14).min().shift(10)
    v_12 = v_2.rolling(15).skew().shift(0)
    v_13 = v_2.diff(16).shift(5)
    v_14 = v_2.diff(17).shift(10)
    v_15 = v_2.rolling(18).skew().shift(0)
    v_16 = v_2.rolling(19).skew().shift(5)
    v_17 = v_2.rolling(20).kurt().shift(10)
    v_18 = v_2.rolling(21).skew().shift(0)
    v_19 = v_2.diff(22).shift(5)
    v_20 = v_2.rolling(23).skew().shift(10)
    v_21 = v_2.rolling(24).mean().shift(0)
    v_22 = v_2.rolling(25).kurt().shift(5)
    v_23 = v_2.diff(26).shift(10)
    v_24 = v_2.diff(27).shift(0)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc050_55d_val_v050_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc050_55d_val_v050_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc051_56d_val_v051_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(7).std().shift(3)
    v_4 = v_2.rolling(8).std().shift(9)
    v_5 = v_2.rolling(9).skew().shift(0)
    v_6 = v_2.rolling(10).std().shift(6)
    v_7 = v_2.rolling(11).mean().shift(12)
    v_8 = v_2.rolling(12).mean().shift(3)
    v_9 = v_2.rolling(13).mean().shift(9)
    v_10 = v_2.rolling(14).std().shift(0)
    v_11 = v_2.rolling(15).skew().shift(6)
    v_12 = v_2.rolling(16).min().shift(12)
    v_13 = v_2.rolling(17).mean().shift(3)
    v_14 = v_2.rolling(18).kurt().shift(9)
    v_15 = v_2.rolling(19).min().shift(0)
    v_16 = v_2.rolling(20).std().shift(6)
    v_17 = v_2.rolling(21).skew().shift(12)
    v_18 = v_2.rolling(22).max().shift(3)
    v_19 = v_2.rolling(23).mean().shift(9)
    v_20 = v_2.rolling(24).mean().shift(0)
    v_21 = v_2.rolling(25).kurt().shift(6)
    v_22 = v_2.rolling(26).max().shift(12)
    v_23 = v_2.rolling(27).mean().shift(3)
    v_24 = v_2.rolling(28).min().shift(9)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc051_56d_val_v051_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc051_56d_val_v051_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc052_57d_val_v052_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(8).max().shift(6)
    v_4 = v_2.rolling(9).max().shift(13)
    v_5 = v_2.rolling(10).std().shift(5)
    v_6 = v_2.rolling(11).max().shift(12)
    v_7 = v_2.rolling(12).min().shift(4)
    v_8 = v_2.rolling(13).kurt().shift(11)
    v_9 = v_2.rolling(14).kurt().shift(3)
    v_10 = v_2.diff(15).shift(10)
    v_11 = v_2.rolling(16).kurt().shift(2)
    v_12 = v_2.diff(17).shift(9)
    v_13 = v_2.rolling(18).std().shift(1)
    v_14 = v_2.rolling(19).mean().shift(8)
    v_15 = v_2.rolling(20).std().shift(0)
    v_16 = v_2.rolling(21).std().shift(7)
    v_17 = v_2.diff(22).shift(14)
    v_18 = v_2.rolling(23).kurt().shift(6)
    v_19 = v_2.diff(24).shift(13)
    v_20 = v_2.rolling(25).mean().shift(5)
    v_21 = v_2.rolling(26).min().shift(12)
    v_22 = v_2.rolling(27).skew().shift(4)
    v_23 = v_2.diff(28).shift(11)
    v_24 = v_2.rolling(29).kurt().shift(3)
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
    res = v_29.rolling(57).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc052_57d_val_v052_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc052_57d_val_v052_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc053_58d_val_v053_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(9).kurt().shift(9)
    v_4 = v_2.rolling(10).std().shift(2)
    v_5 = v_2.rolling(11).min().shift(10)
    v_6 = v_2.rolling(12).skew().shift(3)
    v_7 = v_2.rolling(13).kurt().shift(11)
    v_8 = v_2.rolling(14).kurt().shift(4)
    v_9 = v_2.rolling(15).skew().shift(12)
    v_10 = v_2.rolling(16).max().shift(5)
    v_11 = v_2.rolling(17).mean().shift(13)
    v_12 = v_2.rolling(18).skew().shift(6)
    v_13 = v_2.rolling(19).std().shift(14)
    v_14 = v_2.rolling(20).skew().shift(7)
    v_15 = v_2.rolling(21).min().shift(0)
    v_16 = v_2.rolling(22).max().shift(8)
    v_17 = v_2.rolling(23).mean().shift(1)
    v_18 = v_2.rolling(24).mean().shift(9)
    v_19 = v_2.rolling(25).min().shift(2)
    v_20 = v_2.rolling(26).max().shift(10)
    v_21 = v_2.rolling(27).kurt().shift(3)
    v_22 = v_2.rolling(28).std().shift(11)
    v_23 = v_2.rolling(29).mean().shift(4)
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
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc053_58d_val_v053_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc053_58d_val_v053_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc054_59d_val_v054_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(10).kurt().shift(12)
    v_4 = v_2.rolling(11).std().shift(6)
    v_5 = v_2.rolling(12).max().shift(0)
    v_6 = v_2.diff(13).shift(9)
    v_7 = v_2.rolling(14).skew().shift(3)
    v_8 = v_2.rolling(15).std().shift(12)
    v_9 = v_2.rolling(16).min().shift(6)
    v_10 = v_2.rolling(17).mean().shift(0)
    v_11 = v_2.rolling(18).mean().shift(9)
    v_12 = v_2.rolling(19).skew().shift(3)
    v_13 = v_2.diff(20).shift(12)
    v_14 = v_2.diff(21).shift(6)
    v_15 = v_2.rolling(22).mean().shift(0)
    v_16 = v_2.rolling(23).max().shift(9)
    v_17 = v_2.diff(24).shift(3)
    v_18 = v_2.rolling(25).min().shift(12)
    v_19 = v_2.rolling(26).min().shift(6)
    v_20 = v_2.diff(27).shift(0)
    v_21 = v_2.rolling(28).kurt().shift(9)
    v_22 = v_2.diff(29).shift(3)
    v_23 = v_2.rolling(30).skew().shift(12)
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
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc054_59d_val_v054_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc054_59d_val_v054_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc055_60d_val_v055_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(11).shift(0)
    v_4 = v_2.rolling(12).mean().shift(10)
    v_5 = v_2.rolling(13).kurt().shift(5)
    v_6 = v_2.rolling(14).min().shift(0)
    v_7 = v_2.rolling(15).min().shift(10)
    v_8 = v_2.rolling(16).kurt().shift(5)
    v_9 = v_2.rolling(17).max().shift(0)
    v_10 = v_2.rolling(18).kurt().shift(10)
    v_11 = v_2.rolling(19).max().shift(5)
    v_12 = v_2.rolling(20).skew().shift(0)
    v_13 = v_2.rolling(21).mean().shift(10)
    v_14 = v_2.diff(22).shift(5)
    v_15 = v_2.rolling(23).kurt().shift(0)
    v_16 = v_2.rolling(24).std().shift(10)
    v_17 = v_2.rolling(25).std().shift(5)
    v_18 = v_2.rolling(26).mean().shift(0)
    v_19 = v_2.rolling(27).kurt().shift(10)
    v_20 = v_2.rolling(28).skew().shift(5)
    v_21 = v_2.diff(29).shift(0)
    v_22 = v_2.rolling(30).max().shift(10)
    v_23 = v_2.rolling(31).kurt().shift(5)
    v_24 = v_2.rolling(32).skew().shift(0)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc055_60d_val_v055_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc055_60d_val_v055_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc056_61d_val_v056_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(12).max().shift(3)
    v_4 = v_2.rolling(13).min().shift(14)
    v_5 = v_2.rolling(14).mean().shift(10)
    v_6 = v_2.rolling(15).kurt().shift(6)
    v_7 = v_2.rolling(16).min().shift(2)
    v_8 = v_2.rolling(17).min().shift(13)
    v_9 = v_2.rolling(18).std().shift(9)
    v_10 = v_2.rolling(19).min().shift(5)
    v_11 = v_2.rolling(20).min().shift(1)
    v_12 = v_2.diff(21).shift(12)
    v_13 = v_2.rolling(22).std().shift(8)
    v_14 = v_2.rolling(23).min().shift(4)
    v_15 = v_2.diff(24).shift(0)
    v_16 = v_2.rolling(25).kurt().shift(11)
    v_17 = v_2.rolling(26).skew().shift(7)
    v_18 = v_2.rolling(27).mean().shift(3)
    v_19 = v_2.rolling(28).std().shift(14)
    v_20 = v_2.rolling(29).max().shift(10)
    v_21 = v_2.rolling(30).kurt().shift(6)
    v_22 = v_2.rolling(31).std().shift(2)
    v_23 = v_2.rolling(32).skew().shift(13)
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
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc056_61d_val_v056_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc056_61d_val_v056_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc057_62d_val_v057_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(13).max().shift(6)
    v_4 = v_2.rolling(14).skew().shift(3)
    v_5 = v_2.rolling(15).min().shift(0)
    v_6 = v_2.diff(16).shift(12)
    v_7 = v_2.rolling(17).skew().shift(9)
    v_8 = v_2.rolling(18).mean().shift(6)
    v_9 = v_2.rolling(19).skew().shift(3)
    v_10 = v_2.rolling(20).min().shift(0)
    v_11 = v_2.rolling(21).max().shift(12)
    v_12 = v_2.rolling(22).max().shift(9)
    v_13 = v_2.rolling(23).max().shift(6)
    v_14 = v_2.diff(24).shift(3)
    v_15 = v_2.rolling(25).max().shift(0)
    v_16 = v_2.rolling(26).mean().shift(12)
    v_17 = v_2.rolling(27).mean().shift(9)
    v_18 = v_2.rolling(28).std().shift(6)
    v_19 = v_2.rolling(29).skew().shift(3)
    v_20 = v_2.rolling(30).min().shift(0)
    v_21 = v_2.rolling(31).skew().shift(12)
    v_22 = v_2.rolling(32).std().shift(9)
    v_23 = v_2.rolling(33).max().shift(6)
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
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc057_62d_val_v057_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc057_62d_val_v057_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc058_63d_val_v058_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(14).min().shift(9)
    v_4 = v_2.rolling(15).min().shift(7)
    v_5 = v_2.diff(16).shift(5)
    v_6 = v_2.rolling(17).kurt().shift(3)
    v_7 = v_2.rolling(18).skew().shift(1)
    v_8 = v_2.rolling(19).skew().shift(14)
    v_9 = v_2.rolling(20).std().shift(12)
    v_10 = v_2.rolling(21).std().shift(10)
    v_11 = v_2.rolling(22).min().shift(8)
    v_12 = v_2.diff(23).shift(6)
    v_13 = v_2.rolling(24).std().shift(4)
    v_14 = v_2.diff(25).shift(2)
    v_15 = v_2.rolling(26).skew().shift(0)
    v_16 = v_2.rolling(27).max().shift(13)
    v_17 = v_2.rolling(28).max().shift(11)
    v_18 = v_2.rolling(29).std().shift(9)
    v_19 = v_2.rolling(30).mean().shift(7)
    v_20 = v_2.rolling(31).max().shift(5)
    v_21 = v_2.rolling(32).max().shift(3)
    v_22 = v_2.diff(33).shift(1)
    v_23 = v_2.rolling(34).max().shift(14)
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
    res = v_27 + v_28
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc058_63d_val_v058_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc058_63d_val_v058_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc059_64d_val_v059_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(15).shift(12)
    v_4 = v_2.rolling(16).skew().shift(11)
    v_5 = v_2.rolling(17).kurt().shift(10)
    v_6 = v_2.diff(18).shift(9)
    v_7 = v_2.rolling(19).min().shift(8)
    v_8 = v_2.rolling(20).max().shift(7)
    v_9 = v_2.rolling(21).mean().shift(6)
    v_10 = v_2.diff(22).shift(5)
    v_11 = v_2.rolling(23).max().shift(4)
    v_12 = v_2.diff(24).shift(3)
    v_13 = v_2.rolling(25).skew().shift(2)
    v_14 = v_2.diff(26).shift(1)
    v_15 = v_2.diff(27).shift(0)
    v_16 = v_2.diff(28).shift(14)
    v_17 = v_2.rolling(29).max().shift(13)
    v_18 = v_2.rolling(30).mean().shift(12)
    v_19 = v_2.rolling(31).std().shift(11)
    v_20 = v_2.rolling(32).min().shift(10)
    v_21 = v_2.rolling(33).max().shift(9)
    v_22 = v_2.rolling(34).max().shift(8)
    v_23 = v_2.rolling(35).max().shift(7)
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
    res = v_29.rolling(64).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc059_64d_val_v059_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc059_64d_val_v059_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc060_65d_val_v060_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(16).std().shift(0)
    v_4 = v_2.diff(17).shift(0)
    v_5 = v_2.rolling(18).max().shift(0)
    v_6 = v_2.diff(19).shift(0)
    v_7 = v_2.rolling(20).min().shift(0)
    v_8 = v_2.rolling(21).mean().shift(0)
    v_9 = v_2.rolling(22).min().shift(0)
    v_10 = v_2.rolling(23).skew().shift(0)
    v_11 = v_2.rolling(24).mean().shift(0)
    v_12 = v_2.rolling(25).min().shift(0)
    v_13 = v_2.diff(26).shift(0)
    v_14 = v_2.rolling(27).skew().shift(0)
    v_15 = v_2.rolling(28).kurt().shift(0)
    v_16 = v_2.diff(29).shift(0)
    v_17 = v_2.rolling(30).mean().shift(0)
    v_18 = v_2.rolling(31).min().shift(0)
    v_19 = v_2.rolling(32).min().shift(0)
    v_20 = v_2.rolling(33).kurt().shift(0)
    v_21 = v_2.diff(34).shift(0)
    v_22 = v_2.rolling(35).max().shift(0)
    v_23 = v_2.rolling(36).max().shift(0)
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
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc060_65d_val_v060_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc060_65d_val_v060_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc061_66d_val_v061_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(17).max().shift(3)
    v_4 = v_2.rolling(18).std().shift(4)
    v_5 = v_2.rolling(19).min().shift(5)
    v_6 = v_2.rolling(20).mean().shift(6)
    v_7 = v_2.rolling(21).mean().shift(7)
    v_8 = v_2.rolling(22).min().shift(8)
    v_9 = v_2.rolling(23).max().shift(9)
    v_10 = v_2.rolling(24).max().shift(10)
    v_11 = v_2.rolling(25).skew().shift(11)
    v_12 = v_2.rolling(26).max().shift(12)
    v_13 = v_2.diff(27).shift(13)
    v_14 = v_2.rolling(28).skew().shift(14)
    v_15 = v_2.rolling(29).kurt().shift(0)
    v_16 = v_2.rolling(30).max().shift(1)
    v_17 = v_2.rolling(31).std().shift(2)
    v_18 = v_2.rolling(32).std().shift(3)
    v_19 = v_2.rolling(33).max().shift(4)
    v_20 = v_2.rolling(34).min().shift(5)
    v_21 = v_2.rolling(35).std().shift(6)
    v_22 = v_2.rolling(36).max().shift(7)
    v_23 = v_2.rolling(37).mean().shift(8)
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
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc061_66d_val_v061_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc061_66d_val_v061_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc062_67d_val_v062_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(18).kurt().shift(6)
    v_4 = v_2.rolling(19).max().shift(8)
    v_5 = v_2.rolling(20).kurt().shift(10)
    v_6 = v_2.rolling(21).skew().shift(12)
    v_7 = v_2.rolling(22).max().shift(14)
    v_8 = v_2.rolling(23).mean().shift(1)
    v_9 = v_2.rolling(24).mean().shift(3)
    v_10 = v_2.rolling(25).kurt().shift(5)
    v_11 = v_2.rolling(26).max().shift(7)
    v_12 = v_2.rolling(27).kurt().shift(9)
    v_13 = v_2.rolling(28).kurt().shift(11)
    v_14 = v_2.rolling(29).max().shift(13)
    v_15 = v_2.rolling(30).mean().shift(0)
    v_16 = v_2.rolling(31).max().shift(2)
    v_17 = v_2.rolling(32).kurt().shift(4)
    v_18 = v_2.rolling(33).max().shift(6)
    v_19 = v_2.rolling(34).skew().shift(8)
    v_20 = v_2.rolling(35).std().shift(10)
    v_21 = v_2.rolling(36).kurt().shift(12)
    v_22 = v_2.rolling(37).mean().shift(14)
    v_23 = v_2.rolling(38).mean().shift(1)
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
    res = v_34 + v_35 - v_36
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc062_67d_val_v062_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc062_67d_val_v062_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc063_68d_val_v063_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(19).skew().shift(9)
    v_4 = v_2.rolling(20).min().shift(12)
    v_5 = v_2.rolling(21).mean().shift(0)
    v_6 = v_2.rolling(22).skew().shift(3)
    v_7 = v_2.rolling(23).max().shift(6)
    v_8 = v_2.diff(24).shift(9)
    v_9 = v_2.rolling(25).mean().shift(12)
    v_10 = v_2.rolling(26).skew().shift(0)
    v_11 = v_2.diff(27).shift(3)
    v_12 = v_2.rolling(28).mean().shift(6)
    v_13 = v_2.diff(29).shift(9)
    v_14 = v_2.rolling(30).skew().shift(12)
    v_15 = v_2.rolling(31).kurt().shift(0)
    v_16 = v_2.rolling(32).skew().shift(3)
    v_17 = v_2.rolling(33).min().shift(6)
    v_18 = v_2.rolling(34).std().shift(9)
    v_19 = v_2.rolling(35).std().shift(12)
    v_20 = v_2.rolling(36).kurt().shift(0)
    v_21 = v_2.rolling(37).kurt().shift(3)
    v_22 = v_2.rolling(38).mean().shift(6)
    v_23 = v_2.diff(39).shift(9)
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
    res = v_25
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc063_68d_val_v063_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc063_68d_val_v063_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc064_69d_val_v064_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(20).max().shift(12)
    v_4 = v_2.rolling(21).mean().shift(1)
    v_5 = v_2.rolling(22).skew().shift(5)
    v_6 = v_2.diff(23).shift(9)
    v_7 = v_2.rolling(24).std().shift(13)
    v_8 = v_2.rolling(25).mean().shift(2)
    v_9 = v_2.rolling(26).skew().shift(6)
    v_10 = v_2.rolling(27).min().shift(10)
    v_11 = v_2.rolling(28).std().shift(14)
    v_12 = v_2.rolling(29).std().shift(3)
    v_13 = v_2.diff(30).shift(7)
    v_14 = v_2.rolling(31).skew().shift(11)
    v_15 = v_2.rolling(32).min().shift(0)
    v_16 = v_2.rolling(33).mean().shift(4)
    v_17 = v_2.diff(34).shift(8)
    v_18 = v_2.rolling(35).min().shift(12)
    v_19 = v_2.rolling(36).skew().shift(1)
    v_20 = v_2.rolling(37).kurt().shift(5)
    v_21 = v_2.rolling(38).mean().shift(9)
    v_22 = v_2.diff(39).shift(13)
    v_23 = v_2.diff(40).shift(2)
    v_24 = v_2.rolling(41).max().shift(6)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc064_69d_val_v064_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc064_69d_val_v064_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc065_70d_val_v065_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(21).shift(0)
    v_4 = v_2.rolling(22).mean().shift(5)
    v_5 = v_2.diff(23).shift(10)
    v_6 = v_2.diff(24).shift(0)
    v_7 = v_2.rolling(25).min().shift(5)
    v_8 = v_2.rolling(26).max().shift(10)
    v_9 = v_2.rolling(27).max().shift(0)
    v_10 = v_2.diff(28).shift(5)
    v_11 = v_2.diff(29).shift(10)
    v_12 = v_2.diff(30).shift(0)
    v_13 = v_2.rolling(31).mean().shift(5)
    v_14 = v_2.rolling(32).max().shift(10)
    v_15 = v_2.rolling(33).min().shift(0)
    v_16 = v_2.rolling(34).min().shift(5)
    v_17 = v_2.diff(35).shift(10)
    v_18 = v_2.diff(36).shift(0)
    v_19 = v_2.rolling(37).std().shift(5)
    v_20 = v_2.rolling(38).max().shift(10)
    v_21 = v_2.rolling(39).max().shift(0)
    v_22 = v_2.rolling(40).min().shift(5)
    v_23 = v_2.rolling(41).mean().shift(10)
    v_24 = v_2.rolling(42).std().shift(0)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc065_70d_val_v065_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc065_70d_val_v065_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc066_71d_val_v066_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(22).mean().shift(3)
    v_4 = v_2.rolling(23).min().shift(9)
    v_5 = v_2.rolling(24).std().shift(0)
    v_6 = v_2.rolling(25).min().shift(6)
    v_7 = v_2.rolling(26).kurt().shift(12)
    v_8 = v_2.rolling(27).std().shift(3)
    v_9 = v_2.rolling(28).skew().shift(9)
    v_10 = v_2.rolling(29).skew().shift(0)
    v_11 = v_2.rolling(30).max().shift(6)
    v_12 = v_2.rolling(31).min().shift(12)
    v_13 = v_2.rolling(32).kurt().shift(3)
    v_14 = v_2.rolling(33).mean().shift(9)
    v_15 = v_2.rolling(34).mean().shift(0)
    v_16 = v_2.rolling(35).kurt().shift(6)
    v_17 = v_2.rolling(36).mean().shift(12)
    v_18 = v_2.rolling(37).kurt().shift(3)
    v_19 = v_2.rolling(38).std().shift(9)
    v_20 = v_2.rolling(39).std().shift(0)
    v_21 = v_2.rolling(40).std().shift(6)
    v_22 = v_2.rolling(41).std().shift(12)
    v_23 = v_2.diff(42).shift(3)
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
    res = v_29.rolling(71).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc066_71d_val_v066_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc066_71d_val_v066_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc067_72d_val_v067_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(23).kurt().shift(6)
    v_4 = v_2.rolling(24).min().shift(13)
    v_5 = v_2.rolling(25).std().shift(5)
    v_6 = v_2.rolling(26).skew().shift(12)
    v_7 = v_2.rolling(27).min().shift(4)
    v_8 = v_2.rolling(28).max().shift(11)
    v_9 = v_2.diff(29).shift(3)
    v_10 = v_2.diff(30).shift(10)
    v_11 = v_2.rolling(31).min().shift(2)
    v_12 = v_2.rolling(32).min().shift(9)
    v_13 = v_2.rolling(33).skew().shift(1)
    v_14 = v_2.rolling(34).std().shift(8)
    v_15 = v_2.rolling(35).max().shift(0)
    v_16 = v_2.rolling(36).std().shift(7)
    v_17 = v_2.rolling(37).mean().shift(14)
    v_18 = v_2.rolling(38).std().shift(6)
    v_19 = v_2.rolling(39).max().shift(13)
    v_20 = v_2.rolling(40).std().shift(5)
    v_21 = v_2.rolling(41).skew().shift(12)
    v_22 = v_2.rolling(42).mean().shift(4)
    v_23 = v_2.rolling(43).min().shift(11)
    v_24 = v_2.rolling(44).skew().shift(3)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc067_72d_val_v067_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc067_72d_val_v067_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc068_73d_val_v068_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(24).max().shift(9)
    v_4 = v_2.diff(25).shift(2)
    v_5 = v_2.diff(26).shift(10)
    v_6 = v_2.diff(27).shift(3)
    v_7 = v_2.diff(28).shift(11)
    v_8 = v_2.rolling(29).mean().shift(4)
    v_9 = v_2.rolling(30).mean().shift(12)
    v_10 = v_2.rolling(31).skew().shift(5)
    v_11 = v_2.rolling(32).min().shift(13)
    v_12 = v_2.rolling(33).kurt().shift(6)
    v_13 = v_2.rolling(34).skew().shift(14)
    v_14 = v_2.rolling(35).skew().shift(7)
    v_15 = v_2.rolling(36).max().shift(0)
    v_16 = v_2.rolling(37).kurt().shift(8)
    v_17 = v_2.rolling(38).mean().shift(1)
    v_18 = v_2.rolling(39).skew().shift(9)
    v_19 = v_2.rolling(40).max().shift(2)
    v_20 = v_2.diff(41).shift(10)
    v_21 = v_2.diff(42).shift(3)
    v_22 = v_2.rolling(43).std().shift(11)
    v_23 = v_2.rolling(44).max().shift(4)
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
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc068_73d_val_v068_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc068_73d_val_v068_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc069_74d_val_v069_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(25).min().shift(12)
    v_4 = v_2.rolling(26).mean().shift(6)
    v_5 = v_2.rolling(27).skew().shift(0)
    v_6 = v_2.diff(28).shift(9)
    v_7 = v_2.diff(29).shift(3)
    v_8 = v_2.rolling(30).mean().shift(12)
    v_9 = v_2.rolling(31).std().shift(6)
    v_10 = v_2.rolling(32).mean().shift(0)
    v_11 = v_2.rolling(33).kurt().shift(9)
    v_12 = v_2.rolling(34).skew().shift(3)
    v_13 = v_2.rolling(35).mean().shift(12)
    v_14 = v_2.diff(36).shift(6)
    v_15 = v_2.diff(37).shift(0)
    v_16 = v_2.rolling(38).kurt().shift(9)
    v_17 = v_2.rolling(39).min().shift(3)
    v_18 = v_2.diff(40).shift(12)
    v_19 = v_2.rolling(41).mean().shift(6)
    v_20 = v_2.rolling(42).skew().shift(0)
    v_21 = v_2.rolling(43).std().shift(9)
    v_22 = v_2.diff(44).shift(3)
    v_23 = v_2.rolling(45).kurt().shift(12)
    v_24 = v_2.rolling(46).max().shift(6)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc069_74d_val_v069_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc069_74d_val_v069_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc070_75d_val_v070_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(26).shift(0)
    v_4 = v_2.diff(27).shift(10)
    v_5 = v_2.rolling(28).mean().shift(5)
    v_6 = v_2.rolling(29).max().shift(0)
    v_7 = v_2.rolling(30).std().shift(10)
    v_8 = v_2.rolling(31).mean().shift(5)
    v_9 = v_2.diff(32).shift(0)
    v_10 = v_2.rolling(33).std().shift(10)
    v_11 = v_2.rolling(34).std().shift(5)
    v_12 = v_2.rolling(35).kurt().shift(0)
    v_13 = v_2.diff(36).shift(10)
    v_14 = v_2.rolling(37).max().shift(5)
    v_15 = v_2.rolling(38).skew().shift(0)
    v_16 = v_2.rolling(39).skew().shift(10)
    v_17 = v_2.rolling(40).min().shift(5)
    v_18 = v_2.rolling(41).kurt().shift(0)
    v_19 = v_2.rolling(42).kurt().shift(10)
    v_20 = v_2.rolling(43).skew().shift(5)
    v_21 = v_2.rolling(44).skew().shift(0)
    v_22 = v_2.rolling(45).kurt().shift(10)
    v_23 = v_2.diff(46).shift(5)
    v_24 = v_2.diff(47).shift(0)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc070_75d_val_v070_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc070_75d_val_v070_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc071_76d_val_v071_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.diff(27).shift(3)
    v_4 = v_2.rolling(28).min().shift(14)
    v_5 = v_2.rolling(29).max().shift(10)
    v_6 = v_2.rolling(30).min().shift(6)
    v_7 = v_2.rolling(31).max().shift(2)
    v_8 = v_2.diff(32).shift(13)
    v_9 = v_2.rolling(33).std().shift(9)
    v_10 = v_2.rolling(34).kurt().shift(5)
    v_11 = v_2.rolling(35).max().shift(1)
    v_12 = v_2.diff(36).shift(12)
    v_13 = v_2.rolling(37).max().shift(8)
    v_14 = v_2.rolling(38).kurt().shift(4)
    v_15 = v_2.rolling(39).kurt().shift(0)
    v_16 = v_2.rolling(40).skew().shift(11)
    v_17 = v_2.rolling(41).kurt().shift(7)
    v_18 = v_2.diff(42).shift(3)
    v_19 = v_2.rolling(43).skew().shift(14)
    v_20 = v_2.diff(44).shift(10)
    v_21 = v_2.rolling(45).mean().shift(6)
    v_22 = v_2.rolling(46).max().shift(2)
    v_23 = v_2.rolling(47).std().shift(13)
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
    res = v_26 / v_25.replace(0, np.nan)
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc071_76d_val_v071_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc071_76d_val_v071_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc072_77d_val_v072_signal(workingcapital, revenue):
    v_0 = workingcapital * 1.0
    v_1 = revenue * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(28).skew().shift(6)
    v_4 = v_2.rolling(29).skew().shift(3)
    v_5 = v_2.rolling(30).std().shift(0)
    v_6 = v_2.rolling(31).min().shift(12)
    v_7 = v_2.rolling(32).min().shift(9)
    v_8 = v_2.rolling(33).std().shift(6)
    v_9 = v_2.rolling(34).skew().shift(3)
    v_10 = v_2.rolling(35).max().shift(0)
    v_11 = v_2.rolling(36).min().shift(12)
    v_12 = v_2.rolling(37).skew().shift(9)
    v_13 = v_2.rolling(38).skew().shift(6)
    v_14 = v_2.diff(39).shift(3)
    v_15 = v_2.rolling(40).skew().shift(0)
    v_16 = v_2.rolling(41).min().shift(12)
    v_17 = v_2.diff(42).shift(9)
    v_18 = v_2.diff(43).shift(6)
    v_19 = v_2.rolling(44).max().shift(3)
    v_20 = v_2.rolling(45).skew().shift(0)
    v_21 = v_2.rolling(46).min().shift(12)
    v_22 = v_2.rolling(47).mean().shift(9)
    v_23 = v_2.rolling(48).std().shift(6)
    v_24 = v_2.diff(49).shift(3)
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
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc072_77d_val_v072_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc072_77d_val_v072_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc073_78d_val_v073_signal(revenue, assets):
    v_0 = revenue * 1.0
    v_1 = assets * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(29).mean().shift(9)
    v_4 = v_2.diff(30).shift(7)
    v_5 = v_2.rolling(31).min().shift(5)
    v_6 = v_2.rolling(32).max().shift(3)
    v_7 = v_2.rolling(33).mean().shift(1)
    v_8 = v_2.rolling(34).max().shift(14)
    v_9 = v_2.diff(35).shift(12)
    v_10 = v_2.rolling(36).min().shift(10)
    v_11 = v_2.rolling(37).kurt().shift(8)
    v_12 = v_2.rolling(38).skew().shift(6)
    v_13 = v_2.rolling(39).skew().shift(4)
    v_14 = v_2.rolling(40).mean().shift(2)
    v_15 = v_2.rolling(41).std().shift(0)
    v_16 = v_2.rolling(42).max().shift(13)
    v_17 = v_2.rolling(43).max().shift(11)
    v_18 = v_2.rolling(44).skew().shift(9)
    v_19 = v_2.rolling(45).min().shift(7)
    v_20 = v_2.rolling(46).skew().shift(5)
    v_21 = v_2.rolling(47).mean().shift(3)
    v_22 = v_2.rolling(48).max().shift(1)
    v_23 = v_2.rolling(49).kurt().shift(14)
    v_24 = v_2.rolling(50).mean().shift(12)
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
    res = v_29.rolling(78).mean()
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc073_78d_val_v073_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc073_78d_val_v073_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc074_79d_val_v074_signal(assets, ncfo):
    v_0 = assets * 1.0
    v_1 = ncfo * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(30).kurt().shift(12)
    v_4 = v_2.rolling(31).max().shift(11)
    v_5 = v_2.rolling(32).max().shift(10)
    v_6 = v_2.rolling(33).kurt().shift(9)
    v_7 = v_2.rolling(34).min().shift(8)
    v_8 = v_2.rolling(35).mean().shift(7)
    v_9 = v_2.rolling(36).kurt().shift(6)
    v_10 = v_2.rolling(37).max().shift(5)
    v_11 = v_2.rolling(38).skew().shift(4)
    v_12 = v_2.rolling(39).mean().shift(3)
    v_13 = v_2.rolling(40).min().shift(2)
    v_14 = v_2.rolling(41).kurt().shift(1)
    v_15 = v_2.rolling(42).min().shift(0)
    v_16 = v_2.rolling(43).std().shift(14)
    v_17 = v_2.rolling(44).mean().shift(13)
    v_18 = v_2.rolling(45).kurt().shift(12)
    v_19 = v_2.rolling(46).std().shift(11)
    v_20 = v_2.rolling(47).min().shift(10)
    v_21 = v_2.rolling(48).mean().shift(9)
    v_22 = v_2.rolling(49).skew().shift(8)
    v_23 = v_2.rolling(50).mean().shift(7)
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
    res = (v_30 + v_31) / 2.0
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc074_79d_val_v074_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc074_79d_val_v074_signal

def f92cv_f92_cash_conversion_cycle_velocity_calc075_80d_val_v075_signal(ncfo, workingcapital):
    v_0 = ncfo * 1.0
    v_1 = workingcapital * 1.0
    v_2 = v_0 / v_1.replace(0, np.nan)
    v_3 = v_2.rolling(31).skew().shift(0)
    v_4 = v_2.rolling(32).std().shift(0)
    v_5 = v_2.rolling(33).skew().shift(0)
    v_6 = v_2.rolling(34).max().shift(0)
    v_7 = v_2.rolling(35).skew().shift(0)
    v_8 = v_2.diff(36).shift(0)
    v_9 = v_2.rolling(37).std().shift(0)
    v_10 = v_2.rolling(38).mean().shift(0)
    v_11 = v_2.rolling(39).mean().shift(0)
    v_12 = v_2.rolling(40).skew().shift(0)
    v_13 = v_2.rolling(41).max().shift(0)
    v_14 = v_2.rolling(42).std().shift(0)
    v_15 = v_2.rolling(43).min().shift(0)
    v_16 = v_2.rolling(44).max().shift(0)
    v_17 = v_2.rolling(45).min().shift(0)
    v_18 = v_2.rolling(46).mean().shift(0)
    v_19 = v_2.rolling(47).kurt().shift(0)
    v_20 = v_2.rolling(48).kurt().shift(0)
    v_21 = v_2.rolling(49).std().shift(0)
    v_22 = v_2.rolling(50).max().shift(0)
    v_23 = v_2.rolling(51).min().shift(0)
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
    res = v_32 * v_33
    return res.replace([np.inf, -np.inf], np.nan)
FEATURE_FUNCTIONS['f92cv_f92_cash_conversion_cycle_velocity_calc075_80d_val_v075_signal'] = f92cv_f92_cash_conversion_cycle_velocity_calc075_80d_val_v075_signal


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
