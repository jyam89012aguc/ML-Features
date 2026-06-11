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



def pcmp_001_amihud_illiquidity_accel_1(pcmp_001_amihud_illiquidity_roc_1):
    feature = _s(pcmp_001_amihud_illiquidity_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def pcmp_007_amihud_illiquidity_accel_5(pcmp_007_amihud_illiquidity_roc_5):
    feature = _s(pcmp_007_amihud_illiquidity_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def pcmp_013_amihud_illiquidity_accel_42(pcmp_013_amihud_illiquidity_roc_42):
    feature = _s(pcmp_013_amihud_illiquidity_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def pcmp_179_pcmp_019_amihud_illiquidity_42_019_accel_126(pcmp_154_pcmp_019_amihud_illiquidity_42_019_roc_126):
    feature = _s(pcmp_154_pcmp_019_amihud_illiquidity_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def pcmp_180_pcmp_025_amihud_illiquidity_378_025_accel_378(pcmp_155_pcmp_025_amihud_illiquidity_378_025_roc_378):
    feature = _s(pcmp_155_pcmp_025_amihud_illiquidity_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















PRICE_COMPRESSION_REGISTRY_3RD_DERIVATIVES = {
    'pcmp_001_amihud_illiquidity_accel_1': {'inputs': ['pcmp_001_amihud_illiquidity_roc_1'], 'func': pcmp_001_amihud_illiquidity_accel_1},
    'pcmp_007_amihud_illiquidity_accel_5': {'inputs': ['pcmp_007_amihud_illiquidity_roc_5'], 'func': pcmp_007_amihud_illiquidity_accel_5},
    'pcmp_013_amihud_illiquidity_accel_42': {'inputs': ['pcmp_013_amihud_illiquidity_roc_42'], 'func': pcmp_013_amihud_illiquidity_accel_42},
    'pcmp_179_pcmp_019_amihud_illiquidity_42_019_accel_126': {'inputs': ['pcmp_154_pcmp_019_amihud_illiquidity_42_019_roc_126'], 'func': pcmp_179_pcmp_019_amihud_illiquidity_42_019_accel_126},
    'pcmp_180_pcmp_025_amihud_illiquidity_378_025_accel_378': {'inputs': ['pcmp_155_pcmp_025_amihud_illiquidity_378_025_roc_378'], 'func': pcmp_180_pcmp_025_amihud_illiquidity_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def pc_replacement_d3_001(pc_replacement_d2_001):
    feature = _clean(pc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_001'] = {'inputs': ['pc_replacement_d2_001'], 'func': pc_replacement_d3_001}


def pc_replacement_d3_002(pc_replacement_d2_002):
    feature = _clean(pc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_002'] = {'inputs': ['pc_replacement_d2_002'], 'func': pc_replacement_d3_002}


def pc_replacement_d3_003(pc_replacement_d2_003):
    feature = _clean(pc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_003'] = {'inputs': ['pc_replacement_d2_003'], 'func': pc_replacement_d3_003}


def pc_replacement_d3_004(pc_replacement_d2_004):
    feature = _clean(pc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_004'] = {'inputs': ['pc_replacement_d2_004'], 'func': pc_replacement_d3_004}


def pc_replacement_d3_005(pc_replacement_d2_005):
    feature = _clean(pc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_005'] = {'inputs': ['pc_replacement_d2_005'], 'func': pc_replacement_d3_005}


def pc_replacement_d3_006(pc_replacement_d2_006):
    feature = _clean(pc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_006'] = {'inputs': ['pc_replacement_d2_006'], 'func': pc_replacement_d3_006}


def pc_replacement_d3_007(pc_replacement_d2_007):
    feature = _clean(pc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_007'] = {'inputs': ['pc_replacement_d2_007'], 'func': pc_replacement_d3_007}


def pc_replacement_d3_008(pc_replacement_d2_008):
    feature = _clean(pc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_008'] = {'inputs': ['pc_replacement_d2_008'], 'func': pc_replacement_d3_008}


def pc_replacement_d3_009(pc_replacement_d2_009):
    feature = _clean(pc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_009'] = {'inputs': ['pc_replacement_d2_009'], 'func': pc_replacement_d3_009}


def pc_replacement_d3_010(pc_replacement_d2_010):
    feature = _clean(pc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_010'] = {'inputs': ['pc_replacement_d2_010'], 'func': pc_replacement_d3_010}


def pc_replacement_d3_011(pc_replacement_d2_011):
    feature = _clean(pc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_011'] = {'inputs': ['pc_replacement_d2_011'], 'func': pc_replacement_d3_011}


def pc_replacement_d3_012(pc_replacement_d2_012):
    feature = _clean(pc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_012'] = {'inputs': ['pc_replacement_d2_012'], 'func': pc_replacement_d3_012}


def pc_replacement_d3_013(pc_replacement_d2_013):
    feature = _clean(pc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_013'] = {'inputs': ['pc_replacement_d2_013'], 'func': pc_replacement_d3_013}


def pc_replacement_d3_014(pc_replacement_d2_014):
    feature = _clean(pc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_014'] = {'inputs': ['pc_replacement_d2_014'], 'func': pc_replacement_d3_014}


def pc_replacement_d3_015(pc_replacement_d2_015):
    feature = _clean(pc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_015'] = {'inputs': ['pc_replacement_d2_015'], 'func': pc_replacement_d3_015}


def pc_replacement_d3_016(pc_replacement_d2_016):
    feature = _clean(pc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_016'] = {'inputs': ['pc_replacement_d2_016'], 'func': pc_replacement_d3_016}


def pc_replacement_d3_017(pc_replacement_d2_017):
    feature = _clean(pc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_017'] = {'inputs': ['pc_replacement_d2_017'], 'func': pc_replacement_d3_017}


def pc_replacement_d3_018(pc_replacement_d2_018):
    feature = _clean(pc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_018'] = {'inputs': ['pc_replacement_d2_018'], 'func': pc_replacement_d3_018}


def pc_replacement_d3_019(pc_replacement_d2_019):
    feature = _clean(pc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_019'] = {'inputs': ['pc_replacement_d2_019'], 'func': pc_replacement_d3_019}


def pc_replacement_d3_020(pc_replacement_d2_020):
    feature = _clean(pc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_020'] = {'inputs': ['pc_replacement_d2_020'], 'func': pc_replacement_d3_020}


def pc_replacement_d3_021(pc_replacement_d2_021):
    feature = _clean(pc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_021'] = {'inputs': ['pc_replacement_d2_021'], 'func': pc_replacement_d3_021}


def pc_replacement_d3_022(pc_replacement_d2_022):
    feature = _clean(pc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_022'] = {'inputs': ['pc_replacement_d2_022'], 'func': pc_replacement_d3_022}


def pc_replacement_d3_023(pc_replacement_d2_023):
    feature = _clean(pc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_023'] = {'inputs': ['pc_replacement_d2_023'], 'func': pc_replacement_d3_023}


def pc_replacement_d3_024(pc_replacement_d2_024):
    feature = _clean(pc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_024'] = {'inputs': ['pc_replacement_d2_024'], 'func': pc_replacement_d3_024}


def pc_replacement_d3_025(pc_replacement_d2_025):
    feature = _clean(pc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_025'] = {'inputs': ['pc_replacement_d2_025'], 'func': pc_replacement_d3_025}


def pc_replacement_d3_026(pc_replacement_d2_026):
    feature = _clean(pc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_026'] = {'inputs': ['pc_replacement_d2_026'], 'func': pc_replacement_d3_026}


def pc_replacement_d3_027(pc_replacement_d2_027):
    feature = _clean(pc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_027'] = {'inputs': ['pc_replacement_d2_027'], 'func': pc_replacement_d3_027}


def pc_replacement_d3_028(pc_replacement_d2_028):
    feature = _clean(pc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_028'] = {'inputs': ['pc_replacement_d2_028'], 'func': pc_replacement_d3_028}


def pc_replacement_d3_029(pc_replacement_d2_029):
    feature = _clean(pc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_029'] = {'inputs': ['pc_replacement_d2_029'], 'func': pc_replacement_d3_029}


def pc_replacement_d3_030(pc_replacement_d2_030):
    feature = _clean(pc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_030'] = {'inputs': ['pc_replacement_d2_030'], 'func': pc_replacement_d3_030}


def pc_replacement_d3_031(pc_replacement_d2_031):
    feature = _clean(pc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_031'] = {'inputs': ['pc_replacement_d2_031'], 'func': pc_replacement_d3_031}


def pc_replacement_d3_032(pc_replacement_d2_032):
    feature = _clean(pc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_032'] = {'inputs': ['pc_replacement_d2_032'], 'func': pc_replacement_d3_032}


def pc_replacement_d3_033(pc_replacement_d2_033):
    feature = _clean(pc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_033'] = {'inputs': ['pc_replacement_d2_033'], 'func': pc_replacement_d3_033}


def pc_replacement_d3_034(pc_replacement_d2_034):
    feature = _clean(pc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_034'] = {'inputs': ['pc_replacement_d2_034'], 'func': pc_replacement_d3_034}


def pc_replacement_d3_035(pc_replacement_d2_035):
    feature = _clean(pc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_035'] = {'inputs': ['pc_replacement_d2_035'], 'func': pc_replacement_d3_035}


def pc_replacement_d3_036(pc_replacement_d2_036):
    feature = _clean(pc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_036'] = {'inputs': ['pc_replacement_d2_036'], 'func': pc_replacement_d3_036}


def pc_replacement_d3_037(pc_replacement_d2_037):
    feature = _clean(pc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_037'] = {'inputs': ['pc_replacement_d2_037'], 'func': pc_replacement_d3_037}


def pc_replacement_d3_038(pc_replacement_d2_038):
    feature = _clean(pc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_038'] = {'inputs': ['pc_replacement_d2_038'], 'func': pc_replacement_d3_038}


def pc_replacement_d3_039(pc_replacement_d2_039):
    feature = _clean(pc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_039'] = {'inputs': ['pc_replacement_d2_039'], 'func': pc_replacement_d3_039}


def pc_replacement_d3_040(pc_replacement_d2_040):
    feature = _clean(pc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_040'] = {'inputs': ['pc_replacement_d2_040'], 'func': pc_replacement_d3_040}


def pc_replacement_d3_041(pc_replacement_d2_041):
    feature = _clean(pc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_041'] = {'inputs': ['pc_replacement_d2_041'], 'func': pc_replacement_d3_041}


def pc_replacement_d3_042(pc_replacement_d2_042):
    feature = _clean(pc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_042'] = {'inputs': ['pc_replacement_d2_042'], 'func': pc_replacement_d3_042}


def pc_replacement_d3_043(pc_replacement_d2_043):
    feature = _clean(pc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_043'] = {'inputs': ['pc_replacement_d2_043'], 'func': pc_replacement_d3_043}


def pc_replacement_d3_044(pc_replacement_d2_044):
    feature = _clean(pc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_044'] = {'inputs': ['pc_replacement_d2_044'], 'func': pc_replacement_d3_044}


def pc_replacement_d3_045(pc_replacement_d2_045):
    feature = _clean(pc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_045'] = {'inputs': ['pc_replacement_d2_045'], 'func': pc_replacement_d3_045}


def pc_replacement_d3_046(pc_replacement_d2_046):
    feature = _clean(pc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_046'] = {'inputs': ['pc_replacement_d2_046'], 'func': pc_replacement_d3_046}


def pc_replacement_d3_047(pc_replacement_d2_047):
    feature = _clean(pc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_047'] = {'inputs': ['pc_replacement_d2_047'], 'func': pc_replacement_d3_047}


def pc_replacement_d3_048(pc_replacement_d2_048):
    feature = _clean(pc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_048'] = {'inputs': ['pc_replacement_d2_048'], 'func': pc_replacement_d3_048}


def pc_replacement_d3_049(pc_replacement_d2_049):
    feature = _clean(pc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_049'] = {'inputs': ['pc_replacement_d2_049'], 'func': pc_replacement_d3_049}


def pc_replacement_d3_050(pc_replacement_d2_050):
    feature = _clean(pc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_050'] = {'inputs': ['pc_replacement_d2_050'], 'func': pc_replacement_d3_050}


def pc_replacement_d3_051(pc_replacement_d2_051):
    feature = _clean(pc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_051'] = {'inputs': ['pc_replacement_d2_051'], 'func': pc_replacement_d3_051}


def pc_replacement_d3_052(pc_replacement_d2_052):
    feature = _clean(pc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_052'] = {'inputs': ['pc_replacement_d2_052'], 'func': pc_replacement_d3_052}


def pc_replacement_d3_053(pc_replacement_d2_053):
    feature = _clean(pc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_053'] = {'inputs': ['pc_replacement_d2_053'], 'func': pc_replacement_d3_053}


def pc_replacement_d3_054(pc_replacement_d2_054):
    feature = _clean(pc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_054'] = {'inputs': ['pc_replacement_d2_054'], 'func': pc_replacement_d3_054}


def pc_replacement_d3_055(pc_replacement_d2_055):
    feature = _clean(pc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_055'] = {'inputs': ['pc_replacement_d2_055'], 'func': pc_replacement_d3_055}


def pc_replacement_d3_056(pc_replacement_d2_056):
    feature = _clean(pc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_056'] = {'inputs': ['pc_replacement_d2_056'], 'func': pc_replacement_d3_056}


def pc_replacement_d3_057(pc_replacement_d2_057):
    feature = _clean(pc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_057'] = {'inputs': ['pc_replacement_d2_057'], 'func': pc_replacement_d3_057}


def pc_replacement_d3_058(pc_replacement_d2_058):
    feature = _clean(pc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_058'] = {'inputs': ['pc_replacement_d2_058'], 'func': pc_replacement_d3_058}


def pc_replacement_d3_059(pc_replacement_d2_059):
    feature = _clean(pc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_059'] = {'inputs': ['pc_replacement_d2_059'], 'func': pc_replacement_d3_059}


def pc_replacement_d3_060(pc_replacement_d2_060):
    feature = _clean(pc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_060'] = {'inputs': ['pc_replacement_d2_060'], 'func': pc_replacement_d3_060}


def pc_replacement_d3_061(pc_replacement_d2_061):
    feature = _clean(pc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_061'] = {'inputs': ['pc_replacement_d2_061'], 'func': pc_replacement_d3_061}


def pc_replacement_d3_062(pc_replacement_d2_062):
    feature = _clean(pc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_062'] = {'inputs': ['pc_replacement_d2_062'], 'func': pc_replacement_d3_062}


def pc_replacement_d3_063(pc_replacement_d2_063):
    feature = _clean(pc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_063'] = {'inputs': ['pc_replacement_d2_063'], 'func': pc_replacement_d3_063}


def pc_replacement_d3_064(pc_replacement_d2_064):
    feature = _clean(pc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_064'] = {'inputs': ['pc_replacement_d2_064'], 'func': pc_replacement_d3_064}


def pc_replacement_d3_065(pc_replacement_d2_065):
    feature = _clean(pc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_065'] = {'inputs': ['pc_replacement_d2_065'], 'func': pc_replacement_d3_065}


def pc_replacement_d3_066(pc_replacement_d2_066):
    feature = _clean(pc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_066'] = {'inputs': ['pc_replacement_d2_066'], 'func': pc_replacement_d3_066}


def pc_replacement_d3_067(pc_replacement_d2_067):
    feature = _clean(pc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_067'] = {'inputs': ['pc_replacement_d2_067'], 'func': pc_replacement_d3_067}


def pc_replacement_d3_068(pc_replacement_d2_068):
    feature = _clean(pc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_068'] = {'inputs': ['pc_replacement_d2_068'], 'func': pc_replacement_d3_068}


def pc_replacement_d3_069(pc_replacement_d2_069):
    feature = _clean(pc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_069'] = {'inputs': ['pc_replacement_d2_069'], 'func': pc_replacement_d3_069}


def pc_replacement_d3_070(pc_replacement_d2_070):
    feature = _clean(pc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_070'] = {'inputs': ['pc_replacement_d2_070'], 'func': pc_replacement_d3_070}


def pc_replacement_d3_071(pc_replacement_d2_071):
    feature = _clean(pc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_071'] = {'inputs': ['pc_replacement_d2_071'], 'func': pc_replacement_d3_071}


def pc_replacement_d3_072(pc_replacement_d2_072):
    feature = _clean(pc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_072'] = {'inputs': ['pc_replacement_d2_072'], 'func': pc_replacement_d3_072}


def pc_replacement_d3_073(pc_replacement_d2_073):
    feature = _clean(pc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_073'] = {'inputs': ['pc_replacement_d2_073'], 'func': pc_replacement_d3_073}


def pc_replacement_d3_074(pc_replacement_d2_074):
    feature = _clean(pc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_074'] = {'inputs': ['pc_replacement_d2_074'], 'func': pc_replacement_d3_074}


def pc_replacement_d3_075(pc_replacement_d2_075):
    feature = _clean(pc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_075'] = {'inputs': ['pc_replacement_d2_075'], 'func': pc_replacement_d3_075}


def pc_replacement_d3_076(pc_replacement_d2_076):
    feature = _clean(pc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_076'] = {'inputs': ['pc_replacement_d2_076'], 'func': pc_replacement_d3_076}


def pc_replacement_d3_077(pc_replacement_d2_077):
    feature = _clean(pc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_077'] = {'inputs': ['pc_replacement_d2_077'], 'func': pc_replacement_d3_077}


def pc_replacement_d3_078(pc_replacement_d2_078):
    feature = _clean(pc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_078'] = {'inputs': ['pc_replacement_d2_078'], 'func': pc_replacement_d3_078}


def pc_replacement_d3_079(pc_replacement_d2_079):
    feature = _clean(pc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_079'] = {'inputs': ['pc_replacement_d2_079'], 'func': pc_replacement_d3_079}


def pc_replacement_d3_080(pc_replacement_d2_080):
    feature = _clean(pc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_080'] = {'inputs': ['pc_replacement_d2_080'], 'func': pc_replacement_d3_080}


def pc_replacement_d3_081(pc_replacement_d2_081):
    feature = _clean(pc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_081'] = {'inputs': ['pc_replacement_d2_081'], 'func': pc_replacement_d3_081}


def pc_replacement_d3_082(pc_replacement_d2_082):
    feature = _clean(pc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_082'] = {'inputs': ['pc_replacement_d2_082'], 'func': pc_replacement_d3_082}


def pc_replacement_d3_083(pc_replacement_d2_083):
    feature = _clean(pc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_083'] = {'inputs': ['pc_replacement_d2_083'], 'func': pc_replacement_d3_083}


def pc_replacement_d3_084(pc_replacement_d2_084):
    feature = _clean(pc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_084'] = {'inputs': ['pc_replacement_d2_084'], 'func': pc_replacement_d3_084}


def pc_replacement_d3_085(pc_replacement_d2_085):
    feature = _clean(pc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_085'] = {'inputs': ['pc_replacement_d2_085'], 'func': pc_replacement_d3_085}


def pc_replacement_d3_086(pc_replacement_d2_086):
    feature = _clean(pc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_086'] = {'inputs': ['pc_replacement_d2_086'], 'func': pc_replacement_d3_086}


def pc_replacement_d3_087(pc_replacement_d2_087):
    feature = _clean(pc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_087'] = {'inputs': ['pc_replacement_d2_087'], 'func': pc_replacement_d3_087}


def pc_replacement_d3_088(pc_replacement_d2_088):
    feature = _clean(pc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_088'] = {'inputs': ['pc_replacement_d2_088'], 'func': pc_replacement_d3_088}


def pc_replacement_d3_089(pc_replacement_d2_089):
    feature = _clean(pc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_089'] = {'inputs': ['pc_replacement_d2_089'], 'func': pc_replacement_d3_089}


def pc_replacement_d3_090(pc_replacement_d2_090):
    feature = _clean(pc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_090'] = {'inputs': ['pc_replacement_d2_090'], 'func': pc_replacement_d3_090}


def pc_replacement_d3_091(pc_replacement_d2_091):
    feature = _clean(pc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_091'] = {'inputs': ['pc_replacement_d2_091'], 'func': pc_replacement_d3_091}


def pc_replacement_d3_092(pc_replacement_d2_092):
    feature = _clean(pc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_092'] = {'inputs': ['pc_replacement_d2_092'], 'func': pc_replacement_d3_092}


def pc_replacement_d3_093(pc_replacement_d2_093):
    feature = _clean(pc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_093'] = {'inputs': ['pc_replacement_d2_093'], 'func': pc_replacement_d3_093}


def pc_replacement_d3_094(pc_replacement_d2_094):
    feature = _clean(pc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_094'] = {'inputs': ['pc_replacement_d2_094'], 'func': pc_replacement_d3_094}


def pc_replacement_d3_095(pc_replacement_d2_095):
    feature = _clean(pc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_095'] = {'inputs': ['pc_replacement_d2_095'], 'func': pc_replacement_d3_095}


def pc_replacement_d3_096(pc_replacement_d2_096):
    feature = _clean(pc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_096'] = {'inputs': ['pc_replacement_d2_096'], 'func': pc_replacement_d3_096}


def pc_replacement_d3_097(pc_replacement_d2_097):
    feature = _clean(pc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_097'] = {'inputs': ['pc_replacement_d2_097'], 'func': pc_replacement_d3_097}


def pc_replacement_d3_098(pc_replacement_d2_098):
    feature = _clean(pc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_098'] = {'inputs': ['pc_replacement_d2_098'], 'func': pc_replacement_d3_098}


def pc_replacement_d3_099(pc_replacement_d2_099):
    feature = _clean(pc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_099'] = {'inputs': ['pc_replacement_d2_099'], 'func': pc_replacement_d3_099}


def pc_replacement_d3_100(pc_replacement_d2_100):
    feature = _clean(pc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_100'] = {'inputs': ['pc_replacement_d2_100'], 'func': pc_replacement_d3_100}


def pc_replacement_d3_101(pc_replacement_d2_101):
    feature = _clean(pc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_101'] = {'inputs': ['pc_replacement_d2_101'], 'func': pc_replacement_d3_101}


def pc_replacement_d3_102(pc_replacement_d2_102):
    feature = _clean(pc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_102'] = {'inputs': ['pc_replacement_d2_102'], 'func': pc_replacement_d3_102}


def pc_replacement_d3_103(pc_replacement_d2_103):
    feature = _clean(pc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_103'] = {'inputs': ['pc_replacement_d2_103'], 'func': pc_replacement_d3_103}


def pc_replacement_d3_104(pc_replacement_d2_104):
    feature = _clean(pc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_104'] = {'inputs': ['pc_replacement_d2_104'], 'func': pc_replacement_d3_104}


def pc_replacement_d3_105(pc_replacement_d2_105):
    feature = _clean(pc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_105'] = {'inputs': ['pc_replacement_d2_105'], 'func': pc_replacement_d3_105}


def pc_replacement_d3_106(pc_replacement_d2_106):
    feature = _clean(pc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_106'] = {'inputs': ['pc_replacement_d2_106'], 'func': pc_replacement_d3_106}


def pc_replacement_d3_107(pc_replacement_d2_107):
    feature = _clean(pc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_107'] = {'inputs': ['pc_replacement_d2_107'], 'func': pc_replacement_d3_107}


def pc_replacement_d3_108(pc_replacement_d2_108):
    feature = _clean(pc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_108'] = {'inputs': ['pc_replacement_d2_108'], 'func': pc_replacement_d3_108}


def pc_replacement_d3_109(pc_replacement_d2_109):
    feature = _clean(pc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_109'] = {'inputs': ['pc_replacement_d2_109'], 'func': pc_replacement_d3_109}


def pc_replacement_d3_110(pc_replacement_d2_110):
    feature = _clean(pc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_110'] = {'inputs': ['pc_replacement_d2_110'], 'func': pc_replacement_d3_110}


def pc_replacement_d3_111(pc_replacement_d2_111):
    feature = _clean(pc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_111'] = {'inputs': ['pc_replacement_d2_111'], 'func': pc_replacement_d3_111}


def pc_replacement_d3_112(pc_replacement_d2_112):
    feature = _clean(pc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_112'] = {'inputs': ['pc_replacement_d2_112'], 'func': pc_replacement_d3_112}


def pc_replacement_d3_113(pc_replacement_d2_113):
    feature = _clean(pc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_113'] = {'inputs': ['pc_replacement_d2_113'], 'func': pc_replacement_d3_113}


def pc_replacement_d3_114(pc_replacement_d2_114):
    feature = _clean(pc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_114'] = {'inputs': ['pc_replacement_d2_114'], 'func': pc_replacement_d3_114}


def pc_replacement_d3_115(pc_replacement_d2_115):
    feature = _clean(pc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_115'] = {'inputs': ['pc_replacement_d2_115'], 'func': pc_replacement_d3_115}


def pc_replacement_d3_116(pc_replacement_d2_116):
    feature = _clean(pc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_116'] = {'inputs': ['pc_replacement_d2_116'], 'func': pc_replacement_d3_116}


def pc_replacement_d3_117(pc_replacement_d2_117):
    feature = _clean(pc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_117'] = {'inputs': ['pc_replacement_d2_117'], 'func': pc_replacement_d3_117}


def pc_replacement_d3_118(pc_replacement_d2_118):
    feature = _clean(pc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_118'] = {'inputs': ['pc_replacement_d2_118'], 'func': pc_replacement_d3_118}


def pc_replacement_d3_119(pc_replacement_d2_119):
    feature = _clean(pc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_119'] = {'inputs': ['pc_replacement_d2_119'], 'func': pc_replacement_d3_119}


def pc_replacement_d3_120(pc_replacement_d2_120):
    feature = _clean(pc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_120'] = {'inputs': ['pc_replacement_d2_120'], 'func': pc_replacement_d3_120}


def pc_replacement_d3_121(pc_replacement_d2_121):
    feature = _clean(pc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_121'] = {'inputs': ['pc_replacement_d2_121'], 'func': pc_replacement_d3_121}


def pc_replacement_d3_122(pc_replacement_d2_122):
    feature = _clean(pc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_122'] = {'inputs': ['pc_replacement_d2_122'], 'func': pc_replacement_d3_122}


def pc_replacement_d3_123(pc_replacement_d2_123):
    feature = _clean(pc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_123'] = {'inputs': ['pc_replacement_d2_123'], 'func': pc_replacement_d3_123}


def pc_replacement_d3_124(pc_replacement_d2_124):
    feature = _clean(pc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_124'] = {'inputs': ['pc_replacement_d2_124'], 'func': pc_replacement_d3_124}


def pc_replacement_d3_125(pc_replacement_d2_125):
    feature = _clean(pc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_125'] = {'inputs': ['pc_replacement_d2_125'], 'func': pc_replacement_d3_125}


def pc_replacement_d3_126(pc_replacement_d2_126):
    feature = _clean(pc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_126'] = {'inputs': ['pc_replacement_d2_126'], 'func': pc_replacement_d3_126}


def pc_replacement_d3_127(pc_replacement_d2_127):
    feature = _clean(pc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_127'] = {'inputs': ['pc_replacement_d2_127'], 'func': pc_replacement_d3_127}


def pc_replacement_d3_128(pc_replacement_d2_128):
    feature = _clean(pc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_128'] = {'inputs': ['pc_replacement_d2_128'], 'func': pc_replacement_d3_128}


def pc_replacement_d3_129(pc_replacement_d2_129):
    feature = _clean(pc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_129'] = {'inputs': ['pc_replacement_d2_129'], 'func': pc_replacement_d3_129}


def pc_replacement_d3_130(pc_replacement_d2_130):
    feature = _clean(pc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_130'] = {'inputs': ['pc_replacement_d2_130'], 'func': pc_replacement_d3_130}


def pc_replacement_d3_131(pc_replacement_d2_131):
    feature = _clean(pc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_131'] = {'inputs': ['pc_replacement_d2_131'], 'func': pc_replacement_d3_131}


def pc_replacement_d3_132(pc_replacement_d2_132):
    feature = _clean(pc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_132'] = {'inputs': ['pc_replacement_d2_132'], 'func': pc_replacement_d3_132}


def pc_replacement_d3_133(pc_replacement_d2_133):
    feature = _clean(pc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_133'] = {'inputs': ['pc_replacement_d2_133'], 'func': pc_replacement_d3_133}


def pc_replacement_d3_134(pc_replacement_d2_134):
    feature = _clean(pc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_134'] = {'inputs': ['pc_replacement_d2_134'], 'func': pc_replacement_d3_134}


def pc_replacement_d3_135(pc_replacement_d2_135):
    feature = _clean(pc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_135'] = {'inputs': ['pc_replacement_d2_135'], 'func': pc_replacement_d3_135}


def pc_replacement_d3_136(pc_replacement_d2_136):
    feature = _clean(pc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_136'] = {'inputs': ['pc_replacement_d2_136'], 'func': pc_replacement_d3_136}


def pc_replacement_d3_137(pc_replacement_d2_137):
    feature = _clean(pc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_137'] = {'inputs': ['pc_replacement_d2_137'], 'func': pc_replacement_d3_137}


def pc_replacement_d3_138(pc_replacement_d2_138):
    feature = _clean(pc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_138'] = {'inputs': ['pc_replacement_d2_138'], 'func': pc_replacement_d3_138}


def pc_replacement_d3_139(pc_replacement_d2_139):
    feature = _clean(pc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_139'] = {'inputs': ['pc_replacement_d2_139'], 'func': pc_replacement_d3_139}


def pc_replacement_d3_140(pc_replacement_d2_140):
    feature = _clean(pc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_140'] = {'inputs': ['pc_replacement_d2_140'], 'func': pc_replacement_d3_140}


def pc_replacement_d3_141(pc_replacement_d2_141):
    feature = _clean(pc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_141'] = {'inputs': ['pc_replacement_d2_141'], 'func': pc_replacement_d3_141}


def pc_replacement_d3_142(pc_replacement_d2_142):
    feature = _clean(pc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_142'] = {'inputs': ['pc_replacement_d2_142'], 'func': pc_replacement_d3_142}


def pc_replacement_d3_143(pc_replacement_d2_143):
    feature = _clean(pc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_143'] = {'inputs': ['pc_replacement_d2_143'], 'func': pc_replacement_d3_143}


def pc_replacement_d3_144(pc_replacement_d2_144):
    feature = _clean(pc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_144'] = {'inputs': ['pc_replacement_d2_144'], 'func': pc_replacement_d3_144}


def pc_replacement_d3_145(pc_replacement_d2_145):
    feature = _clean(pc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_145'] = {'inputs': ['pc_replacement_d2_145'], 'func': pc_replacement_d3_145}


def pc_replacement_d3_146(pc_replacement_d2_146):
    feature = _clean(pc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_146'] = {'inputs': ['pc_replacement_d2_146'], 'func': pc_replacement_d3_146}


def pc_replacement_d3_147(pc_replacement_d2_147):
    feature = _clean(pc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_147'] = {'inputs': ['pc_replacement_d2_147'], 'func': pc_replacement_d3_147}


def pc_replacement_d3_148(pc_replacement_d2_148):
    feature = _clean(pc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_148'] = {'inputs': ['pc_replacement_d2_148'], 'func': pc_replacement_d3_148}


def pc_replacement_d3_149(pc_replacement_d2_149):
    feature = _clean(pc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_149'] = {'inputs': ['pc_replacement_d2_149'], 'func': pc_replacement_d3_149}


def pc_replacement_d3_150(pc_replacement_d2_150):
    feature = _clean(pc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_150'] = {'inputs': ['pc_replacement_d2_150'], 'func': pc_replacement_d3_150}


def pc_replacement_d3_151(pc_replacement_d2_151):
    feature = _clean(pc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_151'] = {'inputs': ['pc_replacement_d2_151'], 'func': pc_replacement_d3_151}


def pc_replacement_d3_152(pc_replacement_d2_152):
    feature = _clean(pc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_152'] = {'inputs': ['pc_replacement_d2_152'], 'func': pc_replacement_d3_152}


def pc_replacement_d3_153(pc_replacement_d2_153):
    feature = _clean(pc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_153'] = {'inputs': ['pc_replacement_d2_153'], 'func': pc_replacement_d3_153}


def pc_replacement_d3_154(pc_replacement_d2_154):
    feature = _clean(pc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_154'] = {'inputs': ['pc_replacement_d2_154'], 'func': pc_replacement_d3_154}


def pc_replacement_d3_155(pc_replacement_d2_155):
    feature = _clean(pc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_155'] = {'inputs': ['pc_replacement_d2_155'], 'func': pc_replacement_d3_155}


def pc_replacement_d3_156(pc_replacement_d2_156):
    feature = _clean(pc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_156'] = {'inputs': ['pc_replacement_d2_156'], 'func': pc_replacement_d3_156}


def pc_replacement_d3_157(pc_replacement_d2_157):
    feature = _clean(pc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_157'] = {'inputs': ['pc_replacement_d2_157'], 'func': pc_replacement_d3_157}


def pc_replacement_d3_158(pc_replacement_d2_158):
    feature = _clean(pc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_158'] = {'inputs': ['pc_replacement_d2_158'], 'func': pc_replacement_d3_158}


def pc_replacement_d3_159(pc_replacement_d2_159):
    feature = _clean(pc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_159'] = {'inputs': ['pc_replacement_d2_159'], 'func': pc_replacement_d3_159}


def pc_replacement_d3_160(pc_replacement_d2_160):
    feature = _clean(pc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_160'] = {'inputs': ['pc_replacement_d2_160'], 'func': pc_replacement_d3_160}


def pc_replacement_d3_161(pc_replacement_d2_161):
    feature = _clean(pc_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_161'] = {'inputs': ['pc_replacement_d2_161'], 'func': pc_replacement_d3_161}


def pc_replacement_d3_162(pc_replacement_d2_162):
    feature = _clean(pc_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_162'] = {'inputs': ['pc_replacement_d2_162'], 'func': pc_replacement_d3_162}


def pc_replacement_d3_163(pc_replacement_d2_163):
    feature = _clean(pc_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_163'] = {'inputs': ['pc_replacement_d2_163'], 'func': pc_replacement_d3_163}


def pc_replacement_d3_164(pc_replacement_d2_164):
    feature = _clean(pc_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_164'] = {'inputs': ['pc_replacement_d2_164'], 'func': pc_replacement_d3_164}


def pc_replacement_d3_165(pc_replacement_d2_165):
    feature = _clean(pc_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_165'] = {'inputs': ['pc_replacement_d2_165'], 'func': pc_replacement_d3_165}


def pc_replacement_d3_166(pc_replacement_d2_166):
    feature = _clean(pc_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_166'] = {'inputs': ['pc_replacement_d2_166'], 'func': pc_replacement_d3_166}


def pc_replacement_d3_167(pc_replacement_d2_167):
    feature = _clean(pc_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_167'] = {'inputs': ['pc_replacement_d2_167'], 'func': pc_replacement_d3_167}


def pc_replacement_d3_168(pc_replacement_d2_168):
    feature = _clean(pc_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_168'] = {'inputs': ['pc_replacement_d2_168'], 'func': pc_replacement_d3_168}


def pc_replacement_d3_169(pc_replacement_d2_169):
    feature = _clean(pc_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_169'] = {'inputs': ['pc_replacement_d2_169'], 'func': pc_replacement_d3_169}


def pc_replacement_d3_170(pc_replacement_d2_170):
    feature = _clean(pc_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
PC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['pc_replacement_d3_170'] = {'inputs': ['pc_replacement_d2_170'], 'func': pc_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def pcmp_base_universe_d3_001_pcmp_002_zero_volume_frequency_10_002(pcmp_base_universe_d2_001_pcmp_002_zero_volume_frequency_10_002):
    return _base_universe_d3(pcmp_base_universe_d2_001_pcmp_002_zero_volume_frequency_10_002, 1)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_001_pcmp_002_zero_volume_frequency_10_002'] = {'inputs': ['pcmp_base_universe_d2_001_pcmp_002_zero_volume_frequency_10_002'], 'func': pcmp_base_universe_d3_001_pcmp_002_zero_volume_frequency_10_002}


def pcmp_base_universe_d3_002_pcmp_003_spread_proxy_21_003(pcmp_base_universe_d2_002_pcmp_003_spread_proxy_21_003):
    return _base_universe_d3(pcmp_base_universe_d2_002_pcmp_003_spread_proxy_21_003, 2)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_002_pcmp_003_spread_proxy_21_003'] = {'inputs': ['pcmp_base_universe_d2_002_pcmp_003_spread_proxy_21_003'], 'func': pcmp_base_universe_d3_002_pcmp_003_spread_proxy_21_003}


def pcmp_base_universe_d3_003_pcmp_004_trading_intensity_42_004(pcmp_base_universe_d2_003_pcmp_004_trading_intensity_42_004):
    return _base_universe_d3(pcmp_base_universe_d2_003_pcmp_004_trading_intensity_42_004, 3)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_003_pcmp_004_trading_intensity_42_004'] = {'inputs': ['pcmp_base_universe_d2_003_pcmp_004_trading_intensity_42_004'], 'func': pcmp_base_universe_d3_003_pcmp_004_trading_intensity_42_004}


def pcmp_base_universe_d3_004_pcmp_006_price_level_distress_84_006(pcmp_base_universe_d2_004_pcmp_006_price_level_distress_84_006):
    return _base_universe_d3(pcmp_base_universe_d2_004_pcmp_006_price_level_distress_84_006, 4)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_004_pcmp_006_price_level_distress_84_006'] = {'inputs': ['pcmp_base_universe_d2_004_pcmp_006_price_level_distress_84_006'], 'func': pcmp_base_universe_d3_004_pcmp_006_price_level_distress_84_006}


def pcmp_base_universe_d3_005_pcmp_008_zero_volume_frequency_189_008(pcmp_base_universe_d2_005_pcmp_008_zero_volume_frequency_189_008):
    return _base_universe_d3(pcmp_base_universe_d2_005_pcmp_008_zero_volume_frequency_189_008, 5)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_005_pcmp_008_zero_volume_frequency_189_008'] = {'inputs': ['pcmp_base_universe_d2_005_pcmp_008_zero_volume_frequency_189_008'], 'func': pcmp_base_universe_d3_005_pcmp_008_zero_volume_frequency_189_008}


def pcmp_base_universe_d3_006_pcmp_009_spread_proxy_252_009(pcmp_base_universe_d2_006_pcmp_009_spread_proxy_252_009):
    return _base_universe_d3(pcmp_base_universe_d2_006_pcmp_009_spread_proxy_252_009, 6)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_006_pcmp_009_spread_proxy_252_009'] = {'inputs': ['pcmp_base_universe_d2_006_pcmp_009_spread_proxy_252_009'], 'func': pcmp_base_universe_d3_006_pcmp_009_spread_proxy_252_009}


def pcmp_base_universe_d3_007_pcmp_010_trading_intensity_378_010(pcmp_base_universe_d2_007_pcmp_010_trading_intensity_378_010):
    return _base_universe_d3(pcmp_base_universe_d2_007_pcmp_010_trading_intensity_378_010, 7)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_007_pcmp_010_trading_intensity_378_010'] = {'inputs': ['pcmp_base_universe_d2_007_pcmp_010_trading_intensity_378_010'], 'func': pcmp_base_universe_d3_007_pcmp_010_trading_intensity_378_010}


def pcmp_base_universe_d3_008_pcmp_012_price_level_distress_756_012(pcmp_base_universe_d2_008_pcmp_012_price_level_distress_756_012):
    return _base_universe_d3(pcmp_base_universe_d2_008_pcmp_012_price_level_distress_756_012, 8)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_008_pcmp_012_price_level_distress_756_012'] = {'inputs': ['pcmp_base_universe_d2_008_pcmp_012_price_level_distress_756_012'], 'func': pcmp_base_universe_d3_008_pcmp_012_price_level_distress_756_012}


def pcmp_base_universe_d3_009_pcmp_014_zero_volume_frequency_1260_014(pcmp_base_universe_d2_009_pcmp_014_zero_volume_frequency_1260_014):
    return _base_universe_d3(pcmp_base_universe_d2_009_pcmp_014_zero_volume_frequency_1260_014, 9)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_009_pcmp_014_zero_volume_frequency_1260_014'] = {'inputs': ['pcmp_base_universe_d2_009_pcmp_014_zero_volume_frequency_1260_014'], 'func': pcmp_base_universe_d3_009_pcmp_014_zero_volume_frequency_1260_014}


def pcmp_base_universe_d3_010_pcmp_015_spread_proxy_1512_015(pcmp_base_universe_d2_010_pcmp_015_spread_proxy_1512_015):
    return _base_universe_d3(pcmp_base_universe_d2_010_pcmp_015_spread_proxy_1512_015, 10)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_010_pcmp_015_spread_proxy_1512_015'] = {'inputs': ['pcmp_base_universe_d2_010_pcmp_015_spread_proxy_1512_015'], 'func': pcmp_base_universe_d3_010_pcmp_015_spread_proxy_1512_015}


def pcmp_base_universe_d3_011_pcmp_016_trading_intensity_5_016(pcmp_base_universe_d2_011_pcmp_016_trading_intensity_5_016):
    return _base_universe_d3(pcmp_base_universe_d2_011_pcmp_016_trading_intensity_5_016, 11)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_011_pcmp_016_trading_intensity_5_016'] = {'inputs': ['pcmp_base_universe_d2_011_pcmp_016_trading_intensity_5_016'], 'func': pcmp_base_universe_d3_011_pcmp_016_trading_intensity_5_016}


def pcmp_base_universe_d3_012_pcmp_018_price_level_distress_21_018(pcmp_base_universe_d2_012_pcmp_018_price_level_distress_21_018):
    return _base_universe_d3(pcmp_base_universe_d2_012_pcmp_018_price_level_distress_21_018, 12)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_012_pcmp_018_price_level_distress_21_018'] = {'inputs': ['pcmp_base_universe_d2_012_pcmp_018_price_level_distress_21_018'], 'func': pcmp_base_universe_d3_012_pcmp_018_price_level_distress_21_018}


def pcmp_base_universe_d3_013_pcmp_020_zero_volume_frequency_63_020(pcmp_base_universe_d2_013_pcmp_020_zero_volume_frequency_63_020):
    return _base_universe_d3(pcmp_base_universe_d2_013_pcmp_020_zero_volume_frequency_63_020, 13)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_013_pcmp_020_zero_volume_frequency_63_020'] = {'inputs': ['pcmp_base_universe_d2_013_pcmp_020_zero_volume_frequency_63_020'], 'func': pcmp_base_universe_d3_013_pcmp_020_zero_volume_frequency_63_020}


def pcmp_base_universe_d3_014_pcmp_021_spread_proxy_84_021(pcmp_base_universe_d2_014_pcmp_021_spread_proxy_84_021):
    return _base_universe_d3(pcmp_base_universe_d2_014_pcmp_021_spread_proxy_84_021, 14)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_014_pcmp_021_spread_proxy_84_021'] = {'inputs': ['pcmp_base_universe_d2_014_pcmp_021_spread_proxy_84_021'], 'func': pcmp_base_universe_d3_014_pcmp_021_spread_proxy_84_021}


def pcmp_base_universe_d3_015_pcmp_022_trading_intensity_126_022(pcmp_base_universe_d2_015_pcmp_022_trading_intensity_126_022):
    return _base_universe_d3(pcmp_base_universe_d2_015_pcmp_022_trading_intensity_126_022, 15)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_015_pcmp_022_trading_intensity_126_022'] = {'inputs': ['pcmp_base_universe_d2_015_pcmp_022_trading_intensity_126_022'], 'func': pcmp_base_universe_d3_015_pcmp_022_trading_intensity_126_022}


def pcmp_base_universe_d3_016_pcmp_024_price_level_distress_252_024(pcmp_base_universe_d2_016_pcmp_024_price_level_distress_252_024):
    return _base_universe_d3(pcmp_base_universe_d2_016_pcmp_024_price_level_distress_252_024, 16)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_016_pcmp_024_price_level_distress_252_024'] = {'inputs': ['pcmp_base_universe_d2_016_pcmp_024_price_level_distress_252_024'], 'func': pcmp_base_universe_d3_016_pcmp_024_price_level_distress_252_024}


def pcmp_base_universe_d3_017_pcmp_026_zero_volume_frequency_504_026(pcmp_base_universe_d2_017_pcmp_026_zero_volume_frequency_504_026):
    return _base_universe_d3(pcmp_base_universe_d2_017_pcmp_026_zero_volume_frequency_504_026, 17)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_017_pcmp_026_zero_volume_frequency_504_026'] = {'inputs': ['pcmp_base_universe_d2_017_pcmp_026_zero_volume_frequency_504_026'], 'func': pcmp_base_universe_d3_017_pcmp_026_zero_volume_frequency_504_026}


def pcmp_base_universe_d3_018_pcmp_027_spread_proxy_756_027(pcmp_base_universe_d2_018_pcmp_027_spread_proxy_756_027):
    return _base_universe_d3(pcmp_base_universe_d2_018_pcmp_027_spread_proxy_756_027, 18)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_018_pcmp_027_spread_proxy_756_027'] = {'inputs': ['pcmp_base_universe_d2_018_pcmp_027_spread_proxy_756_027'], 'func': pcmp_base_universe_d3_018_pcmp_027_spread_proxy_756_027}


def pcmp_base_universe_d3_019_pcmp_028_trading_intensity_1008_028(pcmp_base_universe_d2_019_pcmp_028_trading_intensity_1008_028):
    return _base_universe_d3(pcmp_base_universe_d2_019_pcmp_028_trading_intensity_1008_028, 19)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_019_pcmp_028_trading_intensity_1008_028'] = {'inputs': ['pcmp_base_universe_d2_019_pcmp_028_trading_intensity_1008_028'], 'func': pcmp_base_universe_d3_019_pcmp_028_trading_intensity_1008_028}


def pcmp_base_universe_d3_020_pcmp_030_price_level_distress_1512_030(pcmp_base_universe_d2_020_pcmp_030_price_level_distress_1512_030):
    return _base_universe_d3(pcmp_base_universe_d2_020_pcmp_030_price_level_distress_1512_030, 20)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_020_pcmp_030_price_level_distress_1512_030'] = {'inputs': ['pcmp_base_universe_d2_020_pcmp_030_price_level_distress_1512_030'], 'func': pcmp_base_universe_d3_020_pcmp_030_price_level_distress_1512_030}


def pcmp_base_universe_d3_021_pcmp_basefill_001(pcmp_base_universe_d2_021_pcmp_basefill_001):
    return _base_universe_d3(pcmp_base_universe_d2_021_pcmp_basefill_001, 21)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_021_pcmp_basefill_001'] = {'inputs': ['pcmp_base_universe_d2_021_pcmp_basefill_001'], 'func': pcmp_base_universe_d3_021_pcmp_basefill_001}


def pcmp_base_universe_d3_022_pcmp_basefill_005(pcmp_base_universe_d2_022_pcmp_basefill_005):
    return _base_universe_d3(pcmp_base_universe_d2_022_pcmp_basefill_005, 22)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_022_pcmp_basefill_005'] = {'inputs': ['pcmp_base_universe_d2_022_pcmp_basefill_005'], 'func': pcmp_base_universe_d3_022_pcmp_basefill_005}


def pcmp_base_universe_d3_023_pcmp_basefill_007(pcmp_base_universe_d2_023_pcmp_basefill_007):
    return _base_universe_d3(pcmp_base_universe_d2_023_pcmp_basefill_007, 23)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_023_pcmp_basefill_007'] = {'inputs': ['pcmp_base_universe_d2_023_pcmp_basefill_007'], 'func': pcmp_base_universe_d3_023_pcmp_basefill_007}


def pcmp_base_universe_d3_024_pcmp_basefill_011(pcmp_base_universe_d2_024_pcmp_basefill_011):
    return _base_universe_d3(pcmp_base_universe_d2_024_pcmp_basefill_011, 24)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_024_pcmp_basefill_011'] = {'inputs': ['pcmp_base_universe_d2_024_pcmp_basefill_011'], 'func': pcmp_base_universe_d3_024_pcmp_basefill_011}


def pcmp_base_universe_d3_025_pcmp_basefill_013(pcmp_base_universe_d2_025_pcmp_basefill_013):
    return _base_universe_d3(pcmp_base_universe_d2_025_pcmp_basefill_013, 25)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_025_pcmp_basefill_013'] = {'inputs': ['pcmp_base_universe_d2_025_pcmp_basefill_013'], 'func': pcmp_base_universe_d3_025_pcmp_basefill_013}


def pcmp_base_universe_d3_026_pcmp_basefill_017(pcmp_base_universe_d2_026_pcmp_basefill_017):
    return _base_universe_d3(pcmp_base_universe_d2_026_pcmp_basefill_017, 26)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_026_pcmp_basefill_017'] = {'inputs': ['pcmp_base_universe_d2_026_pcmp_basefill_017'], 'func': pcmp_base_universe_d3_026_pcmp_basefill_017}


def pcmp_base_universe_d3_027_pcmp_basefill_019(pcmp_base_universe_d2_027_pcmp_basefill_019):
    return _base_universe_d3(pcmp_base_universe_d2_027_pcmp_basefill_019, 27)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_027_pcmp_basefill_019'] = {'inputs': ['pcmp_base_universe_d2_027_pcmp_basefill_019'], 'func': pcmp_base_universe_d3_027_pcmp_basefill_019}


def pcmp_base_universe_d3_028_pcmp_basefill_023(pcmp_base_universe_d2_028_pcmp_basefill_023):
    return _base_universe_d3(pcmp_base_universe_d2_028_pcmp_basefill_023, 28)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_028_pcmp_basefill_023'] = {'inputs': ['pcmp_base_universe_d2_028_pcmp_basefill_023'], 'func': pcmp_base_universe_d3_028_pcmp_basefill_023}


def pcmp_base_universe_d3_029_pcmp_basefill_025(pcmp_base_universe_d2_029_pcmp_basefill_025):
    return _base_universe_d3(pcmp_base_universe_d2_029_pcmp_basefill_025, 29)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_029_pcmp_basefill_025'] = {'inputs': ['pcmp_base_universe_d2_029_pcmp_basefill_025'], 'func': pcmp_base_universe_d3_029_pcmp_basefill_025}


def pcmp_base_universe_d3_030_pcmp_basefill_029(pcmp_base_universe_d2_030_pcmp_basefill_029):
    return _base_universe_d3(pcmp_base_universe_d2_030_pcmp_basefill_029, 30)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_030_pcmp_basefill_029'] = {'inputs': ['pcmp_base_universe_d2_030_pcmp_basefill_029'], 'func': pcmp_base_universe_d3_030_pcmp_basefill_029}


def pcmp_base_universe_d3_031_pcmp_basefill_031(pcmp_base_universe_d2_031_pcmp_basefill_031):
    return _base_universe_d3(pcmp_base_universe_d2_031_pcmp_basefill_031, 31)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_031_pcmp_basefill_031'] = {'inputs': ['pcmp_base_universe_d2_031_pcmp_basefill_031'], 'func': pcmp_base_universe_d3_031_pcmp_basefill_031}


def pcmp_base_universe_d3_032_pcmp_basefill_032(pcmp_base_universe_d2_032_pcmp_basefill_032):
    return _base_universe_d3(pcmp_base_universe_d2_032_pcmp_basefill_032, 32)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_032_pcmp_basefill_032'] = {'inputs': ['pcmp_base_universe_d2_032_pcmp_basefill_032'], 'func': pcmp_base_universe_d3_032_pcmp_basefill_032}


def pcmp_base_universe_d3_033_pcmp_basefill_033(pcmp_base_universe_d2_033_pcmp_basefill_033):
    return _base_universe_d3(pcmp_base_universe_d2_033_pcmp_basefill_033, 33)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_033_pcmp_basefill_033'] = {'inputs': ['pcmp_base_universe_d2_033_pcmp_basefill_033'], 'func': pcmp_base_universe_d3_033_pcmp_basefill_033}


def pcmp_base_universe_d3_034_pcmp_basefill_034(pcmp_base_universe_d2_034_pcmp_basefill_034):
    return _base_universe_d3(pcmp_base_universe_d2_034_pcmp_basefill_034, 34)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_034_pcmp_basefill_034'] = {'inputs': ['pcmp_base_universe_d2_034_pcmp_basefill_034'], 'func': pcmp_base_universe_d3_034_pcmp_basefill_034}


def pcmp_base_universe_d3_035_pcmp_basefill_035(pcmp_base_universe_d2_035_pcmp_basefill_035):
    return _base_universe_d3(pcmp_base_universe_d2_035_pcmp_basefill_035, 35)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_035_pcmp_basefill_035'] = {'inputs': ['pcmp_base_universe_d2_035_pcmp_basefill_035'], 'func': pcmp_base_universe_d3_035_pcmp_basefill_035}


def pcmp_base_universe_d3_036_pcmp_basefill_036(pcmp_base_universe_d2_036_pcmp_basefill_036):
    return _base_universe_d3(pcmp_base_universe_d2_036_pcmp_basefill_036, 36)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_036_pcmp_basefill_036'] = {'inputs': ['pcmp_base_universe_d2_036_pcmp_basefill_036'], 'func': pcmp_base_universe_d3_036_pcmp_basefill_036}


def pcmp_base_universe_d3_037_pcmp_basefill_037(pcmp_base_universe_d2_037_pcmp_basefill_037):
    return _base_universe_d3(pcmp_base_universe_d2_037_pcmp_basefill_037, 37)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_037_pcmp_basefill_037'] = {'inputs': ['pcmp_base_universe_d2_037_pcmp_basefill_037'], 'func': pcmp_base_universe_d3_037_pcmp_basefill_037}


def pcmp_base_universe_d3_038_pcmp_basefill_038(pcmp_base_universe_d2_038_pcmp_basefill_038):
    return _base_universe_d3(pcmp_base_universe_d2_038_pcmp_basefill_038, 38)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_038_pcmp_basefill_038'] = {'inputs': ['pcmp_base_universe_d2_038_pcmp_basefill_038'], 'func': pcmp_base_universe_d3_038_pcmp_basefill_038}


def pcmp_base_universe_d3_039_pcmp_basefill_039(pcmp_base_universe_d2_039_pcmp_basefill_039):
    return _base_universe_d3(pcmp_base_universe_d2_039_pcmp_basefill_039, 39)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_039_pcmp_basefill_039'] = {'inputs': ['pcmp_base_universe_d2_039_pcmp_basefill_039'], 'func': pcmp_base_universe_d3_039_pcmp_basefill_039}


def pcmp_base_universe_d3_040_pcmp_basefill_040(pcmp_base_universe_d2_040_pcmp_basefill_040):
    return _base_universe_d3(pcmp_base_universe_d2_040_pcmp_basefill_040, 40)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_040_pcmp_basefill_040'] = {'inputs': ['pcmp_base_universe_d2_040_pcmp_basefill_040'], 'func': pcmp_base_universe_d3_040_pcmp_basefill_040}


def pcmp_base_universe_d3_041_pcmp_basefill_041(pcmp_base_universe_d2_041_pcmp_basefill_041):
    return _base_universe_d3(pcmp_base_universe_d2_041_pcmp_basefill_041, 41)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_041_pcmp_basefill_041'] = {'inputs': ['pcmp_base_universe_d2_041_pcmp_basefill_041'], 'func': pcmp_base_universe_d3_041_pcmp_basefill_041}


def pcmp_base_universe_d3_042_pcmp_basefill_042(pcmp_base_universe_d2_042_pcmp_basefill_042):
    return _base_universe_d3(pcmp_base_universe_d2_042_pcmp_basefill_042, 42)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_042_pcmp_basefill_042'] = {'inputs': ['pcmp_base_universe_d2_042_pcmp_basefill_042'], 'func': pcmp_base_universe_d3_042_pcmp_basefill_042}


def pcmp_base_universe_d3_043_pcmp_basefill_043(pcmp_base_universe_d2_043_pcmp_basefill_043):
    return _base_universe_d3(pcmp_base_universe_d2_043_pcmp_basefill_043, 43)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_043_pcmp_basefill_043'] = {'inputs': ['pcmp_base_universe_d2_043_pcmp_basefill_043'], 'func': pcmp_base_universe_d3_043_pcmp_basefill_043}


def pcmp_base_universe_d3_044_pcmp_basefill_044(pcmp_base_universe_d2_044_pcmp_basefill_044):
    return _base_universe_d3(pcmp_base_universe_d2_044_pcmp_basefill_044, 44)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_044_pcmp_basefill_044'] = {'inputs': ['pcmp_base_universe_d2_044_pcmp_basefill_044'], 'func': pcmp_base_universe_d3_044_pcmp_basefill_044}


def pcmp_base_universe_d3_045_pcmp_basefill_045(pcmp_base_universe_d2_045_pcmp_basefill_045):
    return _base_universe_d3(pcmp_base_universe_d2_045_pcmp_basefill_045, 45)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_045_pcmp_basefill_045'] = {'inputs': ['pcmp_base_universe_d2_045_pcmp_basefill_045'], 'func': pcmp_base_universe_d3_045_pcmp_basefill_045}


def pcmp_base_universe_d3_046_pcmp_basefill_046(pcmp_base_universe_d2_046_pcmp_basefill_046):
    return _base_universe_d3(pcmp_base_universe_d2_046_pcmp_basefill_046, 46)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_046_pcmp_basefill_046'] = {'inputs': ['pcmp_base_universe_d2_046_pcmp_basefill_046'], 'func': pcmp_base_universe_d3_046_pcmp_basefill_046}


def pcmp_base_universe_d3_047_pcmp_basefill_047(pcmp_base_universe_d2_047_pcmp_basefill_047):
    return _base_universe_d3(pcmp_base_universe_d2_047_pcmp_basefill_047, 47)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_047_pcmp_basefill_047'] = {'inputs': ['pcmp_base_universe_d2_047_pcmp_basefill_047'], 'func': pcmp_base_universe_d3_047_pcmp_basefill_047}


def pcmp_base_universe_d3_048_pcmp_basefill_048(pcmp_base_universe_d2_048_pcmp_basefill_048):
    return _base_universe_d3(pcmp_base_universe_d2_048_pcmp_basefill_048, 48)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_048_pcmp_basefill_048'] = {'inputs': ['pcmp_base_universe_d2_048_pcmp_basefill_048'], 'func': pcmp_base_universe_d3_048_pcmp_basefill_048}


def pcmp_base_universe_d3_049_pcmp_basefill_049(pcmp_base_universe_d2_049_pcmp_basefill_049):
    return _base_universe_d3(pcmp_base_universe_d2_049_pcmp_basefill_049, 49)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_049_pcmp_basefill_049'] = {'inputs': ['pcmp_base_universe_d2_049_pcmp_basefill_049'], 'func': pcmp_base_universe_d3_049_pcmp_basefill_049}


def pcmp_base_universe_d3_050_pcmp_basefill_050(pcmp_base_universe_d2_050_pcmp_basefill_050):
    return _base_universe_d3(pcmp_base_universe_d2_050_pcmp_basefill_050, 50)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_050_pcmp_basefill_050'] = {'inputs': ['pcmp_base_universe_d2_050_pcmp_basefill_050'], 'func': pcmp_base_universe_d3_050_pcmp_basefill_050}


def pcmp_base_universe_d3_051_pcmp_basefill_051(pcmp_base_universe_d2_051_pcmp_basefill_051):
    return _base_universe_d3(pcmp_base_universe_d2_051_pcmp_basefill_051, 51)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_051_pcmp_basefill_051'] = {'inputs': ['pcmp_base_universe_d2_051_pcmp_basefill_051'], 'func': pcmp_base_universe_d3_051_pcmp_basefill_051}


def pcmp_base_universe_d3_052_pcmp_basefill_052(pcmp_base_universe_d2_052_pcmp_basefill_052):
    return _base_universe_d3(pcmp_base_universe_d2_052_pcmp_basefill_052, 52)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_052_pcmp_basefill_052'] = {'inputs': ['pcmp_base_universe_d2_052_pcmp_basefill_052'], 'func': pcmp_base_universe_d3_052_pcmp_basefill_052}


def pcmp_base_universe_d3_053_pcmp_basefill_053(pcmp_base_universe_d2_053_pcmp_basefill_053):
    return _base_universe_d3(pcmp_base_universe_d2_053_pcmp_basefill_053, 53)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_053_pcmp_basefill_053'] = {'inputs': ['pcmp_base_universe_d2_053_pcmp_basefill_053'], 'func': pcmp_base_universe_d3_053_pcmp_basefill_053}


def pcmp_base_universe_d3_054_pcmp_basefill_054(pcmp_base_universe_d2_054_pcmp_basefill_054):
    return _base_universe_d3(pcmp_base_universe_d2_054_pcmp_basefill_054, 54)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_054_pcmp_basefill_054'] = {'inputs': ['pcmp_base_universe_d2_054_pcmp_basefill_054'], 'func': pcmp_base_universe_d3_054_pcmp_basefill_054}


def pcmp_base_universe_d3_055_pcmp_basefill_055(pcmp_base_universe_d2_055_pcmp_basefill_055):
    return _base_universe_d3(pcmp_base_universe_d2_055_pcmp_basefill_055, 55)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_055_pcmp_basefill_055'] = {'inputs': ['pcmp_base_universe_d2_055_pcmp_basefill_055'], 'func': pcmp_base_universe_d3_055_pcmp_basefill_055}


def pcmp_base_universe_d3_056_pcmp_basefill_056(pcmp_base_universe_d2_056_pcmp_basefill_056):
    return _base_universe_d3(pcmp_base_universe_d2_056_pcmp_basefill_056, 56)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_056_pcmp_basefill_056'] = {'inputs': ['pcmp_base_universe_d2_056_pcmp_basefill_056'], 'func': pcmp_base_universe_d3_056_pcmp_basefill_056}


def pcmp_base_universe_d3_057_pcmp_basefill_057(pcmp_base_universe_d2_057_pcmp_basefill_057):
    return _base_universe_d3(pcmp_base_universe_d2_057_pcmp_basefill_057, 57)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_057_pcmp_basefill_057'] = {'inputs': ['pcmp_base_universe_d2_057_pcmp_basefill_057'], 'func': pcmp_base_universe_d3_057_pcmp_basefill_057}


def pcmp_base_universe_d3_058_pcmp_basefill_058(pcmp_base_universe_d2_058_pcmp_basefill_058):
    return _base_universe_d3(pcmp_base_universe_d2_058_pcmp_basefill_058, 58)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_058_pcmp_basefill_058'] = {'inputs': ['pcmp_base_universe_d2_058_pcmp_basefill_058'], 'func': pcmp_base_universe_d3_058_pcmp_basefill_058}


def pcmp_base_universe_d3_059_pcmp_basefill_059(pcmp_base_universe_d2_059_pcmp_basefill_059):
    return _base_universe_d3(pcmp_base_universe_d2_059_pcmp_basefill_059, 59)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_059_pcmp_basefill_059'] = {'inputs': ['pcmp_base_universe_d2_059_pcmp_basefill_059'], 'func': pcmp_base_universe_d3_059_pcmp_basefill_059}


def pcmp_base_universe_d3_060_pcmp_basefill_060(pcmp_base_universe_d2_060_pcmp_basefill_060):
    return _base_universe_d3(pcmp_base_universe_d2_060_pcmp_basefill_060, 60)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_060_pcmp_basefill_060'] = {'inputs': ['pcmp_base_universe_d2_060_pcmp_basefill_060'], 'func': pcmp_base_universe_d3_060_pcmp_basefill_060}


def pcmp_base_universe_d3_061_pcmp_basefill_061(pcmp_base_universe_d2_061_pcmp_basefill_061):
    return _base_universe_d3(pcmp_base_universe_d2_061_pcmp_basefill_061, 61)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_061_pcmp_basefill_061'] = {'inputs': ['pcmp_base_universe_d2_061_pcmp_basefill_061'], 'func': pcmp_base_universe_d3_061_pcmp_basefill_061}


def pcmp_base_universe_d3_062_pcmp_basefill_062(pcmp_base_universe_d2_062_pcmp_basefill_062):
    return _base_universe_d3(pcmp_base_universe_d2_062_pcmp_basefill_062, 62)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_062_pcmp_basefill_062'] = {'inputs': ['pcmp_base_universe_d2_062_pcmp_basefill_062'], 'func': pcmp_base_universe_d3_062_pcmp_basefill_062}


def pcmp_base_universe_d3_063_pcmp_basefill_063(pcmp_base_universe_d2_063_pcmp_basefill_063):
    return _base_universe_d3(pcmp_base_universe_d2_063_pcmp_basefill_063, 63)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_063_pcmp_basefill_063'] = {'inputs': ['pcmp_base_universe_d2_063_pcmp_basefill_063'], 'func': pcmp_base_universe_d3_063_pcmp_basefill_063}


def pcmp_base_universe_d3_064_pcmp_basefill_064(pcmp_base_universe_d2_064_pcmp_basefill_064):
    return _base_universe_d3(pcmp_base_universe_d2_064_pcmp_basefill_064, 64)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_064_pcmp_basefill_064'] = {'inputs': ['pcmp_base_universe_d2_064_pcmp_basefill_064'], 'func': pcmp_base_universe_d3_064_pcmp_basefill_064}


def pcmp_base_universe_d3_065_pcmp_basefill_065(pcmp_base_universe_d2_065_pcmp_basefill_065):
    return _base_universe_d3(pcmp_base_universe_d2_065_pcmp_basefill_065, 65)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_065_pcmp_basefill_065'] = {'inputs': ['pcmp_base_universe_d2_065_pcmp_basefill_065'], 'func': pcmp_base_universe_d3_065_pcmp_basefill_065}


def pcmp_base_universe_d3_066_pcmp_basefill_066(pcmp_base_universe_d2_066_pcmp_basefill_066):
    return _base_universe_d3(pcmp_base_universe_d2_066_pcmp_basefill_066, 66)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_066_pcmp_basefill_066'] = {'inputs': ['pcmp_base_universe_d2_066_pcmp_basefill_066'], 'func': pcmp_base_universe_d3_066_pcmp_basefill_066}


def pcmp_base_universe_d3_067_pcmp_basefill_067(pcmp_base_universe_d2_067_pcmp_basefill_067):
    return _base_universe_d3(pcmp_base_universe_d2_067_pcmp_basefill_067, 67)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_067_pcmp_basefill_067'] = {'inputs': ['pcmp_base_universe_d2_067_pcmp_basefill_067'], 'func': pcmp_base_universe_d3_067_pcmp_basefill_067}


def pcmp_base_universe_d3_068_pcmp_basefill_068(pcmp_base_universe_d2_068_pcmp_basefill_068):
    return _base_universe_d3(pcmp_base_universe_d2_068_pcmp_basefill_068, 68)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_068_pcmp_basefill_068'] = {'inputs': ['pcmp_base_universe_d2_068_pcmp_basefill_068'], 'func': pcmp_base_universe_d3_068_pcmp_basefill_068}


def pcmp_base_universe_d3_069_pcmp_basefill_069(pcmp_base_universe_d2_069_pcmp_basefill_069):
    return _base_universe_d3(pcmp_base_universe_d2_069_pcmp_basefill_069, 69)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_069_pcmp_basefill_069'] = {'inputs': ['pcmp_base_universe_d2_069_pcmp_basefill_069'], 'func': pcmp_base_universe_d3_069_pcmp_basefill_069}


def pcmp_base_universe_d3_070_pcmp_basefill_070(pcmp_base_universe_d2_070_pcmp_basefill_070):
    return _base_universe_d3(pcmp_base_universe_d2_070_pcmp_basefill_070, 70)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_070_pcmp_basefill_070'] = {'inputs': ['pcmp_base_universe_d2_070_pcmp_basefill_070'], 'func': pcmp_base_universe_d3_070_pcmp_basefill_070}


def pcmp_base_universe_d3_071_pcmp_basefill_071(pcmp_base_universe_d2_071_pcmp_basefill_071):
    return _base_universe_d3(pcmp_base_universe_d2_071_pcmp_basefill_071, 71)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_071_pcmp_basefill_071'] = {'inputs': ['pcmp_base_universe_d2_071_pcmp_basefill_071'], 'func': pcmp_base_universe_d3_071_pcmp_basefill_071}


def pcmp_base_universe_d3_072_pcmp_basefill_072(pcmp_base_universe_d2_072_pcmp_basefill_072):
    return _base_universe_d3(pcmp_base_universe_d2_072_pcmp_basefill_072, 72)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_072_pcmp_basefill_072'] = {'inputs': ['pcmp_base_universe_d2_072_pcmp_basefill_072'], 'func': pcmp_base_universe_d3_072_pcmp_basefill_072}


def pcmp_base_universe_d3_073_pcmp_basefill_073(pcmp_base_universe_d2_073_pcmp_basefill_073):
    return _base_universe_d3(pcmp_base_universe_d2_073_pcmp_basefill_073, 73)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_073_pcmp_basefill_073'] = {'inputs': ['pcmp_base_universe_d2_073_pcmp_basefill_073'], 'func': pcmp_base_universe_d3_073_pcmp_basefill_073}


def pcmp_base_universe_d3_074_pcmp_basefill_074(pcmp_base_universe_d2_074_pcmp_basefill_074):
    return _base_universe_d3(pcmp_base_universe_d2_074_pcmp_basefill_074, 74)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_074_pcmp_basefill_074'] = {'inputs': ['pcmp_base_universe_d2_074_pcmp_basefill_074'], 'func': pcmp_base_universe_d3_074_pcmp_basefill_074}


def pcmp_base_universe_d3_075_pcmp_basefill_075(pcmp_base_universe_d2_075_pcmp_basefill_075):
    return _base_universe_d3(pcmp_base_universe_d2_075_pcmp_basefill_075, 75)
PCMP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['pcmp_base_universe_d3_075_pcmp_basefill_075'] = {'inputs': ['pcmp_base_universe_d2_075_pcmp_basefill_075'], 'func': pcmp_base_universe_d3_075_pcmp_basefill_075}
