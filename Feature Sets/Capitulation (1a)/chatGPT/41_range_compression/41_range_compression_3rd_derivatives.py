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



def rcp_001_realized_vol_z_accel_1(rcp_001_realized_vol_z_roc_1):
    feature = _s(rcp_001_realized_vol_z_roc_1)
    return (_roc(feature, 1).diff(1)).reindex(feature.index)

def rcp_007_realized_vol_z_accel_5(rcp_007_realized_vol_z_roc_5):
    feature = _s(rcp_007_realized_vol_z_roc_5)
    return (_roc(feature, 5).diff(1)).reindex(feature.index)

def rcp_013_realized_vol_z_accel_42(rcp_013_realized_vol_z_roc_42):
    feature = _s(rcp_013_realized_vol_z_roc_42)
    return (_roc(feature, 42).diff(8)).reindex(feature.index)

def rcp_179_rcp_019_realized_vol_z_42_019_accel_126(rcp_154_rcp_019_realized_vol_z_42_019_roc_126):
    feature = _s(rcp_154_rcp_019_realized_vol_z_42_019_roc_126)
    return (_roc(feature, 126).diff(25)).reindex(feature.index)

def rcp_180_rcp_025_realized_vol_z_378_025_accel_378(rcp_155_rcp_025_realized_vol_z_378_025_roc_378):
    feature = _s(rcp_155_rcp_025_realized_vol_z_378_025_roc_378)
    return (_roc(feature, 378).diff(75)).reindex(feature.index)






















RANGE_COMPRESSION_REGISTRY_3RD_DERIVATIVES = {
    'rcp_001_realized_vol_z_accel_1': {'inputs': ['rcp_001_realized_vol_z_roc_1'], 'func': rcp_001_realized_vol_z_accel_1},
    'rcp_007_realized_vol_z_accel_5': {'inputs': ['rcp_007_realized_vol_z_roc_5'], 'func': rcp_007_realized_vol_z_accel_5},
    'rcp_013_realized_vol_z_accel_42': {'inputs': ['rcp_013_realized_vol_z_roc_42'], 'func': rcp_013_realized_vol_z_accel_42},
    'rcp_179_rcp_019_realized_vol_z_42_019_accel_126': {'inputs': ['rcp_154_rcp_019_realized_vol_z_42_019_roc_126'], 'func': rcp_179_rcp_019_realized_vol_z_42_019_accel_126},
    'rcp_180_rcp_025_realized_vol_z_378_025_accel_378': {'inputs': ['rcp_155_rcp_025_realized_vol_z_378_025_roc_378'], 'func': rcp_180_rcp_025_realized_vol_z_378_025_accel_378},
}


# Replacement 3rd-derivative features restored after redundancy audit.

import numpy as np
import pandas as pd


def _s(x):
    return pd.Series(x).astype(float)


def _clean(x):
    return _s(x).replace([np.inf, -np.inf], np.nan)


RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY = {}


def rc_replacement_d3_001(rc_replacement_d2_001):
    feature = _clean(rc_replacement_d2_001)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00000500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_001'] = {'inputs': ['rc_replacement_d2_001'], 'func': rc_replacement_d3_001}


def rc_replacement_d3_002(rc_replacement_d2_002):
    feature = _clean(rc_replacement_d2_002)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_002'] = {'inputs': ['rc_replacement_d2_002'], 'func': rc_replacement_d3_002}


def rc_replacement_d3_003(rc_replacement_d2_003):
    feature = _clean(rc_replacement_d2_003)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00001500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_003'] = {'inputs': ['rc_replacement_d2_003'], 'func': rc_replacement_d3_003}


def rc_replacement_d3_004(rc_replacement_d2_004):
    feature = _clean(rc_replacement_d2_004)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_004'] = {'inputs': ['rc_replacement_d2_004'], 'func': rc_replacement_d3_004}


def rc_replacement_d3_005(rc_replacement_d2_005):
    feature = _clean(rc_replacement_d2_005)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00002500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_005'] = {'inputs': ['rc_replacement_d2_005'], 'func': rc_replacement_d3_005}


def rc_replacement_d3_006(rc_replacement_d2_006):
    feature = _clean(rc_replacement_d2_006)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_006'] = {'inputs': ['rc_replacement_d2_006'], 'func': rc_replacement_d3_006}


def rc_replacement_d3_007(rc_replacement_d2_007):
    feature = _clean(rc_replacement_d2_007)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00003500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_007'] = {'inputs': ['rc_replacement_d2_007'], 'func': rc_replacement_d3_007}


def rc_replacement_d3_008(rc_replacement_d2_008):
    feature = _clean(rc_replacement_d2_008)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_008'] = {'inputs': ['rc_replacement_d2_008'], 'func': rc_replacement_d3_008}


def rc_replacement_d3_009(rc_replacement_d2_009):
    feature = _clean(rc_replacement_d2_009)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00004500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_009'] = {'inputs': ['rc_replacement_d2_009'], 'func': rc_replacement_d3_009}


def rc_replacement_d3_010(rc_replacement_d2_010):
    feature = _clean(rc_replacement_d2_010)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_010'] = {'inputs': ['rc_replacement_d2_010'], 'func': rc_replacement_d3_010}


def rc_replacement_d3_011(rc_replacement_d2_011):
    feature = _clean(rc_replacement_d2_011)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00005500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_011'] = {'inputs': ['rc_replacement_d2_011'], 'func': rc_replacement_d3_011}


def rc_replacement_d3_012(rc_replacement_d2_012):
    feature = _clean(rc_replacement_d2_012)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_012'] = {'inputs': ['rc_replacement_d2_012'], 'func': rc_replacement_d3_012}


def rc_replacement_d3_013(rc_replacement_d2_013):
    feature = _clean(rc_replacement_d2_013)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00006500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_013'] = {'inputs': ['rc_replacement_d2_013'], 'func': rc_replacement_d3_013}


def rc_replacement_d3_014(rc_replacement_d2_014):
    feature = _clean(rc_replacement_d2_014)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_014'] = {'inputs': ['rc_replacement_d2_014'], 'func': rc_replacement_d3_014}


def rc_replacement_d3_015(rc_replacement_d2_015):
    feature = _clean(rc_replacement_d2_015)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00007500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_015'] = {'inputs': ['rc_replacement_d2_015'], 'func': rc_replacement_d3_015}


def rc_replacement_d3_016(rc_replacement_d2_016):
    feature = _clean(rc_replacement_d2_016)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_016'] = {'inputs': ['rc_replacement_d2_016'], 'func': rc_replacement_d3_016}


def rc_replacement_d3_017(rc_replacement_d2_017):
    feature = _clean(rc_replacement_d2_017)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00008500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_017'] = {'inputs': ['rc_replacement_d2_017'], 'func': rc_replacement_d3_017}


def rc_replacement_d3_018(rc_replacement_d2_018):
    feature = _clean(rc_replacement_d2_018)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_018'] = {'inputs': ['rc_replacement_d2_018'], 'func': rc_replacement_d3_018}


def rc_replacement_d3_019(rc_replacement_d2_019):
    feature = _clean(rc_replacement_d2_019)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00009500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_019'] = {'inputs': ['rc_replacement_d2_019'], 'func': rc_replacement_d3_019}


def rc_replacement_d3_020(rc_replacement_d2_020):
    feature = _clean(rc_replacement_d2_020)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_020'] = {'inputs': ['rc_replacement_d2_020'], 'func': rc_replacement_d3_020}


def rc_replacement_d3_021(rc_replacement_d2_021):
    feature = _clean(rc_replacement_d2_021)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00010500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_021'] = {'inputs': ['rc_replacement_d2_021'], 'func': rc_replacement_d3_021}


def rc_replacement_d3_022(rc_replacement_d2_022):
    feature = _clean(rc_replacement_d2_022)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_022'] = {'inputs': ['rc_replacement_d2_022'], 'func': rc_replacement_d3_022}


def rc_replacement_d3_023(rc_replacement_d2_023):
    feature = _clean(rc_replacement_d2_023)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00011500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_023'] = {'inputs': ['rc_replacement_d2_023'], 'func': rc_replacement_d3_023}


def rc_replacement_d3_024(rc_replacement_d2_024):
    feature = _clean(rc_replacement_d2_024)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_024'] = {'inputs': ['rc_replacement_d2_024'], 'func': rc_replacement_d3_024}


def rc_replacement_d3_025(rc_replacement_d2_025):
    feature = _clean(rc_replacement_d2_025)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00012500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_025'] = {'inputs': ['rc_replacement_d2_025'], 'func': rc_replacement_d3_025}


def rc_replacement_d3_026(rc_replacement_d2_026):
    feature = _clean(rc_replacement_d2_026)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_026'] = {'inputs': ['rc_replacement_d2_026'], 'func': rc_replacement_d3_026}


def rc_replacement_d3_027(rc_replacement_d2_027):
    feature = _clean(rc_replacement_d2_027)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00013500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_027'] = {'inputs': ['rc_replacement_d2_027'], 'func': rc_replacement_d3_027}


def rc_replacement_d3_028(rc_replacement_d2_028):
    feature = _clean(rc_replacement_d2_028)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_028'] = {'inputs': ['rc_replacement_d2_028'], 'func': rc_replacement_d3_028}


def rc_replacement_d3_029(rc_replacement_d2_029):
    feature = _clean(rc_replacement_d2_029)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00014500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_029'] = {'inputs': ['rc_replacement_d2_029'], 'func': rc_replacement_d3_029}


def rc_replacement_d3_030(rc_replacement_d2_030):
    feature = _clean(rc_replacement_d2_030)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_030'] = {'inputs': ['rc_replacement_d2_030'], 'func': rc_replacement_d3_030}


def rc_replacement_d3_031(rc_replacement_d2_031):
    feature = _clean(rc_replacement_d2_031)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00015500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_031'] = {'inputs': ['rc_replacement_d2_031'], 'func': rc_replacement_d3_031}


def rc_replacement_d3_032(rc_replacement_d2_032):
    feature = _clean(rc_replacement_d2_032)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_032'] = {'inputs': ['rc_replacement_d2_032'], 'func': rc_replacement_d3_032}


def rc_replacement_d3_033(rc_replacement_d2_033):
    feature = _clean(rc_replacement_d2_033)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00016500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_033'] = {'inputs': ['rc_replacement_d2_033'], 'func': rc_replacement_d3_033}


def rc_replacement_d3_034(rc_replacement_d2_034):
    feature = _clean(rc_replacement_d2_034)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_034'] = {'inputs': ['rc_replacement_d2_034'], 'func': rc_replacement_d3_034}


def rc_replacement_d3_035(rc_replacement_d2_035):
    feature = _clean(rc_replacement_d2_035)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00017500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_035'] = {'inputs': ['rc_replacement_d2_035'], 'func': rc_replacement_d3_035}


def rc_replacement_d3_036(rc_replacement_d2_036):
    feature = _clean(rc_replacement_d2_036)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_036'] = {'inputs': ['rc_replacement_d2_036'], 'func': rc_replacement_d3_036}


def rc_replacement_d3_037(rc_replacement_d2_037):
    feature = _clean(rc_replacement_d2_037)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00018500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_037'] = {'inputs': ['rc_replacement_d2_037'], 'func': rc_replacement_d3_037}


def rc_replacement_d3_038(rc_replacement_d2_038):
    feature = _clean(rc_replacement_d2_038)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_038'] = {'inputs': ['rc_replacement_d2_038'], 'func': rc_replacement_d3_038}


def rc_replacement_d3_039(rc_replacement_d2_039):
    feature = _clean(rc_replacement_d2_039)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00019500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_039'] = {'inputs': ['rc_replacement_d2_039'], 'func': rc_replacement_d3_039}


def rc_replacement_d3_040(rc_replacement_d2_040):
    feature = _clean(rc_replacement_d2_040)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_040'] = {'inputs': ['rc_replacement_d2_040'], 'func': rc_replacement_d3_040}


def rc_replacement_d3_041(rc_replacement_d2_041):
    feature = _clean(rc_replacement_d2_041)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00020500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_041'] = {'inputs': ['rc_replacement_d2_041'], 'func': rc_replacement_d3_041}


def rc_replacement_d3_042(rc_replacement_d2_042):
    feature = _clean(rc_replacement_d2_042)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_042'] = {'inputs': ['rc_replacement_d2_042'], 'func': rc_replacement_d3_042}


def rc_replacement_d3_043(rc_replacement_d2_043):
    feature = _clean(rc_replacement_d2_043)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00021500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_043'] = {'inputs': ['rc_replacement_d2_043'], 'func': rc_replacement_d3_043}


def rc_replacement_d3_044(rc_replacement_d2_044):
    feature = _clean(rc_replacement_d2_044)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_044'] = {'inputs': ['rc_replacement_d2_044'], 'func': rc_replacement_d3_044}


def rc_replacement_d3_045(rc_replacement_d2_045):
    feature = _clean(rc_replacement_d2_045)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00022500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_045'] = {'inputs': ['rc_replacement_d2_045'], 'func': rc_replacement_d3_045}


def rc_replacement_d3_046(rc_replacement_d2_046):
    feature = _clean(rc_replacement_d2_046)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_046'] = {'inputs': ['rc_replacement_d2_046'], 'func': rc_replacement_d3_046}


def rc_replacement_d3_047(rc_replacement_d2_047):
    feature = _clean(rc_replacement_d2_047)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00023500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_047'] = {'inputs': ['rc_replacement_d2_047'], 'func': rc_replacement_d3_047}


def rc_replacement_d3_048(rc_replacement_d2_048):
    feature = _clean(rc_replacement_d2_048)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_048'] = {'inputs': ['rc_replacement_d2_048'], 'func': rc_replacement_d3_048}


def rc_replacement_d3_049(rc_replacement_d2_049):
    feature = _clean(rc_replacement_d2_049)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00024500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_049'] = {'inputs': ['rc_replacement_d2_049'], 'func': rc_replacement_d3_049}


def rc_replacement_d3_050(rc_replacement_d2_050):
    feature = _clean(rc_replacement_d2_050)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_050'] = {'inputs': ['rc_replacement_d2_050'], 'func': rc_replacement_d3_050}


def rc_replacement_d3_051(rc_replacement_d2_051):
    feature = _clean(rc_replacement_d2_051)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00025500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_051'] = {'inputs': ['rc_replacement_d2_051'], 'func': rc_replacement_d3_051}


def rc_replacement_d3_052(rc_replacement_d2_052):
    feature = _clean(rc_replacement_d2_052)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_052'] = {'inputs': ['rc_replacement_d2_052'], 'func': rc_replacement_d3_052}


def rc_replacement_d3_053(rc_replacement_d2_053):
    feature = _clean(rc_replacement_d2_053)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00026500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_053'] = {'inputs': ['rc_replacement_d2_053'], 'func': rc_replacement_d3_053}


def rc_replacement_d3_054(rc_replacement_d2_054):
    feature = _clean(rc_replacement_d2_054)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_054'] = {'inputs': ['rc_replacement_d2_054'], 'func': rc_replacement_d3_054}


def rc_replacement_d3_055(rc_replacement_d2_055):
    feature = _clean(rc_replacement_d2_055)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00027500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_055'] = {'inputs': ['rc_replacement_d2_055'], 'func': rc_replacement_d3_055}


def rc_replacement_d3_056(rc_replacement_d2_056):
    feature = _clean(rc_replacement_d2_056)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_056'] = {'inputs': ['rc_replacement_d2_056'], 'func': rc_replacement_d3_056}


def rc_replacement_d3_057(rc_replacement_d2_057):
    feature = _clean(rc_replacement_d2_057)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00028500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_057'] = {'inputs': ['rc_replacement_d2_057'], 'func': rc_replacement_d3_057}


def rc_replacement_d3_058(rc_replacement_d2_058):
    feature = _clean(rc_replacement_d2_058)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_058'] = {'inputs': ['rc_replacement_d2_058'], 'func': rc_replacement_d3_058}


def rc_replacement_d3_059(rc_replacement_d2_059):
    feature = _clean(rc_replacement_d2_059)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00029500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_059'] = {'inputs': ['rc_replacement_d2_059'], 'func': rc_replacement_d3_059}


def rc_replacement_d3_060(rc_replacement_d2_060):
    feature = _clean(rc_replacement_d2_060)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_060'] = {'inputs': ['rc_replacement_d2_060'], 'func': rc_replacement_d3_060}


def rc_replacement_d3_061(rc_replacement_d2_061):
    feature = _clean(rc_replacement_d2_061)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00030500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_061'] = {'inputs': ['rc_replacement_d2_061'], 'func': rc_replacement_d3_061}


def rc_replacement_d3_062(rc_replacement_d2_062):
    feature = _clean(rc_replacement_d2_062)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_062'] = {'inputs': ['rc_replacement_d2_062'], 'func': rc_replacement_d3_062}


def rc_replacement_d3_063(rc_replacement_d2_063):
    feature = _clean(rc_replacement_d2_063)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00031500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_063'] = {'inputs': ['rc_replacement_d2_063'], 'func': rc_replacement_d3_063}


def rc_replacement_d3_064(rc_replacement_d2_064):
    feature = _clean(rc_replacement_d2_064)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_064'] = {'inputs': ['rc_replacement_d2_064'], 'func': rc_replacement_d3_064}


def rc_replacement_d3_065(rc_replacement_d2_065):
    feature = _clean(rc_replacement_d2_065)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00032500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_065'] = {'inputs': ['rc_replacement_d2_065'], 'func': rc_replacement_d3_065}


def rc_replacement_d3_066(rc_replacement_d2_066):
    feature = _clean(rc_replacement_d2_066)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_066'] = {'inputs': ['rc_replacement_d2_066'], 'func': rc_replacement_d3_066}


def rc_replacement_d3_067(rc_replacement_d2_067):
    feature = _clean(rc_replacement_d2_067)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00033500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_067'] = {'inputs': ['rc_replacement_d2_067'], 'func': rc_replacement_d3_067}


def rc_replacement_d3_068(rc_replacement_d2_068):
    feature = _clean(rc_replacement_d2_068)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_068'] = {'inputs': ['rc_replacement_d2_068'], 'func': rc_replacement_d3_068}


def rc_replacement_d3_069(rc_replacement_d2_069):
    feature = _clean(rc_replacement_d2_069)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00034500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_069'] = {'inputs': ['rc_replacement_d2_069'], 'func': rc_replacement_d3_069}


def rc_replacement_d3_070(rc_replacement_d2_070):
    feature = _clean(rc_replacement_d2_070)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_070'] = {'inputs': ['rc_replacement_d2_070'], 'func': rc_replacement_d3_070}


def rc_replacement_d3_071(rc_replacement_d2_071):
    feature = _clean(rc_replacement_d2_071)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00035500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_071'] = {'inputs': ['rc_replacement_d2_071'], 'func': rc_replacement_d3_071}


def rc_replacement_d3_072(rc_replacement_d2_072):
    feature = _clean(rc_replacement_d2_072)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_072'] = {'inputs': ['rc_replacement_d2_072'], 'func': rc_replacement_d3_072}


def rc_replacement_d3_073(rc_replacement_d2_073):
    feature = _clean(rc_replacement_d2_073)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00036500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_073'] = {'inputs': ['rc_replacement_d2_073'], 'func': rc_replacement_d3_073}


def rc_replacement_d3_074(rc_replacement_d2_074):
    feature = _clean(rc_replacement_d2_074)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_074'] = {'inputs': ['rc_replacement_d2_074'], 'func': rc_replacement_d3_074}


def rc_replacement_d3_075(rc_replacement_d2_075):
    feature = _clean(rc_replacement_d2_075)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00037500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_075'] = {'inputs': ['rc_replacement_d2_075'], 'func': rc_replacement_d3_075}


def rc_replacement_d3_076(rc_replacement_d2_076):
    feature = _clean(rc_replacement_d2_076)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_076'] = {'inputs': ['rc_replacement_d2_076'], 'func': rc_replacement_d3_076}


def rc_replacement_d3_077(rc_replacement_d2_077):
    feature = _clean(rc_replacement_d2_077)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00038500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_077'] = {'inputs': ['rc_replacement_d2_077'], 'func': rc_replacement_d3_077}


def rc_replacement_d3_078(rc_replacement_d2_078):
    feature = _clean(rc_replacement_d2_078)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_078'] = {'inputs': ['rc_replacement_d2_078'], 'func': rc_replacement_d3_078}


def rc_replacement_d3_079(rc_replacement_d2_079):
    feature = _clean(rc_replacement_d2_079)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00039500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_079'] = {'inputs': ['rc_replacement_d2_079'], 'func': rc_replacement_d3_079}


def rc_replacement_d3_080(rc_replacement_d2_080):
    feature = _clean(rc_replacement_d2_080)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_080'] = {'inputs': ['rc_replacement_d2_080'], 'func': rc_replacement_d3_080}


def rc_replacement_d3_081(rc_replacement_d2_081):
    feature = _clean(rc_replacement_d2_081)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00040500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_081'] = {'inputs': ['rc_replacement_d2_081'], 'func': rc_replacement_d3_081}


def rc_replacement_d3_082(rc_replacement_d2_082):
    feature = _clean(rc_replacement_d2_082)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_082'] = {'inputs': ['rc_replacement_d2_082'], 'func': rc_replacement_d3_082}


def rc_replacement_d3_083(rc_replacement_d2_083):
    feature = _clean(rc_replacement_d2_083)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00041500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_083'] = {'inputs': ['rc_replacement_d2_083'], 'func': rc_replacement_d3_083}


def rc_replacement_d3_084(rc_replacement_d2_084):
    feature = _clean(rc_replacement_d2_084)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_084'] = {'inputs': ['rc_replacement_d2_084'], 'func': rc_replacement_d3_084}


def rc_replacement_d3_085(rc_replacement_d2_085):
    feature = _clean(rc_replacement_d2_085)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00042500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_085'] = {'inputs': ['rc_replacement_d2_085'], 'func': rc_replacement_d3_085}


def rc_replacement_d3_086(rc_replacement_d2_086):
    feature = _clean(rc_replacement_d2_086)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_086'] = {'inputs': ['rc_replacement_d2_086'], 'func': rc_replacement_d3_086}


def rc_replacement_d3_087(rc_replacement_d2_087):
    feature = _clean(rc_replacement_d2_087)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00043500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_087'] = {'inputs': ['rc_replacement_d2_087'], 'func': rc_replacement_d3_087}


def rc_replacement_d3_088(rc_replacement_d2_088):
    feature = _clean(rc_replacement_d2_088)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_088'] = {'inputs': ['rc_replacement_d2_088'], 'func': rc_replacement_d3_088}


def rc_replacement_d3_089(rc_replacement_d2_089):
    feature = _clean(rc_replacement_d2_089)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00044500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_089'] = {'inputs': ['rc_replacement_d2_089'], 'func': rc_replacement_d3_089}


def rc_replacement_d3_090(rc_replacement_d2_090):
    feature = _clean(rc_replacement_d2_090)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_090'] = {'inputs': ['rc_replacement_d2_090'], 'func': rc_replacement_d3_090}


def rc_replacement_d3_091(rc_replacement_d2_091):
    feature = _clean(rc_replacement_d2_091)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00045500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_091'] = {'inputs': ['rc_replacement_d2_091'], 'func': rc_replacement_d3_091}


def rc_replacement_d3_092(rc_replacement_d2_092):
    feature = _clean(rc_replacement_d2_092)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_092'] = {'inputs': ['rc_replacement_d2_092'], 'func': rc_replacement_d3_092}


def rc_replacement_d3_093(rc_replacement_d2_093):
    feature = _clean(rc_replacement_d2_093)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00046500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_093'] = {'inputs': ['rc_replacement_d2_093'], 'func': rc_replacement_d3_093}


def rc_replacement_d3_094(rc_replacement_d2_094):
    feature = _clean(rc_replacement_d2_094)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_094'] = {'inputs': ['rc_replacement_d2_094'], 'func': rc_replacement_d3_094}


def rc_replacement_d3_095(rc_replacement_d2_095):
    feature = _clean(rc_replacement_d2_095)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00047500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_095'] = {'inputs': ['rc_replacement_d2_095'], 'func': rc_replacement_d3_095}


def rc_replacement_d3_096(rc_replacement_d2_096):
    feature = _clean(rc_replacement_d2_096)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_096'] = {'inputs': ['rc_replacement_d2_096'], 'func': rc_replacement_d3_096}


def rc_replacement_d3_097(rc_replacement_d2_097):
    feature = _clean(rc_replacement_d2_097)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00048500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_097'] = {'inputs': ['rc_replacement_d2_097'], 'func': rc_replacement_d3_097}


def rc_replacement_d3_098(rc_replacement_d2_098):
    feature = _clean(rc_replacement_d2_098)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_098'] = {'inputs': ['rc_replacement_d2_098'], 'func': rc_replacement_d3_098}


def rc_replacement_d3_099(rc_replacement_d2_099):
    feature = _clean(rc_replacement_d2_099)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00049500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_099'] = {'inputs': ['rc_replacement_d2_099'], 'func': rc_replacement_d3_099}


def rc_replacement_d3_100(rc_replacement_d2_100):
    feature = _clean(rc_replacement_d2_100)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_100'] = {'inputs': ['rc_replacement_d2_100'], 'func': rc_replacement_d3_100}


def rc_replacement_d3_101(rc_replacement_d2_101):
    feature = _clean(rc_replacement_d2_101)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00050500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_101'] = {'inputs': ['rc_replacement_d2_101'], 'func': rc_replacement_d3_101}


def rc_replacement_d3_102(rc_replacement_d2_102):
    feature = _clean(rc_replacement_d2_102)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_102'] = {'inputs': ['rc_replacement_d2_102'], 'func': rc_replacement_d3_102}


def rc_replacement_d3_103(rc_replacement_d2_103):
    feature = _clean(rc_replacement_d2_103)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00051500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_103'] = {'inputs': ['rc_replacement_d2_103'], 'func': rc_replacement_d3_103}


def rc_replacement_d3_104(rc_replacement_d2_104):
    feature = _clean(rc_replacement_d2_104)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_104'] = {'inputs': ['rc_replacement_d2_104'], 'func': rc_replacement_d3_104}


def rc_replacement_d3_105(rc_replacement_d2_105):
    feature = _clean(rc_replacement_d2_105)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00052500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_105'] = {'inputs': ['rc_replacement_d2_105'], 'func': rc_replacement_d3_105}


def rc_replacement_d3_106(rc_replacement_d2_106):
    feature = _clean(rc_replacement_d2_106)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_106'] = {'inputs': ['rc_replacement_d2_106'], 'func': rc_replacement_d3_106}


def rc_replacement_d3_107(rc_replacement_d2_107):
    feature = _clean(rc_replacement_d2_107)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00053500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_107'] = {'inputs': ['rc_replacement_d2_107'], 'func': rc_replacement_d3_107}


def rc_replacement_d3_108(rc_replacement_d2_108):
    feature = _clean(rc_replacement_d2_108)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_108'] = {'inputs': ['rc_replacement_d2_108'], 'func': rc_replacement_d3_108}


def rc_replacement_d3_109(rc_replacement_d2_109):
    feature = _clean(rc_replacement_d2_109)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00054500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_109'] = {'inputs': ['rc_replacement_d2_109'], 'func': rc_replacement_d3_109}


def rc_replacement_d3_110(rc_replacement_d2_110):
    feature = _clean(rc_replacement_d2_110)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_110'] = {'inputs': ['rc_replacement_d2_110'], 'func': rc_replacement_d3_110}


def rc_replacement_d3_111(rc_replacement_d2_111):
    feature = _clean(rc_replacement_d2_111)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00055500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_111'] = {'inputs': ['rc_replacement_d2_111'], 'func': rc_replacement_d3_111}


def rc_replacement_d3_112(rc_replacement_d2_112):
    feature = _clean(rc_replacement_d2_112)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_112'] = {'inputs': ['rc_replacement_d2_112'], 'func': rc_replacement_d3_112}


def rc_replacement_d3_113(rc_replacement_d2_113):
    feature = _clean(rc_replacement_d2_113)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00056500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_113'] = {'inputs': ['rc_replacement_d2_113'], 'func': rc_replacement_d3_113}


def rc_replacement_d3_114(rc_replacement_d2_114):
    feature = _clean(rc_replacement_d2_114)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_114'] = {'inputs': ['rc_replacement_d2_114'], 'func': rc_replacement_d3_114}


def rc_replacement_d3_115(rc_replacement_d2_115):
    feature = _clean(rc_replacement_d2_115)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00057500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_115'] = {'inputs': ['rc_replacement_d2_115'], 'func': rc_replacement_d3_115}


def rc_replacement_d3_116(rc_replacement_d2_116):
    feature = _clean(rc_replacement_d2_116)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_116'] = {'inputs': ['rc_replacement_d2_116'], 'func': rc_replacement_d3_116}


def rc_replacement_d3_117(rc_replacement_d2_117):
    feature = _clean(rc_replacement_d2_117)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00058500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_117'] = {'inputs': ['rc_replacement_d2_117'], 'func': rc_replacement_d3_117}


def rc_replacement_d3_118(rc_replacement_d2_118):
    feature = _clean(rc_replacement_d2_118)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_118'] = {'inputs': ['rc_replacement_d2_118'], 'func': rc_replacement_d3_118}


def rc_replacement_d3_119(rc_replacement_d2_119):
    feature = _clean(rc_replacement_d2_119)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00059500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_119'] = {'inputs': ['rc_replacement_d2_119'], 'func': rc_replacement_d3_119}


def rc_replacement_d3_120(rc_replacement_d2_120):
    feature = _clean(rc_replacement_d2_120)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_120'] = {'inputs': ['rc_replacement_d2_120'], 'func': rc_replacement_d3_120}


def rc_replacement_d3_121(rc_replacement_d2_121):
    feature = _clean(rc_replacement_d2_121)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00060500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_121'] = {'inputs': ['rc_replacement_d2_121'], 'func': rc_replacement_d3_121}


def rc_replacement_d3_122(rc_replacement_d2_122):
    feature = _clean(rc_replacement_d2_122)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_122'] = {'inputs': ['rc_replacement_d2_122'], 'func': rc_replacement_d3_122}


def rc_replacement_d3_123(rc_replacement_d2_123):
    feature = _clean(rc_replacement_d2_123)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00061500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_123'] = {'inputs': ['rc_replacement_d2_123'], 'func': rc_replacement_d3_123}


def rc_replacement_d3_124(rc_replacement_d2_124):
    feature = _clean(rc_replacement_d2_124)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_124'] = {'inputs': ['rc_replacement_d2_124'], 'func': rc_replacement_d3_124}


def rc_replacement_d3_125(rc_replacement_d2_125):
    feature = _clean(rc_replacement_d2_125)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00062500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_125'] = {'inputs': ['rc_replacement_d2_125'], 'func': rc_replacement_d3_125}


def rc_replacement_d3_126(rc_replacement_d2_126):
    feature = _clean(rc_replacement_d2_126)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_126'] = {'inputs': ['rc_replacement_d2_126'], 'func': rc_replacement_d3_126}


def rc_replacement_d3_127(rc_replacement_d2_127):
    feature = _clean(rc_replacement_d2_127)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00063500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_127'] = {'inputs': ['rc_replacement_d2_127'], 'func': rc_replacement_d3_127}


def rc_replacement_d3_128(rc_replacement_d2_128):
    feature = _clean(rc_replacement_d2_128)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_128'] = {'inputs': ['rc_replacement_d2_128'], 'func': rc_replacement_d3_128}


def rc_replacement_d3_129(rc_replacement_d2_129):
    feature = _clean(rc_replacement_d2_129)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00064500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_129'] = {'inputs': ['rc_replacement_d2_129'], 'func': rc_replacement_d3_129}


def rc_replacement_d3_130(rc_replacement_d2_130):
    feature = _clean(rc_replacement_d2_130)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_130'] = {'inputs': ['rc_replacement_d2_130'], 'func': rc_replacement_d3_130}


def rc_replacement_d3_131(rc_replacement_d2_131):
    feature = _clean(rc_replacement_d2_131)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00065500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_131'] = {'inputs': ['rc_replacement_d2_131'], 'func': rc_replacement_d3_131}


def rc_replacement_d3_132(rc_replacement_d2_132):
    feature = _clean(rc_replacement_d2_132)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_132'] = {'inputs': ['rc_replacement_d2_132'], 'func': rc_replacement_d3_132}


def rc_replacement_d3_133(rc_replacement_d2_133):
    feature = _clean(rc_replacement_d2_133)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00066500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_133'] = {'inputs': ['rc_replacement_d2_133'], 'func': rc_replacement_d3_133}


def rc_replacement_d3_134(rc_replacement_d2_134):
    feature = _clean(rc_replacement_d2_134)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_134'] = {'inputs': ['rc_replacement_d2_134'], 'func': rc_replacement_d3_134}


def rc_replacement_d3_135(rc_replacement_d2_135):
    feature = _clean(rc_replacement_d2_135)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00067500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_135'] = {'inputs': ['rc_replacement_d2_135'], 'func': rc_replacement_d3_135}


def rc_replacement_d3_136(rc_replacement_d2_136):
    feature = _clean(rc_replacement_d2_136)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_136'] = {'inputs': ['rc_replacement_d2_136'], 'func': rc_replacement_d3_136}


def rc_replacement_d3_137(rc_replacement_d2_137):
    feature = _clean(rc_replacement_d2_137)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00068500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_137'] = {'inputs': ['rc_replacement_d2_137'], 'func': rc_replacement_d3_137}


def rc_replacement_d3_138(rc_replacement_d2_138):
    feature = _clean(rc_replacement_d2_138)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_138'] = {'inputs': ['rc_replacement_d2_138'], 'func': rc_replacement_d3_138}


def rc_replacement_d3_139(rc_replacement_d2_139):
    feature = _clean(rc_replacement_d2_139)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00069500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_139'] = {'inputs': ['rc_replacement_d2_139'], 'func': rc_replacement_d3_139}


def rc_replacement_d3_140(rc_replacement_d2_140):
    feature = _clean(rc_replacement_d2_140)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_140'] = {'inputs': ['rc_replacement_d2_140'], 'func': rc_replacement_d3_140}


def rc_replacement_d3_141(rc_replacement_d2_141):
    feature = _clean(rc_replacement_d2_141)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00070500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_141'] = {'inputs': ['rc_replacement_d2_141'], 'func': rc_replacement_d3_141}


def rc_replacement_d3_142(rc_replacement_d2_142):
    feature = _clean(rc_replacement_d2_142)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_142'] = {'inputs': ['rc_replacement_d2_142'], 'func': rc_replacement_d3_142}


def rc_replacement_d3_143(rc_replacement_d2_143):
    feature = _clean(rc_replacement_d2_143)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00071500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_143'] = {'inputs': ['rc_replacement_d2_143'], 'func': rc_replacement_d3_143}


def rc_replacement_d3_144(rc_replacement_d2_144):
    feature = _clean(rc_replacement_d2_144)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_144'] = {'inputs': ['rc_replacement_d2_144'], 'func': rc_replacement_d3_144}


def rc_replacement_d3_145(rc_replacement_d2_145):
    feature = _clean(rc_replacement_d2_145)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00072500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_145'] = {'inputs': ['rc_replacement_d2_145'], 'func': rc_replacement_d3_145}


def rc_replacement_d3_146(rc_replacement_d2_146):
    feature = _clean(rc_replacement_d2_146)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_146'] = {'inputs': ['rc_replacement_d2_146'], 'func': rc_replacement_d3_146}


def rc_replacement_d3_147(rc_replacement_d2_147):
    feature = _clean(rc_replacement_d2_147)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00073500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_147'] = {'inputs': ['rc_replacement_d2_147'], 'func': rc_replacement_d3_147}


def rc_replacement_d3_148(rc_replacement_d2_148):
    feature = _clean(rc_replacement_d2_148)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_148'] = {'inputs': ['rc_replacement_d2_148'], 'func': rc_replacement_d3_148}


def rc_replacement_d3_149(rc_replacement_d2_149):
    feature = _clean(rc_replacement_d2_149)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00074500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_149'] = {'inputs': ['rc_replacement_d2_149'], 'func': rc_replacement_d3_149}


def rc_replacement_d3_150(rc_replacement_d2_150):
    feature = _clean(rc_replacement_d2_150)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_150'] = {'inputs': ['rc_replacement_d2_150'], 'func': rc_replacement_d3_150}


def rc_replacement_d3_151(rc_replacement_d2_151):
    feature = _clean(rc_replacement_d2_151)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00075500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_151'] = {'inputs': ['rc_replacement_d2_151'], 'func': rc_replacement_d3_151}


def rc_replacement_d3_152(rc_replacement_d2_152):
    feature = _clean(rc_replacement_d2_152)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_152'] = {'inputs': ['rc_replacement_d2_152'], 'func': rc_replacement_d3_152}


def rc_replacement_d3_153(rc_replacement_d2_153):
    feature = _clean(rc_replacement_d2_153)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00076500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_153'] = {'inputs': ['rc_replacement_d2_153'], 'func': rc_replacement_d3_153}


def rc_replacement_d3_154(rc_replacement_d2_154):
    feature = _clean(rc_replacement_d2_154)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_154'] = {'inputs': ['rc_replacement_d2_154'], 'func': rc_replacement_d3_154}


def rc_replacement_d3_155(rc_replacement_d2_155):
    feature = _clean(rc_replacement_d2_155)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00077500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_155'] = {'inputs': ['rc_replacement_d2_155'], 'func': rc_replacement_d3_155}


def rc_replacement_d3_156(rc_replacement_d2_156):
    feature = _clean(rc_replacement_d2_156)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_156'] = {'inputs': ['rc_replacement_d2_156'], 'func': rc_replacement_d3_156}


def rc_replacement_d3_157(rc_replacement_d2_157):
    feature = _clean(rc_replacement_d2_157)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00078500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_157'] = {'inputs': ['rc_replacement_d2_157'], 'func': rc_replacement_d3_157}


def rc_replacement_d3_158(rc_replacement_d2_158):
    feature = _clean(rc_replacement_d2_158)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_158'] = {'inputs': ['rc_replacement_d2_158'], 'func': rc_replacement_d3_158}


def rc_replacement_d3_159(rc_replacement_d2_159):
    feature = _clean(rc_replacement_d2_159)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00079500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_159'] = {'inputs': ['rc_replacement_d2_159'], 'func': rc_replacement_d3_159}


def rc_replacement_d3_160(rc_replacement_d2_160):
    feature = _clean(rc_replacement_d2_160)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_160'] = {'inputs': ['rc_replacement_d2_160'], 'func': rc_replacement_d3_160}


def rc_replacement_d3_161(rc_replacement_d2_161):
    feature = _clean(rc_replacement_d2_161)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00080500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_161'] = {'inputs': ['rc_replacement_d2_161'], 'func': rc_replacement_d3_161}


def rc_replacement_d3_162(rc_replacement_d2_162):
    feature = _clean(rc_replacement_d2_162)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_162'] = {'inputs': ['rc_replacement_d2_162'], 'func': rc_replacement_d3_162}


def rc_replacement_d3_163(rc_replacement_d2_163):
    feature = _clean(rc_replacement_d2_163)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00081500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_163'] = {'inputs': ['rc_replacement_d2_163'], 'func': rc_replacement_d3_163}


def rc_replacement_d3_164(rc_replacement_d2_164):
    feature = _clean(rc_replacement_d2_164)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_164'] = {'inputs': ['rc_replacement_d2_164'], 'func': rc_replacement_d3_164}


def rc_replacement_d3_165(rc_replacement_d2_165):
    feature = _clean(rc_replacement_d2_165)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00082500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_165'] = {'inputs': ['rc_replacement_d2_165'], 'func': rc_replacement_d3_165}


def rc_replacement_d3_166(rc_replacement_d2_166):
    feature = _clean(rc_replacement_d2_166)
    accel = feature.diff(89)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_166'] = {'inputs': ['rc_replacement_d2_166'], 'func': rc_replacement_d3_166}


def rc_replacement_d3_167(rc_replacement_d2_167):
    feature = _clean(rc_replacement_d2_167)
    accel = feature.diff(1)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00083500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_167'] = {'inputs': ['rc_replacement_d2_167'], 'func': rc_replacement_d3_167}


def rc_replacement_d3_168(rc_replacement_d2_168):
    feature = _clean(rc_replacement_d2_168)
    accel = feature.diff(2)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_168'] = {'inputs': ['rc_replacement_d2_168'], 'func': rc_replacement_d3_168}


def rc_replacement_d3_169(rc_replacement_d2_169):
    feature = _clean(rc_replacement_d2_169)
    accel = feature.diff(3)
    curvature = feature - feature.rolling(13, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00084500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_169'] = {'inputs': ['rc_replacement_d2_169'], 'func': rc_replacement_d3_169}


def rc_replacement_d3_170(rc_replacement_d2_170):
    feature = _clean(rc_replacement_d2_170)
    accel = feature.diff(5)
    curvature = feature - feature.rolling(21, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_170'] = {'inputs': ['rc_replacement_d2_170'], 'func': rc_replacement_d3_170}


def rc_replacement_d3_171(rc_replacement_d2_171):
    feature = _clean(rc_replacement_d2_171)
    accel = feature.diff(8)
    curvature = feature - feature.rolling(34, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00085500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_171'] = {'inputs': ['rc_replacement_d2_171'], 'func': rc_replacement_d3_171}


def rc_replacement_d3_172(rc_replacement_d2_172):
    feature = _clean(rc_replacement_d2_172)
    accel = feature.diff(13)
    curvature = feature - feature.rolling(55, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_172'] = {'inputs': ['rc_replacement_d2_172'], 'func': rc_replacement_d3_172}


def rc_replacement_d3_173(rc_replacement_d2_173):
    feature = _clean(rc_replacement_d2_173)
    accel = feature.diff(21)
    curvature = feature - feature.rolling(3, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00086500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_173'] = {'inputs': ['rc_replacement_d2_173'], 'func': rc_replacement_d3_173}


def rc_replacement_d3_174(rc_replacement_d2_174):
    feature = _clean(rc_replacement_d2_174)
    accel = feature.diff(34)
    curvature = feature - feature.rolling(5, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087000).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_174'] = {'inputs': ['rc_replacement_d2_174'], 'func': rc_replacement_d3_174}


def rc_replacement_d3_175(rc_replacement_d2_175):
    feature = _clean(rc_replacement_d2_175)
    accel = feature.diff(55)
    curvature = feature - feature.rolling(8, min_periods=2).mean()
    return _clean(accel + curvature.fillna(0.0) * 0.00087500).reindex(feature.index)
RC_REPLACEMENT_3RD_DERIVATIVES_REGISTRY['rc_replacement_d3_175'] = {'inputs': ['rc_replacement_d2_175'], 'func': rc_replacement_d3_175}


# Third-derivative extensions for repaired first-base features.
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY = {}


def _base_universe_d3(feature, idx):
    feature = _clean(feature) if '_clean' in globals() else _s(feature).replace([np.inf, -np.inf], np.nan)
    windows = [1, 2, 3, 5, 8, 13, 21, 34, 55]
    lag = windows[(idx * 2) % len(windows)]
    smooth = windows[(idx * 5 + 2) % len(windows)]
    accel = feature.diff(lag)
    curve = feature - feature.rolling(max(3, smooth), min_periods=2).mean()
    out = accel + curve.fillna(0.0) * (0.00019 * ((idx % 19) + 1))
    return out.replace([np.inf, -np.inf], np.nan).reindex(feature.index)


def rcp_base_universe_d3_001_rcp_002_range_expansion_10_002(rcp_base_universe_d2_001_rcp_002_range_expansion_10_002):
    return _base_universe_d3(rcp_base_universe_d2_001_rcp_002_range_expansion_10_002, 1)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_001_rcp_002_range_expansion_10_002'] = {'inputs': ['rcp_base_universe_d2_001_rcp_002_range_expansion_10_002'], 'func': rcp_base_universe_d3_001_rcp_002_range_expansion_10_002}


def rcp_base_universe_d3_002_rcp_004_close_location_42_004(rcp_base_universe_d2_002_rcp_004_close_location_42_004):
    return _base_universe_d3(rcp_base_universe_d2_002_rcp_004_close_location_42_004, 2)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_002_rcp_004_close_location_42_004'] = {'inputs': ['rcp_base_universe_d2_002_rcp_004_close_location_42_004'], 'func': rcp_base_universe_d3_002_rcp_004_close_location_42_004}


def rcp_base_universe_d3_003_rcp_005_atr_move_63_005(rcp_base_universe_d2_003_rcp_005_atr_move_63_005):
    return _base_universe_d3(rcp_base_universe_d2_003_rcp_005_atr_move_63_005, 3)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_003_rcp_005_atr_move_63_005'] = {'inputs': ['rcp_base_universe_d2_003_rcp_005_atr_move_63_005'], 'func': rcp_base_universe_d3_003_rcp_005_atr_move_63_005}


def rcp_base_universe_d3_004_rcp_008_range_expansion_189_008(rcp_base_universe_d2_004_rcp_008_range_expansion_189_008):
    return _base_universe_d3(rcp_base_universe_d2_004_rcp_008_range_expansion_189_008, 4)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_004_rcp_008_range_expansion_189_008'] = {'inputs': ['rcp_base_universe_d2_004_rcp_008_range_expansion_189_008'], 'func': rcp_base_universe_d3_004_rcp_008_range_expansion_189_008}


def rcp_base_universe_d3_005_rcp_010_close_location_378_010(rcp_base_universe_d2_005_rcp_010_close_location_378_010):
    return _base_universe_d3(rcp_base_universe_d2_005_rcp_010_close_location_378_010, 5)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_005_rcp_010_close_location_378_010'] = {'inputs': ['rcp_base_universe_d2_005_rcp_010_close_location_378_010'], 'func': rcp_base_universe_d3_005_rcp_010_close_location_378_010}


def rcp_base_universe_d3_006_rcp_011_atr_move_504_011(rcp_base_universe_d2_006_rcp_011_atr_move_504_011):
    return _base_universe_d3(rcp_base_universe_d2_006_rcp_011_atr_move_504_011, 6)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_006_rcp_011_atr_move_504_011'] = {'inputs': ['rcp_base_universe_d2_006_rcp_011_atr_move_504_011'], 'func': rcp_base_universe_d3_006_rcp_011_atr_move_504_011}


def rcp_base_universe_d3_007_rcp_014_range_expansion_1260_014(rcp_base_universe_d2_007_rcp_014_range_expansion_1260_014):
    return _base_universe_d3(rcp_base_universe_d2_007_rcp_014_range_expansion_1260_014, 7)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_007_rcp_014_range_expansion_1260_014'] = {'inputs': ['rcp_base_universe_d2_007_rcp_014_range_expansion_1260_014'], 'func': rcp_base_universe_d3_007_rcp_014_range_expansion_1260_014}


def rcp_base_universe_d3_008_rcp_016_close_location_5_016(rcp_base_universe_d2_008_rcp_016_close_location_5_016):
    return _base_universe_d3(rcp_base_universe_d2_008_rcp_016_close_location_5_016, 8)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_008_rcp_016_close_location_5_016'] = {'inputs': ['rcp_base_universe_d2_008_rcp_016_close_location_5_016'], 'func': rcp_base_universe_d3_008_rcp_016_close_location_5_016}


def rcp_base_universe_d3_009_rcp_017_atr_move_10_017(rcp_base_universe_d2_009_rcp_017_atr_move_10_017):
    return _base_universe_d3(rcp_base_universe_d2_009_rcp_017_atr_move_10_017, 9)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_009_rcp_017_atr_move_10_017'] = {'inputs': ['rcp_base_universe_d2_009_rcp_017_atr_move_10_017'], 'func': rcp_base_universe_d3_009_rcp_017_atr_move_10_017}


def rcp_base_universe_d3_010_rcp_020_range_expansion_63_020(rcp_base_universe_d2_010_rcp_020_range_expansion_63_020):
    return _base_universe_d3(rcp_base_universe_d2_010_rcp_020_range_expansion_63_020, 10)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_010_rcp_020_range_expansion_63_020'] = {'inputs': ['rcp_base_universe_d2_010_rcp_020_range_expansion_63_020'], 'func': rcp_base_universe_d3_010_rcp_020_range_expansion_63_020}


def rcp_base_universe_d3_011_rcp_022_close_location_126_022(rcp_base_universe_d2_011_rcp_022_close_location_126_022):
    return _base_universe_d3(rcp_base_universe_d2_011_rcp_022_close_location_126_022, 11)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_011_rcp_022_close_location_126_022'] = {'inputs': ['rcp_base_universe_d2_011_rcp_022_close_location_126_022'], 'func': rcp_base_universe_d3_011_rcp_022_close_location_126_022}


def rcp_base_universe_d3_012_rcp_023_atr_move_189_023(rcp_base_universe_d2_012_rcp_023_atr_move_189_023):
    return _base_universe_d3(rcp_base_universe_d2_012_rcp_023_atr_move_189_023, 12)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_012_rcp_023_atr_move_189_023'] = {'inputs': ['rcp_base_universe_d2_012_rcp_023_atr_move_189_023'], 'func': rcp_base_universe_d3_012_rcp_023_atr_move_189_023}


def rcp_base_universe_d3_013_rcp_026_range_expansion_504_026(rcp_base_universe_d2_013_rcp_026_range_expansion_504_026):
    return _base_universe_d3(rcp_base_universe_d2_013_rcp_026_range_expansion_504_026, 13)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_013_rcp_026_range_expansion_504_026'] = {'inputs': ['rcp_base_universe_d2_013_rcp_026_range_expansion_504_026'], 'func': rcp_base_universe_d3_013_rcp_026_range_expansion_504_026}


def rcp_base_universe_d3_014_rcp_028_close_location_1008_028(rcp_base_universe_d2_014_rcp_028_close_location_1008_028):
    return _base_universe_d3(rcp_base_universe_d2_014_rcp_028_close_location_1008_028, 14)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_014_rcp_028_close_location_1008_028'] = {'inputs': ['rcp_base_universe_d2_014_rcp_028_close_location_1008_028'], 'func': rcp_base_universe_d3_014_rcp_028_close_location_1008_028}


def rcp_base_universe_d3_015_rcp_029_atr_move_1260_029(rcp_base_universe_d2_015_rcp_029_atr_move_1260_029):
    return _base_universe_d3(rcp_base_universe_d2_015_rcp_029_atr_move_1260_029, 15)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_015_rcp_029_atr_move_1260_029'] = {'inputs': ['rcp_base_universe_d2_015_rcp_029_atr_move_1260_029'], 'func': rcp_base_universe_d3_015_rcp_029_atr_move_1260_029}


def rcp_base_universe_d3_016_rcp_basefill_001(rcp_base_universe_d2_016_rcp_basefill_001):
    return _base_universe_d3(rcp_base_universe_d2_016_rcp_basefill_001, 16)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_016_rcp_basefill_001'] = {'inputs': ['rcp_base_universe_d2_016_rcp_basefill_001'], 'func': rcp_base_universe_d3_016_rcp_basefill_001}


def rcp_base_universe_d3_017_rcp_basefill_003(rcp_base_universe_d2_017_rcp_basefill_003):
    return _base_universe_d3(rcp_base_universe_d2_017_rcp_basefill_003, 17)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_017_rcp_basefill_003'] = {'inputs': ['rcp_base_universe_d2_017_rcp_basefill_003'], 'func': rcp_base_universe_d3_017_rcp_basefill_003}


def rcp_base_universe_d3_018_rcp_basefill_006(rcp_base_universe_d2_018_rcp_basefill_006):
    return _base_universe_d3(rcp_base_universe_d2_018_rcp_basefill_006, 18)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_018_rcp_basefill_006'] = {'inputs': ['rcp_base_universe_d2_018_rcp_basefill_006'], 'func': rcp_base_universe_d3_018_rcp_basefill_006}


def rcp_base_universe_d3_019_rcp_basefill_007(rcp_base_universe_d2_019_rcp_basefill_007):
    return _base_universe_d3(rcp_base_universe_d2_019_rcp_basefill_007, 19)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_019_rcp_basefill_007'] = {'inputs': ['rcp_base_universe_d2_019_rcp_basefill_007'], 'func': rcp_base_universe_d3_019_rcp_basefill_007}


def rcp_base_universe_d3_020_rcp_basefill_009(rcp_base_universe_d2_020_rcp_basefill_009):
    return _base_universe_d3(rcp_base_universe_d2_020_rcp_basefill_009, 20)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_020_rcp_basefill_009'] = {'inputs': ['rcp_base_universe_d2_020_rcp_basefill_009'], 'func': rcp_base_universe_d3_020_rcp_basefill_009}


def rcp_base_universe_d3_021_rcp_basefill_012(rcp_base_universe_d2_021_rcp_basefill_012):
    return _base_universe_d3(rcp_base_universe_d2_021_rcp_basefill_012, 21)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_021_rcp_basefill_012'] = {'inputs': ['rcp_base_universe_d2_021_rcp_basefill_012'], 'func': rcp_base_universe_d3_021_rcp_basefill_012}


def rcp_base_universe_d3_022_rcp_basefill_013(rcp_base_universe_d2_022_rcp_basefill_013):
    return _base_universe_d3(rcp_base_universe_d2_022_rcp_basefill_013, 22)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_022_rcp_basefill_013'] = {'inputs': ['rcp_base_universe_d2_022_rcp_basefill_013'], 'func': rcp_base_universe_d3_022_rcp_basefill_013}


def rcp_base_universe_d3_023_rcp_basefill_015(rcp_base_universe_d2_023_rcp_basefill_015):
    return _base_universe_d3(rcp_base_universe_d2_023_rcp_basefill_015, 23)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_023_rcp_basefill_015'] = {'inputs': ['rcp_base_universe_d2_023_rcp_basefill_015'], 'func': rcp_base_universe_d3_023_rcp_basefill_015}


def rcp_base_universe_d3_024_rcp_basefill_018(rcp_base_universe_d2_024_rcp_basefill_018):
    return _base_universe_d3(rcp_base_universe_d2_024_rcp_basefill_018, 24)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_024_rcp_basefill_018'] = {'inputs': ['rcp_base_universe_d2_024_rcp_basefill_018'], 'func': rcp_base_universe_d3_024_rcp_basefill_018}


def rcp_base_universe_d3_025_rcp_basefill_019(rcp_base_universe_d2_025_rcp_basefill_019):
    return _base_universe_d3(rcp_base_universe_d2_025_rcp_basefill_019, 25)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_025_rcp_basefill_019'] = {'inputs': ['rcp_base_universe_d2_025_rcp_basefill_019'], 'func': rcp_base_universe_d3_025_rcp_basefill_019}


def rcp_base_universe_d3_026_rcp_basefill_021(rcp_base_universe_d2_026_rcp_basefill_021):
    return _base_universe_d3(rcp_base_universe_d2_026_rcp_basefill_021, 26)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_026_rcp_basefill_021'] = {'inputs': ['rcp_base_universe_d2_026_rcp_basefill_021'], 'func': rcp_base_universe_d3_026_rcp_basefill_021}


def rcp_base_universe_d3_027_rcp_basefill_024(rcp_base_universe_d2_027_rcp_basefill_024):
    return _base_universe_d3(rcp_base_universe_d2_027_rcp_basefill_024, 27)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_027_rcp_basefill_024'] = {'inputs': ['rcp_base_universe_d2_027_rcp_basefill_024'], 'func': rcp_base_universe_d3_027_rcp_basefill_024}


def rcp_base_universe_d3_028_rcp_basefill_025(rcp_base_universe_d2_028_rcp_basefill_025):
    return _base_universe_d3(rcp_base_universe_d2_028_rcp_basefill_025, 28)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_028_rcp_basefill_025'] = {'inputs': ['rcp_base_universe_d2_028_rcp_basefill_025'], 'func': rcp_base_universe_d3_028_rcp_basefill_025}


def rcp_base_universe_d3_029_rcp_basefill_027(rcp_base_universe_d2_029_rcp_basefill_027):
    return _base_universe_d3(rcp_base_universe_d2_029_rcp_basefill_027, 29)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_029_rcp_basefill_027'] = {'inputs': ['rcp_base_universe_d2_029_rcp_basefill_027'], 'func': rcp_base_universe_d3_029_rcp_basefill_027}


def rcp_base_universe_d3_030_rcp_basefill_030(rcp_base_universe_d2_030_rcp_basefill_030):
    return _base_universe_d3(rcp_base_universe_d2_030_rcp_basefill_030, 30)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_030_rcp_basefill_030'] = {'inputs': ['rcp_base_universe_d2_030_rcp_basefill_030'], 'func': rcp_base_universe_d3_030_rcp_basefill_030}


def rcp_base_universe_d3_031_rcp_basefill_031(rcp_base_universe_d2_031_rcp_basefill_031):
    return _base_universe_d3(rcp_base_universe_d2_031_rcp_basefill_031, 31)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_031_rcp_basefill_031'] = {'inputs': ['rcp_base_universe_d2_031_rcp_basefill_031'], 'func': rcp_base_universe_d3_031_rcp_basefill_031}


def rcp_base_universe_d3_032_rcp_basefill_032(rcp_base_universe_d2_032_rcp_basefill_032):
    return _base_universe_d3(rcp_base_universe_d2_032_rcp_basefill_032, 32)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_032_rcp_basefill_032'] = {'inputs': ['rcp_base_universe_d2_032_rcp_basefill_032'], 'func': rcp_base_universe_d3_032_rcp_basefill_032}


def rcp_base_universe_d3_033_rcp_basefill_033(rcp_base_universe_d2_033_rcp_basefill_033):
    return _base_universe_d3(rcp_base_universe_d2_033_rcp_basefill_033, 33)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_033_rcp_basefill_033'] = {'inputs': ['rcp_base_universe_d2_033_rcp_basefill_033'], 'func': rcp_base_universe_d3_033_rcp_basefill_033}


def rcp_base_universe_d3_034_rcp_basefill_034(rcp_base_universe_d2_034_rcp_basefill_034):
    return _base_universe_d3(rcp_base_universe_d2_034_rcp_basefill_034, 34)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_034_rcp_basefill_034'] = {'inputs': ['rcp_base_universe_d2_034_rcp_basefill_034'], 'func': rcp_base_universe_d3_034_rcp_basefill_034}


def rcp_base_universe_d3_035_rcp_basefill_035(rcp_base_universe_d2_035_rcp_basefill_035):
    return _base_universe_d3(rcp_base_universe_d2_035_rcp_basefill_035, 35)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_035_rcp_basefill_035'] = {'inputs': ['rcp_base_universe_d2_035_rcp_basefill_035'], 'func': rcp_base_universe_d3_035_rcp_basefill_035}


def rcp_base_universe_d3_036_rcp_basefill_036(rcp_base_universe_d2_036_rcp_basefill_036):
    return _base_universe_d3(rcp_base_universe_d2_036_rcp_basefill_036, 36)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_036_rcp_basefill_036'] = {'inputs': ['rcp_base_universe_d2_036_rcp_basefill_036'], 'func': rcp_base_universe_d3_036_rcp_basefill_036}


def rcp_base_universe_d3_037_rcp_basefill_037(rcp_base_universe_d2_037_rcp_basefill_037):
    return _base_universe_d3(rcp_base_universe_d2_037_rcp_basefill_037, 37)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_037_rcp_basefill_037'] = {'inputs': ['rcp_base_universe_d2_037_rcp_basefill_037'], 'func': rcp_base_universe_d3_037_rcp_basefill_037}


def rcp_base_universe_d3_038_rcp_basefill_038(rcp_base_universe_d2_038_rcp_basefill_038):
    return _base_universe_d3(rcp_base_universe_d2_038_rcp_basefill_038, 38)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_038_rcp_basefill_038'] = {'inputs': ['rcp_base_universe_d2_038_rcp_basefill_038'], 'func': rcp_base_universe_d3_038_rcp_basefill_038}


def rcp_base_universe_d3_039_rcp_basefill_039(rcp_base_universe_d2_039_rcp_basefill_039):
    return _base_universe_d3(rcp_base_universe_d2_039_rcp_basefill_039, 39)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_039_rcp_basefill_039'] = {'inputs': ['rcp_base_universe_d2_039_rcp_basefill_039'], 'func': rcp_base_universe_d3_039_rcp_basefill_039}


def rcp_base_universe_d3_040_rcp_basefill_040(rcp_base_universe_d2_040_rcp_basefill_040):
    return _base_universe_d3(rcp_base_universe_d2_040_rcp_basefill_040, 40)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_040_rcp_basefill_040'] = {'inputs': ['rcp_base_universe_d2_040_rcp_basefill_040'], 'func': rcp_base_universe_d3_040_rcp_basefill_040}


def rcp_base_universe_d3_041_rcp_basefill_041(rcp_base_universe_d2_041_rcp_basefill_041):
    return _base_universe_d3(rcp_base_universe_d2_041_rcp_basefill_041, 41)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_041_rcp_basefill_041'] = {'inputs': ['rcp_base_universe_d2_041_rcp_basefill_041'], 'func': rcp_base_universe_d3_041_rcp_basefill_041}


def rcp_base_universe_d3_042_rcp_basefill_042(rcp_base_universe_d2_042_rcp_basefill_042):
    return _base_universe_d3(rcp_base_universe_d2_042_rcp_basefill_042, 42)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_042_rcp_basefill_042'] = {'inputs': ['rcp_base_universe_d2_042_rcp_basefill_042'], 'func': rcp_base_universe_d3_042_rcp_basefill_042}


def rcp_base_universe_d3_043_rcp_basefill_043(rcp_base_universe_d2_043_rcp_basefill_043):
    return _base_universe_d3(rcp_base_universe_d2_043_rcp_basefill_043, 43)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_043_rcp_basefill_043'] = {'inputs': ['rcp_base_universe_d2_043_rcp_basefill_043'], 'func': rcp_base_universe_d3_043_rcp_basefill_043}


def rcp_base_universe_d3_044_rcp_basefill_044(rcp_base_universe_d2_044_rcp_basefill_044):
    return _base_universe_d3(rcp_base_universe_d2_044_rcp_basefill_044, 44)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_044_rcp_basefill_044'] = {'inputs': ['rcp_base_universe_d2_044_rcp_basefill_044'], 'func': rcp_base_universe_d3_044_rcp_basefill_044}


def rcp_base_universe_d3_045_rcp_basefill_045(rcp_base_universe_d2_045_rcp_basefill_045):
    return _base_universe_d3(rcp_base_universe_d2_045_rcp_basefill_045, 45)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_045_rcp_basefill_045'] = {'inputs': ['rcp_base_universe_d2_045_rcp_basefill_045'], 'func': rcp_base_universe_d3_045_rcp_basefill_045}


def rcp_base_universe_d3_046_rcp_basefill_046(rcp_base_universe_d2_046_rcp_basefill_046):
    return _base_universe_d3(rcp_base_universe_d2_046_rcp_basefill_046, 46)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_046_rcp_basefill_046'] = {'inputs': ['rcp_base_universe_d2_046_rcp_basefill_046'], 'func': rcp_base_universe_d3_046_rcp_basefill_046}


def rcp_base_universe_d3_047_rcp_basefill_047(rcp_base_universe_d2_047_rcp_basefill_047):
    return _base_universe_d3(rcp_base_universe_d2_047_rcp_basefill_047, 47)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_047_rcp_basefill_047'] = {'inputs': ['rcp_base_universe_d2_047_rcp_basefill_047'], 'func': rcp_base_universe_d3_047_rcp_basefill_047}


def rcp_base_universe_d3_048_rcp_basefill_048(rcp_base_universe_d2_048_rcp_basefill_048):
    return _base_universe_d3(rcp_base_universe_d2_048_rcp_basefill_048, 48)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_048_rcp_basefill_048'] = {'inputs': ['rcp_base_universe_d2_048_rcp_basefill_048'], 'func': rcp_base_universe_d3_048_rcp_basefill_048}


def rcp_base_universe_d3_049_rcp_basefill_049(rcp_base_universe_d2_049_rcp_basefill_049):
    return _base_universe_d3(rcp_base_universe_d2_049_rcp_basefill_049, 49)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_049_rcp_basefill_049'] = {'inputs': ['rcp_base_universe_d2_049_rcp_basefill_049'], 'func': rcp_base_universe_d3_049_rcp_basefill_049}


def rcp_base_universe_d3_050_rcp_basefill_050(rcp_base_universe_d2_050_rcp_basefill_050):
    return _base_universe_d3(rcp_base_universe_d2_050_rcp_basefill_050, 50)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_050_rcp_basefill_050'] = {'inputs': ['rcp_base_universe_d2_050_rcp_basefill_050'], 'func': rcp_base_universe_d3_050_rcp_basefill_050}


def rcp_base_universe_d3_051_rcp_basefill_051(rcp_base_universe_d2_051_rcp_basefill_051):
    return _base_universe_d3(rcp_base_universe_d2_051_rcp_basefill_051, 51)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_051_rcp_basefill_051'] = {'inputs': ['rcp_base_universe_d2_051_rcp_basefill_051'], 'func': rcp_base_universe_d3_051_rcp_basefill_051}


def rcp_base_universe_d3_052_rcp_basefill_052(rcp_base_universe_d2_052_rcp_basefill_052):
    return _base_universe_d3(rcp_base_universe_d2_052_rcp_basefill_052, 52)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_052_rcp_basefill_052'] = {'inputs': ['rcp_base_universe_d2_052_rcp_basefill_052'], 'func': rcp_base_universe_d3_052_rcp_basefill_052}


def rcp_base_universe_d3_053_rcp_basefill_053(rcp_base_universe_d2_053_rcp_basefill_053):
    return _base_universe_d3(rcp_base_universe_d2_053_rcp_basefill_053, 53)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_053_rcp_basefill_053'] = {'inputs': ['rcp_base_universe_d2_053_rcp_basefill_053'], 'func': rcp_base_universe_d3_053_rcp_basefill_053}


def rcp_base_universe_d3_054_rcp_basefill_054(rcp_base_universe_d2_054_rcp_basefill_054):
    return _base_universe_d3(rcp_base_universe_d2_054_rcp_basefill_054, 54)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_054_rcp_basefill_054'] = {'inputs': ['rcp_base_universe_d2_054_rcp_basefill_054'], 'func': rcp_base_universe_d3_054_rcp_basefill_054}


def rcp_base_universe_d3_055_rcp_basefill_055(rcp_base_universe_d2_055_rcp_basefill_055):
    return _base_universe_d3(rcp_base_universe_d2_055_rcp_basefill_055, 55)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_055_rcp_basefill_055'] = {'inputs': ['rcp_base_universe_d2_055_rcp_basefill_055'], 'func': rcp_base_universe_d3_055_rcp_basefill_055}


def rcp_base_universe_d3_056_rcp_basefill_056(rcp_base_universe_d2_056_rcp_basefill_056):
    return _base_universe_d3(rcp_base_universe_d2_056_rcp_basefill_056, 56)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_056_rcp_basefill_056'] = {'inputs': ['rcp_base_universe_d2_056_rcp_basefill_056'], 'func': rcp_base_universe_d3_056_rcp_basefill_056}


def rcp_base_universe_d3_057_rcp_basefill_057(rcp_base_universe_d2_057_rcp_basefill_057):
    return _base_universe_d3(rcp_base_universe_d2_057_rcp_basefill_057, 57)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_057_rcp_basefill_057'] = {'inputs': ['rcp_base_universe_d2_057_rcp_basefill_057'], 'func': rcp_base_universe_d3_057_rcp_basefill_057}


def rcp_base_universe_d3_058_rcp_basefill_058(rcp_base_universe_d2_058_rcp_basefill_058):
    return _base_universe_d3(rcp_base_universe_d2_058_rcp_basefill_058, 58)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_058_rcp_basefill_058'] = {'inputs': ['rcp_base_universe_d2_058_rcp_basefill_058'], 'func': rcp_base_universe_d3_058_rcp_basefill_058}


def rcp_base_universe_d3_059_rcp_basefill_059(rcp_base_universe_d2_059_rcp_basefill_059):
    return _base_universe_d3(rcp_base_universe_d2_059_rcp_basefill_059, 59)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_059_rcp_basefill_059'] = {'inputs': ['rcp_base_universe_d2_059_rcp_basefill_059'], 'func': rcp_base_universe_d3_059_rcp_basefill_059}


def rcp_base_universe_d3_060_rcp_basefill_060(rcp_base_universe_d2_060_rcp_basefill_060):
    return _base_universe_d3(rcp_base_universe_d2_060_rcp_basefill_060, 60)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_060_rcp_basefill_060'] = {'inputs': ['rcp_base_universe_d2_060_rcp_basefill_060'], 'func': rcp_base_universe_d3_060_rcp_basefill_060}


def rcp_base_universe_d3_061_rcp_basefill_061(rcp_base_universe_d2_061_rcp_basefill_061):
    return _base_universe_d3(rcp_base_universe_d2_061_rcp_basefill_061, 61)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_061_rcp_basefill_061'] = {'inputs': ['rcp_base_universe_d2_061_rcp_basefill_061'], 'func': rcp_base_universe_d3_061_rcp_basefill_061}


def rcp_base_universe_d3_062_rcp_basefill_062(rcp_base_universe_d2_062_rcp_basefill_062):
    return _base_universe_d3(rcp_base_universe_d2_062_rcp_basefill_062, 62)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_062_rcp_basefill_062'] = {'inputs': ['rcp_base_universe_d2_062_rcp_basefill_062'], 'func': rcp_base_universe_d3_062_rcp_basefill_062}


def rcp_base_universe_d3_063_rcp_basefill_063(rcp_base_universe_d2_063_rcp_basefill_063):
    return _base_universe_d3(rcp_base_universe_d2_063_rcp_basefill_063, 63)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_063_rcp_basefill_063'] = {'inputs': ['rcp_base_universe_d2_063_rcp_basefill_063'], 'func': rcp_base_universe_d3_063_rcp_basefill_063}


def rcp_base_universe_d3_064_rcp_basefill_064(rcp_base_universe_d2_064_rcp_basefill_064):
    return _base_universe_d3(rcp_base_universe_d2_064_rcp_basefill_064, 64)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_064_rcp_basefill_064'] = {'inputs': ['rcp_base_universe_d2_064_rcp_basefill_064'], 'func': rcp_base_universe_d3_064_rcp_basefill_064}


def rcp_base_universe_d3_065_rcp_basefill_065(rcp_base_universe_d2_065_rcp_basefill_065):
    return _base_universe_d3(rcp_base_universe_d2_065_rcp_basefill_065, 65)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_065_rcp_basefill_065'] = {'inputs': ['rcp_base_universe_d2_065_rcp_basefill_065'], 'func': rcp_base_universe_d3_065_rcp_basefill_065}


def rcp_base_universe_d3_066_rcp_basefill_066(rcp_base_universe_d2_066_rcp_basefill_066):
    return _base_universe_d3(rcp_base_universe_d2_066_rcp_basefill_066, 66)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_066_rcp_basefill_066'] = {'inputs': ['rcp_base_universe_d2_066_rcp_basefill_066'], 'func': rcp_base_universe_d3_066_rcp_basefill_066}


def rcp_base_universe_d3_067_rcp_basefill_067(rcp_base_universe_d2_067_rcp_basefill_067):
    return _base_universe_d3(rcp_base_universe_d2_067_rcp_basefill_067, 67)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_067_rcp_basefill_067'] = {'inputs': ['rcp_base_universe_d2_067_rcp_basefill_067'], 'func': rcp_base_universe_d3_067_rcp_basefill_067}


def rcp_base_universe_d3_068_rcp_basefill_068(rcp_base_universe_d2_068_rcp_basefill_068):
    return _base_universe_d3(rcp_base_universe_d2_068_rcp_basefill_068, 68)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_068_rcp_basefill_068'] = {'inputs': ['rcp_base_universe_d2_068_rcp_basefill_068'], 'func': rcp_base_universe_d3_068_rcp_basefill_068}


def rcp_base_universe_d3_069_rcp_basefill_069(rcp_base_universe_d2_069_rcp_basefill_069):
    return _base_universe_d3(rcp_base_universe_d2_069_rcp_basefill_069, 69)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_069_rcp_basefill_069'] = {'inputs': ['rcp_base_universe_d2_069_rcp_basefill_069'], 'func': rcp_base_universe_d3_069_rcp_basefill_069}


def rcp_base_universe_d3_070_rcp_basefill_070(rcp_base_universe_d2_070_rcp_basefill_070):
    return _base_universe_d3(rcp_base_universe_d2_070_rcp_basefill_070, 70)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_070_rcp_basefill_070'] = {'inputs': ['rcp_base_universe_d2_070_rcp_basefill_070'], 'func': rcp_base_universe_d3_070_rcp_basefill_070}


def rcp_base_universe_d3_071_rcp_basefill_071(rcp_base_universe_d2_071_rcp_basefill_071):
    return _base_universe_d3(rcp_base_universe_d2_071_rcp_basefill_071, 71)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_071_rcp_basefill_071'] = {'inputs': ['rcp_base_universe_d2_071_rcp_basefill_071'], 'func': rcp_base_universe_d3_071_rcp_basefill_071}


def rcp_base_universe_d3_072_rcp_basefill_072(rcp_base_universe_d2_072_rcp_basefill_072):
    return _base_universe_d3(rcp_base_universe_d2_072_rcp_basefill_072, 72)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_072_rcp_basefill_072'] = {'inputs': ['rcp_base_universe_d2_072_rcp_basefill_072'], 'func': rcp_base_universe_d3_072_rcp_basefill_072}


def rcp_base_universe_d3_073_rcp_basefill_073(rcp_base_universe_d2_073_rcp_basefill_073):
    return _base_universe_d3(rcp_base_universe_d2_073_rcp_basefill_073, 73)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_073_rcp_basefill_073'] = {'inputs': ['rcp_base_universe_d2_073_rcp_basefill_073'], 'func': rcp_base_universe_d3_073_rcp_basefill_073}


def rcp_base_universe_d3_074_rcp_basefill_074(rcp_base_universe_d2_074_rcp_basefill_074):
    return _base_universe_d3(rcp_base_universe_d2_074_rcp_basefill_074, 74)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_074_rcp_basefill_074'] = {'inputs': ['rcp_base_universe_d2_074_rcp_basefill_074'], 'func': rcp_base_universe_d3_074_rcp_basefill_074}


def rcp_base_universe_d3_075_rcp_basefill_075(rcp_base_universe_d2_075_rcp_basefill_075):
    return _base_universe_d3(rcp_base_universe_d2_075_rcp_basefill_075, 75)
RCP_BASE_UNIVERSE_3RD_DERIVATIVES_REGISTRY['rcp_base_universe_d3_075_rcp_basefill_075'] = {'inputs': ['rcp_base_universe_d2_075_rcp_basefill_075'], 'func': rcp_base_universe_d3_075_rcp_basefill_075}
