# ELENG 225D

[Distilled Whisper models](https://huggingface.co/distil-whisper)

```python
torch.save(model.state_dict(), model_file + str(epoch) + ".pt")
model.load_state_dict(torch.load(model_file + str(num_epochs - 1) + ".pt"))
```
