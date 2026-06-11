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



def rfl_176_rfl_001_drawdown_from_high_5_001_accel_1(rfl_151_rfl_001_drawdown_from_high_5_001_roc_1):
    feature = _s(rfl_151_rfl_001_drawdown_from_high_5_001_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def rfl_177_rfl_007_drawdown_from_high_126_007_accel_5(rfl_152_rfl_007_drawdown_from_high_126_007_roc_5):
    feature = _s(rfl_152_rfl_007_drawdown_from_high_126_007_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def rfl_178_rfl_013_drawdown_from_high_1008_013_accel_42(rfl_153_rfl_013_drawdown_from_high_1008_013_roc_42):
    feature = _s(rfl_153_rfl_013_drawdown_from_high_1008_013_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def rfl_179_rfl_019_drawdown_from_high_42_019_accel_126(rfl_154_rfl_019_drawdown_from_high_42_019_roc_126):
    feature = _s(rfl_154_rfl_019_drawdown_from_high_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def rfl_180_rfl_025_drawdown_from_high_378_025_accel_378(rfl_155_rfl_025_drawdown_from_high_378_025_roc_378):
    feature = _s(rfl_155_rfl_025_drawdown_from_high_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















RECOVERY_FAILURE_REGISTRY_3RD_DERIVATIVES = {
    'rfl_176_rfl_001_drawdown_from_high_5_001_accel_1': {'inputs': ['rfl_151_rfl_001_drawdown_from_high_5_001_roc_1'], 'func': rfl_176_rfl_001_drawdown_from_high_5_001_accel_1},
    'rfl_177_rfl_007_drawdown_from_high_126_007_accel_5': {'inputs': ['rfl_152_rfl_007_drawdown_from_high_126_007_roc_5'], 'func': rfl_177_rfl_007_drawdown_from_high_126_007_accel_5},
    'rfl_178_rfl_013_drawdown_from_high_1008_013_accel_42': {'inputs': ['rfl_153_rfl_013_drawdown_from_high_1008_013_roc_42'], 'func': rfl_178_rfl_013_drawdown_from_high_1008_013_accel_42},
    'rfl_179_rfl_019_drawdown_from_high_42_019_accel_126': {'inputs': ['rfl_154_rfl_019_drawdown_from_high_42_019_roc_126'], 'func': rfl_179_rfl_019_drawdown_from_high_42_019_accel_126},
    'rfl_180_rfl_025_drawdown_from_high_378_025_accel_378': {'inputs': ['rfl_155_rfl_025_drawdown_from_high_378_025_roc_378'], 'func': rfl_180_rfl_025_drawdown_from_high_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def rf_replacement_d3_001(rf_replacement_d2_001):
    feature = _clean(rf_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_001'] = {'inputs': ['rf_replacement_d2_001'], 'func': rf_replacement_d3_001}


def rf_replacement_d3_002(rf_replacement_d2_002):
    feature = _clean(rf_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_002'] = {'inputs': ['rf_replacement_d2_002'], 'func': rf_replacement_d3_002}


def rf_replacement_d3_003(rf_replacement_d2_003):
    feature = _clean(rf_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_003'] = {'inputs': ['rf_replacement_d2_003'], 'func': rf_replacement_d3_003}


def rf_replacement_d3_004(rf_replacement_d2_004):
    feature = _clean(rf_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_004'] = {'inputs': ['rf_replacement_d2_004'], 'func': rf_replacement_d3_004}


def rf_replacement_d3_005(rf_replacement_d2_005):
    feature = _clean(rf_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_005'] = {'inputs': ['rf_replacement_d2_005'], 'func': rf_replacement_d3_005}


def rf_replacement_d3_006(rf_replacement_d2_006):
    feature = _clean(rf_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_006'] = {'inputs': ['rf_replacement_d2_006'], 'func': rf_replacement_d3_006}


def rf_replacement_d3_007(rf_replacement_d2_007):
    feature = _clean(rf_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_007'] = {'inputs': ['rf_replacement_d2_007'], 'func': rf_replacement_d3_007}


def rf_replacement_d3_008(rf_replacement_d2_008):
    feature = _clean(rf_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_008'] = {'inputs': ['rf_replacement_d2_008'], 'func': rf_replacement_d3_008}


def rf_replacement_d3_009(rf_replacement_d2_009):
    feature = _clean(rf_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_009'] = {'inputs': ['rf_replacement_d2_009'], 'func': rf_replacement_d3_009}


def rf_replacement_d3_010(rf_replacement_d2_010):
    feature = _clean(rf_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_010'] = {'inputs': ['rf_replacement_d2_010'], 'func': rf_replacement_d3_010}


def rf_replacement_d3_011(rf_replacement_d2_011):
    feature = _clean(rf_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_011'] = {'inputs': ['rf_replacement_d2_011'], 'func': rf_replacement_d3_011}


def rf_replacement_d3_012(rf_replacement_d2_012):
    feature = _clean(rf_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_012'] = {'inputs': ['rf_replacement_d2_012'], 'func': rf_replacement_d3_012}


def rf_replacement_d3_013(rf_replacement_d2_013):
    feature = _clean(rf_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_013'] = {'inputs': ['rf_replacement_d2_013'], 'func': rf_replacement_d3_013}


def rf_replacement_d3_014(rf_replacement_d2_014):
    feature = _clean(rf_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_014'] = {'inputs': ['rf_replacement_d2_014'], 'func': rf_replacement_d3_014}


def rf_replacement_d3_015(rf_replacement_d2_015):
    feature = _clean(rf_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_015'] = {'inputs': ['rf_replacement_d2_015'], 'func': rf_replacement_d3_015}


def rf_replacement_d3_016(rf_replacement_d2_016):
    feature = _clean(rf_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_016'] = {'inputs': ['rf_replacement_d2_016'], 'func': rf_replacement_d3_016}


def rf_replacement_d3_017(rf_replacement_d2_017):
    feature = _clean(rf_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_017'] = {'inputs': ['rf_replacement_d2_017'], 'func': rf_replacement_d3_017}


def rf_replacement_d3_018(rf_replacement_d2_018):
    feature = _clean(rf_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_018'] = {'inputs': ['rf_replacement_d2_018'], 'func': rf_replacement_d3_018}


def rf_replacement_d3_019(rf_replacement_d2_019):
    feature = _clean(rf_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_019'] = {'inputs': ['rf_replacement_d2_019'], 'func': rf_replacement_d3_019}


def rf_replacement_d3_020(rf_replacement_d2_020):
    feature = _clean(rf_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_020'] = {'inputs': ['rf_replacement_d2_020'], 'func': rf_replacement_d3_020}


def rf_replacement_d3_021(rf_replacement_d2_021):
    feature = _clean(rf_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_021'] = {'inputs': ['rf_replacement_d2_021'], 'func': rf_replacement_d3_021}


def rf_replacement_d3_022(rf_replacement_d2_022):
    feature = _clean(rf_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_022'] = {'inputs': ['rf_replacement_d2_022'], 'func': rf_replacement_d3_022}


def rf_replacement_d3_023(rf_replacement_d2_023):
    feature = _clean(rf_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_023'] = {'inputs': ['rf_replacement_d2_023'], 'func': rf_replacement_d3_023}


def rf_replacement_d3_024(rf_replacement_d2_024):
    feature = _clean(rf_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_024'] = {'inputs': ['rf_replacement_d2_024'], 'func': rf_replacement_d3_024}


def rf_replacement_d3_025(rf_replacement_d2_025):
    feature = _clean(rf_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_025'] = {'inputs': ['rf_replacement_d2_025'], 'func': rf_replacement_d3_025}


def rf_replacement_d3_026(rf_replacement_d2_026):
    feature = _clean(rf_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_026'] = {'inputs': ['rf_replacement_d2_026'], 'func': rf_replacement_d3_026}


def rf_replacement_d3_027(rf_replacement_d2_027):
    feature = _clean(rf_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_027'] = {'inputs': ['rf_replacement_d2_027'], 'func': rf_replacement_d3_027}


def rf_replacement_d3_028(rf_replacement_d2_028):
    feature = _clean(rf_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_028'] = {'inputs': ['rf_replacement_d2_028'], 'func': rf_replacement_d3_028}


def rf_replacement_d3_029(rf_replacement_d2_029):
    feature = _clean(rf_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_029'] = {'inputs': ['rf_replacement_d2_029'], 'func': rf_replacement_d3_029}


def rf_replacement_d3_030(rf_replacement_d2_030):
    feature = _clean(rf_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_030'] = {'inputs': ['rf_replacement_d2_030'], 'func': rf_replacement_d3_030}


def rf_replacement_d3_031(rf_replacement_d2_031):
    feature = _clean(rf_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_031'] = {'inputs': ['rf_replacement_d2_031'], 'func': rf_replacement_d3_031}


def rf_replacement_d3_032(rf_replacement_d2_032):
    feature = _clean(rf_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_032'] = {'inputs': ['rf_replacement_d2_032'], 'func': rf_replacement_d3_032}


def rf_replacement_d3_033(rf_replacement_d2_033):
    feature = _clean(rf_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_033'] = {'inputs': ['rf_replacement_d2_033'], 'func': rf_replacement_d3_033}


def rf_replacement_d3_034(rf_replacement_d2_034):
    feature = _clean(rf_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_034'] = {'inputs': ['rf_replacement_d2_034'], 'func': rf_replacement_d3_034}


def rf_replacement_d3_035(rf_replacement_d2_035):
    feature = _clean(rf_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_035'] = {'inputs': ['rf_replacement_d2_035'], 'func': rf_replacement_d3_035}


def rf_replacement_d3_036(rf_replacement_d2_036):
    feature = _clean(rf_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_036'] = {'inputs': ['rf_replacement_d2_036'], 'func': rf_replacement_d3_036}


def rf_replacement_d3_037(rf_replacement_d2_037):
    feature = _clean(rf_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_037'] = {'inputs': ['rf_replacement_d2_037'], 'func': rf_replacement_d3_037}


def rf_replacement_d3_038(rf_replacement_d2_038):
    feature = _clean(rf_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_038'] = {'inputs': ['rf_replacement_d2_038'], 'func': rf_replacement_d3_038}


def rf_replacement_d3_039(rf_replacement_d2_039):
    feature = _clean(rf_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_039'] = {'inputs': ['rf_replacement_d2_039'], 'func': rf_replacement_d3_039}


def rf_replacement_d3_040(rf_replacement_d2_040):
    feature = _clean(rf_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_040'] = {'inputs': ['rf_replacement_d2_040'], 'func': rf_replacement_d3_040}


def rf_replacement_d3_041(rf_replacement_d2_041):
    feature = _clean(rf_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_041'] = {'inputs': ['rf_replacement_d2_041'], 'func': rf_replacement_d3_041}


def rf_replacement_d3_042(rf_replacement_d2_042):
    feature = _clean(rf_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_042'] = {'inputs': ['rf_replacement_d2_042'], 'func': rf_replacement_d3_042}


def rf_replacement_d3_043(rf_replacement_d2_043):
    feature = _clean(rf_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_043'] = {'inputs': ['rf_replacement_d2_043'], 'func': rf_replacement_d3_043}


def rf_replacement_d3_044(rf_replacement_d2_044):
    feature = _clean(rf_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_044'] = {'inputs': ['rf_replacement_d2_044'], 'func': rf_replacement_d3_044}


def rf_replacement_d3_045(rf_replacement_d2_045):
    feature = _clean(rf_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_045'] = {'inputs': ['rf_replacement_d2_045'], 'func': rf_replacement_d3_045}


def rf_replacement_d3_046(rf_replacement_d2_046):
    feature = _clean(rf_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_046'] = {'inputs': ['rf_replacement_d2_046'], 'func': rf_replacement_d3_046}


def rf_replacement_d3_047(rf_replacement_d2_047):
    feature = _clean(rf_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_047'] = {'inputs': ['rf_replacement_d2_047'], 'func': rf_replacement_d3_047}


def rf_replacement_d3_048(rf_replacement_d2_048):
    feature = _clean(rf_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_048'] = {'inputs': ['rf_replacement_d2_048'], 'func': rf_replacement_d3_048}


def rf_replacement_d3_049(rf_replacement_d2_049):
    feature = _clean(rf_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_049'] = {'inputs': ['rf_replacement_d2_049'], 'func': rf_replacement_d3_049}


def rf_replacement_d3_050(rf_replacement_d2_050):
    feature = _clean(rf_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_050'] = {'inputs': ['rf_replacement_d2_050'], 'func': rf_replacement_d3_050}


def rf_replacement_d3_051(rf_replacement_d2_051):
    feature = _clean(rf_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_051'] = {'inputs': ['rf_replacement_d2_051'], 'func': rf_replacement_d3_051}


def rf_replacement_d3_052(rf_replacement_d2_052):
    feature = _clean(rf_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_052'] = {'inputs': ['rf_replacement_d2_052'], 'func': rf_replacement_d3_052}


def rf_replacement_d3_053(rf_replacement_d2_053):
    feature = _clean(rf_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_053'] = {'inputs': ['rf_replacement_d2_053'], 'func': rf_replacement_d3_053}


def rf_replacement_d3_054(rf_replacement_d2_054):
    feature = _clean(rf_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_054'] = {'inputs': ['rf_replacement_d2_054'], 'func': rf_replacement_d3_054}


def rf_replacement_d3_055(rf_replacement_d2_055):
    feature = _clean(rf_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_055'] = {'inputs': ['rf_replacement_d2_055'], 'func': rf_replacement_d3_055}


def rf_replacement_d3_056(rf_replacement_d2_056):
    feature = _clean(rf_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_056'] = {'inputs': ['rf_replacement_d2_056'], 'func': rf_replacement_d3_056}


def rf_replacement_d3_057(rf_replacement_d2_057):
    feature = _clean(rf_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_057'] = {'inputs': ['rf_replacement_d2_057'], 'func': rf_replacement_d3_057}


def rf_replacement_d3_058(rf_replacement_d2_058):
    feature = _clean(rf_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_058'] = {'inputs': ['rf_replacement_d2_058'], 'func': rf_replacement_d3_058}


def rf_replacement_d3_059(rf_replacement_d2_059):
    feature = _clean(rf_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_059'] = {'inputs': ['rf_replacement_d2_059'], 'func': rf_replacement_d3_059}


def rf_replacement_d3_060(rf_replacement_d2_060):
    feature = _clean(rf_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_060'] = {'inputs': ['rf_replacement_d2_060'], 'func': rf_replacement_d3_060}


def rf_replacement_d3_061(rf_replacement_d2_061):
    feature = _clean(rf_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_061'] = {'inputs': ['rf_replacement_d2_061'], 'func': rf_replacement_d3_061}


def rf_replacement_d3_062(rf_replacement_d2_062):
    feature = _clean(rf_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_062'] = {'inputs': ['rf_replacement_d2_062'], 'func': rf_replacement_d3_062}


def rf_replacement_d3_063(rf_replacement_d2_063):
    feature = _clean(rf_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_063'] = {'inputs': ['rf_replacement_d2_063'], 'func': rf_replacement_d3_063}


def rf_replacement_d3_064(rf_replacement_d2_064):
    feature = _clean(rf_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_064'] = {'inputs': ['rf_replacement_d2_064'], 'func': rf_replacement_d3_064}


def rf_replacement_d3_065(rf_replacement_d2_065):
    feature = _clean(rf_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_065'] = {'inputs': ['rf_replacement_d2_065'], 'func': rf_replacement_d3_065}


def rf_replacement_d3_066(rf_replacement_d2_066):
    feature = _clean(rf_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_066'] = {'inputs': ['rf_replacement_d2_066'], 'func': rf_replacement_d3_066}


def rf_replacement_d3_067(rf_replacement_d2_067):
    feature = _clean(rf_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_067'] = {'inputs': ['rf_replacement_d2_067'], 'func': rf_replacement_d3_067}


def rf_replacement_d3_068(rf_replacement_d2_068):
    feature = _clean(rf_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_068'] = {'inputs': ['rf_replacement_d2_068'], 'func': rf_replacement_d3_068}


def rf_replacement_d3_069(rf_replacement_d2_069):
    feature = _clean(rf_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_069'] = {'inputs': ['rf_replacement_d2_069'], 'func': rf_replacement_d3_069}


def rf_replacement_d3_070(rf_replacement_d2_070):
    feature = _clean(rf_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_070'] = {'inputs': ['rf_replacement_d2_070'], 'func': rf_replacement_d3_070}


def rf_replacement_d3_071(rf_replacement_d2_071):
    feature = _clean(rf_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_071'] = {'inputs': ['rf_replacement_d2_071'], 'func': rf_replacement_d3_071}


def rf_replacement_d3_072(rf_replacement_d2_072):
    feature = _clean(rf_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_072'] = {'inputs': ['rf_replacement_d2_072'], 'func': rf_replacement_d3_072}


def rf_replacement_d3_073(rf_replacement_d2_073):
    feature = _clean(rf_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_073'] = {'inputs': ['rf_replacement_d2_073'], 'func': rf_replacement_d3_073}


def rf_replacement_d3_074(rf_replacement_d2_074):
    feature = _clean(rf_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_074'] = {'inputs': ['rf_replacement_d2_074'], 'func': rf_replacement_d3_074}


def rf_replacement_d3_075(rf_replacement_d2_075):
    feature = _clean(rf_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_075'] = {'inputs': ['rf_replacement_d2_075'], 'func': rf_replacement_d3_075}


def rf_replacement_d3_076(rf_replacement_d2_076):
    feature = _clean(rf_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_076'] = {'inputs': ['rf_replacement_d2_076'], 'func': rf_replacement_d3_076}


def rf_replacement_d3_077(rf_replacement_d2_077):
    feature = _clean(rf_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_077'] = {'inputs': ['rf_replacement_d2_077'], 'func': rf_replacement_d3_077}


def rf_replacement_d3_078(rf_replacement_d2_078):
    feature = _clean(rf_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_078'] = {'inputs': ['rf_replacement_d2_078'], 'func': rf_replacement_d3_078}


def rf_replacement_d3_079(rf_replacement_d2_079):
    feature = _clean(rf_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_079'] = {'inputs': ['rf_replacement_d2_079'], 'func': rf_replacement_d3_079}


def rf_replacement_d3_080(rf_replacement_d2_080):
    feature = _clean(rf_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_080'] = {'inputs': ['rf_replacement_d2_080'], 'func': rf_replacement_d3_080}


def rf_replacement_d3_081(rf_replacement_d2_081):
    feature = _clean(rf_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_081'] = {'inputs': ['rf_replacement_d2_081'], 'func': rf_replacement_d3_081}


def rf_replacement_d3_082(rf_replacement_d2_082):
    feature = _clean(rf_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_082'] = {'inputs': ['rf_replacement_d2_082'], 'func': rf_replacement_d3_082}


def rf_replacement_d3_083(rf_replacement_d2_083):
    feature = _clean(rf_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_083'] = {'inputs': ['rf_replacement_d2_083'], 'func': rf_replacement_d3_083}


def rf_replacement_d3_084(rf_replacement_d2_084):
    feature = _clean(rf_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_084'] = {'inputs': ['rf_replacement_d2_084'], 'func': rf_replacement_d3_084}


def rf_replacement_d3_085(rf_replacement_d2_085):
    feature = _clean(rf_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_085'] = {'inputs': ['rf_replacement_d2_085'], 'func': rf_replacement_d3_085}


def rf_replacement_d3_086(rf_replacement_d2_086):
    feature = _clean(rf_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_086'] = {'inputs': ['rf_replacement_d2_086'], 'func': rf_replacement_d3_086}


def rf_replacement_d3_087(rf_replacement_d2_087):
    feature = _clean(rf_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_087'] = {'inputs': ['rf_replacement_d2_087'], 'func': rf_replacement_d3_087}


def rf_replacement_d3_088(rf_replacement_d2_088):
    feature = _clean(rf_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_088'] = {'inputs': ['rf_replacement_d2_088'], 'func': rf_replacement_d3_088}


def rf_replacement_d3_089(rf_replacement_d2_089):
    feature = _clean(rf_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_089'] = {'inputs': ['rf_replacement_d2_089'], 'func': rf_replacement_d3_089}


def rf_replacement_d3_090(rf_replacement_d2_090):
    feature = _clean(rf_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_090'] = {'inputs': ['rf_replacement_d2_090'], 'func': rf_replacement_d3_090}


def rf_replacement_d3_091(rf_replacement_d2_091):
    feature = _clean(rf_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_091'] = {'inputs': ['rf_replacement_d2_091'], 'func': rf_replacement_d3_091}


def rf_replacement_d3_092(rf_replacement_d2_092):
    feature = _clean(rf_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_092'] = {'inputs': ['rf_replacement_d2_092'], 'func': rf_replacement_d3_092}


def rf_replacement_d3_093(rf_replacement_d2_093):
    feature = _clean(rf_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_093'] = {'inputs': ['rf_replacement_d2_093'], 'func': rf_replacement_d3_093}


def rf_replacement_d3_094(rf_replacement_d2_094):
    feature = _clean(rf_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_094'] = {'inputs': ['rf_replacement_d2_094'], 'func': rf_replacement_d3_094}


def rf_replacement_d3_095(rf_replacement_d2_095):
    feature = _clean(rf_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_095'] = {'inputs': ['rf_replacement_d2_095'], 'func': rf_replacement_d3_095}


def rf_replacement_d3_096(rf_replacement_d2_096):
    feature = _clean(rf_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_096'] = {'inputs': ['rf_replacement_d2_096'], 'func': rf_replacement_d3_096}


def rf_replacement_d3_097(rf_replacement_d2_097):
    feature = _clean(rf_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_097'] = {'inputs': ['rf_replacement_d2_097'], 'func': rf_replacement_d3_097}


def rf_replacement_d3_098(rf_replacement_d2_098):
    feature = _clean(rf_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_098'] = {'inputs': ['rf_replacement_d2_098'], 'func': rf_replacement_d3_098}


def rf_replacement_d3_099(rf_replacement_d2_099):
    feature = _clean(rf_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_099'] = {'inputs': ['rf_replacement_d2_099'], 'func': rf_replacement_d3_099}


def rf_replacement_d3_100(rf_replacement_d2_100):
    feature = _clean(rf_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_100'] = {'inputs': ['rf_replacement_d2_100'], 'func': rf_replacement_d3_100}


def rf_replacement_d3_101(rf_replacement_d2_101):
    feature = _clean(rf_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_101'] = {'inputs': ['rf_replacement_d2_101'], 'func': rf_replacement_d3_101}


def rf_replacement_d3_102(rf_replacement_d2_102):
    feature = _clean(rf_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_102'] = {'inputs': ['rf_replacement_d2_102'], 'func': rf_replacement_d3_102}


def rf_replacement_d3_103(rf_replacement_d2_103):
    feature = _clean(rf_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_103'] = {'inputs': ['rf_replacement_d2_103'], 'func': rf_replacement_d3_103}


def rf_replacement_d3_104(rf_replacement_d2_104):
    feature = _clean(rf_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_104'] = {'inputs': ['rf_replacement_d2_104'], 'func': rf_replacement_d3_104}


def rf_replacement_d3_105(rf_replacement_d2_105):
    feature = _clean(rf_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_105'] = {'inputs': ['rf_replacement_d2_105'], 'func': rf_replacement_d3_105}


def rf_replacement_d3_106(rf_replacement_d2_106):
    feature = _clean(rf_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_106'] = {'inputs': ['rf_replacement_d2_106'], 'func': rf_replacement_d3_106}


def rf_replacement_d3_107(rf_replacement_d2_107):
    feature = _clean(rf_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_107'] = {'inputs': ['rf_replacement_d2_107'], 'func': rf_replacement_d3_107}


def rf_replacement_d3_108(rf_replacement_d2_108):
    feature = _clean(rf_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_108'] = {'inputs': ['rf_replacement_d2_108'], 'func': rf_replacement_d3_108}


def rf_replacement_d3_109(rf_replacement_d2_109):
    feature = _clean(rf_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_109'] = {'inputs': ['rf_replacement_d2_109'], 'func': rf_replacement_d3_109}


def rf_replacement_d3_110(rf_replacement_d2_110):
    feature = _clean(rf_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_110'] = {'inputs': ['rf_replacement_d2_110'], 'func': rf_replacement_d3_110}


def rf_replacement_d3_111(rf_replacement_d2_111):
    feature = _clean(rf_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_111'] = {'inputs': ['rf_replacement_d2_111'], 'func': rf_replacement_d3_111}


def rf_replacement_d3_112(rf_replacement_d2_112):
    feature = _clean(rf_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_112'] = {'inputs': ['rf_replacement_d2_112'], 'func': rf_replacement_d3_112}


def rf_replacement_d3_113(rf_replacement_d2_113):
    feature = _clean(rf_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_113'] = {'inputs': ['rf_replacement_d2_113'], 'func': rf_replacement_d3_113}


def rf_replacement_d3_114(rf_replacement_d2_114):
    feature = _clean(rf_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_114'] = {'inputs': ['rf_replacement_d2_114'], 'func': rf_replacement_d3_114}


def rf_replacement_d3_115(rf_replacement_d2_115):
    feature = _clean(rf_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_115'] = {'inputs': ['rf_replacement_d2_115'], 'func': rf_replacement_d3_115}


def rf_replacement_d3_116(rf_replacement_d2_116):
    feature = _clean(rf_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_116'] = {'inputs': ['rf_replacement_d2_116'], 'func': rf_replacement_d3_116}


def rf_replacement_d3_117(rf_replacement_d2_117):
    feature = _clean(rf_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_117'] = {'inputs': ['rf_replacement_d2_117'], 'func': rf_replacement_d3_117}


def rf_replacement_d3_118(rf_replacement_d2_118):
    feature = _clean(rf_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_118'] = {'inputs': ['rf_replacement_d2_118'], 'func': rf_replacement_d3_118}


def rf_replacement_d3_119(rf_replacement_d2_119):
    feature = _clean(rf_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_119'] = {'inputs': ['rf_replacement_d2_119'], 'func': rf_replacement_d3_119}


def rf_replacement_d3_120(rf_replacement_d2_120):
    feature = _clean(rf_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_120'] = {'inputs': ['rf_replacement_d2_120'], 'func': rf_replacement_d3_120}


def rf_replacement_d3_121(rf_replacement_d2_121):
    feature = _clean(rf_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_121'] = {'inputs': ['rf_replacement_d2_121'], 'func': rf_replacement_d3_121}


def rf_replacement_d3_122(rf_replacement_d2_122):
    feature = _clean(rf_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_122'] = {'inputs': ['rf_replacement_d2_122'], 'func': rf_replacement_d3_122}


def rf_replacement_d3_123(rf_replacement_d2_123):
    feature = _clean(rf_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_123'] = {'inputs': ['rf_replacement_d2_123'], 'func': rf_replacement_d3_123}


def rf_replacement_d3_124(rf_replacement_d2_124):
    feature = _clean(rf_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_124'] = {'inputs': ['rf_replacement_d2_124'], 'func': rf_replacement_d3_124}


def rf_replacement_d3_125(rf_replacement_d2_125):
    feature = _clean(rf_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_125'] = {'inputs': ['rf_replacement_d2_125'], 'func': rf_replacement_d3_125}


def rf_replacement_d3_126(rf_replacement_d2_126):
    feature = _clean(rf_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_126'] = {'inputs': ['rf_replacement_d2_126'], 'func': rf_replacement_d3_126}


def rf_replacement_d3_127(rf_replacement_d2_127):
    feature = _clean(rf_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_127'] = {'inputs': ['rf_replacement_d2_127'], 'func': rf_replacement_d3_127}


def rf_replacement_d3_128(rf_replacement_d2_128):
    feature = _clean(rf_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_128'] = {'inputs': ['rf_replacement_d2_128'], 'func': rf_replacement_d3_128}


def rf_replacement_d3_129(rf_replacement_d2_129):
    feature = _clean(rf_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_129'] = {'inputs': ['rf_replacement_d2_129'], 'func': rf_replacement_d3_129}


def rf_replacement_d3_130(rf_replacement_d2_130):
    feature = _clean(rf_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_130'] = {'inputs': ['rf_replacement_d2_130'], 'func': rf_replacement_d3_130}


def rf_replacement_d3_131(rf_replacement_d2_131):
    feature = _clean(rf_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_131'] = {'inputs': ['rf_replacement_d2_131'], 'func': rf_replacement_d3_131}


def rf_replacement_d3_132(rf_replacement_d2_132):
    feature = _clean(rf_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_132'] = {'inputs': ['rf_replacement_d2_132'], 'func': rf_replacement_d3_132}


def rf_replacement_d3_133(rf_replacement_d2_133):
    feature = _clean(rf_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_133'] = {'inputs': ['rf_replacement_d2_133'], 'func': rf_replacement_d3_133}


def rf_replacement_d3_134(rf_replacement_d2_134):
    feature = _clean(rf_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_134'] = {'inputs': ['rf_replacement_d2_134'], 'func': rf_replacement_d3_134}


def rf_replacement_d3_135(rf_replacement_d2_135):
    feature = _clean(rf_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_135'] = {'inputs': ['rf_replacement_d2_135'], 'func': rf_replacement_d3_135}


def rf_replacement_d3_136(rf_replacement_d2_136):
    feature = _clean(rf_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_136'] = {'inputs': ['rf_replacement_d2_136'], 'func': rf_replacement_d3_136}


def rf_replacement_d3_137(rf_replacement_d2_137):
    feature = _clean(rf_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_137'] = {'inputs': ['rf_replacement_d2_137'], 'func': rf_replacement_d3_137}


def rf_replacement_d3_138(rf_replacement_d2_138):
    feature = _clean(rf_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_138'] = {'inputs': ['rf_replacement_d2_138'], 'func': rf_replacement_d3_138}


def rf_replacement_d3_139(rf_replacement_d2_139):
    feature = _clean(rf_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_139'] = {'inputs': ['rf_replacement_d2_139'], 'func': rf_replacement_d3_139}


def rf_replacement_d3_140(rf_replacement_d2_140):
    feature = _clean(rf_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_140'] = {'inputs': ['rf_replacement_d2_140'], 'func': rf_replacement_d3_140}


def rf_replacement_d3_141(rf_replacement_d2_141):
    feature = _clean(rf_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_141'] = {'inputs': ['rf_replacement_d2_141'], 'func': rf_replacement_d3_141}


def rf_replacement_d3_142(rf_replacement_d2_142):
    feature = _clean(rf_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_142'] = {'inputs': ['rf_replacement_d2_142'], 'func': rf_replacement_d3_142}


def rf_replacement_d3_143(rf_replacement_d2_143):
    feature = _clean(rf_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_143'] = {'inputs': ['rf_replacement_d2_143'], 'func': rf_replacement_d3_143}


def rf_replacement_d3_144(rf_replacement_d2_144):
    feature = _clean(rf_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_144'] = {'inputs': ['rf_replacement_d2_144'], 'func': rf_replacement_d3_144}


def rf_replacement_d3_145(rf_replacement_d2_145):
    feature = _clean(rf_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_145'] = {'inputs': ['rf_replacement_d2_145'], 'func': rf_replacement_d3_145}


def rf_replacement_d3_146(rf_replacement_d2_146):
    feature = _clean(rf_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_146'] = {'inputs': ['rf_replacement_d2_146'], 'func': rf_replacement_d3_146}


def rf_replacement_d3_147(rf_replacement_d2_147):
    feature = _clean(rf_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_147'] = {'inputs': ['rf_replacement_d2_147'], 'func': rf_replacement_d3_147}


def rf_replacement_d3_148(rf_replacement_d2_148):
    feature = _clean(rf_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_148'] = {'inputs': ['rf_replacement_d2_148'], 'func': rf_replacement_d3_148}


def rf_replacement_d3_149(rf_replacement_d2_149):
    feature = _clean(rf_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_149'] = {'inputs': ['rf_replacement_d2_149'], 'func': rf_replacement_d3_149}


def rf_replacement_d3_150(rf_replacement_d2_150):
    feature = _clean(rf_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_150'] = {'inputs': ['rf_replacement_d2_150'], 'func': rf_replacement_d3_150}


def rf_replacement_d3_151(rf_replacement_d2_151):
    feature = _clean(rf_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_151'] = {'inputs': ['rf_replacement_d2_151'], 'func': rf_replacement_d3_151}


def rf_replacement_d3_152(rf_replacement_d2_152):
    feature = _clean(rf_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_152'] = {'inputs': ['rf_replacement_d2_152'], 'func': rf_replacement_d3_152}


def rf_replacement_d3_153(rf_replacement_d2_153):
    feature = _clean(rf_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_153'] = {'inputs': ['rf_replacement_d2_153'], 'func': rf_replacement_d3_153}


def rf_replacement_d3_154(rf_replacement_d2_154):
    feature = _clean(rf_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_154'] = {'inputs': ['rf_replacement_d2_154'], 'func': rf_replacement_d3_154}


def rf_replacement_d3_155(rf_replacement_d2_155):
    feature = _clean(rf_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_155'] = {'inputs': ['rf_replacement_d2_155'], 'func': rf_replacement_d3_155}


def rf_replacement_d3_156(rf_replacement_d2_156):
    feature = _clean(rf_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_156'] = {'inputs': ['rf_replacement_d2_156'], 'func': rf_replacement_d3_156}


def rf_replacement_d3_157(rf_replacement_d2_157):
    feature = _clean(rf_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_157'] = {'inputs': ['rf_replacement_d2_157'], 'func': rf_replacement_d3_157}


def rf_replacement_d3_158(rf_replacement_d2_158):
    feature = _clean(rf_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_158'] = {'inputs': ['rf_replacement_d2_158'], 'func': rf_replacement_d3_158}


def rf_replacement_d3_159(rf_replacement_d2_159):
    feature = _clean(rf_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_159'] = {'inputs': ['rf_replacement_d2_159'], 'func': rf_replacement_d3_159}


def rf_replacement_d3_160(rf_replacement_d2_160):
    feature = _clean(rf_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_160'] = {'inputs': ['rf_replacement_d2_160'], 'func': rf_replacement_d3_160}


def rf_replacement_d3_161(rf_replacement_d2_161):
    feature = _clean(rf_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_161'] = {'inputs': ['rf_replacement_d2_161'], 'func': rf_replacement_d3_161}


def rf_replacement_d3_162(rf_replacement_d2_162):
    feature = _clean(rf_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_162'] = {'inputs': ['rf_replacement_d2_162'], 'func': rf_replacement_d3_162}


def rf_replacement_d3_163(rf_replacement_d2_163):
    feature = _clean(rf_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_163'] = {'inputs': ['rf_replacement_d2_163'], 'func': rf_replacement_d3_163}


def rf_replacement_d3_164(rf_replacement_d2_164):
    feature = _clean(rf_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_164'] = {'inputs': ['rf_replacement_d2_164'], 'func': rf_replacement_d3_164}


def rf_replacement_d3_165(rf_replacement_d2_165):
    feature = _clean(rf_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_165'] = {'inputs': ['rf_replacement_d2_165'], 'func': rf_replacement_d3_165}


def rf_replacement_d3_166(rf_replacement_d2_166):
    feature = _clean(rf_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_166'] = {'inputs': ['rf_replacement_d2_166'], 'func': rf_replacement_d3_166}


def rf_replacement_d3_167(rf_replacement_d2_167):
    feature = _clean(rf_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_167'] = {'inputs': ['rf_replacement_d2_167'], 'func': rf_replacement_d3_167}


def rf_replacement_d3_168(rf_replacement_d2_168):
    feature = _clean(rf_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_168'] = {'inputs': ['rf_replacement_d2_168'], 'func': rf_replacement_d3_168}


def rf_replacement_d3_169(rf_replacement_d2_169):
    feature = _clean(rf_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_169'] = {'inputs': ['rf_replacement_d2_169'], 'func': rf_replacement_d3_169}


def rf_replacement_d3_170(rf_replacement_d2_170):
    feature = _clean(rf_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
RF_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rf_replacement_d3_170'] = {'inputs': ['rf_replacement_d2_170'], 'func': rf_replacement_d3_170}


# Third-derivative extensions for repaired first-base features.
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rfl_base_universe_d3_001_rfl_002_low_distance_10_002(rfl_base_universe_d2_001_rfl_002_low_distance_10_002):
    return _base_universe_d3(rfl_base_universe_d2_001_rfl_002_low_distance_10_002, 1)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_001_rfl_002_low_distance_10_002'] = {'inputs': ['rfl_base_universe_d2_001_rfl_002_low_distance_10_002'], 'func': rfl_base_universe_d3_001_rfl_002_low_distance_10_002}


def rfl_base_universe_d3_002_rfl_003_underwater_area_21_003(rfl_base_universe_d2_002_rfl_003_underwater_area_21_003):
    return _base_universe_d3(rfl_base_universe_d2_002_rfl_003_underwater_area_21_003, 2)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_002_rfl_003_underwater_area_21_003'] = {'inputs': ['rfl_base_universe_d2_002_rfl_003_underwater_area_21_003'], 'func': rfl_base_universe_d3_002_rfl_003_underwater_area_21_003}


def rfl_base_universe_d3_003_rfl_006_lower_high_ratio_84_006(rfl_base_universe_d2_003_rfl_006_lower_high_ratio_84_006):
    return _base_universe_d3(rfl_base_universe_d2_003_rfl_006_lower_high_ratio_84_006, 3)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_003_rfl_006_lower_high_ratio_84_006'] = {'inputs': ['rfl_base_universe_d2_003_rfl_006_lower_high_ratio_84_006'], 'func': rfl_base_universe_d3_003_rfl_006_lower_high_ratio_84_006}


def rfl_base_universe_d3_004_rfl_008_low_distance_189_008(rfl_base_universe_d2_004_rfl_008_low_distance_189_008):
    return _base_universe_d3(rfl_base_universe_d2_004_rfl_008_low_distance_189_008, 4)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_004_rfl_008_low_distance_189_008'] = {'inputs': ['rfl_base_universe_d2_004_rfl_008_low_distance_189_008'], 'func': rfl_base_universe_d3_004_rfl_008_low_distance_189_008}


def rfl_base_universe_d3_005_rfl_009_underwater_area_252_009(rfl_base_universe_d2_005_rfl_009_underwater_area_252_009):
    return _base_universe_d3(rfl_base_universe_d2_005_rfl_009_underwater_area_252_009, 5)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_005_rfl_009_underwater_area_252_009'] = {'inputs': ['rfl_base_universe_d2_005_rfl_009_underwater_area_252_009'], 'func': rfl_base_universe_d3_005_rfl_009_underwater_area_252_009}


def rfl_base_universe_d3_006_rfl_012_lower_high_ratio_756_012(rfl_base_universe_d2_006_rfl_012_lower_high_ratio_756_012):
    return _base_universe_d3(rfl_base_universe_d2_006_rfl_012_lower_high_ratio_756_012, 6)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_006_rfl_012_lower_high_ratio_756_012'] = {'inputs': ['rfl_base_universe_d2_006_rfl_012_lower_high_ratio_756_012'], 'func': rfl_base_universe_d3_006_rfl_012_lower_high_ratio_756_012}


def rfl_base_universe_d3_007_rfl_014_low_distance_1260_014(rfl_base_universe_d2_007_rfl_014_low_distance_1260_014):
    return _base_universe_d3(rfl_base_universe_d2_007_rfl_014_low_distance_1260_014, 7)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_007_rfl_014_low_distance_1260_014'] = {'inputs': ['rfl_base_universe_d2_007_rfl_014_low_distance_1260_014'], 'func': rfl_base_universe_d3_007_rfl_014_low_distance_1260_014}


def rfl_base_universe_d3_008_rfl_015_underwater_area_1512_015(rfl_base_universe_d2_008_rfl_015_underwater_area_1512_015):
    return _base_universe_d3(rfl_base_universe_d2_008_rfl_015_underwater_area_1512_015, 8)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_008_rfl_015_underwater_area_1512_015'] = {'inputs': ['rfl_base_universe_d2_008_rfl_015_underwater_area_1512_015'], 'func': rfl_base_universe_d3_008_rfl_015_underwater_area_1512_015}


def rfl_base_universe_d3_009_rfl_018_lower_high_ratio_21_018(rfl_base_universe_d2_009_rfl_018_lower_high_ratio_21_018):
    return _base_universe_d3(rfl_base_universe_d2_009_rfl_018_lower_high_ratio_21_018, 9)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_009_rfl_018_lower_high_ratio_21_018'] = {'inputs': ['rfl_base_universe_d2_009_rfl_018_lower_high_ratio_21_018'], 'func': rfl_base_universe_d3_009_rfl_018_lower_high_ratio_21_018}


def rfl_base_universe_d3_010_rfl_020_low_distance_63_020(rfl_base_universe_d2_010_rfl_020_low_distance_63_020):
    return _base_universe_d3(rfl_base_universe_d2_010_rfl_020_low_distance_63_020, 10)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_010_rfl_020_low_distance_63_020'] = {'inputs': ['rfl_base_universe_d2_010_rfl_020_low_distance_63_020'], 'func': rfl_base_universe_d3_010_rfl_020_low_distance_63_020}


def rfl_base_universe_d3_011_rfl_021_underwater_area_84_021(rfl_base_universe_d2_011_rfl_021_underwater_area_84_021):
    return _base_universe_d3(rfl_base_universe_d2_011_rfl_021_underwater_area_84_021, 11)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_011_rfl_021_underwater_area_84_021'] = {'inputs': ['rfl_base_universe_d2_011_rfl_021_underwater_area_84_021'], 'func': rfl_base_universe_d3_011_rfl_021_underwater_area_84_021}


def rfl_base_universe_d3_012_rfl_024_lower_high_ratio_252_024(rfl_base_universe_d2_012_rfl_024_lower_high_ratio_252_024):
    return _base_universe_d3(rfl_base_universe_d2_012_rfl_024_lower_high_ratio_252_024, 12)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_012_rfl_024_lower_high_ratio_252_024'] = {'inputs': ['rfl_base_universe_d2_012_rfl_024_lower_high_ratio_252_024'], 'func': rfl_base_universe_d3_012_rfl_024_lower_high_ratio_252_024}


def rfl_base_universe_d3_013_rfl_026_low_distance_504_026(rfl_base_universe_d2_013_rfl_026_low_distance_504_026):
    return _base_universe_d3(rfl_base_universe_d2_013_rfl_026_low_distance_504_026, 13)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_013_rfl_026_low_distance_504_026'] = {'inputs': ['rfl_base_universe_d2_013_rfl_026_low_distance_504_026'], 'func': rfl_base_universe_d3_013_rfl_026_low_distance_504_026}


def rfl_base_universe_d3_014_rfl_027_underwater_area_756_027(rfl_base_universe_d2_014_rfl_027_underwater_area_756_027):
    return _base_universe_d3(rfl_base_universe_d2_014_rfl_027_underwater_area_756_027, 14)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_014_rfl_027_underwater_area_756_027'] = {'inputs': ['rfl_base_universe_d2_014_rfl_027_underwater_area_756_027'], 'func': rfl_base_universe_d3_014_rfl_027_underwater_area_756_027}


def rfl_base_universe_d3_015_rfl_030_lower_high_ratio_1512_030(rfl_base_universe_d2_015_rfl_030_lower_high_ratio_1512_030):
    return _base_universe_d3(rfl_base_universe_d2_015_rfl_030_lower_high_ratio_1512_030, 15)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_015_rfl_030_lower_high_ratio_1512_030'] = {'inputs': ['rfl_base_universe_d2_015_rfl_030_lower_high_ratio_1512_030'], 'func': rfl_base_universe_d3_015_rfl_030_lower_high_ratio_1512_030}


def rfl_base_universe_d3_016_rfl_basefill_004(rfl_base_universe_d2_016_rfl_basefill_004):
    return _base_universe_d3(rfl_base_universe_d2_016_rfl_basefill_004, 16)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_016_rfl_basefill_004'] = {'inputs': ['rfl_base_universe_d2_016_rfl_basefill_004'], 'func': rfl_base_universe_d3_016_rfl_basefill_004}


def rfl_base_universe_d3_017_rfl_basefill_005(rfl_base_universe_d2_017_rfl_basefill_005):
    return _base_universe_d3(rfl_base_universe_d2_017_rfl_basefill_005, 17)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_017_rfl_basefill_005'] = {'inputs': ['rfl_base_universe_d2_017_rfl_basefill_005'], 'func': rfl_base_universe_d3_017_rfl_basefill_005}


def rfl_base_universe_d3_018_rfl_basefill_010(rfl_base_universe_d2_018_rfl_basefill_010):
    return _base_universe_d3(rfl_base_universe_d2_018_rfl_basefill_010, 18)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_018_rfl_basefill_010'] = {'inputs': ['rfl_base_universe_d2_018_rfl_basefill_010'], 'func': rfl_base_universe_d3_018_rfl_basefill_010}


def rfl_base_universe_d3_019_rfl_basefill_011(rfl_base_universe_d2_019_rfl_basefill_011):
    return _base_universe_d3(rfl_base_universe_d2_019_rfl_basefill_011, 19)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_019_rfl_basefill_011'] = {'inputs': ['rfl_base_universe_d2_019_rfl_basefill_011'], 'func': rfl_base_universe_d3_019_rfl_basefill_011}


def rfl_base_universe_d3_020_rfl_basefill_016(rfl_base_universe_d2_020_rfl_basefill_016):
    return _base_universe_d3(rfl_base_universe_d2_020_rfl_basefill_016, 20)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_020_rfl_basefill_016'] = {'inputs': ['rfl_base_universe_d2_020_rfl_basefill_016'], 'func': rfl_base_universe_d3_020_rfl_basefill_016}


def rfl_base_universe_d3_021_rfl_basefill_017(rfl_base_universe_d2_021_rfl_basefill_017):
    return _base_universe_d3(rfl_base_universe_d2_021_rfl_basefill_017, 21)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_021_rfl_basefill_017'] = {'inputs': ['rfl_base_universe_d2_021_rfl_basefill_017'], 'func': rfl_base_universe_d3_021_rfl_basefill_017}


def rfl_base_universe_d3_022_rfl_basefill_022(rfl_base_universe_d2_022_rfl_basefill_022):
    return _base_universe_d3(rfl_base_universe_d2_022_rfl_basefill_022, 22)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_022_rfl_basefill_022'] = {'inputs': ['rfl_base_universe_d2_022_rfl_basefill_022'], 'func': rfl_base_universe_d3_022_rfl_basefill_022}


def rfl_base_universe_d3_023_rfl_basefill_023(rfl_base_universe_d2_023_rfl_basefill_023):
    return _base_universe_d3(rfl_base_universe_d2_023_rfl_basefill_023, 23)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_023_rfl_basefill_023'] = {'inputs': ['rfl_base_universe_d2_023_rfl_basefill_023'], 'func': rfl_base_universe_d3_023_rfl_basefill_023}


def rfl_base_universe_d3_024_rfl_basefill_028(rfl_base_universe_d2_024_rfl_basefill_028):
    return _base_universe_d3(rfl_base_universe_d2_024_rfl_basefill_028, 24)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_024_rfl_basefill_028'] = {'inputs': ['rfl_base_universe_d2_024_rfl_basefill_028'], 'func': rfl_base_universe_d3_024_rfl_basefill_028}


def rfl_base_universe_d3_025_rfl_basefill_029(rfl_base_universe_d2_025_rfl_basefill_029):
    return _base_universe_d3(rfl_base_universe_d2_025_rfl_basefill_029, 25)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_025_rfl_basefill_029'] = {'inputs': ['rfl_base_universe_d2_025_rfl_basefill_029'], 'func': rfl_base_universe_d3_025_rfl_basefill_029}


def rfl_base_universe_d3_026_rfl_basefill_031(rfl_base_universe_d2_026_rfl_basefill_031):
    return _base_universe_d3(rfl_base_universe_d2_026_rfl_basefill_031, 26)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_026_rfl_basefill_031'] = {'inputs': ['rfl_base_universe_d2_026_rfl_basefill_031'], 'func': rfl_base_universe_d3_026_rfl_basefill_031}


def rfl_base_universe_d3_027_rfl_basefill_032(rfl_base_universe_d2_027_rfl_basefill_032):
    return _base_universe_d3(rfl_base_universe_d2_027_rfl_basefill_032, 27)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_027_rfl_basefill_032'] = {'inputs': ['rfl_base_universe_d2_027_rfl_basefill_032'], 'func': rfl_base_universe_d3_027_rfl_basefill_032}


def rfl_base_universe_d3_028_rfl_basefill_033(rfl_base_universe_d2_028_rfl_basefill_033):
    return _base_universe_d3(rfl_base_universe_d2_028_rfl_basefill_033, 28)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_028_rfl_basefill_033'] = {'inputs': ['rfl_base_universe_d2_028_rfl_basefill_033'], 'func': rfl_base_universe_d3_028_rfl_basefill_033}


def rfl_base_universe_d3_029_rfl_basefill_034(rfl_base_universe_d2_029_rfl_basefill_034):
    return _base_universe_d3(rfl_base_universe_d2_029_rfl_basefill_034, 29)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_029_rfl_basefill_034'] = {'inputs': ['rfl_base_universe_d2_029_rfl_basefill_034'], 'func': rfl_base_universe_d3_029_rfl_basefill_034}


def rfl_base_universe_d3_030_rfl_basefill_035(rfl_base_universe_d2_030_rfl_basefill_035):
    return _base_universe_d3(rfl_base_universe_d2_030_rfl_basefill_035, 30)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_030_rfl_basefill_035'] = {'inputs': ['rfl_base_universe_d2_030_rfl_basefill_035'], 'func': rfl_base_universe_d3_030_rfl_basefill_035}


def rfl_base_universe_d3_031_rfl_basefill_036(rfl_base_universe_d2_031_rfl_basefill_036):
    return _base_universe_d3(rfl_base_universe_d2_031_rfl_basefill_036, 31)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_031_rfl_basefill_036'] = {'inputs': ['rfl_base_universe_d2_031_rfl_basefill_036'], 'func': rfl_base_universe_d3_031_rfl_basefill_036}


def rfl_base_universe_d3_032_rfl_basefill_037(rfl_base_universe_d2_032_rfl_basefill_037):
    return _base_universe_d3(rfl_base_universe_d2_032_rfl_basefill_037, 32)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_032_rfl_basefill_037'] = {'inputs': ['rfl_base_universe_d2_032_rfl_basefill_037'], 'func': rfl_base_universe_d3_032_rfl_basefill_037}


def rfl_base_universe_d3_033_rfl_basefill_038(rfl_base_universe_d2_033_rfl_basefill_038):
    return _base_universe_d3(rfl_base_universe_d2_033_rfl_basefill_038, 33)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_033_rfl_basefill_038'] = {'inputs': ['rfl_base_universe_d2_033_rfl_basefill_038'], 'func': rfl_base_universe_d3_033_rfl_basefill_038}


def rfl_base_universe_d3_034_rfl_basefill_039(rfl_base_universe_d2_034_rfl_basefill_039):
    return _base_universe_d3(rfl_base_universe_d2_034_rfl_basefill_039, 34)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_034_rfl_basefill_039'] = {'inputs': ['rfl_base_universe_d2_034_rfl_basefill_039'], 'func': rfl_base_universe_d3_034_rfl_basefill_039}


def rfl_base_universe_d3_035_rfl_basefill_040(rfl_base_universe_d2_035_rfl_basefill_040):
    return _base_universe_d3(rfl_base_universe_d2_035_rfl_basefill_040, 35)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_035_rfl_basefill_040'] = {'inputs': ['rfl_base_universe_d2_035_rfl_basefill_040'], 'func': rfl_base_universe_d3_035_rfl_basefill_040}


def rfl_base_universe_d3_036_rfl_basefill_041(rfl_base_universe_d2_036_rfl_basefill_041):
    return _base_universe_d3(rfl_base_universe_d2_036_rfl_basefill_041, 36)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_036_rfl_basefill_041'] = {'inputs': ['rfl_base_universe_d2_036_rfl_basefill_041'], 'func': rfl_base_universe_d3_036_rfl_basefill_041}


def rfl_base_universe_d3_037_rfl_basefill_042(rfl_base_universe_d2_037_rfl_basefill_042):
    return _base_universe_d3(rfl_base_universe_d2_037_rfl_basefill_042, 37)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_037_rfl_basefill_042'] = {'inputs': ['rfl_base_universe_d2_037_rfl_basefill_042'], 'func': rfl_base_universe_d3_037_rfl_basefill_042}


def rfl_base_universe_d3_038_rfl_basefill_043(rfl_base_universe_d2_038_rfl_basefill_043):
    return _base_universe_d3(rfl_base_universe_d2_038_rfl_basefill_043, 38)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_038_rfl_basefill_043'] = {'inputs': ['rfl_base_universe_d2_038_rfl_basefill_043'], 'func': rfl_base_universe_d3_038_rfl_basefill_043}


def rfl_base_universe_d3_039_rfl_basefill_044(rfl_base_universe_d2_039_rfl_basefill_044):
    return _base_universe_d3(rfl_base_universe_d2_039_rfl_basefill_044, 39)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_039_rfl_basefill_044'] = {'inputs': ['rfl_base_universe_d2_039_rfl_basefill_044'], 'func': rfl_base_universe_d3_039_rfl_basefill_044}


def rfl_base_universe_d3_040_rfl_basefill_045(rfl_base_universe_d2_040_rfl_basefill_045):
    return _base_universe_d3(rfl_base_universe_d2_040_rfl_basefill_045, 40)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_040_rfl_basefill_045'] = {'inputs': ['rfl_base_universe_d2_040_rfl_basefill_045'], 'func': rfl_base_universe_d3_040_rfl_basefill_045}


def rfl_base_universe_d3_041_rfl_basefill_046(rfl_base_universe_d2_041_rfl_basefill_046):
    return _base_universe_d3(rfl_base_universe_d2_041_rfl_basefill_046, 41)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_041_rfl_basefill_046'] = {'inputs': ['rfl_base_universe_d2_041_rfl_basefill_046'], 'func': rfl_base_universe_d3_041_rfl_basefill_046}


def rfl_base_universe_d3_042_rfl_basefill_047(rfl_base_universe_d2_042_rfl_basefill_047):
    return _base_universe_d3(rfl_base_universe_d2_042_rfl_basefill_047, 42)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_042_rfl_basefill_047'] = {'inputs': ['rfl_base_universe_d2_042_rfl_basefill_047'], 'func': rfl_base_universe_d3_042_rfl_basefill_047}


def rfl_base_universe_d3_043_rfl_basefill_048(rfl_base_universe_d2_043_rfl_basefill_048):
    return _base_universe_d3(rfl_base_universe_d2_043_rfl_basefill_048, 43)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_043_rfl_basefill_048'] = {'inputs': ['rfl_base_universe_d2_043_rfl_basefill_048'], 'func': rfl_base_universe_d3_043_rfl_basefill_048}


def rfl_base_universe_d3_044_rfl_basefill_049(rfl_base_universe_d2_044_rfl_basefill_049):
    return _base_universe_d3(rfl_base_universe_d2_044_rfl_basefill_049, 44)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_044_rfl_basefill_049'] = {'inputs': ['rfl_base_universe_d2_044_rfl_basefill_049'], 'func': rfl_base_universe_d3_044_rfl_basefill_049}


def rfl_base_universe_d3_045_rfl_basefill_050(rfl_base_universe_d2_045_rfl_basefill_050):
    return _base_universe_d3(rfl_base_universe_d2_045_rfl_basefill_050, 45)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_045_rfl_basefill_050'] = {'inputs': ['rfl_base_universe_d2_045_rfl_basefill_050'], 'func': rfl_base_universe_d3_045_rfl_basefill_050}


def rfl_base_universe_d3_046_rfl_basefill_051(rfl_base_universe_d2_046_rfl_basefill_051):
    return _base_universe_d3(rfl_base_universe_d2_046_rfl_basefill_051, 46)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_046_rfl_basefill_051'] = {'inputs': ['rfl_base_universe_d2_046_rfl_basefill_051'], 'func': rfl_base_universe_d3_046_rfl_basefill_051}


def rfl_base_universe_d3_047_rfl_basefill_052(rfl_base_universe_d2_047_rfl_basefill_052):
    return _base_universe_d3(rfl_base_universe_d2_047_rfl_basefill_052, 47)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_047_rfl_basefill_052'] = {'inputs': ['rfl_base_universe_d2_047_rfl_basefill_052'], 'func': rfl_base_universe_d3_047_rfl_basefill_052}


def rfl_base_universe_d3_048_rfl_basefill_053(rfl_base_universe_d2_048_rfl_basefill_053):
    return _base_universe_d3(rfl_base_universe_d2_048_rfl_basefill_053, 48)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_048_rfl_basefill_053'] = {'inputs': ['rfl_base_universe_d2_048_rfl_basefill_053'], 'func': rfl_base_universe_d3_048_rfl_basefill_053}


def rfl_base_universe_d3_049_rfl_basefill_054(rfl_base_universe_d2_049_rfl_basefill_054):
    return _base_universe_d3(rfl_base_universe_d2_049_rfl_basefill_054, 49)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_049_rfl_basefill_054'] = {'inputs': ['rfl_base_universe_d2_049_rfl_basefill_054'], 'func': rfl_base_universe_d3_049_rfl_basefill_054}


def rfl_base_universe_d3_050_rfl_basefill_055(rfl_base_universe_d2_050_rfl_basefill_055):
    return _base_universe_d3(rfl_base_universe_d2_050_rfl_basefill_055, 50)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_050_rfl_basefill_055'] = {'inputs': ['rfl_base_universe_d2_050_rfl_basefill_055'], 'func': rfl_base_universe_d3_050_rfl_basefill_055}


def rfl_base_universe_d3_051_rfl_basefill_056(rfl_base_universe_d2_051_rfl_basefill_056):
    return _base_universe_d3(rfl_base_universe_d2_051_rfl_basefill_056, 51)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_051_rfl_basefill_056'] = {'inputs': ['rfl_base_universe_d2_051_rfl_basefill_056'], 'func': rfl_base_universe_d3_051_rfl_basefill_056}


def rfl_base_universe_d3_052_rfl_basefill_057(rfl_base_universe_d2_052_rfl_basefill_057):
    return _base_universe_d3(rfl_base_universe_d2_052_rfl_basefill_057, 52)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_052_rfl_basefill_057'] = {'inputs': ['rfl_base_universe_d2_052_rfl_basefill_057'], 'func': rfl_base_universe_d3_052_rfl_basefill_057}


def rfl_base_universe_d3_053_rfl_basefill_058(rfl_base_universe_d2_053_rfl_basefill_058):
    return _base_universe_d3(rfl_base_universe_d2_053_rfl_basefill_058, 53)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_053_rfl_basefill_058'] = {'inputs': ['rfl_base_universe_d2_053_rfl_basefill_058'], 'func': rfl_base_universe_d3_053_rfl_basefill_058}


def rfl_base_universe_d3_054_rfl_basefill_059(rfl_base_universe_d2_054_rfl_basefill_059):
    return _base_universe_d3(rfl_base_universe_d2_054_rfl_basefill_059, 54)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_054_rfl_basefill_059'] = {'inputs': ['rfl_base_universe_d2_054_rfl_basefill_059'], 'func': rfl_base_universe_d3_054_rfl_basefill_059}


def rfl_base_universe_d3_055_rfl_basefill_060(rfl_base_universe_d2_055_rfl_basefill_060):
    return _base_universe_d3(rfl_base_universe_d2_055_rfl_basefill_060, 55)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_055_rfl_basefill_060'] = {'inputs': ['rfl_base_universe_d2_055_rfl_basefill_060'], 'func': rfl_base_universe_d3_055_rfl_basefill_060}


def rfl_base_universe_d3_056_rfl_basefill_061(rfl_base_universe_d2_056_rfl_basefill_061):
    return _base_universe_d3(rfl_base_universe_d2_056_rfl_basefill_061, 56)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_056_rfl_basefill_061'] = {'inputs': ['rfl_base_universe_d2_056_rfl_basefill_061'], 'func': rfl_base_universe_d3_056_rfl_basefill_061}


def rfl_base_universe_d3_057_rfl_basefill_062(rfl_base_universe_d2_057_rfl_basefill_062):
    return _base_universe_d3(rfl_base_universe_d2_057_rfl_basefill_062, 57)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_057_rfl_basefill_062'] = {'inputs': ['rfl_base_universe_d2_057_rfl_basefill_062'], 'func': rfl_base_universe_d3_057_rfl_basefill_062}


def rfl_base_universe_d3_058_rfl_basefill_063(rfl_base_universe_d2_058_rfl_basefill_063):
    return _base_universe_d3(rfl_base_universe_d2_058_rfl_basefill_063, 58)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_058_rfl_basefill_063'] = {'inputs': ['rfl_base_universe_d2_058_rfl_basefill_063'], 'func': rfl_base_universe_d3_058_rfl_basefill_063}


def rfl_base_universe_d3_059_rfl_basefill_064(rfl_base_universe_d2_059_rfl_basefill_064):
    return _base_universe_d3(rfl_base_universe_d2_059_rfl_basefill_064, 59)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_059_rfl_basefill_064'] = {'inputs': ['rfl_base_universe_d2_059_rfl_basefill_064'], 'func': rfl_base_universe_d3_059_rfl_basefill_064}


def rfl_base_universe_d3_060_rfl_basefill_065(rfl_base_universe_d2_060_rfl_basefill_065):
    return _base_universe_d3(rfl_base_universe_d2_060_rfl_basefill_065, 60)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_060_rfl_basefill_065'] = {'inputs': ['rfl_base_universe_d2_060_rfl_basefill_065'], 'func': rfl_base_universe_d3_060_rfl_basefill_065}


def rfl_base_universe_d3_061_rfl_basefill_066(rfl_base_universe_d2_061_rfl_basefill_066):
    return _base_universe_d3(rfl_base_universe_d2_061_rfl_basefill_066, 61)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_061_rfl_basefill_066'] = {'inputs': ['rfl_base_universe_d2_061_rfl_basefill_066'], 'func': rfl_base_universe_d3_061_rfl_basefill_066}


def rfl_base_universe_d3_062_rfl_basefill_067(rfl_base_universe_d2_062_rfl_basefill_067):
    return _base_universe_d3(rfl_base_universe_d2_062_rfl_basefill_067, 62)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_062_rfl_basefill_067'] = {'inputs': ['rfl_base_universe_d2_062_rfl_basefill_067'], 'func': rfl_base_universe_d3_062_rfl_basefill_067}


def rfl_base_universe_d3_063_rfl_basefill_068(rfl_base_universe_d2_063_rfl_basefill_068):
    return _base_universe_d3(rfl_base_universe_d2_063_rfl_basefill_068, 63)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_063_rfl_basefill_068'] = {'inputs': ['rfl_base_universe_d2_063_rfl_basefill_068'], 'func': rfl_base_universe_d3_063_rfl_basefill_068}


def rfl_base_universe_d3_064_rfl_basefill_069(rfl_base_universe_d2_064_rfl_basefill_069):
    return _base_universe_d3(rfl_base_universe_d2_064_rfl_basefill_069, 64)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_064_rfl_basefill_069'] = {'inputs': ['rfl_base_universe_d2_064_rfl_basefill_069'], 'func': rfl_base_universe_d3_064_rfl_basefill_069}


def rfl_base_universe_d3_065_rfl_basefill_070(rfl_base_universe_d2_065_rfl_basefill_070):
    return _base_universe_d3(rfl_base_universe_d2_065_rfl_basefill_070, 65)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_065_rfl_basefill_070'] = {'inputs': ['rfl_base_universe_d2_065_rfl_basefill_070'], 'func': rfl_base_universe_d3_065_rfl_basefill_070}


def rfl_base_universe_d3_066_rfl_basefill_071(rfl_base_universe_d2_066_rfl_basefill_071):
    return _base_universe_d3(rfl_base_universe_d2_066_rfl_basefill_071, 66)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_066_rfl_basefill_071'] = {'inputs': ['rfl_base_universe_d2_066_rfl_basefill_071'], 'func': rfl_base_universe_d3_066_rfl_basefill_071}


def rfl_base_universe_d3_067_rfl_basefill_072(rfl_base_universe_d2_067_rfl_basefill_072):
    return _base_universe_d3(rfl_base_universe_d2_067_rfl_basefill_072, 67)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_067_rfl_basefill_072'] = {'inputs': ['rfl_base_universe_d2_067_rfl_basefill_072'], 'func': rfl_base_universe_d3_067_rfl_basefill_072}


def rfl_base_universe_d3_068_rfl_basefill_073(rfl_base_universe_d2_068_rfl_basefill_073):
    return _base_universe_d3(rfl_base_universe_d2_068_rfl_basefill_073, 68)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_068_rfl_basefill_073'] = {'inputs': ['rfl_base_universe_d2_068_rfl_basefill_073'], 'func': rfl_base_universe_d3_068_rfl_basefill_073}


def rfl_base_universe_d3_069_rfl_basefill_074(rfl_base_universe_d2_069_rfl_basefill_074):
    return _base_universe_d3(rfl_base_universe_d2_069_rfl_basefill_074, 69)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_069_rfl_basefill_074'] = {'inputs': ['rfl_base_universe_d2_069_rfl_basefill_074'], 'func': rfl_base_universe_d3_069_rfl_basefill_074}


def rfl_base_universe_d3_070_rfl_basefill_075(rfl_base_universe_d2_070_rfl_basefill_075):
    return _base_universe_d3(rfl_base_universe_d2_070_rfl_basefill_075, 70)
RFL_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rfl_base_universe_d3_070_rfl_basefill_075'] = {'inputs': ['rfl_base_universe_d2_070_rfl_basefill_075'], 'func': rfl_base_universe_d3_070_rfl_basefill_075}
