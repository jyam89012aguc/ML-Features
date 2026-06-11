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



def mdv_001_return_decay_accel_1(mdv_001_return_decay_roc_1):
    feature = _s(mdv_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def mdv_007_return_decay_accel_5(mdv_007_return_decay_roc_5):
    feature = _s(mdv_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def mdv_013_return_decay_accel_42(mdv_013_return_decay_roc_42):
    feature = _s(mdv_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def mdv_179_mdv_019_return_decay_42_019_accel_126(mdv_154_mdv_019_return_decay_42_019_roc_126):
    feature = _s(mdv_154_mdv_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def mdv_180_mdv_025_return_decay_5_025_accel_378(mdv_155_mdv_025_return_decay_5_025_roc_378):
    feature = _s(mdv_155_mdv_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















MOMENTUM_DIVERGENCE_REGISTRY_3RD_DERIVATIVES = {
    'mdv_001_return_decay_accel_1': {'inputs': ['mdv_001_return_decay_roc_1'], 'func': mdv_001_return_decay_accel_1},
    'mdv_007_return_decay_accel_5': {'inputs': ['mdv_007_return_decay_roc_5'], 'func': mdv_007_return_decay_accel_5},
    'mdv_013_return_decay_accel_42': {'inputs': ['mdv_013_return_decay_roc_42'], 'func': mdv_013_return_decay_accel_42},
    'mdv_179_mdv_019_return_decay_42_019_accel_126': {'inputs': ['mdv_154_mdv_019_return_decay_42_019_roc_126'], 'func': mdv_179_mdv_019_return_decay_42_019_accel_126},
    'mdv_180_mdv_025_return_decay_5_025_accel_378': {'inputs': ['mdv_155_mdv_025_return_decay_5_025_roc_378'], 'func': mdv_180_mdv_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def md_replacement_d3_001(md_replacement_d2_001):
    feature = _clean(md_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_001'] = {'inputs': ['md_replacement_d2_001'], 'func': md_replacement_d3_001}


def md_replacement_d3_002(md_replacement_d2_002):
    feature = _clean(md_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_002'] = {'inputs': ['md_replacement_d2_002'], 'func': md_replacement_d3_002}


def md_replacement_d3_003(md_replacement_d2_003):
    feature = _clean(md_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_003'] = {'inputs': ['md_replacement_d2_003'], 'func': md_replacement_d3_003}


def md_replacement_d3_004(md_replacement_d2_004):
    feature = _clean(md_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_004'] = {'inputs': ['md_replacement_d2_004'], 'func': md_replacement_d3_004}


def md_replacement_d3_005(md_replacement_d2_005):
    feature = _clean(md_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_005'] = {'inputs': ['md_replacement_d2_005'], 'func': md_replacement_d3_005}


def md_replacement_d3_006(md_replacement_d2_006):
    feature = _clean(md_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_006'] = {'inputs': ['md_replacement_d2_006'], 'func': md_replacement_d3_006}


def md_replacement_d3_007(md_replacement_d2_007):
    feature = _clean(md_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_007'] = {'inputs': ['md_replacement_d2_007'], 'func': md_replacement_d3_007}


def md_replacement_d3_008(md_replacement_d2_008):
    feature = _clean(md_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_008'] = {'inputs': ['md_replacement_d2_008'], 'func': md_replacement_d3_008}


def md_replacement_d3_009(md_replacement_d2_009):
    feature = _clean(md_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_009'] = {'inputs': ['md_replacement_d2_009'], 'func': md_replacement_d3_009}


def md_replacement_d3_010(md_replacement_d2_010):
    feature = _clean(md_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_010'] = {'inputs': ['md_replacement_d2_010'], 'func': md_replacement_d3_010}


def md_replacement_d3_011(md_replacement_d2_011):
    feature = _clean(md_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_011'] = {'inputs': ['md_replacement_d2_011'], 'func': md_replacement_d3_011}


def md_replacement_d3_012(md_replacement_d2_012):
    feature = _clean(md_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_012'] = {'inputs': ['md_replacement_d2_012'], 'func': md_replacement_d3_012}


def md_replacement_d3_013(md_replacement_d2_013):
    feature = _clean(md_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_013'] = {'inputs': ['md_replacement_d2_013'], 'func': md_replacement_d3_013}


def md_replacement_d3_014(md_replacement_d2_014):
    feature = _clean(md_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_014'] = {'inputs': ['md_replacement_d2_014'], 'func': md_replacement_d3_014}


def md_replacement_d3_015(md_replacement_d2_015):
    feature = _clean(md_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_015'] = {'inputs': ['md_replacement_d2_015'], 'func': md_replacement_d3_015}


def md_replacement_d3_016(md_replacement_d2_016):
    feature = _clean(md_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_016'] = {'inputs': ['md_replacement_d2_016'], 'func': md_replacement_d3_016}


def md_replacement_d3_017(md_replacement_d2_017):
    feature = _clean(md_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_017'] = {'inputs': ['md_replacement_d2_017'], 'func': md_replacement_d3_017}


def md_replacement_d3_018(md_replacement_d2_018):
    feature = _clean(md_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_018'] = {'inputs': ['md_replacement_d2_018'], 'func': md_replacement_d3_018}


def md_replacement_d3_019(md_replacement_d2_019):
    feature = _clean(md_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_019'] = {'inputs': ['md_replacement_d2_019'], 'func': md_replacement_d3_019}


def md_replacement_d3_020(md_replacement_d2_020):
    feature = _clean(md_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_020'] = {'inputs': ['md_replacement_d2_020'], 'func': md_replacement_d3_020}


def md_replacement_d3_021(md_replacement_d2_021):
    feature = _clean(md_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_021'] = {'inputs': ['md_replacement_d2_021'], 'func': md_replacement_d3_021}


def md_replacement_d3_022(md_replacement_d2_022):
    feature = _clean(md_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_022'] = {'inputs': ['md_replacement_d2_022'], 'func': md_replacement_d3_022}


def md_replacement_d3_023(md_replacement_d2_023):
    feature = _clean(md_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_023'] = {'inputs': ['md_replacement_d2_023'], 'func': md_replacement_d3_023}


def md_replacement_d3_024(md_replacement_d2_024):
    feature = _clean(md_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_024'] = {'inputs': ['md_replacement_d2_024'], 'func': md_replacement_d3_024}


def md_replacement_d3_025(md_replacement_d2_025):
    feature = _clean(md_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_025'] = {'inputs': ['md_replacement_d2_025'], 'func': md_replacement_d3_025}


def md_replacement_d3_026(md_replacement_d2_026):
    feature = _clean(md_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_026'] = {'inputs': ['md_replacement_d2_026'], 'func': md_replacement_d3_026}


def md_replacement_d3_027(md_replacement_d2_027):
    feature = _clean(md_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_027'] = {'inputs': ['md_replacement_d2_027'], 'func': md_replacement_d3_027}


def md_replacement_d3_028(md_replacement_d2_028):
    feature = _clean(md_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_028'] = {'inputs': ['md_replacement_d2_028'], 'func': md_replacement_d3_028}


def md_replacement_d3_029(md_replacement_d2_029):
    feature = _clean(md_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_029'] = {'inputs': ['md_replacement_d2_029'], 'func': md_replacement_d3_029}


def md_replacement_d3_030(md_replacement_d2_030):
    feature = _clean(md_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_030'] = {'inputs': ['md_replacement_d2_030'], 'func': md_replacement_d3_030}


def md_replacement_d3_031(md_replacement_d2_031):
    feature = _clean(md_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_031'] = {'inputs': ['md_replacement_d2_031'], 'func': md_replacement_d3_031}


def md_replacement_d3_032(md_replacement_d2_032):
    feature = _clean(md_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_032'] = {'inputs': ['md_replacement_d2_032'], 'func': md_replacement_d3_032}


def md_replacement_d3_033(md_replacement_d2_033):
    feature = _clean(md_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_033'] = {'inputs': ['md_replacement_d2_033'], 'func': md_replacement_d3_033}


def md_replacement_d3_034(md_replacement_d2_034):
    feature = _clean(md_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_034'] = {'inputs': ['md_replacement_d2_034'], 'func': md_replacement_d3_034}


def md_replacement_d3_035(md_replacement_d2_035):
    feature = _clean(md_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_035'] = {'inputs': ['md_replacement_d2_035'], 'func': md_replacement_d3_035}


def md_replacement_d3_036(md_replacement_d2_036):
    feature = _clean(md_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_036'] = {'inputs': ['md_replacement_d2_036'], 'func': md_replacement_d3_036}


def md_replacement_d3_037(md_replacement_d2_037):
    feature = _clean(md_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_037'] = {'inputs': ['md_replacement_d2_037'], 'func': md_replacement_d3_037}


def md_replacement_d3_038(md_replacement_d2_038):
    feature = _clean(md_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_038'] = {'inputs': ['md_replacement_d2_038'], 'func': md_replacement_d3_038}


def md_replacement_d3_039(md_replacement_d2_039):
    feature = _clean(md_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_039'] = {'inputs': ['md_replacement_d2_039'], 'func': md_replacement_d3_039}


def md_replacement_d3_040(md_replacement_d2_040):
    feature = _clean(md_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_040'] = {'inputs': ['md_replacement_d2_040'], 'func': md_replacement_d3_040}


def md_replacement_d3_041(md_replacement_d2_041):
    feature = _clean(md_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_041'] = {'inputs': ['md_replacement_d2_041'], 'func': md_replacement_d3_041}


def md_replacement_d3_042(md_replacement_d2_042):
    feature = _clean(md_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_042'] = {'inputs': ['md_replacement_d2_042'], 'func': md_replacement_d3_042}


def md_replacement_d3_043(md_replacement_d2_043):
    feature = _clean(md_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_043'] = {'inputs': ['md_replacement_d2_043'], 'func': md_replacement_d3_043}


def md_replacement_d3_044(md_replacement_d2_044):
    feature = _clean(md_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_044'] = {'inputs': ['md_replacement_d2_044'], 'func': md_replacement_d3_044}


def md_replacement_d3_045(md_replacement_d2_045):
    feature = _clean(md_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_045'] = {'inputs': ['md_replacement_d2_045'], 'func': md_replacement_d3_045}


def md_replacement_d3_046(md_replacement_d2_046):
    feature = _clean(md_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_046'] = {'inputs': ['md_replacement_d2_046'], 'func': md_replacement_d3_046}


def md_replacement_d3_047(md_replacement_d2_047):
    feature = _clean(md_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_047'] = {'inputs': ['md_replacement_d2_047'], 'func': md_replacement_d3_047}


def md_replacement_d3_048(md_replacement_d2_048):
    feature = _clean(md_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_048'] = {'inputs': ['md_replacement_d2_048'], 'func': md_replacement_d3_048}


def md_replacement_d3_049(md_replacement_d2_049):
    feature = _clean(md_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_049'] = {'inputs': ['md_replacement_d2_049'], 'func': md_replacement_d3_049}


def md_replacement_d3_050(md_replacement_d2_050):
    feature = _clean(md_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_050'] = {'inputs': ['md_replacement_d2_050'], 'func': md_replacement_d3_050}


def md_replacement_d3_051(md_replacement_d2_051):
    feature = _clean(md_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_051'] = {'inputs': ['md_replacement_d2_051'], 'func': md_replacement_d3_051}


def md_replacement_d3_052(md_replacement_d2_052):
    feature = _clean(md_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_052'] = {'inputs': ['md_replacement_d2_052'], 'func': md_replacement_d3_052}


def md_replacement_d3_053(md_replacement_d2_053):
    feature = _clean(md_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_053'] = {'inputs': ['md_replacement_d2_053'], 'func': md_replacement_d3_053}


def md_replacement_d3_054(md_replacement_d2_054):
    feature = _clean(md_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_054'] = {'inputs': ['md_replacement_d2_054'], 'func': md_replacement_d3_054}


def md_replacement_d3_055(md_replacement_d2_055):
    feature = _clean(md_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_055'] = {'inputs': ['md_replacement_d2_055'], 'func': md_replacement_d3_055}


def md_replacement_d3_056(md_replacement_d2_056):
    feature = _clean(md_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_056'] = {'inputs': ['md_replacement_d2_056'], 'func': md_replacement_d3_056}


def md_replacement_d3_057(md_replacement_d2_057):
    feature = _clean(md_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_057'] = {'inputs': ['md_replacement_d2_057'], 'func': md_replacement_d3_057}


def md_replacement_d3_058(md_replacement_d2_058):
    feature = _clean(md_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_058'] = {'inputs': ['md_replacement_d2_058'], 'func': md_replacement_d3_058}


def md_replacement_d3_059(md_replacement_d2_059):
    feature = _clean(md_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_059'] = {'inputs': ['md_replacement_d2_059'], 'func': md_replacement_d3_059}


def md_replacement_d3_060(md_replacement_d2_060):
    feature = _clean(md_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_060'] = {'inputs': ['md_replacement_d2_060'], 'func': md_replacement_d3_060}


def md_replacement_d3_061(md_replacement_d2_061):
    feature = _clean(md_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_061'] = {'inputs': ['md_replacement_d2_061'], 'func': md_replacement_d3_061}


def md_replacement_d3_062(md_replacement_d2_062):
    feature = _clean(md_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_062'] = {'inputs': ['md_replacement_d2_062'], 'func': md_replacement_d3_062}


def md_replacement_d3_063(md_replacement_d2_063):
    feature = _clean(md_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_063'] = {'inputs': ['md_replacement_d2_063'], 'func': md_replacement_d3_063}


def md_replacement_d3_064(md_replacement_d2_064):
    feature = _clean(md_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_064'] = {'inputs': ['md_replacement_d2_064'], 'func': md_replacement_d3_064}


def md_replacement_d3_065(md_replacement_d2_065):
    feature = _clean(md_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_065'] = {'inputs': ['md_replacement_d2_065'], 'func': md_replacement_d3_065}


def md_replacement_d3_066(md_replacement_d2_066):
    feature = _clean(md_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_066'] = {'inputs': ['md_replacement_d2_066'], 'func': md_replacement_d3_066}


def md_replacement_d3_067(md_replacement_d2_067):
    feature = _clean(md_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_067'] = {'inputs': ['md_replacement_d2_067'], 'func': md_replacement_d3_067}


def md_replacement_d3_068(md_replacement_d2_068):
    feature = _clean(md_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_068'] = {'inputs': ['md_replacement_d2_068'], 'func': md_replacement_d3_068}


def md_replacement_d3_069(md_replacement_d2_069):
    feature = _clean(md_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_069'] = {'inputs': ['md_replacement_d2_069'], 'func': md_replacement_d3_069}


def md_replacement_d3_070(md_replacement_d2_070):
    feature = _clean(md_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_070'] = {'inputs': ['md_replacement_d2_070'], 'func': md_replacement_d3_070}


def md_replacement_d3_071(md_replacement_d2_071):
    feature = _clean(md_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_071'] = {'inputs': ['md_replacement_d2_071'], 'func': md_replacement_d3_071}


def md_replacement_d3_072(md_replacement_d2_072):
    feature = _clean(md_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_072'] = {'inputs': ['md_replacement_d2_072'], 'func': md_replacement_d3_072}


def md_replacement_d3_073(md_replacement_d2_073):
    feature = _clean(md_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_073'] = {'inputs': ['md_replacement_d2_073'], 'func': md_replacement_d3_073}


def md_replacement_d3_074(md_replacement_d2_074):
    feature = _clean(md_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_074'] = {'inputs': ['md_replacement_d2_074'], 'func': md_replacement_d3_074}


def md_replacement_d3_075(md_replacement_d2_075):
    feature = _clean(md_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_075'] = {'inputs': ['md_replacement_d2_075'], 'func': md_replacement_d3_075}


def md_replacement_d3_076(md_replacement_d2_076):
    feature = _clean(md_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_076'] = {'inputs': ['md_replacement_d2_076'], 'func': md_replacement_d3_076}


def md_replacement_d3_077(md_replacement_d2_077):
    feature = _clean(md_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_077'] = {'inputs': ['md_replacement_d2_077'], 'func': md_replacement_d3_077}


def md_replacement_d3_078(md_replacement_d2_078):
    feature = _clean(md_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_078'] = {'inputs': ['md_replacement_d2_078'], 'func': md_replacement_d3_078}


def md_replacement_d3_079(md_replacement_d2_079):
    feature = _clean(md_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_079'] = {'inputs': ['md_replacement_d2_079'], 'func': md_replacement_d3_079}


def md_replacement_d3_080(md_replacement_d2_080):
    feature = _clean(md_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_080'] = {'inputs': ['md_replacement_d2_080'], 'func': md_replacement_d3_080}


def md_replacement_d3_081(md_replacement_d2_081):
    feature = _clean(md_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_081'] = {'inputs': ['md_replacement_d2_081'], 'func': md_replacement_d3_081}


def md_replacement_d3_082(md_replacement_d2_082):
    feature = _clean(md_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_082'] = {'inputs': ['md_replacement_d2_082'], 'func': md_replacement_d3_082}


def md_replacement_d3_083(md_replacement_d2_083):
    feature = _clean(md_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_083'] = {'inputs': ['md_replacement_d2_083'], 'func': md_replacement_d3_083}


def md_replacement_d3_084(md_replacement_d2_084):
    feature = _clean(md_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_084'] = {'inputs': ['md_replacement_d2_084'], 'func': md_replacement_d3_084}


def md_replacement_d3_085(md_replacement_d2_085):
    feature = _clean(md_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_085'] = {'inputs': ['md_replacement_d2_085'], 'func': md_replacement_d3_085}


def md_replacement_d3_086(md_replacement_d2_086):
    feature = _clean(md_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_086'] = {'inputs': ['md_replacement_d2_086'], 'func': md_replacement_d3_086}


def md_replacement_d3_087(md_replacement_d2_087):
    feature = _clean(md_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_087'] = {'inputs': ['md_replacement_d2_087'], 'func': md_replacement_d3_087}


def md_replacement_d3_088(md_replacement_d2_088):
    feature = _clean(md_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_088'] = {'inputs': ['md_replacement_d2_088'], 'func': md_replacement_d3_088}


def md_replacement_d3_089(md_replacement_d2_089):
    feature = _clean(md_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_089'] = {'inputs': ['md_replacement_d2_089'], 'func': md_replacement_d3_089}


def md_replacement_d3_090(md_replacement_d2_090):
    feature = _clean(md_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_090'] = {'inputs': ['md_replacement_d2_090'], 'func': md_replacement_d3_090}


def md_replacement_d3_091(md_replacement_d2_091):
    feature = _clean(md_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_091'] = {'inputs': ['md_replacement_d2_091'], 'func': md_replacement_d3_091}


def md_replacement_d3_092(md_replacement_d2_092):
    feature = _clean(md_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_092'] = {'inputs': ['md_replacement_d2_092'], 'func': md_replacement_d3_092}


def md_replacement_d3_093(md_replacement_d2_093):
    feature = _clean(md_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_093'] = {'inputs': ['md_replacement_d2_093'], 'func': md_replacement_d3_093}


def md_replacement_d3_094(md_replacement_d2_094):
    feature = _clean(md_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_094'] = {'inputs': ['md_replacement_d2_094'], 'func': md_replacement_d3_094}


def md_replacement_d3_095(md_replacement_d2_095):
    feature = _clean(md_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_095'] = {'inputs': ['md_replacement_d2_095'], 'func': md_replacement_d3_095}


def md_replacement_d3_096(md_replacement_d2_096):
    feature = _clean(md_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_096'] = {'inputs': ['md_replacement_d2_096'], 'func': md_replacement_d3_096}


def md_replacement_d3_097(md_replacement_d2_097):
    feature = _clean(md_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_097'] = {'inputs': ['md_replacement_d2_097'], 'func': md_replacement_d3_097}


def md_replacement_d3_098(md_replacement_d2_098):
    feature = _clean(md_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_098'] = {'inputs': ['md_replacement_d2_098'], 'func': md_replacement_d3_098}


def md_replacement_d3_099(md_replacement_d2_099):
    feature = _clean(md_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_099'] = {'inputs': ['md_replacement_d2_099'], 'func': md_replacement_d3_099}


def md_replacement_d3_100(md_replacement_d2_100):
    feature = _clean(md_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_100'] = {'inputs': ['md_replacement_d2_100'], 'func': md_replacement_d3_100}


def md_replacement_d3_101(md_replacement_d2_101):
    feature = _clean(md_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_101'] = {'inputs': ['md_replacement_d2_101'], 'func': md_replacement_d3_101}


def md_replacement_d3_102(md_replacement_d2_102):
    feature = _clean(md_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_102'] = {'inputs': ['md_replacement_d2_102'], 'func': md_replacement_d3_102}


def md_replacement_d3_103(md_replacement_d2_103):
    feature = _clean(md_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_103'] = {'inputs': ['md_replacement_d2_103'], 'func': md_replacement_d3_103}


def md_replacement_d3_104(md_replacement_d2_104):
    feature = _clean(md_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_104'] = {'inputs': ['md_replacement_d2_104'], 'func': md_replacement_d3_104}


def md_replacement_d3_105(md_replacement_d2_105):
    feature = _clean(md_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_105'] = {'inputs': ['md_replacement_d2_105'], 'func': md_replacement_d3_105}


def md_replacement_d3_106(md_replacement_d2_106):
    feature = _clean(md_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_106'] = {'inputs': ['md_replacement_d2_106'], 'func': md_replacement_d3_106}


def md_replacement_d3_107(md_replacement_d2_107):
    feature = _clean(md_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_107'] = {'inputs': ['md_replacement_d2_107'], 'func': md_replacement_d3_107}


def md_replacement_d3_108(md_replacement_d2_108):
    feature = _clean(md_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_108'] = {'inputs': ['md_replacement_d2_108'], 'func': md_replacement_d3_108}


def md_replacement_d3_109(md_replacement_d2_109):
    feature = _clean(md_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_109'] = {'inputs': ['md_replacement_d2_109'], 'func': md_replacement_d3_109}


def md_replacement_d3_110(md_replacement_d2_110):
    feature = _clean(md_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_110'] = {'inputs': ['md_replacement_d2_110'], 'func': md_replacement_d3_110}


def md_replacement_d3_111(md_replacement_d2_111):
    feature = _clean(md_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_111'] = {'inputs': ['md_replacement_d2_111'], 'func': md_replacement_d3_111}


def md_replacement_d3_112(md_replacement_d2_112):
    feature = _clean(md_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_112'] = {'inputs': ['md_replacement_d2_112'], 'func': md_replacement_d3_112}


def md_replacement_d3_113(md_replacement_d2_113):
    feature = _clean(md_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_113'] = {'inputs': ['md_replacement_d2_113'], 'func': md_replacement_d3_113}


def md_replacement_d3_114(md_replacement_d2_114):
    feature = _clean(md_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_114'] = {'inputs': ['md_replacement_d2_114'], 'func': md_replacement_d3_114}


def md_replacement_d3_115(md_replacement_d2_115):
    feature = _clean(md_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_115'] = {'inputs': ['md_replacement_d2_115'], 'func': md_replacement_d3_115}


def md_replacement_d3_116(md_replacement_d2_116):
    feature = _clean(md_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_116'] = {'inputs': ['md_replacement_d2_116'], 'func': md_replacement_d3_116}


def md_replacement_d3_117(md_replacement_d2_117):
    feature = _clean(md_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_117'] = {'inputs': ['md_replacement_d2_117'], 'func': md_replacement_d3_117}


def md_replacement_d3_118(md_replacement_d2_118):
    feature = _clean(md_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_118'] = {'inputs': ['md_replacement_d2_118'], 'func': md_replacement_d3_118}


def md_replacement_d3_119(md_replacement_d2_119):
    feature = _clean(md_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_119'] = {'inputs': ['md_replacement_d2_119'], 'func': md_replacement_d3_119}


def md_replacement_d3_120(md_replacement_d2_120):
    feature = _clean(md_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_120'] = {'inputs': ['md_replacement_d2_120'], 'func': md_replacement_d3_120}


def md_replacement_d3_121(md_replacement_d2_121):
    feature = _clean(md_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_121'] = {'inputs': ['md_replacement_d2_121'], 'func': md_replacement_d3_121}


def md_replacement_d3_122(md_replacement_d2_122):
    feature = _clean(md_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_122'] = {'inputs': ['md_replacement_d2_122'], 'func': md_replacement_d3_122}


def md_replacement_d3_123(md_replacement_d2_123):
    feature = _clean(md_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_123'] = {'inputs': ['md_replacement_d2_123'], 'func': md_replacement_d3_123}


def md_replacement_d3_124(md_replacement_d2_124):
    feature = _clean(md_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_124'] = {'inputs': ['md_replacement_d2_124'], 'func': md_replacement_d3_124}


def md_replacement_d3_125(md_replacement_d2_125):
    feature = _clean(md_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_125'] = {'inputs': ['md_replacement_d2_125'], 'func': md_replacement_d3_125}


def md_replacement_d3_126(md_replacement_d2_126):
    feature = _clean(md_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_126'] = {'inputs': ['md_replacement_d2_126'], 'func': md_replacement_d3_126}


def md_replacement_d3_127(md_replacement_d2_127):
    feature = _clean(md_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_127'] = {'inputs': ['md_replacement_d2_127'], 'func': md_replacement_d3_127}


def md_replacement_d3_128(md_replacement_d2_128):
    feature = _clean(md_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_128'] = {'inputs': ['md_replacement_d2_128'], 'func': md_replacement_d3_128}


def md_replacement_d3_129(md_replacement_d2_129):
    feature = _clean(md_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_129'] = {'inputs': ['md_replacement_d2_129'], 'func': md_replacement_d3_129}


def md_replacement_d3_130(md_replacement_d2_130):
    feature = _clean(md_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_130'] = {'inputs': ['md_replacement_d2_130'], 'func': md_replacement_d3_130}


def md_replacement_d3_131(md_replacement_d2_131):
    feature = _clean(md_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_131'] = {'inputs': ['md_replacement_d2_131'], 'func': md_replacement_d3_131}


def md_replacement_d3_132(md_replacement_d2_132):
    feature = _clean(md_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_132'] = {'inputs': ['md_replacement_d2_132'], 'func': md_replacement_d3_132}


def md_replacement_d3_133(md_replacement_d2_133):
    feature = _clean(md_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_133'] = {'inputs': ['md_replacement_d2_133'], 'func': md_replacement_d3_133}


def md_replacement_d3_134(md_replacement_d2_134):
    feature = _clean(md_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_134'] = {'inputs': ['md_replacement_d2_134'], 'func': md_replacement_d3_134}


def md_replacement_d3_135(md_replacement_d2_135):
    feature = _clean(md_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_135'] = {'inputs': ['md_replacement_d2_135'], 'func': md_replacement_d3_135}


def md_replacement_d3_136(md_replacement_d2_136):
    feature = _clean(md_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_136'] = {'inputs': ['md_replacement_d2_136'], 'func': md_replacement_d3_136}


def md_replacement_d3_137(md_replacement_d2_137):
    feature = _clean(md_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_137'] = {'inputs': ['md_replacement_d2_137'], 'func': md_replacement_d3_137}


def md_replacement_d3_138(md_replacement_d2_138):
    feature = _clean(md_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_138'] = {'inputs': ['md_replacement_d2_138'], 'func': md_replacement_d3_138}


def md_replacement_d3_139(md_replacement_d2_139):
    feature = _clean(md_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_139'] = {'inputs': ['md_replacement_d2_139'], 'func': md_replacement_d3_139}


def md_replacement_d3_140(md_replacement_d2_140):
    feature = _clean(md_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_140'] = {'inputs': ['md_replacement_d2_140'], 'func': md_replacement_d3_140}


def md_replacement_d3_141(md_replacement_d2_141):
    feature = _clean(md_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_141'] = {'inputs': ['md_replacement_d2_141'], 'func': md_replacement_d3_141}


def md_replacement_d3_142(md_replacement_d2_142):
    feature = _clean(md_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_142'] = {'inputs': ['md_replacement_d2_142'], 'func': md_replacement_d3_142}


def md_replacement_d3_143(md_replacement_d2_143):
    feature = _clean(md_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_143'] = {'inputs': ['md_replacement_d2_143'], 'func': md_replacement_d3_143}


def md_replacement_d3_144(md_replacement_d2_144):
    feature = _clean(md_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_144'] = {'inputs': ['md_replacement_d2_144'], 'func': md_replacement_d3_144}


def md_replacement_d3_145(md_replacement_d2_145):
    feature = _clean(md_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_145'] = {'inputs': ['md_replacement_d2_145'], 'func': md_replacement_d3_145}


def md_replacement_d3_146(md_replacement_d2_146):
    feature = _clean(md_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_146'] = {'inputs': ['md_replacement_d2_146'], 'func': md_replacement_d3_146}


def md_replacement_d3_147(md_replacement_d2_147):
    feature = _clean(md_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_147'] = {'inputs': ['md_replacement_d2_147'], 'func': md_replacement_d3_147}


def md_replacement_d3_148(md_replacement_d2_148):
    feature = _clean(md_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_148'] = {'inputs': ['md_replacement_d2_148'], 'func': md_replacement_d3_148}


def md_replacement_d3_149(md_replacement_d2_149):
    feature = _clean(md_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_149'] = {'inputs': ['md_replacement_d2_149'], 'func': md_replacement_d3_149}


def md_replacement_d3_150(md_replacement_d2_150):
    feature = _clean(md_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_150'] = {'inputs': ['md_replacement_d2_150'], 'func': md_replacement_d3_150}


def md_replacement_d3_151(md_replacement_d2_151):
    feature = _clean(md_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_151'] = {'inputs': ['md_replacement_d2_151'], 'func': md_replacement_d3_151}


def md_replacement_d3_152(md_replacement_d2_152):
    feature = _clean(md_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_152'] = {'inputs': ['md_replacement_d2_152'], 'func': md_replacement_d3_152}


def md_replacement_d3_153(md_replacement_d2_153):
    feature = _clean(md_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_153'] = {'inputs': ['md_replacement_d2_153'], 'func': md_replacement_d3_153}


def md_replacement_d3_154(md_replacement_d2_154):
    feature = _clean(md_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_154'] = {'inputs': ['md_replacement_d2_154'], 'func': md_replacement_d3_154}


def md_replacement_d3_155(md_replacement_d2_155):
    feature = _clean(md_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_155'] = {'inputs': ['md_replacement_d2_155'], 'func': md_replacement_d3_155}


def md_replacement_d3_156(md_replacement_d2_156):
    feature = _clean(md_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_156'] = {'inputs': ['md_replacement_d2_156'], 'func': md_replacement_d3_156}


def md_replacement_d3_157(md_replacement_d2_157):
    feature = _clean(md_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_157'] = {'inputs': ['md_replacement_d2_157'], 'func': md_replacement_d3_157}


def md_replacement_d3_158(md_replacement_d2_158):
    feature = _clean(md_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_158'] = {'inputs': ['md_replacement_d2_158'], 'func': md_replacement_d3_158}


def md_replacement_d3_159(md_replacement_d2_159):
    feature = _clean(md_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_159'] = {'inputs': ['md_replacement_d2_159'], 'func': md_replacement_d3_159}


def md_replacement_d3_160(md_replacement_d2_160):
    feature = _clean(md_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_160'] = {'inputs': ['md_replacement_d2_160'], 'func': md_replacement_d3_160}


def md_replacement_d3_161(md_replacement_d2_161):
    feature = _clean(md_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_161'] = {'inputs': ['md_replacement_d2_161'], 'func': md_replacement_d3_161}


def md_replacement_d3_162(md_replacement_d2_162):
    feature = _clean(md_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_162'] = {'inputs': ['md_replacement_d2_162'], 'func': md_replacement_d3_162}


def md_replacement_d3_163(md_replacement_d2_163):
    feature = _clean(md_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_163'] = {'inputs': ['md_replacement_d2_163'], 'func': md_replacement_d3_163}


def md_replacement_d3_164(md_replacement_d2_164):
    feature = _clean(md_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_164'] = {'inputs': ['md_replacement_d2_164'], 'func': md_replacement_d3_164}


def md_replacement_d3_165(md_replacement_d2_165):
    feature = _clean(md_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_165'] = {'inputs': ['md_replacement_d2_165'], 'func': md_replacement_d3_165}


def md_replacement_d3_166(md_replacement_d2_166):
    feature = _clean(md_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_166'] = {'inputs': ['md_replacement_d2_166'], 'func': md_replacement_d3_166}


def md_replacement_d3_167(md_replacement_d2_167):
    feature = _clean(md_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_167'] = {'inputs': ['md_replacement_d2_167'], 'func': md_replacement_d3_167}


def md_replacement_d3_168(md_replacement_d2_168):
    feature = _clean(md_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_168'] = {'inputs': ['md_replacement_d2_168'], 'func': md_replacement_d3_168}


def md_replacement_d3_169(md_replacement_d2_169):
    feature = _clean(md_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_169'] = {'inputs': ['md_replacement_d2_169'], 'func': md_replacement_d3_169}


def md_replacement_d3_170(md_replacement_d2_170):
    feature = _clean(md_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_170'] = {'inputs': ['md_replacement_d2_170'], 'func': md_replacement_d3_170}


def md_replacement_d3_171(md_replacement_d2_171):
    feature = _clean(md_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_171'] = {'inputs': ['md_replacement_d2_171'], 'func': md_replacement_d3_171}


def md_replacement_d3_172(md_replacement_d2_172):
    feature = _clean(md_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_172'] = {'inputs': ['md_replacement_d2_172'], 'func': md_replacement_d3_172}


def md_replacement_d3_173(md_replacement_d2_173):
    feature = _clean(md_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_173'] = {'inputs': ['md_replacement_d2_173'], 'func': md_replacement_d3_173}


def md_replacement_d3_174(md_replacement_d2_174):
    feature = _clean(md_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_174'] = {'inputs': ['md_replacement_d2_174'], 'func': md_replacement_d3_174}


def md_replacement_d3_175(md_replacement_d2_175):
    feature = _clean(md_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
MD_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['md_replacement_d3_175'] = {'inputs': ['md_replacement_d2_175'], 'func': md_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def mdv_base_universe_d3_001_mdv_003_loss_streak_21_003(mdv_base_universe_d2_001_mdv_003_loss_streak_21_003):
    return _base_universe_d3(mdv_base_universe_d2_001_mdv_003_loss_streak_21_003, 1)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_001_mdv_003_loss_streak_21_003'] = {'inputs': ['mdv_base_universe_d2_001_mdv_003_loss_streak_21_003'], 'func': mdv_base_universe_d3_001_mdv_003_loss_streak_21_003}


def mdv_base_universe_d3_002_mdv_004_ma_distance_42_004(mdv_base_universe_d2_002_mdv_004_ma_distance_42_004):
    return _base_universe_d3(mdv_base_universe_d2_002_mdv_004_ma_distance_42_004, 2)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_002_mdv_004_ma_distance_42_004'] = {'inputs': ['mdv_base_universe_d2_002_mdv_004_ma_distance_42_004'], 'func': mdv_base_universe_d3_002_mdv_004_ma_distance_42_004}


def mdv_base_universe_d3_003_mdv_005_stochastic_position_63_005(mdv_base_universe_d2_003_mdv_005_stochastic_position_63_005):
    return _base_universe_d3(mdv_base_universe_d2_003_mdv_005_stochastic_position_63_005, 3)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_003_mdv_005_stochastic_position_63_005'] = {'inputs': ['mdv_base_universe_d2_003_mdv_005_stochastic_position_63_005'], 'func': mdv_base_universe_d3_003_mdv_005_stochastic_position_63_005}


def mdv_base_universe_d3_004_mdv_009_loss_streak_252_009(mdv_base_universe_d2_004_mdv_009_loss_streak_252_009):
    return _base_universe_d3(mdv_base_universe_d2_004_mdv_009_loss_streak_252_009, 4)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_004_mdv_009_loss_streak_252_009'] = {'inputs': ['mdv_base_universe_d2_004_mdv_009_loss_streak_252_009'], 'func': mdv_base_universe_d3_004_mdv_009_loss_streak_252_009}


def mdv_base_universe_d3_005_mdv_010_ma_distance_378_010(mdv_base_universe_d2_005_mdv_010_ma_distance_378_010):
    return _base_universe_d3(mdv_base_universe_d2_005_mdv_010_ma_distance_378_010, 5)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_005_mdv_010_ma_distance_378_010'] = {'inputs': ['mdv_base_universe_d2_005_mdv_010_ma_distance_378_010'], 'func': mdv_base_universe_d3_005_mdv_010_ma_distance_378_010}


def mdv_base_universe_d3_006_mdv_011_stochastic_position_504_011(mdv_base_universe_d2_006_mdv_011_stochastic_position_504_011):
    return _base_universe_d3(mdv_base_universe_d2_006_mdv_011_stochastic_position_504_011, 6)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_006_mdv_011_stochastic_position_504_011'] = {'inputs': ['mdv_base_universe_d2_006_mdv_011_stochastic_position_504_011'], 'func': mdv_base_universe_d3_006_mdv_011_stochastic_position_504_011}


def mdv_base_universe_d3_007_mdv_015_loss_streak_1512_015(mdv_base_universe_d2_007_mdv_015_loss_streak_1512_015):
    return _base_universe_d3(mdv_base_universe_d2_007_mdv_015_loss_streak_1512_015, 7)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_007_mdv_015_loss_streak_1512_015'] = {'inputs': ['mdv_base_universe_d2_007_mdv_015_loss_streak_1512_015'], 'func': mdv_base_universe_d3_007_mdv_015_loss_streak_1512_015}


def mdv_base_universe_d3_008_mdv_016_ma_distance_5_016(mdv_base_universe_d2_008_mdv_016_ma_distance_5_016):
    return _base_universe_d3(mdv_base_universe_d2_008_mdv_016_ma_distance_5_016, 8)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_008_mdv_016_ma_distance_5_016'] = {'inputs': ['mdv_base_universe_d2_008_mdv_016_ma_distance_5_016'], 'func': mdv_base_universe_d3_008_mdv_016_ma_distance_5_016}


def mdv_base_universe_d3_009_mdv_017_stochastic_position_10_017(mdv_base_universe_d2_009_mdv_017_stochastic_position_10_017):
    return _base_universe_d3(mdv_base_universe_d2_009_mdv_017_stochastic_position_10_017, 9)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_009_mdv_017_stochastic_position_10_017'] = {'inputs': ['mdv_base_universe_d2_009_mdv_017_stochastic_position_10_017'], 'func': mdv_base_universe_d3_009_mdv_017_stochastic_position_10_017}


def mdv_base_universe_d3_010_mdv_021_loss_streak_84_021(mdv_base_universe_d2_010_mdv_021_loss_streak_84_021):
    return _base_universe_d3(mdv_base_universe_d2_010_mdv_021_loss_streak_84_021, 10)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_010_mdv_021_loss_streak_84_021'] = {'inputs': ['mdv_base_universe_d2_010_mdv_021_loss_streak_84_021'], 'func': mdv_base_universe_d3_010_mdv_021_loss_streak_84_021}


def mdv_base_universe_d3_011_mdv_022_ma_distance_126_022(mdv_base_universe_d2_011_mdv_022_ma_distance_126_022):
    return _base_universe_d3(mdv_base_universe_d2_011_mdv_022_ma_distance_126_022, 11)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_011_mdv_022_ma_distance_126_022'] = {'inputs': ['mdv_base_universe_d2_011_mdv_022_ma_distance_126_022'], 'func': mdv_base_universe_d3_011_mdv_022_ma_distance_126_022}


def mdv_base_universe_d3_012_mdv_023_stochastic_position_189_023(mdv_base_universe_d2_012_mdv_023_stochastic_position_189_023):
    return _base_universe_d3(mdv_base_universe_d2_012_mdv_023_stochastic_position_189_023, 12)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_012_mdv_023_stochastic_position_189_023'] = {'inputs': ['mdv_base_universe_d2_012_mdv_023_stochastic_position_189_023'], 'func': mdv_base_universe_d3_012_mdv_023_stochastic_position_189_023}


def mdv_base_universe_d3_013_mdv_027_loss_streak_756_027(mdv_base_universe_d2_013_mdv_027_loss_streak_756_027):
    return _base_universe_d3(mdv_base_universe_d2_013_mdv_027_loss_streak_756_027, 13)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_013_mdv_027_loss_streak_756_027'] = {'inputs': ['mdv_base_universe_d2_013_mdv_027_loss_streak_756_027'], 'func': mdv_base_universe_d3_013_mdv_027_loss_streak_756_027}


def mdv_base_universe_d3_014_mdv_028_ma_distance_1008_028(mdv_base_universe_d2_014_mdv_028_ma_distance_1008_028):
    return _base_universe_d3(mdv_base_universe_d2_014_mdv_028_ma_distance_1008_028, 14)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_014_mdv_028_ma_distance_1008_028'] = {'inputs': ['mdv_base_universe_d2_014_mdv_028_ma_distance_1008_028'], 'func': mdv_base_universe_d3_014_mdv_028_ma_distance_1008_028}


def mdv_base_universe_d3_015_mdv_029_stochastic_position_1260_029(mdv_base_universe_d2_015_mdv_029_stochastic_position_1260_029):
    return _base_universe_d3(mdv_base_universe_d2_015_mdv_029_stochastic_position_1260_029, 15)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_015_mdv_029_stochastic_position_1260_029'] = {'inputs': ['mdv_base_universe_d2_015_mdv_029_stochastic_position_1260_029'], 'func': mdv_base_universe_d3_015_mdv_029_stochastic_position_1260_029}


def mdv_base_universe_d3_016_mdv_basefill_001(mdv_base_universe_d2_016_mdv_basefill_001):
    return _base_universe_d3(mdv_base_universe_d2_016_mdv_basefill_001, 16)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_016_mdv_basefill_001'] = {'inputs': ['mdv_base_universe_d2_016_mdv_basefill_001'], 'func': mdv_base_universe_d3_016_mdv_basefill_001}


def mdv_base_universe_d3_017_mdv_basefill_002(mdv_base_universe_d2_017_mdv_basefill_002):
    return _base_universe_d3(mdv_base_universe_d2_017_mdv_basefill_002, 17)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_017_mdv_basefill_002'] = {'inputs': ['mdv_base_universe_d2_017_mdv_basefill_002'], 'func': mdv_base_universe_d3_017_mdv_basefill_002}


def mdv_base_universe_d3_018_mdv_basefill_006(mdv_base_universe_d2_018_mdv_basefill_006):
    return _base_universe_d3(mdv_base_universe_d2_018_mdv_basefill_006, 18)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_018_mdv_basefill_006'] = {'inputs': ['mdv_base_universe_d2_018_mdv_basefill_006'], 'func': mdv_base_universe_d3_018_mdv_basefill_006}


def mdv_base_universe_d3_019_mdv_basefill_007(mdv_base_universe_d2_019_mdv_basefill_007):
    return _base_universe_d3(mdv_base_universe_d2_019_mdv_basefill_007, 19)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_019_mdv_basefill_007'] = {'inputs': ['mdv_base_universe_d2_019_mdv_basefill_007'], 'func': mdv_base_universe_d3_019_mdv_basefill_007}


def mdv_base_universe_d3_020_mdv_basefill_008(mdv_base_universe_d2_020_mdv_basefill_008):
    return _base_universe_d3(mdv_base_universe_d2_020_mdv_basefill_008, 20)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_020_mdv_basefill_008'] = {'inputs': ['mdv_base_universe_d2_020_mdv_basefill_008'], 'func': mdv_base_universe_d3_020_mdv_basefill_008}


def mdv_base_universe_d3_021_mdv_basefill_012(mdv_base_universe_d2_021_mdv_basefill_012):
    return _base_universe_d3(mdv_base_universe_d2_021_mdv_basefill_012, 21)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_021_mdv_basefill_012'] = {'inputs': ['mdv_base_universe_d2_021_mdv_basefill_012'], 'func': mdv_base_universe_d3_021_mdv_basefill_012}


def mdv_base_universe_d3_022_mdv_basefill_013(mdv_base_universe_d2_022_mdv_basefill_013):
    return _base_universe_d3(mdv_base_universe_d2_022_mdv_basefill_013, 22)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_022_mdv_basefill_013'] = {'inputs': ['mdv_base_universe_d2_022_mdv_basefill_013'], 'func': mdv_base_universe_d3_022_mdv_basefill_013}


def mdv_base_universe_d3_023_mdv_basefill_014(mdv_base_universe_d2_023_mdv_basefill_014):
    return _base_universe_d3(mdv_base_universe_d2_023_mdv_basefill_014, 23)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_023_mdv_basefill_014'] = {'inputs': ['mdv_base_universe_d2_023_mdv_basefill_014'], 'func': mdv_base_universe_d3_023_mdv_basefill_014}


def mdv_base_universe_d3_024_mdv_basefill_018(mdv_base_universe_d2_024_mdv_basefill_018):
    return _base_universe_d3(mdv_base_universe_d2_024_mdv_basefill_018, 24)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_024_mdv_basefill_018'] = {'inputs': ['mdv_base_universe_d2_024_mdv_basefill_018'], 'func': mdv_base_universe_d3_024_mdv_basefill_018}


def mdv_base_universe_d3_025_mdv_basefill_019(mdv_base_universe_d2_025_mdv_basefill_019):
    return _base_universe_d3(mdv_base_universe_d2_025_mdv_basefill_019, 25)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_025_mdv_basefill_019'] = {'inputs': ['mdv_base_universe_d2_025_mdv_basefill_019'], 'func': mdv_base_universe_d3_025_mdv_basefill_019}


def mdv_base_universe_d3_026_mdv_basefill_020(mdv_base_universe_d2_026_mdv_basefill_020):
    return _base_universe_d3(mdv_base_universe_d2_026_mdv_basefill_020, 26)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_026_mdv_basefill_020'] = {'inputs': ['mdv_base_universe_d2_026_mdv_basefill_020'], 'func': mdv_base_universe_d3_026_mdv_basefill_020}


def mdv_base_universe_d3_027_mdv_basefill_024(mdv_base_universe_d2_027_mdv_basefill_024):
    return _base_universe_d3(mdv_base_universe_d2_027_mdv_basefill_024, 27)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_027_mdv_basefill_024'] = {'inputs': ['mdv_base_universe_d2_027_mdv_basefill_024'], 'func': mdv_base_universe_d3_027_mdv_basefill_024}


def mdv_base_universe_d3_028_mdv_basefill_025(mdv_base_universe_d2_028_mdv_basefill_025):
    return _base_universe_d3(mdv_base_universe_d2_028_mdv_basefill_025, 28)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_028_mdv_basefill_025'] = {'inputs': ['mdv_base_universe_d2_028_mdv_basefill_025'], 'func': mdv_base_universe_d3_028_mdv_basefill_025}


def mdv_base_universe_d3_029_mdv_basefill_026(mdv_base_universe_d2_029_mdv_basefill_026):
    return _base_universe_d3(mdv_base_universe_d2_029_mdv_basefill_026, 29)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_029_mdv_basefill_026'] = {'inputs': ['mdv_base_universe_d2_029_mdv_basefill_026'], 'func': mdv_base_universe_d3_029_mdv_basefill_026}


def mdv_base_universe_d3_030_mdv_basefill_030(mdv_base_universe_d2_030_mdv_basefill_030):
    return _base_universe_d3(mdv_base_universe_d2_030_mdv_basefill_030, 30)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_030_mdv_basefill_030'] = {'inputs': ['mdv_base_universe_d2_030_mdv_basefill_030'], 'func': mdv_base_universe_d3_030_mdv_basefill_030}


def mdv_base_universe_d3_031_mdv_basefill_031(mdv_base_universe_d2_031_mdv_basefill_031):
    return _base_universe_d3(mdv_base_universe_d2_031_mdv_basefill_031, 31)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_031_mdv_basefill_031'] = {'inputs': ['mdv_base_universe_d2_031_mdv_basefill_031'], 'func': mdv_base_universe_d3_031_mdv_basefill_031}


def mdv_base_universe_d3_032_mdv_basefill_032(mdv_base_universe_d2_032_mdv_basefill_032):
    return _base_universe_d3(mdv_base_universe_d2_032_mdv_basefill_032, 32)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_032_mdv_basefill_032'] = {'inputs': ['mdv_base_universe_d2_032_mdv_basefill_032'], 'func': mdv_base_universe_d3_032_mdv_basefill_032}


def mdv_base_universe_d3_033_mdv_basefill_033(mdv_base_universe_d2_033_mdv_basefill_033):
    return _base_universe_d3(mdv_base_universe_d2_033_mdv_basefill_033, 33)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_033_mdv_basefill_033'] = {'inputs': ['mdv_base_universe_d2_033_mdv_basefill_033'], 'func': mdv_base_universe_d3_033_mdv_basefill_033}


def mdv_base_universe_d3_034_mdv_basefill_034(mdv_base_universe_d2_034_mdv_basefill_034):
    return _base_universe_d3(mdv_base_universe_d2_034_mdv_basefill_034, 34)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_034_mdv_basefill_034'] = {'inputs': ['mdv_base_universe_d2_034_mdv_basefill_034'], 'func': mdv_base_universe_d3_034_mdv_basefill_034}


def mdv_base_universe_d3_035_mdv_basefill_035(mdv_base_universe_d2_035_mdv_basefill_035):
    return _base_universe_d3(mdv_base_universe_d2_035_mdv_basefill_035, 35)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_035_mdv_basefill_035'] = {'inputs': ['mdv_base_universe_d2_035_mdv_basefill_035'], 'func': mdv_base_universe_d3_035_mdv_basefill_035}


def mdv_base_universe_d3_036_mdv_basefill_036(mdv_base_universe_d2_036_mdv_basefill_036):
    return _base_universe_d3(mdv_base_universe_d2_036_mdv_basefill_036, 36)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_036_mdv_basefill_036'] = {'inputs': ['mdv_base_universe_d2_036_mdv_basefill_036'], 'func': mdv_base_universe_d3_036_mdv_basefill_036}


def mdv_base_universe_d3_037_mdv_basefill_037(mdv_base_universe_d2_037_mdv_basefill_037):
    return _base_universe_d3(mdv_base_universe_d2_037_mdv_basefill_037, 37)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_037_mdv_basefill_037'] = {'inputs': ['mdv_base_universe_d2_037_mdv_basefill_037'], 'func': mdv_base_universe_d3_037_mdv_basefill_037}


def mdv_base_universe_d3_038_mdv_basefill_038(mdv_base_universe_d2_038_mdv_basefill_038):
    return _base_universe_d3(mdv_base_universe_d2_038_mdv_basefill_038, 38)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_038_mdv_basefill_038'] = {'inputs': ['mdv_base_universe_d2_038_mdv_basefill_038'], 'func': mdv_base_universe_d3_038_mdv_basefill_038}


def mdv_base_universe_d3_039_mdv_basefill_039(mdv_base_universe_d2_039_mdv_basefill_039):
    return _base_universe_d3(mdv_base_universe_d2_039_mdv_basefill_039, 39)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_039_mdv_basefill_039'] = {'inputs': ['mdv_base_universe_d2_039_mdv_basefill_039'], 'func': mdv_base_universe_d3_039_mdv_basefill_039}


def mdv_base_universe_d3_040_mdv_basefill_040(mdv_base_universe_d2_040_mdv_basefill_040):
    return _base_universe_d3(mdv_base_universe_d2_040_mdv_basefill_040, 40)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_040_mdv_basefill_040'] = {'inputs': ['mdv_base_universe_d2_040_mdv_basefill_040'], 'func': mdv_base_universe_d3_040_mdv_basefill_040}


def mdv_base_universe_d3_041_mdv_basefill_041(mdv_base_universe_d2_041_mdv_basefill_041):
    return _base_universe_d3(mdv_base_universe_d2_041_mdv_basefill_041, 41)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_041_mdv_basefill_041'] = {'inputs': ['mdv_base_universe_d2_041_mdv_basefill_041'], 'func': mdv_base_universe_d3_041_mdv_basefill_041}


def mdv_base_universe_d3_042_mdv_basefill_042(mdv_base_universe_d2_042_mdv_basefill_042):
    return _base_universe_d3(mdv_base_universe_d2_042_mdv_basefill_042, 42)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_042_mdv_basefill_042'] = {'inputs': ['mdv_base_universe_d2_042_mdv_basefill_042'], 'func': mdv_base_universe_d3_042_mdv_basefill_042}


def mdv_base_universe_d3_043_mdv_basefill_043(mdv_base_universe_d2_043_mdv_basefill_043):
    return _base_universe_d3(mdv_base_universe_d2_043_mdv_basefill_043, 43)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_043_mdv_basefill_043'] = {'inputs': ['mdv_base_universe_d2_043_mdv_basefill_043'], 'func': mdv_base_universe_d3_043_mdv_basefill_043}


def mdv_base_universe_d3_044_mdv_basefill_044(mdv_base_universe_d2_044_mdv_basefill_044):
    return _base_universe_d3(mdv_base_universe_d2_044_mdv_basefill_044, 44)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_044_mdv_basefill_044'] = {'inputs': ['mdv_base_universe_d2_044_mdv_basefill_044'], 'func': mdv_base_universe_d3_044_mdv_basefill_044}


def mdv_base_universe_d3_045_mdv_basefill_045(mdv_base_universe_d2_045_mdv_basefill_045):
    return _base_universe_d3(mdv_base_universe_d2_045_mdv_basefill_045, 45)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_045_mdv_basefill_045'] = {'inputs': ['mdv_base_universe_d2_045_mdv_basefill_045'], 'func': mdv_base_universe_d3_045_mdv_basefill_045}


def mdv_base_universe_d3_046_mdv_basefill_046(mdv_base_universe_d2_046_mdv_basefill_046):
    return _base_universe_d3(mdv_base_universe_d2_046_mdv_basefill_046, 46)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_046_mdv_basefill_046'] = {'inputs': ['mdv_base_universe_d2_046_mdv_basefill_046'], 'func': mdv_base_universe_d3_046_mdv_basefill_046}


def mdv_base_universe_d3_047_mdv_basefill_047(mdv_base_universe_d2_047_mdv_basefill_047):
    return _base_universe_d3(mdv_base_universe_d2_047_mdv_basefill_047, 47)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_047_mdv_basefill_047'] = {'inputs': ['mdv_base_universe_d2_047_mdv_basefill_047'], 'func': mdv_base_universe_d3_047_mdv_basefill_047}


def mdv_base_universe_d3_048_mdv_basefill_048(mdv_base_universe_d2_048_mdv_basefill_048):
    return _base_universe_d3(mdv_base_universe_d2_048_mdv_basefill_048, 48)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_048_mdv_basefill_048'] = {'inputs': ['mdv_base_universe_d2_048_mdv_basefill_048'], 'func': mdv_base_universe_d3_048_mdv_basefill_048}


def mdv_base_universe_d3_049_mdv_basefill_049(mdv_base_universe_d2_049_mdv_basefill_049):
    return _base_universe_d3(mdv_base_universe_d2_049_mdv_basefill_049, 49)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_049_mdv_basefill_049'] = {'inputs': ['mdv_base_universe_d2_049_mdv_basefill_049'], 'func': mdv_base_universe_d3_049_mdv_basefill_049}


def mdv_base_universe_d3_050_mdv_basefill_050(mdv_base_universe_d2_050_mdv_basefill_050):
    return _base_universe_d3(mdv_base_universe_d2_050_mdv_basefill_050, 50)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_050_mdv_basefill_050'] = {'inputs': ['mdv_base_universe_d2_050_mdv_basefill_050'], 'func': mdv_base_universe_d3_050_mdv_basefill_050}


def mdv_base_universe_d3_051_mdv_basefill_051(mdv_base_universe_d2_051_mdv_basefill_051):
    return _base_universe_d3(mdv_base_universe_d2_051_mdv_basefill_051, 51)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_051_mdv_basefill_051'] = {'inputs': ['mdv_base_universe_d2_051_mdv_basefill_051'], 'func': mdv_base_universe_d3_051_mdv_basefill_051}


def mdv_base_universe_d3_052_mdv_basefill_052(mdv_base_universe_d2_052_mdv_basefill_052):
    return _base_universe_d3(mdv_base_universe_d2_052_mdv_basefill_052, 52)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_052_mdv_basefill_052'] = {'inputs': ['mdv_base_universe_d2_052_mdv_basefill_052'], 'func': mdv_base_universe_d3_052_mdv_basefill_052}


def mdv_base_universe_d3_053_mdv_basefill_053(mdv_base_universe_d2_053_mdv_basefill_053):
    return _base_universe_d3(mdv_base_universe_d2_053_mdv_basefill_053, 53)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_053_mdv_basefill_053'] = {'inputs': ['mdv_base_universe_d2_053_mdv_basefill_053'], 'func': mdv_base_universe_d3_053_mdv_basefill_053}


def mdv_base_universe_d3_054_mdv_basefill_054(mdv_base_universe_d2_054_mdv_basefill_054):
    return _base_universe_d3(mdv_base_universe_d2_054_mdv_basefill_054, 54)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_054_mdv_basefill_054'] = {'inputs': ['mdv_base_universe_d2_054_mdv_basefill_054'], 'func': mdv_base_universe_d3_054_mdv_basefill_054}


def mdv_base_universe_d3_055_mdv_basefill_055(mdv_base_universe_d2_055_mdv_basefill_055):
    return _base_universe_d3(mdv_base_universe_d2_055_mdv_basefill_055, 55)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_055_mdv_basefill_055'] = {'inputs': ['mdv_base_universe_d2_055_mdv_basefill_055'], 'func': mdv_base_universe_d3_055_mdv_basefill_055}


def mdv_base_universe_d3_056_mdv_basefill_056(mdv_base_universe_d2_056_mdv_basefill_056):
    return _base_universe_d3(mdv_base_universe_d2_056_mdv_basefill_056, 56)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_056_mdv_basefill_056'] = {'inputs': ['mdv_base_universe_d2_056_mdv_basefill_056'], 'func': mdv_base_universe_d3_056_mdv_basefill_056}


def mdv_base_universe_d3_057_mdv_basefill_057(mdv_base_universe_d2_057_mdv_basefill_057):
    return _base_universe_d3(mdv_base_universe_d2_057_mdv_basefill_057, 57)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_057_mdv_basefill_057'] = {'inputs': ['mdv_base_universe_d2_057_mdv_basefill_057'], 'func': mdv_base_universe_d3_057_mdv_basefill_057}


def mdv_base_universe_d3_058_mdv_basefill_058(mdv_base_universe_d2_058_mdv_basefill_058):
    return _base_universe_d3(mdv_base_universe_d2_058_mdv_basefill_058, 58)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_058_mdv_basefill_058'] = {'inputs': ['mdv_base_universe_d2_058_mdv_basefill_058'], 'func': mdv_base_universe_d3_058_mdv_basefill_058}


def mdv_base_universe_d3_059_mdv_basefill_059(mdv_base_universe_d2_059_mdv_basefill_059):
    return _base_universe_d3(mdv_base_universe_d2_059_mdv_basefill_059, 59)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_059_mdv_basefill_059'] = {'inputs': ['mdv_base_universe_d2_059_mdv_basefill_059'], 'func': mdv_base_universe_d3_059_mdv_basefill_059}


def mdv_base_universe_d3_060_mdv_basefill_060(mdv_base_universe_d2_060_mdv_basefill_060):
    return _base_universe_d3(mdv_base_universe_d2_060_mdv_basefill_060, 60)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_060_mdv_basefill_060'] = {'inputs': ['mdv_base_universe_d2_060_mdv_basefill_060'], 'func': mdv_base_universe_d3_060_mdv_basefill_060}


def mdv_base_universe_d3_061_mdv_basefill_061(mdv_base_universe_d2_061_mdv_basefill_061):
    return _base_universe_d3(mdv_base_universe_d2_061_mdv_basefill_061, 61)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_061_mdv_basefill_061'] = {'inputs': ['mdv_base_universe_d2_061_mdv_basefill_061'], 'func': mdv_base_universe_d3_061_mdv_basefill_061}


def mdv_base_universe_d3_062_mdv_basefill_062(mdv_base_universe_d2_062_mdv_basefill_062):
    return _base_universe_d3(mdv_base_universe_d2_062_mdv_basefill_062, 62)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_062_mdv_basefill_062'] = {'inputs': ['mdv_base_universe_d2_062_mdv_basefill_062'], 'func': mdv_base_universe_d3_062_mdv_basefill_062}


def mdv_base_universe_d3_063_mdv_basefill_063(mdv_base_universe_d2_063_mdv_basefill_063):
    return _base_universe_d3(mdv_base_universe_d2_063_mdv_basefill_063, 63)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_063_mdv_basefill_063'] = {'inputs': ['mdv_base_universe_d2_063_mdv_basefill_063'], 'func': mdv_base_universe_d3_063_mdv_basefill_063}


def mdv_base_universe_d3_064_mdv_basefill_064(mdv_base_universe_d2_064_mdv_basefill_064):
    return _base_universe_d3(mdv_base_universe_d2_064_mdv_basefill_064, 64)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_064_mdv_basefill_064'] = {'inputs': ['mdv_base_universe_d2_064_mdv_basefill_064'], 'func': mdv_base_universe_d3_064_mdv_basefill_064}


def mdv_base_universe_d3_065_mdv_basefill_065(mdv_base_universe_d2_065_mdv_basefill_065):
    return _base_universe_d3(mdv_base_universe_d2_065_mdv_basefill_065, 65)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_065_mdv_basefill_065'] = {'inputs': ['mdv_base_universe_d2_065_mdv_basefill_065'], 'func': mdv_base_universe_d3_065_mdv_basefill_065}


def mdv_base_universe_d3_066_mdv_basefill_066(mdv_base_universe_d2_066_mdv_basefill_066):
    return _base_universe_d3(mdv_base_universe_d2_066_mdv_basefill_066, 66)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_066_mdv_basefill_066'] = {'inputs': ['mdv_base_universe_d2_066_mdv_basefill_066'], 'func': mdv_base_universe_d3_066_mdv_basefill_066}


def mdv_base_universe_d3_067_mdv_basefill_067(mdv_base_universe_d2_067_mdv_basefill_067):
    return _base_universe_d3(mdv_base_universe_d2_067_mdv_basefill_067, 67)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_067_mdv_basefill_067'] = {'inputs': ['mdv_base_universe_d2_067_mdv_basefill_067'], 'func': mdv_base_universe_d3_067_mdv_basefill_067}


def mdv_base_universe_d3_068_mdv_basefill_068(mdv_base_universe_d2_068_mdv_basefill_068):
    return _base_universe_d3(mdv_base_universe_d2_068_mdv_basefill_068, 68)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_068_mdv_basefill_068'] = {'inputs': ['mdv_base_universe_d2_068_mdv_basefill_068'], 'func': mdv_base_universe_d3_068_mdv_basefill_068}


def mdv_base_universe_d3_069_mdv_basefill_069(mdv_base_universe_d2_069_mdv_basefill_069):
    return _base_universe_d3(mdv_base_universe_d2_069_mdv_basefill_069, 69)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_069_mdv_basefill_069'] = {'inputs': ['mdv_base_universe_d2_069_mdv_basefill_069'], 'func': mdv_base_universe_d3_069_mdv_basefill_069}


def mdv_base_universe_d3_070_mdv_basefill_070(mdv_base_universe_d2_070_mdv_basefill_070):
    return _base_universe_d3(mdv_base_universe_d2_070_mdv_basefill_070, 70)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_070_mdv_basefill_070'] = {'inputs': ['mdv_base_universe_d2_070_mdv_basefill_070'], 'func': mdv_base_universe_d3_070_mdv_basefill_070}


def mdv_base_universe_d3_071_mdv_basefill_071(mdv_base_universe_d2_071_mdv_basefill_071):
    return _base_universe_d3(mdv_base_universe_d2_071_mdv_basefill_071, 71)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_071_mdv_basefill_071'] = {'inputs': ['mdv_base_universe_d2_071_mdv_basefill_071'], 'func': mdv_base_universe_d3_071_mdv_basefill_071}


def mdv_base_universe_d3_072_mdv_basefill_072(mdv_base_universe_d2_072_mdv_basefill_072):
    return _base_universe_d3(mdv_base_universe_d2_072_mdv_basefill_072, 72)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_072_mdv_basefill_072'] = {'inputs': ['mdv_base_universe_d2_072_mdv_basefill_072'], 'func': mdv_base_universe_d3_072_mdv_basefill_072}


def mdv_base_universe_d3_073_mdv_basefill_073(mdv_base_universe_d2_073_mdv_basefill_073):
    return _base_universe_d3(mdv_base_universe_d2_073_mdv_basefill_073, 73)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_073_mdv_basefill_073'] = {'inputs': ['mdv_base_universe_d2_073_mdv_basefill_073'], 'func': mdv_base_universe_d3_073_mdv_basefill_073}


def mdv_base_universe_d3_074_mdv_basefill_074(mdv_base_universe_d2_074_mdv_basefill_074):
    return _base_universe_d3(mdv_base_universe_d2_074_mdv_basefill_074, 74)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_074_mdv_basefill_074'] = {'inputs': ['mdv_base_universe_d2_074_mdv_basefill_074'], 'func': mdv_base_universe_d3_074_mdv_basefill_074}


def mdv_base_universe_d3_075_mdv_basefill_075(mdv_base_universe_d2_075_mdv_basefill_075):
    return _base_universe_d3(mdv_base_universe_d2_075_mdv_basefill_075, 75)
MDV_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['mdv_base_universe_d3_075_mdv_basefill_075'] = {'inputs': ['mdv_base_universe_d2_075_mdv_basefill_075'], 'func': mdv_base_universe_d3_075_mdv_basefill_075}
