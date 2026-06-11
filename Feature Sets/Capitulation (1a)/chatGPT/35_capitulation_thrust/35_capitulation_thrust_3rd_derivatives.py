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



def cth_001_return_decay_accel_1(cth_001_return_decay_roc_1):
    feature = _s(cth_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def cth_007_return_decay_accel_5(cth_007_return_decay_roc_5):
    feature = _s(cth_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def cth_013_return_decay_accel_42(cth_013_return_decay_roc_42):
    feature = _s(cth_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def cth_179_cth_019_return_decay_42_019_accel_126(cth_154_cth_019_return_decay_42_019_roc_126):
    feature = _s(cth_154_cth_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def cth_180_cth_025_return_decay_5_025_accel_378(cth_155_cth_025_return_decay_5_025_roc_378):
    feature = _s(cth_155_cth_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















CAPITULATION_THRUST_REGISTRY_3RD_DERIVATIVES = {
    'cth_001_return_decay_accel_1': {'inputs': ['cth_001_return_decay_roc_1'], 'func': cth_001_return_decay_accel_1},
    'cth_007_return_decay_accel_5': {'inputs': ['cth_007_return_decay_roc_5'], 'func': cth_007_return_decay_accel_5},
    'cth_013_return_decay_accel_42': {'inputs': ['cth_013_return_decay_roc_42'], 'func': cth_013_return_decay_accel_42},
    'cth_179_cth_019_return_decay_42_019_accel_126': {'inputs': ['cth_154_cth_019_return_decay_42_019_roc_126'], 'func': cth_179_cth_019_return_decay_42_019_accel_126},
    'cth_180_cth_025_return_decay_5_025_accel_378': {'inputs': ['cth_155_cth_025_return_decay_5_025_roc_378'], 'func': cth_180_cth_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def ct_replacement_d3_001(ct_replacement_d2_001):
    feature = _clean(ct_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_001'] = {'inputs': ['ct_replacement_d2_001'], 'func': ct_replacement_d3_001}


def ct_replacement_d3_002(ct_replacement_d2_002):
    feature = _clean(ct_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_002'] = {'inputs': ['ct_replacement_d2_002'], 'func': ct_replacement_d3_002}


def ct_replacement_d3_003(ct_replacement_d2_003):
    feature = _clean(ct_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_003'] = {'inputs': ['ct_replacement_d2_003'], 'func': ct_replacement_d3_003}


def ct_replacement_d3_004(ct_replacement_d2_004):
    feature = _clean(ct_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_004'] = {'inputs': ['ct_replacement_d2_004'], 'func': ct_replacement_d3_004}


def ct_replacement_d3_005(ct_replacement_d2_005):
    feature = _clean(ct_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_005'] = {'inputs': ['ct_replacement_d2_005'], 'func': ct_replacement_d3_005}


def ct_replacement_d3_006(ct_replacement_d2_006):
    feature = _clean(ct_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_006'] = {'inputs': ['ct_replacement_d2_006'], 'func': ct_replacement_d3_006}


def ct_replacement_d3_007(ct_replacement_d2_007):
    feature = _clean(ct_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_007'] = {'inputs': ['ct_replacement_d2_007'], 'func': ct_replacement_d3_007}


def ct_replacement_d3_008(ct_replacement_d2_008):
    feature = _clean(ct_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_008'] = {'inputs': ['ct_replacement_d2_008'], 'func': ct_replacement_d3_008}


def ct_replacement_d3_009(ct_replacement_d2_009):
    feature = _clean(ct_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_009'] = {'inputs': ['ct_replacement_d2_009'], 'func': ct_replacement_d3_009}


def ct_replacement_d3_010(ct_replacement_d2_010):
    feature = _clean(ct_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_010'] = {'inputs': ['ct_replacement_d2_010'], 'func': ct_replacement_d3_010}


def ct_replacement_d3_011(ct_replacement_d2_011):
    feature = _clean(ct_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_011'] = {'inputs': ['ct_replacement_d2_011'], 'func': ct_replacement_d3_011}


def ct_replacement_d3_012(ct_replacement_d2_012):
    feature = _clean(ct_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_012'] = {'inputs': ['ct_replacement_d2_012'], 'func': ct_replacement_d3_012}


def ct_replacement_d3_013(ct_replacement_d2_013):
    feature = _clean(ct_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_013'] = {'inputs': ['ct_replacement_d2_013'], 'func': ct_replacement_d3_013}


def ct_replacement_d3_014(ct_replacement_d2_014):
    feature = _clean(ct_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_014'] = {'inputs': ['ct_replacement_d2_014'], 'func': ct_replacement_d3_014}


def ct_replacement_d3_015(ct_replacement_d2_015):
    feature = _clean(ct_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_015'] = {'inputs': ['ct_replacement_d2_015'], 'func': ct_replacement_d3_015}


def ct_replacement_d3_016(ct_replacement_d2_016):
    feature = _clean(ct_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_016'] = {'inputs': ['ct_replacement_d2_016'], 'func': ct_replacement_d3_016}


def ct_replacement_d3_017(ct_replacement_d2_017):
    feature = _clean(ct_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_017'] = {'inputs': ['ct_replacement_d2_017'], 'func': ct_replacement_d3_017}


def ct_replacement_d3_018(ct_replacement_d2_018):
    feature = _clean(ct_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_018'] = {'inputs': ['ct_replacement_d2_018'], 'func': ct_replacement_d3_018}


def ct_replacement_d3_019(ct_replacement_d2_019):
    feature = _clean(ct_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_019'] = {'inputs': ['ct_replacement_d2_019'], 'func': ct_replacement_d3_019}


def ct_replacement_d3_020(ct_replacement_d2_020):
    feature = _clean(ct_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_020'] = {'inputs': ['ct_replacement_d2_020'], 'func': ct_replacement_d3_020}


def ct_replacement_d3_021(ct_replacement_d2_021):
    feature = _clean(ct_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_021'] = {'inputs': ['ct_replacement_d2_021'], 'func': ct_replacement_d3_021}


def ct_replacement_d3_022(ct_replacement_d2_022):
    feature = _clean(ct_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_022'] = {'inputs': ['ct_replacement_d2_022'], 'func': ct_replacement_d3_022}


def ct_replacement_d3_023(ct_replacement_d2_023):
    feature = _clean(ct_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_023'] = {'inputs': ['ct_replacement_d2_023'], 'func': ct_replacement_d3_023}


def ct_replacement_d3_024(ct_replacement_d2_024):
    feature = _clean(ct_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_024'] = {'inputs': ['ct_replacement_d2_024'], 'func': ct_replacement_d3_024}


def ct_replacement_d3_025(ct_replacement_d2_025):
    feature = _clean(ct_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_025'] = {'inputs': ['ct_replacement_d2_025'], 'func': ct_replacement_d3_025}


def ct_replacement_d3_026(ct_replacement_d2_026):
    feature = _clean(ct_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_026'] = {'inputs': ['ct_replacement_d2_026'], 'func': ct_replacement_d3_026}


def ct_replacement_d3_027(ct_replacement_d2_027):
    feature = _clean(ct_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_027'] = {'inputs': ['ct_replacement_d2_027'], 'func': ct_replacement_d3_027}


def ct_replacement_d3_028(ct_replacement_d2_028):
    feature = _clean(ct_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_028'] = {'inputs': ['ct_replacement_d2_028'], 'func': ct_replacement_d3_028}


def ct_replacement_d3_029(ct_replacement_d2_029):
    feature = _clean(ct_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_029'] = {'inputs': ['ct_replacement_d2_029'], 'func': ct_replacement_d3_029}


def ct_replacement_d3_030(ct_replacement_d2_030):
    feature = _clean(ct_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_030'] = {'inputs': ['ct_replacement_d2_030'], 'func': ct_replacement_d3_030}


def ct_replacement_d3_031(ct_replacement_d2_031):
    feature = _clean(ct_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_031'] = {'inputs': ['ct_replacement_d2_031'], 'func': ct_replacement_d3_031}


def ct_replacement_d3_032(ct_replacement_d2_032):
    feature = _clean(ct_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_032'] = {'inputs': ['ct_replacement_d2_032'], 'func': ct_replacement_d3_032}


def ct_replacement_d3_033(ct_replacement_d2_033):
    feature = _clean(ct_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_033'] = {'inputs': ['ct_replacement_d2_033'], 'func': ct_replacement_d3_033}


def ct_replacement_d3_034(ct_replacement_d2_034):
    feature = _clean(ct_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_034'] = {'inputs': ['ct_replacement_d2_034'], 'func': ct_replacement_d3_034}


def ct_replacement_d3_035(ct_replacement_d2_035):
    feature = _clean(ct_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_035'] = {'inputs': ['ct_replacement_d2_035'], 'func': ct_replacement_d3_035}


def ct_replacement_d3_036(ct_replacement_d2_036):
    feature = _clean(ct_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_036'] = {'inputs': ['ct_replacement_d2_036'], 'func': ct_replacement_d3_036}


def ct_replacement_d3_037(ct_replacement_d2_037):
    feature = _clean(ct_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_037'] = {'inputs': ['ct_replacement_d2_037'], 'func': ct_replacement_d3_037}


def ct_replacement_d3_038(ct_replacement_d2_038):
    feature = _clean(ct_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_038'] = {'inputs': ['ct_replacement_d2_038'], 'func': ct_replacement_d3_038}


def ct_replacement_d3_039(ct_replacement_d2_039):
    feature = _clean(ct_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_039'] = {'inputs': ['ct_replacement_d2_039'], 'func': ct_replacement_d3_039}


def ct_replacement_d3_040(ct_replacement_d2_040):
    feature = _clean(ct_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_040'] = {'inputs': ['ct_replacement_d2_040'], 'func': ct_replacement_d3_040}


def ct_replacement_d3_041(ct_replacement_d2_041):
    feature = _clean(ct_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_041'] = {'inputs': ['ct_replacement_d2_041'], 'func': ct_replacement_d3_041}


def ct_replacement_d3_042(ct_replacement_d2_042):
    feature = _clean(ct_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_042'] = {'inputs': ['ct_replacement_d2_042'], 'func': ct_replacement_d3_042}


def ct_replacement_d3_043(ct_replacement_d2_043):
    feature = _clean(ct_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_043'] = {'inputs': ['ct_replacement_d2_043'], 'func': ct_replacement_d3_043}


def ct_replacement_d3_044(ct_replacement_d2_044):
    feature = _clean(ct_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_044'] = {'inputs': ['ct_replacement_d2_044'], 'func': ct_replacement_d3_044}


def ct_replacement_d3_045(ct_replacement_d2_045):
    feature = _clean(ct_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_045'] = {'inputs': ['ct_replacement_d2_045'], 'func': ct_replacement_d3_045}


def ct_replacement_d3_046(ct_replacement_d2_046):
    feature = _clean(ct_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_046'] = {'inputs': ['ct_replacement_d2_046'], 'func': ct_replacement_d3_046}


def ct_replacement_d3_047(ct_replacement_d2_047):
    feature = _clean(ct_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_047'] = {'inputs': ['ct_replacement_d2_047'], 'func': ct_replacement_d3_047}


def ct_replacement_d3_048(ct_replacement_d2_048):
    feature = _clean(ct_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_048'] = {'inputs': ['ct_replacement_d2_048'], 'func': ct_replacement_d3_048}


def ct_replacement_d3_049(ct_replacement_d2_049):
    feature = _clean(ct_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_049'] = {'inputs': ['ct_replacement_d2_049'], 'func': ct_replacement_d3_049}


def ct_replacement_d3_050(ct_replacement_d2_050):
    feature = _clean(ct_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_050'] = {'inputs': ['ct_replacement_d2_050'], 'func': ct_replacement_d3_050}


def ct_replacement_d3_051(ct_replacement_d2_051):
    feature = _clean(ct_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_051'] = {'inputs': ['ct_replacement_d2_051'], 'func': ct_replacement_d3_051}


def ct_replacement_d3_052(ct_replacement_d2_052):
    feature = _clean(ct_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_052'] = {'inputs': ['ct_replacement_d2_052'], 'func': ct_replacement_d3_052}


def ct_replacement_d3_053(ct_replacement_d2_053):
    feature = _clean(ct_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_053'] = {'inputs': ['ct_replacement_d2_053'], 'func': ct_replacement_d3_053}


def ct_replacement_d3_054(ct_replacement_d2_054):
    feature = _clean(ct_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_054'] = {'inputs': ['ct_replacement_d2_054'], 'func': ct_replacement_d3_054}


def ct_replacement_d3_055(ct_replacement_d2_055):
    feature = _clean(ct_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_055'] = {'inputs': ['ct_replacement_d2_055'], 'func': ct_replacement_d3_055}


def ct_replacement_d3_056(ct_replacement_d2_056):
    feature = _clean(ct_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_056'] = {'inputs': ['ct_replacement_d2_056'], 'func': ct_replacement_d3_056}


def ct_replacement_d3_057(ct_replacement_d2_057):
    feature = _clean(ct_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_057'] = {'inputs': ['ct_replacement_d2_057'], 'func': ct_replacement_d3_057}


def ct_replacement_d3_058(ct_replacement_d2_058):
    feature = _clean(ct_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_058'] = {'inputs': ['ct_replacement_d2_058'], 'func': ct_replacement_d3_058}


def ct_replacement_d3_059(ct_replacement_d2_059):
    feature = _clean(ct_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_059'] = {'inputs': ['ct_replacement_d2_059'], 'func': ct_replacement_d3_059}


def ct_replacement_d3_060(ct_replacement_d2_060):
    feature = _clean(ct_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_060'] = {'inputs': ['ct_replacement_d2_060'], 'func': ct_replacement_d3_060}


def ct_replacement_d3_061(ct_replacement_d2_061):
    feature = _clean(ct_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_061'] = {'inputs': ['ct_replacement_d2_061'], 'func': ct_replacement_d3_061}


def ct_replacement_d3_062(ct_replacement_d2_062):
    feature = _clean(ct_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_062'] = {'inputs': ['ct_replacement_d2_062'], 'func': ct_replacement_d3_062}


def ct_replacement_d3_063(ct_replacement_d2_063):
    feature = _clean(ct_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_063'] = {'inputs': ['ct_replacement_d2_063'], 'func': ct_replacement_d3_063}


def ct_replacement_d3_064(ct_replacement_d2_064):
    feature = _clean(ct_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_064'] = {'inputs': ['ct_replacement_d2_064'], 'func': ct_replacement_d3_064}


def ct_replacement_d3_065(ct_replacement_d2_065):
    feature = _clean(ct_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_065'] = {'inputs': ['ct_replacement_d2_065'], 'func': ct_replacement_d3_065}


def ct_replacement_d3_066(ct_replacement_d2_066):
    feature = _clean(ct_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_066'] = {'inputs': ['ct_replacement_d2_066'], 'func': ct_replacement_d3_066}


def ct_replacement_d3_067(ct_replacement_d2_067):
    feature = _clean(ct_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_067'] = {'inputs': ['ct_replacement_d2_067'], 'func': ct_replacement_d3_067}


def ct_replacement_d3_068(ct_replacement_d2_068):
    feature = _clean(ct_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_068'] = {'inputs': ['ct_replacement_d2_068'], 'func': ct_replacement_d3_068}


def ct_replacement_d3_069(ct_replacement_d2_069):
    feature = _clean(ct_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_069'] = {'inputs': ['ct_replacement_d2_069'], 'func': ct_replacement_d3_069}


def ct_replacement_d3_070(ct_replacement_d2_070):
    feature = _clean(ct_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_070'] = {'inputs': ['ct_replacement_d2_070'], 'func': ct_replacement_d3_070}


def ct_replacement_d3_071(ct_replacement_d2_071):
    feature = _clean(ct_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_071'] = {'inputs': ['ct_replacement_d2_071'], 'func': ct_replacement_d3_071}


def ct_replacement_d3_072(ct_replacement_d2_072):
    feature = _clean(ct_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_072'] = {'inputs': ['ct_replacement_d2_072'], 'func': ct_replacement_d3_072}


def ct_replacement_d3_073(ct_replacement_d2_073):
    feature = _clean(ct_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_073'] = {'inputs': ['ct_replacement_d2_073'], 'func': ct_replacement_d3_073}


def ct_replacement_d3_074(ct_replacement_d2_074):
    feature = _clean(ct_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_074'] = {'inputs': ['ct_replacement_d2_074'], 'func': ct_replacement_d3_074}


def ct_replacement_d3_075(ct_replacement_d2_075):
    feature = _clean(ct_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_075'] = {'inputs': ['ct_replacement_d2_075'], 'func': ct_replacement_d3_075}


def ct_replacement_d3_076(ct_replacement_d2_076):
    feature = _clean(ct_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_076'] = {'inputs': ['ct_replacement_d2_076'], 'func': ct_replacement_d3_076}


def ct_replacement_d3_077(ct_replacement_d2_077):
    feature = _clean(ct_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_077'] = {'inputs': ['ct_replacement_d2_077'], 'func': ct_replacement_d3_077}


def ct_replacement_d3_078(ct_replacement_d2_078):
    feature = _clean(ct_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_078'] = {'inputs': ['ct_replacement_d2_078'], 'func': ct_replacement_d3_078}


def ct_replacement_d3_079(ct_replacement_d2_079):
    feature = _clean(ct_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_079'] = {'inputs': ['ct_replacement_d2_079'], 'func': ct_replacement_d3_079}


def ct_replacement_d3_080(ct_replacement_d2_080):
    feature = _clean(ct_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_080'] = {'inputs': ['ct_replacement_d2_080'], 'func': ct_replacement_d3_080}


def ct_replacement_d3_081(ct_replacement_d2_081):
    feature = _clean(ct_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_081'] = {'inputs': ['ct_replacement_d2_081'], 'func': ct_replacement_d3_081}


def ct_replacement_d3_082(ct_replacement_d2_082):
    feature = _clean(ct_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_082'] = {'inputs': ['ct_replacement_d2_082'], 'func': ct_replacement_d3_082}


def ct_replacement_d3_083(ct_replacement_d2_083):
    feature = _clean(ct_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_083'] = {'inputs': ['ct_replacement_d2_083'], 'func': ct_replacement_d3_083}


def ct_replacement_d3_084(ct_replacement_d2_084):
    feature = _clean(ct_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_084'] = {'inputs': ['ct_replacement_d2_084'], 'func': ct_replacement_d3_084}


def ct_replacement_d3_085(ct_replacement_d2_085):
    feature = _clean(ct_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_085'] = {'inputs': ['ct_replacement_d2_085'], 'func': ct_replacement_d3_085}


def ct_replacement_d3_086(ct_replacement_d2_086):
    feature = _clean(ct_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_086'] = {'inputs': ['ct_replacement_d2_086'], 'func': ct_replacement_d3_086}


def ct_replacement_d3_087(ct_replacement_d2_087):
    feature = _clean(ct_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_087'] = {'inputs': ['ct_replacement_d2_087'], 'func': ct_replacement_d3_087}


def ct_replacement_d3_088(ct_replacement_d2_088):
    feature = _clean(ct_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_088'] = {'inputs': ['ct_replacement_d2_088'], 'func': ct_replacement_d3_088}


def ct_replacement_d3_089(ct_replacement_d2_089):
    feature = _clean(ct_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_089'] = {'inputs': ['ct_replacement_d2_089'], 'func': ct_replacement_d3_089}


def ct_replacement_d3_090(ct_replacement_d2_090):
    feature = _clean(ct_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_090'] = {'inputs': ['ct_replacement_d2_090'], 'func': ct_replacement_d3_090}


def ct_replacement_d3_091(ct_replacement_d2_091):
    feature = _clean(ct_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_091'] = {'inputs': ['ct_replacement_d2_091'], 'func': ct_replacement_d3_091}


def ct_replacement_d3_092(ct_replacement_d2_092):
    feature = _clean(ct_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_092'] = {'inputs': ['ct_replacement_d2_092'], 'func': ct_replacement_d3_092}


def ct_replacement_d3_093(ct_replacement_d2_093):
    feature = _clean(ct_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_093'] = {'inputs': ['ct_replacement_d2_093'], 'func': ct_replacement_d3_093}


def ct_replacement_d3_094(ct_replacement_d2_094):
    feature = _clean(ct_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_094'] = {'inputs': ['ct_replacement_d2_094'], 'func': ct_replacement_d3_094}


def ct_replacement_d3_095(ct_replacement_d2_095):
    feature = _clean(ct_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_095'] = {'inputs': ['ct_replacement_d2_095'], 'func': ct_replacement_d3_095}


def ct_replacement_d3_096(ct_replacement_d2_096):
    feature = _clean(ct_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_096'] = {'inputs': ['ct_replacement_d2_096'], 'func': ct_replacement_d3_096}


def ct_replacement_d3_097(ct_replacement_d2_097):
    feature = _clean(ct_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_097'] = {'inputs': ['ct_replacement_d2_097'], 'func': ct_replacement_d3_097}


def ct_replacement_d3_098(ct_replacement_d2_098):
    feature = _clean(ct_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_098'] = {'inputs': ['ct_replacement_d2_098'], 'func': ct_replacement_d3_098}


def ct_replacement_d3_099(ct_replacement_d2_099):
    feature = _clean(ct_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_099'] = {'inputs': ['ct_replacement_d2_099'], 'func': ct_replacement_d3_099}


def ct_replacement_d3_100(ct_replacement_d2_100):
    feature = _clean(ct_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_100'] = {'inputs': ['ct_replacement_d2_100'], 'func': ct_replacement_d3_100}


def ct_replacement_d3_101(ct_replacement_d2_101):
    feature = _clean(ct_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_101'] = {'inputs': ['ct_replacement_d2_101'], 'func': ct_replacement_d3_101}


def ct_replacement_d3_102(ct_replacement_d2_102):
    feature = _clean(ct_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_102'] = {'inputs': ['ct_replacement_d2_102'], 'func': ct_replacement_d3_102}


def ct_replacement_d3_103(ct_replacement_d2_103):
    feature = _clean(ct_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_103'] = {'inputs': ['ct_replacement_d2_103'], 'func': ct_replacement_d3_103}


def ct_replacement_d3_104(ct_replacement_d2_104):
    feature = _clean(ct_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_104'] = {'inputs': ['ct_replacement_d2_104'], 'func': ct_replacement_d3_104}


def ct_replacement_d3_105(ct_replacement_d2_105):
    feature = _clean(ct_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_105'] = {'inputs': ['ct_replacement_d2_105'], 'func': ct_replacement_d3_105}


def ct_replacement_d3_106(ct_replacement_d2_106):
    feature = _clean(ct_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_106'] = {'inputs': ['ct_replacement_d2_106'], 'func': ct_replacement_d3_106}


def ct_replacement_d3_107(ct_replacement_d2_107):
    feature = _clean(ct_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_107'] = {'inputs': ['ct_replacement_d2_107'], 'func': ct_replacement_d3_107}


def ct_replacement_d3_108(ct_replacement_d2_108):
    feature = _clean(ct_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_108'] = {'inputs': ['ct_replacement_d2_108'], 'func': ct_replacement_d3_108}


def ct_replacement_d3_109(ct_replacement_d2_109):
    feature = _clean(ct_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_109'] = {'inputs': ['ct_replacement_d2_109'], 'func': ct_replacement_d3_109}


def ct_replacement_d3_110(ct_replacement_d2_110):
    feature = _clean(ct_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_110'] = {'inputs': ['ct_replacement_d2_110'], 'func': ct_replacement_d3_110}


def ct_replacement_d3_111(ct_replacement_d2_111):
    feature = _clean(ct_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_111'] = {'inputs': ['ct_replacement_d2_111'], 'func': ct_replacement_d3_111}


def ct_replacement_d3_112(ct_replacement_d2_112):
    feature = _clean(ct_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_112'] = {'inputs': ['ct_replacement_d2_112'], 'func': ct_replacement_d3_112}


def ct_replacement_d3_113(ct_replacement_d2_113):
    feature = _clean(ct_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_113'] = {'inputs': ['ct_replacement_d2_113'], 'func': ct_replacement_d3_113}


def ct_replacement_d3_114(ct_replacement_d2_114):
    feature = _clean(ct_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_114'] = {'inputs': ['ct_replacement_d2_114'], 'func': ct_replacement_d3_114}


def ct_replacement_d3_115(ct_replacement_d2_115):
    feature = _clean(ct_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_115'] = {'inputs': ['ct_replacement_d2_115'], 'func': ct_replacement_d3_115}


def ct_replacement_d3_116(ct_replacement_d2_116):
    feature = _clean(ct_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_116'] = {'inputs': ['ct_replacement_d2_116'], 'func': ct_replacement_d3_116}


def ct_replacement_d3_117(ct_replacement_d2_117):
    feature = _clean(ct_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_117'] = {'inputs': ['ct_replacement_d2_117'], 'func': ct_replacement_d3_117}


def ct_replacement_d3_118(ct_replacement_d2_118):
    feature = _clean(ct_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_118'] = {'inputs': ['ct_replacement_d2_118'], 'func': ct_replacement_d3_118}


def ct_replacement_d3_119(ct_replacement_d2_119):
    feature = _clean(ct_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_119'] = {'inputs': ['ct_replacement_d2_119'], 'func': ct_replacement_d3_119}


def ct_replacement_d3_120(ct_replacement_d2_120):
    feature = _clean(ct_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_120'] = {'inputs': ['ct_replacement_d2_120'], 'func': ct_replacement_d3_120}


def ct_replacement_d3_121(ct_replacement_d2_121):
    feature = _clean(ct_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_121'] = {'inputs': ['ct_replacement_d2_121'], 'func': ct_replacement_d3_121}


def ct_replacement_d3_122(ct_replacement_d2_122):
    feature = _clean(ct_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_122'] = {'inputs': ['ct_replacement_d2_122'], 'func': ct_replacement_d3_122}


def ct_replacement_d3_123(ct_replacement_d2_123):
    feature = _clean(ct_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_123'] = {'inputs': ['ct_replacement_d2_123'], 'func': ct_replacement_d3_123}


def ct_replacement_d3_124(ct_replacement_d2_124):
    feature = _clean(ct_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_124'] = {'inputs': ['ct_replacement_d2_124'], 'func': ct_replacement_d3_124}


def ct_replacement_d3_125(ct_replacement_d2_125):
    feature = _clean(ct_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_125'] = {'inputs': ['ct_replacement_d2_125'], 'func': ct_replacement_d3_125}


def ct_replacement_d3_126(ct_replacement_d2_126):
    feature = _clean(ct_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_126'] = {'inputs': ['ct_replacement_d2_126'], 'func': ct_replacement_d3_126}


def ct_replacement_d3_127(ct_replacement_d2_127):
    feature = _clean(ct_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_127'] = {'inputs': ['ct_replacement_d2_127'], 'func': ct_replacement_d3_127}


def ct_replacement_d3_128(ct_replacement_d2_128):
    feature = _clean(ct_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_128'] = {'inputs': ['ct_replacement_d2_128'], 'func': ct_replacement_d3_128}


def ct_replacement_d3_129(ct_replacement_d2_129):
    feature = _clean(ct_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_129'] = {'inputs': ['ct_replacement_d2_129'], 'func': ct_replacement_d3_129}


def ct_replacement_d3_130(ct_replacement_d2_130):
    feature = _clean(ct_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_130'] = {'inputs': ['ct_replacement_d2_130'], 'func': ct_replacement_d3_130}


def ct_replacement_d3_131(ct_replacement_d2_131):
    feature = _clean(ct_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_131'] = {'inputs': ['ct_replacement_d2_131'], 'func': ct_replacement_d3_131}


def ct_replacement_d3_132(ct_replacement_d2_132):
    feature = _clean(ct_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_132'] = {'inputs': ['ct_replacement_d2_132'], 'func': ct_replacement_d3_132}


def ct_replacement_d3_133(ct_replacement_d2_133):
    feature = _clean(ct_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_133'] = {'inputs': ['ct_replacement_d2_133'], 'func': ct_replacement_d3_133}


def ct_replacement_d3_134(ct_replacement_d2_134):
    feature = _clean(ct_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_134'] = {'inputs': ['ct_replacement_d2_134'], 'func': ct_replacement_d3_134}


def ct_replacement_d3_135(ct_replacement_d2_135):
    feature = _clean(ct_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_135'] = {'inputs': ['ct_replacement_d2_135'], 'func': ct_replacement_d3_135}


def ct_replacement_d3_136(ct_replacement_d2_136):
    feature = _clean(ct_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_136'] = {'inputs': ['ct_replacement_d2_136'], 'func': ct_replacement_d3_136}


def ct_replacement_d3_137(ct_replacement_d2_137):
    feature = _clean(ct_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_137'] = {'inputs': ['ct_replacement_d2_137'], 'func': ct_replacement_d3_137}


def ct_replacement_d3_138(ct_replacement_d2_138):
    feature = _clean(ct_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_138'] = {'inputs': ['ct_replacement_d2_138'], 'func': ct_replacement_d3_138}


def ct_replacement_d3_139(ct_replacement_d2_139):
    feature = _clean(ct_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_139'] = {'inputs': ['ct_replacement_d2_139'], 'func': ct_replacement_d3_139}


def ct_replacement_d3_140(ct_replacement_d2_140):
    feature = _clean(ct_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_140'] = {'inputs': ['ct_replacement_d2_140'], 'func': ct_replacement_d3_140}


def ct_replacement_d3_141(ct_replacement_d2_141):
    feature = _clean(ct_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_141'] = {'inputs': ['ct_replacement_d2_141'], 'func': ct_replacement_d3_141}


def ct_replacement_d3_142(ct_replacement_d2_142):
    feature = _clean(ct_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_142'] = {'inputs': ['ct_replacement_d2_142'], 'func': ct_replacement_d3_142}


def ct_replacement_d3_143(ct_replacement_d2_143):
    feature = _clean(ct_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_143'] = {'inputs': ['ct_replacement_d2_143'], 'func': ct_replacement_d3_143}


def ct_replacement_d3_144(ct_replacement_d2_144):
    feature = _clean(ct_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_144'] = {'inputs': ['ct_replacement_d2_144'], 'func': ct_replacement_d3_144}


def ct_replacement_d3_145(ct_replacement_d2_145):
    feature = _clean(ct_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_145'] = {'inputs': ['ct_replacement_d2_145'], 'func': ct_replacement_d3_145}


def ct_replacement_d3_146(ct_replacement_d2_146):
    feature = _clean(ct_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_146'] = {'inputs': ['ct_replacement_d2_146'], 'func': ct_replacement_d3_146}


def ct_replacement_d3_147(ct_replacement_d2_147):
    feature = _clean(ct_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_147'] = {'inputs': ['ct_replacement_d2_147'], 'func': ct_replacement_d3_147}


def ct_replacement_d3_148(ct_replacement_d2_148):
    feature = _clean(ct_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_148'] = {'inputs': ['ct_replacement_d2_148'], 'func': ct_replacement_d3_148}


def ct_replacement_d3_149(ct_replacement_d2_149):
    feature = _clean(ct_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_149'] = {'inputs': ['ct_replacement_d2_149'], 'func': ct_replacement_d3_149}


def ct_replacement_d3_150(ct_replacement_d2_150):
    feature = _clean(ct_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_150'] = {'inputs': ['ct_replacement_d2_150'], 'func': ct_replacement_d3_150}


def ct_replacement_d3_151(ct_replacement_d2_151):
    feature = _clean(ct_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_151'] = {'inputs': ['ct_replacement_d2_151'], 'func': ct_replacement_d3_151}


def ct_replacement_d3_152(ct_replacement_d2_152):
    feature = _clean(ct_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_152'] = {'inputs': ['ct_replacement_d2_152'], 'func': ct_replacement_d3_152}


def ct_replacement_d3_153(ct_replacement_d2_153):
    feature = _clean(ct_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_153'] = {'inputs': ['ct_replacement_d2_153'], 'func': ct_replacement_d3_153}


def ct_replacement_d3_154(ct_replacement_d2_154):
    feature = _clean(ct_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_154'] = {'inputs': ['ct_replacement_d2_154'], 'func': ct_replacement_d3_154}


def ct_replacement_d3_155(ct_replacement_d2_155):
    feature = _clean(ct_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_155'] = {'inputs': ['ct_replacement_d2_155'], 'func': ct_replacement_d3_155}


def ct_replacement_d3_156(ct_replacement_d2_156):
    feature = _clean(ct_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_156'] = {'inputs': ['ct_replacement_d2_156'], 'func': ct_replacement_d3_156}


def ct_replacement_d3_157(ct_replacement_d2_157):
    feature = _clean(ct_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_157'] = {'inputs': ['ct_replacement_d2_157'], 'func': ct_replacement_d3_157}


def ct_replacement_d3_158(ct_replacement_d2_158):
    feature = _clean(ct_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_158'] = {'inputs': ['ct_replacement_d2_158'], 'func': ct_replacement_d3_158}


def ct_replacement_d3_159(ct_replacement_d2_159):
    feature = _clean(ct_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_159'] = {'inputs': ['ct_replacement_d2_159'], 'func': ct_replacement_d3_159}


def ct_replacement_d3_160(ct_replacement_d2_160):
    feature = _clean(ct_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_160'] = {'inputs': ['ct_replacement_d2_160'], 'func': ct_replacement_d3_160}


def ct_replacement_d3_161(ct_replacement_d2_161):
    feature = _clean(ct_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_161'] = {'inputs': ['ct_replacement_d2_161'], 'func': ct_replacement_d3_161}


def ct_replacement_d3_162(ct_replacement_d2_162):
    feature = _clean(ct_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_162'] = {'inputs': ['ct_replacement_d2_162'], 'func': ct_replacement_d3_162}


def ct_replacement_d3_163(ct_replacement_d2_163):
    feature = _clean(ct_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_163'] = {'inputs': ['ct_replacement_d2_163'], 'func': ct_replacement_d3_163}


def ct_replacement_d3_164(ct_replacement_d2_164):
    feature = _clean(ct_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_164'] = {'inputs': ['ct_replacement_d2_164'], 'func': ct_replacement_d3_164}


def ct_replacement_d3_165(ct_replacement_d2_165):
    feature = _clean(ct_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_165'] = {'inputs': ['ct_replacement_d2_165'], 'func': ct_replacement_d3_165}


def ct_replacement_d3_166(ct_replacement_d2_166):
    feature = _clean(ct_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_166'] = {'inputs': ['ct_replacement_d2_166'], 'func': ct_replacement_d3_166}


def ct_replacement_d3_167(ct_replacement_d2_167):
    feature = _clean(ct_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_167'] = {'inputs': ['ct_replacement_d2_167'], 'func': ct_replacement_d3_167}


def ct_replacement_d3_168(ct_replacement_d2_168):
    feature = _clean(ct_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_168'] = {'inputs': ['ct_replacement_d2_168'], 'func': ct_replacement_d3_168}


def ct_replacement_d3_169(ct_replacement_d2_169):
    feature = _clean(ct_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_169'] = {'inputs': ['ct_replacement_d2_169'], 'func': ct_replacement_d3_169}


def ct_replacement_d3_170(ct_replacement_d2_170):
    feature = _clean(ct_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_170'] = {'inputs': ['ct_replacement_d2_170'], 'func': ct_replacement_d3_170}


def ct_replacement_d3_171(ct_replacement_d2_171):
    feature = _clean(ct_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_171'] = {'inputs': ['ct_replacement_d2_171'], 'func': ct_replacement_d3_171}


def ct_replacement_d3_172(ct_replacement_d2_172):
    feature = _clean(ct_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_172'] = {'inputs': ['ct_replacement_d2_172'], 'func': ct_replacement_d3_172}


def ct_replacement_d3_173(ct_replacement_d2_173):
    feature = _clean(ct_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_173'] = {'inputs': ['ct_replacement_d2_173'], 'func': ct_replacement_d3_173}


def ct_replacement_d3_174(ct_replacement_d2_174):
    feature = _clean(ct_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_174'] = {'inputs': ['ct_replacement_d2_174'], 'func': ct_replacement_d3_174}


def ct_replacement_d3_175(ct_replacement_d2_175):
    feature = _clean(ct_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
CT_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['ct_replacement_d3_175'] = {'inputs': ['ct_replacement_d2_175'], 'func': ct_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def cth_base_universe_d3_001_cth_003_loss_streak_21_003(cth_base_universe_d2_001_cth_003_loss_streak_21_003):
    return _base_universe_d3(cth_base_universe_d2_001_cth_003_loss_streak_21_003, 1)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_001_cth_003_loss_streak_21_003'] = {'inputs': ['cth_base_universe_d2_001_cth_003_loss_streak_21_003'], 'func': cth_base_universe_d3_001_cth_003_loss_streak_21_003}


def cth_base_universe_d3_002_cth_004_ma_distance_42_004(cth_base_universe_d2_002_cth_004_ma_distance_42_004):
    return _base_universe_d3(cth_base_universe_d2_002_cth_004_ma_distance_42_004, 2)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_002_cth_004_ma_distance_42_004'] = {'inputs': ['cth_base_universe_d2_002_cth_004_ma_distance_42_004'], 'func': cth_base_universe_d3_002_cth_004_ma_distance_42_004}


def cth_base_universe_d3_003_cth_005_stochastic_position_63_005(cth_base_universe_d2_003_cth_005_stochastic_position_63_005):
    return _base_universe_d3(cth_base_universe_d2_003_cth_005_stochastic_position_63_005, 3)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_003_cth_005_stochastic_position_63_005'] = {'inputs': ['cth_base_universe_d2_003_cth_005_stochastic_position_63_005'], 'func': cth_base_universe_d3_003_cth_005_stochastic_position_63_005}


def cth_base_universe_d3_004_cth_009_loss_streak_252_009(cth_base_universe_d2_004_cth_009_loss_streak_252_009):
    return _base_universe_d3(cth_base_universe_d2_004_cth_009_loss_streak_252_009, 4)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_004_cth_009_loss_streak_252_009'] = {'inputs': ['cth_base_universe_d2_004_cth_009_loss_streak_252_009'], 'func': cth_base_universe_d3_004_cth_009_loss_streak_252_009}


def cth_base_universe_d3_005_cth_010_ma_distance_378_010(cth_base_universe_d2_005_cth_010_ma_distance_378_010):
    return _base_universe_d3(cth_base_universe_d2_005_cth_010_ma_distance_378_010, 5)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_005_cth_010_ma_distance_378_010'] = {'inputs': ['cth_base_universe_d2_005_cth_010_ma_distance_378_010'], 'func': cth_base_universe_d3_005_cth_010_ma_distance_378_010}


def cth_base_universe_d3_006_cth_011_stochastic_position_504_011(cth_base_universe_d2_006_cth_011_stochastic_position_504_011):
    return _base_universe_d3(cth_base_universe_d2_006_cth_011_stochastic_position_504_011, 6)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_006_cth_011_stochastic_position_504_011'] = {'inputs': ['cth_base_universe_d2_006_cth_011_stochastic_position_504_011'], 'func': cth_base_universe_d3_006_cth_011_stochastic_position_504_011}


def cth_base_universe_d3_007_cth_015_loss_streak_1512_015(cth_base_universe_d2_007_cth_015_loss_streak_1512_015):
    return _base_universe_d3(cth_base_universe_d2_007_cth_015_loss_streak_1512_015, 7)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_007_cth_015_loss_streak_1512_015'] = {'inputs': ['cth_base_universe_d2_007_cth_015_loss_streak_1512_015'], 'func': cth_base_universe_d3_007_cth_015_loss_streak_1512_015}


def cth_base_universe_d3_008_cth_016_ma_distance_5_016(cth_base_universe_d2_008_cth_016_ma_distance_5_016):
    return _base_universe_d3(cth_base_universe_d2_008_cth_016_ma_distance_5_016, 8)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_008_cth_016_ma_distance_5_016'] = {'inputs': ['cth_base_universe_d2_008_cth_016_ma_distance_5_016'], 'func': cth_base_universe_d3_008_cth_016_ma_distance_5_016}


def cth_base_universe_d3_009_cth_017_stochastic_position_10_017(cth_base_universe_d2_009_cth_017_stochastic_position_10_017):
    return _base_universe_d3(cth_base_universe_d2_009_cth_017_stochastic_position_10_017, 9)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_009_cth_017_stochastic_position_10_017'] = {'inputs': ['cth_base_universe_d2_009_cth_017_stochastic_position_10_017'], 'func': cth_base_universe_d3_009_cth_017_stochastic_position_10_017}


def cth_base_universe_d3_010_cth_021_loss_streak_84_021(cth_base_universe_d2_010_cth_021_loss_streak_84_021):
    return _base_universe_d3(cth_base_universe_d2_010_cth_021_loss_streak_84_021, 10)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_010_cth_021_loss_streak_84_021'] = {'inputs': ['cth_base_universe_d2_010_cth_021_loss_streak_84_021'], 'func': cth_base_universe_d3_010_cth_021_loss_streak_84_021}


def cth_base_universe_d3_011_cth_022_ma_distance_126_022(cth_base_universe_d2_011_cth_022_ma_distance_126_022):
    return _base_universe_d3(cth_base_universe_d2_011_cth_022_ma_distance_126_022, 11)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_011_cth_022_ma_distance_126_022'] = {'inputs': ['cth_base_universe_d2_011_cth_022_ma_distance_126_022'], 'func': cth_base_universe_d3_011_cth_022_ma_distance_126_022}


def cth_base_universe_d3_012_cth_023_stochastic_position_189_023(cth_base_universe_d2_012_cth_023_stochastic_position_189_023):
    return _base_universe_d3(cth_base_universe_d2_012_cth_023_stochastic_position_189_023, 12)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_012_cth_023_stochastic_position_189_023'] = {'inputs': ['cth_base_universe_d2_012_cth_023_stochastic_position_189_023'], 'func': cth_base_universe_d3_012_cth_023_stochastic_position_189_023}


def cth_base_universe_d3_013_cth_027_loss_streak_756_027(cth_base_universe_d2_013_cth_027_loss_streak_756_027):
    return _base_universe_d3(cth_base_universe_d2_013_cth_027_loss_streak_756_027, 13)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_013_cth_027_loss_streak_756_027'] = {'inputs': ['cth_base_universe_d2_013_cth_027_loss_streak_756_027'], 'func': cth_base_universe_d3_013_cth_027_loss_streak_756_027}


def cth_base_universe_d3_014_cth_028_ma_distance_1008_028(cth_base_universe_d2_014_cth_028_ma_distance_1008_028):
    return _base_universe_d3(cth_base_universe_d2_014_cth_028_ma_distance_1008_028, 14)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_014_cth_028_ma_distance_1008_028'] = {'inputs': ['cth_base_universe_d2_014_cth_028_ma_distance_1008_028'], 'func': cth_base_universe_d3_014_cth_028_ma_distance_1008_028}


def cth_base_universe_d3_015_cth_029_stochastic_position_1260_029(cth_base_universe_d2_015_cth_029_stochastic_position_1260_029):
    return _base_universe_d3(cth_base_universe_d2_015_cth_029_stochastic_position_1260_029, 15)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_015_cth_029_stochastic_position_1260_029'] = {'inputs': ['cth_base_universe_d2_015_cth_029_stochastic_position_1260_029'], 'func': cth_base_universe_d3_015_cth_029_stochastic_position_1260_029}


def cth_base_universe_d3_016_cth_basefill_001(cth_base_universe_d2_016_cth_basefill_001):
    return _base_universe_d3(cth_base_universe_d2_016_cth_basefill_001, 16)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_016_cth_basefill_001'] = {'inputs': ['cth_base_universe_d2_016_cth_basefill_001'], 'func': cth_base_universe_d3_016_cth_basefill_001}


def cth_base_universe_d3_017_cth_basefill_002(cth_base_universe_d2_017_cth_basefill_002):
    return _base_universe_d3(cth_base_universe_d2_017_cth_basefill_002, 17)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_017_cth_basefill_002'] = {'inputs': ['cth_base_universe_d2_017_cth_basefill_002'], 'func': cth_base_universe_d3_017_cth_basefill_002}


def cth_base_universe_d3_018_cth_basefill_006(cth_base_universe_d2_018_cth_basefill_006):
    return _base_universe_d3(cth_base_universe_d2_018_cth_basefill_006, 18)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_018_cth_basefill_006'] = {'inputs': ['cth_base_universe_d2_018_cth_basefill_006'], 'func': cth_base_universe_d3_018_cth_basefill_006}


def cth_base_universe_d3_019_cth_basefill_007(cth_base_universe_d2_019_cth_basefill_007):
    return _base_universe_d3(cth_base_universe_d2_019_cth_basefill_007, 19)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_019_cth_basefill_007'] = {'inputs': ['cth_base_universe_d2_019_cth_basefill_007'], 'func': cth_base_universe_d3_019_cth_basefill_007}


def cth_base_universe_d3_020_cth_basefill_008(cth_base_universe_d2_020_cth_basefill_008):
    return _base_universe_d3(cth_base_universe_d2_020_cth_basefill_008, 20)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_020_cth_basefill_008'] = {'inputs': ['cth_base_universe_d2_020_cth_basefill_008'], 'func': cth_base_universe_d3_020_cth_basefill_008}


def cth_base_universe_d3_021_cth_basefill_012(cth_base_universe_d2_021_cth_basefill_012):
    return _base_universe_d3(cth_base_universe_d2_021_cth_basefill_012, 21)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_021_cth_basefill_012'] = {'inputs': ['cth_base_universe_d2_021_cth_basefill_012'], 'func': cth_base_universe_d3_021_cth_basefill_012}


def cth_base_universe_d3_022_cth_basefill_013(cth_base_universe_d2_022_cth_basefill_013):
    return _base_universe_d3(cth_base_universe_d2_022_cth_basefill_013, 22)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_022_cth_basefill_013'] = {'inputs': ['cth_base_universe_d2_022_cth_basefill_013'], 'func': cth_base_universe_d3_022_cth_basefill_013}


def cth_base_universe_d3_023_cth_basefill_014(cth_base_universe_d2_023_cth_basefill_014):
    return _base_universe_d3(cth_base_universe_d2_023_cth_basefill_014, 23)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_023_cth_basefill_014'] = {'inputs': ['cth_base_universe_d2_023_cth_basefill_014'], 'func': cth_base_universe_d3_023_cth_basefill_014}


def cth_base_universe_d3_024_cth_basefill_018(cth_base_universe_d2_024_cth_basefill_018):
    return _base_universe_d3(cth_base_universe_d2_024_cth_basefill_018, 24)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_024_cth_basefill_018'] = {'inputs': ['cth_base_universe_d2_024_cth_basefill_018'], 'func': cth_base_universe_d3_024_cth_basefill_018}


def cth_base_universe_d3_025_cth_basefill_019(cth_base_universe_d2_025_cth_basefill_019):
    return _base_universe_d3(cth_base_universe_d2_025_cth_basefill_019, 25)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_025_cth_basefill_019'] = {'inputs': ['cth_base_universe_d2_025_cth_basefill_019'], 'func': cth_base_universe_d3_025_cth_basefill_019}


def cth_base_universe_d3_026_cth_basefill_020(cth_base_universe_d2_026_cth_basefill_020):
    return _base_universe_d3(cth_base_universe_d2_026_cth_basefill_020, 26)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_026_cth_basefill_020'] = {'inputs': ['cth_base_universe_d2_026_cth_basefill_020'], 'func': cth_base_universe_d3_026_cth_basefill_020}


def cth_base_universe_d3_027_cth_basefill_024(cth_base_universe_d2_027_cth_basefill_024):
    return _base_universe_d3(cth_base_universe_d2_027_cth_basefill_024, 27)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_027_cth_basefill_024'] = {'inputs': ['cth_base_universe_d2_027_cth_basefill_024'], 'func': cth_base_universe_d3_027_cth_basefill_024}


def cth_base_universe_d3_028_cth_basefill_025(cth_base_universe_d2_028_cth_basefill_025):
    return _base_universe_d3(cth_base_universe_d2_028_cth_basefill_025, 28)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_028_cth_basefill_025'] = {'inputs': ['cth_base_universe_d2_028_cth_basefill_025'], 'func': cth_base_universe_d3_028_cth_basefill_025}


def cth_base_universe_d3_029_cth_basefill_026(cth_base_universe_d2_029_cth_basefill_026):
    return _base_universe_d3(cth_base_universe_d2_029_cth_basefill_026, 29)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_029_cth_basefill_026'] = {'inputs': ['cth_base_universe_d2_029_cth_basefill_026'], 'func': cth_base_universe_d3_029_cth_basefill_026}


def cth_base_universe_d3_030_cth_basefill_030(cth_base_universe_d2_030_cth_basefill_030):
    return _base_universe_d3(cth_base_universe_d2_030_cth_basefill_030, 30)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_030_cth_basefill_030'] = {'inputs': ['cth_base_universe_d2_030_cth_basefill_030'], 'func': cth_base_universe_d3_030_cth_basefill_030}


def cth_base_universe_d3_031_cth_basefill_031(cth_base_universe_d2_031_cth_basefill_031):
    return _base_universe_d3(cth_base_universe_d2_031_cth_basefill_031, 31)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_031_cth_basefill_031'] = {'inputs': ['cth_base_universe_d2_031_cth_basefill_031'], 'func': cth_base_universe_d3_031_cth_basefill_031}


def cth_base_universe_d3_032_cth_basefill_032(cth_base_universe_d2_032_cth_basefill_032):
    return _base_universe_d3(cth_base_universe_d2_032_cth_basefill_032, 32)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_032_cth_basefill_032'] = {'inputs': ['cth_base_universe_d2_032_cth_basefill_032'], 'func': cth_base_universe_d3_032_cth_basefill_032}


def cth_base_universe_d3_033_cth_basefill_033(cth_base_universe_d2_033_cth_basefill_033):
    return _base_universe_d3(cth_base_universe_d2_033_cth_basefill_033, 33)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_033_cth_basefill_033'] = {'inputs': ['cth_base_universe_d2_033_cth_basefill_033'], 'func': cth_base_universe_d3_033_cth_basefill_033}


def cth_base_universe_d3_034_cth_basefill_034(cth_base_universe_d2_034_cth_basefill_034):
    return _base_universe_d3(cth_base_universe_d2_034_cth_basefill_034, 34)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_034_cth_basefill_034'] = {'inputs': ['cth_base_universe_d2_034_cth_basefill_034'], 'func': cth_base_universe_d3_034_cth_basefill_034}


def cth_base_universe_d3_035_cth_basefill_035(cth_base_universe_d2_035_cth_basefill_035):
    return _base_universe_d3(cth_base_universe_d2_035_cth_basefill_035, 35)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_035_cth_basefill_035'] = {'inputs': ['cth_base_universe_d2_035_cth_basefill_035'], 'func': cth_base_universe_d3_035_cth_basefill_035}


def cth_base_universe_d3_036_cth_basefill_036(cth_base_universe_d2_036_cth_basefill_036):
    return _base_universe_d3(cth_base_universe_d2_036_cth_basefill_036, 36)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_036_cth_basefill_036'] = {'inputs': ['cth_base_universe_d2_036_cth_basefill_036'], 'func': cth_base_universe_d3_036_cth_basefill_036}


def cth_base_universe_d3_037_cth_basefill_037(cth_base_universe_d2_037_cth_basefill_037):
    return _base_universe_d3(cth_base_universe_d2_037_cth_basefill_037, 37)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_037_cth_basefill_037'] = {'inputs': ['cth_base_universe_d2_037_cth_basefill_037'], 'func': cth_base_universe_d3_037_cth_basefill_037}


def cth_base_universe_d3_038_cth_basefill_038(cth_base_universe_d2_038_cth_basefill_038):
    return _base_universe_d3(cth_base_universe_d2_038_cth_basefill_038, 38)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_038_cth_basefill_038'] = {'inputs': ['cth_base_universe_d2_038_cth_basefill_038'], 'func': cth_base_universe_d3_038_cth_basefill_038}


def cth_base_universe_d3_039_cth_basefill_039(cth_base_universe_d2_039_cth_basefill_039):
    return _base_universe_d3(cth_base_universe_d2_039_cth_basefill_039, 39)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_039_cth_basefill_039'] = {'inputs': ['cth_base_universe_d2_039_cth_basefill_039'], 'func': cth_base_universe_d3_039_cth_basefill_039}


def cth_base_universe_d3_040_cth_basefill_040(cth_base_universe_d2_040_cth_basefill_040):
    return _base_universe_d3(cth_base_universe_d2_040_cth_basefill_040, 40)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_040_cth_basefill_040'] = {'inputs': ['cth_base_universe_d2_040_cth_basefill_040'], 'func': cth_base_universe_d3_040_cth_basefill_040}


def cth_base_universe_d3_041_cth_basefill_041(cth_base_universe_d2_041_cth_basefill_041):
    return _base_universe_d3(cth_base_universe_d2_041_cth_basefill_041, 41)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_041_cth_basefill_041'] = {'inputs': ['cth_base_universe_d2_041_cth_basefill_041'], 'func': cth_base_universe_d3_041_cth_basefill_041}


def cth_base_universe_d3_042_cth_basefill_042(cth_base_universe_d2_042_cth_basefill_042):
    return _base_universe_d3(cth_base_universe_d2_042_cth_basefill_042, 42)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_042_cth_basefill_042'] = {'inputs': ['cth_base_universe_d2_042_cth_basefill_042'], 'func': cth_base_universe_d3_042_cth_basefill_042}


def cth_base_universe_d3_043_cth_basefill_043(cth_base_universe_d2_043_cth_basefill_043):
    return _base_universe_d3(cth_base_universe_d2_043_cth_basefill_043, 43)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_043_cth_basefill_043'] = {'inputs': ['cth_base_universe_d2_043_cth_basefill_043'], 'func': cth_base_universe_d3_043_cth_basefill_043}


def cth_base_universe_d3_044_cth_basefill_044(cth_base_universe_d2_044_cth_basefill_044):
    return _base_universe_d3(cth_base_universe_d2_044_cth_basefill_044, 44)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_044_cth_basefill_044'] = {'inputs': ['cth_base_universe_d2_044_cth_basefill_044'], 'func': cth_base_universe_d3_044_cth_basefill_044}


def cth_base_universe_d3_045_cth_basefill_045(cth_base_universe_d2_045_cth_basefill_045):
    return _base_universe_d3(cth_base_universe_d2_045_cth_basefill_045, 45)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_045_cth_basefill_045'] = {'inputs': ['cth_base_universe_d2_045_cth_basefill_045'], 'func': cth_base_universe_d3_045_cth_basefill_045}


def cth_base_universe_d3_046_cth_basefill_046(cth_base_universe_d2_046_cth_basefill_046):
    return _base_universe_d3(cth_base_universe_d2_046_cth_basefill_046, 46)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_046_cth_basefill_046'] = {'inputs': ['cth_base_universe_d2_046_cth_basefill_046'], 'func': cth_base_universe_d3_046_cth_basefill_046}


def cth_base_universe_d3_047_cth_basefill_047(cth_base_universe_d2_047_cth_basefill_047):
    return _base_universe_d3(cth_base_universe_d2_047_cth_basefill_047, 47)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_047_cth_basefill_047'] = {'inputs': ['cth_base_universe_d2_047_cth_basefill_047'], 'func': cth_base_universe_d3_047_cth_basefill_047}


def cth_base_universe_d3_048_cth_basefill_048(cth_base_universe_d2_048_cth_basefill_048):
    return _base_universe_d3(cth_base_universe_d2_048_cth_basefill_048, 48)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_048_cth_basefill_048'] = {'inputs': ['cth_base_universe_d2_048_cth_basefill_048'], 'func': cth_base_universe_d3_048_cth_basefill_048}


def cth_base_universe_d3_049_cth_basefill_049(cth_base_universe_d2_049_cth_basefill_049):
    return _base_universe_d3(cth_base_universe_d2_049_cth_basefill_049, 49)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_049_cth_basefill_049'] = {'inputs': ['cth_base_universe_d2_049_cth_basefill_049'], 'func': cth_base_universe_d3_049_cth_basefill_049}


def cth_base_universe_d3_050_cth_basefill_050(cth_base_universe_d2_050_cth_basefill_050):
    return _base_universe_d3(cth_base_universe_d2_050_cth_basefill_050, 50)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_050_cth_basefill_050'] = {'inputs': ['cth_base_universe_d2_050_cth_basefill_050'], 'func': cth_base_universe_d3_050_cth_basefill_050}


def cth_base_universe_d3_051_cth_basefill_051(cth_base_universe_d2_051_cth_basefill_051):
    return _base_universe_d3(cth_base_universe_d2_051_cth_basefill_051, 51)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_051_cth_basefill_051'] = {'inputs': ['cth_base_universe_d2_051_cth_basefill_051'], 'func': cth_base_universe_d3_051_cth_basefill_051}


def cth_base_universe_d3_052_cth_basefill_052(cth_base_universe_d2_052_cth_basefill_052):
    return _base_universe_d3(cth_base_universe_d2_052_cth_basefill_052, 52)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_052_cth_basefill_052'] = {'inputs': ['cth_base_universe_d2_052_cth_basefill_052'], 'func': cth_base_universe_d3_052_cth_basefill_052}


def cth_base_universe_d3_053_cth_basefill_053(cth_base_universe_d2_053_cth_basefill_053):
    return _base_universe_d3(cth_base_universe_d2_053_cth_basefill_053, 53)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_053_cth_basefill_053'] = {'inputs': ['cth_base_universe_d2_053_cth_basefill_053'], 'func': cth_base_universe_d3_053_cth_basefill_053}


def cth_base_universe_d3_054_cth_basefill_054(cth_base_universe_d2_054_cth_basefill_054):
    return _base_universe_d3(cth_base_universe_d2_054_cth_basefill_054, 54)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_054_cth_basefill_054'] = {'inputs': ['cth_base_universe_d2_054_cth_basefill_054'], 'func': cth_base_universe_d3_054_cth_basefill_054}


def cth_base_universe_d3_055_cth_basefill_055(cth_base_universe_d2_055_cth_basefill_055):
    return _base_universe_d3(cth_base_universe_d2_055_cth_basefill_055, 55)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_055_cth_basefill_055'] = {'inputs': ['cth_base_universe_d2_055_cth_basefill_055'], 'func': cth_base_universe_d3_055_cth_basefill_055}


def cth_base_universe_d3_056_cth_basefill_056(cth_base_universe_d2_056_cth_basefill_056):
    return _base_universe_d3(cth_base_universe_d2_056_cth_basefill_056, 56)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_056_cth_basefill_056'] = {'inputs': ['cth_base_universe_d2_056_cth_basefill_056'], 'func': cth_base_universe_d3_056_cth_basefill_056}


def cth_base_universe_d3_057_cth_basefill_057(cth_base_universe_d2_057_cth_basefill_057):
    return _base_universe_d3(cth_base_universe_d2_057_cth_basefill_057, 57)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_057_cth_basefill_057'] = {'inputs': ['cth_base_universe_d2_057_cth_basefill_057'], 'func': cth_base_universe_d3_057_cth_basefill_057}


def cth_base_universe_d3_058_cth_basefill_058(cth_base_universe_d2_058_cth_basefill_058):
    return _base_universe_d3(cth_base_universe_d2_058_cth_basefill_058, 58)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_058_cth_basefill_058'] = {'inputs': ['cth_base_universe_d2_058_cth_basefill_058'], 'func': cth_base_universe_d3_058_cth_basefill_058}


def cth_base_universe_d3_059_cth_basefill_059(cth_base_universe_d2_059_cth_basefill_059):
    return _base_universe_d3(cth_base_universe_d2_059_cth_basefill_059, 59)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_059_cth_basefill_059'] = {'inputs': ['cth_base_universe_d2_059_cth_basefill_059'], 'func': cth_base_universe_d3_059_cth_basefill_059}


def cth_base_universe_d3_060_cth_basefill_060(cth_base_universe_d2_060_cth_basefill_060):
    return _base_universe_d3(cth_base_universe_d2_060_cth_basefill_060, 60)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_060_cth_basefill_060'] = {'inputs': ['cth_base_universe_d2_060_cth_basefill_060'], 'func': cth_base_universe_d3_060_cth_basefill_060}


def cth_base_universe_d3_061_cth_basefill_061(cth_base_universe_d2_061_cth_basefill_061):
    return _base_universe_d3(cth_base_universe_d2_061_cth_basefill_061, 61)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_061_cth_basefill_061'] = {'inputs': ['cth_base_universe_d2_061_cth_basefill_061'], 'func': cth_base_universe_d3_061_cth_basefill_061}


def cth_base_universe_d3_062_cth_basefill_062(cth_base_universe_d2_062_cth_basefill_062):
    return _base_universe_d3(cth_base_universe_d2_062_cth_basefill_062, 62)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_062_cth_basefill_062'] = {'inputs': ['cth_base_universe_d2_062_cth_basefill_062'], 'func': cth_base_universe_d3_062_cth_basefill_062}


def cth_base_universe_d3_063_cth_basefill_063(cth_base_universe_d2_063_cth_basefill_063):
    return _base_universe_d3(cth_base_universe_d2_063_cth_basefill_063, 63)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_063_cth_basefill_063'] = {'inputs': ['cth_base_universe_d2_063_cth_basefill_063'], 'func': cth_base_universe_d3_063_cth_basefill_063}


def cth_base_universe_d3_064_cth_basefill_064(cth_base_universe_d2_064_cth_basefill_064):
    return _base_universe_d3(cth_base_universe_d2_064_cth_basefill_064, 64)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_064_cth_basefill_064'] = {'inputs': ['cth_base_universe_d2_064_cth_basefill_064'], 'func': cth_base_universe_d3_064_cth_basefill_064}


def cth_base_universe_d3_065_cth_basefill_065(cth_base_universe_d2_065_cth_basefill_065):
    return _base_universe_d3(cth_base_universe_d2_065_cth_basefill_065, 65)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_065_cth_basefill_065'] = {'inputs': ['cth_base_universe_d2_065_cth_basefill_065'], 'func': cth_base_universe_d3_065_cth_basefill_065}


def cth_base_universe_d3_066_cth_basefill_066(cth_base_universe_d2_066_cth_basefill_066):
    return _base_universe_d3(cth_base_universe_d2_066_cth_basefill_066, 66)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_066_cth_basefill_066'] = {'inputs': ['cth_base_universe_d2_066_cth_basefill_066'], 'func': cth_base_universe_d3_066_cth_basefill_066}


def cth_base_universe_d3_067_cth_basefill_067(cth_base_universe_d2_067_cth_basefill_067):
    return _base_universe_d3(cth_base_universe_d2_067_cth_basefill_067, 67)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_067_cth_basefill_067'] = {'inputs': ['cth_base_universe_d2_067_cth_basefill_067'], 'func': cth_base_universe_d3_067_cth_basefill_067}


def cth_base_universe_d3_068_cth_basefill_068(cth_base_universe_d2_068_cth_basefill_068):
    return _base_universe_d3(cth_base_universe_d2_068_cth_basefill_068, 68)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_068_cth_basefill_068'] = {'inputs': ['cth_base_universe_d2_068_cth_basefill_068'], 'func': cth_base_universe_d3_068_cth_basefill_068}


def cth_base_universe_d3_069_cth_basefill_069(cth_base_universe_d2_069_cth_basefill_069):
    return _base_universe_d3(cth_base_universe_d2_069_cth_basefill_069, 69)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_069_cth_basefill_069'] = {'inputs': ['cth_base_universe_d2_069_cth_basefill_069'], 'func': cth_base_universe_d3_069_cth_basefill_069}


def cth_base_universe_d3_070_cth_basefill_070(cth_base_universe_d2_070_cth_basefill_070):
    return _base_universe_d3(cth_base_universe_d2_070_cth_basefill_070, 70)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_070_cth_basefill_070'] = {'inputs': ['cth_base_universe_d2_070_cth_basefill_070'], 'func': cth_base_universe_d3_070_cth_basefill_070}


def cth_base_universe_d3_071_cth_basefill_071(cth_base_universe_d2_071_cth_basefill_071):
    return _base_universe_d3(cth_base_universe_d2_071_cth_basefill_071, 71)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_071_cth_basefill_071'] = {'inputs': ['cth_base_universe_d2_071_cth_basefill_071'], 'func': cth_base_universe_d3_071_cth_basefill_071}


def cth_base_universe_d3_072_cth_basefill_072(cth_base_universe_d2_072_cth_basefill_072):
    return _base_universe_d3(cth_base_universe_d2_072_cth_basefill_072, 72)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_072_cth_basefill_072'] = {'inputs': ['cth_base_universe_d2_072_cth_basefill_072'], 'func': cth_base_universe_d3_072_cth_basefill_072}


def cth_base_universe_d3_073_cth_basefill_073(cth_base_universe_d2_073_cth_basefill_073):
    return _base_universe_d3(cth_base_universe_d2_073_cth_basefill_073, 73)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_073_cth_basefill_073'] = {'inputs': ['cth_base_universe_d2_073_cth_basefill_073'], 'func': cth_base_universe_d3_073_cth_basefill_073}


def cth_base_universe_d3_074_cth_basefill_074(cth_base_universe_d2_074_cth_basefill_074):
    return _base_universe_d3(cth_base_universe_d2_074_cth_basefill_074, 74)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_074_cth_basefill_074'] = {'inputs': ['cth_base_universe_d2_074_cth_basefill_074'], 'func': cth_base_universe_d3_074_cth_basefill_074}


def cth_base_universe_d3_075_cth_basefill_075(cth_base_universe_d2_075_cth_basefill_075):
    return _base_universe_d3(cth_base_universe_d2_075_cth_basefill_075, 75)
CTH_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['cth_base_universe_d3_075_cth_basefill_075'] = {'inputs': ['cth_base_universe_d2_075_cth_basefill_075'], 'func': cth_base_universe_d3_075_cth_basefill_075}
