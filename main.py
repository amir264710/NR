from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio
from calculate_SNR import calculate_snr

model = separator.from_hparams(source="speechbrain/sepformer-wham-enhancement", savedir='pretrained_models/sepformer-wham-enhancement', run_opts={"device":"cuda"})

# for custom file, change path
est_sources = model.separate_file(path='noiseyTestAudio.wav')

torchaudio.save("modelDenoised.wav", est_sources[:, :, 0].detach().cpu(), 8000)