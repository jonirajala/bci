# Studying brains and bci devices

## Brains

### Brain waves
Beta waves are responsible for problem solving or decision making and associated 
with attention. 

Alpha waves are associated with now and meditation.

Frequency generally lies within the 0.1–100 Hz

meditation tends to lead to an increase in the production of theta and alpha waves
the specific type of meditation or mindfulness practice does not appear to matter.
During meditation, theta waves were most abundant in the frontal and middle parts of the brain.
- "These types of waves likely originate from a relaxed attention that monitors our inner experiences. Here lies a significant difference between meditation and relaxing without any specific technique," emphasizes Lagopoulos.
Alpha waves were more abundant in the posterior parts of the brain during meditation than during simple relaxation. They are characteristic of wakeful rest.
alpha
- This wave type has been used as a universal sign of relaxation during meditation and other types of rest," comments Professor Øyvind Ellingsen from NTNU. "The amount of alpha waves increases when the brain relaxes from intentional, goal-oriented tasks.This is a sign of deep relaxation, -- but it does not mean that the mind is void."

Different parts of the brain get stimulated in a particular manner during meditation:
- The frontal lobe, which plans and reasons switch off during meditation, helps you detach and relax.
- The thalamus, which relays motor and sensory signals to the cerebral cortex, slows down its activity, enabling you to keep calm.
- The parietal lobe, which gives you a sense of time also slows down, helping to lower your stress and anxiety levels.
- The reticular keeps your brain alert and helps you respond to situations. During meditation, the reticular activity slows down, allowing you to keep calm and be peaceful.

### Event related potential
= Electrical impulse in brain caused by single event
To capture these it is good to filter out regular brain activity
- Method called ”averaging out”
- 
Apart from the motor activity itself, imagination of motion or Motor Imagery (MI) also creates similar detectable responses but of lower intensity. Since MI can be performed without actual movement, it can be used as a control signal for a BCI system [29]

In terms of temporal resolution, the hemodynamic response lags behind the actual neuronal firing with a delay to maximum response of 6–12 s causing a consequent delay

P300 refers to a spike in activity approximately 300ms following presentation of the target stimulus, which is alternated with standard stimuli to create an ‘oddball’ paradigm, which is most commonly auditory. In this paradigm, the subject must respond only to the infrequent target stimulus rather than the frequent standard stimulus. The amplitude of the P300 response is proportional to the amount of attentional resource devoted to the task and the degree of information processing required, while the latency is considered a measure of stimulus classification speed, unrelated to behavioural response time.

## BCI

### EEG
EEG system should have 21 electrodes for a standard 10–20 measurement system though there are several electrode caps containing different numbers of electrodes (19, 32, 64, up to 256 electrodes)

The EEG signal is measured across two electrodes among which one is the
 reference electrode. Reference electrode recording is an electrode, relative to which
 the electric brain potentials in all other electrodes are measured and hence it should
 be placed on a presumed “inactive” zone on the scalp region.  Alternatively, the EEG signals are recorded onall the scalp electrodes making all the scalp electrode as a reference and the EEG signals are estimated by computing the average reference as a mean of all electrodes measurements [107].

20 electrons seems to be the point after which the accuracy starts to decreace´

These electrodes are made of silver chloride (AgCl). A gel is used which
 creates a conductive path between the skin and the electrode for the flow of current.
 Electrodes that do not use gels, called ‘dry’ electrodes are made of materials such as
 titanium and stainless-steel.

### FMRI
Mittaa veren happipitoisuutta hermosolujen lähellä
MRI is capable of detecting activity in deep cortical and subcortical regions,
### MRI
Mittaa aivojen rakennetta magneetti kentän avulla
### MEG
Mittaa aivosähkökäyriä mageneetin avulla
 MEG measures weak magnetic signals produced by neuronal populations using Superconducting Quantum Interference Devices (SQUIDs).
### fNIRS
NIRS estimates the concentration of hemoglobin from changes in absorption of near infrared light. As light moves or propagates through the head, it is alternately scattered or absorbed by the tissue through which it travels.
allowing measurements of concentration changes in both oxygenated and deoxygenated hemoglobin.

fNIRS is only able to detect NIR light that penetrates the first few centimeters of cortical tissue,

KERNEL

Oxyganated and deoxygenated Hemoglobin and blood have different optical properties

They absorb near infrared light differently


## Signal processing
A number of computational techniques are available for dimensionality reduction.These include principal component analysis (PCA), single value decomposition (SVD), and canonical correlation analysis (CCA) etc. These three examples of dimensionality reduction methods are each discussed below.

Independent component analysis and Principal component analysis

Before the eeg data can be used in the NN, there must be some preprocessing to raise the signal-to-noise ratio
-  noise reduction algorithms and spatio-temporal filtering

You need band batch and notch filters

### Wavelet transform
Choosing the number of decomposition levels is based on the dominant frequency components of the signal. The levels are chosen in such a way that the parts of the signal, correlating well with the frequencies required for classification of the signal are retained in the wavelet coefficients.

Wavelet Transform can be thought as an extension to Fourier Transform and also instead of working on a single scale (time or frequency) rather it works on multi-scale basis and also addresses the problems related to non-stationary signals

Continious wavelet transform
Discrete wavelet transform
- Single dimensional
- Multi dimensional
  - One paper used level 3

## Good papers
- https://biomedpharmajournal.org/vol10no4/wavelet-transform-for-classification-of-eeg-signal-using-svm-and-ann/
- https://www.researchgate.net/publication/3717417_Classification_of_EEG_signals_using_the_wavelet_transform
- https://www.sciencedaily.com/releases/2010/03/100319210631.htm