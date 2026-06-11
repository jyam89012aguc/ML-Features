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



def mex_001_return_decay_accel_1(mex_001_return_decay_roc_1):
    feature = _s(mex_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def mex_007_return_decay_accel_5(mex_007_return_decay_roc_5):
    feature = _s(mex_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def mex_013_return_decay_accel_42(mex_013_return_decay_roc_42):
    feature = _s(mex_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def mex_179_mex_019_return_decay_42_019_accel_126(mex_154_mex_019_return_decay_42_019_roc_126):
    feature = _s(mex_154_mex_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def mex_180_mex_025_return_decay_5_025_accel_378(mex_155_mex_025_return_decay_5_025_roc_378):
    feature = _s(mex_155_mex_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















MOMENTUM_EXHAUSTION_REGISTRY_3RD_DERIVATIVES = {
    'mex_001_return_decay_accel_1': {'inputs': ['mex_001_return_decay_roc_1'], 'func': mex_001_return_decay_accel_1},
    'mex_007_return_decay_accel_5': {'inputs': ['mex_007_return_decay_roc_5'], 'func': mex_007_return_decay_accel_5},
    'mex_013_return_decay_accel_42': {'inputs': ['mex_013_return_decay_roc_42'], 'func': mex_013_return_decay_accel_42},
    'mex_179_mex_019_return_decay_42_019_accel_126': {'inputs': ['mex_154_mex_019_return_decay_42_019_roc_126'], 'func': mex_179_mex_019_return_decay_42_019_accel_126},
    'mex_180_mex_025_return_decay_5_025_accel_378': {'inputs': ['mex_155_mex_025_return_decay_5_025_roc_378'], 'func': mex_180_mex_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def me_replacement_d3_001(me_replacement_d2_001):
    feature = _clean(me_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_001'] = {'inputs': ['me_replacement_d2_001'], 'func': me_replacement_d3_001}


def me_replacement_d3_002(me_replacement_d2_002):
    feature = _clean(me_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_002'] = {'inputs': ['me_replacement_d2_002'], 'func': me_replacement_d3_002}


def me_replacement_d3_003(me_replacement_d2_003):
    feature = _clean(me_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_003'] = {'inputs': ['me_replacement_d2_003'], 'func': me_replacement_d3_003}


def me_replacement_d3_004(me_replacement_d2_004):
    feature = _clean(me_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_004'] = {'inputs': ['me_replacement_d2_004'], 'func': me_replacement_d3_004}


def me_replacement_d3_005(me_replacement_d2_005):
    feature = _clean(me_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_005'] = {'inputs': ['me_replacement_d2_005'], 'func': me_replacement_d3_005}


def me_replacement_d3_006(me_replacement_d2_006):
    feature = _clean(me_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_006'] = {'inputs': ['me_replacement_d2_006'], 'func': me_replacement_d3_006}


def me_replacement_d3_007(me_replacement_d2_007):
    feature = _clean(me_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_007'] = {'inputs': ['me_replacement_d2_007'], 'func': me_replacement_d3_007}


def me_replacement_d3_008(me_replacement_d2_008):
    feature = _clean(me_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_008'] = {'inputs': ['me_replacement_d2_008'], 'func': me_replacement_d3_008}


def me_replacement_d3_009(me_replacement_d2_009):
    feature = _clean(me_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_009'] = {'inputs': ['me_replacement_d2_009'], 'func': me_replacement_d3_009}


def me_replacement_d3_010(me_replacement_d2_010):
    feature = _clean(me_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_010'] = {'inputs': ['me_replacement_d2_010'], 'func': me_replacement_d3_010}


def me_replacement_d3_011(me_replacement_d2_011):
    feature = _clean(me_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_011'] = {'inputs': ['me_replacement_d2_011'], 'func': me_replacement_d3_011}


def me_replacement_d3_012(me_replacement_d2_012):
    feature = _clean(me_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_012'] = {'inputs': ['me_replacement_d2_012'], 'func': me_replacement_d3_012}


def me_replacement_d3_013(me_replacement_d2_013):
    feature = _clean(me_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_013'] = {'inputs': ['me_replacement_d2_013'], 'func': me_replacement_d3_013}


def me_replacement_d3_014(me_replacement_d2_014):
    feature = _clean(me_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_014'] = {'inputs': ['me_replacement_d2_014'], 'func': me_replacement_d3_014}


def me_replacement_d3_015(me_replacement_d2_015):
    feature = _clean(me_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_015'] = {'inputs': ['me_replacement_d2_015'], 'func': me_replacement_d3_015}


def me_replacement_d3_016(me_replacement_d2_016):
    feature = _clean(me_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_016'] = {'inputs': ['me_replacement_d2_016'], 'func': me_replacement_d3_016}


def me_replacement_d3_017(me_replacement_d2_017):
    feature = _clean(me_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_017'] = {'inputs': ['me_replacement_d2_017'], 'func': me_replacement_d3_017}


def me_replacement_d3_018(me_replacement_d2_018):
    feature = _clean(me_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_018'] = {'inputs': ['me_replacement_d2_018'], 'func': me_replacement_d3_018}


def me_replacement_d3_019(me_replacement_d2_019):
    feature = _clean(me_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_019'] = {'inputs': ['me_replacement_d2_019'], 'func': me_replacement_d3_019}


def me_replacement_d3_020(me_replacement_d2_020):
    feature = _clean(me_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_020'] = {'inputs': ['me_replacement_d2_020'], 'func': me_replacement_d3_020}


def me_replacement_d3_021(me_replacement_d2_021):
    feature = _clean(me_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_021'] = {'inputs': ['me_replacement_d2_021'], 'func': me_replacement_d3_021}


def me_replacement_d3_022(me_replacement_d2_022):
    feature = _clean(me_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_022'] = {'inputs': ['me_replacement_d2_022'], 'func': me_replacement_d3_022}


def me_replacement_d3_023(me_replacement_d2_023):
    feature = _clean(me_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_023'] = {'inputs': ['me_replacement_d2_023'], 'func': me_replacement_d3_023}


def me_replacement_d3_024(me_replacement_d2_024):
    feature = _clean(me_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_024'] = {'inputs': ['me_replacement_d2_024'], 'func': me_replacement_d3_024}


def me_replacement_d3_025(me_replacement_d2_025):
    feature = _clean(me_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_025'] = {'inputs': ['me_replacement_d2_025'], 'func': me_replacement_d3_025}


def me_replacement_d3_026(me_replacement_d2_026):
    feature = _clean(me_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_026'] = {'inputs': ['me_replacement_d2_026'], 'func': me_replacement_d3_026}


def me_replacement_d3_027(me_replacement_d2_027):
    feature = _clean(me_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_027'] = {'inputs': ['me_replacement_d2_027'], 'func': me_replacement_d3_027}


def me_replacement_d3_028(me_replacement_d2_028):
    feature = _clean(me_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_028'] = {'inputs': ['me_replacement_d2_028'], 'func': me_replacement_d3_028}


def me_replacement_d3_029(me_replacement_d2_029):
    feature = _clean(me_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_029'] = {'inputs': ['me_replacement_d2_029'], 'func': me_replacement_d3_029}


def me_replacement_d3_030(me_replacement_d2_030):
    feature = _clean(me_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_030'] = {'inputs': ['me_replacement_d2_030'], 'func': me_replacement_d3_030}


def me_replacement_d3_031(me_replacement_d2_031):
    feature = _clean(me_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_031'] = {'inputs': ['me_replacement_d2_031'], 'func': me_replacement_d3_031}


def me_replacement_d3_032(me_replacement_d2_032):
    feature = _clean(me_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_032'] = {'inputs': ['me_replacement_d2_032'], 'func': me_replacement_d3_032}


def me_replacement_d3_033(me_replacement_d2_033):
    feature = _clean(me_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_033'] = {'inputs': ['me_replacement_d2_033'], 'func': me_replacement_d3_033}


def me_replacement_d3_034(me_replacement_d2_034):
    feature = _clean(me_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_034'] = {'inputs': ['me_replacement_d2_034'], 'func': me_replacement_d3_034}


def me_replacement_d3_035(me_replacement_d2_035):
    feature = _clean(me_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_035'] = {'inputs': ['me_replacement_d2_035'], 'func': me_replacement_d3_035}


def me_replacement_d3_036(me_replacement_d2_036):
    feature = _clean(me_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_036'] = {'inputs': ['me_replacement_d2_036'], 'func': me_replacement_d3_036}


def me_replacement_d3_037(me_replacement_d2_037):
    feature = _clean(me_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_037'] = {'inputs': ['me_replacement_d2_037'], 'func': me_replacement_d3_037}


def me_replacement_d3_038(me_replacement_d2_038):
    feature = _clean(me_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_038'] = {'inputs': ['me_replacement_d2_038'], 'func': me_replacement_d3_038}


def me_replacement_d3_039(me_replacement_d2_039):
    feature = _clean(me_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_039'] = {'inputs': ['me_replacement_d2_039'], 'func': me_replacement_d3_039}


def me_replacement_d3_040(me_replacement_d2_040):
    feature = _clean(me_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_040'] = {'inputs': ['me_replacement_d2_040'], 'func': me_replacement_d3_040}


def me_replacement_d3_041(me_replacement_d2_041):
    feature = _clean(me_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_041'] = {'inputs': ['me_replacement_d2_041'], 'func': me_replacement_d3_041}


def me_replacement_d3_042(me_replacement_d2_042):
    feature = _clean(me_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_042'] = {'inputs': ['me_replacement_d2_042'], 'func': me_replacement_d3_042}


def me_replacement_d3_043(me_replacement_d2_043):
    feature = _clean(me_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_043'] = {'inputs': ['me_replacement_d2_043'], 'func': me_replacement_d3_043}


def me_replacement_d3_044(me_replacement_d2_044):
    feature = _clean(me_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_044'] = {'inputs': ['me_replacement_d2_044'], 'func': me_replacement_d3_044}


def me_replacement_d3_045(me_replacement_d2_045):
    feature = _clean(me_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_045'] = {'inputs': ['me_replacement_d2_045'], 'func': me_replacement_d3_045}


def me_replacement_d3_046(me_replacement_d2_046):
    feature = _clean(me_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_046'] = {'inputs': ['me_replacement_d2_046'], 'func': me_replacement_d3_046}


def me_replacement_d3_047(me_replacement_d2_047):
    feature = _clean(me_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_047'] = {'inputs': ['me_replacement_d2_047'], 'func': me_replacement_d3_047}


def me_replacement_d3_048(me_replacement_d2_048):
    feature = _clean(me_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_048'] = {'inputs': ['me_replacement_d2_048'], 'func': me_replacement_d3_048}


def me_replacement_d3_049(me_replacement_d2_049):
    feature = _clean(me_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_049'] = {'inputs': ['me_replacement_d2_049'], 'func': me_replacement_d3_049}


def me_replacement_d3_050(me_replacement_d2_050):
    feature = _clean(me_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_050'] = {'inputs': ['me_replacement_d2_050'], 'func': me_replacement_d3_050}


def me_replacement_d3_051(me_replacement_d2_051):
    feature = _clean(me_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_051'] = {'inputs': ['me_replacement_d2_051'], 'func': me_replacement_d3_051}


def me_replacement_d3_052(me_replacement_d2_052):
    feature = _clean(me_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_052'] = {'inputs': ['me_replacement_d2_052'], 'func': me_replacement_d3_052}


def me_replacement_d3_053(me_replacement_d2_053):
    feature = _clean(me_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_053'] = {'inputs': ['me_replacement_d2_053'], 'func': me_replacement_d3_053}


def me_replacement_d3_054(me_replacement_d2_054):
    feature = _clean(me_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_054'] = {'inputs': ['me_replacement_d2_054'], 'func': me_replacement_d3_054}


def me_replacement_d3_055(me_replacement_d2_055):
    feature = _clean(me_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_055'] = {'inputs': ['me_replacement_d2_055'], 'func': me_replacement_d3_055}


def me_replacement_d3_056(me_replacement_d2_056):
    feature = _clean(me_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_056'] = {'inputs': ['me_replacement_d2_056'], 'func': me_replacement_d3_056}


def me_replacement_d3_057(me_replacement_d2_057):
    feature = _clean(me_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_057'] = {'inputs': ['me_replacement_d2_057'], 'func': me_replacement_d3_057}


def me_replacement_d3_058(me_replacement_d2_058):
    feature = _clean(me_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_058'] = {'inputs': ['me_replacement_d2_058'], 'func': me_replacement_d3_058}


def me_replacement_d3_059(me_replacement_d2_059):
    feature = _clean(me_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_059'] = {'inputs': ['me_replacement_d2_059'], 'func': me_replacement_d3_059}


def me_replacement_d3_060(me_replacement_d2_060):
    feature = _clean(me_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_060'] = {'inputs': ['me_replacement_d2_060'], 'func': me_replacement_d3_060}


def me_replacement_d3_061(me_replacement_d2_061):
    feature = _clean(me_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_061'] = {'inputs': ['me_replacement_d2_061'], 'func': me_replacement_d3_061}


def me_replacement_d3_062(me_replacement_d2_062):
    feature = _clean(me_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_062'] = {'inputs': ['me_replacement_d2_062'], 'func': me_replacement_d3_062}


def me_replacement_d3_063(me_replacement_d2_063):
    feature = _clean(me_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_063'] = {'inputs': ['me_replacement_d2_063'], 'func': me_replacement_d3_063}


def me_replacement_d3_064(me_replacement_d2_064):
    feature = _clean(me_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_064'] = {'inputs': ['me_replacement_d2_064'], 'func': me_replacement_d3_064}


def me_replacement_d3_065(me_replacement_d2_065):
    feature = _clean(me_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_065'] = {'inputs': ['me_replacement_d2_065'], 'func': me_replacement_d3_065}


def me_replacement_d3_066(me_replacement_d2_066):
    feature = _clean(me_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_066'] = {'inputs': ['me_replacement_d2_066'], 'func': me_replacement_d3_066}


def me_replacement_d3_067(me_replacement_d2_067):
    feature = _clean(me_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_067'] = {'inputs': ['me_replacement_d2_067'], 'func': me_replacement_d3_067}


def me_replacement_d3_068(me_replacement_d2_068):
    feature = _clean(me_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_068'] = {'inputs': ['me_replacement_d2_068'], 'func': me_replacement_d3_068}


def me_replacement_d3_069(me_replacement_d2_069):
    feature = _clean(me_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_069'] = {'inputs': ['me_replacement_d2_069'], 'func': me_replacement_d3_069}


def me_replacement_d3_070(me_replacement_d2_070):
    feature = _clean(me_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_070'] = {'inputs': ['me_replacement_d2_070'], 'func': me_replacement_d3_070}


def me_replacement_d3_071(me_replacement_d2_071):
    feature = _clean(me_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_071'] = {'inputs': ['me_replacement_d2_071'], 'func': me_replacement_d3_071}


def me_replacement_d3_072(me_replacement_d2_072):
    feature = _clean(me_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_072'] = {'inputs': ['me_replacement_d2_072'], 'func': me_replacement_d3_072}


def me_replacement_d3_073(me_replacement_d2_073):
    feature = _clean(me_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_073'] = {'inputs': ['me_replacement_d2_073'], 'func': me_replacement_d3_073}


def me_replacement_d3_074(me_replacement_d2_074):
    feature = _clean(me_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_074'] = {'inputs': ['me_replacement_d2_074'], 'func': me_replacement_d3_074}


def me_replacement_d3_075(me_replacement_d2_075):
    feature = _clean(me_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_075'] = {'inputs': ['me_replacement_d2_075'], 'func': me_replacement_d3_075}


def me_replacement_d3_076(me_replacement_d2_076):
    feature = _clean(me_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_076'] = {'inputs': ['me_replacement_d2_076'], 'func': me_replacement_d3_076}


def me_replacement_d3_077(me_replacement_d2_077):
    feature = _clean(me_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_077'] = {'inputs': ['me_replacement_d2_077'], 'func': me_replacement_d3_077}


def me_replacement_d3_078(me_replacement_d2_078):
    feature = _clean(me_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_078'] = {'inputs': ['me_replacement_d2_078'], 'func': me_replacement_d3_078}


def me_replacement_d3_079(me_replacement_d2_079):
    feature = _clean(me_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_079'] = {'inputs': ['me_replacement_d2_079'], 'func': me_replacement_d3_079}


def me_replacement_d3_080(me_replacement_d2_080):
    feature = _clean(me_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_080'] = {'inputs': ['me_replacement_d2_080'], 'func': me_replacement_d3_080}


def me_replacement_d3_081(me_replacement_d2_081):
    feature = _clean(me_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_081'] = {'inputs': ['me_replacement_d2_081'], 'func': me_replacement_d3_081}


def me_replacement_d3_082(me_replacement_d2_082):
    feature = _clean(me_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_082'] = {'inputs': ['me_replacement_d2_082'], 'func': me_replacement_d3_082}


def me_replacement_d3_083(me_replacement_d2_083):
    feature = _clean(me_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_083'] = {'inputs': ['me_replacement_d2_083'], 'func': me_replacement_d3_083}


def me_replacement_d3_084(me_replacement_d2_084):
    feature = _clean(me_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_084'] = {'inputs': ['me_replacement_d2_084'], 'func': me_replacement_d3_084}


def me_replacement_d3_085(me_replacement_d2_085):
    feature = _clean(me_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_085'] = {'inputs': ['me_replacement_d2_085'], 'func': me_replacement_d3_085}


def me_replacement_d3_086(me_replacement_d2_086):
    feature = _clean(me_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_086'] = {'inputs': ['me_replacement_d2_086'], 'func': me_replacement_d3_086}


def me_replacement_d3_087(me_replacement_d2_087):
    feature = _clean(me_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_087'] = {'inputs': ['me_replacement_d2_087'], 'func': me_replacement_d3_087}


def me_replacement_d3_088(me_replacement_d2_088):
    feature = _clean(me_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_088'] = {'inputs': ['me_replacement_d2_088'], 'func': me_replacement_d3_088}


def me_replacement_d3_089(me_replacement_d2_089):
    feature = _clean(me_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_089'] = {'inputs': ['me_replacement_d2_089'], 'func': me_replacement_d3_089}


def me_replacement_d3_090(me_replacement_d2_090):
    feature = _clean(me_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_090'] = {'inputs': ['me_replacement_d2_090'], 'func': me_replacement_d3_090}


def me_replacement_d3_091(me_replacement_d2_091):
    feature = _clean(me_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_091'] = {'inputs': ['me_replacement_d2_091'], 'func': me_replacement_d3_091}


def me_replacement_d3_092(me_replacement_d2_092):
    feature = _clean(me_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_092'] = {'inputs': ['me_replacement_d2_092'], 'func': me_replacement_d3_092}


def me_replacement_d3_093(me_replacement_d2_093):
    feature = _clean(me_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_093'] = {'inputs': ['me_replacement_d2_093'], 'func': me_replacement_d3_093}


def me_replacement_d3_094(me_replacement_d2_094):
    feature = _clean(me_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_094'] = {'inputs': ['me_replacement_d2_094'], 'func': me_replacement_d3_094}


def me_replacement_d3_095(me_replacement_d2_095):
    feature = _clean(me_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_095'] = {'inputs': ['me_replacement_d2_095'], 'func': me_replacement_d3_095}


def me_replacement_d3_096(me_replacement_d2_096):
    feature = _clean(me_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_096'] = {'inputs': ['me_replacement_d2_096'], 'func': me_replacement_d3_096}


def me_replacement_d3_097(me_replacement_d2_097):
    feature = _clean(me_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_097'] = {'inputs': ['me_replacement_d2_097'], 'func': me_replacement_d3_097}


def me_replacement_d3_098(me_replacement_d2_098):
    feature = _clean(me_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_098'] = {'inputs': ['me_replacement_d2_098'], 'func': me_replacement_d3_098}


def me_replacement_d3_099(me_replacement_d2_099):
    feature = _clean(me_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_099'] = {'inputs': ['me_replacement_d2_099'], 'func': me_replacement_d3_099}


def me_replacement_d3_100(me_replacement_d2_100):
    feature = _clean(me_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_100'] = {'inputs': ['me_replacement_d2_100'], 'func': me_replacement_d3_100}


def me_replacement_d3_101(me_replacement_d2_101):
    feature = _clean(me_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_101'] = {'inputs': ['me_replacement_d2_101'], 'func': me_replacement_d3_101}


def me_replacement_d3_102(me_replacement_d2_102):
    feature = _clean(me_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_102'] = {'inputs': ['me_replacement_d2_102'], 'func': me_replacement_d3_102}


def me_replacement_d3_103(me_replacement_d2_103):
    feature = _clean(me_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_103'] = {'inputs': ['me_replacement_d2_103'], 'func': me_replacement_d3_103}


def me_replacement_d3_104(me_replacement_d2_104):
    feature = _clean(me_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_104'] = {'inputs': ['me_replacement_d2_104'], 'func': me_replacement_d3_104}


def me_replacement_d3_105(me_replacement_d2_105):
    feature = _clean(me_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_105'] = {'inputs': ['me_replacement_d2_105'], 'func': me_replacement_d3_105}


def me_replacement_d3_106(me_replacement_d2_106):
    feature = _clean(me_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_106'] = {'inputs': ['me_replacement_d2_106'], 'func': me_replacement_d3_106}


def me_replacement_d3_107(me_replacement_d2_107):
    feature = _clean(me_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_107'] = {'inputs': ['me_replacement_d2_107'], 'func': me_replacement_d3_107}


def me_replacement_d3_108(me_replacement_d2_108):
    feature = _clean(me_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_108'] = {'inputs': ['me_replacement_d2_108'], 'func': me_replacement_d3_108}


def me_replacement_d3_109(me_replacement_d2_109):
    feature = _clean(me_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_109'] = {'inputs': ['me_replacement_d2_109'], 'func': me_replacement_d3_109}


def me_replacement_d3_110(me_replacement_d2_110):
    feature = _clean(me_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_110'] = {'inputs': ['me_replacement_d2_110'], 'func': me_replacement_d3_110}


def me_replacement_d3_111(me_replacement_d2_111):
    feature = _clean(me_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_111'] = {'inputs': ['me_replacement_d2_111'], 'func': me_replacement_d3_111}


def me_replacement_d3_112(me_replacement_d2_112):
    feature = _clean(me_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_112'] = {'inputs': ['me_replacement_d2_112'], 'func': me_replacement_d3_112}


def me_replacement_d3_113(me_replacement_d2_113):
    feature = _clean(me_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_113'] = {'inputs': ['me_replacement_d2_113'], 'func': me_replacement_d3_113}


def me_replacement_d3_114(me_replacement_d2_114):
    feature = _clean(me_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_114'] = {'inputs': ['me_replacement_d2_114'], 'func': me_replacement_d3_114}


def me_replacement_d3_115(me_replacement_d2_115):
    feature = _clean(me_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_115'] = {'inputs': ['me_replacement_d2_115'], 'func': me_replacement_d3_115}


def me_replacement_d3_116(me_replacement_d2_116):
    feature = _clean(me_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_116'] = {'inputs': ['me_replacement_d2_116'], 'func': me_replacement_d3_116}


def me_replacement_d3_117(me_replacement_d2_117):
    feature = _clean(me_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_117'] = {'inputs': ['me_replacement_d2_117'], 'func': me_replacement_d3_117}


def me_replacement_d3_118(me_replacement_d2_118):
    feature = _clean(me_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_118'] = {'inputs': ['me_replacement_d2_118'], 'func': me_replacement_d3_118}


def me_replacement_d3_119(me_replacement_d2_119):
    feature = _clean(me_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_119'] = {'inputs': ['me_replacement_d2_119'], 'func': me_replacement_d3_119}


def me_replacement_d3_120(me_replacement_d2_120):
    feature = _clean(me_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_120'] = {'inputs': ['me_replacement_d2_120'], 'func': me_replacement_d3_120}


def me_replacement_d3_121(me_replacement_d2_121):
    feature = _clean(me_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_121'] = {'inputs': ['me_replacement_d2_121'], 'func': me_replacement_d3_121}


def me_replacement_d3_122(me_replacement_d2_122):
    feature = _clean(me_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_122'] = {'inputs': ['me_replacement_d2_122'], 'func': me_replacement_d3_122}


def me_replacement_d3_123(me_replacement_d2_123):
    feature = _clean(me_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_123'] = {'inputs': ['me_replacement_d2_123'], 'func': me_replacement_d3_123}


def me_replacement_d3_124(me_replacement_d2_124):
    feature = _clean(me_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_124'] = {'inputs': ['me_replacement_d2_124'], 'func': me_replacement_d3_124}


def me_replacement_d3_125(me_replacement_d2_125):
    feature = _clean(me_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_125'] = {'inputs': ['me_replacement_d2_125'], 'func': me_replacement_d3_125}


def me_replacement_d3_126(me_replacement_d2_126):
    feature = _clean(me_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_126'] = {'inputs': ['me_replacement_d2_126'], 'func': me_replacement_d3_126}


def me_replacement_d3_127(me_replacement_d2_127):
    feature = _clean(me_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_127'] = {'inputs': ['me_replacement_d2_127'], 'func': me_replacement_d3_127}


def me_replacement_d3_128(me_replacement_d2_128):
    feature = _clean(me_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_128'] = {'inputs': ['me_replacement_d2_128'], 'func': me_replacement_d3_128}


def me_replacement_d3_129(me_replacement_d2_129):
    feature = _clean(me_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_129'] = {'inputs': ['me_replacement_d2_129'], 'func': me_replacement_d3_129}


def me_replacement_d3_130(me_replacement_d2_130):
    feature = _clean(me_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_130'] = {'inputs': ['me_replacement_d2_130'], 'func': me_replacement_d3_130}


def me_replacement_d3_131(me_replacement_d2_131):
    feature = _clean(me_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_131'] = {'inputs': ['me_replacement_d2_131'], 'func': me_replacement_d3_131}


def me_replacement_d3_132(me_replacement_d2_132):
    feature = _clean(me_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_132'] = {'inputs': ['me_replacement_d2_132'], 'func': me_replacement_d3_132}


def me_replacement_d3_133(me_replacement_d2_133):
    feature = _clean(me_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_133'] = {'inputs': ['me_replacement_d2_133'], 'func': me_replacement_d3_133}


def me_replacement_d3_134(me_replacement_d2_134):
    feature = _clean(me_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_134'] = {'inputs': ['me_replacement_d2_134'], 'func': me_replacement_d3_134}


def me_replacement_d3_135(me_replacement_d2_135):
    feature = _clean(me_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_135'] = {'inputs': ['me_replacement_d2_135'], 'func': me_replacement_d3_135}


def me_replacement_d3_136(me_replacement_d2_136):
    feature = _clean(me_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_136'] = {'inputs': ['me_replacement_d2_136'], 'func': me_replacement_d3_136}


def me_replacement_d3_137(me_replacement_d2_137):
    feature = _clean(me_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_137'] = {'inputs': ['me_replacement_d2_137'], 'func': me_replacement_d3_137}


def me_replacement_d3_138(me_replacement_d2_138):
    feature = _clean(me_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_138'] = {'inputs': ['me_replacement_d2_138'], 'func': me_replacement_d3_138}


def me_replacement_d3_139(me_replacement_d2_139):
    feature = _clean(me_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_139'] = {'inputs': ['me_replacement_d2_139'], 'func': me_replacement_d3_139}


def me_replacement_d3_140(me_replacement_d2_140):
    feature = _clean(me_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_140'] = {'inputs': ['me_replacement_d2_140'], 'func': me_replacement_d3_140}


def me_replacement_d3_141(me_replacement_d2_141):
    feature = _clean(me_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_141'] = {'inputs': ['me_replacement_d2_141'], 'func': me_replacement_d3_141}


def me_replacement_d3_142(me_replacement_d2_142):
    feature = _clean(me_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_142'] = {'inputs': ['me_replacement_d2_142'], 'func': me_replacement_d3_142}


def me_replacement_d3_143(me_replacement_d2_143):
    feature = _clean(me_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_143'] = {'inputs': ['me_replacement_d2_143'], 'func': me_replacement_d3_143}


def me_replacement_d3_144(me_replacement_d2_144):
    feature = _clean(me_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_144'] = {'inputs': ['me_replacement_d2_144'], 'func': me_replacement_d3_144}


def me_replacement_d3_145(me_replacement_d2_145):
    feature = _clean(me_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_145'] = {'inputs': ['me_replacement_d2_145'], 'func': me_replacement_d3_145}


def me_replacement_d3_146(me_replacement_d2_146):
    feature = _clean(me_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_146'] = {'inputs': ['me_replacement_d2_146'], 'func': me_replacement_d3_146}


def me_replacement_d3_147(me_replacement_d2_147):
    feature = _clean(me_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_147'] = {'inputs': ['me_replacement_d2_147'], 'func': me_replacement_d3_147}


def me_replacement_d3_148(me_replacement_d2_148):
    feature = _clean(me_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_148'] = {'inputs': ['me_replacement_d2_148'], 'func': me_replacement_d3_148}


def me_replacement_d3_149(me_replacement_d2_149):
    feature = _clean(me_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_149'] = {'inputs': ['me_replacement_d2_149'], 'func': me_replacement_d3_149}


def me_replacement_d3_150(me_replacement_d2_150):
    feature = _clean(me_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_150'] = {'inputs': ['me_replacement_d2_150'], 'func': me_replacement_d3_150}


def me_replacement_d3_151(me_replacement_d2_151):
    feature = _clean(me_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_151'] = {'inputs': ['me_replacement_d2_151'], 'func': me_replacement_d3_151}


def me_replacement_d3_152(me_replacement_d2_152):
    feature = _clean(me_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_152'] = {'inputs': ['me_replacement_d2_152'], 'func': me_replacement_d3_152}


def me_replacement_d3_153(me_replacement_d2_153):
    feature = _clean(me_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_153'] = {'inputs': ['me_replacement_d2_153'], 'func': me_replacement_d3_153}


def me_replacement_d3_154(me_replacement_d2_154):
    feature = _clean(me_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_154'] = {'inputs': ['me_replacement_d2_154'], 'func': me_replacement_d3_154}


def me_replacement_d3_155(me_replacement_d2_155):
    feature = _clean(me_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_155'] = {'inputs': ['me_replacement_d2_155'], 'func': me_replacement_d3_155}


def me_replacement_d3_156(me_replacement_d2_156):
    feature = _clean(me_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_156'] = {'inputs': ['me_replacement_d2_156'], 'func': me_replacement_d3_156}


def me_replacement_d3_157(me_replacement_d2_157):
    feature = _clean(me_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_157'] = {'inputs': ['me_replacement_d2_157'], 'func': me_replacement_d3_157}


def me_replacement_d3_158(me_replacement_d2_158):
    feature = _clean(me_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_158'] = {'inputs': ['me_replacement_d2_158'], 'func': me_replacement_d3_158}


def me_replacement_d3_159(me_replacement_d2_159):
    feature = _clean(me_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_159'] = {'inputs': ['me_replacement_d2_159'], 'func': me_replacement_d3_159}


def me_replacement_d3_160(me_replacement_d2_160):
    feature = _clean(me_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_160'] = {'inputs': ['me_replacement_d2_160'], 'func': me_replacement_d3_160}


def me_replacement_d3_161(me_replacement_d2_161):
    feature = _clean(me_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_161'] = {'inputs': ['me_replacement_d2_161'], 'func': me_replacement_d3_161}


def me_replacement_d3_162(me_replacement_d2_162):
    feature = _clean(me_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_162'] = {'inputs': ['me_replacement_d2_162'], 'func': me_replacement_d3_162}


def me_replacement_d3_163(me_replacement_d2_163):
    feature = _clean(me_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_163'] = {'inputs': ['me_replacement_d2_163'], 'func': me_replacement_d3_163}


def me_replacement_d3_164(me_replacement_d2_164):
    feature = _clean(me_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_164'] = {'inputs': ['me_replacement_d2_164'], 'func': me_replacement_d3_164}


def me_replacement_d3_165(me_replacement_d2_165):
    feature = _clean(me_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_165'] = {'inputs': ['me_replacement_d2_165'], 'func': me_replacement_d3_165}


def me_replacement_d3_166(me_replacement_d2_166):
    feature = _clean(me_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_166'] = {'inputs': ['me_replacement_d2_166'], 'func': me_replacement_d3_166}


def me_replacement_d3_167(me_replacement_d2_167):
    feature = _clean(me_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_167'] = {'inputs': ['me_replacement_d2_167'], 'func': me_replacement_d3_167}


def me_replacement_d3_168(me_replacement_d2_168):
    feature = _clean(me_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_168'] = {'inputs': ['me_replacement_d2_168'], 'func': me_replacement_d3_168}


def me_replacement_d3_169(me_replacement_d2_169):
    feature = _clean(me_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_169'] = {'inputs': ['me_replacement_d2_169'], 'func': me_replacement_d3_169}


def me_replacement_d3_170(me_replacement_d2_170):
    feature = _clean(me_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_170'] = {'inputs': ['me_replacement_d2_170'], 'func': me_replacement_d3_170}


def me_replacement_d3_171(me_replacement_d2_171):
    feature = _clean(me_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_171'] = {'inputs': ['me_replacement_d2_171'], 'func': me_replacement_d3_171}


def me_replacement_d3_172(me_replacement_d2_172):
    feature = _clean(me_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_172'] = {'inputs': ['me_replacement_d2_172'], 'func': me_replacement_d3_172}


def me_replacement_d3_173(me_replacement_d2_173):
    feature = _clean(me_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_173'] = {'inputs': ['me_replacement_d2_173'], 'func': me_replacement_d3_173}


def me_replacement_d3_174(me_replacement_d2_174):
    feature = _clean(me_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_174'] = {'inputs': ['me_replacement_d2_174'], 'func': me_replacement_d3_174}


def me_replacement_d3_175(me_replacement_d2_175):
    feature = _clean(me_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
ME_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['me_replacement_d3_175'] = {'inputs': ['me_replacement_d2_175'], 'func': me_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mex_base_universe_d3_001_mex_003_loss_streak_21_003(mex_base_universe_d2_001_mex_003_loss_streak_21_003):
    return _base_universe_d3(mex_base_universe_d2_001_mex_003_loss_streak_21_003, 1)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_001_mex_003_loss_streak_21_003'] = {'inputs': ['mex_base_universe_d2_001_mex_003_loss_streak_21_003'], 'func': mex_base_universe_d3_001_mex_003_loss_streak_21_003}


def mex_base_universe_d3_002_mex_004_ma_distance_42_004(mex_base_universe_d2_002_mex_004_ma_distance_42_004):
    return _base_universe_d3(mex_base_universe_d2_002_mex_004_ma_distance_42_004, 2)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_002_mex_004_ma_distance_42_004'] = {'inputs': ['mex_base_universe_d2_002_mex_004_ma_distance_42_004'], 'func': mex_base_universe_d3_002_mex_004_ma_distance_42_004}


def mex_base_universe_d3_003_mex_005_stochastic_position_63_005(mex_base_universe_d2_003_mex_005_stochastic_position_63_005):
    return _base_universe_d3(mex_base_universe_d2_003_mex_005_stochastic_position_63_005, 3)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_003_mex_005_stochastic_position_63_005'] = {'inputs': ['mex_base_universe_d2_003_mex_005_stochastic_position_63_005'], 'func': mex_base_universe_d3_003_mex_005_stochastic_position_63_005}


def mex_base_universe_d3_004_mex_009_loss_streak_252_009(mex_base_universe_d2_004_mex_009_loss_streak_252_009):
    return _base_universe_d3(mex_base_universe_d2_004_mex_009_loss_streak_252_009, 4)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_004_mex_009_loss_streak_252_009'] = {'inputs': ['mex_base_universe_d2_004_mex_009_loss_streak_252_009'], 'func': mex_base_universe_d3_004_mex_009_loss_streak_252_009}


def mex_base_universe_d3_005_mex_010_ma_distance_378_010(mex_base_universe_d2_005_mex_010_ma_distance_378_010):
    return _base_universe_d3(mex_base_universe_d2_005_mex_010_ma_distance_378_010, 5)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_005_mex_010_ma_distance_378_010'] = {'inputs': ['mex_base_universe_d2_005_mex_010_ma_distance_378_010'], 'func': mex_base_universe_d3_005_mex_010_ma_distance_378_010}


def mex_base_universe_d3_006_mex_011_stochastic_position_504_011(mex_base_universe_d2_006_mex_011_stochastic_position_504_011):
    return _base_universe_d3(mex_base_universe_d2_006_mex_011_stochastic_position_504_011, 6)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_006_mex_011_stochastic_position_504_011'] = {'inputs': ['mex_base_universe_d2_006_mex_011_stochastic_position_504_011'], 'func': mex_base_universe_d3_006_mex_011_stochastic_position_504_011}


def mex_base_universe_d3_007_mex_015_loss_streak_1512_015(mex_base_universe_d2_007_mex_015_loss_streak_1512_015):
    return _base_universe_d3(mex_base_universe_d2_007_mex_015_loss_streak_1512_015, 7)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_007_mex_015_loss_streak_1512_015'] = {'inputs': ['mex_base_universe_d2_007_mex_015_loss_streak_1512_015'], 'func': mex_base_universe_d3_007_mex_015_loss_streak_1512_015}


def mex_base_universe_d3_008_mex_016_ma_distance_5_016(mex_base_universe_d2_008_mex_016_ma_distance_5_016):
    return _base_universe_d3(mex_base_universe_d2_008_mex_016_ma_distance_5_016, 8)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_008_mex_016_ma_distance_5_016'] = {'inputs': ['mex_base_universe_d2_008_mex_016_ma_distance_5_016'], 'func': mex_base_universe_d3_008_mex_016_ma_distance_5_016}


def mex_base_universe_d3_009_mex_017_stochastic_position_10_017(mex_base_universe_d2_009_mex_017_stochastic_position_10_017):
    return _base_universe_d3(mex_base_universe_d2_009_mex_017_stochastic_position_10_017, 9)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_009_mex_017_stochastic_position_10_017'] = {'inputs': ['mex_base_universe_d2_009_mex_017_stochastic_position_10_017'], 'func': mex_base_universe_d3_009_mex_017_stochastic_position_10_017}


def mex_base_universe_d3_010_mex_021_loss_streak_84_021(mex_base_universe_d2_010_mex_021_loss_streak_84_021):
    return _base_universe_d3(mex_base_universe_d2_010_mex_021_loss_streak_84_021, 10)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_010_mex_021_loss_streak_84_021'] = {'inputs': ['mex_base_universe_d2_010_mex_021_loss_streak_84_021'], 'func': mex_base_universe_d3_010_mex_021_loss_streak_84_021}


def mex_base_universe_d3_011_mex_022_ma_distance_126_022(mex_base_universe_d2_011_mex_022_ma_distance_126_022):
    return _base_universe_d3(mex_base_universe_d2_011_mex_022_ma_distance_126_022, 11)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_011_mex_022_ma_distance_126_022'] = {'inputs': ['mex_base_universe_d2_011_mex_022_ma_distance_126_022'], 'func': mex_base_universe_d3_011_mex_022_ma_distance_126_022}


def mex_base_universe_d3_012_mex_023_stochastic_position_189_023(mex_base_universe_d2_012_mex_023_stochastic_position_189_023):
    return _base_universe_d3(mex_base_universe_d2_012_mex_023_stochastic_position_189_023, 12)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_012_mex_023_stochastic_position_189_023'] = {'inputs': ['mex_base_universe_d2_012_mex_023_stochastic_position_189_023'], 'func': mex_base_universe_d3_012_mex_023_stochastic_position_189_023}


def mex_base_universe_d3_013_mex_027_loss_streak_756_027(mex_base_universe_d2_013_mex_027_loss_streak_756_027):
    return _base_universe_d3(mex_base_universe_d2_013_mex_027_loss_streak_756_027, 13)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_013_mex_027_loss_streak_756_027'] = {'inputs': ['mex_base_universe_d2_013_mex_027_loss_streak_756_027'], 'func': mex_base_universe_d3_013_mex_027_loss_streak_756_027}


def mex_base_universe_d3_014_mex_028_ma_distance_1008_028(mex_base_universe_d2_014_mex_028_ma_distance_1008_028):
    return _base_universe_d3(mex_base_universe_d2_014_mex_028_ma_distance_1008_028, 14)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_014_mex_028_ma_distance_1008_028'] = {'inputs': ['mex_base_universe_d2_014_mex_028_ma_distance_1008_028'], 'func': mex_base_universe_d3_014_mex_028_ma_distance_1008_028}


def mex_base_universe_d3_015_mex_029_stochastic_position_1260_029(mex_base_universe_d2_015_mex_029_stochastic_position_1260_029):
    return _base_universe_d3(mex_base_universe_d2_015_mex_029_stochastic_position_1260_029, 15)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_015_mex_029_stochastic_position_1260_029'] = {'inputs': ['mex_base_universe_d2_015_mex_029_stochastic_position_1260_029'], 'func': mex_base_universe_d3_015_mex_029_stochastic_position_1260_029}


def mex_base_universe_d3_016_mex_basefill_001(mex_base_universe_d2_016_mex_basefill_001):
    return _base_universe_d3(mex_base_universe_d2_016_mex_basefill_001, 16)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_016_mex_basefill_001'] = {'inputs': ['mex_base_universe_d2_016_mex_basefill_001'], 'func': mex_base_universe_d3_016_mex_basefill_001}


def mex_base_universe_d3_017_mex_basefill_002(mex_base_universe_d2_017_mex_basefill_002):
    return _base_universe_d3(mex_base_universe_d2_017_mex_basefill_002, 17)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_017_mex_basefill_002'] = {'inputs': ['mex_base_universe_d2_017_mex_basefill_002'], 'func': mex_base_universe_d3_017_mex_basefill_002}


def mex_base_universe_d3_018_mex_basefill_006(mex_base_universe_d2_018_mex_basefill_006):
    return _base_universe_d3(mex_base_universe_d2_018_mex_basefill_006, 18)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_018_mex_basefill_006'] = {'inputs': ['mex_base_universe_d2_018_mex_basefill_006'], 'func': mex_base_universe_d3_018_mex_basefill_006}


def mex_base_universe_d3_019_mex_basefill_007(mex_base_universe_d2_019_mex_basefill_007):
    return _base_universe_d3(mex_base_universe_d2_019_mex_basefill_007, 19)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_019_mex_basefill_007'] = {'inputs': ['mex_base_universe_d2_019_mex_basefill_007'], 'func': mex_base_universe_d3_019_mex_basefill_007}


def mex_base_universe_d3_020_mex_basefill_008(mex_base_universe_d2_020_mex_basefill_008):
    return _base_universe_d3(mex_base_universe_d2_020_mex_basefill_008, 20)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_020_mex_basefill_008'] = {'inputs': ['mex_base_universe_d2_020_mex_basefill_008'], 'func': mex_base_universe_d3_020_mex_basefill_008}


def mex_base_universe_d3_021_mex_basefill_012(mex_base_universe_d2_021_mex_basefill_012):
    return _base_universe_d3(mex_base_universe_d2_021_mex_basefill_012, 21)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_021_mex_basefill_012'] = {'inputs': ['mex_base_universe_d2_021_mex_basefill_012'], 'func': mex_base_universe_d3_021_mex_basefill_012}


def mex_base_universe_d3_022_mex_basefill_013(mex_base_universe_d2_022_mex_basefill_013):
    return _base_universe_d3(mex_base_universe_d2_022_mex_basefill_013, 22)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_022_mex_basefill_013'] = {'inputs': ['mex_base_universe_d2_022_mex_basefill_013'], 'func': mex_base_universe_d3_022_mex_basefill_013}


def mex_base_universe_d3_023_mex_basefill_014(mex_base_universe_d2_023_mex_basefill_014):
    return _base_universe_d3(mex_base_universe_d2_023_mex_basefill_014, 23)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_023_mex_basefill_014'] = {'inputs': ['mex_base_universe_d2_023_mex_basefill_014'], 'func': mex_base_universe_d3_023_mex_basefill_014}


def mex_base_universe_d3_024_mex_basefill_018(mex_base_universe_d2_024_mex_basefill_018):
    return _base_universe_d3(mex_base_universe_d2_024_mex_basefill_018, 24)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_024_mex_basefill_018'] = {'inputs': ['mex_base_universe_d2_024_mex_basefill_018'], 'func': mex_base_universe_d3_024_mex_basefill_018}


def mex_base_universe_d3_025_mex_basefill_019(mex_base_universe_d2_025_mex_basefill_019):
    return _base_universe_d3(mex_base_universe_d2_025_mex_basefill_019, 25)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_025_mex_basefill_019'] = {'inputs': ['mex_base_universe_d2_025_mex_basefill_019'], 'func': mex_base_universe_d3_025_mex_basefill_019}


def mex_base_universe_d3_026_mex_basefill_020(mex_base_universe_d2_026_mex_basefill_020):
    return _base_universe_d3(mex_base_universe_d2_026_mex_basefill_020, 26)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_026_mex_basefill_020'] = {'inputs': ['mex_base_universe_d2_026_mex_basefill_020'], 'func': mex_base_universe_d3_026_mex_basefill_020}


def mex_base_universe_d3_027_mex_basefill_024(mex_base_universe_d2_027_mex_basefill_024):
    return _base_universe_d3(mex_base_universe_d2_027_mex_basefill_024, 27)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_027_mex_basefill_024'] = {'inputs': ['mex_base_universe_d2_027_mex_basefill_024'], 'func': mex_base_universe_d3_027_mex_basefill_024}


def mex_base_universe_d3_028_mex_basefill_025(mex_base_universe_d2_028_mex_basefill_025):
    return _base_universe_d3(mex_base_universe_d2_028_mex_basefill_025, 28)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_028_mex_basefill_025'] = {'inputs': ['mex_base_universe_d2_028_mex_basefill_025'], 'func': mex_base_universe_d3_028_mex_basefill_025}


def mex_base_universe_d3_029_mex_basefill_026(mex_base_universe_d2_029_mex_basefill_026):
    return _base_universe_d3(mex_base_universe_d2_029_mex_basefill_026, 29)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_029_mex_basefill_026'] = {'inputs': ['mex_base_universe_d2_029_mex_basefill_026'], 'func': mex_base_universe_d3_029_mex_basefill_026}


def mex_base_universe_d3_030_mex_basefill_030(mex_base_universe_d2_030_mex_basefill_030):
    return _base_universe_d3(mex_base_universe_d2_030_mex_basefill_030, 30)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_030_mex_basefill_030'] = {'inputs': ['mex_base_universe_d2_030_mex_basefill_030'], 'func': mex_base_universe_d3_030_mex_basefill_030}


def mex_base_universe_d3_031_mex_basefill_031(mex_base_universe_d2_031_mex_basefill_031):
    return _base_universe_d3(mex_base_universe_d2_031_mex_basefill_031, 31)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_031_mex_basefill_031'] = {'inputs': ['mex_base_universe_d2_031_mex_basefill_031'], 'func': mex_base_universe_d3_031_mex_basefill_031}


def mex_base_universe_d3_032_mex_basefill_032(mex_base_universe_d2_032_mex_basefill_032):
    return _base_universe_d3(mex_base_universe_d2_032_mex_basefill_032, 32)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_032_mex_basefill_032'] = {'inputs': ['mex_base_universe_d2_032_mex_basefill_032'], 'func': mex_base_universe_d3_032_mex_basefill_032}


def mex_base_universe_d3_033_mex_basefill_033(mex_base_universe_d2_033_mex_basefill_033):
    return _base_universe_d3(mex_base_universe_d2_033_mex_basefill_033, 33)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_033_mex_basefill_033'] = {'inputs': ['mex_base_universe_d2_033_mex_basefill_033'], 'func': mex_base_universe_d3_033_mex_basefill_033}


def mex_base_universe_d3_034_mex_basefill_034(mex_base_universe_d2_034_mex_basefill_034):
    return _base_universe_d3(mex_base_universe_d2_034_mex_basefill_034, 34)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_034_mex_basefill_034'] = {'inputs': ['mex_base_universe_d2_034_mex_basefill_034'], 'func': mex_base_universe_d3_034_mex_basefill_034}


def mex_base_universe_d3_035_mex_basefill_035(mex_base_universe_d2_035_mex_basefill_035):
    return _base_universe_d3(mex_base_universe_d2_035_mex_basefill_035, 35)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_035_mex_basefill_035'] = {'inputs': ['mex_base_universe_d2_035_mex_basefill_035'], 'func': mex_base_universe_d3_035_mex_basefill_035}


def mex_base_universe_d3_036_mex_basefill_036(mex_base_universe_d2_036_mex_basefill_036):
    return _base_universe_d3(mex_base_universe_d2_036_mex_basefill_036, 36)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_036_mex_basefill_036'] = {'inputs': ['mex_base_universe_d2_036_mex_basefill_036'], 'func': mex_base_universe_d3_036_mex_basefill_036}


def mex_base_universe_d3_037_mex_basefill_037(mex_base_universe_d2_037_mex_basefill_037):
    return _base_universe_d3(mex_base_universe_d2_037_mex_basefill_037, 37)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_037_mex_basefill_037'] = {'inputs': ['mex_base_universe_d2_037_mex_basefill_037'], 'func': mex_base_universe_d3_037_mex_basefill_037}


def mex_base_universe_d3_038_mex_basefill_038(mex_base_universe_d2_038_mex_basefill_038):
    return _base_universe_d3(mex_base_universe_d2_038_mex_basefill_038, 38)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_038_mex_basefill_038'] = {'inputs': ['mex_base_universe_d2_038_mex_basefill_038'], 'func': mex_base_universe_d3_038_mex_basefill_038}


def mex_base_universe_d3_039_mex_basefill_039(mex_base_universe_d2_039_mex_basefill_039):
    return _base_universe_d3(mex_base_universe_d2_039_mex_basefill_039, 39)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_039_mex_basefill_039'] = {'inputs': ['mex_base_universe_d2_039_mex_basefill_039'], 'func': mex_base_universe_d3_039_mex_basefill_039}


def mex_base_universe_d3_040_mex_basefill_040(mex_base_universe_d2_040_mex_basefill_040):
    return _base_universe_d3(mex_base_universe_d2_040_mex_basefill_040, 40)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_040_mex_basefill_040'] = {'inputs': ['mex_base_universe_d2_040_mex_basefill_040'], 'func': mex_base_universe_d3_040_mex_basefill_040}


def mex_base_universe_d3_041_mex_basefill_041(mex_base_universe_d2_041_mex_basefill_041):
    return _base_universe_d3(mex_base_universe_d2_041_mex_basefill_041, 41)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_041_mex_basefill_041'] = {'inputs': ['mex_base_universe_d2_041_mex_basefill_041'], 'func': mex_base_universe_d3_041_mex_basefill_041}


def mex_base_universe_d3_042_mex_basefill_042(mex_base_universe_d2_042_mex_basefill_042):
    return _base_universe_d3(mex_base_universe_d2_042_mex_basefill_042, 42)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_042_mex_basefill_042'] = {'inputs': ['mex_base_universe_d2_042_mex_basefill_042'], 'func': mex_base_universe_d3_042_mex_basefill_042}


def mex_base_universe_d3_043_mex_basefill_043(mex_base_universe_d2_043_mex_basefill_043):
    return _base_universe_d3(mex_base_universe_d2_043_mex_basefill_043, 43)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_043_mex_basefill_043'] = {'inputs': ['mex_base_universe_d2_043_mex_basefill_043'], 'func': mex_base_universe_d3_043_mex_basefill_043}


def mex_base_universe_d3_044_mex_basefill_044(mex_base_universe_d2_044_mex_basefill_044):
    return _base_universe_d3(mex_base_universe_d2_044_mex_basefill_044, 44)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_044_mex_basefill_044'] = {'inputs': ['mex_base_universe_d2_044_mex_basefill_044'], 'func': mex_base_universe_d3_044_mex_basefill_044}


def mex_base_universe_d3_045_mex_basefill_045(mex_base_universe_d2_045_mex_basefill_045):
    return _base_universe_d3(mex_base_universe_d2_045_mex_basefill_045, 45)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_045_mex_basefill_045'] = {'inputs': ['mex_base_universe_d2_045_mex_basefill_045'], 'func': mex_base_universe_d3_045_mex_basefill_045}


def mex_base_universe_d3_046_mex_basefill_046(mex_base_universe_d2_046_mex_basefill_046):
    return _base_universe_d3(mex_base_universe_d2_046_mex_basefill_046, 46)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_046_mex_basefill_046'] = {'inputs': ['mex_base_universe_d2_046_mex_basefill_046'], 'func': mex_base_universe_d3_046_mex_basefill_046}


def mex_base_universe_d3_047_mex_basefill_047(mex_base_universe_d2_047_mex_basefill_047):
    return _base_universe_d3(mex_base_universe_d2_047_mex_basefill_047, 47)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_047_mex_basefill_047'] = {'inputs': ['mex_base_universe_d2_047_mex_basefill_047'], 'func': mex_base_universe_d3_047_mex_basefill_047}


def mex_base_universe_d3_048_mex_basefill_048(mex_base_universe_d2_048_mex_basefill_048):
    return _base_universe_d3(mex_base_universe_d2_048_mex_basefill_048, 48)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_048_mex_basefill_048'] = {'inputs': ['mex_base_universe_d2_048_mex_basefill_048'], 'func': mex_base_universe_d3_048_mex_basefill_048}


def mex_base_universe_d3_049_mex_basefill_049(mex_base_universe_d2_049_mex_basefill_049):
    return _base_universe_d3(mex_base_universe_d2_049_mex_basefill_049, 49)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_049_mex_basefill_049'] = {'inputs': ['mex_base_universe_d2_049_mex_basefill_049'], 'func': mex_base_universe_d3_049_mex_basefill_049}


def mex_base_universe_d3_050_mex_basefill_050(mex_base_universe_d2_050_mex_basefill_050):
    return _base_universe_d3(mex_base_universe_d2_050_mex_basefill_050, 50)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_050_mex_basefill_050'] = {'inputs': ['mex_base_universe_d2_050_mex_basefill_050'], 'func': mex_base_universe_d3_050_mex_basefill_050}


def mex_base_universe_d3_051_mex_basefill_051(mex_base_universe_d2_051_mex_basefill_051):
    return _base_universe_d3(mex_base_universe_d2_051_mex_basefill_051, 51)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_051_mex_basefill_051'] = {'inputs': ['mex_base_universe_d2_051_mex_basefill_051'], 'func': mex_base_universe_d3_051_mex_basefill_051}


def mex_base_universe_d3_052_mex_basefill_052(mex_base_universe_d2_052_mex_basefill_052):
    return _base_universe_d3(mex_base_universe_d2_052_mex_basefill_052, 52)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_052_mex_basefill_052'] = {'inputs': ['mex_base_universe_d2_052_mex_basefill_052'], 'func': mex_base_universe_d3_052_mex_basefill_052}


def mex_base_universe_d3_053_mex_basefill_053(mex_base_universe_d2_053_mex_basefill_053):
    return _base_universe_d3(mex_base_universe_d2_053_mex_basefill_053, 53)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_053_mex_basefill_053'] = {'inputs': ['mex_base_universe_d2_053_mex_basefill_053'], 'func': mex_base_universe_d3_053_mex_basefill_053}


def mex_base_universe_d3_054_mex_basefill_054(mex_base_universe_d2_054_mex_basefill_054):
    return _base_universe_d3(mex_base_universe_d2_054_mex_basefill_054, 54)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_054_mex_basefill_054'] = {'inputs': ['mex_base_universe_d2_054_mex_basefill_054'], 'func': mex_base_universe_d3_054_mex_basefill_054}


def mex_base_universe_d3_055_mex_basefill_055(mex_base_universe_d2_055_mex_basefill_055):
    return _base_universe_d3(mex_base_universe_d2_055_mex_basefill_055, 55)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_055_mex_basefill_055'] = {'inputs': ['mex_base_universe_d2_055_mex_basefill_055'], 'func': mex_base_universe_d3_055_mex_basefill_055}


def mex_base_universe_d3_056_mex_basefill_056(mex_base_universe_d2_056_mex_basefill_056):
    return _base_universe_d3(mex_base_universe_d2_056_mex_basefill_056, 56)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_056_mex_basefill_056'] = {'inputs': ['mex_base_universe_d2_056_mex_basefill_056'], 'func': mex_base_universe_d3_056_mex_basefill_056}


def mex_base_universe_d3_057_mex_basefill_057(mex_base_universe_d2_057_mex_basefill_057):
    return _base_universe_d3(mex_base_universe_d2_057_mex_basefill_057, 57)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_057_mex_basefill_057'] = {'inputs': ['mex_base_universe_d2_057_mex_basefill_057'], 'func': mex_base_universe_d3_057_mex_basefill_057}


def mex_base_universe_d3_058_mex_basefill_058(mex_base_universe_d2_058_mex_basefill_058):
    return _base_universe_d3(mex_base_universe_d2_058_mex_basefill_058, 58)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_058_mex_basefill_058'] = {'inputs': ['mex_base_universe_d2_058_mex_basefill_058'], 'func': mex_base_universe_d3_058_mex_basefill_058}


def mex_base_universe_d3_059_mex_basefill_059(mex_base_universe_d2_059_mex_basefill_059):
    return _base_universe_d3(mex_base_universe_d2_059_mex_basefill_059, 59)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_059_mex_basefill_059'] = {'inputs': ['mex_base_universe_d2_059_mex_basefill_059'], 'func': mex_base_universe_d3_059_mex_basefill_059}


def mex_base_universe_d3_060_mex_basefill_060(mex_base_universe_d2_060_mex_basefill_060):
    return _base_universe_d3(mex_base_universe_d2_060_mex_basefill_060, 60)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_060_mex_basefill_060'] = {'inputs': ['mex_base_universe_d2_060_mex_basefill_060'], 'func': mex_base_universe_d3_060_mex_basefill_060}


def mex_base_universe_d3_061_mex_basefill_061(mex_base_universe_d2_061_mex_basefill_061):
    return _base_universe_d3(mex_base_universe_d2_061_mex_basefill_061, 61)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_061_mex_basefill_061'] = {'inputs': ['mex_base_universe_d2_061_mex_basefill_061'], 'func': mex_base_universe_d3_061_mex_basefill_061}


def mex_base_universe_d3_062_mex_basefill_062(mex_base_universe_d2_062_mex_basefill_062):
    return _base_universe_d3(mex_base_universe_d2_062_mex_basefill_062, 62)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_062_mex_basefill_062'] = {'inputs': ['mex_base_universe_d2_062_mex_basefill_062'], 'func': mex_base_universe_d3_062_mex_basefill_062}


def mex_base_universe_d3_063_mex_basefill_063(mex_base_universe_d2_063_mex_basefill_063):
    return _base_universe_d3(mex_base_universe_d2_063_mex_basefill_063, 63)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_063_mex_basefill_063'] = {'inputs': ['mex_base_universe_d2_063_mex_basefill_063'], 'func': mex_base_universe_d3_063_mex_basefill_063}


def mex_base_universe_d3_064_mex_basefill_064(mex_base_universe_d2_064_mex_basefill_064):
    return _base_universe_d3(mex_base_universe_d2_064_mex_basefill_064, 64)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_064_mex_basefill_064'] = {'inputs': ['mex_base_universe_d2_064_mex_basefill_064'], 'func': mex_base_universe_d3_064_mex_basefill_064}


def mex_base_universe_d3_065_mex_basefill_065(mex_base_universe_d2_065_mex_basefill_065):
    return _base_universe_d3(mex_base_universe_d2_065_mex_basefill_065, 65)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_065_mex_basefill_065'] = {'inputs': ['mex_base_universe_d2_065_mex_basefill_065'], 'func': mex_base_universe_d3_065_mex_basefill_065}


def mex_base_universe_d3_066_mex_basefill_066(mex_base_universe_d2_066_mex_basefill_066):
    return _base_universe_d3(mex_base_universe_d2_066_mex_basefill_066, 66)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_066_mex_basefill_066'] = {'inputs': ['mex_base_universe_d2_066_mex_basefill_066'], 'func': mex_base_universe_d3_066_mex_basefill_066}


def mex_base_universe_d3_067_mex_basefill_067(mex_base_universe_d2_067_mex_basefill_067):
    return _base_universe_d3(mex_base_universe_d2_067_mex_basefill_067, 67)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_067_mex_basefill_067'] = {'inputs': ['mex_base_universe_d2_067_mex_basefill_067'], 'func': mex_base_universe_d3_067_mex_basefill_067}


def mex_base_universe_d3_068_mex_basefill_068(mex_base_universe_d2_068_mex_basefill_068):
    return _base_universe_d3(mex_base_universe_d2_068_mex_basefill_068, 68)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_068_mex_basefill_068'] = {'inputs': ['mex_base_universe_d2_068_mex_basefill_068'], 'func': mex_base_universe_d3_068_mex_basefill_068}


def mex_base_universe_d3_069_mex_basefill_069(mex_base_universe_d2_069_mex_basefill_069):
    return _base_universe_d3(mex_base_universe_d2_069_mex_basefill_069, 69)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_069_mex_basefill_069'] = {'inputs': ['mex_base_universe_d2_069_mex_basefill_069'], 'func': mex_base_universe_d3_069_mex_basefill_069}


def mex_base_universe_d3_070_mex_basefill_070(mex_base_universe_d2_070_mex_basefill_070):
    return _base_universe_d3(mex_base_universe_d2_070_mex_basefill_070, 70)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_070_mex_basefill_070'] = {'inputs': ['mex_base_universe_d2_070_mex_basefill_070'], 'func': mex_base_universe_d3_070_mex_basefill_070}


def mex_base_universe_d3_071_mex_basefill_071(mex_base_universe_d2_071_mex_basefill_071):
    return _base_universe_d3(mex_base_universe_d2_071_mex_basefill_071, 71)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_071_mex_basefill_071'] = {'inputs': ['mex_base_universe_d2_071_mex_basefill_071'], 'func': mex_base_universe_d3_071_mex_basefill_071}


def mex_base_universe_d3_072_mex_basefill_072(mex_base_universe_d2_072_mex_basefill_072):
    return _base_universe_d3(mex_base_universe_d2_072_mex_basefill_072, 72)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_072_mex_basefill_072'] = {'inputs': ['mex_base_universe_d2_072_mex_basefill_072'], 'func': mex_base_universe_d3_072_mex_basefill_072}


def mex_base_universe_d3_073_mex_basefill_073(mex_base_universe_d2_073_mex_basefill_073):
    return _base_universe_d3(mex_base_universe_d2_073_mex_basefill_073, 73)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_073_mex_basefill_073'] = {'inputs': ['mex_base_universe_d2_073_mex_basefill_073'], 'func': mex_base_universe_d3_073_mex_basefill_073}


def mex_base_universe_d3_074_mex_basefill_074(mex_base_universe_d2_074_mex_basefill_074):
    return _base_universe_d3(mex_base_universe_d2_074_mex_basefill_074, 74)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_074_mex_basefill_074'] = {'inputs': ['mex_base_universe_d2_074_mex_basefill_074'], 'func': mex_base_universe_d3_074_mex_basefill_074}


def mex_base_universe_d3_075_mex_basefill_075(mex_base_universe_d2_075_mex_basefill_075):
    return _base_universe_d3(mex_base_universe_d2_075_mex_basefill_075, 75)
MEX_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mex_base_universe_d3_075_mex_basefill_075'] = {'inputs': ['mex_base_universe_d2_075_mex_basefill_075'], 'func': mex_base_universe_d3_075_mex_basefill_075}
