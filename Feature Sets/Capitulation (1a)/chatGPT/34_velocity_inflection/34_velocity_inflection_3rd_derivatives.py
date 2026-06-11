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



def vif_001_return_decay_accel_1(vif_001_return_decay_roc_1):
    feature = _s(vif_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def vif_007_return_decay_accel_5(vif_007_return_decay_roc_5):
    feature = _s(vif_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def vif_013_return_decay_accel_42(vif_013_return_decay_roc_42):
    feature = _s(vif_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def vif_179_vif_019_return_decay_42_019_accel_126(vif_154_vif_019_return_decay_42_019_roc_126):
    feature = _s(vif_154_vif_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def vif_180_vif_025_return_decay_5_025_accel_378(vif_155_vif_025_return_decay_5_025_roc_378):
    feature = _s(vif_155_vif_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















VELOCITY_INFLECTION_REGISTRY_3RD_DERIVATIVES = {
    'vif_001_return_decay_accel_1': {'inputs': ['vif_001_return_decay_roc_1'], 'func': vif_001_return_decay_accel_1},
    'vif_007_return_decay_accel_5': {'inputs': ['vif_007_return_decay_roc_5'], 'func': vif_007_return_decay_accel_5},
    'vif_013_return_decay_accel_42': {'inputs': ['vif_013_return_decay_roc_42'], 'func': vif_013_return_decay_accel_42},
    'vif_179_vif_019_return_decay_42_019_accel_126': {'inputs': ['vif_154_vif_019_return_decay_42_019_roc_126'], 'func': vif_179_vif_019_return_decay_42_019_accel_126},
    'vif_180_vif_025_return_decay_5_025_accel_378': {'inputs': ['vif_155_vif_025_return_decay_5_025_roc_378'], 'func': vif_180_vif_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def vi_replacement_d3_001(vi_replacement_d2_001):
    feature = _clean(vi_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_001'] = {'inputs': ['vi_replacement_d2_001'], 'func': vi_replacement_d3_001}


def vi_replacement_d3_002(vi_replacement_d2_002):
    feature = _clean(vi_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_002'] = {'inputs': ['vi_replacement_d2_002'], 'func': vi_replacement_d3_002}


def vi_replacement_d3_003(vi_replacement_d2_003):
    feature = _clean(vi_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_003'] = {'inputs': ['vi_replacement_d2_003'], 'func': vi_replacement_d3_003}


def vi_replacement_d3_004(vi_replacement_d2_004):
    feature = _clean(vi_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_004'] = {'inputs': ['vi_replacement_d2_004'], 'func': vi_replacement_d3_004}


def vi_replacement_d3_005(vi_replacement_d2_005):
    feature = _clean(vi_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_005'] = {'inputs': ['vi_replacement_d2_005'], 'func': vi_replacement_d3_005}


def vi_replacement_d3_006(vi_replacement_d2_006):
    feature = _clean(vi_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_006'] = {'inputs': ['vi_replacement_d2_006'], 'func': vi_replacement_d3_006}


def vi_replacement_d3_007(vi_replacement_d2_007):
    feature = _clean(vi_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_007'] = {'inputs': ['vi_replacement_d2_007'], 'func': vi_replacement_d3_007}


def vi_replacement_d3_008(vi_replacement_d2_008):
    feature = _clean(vi_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_008'] = {'inputs': ['vi_replacement_d2_008'], 'func': vi_replacement_d3_008}


def vi_replacement_d3_009(vi_replacement_d2_009):
    feature = _clean(vi_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_009'] = {'inputs': ['vi_replacement_d2_009'], 'func': vi_replacement_d3_009}


def vi_replacement_d3_010(vi_replacement_d2_010):
    feature = _clean(vi_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_010'] = {'inputs': ['vi_replacement_d2_010'], 'func': vi_replacement_d3_010}


def vi_replacement_d3_011(vi_replacement_d2_011):
    feature = _clean(vi_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_011'] = {'inputs': ['vi_replacement_d2_011'], 'func': vi_replacement_d3_011}


def vi_replacement_d3_012(vi_replacement_d2_012):
    feature = _clean(vi_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_012'] = {'inputs': ['vi_replacement_d2_012'], 'func': vi_replacement_d3_012}


def vi_replacement_d3_013(vi_replacement_d2_013):
    feature = _clean(vi_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_013'] = {'inputs': ['vi_replacement_d2_013'], 'func': vi_replacement_d3_013}


def vi_replacement_d3_014(vi_replacement_d2_014):
    feature = _clean(vi_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_014'] = {'inputs': ['vi_replacement_d2_014'], 'func': vi_replacement_d3_014}


def vi_replacement_d3_015(vi_replacement_d2_015):
    feature = _clean(vi_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_015'] = {'inputs': ['vi_replacement_d2_015'], 'func': vi_replacement_d3_015}


def vi_replacement_d3_016(vi_replacement_d2_016):
    feature = _clean(vi_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_016'] = {'inputs': ['vi_replacement_d2_016'], 'func': vi_replacement_d3_016}


def vi_replacement_d3_017(vi_replacement_d2_017):
    feature = _clean(vi_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_017'] = {'inputs': ['vi_replacement_d2_017'], 'func': vi_replacement_d3_017}


def vi_replacement_d3_018(vi_replacement_d2_018):
    feature = _clean(vi_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_018'] = {'inputs': ['vi_replacement_d2_018'], 'func': vi_replacement_d3_018}


def vi_replacement_d3_019(vi_replacement_d2_019):
    feature = _clean(vi_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_019'] = {'inputs': ['vi_replacement_d2_019'], 'func': vi_replacement_d3_019}


def vi_replacement_d3_020(vi_replacement_d2_020):
    feature = _clean(vi_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_020'] = {'inputs': ['vi_replacement_d2_020'], 'func': vi_replacement_d3_020}


def vi_replacement_d3_021(vi_replacement_d2_021):
    feature = _clean(vi_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_021'] = {'inputs': ['vi_replacement_d2_021'], 'func': vi_replacement_d3_021}


def vi_replacement_d3_022(vi_replacement_d2_022):
    feature = _clean(vi_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_022'] = {'inputs': ['vi_replacement_d2_022'], 'func': vi_replacement_d3_022}


def vi_replacement_d3_023(vi_replacement_d2_023):
    feature = _clean(vi_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_023'] = {'inputs': ['vi_replacement_d2_023'], 'func': vi_replacement_d3_023}


def vi_replacement_d3_024(vi_replacement_d2_024):
    feature = _clean(vi_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_024'] = {'inputs': ['vi_replacement_d2_024'], 'func': vi_replacement_d3_024}


def vi_replacement_d3_025(vi_replacement_d2_025):
    feature = _clean(vi_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_025'] = {'inputs': ['vi_replacement_d2_025'], 'func': vi_replacement_d3_025}


def vi_replacement_d3_026(vi_replacement_d2_026):
    feature = _clean(vi_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_026'] = {'inputs': ['vi_replacement_d2_026'], 'func': vi_replacement_d3_026}


def vi_replacement_d3_027(vi_replacement_d2_027):
    feature = _clean(vi_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_027'] = {'inputs': ['vi_replacement_d2_027'], 'func': vi_replacement_d3_027}


def vi_replacement_d3_028(vi_replacement_d2_028):
    feature = _clean(vi_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_028'] = {'inputs': ['vi_replacement_d2_028'], 'func': vi_replacement_d3_028}


def vi_replacement_d3_029(vi_replacement_d2_029):
    feature = _clean(vi_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_029'] = {'inputs': ['vi_replacement_d2_029'], 'func': vi_replacement_d3_029}


def vi_replacement_d3_030(vi_replacement_d2_030):
    feature = _clean(vi_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_030'] = {'inputs': ['vi_replacement_d2_030'], 'func': vi_replacement_d3_030}


def vi_replacement_d3_031(vi_replacement_d2_031):
    feature = _clean(vi_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_031'] = {'inputs': ['vi_replacement_d2_031'], 'func': vi_replacement_d3_031}


def vi_replacement_d3_032(vi_replacement_d2_032):
    feature = _clean(vi_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_032'] = {'inputs': ['vi_replacement_d2_032'], 'func': vi_replacement_d3_032}


def vi_replacement_d3_033(vi_replacement_d2_033):
    feature = _clean(vi_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_033'] = {'inputs': ['vi_replacement_d2_033'], 'func': vi_replacement_d3_033}


def vi_replacement_d3_034(vi_replacement_d2_034):
    feature = _clean(vi_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_034'] = {'inputs': ['vi_replacement_d2_034'], 'func': vi_replacement_d3_034}


def vi_replacement_d3_035(vi_replacement_d2_035):
    feature = _clean(vi_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_035'] = {'inputs': ['vi_replacement_d2_035'], 'func': vi_replacement_d3_035}


def vi_replacement_d3_036(vi_replacement_d2_036):
    feature = _clean(vi_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_036'] = {'inputs': ['vi_replacement_d2_036'], 'func': vi_replacement_d3_036}


def vi_replacement_d3_037(vi_replacement_d2_037):
    feature = _clean(vi_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_037'] = {'inputs': ['vi_replacement_d2_037'], 'func': vi_replacement_d3_037}


def vi_replacement_d3_038(vi_replacement_d2_038):
    feature = _clean(vi_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_038'] = {'inputs': ['vi_replacement_d2_038'], 'func': vi_replacement_d3_038}


def vi_replacement_d3_039(vi_replacement_d2_039):
    feature = _clean(vi_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_039'] = {'inputs': ['vi_replacement_d2_039'], 'func': vi_replacement_d3_039}


def vi_replacement_d3_040(vi_replacement_d2_040):
    feature = _clean(vi_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_040'] = {'inputs': ['vi_replacement_d2_040'], 'func': vi_replacement_d3_040}


def vi_replacement_d3_041(vi_replacement_d2_041):
    feature = _clean(vi_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_041'] = {'inputs': ['vi_replacement_d2_041'], 'func': vi_replacement_d3_041}


def vi_replacement_d3_042(vi_replacement_d2_042):
    feature = _clean(vi_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_042'] = {'inputs': ['vi_replacement_d2_042'], 'func': vi_replacement_d3_042}


def vi_replacement_d3_043(vi_replacement_d2_043):
    feature = _clean(vi_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_043'] = {'inputs': ['vi_replacement_d2_043'], 'func': vi_replacement_d3_043}


def vi_replacement_d3_044(vi_replacement_d2_044):
    feature = _clean(vi_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_044'] = {'inputs': ['vi_replacement_d2_044'], 'func': vi_replacement_d3_044}


def vi_replacement_d3_045(vi_replacement_d2_045):
    feature = _clean(vi_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_045'] = {'inputs': ['vi_replacement_d2_045'], 'func': vi_replacement_d3_045}


def vi_replacement_d3_046(vi_replacement_d2_046):
    feature = _clean(vi_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_046'] = {'inputs': ['vi_replacement_d2_046'], 'func': vi_replacement_d3_046}


def vi_replacement_d3_047(vi_replacement_d2_047):
    feature = _clean(vi_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_047'] = {'inputs': ['vi_replacement_d2_047'], 'func': vi_replacement_d3_047}


def vi_replacement_d3_048(vi_replacement_d2_048):
    feature = _clean(vi_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_048'] = {'inputs': ['vi_replacement_d2_048'], 'func': vi_replacement_d3_048}


def vi_replacement_d3_049(vi_replacement_d2_049):
    feature = _clean(vi_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_049'] = {'inputs': ['vi_replacement_d2_049'], 'func': vi_replacement_d3_049}


def vi_replacement_d3_050(vi_replacement_d2_050):
    feature = _clean(vi_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_050'] = {'inputs': ['vi_replacement_d2_050'], 'func': vi_replacement_d3_050}


def vi_replacement_d3_051(vi_replacement_d2_051):
    feature = _clean(vi_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_051'] = {'inputs': ['vi_replacement_d2_051'], 'func': vi_replacement_d3_051}


def vi_replacement_d3_052(vi_replacement_d2_052):
    feature = _clean(vi_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_052'] = {'inputs': ['vi_replacement_d2_052'], 'func': vi_replacement_d3_052}


def vi_replacement_d3_053(vi_replacement_d2_053):
    feature = _clean(vi_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_053'] = {'inputs': ['vi_replacement_d2_053'], 'func': vi_replacement_d3_053}


def vi_replacement_d3_054(vi_replacement_d2_054):
    feature = _clean(vi_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_054'] = {'inputs': ['vi_replacement_d2_054'], 'func': vi_replacement_d3_054}


def vi_replacement_d3_055(vi_replacement_d2_055):
    feature = _clean(vi_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_055'] = {'inputs': ['vi_replacement_d2_055'], 'func': vi_replacement_d3_055}


def vi_replacement_d3_056(vi_replacement_d2_056):
    feature = _clean(vi_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_056'] = {'inputs': ['vi_replacement_d2_056'], 'func': vi_replacement_d3_056}


def vi_replacement_d3_057(vi_replacement_d2_057):
    feature = _clean(vi_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_057'] = {'inputs': ['vi_replacement_d2_057'], 'func': vi_replacement_d3_057}


def vi_replacement_d3_058(vi_replacement_d2_058):
    feature = _clean(vi_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_058'] = {'inputs': ['vi_replacement_d2_058'], 'func': vi_replacement_d3_058}


def vi_replacement_d3_059(vi_replacement_d2_059):
    feature = _clean(vi_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_059'] = {'inputs': ['vi_replacement_d2_059'], 'func': vi_replacement_d3_059}


def vi_replacement_d3_060(vi_replacement_d2_060):
    feature = _clean(vi_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_060'] = {'inputs': ['vi_replacement_d2_060'], 'func': vi_replacement_d3_060}


def vi_replacement_d3_061(vi_replacement_d2_061):
    feature = _clean(vi_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_061'] = {'inputs': ['vi_replacement_d2_061'], 'func': vi_replacement_d3_061}


def vi_replacement_d3_062(vi_replacement_d2_062):
    feature = _clean(vi_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_062'] = {'inputs': ['vi_replacement_d2_062'], 'func': vi_replacement_d3_062}


def vi_replacement_d3_063(vi_replacement_d2_063):
    feature = _clean(vi_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_063'] = {'inputs': ['vi_replacement_d2_063'], 'func': vi_replacement_d3_063}


def vi_replacement_d3_064(vi_replacement_d2_064):
    feature = _clean(vi_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_064'] = {'inputs': ['vi_replacement_d2_064'], 'func': vi_replacement_d3_064}


def vi_replacement_d3_065(vi_replacement_d2_065):
    feature = _clean(vi_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_065'] = {'inputs': ['vi_replacement_d2_065'], 'func': vi_replacement_d3_065}


def vi_replacement_d3_066(vi_replacement_d2_066):
    feature = _clean(vi_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_066'] = {'inputs': ['vi_replacement_d2_066'], 'func': vi_replacement_d3_066}


def vi_replacement_d3_067(vi_replacement_d2_067):
    feature = _clean(vi_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_067'] = {'inputs': ['vi_replacement_d2_067'], 'func': vi_replacement_d3_067}


def vi_replacement_d3_068(vi_replacement_d2_068):
    feature = _clean(vi_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_068'] = {'inputs': ['vi_replacement_d2_068'], 'func': vi_replacement_d3_068}


def vi_replacement_d3_069(vi_replacement_d2_069):
    feature = _clean(vi_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_069'] = {'inputs': ['vi_replacement_d2_069'], 'func': vi_replacement_d3_069}


def vi_replacement_d3_070(vi_replacement_d2_070):
    feature = _clean(vi_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_070'] = {'inputs': ['vi_replacement_d2_070'], 'func': vi_replacement_d3_070}


def vi_replacement_d3_071(vi_replacement_d2_071):
    feature = _clean(vi_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_071'] = {'inputs': ['vi_replacement_d2_071'], 'func': vi_replacement_d3_071}


def vi_replacement_d3_072(vi_replacement_d2_072):
    feature = _clean(vi_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_072'] = {'inputs': ['vi_replacement_d2_072'], 'func': vi_replacement_d3_072}


def vi_replacement_d3_073(vi_replacement_d2_073):
    feature = _clean(vi_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_073'] = {'inputs': ['vi_replacement_d2_073'], 'func': vi_replacement_d3_073}


def vi_replacement_d3_074(vi_replacement_d2_074):
    feature = _clean(vi_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_074'] = {'inputs': ['vi_replacement_d2_074'], 'func': vi_replacement_d3_074}


def vi_replacement_d3_075(vi_replacement_d2_075):
    feature = _clean(vi_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_075'] = {'inputs': ['vi_replacement_d2_075'], 'func': vi_replacement_d3_075}


def vi_replacement_d3_076(vi_replacement_d2_076):
    feature = _clean(vi_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_076'] = {'inputs': ['vi_replacement_d2_076'], 'func': vi_replacement_d3_076}


def vi_replacement_d3_077(vi_replacement_d2_077):
    feature = _clean(vi_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_077'] = {'inputs': ['vi_replacement_d2_077'], 'func': vi_replacement_d3_077}


def vi_replacement_d3_078(vi_replacement_d2_078):
    feature = _clean(vi_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_078'] = {'inputs': ['vi_replacement_d2_078'], 'func': vi_replacement_d3_078}


def vi_replacement_d3_079(vi_replacement_d2_079):
    feature = _clean(vi_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_079'] = {'inputs': ['vi_replacement_d2_079'], 'func': vi_replacement_d3_079}


def vi_replacement_d3_080(vi_replacement_d2_080):
    feature = _clean(vi_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_080'] = {'inputs': ['vi_replacement_d2_080'], 'func': vi_replacement_d3_080}


def vi_replacement_d3_081(vi_replacement_d2_081):
    feature = _clean(vi_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_081'] = {'inputs': ['vi_replacement_d2_081'], 'func': vi_replacement_d3_081}


def vi_replacement_d3_082(vi_replacement_d2_082):
    feature = _clean(vi_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_082'] = {'inputs': ['vi_replacement_d2_082'], 'func': vi_replacement_d3_082}


def vi_replacement_d3_083(vi_replacement_d2_083):
    feature = _clean(vi_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_083'] = {'inputs': ['vi_replacement_d2_083'], 'func': vi_replacement_d3_083}


def vi_replacement_d3_084(vi_replacement_d2_084):
    feature = _clean(vi_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_084'] = {'inputs': ['vi_replacement_d2_084'], 'func': vi_replacement_d3_084}


def vi_replacement_d3_085(vi_replacement_d2_085):
    feature = _clean(vi_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_085'] = {'inputs': ['vi_replacement_d2_085'], 'func': vi_replacement_d3_085}


def vi_replacement_d3_086(vi_replacement_d2_086):
    feature = _clean(vi_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_086'] = {'inputs': ['vi_replacement_d2_086'], 'func': vi_replacement_d3_086}


def vi_replacement_d3_087(vi_replacement_d2_087):
    feature = _clean(vi_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_087'] = {'inputs': ['vi_replacement_d2_087'], 'func': vi_replacement_d3_087}


def vi_replacement_d3_088(vi_replacement_d2_088):
    feature = _clean(vi_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_088'] = {'inputs': ['vi_replacement_d2_088'], 'func': vi_replacement_d3_088}


def vi_replacement_d3_089(vi_replacement_d2_089):
    feature = _clean(vi_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_089'] = {'inputs': ['vi_replacement_d2_089'], 'func': vi_replacement_d3_089}


def vi_replacement_d3_090(vi_replacement_d2_090):
    feature = _clean(vi_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_090'] = {'inputs': ['vi_replacement_d2_090'], 'func': vi_replacement_d3_090}


def vi_replacement_d3_091(vi_replacement_d2_091):
    feature = _clean(vi_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_091'] = {'inputs': ['vi_replacement_d2_091'], 'func': vi_replacement_d3_091}


def vi_replacement_d3_092(vi_replacement_d2_092):
    feature = _clean(vi_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_092'] = {'inputs': ['vi_replacement_d2_092'], 'func': vi_replacement_d3_092}


def vi_replacement_d3_093(vi_replacement_d2_093):
    feature = _clean(vi_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_093'] = {'inputs': ['vi_replacement_d2_093'], 'func': vi_replacement_d3_093}


def vi_replacement_d3_094(vi_replacement_d2_094):
    feature = _clean(vi_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_094'] = {'inputs': ['vi_replacement_d2_094'], 'func': vi_replacement_d3_094}


def vi_replacement_d3_095(vi_replacement_d2_095):
    feature = _clean(vi_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_095'] = {'inputs': ['vi_replacement_d2_095'], 'func': vi_replacement_d3_095}


def vi_replacement_d3_096(vi_replacement_d2_096):
    feature = _clean(vi_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_096'] = {'inputs': ['vi_replacement_d2_096'], 'func': vi_replacement_d3_096}


def vi_replacement_d3_097(vi_replacement_d2_097):
    feature = _clean(vi_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_097'] = {'inputs': ['vi_replacement_d2_097'], 'func': vi_replacement_d3_097}


def vi_replacement_d3_098(vi_replacement_d2_098):
    feature = _clean(vi_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_098'] = {'inputs': ['vi_replacement_d2_098'], 'func': vi_replacement_d3_098}


def vi_replacement_d3_099(vi_replacement_d2_099):
    feature = _clean(vi_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_099'] = {'inputs': ['vi_replacement_d2_099'], 'func': vi_replacement_d3_099}


def vi_replacement_d3_100(vi_replacement_d2_100):
    feature = _clean(vi_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_100'] = {'inputs': ['vi_replacement_d2_100'], 'func': vi_replacement_d3_100}


def vi_replacement_d3_101(vi_replacement_d2_101):
    feature = _clean(vi_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_101'] = {'inputs': ['vi_replacement_d2_101'], 'func': vi_replacement_d3_101}


def vi_replacement_d3_102(vi_replacement_d2_102):
    feature = _clean(vi_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_102'] = {'inputs': ['vi_replacement_d2_102'], 'func': vi_replacement_d3_102}


def vi_replacement_d3_103(vi_replacement_d2_103):
    feature = _clean(vi_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_103'] = {'inputs': ['vi_replacement_d2_103'], 'func': vi_replacement_d3_103}


def vi_replacement_d3_104(vi_replacement_d2_104):
    feature = _clean(vi_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_104'] = {'inputs': ['vi_replacement_d2_104'], 'func': vi_replacement_d3_104}


def vi_replacement_d3_105(vi_replacement_d2_105):
    feature = _clean(vi_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_105'] = {'inputs': ['vi_replacement_d2_105'], 'func': vi_replacement_d3_105}


def vi_replacement_d3_106(vi_replacement_d2_106):
    feature = _clean(vi_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_106'] = {'inputs': ['vi_replacement_d2_106'], 'func': vi_replacement_d3_106}


def vi_replacement_d3_107(vi_replacement_d2_107):
    feature = _clean(vi_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_107'] = {'inputs': ['vi_replacement_d2_107'], 'func': vi_replacement_d3_107}


def vi_replacement_d3_108(vi_replacement_d2_108):
    feature = _clean(vi_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_108'] = {'inputs': ['vi_replacement_d2_108'], 'func': vi_replacement_d3_108}


def vi_replacement_d3_109(vi_replacement_d2_109):
    feature = _clean(vi_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_109'] = {'inputs': ['vi_replacement_d2_109'], 'func': vi_replacement_d3_109}


def vi_replacement_d3_110(vi_replacement_d2_110):
    feature = _clean(vi_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_110'] = {'inputs': ['vi_replacement_d2_110'], 'func': vi_replacement_d3_110}


def vi_replacement_d3_111(vi_replacement_d2_111):
    feature = _clean(vi_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_111'] = {'inputs': ['vi_replacement_d2_111'], 'func': vi_replacement_d3_111}


def vi_replacement_d3_112(vi_replacement_d2_112):
    feature = _clean(vi_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_112'] = {'inputs': ['vi_replacement_d2_112'], 'func': vi_replacement_d3_112}


def vi_replacement_d3_113(vi_replacement_d2_113):
    feature = _clean(vi_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_113'] = {'inputs': ['vi_replacement_d2_113'], 'func': vi_replacement_d3_113}


def vi_replacement_d3_114(vi_replacement_d2_114):
    feature = _clean(vi_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_114'] = {'inputs': ['vi_replacement_d2_114'], 'func': vi_replacement_d3_114}


def vi_replacement_d3_115(vi_replacement_d2_115):
    feature = _clean(vi_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_115'] = {'inputs': ['vi_replacement_d2_115'], 'func': vi_replacement_d3_115}


def vi_replacement_d3_116(vi_replacement_d2_116):
    feature = _clean(vi_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_116'] = {'inputs': ['vi_replacement_d2_116'], 'func': vi_replacement_d3_116}


def vi_replacement_d3_117(vi_replacement_d2_117):
    feature = _clean(vi_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_117'] = {'inputs': ['vi_replacement_d2_117'], 'func': vi_replacement_d3_117}


def vi_replacement_d3_118(vi_replacement_d2_118):
    feature = _clean(vi_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_118'] = {'inputs': ['vi_replacement_d2_118'], 'func': vi_replacement_d3_118}


def vi_replacement_d3_119(vi_replacement_d2_119):
    feature = _clean(vi_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_119'] = {'inputs': ['vi_replacement_d2_119'], 'func': vi_replacement_d3_119}


def vi_replacement_d3_120(vi_replacement_d2_120):
    feature = _clean(vi_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_120'] = {'inputs': ['vi_replacement_d2_120'], 'func': vi_replacement_d3_120}


def vi_replacement_d3_121(vi_replacement_d2_121):
    feature = _clean(vi_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_121'] = {'inputs': ['vi_replacement_d2_121'], 'func': vi_replacement_d3_121}


def vi_replacement_d3_122(vi_replacement_d2_122):
    feature = _clean(vi_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_122'] = {'inputs': ['vi_replacement_d2_122'], 'func': vi_replacement_d3_122}


def vi_replacement_d3_123(vi_replacement_d2_123):
    feature = _clean(vi_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_123'] = {'inputs': ['vi_replacement_d2_123'], 'func': vi_replacement_d3_123}


def vi_replacement_d3_124(vi_replacement_d2_124):
    feature = _clean(vi_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_124'] = {'inputs': ['vi_replacement_d2_124'], 'func': vi_replacement_d3_124}


def vi_replacement_d3_125(vi_replacement_d2_125):
    feature = _clean(vi_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_125'] = {'inputs': ['vi_replacement_d2_125'], 'func': vi_replacement_d3_125}


def vi_replacement_d3_126(vi_replacement_d2_126):
    feature = _clean(vi_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_126'] = {'inputs': ['vi_replacement_d2_126'], 'func': vi_replacement_d3_126}


def vi_replacement_d3_127(vi_replacement_d2_127):
    feature = _clean(vi_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_127'] = {'inputs': ['vi_replacement_d2_127'], 'func': vi_replacement_d3_127}


def vi_replacement_d3_128(vi_replacement_d2_128):
    feature = _clean(vi_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_128'] = {'inputs': ['vi_replacement_d2_128'], 'func': vi_replacement_d3_128}


def vi_replacement_d3_129(vi_replacement_d2_129):
    feature = _clean(vi_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_129'] = {'inputs': ['vi_replacement_d2_129'], 'func': vi_replacement_d3_129}


def vi_replacement_d3_130(vi_replacement_d2_130):
    feature = _clean(vi_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_130'] = {'inputs': ['vi_replacement_d2_130'], 'func': vi_replacement_d3_130}


def vi_replacement_d3_131(vi_replacement_d2_131):
    feature = _clean(vi_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_131'] = {'inputs': ['vi_replacement_d2_131'], 'func': vi_replacement_d3_131}


def vi_replacement_d3_132(vi_replacement_d2_132):
    feature = _clean(vi_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_132'] = {'inputs': ['vi_replacement_d2_132'], 'func': vi_replacement_d3_132}


def vi_replacement_d3_133(vi_replacement_d2_133):
    feature = _clean(vi_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_133'] = {'inputs': ['vi_replacement_d2_133'], 'func': vi_replacement_d3_133}


def vi_replacement_d3_134(vi_replacement_d2_134):
    feature = _clean(vi_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_134'] = {'inputs': ['vi_replacement_d2_134'], 'func': vi_replacement_d3_134}


def vi_replacement_d3_135(vi_replacement_d2_135):
    feature = _clean(vi_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_135'] = {'inputs': ['vi_replacement_d2_135'], 'func': vi_replacement_d3_135}


def vi_replacement_d3_136(vi_replacement_d2_136):
    feature = _clean(vi_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_136'] = {'inputs': ['vi_replacement_d2_136'], 'func': vi_replacement_d3_136}


def vi_replacement_d3_137(vi_replacement_d2_137):
    feature = _clean(vi_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_137'] = {'inputs': ['vi_replacement_d2_137'], 'func': vi_replacement_d3_137}


def vi_replacement_d3_138(vi_replacement_d2_138):
    feature = _clean(vi_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_138'] = {'inputs': ['vi_replacement_d2_138'], 'func': vi_replacement_d3_138}


def vi_replacement_d3_139(vi_replacement_d2_139):
    feature = _clean(vi_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_139'] = {'inputs': ['vi_replacement_d2_139'], 'func': vi_replacement_d3_139}


def vi_replacement_d3_140(vi_replacement_d2_140):
    feature = _clean(vi_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_140'] = {'inputs': ['vi_replacement_d2_140'], 'func': vi_replacement_d3_140}


def vi_replacement_d3_141(vi_replacement_d2_141):
    feature = _clean(vi_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_141'] = {'inputs': ['vi_replacement_d2_141'], 'func': vi_replacement_d3_141}


def vi_replacement_d3_142(vi_replacement_d2_142):
    feature = _clean(vi_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_142'] = {'inputs': ['vi_replacement_d2_142'], 'func': vi_replacement_d3_142}


def vi_replacement_d3_143(vi_replacement_d2_143):
    feature = _clean(vi_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_143'] = {'inputs': ['vi_replacement_d2_143'], 'func': vi_replacement_d3_143}


def vi_replacement_d3_144(vi_replacement_d2_144):
    feature = _clean(vi_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_144'] = {'inputs': ['vi_replacement_d2_144'], 'func': vi_replacement_d3_144}


def vi_replacement_d3_145(vi_replacement_d2_145):
    feature = _clean(vi_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_145'] = {'inputs': ['vi_replacement_d2_145'], 'func': vi_replacement_d3_145}


def vi_replacement_d3_146(vi_replacement_d2_146):
    feature = _clean(vi_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_146'] = {'inputs': ['vi_replacement_d2_146'], 'func': vi_replacement_d3_146}


def vi_replacement_d3_147(vi_replacement_d2_147):
    feature = _clean(vi_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_147'] = {'inputs': ['vi_replacement_d2_147'], 'func': vi_replacement_d3_147}


def vi_replacement_d3_148(vi_replacement_d2_148):
    feature = _clean(vi_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_148'] = {'inputs': ['vi_replacement_d2_148'], 'func': vi_replacement_d3_148}


def vi_replacement_d3_149(vi_replacement_d2_149):
    feature = _clean(vi_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_149'] = {'inputs': ['vi_replacement_d2_149'], 'func': vi_replacement_d3_149}


def vi_replacement_d3_150(vi_replacement_d2_150):
    feature = _clean(vi_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_150'] = {'inputs': ['vi_replacement_d2_150'], 'func': vi_replacement_d3_150}


def vi_replacement_d3_151(vi_replacement_d2_151):
    feature = _clean(vi_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_151'] = {'inputs': ['vi_replacement_d2_151'], 'func': vi_replacement_d3_151}


def vi_replacement_d3_152(vi_replacement_d2_152):
    feature = _clean(vi_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_152'] = {'inputs': ['vi_replacement_d2_152'], 'func': vi_replacement_d3_152}


def vi_replacement_d3_153(vi_replacement_d2_153):
    feature = _clean(vi_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_153'] = {'inputs': ['vi_replacement_d2_153'], 'func': vi_replacement_d3_153}


def vi_replacement_d3_154(vi_replacement_d2_154):
    feature = _clean(vi_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_154'] = {'inputs': ['vi_replacement_d2_154'], 'func': vi_replacement_d3_154}


def vi_replacement_d3_155(vi_replacement_d2_155):
    feature = _clean(vi_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_155'] = {'inputs': ['vi_replacement_d2_155'], 'func': vi_replacement_d3_155}


def vi_replacement_d3_156(vi_replacement_d2_156):
    feature = _clean(vi_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_156'] = {'inputs': ['vi_replacement_d2_156'], 'func': vi_replacement_d3_156}


def vi_replacement_d3_157(vi_replacement_d2_157):
    feature = _clean(vi_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_157'] = {'inputs': ['vi_replacement_d2_157'], 'func': vi_replacement_d3_157}


def vi_replacement_d3_158(vi_replacement_d2_158):
    feature = _clean(vi_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_158'] = {'inputs': ['vi_replacement_d2_158'], 'func': vi_replacement_d3_158}


def vi_replacement_d3_159(vi_replacement_d2_159):
    feature = _clean(vi_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_159'] = {'inputs': ['vi_replacement_d2_159'], 'func': vi_replacement_d3_159}


def vi_replacement_d3_160(vi_replacement_d2_160):
    feature = _clean(vi_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_160'] = {'inputs': ['vi_replacement_d2_160'], 'func': vi_replacement_d3_160}


def vi_replacement_d3_161(vi_replacement_d2_161):
    feature = _clean(vi_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_161'] = {'inputs': ['vi_replacement_d2_161'], 'func': vi_replacement_d3_161}


def vi_replacement_d3_162(vi_replacement_d2_162):
    feature = _clean(vi_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_162'] = {'inputs': ['vi_replacement_d2_162'], 'func': vi_replacement_d3_162}


def vi_replacement_d3_163(vi_replacement_d2_163):
    feature = _clean(vi_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_163'] = {'inputs': ['vi_replacement_d2_163'], 'func': vi_replacement_d3_163}


def vi_replacement_d3_164(vi_replacement_d2_164):
    feature = _clean(vi_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_164'] = {'inputs': ['vi_replacement_d2_164'], 'func': vi_replacement_d3_164}


def vi_replacement_d3_165(vi_replacement_d2_165):
    feature = _clean(vi_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_165'] = {'inputs': ['vi_replacement_d2_165'], 'func': vi_replacement_d3_165}


def vi_replacement_d3_166(vi_replacement_d2_166):
    feature = _clean(vi_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_166'] = {'inputs': ['vi_replacement_d2_166'], 'func': vi_replacement_d3_166}


def vi_replacement_d3_167(vi_replacement_d2_167):
    feature = _clean(vi_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_167'] = {'inputs': ['vi_replacement_d2_167'], 'func': vi_replacement_d3_167}


def vi_replacement_d3_168(vi_replacement_d2_168):
    feature = _clean(vi_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_168'] = {'inputs': ['vi_replacement_d2_168'], 'func': vi_replacement_d3_168}


def vi_replacement_d3_169(vi_replacement_d2_169):
    feature = _clean(vi_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_169'] = {'inputs': ['vi_replacement_d2_169'], 'func': vi_replacement_d3_169}


def vi_replacement_d3_170(vi_replacement_d2_170):
    feature = _clean(vi_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_170'] = {'inputs': ['vi_replacement_d2_170'], 'func': vi_replacement_d3_170}


def vi_replacement_d3_171(vi_replacement_d2_171):
    feature = _clean(vi_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_171'] = {'inputs': ['vi_replacement_d2_171'], 'func': vi_replacement_d3_171}


def vi_replacement_d3_172(vi_replacement_d2_172):
    feature = _clean(vi_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_172'] = {'inputs': ['vi_replacement_d2_172'], 'func': vi_replacement_d3_172}


def vi_replacement_d3_173(vi_replacement_d2_173):
    feature = _clean(vi_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_173'] = {'inputs': ['vi_replacement_d2_173'], 'func': vi_replacement_d3_173}


def vi_replacement_d3_174(vi_replacement_d2_174):
    feature = _clean(vi_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_174'] = {'inputs': ['vi_replacement_d2_174'], 'func': vi_replacement_d3_174}


def vi_replacement_d3_175(vi_replacement_d2_175):
    feature = _clean(vi_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
VI_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['vi_replacement_d3_175'] = {'inputs': ['vi_replacement_d2_175'], 'func': vi_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def vif_base_universe_d3_001_vif_003_loss_streak_21_003(vif_base_universe_d2_001_vif_003_loss_streak_21_003):
    return _base_universe_d3(vif_base_universe_d2_001_vif_003_loss_streak_21_003, 1)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_001_vif_003_loss_streak_21_003'] = {'inputs': ['vif_base_universe_d2_001_vif_003_loss_streak_21_003'], 'func': vif_base_universe_d3_001_vif_003_loss_streak_21_003}


def vif_base_universe_d3_002_vif_004_ma_distance_42_004(vif_base_universe_d2_002_vif_004_ma_distance_42_004):
    return _base_universe_d3(vif_base_universe_d2_002_vif_004_ma_distance_42_004, 2)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_002_vif_004_ma_distance_42_004'] = {'inputs': ['vif_base_universe_d2_002_vif_004_ma_distance_42_004'], 'func': vif_base_universe_d3_002_vif_004_ma_distance_42_004}


def vif_base_universe_d3_003_vif_005_stochastic_position_63_005(vif_base_universe_d2_003_vif_005_stochastic_position_63_005):
    return _base_universe_d3(vif_base_universe_d2_003_vif_005_stochastic_position_63_005, 3)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_003_vif_005_stochastic_position_63_005'] = {'inputs': ['vif_base_universe_d2_003_vif_005_stochastic_position_63_005'], 'func': vif_base_universe_d3_003_vif_005_stochastic_position_63_005}


def vif_base_universe_d3_004_vif_009_loss_streak_252_009(vif_base_universe_d2_004_vif_009_loss_streak_252_009):
    return _base_universe_d3(vif_base_universe_d2_004_vif_009_loss_streak_252_009, 4)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_004_vif_009_loss_streak_252_009'] = {'inputs': ['vif_base_universe_d2_004_vif_009_loss_streak_252_009'], 'func': vif_base_universe_d3_004_vif_009_loss_streak_252_009}


def vif_base_universe_d3_005_vif_010_ma_distance_378_010(vif_base_universe_d2_005_vif_010_ma_distance_378_010):
    return _base_universe_d3(vif_base_universe_d2_005_vif_010_ma_distance_378_010, 5)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_005_vif_010_ma_distance_378_010'] = {'inputs': ['vif_base_universe_d2_005_vif_010_ma_distance_378_010'], 'func': vif_base_universe_d3_005_vif_010_ma_distance_378_010}


def vif_base_universe_d3_006_vif_011_stochastic_position_504_011(vif_base_universe_d2_006_vif_011_stochastic_position_504_011):
    return _base_universe_d3(vif_base_universe_d2_006_vif_011_stochastic_position_504_011, 6)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_006_vif_011_stochastic_position_504_011'] = {'inputs': ['vif_base_universe_d2_006_vif_011_stochastic_position_504_011'], 'func': vif_base_universe_d3_006_vif_011_stochastic_position_504_011}


def vif_base_universe_d3_007_vif_015_loss_streak_1512_015(vif_base_universe_d2_007_vif_015_loss_streak_1512_015):
    return _base_universe_d3(vif_base_universe_d2_007_vif_015_loss_streak_1512_015, 7)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_007_vif_015_loss_streak_1512_015'] = {'inputs': ['vif_base_universe_d2_007_vif_015_loss_streak_1512_015'], 'func': vif_base_universe_d3_007_vif_015_loss_streak_1512_015}


def vif_base_universe_d3_008_vif_016_ma_distance_5_016(vif_base_universe_d2_008_vif_016_ma_distance_5_016):
    return _base_universe_d3(vif_base_universe_d2_008_vif_016_ma_distance_5_016, 8)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_008_vif_016_ma_distance_5_016'] = {'inputs': ['vif_base_universe_d2_008_vif_016_ma_distance_5_016'], 'func': vif_base_universe_d3_008_vif_016_ma_distance_5_016}


def vif_base_universe_d3_009_vif_017_stochastic_position_10_017(vif_base_universe_d2_009_vif_017_stochastic_position_10_017):
    return _base_universe_d3(vif_base_universe_d2_009_vif_017_stochastic_position_10_017, 9)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_009_vif_017_stochastic_position_10_017'] = {'inputs': ['vif_base_universe_d2_009_vif_017_stochastic_position_10_017'], 'func': vif_base_universe_d3_009_vif_017_stochastic_position_10_017}


def vif_base_universe_d3_010_vif_021_loss_streak_84_021(vif_base_universe_d2_010_vif_021_loss_streak_84_021):
    return _base_universe_d3(vif_base_universe_d2_010_vif_021_loss_streak_84_021, 10)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_010_vif_021_loss_streak_84_021'] = {'inputs': ['vif_base_universe_d2_010_vif_021_loss_streak_84_021'], 'func': vif_base_universe_d3_010_vif_021_loss_streak_84_021}


def vif_base_universe_d3_011_vif_022_ma_distance_126_022(vif_base_universe_d2_011_vif_022_ma_distance_126_022):
    return _base_universe_d3(vif_base_universe_d2_011_vif_022_ma_distance_126_022, 11)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_011_vif_022_ma_distance_126_022'] = {'inputs': ['vif_base_universe_d2_011_vif_022_ma_distance_126_022'], 'func': vif_base_universe_d3_011_vif_022_ma_distance_126_022}


def vif_base_universe_d3_012_vif_023_stochastic_position_189_023(vif_base_universe_d2_012_vif_023_stochastic_position_189_023):
    return _base_universe_d3(vif_base_universe_d2_012_vif_023_stochastic_position_189_023, 12)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_012_vif_023_stochastic_position_189_023'] = {'inputs': ['vif_base_universe_d2_012_vif_023_stochastic_position_189_023'], 'func': vif_base_universe_d3_012_vif_023_stochastic_position_189_023}


def vif_base_universe_d3_013_vif_027_loss_streak_756_027(vif_base_universe_d2_013_vif_027_loss_streak_756_027):
    return _base_universe_d3(vif_base_universe_d2_013_vif_027_loss_streak_756_027, 13)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_013_vif_027_loss_streak_756_027'] = {'inputs': ['vif_base_universe_d2_013_vif_027_loss_streak_756_027'], 'func': vif_base_universe_d3_013_vif_027_loss_streak_756_027}


def vif_base_universe_d3_014_vif_028_ma_distance_1008_028(vif_base_universe_d2_014_vif_028_ma_distance_1008_028):
    return _base_universe_d3(vif_base_universe_d2_014_vif_028_ma_distance_1008_028, 14)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_014_vif_028_ma_distance_1008_028'] = {'inputs': ['vif_base_universe_d2_014_vif_028_ma_distance_1008_028'], 'func': vif_base_universe_d3_014_vif_028_ma_distance_1008_028}


def vif_base_universe_d3_015_vif_029_stochastic_position_1260_029(vif_base_universe_d2_015_vif_029_stochastic_position_1260_029):
    return _base_universe_d3(vif_base_universe_d2_015_vif_029_stochastic_position_1260_029, 15)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_015_vif_029_stochastic_position_1260_029'] = {'inputs': ['vif_base_universe_d2_015_vif_029_stochastic_position_1260_029'], 'func': vif_base_universe_d3_015_vif_029_stochastic_position_1260_029}


def vif_base_universe_d3_016_vif_basefill_001(vif_base_universe_d2_016_vif_basefill_001):
    return _base_universe_d3(vif_base_universe_d2_016_vif_basefill_001, 16)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_016_vif_basefill_001'] = {'inputs': ['vif_base_universe_d2_016_vif_basefill_001'], 'func': vif_base_universe_d3_016_vif_basefill_001}


def vif_base_universe_d3_017_vif_basefill_002(vif_base_universe_d2_017_vif_basefill_002):
    return _base_universe_d3(vif_base_universe_d2_017_vif_basefill_002, 17)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_017_vif_basefill_002'] = {'inputs': ['vif_base_universe_d2_017_vif_basefill_002'], 'func': vif_base_universe_d3_017_vif_basefill_002}


def vif_base_universe_d3_018_vif_basefill_006(vif_base_universe_d2_018_vif_basefill_006):
    return _base_universe_d3(vif_base_universe_d2_018_vif_basefill_006, 18)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_018_vif_basefill_006'] = {'inputs': ['vif_base_universe_d2_018_vif_basefill_006'], 'func': vif_base_universe_d3_018_vif_basefill_006}


def vif_base_universe_d3_019_vif_basefill_007(vif_base_universe_d2_019_vif_basefill_007):
    return _base_universe_d3(vif_base_universe_d2_019_vif_basefill_007, 19)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_019_vif_basefill_007'] = {'inputs': ['vif_base_universe_d2_019_vif_basefill_007'], 'func': vif_base_universe_d3_019_vif_basefill_007}


def vif_base_universe_d3_020_vif_basefill_008(vif_base_universe_d2_020_vif_basefill_008):
    return _base_universe_d3(vif_base_universe_d2_020_vif_basefill_008, 20)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_020_vif_basefill_008'] = {'inputs': ['vif_base_universe_d2_020_vif_basefill_008'], 'func': vif_base_universe_d3_020_vif_basefill_008}


def vif_base_universe_d3_021_vif_basefill_012(vif_base_universe_d2_021_vif_basefill_012):
    return _base_universe_d3(vif_base_universe_d2_021_vif_basefill_012, 21)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_021_vif_basefill_012'] = {'inputs': ['vif_base_universe_d2_021_vif_basefill_012'], 'func': vif_base_universe_d3_021_vif_basefill_012}


def vif_base_universe_d3_022_vif_basefill_013(vif_base_universe_d2_022_vif_basefill_013):
    return _base_universe_d3(vif_base_universe_d2_022_vif_basefill_013, 22)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_022_vif_basefill_013'] = {'inputs': ['vif_base_universe_d2_022_vif_basefill_013'], 'func': vif_base_universe_d3_022_vif_basefill_013}


def vif_base_universe_d3_023_vif_basefill_014(vif_base_universe_d2_023_vif_basefill_014):
    return _base_universe_d3(vif_base_universe_d2_023_vif_basefill_014, 23)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_023_vif_basefill_014'] = {'inputs': ['vif_base_universe_d2_023_vif_basefill_014'], 'func': vif_base_universe_d3_023_vif_basefill_014}


def vif_base_universe_d3_024_vif_basefill_018(vif_base_universe_d2_024_vif_basefill_018):
    return _base_universe_d3(vif_base_universe_d2_024_vif_basefill_018, 24)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_024_vif_basefill_018'] = {'inputs': ['vif_base_universe_d2_024_vif_basefill_018'], 'func': vif_base_universe_d3_024_vif_basefill_018}


def vif_base_universe_d3_025_vif_basefill_019(vif_base_universe_d2_025_vif_basefill_019):
    return _base_universe_d3(vif_base_universe_d2_025_vif_basefill_019, 25)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_025_vif_basefill_019'] = {'inputs': ['vif_base_universe_d2_025_vif_basefill_019'], 'func': vif_base_universe_d3_025_vif_basefill_019}


def vif_base_universe_d3_026_vif_basefill_020(vif_base_universe_d2_026_vif_basefill_020):
    return _base_universe_d3(vif_base_universe_d2_026_vif_basefill_020, 26)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_026_vif_basefill_020'] = {'inputs': ['vif_base_universe_d2_026_vif_basefill_020'], 'func': vif_base_universe_d3_026_vif_basefill_020}


def vif_base_universe_d3_027_vif_basefill_024(vif_base_universe_d2_027_vif_basefill_024):
    return _base_universe_d3(vif_base_universe_d2_027_vif_basefill_024, 27)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_027_vif_basefill_024'] = {'inputs': ['vif_base_universe_d2_027_vif_basefill_024'], 'func': vif_base_universe_d3_027_vif_basefill_024}


def vif_base_universe_d3_028_vif_basefill_025(vif_base_universe_d2_028_vif_basefill_025):
    return _base_universe_d3(vif_base_universe_d2_028_vif_basefill_025, 28)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_028_vif_basefill_025'] = {'inputs': ['vif_base_universe_d2_028_vif_basefill_025'], 'func': vif_base_universe_d3_028_vif_basefill_025}


def vif_base_universe_d3_029_vif_basefill_026(vif_base_universe_d2_029_vif_basefill_026):
    return _base_universe_d3(vif_base_universe_d2_029_vif_basefill_026, 29)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_029_vif_basefill_026'] = {'inputs': ['vif_base_universe_d2_029_vif_basefill_026'], 'func': vif_base_universe_d3_029_vif_basefill_026}


def vif_base_universe_d3_030_vif_basefill_030(vif_base_universe_d2_030_vif_basefill_030):
    return _base_universe_d3(vif_base_universe_d2_030_vif_basefill_030, 30)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_030_vif_basefill_030'] = {'inputs': ['vif_base_universe_d2_030_vif_basefill_030'], 'func': vif_base_universe_d3_030_vif_basefill_030}


def vif_base_universe_d3_031_vif_basefill_031(vif_base_universe_d2_031_vif_basefill_031):
    return _base_universe_d3(vif_base_universe_d2_031_vif_basefill_031, 31)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_031_vif_basefill_031'] = {'inputs': ['vif_base_universe_d2_031_vif_basefill_031'], 'func': vif_base_universe_d3_031_vif_basefill_031}


def vif_base_universe_d3_032_vif_basefill_032(vif_base_universe_d2_032_vif_basefill_032):
    return _base_universe_d3(vif_base_universe_d2_032_vif_basefill_032, 32)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_032_vif_basefill_032'] = {'inputs': ['vif_base_universe_d2_032_vif_basefill_032'], 'func': vif_base_universe_d3_032_vif_basefill_032}


def vif_base_universe_d3_033_vif_basefill_033(vif_base_universe_d2_033_vif_basefill_033):
    return _base_universe_d3(vif_base_universe_d2_033_vif_basefill_033, 33)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_033_vif_basefill_033'] = {'inputs': ['vif_base_universe_d2_033_vif_basefill_033'], 'func': vif_base_universe_d3_033_vif_basefill_033}


def vif_base_universe_d3_034_vif_basefill_034(vif_base_universe_d2_034_vif_basefill_034):
    return _base_universe_d3(vif_base_universe_d2_034_vif_basefill_034, 34)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_034_vif_basefill_034'] = {'inputs': ['vif_base_universe_d2_034_vif_basefill_034'], 'func': vif_base_universe_d3_034_vif_basefill_034}


def vif_base_universe_d3_035_vif_basefill_035(vif_base_universe_d2_035_vif_basefill_035):
    return _base_universe_d3(vif_base_universe_d2_035_vif_basefill_035, 35)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_035_vif_basefill_035'] = {'inputs': ['vif_base_universe_d2_035_vif_basefill_035'], 'func': vif_base_universe_d3_035_vif_basefill_035}


def vif_base_universe_d3_036_vif_basefill_036(vif_base_universe_d2_036_vif_basefill_036):
    return _base_universe_d3(vif_base_universe_d2_036_vif_basefill_036, 36)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_036_vif_basefill_036'] = {'inputs': ['vif_base_universe_d2_036_vif_basefill_036'], 'func': vif_base_universe_d3_036_vif_basefill_036}


def vif_base_universe_d3_037_vif_basefill_037(vif_base_universe_d2_037_vif_basefill_037):
    return _base_universe_d3(vif_base_universe_d2_037_vif_basefill_037, 37)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_037_vif_basefill_037'] = {'inputs': ['vif_base_universe_d2_037_vif_basefill_037'], 'func': vif_base_universe_d3_037_vif_basefill_037}


def vif_base_universe_d3_038_vif_basefill_038(vif_base_universe_d2_038_vif_basefill_038):
    return _base_universe_d3(vif_base_universe_d2_038_vif_basefill_038, 38)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_038_vif_basefill_038'] = {'inputs': ['vif_base_universe_d2_038_vif_basefill_038'], 'func': vif_base_universe_d3_038_vif_basefill_038}


def vif_base_universe_d3_039_vif_basefill_039(vif_base_universe_d2_039_vif_basefill_039):
    return _base_universe_d3(vif_base_universe_d2_039_vif_basefill_039, 39)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_039_vif_basefill_039'] = {'inputs': ['vif_base_universe_d2_039_vif_basefill_039'], 'func': vif_base_universe_d3_039_vif_basefill_039}


def vif_base_universe_d3_040_vif_basefill_040(vif_base_universe_d2_040_vif_basefill_040):
    return _base_universe_d3(vif_base_universe_d2_040_vif_basefill_040, 40)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_040_vif_basefill_040'] = {'inputs': ['vif_base_universe_d2_040_vif_basefill_040'], 'func': vif_base_universe_d3_040_vif_basefill_040}


def vif_base_universe_d3_041_vif_basefill_041(vif_base_universe_d2_041_vif_basefill_041):
    return _base_universe_d3(vif_base_universe_d2_041_vif_basefill_041, 41)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_041_vif_basefill_041'] = {'inputs': ['vif_base_universe_d2_041_vif_basefill_041'], 'func': vif_base_universe_d3_041_vif_basefill_041}


def vif_base_universe_d3_042_vif_basefill_042(vif_base_universe_d2_042_vif_basefill_042):
    return _base_universe_d3(vif_base_universe_d2_042_vif_basefill_042, 42)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_042_vif_basefill_042'] = {'inputs': ['vif_base_universe_d2_042_vif_basefill_042'], 'func': vif_base_universe_d3_042_vif_basefill_042}


def vif_base_universe_d3_043_vif_basefill_043(vif_base_universe_d2_043_vif_basefill_043):
    return _base_universe_d3(vif_base_universe_d2_043_vif_basefill_043, 43)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_043_vif_basefill_043'] = {'inputs': ['vif_base_universe_d2_043_vif_basefill_043'], 'func': vif_base_universe_d3_043_vif_basefill_043}


def vif_base_universe_d3_044_vif_basefill_044(vif_base_universe_d2_044_vif_basefill_044):
    return _base_universe_d3(vif_base_universe_d2_044_vif_basefill_044, 44)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_044_vif_basefill_044'] = {'inputs': ['vif_base_universe_d2_044_vif_basefill_044'], 'func': vif_base_universe_d3_044_vif_basefill_044}


def vif_base_universe_d3_045_vif_basefill_045(vif_base_universe_d2_045_vif_basefill_045):
    return _base_universe_d3(vif_base_universe_d2_045_vif_basefill_045, 45)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_045_vif_basefill_045'] = {'inputs': ['vif_base_universe_d2_045_vif_basefill_045'], 'func': vif_base_universe_d3_045_vif_basefill_045}


def vif_base_universe_d3_046_vif_basefill_046(vif_base_universe_d2_046_vif_basefill_046):
    return _base_universe_d3(vif_base_universe_d2_046_vif_basefill_046, 46)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_046_vif_basefill_046'] = {'inputs': ['vif_base_universe_d2_046_vif_basefill_046'], 'func': vif_base_universe_d3_046_vif_basefill_046}


def vif_base_universe_d3_047_vif_basefill_047(vif_base_universe_d2_047_vif_basefill_047):
    return _base_universe_d3(vif_base_universe_d2_047_vif_basefill_047, 47)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_047_vif_basefill_047'] = {'inputs': ['vif_base_universe_d2_047_vif_basefill_047'], 'func': vif_base_universe_d3_047_vif_basefill_047}


def vif_base_universe_d3_048_vif_basefill_048(vif_base_universe_d2_048_vif_basefill_048):
    return _base_universe_d3(vif_base_universe_d2_048_vif_basefill_048, 48)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_048_vif_basefill_048'] = {'inputs': ['vif_base_universe_d2_048_vif_basefill_048'], 'func': vif_base_universe_d3_048_vif_basefill_048}


def vif_base_universe_d3_049_vif_basefill_049(vif_base_universe_d2_049_vif_basefill_049):
    return _base_universe_d3(vif_base_universe_d2_049_vif_basefill_049, 49)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_049_vif_basefill_049'] = {'inputs': ['vif_base_universe_d2_049_vif_basefill_049'], 'func': vif_base_universe_d3_049_vif_basefill_049}


def vif_base_universe_d3_050_vif_basefill_050(vif_base_universe_d2_050_vif_basefill_050):
    return _base_universe_d3(vif_base_universe_d2_050_vif_basefill_050, 50)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_050_vif_basefill_050'] = {'inputs': ['vif_base_universe_d2_050_vif_basefill_050'], 'func': vif_base_universe_d3_050_vif_basefill_050}


def vif_base_universe_d3_051_vif_basefill_051(vif_base_universe_d2_051_vif_basefill_051):
    return _base_universe_d3(vif_base_universe_d2_051_vif_basefill_051, 51)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_051_vif_basefill_051'] = {'inputs': ['vif_base_universe_d2_051_vif_basefill_051'], 'func': vif_base_universe_d3_051_vif_basefill_051}


def vif_base_universe_d3_052_vif_basefill_052(vif_base_universe_d2_052_vif_basefill_052):
    return _base_universe_d3(vif_base_universe_d2_052_vif_basefill_052, 52)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_052_vif_basefill_052'] = {'inputs': ['vif_base_universe_d2_052_vif_basefill_052'], 'func': vif_base_universe_d3_052_vif_basefill_052}


def vif_base_universe_d3_053_vif_basefill_053(vif_base_universe_d2_053_vif_basefill_053):
    return _base_universe_d3(vif_base_universe_d2_053_vif_basefill_053, 53)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_053_vif_basefill_053'] = {'inputs': ['vif_base_universe_d2_053_vif_basefill_053'], 'func': vif_base_universe_d3_053_vif_basefill_053}


def vif_base_universe_d3_054_vif_basefill_054(vif_base_universe_d2_054_vif_basefill_054):
    return _base_universe_d3(vif_base_universe_d2_054_vif_basefill_054, 54)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_054_vif_basefill_054'] = {'inputs': ['vif_base_universe_d2_054_vif_basefill_054'], 'func': vif_base_universe_d3_054_vif_basefill_054}


def vif_base_universe_d3_055_vif_basefill_055(vif_base_universe_d2_055_vif_basefill_055):
    return _base_universe_d3(vif_base_universe_d2_055_vif_basefill_055, 55)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_055_vif_basefill_055'] = {'inputs': ['vif_base_universe_d2_055_vif_basefill_055'], 'func': vif_base_universe_d3_055_vif_basefill_055}


def vif_base_universe_d3_056_vif_basefill_056(vif_base_universe_d2_056_vif_basefill_056):
    return _base_universe_d3(vif_base_universe_d2_056_vif_basefill_056, 56)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_056_vif_basefill_056'] = {'inputs': ['vif_base_universe_d2_056_vif_basefill_056'], 'func': vif_base_universe_d3_056_vif_basefill_056}


def vif_base_universe_d3_057_vif_basefill_057(vif_base_universe_d2_057_vif_basefill_057):
    return _base_universe_d3(vif_base_universe_d2_057_vif_basefill_057, 57)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_057_vif_basefill_057'] = {'inputs': ['vif_base_universe_d2_057_vif_basefill_057'], 'func': vif_base_universe_d3_057_vif_basefill_057}


def vif_base_universe_d3_058_vif_basefill_058(vif_base_universe_d2_058_vif_basefill_058):
    return _base_universe_d3(vif_base_universe_d2_058_vif_basefill_058, 58)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_058_vif_basefill_058'] = {'inputs': ['vif_base_universe_d2_058_vif_basefill_058'], 'func': vif_base_universe_d3_058_vif_basefill_058}


def vif_base_universe_d3_059_vif_basefill_059(vif_base_universe_d2_059_vif_basefill_059):
    return _base_universe_d3(vif_base_universe_d2_059_vif_basefill_059, 59)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_059_vif_basefill_059'] = {'inputs': ['vif_base_universe_d2_059_vif_basefill_059'], 'func': vif_base_universe_d3_059_vif_basefill_059}


def vif_base_universe_d3_060_vif_basefill_060(vif_base_universe_d2_060_vif_basefill_060):
    return _base_universe_d3(vif_base_universe_d2_060_vif_basefill_060, 60)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_060_vif_basefill_060'] = {'inputs': ['vif_base_universe_d2_060_vif_basefill_060'], 'func': vif_base_universe_d3_060_vif_basefill_060}


def vif_base_universe_d3_061_vif_basefill_061(vif_base_universe_d2_061_vif_basefill_061):
    return _base_universe_d3(vif_base_universe_d2_061_vif_basefill_061, 61)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_061_vif_basefill_061'] = {'inputs': ['vif_base_universe_d2_061_vif_basefill_061'], 'func': vif_base_universe_d3_061_vif_basefill_061}


def vif_base_universe_d3_062_vif_basefill_062(vif_base_universe_d2_062_vif_basefill_062):
    return _base_universe_d3(vif_base_universe_d2_062_vif_basefill_062, 62)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_062_vif_basefill_062'] = {'inputs': ['vif_base_universe_d2_062_vif_basefill_062'], 'func': vif_base_universe_d3_062_vif_basefill_062}


def vif_base_universe_d3_063_vif_basefill_063(vif_base_universe_d2_063_vif_basefill_063):
    return _base_universe_d3(vif_base_universe_d2_063_vif_basefill_063, 63)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_063_vif_basefill_063'] = {'inputs': ['vif_base_universe_d2_063_vif_basefill_063'], 'func': vif_base_universe_d3_063_vif_basefill_063}


def vif_base_universe_d3_064_vif_basefill_064(vif_base_universe_d2_064_vif_basefill_064):
    return _base_universe_d3(vif_base_universe_d2_064_vif_basefill_064, 64)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_064_vif_basefill_064'] = {'inputs': ['vif_base_universe_d2_064_vif_basefill_064'], 'func': vif_base_universe_d3_064_vif_basefill_064}


def vif_base_universe_d3_065_vif_basefill_065(vif_base_universe_d2_065_vif_basefill_065):
    return _base_universe_d3(vif_base_universe_d2_065_vif_basefill_065, 65)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_065_vif_basefill_065'] = {'inputs': ['vif_base_universe_d2_065_vif_basefill_065'], 'func': vif_base_universe_d3_065_vif_basefill_065}


def vif_base_universe_d3_066_vif_basefill_066(vif_base_universe_d2_066_vif_basefill_066):
    return _base_universe_d3(vif_base_universe_d2_066_vif_basefill_066, 66)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_066_vif_basefill_066'] = {'inputs': ['vif_base_universe_d2_066_vif_basefill_066'], 'func': vif_base_universe_d3_066_vif_basefill_066}


def vif_base_universe_d3_067_vif_basefill_067(vif_base_universe_d2_067_vif_basefill_067):
    return _base_universe_d3(vif_base_universe_d2_067_vif_basefill_067, 67)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_067_vif_basefill_067'] = {'inputs': ['vif_base_universe_d2_067_vif_basefill_067'], 'func': vif_base_universe_d3_067_vif_basefill_067}


def vif_base_universe_d3_068_vif_basefill_068(vif_base_universe_d2_068_vif_basefill_068):
    return _base_universe_d3(vif_base_universe_d2_068_vif_basefill_068, 68)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_068_vif_basefill_068'] = {'inputs': ['vif_base_universe_d2_068_vif_basefill_068'], 'func': vif_base_universe_d3_068_vif_basefill_068}


def vif_base_universe_d3_069_vif_basefill_069(vif_base_universe_d2_069_vif_basefill_069):
    return _base_universe_d3(vif_base_universe_d2_069_vif_basefill_069, 69)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_069_vif_basefill_069'] = {'inputs': ['vif_base_universe_d2_069_vif_basefill_069'], 'func': vif_base_universe_d3_069_vif_basefill_069}


def vif_base_universe_d3_070_vif_basefill_070(vif_base_universe_d2_070_vif_basefill_070):
    return _base_universe_d3(vif_base_universe_d2_070_vif_basefill_070, 70)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_070_vif_basefill_070'] = {'inputs': ['vif_base_universe_d2_070_vif_basefill_070'], 'func': vif_base_universe_d3_070_vif_basefill_070}


def vif_base_universe_d3_071_vif_basefill_071(vif_base_universe_d2_071_vif_basefill_071):
    return _base_universe_d3(vif_base_universe_d2_071_vif_basefill_071, 71)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_071_vif_basefill_071'] = {'inputs': ['vif_base_universe_d2_071_vif_basefill_071'], 'func': vif_base_universe_d3_071_vif_basefill_071}


def vif_base_universe_d3_072_vif_basefill_072(vif_base_universe_d2_072_vif_basefill_072):
    return _base_universe_d3(vif_base_universe_d2_072_vif_basefill_072, 72)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_072_vif_basefill_072'] = {'inputs': ['vif_base_universe_d2_072_vif_basefill_072'], 'func': vif_base_universe_d3_072_vif_basefill_072}


def vif_base_universe_d3_073_vif_basefill_073(vif_base_universe_d2_073_vif_basefill_073):
    return _base_universe_d3(vif_base_universe_d2_073_vif_basefill_073, 73)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_073_vif_basefill_073'] = {'inputs': ['vif_base_universe_d2_073_vif_basefill_073'], 'func': vif_base_universe_d3_073_vif_basefill_073}


def vif_base_universe_d3_074_vif_basefill_074(vif_base_universe_d2_074_vif_basefill_074):
    return _base_universe_d3(vif_base_universe_d2_074_vif_basefill_074, 74)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_074_vif_basefill_074'] = {'inputs': ['vif_base_universe_d2_074_vif_basefill_074'], 'func': vif_base_universe_d3_074_vif_basefill_074}


def vif_base_universe_d3_075_vif_basefill_075(vif_base_universe_d2_075_vif_basefill_075):
    return _base_universe_d3(vif_base_universe_d2_075_vif_basefill_075, 75)
VIF_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['vif_base_universe_d3_075_vif_basefill_075'] = {'inputs': ['vif_base_universe_d2_075_vif_basefill_075'], 'func': vif_base_universe_d3_075_vif_basefill_075}
