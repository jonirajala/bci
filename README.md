# Studying brains and bci devices


e
## Good papers
- https://biomedpharmajournal.org/vol10no4/wavelet-transform-for-classification-of-eeg-signal-using-svm-and-ann/






P300??
- P300 refers to a spike in activity approximately 300ms following presentation of the target stimulus, which is alternated with standard stimuli to create an ‘oddball’ paradigm, which is most commonly auditory. In this paradigm, the subject must respond only to the infrequent target stimulus rather than the frequent standard stimulus. The amplitude of the P300 response is proportional to the amount of attentional resource devoted to the task and the degree of information processing required, while the latency is considered a measure of stimulus classification speed, unrelated to behavioural response time.

Emotiv EEG headset

EEG:llä voidaan mitata, joko yksittäisen tapahtuman aikaansaamaa sähköistä impulssia tai erilaisia aivojen jatkuvia aaltoja (kuten alpha waves), jotka riippuvat henkilön sen hetkisestä olotilasta (esim valveilla olo tai nukkuminen)
- Eri aallot mitataan eri taajuuksina

EEG system should have 21 electrodes for a standard 10–20 measurement system though there are several electrode caps containing different numbers of electrodes (19, 32, 64, up to 256 electrodes)

The EEG signal is measured across two electrodes among which one is the
 reference electrode. Reference electrode recording is an electrode, relative to which
 the electric brain potentials in all other electrodes are measured and hence it should
 be placed on a presumed “inactive” zone on the scalp region.  Alternatively, the EEG signals are recorded onall the scalp electrodes making all the scalp electrode as a reference and the EEG signals are estimated by computing the average reference as a mean of all electrodes measurements [107].

A number of computational techniques are available for dimensionality reduction.These include principal component analysis (PCA), single value decomposition (SVD), and canonical correlation analysis (CCA) etc. These three examples of dimensionality reduction methods are each discussed below.

Biophysiological data may be described via a number of different feature types.When considering neurological data measured by, for example, the EEG or ECoG there are three broad groups of features that may be extracted. These are features based upon the amplitude of the data, features based upon the frequency content of the data, and features based upon the phase content of the data [38, 28]. It’s also possible to consider feature types in which two or more types of feature are combined. For example, time-frequency features may be used to describe changes in amplitude of the data across different frequency bands.

On laite jolla voidaan mitata ihmisen ihon sähkönjohtavuuden muutoksia joka on hyvä mittari hermostuneisuudellw/ahdistuneisuudelle ( kalvaanista ihoreaktiota)

Since EEG signal frequency generally lies within the 0.1–100 Hz

Apart from the motor activity itself, imagination of motion or Motor Imagery (MI) also creates similar detectable responses but of lower intensity. Since MI can be performed without actual movement, it can be used as a control signal for a BCI system [29]

Mitä enemmän neuroneita mittataan sitä tarkempia predictioneita saadaan
- 20 neuronia piste, jonka jälkeen tarkkuus laskee rajusti
- 1 neuronilla ei voida ennustaa ollenkaan

Asentamalla just syntyneelle eliölle joku sensori kuten infrapunasensori päähän, joka antaa sähköimpulsseja aivoille kun se vastaanottaa signaaleja, voidaan aivot saada omaksumaan tämä laite ja prosessoimaan luonnollisesti näitä signaaleja
- Näin voidaan luoda helposti esim kaukoohjattavia eliöitä
FMRI
- Mittaa veren happipitoisuutta hermosolujen lähellä
- fMRI is capable of detecting activity in deep cortical and subcortical regions,
MRI
- Mittaa aivojen rakennetta magneetti kentän avulla
MEG
- Mittaa aivosähkökäyriä mageneetin avulla
-  MEG measures weak magnetic signals produced by neuronal populations using Superconducting Quantum Interference Devices (SQUIDs).
fNIRS
- NIRS estimates the concentration of hemoglobin from changes in absorption of near infrared light. As light moves or propagates through the head, it is alternately scattered or absorbed by the tissue through which it travels.
- allowing measurements of concentration changes in both oxygenated and deoxygenated hemoglobin.
-  fNIRS is only able to detect NIR light that penetrates the first few centimeters of cortical tissue,
- KERNEL
- Oxyganated and deoxygenated Hemoglobin and blood have different optical properties
	- They absorb near infrared light differently

In terms of temporal resolution, the hemodynamic response lags behind the actual
 neuronal firing with a delay to maximum response of 6–12 s causing a consequent
 delay
spatial resolution refers to the capacity a technique has to tell you exactly which area of the brain is active, while temporal resolution describes its ability to tell you exactly when the activation happened.


Ihmisten tunteita on kyetty mittaamaan ja ennustamaan 84% tarkkuudella (eeg + svm)
- Laite, joka aina tunnistaa sun tunteet esim surun ja sit sen mukaan yrittää saada sulle paremman olon -> ainainen iloisuus

Independent component analysis

Before the eeg data can be used in the NN, there must be some preprocessing to raise the signal-to-noise ratio
-  noise reduction algorithms and spatio-temporal filtering


How is the egg data inputted to for example the NN
- One sample at the time or for example vector consisting 100 samples
	- The latter could present more realistic view for the NN. It could “see” the whole graph

These electrodes are made of silver chloride (AgCl). A gel is used which
 creates a conductive path between the skin and the electrode for the flow of current.
 Electrodes that do not use gels, called ‘dry’ electrodes are made of materials such as
 titanium and stainless-steel.

You need band batch and notch filters

Applications:
- Control flow of water with your mind - relaxing


YouTube comments on sentdex’s bci video:
-  recommend using stationary wavelet transforms on the raw data instead of FFT.
- Sentdex it won't be as simple as just plugging in fft and expecting a good output because the data itself has a heavy amount of noise. Your preprocessing must be solid. Just doing notch doesn't work. You should look at PCA and ICA to preprocess your data and then try to train a model. You have to go through artifact removal process and also the problem you have started with is not a beginner friendly one.Also instead of FFT you should use wavelet transforms.Can you also please upload the raw data and not just the FFT data
- You might get better data if you show yourself flash cards. There's tons of good research that says the same neurons are activated in the same sequence whether the stimulus is internal (think left/right) or external (respond left/right) and it should be less affected by the fatigue you described.


Facial recognition and sound recognition is possible via brain signals/waves
- Terminator view

Game which adjusts the difficulty level based on your mental state
- If too relaxed make it harder or if too frustrated make it easier
	- -> Keep player engaged

One electrode measures about 100 million - 1 billion neurons

Electrode’s size has big effect in intracranial measurements but on in scalp
- bigger electrode measures more neurons

10million neurons in 1cm is theoretical limit

It would be good if the natural brain oscallations can be filtered out when measuring evoked potentials
- method called ”averaging out”

Animal testing
- we can stick a wire to brain of a cochroach and perform deep brain measurements
- How to keep the bug still? 
- This would allow reading and writing

Reference electrode
- If the resistance of the current path between electrodes is too large, current through the measuring circuit will be too small to meet the sensitivity requirements
- Because of this the reference cant be for example wall etc


Wavelet transform
- Usual Q factor for eeg applications is 0.8
- Usually morlet in egg

ICA

PCA
Beta waves are responsible for problem solving or decision making and
associated with attention. Alpha waves are associated with now and meditation.
Maybe it it possible to measure different concentration levels by doing different tasks
- Reading boring book will have low level of concentration
- Programming will have high level of concentration
Collect data and after that test what filter causes s best predictions
