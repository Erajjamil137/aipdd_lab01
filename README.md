# AI-316 Lab 03 - Computer Vision Prototyping & Object Detection

## Setup
```
pip install -r requirements.txt
```
Keep `utils.py` in the same folder as the scripts. YOLO weights (`yolov8n.pt`, `yolov8m.pt`)
download automatically on first run (internet needed once).

## Run
| Task | Command | Own image option |
|---|---|---|
| 1 Traffic preprocessing | `python task1_preprocessing.py --image traffic.jpg` | yes |
| 2 Defect detection | `python task2_defect_detection.py --image product.jpg` | yes (synthetic if omitted) |
| 3 Medical edges | `python task3_medical_edges.py --image xray.png` | yes (synthetic phantom if omitted) |
| 4 YOLO n vs m | `python task4_yolo_benchmark.py --image test.jpg` | yes |
| 5 Retail count | `python task5_retail_inventory.py --image shelf.jpg --classes 39` | yes (47 = apple) |
| 6 ROI intrusion | `python task6_roi_intrusion.py --image cam.jpg --roi "100,300;600,300;600,700;100,700"` | yes |
| 7 Live dashboard | `python live_detection.py` (q = quit, s = save) | webcam / `--source video.mp4` |
| 8 Surveillance log | `python task8_surveillance.py` (q = quit) | webcam / `--source video.mp4` |

If an image is missing, scripts fall back to a sample image so they still run.
Results are saved in `outputs/` (Tasks 1-6), `captures/` (Task 7), `alerts/` + `events.log` (Task 8).
Tasks 1-6 are also in `LAB03_Tasks1-6.ipynb` (Jupyter Notebook, needed for Task 3 deliverable).

## Notes
- Task 2: tune `LOWER_HSV` / `UPPER_HSV` for your own defect colour.
- Task 3: noise is added synthetically so the filters can be scored (PSNR, edge F1) against the clean image.
- Task 8: `--cooldown` (default 2 s) stops the log being flooded every frame.
