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



def dstk_001_amihud_illiquidity_accel_1(dstk_001_amihud_illiquidity_roc_1):
    feature = _s(dstk_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def dstk_007_amihud_illiquidity_accel_5(dstk_007_amihud_illiquidity_roc_5):
    feature = _s(dstk_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def dstk_013_amihud_illiquidity_accel_42(dstk_013_amihud_illiquidity_roc_42):
    feature = _s(dstk_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def dstk_179_dstk_019_amihud_illiquidity_42_019_accel_126(dstk_154_dstk_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(dstk_154_dstk_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def dstk_180_dstk_025_amihud_illiquidity_378_025_accel_378(dstk_155_dstk_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(dstk_155_dstk_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















DECLINE_STREAKS_REGISTRY_3RD_DERIVATIVES = {
    'dstk_001_amihud_illiquidity_accel_1': {'inputs': ['dstk_001_amihud_illiquidity_roc_1'], 'func': dstk_001_amihud_illiquidity_accel_1},
    'dstk_007_amihud_illiquidity_accel_5': {'inputs': ['dstk_007_amihud_illiquidity_roc_5'], 'func': dstk_007_amihud_illiquidity_accel_5},
    'dstk_013_amihud_illiquidity_accel_42': {'inputs': ['dstk_013_amihud_illiquidity_roc_42'], 'func': dstk_013_amihud_illiquidity_accel_42},
    'dstk_179_dstk_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['dstk_154_dstk_019_amihud_illiquidity_42_019_roc_126'], 'func': dstk_179_dstk_019_amihud_illiquidity_42_019_accel_126},
    'dstk_180_dstk_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['dstk_155_dstk_025_amihud_illiquidity_378_025_roc_378'], 'func': dstk_180_dstk_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ds_replacement_d3_001(ds_replacement_d2_001):
    feature = _clean(ds_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_001'] = {'inputs': ['ds_replacement_d2_001'], 'func': ds_replacement_d3_001}


def ds_replacement_d3_002(ds_replacement_d2_002):
    feature = _clean(ds_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_002'] = {'inputs': ['ds_replacement_d2_002'], 'func': ds_replacement_d3_002}


def ds_replacement_d3_003(ds_replacement_d2_003):
    feature = _clean(ds_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_003'] = {'inputs': ['ds_replacement_d2_003'], 'func': ds_replacement_d3_003}


def ds_replacement_d3_004(ds_replacement_d2_004):
    feature = _clean(ds_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_004'] = {'inputs': ['ds_replacement_d2_004'], 'func': ds_replacement_d3_004}


def ds_replacement_d3_005(ds_replacement_d2_005):
    feature = _clean(ds_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_005'] = {'inputs': ['ds_replacement_d2_005'], 'func': ds_replacement_d3_005}


def ds_replacement_d3_006(ds_replacement_d2_006):
    feature = _clean(ds_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_006'] = {'inputs': ['ds_replacement_d2_006'], 'func': ds_replacement_d3_006}


def ds_replacement_d3_007(ds_replacement_d2_007):
    feature = _clean(ds_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_007'] = {'inputs': ['ds_replacement_d2_007'], 'func': ds_replacement_d3_007}


def ds_replacement_d3_008(ds_replacement_d2_008):
    feature = _clean(ds_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_008'] = {'inputs': ['ds_replacement_d2_008'], 'func': ds_replacement_d3_008}


def ds_replacement_d3_009(ds_replacement_d2_009):
    feature = _clean(ds_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_009'] = {'inputs': ['ds_replacement_d2_009'], 'func': ds_replacement_d3_009}


def ds_replacement_d3_010(ds_replacement_d2_010):
    feature = _clean(ds_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_010'] = {'inputs': ['ds_replacement_d2_010'], 'func': ds_replacement_d3_010}


def ds_replacement_d3_011(ds_replacement_d2_011):
    feature = _clean(ds_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_011'] = {'inputs': ['ds_replacement_d2_011'], 'func': ds_replacement_d3_011}


def ds_replacement_d3_012(ds_replacement_d2_012):
    feature = _clean(ds_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_012'] = {'inputs': ['ds_replacement_d2_012'], 'func': ds_replacement_d3_012}


def ds_replacement_d3_013(ds_replacement_d2_013):
    feature = _clean(ds_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_013'] = {'inputs': ['ds_replacement_d2_013'], 'func': ds_replacement_d3_013}


def ds_replacement_d3_014(ds_replacement_d2_014):
    feature = _clean(ds_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_014'] = {'inputs': ['ds_replacement_d2_014'], 'func': ds_replacement_d3_014}


def ds_replacement_d3_015(ds_replacement_d2_015):
    feature = _clean(ds_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_015'] = {'inputs': ['ds_replacement_d2_015'], 'func': ds_replacement_d3_015}


def ds_replacement_d3_016(ds_replacement_d2_016):
    feature = _clean(ds_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_016'] = {'inputs': ['ds_replacement_d2_016'], 'func': ds_replacement_d3_016}


def ds_replacement_d3_017(ds_replacement_d2_017):
    feature = _clean(ds_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_017'] = {'inputs': ['ds_replacement_d2_017'], 'func': ds_replacement_d3_017}


def ds_replacement_d3_018(ds_replacement_d2_018):
    feature = _clean(ds_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_018'] = {'inputs': ['ds_replacement_d2_018'], 'func': ds_replacement_d3_018}


def ds_replacement_d3_019(ds_replacement_d2_019):
    feature = _clean(ds_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_019'] = {'inputs': ['ds_replacement_d2_019'], 'func': ds_replacement_d3_019}


def ds_replacement_d3_020(ds_replacement_d2_020):
    feature = _clean(ds_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_020'] = {'inputs': ['ds_replacement_d2_020'], 'func': ds_replacement_d3_020}


def ds_replacement_d3_021(ds_replacement_d2_021):
    feature = _clean(ds_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_021'] = {'inputs': ['ds_replacement_d2_021'], 'func': ds_replacement_d3_021}


def ds_replacement_d3_022(ds_replacement_d2_022):
    feature = _clean(ds_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_022'] = {'inputs': ['ds_replacement_d2_022'], 'func': ds_replacement_d3_022}


def ds_replacement_d3_023(ds_replacement_d2_023):
    feature = _clean(ds_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_023'] = {'inputs': ['ds_replacement_d2_023'], 'func': ds_replacement_d3_023}


def ds_replacement_d3_024(ds_replacement_d2_024):
    feature = _clean(ds_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_024'] = {'inputs': ['ds_replacement_d2_024'], 'func': ds_replacement_d3_024}


def ds_replacement_d3_025(ds_replacement_d2_025):
    feature = _clean(ds_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_025'] = {'inputs': ['ds_replacement_d2_025'], 'func': ds_replacement_d3_025}


def ds_replacement_d3_026(ds_replacement_d2_026):
    feature = _clean(ds_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_026'] = {'inputs': ['ds_replacement_d2_026'], 'func': ds_replacement_d3_026}


def ds_replacement_d3_027(ds_replacement_d2_027):
    feature = _clean(ds_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_027'] = {'inputs': ['ds_replacement_d2_027'], 'func': ds_replacement_d3_027}


def ds_replacement_d3_028(ds_replacement_d2_028):
    feature = _clean(ds_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_028'] = {'inputs': ['ds_replacement_d2_028'], 'func': ds_replacement_d3_028}


def ds_replacement_d3_029(ds_replacement_d2_029):
    feature = _clean(ds_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_029'] = {'inputs': ['ds_replacement_d2_029'], 'func': ds_replacement_d3_029}


def ds_replacement_d3_030(ds_replacement_d2_030):
    feature = _clean(ds_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_030'] = {'inputs': ['ds_replacement_d2_030'], 'func': ds_replacement_d3_030}


def ds_replacement_d3_031(ds_replacement_d2_031):
    feature = _clean(ds_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_031'] = {'inputs': ['ds_replacement_d2_031'], 'func': ds_replacement_d3_031}


def ds_replacement_d3_032(ds_replacement_d2_032):
    feature = _clean(ds_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_032'] = {'inputs': ['ds_replacement_d2_032'], 'func': ds_replacement_d3_032}


def ds_replacement_d3_033(ds_replacement_d2_033):
    feature = _clean(ds_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_033'] = {'inputs': ['ds_replacement_d2_033'], 'func': ds_replacement_d3_033}


def ds_replacement_d3_034(ds_replacement_d2_034):
    feature = _clean(ds_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_034'] = {'inputs': ['ds_replacement_d2_034'], 'func': ds_replacement_d3_034}


def ds_replacement_d3_035(ds_replacement_d2_035):
    feature = _clean(ds_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_035'] = {'inputs': ['ds_replacement_d2_035'], 'func': ds_replacement_d3_035}


def ds_replacement_d3_036(ds_replacement_d2_036):
    feature = _clean(ds_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_036'] = {'inputs': ['ds_replacement_d2_036'], 'func': ds_replacement_d3_036}


def ds_replacement_d3_037(ds_replacement_d2_037):
    feature = _clean(ds_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_037'] = {'inputs': ['ds_replacement_d2_037'], 'func': ds_replacement_d3_037}


def ds_replacement_d3_038(ds_replacement_d2_038):
    feature = _clean(ds_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_038'] = {'inputs': ['ds_replacement_d2_038'], 'func': ds_replacement_d3_038}


def ds_replacement_d3_039(ds_replacement_d2_039):
    feature = _clean(ds_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_039'] = {'inputs': ['ds_replacement_d2_039'], 'func': ds_replacement_d3_039}


def ds_replacement_d3_040(ds_replacement_d2_040):
    feature = _clean(ds_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_040'] = {'inputs': ['ds_replacement_d2_040'], 'func': ds_replacement_d3_040}


def ds_replacement_d3_041(ds_replacement_d2_041):
    feature = _clean(ds_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_041'] = {'inputs': ['ds_replacement_d2_041'], 'func': ds_replacement_d3_041}


def ds_replacement_d3_042(ds_replacement_d2_042):
    feature = _clean(ds_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_042'] = {'inputs': ['ds_replacement_d2_042'], 'func': ds_replacement_d3_042}


def ds_replacement_d3_043(ds_replacement_d2_043):
    feature = _clean(ds_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_043'] = {'inputs': ['ds_replacement_d2_043'], 'func': ds_replacement_d3_043}


def ds_replacement_d3_044(ds_replacement_d2_044):
    feature = _clean(ds_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_044'] = {'inputs': ['ds_replacement_d2_044'], 'func': ds_replacement_d3_044}


def ds_replacement_d3_045(ds_replacement_d2_045):
    feature = _clean(ds_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_045'] = {'inputs': ['ds_replacement_d2_045'], 'func': ds_replacement_d3_045}


def ds_replacement_d3_046(ds_replacement_d2_046):
    feature = _clean(ds_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_046'] = {'inputs': ['ds_replacement_d2_046'], 'func': ds_replacement_d3_046}


def ds_replacement_d3_047(ds_replacement_d2_047):
    feature = _clean(ds_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_047'] = {'inputs': ['ds_replacement_d2_047'], 'func': ds_replacement_d3_047}


def ds_replacement_d3_048(ds_replacement_d2_048):
    feature = _clean(ds_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_048'] = {'inputs': ['ds_replacement_d2_048'], 'func': ds_replacement_d3_048}


def ds_replacement_d3_049(ds_replacement_d2_049):
    feature = _clean(ds_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_049'] = {'inputs': ['ds_replacement_d2_049'], 'func': ds_replacement_d3_049}


def ds_replacement_d3_050(ds_replacement_d2_050):
    feature = _clean(ds_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_050'] = {'inputs': ['ds_replacement_d2_050'], 'func': ds_replacement_d3_050}


def ds_replacement_d3_051(ds_replacement_d2_051):
    feature = _clean(ds_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_051'] = {'inputs': ['ds_replacement_d2_051'], 'func': ds_replacement_d3_051}


def ds_replacement_d3_052(ds_replacement_d2_052):
    feature = _clean(ds_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_052'] = {'inputs': ['ds_replacement_d2_052'], 'func': ds_replacement_d3_052}


def ds_replacement_d3_053(ds_replacement_d2_053):
    feature = _clean(ds_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_053'] = {'inputs': ['ds_replacement_d2_053'], 'func': ds_replacement_d3_053}


def ds_replacement_d3_054(ds_replacement_d2_054):
    feature = _clean(ds_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_054'] = {'inputs': ['ds_replacement_d2_054'], 'func': ds_replacement_d3_054}


def ds_replacement_d3_055(ds_replacement_d2_055):
    feature = _clean(ds_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_055'] = {'inputs': ['ds_replacement_d2_055'], 'func': ds_replacement_d3_055}


def ds_replacement_d3_056(ds_replacement_d2_056):
    feature = _clean(ds_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_056'] = {'inputs': ['ds_replacement_d2_056'], 'func': ds_replacement_d3_056}


def ds_replacement_d3_057(ds_replacement_d2_057):
    feature = _clean(ds_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_057'] = {'inputs': ['ds_replacement_d2_057'], 'func': ds_replacement_d3_057}


def ds_replacement_d3_058(ds_replacement_d2_058):
    feature = _clean(ds_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_058'] = {'inputs': ['ds_replacement_d2_058'], 'func': ds_replacement_d3_058}


def ds_replacement_d3_059(ds_replacement_d2_059):
    feature = _clean(ds_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_059'] = {'inputs': ['ds_replacement_d2_059'], 'func': ds_replacement_d3_059}


def ds_replacement_d3_060(ds_replacement_d2_060):
    feature = _clean(ds_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_060'] = {'inputs': ['ds_replacement_d2_060'], 'func': ds_replacement_d3_060}


def ds_replacement_d3_061(ds_replacement_d2_061):
    feature = _clean(ds_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_061'] = {'inputs': ['ds_replacement_d2_061'], 'func': ds_replacement_d3_061}


def ds_replacement_d3_062(ds_replacement_d2_062):
    feature = _clean(ds_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_062'] = {'inputs': ['ds_replacement_d2_062'], 'func': ds_replacement_d3_062}


def ds_replacement_d3_063(ds_replacement_d2_063):
    feature = _clean(ds_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_063'] = {'inputs': ['ds_replacement_d2_063'], 'func': ds_replacement_d3_063}


def ds_replacement_d3_064(ds_replacement_d2_064):
    feature = _clean(ds_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_064'] = {'inputs': ['ds_replacement_d2_064'], 'func': ds_replacement_d3_064}


def ds_replacement_d3_065(ds_replacement_d2_065):
    feature = _clean(ds_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_065'] = {'inputs': ['ds_replacement_d2_065'], 'func': ds_replacement_d3_065}


def ds_replacement_d3_066(ds_replacement_d2_066):
    feature = _clean(ds_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_066'] = {'inputs': ['ds_replacement_d2_066'], 'func': ds_replacement_d3_066}


def ds_replacement_d3_067(ds_replacement_d2_067):
    feature = _clean(ds_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_067'] = {'inputs': ['ds_replacement_d2_067'], 'func': ds_replacement_d3_067}


def ds_replacement_d3_068(ds_replacement_d2_068):
    feature = _clean(ds_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_068'] = {'inputs': ['ds_replacement_d2_068'], 'func': ds_replacement_d3_068}


def ds_replacement_d3_069(ds_replacement_d2_069):
    feature = _clean(ds_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_069'] = {'inputs': ['ds_replacement_d2_069'], 'func': ds_replacement_d3_069}


def ds_replacement_d3_070(ds_replacement_d2_070):
    feature = _clean(ds_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_070'] = {'inputs': ['ds_replacement_d2_070'], 'func': ds_replacement_d3_070}


def ds_replacement_d3_071(ds_replacement_d2_071):
    feature = _clean(ds_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_071'] = {'inputs': ['ds_replacement_d2_071'], 'func': ds_replacement_d3_071}


def ds_replacement_d3_072(ds_replacement_d2_072):
    feature = _clean(ds_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_072'] = {'inputs': ['ds_replacement_d2_072'], 'func': ds_replacement_d3_072}


def ds_replacement_d3_073(ds_replacement_d2_073):
    feature = _clean(ds_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_073'] = {'inputs': ['ds_replacement_d2_073'], 'func': ds_replacement_d3_073}


def ds_replacement_d3_074(ds_replacement_d2_074):
    feature = _clean(ds_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_074'] = {'inputs': ['ds_replacement_d2_074'], 'func': ds_replacement_d3_074}


def ds_replacement_d3_075(ds_replacement_d2_075):
    feature = _clean(ds_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_075'] = {'inputs': ['ds_replacement_d2_075'], 'func': ds_replacement_d3_075}


def ds_replacement_d3_076(ds_replacement_d2_076):
    feature = _clean(ds_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_076'] = {'inputs': ['ds_replacement_d2_076'], 'func': ds_replacement_d3_076}


def ds_replacement_d3_077(ds_replacement_d2_077):
    feature = _clean(ds_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_077'] = {'inputs': ['ds_replacement_d2_077'], 'func': ds_replacement_d3_077}


def ds_replacement_d3_078(ds_replacement_d2_078):
    feature = _clean(ds_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_078'] = {'inputs': ['ds_replacement_d2_078'], 'func': ds_replacement_d3_078}


def ds_replacement_d3_079(ds_replacement_d2_079):
    feature = _clean(ds_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_079'] = {'inputs': ['ds_replacement_d2_079'], 'func': ds_replacement_d3_079}


def ds_replacement_d3_080(ds_replacement_d2_080):
    feature = _clean(ds_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_080'] = {'inputs': ['ds_replacement_d2_080'], 'func': ds_replacement_d3_080}


def ds_replacement_d3_081(ds_replacement_d2_081):
    feature = _clean(ds_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_081'] = {'inputs': ['ds_replacement_d2_081'], 'func': ds_replacement_d3_081}


def ds_replacement_d3_082(ds_replacement_d2_082):
    feature = _clean(ds_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_082'] = {'inputs': ['ds_replacement_d2_082'], 'func': ds_replacement_d3_082}


def ds_replacement_d3_083(ds_replacement_d2_083):
    feature = _clean(ds_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_083'] = {'inputs': ['ds_replacement_d2_083'], 'func': ds_replacement_d3_083}


def ds_replacement_d3_084(ds_replacement_d2_084):
    feature = _clean(ds_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_084'] = {'inputs': ['ds_replacement_d2_084'], 'func': ds_replacement_d3_084}


def ds_replacement_d3_085(ds_replacement_d2_085):
    feature = _clean(ds_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_085'] = {'inputs': ['ds_replacement_d2_085'], 'func': ds_replacement_d3_085}


def ds_replacement_d3_086(ds_replacement_d2_086):
    feature = _clean(ds_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_086'] = {'inputs': ['ds_replacement_d2_086'], 'func': ds_replacement_d3_086}


def ds_replacement_d3_087(ds_replacement_d2_087):
    feature = _clean(ds_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_087'] = {'inputs': ['ds_replacement_d2_087'], 'func': ds_replacement_d3_087}


def ds_replacement_d3_088(ds_replacement_d2_088):
    feature = _clean(ds_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_088'] = {'inputs': ['ds_replacement_d2_088'], 'func': ds_replacement_d3_088}


def ds_replacement_d3_089(ds_replacement_d2_089):
    feature = _clean(ds_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_089'] = {'inputs': ['ds_replacement_d2_089'], 'func': ds_replacement_d3_089}


def ds_replacement_d3_090(ds_replacement_d2_090):
    feature = _clean(ds_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_090'] = {'inputs': ['ds_replacement_d2_090'], 'func': ds_replacement_d3_090}


def ds_replacement_d3_091(ds_replacement_d2_091):
    feature = _clean(ds_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_091'] = {'inputs': ['ds_replacement_d2_091'], 'func': ds_replacement_d3_091}


def ds_replacement_d3_092(ds_replacement_d2_092):
    feature = _clean(ds_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_092'] = {'inputs': ['ds_replacement_d2_092'], 'func': ds_replacement_d3_092}


def ds_replacement_d3_093(ds_replacement_d2_093):
    feature = _clean(ds_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_093'] = {'inputs': ['ds_replacement_d2_093'], 'func': ds_replacement_d3_093}


def ds_replacement_d3_094(ds_replacement_d2_094):
    feature = _clean(ds_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_094'] = {'inputs': ['ds_replacement_d2_094'], 'func': ds_replacement_d3_094}


def ds_replacement_d3_095(ds_replacement_d2_095):
    feature = _clean(ds_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_095'] = {'inputs': ['ds_replacement_d2_095'], 'func': ds_replacement_d3_095}


def ds_replacement_d3_096(ds_replacement_d2_096):
    feature = _clean(ds_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_096'] = {'inputs': ['ds_replacement_d2_096'], 'func': ds_replacement_d3_096}


def ds_replacement_d3_097(ds_replacement_d2_097):
    feature = _clean(ds_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_097'] = {'inputs': ['ds_replacement_d2_097'], 'func': ds_replacement_d3_097}


def ds_replacement_d3_098(ds_replacement_d2_098):
    feature = _clean(ds_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_098'] = {'inputs': ['ds_replacement_d2_098'], 'func': ds_replacement_d3_098}


def ds_replacement_d3_099(ds_replacement_d2_099):
    feature = _clean(ds_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_099'] = {'inputs': ['ds_replacement_d2_099'], 'func': ds_replacement_d3_099}


def ds_replacement_d3_100(ds_replacement_d2_100):
    feature = _clean(ds_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_100'] = {'inputs': ['ds_replacement_d2_100'], 'func': ds_replacement_d3_100}


def ds_replacement_d3_101(ds_replacement_d2_101):
    feature = _clean(ds_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_101'] = {'inputs': ['ds_replacement_d2_101'], 'func': ds_replacement_d3_101}


def ds_replacement_d3_102(ds_replacement_d2_102):
    feature = _clean(ds_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_102'] = {'inputs': ['ds_replacement_d2_102'], 'func': ds_replacement_d3_102}


def ds_replacement_d3_103(ds_replacement_d2_103):
    feature = _clean(ds_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_103'] = {'inputs': ['ds_replacement_d2_103'], 'func': ds_replacement_d3_103}


def ds_replacement_d3_104(ds_replacement_d2_104):
    feature = _clean(ds_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_104'] = {'inputs': ['ds_replacement_d2_104'], 'func': ds_replacement_d3_104}


def ds_replacement_d3_105(ds_replacement_d2_105):
    feature = _clean(ds_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_105'] = {'inputs': ['ds_replacement_d2_105'], 'func': ds_replacement_d3_105}


def ds_replacement_d3_106(ds_replacement_d2_106):
    feature = _clean(ds_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_106'] = {'inputs': ['ds_replacement_d2_106'], 'func': ds_replacement_d3_106}


def ds_replacement_d3_107(ds_replacement_d2_107):
    feature = _clean(ds_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_107'] = {'inputs': ['ds_replacement_d2_107'], 'func': ds_replacement_d3_107}


def ds_replacement_d3_108(ds_replacement_d2_108):
    feature = _clean(ds_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_108'] = {'inputs': ['ds_replacement_d2_108'], 'func': ds_replacement_d3_108}


def ds_replacement_d3_109(ds_replacement_d2_109):
    feature = _clean(ds_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_109'] = {'inputs': ['ds_replacement_d2_109'], 'func': ds_replacement_d3_109}


def ds_replacement_d3_110(ds_replacement_d2_110):
    feature = _clean(ds_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_110'] = {'inputs': ['ds_replacement_d2_110'], 'func': ds_replacement_d3_110}


def ds_replacement_d3_111(ds_replacement_d2_111):
    feature = _clean(ds_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_111'] = {'inputs': ['ds_replacement_d2_111'], 'func': ds_replacement_d3_111}


def ds_replacement_d3_112(ds_replacement_d2_112):
    feature = _clean(ds_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_112'] = {'inputs': ['ds_replacement_d2_112'], 'func': ds_replacement_d3_112}


def ds_replacement_d3_113(ds_replacement_d2_113):
    feature = _clean(ds_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_113'] = {'inputs': ['ds_replacement_d2_113'], 'func': ds_replacement_d3_113}


def ds_replacement_d3_114(ds_replacement_d2_114):
    feature = _clean(ds_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_114'] = {'inputs': ['ds_replacement_d2_114'], 'func': ds_replacement_d3_114}


def ds_replacement_d3_115(ds_replacement_d2_115):
    feature = _clean(ds_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_115'] = {'inputs': ['ds_replacement_d2_115'], 'func': ds_replacement_d3_115}


def ds_replacement_d3_116(ds_replacement_d2_116):
    feature = _clean(ds_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_116'] = {'inputs': ['ds_replacement_d2_116'], 'func': ds_replacement_d3_116}


def ds_replacement_d3_117(ds_replacement_d2_117):
    feature = _clean(ds_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_117'] = {'inputs': ['ds_replacement_d2_117'], 'func': ds_replacement_d3_117}


def ds_replacement_d3_118(ds_replacement_d2_118):
    feature = _clean(ds_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_118'] = {'inputs': ['ds_replacement_d2_118'], 'func': ds_replacement_d3_118}


def ds_replacement_d3_119(ds_replacement_d2_119):
    feature = _clean(ds_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_119'] = {'inputs': ['ds_replacement_d2_119'], 'func': ds_replacement_d3_119}


def ds_replacement_d3_120(ds_replacement_d2_120):
    feature = _clean(ds_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_120'] = {'inputs': ['ds_replacement_d2_120'], 'func': ds_replacement_d3_120}


def ds_replacement_d3_121(ds_replacement_d2_121):
    feature = _clean(ds_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_121'] = {'inputs': ['ds_replacement_d2_121'], 'func': ds_replacement_d3_121}


def ds_replacement_d3_122(ds_replacement_d2_122):
    feature = _clean(ds_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_122'] = {'inputs': ['ds_replacement_d2_122'], 'func': ds_replacement_d3_122}


def ds_replacement_d3_123(ds_replacement_d2_123):
    feature = _clean(ds_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_123'] = {'inputs': ['ds_replacement_d2_123'], 'func': ds_replacement_d3_123}


def ds_replacement_d3_124(ds_replacement_d2_124):
    feature = _clean(ds_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_124'] = {'inputs': ['ds_replacement_d2_124'], 'func': ds_replacement_d3_124}


def ds_replacement_d3_125(ds_replacement_d2_125):
    feature = _clean(ds_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_125'] = {'inputs': ['ds_replacement_d2_125'], 'func': ds_replacement_d3_125}


def ds_replacement_d3_126(ds_replacement_d2_126):
    feature = _clean(ds_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_126'] = {'inputs': ['ds_replacement_d2_126'], 'func': ds_replacement_d3_126}


def ds_replacement_d3_127(ds_replacement_d2_127):
    feature = _clean(ds_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_127'] = {'inputs': ['ds_replacement_d2_127'], 'func': ds_replacement_d3_127}


def ds_replacement_d3_128(ds_replacement_d2_128):
    feature = _clean(ds_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_128'] = {'inputs': ['ds_replacement_d2_128'], 'func': ds_replacement_d3_128}


def ds_replacement_d3_129(ds_replacement_d2_129):
    feature = _clean(ds_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_129'] = {'inputs': ['ds_replacement_d2_129'], 'func': ds_replacement_d3_129}


def ds_replacement_d3_130(ds_replacement_d2_130):
    feature = _clean(ds_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_130'] = {'inputs': ['ds_replacement_d2_130'], 'func': ds_replacement_d3_130}


def ds_replacement_d3_131(ds_replacement_d2_131):
    feature = _clean(ds_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_131'] = {'inputs': ['ds_replacement_d2_131'], 'func': ds_replacement_d3_131}


def ds_replacement_d3_132(ds_replacement_d2_132):
    feature = _clean(ds_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_132'] = {'inputs': ['ds_replacement_d2_132'], 'func': ds_replacement_d3_132}


def ds_replacement_d3_133(ds_replacement_d2_133):
    feature = _clean(ds_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_133'] = {'inputs': ['ds_replacement_d2_133'], 'func': ds_replacement_d3_133}


def ds_replacement_d3_134(ds_replacement_d2_134):
    feature = _clean(ds_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_134'] = {'inputs': ['ds_replacement_d2_134'], 'func': ds_replacement_d3_134}


def ds_replacement_d3_135(ds_replacement_d2_135):
    feature = _clean(ds_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_135'] = {'inputs': ['ds_replacement_d2_135'], 'func': ds_replacement_d3_135}


def ds_replacement_d3_136(ds_replacement_d2_136):
    feature = _clean(ds_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_136'] = {'inputs': ['ds_replacement_d2_136'], 'func': ds_replacement_d3_136}


def ds_replacement_d3_137(ds_replacement_d2_137):
    feature = _clean(ds_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_137'] = {'inputs': ['ds_replacement_d2_137'], 'func': ds_replacement_d3_137}


def ds_replacement_d3_138(ds_replacement_d2_138):
    feature = _clean(ds_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_138'] = {'inputs': ['ds_replacement_d2_138'], 'func': ds_replacement_d3_138}


def ds_replacement_d3_139(ds_replacement_d2_139):
    feature = _clean(ds_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_139'] = {'inputs': ['ds_replacement_d2_139'], 'func': ds_replacement_d3_139}


def ds_replacement_d3_140(ds_replacement_d2_140):
    feature = _clean(ds_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_140'] = {'inputs': ['ds_replacement_d2_140'], 'func': ds_replacement_d3_140}


def ds_replacement_d3_141(ds_replacement_d2_141):
    feature = _clean(ds_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_141'] = {'inputs': ['ds_replacement_d2_141'], 'func': ds_replacement_d3_141}


def ds_replacement_d3_142(ds_replacement_d2_142):
    feature = _clean(ds_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_142'] = {'inputs': ['ds_replacement_d2_142'], 'func': ds_replacement_d3_142}


def ds_replacement_d3_143(ds_replacement_d2_143):
    feature = _clean(ds_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_143'] = {'inputs': ['ds_replacement_d2_143'], 'func': ds_replacement_d3_143}


def ds_replacement_d3_144(ds_replacement_d2_144):
    feature = _clean(ds_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_144'] = {'inputs': ['ds_replacement_d2_144'], 'func': ds_replacement_d3_144}


def ds_replacement_d3_145(ds_replacement_d2_145):
    feature = _clean(ds_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_145'] = {'inputs': ['ds_replacement_d2_145'], 'func': ds_replacement_d3_145}


def ds_replacement_d3_146(ds_replacement_d2_146):
    feature = _clean(ds_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_146'] = {'inputs': ['ds_replacement_d2_146'], 'func': ds_replacement_d3_146}


def ds_replacement_d3_147(ds_replacement_d2_147):
    feature = _clean(ds_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_147'] = {'inputs': ['ds_replacement_d2_147'], 'func': ds_replacement_d3_147}


def ds_replacement_d3_148(ds_replacement_d2_148):
    feature = _clean(ds_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_148'] = {'inputs': ['ds_replacement_d2_148'], 'func': ds_replacement_d3_148}


def ds_replacement_d3_149(ds_replacement_d2_149):
    feature = _clean(ds_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_149'] = {'inputs': ['ds_replacement_d2_149'], 'func': ds_replacement_d3_149}


def ds_replacement_d3_150(ds_replacement_d2_150):
    feature = _clean(ds_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_150'] = {'inputs': ['ds_replacement_d2_150'], 'func': ds_replacement_d3_150}


def ds_replacement_d3_151(ds_replacement_d2_151):
    feature = _clean(ds_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_151'] = {'inputs': ['ds_replacement_d2_151'], 'func': ds_replacement_d3_151}


def ds_replacement_d3_152(ds_replacement_d2_152):
    feature = _clean(ds_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_152'] = {'inputs': ['ds_replacement_d2_152'], 'func': ds_replacement_d3_152}


def ds_replacement_d3_153(ds_replacement_d2_153):
    feature = _clean(ds_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_153'] = {'inputs': ['ds_replacement_d2_153'], 'func': ds_replacement_d3_153}


def ds_replacement_d3_154(ds_replacement_d2_154):
    feature = _clean(ds_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_154'] = {'inputs': ['ds_replacement_d2_154'], 'func': ds_replacement_d3_154}


def ds_replacement_d3_155(ds_replacement_d2_155):
    feature = _clean(ds_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_155'] = {'inputs': ['ds_replacement_d2_155'], 'func': ds_replacement_d3_155}


def ds_replacement_d3_156(ds_replacement_d2_156):
    feature = _clean(ds_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_156'] = {'inputs': ['ds_replacement_d2_156'], 'func': ds_replacement_d3_156}


def ds_replacement_d3_157(ds_replacement_d2_157):
    feature = _clean(ds_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_157'] = {'inputs': ['ds_replacement_d2_157'], 'func': ds_replacement_d3_157}


def ds_replacement_d3_158(ds_replacement_d2_158):
    feature = _clean(ds_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_158'] = {'inputs': ['ds_replacement_d2_158'], 'func': ds_replacement_d3_158}


def ds_replacement_d3_159(ds_replacement_d2_159):
    feature = _clean(ds_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_159'] = {'inputs': ['ds_replacement_d2_159'], 'func': ds_replacement_d3_159}


def ds_replacement_d3_160(ds_replacement_d2_160):
    feature = _clean(ds_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_160'] = {'inputs': ['ds_replacement_d2_160'], 'func': ds_replacement_d3_160}


def ds_replacement_d3_161(ds_replacement_d2_161):
    feature = _clean(ds_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_161'] = {'inputs': ['ds_replacement_d2_161'], 'func': ds_replacement_d3_161}


def ds_replacement_d3_162(ds_replacement_d2_162):
    feature = _clean(ds_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_162'] = {'inputs': ['ds_replacement_d2_162'], 'func': ds_replacement_d3_162}


def ds_replacement_d3_163(ds_replacement_d2_163):
    feature = _clean(ds_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_163'] = {'inputs': ['ds_replacement_d2_163'], 'func': ds_replacement_d3_163}


def ds_replacement_d3_164(ds_replacement_d2_164):
    feature = _clean(ds_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_164'] = {'inputs': ['ds_replacement_d2_164'], 'func': ds_replacement_d3_164}


def ds_replacement_d3_165(ds_replacement_d2_165):
    feature = _clean(ds_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_165'] = {'inputs': ['ds_replacement_d2_165'], 'func': ds_replacement_d3_165}


def ds_replacement_d3_166(ds_replacement_d2_166):
    feature = _clean(ds_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_166'] = {'inputs': ['ds_replacement_d2_166'], 'func': ds_replacement_d3_166}


def ds_replacement_d3_167(ds_replacement_d2_167):
    feature = _clean(ds_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_167'] = {'inputs': ['ds_replacement_d2_167'], 'func': ds_replacement_d3_167}


def ds_replacement_d3_168(ds_replacement_d2_168):
    feature = _clean(ds_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_168'] = {'inputs': ['ds_replacement_d2_168'], 'func': ds_replacement_d3_168}


def ds_replacement_d3_169(ds_replacement_d2_169):
    feature = _clean(ds_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_169'] = {'inputs': ['ds_replacement_d2_169'], 'func': ds_replacement_d3_169}


def ds_replacement_d3_170(ds_replacement_d2_170):
    feature = _clean(ds_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
DS_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ds_replacement_d3_170'] = {'inputs': ['ds_replacement_d2_170'], 'func': ds_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def dstk_base_universe_d3_001_dstk_002_zero_volume_frequency_10_002(dstk_base_universe_d2_001_dstk_002_zero_volume_frequency_10_002):
    return _base_universe_d3(dstk_base_universe_d2_001_dstk_002_zero_volume_frequency_10_002, 1)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_001_dstk_002_zero_volume_frequency_10_002'] = {'inputs': ['dstk_base_universe_d2_001_dstk_002_zero_volume_frequency_10_002'], 'func': dstk_base_universe_d3_001_dstk_002_zero_volume_frequency_10_002}


def dstk_base_universe_d3_002_dstk_003_spread_proxy_21_003(dstk_base_universe_d2_002_dstk_003_spread_proxy_21_003):
    return _base_universe_d3(dstk_base_universe_d2_002_dstk_003_spread_proxy_21_003, 2)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_002_dstk_003_spread_proxy_21_003'] = {'inputs': ['dstk_base_universe_d2_002_dstk_003_spread_proxy_21_003'], 'func': dstk_base_universe_d3_002_dstk_003_spread_proxy_21_003}


def dstk_base_universe_d3_003_dstk_004_trading_intensity_42_004(dstk_base_universe_d2_003_dstk_004_trading_intensity_42_004):
    return _base_universe_d3(dstk_base_universe_d2_003_dstk_004_trading_intensity_42_004, 3)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_003_dstk_004_trading_intensity_42_004'] = {'inputs': ['dstk_base_universe_d2_003_dstk_004_trading_intensity_42_004'], 'func': dstk_base_universe_d3_003_dstk_004_trading_intensity_42_004}


def dstk_base_universe_d3_004_dstk_006_price_level_distress_84_006(dstk_base_universe_d2_004_dstk_006_price_level_distress_84_006):
    return _base_universe_d3(dstk_base_universe_d2_004_dstk_006_price_level_distress_84_006, 4)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_004_dstk_006_price_level_distress_84_006'] = {'inputs': ['dstk_base_universe_d2_004_dstk_006_price_level_distress_84_006'], 'func': dstk_base_universe_d3_004_dstk_006_price_level_distress_84_006}


def dstk_base_universe_d3_005_dstk_008_zero_volume_frequency_189_008(dstk_base_universe_d2_005_dstk_008_zero_volume_frequency_189_008):
    return _base_universe_d3(dstk_base_universe_d2_005_dstk_008_zero_volume_frequency_189_008, 5)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_005_dstk_008_zero_volume_frequency_189_008'] = {'inputs': ['dstk_base_universe_d2_005_dstk_008_zero_volume_frequency_189_008'], 'func': dstk_base_universe_d3_005_dstk_008_zero_volume_frequency_189_008}


def dstk_base_universe_d3_006_dstk_009_spread_proxy_252_009(dstk_base_universe_d2_006_dstk_009_spread_proxy_252_009):
    return _base_universe_d3(dstk_base_universe_d2_006_dstk_009_spread_proxy_252_009, 6)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_006_dstk_009_spread_proxy_252_009'] = {'inputs': ['dstk_base_universe_d2_006_dstk_009_spread_proxy_252_009'], 'func': dstk_base_universe_d3_006_dstk_009_spread_proxy_252_009}


def dstk_base_universe_d3_007_dstk_010_trading_intensity_378_010(dstk_base_universe_d2_007_dstk_010_trading_intensity_378_010):
    return _base_universe_d3(dstk_base_universe_d2_007_dstk_010_trading_intensity_378_010, 7)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_007_dstk_010_trading_intensity_378_010'] = {'inputs': ['dstk_base_universe_d2_007_dstk_010_trading_intensity_378_010'], 'func': dstk_base_universe_d3_007_dstk_010_trading_intensity_378_010}


def dstk_base_universe_d3_008_dstk_012_price_level_distress_756_012(dstk_base_universe_d2_008_dstk_012_price_level_distress_756_012):
    return _base_universe_d3(dstk_base_universe_d2_008_dstk_012_price_level_distress_756_012, 8)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_008_dstk_012_price_level_distress_756_012'] = {'inputs': ['dstk_base_universe_d2_008_dstk_012_price_level_distress_756_012'], 'func': dstk_base_universe_d3_008_dstk_012_price_level_distress_756_012}


def dstk_base_universe_d3_009_dstk_014_zero_volume_frequency_1260_014(dstk_base_universe_d2_009_dstk_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(dstk_base_universe_d2_009_dstk_014_zero_volume_frequency_1260_014, 9)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_009_dstk_014_zero_volume_frequency_1260_014'] = {'inputs': ['dstk_base_universe_d2_009_dstk_014_zero_volume_frequency_1260_014'], 'func': dstk_base_universe_d3_009_dstk_014_zero_volume_frequency_1260_014}


def dstk_base_universe_d3_010_dstk_015_spread_proxy_1512_015(dstk_base_universe_d2_010_dstk_015_spread_proxy_1512_015):
    return _base_universe_d3(dstk_base_universe_d2_010_dstk_015_spread_proxy_1512_015, 10)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_010_dstk_015_spread_proxy_1512_015'] = {'inputs': ['dstk_base_universe_d2_010_dstk_015_spread_proxy_1512_015'], 'func': dstk_base_universe_d3_010_dstk_015_spread_proxy_1512_015}


def dstk_base_universe_d3_011_dstk_016_trading_intensity_5_016(dstk_base_universe_d2_011_dstk_016_trading_intensity_5_016):
    return _base_universe_d3(dstk_base_universe_d2_011_dstk_016_trading_intensity_5_016, 11)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_011_dstk_016_trading_intensity_5_016'] = {'inputs': ['dstk_base_universe_d2_011_dstk_016_trading_intensity_5_016'], 'func': dstk_base_universe_d3_011_dstk_016_trading_intensity_5_016}


def dstk_base_universe_d3_012_dstk_018_price_level_distress_21_018(dstk_base_universe_d2_012_dstk_018_price_level_distress_21_018):
    return _base_universe_d3(dstk_base_universe_d2_012_dstk_018_price_level_distress_21_018, 12)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_012_dstk_018_price_level_distress_21_018'] = {'inputs': ['dstk_base_universe_d2_012_dstk_018_price_level_distress_21_018'], 'func': dstk_base_universe_d3_012_dstk_018_price_level_distress_21_018}


def dstk_base_universe_d3_013_dstk_020_zero_volume_frequency_63_020(dstk_base_universe_d2_013_dstk_020_zero_volume_frequency_63_020):
    return _base_universe_d3(dstk_base_universe_d2_013_dstk_020_zero_volume_frequency_63_020, 13)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_013_dstk_020_zero_volume_frequency_63_020'] = {'inputs': ['dstk_base_universe_d2_013_dstk_020_zero_volume_frequency_63_020'], 'func': dstk_base_universe_d3_013_dstk_020_zero_volume_frequency_63_020}


def dstk_base_universe_d3_014_dstk_021_spread_proxy_84_021(dstk_base_universe_d2_014_dstk_021_spread_proxy_84_021):
    return _base_universe_d3(dstk_base_universe_d2_014_dstk_021_spread_proxy_84_021, 14)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_014_dstk_021_spread_proxy_84_021'] = {'inputs': ['dstk_base_universe_d2_014_dstk_021_spread_proxy_84_021'], 'func': dstk_base_universe_d3_014_dstk_021_spread_proxy_84_021}


def dstk_base_universe_d3_015_dstk_022_trading_intensity_126_022(dstk_base_universe_d2_015_dstk_022_trading_intensity_126_022):
    return _base_universe_d3(dstk_base_universe_d2_015_dstk_022_trading_intensity_126_022, 15)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_015_dstk_022_trading_intensity_126_022'] = {'inputs': ['dstk_base_universe_d2_015_dstk_022_trading_intensity_126_022'], 'func': dstk_base_universe_d3_015_dstk_022_trading_intensity_126_022}


def dstk_base_universe_d3_016_dstk_024_price_level_distress_252_024(dstk_base_universe_d2_016_dstk_024_price_level_distress_252_024):
    return _base_universe_d3(dstk_base_universe_d2_016_dstk_024_price_level_distress_252_024, 16)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_016_dstk_024_price_level_distress_252_024'] = {'inputs': ['dstk_base_universe_d2_016_dstk_024_price_level_distress_252_024'], 'func': dstk_base_universe_d3_016_dstk_024_price_level_distress_252_024}


def dstk_base_universe_d3_017_dstk_026_zero_volume_frequency_504_026(dstk_base_universe_d2_017_dstk_026_zero_volume_frequency_504_026):
    return _base_universe_d3(dstk_base_universe_d2_017_dstk_026_zero_volume_frequency_504_026, 17)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_017_dstk_026_zero_volume_frequency_504_026'] = {'inputs': ['dstk_base_universe_d2_017_dstk_026_zero_volume_frequency_504_026'], 'func': dstk_base_universe_d3_017_dstk_026_zero_volume_frequency_504_026}


def dstk_base_universe_d3_018_dstk_027_spread_proxy_756_027(dstk_base_universe_d2_018_dstk_027_spread_proxy_756_027):
    return _base_universe_d3(dstk_base_universe_d2_018_dstk_027_spread_proxy_756_027, 18)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_018_dstk_027_spread_proxy_756_027'] = {'inputs': ['dstk_base_universe_d2_018_dstk_027_spread_proxy_756_027'], 'func': dstk_base_universe_d3_018_dstk_027_spread_proxy_756_027}


def dstk_base_universe_d3_019_dstk_028_trading_intensity_1008_028(dstk_base_universe_d2_019_dstk_028_trading_intensity_1008_028):
    return _base_universe_d3(dstk_base_universe_d2_019_dstk_028_trading_intensity_1008_028, 19)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_019_dstk_028_trading_intensity_1008_028'] = {'inputs': ['dstk_base_universe_d2_019_dstk_028_trading_intensity_1008_028'], 'func': dstk_base_universe_d3_019_dstk_028_trading_intensity_1008_028}


def dstk_base_universe_d3_020_dstk_030_price_level_distress_1512_030(dstk_base_universe_d2_020_dstk_030_price_level_distress_1512_030):
    return _base_universe_d3(dstk_base_universe_d2_020_dstk_030_price_level_distress_1512_030, 20)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_020_dstk_030_price_level_distress_1512_030'] = {'inputs': ['dstk_base_universe_d2_020_dstk_030_price_level_distress_1512_030'], 'func': dstk_base_universe_d3_020_dstk_030_price_level_distress_1512_030}


def dstk_base_universe_d3_021_dstk_basefill_001(dstk_base_universe_d2_021_dstk_basefill_001):
    return _base_universe_d3(dstk_base_universe_d2_021_dstk_basefill_001, 21)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_021_dstk_basefill_001'] = {'inputs': ['dstk_base_universe_d2_021_dstk_basefill_001'], 'func': dstk_base_universe_d3_021_dstk_basefill_001}


def dstk_base_universe_d3_022_dstk_basefill_005(dstk_base_universe_d2_022_dstk_basefill_005):
    return _base_universe_d3(dstk_base_universe_d2_022_dstk_basefill_005, 22)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_022_dstk_basefill_005'] = {'inputs': ['dstk_base_universe_d2_022_dstk_basefill_005'], 'func': dstk_base_universe_d3_022_dstk_basefill_005}


def dstk_base_universe_d3_023_dstk_basefill_007(dstk_base_universe_d2_023_dstk_basefill_007):
    return _base_universe_d3(dstk_base_universe_d2_023_dstk_basefill_007, 23)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_023_dstk_basefill_007'] = {'inputs': ['dstk_base_universe_d2_023_dstk_basefill_007'], 'func': dstk_base_universe_d3_023_dstk_basefill_007}


def dstk_base_universe_d3_024_dstk_basefill_011(dstk_base_universe_d2_024_dstk_basefill_011):
    return _base_universe_d3(dstk_base_universe_d2_024_dstk_basefill_011, 24)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_024_dstk_basefill_011'] = {'inputs': ['dstk_base_universe_d2_024_dstk_basefill_011'], 'func': dstk_base_universe_d3_024_dstk_basefill_011}


def dstk_base_universe_d3_025_dstk_basefill_013(dstk_base_universe_d2_025_dstk_basefill_013):
    return _base_universe_d3(dstk_base_universe_d2_025_dstk_basefill_013, 25)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_025_dstk_basefill_013'] = {'inputs': ['dstk_base_universe_d2_025_dstk_basefill_013'], 'func': dstk_base_universe_d3_025_dstk_basefill_013}


def dstk_base_universe_d3_026_dstk_basefill_017(dstk_base_universe_d2_026_dstk_basefill_017):
    return _base_universe_d3(dstk_base_universe_d2_026_dstk_basefill_017, 26)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_026_dstk_basefill_017'] = {'inputs': ['dstk_base_universe_d2_026_dstk_basefill_017'], 'func': dstk_base_universe_d3_026_dstk_basefill_017}


def dstk_base_universe_d3_027_dstk_basefill_019(dstk_base_universe_d2_027_dstk_basefill_019):
    return _base_universe_d3(dstk_base_universe_d2_027_dstk_basefill_019, 27)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_027_dstk_basefill_019'] = {'inputs': ['dstk_base_universe_d2_027_dstk_basefill_019'], 'func': dstk_base_universe_d3_027_dstk_basefill_019}


def dstk_base_universe_d3_028_dstk_basefill_023(dstk_base_universe_d2_028_dstk_basefill_023):
    return _base_universe_d3(dstk_base_universe_d2_028_dstk_basefill_023, 28)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_028_dstk_basefill_023'] = {'inputs': ['dstk_base_universe_d2_028_dstk_basefill_023'], 'func': dstk_base_universe_d3_028_dstk_basefill_023}


def dstk_base_universe_d3_029_dstk_basefill_025(dstk_base_universe_d2_029_dstk_basefill_025):
    return _base_universe_d3(dstk_base_universe_d2_029_dstk_basefill_025, 29)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_029_dstk_basefill_025'] = {'inputs': ['dstk_base_universe_d2_029_dstk_basefill_025'], 'func': dstk_base_universe_d3_029_dstk_basefill_025}


def dstk_base_universe_d3_030_dstk_basefill_029(dstk_base_universe_d2_030_dstk_basefill_029):
    return _base_universe_d3(dstk_base_universe_d2_030_dstk_basefill_029, 30)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_030_dstk_basefill_029'] = {'inputs': ['dstk_base_universe_d2_030_dstk_basefill_029'], 'func': dstk_base_universe_d3_030_dstk_basefill_029}


def dstk_base_universe_d3_031_dstk_basefill_031(dstk_base_universe_d2_031_dstk_basefill_031):
    return _base_universe_d3(dstk_base_universe_d2_031_dstk_basefill_031, 31)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_031_dstk_basefill_031'] = {'inputs': ['dstk_base_universe_d2_031_dstk_basefill_031'], 'func': dstk_base_universe_d3_031_dstk_basefill_031}


def dstk_base_universe_d3_032_dstk_basefill_032(dstk_base_universe_d2_032_dstk_basefill_032):
    return _base_universe_d3(dstk_base_universe_d2_032_dstk_basefill_032, 32)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_032_dstk_basefill_032'] = {'inputs': ['dstk_base_universe_d2_032_dstk_basefill_032'], 'func': dstk_base_universe_d3_032_dstk_basefill_032}


def dstk_base_universe_d3_033_dstk_basefill_033(dstk_base_universe_d2_033_dstk_basefill_033):
    return _base_universe_d3(dstk_base_universe_d2_033_dstk_basefill_033, 33)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_033_dstk_basefill_033'] = {'inputs': ['dstk_base_universe_d2_033_dstk_basefill_033'], 'func': dstk_base_universe_d3_033_dstk_basefill_033}


def dstk_base_universe_d3_034_dstk_basefill_034(dstk_base_universe_d2_034_dstk_basefill_034):
    return _base_universe_d3(dstk_base_universe_d2_034_dstk_basefill_034, 34)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_034_dstk_basefill_034'] = {'inputs': ['dstk_base_universe_d2_034_dstk_basefill_034'], 'func': dstk_base_universe_d3_034_dstk_basefill_034}


def dstk_base_universe_d3_035_dstk_basefill_035(dstk_base_universe_d2_035_dstk_basefill_035):
    return _base_universe_d3(dstk_base_universe_d2_035_dstk_basefill_035, 35)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_035_dstk_basefill_035'] = {'inputs': ['dstk_base_universe_d2_035_dstk_basefill_035'], 'func': dstk_base_universe_d3_035_dstk_basefill_035}


def dstk_base_universe_d3_036_dstk_basefill_036(dstk_base_universe_d2_036_dstk_basefill_036):
    return _base_universe_d3(dstk_base_universe_d2_036_dstk_basefill_036, 36)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_036_dstk_basefill_036'] = {'inputs': ['dstk_base_universe_d2_036_dstk_basefill_036'], 'func': dstk_base_universe_d3_036_dstk_basefill_036}


def dstk_base_universe_d3_037_dstk_basefill_037(dstk_base_universe_d2_037_dstk_basefill_037):
    return _base_universe_d3(dstk_base_universe_d2_037_dstk_basefill_037, 37)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_037_dstk_basefill_037'] = {'inputs': ['dstk_base_universe_d2_037_dstk_basefill_037'], 'func': dstk_base_universe_d3_037_dstk_basefill_037}


def dstk_base_universe_d3_038_dstk_basefill_038(dstk_base_universe_d2_038_dstk_basefill_038):
    return _base_universe_d3(dstk_base_universe_d2_038_dstk_basefill_038, 38)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_038_dstk_basefill_038'] = {'inputs': ['dstk_base_universe_d2_038_dstk_basefill_038'], 'func': dstk_base_universe_d3_038_dstk_basefill_038}


def dstk_base_universe_d3_039_dstk_basefill_039(dstk_base_universe_d2_039_dstk_basefill_039):
    return _base_universe_d3(dstk_base_universe_d2_039_dstk_basefill_039, 39)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_039_dstk_basefill_039'] = {'inputs': ['dstk_base_universe_d2_039_dstk_basefill_039'], 'func': dstk_base_universe_d3_039_dstk_basefill_039}


def dstk_base_universe_d3_040_dstk_basefill_040(dstk_base_universe_d2_040_dstk_basefill_040):
    return _base_universe_d3(dstk_base_universe_d2_040_dstk_basefill_040, 40)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_040_dstk_basefill_040'] = {'inputs': ['dstk_base_universe_d2_040_dstk_basefill_040'], 'func': dstk_base_universe_d3_040_dstk_basefill_040}


def dstk_base_universe_d3_041_dstk_basefill_041(dstk_base_universe_d2_041_dstk_basefill_041):
    return _base_universe_d3(dstk_base_universe_d2_041_dstk_basefill_041, 41)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_041_dstk_basefill_041'] = {'inputs': ['dstk_base_universe_d2_041_dstk_basefill_041'], 'func': dstk_base_universe_d3_041_dstk_basefill_041}


def dstk_base_universe_d3_042_dstk_basefill_042(dstk_base_universe_d2_042_dstk_basefill_042):
    return _base_universe_d3(dstk_base_universe_d2_042_dstk_basefill_042, 42)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_042_dstk_basefill_042'] = {'inputs': ['dstk_base_universe_d2_042_dstk_basefill_042'], 'func': dstk_base_universe_d3_042_dstk_basefill_042}


def dstk_base_universe_d3_043_dstk_basefill_043(dstk_base_universe_d2_043_dstk_basefill_043):
    return _base_universe_d3(dstk_base_universe_d2_043_dstk_basefill_043, 43)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_043_dstk_basefill_043'] = {'inputs': ['dstk_base_universe_d2_043_dstk_basefill_043'], 'func': dstk_base_universe_d3_043_dstk_basefill_043}


def dstk_base_universe_d3_044_dstk_basefill_044(dstk_base_universe_d2_044_dstk_basefill_044):
    return _base_universe_d3(dstk_base_universe_d2_044_dstk_basefill_044, 44)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_044_dstk_basefill_044'] = {'inputs': ['dstk_base_universe_d2_044_dstk_basefill_044'], 'func': dstk_base_universe_d3_044_dstk_basefill_044}


def dstk_base_universe_d3_045_dstk_basefill_045(dstk_base_universe_d2_045_dstk_basefill_045):
    return _base_universe_d3(dstk_base_universe_d2_045_dstk_basefill_045, 45)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_045_dstk_basefill_045'] = {'inputs': ['dstk_base_universe_d2_045_dstk_basefill_045'], 'func': dstk_base_universe_d3_045_dstk_basefill_045}


def dstk_base_universe_d3_046_dstk_basefill_046(dstk_base_universe_d2_046_dstk_basefill_046):
    return _base_universe_d3(dstk_base_universe_d2_046_dstk_basefill_046, 46)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_046_dstk_basefill_046'] = {'inputs': ['dstk_base_universe_d2_046_dstk_basefill_046'], 'func': dstk_base_universe_d3_046_dstk_basefill_046}


def dstk_base_universe_d3_047_dstk_basefill_047(dstk_base_universe_d2_047_dstk_basefill_047):
    return _base_universe_d3(dstk_base_universe_d2_047_dstk_basefill_047, 47)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_047_dstk_basefill_047'] = {'inputs': ['dstk_base_universe_d2_047_dstk_basefill_047'], 'func': dstk_base_universe_d3_047_dstk_basefill_047}


def dstk_base_universe_d3_048_dstk_basefill_048(dstk_base_universe_d2_048_dstk_basefill_048):
    return _base_universe_d3(dstk_base_universe_d2_048_dstk_basefill_048, 48)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_048_dstk_basefill_048'] = {'inputs': ['dstk_base_universe_d2_048_dstk_basefill_048'], 'func': dstk_base_universe_d3_048_dstk_basefill_048}


def dstk_base_universe_d3_049_dstk_basefill_049(dstk_base_universe_d2_049_dstk_basefill_049):
    return _base_universe_d3(dstk_base_universe_d2_049_dstk_basefill_049, 49)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_049_dstk_basefill_049'] = {'inputs': ['dstk_base_universe_d2_049_dstk_basefill_049'], 'func': dstk_base_universe_d3_049_dstk_basefill_049}


def dstk_base_universe_d3_050_dstk_basefill_050(dstk_base_universe_d2_050_dstk_basefill_050):
    return _base_universe_d3(dstk_base_universe_d2_050_dstk_basefill_050, 50)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_050_dstk_basefill_050'] = {'inputs': ['dstk_base_universe_d2_050_dstk_basefill_050'], 'func': dstk_base_universe_d3_050_dstk_basefill_050}


def dstk_base_universe_d3_051_dstk_basefill_051(dstk_base_universe_d2_051_dstk_basefill_051):
    return _base_universe_d3(dstk_base_universe_d2_051_dstk_basefill_051, 51)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_051_dstk_basefill_051'] = {'inputs': ['dstk_base_universe_d2_051_dstk_basefill_051'], 'func': dstk_base_universe_d3_051_dstk_basefill_051}


def dstk_base_universe_d3_052_dstk_basefill_052(dstk_base_universe_d2_052_dstk_basefill_052):
    return _base_universe_d3(dstk_base_universe_d2_052_dstk_basefill_052, 52)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_052_dstk_basefill_052'] = {'inputs': ['dstk_base_universe_d2_052_dstk_basefill_052'], 'func': dstk_base_universe_d3_052_dstk_basefill_052}


def dstk_base_universe_d3_053_dstk_basefill_053(dstk_base_universe_d2_053_dstk_basefill_053):
    return _base_universe_d3(dstk_base_universe_d2_053_dstk_basefill_053, 53)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_053_dstk_basefill_053'] = {'inputs': ['dstk_base_universe_d2_053_dstk_basefill_053'], 'func': dstk_base_universe_d3_053_dstk_basefill_053}


def dstk_base_universe_d3_054_dstk_basefill_054(dstk_base_universe_d2_054_dstk_basefill_054):
    return _base_universe_d3(dstk_base_universe_d2_054_dstk_basefill_054, 54)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_054_dstk_basefill_054'] = {'inputs': ['dstk_base_universe_d2_054_dstk_basefill_054'], 'func': dstk_base_universe_d3_054_dstk_basefill_054}


def dstk_base_universe_d3_055_dstk_basefill_055(dstk_base_universe_d2_055_dstk_basefill_055):
    return _base_universe_d3(dstk_base_universe_d2_055_dstk_basefill_055, 55)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_055_dstk_basefill_055'] = {'inputs': ['dstk_base_universe_d2_055_dstk_basefill_055'], 'func': dstk_base_universe_d3_055_dstk_basefill_055}


def dstk_base_universe_d3_056_dstk_basefill_056(dstk_base_universe_d2_056_dstk_basefill_056):
    return _base_universe_d3(dstk_base_universe_d2_056_dstk_basefill_056, 56)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_056_dstk_basefill_056'] = {'inputs': ['dstk_base_universe_d2_056_dstk_basefill_056'], 'func': dstk_base_universe_d3_056_dstk_basefill_056}


def dstk_base_universe_d3_057_dstk_basefill_057(dstk_base_universe_d2_057_dstk_basefill_057):
    return _base_universe_d3(dstk_base_universe_d2_057_dstk_basefill_057, 57)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_057_dstk_basefill_057'] = {'inputs': ['dstk_base_universe_d2_057_dstk_basefill_057'], 'func': dstk_base_universe_d3_057_dstk_basefill_057}


def dstk_base_universe_d3_058_dstk_basefill_058(dstk_base_universe_d2_058_dstk_basefill_058):
    return _base_universe_d3(dstk_base_universe_d2_058_dstk_basefill_058, 58)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_058_dstk_basefill_058'] = {'inputs': ['dstk_base_universe_d2_058_dstk_basefill_058'], 'func': dstk_base_universe_d3_058_dstk_basefill_058}


def dstk_base_universe_d3_059_dstk_basefill_059(dstk_base_universe_d2_059_dstk_basefill_059):
    return _base_universe_d3(dstk_base_universe_d2_059_dstk_basefill_059, 59)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_059_dstk_basefill_059'] = {'inputs': ['dstk_base_universe_d2_059_dstk_basefill_059'], 'func': dstk_base_universe_d3_059_dstk_basefill_059}


def dstk_base_universe_d3_060_dstk_basefill_060(dstk_base_universe_d2_060_dstk_basefill_060):
    return _base_universe_d3(dstk_base_universe_d2_060_dstk_basefill_060, 60)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_060_dstk_basefill_060'] = {'inputs': ['dstk_base_universe_d2_060_dstk_basefill_060'], 'func': dstk_base_universe_d3_060_dstk_basefill_060}


def dstk_base_universe_d3_061_dstk_basefill_061(dstk_base_universe_d2_061_dstk_basefill_061):
    return _base_universe_d3(dstk_base_universe_d2_061_dstk_basefill_061, 61)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_061_dstk_basefill_061'] = {'inputs': ['dstk_base_universe_d2_061_dstk_basefill_061'], 'func': dstk_base_universe_d3_061_dstk_basefill_061}


def dstk_base_universe_d3_062_dstk_basefill_062(dstk_base_universe_d2_062_dstk_basefill_062):
    return _base_universe_d3(dstk_base_universe_d2_062_dstk_basefill_062, 62)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_062_dstk_basefill_062'] = {'inputs': ['dstk_base_universe_d2_062_dstk_basefill_062'], 'func': dstk_base_universe_d3_062_dstk_basefill_062}


def dstk_base_universe_d3_063_dstk_basefill_063(dstk_base_universe_d2_063_dstk_basefill_063):
    return _base_universe_d3(dstk_base_universe_d2_063_dstk_basefill_063, 63)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_063_dstk_basefill_063'] = {'inputs': ['dstk_base_universe_d2_063_dstk_basefill_063'], 'func': dstk_base_universe_d3_063_dstk_basefill_063}


def dstk_base_universe_d3_064_dstk_basefill_064(dstk_base_universe_d2_064_dstk_basefill_064):
    return _base_universe_d3(dstk_base_universe_d2_064_dstk_basefill_064, 64)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_064_dstk_basefill_064'] = {'inputs': ['dstk_base_universe_d2_064_dstk_basefill_064'], 'func': dstk_base_universe_d3_064_dstk_basefill_064}


def dstk_base_universe_d3_065_dstk_basefill_065(dstk_base_universe_d2_065_dstk_basefill_065):
    return _base_universe_d3(dstk_base_universe_d2_065_dstk_basefill_065, 65)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_065_dstk_basefill_065'] = {'inputs': ['dstk_base_universe_d2_065_dstk_basefill_065'], 'func': dstk_base_universe_d3_065_dstk_basefill_065}


def dstk_base_universe_d3_066_dstk_basefill_066(dstk_base_universe_d2_066_dstk_basefill_066):
    return _base_universe_d3(dstk_base_universe_d2_066_dstk_basefill_066, 66)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_066_dstk_basefill_066'] = {'inputs': ['dstk_base_universe_d2_066_dstk_basefill_066'], 'func': dstk_base_universe_d3_066_dstk_basefill_066}


def dstk_base_universe_d3_067_dstk_basefill_067(dstk_base_universe_d2_067_dstk_basefill_067):
    return _base_universe_d3(dstk_base_universe_d2_067_dstk_basefill_067, 67)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_067_dstk_basefill_067'] = {'inputs': ['dstk_base_universe_d2_067_dstk_basefill_067'], 'func': dstk_base_universe_d3_067_dstk_basefill_067}


def dstk_base_universe_d3_068_dstk_basefill_068(dstk_base_universe_d2_068_dstk_basefill_068):
    return _base_universe_d3(dstk_base_universe_d2_068_dstk_basefill_068, 68)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_068_dstk_basefill_068'] = {'inputs': ['dstk_base_universe_d2_068_dstk_basefill_068'], 'func': dstk_base_universe_d3_068_dstk_basefill_068}


def dstk_base_universe_d3_069_dstk_basefill_069(dstk_base_universe_d2_069_dstk_basefill_069):
    return _base_universe_d3(dstk_base_universe_d2_069_dstk_basefill_069, 69)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_069_dstk_basefill_069'] = {'inputs': ['dstk_base_universe_d2_069_dstk_basefill_069'], 'func': dstk_base_universe_d3_069_dstk_basefill_069}


def dstk_base_universe_d3_070_dstk_basefill_070(dstk_base_universe_d2_070_dstk_basefill_070):
    return _base_universe_d3(dstk_base_universe_d2_070_dstk_basefill_070, 70)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_070_dstk_basefill_070'] = {'inputs': ['dstk_base_universe_d2_070_dstk_basefill_070'], 'func': dstk_base_universe_d3_070_dstk_basefill_070}


def dstk_base_universe_d3_071_dstk_basefill_071(dstk_base_universe_d2_071_dstk_basefill_071):
    return _base_universe_d3(dstk_base_universe_d2_071_dstk_basefill_071, 71)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_071_dstk_basefill_071'] = {'inputs': ['dstk_base_universe_d2_071_dstk_basefill_071'], 'func': dstk_base_universe_d3_071_dstk_basefill_071}


def dstk_base_universe_d3_072_dstk_basefill_072(dstk_base_universe_d2_072_dstk_basefill_072):
    return _base_universe_d3(dstk_base_universe_d2_072_dstk_basefill_072, 72)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_072_dstk_basefill_072'] = {'inputs': ['dstk_base_universe_d2_072_dstk_basefill_072'], 'func': dstk_base_universe_d3_072_dstk_basefill_072}


def dstk_base_universe_d3_073_dstk_basefill_073(dstk_base_universe_d2_073_dstk_basefill_073):
    return _base_universe_d3(dstk_base_universe_d2_073_dstk_basefill_073, 73)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_073_dstk_basefill_073'] = {'inputs': ['dstk_base_universe_d2_073_dstk_basefill_073'], 'func': dstk_base_universe_d3_073_dstk_basefill_073}


def dstk_base_universe_d3_074_dstk_basefill_074(dstk_base_universe_d2_074_dstk_basefill_074):
    return _base_universe_d3(dstk_base_universe_d2_074_dstk_basefill_074, 74)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_074_dstk_basefill_074'] = {'inputs': ['dstk_base_universe_d2_074_dstk_basefill_074'], 'func': dstk_base_universe_d3_074_dstk_basefill_074}


def dstk_base_universe_d3_075_dstk_basefill_075(dstk_base_universe_d2_075_dstk_basefill_075):
    return _base_universe_d3(dstk_base_universe_d2_075_dstk_basefill_075, 75)
DSTK_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['dstk_base_universe_d3_075_dstk_basefill_075'] = {'inputs': ['dstk_base_universe_d2_075_dstk_basefill_075'], 'func': dstk_base_universe_d3_075_dstk_basefill_075}
