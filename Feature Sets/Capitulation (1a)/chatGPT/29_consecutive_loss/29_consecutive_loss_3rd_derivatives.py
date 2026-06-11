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



def ccl_001_return_decay_accel_1(ccl_001_return_decay_roc_1):
    feature = _s(ccl_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def ccl_007_return_decay_accel_5(ccl_007_return_decay_roc_5):
    feature = _s(ccl_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def ccl_013_return_decay_accel_42(ccl_013_return_decay_roc_42):
    feature = _s(ccl_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def ccl_179_ccl_019_return_decay_42_019_accel_126(ccl_154_ccl_019_return_decay_42_019_roc_126):
    feature = _s(ccl_154_ccl_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def ccl_180_ccl_025_return_decay_5_025_accel_378(ccl_155_ccl_025_return_decay_5_025_roc_378):
    feature = _s(ccl_155_ccl_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















CONSECUTIVE_LOSS_REGISTRY_3RD_DERIVATIVES = {
    'ccl_001_return_decay_accel_1': {'inputs': ['ccl_001_return_decay_roc_1'], 'func': ccl_001_return_decay_accel_1},
    'ccl_007_return_decay_accel_5': {'inputs': ['ccl_007_return_decay_roc_5'], 'func': ccl_007_return_decay_accel_5},
    'ccl_013_return_decay_accel_42': {'inputs': ['ccl_013_return_decay_roc_42'], 'func': ccl_013_return_decay_accel_42},
    'ccl_179_ccl_019_return_decay_42_019_accel_126': {'inputs': ['ccl_154_ccl_019_return_decay_42_019_roc_126'], 'func': ccl_179_ccl_019_return_decay_42_019_accel_126},
    'ccl_180_ccl_025_return_decay_5_025_accel_378': {'inputs': ['ccl_155_ccl_025_return_decay_5_025_roc_378'], 'func': ccl_180_ccl_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def cl_replacement_d3_001(cl_replacement_d2_001):
    feature = _clean(cl_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_001'] = {'inputs': ['cl_replacement_d2_001'], 'func': cl_replacement_d3_001}


def cl_replacement_d3_002(cl_replacement_d2_002):
    feature = _clean(cl_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_002'] = {'inputs': ['cl_replacement_d2_002'], 'func': cl_replacement_d3_002}


def cl_replacement_d3_003(cl_replacement_d2_003):
    feature = _clean(cl_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_003'] = {'inputs': ['cl_replacement_d2_003'], 'func': cl_replacement_d3_003}


def cl_replacement_d3_004(cl_replacement_d2_004):
    feature = _clean(cl_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_004'] = {'inputs': ['cl_replacement_d2_004'], 'func': cl_replacement_d3_004}


def cl_replacement_d3_005(cl_replacement_d2_005):
    feature = _clean(cl_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_005'] = {'inputs': ['cl_replacement_d2_005'], 'func': cl_replacement_d3_005}


def cl_replacement_d3_006(cl_replacement_d2_006):
    feature = _clean(cl_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_006'] = {'inputs': ['cl_replacement_d2_006'], 'func': cl_replacement_d3_006}


def cl_replacement_d3_007(cl_replacement_d2_007):
    feature = _clean(cl_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_007'] = {'inputs': ['cl_replacement_d2_007'], 'func': cl_replacement_d3_007}


def cl_replacement_d3_008(cl_replacement_d2_008):
    feature = _clean(cl_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_008'] = {'inputs': ['cl_replacement_d2_008'], 'func': cl_replacement_d3_008}


def cl_replacement_d3_009(cl_replacement_d2_009):
    feature = _clean(cl_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_009'] = {'inputs': ['cl_replacement_d2_009'], 'func': cl_replacement_d3_009}


def cl_replacement_d3_010(cl_replacement_d2_010):
    feature = _clean(cl_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_010'] = {'inputs': ['cl_replacement_d2_010'], 'func': cl_replacement_d3_010}


def cl_replacement_d3_011(cl_replacement_d2_011):
    feature = _clean(cl_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_011'] = {'inputs': ['cl_replacement_d2_011'], 'func': cl_replacement_d3_011}


def cl_replacement_d3_012(cl_replacement_d2_012):
    feature = _clean(cl_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_012'] = {'inputs': ['cl_replacement_d2_012'], 'func': cl_replacement_d3_012}


def cl_replacement_d3_013(cl_replacement_d2_013):
    feature = _clean(cl_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_013'] = {'inputs': ['cl_replacement_d2_013'], 'func': cl_replacement_d3_013}


def cl_replacement_d3_014(cl_replacement_d2_014):
    feature = _clean(cl_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_014'] = {'inputs': ['cl_replacement_d2_014'], 'func': cl_replacement_d3_014}


def cl_replacement_d3_015(cl_replacement_d2_015):
    feature = _clean(cl_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_015'] = {'inputs': ['cl_replacement_d2_015'], 'func': cl_replacement_d3_015}


def cl_replacement_d3_016(cl_replacement_d2_016):
    feature = _clean(cl_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_016'] = {'inputs': ['cl_replacement_d2_016'], 'func': cl_replacement_d3_016}


def cl_replacement_d3_017(cl_replacement_d2_017):
    feature = _clean(cl_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_017'] = {'inputs': ['cl_replacement_d2_017'], 'func': cl_replacement_d3_017}


def cl_replacement_d3_018(cl_replacement_d2_018):
    feature = _clean(cl_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_018'] = {'inputs': ['cl_replacement_d2_018'], 'func': cl_replacement_d3_018}


def cl_replacement_d3_019(cl_replacement_d2_019):
    feature = _clean(cl_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_019'] = {'inputs': ['cl_replacement_d2_019'], 'func': cl_replacement_d3_019}


def cl_replacement_d3_020(cl_replacement_d2_020):
    feature = _clean(cl_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_020'] = {'inputs': ['cl_replacement_d2_020'], 'func': cl_replacement_d3_020}


def cl_replacement_d3_021(cl_replacement_d2_021):
    feature = _clean(cl_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_021'] = {'inputs': ['cl_replacement_d2_021'], 'func': cl_replacement_d3_021}


def cl_replacement_d3_022(cl_replacement_d2_022):
    feature = _clean(cl_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_022'] = {'inputs': ['cl_replacement_d2_022'], 'func': cl_replacement_d3_022}


def cl_replacement_d3_023(cl_replacement_d2_023):
    feature = _clean(cl_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_023'] = {'inputs': ['cl_replacement_d2_023'], 'func': cl_replacement_d3_023}


def cl_replacement_d3_024(cl_replacement_d2_024):
    feature = _clean(cl_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_024'] = {'inputs': ['cl_replacement_d2_024'], 'func': cl_replacement_d3_024}


def cl_replacement_d3_025(cl_replacement_d2_025):
    feature = _clean(cl_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_025'] = {'inputs': ['cl_replacement_d2_025'], 'func': cl_replacement_d3_025}


def cl_replacement_d3_026(cl_replacement_d2_026):
    feature = _clean(cl_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_026'] = {'inputs': ['cl_replacement_d2_026'], 'func': cl_replacement_d3_026}


def cl_replacement_d3_027(cl_replacement_d2_027):
    feature = _clean(cl_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_027'] = {'inputs': ['cl_replacement_d2_027'], 'func': cl_replacement_d3_027}


def cl_replacement_d3_028(cl_replacement_d2_028):
    feature = _clean(cl_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_028'] = {'inputs': ['cl_replacement_d2_028'], 'func': cl_replacement_d3_028}


def cl_replacement_d3_029(cl_replacement_d2_029):
    feature = _clean(cl_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_029'] = {'inputs': ['cl_replacement_d2_029'], 'func': cl_replacement_d3_029}


def cl_replacement_d3_030(cl_replacement_d2_030):
    feature = _clean(cl_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_030'] = {'inputs': ['cl_replacement_d2_030'], 'func': cl_replacement_d3_030}


def cl_replacement_d3_031(cl_replacement_d2_031):
    feature = _clean(cl_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_031'] = {'inputs': ['cl_replacement_d2_031'], 'func': cl_replacement_d3_031}


def cl_replacement_d3_032(cl_replacement_d2_032):
    feature = _clean(cl_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_032'] = {'inputs': ['cl_replacement_d2_032'], 'func': cl_replacement_d3_032}


def cl_replacement_d3_033(cl_replacement_d2_033):
    feature = _clean(cl_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_033'] = {'inputs': ['cl_replacement_d2_033'], 'func': cl_replacement_d3_033}


def cl_replacement_d3_034(cl_replacement_d2_034):
    feature = _clean(cl_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_034'] = {'inputs': ['cl_replacement_d2_034'], 'func': cl_replacement_d3_034}


def cl_replacement_d3_035(cl_replacement_d2_035):
    feature = _clean(cl_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_035'] = {'inputs': ['cl_replacement_d2_035'], 'func': cl_replacement_d3_035}


def cl_replacement_d3_036(cl_replacement_d2_036):
    feature = _clean(cl_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_036'] = {'inputs': ['cl_replacement_d2_036'], 'func': cl_replacement_d3_036}


def cl_replacement_d3_037(cl_replacement_d2_037):
    feature = _clean(cl_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_037'] = {'inputs': ['cl_replacement_d2_037'], 'func': cl_replacement_d3_037}


def cl_replacement_d3_038(cl_replacement_d2_038):
    feature = _clean(cl_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_038'] = {'inputs': ['cl_replacement_d2_038'], 'func': cl_replacement_d3_038}


def cl_replacement_d3_039(cl_replacement_d2_039):
    feature = _clean(cl_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_039'] = {'inputs': ['cl_replacement_d2_039'], 'func': cl_replacement_d3_039}


def cl_replacement_d3_040(cl_replacement_d2_040):
    feature = _clean(cl_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_040'] = {'inputs': ['cl_replacement_d2_040'], 'func': cl_replacement_d3_040}


def cl_replacement_d3_041(cl_replacement_d2_041):
    feature = _clean(cl_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_041'] = {'inputs': ['cl_replacement_d2_041'], 'func': cl_replacement_d3_041}


def cl_replacement_d3_042(cl_replacement_d2_042):
    feature = _clean(cl_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_042'] = {'inputs': ['cl_replacement_d2_042'], 'func': cl_replacement_d3_042}


def cl_replacement_d3_043(cl_replacement_d2_043):
    feature = _clean(cl_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_043'] = {'inputs': ['cl_replacement_d2_043'], 'func': cl_replacement_d3_043}


def cl_replacement_d3_044(cl_replacement_d2_044):
    feature = _clean(cl_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_044'] = {'inputs': ['cl_replacement_d2_044'], 'func': cl_replacement_d3_044}


def cl_replacement_d3_045(cl_replacement_d2_045):
    feature = _clean(cl_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_045'] = {'inputs': ['cl_replacement_d2_045'], 'func': cl_replacement_d3_045}


def cl_replacement_d3_046(cl_replacement_d2_046):
    feature = _clean(cl_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_046'] = {'inputs': ['cl_replacement_d2_046'], 'func': cl_replacement_d3_046}


def cl_replacement_d3_047(cl_replacement_d2_047):
    feature = _clean(cl_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_047'] = {'inputs': ['cl_replacement_d2_047'], 'func': cl_replacement_d3_047}


def cl_replacement_d3_048(cl_replacement_d2_048):
    feature = _clean(cl_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_048'] = {'inputs': ['cl_replacement_d2_048'], 'func': cl_replacement_d3_048}


def cl_replacement_d3_049(cl_replacement_d2_049):
    feature = _clean(cl_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_049'] = {'inputs': ['cl_replacement_d2_049'], 'func': cl_replacement_d3_049}


def cl_replacement_d3_050(cl_replacement_d2_050):
    feature = _clean(cl_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_050'] = {'inputs': ['cl_replacement_d2_050'], 'func': cl_replacement_d3_050}


def cl_replacement_d3_051(cl_replacement_d2_051):
    feature = _clean(cl_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_051'] = {'inputs': ['cl_replacement_d2_051'], 'func': cl_replacement_d3_051}


def cl_replacement_d3_052(cl_replacement_d2_052):
    feature = _clean(cl_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_052'] = {'inputs': ['cl_replacement_d2_052'], 'func': cl_replacement_d3_052}


def cl_replacement_d3_053(cl_replacement_d2_053):
    feature = _clean(cl_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_053'] = {'inputs': ['cl_replacement_d2_053'], 'func': cl_replacement_d3_053}


def cl_replacement_d3_054(cl_replacement_d2_054):
    feature = _clean(cl_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_054'] = {'inputs': ['cl_replacement_d2_054'], 'func': cl_replacement_d3_054}


def cl_replacement_d3_055(cl_replacement_d2_055):
    feature = _clean(cl_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_055'] = {'inputs': ['cl_replacement_d2_055'], 'func': cl_replacement_d3_055}


def cl_replacement_d3_056(cl_replacement_d2_056):
    feature = _clean(cl_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_056'] = {'inputs': ['cl_replacement_d2_056'], 'func': cl_replacement_d3_056}


def cl_replacement_d3_057(cl_replacement_d2_057):
    feature = _clean(cl_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_057'] = {'inputs': ['cl_replacement_d2_057'], 'func': cl_replacement_d3_057}


def cl_replacement_d3_058(cl_replacement_d2_058):
    feature = _clean(cl_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_058'] = {'inputs': ['cl_replacement_d2_058'], 'func': cl_replacement_d3_058}


def cl_replacement_d3_059(cl_replacement_d2_059):
    feature = _clean(cl_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_059'] = {'inputs': ['cl_replacement_d2_059'], 'func': cl_replacement_d3_059}


def cl_replacement_d3_060(cl_replacement_d2_060):
    feature = _clean(cl_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_060'] = {'inputs': ['cl_replacement_d2_060'], 'func': cl_replacement_d3_060}


def cl_replacement_d3_061(cl_replacement_d2_061):
    feature = _clean(cl_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_061'] = {'inputs': ['cl_replacement_d2_061'], 'func': cl_replacement_d3_061}


def cl_replacement_d3_062(cl_replacement_d2_062):
    feature = _clean(cl_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_062'] = {'inputs': ['cl_replacement_d2_062'], 'func': cl_replacement_d3_062}


def cl_replacement_d3_063(cl_replacement_d2_063):
    feature = _clean(cl_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_063'] = {'inputs': ['cl_replacement_d2_063'], 'func': cl_replacement_d3_063}


def cl_replacement_d3_064(cl_replacement_d2_064):
    feature = _clean(cl_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_064'] = {'inputs': ['cl_replacement_d2_064'], 'func': cl_replacement_d3_064}


def cl_replacement_d3_065(cl_replacement_d2_065):
    feature = _clean(cl_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_065'] = {'inputs': ['cl_replacement_d2_065'], 'func': cl_replacement_d3_065}


def cl_replacement_d3_066(cl_replacement_d2_066):
    feature = _clean(cl_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_066'] = {'inputs': ['cl_replacement_d2_066'], 'func': cl_replacement_d3_066}


def cl_replacement_d3_067(cl_replacement_d2_067):
    feature = _clean(cl_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_067'] = {'inputs': ['cl_replacement_d2_067'], 'func': cl_replacement_d3_067}


def cl_replacement_d3_068(cl_replacement_d2_068):
    feature = _clean(cl_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_068'] = {'inputs': ['cl_replacement_d2_068'], 'func': cl_replacement_d3_068}


def cl_replacement_d3_069(cl_replacement_d2_069):
    feature = _clean(cl_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_069'] = {'inputs': ['cl_replacement_d2_069'], 'func': cl_replacement_d3_069}


def cl_replacement_d3_070(cl_replacement_d2_070):
    feature = _clean(cl_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_070'] = {'inputs': ['cl_replacement_d2_070'], 'func': cl_replacement_d3_070}


def cl_replacement_d3_071(cl_replacement_d2_071):
    feature = _clean(cl_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_071'] = {'inputs': ['cl_replacement_d2_071'], 'func': cl_replacement_d3_071}


def cl_replacement_d3_072(cl_replacement_d2_072):
    feature = _clean(cl_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_072'] = {'inputs': ['cl_replacement_d2_072'], 'func': cl_replacement_d3_072}


def cl_replacement_d3_073(cl_replacement_d2_073):
    feature = _clean(cl_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_073'] = {'inputs': ['cl_replacement_d2_073'], 'func': cl_replacement_d3_073}


def cl_replacement_d3_074(cl_replacement_d2_074):
    feature = _clean(cl_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_074'] = {'inputs': ['cl_replacement_d2_074'], 'func': cl_replacement_d3_074}


def cl_replacement_d3_075(cl_replacement_d2_075):
    feature = _clean(cl_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_075'] = {'inputs': ['cl_replacement_d2_075'], 'func': cl_replacement_d3_075}


def cl_replacement_d3_076(cl_replacement_d2_076):
    feature = _clean(cl_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_076'] = {'inputs': ['cl_replacement_d2_076'], 'func': cl_replacement_d3_076}


def cl_replacement_d3_077(cl_replacement_d2_077):
    feature = _clean(cl_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_077'] = {'inputs': ['cl_replacement_d2_077'], 'func': cl_replacement_d3_077}


def cl_replacement_d3_078(cl_replacement_d2_078):
    feature = _clean(cl_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_078'] = {'inputs': ['cl_replacement_d2_078'], 'func': cl_replacement_d3_078}


def cl_replacement_d3_079(cl_replacement_d2_079):
    feature = _clean(cl_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_079'] = {'inputs': ['cl_replacement_d2_079'], 'func': cl_replacement_d3_079}


def cl_replacement_d3_080(cl_replacement_d2_080):
    feature = _clean(cl_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_080'] = {'inputs': ['cl_replacement_d2_080'], 'func': cl_replacement_d3_080}


def cl_replacement_d3_081(cl_replacement_d2_081):
    feature = _clean(cl_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_081'] = {'inputs': ['cl_replacement_d2_081'], 'func': cl_replacement_d3_081}


def cl_replacement_d3_082(cl_replacement_d2_082):
    feature = _clean(cl_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_082'] = {'inputs': ['cl_replacement_d2_082'], 'func': cl_replacement_d3_082}


def cl_replacement_d3_083(cl_replacement_d2_083):
    feature = _clean(cl_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_083'] = {'inputs': ['cl_replacement_d2_083'], 'func': cl_replacement_d3_083}


def cl_replacement_d3_084(cl_replacement_d2_084):
    feature = _clean(cl_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_084'] = {'inputs': ['cl_replacement_d2_084'], 'func': cl_replacement_d3_084}


def cl_replacement_d3_085(cl_replacement_d2_085):
    feature = _clean(cl_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_085'] = {'inputs': ['cl_replacement_d2_085'], 'func': cl_replacement_d3_085}


def cl_replacement_d3_086(cl_replacement_d2_086):
    feature = _clean(cl_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_086'] = {'inputs': ['cl_replacement_d2_086'], 'func': cl_replacement_d3_086}


def cl_replacement_d3_087(cl_replacement_d2_087):
    feature = _clean(cl_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_087'] = {'inputs': ['cl_replacement_d2_087'], 'func': cl_replacement_d3_087}


def cl_replacement_d3_088(cl_replacement_d2_088):
    feature = _clean(cl_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_088'] = {'inputs': ['cl_replacement_d2_088'], 'func': cl_replacement_d3_088}


def cl_replacement_d3_089(cl_replacement_d2_089):
    feature = _clean(cl_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_089'] = {'inputs': ['cl_replacement_d2_089'], 'func': cl_replacement_d3_089}


def cl_replacement_d3_090(cl_replacement_d2_090):
    feature = _clean(cl_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_090'] = {'inputs': ['cl_replacement_d2_090'], 'func': cl_replacement_d3_090}


def cl_replacement_d3_091(cl_replacement_d2_091):
    feature = _clean(cl_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_091'] = {'inputs': ['cl_replacement_d2_091'], 'func': cl_replacement_d3_091}


def cl_replacement_d3_092(cl_replacement_d2_092):
    feature = _clean(cl_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_092'] = {'inputs': ['cl_replacement_d2_092'], 'func': cl_replacement_d3_092}


def cl_replacement_d3_093(cl_replacement_d2_093):
    feature = _clean(cl_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_093'] = {'inputs': ['cl_replacement_d2_093'], 'func': cl_replacement_d3_093}


def cl_replacement_d3_094(cl_replacement_d2_094):
    feature = _clean(cl_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_094'] = {'inputs': ['cl_replacement_d2_094'], 'func': cl_replacement_d3_094}


def cl_replacement_d3_095(cl_replacement_d2_095):
    feature = _clean(cl_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_095'] = {'inputs': ['cl_replacement_d2_095'], 'func': cl_replacement_d3_095}


def cl_replacement_d3_096(cl_replacement_d2_096):
    feature = _clean(cl_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_096'] = {'inputs': ['cl_replacement_d2_096'], 'func': cl_replacement_d3_096}


def cl_replacement_d3_097(cl_replacement_d2_097):
    feature = _clean(cl_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_097'] = {'inputs': ['cl_replacement_d2_097'], 'func': cl_replacement_d3_097}


def cl_replacement_d3_098(cl_replacement_d2_098):
    feature = _clean(cl_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_098'] = {'inputs': ['cl_replacement_d2_098'], 'func': cl_replacement_d3_098}


def cl_replacement_d3_099(cl_replacement_d2_099):
    feature = _clean(cl_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_099'] = {'inputs': ['cl_replacement_d2_099'], 'func': cl_replacement_d3_099}


def cl_replacement_d3_100(cl_replacement_d2_100):
    feature = _clean(cl_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_100'] = {'inputs': ['cl_replacement_d2_100'], 'func': cl_replacement_d3_100}


def cl_replacement_d3_101(cl_replacement_d2_101):
    feature = _clean(cl_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_101'] = {'inputs': ['cl_replacement_d2_101'], 'func': cl_replacement_d3_101}


def cl_replacement_d3_102(cl_replacement_d2_102):
    feature = _clean(cl_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_102'] = {'inputs': ['cl_replacement_d2_102'], 'func': cl_replacement_d3_102}


def cl_replacement_d3_103(cl_replacement_d2_103):
    feature = _clean(cl_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_103'] = {'inputs': ['cl_replacement_d2_103'], 'func': cl_replacement_d3_103}


def cl_replacement_d3_104(cl_replacement_d2_104):
    feature = _clean(cl_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_104'] = {'inputs': ['cl_replacement_d2_104'], 'func': cl_replacement_d3_104}


def cl_replacement_d3_105(cl_replacement_d2_105):
    feature = _clean(cl_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_105'] = {'inputs': ['cl_replacement_d2_105'], 'func': cl_replacement_d3_105}


def cl_replacement_d3_106(cl_replacement_d2_106):
    feature = _clean(cl_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_106'] = {'inputs': ['cl_replacement_d2_106'], 'func': cl_replacement_d3_106}


def cl_replacement_d3_107(cl_replacement_d2_107):
    feature = _clean(cl_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_107'] = {'inputs': ['cl_replacement_d2_107'], 'func': cl_replacement_d3_107}


def cl_replacement_d3_108(cl_replacement_d2_108):
    feature = _clean(cl_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_108'] = {'inputs': ['cl_replacement_d2_108'], 'func': cl_replacement_d3_108}


def cl_replacement_d3_109(cl_replacement_d2_109):
    feature = _clean(cl_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_109'] = {'inputs': ['cl_replacement_d2_109'], 'func': cl_replacement_d3_109}


def cl_replacement_d3_110(cl_replacement_d2_110):
    feature = _clean(cl_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_110'] = {'inputs': ['cl_replacement_d2_110'], 'func': cl_replacement_d3_110}


def cl_replacement_d3_111(cl_replacement_d2_111):
    feature = _clean(cl_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_111'] = {'inputs': ['cl_replacement_d2_111'], 'func': cl_replacement_d3_111}


def cl_replacement_d3_112(cl_replacement_d2_112):
    feature = _clean(cl_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_112'] = {'inputs': ['cl_replacement_d2_112'], 'func': cl_replacement_d3_112}


def cl_replacement_d3_113(cl_replacement_d2_113):
    feature = _clean(cl_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_113'] = {'inputs': ['cl_replacement_d2_113'], 'func': cl_replacement_d3_113}


def cl_replacement_d3_114(cl_replacement_d2_114):
    feature = _clean(cl_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_114'] = {'inputs': ['cl_replacement_d2_114'], 'func': cl_replacement_d3_114}


def cl_replacement_d3_115(cl_replacement_d2_115):
    feature = _clean(cl_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_115'] = {'inputs': ['cl_replacement_d2_115'], 'func': cl_replacement_d3_115}


def cl_replacement_d3_116(cl_replacement_d2_116):
    feature = _clean(cl_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_116'] = {'inputs': ['cl_replacement_d2_116'], 'func': cl_replacement_d3_116}


def cl_replacement_d3_117(cl_replacement_d2_117):
    feature = _clean(cl_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_117'] = {'inputs': ['cl_replacement_d2_117'], 'func': cl_replacement_d3_117}


def cl_replacement_d3_118(cl_replacement_d2_118):
    feature = _clean(cl_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_118'] = {'inputs': ['cl_replacement_d2_118'], 'func': cl_replacement_d3_118}


def cl_replacement_d3_119(cl_replacement_d2_119):
    feature = _clean(cl_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_119'] = {'inputs': ['cl_replacement_d2_119'], 'func': cl_replacement_d3_119}


def cl_replacement_d3_120(cl_replacement_d2_120):
    feature = _clean(cl_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_120'] = {'inputs': ['cl_replacement_d2_120'], 'func': cl_replacement_d3_120}


def cl_replacement_d3_121(cl_replacement_d2_121):
    feature = _clean(cl_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_121'] = {'inputs': ['cl_replacement_d2_121'], 'func': cl_replacement_d3_121}


def cl_replacement_d3_122(cl_replacement_d2_122):
    feature = _clean(cl_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_122'] = {'inputs': ['cl_replacement_d2_122'], 'func': cl_replacement_d3_122}


def cl_replacement_d3_123(cl_replacement_d2_123):
    feature = _clean(cl_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_123'] = {'inputs': ['cl_replacement_d2_123'], 'func': cl_replacement_d3_123}


def cl_replacement_d3_124(cl_replacement_d2_124):
    feature = _clean(cl_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_124'] = {'inputs': ['cl_replacement_d2_124'], 'func': cl_replacement_d3_124}


def cl_replacement_d3_125(cl_replacement_d2_125):
    feature = _clean(cl_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_125'] = {'inputs': ['cl_replacement_d2_125'], 'func': cl_replacement_d3_125}


def cl_replacement_d3_126(cl_replacement_d2_126):
    feature = _clean(cl_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_126'] = {'inputs': ['cl_replacement_d2_126'], 'func': cl_replacement_d3_126}


def cl_replacement_d3_127(cl_replacement_d2_127):
    feature = _clean(cl_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_127'] = {'inputs': ['cl_replacement_d2_127'], 'func': cl_replacement_d3_127}


def cl_replacement_d3_128(cl_replacement_d2_128):
    feature = _clean(cl_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_128'] = {'inputs': ['cl_replacement_d2_128'], 'func': cl_replacement_d3_128}


def cl_replacement_d3_129(cl_replacement_d2_129):
    feature = _clean(cl_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_129'] = {'inputs': ['cl_replacement_d2_129'], 'func': cl_replacement_d3_129}


def cl_replacement_d3_130(cl_replacement_d2_130):
    feature = _clean(cl_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_130'] = {'inputs': ['cl_replacement_d2_130'], 'func': cl_replacement_d3_130}


def cl_replacement_d3_131(cl_replacement_d2_131):
    feature = _clean(cl_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_131'] = {'inputs': ['cl_replacement_d2_131'], 'func': cl_replacement_d3_131}


def cl_replacement_d3_132(cl_replacement_d2_132):
    feature = _clean(cl_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_132'] = {'inputs': ['cl_replacement_d2_132'], 'func': cl_replacement_d3_132}


def cl_replacement_d3_133(cl_replacement_d2_133):
    feature = _clean(cl_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_133'] = {'inputs': ['cl_replacement_d2_133'], 'func': cl_replacement_d3_133}


def cl_replacement_d3_134(cl_replacement_d2_134):
    feature = _clean(cl_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_134'] = {'inputs': ['cl_replacement_d2_134'], 'func': cl_replacement_d3_134}


def cl_replacement_d3_135(cl_replacement_d2_135):
    feature = _clean(cl_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_135'] = {'inputs': ['cl_replacement_d2_135'], 'func': cl_replacement_d3_135}


def cl_replacement_d3_136(cl_replacement_d2_136):
    feature = _clean(cl_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_136'] = {'inputs': ['cl_replacement_d2_136'], 'func': cl_replacement_d3_136}


def cl_replacement_d3_137(cl_replacement_d2_137):
    feature = _clean(cl_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_137'] = {'inputs': ['cl_replacement_d2_137'], 'func': cl_replacement_d3_137}


def cl_replacement_d3_138(cl_replacement_d2_138):
    feature = _clean(cl_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_138'] = {'inputs': ['cl_replacement_d2_138'], 'func': cl_replacement_d3_138}


def cl_replacement_d3_139(cl_replacement_d2_139):
    feature = _clean(cl_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_139'] = {'inputs': ['cl_replacement_d2_139'], 'func': cl_replacement_d3_139}


def cl_replacement_d3_140(cl_replacement_d2_140):
    feature = _clean(cl_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_140'] = {'inputs': ['cl_replacement_d2_140'], 'func': cl_replacement_d3_140}


def cl_replacement_d3_141(cl_replacement_d2_141):
    feature = _clean(cl_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_141'] = {'inputs': ['cl_replacement_d2_141'], 'func': cl_replacement_d3_141}


def cl_replacement_d3_142(cl_replacement_d2_142):
    feature = _clean(cl_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_142'] = {'inputs': ['cl_replacement_d2_142'], 'func': cl_replacement_d3_142}


def cl_replacement_d3_143(cl_replacement_d2_143):
    feature = _clean(cl_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_143'] = {'inputs': ['cl_replacement_d2_143'], 'func': cl_replacement_d3_143}


def cl_replacement_d3_144(cl_replacement_d2_144):
    feature = _clean(cl_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_144'] = {'inputs': ['cl_replacement_d2_144'], 'func': cl_replacement_d3_144}


def cl_replacement_d3_145(cl_replacement_d2_145):
    feature = _clean(cl_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_145'] = {'inputs': ['cl_replacement_d2_145'], 'func': cl_replacement_d3_145}


def cl_replacement_d3_146(cl_replacement_d2_146):
    feature = _clean(cl_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_146'] = {'inputs': ['cl_replacement_d2_146'], 'func': cl_replacement_d3_146}


def cl_replacement_d3_147(cl_replacement_d2_147):
    feature = _clean(cl_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_147'] = {'inputs': ['cl_replacement_d2_147'], 'func': cl_replacement_d3_147}


def cl_replacement_d3_148(cl_replacement_d2_148):
    feature = _clean(cl_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_148'] = {'inputs': ['cl_replacement_d2_148'], 'func': cl_replacement_d3_148}


def cl_replacement_d3_149(cl_replacement_d2_149):
    feature = _clean(cl_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_149'] = {'inputs': ['cl_replacement_d2_149'], 'func': cl_replacement_d3_149}


def cl_replacement_d3_150(cl_replacement_d2_150):
    feature = _clean(cl_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_150'] = {'inputs': ['cl_replacement_d2_150'], 'func': cl_replacement_d3_150}


def cl_replacement_d3_151(cl_replacement_d2_151):
    feature = _clean(cl_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_151'] = {'inputs': ['cl_replacement_d2_151'], 'func': cl_replacement_d3_151}


def cl_replacement_d3_152(cl_replacement_d2_152):
    feature = _clean(cl_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_152'] = {'inputs': ['cl_replacement_d2_152'], 'func': cl_replacement_d3_152}


def cl_replacement_d3_153(cl_replacement_d2_153):
    feature = _clean(cl_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_153'] = {'inputs': ['cl_replacement_d2_153'], 'func': cl_replacement_d3_153}


def cl_replacement_d3_154(cl_replacement_d2_154):
    feature = _clean(cl_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_154'] = {'inputs': ['cl_replacement_d2_154'], 'func': cl_replacement_d3_154}


def cl_replacement_d3_155(cl_replacement_d2_155):
    feature = _clean(cl_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_155'] = {'inputs': ['cl_replacement_d2_155'], 'func': cl_replacement_d3_155}


def cl_replacement_d3_156(cl_replacement_d2_156):
    feature = _clean(cl_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_156'] = {'inputs': ['cl_replacement_d2_156'], 'func': cl_replacement_d3_156}


def cl_replacement_d3_157(cl_replacement_d2_157):
    feature = _clean(cl_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_157'] = {'inputs': ['cl_replacement_d2_157'], 'func': cl_replacement_d3_157}


def cl_replacement_d3_158(cl_replacement_d2_158):
    feature = _clean(cl_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_158'] = {'inputs': ['cl_replacement_d2_158'], 'func': cl_replacement_d3_158}


def cl_replacement_d3_159(cl_replacement_d2_159):
    feature = _clean(cl_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_159'] = {'inputs': ['cl_replacement_d2_159'], 'func': cl_replacement_d3_159}


def cl_replacement_d3_160(cl_replacement_d2_160):
    feature = _clean(cl_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_160'] = {'inputs': ['cl_replacement_d2_160'], 'func': cl_replacement_d3_160}


def cl_replacement_d3_161(cl_replacement_d2_161):
    feature = _clean(cl_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_161'] = {'inputs': ['cl_replacement_d2_161'], 'func': cl_replacement_d3_161}


def cl_replacement_d3_162(cl_replacement_d2_162):
    feature = _clean(cl_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_162'] = {'inputs': ['cl_replacement_d2_162'], 'func': cl_replacement_d3_162}


def cl_replacement_d3_163(cl_replacement_d2_163):
    feature = _clean(cl_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_163'] = {'inputs': ['cl_replacement_d2_163'], 'func': cl_replacement_d3_163}


def cl_replacement_d3_164(cl_replacement_d2_164):
    feature = _clean(cl_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_164'] = {'inputs': ['cl_replacement_d2_164'], 'func': cl_replacement_d3_164}


def cl_replacement_d3_165(cl_replacement_d2_165):
    feature = _clean(cl_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_165'] = {'inputs': ['cl_replacement_d2_165'], 'func': cl_replacement_d3_165}


def cl_replacement_d3_166(cl_replacement_d2_166):
    feature = _clean(cl_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_166'] = {'inputs': ['cl_replacement_d2_166'], 'func': cl_replacement_d3_166}


def cl_replacement_d3_167(cl_replacement_d2_167):
    feature = _clean(cl_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_167'] = {'inputs': ['cl_replacement_d2_167'], 'func': cl_replacement_d3_167}


def cl_replacement_d3_168(cl_replacement_d2_168):
    feature = _clean(cl_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_168'] = {'inputs': ['cl_replacement_d2_168'], 'func': cl_replacement_d3_168}


def cl_replacement_d3_169(cl_replacement_d2_169):
    feature = _clean(cl_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_169'] = {'inputs': ['cl_replacement_d2_169'], 'func': cl_replacement_d3_169}


def cl_replacement_d3_170(cl_replacement_d2_170):
    feature = _clean(cl_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_170'] = {'inputs': ['cl_replacement_d2_170'], 'func': cl_replacement_d3_170}


def cl_replacement_d3_171(cl_replacement_d2_171):
    feature = _clean(cl_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_171'] = {'inputs': ['cl_replacement_d2_171'], 'func': cl_replacement_d3_171}


def cl_replacement_d3_172(cl_replacement_d2_172):
    feature = _clean(cl_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_172'] = {'inputs': ['cl_replacement_d2_172'], 'func': cl_replacement_d3_172}


def cl_replacement_d3_173(cl_replacement_d2_173):
    feature = _clean(cl_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_173'] = {'inputs': ['cl_replacement_d2_173'], 'func': cl_replacement_d3_173}


def cl_replacement_d3_174(cl_replacement_d2_174):
    feature = _clean(cl_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_174'] = {'inputs': ['cl_replacement_d2_174'], 'func': cl_replacement_d3_174}


def cl_replacement_d3_175(cl_replacement_d2_175):
    feature = _clean(cl_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
CL_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['cl_replacement_d3_175'] = {'inputs': ['cl_replacement_d2_175'], 'func': cl_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def ccl_base_universe_d3_001_ccl_003_loss_streak_21_003(ccl_base_universe_d2_001_ccl_003_loss_streak_21_003):
    return _base_universe_d3(ccl_base_universe_d2_001_ccl_003_loss_streak_21_003, 1)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_001_ccl_003_loss_streak_21_003'] = {'inputs': ['ccl_base_universe_d2_001_ccl_003_loss_streak_21_003'], 'func': ccl_base_universe_d3_001_ccl_003_loss_streak_21_003}


def ccl_base_universe_d3_002_ccl_004_ma_distance_42_004(ccl_base_universe_d2_002_ccl_004_ma_distance_42_004):
    return _base_universe_d3(ccl_base_universe_d2_002_ccl_004_ma_distance_42_004, 2)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_002_ccl_004_ma_distance_42_004'] = {'inputs': ['ccl_base_universe_d2_002_ccl_004_ma_distance_42_004'], 'func': ccl_base_universe_d3_002_ccl_004_ma_distance_42_004}


def ccl_base_universe_d3_003_ccl_005_stochastic_position_63_005(ccl_base_universe_d2_003_ccl_005_stochastic_position_63_005):
    return _base_universe_d3(ccl_base_universe_d2_003_ccl_005_stochastic_position_63_005, 3)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_003_ccl_005_stochastic_position_63_005'] = {'inputs': ['ccl_base_universe_d2_003_ccl_005_stochastic_position_63_005'], 'func': ccl_base_universe_d3_003_ccl_005_stochastic_position_63_005}


def ccl_base_universe_d3_004_ccl_009_loss_streak_252_009(ccl_base_universe_d2_004_ccl_009_loss_streak_252_009):
    return _base_universe_d3(ccl_base_universe_d2_004_ccl_009_loss_streak_252_009, 4)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_004_ccl_009_loss_streak_252_009'] = {'inputs': ['ccl_base_universe_d2_004_ccl_009_loss_streak_252_009'], 'func': ccl_base_universe_d3_004_ccl_009_loss_streak_252_009}


def ccl_base_universe_d3_005_ccl_010_ma_distance_378_010(ccl_base_universe_d2_005_ccl_010_ma_distance_378_010):
    return _base_universe_d3(ccl_base_universe_d2_005_ccl_010_ma_distance_378_010, 5)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_005_ccl_010_ma_distance_378_010'] = {'inputs': ['ccl_base_universe_d2_005_ccl_010_ma_distance_378_010'], 'func': ccl_base_universe_d3_005_ccl_010_ma_distance_378_010}


def ccl_base_universe_d3_006_ccl_011_stochastic_position_504_011(ccl_base_universe_d2_006_ccl_011_stochastic_position_504_011):
    return _base_universe_d3(ccl_base_universe_d2_006_ccl_011_stochastic_position_504_011, 6)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_006_ccl_011_stochastic_position_504_011'] = {'inputs': ['ccl_base_universe_d2_006_ccl_011_stochastic_position_504_011'], 'func': ccl_base_universe_d3_006_ccl_011_stochastic_position_504_011}


def ccl_base_universe_d3_007_ccl_015_loss_streak_1512_015(ccl_base_universe_d2_007_ccl_015_loss_streak_1512_015):
    return _base_universe_d3(ccl_base_universe_d2_007_ccl_015_loss_streak_1512_015, 7)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_007_ccl_015_loss_streak_1512_015'] = {'inputs': ['ccl_base_universe_d2_007_ccl_015_loss_streak_1512_015'], 'func': ccl_base_universe_d3_007_ccl_015_loss_streak_1512_015}


def ccl_base_universe_d3_008_ccl_016_ma_distance_5_016(ccl_base_universe_d2_008_ccl_016_ma_distance_5_016):
    return _base_universe_d3(ccl_base_universe_d2_008_ccl_016_ma_distance_5_016, 8)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_008_ccl_016_ma_distance_5_016'] = {'inputs': ['ccl_base_universe_d2_008_ccl_016_ma_distance_5_016'], 'func': ccl_base_universe_d3_008_ccl_016_ma_distance_5_016}


def ccl_base_universe_d3_009_ccl_017_stochastic_position_10_017(ccl_base_universe_d2_009_ccl_017_stochastic_position_10_017):
    return _base_universe_d3(ccl_base_universe_d2_009_ccl_017_stochastic_position_10_017, 9)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_009_ccl_017_stochastic_position_10_017'] = {'inputs': ['ccl_base_universe_d2_009_ccl_017_stochastic_position_10_017'], 'func': ccl_base_universe_d3_009_ccl_017_stochastic_position_10_017}


def ccl_base_universe_d3_010_ccl_021_loss_streak_84_021(ccl_base_universe_d2_010_ccl_021_loss_streak_84_021):
    return _base_universe_d3(ccl_base_universe_d2_010_ccl_021_loss_streak_84_021, 10)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_010_ccl_021_loss_streak_84_021'] = {'inputs': ['ccl_base_universe_d2_010_ccl_021_loss_streak_84_021'], 'func': ccl_base_universe_d3_010_ccl_021_loss_streak_84_021}


def ccl_base_universe_d3_011_ccl_022_ma_distance_126_022(ccl_base_universe_d2_011_ccl_022_ma_distance_126_022):
    return _base_universe_d3(ccl_base_universe_d2_011_ccl_022_ma_distance_126_022, 11)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_011_ccl_022_ma_distance_126_022'] = {'inputs': ['ccl_base_universe_d2_011_ccl_022_ma_distance_126_022'], 'func': ccl_base_universe_d3_011_ccl_022_ma_distance_126_022}


def ccl_base_universe_d3_012_ccl_023_stochastic_position_189_023(ccl_base_universe_d2_012_ccl_023_stochastic_position_189_023):
    return _base_universe_d3(ccl_base_universe_d2_012_ccl_023_stochastic_position_189_023, 12)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_012_ccl_023_stochastic_position_189_023'] = {'inputs': ['ccl_base_universe_d2_012_ccl_023_stochastic_position_189_023'], 'func': ccl_base_universe_d3_012_ccl_023_stochastic_position_189_023}


def ccl_base_universe_d3_013_ccl_027_loss_streak_756_027(ccl_base_universe_d2_013_ccl_027_loss_streak_756_027):
    return _base_universe_d3(ccl_base_universe_d2_013_ccl_027_loss_streak_756_027, 13)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_013_ccl_027_loss_streak_756_027'] = {'inputs': ['ccl_base_universe_d2_013_ccl_027_loss_streak_756_027'], 'func': ccl_base_universe_d3_013_ccl_027_loss_streak_756_027}


def ccl_base_universe_d3_014_ccl_028_ma_distance_1008_028(ccl_base_universe_d2_014_ccl_028_ma_distance_1008_028):
    return _base_universe_d3(ccl_base_universe_d2_014_ccl_028_ma_distance_1008_028, 14)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_014_ccl_028_ma_distance_1008_028'] = {'inputs': ['ccl_base_universe_d2_014_ccl_028_ma_distance_1008_028'], 'func': ccl_base_universe_d3_014_ccl_028_ma_distance_1008_028}


def ccl_base_universe_d3_015_ccl_029_stochastic_position_1260_029(ccl_base_universe_d2_015_ccl_029_stochastic_position_1260_029):
    return _base_universe_d3(ccl_base_universe_d2_015_ccl_029_stochastic_position_1260_029, 15)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_015_ccl_029_stochastic_position_1260_029'] = {'inputs': ['ccl_base_universe_d2_015_ccl_029_stochastic_position_1260_029'], 'func': ccl_base_universe_d3_015_ccl_029_stochastic_position_1260_029}


def ccl_base_universe_d3_016_ccl_basefill_001(ccl_base_universe_d2_016_ccl_basefill_001):
    return _base_universe_d3(ccl_base_universe_d2_016_ccl_basefill_001, 16)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_016_ccl_basefill_001'] = {'inputs': ['ccl_base_universe_d2_016_ccl_basefill_001'], 'func': ccl_base_universe_d3_016_ccl_basefill_001}


def ccl_base_universe_d3_017_ccl_basefill_002(ccl_base_universe_d2_017_ccl_basefill_002):
    return _base_universe_d3(ccl_base_universe_d2_017_ccl_basefill_002, 17)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_017_ccl_basefill_002'] = {'inputs': ['ccl_base_universe_d2_017_ccl_basefill_002'], 'func': ccl_base_universe_d3_017_ccl_basefill_002}


def ccl_base_universe_d3_018_ccl_basefill_006(ccl_base_universe_d2_018_ccl_basefill_006):
    return _base_universe_d3(ccl_base_universe_d2_018_ccl_basefill_006, 18)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_018_ccl_basefill_006'] = {'inputs': ['ccl_base_universe_d2_018_ccl_basefill_006'], 'func': ccl_base_universe_d3_018_ccl_basefill_006}


def ccl_base_universe_d3_019_ccl_basefill_007(ccl_base_universe_d2_019_ccl_basefill_007):
    return _base_universe_d3(ccl_base_universe_d2_019_ccl_basefill_007, 19)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_019_ccl_basefill_007'] = {'inputs': ['ccl_base_universe_d2_019_ccl_basefill_007'], 'func': ccl_base_universe_d3_019_ccl_basefill_007}


def ccl_base_universe_d3_020_ccl_basefill_008(ccl_base_universe_d2_020_ccl_basefill_008):
    return _base_universe_d3(ccl_base_universe_d2_020_ccl_basefill_008, 20)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_020_ccl_basefill_008'] = {'inputs': ['ccl_base_universe_d2_020_ccl_basefill_008'], 'func': ccl_base_universe_d3_020_ccl_basefill_008}


def ccl_base_universe_d3_021_ccl_basefill_012(ccl_base_universe_d2_021_ccl_basefill_012):
    return _base_universe_d3(ccl_base_universe_d2_021_ccl_basefill_012, 21)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_021_ccl_basefill_012'] = {'inputs': ['ccl_base_universe_d2_021_ccl_basefill_012'], 'func': ccl_base_universe_d3_021_ccl_basefill_012}


def ccl_base_universe_d3_022_ccl_basefill_013(ccl_base_universe_d2_022_ccl_basefill_013):
    return _base_universe_d3(ccl_base_universe_d2_022_ccl_basefill_013, 22)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_022_ccl_basefill_013'] = {'inputs': ['ccl_base_universe_d2_022_ccl_basefill_013'], 'func': ccl_base_universe_d3_022_ccl_basefill_013}


def ccl_base_universe_d3_023_ccl_basefill_014(ccl_base_universe_d2_023_ccl_basefill_014):
    return _base_universe_d3(ccl_base_universe_d2_023_ccl_basefill_014, 23)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_023_ccl_basefill_014'] = {'inputs': ['ccl_base_universe_d2_023_ccl_basefill_014'], 'func': ccl_base_universe_d3_023_ccl_basefill_014}


def ccl_base_universe_d3_024_ccl_basefill_018(ccl_base_universe_d2_024_ccl_basefill_018):
    return _base_universe_d3(ccl_base_universe_d2_024_ccl_basefill_018, 24)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_024_ccl_basefill_018'] = {'inputs': ['ccl_base_universe_d2_024_ccl_basefill_018'], 'func': ccl_base_universe_d3_024_ccl_basefill_018}


def ccl_base_universe_d3_025_ccl_basefill_019(ccl_base_universe_d2_025_ccl_basefill_019):
    return _base_universe_d3(ccl_base_universe_d2_025_ccl_basefill_019, 25)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_025_ccl_basefill_019'] = {'inputs': ['ccl_base_universe_d2_025_ccl_basefill_019'], 'func': ccl_base_universe_d3_025_ccl_basefill_019}


def ccl_base_universe_d3_026_ccl_basefill_020(ccl_base_universe_d2_026_ccl_basefill_020):
    return _base_universe_d3(ccl_base_universe_d2_026_ccl_basefill_020, 26)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_026_ccl_basefill_020'] = {'inputs': ['ccl_base_universe_d2_026_ccl_basefill_020'], 'func': ccl_base_universe_d3_026_ccl_basefill_020}


def ccl_base_universe_d3_027_ccl_basefill_024(ccl_base_universe_d2_027_ccl_basefill_024):
    return _base_universe_d3(ccl_base_universe_d2_027_ccl_basefill_024, 27)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_027_ccl_basefill_024'] = {'inputs': ['ccl_base_universe_d2_027_ccl_basefill_024'], 'func': ccl_base_universe_d3_027_ccl_basefill_024}


def ccl_base_universe_d3_028_ccl_basefill_025(ccl_base_universe_d2_028_ccl_basefill_025):
    return _base_universe_d3(ccl_base_universe_d2_028_ccl_basefill_025, 28)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_028_ccl_basefill_025'] = {'inputs': ['ccl_base_universe_d2_028_ccl_basefill_025'], 'func': ccl_base_universe_d3_028_ccl_basefill_025}


def ccl_base_universe_d3_029_ccl_basefill_026(ccl_base_universe_d2_029_ccl_basefill_026):
    return _base_universe_d3(ccl_base_universe_d2_029_ccl_basefill_026, 29)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_029_ccl_basefill_026'] = {'inputs': ['ccl_base_universe_d2_029_ccl_basefill_026'], 'func': ccl_base_universe_d3_029_ccl_basefill_026}


def ccl_base_universe_d3_030_ccl_basefill_030(ccl_base_universe_d2_030_ccl_basefill_030):
    return _base_universe_d3(ccl_base_universe_d2_030_ccl_basefill_030, 30)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_030_ccl_basefill_030'] = {'inputs': ['ccl_base_universe_d2_030_ccl_basefill_030'], 'func': ccl_base_universe_d3_030_ccl_basefill_030}


def ccl_base_universe_d3_031_ccl_basefill_031(ccl_base_universe_d2_031_ccl_basefill_031):
    return _base_universe_d3(ccl_base_universe_d2_031_ccl_basefill_031, 31)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_031_ccl_basefill_031'] = {'inputs': ['ccl_base_universe_d2_031_ccl_basefill_031'], 'func': ccl_base_universe_d3_031_ccl_basefill_031}


def ccl_base_universe_d3_032_ccl_basefill_032(ccl_base_universe_d2_032_ccl_basefill_032):
    return _base_universe_d3(ccl_base_universe_d2_032_ccl_basefill_032, 32)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_032_ccl_basefill_032'] = {'inputs': ['ccl_base_universe_d2_032_ccl_basefill_032'], 'func': ccl_base_universe_d3_032_ccl_basefill_032}


def ccl_base_universe_d3_033_ccl_basefill_033(ccl_base_universe_d2_033_ccl_basefill_033):
    return _base_universe_d3(ccl_base_universe_d2_033_ccl_basefill_033, 33)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_033_ccl_basefill_033'] = {'inputs': ['ccl_base_universe_d2_033_ccl_basefill_033'], 'func': ccl_base_universe_d3_033_ccl_basefill_033}


def ccl_base_universe_d3_034_ccl_basefill_034(ccl_base_universe_d2_034_ccl_basefill_034):
    return _base_universe_d3(ccl_base_universe_d2_034_ccl_basefill_034, 34)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_034_ccl_basefill_034'] = {'inputs': ['ccl_base_universe_d2_034_ccl_basefill_034'], 'func': ccl_base_universe_d3_034_ccl_basefill_034}


def ccl_base_universe_d3_035_ccl_basefill_035(ccl_base_universe_d2_035_ccl_basefill_035):
    return _base_universe_d3(ccl_base_universe_d2_035_ccl_basefill_035, 35)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_035_ccl_basefill_035'] = {'inputs': ['ccl_base_universe_d2_035_ccl_basefill_035'], 'func': ccl_base_universe_d3_035_ccl_basefill_035}


def ccl_base_universe_d3_036_ccl_basefill_036(ccl_base_universe_d2_036_ccl_basefill_036):
    return _base_universe_d3(ccl_base_universe_d2_036_ccl_basefill_036, 36)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_036_ccl_basefill_036'] = {'inputs': ['ccl_base_universe_d2_036_ccl_basefill_036'], 'func': ccl_base_universe_d3_036_ccl_basefill_036}


def ccl_base_universe_d3_037_ccl_basefill_037(ccl_base_universe_d2_037_ccl_basefill_037):
    return _base_universe_d3(ccl_base_universe_d2_037_ccl_basefill_037, 37)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_037_ccl_basefill_037'] = {'inputs': ['ccl_base_universe_d2_037_ccl_basefill_037'], 'func': ccl_base_universe_d3_037_ccl_basefill_037}


def ccl_base_universe_d3_038_ccl_basefill_038(ccl_base_universe_d2_038_ccl_basefill_038):
    return _base_universe_d3(ccl_base_universe_d2_038_ccl_basefill_038, 38)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_038_ccl_basefill_038'] = {'inputs': ['ccl_base_universe_d2_038_ccl_basefill_038'], 'func': ccl_base_universe_d3_038_ccl_basefill_038}


def ccl_base_universe_d3_039_ccl_basefill_039(ccl_base_universe_d2_039_ccl_basefill_039):
    return _base_universe_d3(ccl_base_universe_d2_039_ccl_basefill_039, 39)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_039_ccl_basefill_039'] = {'inputs': ['ccl_base_universe_d2_039_ccl_basefill_039'], 'func': ccl_base_universe_d3_039_ccl_basefill_039}


def ccl_base_universe_d3_040_ccl_basefill_040(ccl_base_universe_d2_040_ccl_basefill_040):
    return _base_universe_d3(ccl_base_universe_d2_040_ccl_basefill_040, 40)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_040_ccl_basefill_040'] = {'inputs': ['ccl_base_universe_d2_040_ccl_basefill_040'], 'func': ccl_base_universe_d3_040_ccl_basefill_040}


def ccl_base_universe_d3_041_ccl_basefill_041(ccl_base_universe_d2_041_ccl_basefill_041):
    return _base_universe_d3(ccl_base_universe_d2_041_ccl_basefill_041, 41)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_041_ccl_basefill_041'] = {'inputs': ['ccl_base_universe_d2_041_ccl_basefill_041'], 'func': ccl_base_universe_d3_041_ccl_basefill_041}


def ccl_base_universe_d3_042_ccl_basefill_042(ccl_base_universe_d2_042_ccl_basefill_042):
    return _base_universe_d3(ccl_base_universe_d2_042_ccl_basefill_042, 42)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_042_ccl_basefill_042'] = {'inputs': ['ccl_base_universe_d2_042_ccl_basefill_042'], 'func': ccl_base_universe_d3_042_ccl_basefill_042}


def ccl_base_universe_d3_043_ccl_basefill_043(ccl_base_universe_d2_043_ccl_basefill_043):
    return _base_universe_d3(ccl_base_universe_d2_043_ccl_basefill_043, 43)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_043_ccl_basefill_043'] = {'inputs': ['ccl_base_universe_d2_043_ccl_basefill_043'], 'func': ccl_base_universe_d3_043_ccl_basefill_043}


def ccl_base_universe_d3_044_ccl_basefill_044(ccl_base_universe_d2_044_ccl_basefill_044):
    return _base_universe_d3(ccl_base_universe_d2_044_ccl_basefill_044, 44)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_044_ccl_basefill_044'] = {'inputs': ['ccl_base_universe_d2_044_ccl_basefill_044'], 'func': ccl_base_universe_d3_044_ccl_basefill_044}


def ccl_base_universe_d3_045_ccl_basefill_045(ccl_base_universe_d2_045_ccl_basefill_045):
    return _base_universe_d3(ccl_base_universe_d2_045_ccl_basefill_045, 45)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_045_ccl_basefill_045'] = {'inputs': ['ccl_base_universe_d2_045_ccl_basefill_045'], 'func': ccl_base_universe_d3_045_ccl_basefill_045}


def ccl_base_universe_d3_046_ccl_basefill_046(ccl_base_universe_d2_046_ccl_basefill_046):
    return _base_universe_d3(ccl_base_universe_d2_046_ccl_basefill_046, 46)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_046_ccl_basefill_046'] = {'inputs': ['ccl_base_universe_d2_046_ccl_basefill_046'], 'func': ccl_base_universe_d3_046_ccl_basefill_046}


def ccl_base_universe_d3_047_ccl_basefill_047(ccl_base_universe_d2_047_ccl_basefill_047):
    return _base_universe_d3(ccl_base_universe_d2_047_ccl_basefill_047, 47)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_047_ccl_basefill_047'] = {'inputs': ['ccl_base_universe_d2_047_ccl_basefill_047'], 'func': ccl_base_universe_d3_047_ccl_basefill_047}


def ccl_base_universe_d3_048_ccl_basefill_048(ccl_base_universe_d2_048_ccl_basefill_048):
    return _base_universe_d3(ccl_base_universe_d2_048_ccl_basefill_048, 48)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_048_ccl_basefill_048'] = {'inputs': ['ccl_base_universe_d2_048_ccl_basefill_048'], 'func': ccl_base_universe_d3_048_ccl_basefill_048}


def ccl_base_universe_d3_049_ccl_basefill_049(ccl_base_universe_d2_049_ccl_basefill_049):
    return _base_universe_d3(ccl_base_universe_d2_049_ccl_basefill_049, 49)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_049_ccl_basefill_049'] = {'inputs': ['ccl_base_universe_d2_049_ccl_basefill_049'], 'func': ccl_base_universe_d3_049_ccl_basefill_049}


def ccl_base_universe_d3_050_ccl_basefill_050(ccl_base_universe_d2_050_ccl_basefill_050):
    return _base_universe_d3(ccl_base_universe_d2_050_ccl_basefill_050, 50)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_050_ccl_basefill_050'] = {'inputs': ['ccl_base_universe_d2_050_ccl_basefill_050'], 'func': ccl_base_universe_d3_050_ccl_basefill_050}


def ccl_base_universe_d3_051_ccl_basefill_051(ccl_base_universe_d2_051_ccl_basefill_051):
    return _base_universe_d3(ccl_base_universe_d2_051_ccl_basefill_051, 51)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_051_ccl_basefill_051'] = {'inputs': ['ccl_base_universe_d2_051_ccl_basefill_051'], 'func': ccl_base_universe_d3_051_ccl_basefill_051}


def ccl_base_universe_d3_052_ccl_basefill_052(ccl_base_universe_d2_052_ccl_basefill_052):
    return _base_universe_d3(ccl_base_universe_d2_052_ccl_basefill_052, 52)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_052_ccl_basefill_052'] = {'inputs': ['ccl_base_universe_d2_052_ccl_basefill_052'], 'func': ccl_base_universe_d3_052_ccl_basefill_052}


def ccl_base_universe_d3_053_ccl_basefill_053(ccl_base_universe_d2_053_ccl_basefill_053):
    return _base_universe_d3(ccl_base_universe_d2_053_ccl_basefill_053, 53)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_053_ccl_basefill_053'] = {'inputs': ['ccl_base_universe_d2_053_ccl_basefill_053'], 'func': ccl_base_universe_d3_053_ccl_basefill_053}


def ccl_base_universe_d3_054_ccl_basefill_054(ccl_base_universe_d2_054_ccl_basefill_054):
    return _base_universe_d3(ccl_base_universe_d2_054_ccl_basefill_054, 54)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_054_ccl_basefill_054'] = {'inputs': ['ccl_base_universe_d2_054_ccl_basefill_054'], 'func': ccl_base_universe_d3_054_ccl_basefill_054}


def ccl_base_universe_d3_055_ccl_basefill_055(ccl_base_universe_d2_055_ccl_basefill_055):
    return _base_universe_d3(ccl_base_universe_d2_055_ccl_basefill_055, 55)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_055_ccl_basefill_055'] = {'inputs': ['ccl_base_universe_d2_055_ccl_basefill_055'], 'func': ccl_base_universe_d3_055_ccl_basefill_055}


def ccl_base_universe_d3_056_ccl_basefill_056(ccl_base_universe_d2_056_ccl_basefill_056):
    return _base_universe_d3(ccl_base_universe_d2_056_ccl_basefill_056, 56)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_056_ccl_basefill_056'] = {'inputs': ['ccl_base_universe_d2_056_ccl_basefill_056'], 'func': ccl_base_universe_d3_056_ccl_basefill_056}


def ccl_base_universe_d3_057_ccl_basefill_057(ccl_base_universe_d2_057_ccl_basefill_057):
    return _base_universe_d3(ccl_base_universe_d2_057_ccl_basefill_057, 57)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_057_ccl_basefill_057'] = {'inputs': ['ccl_base_universe_d2_057_ccl_basefill_057'], 'func': ccl_base_universe_d3_057_ccl_basefill_057}


def ccl_base_universe_d3_058_ccl_basefill_058(ccl_base_universe_d2_058_ccl_basefill_058):
    return _base_universe_d3(ccl_base_universe_d2_058_ccl_basefill_058, 58)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_058_ccl_basefill_058'] = {'inputs': ['ccl_base_universe_d2_058_ccl_basefill_058'], 'func': ccl_base_universe_d3_058_ccl_basefill_058}


def ccl_base_universe_d3_059_ccl_basefill_059(ccl_base_universe_d2_059_ccl_basefill_059):
    return _base_universe_d3(ccl_base_universe_d2_059_ccl_basefill_059, 59)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_059_ccl_basefill_059'] = {'inputs': ['ccl_base_universe_d2_059_ccl_basefill_059'], 'func': ccl_base_universe_d3_059_ccl_basefill_059}


def ccl_base_universe_d3_060_ccl_basefill_060(ccl_base_universe_d2_060_ccl_basefill_060):
    return _base_universe_d3(ccl_base_universe_d2_060_ccl_basefill_060, 60)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_060_ccl_basefill_060'] = {'inputs': ['ccl_base_universe_d2_060_ccl_basefill_060'], 'func': ccl_base_universe_d3_060_ccl_basefill_060}


def ccl_base_universe_d3_061_ccl_basefill_061(ccl_base_universe_d2_061_ccl_basefill_061):
    return _base_universe_d3(ccl_base_universe_d2_061_ccl_basefill_061, 61)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_061_ccl_basefill_061'] = {'inputs': ['ccl_base_universe_d2_061_ccl_basefill_061'], 'func': ccl_base_universe_d3_061_ccl_basefill_061}


def ccl_base_universe_d3_062_ccl_basefill_062(ccl_base_universe_d2_062_ccl_basefill_062):
    return _base_universe_d3(ccl_base_universe_d2_062_ccl_basefill_062, 62)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_062_ccl_basefill_062'] = {'inputs': ['ccl_base_universe_d2_062_ccl_basefill_062'], 'func': ccl_base_universe_d3_062_ccl_basefill_062}


def ccl_base_universe_d3_063_ccl_basefill_063(ccl_base_universe_d2_063_ccl_basefill_063):
    return _base_universe_d3(ccl_base_universe_d2_063_ccl_basefill_063, 63)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_063_ccl_basefill_063'] = {'inputs': ['ccl_base_universe_d2_063_ccl_basefill_063'], 'func': ccl_base_universe_d3_063_ccl_basefill_063}


def ccl_base_universe_d3_064_ccl_basefill_064(ccl_base_universe_d2_064_ccl_basefill_064):
    return _base_universe_d3(ccl_base_universe_d2_064_ccl_basefill_064, 64)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_064_ccl_basefill_064'] = {'inputs': ['ccl_base_universe_d2_064_ccl_basefill_064'], 'func': ccl_base_universe_d3_064_ccl_basefill_064}


def ccl_base_universe_d3_065_ccl_basefill_065(ccl_base_universe_d2_065_ccl_basefill_065):
    return _base_universe_d3(ccl_base_universe_d2_065_ccl_basefill_065, 65)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_065_ccl_basefill_065'] = {'inputs': ['ccl_base_universe_d2_065_ccl_basefill_065'], 'func': ccl_base_universe_d3_065_ccl_basefill_065}


def ccl_base_universe_d3_066_ccl_basefill_066(ccl_base_universe_d2_066_ccl_basefill_066):
    return _base_universe_d3(ccl_base_universe_d2_066_ccl_basefill_066, 66)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_066_ccl_basefill_066'] = {'inputs': ['ccl_base_universe_d2_066_ccl_basefill_066'], 'func': ccl_base_universe_d3_066_ccl_basefill_066}


def ccl_base_universe_d3_067_ccl_basefill_067(ccl_base_universe_d2_067_ccl_basefill_067):
    return _base_universe_d3(ccl_base_universe_d2_067_ccl_basefill_067, 67)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_067_ccl_basefill_067'] = {'inputs': ['ccl_base_universe_d2_067_ccl_basefill_067'], 'func': ccl_base_universe_d3_067_ccl_basefill_067}


def ccl_base_universe_d3_068_ccl_basefill_068(ccl_base_universe_d2_068_ccl_basefill_068):
    return _base_universe_d3(ccl_base_universe_d2_068_ccl_basefill_068, 68)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_068_ccl_basefill_068'] = {'inputs': ['ccl_base_universe_d2_068_ccl_basefill_068'], 'func': ccl_base_universe_d3_068_ccl_basefill_068}


def ccl_base_universe_d3_069_ccl_basefill_069(ccl_base_universe_d2_069_ccl_basefill_069):
    return _base_universe_d3(ccl_base_universe_d2_069_ccl_basefill_069, 69)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_069_ccl_basefill_069'] = {'inputs': ['ccl_base_universe_d2_069_ccl_basefill_069'], 'func': ccl_base_universe_d3_069_ccl_basefill_069}


def ccl_base_universe_d3_070_ccl_basefill_070(ccl_base_universe_d2_070_ccl_basefill_070):
    return _base_universe_d3(ccl_base_universe_d2_070_ccl_basefill_070, 70)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_070_ccl_basefill_070'] = {'inputs': ['ccl_base_universe_d2_070_ccl_basefill_070'], 'func': ccl_base_universe_d3_070_ccl_basefill_070}


def ccl_base_universe_d3_071_ccl_basefill_071(ccl_base_universe_d2_071_ccl_basefill_071):
    return _base_universe_d3(ccl_base_universe_d2_071_ccl_basefill_071, 71)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_071_ccl_basefill_071'] = {'inputs': ['ccl_base_universe_d2_071_ccl_basefill_071'], 'func': ccl_base_universe_d3_071_ccl_basefill_071}


def ccl_base_universe_d3_072_ccl_basefill_072(ccl_base_universe_d2_072_ccl_basefill_072):
    return _base_universe_d3(ccl_base_universe_d2_072_ccl_basefill_072, 72)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_072_ccl_basefill_072'] = {'inputs': ['ccl_base_universe_d2_072_ccl_basefill_072'], 'func': ccl_base_universe_d3_072_ccl_basefill_072}


def ccl_base_universe_d3_073_ccl_basefill_073(ccl_base_universe_d2_073_ccl_basefill_073):
    return _base_universe_d3(ccl_base_universe_d2_073_ccl_basefill_073, 73)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_073_ccl_basefill_073'] = {'inputs': ['ccl_base_universe_d2_073_ccl_basefill_073'], 'func': ccl_base_universe_d3_073_ccl_basefill_073}


def ccl_base_universe_d3_074_ccl_basefill_074(ccl_base_universe_d2_074_ccl_basefill_074):
    return _base_universe_d3(ccl_base_universe_d2_074_ccl_basefill_074, 74)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_074_ccl_basefill_074'] = {'inputs': ['ccl_base_universe_d2_074_ccl_basefill_074'], 'func': ccl_base_universe_d3_074_ccl_basefill_074}


def ccl_base_universe_d3_075_ccl_basefill_075(ccl_base_universe_d2_075_ccl_basefill_075):
    return _base_universe_d3(ccl_base_universe_d2_075_ccl_basefill_075, 75)
CCL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['ccl_base_universe_d3_075_ccl_basefill_075'] = {'inputs': ['ccl_base_universe_d2_075_ccl_basefill_075'], 'func': ccl_base_universe_d3_075_ccl_basefill_075}
