# urbansound dataset 

https://serv.cusp.nyu.edu/projects/urbansounddataset/urbansound.html

##Description

This dataset contains 1302 labeled sound recordings. Each recording is labeled with the start and end times of sound events from 10 classes: air_conditioner, car_horn, children_playing, dog_bark, drilling, enginge_idling, gun_shot, jackhammer, siren, and street_music. Each recording may contain multiple sound events, but for each file only events from a single class are labeled. The classes are drawn from the urban sound taxonomy. For a detailed description of the dataset and how it was compiled please see our paper.


All recordings were obtained from www.freesound.org. The files are pre-sorted into folders by the class of events that have been annotated for each file.

In addition to the sound recordings, each audio file is accompanied by two metadata files: a JSON file containing the metadata provided by the Freesound API (description, tags, id, format, etc.); and a CSV file containing the sound event annotations.

## Audio Files Included

1302 audio files of field recordings (see description above). The audio codec, sampling rate, bit depth, and number of channels are the same as those of the original file uploaded to Freesound (and hence may vary from file to file).

## Meta-data Files Included

Every audio file (e.g. 12345.wav) is accompanied by two metadata files (e.g. 12345.json and 12345.csv).

### JSON file
Contains the file metadata provided by the Freesound API in JSON format. Includes fields such as: analysis_frames, analysis_stats, avg_rating, bitdepth, bitrate, channels, created, description, duration, filesize, geotag, id, license, num_comments, num_downloads, num_ratings, original_filename, pack, preview-hq-mp3, preview-hq-ogg, preview-lq-mp3, preview-lq-ogg, ref, samplerate, serve, similarity, spectral_l, spectral_m, tags, type, url, user, waveform_l, waveform_m.

### CSV file
Contains the annotations of sound events. Each line represents an event, and contains four comma-separated values: start time, end time, salience label and class label. The salience label is a (subjective) assessment of the sound's presence: 1 = foreground, 2 = background. The class label takes one of ten values: air_conditioner, car_horn,  children_playing, dog_bark, drilling, engine_idling, gun_shot, jackhammer, siren, street_music. Note that for each file only events from a single class (indicated by the name of the folder where the file resides) are annotated.

## Download 
 
  [Form](https://serv.cusp.nyu.edu/projects/urbansounddataset/download-urbansound8k.html)

Please [acknowledge](http://urbansounddataset.weebly.com/index.html#acknowledge)
this dataset in academic research.

