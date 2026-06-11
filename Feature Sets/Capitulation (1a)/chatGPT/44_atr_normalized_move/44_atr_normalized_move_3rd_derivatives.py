import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _safe_div(a, b):
    b = _s(b).replace(0, np.nan)
    if np.isscalar(a):
        return a / b
    a = _s(a)
    return a / b


def _roc(x, periods=1):
    return _s(x).pct_change(periods)


def _z(x, window):
    x = _s(x)
    mean = x.rolling(window, min_periods=max(3, window // 4)).mean()
    std = x.rolling(window, min_periods=max(3, window // 4)).std().replace(0, np.nan)
    return (x - mean) / std


def _slope(x, window):
    x = _s(x)
    idx = np.arange(window, dtype=float)
    denom = ((idx - idx.mean()) ** 2).sum()
    def calc(v):
        return float(((v - np.nanmean(v)) * (idx - idx.mean())).sum() / denom)
    return x.rolling(window, min_periods=window).apply(calc, raw=True)


def _true_range(high, low, close):
    high = _s(high)
    low = _s(low)
    prev_close = _s(close).shift(1)
    return pd.concat([high - low, (high - prev_close).abs(), (low - prev_close).abs()], axis=1).max(axis=1)


def _streak(mask):
    mask = pd.Series(mask).fillna(False).astype(bool)
    groups = mask.ne(mask.shift()).cumsum()
    return mask.groupby(groups).cumcount().add(1).where(mask, 0).astype(float)



def atr_001_realized_vol_z_accel_1(atr_001_realized_vol_z_roc_1):
    feature = _s(atr_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def atr_007_realized_vol_z_accel_5(atr_007_realized_vol_z_roc_5):
    feature = _s(atr_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def atr_013_realized_vol_z_accel_42(atr_013_realized_vol_z_roc_42):
    feature = _s(atr_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def atr_179_atr_019_realized_vol_z_42_019_accel_126(atr_154_atr_019_realized_vol_z_42_019_roc_126):
    feature = _s(atr_154_atr_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def atr_180_atr_025_realized_vol_z_378_025_accel_378(atr_155_atr_025_realized_vol_z_378_025_roc_378):
    feature = _s(atr_155_atr_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















ATR_NORMALIZED_MOVE_REGISTRY_3RD_DERIVATIVES = {
    'atr_001_realized_vol_z_accel_1': {'inputs': ['atr_001_realized_vol_z_roc_1'], 'func': atr_001_realized_vol_z_accel_1},
    'atr_007_realized_vol_z_accel_5': {'inputs': ['atr_007_realized_vol_z_roc_5'], 'func': atr_007_realized_vol_z_accel_5},
    'atr_013_realized_vol_z_accel_42': {'inputs': ['atr_013_realized_vol_z_roc_42'], 'func': atr_013_realized_vol_z_accel_42},
    'atr_179_atr_019_realized_vol_z_42_019_accel_126': {'inputs': ['atr_154_atr_019_realized_vol_z_42_019_roc_126'], 'func': atr_179_atr_019_realized_vol_z_42_019_accel_126},
    'atr_180_atr_025_realized_vol_z_378_025_accel_378': {'inputs': ['atr_155_atr_025_realized_vol_z_378_025_roc_378'], 'func': atr_180_atr_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def anm_replacement_d3_001(anm_replacement_d2_001):
    feature = _clean(anm_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_001'] = {'inputs': ['anm_replacement_d2_001'], 'func': anm_replacement_d3_001}


def anm_replacement_d3_002(anm_replacement_d2_002):
    feature = _clean(anm_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_002'] = {'inputs': ['anm_replacement_d2_002'], 'func': anm_replacement_d3_002}


def anm_replacement_d3_003(anm_replacement_d2_003):
    feature = _clean(anm_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_003'] = {'inputs': ['anm_replacement_d2_003'], 'func': anm_replacement_d3_003}


def anm_replacement_d3_004(anm_replacement_d2_004):
    feature = _clean(anm_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_004'] = {'inputs': ['anm_replacement_d2_004'], 'func': anm_replacement_d3_004}


def anm_replacement_d3_005(anm_replacement_d2_005):
    feature = _clean(anm_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_005'] = {'inputs': ['anm_replacement_d2_005'], 'func': anm_replacement_d3_005}


def anm_replacement_d3_006(anm_replacement_d2_006):
    feature = _clean(anm_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_006'] = {'inputs': ['anm_replacement_d2_006'], 'func': anm_replacement_d3_006}


def anm_replacement_d3_007(anm_replacement_d2_007):
    feature = _clean(anm_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_007'] = {'inputs': ['anm_replacement_d2_007'], 'func': anm_replacement_d3_007}


def anm_replacement_d3_008(anm_replacement_d2_008):
    feature = _clean(anm_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_008'] = {'inputs': ['anm_replacement_d2_008'], 'func': anm_replacement_d3_008}


def anm_replacement_d3_009(anm_replacement_d2_009):
    feature = _clean(anm_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_009'] = {'inputs': ['anm_replacement_d2_009'], 'func': anm_replacement_d3_009}


def anm_replacement_d3_010(anm_replacement_d2_010):
    feature = _clean(anm_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_010'] = {'inputs': ['anm_replacement_d2_010'], 'func': anm_replacement_d3_010}


def anm_replacement_d3_011(anm_replacement_d2_011):
    feature = _clean(anm_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_011'] = {'inputs': ['anm_replacement_d2_011'], 'func': anm_replacement_d3_011}


def anm_replacement_d3_012(anm_replacement_d2_012):
    feature = _clean(anm_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_012'] = {'inputs': ['anm_replacement_d2_012'], 'func': anm_replacement_d3_012}


def anm_replacement_d3_013(anm_replacement_d2_013):
    feature = _clean(anm_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_013'] = {'inputs': ['anm_replacement_d2_013'], 'func': anm_replacement_d3_013}


def anm_replacement_d3_014(anm_replacement_d2_014):
    feature = _clean(anm_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_014'] = {'inputs': ['anm_replacement_d2_014'], 'func': anm_replacement_d3_014}


def anm_replacement_d3_015(anm_replacement_d2_015):
    feature = _clean(anm_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_015'] = {'inputs': ['anm_replacement_d2_015'], 'func': anm_replacement_d3_015}


def anm_replacement_d3_016(anm_replacement_d2_016):
    feature = _clean(anm_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_016'] = {'inputs': ['anm_replacement_d2_016'], 'func': anm_replacement_d3_016}


def anm_replacement_d3_017(anm_replacement_d2_017):
    feature = _clean(anm_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_017'] = {'inputs': ['anm_replacement_d2_017'], 'func': anm_replacement_d3_017}


def anm_replacement_d3_018(anm_replacement_d2_018):
    feature = _clean(anm_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_018'] = {'inputs': ['anm_replacement_d2_018'], 'func': anm_replacement_d3_018}


def anm_replacement_d3_019(anm_replacement_d2_019):
    feature = _clean(anm_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_019'] = {'inputs': ['anm_replacement_d2_019'], 'func': anm_replacement_d3_019}


def anm_replacement_d3_020(anm_replacement_d2_020):
    feature = _clean(anm_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_020'] = {'inputs': ['anm_replacement_d2_020'], 'func': anm_replacement_d3_020}


def anm_replacement_d3_021(anm_replacement_d2_021):
    feature = _clean(anm_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_021'] = {'inputs': ['anm_replacement_d2_021'], 'func': anm_replacement_d3_021}


def anm_replacement_d3_022(anm_replacement_d2_022):
    feature = _clean(anm_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_022'] = {'inputs': ['anm_replacement_d2_022'], 'func': anm_replacement_d3_022}


def anm_replacement_d3_023(anm_replacement_d2_023):
    feature = _clean(anm_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_023'] = {'inputs': ['anm_replacement_d2_023'], 'func': anm_replacement_d3_023}


def anm_replacement_d3_024(anm_replacement_d2_024):
    feature = _clean(anm_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_024'] = {'inputs': ['anm_replacement_d2_024'], 'func': anm_replacement_d3_024}


def anm_replacement_d3_025(anm_replacement_d2_025):
    feature = _clean(anm_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_025'] = {'inputs': ['anm_replacement_d2_025'], 'func': anm_replacement_d3_025}


def anm_replacement_d3_026(anm_replacement_d2_026):
    feature = _clean(anm_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_026'] = {'inputs': ['anm_replacement_d2_026'], 'func': anm_replacement_d3_026}


def anm_replacement_d3_027(anm_replacement_d2_027):
    feature = _clean(anm_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_027'] = {'inputs': ['anm_replacement_d2_027'], 'func': anm_replacement_d3_027}


def anm_replacement_d3_028(anm_replacement_d2_028):
    feature = _clean(anm_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_028'] = {'inputs': ['anm_replacement_d2_028'], 'func': anm_replacement_d3_028}


def anm_replacement_d3_029(anm_replacement_d2_029):
    feature = _clean(anm_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_029'] = {'inputs': ['anm_replacement_d2_029'], 'func': anm_replacement_d3_029}


def anm_replacement_d3_030(anm_replacement_d2_030):
    feature = _clean(anm_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_030'] = {'inputs': ['anm_replacement_d2_030'], 'func': anm_replacement_d3_030}


def anm_replacement_d3_031(anm_replacement_d2_031):
    feature = _clean(anm_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_031'] = {'inputs': ['anm_replacement_d2_031'], 'func': anm_replacement_d3_031}


def anm_replacement_d3_032(anm_replacement_d2_032):
    feature = _clean(anm_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_032'] = {'inputs': ['anm_replacement_d2_032'], 'func': anm_replacement_d3_032}


def anm_replacement_d3_033(anm_replacement_d2_033):
    feature = _clean(anm_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_033'] = {'inputs': ['anm_replacement_d2_033'], 'func': anm_replacement_d3_033}


def anm_replacement_d3_034(anm_replacement_d2_034):
    feature = _clean(anm_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_034'] = {'inputs': ['anm_replacement_d2_034'], 'func': anm_replacement_d3_034}


def anm_replacement_d3_035(anm_replacement_d2_035):
    feature = _clean(anm_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_035'] = {'inputs': ['anm_replacement_d2_035'], 'func': anm_replacement_d3_035}


def anm_replacement_d3_036(anm_replacement_d2_036):
    feature = _clean(anm_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_036'] = {'inputs': ['anm_replacement_d2_036'], 'func': anm_replacement_d3_036}


def anm_replacement_d3_037(anm_replacement_d2_037):
    feature = _clean(anm_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_037'] = {'inputs': ['anm_replacement_d2_037'], 'func': anm_replacement_d3_037}


def anm_replacement_d3_038(anm_replacement_d2_038):
    feature = _clean(anm_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_038'] = {'inputs': ['anm_replacement_d2_038'], 'func': anm_replacement_d3_038}


def anm_replacement_d3_039(anm_replacement_d2_039):
    feature = _clean(anm_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_039'] = {'inputs': ['anm_replacement_d2_039'], 'func': anm_replacement_d3_039}


def anm_replacement_d3_040(anm_replacement_d2_040):
    feature = _clean(anm_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_040'] = {'inputs': ['anm_replacement_d2_040'], 'func': anm_replacement_d3_040}


def anm_replacement_d3_041(anm_replacement_d2_041):
    feature = _clean(anm_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_041'] = {'inputs': ['anm_replacement_d2_041'], 'func': anm_replacement_d3_041}


def anm_replacement_d3_042(anm_replacement_d2_042):
    feature = _clean(anm_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_042'] = {'inputs': ['anm_replacement_d2_042'], 'func': anm_replacement_d3_042}


def anm_replacement_d3_043(anm_replacement_d2_043):
    feature = _clean(anm_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_043'] = {'inputs': ['anm_replacement_d2_043'], 'func': anm_replacement_d3_043}


def anm_replacement_d3_044(anm_replacement_d2_044):
    feature = _clean(anm_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_044'] = {'inputs': ['anm_replacement_d2_044'], 'func': anm_replacement_d3_044}


def anm_replacement_d3_045(anm_replacement_d2_045):
    feature = _clean(anm_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_045'] = {'inputs': ['anm_replacement_d2_045'], 'func': anm_replacement_d3_045}


def anm_replacement_d3_046(anm_replacement_d2_046):
    feature = _clean(anm_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_046'] = {'inputs': ['anm_replacement_d2_046'], 'func': anm_replacement_d3_046}


def anm_replacement_d3_047(anm_replacement_d2_047):
    feature = _clean(anm_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_047'] = {'inputs': ['anm_replacement_d2_047'], 'func': anm_replacement_d3_047}


def anm_replacement_d3_048(anm_replacement_d2_048):
    feature = _clean(anm_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_048'] = {'inputs': ['anm_replacement_d2_048'], 'func': anm_replacement_d3_048}


def anm_replacement_d3_049(anm_replacement_d2_049):
    feature = _clean(anm_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_049'] = {'inputs': ['anm_replacement_d2_049'], 'func': anm_replacement_d3_049}


def anm_replacement_d3_050(anm_replacement_d2_050):
    feature = _clean(anm_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_050'] = {'inputs': ['anm_replacement_d2_050'], 'func': anm_replacement_d3_050}


def anm_replacement_d3_051(anm_replacement_d2_051):
    feature = _clean(anm_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_051'] = {'inputs': ['anm_replacement_d2_051'], 'func': anm_replacement_d3_051}


def anm_replacement_d3_052(anm_replacement_d2_052):
    feature = _clean(anm_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_052'] = {'inputs': ['anm_replacement_d2_052'], 'func': anm_replacement_d3_052}


def anm_replacement_d3_053(anm_replacement_d2_053):
    feature = _clean(anm_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_053'] = {'inputs': ['anm_replacement_d2_053'], 'func': anm_replacement_d3_053}


def anm_replacement_d3_054(anm_replacement_d2_054):
    feature = _clean(anm_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_054'] = {'inputs': ['anm_replacement_d2_054'], 'func': anm_replacement_d3_054}


def anm_replacement_d3_055(anm_replacement_d2_055):
    feature = _clean(anm_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_055'] = {'inputs': ['anm_replacement_d2_055'], 'func': anm_replacement_d3_055}


def anm_replacement_d3_056(anm_replacement_d2_056):
    feature = _clean(anm_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_056'] = {'inputs': ['anm_replacement_d2_056'], 'func': anm_replacement_d3_056}


def anm_replacement_d3_057(anm_replacement_d2_057):
    feature = _clean(anm_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_057'] = {'inputs': ['anm_replacement_d2_057'], 'func': anm_replacement_d3_057}


def anm_replacement_d3_058(anm_replacement_d2_058):
    feature = _clean(anm_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_058'] = {'inputs': ['anm_replacement_d2_058'], 'func': anm_replacement_d3_058}


def anm_replacement_d3_059(anm_replacement_d2_059):
    feature = _clean(anm_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_059'] = {'inputs': ['anm_replacement_d2_059'], 'func': anm_replacement_d3_059}


def anm_replacement_d3_060(anm_replacement_d2_060):
    feature = _clean(anm_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_060'] = {'inputs': ['anm_replacement_d2_060'], 'func': anm_replacement_d3_060}


def anm_replacement_d3_061(anm_replacement_d2_061):
    feature = _clean(anm_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_061'] = {'inputs': ['anm_replacement_d2_061'], 'func': anm_replacement_d3_061}


def anm_replacement_d3_062(anm_replacement_d2_062):
    feature = _clean(anm_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_062'] = {'inputs': ['anm_replacement_d2_062'], 'func': anm_replacement_d3_062}


def anm_replacement_d3_063(anm_replacement_d2_063):
    feature = _clean(anm_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_063'] = {'inputs': ['anm_replacement_d2_063'], 'func': anm_replacement_d3_063}


def anm_replacement_d3_064(anm_replacement_d2_064):
    feature = _clean(anm_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_064'] = {'inputs': ['anm_replacement_d2_064'], 'func': anm_replacement_d3_064}


def anm_replacement_d3_065(anm_replacement_d2_065):
    feature = _clean(anm_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_065'] = {'inputs': ['anm_replacement_d2_065'], 'func': anm_replacement_d3_065}


def anm_replacement_d3_066(anm_replacement_d2_066):
    feature = _clean(anm_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_066'] = {'inputs': ['anm_replacement_d2_066'], 'func': anm_replacement_d3_066}


def anm_replacement_d3_067(anm_replacement_d2_067):
    feature = _clean(anm_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_067'] = {'inputs': ['anm_replacement_d2_067'], 'func': anm_replacement_d3_067}


def anm_replacement_d3_068(anm_replacement_d2_068):
    feature = _clean(anm_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_068'] = {'inputs': ['anm_replacement_d2_068'], 'func': anm_replacement_d3_068}


def anm_replacement_d3_069(anm_replacement_d2_069):
    feature = _clean(anm_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_069'] = {'inputs': ['anm_replacement_d2_069'], 'func': anm_replacement_d3_069}


def anm_replacement_d3_070(anm_replacement_d2_070):
    feature = _clean(anm_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_070'] = {'inputs': ['anm_replacement_d2_070'], 'func': anm_replacement_d3_070}


def anm_replacement_d3_071(anm_replacement_d2_071):
    feature = _clean(anm_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_071'] = {'inputs': ['anm_replacement_d2_071'], 'func': anm_replacement_d3_071}


def anm_replacement_d3_072(anm_replacement_d2_072):
    feature = _clean(anm_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_072'] = {'inputs': ['anm_replacement_d2_072'], 'func': anm_replacement_d3_072}


def anm_replacement_d3_073(anm_replacement_d2_073):
    feature = _clean(anm_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_073'] = {'inputs': ['anm_replacement_d2_073'], 'func': anm_replacement_d3_073}


def anm_replacement_d3_074(anm_replacement_d2_074):
    feature = _clean(anm_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_074'] = {'inputs': ['anm_replacement_d2_074'], 'func': anm_replacement_d3_074}


def anm_replacement_d3_075(anm_replacement_d2_075):
    feature = _clean(anm_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_075'] = {'inputs': ['anm_replacement_d2_075'], 'func': anm_replacement_d3_075}


def anm_replacement_d3_076(anm_replacement_d2_076):
    feature = _clean(anm_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_076'] = {'inputs': ['anm_replacement_d2_076'], 'func': anm_replacement_d3_076}


def anm_replacement_d3_077(anm_replacement_d2_077):
    feature = _clean(anm_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_077'] = {'inputs': ['anm_replacement_d2_077'], 'func': anm_replacement_d3_077}


def anm_replacement_d3_078(anm_replacement_d2_078):
    feature = _clean(anm_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_078'] = {'inputs': ['anm_replacement_d2_078'], 'func': anm_replacement_d3_078}


def anm_replacement_d3_079(anm_replacement_d2_079):
    feature = _clean(anm_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_079'] = {'inputs': ['anm_replacement_d2_079'], 'func': anm_replacement_d3_079}


def anm_replacement_d3_080(anm_replacement_d2_080):
    feature = _clean(anm_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_080'] = {'inputs': ['anm_replacement_d2_080'], 'func': anm_replacement_d3_080}


def anm_replacement_d3_081(anm_replacement_d2_081):
    feature = _clean(anm_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_081'] = {'inputs': ['anm_replacement_d2_081'], 'func': anm_replacement_d3_081}


def anm_replacement_d3_082(anm_replacement_d2_082):
    feature = _clean(anm_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_082'] = {'inputs': ['anm_replacement_d2_082'], 'func': anm_replacement_d3_082}


def anm_replacement_d3_083(anm_replacement_d2_083):
    feature = _clean(anm_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_083'] = {'inputs': ['anm_replacement_d2_083'], 'func': anm_replacement_d3_083}


def anm_replacement_d3_084(anm_replacement_d2_084):
    feature = _clean(anm_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_084'] = {'inputs': ['anm_replacement_d2_084'], 'func': anm_replacement_d3_084}


def anm_replacement_d3_085(anm_replacement_d2_085):
    feature = _clean(anm_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_085'] = {'inputs': ['anm_replacement_d2_085'], 'func': anm_replacement_d3_085}


def anm_replacement_d3_086(anm_replacement_d2_086):
    feature = _clean(anm_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_086'] = {'inputs': ['anm_replacement_d2_086'], 'func': anm_replacement_d3_086}


def anm_replacement_d3_087(anm_replacement_d2_087):
    feature = _clean(anm_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_087'] = {'inputs': ['anm_replacement_d2_087'], 'func': anm_replacement_d3_087}


def anm_replacement_d3_088(anm_replacement_d2_088):
    feature = _clean(anm_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_088'] = {'inputs': ['anm_replacement_d2_088'], 'func': anm_replacement_d3_088}


def anm_replacement_d3_089(anm_replacement_d2_089):
    feature = _clean(anm_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_089'] = {'inputs': ['anm_replacement_d2_089'], 'func': anm_replacement_d3_089}


def anm_replacement_d3_090(anm_replacement_d2_090):
    feature = _clean(anm_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_090'] = {'inputs': ['anm_replacement_d2_090'], 'func': anm_replacement_d3_090}


def anm_replacement_d3_091(anm_replacement_d2_091):
    feature = _clean(anm_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_091'] = {'inputs': ['anm_replacement_d2_091'], 'func': anm_replacement_d3_091}


def anm_replacement_d3_092(anm_replacement_d2_092):
    feature = _clean(anm_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_092'] = {'inputs': ['anm_replacement_d2_092'], 'func': anm_replacement_d3_092}


def anm_replacement_d3_093(anm_replacement_d2_093):
    feature = _clean(anm_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_093'] = {'inputs': ['anm_replacement_d2_093'], 'func': anm_replacement_d3_093}


def anm_replacement_d3_094(anm_replacement_d2_094):
    feature = _clean(anm_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_094'] = {'inputs': ['anm_replacement_d2_094'], 'func': anm_replacement_d3_094}


def anm_replacement_d3_095(anm_replacement_d2_095):
    feature = _clean(anm_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_095'] = {'inputs': ['anm_replacement_d2_095'], 'func': anm_replacement_d3_095}


def anm_replacement_d3_096(anm_replacement_d2_096):
    feature = _clean(anm_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_096'] = {'inputs': ['anm_replacement_d2_096'], 'func': anm_replacement_d3_096}


def anm_replacement_d3_097(anm_replacement_d2_097):
    feature = _clean(anm_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_097'] = {'inputs': ['anm_replacement_d2_097'], 'func': anm_replacement_d3_097}


def anm_replacement_d3_098(anm_replacement_d2_098):
    feature = _clean(anm_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_098'] = {'inputs': ['anm_replacement_d2_098'], 'func': anm_replacement_d3_098}


def anm_replacement_d3_099(anm_replacement_d2_099):
    feature = _clean(anm_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_099'] = {'inputs': ['anm_replacement_d2_099'], 'func': anm_replacement_d3_099}


def anm_replacement_d3_100(anm_replacement_d2_100):
    feature = _clean(anm_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_100'] = {'inputs': ['anm_replacement_d2_100'], 'func': anm_replacement_d3_100}


def anm_replacement_d3_101(anm_replacement_d2_101):
    feature = _clean(anm_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_101'] = {'inputs': ['anm_replacement_d2_101'], 'func': anm_replacement_d3_101}


def anm_replacement_d3_102(anm_replacement_d2_102):
    feature = _clean(anm_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_102'] = {'inputs': ['anm_replacement_d2_102'], 'func': anm_replacement_d3_102}


def anm_replacement_d3_103(anm_replacement_d2_103):
    feature = _clean(anm_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_103'] = {'inputs': ['anm_replacement_d2_103'], 'func': anm_replacement_d3_103}


def anm_replacement_d3_104(anm_replacement_d2_104):
    feature = _clean(anm_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_104'] = {'inputs': ['anm_replacement_d2_104'], 'func': anm_replacement_d3_104}


def anm_replacement_d3_105(anm_replacement_d2_105):
    feature = _clean(anm_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_105'] = {'inputs': ['anm_replacement_d2_105'], 'func': anm_replacement_d3_105}


def anm_replacement_d3_106(anm_replacement_d2_106):
    feature = _clean(anm_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_106'] = {'inputs': ['anm_replacement_d2_106'], 'func': anm_replacement_d3_106}


def anm_replacement_d3_107(anm_replacement_d2_107):
    feature = _clean(anm_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_107'] = {'inputs': ['anm_replacement_d2_107'], 'func': anm_replacement_d3_107}


def anm_replacement_d3_108(anm_replacement_d2_108):
    feature = _clean(anm_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_108'] = {'inputs': ['anm_replacement_d2_108'], 'func': anm_replacement_d3_108}


def anm_replacement_d3_109(anm_replacement_d2_109):
    feature = _clean(anm_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_109'] = {'inputs': ['anm_replacement_d2_109'], 'func': anm_replacement_d3_109}


def anm_replacement_d3_110(anm_replacement_d2_110):
    feature = _clean(anm_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_110'] = {'inputs': ['anm_replacement_d2_110'], 'func': anm_replacement_d3_110}


def anm_replacement_d3_111(anm_replacement_d2_111):
    feature = _clean(anm_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_111'] = {'inputs': ['anm_replacement_d2_111'], 'func': anm_replacement_d3_111}


def anm_replacement_d3_112(anm_replacement_d2_112):
    feature = _clean(anm_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_112'] = {'inputs': ['anm_replacement_d2_112'], 'func': anm_replacement_d3_112}


def anm_replacement_d3_113(anm_replacement_d2_113):
    feature = _clean(anm_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_113'] = {'inputs': ['anm_replacement_d2_113'], 'func': anm_replacement_d3_113}


def anm_replacement_d3_114(anm_replacement_d2_114):
    feature = _clean(anm_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_114'] = {'inputs': ['anm_replacement_d2_114'], 'func': anm_replacement_d3_114}


def anm_replacement_d3_115(anm_replacement_d2_115):
    feature = _clean(anm_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_115'] = {'inputs': ['anm_replacement_d2_115'], 'func': anm_replacement_d3_115}


def anm_replacement_d3_116(anm_replacement_d2_116):
    feature = _clean(anm_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_116'] = {'inputs': ['anm_replacement_d2_116'], 'func': anm_replacement_d3_116}


def anm_replacement_d3_117(anm_replacement_d2_117):
    feature = _clean(anm_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_117'] = {'inputs': ['anm_replacement_d2_117'], 'func': anm_replacement_d3_117}


def anm_replacement_d3_118(anm_replacement_d2_118):
    feature = _clean(anm_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_118'] = {'inputs': ['anm_replacement_d2_118'], 'func': anm_replacement_d3_118}


def anm_replacement_d3_119(anm_replacement_d2_119):
    feature = _clean(anm_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_119'] = {'inputs': ['anm_replacement_d2_119'], 'func': anm_replacement_d3_119}


def anm_replacement_d3_120(anm_replacement_d2_120):
    feature = _clean(anm_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_120'] = {'inputs': ['anm_replacement_d2_120'], 'func': anm_replacement_d3_120}


def anm_replacement_d3_121(anm_replacement_d2_121):
    feature = _clean(anm_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_121'] = {'inputs': ['anm_replacement_d2_121'], 'func': anm_replacement_d3_121}


def anm_replacement_d3_122(anm_replacement_d2_122):
    feature = _clean(anm_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_122'] = {'inputs': ['anm_replacement_d2_122'], 'func': anm_replacement_d3_122}


def anm_replacement_d3_123(anm_replacement_d2_123):
    feature = _clean(anm_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_123'] = {'inputs': ['anm_replacement_d2_123'], 'func': anm_replacement_d3_123}


def anm_replacement_d3_124(anm_replacement_d2_124):
    feature = _clean(anm_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_124'] = {'inputs': ['anm_replacement_d2_124'], 'func': anm_replacement_d3_124}


def anm_replacement_d3_125(anm_replacement_d2_125):
    feature = _clean(anm_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_125'] = {'inputs': ['anm_replacement_d2_125'], 'func': anm_replacement_d3_125}


def anm_replacement_d3_126(anm_replacement_d2_126):
    feature = _clean(anm_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_126'] = {'inputs': ['anm_replacement_d2_126'], 'func': anm_replacement_d3_126}


def anm_replacement_d3_127(anm_replacement_d2_127):
    feature = _clean(anm_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_127'] = {'inputs': ['anm_replacement_d2_127'], 'func': anm_replacement_d3_127}


def anm_replacement_d3_128(anm_replacement_d2_128):
    feature = _clean(anm_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_128'] = {'inputs': ['anm_replacement_d2_128'], 'func': anm_replacement_d3_128}


def anm_replacement_d3_129(anm_replacement_d2_129):
    feature = _clean(anm_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_129'] = {'inputs': ['anm_replacement_d2_129'], 'func': anm_replacement_d3_129}


def anm_replacement_d3_130(anm_replacement_d2_130):
    feature = _clean(anm_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_130'] = {'inputs': ['anm_replacement_d2_130'], 'func': anm_replacement_d3_130}


def anm_replacement_d3_131(anm_replacement_d2_131):
    feature = _clean(anm_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_131'] = {'inputs': ['anm_replacement_d2_131'], 'func': anm_replacement_d3_131}


def anm_replacement_d3_132(anm_replacement_d2_132):
    feature = _clean(anm_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_132'] = {'inputs': ['anm_replacement_d2_132'], 'func': anm_replacement_d3_132}


def anm_replacement_d3_133(anm_replacement_d2_133):
    feature = _clean(anm_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_133'] = {'inputs': ['anm_replacement_d2_133'], 'func': anm_replacement_d3_133}


def anm_replacement_d3_134(anm_replacement_d2_134):
    feature = _clean(anm_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_134'] = {'inputs': ['anm_replacement_d2_134'], 'func': anm_replacement_d3_134}


def anm_replacement_d3_135(anm_replacement_d2_135):
    feature = _clean(anm_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_135'] = {'inputs': ['anm_replacement_d2_135'], 'func': anm_replacement_d3_135}


def anm_replacement_d3_136(anm_replacement_d2_136):
    feature = _clean(anm_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_136'] = {'inputs': ['anm_replacement_d2_136'], 'func': anm_replacement_d3_136}


def anm_replacement_d3_137(anm_replacement_d2_137):
    feature = _clean(anm_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_137'] = {'inputs': ['anm_replacement_d2_137'], 'func': anm_replacement_d3_137}


def anm_replacement_d3_138(anm_replacement_d2_138):
    feature = _clean(anm_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_138'] = {'inputs': ['anm_replacement_d2_138'], 'func': anm_replacement_d3_138}


def anm_replacement_d3_139(anm_replacement_d2_139):
    feature = _clean(anm_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_139'] = {'inputs': ['anm_replacement_d2_139'], 'func': anm_replacement_d3_139}


def anm_replacement_d3_140(anm_replacement_d2_140):
    feature = _clean(anm_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_140'] = {'inputs': ['anm_replacement_d2_140'], 'func': anm_replacement_d3_140}


def anm_replacement_d3_141(anm_replacement_d2_141):
    feature = _clean(anm_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_141'] = {'inputs': ['anm_replacement_d2_141'], 'func': anm_replacement_d3_141}


def anm_replacement_d3_142(anm_replacement_d2_142):
    feature = _clean(anm_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_142'] = {'inputs': ['anm_replacement_d2_142'], 'func': anm_replacement_d3_142}


def anm_replacement_d3_143(anm_replacement_d2_143):
    feature = _clean(anm_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_143'] = {'inputs': ['anm_replacement_d2_143'], 'func': anm_replacement_d3_143}


def anm_replacement_d3_144(anm_replacement_d2_144):
    feature = _clean(anm_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_144'] = {'inputs': ['anm_replacement_d2_144'], 'func': anm_replacement_d3_144}


def anm_replacement_d3_145(anm_replacement_d2_145):
    feature = _clean(anm_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_145'] = {'inputs': ['anm_replacement_d2_145'], 'func': anm_replacement_d3_145}


def anm_replacement_d3_146(anm_replacement_d2_146):
    feature = _clean(anm_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_146'] = {'inputs': ['anm_replacement_d2_146'], 'func': anm_replacement_d3_146}


def anm_replacement_d3_147(anm_replacement_d2_147):
    feature = _clean(anm_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_147'] = {'inputs': ['anm_replacement_d2_147'], 'func': anm_replacement_d3_147}


def anm_replacement_d3_148(anm_replacement_d2_148):
    feature = _clean(anm_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_148'] = {'inputs': ['anm_replacement_d2_148'], 'func': anm_replacement_d3_148}


def anm_replacement_d3_149(anm_replacement_d2_149):
    feature = _clean(anm_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_149'] = {'inputs': ['anm_replacement_d2_149'], 'func': anm_replacement_d3_149}


def anm_replacement_d3_150(anm_replacement_d2_150):
    feature = _clean(anm_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_150'] = {'inputs': ['anm_replacement_d2_150'], 'func': anm_replacement_d3_150}


def anm_replacement_d3_151(anm_replacement_d2_151):
    feature = _clean(anm_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_151'] = {'inputs': ['anm_replacement_d2_151'], 'func': anm_replacement_d3_151}


def anm_replacement_d3_152(anm_replacement_d2_152):
    feature = _clean(anm_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_152'] = {'inputs': ['anm_replacement_d2_152'], 'func': anm_replacement_d3_152}


def anm_replacement_d3_153(anm_replacement_d2_153):
    feature = _clean(anm_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_153'] = {'inputs': ['anm_replacement_d2_153'], 'func': anm_replacement_d3_153}


def anm_replacement_d3_154(anm_replacement_d2_154):
    feature = _clean(anm_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_154'] = {'inputs': ['anm_replacement_d2_154'], 'func': anm_replacement_d3_154}


def anm_replacement_d3_155(anm_replacement_d2_155):
    feature = _clean(anm_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_155'] = {'inputs': ['anm_replacement_d2_155'], 'func': anm_replacement_d3_155}


def anm_replacement_d3_156(anm_replacement_d2_156):
    feature = _clean(anm_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_156'] = {'inputs': ['anm_replacement_d2_156'], 'func': anm_replacement_d3_156}


def anm_replacement_d3_157(anm_replacement_d2_157):
    feature = _clean(anm_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_157'] = {'inputs': ['anm_replacement_d2_157'], 'func': anm_replacement_d3_157}


def anm_replacement_d3_158(anm_replacement_d2_158):
    feature = _clean(anm_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_158'] = {'inputs': ['anm_replacement_d2_158'], 'func': anm_replacement_d3_158}


def anm_replacement_d3_159(anm_replacement_d2_159):
    feature = _clean(anm_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_159'] = {'inputs': ['anm_replacement_d2_159'], 'func': anm_replacement_d3_159}


def anm_replacement_d3_160(anm_replacement_d2_160):
    feature = _clean(anm_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_160'] = {'inputs': ['anm_replacement_d2_160'], 'func': anm_replacement_d3_160}


def anm_replacement_d3_161(anm_replacement_d2_161):
    feature = _clean(anm_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_161'] = {'inputs': ['anm_replacement_d2_161'], 'func': anm_replacement_d3_161}


def anm_replacement_d3_162(anm_replacement_d2_162):
    feature = _clean(anm_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_162'] = {'inputs': ['anm_replacement_d2_162'], 'func': anm_replacement_d3_162}


def anm_replacement_d3_163(anm_replacement_d2_163):
    feature = _clean(anm_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_163'] = {'inputs': ['anm_replacement_d2_163'], 'func': anm_replacement_d3_163}


def anm_replacement_d3_164(anm_replacement_d2_164):
    feature = _clean(anm_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_164'] = {'inputs': ['anm_replacement_d2_164'], 'func': anm_replacement_d3_164}


def anm_replacement_d3_165(anm_replacement_d2_165):
    feature = _clean(anm_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_165'] = {'inputs': ['anm_replacement_d2_165'], 'func': anm_replacement_d3_165}


def anm_replacement_d3_166(anm_replacement_d2_166):
    feature = _clean(anm_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_166'] = {'inputs': ['anm_replacement_d2_166'], 'func': anm_replacement_d3_166}


def anm_replacement_d3_167(anm_replacement_d2_167):
    feature = _clean(anm_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_167'] = {'inputs': ['anm_replacement_d2_167'], 'func': anm_replacement_d3_167}


def anm_replacement_d3_168(anm_replacement_d2_168):
    feature = _clean(anm_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_168'] = {'inputs': ['anm_replacement_d2_168'], 'func': anm_replacement_d3_168}


def anm_replacement_d3_169(anm_replacement_d2_169):
    feature = _clean(anm_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_169'] = {'inputs': ['anm_replacement_d2_169'], 'func': anm_replacement_d3_169}


def anm_replacement_d3_170(anm_replacement_d2_170):
    feature = _clean(anm_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_170'] = {'inputs': ['anm_replacement_d2_170'], 'func': anm_replacement_d3_170}


def anm_replacement_d3_171(anm_replacement_d2_171):
    feature = _clean(anm_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_171'] = {'inputs': ['anm_replacement_d2_171'], 'func': anm_replacement_d3_171}


def anm_replacement_d3_172(anm_replacement_d2_172):
    feature = _clean(anm_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_172'] = {'inputs': ['anm_replacement_d2_172'], 'func': anm_replacement_d3_172}


def anm_replacement_d3_173(anm_replacement_d2_173):
    feature = _clean(anm_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_173'] = {'inputs': ['anm_replacement_d2_173'], 'func': anm_replacement_d3_173}


def anm_replacement_d3_174(anm_replacement_d2_174):
    feature = _clean(anm_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_174'] = {'inputs': ['anm_replacement_d2_174'], 'func': anm_replacement_d3_174}


def anm_replacement_d3_175(anm_replacement_d2_175):
    feature = _clean(anm_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
ANM_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['anm_replacement_d3_175'] = {'inputs': ['anm_replacement_d2_175'], 'func': anm_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def atr_base_universe_d3_001_atr_002_range_expansion_10_002(atr_base_universe_d2_001_atr_002_range_expansion_10_002):
    return _base_universe_d3(atr_base_universe_d2_001_atr_002_range_expansion_10_002, 1)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_001_atr_002_range_expansion_10_002'] = {'inputs': ['atr_base_universe_d2_001_atr_002_range_expansion_10_002'], 'func': atr_base_universe_d3_001_atr_002_range_expansion_10_002}


def atr_base_universe_d3_002_atr_004_close_location_42_004(atr_base_universe_d2_002_atr_004_close_location_42_004):
    return _base_universe_d3(atr_base_universe_d2_002_atr_004_close_location_42_004, 2)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_002_atr_004_close_location_42_004'] = {'inputs': ['atr_base_universe_d2_002_atr_004_close_location_42_004'], 'func': atr_base_universe_d3_002_atr_004_close_location_42_004}


def atr_base_universe_d3_003_atr_005_atr_move_63_005(atr_base_universe_d2_003_atr_005_atr_move_63_005):
    return _base_universe_d3(atr_base_universe_d2_003_atr_005_atr_move_63_005, 3)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_003_atr_005_atr_move_63_005'] = {'inputs': ['atr_base_universe_d2_003_atr_005_atr_move_63_005'], 'func': atr_base_universe_d3_003_atr_005_atr_move_63_005}


def atr_base_universe_d3_004_atr_008_range_expansion_189_008(atr_base_universe_d2_004_atr_008_range_expansion_189_008):
    return _base_universe_d3(atr_base_universe_d2_004_atr_008_range_expansion_189_008, 4)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_004_atr_008_range_expansion_189_008'] = {'inputs': ['atr_base_universe_d2_004_atr_008_range_expansion_189_008'], 'func': atr_base_universe_d3_004_atr_008_range_expansion_189_008}


def atr_base_universe_d3_005_atr_010_close_location_378_010(atr_base_universe_d2_005_atr_010_close_location_378_010):
    return _base_universe_d3(atr_base_universe_d2_005_atr_010_close_location_378_010, 5)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_005_atr_010_close_location_378_010'] = {'inputs': ['atr_base_universe_d2_005_atr_010_close_location_378_010'], 'func': atr_base_universe_d3_005_atr_010_close_location_378_010}


def atr_base_universe_d3_006_atr_011_atr_move_504_011(atr_base_universe_d2_006_atr_011_atr_move_504_011):
    return _base_universe_d3(atr_base_universe_d2_006_atr_011_atr_move_504_011, 6)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_006_atr_011_atr_move_504_011'] = {'inputs': ['atr_base_universe_d2_006_atr_011_atr_move_504_011'], 'func': atr_base_universe_d3_006_atr_011_atr_move_504_011}


def atr_base_universe_d3_007_atr_014_range_expansion_1260_014(atr_base_universe_d2_007_atr_014_range_expansion_1260_014):
    return _base_universe_d3(atr_base_universe_d2_007_atr_014_range_expansion_1260_014, 7)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_007_atr_014_range_expansion_1260_014'] = {'inputs': ['atr_base_universe_d2_007_atr_014_range_expansion_1260_014'], 'func': atr_base_universe_d3_007_atr_014_range_expansion_1260_014}


def atr_base_universe_d3_008_atr_016_close_location_5_016(atr_base_universe_d2_008_atr_016_close_location_5_016):
    return _base_universe_d3(atr_base_universe_d2_008_atr_016_close_location_5_016, 8)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_008_atr_016_close_location_5_016'] = {'inputs': ['atr_base_universe_d2_008_atr_016_close_location_5_016'], 'func': atr_base_universe_d3_008_atr_016_close_location_5_016}


def atr_base_universe_d3_009_atr_017_atr_move_10_017(atr_base_universe_d2_009_atr_017_atr_move_10_017):
    return _base_universe_d3(atr_base_universe_d2_009_atr_017_atr_move_10_017, 9)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_009_atr_017_atr_move_10_017'] = {'inputs': ['atr_base_universe_d2_009_atr_017_atr_move_10_017'], 'func': atr_base_universe_d3_009_atr_017_atr_move_10_017}


def atr_base_universe_d3_010_atr_020_range_expansion_63_020(atr_base_universe_d2_010_atr_020_range_expansion_63_020):
    return _base_universe_d3(atr_base_universe_d2_010_atr_020_range_expansion_63_020, 10)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_010_atr_020_range_expansion_63_020'] = {'inputs': ['atr_base_universe_d2_010_atr_020_range_expansion_63_020'], 'func': atr_base_universe_d3_010_atr_020_range_expansion_63_020}


def atr_base_universe_d3_011_atr_022_close_location_126_022(atr_base_universe_d2_011_atr_022_close_location_126_022):
    return _base_universe_d3(atr_base_universe_d2_011_atr_022_close_location_126_022, 11)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_011_atr_022_close_location_126_022'] = {'inputs': ['atr_base_universe_d2_011_atr_022_close_location_126_022'], 'func': atr_base_universe_d3_011_atr_022_close_location_126_022}


def atr_base_universe_d3_012_atr_023_atr_move_189_023(atr_base_universe_d2_012_atr_023_atr_move_189_023):
    return _base_universe_d3(atr_base_universe_d2_012_atr_023_atr_move_189_023, 12)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_012_atr_023_atr_move_189_023'] = {'inputs': ['atr_base_universe_d2_012_atr_023_atr_move_189_023'], 'func': atr_base_universe_d3_012_atr_023_atr_move_189_023}


def atr_base_universe_d3_013_atr_026_range_expansion_504_026(atr_base_universe_d2_013_atr_026_range_expansion_504_026):
    return _base_universe_d3(atr_base_universe_d2_013_atr_026_range_expansion_504_026, 13)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_013_atr_026_range_expansion_504_026'] = {'inputs': ['atr_base_universe_d2_013_atr_026_range_expansion_504_026'], 'func': atr_base_universe_d3_013_atr_026_range_expansion_504_026}


def atr_base_universe_d3_014_atr_028_close_location_1008_028(atr_base_universe_d2_014_atr_028_close_location_1008_028):
    return _base_universe_d3(atr_base_universe_d2_014_atr_028_close_location_1008_028, 14)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_014_atr_028_close_location_1008_028'] = {'inputs': ['atr_base_universe_d2_014_atr_028_close_location_1008_028'], 'func': atr_base_universe_d3_014_atr_028_close_location_1008_028}


def atr_base_universe_d3_015_atr_029_atr_move_1260_029(atr_base_universe_d2_015_atr_029_atr_move_1260_029):
    return _base_universe_d3(atr_base_universe_d2_015_atr_029_atr_move_1260_029, 15)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_015_atr_029_atr_move_1260_029'] = {'inputs': ['atr_base_universe_d2_015_atr_029_atr_move_1260_029'], 'func': atr_base_universe_d3_015_atr_029_atr_move_1260_029}


def atr_base_universe_d3_016_atr_basefill_001(atr_base_universe_d2_016_atr_basefill_001):
    return _base_universe_d3(atr_base_universe_d2_016_atr_basefill_001, 16)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_016_atr_basefill_001'] = {'inputs': ['atr_base_universe_d2_016_atr_basefill_001'], 'func': atr_base_universe_d3_016_atr_basefill_001}


def atr_base_universe_d3_017_atr_basefill_003(atr_base_universe_d2_017_atr_basefill_003):
    return _base_universe_d3(atr_base_universe_d2_017_atr_basefill_003, 17)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_017_atr_basefill_003'] = {'inputs': ['atr_base_universe_d2_017_atr_basefill_003'], 'func': atr_base_universe_d3_017_atr_basefill_003}


def atr_base_universe_d3_018_atr_basefill_006(atr_base_universe_d2_018_atr_basefill_006):
    return _base_universe_d3(atr_base_universe_d2_018_atr_basefill_006, 18)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_018_atr_basefill_006'] = {'inputs': ['atr_base_universe_d2_018_atr_basefill_006'], 'func': atr_base_universe_d3_018_atr_basefill_006}


def atr_base_universe_d3_019_atr_basefill_007(atr_base_universe_d2_019_atr_basefill_007):
    return _base_universe_d3(atr_base_universe_d2_019_atr_basefill_007, 19)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_019_atr_basefill_007'] = {'inputs': ['atr_base_universe_d2_019_atr_basefill_007'], 'func': atr_base_universe_d3_019_atr_basefill_007}


def atr_base_universe_d3_020_atr_basefill_009(atr_base_universe_d2_020_atr_basefill_009):
    return _base_universe_d3(atr_base_universe_d2_020_atr_basefill_009, 20)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_020_atr_basefill_009'] = {'inputs': ['atr_base_universe_d2_020_atr_basefill_009'], 'func': atr_base_universe_d3_020_atr_basefill_009}


def atr_base_universe_d3_021_atr_basefill_012(atr_base_universe_d2_021_atr_basefill_012):
    return _base_universe_d3(atr_base_universe_d2_021_atr_basefill_012, 21)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_021_atr_basefill_012'] = {'inputs': ['atr_base_universe_d2_021_atr_basefill_012'], 'func': atr_base_universe_d3_021_atr_basefill_012}


def atr_base_universe_d3_022_atr_basefill_013(atr_base_universe_d2_022_atr_basefill_013):
    return _base_universe_d3(atr_base_universe_d2_022_atr_basefill_013, 22)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_022_atr_basefill_013'] = {'inputs': ['atr_base_universe_d2_022_atr_basefill_013'], 'func': atr_base_universe_d3_022_atr_basefill_013}


def atr_base_universe_d3_023_atr_basefill_015(atr_base_universe_d2_023_atr_basefill_015):
    return _base_universe_d3(atr_base_universe_d2_023_atr_basefill_015, 23)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_023_atr_basefill_015'] = {'inputs': ['atr_base_universe_d2_023_atr_basefill_015'], 'func': atr_base_universe_d3_023_atr_basefill_015}


def atr_base_universe_d3_024_atr_basefill_018(atr_base_universe_d2_024_atr_basefill_018):
    return _base_universe_d3(atr_base_universe_d2_024_atr_basefill_018, 24)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_024_atr_basefill_018'] = {'inputs': ['atr_base_universe_d2_024_atr_basefill_018'], 'func': atr_base_universe_d3_024_atr_basefill_018}


def atr_base_universe_d3_025_atr_basefill_019(atr_base_universe_d2_025_atr_basefill_019):
    return _base_universe_d3(atr_base_universe_d2_025_atr_basefill_019, 25)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_025_atr_basefill_019'] = {'inputs': ['atr_base_universe_d2_025_atr_basefill_019'], 'func': atr_base_universe_d3_025_atr_basefill_019}


def atr_base_universe_d3_026_atr_basefill_021(atr_base_universe_d2_026_atr_basefill_021):
    return _base_universe_d3(atr_base_universe_d2_026_atr_basefill_021, 26)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_026_atr_basefill_021'] = {'inputs': ['atr_base_universe_d2_026_atr_basefill_021'], 'func': atr_base_universe_d3_026_atr_basefill_021}


def atr_base_universe_d3_027_atr_basefill_024(atr_base_universe_d2_027_atr_basefill_024):
    return _base_universe_d3(atr_base_universe_d2_027_atr_basefill_024, 27)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_027_atr_basefill_024'] = {'inputs': ['atr_base_universe_d2_027_atr_basefill_024'], 'func': atr_base_universe_d3_027_atr_basefill_024}


def atr_base_universe_d3_028_atr_basefill_025(atr_base_universe_d2_028_atr_basefill_025):
    return _base_universe_d3(atr_base_universe_d2_028_atr_basefill_025, 28)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_028_atr_basefill_025'] = {'inputs': ['atr_base_universe_d2_028_atr_basefill_025'], 'func': atr_base_universe_d3_028_atr_basefill_025}


def atr_base_universe_d3_029_atr_basefill_027(atr_base_universe_d2_029_atr_basefill_027):
    return _base_universe_d3(atr_base_universe_d2_029_atr_basefill_027, 29)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_029_atr_basefill_027'] = {'inputs': ['atr_base_universe_d2_029_atr_basefill_027'], 'func': atr_base_universe_d3_029_atr_basefill_027}


def atr_base_universe_d3_030_atr_basefill_030(atr_base_universe_d2_030_atr_basefill_030):
    return _base_universe_d3(atr_base_universe_d2_030_atr_basefill_030, 30)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_030_atr_basefill_030'] = {'inputs': ['atr_base_universe_d2_030_atr_basefill_030'], 'func': atr_base_universe_d3_030_atr_basefill_030}


def atr_base_universe_d3_031_atr_basefill_031(atr_base_universe_d2_031_atr_basefill_031):
    return _base_universe_d3(atr_base_universe_d2_031_atr_basefill_031, 31)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_031_atr_basefill_031'] = {'inputs': ['atr_base_universe_d2_031_atr_basefill_031'], 'func': atr_base_universe_d3_031_atr_basefill_031}


def atr_base_universe_d3_032_atr_basefill_032(atr_base_universe_d2_032_atr_basefill_032):
    return _base_universe_d3(atr_base_universe_d2_032_atr_basefill_032, 32)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_032_atr_basefill_032'] = {'inputs': ['atr_base_universe_d2_032_atr_basefill_032'], 'func': atr_base_universe_d3_032_atr_basefill_032}


def atr_base_universe_d3_033_atr_basefill_033(atr_base_universe_d2_033_atr_basefill_033):
    return _base_universe_d3(atr_base_universe_d2_033_atr_basefill_033, 33)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_033_atr_basefill_033'] = {'inputs': ['atr_base_universe_d2_033_atr_basefill_033'], 'func': atr_base_universe_d3_033_atr_basefill_033}


def atr_base_universe_d3_034_atr_basefill_034(atr_base_universe_d2_034_atr_basefill_034):
    return _base_universe_d3(atr_base_universe_d2_034_atr_basefill_034, 34)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_034_atr_basefill_034'] = {'inputs': ['atr_base_universe_d2_034_atr_basefill_034'], 'func': atr_base_universe_d3_034_atr_basefill_034}


def atr_base_universe_d3_035_atr_basefill_035(atr_base_universe_d2_035_atr_basefill_035):
    return _base_universe_d3(atr_base_universe_d2_035_atr_basefill_035, 35)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_035_atr_basefill_035'] = {'inputs': ['atr_base_universe_d2_035_atr_basefill_035'], 'func': atr_base_universe_d3_035_atr_basefill_035}


def atr_base_universe_d3_036_atr_basefill_036(atr_base_universe_d2_036_atr_basefill_036):
    return _base_universe_d3(atr_base_universe_d2_036_atr_basefill_036, 36)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_036_atr_basefill_036'] = {'inputs': ['atr_base_universe_d2_036_atr_basefill_036'], 'func': atr_base_universe_d3_036_atr_basefill_036}


def atr_base_universe_d3_037_atr_basefill_037(atr_base_universe_d2_037_atr_basefill_037):
    return _base_universe_d3(atr_base_universe_d2_037_atr_basefill_037, 37)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_037_atr_basefill_037'] = {'inputs': ['atr_base_universe_d2_037_atr_basefill_037'], 'func': atr_base_universe_d3_037_atr_basefill_037}


def atr_base_universe_d3_038_atr_basefill_038(atr_base_universe_d2_038_atr_basefill_038):
    return _base_universe_d3(atr_base_universe_d2_038_atr_basefill_038, 38)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_038_atr_basefill_038'] = {'inputs': ['atr_base_universe_d2_038_atr_basefill_038'], 'func': atr_base_universe_d3_038_atr_basefill_038}


def atr_base_universe_d3_039_atr_basefill_039(atr_base_universe_d2_039_atr_basefill_039):
    return _base_universe_d3(atr_base_universe_d2_039_atr_basefill_039, 39)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_039_atr_basefill_039'] = {'inputs': ['atr_base_universe_d2_039_atr_basefill_039'], 'func': atr_base_universe_d3_039_atr_basefill_039}


def atr_base_universe_d3_040_atr_basefill_040(atr_base_universe_d2_040_atr_basefill_040):
    return _base_universe_d3(atr_base_universe_d2_040_atr_basefill_040, 40)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_040_atr_basefill_040'] = {'inputs': ['atr_base_universe_d2_040_atr_basefill_040'], 'func': atr_base_universe_d3_040_atr_basefill_040}


def atr_base_universe_d3_041_atr_basefill_041(atr_base_universe_d2_041_atr_basefill_041):
    return _base_universe_d3(atr_base_universe_d2_041_atr_basefill_041, 41)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_041_atr_basefill_041'] = {'inputs': ['atr_base_universe_d2_041_atr_basefill_041'], 'func': atr_base_universe_d3_041_atr_basefill_041}


def atr_base_universe_d3_042_atr_basefill_042(atr_base_universe_d2_042_atr_basefill_042):
    return _base_universe_d3(atr_base_universe_d2_042_atr_basefill_042, 42)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_042_atr_basefill_042'] = {'inputs': ['atr_base_universe_d2_042_atr_basefill_042'], 'func': atr_base_universe_d3_042_atr_basefill_042}


def atr_base_universe_d3_043_atr_basefill_043(atr_base_universe_d2_043_atr_basefill_043):
    return _base_universe_d3(atr_base_universe_d2_043_atr_basefill_043, 43)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_043_atr_basefill_043'] = {'inputs': ['atr_base_universe_d2_043_atr_basefill_043'], 'func': atr_base_universe_d3_043_atr_basefill_043}


def atr_base_universe_d3_044_atr_basefill_044(atr_base_universe_d2_044_atr_basefill_044):
    return _base_universe_d3(atr_base_universe_d2_044_atr_basefill_044, 44)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_044_atr_basefill_044'] = {'inputs': ['atr_base_universe_d2_044_atr_basefill_044'], 'func': atr_base_universe_d3_044_atr_basefill_044}


def atr_base_universe_d3_045_atr_basefill_045(atr_base_universe_d2_045_atr_basefill_045):
    return _base_universe_d3(atr_base_universe_d2_045_atr_basefill_045, 45)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_045_atr_basefill_045'] = {'inputs': ['atr_base_universe_d2_045_atr_basefill_045'], 'func': atr_base_universe_d3_045_atr_basefill_045}


def atr_base_universe_d3_046_atr_basefill_046(atr_base_universe_d2_046_atr_basefill_046):
    return _base_universe_d3(atr_base_universe_d2_046_atr_basefill_046, 46)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_046_atr_basefill_046'] = {'inputs': ['atr_base_universe_d2_046_atr_basefill_046'], 'func': atr_base_universe_d3_046_atr_basefill_046}


def atr_base_universe_d3_047_atr_basefill_047(atr_base_universe_d2_047_atr_basefill_047):
    return _base_universe_d3(atr_base_universe_d2_047_atr_basefill_047, 47)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_047_atr_basefill_047'] = {'inputs': ['atr_base_universe_d2_047_atr_basefill_047'], 'func': atr_base_universe_d3_047_atr_basefill_047}


def atr_base_universe_d3_048_atr_basefill_048(atr_base_universe_d2_048_atr_basefill_048):
    return _base_universe_d3(atr_base_universe_d2_048_atr_basefill_048, 48)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_048_atr_basefill_048'] = {'inputs': ['atr_base_universe_d2_048_atr_basefill_048'], 'func': atr_base_universe_d3_048_atr_basefill_048}


def atr_base_universe_d3_049_atr_basefill_049(atr_base_universe_d2_049_atr_basefill_049):
    return _base_universe_d3(atr_base_universe_d2_049_atr_basefill_049, 49)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_049_atr_basefill_049'] = {'inputs': ['atr_base_universe_d2_049_atr_basefill_049'], 'func': atr_base_universe_d3_049_atr_basefill_049}


def atr_base_universe_d3_050_atr_basefill_050(atr_base_universe_d2_050_atr_basefill_050):
    return _base_universe_d3(atr_base_universe_d2_050_atr_basefill_050, 50)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_050_atr_basefill_050'] = {'inputs': ['atr_base_universe_d2_050_atr_basefill_050'], 'func': atr_base_universe_d3_050_atr_basefill_050}


def atr_base_universe_d3_051_atr_basefill_051(atr_base_universe_d2_051_atr_basefill_051):
    return _base_universe_d3(atr_base_universe_d2_051_atr_basefill_051, 51)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_051_atr_basefill_051'] = {'inputs': ['atr_base_universe_d2_051_atr_basefill_051'], 'func': atr_base_universe_d3_051_atr_basefill_051}


def atr_base_universe_d3_052_atr_basefill_052(atr_base_universe_d2_052_atr_basefill_052):
    return _base_universe_d3(atr_base_universe_d2_052_atr_basefill_052, 52)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_052_atr_basefill_052'] = {'inputs': ['atr_base_universe_d2_052_atr_basefill_052'], 'func': atr_base_universe_d3_052_atr_basefill_052}


def atr_base_universe_d3_053_atr_basefill_053(atr_base_universe_d2_053_atr_basefill_053):
    return _base_universe_d3(atr_base_universe_d2_053_atr_basefill_053, 53)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_053_atr_basefill_053'] = {'inputs': ['atr_base_universe_d2_053_atr_basefill_053'], 'func': atr_base_universe_d3_053_atr_basefill_053}


def atr_base_universe_d3_054_atr_basefill_054(atr_base_universe_d2_054_atr_basefill_054):
    return _base_universe_d3(atr_base_universe_d2_054_atr_basefill_054, 54)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_054_atr_basefill_054'] = {'inputs': ['atr_base_universe_d2_054_atr_basefill_054'], 'func': atr_base_universe_d3_054_atr_basefill_054}


def atr_base_universe_d3_055_atr_basefill_055(atr_base_universe_d2_055_atr_basefill_055):
    return _base_universe_d3(atr_base_universe_d2_055_atr_basefill_055, 55)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_055_atr_basefill_055'] = {'inputs': ['atr_base_universe_d2_055_atr_basefill_055'], 'func': atr_base_universe_d3_055_atr_basefill_055}


def atr_base_universe_d3_056_atr_basefill_056(atr_base_universe_d2_056_atr_basefill_056):
    return _base_universe_d3(atr_base_universe_d2_056_atr_basefill_056, 56)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_056_atr_basefill_056'] = {'inputs': ['atr_base_universe_d2_056_atr_basefill_056'], 'func': atr_base_universe_d3_056_atr_basefill_056}


def atr_base_universe_d3_057_atr_basefill_057(atr_base_universe_d2_057_atr_basefill_057):
    return _base_universe_d3(atr_base_universe_d2_057_atr_basefill_057, 57)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_057_atr_basefill_057'] = {'inputs': ['atr_base_universe_d2_057_atr_basefill_057'], 'func': atr_base_universe_d3_057_atr_basefill_057}


def atr_base_universe_d3_058_atr_basefill_058(atr_base_universe_d2_058_atr_basefill_058):
    return _base_universe_d3(atr_base_universe_d2_058_atr_basefill_058, 58)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_058_atr_basefill_058'] = {'inputs': ['atr_base_universe_d2_058_atr_basefill_058'], 'func': atr_base_universe_d3_058_atr_basefill_058}


def atr_base_universe_d3_059_atr_basefill_059(atr_base_universe_d2_059_atr_basefill_059):
    return _base_universe_d3(atr_base_universe_d2_059_atr_basefill_059, 59)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_059_atr_basefill_059'] = {'inputs': ['atr_base_universe_d2_059_atr_basefill_059'], 'func': atr_base_universe_d3_059_atr_basefill_059}


def atr_base_universe_d3_060_atr_basefill_060(atr_base_universe_d2_060_atr_basefill_060):
    return _base_universe_d3(atr_base_universe_d2_060_atr_basefill_060, 60)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_060_atr_basefill_060'] = {'inputs': ['atr_base_universe_d2_060_atr_basefill_060'], 'func': atr_base_universe_d3_060_atr_basefill_060}


def atr_base_universe_d3_061_atr_basefill_061(atr_base_universe_d2_061_atr_basefill_061):
    return _base_universe_d3(atr_base_universe_d2_061_atr_basefill_061, 61)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_061_atr_basefill_061'] = {'inputs': ['atr_base_universe_d2_061_atr_basefill_061'], 'func': atr_base_universe_d3_061_atr_basefill_061}


def atr_base_universe_d3_062_atr_basefill_062(atr_base_universe_d2_062_atr_basefill_062):
    return _base_universe_d3(atr_base_universe_d2_062_atr_basefill_062, 62)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_062_atr_basefill_062'] = {'inputs': ['atr_base_universe_d2_062_atr_basefill_062'], 'func': atr_base_universe_d3_062_atr_basefill_062}


def atr_base_universe_d3_063_atr_basefill_063(atr_base_universe_d2_063_atr_basefill_063):
    return _base_universe_d3(atr_base_universe_d2_063_atr_basefill_063, 63)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_063_atr_basefill_063'] = {'inputs': ['atr_base_universe_d2_063_atr_basefill_063'], 'func': atr_base_universe_d3_063_atr_basefill_063}


def atr_base_universe_d3_064_atr_basefill_064(atr_base_universe_d2_064_atr_basefill_064):
    return _base_universe_d3(atr_base_universe_d2_064_atr_basefill_064, 64)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_064_atr_basefill_064'] = {'inputs': ['atr_base_universe_d2_064_atr_basefill_064'], 'func': atr_base_universe_d3_064_atr_basefill_064}


def atr_base_universe_d3_065_atr_basefill_065(atr_base_universe_d2_065_atr_basefill_065):
    return _base_universe_d3(atr_base_universe_d2_065_atr_basefill_065, 65)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_065_atr_basefill_065'] = {'inputs': ['atr_base_universe_d2_065_atr_basefill_065'], 'func': atr_base_universe_d3_065_atr_basefill_065}


def atr_base_universe_d3_066_atr_basefill_066(atr_base_universe_d2_066_atr_basefill_066):
    return _base_universe_d3(atr_base_universe_d2_066_atr_basefill_066, 66)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_066_atr_basefill_066'] = {'inputs': ['atr_base_universe_d2_066_atr_basefill_066'], 'func': atr_base_universe_d3_066_atr_basefill_066}


def atr_base_universe_d3_067_atr_basefill_067(atr_base_universe_d2_067_atr_basefill_067):
    return _base_universe_d3(atr_base_universe_d2_067_atr_basefill_067, 67)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_067_atr_basefill_067'] = {'inputs': ['atr_base_universe_d2_067_atr_basefill_067'], 'func': atr_base_universe_d3_067_atr_basefill_067}


def atr_base_universe_d3_068_atr_basefill_068(atr_base_universe_d2_068_atr_basefill_068):
    return _base_universe_d3(atr_base_universe_d2_068_atr_basefill_068, 68)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_068_atr_basefill_068'] = {'inputs': ['atr_base_universe_d2_068_atr_basefill_068'], 'func': atr_base_universe_d3_068_atr_basefill_068}


def atr_base_universe_d3_069_atr_basefill_069(atr_base_universe_d2_069_atr_basefill_069):
    return _base_universe_d3(atr_base_universe_d2_069_atr_basefill_069, 69)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_069_atr_basefill_069'] = {'inputs': ['atr_base_universe_d2_069_atr_basefill_069'], 'func': atr_base_universe_d3_069_atr_basefill_069}


def atr_base_universe_d3_070_atr_basefill_070(atr_base_universe_d2_070_atr_basefill_070):
    return _base_universe_d3(atr_base_universe_d2_070_atr_basefill_070, 70)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_070_atr_basefill_070'] = {'inputs': ['atr_base_universe_d2_070_atr_basefill_070'], 'func': atr_base_universe_d3_070_atr_basefill_070}


def atr_base_universe_d3_071_atr_basefill_071(atr_base_universe_d2_071_atr_basefill_071):
    return _base_universe_d3(atr_base_universe_d2_071_atr_basefill_071, 71)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_071_atr_basefill_071'] = {'inputs': ['atr_base_universe_d2_071_atr_basefill_071'], 'func': atr_base_universe_d3_071_atr_basefill_071}


def atr_base_universe_d3_072_atr_basefill_072(atr_base_universe_d2_072_atr_basefill_072):
    return _base_universe_d3(atr_base_universe_d2_072_atr_basefill_072, 72)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_072_atr_basefill_072'] = {'inputs': ['atr_base_universe_d2_072_atr_basefill_072'], 'func': atr_base_universe_d3_072_atr_basefill_072}


def atr_base_universe_d3_073_atr_basefill_073(atr_base_universe_d2_073_atr_basefill_073):
    return _base_universe_d3(atr_base_universe_d2_073_atr_basefill_073, 73)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_073_atr_basefill_073'] = {'inputs': ['atr_base_universe_d2_073_atr_basefill_073'], 'func': atr_base_universe_d3_073_atr_basefill_073}


def atr_base_universe_d3_074_atr_basefill_074(atr_base_universe_d2_074_atr_basefill_074):
    return _base_universe_d3(atr_base_universe_d2_074_atr_basefill_074, 74)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_074_atr_basefill_074'] = {'inputs': ['atr_base_universe_d2_074_atr_basefill_074'], 'func': atr_base_universe_d3_074_atr_basefill_074}


def atr_base_universe_d3_075_atr_basefill_075(atr_base_universe_d2_075_atr_basefill_075):
    return _base_universe_d3(atr_base_universe_d2_075_atr_basefill_075, 75)
ATR_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['atr_base_universe_d3_075_atr_basefill_075'] = {'inputs': ['atr_base_universe_d2_075_atr_basefill_075'], 'func': atr_base_universe_d3_075_atr_basefill_075}
