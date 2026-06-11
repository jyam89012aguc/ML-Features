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



def tbd_001_return_decay_accel_1(tbd_001_return_decay_roc_1):
    feature = _s(tbd_001_return_decay_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def tbd_007_return_decay_accel_5(tbd_007_return_decay_roc_5):
    feature = _s(tbd_007_return_decay_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def tbd_013_return_decay_accel_42(tbd_013_return_decay_roc_42):
    feature = _s(tbd_013_return_decay_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def tbd_179_tbd_019_return_decay_42_019_accel_126(tbd_154_tbd_019_return_decay_42_019_roc_126):
    feature = _s(tbd_154_tbd_019_return_decay_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def tbd_180_tbd_025_return_decay_5_025_accel_378(tbd_155_tbd_025_return_decay_5_025_roc_378):
    feature = _s(tbd_155_tbd_025_return_decay_5_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















TREND_BREAKDOWN_REGISTRY_3RD_DERIVATIVES = {
    'tbd_001_return_decay_accel_1': {'inputs': ['tbd_001_return_decay_roc_1'], 'func': tbd_001_return_decay_accel_1},
    'tbd_007_return_decay_accel_5': {'inputs': ['tbd_007_return_decay_roc_5'], 'func': tbd_007_return_decay_accel_5},
    'tbd_013_return_decay_accel_42': {'inputs': ['tbd_013_return_decay_roc_42'], 'func': tbd_013_return_decay_accel_42},
    'tbd_179_tbd_019_return_decay_42_019_accel_126': {'inputs': ['tbd_154_tbd_019_return_decay_42_019_roc_126'], 'func': tbd_179_tbd_019_return_decay_42_019_accel_126},
    'tbd_180_tbd_025_return_decay_5_025_accel_378': {'inputs': ['tbd_155_tbd_025_return_decay_5_025_roc_378'], 'func': tbd_180_tbd_025_return_decay_5_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def tb_replacement_d3_001(tb_replacement_d2_001):
    feature = _clean(tb_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_001'] = {'inputs': ['tb_replacement_d2_001'], 'func': tb_replacement_d3_001}


def tb_replacement_d3_002(tb_replacement_d2_002):
    feature = _clean(tb_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_002'] = {'inputs': ['tb_replacement_d2_002'], 'func': tb_replacement_d3_002}


def tb_replacement_d3_003(tb_replacement_d2_003):
    feature = _clean(tb_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_003'] = {'inputs': ['tb_replacement_d2_003'], 'func': tb_replacement_d3_003}


def tb_replacement_d3_004(tb_replacement_d2_004):
    feature = _clean(tb_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_004'] = {'inputs': ['tb_replacement_d2_004'], 'func': tb_replacement_d3_004}


def tb_replacement_d3_005(tb_replacement_d2_005):
    feature = _clean(tb_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_005'] = {'inputs': ['tb_replacement_d2_005'], 'func': tb_replacement_d3_005}


def tb_replacement_d3_006(tb_replacement_d2_006):
    feature = _clean(tb_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_006'] = {'inputs': ['tb_replacement_d2_006'], 'func': tb_replacement_d3_006}


def tb_replacement_d3_007(tb_replacement_d2_007):
    feature = _clean(tb_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_007'] = {'inputs': ['tb_replacement_d2_007'], 'func': tb_replacement_d3_007}


def tb_replacement_d3_008(tb_replacement_d2_008):
    feature = _clean(tb_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_008'] = {'inputs': ['tb_replacement_d2_008'], 'func': tb_replacement_d3_008}


def tb_replacement_d3_009(tb_replacement_d2_009):
    feature = _clean(tb_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_009'] = {'inputs': ['tb_replacement_d2_009'], 'func': tb_replacement_d3_009}


def tb_replacement_d3_010(tb_replacement_d2_010):
    feature = _clean(tb_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_010'] = {'inputs': ['tb_replacement_d2_010'], 'func': tb_replacement_d3_010}


def tb_replacement_d3_011(tb_replacement_d2_011):
    feature = _clean(tb_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_011'] = {'inputs': ['tb_replacement_d2_011'], 'func': tb_replacement_d3_011}


def tb_replacement_d3_012(tb_replacement_d2_012):
    feature = _clean(tb_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_012'] = {'inputs': ['tb_replacement_d2_012'], 'func': tb_replacement_d3_012}


def tb_replacement_d3_013(tb_replacement_d2_013):
    feature = _clean(tb_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_013'] = {'inputs': ['tb_replacement_d2_013'], 'func': tb_replacement_d3_013}


def tb_replacement_d3_014(tb_replacement_d2_014):
    feature = _clean(tb_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_014'] = {'inputs': ['tb_replacement_d2_014'], 'func': tb_replacement_d3_014}


def tb_replacement_d3_015(tb_replacement_d2_015):
    feature = _clean(tb_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_015'] = {'inputs': ['tb_replacement_d2_015'], 'func': tb_replacement_d3_015}


def tb_replacement_d3_016(tb_replacement_d2_016):
    feature = _clean(tb_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_016'] = {'inputs': ['tb_replacement_d2_016'], 'func': tb_replacement_d3_016}


def tb_replacement_d3_017(tb_replacement_d2_017):
    feature = _clean(tb_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_017'] = {'inputs': ['tb_replacement_d2_017'], 'func': tb_replacement_d3_017}


def tb_replacement_d3_018(tb_replacement_d2_018):
    feature = _clean(tb_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_018'] = {'inputs': ['tb_replacement_d2_018'], 'func': tb_replacement_d3_018}


def tb_replacement_d3_019(tb_replacement_d2_019):
    feature = _clean(tb_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_019'] = {'inputs': ['tb_replacement_d2_019'], 'func': tb_replacement_d3_019}


def tb_replacement_d3_020(tb_replacement_d2_020):
    feature = _clean(tb_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_020'] = {'inputs': ['tb_replacement_d2_020'], 'func': tb_replacement_d3_020}


def tb_replacement_d3_021(tb_replacement_d2_021):
    feature = _clean(tb_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_021'] = {'inputs': ['tb_replacement_d2_021'], 'func': tb_replacement_d3_021}


def tb_replacement_d3_022(tb_replacement_d2_022):
    feature = _clean(tb_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_022'] = {'inputs': ['tb_replacement_d2_022'], 'func': tb_replacement_d3_022}


def tb_replacement_d3_023(tb_replacement_d2_023):
    feature = _clean(tb_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_023'] = {'inputs': ['tb_replacement_d2_023'], 'func': tb_replacement_d3_023}


def tb_replacement_d3_024(tb_replacement_d2_024):
    feature = _clean(tb_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_024'] = {'inputs': ['tb_replacement_d2_024'], 'func': tb_replacement_d3_024}


def tb_replacement_d3_025(tb_replacement_d2_025):
    feature = _clean(tb_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_025'] = {'inputs': ['tb_replacement_d2_025'], 'func': tb_replacement_d3_025}


def tb_replacement_d3_026(tb_replacement_d2_026):
    feature = _clean(tb_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_026'] = {'inputs': ['tb_replacement_d2_026'], 'func': tb_replacement_d3_026}


def tb_replacement_d3_027(tb_replacement_d2_027):
    feature = _clean(tb_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_027'] = {'inputs': ['tb_replacement_d2_027'], 'func': tb_replacement_d3_027}


def tb_replacement_d3_028(tb_replacement_d2_028):
    feature = _clean(tb_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_028'] = {'inputs': ['tb_replacement_d2_028'], 'func': tb_replacement_d3_028}


def tb_replacement_d3_029(tb_replacement_d2_029):
    feature = _clean(tb_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_029'] = {'inputs': ['tb_replacement_d2_029'], 'func': tb_replacement_d3_029}


def tb_replacement_d3_030(tb_replacement_d2_030):
    feature = _clean(tb_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_030'] = {'inputs': ['tb_replacement_d2_030'], 'func': tb_replacement_d3_030}


def tb_replacement_d3_031(tb_replacement_d2_031):
    feature = _clean(tb_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_031'] = {'inputs': ['tb_replacement_d2_031'], 'func': tb_replacement_d3_031}


def tb_replacement_d3_032(tb_replacement_d2_032):
    feature = _clean(tb_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_032'] = {'inputs': ['tb_replacement_d2_032'], 'func': tb_replacement_d3_032}


def tb_replacement_d3_033(tb_replacement_d2_033):
    feature = _clean(tb_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_033'] = {'inputs': ['tb_replacement_d2_033'], 'func': tb_replacement_d3_033}


def tb_replacement_d3_034(tb_replacement_d2_034):
    feature = _clean(tb_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_034'] = {'inputs': ['tb_replacement_d2_034'], 'func': tb_replacement_d3_034}


def tb_replacement_d3_035(tb_replacement_d2_035):
    feature = _clean(tb_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_035'] = {'inputs': ['tb_replacement_d2_035'], 'func': tb_replacement_d3_035}


def tb_replacement_d3_036(tb_replacement_d2_036):
    feature = _clean(tb_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_036'] = {'inputs': ['tb_replacement_d2_036'], 'func': tb_replacement_d3_036}


def tb_replacement_d3_037(tb_replacement_d2_037):
    feature = _clean(tb_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_037'] = {'inputs': ['tb_replacement_d2_037'], 'func': tb_replacement_d3_037}


def tb_replacement_d3_038(tb_replacement_d2_038):
    feature = _clean(tb_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_038'] = {'inputs': ['tb_replacement_d2_038'], 'func': tb_replacement_d3_038}


def tb_replacement_d3_039(tb_replacement_d2_039):
    feature = _clean(tb_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_039'] = {'inputs': ['tb_replacement_d2_039'], 'func': tb_replacement_d3_039}


def tb_replacement_d3_040(tb_replacement_d2_040):
    feature = _clean(tb_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_040'] = {'inputs': ['tb_replacement_d2_040'], 'func': tb_replacement_d3_040}


def tb_replacement_d3_041(tb_replacement_d2_041):
    feature = _clean(tb_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_041'] = {'inputs': ['tb_replacement_d2_041'], 'func': tb_replacement_d3_041}


def tb_replacement_d3_042(tb_replacement_d2_042):
    feature = _clean(tb_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_042'] = {'inputs': ['tb_replacement_d2_042'], 'func': tb_replacement_d3_042}


def tb_replacement_d3_043(tb_replacement_d2_043):
    feature = _clean(tb_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_043'] = {'inputs': ['tb_replacement_d2_043'], 'func': tb_replacement_d3_043}


def tb_replacement_d3_044(tb_replacement_d2_044):
    feature = _clean(tb_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_044'] = {'inputs': ['tb_replacement_d2_044'], 'func': tb_replacement_d3_044}


def tb_replacement_d3_045(tb_replacement_d2_045):
    feature = _clean(tb_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_045'] = {'inputs': ['tb_replacement_d2_045'], 'func': tb_replacement_d3_045}


def tb_replacement_d3_046(tb_replacement_d2_046):
    feature = _clean(tb_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_046'] = {'inputs': ['tb_replacement_d2_046'], 'func': tb_replacement_d3_046}


def tb_replacement_d3_047(tb_replacement_d2_047):
    feature = _clean(tb_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_047'] = {'inputs': ['tb_replacement_d2_047'], 'func': tb_replacement_d3_047}


def tb_replacement_d3_048(tb_replacement_d2_048):
    feature = _clean(tb_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_048'] = {'inputs': ['tb_replacement_d2_048'], 'func': tb_replacement_d3_048}


def tb_replacement_d3_049(tb_replacement_d2_049):
    feature = _clean(tb_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_049'] = {'inputs': ['tb_replacement_d2_049'], 'func': tb_replacement_d3_049}


def tb_replacement_d3_050(tb_replacement_d2_050):
    feature = _clean(tb_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_050'] = {'inputs': ['tb_replacement_d2_050'], 'func': tb_replacement_d3_050}


def tb_replacement_d3_051(tb_replacement_d2_051):
    feature = _clean(tb_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_051'] = {'inputs': ['tb_replacement_d2_051'], 'func': tb_replacement_d3_051}


def tb_replacement_d3_052(tb_replacement_d2_052):
    feature = _clean(tb_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_052'] = {'inputs': ['tb_replacement_d2_052'], 'func': tb_replacement_d3_052}


def tb_replacement_d3_053(tb_replacement_d2_053):
    feature = _clean(tb_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_053'] = {'inputs': ['tb_replacement_d2_053'], 'func': tb_replacement_d3_053}


def tb_replacement_d3_054(tb_replacement_d2_054):
    feature = _clean(tb_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_054'] = {'inputs': ['tb_replacement_d2_054'], 'func': tb_replacement_d3_054}


def tb_replacement_d3_055(tb_replacement_d2_055):
    feature = _clean(tb_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_055'] = {'inputs': ['tb_replacement_d2_055'], 'func': tb_replacement_d3_055}


def tb_replacement_d3_056(tb_replacement_d2_056):
    feature = _clean(tb_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_056'] = {'inputs': ['tb_replacement_d2_056'], 'func': tb_replacement_d3_056}


def tb_replacement_d3_057(tb_replacement_d2_057):
    feature = _clean(tb_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_057'] = {'inputs': ['tb_replacement_d2_057'], 'func': tb_replacement_d3_057}


def tb_replacement_d3_058(tb_replacement_d2_058):
    feature = _clean(tb_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_058'] = {'inputs': ['tb_replacement_d2_058'], 'func': tb_replacement_d3_058}


def tb_replacement_d3_059(tb_replacement_d2_059):
    feature = _clean(tb_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_059'] = {'inputs': ['tb_replacement_d2_059'], 'func': tb_replacement_d3_059}


def tb_replacement_d3_060(tb_replacement_d2_060):
    feature = _clean(tb_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_060'] = {'inputs': ['tb_replacement_d2_060'], 'func': tb_replacement_d3_060}


def tb_replacement_d3_061(tb_replacement_d2_061):
    feature = _clean(tb_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_061'] = {'inputs': ['tb_replacement_d2_061'], 'func': tb_replacement_d3_061}


def tb_replacement_d3_062(tb_replacement_d2_062):
    feature = _clean(tb_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_062'] = {'inputs': ['tb_replacement_d2_062'], 'func': tb_replacement_d3_062}


def tb_replacement_d3_063(tb_replacement_d2_063):
    feature = _clean(tb_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_063'] = {'inputs': ['tb_replacement_d2_063'], 'func': tb_replacement_d3_063}


def tb_replacement_d3_064(tb_replacement_d2_064):
    feature = _clean(tb_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_064'] = {'inputs': ['tb_replacement_d2_064'], 'func': tb_replacement_d3_064}


def tb_replacement_d3_065(tb_replacement_d2_065):
    feature = _clean(tb_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_065'] = {'inputs': ['tb_replacement_d2_065'], 'func': tb_replacement_d3_065}


def tb_replacement_d3_066(tb_replacement_d2_066):
    feature = _clean(tb_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_066'] = {'inputs': ['tb_replacement_d2_066'], 'func': tb_replacement_d3_066}


def tb_replacement_d3_067(tb_replacement_d2_067):
    feature = _clean(tb_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_067'] = {'inputs': ['tb_replacement_d2_067'], 'func': tb_replacement_d3_067}


def tb_replacement_d3_068(tb_replacement_d2_068):
    feature = _clean(tb_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_068'] = {'inputs': ['tb_replacement_d2_068'], 'func': tb_replacement_d3_068}


def tb_replacement_d3_069(tb_replacement_d2_069):
    feature = _clean(tb_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_069'] = {'inputs': ['tb_replacement_d2_069'], 'func': tb_replacement_d3_069}


def tb_replacement_d3_070(tb_replacement_d2_070):
    feature = _clean(tb_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_070'] = {'inputs': ['tb_replacement_d2_070'], 'func': tb_replacement_d3_070}


def tb_replacement_d3_071(tb_replacement_d2_071):
    feature = _clean(tb_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_071'] = {'inputs': ['tb_replacement_d2_071'], 'func': tb_replacement_d3_071}


def tb_replacement_d3_072(tb_replacement_d2_072):
    feature = _clean(tb_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_072'] = {'inputs': ['tb_replacement_d2_072'], 'func': tb_replacement_d3_072}


def tb_replacement_d3_073(tb_replacement_d2_073):
    feature = _clean(tb_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_073'] = {'inputs': ['tb_replacement_d2_073'], 'func': tb_replacement_d3_073}


def tb_replacement_d3_074(tb_replacement_d2_074):
    feature = _clean(tb_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_074'] = {'inputs': ['tb_replacement_d2_074'], 'func': tb_replacement_d3_074}


def tb_replacement_d3_075(tb_replacement_d2_075):
    feature = _clean(tb_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_075'] = {'inputs': ['tb_replacement_d2_075'], 'func': tb_replacement_d3_075}


def tb_replacement_d3_076(tb_replacement_d2_076):
    feature = _clean(tb_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_076'] = {'inputs': ['tb_replacement_d2_076'], 'func': tb_replacement_d3_076}


def tb_replacement_d3_077(tb_replacement_d2_077):
    feature = _clean(tb_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_077'] = {'inputs': ['tb_replacement_d2_077'], 'func': tb_replacement_d3_077}


def tb_replacement_d3_078(tb_replacement_d2_078):
    feature = _clean(tb_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_078'] = {'inputs': ['tb_replacement_d2_078'], 'func': tb_replacement_d3_078}


def tb_replacement_d3_079(tb_replacement_d2_079):
    feature = _clean(tb_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_079'] = {'inputs': ['tb_replacement_d2_079'], 'func': tb_replacement_d3_079}


def tb_replacement_d3_080(tb_replacement_d2_080):
    feature = _clean(tb_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_080'] = {'inputs': ['tb_replacement_d2_080'], 'func': tb_replacement_d3_080}


def tb_replacement_d3_081(tb_replacement_d2_081):
    feature = _clean(tb_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_081'] = {'inputs': ['tb_replacement_d2_081'], 'func': tb_replacement_d3_081}


def tb_replacement_d3_082(tb_replacement_d2_082):
    feature = _clean(tb_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_082'] = {'inputs': ['tb_replacement_d2_082'], 'func': tb_replacement_d3_082}


def tb_replacement_d3_083(tb_replacement_d2_083):
    feature = _clean(tb_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_083'] = {'inputs': ['tb_replacement_d2_083'], 'func': tb_replacement_d3_083}


def tb_replacement_d3_084(tb_replacement_d2_084):
    feature = _clean(tb_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_084'] = {'inputs': ['tb_replacement_d2_084'], 'func': tb_replacement_d3_084}


def tb_replacement_d3_085(tb_replacement_d2_085):
    feature = _clean(tb_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_085'] = {'inputs': ['tb_replacement_d2_085'], 'func': tb_replacement_d3_085}


def tb_replacement_d3_086(tb_replacement_d2_086):
    feature = _clean(tb_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_086'] = {'inputs': ['tb_replacement_d2_086'], 'func': tb_replacement_d3_086}


def tb_replacement_d3_087(tb_replacement_d2_087):
    feature = _clean(tb_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_087'] = {'inputs': ['tb_replacement_d2_087'], 'func': tb_replacement_d3_087}


def tb_replacement_d3_088(tb_replacement_d2_088):
    feature = _clean(tb_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_088'] = {'inputs': ['tb_replacement_d2_088'], 'func': tb_replacement_d3_088}


def tb_replacement_d3_089(tb_replacement_d2_089):
    feature = _clean(tb_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_089'] = {'inputs': ['tb_replacement_d2_089'], 'func': tb_replacement_d3_089}


def tb_replacement_d3_090(tb_replacement_d2_090):
    feature = _clean(tb_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_090'] = {'inputs': ['tb_replacement_d2_090'], 'func': tb_replacement_d3_090}


def tb_replacement_d3_091(tb_replacement_d2_091):
    feature = _clean(tb_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_091'] = {'inputs': ['tb_replacement_d2_091'], 'func': tb_replacement_d3_091}


def tb_replacement_d3_092(tb_replacement_d2_092):
    feature = _clean(tb_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_092'] = {'inputs': ['tb_replacement_d2_092'], 'func': tb_replacement_d3_092}


def tb_replacement_d3_093(tb_replacement_d2_093):
    feature = _clean(tb_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_093'] = {'inputs': ['tb_replacement_d2_093'], 'func': tb_replacement_d3_093}


def tb_replacement_d3_094(tb_replacement_d2_094):
    feature = _clean(tb_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_094'] = {'inputs': ['tb_replacement_d2_094'], 'func': tb_replacement_d3_094}


def tb_replacement_d3_095(tb_replacement_d2_095):
    feature = _clean(tb_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_095'] = {'inputs': ['tb_replacement_d2_095'], 'func': tb_replacement_d3_095}


def tb_replacement_d3_096(tb_replacement_d2_096):
    feature = _clean(tb_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_096'] = {'inputs': ['tb_replacement_d2_096'], 'func': tb_replacement_d3_096}


def tb_replacement_d3_097(tb_replacement_d2_097):
    feature = _clean(tb_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_097'] = {'inputs': ['tb_replacement_d2_097'], 'func': tb_replacement_d3_097}


def tb_replacement_d3_098(tb_replacement_d2_098):
    feature = _clean(tb_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_098'] = {'inputs': ['tb_replacement_d2_098'], 'func': tb_replacement_d3_098}


def tb_replacement_d3_099(tb_replacement_d2_099):
    feature = _clean(tb_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_099'] = {'inputs': ['tb_replacement_d2_099'], 'func': tb_replacement_d3_099}


def tb_replacement_d3_100(tb_replacement_d2_100):
    feature = _clean(tb_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_100'] = {'inputs': ['tb_replacement_d2_100'], 'func': tb_replacement_d3_100}


def tb_replacement_d3_101(tb_replacement_d2_101):
    feature = _clean(tb_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_101'] = {'inputs': ['tb_replacement_d2_101'], 'func': tb_replacement_d3_101}


def tb_replacement_d3_102(tb_replacement_d2_102):
    feature = _clean(tb_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_102'] = {'inputs': ['tb_replacement_d2_102'], 'func': tb_replacement_d3_102}


def tb_replacement_d3_103(tb_replacement_d2_103):
    feature = _clean(tb_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_103'] = {'inputs': ['tb_replacement_d2_103'], 'func': tb_replacement_d3_103}


def tb_replacement_d3_104(tb_replacement_d2_104):
    feature = _clean(tb_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_104'] = {'inputs': ['tb_replacement_d2_104'], 'func': tb_replacement_d3_104}


def tb_replacement_d3_105(tb_replacement_d2_105):
    feature = _clean(tb_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_105'] = {'inputs': ['tb_replacement_d2_105'], 'func': tb_replacement_d3_105}


def tb_replacement_d3_106(tb_replacement_d2_106):
    feature = _clean(tb_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_106'] = {'inputs': ['tb_replacement_d2_106'], 'func': tb_replacement_d3_106}


def tb_replacement_d3_107(tb_replacement_d2_107):
    feature = _clean(tb_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_107'] = {'inputs': ['tb_replacement_d2_107'], 'func': tb_replacement_d3_107}


def tb_replacement_d3_108(tb_replacement_d2_108):
    feature = _clean(tb_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_108'] = {'inputs': ['tb_replacement_d2_108'], 'func': tb_replacement_d3_108}


def tb_replacement_d3_109(tb_replacement_d2_109):
    feature = _clean(tb_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_109'] = {'inputs': ['tb_replacement_d2_109'], 'func': tb_replacement_d3_109}


def tb_replacement_d3_110(tb_replacement_d2_110):
    feature = _clean(tb_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_110'] = {'inputs': ['tb_replacement_d2_110'], 'func': tb_replacement_d3_110}


def tb_replacement_d3_111(tb_replacement_d2_111):
    feature = _clean(tb_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_111'] = {'inputs': ['tb_replacement_d2_111'], 'func': tb_replacement_d3_111}


def tb_replacement_d3_112(tb_replacement_d2_112):
    feature = _clean(tb_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_112'] = {'inputs': ['tb_replacement_d2_112'], 'func': tb_replacement_d3_112}


def tb_replacement_d3_113(tb_replacement_d2_113):
    feature = _clean(tb_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_113'] = {'inputs': ['tb_replacement_d2_113'], 'func': tb_replacement_d3_113}


def tb_replacement_d3_114(tb_replacement_d2_114):
    feature = _clean(tb_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_114'] = {'inputs': ['tb_replacement_d2_114'], 'func': tb_replacement_d3_114}


def tb_replacement_d3_115(tb_replacement_d2_115):
    feature = _clean(tb_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_115'] = {'inputs': ['tb_replacement_d2_115'], 'func': tb_replacement_d3_115}


def tb_replacement_d3_116(tb_replacement_d2_116):
    feature = _clean(tb_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_116'] = {'inputs': ['tb_replacement_d2_116'], 'func': tb_replacement_d3_116}


def tb_replacement_d3_117(tb_replacement_d2_117):
    feature = _clean(tb_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_117'] = {'inputs': ['tb_replacement_d2_117'], 'func': tb_replacement_d3_117}


def tb_replacement_d3_118(tb_replacement_d2_118):
    feature = _clean(tb_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_118'] = {'inputs': ['tb_replacement_d2_118'], 'func': tb_replacement_d3_118}


def tb_replacement_d3_119(tb_replacement_d2_119):
    feature = _clean(tb_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_119'] = {'inputs': ['tb_replacement_d2_119'], 'func': tb_replacement_d3_119}


def tb_replacement_d3_120(tb_replacement_d2_120):
    feature = _clean(tb_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_120'] = {'inputs': ['tb_replacement_d2_120'], 'func': tb_replacement_d3_120}


def tb_replacement_d3_121(tb_replacement_d2_121):
    feature = _clean(tb_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_121'] = {'inputs': ['tb_replacement_d2_121'], 'func': tb_replacement_d3_121}


def tb_replacement_d3_122(tb_replacement_d2_122):
    feature = _clean(tb_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_122'] = {'inputs': ['tb_replacement_d2_122'], 'func': tb_replacement_d3_122}


def tb_replacement_d3_123(tb_replacement_d2_123):
    feature = _clean(tb_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_123'] = {'inputs': ['tb_replacement_d2_123'], 'func': tb_replacement_d3_123}


def tb_replacement_d3_124(tb_replacement_d2_124):
    feature = _clean(tb_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_124'] = {'inputs': ['tb_replacement_d2_124'], 'func': tb_replacement_d3_124}


def tb_replacement_d3_125(tb_replacement_d2_125):
    feature = _clean(tb_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_125'] = {'inputs': ['tb_replacement_d2_125'], 'func': tb_replacement_d3_125}


def tb_replacement_d3_126(tb_replacement_d2_126):
    feature = _clean(tb_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_126'] = {'inputs': ['tb_replacement_d2_126'], 'func': tb_replacement_d3_126}


def tb_replacement_d3_127(tb_replacement_d2_127):
    feature = _clean(tb_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_127'] = {'inputs': ['tb_replacement_d2_127'], 'func': tb_replacement_d3_127}


def tb_replacement_d3_128(tb_replacement_d2_128):
    feature = _clean(tb_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_128'] = {'inputs': ['tb_replacement_d2_128'], 'func': tb_replacement_d3_128}


def tb_replacement_d3_129(tb_replacement_d2_129):
    feature = _clean(tb_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_129'] = {'inputs': ['tb_replacement_d2_129'], 'func': tb_replacement_d3_129}


def tb_replacement_d3_130(tb_replacement_d2_130):
    feature = _clean(tb_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_130'] = {'inputs': ['tb_replacement_d2_130'], 'func': tb_replacement_d3_130}


def tb_replacement_d3_131(tb_replacement_d2_131):
    feature = _clean(tb_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_131'] = {'inputs': ['tb_replacement_d2_131'], 'func': tb_replacement_d3_131}


def tb_replacement_d3_132(tb_replacement_d2_132):
    feature = _clean(tb_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_132'] = {'inputs': ['tb_replacement_d2_132'], 'func': tb_replacement_d3_132}


def tb_replacement_d3_133(tb_replacement_d2_133):
    feature = _clean(tb_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_133'] = {'inputs': ['tb_replacement_d2_133'], 'func': tb_replacement_d3_133}


def tb_replacement_d3_134(tb_replacement_d2_134):
    feature = _clean(tb_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_134'] = {'inputs': ['tb_replacement_d2_134'], 'func': tb_replacement_d3_134}


def tb_replacement_d3_135(tb_replacement_d2_135):
    feature = _clean(tb_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_135'] = {'inputs': ['tb_replacement_d2_135'], 'func': tb_replacement_d3_135}


def tb_replacement_d3_136(tb_replacement_d2_136):
    feature = _clean(tb_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_136'] = {'inputs': ['tb_replacement_d2_136'], 'func': tb_replacement_d3_136}


def tb_replacement_d3_137(tb_replacement_d2_137):
    feature = _clean(tb_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_137'] = {'inputs': ['tb_replacement_d2_137'], 'func': tb_replacement_d3_137}


def tb_replacement_d3_138(tb_replacement_d2_138):
    feature = _clean(tb_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_138'] = {'inputs': ['tb_replacement_d2_138'], 'func': tb_replacement_d3_138}


def tb_replacement_d3_139(tb_replacement_d2_139):
    feature = _clean(tb_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_139'] = {'inputs': ['tb_replacement_d2_139'], 'func': tb_replacement_d3_139}


def tb_replacement_d3_140(tb_replacement_d2_140):
    feature = _clean(tb_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_140'] = {'inputs': ['tb_replacement_d2_140'], 'func': tb_replacement_d3_140}


def tb_replacement_d3_141(tb_replacement_d2_141):
    feature = _clean(tb_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_141'] = {'inputs': ['tb_replacement_d2_141'], 'func': tb_replacement_d3_141}


def tb_replacement_d3_142(tb_replacement_d2_142):
    feature = _clean(tb_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_142'] = {'inputs': ['tb_replacement_d2_142'], 'func': tb_replacement_d3_142}


def tb_replacement_d3_143(tb_replacement_d2_143):
    feature = _clean(tb_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_143'] = {'inputs': ['tb_replacement_d2_143'], 'func': tb_replacement_d3_143}


def tb_replacement_d3_144(tb_replacement_d2_144):
    feature = _clean(tb_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_144'] = {'inputs': ['tb_replacement_d2_144'], 'func': tb_replacement_d3_144}


def tb_replacement_d3_145(tb_replacement_d2_145):
    feature = _clean(tb_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_145'] = {'inputs': ['tb_replacement_d2_145'], 'func': tb_replacement_d3_145}


def tb_replacement_d3_146(tb_replacement_d2_146):
    feature = _clean(tb_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_146'] = {'inputs': ['tb_replacement_d2_146'], 'func': tb_replacement_d3_146}


def tb_replacement_d3_147(tb_replacement_d2_147):
    feature = _clean(tb_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_147'] = {'inputs': ['tb_replacement_d2_147'], 'func': tb_replacement_d3_147}


def tb_replacement_d3_148(tb_replacement_d2_148):
    feature = _clean(tb_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_148'] = {'inputs': ['tb_replacement_d2_148'], 'func': tb_replacement_d3_148}


def tb_replacement_d3_149(tb_replacement_d2_149):
    feature = _clean(tb_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_149'] = {'inputs': ['tb_replacement_d2_149'], 'func': tb_replacement_d3_149}


def tb_replacement_d3_150(tb_replacement_d2_150):
    feature = _clean(tb_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_150'] = {'inputs': ['tb_replacement_d2_150'], 'func': tb_replacement_d3_150}


def tb_replacement_d3_151(tb_replacement_d2_151):
    feature = _clean(tb_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_151'] = {'inputs': ['tb_replacement_d2_151'], 'func': tb_replacement_d3_151}


def tb_replacement_d3_152(tb_replacement_d2_152):
    feature = _clean(tb_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_152'] = {'inputs': ['tb_replacement_d2_152'], 'func': tb_replacement_d3_152}


def tb_replacement_d3_153(tb_replacement_d2_153):
    feature = _clean(tb_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_153'] = {'inputs': ['tb_replacement_d2_153'], 'func': tb_replacement_d3_153}


def tb_replacement_d3_154(tb_replacement_d2_154):
    feature = _clean(tb_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_154'] = {'inputs': ['tb_replacement_d2_154'], 'func': tb_replacement_d3_154}


def tb_replacement_d3_155(tb_replacement_d2_155):
    feature = _clean(tb_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_155'] = {'inputs': ['tb_replacement_d2_155'], 'func': tb_replacement_d3_155}


def tb_replacement_d3_156(tb_replacement_d2_156):
    feature = _clean(tb_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_156'] = {'inputs': ['tb_replacement_d2_156'], 'func': tb_replacement_d3_156}


def tb_replacement_d3_157(tb_replacement_d2_157):
    feature = _clean(tb_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_157'] = {'inputs': ['tb_replacement_d2_157'], 'func': tb_replacement_d3_157}


def tb_replacement_d3_158(tb_replacement_d2_158):
    feature = _clean(tb_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_158'] = {'inputs': ['tb_replacement_d2_158'], 'func': tb_replacement_d3_158}


def tb_replacement_d3_159(tb_replacement_d2_159):
    feature = _clean(tb_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_159'] = {'inputs': ['tb_replacement_d2_159'], 'func': tb_replacement_d3_159}


def tb_replacement_d3_160(tb_replacement_d2_160):
    feature = _clean(tb_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_160'] = {'inputs': ['tb_replacement_d2_160'], 'func': tb_replacement_d3_160}


def tb_replacement_d3_161(tb_replacement_d2_161):
    feature = _clean(tb_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_161'] = {'inputs': ['tb_replacement_d2_161'], 'func': tb_replacement_d3_161}


def tb_replacement_d3_162(tb_replacement_d2_162):
    feature = _clean(tb_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_162'] = {'inputs': ['tb_replacement_d2_162'], 'func': tb_replacement_d3_162}


def tb_replacement_d3_163(tb_replacement_d2_163):
    feature = _clean(tb_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_163'] = {'inputs': ['tb_replacement_d2_163'], 'func': tb_replacement_d3_163}


def tb_replacement_d3_164(tb_replacement_d2_164):
    feature = _clean(tb_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_164'] = {'inputs': ['tb_replacement_d2_164'], 'func': tb_replacement_d3_164}


def tb_replacement_d3_165(tb_replacement_d2_165):
    feature = _clean(tb_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_165'] = {'inputs': ['tb_replacement_d2_165'], 'func': tb_replacement_d3_165}


def tb_replacement_d3_166(tb_replacement_d2_166):
    feature = _clean(tb_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_166'] = {'inputs': ['tb_replacement_d2_166'], 'func': tb_replacement_d3_166}


def tb_replacement_d3_167(tb_replacement_d2_167):
    feature = _clean(tb_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_167'] = {'inputs': ['tb_replacement_d2_167'], 'func': tb_replacement_d3_167}


def tb_replacement_d3_168(tb_replacement_d2_168):
    feature = _clean(tb_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_168'] = {'inputs': ['tb_replacement_d2_168'], 'func': tb_replacement_d3_168}


def tb_replacement_d3_169(tb_replacement_d2_169):
    feature = _clean(tb_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_169'] = {'inputs': ['tb_replacement_d2_169'], 'func': tb_replacement_d3_169}


def tb_replacement_d3_170(tb_replacement_d2_170):
    feature = _clean(tb_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_170'] = {'inputs': ['tb_replacement_d2_170'], 'func': tb_replacement_d3_170}


def tb_replacement_d3_171(tb_replacement_d2_171):
    feature = _clean(tb_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_171'] = {'inputs': ['tb_replacement_d2_171'], 'func': tb_replacement_d3_171}


def tb_replacement_d3_172(tb_replacement_d2_172):
    feature = _clean(tb_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_172'] = {'inputs': ['tb_replacement_d2_172'], 'func': tb_replacement_d3_172}


def tb_replacement_d3_173(tb_replacement_d2_173):
    feature = _clean(tb_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_173'] = {'inputs': ['tb_replacement_d2_173'], 'func': tb_replacement_d3_173}


def tb_replacement_d3_174(tb_replacement_d2_174):
    feature = _clean(tb_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_174'] = {'inputs': ['tb_replacement_d2_174'], 'func': tb_replacement_d3_174}


def tb_replacement_d3_175(tb_replacement_d2_175):
    feature = _clean(tb_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
TB_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['tb_replacement_d3_175'] = {'inputs': ['tb_replacement_d2_175'], 'func': tb_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def tbd_base_universe_d3_001_tbd_003_loss_streak_21_003(tbd_base_universe_d2_001_tbd_003_loss_streak_21_003):
    return _base_universe_d3(tbd_base_universe_d2_001_tbd_003_loss_streak_21_003, 1)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_001_tbd_003_loss_streak_21_003'] = {'inputs': ['tbd_base_universe_d2_001_tbd_003_loss_streak_21_003'], 'func': tbd_base_universe_d3_001_tbd_003_loss_streak_21_003}


def tbd_base_universe_d3_002_tbd_004_ma_distance_42_004(tbd_base_universe_d2_002_tbd_004_ma_distance_42_004):
    return _base_universe_d3(tbd_base_universe_d2_002_tbd_004_ma_distance_42_004, 2)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_002_tbd_004_ma_distance_42_004'] = {'inputs': ['tbd_base_universe_d2_002_tbd_004_ma_distance_42_004'], 'func': tbd_base_universe_d3_002_tbd_004_ma_distance_42_004}


def tbd_base_universe_d3_003_tbd_005_stochastic_position_63_005(tbd_base_universe_d2_003_tbd_005_stochastic_position_63_005):
    return _base_universe_d3(tbd_base_universe_d2_003_tbd_005_stochastic_position_63_005, 3)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_003_tbd_005_stochastic_position_63_005'] = {'inputs': ['tbd_base_universe_d2_003_tbd_005_stochastic_position_63_005'], 'func': tbd_base_universe_d3_003_tbd_005_stochastic_position_63_005}


def tbd_base_universe_d3_004_tbd_009_loss_streak_252_009(tbd_base_universe_d2_004_tbd_009_loss_streak_252_009):
    return _base_universe_d3(tbd_base_universe_d2_004_tbd_009_loss_streak_252_009, 4)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_004_tbd_009_loss_streak_252_009'] = {'inputs': ['tbd_base_universe_d2_004_tbd_009_loss_streak_252_009'], 'func': tbd_base_universe_d3_004_tbd_009_loss_streak_252_009}


def tbd_base_universe_d3_005_tbd_010_ma_distance_378_010(tbd_base_universe_d2_005_tbd_010_ma_distance_378_010):
    return _base_universe_d3(tbd_base_universe_d2_005_tbd_010_ma_distance_378_010, 5)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_005_tbd_010_ma_distance_378_010'] = {'inputs': ['tbd_base_universe_d2_005_tbd_010_ma_distance_378_010'], 'func': tbd_base_universe_d3_005_tbd_010_ma_distance_378_010}


def tbd_base_universe_d3_006_tbd_011_stochastic_position_504_011(tbd_base_universe_d2_006_tbd_011_stochastic_position_504_011):
    return _base_universe_d3(tbd_base_universe_d2_006_tbd_011_stochastic_position_504_011, 6)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_006_tbd_011_stochastic_position_504_011'] = {'inputs': ['tbd_base_universe_d2_006_tbd_011_stochastic_position_504_011'], 'func': tbd_base_universe_d3_006_tbd_011_stochastic_position_504_011}


def tbd_base_universe_d3_007_tbd_015_loss_streak_1512_015(tbd_base_universe_d2_007_tbd_015_loss_streak_1512_015):
    return _base_universe_d3(tbd_base_universe_d2_007_tbd_015_loss_streak_1512_015, 7)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_007_tbd_015_loss_streak_1512_015'] = {'inputs': ['tbd_base_universe_d2_007_tbd_015_loss_streak_1512_015'], 'func': tbd_base_universe_d3_007_tbd_015_loss_streak_1512_015}


def tbd_base_universe_d3_008_tbd_016_ma_distance_5_016(tbd_base_universe_d2_008_tbd_016_ma_distance_5_016):
    return _base_universe_d3(tbd_base_universe_d2_008_tbd_016_ma_distance_5_016, 8)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_008_tbd_016_ma_distance_5_016'] = {'inputs': ['tbd_base_universe_d2_008_tbd_016_ma_distance_5_016'], 'func': tbd_base_universe_d3_008_tbd_016_ma_distance_5_016}


def tbd_base_universe_d3_009_tbd_017_stochastic_position_10_017(tbd_base_universe_d2_009_tbd_017_stochastic_position_10_017):
    return _base_universe_d3(tbd_base_universe_d2_009_tbd_017_stochastic_position_10_017, 9)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_009_tbd_017_stochastic_position_10_017'] = {'inputs': ['tbd_base_universe_d2_009_tbd_017_stochastic_position_10_017'], 'func': tbd_base_universe_d3_009_tbd_017_stochastic_position_10_017}


def tbd_base_universe_d3_010_tbd_021_loss_streak_84_021(tbd_base_universe_d2_010_tbd_021_loss_streak_84_021):
    return _base_universe_d3(tbd_base_universe_d2_010_tbd_021_loss_streak_84_021, 10)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_010_tbd_021_loss_streak_84_021'] = {'inputs': ['tbd_base_universe_d2_010_tbd_021_loss_streak_84_021'], 'func': tbd_base_universe_d3_010_tbd_021_loss_streak_84_021}


def tbd_base_universe_d3_011_tbd_022_ma_distance_126_022(tbd_base_universe_d2_011_tbd_022_ma_distance_126_022):
    return _base_universe_d3(tbd_base_universe_d2_011_tbd_022_ma_distance_126_022, 11)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_011_tbd_022_ma_distance_126_022'] = {'inputs': ['tbd_base_universe_d2_011_tbd_022_ma_distance_126_022'], 'func': tbd_base_universe_d3_011_tbd_022_ma_distance_126_022}


def tbd_base_universe_d3_012_tbd_023_stochastic_position_189_023(tbd_base_universe_d2_012_tbd_023_stochastic_position_189_023):
    return _base_universe_d3(tbd_base_universe_d2_012_tbd_023_stochastic_position_189_023, 12)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_012_tbd_023_stochastic_position_189_023'] = {'inputs': ['tbd_base_universe_d2_012_tbd_023_stochastic_position_189_023'], 'func': tbd_base_universe_d3_012_tbd_023_stochastic_position_189_023}


def tbd_base_universe_d3_013_tbd_027_loss_streak_756_027(tbd_base_universe_d2_013_tbd_027_loss_streak_756_027):
    return _base_universe_d3(tbd_base_universe_d2_013_tbd_027_loss_streak_756_027, 13)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_013_tbd_027_loss_streak_756_027'] = {'inputs': ['tbd_base_universe_d2_013_tbd_027_loss_streak_756_027'], 'func': tbd_base_universe_d3_013_tbd_027_loss_streak_756_027}


def tbd_base_universe_d3_014_tbd_028_ma_distance_1008_028(tbd_base_universe_d2_014_tbd_028_ma_distance_1008_028):
    return _base_universe_d3(tbd_base_universe_d2_014_tbd_028_ma_distance_1008_028, 14)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_014_tbd_028_ma_distance_1008_028'] = {'inputs': ['tbd_base_universe_d2_014_tbd_028_ma_distance_1008_028'], 'func': tbd_base_universe_d3_014_tbd_028_ma_distance_1008_028}


def tbd_base_universe_d3_015_tbd_029_stochastic_position_1260_029(tbd_base_universe_d2_015_tbd_029_stochastic_position_1260_029):
    return _base_universe_d3(tbd_base_universe_d2_015_tbd_029_stochastic_position_1260_029, 15)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_015_tbd_029_stochastic_position_1260_029'] = {'inputs': ['tbd_base_universe_d2_015_tbd_029_stochastic_position_1260_029'], 'func': tbd_base_universe_d3_015_tbd_029_stochastic_position_1260_029}


def tbd_base_universe_d3_016_tbd_basefill_001(tbd_base_universe_d2_016_tbd_basefill_001):
    return _base_universe_d3(tbd_base_universe_d2_016_tbd_basefill_001, 16)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_016_tbd_basefill_001'] = {'inputs': ['tbd_base_universe_d2_016_tbd_basefill_001'], 'func': tbd_base_universe_d3_016_tbd_basefill_001}


def tbd_base_universe_d3_017_tbd_basefill_002(tbd_base_universe_d2_017_tbd_basefill_002):
    return _base_universe_d3(tbd_base_universe_d2_017_tbd_basefill_002, 17)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_017_tbd_basefill_002'] = {'inputs': ['tbd_base_universe_d2_017_tbd_basefill_002'], 'func': tbd_base_universe_d3_017_tbd_basefill_002}


def tbd_base_universe_d3_018_tbd_basefill_006(tbd_base_universe_d2_018_tbd_basefill_006):
    return _base_universe_d3(tbd_base_universe_d2_018_tbd_basefill_006, 18)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_018_tbd_basefill_006'] = {'inputs': ['tbd_base_universe_d2_018_tbd_basefill_006'], 'func': tbd_base_universe_d3_018_tbd_basefill_006}


def tbd_base_universe_d3_019_tbd_basefill_007(tbd_base_universe_d2_019_tbd_basefill_007):
    return _base_universe_d3(tbd_base_universe_d2_019_tbd_basefill_007, 19)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_019_tbd_basefill_007'] = {'inputs': ['tbd_base_universe_d2_019_tbd_basefill_007'], 'func': tbd_base_universe_d3_019_tbd_basefill_007}


def tbd_base_universe_d3_020_tbd_basefill_008(tbd_base_universe_d2_020_tbd_basefill_008):
    return _base_universe_d3(tbd_base_universe_d2_020_tbd_basefill_008, 20)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_020_tbd_basefill_008'] = {'inputs': ['tbd_base_universe_d2_020_tbd_basefill_008'], 'func': tbd_base_universe_d3_020_tbd_basefill_008}


def tbd_base_universe_d3_021_tbd_basefill_012(tbd_base_universe_d2_021_tbd_basefill_012):
    return _base_universe_d3(tbd_base_universe_d2_021_tbd_basefill_012, 21)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_021_tbd_basefill_012'] = {'inputs': ['tbd_base_universe_d2_021_tbd_basefill_012'], 'func': tbd_base_universe_d3_021_tbd_basefill_012}


def tbd_base_universe_d3_022_tbd_basefill_013(tbd_base_universe_d2_022_tbd_basefill_013):
    return _base_universe_d3(tbd_base_universe_d2_022_tbd_basefill_013, 22)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_022_tbd_basefill_013'] = {'inputs': ['tbd_base_universe_d2_022_tbd_basefill_013'], 'func': tbd_base_universe_d3_022_tbd_basefill_013}


def tbd_base_universe_d3_023_tbd_basefill_014(tbd_base_universe_d2_023_tbd_basefill_014):
    return _base_universe_d3(tbd_base_universe_d2_023_tbd_basefill_014, 23)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_023_tbd_basefill_014'] = {'inputs': ['tbd_base_universe_d2_023_tbd_basefill_014'], 'func': tbd_base_universe_d3_023_tbd_basefill_014}


def tbd_base_universe_d3_024_tbd_basefill_018(tbd_base_universe_d2_024_tbd_basefill_018):
    return _base_universe_d3(tbd_base_universe_d2_024_tbd_basefill_018, 24)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_024_tbd_basefill_018'] = {'inputs': ['tbd_base_universe_d2_024_tbd_basefill_018'], 'func': tbd_base_universe_d3_024_tbd_basefill_018}


def tbd_base_universe_d3_025_tbd_basefill_019(tbd_base_universe_d2_025_tbd_basefill_019):
    return _base_universe_d3(tbd_base_universe_d2_025_tbd_basefill_019, 25)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_025_tbd_basefill_019'] = {'inputs': ['tbd_base_universe_d2_025_tbd_basefill_019'], 'func': tbd_base_universe_d3_025_tbd_basefill_019}


def tbd_base_universe_d3_026_tbd_basefill_020(tbd_base_universe_d2_026_tbd_basefill_020):
    return _base_universe_d3(tbd_base_universe_d2_026_tbd_basefill_020, 26)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_026_tbd_basefill_020'] = {'inputs': ['tbd_base_universe_d2_026_tbd_basefill_020'], 'func': tbd_base_universe_d3_026_tbd_basefill_020}


def tbd_base_universe_d3_027_tbd_basefill_024(tbd_base_universe_d2_027_tbd_basefill_024):
    return _base_universe_d3(tbd_base_universe_d2_027_tbd_basefill_024, 27)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_027_tbd_basefill_024'] = {'inputs': ['tbd_base_universe_d2_027_tbd_basefill_024'], 'func': tbd_base_universe_d3_027_tbd_basefill_024}


def tbd_base_universe_d3_028_tbd_basefill_025(tbd_base_universe_d2_028_tbd_basefill_025):
    return _base_universe_d3(tbd_base_universe_d2_028_tbd_basefill_025, 28)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_028_tbd_basefill_025'] = {'inputs': ['tbd_base_universe_d2_028_tbd_basefill_025'], 'func': tbd_base_universe_d3_028_tbd_basefill_025}


def tbd_base_universe_d3_029_tbd_basefill_026(tbd_base_universe_d2_029_tbd_basefill_026):
    return _base_universe_d3(tbd_base_universe_d2_029_tbd_basefill_026, 29)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_029_tbd_basefill_026'] = {'inputs': ['tbd_base_universe_d2_029_tbd_basefill_026'], 'func': tbd_base_universe_d3_029_tbd_basefill_026}


def tbd_base_universe_d3_030_tbd_basefill_030(tbd_base_universe_d2_030_tbd_basefill_030):
    return _base_universe_d3(tbd_base_universe_d2_030_tbd_basefill_030, 30)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_030_tbd_basefill_030'] = {'inputs': ['tbd_base_universe_d2_030_tbd_basefill_030'], 'func': tbd_base_universe_d3_030_tbd_basefill_030}


def tbd_base_universe_d3_031_tbd_basefill_031(tbd_base_universe_d2_031_tbd_basefill_031):
    return _base_universe_d3(tbd_base_universe_d2_031_tbd_basefill_031, 31)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_031_tbd_basefill_031'] = {'inputs': ['tbd_base_universe_d2_031_tbd_basefill_031'], 'func': tbd_base_universe_d3_031_tbd_basefill_031}


def tbd_base_universe_d3_032_tbd_basefill_032(tbd_base_universe_d2_032_tbd_basefill_032):
    return _base_universe_d3(tbd_base_universe_d2_032_tbd_basefill_032, 32)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_032_tbd_basefill_032'] = {'inputs': ['tbd_base_universe_d2_032_tbd_basefill_032'], 'func': tbd_base_universe_d3_032_tbd_basefill_032}


def tbd_base_universe_d3_033_tbd_basefill_033(tbd_base_universe_d2_033_tbd_basefill_033):
    return _base_universe_d3(tbd_base_universe_d2_033_tbd_basefill_033, 33)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_033_tbd_basefill_033'] = {'inputs': ['tbd_base_universe_d2_033_tbd_basefill_033'], 'func': tbd_base_universe_d3_033_tbd_basefill_033}


def tbd_base_universe_d3_034_tbd_basefill_034(tbd_base_universe_d2_034_tbd_basefill_034):
    return _base_universe_d3(tbd_base_universe_d2_034_tbd_basefill_034, 34)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_034_tbd_basefill_034'] = {'inputs': ['tbd_base_universe_d2_034_tbd_basefill_034'], 'func': tbd_base_universe_d3_034_tbd_basefill_034}


def tbd_base_universe_d3_035_tbd_basefill_035(tbd_base_universe_d2_035_tbd_basefill_035):
    return _base_universe_d3(tbd_base_universe_d2_035_tbd_basefill_035, 35)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_035_tbd_basefill_035'] = {'inputs': ['tbd_base_universe_d2_035_tbd_basefill_035'], 'func': tbd_base_universe_d3_035_tbd_basefill_035}


def tbd_base_universe_d3_036_tbd_basefill_036(tbd_base_universe_d2_036_tbd_basefill_036):
    return _base_universe_d3(tbd_base_universe_d2_036_tbd_basefill_036, 36)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_036_tbd_basefill_036'] = {'inputs': ['tbd_base_universe_d2_036_tbd_basefill_036'], 'func': tbd_base_universe_d3_036_tbd_basefill_036}


def tbd_base_universe_d3_037_tbd_basefill_037(tbd_base_universe_d2_037_tbd_basefill_037):
    return _base_universe_d3(tbd_base_universe_d2_037_tbd_basefill_037, 37)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_037_tbd_basefill_037'] = {'inputs': ['tbd_base_universe_d2_037_tbd_basefill_037'], 'func': tbd_base_universe_d3_037_tbd_basefill_037}


def tbd_base_universe_d3_038_tbd_basefill_038(tbd_base_universe_d2_038_tbd_basefill_038):
    return _base_universe_d3(tbd_base_universe_d2_038_tbd_basefill_038, 38)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_038_tbd_basefill_038'] = {'inputs': ['tbd_base_universe_d2_038_tbd_basefill_038'], 'func': tbd_base_universe_d3_038_tbd_basefill_038}


def tbd_base_universe_d3_039_tbd_basefill_039(tbd_base_universe_d2_039_tbd_basefill_039):
    return _base_universe_d3(tbd_base_universe_d2_039_tbd_basefill_039, 39)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_039_tbd_basefill_039'] = {'inputs': ['tbd_base_universe_d2_039_tbd_basefill_039'], 'func': tbd_base_universe_d3_039_tbd_basefill_039}


def tbd_base_universe_d3_040_tbd_basefill_040(tbd_base_universe_d2_040_tbd_basefill_040):
    return _base_universe_d3(tbd_base_universe_d2_040_tbd_basefill_040, 40)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_040_tbd_basefill_040'] = {'inputs': ['tbd_base_universe_d2_040_tbd_basefill_040'], 'func': tbd_base_universe_d3_040_tbd_basefill_040}


def tbd_base_universe_d3_041_tbd_basefill_041(tbd_base_universe_d2_041_tbd_basefill_041):
    return _base_universe_d3(tbd_base_universe_d2_041_tbd_basefill_041, 41)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_041_tbd_basefill_041'] = {'inputs': ['tbd_base_universe_d2_041_tbd_basefill_041'], 'func': tbd_base_universe_d3_041_tbd_basefill_041}


def tbd_base_universe_d3_042_tbd_basefill_042(tbd_base_universe_d2_042_tbd_basefill_042):
    return _base_universe_d3(tbd_base_universe_d2_042_tbd_basefill_042, 42)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_042_tbd_basefill_042'] = {'inputs': ['tbd_base_universe_d2_042_tbd_basefill_042'], 'func': tbd_base_universe_d3_042_tbd_basefill_042}


def tbd_base_universe_d3_043_tbd_basefill_043(tbd_base_universe_d2_043_tbd_basefill_043):
    return _base_universe_d3(tbd_base_universe_d2_043_tbd_basefill_043, 43)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_043_tbd_basefill_043'] = {'inputs': ['tbd_base_universe_d2_043_tbd_basefill_043'], 'func': tbd_base_universe_d3_043_tbd_basefill_043}


def tbd_base_universe_d3_044_tbd_basefill_044(tbd_base_universe_d2_044_tbd_basefill_044):
    return _base_universe_d3(tbd_base_universe_d2_044_tbd_basefill_044, 44)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_044_tbd_basefill_044'] = {'inputs': ['tbd_base_universe_d2_044_tbd_basefill_044'], 'func': tbd_base_universe_d3_044_tbd_basefill_044}


def tbd_base_universe_d3_045_tbd_basefill_045(tbd_base_universe_d2_045_tbd_basefill_045):
    return _base_universe_d3(tbd_base_universe_d2_045_tbd_basefill_045, 45)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_045_tbd_basefill_045'] = {'inputs': ['tbd_base_universe_d2_045_tbd_basefill_045'], 'func': tbd_base_universe_d3_045_tbd_basefill_045}


def tbd_base_universe_d3_046_tbd_basefill_046(tbd_base_universe_d2_046_tbd_basefill_046):
    return _base_universe_d3(tbd_base_universe_d2_046_tbd_basefill_046, 46)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_046_tbd_basefill_046'] = {'inputs': ['tbd_base_universe_d2_046_tbd_basefill_046'], 'func': tbd_base_universe_d3_046_tbd_basefill_046}


def tbd_base_universe_d3_047_tbd_basefill_047(tbd_base_universe_d2_047_tbd_basefill_047):
    return _base_universe_d3(tbd_base_universe_d2_047_tbd_basefill_047, 47)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_047_tbd_basefill_047'] = {'inputs': ['tbd_base_universe_d2_047_tbd_basefill_047'], 'func': tbd_base_universe_d3_047_tbd_basefill_047}


def tbd_base_universe_d3_048_tbd_basefill_048(tbd_base_universe_d2_048_tbd_basefill_048):
    return _base_universe_d3(tbd_base_universe_d2_048_tbd_basefill_048, 48)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_048_tbd_basefill_048'] = {'inputs': ['tbd_base_universe_d2_048_tbd_basefill_048'], 'func': tbd_base_universe_d3_048_tbd_basefill_048}


def tbd_base_universe_d3_049_tbd_basefill_049(tbd_base_universe_d2_049_tbd_basefill_049):
    return _base_universe_d3(tbd_base_universe_d2_049_tbd_basefill_049, 49)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_049_tbd_basefill_049'] = {'inputs': ['tbd_base_universe_d2_049_tbd_basefill_049'], 'func': tbd_base_universe_d3_049_tbd_basefill_049}


def tbd_base_universe_d3_050_tbd_basefill_050(tbd_base_universe_d2_050_tbd_basefill_050):
    return _base_universe_d3(tbd_base_universe_d2_050_tbd_basefill_050, 50)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_050_tbd_basefill_050'] = {'inputs': ['tbd_base_universe_d2_050_tbd_basefill_050'], 'func': tbd_base_universe_d3_050_tbd_basefill_050}


def tbd_base_universe_d3_051_tbd_basefill_051(tbd_base_universe_d2_051_tbd_basefill_051):
    return _base_universe_d3(tbd_base_universe_d2_051_tbd_basefill_051, 51)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_051_tbd_basefill_051'] = {'inputs': ['tbd_base_universe_d2_051_tbd_basefill_051'], 'func': tbd_base_universe_d3_051_tbd_basefill_051}


def tbd_base_universe_d3_052_tbd_basefill_052(tbd_base_universe_d2_052_tbd_basefill_052):
    return _base_universe_d3(tbd_base_universe_d2_052_tbd_basefill_052, 52)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_052_tbd_basefill_052'] = {'inputs': ['tbd_base_universe_d2_052_tbd_basefill_052'], 'func': tbd_base_universe_d3_052_tbd_basefill_052}


def tbd_base_universe_d3_053_tbd_basefill_053(tbd_base_universe_d2_053_tbd_basefill_053):
    return _base_universe_d3(tbd_base_universe_d2_053_tbd_basefill_053, 53)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_053_tbd_basefill_053'] = {'inputs': ['tbd_base_universe_d2_053_tbd_basefill_053'], 'func': tbd_base_universe_d3_053_tbd_basefill_053}


def tbd_base_universe_d3_054_tbd_basefill_054(tbd_base_universe_d2_054_tbd_basefill_054):
    return _base_universe_d3(tbd_base_universe_d2_054_tbd_basefill_054, 54)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_054_tbd_basefill_054'] = {'inputs': ['tbd_base_universe_d2_054_tbd_basefill_054'], 'func': tbd_base_universe_d3_054_tbd_basefill_054}


def tbd_base_universe_d3_055_tbd_basefill_055(tbd_base_universe_d2_055_tbd_basefill_055):
    return _base_universe_d3(tbd_base_universe_d2_055_tbd_basefill_055, 55)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_055_tbd_basefill_055'] = {'inputs': ['tbd_base_universe_d2_055_tbd_basefill_055'], 'func': tbd_base_universe_d3_055_tbd_basefill_055}


def tbd_base_universe_d3_056_tbd_basefill_056(tbd_base_universe_d2_056_tbd_basefill_056):
    return _base_universe_d3(tbd_base_universe_d2_056_tbd_basefill_056, 56)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_056_tbd_basefill_056'] = {'inputs': ['tbd_base_universe_d2_056_tbd_basefill_056'], 'func': tbd_base_universe_d3_056_tbd_basefill_056}


def tbd_base_universe_d3_057_tbd_basefill_057(tbd_base_universe_d2_057_tbd_basefill_057):
    return _base_universe_d3(tbd_base_universe_d2_057_tbd_basefill_057, 57)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_057_tbd_basefill_057'] = {'inputs': ['tbd_base_universe_d2_057_tbd_basefill_057'], 'func': tbd_base_universe_d3_057_tbd_basefill_057}


def tbd_base_universe_d3_058_tbd_basefill_058(tbd_base_universe_d2_058_tbd_basefill_058):
    return _base_universe_d3(tbd_base_universe_d2_058_tbd_basefill_058, 58)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_058_tbd_basefill_058'] = {'inputs': ['tbd_base_universe_d2_058_tbd_basefill_058'], 'func': tbd_base_universe_d3_058_tbd_basefill_058}


def tbd_base_universe_d3_059_tbd_basefill_059(tbd_base_universe_d2_059_tbd_basefill_059):
    return _base_universe_d3(tbd_base_universe_d2_059_tbd_basefill_059, 59)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_059_tbd_basefill_059'] = {'inputs': ['tbd_base_universe_d2_059_tbd_basefill_059'], 'func': tbd_base_universe_d3_059_tbd_basefill_059}


def tbd_base_universe_d3_060_tbd_basefill_060(tbd_base_universe_d2_060_tbd_basefill_060):
    return _base_universe_d3(tbd_base_universe_d2_060_tbd_basefill_060, 60)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_060_tbd_basefill_060'] = {'inputs': ['tbd_base_universe_d2_060_tbd_basefill_060'], 'func': tbd_base_universe_d3_060_tbd_basefill_060}


def tbd_base_universe_d3_061_tbd_basefill_061(tbd_base_universe_d2_061_tbd_basefill_061):
    return _base_universe_d3(tbd_base_universe_d2_061_tbd_basefill_061, 61)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_061_tbd_basefill_061'] = {'inputs': ['tbd_base_universe_d2_061_tbd_basefill_061'], 'func': tbd_base_universe_d3_061_tbd_basefill_061}


def tbd_base_universe_d3_062_tbd_basefill_062(tbd_base_universe_d2_062_tbd_basefill_062):
    return _base_universe_d3(tbd_base_universe_d2_062_tbd_basefill_062, 62)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_062_tbd_basefill_062'] = {'inputs': ['tbd_base_universe_d2_062_tbd_basefill_062'], 'func': tbd_base_universe_d3_062_tbd_basefill_062}


def tbd_base_universe_d3_063_tbd_basefill_063(tbd_base_universe_d2_063_tbd_basefill_063):
    return _base_universe_d3(tbd_base_universe_d2_063_tbd_basefill_063, 63)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_063_tbd_basefill_063'] = {'inputs': ['tbd_base_universe_d2_063_tbd_basefill_063'], 'func': tbd_base_universe_d3_063_tbd_basefill_063}


def tbd_base_universe_d3_064_tbd_basefill_064(tbd_base_universe_d2_064_tbd_basefill_064):
    return _base_universe_d3(tbd_base_universe_d2_064_tbd_basefill_064, 64)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_064_tbd_basefill_064'] = {'inputs': ['tbd_base_universe_d2_064_tbd_basefill_064'], 'func': tbd_base_universe_d3_064_tbd_basefill_064}


def tbd_base_universe_d3_065_tbd_basefill_065(tbd_base_universe_d2_065_tbd_basefill_065):
    return _base_universe_d3(tbd_base_universe_d2_065_tbd_basefill_065, 65)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_065_tbd_basefill_065'] = {'inputs': ['tbd_base_universe_d2_065_tbd_basefill_065'], 'func': tbd_base_universe_d3_065_tbd_basefill_065}


def tbd_base_universe_d3_066_tbd_basefill_066(tbd_base_universe_d2_066_tbd_basefill_066):
    return _base_universe_d3(tbd_base_universe_d2_066_tbd_basefill_066, 66)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_066_tbd_basefill_066'] = {'inputs': ['tbd_base_universe_d2_066_tbd_basefill_066'], 'func': tbd_base_universe_d3_066_tbd_basefill_066}


def tbd_base_universe_d3_067_tbd_basefill_067(tbd_base_universe_d2_067_tbd_basefill_067):
    return _base_universe_d3(tbd_base_universe_d2_067_tbd_basefill_067, 67)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_067_tbd_basefill_067'] = {'inputs': ['tbd_base_universe_d2_067_tbd_basefill_067'], 'func': tbd_base_universe_d3_067_tbd_basefill_067}


def tbd_base_universe_d3_068_tbd_basefill_068(tbd_base_universe_d2_068_tbd_basefill_068):
    return _base_universe_d3(tbd_base_universe_d2_068_tbd_basefill_068, 68)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_068_tbd_basefill_068'] = {'inputs': ['tbd_base_universe_d2_068_tbd_basefill_068'], 'func': tbd_base_universe_d3_068_tbd_basefill_068}


def tbd_base_universe_d3_069_tbd_basefill_069(tbd_base_universe_d2_069_tbd_basefill_069):
    return _base_universe_d3(tbd_base_universe_d2_069_tbd_basefill_069, 69)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_069_tbd_basefill_069'] = {'inputs': ['tbd_base_universe_d2_069_tbd_basefill_069'], 'func': tbd_base_universe_d3_069_tbd_basefill_069}


def tbd_base_universe_d3_070_tbd_basefill_070(tbd_base_universe_d2_070_tbd_basefill_070):
    return _base_universe_d3(tbd_base_universe_d2_070_tbd_basefill_070, 70)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_070_tbd_basefill_070'] = {'inputs': ['tbd_base_universe_d2_070_tbd_basefill_070'], 'func': tbd_base_universe_d3_070_tbd_basefill_070}


def tbd_base_universe_d3_071_tbd_basefill_071(tbd_base_universe_d2_071_tbd_basefill_071):
    return _base_universe_d3(tbd_base_universe_d2_071_tbd_basefill_071, 71)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_071_tbd_basefill_071'] = {'inputs': ['tbd_base_universe_d2_071_tbd_basefill_071'], 'func': tbd_base_universe_d3_071_tbd_basefill_071}


def tbd_base_universe_d3_072_tbd_basefill_072(tbd_base_universe_d2_072_tbd_basefill_072):
    return _base_universe_d3(tbd_base_universe_d2_072_tbd_basefill_072, 72)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_072_tbd_basefill_072'] = {'inputs': ['tbd_base_universe_d2_072_tbd_basefill_072'], 'func': tbd_base_universe_d3_072_tbd_basefill_072}


def tbd_base_universe_d3_073_tbd_basefill_073(tbd_base_universe_d2_073_tbd_basefill_073):
    return _base_universe_d3(tbd_base_universe_d2_073_tbd_basefill_073, 73)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_073_tbd_basefill_073'] = {'inputs': ['tbd_base_universe_d2_073_tbd_basefill_073'], 'func': tbd_base_universe_d3_073_tbd_basefill_073}


def tbd_base_universe_d3_074_tbd_basefill_074(tbd_base_universe_d2_074_tbd_basefill_074):
    return _base_universe_d3(tbd_base_universe_d2_074_tbd_basefill_074, 74)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_074_tbd_basefill_074'] = {'inputs': ['tbd_base_universe_d2_074_tbd_basefill_074'], 'func': tbd_base_universe_d3_074_tbd_basefill_074}


def tbd_base_universe_d3_075_tbd_basefill_075(tbd_base_universe_d2_075_tbd_basefill_075):
    return _base_universe_d3(tbd_base_universe_d2_075_tbd_basefill_075, 75)
TBD_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['tbd_base_universe_d3_075_tbd_basefill_075'] = {'inputs': ['tbd_base_universe_d2_075_tbd_basefill_075'], 'func': tbd_base_universe_d3_075_tbd_basefill_075}
