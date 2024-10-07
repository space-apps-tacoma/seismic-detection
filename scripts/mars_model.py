# Provide a sample Random Forest ML Model for seismic event detection on Mars
import extract_csv
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from obspy import read
from obspy.signal.invsim import cosine_taper
from obspy.signal.filter import highpass
from obspy.signal.trigger import classic_sta_lta, plot_trigger, trigger_onset

# Mars training data
mars_train = extract_csv.extract_data('mars', 'train', 'csv')

# Mars window lengths
mars_short = 100
mars_long = 500

# Calculate Mars sampling frequency
mars_obs = len(mars_train)
mars_time_diffs = mars_train.groupby('filename')['time_abs'].apply(
    lambda x: (x.max() - x.min()).total_seconds()
)
mars_total_time = mars_time_diffs.sum()
mars_sampling_freq = (mars_obs / mars_total_time)

# Get numpy array of velocity observations
mars_tr_data = mars_train['velocity(c/s)'].to_numpy()

# Get numpy array of time observations
mars_tr_times = mars_train['time_abs'].to_numpy()

# Run Obspy's STA/LTA to obtain a characteristic function
mars_cft = classic_sta_lta(mars_tr_data, int(mars_short * mars_sampling_freq), int(mars_long * mars_sampling_freq))

# Plot characteristic function
fig,ax = plt.subplots(1,1,figsize=(12,3))
ax.plot(mars_tr_times,mars_cft)
ax.set_xlim([pd.Timestamp('2022-02-03 07:00:00'),pd.Timestamp('2022-02-03 09:00:00')])
ax.set_xlabel('Time')
ax.set_ylabel('Characteristic function')
plt.show()

# Mars triggers
mars_thr_on = 2.5
mars_thr_off = 2.0
on_off = np.array(trigger_onset(mars_cft, mars_thr_on, mars_thr_off))

# Plot on and off triggers
fig,ax = plt.subplots(1,1,figsize=(12,3))
for i in np.arange(0,len(on_off)):
    triggers = on_off[i]
    ax.axvline(x = mars_tr_times[triggers[0]], color='red', label='Trig. On')
    ax.axvline(x = mars_tr_times[triggers[1]], color='purple', label='Trig. Off')

# Plot seismogram
ax.plot(mars_tr_times,mars_tr_data)
ax.set_xlim([pd.Timestamp('2022-02-03 07:00:00'),pd.Timestamp('2022-02-03 09:00:00')])
ax.legend()
plt.show()
