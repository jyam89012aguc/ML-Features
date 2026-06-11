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



def dpe_001_amihud_illiquidity_accel_1(dpe_001_amihud_illiquidity_roc_1):
    feature = _s(dpe_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def dpe_007_amihud_illiquidity_accel_5(dpe_007_amihud_illiquidity_roc_5):
    feature = _s(dpe_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def dpe_013_amihud_illiquidity_accel_42(dpe_013_amihud_illiquidity_roc_42):
    feature = _s(dpe_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def dpe_179_dpe_019_amihud_illiquidity_42_019_accel_126(dpe_154_dpe_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(dpe_154_dpe_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def dpe_180_dpe_025_amihud_illiquidity_378_025_accel_378(dpe_155_dpe_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(dpe_155_dpe_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















DECLINE_PATH_ENTROPY_REGISTRY_3RD_DERIVATIVES = {
    'dpe_001_amihud_illiquidity_accel_1': {'inputs': ['dpe_001_amihud_illiquidity_roc_1'], 'func': dpe_001_amihud_illiquidity_accel_1},
    'dpe_007_amihud_illiquidity_accel_5': {'inputs': ['dpe_007_amihud_illiquidity_roc_5'], 'func': dpe_007_amihud_illiquidity_accel_5},
    'dpe_013_amihud_illiquidity_accel_42': {'inputs': ['dpe_013_amihud_illiquidity_roc_42'], 'func': dpe_013_amihud_illiquidity_accel_42},
    'dpe_179_dpe_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['dpe_154_dpe_019_amihud_illiquidity_42_019_roc_126'], 'func': dpe_179_dpe_019_amihud_illiquidity_42_019_accel_126},
    'dpe_180_dpe_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['dpe_155_dpe_025_amihud_illiquidity_378_025_roc_378'], 'func': dpe_180_dpe_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def dpe_replacement_d3_001(dpe_replacement_d2_001):
    feature = _clean(dpe_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_001'] = {'inputs': ['dpe_replacement_d2_001'], 'func': dpe_replacement_d3_001}


def dpe_replacement_d3_002(dpe_replacement_d2_002):
    feature = _clean(dpe_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_002'] = {'inputs': ['dpe_replacement_d2_002'], 'func': dpe_replacement_d3_002}


def dpe_replacement_d3_003(dpe_replacement_d2_003):
    feature = _clean(dpe_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_003'] = {'inputs': ['dpe_replacement_d2_003'], 'func': dpe_replacement_d3_003}


def dpe_replacement_d3_004(dpe_replacement_d2_004):
    feature = _clean(dpe_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_004'] = {'inputs': ['dpe_replacement_d2_004'], 'func': dpe_replacement_d3_004}


def dpe_replacement_d3_005(dpe_replacement_d2_005):
    feature = _clean(dpe_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_005'] = {'inputs': ['dpe_replacement_d2_005'], 'func': dpe_replacement_d3_005}


def dpe_replacement_d3_006(dpe_replacement_d2_006):
    feature = _clean(dpe_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_006'] = {'inputs': ['dpe_replacement_d2_006'], 'func': dpe_replacement_d3_006}


def dpe_replacement_d3_007(dpe_replacement_d2_007):
    feature = _clean(dpe_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_007'] = {'inputs': ['dpe_replacement_d2_007'], 'func': dpe_replacement_d3_007}


def dpe_replacement_d3_008(dpe_replacement_d2_008):
    feature = _clean(dpe_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_008'] = {'inputs': ['dpe_replacement_d2_008'], 'func': dpe_replacement_d3_008}


def dpe_replacement_d3_009(dpe_replacement_d2_009):
    feature = _clean(dpe_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_009'] = {'inputs': ['dpe_replacement_d2_009'], 'func': dpe_replacement_d3_009}


def dpe_replacement_d3_010(dpe_replacement_d2_010):
    feature = _clean(dpe_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_010'] = {'inputs': ['dpe_replacement_d2_010'], 'func': dpe_replacement_d3_010}


def dpe_replacement_d3_011(dpe_replacement_d2_011):
    feature = _clean(dpe_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_011'] = {'inputs': ['dpe_replacement_d2_011'], 'func': dpe_replacement_d3_011}


def dpe_replacement_d3_012(dpe_replacement_d2_012):
    feature = _clean(dpe_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_012'] = {'inputs': ['dpe_replacement_d2_012'], 'func': dpe_replacement_d3_012}


def dpe_replacement_d3_013(dpe_replacement_d2_013):
    feature = _clean(dpe_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_013'] = {'inputs': ['dpe_replacement_d2_013'], 'func': dpe_replacement_d3_013}


def dpe_replacement_d3_014(dpe_replacement_d2_014):
    feature = _clean(dpe_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_014'] = {'inputs': ['dpe_replacement_d2_014'], 'func': dpe_replacement_d3_014}


def dpe_replacement_d3_015(dpe_replacement_d2_015):
    feature = _clean(dpe_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_015'] = {'inputs': ['dpe_replacement_d2_015'], 'func': dpe_replacement_d3_015}


def dpe_replacement_d3_016(dpe_replacement_d2_016):
    feature = _clean(dpe_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_016'] = {'inputs': ['dpe_replacement_d2_016'], 'func': dpe_replacement_d3_016}


def dpe_replacement_d3_017(dpe_replacement_d2_017):
    feature = _clean(dpe_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_017'] = {'inputs': ['dpe_replacement_d2_017'], 'func': dpe_replacement_d3_017}


def dpe_replacement_d3_018(dpe_replacement_d2_018):
    feature = _clean(dpe_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_018'] = {'inputs': ['dpe_replacement_d2_018'], 'func': dpe_replacement_d3_018}


def dpe_replacement_d3_019(dpe_replacement_d2_019):
    feature = _clean(dpe_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_019'] = {'inputs': ['dpe_replacement_d2_019'], 'func': dpe_replacement_d3_019}


def dpe_replacement_d3_020(dpe_replacement_d2_020):
    feature = _clean(dpe_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_020'] = {'inputs': ['dpe_replacement_d2_020'], 'func': dpe_replacement_d3_020}


def dpe_replacement_d3_021(dpe_replacement_d2_021):
    feature = _clean(dpe_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_021'] = {'inputs': ['dpe_replacement_d2_021'], 'func': dpe_replacement_d3_021}


def dpe_replacement_d3_022(dpe_replacement_d2_022):
    feature = _clean(dpe_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_022'] = {'inputs': ['dpe_replacement_d2_022'], 'func': dpe_replacement_d3_022}


def dpe_replacement_d3_023(dpe_replacement_d2_023):
    feature = _clean(dpe_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_023'] = {'inputs': ['dpe_replacement_d2_023'], 'func': dpe_replacement_d3_023}


def dpe_replacement_d3_024(dpe_replacement_d2_024):
    feature = _clean(dpe_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_024'] = {'inputs': ['dpe_replacement_d2_024'], 'func': dpe_replacement_d3_024}


def dpe_replacement_d3_025(dpe_replacement_d2_025):
    feature = _clean(dpe_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_025'] = {'inputs': ['dpe_replacement_d2_025'], 'func': dpe_replacement_d3_025}


def dpe_replacement_d3_026(dpe_replacement_d2_026):
    feature = _clean(dpe_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_026'] = {'inputs': ['dpe_replacement_d2_026'], 'func': dpe_replacement_d3_026}


def dpe_replacement_d3_027(dpe_replacement_d2_027):
    feature = _clean(dpe_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_027'] = {'inputs': ['dpe_replacement_d2_027'], 'func': dpe_replacement_d3_027}


def dpe_replacement_d3_028(dpe_replacement_d2_028):
    feature = _clean(dpe_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_028'] = {'inputs': ['dpe_replacement_d2_028'], 'func': dpe_replacement_d3_028}


def dpe_replacement_d3_029(dpe_replacement_d2_029):
    feature = _clean(dpe_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_029'] = {'inputs': ['dpe_replacement_d2_029'], 'func': dpe_replacement_d3_029}


def dpe_replacement_d3_030(dpe_replacement_d2_030):
    feature = _clean(dpe_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_030'] = {'inputs': ['dpe_replacement_d2_030'], 'func': dpe_replacement_d3_030}


def dpe_replacement_d3_031(dpe_replacement_d2_031):
    feature = _clean(dpe_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_031'] = {'inputs': ['dpe_replacement_d2_031'], 'func': dpe_replacement_d3_031}


def dpe_replacement_d3_032(dpe_replacement_d2_032):
    feature = _clean(dpe_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_032'] = {'inputs': ['dpe_replacement_d2_032'], 'func': dpe_replacement_d3_032}


def dpe_replacement_d3_033(dpe_replacement_d2_033):
    feature = _clean(dpe_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_033'] = {'inputs': ['dpe_replacement_d2_033'], 'func': dpe_replacement_d3_033}


def dpe_replacement_d3_034(dpe_replacement_d2_034):
    feature = _clean(dpe_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_034'] = {'inputs': ['dpe_replacement_d2_034'], 'func': dpe_replacement_d3_034}


def dpe_replacement_d3_035(dpe_replacement_d2_035):
    feature = _clean(dpe_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_035'] = {'inputs': ['dpe_replacement_d2_035'], 'func': dpe_replacement_d3_035}


def dpe_replacement_d3_036(dpe_replacement_d2_036):
    feature = _clean(dpe_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_036'] = {'inputs': ['dpe_replacement_d2_036'], 'func': dpe_replacement_d3_036}


def dpe_replacement_d3_037(dpe_replacement_d2_037):
    feature = _clean(dpe_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_037'] = {'inputs': ['dpe_replacement_d2_037'], 'func': dpe_replacement_d3_037}


def dpe_replacement_d3_038(dpe_replacement_d2_038):
    feature = _clean(dpe_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_038'] = {'inputs': ['dpe_replacement_d2_038'], 'func': dpe_replacement_d3_038}


def dpe_replacement_d3_039(dpe_replacement_d2_039):
    feature = _clean(dpe_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_039'] = {'inputs': ['dpe_replacement_d2_039'], 'func': dpe_replacement_d3_039}


def dpe_replacement_d3_040(dpe_replacement_d2_040):
    feature = _clean(dpe_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_040'] = {'inputs': ['dpe_replacement_d2_040'], 'func': dpe_replacement_d3_040}


def dpe_replacement_d3_041(dpe_replacement_d2_041):
    feature = _clean(dpe_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_041'] = {'inputs': ['dpe_replacement_d2_041'], 'func': dpe_replacement_d3_041}


def dpe_replacement_d3_042(dpe_replacement_d2_042):
    feature = _clean(dpe_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_042'] = {'inputs': ['dpe_replacement_d2_042'], 'func': dpe_replacement_d3_042}


def dpe_replacement_d3_043(dpe_replacement_d2_043):
    feature = _clean(dpe_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_043'] = {'inputs': ['dpe_replacement_d2_043'], 'func': dpe_replacement_d3_043}


def dpe_replacement_d3_044(dpe_replacement_d2_044):
    feature = _clean(dpe_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_044'] = {'inputs': ['dpe_replacement_d2_044'], 'func': dpe_replacement_d3_044}


def dpe_replacement_d3_045(dpe_replacement_d2_045):
    feature = _clean(dpe_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_045'] = {'inputs': ['dpe_replacement_d2_045'], 'func': dpe_replacement_d3_045}


def dpe_replacement_d3_046(dpe_replacement_d2_046):
    feature = _clean(dpe_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_046'] = {'inputs': ['dpe_replacement_d2_046'], 'func': dpe_replacement_d3_046}


def dpe_replacement_d3_047(dpe_replacement_d2_047):
    feature = _clean(dpe_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_047'] = {'inputs': ['dpe_replacement_d2_047'], 'func': dpe_replacement_d3_047}


def dpe_replacement_d3_048(dpe_replacement_d2_048):
    feature = _clean(dpe_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_048'] = {'inputs': ['dpe_replacement_d2_048'], 'func': dpe_replacement_d3_048}


def dpe_replacement_d3_049(dpe_replacement_d2_049):
    feature = _clean(dpe_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_049'] = {'inputs': ['dpe_replacement_d2_049'], 'func': dpe_replacement_d3_049}


def dpe_replacement_d3_050(dpe_replacement_d2_050):
    feature = _clean(dpe_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_050'] = {'inputs': ['dpe_replacement_d2_050'], 'func': dpe_replacement_d3_050}


def dpe_replacement_d3_051(dpe_replacement_d2_051):
    feature = _clean(dpe_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_051'] = {'inputs': ['dpe_replacement_d2_051'], 'func': dpe_replacement_d3_051}


def dpe_replacement_d3_052(dpe_replacement_d2_052):
    feature = _clean(dpe_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_052'] = {'inputs': ['dpe_replacement_d2_052'], 'func': dpe_replacement_d3_052}


def dpe_replacement_d3_053(dpe_replacement_d2_053):
    feature = _clean(dpe_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_053'] = {'inputs': ['dpe_replacement_d2_053'], 'func': dpe_replacement_d3_053}


def dpe_replacement_d3_054(dpe_replacement_d2_054):
    feature = _clean(dpe_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_054'] = {'inputs': ['dpe_replacement_d2_054'], 'func': dpe_replacement_d3_054}


def dpe_replacement_d3_055(dpe_replacement_d2_055):
    feature = _clean(dpe_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_055'] = {'inputs': ['dpe_replacement_d2_055'], 'func': dpe_replacement_d3_055}


def dpe_replacement_d3_056(dpe_replacement_d2_056):
    feature = _clean(dpe_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_056'] = {'inputs': ['dpe_replacement_d2_056'], 'func': dpe_replacement_d3_056}


def dpe_replacement_d3_057(dpe_replacement_d2_057):
    feature = _clean(dpe_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_057'] = {'inputs': ['dpe_replacement_d2_057'], 'func': dpe_replacement_d3_057}


def dpe_replacement_d3_058(dpe_replacement_d2_058):
    feature = _clean(dpe_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_058'] = {'inputs': ['dpe_replacement_d2_058'], 'func': dpe_replacement_d3_058}


def dpe_replacement_d3_059(dpe_replacement_d2_059):
    feature = _clean(dpe_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_059'] = {'inputs': ['dpe_replacement_d2_059'], 'func': dpe_replacement_d3_059}


def dpe_replacement_d3_060(dpe_replacement_d2_060):
    feature = _clean(dpe_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_060'] = {'inputs': ['dpe_replacement_d2_060'], 'func': dpe_replacement_d3_060}


def dpe_replacement_d3_061(dpe_replacement_d2_061):
    feature = _clean(dpe_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_061'] = {'inputs': ['dpe_replacement_d2_061'], 'func': dpe_replacement_d3_061}


def dpe_replacement_d3_062(dpe_replacement_d2_062):
    feature = _clean(dpe_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_062'] = {'inputs': ['dpe_replacement_d2_062'], 'func': dpe_replacement_d3_062}


def dpe_replacement_d3_063(dpe_replacement_d2_063):
    feature = _clean(dpe_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_063'] = {'inputs': ['dpe_replacement_d2_063'], 'func': dpe_replacement_d3_063}


def dpe_replacement_d3_064(dpe_replacement_d2_064):
    feature = _clean(dpe_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_064'] = {'inputs': ['dpe_replacement_d2_064'], 'func': dpe_replacement_d3_064}


def dpe_replacement_d3_065(dpe_replacement_d2_065):
    feature = _clean(dpe_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_065'] = {'inputs': ['dpe_replacement_d2_065'], 'func': dpe_replacement_d3_065}


def dpe_replacement_d3_066(dpe_replacement_d2_066):
    feature = _clean(dpe_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_066'] = {'inputs': ['dpe_replacement_d2_066'], 'func': dpe_replacement_d3_066}


def dpe_replacement_d3_067(dpe_replacement_d2_067):
    feature = _clean(dpe_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_067'] = {'inputs': ['dpe_replacement_d2_067'], 'func': dpe_replacement_d3_067}


def dpe_replacement_d3_068(dpe_replacement_d2_068):
    feature = _clean(dpe_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_068'] = {'inputs': ['dpe_replacement_d2_068'], 'func': dpe_replacement_d3_068}


def dpe_replacement_d3_069(dpe_replacement_d2_069):
    feature = _clean(dpe_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_069'] = {'inputs': ['dpe_replacement_d2_069'], 'func': dpe_replacement_d3_069}


def dpe_replacement_d3_070(dpe_replacement_d2_070):
    feature = _clean(dpe_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_070'] = {'inputs': ['dpe_replacement_d2_070'], 'func': dpe_replacement_d3_070}


def dpe_replacement_d3_071(dpe_replacement_d2_071):
    feature = _clean(dpe_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_071'] = {'inputs': ['dpe_replacement_d2_071'], 'func': dpe_replacement_d3_071}


def dpe_replacement_d3_072(dpe_replacement_d2_072):
    feature = _clean(dpe_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_072'] = {'inputs': ['dpe_replacement_d2_072'], 'func': dpe_replacement_d3_072}


def dpe_replacement_d3_073(dpe_replacement_d2_073):
    feature = _clean(dpe_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_073'] = {'inputs': ['dpe_replacement_d2_073'], 'func': dpe_replacement_d3_073}


def dpe_replacement_d3_074(dpe_replacement_d2_074):
    feature = _clean(dpe_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_074'] = {'inputs': ['dpe_replacement_d2_074'], 'func': dpe_replacement_d3_074}


def dpe_replacement_d3_075(dpe_replacement_d2_075):
    feature = _clean(dpe_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_075'] = {'inputs': ['dpe_replacement_d2_075'], 'func': dpe_replacement_d3_075}


def dpe_replacement_d3_076(dpe_replacement_d2_076):
    feature = _clean(dpe_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_076'] = {'inputs': ['dpe_replacement_d2_076'], 'func': dpe_replacement_d3_076}


def dpe_replacement_d3_077(dpe_replacement_d2_077):
    feature = _clean(dpe_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_077'] = {'inputs': ['dpe_replacement_d2_077'], 'func': dpe_replacement_d3_077}


def dpe_replacement_d3_078(dpe_replacement_d2_078):
    feature = _clean(dpe_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_078'] = {'inputs': ['dpe_replacement_d2_078'], 'func': dpe_replacement_d3_078}


def dpe_replacement_d3_079(dpe_replacement_d2_079):
    feature = _clean(dpe_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_079'] = {'inputs': ['dpe_replacement_d2_079'], 'func': dpe_replacement_d3_079}


def dpe_replacement_d3_080(dpe_replacement_d2_080):
    feature = _clean(dpe_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_080'] = {'inputs': ['dpe_replacement_d2_080'], 'func': dpe_replacement_d3_080}


def dpe_replacement_d3_081(dpe_replacement_d2_081):
    feature = _clean(dpe_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_081'] = {'inputs': ['dpe_replacement_d2_081'], 'func': dpe_replacement_d3_081}


def dpe_replacement_d3_082(dpe_replacement_d2_082):
    feature = _clean(dpe_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_082'] = {'inputs': ['dpe_replacement_d2_082'], 'func': dpe_replacement_d3_082}


def dpe_replacement_d3_083(dpe_replacement_d2_083):
    feature = _clean(dpe_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_083'] = {'inputs': ['dpe_replacement_d2_083'], 'func': dpe_replacement_d3_083}


def dpe_replacement_d3_084(dpe_replacement_d2_084):
    feature = _clean(dpe_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_084'] = {'inputs': ['dpe_replacement_d2_084'], 'func': dpe_replacement_d3_084}


def dpe_replacement_d3_085(dpe_replacement_d2_085):
    feature = _clean(dpe_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_085'] = {'inputs': ['dpe_replacement_d2_085'], 'func': dpe_replacement_d3_085}


def dpe_replacement_d3_086(dpe_replacement_d2_086):
    feature = _clean(dpe_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_086'] = {'inputs': ['dpe_replacement_d2_086'], 'func': dpe_replacement_d3_086}


def dpe_replacement_d3_087(dpe_replacement_d2_087):
    feature = _clean(dpe_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_087'] = {'inputs': ['dpe_replacement_d2_087'], 'func': dpe_replacement_d3_087}


def dpe_replacement_d3_088(dpe_replacement_d2_088):
    feature = _clean(dpe_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_088'] = {'inputs': ['dpe_replacement_d2_088'], 'func': dpe_replacement_d3_088}


def dpe_replacement_d3_089(dpe_replacement_d2_089):
    feature = _clean(dpe_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_089'] = {'inputs': ['dpe_replacement_d2_089'], 'func': dpe_replacement_d3_089}


def dpe_replacement_d3_090(dpe_replacement_d2_090):
    feature = _clean(dpe_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_090'] = {'inputs': ['dpe_replacement_d2_090'], 'func': dpe_replacement_d3_090}


def dpe_replacement_d3_091(dpe_replacement_d2_091):
    feature = _clean(dpe_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_091'] = {'inputs': ['dpe_replacement_d2_091'], 'func': dpe_replacement_d3_091}


def dpe_replacement_d3_092(dpe_replacement_d2_092):
    feature = _clean(dpe_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_092'] = {'inputs': ['dpe_replacement_d2_092'], 'func': dpe_replacement_d3_092}


def dpe_replacement_d3_093(dpe_replacement_d2_093):
    feature = _clean(dpe_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_093'] = {'inputs': ['dpe_replacement_d2_093'], 'func': dpe_replacement_d3_093}


def dpe_replacement_d3_094(dpe_replacement_d2_094):
    feature = _clean(dpe_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_094'] = {'inputs': ['dpe_replacement_d2_094'], 'func': dpe_replacement_d3_094}


def dpe_replacement_d3_095(dpe_replacement_d2_095):
    feature = _clean(dpe_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_095'] = {'inputs': ['dpe_replacement_d2_095'], 'func': dpe_replacement_d3_095}


def dpe_replacement_d3_096(dpe_replacement_d2_096):
    feature = _clean(dpe_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_096'] = {'inputs': ['dpe_replacement_d2_096'], 'func': dpe_replacement_d3_096}


def dpe_replacement_d3_097(dpe_replacement_d2_097):
    feature = _clean(dpe_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_097'] = {'inputs': ['dpe_replacement_d2_097'], 'func': dpe_replacement_d3_097}


def dpe_replacement_d3_098(dpe_replacement_d2_098):
    feature = _clean(dpe_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_098'] = {'inputs': ['dpe_replacement_d2_098'], 'func': dpe_replacement_d3_098}


def dpe_replacement_d3_099(dpe_replacement_d2_099):
    feature = _clean(dpe_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_099'] = {'inputs': ['dpe_replacement_d2_099'], 'func': dpe_replacement_d3_099}


def dpe_replacement_d3_100(dpe_replacement_d2_100):
    feature = _clean(dpe_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_100'] = {'inputs': ['dpe_replacement_d2_100'], 'func': dpe_replacement_d3_100}


def dpe_replacement_d3_101(dpe_replacement_d2_101):
    feature = _clean(dpe_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_101'] = {'inputs': ['dpe_replacement_d2_101'], 'func': dpe_replacement_d3_101}


def dpe_replacement_d3_102(dpe_replacement_d2_102):
    feature = _clean(dpe_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_102'] = {'inputs': ['dpe_replacement_d2_102'], 'func': dpe_replacement_d3_102}


def dpe_replacement_d3_103(dpe_replacement_d2_103):
    feature = _clean(dpe_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_103'] = {'inputs': ['dpe_replacement_d2_103'], 'func': dpe_replacement_d3_103}


def dpe_replacement_d3_104(dpe_replacement_d2_104):
    feature = _clean(dpe_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_104'] = {'inputs': ['dpe_replacement_d2_104'], 'func': dpe_replacement_d3_104}


def dpe_replacement_d3_105(dpe_replacement_d2_105):
    feature = _clean(dpe_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_105'] = {'inputs': ['dpe_replacement_d2_105'], 'func': dpe_replacement_d3_105}


def dpe_replacement_d3_106(dpe_replacement_d2_106):
    feature = _clean(dpe_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_106'] = {'inputs': ['dpe_replacement_d2_106'], 'func': dpe_replacement_d3_106}


def dpe_replacement_d3_107(dpe_replacement_d2_107):
    feature = _clean(dpe_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_107'] = {'inputs': ['dpe_replacement_d2_107'], 'func': dpe_replacement_d3_107}


def dpe_replacement_d3_108(dpe_replacement_d2_108):
    feature = _clean(dpe_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_108'] = {'inputs': ['dpe_replacement_d2_108'], 'func': dpe_replacement_d3_108}


def dpe_replacement_d3_109(dpe_replacement_d2_109):
    feature = _clean(dpe_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_109'] = {'inputs': ['dpe_replacement_d2_109'], 'func': dpe_replacement_d3_109}


def dpe_replacement_d3_110(dpe_replacement_d2_110):
    feature = _clean(dpe_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_110'] = {'inputs': ['dpe_replacement_d2_110'], 'func': dpe_replacement_d3_110}


def dpe_replacement_d3_111(dpe_replacement_d2_111):
    feature = _clean(dpe_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_111'] = {'inputs': ['dpe_replacement_d2_111'], 'func': dpe_replacement_d3_111}


def dpe_replacement_d3_112(dpe_replacement_d2_112):
    feature = _clean(dpe_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_112'] = {'inputs': ['dpe_replacement_d2_112'], 'func': dpe_replacement_d3_112}


def dpe_replacement_d3_113(dpe_replacement_d2_113):
    feature = _clean(dpe_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_113'] = {'inputs': ['dpe_replacement_d2_113'], 'func': dpe_replacement_d3_113}


def dpe_replacement_d3_114(dpe_replacement_d2_114):
    feature = _clean(dpe_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_114'] = {'inputs': ['dpe_replacement_d2_114'], 'func': dpe_replacement_d3_114}


def dpe_replacement_d3_115(dpe_replacement_d2_115):
    feature = _clean(dpe_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_115'] = {'inputs': ['dpe_replacement_d2_115'], 'func': dpe_replacement_d3_115}


def dpe_replacement_d3_116(dpe_replacement_d2_116):
    feature = _clean(dpe_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_116'] = {'inputs': ['dpe_replacement_d2_116'], 'func': dpe_replacement_d3_116}


def dpe_replacement_d3_117(dpe_replacement_d2_117):
    feature = _clean(dpe_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_117'] = {'inputs': ['dpe_replacement_d2_117'], 'func': dpe_replacement_d3_117}


def dpe_replacement_d3_118(dpe_replacement_d2_118):
    feature = _clean(dpe_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_118'] = {'inputs': ['dpe_replacement_d2_118'], 'func': dpe_replacement_d3_118}


def dpe_replacement_d3_119(dpe_replacement_d2_119):
    feature = _clean(dpe_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_119'] = {'inputs': ['dpe_replacement_d2_119'], 'func': dpe_replacement_d3_119}


def dpe_replacement_d3_120(dpe_replacement_d2_120):
    feature = _clean(dpe_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_120'] = {'inputs': ['dpe_replacement_d2_120'], 'func': dpe_replacement_d3_120}


def dpe_replacement_d3_121(dpe_replacement_d2_121):
    feature = _clean(dpe_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_121'] = {'inputs': ['dpe_replacement_d2_121'], 'func': dpe_replacement_d3_121}


def dpe_replacement_d3_122(dpe_replacement_d2_122):
    feature = _clean(dpe_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_122'] = {'inputs': ['dpe_replacement_d2_122'], 'func': dpe_replacement_d3_122}


def dpe_replacement_d3_123(dpe_replacement_d2_123):
    feature = _clean(dpe_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_123'] = {'inputs': ['dpe_replacement_d2_123'], 'func': dpe_replacement_d3_123}


def dpe_replacement_d3_124(dpe_replacement_d2_124):
    feature = _clean(dpe_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_124'] = {'inputs': ['dpe_replacement_d2_124'], 'func': dpe_replacement_d3_124}


def dpe_replacement_d3_125(dpe_replacement_d2_125):
    feature = _clean(dpe_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_125'] = {'inputs': ['dpe_replacement_d2_125'], 'func': dpe_replacement_d3_125}


def dpe_replacement_d3_126(dpe_replacement_d2_126):
    feature = _clean(dpe_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_126'] = {'inputs': ['dpe_replacement_d2_126'], 'func': dpe_replacement_d3_126}


def dpe_replacement_d3_127(dpe_replacement_d2_127):
    feature = _clean(dpe_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_127'] = {'inputs': ['dpe_replacement_d2_127'], 'func': dpe_replacement_d3_127}


def dpe_replacement_d3_128(dpe_replacement_d2_128):
    feature = _clean(dpe_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_128'] = {'inputs': ['dpe_replacement_d2_128'], 'func': dpe_replacement_d3_128}


def dpe_replacement_d3_129(dpe_replacement_d2_129):
    feature = _clean(dpe_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_129'] = {'inputs': ['dpe_replacement_d2_129'], 'func': dpe_replacement_d3_129}


def dpe_replacement_d3_130(dpe_replacement_d2_130):
    feature = _clean(dpe_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_130'] = {'inputs': ['dpe_replacement_d2_130'], 'func': dpe_replacement_d3_130}


def dpe_replacement_d3_131(dpe_replacement_d2_131):
    feature = _clean(dpe_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_131'] = {'inputs': ['dpe_replacement_d2_131'], 'func': dpe_replacement_d3_131}


def dpe_replacement_d3_132(dpe_replacement_d2_132):
    feature = _clean(dpe_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_132'] = {'inputs': ['dpe_replacement_d2_132'], 'func': dpe_replacement_d3_132}


def dpe_replacement_d3_133(dpe_replacement_d2_133):
    feature = _clean(dpe_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_133'] = {'inputs': ['dpe_replacement_d2_133'], 'func': dpe_replacement_d3_133}


def dpe_replacement_d3_134(dpe_replacement_d2_134):
    feature = _clean(dpe_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_134'] = {'inputs': ['dpe_replacement_d2_134'], 'func': dpe_replacement_d3_134}


def dpe_replacement_d3_135(dpe_replacement_d2_135):
    feature = _clean(dpe_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_135'] = {'inputs': ['dpe_replacement_d2_135'], 'func': dpe_replacement_d3_135}


def dpe_replacement_d3_136(dpe_replacement_d2_136):
    feature = _clean(dpe_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_136'] = {'inputs': ['dpe_replacement_d2_136'], 'func': dpe_replacement_d3_136}


def dpe_replacement_d3_137(dpe_replacement_d2_137):
    feature = _clean(dpe_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_137'] = {'inputs': ['dpe_replacement_d2_137'], 'func': dpe_replacement_d3_137}


def dpe_replacement_d3_138(dpe_replacement_d2_138):
    feature = _clean(dpe_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_138'] = {'inputs': ['dpe_replacement_d2_138'], 'func': dpe_replacement_d3_138}


def dpe_replacement_d3_139(dpe_replacement_d2_139):
    feature = _clean(dpe_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_139'] = {'inputs': ['dpe_replacement_d2_139'], 'func': dpe_replacement_d3_139}


def dpe_replacement_d3_140(dpe_replacement_d2_140):
    feature = _clean(dpe_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_140'] = {'inputs': ['dpe_replacement_d2_140'], 'func': dpe_replacement_d3_140}


def dpe_replacement_d3_141(dpe_replacement_d2_141):
    feature = _clean(dpe_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_141'] = {'inputs': ['dpe_replacement_d2_141'], 'func': dpe_replacement_d3_141}


def dpe_replacement_d3_142(dpe_replacement_d2_142):
    feature = _clean(dpe_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_142'] = {'inputs': ['dpe_replacement_d2_142'], 'func': dpe_replacement_d3_142}


def dpe_replacement_d3_143(dpe_replacement_d2_143):
    feature = _clean(dpe_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_143'] = {'inputs': ['dpe_replacement_d2_143'], 'func': dpe_replacement_d3_143}


def dpe_replacement_d3_144(dpe_replacement_d2_144):
    feature = _clean(dpe_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_144'] = {'inputs': ['dpe_replacement_d2_144'], 'func': dpe_replacement_d3_144}


def dpe_replacement_d3_145(dpe_replacement_d2_145):
    feature = _clean(dpe_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_145'] = {'inputs': ['dpe_replacement_d2_145'], 'func': dpe_replacement_d3_145}


def dpe_replacement_d3_146(dpe_replacement_d2_146):
    feature = _clean(dpe_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_146'] = {'inputs': ['dpe_replacement_d2_146'], 'func': dpe_replacement_d3_146}


def dpe_replacement_d3_147(dpe_replacement_d2_147):
    feature = _clean(dpe_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_147'] = {'inputs': ['dpe_replacement_d2_147'], 'func': dpe_replacement_d3_147}


def dpe_replacement_d3_148(dpe_replacement_d2_148):
    feature = _clean(dpe_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_148'] = {'inputs': ['dpe_replacement_d2_148'], 'func': dpe_replacement_d3_148}


def dpe_replacement_d3_149(dpe_replacement_d2_149):
    feature = _clean(dpe_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_149'] = {'inputs': ['dpe_replacement_d2_149'], 'func': dpe_replacement_d3_149}


def dpe_replacement_d3_150(dpe_replacement_d2_150):
    feature = _clean(dpe_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_150'] = {'inputs': ['dpe_replacement_d2_150'], 'func': dpe_replacement_d3_150}


def dpe_replacement_d3_151(dpe_replacement_d2_151):
    feature = _clean(dpe_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_151'] = {'inputs': ['dpe_replacement_d2_151'], 'func': dpe_replacement_d3_151}


def dpe_replacement_d3_152(dpe_replacement_d2_152):
    feature = _clean(dpe_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_152'] = {'inputs': ['dpe_replacement_d2_152'], 'func': dpe_replacement_d3_152}


def dpe_replacement_d3_153(dpe_replacement_d2_153):
    feature = _clean(dpe_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_153'] = {'inputs': ['dpe_replacement_d2_153'], 'func': dpe_replacement_d3_153}


def dpe_replacement_d3_154(dpe_replacement_d2_154):
    feature = _clean(dpe_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_154'] = {'inputs': ['dpe_replacement_d2_154'], 'func': dpe_replacement_d3_154}


def dpe_replacement_d3_155(dpe_replacement_d2_155):
    feature = _clean(dpe_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_155'] = {'inputs': ['dpe_replacement_d2_155'], 'func': dpe_replacement_d3_155}


def dpe_replacement_d3_156(dpe_replacement_d2_156):
    feature = _clean(dpe_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_156'] = {'inputs': ['dpe_replacement_d2_156'], 'func': dpe_replacement_d3_156}


def dpe_replacement_d3_157(dpe_replacement_d2_157):
    feature = _clean(dpe_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_157'] = {'inputs': ['dpe_replacement_d2_157'], 'func': dpe_replacement_d3_157}


def dpe_replacement_d3_158(dpe_replacement_d2_158):
    feature = _clean(dpe_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_158'] = {'inputs': ['dpe_replacement_d2_158'], 'func': dpe_replacement_d3_158}


def dpe_replacement_d3_159(dpe_replacement_d2_159):
    feature = _clean(dpe_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_159'] = {'inputs': ['dpe_replacement_d2_159'], 'func': dpe_replacement_d3_159}


def dpe_replacement_d3_160(dpe_replacement_d2_160):
    feature = _clean(dpe_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_160'] = {'inputs': ['dpe_replacement_d2_160'], 'func': dpe_replacement_d3_160}


def dpe_replacement_d3_161(dpe_replacement_d2_161):
    feature = _clean(dpe_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_161'] = {'inputs': ['dpe_replacement_d2_161'], 'func': dpe_replacement_d3_161}


def dpe_replacement_d3_162(dpe_replacement_d2_162):
    feature = _clean(dpe_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_162'] = {'inputs': ['dpe_replacement_d2_162'], 'func': dpe_replacement_d3_162}


def dpe_replacement_d3_163(dpe_replacement_d2_163):
    feature = _clean(dpe_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_163'] = {'inputs': ['dpe_replacement_d2_163'], 'func': dpe_replacement_d3_163}


def dpe_replacement_d3_164(dpe_replacement_d2_164):
    feature = _clean(dpe_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_164'] = {'inputs': ['dpe_replacement_d2_164'], 'func': dpe_replacement_d3_164}


def dpe_replacement_d3_165(dpe_replacement_d2_165):
    feature = _clean(dpe_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_165'] = {'inputs': ['dpe_replacement_d2_165'], 'func': dpe_replacement_d3_165}


def dpe_replacement_d3_166(dpe_replacement_d2_166):
    feature = _clean(dpe_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_166'] = {'inputs': ['dpe_replacement_d2_166'], 'func': dpe_replacement_d3_166}


def dpe_replacement_d3_167(dpe_replacement_d2_167):
    feature = _clean(dpe_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_167'] = {'inputs': ['dpe_replacement_d2_167'], 'func': dpe_replacement_d3_167}


def dpe_replacement_d3_168(dpe_replacement_d2_168):
    feature = _clean(dpe_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_168'] = {'inputs': ['dpe_replacement_d2_168'], 'func': dpe_replacement_d3_168}


def dpe_replacement_d3_169(dpe_replacement_d2_169):
    feature = _clean(dpe_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_169'] = {'inputs': ['dpe_replacement_d2_169'], 'func': dpe_replacement_d3_169}


def dpe_replacement_d3_170(dpe_replacement_d2_170):
    feature = _clean(dpe_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
DPE_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['dpe_replacement_d3_170'] = {'inputs': ['dpe_replacement_d2_170'], 'func': dpe_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dpe_base_universe_d3_001_dpe_002_zero_volume_frequency_10_002(dpe_base_universe_d2_001_dpe_002_zero_volume_frequency_10_002):
    return _base_universe_d3(dpe_base_universe_d2_001_dpe_002_zero_volume_frequency_10_002, 1)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_001_dpe_002_zero_volume_frequency_10_002'] = {'inputs': ['dpe_base_universe_d2_001_dpe_002_zero_volume_frequency_10_002'], 'func': dpe_base_universe_d3_001_dpe_002_zero_volume_frequency_10_002}


def dpe_base_universe_d3_002_dpe_003_spread_proxy_21_003(dpe_base_universe_d2_002_dpe_003_spread_proxy_21_003):
    return _base_universe_d3(dpe_base_universe_d2_002_dpe_003_spread_proxy_21_003, 2)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_002_dpe_003_spread_proxy_21_003'] = {'inputs': ['dpe_base_universe_d2_002_dpe_003_spread_proxy_21_003'], 'func': dpe_base_universe_d3_002_dpe_003_spread_proxy_21_003}


def dpe_base_universe_d3_003_dpe_004_trading_intensity_42_004(dpe_base_universe_d2_003_dpe_004_trading_intensity_42_004):
    return _base_universe_d3(dpe_base_universe_d2_003_dpe_004_trading_intensity_42_004, 3)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_003_dpe_004_trading_intensity_42_004'] = {'inputs': ['dpe_base_universe_d2_003_dpe_004_trading_intensity_42_004'], 'func': dpe_base_universe_d3_003_dpe_004_trading_intensity_42_004}


def dpe_base_universe_d3_004_dpe_006_price_level_distress_84_006(dpe_base_universe_d2_004_dpe_006_price_level_distress_84_006):
    return _base_universe_d3(dpe_base_universe_d2_004_dpe_006_price_level_distress_84_006, 4)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_004_dpe_006_price_level_distress_84_006'] = {'inputs': ['dpe_base_universe_d2_004_dpe_006_price_level_distress_84_006'], 'func': dpe_base_universe_d3_004_dpe_006_price_level_distress_84_006}


def dpe_base_universe_d3_005_dpe_008_zero_volume_frequency_189_008(dpe_base_universe_d2_005_dpe_008_zero_volume_frequency_189_008):
    return _base_universe_d3(dpe_base_universe_d2_005_dpe_008_zero_volume_frequency_189_008, 5)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_005_dpe_008_zero_volume_frequency_189_008'] = {'inputs': ['dpe_base_universe_d2_005_dpe_008_zero_volume_frequency_189_008'], 'func': dpe_base_universe_d3_005_dpe_008_zero_volume_frequency_189_008}


def dpe_base_universe_d3_006_dpe_009_spread_proxy_252_009(dpe_base_universe_d2_006_dpe_009_spread_proxy_252_009):
    return _base_universe_d3(dpe_base_universe_d2_006_dpe_009_spread_proxy_252_009, 6)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_006_dpe_009_spread_proxy_252_009'] = {'inputs': ['dpe_base_universe_d2_006_dpe_009_spread_proxy_252_009'], 'func': dpe_base_universe_d3_006_dpe_009_spread_proxy_252_009}


def dpe_base_universe_d3_007_dpe_010_trading_intensity_378_010(dpe_base_universe_d2_007_dpe_010_trading_intensity_378_010):
    return _base_universe_d3(dpe_base_universe_d2_007_dpe_010_trading_intensity_378_010, 7)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_007_dpe_010_trading_intensity_378_010'] = {'inputs': ['dpe_base_universe_d2_007_dpe_010_trading_intensity_378_010'], 'func': dpe_base_universe_d3_007_dpe_010_trading_intensity_378_010}


def dpe_base_universe_d3_008_dpe_012_price_level_distress_756_012(dpe_base_universe_d2_008_dpe_012_price_level_distress_756_012):
    return _base_universe_d3(dpe_base_universe_d2_008_dpe_012_price_level_distress_756_012, 8)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_008_dpe_012_price_level_distress_756_012'] = {'inputs': ['dpe_base_universe_d2_008_dpe_012_price_level_distress_756_012'], 'func': dpe_base_universe_d3_008_dpe_012_price_level_distress_756_012}


def dpe_base_universe_d3_009_dpe_014_zero_volume_frequency_1260_014(dpe_base_universe_d2_009_dpe_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(dpe_base_universe_d2_009_dpe_014_zero_volume_frequency_1260_014, 9)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_009_dpe_014_zero_volume_frequency_1260_014'] = {'inputs': ['dpe_base_universe_d2_009_dpe_014_zero_volume_frequency_1260_014'], 'func': dpe_base_universe_d3_009_dpe_014_zero_volume_frequency_1260_014}


def dpe_base_universe_d3_010_dpe_015_spread_proxy_1512_015(dpe_base_universe_d2_010_dpe_015_spread_proxy_1512_015):
    return _base_universe_d3(dpe_base_universe_d2_010_dpe_015_spread_proxy_1512_015, 10)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_010_dpe_015_spread_proxy_1512_015'] = {'inputs': ['dpe_base_universe_d2_010_dpe_015_spread_proxy_1512_015'], 'func': dpe_base_universe_d3_010_dpe_015_spread_proxy_1512_015}


def dpe_base_universe_d3_011_dpe_016_trading_intensity_5_016(dpe_base_universe_d2_011_dpe_016_trading_intensity_5_016):
    return _base_universe_d3(dpe_base_universe_d2_011_dpe_016_trading_intensity_5_016, 11)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_011_dpe_016_trading_intensity_5_016'] = {'inputs': ['dpe_base_universe_d2_011_dpe_016_trading_intensity_5_016'], 'func': dpe_base_universe_d3_011_dpe_016_trading_intensity_5_016}


def dpe_base_universe_d3_012_dpe_018_price_level_distress_21_018(dpe_base_universe_d2_012_dpe_018_price_level_distress_21_018):
    return _base_universe_d3(dpe_base_universe_d2_012_dpe_018_price_level_distress_21_018, 12)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_012_dpe_018_price_level_distress_21_018'] = {'inputs': ['dpe_base_universe_d2_012_dpe_018_price_level_distress_21_018'], 'func': dpe_base_universe_d3_012_dpe_018_price_level_distress_21_018}


def dpe_base_universe_d3_013_dpe_020_zero_volume_frequency_63_020(dpe_base_universe_d2_013_dpe_020_zero_volume_frequency_63_020):
    return _base_universe_d3(dpe_base_universe_d2_013_dpe_020_zero_volume_frequency_63_020, 13)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_013_dpe_020_zero_volume_frequency_63_020'] = {'inputs': ['dpe_base_universe_d2_013_dpe_020_zero_volume_frequency_63_020'], 'func': dpe_base_universe_d3_013_dpe_020_zero_volume_frequency_63_020}


def dpe_base_universe_d3_014_dpe_021_spread_proxy_84_021(dpe_base_universe_d2_014_dpe_021_spread_proxy_84_021):
    return _base_universe_d3(dpe_base_universe_d2_014_dpe_021_spread_proxy_84_021, 14)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_014_dpe_021_spread_proxy_84_021'] = {'inputs': ['dpe_base_universe_d2_014_dpe_021_spread_proxy_84_021'], 'func': dpe_base_universe_d3_014_dpe_021_spread_proxy_84_021}


def dpe_base_universe_d3_015_dpe_022_trading_intensity_126_022(dpe_base_universe_d2_015_dpe_022_trading_intensity_126_022):
    return _base_universe_d3(dpe_base_universe_d2_015_dpe_022_trading_intensity_126_022, 15)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_015_dpe_022_trading_intensity_126_022'] = {'inputs': ['dpe_base_universe_d2_015_dpe_022_trading_intensity_126_022'], 'func': dpe_base_universe_d3_015_dpe_022_trading_intensity_126_022}


def dpe_base_universe_d3_016_dpe_024_price_level_distress_252_024(dpe_base_universe_d2_016_dpe_024_price_level_distress_252_024):
    return _base_universe_d3(dpe_base_universe_d2_016_dpe_024_price_level_distress_252_024, 16)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_016_dpe_024_price_level_distress_252_024'] = {'inputs': ['dpe_base_universe_d2_016_dpe_024_price_level_distress_252_024'], 'func': dpe_base_universe_d3_016_dpe_024_price_level_distress_252_024}


def dpe_base_universe_d3_017_dpe_026_zero_volume_frequency_504_026(dpe_base_universe_d2_017_dpe_026_zero_volume_frequency_504_026):
    return _base_universe_d3(dpe_base_universe_d2_017_dpe_026_zero_volume_frequency_504_026, 17)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_017_dpe_026_zero_volume_frequency_504_026'] = {'inputs': ['dpe_base_universe_d2_017_dpe_026_zero_volume_frequency_504_026'], 'func': dpe_base_universe_d3_017_dpe_026_zero_volume_frequency_504_026}


def dpe_base_universe_d3_018_dpe_027_spread_proxy_756_027(dpe_base_universe_d2_018_dpe_027_spread_proxy_756_027):
    return _base_universe_d3(dpe_base_universe_d2_018_dpe_027_spread_proxy_756_027, 18)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_018_dpe_027_spread_proxy_756_027'] = {'inputs': ['dpe_base_universe_d2_018_dpe_027_spread_proxy_756_027'], 'func': dpe_base_universe_d3_018_dpe_027_spread_proxy_756_027}


def dpe_base_universe_d3_019_dpe_028_trading_intensity_1008_028(dpe_base_universe_d2_019_dpe_028_trading_intensity_1008_028):
    return _base_universe_d3(dpe_base_universe_d2_019_dpe_028_trading_intensity_1008_028, 19)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_019_dpe_028_trading_intensity_1008_028'] = {'inputs': ['dpe_base_universe_d2_019_dpe_028_trading_intensity_1008_028'], 'func': dpe_base_universe_d3_019_dpe_028_trading_intensity_1008_028}


def dpe_base_universe_d3_020_dpe_030_price_level_distress_1512_030(dpe_base_universe_d2_020_dpe_030_price_level_distress_1512_030):
    return _base_universe_d3(dpe_base_universe_d2_020_dpe_030_price_level_distress_1512_030, 20)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_020_dpe_030_price_level_distress_1512_030'] = {'inputs': ['dpe_base_universe_d2_020_dpe_030_price_level_distress_1512_030'], 'func': dpe_base_universe_d3_020_dpe_030_price_level_distress_1512_030}


def dpe_base_universe_d3_021_dpe_basefill_001(dpe_base_universe_d2_021_dpe_basefill_001):
    return _base_universe_d3(dpe_base_universe_d2_021_dpe_basefill_001, 21)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_021_dpe_basefill_001'] = {'inputs': ['dpe_base_universe_d2_021_dpe_basefill_001'], 'func': dpe_base_universe_d3_021_dpe_basefill_001}


def dpe_base_universe_d3_022_dpe_basefill_005(dpe_base_universe_d2_022_dpe_basefill_005):
    return _base_universe_d3(dpe_base_universe_d2_022_dpe_basefill_005, 22)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_022_dpe_basefill_005'] = {'inputs': ['dpe_base_universe_d2_022_dpe_basefill_005'], 'func': dpe_base_universe_d3_022_dpe_basefill_005}


def dpe_base_universe_d3_023_dpe_basefill_007(dpe_base_universe_d2_023_dpe_basefill_007):
    return _base_universe_d3(dpe_base_universe_d2_023_dpe_basefill_007, 23)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_023_dpe_basefill_007'] = {'inputs': ['dpe_base_universe_d2_023_dpe_basefill_007'], 'func': dpe_base_universe_d3_023_dpe_basefill_007}


def dpe_base_universe_d3_024_dpe_basefill_011(dpe_base_universe_d2_024_dpe_basefill_011):
    return _base_universe_d3(dpe_base_universe_d2_024_dpe_basefill_011, 24)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_024_dpe_basefill_011'] = {'inputs': ['dpe_base_universe_d2_024_dpe_basefill_011'], 'func': dpe_base_universe_d3_024_dpe_basefill_011}


def dpe_base_universe_d3_025_dpe_basefill_013(dpe_base_universe_d2_025_dpe_basefill_013):
    return _base_universe_d3(dpe_base_universe_d2_025_dpe_basefill_013, 25)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_025_dpe_basefill_013'] = {'inputs': ['dpe_base_universe_d2_025_dpe_basefill_013'], 'func': dpe_base_universe_d3_025_dpe_basefill_013}


def dpe_base_universe_d3_026_dpe_basefill_017(dpe_base_universe_d2_026_dpe_basefill_017):
    return _base_universe_d3(dpe_base_universe_d2_026_dpe_basefill_017, 26)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_026_dpe_basefill_017'] = {'inputs': ['dpe_base_universe_d2_026_dpe_basefill_017'], 'func': dpe_base_universe_d3_026_dpe_basefill_017}


def dpe_base_universe_d3_027_dpe_basefill_019(dpe_base_universe_d2_027_dpe_basefill_019):
    return _base_universe_d3(dpe_base_universe_d2_027_dpe_basefill_019, 27)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_027_dpe_basefill_019'] = {'inputs': ['dpe_base_universe_d2_027_dpe_basefill_019'], 'func': dpe_base_universe_d3_027_dpe_basefill_019}


def dpe_base_universe_d3_028_dpe_basefill_023(dpe_base_universe_d2_028_dpe_basefill_023):
    return _base_universe_d3(dpe_base_universe_d2_028_dpe_basefill_023, 28)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_028_dpe_basefill_023'] = {'inputs': ['dpe_base_universe_d2_028_dpe_basefill_023'], 'func': dpe_base_universe_d3_028_dpe_basefill_023}


def dpe_base_universe_d3_029_dpe_basefill_025(dpe_base_universe_d2_029_dpe_basefill_025):
    return _base_universe_d3(dpe_base_universe_d2_029_dpe_basefill_025, 29)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_029_dpe_basefill_025'] = {'inputs': ['dpe_base_universe_d2_029_dpe_basefill_025'], 'func': dpe_base_universe_d3_029_dpe_basefill_025}


def dpe_base_universe_d3_030_dpe_basefill_029(dpe_base_universe_d2_030_dpe_basefill_029):
    return _base_universe_d3(dpe_base_universe_d2_030_dpe_basefill_029, 30)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_030_dpe_basefill_029'] = {'inputs': ['dpe_base_universe_d2_030_dpe_basefill_029'], 'func': dpe_base_universe_d3_030_dpe_basefill_029}


def dpe_base_universe_d3_031_dpe_basefill_031(dpe_base_universe_d2_031_dpe_basefill_031):
    return _base_universe_d3(dpe_base_universe_d2_031_dpe_basefill_031, 31)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_031_dpe_basefill_031'] = {'inputs': ['dpe_base_universe_d2_031_dpe_basefill_031'], 'func': dpe_base_universe_d3_031_dpe_basefill_031}


def dpe_base_universe_d3_032_dpe_basefill_032(dpe_base_universe_d2_032_dpe_basefill_032):
    return _base_universe_d3(dpe_base_universe_d2_032_dpe_basefill_032, 32)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_032_dpe_basefill_032'] = {'inputs': ['dpe_base_universe_d2_032_dpe_basefill_032'], 'func': dpe_base_universe_d3_032_dpe_basefill_032}


def dpe_base_universe_d3_033_dpe_basefill_033(dpe_base_universe_d2_033_dpe_basefill_033):
    return _base_universe_d3(dpe_base_universe_d2_033_dpe_basefill_033, 33)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_033_dpe_basefill_033'] = {'inputs': ['dpe_base_universe_d2_033_dpe_basefill_033'], 'func': dpe_base_universe_d3_033_dpe_basefill_033}


def dpe_base_universe_d3_034_dpe_basefill_034(dpe_base_universe_d2_034_dpe_basefill_034):
    return _base_universe_d3(dpe_base_universe_d2_034_dpe_basefill_034, 34)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_034_dpe_basefill_034'] = {'inputs': ['dpe_base_universe_d2_034_dpe_basefill_034'], 'func': dpe_base_universe_d3_034_dpe_basefill_034}


def dpe_base_universe_d3_035_dpe_basefill_035(dpe_base_universe_d2_035_dpe_basefill_035):
    return _base_universe_d3(dpe_base_universe_d2_035_dpe_basefill_035, 35)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_035_dpe_basefill_035'] = {'inputs': ['dpe_base_universe_d2_035_dpe_basefill_035'], 'func': dpe_base_universe_d3_035_dpe_basefill_035}


def dpe_base_universe_d3_036_dpe_basefill_036(dpe_base_universe_d2_036_dpe_basefill_036):
    return _base_universe_d3(dpe_base_universe_d2_036_dpe_basefill_036, 36)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_036_dpe_basefill_036'] = {'inputs': ['dpe_base_universe_d2_036_dpe_basefill_036'], 'func': dpe_base_universe_d3_036_dpe_basefill_036}


def dpe_base_universe_d3_037_dpe_basefill_037(dpe_base_universe_d2_037_dpe_basefill_037):
    return _base_universe_d3(dpe_base_universe_d2_037_dpe_basefill_037, 37)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_037_dpe_basefill_037'] = {'inputs': ['dpe_base_universe_d2_037_dpe_basefill_037'], 'func': dpe_base_universe_d3_037_dpe_basefill_037}


def dpe_base_universe_d3_038_dpe_basefill_038(dpe_base_universe_d2_038_dpe_basefill_038):
    return _base_universe_d3(dpe_base_universe_d2_038_dpe_basefill_038, 38)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_038_dpe_basefill_038'] = {'inputs': ['dpe_base_universe_d2_038_dpe_basefill_038'], 'func': dpe_base_universe_d3_038_dpe_basefill_038}


def dpe_base_universe_d3_039_dpe_basefill_039(dpe_base_universe_d2_039_dpe_basefill_039):
    return _base_universe_d3(dpe_base_universe_d2_039_dpe_basefill_039, 39)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_039_dpe_basefill_039'] = {'inputs': ['dpe_base_universe_d2_039_dpe_basefill_039'], 'func': dpe_base_universe_d3_039_dpe_basefill_039}


def dpe_base_universe_d3_040_dpe_basefill_040(dpe_base_universe_d2_040_dpe_basefill_040):
    return _base_universe_d3(dpe_base_universe_d2_040_dpe_basefill_040, 40)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_040_dpe_basefill_040'] = {'inputs': ['dpe_base_universe_d2_040_dpe_basefill_040'], 'func': dpe_base_universe_d3_040_dpe_basefill_040}


def dpe_base_universe_d3_041_dpe_basefill_041(dpe_base_universe_d2_041_dpe_basefill_041):
    return _base_universe_d3(dpe_base_universe_d2_041_dpe_basefill_041, 41)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_041_dpe_basefill_041'] = {'inputs': ['dpe_base_universe_d2_041_dpe_basefill_041'], 'func': dpe_base_universe_d3_041_dpe_basefill_041}


def dpe_base_universe_d3_042_dpe_basefill_042(dpe_base_universe_d2_042_dpe_basefill_042):
    return _base_universe_d3(dpe_base_universe_d2_042_dpe_basefill_042, 42)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_042_dpe_basefill_042'] = {'inputs': ['dpe_base_universe_d2_042_dpe_basefill_042'], 'func': dpe_base_universe_d3_042_dpe_basefill_042}


def dpe_base_universe_d3_043_dpe_basefill_043(dpe_base_universe_d2_043_dpe_basefill_043):
    return _base_universe_d3(dpe_base_universe_d2_043_dpe_basefill_043, 43)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_043_dpe_basefill_043'] = {'inputs': ['dpe_base_universe_d2_043_dpe_basefill_043'], 'func': dpe_base_universe_d3_043_dpe_basefill_043}


def dpe_base_universe_d3_044_dpe_basefill_044(dpe_base_universe_d2_044_dpe_basefill_044):
    return _base_universe_d3(dpe_base_universe_d2_044_dpe_basefill_044, 44)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_044_dpe_basefill_044'] = {'inputs': ['dpe_base_universe_d2_044_dpe_basefill_044'], 'func': dpe_base_universe_d3_044_dpe_basefill_044}


def dpe_base_universe_d3_045_dpe_basefill_045(dpe_base_universe_d2_045_dpe_basefill_045):
    return _base_universe_d3(dpe_base_universe_d2_045_dpe_basefill_045, 45)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_045_dpe_basefill_045'] = {'inputs': ['dpe_base_universe_d2_045_dpe_basefill_045'], 'func': dpe_base_universe_d3_045_dpe_basefill_045}


def dpe_base_universe_d3_046_dpe_basefill_046(dpe_base_universe_d2_046_dpe_basefill_046):
    return _base_universe_d3(dpe_base_universe_d2_046_dpe_basefill_046, 46)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_046_dpe_basefill_046'] = {'inputs': ['dpe_base_universe_d2_046_dpe_basefill_046'], 'func': dpe_base_universe_d3_046_dpe_basefill_046}


def dpe_base_universe_d3_047_dpe_basefill_047(dpe_base_universe_d2_047_dpe_basefill_047):
    return _base_universe_d3(dpe_base_universe_d2_047_dpe_basefill_047, 47)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_047_dpe_basefill_047'] = {'inputs': ['dpe_base_universe_d2_047_dpe_basefill_047'], 'func': dpe_base_universe_d3_047_dpe_basefill_047}


def dpe_base_universe_d3_048_dpe_basefill_048(dpe_base_universe_d2_048_dpe_basefill_048):
    return _base_universe_d3(dpe_base_universe_d2_048_dpe_basefill_048, 48)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_048_dpe_basefill_048'] = {'inputs': ['dpe_base_universe_d2_048_dpe_basefill_048'], 'func': dpe_base_universe_d3_048_dpe_basefill_048}


def dpe_base_universe_d3_049_dpe_basefill_049(dpe_base_universe_d2_049_dpe_basefill_049):
    return _base_universe_d3(dpe_base_universe_d2_049_dpe_basefill_049, 49)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_049_dpe_basefill_049'] = {'inputs': ['dpe_base_universe_d2_049_dpe_basefill_049'], 'func': dpe_base_universe_d3_049_dpe_basefill_049}


def dpe_base_universe_d3_050_dpe_basefill_050(dpe_base_universe_d2_050_dpe_basefill_050):
    return _base_universe_d3(dpe_base_universe_d2_050_dpe_basefill_050, 50)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_050_dpe_basefill_050'] = {'inputs': ['dpe_base_universe_d2_050_dpe_basefill_050'], 'func': dpe_base_universe_d3_050_dpe_basefill_050}


def dpe_base_universe_d3_051_dpe_basefill_051(dpe_base_universe_d2_051_dpe_basefill_051):
    return _base_universe_d3(dpe_base_universe_d2_051_dpe_basefill_051, 51)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_051_dpe_basefill_051'] = {'inputs': ['dpe_base_universe_d2_051_dpe_basefill_051'], 'func': dpe_base_universe_d3_051_dpe_basefill_051}


def dpe_base_universe_d3_052_dpe_basefill_052(dpe_base_universe_d2_052_dpe_basefill_052):
    return _base_universe_d3(dpe_base_universe_d2_052_dpe_basefill_052, 52)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_052_dpe_basefill_052'] = {'inputs': ['dpe_base_universe_d2_052_dpe_basefill_052'], 'func': dpe_base_universe_d3_052_dpe_basefill_052}


def dpe_base_universe_d3_053_dpe_basefill_053(dpe_base_universe_d2_053_dpe_basefill_053):
    return _base_universe_d3(dpe_base_universe_d2_053_dpe_basefill_053, 53)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_053_dpe_basefill_053'] = {'inputs': ['dpe_base_universe_d2_053_dpe_basefill_053'], 'func': dpe_base_universe_d3_053_dpe_basefill_053}


def dpe_base_universe_d3_054_dpe_basefill_054(dpe_base_universe_d2_054_dpe_basefill_054):
    return _base_universe_d3(dpe_base_universe_d2_054_dpe_basefill_054, 54)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_054_dpe_basefill_054'] = {'inputs': ['dpe_base_universe_d2_054_dpe_basefill_054'], 'func': dpe_base_universe_d3_054_dpe_basefill_054}


def dpe_base_universe_d3_055_dpe_basefill_055(dpe_base_universe_d2_055_dpe_basefill_055):
    return _base_universe_d3(dpe_base_universe_d2_055_dpe_basefill_055, 55)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_055_dpe_basefill_055'] = {'inputs': ['dpe_base_universe_d2_055_dpe_basefill_055'], 'func': dpe_base_universe_d3_055_dpe_basefill_055}


def dpe_base_universe_d3_056_dpe_basefill_056(dpe_base_universe_d2_056_dpe_basefill_056):
    return _base_universe_d3(dpe_base_universe_d2_056_dpe_basefill_056, 56)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_056_dpe_basefill_056'] = {'inputs': ['dpe_base_universe_d2_056_dpe_basefill_056'], 'func': dpe_base_universe_d3_056_dpe_basefill_056}


def dpe_base_universe_d3_057_dpe_basefill_057(dpe_base_universe_d2_057_dpe_basefill_057):
    return _base_universe_d3(dpe_base_universe_d2_057_dpe_basefill_057, 57)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_057_dpe_basefill_057'] = {'inputs': ['dpe_base_universe_d2_057_dpe_basefill_057'], 'func': dpe_base_universe_d3_057_dpe_basefill_057}


def dpe_base_universe_d3_058_dpe_basefill_058(dpe_base_universe_d2_058_dpe_basefill_058):
    return _base_universe_d3(dpe_base_universe_d2_058_dpe_basefill_058, 58)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_058_dpe_basefill_058'] = {'inputs': ['dpe_base_universe_d2_058_dpe_basefill_058'], 'func': dpe_base_universe_d3_058_dpe_basefill_058}


def dpe_base_universe_d3_059_dpe_basefill_059(dpe_base_universe_d2_059_dpe_basefill_059):
    return _base_universe_d3(dpe_base_universe_d2_059_dpe_basefill_059, 59)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_059_dpe_basefill_059'] = {'inputs': ['dpe_base_universe_d2_059_dpe_basefill_059'], 'func': dpe_base_universe_d3_059_dpe_basefill_059}


def dpe_base_universe_d3_060_dpe_basefill_060(dpe_base_universe_d2_060_dpe_basefill_060):
    return _base_universe_d3(dpe_base_universe_d2_060_dpe_basefill_060, 60)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_060_dpe_basefill_060'] = {'inputs': ['dpe_base_universe_d2_060_dpe_basefill_060'], 'func': dpe_base_universe_d3_060_dpe_basefill_060}


def dpe_base_universe_d3_061_dpe_basefill_061(dpe_base_universe_d2_061_dpe_basefill_061):
    return _base_universe_d3(dpe_base_universe_d2_061_dpe_basefill_061, 61)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_061_dpe_basefill_061'] = {'inputs': ['dpe_base_universe_d2_061_dpe_basefill_061'], 'func': dpe_base_universe_d3_061_dpe_basefill_061}


def dpe_base_universe_d3_062_dpe_basefill_062(dpe_base_universe_d2_062_dpe_basefill_062):
    return _base_universe_d3(dpe_base_universe_d2_062_dpe_basefill_062, 62)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_062_dpe_basefill_062'] = {'inputs': ['dpe_base_universe_d2_062_dpe_basefill_062'], 'func': dpe_base_universe_d3_062_dpe_basefill_062}


def dpe_base_universe_d3_063_dpe_basefill_063(dpe_base_universe_d2_063_dpe_basefill_063):
    return _base_universe_d3(dpe_base_universe_d2_063_dpe_basefill_063, 63)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_063_dpe_basefill_063'] = {'inputs': ['dpe_base_universe_d2_063_dpe_basefill_063'], 'func': dpe_base_universe_d3_063_dpe_basefill_063}


def dpe_base_universe_d3_064_dpe_basefill_064(dpe_base_universe_d2_064_dpe_basefill_064):
    return _base_universe_d3(dpe_base_universe_d2_064_dpe_basefill_064, 64)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_064_dpe_basefill_064'] = {'inputs': ['dpe_base_universe_d2_064_dpe_basefill_064'], 'func': dpe_base_universe_d3_064_dpe_basefill_064}


def dpe_base_universe_d3_065_dpe_basefill_065(dpe_base_universe_d2_065_dpe_basefill_065):
    return _base_universe_d3(dpe_base_universe_d2_065_dpe_basefill_065, 65)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_065_dpe_basefill_065'] = {'inputs': ['dpe_base_universe_d2_065_dpe_basefill_065'], 'func': dpe_base_universe_d3_065_dpe_basefill_065}


def dpe_base_universe_d3_066_dpe_basefill_066(dpe_base_universe_d2_066_dpe_basefill_066):
    return _base_universe_d3(dpe_base_universe_d2_066_dpe_basefill_066, 66)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_066_dpe_basefill_066'] = {'inputs': ['dpe_base_universe_d2_066_dpe_basefill_066'], 'func': dpe_base_universe_d3_066_dpe_basefill_066}


def dpe_base_universe_d3_067_dpe_basefill_067(dpe_base_universe_d2_067_dpe_basefill_067):
    return _base_universe_d3(dpe_base_universe_d2_067_dpe_basefill_067, 67)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_067_dpe_basefill_067'] = {'inputs': ['dpe_base_universe_d2_067_dpe_basefill_067'], 'func': dpe_base_universe_d3_067_dpe_basefill_067}


def dpe_base_universe_d3_068_dpe_basefill_068(dpe_base_universe_d2_068_dpe_basefill_068):
    return _base_universe_d3(dpe_base_universe_d2_068_dpe_basefill_068, 68)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_068_dpe_basefill_068'] = {'inputs': ['dpe_base_universe_d2_068_dpe_basefill_068'], 'func': dpe_base_universe_d3_068_dpe_basefill_068}


def dpe_base_universe_d3_069_dpe_basefill_069(dpe_base_universe_d2_069_dpe_basefill_069):
    return _base_universe_d3(dpe_base_universe_d2_069_dpe_basefill_069, 69)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_069_dpe_basefill_069'] = {'inputs': ['dpe_base_universe_d2_069_dpe_basefill_069'], 'func': dpe_base_universe_d3_069_dpe_basefill_069}


def dpe_base_universe_d3_070_dpe_basefill_070(dpe_base_universe_d2_070_dpe_basefill_070):
    return _base_universe_d3(dpe_base_universe_d2_070_dpe_basefill_070, 70)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_070_dpe_basefill_070'] = {'inputs': ['dpe_base_universe_d2_070_dpe_basefill_070'], 'func': dpe_base_universe_d3_070_dpe_basefill_070}


def dpe_base_universe_d3_071_dpe_basefill_071(dpe_base_universe_d2_071_dpe_basefill_071):
    return _base_universe_d3(dpe_base_universe_d2_071_dpe_basefill_071, 71)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_071_dpe_basefill_071'] = {'inputs': ['dpe_base_universe_d2_071_dpe_basefill_071'], 'func': dpe_base_universe_d3_071_dpe_basefill_071}


def dpe_base_universe_d3_072_dpe_basefill_072(dpe_base_universe_d2_072_dpe_basefill_072):
    return _base_universe_d3(dpe_base_universe_d2_072_dpe_basefill_072, 72)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_072_dpe_basefill_072'] = {'inputs': ['dpe_base_universe_d2_072_dpe_basefill_072'], 'func': dpe_base_universe_d3_072_dpe_basefill_072}


def dpe_base_universe_d3_073_dpe_basefill_073(dpe_base_universe_d2_073_dpe_basefill_073):
    return _base_universe_d3(dpe_base_universe_d2_073_dpe_basefill_073, 73)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_073_dpe_basefill_073'] = {'inputs': ['dpe_base_universe_d2_073_dpe_basefill_073'], 'func': dpe_base_universe_d3_073_dpe_basefill_073}


def dpe_base_universe_d3_074_dpe_basefill_074(dpe_base_universe_d2_074_dpe_basefill_074):
    return _base_universe_d3(dpe_base_universe_d2_074_dpe_basefill_074, 74)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_074_dpe_basefill_074'] = {'inputs': ['dpe_base_universe_d2_074_dpe_basefill_074'], 'func': dpe_base_universe_d3_074_dpe_basefill_074}


def dpe_base_universe_d3_075_dpe_basefill_075(dpe_base_universe_d2_075_dpe_basefill_075):
    return _base_universe_d3(dpe_base_universe_d2_075_dpe_basefill_075, 75)
DPE_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dpe_base_universe_d3_075_dpe_basefill_075'] = {'inputs': ['dpe_base_universe_d2_075_dpe_basefill_075'], 'func': dpe_base_universe_d3_075_dpe_basefill_075}
