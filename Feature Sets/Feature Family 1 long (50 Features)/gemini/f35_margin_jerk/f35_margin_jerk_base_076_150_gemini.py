import pandas as pd
import numpy as np

def _sma(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).mean()
def _std(s, w): return s.rolling(w, min_periods=min(w, 20) if w > 20 else min(w, 2)).std()
def _z(s, w): return (s - _sma(s, w)) / _std(s, w).replace(0, np.nan)

def _mj_margin(num, den):
    return num / den.replace(0, np.nan)

def _mj_accel(s, w1, w2):
    return s.pct_change(w1).pct_change(w2)

def _mj_jerk(s, w1, w2, w3):
    accel = s.pct_change(w1).pct_change(w2)
    return accel.diff(w3)

def _mj_slope(s, w):
    return s.pct_change(w)

def _mj_jerk_deriv(s, w):
    return s.diff(w)

def _mj_zscore(s, w):
    return _z(s, w)

def f35_margin_jerk_margin_accel_v076_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 76. Component of the jerk calculation for 76d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 76, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v077_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 77. Component of the jerk calculation for 77d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 77, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v078_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 78. Component of the jerk calculation for 78d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 78, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v079_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 79. Component of the jerk calculation for 79d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 79, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v080_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 80. Component of the jerk calculation for 80d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 80, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v081_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 81. Component of the jerk calculation for 81d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 81, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v082_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 82. Component of the jerk calculation for 82d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 82, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v083_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 83. Component of the jerk calculation for 83d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 83, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v084_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 84. Component of the jerk calculation for 84d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 84, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v085_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 85. Component of the jerk calculation for 85d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 85, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v086_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 86. Component of the jerk calculation for 86d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 86, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v087_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 87. Component of the jerk calculation for 87d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 87, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v088_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 88. Component of the jerk calculation for 88d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 88, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v089_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 89. Component of the jerk calculation for 89d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 89, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v090_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 90. Component of the jerk calculation for 90d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 90, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v091_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 91. Component of the jerk calculation for 91d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 91, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v092_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 92. Component of the jerk calculation for 92d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 92, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v093_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 93. Component of the jerk calculation for 93d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 93, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v094_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 94. Component of the jerk calculation for 94d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 94, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v095_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 95. Component of the jerk calculation for 95d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 95, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v096_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 96. Component of the jerk calculation for 96d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 96, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v097_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 97. Component of the jerk calculation for 97d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 97, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v098_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 98. Component of the jerk calculation for 98d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 98, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v099_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 99. Component of the jerk calculation for 99d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 99, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v100_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 100. Component of the jerk calculation for 100d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 100, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v101_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 101. Component of the jerk calculation for 101d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 101, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v102_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 102. Component of the jerk calculation for 102d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 102, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v103_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 103. Component of the jerk calculation for 103d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 103, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v104_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 104. Component of the jerk calculation for 104d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 104, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v105_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 105. Component of the jerk calculation for 105d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 105, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v106_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 106. Component of the jerk calculation for 106d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 106, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v107_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 107. Component of the jerk calculation for 107d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 107, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v108_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 108. Component of the jerk calculation for 108d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 108, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v109_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 109. Component of the jerk calculation for 109d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 109, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v110_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 110. Component of the jerk calculation for 110d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 110, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v111_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 111. Component of the jerk calculation for 111d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 111, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v112_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 112. Component of the jerk calculation for 112d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 112, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v113_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 113. Component of the jerk calculation for 113d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 113, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v114_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 114. Component of the jerk calculation for 114d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 114, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v115_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 115. Component of the jerk calculation for 115d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 115, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v116_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 116. Component of the jerk calculation for 116d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 116, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v117_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 117. Component of the jerk calculation for 117d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 117, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v118_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 118. Component of the jerk calculation for 118d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 118, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v119_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 119. Component of the jerk calculation for 119d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 119, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v120_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 120. Component of the jerk calculation for 120d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 120, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v121_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 121. Component of the jerk calculation for 121d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 121, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v122_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 122. Component of the jerk calculation for 122d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 122, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v123_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 123. Component of the jerk calculation for 123d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 123, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v124_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 124. Component of the jerk calculation for 124d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 124, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v125_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 125. Component of the jerk calculation for 125d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 125, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v126_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 126. Component of the jerk calculation for 126d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 126, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v127_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 127. Component of the jerk calculation for 127d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 127, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v128_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 128. Component of the jerk calculation for 128d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 128, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v129_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 129. Component of the jerk calculation for 129d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 129, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v130_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 130. Component of the jerk calculation for 130d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 130, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v131_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 131. Component of the jerk calculation for 131d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 131, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v132_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 132. Component of the jerk calculation for 132d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 132, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v133_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 133. Component of the jerk calculation for 133d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 133, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v134_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 134. Component of the jerk calculation for 134d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 134, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v135_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 135. Component of the jerk calculation for 135d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 135, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v136_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 136. Component of the jerk calculation for 136d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 136, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v137_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 137. Component of the jerk calculation for 137d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 137, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v138_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 138. Component of the jerk calculation for 138d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 138, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v139_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 139. Component of the jerk calculation for 139d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 139, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v140_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 140. Component of the jerk calculation for 140d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 140, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v141_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 141. Component of the jerk calculation for 141d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 141, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v142_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 142. Component of the jerk calculation for 142d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 142, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v143_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 143. Component of the jerk calculation for 143d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 143, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v144_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 144. Component of the jerk calculation for 144d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 144, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v145_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 145. Component of the jerk calculation for 145d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 145, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v146_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 146. Component of the jerk calculation for 146d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 146, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v147_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 147. Component of the jerk calculation for 147d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 147, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v148_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 148. Component of the jerk calculation for 148d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 148, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v149_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 149. Component of the jerk calculation for 149d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 149, 21)
    return res.replace([np.inf, -np.inf], np.nan)

def f35_margin_jerk_margin_accel_v150_signal(ebitda, revenue) -> pd.Series:
    """Margin acceleration variation 150. Component of the jerk calculation for 150d window."""
    margin = _mj_margin(ebitda, revenue)
    res = _mj_accel(margin, 150, 21)
    return res.replace([np.inf, -np.inf], np.nan)

if __name__ == "__main__":
    import inspect
    np.random.seed(42)
    n = 800
    df = pd.DataFrame({
        "revenue": np.random.normal(1000, 100, n).cumsum() + 10000,
        "opinc": np.random.normal(100, 20, n).cumsum() + 1000,
        "ebitda": np.random.normal(150, 30, n).cumsum() + 1500,
    })
    
    funcs = [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f35_margin_jerk_"))]
    
    print(f"Testing {len(funcs)} functions...")
    for func in funcs:
        sig = inspect.signature(func)
        args = [df[p] for p in sig.parameters]
        y1 = func(*args)
        y2 = func(*args)
        pd.testing.assert_series_equal(y1, y2)
        
        q = y1.iloc[504:].dropna()
        assert len(q) > 0
        assert q.nunique() > 10

    print("All tests passed!")

REGISTRY = {fn.__name__: {"inputs": list(inspect.signature(fn).parameters.keys()), "func": fn} for fn in [obj for name, obj in inspect.getmembers(inspect.getmodule(inspect.currentframe())) if (inspect.isfunction(obj) and name.startswith("f35_margin_jerk_"))]}
F35_MARGIN_JERK_REGISTRY_BASE_076_150 = REGISTRY
